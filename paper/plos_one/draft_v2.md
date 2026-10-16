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
| Introduction | 930 | 994 |
| Materials and methods | 3,699 | 3,981 |
| Results | 0 | 0 |
| Discussion | 0 | 0 |
| Conclusions | 0 | 0 |
| **Main text (Introduction to Conclusions)** | **4,629** | **4,975** |

Abstract: 288 words of prose (288 raw); PLOS ONE limit 300.
Figure legends in the main text: 0 words. Tables in the main text: 0 words.
References: 50 in the main list; SI lists: .
Markers: [AUTHOR] 22, [ANALYSIS PENDING] 9, [RECHECK] 3.
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

Decisions on hiring, promotion and funding rely heavily on counts of research outputs [1]. Counts are crude proxies for originality and rigour, but they carried some information because the outputs they count were costly to produce [2,3]. Generative artificial intelligence (AI) lowers the cost of producing the written part of research, whether it is used well or badly, and in preprints the use of large language models (LLMs) has reversed the association between writing complexity and paper quality [4]. Whether AI has also changed how many outputs are produced, and where, is an empirical question that bears directly on how counts can be read. A companion essay argues that evaluation built on costly outputs is not prepared for widespread, legitimate use of AI [5]; this article tests one empirical premise of that argument.

Output was growing before generative AI [6]: indexed articles were about 47% more numerous in 2022 than in 2016 [7]. Since then, an editorial in *Organization Science* has reported a 42% rise in submissions since the release of ChatGPT [8], the US National Institutes of Health (NIH) has reported that AI tools enabled some applicants to submit more than 40 applications in a single round [9], and arXiv received 40,363 submissions of all kinds in September 2026, against 20,569 in September 2024 [10]. Several funders, preprint servers and conferences have responded by limiting how many items each person may submit (S1 Table).

Several studies have measured how output changed. Qi et al. analysed 2.1 million preprints posted on arXiv, bioRxiv, medRxiv and SocArXiv from 2016 to 2025 with interrupted time series; they report that LLMs accelerated submission and revision and that computationally intensive fields benefited more than others [11]. Nee et al. fitted a synthetic control to monthly counts for 20 arXiv archives from January 2018 to August 2026 and estimated that mathematics recorded 11.9% more list entries in January–August 2026 than its synthetic counterfactual, a change they describe as a regime shift; in a pseudonymised author panel, the share of author units with at least five submissions rose from 2.45% to 3.80% [12]. At the level of individual authors, LLM adoption has been associated with higher output on arXiv, bioRxiv and SSRN [4] and in the social and behavioural sciences [13], although the event-study design behind the first of these estimates has been argued to produce spurious post-adoption dynamics [14]. [AUTHOR: the brief of 16 Oct dropped Kusumegi et al.'s output-gain estimate from the essay; R2 asks for it here together with Renault et al.'s comment. Confirm or delete this sentence.] The studies by Qi et al., Nee et al. and Filimonovic et al. are preprints.

A separate literature estimates how much scientific text is written with LLMs, from word frequencies and classifiers that measure style rather than purpose. At least 13.5% of 2024 PubMed abstracts were processed with LLMs, more in computational fields [15], and other studies estimate the prevalence by field and corpus with different measures [16–19] (S4 Table). Reading preprint counts as research output also requires attention to the servers. Fields adopted preprints at different times and to different degrees [20–22], medRxiv opened only in 2019 [23], COVID-19 brought a surge of preprints in 2020 [24], and servers screen submissions and differ in the genres they accept [25–27]. Output per author, finally, depends on how author names are matched [28,29], and extreme individual output has been studied with thresholds of more than 60 papers a year [30,31].

These studies leave two questions open. First, the finding that computationally intensive fields benefited more [11] rests on comparisons between servers and fields, which differ in preprint culture, platform rules and author populations as well as in the cost of research. Within a field, experimental and non-experimental work share most of these conditions, so a contrast between them is a sharper, falsifiable test of the idea that output grows where the work beyond writing is cheap and not where experiments bind; Blekhman has argued that AI has not yet raised productivity much in biology because its bottlenecks are experimental [2]. Second, aggregate counts do not show whether growth comes from many authors or a few. Nee et al.'s author panel addresses this for mathematics [12], with fixed thresholds of output that rise mechanically when everyone produces more.

