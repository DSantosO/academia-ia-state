"""Confirmatory ND/NN tests: HN (held-out arXiv archives), Test A (bioRxiv, medRxiv) and Test B (dose-response).

Specification: pre-registration sections 5-7 and Amendment 1, with Deviations 1 (estimates computed before the
author's blind validation), 2 (sampled classification; design in nd_design.py) and 3 with its addendum (essay branch,
commits 8932773 and 80a2ef2). Every result is labelled "pending human validation (Deviation 1)".

Sealing (Deviation 3, D3i): the results are written only to validation/sealed/nd_results_<test>.json.gz and are not
printed; the script prints the file names and their SHA-256 hashes. They are opened after the author's validation
coding is committed.

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
Placebo: the same estimand for 2019 (trend from 2017-2018 and 2020-2022); on bioRxiv and medRxiv, whose series start
in 2019, it is reported but not interpreted (D3n). Power: MDE = exp(2.8 x bootstrap SE).
Decision rule (HN): supported if the pooled RRR > 1 with a 95% CI excluding 1 and the archive-specific RRR > 1 in at
least 2 of 3 archives; contradicted if the pooled RRR < 1 with a CI excluding 1; otherwise not supported.
Test A has one unit per test (the server), so the archive-specific condition does not apply (D3b).

Level-based companion (D3e): unit x class fixed effects and unit x class month-of-year effects, no trends, own
indicators for 2020-2021, 2023 and 2024, so the base is the remaining months before 2025 (HN: 2017-2019 and 2022;
bioRxiv: 2019 and 2022; medRxiv: July-December 2019 and 2022). For Test A it is reported beside the registered
estimate, with the flag "dependent on the counterfactual" when the two disagree (one CI excludes 1 and the other does
not, or the points lie on opposite sides of 1); for HN it is sensitivity 7. For medRxiv it is post hoc.

Sensitivity analyses. HN: (1) announcement dating (identifier month; each classified paper of a submission-month
stratum carries weight N / n and is counted in its announcement month); (2) excluding September 2026; (3) U as NN;
(4) excluding reviews and white papers from NN (keyword genres of stats_round1.py); (5) excluding papers with more
than 50 authors; (6) trend from 2017-2019 only; (7) level-based; (8) without astro-ph, and leaving out each archive in
turn (D3l); (9) astro-ph without papers naming DESI, Euclid, Rubin or LSST (D3l); (10) without AI-topic papers (D3m).
Test A: (2), (3), (4) with "reviews" = titles naming a review or meta-analysis, (6) and (10); (1) and (5) do not apply.
Excluded papers stay in each stratum's denominator and are counted in neither class, so the estimates are counts of
the papers that remain. Misclassification (D3g): the interval is recomputed with papers relabelled at random in each
bootstrap draw, using each domain's test-retest transition matrix (first run -> second run): arXiv, a second blind run
of the 200 arXiv validation papers; bioRxiv, the 100 bioRxiv validation papers; medRxiv, the 900 medRxiv sample papers
and the 100 medRxiv validation papers (second Deviation 3 addendum).

Test B: exposure = ND share among classified papers of each category in 2019-2022; outcome = the category's departure
in January 2025 - September 2026. Registered outcome: Poisson PML of the monthly count on a linear trend, month of
year, a 2020-2021 indicator, 2023 and 2024 indicators and one post indicator. Level-based outcome (D3e): the same
without the trend, from 2019 (medRxiv from July 2019), so the base is 2019 and 2022.
Counts (nd_category_monthly*.csv, arxiv_archive_monthly.csv): held-out subcategories by first-version month from 2017;
maths subcategories by identifier month from 2019; the six HEP/nuclear archives by announcement month from 2017;
bioRxiv from 2019 and medRxiv (without COVID-19) from July 2019, by first posting.
Category sets (D3d): primary (decides the verdict) = the 15 held-out arXiv subcategories, all bioRxiv categories and
the medRxiv categories in the frame (at least 150 eligible papers in 2019-2022, D3k); sensitivity = the primary set
plus the maths subcategories and the six HEP/nuclear archives.
Estimand = slope of the outcome on the ND share, servers jointly (server fixed effects) and separately; inference by
a permutation test shuffling ND shares within server (10,000 permutations; one-sided p decides, two-sided p reported,
D3c) and a bootstrap over categories. Decision rule: supported if the joint slope is negative with one-sided
permutation p < 0.05 and the slope is negative in at least 2 of the 3 servers. Sensitivities: U counted as NN;
level-based outcome (flag as for Test A, on the slope's sign and bootstrap interval); without AI-topic papers in
exposure and outcome (primary set); the bootstrap with relabelling (D3g).
A test is estimated only when every sampled paper of its designs has a label (coverage is reported).
Usage: python3 scripts/stats_nd_tests.py LABELS_FILE[,LABELS_FILE...] [repo_dir] [--tests HN,A-biorxiv,...]
"""
import csv
import gzip
import hashlib
import io
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
CLASSES = ("ND", "NN", "U")
HELD_OUT = ("cond-mat.", "astro-ph.", "quant-ph")


