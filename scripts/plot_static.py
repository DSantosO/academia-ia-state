"""Static PNG charts of quarterly preprints by field and of the 2026 jump in arXiv mathematics.

Reads data/processed/preprints_by_field_quarterly.csv (build_datasets.py) and, when present,
data/processed/arxiv_math_monthly_profile.csv and arxiv_math_subcategories.csv (analyze_math.py).
Writes PNGs to docs/figures/.  Usage: python3 scripts/plot_static.py [repo_dir]   (needs matplotlib)
"""
import csv
import datetime as dt
import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.ticker as mticker  # noqa: E402
import matplotlib.transforms as mtransforms  # noqa: E402

SURFACE, INK, INK2, MUTED, GRID, AXIS = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
FIELDS = [  # column, label, colour (validated categorical slots 1-5)
    ("physics", "Physics", "#2a78d6"),
    ("mathematics", "Mathematics", "#eb6834"),
    ("biology_biorxiv", "Biology (bioRxiv)", "#1baf7a"),
    ("medicine_medrxiv_no_covid", "Medicine excl. COVID-19 (medRxiv)", "#eda100"),
    ("social_sciences", "Social sciences", "#e87ba4"),
]
REF = ("computer_science_reference", "Computer science (reference)", MUTED)
SHORT = {"computer_science_reference": "Computer science (ref.)", "medicine_medrxiv_no_covid": "Medicine excl. COVID-19"}
EVENTS = [
    (dt.date(2022, 11, 30), "ChatGPT"),
    (dt.date(2025, 10, 31), "arXiv rules"),
    (dt.date(2026, 2, 5), "Claude Opus 4.6"),
    (dt.date(2026, 7, 24), "Claude Opus 5"),
    (dt.date(2026, 10, 1), "arXiv cap"),
]
MATH_NAMES = {
    "math.AC": "Commutative algebra", "math.AG": "Algebraic geometry", "math.AP": "Analysis of PDEs",
    "math.AT": "Algebraic topology", "math.CA": "Classical analysis and ODEs", "math.CO": "Combinatorics",
    "math.CT": "Category theory", "math.CV": "Complex variables", "math.DG": "Differential geometry",
    "math.DS": "Dynamical systems", "math.FA": "Functional analysis", "math.GM": "General mathematics",
    "math.GN": "General topology", "math.GR": "Group theory", "math.GT": "Geometric topology",
    "math.HO": "History and overview", "math.IT": "Information theory", "math.KT": "K-theory and homology",
    "math.LO": "Logic", "math.MG": "Metric geometry", "math.MP": "Mathematical physics", "math.NA": "Numerical analysis",
    "math.NT": "Number theory", "math.OA": "Operator algebras", "math.OC": "Optimization and control",
    "math.PR": "Probability", "math.QA": "Quantum algebra", "math.RA": "Rings and algebras",
    "math.RT": "Representation theory", "math.SG": "Symplectic geometry", "math.SP": "Spectral theory",
    "math.ST": "Statistics theory",
}
MATH_EVENTS = [
    (dt.date(2025, 10, 31), "arXiv rules"),
    (dt.date(2026, 2, 5), "Claude Opus 4.6"),
    (dt.date(2026, 5, 20), "OpenAI disproves unit-distance conjecture"),
    (dt.date(2026, 7, 24), "Claude Opus 5"),
    (dt.date(2026, 10, 1), "arXiv cap"),
]
SOURCES = ("Sources: arXiv (primary archive), bioRxiv, medRxiv (COVID-19 preprints removed), PsyArXiv, SocArXiv and "
           "EdArXiv (first versions). New preprints per quarter; data as of 15 Oct 2026.")
ADVISORY = "Advisory: from 1 Oct 2026 arXiv caps each submitter at 2 submissions a month, so later arXiv counts are not comparable."


def mid(q):
    y, n = q.split("-Q")
    return dt.date(int(y), 3 * (int(n) - 1) + 2, 15)


def style(ax, grid_axis="y"):
    ax.set_facecolor(SURFACE)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(AXIS)
    ax.tick_params(colors=MUTED, labelsize=9, length=0)
    ax.grid(axis=grid_axis, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)