This article makes three contributions. It reports three within-field contrasts, fixed before any model was estimated, as a falsification test of the account in which computational intensity governs where output grows. It replicates Nee et al.'s synthetic control for mathematics on a different count unit and extends the author-level analysis to theoretical physics with a decomposition free of regression to the mean. And it measures a marker of AI-assisted writing in the same groups whose output it compares.

The hypotheses were recorded in the analysis skeleton committed on 16 October 2026 at 16:42 UTC (commit 2cac071), after descriptive counts had been seen and before any model was estimated. They are reproduced as recorded:

- **H1.** AI-era acceleration of output is concentrated where the work beyond writing is also cheap: theory, computation, existing data. In experimental work, AI shows in the writing but much less, or not yet, in output.
- **H2.** Where output accelerates, the shift is broad. It comes from many established researchers producing more, not from a few outliers.
- **H3.** AI-assisted writing is widespread across fields, including experimental ones, so differences in output are not explained by differences in adoption.

H1 originated with me, from my view as a physicist and biologist that experimental biology was less affected than other fields; its wording, and H2 and H3, were drafted with AI assistance and adopted by me [AUTHOR: confirm the origin of H2 and H3]. The first clause of H1 was tested with three pre-specified within-field contrasts, its second clause and H3 with a marker of AI-assisted writing, and H2 with author-level measures. The design is observational: the release of AI tools and the dates of platform rules mark when things happened, not why.

## Materials and methods

### Study design and pre-specification

This observational study analyses monthly counts of new preprints (first versions). It has four parts: three within-field contrasts between experimental and non-experimental work (H1); the distribution of output among authors (H2); a marker of AI-assisted writing in the same groups (H3); and exploratory comparisons of fields, archives and servers with their own pre-2023 trends.

The groups were defined before their growth was computed, but the hypotheses and the choice of the three contrasts as the primary tests were recorded afterwards (commit 2cac071), when the descriptive growth of each group was known. The analysis plan was then written in the first version of this manuscript (commit 697fb25, 17:27 UTC), and the models were run in a separate session (the companion analysis; commits 37b4b11, f5ab16e and 7ac5647) [AUTHOR: state when the companion fixed its model specification relative to commit 697fb25]. "Pre-specified" and "primary" therefore mean fixed before any model was estimated, not before the data were seen: they protect against choosing models after seeing estimates, not against choosing contrasts. All other analyses are exploratory, and no exploratory estimate is used on its own to support a conclusion. Deviations from the plan are listed below. A hypothesis that I formed after seeing these results is being tested on held-out data under a separate, timestamped pre-registration (Pre-registered paper-level test).

### Data sources

*arXiv counts.* Monthly counts of new submissions by primary archive, excluding replacements and cross-lists, were read from arXiv's yearly statistics pages [32] for January 2010 to September 2026; the models use January 2015 onwards. Physics is the sum of 13 archives (astro-ph, cond-mat, gr-qc, hep-ex, hep-lat, hep-ph, hep-th, math-ph, nlin, nucl-ex, nucl-th, physics and quant-ph), mathematics is math and computer science is cs. Six pairs of categories are aliases of each other (for example math-ph and math.MP), so archive sums exceed arXiv's own total by about 5% and the physics and mathematics series overlap through math-ph. Unlike Nee et al.'s list entries, these counts exclude cross-lists [12].

*arXiv metadata.* Titles, abstracts, author lists, comments and categories were harvested through arXiv's OAI-PMH interface: every mathematics record modified since 1 January 2025 (harvested 15 October 2026; used for the descriptive measures of S3 Table), and every paper first submitted from January 2019 in mathematics and six physics archives, hep-th, hep-ph, gr-qc, nucl-th, hep-ex and nucl-ex (harvested 16 October 2026). Papers are assigned to their primary category and dated by the year and month in their identifier, which arXiv assigns when a paper is announced, not when it is submitted [33]. Annual counts of primary hep-th and hep-ph papers from this harvest match arXiv's statistics exactly for 2019–2025.

