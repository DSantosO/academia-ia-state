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
| Results | 1,663 | 1,727 |
| Discussion | 0 | 0 |
| Conclusions | 0 | 0 |
| **Main text (Introduction to Conclusions)** | **5,290** | **5,690** |

Abstract: 288 words of prose (288 raw); PLOS ONE limit 300.
Figure legends in the main text: 799 words. Tables in the main text: 743 words.
References: 52 in the main list; SI lists: .
Markers: [AUTHOR] 22, [ANALYSIS PENDING] 19, [RECHECK] 2.
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

### Overview of counts

New preprints rose in every field from 2022 to 2026, but not in the same way (Fig 1). From January–September 2022 to the same months of 2026, bioRxiv grew 1.53-fold, more than the six physics archives of the within-field contrast (1.33-fold) and less than mathematics (1.71-fold). Year-on-year growth was steady on bioRxiv (9–13% a year in 2023–2026), whereas the six physics archives grew by 0%, 6% and 6% in 2023–2025 and by 19% in 2026; medRxiv without COVID-19 preprints grew by 27%, 21% and 22% in 2024–2026. In arXiv mathematics, September 2026 alone had 8,360 new papers, against 5,903 in August [ANALYSIS PENDING: re-dating by first-version submission, and January–August versions of every 2026 estimate].

**Fig 1. New preprints by field, indexed to 2022.** Quarterly new preprints (first versions), each series divided by its mean quarterly count in 2022 (2022 = 100), January 2020 to September 2026; the number in each legend entry is the index for July–September 2026. Physics: new submissions to the 13 arXiv physics archives, by primary archive. Mathematics: arXiv math. Computer science: arXiv cs, shown for reference; it includes AI research itself. Biology: bioRxiv. Medicine: medRxiv, excluding preprints that mention COVID-19 or SARS-CoV-2 in the title or abstract. Social sciences: first versions on PsyArXiv, SocArXiv and EdArXiv plus arXiv econ and q-fin, shown for reference only (Methods). Dashed vertical lines mark the release of ChatGPT (30 November 2022), arXiv's rule on review and position papers in computer science (31 October 2025) and arXiv's cap of two submissions per submitter per month (1 October 2026); they are dates for reference, not estimated break points or causes. Indexing to 2022 favours series whose 2022 count was low, such as medicine and biology; departures from each series' own trend are reported in the text. The figure was made with plotting code written by an AI agent (Claude, Anthropic, via Claude Code) under the author's direction (Methods, Use of AI tools).

### Within-field contrasts (H1)

The pre-specified within-field tests did not support H1 (Table 1; Fig 2). Relative to 2022, the January–September 2026 rate ratio of non-experimental to experimental work was 1.14 (95% CI 1.00–1.30; Holm-adjusted p = 0.11) in physics, 1.08 (1.03–1.14; p = 0.01) in biology and 0.99 (0.88–1.10; p = 0.82) in medicine. With the planned Bonferroni-adjusted intervals only the biology contrast excludes 1 (1.02–1.16), so H1 fails the rule that it needs support in all three fields. Measured against the in-space placebos, which capture the heterogeneity between archives and categories that the model intervals omit, none of the contrasts stands out.

**Table 1. Pre-specified within-field contrasts: estimates and checks.**

