"""Write docs/stats/results.md from the JSON outputs of the stats_*.py scripts (numbers are never typed by hand).
Usage: python3 scripts/report_stats.py [repo_dir]
"""
import json
import os
import sys


def ci(d, digits=2):
    s = f"{d['rr']:.{digits}f} [{d['lo']:.{digits}f}, {d['hi']:.{digits}f}]"
    return s + (f", p = {d['p']:.2g}" if d.get("p") is not None else "")


def pct(x, digits=1):
    return f"{100 * x:.{digits}f}%"


def p1(lines, w, f):
    names = {"C1_physics_theory_vs_experiment": "C1 physics: theory / experiment",
             "C2_biology_computational_vs_wetlab": "C2 biology: computational / wet lab",
             "C3_medicine_public_dataset_vs_rest": "C3 medicine: public dataset / other"}
    lines += ["## H1: within-field contrasts", "",
              "Rate ratio of group A to group B relative to 2022 (Poisson PML, month fixed effects, Driscoll–Kraay 95% CI).", "",
              "| Contrast | 2023 | 2024 | 2025 | 2026 (Jan–Sep) | Holm p (2026) |", "|---|---|---|---|---|---|"]
    for k, v in w["confirmatory"].items():
        ev = v["event_study"]
        lines.append(f"| {names.get(k, k)} | {ci(ev['2023'])} | {ci(ev['2024'])} | {ci(ev['2025'])} | {ci(ev['2026'])} | "
                     f"{v['p_holm_2026']:.2g} |")
    lines += ["", "Pre-2022 years of the event study (should be near 1 if the groups moved together before ChatGPT):", ""]
    for k, v in w["confirmatory"].items():
        ev = v["event_study"]
        lines.append(f"- {names.get(k, k)}: " + "; ".join(f"{y}: {ci(ev[y])}" for y in ev if int(y) < 2022))
    lines += ["", "Cross-checks and precision for 2026:", "",
              "| Contrast | Log-ratio OLS (NW) | Block bootstrap | Trend-adjusted | Minimum detectable effect (80% power) |",
              "|---|---|---|---|---|"]
    for k, v in w["confirmatory"].items():
        lines.append(f"| {names.get(k, k)} | {ci(v['ols_log_ratio']['2026'])} | {ci(v['block_bootstrap_2026'])} | "
                     f"{ci(v['trend_adjusted']['2026']) if 'trend_adjusted' in v else 'n/a'} | "
                     f"rate ratio ≥ {1 + v['mde_2026_80pct_power']:.2f} |")
    lines += ["", "Break tests with no pre-specified date (deseasonalised log ratio; sup-Wald, bootstrap p):", ""]
    for k, v in w["confirmatory"].items():
        s, l = v["unknown_break_slope"], v["unknown_break_level"]
        lines.append(f"- {names.get(k, k)}: slope break at {s['break_month']} (sup-Wald {s['sup_wald']:.1f}, p = {s['p_bootstrap']:.3f}); "
                     f"level break at {l['break_month']} (sup-Wald {l['sup_wald']:.1f}, p = {l['p_bootstrap']:.3f})")
    lines += ["", "Placebo break dates (pre-2023 data, group-specific trend plus level shift):", ""]
    for k, v in w["placebo_breaks"].items():
        lines.append(f"- {names.get(k, k)}: " + "; ".join(f"{d['placebo_year']}: {ci(d)}" for d in v))
    lines += ["", "Sensitivity (2026 rate ratio unless stated):", ""]
    for k, v in w["sensitivity"].items():
        if isinstance(v, dict) and "rr" in v:
            lines.append(f"- {k}: {ci(v)}")
        elif isinstance(v, dict):
            lines.append(f"- {k}: " + "; ".join(f"{y}: {ci(d)}" for y, d in v.items() if int(y) >= 2023))
    lines += ["", "Leave one category out (2026 rate ratio):", ""]
    lines += [f"- {k}: {ci(v)}" for k, v in w["leave_one_out"].items()]
    lines += ["", "Negative controls (pairs where H1 predicts no divergence; 2026 rate ratio):", ""]
    for k, v in w["negative_controls"].items():
        if "rr" in v:
            lines.append(f"- {k}: {ci(v)}")
        else:
            lines.append(f"- {k}: " + json.dumps(v, default=float))
    lines += ["", "## Field-level departures from the 2015–2022 trend", "",
              "Ratio of observed to trend-expected counts (Poisson PML, linear trend, seasonality, COVID dummy; Newey–West 95% CI).", "",
              "| Field | Trend per year | 2024 | 2025 | 2026 (Jan–Sep) |", "|---|---|---|---|---|"]
    for k, v in f["fields"].items():
        lines.append(f"| {k} | {pct(v['trend_per_year'])} | {ci(v['2024'])} | {ci(v['2025'])} | {ci(v['2026'])} |")
    lines += ["", "Break tests with no pre-specified date (deseasonalised log counts):", ""]
    for k, v in f["unknown_break"].items():
        lines.append(f"- {k}: slope break at {v['slope']['break_month']} (p = {v['slope']['p_bootstrap']:.3f}); "
                     f"level break at {v['level']['break_month']} (p = {v['level']['p_bootstrap']:.3f})")
    lines += ["", "2026 departure by arXiv archive (in-space placebo; mathematics' rank p = "
              f"{f['math_rank_p']:.2f}): " + ", ".join(f"{a} {r:.2f}" for a, r in f["archive_rank_2026"]), ""]
    s = f["synthetic_control_math"]
    lines += [f"Synthetic control for mathematics (pre-period {s['pre_window']}): 2026 gap {pct(s['gap_2026_pct'])}, "
              f"pre-period RMSPE {s['rmspe_pre']:.3f}, rank p = {s['rank_p']:.2f} (permutation over {len(s['donors']) + 1} units). "
              f"Weights: " + ", ".join(f"{d} {w:.2f}" for d, w in s["weights"].items()) + ". "
              f"With the pre-period ending in November 2022: gap {pct(f['synthetic_control_math_pre_to_2022_11']['gap_2026_pct'])}.", ""]


