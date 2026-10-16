"""Confirmatory ND/NN tests: HN (held-out arXiv archives), Test A (bioRxiv, medRxiv) and Test B (dose-response).

Specification: pre-registration sections 5-7 and Amendment 1, with Deviations 1 (estimates computed before the
author's blind validation) and 2 (sampled classification; design in nd_design.py). Every result is labelled
"pending human validation (Deviation 1)".

Monthly class counts are estimated from the classified samples: for each stratum (archive- or server-month),
ND_hat = N x n_ND / n and NN_hat = N x n_NN / n, where N is the frame size and n the number of classified papers;
papers labelled U are left out (primary) or counted as NN (sensitivity).

HN and Test A model (Poisson pseudo-maximum likelihood), for units u (archives or servers) and classes c:
  log E[y_uct] = a_uc + b_uc * t + s_m(t) + g_uc * 1[2020-2021] + d_uc,2023 + d_uc,2024 + beta_c * 1[2025-01..2026-09]
The trends are identified from 2017-2022 (bioRxiv from 2019, medRxiv from July 2019); 2023 and 2024 have their own
effects; beta_c is the departure from trend in January 2025 - September 2026, pooled over units, and archive-specific
departures come from a second model with beta_uc. RRR = exp(beta_NN - beta_ND).
Inference: moving-block bootstrap over months (blocks of 12), which in each replicate also resamples the classified
papers within each stratum, so sampling and classification noise enter the intervals (999 replicates).
Placebo: the same estimand for 2019 (trend from 2017-2018 and 2020-2022). Power: MDE = exp(2.8 x bootstrap SE).
Decision rule (HN): supported if the pooled RRR > 1 with a 95% CI excluding 1 and the archive-specific RRR > 1 in at
least 2 of 3 archives; contradicted if the pooled RRR < 1 with a CI excluding 1; otherwise not supported.
Test A has one unit per test (the server), so the archive-specific condition does not apply and only the first
condition is used (fixed here before any estimate).
Sensitivity analyses (HN): announcement dating (identifier month; each classified paper of a submission-month
stratum carries weight N / n and is counted in its announcement month); excluding September 2026; U as NN; excluding
reviews and white papers from NN (keyword genres of stats_round1.py); excluding papers with more than 50 authors;
trend from 2017-2019 only. Test A: the same where they apply (no announcement dating, which is the posting month on
these servers; no author counts, which the harvested records lack); "reviews" are titles naming a review or
meta-analysis. Excluded papers stay in each stratum's denominator and are counted in neither class, so the
estimates are counts of the papers that remain.

Test B: exposure = ND share among classified papers of each category in 2019-2022; outcome = the category's departure
from its own trend in January 2025 - September 2026: Poisson PML of the monthly count on a linear trend, month of year,
a 2020-2021 indicator, 2023 and 2024 indicators and one post indicator, so the trend comes from the years to 2022.
Counts (nd_category_monthly*.csv, arxiv_archive_monthly.csv): held-out subcategories by first-version month from 2017;
maths subcategories by identifier month from 2019; the six HEP/nuclear archives by announcement month from 2017;
bioRxiv from 2019 and medRxiv (without COVID-19) from July 2019, by first posting.
Estimand = slope of the outcome on the ND share, servers jointly (server fixed effects) and separately; inference by
a permutation test shuffling ND shares within server (10,000 permutations) and a bootstrap over categories.
Decision rule: supported if the joint slope is negative with one-sided permutation p < 0.05 and the slope is negative
in at least 2 of the 3 servers. Sensitivity: U counted as NN in the ND share.
Usage: python3 scripts/stats_nd_tests.py LABELS_FILE [repo_dir]
"""
import csv
import gzip
import json
import math
import os
import sys
from collections import Counter, defaultdict

import numpy as np
import pandas as pd
import statsmodels.api as sm

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nd_design as D  # noqa: E402
from stats_within_field import ym_range  # noqa: E402

