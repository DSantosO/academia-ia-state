"""Prototype metrics for the chart-improvement proposal (docs/propuesta-graficos.md).

1. Excess over the pre-ChatGPT trend ("P-score", as in excess-mortality work): a log-linear trend with quarterly
   seasonality is fitted on a baseline window and extrapolated; excess = observed / expected - 1, with a 95%
   prediction interval. COVID quarters (2020-Q2 to 2021-Q1) are left out of every baseline window.
2. Growth gradient across arXiv archives: growth in Q1-Q3 2026 vs Q1-Q3 2025, against each archive's
   2017-2022 compound annual growth.

Reads data/raw/arxiv_archive_monthly.csv (2010 onwards, scripts/fetch_arxiv_years.sh <dir> 2010),
data/raw/biorxiv_sum_m.json and data/raw/pubmed_edat_quarterly.json (fetch_pubmed_quarterly.py). bioRxiv was still in
its adoption phase until about 2018 (new papers doubled every year), so it gets the 2018-2022 baseline only. Writes data/processed/excess_over_trend_quarterly.csv and
data/processed/arxiv_archive_growth.csv.  Usage: python3 scripts/analyze_trends.py [repo_dir]
"""
import csv
import json
import math
import os
import sys
from collections import defaultdict

import numpy as np

PHYSICS = ["astro-ph", "cond-mat", "gr-qc", "hep-ex", "hep-lat", "hep-ph", "hep-th", "math-ph", "nlin", "nucl-ex",
           "nucl-th", "physics", "quant-ph"]
LAST = "2026-Q3"
COVID = {"2020-Q2", "2020-Q3", "2020-Q4", "2021-Q1"}
BASELINES = {  # name: (first quarter, last quarter)
    "2015-2022": ("2015-Q1", "2022-Q4"),
    "2015-2019": ("2015-Q1", "2019-Q4"),
    "2018-2022": ("2018-Q1", "2022-Q4"),
}
MAIN = "2015-2022"
ONLY = {"biology_biorxiv": ["2018-2022"]}  # series whose earlier years are an adoption phase, not a trend



def qkey(year, month):
    return f"{year}-Q{(month - 1) // 3 + 1}"


def qindex(q):
    return int(q[:4]) * 4 + int(q[-1]) - 1


def t975(df):
    """97.5% quantile of Student's t (Cornish-Fisher expansion; error < 0.001 for df >= 10)."""
    z = 1.959964
    return (z + (z ** 3 + z) / (4 * df) + (5 * z ** 5 + 16 * z ** 3 + 3 * z) / (96 * df ** 2)
            + (3 * z ** 7 + 19 * z ** 5 + 17 * z ** 3 - 15 * z) / (384 * df ** 3))


def load(repo):
    arch = defaultdict(lambda: defaultdict(int))
    for r in csv.DictReader(open(os.path.join(repo, "data/raw/arxiv_archive_monthly.csv"))):
        arch[r["archive"]][qkey(int(r["year"]), int(r["month"]))] += int(r["new"])
    fields = {
        "physics": {q: sum(arch[a].get(q, 0) for a in PHYSICS) for q in arch["hep-th"]},
        "mathematics": dict(arch["math"]),
        "computer_science": dict(arch["cs"]),
    }
    bio = defaultdict(int)
    for r in json.load(open(os.path.join(repo, "data/raw/biorxiv_sum_m.json")))["bioRxiv content statistics"]:
        bio[qkey(int(r["month"][:4]), int(r["month"][5:7]))] += int(r["new_papers"])
    fields["biology_biorxiv"] = dict(bio)
    pubmed = json.load(open(os.path.join(repo, "data/raw/pubmed_edat_quarterly.json")))
    fields["biomedicine_pubmed"] = {r["quarter"]: r["journal_article"] for r in pubmed}
    for s in list(fields.values()) + list(arch.values()):
        for q in [q for q in s if qindex(q) > qindex(LAST)]:
            del s[q]
    return fields, arch


def design(q):
    n = int(q[-1])
    return [1.0, qindex(q) / 4.0, float(n == 2), float(n == 3), float(n == 4)]


