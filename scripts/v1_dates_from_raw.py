"""First-version submission dates from arXivRaw harvests (harvest_arxiv_raw.py), written as
data/raw/arxiv_v1_dates.csv.gz (arxiv_id, v1_submitted), the input of the P1a dating analysis in stats_round1.py.
Replaces fetch_arxiv_v1_dates.py, because the arXiv API answered "429 Rate exceeded" from this environment.
Usage: python3 scripts/v1_dates_from_raw.py out.csv.gz raw1.jsonl.gz [raw2.jsonl.gz ...]
"""
import csv
import gzip
import json
import sys


def main(out, *files):
    v1 = {}
    for fn in files:
        for line in gzip.open(fn, "rt", encoding="utf-8"):
            r = json.loads(line)
            v1[r["id"]] = r["v1"]
    with gzip.open(out, "wt", newline="") as f:
        w = csv.writer(f)
        w.writerow(["arxiv_id", "v1_submitted"])
        w.writerows(sorted(v1.items()))
    print("v1 dates:", len(v1))


if __name__ == "__main__":
    main(*sys.argv[1:])
