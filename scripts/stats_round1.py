"""Round-1 review analyses: confounds of the field-level finding (arXiv accelerates; bioRxiv, medRxiv and PubMed do not).

Sections (each writes its own key of data/processed/stats/round1_tests.json; run all or name some):
  estimands   C1-C3 with multi-year baselines, a slope-change estimand, the 2026-vs-2025 acceleration, and inference
              from in-space placebos (review item P1c; the year-shock z was replaced by the calibration section)
  breaks      unknown-break tests with 5% trimming, so that breaks up to early 2026 can be found, and known-date tests
              (December 2022, November 2024, November 2025) with AR(1) bootstrap p-values (P1d)
  crosslists  field-level departures and the archive ranking with new + cross-listed submissions (list entries,
              as in Nee, Zhong & Ni 2026) instead of new submissions only (P1g)
  funding     PubMed journal articles with vs without a US affiliation, and bioRxiv preprints by the corresponding
              author's institution (US vs elsewhere), as tests of a US funding shock in 2025 (P1e)
  oai         from the arXiv OAI-PMH harvests (maths and six physics archives): Snowmass 2021 and European Strategy
              2026 inputs, the C1 variants (hep-ph vs hep-ex, gr-qc out of theory), genres (reviews, proceedings, white
              papers, theses), and OAI vs statistics-page counts (P1b, P1f). Writes the paper-level table
              data/processed/arxiv_paper_flags.csv.gz.
  dating      identifier (announcement) month vs first-version submission month, 2024-2026 (P1a); round 2: the
              September 2026 spike in mathematics, October 2026 under the cap, C1 and arXiv vs bioRxiv by dating
  inspire_dating  round 2: INSPIRE-HEP records dated by submission against arXiv's statistics pages
  hepex_crosslists  round 2: cross-lists of hep-ex papers by month (OAI), for the 2025-2026 change in composition
  genre_round2  round 2: the keyword genres validated against INSPIRE's types, revised rules, revision sensitivity
  c2_ai_split  round 2 (exploratory): C2 without papers on AI or machine learning as a topic (D3m list)
  biorxiv_sum_check  round 2: bioRxiv's /sum statistics against the record-level and per-category counts
  placebos_matched  round 2: in-space placebos matched to the structure of C1 and C2, with their floors
  funding_round2  round 2: bioRxiv and medRxiv by the corresponding author's institution (US or elsewhere),
              against a prediction stated first; PubMed's US/non-US ratio calibrated in time
  inspire_round2  round 2: the INSPIRE classes with the C1-C3 estimator under four bases, without planning
              papers, research articles only; link, type and cross-list shares by year
  planned     round 2: the C1-C3 specification planned in draft v1 (period effects against multi-year baselines,
              Poisson or negative binomial, Newey-West errors, Bonferroni intervals), beside the 2022-base estimate
  calibration round 2: rank-based in-time calibration with the estimator itself (replaces the year-shock z)
  medrxiv_flags  C3 with the title-only COVID-19 filter and with Spick et al.'s four missing datasets (P3)
  inspire     pre-registration section 10 (exploratory): INSPIRE-HEP classes from curated metadata (no AI)
Usage: python3 scripts/stats_round1.py [repo_dir] [section ...] [--oai OAI_DIR]
STATS_LAST=2026-08 writes the January-August 2026 versions to round1_tests_to_2026-08.json.
"""
import csv
import gzip
import json
import math
import os
import re
import sys
from collections import Counter, defaultdict
from itertools import combinations

import numpy as np
import pandas as pd
import statsmodels.api as sm

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stats_fields import PHYSICS, deseason_log, field_model  # noqa: E402
from stats_within_field import (COMPUTATIONAL, EXPERIMENT, LAST, SUFFIX, THEORY, WET_LAB,  # noqa: E402
                                contrast_frame, deseasonalised_log_ratio, hac_wald_last, load_arxiv, load_biorxiv,
                                load_medrxiv_public, total, ym_range)

RNG = np.random.default_rng(20261016)
HEP6 = ["hep-th", "hep-ph", "gr-qc", "nucl-th", "hep-ex", "nucl-ex"]


# ---------------------------------------------------------------- models
def event_study(ya, yb, months, base_years, lags=12, per_year=12):
    """Poisson PML event study of group A vs B (month FE, group-specific calendar effects), reference = pooled
    base_years. Returns {year: rr, lo, hi, p, b, se} and the 2026-vs-2025 contrast."""
    df = contrast_frame(ya, yb, months)
    X = pd.get_dummies(df["month"], prefix="mo", dtype=float)
    cal = sorted(df["cm"].unique())
    for c in cal[1:]:
        X[f"A_cm{c}"] = df["A"] * (df["cm"] == c)
    years = sorted(df["year"].unique())
    for k in years:
        if k not in base_years:
            X[f"A_y{k}"] = df["A"] * (df["year"] == k)
    X["A"] = df["A"].astype(float)
    res = sm.GLM(df["y"].values, X.astype(float), family=sm.families.Poisson()).fit(
        cov_type="hac-groupsum", cov_kwds={"time": df["t"].values, "maxlags": lags})
    out = {}
    for k in years:
        if k in base_years:
            continue
        b, se = float(res.params[f"A_y{k}"]), float(res.bse[f"A_y{k}"])
        out[str(k)] = {"rr": math.exp(b), "lo": math.exp(b - 1.96 * se), "hi": math.exp(b + 1.96 * se),
                       "p": float(res.pvalues[f"A_y{k}"]), "b": b, "se": se}
    if "A_y2026" in X and "A_y2025" in X:
        cv = res.cov_params()
        d = res.params["A_y2026"] - res.params["A_y2025"]
        se = math.sqrt(cv.loc["A_y2026", "A_y2026"] + cv.loc["A_y2025", "A_y2025"] - 2 * cv.loc["A_y2026", "A_y2025"])
        out["2026_vs_2025"] = {"rr": math.exp(d), "lo": math.exp(d - 1.96 * se), "hi": math.exp(d + 1.96 * se),
                               "p": float(math.erfc(abs(d / se) / math.sqrt(2)))}
    return out


def hinge_change(r, months, tau_month, lags=12, reps=999):
    """Change in the slope of a deseasonalised log series (or log ratio) after tau_month:
    r_t = a + b t + c (t - tau)_+, t in years. Newey-West CI for c, and an AR(1) parametric-bootstrap p-value."""
    y = np.asarray(r, float)
    n = len(y)
    t = np.arange(n) / 12.0
    tau = months.index(tau_month) / 12.0
    X = np.column_stack([np.ones(n), t, np.maximum(t - tau, 0)])
    m = sm.OLS(y, X).fit(cov_type="HAC", cov_kwds={"maxlags": lags})
    w_obs = hac_wald_last(X, y, lags)
    X0 = X[:, :2]
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
        exceed += hac_wald_last(X, X0 @ b0 + e, lags) >= w_obs
    c, se = float(m.params[2]), float(m.bse[2])
    return {"tau": tau_month, "slope_change_per_year": math.exp(c) - 1, "lo": math.exp(c - 1.96 * se) - 1,
            "hi": math.exp(c + 1.96 * se) - 1, "pre_slope_per_year": math.exp(float(m.params[1])) - 1,
            "p_bootstrap": (exceed + 1) / (reps + 1)}


def sup_wald(y, months, kind, trim=0.05, reps=999, lags=12, known=None):
    """Unknown-break sup-Wald (trim) or, with known=[months], Wald tests at fixed dates; AR(1) bootstrap p-values."""
    y = np.asarray(y, float)
    n = len(y)
    t = np.arange(n, dtype=float)
    taus = [months.index(k) for k in known if k in months] if known else list(range(int(n * trim), int(n * (1 - trim))))
    designs = {tau: np.column_stack([np.ones(n), t, np.maximum(t - tau, 0) if kind == "slope"
                                      else (t >= tau).astype(float)]) for tau in taus}
    stats_obs = {tau: hac_wald_last(X, y, lags) for tau, X in designs.items()}
    X0 = np.column_stack([np.ones(n), t])
    b0, *_ = np.linalg.lstsq(X0, y, rcond=None)
    e0 = y - X0 @ b0
    rho = float(np.corrcoef(e0[:-1], e0[1:])[0, 1])
    sd = float(np.std(e0[1:] - rho * e0[:-1], ddof=2))
    sup_obs = max(stats_obs.values())
    exceed_sup, exceed_each = 0, Counter()
    for _ in range(reps):
        e = np.zeros(n)
        e[0] = RNG.normal(0, sd / math.sqrt(max(1e-6, 1 - rho ** 2)))
        for i in range(1, n):
            e[i] = rho * e[i - 1] + RNG.normal(0, sd)
        yb = X0 @ b0 + e
        sb = {tau: hac_wald_last(X, yb, lags) for tau, X in designs.items()}
        exceed_sup += max(sb.values()) >= sup_obs
        if known:
            for tau in taus:
                exceed_each[tau] += sb[tau] >= stats_obs[tau]
    if known:
        return {months[tau]: {"wald": stats_obs[tau], "p_bootstrap": (exceed_each[tau] + 1) / (reps + 1)} for tau in taus}
    tau_obs = max(stats_obs, key=stats_obs.get)
    return {"break_month": months[tau_obs], "sup_wald": sup_obs, "p_bootstrap": (exceed_sup + 1) / (reps + 1),
            "last_candidate": months[taus[-1]], "trim": trim}


def placebo_p(obs_log, null_logs):
    null = np.abs(np.asarray(null_logs))
    return float((np.sum(null >= abs(obs_log)) + 1) / (len(null) + 1))


PERIODS = ["2023-2024", "2025", "2026"]
Z_BONF3 = 2.3940  # two-sided 98.33% (Bonferroni over the three confirmatory contrasts)


def _rr(b, se, z=1.96):
    return {"rr": math.exp(b), "lo": math.exp(b - z * se), "hi": math.exp(b + z * se), "b": b, "se": se}


