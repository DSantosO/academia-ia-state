<!--
DRAFT v2.
PLOS ONE Research Article. 16 Oct 2026. Revised from v1 (paper/plos_one/draft_v1.md) by an AI agent (Claude,
Anthropic, via Claude Code) after the round-1 reviews R1–R4 (paper/plos_one/reviews/round1/), the companion analysis's
formal results (paper/plos_one/stats/; companion commits 37b4b11, f5ab16e, 7ac5647 and 26ce2eb) and the author's
decisions of 16 Oct 2026 (paper/brief.md; pre-registration activated in commits 763aa2b and 78890e5, deviations
recorded in 11264ee and 1de63a9). Point-by-point response: paper/plos_one/reviews/round1/response_round1.md. Not yet
revised by the author.
WORD COUNT: [filled at build time]
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
- Figures: Fig1–Fig4 are the companion's PLOS-format files (paper/plos_one/figures/). Fig1 as committed still shows a
  model-release marker; on 16 Oct the author decided to remove it, and the companion is re-exporting the figure. The
  legends describe the re-exported figures (ChatGPT and the arXiv rules only). The files use Liberation Sans, which is
  metric-compatible with Arial; re-render them with Arial before submission (R4 minor 24).
- Mathematics' rank among arXiv archives: the companion's field_tests.json ranks 18 archives (rank p 0.111 = 2/18);
  a coordinator note said "2nd of 20". The text follows the JSON. methods.md says the synthetic control has "15
  donors"; the JSON has 19 candidate donors, 14 with positive weight. The text follows the JSON.
- The statements entered in the PLOS submission form (funding, competing interests, data availability, author
  contributions) follow the Supporting Information captions, outside the manuscript proper.