def reseed(name):
    global RNG
    RNG = np.random.default_rng(D.seed("estimation", name))


def load_labels(paths):
    out = {}
    for path in paths.split(","):
        for r in csv.DictReader(gzip.open(path, "rt") if path.endswith(".gz") else open(path)):
            out[r.get("paper_key") or r["id"]] = r["label"]
    return out


def load_samples(repo):
    rows = []
    for fn in sorted(os.listdir(os.path.join(repo, "data/processed"))):
        if fn.startswith("nd_samples") and fn.endswith(".csv.gz"):
            rows += list(csv.DictReader(gzip.open(os.path.join(repo, "data/processed", fn), "rt")))
    sizes = {}
    for fn in sorted(os.listdir(os.path.join(repo, "data/processed"))):
        if fn.startswith("nd_frame_counts") and fn.endswith(".csv"):
            with open(os.path.join(repo, "data/processed", fn)) as f:
                for r in csv.DictReader(f):
                    sizes[(r["design"], r["stratum"])] = int(r["frame_size"])
    return rows, sizes


def load_attributes(repo):
    out = {}
    for fn in sorted(os.listdir(os.path.join(repo, "data/processed"))):
        if fn.startswith("nd_sample_attributes") and fn.endswith(".csv.gz"):
            for r in csv.DictReader(gzip.open(os.path.join(repo, "data/processed", fn), "rt")):
                out[r["paper_key"]] = r
    return out


def retest_kernel(paths):
    """D3g: P(label in a second run | label in the first run), pooled over the test-retest tables."""
    counts = defaultdict(Counter)
    for path in paths:
        with (gzip.open(path, "rt") if path.endswith(".gz") else open(path)) as f:
            table = json.load(f)["table_first_by_second"]
        for a in CLASSES:
            for b in CLASSES:
                counts[a][b] += table[a][b]
    return {a: ([b for b in CLASSES], np.array([counts[a][b] for b in CLASSES], float) / sum(counts[a].values()))
            for a in CLASSES if sum(counts[a].values())}


def relabel(labs, kernel):
    """Relabel each paper at random from its row of the test-retest transition matrix."""
    labs = np.array(labs, dtype=object)
    out = labs.copy()
    for a, (choices, p) in kernel.items():
        idx = np.flatnonzero(labs == a)
        if len(idx):
            out[idx] = np.array(choices, dtype=object)[RNG.choice(len(choices), size=len(idx), p=p)]
    return list(out)


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


def only_units(st, units):
    return {k: v for k, v in st.items() if k[0] in units}


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


def class_counts(st, resample=False, kernel=None):
    """Estimated monthly counts per unit and class; with resample, the classified papers of each stratum are drawn
    with replacement, and with kernel they are then relabelled at the test-retest rates (D3g)."""
    rows = []
    for (unit, month), (n, labs) in st.items():
        if resample and labs:
            labs = list(RNG.choice(labs, len(labs)))
        if kernel is not None and labs:
            labs = relabel(labs, kernel)
        k = len(labs)
        for c in ("ND", "NN"):
            y = n * sum(1 for x in labs if x == c) / k if k else np.nan
            rows.append({"unit": unit, "month": month, "class": c, "y": y})
    return pd.DataFrame(rows).dropna()


def _post_terms(X, df, uc, post_ind, pooled):
    names = []
    if pooled:
        for c in ("ND", "NN"):
            X[f"post_{c}"] = post_ind * (df["class"] == c).astype(float)
            names.append(f"post_{c}")
    else:
        for k in sorted(uc.unique()):
            X[f"post_{k}"] = post_ind * (uc.loc[df.index] == k).astype(float)
            names.append(f"post_{k}")
    return names


def _glm(y, X, names):
    X = X.loc[:, (X != 0).any(axis=0)]
    res = sm.GLM(y, X.values, family=sm.families.Poisson()).fit()
    params = dict(zip(X.columns, res.params))
    return {n: params[n] for n in names if n in params}


