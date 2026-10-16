"""Harvest arXiv metadata in the arXivRaw format (which lists every version with its submission date) for one OAI-PMH
set, keeping papers whose primary category is in ARCHIVE and whose first version was submitted on or after
--v1-from. Writes gzipped JSON lines: id, v1 (first-version submission date), versions, primary, categories, n_authors,
title, abstract, comments.

Used for the held-out archives of the new-data test (cond-mat, astro-ph, quant-ph) and for first-version dates of
maths and HEP papers, because the arXiv API (export.arxiv.org) answered "429 Rate exceeded" from this environment and
the `created` field of the arXiv OAI format is the latest version's date.
Pacing: arXiv API terms, one request every 3 s (after each response), one connection.
Usage: python3 scripts/harvest_arxiv_raw.py --set physics:cond-mat --archive cond-mat --from 2017-01-01 \
           --v1-from 2017-01-01 out.jsonl.gz
"""
import argparse
import datetime as dt
import email.utils
import gzip
import json
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--set", required=True)
    ap.add_argument("--archive", required=True, help="primary-category prefix to keep, e.g. cond-mat or math")
    ap.add_argument("--from", dest="frm", required=True)
    ap.add_argument("--v1-from", default="0000-00-00")
    ap.add_argument("out")
    a = ap.parse_args()
    params = {"verb": "ListRecords", "metadataPrefix": "arXivRaw", "set": a.set, "from": a.frm}
    pages = kept = 0
    with gzip.open(a.out, "wt", encoding="utf-8") as out:
        while True:
            root = ET.fromstring(fetch(params))
            err = root.find("o:error", NS)
            if err is not None:
                print("OAI error:", err.get("code"), err.text)
                break
            lr = root.find("o:ListRecords", NS)
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
                out.write(json.dumps({
                    "id": text(m, "r:id"), "v1": vers[0], "versions": len(vers), "primary": cats[0],
                    "categories": cats, "n_authors": len([x for x in authors.replace(" and ", ",").split(",")
                                                          if x.strip()]),
                    "title": text(m, "r:title"), "abstract": text(m, "r:abstract"), "comments": text(m, "r:comments"),
                }, ensure_ascii=False) + "\n")
                kept += 1
            pages += 1
            tok = lr.find("o:resumptionToken", NS)
            print(f"page {pages} kept {kept}", flush=True)
            if tok is None or not (tok.text or "").strip():
                break
            params = {"verb": "ListRecords", "resumptionToken": tok.text.strip()}
            time.sleep(3)  # arXiv API terms: no more than one request every three seconds
    print("done", pages, kept)


if __name__ == "__main__":
    main()
