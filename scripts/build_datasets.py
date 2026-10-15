"""Build the quarterly preprint series used by the "Preprints by Field" dashboard and charts.

Inputs (data/raw/):
  arxiv_archive_monthly.csv   archive,year,month,new,cross            (parse_arxiv.py)
  biorxiv_sum_m.json          bioRxiv monthly content summary         (fetch_biorxiv_medrxiv.sh)
  medrxiv_sum_m.json          medRxiv monthly content summary         (fetch_biorxiv_medrxiv.sh)
  medrxiv_covid_monthly.csv   medRxiv new papers split by COVID topic (harvest_medrxiv_details.py)
  osf_quarterly.csv           provider,quarter,new_papers,records,method (osf_quarterly.py)

Outputs (data/processed/):
  arxiv_fields_quarterly.json, biorxiv_medrxiv_quarterly.json, osf_social_quarterly.json
      one file per dashboard dataset
  preprints_by_field_quarterly.csv   all series joined, one row per quarter

Medicine excludes COVID-19 preprints: a medRxiv paper counts as COVID-related when its title or
abstract mentions COVID-19, SARS-CoV-2 or 2019-nCoV (column covid_title_or_abstract).
Only complete quarters from 2020-Q1 to the last quarter that ended before today are kept.
Usage: python3 scripts/build_datasets.py [data_dir]
"""
import csv
import datetime
import json
import os
import sys
from collections import Counter, defaultdict

PHYSICS = set("astro-ph cond-mat gr-qc hep-ex hep-lat hep-ph hep-th math-ph nlin nucl-ex nucl-th physics quant-ph".split())
FIRST = "2020-Q1"
COVID_FLAG = "covid_title_or_abstract"


def quarter(y, m):
    return f"{y}-Q{(m - 1) // 3 + 1}"


def quarter_start(q):
    y, n = q.split("-Q")
    return f"{y}-{3 * (int(n) - 1) + 1:02d}-01"


def last_complete_quarter(today):
    y, n = today.year, (today.month - 1) // 3 + 1
    return f"{y - 1}-Q4" if n == 1 else f"{y}-Q{n - 1}"


def main(data_dir):
    raw, out = os.path.join(data_dir, "raw"), os.path.join(data_dir, "processed")
    os.makedirs(out, exist_ok=True)
    last = last_complete_quarter(datetime.date.today())
    s = defaultdict(Counter)

    for r in csv.DictReader(open(os.path.join(raw, "arxiv_archive_monthly.csv"))):
        k, a, n = quarter(int(r["year"]), int(r["month"])), r["archive"], int(r["new"])
        if a in PHYSICS:
            s["physics"][k] += n
        elif a == "math":
            s["mathematics"][k] += n
        elif a in ("econ", "q-fin"):
            s["econ_finance"][k] += n
        elif a == "cs":
            s["computer_science"][k] += n

    for key, fn in (("biorxiv", "biorxiv_sum_m.json"), ("medrxiv", "medrxiv_sum_m.json")):
        j = json.load(open(os.path.join(raw, fn)))
        rows = j[[x for x in j if x != "messages"][0]]
        for x in rows:
            y, m = map(int, x["month"].split("-"))
            s[key][quarter(y, m)] += int(x["new_papers"])

    for r in csv.DictReader(open(os.path.join(raw, "medrxiv_covid_monthly.csv"))):
        y, m = map(int, r["month"].split("-"))
        s["medrxiv_details"][quarter(y, m)] += int(r["new_papers"])
        s["medrxiv_covid"][quarter(y, m)] += int(r[COVID_FLAG])

    for r in csv.DictReader(open(os.path.join(raw, "osf_quarterly.csv"))):
        y, n = r["quarter"].split("Q")
        s[r["provider"]][f"{y}-Q{n}"] += int(r["new_papers"])

    quarters = sorted(q for q in s["physics"] if FIRST <= q <= last)
    cols = ["physics", "mathematics", "econ_finance", "computer_science", "biorxiv", "medrxiv", "medrxiv_covid",
            "psyarxiv", "socarxiv", "edarxiv"]
    missing = [(c, q) for c in cols for q in quarters if q not in s[c]]
    if missing:
        sys.exit(f"missing values: {missing[:10]}")
    for q in quarters:  # the per-paper harvest must agree with medRxiv's own monthly totals
        if abs(s["medrxiv_details"][q] - s["medrxiv"][q]) > 0.01 * s["medrxiv"][q]:
            sys.exit(f"medRxiv totals disagree in {q}: {s['medrxiv_details'][q]} vs {s['medrxiv'][q]}")
    for q in quarters:
        s["medrxiv_no_covid"][q] = s["medrxiv"][q] - s["medrxiv_covid"][q]

    def rows(keys):
        return [{"quarter": q, "start": quarter_start(q), **{k: s[k][q] for k in keys}} for q in quarters]

    files = {
        "arxiv_fields_quarterly.json": rows(["physics", "mathematics", "econ_finance", "computer_science"]),
        "biorxiv_medrxiv_quarterly.json": rows(["biorxiv", "medrxiv", "medrxiv_covid", "medrxiv_no_covid"]),
        "osf_social_quarterly.json": rows(["psyarxiv", "socarxiv", "edarxiv"]),
    }
    for name, data in files.items():
        with open(os.path.join(out, name), "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)

    with open(os.path.join(out, "preprints_by_field_quarterly.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["quarter", "start", "physics", "mathematics", "biology_biorxiv", "medicine_medrxiv_no_covid",
                    "medicine_medrxiv_all", "medrxiv_covid", "social_sciences", "psyarxiv", "socarxiv", "edarxiv",
                    "arxiv_econ_finance", "computer_science_reference"])
        for q in quarters:
            social = s["psyarxiv"][q] + s["socarxiv"][q] + s["edarxiv"][q] + s["econ_finance"][q]
            w.writerow([q, quarter_start(q), s["physics"][q], s["mathematics"][q], s["biorxiv"][q],
                        s["medrxiv_no_covid"][q], s["medrxiv"][q], s["medrxiv_covid"][q], social, s["psyarxiv"][q],
                        s["socarxiv"][q], s["edarxiv"][q], s["econ_finance"][q], s["computer_science"][q]])
    print(f"{len(quarters)} quarters: {quarters[0]} .. {quarters[-1]}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data")