def fit(df, post=POST, trend_end="2022-12", placebo_year=None, pooled=True, trend_years=None):
    """Poisson PML of the registered HN/Test A model; returns {class: beta} (pooled) or {(unit, class): beta}."""
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
    names = _post_terms(X, df, uc, post_ind, pooled)
    return _glm(df["y"].values, X, names)


def fit_level(df, post=POST, pooled=True):
    """Level-based companion (D3e): unit x class fixed and month-of-year effects, own 2020-2021, 2023 and 2024
    indicators, no trends; the base is the other months before 2025."""
    df = df.copy()
    df["year"] = df["month"].str[:4].astype(int)
    df["m"] = df["month"].str[5:7].astype(int)
    keep = ~((df["month"] > post[1]) | ((df["month"] < post[0]) & (df["year"] >= 2025)))
    df = df[keep]
    uc = (df["unit"] + "|" + df["class"])
    X = pd.get_dummies(uc, prefix="uc", dtype=float)
    for k in sorted(uc.unique()):
        sel = (uc == k).astype(float)
        for mm in range(2, 13):
            X[f"m{mm}_{k}"] = sel * (df["m"] == mm).astype(float)
        X[f"cv_{k}"] = sel * df["year"].isin([2020, 2021]).astype(float)
        for y in (2023, 2024):
            X[f"y{y}_{k}"] = sel * (df["year"] == y).astype(float)
    post_ind = df["month"].between(*post).astype(float)
    names = _post_terms(X, df, uc, post_ind, pooled)
    return _glm(df["y"].values, X, names)


def rrr(b):
    return math.exp(b["post_NN"] - b["post_ND"])


def block_bootstrap(st, reps=999, block=12, fitter=fit, kernel=None, **kw):
    """Moving-block pairs bootstrap over months, drawn separately before and from January 2025 so that every
    replicate has a post period; each drawn month keeps its own covariates. In each replicate the classified papers of
    every stratum are also resampled (and, with kernel, relabelled), so sampling and classification noise enter the
    intervals."""
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
        base = class_counts(st, resample=True, kernel=kernel)
        frames = [base[base["month"] == m] for m in picked]
        try:
            out.append(fitter(pd.concat(frames, ignore_index=True), **kw))
        except Exception:
            continue
    return out


def summarise(point, boots, key=rrr):
    vals = np.array([key(b) for b in boots if b])
    lo, hi = np.percentile(vals, [2.5, 97.5])
    se = float(np.std(np.log(vals), ddof=1))
    return {"rr": key(point), "lo": float(lo), "hi": float(hi), "se_log": se, "mde_80": math.exp(2.8 * se),
            "n_boot": int(len(vals))}


def disagree(a, b, null=1.0, est="rr"):
    """Deviation 3, D3e: the registered and level-based estimates disagree if one interval excludes the null and the
    other does not, or if the points lie on opposite sides of the null."""
    def excludes(s):
        return s["lo"] > null or s["hi"] < null
    return excludes(a) != excludes(b) or (a[est] - null) * (b[est] - null) < 0


