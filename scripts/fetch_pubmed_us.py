"""PubMed journal articles per quarter by entry date ([edat]), with and without a US affiliation, 2019-Q1 to 2026-Q3.

"US" means at least one author affiliation matching usa[ad] OR "united states"[ad] (PubMed indexes the affiliations
of all authors from 2014). Used to test whether the 2025-26 slowdown in biomedicine is concentrated in US-affiliated
work, as a US funding shock (NIH grant terminations from February 2025) would predict.
Pacing: one request every 0.4 s (E-utilities allow 3 per second without a key); no e-mail address is sent.
Usage: python3 scripts/fetch_pubmed_us.py data/raw/pubmed_us_quarterly.json
"""
import json
import sys
import time
import urllib.parse
import urllib.request

STARTS = {1: "01/01", 2: "04/01", 3: "07/01", 4: "10/01"}
ENDS = {1: "03/31", 2: "06/30", 3: "09/30", 4: "12/31"}
US = '(usa[ad] OR "united states"[ad])'


def count(term):
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&retmode=json"
           "&tool=academia-ia-state&term=" + urllib.parse.quote(term))
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "academia-ia-state research"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return int(json.load(r)["esearchresult"]["count"])
        except Exception:
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(term)


def main(out):
    rows = []
    for y in range(2019, 2027):
        for q in range(1, 5):
            if (y, q) > (2026, 3):
                break
            base = f'("{y}/{STARTS[q]}"[edat] : "{y}/{ENDS[q]}"[edat]) AND "journal article"[pt]'
            rec = {"quarter": f"{y}-Q{q}", "journal_article": count(base)}
            time.sleep(0.4)
            rec["us_affiliation"] = count(f"{base} AND {US}")
            time.sleep(0.4)
            rec["non_us"] = rec["journal_article"] - rec["us_affiliation"]
            rows.append(rec)
            print(rec, flush=True)
    json.dump(rows, open(out, "w"), indent=1)


if __name__ == "__main__":
    main(sys.argv[1])
