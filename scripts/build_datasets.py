"""Build the quarterly preprint series used by the "Preprints por campo" dashboard.

Inputs (data/raw/):
  arxiv_archive_monthly.csv  archive,year,month,new,cross  (from parse_arxiv.py)
  biorxiv_sum_m.json         bioRxiv monthly content summary (api.biorxiv.org/sum/m)
  medrxiv_sum_m.json         medRxiv monthly content summary (api.medrxiv.org/sum/m)
  osf_quarterly.csv          provider,quarter,new_papers,records,method  (from osf_quarterly.py)

Outputs (data/processed/):
  arxiv_campos_trimestral.json, biorxiv_medrxiv_trimestral.json,
  osf_sociales_trimestral.json   one file per dashboard dataset
  preprints_por_campo_trimestral.csv   all series joined, one row per quarter

Only complete quarters from 2020-T1 to the last quarter that ended before today are kept.
Usage: python3 scripts/build_datasets.py [data_dir]
"""
import csv
import datetime
import json
import os
import sys
from collections import Counter, defaultdict

PHYSICS = set("astro-ph cond-mat gr-qc hep-ex hep-lat hep-ph hep-th math-ph nlin nucl-ex nucl-th physics quant-ph".split())
FIRST = "2020-T1"


def quarter(y, m):
    return f"{y}-T{(m - 1) // 3 + 1}"


def quarter_start(q):
    y, n = q.split("-T")
    return f"{y}-{3 * (int(n) - 1) + 1:02d}-01"


def last_complete_quarter(today):
    y, n = today.year, (today.month - 1) // 3 + 1
    return f"{y - 1}-T4" if n == 1 else f"{y}-T{n - 1}"


def main(data_dir):
    raw, out = os.path.join(data_dir, "raw"), os.path.join(data_dir, "processed")
    os.makedirs(out, exist_ok=True)
    last = last_complete_quarter(datetime.date.today())
    s = defaultdict(Counter)

    for r in csv.DictReader(open(os.path.join(raw, "arxiv_archive_monthly.csv"))):
        k, a, n = quarter(int(r["year"]), int(r["month"])), r["archive"], int(r["new"])
        if a in PHYSICS:
            s["fisica"][k] += n
        elif a == "math":
            s["matematicas"][k] += n
        elif a in ("econ", "q-fin"):
            s["econ_finanzas"][k] += n
        elif a == "cs":
            s["informatica"][k] += n

    for key, fn in (("biorxiv", "biorxiv_sum_m.json"), ("medrxiv", "medrxiv_sum_m.json")):
        j = json.load(open(os.path.join(raw, fn)))
        rows = j[[x for x in j if x != "messages"][0]]
        for x in rows:
            y, m = map(int, x["month"].split("-"))
            s[key][quarter(y, m)] += int(x["new_papers"])

    for r in csv.DictReader(open(os.path.join(raw, "osf_quarterly.csv"))):
        y, n = r["quarter"].split("Q")
        s[r["provider"]][f"{y}-T{n}"] += int(r["new_papers"])

    quarters = sorted(q for q in s["fisica"] if FIRST <= q <= last)
    cols = ["fisica", "matematicas", "econ_finanzas", "informatica", "biorxiv", "medrxiv", "psyarxiv", "socarxiv", "edarxiv"]
    missing = [(c, q) for c in cols for q in quarters if q not in s[c]]
    if missing:
        sys.exit(f"missing values: {missing[:10]}")

    def rows(keys):
        return [{"trimestre": q, "inicio": quarter_start(q), **{k: s[k][q] for k in keys}} for q in quarters]

    files = {
        "arxiv_campos_trimestral.json": rows(["fisica", "matematicas", "econ_finanzas", "informatica"]),
        "biorxiv_medrxiv_trimestral.json": rows(["biorxiv", "medrxiv"]),
        "osf_sociales_trimestral.json": rows(["psyarxiv", "socarxiv", "edarxiv"]),
    }
    for name, data in files.items():
        with open(os.path.join(out, name), "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)

    with open(os.path.join(out, "preprints_por_campo_trimestral.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["trimestre", "inicio", "fisica", "matematicas", "biologia_biorxiv", "medicina_medrxiv",
                    "ciencias_sociales", "psyarxiv", "socarxiv", "edarxiv", "arxiv_econ_finanzas", "informatica_referencia"])
        for q in quarters:
            social = s["psyarxiv"][q] + s["socarxiv"][q] + s["edarxiv"][q] + s["econ_finanzas"][q]
            w.writerow([q, quarter_start(q), s["fisica"][q], s["matematicas"][q], s["biorxiv"][q], s["medrxiv"][q],
                        social, s["psyarxiv"][q], s["socarxiv"][q], s["edarxiv"][q], s["econ_finanzas"][q], s["informatica"][q]])
    print(f"{len(quarters)} quarters: {quarters[0]} .. {quarters[-1]}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data")
