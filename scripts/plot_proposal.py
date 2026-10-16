"""Prototype charts for the chart-improvement proposal (docs/propuesta-graficos.md).

Reads data/processed/excess_over_trend_quarterly.csv and arxiv_archive_growth.csv (analyze_trends.py).
Writes PNGs to docs/figures/proposal/.  Usage: python3 scripts/plot_proposal.py [repo_dir]   (needs matplotlib)
"""
import csv
import datetime as dt
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plot_static import (AXIS, EVENTS, GRID, INK, INK2, MUTED, SURFACE, events, header, mid, plt,  # noqa: E402
                         style)
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.ticker as mticker  # noqa: E402

FIELDS = [("physics", "Physics", "#2a78d6"), ("mathematics", "Mathematics", "#eb6834"),
          ("computer_science", "Computer science", "#6250d6")]
MAIN, ALT = "2015-2022", ["2015-2019", "2018-2022"]
ARCHIVE_NAMES = {
    "math": "Mathematics", "math-ph": "Mathematical physics", "hep-th": "High-energy theory",
    "gr-qc": "General relativity", "hep-ph": "High-energy phenomenology", "nucl-th": "Nuclear theory",
    "hep-ex": "High-energy experiment", "nucl-ex": "Nuclear experiment", "quant-ph": "Quantum physics",
    "stat": "Statistics", "cs": "Computer science", "econ": "Economics", "nlin": "Nonlinear sciences",
    "cond-mat": "Condensed matter", "astro-ph": "Astrophysics", "physics": "Physics (other)",
    "q-fin": "Quantitative finance", "hep-lat": "Lattice field theory", "eess": "Electrical engineering",
    "q-bio": "Quantitative biology",
}
THEORY = {"math", "math-ph", "hep-th", "gr-qc", "hep-ph", "nucl-th"}
EXPERIMENT = {"hep-ex", "nucl-ex"}
TEAL, PINK = "#1baf7a", "#e87ba4"


def load(repo):
    rows = list(csv.DictReader(open(os.path.join(repo, "data/processed/excess_over_trend_quarterly.csv"))))
    data = {}
    for r in rows:
        data.setdefault((r["field"], r["baseline"]), []).append(r)
    growth = list(csv.DictReader(open(os.path.join(repo, "data/processed/arxiv_archive_growth.csv"))))
    return data, growth


