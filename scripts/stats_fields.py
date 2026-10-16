"""Field-level departures from pre-ChatGPT trends, an in-space placebo across arXiv archives, and a synthetic-control
cross-check for mathematics (PLOS ONE analysis, Priority 1, field level).

Field model (Poisson pseudo-maximum likelihood, log link) for a monthly series y_t:
  log E[y_t] = a + b*t + s_{m(t)} + c * COVID_t + sum_{k=2023..2026} beta_k * 1[year(t) = k]
t in years; s_m calendar-month effects; COVID_t = 1 from April 2020 to March 2021. exp(beta_k) is the ratio of
observed to trend-expected counts in year k (the trend is identified from the pre-2023 months only).
Newey-West standard errors (12 lags). Fit window: 2015-01..2026-09 for arXiv and PubMed; shorter for servers that
opened later (flagged as less reliable).

In-space placebo: the same model for every arXiv archive with complete data; maths' 2026 departure is ranked
against all archives (rank p-value).

Synthetic control (Abadie et al. 2010; as in Nee, Zhong & Ni 2026): maths' deseasonalised monthly log series is
matched by a convex combination of the other archives over 2018-01..2025-12; the 2026 gap is the mean
difference over January-September 2026. Placebo: each donor in turn as the treated unit; p-value from the rank of
the post/pre RMSPE ratio.
Usage: python3 scripts/stats_fields.py [repo_dir]
"""
import csv
import json
import math
import os
import sys
from collections import defaultdict

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.optimize import minimize

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stats_within_field import load_arxiv, sup_wald_break, ym_range  # noqa: E402

LAST = "2026-09"
PHYSICS = ["astro-ph", "cond-mat", "gr-qc", "hep-ex", "hep-lat", "hep-ph", "hep-th", "math-ph", "nlin", "nucl-ex",
           "nucl-th", "physics", "quant-ph"]


def field_model(y, months, lags=12, per_year=12):
    df = pd.DataFrame({"y": y, "t": np.arange(len(y)) / per_year, "cm": [int(m[5:]) for m in months],
                       "year": [int(m[:4]) for m in months]})
    X = pd.get_dummies(df["cm"], prefix="cm", drop_first=True, dtype=float)
    X["t"] = df["t"]
    X["covid"] = [1.0 if "2020-04" <= m <= "2021-03" else 0.0 for m in months]
    for k in (2023, 2024, 2025, 2026):
        X[f"y{k}"] = (df["year"] == k).astype(float)
    X = sm.add_constant(X)
    res = sm.GLM(df["y"].values, X, family=sm.families.Poisson()).fit(cov_type="HAC", cov_kwds={"maxlags": lags})
    out = {str(k): {"rr": math.exp(res.params[f"y{k}"]), "lo": math.exp(res.conf_int().loc[f"y{k}", 0]),
                    "hi": math.exp(res.conf_int().loc[f"y{k}", 1]), "p": float(res.pvalues[f"y{k}"])}
           for k in (2023, 2024, 2025, 2026)}
    out["trend_per_year"] = math.exp(res.params["t"]) - 1
    return out


def deseason_log(y, months, upto="2025-12"):
    ly = np.log(np.asarray(y, float))
    cm = np.array([int(m[5:]) for m in months])
    ref = np.array([m <= upto for m in months])
    adj = {c: ly[(cm == c) & ref].mean() - ly[ref].mean() for c in range(1, 13)}
    return ly - np.array([adj[c] for c in cm])


