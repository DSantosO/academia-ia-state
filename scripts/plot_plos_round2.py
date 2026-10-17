"""Round-2 figures for the PLOS ONE article, in the style of plot_plos.py (175 mm wide; PNG at 300 dpi, SVG and TIFF).
Every number is read from the committed JSON files in data/processed/stats/, so the figures show the values of Table 1,
Table 2 and S5 Table.

Fig4_forest       the 2026 rate ratio of each within-field contrast under every specification
Fig6_departures   2026 departures from the pre-2023 trend by arXiv archive and for the other series
Fig7_h2_ranking   H2: growth by class of names ranked on an independent window; uniform-scaling expectation
Fig8_inspire      INSPIRE-HEP: papers without to papers with new experimental results, 2026, by archive and base
Usage: python3 scripts/plot_plos_round2.py [repo_dir] [figure ...]
"""
import io
import json
import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402
from PIL import Image  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plot_plos import AXIS, CM, GRID, INK, INK2, MUTED, OI, setup  # noqa: E402

WIDTH = 17.5 * CM
PRIMARY = OI["blue"]
YEARS = {"2024": "#86b6ef", "2025": "#3f86d0", "2026": "#104281"}  # one-hue ramp, validated (ordinal, light mode)
GREY = "#a6a6a6"
SHADE = "#e6eef6"


def load(repo, name):
    return json.load(open(os.path.join(repo, "data/processed/stats", name)))


def save(fig, out, name):
    """PNG (300 dpi), SVG and TIFF (LZW, RGB, 300 dpi), with no dates, so re-running reproduces the files."""
    os.makedirs(out, exist_ok=True)
    fig.savefig(os.path.join(out, name + ".svg"), facecolor="white", metadata={"Date": None})
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=300, facecolor="white")
    buf.seek(0)
    img = Image.open(buf).convert("RGB")
    assert img.width <= 2250, f"{name}: {img.width}px wider than PLOS maximum"
    img.save(os.path.join(out, name + ".png"), dpi=(300, 300))
    img.save(os.path.join(out, name + ".tif"), compression="tiff_lzw", dpi=(300, 300))
    plt.close(fig)


def log_axis(ax, lo, hi, ticks):
    ax.set_xscale("log")
    ax.set_xlim(lo, hi)
    ax.set_xticks(ticks)
    ax.set_xticklabels([f"{t:g}" for t in ticks])
    ax.xaxis.set_minor_locator(matplotlib.ticker.NullLocator())
    ax.axvline(1, color=INK2, linewidth=0.7, zorder=1)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(AXIS)
    ax.tick_params(axis="x", length=3, width=0.6, color=AXIS, colors=INK2, pad=2)
    ax.tick_params(axis="y", length=0, colors=INK, pad=4)
    ax.grid(axis="x", color=GRID, linewidth=0.5)
    ax.set_axisbelow(True)


def ci_text(d):
    return f"{d['rr']:.2f} ({d['lo']:.2f}–{d['hi']:.2f})"


