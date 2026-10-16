"""AI-writing marker prevalence by group, and whether marker rises predict output growth (PLOS ONE analysis, H3).

Inputs (aggregate counts only): data/raw/{biorxiv,medrxiv}_text_{main,words}.csv (harvest_rxiv_text_features.py;
bioRxiv: March and September of each year) and data/raw/arxiv_text_{main,words}.csv (aggregate_arxiv_text.py).

Marker words. The style words of Kobak et al. (2025) are filtered by a rule that uses baseline data only: words whose
pooled document frequency in 2019-2022 in the biomedical corpora (bioRxiv and medRxiv, matching the PubMed origin of
the list) is below 0.5%. The same list is then applied to every corpus. The resulting core list is written to
data/processed/stats/core_marker_words.txt. Metric: core marker words per 100 abstracts (distinct words per
abstract, summed), by group and year; non-COVID preprints only for bioRxiv and medRxiv.

Tests.
  1. Rise by group: marker rate in each year relative to the group's 2019-2022 mean (rate ratio).
  2. Same rise across groups? Poisson model of marker counts with log(abstracts) offset:
       log E[M_gt] = log N_gt + period FE + group FE + sum_k beta_k 1[g = A] 1[year = k]   (base 2022)
     exp(beta_2026) near 1 means the marker rise is similar in both groups. Newey-West/Driscoll-Kraay SEs.
  3. Does the marker rise predict output growth, and only where experiments are not the bottleneck?
     Category-level panel (bioRxiv categories, arXiv archives), years 2023-2026:
       growth_cy = a_y + b * dmarker_cy + c * dmarker_cy * experimental_c + d * experimental_c + e
     growth_cy: log(papers Jan-Sep year y) - log(papers Jan-Sep 2022); dmarker_cy: marker rate in y minus 2019-2022
     mean (per 100 abstracts); experimental_c: 1 wet-lab / experimental, 0 computational / theory, 0.5 mixed.
     OLS with standard errors clustered by category; the pooled model has year effects specific to each server.
     The arXiv panel has only 6-7 archives, too few clusters for reliable inference; it is descriptive.
  4. Lower bound on the share of LLM-processed abstracts (Kobak et al. 2025), arXiv only: the excess share of abstracts
     with at least one core marker word over its 2019-2022 trend, divided by one minus the counterfactual share.
     bioRxiv and medRxiv were aggregated by word, not by abstract, so the share with any marker is not available.
     Run order: this script writes the core list from bioRxiv and medRxiv alone; aggregate_arxiv_text.py --core then
     counts arXiv abstracts with any core word; a second run of this script reads those counts.
Usage: python3 scripts/stats_markers.py [repo_dir]
"""
import csv
import gzip
import json
import math
import os
import sys
from collections import defaultdict

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stats_within_field import COMPUTATIONAL, EXPERIMENT, THEORY, WET_LAB  # noqa: E402

BASE_YEARS = (2019, 2020, 2021, 2022)
THRESHOLD = 0.005


def load(repo, prefix, papers_col):
    main = {}
    p = os.path.join(repo, "data/raw", prefix + "_main.csv")
    if not os.path.exists(p):
        return None, None
    for r in csv.DictReader(open(p)):
        main[(r["month"], r["category"])] = int(r[papers_col])
    words = defaultdict(dict)
    wp = os.path.join(repo, "data/raw", prefix + "_words.csv")
    fh = gzip.open(wp + ".gz", "rt") if os.path.exists(wp + ".gz") else open(wp)
    for r in csv.DictReader(fh):
        words[(r["month"], r["category"])][r["word"]] = int(r.get("docs_noncovid") or r.get("docs"))
    return main, words


def core_list(corpora):
    docs, n = defaultdict(int), 0
    for main, words in corpora:
        for key, papers in main.items():
            if int(key[0][:4]) in BASE_YEARS:
                n += papers
                for w, d in words.get(key, {}).items():
                    docs[w] += d
    allw = [r["word"] for r in csv.DictReader(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                                                 "data", "raw", "kobak_style_words.csv")))]
    return sorted(w for w in allw if docs.get(w, 0) / n < THRESHOLD), n


def group_series(main, words, groups, core):
    """{group: {month: (papers, marker_words)}}"""
    out = defaultdict(lambda: defaultdict(lambda: [0, 0]))
    for (month, cat), papers in main.items():
        g = groups(cat)
        if g is None:
            continue
        out[g][month][0] += papers
        out[g][month][1] += sum(d for w, d in words.get((month, cat), {}).items() if w in core)
    return out


