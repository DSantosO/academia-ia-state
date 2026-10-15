"""Static PNG versions of the "Preprints por campo" charts.

Reads data/processed/preprints_por_campo_trimestral.csv and writes:
  docs/figures/indice_por_campo.png             index, 2022 = 100, one line per field
  docs/figures/preprints_por_campo_trimestral.png   quarterly counts, one panel per field
Usage: python3 scripts/plot_static.py [repo_dir]   (needs matplotlib)
"""
import csv
import datetime as dt
import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

SURFACE, INK, INK2, MUTED, GRID, AXIS = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
FIELDS = [  # key, label, colour (validated categorical slots 1-5)
    ("fisica", "Física", "#2a78d6"),
    ("matematicas", "Matemáticas", "#eb6834"),
    ("biologia_biorxiv", "Biología (bioRxiv)", "#1baf7a"),
    ("medicina_medrxiv", "Medicina (medRxiv)", "#eda100"),
    ("ciencias_sociales", "Ciencias sociales", "#e87ba4"),
]
REF = ("informatica_referencia", "Informática (referencia)", MUTED)
SHORT = {"informatica_referencia": "Informática (ref.)"}
CHATGPT = dt.date(2022, 11, 30)
ARXIV_RULES = dt.date(2025, 10, 31)
SOURCES = ("Fuentes: arXiv (archivo principal), bioRxiv, medRxiv, PsyArXiv, SocArXiv y EdArXiv (primeras versiones). "
           "Preprints nuevos por trimestre; datos del 15 oct 2026.")


def thousands(v):
    return f"{v:,.0f}".replace(",", " ")


def compact(v):
    if v >= 1000:
        s = f"{v / 1000:.1f}".rstrip("0").rstrip(".").replace(".", ",")
        return f"{s} mil"
    return thousands(v)


def mid(q):
    y, n = q.split("-T")
    return dt.date(int(y), 3 * (int(n) - 1) + 2, 15)


def style_axes(ax):
    ax.set_facecolor(SURFACE)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(AXIS)
    ax.tick_params(colors=MUTED, labelsize=9, length=0)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)


def spread(ys, gap):
    """Nudge label positions apart (keeping order) so none are closer than `gap`."""
    order = sorted(range(len(ys)), key=lambda i: ys[i])
    pos = [ys[i] for i in order]
    for _ in range(50):
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