def fit_trend(series, first, last):
    train = [q for q in series if qindex(first) <= qindex(q) <= qindex(last) and q not in COVID and series[q] > 0]
    X = np.array([design(q) for q in train])
    y = np.log([series[q] for q in train])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    df = len(train) - X.shape[1]
    s2 = float(resid @ resid) / df
    xtx_inv = np.linalg.inv(X.T @ X)
    return beta, s2, xtx_inv, df, len(train)


def excess(series, first, last):
    beta, s2, xtx_inv, df, n = fit_trend(series, first, last)
    t = t975(df)
    out = {}
    for q in sorted(series, key=qindex):
        x = np.array(design(q))
        mu = float(x @ beta)
        se = math.sqrt(s2 * (1 + float(x @ xtx_inv @ x)))
        exp_mid, exp_lo, exp_hi = math.exp(mu), math.exp(mu - t * se), math.exp(mu + t * se)
        out[q] = {"observed": series[q], "expected": exp_mid, "expected_lo": exp_lo, "expected_hi": exp_hi,
                  "excess": series[q] / exp_mid - 1, "excess_lo": series[q] / exp_hi - 1,
                  "excess_hi": series[q] / exp_lo - 1}
    return out, {"annual_trend_growth": math.exp(beta[1]) - 1, "quarters_fitted": n, "resid_sd": math.sqrt(s2)}


def archive_growth(arch):
    rows = []
    for a, s in arch.items():
        yr = defaultdict(int)
        for q, v in s.items():
            yr[q[:4]] += v
        if not (yr.get("2017") and yr.get("2022")):
            continue
        q123 = lambda y: sum(s.get(f"{y}-Q{i}", 0) for i in (1, 2, 3))  # noqa: E731
        cagr = (yr["2022"] / yr["2017"]) ** (1 / 5) - 1
        g26 = q123(2026) / q123(2025) - 1
        g25 = q123(2025) / q123(2024) - 1
        rows.append({"archive": a, "papers_2017": yr["2017"], "papers_2022": yr["2022"],
                     "papers_q1q3_2025": q123(2025), "papers_q1q3_2026": q123(2026),
                     "cagr_2017_2022": round(cagr, 4), "growth_q1q3_2025": round(g25, 4),
                     "growth_q1q3_2026": round(g26, 4), "acceleration_pp": round(100 * (g26 - cagr), 1)})
    return sorted(rows, key=lambda r: -r["growth_q1q3_2026"])


def main(repo):
    fields, arch = load(repo)
    rows, summary = [], {}
    for f, s in fields.items():
        for b, (first, last) in BASELINES.items():
            if b not in ONLY.get(f, BASELINES):
                continue
            res, info = excess(s, first, last)
            summary[(f, b)] = {**info, **{k: res[LAST][k] for k in ("excess", "excess_lo", "excess_hi")}}
            for q, r in res.items():
                if qindex(q) >= qindex("2015-Q1"):
                    rows.append({"field": f, "baseline": b, "quarter": q,
                                 **{k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()}})
    out = os.path.join(repo, "data/processed")
    with open(os.path.join(out, "excess_over_trend_quarterly.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    growth = archive_growth(arch)
    with open(os.path.join(out, "arxiv_archive_growth.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(growth[0]))
        w.writeheader()
        w.writerows(growth)
    for (f, b), v in summary.items():
        print(f"{f:18} {b:10} trend {v['annual_trend_growth']:+.1%}/yr  n={v['quarters_fitted']:2}  "
              f"resid_sd={v['resid_sd']:.3f}  excess {LAST} {v['excess']:+.0%} [{v['excess_lo']:+.0%}, {v['excess_hi']:+.0%}]")
    for r in growth:
        print(f"{r['archive']:9} cagr17-22 {r['cagr_2017_2022']:+.1%}  q1q3 2025 {r['growth_q1q3_2025']:+.1%}  "
              f"q1q3 2026 {r['growth_q1q3_2026']:+.1%}  accel {r['acceleration_pp']:+.1f}pp  (2026: {r['papers_q1q3_2026']})")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
