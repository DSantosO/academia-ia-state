<!-- Copied from branch claude/happy-lovelace-wqek9b, commit 7ac5647 (companion analysis session). -->
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
ASCII-folded, lower-case and tokenised. Papers are dated by the month in their identifier, from January 2019 to
September 2026 (October 2026 was incomplete at harvest).

**Measures, by quarter and for January–August windows** (comparable with Nee et al. 2026):
- *Per paper:* the share of papers with at least one author who has five or more papers in the group that quarter.
- *Per author:* the shares of active authors with ≥5, ≥10 and ≥15 papers per quarter. ≥15 per quarter is roughly the
  >60 papers a year of Ioannidis, Collins & Baas (2024).
- *Concentration:* the share of fractional output (each paper split equally among its authors) produced by the top
  1% and the top 10% of active authors.

Fixed-threshold measures (per paper, per author) rise mechanically when everyone publishes more: a uniform increase
in output pushes more authors over the threshold. The concentration shares do not move under proportional growth, so
they are the main test of whether the acceleration is broad-based or driven by a fringe.

**Departure from trend.** Each quarterly measure is regressed on a linear trend, quarter-of-year effects and dummies
for 2023, 2024, 2025 and 2026 (OLS, Newey–West standard errors, 4 lags). The year coefficients are departures from
the 2019–2022 trend, in percentage points.

**Who produced the growth?** The change in fractional output between the third quarters of consecutive years is
split by author class.
- *Classes.* Authors are ranked by their combined fractional output in the two years compared: the top 1%, the next
  9% and the bottom 90%. Authors tied at a class boundary share the remaining places equally (fractional
  membership, the expectation over random tie-breaking).
- *Why combined output.* Classes defined on one year select on that year's output, so they carry regression to the
  mean: authors who are heavy producers in the second year will, on average, have produced less in the first even if
  nothing changed. Ranking on the sum of both years is symmetric in the two years, so when the years are exchangeable
  each class's expected change is zero. Under proportional growth every class grows at the total rate.
- *Reference.* Pairs ending before ChatGPT's release (2019→2020, 2020→2021, 2021→2022) show how much the classes
  differ by chance.

**Namesake robustness.** Full first names only; and full first names with the 1% most frequent surnames removed.

**Physics.** Papers with more than 50 authors (collaboration papers) are excluded. With them, a handful of white papers
signed by hundreds of theorists make hundreds of authors "heavy producers" in a quarter (for example 16.9% of active
theory authors with ≥5 papers in Q3 2025, against 1.3% without them). Experimental physics has about 300 papers a
quarter with 50 or fewer authors, and few of their authors give full first names, so only its all-names version is
reported.

**Intervals.** Wilson 95% intervals and two-proportion z-tests (in the JSON output) treat papers, or authors, as
independent. Shared authorship makes them too narrow, so they are a guide only.

## AI-writing markers (H3)

**Text features.** Title plus abstract, lower-cased and split into alphabetic tokens.
- bioRxiv: every version-1 preprint posted in March and September of each year, 2019–2026.
- medRxiv: every version-1 preprint, June 2019 to September 2026.
- arXiv: every paper with primary category in maths (math.*) or in hep-th, hep-ph, gr-qc, nucl-th, hep-ex and
  nucl-ex, January 2019 to September 2026, from OAI-PMH metadata.
- COVID-19 preprints are excluded from bioRxiv and medRxiv.

**Marker words.**
- *Source list.* The 407 "style" words of Kobak et al. (2025), from their published list
  (`github.com/berenslab/llm-excess-vocab`, `results/excess_words.csv`). Their list was derived from PubMed abstracts.