| | C1 physics: theory / experiment | C2 biology: computational / wet lab | C3 medicine: public dataset / other |
|---|---|---|---|
| New preprints per month, 2026 (A; B) | 1,484; 142 | 698; 1,994 | 100; 1,292 |
| 2026 vs 2022: rate ratio (95% CI) | 1.14 (1.00–1.30) | 1.08 (1.03–1.14) | 0.99 (0.88–1.10) |
| Holm-adjusted p; Bonferroni 98.3% CI | 0.11; 0.97–1.34 | 0.01; 1.02–1.16 | 0.82; 0.86–1.13 |
| Minimum detectable rate ratio, 80% power (α = 0.05; α/3) | 1.21; 1.25 | 1.08; 1.09 | 1.17; 1.20 |
| Event study, 2023; 2024; 2025 | 1.08; 1.11; 1.08 | 0.97; 0.94; 0.98 | 0.99; 0.97; 0.92 |
| Pre-period coefficients beyond 0.9–1.1 | 2020: 1.25; 2021: 1.19 | 2019: 1.24 | 2020: 0.88 |
| 2026 vs 2019 (95% CI) | 1.05 (0.90–1.23) | 0.87 (0.80–0.95) | 0.98 (0.84–1.15) |
| 2026 vs planned baseline (approximate) | 1.05 | 1.02 | 1.03 |
| Trend-adjusted, 2026 (95% CI) | 0.98 (0.72–1.33) | 1.48 (1.06–2.07) | 0.85 (0.60–1.19) |
| Leave-one-out range (component dropped) | 1.03 (nucl-ex) to 1.43 (hep-ex) | 0.93 (bioinformatics) to 1.14 (genomics) | – |
| Negative controls | hep-ex / nucl-ex 1.39 (1.19–1.64); six theory pairs 0.85–1.06 | – | – |
| In-space placebos at least as extreme (percentile of the contrast) | 61% of 153 archive pairs (39th) | 19.7% of 462 wet-lab half-splits (80th) | not defined |
| Reading | Inconclusive | Fragile | Null |

Rate ratio of group A to group B relative to 2022, from Poisson pseudo-maximum-likelihood models with month fixed effects and group-specific calendar-month effects; values above 1 mean that the non-experimental group grew faster. 95% CIs are Driscoll–Kraay intervals, which measure within-year uncertainty only. Bonferroni intervals and detectable effects at α/3 were computed from the reported standard errors. Planned baseline: unweighted mean of the event-study coefficients over 2017–2022 (C1) or 2019–2022 (C2, C3), not a model estimate. Trend-adjusted: departure from the extrapolated pre-2023 relative trend, reported as a sensitivity analysis only. Theory pairs: hep-th / hep-ph 1.02, hep-th / gr-qc 0.87, hep-th / nucl-th 0.91, hep-ph / gr-qc 0.85, hep-ph / nucl-th 0.89, gr-qc / nucl-th 1.06. All estimates are in S5 Table.

**Fig 2. Within-field contrasts.** (A–C) Quarterly new preprints, 2022 = 100, for groups within a field that differ in how much of the work is experimental. (A) arXiv physics, by primary archive: theory (hep-th, hep-ph, gr-qc, nucl-th) and experiment (hep-ex, nucl-ex); the experimental series is small (about 430 papers a quarter in 2026). (B) bioRxiv version-1 preprints: computational (bioinformatics, systems biology, genomics), wet lab (twelve categories; Methods) and all other categories; COVID-19 preprints are included. (C) medRxiv, excluding COVID-19: preprints whose title or abstract names a public dataset or design that recurs in formulaic papers (NHANES, UK Biobank, Global Burden of Disease, Mendelian randomisation, FAERS, MIMIC, SEER, BRFSS) and all other preprints. (D) Rate ratio of group A to group B in each year relative to 2022 (theory / experiment, computational / wet lab, public dataset / other), from a Poisson pseudo-maximum-likelihood model with month fixed effects and group-specific calendar-month effects; bars are 95% Driscoll–Kraay confidence intervals, which omit year-level and between-category variation; logarithmic scale; 2026*, January–September. Dashed vertical lines in A–C as in Fig 1. The figure was made with plotting code written by an AI agent (Claude, Anthropic, via Claude Code) under the author's direction (Methods, Use of AI tools).

The physics contrast is inconclusive rather than null. Its interval touches 1, the test could detect only rate ratios of about 1.21 or more, and the contrast fails its negative controls: the two experimental archives diverged from each other (hep-ex / nucl-ex 1.39) more than theory diverged from experiment, and 61% of all pairs of arXiv archives diverged at least as much. The estimate rests on nucl-ex, a small archive whose January–September count barely changed in a decade (323 papers in 2016, 346 in 2026); without it the ratio is 1.03. The 2020 and 2021 coefficients exceed the 2026 value, and the most closely paired archives, hep-ph and hep-ex, grew alike in 2026 (18% and 14%). The 2026 change in the log ratio of theory to experiment (+0.08) lay within the spread of the 2017–2025 changes (standard deviation 0.10); comparing each group's growth with its own historical range instead would set a stable series against a volatile one [51].

