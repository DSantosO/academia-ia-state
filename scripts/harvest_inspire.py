"""INSPIRE-HEP records with arXiv e-prints whose primary category is hep-ex, hep-ph, hep-th, hep-lat, nucl-ex or
nucl-th, by month of earliest date, January 2017 to September 2026 (pre-registration section 10, exploratory).

One query per month (any of the six categories, earliest date in the month; up to 1000 records per page). Records are
kept when the first listed arXiv category (the primary) is one of the six, and dated by `preprint_date` (first arXiv
version), falling back to the earliest date. Only curated metadata and keyword flags are written, never names, e-mail
addresses or abstracts: data/raw/inspire_hep_records.csv.gz.
Flags from title and abstract: prospect/sensitivity wording, Snowmass 2021, European Strategy.
Terms: INSPIRE allows 15 requests per 5 s per IP; this script makes at most one per second. Most INSPIRE metadata are
CC0 (https://github.com/inspirehep/rest-api-doc).
Usage: python3 scripts/harvest_inspire.py [repo_dir]
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

UA = "academia-ia-state research"
ARCH = ["hep-ex", "hep-ph", "hep-th", "hep-lat", "nucl-ex", "nucl-th"]
FIELDS = ("control_number,arxiv_eprints,preprint_date,earliest_date,document_type,publication_type,inspire_categories,"
          "accelerator_experiments.legacy_name,collaborations.value,author_count,titles.title,abstracts.value")
PROSPECT = re.compile(
    r"\bprospects?\b|\bsensitivity (?:stud|projection|to (?:future|new physics at)|of (?:future|the proposed|the "
    r"planned|the upcoming))|\bprojected (?:sensitivit|precision|reach|limits?)\b|\bfuture (?:experiment|collider|"
    r"facilit|run|measurement|upgrade)|\bphysics (?:case|potential|reach)\b|\bfeasibility\b|\b(?:conceptual|technical) "
    r"design\b|\bdesign report\b|\bwhite paper\b|\bsnowmass\b|\beuropean strategy\b|\bletter of intent\b|"
    r"\bdiscovery potential\b|\bproposed (?:experiment|detector|facility|collider)\b|\bexpected (?:sensitivity|"
    r"precision|performance|reach)\b", re.I)
SNOWMASS = re.compile(r"snowmass", re.I)
ESPP = re.compile(r"european strategy|\bESPPU?\b|strategy for particle physics", re.I)


def get(params):
    url = "https://inspirehep.net/api/literature?" + urllib.parse.urlencode(params)
    for attempt in range(8):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA,
                                                                              "Accept": "application/json"}),
                                        timeout=180) as r:
                return json.load(r)
        except Exception:
            time.sleep(10 * (attempt + 1))
    raise RuntimeError(url)


def months(a="2017-01", b="2026-09"):
    y, m = map(int, a.split("-"))
    while f"{y}-{m:02d}" <= b:
        yield f"{y}-{m:02d}"
        m += 1
        if m == 13:
            y, m = y + 1, 1


def main(repo="."):
    out = os.path.join(repo, "data/raw/inspire_hep_records.csv.gz")
    q_cat = "(" + " or ".join(f"arxiv_eprints.categories:{a}" for a in ARCH) + ")"
    seen, rows = set(), []
    for ym in months():
        page, got = 1, 0
        while True:
            j = get({"q": f"{q_cat} and de {ym}", "size": 1000, "page": page, "fields": FIELDS, "sort": "mostrecent"})
            time.sleep(1)
            hits = j["hits"]["hits"]
            total = j["hits"]["total"]
            for h in hits:
                md = h["metadata"]
                eps = md.get("arxiv_eprints") or []
                if not eps or not eps[0].get("categories"):
                    continue
                prim = eps[0]["categories"][0]
                rid = md.get("control_number")
                if prim not in ARCH or rid in seen:
                    continue
                seen.add(rid)
                title = " ".join(t.get("title", "") for t in md.get("titles") or [])
                abstract = " ".join(a.get("value", "") for a in md.get("abstracts") or [])
                text = title + " " + abstract
                rows.append({
                    "recid": rid, "arxiv_id": eps[0].get("value"), "primary": prim,
                    "categories": ";".join(eps[0]["categories"]),
                    "date": md.get("preprint_date") or md.get("earliest_date") or "",
                    "earliest_date": md.get("earliest_date") or "",
                    "document_type": ";".join(md.get("document_type") or []),
                    "publication_type": ";".join(md.get("publication_type") or []),
                    "inspire_categories": ";".join(c.get("term", "") for c in md.get("inspire_categories") or []),
                    "experiments": ";".join(e.get("legacy_name", "") for e in md.get("accelerator_experiments") or []
                                            if e.get("legacy_name")),
                    "collaborations": ";".join(c.get("value", "") for c in md.get("collaborations") or []),
                    "author_count": md.get("author_count") if md.get("author_count") is not None else "",
                    "prospect_title": int(bool(PROSPECT.search(title))),
                    "prospect_title_abstract": int(bool(PROSPECT.search(text))),
                    "snowmass": int(bool(SNOWMASS.search(text))), "european_strategy": int(bool(ESPP.search(text)))})
            got += len(hits)
            if got >= total or not hits or page * 1000 >= 10000:
                break
            page += 1
        print(ym, total, "kept so far", len(rows), time.strftime("%H:%M:%S"), flush=True)
    rows.sort(key=lambda r: (r["date"], r["recid"]))
    with gzip.open(out, "wt", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print("written", out, len(rows))


if __name__ == "__main__":
    main(*sys.argv[1:])