def p2(lines, h):
    groups = [("maths", "Maths"), ("theory_max50_authors", "Physics theory, ≤50 authors"),
              ("experiment_max50_authors", "Physics experiment, ≤50 authors")]
    variants = [("all_names", "all names"), ("full_first_names_no_top1pct_surnames", "namesake-robust")]
    measures = [("share_papers_with_heavy_author", "papers with an author who has ≥5 papers in the quarter"),
                ("share_authors_ge5", "active authors with ≥5 papers"),
                ("top1pct_share_of_output", "share of fractional output by the top 1% of authors"),
                ("top10pct_share_of_output", "share of fractional output by the top 10% of authors")]
    lines += ["## H2: heavy producers", "",
              "Authors matched by normalised name strings (arXiv has no author identifiers). Namesake-robust: full first "
              "names only, the 1% most frequent surnames removed. Physics excludes papers with more than 50 authors "
              "(collaboration papers, which otherwise dominate author counts). Experimental physics has only about 300 "
              "such papers a quarter and very few authors with full first names, so only its all-names version is shown. "
              "No statistic describing fewer than ten authors is shown (\"<10 authors\").",
              "", "**Levels and departures from the 2019–2022 trend** (quarterly series; OLS on a linear trend, "
              "quarter effects and 2023–2026 year dummies, Newey–West 95% CI, in percentage points):", "",
              "| Group | Names | Measure | Q3 2022 | Q3 2025 | Q3 2026 | 2026 departure from trend (pp) |",
              "|---|---|---|---|---|---|---|"]
    for g, glab in groups:
        if g not in h:
            continue
        for vname, vlab in variants:
            if g.startswith("experiment") and vname != "all_names":
                continue
            v = h[g][vname]
            q = v["quarterly"]
            for mkey, mlab in measures:
                t = (v.get("trend_departure") or {}).get(mkey)
                dep = f"{t['2026']['pp']:+.2f} [{t['2026']['lo']:+.2f}, {t['2026']['hi']:+.2f}], p = {t['2026']['p']:.2g}" \
                    if t and "2026" in t else "n/a"
                cell = lambda k: pct(q[k][mkey], 2) if k in q and q[k].get(mkey) is not None else (  # noqa: E731
                    "<10 authors" if k in q and q[k].get("suppressed_lt10_authors") else "n/a")
                lines.append(f"| {glab} | {vlab} | {mlab} | {cell('2022-Q3')} | {cell('2025-Q3')} | {cell('2026-Q3')} "
                             f"| {dep} |")
    lines += ["", "**Who produced the growth?** Change in fractional output between the third quarters of consecutive "
              "years, by author class defined on the author's combined output in both years (symmetric in the two "
              "years, so free of regression to the mean; under proportional growth every class grows at the total "
              "rate). Pairs that end before ChatGPT's release (2019→2020 to 2021→2022) show how much the classes differ by "
              "chance.", "",
              "| Group | Names | Q3 pair | Total | Top 1% | Next 9% | Bottom 90% | Share of the change: top 1% / next 9% / bottom 90% |",
              "|---|---|---|---|---|---|---|---|"]
    for g, glab in groups:
        if g not in h:
            continue
        for vname, vlab in variants:
            if g.startswith("experiment") and vname != "all_names":
                continue
            for pair, d in h[g][vname].get("decomposition", {}).items():
                if "Q3" not in pair:
                    continue
                gr = lambda x: f"{100 * x:+.1f}%" if x is not None else "<10 authors"  # noqa: E731
                sh = " / ".join(f"{100 * d[k]['share_of_change']:.0f}%" if d[k].get("share_of_change") is not None
                                and abs(d["growth"] or 0) >= 0.03 else "–" for k in ("top1pct", "next9pct", "bottom90pct"))
                lines.append(f"| {glab} | {vlab} | {pair.replace('-Q3', '').replace('_to_', '→')} | {gr(d['growth'])} | "
                             f"{gr(d['top1pct'].get('growth'))} | {gr(d['next9pct'].get('growth'))} | "
                             f"{gr(d['bottom90pct'].get('growth'))} | {sh} |")
    lines += ["", "Shares of the change are omitted (–) when total growth is below 3%, where they are unstable.", "",
              "**January–August windows** (comparable with Nee, Zhong & Ni 2026):", ""]
    for g, glab in groups:
        if g not in h:
            continue
        for vname, vlab in variants:
            if g.startswith("experiment") and vname != "all_names":
                continue
            ja = h[g][vname]["jan_aug"]
            if "2025-JanAug" in ja and "2026-JanAug" in ja:
                a, b = ja["2025-JanAug"], ja["2026-JanAug"]
                f = lambda x, d=1: pct(x, d) if x is not None else "<10 authors"  # noqa: E731
                lines.append(f"- {glab}, {vlab}: papers {a['papers']:,} → {b['papers']:,}; with a heavy producer "
                             f"{f(a['share_papers_with_heavy_author'])} → {f(b['share_papers_with_heavy_author'])}; "
                             f"authors ≥5 {f(a['share_authors_ge5'], 2)} → {f(b['share_authors_ge5'], 2)}; "
                             f"top-1% share {f(a['top1pct_share_of_output'])} → {f(b['top1pct_share_of_output'])}")
    lines.append("")


def ci3(d, digits=2):
    return f"{d['rr']:.{digits}f} [{d['lo']:.{digits}f}, {d['hi']:.{digits}f}]"