RNG = np.random.default_rng(D.BASE_SEED)
STATUS = "pending human validation (Deviation 1)"
POST = ("2025-01", "2026-09")


def load_labels(path):
    out = {}
    for r in csv.DictReader(gzip.open(path, "rt") if path.endswith(".gz") else open(path)):
        out[r["id"]] = r["label"]
    return out


def load_samples(repo):
    rows = []
    for fn in sorted(os.listdir(os.path.join(repo, "data/processed"))):
        if fn.startswith("nd_samples") and fn.endswith(".csv.gz"):
            rows += list(csv.DictReader(gzip.open(os.path.join(repo, "data/processed", fn), "rt")))
    sizes = {}
    for fn in sorted(os.listdir(os.path.join(repo, "data/processed"))):
        if fn.startswith("nd_frame_counts") and fn.endswith(".csv"):
            for r in csv.DictReader(open(os.path.join(repo, "data/processed", fn))):
                sizes[(r["design"], r["stratum"])] = int(r["frame_size"])
    return rows, sizes


def load_attributes(repo):
    out = {}
    for fn in sorted(os.listdir(os.path.join(repo, "data/processed"))):
        if fn.startswith("nd_sample_attributes") and fn.endswith(".csv.gz"):
            for r in csv.DictReader(gzip.open(os.path.join(repo, "data/processed", fn), "rt")):
                out[r["paper_key"]] = r
    return out


def strata(rows, sizes, labels, design, u_as_nn=False, exclude=None):
    """{(unit, month): (N, [labels of classified papers])} for one design. A paper for which exclude(key, label) is
    true keeps its place in the denominator but is counted in neither class (label X)."""
    out = {}
    by = defaultdict(list)
    for r in rows:
        if r["design"] == design and r["paper_key"] in labels:
            lab = labels[r["paper_key"]]
            if u_as_nn and lab == "U":
                lab = "NN"
            if exclude is not None and exclude(r["paper_key"], lab):
                lab = "X"
            by[r["stratum"]].append(lab)
    for (d, st), n in sizes.items():
        if d != design:
            continue
        unit, month = st.split("|") if "|" in st else (design, st)
        out[(unit, month)] = (n, by.get(st, []))
    return out


def counts_by_announcement(rows, sizes, labels, design, attrs):
    """Estimated counts by announcement month: each classified paper of a stratum (unit, submission month) with frame
    size N and n classified papers carries weight N / n and is counted in its announcement month."""
    by = defaultdict(list)
    for r in rows:
        if r["design"] == design and r["paper_key"] in labels:
            by[r["stratum"]].append(r["paper_key"])
    acc = defaultdict(float)
    units, months = set(), set()
    for (d, st), n in sizes.items():
        if d != design or not by.get(st):
            continue
        unit = st.split("|")[0] if "|" in st else design
        units.add(unit)
        for k in by[st]:
            m = attrs[k]["announce_month"]
            months.add(m)
            if labels[k] in ("ND", "NN"):
                acc[(unit, m, labels[k])] += n / len(by[st])
    return pd.DataFrame([{"unit": u, "month": m, "class": c, "y": acc.get((u, m, c), 0.0)}
                         for u in sorted(units) for m in sorted(months) for c in ("ND", "NN")])


def class_counts(st, resample=False):
    """Estimated monthly counts per unit and class."""
    rows = []
    for (unit, month), (n, labs) in st.items():
        if resample and labs:
            labs = list(RNG.choice(labs, len(labs)))
        k = len(labs)
        for c in ("ND", "NN"):
            y = n * sum(1 for x in labs if x == c) / k if k else np.nan
            rows.append({"unit": unit, "month": month, "class": c, "y": y})
    return pd.DataFrame(rows).dropna()


