<!--
DRAFT v2.
PLOS ONE Research Article. 16 Oct 2026. Revised from v1 (paper/plos_one/draft_v1.md) by an AI agent (Claude,
Anthropic, via Claude Code) after the round-1 reviews R1–R4 (paper/plos_one/reviews/round1/), the companion analysis's
formal results (paper/plos_one/stats/, companion commit 7ac5647) and the author's decisions of 16 Oct 2026
(paper/brief.md; pre-registration activated in commit 763aa2b). Point-by-point response:
paper/plos_one/reviews/round1/response_round1.md. Not yet revised by the author.
WORD COUNTS (computed by build_v2.py; HTML comments, headings, figure legends and tables excluded).
'Prose' also removes the editorial markers ([AUTHOR: ...], [ANALYSIS PENDING: ...], [RECHECK: ...]) and numbered citations; 'raw' keeps them.

| Section | Prose | Raw |
|---|---|---|
| Introduction | 885 | 955 |
| Materials and methods | 2,742 | 3,008 |
| Results | 0 | 0 |
| Discussion | 0 | 0 |
| Conclusions | 0 | 0 |
| **Main text (Introduction to Conclusions)** | **3,627** | **3,963** |

Abstract: 288 words of prose (288 raw); PLOS ONE limit 300.
Figure legends in the main text: 0 words. Tables in the main text: 0 words.
References: 50 in the main list; SI lists: .
Markers: [AUTHOR] 22, [ANALYSIS PENDING] 9, [RECHECK] 2.
-->

<!--
HOW TO READ THIS FILE
- Built from build/draft_v2_keyed.md by build/build_v2.py (references numbered by first citation; S1 Table, S2 Appendix
  and S4 Table have their own reference lists). Edit the keyed file, not this one.
- Markers: [AUTHOR: ...] only the author can supply or decide this; [ANALYSIS PENDING: ...] an analysis requested in
  round 1 or registered, not yet run; [RECHECK: ...] a claim or reference to check against its source. All must be
  resolved before submission.
- Reframing agreed by all four reviewers and applied here: H1–H3 kept as pre-specified and dated; the pre-specified
  within-field tests reported as not supporting H1; the field-level divergence treated as exploratory, with candidate
  explanations and pending checks; H3 based on the companion's marker analysis; the discussion of evaluation reduced
  to what the findings support.
- Figures: Fig1–Fig4 are the companion's PLOS-format files (paper/plos_one/figures/). The files of commit 7ac5647 still
  show a model-release marker; on 16 Oct the author decided to remove it, and the companion is re-exporting the
  figures. The legends describe the re-exported figures (ChatGPT and the arXiv rules only). Before submission the
  figure fonts must also be changed to Arial (the files use Liberation Sans; R4 minor 24).
- The statements entered in the PLOS submission form (funding, competing interests, data availability, author
  contributions) follow the Supporting Information captions, outside the manuscript proper.
- To re-check before submission (R4 Major 12; carried over from v1's S1 Appendix, which no longer lists them): every
  quotation; the figures taken from McKiernan et al., Rice et al., Hanson et al., Lin and Zhu, Kobak et al.
  (computational fields), Liang et al., Holzwarth et al. and He and Bu; Moed; Cotton et al. References added in v2
  (refs_v2.py) have metadata read from Crossref or arXiv on 16 Oct 2026; the author should confirm that each supports
  the sentence that cites it. Sever et al.: author order as registered in Crossref.
- Nee et al.: the arXiv record (read 16 Oct 2026) lists the authors as "Xiaoshn Nee", "Haobo Zhong" and "Xiaomin Ni";
  the submitter is "Xiao-Sheng Ni". The given name may be misspelt on arXiv; the citation follows the record (Nee X).
-->

# Preprint output in the generative-AI era: pre-specified within-field tests find no robust evidence of an experimental bottleneck

<!--
TITLE: working title for v2. All four reviewers asked for a new title: v1's ("Generative AI is eroding publication
counts as a measure of scientific work: evidence from 1.9 million preprints") fails criterion 4 (a causal verb, an
unmeasured construct, "publication counts" for preprints, and a finding the pre-specified tests did not support), and
its 1.9 million is not the sample of any test and counts aliased papers twice. The author decides.
Short title (at most 100 characters): Preprint output in the generative-AI era
Alternatives proposed by the reviewers:
- R4 (its recommendation): "Preprint growth in the generative-AI era: an arXiv-wide acceleration and no robust
  difference between experimental and non-experimental work within fields"
- R4: "No robust difference between experimental and non-experimental preprint growth within fields after generative
  AI, 2015–2026"
- R4: "Preprint output after generative AI: acceleration across arXiv in 2026, not concentrated in theoretical or
  computational work"
- R1: "Preprint output in 2025–2026: a broad acceleration on arXiv, and no consistent difference between experimental
  and non-experimental work within fields"
- R1: "Where preprint output accelerated in 2025–2026: pre-specified tests on arXiv, bioRxiv and medRxiv"
- R1 (a question, which the author prefers to avoid): "Did preprint output accelerate where experiments are not the
  bottleneck? Pre-specified tests on arXiv, bioRxiv and medRxiv"
