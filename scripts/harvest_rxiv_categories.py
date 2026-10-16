"""Count new bioRxiv or medRxiv preprints per month and subject category via api.biorxiv.org/details.

A preprint is "new" in the month its version 1 was posted. For each month and category the script counts:
  new_papers       version-1 preprints
  covid            those whose title or abstract matches COVID_RE (same pattern as harvest_medrxiv_details.py)
  public_dataset   those whose title or abstract names a public dataset or design that is often reused in
                   formulaic papers (PUBLIC_RE: NHANES, UK Biobank, Global Burden of Disease, Mendelian
                   randomisation, FAERS, MIMIC, SEER, BRFSS)
Only aggregate counts are written. Usage:
  python3 scripts/harvest_rxiv_categories.py medrxiv 2019-06 2026-09 data/raw/medrxiv_category_monthly.csv [workers]

With --counts the script instead makes one call per month and category (details endpoint with ?category=) and
reads count_new_papers from its messages block. That is about ten times faster for bioRxiv, whose records come
30 per page, but it gives no COVID-19 or public-dataset flags (those columns are left empty):
  python3 scripts/harvest_rxiv_categories.py biorxiv 2019-01 2026-09 data/raw/biorxiv_category_monthly.csv 4 --counts
"""
import calendar
import csv
import json
import re
import sys
import time
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

UA = "academia-ia-state research"
COVID_RE = re.compile(
    r"covid|sars[\s-]*cov[\s-]*2|2019[\s-]*ncov|ncov[\s-]*2019|novel coronavirus|coronavirus disease 2019", re.I)
PUBLIC_RE = re.compile(
    r"\bNHANES\b|national health and nutrition examination survey|uk[\s-]?biobank|global burden of disease|"
    r"\bGBD\s?20\d\d\b|mendelian randomi[sz]ation|\bFAERS\b|adverse event reporting system|\bMIMIC-?(?:III|IV)\b|"
    r"\bSEER\b|\bBRFSS\b", re.I)


def get(url):
    for attempt in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=120) as r:
                return json.load(r)
        except Exception:
            time.sleep(5 * (attempt + 1))
    raise RuntimeError(url)


def harvest_month(server, ym):
    y, m = map(int, ym.split("-"))
    start, end = f"{y}-{m:02d}-01", f"{y}-{m:02d}-{calendar.monthrange(y, m)[1]:02d}"
    cursor, total, pages = 0, None, 0
    new, cov, pub = Counter(), Counter(), Counter()
    while (total is None or cursor < total) and pages < 600:
        pages += 1
        j = get(f"https://api.biorxiv.org/details/{server}/{start}/{end}/{cursor}")
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
            new[cat] += 1
            cov[cat] += bool(COVID_RE.search(text))
            pub[cat] += bool(PUBLIC_RE.search(text))
        if not coll:
            break
        cursor += len(coll)
        time.sleep(0.3)
    print(server, ym, sum(new.values()), f"records={total} pages={pages}", flush=True)
    return [{"month": ym, "category": c, "new_papers": new[c], "covid": cov[c], "public_dataset": pub[c]}
            for c in sorted(new)]


# The API's category filter accepts these 25. "clinical trials" and "epidemiology" moved to medRxiv in 2019 and fall
# back to all categories, so they are left out; the gap to the official monthly total is checked afterwards.
BIORXIV_CATEGORIES = [
    "animal behavior and cognition", "biochemistry", "bioengineering", "bioinformatics", "biophysics",
    "cancer biology", "cell biology", "developmental biology", "ecology", "evolutionary biology", "genetics", "genomics", "immunology", "microbiology", "molecular biology", "neuroscience",
    "paleontology", "pathology", "pharmacology and toxicology", "physiology", "plant biology",
    "scientific communication and education", "synthetic biology", "systems biology", "zoology"]


def count_month(server, ym, cat):
    y, m = map(int, ym.split("-"))
    start, end = f"{y}-{m:02d}-01", f"{y}-{m:02d}-{calendar.monthrange(y, m)[1]:02d}"
    msg = get(f"https://api.biorxiv.org/details/{server}/{start}/{end}/0?category={cat.replace(' ', '_')}")["messages"][0]
    if msg.get("status") == "no posts found":
        return {"month": ym, "category": cat, "new_papers": 0, "covid": "", "public_dataset": ""}
    if msg.get("status") != "ok" or msg.get("category", "").lower() != cat:
        raise RuntimeError(f"{ym} {cat}: {msg}")
    return {"month": ym, "category": cat, "new_papers": int(msg.get("count_new_papers", 0)), "covid": "",
            "public_dataset": ""}


def months(a, b):
    y, m = map(int, a.split("-"))
    while f"{y}-{m:02d}" <= b:
        yield f"{y}-{m:02d}"
        m += 1
        if m == 13:
            y, m = y + 1, 1


def main():
    args = [x for x in sys.argv[1:] if x != "--counts"]
    server, a, b, out = args[:4]
    workers = int(args[4]) if len(args) > 4 else 6
    with ThreadPoolExecutor(workers) as ex:
        if "--counts" in sys.argv:
            jobs = [(ym, c) for ym in months(a, b) for c in BIORXIV_CATEGORIES]
            rows = list(ex.map(lambda j: count_month(server, *j), jobs))
            print("done counts", len(rows), flush=True)
        else:
            rows = [r for month_rows in ex.map(lambda ym: harvest_month(server, ym), months(a, b))
                    for r in month_rows]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["month", "category", "new_papers", "covid", "public_dataset"])
        w.writeheader()
        w.writerows(rows)
    print("done", len(rows), "rows")


if __name__ == "__main__":
    main()
