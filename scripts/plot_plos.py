"""Figures for the PLOS ONE article, to PLOS ONE's figure specification.

TIFF (LZW, RGB 8 bit, no alpha, 300 dpi), width <= 19.05 cm, text 8-12 pt in an Arial-metric font (Arial if
installed, otherwise Liberation Sans, which has Arial's metrics); PDF (TrueType fonts embedded) and SVG copies.
Captions live in the manuscript (docs/stats/figure_captions.md). Writes docs/figures/plos/Fig{n}.{tif,pdf,svg}.
Usage: python3 scripts/plot_plos.py [repo_dir]
"""
import csv
import datetime as dt
import io
import json
import os
import sys
from collections import defaultdict

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.font_manager as fm  # noqa: E402
import matplotlib.lines  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.ticker as mticker  # noqa: E402
from PIL import Image  # noqa: E402

CM = 1 / 2.54
INK, INK2, MUTED, GRID, AXIS = "#000000", "#404040", "#7f7f7f", "#e3e3e3", "#9a9a9a"
OI = {"blue": "#0072B2", "vermillion": "#D55E00", "green": "#009E73", "orange": "#E69F00", "purple": "#CC79A7",
      "grey": "#999999", "sky": "#56B4E9", "black": "#000000"}
EVENTS = [(dt.date(2022, 11, 30), "ChatGPT"), (dt.date(2025, 10, 31), "arXiv CS review rule"),
          (dt.date(2026, 10, 1), "arXiv cap")]
FONT = "Arial" if any("Arial" in f.name for f in fm.fontManager.ttflist) else "Liberation Sans"


def setup():
    plt.rcParams.update({"font.family": FONT, "font.size": 8, "axes.labelsize": 8, "xtick.labelsize": 8,
                         "ytick.labelsize": 8, "legend.fontsize": 8, "axes.titlesize": 9, "text.color": INK,
                         "axes.labelcolor": INK2, "pdf.fonttype": 42, "svg.fonttype": "none", "axes.linewidth": 0.6,
                         "svg.hashsalt": "plos-figures"})


def style(ax):
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(AXIS)
    ax.tick_params(colors=INK2, length=0, pad=2)
    ax.tick_params(axis="x", length=3, width=0.6, color=AXIS)
    ax.grid(axis="y", color=GRID, linewidth=0.5)
    ax.set_axisbelow(True)


def year_ticks(ax, first, last):
    ax.set_xticks([dt.date(y, 1, 1) for y in range(first, last + 1)])
    ax.set_xticklabels([str(y) for y in range(first, last + 1)])


def events(ax, label=True, only=None):
    lo, hi = ax.get_xlim()
    rows = []
    fig = ax.figure
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    for d, text in EVENTS:
        if only and text not in only:
            continue
        if not lo <= mdates.date2num(d) <= hi:
            continue
        ax.axvline(d, color=MUTED, linewidth=0.6, linestyle=(0, (3, 2)), zorder=1)
        if not label:
            continue
        t = ax.text(d, 1.0, text, transform=ax.get_xaxis_transform(), fontsize=8, color=INK2, ha="center",
                    va="bottom")
        bb = t.get_window_extent(r)
        if bb.x1 > ax.get_window_extent(r).x1 + 10:
            t.set_ha("right")
            bb = t.get_window_extent(r)
        row = 0
        while row < len(rows) and any(not (bb.x1 + 3 < a or bb.x0 - 3 > b) for a, b in rows[row]):
            row += 1
        if row == len(rows):
            rows.append([])
        rows[row].append((bb.x0, bb.x1))
        t.set_y(1.0 + 0.01 + row * 9.5 / 72 / (ax.get_window_extent(r).height / fig.dpi))


def panel_label(ax, s, pad=24):
    """Bold panel letter level with the panel title (titles use the same pad in points)."""
    ax.annotate(s, xy=(0, 1), xycoords="axes fraction", xytext=(-28, pad), textcoords="offset points",
                fontsize=11, weight="bold", va="baseline", ha="left")


def save(fig, out, name):
    os.makedirs(out, exist_ok=True)
    # no creation dates, fixed SVG ids: re-running the script reproduces the files byte for byte
    fig.savefig(os.path.join(out, name + ".pdf"), facecolor="white", metadata={"CreationDate": None})
    fig.savefig(os.path.join(out, name + ".svg"), facecolor="white", metadata={"Date": None})
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=300, facecolor="white")
    buf.seek(0)
    img = Image.open(buf).convert("RGB")
    assert img.width <= 2250, f"{name}: {img.width}px wider than PLOS maximum"
    img.save(os.path.join(out, name + ".tif"), compression="tiff_lzw", dpi=(300, 300))
    plt.close(fig)