def planned_v1(ya, yb, months, base_from, lags=12, reps=999, block=12):
    """The specification planned in draft v1 (essay branch, 697fb25), reported beside the 2022-base estimate as run:
    log E[y_gt] = a_g + c_m(t) + b_p(t) + th_p(t) D_g, periods 2023-2024, 2025 and 2026 against a multi-year baseline
    (base_from to December 2022), calendar-month effects common to both groups, D_g = 1 for the non-experimental group.
    Poisson, replaced by a negative binomial (NB2, dispersion by maximum likelihood) if the Cameron-Trivedi test finds
    overdispersion at the 5% level; Newey-West errors in their panel (Driscoll-Kraay) form, 12 lags; a moving-block
    bootstrap of exp(th_2026) as a check (residuals of the log ratio, 12-month blocks); group-specific linear trends
    as a sensitivity. Bonferroni intervals (98.3%) for the three contrasts."""
    keep = [i for i, m in enumerate(months) if m >= base_from]
    ms = [months[i] for i in keep]
    ya, yb = np.asarray(ya, float)[keep], np.asarray(yb, float)[keep]
    df = contrast_frame(ya, yb, ms)
    period = np.where(df["year"] <= 2022, "base", np.where(df["year"] <= 2024, "2023-2024", df["year"].astype(str)))

    def design(trend=False):
        X = pd.DataFrame({"const": 1.0, "A": df["A"].astype(float)})
        for c in range(2, 13):
            X[f"cm{c}"] = (df["cm"] == c).astype(float)
        for p in PERIODS:
            X[f"P{p}"] = (period == p).astype(float)
            X[f"A_P{p}"] = df["A"] * (period == p)
        if trend:
            X["t"] = df["t"] / 12.0
            X["A_t"] = df["A"] * df["t"] / 12.0
        return X.astype(float)

    def fit(X, family):
        return sm.GLM(df["y"].values, X, family=family).fit(
            cov_type="hac-groupsum", cov_kwds={"time": df["t"].values, "maxlags": lags})

    def periods(res, z=1.96):
        return {p: _rr(float(res.params[f"A_P{p}"]), float(res.bse[f"A_P{p}"]), z) for p in PERIODS}

    X = design()
    pois = fit(X, sm.families.Poisson())
    mu = sm.GLM(df["y"].values, X, family=sm.families.Poisson()).fit().mu
    mu = np.asarray(mu)
    aux = sm.OLS(((df["y"].values - mu) ** 2 - df["y"].values) / mu, mu).fit()
    a_ct, t_ct, p_ct = (float(np.asarray(v)[0]) for v in (aux.params, aux.tvalues, aux.pvalues))
    ct = {"alpha": a_ct, "t": t_ct, "p_one_sided": p_ct / 2 if a_ct > 0 else 1 - p_ct / 2,
          "pearson_dispersion": float(np.sum((df["y"].values - mu) ** 2 / mu) / (len(mu) - X.shape[1]))}
    out = {"window": [ms[0], ms[-1]], "baseline": f"{ms[0]} to 2022-12", "overdispersion": ct,
           "poisson": periods(pois)}
    alpha = float(np.asarray(sm.NegativeBinomial(df["y"].values, X, loglike_method="nb2").fit(
        disp=0, maxiter=500).params)[-1])
    nb = fit(X, sm.families.NegativeBinomial(alpha=alpha))
    out["negative_binomial"] = dict(periods(nb), alpha=alpha)
    chosen, label = (nb, "negative_binomial") if ct["p_one_sided"] < 0.05 else (pois, "poisson")
    out["planned_model"] = label
    out["planned_2026"] = periods(chosen)["2026"]
    out["planned_2026_bonferroni"] = periods(chosen, Z_BONF3)["2026"]
    out["planned_2026"]["p"] = float(chosen.pvalues["A_P2026"])
    out["mde_2026_80pct_power"] = math.exp(2.8 * out["planned_2026"]["se"]) - 1
    # moving-block bootstrap (check): residuals of the monthly log ratio around the period model
    r = np.log(ya) - np.log(yb)
    pr = period[df["A"].values == 1]
    cm = np.array([int(m[5:]) for m in ms])
    Z = np.column_stack([np.ones(len(r))] + [(cm == c).astype(float) for c in range(2, 13)] +
                        [(pr == p).astype(float) for p in PERIODS])
    beta, *_ = np.linalg.lstsq(Z, r, rcond=None)
    fitted, resid = Z @ beta, r - Z @ beta
    n, draws = len(r), []
    for _ in range(reps):
        idx = []
        while len(idx) < n:
            s = RNG.integers(0, n - block + 1)
            idx.extend(range(s, s + block))
        bb, *_ = np.linalg.lstsq(Z, fitted + resid[np.array(idx[:n])], rcond=None)
        draws.append(bb[-1])
    lo, hi = np.percentile(draws, [2.5, 97.5])
    out["block_bootstrap_2026"] = {"rr": math.exp(beta[-1]), "lo": math.exp(lo), "hi": math.exp(hi)}
    tr = fit(design(trend=True), sm.families.NegativeBinomial(alpha=alpha) if label == "negative_binomial"
             else sm.families.Poisson())
    out["with_group_trends"] = dict(periods(tr), trend_ratio_per_year=math.exp(float(tr.params["A_t"])))
    return out


def rank_calibration(ya, yb, months, pre_last=2022, target=2026, lags=12):
    """In-time calibration with the estimator itself (event study: month effects, group-specific calendar effects),
    replacing the year-shock z. Level: the target year's log rate ratio against all years up to pre_last pooled,
    compared with each of those years' log rate ratio against the other years pooled (leave-one-out base, so every
    statistic is centred on the pre-period mean). Acceleration: the change from the year before the target, compared
    with the year-on-year changes before it (up to pre_last, and up to the year before the target). Rank p values
    count the comparison values at least as large, plus one, over their number plus one: two-sided on absolute values
    and one-sided in the direction of the observed statistic."""
    years = sorted({int(m[:4]) for m in months})
    pre = [y for y in years if y <= pre_last]

    def rank(obs, ref):
        ref = np.asarray(ref, float)
        two = float((np.sum(np.abs(ref) >= abs(obs)) + 1) / (len(ref) + 1))
        one = float((np.sum(ref * np.sign(obs) >= abs(obs)) + 1) / (len(ref) + 1))
        return {"stat": obs, "n_ref": int(len(ref)), "p_two_sided": two, "p_one_sided": one}

    ev = event_study(ya, yb, months, set(pre), lags=lags)
    loo = [event_study(ya, yb, months, set(pre) - {k}, lags=lags)[str(k)]["b"] for k in pre]
    b = {y: (ev[str(y)]["b"] if str(y) in ev else 0.0) for y in years}
    out = {"level": dict(rank(b[target], loo), rr=math.exp(b[target]), ref_years=pre,
                         ref_rr={str(k): math.exp(v) for k, v in zip(pre, loo)})}
    # year-on-year changes need a coefficient for every year: the pooled base above sets every pre-period change to
    # zero. With one base year they are differences of year coefficients and do not depend on which year it is.
    ev1 = event_study(ya, yb, months, {pre_last}, lags=lags)
    b1 = {y: (ev1[str(y)]["b"] if str(y) in ev1 else 0.0) for y in years}
    ch = {y: b1[y] - b1[y - 1] for y in years if y - 1 in b1}
    out["acceleration_pre_period"] = dict(rank(ch[target], [ch[y] for y in ch if y <= pre_last]),
                                          rr=math.exp(ch[target]))
    out["acceleration_all_earlier"] = dict(rank(ch[target], [ch[y] for y in ch if y < target]),
                                           rr=math.exp(ch[target]),
                                           ref_rr={str(y): math.exp(ch[y]) for y in ch if y < target})
    return out


# ---------------------------------------------------------------- sections
def contrasts(repo):
    ax, bx = load_arxiv(repo), load_biorxiv(repo)
    m15, m19 = ym_range("2015-01", LAST), ym_range("2019-01", LAST)
    theory_no_grqc = [a for a in THEORY if a != "gr-qc"]
    out = {
        "C1_theory_vs_experiment": (total(ax, THEORY, m15), total(ax, EXPERIMENT, m15), m15),
        "C1_theory_without_gr-qc_vs_experiment": (total(ax, theory_no_grqc, m15), total(ax, EXPERIMENT, m15), m15),
        "hep-ph_vs_hep-ex": (total(ax, ["hep-ph"], m15), total(ax, ["hep-ex"], m15), m15),
        "hep-th_vs_hep-ex": (total(ax, ["hep-th"], m15), total(ax, ["hep-ex"], m15), m15),
        "gr-qc_vs_experiment": (total(ax, ["gr-qc"], m15), total(ax, EXPERIMENT, m15), m15),
        "C2_computational_vs_wet_lab": (total(bx, COMPUTATIONAL, m19), total(bx, WET_LAB, m19), m19)}
    med = load_medrxiv_public(repo)
    if med:
        m = ym_range("2019-07", LAST)
        out["C3_public_dataset_vs_other"] = (np.array([med[0][x] for x in m], float),
                                             np.array([med[1][x] for x in m], float), m)
    return out, ax, bx


def section_estimands(repo):
    C, ax, bx = contrasts(repo)
    m15, m19 = ym_range("2015-01", LAST), ym_range("2019-01", LAST)
    # in-space placebo distributions of the 2026 log rate ratio (base 2022), as in the P1 negative controls
    archives = sorted(a for a in ax if all(ax[a].get(m, 0) > 0 for m in m15))
    pair_logs = [event_study(total(ax, [a], m15), total(ax, [b], m15), m15, {2022})["2026"]["b"]
                 for a, b in combinations(archives, 2)]
    halves = []
    for half in combinations(WET_LAB, 6):
        if WET_LAB[0] in half:
            other = [c for c in WET_LAB if c not in half]
            halves.append(event_study(total(bx, list(half), m19), total(bx, other, m19), m19, {2022})["2026"]["b"])
    res = {"placebo_distributions": {"arxiv_archive_pairs": len(pair_logs), "wet_lab_halves": len(halves)}}
    for name, (ya, yb, ms) in C.items():
        first = int(ms[0][:4])
        bases = {"2022": {2022}}
        if first <= 2017:
            bases["2017-2019"] = {2017, 2018, 2019}
            bases["2017-2019+2022"] = {2017, 2018, 2019, 2022}
        else:
            bases["2019"] = {first} if first == 2019 else set()
            bases["2019+2022"] = {2019, 2022}
        bases = {k: v for k, v in bases.items() if v}
        r = {"window": [ms[0], ms[-1]], "by_base": {}}
        for bname, bset in bases.items():
            ev = event_study(ya, yb, ms, bset)
            r["by_base"][bname] = {"event_study": ev}
        ev22 = r["by_base"]["2022"]["event_study"]
        null = pair_logs if not name.startswith(("C2", "C3")) else halves if name.startswith("C2") else None
        if null is not None:
            r["placebo_p_2026"] = placebo_p(ev22["2026"]["b"], null)
            r["placebo_reference"] = "arxiv_archive_pairs" if null is pair_logs else "wet_lab_halves"
        lr = deseasonalised_log_ratio(ya, yb, ms, upto="2022-12")
        r["slope_change_after_2022_12"] = hinge_change(lr, ms, "2022-12")
        r["slope_change_after_2024_11"] = hinge_change(lr, ms, "2024-11")
        res[name] = r
    # field level: in-space placebo rank of each field-like series' 2026 departure among archives
    dep = {a: field_model([ax[a].get(m, 0) for m in m15], m15)["2026"]["rr"] for a in archives}
    res["archive_departures_2026"] = dict(sorted(dep.items(), key=lambda kv: -kv[1]))
    res["math_rank_p"] = float(np.mean([v >= dep["math"] for v in dep.values()]))
    return res


PLANNED_BASE_FROM = {"C1_theory_vs_experiment": "2017-01", "C1_theory_without_gr-qc_vs_experiment": "2017-01",
                     "C2_computational_vs_wet_lab": "2019-01", "C3_public_dataset_vs_other": "2019-07"}


def section_planned(repo):
    """Round 2 (R1 N7, R4 N3): the specification planned in draft v1, beside the 2022-base estimate as run."""
    C, _, _ = contrasts(repo)
    out = {}
    for name, base_from in PLANNED_BASE_FROM.items():
        if name not in C:
            continue
        ya, yb, ms = C[name]
        r = planned_v1(ya, yb, ms, base_from)
        r["as_run_2022_base_2026"] = event_study(ya, yb, ms, {2022})["2026"]
        out[name] = r
    return out


def section_calibration(repo):
    """Round 2 (R1 N1): rank-based in-time calibration with the estimator itself, replacing the year-shock z: the
    within-field contrasts, the arXiv groups against bioRxiv (output) and PubMed US vs non-US."""
    C, ax, bx = contrasts(repo)
    out = {}
    for name in ("C1_theory_vs_experiment", "C1_theory_without_gr-qc_vs_experiment", "C2_computational_vs_wet_lab",
                 "C3_public_dataset_vs_other"):
        if name in C:
            out[name] = rank_calibration(*C[name])
    m19 = ym_range("2019-01", LAST)
    yb = total(bx, list(bx), m19)
    for g, arch in (("arxiv_physics_6", HEP6), ("arxiv_theory", THEORY), ("arxiv_experiment", EXPERIMENT),
                    ("arxiv_maths", ["math"])):
        out[f"{g}_vs_biorxiv"] = rank_calibration(total(ax, arch, m19), yb, m19)
    pub = json.load(open(os.path.join(repo, "data/raw/pubmed_us_quarterly.json")))
    lab = [f"{r['quarter'][:4]}-{3 * int(r['quarter'][-1]):02d}" for r in pub]
    out["pubmed_us_vs_non_us"] = rank_calibration(np.array([r["us_affiliation"] for r in pub], float),
                                                  np.array([r["non_us"] for r in pub], float), lab, lags=4)
    return out


