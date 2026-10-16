"""Continuity check for the OSF series (PsyArXiv, SocArXiv, EdArXiv) across the 2025-Q1 change in how OSF lists versions.

osf_quarterly.py counts new preprints as the API total before 2025 and, from 2025-Q1, by paging through the records and
keeping first versions (ids ending in _v1 or without a version suffix), because OSF began listing every version as its
own record. This script applies the paged first-version count to the last two quarters before the switch and to the
first quarter after it, and records how many of the first versions created in a quarter were published (date_published)
before that quarter, which would indicate re-imported older preprints.
Request pacing: one request every 36 s (100 unauthenticated requests per hour, osfr documentation).
Usage: python3 scripts/osf_continuity.py out.csv
"""
import csv
import json
import sys
import time
import urllib.request

UA = "academia-ia-state research"
PAUSE = 36
QUARTERS = [("2024Q3", "2024-07-01", "2024-10-01"), ("2024Q4", "2024-10-01", "2025-01-01"),
            ("2025Q1", "2025-01-01", "2025-04-01")]
PROVIDERS = ["psyarxiv", "socarxiv", "edarxiv"]


def get(url):
    for t in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=120) as r:
                return json.load(r)
        except Exception:
            time.sleep(PAUSE * (t + 1))
    raise RuntimeError(url)


def main(out):
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["provider", "quarter", "api_total", "records_paged", "first_versions",
                    "first_versions_published_before_quarter"])
        for p in PROVIDERS:
            for qn, s, e in QUARTERS:
                url = (f"https://api.osf.io/v2/preprints/?filter%5Bprovider%5D={p}&filter%5Bdate_created%5D%5Bgte%5D={s}"
                       f"&filter%5Bdate_created%5D%5Blt%5D={e}&page%5Bsize%5D=100"
                       "&fields%5Bpreprints%5D=date_created,date_published")
                total, ids, early = None, [], 0
                while url:
                    j = get(url)
                    total = total if total is not None else j["links"]["meta"]["total"]
                    for d in j["data"]:
                        i = d["id"]
                        ids.append(i)
                        first = i.endswith("_v1") or "_v" not in i
                        pub = (d.get("attributes") or {}).get("date_published") or ""
                        if first and pub and pub[:10] < s:
                            early += 1
                    url = j["links"].get("next")
                    time.sleep(PAUSE)
                v1 = sum(1 for i in ids if i.endswith("_v1") or "_v" not in i)
                w.writerow([p, qn, total, len(ids), v1, early])
                f.flush()
                print(p, qn, total, len(ids), v1, early, flush=True)


if __name__ == "__main__":
    main(sys.argv[1])
