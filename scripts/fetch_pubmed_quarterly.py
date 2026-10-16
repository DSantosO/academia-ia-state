"""PubMed records per quarter by entry date ([edat]), 2015-Q1 to 2026-Q3, via NCBI E-utilities (no key needed).

Three counts per quarter: all records, MEDLINE-indexed records (incomplete for recent quarters, which are still being
indexed) and records of publication type "journal article". Usage: python3 scripts/fetch_pubmed_quarterly.py out.json
"""
import json, sys, time, urllib.parse, urllib.request
out = sys.argv[1]
ENDS = {1: "03/31", 2: "06/30", 3: "09/30", 4: "12/31"}
STARTS = {1: "01/01", 2: "04/01", 3: "07/01", 4: "10/01"}
rows = []
for y in range(2015, 2027):
    for q in range(1, 5):
        if (y, q) > (2026, 3):
            break
        rng = f'("{y}/{STARTS[q]}"[edat] : "{y}/{ENDS[q]}"[edat])'
        rec = {"quarter": f"{y}-Q{q}"}
        for name, extra in (("all", ""), ("medline", " AND medline[sb]"), ("journal_article", ' AND "journal article"[pt]')):
            url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&retmode=json&term="
                   + urllib.parse.quote(rng + extra))
            for attempt in range(4):
                try:
                    req = urllib.request.Request(url, headers={"User-Agent": "academia-ia-state research"})
                    rec[name] = int(json.load(urllib.request.urlopen(req, timeout=40))["esearchresult"]["count"])
                    break
                except Exception as e:  # noqa: BLE001
                    time.sleep(2 * (attempt + 1))
            time.sleep(0.4)
        rows.append(rec)
        print(rec, flush=True)
json.dump(rows, open(out, "w"), indent=1)
