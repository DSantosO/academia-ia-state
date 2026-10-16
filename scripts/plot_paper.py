"""Publication versions of figures 1, 4 and 5 for the essay (no titles; captions live in the text).

Writes docs/figures/paper/<name>_{85mm,175mm}.{svg,pdf,png} (PNG at 300 dpi) from data/processed.
Markers: ChatGPT, arXiv rule changes and Claude Opus 5 only. Colours: Okabe-Ito (colour-blind safe).
Usage: python3 scripts/plot_paper.py [repo_dir]   (needs matplotlib)
"""
import csv
import datetime as dt
import json
import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.lines  # noqa: E402,F401
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.ticker as mticker  # noqa: E402

MM = 1 / 25.4
INK, INK2, MUTED, GRID, AXIS = "#000000", "#444444", "#7f7f7f", "#e3e3e3", "#9a9a9a"
OI = {"blue": "#0072B2", "vermillion": "#D55E00", "green": "#009E73", "orange": "#E69F00", "purple": "#CC79A7",
      "grey": "#999999"}
FIELDS = [
    ("physics", "Physics", OI["blue"]),
    ("mathematics", "Mathematics", OI["vermillion"]),
    ("biology_biorxiv", "Biology (bioRxiv)", OI["green"]),
    ("medicine_medrxiv_no_covid", "Medicine excl. COVID-19 (medRxiv)", OI["orange"]),
    ("social_sciences", "Social sciences", OI["purple"]),
    ("computer_science_reference", "Computer science", OI["grey"]),
]
SHORT = {"medicine_medrxiv_no_covid": "Medicine excl. COVID-19", "biology_biorxiv": "Biology",
         "computer_science_reference": "Computer sci.", "social_sciences": "Social sci."}
FIELD_EVENTS = [
    (dt.date(2022, 11, 30), "ChatGPT"),
    (dt.date(2025, 10, 31), "arXiv CS review rule"),
    (dt.date(2026, 7, 24), "Claude Opus 5"),
    (dt.date(2026, 10, 1), "arXiv cap"),
]
MATH_EVENTS = [
    (dt.date(2025, 12, 10), "arXiv math endorsement rule"),
    (dt.date(2026, 7, 24), "Claude Opus 5"),
    (dt.date(2026, 10, 1), "arXiv cap"),
]


def setup(fontsize):
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": fontsize, "axes.labelsize": fontsize,
        "xtick.labelsize": fontsize - 0.5, "ytick.labelsize": fontsize - 0.5, "text.color": INK,
        "axes.labelcolor": INK2, "svg.fonttype": "none", "pdf.fonttype": 42, "axes.linewidth": 0.6,
    })


def style(ax):
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(AXIS)
    ax.tick_params(colors=INK2, length=0, pad=2)
    ax.tick_params(axis="x", length=2.5, width=0.6, color=AXIS)  # date ticks mark the start of the period
    ax.grid(axis="y", color=GRID, linewidth=0.5)
    ax.set_axisbelow(True)


def year_ticks(ax, first, last, every=1):
    """Major ticks on 1 January of each year, labelled at the tick (every `every` years)."""
    ax.set_xticks([dt.date(y, 1, 1) for y in range(first, last + 1)])
    ax.set_xticklabels([str(y) if (y - first) % every == 0 else "" for y in range(first, last + 1)])


def spread(ys, gap):
    order = sorted(range(len(ys)), key=lambda i: ys[i])
    pos = [ys[i] for i in order]
    for _ in range(200):
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


def events(ax, items, label=True, fontsize=6):
    """Dashed lines; labels in rows above the plot so they never overlap."""
    fig = ax.figure
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    lo, hi = ax.get_xlim()
    rows = []
    for d, text in items:
        if not lo <= mdates.date2num(d) <= hi:
            continue
        ax.axvline(d, color=MUTED, linewidth=0.6, linestyle=(0, (3, 2)), zorder=1)
        if not label:
            continue
        t = ax.text(d, 1.0, text, transform=ax.get_xaxis_transform(), fontsize=fontsize, color=INK2,
                    ha="center", va="bottom")
        bb = t.get_window_extent(r)
        if bb.x1 > fig.bbox.x1 - 4:
            t.set_ha("right")
            bb = t.get_window_extent(r)
        row = 0
        while row < len(rows) and any(not (bb.x1 + 3 < a or bb.x0 - 3 > b) for a, b in rows[row]):
            row += 1
        if row == len(rows):
            rows.append([])
        rows[row].append((bb.x0, bb.x1))
        t.set_y(1.0 + 0.004 + row * (fontsize + 1.5) / 72 / (ax.get_window_extent(r).height / fig.dpi))