def fig4_forest(repo, out):
    r, w, w8 = load(repo, "round1_tests.json"), load(repo, "within_field_tests.json"), \
        load(repo, "within_field_tests_to_2026-08.json")
    blocks = [("C1 physics: theory / experiment", "C1_theory_vs_experiment", "C1_physics_theory_vs_experiment", "C1__"),
              ("C2 biology: computational / wet lab", "C2_computational_vs_wet_lab",
               "C2_biology_computational_vs_wetlab", "C2__"),
              ("C3 medicine: public dataset / other", "C3_public_dataset_vs_other",
               "C3_medicine_public_dataset_vs_rest", None)]
    rows = []  # (label, kind, value, block index)
    for b, (title, pk, wk, loo) in enumerate(blocks):
        pl = r["planned"][pk]
        rows.append((title, "header", None, b))
        rows.append(("Planned: NB2, multi-year base", "primary", pl["planned_2026"], b))
        rows.append(("Planned, group-specific trends", "point", pl["with_group_trends"]["2026"], b))
        rows.append(("Planned, block bootstrap", "point", pl["block_bootstrap_2026"], b))
        rows.append(("First reported: base 2022", "point", w["confirmatory"][wk]["event_study"]["2026"], b))
        rows.append(("First reported, January–August", "hollow", w8["confirmatory"][wk]["event_study"]["2026"], b))
        if loo:
            vals = [v["rr"] for k, v in w["leave_one_out"].items() if k.startswith(loo)]
            rows.append(("Leave one category out: range", "range", (min(vals), max(vals)), b))
        if pk.startswith("C1"):
            g = r["planned"]["C1_theory_without_gr-qc_vs_experiment"]
            rows.append(("Without gr-qc: planned", "point", g["planned_2026"], b))
            rows.append(("Without gr-qc: first reported", "point", g["as_run_2022_base_2026"], b))
        if pk.startswith("C2"):
            rows.append(("Without AI-topic papers: base 2022", "point",
                         r["c2_ai_split"]["contrasts"]["without_ai_topic_papers"]["2022"]["2026"], b))
    n = len(rows)
    fig, ax = plt.subplots(figsize=(WIDTH, 0.17 * n + 1.25))
    fig.subplots_adjust(left=0.30, right=0.80, top=0.99, bottom=0.165)
    y = {i: n - 1 - i for i in range(n)}
    # shade 1 to the planned minimum detectable rate ratio (80% power), over each block's rows
    for b, (_, pk, _, _) in enumerate(blocks):
        ys = [y[i] for i, row in enumerate(rows) if row[3] == b and row[1] != "header"]
        ax.fill_betweenx([min(ys) - 0.45, max(ys) + 0.45], 1, 1 + r["planned"][pk]["mde_2026_80pct_power"],
                         color=SHADE, linewidth=0, zorder=0)
    labels = []
    for i, (label, kind, v, b) in enumerate(rows):
        yy = y[i]
        labels.append(label)
        if kind == "header":
            continue
        if kind == "range":
            ax.plot([v[0], v[1]], [yy, yy], color=GREY, linewidth=4, solid_capstyle="butt", zorder=2)
            txt = f"{v[0]:.2f} to {v[1]:.2f}"
        else:
            color = PRIMARY if kind == "primary" else INK2
            ax.plot([v["lo"], v["hi"]], [yy, yy], color=color, linewidth=1.6 if kind == "primary" else 1.0, zorder=3)
            ax.plot(v["rr"], yy, marker="o", markersize=5.5 if kind == "primary" else 4.5,
                    markerfacecolor="white" if kind == "hollow" else color, markeredgecolor=color,
                    markeredgewidth=1.0, linestyle="none", zorder=4)
            txt = ci_text(v)
        ax.text(1.02, yy, txt, transform=ax.get_yaxis_transform(), va="center", ha="left", fontsize=8,
                color=INK, weight="bold" if kind == "primary" else "normal")
    ax.set_yticks([y[i] for i in range(n)])
    ax.set_yticklabels(labels)
    for i, t in enumerate(ax.get_yticklabels()):
        if rows[i][1] == "header":
            t.set_weight("bold")
        elif rows[i][1] == "primary":
            t.set_weight("bold")
            t.set_color(INK)
        else:
            t.set_color(INK2)
    ax.set_ylim(-0.8, n - 0.4)
    log_axis(ax, 0.62, 1.95, [0.7, 0.8, 0.9, 1, 1.1, 1.25, 1.5, 1.75])
    ax.set_xlabel("Rate ratio of the non-experimental to the experimental group, 2026 (log scale)", color=INK2)
    ax.text(1.02, y[0], "Rate ratio (95% CI)", transform=ax.get_yaxis_transform(), va="center", ha="left",
            fontsize=8, color=INK2)
    ax.legend(handles=[Line2D([], [], marker="o", color=PRIMARY, markersize=5.5, linewidth=1.6,
                              label="Planned specification (primary)"),
                       Line2D([], [], marker="o", color=INK2, markersize=4.5, linewidth=1.0,
                              label="Other specifications"),
                       Line2D([], [], marker="o", color=INK2, markerfacecolor="white", markersize=4.5, linewidth=1.0,
                              label="January–August 2026"),
                       Patch(facecolor=SHADE, edgecolor="none",
                             label="1 to the minimum detectable rate ratio (planned, 80% power)")],
              loc="upper center", bbox_to_anchor=(0.45, -0.07), ncol=2, frameon=False, fontsize=8,
              handlelength=1.6, columnspacing=1.5)
    save(fig, out, "Fig4_forest")