def trend_panels(data, out):
    fig, axes = plt.subplots(1, 3, figsize=(13, 5.6), dpi=150)
    fig.patch.set_facecolor(SURFACE)
    for ax, (key, name, color) in zip(axes, FIELDS):
        style(ax)
        main = data[(key, MAIN)]
        x = [mid(r["quarter"]) for r in main]
        obs = [float(r["observed"]) for r in main]
        exp = [float(r["expected"]) for r in main]
        post = [i for i, r in enumerate(main) if r["quarter"] >= "2023-Q1"]
        ax.fill_between([x[i] for i in post], [float(main[i]["expected_lo"]) for i in post],
                        [float(main[i]["expected_hi"]) for i in post], color=GRID, linewidth=0, zorder=1)
        for b, ls in zip(ALT, [(0, (1, 2)), (0, (1, 2))]):
            alt = data[(key, b)]
            ax.plot(x, [float(r["expected"]) for r in alt], color=MUTED, linewidth=1, linestyle=ls, zorder=2)
            ax.text(x[-1] + dt.timedelta(days=40), float(alt[-1]["expected"]), f"{b[:4]}–{b[7:]}", fontsize=7.5,
                    color=MUTED, va="center")
        ax.plot(x, exp, color=INK2, linewidth=1.2, linestyle=(0, (4, 3)), zorder=3)
        ax.text(x[-1] + dt.timedelta(days=40), exp[-1], f"{MAIN[:4]}–{MAIN[7:]}", fontsize=7.5, color=INK2,
                va="center")
        ax.plot(x, obs, color=color, linewidth=2, zorder=4, solid_capstyle="round")
        ax.plot(x[-1], obs[-1], "o", color=color, markersize=5, markeredgecolor=SURFACE, markeredgewidth=1.5, zorder=5)
        ax.set_yscale("log")
        ax.yaxis.set_major_locator(mticker.LogLocator(base=10, subs=(1, 2, 5)))
        ax.yaxis.set_minor_locator(mticker.NullLocator())
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda t, _: f"{t / 1000:g}k" if t >= 1000 else f"{t:g}"))
        ax.set_xlim(dt.date(2015, 1, 1), dt.date(2028, 6, 1))
        ax.set_xticks([dt.date(y, 1, 1) for y in (2015, 2018, 2021, 2024, 2027)])
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
        ax.spines["bottom"].set_bounds(mdates.date2num(dt.date(2015, 1, 1)), mdates.date2num(dt.date(2026, 10, 1)))
        e = {b: float(data[(key, b)][-1]["excess"]) for b in [MAIN] + ALT}
        lo, hi = float(main[-1]["excess_lo"]), float(main[-1]["excess_hi"])
        ax.set_title(name, loc="left", fontsize=11, color=INK, pad=30)
        ax.text(0, 1.03, f"Q3 2026: {e[MAIN]:+.0%} vs trend (95% PI {lo:+.0%} to {hi:+.0%})\n"
                f"other baselines: {min(e[b] for b in ALT):+.0%} to {max(e[b] for b in ALT):+.0%}",
                transform=ax.transAxes, fontsize=8.5, color=INK2, va="bottom")
    fig.subplots_adjust(left=0.05, right=0.97, top=0.70, bottom=0.12, wspace=0.22)
    fig.text(0.05, 0.95, "New arXiv papers per quarter against each field's own pre-ChatGPT trend", fontsize=14,
             color=INK, ha="left", weight="bold")
    fig.text(0.05, 0.915, "Log scale. Dashed: log-linear trend with quarterly seasonality fitted on 2015–2022, COVID "
             "quarters 2020-Q2 to 2021-Q1 left out (band: 95% prediction interval).\nDotted: the same trend fitted on "
             "2015–2019 and on 2018–2022.", fontsize=10, color=INK2, ha="left", va="top", linespacing=1.5)
    fig.text(0.05, 0.02, "Source: arXiv yearly statistics by primary archive (new submissions), Q1 2015 – Q3 2026. "
             "Prototype for the chart proposal.", fontsize=7.5, color=MUTED)
    fig.savefig(os.path.join(out, "p1_trend_by_field.png"), facecolor=SURFACE)
    plt.close(fig)


def pscore_chart(data, out):
    fig, ax = plt.subplots(figsize=(10, 6), dpi=160)
    fig.patch.set_facecolor(SURFACE)
    style(ax)
    ax.axhline(0, color=AXIS, linewidth=1, zorder=1)
    ends = []
    for key, name, color in FIELDS:
        rows = [r for r in data[(key, MAIN)] if r["quarter"] >= "2021-Q2"]
        x = [mid(r["quarter"]) for r in rows]
        ax.fill_between(x, [float(r["excess_lo"]) for r in rows], [float(r["excess_hi"]) for r in rows],
                        color=color, alpha=0.12, linewidth=0, zorder=2)
        ys = [float(r["excess"]) for r in rows]
        ax.plot(x, ys, color=color, linewidth=2, zorder=3, solid_capstyle="round")
        ax.plot(x[-1], ys[-1], "o", color=color, markersize=5, markeredgecolor=SURFACE, markeredgewidth=1.5, zorder=4)
        ends.append((name, ys[-1], x[-1]))
    for name, y, x in ends:
        ax.text(x + dt.timedelta(days=50), y, f"{name}  {y:+.0%}", fontsize=9, color=INK, va="center")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda t, _: "0%" if abs(t) < 1e-9 else f"{t:+.0%}"))
    ax.set_ylim(-0.3, 1.15)
    ax.set_xlim(dt.date(2021, 4, 1), dt.date(2028, 3, 1))
    ax.set_xticks([dt.date(y, 7, 1) for y in range(2021, 2027)])
    ax.set_xticklabels([str(y) for y in range(2021, 2027)])
    ax.spines["bottom"].set_bounds(mdates.date2num(dt.date(2021, 4, 1)), mdates.date2num(dt.date(2026, 10, 1)))
    fig.subplots_adjust(left=0.08, right=0.98, top=0.76, bottom=0.12)
    events(ax, 1.15, EVENTS)
    header(fig, "Excess new arXiv papers over each field's pre-ChatGPT trend",
           "Observed / expected − 1. Trend fitted on 2015–2022 (COVID quarters left out); bands = 95% prediction intervals.")
    fig.text(0.05, 0.045, "Computer science depends on the baseline (Q3 2026: −29% with a 2015–2019 trend, +48% with "
             "2018–2022); physics and mathematics stay above trend under all three.", fontsize=8, color=INK2)
    fig.text(0.05, 0.02, "Source: arXiv yearly statistics by primary archive (new submissions). Prototype for the chart "
             "proposal.", fontsize=7.5, color=MUTED)
    fig.savefig(os.path.join(out, "p2_excess_over_trend.png"), facecolor=SURFACE)
    plt.close(fig)