def xq(q):
    return dt.date(int(q[:4]), 3 * (int(q[-1]) - 1) + 2, 15)


def index_lines(ax, series, colors, labels, first="2020-Q1"):
    for key, c, lab in zip(series, colors, labels):
        qs = sorted(q for q in series[key] if q >= first)
        x = [xq(q) for q in qs]
        ys = [series[key][q] for q in qs]
        ax.plot(x, ys, color=c, linewidth=1.3, label=f"{lab} ({ys[-1]:.0f})", solid_capstyle="round")
        ax.plot(x[-1], ys[-1], "o", color=c, markersize=3)
    ax.axhline(100, color=AXIS, linewidth=0.6, zorder=1)
    ax.set_xlim(dt.date(2020, 1, 1), dt.date(2026, 12, 1))
    year_ticks(ax, 2020, 2026)
    ax.spines["bottom"].set_bounds(mdates.date2num(dt.date(2020, 1, 1)), mdates.date2num(dt.date(2026, 10, 15)))
    ax.set_ylabel("Index (2022 = 100)")


def quarterly_index(monthly):
    q = defaultdict(int)
    for m, v in monthly.items():
        q[f"{m[:4]}-Q{(int(m[5:]) - 1) // 3 + 1}"] += v
    q = {k: v for k, v in q.items() if k <= "2026-Q3"}
    base = sum(q.get(f"2022-Q{i}", 0) for i in range(1, 5)) / 4
    return {k: 100 * v / base for k, v in q.items()}


def fig1(repo, out):
    rows = list(csv.DictReader(open(os.path.join(repo, "data/processed/preprints_by_field_quarterly.csv"))))
    fields = [("physics", "Physics", OI["blue"]), ("mathematics", "Mathematics", OI["vermillion"]),
              ("biology_biorxiv", "Biology (bioRxiv)", OI["green"]),
              ("medicine_medrxiv_no_covid", "Medicine excl. COVID-19 (medRxiv)", OI["orange"]),
              ("social_sciences", "Social sciences", OI["purple"]),
              ("computer_science_reference", "Computer science", OI["grey"])]
    fig, ax = plt.subplots(figsize=(19.05 * CM, 10.5 * CM))
    style(ax)
    series = {}
    for key, _, _ in fields:
        base = sum(int(r[key]) for r in rows if r["quarter"].startswith("2022-")) / 4
        series[key] = {r["quarter"]: 100 * int(r[key]) / base for r in rows}
    index_lines(ax, series, [f[2] for f in fields], [f[1] for f in fields])
    ax.set_ylim(40, 310)
    ax.legend(loc="upper left", frameon=False, ncol=2, handlelength=1.6, columnspacing=1.2)
    fig.subplots_adjust(left=0.07, right=0.98, top=0.85, bottom=0.08)
    events(ax)
    save(fig, out, "Fig1")


