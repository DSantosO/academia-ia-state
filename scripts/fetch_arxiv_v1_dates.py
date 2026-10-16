"""First-version submission dates of revised arXiv papers, from the arXiv API (`published` = submission time of v1).

The OAI-PMH arXiv format served by oaipmh.arxiv.org gives in `created` the submission date of the latest version, so for
papers revised after their first announcement it is not the first-version date (checked on arXiv abstract pages:
1902.06571 has created 2019-05-01, the date of its v2; its v1 is 18 February 2019). This script asks the API for those
papers only: identifiers from the OAI harvests whose `created` month is later than their identifier month, with
identifier months in [FIRST, LAST].
Pacing: arXiv API terms, at most one request every 3 s over a single connection; 200 identifiers per request.
Writes data/raw/arxiv_v1_dates.csv.gz (arxiv_id, v1_submitted); resumes from an existing file.
Usage: python3 scripts/fetch_arxiv_v1_dates.py OAI_DIR 2024-01 2026-10 data/raw/arxiv_v1_dates.csv.gz
"""
import csv
import gzip
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

UA = "academia-ia-state research"
NS = {"a": "http://www.w3.org/2005/Atom"}
ARCHIVES = {"math", "hep-th", "hep-ph", "gr-qc", "nucl-th", "hep-ex", "nucl-ex"}
BATCH = 200


def candidates(oai_dir, first, last):
    ids = set()
    for fn in sorted(os.listdir(oai_dir)):
        if not (fn.startswith("oai_") and fn.endswith(".jsonl.gz")):
            continue
        with gzip.open(os.path.join(oai_dir, fn), "rt", encoding="utf-8") as f:
            for line in f:
                r = json.loads(line)
                m = re.fullmatch(r"(\d{2})(\d{2})\.\d{4,5}", r.get("id") or "")
                if not m or not r.get("categories"):
                    continue
                prim = r["categories"][0]
                arch = "math" if prim.startswith("math.") else prim.split(".")[0]
                idm = f"20{m.group(1)}-{m.group(2)}"
                if arch in ARCHIVES and first <= idm <= last and (r.get("created") or "")[:7] > idm:
                    ids.add(r["id"])
    return sorted(ids)


def fetch(batch):
    url = ("https://export.arxiv.org/api/query?" +
           urllib.parse.urlencode({"id_list": ",".join(batch), "max_results": len(batch)}))
    for attempt in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=180) as r:
                root = ET.fromstring(r.read())
            out = {}
            for e in root.findall("a:entry", NS):
                aid = re.sub(r"v\d+$", "", e.find("a:id", NS).text.rsplit("/abs/", 1)[-1])
                out[aid] = e.find("a:published", NS).text[:10]
            return out
        except Exception:
            time.sleep(15 * (attempt + 1))
    raise RuntimeError(f"failed batch starting {batch[0]}")


def main(oai_dir, first, last, out):
    done = {}
    if os.path.exists(out):
        done = {r["arxiv_id"]: r["v1_submitted"] for r in csv.DictReader(gzip.open(out, "rt"))}
    todo = [i for i in candidates(oai_dir, first, last) if i not in done]
    print("to fetch:", len(todo), "already:", len(done), flush=True)
    for k in range(0, len(todo), BATCH):
        done.update(fetch(todo[k:k + BATCH]))
        if (k // BATCH) % 20 == 0 or k + BATCH >= len(todo):
            with gzip.open(out + ".tmp", "wt", newline="") as f:
                w = csv.writer(f)
                w.writerow(["arxiv_id", "v1_submitted"])
                w.writerows(sorted(done.items()))
            os.replace(out + ".tmp", out)
            print(k + BATCH, "of", len(todo), time.strftime("%H:%M:%S"), flush=True)
        time.sleep(3)


if __name__ == "__main__":
    main(*sys.argv[1:5])