- R2: "Where has preprint output accelerated since generative AI? Pre-specified within-field tests across arXiv,
  bioRxiv and medRxiv"
- R2: "An arXiv-wide acceleration, not an experimental bottleneck: preprint output across servers, 2016–2026"
- R3: retitle around where acceleration is and is not seen in 2026, and avoid "eroding".
Caution for titles that name the arXiv acceleration (coordinator, 16 Oct): it holds against each series' own 2015–2022
trend, but since 2022 bioRxiv has grown more in level than the physics archives tested; name the counterfactual.
-->

[AUTHOR: full name]<sup>1,2,*</sup>

<sup>1</sup> European Molecular Biology Laboratory (EMBL), [AUTHOR: unit, site, city, country]
<sup>2</sup> Universitat Pompeu Fabra (UPF), Barcelona, Spain

\* Corresponding author: [AUTHOR: email; ORCID iD]. <!-- EMBL must be the corresponding affiliation for the EMBL–PLOS flat-fee agreement; confirm with the EMBL library. -->

## Abstract

Research evaluation relies on counts of outputs, and generative artificial intelligence (AI) lowers the cost of writing them. If it lowered the cost of papers mainly where no new experiments are needed, preprint output should have grown faster in theoretical, computational and secondary-data work than in experimental work within the same field. I tested this prediction with three contrasts fixed before any model was estimated, using monthly counts of new preprints on arXiv (2015–2026), bioRxiv and medRxiv (2019–2026). Relative to 2022, the January–September 2026 rate ratios were 1.14 (95% CI 1.00–1.30; Holm-adjusted p = 0.11) for theoretical against experimental physics, 1.08 (1.03–1.14; p = 0.01) for computational against wet-lab biology, and 0.99 (0.88–1.10; p = 0.82) for medRxiv preprints naming widely reused public datasets against the rest. The physics test could detect only ratios above 1.21, and 61% of pairs of arXiv archives diverged as much; the biology ratio fell to 0.87 against 2019 and to 0.93 without bioinformatics. The pre-specified tests therefore did not support the prediction. AI-associated style words in abstracts rose two- to threefold in every group by 2024, experimental groups included, and did not predict output growth across categories. In exploratory analyses, arXiv physics and mathematics stood 32% and 48% above their 2015–2022 trends in 2026, and 14 of 18 arXiv archives, experimental particle physics included, stood at least 25% above theirs; bioRxiv (0.91 of trend) and PubMed (0.93) did not, although bioRxiv has grown more in absolute terms since 2022. In theoretical physics, output grew in every class of authors, fastest among the most productive. These data cannot attribute the changes to AI. They show AI-assisted writing in every field studied while counts moved unevenly across servers, which limits comparisons of counts across fields and years.

<!-- Abstract: PLOS ONE limit 300 words; see the word count in the header. -->

## Introduction

Decisions on hiring, promotion and funding rely heavily on counts of research outputs [1]. Counts are crude proxies for originality and rigour, but they carried some information because the outputs they count were costly to produce [2,3]. Generative artificial intelligence (AI) lowers the cost of producing the written part of research, whether it is used well or badly, and in preprints the use of large language models (LLMs) has reversed the association between writing complexity and paper quality [4]. Whether AI has also changed how many outputs are produced, and where, is an empirical question that bears on how counts can be read. A companion essay argues that evaluation built on costly outputs is not prepared for widespread, legitimate use of AI [5]; this article tests one empirical premise of that argument.

Output was growing before generative AI [6]: indexed articles were about 47% more numerous in 2022 than in 2016 [7]. Since then, an editorial in *Organization Science* has reported a 42% rise in submissions since the release of ChatGPT [8], the US National Institutes of Health (NIH) has reported that AI tools enabled some applicants to submit more than 40 applications in one round [9], and arXiv received 40,363 submissions of all kinds in September 2026, against 20,569 in September 2024 [10]. Several funders, preprint servers and conferences have responded by limiting how many items each person may submit (S1 Table).

Several studies have measured how output changed. Qi et al. analysed 2.1 million preprints posted on arXiv, bioRxiv, medRxiv and SocArXiv from 2016 to 2025 with interrupted time series and report that computationally intensive fields benefited more than others [11]. Nee et al. fitted a synthetic control to monthly counts for 20 arXiv archives up to August 2026 and estimated that mathematics recorded 11.9% more list entries in January–August 2026 than its counterfactual, a change they describe as a regime shift; in a pseudonymised author panel, the share of author units with at least five submissions rose from 2.45% to 3.80% [12]. For individual authors, LLM adoption has been associated with higher output on arXiv, bioRxiv and SSRN [4] and in the social and behavioural sciences [13], although the event-study design behind the first estimate has been argued to produce spurious post-adoption dynamics [14]. [AUTHOR: the brief of 16 Oct dropped Kusumegi et al.'s output-gain estimate from the essay; R2 asks for it here together with Renault et al.'s comment. Confirm or delete this sentence.] The studies of Qi et al., Nee et al. and Filimonovic et al. are preprints.

