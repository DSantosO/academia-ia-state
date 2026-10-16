# Pre-registration (ACTIVE): the new-data bottleneck test on held-out arXiv archives

*Drafted 16 Oct 2026 by the coordinating assistant. The author approved the analysis in chat on 16 Oct 2026 ("Do the abstract analysis"). This commit activates the plan and timestamps it. The author may also register it on OSF [AUTHOR: optional OSF DOI]. At activation, no paper-type classification of the held-out archives has been done.*

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
- **Classifier:** a large language model with the fixed prompt and codebook in Appendix A, run at temperature 0. The model name and version are recorded. Every label is stored with the paper ID.
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

## 10. Exploratory companion analysis: INSPIRE-HEP (not confirmatory)

The author proposed using INSPIRE-HEP because its metadata are rich. HEP is where the hypothesis came from, so this analysis is **exploratory**. It is reported separately and never pooled with the confirmatory test.

- **Records:** INSPIRE-HEP records with arXiv e-prints in hep-ex, hep-ph, hep-th, hep-lat, nucl-ex and nucl-th, 2017–2026, dated by v1 submission.
- **Fields used:**
  - INSPIRE subject categories (e.g. Experiment-HEP, Phenomenology-HEP, Theory-HEP, Instrumentation, Computing, Experiment-Nucl);
  - document type (article, conference paper, review, thesis, report);
  - linked accelerator experiments;
  - collaborations;
  - author counts.
- **Class rules from curated metadata, with no AI classification:**
  - **ND-INSPIRE:** a research article (not a review, proceedings or thesis) in an experimental category that is linked to an experiment or collaboration and does not match prospect or sensitivity wording.
  - **NN-INSPIRE:** everything else in scope.
  - Report the rule variants as sensitivity checks.
- **Questions:**
  - Do ND-INSPIRE papers depart from their pre-2023 trend in 2025–2026 less than NN-INSPIRE papers, overall and within hep-ex and nucl-ex?
  - Report breakdowns by collaboration size (≤10, 11–300, >300 authors) and by document type.
- **Terms of use:** respect INSPIRE's API rate limits and terms of use.

## Appendix A. Codebook and classifier prompt (fixed at activation)

**Input:** the title, abstract and arXiv comments of one paper. The date and the archive are withheld.

**Prompt (verbatim):**

> Classify this physics or astronomy paper from its title, abstract and comments into exactly one class.
>
> ND — The paper reports NEW empirical data obtained by the authors: new measurements, experiments, or observations (including new telescope, satellite or detector observations), or the experimental characterisation of samples or devices the authors made or measured.
>
> NN — The paper does NOT report new empirical data. This includes theory or analytic results; numerical calculations or simulations (including first-principles/DFT); computational methods, algorithms, machine-learning methods or software; designs, proposals, or prospect/sensitivity studies for future experiments; reviews, perspectives, white papers or lecture notes; and reanalysis of existing, archival or public data without new data collection by the authors.
>
> U — It cannot be determined from the text.
>
> Rules:
> (1) If the paper combines new measurements or observations with theory or simulation, choose ND.
> (2) Analysis of public or archival datasets (e.g., public survey catalogues, public telescope archives, published databases) is NN unless the authors obtained new observations.
> (3) Fabricating and measuring a device or sample is ND; designing or simulating one is NN.
> (4) Answer with only the label: ND, NN or U.

**Validation sheet:**
- 200 papers, stratified by archive (cond-mat, astro-ph, quant-ph) and by period (2019–2022 vs 2023–2026).
- Each entry carries a pseudonymous ID, title, abstract and comments.
- Dates, archives and model labels are withheld.
- The author codes the papers using the same three classes and rules.

## Deviation 1 (recorded 16 Oct 2026, before any growth-by-class analysis)

**What changed.** The author asked to proceed on the assumption that the classifier is adequate, and to complete the human validation the next day ("supón que está bien y mañana lo valido"). The classification and the confirmatory estimates in this plan will therefore be computed **before** the author's blind validation coding, reversing the order in §4 and §5.

**Safeguards:**
1. The classifier (model, version and verbatim prompt in Appendix A/B) is frozen as registered and will not be changed after results are seen.
2. The validation sheet stays blind (no dates, servers or model labels), so the author's coding cannot be steered by the results.
3. **If κ ≥ 0.60 in a domain,** that domain's results stand as confirmatory, with this deviation disclosed.
4. **If κ < 0.60 in a domain,** that domain's confirmatory results are withdrawn and reported as exploratory only. Any codebook revision made after seeing results will be labelled post hoc.
5. The paper will report this deviation in full.

## Deviation 2 (recorded 16 Oct 2026, before any growth-by-class analysis)

**What changed:**
1. **Sampling instead of full classification.** Classifying all papers is not feasible with the available tooling: about 391,000 held-out arXiv papers, 313,000 bioRxiv and 65,000 non-COVID medRxiv papers. Monthly class counts are therefore estimated as the monthly total multiplied by the class share in a stratified random sample.
   - **Held-out arXiv:** 15 papers per archive-month for 2017–2024 and 40 for 2025–2026, about 6,800 papers. The expected minimum detectable effect for the pooled RRR is about 1.15–1.20.
   - **bioRxiv and medRxiv (Test A):** the same per-month design, about 3,700 papers.
   - **Test B:** at least 150 papers per category for 2019–2022, reusing Test A papers that fall in that window. medRxiv categories with fewer than 150 non-COVID papers in 2019–2022 are pooled with their closest category or dropped. The rule is fixed before results.
   - **Inference:** the bootstrap resamples months *and* redraws the classified sample, so sampling error is carried into the CIs.
   - **Fractions and seeds:** fixed in the analysis script before any estimate is computed.
2. **Temperature.** The classifier runs through subagents whose temperature cannot be set, so "temperature 0" cannot be achieved. Each paper is classified once, independently, with the verbatim prompt. Labels are stored and will not be re-drawn.
3. **Classifier identity.** The classifier is a Claude model (Anthropic), frozen for all runs: [AUTHOR: record the model name and version]. Repository policy prevents model identifiers from being written here.
4. **Validation frame.** The validation sheet is published in a public repository, so its bioRxiv and medRxiv draws are restricted to papers under Creative Commons licences. arXiv metadata are CC0. This slightly narrows the sampling frame for validation only.
5. **Blinding.** The key and the model labels for the validation sheet are stored compressed and hash-committed in validation/sealed/. Blinding depends on the author not opening those files before coding.

**Authorisation.** The author's standing instructions of 16 Oct ("as much statistics as we can but with sense"; usage limits removed; "supón que está bien y mañana lo valido") are taken as authorising the full sampled plan, not the cheaper option. The author can revise this choice before results are reported.
