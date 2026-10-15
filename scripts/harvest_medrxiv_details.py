"""Count medRxiv new papers per month, split into COVID-related and other, via api.biorxiv.org/details.

A paper is "new" in the month its version 1 was posted. It is COVID-related when its title (and, for the
broader flag, its abstract) matches COVID_RE. Writes one CSV row per month.
Usage: python3 scripts/harvest_medrxiv_details.py 2019-06 2026-09 data/raw/medrxiv_covid_monthly.csv
"""
import calendar
import csv
import json
import re
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = "academia-ia-state research"
COVID_RE = re.compile(
    r"covid|sars[\s-]*cov[\s-]*2|2019[\s-]*ncov|ncov[\s-]*2019|novel coronavirus|coronavirus disease 2019", re.I)


def get(url):
    for attempt in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=120) as r:
                return json.load(r)
        except Exception:
            time.sleep(5 * (attempt + 1))
    raise RuntimeError(url)


def month(ym):
    y, m = map(int, ym.split("-"))
    start, end = f"{y}-{m:02d}-01", f"{y}-{m:02d}-{calendar.monthrange(y, m)[1]:02d}"
    cursor, total, pages = 0, None, 0
    new = cov_title = cov_any = 0
    while (total is None or cursor < total) and pages < 400:
        pages += 1
        j = get(f"https://api.biorxiv.org/details/medrxiv/{start}/{end}/{cursor}")
        msg = j["messages"][0]
        if msg.get("status") != "ok":
            break
        total = int(msg.get("total", 0))
        coll = j.get("collection", [])
        for p in coll:
            if str(p.get("version")) != "1":
                continue
            new += 1
            t, a = p.get("title") or "", p.get("abstract") or ""
            in_title = bool(COVID_RE.search(t))
            cov_title += in_title
            cov_any += in_title or bool(COVID_RE.search(a))
        if not coll:
            break
        cursor += len(coll)
        time.sleep(0.3)
    print(ym, new, cov_title, cov_any, f"pages={pages}", flush=True)
    return {"month": ym, "new_papers": new, "covid_title": cov_title, "covid_title_or_abstract": cov_any}


def months(a, b):
    y, m = map(int, a.split("-"))
    while f"{y}-{m:02d}" <= b:
        yield f"{y}-{m:02d}"
        m += 1
        if m == 13:
            y, m = y + 1, 1


def main():
    a, b, out = sys.argv[1:4]
    with ThreadPoolExecutor(6) as ex:
        rows = list(ex.map(month, months(a, b)))
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print("done", len(rows))


if __name__ == "__main__":
    main()