- To re-check before submission (R4 Major 12; carried over from v1's S1 Appendix, which no longer lists them): every
  quotation; the figures taken from McKiernan et al., Rice et al., Hanson et al., Lin and Zhu, Kobak et al.
  (computational fields), Liang et al., Holzwarth et al. and He and Bu; Moed; Cotton et al. References added in v2
  (refs_v2.py) have metadata read from Crossref or arXiv on 16 Oct 2026; the author should confirm that each supports
  the sentence that cites it. Sever et al.: author order as registered in Crossref.
- Related manuscripts (R4 Major 9) [AUTHOR]: the EMBO Reports essay draft uses the same figures and numbers; decide
  before submission (replace its data figures or withdraw it), post this article as a preprint, disclose the Zenodo
  essay and the Nature Correspondence in the cover letter with copies, align the competing-interest statements across
  venues, and mint the companion essay's DOI (reference CompanionEssay), which cannot be cited without one.
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

Research evaluation relies on counts of outputs, and generative artificial intelligence (AI) lowers the cost of writing them. If it lowered the cost of papers mainly where no new experiments are needed, preprint output should have grown faster in theoretical, computational and secondary-data work than in experimental work within the same field. I tested this prediction with three contrasts fixed before any model was estimated, in monthly counts of new preprints on arXiv (2015–2026), bioRxiv and medRxiv (2019–2026). Relative to 2022, the January–September 2026 rate ratios were 1.14 (95% CI 1.00–1.30; Holm-adjusted p = 0.11) for theoretical against experimental physics, 1.08 (1.03–1.14; p = 0.01) for computational against wet-lab biology and 0.99 (0.88–1.10; p = 0.82) for medRxiv preprints naming widely reused public datasets against the rest. Against in-space placebos, the physics and biology contrasts were unremarkable (placebo p = 0.61 and 0.20); the physics test could detect only ratios above 1.21, and the biology ratio fell to 0.93 without bioinformatics. The pre-specified tests therefore did not support the prediction. AI-associated style words in abstracts rose two- to threefold in every group by 2024, experimental groups included, and did not predict output growth. In exploratory analyses, arXiv physics and mathematics stood 32% and 48% above their 2015–2022 trends in 2026, and 14 of 18 arXiv archives, experimental particle physics included, stood at least 25% above theirs; bioRxiv (0.91 of trend) and PubMed (0.93) did not, although bioRxiv's count grew more since 2022 (1.53-fold) than that of the physics archives tested (1.33-fold). In theoretical physics, output grew in every class of authors, fastest among the most productive. These data cannot attribute the changes to AI. They show AI-assisted writing in every field studied while counts moved unevenly across servers, which limits comparisons of counts across fields and years.

<!-- Abstract: PLOS ONE limit 300 words; see the word count in the header. -->

## Introduction

Decisions on hiring, promotion and funding rely heavily on counts of research outputs [@Moher2018]. Counts are crude proxies for originality and rigour, but they carried some information because the outputs they count were costly to produce [@Blekhman2026; @Hansen2026]. Generative artificial intelligence (AI) lowers the cost of producing the written part of research, whether it is used well or badly; in preprints, the use of large language models (LLMs) has even reversed the association between writing complexity and paper quality [@Kusumegi2025]. Whether AI has also changed how many outputs are produced, and where, bears directly on how counts can be read. A companion essay argues that evaluation built on costly outputs is not prepared for widespread, legitimate use of AI [@CompanionEssay]; this article tests one empirical premise of that argument.

Output was growing before generative AI [@Bornmann2021]: indexed articles were about 47% more numerous in 2022 than in 2016 [@Hanson2024]. Since then, an editorial in *Organization Science* has reported a 42% rise in submissions since the release of ChatGPT [@Gartenberg2026], the US National Institutes of Health (NIH) has reported that AI tools enabled some applicants to submit more than 40 applications in one round [@NIH2025], and arXiv received 40,363 submissions of all kinds in September 2026, against 20,569 in September 2024 [@arXiv2026]. Several funders, preprint servers and conferences have responded by limiting how many items each person may submit (S1 Table).

Several studies have measured how output changed. Qi et al. analysed 2.1 million preprints on arXiv, bioRxiv, medRxiv and SocArXiv from 2016 to 2025 and report that computationally intensive fields benefited more than others [@Qi2025]. Nee et al. estimated with a synthetic control that arXiv mathematics recorded 11.9% more list entries in January–August 2026 than its counterfactual, a change they call a regime shift, and that the share of author units with at least five submissions rose from 2.45% to 3.80% [@Nee2026]. For individual authors, LLM adoption has been associated with higher output on arXiv, bioRxiv and SSRN [@Kusumegi2025] and in the social and behavioural sciences [@Filimonovic2025], although the design behind the first of these estimates may produce spurious post-adoption dynamics [@Renault2026]. [AUTHOR: the brief of 16 Oct dropped Kusumegi et al.'s output-gain estimate from the essay; R2 asks for it here together with Renault et al.'s comment. Confirm or delete this sentence and the related one in Limitations.]

Other studies estimate how much scientific text is written with LLMs, from word frequencies and classifiers that measure style rather than purpose: at least 13.5% of 2024 PubMed abstracts were processed with LLMs, more in computational fields [@Kobak2025], and estimates by field vary with the measure [@Liang2025; @LinZhu2025; @Holzwarth2026; @HeBu2025] (S4 Table). Preprint counts also depend on the servers: fields adopted preprints at different times and rates [@Lariviere2014; @Abdill2019; @WangChenGlanzel2020], medRxiv opened only in 2019 [@Krumholz2020], COVID-19 brought a surge of preprints in 2020 [@Fraser2021], and servers screen submissions and differ in the genres they accept [@Sever2019; @bioRxivFAQ; @medRxivAbout]. Output per author depends on how names are matched [@Milojevic2013; @KimDiesner2016], and extreme individual output has been studied with thresholds above 60 papers a year [@Ioannidis2018; @Ioannidis2024].

The finding that computationally intensive fields benefited more [@Qi2025] rests on comparisons between servers and fields, which differ in preprint culture, platform rules and author populations as well as in the cost of research. Within a field, experimental and non-experimental work share most of these conditions, so contrasting them is a sharper, falsifiable test of the idea, argued for biology by Blekhman [@Blekhman2026], that output grows where the work beyond writing is cheap and not where experiments bind. Aggregate counts, moreover, do not show whether growth comes from many authors or a few.

This article therefore reports three within-field contrasts, fixed before any model was estimated, as a falsification test of the account in which computational intensity governs where output grows; replicates Nee et al.'s synthetic control on a different count unit and extends the author-level analysis to theoretical physics; and measures a marker of AI-assisted writing in the same groups. The hypotheses were recorded in the analysis skeleton committed on 16 October 2026 at 16:42 UTC (commit 2cac071), after descriptive counts had been seen and before any model was estimated, and are reproduced as recorded:

- **H1.** AI-era acceleration of output is concentrated where the work beyond writing is also cheap: theory, computation, existing data. In experimental work, AI shows in the writing but much less, or not yet, in output.
- **H2.** Where output accelerates, the shift is broad. It comes from many established researchers producing more, not from a few outliers.
- **H3.** AI-assisted writing is widespread across fields, including experimental ones, so differences in output are not explained by differences in adoption.

H1 originated with me, from my view as a physicist and biologist that experimental biology was less affected than other fields; its wording, and H2 and H3, were drafted with AI assistance and adopted by me [AUTHOR: confirm the origin of H2 and H3, and the description of your field]. The first clause of H1 was tested with three pre-specified contrasts, its second clause and H3 with a marker of AI-assisted writing, and H2 with author-level measures. The design is observational: the release dates of AI tools and of platform rules mark when things happened, not why.

## Materials and methods

### Study design and pre-specification

This observational study analyses monthly counts of new preprints (first versions) and, for H2 and H3, the authors, titles and abstracts of individual papers. The groups were defined before their growth was computed, but the hypotheses and the choice of the three contrasts as primary tests were recorded when each group's descriptive growth was known (commit 2cac071). The analysis plan was written in v1 of this manuscript (commit 697fb25, 17:27 UTC), and the models were run in a separate session, the companion analysis [AUTHOR: state when the companion fixed its model specification relative to commit 697fb25]. "Pre-specified" therefore means fixed before any model was estimated, not before the data were seen: it protects against choosing models after seeing estimates, not against choosing contrasts. All other analyses, including those requested in review, are exploratory.

### Data sources

*arXiv.* Monthly counts of new submissions by primary archive, excluding replacements and cross-lists, were read from arXiv's statistics pages for January 2010 to September 2026 [@arXivStats], with versions adding cross-lists (list entries, the unit of Nee et al. [@Nee2026]); physics sums 13 archives (S2 Appendix), and aliased categories put archive sums about 5% above arXiv's total. Titles, abstracts, authors, comments and categories were harvested through arXiv's OAI-PMH interface on 15 October 2026 (mathematics records modified since January 2025) and 16 October 2026 (papers since 2019 in mathematics and the six physics archives of the contrast). Papers are dated by the month in their identifier, which arXiv assigns at announcement, not submission [@arXivAvailability]; annual hep-th and hep-ph counts from the harvest match arXiv's statistics exactly for 2019–2025.

*bioRxiv and medRxiv.* Monthly counts of version-1 preprints in 25 bioRxiv subject categories (January 2019 to September 2026) came from the bioRxiv API [@bioRxivAPI]; from July 2019 they sum to bioRxiv's official totals, and they include COVID-19 preprints. Titles and abstracts were retrieved for bioRxiv preprints posted in March and September of each year and for every medRxiv version-1 preprint from June 2019; medRxiv preprints that mention COVID-19 in the title or abstract are excluded from every medRxiv series (S2 Appendix).

*Other series.* PubMed journal articles per quarter by entry date, in total and with a US affiliation, were counted with NCBI's E-utilities. A social-science series (PsyArXiv, SocArXiv and EdArXiv through the Open Science Framework (OSF) API, plus arXiv econ and q-fin) is shown for reference only: from early 2025 the OSF API lists each version of a preprint as a separate record, so first versions were counted differently from 2025 [ANALYSIS PENDING: OSF continuity check, with 2023–2024 quarters counted both ways], and SocArXiv limits submissions per author [@SocArXiv2026].

*Terms of use and request rates.* arXiv metadata are released under CC0. The OAI-PMH harvests kept to arXiv's limit of one request every three seconds [@arXivAPITerms], but arXiv's statistics pages were retrieved with 1-s pauses against a 15-s crawl delay [@arXivRobots], and the OSF counts faster than the rate documented for unauthenticated clients, whereas the Center for Open Science's terms forbid unreasonable traffic loads [@OSFTerms]; no request was refused, and the scripts now comply (S1 Data). The bioRxiv and medRxiv API states no limit, and PubMed requests stayed within three a second. Abstracts are not redistributed, and no source endorses this work. Data were retrieved on 15–16 October 2026.

### Groups for the within-field contrasts (H1)

The groups were proposed while the companion essay was being drafted and fixed before their growth was computed (S2 Appendix). In physics (C1), theory is hep-th, hep-ph, gr-qc and nucl-th, and experiment is hep-ex and nucl-ex; astro-ph, cond-mat, quant-ph and hep-lat are in neither group [AUTHOR: state why hep-lat was left out]. gr-qc includes gravitational-wave experiments and, under the rule applied to astro-ph and cond-mat, should have been left out of theory; C1 is reported as pre-specified and also, as a correction made after the results were seen, without gr-qc. In biology (C2), bioinformatics, systems biology and genomics are contrasted with 12 wet-lab categories; genomics includes bench sequencing, and in bioinformatics AI is often the topic rather than a tool. In medicine (C3), medRxiv preprints naming a widely reused public dataset or design (NHANES, UK Biobank, Global Burden of Disease, Mendelian randomisation, FAERS, MIMIC-III or MIMIC-IV, SEER or BRFSS), which recur in formulaic analyses [@Suchak2025; @Spick2026], are contrasted with all other medRxiv preprints, both without COVID-19 preprints. The list shares five of the nine heavily mined datasets of Spick et al. [@Spick2026] [AUTHOR: state when the list was fixed], and the comparison group is largely secondary-data research, not experiment.

### Author-level measures (H2)

Authors are matched by normalised name strings, because arXiv has no author identifiers. Such strings merge different people and split the same person [@Milojevic2013; @KimDiesner2016], so every measure is also computed in a namesake-robust variant (full first names only, 1% most frequent surnames removed), which describes a different population; in physics, papers with more than 50 authors are excluded (S2 Appendix). A heavy producer is a name with five or more papers in a group in a quarter, about 20 a year, far below the thresholds used for extreme output [@Ioannidis2018; @Ioannidis2024]. Because fixed thresholds are crossed mechanically when everyone produces more, the main measures are the shares of fractional output (each paper divided equally among its authors) produced by the top 1% and top 10% of active authors, which do not move under proportional growth, and a decomposition of the change in fractional output between consecutive third quarters by author class (top 1%, next 9%, bottom 90%). Classes are defined on combined output in both years, which avoids regression to the mean; under proportional growth every class grows at the total rate, and pairs of years before ChatGPT's release show how much classes differ by chance. Departures from 2019–2022 trends were estimated by ordinary least squares with quarter effects and Newey–West errors [@NeweyWest1987]. The data are a population, so shares carry no sampling intervals. Mathematics is pending [ANALYSIS PENDING: maths H2].

### Marker of AI-assisted writing (H3)

AI-assisted writing was measured by the frequency of the 407 style words whose use rose with LLMs in Kobak et al.'s study [@Kobak2025], filtered on baseline data only to the 261 that appeared in fewer than 0.5% of the 41,270 bioRxiv and medRxiv abstracts of 2019–2022 (S2 Appendix). The words were counted in the titles and abstracts of bioRxiv preprints posted in March and September, all medRxiv preprints and all arXiv papers in mathematics and the six physics archives (COVID-19 preprints excluded), as distinct core words per 100 abstracts relative to the group's 2019–2022 mean. The words peaked in 2024, the year the list was built from, and some were rarer in 2026 than before 2023, so the rates are lower bounds on LLM-assisted writing, weak ones from 2025, and comparisons between groups are cleanest in 2024. Differences in the rise were estimated by ordinary least squares on monthly log ratios of two groups' rates relative to 2019–2022, with t intervals (autocorrelation-robust errors had been about 2.5 times too narrow). For arXiv, a lower bound on the share of LLM-processed abstracts was computed as in Kobak et al. A panel of 27 bioRxiv categories and arXiv archives regressed output growth in 2023–2026 on the change in marker rate, an indicator of experimental work and their interaction (server-specific year effects; errors clustered by category); H1 predicted a negative interaction. The panel is ecological and its arXiv part (six clusters) descriptive. Mathematics is pending [ANALYSIS PENDING: maths H3 markers].

### Statistical analysis

*Within-field contrasts.* For each contrast, the monthly counts of the non-experimental group A and the experimental group B were stacked and fitted by Poisson pseudo-maximum likelihood [@SantosSilva2006]: log E[*y*<sub>*gt*</sub>] = *λ*<sub>*t*</sub> + *μ*<sub>*g*,*m*(*t*)</sub> + Σ<sub>*k*≠2022</sub> *β*<sub>*k*</sub>·1[*g* = A]·1[year(*t*) = *k*]. Month fixed effects *λ*<sub>*t*</sub> absorb every shock common to both groups, including platform-wide changes in rules and moderation, and *μ*<sub>*g*,*m*</sub> are group-specific calendar-month effects. The pre-specified estimate is exp(*β*<sub>2026</sub>), the rate ratio of A to B in January–September 2026 relative to 2022; values above 1 mean that the non-experimental group grew faster. Driscoll–Kraay standard errors (12 lags) [@DriscollKraay1998] measure within-year uncertainty only; they omit year-to-year shocks to the ratio and heterogeneity between the archives or categories in each group [@Bertrand2004]. The three 2026 p values are Holm-adjusted [@Holm1979] and reported with Bonferroni-adjusted (98.3%) intervals. Minimum detectable rate ratios at 80% power are exp(2.80 × SE) at α = 0.05 and exp(3.24 × SE) at α/3, the level of Holm's first step.

*In-space placebos (primary inference).* As with few treated units [@ConleyTaber2011], each contrast is compared with the same estimate for all 153 pairs of the 18 arXiv archives with complete data since 2015 (C1 and its variants) and all 462 splits of the 12 wet-lab categories into halves (C2). The placebo p value is the share of placebos at least as far from 1, with one added to numerator and denominator; it asks whether the experimental split predicts divergence better than arbitrary splits do [ANALYSIS PENDING: structure-matched placebos (all 455 assignments of 3 of the 15 bioRxiv categories as computational; all 4-against-2 draws of physics archives)]. I also report the 2026 coefficient divided by the standard deviation of the pre-2022 year coefficients. No placebo was defined for C3.

*Robustness and acceleration.* Under H1, the two experimental archives, and pairs of theory archives, should not diverge. Each contrast was re-estimated without each component; an estimate is treated as robust only if no single exclusion moves it across 1 (a criterion stated after the estimates were seen). Because 2022 was a low year for two contrasts, each was also estimated against pooled bases (2017–2019, alone and with 2022, for arXiv; 2019, alone and with 2022, for bioRxiv and medRxiv). Because H1 concerns acceleration, each was also estimated as the ratio of its 2026 to its 2025 coefficient and as the change in slope of the deseasonalised log ratio after December 2022 and November 2024 (Newey–West intervals; parametric-bootstrap p values). Other sensitivity analyses (S5 Table) removed hep-ph, removed or reassigned genomics, dropped November 2025 to February 2026, ended the sample in October 2025 or added group-specific linear trends, which cannot credibly be extrapolated from years shaped by COVID-19 and bioRxiv's adoption.

*Exploratory analyses.* Each field and arXiv archive was fitted by Poisson pseudo-maximum likelihood with a linear trend, calendar-month effects, a COVID-19 indicator (April 2020 to March 2021) and indicators for 2023–2026 (Newey–West errors). The exponentiated year coefficients are ratios of observed to trend-expected counts, with trends fitted to pre-2023 months (from 2015 for arXiv and 2018 for bioRxiv); the medRxiv and social-science trends reflect the adoption of new servers and are not interpreted. Mathematics was ranked among the 18 archives, for new submissions and for list entries. The 2026 acceleration of an arXiv group relative to bioRxiv, and US against other PubMed articles (base 2023–2024), were estimated with the event-study model. A synthetic control for mathematics followed Nee et al. [@Nee2026] and Abadie et al. [@Abadie2010], and sup-Wald [@Andrews1993] and fixed-date Wald tests looked for breaks in slope or level as late as January 2026 (S2 Appendix) [ANALYSIS PENDING: synthetic control with the OAI mathematics series, physics-only donors and math-ph excluded].

### Deviations from the analysis plan

The plan in v1 specified period effects against multi-year baselines (2017–2022 for arXiv, 2019–2022 for bioRxiv, mid-2019 to 2022 for medRxiv), Poisson or negative binomial models with Newey–West errors, Bonferroni-adjusted intervals, Benjamini–Hochberg adjustment of negative controls and Bai–Perron break tests. The analysis as run used year-by-group effects with 2022 as the reference, turning the plan's pre-trend diagnostic into the primary estimate; month fixed effects; pseudo-maximum likelihood with Driscoll–Kraay errors; Holm adjustment, reported with the planned Bonferroni intervals; placebo shares for negative controls, because adjusting falsification tests makes problems harder to flag; and single-break tests [AUTHOR: reasons for, and timing of, the change of reference year]. The reference year matters, because 2022 was a low year for C1 (pre-period coefficients 1.25 in 2020 and 1.19 in 2021) and C2 (1.24 in 2019): pooled bases close to the planned ones give 1.12 (C1), 0.99 (C2) and 0.99 (C3), against 1.14, 1.08 and 0.99 relative to 2022 [ANALYSIS PENDING: planned specification (period effects against the planned 2017–2022 and 2019–2022 baselines, with Bonferroni-adjusted intervals)]. The plan gave a decision rule for each contrast (support only if the adjusted interval excludes 1) but none for H1 as a whole; I add, after the fact, that H1 as a general claim needs support in all three fields.

### Pre-registered paper-level tests

After these results were known, I formed a refined hypothesis, prompted by an exploratory observation in experimental particle physics (Results): within a field, papers that report no new empirical data grew faster in 2025–2026, relative to their pre-2023 trends, than papers that do. It moves the measure of experimental dependence from labels to individual papers. Its tests were drafted with AI assistance, approved by me and timestamped in the project repository before any paper was classified (commits 763aa2b and 78890e5; S1 Text) [AUTHOR: OSF Registries DOI, if registered]. Three confirmatory tests compare the 2025–2026 departures from 2017–2022 trends of papers with and without new data: in arXiv cond-mat, astro-ph and quant-ph, archives not used to form the hypothesis; on bioRxiv and medRxiv; and as a dose–response across the categories of all three servers. A Claude model (Anthropic) [AUTHOR: model and version] classifies stratified random samples (about 6,800 arXiv and 3,700 bioRxiv and medRxiv papers) once each, from title and abstract without date or server; class shares scale monthly totals, and the bootstrap redraws the samples. A domain's results are confirmatory only if the classifier agrees with my blind coding of 400 papers at Cohen's κ ≥ 0.60, and exploratory otherwise. Two deviations were recorded before any growth by class was computed (commits 11264ee and 1de63a9): at my request, classification and estimation precede my coding, which stays blind to dates, servers and model labels; and samples replace full classification, with one classification per paper because the temperature could not be set. An exploratory component that I proposed classifies particle and nuclear physics papers by rule from INSPIRE-HEP metadata [@INSPIREAPI]. No result of these tests is reported here [ANALYSIS PENDING: pre-registered test] [ANALYSIS PENDING: INSPIRE].

### Software and data processing

Data were harvested and analysed with Python scripts (numpy, pandas, scipy, statsmodels and matplotlib) in the companion analysis, whose last commit for this version is 26ce2eb; its pipeline reproduces every estimate and figure from the committed data with fixed random seeds [ANALYSIS PENDING: software versions and a pinned environment].

### Ethics statement

This study analysed public bibliographic metadata and aggregate counts; no human participants were recruited. Author name strings from arXiv, which are personal data, were processed only to count papers per name within periods and are never written to released files; no name is reported, and no statistic describing fewer than ten authors is released. Any author-level file released later will be pseudonymised with a salted hash [AUTHOR: decide whether to release it after the consultation below]. The main risk, re-identification of heavy producers by re-running the code, with reputational harm if high output were read as misuse of AI, is mitigated by reporting aggregates only and by interpreting no individual's output. [AUTHOR: data-protection office consultation, UPF/EMBL: name the office, the date and the outcome, and the lawful basis and safeguards recorded.] Data were retrieved under each source's terms of use (Data sources).

### Use of AI tools

I used Claude (Anthropic), via Claude Code [AUTHOR: model and version], between 15 October and [AUTHOR: date] 2026, on a [AUTHOR: account type] account [AUTHOR: state whether model training on your data was switched off]. AI agents (i) searched the literature and checked references; (ii) drafted the text of every section from my decisions and outlines, and revised it after review; (iii) wrote all code for harvesting, processing, statistical analysis and figures, in a separate session (the companion analysis); (iv) produced all figures with that code; and (v) wrote internal critical reviews of the drafts in four reviewer roles, which are not peer review. H1 originated with me, as did the refined hypothesis of the pre-registered tests and their INSPIRE-HEP component. The analysis plan, the group definitions, the statistical specification and the candidate recommendations in the Discussion were proposed by AI agents and adopted or modified by me [AUTHOR: confirm and describe your own validation, e.g. code review and re-runs: the code you reviewed line by line (groups, flags, author matching, models); re-runs of the pipeline (commit hash) with identical outputs; key numbers recomputed from the source APIs; sources read in full; any AI proposal you rejected]. The interpretations and conclusions are mine. Checks made by AI agents are listed in S1 Appendix and are not counted as validation. No AI tool is an author, and I take responsibility for the content.

## Results

### Overview of counts

New preprints rose in every field from 2022 to 2026, but not in the same way (Fig 1; S2 Table). From January–September 2022 to the same months of 2026, bioRxiv grew 1.53-fold, more than the six physics archives of the within-field contrast (1.33-fold) and less than mathematics (1.71-fold). bioRxiv grew steadily, by 9–13% a year in 2023–2026, whereas the six physics archives grew by 0%, 6% and 6% in 2023–2025 and by 19% in 2026. In arXiv mathematics, September 2026 alone had 8,360 new papers, against 5,903 in August [ANALYSIS PENDING: dating by first-version submission, and January–August versions of every 2026 estimate].

<!--LEGEND-->
**Fig 1. New preprints by field, indexed to 2022.** Quarterly new preprints (first versions), each series divided by its mean quarterly count in 2022 (2022 = 100), January 2020 to September 2026; the number in each legend entry is the index for July–September 2026. Physics: new submissions to the 13 arXiv physics archives, by primary archive. Mathematics: arXiv math. Computer science: arXiv cs, shown for reference; it includes AI research itself. Biology: bioRxiv. Medicine: medRxiv, excluding preprints that mention COVID-19 or SARS-CoV-2 in the title or abstract. Social sciences: first versions on PsyArXiv, SocArXiv and EdArXiv plus arXiv econ and q-fin, shown for reference only (Methods). Dashed vertical lines mark the release of ChatGPT (30 November 2022), arXiv's rule on review and position papers in computer science (31 October 2025) and arXiv's cap of two submissions per submitter per month (1 October 2026); they are dates for reference, not estimated break points or causes. Indexing to 2022 favours series whose 2022 count was low, such as medicine and biology; departures from each series' own trend are reported in the text. The code that drew this figure was written with an AI assistant (Claude, Anthropic, via Claude Code) under the author's direction; data and code are in S1 Data.
<!--/LEGEND-->

### Within-field contrasts (H1)

The pre-specified within-field tests did not support H1 (Table 1; Fig 2). Relative to 2022, the January–September 2026 rate ratio of non-experimental to experimental work was 1.14 (95% CI 1.00–1.30; Holm-adjusted p = 0.11) in physics, 1.08 (1.03–1.14; p = 0.01) in biology and 0.99 (0.88–1.10; p = 0.82) in medicine. With the planned Bonferroni-adjusted intervals only the biology contrast excludes 1 (1.02–1.16), so H1 fails the rule that it needs support in all three fields. The model intervals understate the uncertainty, because year-level shocks are common: four of the 13 pre-2022 year coefficients of the three contrasts have p < 0.05. Against the in-space placebos, the primary inference, the physics contrast was matched or exceeded by 61% of pairs of arXiv archives (placebo p = 0.61) and the biology contrast by 20% of halvings of the wet-lab categories (p = 0.20).

<!--TABLE-->
**Table 1. Pre-specified within-field contrasts: estimates and checks.**

| | C1 physics: theory / experiment | C2 biology: computational / wet lab | C3 medicine: public dataset / other |
|---|---|---|---|
| New preprints per month, 2026 (A; B) | 1,484; 142 | 698; 1,994 | 100; 1,292 |
| 2026 vs 2022: rate ratio (95% CI) | 1.14 (1.00–1.30) | 1.08 (1.03–1.14) | 0.99 (0.88–1.10) |
| Holm-adjusted p; Bonferroni 98.3% CI | 0.11; 0.97–1.34 | 0.01; 1.02–1.16 | 0.82; 0.86–1.13 |
| In-space placebo p (primary inference) | 0.61 (153 archive pairs) | 0.20 (462 wet-lab halvings) | not defined |
| 2026 coefficient / SD of pre-2022 year coefficients (p) | 1.54 (0.12) | 0.67 (0.50) | −0.19 (0.85) |
| Minimum detectable rate ratio, 80% power (α = 0.05; α/3) | 1.21; 1.25 | 1.08; 1.09 | 1.17; 1.20 |
| Event study, 2023; 2024; 2025 | 1.08; 1.11; 1.08 | 0.97; 0.94; 0.98 | 0.99; 0.97; 0.92 |
| Pre-period coefficients beyond 0.9–1.1 | 2020: 1.25; 2021: 1.19 | 2019: 1.24 | 2020: 0.88 |
| Other bases: 2019 | 1.05 (0.90–1.23) | 0.87 (0.80–0.95) | 0.98 (0.84–1.15) |
| Other bases: pooled | 2017–2019: 1.11 (0.97–1.26); with 2022: 1.12 (0.99–1.26) | 2019 and 2022: 0.99 (0.80–1.22) | 2019 and 2022: 0.99 (0.89–1.09) |
| Planned baseline (approximate) | 1.05 | 1.02 | 1.03 |
| Acceleration: 2026 / 2025 | 1.05 (0.89–1.24) | 1.10 (1.06–1.15) | 1.08 (1.01–1.14) |
| Slope change after December 2022, % a year (bootstrap p) | −0.6 (−5.4 to 4.4; 0.86) | 10.8 (5.2 to 16.7; 0.024) | −4.5 (−9.0 to 0.2; 0.17) |
| Trend-adjusted, 2026 | 0.98 (0.72–1.33) | 1.48 (1.06–2.07) | 0.85 (0.60–1.19) |
| Leave-one-out range (component dropped) | 1.03 (nucl-ex) to 1.43 (hep-ex) | 0.93 (bioinformatics) to 1.14 (genomics) | – |
| Negative controls | hep-ex / nucl-ex 1.39 (1.19–1.64); six theory pairs 0.85–1.06 | – | – |
| Reading | Inconclusive | Fragile in level; acceleration confounded with the end of adoption | Null |

Rate ratio of group A to group B, from Poisson pseudo-maximum-likelihood models with month fixed effects and group-specific calendar-month effects; values above 1 mean that the non-experimental group grew faster. 95% CIs are Driscoll–Kraay intervals, which measure within-year uncertainty only. Placebo p: share of placebo pairs at least as far from 1, with one added to numerator and denominator. Bonferroni intervals and detectable effects at α/3 were computed from the reported standard errors. Planned baseline: unweighted mean of the event-study coefficients over 2017–2022 (C1) or 2019–2022 (C2, C3), not a model estimate. Slope change: change in the slope of the deseasonalised log ratio, with Newey–West intervals; pre-2023 slopes were 0.7% (C1), −6.7% (C2) and 3.5% (C3) a year. Trend-adjusted: departure from the extrapolated pre-2023 relative trend, a sensitivity analysis only. Theory pairs: hep-th / hep-ph 1.02, hep-th / gr-qc 0.87, hep-th / nucl-th 0.91, hep-ph / gr-qc 0.85, hep-ph / nucl-th 0.89, gr-qc / nucl-th 1.06. Variants of C1 (2022 base; placebo p): theory without gr-qc 1.10 (0.96–1.25; 0.70), and 1.03 (0.91–1.16) on the 2017–2019 base; hep-ph / hep-ex 0.97 (0.86–1.10; 0.86); hep-th / hep-ex 0.99 (0.87–1.14; 0.95); gr-qc / experiment 1.27 (1.10–1.46; 0.40). All estimates are in S5 Table.
<!--/TABLE-->

<!--LEGEND-->
**Fig 2. Within-field contrasts.** (A–C) Quarterly new preprints, 2022 = 100, for groups within a field that differ in how much of the work is experimental. (A) arXiv physics, by primary archive: theory (hep-th, hep-ph, gr-qc, nucl-th) and experiment (hep-ex, nucl-ex); the experimental series is small (about 430 papers a quarter in 2026). (B) bioRxiv version-1 preprints: computational (bioinformatics, systems biology, genomics), wet lab (twelve categories; Methods) and all other categories; COVID-19 preprints are included. (C) medRxiv, excluding COVID-19: preprints whose title or abstract names a public dataset or design that recurs in formulaic papers (NHANES, UK Biobank, Global Burden of Disease, Mendelian randomisation, FAERS, MIMIC, SEER, BRFSS) and all other preprints. (D) Rate ratio of group A to group B in each year relative to 2022 (theory / experiment, computational / wet lab, public dataset / other), from a Poisson pseudo-maximum-likelihood model with month fixed effects and group-specific calendar-month effects; bars are 95% Driscoll–Kraay confidence intervals, which omit year-level and between-category variation; logarithmic scale; 2026*, January–September. Dashed vertical lines in A–C as in Fig 1. The code that drew this figure was written with an AI assistant (Claude, Anthropic, via Claude Code) under the author's direction; data and code are in S1 Data.
<!--/LEGEND-->

The physics contrast is inconclusive rather than null. Its interval touches 1, the test could detect only rate ratios of about 1.21 or more, and the two experimental archives diverged from each other (hep-ex / nucl-ex 1.39) more than theory diverged from experiment. The estimate rests on nucl-ex, whose January–September count barely changed in a decade (323 papers in 2016, 346 in 2026): without it the ratio is 1.03, and within particle physics experiment grew as much as theory (hep-ph / hep-ex 0.97; 0.86–1.10; placebo p = 0.86). Against 2017–2019 the contrast is 1.11 (0.97–1.26), and it shows no acceleration (Table 1; no break, p = 0.56). Part of what remains comes from gr-qc, whose growth relative to experiment predates 2023 (4.0% a year): without gr-qc the contrast is 1.10 relative to 2022 and 1.03 (0.91–1.16) relative to 2017–2019 (placebo p = 0.70).

The biology contrast is fragile in level and ambiguous as acceleration. It equals its own minimum detectable effect, one in five halvings of the wet-lab categories diverged as much, and it rests on bioinformatics, 63% of the computational group: without bioinformatics it is 0.93, as genomics and systems biology grew more slowly in 2026 (7% and 5%) than the wet-lab categories (8%). It is 0.87 against 2019 and 0.99 (0.80–1.22) against 2019 and 2022 pooled. As acceleration, however, it moved: the slope of its log ratio rose by 10.8% a year after December 2022 (5.2% to 16.7%; bootstrap p = 0.024), from −6.7% a year before, and 2026 exceeded 2025 by 10% (1.10; 1.06–1.15). Computational categories, which had been losing share as wet-lab fields adopted bioRxiv, regained it. But the ratio's strongest break is in July 2020 (p = 0.013), within the adoption period, so the end of adoption and any effect of AI cannot be separated, and in 2026 the movement was mainly a wet-lab slowdown (from 13% growth in 2025 to 8%) while computational growth held at 20% and 18% [ANALYSIS PENDING: bioinformatics split by AI/ML topic] [ANALYSIS PENDING: bioRxiv categories without COVID-19 preprints].

The medicine contrast is null under every base (0.99, 0.89–1.09, against 2019 and 2022 pooled) and excludes level increases of more than about 10%; its 2026/2025 ratio (1.08; 1.01–1.14) reflects a dip in 2025. Without COVID-19 preprints, those naming a listed dataset grew 2.47-fold from January–September 2022 to the same months of 2026 and others 2.51-fold (1.91-fold and 1.88-fold since 2023), and a title-only COVID-19 filter leaves recent growth unchanged (22.2% and 21.3% from 2025 to 2026). C3 is a weak test of H1, however: the flag records a mention, not a design, and the comparison group is itself largely secondary-data research [ANALYSIS PENDING: medRxiv flags (validation of the regular expressions; extended dataset list)].

### Distribution of output among authors (H2)

In theoretical physics, output grew in every class of authors in 2026, fastest at the top (Fig 3). Ranked on their combined output in the third quarters of 2025 and 2026, the top 1% of authors increased their fractional output by 44%, the next 9% by 37% and the bottom 90% by 21% (26% overall), and the bottom 90% contributed 54% of the increase; in earlier pairs of years, the bottom 90% had grown by between −0.7% and 8.1%. The namesake-robust variant gave 50%, 33% and 20%. The top 1%'s share of fractional output rose from 5.86% to 6.52%, 0.82 percentage points above its 2019–2022 trend (0.53–1.10; namesake-robust 0.73), while the top 10%'s share stayed at trend (−0.30; −1.11 to 0.50). Growth in theoretical physics was therefore broad-based but concentrating. Whether the authors behind it were established before 2023 cannot be judged from name strings, and small-team experimental papers were too few for these measures to be informative.

<!--LEGEND-->
**Fig 3. Concentration of output among authors in theoretical physics.** arXiv hep-th, hep-ph, gr-qc and nucl-th (primary category), papers with at most 50 authors; authors are matched by name strings, because arXiv has no author identifiers. (A) Share of fractional output (each paper divided equally among its authors) produced by the top 1% of active authors in each quarter. (B) Share of papers with at least one author who has five or more papers in the group that quarter, a fixed-threshold measure that rises mechanically with volume. Solid lines, all author names; dashed lines, namesake-robust (full first names only, with the 1% most frequent surnames removed). (C) Growth in fractional output between the third quarters (July–September) of consecutive years, by author class. Authors are ranked by their combined output in the two years compared (top 1%, next 9%, bottom 90%; ties at a class boundary are shared), which avoids regression to the mean. Black bars, all authors; under proportional growth, every class would grow at the black-bar rate. The grey background marks pairs that end before ChatGPT's release, which show how far the classes diverge by chance. The dashed vertical line in A and B marks the release of ChatGPT. Panels for mathematics will be added [ANALYSIS PENDING: maths H2]. The code that drew this figure was written with an AI assistant (Claude, Anthropic, via Claude Code) under the author's direction; data and code are in S1 Data.
<!--/LEGEND-->

For mathematics, the decomposition is pending [ANALYSIS PENDING: maths H2]. The share of papers with an author name posting five or more mathematics papers in a quarter rose from 5.3% in the third quarter of 2025 to 18.1% a year later (1.8% to 5.9% namesake-robust; S3 Table), but this share rises mechanically with volume and with shared names, and arXiv's endorsement rule of December 2025, by restricting newcomers, would raise it too. As a cross-section, papers without such an author grew by 56%, two-thirds of the 8,716 additional papers, while distinct author names rose by 41% and fractional output per name by 28%.

### AI-assisted writing (H3)

AI-associated style words rose in every group, experimental groups included (Fig 4; Table 2). In 2024, the year from which the word list was built, marker rates were 2.56 times their 2019–2022 level in computational bioRxiv categories, 2.15 in wet-lab categories, 2.17 in arXiv theory, 2.13 in arXiv experiment and 2.73 on medRxiv. Within fields the rise did not differ detectably in 2024 (computational against wet lab 1.18, 0.98–1.42; theory against experiment 1.00, 0.81–1.22); in 2025 and 2026, when rates are weak lower bounds, experimental physics rose more than theory (theory against experiment 0.75 in both years; 0.61–0.91 and 0.60–0.95). Computational categories started higher (38.6 against 27.7 words per 100 abstracts), as Kobak et al. found for computational fields [@Kobak2025], but rose by a similar factor. No equivalence margin was set in advance [@Lakens2017], so "similar" means no detectable difference: the 2024 intervals allow differences of about 20% in physics and 40% in biology.

<!--LEGEND-->
**Fig 4. AI-associated style words by group.** Core marker words per 100 abstracts, relative to each group's 2019–2022 mean. The core words are the 261 style words of Kobak et al. [@Kobak2025] that appeared in fewer than 0.5% of bioRxiv and medRxiv abstracts in 2019–2022. bioRxiv: version-1 preprints posted in March and September of each year; medRxiv: all version-1 preprints; arXiv: papers with primary category in the physics theory or experiment archives; bioRxiv and medRxiv exclude COVID-19 preprints; 2026*, January–September (bioRxiv, March and September). The list was built from 2024 text, and its fall after 2024 reflects, at least in part, newer models and authors avoiding words now read as signs of LLM text; values after 2024 are therefore lower bounds on LLM-assisted writing. The markers date changes in style; they do not identify causes. Mathematics will be added [ANALYSIS PENDING: maths H3 markers]. The code that drew this figure was written with an AI assistant (Claude, Anthropic, via Claude Code) under the author's direction; data and code are in S1 Data.
<!--/LEGEND-->

<!--TABLE-->
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

Marker rate: distinct core marker words per 100 titles and abstracts (Methods); rises are relative to the group's 2019–2022 mean. Ratios of rises: ordinary least squares on monthly log ratios relative to 2019–2022, with t intervals; comparisons involving bioRxiv use the 16 sampled months (March and September). Marker words drifted after 2024, and differently by corpus, so 2024 is the year for comparisons. ᵃ Share of abstracts with at least one core word in 2019–2022; the lower bounds use a counterfactual extrapolated from the 2019–2022 trend.
<!--/TABLE-->

The marker rise did not predict output growth. Across 27 bioRxiv categories and arXiv archives in 2023–2026, growth was unrelated to the change in marker rate (coefficient 0.0005; −0.0016 to 0.0026), and the interaction with experimental work was positive (0.0037; 0.0000 to 0.0073; p = 0.049), opposite to the sign H1 predicted; within bioRxiv it was 0.0011 (−0.0023 to 0.0045) [ANALYSIS PENDING: maths H3 markers]. Within arXiv physics, the second clause of H1 is not supported: experimental groups showed at least as large a rise in markers as theory and, in hep-ex, as large a departure of output from trend (below).

### Departures from trend and the comparison between servers (exploratory)

Against their own 2015–2022 trends, arXiv physics and mathematics accelerated in 2025–2026, while bioRxiv and PubMed did not (Table 3). In 2026, 14 of the 18 arXiv archives stood at least 1.25 times their trends, among them experimental particle physics (hep-ex 1.37; 1.12–1.67); the exceptions were nucl-ex (1.00), q-fin (1.03), physics (1.06) and cs (1.15), whose trend was 21% a year. arXiv's quantitative-biology archive stood at 1.26 although its count fell by 7% from 2025. Counted as list entries, which include cross-lists, the departures are smaller (physics 1.24, 1.17–1.32; mathematics 1.43, 1.24–1.66; computer science 1.06, 0.88–1.27), and mathematics ranks second of the 18 archives, behind math-ph (rank p = 0.11), against fifth on new submissions (p = 0.28).

<!--TABLE-->
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

Ratio of observed to trend-expected counts (95% CI), from Poisson pseudo-maximum-likelihood models with a linear trend, calendar-month effects and an indicator for April 2020 to March 2021, fitted to pre-2023 data from 2015 (arXiv), 2018 (bioRxiv) or 2019 (medRxiv, social sciences); Newey–West intervals. The counterfactual is each series' own extrapolated trend, not a level shared across series. New submissions; for list entries, see the text. ᵃ Trend dominated by the adoption of a new server; not interpreted. Archives, 2026: math-ph 1.81, nucl-th 1.58, quant-ph 1.54, nlin 1.52, math 1.48, hep-lat 1.39, hep-ex 1.37, astro-ph 1.34, stat 1.33, cond-mat 1.30, hep-ph 1.28, hep-th 1.28, gr-qc 1.26, q-bio 1.26, cs 1.15, physics 1.06, q-fin 1.03, nucl-ex 1.00; the largest departures are in archives whose pre-2023 trend was falling (math-ph −4.3%, nucl-th −2.5% and nlin −1.1% a year).
<!--/TABLE-->

These departures compare each series with its own extrapolated trend, and bioRxiv's trend of 12% a year was fitted to years in which the server was still being adopted; in levels, bioRxiv grew more than the physics archives tested. What is specific to arXiv is the acceleration in 2026: relative to bioRxiv, the six physics archives gained 7% from 2025 to 2026 (1.07; 0.99–1.16), theory 8% (1.08; 0.99–1.17) and experiment 2% (1.02; 0.93–1.11), although the marker rise in 2024 was similar on the two servers (arXiv physics against bioRxiv 0.89; 0.77–1.03; experiment 1.02; 0.61–1.71). Output did not follow measured AI-assisted writing on either server.

Break tests able to place a break as late as January 2026 put the largest change in the slope of the physics series in May 2025 (p = 0.001), and those of the six particle and nuclear physics archives and of mathematics at January 2026, the last admissible month, so the true dates may be later; computer science, bioRxiv and the physics contrast showed no slope break (p = 0.34, 0.17 and 0.56). The arXiv acceleration is therefore mainly a phenomenon of 2025–2026, not of the months after ChatGPT's release. The synthetic control replicated Nee et al.'s figure for mathematics [@Nee2026], 11.9% above the counterfactual in January–September 2026 (rank p = 0.05, the minimum attainable), but not like for like: theirs is for January–August on list entries, and our monthly gap was near zero until April and 0.31 and 0.40 log points in August and September, so that without September the excess is about 8%. It measures mathematics' excess over an accelerating arXiv, not an effect of AI.

PubMed journal articles with a US affiliation fell relative to the rest from 2025 (0.94, 0.92–0.96, in 2025 and 0.91, 0.89–0.93, in 2026, against 2023–2024), after no comparable decline in 2019–2022; the US share fell from 19.6% to 18.2% between the third quarters of 2024 and 2026. This US-specific slowdown, coinciding with the 2025 disruption of US research funding, accounts for about 1.7 of the roughly 7 percentage points by which PubMed fell below its trend in 2026 [ANALYSIS PENDING: US vs non-US split on bioRxiv].

### Small-team papers in experimental particle physics (exploratory)

One further observation, made after the tests above, motivated the pre-registered tests. INSPIRE-HEP queries made during internal review (16 October 2026; S2 Appendix) found that hep-ex records with at most 10 authors and no collaboration nearly doubled from January–September 2024 to the same months of 2026 (187 to 366), accounting for 185 of the 205 records added since 2022, while papers with more than 300 authors rose by 4%. Of 60 such 2026 records that were not conference papers, sampled at random and classified from titles and abstracts by one unblinded coder, an AI agent in a reviewer role, one reported new measurements; most were simulation or future-facility studies (18) or machine-learning and AI methods (17). The growth of hep-ex may thus lie mostly in papers that need no new data, but these counts are unvalidated [ANALYSIS PENDING: INSPIRE] and only motivate the tests [ANALYSIS PENDING: pre-registered test].

## Discussion

### Principal findings

None of the three pre-specified within-field contrasts supported H1: physics was inconclusive and typical of arbitrary pairs of arXiv archives, biology fragile in level, with an acceleration inseparable from the end of bioRxiv's adoption by wet-lab fields, and medicine null. AI-associated style words rose by similar factors in experimental and non-experimental groups, on arXiv and bioRxiv, and did not predict output growth. Against their own pre-2023 trends, nearly all arXiv archives, experimental ones included, accelerated in 2025–2026 while bioRxiv and PubMed did not, although in levels bioRxiv grew more than the physics archives tested. In theoretical physics, growth was broad-based but concentrating.

### What the within-field tests show

The contrasts were meant to hold preprint culture, platform and incentives fixed while varying the cost of the work beyond writing, but they also vary archive identity, collaboration structure and topic, and each depends on one component. Archive and category labels are weak proxies for experimental work: hep-ph is phenomenology fitted to data, gr-qc includes gravitational-wave experiments, genomics includes bench sequencing, arXiv keeps instrumentation and analysis methods out of hep-ex [@arXivTaxonomy], and much of hep-ex analyses data already collected. The tests therefore do not support the label-based version of H1, but they do not test the idea behind it, that the need for new data limits how far AI can raise output, which needs paper-level measures [ANALYSIS PENDING: pre-registered test]. They also bear on the account in which computationally intensive fields benefit more [@Qi2025]: within fields, computational intensity did not predict where output grew, which suggests that differences between fields partly reflect servers and their author populations. Nee et al.'s mathematics result [@Nee2026] replicates, but as an excess over an accelerating arXiv concentrated in a few months; their author panel shows a thicker tail of repeat producers, as the decomposition here does for theoretical physics [ANALYSIS PENDING: maths H2].

### Why might arXiv differ from bioRxiv?

The acceleration of arXiv against its own trend, absent on bioRxiv and in PubMed, is exploratory and confounds field with platform, the limitation that motivated the within-field design. Six explanations remain open, each with a pending check. (i) arXiv dates papers by announcement [@arXivAvailability], and before the October 2026 cap moderators held some submissions of heavy submitters, which could spill into later months [@arXiv2026] [RECHECK: against the arXiv post of 1 October 2026]; this could explain the September 2026 spike in mathematics but not, alone, the physics break of May 2025 [ANALYSIS PENDING: dating by first-version submission]. (ii) arXiv accepts proceedings, reviews outside computer science, lecture notes, comments and white papers, genres that may gain most from cheaper writing and that bioRxiv and medRxiv are not intended for [@bioRxivFAQ; @medRxivAbout] [ANALYSIS PENDING: genre decomposition]. (iii) Snowmass 2021 white papers inflate the 2022 base of the experimental archives, and inputs to the European Strategy for Particle Physics were due in March 2025 (S2 Appendix) [ANALYSIS PENDING: Snowmass and European Strategy papers removed]. (iv) The 2025 disruption of US research funding (S2 Appendix) explains only part of PubMed's shortfall and, on bioRxiv, would depress US wet-lab output first, as in the 2026 wet-lab slowdown [ANALYSIS PENDING: US vs non-US split on bioRxiv]. (v) Facility cycles move experimental output: LHC Run 3 was scheduled to end in mid-2026, RHIC's final run ended in February 2026 and the LIGO–Virgo–KAGRA O4 run in November 2025 (S2 Appendix) [ANALYSIS PENDING: INSPIRE]. (vi) AI may have raised production across arXiv fields, including the analysis, simulation and methods work of experimentalists, more than in the fields that post on bioRxiv; the small-team growth in hep-ex fits this reading but was observed after the fact, and the pre-registered tests examine it where it was not formed [ANALYSIS PENDING: pre-registered test]. Changes in who posts to arXiv, as AI lowers language barriers, and in the propensity to post work published elsewhere were not examined; arXiv's endorsement and language rules restrict entry and would slow growth rather than add papers. The design cannot choose among these explanations; it shows only that measured AI-assisted writing does not explain them.

### Implications for research evaluation

Two findings bear on research evaluation, whatever caused the growth. First, AI-assisted writing is present in every group examined, experimental work included: by 2024 its marker words had roughly doubled or tripled in theoretical and experimental physics, computational and wet-lab biology and medicine, and at least 6% of experimental and 11% of theoretical physics abstracts on arXiv were processed with LLMs. If fluent text can be produced cheaply by anyone, its quality no longer indicates the effort behind a paper. This is an interpretation, consistent with the reversed association between writing complexity and paper quality [@Kusumegi2025], not a result of this study.

Second, preprint counts moved unevenly across servers in 2025–2026, by amounts that depend on the counterfactual and for reasons not yet attributable. Against their own trends, arXiv physics and mathematics stood about a third and a half higher in 2026 while bioRxiv and PubMed did not, and in theoretical physics the distribution of output among authors shifted at the same time. This supports, at the strength the data allow, the view that evaluation built on counts is not prepared for widespread use of AI [@CompanionEssay]: counts can no longer be compared across fields or over time as before, and measured adoption of AI for writing cannot be used to adjust them. Whether a falling cost of producing papers, rather than more research, drives the change would need measures of research inputs or of the work behind each paper.

Several institutions have responded by rationing: in 2025–2026, funders, preprint servers and conferences introduced per-person limits on submissions, from NIH's six applications per investigator a year [@NIH2025] to arXiv's two submissions per submitter a month [@arXiv2026] (S1 Table). Such caps limit volume; whether they preserve information about the work behind each item has not been evaluated. Reforms of what is counted predate generative AI [@DORA; @CoARA2022] but remain largely unimplemented where measured, and mostly unmeasured: in measurements that predate the CoARA agreement, the Journal Impact Factor appeared in the promotion and tenure documents of 40% of research-intensive universities in the United States and Canada [@McKiernan2019] and peer-reviewed publications were a criterion in 95% of the promotion guidelines of 92 biomedical faculties [@Rice2020], and a 2026 study for the European Commission found engagement broad and growing but progress uneven [@EC2026] [RECHECK: figures of McKiernan et al., Rice et al. and the Commission's study]. These reforms also assume that evaluators can read what they assess; whether the growth in volume strains that capacity was not examined.

The literature offers proposals that these data do not test, none with strong evidence of effect, so each would best be introduced as an evaluated experiment [@NielsenQiu2022]: count fewer, self-selected outputs and read them, moving the cap from those who submit to those who count [@CoARA2022; @Frith2020; @Moed2008]; make effort visible for the outputs that count, through records of how they were made [@Cwik2026; @Hosseini2026]; pay for verification and count it [@Hansen2026; @Cotton2025]; reward exploration directly [@Huang2026; @Azoulay2011]; build public infrastructure for data and open models [@Huang2026; @Palmer2024]; record the model family in AI-use statements, so that the concentration of tools can be measured [@Suchikova2025; @Kleinberg2021]; and treat submission caps as experiments, with sunset dates and published data [@NielsenQiu2022]. [AUTHOR: merge your own recommendations, or confirm this shortlist (S1–S7 of research note 7).]

### Limitations

The design is observational and has no measure of exposure to AI: the treatment is the calendar year, which bundles AI capabilities with platform rules and moderation, funding, facility cycles and server-specific dynamics, and within-field differencing removes only shocks that hit both groups in proportion. The contrasts were chosen after descriptive growth had been seen, two failed and the third is fragile, and the reference year departed from the plan. The physics test could not detect effects below about 1.21, every contrast depends on one archive or category, and the placebos are not yet matched to each contrast's structure. Archive sums double-count aliased papers, arXiv dates papers by announcement, bioRxiv categories are chosen by authors and include COVID-19 preprints, the regular expressions are unvalidated, the social-science series could not be checked across its change of method, and journal-side changes, such as a pre-screen for Mendelian randomisation studies at PLOS ONE from April 2024 [@Pruller2025], can move PubMed and medRxiv series. Marker words measure style, not purpose, come from PubMed, drift as authors and models avoid them [@GengTrotta2025] and may share the bias of AI detectors against non-native English writers [@Liang2023]. Author-level measures rest on name strings and short histories and cover arXiv only, so this study cannot reconcile the output gains of individual LLM adopters on bioRxiv [@Kusumegi2025] with bioRxiv's flat departure from trend; the gains may be overestimated [@Renault2026], confined to few authors or published elsewhere. Preprints are not publications, and bioRxiv and medRxiv exclude genres that arXiv accepts.

Whether experimental work will show the effect later cannot be tested with these data, but the idea can be stated as a prediction. If a fraction *f* of the effort behind a paper can be compressed by a factor *s*, output per unit of effort can rise at most by a factor of 1/[(1 − *f*) + *f*/*s*]: by 8% for *f* = 0.15 and *s* = 2, and by 54% for *f* = 0.7 and *s* = 2. Gains should then be larger for types of paper with a larger compressible share, which the pre-registered tests examine, and lags from data to paper should shorten in experimental work even where counts are flat. Finally, the article and all its code were produced with AI assistance under my direction (Methods); independent checks agree with the counts where available (bioRxiv's official totals; arXiv's statistics for hep-th and hep-ph), but not for every series.

## Conclusions

Pre-specified within-field tests did not show that preprint output in the generative-AI era grew faster in non-experimental than in experimental work: the physics contrast was inconclusive, the biology contrast fragile and the medicine contrast null. AI-associated style words rose in experimental and non-experimental groups alike and did not predict output. Against their own pre-2023 trends, arXiv physics and mathematics, experimental archives included, accelerated in 2025–2026 while bioRxiv and PubMed did not; in theoretical physics, the growth was broad-based but concentrating. These data cannot attribute the changes to generative AI, but they show that preprint counts from 2026 cannot be compared with those of earlier years, or across servers, as before.

## Acknowledgments

[AUTHOR: acknowledgements, e.g. anyone who read the draft or checked the code.] This work used arXiv's open-access interoperability and data from the US National Library of Medicine, bioRxiv, medRxiv and the Open Science Framework; none of them endorses it.

## References

<!--REFERENCES-->

## Supporting information

**S1 Appendix. AI use and verification record.** For each task, the tool, the author's role, how the output was checked and its status; the code-review and re-run log; the reading depth for the references of this article; time and cost; and the archived project history.

**S2 Appendix. Definitions, regular expressions, queries and dated events.** Archives and categories in each group; normalisation of author names and the namesake-robust variant; the regular expressions; the core marker words; the INSPIRE-HEP queries behind the exploratory observation in hep-ex; and a dated timeline of server policies, facility schedules, planning exercises and funding events, with sources.

**S1 Text. Pre-registration of the paper-level tests.** The plan (commit 763aa2b) and its amendment 1 (commit 78890e5), with the codebooks and classifier prompts, as activated on 16 October 2026, and the two deviations recorded later that day (commits 11264ee and 1de63a9).

**S1 Table. Per-person limits on submissions, 2025–2026.** Caps, gates and quotas introduced by funders, preprint servers, journals and conferences, with their stated reasons and primary sources.

**S2 Table. Growth by arXiv archive and by bioRxiv and medRxiv category.** January–September counts and year-on-year growth, 2017–2026 (bioRxiv and medRxiv from 2019), with 2017–2025 ranges, the yearly change in the log ratio of each contrasted pair, and COVID-19 and public-dataset shares. <!-- To be assembled from the companion files (data/raw/arxiv_archive_monthly.csv, biorxiv_category_monthly.csv, medrxiv_category_monthly.csv) with the deposit. -->

**S3 Table. Descriptive heavy-producer measures.** arXiv mathematics, third quarters of 2025 and 2026, and arXiv physics theory and experiment, 2022–2026, under each author-matching rule; cells describing fewer than ten authors are suppressed.

**S4 Table. Published estimates of LLM-assisted writing by field.** Context for H3; the measures differ, so only rankings within a study are comparable.

**S5 Table. All estimates.** Event-study coefficients by year and base, acceleration and slope-change estimates, placebo distributions, negative controls, leave-one-out and sensitivity analyses, placebo dates, break tests, field and archive departures from trend (new submissions and list entries), the synthetic control, the PubMed funding check, the marker tests and the category panel, and the analyses tried and dropped, with reasons (companion files within_field_tests.json, round1_tests.json, field_tests.json, heavy_producers.json, marker_tests.json and marker_growth_panel.csv).

**S1 Data. Data and code.** The deposit described under Data availability (Zenodo, doi:[AUTHOR: DOI]).

<!-- SUBMISSION FORM START -->

## Statements for the submission form (not part of the manuscript file)

<!-- PLOS ONE collects these in its submission system, not in the manuscript file (R4, minor 2). Kept here so that the author can review them with the article. -->

### Funding

[AUTHOR: e.g. "The author received no specific funding for this work." State who paid for the AI tool subscription or API use. The article-processing charge falls under EMBL's flat-fee agreement with PLOS; confirm whether it needs mentioning.]

### Competing interests

I have no financial relationship with Anthropic or any other developer of AI tools [AUTHOR: confirm; state who paid for the Claude subscription or API use, and whether any credits were received from Anthropic]. I used Anthropic's Claude, via Claude Code, to draft this article and to write its analysis code (Methods, Use of AI tools). Because the article studies changes in scientific output in the period in which such tools became available, I declare this use as a potential non-financial competing interest. Anthropic had no role in the study design, data collection and analysis, decision to publish or preparation of the manuscript, beyond the use of its commercially available product. [AUTHOR: align this declaration with the Zenodo essay and any Correspondence, which discuss Anthropic's data policy.]

### Data availability

All data and code are available from Zenodo (doi:[AUTHOR: DOI of the tagged release]). The deposit is a tagged release of the project repository. It contains monthly counts of new preprints by arXiv archive (new submissions and list entries, 2010–2026), by bioRxiv subject category and for medRxiv (2019–2026), with retrieval dates; PubMed quarterly counts, in total and with a US affiliation; aggregate text features and marker-word counts by group and month, with the core word list; the values behind every figure and table and the JSON output of every model; and the scripts that harvest, process and analyse the data, which reproduce every figure and estimate from the committed data with fixed random seeds. Record-level tables of identifiers with derived variables (arXiv identifiers or bioRxiv and medRxiv DOIs, dates, primary category, number of authors, and the COVID-19, public-dataset and keyword flags) will be added [ANALYSIS PENDING: record-level identifier and flag tables for the deposit]. No titles, abstracts or author names are redistributed. A pseudonymised author–paper table for the heavy-producer analyses is not yet deposited [AUTHOR: deposit it after the data-protection consultation, or state why it is withheld and name a non-author contact for access]. Source metadata are public (arXiv statistics pages and OAI-PMH, under CC0; the bioRxiv and medRxiv API; the OSF API; PubMed E-utilities) and were retrieved on 15–16 October 2026; earlier retrievals from arXiv's statistics pages and the OSF API ran faster than those sources' stated limits, and the deposited scripts follow them. Licences: CC BY 4.0 for the data and MIT for the code [AUTHOR: confirm]; the word list of Kobak et al. keeps its MIT licence.

### Author contributions (CRediT)

[AUTHOR: full name]: Conceptualization; Methodology (adoption and modification of AI-proposed designs) [AUTHOR: confirm]; Investigation (direction and verification of the literature search and the companion analysis); Formal analysis (direction and review of AI-written code) [AUTHOR: confirm]; Validation [AUTHOR: confirm]; Visualization (direction); Writing – review & editing; Project administration. AI tools are not contributors under CRediT; their use is described in Methods.

<!-- SUBMISSION FORM END -->

<!-- SI FILES START -->

<!-- SI FILE: S1 Appendix -->

## S1 Appendix. AI use and verification record

*A separate Supporting Information file at submission. It covers this article and its companion analysis only. Times are UTC, from the project repository. Items marked [AUTHOR] must be completed by the author.*

**Timeline.**

- 16 October 2026, 16:42: skeleton with hypotheses H1–H3 and the three contrasts committed (2cac071), after the groups' descriptive growth had been computed.
- 17:27: v1, with the analysis plan drafted by an AI agent, committed (697fb25).
- 17:45, 18:08, 18:19 and 18:47: formal results of the companion analysis added to the repository (companion commits 37b4b11, f5ab16e, 7ac5647 and 26ce2eb).
- 18:00–18:15: four internal reviews written by AI agents in reviewer roles (statistics, scientometrics, experimental science, journal editor); they are not peer review.
- 18:28 and 18:47: pre-registration of the paper-level tests and its amendment 1, approved by the author, committed (763aa2b and 78890e5); 18:48 and 18:55: deviations 1 (classification and estimation before the author's validation coding, at the author's request) and 2 (stratified samples; one classification per paper) recorded (11264ee and 1de63a9).
- [AUTHOR: time and commit of this v2; the companion analysis's own timeline.]

**Tasks.**

| Task | Done by | Author's role | How the output was checked | Status |
|---|---|---|---|---|
| Literature search; reference checks | AI agents | Directed [AUTHOR: confirm] | Identifiers and metadata of added references read from Crossref and arXiv by AI agents | Each source cited for a number, quotation or method to be read by the author [AUTHOR] |
| Hypotheses | Author (H1; refined hypothesis of the pre-registered tests); AI agents (wording; H2, H3) [AUTHOR: confirm] | Originated or adopted | Recorded before modelling (commit 2cac071) | Done |
| Group definitions; analysis plan; statistical specification | AI agents | Adopted or modified [AUTHOR: specify] | Deviations listed in Methods | Done |
| Harvesting, processing, statistics and figure code | AI agents, in a separate session | Directed [AUTHOR: code review] | Independent agreement with bioRxiv's official totals and arXiv's statistics for hep-th and hep-ph; [AUTHOR: own re-runs] | Pipeline reproduces all outputs from committed data |
| Country classifier for the bioRxiv funding check | AI agents | – | 150 classified records checked by an AI agent, not by a person | Analysis pending |
| Drafting and revision of the text (v1, v2) | AI agents | Decisions recorded in the project brief; [AUTHOR: own revision] | [AUTHOR] | In progress |
| Internal reviews (four roles) | AI agents | Read the reviews and decided the responses | Not peer review | Round 1 done |
| INSPIRE-HEP queries and sample classification (hep-ex) | AI agent in a reviewer role | – | Not validated; to be reproduced | Pending |
| Classifier of the pre-registered tests | LLM with fixed prompts | Approved the plan and deviations; blind coding of 400 papers | Cohen's κ ≥ 0.60 per domain, coded by the author; classification precedes coding (deviation 1) | No results reported |

**Code review and re-runs.** [AUTHOR: what you reviewed, with commit hashes.]

**Reading depth.** [AUTHOR: for each reference cited for a number, a quotation or a method, how it was read (in full, as a primary document, abstract only).]

**Time and cost.** [AUTHOR: compute cost of this article and its companion analysis; your own hours by phase.]

**Tool and account.** Claude (Anthropic), via Claude Code [AUTHOR: model and version], on a [AUTHOR: account type] account with model training [AUTHOR: on/off]. [AUTHOR: why a proprietary model was used.]

**Archive.** The repository history, with the commits above, will be archived on Zenodo with the data (doi:[AUTHOR]) after a check for personal data, third-party text and files the author does not want public.

<!-- SI FILE: S2 Appendix -->

## S2 Appendix. Definitions, regular expressions, queries and dated events

*A separate Supporting Information file at submission.*

**Physics.** The physics field series sums 13 arXiv archives: astro-ph, cond-mat, gr-qc, hep-ex, hep-lat, hep-ph, hep-th, math-ph, nlin, nucl-ex, nucl-th, physics and quant-ph. The physics archive includes physics.ins-det (instrumentation and detectors) and physics.data-an (data analysis). Contrast C1: theory = hep-th, hep-ph, gr-qc and nucl-th; experiment = hep-ex and nucl-ex; the other archives, including hep-lat, are in neither group. The aliased pairs are math-ph/math.MP, cs.IT/math.IT, cs.NA/math.NA, math.ST/stat.TH, eess.SY/cs.SY and econ.GN/q-fin.EC.

**bioRxiv.** Computational: bioinformatics, genomics, systems biology. Wet lab: biochemistry, cancer biology, cell biology, developmental biology, immunology, microbiology, molecular biology, pathology, pharmacology and toxicology, physiology, plant biology, synthetic biology. Mixed: animal behavior and cognition, bioengineering, biophysics, ecology, evolutionary biology, genetics, neuroscience, paleontology, scientific communication and education, zoology. Epidemiology and clinical trials, which moved to medRxiv in 2019, cannot be queried by category, so category sums are about 4% below bioRxiv's totals in January–June 2019 and equal to them from July 2019.

**medRxiv.** The public-dataset list shares FAERS, NHANES, UK Biobank, the Global Burden of Disease study and MIMIC with the nine datasets of Spick et al. [@Spick2026], and lacks FinnGen, CHARLS, CDC WONDER and TriNetX; it adds Mendelian randomisation, SEER and BRFSS. COVID-19 preprints were 66% of new medRxiv preprints in 2020 and 5% in 2026.

**Regular expressions** (Python, case-insensitive; a record is flagged if the pattern matches at least once in the fields named). Their precision has not yet been measured [ANALYSIS PENDING: medRxiv flags (validation of the regular expressions; extended dataset list)].

- *COVID-19 (medRxiv; title and abstract):* `covid|sars[\s-]*cov[\s-]*2|2019[\s-]*ncov|ncov[\s-]*2019|novel coronavirus|coronavirus disease 2019`. A title-only variant gives the same growth from 2025 to 2026 (22.2% and 21.3%).
- *Public datasets and designs (medRxiv; title and abstract):* `\bNHANES\b|national health and nutrition examination survey|uk[\s-]?biobank|global burden of disease|\bGBD\s?20\d\d\b|mendelian randomi[sz]ation|\bFAERS\b|adverse event reporting system|\bMIMIC-?(?:III|IV)\b|\bSEER\b|\bBRFSS\b`. "adverse event reporting system" also matches VAERS, and `\bSEER\b` matches the word "seer".
- *AI-related terms (arXiv mathematics; title, abstract and comments):* `\b(chat ?gpt|gpt-?\d(\.\d)?|o[134](-mini|-pro)?\b|openai|claude|anthropic|gemini|deepseek|grok|qwen|alphaproof|alphaevolve|alphageometry|large language models?|llms?|ai[- ]assisted|ai[- ]generated|generative ai|ai (tools?|assistants?|systems?|models?)|with the (help|assistance) of (an? )?ai)\b`. It matches AI as a topic as well as a tool, "claude" as a given name and bare model-like tokens, so it counts papers using AI-related terms, not papers using AI. It is used only in S3 Table.

**Author names.** Names are normalised by Unicode decomposition, removal of accents, conversion to lower case and tokenisation. The namesake-robust variant keeps only names whose first part is a full given name and drops names whose surname is among the 1% most frequent (in mathematics, 407 surnames holding 35.7% of author slots, mostly common East Asian surnames). In physics, papers with more than 50 authors are excluded; with them, white papers signed by hundreds of theorists would make 16.9% of active theory authors heavy producers in the third quarter of 2025, against 1.3% without them. Authors tied at a class boundary in the decomposition share the remaining places equally. Experimental physics, with about 300 papers a quarter of at most 50 authors and few full first names, is analysed with all names only.

**Marker words.** The source list is the 407 style words of Kobak et al. [@Kobak2025] (repository berenslab/llm-excess-vocab, file results/excess_words.csv, MIT licence). The 261 core words are those with a pooled 2019–2022 document frequency below 0.5% in the 41,270 bioRxiv and medRxiv abstracts of those years (S1 Data, core_marker_words.txt). Core words such as "delve", "intricate" and "underscores" peaked in 2024 and were back near baseline in 2026; in September 2026, "crucial" appeared in 1.7% of bioRxiv abstracts against 4.5% before 2023. For the lower bound on LLM-processed abstracts, with *p* the observed share of abstracts containing at least one core word and *q* its counterfactual extrapolated from the 2019–2022 trend, a fraction *f* of processed abstracts gives *p* = (1 − *f*)*q* + *fr* with *r* ≤ 1, so *f* ≥ (*p* − *q*)/(1 − *q*). The category panel codes experimental work as 1 (wet lab, experiment), 0 (computational, theory, mathematics) or 0.5 (mixed).

**Synthetic control and break tests.** Mathematics' deseasonalised monthly log series was approximated by a convex combination of the 19 other archives with monthly data since 2018; 14 received positive weight (astro-ph 0.11, cond-mat 0.13, cs 0.01, gr-qc 0.09, hep-ex 0.01, hep-ph 0.09, hep-th 0.12, math-ph 0.12, nucl-ex 0.03, nucl-th 0.06, physics 0.09, q-fin 0.02, quant-ph 0.05, stat 0.08). The fit used January 2018 to December 2025 after demeaning; the 2026 gap is the mean log difference over January–September 2026, expressed as a percentage; and each donor in turn served as a placebo, with units ranked by the ratio of post- to pre-period fit error, so that with 20 units the smallest attainable rank p value is 0.05. A fit with the pre-period ending in November 2022 gave a gap of 10.1%. math-ph shares aliased papers with mathematics. For breaks, sup-Wald statistics for a change in the slope or level of each deseasonalised log series (fields) or log ratio (contrasts) were computed for every candidate month in the central 90% of the sample, so that the last candidate for arXiv was January 2026, with Newey–West Wald statistics and p values from 999 parametric-bootstrap draws of the no-break model with first-order autoregressive errors; Wald tests at December 2022, November 2024 and November 2025 used the same bootstrap. The first tests, with 15% trimming, could not place a break after December 2024 (arXiv) or August 2025 (bioRxiv and medRxiv) and are not used.

**INSPIRE-HEP queries behind the exploratory observation in hep-ex.** Made on 16 October 2026 by an AI agent in a reviewer role through the INSPIRE-HEP literature API [@INSPIREAPI] (`https://inspirehep.net/api/literature?q=<query>&size=1`, field `hits.total`); to be reproduced [ANALYSIS PENDING: INSPIRE]. Base query: `primarch hep-ex and de YYYY-01-01->YYYY-09-30`. Added clauses: `ac > 300` (more than 300 authors); `ac 1->300 and collaboration:*`; `ac 1->10 and not collaboration:*` (at most 10 authors, no collaboration field); `ac 11->300 and not collaboration:*`; `tc c` (conference papers). The 60 records of January–September 2026 with at most 10 authors, no collaboration field and no conference tag were drawn at random with a fixed seed and classified from titles and abstracts by the same agent, alone and unblinded: 18 were simulation, sensitivity or future-facility studies, 17 machine-learning or AI methods, 7 statistical or analysis methods and software, 6 reviews or talk write-ups, 5 instrumentation papers, 4 reanalyses of existing data, 2 concept studies and 1 a report of new measurements. A keyword classification of all such records by the same agent gave similar shares in 2024 and 2026 (machine-learning or AI terms 26% in both years; simulation or future-facility terms 38% and 42%; review terms 8% in both). INSPIRE counts track arXiv's statistics for hep-ex to within 1–2% (717 against 713 in January–September 2022).

**Dated events** (sources as listed; checked on 16 October 2026 during internal review).

| Date | Event | Source |
|---|---|---|
| 15 Mar 2022 | Contributed papers for the US particle-physics planning exercise Snowmass 2021 due on arXiv | Snowmass Steering Group message of 9 Mar 2022, forwarded at https://mailman.jlab.org/pipermail/hps/2022-March/002209.html |
| 24 May 2023 – 18 Nov 2025 | LIGO–Virgo–KAGRA fourth observing run (O4) | https://ligo.org/ligo-virgo-kagra-collaboration-successfully-wraps-up-its-fourth-observing-run/ |
| 2024 | arXiv limits each submitter to three active submissions | [@arXiv2026] |
| 1 Jan 2025 | The Gates Foundation expects funded manuscripts to be shared as preprints | https://openaccess.gatesfoundation.org/open-access-policy/ |
| 28 Feb – 8 Apr 2025 | 694 NIH grants terminated (US$1.81 billion), per a JAMA research letter as reported by HPN Online, 9 May 2025 | https://www.hpnonline.com/regulatory/news/55289345/newly-published-study-quantifies-types-of-grants-terminated-by-nih-since-late-february |
| 31 Mar 2025 | Written input to the 2026 update of the European Strategy for Particle Physics due | CERN Courier, 19 Sep 2024, https://cerncourier.com/a/a-decider-for-cerns-next-collider/ |
| 26 Aug 2025 | Fourth gravitational-wave transient catalogue (GWTC-4.0) and O4a strain data released | https://www.ego-gw.it/blog/2025/08/26/gwtc-4-0-updated-gravitational-wave-catalog-released/ |
| 31 Oct 2025 | arXiv computer science accepts review and position papers only after peer review | [@arXiv2025a] |
| 28 Nov 2025 | 977 NIH grant awards terminated (US$1.7 billion); NIH made fewer awards in 2025 than its 2020–2024 average | Congressional Research Service, IF13131, 11 Dec 2025, https://www.everycrsreport.com/files/2025-12-11_IF13131_63aaed675c9924bb0867a577571eb87d3451439c.html |
| 10 Dec 2025; 21 Jan 2026 | arXiv tightens endorsement of new submitters (mathematics; all sections) | [@arXiv2025c] |
| 6 Feb 2026 | Final run of RHIC ends | Brookhaven National Laboratory, https://www.bnl.gov/newsroom/news.php?a=122794 |
| 11 Feb 2026 | arXiv requires a full English version of every submission | [@arXiv2025b] |
| 8 Mar 2026 (updated 28 Sep 2026) | SocArXiv: generally at most one paper per author per week | [@SocArXiv2026] |
| 22 May 2026 | CERN Council adopts the 2026 update of the European Strategy for Particle Physics | CERN/3997, https://council.web.cern.ch/sites/default/files/c-e-3997-Council%20Resolution%20on%20the%202026%20update%20of%20the%20European%20Strategy%20for%20Particle%20Physics.pdf |
| 1 Jul 2026 | arXiv becomes an independent nonprofit and completes a migration to cloud infrastructure | Cornell Chronicle, 29 Jun 2026, https://news.cornell.edu/node/333261 |
| Jul 2026 | LHC Long Shutdown 3 scheduled to begin, ending Run 3 | CERN, 4 Oct 2024, https://home.cern/updated-schedule-cerns-accelerators |
| Until Oct 2026 | arXiv rate-limits heavy submitters at moderators' discretion; held submissions can spill into the next month | [@arXiv2026] [RECHECK: against the post] |
| 1 Oct 2026 | arXiv caps submissions at two per submitter per month | [@arXiv2026] |
| 2025 | bioRxiv and medRxiv move to the openRxiv organisation; new DOI prefix 10.64898 | [RECHECK: source and date] |

### References for S2 Appendix

<!--SIREFS-->

<!-- SI FILE: S1 Table -->

## S1 Table. Per-person limits on submissions, 2025–2026

*A separate Supporting Information file at submission.* Caps, gates and quotas that restore scarcity by rule. Earlier limits existed (arXiv has limited each submitter to three active submissions since 2024); none of the measures listed predates 2025. "Cap" means a limit on how many items a person may submit, whatever the quality of the work or the conduct of its author.

| Effective | Institution | Type | Measure | What is limited | Stated reason | Source |
|---|---|---|---|---|---|---|
| 25 Sep 2025 | NIH (US) | Cap | At most 6 applications per principal investigator per calendar year (T activity codes and R13 excepted); applications "substantially developed by AI" not considered original | Grant applications | AI "enabled Principal Investigators to submit more than 40 distinct applications in a single application submission round"; the cap is expected to affect "a relatively small number of Principal Investigators" | [@NIH2025] |
| 31 Oct 2025 | arXiv, computer science | Gate | Review/survey and position papers only after acceptance at a peer-reviewed journal or conference (workshop review does not count) | Unrefereed reviews and position papers | "unmanageable influx"; "hundreds of review articles every month" | [@arXiv2025a]; one subfield could lose about half its papers [@ElazarAntoniak2026] |
| Mar 2026 (updated 28 Sep 2026) | SocArXiv | Cap | Generally at most 1 paper per author per week; no verbatim AI-generated paragraphs; no "superficial, high-level theory synthesis" | Submissions per author | AI-generated content | [@SocArXiv2026] |
| Jun 2026 | TMLR (journal) | Cap | Yearly per-author submission budget under the Generalized Harmonic Quota Rule (N₁ = 2, N₉ = 9), each submission costing according to its number of authors [@Shah2026]; doubled for reviewers and action editors; desk-rejected submissions count | Submissions | Submissions tripled in a year, including a 13-fold rise in single-author submissions | [@TMLR]; [@SinghChawla2026a] for the date and growth figures |
| 2027 cycle (announced 28 Jul 2026; papers due 25 Sep 2026) | ICLR 2027 | Cap, tiered by prior acceptance | At most 20 submissions per author; at most 1 paper on which no author has had a paper accepted at a major machine-learning conference or journal; excess submissions randomly desk-rejected; each submission must register an author with such an acceptance to review, unless no author has one | Submissions | "The rapid rate of growth in submissions, while exciting, has begun to strain the review system"; more than 62,000 submissions expected (490 a decade ago) | [@ICLR2027]; [@SinghChawla2026a] |
| 1 Oct 2026 | arXiv, all categories | Cap | At most 2 submissions per submitter per calendar month, and 3 active (the 3-active limit dates from 2024); rejected submissions count; described as a "stopgap" | Submissions | 40,363 submissions in Sep 2026 (20,569 in Sep 2024; 9,869 in Sep 2016) | [@arXiv2026] |
| ARR cycles from Oct 2026 | ACL Rolling Review (ACL venues) | Cap, plus a lottery | At most 20 submissions per author and 5 as first or joint first author per cycle; each submission must name a qualified reviewer or chair, and submissions without one enter a lottery for spare reviewing capacity | Submissions (reviewing capacity) | "unsustainable rate of submissions at EMNLP'26"; 38% of ~17,000 May 2026 submissions from authors with no available publication record | [@ACL2026]; [@SinghChawla2026a] |
| May 2027 conference | AISTATS 2027 | Cap, tiered by prior acceptance | At most 12 submissions per author; at most 3 for authors without an accepted paper at ICLR, ICML, NeurIPS or AISTATS; excess randomly desk-rejected | Submissions | "Peer review is the scarcest resource of a conference … generative AI tools now make it possible to produce far more manuscripts than the community can carefully evaluate" | [@AISTATS2027]; [@SinghChawla2026a] |

*Note.* Conduct rules from 2023–2024 (authorship and disclosure rules; the ban on generative AI in NIH peer review) are not rationing and are not listed [@Thorp2023; @Ganjavi2024; @NIH2023]. Not listed either: arXiv's changes to endorsement (from 10 December 2025 in mathematics and 21 January 2026 in all sections) [@arXiv2025c] and language (a full English version of every submission from 11 February 2026) [@arXiv2025b] [AUTHOR: list the endorsement rule as a gate?]; a one-year ban on submitting for authors who did not check LLM output, announced in May 2026 by the chair of arXiv's computer-science section but not on arXiv's policy pages; and thesis gates based on AI detectors at some Chinese universities, which are not per-person limits. Conference rows were checked against each venue's call or policy on 16 October 2026; TMLR's start date and growth figures rest on a news report. All rows are date-sensitive.

### References for S1 Table

<!--SIREFS-->

<!-- SI FILE: S3 Table -->

## S3 Table. Descriptive heavy-producer measures

*A separate Supporting Information file at submission. Fixed-threshold measures rise mechanically with volume and with namesake collisions (Methods); they describe, and do not test, how output is distributed. Statistics describing fewer than ten authors are suppressed.*

**(A) arXiv mathematics, third quarters of 2025 and 2026** (primary category math.\*, OAI-PMH metadata harvested on 15 October 2026; a prolific name has five or more mathematics papers in the quarter).

| Measure | Q3 2025 | Q3 2026 |
|---|---|---|
| New mathematics papers | 10,846 | 19,562 |
| Papers with a prolific name: all name strings | 5.3% | 18.1% |
| — full first names only | 5.2% | 18.0% |
| — full first names, 1% most frequent surnames removed | 1.8% | 5.9% |
| — full first names, 2% most frequent surnames removed | 1.2% | 4.3% |
| Papers with a prolific name (all name strings), n | 575 | 3,549 |
| Papers without a prolific name, n | 10,271 | 16,013 |
| Distinct author names | 20,108 | 28,279 |
| Names with five or more papers | 112 | 693 |
| Names with ten or more papers | <10 | 69 |
| Prolific share, single-author papers (n = 3,164; 7,122) | 2.8% | 12.1% |
| — two authors (n = 3,617; 6,197) | 4.2% | 18.5% |
| — three authors (n = 2,572; 4,036) | 7.1% | 23.0% |
| — four or five authors (n = 1,301; 1,976) | 10.2% | 27.9% |
| — six or more authors (n = 192; 231) | 11.5% | 28.1% |

Histories begin in January 2025, so whether prolific names were active before cannot be assessed here; the symmetric decomposition with histories from 2019 is pending [ANALYSIS PENDING: maths H2]. Source: companion file arxiv_math_prolific_robustness.json.

**(B) arXiv physics, papers with at most 50 authors** (OAI-PMH metadata harvested on 16 October 2026).

| Group and names | Measure | Q3 2022 | Q3 2025 | Q3 2026 | 2026 departure from 2019–2022 trend, percentage points (95% CI) |
|---|---|---|---|---|---|
| Theory, all names | Papers with an author who has ≥5 papers in the quarter | 7.94% | 13.37% | 16.61% | 2.09 (0.06 to 4.13) |
| Theory, all names | Active authors with ≥5 papers | 0.67% | 1.27% | 1.74% | 0.45 (0.19 to 0.72) |
| Theory, all names | Top 1%'s share of fractional output | 5.50% | 5.86% | 6.52% | 0.82 (0.53 to 1.10) |
| Theory, all names | Top 10%'s share of fractional output | 29.21% | 29.54% | 30.88% | −0.30 (−1.11 to 0.50) |
| Theory, namesake-robust | Papers with an author who has ≥5 papers in the quarter | 2.62% | 5.64% | 8.06% | 1.86 (0.30 to 3.42) |
| Theory, namesake-robust | Active authors with ≥5 papers | 0.38% | 0.92% | 1.33% | 0.40 (0.11 to 0.69) |
| Theory, namesake-robust | Top 1%'s share of fractional output | 4.93% | 5.59% | 6.11% | 0.73 (0.36 to 1.10) |
| Theory, namesake-robust | Top 10%'s share of fractional output | 26.82% | 28.18% | 30.27% | 0.71 (−0.55 to 1.97) |
| Experiment, all names | Top 1%'s share of fractional output | 25.56% | 23.14% | 25.57% | 0.13 (−7.08 to 7.34) |
| Experiment, all names | Top 10%'s share of fractional output | 64.70% | 56.56% | 58.55% | 3.21 (−4.66 to 11.08) |

Ordinary least squares on a linear trend, quarter effects and indicators for 2023–2026, Newey–West intervals. Source: companion file heavy_producers.json.

<!-- SI FILE: S4 Table -->

## S4 Table. Published estimates of LLM-assisted writing by field

*A separate Supporting Information file at submission. Context for H3. The measures differ, so levels cannot be compared across studies; only rankings within a study are informative.*

| Study | Corpus and period | Measure | Results by field |
|---|---|---|---|
| Lin and Zhu (preprint) [@LinZhu2025] | 627,384 arXiv papers, 2021–2023 | Share of abstracts classified as AI-generated; increase from the end of 2022 to the end of 2023 [RECHECK: relative or percentage-point increase] | Computer science 22%; electrical engineering and systems science 21%; finance 18%; statistics 15%; economics 11%; quantitative biology (arXiv q-bio, not bioRxiv) 11%; physics 10%; mathematics 3.5% |
| Liang et al. [@Liang2025] | 1,121,912 preprints and papers on arXiv, bioRxiv and *Nature* portfolio journals, January 2020–September 2024 | Estimated share of LLM-modified sentences, at corpus level | Computer science up to 22%; mathematics and *Nature* portfolio up to 9% [RECHECK: add the bioRxiv series, not read because the article is not open access] |
| Kobak et al. [@Kobak2025] | 15.1 million PubMed abstracts, 2010–2024 | Lower bound on the share of 2024 abstracts processed with LLMs (excess vocabulary) | All abstracts at least 13.5%; computational fields (computation, bioinformatics) about 20%; from below 5% to more than 40% across fields, countries and journals |
| Holzwarth et al. (preprint) [@Holzwarth2026] | PubMed Central open-access full texts | Share of papers with an excess of LLM-associated vocabulary | 89% of papers by the end of 2025 |
| He and Bu (preprint) [@HeBu2025] | 5,114 journals, more than 5.2 million papers, 2021–2025 | Growth in the share of AI-assisted text in abstracts | Fastest growth in the physical sciences (a domain that includes mathematics and computer science); slower growth in the life and health sciences |

### References for S4 Table

<!--SIREFS-->
