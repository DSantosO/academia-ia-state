"""Monthly listings of arXiv papers by first-version submission date (arXiv API submittedDate), for the held-out
archives of the new-data test (cond-mat, astro-ph, quant-ph), January 2017 to September 2026.

For each archive and month, all papers listed in any of the archive's categories and submitted (version 1) in the
month are read in pages of 2000, and those whose primary category belongs to the archive are kept.
Writes OUT_DIR/<archive>.jsonl.gz (id, v1 submission date, primary category, number of authors, title, abstract,
comments; kept outside the repository) and data/raw/arxiv_heldout_monthly.csv (archive, primary category, month,
papers). Resumes from the months already in OUT_DIR/<archive>.done.
Pacing: arXiv API terms, one request every 3 s over one connection; run when no other arXiv harvest is running.
Usage: python3 scripts/harvest_arxiv_api_months.py OUT_DIR [repo_dir]
"""
import calendar
import csv
import gzip
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter

UA = "academia-ia-state research"
NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom",
      "os": "http://a9.com/-/spec/opensearch/1.1/"}
CATS = {"cond-mat": ["cond-mat.dis-nn", "cond-mat.mes-hall", "cond-mat.mtrl-sci", "cond-mat.other",
                     "cond-mat.quant-gas", "cond-mat.soft", "cond-mat.stat-mech", "cond-mat.str-el", "cond-mat.supr-con"],
        "astro-ph": ["astro-ph.CO", "astro-ph.EP", "astro-ph.GA", "astro-ph.HE", "astro-ph.IM", "astro-ph.SR"],
        "quant-ph": ["quant-ph"]}
PAGE = 2000


def fetch(query, start):
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": query, "start": start, "max_results": PAGE, "sortBy": "submittedDate", "sortOrder": "ascending"})
    for attempt in range(8):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=300) as r:
                root = ET.fromstring(r.read())
            total = int(root.find("os:totalResults", NS).text)
            entries = root.findall("a:entry", NS)
            if entries or start >= total:
                return total, entries
        except Exception:
            pass
        time.sleep(15 * (attempt + 1))  # the API sometimes returns an empty page; wait and retry
    raise RuntimeError(f"failed: {query} start={start}")


def months(a="2017-01", b="2026-09"):
    y, m = map(int, a.split("-"))
    while f"{y}-{m:02d}" <= b:
        yield y, m
        m += 1
        if m == 13:
            y, m = y + 1, 1


def main(out_dir, repo="."):
    os.makedirs(out_dir, exist_ok=True)
    for arch, cats in CATS.items():
        done_path = os.path.join(out_dir, f"{arch}.done")
        done = set(open(done_path).read().split()) if os.path.exists(done_path) else set()
        for y, m in months():
            ym = f"{y}-{m:02d}"
            if ym in done:
                continue
            last = calendar.monthrange(y, m)[1]
            q = "(" + " OR ".join(f"cat:{c}" for c in cats) + f") AND submittedDate:[{y}{m:02d}010000 TO {y}{m:02d}{last}2359]"
            start, kept, total = 0, [], None
            while total is None or start < total:
                total, entries = fetch(q, start)
                time.sleep(3)
                for e in entries:
                    prim = e.find("x:primary_category", NS).get("term", "")
                    if not prim.startswith(arch):
                        continue
                    com = e.find("x:comment", NS)
                    kept.append({"id": re.sub(r"v\d+$", "", e.find("a:id", NS).text.rsplit("/abs/", 1)[-1]),
                                 "v1": e.find("a:published", NS).text[:10], "primary": prim,
                                 "n_authors": len(e.findall("a:author", NS)),
                                 "title": " ".join((e.find("a:title", NS).text or "").split()),
                                 "abstract": " ".join((e.find("a:summary", NS).text or "").split()),
                                 "comments": " ".join(com.text.split()) if com is not None and com.text else ""})
                if not entries:
                    break
                start += len(entries)
            with gzip.open(os.path.join(out_dir, f"{arch}.jsonl.gz"), "at", encoding="utf-8") as f:
                for k in kept:
                    f.write(json.dumps(k, ensure_ascii=False) + "\n")
            with open(done_path, "a") as f:
                f.write(ym + "\n")
            print(arch, ym, "listed", total, "kept", len(kept), time.strftime("%H:%M:%S"), flush=True)
    counts = Counter()
    for arch in CATS:
        seen = set()
        for line in gzip.open(os.path.join(out_dir, f"{arch}.jsonl.gz"), "rt", encoding="utf-8"):
            r = json.loads(line)
            if r["id"] in seen:
                continue
            seen.add(r["id"])
            counts[(arch, r["primary"], r["v1"][:7])] += 1
    with open(os.path.join(repo, "data/raw/arxiv_heldout_monthly.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["archive", "primary_category", "month_v1", "papers"])
        for (a, c, m), n in sorted(counts.items()):
            w.writerow([a, c, m, n])
    print("done")


if __name__ == "__main__":
    main(*sys.argv[1:])