def fit(df, post=POST, trend_end="2022-12", placebo_year=None, pooled=True, trend_years=None):
    """Poisson PML of the HN/Test A model; returns {class: beta} (pooled) or {(unit, class): beta}."""
    df = df.copy()
    df["year"] = df["month"].str[:4].astype(int)
    df["m"] = df["month"].str[5:7].astype(int)
    df["t"] = (df["year"] - 2017) + (df["m"] - 1) / 12  # calendar time, so resampled data keep their own position
    uc = (df["unit"] + "|" + df["class"])
    X = pd.get_dummies(uc, prefix="uc", dtype=float)
    for k in sorted(uc.unique()):
        sel = (uc == k).astype(float)
        X[f"tr_{k}"] = sel * df["t"]
        X[f"cv_{k}"] = sel * df["year"].isin([2020, 2021]).astype(float)
        if placebo_year is None:
            for y in (2023, 2024):
                X[f"y{y}_{k}"] = sel * (df["year"] == y).astype(float)
    for mm in range(2, 13):
        X[f"m{mm}"] = (df["m"] == mm).astype(float)
    if placebo_year is not None:
        df = df[df["year"] <= 2022]
        X = X.loc[df.index]
        post_ind = (df["year"] == placebo_year).astype(float)
    else:
        if trend_years:  # trend from these years only: other pre-2023 years get their own effects
            for k in sorted(uc.unique()):
                sel = (uc == k).astype(float)
                for y in range(2017, 2023):
                    if y not in trend_years and y not in (2020, 2021):
                        X[f"y{y}_{k}"] = sel * (df["year"] == y).astype(float)
        post_ind = df["month"].between(*post).astype(float)
        keep = ~((df["month"] > post[1]) | ((df["month"] < post[0]) & (df["year"] >= 2025)))
        df, X, post_ind = df[keep], X[keep], post_ind[keep]
    names = []
    if pooled:
        for c in ("ND", "NN"):
            X[f"post_{c}"] = post_ind * (df["class"] == c).astype(float)
            names.append(f"post_{c}")
    else:
        for k in sorted(uc.unique()):
            X[f"post_{k}"] = post_ind * (uc.loc[df.index] == k).astype(float)
            names.append(f"post_{k}")
    X = X.loc[:, (X != 0).any(axis=0)]
    res = sm.GLM(df["y"].values, X.values, family=sm.families.Poisson()).fit()
    params = dict(zip(X.columns, res.params))
    return {n: params[n] for n in names if n in params}


def rrr(b):
    return math.exp(b["post_NN"] - b["post_ND"])


def block_bootstrap(st, reps=999, block=12, **kw):
    """Moving-block pairs bootstrap over months, drawn separately before and from January 2025 so that every
    replicate has a post period; each drawn month keeps its own covariates. In each replicate the classified papers of
    every stratum are also resampled, so sampling and classification noise enter the intervals."""
    months = sorted({m for _, m in st})
    pre = [m for m in months if m < POST[0]]
    post = [m for m in months if POST[0] <= m <= POST[1]]

    def draw(seq):
        b = min(block, len(seq))
        starts = RNG.integers(0, len(seq) - b + 1, size=math.ceil(len(seq) / b))
        return [seq[s + i] for s in starts for i in range(b)][:len(seq)]

    out = []
    for _ in range(reps):
        picked = draw(pre) + draw(post)
        frames = []
        base = class_counts(st, resample=True)
        for m in picked:
            frames.append(base[base["month"] == m])
        try:
            out.append(fit(pd.concat(frames, ignore_index=True), **kw))
        except Exception:
            continue
    return out


def summarise(point, boots, key=rrr):
    vals = np.array([key(b) for b in boots if b])
    lo, hi = np.percentile(vals, [2.5, 97.5])
    se = float(np.std(np.log(vals), ddof=1))
    return {"rr": key(point), "lo": float(lo), "hi": float(hi), "se_log": se, "mde_80": math.exp(2.8 * se),
            "n_boot": int(len(vals))}