def spread(ys, gap):
    """Nudge label positions apart, keeping their order, so none are closer than `gap`."""
    order = sorted(range(len(ys)), key=lambda i: ys[i])
    pos = [ys[i] for i in order]
    for _ in range(100):
        moved = False
        for k in range(1, len(pos)):
            if pos[k] - pos[k - 1] < gap:
                d = (gap - (pos[k] - pos[k - 1])) / 2
                pos[k - 1] -= d
                pos[k] += d
                moved = True
        if not moved:
            break
    out = [0.0] * len(ys)
    for k, i in enumerate(order):
        out[i] = pos[k]
    return out


def events(ax, top, items):
    """Dashed vertical lines, each labelled directly above itself; labels that would overlap move up a row."""
    fig = ax.figure
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    lo, hi = ax.get_xlim()
    right_px = ax.transData.transform((hi, 0))[0]
    rows = []
    for d, label in items:
        if not lo <= mdates.date2num(d) <= hi:
            continue
        ax.axvline(d, color=MUTED, linewidth=1, linestyle=(0, (4, 3)), zorder=1)
        t = ax.text(d, top, label, fontsize=8.5, color=INK2, ha="center", va="bottom",
                    bbox=dict(facecolor=SURFACE, edgecolor="none", pad=1))
        bb = t.get_window_extent(renderer)
        if bb.x1 > right_px:
            t.set_ha("right")
            bb = t.get_window_extent(renderer)
        row = 0
        while row < len(rows) and any(not (bb.x1 + 6 < a or bb.x0 - 6 > b) for a, b in rows[row]):
            row += 1
        if row == len(rows):
            rows.append([])
        rows[row].append((bb.x0, bb.x1))
        if row:
            t.set_transform(ax.transData + mtransforms.ScaledTranslation(0, row * 14 / 72, fig.dpi_scale_trans))


def header(fig, title, subtitle, y=0.95):
    fig.text(0.05, y, title, fontsize=14, color=INK, ha="left", weight="bold")
    fig.text(0.05, y - 0.045, subtitle, fontsize=10, color=INK2, ha="left")


def line_chart(path, x, series, title, subtitle, fmt, ylim, base, end_fmt, note=None):
    fig, ax = plt.subplots(figsize=(10, 6.2), dpi=160)
    fig.patch.set_facecolor(SURFACE)
    style(ax)
    ax.axhline(base, color=AXIS, linewidth=1, zorder=1)
    for key, name, color, ys in series:
        ax.plot(x, ys, color=color, linewidth=1.5 if key == REF[0] else 2, solid_capstyle="round",
                solid_joinstyle="round", zorder=3)
        ax.plot(x[-1], ys[-1], "o", color=color, markersize=5, markeredgecolor=SURFACE, markeredgewidth=1.5, zorder=4)
    ax.set_ylim(*ylim)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda t, _: fmt(t)))
    first = x[0].year
    ax.set_xlim(dt.date(first, 1, 1), dt.date(2028, 9, 1))
    ax.set_xticks([dt.date(y, 7, 1) for y in range(first, 2027)])
    ax.set_xticklabels([str(y) for y in range(first, 2027)])
    ax.spines["bottom"].set_bounds(mdates.date2num(dt.date(first, 1, 1)), mdates.date2num(dt.date(2026, 10, 1)))
    ends = [s[3][-1] for s in series]
    labels_y = spread(ends, (ylim[1] - ylim[0]) * 0.05)
    x_lab = x[-1] + dt.timedelta(days=60)
    for (key, name, color, ys), y_end, y_lab in zip(series, ends, labels_y):
        ax.plot([x[-1] + dt.timedelta(days=8), x_lab - dt.timedelta(days=6)], [y_end, y_lab], color=AXIS, linewidth=0.8)
        ax.text(x_lab, y_lab, f"{SHORT.get(key, name)}  {end_fmt(y_end)}", color=INK, fontsize=9, va="center")
    fig.subplots_adjust(left=0.07, right=0.98, top=0.78, bottom=0.135)
    events(ax, ylim[1], EVENTS)
    header(fig, title, subtitle)
    fig.text(0.05, 0.02, SOURCES, fontsize=7.5, color=MUTED, ha="left")
    fig.text(0.05, 0.07 if note else 0.045, ADVISORY, fontsize=8, color=INK2, ha="left")
    if note:
        fig.text(0.05, 0.045, note, fontsize=8, color=INK2, ha="left")
    fig.savefig(path, facecolor=SURFACE)
    plt.close(fig)


