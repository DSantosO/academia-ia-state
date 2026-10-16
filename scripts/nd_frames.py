"""Sampling frames and samples for the confirmatory ND/NN tests, with the design fixed in nd_design.py.

Frames (text kept outside the repository):
  held-out arXiv   harvest_arxiv_raw.py output HELDOUT_DIR/<archive>.raw.jsonl.gz (cond-mat, astro-ph, quant-ph by
                   primary category; first-version submission month)
  maths            OAI-PMH harvest (primary math.*; identifier month), for Test B
  HEP/nuclear      OAI-PMH harvests (primary hep-th, hep-ph, gr-qc, nucl-th, hep-ex, nucl-ex; identifier month), Test B
  bioRxiv/medRxiv  harvest_rxiv_records.py part files (version 1; posting month; medRxiv without COVID-19). bioRxiv
                   "epidemiology" and "clinical trials" preprints are left out: bioRxiv listed these categories only
                   until medRxiv opened (January-July 2019, about 95 a month, none afterwards), so keeping them would
                   put a composition break into the 2019 baseline.
Writes:
  data/processed/nd_samples.csv.gz       design, stratum, paper key (identifiers only)
  data/processed/nd_frame_counts.csv     design, stratum, frame size (monthly totals and category totals)
  data/processed/nd_sample_attributes.csv.gz  per sampled paper: announcement month (arXiv identifier month; posting
                                         month for bioRxiv/medRxiv), number of authors (held-out arXiv only) and genre
                                         (arXiv: the keyword genres of stats_round1.py; bioRxiv/medRxiv: "review" if
                                         the title names a review or meta-analysis), for the sensitivity analyses
  data/processed/nd_category_monthly.csv server, category, month, papers: monthly output by category for the Test B
                                         outcomes (held-out arXiv subcategories by first-version month, maths
                                         subcategories by identifier month, bioRxiv and medRxiv by first posting,
                                         every preprint once, medRxiv without COVID-19); the six HEP/nuclear archives
                                         come from data/raw/arxiv_archive_monthly.csv
  WORK_DIR/classifier_input_full.json    unique papers to classify (key, domain, title, abstract, comments)
With --only DESIGN_PREFIX (for example --only medrxiv) only the designs of that server are drawn, from the frames
available so far; draws are per stratum with fixed seeds, so they are identical to those of the full run.
Usage: python3 scripts/nd_frames.py HELDOUT_DIR OAI_DIR BIORXIV_PARTS MEDRXIV_PARTS WORK_DIR [repo_dir] [--only X]
"""
import csv
import glob
import gzip
import io
import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nd_design as D  # noqa: E402
from harvest_rxiv_categories import COVID_RE  # noqa: E402
from stats_round1 import classify as genre  # noqa: E402
from stats_within_field import ym_range  # noqa: E402

BIORXIV_MOVED = {"epidemiology", "clinical trials"}  # bioRxiv categories that moved to medRxiv in mid-2019
RXIV_REVIEW = re.compile(r"\breview\b|meta-?analy[sz]", re.I)


def gz_text(path):
    """gzip text file with a fixed header time, so that identical content gives identical bytes."""
    return io.TextIOWrapper(gzip.GzipFile(path, "wb", mtime=0), encoding="utf-8", newline="")


def arxiv_month(aid):
    return f"20{aid[:2]}-{aid[2:4]}"


def heldout(dir_):
    out = {}
    for arch in D.HN_ARCHIVES:
        for line in gzip.open(os.path.join(dir_, f"{arch}.raw.jsonl.gz"), "rt", encoding="utf-8"):
            r = json.loads(line)
            out[r["id"]] = {"key": "arxiv:" + r["id"], "domain": "arxiv", "archive": arch, "category": r["primary"],
                            "month": r["v1"][:7], "title": r["title"], "abstract": r["abstract"],
                            "comments": r["comments"], "announce": arxiv_month(r["id"]), "n_authors": r["n_authors"],
                            "genre": genre(r)}
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
                            "comments": " ".join((r.get("comments") or "").split()), "announce": f"20{m.group(1)}-{m.group(2)}",
                            "n_authors": "", "genre": genre(r)}
    return list(out.values())


def rxiv(parts, server):
    out = {}
    for fn in sorted(glob.glob(os.path.join(parts, "*.csv"))):
        for r in csv.DictReader(open(fn)):
            if r["doi"] in out or not r["abstract"]:
                continue
            if server == "medrxiv" and COVID_RE.search(r["title"] + " " + r["abstract"]):
                continue
            if server == "biorxiv" and r["category"] in BIORXIV_MOVED:
                continue
            out[r["doi"]] = {"key": f"{server}:{r['doi']}", "domain": server, "archive": server,
                             "category": r["category"], "month": r["date"][:7], "title": r["title"],
                             "abstract": r["abstract"], "comments": "", "announce": r["date"][:7], "n_authors": "",
                             "genre": "review" if RXIV_REVIEW.search(r["title"]) else "research"}
    return list(out.values())


