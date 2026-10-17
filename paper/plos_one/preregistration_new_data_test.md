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

## Deviation 3 (recorded 17 Oct 2026, about 08:20 UTC)

*Recorded after the round-2 reviews (statistics; PLOS academic editor) and before any HN, Test A (bioRxiv) or Test B estimate was computed. Times are UTC and can be checked against the repository's commit and push log.*

**What had been seen when this was recorded.**
- **Test A, medRxiv: already computed.** The registered, trend-based estimate was computed at about 00:10 UTC and committed at 00:11:46 UTC (companion commit dacd064). The coordinating session asked for a hold on further estimates at 00:15 UTC. The result is known to the analysis and coordinating sessions. The author has not seen it.
- **Partial class shares, no estimates:**
  - shares in the 900 earliest medRxiv sample papers, June 2019 to about mid-2020, from the test–retest table;
  - per-batch ND counts for six shuffled arXiv batches, which carry no period information;
  - pooled counts of the superseded DOI-keyed validation labels, with no period information.
- **Nothing else.** No HN, Test A (bioRxiv) or Test B estimate, and no arXiv or bioRxiv class share by period, had been computed.

**D3a. Classifier re-runs.**
- Before any estimate, two sets of papers were first classified in date-ordered batches keyed by DOI:
  - the first 18 medRxiv batches (900 sampled papers);
  - the 200 bioRxiv and medRxiv validation papers.
- DOIs encode posting dates, so these runs exposed the information the classifier was meant not to see.
- They were superseded by blind runs (random order, pseudonymous identifiers) at companion commit 8ab4d9d, 23:43 UTC on 16 Oct.
- The first-run labels feed no estimate. They are used only to report agreement between runs.
- This departs from Deviation 2's "Labels are stored and will not be re-drawn". The re-draw removed the date exposure, and was made before any label was analysed.

**D3b. Test A decision rule.**
- Each Test A hypothesis has one unit, its server, so the "at least 2 of 3 archives" condition of §6 cannot apply.
- The rule is:
  - **supported** if the RRR > 1 and its 95% CI excludes 1;
  - **contradicted** if the RRR < 1 and its 95% CI excludes 1;
  - **not supported** otherwise.
- This was fixed in code at 8ab4d9d, before any estimate. The earlier code, at 15df0b1, applied the 2-of-3 clause, which could never return "supported".

**D3c. Test B sidedness.**
- The prediction is directional (a negative slope), so the decision uses the one-sided permutation p-value, as coded before estimation.
- The two-sided p-value is also reported.

**D3d. Test B category set (design change).**
- **Primary (decides the verdict):**
  - the held-out arXiv subcategories with at least 1,200 papers in 2019–2022: astro-ph.CO, EP, GA, HE, IM and SR; cond-mat.dis-nn, mes-hall, mtrl-sci, quant-gas, soft, stat-mech, str-el and supr-con; and quant-ph (15 categories);
  - all bioRxiv categories in the frame;
  - the medRxiv categories after the pooling rule of Deviation 2.
- **Sensitivity only (cannot change the verdict):** the set in the sampling design (companion commit c2f891b). It adds 23 math.* subcategories, hep-ex, hep-ph, hep-th, nucl-ex, nucl-th and gr-qc.
- **Reasons:**
  1. §3 of the plan reserves hep-ex and nucl-ex for exploratory use and says they are never pooled with the confirmatory archives.
  2. The mathematics outcomes (Q3 2025 to Q3 2026 growth) had been computed on 15 Oct, and their ND share is expected to be near zero. Together they would largely fix the arXiv slope in advance.
  3. The classifier is validated only for cond-mat, astro-ph, quant-ph, bioRxiv and medRxiv. The validation sheet contains no mathematics or particle-physics papers.
- **Description.** Test B remains "pre-specified, with outcomes already examined; only the exposure was unmeasured".

