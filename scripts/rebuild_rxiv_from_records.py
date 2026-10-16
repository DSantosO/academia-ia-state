"""Rebuild the monthly bioRxiv or medRxiv inputs from version-1 records, counting each preprint (DOI) once.

The API lists some version-1 preprints on more than one day: the same DOI appears as version 1 with two posting dates.
In medRxiv this inflates the counts for mid-2026, and the server's own monthly totals (api.biorxiv.org/sum) include
the duplicates: July 2026 has 1,794 listings but 1,617 preprints, and August 2026 has 1,704 listings but 1,399.
Each preprint is counted at its first version-1 listing.

From the harvest_rxiv_records.py part files this writes, for medRxiv:
  data/raw/medrxiv_covid_monthly.csv   month, new_papers, covid_title, covid_title_or_abstract, listings
  data/raw/medrxiv_category_monthly.csv month, category, new_papers, covid, public_dataset
  data/raw/medrxiv_text_main.csv, medrxiv_text_words.csv.gz  (same format as harvest_rxiv_text_features.py)
and for bioRxiv:
  data/raw/biorxiv_records_monthly.csv month, category, new_papers, listings
Usage: python3 scripts/rebuild_rxiv_from_records.py {medrxiv|biorxiv} PARTS_DIR [repo_dir]
"""
import csv
import glob
import gzip
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harvest_rxiv_categories import COVID_RE, PUBLIC_RE  # noqa: E402

TOKEN = re.compile(r"[a-z]+")
STYLE = {r["word"] for r in csv.DictReader(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                                              "data", "raw", "kobak_style_words.csv")))}


def main(server, parts, repo="."):
    raw = os.path.join(repo, "data/raw")
    first, listings = {}, Counter()
    for fn in sorted(glob.glob(os.path.join(parts, "*.csv"))):
        for r in csv.DictReader(open(fn)):
            listings[r["date"][:7]] += 1
            if r["doi"] not in first or r["date"] < first[r["doi"]]["date"]:
                first[r["doi"]] = r
    if server == "biorxiv":
        c = Counter((r["date"][:7], r["category"]) for r in first.values())
        tot = Counter(r["date"][:7] for r in first.values())
        with open(os.path.join(raw, "biorxiv_records_monthly.csv"), "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["month", "category", "new_papers", "listings_all_categories"])
            for (m, cat), n in sorted(c.items()):
                w.writerow([m, cat, n, listings[m]])
        print("biorxiv preprints", len(first), "listings", sum(listings.values()),
              {m: (tot[m], listings[m]) for m in sorted(tot) if listings[m] - tot[m] > 0.01 * tot[m]})
        return
    covid = defaultdict(Counter)
    cat = defaultdict(Counter)
    main_ = defaultdict(Counter)
    words = defaultdict(Counter)
    for r in first.values():
        m, c = r["date"][:7], r["category"]
        text = r["title"] + " " + r["abstract"]
        cv = bool(COVID_RE.search(text))
        pub = bool(PUBLIC_RE.search(text))
        covid[m]["new_papers"] += 1
        covid[m]["covid_title"] += bool(COVID_RE.search(r["title"]))
        covid[m]["covid_title_or_abstract"] += cv
        cat[(m, c)]["new_papers"] += 1
        cat[(m, c)]["covid"] += cv
        cat[(m, c)]["public_dataset"] += pub
        k = main_[(m, c)]
        k["papers"] += 1
        k["covid"] += cv
        k["public"] += pub
        if not cv:
            k["public_noncovid"] += pub
            k["papers_noncovid"] += 1
            tokens = TOKEN.findall(text.lower())
            k["words_noncovid"] += len(tokens)
            for wd in STYLE.intersection(tokens):
                words[(m, c)][wd] += 1
    with open(os.path.join(raw, "medrxiv_covid_monthly.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["month", "new_papers", "covid_title", "covid_title_or_abstract", "listings"])
        for m in sorted(covid):
            w.writerow([m, covid[m]["new_papers"], covid[m]["covid_title"], covid[m]["covid_title_or_abstract"],
                        listings[m]])
    with open(os.path.join(raw, "medrxiv_category_monthly.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["month", "category", "new_papers", "covid", "public_dataset"])
        for (m, c), v in sorted(cat.items()):
            w.writerow([m, c, v["new_papers"], v["covid"], v["public_dataset"]])
    fields = ["papers", "covid", "public", "public_noncovid", "papers_noncovid", "words_noncovid"]
    with open(os.path.join(raw, "medrxiv_text_main.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["month", "category"] + fields)
        for (m, c), v in sorted(main_.items()):
            w.writerow([m, c] + [v[k] for k in fields])
    with gzip.open(os.path.join(raw, "medrxiv_text_words.csv.gz"), "wt", newline="") as f:
        w = csv.writer(f)
        w.writerow(["month", "category", "word", "docs_noncovid"])
        for (m, c), v in sorted(words.items()):
            for wd, n in sorted(v.items()):
                w.writerow([m, c, wd, n])
    print("medrxiv preprints", len(first), "listings", sum(listings.values()))


if __name__ == "__main__":
    main(*sys.argv[1:])