def r1(lines, r):
    lines += ["## Round-1 review analyses (confounds of the field-level finding)", "",
              "Generated from `data/processed/stats/round1_tests.json` (`scripts/stats_round1.py`). Item labels follow the "
              "consolidated review request.", ""]
    e = r.get("estimands")
    if e:
        lines += ["### P1c. Estimands and inference for the within-field contrasts", "",
                  "Rate ratio of group A to group B in 2026 relative to the stated base (Poisson event study, Driscoll–Kraay "
                  "95% CI); the 2026/2025 ratio (acceleration); and the placebo p-value (share of the 153 pairs of arXiv "
                  "archives, or of the 462 halvings of the wet-lab categories, whose 2026 ratio is at least as far from 1). "
                  "The year-shock z of round 1 is replaced by the rank-based calibration below.", "",
                  "| Contrast | Base | 2026 | 2026 / 2025 | Placebo p |", "|---|---|---|---|---|"]
        for name, v in e.items():
            if not isinstance(v, dict) or "by_base" not in v:
                continue
            for b, bb in v["by_base"].items():
                ev = bb["event_study"]
                pl = f"{v['placebo_p_2026']:.2f}" if "placebo_p_2026" in v and b == "2022" else "–"
                lines.append(f"| {name} | {b} | {ci3(ev['2026'])} | {ci3(ev['2026_vs_2025'])} | {pl} |")
        lines += ["", "Change in the slope of the deseasonalised log ratio after a known date (per year; Newey–West CI; "
                  "AR(1) bootstrap p):", ""]
        for name, v in e.items():
            if isinstance(v, dict) and "slope_change_after_2022_12" in v:
                a, b = v["slope_change_after_2022_12"], v["slope_change_after_2024_11"]
                lines.append(f"- {name}: after Dec 2022 {100 * a['slope_change_per_year']:+.1f}% "
                             f"[{100 * a['lo']:+.1f}, {100 * a['hi']:+.1f}], p = {a['p_bootstrap']:.3f}; after Nov 2024 "
                             f"{100 * b['slope_change_per_year']:+.1f}% [{100 * b['lo']:+.1f}, {100 * b['hi']:+.1f}], "
                             f"p = {b['p_bootstrap']:.3f} (pre-2023 slope {100 * a['pre_slope_per_year']:+.1f}% a year)")
        lines.append("")
    pl = r.get("planned")
    if pl:
        lines += ["### Round 2. The specification planned in draft v1", "",
                  "Period effects (2023–2024, 2025, 2026) against the planned multi-year baseline (from the first month "
                  "shown to December 2022), calendar-month effects common to both groups, Newey–West (Driscoll–Kraay) "
                  "errors with 12 lags. The plan replaced the Poisson model by a negative binomial (NB2) if the counts "
                  "were overdispersed (Cameron–Trivedi test, 5%); 98.3% Bonferroni intervals over the three contrasts. "
                  "Checks: moving-block bootstrap of the log ratio (12-month blocks, 999 draws) and group-specific linear "
                  "trends. The last column is the estimate as run (year effects, base 2022).", "",
                  "| Contrast | Baseline | Model (Pearson dispersion) | 2023–2024 | 2025 | 2026 (95% CI) | 2026, 98.3% CI | p | "
                  "Bootstrap 2026 | With group trends, 2026 | As run, base 2022 |", "|---|---|---|---|---|---|---|---|---|---|---|"]
        for name, v in pl.items():
            m = v[v["planned_model"]]
            lines.append(f"| {name} | {v['baseline']} | {v['planned_model'].replace('_', ' ')} "
                         f"({v['overdispersion']['pearson_dispersion']:.1f}) | {ci3(m['2023-2024'])} | {ci3(m['2025'])} | "
                         f"{ci3(v['planned_2026'])} | {ci3(v['planned_2026_bonferroni'])} | {v['planned_2026']['p']:.2f} | "
                         f"{ci3(v['block_bootstrap_2026'])} | {ci3(v['with_group_trends']['2026'])} | "
                         f"{ci3(v['as_run_2022_base_2026'])} |")
        lines.append("")
    cal = r.get("calibration")
    if cal:
        lines += ["### Round 2. Rank-based in-time calibration (replaces the year-shock z)", "",
                  "The same event-study estimator as above. Level: the 2026 log rate ratio against all years to 2022 "
                  "pooled, ranked among each of those years' log rate ratios against the other years pooled (so every "
                  "statistic is centred on the pre-period mean). Acceleration: the change from 2025 to 2026, ranked among "
                  "the earlier year-on-year changes, to 2022 and to 2025. p = (number of reference values at least as "
                  "large + 1) / (number of reference values + 1); two-sided on absolute values, one-sided in the observed "
                  "direction. With n reference values, p cannot fall below 1/(n + 1).", "",
                  "| Series | 2026 vs pre-period | p two-sided / one-sided (n) | 2026 / 2025 | p vs changes to 2022 (n) | "
                  "p vs all earlier changes, two-sided / one-sided (n) |", "|---|---|---|---|---|---|"]
        for name, v in cal.items():
            lv, a1, a2 = v["level"], v["acceleration_pre_period"], v["acceleration_all_earlier"]
            lines.append(f"| {name} | {lv['rr']:.3f} | {lv['p_two_sided']:.2f} / {lv['p_one_sided']:.2f} ({lv['n_ref']}) | "
                         f"{a1['rr']:.3f} | {a1['p_two_sided']:.2f} ({a1['n_ref']}) | {a2['p_two_sided']:.2f} / "
                         f"{a2['p_one_sided']:.2f} ({a2['n_ref']}) |")
        lines.append("")
    b = r.get("breaks")
    if b:
        lines += ["### P1d. Break tests that can see 2025–2026", "",
                  "Deseasonalised log series (fields) or log ratios (contrasts). Unknown date: sup-Wald with 5% trimming "
                  "(candidates up to the stated month). Known dates: Wald tests at December 2022, November 2024 and "
                  "November 2025. AR(1) parametric-bootstrap p-values (999 draws).", "",
                  "| Series | Slope break (unknown date) | Level break (unknown date) | Slope: Dec 2022 / Nov 2024 / Nov 2025 (p) |",
                  "|---|---|---|---|"]
        for name, v in b.items():
            su, lu = v["slope_unknown_trim5"], v["level_unknown_trim5"]
            kn = " / ".join(f"{x['p_bootstrap']:.3f}" for x in v["slope_known"].values())
            lines.append(f"| {name} | {su['break_month']} (p = {su['p_bootstrap']:.3f}; last candidate "
                         f"{su['last_candidate']}) | {lu['break_month']} (p = {lu['p_bootstrap']:.3f}) | {kn} |")
        lines.append("")
    c = r.get("crosslists")
    if c:
        lines += ["### P1g. New submissions vs list entries (new + cross-lists)", "",
                  "| Field | 2026 departure from 2015–2022 trend, new | New + cross-lists |", "|---|---|---|"]
        for f, v in c["fields"].items():
            lines.append(f"| {f} | {ci3(v['new']['2026'])} | {ci3(v['new_plus_cross']['2026'])} |")
        lines += ["", f"Mathematics' rank among arXiv archives (placebo p): new {c['archives']['new']['math_rank_p']:.2f}; "
                  f"new + cross-lists {c['archives']['new_plus_cross']['math_rank_p']:.2f}.", ""]
    f = r.get("funding")
    if f:
        pm = f["pubmed_us_vs_non_us"]
        lines += ["### P1e. Funding shock: US vs non-US", "",
                  "PubMed journal articles with at least one US affiliation vs the rest (quarterly; rate ratio relative to "
                  "the stated base):", "",
                  f"- base 2023–2024: 2025 {ci3(pm['base_2023_2024']['2025'])}; 2026 {ci3(pm['base_2023_2024']['2026'])}; "
                  f"2026/2025 {ci3(pm['base_2023_2024']['2026_vs_2025'])}; pre-period: " +
                  "; ".join(f"{y} {pm['base_2023_2024'][y]['rr']:.3f}" for y in ("2019", "2020", "2021", "2022")),
                  f"- US share of journal articles: " + ", ".join(f"{q} {100 * v:.1f}%" for q, v in pm["us_share"].items()
                                                                if q.endswith("Q3")), ""]
        for k, v in f.items():
            if k.startswith("biorxiv_"):
                lines.append(f"- {k} (base 2023–2024): 2025 {ci3(v['base_2023_2024']['2025'])}; 2026 "
                             f"{ci3(v['base_2023_2024']['2026'])}; US share by year: " +
                             ", ".join(f"{y} {100 * x:.1f}%" for y, x in v["us_share_by_year"].items()))
        lines.append("")
    o = r.get("oai")
    if o:
        lines += ["### P1b. Snowmass 2021 and European Strategy inputs; C1 variants", "",
                  "| Archive | Snowmass share, Jan–Sep 2022 | European Strategy share, Jan–Sep 2025 |", "|---|---|---|"]
        for a, v in o["snowmass_espp"].items():
            lines.append(f"| {a} | {pct(v['snowmass_share_2022'])} ({v['snowmass_jan_sep_2022']}) | "
                         f"{pct(v['espp_share_2025'])} ({v['espp_jan_sep_2025']}) |")
        lines += ["", "Contrasts after removing those papers (2026 rate ratio):", ""]
        for name, v in o["clean_physics"].items():
            if "base_2022" in v:
                lines.append(f"- {name}: base 2022 {ci3(v['base_2022']['2026'])}; base 2017–2019 "
                             f"{ci3(v['base_2017_2019']['2026'])}")
        hx = o["clean_physics"]["hep-ex_field_model"]
        lines += [f"- hep-ex, 2026 departure from trend: raw {ci3(hx['raw']['2026'])}; without Snowmass and European "
                  f"Strategy papers {ci3(hx['without_snowmass_espp']['2026'])}", "",
                  "### P1f. Genres (maths and the six HEP/nuclear archives only)", "",
                  "Genre from keywords in the comments, title or abstract (white papers; proceedings; theses; reviews, "
                  "lectures and chapters); everything else is a research article.", ""]
        for g, v in o["genre"].items():
            gc = v["genre_counts"]
            share = "; ".join(f"{y[:4]}: " + ", ".join(f"{k} {100 * n / sum(c.values()):.1f}%" for k, n in sorted(c.items())
                                                       if k != "research") for y, c in gc.items() if y[:4] in ("2022", "2025", "2026"))
            fa, fr = v["field_model_2019_2026"]["all"]["2026"], v["field_model_2019_2026"]["research_only"]["2026"]
            ga, gr_ = v["all"]["growth"], v["research_only"]["growth"]
            lines.append(f"- {g}: genre shares (Jan–Sep) {share}. Growth Jan–Sep 2025 → 2026: all {100 * ga['jan_sep']:+.1f}%, "
                         f"research only {100 * gr_['jan_sep']:+.1f}%. 2026 departure from the 2019–2022 trend: all "
                         f"{ci3(fa)}, research only {ci3(fr)}")
        lines.append("")
    mf = r.get("medrxiv_flags")
    if mf:
        lines += ["### P3. medRxiv flags", "",
                  "Each preprint counted once (the API lists some version-1 preprints twice; see Methods). C3 rate ratio "
                  "in 2026 under each flag definition (base 2022; in brackets base 2019 + 2022):", ""]
        for k, v in mf["C3_variants"].items():
            lines.append(f"- {k}: {ci3(v['base_2022']['2026'])} ({ci3(v['base_2019_2022']['2026'])}); 2026/2025 "
                         f"{ci3(v['base_2022']['2026_vs_2025'])}")
        yrs = mf["by_year_jan_sep"]
        lines += ["", "Preprints added by Spick et al.'s four datasets (January–September, non-COVID): " + ", ".join(
            f"{y} {c.get('spick4_only_noncovid', 0)} of {c.get('public_or_spick4_noncovid', 0)}" for y, c in yrs.items()
            if y >= "2022"), "",
            f"Non-COVID medRxiv index, Q3 2026 (2022 = 100): {mf['noncovid_index_2022_100']['title_or_abstract']['2026-Q3']:.1f} "
            f"with a title-or-abstract COVID-19 filter, {mf['noncovid_index_2022_100']['title_only']['2026-Q3']:.1f} with a "
            "title-only filter.", ""]
    ins = r.get("inspire")
    if ins:
        lines += ["### Exploratory: INSPIRE-HEP (pre-registration §10)", "",
                  f"{ins['n_records']:,} INSPIRE records with a primary arXiv category in hep-ex, hep-ph, hep-th, hep-lat, "
                  "nucl-ex or nucl-th, 2017–2026, dated by first arXiv version. ND-INSPIRE: research article, experimental "
                  "INSPIRE category, linked to an experiment or collaboration, no prospect or sensitivity wording; NN-INSPIRE: "
                  "all others. Departures from the 2017–2022 trend (field model) and the ratio NN/ND of the 2026 departures "
                  "(approximate CI from independent fits).", "",
                  "| Rule | Scope | ND papers | NN papers | ND 2026 | NN 2026 | NN/ND 2026 |", "|---|---|---|---|---|---|---|"]
        for k, v in ins["classes"].items():
            rule, scope = k.split("__")
            f = lambda d: ci3(d["2026"]) if d else "n/a"  # noqa: E731
            rr = v["RRR_NN_vs_ND"]["2026"]
            lines.append(f"| {rule} | {scope} | {v['n_ND']:,} | {v['n_NN']:,} | {f(v['ND'])} | {f(v['NN'])} | "
                         f"{ci3(rr) if rr else 'n/a'} |")
        lines += ["", "hep-ex + nucl-ex by author count (2026 departure): " + "; ".join(
            f"{b} ({v['n']:,} papers) {ci3(v['departure']['2026']) if v['departure'] else 'n/a'}"
            for b, v in ins["by_author_count_hep-ex_nucl-ex"].items()) + ".",
                  "By document type: " + "; ".join(f"{t} ({v['n']:,}) {ci3(v['departure']['2026']) if v['departure'] else 'n/a'}"
                                                  for t, v in ins["by_document_type_hep-ex_nucl-ex"].items()) + ".",
                  "Snowmass and European Strategy records by year: " + "; ".join(
                      f"{y} {v['snowmass']} / {v['european_strategy']} of {v['all']:,}" for y, v in
                      ins["snowmass_espp_by_year"].items() if y in ("2021", "2022", "2025")) + ".", ""]
    d = r.get("dating")
    if d:
        lines += ["### P1a. Announcement vs first-version submission", "",
                  f"First-version dates known for {pct(d['v1_known_share_2024_on'])} of papers announced from January 2024 "
                  "(OAI `created` is the latest version's date; revised papers' v1 dates come from the arXiv API).", "",
                  "| Group | Dating | Jan–Aug | Jan–Sep | Q3 | September | Trailing 12 months |", "|---|---|---|---|---|---|---|"]
        for g, v in d["groups"].items():
            for k, lab in (("by_identifier", "announcement"), ("by_v1_submission", "v1 submission")):
                gg = v[k]["growth"]
                lines.append(f"| {g} | {lab} | " + " | ".join(f"{100 * gg[x]:+.1f}%" for x in
                                                                ("jan_aug", "jan_sep", "q3", "sep", "trailing12")) + " |")
        lines += ["", "Share of papers announced in a month that were submitted in an earlier month:", ""]
        for g, v in d["groups"].items():
            sh = v["share_submitted_in_an_earlier_month"]
            lines.append(f"- {g}: " + ", ".join(f"{m} {100 * x:.0f}%" for m, x in sh.items() if m >= "2025-07"))
        lines.append("")


