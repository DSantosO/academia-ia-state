# Data and code for "Publication counts after generative AI" (working title)

This folder describes the deposit-ready package: the data, the scripts that produce them and every reported
estimate, and the terms of use of each source. The package is the repository itself (`academia-ia-state`); deposit a
tagged release on Zenodo.

What is redistributed:
- aggregate counts and statistics (most files);
- record-level tables of identifiers (DOIs, arXiv identifiers, INSPIRE record numbers) with dates, categories and
  derived flags, listed below. They contain no author names, e-mail addresses, affiliations, titles or abstracts;
- titles and abstracts in one place only: the blind validation sheet of the pre-registered tests (`validation/`,
  400 papers). Its arXiv half is arXiv metadata (CC0); its bioRxiv and medRxiv half was drawn only from preprints under
  Creative Commons licences. The sealed key in `validation/sealed/` gives each paper's DOI or arXiv identifier, for
  attribution, once the blind coding is finished.

What is not redistributed: the arXiv OAI-PMH and arXivRaw harvests (they contain author names) and any author-level
or paper-level heavy-producer flag. The author-level analyses (H2) store only aggregate shares.

## Contents

Aggregate data:

| Path | What it is |
|---|---|
| `data/raw/arxiv_archive_monthly.csv` | New arXiv submissions per month and primary archive, 2010–2026 (arXiv yearly statistics pages) |
| `data/raw/arxiv_monthly_submissions.csv` | arXiv's official monthly submission totals |
| `data/raw/biorxiv_sum_m.json`, `medrxiv_sum_m.json` | Official monthly new-paper totals (bioRxiv/medRxiv API `sum` endpoint) |
| `data/raw/biorxiv_category_monthly.csv` | bioRxiv version-1 preprints per month and subject category, 2019–2026 |
| `data/raw/biorxiv_records_monthly.csv` | bioRxiv version-1 preprints per month from the record-level harvest (unique DOIs) |
| `data/raw/medrxiv_category_monthly.csv` | medRxiv version-1 preprints per month and subject, with COVID-19 and public-dataset counts |
| `data/raw/medrxiv_covid_monthly.csv` | medRxiv new preprints per month, total and COVID-19-related |
| `data/raw/pubmed_edat_quarterly.json`, `pubmed_us_quarterly.json` | PubMed records per quarter by entry date (all, MEDLINE, journal articles; with and without a US affiliation) |
| `data/raw/osf_quarterly.csv` | First versions per quarter on PsyArXiv, SocArXiv and EdArXiv (OSF API). Not used in the article's figures or tables: the series changes method in 2025 and its continuity could not be checked |
| `data/processed/` | Series used in the figures and tables (one CSV/JSON per analysis) |
| `data/processed/stats/` | Every estimate reported in the article (JSON): `within_field_tests.json` (H1 contrasts), `field_tests.json` (field departures, breaks, synthetic control), `round1_tests.json` (review analyses, including the planned specification and the rank-based calibration), `heavy_producers.json` (H2, aggregate shares only), `nd_tests.json` (pre-registered test of medRxiv, Test A) |
| `validation/sealed/` | Sealed results and labels of the pre-registered tests (SHA-256 hashes in `validation/README.md`) |

Record-level identifier tables (no names, titles or abstracts):