def hn_like(rows, sizes, labels, design, units, attrs, reps=999):
    st = strata(rows, sizes, labels, design)
    point = fit(class_counts(st))
    res = {"status": STATUS, "pooled": summarise(point, block_bootstrap(st, reps=reps))}
    res["n_classified"] = dict(Counter(x for _, labs in st.values() for x in labs))
    p = res["pooled"]
    if len(units) > 1:
        by = fit(class_counts(st), pooled=False)
        res["by_unit"] = {u: math.exp(by[f"post_{u}|NN"] - by[f"post_{u}|ND"]) for u in units
                          if f"post_{u}|NN" in by and f"post_{u}|ND" in by}
        units_ok = sum(v > 1 for v in res["by_unit"].values()) >= 2
    else:
        units_ok = True  # one unit: the archive-specific condition does not apply
    res["placebo_2019"] = rrr(fit(class_counts(st), placebo_year=2019))
    res["decision"] = ("supported" if p["rr"] > 1 and p["lo"] > 1 and units_ok
                       else "contradicted" if p["rr"] < 1 and p["hi"] < 1 else "not supported")
    sens = {
        "excluding_september_2026": rrr(fit(class_counts(st), post=("2025-01", "2026-08"))),
        "U_as_NN": rrr(fit(class_counts(strata(rows, sizes, labels, design, u_as_nn=True)))),
        "trend_2017_2019_only": rrr(fit(class_counts(st), trend_years={2017, 2018, 2019})),
    }
    genres = ("review", "white_paper") if design == "HN" else ("review",)
    sens["excluding_reviews_from_NN"] = rrr(fit(class_counts(strata(
        rows, sizes, labels, design, exclude=lambda k, lab: lab == "NN" and attrs[k]["genre"] in genres))))
    if design == "HN":
        sens["announcement_dating"] = rrr(fit(counts_by_announcement(rows, sizes, labels, design, attrs)))
        sens["excluding_over_50_authors"] = rrr(fit(class_counts(strata(
            rows, sizes, labels, design, exclude=lambda k, lab: int(attrs[k]["n_authors"] or 0) > 50))))
    res["sensitivity"] = sens
    return res


def departure(counts, first):
    """Log ratio of observed to trend output in January 2025 - September 2026 for one monthly series."""
    months = ym_range(first, D.LAST)
    y = np.array([counts.get(m, 0) for m in months], float)
    yr = np.array([int(m[:4]) for m in months])
    mo = np.array([int(m[5:7]) for m in months])
    X = np.column_stack([np.ones(len(months)), (yr - 2017) + (mo - 1) / 12]
                        + [(mo == k).astype(float) for k in range(2, 13)]
                        + [np.isin(yr, [2020, 2021]).astype(float), (yr == 2023).astype(float),
                           (yr == 2024).astype(float), (yr >= 2025).astype(float)])
    return float(sm.GLM(y, X, family=sm.families.Poisson()).fit().params[-1])


def testb_outcomes(repo):
    series = defaultdict(dict)
    for fn in sorted(os.listdir(os.path.join(repo, "data/processed"))):
        if fn.startswith("nd_category_monthly") and fn.endswith(".csv"):
            for r in csv.DictReader(open(os.path.join(repo, "data/processed", fn))):
                series[(r["server"], r["category"])][r["month"]] = int(r["papers"])
    for r in csv.DictReader(open(os.path.join(repo, "data/raw/arxiv_archive_monthly.csv"))):
        if r["archive"] in D.TESTB_ARXIV_ARCHIVES:
            series[("arxiv", r["archive"])][f"{r['year']}-{int(r['month']):02d}"] = int(r["new"])
    first = {"biorxiv": D.BIO_FIRST, "medrxiv": D.MED_FIRST}
    out = {}
    for (server, cat), counts in series.items():
        f = first.get(server, "2019-01" if cat.startswith("math.") else D.HN_FIRST)
        out[(server, cat)] = departure(counts, f)
    return out


