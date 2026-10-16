"""Formal tests of the within-field contrasts and field-level departures (PLOS ONE analysis, Priority 1).

Contrasts (confirmatory, H1): monthly new-preprint counts of group A vs group B
  C1 physics:  theory (hep-th, hep-ph, gr-qc, nucl-th) vs experiment (hep-ex, nucl-ex)          arXiv, 2015-01..2026-09
  C2 biology:  computational (bioinformatics, systems biology, genomics) vs wet lab (12 cats)    bioRxiv, 2019-01..2026-09
  C3 medicine: preprints naming a public dataset vs the rest, both excluding COVID-19           medRxiv, 2019-07..2026-09

Main model (Poisson pseudo-maximum likelihood, log link), for a contrast with groups g in {A, B} and months t:
  log E[y_gt] = lambda_t + mu_{g,m(t)} + sum_{k != base} beta_k * 1[g = A] * 1[year(t) = k]
lambda_t: month fixed effects (absorb every shock common to both groups, including platform-wide changes);
mu_{g,m}: group-specific calendar-month effects (seasonality); beta_k: log rate ratio of A relative to B in year k,
relative to the base year (2022; 2019 as sensitivity). Standard errors: Driscoll-Kraay (HAC over months, 12 lags).
Cross-checks: OLS on the deseasonalised monthly log ratio with Newey-West SEs, and a moving-block bootstrap
(12-month blocks, 999 draws) for the 2026 rate ratio.

Everything is written to data/processed/stats/ (JSON + CSV); a readable summary is printed.
Usage: python3 scripts/stats_within_field.py [repo_dir]
"""
import csv
import json
import math
import os
import sys
from collections import defaultdict
from itertools import combinations

import numpy as np
import pandas as pd
import statsmodels.api as sm

RNG = np.random.default_rng(20261016)
LAST = "2026-09"
THEORY = ["hep-th", "hep-ph", "gr-qc", "nucl-th"]
EXPERIMENT = ["hep-ex", "nucl-ex"]
COMPUTATIONAL = ["bioinformatics", "systems biology", "genomics"]
WET_LAB = ["biochemistry", "cell biology", "developmental biology", "molecular biology", "microbiology", "immunology",
           "plant biology", "physiology", "cancer biology", "pharmacology and toxicology", "pathology",
           "synthetic biology"]
YEARS_REPORTED = [2023, 2024, 2025, 2026]


# ---------------------------------------------------------------- data
def ym_range(a, b):
    y, m = map(int, a.split("-"))
    out = []
    while f"{y}-{m:02d}" <= b:
        out.append(f"{y}-{m:02d}")
        m += 1
        if m == 13:
            y, m = y + 1, 1
    return out


def load_arxiv(repo):
    s = defaultdict(lambda: defaultdict(int))
    for r in csv.DictReader(open(os.path.join(repo, "data/raw/arxiv_archive_monthly.csv"))):
        s[r["archive"]][f"{r['year']}-{int(r['month']):02d}"] += int(r["new"])
    return s


def load_biorxiv(repo):
    s = defaultdict(lambda: defaultdict(int))
    for r in csv.DictReader(open(os.path.join(repo, "data/raw/biorxiv_category_monthly.csv"))):
        s[r["category"]][r["month"]] += int(r["new_papers"])
    return s


def load_medrxiv_public(repo):
    path = os.path.join(repo, "data/raw/medrxiv_text_main.csv")
    if not os.path.exists(path):
        return None
    pub, rest = defaultdict(int), defaultdict(int)
    for r in csv.DictReader(open(path)):
        pub[r["month"]] += int(r["public_noncovid"])
        rest[r["month"]] += int(r["papers_noncovid"]) - int(r["public_noncovid"])
    return pub, rest


def total(series, keys, months):
    return np.array([sum(series[k].get(m, 0) for k in keys) for m in months], dtype=float)


# ---------------------------------------------------------------- models
def contrast_frame(ya, yb, months):
    rows = []
    for i, m in enumerate(months):
        for g, y in (("A", ya[i]), ("B", yb[i])):
            rows.append({"month": m, "t": i, "year": int(m[:4]), "cm": int(m[5:]), "A": int(g == "A"), "y": y})
    return pd.DataFrame(rows)


def design(df, base, years, trend=False):
    X = pd.get_dummies(df["month"], prefix="mo", dtype=float)  # month fixed effects (include intercept role)
    for c in range(2, 13):  # group-specific seasonality, January as reference
        X[f"A_cm{c}"] = df["A"] * (df["cm"] == c)
    for k in years:
        if k != base:
            X[f"A_y{k}"] = df["A"] * (df["year"] == k)
    if trend:  # group-specific linear trend (years), for trend-adjusted variants
        X["A_trend"] = df["A"] * df["t"] / 12.0
    X["A"] = df["A"].astype(float)
    return X.astype(float)