**D3e. Level-based companion estimates (added).**
- **Why.** The registered Test A and Test B estimands extrapolate class- or category-specific trends. The article itself treats such trends as not credible on bioRxiv and medRxiv, where the 2019–2022 years are shaped by server adoption and COVID-19.
- **What is added:**
  - **Test A:** a level-based RRR for January 2025 to September 2026 against a pooled 2019 + 2022 base (medRxiv: July–December 2019 + 2022). It has class-specific month-of-year effects and no class-specific trends; 2020–2021, 2023 and 2024 get their own indicators.
  - **Test B:** the same level-based departure for each category.
  - **HN:** a level-based RRR against a pooled 2017–2019 + 2022 base, reported as a seventh sensitivity analysis.
- **Interpretation:**
  - The registered estimate decides the verdict. The level-based estimate is reported beside it.
  - If the two disagree (one CI excludes 1 and the other does not, or the points lie on opposite sides of 1), the result is reported as dependent on the counterfactual.
- **For medRxiv this addition is post hoc,** because the trend-based estimate was already computed (see above). The registered medRxiv estimate and its verdict stand as computed.
- **The 2019 placebo** is reported for every test. For medRxiv the note is that its pre-trend rests mainly on months of server adoption and COVID-19.

**D3f. Validation sampling and frames.**
- **arXiv half of the validation sheet.** It is a simple random sample per stratum from the complete arXivRaw harvests, instead of the planned draw by random submission day. The arXiv API answered "429 Rate exceeded" from the analysis environment.
- **bioRxiv frames.** The bioRxiv categories "epidemiology" and "clinical trials" are left out of the bioRxiv frames. bioRxiv listed them only until medRxiv opened (January–July 2019), so they would put a composition break into the 2019 baseline. This was fixed before the bioRxiv sample was drawn.

**D3g. Batching (correction to Deviation 2).**
- Deviation 2 says each paper is "classified once, independently". In fact each sub-agent run judges a batch of 50 papers in one context, with one domain prompt.
- **Added sensitivity analysis:** the test–retest disagreement rate is propagated into the estimates by randomly relabelling papers at the observed rate in each bootstrap draw.

**D3h. Reporting fixed now (secondary; does not change any verdict).**
- **Agreement:**
  - Cohen's κ with 95% CIs, by domain and by period (2019–2022 and 2023–2026);
  - confusion matrices by domain and period;
  - precision and recall for each class;
  - agreement between the DOI-keyed and blind runs.
- **Misclassification-corrected ratios (exploratory).** Using period-specific sensitivity and specificity from the validation sheet (Rogan WJ, Gladen B. Am J Epidemiol. 1978;107:71–76).
- **Minimum detectable effects** for the observed-label ratio and for the implied true ratio given the validation error rates.
- **Multiplicity.** Holm-adjusted p-values across HN, HN-bio, HN-med and HN-dose, as a secondary statistic. Each hypothesis is still judged by its registered rule.
- **Licence check.** For the bioRxiv and medRxiv samples: the share under Creative Commons licences, and the classifier's ND share for CC and non-CC papers. The validation sheet contains CC papers only.
- **Run records.** Model identifier, time, batch-file hash and tools used. They are kept outside this repository's text, under repository policy, and reported in the article.

**D3i. Sealing the remaining estimates from the author (strengthens Deviation 1).**
- **Sealed estimates.** From this record on, every remaining confirmatory estimate is written to results files committed only as compressed files in validation/sealed/, with their SHA-256 hashes in the commit message and in validation/README.md. This covers HN, Test A (bioRxiv), Test B, the level-based companions, sensitivities, placebos and minimum detectable effects.
- **What may be shared.** Commit messages and session summaries do not state estimates or verdicts. Neither the author nor the coordinating session is told any estimate until the author's coding is committed (validation/author_labels.csv, with its hash).
- **Unsealing.** After the coding commit, the files are unsealed, κ is computed, and each domain's results are reported with its κ status (Deviation 1, safeguards 3–4).
- **The medRxiv estimate already committed.** The Test A (medRxiv) estimate is already in commit dacd064, whose commit message states the result. The author should not open the analysis branch's commit list or data/processed/stats/nd_tests.json before committing the coding.