def year_effects_fast(ya, yb, months, base=2022):
    """Point estimates of the event study's year effects (base year 0). With month fixed effects the Poisson model is
    the binomial logit of group A's share of each month's papers on group-specific calendar-month and year effects, so
    this IRLS fit returns the same coefficients as event_study in a fraction of the time (used for the placebos)."""
    yrs = sorted({int(m[:4]) for m in months})
    n = np.asarray(ya, float) + np.asarray(yb, float)
    keep = n > 0
    cm = np.array([int(m[5:]) for m in months])
    yr = np.array([int(m[:4]) for m in months])
    X = np.column_stack([np.ones(len(months))] + [(cm == c).astype(float) for c in range(2, 13)] +
                        [(yr == k).astype(float) for k in yrs if k != base])[keep]
    y, n = np.asarray(ya, float)[keep], n[keep]
    beta = np.zeros(X.shape[1])
    beta[0] = math.log(y.sum() / (n - y).sum())
    for _ in range(50):
        pi = 1 / (1 + np.exp(-(X @ beta)))
        w = n * pi * (1 - pi)
        step = np.linalg.solve(X.T @ (X * w[:, None]), X.T @ (y - n * pi))
        beta += step
        if np.max(np.abs(step)) < 1e-10:
            break
    names = [k for k in yrs if k != base]
    return {k: float(b) for k, b in zip(names, beta[12:])}


def planned_fast(ya, yb, months, base_from):
    """Point estimates of planned_v1 for the placebos: the same design, Poisson by IRLS, the Cameron-Trivedi test, and
    NB2 with the dispersion maximising the profile likelihood when the test rejects at 5%. Returns the 2026 and 2025
    period effects of group A (log scale) and the model used."""
    from scipy.optimize import minimize_scalar
    from scipy.special import gammaln
    from scipy.stats import t as tdist
    keep = [i for i, m in enumerate(months) if m >= base_from]
    ms = [months[i] for i in keep]
    n = len(ms)
    cm = np.array([int(m[5:]) for m in ms])
    yr = np.array([int(m[:4]) for m in ms])
    per = np.where(yr <= 2022, "base", np.where(yr <= 2024, "2023-2024", yr.astype(str)))

    def block(a):
        cols = [np.ones(n), np.full(n, float(a))] + [(cm == c).astype(float) for c in range(2, 13)]
        for p in PERIODS:
            cols += [(per == p).astype(float), a * (per == p).astype(float)]
        return np.column_stack(cols)
    X = np.vstack([block(1), block(0)])
    y = np.concatenate([np.asarray(ya, float)[keep], np.asarray(yb, float)[keep]])
    i25, i26 = 2 + 11 + 2 * PERIODS.index("2025") + 1, 2 + 11 + 2 * PERIODS.index("2026") + 1

    def irls(alpha, beta):
        for _ in range(100):
            eta = X @ beta
            mu = np.exp(eta)
            w = mu / (1 + alpha * mu)
            xtw = X.T * w
            new = np.linalg.solve(xtw @ X, xtw @ (eta + (y - mu) / mu))
            done = np.max(np.abs(new - beta)) < 1e-10
            beta = new
            if done:
                break
        return beta, np.exp(X @ beta)
    b0 = np.zeros(X.shape[1])
    b0[0] = math.log(y.mean())
    bp, mu = irls(0.0, b0)
    z = ((y - mu) ** 2 - y) / mu
    a_ct = float(np.sum(z * mu) / np.sum(mu * mu))
    s2 = float(np.sum((z - a_ct * mu) ** 2) / (len(y) - 1))
    t_ct = a_ct / math.sqrt(s2 / float(np.sum(mu * mu)))
    if tdist.sf(t_ct, len(y) - 1) >= 0.05:
        return float(bp[i26]), float(bp[i25]), "poisson"
    state = {"b": bp}

    def negll(la):
        a = math.exp(la)
        b, m = irls(a, state["b"])
        state["b"] = b
        r = 1 / a
        return -float(np.sum(gammaln(y + r) - gammaln(r) - gammaln(y + 1) + y * np.log(a * m / (1 + a * m)) -
                             r * np.log1p(a * m)))
    la = minimize_scalar(negll, bounds=(math.log(1e-6), math.log(2.0)), method="bounded",
                         options={"xatol": 1e-6}).x
    b, _ = irls(math.exp(la), state["b"])
    return float(b[i26]), float(b[i25]), "negative_binomial"


def section_placebos_matched(repo):
    """Round 2 (item 8; R1 #7, R3 #7): in-space placebos matched to each contrast's structure, with the observed
    contrast counted among them, so p cannot fall below 1/n (the floor). C1 (four theory archives against two
    experimental ones): every split of the six particle and nuclear physics archives into four against two (15), and
    every disjoint draw of four against two of the 13 physics archives (25,740). C1 without gr-qc (three against two):
    the ten splits of the five archives, and the 12,870 draws from the 13 physics archives. C2 (three computational
    against twelve wet-lab categories): every choice of three of the fifteen categories as the computational group
    (455). Statistics, from the event-study estimator as run (base 2022) and from the planned specification (period
    effects against the multi-year baseline, NB2 when overdispersed; planned_fast): the 2026 log rate ratio and the
    2026/2025 log ratio; p two-sided on absolute values, one-sided in the observed direction."""
    ax, bx = load_arxiv(repo), load_biorxiv(repo)
    m15, m19 = ym_range("2015-01", LAST), ym_range("2019-01", LAST)
    out = {}

    def stats(ya, yb, ms, base_from):
        e = year_effects_fast(ya, yb, ms)
        p26, p25, _ = planned_fast(ya, yb, ms, base_from)
        return e[2026], e[2026] - e[2025], p26, p26 - p25

    def summarise(obs, draws):
        res = {"n": len(draws), "floor": 1 / len(draws)}
        for name, j in (("2026_vs_2022", 0), ("2026_vs_2025", 1), ("planned_2026_vs_base", 2),
                        ("planned_2026_vs_2025", 3)):
            v, o = np.array([d[j] for d in draws]), obs[j]
            res[name] = {"observed_rr": math.exp(o), "p_two_sided": float(np.mean(np.abs(v) >= abs(o) - 1e-12)),
                         "p_one_sided": float(np.mean(v * np.sign(o) >= abs(o) - 1e-12)),
                         "placebo_rr_5_50_95": [float(math.exp(q)) for q in np.percentile(v, [5, 50, 95])]}
        return res

    hep_nucl = ["hep-th", "hep-ph", "gr-qc", "nucl-th", "hep-ex", "nucl-ex"]
    for name, A, B, pool6 in (("C1_theory_vs_experiment", THEORY, EXPERIMENT, hep_nucl),
                              ("C1_theory_without_gr-qc_vs_experiment", ["hep-th", "hep-ph", "nucl-th"], EXPERIMENT,
                               [a for a in hep_nucl if a != "gr-qc"])):
        base_from = PLANNED_BASE_FROM[name]
        obs = stats(total(ax, A, m15), total(ax, B, m15), m15, base_from)
        k, j = len(A), len(B)
        within = [stats(total(ax, list(a), m15), total(ax, [x for x in pool6 if x not in a], m15), m15, base_from)
                  for a in combinations(pool6, k)]
        cache = {a: total(ax, [a], m15) for a in PHYSICS}
        draws = []
        for a in combinations(PHYSICS, k):
            ya = sum(cache[x] for x in a)
            for b in combinations([x for x in PHYSICS if x not in a], j):
                draws.append(stats(ya, sum(cache[x] for x in b), m15, base_from))
        out[name] = {"observed": {"rr_2026_vs_2022": math.exp(obs[0]), "rr_2026_vs_2025": math.exp(obs[1]),
                                  "planned_rr_2026_vs_base": math.exp(obs[2]),
                                  "planned_rr_2026_vs_2025": math.exp(obs[3])},
                     "splits_of_the_hep_nucl_archives": summarise(obs, within),
                     "draws_from_13_physics_archives": summarise(obs, draws)}
        print("placebos", name, len(within), len(draws), flush=True)
    cats = list(COMPUTATIONAL) + list(WET_LAB)
    cache = {c: total(bx, [c], m19) for c in cats}
    allsum = sum(cache.values())
    base_from = PLANNED_BASE_FROM["C2_computational_vs_wet_lab"]
    obs = stats(sum(cache[c] for c in COMPUTATIONAL), sum(cache[c] for c in WET_LAB), m19, base_from)
    draws = []
    for a in combinations(cats, len(COMPUTATIONAL)):
        ya = sum(cache[c] for c in a)
        draws.append(stats(ya, allsum - ya, m19, base_from))
    out["C2_computational_vs_wet_lab"] = {"observed": {"rr_2026_vs_2022": math.exp(obs[0]),
                                                       "rr_2026_vs_2025": math.exp(obs[1]),
                                                       "planned_rr_2026_vs_base": math.exp(obs[2]),
                                                       "planned_rr_2026_vs_2025": math.exp(obs[3])},
                                          "three_of_the_fifteen_categories": summarise(obs, draws)}
    return out


def section_breaks(repo):
    ax = load_arxiv(repo)
    m15 = ym_range("2015-01", LAST)
    series = {"physics_13_archives": ([sum(ax[a].get(m, 0) for a in PHYSICS) for m in m15], m15),
              "hep_nucl_6_archives": ([sum(ax[a].get(m, 0) for a in HEP6) for m in m15], m15),
              "mathematics": ([ax["math"].get(m, 0) for m in m15], m15),
              "computer_science": ([ax["cs"].get(m, 0) for m in m15], m15)}
    bio = json.load(open(os.path.join(repo, "data/raw/biorxiv_sum_m.json")))["bioRxiv content statistics"]
    bm = {r["month"]: int(r["new_papers"]) for r in bio}
    m18 = ym_range("2018-01", LAST)
    series["biorxiv"] = ([bm[m] for m in m18], m18)
    known = ["2022-12", "2024-11", "2025-11"]
    out = {}
    for name, (y, ms) in series.items():
        ly = deseason_log(y, ms, upto="2022-12")
        out[name] = {"slope_unknown_trim5": sup_wald(ly, ms, "slope"), "level_unknown_trim5": sup_wald(ly, ms, "level"),
                     "slope_known": sup_wald(ly, ms, "slope", known=known),
                     "level_known": sup_wald(ly, ms, "level", known=known)}
        print("breaks", name, out[name]["slope_unknown_trim5"], flush=True)
    C, _, _ = contrasts(repo)
    for name in ("C1_theory_vs_experiment", "C2_computational_vs_wet_lab"):
        ya, yb, ms = C[name]
        lr = deseasonalised_log_ratio(ya, yb, ms, upto="2022-12")
        out[name] = {"slope_unknown_trim5": sup_wald(lr, ms, "slope"), "level_unknown_trim5": sup_wald(lr, ms, "level"),
                     "slope_known": sup_wald(lr, ms, "slope", known=known),
                     "level_known": sup_wald(lr, ms, "level", known=known)}
    return out


