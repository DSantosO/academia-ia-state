"""Supporting Information tables assembled from the deposited data and estimates (review round 2, item 4).

S2 Table (docs/si/S2_Table.xlsx): January-September counts of new preprints by arXiv archive (2017-2026), bioRxiv
  category and medRxiv category (2019-2026), year-on-year growth, the range of that growth in 2018-2025, the COVID-19
  share (bioRxiv and medRxiv), the public-dataset share of non-COVID medRxiv preprints and the AI-topic share of
  bioRxiv (D3m list); and, for each contrasted pair, the log ratio of its January-September counts and its yearly
  change. Descriptive: the models use monthly counts with calendar-month effects.
S5 Table (docs/si/S5_Table.xlsx): every estimate in within_field_tests.json, field_tests.json, round1_tests.json,
  heavy_producers.json and h2_round2.json, and in the January-August versions (*_to_2026-08.json), one row per
  estimate (rate ratio, 95% CI, p, coefficient and standard error where present), plus every other number (counts,
  shares, statistics) in a second sheet, with a README sheet. The withdrawn marker analysis (marker_tests.json) and the
  pre-registered paper-level tests (nd_tests.json and the sealed files) are not included.
Usage: python3 scripts/build_si_tables.py [repo_dir]
"""
import csv
import gzip
import json
import math
import os
import sys
from collections import Counter, defaultdict

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stats_within_field import COMPUTATIONAL, EXPERIMENT, THEORY, WET_LAB  # noqa: E402

S5_FILES = ["within_field_tests.json", "field_tests.json", "round1_tests.json", "heavy_producers.json",
            "h2_round2.json", "within_field_tests_to_2026-08.json", "field_tests_to_2026-08.json",
            "round1_tests_to_2026-08.json"]


def jan_sep(rows, key, years, value=lambda r: 1, month="month"):
    """Counts (or sums of value) by key and year over January-September."""
    out = defaultdict(Counter)
    for r in rows:
        m = r[month][:7]
        if m[5:] <= "09" and int(m[:4]) in years:
            out[r[key]][int(m[:4])] += value(r)
    return out


def growth_table(counts, years, extra=None):
    recs = []
    for unit in sorted(counts):
        c = counts[unit]
        row = {"unit": unit}
        for y in years:
            row[f"jan_sep_{y}"] = c.get(y, 0)
        g = {}
        for y in years[1:]:
            if c.get(y - 1, 0) > 0:
                g[y] = c.get(y, 0) / c[y - 1] - 1
                row[f"growth_{y}"] = round(g[y], 4)
        past = [v for y, v in g.items() if y <= 2025]
        row["growth_range_to_2025_min"] = round(min(past), 4) if past else None
        row["growth_range_to_2025_max"] = round(max(past), 4) if past else None
        if extra:
            row.update(extra(unit))
        recs.append(row)
    return pd.DataFrame(recs)