def fit_poisson(df, base, years, trend=False, lags=12):
    X = design(df, base, years, trend)
    res = sm.GLM(df["y"].values, X, family=sm.families.Poisson()).fit(
        cov_type="hac-groupsum", cov_kwds={"time": df["t"].values, "maxlags": lags})
    return res, X


def yearly_rr(res, years, base):
    out = {}
    for k in years:
        if k == base:
            out[k] = {"rr": 1.0, "lo": 1.0, "hi": 1.0, "p": None, "se": 0.0}
            continue
        b, se = res.params[f"A_y{k}"], res.bse[f"A_y{k}"]
        out[k] = {"rr": math.exp(b), "lo": math.exp(b - 1.96 * se), "hi": math.exp(b + 1.96 * se),
                  "p": float(res.pvalues[f"A_y{k}"]), "se": float(se)}
    return out


def deseasonalised_log_ratio(ya, yb, months, upto=None):
    r = np.log(ya) - np.log(yb)
    cm = np.array([int(m[5:]) for m in months])
    ref = np.array([m <= (upto or months[-1]) for m in months])
    seas = {c: r[(cm == c) & ref].mean() - r[ref].mean() for c in range(1, 13)}
    return r - np.array([seas[c] for c in cm])


def ols_log_ratio(ya, yb, months, base, years, lags=12):
    r = np.log(ya) - np.log(yb)
    df = pd.DataFrame({"r": r, "year": [int(m[:4]) for m in months], "cm": [int(m[5:]) for m in months]})
    X = pd.get_dummies(df["cm"], prefix="cm", drop_first=True, dtype=float)
    for k in years:
        if k != base:
            X[f"y{k}"] = (df["year"] == k).astype(float)
    X = sm.add_constant(X)
    res = sm.OLS(df["r"], X).fit(cov_type="HAC", cov_kwds={"maxlags": lags})
    return {k: {"rr": math.exp(res.params[f"y{k}"]), "lo": math.exp(res.conf_int().loc[f"y{k}", 0]),
                "hi": math.exp(res.conf_int().loc[f"y{k}", 1]), "p": float(res.pvalues[f"y{k}"])}
            for k in years if k != base}


def block_bootstrap_rr(ya, yb, months, base, target=2026, reps=999, block=12):
    """Moving-block bootstrap of the log ratio's residuals around the yearly-mean model (OLS version)."""
    r = np.log(ya) - np.log(yb)
    years = np.array([int(m[:4]) for m in months])
    cm = np.array([int(m[5:]) for m in months])
    X = np.column_stack([np.ones(len(r))] + [(cm == c).astype(float) for c in range(2, 13)] +
                        [(years == k).astype(float) for k in sorted(set(years)) if k != base])
    names = [k for k in sorted(set(years)) if k != base]
    beta, *_ = np.linalg.lstsq(X, r, rcond=None)
    fitted, resid = X @ beta, r - X @ beta
    j = 12 + names.index(target)
    n = len(r)
    draws = []
    for _ in range(reps):
        idx = []
        while len(idx) < n:
            s = RNG.integers(0, n - block + 1)
            idx.extend(range(s, s + block))
        rb = fitted + resid[np.array(idx[:n])]
        bb, *_ = np.linalg.lstsq(X, rb, rcond=None)
        draws.append(bb[j])
    lo, hi = np.percentile(draws, [2.5, 97.5])
    return {"rr": math.exp(beta[j]), "lo": math.exp(lo), "hi": math.exp(hi)}


def hac_wald_last(X, y, lags):
    """OLS with Newey-West (Bartlett) covariance; Wald statistic for the last coefficient (fast numpy version)."""
    XtX_inv = np.linalg.inv(X.T @ X)
    beta = XtX_inv @ X.T @ y
    u = (X * (y - X @ beta)[:, None])
    S = u.T @ u
    for lag in range(1, lags + 1):
        g = u[lag:].T @ u[:-lag]
        S += (1 - lag / (lags + 1)) * (g + g.T)
    V = XtX_inv @ S @ XtX_inv
    return float(beta[-1] ** 2 / V[-1, -1])