def archive_chart(growth, out):
    rows = sorted(growth, key=lambda r: float(r["growth_q1q3_2026"]))
    fig, ax = plt.subplots(figsize=(10, 8), dpi=150)
    fig.patch.set_facecolor(SURFACE)
    style(ax, grid_axis="x")
    ax.spines["bottom"].set_visible(False)
    ax.axvline(0, color=AXIS, linewidth=1, zorder=1)
    for i, r in enumerate(rows):
        a = r["archive"]
        color = PINK if a in THEORY else TEAL if a in EXPERIMENT else MUTED
        g17, g25, g26 = (float(r[k]) for k in ("cagr_2017_2022", "growth_q1q3_2025", "growth_q1q3_2026"))
        ax.plot([g25, g26], [i, i], color=color, linewidth=1.5, alpha=0.5, zorder=2)
        ax.plot(g17, i, "|", color=INK, markersize=9, markeredgewidth=1.5, zorder=3)
        ax.plot(g25, i, "o", color=SURFACE, markeredgecolor=color, markeredgewidth=1.5, markersize=6, zorder=3)
        ax.plot(g26, i, "o", color=color, markeredgecolor=SURFACE, markeredgewidth=1, markersize=8, zorder=4)
        ax.text(-0.47, i, f"{ARCHIVE_NAMES.get(a, a)} ({a})", fontsize=8.5, color=INK, va="center", ha="right")
        ax.text(0.65, i, f"{int(r['papers_q1q3_2026']):,}", fontsize=7.5, color=MUTED, va="center", ha="right")
    ax.set_yticks([])
    ax.set_xlim(-0.45, 0.66)
    ax.set_xticks([-0.4, -0.2, 0, 0.2, 0.4])
    ax.set_ylim(-1, len(rows) + 0.5)
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda t, _: "0%" if abs(t) < 1e-9 else f"{t:+.0%}"))
    ax.xaxis.set_ticks_position("top")
    ax.text(0.65, len(rows) - 0.4, "papers\nQ1–Q3 2026", fontsize=7.5, color=MUTED, ha="right", va="bottom")
    fig.subplots_adjust(left=0.36, right=0.97, top=0.82, bottom=0.1)
    header(fig, "Growth of new arXiv papers by archive, Q1–Q3 2026 vs Q1–Q3 2025",
           "Filled dot: 2026 growth. Open dot: 2025 growth (Q1–Q3 vs Q1–Q3 2024). Black tick: compound annual growth "
           "2017–2022.", y=0.95)
    for k, (label, c) in enumerate([("Theory archives (pen and paper)", PINK), ("Experimental archives", TEAL),
                                    ("Other archives", MUTED)]):
        fig.text(0.05 + 0.3 * k, 0.865, "●", color=c, fontsize=11, va="center")
        fig.text(0.068 + 0.3 * k, 0.865, label, color=INK2, fontsize=8.5, va="center")
    fig.text(0.05, 0.045, "Economics and electrical engineering opened in 2017, so their 2017–2022 growth (+49% and +45% "
             "a year) reflects adoption.", fontsize=8, color=INK2)
    fig.text(0.05, 0.02, "Source: arXiv yearly statistics by primary archive (new submissions). The grouping is a "
             "hypothesis to test, not an official classification. Prototype for the chart proposal.",
             fontsize=7.5, color=MUTED)
    fig.savefig(os.path.join(out, "p3_growth_by_archive.png"), facecolor=SURFACE)
    plt.close(fig)


