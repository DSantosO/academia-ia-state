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
              "such papers a quarter and very few authors with full first names, so only its all-names version is shown.",
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
                cell = lambda k: pct(q[k][mkey], 2) if k in q and q[k].get(mkey) is not None else "n/a"  # noqa: E731
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
                gr = lambda x: f"{100 * x:+.1f}%" if x is not None else "n/a"  # noqa: E731
                sh = " / ".join(f"{100 * d[k]['share_of_change']:.0f}%" if d[k]["share_of_change"] is not None
                                and abs(d["growth"] or 0) >= 0.03 else "–" for k in ("top1pct", "next9pct", "bottom90pct"))
                lines.append(f"| {glab} | {vlab} | {pair.replace('-Q3', '').replace('_to_', '→')} | {gr(d['growth'])} | "
                             f"{gr(d['top1pct']['growth'])} | {gr(d['next9pct']['growth'])} | "
                             f"{gr(d['bottom90pct']['growth'])} | {sh} |")
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
                lines.append(f"- {glab}, {vlab}: papers {a['papers']:,} → {b['papers']:,}; with a heavy producer "
                             f"{pct(a['share_papers_with_heavy_author'])} → {pct(b['share_papers_with_heavy_author'])}; "
                             f"authors ≥5 {pct(a['share_authors_ge5'], 2)} → {pct(b['share_authors_ge5'], 2)}; "
                             f"top-1% share {pct(a['top1pct_share_of_output'])} → {pct(b['top1pct_share_of_output'])}")
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
    lines += ["", "Is the marker rise the same across groups? Rate ratio of marker rates, group A / group B, relative to 2022 "
              "(Poisson with abstracts offset):", ""]
    for k, v in m["did"].items():
        lines.append(f"- {k}: " + "; ".join(f"{y}: {ci(d)}" for y, d in v.items() if int(y) >= 2023))
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
    os.makedirs(os.path.join(repo, "docs/stats"), exist_ok=True)
    open(os.path.join(repo, "docs/stats/results.md"), "w").write("\n".join(lines) + "\n")
    print("written docs/stats/results.md", len(lines), "lines")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