def dose_response(rows, labels, outcomes, perms=10000, u_as_nn=False):
    """Test B: slope of the 2025-26 departure (log ratio) on the 2019-2022 ND share across categories."""
    cats = []
    for r in rows:
        if r["design"].startswith("B-") and r["paper_key"] in labels:
            lab = labels[r["paper_key"]]
            cats.append((r["design"][2:], r["stratum"], "NN" if u_as_nn and lab == "U" else lab))
    share = defaultdict(lambda: [0, 0])
    for server, cat, lab in cats:
        if lab in ("ND", "NN"):
            share[(server, cat)][0] += lab == "ND"
            share[(server, cat)][1] += 1
    df = pd.DataFrame([{"server": s, "category": c, "nd_share": v[0] / v[1], "n": v[1],
                        "outcome": outcomes.get((s, c))} for (s, c), v in share.items() if v[1]]).dropna()

    def slope(d):
        X = pd.get_dummies(d["server"], dtype=float)
        X["nd_share"] = d["nd_share"]
        return float(sm.OLS(d["outcome"], X).fit().params["nd_share"])

    obs = slope(df)
    null = []
    for _ in range(perms):
        d = df.copy()
        d["nd_share"] = d.groupby("server")["nd_share"].transform(lambda x: RNG.permutation(x.values))
        null.append(slope(d))
    boot = []
    for _ in range(999):
        d = pd.concat([g.sample(len(g), replace=True, random_state=int(RNG.integers(1e9))) for _, g in df.groupby("server")])
        try:
            boot.append(slope(d))
        except Exception:
            pass
    by_server = {}
    for s, g in df.groupby("server"):
        if len(g) >= 3:
            by_server[s] = {"n_categories": int(len(g)),
                            "slope": float(sm.OLS(g["outcome"], sm.add_constant(g["nd_share"])).fit().params["nd_share"])}
    p_perm = float((np.sum(np.array(null) <= obs) + 1) / (perms + 1))  # one-sided: prediction is a negative slope
    neg = sum(v["slope"] < 0 for v in by_server.values())
    return {"status": STATUS, "n_categories": int(len(df)), "slope_joint": obs,
            "ci_bootstrap": [float(np.percentile(boot, 2.5)), float(np.percentile(boot, 97.5))],
            "p_permutation_one_sided": p_perm, "by_server": by_server,
            "decision": "supported" if obs < 0 and p_perm < 0.05 and neg >= 2 else "not supported",
            "categories": df.to_dict("records")}


def main():
    args = sys.argv[1:]
    labels = load_labels(args[0])
    repo = args[1] if len(args) > 1 else "."
    rows, sizes = load_samples(repo)
    attrs = load_attributes(repo)
    out_path = os.path.join(repo, "data/processed/stats/nd_tests.json")
    out = json.load(open(out_path)) if os.path.exists(out_path) else {}
    designs = {r["design"] for r in rows}
    if "A-medrxiv" in designs:
        out["testA_medrxiv"] = hn_like(rows, sizes, labels, "A-medrxiv", ["A-medrxiv"], attrs)
    if "A-biorxiv" in designs:
        out["testA_biorxiv"] = hn_like(rows, sizes, labels, "A-biorxiv", ["A-biorxiv"], attrs)
    if "HN" in designs:
        out["HN"] = hn_like(rows, sizes, labels, "HN", D.HN_ARCHIVES, attrs)
    if {"B-arxiv", "B-biorxiv", "B-medrxiv"} <= designs:
        outcomes = testb_outcomes(repo)
        out["testB"] = dose_response(rows, labels, outcomes)
        out["testB"]["sensitivity_U_as_NN"] = {k: v for k, v in dose_response(rows, labels, outcomes, u_as_nn=True)
                                               .items() if k in ("slope_joint", "p_permutation_one_sided", "by_server")}
    json.dump(out, open(out_path, "w"), indent=1, default=float)
    print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk in ("pooled", "decision", "placebo_2019")}
                      for k, v in out.items()}, indent=1, default=float))


if __name__ == "__main__":
    main()