def fig6_departures(repo, out):
    f = load(repo, "field_tests.json")
    names = {"math": "math (mathematics)", "cs": "cs (computer science)", "physics": "physics (archive)"}
    series = [(names.get(a, a), v, "archive") for a, v in f["archives"].items()]
    series += [("Physics, 13 archives", f["fields"]["physics"], "field"),
               ("bioRxiv (biology)", f["fields"]["biology_biorxiv_from2018"], "field"),
               ("PubMed (biomedicine, quarterly)", f["fields"]["biomedicine_pubmed_quarterly"], "field"),
               ("medRxiv (medicine; not interpreted)", f["fields"]["medicine_medrxiv_excl_covid_from2019_unreliable"],
                "grey")]
    series.sort(key=lambda s: s[1]["2026"]["rr"])
    n = len(series)
    fig, ax = plt.subplots(figsize=(WIDTH, 0.165 * n + 1.25))
    fig.subplots_adjust(left=0.28, right=0.84, top=0.955, bottom=0.165)
    for i, (label, v, kind) in enumerate(series):
        grey = kind == "grey"
        for yr in ("2024", "2025"):
            ax.plot(v[yr]["rr"], i, marker="o", markersize=3.5, linestyle="none", zorder=3,
                    color=GREY if grey else YEARS[yr], markeredgewidth=0)
        d = v["2026"]
        c = GREY if grey else YEARS["2026"]
        ax.plot([d["lo"], d["hi"]], [i, i], color=c, linewidth=1.0, zorder=3)
        ax.plot(d["rr"], i, marker="D" if kind == "field" else "o", markersize=4.8, linestyle="none", color=c,
                markeredgecolor="white", markeredgewidth=0.6, zorder=4)
        ax.text(1.02, i, f"{d['rr']:.2f}", transform=ax.get_yaxis_transform(), va="center", ha="left", fontsize=8,
                color=MUTED if grey else INK)
        ax.text(1.10, i, f"{100 * v['trend_per_year']:+.1f}%".replace("-", "\u2212"), transform=ax.get_yaxis_transform(), va="center",
                ha="left", fontsize=8, color=MUTED if grey else INK2)
    ax.set_yticks(range(n))
    ax.set_yticklabels([s[0] for s in series])
    for t, s in zip(ax.get_yticklabels(), series):
        t.set_weight("bold" if s[2] == "field" else "normal")
        t.set_color(MUTED if s[2] == "grey" else INK)
    ax.set_ylim(-0.7, n - 0.3)
    log_axis(ax, 0.27, 2.3, [0.3, 0.4, 0.5, 0.7, 1, 1.25, 1.5, 2])
    ax.set_xlabel("Observed / expected from the pre-2023 trend (log scale)", color=INK2)
    ax.text(1.02, n - 0.3, "2026", transform=ax.get_yaxis_transform(), va="bottom", ha="left", fontsize=8,
            color=INK2)
    ax.text(1.10, n - 0.3, "Trend/yr", transform=ax.get_yaxis_transform(), va="bottom", ha="left",
            fontsize=8, color=INK2)
    handles = [Line2D([], [], marker="o", linestyle="none", color=YEARS["2024"], markersize=3.5, label="2024"),
               Line2D([], [], marker="o", linestyle="none", color=YEARS["2025"], markersize=3.5, label="2025"),
               Line2D([], [], marker="o", color=YEARS["2026"], markersize=4.8, linewidth=1.0,
                      label="2026, January–September (95% CI)"),
               Line2D([], [], marker="D", linestyle="none", color=YEARS["2026"], markersize=4.8,
                      label="Series other than single arXiv archives")]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.45, -0.075), ncol=2, frameon=False, fontsize=8,
              handletextpad=0.4, columnspacing=1.5)
    save(fig, out, "Fig6_departures")