def field_charts(repo, out):
    rows = list(csv.DictReader(open(os.path.join(repo, "data/processed/preprints_by_field_quarterly.csv"))))
    quarters = [r["quarter"] for r in rows]
    x = [mid(q) for q in quarters]
    vals = {k: [int(r[k]) for r in rows] for k, _, _ in FIELDS + [REF]}
    base = {k: sum(v for q, v in zip(quarters, vals[k]) if q.startswith("2022-")) / 4 for k in vals}
    order = [REF] + FIELDS

    idx = [(k, n, c, [100 * v / base[k] for v in vals[k]]) for k, n, c in order]
    top = max(max(s[3]) for s in idx)
    line_chart(os.path.join(out, "fig1_index_by_field.png"), x, idx,
               "New preprints by field (index, 2022 = 100)",
               "Each quarter relative to the field's 2022 quarterly average. Q1 2020 – Q3 2026.",
               lambda t: f"{t:.0f}", (40, top * 1.06), 100, lambda v: f"{v:.0f}",
               note="Medicine's 2022 base is low: COVID-19 research crowded out other medRxiv preprints in "
                    "2020–2022, which inflates its index.")

    yoy = [(k, n, c, [vals[k][i] / vals[k][i - 4] - 1 for i in range(4, len(rows))]) for k, n, c in order]
    lo = min(min(s[3]) for s in yoy)
    hi = max(max(s[3]) for s in yoy)
    line_chart(os.path.join(out, "fig2_yoy_growth_by_field.png"), x[4:], yoy,
               "Year-on-year growth of new preprints by field",
               "Each quarter compared with the same quarter a year earlier. Q1 2021 – Q3 2026.",
               lambda t: "0%" if abs(t) < 1e-9 else f"{t:+.0%}", (min(lo, 0) - 0.05, hi + 0.08), 0,
               lambda v: f"{v:+.0%}",
               note="medRxiv opened in June 2019, so medicine's early-2021 growth compares against its first months.")

    panels = FIELDS + [REF]
    fig, axes = plt.subplots(2, 3, figsize=(12, 6.8), dpi=150)
    fig.patch.set_facecolor(SURFACE)
    pos = list(range(len(quarters)))
    i_chatgpt = quarters.index("2023-Q1") - 0.5
    for ax, (k, name, c) in zip(axes.flat, panels):
        style(ax)
        v = vals[k]
        ax.bar(pos, v, width=0.72, color=c, zorder=2)
        ax.set_ylim(0, max(v) * 1.18)
        ax.yaxis.set_major_locator(mticker.MaxNLocator(3))
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda t, _: f"{t / 1000:g}k" if t >= 1000 else f"{t:.0f}"))
        ax.axvline(i_chatgpt, color=MUTED, linewidth=1, linestyle=(0, (4, 3)), zorder=1)
        ax.text(i_chatgpt - 0.4, max(v) * 1.16, "ChatGPT", fontsize=8, color=INK2, ha="right", va="top")
        ax.text(pos[-1], v[-1] + max(v) * 0.03, f"{v[-1]:,}", fontsize=8, color=INK, ha="center", va="bottom")
        firsts = [i for i, q in enumerate(quarters) if q.endswith("-Q1")]
        ax.set_xticks([i + 1.5 for i in firsts])
        ax.set_xticklabels([quarters[i][:4] for i in firsts])
        ax.set_xlim(-0.8, len(quarters) - 0.2)
        change = sum(v[-4:]) / sum(val for q, val in zip(quarters, v) if q.startswith("2022-")) - 1
        ax.set_title(name.replace(" (medRxiv)", ""), loc="left", fontsize=11, color=INK, pad=14)
        ax.text(0, 1.015, f"Last year vs 2022: {change:+.0%}", transform=ax.transAxes, fontsize=8.5, color=INK2,
                ha="left", va="bottom")
    fig.subplots_adjust(left=0.05, right=0.99, top=0.83, bottom=0.08, hspace=0.62, wspace=0.18)
    header(fig, "New preprints per quarter by field",
           "Q1 2020 – Q3 2026. Each panel has its own scale; last year = Oct 2025 – Sep 2026.", y=0.965)
    fig.text(0.05, 0.012, SOURCES, fontsize=7.5, color=MUTED, ha="left")
    fig.savefig(os.path.join(out, "fig3_quarterly_by_field.png"), facecolor=SURFACE)
    plt.close(fig)