*bioRxiv.* Monthly counts of version-1 preprints for 25 subject categories, January 2019 to September 2026, came from the bioRxiv API [34] (retrieved 16 October 2026). From July 2019 their sum equals bioRxiv's official monthly totals; January–June 2019 is about 4% lower, because epidemiology and clinical-trials preprints, which later moved to medRxiv, cannot be queried by category. The category counts carry no topic flag and therefore include COVID-19 preprints. For the marker analysis, the titles and abstracts of every version-1 preprint posted in March and September of each year from 2019 to 2026 were retrieved.

*medRxiv.* Every version-1 preprint from the server's opening in June 2019 to September 2026 was read through the same API, one day at a time. Preprints whose title or abstract mentions COVID-19, SARS-CoV-2 or 2019-nCoV (S2 Appendix) are excluded from every medRxiv series; they were 66% of new medRxiv preprints in 2020 and 5% in 2026.

*PubMed and the social sciences.* PubMed counts are quarterly journal-article records by entry date [RECHECK: query, interface and retrieval date, from the companion scripts]. First versions on PsyArXiv, SocArXiv and EdArXiv were counted through the Open Science Framework (OSF) API [RECHECK: endpoint, from the companion scripts], with arXiv's econ and q-fin archives added. Because its counting method changed in the first quarter of 2025 and SocArXiv limits submissions to about one paper per author per week [35], the social-science series is shown for reference only and is not analysed.

*Terms of use and request rates.* arXiv's API terms, which cover OAI-PMH, allow no more than one request every three seconds over a single connection [36], and arXiv's robots.txt sets a crawl delay of 15 seconds [37]. The harvests for this study paused 2 s between OAI-PMH requests and 1 s between statistics pages, faster than these limits; the scripts' defaults are being set to the published limits, and any re-harvest will comply [AUTHOR: confirm before submission]. The bioRxiv and medRxiv API publishes no rate limit; its harvests used four to six parallel workers. arXiv metadata are released under CC0, and this work is not endorsed by arXiv. bioRxiv and medRxiv records carry their own licences, so abstracts are not redistributed; identifiers, dates, categories and derived flags are. OSF and PubMed data were used under their terms [38] [AUTHOR: confirm the NCBI terms].

### Groups for the within-field contrasts (H1)

The groups were proposed while the companion essay was being drafted and were fixed before their growth was computed; S2 Appendix lists them in full.

*Physics (C1).* Theory comprises hep-th, hep-ph, gr-qc and nucl-th, and experiment comprises hep-ex and nucl-ex. Archives that mix theory with observation or experiment (astro-ph, cond-mat, quant-ph) are in neither group, and neither is the lattice archive, hep-lat [AUTHOR: state why hep-lat was left out]. The labels are approximate. hep-ph includes phenomenology fitted to experimental data, gr-qc includes gravitational-wave data analysis, and arXiv's taxonomy places detectors, instrumentation and analysis methods outside hep-ex and nucl-ex, and descriptions of future programmes outside nucl-ex but not hep-ex [39].

*Biology (C2).* The computational group comprises the bioRxiv categories bioinformatics, systems biology and genomics, and the wet-lab group 12 categories from biochemistry to synthetic biology; the other ten categories form a mixed group that is shown but not tested. Genomics includes much bench sequencing, and bioinformatics includes research in which AI is the topic rather than a tool.

*Medicine (C3).* medRxiv preprints whose title or abstract names a widely reused public dataset or design (NHANES, UK Biobank, Global Burden of Disease, Mendelian randomisation, FAERS, MIMIC-III or MIMIC-IV, SEER or BRFSS), which recur in formulaic, rapidly scaled analyses [40,41], are contrasted with all other medRxiv preprints, both without COVID-19 preprints. The list shares five of the nine heavily mined datasets identified by Spick et al. (FAERS, NHANES, UK Biobank, FinnGen, Global Burden of Disease, MIMIC, CHARLS, CDC WONDER and TriNetX) [41] [AUTHOR: state when the list was fixed]. The comparison group is not experimental: it contains registries, health records, cohorts, modelling studies and reviews.