**D3j. Changes after this record.**
- This replaces Deviation 2's clause "The author can revise this choice before results are reported".
- Any further change to the design, estimands or decision rules counts as pre-specified only if it is recorded here before the relevant estimate is computed. Otherwise it is labelled post hoc.

**Authorisation.**
- D3a–D3c and D3f–D3g record what was done.
- D3d, D3e and D3h–D3j are design decisions made by the coordinating assistant under the author's standing instructions, following the two reviews, before the estimates they govern.
- The author is told of them in chat on 17 Oct. Under D3j, any change the author makes is pre-specified only if recorded before the relevant estimate is computed.

## Erratum (recorded 17 Oct 2026; the registered text above is left unchanged)

§1 says the 60 small-team hep-ex records were "classified by one person". They were classified by **one AI agent acting as an internal reviewer, not blind to the hypothesis**, as the article's Supporting Information states. No human classified them.

### Deviation 3, addendum (recorded 17 Oct 2026, about 08:45 UTC)

*Recorded after the round-2 experimental-scientist review and before any HN, Test A (bioRxiv) or Test B estimate was computed. The facts in the "What had been seen" list of Deviation 3 still hold.*

**D3k. medRxiv category eligibility for Test B.**
- **The rule applied** is the registered one (Deviation 2): a medRxiv category enters Test B if it has at least 150 non-COVID papers in 2019–2022.
- **Below the threshold.** Of the registered options ("pooled with their closest category or dropped"), the fixed choice is **dropped**, so that no judgment of closeness is needed.
- **The code.** The reviewer reports that the code, as of 15df0b1, applied a higher threshold that dropped 13 more categories. It is corrected to this rule before any Test B estimate.

**D3l. Public astronomy data releases in 2025 (added HN sensitivities).**
- **The issue.** Under the codebook, analysis of public data is NN. The 2025 public releases (DESI DR1, Euclid Q1 and Rubin DP1) can therefore move astro-ph papers on the same data from ND to NN within the test period, for reasons unrelated to AI.
- **Added sensitivity analyses** (reported; the verdict is unchanged):
  - **8.** The pooled RRR without astro-ph (cond-mat and quant-ph only), together with leave-one-archive-out estimates for each archive.
  - **9.** astro-ph without papers whose title or abstract contains "DESI", "Euclid", "Rubin" or "LSST". Matching is case-sensitive, on whole words.

**D3m. AI as a research topic (added sensitivity for HN, Test A and Test B).**
- **The issue.** Papers about machine learning are NN by construction, so growth in AI as a topic could pass for AI-accelerated production.
- **Sensitivity 10.** Exclude papers whose title or abstract matches the following terms, with matching fixed now:
  - **Case-insensitive:** "machine learning", "machine-learning", "deep learning", "neural network", "neural-network", "language model", "artificial intelligence", "reinforcement learning", "generative model", "diffusion model", "foundation model", "graph neural", "transformer-based", "vision transformer".
  - **Case-sensitive whole words:** "AI", "LLM", "LLMs".

**D3n. The 2019 placebo on bioRxiv and medRxiv.**
- 2019 is the first year of both series (medRxiv opened in June 2019), so a 2019 placebo there is not informative. It is reported but not interpreted.
- The registered 2019 placebo for HN (arXiv, from 2017) is unchanged.

**D3o. Implementation completeness.**
- All six registered HN sensitivity analyses (§7), plus sensitivities 7–10 above, are implemented before the HN estimate is computed.
- The Test B estimate is computed only once its code covers both category sets (D3d) and the level-based outcome (D3e).

**Note on the validation runs.**
- The validation sheet's classifier labels and the estimation samples' labels come from separate runs of the same procedure: the same prompts, batch size and blinding.
- Agreement on the sheet therefore measures the procedure. Agreement between runs is reported (D3h).