- *Core list.* Filtered by a rule that uses baseline data only: words whose pooled document frequency in 2019–2022
  in the biomedical corpora (bioRxiv and medRxiv, matching the list's PubMed origin) is below 0.5%. This leaves 261
  words (`data/processed/stats/core_marker_words.txt`), and the same list is applied to every corpus.

**Metric.** Distinct core marker words per 100 abstracts, by group and year.

**Marker drift.** The words that identify LLM text change as models and authors change. The list was built from 2024
abstracts. Its words rose sharply in 2023–2024 and have fallen since, while abstract length stayed stable (bioRxiv
234–247 words per abstract in every sampled month from 2024 to 2026).
- Core words such as "delve", "intricate" and "underscores" peaked in 2024 and are back near baseline in 2026.
- By September 2026 some common words on the list are below their 2019–2022 frequency in bioRxiv: "crucial" appears in
  1.7% of abstracts against 4.5% before 2023, and "insights" in 4.4% against 6.2%. The fall is gradual across the
  sampled months (September 2024, March 2025, September 2025, March 2026, September 2026).
  It looks like deliberate avoidance of words now read as signs of LLM text, by authors and by newer models, not a
  change in the data.

Consequences:
- The marker rate is a lower bound on LLM-assisted writing, and from 2025 a weak one.
- Comparisons across years after 2024 are not interpretable as changes in LLM use.
- Comparisons across groups within a year remain valid if the groups use the same tools. 2024 is the cleanest year
  for them, because the list was built on 2024 text.

**Tests.**
1. *Rise by group.* Each year's rate relative to the group's 2019–2022 mean.
2. *Same rise across groups.*
   - *Model.* OLS of the monthly log ratio of marker rates, log(M_A/N_A) − log(M_B/N_B), on dummies for 2023, 2024,
     2025 and 2026. The reference is the pooled 2019–2022 baseline, which is more stable than a single base year,
     notably for small groups such as experimental physics.
   - *Inference.* Classical standard errors and t intervals. The bioRxiv text sample has only 16 months (March and
     September), too few for HAC or Driscoll–Kraay standard errors. Those came out about 2.5 times too narrow when
     checked against the month-to-month variation of 2019–2022.
   - *Reading.* A ratio near 1 means the marker rise is similar in both groups.
   - *Pairs.* bioRxiv computational vs wet lab; arXiv theory vs experiment; arXiv maths vs experiment.
3. *Does the marker rise predict output growth, and only where experiments are not the bottleneck?*
   - *Panel.* A category-level panel of bioRxiv categories and arXiv archives, 2023–2026.
   - *Model.* growth_cy = a_y + b·Δmarker_cy + c·Δmarker_cy·experimental_c + d·experimental_c + e.
   - *Variables.* growth_cy is the log ratio of January–September papers in year y to 2022. Δmarker_cy is the marker
     rate in y minus the 2019–2022 mean. experimental_c is 1 for wet-lab or experimental, 0 for computational, theory
     or maths, and 0.5 for mixed.
   - *Estimation.* OLS with standard errors clustered by category. The pooled model has year effects specific to
     each server.
   - *Limits.* The arXiv panel has only 6 or 7 archives, too few clusters for reliable inference, so it is
     descriptive. The panel is an ecological association: categories differ in more than experimental intensity.

4. *Use vs output.* Do markers rise as much in arXiv physics (all six archives, theory, experiment) and maths as in
   bioRxiv, while output diverges?
   - *Markers.* Test 2 for each arXiv group against all of bioRxiv, on the months both corpora cover (March and
     September).
   - *Output.* The event-study model of the within-field contrasts, applied to the arXiv group against bioRxiv new
     preprints (sum of categories), monthly from January 2019 to September 2026. Two quantities: rate ratios relative
     to 2022 (levels), and 2026 relative to 2025, the 2026 acceleration of one group relative to the other. The
     2026-vs-2025 ratio uses the coefficients' covariance.
   - *Limit.* After 2024 marker drift differs by field (bioRxiv's 2024 vocabulary fell further than arXiv's), so
     cross-corpus marker ratios are cleanest in 2024.
5. *Lower bound on the share of LLM-processed abstracts* (Kobak et al. 2025; arXiv only).
   - *Counterfactual.* The share of abstracts with at least one core marker word, extrapolated from a linear trend
     over 2019–2022.
   - *Bound.* With p the observed share and q the counterfactual, a fraction f of LLM-processed abstracts gives
     p = (1 − f)q + fr with r ≤ 1, so f ≥ (p − q)/(1 − q).
   - *Why arXiv only.* bioRxiv and medRxiv were aggregated by word, not by abstract, so their share with any marker
     is not available.

## Analyses tried and dropped

- **Share of the change contributed by heavy producers defined in the later period.** Our first version credited the
  Q3 2025 → Q3 2026 change to authors with five or more papers in Q3 2026. It was dropped because defining the class on
  the later period selects on the outcome and biases the share upward (regression to the mean). It was replaced by the
  combined-output classes above. The old figure is kept in the JSON output (`contribution_Q3_2025_to_Q3_2026`) for
  reference only.
- **Bootstrap of papers for the per-paper heavy-producer share.** Dropped because resampling papers duplicates them,
  which inflates authors' paper counts and biases the share upward (for example 6% observed against a 15–22%
  bootstrap interval).
- **Trend-adjusted C2 as a headline estimate.** Dropped because its 2019–2022 pre-trend mixes late adoption of
  bioRxiv by wet-lab fields with the COVID-19 surge, and extrapolating it is not credible. It is reported only as a
  sensitivity analysis.
- **Field-level trend models for medRxiv and the social sciences.** Kept but flagged: their 2019–2022 trends reflect
  adoption of new servers, so departures from them are not interpretable as changes in output.