The biology contrast is nominally significant but fragile. It equals its own minimum detectable effect, 19.7% of random splits of the wet-lab categories diverged at least as much, and it rests on bioinformatics, 63% of the computational group in 2026: without bioinformatics the ratio is 0.93, because genomics and systems biology grew more slowly in 2026 (7% and 5%) than the wet-lab categories (8%). The contrast reverses against 2019 (0.87), because the computational categories were already losing ground before ChatGPT, as wet-lab fields adopted bioRxiv and surged with COVID-19 research in 2020. Its 2026 movement is mainly a wet-lab slowdown, from 13% growth in 2025 to 8% in 2026, while computational growth held at 20% and 18%, with bioinformatics accelerating from 22% to 27% [ANALYSIS PENDING: bioinformatics split by AI/ML topic] [ANALYSIS PENDING: bioRxiv categories without COVID-19 preprints].

The medicine contrast is null and excludes increases of more than about 10%. Among preprints without COVID-19, those naming a listed dataset grew 2.47-fold from January–September 2022 to the same months of 2026 and other preprints 2.51-fold, and since 2023 they grew 1.91-fold and 1.88-fold. It is a weak test of H1, however: the flag records a mention, not a design, and the comparison group is itself largely secondary-data research [ANALYSIS PENDING: validation of the regular expressions, a title-only COVID-19 filter and a pre-declared extended dataset list]. The second clause of H1, that AI shows in the writing but much less in the output of experimental work, is examined with the markers below.

### Distribution of output among authors (H2)

In theoretical physics, output grew in every class of authors in 2026, fastest at the top (Fig 3). Ranked on their combined output in the third quarters of 2025 and 2026, the top 1% of authors increased their fractional output by 44%, the next 9% by 37% and the bottom 90% by 21%, against 26% overall, and the bottom 90% contributed 54% of the increase. In earlier pairs of years the bottom 90% had grown by between −0.7% and 8.1%. The namesake-robust variant gave 50%, 33% and 20%. The top 1%'s share of fractional output rose from 5.86% to 6.52%, 0.82 percentage points above its 2019–2022 trend (0.53–1.10; namesake-robust 0.73), while the top 10%'s share stayed at its trend (−0.30; −1.11 to 0.50). Growth in theoretical physics was therefore broad-based but concentrating. Whether the authors behind it were established before 2023 cannot be judged from name strings. Small-team experimental papers were too few for these measures to be informative (top-1% share, 0.13 percentage points above trend; −7.08 to 7.34).

**Fig 3. Concentration of output among authors in theoretical physics.** arXiv hep-th, hep-ph, gr-qc and nucl-th (primary category), papers with at most 50 authors; authors are matched by name strings, because arXiv has no author identifiers. (A) Share of fractional output (each paper divided equally among its authors) produced by the top 1% of active authors in each quarter. (B) Share of papers with at least one author who has five or more papers in the group that quarter, a fixed-threshold measure that rises mechanically with volume. Solid lines, all author names; dashed lines, namesake-robust (full first names only, with the 1% most frequent surnames removed). (C) Growth in fractional output between the third quarters (July–September) of consecutive years, by author class. Authors are ranked by their combined output in the two years compared (top 1%, next 9%, bottom 90%; ties at a class boundary are shared), which avoids regression to the mean. Black bars, all authors; under proportional growth, every class would grow at the black-bar rate. The grey background marks pairs that end before ChatGPT's release, which show how far the classes diverge by chance. The dashed vertical line in A and B marks the release of ChatGPT. Panels for mathematics will be added [ANALYSIS PENDING: maths H2]. The figure was made with plotting code written by an AI agent (Claude, Anthropic, via Claude Code) under the author's direction (Methods, Use of AI tools).

