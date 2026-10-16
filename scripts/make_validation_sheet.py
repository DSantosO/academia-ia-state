"""Blind validation sheet for the new-data (ND/NN) classifier: 400 papers (pre-registration and Amendment 1).

Composition: 200 arXiv papers (cond-mat, astro-ph, quant-ph by primary category; 34/33/33 per period), 100 bioRxiv and
100 medRxiv preprints (COVID-19 excluded), each split evenly between 2019-2022 and 2023-2026 (to September), dated by
first-version submission or posting.

Sampling (fixed seeds):
  arXiv     a simple random sample of the papers in the stratum (primary category in the archive, version 1 submitted
            in the period, with an abstract), drawn from the complete arXivRaw harvests of the three archives
            (harvest_arxiv_raw.py, the sampling frames of the new-data test). The arXiv API answered "429 Rate
            exceeded" from this environment, so the planned draw by random submission day could not be run.
  bioRxiv / medRxiv  a random day, a random page of that day's records (api.biorxiv.org/details), one random
            version-1 record on the page with an abstract; medRxiv COVID-19 preprints (title or abstract) rejected.
  Only preprints whose licence allows redistribution are kept for bioRxiv and medRxiv (Creative Commons; "cc_no"
  rejected), because the sheet is published in a public repository. arXiv metadata are CC0.
Outputs:
  validation/sheet.csv and sheet.json   pseudonymous id, title, abstract, comments (arXiv only), label, note
  validation/sealed/key.csv.gz          id -> server, paper id, date, archive or category, period, licence
The rows are shuffled across domains; dates, servers, archives and model labels are not in the sheet.
Pacing: bioRxiv/medRxiv API one request at a time with a 0.3 s pause.
Usage: python3 scripts/make_validation_sheet.py rxiv WORK_DIR
       python3 scripts/make_validation_sheet.py arxiv WORK_DIR HELDOUT_DIR
       python3 scripts/make_validation_sheet.py assemble WORK_DIR [repo_dir]
"""
import csv
import datetime as dt
import gzip
import json
import os
import random
import sys
import time
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harvest_rxiv_categories import COVID_RE  # noqa: E402

UA = "academia-ia-state research"
PERIODS = {"2019-2022": (dt.date(2019, 1, 1), dt.date(2022, 12, 31)), "2023-2026": (dt.date(2023, 1, 1), dt.date(2026, 9, 30))}
ARXIV_N = {"cond-mat": 34, "astro-ph": 33, "quant-ph": 33}
RXIV_N = 50  # per server and period


def get(url):
    for attempt in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=120) as r:
                return json.load(r)
        except Exception:
            time.sleep(10 * (attempt + 1))
    raise RuntimeError(url)


def rand_day(rng, period):
    a, b = PERIODS[period]
    return a + dt.timedelta(days=rng.randrange((b - a).days + 1))


def clean(s):
    return " ".join((s or "").split())


def sample_rxiv(server, period, n, rng, seen):
    out = []
    while len(out) < n:
        day = rand_day(rng, period).isoformat()
        j = get(f"https://api.biorxiv.org/details/{server}/{day}/{day}/0")
        time.sleep(0.3)
        total = int(j["messages"][0].get("total", 0) or 0)
        if not total:
            continue
        cursor = 30 * rng.randrange((total + 29) // 30)
        if cursor:
            j = get(f"https://api.biorxiv.org/details/{server}/{day}/{day}/{cursor}")
            time.sleep(0.3)
        recs = [p for p in j.get("collection", []) if str(p.get("version")) == "1" and clean(p.get("abstract"))
                and p.get("doi") not in seen]
        if not recs:
            continue
        p = rng.choice(recs)
        lic = (p.get("license") or "").lower()
        if not lic.startswith("cc") or lic == "cc_no":
            continue
        if server == "medrxiv" and COVID_RE.search(clean(p.get("title")) + " " + clean(p.get("abstract"))):
            continue
        seen.add(p["doi"])
        out.append({"server": server, "paper_id": p["doi"], "date": p.get("date"), "category": p.get("category"),
                    "period": period, "licence": lic, "title": clean(p.get("title")),
                    "abstract": clean(p.get("abstract")), "comments": ""})
        print(server, period, len(out), flush=True)
    return out


def sample_arxiv(heldout_dir):
    rng, rows = random.Random(20261017), []
    for archive in ARXIV_N:
        recs = {}
        for line in gzip.open(os.path.join(heldout_dir, f"{archive}.raw.jsonl.gz"), "rt", encoding="utf-8"):
            r = json.loads(line)
            recs[r["id"]] = r
        for period, (a, b) in PERIODS.items():
            pool = sorted(k for k, r in recs.items() if a.isoformat() <= r["v1"] <= b.isoformat() and r["abstract"])
            for k in rng.sample(pool, ARXIV_N[archive]):
                r = recs[k]
                rows.append({"server": "arxiv", "paper_id": k, "date": r["v1"], "category": r["primary"],
                             "period": period, "licence": "arXiv metadata CC0", "title": clean(r["title"]),
                             "abstract": clean(r["abstract"]), "comments": clean(r["comments"])})
            print(archive, period, "frame", len(pool), flush=True)
    return rows


def main(stage, work, arg=None):
    repo = arg or "."
    os.makedirs(work, exist_ok=True)
    if stage == "rxiv":
        rng, seen, rows = random.Random(20261016), set(), []
        for server in ("biorxiv", "medrxiv"):
            for period in PERIODS:
                rows += sample_rxiv(server, period, RXIV_N, rng, seen)
        json.dump(rows, open(os.path.join(work, "rxiv_sample.json"), "w"), indent=1)
    elif stage == "arxiv":
        json.dump(sample_arxiv(arg), open(os.path.join(work, "arxiv_sample.json"), "w"), indent=1)
    elif stage == "assemble":
        rows = json.load(open(os.path.join(work, "arxiv_sample.json"))) + json.load(
            open(os.path.join(work, "rxiv_sample.json")))
        rng = random.Random(20261018)
        rng.shuffle(rows)
        vdir = os.path.join(repo, "validation")
        os.makedirs(os.path.join(vdir, "sealed"), exist_ok=True)
        sheet = [{"id": f"V{i + 1:03d}", "title": r["title"], "abstract": r["abstract"], "comments": r["comments"],
                  "label": "", "note": ""} for i, r in enumerate(rows)]
        with open(os.path.join(vdir, "sheet.csv"), "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(sheet[0]))
            w.writeheader()
            w.writerows(sheet)
        json.dump(sheet, open(os.path.join(vdir, "sheet.json"), "w"), indent=1, ensure_ascii=False)
        with gzip.open(os.path.join(vdir, "sealed", "key.csv.gz"), "wt", newline="") as f:
            w = csv.writer(f)
            w.writerow(["id", "server", "paper_id", "date", "category", "period", "licence"])
            for s, r in zip(sheet, rows):
                w.writerow([s["id"], r["server"], r["paper_id"], r["date"], r["category"], r["period"], r["licence"]])
        # the classifier sees each paper with its domain's prompt; written to WORK_DIR, outside the repository
        json.dump([{"id": s["id"], "domain": r["server"], "title": r["title"], "abstract": r["abstract"],
                    "comments": r["comments"]} for s, r in zip(sheet, rows)],
                  open(os.path.join(work, "classifier_input.json"), "w"), indent=1, ensure_ascii=False)
        print("sheet:", len(sheet), "rows")


if __name__ == "__main__":
    main(*sys.argv[1:])
