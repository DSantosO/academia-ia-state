"""Profile new arXiv mathematics papers by month (2025 onwards) from an OAI-PMH harvest.

Input: one or more gzipped JSON-lines files written by harvest_arxiv_oai.py (set "math").
Outputs (data/processed/):
  arxiv_math_monthly_profile.csv     per month: papers, AI-tool mentions, Erdos mentions, Lean mentions,
                                     single-author share, first-time-author share, prolific-author share
  arxiv_math_subcategories.csv       papers per primary subcategory, Q3 2025 vs Q3 2026
A paper is "math" when its primary (first-listed) category starts with "math.". It counts in the month of
its first version, read from the arXiv identifier (YYMM.NNNNN), because the OAI <created> field is not always
the first-version date. Only identifiers from 2501 onwards are kept.
Usage: python3 scripts/analyze_math.py out_dir harvest1.jsonl.gz [harvest2.jsonl.gz ...]
"""
import csv
import gzip
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

AI_TOOLS = re.compile(
    r"\b(chat ?gpt|gpt-?\d(\.\d)?|o[134](-mini|-pro)?\b|openai|claude|anthropic|gemini|deepseek|grok|qwen|"
    r"alphaproof|alphaevolve|alphageometry|large language models?|llms?|ai[- ]assisted|ai[- ]generated|"
    r"generative ai|ai (tools?|assistants?|systems?|models?)|with the (help|assistance) of (an? )?ai)\b", re.I)
ERDOS = re.compile(r"erd(?:o|ö|ő|\\h\{?o\}?|\\\"\{?o\}?)s", re.I)
LEAN = re.compile(r"\bLean ?4\b|\bMathlib\b|\bin Lean\b|\bLean proof|\bLean formali", re.I)


def norm(name):
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z ]", "", s).strip()


def main():
    out_dir, files = sys.argv[1], sys.argv[2:]
    papers = {}
    for fn in files:
        with gzip.open(fn, "rt", encoding="utf-8") as f:
            for line in f:
                r = json.loads(line)
                m = re.fullmatch(r"(\d{2})(\d{2})\.\d{4,5}", r["id"] or "")
                if m and m.group(1) + m.group(2) >= "2501" and r["categories"] and r["categories"][0].startswith("math."):
                    r["month"] = f"20{m.group(1)}-{m.group(2)}"
                    papers[r["id"]] = r
    rows = sorted(papers.values(), key=lambda r: r["id"])
    seen_authors = set()
    by_month = defaultdict(Counter)
    author_quarter = Counter()
    sub_q = defaultdict(Counter)
    quarter_of = lambda m: f"{m[:4]}-Q{(int(m[5:7]) - 1) // 3 + 1}"
    for r in rows:
        authors = [norm(a) for a in r["authors"] if norm(a)]
        for a in set(authors):
            author_quarter[(a, quarter_of(r["month"]))] += 1
    for r in rows:
        m, q = r["month"], quarter_of(r["month"])
        text = " ".join(filter(None, [r.get("title"), r.get("abstract"), r.get("comments")]))
        authors = [norm(a) for a in r["authors"] if norm(a)]
        c = by_month[m]
        c["papers"] += 1
        c["ai_tool_mention"] += bool(AI_TOOLS.search(text))
        c["erdos_mention"] += bool(ERDOS.search(text))
        c["lean_mention"] += bool(LEAN.search(text))
        c["single_author"] += len(authors) == 1
        c["all_authors_first_time"] += bool(authors) and all(a not in seen_authors for a in authors)
        c["prolific_author"] += any(author_quarter[(a, q)] >= 5 for a in authors)
        seen_authors.update(authors)
        sub_q[r["categories"][0]][q] += 1
    os.makedirs(out_dir, exist_ok=True)
    keys = ["papers", "ai_tool_mention", "erdos_mention", "lean_mention", "single_author",
            "all_authors_first_time", "prolific_author"]
    with open(os.path.join(out_dir, "arxiv_math_monthly_profile.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["month"] + keys)
        for m in sorted(by_month):
            w.writerow([m] + [by_month[m][k] for k in keys])
    with open(os.path.join(out_dir, "arxiv_math_subcategories.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["subcategory", "q3_2025", "q3_2026", "change"])
        for s in sorted(sub_q, key=lambda s: -sub_q[s]["2026-Q3"]):
            a, b = sub_q[s]["2025-Q3"], sub_q[s]["2026-Q3"]
            w.writerow([s, a, b, f"{(b / a - 1):.4f}" if a else ""])
    print(len(rows), "math papers;", rows[0]["month"], "to", rows[-1]["month"])


if __name__ == "__main__":
    main()
