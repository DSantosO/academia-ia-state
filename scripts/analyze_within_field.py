"""Within-field contrasts: computational vs wet-lab biology (bioRxiv), theory vs experiment (arXiv physics),
and where medRxiv growth sits (subject categories and public-dataset papers).

Reads data/raw/biorxiv_category_monthly.csv and medrxiv_category_monthly.csv (harvest_rxiv_categories.py) and
data/raw/arxiv_archive_monthly.csv. medRxiv series leave out COVID-19 preprints (COVID_RE in title or abstract),
which were a third of medRxiv in 2022. bioRxiv counts come from the API's per-category totals (--counts), which
carry no COVID-19 flag, so bioRxiv series include COVID-19 preprints; their share by group is estimated from
sampled months (data/raw/biorxiv_covid_sample_2022.csv) and reported in the methods note.
Writes to data/processed/:
  within_field_quarterly.csv        quarter, start, series, papers, index_2022, yoy
  biorxiv_categories_growth.csv     one row per bioRxiv category
  medrxiv_categories_growth.csv     one row per medRxiv category
  medrxiv_public_dataset_quarterly.csv
Usage: python3 scripts/analyze_within_field.py [repo_dir]
"""
import csv
import os
import sys
from collections import defaultdict

LAST = "2026-Q3"
# Grouping fixed before looking at growth: computational and wet-lab cores as proposed by the essay session;
# everything else is mixed. Genomics is also reported on its own and the computational group is rerun without it.
COMPUTATIONAL = {"bioinformatics", "systems biology", "genomics"}
WET_LAB = {"biochemistry", "cell biology", "developmental biology", "molecular biology", "microbiology", "immunology",
           "plant biology", "physiology", "cancer biology", "pharmacology and toxicology", "pathology",
           "synthetic biology"}
THEORY = ["hep-th", "hep-ph", "gr-qc", "nucl-th"]
EXPERIMENT = ["hep-ex", "nucl-ex"]


def quarter(month):
    return f"{month[:4]}-Q{(int(month[5:7]) - 1) // 3 + 1}"


def start(q):
    return f"{q[:4]}-{3 * (int(q[-1]) - 1) + 1:02d}-01"


def prev_year(q):
    return f"{int(q[:4]) - 1}{q[4:]}"


def load_rxiv(path):
    """{category: {quarter: papers without COVID-19}}, {category: {quarter: covid}}, {category: {quarter: public}}"""
    papers, covid, public = defaultdict(lambda: defaultdict(int)), defaultdict(lambda: defaultdict(int)), \
        defaultdict(lambda: defaultdict(int))
    for r in csv.DictReader(open(path)):
        q = quarter(r["month"])
        if q > LAST:
            continue
        c = r["category"]
        cov, pub = int(r["covid"] or 0), int(r["public_dataset"] or 0)  # empty in --counts files
        papers[c][q] += int(r["new_papers"]) - cov
        covid[c][q] += cov
        public[c][q] += pub
    return papers, covid, public


def series_rows(name, s, first="2019-Q1"):
    qs = sorted(q for q in s if q >= first)
    base = sum(s.get(f"2022-Q{i}", 0) for i in range(1, 5)) / 4
    out = []
    for q in qs:
        p = s[q]
        py = s.get(prev_year(q))
        out.append({"quarter": q, "start": start(q), "series": name, "papers": p,
                    "index_2022": round(100 * p / base, 1) if base else "",
                    "yoy": round(p / py - 1, 4) if py else ""})
    return out


def sum_cats(papers, cats):
    s = defaultdict(int)
    for c in cats:
        for q, v in papers.get(c, {}).items():
            s[q] += v
    return s


def q123(s, year):
    return sum(s.get(f"{year}-Q{i}", 0) for i in (1, 2, 3))


def category_table(papers, covid, public, group_of):
    rows = []
    for c in sorted(papers):
        s = papers[c]
        y22 = sum(s.get(f"2022-Q{i}", 0) for i in range(1, 5))
        a24, a25, a26 = q123(s, 2024), q123(s, 2025), q123(s, 2026)
        pub = public[c]
        all22 = y22 + sum(covid[c].get(f"2022-Q{i}", 0) for i in range(1, 5))
        all26 = a26 + q123(covid[c], 2026)
        rows.append({
            "category": c, "group": group_of(c), "papers_2022": y22, "papers_q1q3_2024": a24,
            "papers_q1q3_2025": a25, "papers_q1q3_2026": a26,
            "growth_q1q3_2025": round(a25 / a24 - 1, 4) if a24 else "",
            "growth_q1q3_2026": round(a26 / a25 - 1, 4) if a25 else "",
            "covid_share_2020": round(sum(covid[c].get(f"2020-Q{i}", 0) for i in range(1, 5)) / max(1, sum(
                covid[c].get(f"2020-Q{i}", 0) + s.get(f"2020-Q{i}", 0) for i in range(1, 5))), 4),
            "public_dataset_share_2022": round(sum(pub.get(f"2022-Q{i}", 0) for i in range(1, 5)) / all22, 4)
            if all22 and any(pub.values()) else "",
            "public_dataset_share_q1q3_2026": round(q123(pub, 2026) / all26, 4) if all26 and any(pub.values()) else "",
        })
    return sorted(rows, key=lambda r: -r["papers_q1q3_2026"])