def section_crosslists(repo):
    new, both = defaultdict(lambda: defaultdict(int)), defaultdict(lambda: defaultdict(int))
    for r in csv.DictReader(open(os.path.join(repo, "data/raw/arxiv_archive_monthly.csv"))):
        m = f"{r['year']}-{int(r['month']):02d}"
        new[r["archive"]][m] += int(r["new"])
        both[r["archive"]][m] += int(r["new"]) + int(r["cross"])
    m15 = ym_range("2015-01", LAST)
    out = {"fields": {}, "archives": {}}
    for label, src in (("new", new), ("new_plus_cross", both)):
        for f, arch in (("physics_13_archives", PHYSICS), ("hep_nucl_6_archives", HEP6), ("mathematics", ["math"]),
                        ("computer_science", ["cs"])):
            out["fields"].setdefault(f, {})[label] = field_model([sum(src[a].get(m, 0) for a in arch) for m in m15], m15)
        archives = sorted(a for a in src if all(src[a].get(m, 0) > 0 for m in m15))
        dep = {a: field_model([src[a].get(m, 0) for m in m15], m15)["2026"]["rr"] for a in archives}
        out["archives"][label] = {"departure_2026": dict(sorted(dep.items(), key=lambda kv: -kv[1])),
                                  "math_rank_p": float(np.mean([v >= dep["math"] for v in dep.values()]))}
    share = {a: sum(both[a].get(m, 0) - new[a].get(m, 0) for m in m15 if m >= "2026-01") /
             max(1, sum(both[a].get(m, 0) for m in m15 if m >= "2026-01")) for a in sorted(both)}
    out["cross_list_share_of_entries_2026"] = share
    return out


def section_funding(repo):
    out = {}
    pub = json.load(open(os.path.join(repo, "data/raw/pubmed_us_quarterly.json")))
    qs = [r["quarter"] for r in pub]
    lab = [f"{q[:4]}-{3 * int(q[-1]):02d}" for q in qs]
    ya = np.array([r["us_affiliation"] for r in pub], float)
    yb = np.array([r["non_us"] for r in pub], float)
    out["pubmed_us_vs_non_us"] = {"quarters": [qs[0], qs[-1]],
                                  "us_share": {q: r["us_affiliation"] / r["journal_article"] for q, r in zip(qs, pub)},
                                  "base_2022": event_study(ya, yb, lab, {2022}, lags=4),
                                  "base_2023_2024": event_study(ya, yb, lab, {2023, 2024}, lags=4)}
    path = os.path.join(repo, "data/processed/biorxiv_records_country_monthly.csv")
    if os.path.exists(path):
        cnt = defaultdict(lambda: defaultdict(int))
        for r in csv.DictReader(open(path)):
            cnt[(r["group"], r["country"])][r["month"]] += int(r["preprints"])
        ms = ym_range("2022-01", LAST)
        for g in ("wet_lab", "computational", "mixed", "all"):
            us = np.array([sum(cnt[(gg, "US")].get(m, 0) for gg in (["wet_lab", "computational", "mixed"]
                                                                     if g == "all" else [g])) for m in ms], float)
            non = np.array([sum(cnt[(gg, "non-US")].get(m, 0) for gg in (["wet_lab", "computational", "mixed"]
                                                                         if g == "all" else [g])) for m in ms], float)
            if us.min() > 0 and non.min() > 0:
                out[f"biorxiv_{g}_us_vs_non_us"] = {"base_2022": event_study(us, non, ms, {2022}),
                                                    "base_2023_2024": event_study(us, non, ms, {2023, 2024}),
                                                    "us_share_by_year": {str(y): float(sum(us[i] for i, m in enumerate(ms)
                                                                                           if m.startswith(str(y))) /
                                                                                       sum(us[i] + non[i] for i, m in
                                                                                           enumerate(ms) if m.startswith(str(y))))
                                                                         for y in range(2022, 2027)}}
    return out


FUNDING_PREDICTION = (
    "Stated before the bioRxiv split was read (draft v3, Discussion, explanation (i)): if the 2025 disruption of US "
    "research funding drove the 2026 wet-lab slowdown, US wet-lab preprints fall relative to non-US wet-lab preprints "
    "in 2025-2026 against 2023-2024 (ratio below 1), and by more than computational preprints do (wet-lab ratio "
    "below the computational one).")


def section_funding_round2(repo):
    """Round 2 (item 10; R1 N5, R3 #4): bioRxiv by the corresponding author's institution (US or elsewhere) against the
    prediction in FUNDING_PREDICTION; the medRxiv split (all preprints and without COVID-19); PubMed's US/non-US
    ratio calibrated in time (its year-on-year and two-year changes against the earlier ones). Event studies as in
    P1c (bases 2023-2024 and 2022); preprints whose institution has no country stay out of both groups, and their
    share is reported. The country classifier (scripts/classify_country.py) was checked by an AI agent only; a sheet
    for a human spot check is in docs/stats/validation/country_spot_check_sheet.csv."""
    out = {"prediction": FUNDING_PREDICTION}
    path = os.path.join(repo, "data/processed/biorxiv_records_country_monthly.csv")
    cnt = defaultdict(lambda: defaultdict(int))
    for r in csv.DictReader(open(path)):
        cnt[(r["group"], r["country"])][r["month"]] += int(r["preprints"])
    ms = ym_range("2019-01", LAST)
    groups = {"wet_lab": ["wet_lab"], "computational": ["computational"], "mixed": ["mixed"],
              "all": ["wet_lab", "computational", "mixed"]}
    bio = {}
    for g, gg in groups.items():
        series = {c: np.array([sum(cnt[(x, c)].get(m, 0) for x in gg) for m in ms], float)
                  for c in ("US", "non-US", "unknown")}
        jan_sep = {str(y): {c: int(sum(v[i] for i, m in enumerate(ms) if m[:4] == str(y) and m[5:] <= "09"))
                            for c, v in series.items()} for y in range(2019, 2027)}
        bio[g] = {"base_2023_2024": event_study(series["US"], series["non-US"], ms, {2023, 2024}),
                  "base_2022": event_study(series["US"], series["non-US"], ms, {2022}),
                  "jan_sep_counts": jan_sep}
    # wet lab against computational: ratio of the two US/non-US ratios (independent fits, conservative interval)
    wl, cp = bio["wet_lab"]["base_2023_2024"], bio["computational"]["base_2023_2024"]
    bio["wet_lab_vs_computational"] = {}
    for y in ("2025", "2026"):
        la, lb = math.log(wl[y]["rr"]), math.log(cp[y]["rr"])
        d, se = la - lb, math.sqrt(wl[y]["se"] ** 2 + cp[y]["se"] ** 2)
        bio["wet_lab_vs_computational"][y] = {"rr": math.exp(d), "lo": math.exp(d - 1.96 * se),
                                              "hi": math.exp(d + 1.96 * se)}
    out["biorxiv"] = bio
    med = defaultdict(Counter)
    for r in csv.DictReader(gzip.open(os.path.join(repo, "data/raw/medrxiv_records.csv.gz"), "rt")):
        m = r["date"][:7]
        med[(r["country"], "all")][m] += 1
        if r["covid_title_abstract"] != "1":
            med[(r["country"], "noncovid")][m] += 1
    mm = ym_range("2019-07", LAST)
    medo = {}
    for scope in ("all", "noncovid"):
        us = np.array([med[("US", scope)].get(m, 0) for m in mm], float)
        non = np.array([med[("non-US", scope)].get(m, 0) for m in mm], float)
        unk = np.array([med[("unknown", scope)].get(m, 0) for m in mm], float)
        js = {}
        for y in range(2020, 2027):
            sel = [i for i, m in enumerate(mm) if m[:4] == str(y) and m[5:] <= "09"]
            js[str(y)] = {"US": int(us[sel].sum()), "non-US": int(non[sel].sum()), "unknown": int(unk[sel].sum())}
        medo[scope] = {"base_2023_2024": event_study(us, non, mm, {2023, 2024}),
                       "base_2022": event_study(us, non, mm, {2022}), "jan_sep_counts": js}
    out["medrxiv"] = medo
    pub = json.load(open(os.path.join(repo, "data/raw/pubmed_us_quarterly.json")))
    lab = [f"{r['quarter'][:4]}-{3 * int(r['quarter'][-1]):02d}" for r in pub if
           f"{r['quarter'][:4]}-{3 * int(r['quarter'][-1]):02d}" <= LAST]
    ev = event_study(np.array([r["us_affiliation"] for r in pub][:len(lab)], float),
                     np.array([r["non_us"] for r in pub][:len(lab)], float), lab, {2022}, lags=4)
    years = sorted({int(m[:4]) for m in lab})
    b = {y: (ev[str(y)]["b"] if str(y) in ev else 0.0) for y in years}
    one = {y: b[y] - b[y - 1] for y in years if y - 1 in b}
    two = {y: b[y] - b[y - 2] for y in years if y - 2 in b}

    def rank(obs, ref):
        ref = np.asarray(ref)
        return {"rr": math.exp(obs), "n_ref": len(ref),
                "p_one_sided_fall": float((np.sum(ref <= obs) + 1) / (len(ref) + 1)),
                "p_two_sided": float((np.sum(np.abs(ref) >= abs(obs)) + 1) / (len(ref) + 1))}
    out["pubmed_us_vs_non_us"] = {
        "year_on_year_change": {str(y): math.exp(v) for y, v in one.items()},
        "two_year_change": {str(y): math.exp(v) for y, v in two.items()},
        "rank_2025_change": rank(one[2025], [one[y] for y in one if y < 2025]),
        "rank_2026_change": rank(one[2026], [one[y] for y in one if y < 2026]),
        "rank_2024_to_2026": rank(two[2026], [two[y] for y in two if y < 2026])}
    return out

def section_medrxiv_flags(repo):
    """P3: medRxiv COVID-19 filter (title only vs title or abstract) and the public-dataset list extended with the
    four datasets of Spick et al. that it lacked (FinnGen, CHARLS, CDC WONDER, TriNetX); C3 re-estimated each way.
    Reads data/processed/medrxiv_flags_monthly.csv (build_rxiv_records.py)."""
    path = os.path.join(repo, "data/processed/medrxiv_flags_monthly.csv")
    if not os.path.exists(path):
        return None
    rows = {r["month"]: {k: int(v) for k, v in r.items() if k != "month"} for r in csv.DictReader(open(path))}
    ms = [m for m in ym_range("2019-07", LAST) if m in rows]
    col = lambda k: np.array([rows[m][k] for m in ms], float)  # noqa: E731
    variants = {
        "original_list_title_or_abstract_covid": (col("public_noncovid"), col("noncovid") - col("public_noncovid")),
        "extended_list_title_or_abstract_covid": (col("public_or_spick4_noncovid"),
                                                  col("noncovid") - col("public_or_spick4_noncovid")),
        "original_list_title_only_covid": (col("public_noncovid_title_only"),
                                           col("noncovid_title_only") - col("public_noncovid_title_only"))}
    out = {"C3_variants": {k: {"base_2022": event_study(a, b, ms, {2022}), "base_2019_2022": event_study(a, b, ms, {2019, 2022})}
                           for k, (a, b) in variants.items()}}
    by_year = defaultdict(Counter)
    for m in ms:
        by_year[m[:4] + ("" if m[5:] <= "09" else "-OctDec")].update(rows[m])
    out["by_year_jan_sep"] = {y: dict(c) for y, c in sorted(by_year.items()) if "-" not in y}

    def q_index(key):
        q = defaultdict(int)
        for m in ms:
            q[f"{m[:4]}-Q{(int(m[5:]) - 1) // 3 + 1}"] += rows[m][key]
        base = sum(q[f"2022-Q{i}"] for i in range(1, 5)) / 4
        return {k: 100 * v / base for k, v in sorted(q.items())}
    out["noncovid_index_2022_100"] = {"title_or_abstract": q_index("noncovid"), "title_only": q_index("noncovid_title_only")}
    return out


