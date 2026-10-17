"""Draw the 100 validation papers for the second human coder (Amendment 1, optional second coder; Deviation 3, fourth
addendum, D3r). Stratified as the 400-paper sheet: 50 physics and astronomy (arXiv), 25 bioRxiv, 25 medRxiv, at random
within each stratum with seed 20261017, taken in that order from the V-ids of each stratum sorted. Only the V-id and
server columns of the sealed key are read; no label of any kind. The list is written sorted by V-id, so it does not
show which papers come from which server: validation/second_coder_ids.csv (one column, id).
Usage: python3 scripts/draw_second_coder.py [repo_dir]
"""
import csv
import gzip
import os
import random
import sys

STRATA = (("arxiv", 50), ("biorxiv", 25), ("medrxiv", 25))
SEED = 20261017


def main(repo):
    key = [(r["id"], r["server"]) for r in csv.DictReader(gzip.open(os.path.join(repo, "validation/sealed/key.csv.gz"),
                                                                    "rt"))]
    rng = random.Random(SEED)
    drawn = []
    for server, n in STRATA:
        drawn += rng.sample(sorted(v for v, s in key if s == server), n)
    path = os.path.join(repo, "validation/second_coder_ids.csv")
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id"])
        for v in sorted(drawn):
            w.writerow([v])
    print("written", path, len(drawn), "ids;", ", ".join(f"{s} {n}" for s, n in STRATA))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