def fig2(repo, out):
    bio = defaultdict(lambda: defaultdict(int))
    for r in csv.DictReader(open(os.path.join(repo, "data/raw/biorxiv_category_monthly.csv"))):
        bio[r["category"]][r["month"]] += int(r["new_papers"])
    sys.path.insert(0, os.path.join(repo, "scripts"))
    from stats_within_field import COMPUTATIONAL, EXPERIMENT, THEORY, WET_LAB, load_arxiv  # noqa: E402
    ax_ = load_arxiv(repo)
    agg = lambda src, keys: {m: sum(src[k].get(m, 0) for k in keys) for m in set().union(*[src[k] for k in keys])}  # noqa: E731
    mixed = [c for c in bio if c not in COMPUTATIONAL and c not in WET_LAB]
    phys = {"theory": quarterly_index(agg(ax_, THEORY)), "experiment": quarterly_index(agg(ax_, EXPERIMENT))}
    biol = {"computational": quarterly_index(agg(bio, COMPUTATIONAL)), "mixed": quarterly_index(agg(bio, mixed)),
            "wet": quarterly_index(agg(bio, WET_LAB))}
    med_path = os.path.join(repo, "data/raw/medrxiv_text_main.csv")
    med = None
    if os.path.exists(med_path):
        pub, rest = defaultdict(int), defaultdict(int)
        for r in csv.DictReader(open(med_path)):
            pub[r["month"]] += int(r["public_noncovid"])
            rest[r["month"]] += int(r["papers_noncovid"]) - int(r["public_noncovid"])
        med = {"public": quarterly_index(pub), "rest": quarterly_index(rest)}
    tests = json.load(open(os.path.join(repo, "data/processed/stats/within_field_tests.json")))["confirmatory"]

    fig, axes = plt.subplots(2, 2, figsize=(19.05 * CM, 15.5 * CM))
    (a, b), (c, d) = axes
    for ax in (a, b, c, d):
        style(ax)
    index_lines(a, phys, [OI["purple"], OI["green"]], ["Theory", "Experiment"])
    index_lines(b, biol, [OI["blue"], OI["grey"], OI["green"]], ["Computational", "Mixed", "Wet lab"])
    if med:
        index_lines(c, med, [OI["orange"], OI["grey"]], ["Names a public dataset", "Other preprints"])
    for ax, title in ((a, "Physics (arXiv)"), (b, "Biology (bioRxiv)"), (c, "Medicine excl. COVID-19 (medRxiv)")):
        ax.legend(loc="upper left", frameon=False, handlelength=1.6)
        ax.set_title(title, loc="left", pad=24)
    # D: event study (rate ratio of group A to group B by year, relative to 2022)
    style(d)
    d.axhline(1, color=AXIS, linewidth=0.6)
    spec = [("C1_physics_theory_vs_experiment", "Physics: theory / experiment", OI["purple"], -0.2),
            ("C2_biology_computational_vs_wetlab", "Biology: computational / wet lab", OI["blue"], 0.0),
            ("C3_medicine_public_dataset_vs_rest", "Medicine: public dataset / other", OI["orange"], 0.2)]
    for key, lab, col, off in spec:
        if key not in tests:
            continue
        ev = tests[key]["event_study"]
        ys = [int(y) for y in ev if int(y) >= 2019]
        d.errorbar([y + off for y in ys], [ev[str(y)]["rr"] for y in ys],
                   yerr=[[ev[str(y)]["rr"] - ev[str(y)]["lo"] for y in ys], [ev[str(y)]["hi"] - ev[str(y)]["rr"] for y in ys]],
                   fmt="o", color=col, markersize=3, elinewidth=0.9, capsize=1.5, label=lab)
    d.set_xticks(range(2019, 2027))
    d.set_xticklabels([str(y) if y < 2026 else "2026*" for y in range(2019, 2027)])
    d.set_ylabel("Rate ratio vs 2022 (95% CI)")
    d.set_yscale("log")
    d.yaxis.set_major_locator(mticker.FixedLocator([0.7, 0.8, 0.9, 1.0, 1.1, 1.25, 1.5, 2.0]))
    d.yaxis.set_major_formatter(mticker.FuncFormatter(lambda t, _: f"{t:g}"))
    d.yaxis.set_minor_locator(mticker.NullLocator())
    d.set_ylim(0.62, 1.5)
    d.legend(loc="lower left", frameon=False, handlelength=1.2)
    d.set_title("Group ratio by year, relative to 2022", loc="left", pad=24)
    for ax, s in zip((a, b, c, d), "ABCD"):
        panel_label(ax, s)
    fig.subplots_adjust(left=0.08, right=0.98, top=0.9, bottom=0.07, hspace=0.55, wspace=0.25)
    for ax in (a, b, c):
        events(ax, label=False)
    save(fig, out, "Fig2")