def hn_like(rows, sizes, labels, design, units, attrs, kernel, reps=999, registered=True):
    """HN (three archives) or Test A (one server). With registered=False the registered estimate is not recomputed
    (Test A medRxiv, computed at dacd064) and only its companions and the added sensitivities are produced."""
    reseed(design)
    st = strata(rows, sizes, labels, design)
    res = {"status": STATUS, "n_classified": dict(Counter(x for _, labs in st.values() for x in labs))}
    point = fit(class_counts(st))
    if registered:
        res["pooled"] = summarise(point, block_bootstrap(st, reps=reps))
        p = res["pooled"]
        if len(units) > 1:
            by = fit(class_counts(st), pooled=False)
            res["by_unit"] = {u: math.exp(by[f"post_{u}|NN"] - by[f"post_{u}|ND"]) for u in units
                              if f"post_{u}|NN" in by and f"post_{u}|ND" in by}
            units_ok = sum(v > 1 for v in res["by_unit"].values()) >= 2
        else:
            units_ok = True  # one unit: the archive-specific condition does not apply (D3b)
        res["decision"] = ("supported" if p["rr"] > 1 and p["lo"] > 1 and units_ok
                           else "contradicted" if p["rr"] < 1 and p["hi"] < 1 else "not supported")
        res["placebo_2019"] = rrr(fit(class_counts(st), placebo_year=2019))
        if design != "HN":
            res["placebo_note"] = "reported, not interpreted: 2019 is the first year of the series (D3n)"
    else:
        res["registered"] = "computed earlier (companion commit dacd064); not recomputed here"
        res["registered_point_check"] = rrr(point)
    level = summarise(fit_level(class_counts(st)), block_bootstrap(st, reps=reps, fitter=fit_level))
    sens = {}
    if design == "HN":
        sens["7_level_based"] = level
    else:
        res["level_based"] = level
        if design == "A-medrxiv":
            res["level_based_note"] = "post hoc: added by Deviation 3 after the registered estimate was computed"
        if registered:
            res["dependent_on_counterfactual"] = disagree(res["pooled"], level)
        else:
            res["dependent_on_counterfactual"] = "see dacd064 for the registered interval"
    sens["2_excluding_september_2026"] = rrr(fit(class_counts(st), post=("2025-01", "2026-08")))
    sens["3_U_as_NN"] = rrr(fit(class_counts(strata(rows, sizes, labels, design, u_as_nn=True))))
    genres = ("review", "white_paper") if design == "HN" else ("review",)
    sens["4_excluding_reviews_from_NN"] = rrr(fit(class_counts(strata(
        rows, sizes, labels, design, exclude=lambda k, lab: lab == "NN" and attrs[k]["genre"] in genres))))
    sens["6_trend_2017_2019_only"] = rrr(fit(class_counts(st), trend_years={2017, 2018, 2019}))
    sens["10_without_ai_topic"] = rrr(fit(class_counts(strata(
        rows, sizes, labels, design, exclude=lambda k, lab: attrs[k]["ai_topic"] == "1"))))
    if design == "HN":
        sens["1_announcement_dating"] = rrr(fit(counts_by_announcement(rows, sizes, labels, design, attrs)))
        sens["5_excluding_over_50_authors"] = rrr(fit(class_counts(strata(
            rows, sizes, labels, design, exclude=lambda k, lab: int(attrs[k]["n_authors"] or 0) > 50))))
        sens["8_without_astro_ph"] = rrr(fit(class_counts(only_units(st, {"cond-mat", "quant-ph"}))))
        sens["8_leave_one_archive_out"] = {f"without_{u}": rrr(fit(class_counts(only_units(st, set(units) - {u}))))
                                           for u in units}
        sens["9_astro_ph_without_survey_words"] = rrr(fit(class_counts(strata(
            rows, sizes, labels, design,
            exclude=lambda k, lab: attrs[k]["survey_words"] == "1" and k in astro_keys(rows)))))
    else:
        sens["not_applicable"] = ["1 announcement dating (posting month is the announcement)",
                                  "5 author counts (not in the harvested records)"]
    res["sensitivity"] = sens
    res["misclassification_D3g"] = summarise(point, block_bootstrap(st, reps=reps, kernel=kernel))
    return res


_ASTRO = {}


def astro_keys(rows):
    if "keys" not in _ASTRO:
        _ASTRO["keys"] = {r["paper_key"] for r in rows if r["design"] == "HN" and r["stratum"].startswith("astro-ph|")}
    return _ASTRO["keys"]


# ----------------------------------------------------------------------------------------------------------- Test B
def _design_matrix_category(months, level):
    yr = np.array([int(m[:4]) for m in months])
    mo = np.array([int(m[5:7]) for m in months])
    cols = [np.ones(len(months))]
    if not level:
        cols.append((yr - 2017) + (mo - 1) / 12)
    cols += [(mo == k).astype(float) for k in range(2, 13)]
    cols += [np.isin(yr, [2020, 2021]).astype(float), (yr == 2023).astype(float), (yr == 2024).astype(float),
             (yr >= 2025).astype(float)]
    X = np.column_stack(cols)
    return X


def departure(counts, first, level=False):
    """Log ratio of observed to expected output in January 2025 - September 2026 for one monthly series: registered
    (trend) or level-based (D3e: from 2019, base 2019 and 2022)."""
    if level:
        first = max(first, "2019-01")
    months = ym_range(first, D.LAST)
    y = np.array([counts.get(m, 0) for m in months], float)
    X = _design_matrix_category(months, level)
    return float(sm.GLM(y, X, family=sm.families.Poisson()).fit().params[-1])