def write(path, rows):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def group_bio(c):
    return "computational" if c in COMPUTATIONAL else "wet_lab" if c in WET_LAB else "mixed"


def main(repo):
    raw, out = os.path.join(repo, "data/raw"), os.path.join(repo, "data/processed")
    rows = []

    bio, bio_cov, bio_pub = load_rxiv(os.path.join(raw, "biorxiv_category_monthly.csv"))
    mixed = set(bio) - COMPUTATIONAL - WET_LAB
    for name, cats in [("biorxiv_computational", COMPUTATIONAL), ("biorxiv_wet_lab", WET_LAB),
                       ("biorxiv_mixed", mixed), ("biorxiv_computational_without_genomics",
                                                  COMPUTATIONAL - {"genomics"}),
                       ("biorxiv_genomics", {"genomics"}), ("biorxiv_neuroscience", {"neuroscience"}),
                       ("biorxiv_all", set(bio))]:
        rows += series_rows(name, sum_cats(bio, cats))
    write(os.path.join(out, "biorxiv_categories_growth.csv"), category_table(bio, bio_cov, bio_pub, group_bio))

    med, med_cov, med_pub = load_rxiv(os.path.join(raw, "medrxiv_category_monthly.csv"))
    rows += series_rows("medrxiv_all_excl_covid", sum_cats(med, set(med)), first="2019-Q3")  # opened June 2019
    # public-dataset shares among non-COVID preprints, from the text-feature harvest (harvest_rxiv_text_features.py):
    # a denominator that includes COVID-19 preprints makes the share rise spuriously as COVID research fades
    pub_nc, n_nc = defaultdict(lambda: defaultdict(int)), defaultdict(lambda: defaultdict(int))
    for r in csv.DictReader(open(os.path.join(raw, "medrxiv_text_main.csv"))):
        q = quarter(r["month"])
        if q <= LAST:
            pub_nc[r["category"]][q] += int(r["public_noncovid"])
            n_nc[r["category"]][q] += int(r["papers_noncovid"])
    table = category_table(med, med_cov, med_pub, lambda c: "")
    for row in table:
        c = row["category"]
        d22 = sum(n_nc[c].get(f"2022-Q{i}", 0) for i in range(1, 5))
        d26 = q123(n_nc[c], 2026)
        row["public_dataset_share_2022"] = round(sum(pub_nc[c].get(f"2022-Q{i}", 0) for i in range(1, 5)) / d22, 4) \
            if d22 else ""
        row["public_dataset_share_q1q3_2026"] = round(q123(pub_nc[c], 2026) / d26, 4) if d26 else ""
    write(os.path.join(out, "medrxiv_categories_growth.csv"), table)
    pub_rows = []
    for q in sorted({q for c in n_nc for q in n_nc[c] if q >= "2019-Q3"}):
        n = sum(n_nc[c].get(q, 0) for c in n_nc)
        k = sum(pub_nc[c].get(q, 0) for c in pub_nc)
        pub_rows.append({"quarter": q, "start": start(q), "papers_noncovid": n, "public_dataset_noncovid": k,
                         "public_dataset_share": round(k / n, 4) if n else ""})
    write(os.path.join(out, "medrxiv_public_dataset_quarterly.csv"), pub_rows)

    arch = defaultdict(lambda: defaultdict(int))
    for r in csv.DictReader(open(os.path.join(raw, "arxiv_archive_monthly.csv"))):
        q = quarter(f"{r['year']}-{int(r['month']):02d}")
        if "2015-Q1" <= q <= LAST:
            arch[r["archive"]][q] += int(r["new"])
    rows += series_rows("arxiv_theory", sum_cats(arch, THEORY), first="2016-Q1")
    rows += series_rows("arxiv_experiment", sum_cats(arch, EXPERIMENT), first="2016-Q1")
    for a in THEORY + EXPERIMENT + ["q-bio"]:
        rows += series_rows("arxiv_" + a.replace("-", "_"), arch[a], first="2016-Q1")
    write(os.path.join(out, "within_field_quarterly.csv"), rows)

    by = defaultdict(dict)
    for r in rows:
        by[r["series"]][r["quarter"]] = r["papers"]
    print(f"{'series':42} {'idx26Q3':>7} {'yoy26Q3':>7}  growth Jan-Sep: 2021  2022  2023  2024  2025  2026")
    for name, s in by.items():
        idx = [r for r in rows if r["series"] == name and r["quarter"] == LAST][0]
        g = " ".join(f"{q123(s, y) / q123(s, y - 1) - 1:+5.0%}" if q123(s, y - 1) else "   - "
                     for y in range(2021, 2027))
        print(f"{name:42} {idx['index_2022']:>7} {idx['yoy']:>+7.0%}  {g}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