def math_charts(repo, out):
    prof_path = os.path.join(repo, "data/processed/arxiv_math_monthly_profile.csv")
    if not os.path.exists(prof_path):
        return
    prof = [r for r in csv.DictReader(open(prof_path)) if r["month"] <= "2026-09"]
    months = [dt.date(int(r["month"][:4]), int(r["month"][5:]), 15) for r in prof]
    papers = [int(r["papers"]) for r in prof]
    color = "#eb6834"

    fig, ax = plt.subplots(figsize=(10, 5.8), dpi=160)
    fig.patch.set_facecolor(SURFACE)
    style(ax)
    ax.bar(months, papers, width=22, color=color, zorder=2)
    ax.set_ylim(0, max(papers) * 1.12)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda t, _: f"{t:,.0f}"))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 4, 7, 10)))
    ax.set_xlim(dt.date(2024, 12, 20), dt.date(2026, 10, 25))
    for d, v in zip(months, papers):
        if d >= dt.date(2026, 6, 1) or d == dt.date(2025, 9, 15):
            ax.text(d, v + max(papers) * 0.015, f"{v:,}", ha="center", va="bottom", fontsize=8, color=INK)
    fig.subplots_adjust(left=0.08, right=0.98, top=0.72, bottom=0.13)
    events(ax, max(papers) * 1.12, MATH_EVENTS)
    header(fig, "New arXiv mathematics papers per month",
           "Primary category math.*, counted in the month of the first version. Jan 2025 – Sep 2026.")
    fig.text(0.05, 0.02, "Source: arXiv OAI-PMH metadata (harvested 15 Oct 2026).", fontsize=7.5, color=MUTED)
    fig.text(0.05, 0.045, ADVISORY, fontsize=8, color=INK2)
    fig.savefig(os.path.join(out, "fig4_math_monthly.png"), facecolor=SURFACE)
    plt.close(fig)

    metrics = [
        ("ai_tool_mention", "Mention an AI tool or model", "Share of papers (title, abstract or comments)", True),
        ("erdos_mention", "Mention Erdős", "Papers per month", False),
        ("prolific_author", "Have an author with 5+ math papers that quarter", "Share of papers", True),
        ("single_author", "Single-author papers", "Share of papers", True),
    ]
    fig, axes = plt.subplots(2, 2, figsize=(11, 6.8), dpi=150)
    fig.patch.set_facecolor(SURFACE)
    for ax, (key, title, sub, share) in zip(axes.flat, metrics):
        style(ax)
        ys = [int(r[key]) / int(r["papers"]) if share else int(r[key]) for r in prof]
        ax.plot(months, ys, color=color, linewidth=2, solid_capstyle="round", zorder=3)
        ax.plot(months[-1], ys[-1], "o", color=color, markersize=5, markeredgecolor=SURFACE, markeredgewidth=1.5,
                zorder=4)
        ax.text(months[-1], ys[-1], f"  {ys[-1]:.1%}" if share else f"  {ys[-1]:,}", fontsize=8.5, color=INK,
                va="center", ha="left")
        ax.set_ylim(0, max(ys) * 1.25)
        ax.yaxis.set_major_locator(mticker.MaxNLocator(4))
        small = share and max(ys) < 0.05
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(
            lambda t, _, s=share, sm=small: (f"{t:.1%}" if sm else f"{t:.0%}") if s else f"{t:.0f}"))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
        ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
        ax.set_xlim(dt.date(2024, 12, 15), dt.date(2026, 11, 15))
        for d in (dt.date(2026, 2, 5), dt.date(2026, 7, 24), dt.date(2026, 10, 1)):
            ax.axvline(d, color=MUTED, linewidth=1, linestyle=(0, (4, 3)), zorder=1)
        ax.set_title(title, loc="left", fontsize=11, color=INK, pad=16)
        ax.text(0, 1.02, sub, transform=ax.transAxes, fontsize=8.5, color=INK2, va="bottom")
    fig.subplots_adjust(left=0.07, right=0.97, top=0.8, bottom=0.08, hspace=0.62, wspace=0.18)
    header(fig, "What changed in arXiv mathematics papers",
           "Monthly, Jan 2025 – Sep 2026. Dashed lines: Claude Opus 4.6 (5 Feb 2026), Claude Opus 5 (24 Jul 2026), "
           "arXiv cap (1 Oct 2026).",
           y=0.955)
    fig.text(0.05, 0.012, "Source: arXiv OAI-PMH metadata; keyword matching on title, abstract and comments.",
             fontsize=7.5, color=MUTED)
    fig.savefig(os.path.join(out, "fig5_math_profile.png"), facecolor=SURFACE)
    plt.close(fig)

    subs = list(csv.DictReader(open(os.path.join(repo, "data/processed/arxiv_math_subcategories.csv"))))
    subs = subs[:20]  # the file is sorted by Q3 2026 volume
    subs.sort(key=lambda s: float(s["change"]))
    fig, ax = plt.subplots(figsize=(9, 7), dpi=150)
    fig.patch.set_facecolor(SURFACE)
    style(ax, grid_axis="x")
    names = [f"{MATH_NAMES.get(s['subcategory'], s['subcategory'])} ({s['subcategory'][5:]})" for s in subs]
    ch = [float(s["change"]) for s in subs]
    ax.barh(names, ch, height=0.62, color=color, zorder=2)
    for i, (c, s) in enumerate(zip(ch, subs)):
        ax.text(max(c, 0) + 0.01, i, f"{c:+.0%}  ({int(s['q3_2025']):,} → {int(s['q3_2026']):,})", va="center",
                fontsize=8, color=INK)
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda t, _: "0%" if abs(t) < 1e-9 else f"{t:+.0%}"))
    ax.set_xlim(min(0, min(ch)) - 0.05, max(ch) * 1.5)
    ax.tick_params(axis="y", labelsize=9, colors=INK2)
    ax.spines["bottom"].set_visible(False)
    ax.axvline(0, color=AXIS, linewidth=1)
    fig.subplots_adjust(left=0.27, right=0.97, top=0.86, bottom=0.07)
    header(fig, "Growth by mathematics subfield, Q3 2026 vs Q3 2025",
           "New arXiv papers by primary subcategory; the 20 largest subfields.", y=0.95)
    fig.text(0.05, 0.015, "Source: arXiv OAI-PMH metadata (harvested 15 Oct 2026).", fontsize=7.5, color=MUTED)
    fig.savefig(os.path.join(out, "fig6_math_subfields.png"), facecolor=SURFACE)
    plt.close(fig)


