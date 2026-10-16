"""Charts of the within-field contrasts (analyze_within_field.py).

Static (docs/figures/): fig8_within_field_contrasts.png and fig9_medrxiv_categories.png.
Publication (docs/figures/paper/): fig8_within_field_{85,175}mm.{svg,pdf,png}, in the style of plot_paper.py.
Usage: python3 scripts/plot_within_field.py [repo_dir]   (needs matplotlib)
"""
import csv
import datetime as dt
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import plot_paper as pp  # noqa: E402
import plot_static as ps  # noqa: E402
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.lines  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.ticker as mticker  # noqa: E402

BIO = [("biorxiv_computational", "Computational", "#2a78d6", pp.OI["blue"]),
       ("biorxiv_mixed", "Mixed", "#898781", pp.OI["grey"]),
       ("biorxiv_wet_lab", "Wet lab", "#1baf7a", pp.OI["green"])]
PHYS = [("arxiv_theory", "Theory", "#e87ba4", pp.OI["purple"]),
        ("arxiv_experiment", "Experiment", "#1baf7a", pp.OI["green"])]
BIO_NOTE = ("Computational: bioinformatics, systems biology, genomics. Wet lab: biochemistry, cell, developmental,\n"
            "molecular, plant and cancer biology, microbiology, immunology, physiology, pharmacology, pathology,\n"
            "synthetic biology. Mixed: the rest (neuroscience is the largest). COVID-19 preprints included.")
PHYS_NOTE = "Theory: hep-th, hep-ph, gr-qc, nucl-th. Experiment: hep-ex, nucl-ex."


def load(repo):
    s = defaultdict(dict)
    for r in csv.DictReader(open(os.path.join(repo, "data/processed/within_field_quarterly.csv"))):
        s[r["series"]][r["quarter"]] = r
    return s


def xq(q):
    return dt.date(int(q[:4]), 3 * (int(q[-1]) - 1) + 2, 15)


def q123(rows, year):
    return sum(int(rows[f"{year}-Q{i}"]["papers"]) for i in (1, 2, 3) if f"{year}-Q{i}" in rows)


def index_panel(ax, s, groups, colour_pos, label_size, end_labels=True, events=None, event_size=6):
    qs = [q for q in sorted(s[groups[0][0]]) if q >= "2020-Q1"]
    x = [xq(q) for q in qs]
    ends = []
    for key, name, *colours in groups:
        ys = [float(s[key][q]["index_2022"]) for q in qs]
        ax.plot(x, ys, color=colours[colour_pos], linewidth=1.8 if colour_pos == 0 else 1.2, zorder=3,
                solid_capstyle="round")
        ax.plot(x[-1], ys[-1], "o", color=colours[colour_pos], markersize=4 if colour_pos == 0 else 2.5, zorder=4)
        ends.append((name, colours[colour_pos], ys[-1]))
    return x, ends