def dating2(lines, r):
    """Round 2, item 6: dating by first-version submission."""
    d, ins = r.get("dating") or {}, r.get("inspire_dating")
    if ins:
        lines += ["### Round 2. INSPIRE-HEP dated by submission against arXiv's statistics pages", "",
                  "Growth from 2025 to 2026 by primary archive: INSPIRE-HEP records counted by `preprint_date` "
                  "(first-version submission) and arXiv's statistics pages (new submissions, counted by announcement).", "",
                  "| Archive | Jan–Sep: INSPIRE, submission | Jan–Sep: statistics pages, announcement | Jan–Aug: INSPIRE | "
                  "Jan–Aug: statistics pages | September 2026: INSPIRE / pages |", "|---|---|---|---|---|---|"]
        for a, v in ins["growth_2025_to_2026"].items():
            def g(k, src):
                return f"{100 * v[k][src]['growth']:+.1f}%"
            lines.append(f"| {a} | {g('jan_sep', 'inspire_by_submission')} | "
                         f"{g('jan_sep', 'statistics_pages_by_announcement')} | {g('jan_aug', 'inspire_by_submission')} | "
                         f"{g('jan_aug', 'statistics_pages_by_announcement')} | "
                         f"{v['sep_2026']['inspire_by_submission']:,} / {v['sep_2026']['statistics_pages_by_announcement']:,} |")
        wk = ins["weekend_share_of_submission_dates"]
        lines += ["", f"Records whose arXiv identifier month is later than their submission month: "
                  f"{pct(ins['identifier_month_later_overall'])} overall; by year " +
                  ", ".join(f"{y} {pct(x)}" for y, x in ins["identifier_month_later_than_submission"].items()) +
                  f". Submission dates on Saturdays: {pct(wk['saturday'])}; on Sundays: {pct(wk['sunday'])} (arXiv does "
                  "not announce on those days).", ""]
    ms = d.get("maths_september")
    if ms:
        lines += ["### Round 2. The September 2026 spike in mathematics and October 2026 under the cap", ""]
        for y, v in ms.items():
            lines.append(f"- September {y}: {v['by_identifier']:,} mathematics papers announced (identifier month) and "
                         f"{v['submitted_in_september']:,} submitted (first version) in September. Of the announced papers "
                         f"with a known v1 date ({v['v1_known']:,}), "
                         f"{pct(v['identifier_september_submitted_earlier'] / v['v1_known'])} were submitted in an earlier "
                         f"month and {pct(v['identifier_september_submitted_over_7_days_before'] / v['v1_known'])} more than "
                         "seven days before 1 September.")
        o = d["october_2026"]
        wins = list(o["weekdays_in_window"])
        lines += ["", "Papers by first-version date in 14-day and 7-day windows (weekdays per window: " +
                  ", ".join(f"{w} {n}" for w, n in o["weekdays_in_window"].items()) + "). arXiv's cap of two "
                  "submissions per submitter a month applies from 1 October 2026. The harvest of 16 October holds "
                  "announcements to 15 October, so the October 2026 counts miss papers still on hold and are lower "
                  "bounds.", "",
                  "| Group | " + " | ".join(wins) + " | Oct 1–14, 2026 / 2025 | Oct 1–14 / Sep 1–14, 2026 |",
                  "|---|" + "---|" * (len(wins) + 2)]
        for g, c in o["counts_by_v1_date"].items():
            lines.append(f"| {g} | " + " | ".join(f"{c[w]:,}" for w in wins) +
                         f" | {c['oct_01_14_2026'] / c['oct_01_14_2025']:.2f} | "
                         f"{c['oct_01_14_2026'] / c['sep_01_14_2026']:.2f} |")
        lines.append("")
    cd = d.get("contrasts_by_dating")
    if cd:
        lines += ["### Round 2. C1 and arXiv against bioRxiv, dated by announcement or by first-version submission", "",
                  "Event study as in P1c (base 2022), February 2019 to the stated month. 'Statistics pages' are arXiv's "
                  "published counts; the other two columns count the same OAI records by identifier (announcement) month "
                  "or by first-version month (identifier month when the v1 date is unknown, which holds for papers first "
                  "posted before December 2023 and revised later). Cells: 2026 rate ratio [95% CI]; 2026/2025 ratio.", "",
                  "| Series | Data to | Statistics pages | OAI, identifier month | OAI, v1 month |", "|---|---|---|---|---|"]
        res = cd["results"]
        for n in res["identifier|to_2026-09"]:
            for last in ("2026-09", "2026-08"):
                cells = [f"{ci3(res[f'{src}|to_{last}'][n]['2026'])}; {res[f'{src}|to_{last}'][n]['2026_vs_2025']['rr']:.3f}"
                         for src in ("statistics_pages", "identifier", "v1")]
                lines.append(f"| {n} | {last} | " + " | ".join(cells) + " |")
        lines.append("")


