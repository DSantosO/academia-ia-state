# Statistical methods (PLOS ONE analysis)

Written to be pasted into the article's Methods section. Every model below is implemented in `scripts/` and every
number in `results.md` is generated from the JSON files in `data/processed/stats/`.

## Data

- **arXiv, counts.** Monthly counts of new submissions by primary archive, January 2010 to September 2026, from arXiv's
  yearly statistics pages (`https://arxiv.org/year/<archive>/<year>`). Replacements and cross-lists are excluded.
- **arXiv, metadata.** Title, abstract, authors and categories from arXiv's OAI-PMH interface, harvested on
  16 October 2026 for the sets `math`, `physics:hep-th`, `physics:hep-ph`, `physics:gr-qc`, `physics:nucl-th`,
  `physics:hep-ex` and `physics:nucl-ex`, for papers first submitted from January 2019. Papers are dated by the month in
  their identifier (YYMM) and assigned to their primary category. Annual counts of primary hep-th and hep-ph papers
  from this harvest match arXiv's statistics exactly for 2019–2025. arXiv metadata are released under CC0.
- **bioRxiv.** Monthly counts of version-1 preprints by subject category, January 2019 to September 2026, from the
  bioRxiv API (`api.biorxiv.org/details/biorxiv/<interval>?category=<category>`, field `count_new_papers`).
  - From July 2019 the category sums equal bioRxiv's official monthly totals. In January–June 2019 they are about
    4% lower, because epidemiology and clinical-trials preprints, which later moved to medRxiv, cannot be queried by
    category.
  - Text features come from every version-1 preprint posted in March and September of each year, 2019–2026.
- **medRxiv.** Every version-1 preprint from June 2019 to September 2026, read through the same API, one day at a time.
  - COVID-19 preprints are those whose title or abstract mentions COVID-19, SARS-CoV-2 or 2019-nCoV; they are excluded
    from every medRxiv series.
  - "Public-dataset" preprints name in their title or abstract NHANES, UK Biobank, the Global Burden of Disease study,
    Mendelian randomisation, FAERS, MIMIC, SEER or BRFSS. These are data sources or designs that recur in formulaic
    papers.
- **Field series.** Physics is the sum of the 13 physics archives; mathematics is the math archive; computer science is
  the cs archive.
  - Biology is bioRxiv's official monthly new-paper count.
  - Medicine is medRxiv excluding COVID-19.
  - Social sciences are first versions on PsyArXiv, SocArXiv and EdArXiv (OSF API) plus arXiv econ and q-fin.
  - PubMed counts journal-article records by entry date.

## Within-field contrasts (H1)

The three confirmatory contrasts were fixed before the formal analysis:

| Contrast | Group A | Group B | Series |
|---|---|---|---|
| C1 physics | theory: hep-th, hep-ph, gr-qc, nucl-th | experiment: hep-ex, nucl-ex | arXiv, monthly, 2015-01 to 2026-09 |
| C2 biology | computational: bioinformatics, systems biology, genomics | wet lab: biochemistry, cell biology, developmental biology, molecular biology, microbiology, immunology, plant biology, physiology, cancer biology, pharmacology and toxicology, pathology, synthetic biology | bioRxiv, monthly, 2019-01 to 2026-09 |
| C3 medicine | names a public dataset | all other preprints | medRxiv excluding COVID-19, monthly, 2019-07 to 2026-09 |

**Main model.** Poisson pseudo-maximum likelihood with a log link, fitted to the two monthly series of a contrast
stacked (g ∈ {A, B}, months t):

    log E[y_gt] = λ_t + μ_{g, m(t)} + Σ_{k ≠ 2022} β_k · 1[g = A] · 1[year(t) = k]

- λ_t are month fixed effects. They absorb every shock common to both groups, including platform-wide changes in
  moderation, submission rules or traffic.
- μ_{g,m} are group-specific calendar-month effects (seasonality).
- exp(β_k) is the rate ratio of group A to group B in year k relative to 2022: the event-study coefficient.
- Standard errors are Driscoll–Kraay: heteroskedasticity and autocorrelation consistent over months, Bartlett
  kernel, 12 lags.