def fig3(repo, out):
    """Heavy producers (H2): concentration of output and per-paper share over time (maths, physics theory), and the
    growth of each author class between the third quarters of consecutive years."""
    path = os.path.join(repo, "data/processed/stats/heavy_producers.json")
    if not os.path.exists(path):
        return
    h = json.load(open(path))
    groups = [(g, lab, col) for g, lab, col in (("maths", "Maths", OI["vermillion"]),
                                                ("theory_max50_authors", "Physics theory", OI["purple"])) if g in h]
    short = {"Maths": "Maths", "Physics theory": "Theory"}
    variants = [("all_names", "all names", "-"), ("full_first_names_no_top1pct_surnames", "namesake-robust",
                                                  (0, (2.5, 1.5)))]
    fig, axes = plt.subplots(2, 2, figsize=(19.05 * CM, 13.5 * CM))
    (a, b), (c, d) = axes
    for ax in axes.flat:
        style(ax)
    for g, glab, col in groups:
        for vname, vlab, ls in variants:
            q = h[g][vname]["quarterly"]
            qs = [k for k in sorted(q) if "2019-Q1" <= k <= "2026-Q3"]
            x = [xq(k) for k in qs]
            lab = short[glab] + (", namesake-robust" if vname != "all_names" else ", all names")
            a.plot(x, [q[k]["top1pct_share_of_output"] for k in qs], color=col, linestyle=ls, linewidth=1.2, label=lab)
            b.plot(x, [q[k]["share_papers_with_heavy_author"] for k in qs], color=col, linestyle=ls, linewidth=1.2,
                   label=lab)
    for ax, title in ((a, "Share of output by the top 1% of authors"),
                      (b, "Papers with an author who has ≥5 papers that quarter")):
        ax.set_xlim(dt.date(2019, 1, 1), dt.date(2026, 12, 1))
        year_ticks(ax, 2019, 2026)
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda t, _: f"{100 * t:g}%"))
        ax.set_ylim(0, None)
        ax.set_title(title, loc="left", pad=6)
    a.legend(loc="lower left", frameon=False, handlelength=2.2, ncol=2, columnspacing=1.0)
    classes = [("top1pct", "Top 1%", OI["blue"]), ("next9pct", "Next 9%", OI["sky"]),
               ("bottom90pct", "Bottom 90%", OI["grey"])]
    for ax, (g, glab, col) in zip((c, d), groups):
        dec = h[g]["all_names"]["decomposition"]
        pairs = [k for k in dec if "Q3" in k]
        xs = range(len(pairs))
        w = 0.26
        for i, (key, lab, ccol) in enumerate(classes):
            ax.bar([x + (i - 1) * w for x in xs], [100 * dec[p][key]["growth"] for p in pairs], width=w, color=ccol,
                   label=lab, zorder=2)
        ax.scatter(list(xs), [100 * dec[p]["growth"] for p in pairs], marker="_", s=160, color=INK, linewidths=1.4,
                   zorder=3, label="All authors")
        ax.axhline(0, color=AXIS, linewidth=0.6, zorder=1)
        ax.axvspan(-0.5, 2.5, color="#f2f2f2", zorder=0)  # pairs that end before ChatGPT's release
        ax.text(1.0, 0.98, "Before ChatGPT", transform=ax.get_xaxis_transform(), ha="center", va="top", fontsize=8,
                color=INK2)
        ax.set_xticks(list(xs))
        ax.set_xticklabels([p[2:4] + "–" + p[-5:-3] for p in pairs])
        ax.set_xlabel("Years compared (third quarter)", labelpad=2)
        ax.set_xlim(-0.5, len(pairs) - 0.5)
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda t, _: f"{t:+.0f}%" if t else "0"))
        ax.set_title(f"{glab}: output growth by author class", loc="left", pad=6)
    for ax in (c, d)[len(groups):]:
        ax.set_visible(False)
    c.legend(loc="upper left", bbox_to_anchor=(0, 0.9), frameon=False, handlelength=1.4)
    for ax, s_ in zip(axes.flat, "ABCD"):
        panel_label(ax, s_, pad=6)
    fig.subplots_adjust(left=0.07, right=0.99, top=0.94, bottom=0.09, wspace=0.2, hspace=0.4)
    for ax in (a, b):
        events(ax, label=False, only={"ChatGPT"})
    save(fig, out, "Fig3")


def fig4(repo, out):
    """AI-writing marker rates by group and year (core Kobak style words per 100 abstracts, 2019-2022 = 1)."""
    path = os.path.join(repo, "data/processed/stats/marker_tests.json")
    if not os.path.exists(path):
        return
    m = json.load(open(path))["rates"]
    spec = [("biorxiv", "computational", "bioRxiv computational", OI["blue"], "-"),
            ("biorxiv", "mixed", "bioRxiv mixed", OI["grey"], "-"),
            ("biorxiv", "wet_lab", "bioRxiv wet lab", OI["green"], "-"),
            ("medrxiv", "all", "medRxiv", OI["orange"], "-"),
            ("arxiv", "maths", "arXiv maths", OI["vermillion"], (0, (3, 1.5))),
            ("arxiv", "theory", "arXiv physics theory", OI["purple"], (0, (3, 1.5))),
            ("arxiv", "experiment", "arXiv physics experiment", OI["sky"], (0, (3, 1.5)))]
    fig, ax = plt.subplots(figsize=(14 * CM, 8.5 * CM))
    style(ax)
    ax.axhline(1, color=AXIS, linewidth=0.6)
    for src, g, lab, col, ls in spec:
        if src not in m or g not in m[src]:
            continue
        v = m[src][g]
        ys = [int(y) for y in v if y.isdigit()]
        ax.plot(ys, [v[str(y)]["ratio_to_2019_2022"] for y in ys], color=col, linestyle=ls, linewidth=1.3,
                marker="o", markersize=2.5, label=lab)
    ax.set_xticks(range(2019, 2027))
    ax.set_xticklabels([str(y) if y < 2026 else "2026*" for y in range(2019, 2027)])
    ax.set_ylabel("Marker rate relative to 2019–2022")
    ax.legend(loc="upper left", frameon=False, handlelength=2.2, fontsize=8)
    fig.subplots_adjust(left=0.1, right=0.98, top=0.95, bottom=0.12)
    save(fig, out, "Fig4")


def main(repo):
    setup()
    out = os.path.join(repo, "docs/figures/plos")
    fig1(repo, out)
    fig2(repo, out)
    fig3(repo, out)
    fig4(repo, out)
    print("font:", FONT, "written:", sorted(os.listdir(out)))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
