"""Robustness checks for the "paper has an author with 5+ math papers that quarter" measure.

Works on the same OAI-PMH harvest as analyze_math.py and prints aggregated results only (no names):
  1. namesakes: full first names only; then also dropping the most frequent surnames
  2. concentration: authors by papers-per-quarter bins, and whether Q3 2026 prolific authors were active before
  3. team size: prolific share by number of authors
  4. cross-tab: AI-tool, Lean and Erdos mentions in prolific-author papers vs the rest
  5. subfields: where prolific-author papers sit in Q3 2026
  6. timing: prolific share by month
Usage: python3 scripts/robustness_math_prolific.py out.json harvest1.jsonl.gz [...]
"""
import gzip
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from analyze_math import AI_TOOLS, ERDOS, LEAN  # noqa: E402


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z ]", " ", s).split()


def load(files):
    papers = {}
    for fn in files:
        with gzip.open(fn, "rt", encoding="utf-8") as f:
            for line in f:
                r = json.loads(line)
                m = re.fullmatch(r"(\d{2})(\d{2})\.\d{4,5}", r["id"] or "")
                if not (m and m.group(1) + m.group(2) >= "2501" and r["categories"]
                        and r["categories"][0].startswith("math.")):
                    continue
                month = f"20{m.group(1)}-{m.group(2)}"
                authors = []
                for a in r["authors"]:
                    toks = norm(a)
                    if toks:
                        authors.append((" ".join(toks), toks[-1], len(toks[0]) > 1 and len(toks) > 1))
                text = " ".join(filter(None, [r.get("title"), r.get("abstract"), r.get("comments")]))
                papers[r["id"]] = {
                    "month": month, "quarter": f"{month[:4]}-Q{(int(month[5:]) - 1) // 3 + 1}",
                    "authors": authors, "cat": r["categories"][0],
                    "ai": bool(AI_TOOLS.search(text)), "lean": bool(LEAN.search(text)), "erdos": bool(ERDOS.search(text)),
                }
    return list(papers.values())


def prolific_share(papers, quarters, keep=lambda a: True, threshold=5):
    cnt = Counter()
    for p in papers:
        for name in {a[0] for a in p["authors"] if keep(a)}:
            cnt[(name, p["quarter"])] += 1
    out = {}
    for q in quarters:
        ps = [p for p in papers if p["quarter"] == q]
        hit = sum(any(keep(a) and cnt[(a[0], q)] >= threshold for a in p["authors"]) for p in ps)
        out[q] = round(hit / len(ps), 4) if ps else None
    return out, cnt


def main():
    out_path, files = sys.argv[1], sys.argv[2:]
    papers = load(files)
    quarters = ["2025-Q1", "2025-Q2", "2025-Q3", "2025-Q4", "2026-Q1", "2026-Q2", "2026-Q3"]
    res = {"papers_by_quarter": dict(Counter(p["quarter"] for p in papers))}

    base, cnt = prolific_share(papers, quarters)
    res["1_baseline_share"] = base
    res["1_full_first_names_share"] = prolific_share(papers, quarters, keep=lambda a: a[2])[0]
    surnames = Counter(a[1] for p in papers for a in p["authors"])
    ranked = [s for s, _ in surnames.most_common()]
    for pct in (1, 2):
        top = set(ranked[: max(1, len(ranked) * pct // 100)])
        res[f"1_full_first_names_drop_top{pct}pct_surnames_share"] = prolific_share(
            papers, quarters, keep=lambda a, t=top: a[2] and a[1] not in t)[0]
        res[f"1_top{pct}pct_surnames_count"] = len(top)
        res[f"1_top{pct}pct_surnames_author_slot_share"] = round(
            sum(surnames[s] for s in top) / sum(surnames.values()), 4)

    bins = [(5, 9), (10, 19), (20, 49), (50, 10 ** 6)]
    conc = {}
    for q in ("2025-Q3", "2026-Q3"):
        per = [v for (n, qq), v in cnt.items() if qq == q]
        conc[q] = {f"{a}-{b if b < 10 ** 6 else '+'}": sum(a <= v <= b for v in per) for a, b in bins}
        conc[q]["authors_total"] = len(per)
    prolific26 = {n for (n, q), v in cnt.items() if q == "2026-Q3" and v >= 5}
    earlier = defaultdict(int)
    for (n, q), v in cnt.items():
        if q < "2026-Q3":
            earlier[n] = max(earlier[n], v)
    conc["2026-Q3_prolific_authors_by_history"] = {
        "already_5plus_in_an_earlier_quarter": sum(earlier[n] >= 5 for n in prolific26),
        "active_earlier_but_below_5": sum(0 < earlier[n] < 5 for n in prolific26),
        "no_math_paper_since_Jan_2025": sum(earlier[n] == 0 for n in prolific26),
    }
    papers_by_new_prolific = Counter()
    for p in papers:
        if p["quarter"] == "2026-Q3":
            names = {a[0] for a in p["authors"]}
            if names & prolific26:
                papers_by_new_prolific["any_prolific"] += 1
                if any(n in prolific26 and earlier[n] < 5 for n in names):
                    papers_by_new_prolific["with_newly_prolific_author"] += 1
    conc["2026-Q3_papers_with_prolific_author"] = dict(papers_by_new_prolific)
    res["2_concentration"] = conc

    def is_prolific(p):
        return any(cnt[(a[0], p["quarter"])] >= 5 for a in p["authors"])

    team = {}
    for q in ("2025-Q3", "2026-Q3"):
        team[q] = {}
        for label, lo, hi in (("1", 1, 1), ("2", 2, 2), ("3", 3, 3), ("4-5", 4, 5), ("6+", 6, 10 ** 6)):
            ps = [p for p in papers if p["quarter"] == q and lo <= len(p["authors"]) <= hi]
            team[q][label] = {"papers": len(ps), "prolific_share": round(sum(map(is_prolific, ps)) / len(ps), 4) if ps else None}
    res["3_team_size"] = team

    cross = {}
    for q in ("2025-Q3", "2026-Q3"):
        cross[q] = {}
        for grp, sel in (("prolific", True), ("other", False)):
            ps = [p for p in papers if p["quarter"] == q and is_prolific(p) == sel]
            cross[q][grp] = {"papers": len(ps), **{k: round(sum(p[k] for p in ps) / len(ps), 4) for k in ("ai", "lean", "erdos")}}
    res["4_crosstab"] = cross

    subs = Counter(p["cat"] for p in papers if p["quarter"] == "2026-Q3" and is_prolific(p))
    tot = Counter(p["cat"] for p in papers if p["quarter"] == "2026-Q3")
    res["5_subfields_2026Q3"] = [
        {"subcategory": c, "prolific_papers": n, "share_within_subfield": round(n / tot[c], 4)} for c, n in subs.most_common(12)]

    months = sorted({p["month"] for p in papers})
    res["6_monthly_prolific_share"] = {
        m: round(sum(map(is_prolific, [p for p in papers if p["month"] == m])) /
                 max(1, sum(p["month"] == m for p in papers)), 4) for m in months}
    json.dump(res, open(out_path, "w"), indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