def testb_outcomes(repo, level=False, column="papers"):
    series = defaultdict(dict)
    for fn in sorted(os.listdir(os.path.join(repo, "data/processed"))):
        if fn.startswith("nd_category_monthly") and fn.endswith(".csv"):
            with open(os.path.join(repo, "data/processed", fn)) as f:
                for r in csv.DictReader(f):
                    series[(r["server"], r["category"])][r["month"]] = int(r[column])
    if column == "papers":
        with open(os.path.join(repo, "data/raw/arxiv_archive_monthly.csv")) as f:
            for r in csv.DictReader(f):
                if r["archive"] in D.TESTB_ARXIV_ARCHIVES:
                    series[("arxiv", r["archive"])][f"{r['year']}-{int(r['month']):02d}"] = int(r["new"])
    first = {"biorxiv": D.BIO_FIRST, "medrxiv": D.MED_FIRST}
    out = {}
    for (server, cat), counts in series.items():
        f = first.get(server, "2019-01" if cat.startswith("math.") else D.HN_FIRST)
        out[(server, cat)] = departure(counts, f, level=level)
    return out


def primary(server, cat):
    return server != "arxiv" or cat.startswith(HELD_OUT)


def exposure_labels(rows, labels, u_as_nn=False, exclude=None):
    """{(server, category): [labels of classified exposure papers]}."""
    out = defaultdict(list)
    for r in rows:
        if r["design"].startswith("B-") and r["paper_key"] in labels:
            lab = labels[r["paper_key"]]
            if exclude is not None and exclude(r["paper_key"]):
                continue
            out[(r["design"][2:], r["stratum"])].append("NN" if u_as_nn and lab == "U" else lab)
    return out


def share(labs):
    nd, nn = sum(x == "ND" for x in labs), sum(x == "NN" for x in labs)
    return (nd / (nd + nn), nd + nn) if nd + nn else (np.nan, 0)


def _slope(d):
    X = pd.get_dummies(d["server"], dtype=float)
    X["nd_share"] = d["nd_share"].values
    return float(sm.OLS(d["outcome"].values, X).fit().params["nd_share"])


def dose_response(expo, outcomes, keep, perms=10000, kernel=None):
    """Slope of the outcome on the 2019-2022 ND share across the categories selected by keep(server, category)."""
    recs = []
    for (s, c), labs in expo.items():
        if not keep(s, c) or (s, c) not in outcomes:
            continue
        sh, n = share(labs)
        if n:
            recs.append({"server": s, "category": c, "nd_share": sh, "n": n, "outcome": outcomes[(s, c)]})
    df = pd.DataFrame(recs)
    obs = _slope(df)
    null = []
    for _ in range(perms):
        d = df.copy()
        d["nd_share"] = d.groupby("server")["nd_share"].transform(lambda x: RNG.permutation(x.values))
        null.append(_slope(d))
    null = np.array(null)

    def boot(relabelled):
        out = []
        for _ in range(999):
            d = pd.concat([g.sample(len(g), replace=True, random_state=int(RNG.integers(1e9)))
                           for _, g in df.groupby("server")])
            if relabelled:
                d = d.copy()
                d["nd_share"] = [share(relabel(expo[(s, c)], kernel[s]))[0]
                                 for s, c in zip(d["server"], d["category"])]
            try:
                out.append(_slope(d))
            except Exception:
                pass
        return [float(np.percentile(out, 2.5)), float(np.percentile(out, 97.5))]

    by_server = {}
    for s, g in df.groupby("server"):
        if len(g) >= 3:
            by_server[s] = {"n_categories": int(len(g)),
                            "slope": float(sm.OLS(g["outcome"], sm.add_constant(g["nd_share"])).fit().params["nd_share"])}
    p_one = float((np.sum(null <= obs) + 1) / (perms + 1))  # prediction: a negative slope
    p_two = float((np.sum(np.abs(null) >= abs(obs)) + 1) / (perms + 1))
    neg = sum(v["slope"] < 0 for v in by_server.values())
    out = {"status": STATUS, "n_categories": int(len(df)), "slope_joint": obs, "ci_bootstrap": boot(False),
           "p_permutation_one_sided": p_one, "p_permutation_two_sided": p_two, "by_server": by_server,
           "decision": "supported" if obs < 0 and p_one < 0.05 and neg >= 2 else "not supported",
           "categories": df.to_dict("records")}
    if kernel is not None:
        out["ci_bootstrap_relabelled_D3g"] = boot(True)
    return out


