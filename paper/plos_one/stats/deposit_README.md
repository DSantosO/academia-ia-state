<!-- Copied from branch claude/happy-lovelace-wqek9b, commit 26ce2eb (companion analysis session). -->
# Data and code for "Publication counts after generative AI" (working title)

This folder describes the deposit-ready package: aggregate data, the scripts that produce them and every reported
estimate, and the terms of use of each source. The package is the repository itself (`academia-ia-state`); deposit a
tagged release on Zenodo. No individual preprint text is redistributed. Every file holds counts or aggregate
statistics.

## Contents

| Path | What it is |
|---|---|
| `data/raw/arxiv_archive_monthly.csv` | New arXiv submissions per month and primary archive, 2010–2026 (arXiv yearly statistics pages) |
| `data/raw/arxiv_monthly_submissions.csv` | arXiv's official monthly submission totals |
| `data/raw/biorxiv_sum_m.json`, `medrxiv_sum_m.json` | Official monthly new-paper totals (bioRxiv/medRxiv API `sum` endpoint) |
| `data/raw/biorxiv_category_monthly.csv` | bioRxiv version-1 preprints per month and subject category, 2019–2026 |
| `data/raw/medrxiv_category_monthly.csv` | medRxiv version-1 preprints per month and subject, with COVID-19 and public-dataset counts |
| `data/raw/medrxiv_covid_monthly.csv` | medRxiv new preprints per month, total and COVID-19-related |
| `data/raw/{biorxiv,medrxiv}_text_main.csv`, `*_text_words.csv.gz` | Aggregate text features (papers, words, documents containing each style word) per month and category; bioRxiv in March and September of each year |
| `data/raw/arxiv_text_main.csv`, `arxiv_text_words.csv.gz` | The same for arXiv maths (math.*) and six physics archives (hep-th, hep-ph, gr-qc, nucl-th, hep-ex, nucl-ex), January 2019 to September 2026 (from OAI-PMH metadata) |
| `data/raw/osf_quarterly.csv` | First versions per quarter on PsyArXiv, SocArXiv and EdArXiv (OSF API) |
| `data/raw/pubmed_edat_quarterly.json` | PubMed records per quarter by entry date (all, MEDLINE, journal articles) |
| `data/raw/kobak_style_words.csv` | The 407 style words of Kobak et al. (2025), from their repository (MIT licence) |
| `data/processed/` | Series used in the figures (one CSV/JSON per analysis) |
| `data/processed/stats/` | Every estimate reported in the article (JSON): `within_field_tests.json` (H1 contrasts), `field_tests.json` (field departures, breaks, synthetic control), `heavy_producers.json` (H2, aggregate shares only), `marker_tests.json` (H3); the core marker word list and the category panel |
| `docs/stats/methods.md` | Model specifications (Methods text) |
| `docs/stats/results.md` | All estimates with confidence intervals, generated from the JSON files |
| `docs/stats/figure_captions.md` | Figure captions |
| `docs/figures/plos/` | Article figures (TIFF, PDF, SVG) |
| `scripts/` | Download, processing, statistics and plotting scripts (Python 3; numpy, pandas, statsmodels, scipy, matplotlib) |

Author-level analyses (heavy producers) are computed from arXiv OAI-PMH metadata at run time and only aggregate shares
are stored; names are never written to the package.

## Reproducing

```bash
pip install numpy pandas scipy statsmodels matplotlib pillow
# downloads (slow; arXiv asks for at most one request every three seconds)
scripts/fetch_arxiv_years.sh /tmp/arxiv_years 2010
python3 scripts/parse_arxiv.py /tmp/arxiv_years data/raw/arxiv_archive_monthly.csv
scripts/fetch_biorxiv_medrxiv.sh data/raw
python3 scripts/harvest_rxiv_categories.py biorxiv 2019-01 2026-09 data/raw/biorxiv_category_monthly.csv 4 --counts
python3 scripts/harvest_rxiv_text_features.py medrxiv 2019-06 2026-09 data/raw/medrxiv_text 4
python3 scripts/harvest_rxiv_text_features.py biorxiv 2019-03 2026-09 data/raw/biorxiv_text 4 --months 3,9
for s in math:math physics:hep-th physics:hep-ph physics:gr-qc physics:nucl-th physics:hep-ex physics:nucl-ex; do
  python3 scripts/harvest_arxiv_oai.py --set $s --from 2019-01-01 --min-created 2019-01-01 /tmp/oai_${s/:/_}.jsonl.gz
done
python3 scripts/fetch_pubmed_quarterly.py data/raw/pubmed_edat_quarterly.json
python3 scripts/osf_quarterly.py data/raw/osf_quarterly.csv
# processing, statistics, results.md and figures (about three minutes; with the OAI directory it also rebuilds the
# heavy-producer statistics and the arXiv text counts)
scripts/run_all.sh /tmp
```