### Author-level measures (H2)

arXiv metadata carry no author identifiers, so authors are matched by normalised name strings (S2 Appendix). Different people can share a string, and initials-based matching distorts author-level measures [28,29], so every measure is also computed in a namesake-robust variant that keeps only full first names and removes the 1% most frequent surnames. In mathematics this removes 35.7% of author slots, mostly common East Asian surnames, so the variant describes a different population, not the same one with fewer collisions. In physics, papers with more than 50 authors are excluded: with them, a few white papers signed by hundreds of theorists would make 16.9% of active theory authors heavy producers in the third quarter of 2025, against 1.3% without them.

A heavy producer is an author name with five or more papers in a group in a calendar quarter, about 20 a year, far below the thresholds used for extreme output [30,31]. Fixed-threshold measures, such as the share of papers with a heavy producer, rise mechanically when everyone produces more. The main H2 measures are therefore (i) the shares of fractional output (each paper divided equally among its authors) produced by the top 1% and top 10% of active authors, which do not move under proportional growth; and (ii) a decomposition of the change in fractional output between the third quarters of consecutive years by author class. Authors are ranked on their combined output in the two years compared (top 1%, next 9% and bottom 90%; authors tied at a class boundary share the remaining places equally). The ranking is symmetric in the two years and so free of the regression to the mean that arises when classes are defined on one year; under proportional growth every class grows at the total rate, and pairs of years that end before ChatGPT's release show how much the classes differ by chance. Departures of each quarterly measure from its 2019–2022 trend were estimated by ordinary least squares with quarter effects and indicators for 2023–2026 (Newey–West errors, 4 lags) [42]. The data are a population of papers, not a sample, so no sampling intervals are given for the shares. Experimental physics has about 300 papers a quarter with 50 or fewer authors, and few of its authors give full first names, so only its all-names version is computed. For mathematics the same measures, with author histories from 2019 and windows aligned with Nee et al.'s panel, are pending [ANALYSIS PENDING: maths H2].

### Marker of AI-assisted writing (H3)

Following Kobak et al. [15], AI-assisted writing was measured by the frequency of style words whose use rose with LLMs. The source list is the 407 style words that Kobak et al. derived from PubMed abstracts. To keep words that were rare before LLMs, the list was filtered on baseline data only: 261 words appeared in fewer than 0.5% of the 41,270 bioRxiv and medRxiv abstracts of 2019–2022 (S2 Appendix). The same list was applied to the titles and abstracts of every corpus: bioRxiv version-1 preprints posted in March and September of each year, all medRxiv preprints, and every arXiv paper in mathematics and the six physics archives from 2019, with COVID-19 preprints excluded from bioRxiv and medRxiv. The metric is the number of distinct core words per 100 abstracts, by group and year, relative to the group's 2019–2022 mean.

The words that identify LLM text drift as models and authors change. The list was built from 2024 text; core words such as "delve" and "intricate" peaked in 2024 and were back near baseline in 2026, and by September 2026 some listed words were rarer in bioRxiv abstracts than before 2023, while abstract length did not change. Marker rates are therefore lower bounds on LLM-assisted writing, weak ones from 2025, and comparisons between groups are cleanest in 2024.

Whether the rise was similar in two groups was tested by ordinary least squares on the monthly log ratio of their marker rates, with indicators for 2023–2026 against the pooled 2019–2022 baseline and classical t intervals; autocorrelation-robust errors had come out about 2.5 times too narrow against the month-to-month variation of 2019–2022, and the bioRxiv sample has only 16 months. The pairs were computational against wet-lab bioRxiv categories, theory against experiment on arXiv, and each arXiv physics group against all of bioRxiv on the months both corpora cover. For arXiv, a lower bound on the share of LLM-processed abstracts was computed as in Kobak et al.: with *p* the observed share of abstracts containing at least one core word and *q* its counterfactual extrapolated from 2019–2022, the share is at least (*p* − *q*)/(1 − *q*). Finally, a panel of 27 bioRxiv categories and arXiv archives regressed output growth in 2023–2026 (the log ratio of January–September papers to 2022) on the change in marker rate, an indicator of experimental work (1 for wet lab or experiment, 0 for computational or theory, 0.5 for mixed) and their interaction, with server-specific year effects and errors clustered by category. H1 predicted a weaker association in experimental groups, that is, a negative interaction. The panel is ecological, and its arXiv part has only six clusters, so it is descriptive. Markers for mathematics are pending [ANALYSIS PENDING: maths H3 markers].

