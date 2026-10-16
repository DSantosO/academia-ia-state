"""Aggregate text features of new bioRxiv or medRxiv preprints by month and subject category.

Pages the api.biorxiv.org details endpoint one day at a time (short cursors keep calls fast) and keeps version-1
preprints only. For each month and category it writes aggregate counts, never individual records:
  <out>_main.csv   month, category, papers, covid, public, public_noncovid, papers_noncovid, words_noncovid
  <out>_words.csv  month, category, word, docs_noncovid   (style words of Kobak et al. 2025, documents containing them)
covid: COVID_RE in title or abstract; public: PUBLIC_RE (named public datasets or designs often reused in formulaic
papers). Word features use title + abstract of non-COVID preprints, lower-cased and split on non-letters.
Style words: data/raw/kobak_style_words.csv (berenslab/llm-excess-vocab, results/excess_words.csv, type "style").
Usage:
  python3 scripts/harvest_rxiv_text_features.py medrxiv 2019-06 2026-09 data/raw/medrxiv_text [workers] [--months 3,9]
"""
import calendar
import csv
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harvest_rxiv_categories import COVID_RE, PUBLIC_RE  # noqa: E402

UA = "academia-ia-state research"
TOKEN = re.compile(r"[a-z]+")
STYLE = {r["word"] for r in csv.DictReader(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                                              "data", "raw", "kobak_style_words.csv")))}


def get(url):
    for attempt in range(8):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=120) as r:
                return json.load(r)
        except Exception:
            time.sleep(5 * (attempt + 1))
    raise RuntimeError(url)


def harvest_day(server, day):
    main, words = defaultdict(Counter), defaultdict(Counter)
    cursor, total = 0, None
    while total is None or cursor < total:
        j = get(f"https://api.biorxiv.org/details/{server}/{day}/{day}/{cursor}")
        msg = j["messages"][0]
        if msg.get("status") != "ok":
            break
        total = int(msg.get("total", 0))
        coll = j.get("collection", [])
        for p in coll:
            if str(p.get("version")) != "1":
                continue
            cat = (p.get("category") or "unknown").strip().lower()
            text = (p.get("title") or "") + " " + (p.get("abstract") or "")
            m = main[cat]
            m["papers"] += 1
            covid = bool(COVID_RE.search(text))
            public = bool(PUBLIC_RE.search(text))
            m["covid"] += covid
            m["public"] += public
            if not covid:
                m["public_noncovid"] += public
                m["papers_noncovid"] += 1
                tokens = TOKEN.findall(text.lower())
                m["words_noncovid"] += len(tokens)
                for w in STYLE.intersection(tokens):
                    words[cat][w] += 1
        if not coll:
            break
        cursor += len(coll)
    return main, words


def harvest_month(server, ym):
    y, m = map(int, ym.split("-"))
    main, words = defaultdict(Counter), defaultdict(Counter)
    for d in range(1, calendar.monthrange(y, m)[1] + 1):
        dm, dw = harvest_day(server, f"{y}-{m:02d}-{d:02d}")
        for c, cnt in dm.items():
            main[c].update(cnt)
        for c, cnt in dw.items():
            words[c].update(cnt)
    print(server, ym, sum(c["papers"] for c in main.values()), "papers", dt.datetime.now().strftime("%H:%M:%S"),
          flush=True)
    return ym, main, words


def months(a, b, keep=None):
    y, m = map(int, a.split("-"))
    while f"{y}-{m:02d}" <= b:
        if keep is None or m in keep:
            yield f"{y}-{m:02d}"
        m += 1
        if m == 13:
            y, m = y + 1, 1


def main():
    args = sys.argv[1:]
    keep = None
    if "--months" in args:
        i = args.index("--months")
        keep = {int(x) for x in args[i + 1].split(",")}
        args = args[:i] + args[i + 2:]
    server, a, b, out = args[:4]
    workers = int(args[4]) if len(args) > 4 else 6
    fields = ["papers", "covid", "public", "public_noncovid", "papers_noncovid", "words_noncovid"]
    with ThreadPoolExecutor(workers) as ex:
        results = list(ex.map(lambda ym: harvest_month(server, ym), months(a, b, keep)))
    with open(out + "_main.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["month", "category"] + fields)
        for ym, main_, _ in results:
            for c in sorted(main_):
                w.writerow([ym, c] + [main_[c][k] for k in fields])
    with open(out + "_words.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["month", "category", "word", "docs_noncovid"])
        for ym, _, words_ in results:
            for c in sorted(words_):
                for word, n in sorted(words_[c].items()):
                    w.writerow([ym, c, word, n])
    print("done", len(results), "months")


if __name__ == "__main__":
    main()