- Poisson pseudo-maximum likelihood is consistent under overdispersion, so a negative-binomial variance is not needed
  for the point estimates. The robust standard errors absorb the extra variance.

**Cross-checks of the 2026 estimate.**
- *Log ratio.* OLS on the monthly log ratio log(y_A/y_B), with calendar-month and year dummies and Newey–West
  standard errors (12 lags).
- *Bootstrap.* A moving-block bootstrap of that regression's residuals: 12-month blocks, 999 draws, percentile
  intervals.

**Trend-adjusted variant.** The same Poisson model, but with a group-specific linear trend instead of pre-2023 year
effects, plus group × year terms for 2023–2026. This measures departures from the extrapolated pre-2023 relative
trend.

**Placebo break dates.** Using pre-2023 months only, a group-specific linear trend plus a level shift of group A
starting in 2019, 2020 or 2021 (each placebo date where the series allows it).

**Break test with no pre-specified date.**
- *Series.* The deseasonalised monthly log ratio.
- *Model.* A broken-trend model, either r_t = a + b·t + c·(t − τ)₊ (a change in slope) or r_t = a + b·t + d·1[t ≥ τ]
  (a change in level).
- *Statistic.* The Newey–West Wald statistic for c (or d), computed for every τ in the central 70% of the sample. The
  sup-Wald statistic is the maximum over τ.
- *p-value.* From 999 parametric-bootstrap draws of the no-break model with AR(1) errors estimated from the data.
- *Date.* The break date is the τ that maximises the statistic.

**Negative controls.** The 2026 rate ratio (same model) for pairs where H1 predicts no divergence:
- the two experimental archives (hep-ex vs nucl-ex);
- every pair of theory archives;
- all 462 ways of splitting the 12 wet-lab categories into two halves of six;
- every pair among the 18 arXiv archives with complete monthly data since 2015 (153 pairs; an in-space placebo).

For each contrast we report the share of placebo pairs whose |log rate ratio| is at least as large as the contrast's.

**Leave-one-out.** C1 and C2 re-estimated dropping each component archive or category in turn.

**Sensitivity analyses.**
- Base year 2019 instead of 2022.
- Hep-ph removed from theory.
- Genomics removed from the computational group, or moved to wet lab.
- November 2025 to February 2026 dropped. These months follow arXiv's changes to review articles, endorsement and
  the English-version requirement.
- Sample ending October 2025, to estimate 2025 before those changes.

**Precision.** The minimum detectable 2026 rate ratio at 80% power and α = 0.05 is exp(2.80 · SE(β_2026)).

**Multiple comparisons.**
- *Confirmatory.* The family is the three 2026 rate ratios (C1–C3), with Holm-adjusted p-values.
- *Exploratory.* Everything else (other years, sensitivity analyses, negative controls, field-level and author-level
  analyses) is exploratory and reported as such.

## Field-level departures from trend

**Field model.** Poisson pseudo-maximum likelihood for a monthly series y_t:

    log E[y_t] = a + b·t + s_{m(t)} + c·COVID_t + Σ_{k=2023}^{2026} β_k · 1[year(t) = k]

- t is time in years and s_m are calendar-month effects.
- COVID_t marks April 2020 to March 2021.
- exp(β_k) is the ratio of observed to trend-expected counts in year k. The trend is identified from pre-2023 months.
- Newey–West standard errors, 12 lags (4 for quarterly series).

**Fit windows.**
- arXiv fields: 2015-01 to 2026-09.
- bioRxiv: from 2018.
- medRxiv and the social sciences: from 2019, flagged as unreliable because the servers were still being adopted.

**Unknown-break tests.** The same sup-Wald tests as above, applied to each field's deseasonalised log series.

**In-space placebo.** The field model fitted to each of the 18 arXiv archives; mathematics' 2026 departure is ranked
among them.

