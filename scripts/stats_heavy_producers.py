"""Heavy producers in arXiv mathematics and in theoretical vs experimental physics (PLOS ONE analysis, Priority 2).

Input: gzipped JSON-lines harvests from harvest_arxiv_oai.py (math:math and physics:<archive> sets since 2019).
Papers are dated by the month of their identifier (YYMM) and assigned to a group by primary category:
  maths: math.*;  theory: hep-th, hep-ph, gr-qc, nucl-th;  experiment: hep-ex, nucl-ex.
Authors are matched by normalised name strings (ASCII-folded, lower-case tokens), as arXiv has no author IDs.

Measures by quarter (and for January-August windows, to compare with Nee, Zhong & Ni 2026):
  per paper   share of papers with at least one author who has >=5 papers in the group that quarter
  CIs: Wilson intervals and two-proportion z-tests treating papers (or authors) as independent units. Papers that
  share authors are not independent, so these intervals are too narrow; they are reported as a guide only.
  A bootstrap of papers was tried and dropped: duplicated papers inflate author counts and bias the share upward.
  per author  share of active authors with >=5 and >=10 papers (and >=15 per quarter, roughly >60 a year)
  output      fractional output (each paper split equally among its authors); share of the change in fractional
              output from Q3 2025 to Q3 2026 contributed by authors with >=5 papers in Q3 2026 ("heavy producers"),
              and by the top 1% of authors by fractional output
Namesake-robust variants: full first names only; full first names with the 1% most frequent surnames removed.
Physics also reports a version without papers that have more than 50 authors (collaboration papers).
Usage: python3 scripts/stats_heavy_producers.py out.json maths=math.jsonl.gz physics=hep-th.jsonl.gz,hep-ex.jsonl.gz,...
"""
import gzip
import json
import math
import re
import sys
import unicodedata
from collections import Counter, defaultdict

import numpy as np

RNG = np.random.default_rng(20261016)
THEORY = {"hep-th", "hep-ph", "gr-qc", "nucl-th"}
EXPERIMENT = {"hep-ex", "nucl-ex"}


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z ]", " ", s).split()


def load(files, group_of):
    papers = {}
    for fn in files:
        with gzip.open(fn, "rt", encoding="utf-8") as f:
            for line in f:
                r = json.loads(line)
                m = re.fullmatch(r"(\d{2})(\d{2})\.\d{4,5}", r.get("id") or "")
                if not m or not r.get("categories") or m.group(1) + m.group(2) < "1901":
                    continue
                g = group_of(r["categories"][0])
                if not g or r["id"] in papers:
                    continue
                month = f"20{m.group(1)}-{m.group(2)}"
                authors = []
                for a in r.get("authors") or []:
                    toks = norm(a)
                    if toks:
                        authors.append((" ".join(toks), toks[-1], len(toks[0]) > 1 and len(toks) > 1))
                papers[r["id"]] = {"group": g, "month": month, "quarter": f"{month[:4]}-Q{(int(month[5:]) - 1) // 3 + 1}",
                                   "authors": authors}
    return list(papers.values())


def per_quarter(papers, key, keep=lambda a: True, threshold=5):
    """Return per-period stats for one group; key(p) gives the period label."""
    by = defaultdict(list)
    for p in papers:
        by[key(p)].append(p)
    out = {}
    for period, ps in sorted(by.items()):
        names = [[a[0] for a in p["authors"] if keep(a)] for p in ps]
        cnt = Counter(n for ns in names for n in set(ns))
        active = len(cnt)
        heavy_paper = np.array([any(cnt[n] >= threshold for n in ns) for ns in names])
        frac = Counter()
        for ns in names:
            for n in set(ns):
                frac[n] += 1 / len(set(ns))
        out[period] = {
            "papers": len(ps), "active_authors": active,
            "share_papers_with_heavy_author": float(heavy_paper.mean()) if len(ps) else None,
            "share_authors_ge5": sum(v >= 5 for v in cnt.values()) / active if active else None,
            "share_authors_ge10": sum(v >= 10 for v in cnt.values()) / active if active else None,
            "share_authors_ge15": sum(v >= 15 for v in cnt.values()) / active if active else None,
            "authors_ge5": sum(v >= 5 for v in cnt.values()),
            "_cnt": cnt, "_frac": frac, "_names": names,
        }
    return out


def wilson(k, n, z=1.96):
    if not n:
        return None
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return [c - h, c + h]


def two_prop(k1, n1, k2, n2):
    p = (k1 + k2) / (n1 + n2)
    se = math.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    z = (k2 / n2 - k1 / n1) / se if se else float("nan")
    return {"diff": k2 / n2 - k1 / n1, "z": z, "p": math.erfc(abs(z) / math.sqrt(2))}


