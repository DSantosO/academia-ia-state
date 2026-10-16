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


def p3(lines, m):
    lines += ["## H3: AI-writing markers", "",
              f"Core marker words: {len(m['core_words'])} style words of Kobak et al. (2025) with pooled 2019–2022 document "
              f"frequency below {100 * m['threshold']:.1f}% in bioRxiv and medRxiv ({m['baseline_abstracts']:,} baseline abstracts). "
              "Rate = distinct core marker words per 100 abstracts (non-COVID preprints).", "",
              "| Corpus | Group | 2019–2022 mean | 2023 | 2024 | 2025 | 2026 (Jan–Sep) |", "|---|---|---|---|---|---|---|"]
    for src, groups in m["rates"].items():
        for g, v in groups.items():
            cells = []
            for y in ("2023", "2024", "2025", "2026"):
                cells.append(f"{v[y]['markers_per_100']:.1f} (×{v[y]['ratio_to_2019_2022']:.2f})" if y in v else "n/a")
            lines.append(f"| {src} | {g} | {v['baseline_2019_2022_per_100']:.1f} | " + " | ".join(cells) + " |")
    lines += ["", "Is the marker rise the same across groups? Ratio of marker rates, group A / group B, relative to "
              "2019–2022 (OLS on monthly log ratios, t intervals):", ""]
    for k, v in m["did"].items():
        lines.append(f"- {k} ({v['_n_months']} months): " + "; ".join(f"{y}: {ci(d)}" for y, d in v.items()
                                                                       if not y.startswith("_")))
    uvo = m.get("use_vs_output")
    if uvo:
        lines += ["", "**Use vs output: arXiv groups against bioRxiv.** Markers: ratio of marker rates relative to "
                  "2019–2022, on the months both corpora cover (March and September). Output: ratio of new preprints "
                  "relative to 2022 (event-study model of the within-field contrasts, Driscoll–Kraay 95% CI), and 2026 "
                  "relative to 2025 (the 2026 acceleration of one group relative to the other).", "",
                  "| Contrast | Markers 2024 | Markers 2025 | Markers 2026 | Output 2024 | Output 2025 | Output 2026 | "
                  "Output 2026 vs 2025 |", "|---|---|---|---|---|---|---|---|"]
        for k, v in uvo.items():
            mk, out = v["markers"], v["output"]
            lines.append(f"| {k} | " + " | ".join(ci(mk[y]) for y in ("2024", "2025", "2026")) + " | "
                         + " | ".join(ci(out[y]) for y in ("2024", "2025", "2026", "2026_vs_2025")) + " |")
    lb = m.get("llm_share_lower_bound_arxiv")
    if lb:
        lines += ["", "Lower bound on the share of LLM-processed abstracts (Kobak et al. 2025; arXiv only): excess share "
                  "of abstracts with at least one core marker word over the 2019–2022 linear trend, divided by one "
                  "minus the counterfactual share (in brackets: with the 2019–2022 mean as counterfactual).", "",
                  "| Group | Share with a marker, 2019–2022 | 2023 | 2024 | 2025 | 2026 (Jan–Sep) |", "|---|---|---|---|---|---|"]
        for g, v in lb.items():
            base = sum(v[str(y)]["share_with_marker"] for y in range(2019, 2023)) / 4
            cells = [f"≥{pct(v[y]['lower_bound_trend'])} (≥{pct(v[y]['lower_bound_mean'])})" if y in v else "n/a"
                     for y in ("2023", "2024", "2025", "2026")]
            lines.append(f"| arXiv {g} | {pct(base)} | " + " | ".join(cells) + " |")
        lines += ["", "The list was built from 2024 text and its words have drifted since (Methods), so 2024 is the "
                  "cleanest year; later bounds are weaker."]
    pn = m["panel"]
    lines += ["", f"Does the marker rise predict output growth? Category panel ({pn['n_obs']} category-years, "
              f"{pn['n_categories']} categories), growth vs 2022 on marker change, interacted with experimental intensity "
              "(OLS, year effects, SEs clustered by category):", ""]
    for name in ("all", "biorxiv", "arxiv"):
        if name in pn:
            v = pn[name]
            lines.append(f"- {name} (n = {v['n']}, {v.get('clusters', '?')} clusters): " + "; ".join(
                f"{k}: {v[k]['coef']:.4f} [{v[k]['lo']:.4f}, {v[k]['hi']:.4f}], p = {v[k]['p']:.2g}"
                for k in ("dmarker", "experimental", "dmarker:experimental")) + (f" ({v['note']})" if v.get("note") else ""))
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
                  "95% CI); the 2026/2025 ratio (acceleration); the placebo p-value (share of the 153 pairs of arXiv "
                  "archives, or of the 462 halvings of the wet-lab categories, whose 2026 ratio is at least as far from 1); "
                  "and the 2026 coefficient against the spread of the pre-2022 year coefficients (z).", "",
                  "| Contrast | Base | 2026 | 2026 / 2025 | Placebo p | Year-shock z (p) |", "|---|---|---|---|---|---|"]
        for name, v in e.items():
            if not isinstance(v, dict) or "by_base" not in v:
                continue
            for b, bb in v["by_base"].items():
                ev, z = bb["event_study"], bb["year_shock_calibration_2026"]
                lines.append(f"| {name} | {b} | {ci3(ev['2026'])} | {ci3(ev['2026_vs_2025'])} | "
                             f"{v['placebo_p_2026']:.2f} | " if "placebo_p_2026" in v and b == "2022" else
                             f"| {name} | {b} | {ci3(ev['2026'])} | {ci3(ev['2026_vs_2025'])} | – | ")
                lines[-1] += (f"{z['z']:.2f} ({z['p_normal']:.2f}) |" if z else "– |")
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


def main(repo):
    d = os.path.join(repo, "data/processed/stats")
    lines = ["# Results (generated by scripts/report_stats.py)", "",
             "All estimates come from `data/processed/stats/*.json`. Specifications are in `methods.md`.", ""]
    w, f = json.load(open(os.path.join(d, "within_field_tests.json"))), json.load(open(os.path.join(d, "field_tests.json")))
    p1(lines, w, f)
    if os.path.exists(os.path.join(d, "heavy_producers.json")):
        p2(lines, json.load(open(os.path.join(d, "heavy_producers.json"))))
    if os.path.exists(os.path.join(d, "marker_tests.json")):
        p3(lines, json.load(open(os.path.join(d, "marker_tests.json"))))
    if os.path.exists(os.path.join(d, "round1_tests.json")):
        r1(lines, json.load(open(os.path.join(d, "round1_tests.json"))))
    os.makedirs(os.path.join(repo, "docs/stats"), exist_ok=True)
    open(os.path.join(repo, "docs/stats/results.md"), "w").write("\n".join(lines) + "\n")
    print("written docs/stats/results.md", len(lines), "lines")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