### Deviation 3, second addendum (recorded 17 Oct 2026, about 09:05 UTC)

*Recorded before any HN, Test A (bioRxiv) or Test B estimate was computed.*

**Correction to "What had been seen".**
- **What happened.** Deviation 3 says the author had not seen the Test A (medRxiv) estimate. In fact, at about 00:12 UTC on 17 Oct the analysis session wrote its point estimate, CI, verdict and minimum detectable effect in a status line in its chat with the author. This was before the hold request. The author may therefore have read it.
- **Consequence.** The author's coding of the 100 medRxiv validation papers may not be blind to that result. [AUTHOR: state whether you read it before coding.]
- **Other results.** No other paper-level result has been reported to the author.

**D3k, completed.**
- The registered rule (at least 150 eligible papers in 2019–2022; below that, dropped) applies to **both** bioRxiv and medRxiv.
- The code's earlier threshold of 300 (`nd_design.py`, c2f891b) is replaced by 150. Under 150, 28 medRxiv categories enter (15 under the old threshold) and 23 are dropped.
- The bioRxiv Test B sample had not been drawn when this was fixed.

**D3p. Test B samples are drawn independently of Test A.**
- Deviation 2 says Test B samples reuse "Test A papers that fall in that window". The code instead draws 150 papers per category independently of Test A. A paper drawn in both samples is classified once and its label shared.
- Each category's sample is still a simple random sample, so the exposure estimate is unbiased; only efficiency differs.
- It is kept because the medRxiv Test B draws had already been classified.

**D3g, detail.**
- The relabelling sensitivity uses the empirical first-run to second-run transition matrices from the test–retest sets.
- There was no arXiv retest. So the 200 arXiv validation papers are classified a second time, blind, to give an arXiv-specific matrix. The bioRxiv and medRxiv matrices come from their own retest sets.

### Deviation 3, third addendum (recorded 17 Oct 2026, about 09:00 UTC)

*Recorded before any HN, Test A (bioRxiv) or Test B estimate was computed.*

**D3q. A coding error in the bootstrap, and the fix.**
- **The error.** A full run of the test script on random synthetic labels, made before any estimate on real labels, found that some moving-block bootstrap replicates contain no month of a base year: bioRxiv without 2019 or 2022, medRxiv without July–December 2019 or 2022. In those replicates the post-period terms are not identified (the unit-by-class effects equal the sum of the period indicators). The model nonetheless returned arbitrary coefficients, which entered the percentile intervals.
- **Extent.** In the synthetic runs, 1–3% of bioRxiv and medRxiv replicates were affected, and none for HN, whose base years are 2017–2019 and 2022. Point estimates are unaffected. Intervals, standard errors and minimum detectable effects can be affected.
- **The fix.** Before each fit, the code checks that every requested term is identified, by testing whether its unit vector lies in the row space of the design. A replicate that fails is discarded. Each result reports the number of retained replicates.
- **Test A (medRxiv), computed at dacd064 with the faulty code.** It is recomputed with the corrected code, sealed, and labelled a correction of dacd064. The point estimate is unchanged by construction.
  - The verdict is taken from the corrected computation, because that is the registered estimator correctly implemented.
  - Both intervals are reported in S6 Table.
- **Applies to all tests.** The same correction applies to every bootstrap in HN, Test A and Test B, and to the level-based companions. It is not specific to the result already computed.
- **Status (17 Oct 2026, 14:42 UTC).** Test A (medRxiv) recomputed with the corrected code and sealed at commit 1b0ec82 on the analysis branch: `validation/sealed/nd_results_A-medrxiv.json.gz`, SHA-256 `e07ec58761bef9d4d94f48a155534fa631b9ca0367bc2c2e5c96dc3d767ee06e`. Only the hash has been reported; the corrected value has not been shown to the author or the coordinator.
