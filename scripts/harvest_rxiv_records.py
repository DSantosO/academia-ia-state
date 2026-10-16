"""Harvest version-1 bioRxiv or medRxiv records (one row per preprint) from api.biorxiv.org/details, one day at a time.

Writes one CSV per month into PARTS_DIR (doi, date, category, corresponding-author institution, title, abstract).
These part files hold full titles and abstracts and are kept out of the repository; scripts/build_rxiv_records.py turns
them into the record-level table that is deposited (identifiers, dates, categories and flags only).
Months whose part file exists are skipped, so an interrupted harvest can be resumed.

Request pacing: WORKERS months in parallel (default 2), each making one request at a time with a 0.3 s pause.
The API states no rate limit or terms of use (https://api.biorxiv.org, checked 16 October 2026).
Usage: python3 scripts/harvest_rxiv_records.py medrxiv 2019-06 2026-09 PARTS_DIR [workers]
"""
import calendar
import csv
import json
import os
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = "academia-ia-state research"
FIELDS = ["doi", "date", "category", "institution", "title", "abstract"]


def get(url):
    for attempt in range(8):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=120) as r:
                return json.load(r)
        except Exception:
            time.sleep(5 * (attempt + 1))
    raise RuntimeError(url)


def harvest_month(server, ym, parts):
    path = os.path.join(parts, f"{ym}.csv")
    if os.path.exists(path):
        return ym, None
    y, m = map(int, ym.split("-"))
    rows = []
    for d in range(1, calendar.monthrange(y, m)[1] + 1):
        day = f"{y}-{m:02d}-{d:02d}"
        cursor, total, tries = 0, None, 0
        while total is None or cursor < total:
            j = get(f"https://api.biorxiv.org/details/{server}/{day}/{day}/{cursor}")
            msg = j["messages"][0]
            coll = j.get("collection", [])
            if msg.get("status") != "ok" or not coll:
                if msg.get("status") == "no posts found" and cursor == 0:
                    break
                tries += 1  # transient errors and empty pages: retry before moving on
                if tries > 6:
                    print("WARNING incomplete day", server, day, cursor, total, flush=True)
                    break
                time.sleep(10 * tries)
                continue
            tries = 0
            total = int(msg.get("total", 0))
            for p in coll:
                if str(p.get("version")) == "1":
                    rows.append({"doi": p.get("doi"), "date": p.get("date"),
                                 "category": (p.get("category") or "unknown").strip().lower(),
                                 "institution": " ".join((p.get("author_corresponding_institution") or "").split()),
                                 "title": " ".join((p.get("title") or "").split()),
                                 "abstract": " ".join((p.get("abstract") or "").split())})
            cursor += len(coll)
            time.sleep(0.3)
    tmp = path + ".tmp"
    with open(tmp, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    os.replace(tmp, path)
    print(server, ym, len(rows), "v1 records", time.strftime("%H:%M:%S"), flush=True)
    return ym, len(rows)


def months(a, b):
    y, m = map(int, a.split("-"))
    while f"{y}-{m:02d}" <= b:
        yield f"{y}-{m:02d}"
        m += 1
        if m == 13:
            y, m = y + 1, 1


def main():
    server, a, b, parts = sys.argv[1:5]
    workers = int(sys.argv[5]) if len(sys.argv) > 5 else 2
    os.makedirs(parts, exist_ok=True)
    with ThreadPoolExecutor(workers) as ex:
        done = list(ex.map(lambda ym: harvest_month(server, ym, parts), months(a, b)))
    print("done", len(done), "months")


if __name__ == "__main__":
    main()