def placebos_matched(lines, r):
    """Round 2, item 8: in-space placebos matched to each contrast's structure."""
    pm = r.get("placebos_matched")
    if not pm:
        return
    lines += ["### Round 2. Placebos matched to each contrast's structure", "",
              "Every grouping with the contrast's structure, the observed one included, so p cannot fall below 1/n "
              "(the floor). C1: four theory archives against two experimental ones, as splits of the six particle and "
              "nuclear physics archives and as disjoint draws from the 13 physics archives; C1 without gr-qc: three "
              "against two; C2: three of the fifteen bioRxiv categories as the computational group against the other "
              "twelve. Statistics from the event-study estimator (base 2022); p two-sided on |log ratio|, one-sided in "
              "the observed direction.", "",
              "| Contrast | Reference set | n (floor) | 2026 vs 2022: observed; p two-sided / one-sided | Placebo 5th / 50th / "
              "95th percentile | 2026 / 2025: observed; p two-sided / one-sided |", "|---|---|---|---|---|---|"]
    for name, v in pm.items():
        for ref, x in v.items():
            if ref == "observed":
                continue
            a, b = x["2026_vs_2022"], x["2026_vs_2025"]
            q = " / ".join(f"{t:.2f}" for t in a["placebo_rr_5_50_95"])
            lines.append(f"| {name} | {ref.replace('_', ' ')} | {x['n']:,} ({x['floor']:.4f}) | {a['observed_rr']:.3f}; "
                         f"{a['p_two_sided']:.3f} / {a['p_one_sided']:.3f} | {q} | {b['observed_rr']:.3f}; "
                         f"{b['p_two_sided']:.3f} / {b['p_one_sided']:.3f} |")
    lines.append("")