def sup_wald_break(series, months, kind="slope", trim=0.15, reps=999, lags=12):
    """Single unknown break in a (deseasonalised) monthly series: sup-Wald over candidate dates.

    kind="slope": r_t = a + b t + c (t - tau)_+ (continuous change in growth);  kind="level": r_t = a + b t + d 1[t>=tau].
    HAC (Newey-West) Wald statistic for the break term at every tau in the trimmed range; p-value from a parametric
    bootstrap of the no-break model with AR(1) errors (reps draws). Returns the break month, sup-Wald and p-value.
    """
    y = np.asarray(series, dtype=float)
    n = len(y)
    t = np.arange(n, dtype=float)
    cands = range(int(n * trim), int(n * (1 - trim)))

    designs = {tau: np.column_stack([np.ones(n), t, np.maximum(t - tau, 0) if kind == "slope"
                                      else (t >= tau).astype(float)]) for tau in cands}

    def stat_for(yv):
        best = (-1.0, None)
        for tau, X in designs.items():
            w = hac_wald_last(X, yv, lags)
            if w > best[0]:
                best = (w, tau)
        return best

    w_obs, tau_obs = stat_for(y)
    X0 = np.column_stack([np.ones(n), t])
    b0, *_ = np.linalg.lstsq(X0, y, rcond=None)
    e0 = y - X0 @ b0
    rho = float(np.corrcoef(e0[:-1], e0[1:])[0, 1])
    sd = float(np.std(e0[1:] - rho * e0[:-1], ddof=2))
    exceed = 0
    for _ in range(reps):
        e = np.zeros(n)
        e[0] = RNG.normal(0, sd / math.sqrt(max(1e-6, 1 - rho ** 2)))
        for i in range(1, n):
            e[i] = rho * e[i - 1] + RNG.normal(0, sd)
        if stat_for(X0 @ b0 + e)[0] >= w_obs:
            exceed += 1
    return {"break_month": months[tau_obs], "sup_wald": w_obs, "p_bootstrap": (exceed + 1) / (reps + 1),
            "ar1_rho": rho, "kind": kind}


def placebo_post(ya, yb, months, placebo_year, end="2022-12", lags=12):
    """Pre-ChatGPT data only: level shift of the A/B ratio from placebo_year on, with a group-specific trend."""
    keep = [i for i, m in enumerate(months) if m <= end]
    ms = [months[i] for i in keep]
    df = contrast_frame(ya[keep], yb[keep], ms)
    X = pd.get_dummies(df["month"], prefix="mo", dtype=float)
    for c in range(2, 13):
        X[f"A_cm{c}"] = df["A"] * (df["cm"] == c)
    X["A_trend"] = df["A"] * df["t"] / 12.0
    X["A_post"] = df["A"] * (df["year"] >= placebo_year)
    X["A"] = df["A"].astype(float)
    res = sm.GLM(df["y"].values, X.astype(float), family=sm.families.Poisson()).fit(
        cov_type="hac-groupsum", cov_kwds={"time": df["t"].values, "maxlags": lags})
    b, se = res.params["A_post"], res.bse["A_post"]
    return {"placebo_year": placebo_year, "rr": math.exp(b), "lo": math.exp(b - 1.96 * se),
            "hi": math.exp(b + 1.96 * se), "p": float(res.pvalues["A_post"])}


def contrast_summary(name, ya, yb, months, base=2022, with_bootstrap=True, with_break=True):
    years = sorted({int(m[:4]) for m in months})
    df = contrast_frame(ya, yb, months)
    res, _ = fit_poisson(df, base, years)
    ev = yearly_rr(res, years, base)
    out = {"contrast": name, "months": [months[0], months[-1]], "base_year": base,
           "mean_monthly_A_2026": float(np.mean(ya[[i for i, m in enumerate(months) if m.startswith("2026")]])),
           "mean_monthly_B_2026": float(np.mean(yb[[i for i, m in enumerate(months) if m.startswith("2026")]])),
           "event_study": {str(k): v for k, v in ev.items()},
           "ols_log_ratio": {str(k): v for k, v in ols_log_ratio(ya, yb, months, base, years).items()}}
    # trend-adjusted: group-specific linear trend fitted alongside pre-period year effects collapsed
    pre = [i for i, m in enumerate(months) if int(m[:4]) <= 2022]
    if len({int(months[i][:4]) for i in pre}) >= 3:
        df_t = contrast_frame(ya, yb, months)
        Xt = pd.get_dummies(df_t["month"], prefix="mo", dtype=float)
        for c in range(2, 13):
            Xt[f"A_cm{c}"] = df_t["A"] * (df_t["cm"] == c)
        Xt["A_trend"] = df_t["A"] * df_t["t"] / 12.0
        for k in YEARS_REPORTED:
            Xt[f"A_y{k}"] = df_t["A"] * (df_t["year"] == k)
        Xt["A"] = df_t["A"].astype(float)
        rt = sm.GLM(df_t["y"].values, Xt.astype(float), family=sm.families.Poisson()).fit(
            cov_type="hac-groupsum", cov_kwds={"time": df_t["t"].values, "maxlags": 12})
        out["trend_adjusted"] = {str(k): {"rr": math.exp(rt.params[f"A_y{k}"]),
                                          "lo": math.exp(rt.params[f"A_y{k}"] - 1.96 * rt.bse[f"A_y{k}"]),
                                          "hi": math.exp(rt.params[f"A_y{k}"] + 1.96 * rt.bse[f"A_y{k}"]),
                                          "p": float(rt.pvalues[f"A_y{k}"])} for k in YEARS_REPORTED}
        out["pre_trend_per_year"] = {"rr": math.exp(rt.params["A_trend"]),
                                     "lo": math.exp(rt.params["A_trend"] - 1.96 * rt.bse["A_trend"]),
                                     "hi": math.exp(rt.params["A_trend"] + 1.96 * rt.bse["A_trend"])}
    if with_bootstrap:
        out["block_bootstrap_2026"] = block_bootstrap_rr(ya, yb, months, base)
    se26 = ev[2026]["se"]
    out["mde_2026_80pct_power"] = math.exp(2.8 * se26) - 1  # (1.96 + 0.84) * SE
    if with_break:
        r = deseasonalised_log_ratio(ya, yb, months)
        out["unknown_break_slope"] = sup_wald_break(r, months, "slope")
        out["unknown_break_level"] = sup_wald_break(r, months, "level")
    return out