INSPIRE_EXP_CATS = {"Experiment-HEP", "Experiment-Nucl"}
NON_RESEARCH_DOCS = {"conference paper", "proceedings", "review", "thesis", "lectures", "book", "book chapter",
                     "activity report", "note"}


def inspire_classes(r, variant="main"):
    """ND-INSPIRE: a research article in an experimental INSPIRE category, linked to an accelerator experiment or a
    collaboration, without prospect or sensitivity wording; NN-INSPIRE: everything else in scope.
    Variants: no_link (link not required), title_prospect (prospect wording in the title only), no_prospect (wording
    ignored), primary_exp (experimental = primary arXiv category hep-ex or nucl-ex instead of INSPIRE category)."""
    docs = set(filter(None, r["document_type"].split(";"))) | set(filter(None, r["publication_type"].split(";")))
    research = "article" in docs and not (docs & NON_RESEARCH_DOCS)
    cats = set(filter(None, r["inspire_categories"].split(";")))
    exp = (r["primary"] in ("hep-ex", "nucl-ex")) if variant == "primary_exp" else bool(cats & INSPIRE_EXP_CATS)
    linked = True if variant == "no_link" else bool(r["experiments"] or r["collaborations"])
    if variant == "no_prospect":
        prospect = False
    elif variant == "title_prospect":
        prospect = r["prospect_title"] == "1"
    else:
        prospect = r["prospect_title_abstract"] == "1"
    return "ND" if research and exp and linked and not prospect else "NN"


def section_inspire(repo):
    """Pre-registration section 10 (exploratory): departures from the pre-2023 trend in 2025-2026 by INSPIRE class,
    overall and within hep-ex and nucl-ex, by collaboration size and by document type."""
    path = os.path.join(repo, "data/raw/inspire_hep_records.csv.gz")
    if not os.path.exists(path):
        return None
    recs = [r for r in csv.DictReader(gzip.open(path, "rt")) if "2017-01" <= r["date"][:7] <= LAST]
    ms = ym_range("2017-01", LAST)

    def series(keep):
        c = Counter(r["date"][:7] for r in recs if keep(r))
        return [c.get(m, 0) for m in ms]

    def dep(y):
        if min(y) <= 0:
            return None
        fm = field_model(y, ms)
        return {k: fm[k] for k in ("2023", "2024", "2025", "2026")} | {"trend_per_year": fm["trend_per_year"]}

    def rrr(a, b, year):
        """Ratio of NN to ND departures (independent fits; conservative if common shocks correlate them)."""
        if not a or not b:
            return None
        la, lb = math.log(a[year]["rr"]), math.log(b[year]["rr"])
        sa = (math.log(a[year]["hi"]) - math.log(a[year]["lo"])) / 3.92
        sb = (math.log(b[year]["hi"]) - math.log(b[year]["lo"])) / 3.92
        d, se = la - lb, math.sqrt(sa * sa + sb * sb)
        return {"rr": math.exp(d), "lo": math.exp(d - 1.96 * se), "hi": math.exp(d + 1.96 * se)}

    out = {"n_records": len(recs), "by_primary": dict(Counter(r["primary"] for r in recs)), "classes": {}}
    scopes = {"all_six": lambda r: True, "hep-ex": lambda r: r["primary"] == "hep-ex",
              "nucl-ex": lambda r: r["primary"] == "nucl-ex", "hep-ex+nucl-ex": lambda r: r["primary"] in ("hep-ex", "nucl-ex")}
    for variant in ("main", "no_link", "title_prospect", "no_prospect", "primary_exp"):
        for sname, sk in scopes.items():
            nd = dep(series(lambda r: sk(r) and inspire_classes(r, variant) == "ND"))
            nn = dep(series(lambda r: sk(r) and inspire_classes(r, variant) == "NN"))
            n_nd = sum(1 for r in recs if sk(r) and inspire_classes(r, variant) == "ND")
            out["classes"][f"{variant}__{sname}"] = {
                "n_ND": n_nd, "n_NN": sum(1 for r in recs if sk(r)) - n_nd, "ND": nd, "NN": nn,
                "RRR_NN_vs_ND": {y: rrr(nn, nd, y) for y in ("2025", "2026")}}
    # collaboration size and document type, hep-ex + nucl-ex
    exp = lambda r: r["primary"] in ("hep-ex", "nucl-ex")  # noqa: E731
    size = lambda r: (None if r["author_count"] in ("", "0") else  # noqa: E731
                      "le10" if int(r["author_count"]) <= 10 else
                      "11to300" if int(r["author_count"]) <= 300 else "gt300")
    out["by_author_count_hep-ex_nucl-ex"] = {b: {"n": sum(1 for r in recs if exp(r) and size(r) == b),
                                                 "departure": dep(series(lambda r, b=b: exp(r) and size(r) == b))}
                                             for b in ("le10", "11to300", "gt300")}
    doc = lambda r: ("research_article" if inspire_classes(r, "no_prospect") in ("ND", "NN") and "article" in  # noqa: E731
                     r["document_type"] and not (set(r["document_type"].split(";")) & NON_RESEARCH_DOCS) else
                     (r["document_type"].split(";")[0] or "unknown"))
    types = Counter(doc(r) for r in recs if exp(r))
    out["by_document_type_hep-ex_nucl-ex"] = {t: {"n": n, "departure": dep(series(lambda r, t=t: exp(r) and doc(r) == t))}
                                              for t, n in types.most_common(6)}
    # Snowmass 2021 (2022 base) and European Strategy inputs (2025)
    out["snowmass_espp_by_year"] = {y: {"snowmass": sum(1 for r in recs if r["date"][:4] == y and r["snowmass"] == "1"),
                                        "european_strategy": sum(1 for r in recs if r["date"][:4] == y and
                                                                 r["european_strategy"] == "1"),
                                        "all": sum(1 for r in recs if r["date"][:4] == y)}
                                    for y in sorted({r["date"][:4] for r in recs})}
    out["without_snowmass_espp"] = {
        "hep-ex+nucl-ex": dep(series(lambda r: exp(r) and r["snowmass"] != "1" and r["european_strategy"] != "1")),
        "all_six": dep(series(lambda r: r["snowmass"] != "1" and r["european_strategy"] != "1"))}
    return out



def section_inspire_round2(repo):
    """Round 2 (item 9; R3 #2, R2 N3): the INSPIRE-HEP classes with the estimator of C1-C3 (NN as group A, ND as
    group B) under four bases (2022; 2017-2019; 2017-2019 and 2022 pooled; 2017-2022 pooled), for records as
    harvested, without planning papers (INSPIRE's flags, plus the arXiv flags that read title, abstract and comments,
    matched by arXiv identifier from 2019), and for research articles only without planning papers; with ND restricted
    to records that carry a collaboration as a sensitivity; proceedings (conference papers) reported separately as
    departures from their 2017-2022 trend. An author count of 0 (author list not yet loaded) is treated as missing.
    Also the shares of hep-ex and nucl-ex records with an experiment link, a collaboration, each document type and
    cross-lists to physics.ins-det or to cs/stat, by year (January-September)."""
    path = os.path.join(repo, "data/raw/inspire_hep_records.csv.gz")
    if not os.path.exists(path):
        return None
    recs = [r for r in csv.DictReader(gzip.open(path, "rt")) if "2017-01" <= r["date"][:7] <= LAST]
    ms = ym_range("2017-01", LAST)
    flags = {}
    fpath = os.path.join(repo, "data/processed/arxiv_paper_flags.csv.gz")
    if os.path.exists(fpath):
        flags = {r["arxiv_id"]: r["snowmass"] == "1" or r["european_strategy"] == "1"
                 for r in csv.DictReader(gzip.open(fpath, "rt"))}

    def docs(r):
        return set(filter(None, r["document_type"].split(";"))) | set(filter(None, r["publication_type"].split(";")))

    planning = lambda r: r["snowmass"] == "1" or r["european_strategy"] == "1" or flags.get(r["arxiv_id"], False)  # noqa: E731
    research = lambda r: "article" in docs(r) and not (docs(r) & NON_RESEARCH_DOCS)  # noqa: E731
    proceedings = lambda r: bool(docs(r) & {"conference paper", "proceedings"})  # noqa: E731
    nd = lambda r: inspire_classes(r) == "ND"  # noqa: E731
    nd_collab = lambda r: nd(r) and bool(r["collaborations"])  # noqa: E731

    def series(keep):
        c = Counter(r["date"][:7] for r in recs if keep(r))
        return np.array([c.get(m, 0) for m in ms], float)

    scopes = {"all_six": lambda r: True, "hep-ex": lambda r: r["primary"] == "hep-ex",
              "nucl-ex": lambda r: r["primary"] == "nucl-ex",
              "hep-ex+nucl-ex": lambda r: r["primary"] in ("hep-ex", "nucl-ex")}
    samples = {"as_harvested": lambda r: True, "without_planning": lambda r: not planning(r),
               "research_articles_without_planning": lambda r: research(r) and not planning(r)}
    bases = {"2022": {2022}, "2017-2019": {2017, 2018, 2019}, "2017-2019+2022": {2017, 2018, 2019, 2022},
             "2017-2022": set(range(2017, 2023))}
    out = {"n_records": len(recs), "planning_flagged": {"inspire_flags": sum(1 for r in recs if r["snowmass"] == "1" or
                                                                              r["european_strategy"] == "1"),
                                                        "with_arxiv_flags": sum(1 for r in recs if planning(r))},
           "author_count_zero": sum(1 for r in recs if r["author_count"] == "0"), "contrasts": {}}
    for sname, sk in scopes.items():
        for smp, keep in samples.items():
            for ndname, ndrule in (("ND", nd), ("ND_with_collaboration", nd_collab)):
                if ndname != "ND" and smp != "research_articles_without_planning":
                    continue
                ya = series(lambda r: sk(r) and keep(r) and not ndrule(r))
                yb = series(lambda r: sk(r) and keep(r) and ndrule(r))
                res = {"n_NN": int(ya.sum()), "n_ND": int(yb.sum())}
                if yb.sum() > 0 and min(ya.sum(), yb.sum()) >= 100:
                    for bname, bset in bases.items():
                        ev = event_study(ya, yb, ms, bset)
                        res[bname] = {k: ev[k] for k in ("2025", "2026", "2026_vs_2025") if k in ev}
                out["contrasts"][f"{sname}|{smp}|{ndname}"] = res
        print("inspire round 2", sname, flush=True)
    out["proceedings_departure"] = {}
    for sname, sk in scopes.items():
        y = series(lambda r: sk(r) and proceedings(r) and not planning(r))
        if y.min() > 0:
            fm = field_model(list(y), ms)
            out["proceedings_departure"][sname] = {k: fm[k] for k in ("2025", "2026")} | {
                "trend_per_year": fm["trend_per_year"], "n": int(y.sum())}
        else:
            out["proceedings_departure"][sname] = {"n": int(y.sum()), "months_with_zero": int((y == 0).sum())}
    exp = [r for r in recs if r["primary"] in ("hep-ex", "nucl-ex") and r["date"][5:7] <= "09"]
    shares = {}
    for y in sorted({r["date"][:4] for r in exp}):
        ry = [r for r in exp if r["date"][:4] == y]
        cats = [set(r["categories"].split(";")) for r in ry]
        n = len(ry)
        shares[y] = {"records": n,
                     "experiment_link": sum(1 for r in ry if r["experiments"]) / n,
                     "collaboration": sum(1 for r in ry if r["collaborations"]) / n,
                     "conference_paper": sum(1 for r in ry if "conference paper" in docs(r)) / n,
                     "research_article": sum(1 for r in ry if research(r)) / n,
                     "planning": sum(1 for r in ry if planning(r)) / n,
                     "cross_list_physics.ins-det": sum(1 for c in cats if "physics.ins-det" in c) / n,
                     "cross_list_cs_or_stat": sum(1 for c in cats if any(x.startswith(("cs.", "stat.")) for x in c)) / n,
                     "author_count_zero": sum(1 for r in ry if r["author_count"] == "0"),
                     "ND": sum(1 for r in ry if nd(r)) / n}
    out["hep-ex+nucl-ex_shares_jan_sep"] = shares
    return out