def synth(target, donors, pre, post):
    """Convex weights minimising pre-period MSE of (target - donors @ w), with an intercept (demeaned series)."""
    Y, D = target - target[pre].mean(), donors - donors[pre].mean(axis=0)
    k = D.shape[1]
    fun = lambda w: np.mean((Y[pre] - D[pre] @ w) ** 2)  # noqa: E731
    res = minimize(fun, np.full(k, 1 / k), method="SLSQP", bounds=[(0, 1)] * k,
                   constraints=[{"type": "eq", "fun": lambda w: w.sum() - 1}], options={"maxiter": 500})
    w = res.x
    gap = Y - D @ w
    rmspe_pre = math.sqrt(np.mean(gap[pre] ** 2))
    rmspe_post = math.sqrt(np.mean(gap[post] ** 2))
    return {"weights": w, "gap_post_mean": float(np.mean(gap[post])), "rmspe_pre": rmspe_pre,
            "ratio": rmspe_post / rmspe_pre if rmspe_pre > 0 else float("inf"), "gap_series": gap}


def main(repo):
    out_dir = os.path.join(repo, "data/processed/stats")
    os.makedirs(out_dir, exist_ok=True)
    ax = load_arxiv(repo)
    months = ym_range("2015-01", LAST)
    series = {
        "physics": [sum(ax[a].get(m, 0) for a in PHYSICS) for m in months],
        "mathematics": [ax["math"].get(m, 0) for m in months],
        "computer_science": [ax["cs"].get(m, 0) for m in months],
    }
    results = {"fields": {}, "archives": {}, "synthetic_control_math": {}, "notes": []}
    results["unknown_break"] = {}
    for f, y in series.items():
        results["fields"][f] = field_model(y, months)
        ly = deseason_log(y, months, upto="2022-12")
        results["unknown_break"][f] = {"slope": sup_wald_break(ly, months, "slope"),
                                       "level": sup_wald_break(ly, months, "level")}
    # bioRxiv total, medRxiv excluding COVID, PubMed, OSF social sciences (shorter or adoption-affected windows)
    bio = json.load(open(os.path.join(repo, "data/raw/biorxiv_sum_m.json")))["bioRxiv content statistics"]
    bm = {r["month"]: int(r["new_papers"]) for r in bio}
    mb = ym_range("2018-01", LAST)
    results["fields"]["biology_biorxiv_from2018"] = field_model([bm[m] for m in mb], mb)
    med = {r["month"]: int(r["new_papers"]) - int(r["covid_title_or_abstract"])
           for r in csv.DictReader(open(os.path.join(repo, "data/raw/medrxiv_covid_monthly.csv")))}
    mm = ym_range("2019-07", LAST)
    results["fields"]["medicine_medrxiv_excl_covid_from2019_unreliable"] = field_model([med[m] for m in mm], mm)
    pub = json.load(open(os.path.join(repo, "data/raw/pubmed_edat_quarterly.json")))
    results["notes"].append("PubMed is quarterly; fitted with quarterly months (t in years, quarter effects).")
    pq = [r["quarter"] for r in pub]
    pm = [f"{q[:4]}-{3 * int(q[-1]):02d}" for q in pq]  # label quarters by their last month
    results["fields"]["biomedicine_pubmed_quarterly"] = field_model([r["journal_article"] for r in pub], pm, lags=4,
                                                                    per_year=4)
    # social sciences: OSF servers (quarterly, first versions) plus arXiv econ and q-fin, from 2019 (short, flagged)
    osf = defaultdict(int)
    for r in csv.DictReader(open(os.path.join(repo, "data/raw/osf_quarterly.csv"))):
        osf[f"{r['quarter'][:4]}-Q{r['quarter'][-1]}"] += int(r["new_papers"])
    qs = [q for q in sorted(osf) if "2019-Q1" <= q <= "2026-Q3"]
    econ = defaultdict(int)
    for a in ("econ", "q-fin"):
        for m, v in ax[a].items():
            econ[f"{m[:4]}-Q{(int(m[5:]) - 1) // 3 + 1}"] += v
    results["fields"]["social_sciences_quarterly_from2019_unreliable"] = field_model(
        [osf[q] + econ[q] for q in qs], [f"{q[:4]}-{3 * int(q[-1]):02d}" for q in qs], lags=4, per_year=4)

    # in-space placebo across archives
    archives = [a for a in ax if all(ax[a].get(m, 0) > 0 for m in months)]
    for a in archives:
        results["archives"][a] = field_model([ax[a][m] for m in months], months)
    logs = {a: math.log(v["2026"]["rr"]) for a, v in results["archives"].items()}
    ranked = sorted(logs, key=logs.get, reverse=True)
    results["archive_rank_2026"] = [(a, round(math.exp(logs[a]), 3)) for a in ranked]
    results["math_rank_p"] = (ranked.index("math") + 1) / len(ranked)

    # synthetic control for maths (donors: other archives with complete data since 2018)
    ms = ym_range("2018-01", LAST)
    donors = [a for a in ax if a != "math" and all(ax[a].get(m, 0) > 0 for m in ms)]
    L = {a: deseason_log([ax[a][m] for m in ms], ms) for a in donors + ["math"]}
    pre = np.array([m <= "2025-12" for m in ms])
    post = np.array([m >= "2026-01" for m in ms])
    sc = synth(L["math"], np.column_stack([L[a] for a in donors]), pre, post)
    placebo = {}
    for a in donors:
        others = [d for d in donors if d != a] + ["math"]
        placebo[a] = synth(L[a], np.column_stack([L[d] for d in others]), pre, post)
    ratios = sorted([sc["ratio"]] + [p["ratio"] for p in placebo.values()], reverse=True)
    results["synthetic_control_math"] = {
        "donors": donors, "weights": {d: round(float(w), 3) for d, w in zip(donors, sc["weights"]) if w > 0.005},
        "pre_window": "2018-01..2025-12", "post_window": "2026-01..2026-09",
        "gap_2026_pct": math.exp(sc["gap_post_mean"]) - 1, "rmspe_pre": sc["rmspe_pre"],
        "post_pre_rmspe_ratio": sc["ratio"], "rank_p": (ratios.index(sc["ratio"]) + 1) / len(ratios),
        "placebo_gaps_2026_pct": {a: round(math.exp(p["gap_post_mean"]) - 1, 3) for a, p in placebo.items()},
        "monthly_gap_2025_2026": {m: round(float(g), 4) for m, g in zip(ms, sc["gap_series"]) if m >= "2025-01"},
    }
    # same design with the pre-period ending before ChatGPT (2018-01..2022-11)
    pre2 = np.array([m <= "2022-11" for m in ms])
    sc2 = synth(L["math"], np.column_stack([L[a] for a in donors]), pre2, post)
    results["synthetic_control_math_pre_to_2022_11"] = {
        "gap_2026_pct": math.exp(sc2["gap_post_mean"]) - 1, "rmspe_pre": sc2["rmspe_pre"],
        "weights": {d: round(float(w), 3) for d, w in zip(donors, sc2["weights"]) if w > 0.005}}

    json.dump(results, open(os.path.join(out_dir, "field_tests.json"), "w"), indent=1, default=float)
    f = lambda d: f"{d['rr']:.3f} [{d['lo']:.3f}, {d['hi']:.3f}] p={d['p']:.2g}"  # noqa: E731
    for name, v in results["fields"].items():
        print(f"{name:50} trend {v['trend_per_year']:+.1%}/yr | " + " | ".join(f"{k}: {f(v[k])}" for k in ("2024", "2025", "2026")))
    for f, v in results["unknown_break"].items():
        print("break", f, {k: (b["break_month"], round(b["sup_wald"], 1), b["p_bootstrap"]) for k, b in v.items()})
    print("archive 2026 ranking:", results["archive_rank_2026"])
    print("math rank p:", results["math_rank_p"])
    s = results["synthetic_control_math"]
    print("synthetic control math gap 2026:", f"{s['gap_2026_pct']:+.1%}", "rank p", s["rank_p"], "weights", s["weights"])
    print("pre to 2022-11:", results["synthetic_control_math_pre_to_2022_11"])


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