def holm(pvals):
    order = sorted(range(len(pvals)), key=lambda i: pvals[i])
    adj, running = [0.0] * len(pvals), 0.0
    for rank, i in enumerate(order):
        running = max(running, min(1.0, (len(pvals) - rank) * pvals[i]))
        adj[i] = running
    return adj


def bh(pvals):
    n = len(pvals)
    order = sorted(range(n), key=lambda i: pvals[i], reverse=True)
    adj, running = [0.0] * n, 1.0
    for rank, i in enumerate(order):
        running = min(running, pvals[i] * n / (n - rank))
        adj[i] = running
    return adj


def rr2026(ya, yb, months, base=2022):
    years = sorted({int(m[:4]) for m in months})
    res, _ = fit_poisson(contrast_frame(ya, yb, months), base, years)
    return yearly_rr(res, years, base)[2026]


# ---------------------------------------------------------------- main
def main(repo):
    out_dir = os.path.join(repo, "data/processed/stats")
    os.makedirs(out_dir, exist_ok=True)
    ax, bx = load_arxiv(repo), load_biorxiv(repo)
    results = {"confirmatory": {}, "sensitivity": {}, "negative_controls": {}, "leave_one_out": {},
               "placebo_breaks": {}, "notes": []}

    m_ax = ym_range("2015-01", LAST)
    m_bx = ym_range("2019-01", LAST)
    C = {"C1_physics_theory_vs_experiment": (total(ax, THEORY, m_ax), total(ax, EXPERIMENT, m_ax), m_ax),
         "C2_biology_computational_vs_wetlab": (total(bx, COMPUTATIONAL, m_bx), total(bx, WET_LAB, m_bx), m_bx)}
    med = load_medrxiv_public(repo)
    if med:
        m_md = ym_range("2019-07", LAST)
        C["C3_medicine_public_dataset_vs_rest"] = (np.array([med[0][m] for m in m_md], float),
                                                   np.array([med[1][m] for m in m_md], float), m_md)
    else:
        results["notes"].append("C3 not run: data/raw/medrxiv_text_main.csv missing.")

    for name, (ya, yb, ms) in C.items():
        print("fitting", name, flush=True)
        results["confirmatory"][name] = contrast_summary(name, ya, yb, ms)
        results["sensitivity"][name + "__base2019"] = contrast_summary(
            name, ya, yb, ms, base=2019, with_bootstrap=False, with_break=False)["event_study"]
        results["placebo_breaks"][name] = [placebo_post(ya, yb, ms, y) for y in (2019, 2020, 2021)
                                           if int(ms[0][:4]) < y]

    # confirmatory family: 2026 rate ratio of each contrast, Holm-adjusted
    names = list(results["confirmatory"])
    ps = [results["confirmatory"][n]["event_study"]["2026"]["p"] for n in names]
    for n, p_adj in zip(names, holm(ps)):
        results["confirmatory"][n]["p_holm_2026"] = p_adj

    # sensitivity: composition and rule-change months
    print("sensitivity", flush=True)
    sens = results["sensitivity"]
    sens["C1__without_hep-ph"] = rr2026(total(ax, [a for a in THEORY if a != "hep-ph"], m_ax),
                                        total(ax, EXPERIMENT, m_ax), m_ax)
    sens["C2__without_genomics"] = rr2026(total(bx, ["bioinformatics", "systems biology"], m_bx),
                                          total(bx, WET_LAB, m_bx), m_bx)
    sens["C2__genomics_as_wet_lab"] = rr2026(total(bx, ["bioinformatics", "systems biology"], m_bx),
                                             total(bx, WET_LAB + ["genomics"], m_bx), m_bx)
    rule = {"2025-11", "2025-12", "2026-01", "2026-02"}
    m_ax_r = [m for m in m_ax if m not in rule]
    idx = [m_ax.index(m) for m in m_ax_r]
    sens["C1__drop_Nov2025_Feb2026"] = rr2026(total(ax, THEORY, m_ax)[idx], total(ax, EXPERIMENT, m_ax)[idx], m_ax_r)
    for name, (ya, yb, ms) in C.items():
        pre = [i for i, m in enumerate(ms) if m <= "2025-10"]
        years = sorted({int(ms[i][:4]) for i in pre})
        res, _ = fit_poisson(contrast_frame(ya[pre], yb[pre], [ms[i] for i in pre]), 2022, years)
        sens[name + "__sample_to_Oct2025__rr2025"] = yearly_rr(res, years, 2022)[2025]

    # leave one category out
    print("leave-one-out", flush=True)
    loo = results["leave_one_out"]
    for a in THEORY:
        loo[f"C1__drop_{a}"] = rr2026(total(ax, [x for x in THEORY if x != a], m_ax), total(ax, EXPERIMENT, m_ax),
                                      m_ax)
    for a in EXPERIMENT:
        loo[f"C1__drop_{a}"] = rr2026(total(ax, THEORY, m_ax), total(ax, [x for x in EXPERIMENT if x != a], m_ax),
                                      m_ax)
    for c in COMPUTATIONAL:
        loo[f"C2__drop_{c}"] = rr2026(total(bx, [x for x in COMPUTATIONAL if x != c], m_bx),
                                      total(bx, WET_LAB, m_bx), m_bx)
    for c in WET_LAB:
        loo[f"C2__drop_{c}"] = rr2026(total(bx, COMPUTATIONAL, m_bx), total(bx, [x for x in WET_LAB if x != c], m_bx),
                                      m_bx)

    # negative controls: pairs that H1 says should not diverge
    print("negative controls", flush=True)
    neg = results["negative_controls"]
    neg["hep-ex_vs_nucl-ex"] = rr2026(total(ax, ["hep-ex"], m_ax), total(ax, ["nucl-ex"], m_ax), m_ax)
    for a, b in combinations(THEORY, 2):
        neg[f"{a}_vs_{b}"] = rr2026(total(ax, [a], m_ax), total(ax, [b], m_ax), m_ax)
    splits = []
    for half in combinations(WET_LAB, 6):
        if WET_LAB[0] not in half:
            continue
        other = [c for c in WET_LAB if c not in half]
        splits.append(math.log(rr2026(total(bx, list(half), m_bx), total(bx, other, m_bx), m_bx)["rr"]))
    obs = math.log(results["confirmatory"]["C2_biology_computational_vs_wetlab"]["event_study"]["2026"]["rr"])
    neg["wetlab_random_halves"] = {
        "n_splits": len(splits), "abs_log_rr_quantiles": dict(zip(["50%", "90%", "95%", "99%"], [
            float(math.exp(q)) for q in np.percentile(np.abs(splits), [50, 90, 95, 99])])),
        "share_at_least_as_extreme_as_C2": float(np.mean(np.abs(splits) >= abs(obs)))}
    archives = [a for a in ax if all(ax[a].get(m, 0) > 0 for m in m_ax)]
    pair_logs = []
    for a, b in combinations(sorted(archives), 2):
        pair_logs.append(abs(math.log(rr2026(total(ax, [a], m_ax), total(ax, [b], m_ax), m_ax)["rr"])))
    obs1 = abs(math.log(results["confirmatory"]["C1_physics_theory_vs_experiment"]["event_study"]["2026"]["rr"]))
    neg["arxiv_all_archive_pairs"] = {"n_pairs": len(pair_logs), "archives": archives,
                                      "share_at_least_as_extreme_as_C1": float(np.mean(np.array(pair_logs) >= obs1))}

    json.dump(results, open(os.path.join(out_dir, "within_field_tests.json"), "w"), indent=1, default=float)
    print(json.dumps(results, indent=1, default=float)[:6000])


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
