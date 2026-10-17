"""Build the deposited record-level tables and monthly aggregates from the harvest_rxiv_records.py part files.

medRxiv -> data/raw/medrxiv_records.csv.gz: doi, date, category, covid_title, covid_title_abstract,
           public_dataset (original list), public_dataset_spick4 (FinnGen, CHARLS, CDC WONDER, TriNetX), country
           data/processed/medrxiv_flags_monthly.csv: monthly counts under each flag definition
bioRxiv -> data/raw/biorxiv_records.csv.gz: doi, date, category, group (computational / wet_lab / mixed), country,
           covid_title_abstract (COVID-19 pattern in the title or abstract), ai_topic (AI or machine learning as a
           topic, the list of Deviation 3, D3m, in nd_frames.py)
           data/processed/biorxiv_records_country_monthly.csv: month, group, country, preprints
Country is the corresponding author's institution classified by scripts/classify_country.py (US / non-US / unknown).
Titles, abstracts and institution strings are not written to the repository.
Usage: python3 scripts/build_rxiv_records.py {medrxiv|biorxiv} PARTS_DIR [repo_dir]
"""
import csv
import glob
import gzip
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from classify_country import classify  # noqa: E402
from harvest_rxiv_categories import COVID_RE, PUBLIC_RE  # noqa: E402
from stats_within_field import COMPUTATIONAL, WET_LAB  # noqa: E402
from nd_frames import flags as nd_flags  # noqa: E402

SPICK4_RE = re.compile(r"\bFinnGen\b|\bCHARLS\b|China Health and Retirement Longitudinal Study|CDC[\s-]?WONDER|"
                       r"\bTriNetX\b", re.I)


def records(parts):
    for fn in sorted(glob.glob(os.path.join(parts, "*.csv"))):
        yield from csv.DictReader(open(fn))


def main(server, parts, repo="."):
    seen = set()
    rows = []
    for r in records(parts):
        if r["doi"] in seen:
            continue
        seen.add(r["doi"])
        text = r["title"] + " " + r["abstract"]
        row = {"doi": r["doi"], "date": r["date"], "category": r["category"], "country": classify(r["institution"])}
        if server == "medrxiv":
            row.update({"covid_title": int(bool(COVID_RE.search(r["title"]))),
                        "covid_title_abstract": int(bool(COVID_RE.search(text))),
                        "public_dataset": int(bool(PUBLIC_RE.search(text))),
                        "public_dataset_spick4": int(bool(SPICK4_RE.search(text)))})
        else:
            c = r["category"]
            row["group"] = "computational" if c in COMPUTATIONAL else "wet_lab" if c in WET_LAB else "mixed"
            row["covid_title_abstract"] = int(bool(COVID_RE.search(text)))
            row["ai_topic"] = nd_flags(r["title"], r["abstract"])["ai_topic"]
        rows.append(row)
    rows.sort(key=lambda x: (x["date"], x["doi"]))
    fields = list(rows[0])
    with gzip.open(os.path.join(repo, f"data/raw/{server}_records.csv.gz"), "wt", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    if server == "medrxiv":
        agg = {}
        for x in rows:
            m = x["date"][:7]
            a = agg.setdefault(m, Counter())
            a["preprints"] += 1
            a["covid_title"] += x["covid_title"]
            a["covid_title_abstract"] += x["covid_title_abstract"]
            nc = not x["covid_title_abstract"]
            a["noncovid"] += nc
            a["public_noncovid"] += nc and x["public_dataset"]
            a["public_or_spick4_noncovid"] += nc and (x["public_dataset"] or x["public_dataset_spick4"])
            a["spick4_only_noncovid"] += nc and x["public_dataset_spick4"] and not x["public_dataset"]
            a["noncovid_title_only"] += not x["covid_title"]
            a["public_noncovid_title_only"] += (not x["covid_title"]) and x["public_dataset"]
            a[f"country_{x['country']}"] += 1
        keys = ["preprints", "covid_title", "covid_title_abstract", "noncovid", "public_noncovid",
                "public_or_spick4_noncovid", "spick4_only_noncovid", "noncovid_title_only",
                "public_noncovid_title_only", "country_US", "country_non-US", "country_unknown"]
        with open(os.path.join(repo, "data/processed/medrxiv_flags_monthly.csv"), "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["month"] + keys)
            for m in sorted(agg):
                w.writerow([m] + [agg[m][k] for k in keys])
    else:
        agg = Counter((x["date"][:7], x["group"], x["country"]) for x in rows)
        with open(os.path.join(repo, "data/processed/biorxiv_records_country_monthly.csv"), "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["month", "group", "country", "preprints"])
            for (m, g, c), n in sorted(agg.items()):
                w.writerow([m, g, c, n])
    print(server, len(rows), "records;", Counter(x["country"] for x in rows))


if __name__ == "__main__":
    main(*sys.argv[1:])