def inspire_round2(lines, r):
    """Round 2, item 9: the INSPIRE classes with the C1-C3 estimator."""
    ins = r.get("inspire_round2")
    if not ins:
        return
    pf = ins["planning_flagged"]
    lines += ["### Round 2. INSPIRE-HEP classes with the estimator of C1–C3", "",
              f"NN-INSPIRE (group A) against ND-INSPIRE (group B), event study as in P1c, 2026 rate ratio [95% CI] by base. "
              f"Planning papers: {pf['inspire_flags']} records flagged by INSPIRE's title-and-abstract flags, "
              f"{pf['with_arxiv_flags']} with the arXiv flags that also read the comments (matched by arXiv identifier, "
              f"2019 on). Author count 0 (author list not yet loaded; {ins['author_count_zero']} records) is treated as "
              "missing. 'ND with collaboration' requires a collaboration field.", "",
              "| Scope | Sample | ND rule | NN; ND records | Base 2022 | Base 2017–2019 | Base 2017–2019 + 2022 | "
              "Base 2017–2022 | 2026 / 2025 |", "|---|---|---|---|---|---|---|---|---|"]
    for k, v in ins["contrasts"].items():
        scope, smp, rule = k.split("|")
        cells = [ci3(v[b]["2026"]) if b in v else "–" for b in ("2022", "2017-2019", "2017-2019+2022", "2017-2022")]
        acc = ci3(v["2022"]["2026_vs_2025"]) if "2022" in v else "–"
        lines.append(f"| {scope} | {smp.replace('_', ' ')} | {rule.replace('_', ' ')} | {v['n_NN']:,}; {v['n_ND']:,} | "
                     + " | ".join(cells) + f" | {acc} |")
    pdp = ins["proceedings_departure"]
    lines += ["", "Proceedings (conference papers, planning papers removed), 2026 departure from the 2017–2022 trend: " +
              "; ".join(f"{sc} {ci3(v['2026'])} ({v['n']:,} records)" if "2026" in v else
                        f"{sc} not estimated ({v['n']:,} records, {v['months_with_zero']} months with none)"
                        for sc, v in pdp.items()) + ".", "",
              "Records with primary category hep-ex or nucl-ex, January–September of each year: shares with an "
              "experiment link, a collaboration, each document type, a planning flag, and cross-lists.", "",
              "| Year | Records | Experiment link | Collaboration | Conference paper | Research article | Planning | "
              "Cross-list physics.ins-det | Cross-list cs or stat | Author count 0 | ND |",
              "|---|---|---|---|---|---|---|---|---|---|---|"]
    for y, v in ins["hep-ex+nucl-ex_shares_jan_sep"].items():
        lines.append(f"| {y} | {v['records']:,} | " + " | ".join(
            f"{v[k]:.3f}" for k in ("experiment_link", "collaboration", "conference_paper", "research_article",
                                    "planning", "cross_list_physics.ins-det", "cross_list_cs_or_stat")) +
            f" | {v['author_count_zero']} | {v['ND']:.3f} |")
    lines.append("")
    xl = r.get("hepex_crosslists")
    if xl:
        by = xl["hep-ex_primary_by_month"]
        into = xl["cross_listed_into_hep-ex_by_month"]

        def tot(months, key, src):
            return sum(src[m][key] for m in months if m in src)
        lines += ["Cross-lists of papers with primary category hep-ex, from the arXiv OAI records (so not an INSPIRE "
                  "curation effect), by half-year: papers; with any cross-list; with physics.ins-det; with cs or stat; "
                  "and papers of other primary categories cross-listed into hep-ex (of which physics.ins-det primary):", ""]
        for y in range(2023, 2027):
            for h, ms in (("H1", [f"{y}-{i:02d}" for i in range(1, 7)]), ("H2", [f"{y}-{i:02d}" for i in range(7, 13)])):
                if not any(m in by for m in ms):
                    continue
                lines.append(f"- {y} {h}: {tot(ms, 'papers', by):,} papers; {tot(ms, 'any_cross_list', by):,} with a "
                             f"cross-list; {tot(ms, 'physics.ins-det', by)} physics.ins-det; {tot(ms, 'cs_or_stat', by)} cs "
                             f"or stat; {tot(ms, 'all', into):,} cross-listed into hep-ex ({tot(ms, 'physics.ins-det', into)} "
                             "physics.ins-det primary)")
        lines.append("")