def save(fig, out, name):
    for ext in ("svg", "pdf", "png"):
        fig.savefig(os.path.join(out, f"{name}.{ext}"), dpi=300 if ext == "png" else None, facecolor="white")
    plt.close(fig)


def fig1(repo, out, width_mm):
    rows = list(csv.DictReader(open(os.path.join(repo, "data/processed/preprints_by_field_quarterly.csv"))))
    q = [r["quarter"] for r in rows]
    x = [dt.date(int(s[:4]), 3 * (int(s[-1]) - 1) + 2, 15) for s in q]
    narrow = width_mm < 120
    setup(6.5 if narrow else 7)
    fig, ax = plt.subplots(figsize=(width_mm * MM, (88 if narrow else 100) * MM))
    style(ax)
    ax.axhline(100, color=AXIS, linewidth=0.6, zorder=1)
    ends = []
    for key, name, color in reversed(FIELDS):
        v = [int(r[key]) for r in rows]
        base = sum(val for s, val in zip(q, v) if s.startswith("2022-")) / 4
        ys = [100 * val / base for val in v]
        lw = 0.9 if key == "computer_science_reference" else 1.2
        ax.plot(x, ys, color=color, linewidth=lw, solid_capstyle="round", solid_joinstyle="round", zorder=3)
        ax.plot(x[-1], ys[-1], "o", color=color, markersize=2.5, zorder=4)
        ends.append((key, name, color, ys[-1]))
    top = max(e[3] for e in ends)
    ax.set_ylim(40, top * 1.06)
    ax.set_xlim(dt.date(2020, 1, 1), dt.date(2028, 11, 1) if not narrow else dt.date(2026, 12, 1))
    year_ticks(ax, 2020, 2026, every=2 if narrow else 1)
    ax.spines["bottom"].set_bounds(mdates.date2num(dt.date(2020, 1, 1)), mdates.date2num(dt.date(2026, 10, 15)))
    ax.set_ylabel("Index (2022 = 100)")
    if narrow:  # no room for end labels: a legend below the plot carries names and latest values
        handles = [matplotlib.lines.Line2D([], [], color=c, linewidth=1.2, marker="o", markersize=2.5)
                   for _, _, c, _ in reversed(ends)]
        names = [f"{n.replace(' (medRxiv)', '').replace(' (bioRxiv)', '')} ({y:.0f})" for _, n, _, y in reversed(ends)]
        ax.legend(handles, names, loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=2, frameon=False,
                  fontsize=plt.rcParams["font.size"] - 0.5, handlelength=1.6, columnspacing=1.2)
    else:
        labels_y = spread([e[3] for e in ends], (top * 1.06 - 40) * 0.05)
        x_lab = x[-1] + dt.timedelta(days=95)
        for (key, name, color, y_end), y_lab in zip(ends, labels_y):
            ax.plot([x[-1] + dt.timedelta(days=10), x_lab - dt.timedelta(days=8)], [y_end, y_lab], color=AXIS,
                    linewidth=0.5)
            ax.text(x_lab, y_lab, f"{name.replace(' (medRxiv)', '').replace(' (bioRxiv)', '')} {y_end:.0f}",
                    fontsize=plt.rcParams["font.size"] - 0.5, color=INK, va="center")
    fig.subplots_adjust(left=0.13 if narrow else 0.08, right=0.97 if narrow else 0.99, top=0.84,
                        bottom=0.25 if narrow else 0.09)
    events(ax, FIELD_EVENTS, fontsize=5.5 if narrow else 6)
    save(fig, out, f"fig1_index_by_field_{width_mm}mm")


def math_rows(repo):
    prof = [r for r in csv.DictReader(open(os.path.join(repo, "data/processed/arxiv_math_monthly_profile.csv")))
            if r["month"] <= "2026-09"]
    rob = json.load(open(os.path.join(repo, "data/processed/arxiv_math_prolific_robustness.json")))
    return prof, rob["6b_monthly_prolific_share_full_names_without_top1pct_surnames"]