def yearly_rates(series):
    res = {}
    for g, months in series.items():
        yr = defaultdict(lambda: [0, 0])
        for m, (n, k) in months.items():
            yr[int(m[:4])][0] += n
            yr[int(m[:4])][1] += k
        base_n = sum(yr[y][0] for y in BASE_YEARS if y in yr)
        base_k = sum(yr[y][1] for y in BASE_YEARS if y in yr)
        base = 100 * base_k / base_n if base_n else None
        res[g] = {str(y): {"abstracts": n, "markers_per_100": 100 * k / n if n else None,
                           "ratio_to_2019_2022": (100 * k / n) / base if n and base else None}
                  for y, (n, k) in sorted(yr.items())}
        res[g]["baseline_2019_2022_per_100"] = base
    return res


def did(series, a, b, base=2022):
    rows = []
    for g in (a, b):
        for m, (n, k) in series[g].items():
            if n:
                rows.append({"g": int(g == a), "month": m, "year": int(m[:4]), "n": n, "k": k})
    df = pd.DataFrame(rows).sort_values("month")
    months = sorted(df["month"].unique())
    df["t"] = df["month"].map({m: i for i, m in enumerate(months)})
    X = pd.get_dummies(df["month"], prefix="mo", dtype=float)
    years = sorted(df["year"].unique())
    for y in years:
        if y != base:
            X[f"A_y{y}"] = (df["g"] * (df["year"] == y)).astype(float)
    X["A"] = df["g"].astype(float)
    res = sm.GLM(df["k"].values, X, family=sm.families.Poisson(), offset=np.log(df["n"].values)).fit(
        cov_type="hac-groupsum", cov_kwds={"time": df["t"].values, "maxlags": 2})
    return {str(y): {"rr": math.exp(res.params[f"A_y{y}"]), "lo": math.exp(res.params[f"A_y{y}"] - 1.96 * res.bse[f"A_y{y}"]),
                     "hi": math.exp(res.params[f"A_y{y}"] + 1.96 * res.bse[f"A_y{y}"]), "p": float(res.pvalues[f"A_y{y}"])}
            for y in years if y != base}


def any_marker_lower_bound(repo, groups):
    """Share of abstracts with at least one core marker word (arXiv only: data/raw/arxiv_text_core_any.csv), and the
    lower bound on the share of LLM-processed abstracts of Kobak et al. (2025): with p the observed share and q the
    counterfactual share, a fraction f of LLM-processed abstracts gives p = (1 - f) q + f r with r <= 1, so
    f >= (p - q) / (1 - q). q is extrapolated from a linear trend over 2019-2022 (alternative: the 2019-2022 mean)."""
    path = os.path.join(repo, "data/raw/arxiv_text_core_any.csv")
    main_path = os.path.join(repo, "data/raw/arxiv_text_main.csv")
    if not os.path.exists(path):
        return None
    n, k = defaultdict(int), defaultdict(int)
    for r in csv.DictReader(open(main_path)):
        g = groups(r["category"])
        if g:
            n[(g, int(r["month"][:4]))] += int(r["papers"])
    for r in csv.DictReader(open(path)):
        g = groups(r["category"])
        if g:
            k[(g, int(r["month"][:4]))] += int(r["papers_with_core_marker"])
    out = {}
    for g in sorted({g for g, _ in n}):
        years = sorted(y for gg, y in n if gg == g)
        share = {y: k[(g, y)] / n[(g, y)] for y in years}
        b = np.polyfit(BASE_YEARS, [share[y] for y in BASE_YEARS], 1)
        mean = float(np.mean([share[y] for y in BASE_YEARS]))
        out[g] = {}
        for y in years:
            q = float(np.polyval(b, y))
            out[g][str(y)] = {"abstracts": n[(g, y)], "share_with_marker": share[y], "counterfactual_trend": q,
                              "lower_bound_trend": (share[y] - q) / (1 - q) if y > 2022 else None,
                              "lower_bound_mean": (share[y] - mean) / (1 - mean) if y > 2022 else None}
    return out