# ---------------------------------------------------------------- arXiv paper-level flags (OAI)
SNOWMASS = re.compile(r"snowmass", re.I)
ESPP = re.compile(r"european strategy|\bESPP|\bESPPU\b|strategy for particle physics", re.I)
GENRES = [
    ("white_paper", re.compile(r"white ?paper|snowmass|european strategy|\bESPPU?\b|community (?:report|input)|"
                               r"input to the|roadmap", re.I), ("title", "abstract", "comments")),
    ("proceedings", re.compile(r"proceedings|\bproc\.|conference|workshop|symposium|talk (?:given|presented)|"
                               r"presented at|contribution to|contributed (?:talk|paper|to)|plenary|poster|"
                               r"\bPoS\b|invited talk|seminar given|school on|summer school|lectures? (?:given|delivered)",
                               re.I), ("comments",)),
    ("thesis", re.compile(r"\bthesis\b|dissertation|habilitation|\bPh\.? ?D\b|master'?s thesis", re.I), ("comments", "title")),
    ("review", re.compile(r"\breview\b|\bsurvey\b|lecture notes|\blectures on\b|\btutorial\b|\bprimer\b|"
                          r"encyclop(?:a)?edia|book chapter|\bchapter\b|handbook", re.I), ("title", "comments")),
]


def classify(r):
    for name, rx, fields in GENRES:
        if any(rx.search(r.get(f) or "") for f in fields):
            return name
    return "research"


# Round 2 (item 11; R2 N1): the rule above matches journal names ("Physical Review", "Proc. Amer. Math. Soc.") and
# research papers "accepted at" a conference, and finds "review" anywhere in the comments. The revised rule removes
# journal names and acceptance notes (unless they name proceedings, a talk or a poster) before matching, and accepts
# "review" in the title or as an explicit phrase in the comments.
JOURNAL_NAMES = re.compile(
    r"Phys(?:ical|\.)?\s*Rev(?:iew|\.)?(?:\s*(?:Lett(?:ers|\.)?|[A-EX]\b|Research|Applied|Materials|Fluids|"
    r"Accelerators and Beams|Special Topics))*|Rev(?:iews|\.)\s*(?:of\s+)?Mod(?:ern|\.)\s*Phys(?:ics|\.)?|"
    r"Proc(?:eedings|\.)\s*(?:of\s+the\s+)?(?:Amer(?:ican|\.)\s*Math(?:ematical|\.)\s*Soc(?:iety|\.)?|"
    r"Natl\.?\s*Acad\.?\s*Sci\.?(?:\s*U\.?\s*S\.?\s*A\.?)?|National\s+Academy\s+of\s+Sciences|"
    r"(?:[A-Z][\w.'-]*\s+){1,4}(?:Soc(?:iety|\.)|Acad(?:emy|\.)))|\bPNAS\b|Annual\s+Reviews?\s+of\s+[A-Z][\w ]+|"
    r"Living\s+Reviews\s+in\s+[A-Z][\w ]+|Rev(?:iew|\.)\s+(?:of\s+)?Sci(?:entific|\.)\s+Instrum(?:ents|\.)?|"
    r"Rev(?:iews|\.)\s+(?:in\s+)?Math(?:ematical|\.)\s+Phys(?:ics|\.)?|Phys(?:ics|\.)\s+Rep(?:orts|\.)?")
ACCEPTED = re.compile(r"accepted\s+(?:at|to|for|in|by)\b[^.;]*", re.I)
PROC_WORDS = re.compile(r"proceedings|\bPoS\b|talk|poster|contribution", re.I)
REVIEW_EXPLICIT = re.compile(r"review article|invited review|\ba review\b|review paper|survey article|lecture notes|"
                             r"lectures? (?:given|delivered)|book chapter|chapter (?:in|of|for)\b|encyclop(?:a)?edia|"
                             r"handbook", re.I)
REVIEW_TITLE = re.compile(r"\breview\b|\bsurvey\b|lecture notes|\blectures on\b|\btutorial\b|\bprimer\b|"
                          r"encyclop(?:a)?edia|handbook", re.I)


def clean_comments(text):
    text = JOURNAL_NAMES.sub(" ", text or "")
    return ACCEPTED.sub(lambda m: m.group(0) if PROC_WORDS.search(m.group(0)) else " ", text)


def classify2(r):
    title, comments = r.get("title") or "", clean_comments(r.get("comments"))
    text = {"title": JOURNAL_NAMES.sub(" ", title), "abstract": r.get("abstract") or "", "comments": comments}
    for name, rx, fields in GENRES:
        if name == "review":
            if REVIEW_TITLE.search(text["title"]) or REVIEW_EXPLICIT.search(comments):
                return name
        elif any(rx.search(text[f]) for f in fields):
            return name
    return "research"


def classify_title(r):
    """Title only, a field that rarely changes at revision (R2 N1, revision sensitivity)."""
    title = JOURNAL_NAMES.sub(" ", r.get("title") or "")
    for name, rx, _ in GENRES:
        if (REVIEW_TITLE if name == "review" else rx).search(title):
            return name
    return "research"


def load_v1_dates(repo):
    path = os.path.join(repo, "data/raw/arxiv_v1_dates.csv.gz")
    if not os.path.exists(path):
        return {}
    return {r["arxiv_id"]: r["v1_submitted"] for r in csv.DictReader(gzip.open(path, "rt"))}


def load_oai(oai_dir, v1=None):
    """One row per paper with primary category in maths or the six HEP/nuclear archives, January 2019 on.
    In the OAI-PMH arXiv format served by oaipmh.arxiv.org, `created` is the submission date of the LATEST version
    (checked on arXiv abstract pages: 1902.06571 has created 2019-05-01, the date of its v2; its v1 is 18 February
    2019). So `created` gives the first-version date only for papers never revised; v1 dates of revised papers come
    from the arXiv API (`published`), read from data/raw/arxiv_v1_dates.csv.gz (fetch_arxiv_v1_dates.py)."""
    v1 = v1 or {}
    papers = {}
    for fn in sorted(os.listdir(oai_dir)):
        if not (fn.startswith("oai_") and fn.endswith(".jsonl.gz")):
            continue
        with gzip.open(os.path.join(oai_dir, fn), "rt", encoding="utf-8") as f:
            for line in f:
                r = json.loads(line)
                m = re.fullmatch(r"(\d{2})(\d{2})\.\d{4,5}", r.get("id") or "")
                if not m or r["id"] in papers or not r.get("categories"):
                    continue
                prim = r["categories"][0]
                arch = "math" if prim.startswith("math.") else prim.split(".")[0]
                if arch not in HEP6 + ["math"]:
                    continue
                idm = f"20{m.group(1)}-{m.group(2)}"
                created = r.get("created") or ""
                first = v1.get(r["id"]) or (created if created and created[:7] <= idm else "")
                papers[r["id"]] = {
                    "id": r["id"], "id_month": idm, "created": created, "v1": first,
                    "archive": arch, "primary": prim, "n_authors": len(r.get("authors") or []),
                    "snowmass": bool(SNOWMASS.search(" ".join(filter(None, [r.get("title"), r.get("abstract"),
                                                                           r.get("comments")])))),
                    "espp": bool(ESPP.search(" ".join(filter(None, [r.get("title"), r.get("abstract"),
                                                                   r.get("comments")])))),
                    "genre": classify(r), "genre2": classify2(r), "genre_title": classify_title(r),
                    "revised": bool(created) and created[:7] > idm}
    return list(papers.values())


def monthly(papers, key, keep=lambda p: True, archives=None):
    c = defaultdict(int)
    for p in papers:
        if (archives is None or p["archive"] in archives) and keep(p):
            c[p[key][:7]] += 1
    return c


def growth_windows(c, label):
    def s(ms):
        return sum(c.get(m, 0) for m in ms)
    out = {}
    for y in (2025, 2026):
        out[f"jan_aug_{y}"] = s([f"{y}-{i:02d}" for i in range(1, 9)])
        out[f"jan_sep_{y}"] = s([f"{y}-{i:02d}" for i in range(1, 10)])
        out[f"q3_{y}"] = s([f"{y}-{i:02d}" for i in (7, 8, 9)])
        out[f"sep_{y}"] = s([f"{y}-09"])
    out["trailing12_to_2026_09"] = s(ym_range("2025-10", "2026-09"))
    out["trailing12_to_2025_09"] = s(ym_range("2024-10", "2025-09"))
    g = {k: out[f"{k}_2026"] / out[f"{k}_2025"] - 1 for k in ("jan_aug", "jan_sep", "q3", "sep") if out[f"{k}_2025"]}
    g["trailing12"] = out["trailing12_to_2026_09"] / out["trailing12_to_2025_09"] - 1
    return {"counts": out, "growth": g, "dating": label}


def dt_days(day, month):
    """Days from a date (YYYY-MM-DD) to the first day of a month (YYYY-MM)."""
    import datetime as dt
    try:
        return (dt.date(int(month[:4]), int(month[5:7]), 1) - dt.date.fromisoformat(day[:10])).days
    except ValueError:
        return None


def section_dating(repo, oai_dir):
    """P1a: identifier (announcement) month vs first-version submission month, 2024-2026 (v1 dates of revised papers
    fetched from the arXiv API)."""
    v1 = load_v1_dates(repo)
    papers = load_oai(oai_dir, v1)
    out = {"n_papers": len(papers), "v1_dates_from_api": len(v1)}
    groups = {"maths": ["math"], "hep_nucl_6": HEP6, "theory_hep-th_hep-ph_nucl-th": ["hep-th", "hep-ph", "nucl-th"],
              "gr-qc": ["gr-qc"], "experiment": EXPERIMENT, "hep-ph": ["hep-ph"], "hep-ex": ["hep-ex"]}
    ms = ym_range("2024-01", LAST)
    covered = [p for p in papers if "2024-01" <= p["id_month"] <= "2026-10"]
    out["v1_known_share_2024_on"] = float(np.mean([bool(p["v1"]) for p in covered])) if covered else None
    dating = {}
    for g, arch in groups.items():
        sel = [p for p in covered if p["archive"] in arch and p["v1"]]
        by_id = monthly(sel, "id_month")
        by_v1 = monthly([p for p in sel if p["v1"][:7] >= "2024-01"], "v1")
        spill = defaultdict(lambda: [0, 0, 0])
        for p in sel:
            spill[p["id_month"]][0] += 1
            spill[p["id_month"]][1] += p["v1"][:7] < p["id_month"]
            spill[p["id_month"]][2] += (dt_days(p["v1"], p["id_month"]) or 0) > 31
        dating[g] = {"by_identifier": growth_windows(by_id, "identifier (announcement) month"),
                     "by_v1_submission": growth_windows(by_v1, "first-version submission month"),
                     "share_submitted_in_an_earlier_month": {m: v[1] / v[0] for m, v in sorted(spill.items()) if v[0]},
                     "share_submitted_over_a_month_before": {m: v[2] / v[0] for m, v in sorted(spill.items()) if v[0]},
                     "monthly": {m: {"by_identifier": by_id.get(m, 0), "by_v1": by_v1.get(m, 0)} for m in ms}}
    out["groups"] = dating
    out.update(dating_round2(repo, papers))
    return out