def contribution(stats, a, b, threshold=5):
    """Share of the change in fractional output between periods a and b contributed by heavy producers in b,
    and by the top 1% of authors (by fractional output in b)."""
    fa, fb, cb = stats[a]["_frac"], stats[b]["_frac"], stats[b]["_cnt"]
    total_change = sum(fb.values()) - sum(fa.values())
    heavy = {n for n, v in cb.items() if v >= threshold}
    top = set(sorted(fb, key=fb.get, reverse=True)[: max(1, len(fb) // 100)])
    ch = lambda s: sum(fb.get(n, 0) for n in s) - sum(fa.get(n, 0) for n in s)  # noqa: E731
    return {"fractional_output_a": sum(fa.values()), "fractional_output_b": sum(fb.values()),
            "change": total_change,
            "share_of_change_from_heavy_producers_in_b": ch(heavy) / total_change if total_change else None,
            "share_of_output_b_by_heavy_producers": sum(fb[n] for n in heavy) / sum(fb.values()),
            "share_of_change_from_top1pct_in_b": ch(top) / total_change if total_change else None,
            "share_of_output_b_by_top1pct": sum(fb[n] for n in top) / sum(fb.values())}


def clean(stats):
    return {k: {kk: vv for kk, vv in v.items() if not kk.startswith("_")} for k, v in stats.items()}


def analyse(papers, label):
    surnames = Counter(a[1] for p in papers for a in p["authors"])
    top1 = set(s for s, _ in surnames.most_common(max(1, len(surnames) // 100)))
    variants = {"all_names": lambda a: True, "full_first_names": lambda a: a[2],
                "full_first_names_no_top1pct_surnames": lambda a: a[2] and a[1] not in top1}
    res = {}
    for vname, keep in variants.items():
        q = per_quarter(papers, lambda p: p["quarter"], keep)
        janaug = per_quarter([p for p in papers if p["month"][5:] <= "08"], lambda p: p["month"][:4] + "-JanAug", keep)
        for st in (q, janaug):
            for v in st.values():
                if v["share_papers_with_heavy_author"] is None or not v["active_authors"]:
                    continue
                kp = round(v["share_papers_with_heavy_author"] * v["papers"])
                v["share_papers_with_heavy_author_ci"] = wilson(kp, v["papers"])
                for t in ("ge5", "ge10"):
                    k = round(v[f"share_authors_{t}"] * v["active_authors"])
                    v[f"share_authors_{t}_ci"] = wilson(k, v["active_authors"])
        tests = {}
        for a, b, st in (("2025-Q3", "2026-Q3", q), ("2025-JanAug", "2026-JanAug", janaug)):
            if a in st and b in st and st[a]["active_authors"] and st[b]["active_authors"]:
                A, B = st[a], st[b]
                tests[f"{a}_vs_{b}"] = {
                    "per_paper": two_prop(round(A["share_papers_with_heavy_author"] * A["papers"]), A["papers"],
                                          round(B["share_papers_with_heavy_author"] * B["papers"]), B["papers"]),
                    "authors_ge5": two_prop(A["authors_ge5"], A["active_authors"], B["authors_ge5"],
                                            B["active_authors"]),
                    "authors_ge10": two_prop(round(A["share_authors_ge10"] * A["active_authors"]), A["active_authors"],
                                             round(B["share_authors_ge10"] * B["active_authors"]),
                                             B["active_authors"])}
        res[vname] = {"quarterly": clean(q), "jan_aug": clean(janaug), "tests": tests}
        if "2025-Q3" in q and "2026-Q3" in q:
            res[vname]["contribution_Q3_2025_to_Q3_2026"] = contribution(q, "2025-Q3", "2026-Q3")
    print(label, "papers:", len(papers), flush=True)
    return res


def main():
    out = sys.argv[1]
    specs = dict(arg.split("=", 1) for arg in sys.argv[2:])
    results = {}
    if "maths" in specs:
        ps = load(specs["maths"].split(","), lambda c: "maths" if c.startswith("math.") else None)
        results["maths"] = analyse(ps, "maths")
    if "physics" in specs:
        files = specs["physics"].split(",")
        grp = lambda c: "theory" if c in THEORY else "experiment" if c in EXPERIMENT else None  # noqa: E731
        ps = load(files, grp)
        for g in ("theory", "experiment"):
            sub = [p for p in ps if p["group"] == g]
            results[g] = analyse(sub, g)
            results[g + "_max50_authors"] = analyse([p for p in sub if len(p["authors"]) <= 50], g + " <=50 authors")
    json.dump(results, open(out, "w"), indent=1, default=float)


if __name__ == "__main__":
    main()