def static_fig(repo, s, out):
    fig, axes = plt.subplots(2, 2, figsize=(13, 8.6), dpi=150, gridspec_kw={"height_ratios": [1.25, 1]})
    fig.patch.set_facecolor(ps.SURFACE)
    for col, (groups, title, note, years) in enumerate([
            (BIO, "Biology (bioRxiv): index, 2022 = 100", BIO_NOTE, range(2020, 2027)),
            (PHYS, "Physics (arXiv): index, 2022 = 100", PHYS_NOTE, range(2016, 2027))]):
        ax = axes[0][col]
        ps.style(ax)
        ax.axhline(100, color=ps.AXIS, linewidth=1, zorder=1)
        x, ends = index_panel(ax, s, groups, 0, 9)
        top = max(max(float(s[g[0]][q]["index_2022"]) for q in s[g[0]] if q >= "2020-Q1") for g in groups)
        low = min(min(float(s[g[0]][q]["index_2022"]) for q in s[g[0]] if q >= "2020-Q1") for g in groups)
        ax.set_ylim(min(60, low * 0.95), top * 1.12)
        ax.set_xlim(dt.date(2020, 1, 1), dt.date(2028, 1, 1))
        ps.year_axis(ax, 2020, 2026)
        ax.spines["bottom"].set_bounds(mdates.date2num(dt.date(2020, 1, 1)), mdates.date2num(dt.date(2026, 10, 1)))
        labels = ps.spread([e[2] for e in ends], (top * 1.12 - 60) * 0.06)
        for (name, c, y_end), y_lab in zip(ends, labels):
            ax.plot([x[-1] + dt.timedelta(days=8), x[-1] + dt.timedelta(days=54)], [y_end, y_lab], color=ps.AXIS,
                    linewidth=0.8)
            ax.text(x[-1] + dt.timedelta(days=60), y_lab, f"{name}  {y_end:.0f}", fontsize=9, color=ps.INK,
                    va="center")
        ax.set_title(title, loc="left", fontsize=11, color=ps.INK, pad=66)
        ps.events(ax, top * 1.12, ps.EVENTS)

        ax = axes[1][col]
        ps.style(ax)
        ax.axhline(0, color=ps.AXIS, linewidth=1, zorder=1)
        yrs = [y for y in years if all(q123(s[g[0]], y - 1) for g in groups)]
        w = 0.8 / len(groups)
        for k, (key, name, colour, _) in enumerate(groups):
            g = [q123(s[key], y) / q123(s[key], y - 1) - 1 for y in yrs]
            ax.bar([y + (k - (len(groups) - 1) / 2) * w for y in yrs], g, width=w * 0.92, color=colour, zorder=2,
                   label=name)
        ax.set_xticks(list(yrs))
        ax.set_xticklabels([("2026*" if y == 2026 else str(y)) for y in yrs])
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda t, _: "0%" if abs(t) < 1e-9 else f"{t:+.0%}"))
        ax.set_ylim(ax.get_ylim()[0], ax.get_ylim()[1] * 1.22)
        ax.legend(frameon=False, fontsize=8.5, loc="upper center", ncol=len(groups), labelcolor=ps.INK2)
        ax.set_title("Growth, January–September vs the same months a year earlier", loc="left", fontsize=10,
                     color=ps.INK, pad=8)
        fig.text(0.05 + 0.5 * col, 0.075, note, fontsize=7.5, color=ps.INK2, va="bottom", linespacing=1.4)
    fig.subplots_adjust(left=0.05, right=0.98, top=0.76, bottom=0.18, hspace=0.42, wspace=0.16)
    ps.header(fig, "Within-field contrasts: computational vs wet-lab biology, theory vs experiment in physics",
              "Does the 2025–2026 acceleration reach work that is bottlenecked by experiments?")
    fig.text(0.05, 0.03, "*2026: January–September. Sources: bioRxiv API (version-1 preprints by subject category); "
             "arXiv yearly statistics by primary archive.", fontsize=7.5, color=ps.MUTED)
    fig.text(0.05, 0.012, ps.ADVISORY, fontsize=7.5, color=ps.MUTED)
    fig.savefig(os.path.join(out, "fig8_within_field_contrasts.png"), facecolor=ps.SURFACE)
    plt.close(fig)