def dating_round2(repo, papers):
    """Round 2 (item 6): the September 2026 spike in mathematics by submission and by announcement; October 2026,
    under arXiv's cap of two submissions per submitter a month (from 1 October 2026), in 14-day windows by
    first-version date (the harvest of 16 October holds announcements to 15 October, so papers still on hold are
    missing from the October windows); and C1 and the arXiv groups against bioRxiv with arXiv dated by identifier month
    or by first-version month (identifier month when the v1 date is unknown, as for papers first posted before December
    2023 and revised later), January-September and January-August 2026, from the same OAI records."""
    import datetime as dt
    out = {}
    maths = [p for p in papers if p["archive"] == "math"]
    sep = {}
    for y in (2025, 2026):
        ids = [p for p in maths if p["id_month"] == f"{y}-09"]
        known = [p for p in ids if p["v1"]]
        sep[str(y)] = {"by_identifier": len(ids), "v1_known": len(known),
                       "submitted_in_september": sum(1 for p in maths if p["v1"][:7] == f"{y}-09"),
                       "identifier_september_submitted_earlier": sum(1 for p in known if p["v1"][:7] < f"{y}-09"),
                       "identifier_september_submitted_over_7_days_before":
                           sum(1 for p in known if (dt_days(p["v1"], f"{y}-09") or 0) > 7)}
    out["maths_september"] = sep
    windows = {"aug_01_14_2026": ("2026-08-01", "2026-08-14"), "sep_01_14_2026": ("2026-09-01", "2026-09-14"),
               "oct_01_14_2025": ("2025-10-01", "2025-10-14"), "oct_01_14_2026": ("2026-10-01", "2026-10-14"),
               "sep_01_07_2026": ("2026-09-01", "2026-09-07"), "oct_01_07_2025": ("2025-10-01", "2025-10-07"),
               "oct_01_07_2026": ("2026-10-01", "2026-10-07")}
    weekdays = {}
    for w, (a, b) in windows.items():
        d0, d1 = dt.date.fromisoformat(a), dt.date.fromisoformat(b)
        weekdays[w] = sum((d0 + dt.timedelta(i)).weekday() < 5 for i in range((d1 - d0).days + 1))
    groups = {"maths": ["math"], "hep_nucl_6": HEP6, "theory": THEORY, "experiment": EXPERIMENT, "hep-ph": ["hep-ph"],
              "hep-ex": ["hep-ex"]}
    octo = {"weekdays_in_window": weekdays, "counts_by_v1_date": {}}
    for g, arch in groups.items():
        days = Counter(p["v1"][:10] for p in papers if p["archive"] in arch and p["v1"])
        octo["counts_by_v1_date"][g] = {w: sum(n for d, n in days.items() if a <= d <= b) for w, (a, b) in windows.items()}
    out["october_2026"] = octo
    by = {"identifier": defaultdict(Counter), "v1": defaultdict(Counter)}
    for p in papers:
        by["identifier"][p["archive"]][p["id_month"]] += 1
        by["v1"][p["archive"]][(p["v1"] or p["id_month"])[:7]] += 1
    ax, bx = load_arxiv(repo), load_biorxiv(repo)
    con = {}
    for last in ("2026-09", "2026-08"):
        ms = ym_range("2019-02", last)
        sources = {"identifier": by["identifier"], "v1": by["v1"], "statistics_pages": ax}
        for src, ser in sources.items():
            c = lambda arch: np.array([sum(ser[a].get(m, 0) for a in arch) for m in ms], float)  # noqa: E731
            res = {}
            for name, (A, B) in (("C1_theory_vs_experiment", (THEORY, EXPERIMENT)),
                                 ("C1_without_gr-qc", (["hep-th", "hep-ph", "nucl-th"], EXPERIMENT))):
                es = event_study(c(A), c(B), ms, {2022})
                res[name] = {"2026": es["2026"], "2026_vs_2025": es["2026_vs_2025"]}
            yb = total(bx, list(bx), ms)
            for g, arch in (("hep_nucl_6", HEP6), ("theory", THEORY), ("experiment", EXPERIMENT), ("maths", ["math"])):
                es = event_study(c(arch), yb, ms, {2022})
                res[f"{g}_vs_biorxiv"] = {"2026": es["2026"], "2026_vs_2025": es["2026_vs_2025"]}
            con[f"{src}|to_{last}"] = res
    out["contrasts_by_dating"] = {"window_from": "2019-02", "base": 2022, "results": con}
    return out


