"""Sheet for a human spot check of the country classifier (scripts/classify_country.py), which so far was checked by an
AI agent only (review round 2, R4). 100 version-1 preprints of 2025-2026: per server (bioRxiv, medRxiv), 20 classified
US, 20 non-US and 10 with no country, drawn at random with a fixed seed. The coder opens the DOI link, reads the
corresponding author's institution and enters US, non-US or unclear. No titles or names are written.
Usage: python3 scripts/sample_country_check.py [repo_dir]
"""
import csv
import gzip
import os
import random
import sys

STRATA = {"US": 20, "non-US": 20, "unknown": 10}


def main(repo):
    rng = random.Random(20261017)
    rows = []
    for server in ("biorxiv", "medrxiv"):
        recs = [r for r in csv.DictReader(gzip.open(os.path.join(repo, f"data/raw/{server}_records.csv.gz"), "rt"))
                if r["date"][:4] in ("2025", "2026")]
        for cls, n in STRATA.items():
            pool = sorted((r for r in recs if r["country"] == cls), key=lambda r: r["doi"])
            for r in rng.sample(pool, n):
                rows.append({"server": server, "doi": r["doi"], "link": f"https://doi.org/{r['doi']}",
                             "assigned": cls, "coder": "", "true_country": "", "note": ""})
    rng.shuffle(rows)
    path = os.path.join(repo, "docs/stats/validation/country_spot_check_sheet.csv")
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print("written", path, len(rows))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