**Synthetic control** (Abadie, Diamond & Hainmueller 2010), following Nee, Zhong & Ni (2026).
- *Synthetic maths.* Mathematics' deseasonalised monthly log series is approximated by a convex combination of the
  other archives with complete data since 2018 (15 donors), fitted on January 2018 to December 2025 (demeaned).
- *Gap.* The 2026 gap is the mean difference over January–September 2026.
- *Inference.* Each donor is used in turn as the treated unit. The p-value is the rank of mathematics' post/pre
  root-mean-squared prediction error ratio among all units.
- *Robustness.* A second fit uses a pre-period ending in November 2022.

## Heavy producers (H2)

**Matching authors.** arXiv records carry no author identifiers, so authors are matched by normalised name strings:
ASCII-folded, lower-case and tokenised.

**Measures, by quarter and for January–August windows** (comparable with Nee et al. 2026):
- *Per paper:* the share of papers with at least one author who has five or more papers in the group that quarter.
- *Per author:* the shares of active authors with ≥5, ≥10 and ≥15 papers per quarter. ≥15 per quarter is roughly the
  >60 papers a year of Ioannidis, Collins & Baas (2024).
- *Output:* fractional output, with each paper split equally among its authors.
  - The share of the change in fractional output from Q3 2025 to Q3 2026 contributed by authors with five or more
    papers in Q3 2026.
  - The same share for the top 1% of authors by fractional output.

**Namesake robustness.** Full first names only; and full first names with the 1% most frequent surnames removed.

**Physics.** Results are also reported without papers that have more than 50 authors (collaboration papers).

**Intervals.** Wilson 95% intervals and two-proportion z-tests treat papers, or authors, as independent. Shared
authorship makes them too narrow, so they are a guide only.

## AI-writing markers (H3)

**Marker words.**
- *Source list.* The 407 "style" words of Kobak et al. (2025), from their published list
  (`github.com/berenslab/llm-excess-vocab`, `results/excess_words.csv`).
- *Core list.* Filtered by a rule that uses baseline data only: words whose pooled document frequency in 2019–2022,
  across all our corpora, is below 0.5% (list in `data/processed/stats/core_marker_words.txt`).

**Metric.** Distinct core marker words per 100 abstracts (title and abstract), by group and year; non-COVID preprints
only for bioRxiv and medRxiv.

**Tests.**
1. *Rise by group.* Each year's rate relative to the group's 2019–2022 mean.
2. *Same rise across groups.* Poisson model of marker counts with a log(abstracts) offset, period fixed effects and
   group × year terms, with base year 2022 and Driscoll–Kraay standard errors. A 2026 rate ratio near 1 means the
   marker rise is similar in both groups.
3. *Does the marker rise predict output growth, and only where experiments are not the bottleneck?*
   - *Panel.* A category-level panel of bioRxiv categories and arXiv archives, 2023–2026.
   - *Model.* growth_cy = a_y + b·Δmarker_cy + c·Δmarker_cy·experimental_c + d·experimental_c + e.
   - *Variables.* growth_cy is the log ratio of January–September papers in year y to 2022. Δmarker_cy is the marker
     rate in y minus the 2019–2022 mean. experimental_c is 1 for wet-lab or experimental, 0 for computational or
     theory, and 0.5 for mixed.
   - *Estimation.* OLS with standard errors clustered by category.

## Analyses tried and dropped

- **Bootstrap of papers for the per-paper heavy-producer share.** Dropped because resampling papers duplicates them,
  which inflates authors' paper counts and biases the share upward (for example 6% observed against a 15–22%
  bootstrap interval).
- **Trend-adjusted C2 as a headline estimate.** Dropped because its 2019–2022 pre-trend mixes late adoption of
  bioRxiv by wet-lab fields with the COVID-19 surge, and extrapolating it is not credible. It is reported only as a
  sensitivity analysis.
- **Field-level trend models for medRxiv and the social sciences.** Kept but flagged: their 2019–2022 trends reflect
  adoption of new servers, so departures from them are not interpretable as changes in output.
