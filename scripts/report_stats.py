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


def main(repo):
    d = os.path.join(repo, "data/processed/stats")
    lines = ["# Results (generated by scripts/report_stats.py)", "",
             "All estimates come from `data/processed/stats/*.json`. Specifications are in `methods.md`.", ""]
    w, f = json.load(open(os.path.join(d, "within_field_tests.json"))), json.load(open(os.path.join(d, "field_tests.json")))
    p1(lines, w, f)
    for extra in ("heavy_producers.md", "markers.md"):
        p = os.path.join(d, extra)
        if os.path.exists(p):
            lines += open(p).read().splitlines() + [""]
    os.makedirs(os.path.join(repo, "docs/stats"), exist_ok=True)
    open(os.path.join(repo, "docs/stats/results.md"), "w").write("\n".join(lines) + "\n")
    print("written docs/stats/results.md", len(lines), "lines")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