### Statistical analysis

*Within-field contrasts.* For each contrast, the monthly counts of the non-experimental group A and the experimental group B were stacked and fitted by Poisson pseudo-maximum likelihood [43]: log E[*y*<sub>*gt*</sub>] = *λ*<sub>*t*</sub> + *μ*<sub>*g*,*m*(*t*)</sub> + Σ<sub>*k*≠2022</sub> *β*<sub>*k*</sub>·1[*g* = A]·1[year(*t*) = *k*]. Month fixed effects *λ*<sub>*t*</sub> absorb every shock common to both groups, including platform-wide changes in rules, moderation and traffic, and *μ*<sub>*g*,*m*</sub> are group-specific calendar-month effects. exp(*β*<sub>*k*</sub>) is the rate ratio of A to B in year *k* relative to 2022, and exp(*β*<sub>2026</sub>), for January–September 2026, is the pre-specified estimate; values above 1 mean that the non-experimental group grew faster. With two groups the model is equivalent to a binomial model for A's share of the pair's monthly total, and it is consistent under overdispersion. Standard errors are Driscoll–Kraay (Bartlett kernel, 12 lags) [44]. Because the model has a coefficient for every year, these intervals measure within-year uncertainty only: they omit year-to-year shocks to the ratio and the heterogeneity between the archives or categories inside each group [45]. The three 2026 p values are Holm-adjusted [46] and reported with Bonferroni-adjusted (98.3%) intervals. The minimum detectable rate ratio at 80% power is exp(2.80 × SE) at α = 0.05 and exp(3.24 × SE) at α/3, the level of Holm's first step.

*In-space placebos.* Because the model intervals omit the heterogeneity between units, in-space placebos are the main benchmark, in the spirit of inference with few treated units [47]. The same estimate was computed for every pair among the 18 arXiv archives with complete monthly data since 2015 (153 pairs; the benchmark for C1) and for all 462 ways of splitting the 12 wet-lab categories into two halves of six (C2). I report the share of placebo pairs whose absolute log rate ratio is at least as large as the contrast's, and the contrast's percentile. These placebos ask whether the split between experimental and non-experimental work predicts divergence in 2026 better than arbitrary splits do. Placebos matched to each contrast's structure are pending [ANALYSIS PENDING: structure-matched placebos (all 455 assignments of 3 of the 15 contrasted bioRxiv categories as computational; all 4-against-2 draws of physics archives) and in-time placebos with the identical estimator]. No placebo distribution was defined for C3.

