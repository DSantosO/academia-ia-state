"""Split new arXiv computer-science papers into AI research and the rest, by quarter (2020 onwards).

Input: gzipped JSON-lines files written by harvest_arxiv_oai.py for the set "cs".
A paper counts in the quarter of its first version, read from its arXiv identifier (YYMM.NNNNN), and in the
field of its primary (first-listed) category. Three groups:
  ai_categories   primary category is an AI/ML category (AI_CATEGORIES)
  ai_text_other   other CS category, but the title or abstract uses AI/ML vocabulary (AI_TEXT)
  non_ai          everything else
Outputs (data/processed/):
  arxiv_cs_ai_split_quarterly.csv      quarter, start, cs_total, ai_categories, ai_text_other, non_ai
  arxiv_cs_categories_quarterly.csv    quarter, category, papers, ai_text   (long format, every primary cs.*)
Usage: python3 scripts/analyze_cs_ai.py out_dir harvest1.jsonl.gz [harvest2.jsonl.gz ...]
"""
import csv
import gzip
import json
import os
import re
import sys
from collections import Counter, defaultdict

AI_CATEGORIES = {"cs.AI", "cs.LG", "cs.CL", "cs.CV", "cs.NE", "cs.MA"}
AI_TEXT = re.compile(
    r"\b(artificial intelligence|machine[- ]learning|deep[- ]learning|neural (?:networks?|models?|architectures?)|"
    r"large language models?|small language models?|language models?|llms?|vlms?|chat ?gpt|gpt-?\d(?:\.\d)?o?|"
    r"generative (?:ai|models?|pre-?trained)|foundation models?|diffusion models?|transformer(?:s|-based)?|"
    r"reinforcement learning|computer vision|natural language processing|vision[- ]language|"
    r"graph neural networks?|convolutional|self-supervised|federated learning|fine-?tun(?:e|ed|ing)|"
    r"pre-?trained models?|prompt(?:s|ing)? (?:engineering|injection|tuning)|in-context learning|"
    r"(?:ai|llm|llm-based|autonomous) agents?|agentic|retrieval-augmented)\b", re.I)


def quarter_start(q):
    y, n = q.split("-Q")
    return f"{y}-{3 * (int(n) - 1) + 1:02d}-01"


def main():
    out_dir, files = sys.argv[1], sys.argv[2:]
    papers = {}
    for fn in files:
        with gzip.open(fn, "rt", encoding="utf-8") as f:
            for line in f:
                r = json.loads(line)
                m = re.fullmatch(r"(\d{2})(\d{2})\.\d{4,5}", r["id"] or "")
                if not (m and m.group(1) + m.group(2) >= "2001" and r["categories"]):
                    continue
                if not r["categories"][0].startswith("cs."):
                    continue
                quarter = f"20{m.group(1)}-Q{(int(m.group(2)) - 1) // 3 + 1}"
                text = " ".join(filter(None, [r.get("title"), r.get("abstract")]))
                papers[r["id"]] = (quarter, r["categories"][0], bool(AI_TEXT.search(text)))
    split = defaultdict(Counter)
    cats = defaultdict(Counter)
    for quarter, cat, ai_text in papers.values():
        s = split[quarter]
        s["cs_total"] += 1
        if cat in AI_CATEGORIES:
            s["ai_categories"] += 1
        elif ai_text:
            s["ai_text_other"] += 1
        else:
            s["non_ai"] += 1
        cats[(quarter, cat)]["papers"] += 1
        cats[(quarter, cat)]["ai_text"] += ai_text
    os.makedirs(out_dir, exist_ok=True)
    keys = ["cs_total", "ai_categories", "ai_text_other", "non_ai"]
    with open(os.path.join(out_dir, "arxiv_cs_ai_split_quarterly.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["quarter", "start"] + keys)
        for q in sorted(split):
            w.writerow([q, quarter_start(q)] + [split[q][k] for k in keys])
    with open(os.path.join(out_dir, "arxiv_cs_categories_quarterly.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["quarter", "category", "papers", "ai_text"])
        for (q, c) in sorted(cats):
            w.writerow([q, c, cats[(q, c)]["papers"], cats[(q, c)]["ai_text"]])
    print(len(papers), "cs papers in", len(split), "quarters")


if __name__ == "__main__":
    main()