def funding_round2(lines, r):
    """Round 2, item 10: bioRxiv and medRxiv by country, PubMed calibrated in time."""
    f = r.get("funding_round2")
    if not f:
        return
    lines += ["### Round 2. The funding explanation: bioRxiv and medRxiv by country, PubMed in time", "",
              f"**Prediction.** {f['prediction']}", "",
              "US against non-US preprints by the corresponding author's institution (preprints with no country left "
              "out), event study as in P1c. The country classifier was checked by an AI agent only; a human spot-check "
              "sheet is in `docs/stats/validation/country_spot_check_sheet.csv`.", "",
              "| Series | 2025 vs 2023–2024 | 2026 vs 2023–2024 | 2026 vs 2022 | Jan–Sep US 2024 / 2025 / 2026 | "
              "Jan–Sep non-US 2024 / 2025 / 2026 | No country, 2026 |", "|---|---|---|---|---|---|---|"]
    rows = [(f"bioRxiv {g.replace('_', ' ')}", v) for g, v in f["biorxiv"].items() if g != "wet_lab_vs_computational"]
    rows += [(f"medRxiv {sc.replace('noncovid', 'without COVID-19')}", v) for sc, v in f["medrxiv"].items()]
    for name, v in rows:
        js = v["jan_sep_counts"]
        lines.append(f"| {name} | {ci3(v['base_2023_2024']['2025'])} | {ci3(v['base_2023_2024']['2026'])} | "
                     f"{ci3(v['base_2022']['2026'])} | " +
                     " / ".join(f"{js[y]['US']:,}" for y in ("2024", "2025", "2026")) + " | " +
                     " / ".join(f"{js[y]['non-US']:,}" for y in ("2024", "2025", "2026")) +
                     f" | {pct(js['2026']['unknown'] / sum(js['2026'].values()))} |")
    wc = f["biorxiv"]["wet_lab_vs_computational"]
    pm = f["pubmed_us_vs_non_us"]
    lines += ["", "bioRxiv wet lab against computational (ratio of the two US/non-US ratios, base 2023–2024; independent "
              f"fits): 2025 {ci3(wc['2025'])}, 2026 {ci3(wc['2026'])}.", "",
              "PubMed US/non-US ratio, year-on-year change: " +
              ", ".join(f"{y} {100 * (v - 1):+.1f}%" for y, v in pm["year_on_year_change"].items()) +
              "; two-year change: " + ", ".join(f"{y} {100 * (v - 1):+.1f}%" for y, v in pm["two_year_change"].items()) +
              ". Rank among earlier changes (one-sided, falls; n): " + "; ".join(
                  f"{lab} {pm[k]['p_one_sided_fall']:.2f} ({pm[k]['n_ref']})" for k, lab in
                  (("rank_2025_change", "2025"), ("rank_2026_change", "2026"), ("rank_2024_to_2026", "2024 to 2026"))) +
              ".", ""]


def h2_round2(lines, d):
    """Round 2, item 7: H2 with classes ranked on an independent window, and the uniform-scaling simulation."""
    path = os.path.join(d, "h2_round2.json")
    if not os.path.exists(path):
        return
    h = json.load(open(path))
    lines += ["### Round 2. H2: classes ranked on an independent window; uniform-scaling simulation", "",
              "Names ranked on fractional output in the twelve months before the first compared window (Q3 of the "
              "previous year to Q2 for third quarters; the previous calendar year for January–August); growth of each "
              "class between the two compared windows. 'New top 1%': share of the total increase that came from names "
              "in the combined-output top 1% (the main decomposition's class) that were not in the ranking window's top "
              "1%; 'old': from names that were.", "",
              "| Group | Names | Pair | Total | Top 1% | Next 9% | Bottom 90% | Not active in ranking window | "
              "Increase from new top 1% / old top 1% |", "|---|---|---|---|---|---|---|---|---|"]

    def g_(x):
        return "–" if x is None else f"{100 * x:+.0f}%"
    for grp in ("maths", "theory_max50_authors"):
        for v in ("all_names", "full_first_names_no_top1pct_surnames"):
            for pair, x in h[grp][v]["independent_window"].items():
                c = x["combined_top1pct"]
                lines.append(f"| {grp} | {v.replace('_', ' ')} | {pair.replace('_to_', ' → ')} | {g_(x['growth'])} | " +
                             " | ".join(g_(x[k].get("growth")) for k in ("top1pct", "next9pct", "bottom90pct",
                                                                           "not_active_in_ranking_window")) +
                             f" | {g_(c['share_of_change_from_names_not_in_ranking_top1pct'])} / "
                             f"{g_(c['share_of_change_from_names_in_ranking_top1pct'])} |")
    lines += ["", "Uniform-scaling simulation (all names): a pool of names with Gamma or lognormal rates, calibrated to the "
              "first window's active names and top-1% share, fills author slots of papers with the observed team sizes; "
              "the number of papers is scaled by the observed growth with every rate unchanged. Mean (SD) over 100 "
              "replications of the change in the share of fractional output of the top 1% and top 10% of active names.", "",
              "| Group | Pair | Papers | Observed change, top 1%; top 10% | Model (parameter; fit of top 1% and top 10% in "
              "the first window) | Change under uniform scaling, top 1%; top 10% | Share of the observed change | "
              "Active names: observed; under the null |", "|---|---|---|---|---|---|---|---|"]
    for grp in ("maths", "theory_max50_authors"):
        for pair, u in h[grp]["all_names"]["uniform_scaling"].items():
            for m in ("gamma", "lognormal"):
                x = u.get(m)
                if not x:
                    continue
                c = x["calibration"]
                lines.append(
                    f"| {grp} | {pair.replace('_to_', ' → ')} | {g_(u['paper_growth'])} | "
                    f"{100 * u['observed_change_top1']:+.2f} pp; {100 * u['observed_change_top10']:+.2f} pp | {m} "
                    f"({c['parameter']}; {100 * c['top1_sim']:.2f}% vs {100 * u['observed']['a']['top1']:.2f}%, "
                    f"{100 * c['top10_sim']:.1f}% vs {100 * u['observed']['a']['top10']:.1f}%) | "
                    f"{100 * x['null_change_top1']['mean']:+.2f} ({100 * x['null_change_top1']['sd']:.2f}) pp; "
                    f"{100 * x['null_change_top10']['mean']:+.2f} pp | {x['mechanical_fraction_top1']:.2f}; "
                    f"{x['mechanical_fraction_top10']:.2f} | {g_(u['observed_active_growth'])}; "
                    f"{g_(x['null_active_growth'])} |")
    lines.append("")


