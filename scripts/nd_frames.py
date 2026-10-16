"""Sampling frames and samples for the confirmatory ND/NN tests, with the design fixed in nd_design.py.

Frames (text kept outside the repository):
  held-out arXiv   harvest_arxiv_api_months.py output (cond-mat, astro-ph, quant-ph; first-version month)
  maths            OAI-PMH harvest (primary math.*; identifier month), for Test B
  HEP/nuclear      OAI-PMH harvests (primary hep-th, hep-ph, gr-qc, nucl-th, hep-ex, nucl-ex; identifier month), Test B
  bioRxiv/medRxiv  harvest_rxiv_records.py part files (version 1; posting month; medRxiv without COVID-19)
Writes:
  data/processed/nd_samples.csv.gz       design, stratum, paper key (identifiers only)
  data/processed/nd_frame_counts.csv     design, stratum, frame size (monthly totals and category totals)
  WORK_DIR/classifier_input_full.json    unique papers to classify (key, domain, title, abstract, comments)
Usage: python3 scripts/nd_frames.py HELDOUT_DIR OAI_DIR BIORXIV_PARTS MEDRXIV_PARTS WORK_DIR [repo_dir]
"""
import csv
import glob
import gzip
import json
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nd_design as D  # noqa: E402
from harvest_rxiv_categories import COVID_RE  # noqa: E402
from stats_within_field import ym_range  # noqa: E402


def heldout(dir_):
    out = {}
    for arch in D.HN_ARCHIVES:
        for line in gzip.open(os.path.join(dir_, f"{arch}.jsonl.gz"), "rt", encoding="utf-8"):
            r = json.loads(line)
            out[r["id"]] = {"key": "arxiv:" + r["id"], "domain": "arxiv", "archive": arch, "category": r["primary"],
                            "month": r["v1"][:7], "title": r["title"], "abstract": r["abstract"],
                            "comments": r["comments"]}
    return list(out.values())


def oai(dir_):
    out = {}
    for fn in sorted(glob.glob(os.path.join(dir_, "oai_*.jsonl.gz"))):
        for line in gzip.open(fn, "rt", encoding="utf-8"):
            r = json.loads(line)
            m = re.fullmatch(r"(\d{2})(\d{2})\.\d{4,5}", r.get("id") or "")
            if not m or not r.get("categories") or r["id"] in out:
                continue
            prim = r["categories"][0]
            if prim.startswith("math."):
                cat = prim
            elif prim in D.TESTB_ARXIV_ARCHIVES:
                cat = prim
            else:
                continue
            out[r["id"]] = {"key": "arxiv:" + r["id"], "domain": "arxiv", "archive": "math" if prim.startswith("math.")
                            else prim, "category": cat, "month": f"20{m.group(1)}-{m.group(2)}",
                            "title": " ".join((r.get("title") or "").split()),
                            "abstract": " ".join((r.get("abstract") or "").split()),
                            "comments": " ".join((r.get("comments") or "").split())}
    return list(out.values())


def rxiv(parts, server):
    out = {}
    for fn in sorted(glob.glob(os.path.join(parts, "*.csv"))):
        for r in csv.DictReader(open(fn)):
            if r["doi"] in out or not r["abstract"]:
                continue
            if server == "medrxiv" and COVID_RE.search(r["title"] + " " + r["abstract"]):
                continue
            out[r["doi"]] = {"key": f"{server}:{r['doi']}", "domain": server, "archive": server,
                             "category": r["category"], "month": r["date"][:7], "title": r["title"],
                             "abstract": r["abstract"], "comments": ""}
    return list(out.values())


def main(heldout_dir, oai_dir, bio_parts, med_parts, work, repo="."):
    os.makedirs(work, exist_ok=True)
    frames = {"heldout": heldout(heldout_dir), "oai": oai(oai_dir), "biorxiv": rxiv(bio_parts, "biorxiv"),
              "medrxiv": rxiv(med_parts, "medrxiv")}
    by_key = {p["key"]: p for f in frames.values() for p in f}
    samples, sizes = [], []

    def add(design, stratum, papers, n):
        sizes.append((design, stratum, len(papers)))
        for k in D.draw(design, stratum, [p["key"] for p in papers], n):
            samples.append((design, stratum, k))

    # HN
    for arch in D.HN_ARCHIVES:
        grp = defaultdict(list)
        for p in frames["heldout"]:
            if p["archive"] == arch:
                grp[p["month"]].append(p)
        for m in ym_range(D.HN_FIRST, D.LAST):
            add("HN", f"{arch}|{m}", grp.get(m, []), D.per_month(m))
    # Test A
    for server, first in (("biorxiv", D.BIO_FIRST), ("medrxiv", D.MED_FIRST)):
        grp = defaultdict(list)
        for p in frames[server]:
            grp[p["month"]].append(p)
        for m in ym_range(first, D.LAST):
            add(f"A-{server}", m, grp.get(m, []), D.per_month(m))
    # Test B (exposure samples, 2019-2022)
    a, b = D.TESTB_WINDOW
    cat = defaultdict(list)
    for fname in ("heldout", "oai"):
        for p in frames[fname]:
            if a <= p["month"] <= b:
                cat[("arxiv", p["category"])].append(p)
    for server in ("biorxiv", "medrxiv"):
        for p in frames[server]:
            if a <= p["month"] <= b:
                cat[(server, p["category"])].append(p)
    dropped = []
    for (server, c), papers in sorted(cat.items()):
        rule = D.TESTB_MIN_PER_YEAR * 4 if server == "arxiv" else D.TESTB_MIN_RXIV
        if len(papers) < rule:
            dropped.append((server, c, len(papers)))
            continue
        add(f"B-{server}", c, papers, D.TESTB_N)
    with gzip.open(os.path.join(repo, "data/processed/nd_samples.csv.gz"), "wt", newline="") as f:
        w = csv.writer(f)
        w.writerow(["design", "stratum", "paper_key"])
        w.writerows(samples)
    with open(os.path.join(repo, "data/processed/nd_frame_counts.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["design", "stratum", "frame_size"])
        w.writerows(sizes)
        for server, c, n in dropped:
            w.writerow([f"B-{server}-dropped", c, n])
    keys = sorted({k for _, _, k in samples})
    json.dump([{"id": k, "domain": by_key[k]["domain"], "title": by_key[k]["title"], "abstract": by_key[k]["abstract"],
                "comments": by_key[k]["comments"]} for k in keys],
              open(os.path.join(work, "classifier_input_full.json"), "w"), ensure_ascii=False)
    print({d: sum(1 for s in samples if s[0] == d) for d in sorted({s[0] for s in samples})}, "unique papers:", len(keys),
          "dropped categories:", len(dropped))


if __name__ == "__main__":
    main(*sys.argv[1:])