def fig7_h2_ranking(repo, out):
    h = load(repo, "h2_round2.json")
    classes = [("top1pct", "Previous\ntop 1%"), ("next9pct", "Next\n9%"), ("bottom90pct", "Bottom\n90%"),
               ("not_active_in_ranking_window", "Not\nactive")]
    pre = ["2020-Q3_to_2021-Q3", "2021-Q3_to_2022-Q3"]
    fig = plt.figure(figsize=(WIDTH, 8.4 * CM))
    gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 0.72], wspace=0.40, left=0.075, right=0.975, top=0.78,
                          bottom=0.15)
    groups = [("maths", "A  Mathematics"), ("theory_max50_authors", "B  Physics theory (≤50 authors)")]
    for k, (g, title) in enumerate(groups):
        ax = fig.add_subplot(gs[0, k])
        iw = h[g]["all_names"]["independent_window"]
        xs = range(len(classes))
        for j, pair in enumerate(pre):
            d = iw[pair]
            ax.plot([x + 0.12 * (j - 0.5) for x in xs], [100 * d[c]["growth"] for c, _ in classes], marker="o",
                    markersize=3.5, linestyle="none", color=GREY, zorder=2)
            ax.axhline(100 * d["growth"], color=GREY, linewidth=0.7, linestyle=(0, (3, 2)), zorder=1)
        d = iw["2025-Q3_to_2026-Q3"]
        ax.axhline(100 * d["growth"], color=PRIMARY, linewidth=1.0, zorder=1)
        ax.plot(list(xs), [100 * d[c]["growth"] for c, _ in classes], marker="o", markersize=5.5, linestyle="none",
                color=PRIMARY, zorder=3)
        for x, (c, _) in zip(xs, classes):
            v = 100 * d[c]["growth"]
            below = abs(v + 9 - 100 * d["growth"]) < 9
            ax.text(x, v - 7 if below else v + 6, f"{v:+.0f}%".replace("-", "\u2212"), ha="center",
                    va="top" if below else "bottom", fontsize=8, color=INK)
        ax.text(len(classes) - 0.4, 100 * d["growth"] + 2, f"All\nnames\n{100 * d['growth']:+.0f}%", ha="left",
                va="bottom", fontsize=8, color=INK2)
        ax.set_xticks(list(xs))
        ax.set_xticklabels([lab for _, lab in classes])
        ax.set_xlim(-0.5, len(classes) + 0.35)
        ax.set_ylim(-30, 125)
        ax.set_ylabel("Growth in fractional output, Q3 to Q3 (%)" if k == 0 else "")
        for side in ("top", "right", "left"):
            ax.spines[side].set_visible(False)
        ax.spines["bottom"].set_color(AXIS)
        ax.tick_params(axis="y", length=0, colors=INK2, pad=2)
        ax.tick_params(axis="x", length=0, colors=INK, pad=3)
        ax.grid(axis="y", color=GRID, linewidth=0.5)
        ax.set_axisbelow(True)
        ax.axhline(0, color=AXIS, linewidth=0.6)
        ax.set_title(title, loc="left", fontsize=9, weight="bold", pad=8)
    ax = fig.add_subplot(gs[0, 2])
    xs = [0, 1.25]
    for x, (g, lab) in zip(xs, (("maths", "Mathematics"), ("theory_max50_authors", "Physics\ntheory"))):
        u = h[g]["all_names"]["uniform_scaling"]["2025-Q3_to_2026-Q3"]
        obs, null = 100 * u["observed_change_top1"], u["lognormal"]["null_change_top1"]
        ax.bar(x, obs, width=0.55, color=PRIMARY, zorder=2)
        m, sd = 100 * null["mean"], 100 * null["sd"]
        ax.plot([x, x], [m - sd, m + sd], color=INK, linewidth=1.0, zorder=4)
        ax.plot(x, m, marker="_", markersize=14, markeredgewidth=1.6, color=INK, zorder=4)
        ax.text(x, obs + 0.06, f"{obs:.2f}", ha="center", va="bottom", fontsize=8, color=INK)
        ax.text(x + 0.33, m, f"{m:.2f}", ha="left", va="center", fontsize=8, color=INK2)
    ax.set_xticks(xs)
    ax.set_xticklabels(["Mathe-\nmatics", "Physics\ntheory"])
    ax.set_xlim(-0.5, 2.0)
    ax.set_ylim(0, 2.0)
    ax.set_ylabel("Rise in the top-1% share (pp)")
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(AXIS)
    ax.tick_params(axis="y", length=0, colors=INK2, pad=2)
    ax.tick_params(axis="x", length=0, colors=INK, pad=3)
    ax.grid(axis="y", color=GRID, linewidth=0.5)
    ax.set_axisbelow(True)
    ax.set_title("C  Uniform scaling", loc="left", fontsize=9, weight="bold", pad=8)
    handles = [Line2D([], [], marker="o", linestyle="none", color=PRIMARY, markersize=5.5,
                      label="Q3 2025 to Q3 2026; line: all names"),
               Line2D([], [], marker="o", linestyle=(0, (3, 2)), color=GREY, markersize=3.5, linewidth=0.7,
                      label="Pairs before ChatGPT (2020–21, 2021–22)"),
               Patch(facecolor=PRIMARY, label="Observed rise"),
               Line2D([], [], marker="_", color=INK, markersize=10, markeredgewidth=1.6, linewidth=1.0,
                      label="Uniform scaling: mean ± SD (100 runs)")]
    fig.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, 1.0), ncol=2, frameon=False, fontsize=8,
               handletextpad=0.4, columnspacing=2.0)
    save(fig, out, "Fig7_h2_ranking")