def test_b(rows, labels, attrs, kernels, repo):
    reseed("B")
    trend = testb_outcomes(repo)
    level = testb_outcomes(repo, level=True)
    expo = exposure_labels(rows, labels)
    res = {"primary": dose_response(expo, trend, primary, kernel=kernels)}
    res["primary_level_based"] = dose_response(expo, level, primary)
    p, lv = res["primary"], res["primary_level_based"]
    res["primary_dependent_on_counterfactual"] = disagree(
        {"est": p["slope_joint"], "lo": p["ci_bootstrap"][0], "hi": p["ci_bootstrap"][1]},
        {"est": lv["slope_joint"], "lo": lv["ci_bootstrap"][0], "hi": lv["ci_bootstrap"][1]}, null=0.0, est="est")
    res["sensitivity_set"] = dose_response(expo, trend, lambda s, c: True)
    res["sensitivity_set_level_based"] = dose_response(expo, level, lambda s, c: True)
    res["primary_U_as_NN"] = dose_response(exposure_labels(rows, labels, u_as_nn=True), trend, primary)
    no_ai_expo = exposure_labels(rows, labels, exclude=lambda k: attrs[k]["ai_topic"] == "1")
    res["primary_without_ai_topic"] = dose_response(no_ai_expo, testb_outcomes(repo, column="papers_without_ai_topic"),
                                                    primary)
    for v in res.values():
        if isinstance(v, dict):
            v.pop("status", None)
    res["status"] = STATUS
    return res


# ------------------------------------------------------------------------------------------------------------- main
def seal(obj, path):
    """Write JSON as gzip with a fixed header time; return the SHA-256 of the file."""
    buf = io.BytesIO()
    with gzip.GzipFile(fileobj=buf, mode="wb", mtime=0) as g:
        g.write(json.dumps(obj, indent=1, default=float, sort_keys=True).encode())
    data = buf.getvalue()
    with open(path, "wb") as f:
        f.write(data)
    return hashlib.sha256(data).hexdigest()


def main():
    args = sys.argv[1:]
    tests = None
    if "--tests" in args:
        i = args.index("--tests")
        tests = set(args[i + 1].split(","))
        args = args[:i] + args[i + 2:]
    labels = load_labels(args[0])
    repo = args[1] if len(args) > 1 else "."
    rows, sizes = load_samples(repo)
    attrs = load_attributes(repo)
    sealed = os.path.join(repo, "validation/sealed")
    kernels = {
        "arxiv": retest_kernel([os.path.join(sealed, "classifier_retest_validation_arxiv.json.gz")]),
        "biorxiv": retest_kernel([os.path.join(sealed, "classifier_retest_validation_biorxiv.json.gz")]),
        "medrxiv": retest_kernel([os.path.join(repo, "data/processed/stats/classifier_retest_medrxiv.json"),
                                  os.path.join(sealed, "classifier_retest_validation_medrxiv.json.gz")]),
    }
    coverage = defaultdict(lambda: [0, 0])
    for r in rows:
        coverage[r["design"]][0] += r["paper_key"] in labels
        coverage[r["design"]][1] += 1
    done = {d for d, (a, b) in coverage.items() if a == b}
    print("coverage:", {d: f"{a}/{b}" for d, (a, b) in sorted(coverage.items())})
    jobs = {
        "HN": ({"HN"}, lambda: hn_like(rows, sizes, labels, "HN", D.HN_ARCHIVES, attrs, kernels["arxiv"])),
        "A-biorxiv": ({"A-biorxiv"}, lambda: hn_like(rows, sizes, labels, "A-biorxiv", ["A-biorxiv"], attrs,
                                                     kernels["biorxiv"])),
        "A-medrxiv": ({"A-medrxiv"}, lambda: hn_like(rows, sizes, labels, "A-medrxiv", ["A-medrxiv"], attrs,
                                                     kernels["medrxiv"], registered=False)),
        "B": ({"B-arxiv", "B-biorxiv", "B-medrxiv"}, lambda: test_b(rows, labels, attrs, kernels, repo)),
    }
    os.makedirs(os.path.join(repo, "validation/sealed"), exist_ok=True)
    for name, (needs, job) in jobs.items():
        if (tests is not None and name not in tests) or not needs <= done:
            continue
        res = job()
        res["coverage"] = {d: f"{coverage[d][0]}/{coverage[d][1]}" for d in sorted(needs)}
        path = os.path.join(repo, "validation/sealed", f"nd_results_{name}.json.gz")
        print("computed and sealed:", os.path.relpath(path, repo), seal(res, path))


if __name__ == "__main__":
    main()