def cs_charts(repo, out):
    split_path = os.path.join(repo, "data/processed/arxiv_cs_ai_split_quarterly.csv")
    if not os.path.exists(split_path):
        return
    fields = {r["quarter"]: r for r in csv.DictReader(open(os.path.join(repo, "data/processed/preprints_by_field_quarterly.csv")))}
    rows = [r for r in csv.DictReader(open(split_path)) if r["quarter"] in fields]
    quarters = [r["quarter"] for r in rows]
    x = [mid(q) for q in quarters]
    ai = [int(r["ai_categories"]) + int(r["ai_text_other"]) for r in rows]
    other = [int(r["non_ai"]) for r in rows]
    total = [int(r["cs_total"]) for r in rows]
    violet, red = "#6250d6", "#e34948"

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.8), dpi=150, gridspec_kw={"width_ratios": [1, 1.15]})
    fig.patch.set_facecolor(SURFACE)
    style(ax1)
    pos = list(range(len(quarters)))
    ax1.bar(pos, other, width=0.72, color=red, zorder=2, label="CS without AI")
    ax1.bar(pos, ai, width=0.72, bottom=other, color=violet, zorder=2, label="AI research")
    ax1.set_ylim(0, max(total) * 1.15)
    ax1.yaxis.set_major_locator(mticker.MaxNLocator(4))
    ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda t, _: f"{t / 1000:g}k" if t >= 1000 else f"{t:.0f}"))
    firsts = [i for i, q in enumerate(quarters) if q.endswith("-Q1")]
    ax1.set_xticks([i + 1.5 for i in firsts])
    ax1.set_xticklabels([quarters[i][:4] for i in firsts])
    ax1.set_xlim(-0.8, len(quarters) - 0.2)
    share = ai[-1] / total[-1]
    ax1.text(pos[-1], total[-1] + max(total) * 0.02, f"AI {share:.0%}", fontsize=8.5, color=INK, ha="center")
    handles, labels = ax1.get_legend_handles_labels()
    ax1.legend(handles[::-1], labels[::-1], loc="upper left", frameon=False, fontsize=9, labelcolor=INK2)
    ax1.set_title("New arXiv computer-science papers per quarter", loc="left", fontsize=11, color=INK, pad=64)

    style(ax2)
    base = lambda v: sum(val for q, val in zip(quarters, v) if q.startswith("2022-")) / 4
    series = [  # the two CS series carry colour; physics and mathematics are grey context
        ("Physics", MUTED, [int(fields[q]["physics"]) for q in quarters], 1.5),
        ("Mathematics", INK2, [int(fields[q]["mathematics"]) for q in quarters], 1.5),
        ("AI research", violet, ai, 2),
        ("CS without AI", red, other, 2),
    ]
    idx = [(n, c, [100 * v / base(vals) for v in vals], lw) for n, c, vals, lw in series]
    ax2.axhline(100, color=AXIS, linewidth=1, zorder=1)
    for n, c, ys, lw in idx:
        ax2.plot(x, ys, color=c, linewidth=lw, solid_capstyle="round", solid_joinstyle="round", zorder=3)
        ax2.plot(x[-1], ys[-1], "o", color=c, markersize=5, markeredgecolor=SURFACE, markeredgewidth=1.5, zorder=4)
    top = max(max(s[2]) for s in idx)
    ax2.set_ylim(40, top * 1.12)
    ax2.set_xlim(dt.date(2020, 1, 1), dt.date(2029, 3, 1))
    ax2.set_xticks([dt.date(y, 7, 1) for y in range(2020, 2027)])
    ax2.set_xticklabels([str(y) for y in range(2020, 2027)])
    ax2.spines["bottom"].set_bounds(mdates.date2num(dt.date(2020, 1, 1)), mdates.date2num(dt.date(2026, 10, 1)))
    ends = [s[2][-1] for s in idx]
    labels_y = spread(ends, (top * 1.12 - 40) * 0.055)
    x_lab = x[-1] + dt.timedelta(days=60)
    for (n, c, ys, lw), y_end, y_lab in zip(idx, ends, labels_y):
        ax2.plot([x[-1] + dt.timedelta(days=8), x_lab - dt.timedelta(days=6)], [y_end, y_lab], color=AXIS, linewidth=0.8)
        ax2.text(x_lab, y_lab, f"{n}  {y_end:.0f}", color=INK, fontsize=9, va="center")
    ax2.set_title("Index, 2022 = 100 (physics and mathematics in grey)", loc="left", fontsize=11, color=INK, pad=64)
    fig.subplots_adjust(left=0.05, right=0.98, top=0.66, bottom=0.12, wspace=0.12)
    events(ax2, top * 1.12, EVENTS)
    header(fig, "Computer science with and without AI research",
           "AI research = primary category cs.AI, cs.LG, cs.CL, cs.CV, cs.NE or cs.MA, or another CS category whose "
           "title or abstract uses AI/ML vocabulary.", y=0.95)
    fig.text(0.05, 0.02, "Source: arXiv OAI-PMH metadata (harvested Oct 2026); physics and mathematics from arXiv "
             "yearly statistics. New papers per quarter, Q1 2020 – Q3 2026.", fontsize=7.5, color=MUTED)
    fig.text(0.05, 0.045, ADVISORY, fontsize=8, color=INK2)
    fig.savefig(os.path.join(out, "fig7_cs_without_ai.png"), facecolor=SURFACE)
    plt.close(fig)


def main(repo):
    out = os.path.join(repo, "docs/figures")
    os.makedirs(out, exist_ok=True)
    plt.rcParams.update({"font.family": "DejaVu Sans", "text.color": INK, "axes.labelcolor": INK2})
    field_charts(repo, out)
    math_charts(repo, out)
    cs_charts(repo, out)
    print("written:", sorted(os.listdir(out)))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