def medrxiv_fig(repo, out):
    rows = list(csv.DictReader(open(os.path.join(repo, "data/processed/medrxiv_categories_growth.csv"))))
    rows = [r for r in rows if int(r["papers_q1q3_2025"]) >= 150]
    rows.sort(key=lambda r: float(r["growth_q1q3_2026"]))
    pub = list(csv.DictReader(open(os.path.join(repo, "data/processed/medrxiv_public_dataset_quarterly.csv"))))
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 7.4), dpi=150, gridspec_kw={"width_ratios": [1.25, 1]})
    fig.patch.set_facecolor(ps.SURFACE)
    ps.style(ax1, grid_axis="x")
    ax1.spines["bottom"].set_visible(False)
    ax1.axvline(0, color=ps.AXIS, linewidth=1)
    for i, r in enumerate(rows):
        g25, g26 = float(r["growth_q1q3_2025"]), float(r["growth_q1q3_2026"])
        ax1.plot([g25, g26], [i, i], color="#eda100", linewidth=1.5, alpha=0.5, zorder=2)
        ax1.plot(g25, i, "o", color=ps.SURFACE, markeredgecolor="#eda100", markeredgewidth=1.5, markersize=6, zorder=3)
        ax1.plot(g26, i, "o", color="#eda100", markersize=7.5, zorder=4)
        ax1.text(ax1.get_xlim()[0], i, r["category"].capitalize(), fontsize=8, ha="right", va="center", color=ps.INK)
    ax1.set_yticks([])
    ax1.xaxis.set_major_formatter(mticker.FuncFormatter(lambda t, _: "0%" if abs(t) < 1e-9 else f"{t:+.0%}"))
    ax1.xaxis.set_ticks_position("top")
    ax1.set_title("Growth by subject, Jan–Sep 2026 (filled) and 2025 (open)", loc="left", fontsize=10.5,
                  color=ps.INK, pad=26)
    ps.style(ax2)
    pub = [r for r in pub if r["quarter"] >= "2020-Q1"]
    x = [xq(r["quarter"]) for r in pub]
    ax2.plot(x, [float(r["public_dataset_share"]) for r in pub], color="#eda100", linewidth=2)
    ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda t, _: f"{t:.0%}"))
    ax2.set_ylim(0, None)
    ax2.set_xlim(dt.date(2020, 1, 1), dt.date(2026, 11, 1))
    ps.year_axis(ax2, 2020, 2026)
    ax2.set_title("Share naming a public dataset (non-COVID preprints)", loc="left", fontsize=10.5, color=ps.INK,
                  pad=34)
    ax2.text(0, 1.02, "NHANES, UK Biobank, GBD, Mendelian randomisation,\nFAERS, MIMIC, SEER or BRFSS in title or abstract",
             transform=ax2.transAxes, fontsize=8, color=ps.INK2, va="bottom")
    fig.subplots_adjust(left=0.27, right=0.98, top=0.82, bottom=0.08, wspace=0.18)
    ps.header(fig, "Where medRxiv growth sits", "New preprints excluding COVID-19; subjects with at least 150 "
              "preprints in January–September 2025.")
    fig.text(0.05, 0.02, "Source: bioRxiv API (medRxiv version-1 preprints by subject category; keyword matches on "
             "title and abstract).", fontsize=7.5, color=ps.MUTED)
    fig.savefig(os.path.join(out, "fig9_medrxiv_categories.png"), facecolor=ps.SURFACE)
    plt.close(fig)


def paper_fig(repo, s, out, width_mm):
    narrow = width_mm < 120
    pp.setup(6.5 if narrow else 7)
    fig, axes = plt.subplots(2 if narrow else 1, 1 if narrow else 2,
                             figsize=(width_mm * pp.MM, (120 if narrow else 72) * pp.MM))
    for ax, groups, tag in zip(axes, [BIO, PHYS], ["a", "b"]):
        pp.style(ax)
        ax.axhline(100, color=pp.AXIS, linewidth=0.6, zorder=1)
        x, ends = index_panel(ax, s, groups, 1, 6)
        vals = [float(s[g[0]][q]["index_2022"]) for g in groups for q in s[g[0]] if q >= "2020-Q1"]
        ax.set_ylim(min(60, min(vals) * 0.95), max(vals) * 1.08)
        ax.set_xlim(dt.date(2020, 1, 1), dt.date(2026, 12, 1))
        pp.year_ticks(ax, 2020, 2026, every=2 if narrow else 1)
        ax.spines["bottom"].set_bounds(mdates.date2num(dt.date(2020, 1, 1)), mdates.date2num(dt.date(2026, 10, 15)))
        ax.set_ylabel("Index (2022 = 100)")
        handles = [matplotlib.lines.Line2D([], [], color=c, linewidth=1.2, marker="o", markersize=2.5)
                   for _, c, _ in ends]
        ax.legend(handles, [f"{n} ({y:.0f})" for n, _, y in ends], loc="upper left", frameon=False,
                  fontsize=plt.rcParams["font.size"] - 0.5, handlelength=1.6)
        ax.text(-0.12 if narrow else -0.13, 1.0, tag, transform=ax.transAxes, fontsize=8, weight="bold", va="bottom")
    fig.subplots_adjust(left=0.13 if narrow else 0.07, right=0.97 if narrow else 0.99, top=0.9 if narrow else 0.82,
                        bottom=0.07 if narrow else 0.1, hspace=0.45, wspace=0.22)
    for ax in axes:
        pp.events(ax, pp.FIELD_EVENTS, fontsize=5.5 if narrow else 6)
    pp.save(fig, out, f"fig8_within_field_{width_mm}mm")


def main(repo):
    s = load(repo)
    plt.rcParams.update({"font.family": "DejaVu Sans", "text.color": ps.INK, "axes.labelcolor": ps.INK2})
    static_fig(repo, s, os.path.join(repo, "docs/figures"))
    medrxiv_fig(repo, os.path.join(repo, "docs/figures"))
    for w in (85, 175):
        paper_fig(repo, s, os.path.join(repo, "docs/figures/paper"), w)
    print("written fig8 (static and paper) and fig9")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