def annual_growth(repo):
    """Annual growth by field: full calendar years to 2025, then Q1-Q3 2026 vs Q1-Q3 2025."""
    from analyze_trends import PHYSICS  # noqa: E402
    import json
    totals = {"physics": {}, "mathematics": {}, "computer_science": {}, "biomedicine_pubmed": {}}
    part = {k: {} for k in totals}  # Q1-Q3 sums
    for r in csv.DictReader(open(os.path.join(repo, "data/raw/arxiv_archive_monthly.csv"))):
        a, y, m, n = r["archive"], int(r["year"]), int(r["month"]), int(r["new"])
        f = "physics" if a in PHYSICS else {"math": "mathematics", "cs": "computer_science"}.get(a)
        if not f or (y, m) > (2026, 9):
            continue
        totals[f][y] = totals[f].get(y, 0) + n
        if m <= 9:
            part[f][y] = part[f].get(y, 0) + n
    for r in json.load(open(os.path.join(repo, "data/raw/pubmed_edat_quarterly.json"))):
        y, q = int(r["quarter"][:4]), int(r["quarter"][-1])
        totals["biomedicine_pubmed"][y] = totals["biomedicine_pubmed"].get(y, 0) + r["journal_article"]
        if q <= 3:
            part["biomedicine_pubmed"][y] = part["biomedicine_pubmed"].get(y, 0) + r["journal_article"]
    out = {}
    for f, t in totals.items():
        ys = sorted(y for y in t if y - 1 in t and y <= 2025)
        out[f] = {y: t[y] / t[y - 1] - 1 for y in ys}
        out[f][2026] = part[f][2026] / part[f][2025] - 1
    return out


def corridor_chart(repo, out):
    growth = annual_growth(repo)
    panels = FIELDS + [("biomedicine_pubmed", "Biomedicine (PubMed journal articles)", "#1baf7a")]
    fig, axes = plt.subplots(1, 4, figsize=(14, 5.4), dpi=150, sharey=True)
    fig.patch.set_facecolor(SURFACE)
    for ax, (key, name, color) in zip(axes, panels):
        style(ax)
        g = growth[key]
        pre = [v for y, v in g.items() if y <= 2022]
        ax.axhspan(min(pre), max(pre), color=GRID, zorder=1, linewidth=0)
        ax.axhline(0, color=AXIS, linewidth=1, zorder=1)
        ys = sorted(g)
        ax.bar(ys, [g[y] for y in ys], width=0.7, zorder=2,
               color=[color if y >= 2023 else "#c3c2b7" for y in ys])
        ax.text(2026, g[2026] + 0.012, f"{g[2026]:+.0%}", ha="center", va="bottom", fontsize=8.5, color=INK)
        ax.set_title(name, loc="left", fontsize=10.5, color=INK, pad=22)
        ax.text(0, 1.02, f"{min(ys)}–2022 range: {min(pre):+.0%} to {max(pre):+.0%}", transform=ax.transAxes,
                fontsize=8, color=INK2, va="bottom")
        ticks = [y for y in ys if y in (2015, 2020, 2026)]
        ax.set_xticks(ticks)
        ax.set_xticklabels([("2026*" if y == 2026 else str(y)) for y in ticks])
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda t, _: "0%" if abs(t) < 1e-9 else f"{t:+.0%}"))
    fig.subplots_adjust(left=0.05, right=0.98, top=0.74, bottom=0.13, wspace=0.12)
    header(fig, "Is this year's growth unusual for the field?",
           "Annual growth of new papers. Grey band: the field's range up to 2022 (before ChatGPT). Coloured bars: 2023 on.")
    fig.text(0.05, 0.045, "*2026: January–September against January–September 2025. PubMed counts journal-article records "
             "by entry date, which also moves with indexing policy.", fontsize=8, color=INK2)
    fig.text(0.05, 0.02, "Sources: arXiv yearly statistics by primary archive (new submissions); PubMed E-utilities "
             "(publication type journal article, [edat]). Prototype for the chart proposal.", fontsize=7.5, color=MUTED)
    fig.savefig(os.path.join(out, "p4_growth_corridor.png"), facecolor=SURFACE)
    plt.close(fig)


def main(repo):
    out = os.path.join(repo, "docs/figures/proposal")
    os.makedirs(out, exist_ok=True)
    plt.rcParams.update({"font.family": "DejaVu Sans", "text.color": INK, "axes.labelcolor": INK2})
    data, growth = load(repo)
    trend_panels(data, out)
    pscore_chart(data, out)
    archive_chart(growth, out)
    corridor_chart(repo, out)
    print("written:", sorted(os.listdir(out)))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
