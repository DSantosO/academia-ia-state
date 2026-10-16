"""Round-1 review analyses: confounds of the field-level finding (arXiv accelerates; bioRxiv, medRxiv and PubMed do not).

Sections (each writes its own key of data/processed/stats/round1_tests.json; run all or name some):
  estimands   C1-C3 with multi-year baselines, a slope-change estimand, the 2026-vs-2025 acceleration, and inference
              from in-space placebos and from the spread of pre-2022 year effects (review item P1c)
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
  dating      identifier (announcement) month vs first-version submission month, 2024-2026 (P1a)
  medrxiv_flags  C3 with the title-only COVID-19 filter and with Spick et al.'s four missing datasets (P3)
  inspire     pre-registration section 10 (exploratory): INSPIRE-HEP classes from curated metadata (no AI)
Usage: python3 scripts/stats_round1.py [repo_dir] [section ...] [--oai OAI_DIR]
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
from stats_within_field import (COMPUTATIONAL, EXPERIMENT, THEORY, WET_LAB, contrast_frame,  # noqa: E402
                                deseasonalised_log_ratio, hac_wald_last, load_arxiv, load_biorxiv,
                                load_medrxiv_public, total, ym_range)

LAST = "2026-09"
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


def year_shock_z(ev, target="2026", pre_last=2021):
    """Calibrate the target-year log rate ratio against the spread of the pre-ChatGPT year effects (relative to the
    same base): z = b_target / sd(b_pre). Year-level shocks that the HAC errors miss are in that spread."""
    pre = [v["b"] for k, v in ev.items() if k.isdigit() and int(k) <= pre_last]
    if len(pre) < 3 or target not in ev:
        return None
    sd = float(np.std(pre, ddof=1))
    z = ev[target]["b"] / sd
    return {"sd_pre_year_effects": sd, "n_pre_years": len(pre), "z": z,
            "p_normal": float(math.erfc(abs(z) / math.sqrt(2))),
            "share_pre_years_at_least_as_large": float(np.mean(np.abs(pre) >= abs(ev[target]["b"])))}


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
            r["by_base"][bname] = {"event_study": ev, "year_shock_calibration_2026": year_shock_z(ev)}
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
    size = lambda r: (None if r["author_count"] == "" else "le10" if int(r["author_count"]) <= 10 else  # noqa: E731
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
                    "genre": classify(r)}
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
    return out


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
    # paper-level table for the deposit (no names, no text)
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
    sections = args[1:] or ["estimands", "breaks", "crosslists", "funding"] + (["oai"] if oai else [])
    path = os.path.join(repo, "data/processed/stats/round1_tests.json")
    out = json.load(open(path)) if os.path.exists(path) else {}
    funcs = {"estimands": section_estimands, "breaks": section_breaks, "crosslists": section_crosslists,
             "funding": section_funding, "oai": lambda r: section_oai(r, oai), "dating": lambda r: section_dating(r, oai),
             "medrxiv_flags": section_medrxiv_flags, "inspire": section_inspire}
    for s in sections:
        print("section", s, flush=True)
        out[s] = funcs[s](repo)
        json.dump(out, open(path, "w"), indent=1, default=float)
    print("written", path)


if __name__ == "__main__":
    main()
