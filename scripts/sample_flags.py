"""Random samples of medRxiv preprints for checking the COVID-19 and public-dataset flags by hand.

Draws, with a fixed seed, preprints flagged by each rule from the harvest_rxiv_records.py part files:
  covid_title            COVID_RE matches the title
  covid_abstract_only    COVID_RE matches the abstract but not the title (where false positives concentrate)
  public_dataset         PUBLIC_RE (original list) matches title or abstract
  public_spick4          one of FinnGen, CHARLS, CDC WONDER, TriNetX matches and the original list does not
For each it writes the DOI, the title and a snippet around the first match to SAMPLE_CSV (kept out of the repository,
because abstracts are the authors' text) and a coding sheet with the DOI and flag only to SHEET_CSV (deposited).
A preprint is a true positive if it studies COVID-19 (covid flags) or analyses data from the named source (dataset
flags); a passing mention is a false positive.
Usage: python3 scripts/sample_flags.py PARTS_DIR SAMPLE_CSV SHEET_CSV [n_per_flag]
"""
import csv
import glob
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_rxiv_records import SPICK4_RE  # noqa: E402
from harvest_rxiv_categories import COVID_RE, PUBLIC_RE  # noqa: E402


def snippet(text, rx, width=160):
    m = rx.search(text)
    if not m:
        return ""
    a, b = max(0, m.start() - width), min(len(text), m.end() + width)
    return ("…" if a else "") + text[a:b] + ("…" if b < len(text) else "")


def main(parts, sample_csv, sheet_csv, n=60):
    n = int(n)
    pools = {"covid_title": [], "covid_abstract_only": [], "public_dataset": [], "public_spick4": []}
    seen = set()
    for fn in sorted(glob.glob(os.path.join(parts, "*.csv"))):
        for r in csv.DictReader(open(fn)):
            if r["doi"] in seen:
                continue
            seen.add(r["doi"])
            t, a = r["title"], r["abstract"]
            text = t + " " + a
            if COVID_RE.search(t):
                pools["covid_title"].append((r, COVID_RE))
            elif COVID_RE.search(a):
                pools["covid_abstract_only"].append((r, COVID_RE))
            if PUBLIC_RE.search(text):
                pools["public_dataset"].append((r, PUBLIC_RE))
            elif SPICK4_RE.search(text):
                pools["public_spick4"].append((r, SPICK4_RE))
    rng = random.Random(20261016)
    with open(sample_csv, "w", newline="") as f, open(sheet_csv, "w", newline="") as g:
        w = csv.writer(f)
        w.writerow(["id", "flag", "doi", "date", "title", "snippet"])
        s = csv.writer(g)
        s.writerow(["id", "flag", "doi", "pool_size", "coder", "true_positive", "note"])
        k = 0
        for flag, pool in pools.items():
            for r, rx in rng.sample(pool, min(n, len(pool))):
                k += 1
                w.writerow([k, flag, r["doi"], r["date"], r["title"], snippet(r["title"] + " " + r["abstract"], rx)])
                s.writerow([k, flag, r["doi"], len(pool), "", "", ""])
    print({f: len(p) for f, p in pools.items()})


if __name__ == "__main__":
    main(*sys.argv[1:])