For mathematics, the decomposition is pending [ANALYSIS PENDING: maths H2]. The share of papers with an author name posting five or more mathematics papers in a quarter rose from 5.3% in the third quarter of 2025 to 18.1% a year later (1.8% to 5.9% in the namesake-robust variant; S3 Table), but this share rises mechanically when everyone produces more and when more papers share common names, so it cannot separate broad from concentrated growth. As a cross-section, papers without such an author grew by 56% (from 10,271 to 16,013), two-thirds of the 8,716 additional papers, and the number of distinct author names rose by 41% and fractional output per name by 28%.

### AI-assisted writing (H3)

AI-associated style words rose in every group, experimental groups included (Fig 4; Table 2). In 2024, the year from which the word list was built, marker rates were 2.56 times their 2019–2022 level in computational bioRxiv categories, 2.15 times in wet-lab categories, 2.17 in arXiv theory, 2.13 in arXiv experiment and 2.73 on medRxiv. Within fields the rise did not differ detectably in 2024: the ratio of rises was 1.18 (0.98–1.42; p = 0.08) for computational against wet-lab biology and 1.00 (0.81–1.22) for theory against experiment. In 2025 and 2026 the rise in experimental physics exceeded that in theory (0.75; 0.61–0.91 and 0.60–0.95), but rates in these years are weak lower bounds. Computational categories started from a higher baseline (38.6 against 27.7 words per 100 abstracts), as Kobak et al. found for computational fields [15], but rose by a similar factor. On arXiv, at least 10.8% of 2024 abstracts in theory and 6.1% in experiment were processed with LLMs. No equivalence margin was set in advance [52], so "similar" here means no detectable difference: the 2024 intervals allow differences of about 20% in physics and 40% in biology.

**Fig 4. AI-associated style words by group.** Core marker words per 100 abstracts, relative to each group's 2019–2022 mean. The core words are the 261 style words of Kobak et al. [15] that appeared in fewer than 0.5% of bioRxiv and medRxiv abstracts in 2019–2022. bioRxiv: version-1 preprints posted in March and September of each year; medRxiv: all version-1 preprints; arXiv: papers with primary category in the physics theory or experiment archives; bioRxiv and medRxiv exclude COVID-19 preprints; 2026*, January–September (bioRxiv, March and September). The list was built from 2024 text, and its fall after 2024 reflects, at least in part, newer models and authors avoiding words now read as signs of LLM text; values after 2024 are therefore lower bounds on LLM-assisted writing. The markers date changes in style; they do not identify causes. Mathematics will be added [ANALYSIS PENDING: maths H3 markers]. The figure was made with plotting code written by an AI agent (Claude, Anthropic, via Claude Code) under the author's direction (Methods, Use of AI tools).

**Table 2. AI-associated style words (H3): rise by group and comparisons between groups.**

| Group or comparison | 2019–2022 | 2023 | 2024 | 2025 | 2026 (Jan–Sep) |
|---|---|---|---|---|---|
| *Marker rate (words per 100 abstracts) and rise* | | | | | |
| bioRxiv computational | 38.6 | ×1.89 | ×2.56 | ×2.41 | ×1.64 |
| bioRxiv wet lab | 27.7 | ×1.52 | ×2.15 | ×2.30 | ×1.57 |
| bioRxiv mixed | 31.0 | ×1.53 | ×1.96 | ×2.07 | ×1.44 |
| medRxiv | 26.6 | ×1.70 | ×2.73 | ×2.70 | ×1.87 |
| arXiv physics theory | 15.0 | ×1.55 | ×2.17 | ×2.34 | ×2.05 |
| arXiv physics experiment | 11.7 | ×1.52 | ×2.13 | ×2.95 | ×2.57 |
| *Ratio of rises (95% CI)* | | | | | |
| bioRxiv computational / wet lab | – | 1.19 (0.99–1.43) | 1.18 (0.98–1.42) | 1.04 (0.86–1.25) | 1.03 (0.86–1.24) |
| arXiv theory / experiment | – | 0.96 (0.79–1.18) | 1.00 (0.81–1.22) | 0.75 (0.61–0.91) | 0.75 (0.60–0.95) |
| arXiv physics / bioRxiv | – | 0.96 (0.83–1.11) | 0.89 (0.77–1.03) | 1.05 (0.91–1.21) | 1.36 (1.17–1.57) |
| arXiv experiment / bioRxiv | – | 0.76 (0.45–1.27) | 1.02 (0.61–1.71) | 1.32 (0.79–2.21) | 1.45 (0.87–2.44) |
| *Lower bound on LLM-processed abstracts* | | | | | |
| arXiv physics theory | 13.5%ᵃ | 4.9% | 10.8% | 13.8% | 11.2% |
| arXiv physics experiment | 10.2%ᵃ | 3.1% | 6.1% | 14.2% | 11.4% |

