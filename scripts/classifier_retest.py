"""Test-retest agreement of the ND/NN/U classifier: the same papers classified in two separate runs.

The first runs on the medRxiv samples (18 batches of the date-ordered, DOI-keyed split, 900 papers) and on the 200
bioRxiv and medRxiv papers of the validation sheet were superseded by blind runs (pseudonymous ids, random order);
the superseded labels are used only here. The 200 arXiv papers of the sheet were classified a second time, blind, with
a new random order and new pseudonymous ids. Agreement between runs measures how stable the labels are when the batch
composition and order change; it says nothing about accuracy, which the human validation measures.
Inputs: CSV or gzip CSV files with columns id,label; with --map, a CSV pseudonym,id that turns the second file's
ids into the first file's ids (a prefix such as "medrxiv:" is ignored when matching).
Usage: python3 scripts/classifier_retest.py FIRST SECOND [--map PSEUDONYMS] [--out OUT_JSON]
"""
import csv
import gzip
import json
import sys
from collections import Counter

CLASSES = ("ND", "NN", "U")


def read(path):
    f = gzip.open(path, "rt") if path.endswith(".gz") else open(path)
    return {r["id"].split(":", 1)[-1] if r["id"].startswith(("medrxiv:", "biorxiv:", "arxiv:")) else r["id"]:
            r["label"] for r in csv.DictReader(f)}


def kappa(pairs):
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum(ca[c] * cb[c] for c in CLASSES) / n ** 2
    return po, (po - pe) / (1 - pe) if pe < 1 else float("nan")


def main():
    args = sys.argv[1:]
    opts = {}
    for k in ("--map", "--out"):
        if k in args:
            i = args.index(k)
            opts[k] = args[i + 1]
            args = args[:i] + args[i + 2:]
    first, second = read(args[0]), read(args[1])
    if "--map" in opts:
        m = {r["pseudonym"]: r["id"].split(":", 1)[-1] for r in csv.DictReader(open(opts["--map"]))}
        second = {m[k]: v for k, v in second.items() if k in m}
    common = sorted(set(first) & set(second))
    pairs = [(first[k], second[k]) for k in common]
    po, k = kappa(pairs)
    table = {a: {b: sum(1 for x, y in pairs if (x, y) == (a, b)) for b in CLASSES} for a in CLASSES}
    out = {"n": len(pairs), "agreement": po, "kappa": k, "table_first_by_second": table}
    print(json.dumps(out, indent=1))
    if "--out" in opts:
        json.dump(out, open(opts["--out"], "w"), indent=1)


if __name__ == "__main__":
    main()