def category_months(frames, bio_parts, med_parts, only):
    """Monthly output by category for the Test B outcomes; bioRxiv and medRxiv count every preprint once, at its
    first version-1 listing, including the few without an abstract."""
    c = Counter()
    for p in frames["heldout"]:
        c[("arxiv", p["category"], p["month"])] += 1
    for p in frames["oai"]:
        if p["archive"] == "math":
            c[("arxiv", p["category"], p["month"])] += 1
    for server, parts in (("biorxiv", bio_parts), ("medrxiv", med_parts)):
        if only not in (None, server):
            continue
        first = {}
        for fn in sorted(glob.glob(os.path.join(parts, "*.csv"))):
            for r in csv.DictReader(open(fn)):
                if r["doi"] not in first or r["date"] < first[r["doi"]]["date"]:
                    first[r["doi"]] = r
        for r in first.values():
            if server == "medrxiv" and COVID_RE.search(r["title"] + " " + r["abstract"]):
                continue
            if server == "biorxiv" and r["category"] in BIORXIV_MOVED:
                continue
            c[(server, r["category"], r["date"][:7])] += 1
    return sorted((k + (n,) for k, n in c.items() if k[2] <= D.LAST))


def main(heldout_dir, oai_dir, bio_parts, med_parts, work, repo=".", only=None):
    os.makedirs(work, exist_ok=True)
    frames = {"heldout": heldout(heldout_dir) if only in (None, "arxiv") else [],
              "oai": oai(oai_dir) if only in (None, "arxiv") else [],
              "biorxiv": rxiv(bio_parts, "biorxiv") if only in (None, "biorxiv") else [],
              "medrxiv": rxiv(med_parts, "medrxiv") if only in (None, "medrxiv") else []}
    by_key = {p["key"]: p for f in frames.values() for p in f}
    samples, sizes = [], []

    def add(design, stratum, papers, n):
        sizes.append((design, stratum, len(papers)))
        for k in D.draw(design, stratum, [p["key"] for p in papers], n):
            samples.append((design, stratum, k))

    # HN
    for arch in (D.HN_ARCHIVES if only in (None, "arxiv") else []):
        grp = defaultdict(list)
        for p in frames["heldout"]:
            if p["archive"] == arch:
                grp[p["month"]].append(p)
        for m in ym_range(D.HN_FIRST, D.LAST):
            add("HN", f"{arch}|{m}", grp.get(m, []), D.per_month(m))
    # Test A
    for server, first in (("biorxiv", D.BIO_FIRST), ("medrxiv", D.MED_FIRST)):
        if only not in (None, server):
            continue
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
    suffix = f"_{only}" if only else ""
    with gz_text(os.path.join(repo, f"data/processed/nd_samples{suffix}.csv.gz")) as f:
        w = csv.writer(f)
        w.writerow(["design", "stratum", "paper_key"])
        w.writerows(samples)
    with open(os.path.join(repo, f"data/processed/nd_frame_counts{suffix}.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["design", "stratum", "frame_size"])
        w.writerows(sizes)
        for server, c, n in dropped:
            w.writerow([f"B-{server}-dropped", c, n])
    keys = sorted({k for _, _, k in samples})
    with gz_text(os.path.join(repo, f"data/processed/nd_sample_attributes{suffix}.csv.gz")) as f:
        w = csv.writer(f)
        w.writerow(["paper_key", "announce_month", "n_authors", "genre"])
        for k in keys:
            w.writerow([k, by_key[k]["announce"], by_key[k]["n_authors"], by_key[k]["genre"]])
    with open(os.path.join(repo, f"data/processed/nd_category_monthly{suffix}.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["server", "category", "month", "papers"])
        w.writerows(category_months(frames, bio_parts, med_parts, only))
    json.dump([{"id": k, "domain": by_key[k]["domain"], "title": by_key[k]["title"], "abstract": by_key[k]["abstract"],
                "comments": by_key[k]["comments"]} for k in keys],
              open(os.path.join(work, f"classifier_input_full{suffix}.json"), "w"), ensure_ascii=False)
    print({d: sum(1 for s in samples if s[0] == d) for d in sorted({s[0] for s in samples})}, "unique papers:", len(keys),
          "dropped categories:", len(dropped))


if __name__ == "__main__":
    args = sys.argv[1:]
    only = None
    if "--only" in args:
        i = args.index("--only")
        only = args[i + 1]
        args = args[:i] + args[i + 2:]
    main(*args, only=only)
