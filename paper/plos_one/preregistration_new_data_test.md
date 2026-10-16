# Pre-registration (DRAFT, needs the author's approval): the new-data bottleneck test on held-out arXiv archives

*Drafted 16 Oct 2026 by the coordinating assistant. It is not active until the author approves it. Approval is recorded by a commit that removes "DRAFT" from the title, and optionally by an OSF registration. No paper-type classification of the held-out archives may be done before then.*

## 1. Background and state of knowledge at registration

- **H1 failed at archive level.** H1 was pre-specified in v1: within each field, output accelerates where experiments are not the bottleneck. It was not supported at archive level:
  - C1 is inconclusive and fails the negative controls;
  - C2 is fragile (it depends on bioinformatics and on the base year);
  - C3 is null.
- **An exploratory observation in hep-ex** gave rise to this refined hypothesis (round-1 Reviewer 3, INSPIRE-HEP queries):
  - Records with at most 10 authors and no collaboration grew from 187 to 366 (Jan–Sep 2024 → 2026).
  - Collaboration papers (>300 authors) grew 4%.
  - In a sample of 60 small-team records, classified by one person, only 1 reported new measurements.
- **Data already examined.** Archive-level monthly counts for all 18 arXiv archives, including cond-mat, astro-ph and quant-ph, have been examined. The **classification of papers by type** in those three archives has **not** been examined.

## 2. Hypothesis (HN)

Within arXiv archives, papers that **do not report new empirical data** grew faster in 2025–2026, relative to their pre-2023 trend, than papers that **report new empirical data**.

The hypothesis is stated in the author's terms: what AI can accelerate is work that needs no new data. The confirmatory test uses archives that were not used to form it at paper level.

## 3. Data

- **Primary:** arXiv **cond-mat**, **astro-ph** and **quant-ph**, by primary category, new submissions only. Papers are dated by **v1 submission date**, not by announcement. Period: January 2017 to September 2026.
- **Source:** arXiv API or OAI-PMH metadata (title, abstract, comments, author count), collected within arXiv's rate limits (OAI 1 request per 3 s; the 15 s crawl delay where it applies).
- **Exploratory only:** hep-ex and nucl-ex, the archives that generated the hypothesis. They are reported separately and never pooled with the confirmatory archives.

## 4. Classification

- **ND (new empirical data):** the paper reports new measurements, observations or experiments carried out or obtained by the authors, including new observational data.
- **NN (no new empirical data):**
  - theory;
  - analytic or numerical calculation;
  - simulation;
  - methods, software or instrumentation proposals without new measurements;
  - reviews, perspectives or white papers;
  - reanalysis of existing or public data;
  - prospects or sensitivity studies for future experiments.
- **Unclear:** excluded from the primary analysis. In a sensitivity analysis it is added to NN.
- **Classifier:** a large language model with a fixed prompt and codebook (Appendix A, to be added before activation), run at temperature 0. The model name and version are recorded. Every label is stored with the paper ID.
- **Validation by the author, a human expert:**
  - The author codes a **stratified random sample of 200 abstracts** from the three archives (2019–2026), blind to the model's labels and to dates.
  - Report Cohen's κ, plus precision and recall per class.
  - **Rule:** proceed if κ ≥ 0.60. If κ < 0.60, revise the codebook **once** on a separate development sample from hep-ex, then re-validate on a fresh sample of 200 from the held-out archives.

## 5. Estimand and model

- **Data and model.** Monthly counts by archive *a* and class *c*, fitted with Poisson pseudo-maximum likelihood. The model includes:
  - archive × class fixed effects;
  - archive × class linear trends, fitted on January 2017 to December 2022 with 2020–2021 indicators;
  - month-of-year seasonality.
- **Primary estimand:** the ratio of rate ratios, RRR = exp(β_NN − β_ND). Here β is the departure from trend over January 2025 to September 2026, **pooled over the three archives** with archive-specific estimates also reported.
- **Inference:** 95% CIs from a moving-block bootstrap over months (block length 12).
- **Pre-period placebo:** the same estimand for 2019 should be about 1.
- **Power:** report the minimum detectable RRR at 80% power.

## 6. Decision rule

- **HN supported** if both hold:
  - the pooled RRR > 1 and its 95% CI excludes 1;
  - the archive-specific RRR > 1 in at least 2 of the 3 archives.
- **HN not supported** if the pooled CI includes 1. Report the minimum detectable effect, and do not describe the result as evidence of no effect if the test is underpowered.
- **Contradicted** if the pooled RRR < 1 and its CI excludes 1.

## 7. Sensitivity analyses (all reported; none changes the primary verdict)

1. Papers dated by announcement month instead of submission.
2. Excluding September 2026.
3. "Unclear" papers added to NN.
4. Excluding reviews and white papers from NN.
5. Excluding papers with more than 50 authors.
6. A baseline of 2017–2019 only.

## 8. Deviations

Every deviation from this plan will be listed and explained in the paper.

## 9. AI use

- The classifier is an AI model; its use and the author's validation will be disclosed under PLOS policy.
- This plan was drafted by an AI assistant and approved by the author, who is responsible for it.