Running `scripts/run_all.sh` on the committed data reproduces every file in `data/processed/`, `docs/stats/results.md`
and `docs/figures/plos/` byte for byte. Counts change slightly when the sources revise their records; the data in this package were retrieved on
15–16 October 2026. Random seeds are fixed (20261016).

## Sources and terms of use

| Source | Terms | What this package contains |
|---|---|---|
| arXiv statistics pages and OAI-PMH metadata | Descriptive metadata are available under CC0 1.0 ("You are free to use descriptive metadata about arXiv e-prints under the terms of the Creative Commons Universal (CC0 1.0) Public Domain Declaration"). Full texts are not covered. API use: at most one request every three seconds, one connection at a time ([arXiv API terms of use](https://info.arxiv.org/help/api/tou.html)). | Counts and aggregate word statistics; no e-print content |
| bioRxiv and medRxiv API (`api.biorxiv.org`) | The API page states no terms of use or licence for the returned metadata. Each preprint carries its own licence, reported in the API's `license` field. | Counts and aggregate word statistics only; no titles, abstracts or author names |
| OSF API v2 (PsyArXiv, SocArXiv, EdArXiv) | The Center for Open Science's Terms of Use cover API access. They forbid "unreasonable traffic loads" and harvesting personal data for commercial purposes, and state no metadata licence ([COS Terms of Use](https://github.com/CenterForOpenScience/cos.io/blob/master/TERMS_OF_USE.md)). | Quarterly counts only |
| PubMed (NCBI E-utilities) | Free; the PubMed baseline README asks users to acknowledge the National Library of Medicine and not to imply endorsement ([README](https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/README.txt)). E-utilities allow about three requests per second without a key. | Quarterly counts only |
| Kobak et al. (2025) excess-vocabulary list | MIT licence ([berenslab/llm-excess-vocab](https://github.com/berenslab/llm-excess-vocab)); cite Kobak, González-Márquez, Horvát & Lause, *Science Advances* 11(27): eadt3813 (2025) | The 407 words they annotate as "style", with part of speech |

### Request pacing (what the scripts do, and what was done for this package)

| Source and rule | Scripts now | Retrievals behind this package |
|---|---|---|
| arXiv statistics pages (`arxiv.org/year/...`): `robots.txt` sets `Crawl-delay: 15` and allows `/year` | `fetch_arxiv_years.sh` waits 15 s between requests | Retrieved on 15 October 2026 with a 1 s pause, shorter than the crawl delay. The script was corrected afterwards. |
| arXiv OAI-PMH (`oaipmh.arxiv.org`): at most one request every 3 s, one connection ([API terms](https://info.arxiv.org/help/api/tou.html)) | `harvest_arxiv_oai.py` waits 3 s after each response, one set at a time | One connection at a time. Each response took 5–15 s, so requests were at least 8 s apart, whatever the pause (2 s in early runs, 3 s later). |
| bioRxiv and medRxiv API (`api.biorxiv.org`): no stated limit, no `robots.txt` | 2 months in parallel by default, one request at a time per month, 0.3 s pause in the record and category harvesters | 2–4 parallel connections |
| OSF API v2: COS Terms of Use forbid "unreasonable traffic loads"; the osfr package documents 100 unauthenticated requests per hour | `osf_quarterly.py`, `osf_check_quarter.py` and `osf_continuity.py` wait 36 s between requests | `osf_quarterly.csv` was retrieved with 0.3–0.5 s pauses (a few hundred requests in total), faster than that documented rate; no request was refused. `osf_continuity.csv` was retrieved at the 36 s pace. |
| PubMed E-utilities: at most 3 requests per second without an API key | `fetch_pubmed_quarterly.py` waits 0.4 s and identifies itself with `tool=`; no e-mail address is sent | Same as now |

Acknowledgement: this work used arXiv's open-access interoperability and data from the National Library of Medicine,
bioRxiv, medRxiv and the Open Science Framework. None of them endorses it.

## Licence of this package (to be chosen by the authors)

Suggested: CC BY 4.0 for the derived data and documentation (PLOS requires data licences no more restrictive than
CC BY) and MIT for the code. The Kobak et al. word list keeps its MIT licence.

## Data availability statement (draft)

"All data and code are available at Zenodo (DOI: to be added). The package contains aggregate counts derived from
public interfaces of arXiv (metadata CC0), bioRxiv and medRxiv, the Open Science Framework and PubMed, together with
the scripts that download and process them and reproduce every figure and estimate. No individual-level data are
included."