def build_s2(repo, out):
    yrs_ax, yrs_rx = list(range(2017, 2027)), list(range(2019, 2027))
    ax = [{"archive": r["archive"], "month": f"{r['year']}-{int(r['month']):02d}", "new": int(r["new"])}
          for r in csv.DictReader(open(os.path.join(repo, "data/raw/arxiv_archive_monthly.csv")))]
    ax_counts = jan_sep(ax, "archive", yrs_ax, value=lambda r: r["new"])
    bio = list(csv.DictReader(gzip.open(os.path.join(repo, "data/raw/biorxiv_records.csv.gz"), "rt")))
    med = list(csv.DictReader(gzip.open(os.path.join(repo, "data/raw/medrxiv_records.csv.gz"), "rt")))
    bc = jan_sep(bio, "category", yrs_rx, month="date")
    mc = jan_sep(med, "category", yrs_rx, month="date")

    def shares(rows, flag, cond=lambda r: True):
        num, den = jan_sep([r for r in rows if cond(r)], "category", yrs_rx, value=lambda r: int(r[flag]), month="date"), \
            jan_sep([r for r in rows if cond(r)], "category", yrs_rx, month="date")
        return lambda unit: {f"{flag}_share_{y}": round(num[unit][y] / den[unit][y], 4) for y in yrs_rx
                             if den[unit][y]}
    bcov, bai = shares(bio, "covid_title_abstract"), shares(bio, "ai_topic")
    mcov = shares(med, "covid_title_abstract")
    mpub = shares(med, "public_dataset", cond=lambda r: r["covid_title_abstract"] != "1")
    sheets = {"arxiv_archives": growth_table(ax_counts, yrs_ax),
              "biorxiv_categories": growth_table(bc, yrs_rx, extra=lambda u: bcov(u) | bai(u)),
              "medrxiv_categories": growth_table(mc, yrs_rx, extra=lambda u: mcov(u) | {
                  k.replace("public_dataset", "public_dataset_noncovid"): v for k, v in mpub(u).items()})}
    # contrasted pairs: log ratio of January-September counts and its yearly change
    pairs = []
    bio_all = jan_sep(bio, "category", yrs_rx, month="date")
    nonc = [r for r in med if r["covid_title_abstract"] != "1"]
    c3 = jan_sep([dict(r, grp="public" if r["public_dataset"] == "1" else "other") for r in nonc], "grp", yrs_rx,
                 month="date")
    for name, a, b, years in (
            ("C1 theory / experiment (arXiv)", {y: sum(ax_counts[x][y] for x in THEORY) for y in yrs_ax},
             {y: sum(ax_counts[x][y] for x in EXPERIMENT) for y in yrs_ax}, yrs_ax),
            ("C2 computational / wet lab (bioRxiv)", {y: sum(bio_all[x][y] for x in COMPUTATIONAL) for y in yrs_rx},
             {y: sum(bio_all[x][y] for x in WET_LAB) for y in yrs_rx}, yrs_rx),
            ("C3 public dataset / other, without COVID-19 (medRxiv)", {y: c3["public"][y] for y in yrs_rx},
             {y: c3["other"][y] for y in yrs_rx}, yrs_rx)):
        prev = None
        for y in years:
            lr = math.log(a[y] / b[y]) if a[y] and b[y] else None
            pairs.append({"contrast": name, "year": y, "jan_sep_A": a[y], "jan_sep_B": b[y],
                          "log_ratio": round(lr, 4) if lr is not None else None,
                          "change_from_previous_year": round(lr - prev, 4) if lr is not None and prev is not None
                          else None})
            prev = lr
    sheets["contrasted_pairs"] = pd.DataFrame(pairs)
    readme = pd.DataFrame({"S2 Table": [
        "Growth by arXiv archive and by bioRxiv and medRxiv category (January-September of each year).",
        "arxiv_archives: new submissions by primary archive, arXiv statistics pages (data/raw/arxiv_archive_monthly.csv).",
        "biorxiv_categories, medrxiv_categories: version-1 preprints, one per DOI, from the record-level tables "
        "(data/raw/biorxiv_records.csv.gz, medrxiv_records.csv.gz). medRxiv started in June 2019, so its 2019 counts "
        "are partial and its 2020 growth is not comparable.",
        "growth_Y: count in Y over count in Y-1, minus 1. growth_range_to_2025_min/max: range of that growth over the "
        "years to 2025.",
        "covid_title_abstract_share_Y: share of preprints whose title or abstract names COVID-19 or SARS-CoV-2. "
        "ai_topic_share_Y (bioRxiv): share naming AI or machine learning as a topic (Deviation 3, D3m list). "
        "public_dataset_noncovid_share_Y (medRxiv): share of non-COVID preprints naming a public dataset or design.",
        "contrasted_pairs: log ratio of the January-September counts of the two groups of each contrast and its change "
        "from the previous year. Descriptive; the estimates in Table 1 use monthly counts with calendar-month effects.",
        "Built by scripts/build_si_tables.py from the deposited files."]})
    with pd.ExcelWriter(out) as xw:
        readme.to_excel(xw, sheet_name="README", index=False)
        for name, df in sheets.items():
            df.to_excel(xw, sheet_name=name, index=False)
    return {k: len(v) for k, v in sheets.items()}