def jan_aug(lines, d):
    """Round 2, item 6: every 2026 estimate with the data ending in August 2026 beside the main (January-September)
    estimate."""
    stems = ("within_field_tests", "field_tests", "round1_tests")
    if not all(os.path.exists(os.path.join(d, f"{s}_to_2026-08.json")) for s in stems):
        return
    src = {s: (json.load(open(os.path.join(d, f"{s}.json"))), json.load(open(os.path.join(d, f"{s}_to_2026-08.json"))))
           for s in stems}
    num = lambda x: f"{x:.2f}"  # noqa: E731
    rows = []
    conf = {"C1_physics_theory_vs_experiment": "C1", "C2_biology_computational_vs_wetlab": "C2",
            "C3_medicine_public_dataset_vs_rest": "C3"}
    for k, c in conf.items():
        rows += [(f"{c}: 2026 vs 2022", "within_field_tests", lambda x, k=k: x["confirmatory"][k]["event_study"]["2026"], ci3),
                 (f"{c}: Holm-adjusted p", "within_field_tests", lambda x, k=k: x["confirmatory"][k]["p_holm_2026"], num),
                 (f"{c}: minimum detectable rate ratio, 80% power", "within_field_tests",
                  lambda x, k=k: 1 + x["confirmatory"][k]["mde_2026_80pct_power"], num)]
    for n in ("C1_theory_vs_experiment", "C1_theory_without_gr-qc_vs_experiment", "C2_computational_vs_wet_lab",
              "C3_public_dataset_vs_other"):
        rows += [(f"{n}: placebo p", "round1_tests", lambda x, n=n: x["estimands"][n]["placebo_p_2026"], num),
                 (f"{n}: 2026 / 2025", "round1_tests",
                  lambda x, n=n: x["estimands"][n]["by_base"]["2022"]["event_study"]["2026_vs_2025"], ci3)]
        for b in src["round1_tests"][0]["estimands"].get(n, {}).get("by_base", {}):
            if b != "2022":
                rows.append((f"{n}: 2026, base {b}", "round1_tests",
                             lambda x, n=n, b=b: x["estimands"][n]["by_base"][b]["event_study"]["2026"], ci3))
        rows += [(f"{n}: planned specification, 2026", "round1_tests", lambda x, n=n: x["planned"][n]["planned_2026"], ci3),
                 (f"{n}: calibration, 2026/2025 rank p (all earlier changes)", "round1_tests",
                  lambda x, n=n: x["calibration"][n]["acceleration_all_earlier"]["p_two_sided"], num)]
    for n in ("C1", "C1_without_gr-qc", "hep-ph_vs_hep-ex", "hep-th_vs_hep-ex"):
        for b in ("base_2022", "base_2017_2019"):
            rows.append((f"{n} without planning papers: 2026, {'base 2022' if b == 'base_2022' else 'base 2017–2019'}",
                         "round1_tests",
                         lambda x, n=n, b=b: x["oai"]["clean_physics"][n][b]["2026"], ci3))
    for n, ref in (("C1_theory_vs_experiment", "splits_of_the_hep_nucl_archives"),
                   ("C1_theory_vs_experiment", "draws_from_13_physics_archives"),
                   ("C2_computational_vs_wet_lab", "three_of_the_fifteen_categories")):
        rows.append((f"{n}: matched placebo p, {ref.replace('_', ' ')} (two-sided)", "round1_tests",
                     lambda x, n=n, ref=ref: x["placebos_matched"][n][ref]["2026_vs_2022"]["p_two_sided"], num))
    for k in src["within_field_tests"][0]["leave_one_out"]:
        rows.append((f"Leave one out: {k}", "within_field_tests", lambda x, k=k: x["leave_one_out"][k], ci3))
    for g in ("arxiv_physics_6_vs_biorxiv", "arxiv_theory_vs_biorxiv", "arxiv_experiment_vs_biorxiv",
              "arxiv_maths_vs_biorxiv", "pubmed_us_vs_non_us"):
        rows.append((f"{g}: 2026 / 2025 (rank p, all earlier changes)", "round1_tests",
                     lambda x, g=g: x["calibration"][g]["acceleration_all_earlier"],
                     lambda v: f"{v['rr']:.3f} (p {v['p_two_sided']:.2f})"))
    for k in src["field_tests"][0]["fields"]:
        if not k.startswith("social"):
            rows.append((f"Departure from trend, 2026: {k}", "field_tests", lambda x, k=k: x["fields"][k]["2026"], ci3))
    rows += [("Synthetic control, mathematics: gap in 2026", "field_tests",
              lambda x: x["synthetic_control_math"]["gap_2026_pct"], pct),
             ("Synthetic control, mathematics: rank p", "field_tests", lambda x: x["synthetic_control_math"]["rank_p"], num),
             ("Mathematics' rank among archive departures: p", "field_tests", lambda x: x["math_rank_p"], num)]
    lines += ["### Round 2. January–August versions of the 2026 estimates", "",
              "Every estimate re-run with the data ending in August 2026 (`STATS_LAST=2026-08`; files "
              "`*_to_2026-08.json`), leaving out September 2026, the month before arXiv's submission cap, when mathematics "
              "submissions doubled. In the event studies the 2026 effect is then January–August against whole earlier "
              "years, with calendar-month effects; PubMed, which is quarterly, ends in the second quarter.", "",
              "| Estimate | January–September 2026 | January–August 2026 |", "|---|---|---|"]
    for label, s, get, fmt in rows:
        cells = []
        for x in src[s]:
            try:
                cells.append(fmt(get(x)))
            except (KeyError, TypeError, IndexError):
                cells.append("–")
        lines.append(f"| {label} | {cells[0]} | {cells[1]} |")
    lines.append("")


def main(repo):
    d = os.path.join(repo, "data/processed/stats")
    lines = ["# Results (generated by scripts/report_stats.py)", "",
             "All estimates come from `data/processed/stats/*.json`. Specifications are in `methods.md`.", ""]
    w, f = json.load(open(os.path.join(d, "within_field_tests.json"))), json.load(open(os.path.join(d, "field_tests.json")))
    p1(lines, w, f)
    if os.path.exists(os.path.join(d, "heavy_producers.json")):
        p2(lines, json.load(open(os.path.join(d, "heavy_producers.json"))))
    if os.path.exists(os.path.join(d, "round1_tests.json")):
        r1(lines, json.load(open(os.path.join(d, "round1_tests.json"))))
        dating2(lines, json.load(open(os.path.join(d, "round1_tests.json"))))
        placebos_matched(lines, json.load(open(os.path.join(d, "round1_tests.json"))))
        inspire_round2(lines, json.load(open(os.path.join(d, "round1_tests.json"))))
        funding_round2(lines, json.load(open(os.path.join(d, "round1_tests.json"))))
        h2_round2(lines, d)
        jan_aug(lines, d)
    os.makedirs(os.path.join(repo, "docs/stats"), exist_ok=True)
    open(os.path.join(repo, "docs/stats/results.md"), "w").write("\n".join(lines) + "\n")
    print("written docs/stats/results.md", len(lines), "lines")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