| Path | Rows | Columns |
|---|---|---|
| `data/raw/biorxiv_records.csv.gz` | One per bioRxiv version-1 preprint, 2019–2026 (unique DOIs) | `doi, date, category, country, group`; `country` is US or non-US for the corresponding author's institution, classified by `scripts/classify_country.py` from the API's institution field |
| `data/raw/medrxiv_records.csv.gz` | One per medRxiv version-1 preprint, mid-2019 to 2026 (unique DOIs) | `doi, date, category, country` and keyword flags: COVID-19 in the title, or in the title or abstract; public dataset (original list; Spick et al.'s four added datasets) |
| `data/raw/inspire_hep_records.csv.gz` | One per INSPIRE-HEP record with a primary arXiv category in hep-ex, hep-ph, hep-th, hep-lat, nucl-ex or nucl-th, 2017–2026 | INSPIRE record id, arXiv id, categories, dates, document and publication types, INSPIRE categories, experiments, collaborations, author count, keyword flags (prospects, Snowmass, European Strategy) |
| `data/raw/arxiv_v1_dates.csv.gz` | One per arXiv paper in maths and the six HEP/nuclear archives with a first version from December 2023 | `arxiv_id, v1_submitted` (from arXivRaw) |
| `data/processed/arxiv_paper_flags.csv.gz` | One per arXiv paper in maths and the six HEP/nuclear archives, 2019–2026 | identifier, months and dates, categories, author count, genre and Snowmass/European Strategy flags |
| `data/processed/nd_samples_{arxiv,biorxiv,medrxiv}.csv.gz` | The stratified random samples of the pre-registered tests | `design, stratum, paper_key` |
| `data/processed/nd_sample_attributes_*.csv.gz` | The sampled papers | month, author count, genre and keyword flags used by the registered sensitivities |
| `data/processed/nd_frame_counts_*.csv`, `nd_category_monthly_*.csv` | Sampling frames | papers per stratum or category and month |
| `docs/stats/validation/medrxiv_flag_coding_sheet.csv` | 200 medRxiv preprints flagged by the COVID-19 or dataset rules, for a hand check | DOI, DOI link and flag (no titles) |

Text and code:

| Path | What it is |
|---|---|
| `docs/stats/methods.md`, `docs/stats/results.md` | Model specifications; all estimates with confidence intervals, generated from the JSON files |
| `docs/stats/figure_captions.md`, `docs/figures/plos/` | Figure captions; article figures (TIFF, PDF, SVG) |
| `scripts/` | Download, processing, statistics and plotting scripts |
| `requirements.txt` | Pinned versions of the Python packages used for every committed output (Python 3.13.16) |

The AI-vocabulary marker files (`data/raw/*_text_main.csv`, `*_text_words.csv.gz`, `arxiv_text_core_any.csv`,
`kobak_style_words.csv`, `data/processed/stats/marker_tests.json`, `marker_growth_panel.csv`, `core_marker_words.txt`)
and `scripts/stats_markers.py` remain in the repository but are not used by the article: the marker metric was
dropped, and `run_all.sh` no longer runs it.

## Reproducing

```bash
pip install -r requirements.txt     # Python 3.13
# downloads (slow; arXiv asks for at most one request every three seconds)
scripts/fetch_arxiv_years.sh /tmp/arxiv_years 2010
python3 scripts/parse_arxiv.py /tmp/arxiv_years data/raw/arxiv_archive_monthly.csv
scripts/fetch_biorxiv_medrxiv.sh data/raw
python3 scripts/harvest_rxiv_categories.py biorxiv 2019-01 2026-09 data/raw/biorxiv_category_monthly.csv 4 --counts
python3 scripts/harvest_rxiv_records.py biorxiv 2019-01 2026-09 /tmp/rxiv_parts_biorxiv 2
python3 scripts/harvest_rxiv_records.py medrxiv 2019-06 2026-09 /tmp/rxiv_parts_medrxiv 2
for s in math:math physics:hep-th physics:hep-ph physics:gr-qc physics:nucl-th physics:hep-ex physics:nucl-ex; do
  python3 scripts/harvest_arxiv_oai.py --set $s --from 2019-01-01 --min-created 2019-01-01 /tmp/oai_${s/:/_}.jsonl.gz
done
# arXivRaw (first-version dates), one archive at a time, e.g.
python3 scripts/harvest_arxiv_raw.py --set math:math --archive math --from 2024-01-01 --v1-from 2023-12-01 /tmp/raw_v1/math.raw.jsonl.gz
python3 scripts/v1_dates_from_raw.py data/raw/arxiv_v1_dates.csv.gz /tmp/raw_v1/*.raw.jsonl.gz
python3 scripts/harvest_inspire.py data/raw/inspire_hep_records.csv.gz
python3 scripts/fetch_pubmed_quarterly.py data/raw/pubmed_edat_quarterly.json
# processing, statistics, results.md and figures; with the OAI directory it also rebuilds the heavy-producer
# statistics and the OAI-based review analyses
scripts/run_all.sh /tmp
```

Running `scripts/run_all.sh` on the committed data with the pinned packages reproduces the files in `data/processed/`,
`docs/stats/results.md` and `docs/figures/plos/`. Counts change slightly when the sources revise their records; the
data were retrieved on 15–17 October 2026. Random seeds are fixed (20261016).

## Sources and terms of use

| Source | Terms | What this package contains |
|---|---|---|
| arXiv statistics pages, OAI-PMH metadata and arXivRaw | Descriptive metadata are available under CC0 1.0 ("You are free to use descriptive metadata about arXiv e-prints under the terms of the Creative Commons Universal (CC0 1.0) Public Domain Declaration"). Full texts are not covered. API use: at most one request every three seconds, one connection at a time ([arXiv API terms of use](https://info.arxiv.org/help/api/tou.html)). | Counts; identifier tables; titles, abstracts and comments of the 200 arXiv papers of the validation sheet |
| bioRxiv and medRxiv API (`api.biorxiv.org`) | The API page states no terms of use or licence for the returned metadata. Each preprint carries its own licence, reported in the API's `license` field. | Counts; DOI tables with dates, categories, a US/non-US flag and keyword flags; titles and abstracts of 200 CC-licensed preprints in the validation sheet |
| INSPIRE-HEP REST API (`inspirehep.net/api`) | At most 15 requests per 5 s per IP; most INSPIRE metadata are released under CC0 ([INSPIRE REST API documentation](https://github.com/inspirehep/rest-api-doc)) | Record-level table of curated metadata and keyword flags, without names, titles or abstracts |
| OSF API v2 (PsyArXiv, SocArXiv, EdArXiv) | The Center for Open Science's Terms of Use cover API access. They forbid "unreasonable traffic loads" and harvesting personal data for commercial purposes, and state no metadata licence ([COS Terms of Use](https://github.com/CenterForOpenScience/cos.io/blob/master/TERMS_OF_USE.md)). | Quarterly counts only |
| PubMed (NCBI E-utilities) | Free; the PubMed baseline README asks users to acknowledge the National Library of Medicine and not to imply endorsement ([README](https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/README.txt)). E-utilities allow about three requests per second without a key. | Quarterly counts only |

### Request pacing (what the scripts do, and what was done for this package)

| Source and rule | Scripts now | Retrievals behind this package |
|---|---|---|
| arXiv statistics pages (`arxiv.org/year/...`): `robots.txt` sets `Crawl-delay: 15` and allows `/year` | `fetch_arxiv_years.sh` waits 15 s between requests | Retrieved on 15 October 2026 with a 1 s pause, shorter than the crawl delay. The script was corrected afterwards. |
| arXiv OAI-PMH (`oaipmh.arxiv.org`), including arXivRaw: at most one request every 3 s, one connection ([API terms](https://info.arxiv.org/help/api/tou.html)) | `harvest_arxiv_oai.py` and `harvest_arxiv_raw.py` wait 3 s after each response, one connection at a time | One connection at a time. Each response took 5–15 s, so requests were at least 8 s apart, whatever the pause (2 s in early runs, 3 s later). |
| arXiv API (`export.arxiv.org/api`): the same terms | `fetch_arxiv_v1_dates.py` waits 3 s; it is no longer used | Requests for first-version dates, and the planned draw of the validation sheet's arXiv half, were answered with HTTP 429 ("Rate exceeded"). The requests were stopped; no data from the API are used. First-version dates come from arXivRaw instead, and the validation sheet's arXiv half was drawn from the OAI-PMH harvests. |
| bioRxiv and medRxiv API (`api.biorxiv.org`): no stated limit, no `robots.txt` | Parallel connections: up to 4 in the category and text harvests (one per month), 2 in the record harvests; each connection makes one request at a time with a 0.3 s pause in the record and category harvesters | 2–4 parallel connections |
| INSPIRE-HEP REST API: 15 requests per 5 s per IP | `harvest_inspire.py` makes at most one request per second | Same as now |
| OSF API v2: COS Terms of Use forbid "unreasonable traffic loads"; the osfr package documents 100 unauthenticated requests per hour | `osf_quarterly.py`, `osf_check_quarter.py` and `osf_continuity.py` wait 36 s between requests | `osf_quarterly.csv` was retrieved with 0.3–0.5 s pauses (a few hundred requests in total), faster than that documented rate; the OSF API refused no request. The continuity check (`osf_continuity.py`) was not completed, and no continuity file is included. |
| PubMed E-utilities: at most 3 requests per second without an API key | `fetch_pubmed_quarterly.py` and `fetch_pubmed_us.py` wait 0.4 s and identify themselves with `tool=`; no e-mail address is sent | Same as now |

Acknowledgement: this work used arXiv's open-access interoperability, INSPIRE-HEP, and data from the National Library
of Medicine, bioRxiv, medRxiv and the Open Science Framework. None of them endorses it.

## Licence of this package (to be chosen by the authors)

Suggested: CC BY 4.0 for the derived data and documentation (PLOS requires data licences no more restrictive than
CC BY) and MIT for the code. The validation sheet's bioRxiv and medRxiv texts keep their own Creative Commons licences.

## Data availability statement (draft)

"All data and code are available at Zenodo (DOI: to be added). The package contains counts derived from public
interfaces of arXiv (metadata CC0), bioRxiv and medRxiv, INSPIRE-HEP, the Open Science Framework and PubMed;
record-level tables of preprint identifiers with dates, categories and derived flags, without names; the blind
validation sheet of the pre-registered tests; and the scripts that download and process the data and reproduce every
figure and estimate."
