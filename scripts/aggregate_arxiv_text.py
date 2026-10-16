"""Aggregate title+abstract word features of arXiv papers by month and primary archive (same format as
harvest_rxiv_text_features.py), from OAI-PMH harvests (harvest_arxiv_oai.py).

Papers are dated by identifier (YYMM) and kept from January 2019; each paper counts once, under its primary category's
archive (math.* -> "math"). Writes <out>_main.csv (month, category, papers, words) and <out>_words.csv
(month, category, word, docs) for the style words of Kobak et al. 2025 (data/raw/kobak_style_words.csv), plus
<out>_core_any.csv with the number of papers containing at least one core marker word (core list given by
--core words.txt, optional).
Usage: python3 scripts/aggregate_arxiv_text.py data/raw/arxiv_text in1.jsonl.gz [in2.jsonl.gz ...] [--core core.txt]
"""
import csv
import gzip
import json
import os
import re
import sys
from collections import Counter, defaultdict

TOKEN = re.compile(r"[a-z]+")
STYLE = {r["word"] for r in csv.DictReader(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                                              "data", "raw", "kobak_style_words.csv")))}


def main():
    args = sys.argv[1:]
    core = None
    if "--core" in args:
        i = args.index("--core")
        core = {w.strip() for w in open(args[i + 1]) if w.strip()}
        args = args[:i] + args[i + 2:]
    out, files = args[0], args[1:]
    seen = set()
    main_, words, core_any = defaultdict(Counter), defaultdict(Counter), Counter()
    for fn in files:
        with gzip.open(fn, "rt", encoding="utf-8") as f:
            for line in f:
                r = json.loads(line)
                m = re.fullmatch(r"(\d{2})(\d{2})\.\d{4,5}", r.get("id") or "")
                if not m or r["id"] in seen or not r.get("categories") or m.group(1) + m.group(2) < "1901":
                    continue
                seen.add(r["id"])
                prim = r["categories"][0]
                arch = "math" if prim.startswith("math.") else prim.split(".")[0]
                key = (f"20{m.group(1)}-{m.group(2)}", arch)
                tokens = TOKEN.findall(((r.get("title") or "") + " " + (r.get("abstract") or "")).lower())
                main_[key]["papers"] += 1
                main_[key]["words"] += len(tokens)
                present = STYLE.intersection(tokens)
                for w in present:
                    words[key][w] += 1
                if core is not None and core.intersection(tokens):
                    core_any[key] += 1
    with open(out + "_main.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["month", "category", "papers", "words"])
        for (mo, cat), c in sorted(main_.items()):
            w.writerow([mo, cat, c["papers"], c["words"]])
    with open(out + "_words.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["month", "category", "word", "docs"])
        for (mo, cat), c in sorted(words.items()):
            for word, n in sorted(c.items()):
                w.writerow([mo, cat, word, n])
    if core is not None:
        with open(out + "_core_any.csv", "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["month", "category", "papers_with_core_marker"])
            for (mo, cat), n in sorted(core_any.items()):
                w.writerow([mo, cat, n])
    print("papers", len(seen))


if __name__ == "__main__":
    main()