Other studies estimate how much scientific text is written with LLMs, from word frequencies and classifiers that measure style rather than purpose: at least 13.5% of 2024 PubMed abstracts were processed with LLMs, more in computational fields [15], and estimates by field and corpus vary with the measure [16–19] (S4 Table). Reading preprint counts as research output also requires attention to the servers. Fields adopted preprints at different times and to different degrees [20–22], medRxiv opened only in 2019 [23], COVID-19 brought a surge of preprints in 2020 [24], and servers screen submissions and differ in the genres they accept [25–27]. Output per author depends on how names are matched [28,29], and extreme individual output has been studied with thresholds of more than 60 papers a year [30,31].

These studies leave two questions open. First, the finding that computationally intensive fields benefited more [11] rests on comparisons between servers and fields, which differ in preprint culture, platform rules and author populations as well as in the cost of research. Within a field, experimental and non-experimental work share most of these conditions, so contrasting them is a sharper, falsifiable test of the idea that output grows where the work beyond writing is cheap and not where experiments bind, which Blekhman has argued for biology [2]. Second, aggregate counts do not show whether growth comes from many authors or a few; Nee et al.'s panel addresses this for mathematics [12], with fixed thresholds that are crossed mechanically when everyone produces more.

This article therefore reports three within-field contrasts, fixed before any model was estimated, as a falsification test of the account in which computational intensity governs where output grows; replicates Nee et al.'s synthetic control for mathematics on a different count unit and extends the author-level analysis to theoretical physics with a decomposition free of regression to the mean; and measures a marker of AI-assisted writing in the same groups whose output it compares. The hypotheses were recorded in the analysis skeleton committed on 16 October 2026 at 16:42 UTC (commit 2cac071), after descriptive counts had been seen and before any model was estimated. They are reproduced as recorded:

- **H1.** AI-era acceleration of output is concentrated where the work beyond writing is also cheap: theory, computation, existing data. In experimental work, AI shows in the writing but much less, or not yet, in output.
- **H2.** Where output accelerates, the shift is broad. It comes from many established researchers producing more, not from a few outliers.
- **H3.** AI-assisted writing is widespread across fields, including experimental ones, so differences in output are not explained by differences in adoption.

H1 originated with me, from my view as a physicist and biologist that experimental biology was less affected than other fields; its wording, and H2 and H3, were drafted with AI assistance and adopted by me [AUTHOR: confirm the origin of H2 and H3, and the description of your field]. The first clause of H1 was tested with three pre-specified within-field contrasts, its second clause and H3 with a marker of AI-assisted writing, and H2 with author-level measures. The design is observational: the release dates of AI tools and of platform rules mark when things happened, not why.

## Materials and methods

### Study design and pre-specification

This observational study analyses monthly counts of new preprints (first versions) in four parts: three within-field contrasts between experimental and non-experimental work (H1), the distribution of output among authors (H2), a marker of AI-assisted writing (H3), and exploratory comparisons of fields and servers with their own pre-2023 trends. The groups were defined before their growth was computed, but the hypotheses and the choice of the three contrasts as primary tests were recorded when each group's descriptive growth was already known (commit 2cac071). The analysis plan was written in v1 of this manuscript (commit 697fb25, 17:27 UTC), and the models were run in a separate session, the companion analysis (commits 37b4b11, f5ab16e and 7ac5647) [AUTHOR: state when the companion fixed its model specification relative to commit 697fb25]. "Pre-specified" and "primary" therefore mean fixed before any model was estimated, not before the data were seen: they protect against choosing models after seeing estimates, not against choosing contrasts. All other analyses are exploratory, and none is used on its own to support a conclusion.

### Data sources

*arXiv.* Monthly counts of new submissions by primary archive, excluding replacements and cross-lists, were read from arXiv's statistics pages for January 2010 to September 2026 [32]; models use 2015 onwards. Physics sums 13 archives, mathematics is math and computer science is cs (S2 Appendix). Six pairs of categories are aliases, so archive sums exceed arXiv's total by about 5%, and unlike Nee et al.'s list entries [12] these counts exclude cross-lists. Titles, abstracts, author lists, comments and categories were harvested through arXiv's OAI-PMH interface on 15 October 2026 (mathematics records modified since January 2025) and 16 October 2026 (papers submitted since January 2019 in mathematics and the six physics archives of the contrast). Papers are dated by the month in their identifier, which arXiv assigns at announcement, not submission [33]; annual hep-th and hep-ph counts from the harvest match arXiv's statistics exactly for 2019–2025.

*bioRxiv and medRxiv.* Monthly counts of version-1 preprints in 25 bioRxiv subject categories, January 2019 to September 2026, came from the bioRxiv API [34]; from July 2019 they sum to bioRxiv's official totals. They carry no topic flag and so include COVID-19 preprints. For the marker analysis, the titles and abstracts of all bioRxiv version-1 preprints posted in March and September of each year were retrieved. Every medRxiv version-1 preprint from June 2019 to September 2026 was read through the same API, and preprints that mention COVID-19 in the title or abstract (S2 Appendix) are excluded from every medRxiv series.