Marker rate: distinct core marker words per 100 titles and abstracts (Methods); rises are relative to the group's 2019–2022 mean. Ratios of rises: ordinary least squares on monthly log ratios relative to 2019–2022, with t intervals; comparisons involving bioRxiv use the 16 sampled months (March and September). Marker words drifted after 2024, and differently by corpus, so 2024 is the year for comparisons. ᵃ Share of abstracts with at least one core word in 2019–2022; lower bounds use a counterfactual extrapolated from the 2019–2022 trend.

The marker rise did not predict output growth. Across 27 bioRxiv categories and arXiv archives in 2023–2026, output growth was unrelated to the change in marker rate (coefficient 0.0005; −0.0016 to 0.0026), and its interaction with experimental work was positive (0.0037; 0.0000 to 0.0073; p = 0.049), the opposite of the sign H1 predicted; within bioRxiv the interaction was 0.0011 (−0.0023 to 0.0045). Markers for mathematics are pending [ANALYSIS PENDING: maths H3 markers]. Within arXiv physics, the second clause of H1 is not supported: experimental groups showed at least as large a rise in markers as theory and, in hep-ex, a departure of output from trend as large as theory's (below).

### Departures from trend and the comparison between servers (exploratory)

Against their own 2015–2022 trends, arXiv physics and mathematics accelerated in 2025–2026, while bioRxiv and PubMed did not (Table 3). In 2026, 14 of the 18 arXiv archives stood at least 1.25 times their trends, among them experimental particle physics (hep-ex 1.37; 1.12–1.67) and lattice gauge theory (hep-lat 1.39); the exceptions were nucl-ex (1.00), q-fin (1.03), physics (1.06) and cs (1.15), whose trend was 21% a year. arXiv's quantitative-biology archive stood at 1.26 although its January–September count fell by 7% from 2025. Mathematics ranked fifth of the 18 archives (rank p = 0.28).

**Table 3. Departures from the pre-2023 trend by field (exploratory).**

| Series | Trend per year | 2024 | 2025 | 2026 (Jan–Sep) |
|---|---|---|---|---|
| Physics (13 arXiv archives) | 2.9% | 1.05 (1.02–1.08) | 1.14 (1.10–1.18) | 1.32 (1.24–1.39) |
| Mathematics (arXiv math) | 2.9% | 1.04 (0.98–1.11) | 1.08 (1.02–1.14) | 1.48 (1.26–1.73) |
| Computer science (arXiv cs) | 21.0% | 1.00 (0.88–1.14) | 1.02 (0.88–1.18) | 1.15 (0.97–1.37) |
| Biology (bioRxiv, trend from 2018) | 12.4% | 0.91 (0.78–1.06) | 0.92 (0.75–1.12) | 0.91 (0.71–1.15) |
| Biomedicine (PubMed, quarterly) | 5.6% | 0.90 (0.85–0.96) | 0.95 (0.88–1.02) | 0.93 (0.86–1.01) |
| Medicine (medRxiv without COVID-19)ᵃ | 48.5% | 0.74 (0.56–0.97) | 0.60 (0.41–0.88) | 0.50 (0.30–0.80) |
| Social sciencesᵃ | 18.5% | 0.74 (0.61–0.91) | 0.83 (0.64–1.08) | 0.83 (0.62–1.11) |

