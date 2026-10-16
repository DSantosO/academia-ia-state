"""Batches for the ND/NN/U classifier and collection of its labels (pre-registration Appendix A, Amendment 1 Appendix B).

split:   reads CLASSIFIER_INPUT (JSON list: id, domain, title, abstract, comments) and writes, per domain, batch files
         of at most BATCH papers: OUT_DIR/<domain>_<k>.json, each with the verbatim prompt for its domain.
collect: reads OUT_DIR/*_labels.csv written by the classifier runs (id,label), checks that every paper has exactly
         one label in {ND, NN, U}, and writes the gzip CSV LABELS_OUT (id, domain, label).
The classifier is a large language model run as one sub-agent per batch; each paper is judged on its own with the
verbatim prompt, and only the label is returned.
Blind batches (split ... --blind SEED): within each domain the papers are put in random order and given pseudonymous
ids (A00001, ... for arXiv; B for bioRxiv; M for medRxiv), so a batch shows neither identifiers nor dates (bioRxiv and
medRxiv DOIs and arXiv identifiers encode the posting month), and batches do not group papers by date. The mapping is
written to OUT_DIR/pseudonyms.csv; collect reads it and writes the labels under the original ids.
Usage: python3 scripts/classifier_batches.py split CLASSIFIER_INPUT OUT_DIR [batch] [--blind SEED]
       python3 scripts/classifier_batches.py collect CLASSIFIER_INPUT OUT_DIR LABELS_OUT
"""
import csv
import glob
import gzip
import json
import os
import random
import sys

PROMPTS = {
    "arxiv": (
        "Classify this physics or astronomy paper from its title, abstract and comments into exactly one class.\n\n"
        "ND — The paper reports NEW empirical data obtained by the authors: new measurements, experiments, or "
        "observations (including new telescope, satellite or detector observations), or the experimental "
        "characterisation of samples or devices the authors made or measured.\n\n"
        "NN — The paper does NOT report new empirical data. This includes theory or analytic results; numerical "
        "calculations or simulations (including first-principles/DFT); computational methods, algorithms, "
        "machine-learning methods or software; designs, proposals, or prospect/sensitivity studies for future "
        "experiments; reviews, perspectives, white papers or lecture notes; and reanalysis of existing, archival or "
        "public data without new data collection by the authors.\n\n"
        "U — It cannot be determined from the text.\n\n"
        "Rules:\n"
        "(1) If the paper combines new measurements or observations with theory or simulation, choose ND.\n"
        "(2) Analysis of public or archival datasets (e.g., public survey catalogues, public telescope archives, "
        "published databases) is NN unless the authors obtained new observations.\n"
        "(3) Fabricating and measuring a device or sample is ND; designing or simulating one is NN.\n"
        "(4) Answer with only the label: ND, NN or U."),
    "biorxiv": (
        "Classify this biology preprint from its title and abstract into one class. ND — the authors report NEW "
        "experimental or observational data they generated (wet-lab experiments, new sequencing or imaging they "
        "performed, field sampling, new clinical or patient samples). NN — no new experimental data: computational "
        "analysis of existing or public datasets, methods/software/algorithms, theory or mathematical modelling, "
        "simulations, reanalysis. U — cannot tell. If new experimental data are combined with computation, choose ND. "
        "Answer only ND, NN or U."),
    "medrxiv": (
        "Classify this medical/health preprint from its title and abstract into one class. ND — the authors collected "
        "NEW primary data (a trial, a newly recruited cohort or sample, a new survey, newly collected clinical samples "
        "or measurements). NN — no new primary data: secondary analysis of existing datasets, registries, electronic "
        "health records, administrative or public data (e.g., NHANES, UK Biobank), systematic reviews or "
        "meta-analyses, modelling or simulation. U — cannot tell. Answer only ND, NN or U."),
}

PREFIX = {"arxiv": "A", "biorxiv": "B", "medrxiv": "M"}


def split(inp, out_dir, batch=50, blind=None):
    batch = int(batch)
    os.makedirs(out_dir, exist_ok=True)
    rows = json.load(open(inp))
    alias = []
    for dom in PROMPTS:
        sel = [r for r in rows if r["domain"] == dom]
        if blind is not None:
            sel = sorted(sel, key=lambda r: r["id"])
            random.Random(f"{blind}|{dom}").shuffle(sel)
            names = [f"{PREFIX[dom]}{i + 1:05d}" for i in range(len(sel))]
            alias += zip(names, [r["id"] for r in sel])
            sel = [{**r, "id": a} for a, r in zip(names, sel)]
        items = [{"id": r["id"], "title": r["title"], "abstract": r["abstract"],
                  **({"comments": r["comments"]} if dom == "arxiv" else {})} for r in sel]
        for k in range(0, len(items), batch):
            json.dump({"domain": dom, "prompt": PROMPTS[dom], "papers": items[k:k + batch]},
                      open(os.path.join(out_dir, f"{dom}_{k // batch + 1:03d}.json"), "w"), indent=1,
                      ensure_ascii=False)
    if blind is not None:
        with open(os.path.join(out_dir, "pseudonyms.csv"), "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["pseudonym", "id"])
            w.writerows(alias)
    print({d: sum(1 for r in rows if r["domain"] == d) for d in PROMPTS})


def collect(inp, out_dir, labels_out):
    rows = json.load(open(inp))
    dom = {r["id"]: r["domain"] for r in rows}
    labels = {}
    pseud = os.path.join(out_dir, "pseudonyms.csv")
    real = {r["pseudonym"]: r["id"] for r in csv.DictReader(open(pseud))} if os.path.exists(pseud) else None
    for fn in sorted(glob.glob(os.path.join(out_dir, "*_labels.csv"))):
        for r in csv.reader(open(fn)):
            if not r or r[0] == "id":
                continue
            pid, lab = r[0].strip(), r[1].strip().upper()
            if real is not None:
                pid = real.get(pid, "unknown pseudonym " + pid)
            if pid in labels and labels[pid] != lab:
                raise SystemExit(f"conflicting labels for {pid}")
            labels[pid] = lab
    missing = sorted(set(dom) - set(labels))
    bad = {k: v for k, v in labels.items() if v not in ("ND", "NN", "U")}
    if missing or bad or set(labels) - set(dom):
        raise SystemExit(f"missing {missing[:10]} ({len(missing)}), bad {bad}, unknown {sorted(set(labels) - set(dom))[:5]}")
    with gzip.open(labels_out, "wt", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "domain", "label"])
        for pid in sorted(labels):
            w.writerow([pid, dom[pid], labels[pid]])
    print("labels:", len(labels))


if __name__ == "__main__":
    args = sys.argv[2:]
    kw = {}
    if "--blind" in args:
        i = args.index("--blind")
        kw["blind"] = args[i + 1]
        args = args[:i] + args[i + 2:]
    {"split": split, "collect": collect}[sys.argv[1]](*args, **kw)