def panel(repo, bio, arx, core):
    """Category-level growth vs marker rise, interacted with experimental intensity."""
    rows = []
    counts = defaultdict(lambda: defaultdict(int))
    for r in csv.DictReader(open(os.path.join(repo, "data/raw/biorxiv_category_monthly.csv"))):
        if int(r["month"][5:]) <= 9:
            counts[("bio", r["category"])][int(r["month"][:4])] += int(r["new_papers"])
    for r in csv.DictReader(open(os.path.join(repo, "data/raw/arxiv_archive_monthly.csv"))):
        if int(r["month"]) <= 9:
            counts[("arx", r["archive"])][int(r["year"])] += int(r["new"])
    exp_bio = lambda c: 0.0 if c in COMPUTATIONAL else 1.0 if c in WET_LAB else 0.5  # noqa: E731
    exp_arx = {**{a: 0.0 for a in THEORY}, **{a: 1.0 for a in EXPERIMENT}, "math": 0.0}
    for src, (main, words), expf in (("bio", bio, exp_bio), ("arx", arx, lambda c: exp_arx.get(c))):
        if main is None:
            continue
        rate = defaultdict(lambda: defaultdict(lambda: [0, 0]))
        for (month, cat), n in main.items():
            rate[cat][int(month[:4])][0] += n
            rate[cat][int(month[:4])][1] += sum(d for w, d in words.get((month, cat), {}).items() if w in core)
        for cat, yr in rate.items():
            e = expf(cat)
            if e is None:
                continue
            bn = sum(yr[y][0] for y in BASE_YEARS)
            if bn < 200 or counts[(src, cat)].get(2022, 0) < 100:
                continue
            base = 100 * sum(yr[y][1] for y in BASE_YEARS) / bn
            for y in (2023, 2024, 2025, 2026):
                n, k = yr.get(y, [0, 0])
                if n < 50 or not counts[(src, cat)].get(y):
                    continue
                rows.append({"source": src, "category": cat, "year": y, "experimental": e,
                             "dmarker": 100 * k / n - base,
                             "growth": math.log(counts[(src, cat)][y] / counts[(src, cat)][2022])})
    df = pd.DataFrame(rows)
    out = {"n_obs": len(df), "n_categories": int(df["category"].nunique())}
    for name, sub in (("all", df), ("biorxiv", df[df.source == "bio"]), ("arxiv", df[df.source == "arx"])):
        if len(sub) < 10:
            continue
        fe = "C(source):C(year)" if name == "all" else "C(year)"  # year effects specific to each server
        m = smf.ols(f"growth ~ {fe} + dmarker * experimental", data=sub).fit(
            cov_type="cluster", cov_kwds={"groups": pd.factorize(sub["category"])[0]})
        out[name] = {k: {"coef": float(m.params[k]), "lo": float(m.conf_int().loc[k, 0]),
                         "hi": float(m.conf_int().loc[k, 1]), "p": float(m.pvalues[k])}
                     for k in ("dmarker", "experimental", "dmarker:experimental")}
        out[name]["n"] = int(len(sub))
        out[name]["clusters"] = int(sub["category"].nunique())
        if out[name]["clusters"] < 20:
            out[name]["note"] = "fewer than 20 clusters: clustered standard errors are unreliable; descriptive only"
    return out, df


def main(repo):
    out_dir = os.path.join(repo, "data/processed/stats")
    os.makedirs(out_dir, exist_ok=True)
    bio = load(repo, "biorxiv_text", "papers_noncovid")
    med = load(repo, "medrxiv_text", "papers_noncovid")
    arx = load(repo, "arxiv_text", "papers")
    core, n_base = core_list([c for c in (bio, med) if c[0] is not None])
    open(os.path.join(out_dir, "core_marker_words.txt"), "w").write("\n".join(core) + "\n")
    results = {"core_words": core, "baseline_abstracts": n_base, "threshold": THRESHOLD}
    gbio = lambda c: "computational" if c in COMPUTATIONAL else "wet_lab" if c in WET_LAB else "mixed"  # noqa: E731
    garx = lambda c: "theory" if c in THEORY else "experiment" if c in EXPERIMENT else "maths" if c == "math" else None  # noqa: E731
    series = {}
    if bio[0] is not None:
        series["biorxiv"] = group_series(*bio, gbio, set(core))
    if arx[0] is not None:
        series["arxiv"] = group_series(*arx, garx, set(core))
    if med[0] is not None:
        series["medrxiv"] = group_series(*med, lambda c: "all", set(core))
    results["rates"] = {src: yearly_rates(s) for src, s in series.items()}
    results["did"] = {}
    if "biorxiv" in series:
        results["did"]["biorxiv_computational_vs_wet_lab"] = did(series["biorxiv"], "computational", "wet_lab")
    if "arxiv" in series:
        for a in ("theory", "maths"):
            if a in series["arxiv"] and "experiment" in series["arxiv"]:
                results["did"][f"arxiv_{a}_vs_experiment"] = did(series["arxiv"], a, "experiment")
    lb = any_marker_lower_bound(repo, garx)
    if lb:
        results["llm_share_lower_bound_arxiv"] = lb
    results["panel"], df = panel(repo, bio, arx, set(core))
    df.to_csv(os.path.join(out_dir, "marker_growth_panel.csv"), index=False)
    json.dump(results, open(os.path.join(out_dir, "marker_tests.json"), "w"), indent=1, default=float)
    print("core words:", len(core), core[:60])
    for src, r in results["rates"].items():
        for g, v in r.items():
            print(src, g, "baseline", round(v["baseline_2019_2022_per_100"] or 0, 2), {y: round(v[y]["markers_per_100"], 2)
                                                                                    for y in v if y.isdigit()})
    print(json.dumps(results["did"], indent=0, default=float)[:3000])
    print(json.dumps(results["panel"], indent=0, default=float)[:3000])


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
