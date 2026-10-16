"""Harvest arXiv metadata in the arXivRaw format (which lists every version with its submission date) for one OAI-PMH
set, keeping papers whose primary category is in ARCHIVE and whose first version was submitted on or after
--v1-from. Writes gzipped JSON lines: id, v1 (first-version submission date), versions, primary, categories, n_authors,
title, abstract, comments.

Used for the held-out archives of the new-data test (cond-mat, astro-ph, quant-ph) and for first-version dates of
maths and HEP papers, because the arXiv API (export.arxiv.org) answered "429 Rate exceeded" from this environment and
the `created` field of the arXiv OAI format is the latest version's date.
Pacing: arXiv API terms, one request every 3 s (after each response), one connection.
Resumable: each page is written to OUT.parts/NNNNN.jsonl.gz together with the next resumption token (state.json); a
run that finds OUT.parts continues from the saved token (or starts again if the token has expired), and the pages are
joined into OUT at the end.
Usage: python3 scripts/harvest_arxiv_raw.py --set physics:cond-mat --archive cond-mat --from 2017-01-01 \
           --v1-from 2017-01-01 out.jsonl.gz
"""
import argparse
import datetime as dt
import email.utils
import glob
import gzip
import json
import os
import shutil
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

BASE = "https://oaipmh.arxiv.org/oai"
UA = "academia-ia-state research"
NS = {"o": "http://www.openarchives.org/OAI/2.0/", "r": "http://arxiv.org/OAI/arXivRaw/"}


def fetch(params):
    url = BASE + "?" + urllib.parse.urlencode(params)
    for attempt in range(10):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=300) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            time.sleep(int(e.headers.get("Retry-After", 0) or 0) or 15 * (attempt + 1))
        except Exception:
            time.sleep(15 * (attempt + 1))
    raise RuntimeError(f"failed: {url}")


def text(el, path):
    x = el.find(path, NS)
    return " ".join(x.text.split()) if x is not None and x.text else ""


def records(lr, a):
    rows = []
    for rec in lr.findall("o:record", NS):
        if rec.find("o:header", NS).get("status") == "deleted":
            continue
        m = rec.find("o:metadata/r:arXivRaw", NS)
        cats = text(m, "r:categories").split()
        if not cats or not (cats[0] == a.archive or cats[0].startswith(a.archive + ".")):
            continue
        vers = []
        for v in m.findall("r:version", NS):
            d = email.utils.parsedate_to_datetime(text(v, "r:date"))
            vers.append(d.astimezone(dt.timezone.utc).strftime("%Y-%m-%d"))
        if not vers or vers[0] < a.v1_from:
            continue
        authors = text(m, "r:authors")
        rows.append({
            "id": text(m, "r:id"), "v1": vers[0], "versions": len(vers), "primary": cats[0],
            "categories": cats, "n_authors": len([x for x in authors.replace(" and ", ",").split(",") if x.strip()]),
            "title": text(m, "r:title"), "abstract": text(m, "r:abstract"), "comments": text(m, "r:comments"),
        })
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--set", required=True)
    ap.add_argument("--archive", required=True, help="primary-category prefix to keep, e.g. cond-mat or math")
    ap.add_argument("--from", dest="frm", required=True)
    ap.add_argument("--v1-from", default="0000-00-00")
    ap.add_argument("out")
    a = ap.parse_args()
    first = {"verb": "ListRecords", "metadataPrefix": "arXivRaw", "set": a.set, "from": a.frm}
    parts = a.out + ".parts"
    os.makedirs(parts, exist_ok=True)
    state_fn = os.path.join(parts, "state.json")
    st = json.load(open(state_fn)) if os.path.exists(state_fn) else {"page": 0, "kept": 0, "token": None}
    params = {"verb": "ListRecords", "resumptionToken": st["token"]} if st["token"] else first
    if st["page"]:
        print(f"resuming after page {st['page']}", flush=True)
    while True:
        root = ET.fromstring(fetch(params))
        err = root.find("o:error", NS)
        if err is not None:
            if err.get("code") == "badResumptionToken" and st["page"]:
                print("resumption token no longer valid; starting again", flush=True)
                for fn in glob.glob(os.path.join(parts, "*.jsonl.gz")):
                    os.remove(fn)
                st, params = {"page": 0, "kept": 0, "token": None}, first
                continue
            if err.get("code") == "noRecordsMatch":
                break
            raise SystemExit(f"OAI error: {err.get('code')} {err.text}")
        lr = root.find("o:ListRecords", NS)
        rows = records(lr, a)
        page = st["page"] + 1
        fn = os.path.join(parts, f"{page:05d}.jsonl.gz")
        with gzip.open(fn + ".tmp", "wt", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        os.replace(fn + ".tmp", fn)
        tok = lr.find("o:resumptionToken", NS)
        tok = (tok.text or "").strip() if tok is not None else ""
        st = {"page": page, "kept": st["kept"] + len(rows), "token": tok or None}
        json.dump(st, open(state_fn + ".tmp", "w"))
        os.replace(state_fn + ".tmp", state_fn)
        print(f"page {page} kept {st['kept']}", flush=True)
        if not tok:
            break
        params = {"verb": "ListRecords", "resumptionToken": tok}
        time.sleep(3)  # arXiv API terms: no more than one request every three seconds
    with open(a.out + ".tmp", "wb") as out:
        for fn in sorted(glob.glob(os.path.join(parts, "*.jsonl.gz"))):
            with open(fn, "rb") as f:
                shutil.copyfileobj(f, out)
    os.replace(a.out + ".tmp", a.out)
    shutil.rmtree(parts)
    print("done", st["page"], st["kept"])


if __name__ == "__main__":
    main()