*Negative controls, leave-one-out estimates and sensitivity analyses.* H1 predicts no divergence between hep-ex and nucl-ex or between pairs of theory archives; a divergence as large as the main contrast points to heterogeneity among archives rather than to the cost of experiments. Each contrast was re-estimated without each of its archives or categories in turn; I treat an estimate as robust only if no single exclusion moves it across 1, a criterion stated after the estimates were seen. Sensitivity analyses used 2019 as the reference year, removed hep-ph from theory, removed genomics from the computational group or moved it to wet lab, dropped November 2025 to February 2026 (the months after arXiv's rule changes) and ended the sample in October 2025. A trend-adjusted variant, with group-specific linear trends instead of pre-2023 year effects, is reported only as a sensitivity analysis, because extrapolating the 2019–2022 trends of bioRxiv, when wet-lab fields were still adopting the server and COVID-19 inflated 2020, is not credible. Placebo break dates (a level shift in 2019, 2020 or 2021, fitted to pre-2023 data) are descriptive: their estimator differs from the main one, and with two or three pre-period years no informative p value is possible.

*Field-level departures from trend (exploratory).* Each field and archive series was fitted by Poisson pseudo-maximum likelihood with a linear trend, calendar-month effects, an indicator for April 2020 to March 2021 and indicators for 2023–2026, with Newey–West errors (12 lags; 4 for quarterly series) [42]. The exponentiated year coefficients are ratios of observed to trend-expected counts, with the trend identified from pre-2023 months: from 2015 for arXiv, 2018 for bioRxiv and 2019 for medRxiv and the social sciences. The medRxiv and social-science trends reflect the adoption of new servers and are not interpreted. The counterfactual is each series' own extrapolated trend, so a departure from trend is not a comparison of levels between servers. Mathematics' 2026 departure was ranked among those of the 18 arXiv archives. The relative acceleration of an arXiv group against bioRxiv in 2026 was estimated with the event-study model above, fitted to the arXiv group and bioRxiv from January 2019, as the ratio of the 2026 to the 2025 coefficient, using their covariance.

*Synthetic control for mathematics (exploratory).* Following Nee et al. [12] and Abadie et al. [48], mathematics' deseasonalised monthly log series was approximated by a convex combination of the 19 other archives with complete data since 2018 (14 received positive weight), fitted on January 2018 to December 2025. The 2026 gap is the mean log difference over January–September 2026, expressed as a percentage. Each donor in turn was treated as the treated unit; with 20 units the smallest attainable rank p value is 0.05. Because the donors are other arXiv archives, which also departed from trend in 2026, the gap measures mathematics' excess over arXiv, not an effect of AI [ANALYSIS PENDING: synthetic control with the OAI mathematics series, physics-only donors, math-ph excluded and mathematics excluded from the placebo donor pools].

*Break tests.* Sup-Wald tests for a single break at an unknown date [49] were computed on deseasonalised log series over the central 70% of each sample, with p values from a parametric bootstrap. With this trimming the last admissible break date is about December 2024 for the arXiv series and August 2025 for bioRxiv and medRxiv, so the tests cannot detect a break in 2025–2026. They are reported in S5 Table and not used to date the acceleration.

### Deviations from the analysis plan

The plan in v1 of this manuscript specified period effects for 2023–2024, 2025 and 2026 against multi-year baselines (2017–2022 for arXiv, 2019–2022 for bioRxiv and mid-2019 to 2022 for medRxiv), Poisson or negative binomial models with Newey–West errors, Bonferroni-adjusted intervals, Benjamini–Hochberg adjustment of the negative controls and leave-one-out estimates, and Bai–Perron tests for multiple breaks. The analysis as run used year-by-group effects with 2022 as the reference year, which turned the plan's pre-trend diagnostic into the primary estimate; month fixed effects and group-specific seasonality; Poisson pseudo-maximum likelihood with Driscoll–Kraay errors; Holm-adjusted p values, reported here with the planned Bonferroni intervals; shares of placebo pairs instead of adjusted p values for the negative controls, because adjusting falsification tests makes problems less likely to be flagged; and single-break sup-Wald tests [AUTHOR: reasons for, and timing of, the change of reference year]. The reference year matters. 2022 is not neutral: in the pre-period, C1's coefficients were 1.25 in 2020 and 1.19 in 2021, and C2's was 1.24 in 2019. Unweighted averages of the event-study coefficients over the planned baseline years give approximate 2026 estimates of 1.05 (C1), 1.02 (C2) and 1.03 (C3), against 1.14, 1.08 and 0.99 relative to 2022; these are not model estimates [ANALYSIS PENDING: planned specification (period effects against the planned baselines, with Bonferroni-adjusted intervals)]. The plan stated a decision rule for each contrast (support only if the adjusted interval excludes 1) but not for H1 as a whole; I add, after the fact, that H1 as a general claim needs support in all three fields.

### Pre-registered paper-level test

After the results above were known, I formed a refined hypothesis: within arXiv archives, papers that do not report new empirical data grew faster in 2025–2026, relative to their pre-2023 trend, than papers that do. The hypothesis is mine; it was prompted by an exploratory observation in experimental particle physics (Results). Its test was drafted with AI assistance and approved by me, and the plan was timestamped in the project repository (commit 763aa2b, 16 October 2026, 18:28 UTC) before any paper in the test archives was classified (S1 Text) [AUTHOR: OSF Registries DOI, if registered]. The confirmatory test uses arXiv cond-mat, astro-ph and quant-ph, which were not used to form the hypothesis at paper level, with papers dated by the submission of their first version from January 2017 to September 2026. A large language model with a fixed prompt and codebook, run at temperature 0, will classify each paper from its title, abstract and comments, without date or archive, as reporting new empirical data (new measurements, experiments or observations), not reporting new empirical data (theory, calculation, simulation, methods, reviews, reanalysis of existing data, or prospect studies) or unclear. I will code a stratified random sample of 200 abstracts blind to the model's labels and to dates, and the classifier will be used only if Cohen's κ is at least 0.60. The estimand is the ratio of the two classes' departures from archive-by-class trends (fitted to 2017–2022, with indicators for 2020–2021) over January 2025 to September 2026, pooled over the three archives, with moving-block bootstrap intervals. The hypothesis is supported if the pooled ratio exceeds 1 with an interval that excludes 1 and the ratio exceeds 1 in at least two of the three archives, and contradicted if the pooled ratio is below 1 with an interval that excludes 1. hep-ex and nucl-ex, where the idea arose, are analysed separately as exploratory. A second, exploratory component, which I proposed, uses the curated metadata of INSPIRE-HEP [50] (subject categories, document types, linked experiments, collaborations and author counts) to classify papers in hep-ex, hep-ph, hep-th, hep-lat, nucl-ex and nucl-th from 2017 to 2026 by rule, without AI, and asks whether papers that report new data departed less from their pre-2023 trend in 2025–2026 than other papers, overall and by collaboration size and document type. Neither component has been run [ANALYSIS PENDING: pre-registered test] [ANALYSIS PENDING: INSPIRE].

### Software and data processing

Data were harvested and analysed with Python scripts in the companion analysis (commit 7ac5647), which write only aggregate counts and derived variables [ANALYSIS PENDING: software versions and a pinned environment]. Data and code are described under Data availability.

### Ethics statement

This study analysed publicly available bibliographic metadata and aggregate counts; no human participants were recruited. Author name strings from arXiv metadata, which are personal data, were processed only to count papers per name within periods. Released author-level data are pseudonymised with a salted hash and keep only the variables the namesake-robust variants need (whether the first name is an initial, and the frequency rank of the surname) [AUTHOR: confirm that the pseudonymisation is implemented before release]. No name is reported, and table cells describing fewer than ten names are merged or suppressed. The main risk to individuals is that heavy producers could be re-identified by re-running the code on public metadata, with reputational harm if high output were read as AI misuse; it is mitigated by reporting aggregates only and by not interpreting any individual's output. [AUTHOR: data-protection office consultation, UPF/EMBL: name the office, the date and the outcome, and the lawful basis and safeguards recorded.] Data were retrieved under the terms of use of each source (Data sources).

### Use of AI tools

I used Claude (Anthropic), via Claude Code [AUTHOR: model and version], between 15 October and [AUTHOR: date] 2026, on a [AUTHOR: account type] account [AUTHOR: state whether model training on your data was switched off]. AI agents (i) searched the literature and checked references; (ii) drafted the text of every section from my decisions and outlines, and revised it after review; (iii) wrote all code for harvesting, processing, statistical analysis and figures, in a separate session (the companion analysis); (iv) produced all figures with that code; and (v) wrote internal critical reviews of the drafts in four reviewer roles, which are not peer review. H1 originated with me, as did the refined hypothesis of the pre-registered test and its INSPIRE-HEP component. The analysis plan, the group definitions, the statistical specification and the candidate recommendations in the Discussion were proposed by AI agents and adopted or modified by me [AUTHOR: confirm and describe your own validation, e.g. code review and re-runs: which code you reviewed line by line (groups, flags, author matching, models); re-runs in a clean environment (commit hash) with identical outputs; key numbers recomputed from the source APIs; sources read in full; and any AI proposal you rejected]. The interpretations and conclusions are mine. Checks made by AI agents are listed in S1 Appendix and are not counted as validation. The classifier of the pre-registered test is itself an LLM, validated against my blind coding. No AI tool is an author, and I take responsibility for the content.

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
