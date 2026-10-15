"""Harvest arXiv metadata (arXiv format) for one OAI-PMH set into a gzipped JSON-lines file.

Records are selected by OAI datestamp (last metadata change), so a harvest from date D contains
every paper created on or after D plus older papers updated since then; --min-created drops the latter.
Usage: python3 scripts/harvest_arxiv_oai.py --set math:math --from 2025-01-01 --min-created 2025-01-01 out.jsonl.gz
"""
import argparse
import gzip
import json
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

BASE = "https://oaipmh.arxiv.org/oai"
UA = "academia-ia-state research"
NS = {"o": "http://www.openarchives.org/OAI/2.0/", "a": "http://arxiv.org/OAI/arXiv/"}


def fetch(params):
    url = BASE + "?" + urllib.parse.urlencode(params)
    for attempt in range(8):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=300) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            wait = int(e.headers.get("Retry-After", 0) or 0) or 10 * (attempt + 1)
            time.sleep(wait)
        except Exception:
            time.sleep(10 * (attempt + 1))
    raise RuntimeError(f"failed: {url}")


def text(el, path):
    x = el.find(path, NS)
    return " ".join(x.text.split()) if x is not None and x.text else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--set", required=True)
    ap.add_argument("--from", dest="frm", required=True)
    ap.add_argument("--until")
    ap.add_argument("--min-created", default="0000-00-00")
    ap.add_argument("out")
    a = ap.parse_args()
    params = {"verb": "ListRecords", "metadataPrefix": "arXiv", "set": a.set, "from": a.frm}
    if a.until:
        params["until"] = a.until
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
                m = rec.find("o:metadata/a:arXiv", NS)
                created = text(m, "a:created") or ""
                if created < a.min_created:
                    continue
                authors = []
                for au in m.findall("a:authors/a:author", NS):
                    authors.append(" ".join(filter(None, [text(au, "a:forenames"), text(au, "a:keyname")])))
                out.write(json.dumps({
                    "id": text(m, "a:id"), "created": created, "updated": text(m, "a:updated"),
                    "categories": (text(m, "a:categories") or "").split(), "authors": authors,
                    "title": text(m, "a:title"), "comments": text(m, "a:comments"),
                    "msc": text(m, "a:msc-class"), "journal_ref": text(m, "a:journal-ref"),
                    "license": text(m, "a:license"), "abstract": text(m, "a:abstract"),
                }, ensure_ascii=False) + "\n")
                kept += 1
            pages += 1
            tok = lr.find("o:resumptionToken", NS)
            print(f"page {pages} kept {kept}", flush=True)
            if tok is None or not (tok.text or "").strip():
                break
            params = {"verb": "ListRecords", "resumptionToken": tok.text.strip()}
            time.sleep(2)
    print("done", pages, kept)


if __name__ == "__main__":
    main()