def fig4(repo, out, width_mm):
    prof, _ = math_rows(repo)
    narrow = width_mm < 120
    setup(6.5 if narrow else 7)
    months = [dt.date(int(r["month"][:4]), int(r["month"][5:]), 15) for r in prof]
    papers = [int(r["papers"]) for r in prof]
    fig, ax = plt.subplots(figsize=(width_mm * MM, (62 if narrow else 75) * MM))
    style(ax)
    ax.bar(months, papers, width=22, color=OI["vermillion"], zorder=2)
    ax.set_ylim(0, max(papers) * 1.1)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda t, _: f"{t:,.0f}"))
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7) if narrow else (1, 4, 7, 10)))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
    ax.set_xlim(dt.date(2024, 12, 20), dt.date(2026, 10, 12))
    ax.set_ylabel("New mathematics papers")
    for d, v in zip(months, papers):
        if (narrow and d in (dt.date(2025, 9, 15), dt.date(2026, 9, 15))) or (
                not narrow and (d >= dt.date(2026, 6, 1) or d == dt.date(2025, 9, 15))):
            ax.text(d, v + max(papers) * 0.01, f"{v:,}", ha="center", va="bottom", fontsize=5.5 if narrow else 6)
    fig.subplots_adjust(left=0.15 if narrow else 0.09, right=0.98, top=0.82, bottom=0.17)
    events(ax, MATH_EVENTS, fontsize=5.5 if narrow else 6)
    save(fig, out, f"fig4_math_monthly_{width_mm}mm")


def fig5(repo, out, width_mm):
    prof, robust = math_rows(repo)
    narrow = width_mm < 120
    setup(6.5 if narrow else 7)
    months = [dt.date(int(r["month"][:4]), int(r["month"][5:]), 15) for r in prof]
    share = lambda k: [int(r[k]) / int(r["papers"]) for r in prof]  # noqa: E731
    panels = [
        ("a", "Papers with a prolific author",
         [(share("prolific_author"), "All author names", OI["vermillion"]),
          ([robust[r["month"]] for r in prof], "Full first names only, 1% most\ncommon surnames removed", OI["grey"])], True),
        ("b", "Single-author papers", [(share("single_author"), None, OI["vermillion"])], True),
        ("c", "Papers mentioning an AI tool or model" if not narrow else "Papers mentioning an AI tool\nor model",
         [(share("ai_tool_mention"), None, OI["vermillion"])], True),
        ("d", "Papers mentioning Erdős (count)", [([int(r["erdos_mention"]) for r in prof], None, OI["vermillion"])], False),
    ]
    if narrow:
        fig, axes = plt.subplots(4, 1, figsize=(width_mm * MM, 175 * MM))
    else:
        fig, axes = plt.subplots(2, 2, figsize=(width_mm * MM, 115 * MM))
    for ax, (tag, title, lines, is_share) in zip(axes.flat, panels):
        style(ax)
        top = 0
        for ys, label, color in lines:
            ax.plot(months, ys, color=color, linewidth=1.2, solid_capstyle="round", zorder=3)
            ax.plot(months[-1], ys[-1], "o", color=color, markersize=2.5, zorder=4)
            ax.text(months[-1] + dt.timedelta(days=12), ys[-1], f"{ys[-1]:.1%}" if is_share else f"{ys[-1]:,}",
                    fontsize=plt.rcParams["font.size"] - 0.5, va="center", color=INK)
            top = max(top, max(ys))
        if len(lines) > 1:
            handles = [matplotlib.lines.Line2D([], [], color=c, linewidth=1.2) for _, _, c in lines]
            ax.legend(handles, [lab for _, lab, _ in lines], loc="upper left", frameon=False,
                      fontsize=plt.rcParams["font.size"] - 1, handlelength=1.4, labelcolor=INK2)
        ax.set_ylim(0, top * 1.25)
        ax.yaxis.set_major_locator(mticker.MaxNLocator(4))
        small = is_share and top < 0.05
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(
            lambda t, _, s=is_share, sm=small: (f"{t:.1%}" if sm else f"{t:.0%}") if s else f"{t:.0f}"))
        ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
        ax.set_xlim(dt.date(2024, 12, 20), dt.date(2026, 11, 30))
        ax.set_title(f"{tag}   {title}", loc="left", fontsize=plt.rcParams["font.size"], color=INK, pad=4)
        events(ax, MATH_EVENTS, label=False)
    if narrow:
        fig.subplots_adjust(left=0.14, right=0.93, top=0.97, bottom=0.04, hspace=0.62)
    else:
        fig.subplots_adjust(left=0.07, right=0.96, top=0.94, bottom=0.07, hspace=0.5, wspace=0.2)
    save(fig, out, f"fig5_math_profile_{width_mm}mm")


def main(repo):
    out = os.path.join(repo, "docs/figures/paper")
    os.makedirs(out, exist_ok=True)
    for w in (85, 175):
        fig1(repo, out, w)
        fig4(repo, out, w)
        fig5(repo, out, w)
    print("written:", sorted(os.listdir(out)))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