def flatten(obj, path, est, other):
    if isinstance(obj, dict):
        if "rr" in obj and isinstance(obj["rr"], (int, float)):
            est.append({"path": path} | {k: obj.get(k) for k in ("rr", "lo", "hi", "p", "b", "se")})
            for k, v in obj.items():
                if k not in ("rr", "lo", "hi", "p", "b", "se"):
                    flatten(v, f"{path} > {k}", est, other)
            return
        for k, v in obj.items():
            flatten(v, f"{path} > {k}" if path else str(k), est, other)
    elif isinstance(obj, list):
        if all(isinstance(x, (int, float, str)) or x is None for x in obj):
            other.append({"path": path, "value": "; ".join("" if x is None else str(x) for x in obj)})
        else:
            for i, x in enumerate(obj):
                flatten(x, f"{path} > [{i}]", est, other)
    elif obj is not None:
        other.append({"path": path, "value": obj})


def build_s5(repo, out):
    d = os.path.join(repo, "data/processed/stats")
    est, other = [], []
    for fn in S5_FILES:
        p = os.path.join(d, fn)
        if not os.path.exists(p):
            continue
        e, o = [], []
        flatten(json.load(open(p)), "", e, o)
        est += [{"file": fn} | r for r in e]
        other += [{"file": fn} | r for r in o]
    doc = __import__("stats_round1").__doc__.split("Usage:")[0].strip().splitlines()
    readme = pd.DataFrame({"S5 Table": [
        "All estimates of the article and of the review analyses, one row per estimate ('estimates') and one per other "
        "number ('other_values'), read from the JSON files named in column 'file' (data/processed/stats/ in the deposit).",
        "path: the location of the number in its file, keys joined by ' > '. Files ending in _to_2026-08 hold the same "
        "analyses with the data ending in August 2026.",
        "estimates: rr = rate ratio (or ratio of observed to expected counts for departures from trend); lo, hi = 95% "
        "interval unless the path says otherwise (for example '_bonferroni', 98.3%); p = p value; b, se = log-scale "
        "coefficient and standard error.",
        "Fractional shares and growth are proportions (0.05 = 5%). Statistics describing fewer than ten authors are "
        "suppressed in heavy_producers.json and h2_round2.json.",
        "Not included: the withdrawn marker analysis (marker_tests.json, in the deposit) and the pre-registered "
        "paper-level tests (reported in S1 Text after unsealing).",
        "Sections of round1_tests.json (scripts/stats_round1.py):"] + [line.rstrip() for line in doc] + [
        "within_field_tests.json: C1-C3 as run (scripts/stats_within_field.py); field_tests.json: departures from "
        "trend, break tests, synthetic control (stats_fields.py); heavy_producers.json and h2_round2.json: H2 "
        "(stats_heavy_producers.py, stats_h2_round2.py).",
        "Built by scripts/build_si_tables.py."]})
    with pd.ExcelWriter(out) as xw:
        readme.to_excel(xw, sheet_name="README", index=False)
        pd.DataFrame(est).to_excel(xw, sheet_name="estimates", index=False)
        pd.DataFrame(other).to_excel(xw, sheet_name="other_values", index=False)
    return len(est), len(other)


def main(repo):
    out_dir = os.path.join(repo, "docs/si")
    os.makedirs(out_dir, exist_ok=True)
    print("S2", build_s2(repo, os.path.join(out_dir, "S2_Table.xlsx")))
    print("S5", build_s5(repo, os.path.join(out_dir, "S5_Table.xlsx")))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
