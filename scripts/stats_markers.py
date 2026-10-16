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
  2. Same rise across groups? OLS of the monthly log ratio of marker rates (group A / group B) on year dummies for
     2023-2026, reference pooled 2019-2022, classical SEs and t intervals (the bioRxiv sample has 16 months, too few
     for HAC SEs). exp(beta_k) near 1 means the marker rise is similar in both groups.
  3. Does the marker rise predict output growth, and only where experiments are not the bottleneck?
     Category-level panel (bioRxiv categories, arXiv archives), years 2023-2026:
       growth_cy = a_y + b * dmarker_cy + c * dmarker_cy * experimental_c + d * experimental_c + e
     growth_cy: log(papers Jan-Sep year y) - log(papers Jan-Sep 2022); dmarker_cy: marker rate in y minus 2019-2022
     mean (per 100 abstracts); experimental_c: 1 wet-lab / experimental, 0 computational / theory, 0.5 mixed.
     OLS with standard errors clustered by category; the pooled model has year effects specific to each server.
     The arXiv panel has only 6-7 archives, too few clusters for reliable inference; it is descriptive.
  4. Use vs output: does the marker rise in arXiv physics (and maths) match bioRxiv's while output diverges? Marker
     difference-in-differences (test 2) for arXiv group vs all of bioRxiv, on the months both cover, next to the
     output event study of the within-field contrasts for the same pair (rate ratios relative to 2022, and 2026
     relative to 2025, i.e. the 2026 acceleration of one group relative to the other).
  5. Lower bound on the share of LLM-processed abstracts (Kobak et al. 2025), arXiv only: the excess share of abstracts
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
from scipy import stats

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stats_within_field import (COMPUTATIONAL, EXPERIMENT, THEORY, WET_LAB, contrast_frame, fit_poisson,  # noqa: E402
                                load_arxiv, load_biorxiv, total, ym_range, yearly_rr)

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


def did(series, a, b, first_post=2023):
    """Marker rate ratio of group a to group b in each year from first_post on, relative to the pooled 2019-2022
    baseline. OLS of the monthly log ratio of marker rates, log(k_a/n_a) - log(k_b/n_b), on dummies for 2023-2026,
    with classical standard errors and t intervals. Pooling the four pre-ChatGPT years is more stable than a single
    base year, notably for small groups. The bioRxiv text sample has only 16 months, too few for HAC/Driscoll-Kraay
    standard errors, which come out too narrow there (checked against the month-to-month variation of 2019-2022)."""
    ms = sorted(m for m in set(series[a]) & set(series[b])
                if min(series[a][m][0], series[b][m][0], series[a][m][1], series[b][m][1]) > 0)
    r = np.array([math.log(series[a][m][1] / series[a][m][0]) - math.log(series[b][m][1] / series[b][m][0])
                  for m in ms])
    yr = np.array([int(m[:4]) for m in ms])
    years = sorted(y for y in set(yr) if y >= first_post)
    X = np.column_stack([np.ones(len(ms))] + [(yr == y).astype(float) for y in years])
    res = sm.OLS(r, X).fit()
    tq = stats.t.ppf(0.975, res.df_resid)
    return {str(y): {"rr": math.exp(res.params[i + 1]), "lo": math.exp(res.params[i + 1] - tq * res.bse[i + 1]),
                     "hi": math.exp(res.params[i + 1] + tq * res.bse[i + 1]), "p": float(res.pvalues[i + 1]),
                     "months": int((yr == y).sum())}
            for i, y in enumerate(years)} | {"_n_months": len(ms), "_df": float(res.df_resid)}


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


def merge(*parts):
    """Sum group series {month: [papers, markers]} into one."""
    out = defaultdict(lambda: [0, 0])
    for part in parts:
        for m, (n, k) in part.items():
            out[m][0] += n
            out[m][1] += k
    return out


def use_vs_output(repo, series):
    """Do AI-writing markers rise as much in arXiv physics (and maths) as in bioRxiv, while output diverges?
    Markers: the Poisson difference-in-differences above, arXiv group vs all bioRxiv, on the months both corpora cover
    (bioRxiv text is sampled in March and September). Output: the event-study model of the within-field contrasts
    (stats_within_field.py), arXiv group vs bioRxiv new preprints (sum of categories), monthly 2019-01 to 2026-09.
    Both are rate ratios relative to 2022."""
    if "biorxiv" not in series or "arxiv" not in series:
        return None
    bio_all = merge(*series["biorxiv"].values())
    arx_groups = {"arxiv_physics": (merge(series["arxiv"]["theory"], series["arxiv"]["experiment"]), THEORY + EXPERIMENT),
                  "arxiv_theory": (series["arxiv"]["theory"], THEORY),
                  "arxiv_experiment": (series["arxiv"]["experiment"], EXPERIMENT)}
    if "maths" in series["arxiv"]:
        arx_groups["arxiv_maths"] = (series["arxiv"]["maths"], ["math"])
    counts_arx, counts_bio = load_arxiv(repo), load_biorxiv(repo)
    months = ym_range("2019-01", "2026-09")
    yb = total(counts_bio, list(counts_bio), months)
    out = {}
    for name, (ms, archives) in arx_groups.items():
        common = sorted(set(ms) & set(bio_all))
        markers = did({"A": {m: ms[m] for m in common}, "B": {m: bio_all[m] for m in common}}, "A", "B")
        df = contrast_frame(total(counts_arx, archives, months), yb, months)
        years = sorted(df["year"].unique())
        res, _ = fit_poisson(df, 2022, years)
        output = {str(k): {kk: vv for kk, vv in v.items() if kk != "se"} for k, v in yearly_rr(res, years, 2022).items()
                  if k != 2022}
        d = res.params["A_y2026"] - res.params["A_y2025"]
        cv = res.cov_params()
        se = math.sqrt(cv.loc["A_y2026", "A_y2026"] + cv.loc["A_y2025", "A_y2025"] - 2 * cv.loc["A_y2026", "A_y2025"])
        output["2026_vs_2025"] = {"rr": math.exp(d), "lo": math.exp(d - 1.96 * se), "hi": math.exp(d + 1.96 * se),
                                  "p": float(math.erfc(abs(d / se) / math.sqrt(2)))}
        out[f"{name}_vs_biorxiv"] = {"markers": markers, "output": output, "marker_months": len(common)}
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
    uvo = use_vs_output(repo, series)
    if uvo:
        results["use_vs_output"] = uvo
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