def fig8_inspire(repo, out):
    c = load(repo, "round1_tests.json")["inspire_round2"]["contrasts"]
    scopes = [("all_six", "INSPIRE's six archives"), ("hep-ex", "hep-ex"), ("nucl-ex", "nucl-ex"),
              ("hep-ex+nucl-ex", "hep-ex + nucl-ex")]
    bases = [("2022", "Base 2022"), ("2017-2019", "Base 2017–2019"), ("2017-2019+2022", "Base 2017–2019 + 2022"),
             ("2017-2022", "Base 2017–2022")]
    rows = []
    for sc, title in scopes:
        rows.append((title, None, None))
        for b, lab in bases:
            rows.append((lab, c[f"{sc}|research_articles_without_planning|ND"].get(b),
                         c[f"{sc}|as_harvested|ND"].get(b)))
    n = len(rows)
    fig, ax = plt.subplots(figsize=(WIDTH, 0.19 * n + 1.2))
    fig.subplots_adjust(left=0.22, right=0.80, top=0.99, bottom=0.17)
    labels = []
    for i, (lab, main, allrec) in enumerate(rows):
        y = n - 1 - i
        labels.append(lab)
        if main is None:
            continue
        for v, off, filled in ((main["2026"], 0.12, True), (allrec["2026"], -0.12, False)):
            col = PRIMARY if filled else INK2
            ax.plot([v["lo"], v["hi"]], [y + off, y + off], color=col, linewidth=1.3 if filled else 0.9, zorder=3)
            ax.plot(v["rr"], y + off, marker="o", markersize=5 if filled else 4.2, linestyle="none", color=col,
                    markerfacecolor=col if filled else "white", markeredgewidth=1.0, zorder=4)
        ax.text(1.02, y, ci_text(main["2026"]), transform=ax.get_yaxis_transform(), va="center", ha="left",
                fontsize=8, color=INK)
    ax.set_yticks([n - 1 - i for i in range(n)])
    ax.set_yticklabels(labels)
    for t, row in zip(ax.get_yticklabels(), rows):
        t.set_weight("bold" if row[1] is None else "normal")
        t.set_color(INK if row[1] is None else INK2)
    ax.set_ylim(-0.7, n - 0.4)
    log_axis(ax, 0.45, 6.5, [0.5, 0.75, 1, 1.5, 2, 3, 4, 6])
    ax.set_xlabel("Rate ratio, papers without to papers with new experimental results, 2026 (log scale)",
                  color=INK2)
    ax.text(1.02, n - 1, "Research articles\n(95% CI)", transform=ax.get_yaxis_transform(), va="center",
            ha="left", fontsize=8, color=INK2)
    handles = [Line2D([], [], marker="o", color=PRIMARY, markersize=5, linewidth=1.3,
                      label="Research articles, planning papers removed"),
               Line2D([], [], marker="o", color=INK2, markerfacecolor="white", markersize=4.2, linewidth=0.9,
                      label="All record types, as harvested")]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.4, -0.085), ncol=2, frameon=False, fontsize=8,
              handletextpad=0.4, columnspacing=1.5)
    save(fig, out, "Fig8_inspire")


FIGURES = {"fig4": fig4_forest, "fig6": fig6_departures, "fig7": fig7_h2_ranking, "fig8": fig8_inspire}


def main(args):
    repo = args[0] if args else "."
    setup()
    out = os.path.join(repo, "docs/figures/plos")
    for name in (args[1:] or FIGURES):
        FIGURES[name](repo, out)
        print("written", name)


if __name__ == "__main__":
    main(sys.argv[1:])