*Other series.* PubMed counts are quarterly journal-article records by entry date [RECHECK: query and retrieval date, from the companion scripts]. A social-science series (first versions on PsyArXiv, SocArXiv and EdArXiv through the Open Science Framework (OSF) API, plus arXiv's econ and q-fin archives) changed its counting method in 2025 and is subject to SocArXiv's per-author limit [35]; it is shown for reference only.

*Terms of use and request rates.* arXiv's API terms, which cover OAI-PMH, allow one request every three seconds over a single connection [36], and its robots.txt sets a crawl delay of 15 seconds [37]. The harvests for this study paused 2 s between OAI-PMH requests and 1 s between statistics pages, faster than these limits; the scripts are being set to the published limits for any re-harvest [AUTHOR: confirm before submission]. The bioRxiv and medRxiv API publishes no limit. arXiv metadata are released under CC0, and this work is not endorsed by arXiv; bioRxiv and medRxiv abstracts carry their own licences and are not redistributed; OSF and PubMed data were used under their terms [38] [AUTHOR: confirm the NCBI terms]. All data were retrieved on 15–16 October 2026.

### Groups for the within-field contrasts (H1)

The groups were proposed while the companion essay was being drafted and fixed before their growth was computed (S2 Appendix). In physics (C1), theory comprises hep-th, hep-ph, gr-qc and nucl-th, and experiment comprises hep-ex and nucl-ex; astro-ph, cond-mat, quant-ph and the lattice archive hep-lat are in neither group [AUTHOR: state why hep-lat was left out]. The labels are approximate: hep-ph includes phenomenology fitted to experimental data, gr-qc includes gravitational-wave data analysis, and arXiv's taxonomy places instrumentation and analysis methods outside hep-ex and nucl-ex [39]. In biology (C2), the bioRxiv categories bioinformatics, systems biology and genomics are contrasted with 12 wet-lab categories; the other ten form a mixed group that is shown but not tested. Genomics includes bench sequencing, and bioinformatics includes research in which AI is the topic rather than a tool. In medicine (C3), medRxiv preprints naming a widely reused public dataset or design in the title or abstract (NHANES, UK Biobank, Global Burden of Disease, Mendelian randomisation, FAERS, MIMIC-III or MIMIC-IV, SEER or BRFSS), which recur in formulaic, rapidly scaled analyses [40,41], are contrasted with all other medRxiv preprints, both without COVID-19 preprints. The list shares five of the nine heavily mined datasets identified by Spick et al. [41] (S2 Appendix) [AUTHOR: state when the list was fixed], and the comparison group consists largely of secondary-data research, not experiments.

### Author-level measures (H2)

Authors are matched by normalised name strings, because arXiv metadata carry no author identifiers; such strings merge different people and split the same person [28,29]. Every measure is also computed in a namesake-robust variant (full first names only, with the 1% most frequent surnames removed), which describes a different population rather than the same one with fewer collisions, and in physics papers with more than 50 authors are excluded (S2 Appendix). A heavy producer is an author name with five or more papers in a group in a calendar quarter, about 20 a year, far below the thresholds used for extreme output [30,31]. Because fixed thresholds are crossed mechanically when everyone produces more, the main H2 measures are the shares of fractional output (each paper divided equally among its authors) produced by the top 1% and top 10% of active authors, which do not move under proportional growth, and a decomposition of the change in fractional output between the third quarters of consecutive years by author class (top 1%, next 9% and bottom 90%). Classes are defined on combined output in both years, which avoids regression to the mean; under proportional growth every class grows at the total rate, and pairs of years that end before ChatGPT's release show how much the classes differ by chance. Departures of quarterly measures from their 2019–2022 trends were estimated by ordinary least squares with quarter effects and Newey–West errors [42]. The data are a population, not a sample, so shares carry no sampling intervals. For mathematics, these measures are pending [ANALYSIS PENDING: maths H2].

### Marker of AI-assisted writing (H3)

Following Kobak et al. [15], AI-assisted writing was measured by the frequency of style words whose use rose with LLMs. Their 407 style words, derived from PubMed abstracts, were filtered on baseline data only to the 261 that appeared in fewer than 0.5% of the 41,270 bioRxiv and medRxiv abstracts of 2019–2022 (S2 Appendix). The list was applied to titles and abstracts of bioRxiv preprints posted in March and September, all medRxiv preprints and all arXiv papers in mathematics and the six physics archives, without COVID-19 preprints; the metric is the number of distinct core words per 100 abstracts, relative to the group's 2019–2022 mean. The words drift: built from 2024 text, they peaked in 2024, and by 2026 some were rarer than before 2023 while abstract length had not changed. The rates are therefore lower bounds on LLM-assisted writing, weak ones from 2025, and comparisons between groups are cleanest in 2024. Differences in the rise between two groups were estimated by ordinary least squares on the monthly log ratio of their rates relative to 2019–2022, with t intervals; autocorrelation-robust errors had been about 2.5 times too narrow against the month-to-month variation of 2019–2022. For arXiv, a lower bound on the share of LLM-processed abstracts was computed as in Kobak et al. A panel of 27 bioRxiv categories and arXiv archives regressed output growth in 2023–2026 on the change in marker rate, an indicator of experimental work and their interaction, with server-specific year effects and errors clustered by category; H1 predicted a negative interaction. The panel is ecological, and its arXiv part (six clusters) is descriptive. Markers for mathematics are pending [ANALYSIS PENDING: maths H3 markers].

### Statistical analysis

*Within-field contrasts.* For each contrast, the monthly counts of the non-experimental group A and the experimental group B were stacked and fitted by Poisson pseudo-maximum likelihood [43]: log E[*y*<sub>*gt*</sub>] = *λ*<sub>*t*</sub> + *μ*<sub>*g*,*m*(*t*)</sub> + Σ<sub>*k*≠2022</sub> *β*<sub>*k*</sub>·1[*g* = A]·1[year(*t*) = *k*]. Month fixed effects *λ*<sub>*t*</sub> absorb every shock common to both groups, including platform-wide changes in rules and moderation, and *μ*<sub>*g*,*m*</sub> are group-specific calendar-month effects. exp(*β*<sub>2026</sub>), the rate ratio of A to B in January–September 2026 relative to 2022, is the pre-specified estimate; values above 1 mean that the non-experimental group grew faster. Standard errors are Driscoll–Kraay with 12 lags [44]. Because the model has a coefficient for every year, these intervals measure within-year uncertainty only; they omit year-to-year shocks to the ratio and the heterogeneity between archives or categories within each group [45]. The three 2026 p values are Holm-adjusted [46] and reported with Bonferroni-adjusted (98.3%) intervals. Minimum detectable rate ratios at 80% power are exp(2.80 × SE) at α = 0.05 and exp(3.24 × SE) at α/3, the level of Holm's first step.

*In-space placebos.* Because the model intervals omit heterogeneity between units, in-space placebos are the main benchmark, as in inference with few treated units [47]. The same estimate was computed for all 153 pairs of the 18 arXiv archives with complete data since 2015 (the benchmark for C1) and for all 462 splits of the 12 wet-lab categories into two halves (C2). I report the share of placebos whose absolute log rate ratio is at least as large as the contrast's; this asks whether the split between experimental and non-experimental work predicts divergence in 2026 better than arbitrary splits [ANALYSIS PENDING: structure-matched placebos (all 455 assignments of 3 of the 15 bioRxiv categories as computational; all 4-against-2 draws of physics archives) and in-time placebos with the identical estimator]. No placebo distribution was defined for C3.

*Negative controls, leave-one-out estimates and sensitivity analyses.* H1 predicts no divergence between hep-ex and nucl-ex or between theory archives; a divergence as large as the main contrast points to heterogeneity among archives rather than to the cost of experiments. Each contrast was re-estimated without each of its archives or categories in turn; I treat an estimate as robust only if no single exclusion moves it across 1, a criterion stated after the estimates were seen. Sensitivity analyses used 2019 as the reference year, removed hep-ph from theory, removed genomics or moved it to wet lab, dropped November 2025 to February 2026 (after arXiv's rule changes) and ended the sample in October 2025. A variant with group-specific linear trends instead of pre-2023 year effects is reported only as a sensitivity analysis, because extrapolating 2019–2022 trends shaped by COVID-19 and by the adoption of bioRxiv is not credible.

*Departures from trend (exploratory).* Each field and arXiv archive was fitted by Poisson pseudo-maximum likelihood with a linear trend, calendar-month effects, an indicator for April 2020 to March 2021 and indicators for 2023–2026, with Newey–West errors [42]. The exponentiated year coefficients are ratios of observed to trend-expected counts, with trends identified from pre-2023 months (from 2015 for arXiv and 2018 for bioRxiv); the medRxiv and social-science trends reflect the adoption of new servers and are not interpreted. Mathematics' 2026 departure was ranked among those of the 18 archives. The 2026 acceleration of an arXiv group relative to bioRxiv is the ratio of its 2026 and 2025 coefficients in the event-study model above, fitted to the arXiv group and bioRxiv from 2019.

*Synthetic control (exploratory).* Following Nee et al. [12] and Abadie et al. [48], mathematics' deseasonalised monthly log series was approximated by a convex combination of 19 other archives (14 received positive weight), fitted on January 2018 to December 2025. Each donor in turn served as a placebo; with 20 units, the smallest attainable rank p value is 0.05. The donors also departed from trend in 2026, so the gap measures mathematics' excess over arXiv, not an effect of AI [ANALYSIS PENDING: synthetic control with the OAI mathematics series, physics-only donors and math-ph excluded].

*Break tests.* Sup-Wald tests for one break at an unknown date [49], computed over the central 70% of each series, cannot place a break after about December 2024 on arXiv or August 2025 on bioRxiv and medRxiv, so they are not used to date the acceleration (S5 Table).

### Deviations from the analysis plan

The plan in v1 specified period effects against multi-year baselines (2017–2022 for arXiv, 2019–2022 for bioRxiv and mid-2019 to 2022 for medRxiv), Poisson or negative binomial models with Newey–West errors, Bonferroni-adjusted intervals, Benjamini–Hochberg adjustment of negative controls and Bai–Perron break tests. The analysis as run used year-by-group effects with 2022 as the reference, which turned the plan's pre-trend diagnostic into the primary estimate; month fixed effects; Poisson pseudo-maximum likelihood with Driscoll–Kraay errors; Holm adjustment, reported here with the planned Bonferroni intervals; placebo shares rather than adjusted p values for the negative controls, because adjusting falsification tests makes problems less likely to be flagged; and single-break sup-Wald tests [AUTHOR: reasons for, and timing of, the change of reference year]. The reference year matters, because 2022 was a low year for C1 (pre-period coefficients 1.25 in 2020 and 1.19 in 2021) and for C2 (1.24 in 2019). Averaging the event-study coefficients over the planned baseline years gives approximate 2026 estimates of 1.05 (C1), 1.02 (C2) and 1.03 (C3), against 1.14, 1.08 and 0.99 relative to 2022; these are not model estimates [ANALYSIS PENDING: planned specification (period effects against the planned baselines, with Bonferroni-adjusted intervals)]. The plan gave a decision rule for each contrast (support only if the adjusted interval excludes 1) but none for H1 as a whole; I add, after the fact, that H1 as a general claim needs support in all three fields.

### Pre-registered paper-level test

After these results were known, I formed a refined hypothesis: within arXiv archives, papers that report no new empirical data grew faster in 2025–2026, relative to their pre-2023 trend, than papers that do. The hypothesis is mine; it was prompted by an exploratory observation in experimental particle physics (Results). Its test was drafted with AI assistance, approved by me and timestamped in the project repository (commit 763aa2b, 16 October 2026, 18:28 UTC) before any paper in the test archives was classified (S1 Text) [AUTHOR: OSF Registries DOI, if registered]. The confirmatory test uses arXiv cond-mat, astro-ph and quant-ph, which were not used to form the hypothesis, with papers dated by first submission from 2017. An LLM with a fixed prompt and codebook will classify each paper from its title, abstract and comments, without date or archive, as reporting new empirical data, not reporting it (theory, simulation, methods, reviews, reanalysis of existing data or prospect studies) or unclear. It will be used only if its agreement with my blind coding of 200 stratified abstracts reaches Cohen's κ ≥ 0.60. The estimand is the ratio of the two classes' departures from their 2017–2022 trends over January 2025 to September 2026, pooled over the three archives, with a decision rule fixed in advance (S1 Text). A second, exploratory component, which I proposed, classifies papers in hep-ex, hep-ph, hep-th, hep-lat, nucl-ex and nucl-th by rule from the curated metadata of INSPIRE-HEP [50] (document type, subject category, linked experiments, collaborations and author counts), without AI. Neither component has been run [ANALYSIS PENDING: pre-registered test] [ANALYSIS PENDING: INSPIRE].

### Software and data processing

Data were harvested and analysed with Python scripts in the companion analysis (commit 7ac5647), which write only aggregate counts and derived variables [ANALYSIS PENDING: software versions and a pinned environment]. Data and code are described under Data availability.

### Ethics statement

This study analysed publicly available bibliographic metadata and aggregate counts; no human participants were recruited. Author name strings from arXiv metadata, which are personal data, were processed only to count papers per name within periods. Released author-level data are pseudonymised with a salted hash and keep only the variables that the namesake-robust variants need [AUTHOR: confirm that the pseudonymisation is implemented before release]; no name is reported, and table cells describing fewer than ten names are merged or suppressed. The main risk to individuals is re-identification of heavy producers by re-running the code on public metadata, with reputational harm if high output were read as misuse of AI; it is mitigated by reporting aggregates only and by not interpreting any individual's output. [AUTHOR: data-protection office consultation, UPF/EMBL: name the office, the date and the outcome, and the lawful basis and safeguards recorded.] Data were retrieved under each source's terms of use (Data sources).

### Use of AI tools

I used Claude (Anthropic), via Claude Code [AUTHOR: model and version], between 15 October and [AUTHOR: date] 2026, on a [AUTHOR: account type] account [AUTHOR: state whether model training on your data was switched off]. AI agents (i) searched the literature and checked references; (ii) drafted the text of every section from my decisions and outlines, and revised it after review; (iii) wrote all code for harvesting, processing, statistical analysis and figures, in a separate session (the companion analysis); (iv) produced all figures with that code; and (v) wrote internal critical reviews of the drafts in four reviewer roles, which are not peer review. H1 originated with me, as did the refined hypothesis of the pre-registered test and its INSPIRE-HEP component. The analysis plan, the group definitions, the statistical specification and the candidate recommendations in the Discussion were proposed by AI agents and adopted or modified by me [AUTHOR: confirm and describe your own validation, e.g. code review and re-runs: the code you reviewed line by line (groups, flags, author matching, models); re-runs in a clean environment (commit hash) with identical outputs; key numbers recomputed from the source APIs; sources read in full; any AI proposal you rejected]. The interpretations and conclusions are mine. Checks made by AI agents are listed in S1 Appendix and are not counted as validation. The classifier of the pre-registered test is itself an LLM, to be validated against my blind coding. No AI tool is an author, and I take responsibility for the content.

## Results

<!-- RESULTS TO BE WRITTEN -->

## Discussion

<!-- DISCUSSION TO BE WRITTEN -->

## Conclusions

<!-- CONCLUSIONS TO BE WRITTEN -->

## Acknowledgments

[AUTHOR: acknowledgements, e.g. anyone who read the draft or checked the code.]

## References

1. Moher D, Naudet F, Cristea IA, Miedema F, Ioannidis JPA, Goodman SN. Assessing scientists for hiring, promotion, and tenure. PLoS Biol. 2018;16(3):e2004089. doi:10.1371/journal.pbio.2004089
2. Blekhman R. What is biology research for? PLoS Biol. 2026;24(10):e3004075. doi:10.1371/journal.pbio.3004075
3. Hansen T. Symbolic scarcity and epistemic waste: a systems theory of academic publishing failure. Res Integr Peer Rev. 2026;11:7. doi:10.1186/s41073-026-00193-3
4. Kusumegi K, Yang X, Ginsparg P, de Vaan M, Stuart T, Yin Y. Scientific production in the era of large language models. Science. 2025;390(6779):1240–1243. doi:10.1126/science.adw3000
5. [AUTHOR: surname initials]. The cost was the signal: why academic evaluation is not ready for AI used well [Preprint]. Zenodo. 2026. doi:[to be minted]
6. Bornmann L, Haunschild R, Mutz R. Growth rates of modern science: a latent piecewise growth curve approach to model publication numbers from established and new literature databases. Humanit Soc Sci Commun. 2021;8:224. doi:10.1057/s41599-021-00903-w
7. Hanson MA, Gómez Barreiro P, Crosetto P, Brockington D. The strain on scientific publishing. Quant Sci Stud. 2024;5(4):823–843. doi:10.1162/qss_a_00327
8. Gartenberg C, Hasan S, Murray A, Pierce L. More versus better: artificial intelligence, incentives, and the emerging crisis in peer review. Organ Sci. 2026;37(3):795–812. doi:10.1287/orsc.2026.ed.v37.n3
9. National Institutes of Health. NOT-OD-25-132: Supporting fairness and originality in NIH research applications [Internet]. 17 Jul 2025 [cited 2026 Oct 16]. Available from: https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html
10. Boboris K. Fair moderation, equitable access, and AI: arXiv's updated rate limit policy [Internet]. arXiv blog; 1 Oct 2026 [cited 2026 Oct 16]. Available from: https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/
11. Qi M, Cao Z, Wang Q, Li N, Zhu T. Does GenAI rewrite how we write? An empirical study on two-million preprints [Preprint]. arXiv:2510.17882. 2025 [cited 2026 Oct 16]. Available from: https://arxiv.org/abs/2510.17882
12. Nee X, Zhong H, Ni X. The generative AI gold rush in theoretical and computational research [Preprint]. arXiv:2609.04872v1 [cs.DL]. 2026 [cited 2026 Oct 16]. Available from: https://arxiv.org/abs/2609.04872
13. Filimonovic D, Rutzer C, Wunsch C. Can GenAI improve academic performance? Evidence from the social and behavioral sciences [Preprint]. arXiv:2510.02408. 2025 [cited 2026 Oct 16]. Available from: https://arxiv.org/abs/2510.02408
14. Renault T, Bergeaud A, Bosquet C. Scientific production in the era of large language models: outcome-triggered treatment timing and spurious event-study dynamics. Proc Natl Acad Sci U S A. 2026;123(33):e2618638123. doi:10.1073/pnas.2618638123
15. Kobak D, González-Márquez R, Horvát EÁ, Lause J. Delving into LLM-assisted writing in biomedical publications through excess vocabulary. Sci Adv. 2025;11(27):eadt3813. doi:10.1126/sciadv.adt3813
16. Liang W, Zhang Y, Wu Z, Lepp H, Ji W, Zhao X, et al. Quantifying large language model usage in scientific papers. Nat Hum Behav. 2025;9(12):2599–2609. doi:10.1038/s41562-025-02273-8
17. Lin CW, Zhu W. Divergent LLM adoption and heterogeneous convergence paths in research writing [Preprint]. arXiv:2504.13629. 2025 [cited 2026 Oct 16]. Available from: https://arxiv.org/abs/2504.13629
18. Holzwarth L, González-Márquez R, Kobak D. Most biomedical publications show signs of LLM-assisted writing [Preprint]. arXiv:2608.10715v1. 2026 [cited 2026 Oct 16]. Available from: https://arxiv.org/abs/2608.10715
19. He Y, Bu Y. Academic journals' AI policies fail to curb the surge in AI-assisted academic writing [Preprint]. arXiv:2512.06705v2. 2026 [cited 2026 Oct 16]. Available from: https://arxiv.org/abs/2512.06705
20. Larivière V, Sugimoto CR, Macaluso B, Milojević S, Cronin B, Thelwall M. arXiv e-prints and the journal of record: an analysis of roles and relationships. J Assoc Inf Sci Technol. 2014;65(6):1157–1169. doi:10.1002/asi.23044
21. Abdill RJ, Blekhman R. Tracking the popularity and outcomes of all bioRxiv preprints. eLife. 2019;8:e45133. doi:10.7554/eLife.45133
22. Wang Z, Chen Y, Glänzel W. Preprints as accelerator of scholarly communication: an empirical analysis in mathematics. J Informetr. 2020;14(4):101097. doi:10.1016/j.joi.2020.101097
23. Krumholz HM, Bloom T, Sever R, Rawlinson C, Inglis JR, Ross JS. Submissions and downloads of preprints in the first year of medRxiv. JAMA. 2020;324(18):1903–1905. doi:10.1001/jama.2020.17529
24. Fraser N, Brierley L, Dey G, Polka JK, Pálfy M, Nanni F, et al. The evolving role of preprints in the dissemination of COVID-19 research and their impact on the science communication landscape. PLoS Biol. 2021;19(4):e3000959. doi:10.1371/journal.pbio.3000959
25. Sever R, Hindle S, Roeder T, Fereres S, Fernández Gayol O, Ghosh S, et al. bioRxiv: the preprint server for biology [Preprint]. bioRxiv. 2019. doi:10.1101/833400
26. bioRxiv. Frequently asked questions [Internet]. Cold Spring Harbor Laboratory [cited 2026 Oct 16]. Available from: https://www.biorxiv.org/about/FAQ
27. medRxiv. About medRxiv [Internet] [cited 2026 Oct 16]. Available from: https://www.medrxiv.org/content/about-medrxiv
28. Milojević S. Accuracy of simple, initials-based methods for author name disambiguation. J Informetr. 2013;7(4):767–773. doi:10.1016/j.joi.2013.06.006
29. Kim J, Diesner J. Distortive effects of initial-based name disambiguation on measurements of large-scale coauthorship networks. J Assoc Inf Sci Technol. 2016;67(6):1446–1461. doi:10.1002/asi.23489
30. Ioannidis JPA, Klavans R, Boyack KW. Thousands of scientists publish a paper every five days. Nature. 2018;561(7722):167–169. doi:10.1038/d41586-018-06185-8
31. Ioannidis JPA, Collins TA, Baas J. Evolving patterns of extreme publishing behavior across science. Scientometrics. 2024;129(9):5783–5796. doi:10.1007/s11192-024-05117-w
32. arXiv. Submission statistics by archive and year [Internet] [cited 2026 Oct 16]. Available from: https://arxiv.org/year/<archive>/<year>
33. arXiv. Availability of submissions [Internet] [cited 2026 Oct 16]. Available from: https://info.arxiv.org/help/availability.html
34. bioRxiv, medRxiv. bioRxiv and medRxiv API [Internet] [cited 2026 Oct 16]. Available from: https://api.biorxiv.org/
35. SocArXiv. AI policy [Internet]. Dated 8 Mar 2026, updated 28 Sep 2026 [cited 2026 Oct 16]. Available from: https://socopen.org/ai-policy/
36. arXiv. Terms of use for arXiv APIs [Internet] [cited 2026 Oct 16]. Available from: https://info.arxiv.org/help/api/tou.html
37. arXiv. robots.txt [Internet] [cited 2026 Oct 16]. Available from: https://arxiv.org/robots.txt
38. Center for Open Science. OSF terms of use [Internet] [cited 2026 Oct 16]. Available from: https://osf.io/terms-of-use/
39. arXiv. Category taxonomy [Internet] [cited 2026 Oct 16]. Available from: https://arxiv.org/category_taxonomy
40. Suchak T, Aliu AE, Harrison C, Zwiggelaar R, Geifman N, Spick M. Explosion of formulaic research articles, including inappropriate study designs and false discoveries, based on the NHANES US national health database. PLoS Biol. 2025;23(5):e3003152. doi:10.1371/journal.pbio.3003152
41. Spick M, Onoja A, Harrison C, Stender S, Byrne J, Geifman N. Quantifying new threats to health and biomedical literature integrity from rapidly scaled publications and problematic research. J Clin Epidemiol. 2026;193:112203. doi:10.1016/j.jclinepi.2026.112203
42. Newey WK, West KD. A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. Econometrica. 1987;55(3):703–708. doi:10.2307/1913610
43. Santos Silva JMC, Tenreyro S. The log of gravity. Rev Econ Stat. 2006;88(4):641–658. doi:10.1162/rest.88.4.641
44. Driscoll JC, Kraay AC. Consistent covariance matrix estimation with spatially dependent panel data. Rev Econ Stat. 1998;80(4):549–560. doi:10.1162/003465398557825
45. Bertrand M, Duflo E, Mullainathan S. How much should we trust differences-in-differences estimates? Q J Econ. 2004;119(1):249–275. doi:10.1162/003355304772839588
46. Holm S. A simple sequentially rejective multiple test procedure. Scand J Stat. 1979;6(2):65–70.
47. Conley TG, Taber CR. Inference with "difference in differences" with a small number of policy changes. Rev Econ Stat. 2011;93(1):113–125. doi:10.1162/rest_a_00049
48. Abadie A, Diamond A, Hainmueller J. Synthetic control methods for comparative case studies: estimating the effect of California's tobacco control program. J Am Stat Assoc. 2010;105(490):493–505. doi:10.1198/jasa.2009.ap08746
49. Andrews DWK. Tests for parameter instability and structural change with unknown change point. Econometrica. 1993;61(4):821–856. doi:10.2307/2951764
50. INSPIRE-HEP. REST API documentation [Internet] [cited 2026 Oct 16]. Available from: https://github.com/inspirehep/rest-api-doc

<!-- SI FILES START -->