def section_hepex_crosslists(repo, oai_dir):
    """Round 2 (R3 minor 10): cross-lists of papers with primary category hep-ex, by month, from the arXiv OAI records
    (the same fall appears in INSPIRE's categories, so it is not an INSPIRE curation effect); and papers of other
    primary categories cross-listed to hep-ex, which would rise if instrumentation papers had moved to
    physics.ins-det as primary."""
    by, into = defaultdict(lambda: [0, 0, 0, 0]), defaultdict(Counter)
    with gzip.open(os.path.join(oai_dir, "oai_physics_hep-ex.jsonl.gz"), "rt", encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            m = re.fullmatch(r"(\d{2})(\d{2})\.\d{4,5}", r.get("id") or "")
            if not m or not r.get("categories") or m.group(1) < "19":
                continue
            month, cats = f"20{m.group(1)}-{m.group(2)}", r["categories"]
            if month > LAST:
                continue
            if cats[0] == "hep-ex":
                v = by[month]
                v[0] += 1
                v[1] += len(cats) > 1
                v[2] += "physics.ins-det" in cats
                v[3] += any(c.startswith(("cs.", "stat.")) for c in cats)
            elif "hep-ex" in cats[1:]:
                into[month][cats[0]] += 1
    return {"hep-ex_primary_by_month": {m: {"papers": v[0], "any_cross_list": v[1], "physics.ins-det": v[2],
                                            "cs_or_stat": v[3]} for m, v in sorted(by.items())},
            "cross_listed_into_hep-ex_by_month": {m: {"all": sum(c.values()), "physics.ins-det": c["physics.ins-det"]}
                                                  for m, c in sorted(into.items())}}

def section_genre_round2(repo, oai_dir):
    """Round 2 (item 11; R2 N1): validation of the keyword genres. (i) Precision and recall by year against INSPIRE's
    curated types (proceedings: document type conference paper or proceedings; review: publication type review,
    lectures or introductory), for the five archives in both tables (hep-th, hep-ph, nucl-th, hep-ex, nucl-ex),
    January-September 2019-2026, for the original rule, the revised rule (journal names and acceptance notes removed;
    review only in titles or explicit phrases) and a title-only rule; (ii) genre shares by year for revised and
    unrevised papers (a later version submitted after the identifier month); (iii) the 2026 departures of all papers
    and of research papers from their 2019-2022 trends under each rule."""
    papers = load_oai(oai_dir, load_v1_dates(repo))
    rules = ("genre", "genre2", "genre_title")
    ins = {}
    path = os.path.join(repo, "data/raw/inspire_hep_records.csv.gz")
    for r in csv.DictReader(gzip.open(path, "rt")):
        docs = set(filter(None, r["document_type"].split(";")))
        pubs = set(filter(None, r["publication_type"].split(";")))
        ins[r["arxiv_id"]] = {"proceedings": bool(docs & {"conference paper", "proceedings"}),
                              "review": bool(pubs & {"review", "lectures", "introductory"})}
    five = {"hep-th", "hep-ph", "nucl-th", "hep-ex", "nucl-ex"}
    val = {}
    for rule in rules:
        for cls in ("proceedings", "review"):
            by = {}
            for y in range(2019, 2027):
                sel = [p for p in papers if p["archive"] in five and p["id_month"][:4] == str(y) and
                       p["id_month"][5:] <= "09" and p["id"] in ins]
                kw = [p for p in sel if p[rule] == cls]
                ref = [p for p in sel if ins[p["id"]][cls]]
                both = sum(1 for p in kw if ins[p["id"]][cls])
                by[str(y)] = {"matched": len(sel), "keyword": len(kw), "inspire": len(ref),
                              "precision": both / len(kw) if kw else None, "recall": both / len(ref) if ref else None}
            val[f"{rule}|{cls}"] = by
    out = {"validation_against_inspire": val}
    groups = {"maths": ["math"], "hep_nucl_6": HEP6, "theory": THEORY, "experiment": EXPERIMENT}
    shares = {}
    for g, arch in groups.items():
        for rev in (False, True):
            by = {}
            for y in range(2019, 2027):
                sel = [p for p in papers if p["archive"] in arch and p["revised"] == rev and p["id_month"][:4] == str(y)
                       and p["id_month"][5:] <= "09"]
                c = Counter(p["genre2"] for p in sel)
                by[str(y)] = {"papers": len(sel)} | {k: v / len(sel) for k, v in c.items()} if sel else {"papers": 0}
            shares[f"{g}|{'revised' if rev else 'unrevised'}"] = by
    out["genre2_shares_by_revision"] = shares
    ms = ym_range("2019-01", LAST)
    dep = {}
    for g, arch in groups.items():
        allc = monthly(papers, "id_month", archives=arch)
        res = {"all": field_model([allc.get(m, 0) for m in ms], ms)["2026"]}
        for rule in rules:
            rc = monthly(papers, "id_month", keep=lambda p, rule=rule: p[rule] == "research", archives=arch)
            res[f"research_{rule}"] = field_model([rc.get(m, 0) for m in ms], ms)["2026"]
        dep[g] = res
    out["departure_2026_from_2019_2022_trend"] = dep
    return out

def section_c2_ai_split(repo):
    """Round 2 (item 12; R4 P1, R3 #5; exploratory): C2 with papers whose title or abstract names AI or machine
    learning as a topic (the list of Deviation 3, D3m, in nd_frames.py) removed from both groups, from bioinformatics
    only, or kept; bioinformatics papers with the AI topic against those without; and the AI-topic share by year. All
    series from data/processed/nd_category_monthly_biorxiv.csv (version-1 records with text), so the 'all papers' row
    shows how far that source differs from the category counts used for C2."""
    path = os.path.join(repo, "data/processed/nd_category_monthly_biorxiv.csv")
    if not os.path.exists(path):
        return None
    allp, noai = defaultdict(Counter), defaultdict(Counter)
    for r in csv.DictReader(open(path)):
        allp[r["category"]][r["month"]] += int(r["papers"])
        noai[r["category"]][r["month"]] += int(r["papers_without_ai_topic"])
    ms = ym_range("2019-01", LAST)

    def tot(src, cats):
        return np.array([sum(src[c].get(m, 0) for c in cats) for m in ms], float)
    ai = {c: Counter({m: allp[c][m] - noai[c][m] for m in allp[c]}) for c in allp}
    comp_no_bioinf_ai = tot(allp, COMPUTATIONAL) - tot(ai, ["bioinformatics"])
    variants = {"all_papers": (tot(allp, COMPUTATIONAL), tot(allp, WET_LAB)),
                "without_ai_topic_papers": (tot(noai, COMPUTATIONAL), tot(noai, WET_LAB)),
                "without_bioinformatics_ai_topic_papers": (comp_no_bioinf_ai, tot(allp, WET_LAB)),
                "bioinformatics_ai_vs_wet_lab": (tot(ai, ["bioinformatics"]), tot(allp, WET_LAB)),
                "bioinformatics_without_ai_vs_wet_lab": (tot(noai, ["bioinformatics"]), tot(allp, WET_LAB)),
                "bioinformatics_ai_vs_without_ai": (tot(ai, ["bioinformatics"]), tot(noai, ["bioinformatics"]))}
    out = {"contrasts": {}}
    for name, (ya, yb) in variants.items():
        res = {}
        for bname, bset in (("2022", {2022}), ("2019+2022", {2019, 2022})):
            ev = event_study(ya, yb, ms, bset)
            res[bname] = {k: ev[k] for k in ("2025", "2026", "2026_vs_2025")}
        out["contrasts"][name] = res
    share = {}
    for g, cats in (("bioinformatics", ["bioinformatics"]), ("systems biology", ["systems biology"]),
                    ("genomics", ["genomics"]), ("wet_lab", WET_LAB)):
        share[g] = {}
        for y in range(2019, 2027):
            sel = [m for m in ms if m[:4] == str(y) and m[5:] <= "09"]
            n = sum(allp[c].get(m, 0) for c in cats for m in sel)
            k = n - sum(noai[c].get(m, 0) for c in cats for m in sel)
            share[g][str(y)] = {"papers": n, "ai_topic_share": k / n if n else None}
    out["ai_topic_share_jan_sep"] = share
    return out

def section_biorxiv_sum_check(repo):
    """Round 2 (item 13): bioRxiv's own monthly statistics (/sum, new papers) against the record-level harvest (unique
    version-1 DOIs, data/raw/biorxiv_records_monthly.csv) and against the per-category counts used for C2
    (data/raw/biorxiv_category_monthly.csv), January 2019 to the last month; the categories behind any difference, and
    whether the categories of C2 differ in any month."""
    sm = {r["month"]: int(r["new_papers"]) for r in
          json.load(open(os.path.join(repo, "data/raw/biorxiv_sum_m.json")))["bioRxiv content statistics"]}
    rec, cat = defaultdict(Counter), defaultdict(Counter)
    for r in csv.DictReader(open(os.path.join(repo, "data/raw/biorxiv_records_monthly.csv"))):
        rec[r["month"]][r["category"]] += int(r["new_papers"])
    for r in csv.DictReader(open(os.path.join(repo, "data/raw/biorxiv_category_monthly.csv"))):
        cat[r["month"]][r["category"]] += int(r["new_papers"])
    ms = ym_range("2019-01", LAST)
    c2 = set(COMPUTATIONAL) | set(WET_LAB)
    out = {"months": len(ms), "records_total": sum(sum(rec[m].values()) for m in ms),
           "sum_total": sum(sm[m] for m in ms), "category_file_total": sum(sum(cat[m].values()) for m in ms),
           "records_vs_sum": {m: sum(rec[m].values()) - sm[m] for m in ms if sum(rec[m].values()) != sm[m]},
           "category_file_vs_sum": {m: sum(cat[m].values()) - sm[m] for m in ms if sum(cat[m].values()) != sm[m]},
           "category_file_vs_records_by_category": {}, "c2_categories_differ_in_months": []}
    gaps = Counter()
    for m in ms:
        for c in set(rec[m]) | set(cat[m]):
            if cat[m][c] != rec[m][c]:
                gaps[c] += cat[m][c] - rec[m][c]
                if c in c2:
                    out["c2_categories_differ_in_months"].append(m)
    out["category_file_vs_records_by_category"] = dict(gaps)
    return out

def section_inspire_dating(repo):
    """Round 2 (item 6): INSPIRE-HEP records dated by first-version submission (preprint_date) against arXiv's
    statistics pages (announced new submissions): growth from 2025 to 2026 in January-September and January-August by
    primary archive; the share of records whose arXiv identifier month is later than their submission month, by year;
    and the share of submission dates on weekends, when arXiv does not announce."""
    import datetime as dt
    path = os.path.join(repo, "data/raw/inspire_hep_records.csv.gz")
    if not os.path.exists(path):
        return None
    recs = list(csv.DictReader(gzip.open(path, "rt")))
    ax = load_arxiv(repo)

    def window(c, y, last):
        return sum(c.get(f"{y}-{i:02d}", 0) for i in range(1, last + 1))
    growth = {}
    for a in ("hep-ex", "hep-ph", "hep-th", "hep-lat", "nucl-ex", "nucl-th"):
        ins = Counter(r["date"][:7] for r in recs if r["primary"] == a)
        row = {}
        for name, last in (("jan_sep", 9), ("jan_aug", 8)):
            i25, i26, s25, s26 = window(ins, 2025, last), window(ins, 2026, last), window(ax[a], 2025, last), \
                window(ax[a], 2026, last)
            row[name] = {"inspire_by_submission": {"2025": i25, "2026": i26, "growth": i26 / i25 - 1},
                         "statistics_pages_by_announcement": {"2025": s25, "2026": s26, "growth": s26 / s25 - 1}}
        row["sep_2026"] = {"inspire_by_submission": ins.get("2026-09", 0),
                           "statistics_pages_by_announcement": ax[a].get("2026-09", 0)}
        growth[a] = row
    later, wk = defaultdict(lambda: [0, 0]), Counter()
    for r in recs:
        d = r["date"]
        m = re.fullmatch(r"(\d{2})(\d{2})\.\d{4,5}", r["arxiv_id"] or "")
        if not m or len(d) < 10 or not "2017" <= d[:4] <= "2026":
            continue
        later[d[:4]][0] += 1
        later[d[:4]][1] += f"20{m.group(1)}-{m.group(2)}" > d[:7]
        wk[dt.date.fromisoformat(d[:10]).weekday()] += 1
    n = sum(wk.values())
    return {"growth_2025_to_2026": growth,
            "identifier_month_later_than_submission": {y: v[1] / v[0] for y, v in sorted(later.items())},
            "identifier_month_later_overall": sum(v[1] for v in later.values()) / sum(v[0] for v in later.values()),
            "weekend_share_of_submission_dates": {"saturday": wk[5] / n, "sunday": wk[6] / n, "n": n}}


def section_oai(repo, oai_dir):
    papers = load_oai(oai_dir, load_v1_dates(repo))
    out = {"n_papers": len(papers)}
    ms = ym_range("2019-02", LAST)  # January 2019 identifiers include December 2018 submissions, which were not kept
    ax = load_arxiv(repo)
    # P1b: Snowmass 2021 and European Strategy inputs
    sm_ = {}
    for a in HEP6:
        n22 = sum(1 for p in papers if p["archive"] == a and "2022-01" <= p["id_month"] <= "2022-09")
        s22 = sum(1 for p in papers if p["archive"] == a and "2022-01" <= p["id_month"] <= "2022-09" and p["snowmass"])
        n25 = sum(1 for p in papers if p["archive"] == a and "2025-01" <= p["id_month"] <= "2025-09")
        e25 = sum(1 for p in papers if p["archive"] == a and "2025-01" <= p["id_month"] <= "2025-09" and p["espp"])
        sm_[a] = {"jan_sep_2022": n22, "snowmass_jan_sep_2022": s22, "snowmass_share_2022": s22 / n22 if n22 else None,
                  "jan_sep_2025": n25, "espp_jan_sep_2025": e25, "espp_share_2025": e25 / n25 if n25 else None}
    out["snowmass_espp"] = sm_
    m15 = ym_range("2015-01", LAST)
    drop = defaultdict(lambda: defaultdict(int))
    for p in papers:
        if p["archive"] in HEP6 and (p["snowmass"] or p["espp"]):
            drop[p["archive"]][p["id_month"]] += 1
    clean = {a: {m: ax[a].get(m, 0) - drop[a].get(m, 0) for m in m15} for a in HEP6}
    variants = {"C1": (THEORY, EXPERIMENT), "C1_without_gr-qc": (["hep-th", "hep-ph", "nucl-th"], EXPERIMENT),
                "hep-ph_vs_hep-ex": (["hep-ph"], ["hep-ex"]), "hep-th_vs_hep-ex": (["hep-th"], ["hep-ex"]),
                "gr-qc_vs_experiment": (["gr-qc"], EXPERIMENT)}
    out["clean_physics"] = {}
    for name, (A, B) in variants.items():
        ya = np.array([sum(clean[a][m] for a in A) for m in m15], float)
        yb = np.array([sum(clean[b][m] for b in B) for m in m15], float)
        out["clean_physics"][name] = {"base_2022": event_study(ya, yb, m15, {2022}),
                                      "base_2017_2019": event_study(ya, yb, m15, {2017, 2018, 2019})}
    out["clean_physics"]["hep-ex_field_model"] = {
        "raw": field_model([ax["hep-ex"].get(m, 0) for m in m15], m15),
        "without_snowmass_espp": field_model([clean["hep-ex"][m] for m in m15], m15)}
    # P1f: genres
    gen = {}
    for g, arch in (("maths", ["math"]), ("hep_nucl_6", HEP6), ("theory", THEORY), ("experiment", EXPERIMENT)):
        by_year = defaultdict(Counter)
        for p in papers:
            if p["archive"] in arch and "2019-01" <= p["id_month"] <= LAST:
                by_year[p["id_month"][:4] + ("-JanSep" if p["id_month"][5:] <= "09" else "-OctDec")][p["genre"]] += 1
        allc = monthly(papers, "id_month", archives=arch)
        res_c = monthly(papers, "id_month", keep=lambda p: p["genre"] == "research", archives=arch)
        gen[g] = {"genre_counts": {k: dict(v) for k, v in sorted(by_year.items()) if k.endswith("JanSep")},
                  "all": growth_windows(allc, "identifier month"),
                  "research_only": growth_windows(res_c, "identifier month"),
                  "field_model_2019_2026": {"all": field_model([allc.get(m, 0) for m in ms], ms),
                                            "research_only": field_model([res_c.get(m, 0) for m in ms], ms)}}
    out["genre"] = gen
    # paper-level table for the deposit (no names, no text); written by the main run only
    if SUFFIX:
        return out
    path = os.path.join(repo, "data/processed/arxiv_paper_flags.csv.gz")
    with gzip.open(path, "wt", newline="") as f:
        w = csv.writer(f)
        w.writerow(["arxiv_id", "id_month", "v1_submitted", "latest_version_submitted", "primary_category", "archive",
                    "n_authors", "genre", "snowmass", "european_strategy"])
        for p in sorted(papers, key=lambda p: p["id"]):
            w.writerow([p["id"], p["id_month"], p["v1"], p["created"], p["primary"], p["archive"], p["n_authors"],
                        p["genre"], int(p["snowmass"]), int(p["espp"])])
    return out


def main():
    args = sys.argv[1:]
    oai = None
    if "--oai" in args:
        i = args.index("--oai")
        oai = args[i + 1]
        args = args[:i] + args[i + 2:]
    repo = args[0] if args else "."
    sections = args[1:] or ["estimands", "planned", "calibration", "breaks", "crosslists", "funding",
                            "funding_round2", "medrxiv_flags", "inspire", "inspire_dating", "inspire_round2",
                            "placebos_matched", "c2_ai_split", "biorxiv_sum_check"] + (
                                ["oai", "dating", "hepex_crosslists", "genre_round2"] if oai else [])
    path = os.path.join(repo, f"data/processed/stats/round1_tests{SUFFIX}.json")
    out = json.load(open(path)) if os.path.exists(path) else {}
    funcs = {"estimands": section_estimands, "breaks": section_breaks, "crosslists": section_crosslists,
             "funding": section_funding, "oai": lambda r: section_oai(r, oai), "dating": lambda r: section_dating(r, oai),
             "medrxiv_flags": section_medrxiv_flags, "inspire": section_inspire, "planned": section_planned,
             "calibration": section_calibration, "inspire_dating": section_inspire_dating,
             "placebos_matched": section_placebos_matched, "inspire_round2": section_inspire_round2,
             "funding_round2": section_funding_round2, "hepex_crosslists": lambda r: section_hepex_crosslists(r, oai),
             "genre_round2": lambda r: section_genre_round2(r, oai), "c2_ai_split": section_c2_ai_split,
             "biorxiv_sum_check": section_biorxiv_sum_check}
    for s in sections:
        print("section", s, flush=True)
        out[s] = funcs[s](repo)
        json.dump(out, open(path, "w"), indent=1, default=float)
    print("written", path)


if __name__ == "__main__":
    main()