def main(repo):
    rows = list(csv.DictReader(open(os.path.join(repo, "data/processed/preprints_por_campo_trimestral.csv"))))
    quarters = [r["trimestre"] for r in rows]
    x = [mid(q) for q in quarters]
    vals = {k: [int(r[k]) for r in rows] for k, _, _ in FIELDS + [REF]}
    base = {k: sum(v for q, v in zip(quarters, vals[k]) if q.startswith("2022-")) / 4 for k in vals}
    idx = {k: [100 * v / base[k] for v in vals[k]] for k in vals}
    out = os.path.join(repo, "docs/figures")
    os.makedirs(out, exist_ok=True)
    plt.rcParams.update({"font.family": "DejaVu Sans", "text.color": INK, "axes.labelcolor": INK2})

    # 1. Index chart
    fig, ax = plt.subplots(figsize=(10, 5.8), dpi=160)
    fig.patch.set_facecolor(SURFACE)
    style_axes(ax)
    ax.plot(x, idx[REF[0]], color=MUTED, linewidth=1.5, solid_capstyle="round", zorder=2)
    for k, _, c in FIELDS:
        ax.plot(x, idx[k], color=c, linewidth=2, solid_capstyle="round", solid_joinstyle="round", zorder=3)
        ax.plot(x[-1], idx[k][-1], "o", color=c, markersize=5, markeredgecolor=SURFACE, markeredgewidth=1.5, zorder=4)
    ax.axhline(100, color=AXIS, linewidth=1, zorder=1)
    ymax = max(max(v) for v in idx.values())
    ax.set_ylim(40, ymax * 1.08)
    for d, label in ((CHATGPT, "ChatGPT"), (ARXIV_RULES, "Normas de arXiv")):
        ax.axvline(d, color=MUTED, linewidth=1, linestyle=(0, (4, 3)), zorder=1)
        ax.text(d, ymax * 1.065, label, color=INK2, fontsize=9, ha="right", va="top", rotation=0,
                transform=ax.transData, bbox=dict(facecolor=SURFACE, edgecolor="none", pad=1.5))
    # direct end labels with leader lines
    series = FIELDS + [REF]
    ends = [idx[k][-1] for k, _, _ in series]
    gap = (ax.get_ylim()[1] - ax.get_ylim()[0]) * 0.055
    lab_y = spread(ends, gap)
    x_end = x[-1]
    x_lab = x_end + dt.timedelta(days=55)
    for (k, name, c), y_end, y_lab in zip(series, ends, lab_y):
        ax.plot([x_end + dt.timedelta(days=8), x_lab - dt.timedelta(days=6)], [y_end, y_lab], color=AXIS, linewidth=0.8)
        ax.text(x_lab, y_lab, f"{SHORT.get(k, name)}  {y_end:.0f}", color=INK, fontsize=9, va="center", ha="left")
    ax.set_xlim(dt.date(2020, 1, 1), dt.date(2028, 6, 1))
    ax.set_xticks([dt.date(y, 7, 1) for y in range(2020, 2027)])
    ax.set_xticklabels([str(y) for y in range(2020, 2027)])
    ax.spines["bottom"].set_bounds(mdates.date2num(dt.date(2020, 1, 1)), mdates.date2num(dt.date(2026, 10, 1)))
    fig.text(0.06, 0.95, "Preprints nuevos por campo (índice, 2022 = 100)", fontsize=14, color=INK, ha="left", weight="bold")
    fig.text(0.06, 0.905, "Cada trimestre frente a la media trimestral de 2022 del mismo campo. T1 2020 – T3 2026.",
             fontsize=10, color=INK2, ha="left")
    fig.text(0.06, 0.02, SOURCES, fontsize=7.5, color=MUTED, ha="left")
    fig.subplots_adjust(left=0.06, right=0.98, top=0.86, bottom=0.1)
    fig.savefig(os.path.join(out, "indice_por_campo.png"), facecolor=SURFACE)
    plt.close(fig)

    # 2. Small multiples of quarterly counts
    panels = FIELDS + [REF]
    fig, axes = plt.subplots(2, 3, figsize=(12, 6.8), dpi=150)
    fig.patch.set_facecolor(SURFACE)
    pos = list(range(len(quarters)))
    i_chatgpt = quarters.index("2023-T1") - 0.5
    for ax, (k, name, c) in zip(axes.flat, panels):
        style_axes(ax)
        v = vals[k]
        ax.bar(pos, v, width=0.72, color=c, zorder=2)
        ax.set_ylim(0, max(v) * 1.18)
        ax.yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(3))
        ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda t, _: compact(t)))
        ax.axvline(i_chatgpt, color=MUTED, linewidth=1, linestyle=(0, (4, 3)), zorder=1)
        ax.text(i_chatgpt - 0.4, max(v) * 1.16, "ChatGPT", fontsize=8, color=INK2, ha="right", va="top")
        ax.text(pos[-1], v[-1] + max(v) * 0.03, thousands(v[-1]), fontsize=8, color=INK, ha="center", va="bottom")
        firsts = [i for i, q in enumerate(quarters) if q.endswith("-T1")]
        ax.set_xticks([i + 1.5 for i in firsts])
        ax.set_xticklabels([quarters[i][:4] for i in firsts])
        ax.set_xlim(-0.8, len(quarters) - 0.2)
        change = sum(v[-4:]) / sum(x_ for q, x_ in zip(quarters, v) if q.startswith("2022-")) - 1
        ax.set_title(name, loc="left", fontsize=11, color=INK, pad=14)
        ax.text(0, 1.015, f"Último año vs 2022: {'+' if change >= 0 else '−'}{abs(change) * 100:.0f} %",
                transform=ax.transAxes, fontsize=8.5, color=INK2, ha="left", va="bottom")
    fig.text(0.02, 0.965, "Preprints nuevos por trimestre y campo", fontsize=14, color=INK, ha="left", weight="bold")
    fig.text(0.02, 0.93, "T1 2020 – T3 2026. Cada panel tiene su propia escala; «último año» = oct 2025 – sep 2026.",
             fontsize=10, color=INK2, ha="left")
    fig.text(0.02, 0.012, SOURCES, fontsize=7.5, color=MUTED, ha="left")
    fig.subplots_adjust(left=0.05, right=0.99, top=0.83, bottom=0.08, hspace=0.62, wspace=0.18)
    fig.savefig(os.path.join(out, "preprints_por_campo_trimestral.png"), facecolor=SURFACE)
    plt.close(fig)
    print("written:", sorted(os.listdir(out)))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