Ratio of observed to trend-expected counts (95% CI), from Poisson pseudo-maximum-likelihood models with a linear trend, calendar-month effects and an indicator for April 2020 to March 2021, fitted to pre-2023 data from 2015 (arXiv), 2018 (bioRxiv) or 2019 (medRxiv, social sciences); Newey–West intervals. The counterfactual is each series' own extrapolated trend, not a level shared across series. ᵃ Trend dominated by the adoption of a new server; not interpreted. Archives, 2026: math-ph 1.81, nucl-th 1.58, quant-ph 1.54, nlin 1.52, math 1.48, hep-lat 1.39, hep-ex 1.37, astro-ph 1.34, stat 1.33, cond-mat 1.30, hep-ph 1.28, hep-th 1.28, gr-qc 1.26, q-bio 1.26, cs 1.15, physics 1.06, q-fin 1.03, nucl-ex 1.00; the largest departures are in archives whose pre-2023 trend was falling (math-ph −4.3%, nucl-th −2.5% and nlin −1.1% a year).

These departures compare each series with its own extrapolated trend, and bioRxiv's trend of 12% a year was fitted to years in which the server was still being adopted; in levels, bioRxiv grew more than the physics archives tested. What is specific to arXiv is the acceleration in 2026: relative to bioRxiv, the six physics archives gained 7% from 2025 to 2026 (1.07; 0.99–1.16), theory 8% (1.08; 0.99–1.17) and experiment 2% (1.02; 0.93–1.11). Meanwhile, the marker rise in 2024 was similar on the two servers (arXiv physics against bioRxiv 0.89; 0.77–1.03; experiment 1.02; 0.61–1.71). Output did not follow measured AI-assisted writing on either server.

The break tests cannot date the acceleration, because their admissible window ends before 2025; the slope break they place in physics in November 2024 (p = 0.001) lies at its edge. The yearly departures place most of the acceleration in 2025–2026 for physics and in 2026 for mathematics. The synthetic control replicated Nee et al.'s figure for mathematics [12]: 11.9% above its counterfactual in January–September 2026 (rank p = 0.05, the minimum attainable; 10.1% with a pre-period ending in November 2022), against their 11.9% for January–August on list entries. The agreement is not like for like. The monthly gap was near zero in January–April and reached 0.31 and 0.40 log points in August and September, so without September the excess is about 8%, and three donors had larger raw gaps in the placebo runs (cs 22.1%, stat 18.7%, econ 16.7%). The estimate is mathematics' excess over an accelerating arXiv, concentrated in a few months, not an effect of AI.

### Small-team papers in experimental particle physics (exploratory)

One further observation, made after the tests above, motivated the pre-registered test. Queries of INSPIRE-HEP during internal review (16 October 2026; S2 Appendix) found that primary hep-ex records with at most 10 authors and no collaboration nearly doubled from January–September 2024 to the same months of 2026 (from 187 to 366), accounting for 185 of the 205 records added since 2022, while papers with more than 300 authors rose by 4%. Of 60 such records from 2026 that were not conference papers, sampled at random and classified from titles and abstracts by a single unblinded coder (an AI agent in a reviewer role), 18 were simulation or future-facility studies, 17 machine-learning or AI methods, 7 statistical or software methods, 6 reviews or talk write-ups, 5 instrumentation papers, 4 reanalyses of existing data, 2 concept studies and 1 a report of new measurements. The growth of hep-ex may therefore lie mostly in papers that need no new data, but these counts are unvalidated [ANALYSIS PENDING: INSPIRE] and serve only to motivate the test [ANALYSIS PENDING: pre-registered test].

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
51. Gelman A, Stern H. The difference between "significant" and "not significant" is not itself statistically significant. Am Stat. 2006;60(4):328–331. doi:10.1198/000313006X152649
52. Lakens D. Equivalence tests: a practical primer for t tests, correlations, and meta-analyses. Soc Psychol Personal Sci. 2017;8(4):355–362. doi:10.1177/1948550617697177

<!-- SI FILES START -->
