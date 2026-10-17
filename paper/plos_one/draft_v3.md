<!--
DRAFT v3.
PLOS ONE Research Article. 17 Oct 2026. Revised from v2 (paper/plos_one/draft_v2.md, commit a17a8b9) by an AI agent
(Claude, Anthropic, via Claude Code) after the round-2 internal reviews R1–R4 (paper/plos_one/reviews/round2/), the
author's decisions A1–A3 (paper/plos_one/reviews/author_critique.md; paper/brief.md) and Deviation 3 of the paper-level
analysis plan with its two addenda (registration files; commits 8932773, 80a2ef2 and 6e1c119). Point-by-point response:
paper/plos_one/reviews/round2/response_round2.md. Not yet revised by the author.

WHAT CHANGED FROM v2
1. Framing (A1). The abstract opening, the Introduction framework and the Discussion now say that evaluation judges
   results; that producing a polished, submittable result used to take substantial skilled work; that generative AI
   makes polish cheap; and that output can therefore rise faster than the research behind it while form becomes a
   weaker cue of quality. Nothing says that evaluation valued effort or cost. A new Introduction paragraph presents form
   as a cue that was always unreliable (Sokal 1996; Bohannon 2013, numbers checked in two secondary reports; Labbé and
   Labbé 2013; Van Noorden 2014). Kusumegi et al. are cited only for the reversed association between writing
   complexity and paper quality; their output-gain estimate is gone from the Introduction and Limitations, and so is
   Renault et al.'s critique of it, which concerns only that estimate.
2. Marker metric removed (A2, "Quitarla del todo"). Fig 4, Table 2, the H3 marker Methods subsection, the H3 Results
   subsection and every marker sentence in the abstract, Discussion and Conclusions are gone; the S2 Appendix
   definitions of the markers are gone too. Methods (Deviations) says that H3 and the second clause of H1 were
   pre-specified with a marker, that the test was run and that the measure was withdrawn after its results were known,
   with the author's reason; the results stay in the deposited files. S4 Table stays as literature context. Figures
   and tables renumbered: Figs 1–3; Tables 1–2 (v2's Table 3 is now Table 2).
3. Author's proposal (A3): one paragraph in "Implications", engaging Blekhman. The verified file of prior attempts
   (paper/sources/open_publishing_attempts.md) did not exist when this version was built, so it carries
   [A3 REFS PENDING]. The rest of "Implications" follows R4 N4: "This supports…" and the DORA/CoARA claim deleted, the
   seven proposals replaced by one sentence (the DORA critique moves to the essay).
4. Paper-level tests. Methods follows R4 N1's model paragraph, updated with Deviation 3 and its addenda (Test B's
   primary set, level-based companion estimates, sealing, the medRxiv estimate computed before the hold and possibly
   seen by the author, the added sensitivity analyses); "held out" is kept for HN only and the set is called
   "pre-specified paper-level tests". Results follows R4's template with [SEALED: ...] placeholders; the abstract has
   one sentence with placeholders. No paper-level result appears anywhere in this file. S1 Text is re-captioned and
   S6 Table (deviations) is built in the Supporting Information.
5. Sentence fixes: R1 N7 and R4 N4 (rows that concern only markers are moot); "falsification test" -> "test";
   "pre-specified estimate relative to 2022" -> "primary estimate as run"; "Four findings withstood the checks" ->
   a corrected statement; Conclusions "should not be compared ... without adjustment"; the abstract leads with the
   placebo p values, has no INSPIRE sentence, a narrowed genre sentence and an H2 sentence on a September-robust
   window with the selection caveat.
6. INSPIRE rewritten (R3 N1–N2, R1): the result depends on the baseline, the rule mostly separates collaboration
   papers from small-team papers, three modes of production, planning-paper removal incomplete, author count 0 as
   missing; the team-size estimates are gone; the Discussion no longer contradicts itself; redo pending (item 9).
7. Settled facts: the bioRxiv duplicate check (no problem; marker removed); dating by first-version submission
   (R2's evidence, to be confirmed); Nee et al.'s like-for-like author panel (list entries, 2.80% -> 4.07%, checked in
   stats/heavy_producers.json); PubMed reduced to one sentence; Qi et al. described as measuring the share of papers
   mentioning AI by discipline, with their bioRxiv slope read as a recovery; the social-science series removed from
   the Fig 1 legend and Table 2.
8. Pending analyses renumbered as companion items 1–13 (list below); mentions of analyses that will not be run
   (OSF continuity, synthetic-control variants, bioRxiv categories without COVID-19, medRxiv flag recall) deleted.
9. Length (R4 N6): main-text prose cut from 7,126 to the figure in the table below; Table 1 cut from 18 to 10 rows;
   detail moved to S2 Appendix, S5 Table and S6 Table (listed in the response, section 3).
10. AI-use statement (R4 N1, §7.1): tools, uses and validation, with placeholders for the model and version of the
    main session and of the classifier and for the training setting; the classifier ran as agents with the harness's
    system prompt and file tools. Title: v2's, with the author's earlier wording in an [AUTHOR] comment.

WORD COUNTS (computed by build_v3.py; HTML comments, headings, figure legends and tables excluded).
'Prose' also removes the editorial markers ([AUTHOR: ...], [ANALYSIS PENDING: ...], [RECHECK: ...], [CONFIRM: ...], [SEALED: ...], [A3 REFS PENDING]) and numbered citations; 'raw' keeps them.

| Section | Prose | Raw |
|---|---|---|
| Introduction | 723 | 756 |
| Materials and methods | 2,073 | 2,371 |
| Results | 1,943 | 2,044 |
| Discussion | 1,383 | 1,427 |
| Conclusions | 114 | 126 |
| **Main text (Introduction to Conclusions)** | **6,236** | **6,724** |

By subsection (prose):

| Section | Subsection | Prose |
|---|---|---|
| Materials and methods | Study design and pre-specification | 128 |
| Materials and methods | Data sources | 249 |
| Materials and methods | Groups for the within-field contrasts (H1) | 165 |
| Materials and methods | Author-level measures (H2) | 194 |
| Materials and methods | Statistical analysis | 454 |
| Materials and methods | Deviations from the analysis plans | 193 |
| Materials and methods | Pre-specified paper-level tests | 297 |
| Materials and methods | Software and data processing | 59 |
| Materials and methods | Ethics statement | 108 |
| Materials and methods | Use of AI tools | 226 |
| Results | Overview of counts | 151 |
| Results | Within-field contrasts (H1) | 599 |
| Results | Distribution of output among authors (H2) | 379 |
| Results | Departures from trend and the comparison between servers (exploratory) | 403 |
| Results | Paper-level evidence in particle and nuclear physics (exploratory) | 270 |
| Results | Pre-specified paper-level tests | 141 |
| Discussion | Principal findings | 164 |
| Discussion | What the within-field tests show | 247 |
| Discussion | Why might arXiv differ from bioRxiv? | 275 |
| Discussion | Implications for research evaluation | 399 |
| Discussion | Limitations | 298 |

Abstract: 276 words of prose (288 raw; 278 by a word-processor count, which also counts '='); PLOS ONE limit 300.
Figure legends in the main text: 677 words. Tables in the main text: 608 words.
References: 61 in the main list; SI lists: S1 Appendix 0, S2 Appendix 13, S1 Table 16, S3 Table 0, S4 Table 5, S5 Table 0, S6 Table 3.

Markers outside HTML comments (title page to the end of the Conclusions; whole file):

| Marker | Manuscript | Whole file |
|---|---|---|
| [AUTHOR] | 25 | 68 |
| [ANALYSIS PENDING] | 20 | 25 |
| [RECHECK] | 0 | 4 |
| [CONFIRM] | 7 | 8 |
| [SEALED] | 29 | 29 |
| [A3 REFS PENDING] | 0 | 0 |
-->

<!--
HOW TO READ THIS FILE
- Built from build/draft_v3_keyed.md by build/build_v3.py (references in build/refs_v3.py, numbered by first citation;
  S1 Table, S2 Appendix, S4 Table and S6 Table have their own reference lists). Edit the keyed file, not this one.
- Markers (all must be resolved before submission):
  [AUTHOR: ...] only the author can supply or decide this;
  [ANALYSIS PENDING: companion item N] an analysis requested from the companion analysis session, not yet delivered;
  [CONFIRM: companion item N] a number taken from a round-2 reviewer's own calculation on committed files, to be
  confirmed by the companion before submission;
  [RECHECK: ...] a claim or reference to check against its source;
  [SEALED: ...] a result of the pre-specified paper-level tests, sealed until the author's blind validation coding is
  committed (Deviation 3, D3i); fill only after unsealing;
  [A3 REFS PENDING] references to prior attempts at open evaluation, from paper/sources/open_publishing_attempts.md.
- Companion items, as sent to the analysis session on 17 Oct 2026: 1 planned specification; 2 regenerated C3 and its
  slope change; 3 rank-based in-time calibration; 4 deposit fixes; 5 figures; 6 dating by first-version submission;
  7 H2 on an independent window, plus the uniform-scaling simulation; 8 structure-matched placebos; 9 INSPIRE redo;
  10 funding splits; 11 genre validation; 12 bioinformatics AI/ML split; 13 the bioRxiv /sum check.
- Blinding: the author has not finished the blind validation coding. Nothing in this file states, or was written from,
  an estimate of HN, Test A or Test B; the drafting agent did not open validation/sealed/, nd_tests.json or anything the
  analysis branch committed about those tests at or after dacd064.
- Figures: Fig1–Fig3 are the companion's files (paper/plos_one/figures/Fig1–Fig3). v2's Fig 4 (marker words) is
  withdrawn, and Fig 1 still draws the social-science series; both are for companion item 5 (re-render in Arial,
  NAAS check, Fig 1 without the social-science series).
- The statements entered in the PLOS submission form (funding, competing interests, data availability, author
  contributions) follow the Supporting Information captions, outside the manuscript proper.
- Related manuscripts (R4 N5) [AUTHOR]: revise the companion essay's empirical paragraphs to cite this article, keep
  the marker-free figures, post this article's preprint first, decide on EMBO Reports, disclose the essay and the
  Correspondence in the cover letter, and mint the essay's DOI (reference CompanionEssay).
- Nee et al.: the arXiv record lists the authors as "Xiaoshn Nee", "Haobo Zhong" and "Xiaomin Ni"; the citation
  follows the record (Nee X).
-->

# Preprint output in the generative-AI era: pre-specified within-field tests find no robust evidence of an experimental bottleneck

<!--
TITLE: v2's title, kept for v3.
[AUTHOR: choose the title. Your earlier preferred wording was "Generative AI is eroding publication counts as a measure
of scientific work: evidence from [N] preprints". R4 (round 2, section 3.1 and minor 1) points out that the evidence
does not attribute the change to AI (the article itself says so in its abstract and Conclusions), so a title that makes
AI the cause, or says "eroding", would claim more than the data show (PLOS criterion 4). R4 also suggests "contrasts"
for "tests", because the contrasts, not the estimand, were pre-specified (N3), and a plainer object than "experimental
bottleneck".]
Short title (at most 100 characters): Preprint output in the generative-AI era
Alternatives from round 2 (R4 minor 1): "Preprint growth in the generative-AI era: pre-specified within-field contrasts show
no robust difference between experimental and non-experimental work" (151 characters); or v2's title with "contrasts"
for "tests". Round-1 alternatives are listed in build/draft_v2_keyed.md.
-->

[AUTHOR: full name]<sup>1,2,*</sup>

<sup>1</sup> European Molecular Biology Laboratory (EMBL), [AUTHOR: unit, site, city, country]
<sup>2</sup> Universitat Pompeu Fabra (UPF), Barcelona, Spain

\* Corresponding author: [AUTHOR: email; ORCID iD]. <!-- EMBL must be the corresponding affiliation for the EMBL–PLOS flat-fee agreement; confirm with the EMBL library. -->

## Abstract

Research evaluation judges results, but a polished, submittable result used to take substantial skilled work. Generative artificial intelligence (AI) makes polish cheap, so output can outpace the research behind it and form becomes a weaker cue of quality. If AI raised output mainly where no new experiments are needed, theoretical, computational and secondary-data preprints should have outgrown experimental ones within a field. I tested this with three contrasts fixed before modelling, in monthly counts of new preprints on arXiv (2015–2026), bioRxiv and medRxiv (2019–2026). With the planned specification, January–September 2026 rate ratios against pre-2023 baselines were 1.05 (95% CI 0.93–1.18) for theoretical against experimental physics, 1.02 (0.94–1.11) for computational against wet-lab biology and 1.05 (0.98–1.13) for medRxiv preprints naming reused datasets against others. Against 2022 alone, as first reported, they were 1.14 (1.00–1.30), 1.08 (1.03–1.14) and 1.01 (0.90–1.14), typical of arbitrary splits and of each contrast's own years. The prediction was not supported; only biology's contrast favoured it, against extrapolated pre-2023 trends (1.36; 1.07–1.75). In pre-specified paper-level tests, papers without new data in three held-out arXiv archives [SEALED: grew faster than / did not grow detectably faster than] papers with new data (ratio [SEALED]; 95% CI [SEALED]). Against 2015–2022 trends, arXiv physics and mathematics stood 32% and 48% higher in 2026, whereas bioRxiv (0.91) and PubMed (0.93) did not, although bioRxiv grew more in levels than the physics archives tested. Output grew in every class of authors; in mathematics, between January–August 2025 and 2026, the 1% of names with the highest combined output grew 78% and the bottom 90% 26%, a ranking that partly selects on 2026 output. These data cannot attribute the changes to AI, but counts moved unevenly across servers, which limits comparisons across fields and years.

<!-- Abstract: PLOS ONE limit 300 words; see the word counts in the header (the word-processor count includes "=").
The [SEALED] placeholders will add about 10 words. The genre clause ("there") refers to mathematics and the six particle and
nuclear physics archives of C1, the only archives the genre split covers (Results). -->

## Introduction

Research evaluation judges results. Decisions on hiring, promotion and funding rest heavily on counts of research outputs [1], but results are hard to observe directly, and producing a polished, submittable result (a paper, a review, a grant application) used to take substantial skilled work. That work limited how much could be produced, and polish served as a cue of quality. Generative artificial intelligence (AI) makes polish cheap, whether it is used well or badly. If the work needed to reach a submittable form falls, output can rise faster than the research behind it, counts change meaning, and form becomes a weaker cue of quality. A companion essay develops this argument [2]; this article tests one empirical premise of it: whether, and where, output rose.

Form was always an unreliable cue. Hoaxes have shown repeatedly that plausible form can pass gatekeeping without substance: *Social Text* published Sokal's parody in 1996 [3]; a deliberately flawed paper sent to 304 open-access journals in 2013 was accepted by 157 of them [4]; and computer-generated nonsense appeared in more than 30 published conference proceedings until publishers withdrew more than 120 such papers in 2014 [5,6]. Yet the cue carried some information: in preprints, writing complexity went with paper quality before large language models (LLMs), and LLM use has reversed that association [7]. What generative AI changes is the cost of plausible, polished form, which is now cheap at scale.

Output was growing before generative AI [8]: indexed articles were about 47% more numerous in 2022 than in 2016 [9]. Since then, an editorial in *Organization Science* has reported a 42% rise in submissions [10], the US National Institutes of Health (NIH) has reported that AI tools enabled some applicants to submit more than 40 applications in one round [11], and arXiv received 40,363 submissions in September 2026, against 20,569 in September 2024 [12]. Funders, preprint servers and conferences have responded by limiting how many items each person may submit (S1 Table).

Two studies measured where output changed. Qi et al. analysed 2.1 million preprints on arXiv, bioRxiv, medRxiv and SocArXiv from 2016 to August 2025: the share of papers mentioning AI in their titles or abstracts ranged from over half in computer science to under a fifth in physics and mathematics, and monthly submissions accelerated after ChatGPT's release on arXiv and bioRxiv but not on medRxiv or SocArXiv [13]. Nee et al. estimated with a synthetic control that arXiv mathematics recorded 11.9% more list entries in January–August 2026 than its counterfactual, and that the share of author units with at least five submissions rose from 2.45% to 3.80% [14]. Comparisons between servers and fields are hard to read: fields adopted preprints at different times and rates [15–17], medRxiv opened only in 2019 [18], COVID-19 brought a surge of preprints [19], and servers screen submissions and accept different genres [20–22]. Within a field, experimental and non-experimental work share most of these conditions, so contrasting them is a sharper test of the idea, argued for biology by Blekhman [23], that output grows where the work beyond writing is cheap and not where experiments bind. Aggregate counts also hide whether growth comes from many authors or a few, a question studied mainly for extreme output [24,25].

This article therefore reports three within-field contrasts, fixed before any model was estimated, as a test of that idea; replicates Nee et al.'s measures on a different count unit and decomposes growth by class of author in mathematics and theoretical physics; and reports pre-specified paper-level tests of a refined hypothesis. The hypotheses, recorded after descriptive counts had been seen and before any model was estimated (commit 2cac071, 16 October 2026, 16:42 UTC), read:

- **H1.** AI-era acceleration of output is concentrated where the work beyond writing is also cheap: theory, computation, existing data. In experimental work, AI shows in the writing but much less, or not yet, in output.
- **H2.** Where output accelerates, the shift is broad. It comes from many established researchers producing more, not from a few outliers.
- **H3.** AI-assisted writing is widespread across fields, including experimental ones, so differences in output are not explained by differences in adoption.

H1 came from my view, as a physicist and biologist, that experimental biology was less affected than other fields [AUTHOR: confirm the origin of H2 and H3, and the description of your field]. Its first clause was tested with the three contrasts and H2 with author-level measures; H3 and the second clause of H1 were to be tested with a marker of AI-assisted writing, which I withdrew (Methods).

## Materials and methods

### Study design and pre-specification

This observational study analyses monthly counts of new preprints (first versions) and, for H2, the author lists of individual papers. The groups were defined before their growth was computed, but the hypotheses and the choice of the three contrasts as primary tests were recorded when each group's descriptive growth was known (commit 2cac071). The analysis plan was written in v1 of this manuscript (commit 697fb25, 17:27 UTC), and the companion analysis committed its model specification together with its first estimates (companion commit 37b4b11, 17:43 UTC) [AUTHOR: state whether the session logs show that the specification was fixed before any estimate was computed]. "Pre-specified" therefore means fixed before any model was estimated, not before the data were seen: it protects against choosing models after seeing estimates, not against choosing contrasts. All other analyses, including those requested in review, are exploratory, except the paper-level tests described below.

### Data sources

*arXiv.* Monthly counts of new submissions by primary archive, January 2010 to September 2026, were read from arXiv's statistics pages [26], with versions adding cross-lists (list entries, the unit of Nee et al. [14]); physics sums 13 archives, and aliased categories put archive sums about 5% above arXiv's total (S2 Appendix). Author lists, comments and categories of papers since 2019 in mathematics and the six archives of contrast C1 (C1's six archives) were harvested through arXiv's OAI-PMH interface; they describe each paper's latest version, and their series of primary math.\* papers (H2, genres) is about 90% of the statistics pages' mathematics count, with the same growth (S2 Appendix). Papers are dated by the month of their identifier, which arXiv assigns at announcement [27].

*bioRxiv and medRxiv.* Monthly counts of version-1 preprints in 25 bioRxiv subject categories, January 2019 to September 2026, came from the bioRxiv API [28]; they include COVID-19 preprints, have almost no duplicate DOIs and from July 2019 sum to bioRxiv's official totals [29] (S2 Appendix) [ANALYSIS PENDING: companion item 13 (bioRxiv /sum check)]. The medRxiv API lists some version-1 preprints twice, mostly in 2026, so every medRxiv series counts each DOI once and excludes preprints that mention COVID-19 in the title or abstract.

*PubMed and INSPIRE-HEP.* PubMed journal articles per quarter by entry date were counted with NCBI's E-utilities [30]. INSPIRE-HEP records of six particle and nuclear physics archives, dated by first-version submission, were read from its API [31]. Retrieval followed each source's terms, except two earlier retrievals that exceeded documented rates (S2 Appendix). Data were retrieved on 15–16 October 2026 [CONFIRM: companion item 4 (retrieval dates of the INSPIRE-HEP, arXivRaw and paper-level samples)].

### Groups for the within-field contrasts (H1)

The groups were proposed while the companion essay was being drafted (S2 Appendix). In physics (C1), theory is hep-th, hep-ph, gr-qc and nucl-th, and experiment is hep-ex and nucl-ex; astro-ph, cond-mat, quant-ph and hep-lat are in neither group [AUTHOR: state why hep-lat was left out]. gr-qc includes gravitational-wave experiments and, under the rule applied to astro-ph and cond-mat, should have been left out of theory; C1 is reported as pre-specified and also, as a correction made after the results were seen, without gr-qc. In biology (C2), bioinformatics, systems biology and genomics are contrasted with 12 wet-lab categories; genomics includes bench sequencing, and in bioinformatics AI is often the topic rather than a tool. In medicine (C3), medRxiv preprints naming a widely reused public dataset or design (NHANES, UK Biobank, Global Burden of Disease, Mendelian randomisation, FAERS, MIMIC-III or MIMIC-IV, SEER or BRFSS), which recur in formulaic analyses [32,33], are contrasted with all other medRxiv preprints, both without COVID-19 preprints. The list shares five of the nine heavily mined datasets of Spick et al. [33] [AUTHOR: state when the list was fixed].

### Author-level measures (H2)

Authors are matched by normalised name strings, because arXiv has no author identifiers. Such strings merge different people and split the same person [34,35], so every measure is also computed for namesake-robust names (full first names only, 1% most frequent surnames removed); in physics, papers with more than 50 authors are excluded (S2 Appendix). The main statistic decomposes the change in fractional output (each paper divided equally among its authors) between the same months of consecutive years by author class (top 1%, next 9%, bottom 90%), with names ranked on their combined output in both years. Under proportional growth every class grows at the total rate, and pairs of years before ChatGPT's release show how much classes differ by chance. Ranking on combined output avoids regression to the mean, but when growth is uneven it also moves names with large increases into the top class [ANALYSIS PENDING: companion item 7 (classes ranked on an independent window)]. The shares of output produced by the top 1% and top 10% of active names are descriptive, because with count noise and an activity threshold they can rise under proportional growth [ANALYSIS PENDING: companion item 7 (uniform-scaling simulation)]; their departures from 2019–2022 trends (ordinary least squares, quarter effects, Newey–West errors [36]) describe uncertainty about the trend, not sampling.

### Statistical analysis

*Within-field contrasts.* As planned (v1, commit 697fb25), the monthly counts of the non-experimental group A and the experimental group B were stacked and modelled as log E[*y*<sub>*gt*</sub>] = *α*<sub>*g*</sub> + *γ*<sub>*m*(*t*)</sub> + *β*<sub>*p*(*t*)</sub> + *θ*<sub>*p*(*t*)</sub>·1[*g* = A], with group effects, calendar-month effects and effects of the periods 2023–2024, 2025 and 2026 against a multi-year baseline (2017–2022 for arXiv, 2019–2022 for bioRxiv, July 2019 to 2022 for medRxiv). The estimate, exp(*θ*<sub>2026</sub>), is the rate ratio of A to B in January–September 2026 relative to baseline; values above 1 mean that the non-experimental group grew faster. Counts were overdispersed in every contrast [37], so, as planned, a negative binomial (NB2) model replaced the Poisson model. Driscoll–Kraay standard errors (12 lags) [38], the panel form of the planned Newey–West errors, measure within-period uncertainty only: they omit year-to-year shocks to the ratio and heterogeneity between the archives or categories in each group [39], so minimum detectable effects at 80% power are lower bounds. The three 2026 p values are Holm-adjusted [40] and reported with Bonferroni-adjusted (98.3%) intervals. The planned checks were a moving-block bootstrap, run on the log ratio by ordinary least squares, and group-specific linear pre-trends. The estimates first reported, a deviation (Deviations), used 2022 as the reference year, Poisson pseudo-maximum likelihood [41], month fixed effects and group-specific calendar-month effects; they are reported beside the planned ones.

*Calibration (added after the estimates were seen).* As with few treated units [42], each contrast's 2022-based estimate is compared with the same estimate for all 153 pairs of the 18 arXiv archives with complete data since 2015 (C1) and all 462 splits of the 12 wet-lab categories into halves (C2); the placebo p value is the share of placebos at least as far from 1, with one added to numerator and denominator [ANALYSIS PENDING: companion item 8 (placebos matched to each contrast's structure, with both estimators)]. No placebo was defined for C3. Whether 2026 was unusual for a contrast is judged by rank, with the same estimator: its 2026 year coefficient among the earlier ones, and its 2026/2025 change among all earlier year-on-year changes (two-sided p, the share at least as far from 1, 2026 included) [CONFIRM: companion item 3 (definition)].

*Robustness and exploratory analyses.* Each contrast was re-estimated without each component (robust only if no single exclusion moves it across 1, a criterion stated after the estimates were seen), against other base years and as acceleration (2026 against 2025). Departures of each field and archive from its own pre-2023 trend were estimated by Poisson pseudo-maximum likelihood with a linear trend, calendar-month effects and a COVID-19 indicator. Further checks compared arXiv groups with bioRxiv, replicated Nee et al.'s synthetic control [14,43], tested for breaks as late as January 2026 [44], removed planning papers (Snowmass 2021, European Strategy), split mathematics and C1's six archives into genres by keyword, and classified INSPIRE-HEP records by a registered rule (S2 Appendix; S5 Table).

### Deviations from the analysis plans

S6 Table lists every departure from the two plans, when it was recorded and what had been seen by then [45,46]. Three matter most. First, the estimates first computed and reported (v1 and v2) replaced the planned multi-year baselines with 2022 as the reference year, which turned the plan's pre-trend diagnostic into the primary estimate [AUTHOR: reasons for, and timing of, the change of reference year]. The ratios were low in 2022 in C1 and C2, which favours H1 there. The planned specification was computed only in review, after the 2022-based estimates were known; it is primary here, and both are reported. Second, after the estimates were seen I added a decision rule for H1 as a whole (support in all three fields), the leave-one-out criterion, and the placebos and ranks as calibration. Third, H3 and the second clause of H1 were pre-specified with a marker of AI-assisted writing, the frequency of style words whose use rose with LLMs [47], and that test was run. After its results were known I withdrew the measure, because its relevance after 2024 cannot be assured: the marker vocabulary drifts as authors and models avoid the words [48]. The results remain in the deposited analysis files (marker_tests.json and marker_growth_panel.csv; S1 Data) [AUTHOR: R4 recommends instead reporting the 2024-only marker test in an S Table, with your reason as a limitation; choose].

### Pre-specified paper-level tests

After the H1 results were known, I formed a refined hypothesis, prompted by an exploratory count made by an AI agent during internal review (Results): within a field, papers that report no new empirical data grew faster in January 2025–September 2026, relative to their 2017–2022 trends, than papers that do. Its tests were written with AI assistance, approved by me and time-stamped in the project's public repository before any paper was classified (commits 763aa2b and 78890e5, 16 October 2026, 18:28 and 18:47 UTC; S1 Text), not in a registry. HN, the held-out test, compares the two classes in arXiv cond-mat, astro-ph and quant-ph, whose totals, but not their composition, had been examined. Test A repeats it on bioRxiv and medRxiv, examined in C2 and C3. Test B relates each category's departure from trend, already examined, to its share of papers with new data, in 15 held-out arXiv subcategories and the bioRxiv and medRxiv categories. Each trend-based estimate is reported beside a level-based one against pooled base years. Papers were classified by [AUTHOR: model and version of the classifier] (Anthropic), run as Claude Code sub-agents in batches of 50, in random order and under pseudonymous identifiers, from the title, abstract and (for arXiv) comments; class shares in stratified random samples scale monthly totals, and the bootstrap does not carry misclassification. A domain's results are confirmatory only if the classifier agrees with my blind coding of 400 papers at Cohen's κ ≥ 0.60. The estimates stayed sealed, with only their hashes committed, until my coding was committed, except Test A on medRxiv, which was computed before the hold and reported in the analysis session's chat with me, so my coding of medRxiv papers may not be blind to it [AUTHOR: state whether you read it before coding]. The sensitivity analyses are in S1 Text; S6 Table gives every deviation, its time and what had been seen.

### Software and data processing

Data were harvested and analysed with Python 3.13.16 (numpy 2.5.3, pandas 3.0.5, scipy 1.18.1, statsmodels 0.15.0, matplotlib 3.11.2 and pillow 12.3.0, pinned in requirements.txt) in the companion analysis, whose script run_all.sh reproduces the count-based estimates and figures from the committed data with fixed random seeds; the author-level analyses need harvests that contain names and are not deposited (Data availability).

### Ethics statement

This study analysed public bibliographic metadata and aggregate counts; no human participants were recruited. Author name strings from arXiv, which are personal data, were processed only to count papers per name within periods and are never written to released files; no name is reported, and no statistic describing fewer than ten authors is released. Any author-level file released later will be pseudonymised [AUTHOR: decide whether to release it after the consultation below]. The main risk, re-identification of heavy producers by re-running the code, with reputational harm if high output were read as misuse of AI, is mitigated by reporting aggregates only and by interpreting no individual's output. [AUTHOR: data-protection consultation: name the office (EMBL, under its Internal Policy No. 68, or UPF, under the GDPR), the framework that governs this processing, the date, the outcome, and the lawful basis and safeguards recorded.] Data were retrieved under each source's terms of use (S2 Appendix).

### Use of AI tools

I used Claude (Anthropic), via Claude Code [AUTHOR: model and version of the main sessions], between 15 October and [AUTHOR: date] 2026, on a [AUTHOR: account type] account [AUTHOR: state the account's model-training setting]. AI agents (i) searched the literature and checked references; (ii) drafted the text of every section from my decisions and outlines, and revised it after review; (iii) wrote all code for harvesting, processing, statistical analysis and figures, in a separate session (the companion analysis); (iv) produced all figures with that code; (v) wrote internal critical reviews of the drafts in four reviewer roles, which are not peer review; and (vi) classified about [AUTHOR: N] papers by whether they report new empirical data, as Claude Code sub-agents running [AUTHOR: model and version of the classifier], with the harness's system prompt, a fixed run instruction and file tools (Methods). I evaluated these labels by coding a blind stratified random sample of 400 papers [AUTHOR: state whether a colleague coded 100 of them] (S1 Text). H1 originated with me, as did the refined hypothesis of the paper-level tests and their INSPIRE-HEP component; the wording of H1, and H2 and H3, were drafted with AI assistance and adopted by me. The analysis plan, the group definitions and the statistical specification were proposed by AI agents and adopted or modified by me [AUTHOR: describe your own validation: the code you reviewed line by line (groups, flags, author matching, models); re-runs of the pipeline (commit hash) with identical outputs; numbers recomputed from the source APIs; sources read in full; AI proposals you rejected]. A proprietary model needs justification in research [49] [AUTHOR: give yours]. The interpretations and conclusions are mine [AUTHOR: adopt or amend those of v3, which an AI agent drafted from AI reviews]. Checks made by AI agents are listed in S1 Appendix and are not counted as validation. No AI tool is an author, and I take responsibility for the content.

## Results

### Overview of counts

New preprints rose in every field from 2022 to 2026, but not in the same way (Fig 1; S2 Table). From January–September 2022 to the same months of 2026, bioRxiv grew 1.53-fold, more than C1's six physics archives (1.33-fold) and less than mathematics (1.71-fold). bioRxiv grew steadily, by 9–13% a year in 2023–2026, whereas the six physics archives grew by 0%, 6% and 6% in 2023–2025 and by 19% in 2026. Non-COVID medRxiv preprints, each counted once, grew by 20.9% in 2025 and 16.4% in 2026. In arXiv mathematics, September 2026 alone had 8,360 new papers, against 5,903 in August, a spike in submissions rather than a release of held papers: of the papers with a known first-version date, 7,697 were submitted in September and 7,842 announced in it. INSPIRE-HEP records dated by submission grew as fast as arXiv counts dated by announcement (hep-ex +13.7% against +14.2% from 2025 to 2026) [CONFIRM: companion item 6].

**Fig 1. New preprints by field, indexed to 2022.** Quarterly new preprints (first versions), each series divided by its mean quarterly count in 2022 (2022 = 100), January 2020 to September 2026; the number in each legend entry is the index for July–September 2026. Physics: new submissions to the 13 arXiv physics archives, by primary archive. Mathematics: arXiv math. Computer science: arXiv cs, shown for reference; it includes AI research itself. Biology: bioRxiv. Medicine: medRxiv, excluding preprints that mention COVID-19 or SARS-CoV-2 in the title or abstract, each preprint counted once. Dashed vertical lines mark the release of ChatGPT (30 November 2022), arXiv's rule on review and position papers in computer science (31 October 2025) and arXiv's cap of two submissions per submitter per month (1 October 2026, after the last quarter shown); they are dates for reference, not estimated break points or causes. Indexing to 2022 favours series whose 2022 count was low, such as medicine and biology; departures from each series' own trend are reported in the text. The code that drew this figure was written with an AI assistant (Claude, Anthropic, via Claude Code) under the author's direction; data and code are in S1 Data.
<!-- Figures (companion item 5, done): OSF and social sciences removed; the TIFFs use Liberation Sans, metric-compatible with
Arial, because Arial cannot be installed in the analysis container. [AUTHOR: re-run plot_plos.py on a machine with Arial
before submission; it uses Arial when present.] -->

### Within-field contrasts (H1)

The pre-specified within-field contrasts did not support H1 (Table 1; Fig 2). With the planned specification, the January–September 2026 rate ratio of non-experimental to experimental work against the multi-year baseline was 1.05 (95% CI 0.93–1.18; p = 0.41) in physics, 1.02 (0.94–1.11; p = 0.66) in biology and 1.05 (0.98–1.13; p = 0.19) in medicine, none different from 1 even before adjustment for multiplicity; the smallest rate ratios detectable with 80% power were 1.18, 1.12 and 1.11. The estimates first reported, against 2022 alone, were larger in physics and biology, 1.14 (1.00–1.30; Holm-adjusted p = 0.11) and 1.08 (1.03–1.14; p = 0.01), because the ratios were low in 2022, and 1.01 (0.90–1.14; p = 0.84) in medicine. Even these were typical of arbitrary splits (placebo p = 0.61 in physics, 0.20 in biology), and no contrast's 2026 coefficient was unusual among its own years (rank p = 0.67, 0.80 and 0.60). H1 therefore fails under either specification, with or without the rule, added after the results (Methods), that it needs support in all three fields. The planned checks are in Table 1; group-specific pre-trends are discussed below.

**Table 1. Within-field contrasts: planned (pre-specified) estimates, estimates first reported, and checks.**

| | C1 physics: theory / experiment (1,484; 142) | C2 biology: computational / wet lab (698; 1,994) | C3 medicine: public dataset / other (97; 1,226) |
|---|---|---|---|
| Planned: 2026 vs multi-year baseline, rate ratio (95% CI); p | 1.05 (0.93–1.18); 0.41 | 1.02 (0.94–1.11); 0.66 | 1.05 (0.98–1.13); 0.19 |
| Planned: Holm-adjusted p; Bonferroni 98.3% CI | [ANALYSIS PENDING: companion, Table 1 request 2] | [ANALYSIS PENDING] | [ANALYSIS PENDING] |
| Planned: 2023–2024; 2025 | [ANALYSIS PENDING: companion, Table 1 request 2] | [ANALYSIS PENDING] | [ANALYSIS PENDING] |
| Planned: minimum detectable rate ratio, 80% power (α = 0.05), lower bound | 1.18 | 1.12 | 1.11 |
| Planned check: moving-block bootstrap of the log ratio | [ANALYSIS PENDING: companion, Table 1 request 3] | [ANALYSIS PENDING] | 1.09 (0.995–1.20) |
| Planned check: group-specific linear pre-trends | [ANALYSIS PENDING: companion, Table 1 request 1] | 1.36 (1.07–1.75) | [ANALYSIS PENDING] |
| First reported: 2026 vs 2022, rate ratio (95% CI) | 1.14 (1.00–1.30) | 1.08 (1.03–1.14) | 1.01 (0.90–1.14) |
| First reported: Holm-adjusted p; Bonferroni 98.3% CI | 0.11; 0.97–1.34 | 0.01; 1.02–1.16 | 0.84; 0.87–1.17 |
| First reported: minimum detectable rate ratio, 80% power (α = 0.05; α/3), lower bounds | 1.21; 1.25 | 1.08; 1.09 | 1.19; 1.22 |
| First reported: event study, 2023; 2024; 2025 | 1.08; 1.11; 1.08 | 0.97; 0.94; 0.98 | 0.99; 0.97; 0.92 |
| First reported: pre-period coefficients beyond 0.9–1.1 | 2020: 1.25; 2021: 1.19 | 2019: 1.24 | 2020: 0.88 |
| Calibration: placebo p; rank p of 2026 | 0.61 (153 archive pairs); 0.67 | 0.20 (462 wet-lab halvings); 0.80 | not defined; 0.60 |
| Other bases | 2019: 1.05 (0.90–1.23); 2017–2019 + 2022: 1.12 (0.99–1.26); 2022 without planning papers: 1.06 (0.89–1.25) | 2019: 0.87 (0.80–0.95); 2019 + 2022: 0.99 (0.80–1.22) | 2019: 1.01 (0.86–1.19); 2019 + 2022: 1.01 (0.90–1.13) |
| Leave-one-out range (component dropped) | 1.03 (nucl-ex) to 1.43 (hep-ex) | 0.93 (bioinformatics) to 1.14 (genomics) | – |
| Reading | Inconclusive | Null against the planned baseline; depends on the counterfactual | Null |

Rate ratio of group A to group B; values above 1 mean that the non-experimental group grew faster. Column heads give new preprints per month in 2026 (A; B). Planned: negative binomial (NB2) model with group, calendar-month and period effects against 2017–2022 (C1), 2019–2022 (C2) or July 2019 to 2022 (C3). First reported: Poisson pseudo-maximum likelihood with month fixed effects, group-specific calendar-month effects and year effects, 2022 = 1; the other bases and the leave-one-out range use this model. 95% CIs are Driscoll–Kraay intervals, which measure within-period uncertainty only; the detectable effects are therefore lower bounds. Placebo p: share of placebos at least as far from 1, with one added to numerator and denominator. Rank p: two-sided, the share of the contrast's year coefficients at least as far from 1 as 2026's, 2026 included. C3 counts each medRxiv preprint once. Acceleration, slope changes, negative controls and variants of C1 are in S5 Table.

**Fig 2. Within-field contrasts.** (A–C) Quarterly new preprints, 2022 = 100, for groups within a field that differ in how much of the work is experimental. (A) arXiv physics, by primary archive: theory (hep-th, hep-ph, gr-qc, nucl-th) and experiment (hep-ex, nucl-ex); the experimental series is small (about 430 papers a quarter in 2026). (B) bioRxiv version-1 preprints: computational (bioinformatics, systems biology, genomics), wet lab (twelve categories; Methods) and all other categories; COVID-19 preprints are included. (C) medRxiv, excluding COVID-19 and counting each preprint once: preprints whose title or abstract names a public dataset or design that recurs in formulaic papers (NHANES, UK Biobank, Global Burden of Disease, Mendelian randomisation, FAERS, MIMIC, SEER, BRFSS) and all other preprints. (D) Rate ratio of group A to group B in each year relative to 2022 (theory / experiment, computational / wet lab, public dataset / other), from a Poisson pseudo-maximum-likelihood model with month fixed effects and group-specific calendar-month effects; bars are 95% Driscoll–Kraay confidence intervals, which omit year-level and between-category variation; logarithmic scale; 2026*, January–September. Dashed vertical lines in A–C as in Fig 1. The code that drew this figure was written with an AI assistant (Claude, Anthropic, via Claude Code) under the author's direction; data and code are in S1 Data.

The physics contrast is inconclusive rather than null: its planned interval includes rate ratios up to 1.18, about the smallest it could detect, and the two experimental archives diverged from each other (hep-ex / nucl-ex 1.39, against 2022) more than theory diverged from experiment. The estimate first reported rests on nucl-ex, whose January–September count barely changed in a decade (323 papers in 2016, 346 in 2026), and on a 2022 base inflated by Snowmass 2021 white papers (16.4% of hep-ex's papers that year): without nucl-ex it is 1.03, and without planning white papers 1.06 (0.89–1.25), with experiment growing at least as much as theory within particle physics (hep-ph / hep-ex 0.88, 0.74–1.04). Part of what remains comes from gr-qc, whose growth relative to experiment predates 2023: without gr-qc the planned estimate is 0.99 (0.89–1.11; p = 0.88), and the estimate first reported 1.10 (placebo p = 0.70).

The biology contrast depends on the counterfactual. Against the planned baseline it is null. The estimate first reported (1.08) equals its own minimum detectable effect, was matched by one in five halvings of the wet-lab categories, and rests on bioinformatics, 63% of the computational group: without bioinformatics it is 0.93, as genomics and systems biology grew more slowly in 2026 (7% and 5%) than the wet-lab categories (8%). With group-specific linear pre-trends, a planned check, it is 1.36 (1.07–1.75), because the computational categories had been losing ground to the wet-lab ones by 5.4% a year in 2019–2022, with the ratio's strongest break in July 2020 (p = 0.013), within bioRxiv's adoption period; whether that decline would have continued cannot be known. With pre-trends, physics and medicine stay near or below 1 [ANALYSIS PENDING: companion, Table 1 request 1 (planned); first reported 0.98 and 0.87]. As acceleration the biology contrast is ordinary for its series: its 2026/2025 ratio (1.10; 1.06–1.15) was the largest rise since 2019 but smaller than the fall of 2020 (rank p = 0.29), and it was mainly a wet-lab slowdown (from 13% growth in 2025 to 8%) while computational growth held at 20% and 18% [ANALYSIS PENDING: companion item 12 (bioinformatics split by AI/ML topic)].

The medicine contrast is null under every base (planned 1.05, 0.98–1.13; 1.01 against 2022) and, under within-period uncertainty only, excludes increases of more than 13%. Its 2026/2025 ratio (1.10; 1.03–1.18; rank p = 0.29), a rise after a dip in 2025, is as large as biology's and is read the same way. Variants of the dataset list and of the COVID-19 filter change it little (S5 Table). C3 is a weak test of H1: the flag records a mention, not a design, its expressions are unvalidated [AUTHOR: code the 200-row medRxiv flag sheet for precision, or keep "unvalidated"], and the comparison group is itself largely secondary-data research.

### Distribution of output among authors (H2)

Output grew in every class of authors in 2026, and far more unevenly in mathematics than in theoretical physics (Fig 3). In mathematics, with names ranked on their combined output in January–August of 2025 and 2026, the top 1% increased their fractional output by 78%, the next 9% by 41% and the bottom 90% by 26% (33% overall); between the third quarters, which include the September spike, the figures were 266%, 120% and 57% (80% overall). In both windows the bottom 90% contributed 52% of the increase and the top 1% 14–15%. In pairs of years before ChatGPT's release the classes' growth differed by at most nine percentage points (14 for namesake-robust names). In every window and name variant the top 1% grew fastest, by 62% to 266%, against 12% to 57% for the bottom 90% (S5 Table). The top class is partly selected on 2026 output: the third-quarter top 1% of 2026 had produced 1.08 fractional papers per name in 2025, against 1.64–1.80 for the top 1% of earlier pairs, so it is not the previously most productive 1% [ANALYSIS PENDING: companion item 7]. The top 1%'s share of fractional output rose from 5.15% to 6.84% between third quarters, 1.77 percentage points above its 2019–2022 trend (1.37–2.17), part of which may be mechanical (Methods). Counted as list entries in January–August, as in Nee et al. [14], the share of names with five or more papers rose from 2.80% to 4.07%, against their 2.45% to 3.80%. Fixed-threshold measures are in S3 Table.

**Fig 3. Concentration of output among authors in mathematics and theoretical physics.** arXiv mathematics (math.\*) and physics theory (hep-th, hep-ph, gr-qc and nucl-th; papers with at most 50 authors), by primary category; authors are matched by name strings, because arXiv has no author identifiers. (A) Share of fractional output (each paper divided equally among its authors) produced by the top 1% of active authors in each quarter. (B) Share of papers with at least one author who has five or more papers in the same field that quarter, a fixed-threshold measure that rises mechanically with volume. Solid lines, all author names; dashed lines, namesake-robust (full first names only, with the 1% most frequent surnames removed); the dashed vertical line marks the release of ChatGPT. (C, D) Growth in fractional output between the third quarters (July–September) of consecutive years, by author class, in mathematics (C) and physics theory (D). Authors are ranked by their combined output in the two years compared (top 1%, next 9%, bottom 90%; ties at a class boundary are shared), which avoids regression to the mean but, when growth is uneven, places names with large increases in the top class. Black horizontal marks, all authors; under proportional growth, every class would grow at that rate. The grey background marks pairs that end before ChatGPT's release, which show how far the classes diverge by chance. The third quarter of 2026 includes the September spike in mathematics; January–August windows are in the text and S5 Table. The code that drew this figure was written with an AI assistant (Claude, Anthropic, via Claude Code) under the author's direction; data and code are in S1 Data.

In theoretical physics, the top 1% of names increased their fractional output by 44%, the next 9% by 37% and the bottom 90% by 21% between third quarters (26% overall), and the bottom 90% contributed 54% of the increase, after growing by −0.7% to 8.1% in earlier pairs of years; in one variant (namesake-robust names, July–August) the top 1% grew least. The top 1%'s share rose from 5.86% to 6.52%, 0.82 percentage points above trend (0.53–1.10), while the top 10%'s share stayed at trend. H2 is therefore partly supported: growth was broad, since every class grew and the bottom 90% contributed about half of the increase, and it did not come from a few outliers, but whether established researchers produced more was not tested; small-team experimental papers were too few for these measures.

### Departures from trend and the comparison between servers (exploratory)

Against their own 2015–2022 trends, arXiv physics and mathematics accelerated in 2025–2026, while bioRxiv and PubMed did not (Table 2). In 2026, 14 of the 18 arXiv archives stood at least 1.25 times their trends, with the largest departures in archives whose pre-2023 trend was falling; among them was the experimental particle-physics archive (hep-ex 1.37, 1.12–1.67), but not nucl-ex (1.00). Removing planning papers raised hep-ex's departure to 1.58 (1.38–1.82), mostly by lowering the trend whose last year they had inflated. Counted as list entries, which include cross-lists (67–69% of hep-ex and nucl-ex entries in 2026), departures are smaller (physics 1.24, 1.17–1.32; mathematics 1.43, 1.24–1.66; S5 Table). In C1's six archives, proceedings fell as a share of output, and papers not flagged by keyword as proceedings, white papers, theses or reviews departed from their 2019–2022 trends as much as all papers (1.27, 1.19–1.37, against 1.19); so did they in mathematics (1.69 against 1.68), where the keyword classes are unvalidated, while in the two experimental archives neither series departed (1.08 and 0.97) [ANALYSIS PENDING: companion item 11 (genre validation)].

**Table 2. Departures from the pre-2023 trend by field (exploratory).**

| Series | Trend per year | 2024 | 2025 | 2026 (Jan–Sep) |
|---|---|---|---|---|
| Physics (13 arXiv archives) | 2.9% | 1.05 (1.02–1.08) | 1.14 (1.10–1.18) | 1.32 (1.24–1.39) |
| Mathematics (arXiv math) | 2.9% | 1.04 (0.98–1.11) | 1.08 (1.02–1.14) | 1.48 (1.26–1.73) |
| Computer science (arXiv cs) | 21.0% | 1.00 (0.88–1.14) | 1.02 (0.88–1.18) | 1.15 (0.97–1.37) |
| Biology (bioRxiv, trend from 2018) | 12.4% | 0.91 (0.78–1.06) | 0.92 (0.75–1.12) | 0.91 (0.71–1.15) |
| Biomedicine (PubMed, quarterly) | 5.6% | 0.90 (0.85–0.96) | 0.95 (0.88–1.02) | 0.93 (0.86–1.01) |
| Medicine (medRxiv without COVID-19)ᵃ | 48.1% | 0.74 (0.57–0.97) | 0.60 (0.42–0.88) | 0.48 (0.29–0.77) |

Ratio of observed to trend-expected counts (95% CI), from Poisson pseudo-maximum-likelihood models with a linear trend, calendar-month effects and an indicator for April 2020 to March 2021, fitted to pre-2023 data from 2015 (arXiv), 2018 (bioRxiv) or 2019 (medRxiv); Newey–West intervals. The counterfactual is each series' own extrapolated trend, not a level shared across series. New submissions; for list entries, see the text. ᵃ Trend dominated by the adoption of a new server; not interpreted. Archives, 2026: math-ph 1.81, nucl-th 1.58, quant-ph 1.54, nlin 1.52, math 1.48, hep-lat 1.39, hep-ex 1.37, astro-ph 1.34, stat 1.33, cond-mat 1.30, hep-ph 1.28, hep-th 1.28, gr-qc 1.26, q-bio 1.26, cs 1.15, physics 1.06, q-fin 1.03, nucl-ex 1.00; the largest departures are in archives whose pre-2023 trend was falling (math-ph −4.3%, nucl-th −2.5% and nlin −1.1% a year).

These departures compare each series with its own extrapolated trend, and bioRxiv's trend of 12% a year was fitted to years in which the server was still being adopted; in levels, bioRxiv grew more than the physics archives tested. Compared directly with bioRxiv in the event-study model, C1's six archives gained 7% from 2025 to 2026 (1.07; 0.99–1.16), as much as in 2021 and 2022, experiment 2% (1.02; 0.93–1.11) and mathematics 27% (1.27; 1.04–1.56), which is not unusual by rank among its six earlier year-on-year changes (two-sided p = 0.29; floor 0.14) [CONFIRM: companion item 3].

Break tests put the largest slope change of the physics series in May 2025 (p = 0.001), and those of C1's six archives and of mathematics at January 2026, the last admissible month; computer science, bioRxiv and the physics contrast showed no detectable slope break (p = 0.34, 0.17 and 0.56). The synthetic control replicated Nee et al.'s figure for mathematics [14], 11.9% above the counterfactual in January–September 2026 (exponentiated mean monthly log gap; rank p = 0.05, the floor), but the gap was near zero until April and about 8% without September; it measures mathematics' excess over an accelerating arXiv, not an effect of AI. A PubMed comparison by US affiliation is uninformative: the query misses about a quarter of articles from large US institutions, at a rate that drifts, and the 2026 value is not unusual for the series (rank p = 0.20; S5 Table).

### Paper-level evidence in particle and nuclear physics (exploratory)

INSPIRE-HEP queries made by an AI agent during internal review found that hep-ex records with at most 10 authors and no collaboration nearly doubled from January–September 2024 to the same months of 2026 (187 to 366; S2 Appendix), which motivated the paper-level tests. The companion analysis then classified all 117,950 INSPIRE records of 2017–2026 in six particle and nuclear physics archives (hep-lat in place of C1's gr-qc), from curated metadata and without AI, by the rule registered for this exploratory component (S1 Text): papers reporting new experimental results are research articles in an experimental category, linked to an experiment or collaboration and without prospect wording. The rule mostly separates collaboration papers from small-team papers and proceedings: in hep-ex and nucl-ex, 97–98% of records with more than 300 authors are in the new-results class and 97–98% of those with at most 10 authors are not [CONFIRM: companion item 9]. Against 2017–2022 trends the two classes stood at similar levels in 2026 (ratio 1.00; 0.74–1.35, from separate fits), but with the estimator of C1–C3 the ratio depends on the base years and moves in opposite directions in the two archives. Three modes of production moved differently: small-team research articles without an experiment link grew about fivefold in hep-ex from 2017–2019, a rise under way before 2023; collaboration papers rose with new data, such as the LHC's Run 3 samples; and mid-size collaborations and nucl-ex stayed flat [CONFIRM: companion item 9]. INSPIRE's planning-paper flag misses about half of hep-ex's Snowmass papers, and author counts of 0, for collaboration papers whose author lists are not yet loaded, must be treated as missing [ANALYSIS PENDING: companion item 9 (INSPIRE redo)]. The analysis therefore neither supports nor refutes the refined hypothesis.

### Pre-specified paper-level tests

The classifier agreed with my coding at κ = [SEALED: κ (95% CI)] for arXiv, [SEALED] for bioRxiv and [SEALED] for medRxiv, and repeated runs of the classifier agreed at κ = [SEALED] (S1 Text). Relative to their 2017–2022 trends, papers without new data in cond-mat, astro-ph and quant-ph stood at [SEALED] in January 2025–September 2026 and papers with new data at [SEALED], a ratio of [SEALED] (95% CI [SEALED]; minimum detectable ratio [SEALED]), above 1 in [SEALED] of the three archives, and [SEALED] against pooled base years. By the registered rule, HN was [SEALED: supported / not supported / contradicted]. On bioRxiv and medRxiv, which were not held out, the ratios were [SEALED] and [SEALED] (level-based [SEALED] and [SEALED]), so HN-bio was [SEALED] and HN-med [SEALED]. Across categories, the slope of the departure from trend on the share of papers with new data was [SEALED] (one-sided permutation p = [SEALED]) in the primary set and [SEALED] in the sampling design's set, so HN-dose was [SEALED]. Holm-adjusted across the four hypotheses, the p values were [SEALED] (S5 Table).

## Discussion

### Principal findings

None of the three pre-specified within-field contrasts supported H1, with the planned specification or as first reported; only biology's, against extrapolated pre-2023 trends, favoured it. The exploratory paper-level analysis in particle and nuclear physics could neither support nor refute its refinement, and the pre-specified paper-level tests [SEALED: one clause per hypothesis, by its registered rule and κ status]. Two descriptive findings held under the checks made. Growth was broad: every class of authors grew and the bottom 90% contributed about half of the increase, although in mathematics the top 1% grew fastest, partly because the ranking selects on 2026 output. Nearly all arXiv archives accelerated against their own pre-2023 trends in 2025–2026 while bioRxiv kept its pre-2023 pace, a contrast that depends on the counterfactual, since in levels bioRxiv grew more. As for output, the second clause of H1 does not describe the experimental particle-physics archive, whose output departed from its trend as much as the theory archives did, although nucl-ex did not; whether experimental work as such responded to AI cannot be determined from counts.

### What the within-field tests show

The contrasts were meant to hold preprint culture, platform and incentives fixed while varying the cost of the work beyond writing, but they also vary archive identity, collaboration structure and topic, and each depends on one component. Archive and category labels are weak proxies for experimental work: hep-ph is phenomenology fitted to data, gr-qc includes gravitational-wave experiments, genomics includes bench sequencing, arXiv keeps instrumentation and analysis methods out of hep-ex [50], and much of hep-ex analyses data already collected. The paper-level analysis in particle and nuclear physics avoids labels but not the last problem: its rule counts collaboration analyses of stored data as new results, and the registered codebook of the paper-level tests also classes data by who obtained them, not by whether a paper needed a new acquisition. Whichever way it went, the paper-level result bears on the unit of analysis: a supported HN would show that archive labels were the wrong unit, not that H1 was right. Qi et al.'s finding that computationally intensive fields benefited more [13] concerns the share of papers mentioning AI, not the volume of output, so these contrasts neither corroborate nor refute it; their post-ChatGPT acceleration on bioRxiv is a recovery from a fall after 2020 that, on their own estimates, left the slope below its pre-2020 level, consistent with bioRxiv's flat departure from trend here. Nee et al.'s mathematics result [14] replicates, but as an excess over an accelerating arXiv concentrated in a few months, and both author panels show rising concentration.

### Why might arXiv differ from bioRxiv?

The acceleration of arXiv against its own trend, absent on bioRxiv and in PubMed, is exploratory and confounds field with platform, the limitation that motivated the within-field design. Three explanations were checked and do not account for it. Genres that bioRxiv and medRxiv are not intended for [21,22] fell as shares of output in particle and nuclear physics, where research articles alone departed as much as all papers; removing the papers of planning exercises (Snowmass 2021; the European Strategy for Particle Physics in 2025) did not reduce hep-ex's departure; and dating by announcement [27], with moderators holding some submissions of heavy submitters before the October 2026 cap [12], explains at most a few per cent of the September 2026 spike in mathematics [CONFIRM: companion item 6]. Three remain open. (i) The 2025 disruption of US research funding (S2 Appendix) would depress US wet-lab output first, as in the 2026 wet-lab slowdown; a split of bioRxiv and medRxiv preprints by the country of the corresponding author, with the prediction stated first, is pending [ANALYSIS PENDING: companion item 10]. (ii) Facility cycles move experimental output: the LHC delivered record luminosity in 2024, and LHCb and BESIII completed large data sets that year (S2 Appendix), so the rise of collaboration papers in 2025–2026 may reflect data supply, which this study did not model. (iii) AI may have raised production across arXiv fields, including the analysis, simulation and methods work of experimentalists, more than in the fields that post on bioRxiv; the held-out test examines this in archives where the idea was not formed. Changes in who posts, as AI lowers language barriers, and in the propensity to post published work were not examined. The design cannot choose among these explanations.

### Implications for research evaluation

Two findings bear on research evaluation, whatever caused the growth. Preprint counts moved unevenly across servers in 2025–2026, by amounts that depend on the counterfactual and for reasons not yet attributable, so counts from these years should not be compared across servers or with earlier years without series-specific baselines; and the distribution of output among author names shifted at the same time, most in mathematics. If polished text can be produced cheaply, and published estimates find LLM-assisted writing in every field studied [47,51], form becomes a weaker cue of the quality of the work behind it; this is an interpretation, not a result of this study. Several institutions have responded by rationing: funders, servers and conferences introduced per-person limits on submissions, from NIH's six applications per investigator a year [11] to arXiv's two submissions per submitter a month [12] (S1 Table). Such caps limit volume; whether they preserve information about the work behind each item, or whether the growth in volume strains evaluators' capacity to read what they assess, has not been evaluated.

Others have proposed changing what is counted [52,53]. Blekhman asks the field to define evaluation from the goals of research, not from paper counts, but names no mechanism [23]. I propose one, which these data do not test: arXiv-type repositories could evolve into web-native articles that combine text with data, code, interactive visualisation and video, in which nothing is accepted or rejected, reviews are public, anyone can critique, and what is credited is the critique rather than the article. Each element has been tried, and the record shows where such a system strains. eLife stopped rejecting reviewed papers in 2023, lost its Journal Impact Factor, and received 55% fewer submissions in 2025 than in 2024 [54]. Unsolicited critique is rare: 5% of authors joined Nature's 2006 open-review trial [55], PubMed Commons closed after comments on 6,000 of 28 million articles [56], and 7.3% of 2020 bioRxiv and medRxiv preprints drew a comment [57]. AI makes critique cheap: an estimated 21% of reviews at one 2026 machine-learning conference were fully AI-generated [58], and another conference generated a review for each of its 22,977 papers in under a day [59]. Credited critiques would inflate as papers have. What should be credited is therefore verification with consequences, such as reproductions, which have earned conventional credit at scale [60], and errors confirmed and corrected. Data and code attached to the text make that verification cheaper, the mirror image of this paper's thesis.

### Limitations

The design is observational and has no measure of exposure to AI: the treatment is the calendar year, which bundles AI capabilities with platform rules and moderation, funding, facility cycles and server-specific dynamics, and within-field differencing removes only shocks that hit both groups in proportion. With the marker withdrawn, the study does not measure AI-assisted writing either. The contrasts were chosen after descriptive growth had been seen, the estimates first reported departed from the plan, and the genre, planning-paper and paper-level analyses were made after the results were known. The tests could not detect rate ratios below 1.11–1.18 even with within-period uncertainty only, every contrast depends on one archive or category, and the placebos are not yet matched to each contrast's structure. Archive sums double-count aliased papers, arXiv's metadata describe each paper's latest version, bioRxiv categories are chosen by authors and include COVID-19 preprints, the regular expressions and genre keywords are unvalidated, duplicate records were removed from the medRxiv series late in the analysis, and journal-side changes, such as a pre-screen for Mendelian randomisation studies at PLOS ONE from April 2024 [61], can move PubMed and medRxiv series. Author-level measures rest on name strings, with histories from 2019 only, and cover arXiv only. The paper-level tests rest on a single human coder who formed the hypothesis, on labels whose errors the intervals do not carry, on a validation frame limited to openly licensed bioRxiv and medRxiv preprints, and on a proprietary classifier [SEALED: κ status of each domain]. arXiv's cap of two submissions per submitter a month, from October 2026, breaks the continuity of its series, and any extension must model it. Preprints are not publications. Finally, the article and all its code were produced with AI assistance under my direction (Methods); independent checks agree with the counts where available, but not for every series.

## Conclusions

Pre-specified within-field tests did not show that preprint output in the generative-AI era grew faster in non-experimental than in experimental work: the physics contrast was inconclusive, the biology contrast null against the planned baseline but dependent on the counterfactual, and the medicine contrast null. [SEALED: one sentence on the pre-specified paper-level tests, by their registered rules.] Against their own pre-2023 trends, arXiv physics and mathematics accelerated in 2025–2026, the experimental particle-physics archive (hep-ex) included but not nucl-ex, while bioRxiv and PubMed did not, and output grew in every class of authors, most unevenly in mathematics. These data cannot attribute the changes to generative AI, but they show that preprint counts from 2026 should not be compared with those of earlier years, or across servers, without adjustment.

## Acknowledgments

[AUTHOR: acknowledgements, e.g. anyone who read the draft, checked the code or coded validation papers.] This work used arXiv's open-access interoperability and data from the US National Library of Medicine, bioRxiv, medRxiv and INSPIRE-HEP; none of them endorses it.

## References

1. Moher D, Naudet F, Cristea IA, Miedema F, Ioannidis JPA, Goodman SN. Assessing scientists for hiring, promotion, and tenure. PLoS Biol. 2018;16(3):e2004089. doi:10.1371/journal.pbio.2004089
2. [AUTHOR: surname initials]. The cost was the signal: why academic evaluation is not ready for AI used well [Preprint]. Zenodo. 2026. doi:[to be minted]
3. Sokal AD. Transgressing the boundaries: toward a transformative hermeneutics of quantum gravity. Soc Text. 1996;(46/47):217–252. doi:10.2307/466856
4. Bohannon J. Who's afraid of peer review? Science. 2013;342(6154):60–65. doi:10.1126/science.342.6154.60
5. Labbé C, Labbé D. Duplicate and fake publications in the scientific literature: how many SCIgen papers in computer science? Scientometrics. 2013;94(1):379–396. doi:10.1007/s11192-012-0781-y
6. Van Noorden R. Publishers withdraw more than 120 gibberish papers. Nature. 2014 Feb 24. doi:10.1038/nature.2014.14763
7. Kusumegi K, Yang X, Ginsparg P, de Vaan M, Stuart T, Yin Y. Scientific production in the era of large language models. Science. 2025;390(6779):1240–1243. doi:10.1126/science.adw3000
8. Bornmann L, Haunschild R, Mutz R. Growth rates of modern science: a latent piecewise growth curve approach to model publication numbers from established and new literature databases. Humanit Soc Sci Commun. 2021;8:224. doi:10.1057/s41599-021-00903-w
9. Hanson MA, Gómez Barreiro P, Crosetto P, Brockington D. The strain on scientific publishing. Quant Sci Stud. 2024;5(4):823–843. doi:10.1162/qss_a_00327
10. Gartenberg C, Hasan S, Murray A, Pierce L. More versus better: artificial intelligence, incentives, and the emerging crisis in peer review. Organ Sci. 2026;37(3):795–812. doi:10.1287/orsc.2026.ed.v37.n3
11. National Institutes of Health. NOT-OD-25-132: Supporting fairness and originality in NIH research applications [Internet]. 17 Jul 2025 [cited 2026 Oct 16]. Available from: https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html
12. Boboris K. Fair moderation, equitable access, and AI: arXiv's updated rate limit policy [Internet]. arXiv blog; 1 Oct 2026 [cited 2026 Oct 17]. Available from: https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/
13. Qi M, Cao Z, Wang Q, Li N, Zhu T. Does GenAI rewrite how we write? An empirical study on two-million preprints [Preprint]. arXiv:2510.17882. 2025 [cited 2026 Oct 16]. Available from: https://arxiv.org/abs/2510.17882
14. Nee X, Zhong H, Ni X. The generative AI gold rush in theoretical and computational research [Preprint]. arXiv:2609.04872v1 [cs.DL]. 2026 [cited 2026 Oct 16]. Available from: https://arxiv.org/abs/2609.04872
15. Larivière V, Sugimoto CR, Macaluso B, Milojević S, Cronin B, Thelwall M. arXiv e-prints and the journal of record: an analysis of roles and relationships. J Assoc Inf Sci Technol. 2014;65(6):1157–1169. doi:10.1002/asi.23044
16. Abdill RJ, Blekhman R. Tracking the popularity and outcomes of all bioRxiv preprints. eLife. 2019;8:e45133. doi:10.7554/eLife.45133
17. Wang Z, Chen Y, Glänzel W. Preprints as accelerator of scholarly communication: an empirical analysis in mathematics. J Informetr. 2020;14(4):101097. doi:10.1016/j.joi.2020.101097
18. Krumholz HM, Bloom T, Sever R, Rawlinson C, Inglis JR, Ross JS. Submissions and downloads of preprints in the first year of medRxiv. JAMA. 2020;324(18):1903–1905. doi:10.1001/jama.2020.17529
19. Fraser N, Brierley L, Dey G, Polka JK, Pálfy M, Nanni F, et al. The evolving role of preprints in the dissemination of COVID-19 research and their impact on the science communication landscape. PLoS Biol. 2021;19(4):e3000959. doi:10.1371/journal.pbio.3000959
20. Sever R, Hindle S, Roeder T, Fereres S, Fernández Gayol O, Ghosh S, et al. bioRxiv: the preprint server for biology [Preprint]. bioRxiv. 2019. doi:10.1101/833400
21. bioRxiv. Frequently asked questions [Internet]. Cold Spring Harbor Laboratory [cited 2026 Oct 16]. Available from: https://www.biorxiv.org/about/FAQ
22. medRxiv. About medRxiv [Internet] [cited 2026 Oct 16]. Available from: https://www.medrxiv.org/content/about-medrxiv
23. Blekhman R. What is biology research for? PLoS Biol. 2026;24(10):e3004075. doi:10.1371/journal.pbio.3004075
24. Ioannidis JPA, Klavans R, Boyack KW. Thousands of scientists publish a paper every five days. Nature. 2018;561(7722):167–169. doi:10.1038/d41586-018-06185-8
25. Ioannidis JPA, Collins TA, Baas J. Evolving patterns of extreme publishing behavior across science. Scientometrics. 2024;129(9):5783–5796. doi:10.1007/s11192-024-05117-w
26. arXiv. Yearly submission statistics, one page per archive and year (for example, hep-th in 2025) [Internet] [cited 2026 Oct 16]. Available from: https://arxiv.org/year/hep-th/2025
27. arXiv. Availability of submissions [Internet] [cited 2026 Oct 16]. Available from: https://info.arxiv.org/help/availability.html
28. bioRxiv, medRxiv. bioRxiv and medRxiv API [Internet] [cited 2026 Oct 16]. Available from: https://api.biorxiv.org/
29. bioRxiv. Content statistics: new papers per year and per month [Internet]. Cold Spring Harbor Laboratory [cited 2026 Oct 16]. Available from: https://api.biorxiv.org/sum/y and https://api.biorxiv.org/sum/m
30. Sayers E. A general introduction to the E-utilities. 2009 May 26 [updated 2022 Nov 17]. In: Entrez Programming Utilities Help [Internet]. Bethesda (MD): National Center for Biotechnology Information (US); 2010– [cited 2026 Oct 17]. Available from: https://www.ncbi.nlm.nih.gov/books/NBK25497/
31. INSPIRE-HEP. REST API documentation [Internet] [cited 2026 Oct 16]. Available from: https://github.com/inspirehep/rest-api-doc
32. Suchak T, Aliu AE, Harrison C, Zwiggelaar R, Geifman N, Spick M. Explosion of formulaic research articles, including inappropriate study designs and false discoveries, based on the NHANES US national health database. PLoS Biol. 2025;23(5):e3003152. doi:10.1371/journal.pbio.3003152
33. Spick M, Onoja A, Harrison C, Stender S, Byrne J, Geifman N. Quantifying new threats to health and biomedical literature integrity from rapidly scaled publications and problematic research. J Clin Epidemiol. 2026;193:112203. doi:10.1016/j.jclinepi.2026.112203
34. Milojević S. Accuracy of simple, initials-based methods for author name disambiguation. J Informetr. 2013;7(4):767–773. doi:10.1016/j.joi.2013.06.006
35. Kim J, Diesner J. Distortive effects of initial-based name disambiguation on measurements of large-scale coauthorship networks. J Assoc Inf Sci Technol. 2016;67(6):1446–1461. doi:10.1002/asi.23489
36. Newey WK, West KD. A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. Econometrica. 1987;55(3):703–708. doi:10.2307/1913610
37. Cameron AC, Trivedi PK. Regression-based tests for overdispersion in the Poisson model. J Econom. 1990;46(3):347–364. doi:10.1016/0304-4076(90)90014-K
38. Driscoll JC, Kraay AC. Consistent covariance matrix estimation with spatially dependent panel data. Rev Econ Stat. 1998;80(4):549–560. doi:10.1162/003465398557825
39. Bertrand M, Duflo E, Mullainathan S. How much should we trust differences-in-differences estimates? Q J Econ. 2004;119(1):249–275. doi:10.1162/003355304772839588
40. Holm S. A simple sequentially rejective multiple test procedure. Scand J Stat. 1979;6(2):65–70.
41. Santos Silva JMC, Tenreyro S. The log of gravity. Rev Econ Stat. 2006;88(4):641–658. doi:10.1162/rest.88.4.641
42. Conley TG, Taber CR. Inference with "difference in differences" with a small number of policy changes. Rev Econ Stat. 2011;93(1):113–125. doi:10.1162/rest_a_00049
43. Abadie A, Diamond A, Hainmueller J. Synthetic control methods for comparative case studies: estimating the effect of California's tobacco control program. J Am Stat Assoc. 2010;105(490):493–505. doi:10.1198/jasa.2009.ap08746
44. Andrews DWK. Tests for parameter instability and structural change with unknown change point. Econometrica. 1993;61(4):821–856. doi:10.2307/2951764
45. Willroth EC, Atherton OE. Best laid plans: a guide to reporting preregistration deviations. Adv Methods Pract Psychol Sci. 2024;7(1):25152459231213802. doi:10.1177/25152459231213802
46. Lakens D. When and how to deviate from a preregistration. Collabra Psychol. 2024;10(1):117094. doi:10.1525/collabra.117094
47. Kobak D, González-Márquez R, Horvát EÁ, Lause J. Delving into LLM-assisted writing in biomedical publications through excess vocabulary. Sci Adv. 2025;11(27):eadt3813. doi:10.1126/sciadv.adt3813
48. Geng M, Trotta R. Human-LLM coevolution: evidence from academic writing. In: Findings of the Association for Computational Linguistics: ACL 2025. 2025. p. 12689–12696. doi:10.18653/v1/2025.findings-acl.657
49. Palmer A, Smith NA, Spirling A. Using proprietary language models in academic research requires explicit justification. Nat Comput Sci. 2024;4:2–3. doi:10.1038/s43588-023-00585-1
50. arXiv. Category taxonomy [Internet] [cited 2026 Oct 16]. Available from: https://arxiv.org/category_taxonomy
51. Liang W, Zhang Y, Wu Z, Lepp H, Ji W, Zhao X, et al. Quantifying large language model usage in scientific papers. Nat Hum Behav. 2025;9(12):2599–2609. doi:10.1038/s41562-025-02273-8
52. Huang G, Hu X, Zhang P, Lin Z. AI can widen science — but only if institutions stop rewarding the already measurable. Nature. 2026;658:32–33. doi:10.1038/d41586-026-02961-z
53. Hosseini M, Earp BD, Porsdam Mann S, Holmes K. Generative AI can and should accelerate research evaluation reform to better recognize 'distinctly human contributions'. Res Eval. 2026;35:rvag020. doi:10.1093/reseval/rvag020
54. Rodgers P, Pattinson D. The eLife Model: three-year update [Internet]. Cambridge (UK): eLife Sciences Publications; 2026 Mar 17 [cited 2026 Oct 17]. Available from: https://elifesciences.org/inside-elife/7da92a51/the-elife-model-three-year-update
55. Campbell P, et al. Report of Nature's peer review trial [Internet]. London: Nature Publishing Group; 2006 Dec 20 [cited 2026 Oct 17]. Available from: https://blogs.nature.com/blog/report_of_natures_peer_review_trial/
56. National Center for Biotechnology Information. PubMed Commons to be discontinued [Internet]. Bethesda (MD): NCBI; 2018 Feb 1 [updated 2018 Feb 27; cited 2026 Oct 17]. Available from: https://ncbiinsights.ncbi.nlm.nih.gov/2018/02/01/pubmed-commons-to-be-discontinued/
57. Carneiro CFD, da Costa GG, Neves K, Abreu MB, Tan PB, Rayêe D, et al. Characterization of comments about bioRxiv and medRxiv preprints. JAMA Netw Open. 2023;6(8):e2331410. doi:10.1001/jamanetworkopen.2023.31410
58. Naddaf M. Major AI conference flooded with peer reviews written fully by AI. Nature. 2025;648(8093):256–257. doi:10.1038/d41586-025-03506-6
59. Biswas J, Schoepp S, Vasan G, Opipari AW, Zhang A, Hu Z, et al. AI-assisted peer review at scale: the AAAI-26 AI review pilot [Preprint]. arXiv:2604.13940. 2026 Apr 15 [cited 2026 Oct 17]. doi:10.48550/arXiv.2604.13940
60. Brodeur A, Mikola D, Cook N, Fiala L, Brailey T, Briggs R, et al. Reproducibility and robustness of economics and political science research. Nature. 2026;652(8108):151–156. doi:10.1038/s41586-026-10251-x
61. Pruller J, Mockridge J, Vousden G. Expectations for Mendelian randomization research in PLOS One. PLoS One. 2025;20(11):e0337199. doi:10.1371/journal.pone.0337199

## Supporting information

**S1 Appendix. AI use and verification record.** For each task, the tool, the author's role, how the output was checked and its status, including the classifier runs of the paper-level tests and the author's validation coding; the code-review and re-run log; the reading depth for the references of this article; time and cost; and the archived project history.

**S2 Appendix. Definitions, regular expressions, queries, terms of use and dated events.** Archives and categories in each group; the two arXiv mathematics series; normalisation of author names, the namesake-robust variant and the H2 variants; the regular expressions; the sensitivity and exploratory analyses; the synthetic control and break tests; terms of use and request rates for each source; the INSPIRE-HEP queries behind the exploratory observation in hep-ex; and a dated timeline of server policies, facility schedules and data releases, planning exercises and funding events, with sources.

**S1 Text. Analysis plan for the paper-level tests (time-stamped in the project's public repository).** The plan (commit 763aa2b) and its Amendment 1 (commit 78890e5), with the codebooks and classifier prompts, as activated on 16 October 2026; Deviations 1 and 2 (commits 11264ee and 1de63a9); Deviation 3 with its two addenda and the erratum (commits 8932773, 80a2ef2 and 6e1c119, 17 October 2026); and the run instruction of the classifier.

**S1 Table. Per-person limits on submissions, 2025–2026.** Caps, gates and quotas introduced by funders, preprint servers, journals and conferences, with their stated reasons and primary sources.

**S2 Table. Growth by arXiv archive and by bioRxiv and medRxiv category.** January–September counts and year-on-year growth, 2017–2026 (bioRxiv and medRxiv from 2019), with 2017–2025 ranges, the yearly change in the log ratio of each contrasted pair, and COVID-19 and public-dataset shares. [ANALYSIS PENDING: companion item 4 (assemble S2 Table)]

**S3 Table. Descriptive heavy-producer measures.** arXiv mathematics, third quarters of 2025 and 2026, and arXiv physics theory and experiment, 2022–2026, under each author-matching rule; cells describing fewer than ten authors are suppressed.

**S4 Table. Published estimates of LLM-assisted writing by field.** Literature context; this study runs no marker analysis of its own. The measures differ, so only rankings within a study are comparable.

**S5 Table. All estimates.** The rows moved from Table 1 (acceleration, slope changes, trend-adjusted estimates, the year-shock ratio of v2, negative controls and variants of C1), the H2 decompositions by window and name variant, and the full set: event-study coefficients by year and base, placebo distributions, leave-one-out and sensitivity analyses, placebo dates, break tests, field and archive departures from trend (new submissions and list entries), comparisons of arXiv groups with bioRxiv, the synthetic control, the PubMed check, the genre split, the medRxiv flag variants and the INSPIRE-HEP classes, with the analyses tried and dropped and the reasons. [ANALYSIS PENDING: companion item 4 (assemble S5 Table as a spreadsheet with a README)]

**S6 Table. Deviations from the analysis plans.** For each departure from the plan in v1 and from the plan of the paper-level tests (S1 Text): what was planned, what was done, when it was recorded (commit and UTC time), what had been seen by then, the reason and the expected effect on inference.

**S1 Data. Data and code.** The deposit described under Data availability (Zenodo, doi:[AUTHOR: DOI]).

<!-- SUBMISSION FORM START -->

## Statements for the submission form (not part of the manuscript file)

<!-- PLOS ONE collects these in its submission system, not in the manuscript file. Kept here so that the author can review them with the article. -->

### Funding

[AUTHOR: e.g. "The author received no specific funding for this work." State who paid for the AI tool subscription or API use. The article-processing charge falls under EMBL's flat-fee agreement with PLOS; confirm whether it needs mentioning.]

### Competing interests

I have no financial relationship with Anthropic or any other developer of AI tools [AUTHOR: confirm; state who paid for the Claude subscription or API use, and whether any credits were received from Anthropic]. I used Anthropic's Claude, via Claude Code, to draft this article and to write its analysis code, and a Claude model classified the papers of the paper-level tests (Methods, Use of AI tools). Because the article studies changes in scientific output in the period in which such tools became available, I declare this use as a potential non-financial competing interest. Anthropic had no role in the study design, data collection and analysis, decision to publish or preparation of the manuscript, beyond the use of its commercially available products. [AUTHOR: align this declaration with the Zenodo essay and any Correspondence, which discuss Anthropic's data policy.]

### Data availability

All data and code are available from Zenodo (doi:[AUTHOR: DOI of the tagged release]). The deposit is a tagged release of the project repository. It contains: monthly counts of new preprints by arXiv archive (new submissions and list entries, 2010–2026), by bioRxiv subject category and for medRxiv (2019–2026), and PubMed quarterly counts, with retrieval dates; record-level tables of identifiers with derived variables, without names, for arXiv (identifier, identifier month, first-version date where known, latest-version date, primary category, number of authors, genre and planning-paper flags), medRxiv (DOI, date, category, country of the corresponding institution, COVID-19 and public-dataset flags) and INSPIRE-HEP (curated fields), and for bioRxiv [ANALYSIS PENDING: companion item 4 (bioRxiv record table)]; for the paper-level tests, after unsealing, the samples, both sets of classifier labels, the run records, the prompts and run instruction, and the validation sheet with my codes and its key; the values behind every figure and table and the output of every model, including the withdrawn marker analysis (marker_tests.json and marker_growth_panel.csv); and the scripts that harvest, process and analyse the data, which reproduce the count-based figures and estimates with fixed random seeds. The author-level analyses (Fig 3, S3 Table) need the arXiv OAI-PMH harvests, which contain names and are not deposited; they can be reproduced from the public CC0 source with the deposited list of records and the code. No author names are redistributed. The medRxiv flag coding sheet includes titles, and the validation sheet of the paper-level tests republishes the titles and abstracts of Creative Commons-licensed bioRxiv and medRxiv preprints, with attribution, once the coding is finished. [AUTHOR: decide on a pseudonymised author–paper table after the data-protection consultation, or state why it is withheld and name a non-author contact for access.] Source metadata are public (arXiv statistics pages and OAI-PMH, under CC0; the bioRxiv and medRxiv API; PubMed E-utilities; the INSPIRE-HEP API, mostly under CC0) and were retrieved in October 2026; earlier retrievals from arXiv's statistics pages and the OSF API ran faster than those sources' stated limits, and the deposited scripts follow them. Licences: CC BY 4.0 for the data, or CC0 for tables derived from CC0 sources, and MIT for the code [AUTHOR: confirm]; the word list of Kobak et al. keeps its MIT licence.

### Author contributions (CRediT)

[AUTHOR: full name]: Conceptualization; Methodology (adoption and modification of AI-proposed designs) [AUTHOR: confirm]; Investigation (direction and verification of the literature search and the companion analysis); Formal analysis (direction and review of AI-written code) [AUTHOR: confirm]; Validation (blind coding of the classifier's validation sample) [AUTHOR: confirm]; Visualization (direction); Writing – review & editing; Project administration. AI tools are not contributors under CRediT; their use is described in Methods.

<!-- SUBMISSION FORM END -->

<!-- SI FILES START -->

<!-- SI FILE: S1 Appendix -->

## S1 Appendix. AI use and verification record

*A separate Supporting Information file at submission. It covers this article and its companion analysis only. Times are UTC, from the project repository; push times are those recorded by GitHub. Items marked [AUTHOR] must be completed by the author.*

**Timeline.**

- 16 October 2026, 16:42: skeleton with hypotheses H1–H3 and the three contrasts committed (2cac071), after the groups' descriptive growth had been computed.
- 17:27: v1, with the analysis plan drafted by an AI agent, committed (697fb25).
- 17:43, 18:08, 18:19, 18:47 and 19:22: formal results of the companion analysis added to the repository (companion commits 37b4b11, f5ab16e, 7ac5647, 26ce2eb and 0e239cd); the specification of the contrasts arrived with the first of them.
- 18:00–18:15: four internal reviews written by AI agents in reviewer roles (statistics, scientometrics, experimental science, journal editor); they are not peer review.
- 18:28 and 18:47: plan of the paper-level tests and its Amendment 1, approved by the author, committed (763aa2b and 78890e5); 18:48 and 18:55: Deviations 1 and 2 (11264ee and 1de63a9); 19:01: the sampling design (companion c2f891b).
- 23:39: v2 (a17a8b9). 23:43: the first, date-ordered classifier runs (900 medRxiv sample papers and the 200 bioRxiv and medRxiv validation papers) superseded by blind runs, and the Test A decision rule fixed in code (companion 8ab4d9d).
- 17 October, 00:11: the Test A (medRxiv) estimate computed and committed (companion dacd064); at about 00:12 the analysis session reported it in its chat with the author; at 00:15 the coordinating session asked for a hold on further estimates.
- 08:07, 08:14 and 08:18: Deviation 3, its addendum and its second addendum committed (8932773, 80a2ef2 and 6e1c119); 08:15: the author's decisions to withdraw the marker metric and to propose a publishing mechanism logged (116910b).
- [AUTHOR: time and commit of the validation coding (validation/author_labels.csv), of unsealing, and of this v3.]

**Tasks.**

| Task | Done by | Author's role | How the output was checked | Status |
|---|---|---|---|---|
| Literature search; reference checks | AI agents | Directed [AUTHOR: confirm] | Identifiers and metadata of added references read from Crossref, arXiv or the publisher by AI agents | Each source cited for a number, quotation or method to be read by the author [AUTHOR] |
| Hypotheses | Author (H1; refined hypothesis of the paper-level tests); AI agents (wording; H2, H3) [AUTHOR: confirm] | Originated or adopted | Recorded before modelling (commit 2cac071) | Done |
| Group definitions; analysis plan; statistical specification | AI agents | Adopted or modified [AUTHOR: specify] | Deviations listed in S6 Table | Done |
| Harvesting, processing, statistics and figure code | AI agents, in a separate session | Directed [AUTHOR: code review] | Agreement with bioRxiv's official totals and arXiv's statistics for hep-th and hep-ph; a re-run in internal review reproduced the committed outputs; [AUTHOR: own re-runs] | Pipeline reproduces the count-based outputs from committed data |
| Marker analysis (H3) | AI agents, in the companion session | Withdrew the measure (17 Oct) | Not reported; results deposited | Withdrawn |
| Country classifier for the funding splits | AI agents | – | 150 classified records checked by an AI agent, not by a person | Not used in this article; a person's check is needed before use |
| Drafting and revision of the text (v1–v3) | AI agents | Decisions recorded in the project brief and critique log; [AUTHOR: own revision] | [AUTHOR] | In progress |
| Internal reviews (four roles, two rounds) | AI agents | Read the reviews and decided the responses | Not peer review | Rounds 1 and 2 done |
| INSPIRE-HEP queries and sample classification (hep-ex) | AI agent in a reviewer role | – | Not validated; superseded by the rule-based classification | Reported as motivation only |
| INSPIRE-HEP classification of all records (exploratory component of the plan) | Rule proposed by the author; code by AI agents in the companion session | Proposed the component; approved the registered rule | Curated metadata, no AI classification; no human check of the classes [AUTHOR: spot-check about 100 records] | Redo pending (companion item 9) |
| Classifier of the paper-level tests | Claude Code sub-agents ([AUTHOR: model and version]) with fixed prompts, in batches of 50 | Approved the plan and deviations | Agreement with the author's blind coding of 400 papers (κ ≥ 0.60 per domain); agreement between repeated runs | Estimates sealed until the coding is committed |
| First, date-ordered classifier runs (D3a) | AI agents in the companion session | – | Superseded by blind runs; used only to measure agreement between runs | Done |
| Validation coding of 400 papers | Author | – | Blind to dates, servers and labels; the medRxiv part possibly not blind to the Test A (medRxiv) estimate | [AUTHOR: date and commit] |
| medRxiv flag coding (200 rows) | [AUTHOR] | – | Precision of the public-dataset and COVID-19 expressions | Pending |

**Run records.** [AUTHOR: for each classifier run, from the run logs: model identifier, time, hash of the batch file and tools used, and whether any tool was used other than reading the batch and writing labels.]

**Code review and re-runs.** [AUTHOR: what you reviewed, with commit hashes.]

**Reading depth.** [AUTHOR: for each reference cited for a number, a quotation or a method, how it was read (in full, as a primary document, abstract only).]

**Time and cost.** [AUTHOR: compute cost of this article and its companion analysis; your own hours by phase.]

**Tool and account.** Claude (Anthropic), via Claude Code [AUTHOR: model and version of the main sessions and of the classifier], on a [AUTHOR: account type] account with model training [AUTHOR: on/off]. [AUTHOR: why a proprietary model was used.]

**Archive.** The repository history, with the commits above, will be archived on Zenodo with the data (doi:[AUTHOR]) after a check for personal data, third-party text and files the author does not want public.

<!-- SI FILE: S2 Appendix -->

## S2 Appendix. Definitions, regular expressions, queries, terms of use and dated events

*A separate Supporting Information file at submission.*

**Physics.** The physics field series sums 13 arXiv archives: astro-ph, cond-mat, gr-qc, hep-ex, hep-lat, hep-ph, hep-th, math-ph, nlin, nucl-ex, nucl-th, physics and quant-ph. The physics archive includes physics.ins-det (instrumentation and detectors) and physics.data-an (data analysis). Contrast C1: theory = hep-th, hep-ph, gr-qc and nucl-th; experiment = hep-ex and nucl-ex; the other archives, including hep-lat, are in neither group. "C1's six archives" are these six; the INSPIRE-HEP analysis uses hep-ex, hep-ph, hep-th, hep-lat, nucl-ex and nucl-th ("INSPIRE's six archives"). The aliased pairs are math-ph/math.MP, cs.IT/math.IT, cs.NA/math.NA, math.ST/stat.TH, eess.SY/cs.SY and econ.GN/q-fin.EC.

**Mathematics.** Two series are used. The statistics pages' "math" count (Fig 1, Table 2, the synthetic control and the archive ranking) includes papers whose primary category is an alias with a canonical name outside mathematics; the OAI-PMH series of papers with a primary math.\* category (H2, the genre split and the September 2026 count of 8,360) is 89.9% of it in January–September 2019 and 92.3% in 2026, and the two grew alike from 2025 to 2026 (+43.2% and +43.3%).

**Revision.** The OAI-PMH metadata (comments, author lists, categories) describe each paper's latest version. Recent papers have had less time to be revised, so labels added or removed at revision, such as a journal reference or "accepted at", change with a paper's age.

**bioRxiv.** Computational: bioinformatics, genomics, systems biology. Wet lab: biochemistry, cancer biology, cell biology, developmental biology, immunology, microbiology, molecular biology, pathology, pharmacology and toxicology, physiology, plant biology, synthetic biology. Mixed: animal behavior and cognition, bioengineering, biophysics, ecology, evolutionary biology, genetics, neuroscience, paleontology, scientific communication and education, zoology. Epidemiology and clinical trials, which moved to medRxiv in 2019, cannot be queried by category, so category sums are about 4% below bioRxiv's totals in January–June 2019 and equal to them from July 2019. A record-level harvest of 2019–2026 found 313,165 version-1 listings and 313,161 unique DOIs.

**medRxiv.** The public-dataset list shares FAERS, NHANES, UK Biobank, the Global Burden of Disease study and MIMIC with the nine datasets of Spick et al. [1], and lacks FinnGen, CHARLS, CDC WONDER and TriNetX; it adds Mendelian randomisation, SEER and BRFSS. With the four missing datasets added, 48 further non-COVID preprints were flagged in January–September 2026 (922 against 874). The medRxiv API lists some version-1 preprints twice; the share of duplicate listings stayed below 0.5% until late 2025 and rose in 2026, most in July and August. Every series counts each DOI once; so counted, COVID-19 preprints were 68% of new medRxiv preprints in January–September 2020 and 5% in the same months of 2026.

**Regular expressions** (Python, case-insensitive; a record is flagged if the pattern matches at least once in the fields named). Their precision has not been measured; a coding sheet of randomly sampled flagged preprints has been prepared [AUTHOR: code it].

- *COVID-19 (medRxiv; title and abstract):* `covid|sars[\s-]*cov[\s-]*2|2019[\s-]*ncov|ncov[\s-]*2019|novel coronavirus|coronavirus disease 2019`. A title-only variant gives similar growth from January–September 2025 to the same months of 2026 (15.6%, against 16.4%) and a third-quarter 2026 index of 241 (2022 = 100), against 257.
- *Public datasets and designs (medRxiv; title and abstract):* `\bNHANES\b|national health and nutrition examination survey|uk[\s-]?biobank|global burden of disease|\bGBD\s?20\d\d\b|mendelian randomi[sz]ation|\bFAERS\b|adverse event reporting system|\bMIMIC-?(?:III|IV)\b|\bSEER\b|\bBRFSS\b`. "adverse event reporting system" also matches VAERS, and `\bSEER\b` matches the word "seer".
- *Planning papers (arXiv; title, abstract and comments):* "Snowmass", "European Strategy", "ESPP" or "strategy for particle physics".
- *Genres (arXiv; comments, title or abstract), checked in this order:* white paper (also Snowmass, European Strategy, roadmap, community input); proceedings (proceedings, conference, workshop, talk, contribution to, PoS, school); thesis; review (review, survey, lecture notes, tutorial, primer, chapter, handbook). Everything else is a research article. The proceedings and review patterns also match journal names in comments (for example "Proc. Natl. Acad. Sci." and "Physical Review"), so the review class in particular is not valid as built [ANALYSIS PENDING: companion item 11].

**Author names.** Names are normalised by Unicode decomposition, removal of accents, conversion to lower case and tokenisation. The namesake-robust variant keeps only names whose first part is a full given name and drops names whose surname is among the 1% most frequent. In physics, papers with more than 50 authors are excluded; with them, white papers signed by hundreds of theorists would make 16.9% of active theory authors heavy producers in the third quarter of 2025, against 1.3% without them. Authors tied at a class boundary in the decomposition share the remaining places equally. Experimental physics, with about 300 papers a quarter of at most 50 authors and few full first names, is analysed with all names only. A heavy producer has five or more papers in a group in a quarter, about 20 a year, far below the thresholds used for extreme output. The H2 decomposition is repeated for January–August windows (as in Nee et al.), for July and August only (without the September 2026 spike), for names already active in 2019–2024 (without newcomers, whom arXiv's endorsement rule of December 2025 affects most) and for list entries.

**Sensitivity and exploratory analyses** (estimates in S5 Table). Contrasts: hep-ph removed; genomics removed or moved to the wet-lab group; November 2025 to February 2026 dropped; the sample ended in October 2025; group-specific linear trends (a trend-adjusted estimate that cannot credibly be extrapolated from years shaped by COVID-19 and bioRxiv's adoption); acceleration as the 2026/2025 ratio and as changes in the slope of the deseasonalised log ratio after December 2022 and November 2024 (Newey–West intervals; parametric-bootstrap p values); negative controls (hep-ex against nucl-ex; pairs of theory archives). Exploratory: departures from trend by field and archive (new submissions and list entries); mathematics ranked among the 18 archives; arXiv groups against bioRxiv; PubMed journal articles with at least one affiliation matching `usa[ad] OR "united states"[ad]` against the rest (base 2023–2024); the synthetic control; break tests; planning-paper removal; the genre split (against 2019–2022 trends, the span of the paper-level harvest); and the INSPIRE-HEP classification.

**Synthetic control and break tests.** Mathematics' deseasonalised monthly log series was approximated by a convex combination of the 19 other archives with monthly data since 2018; 14 received positive weight (astro-ph 0.11, cond-mat 0.13, cs 0.01, gr-qc 0.09, hep-ex 0.01, hep-ph 0.09, hep-th 0.12, math-ph 0.12, nucl-ex 0.03, nucl-th 0.06, physics 0.09, q-fin 0.02, quant-ph 0.05, stat 0.08). The fit used January 2018 to December 2025 after demeaning; the 2026 gap is the mean log difference over January–September 2026, exponentiated and expressed as a percentage; and each donor in turn served as a placebo, with units ranked by the ratio of post- to pre-period fit error, so that with 20 units the smallest attainable rank p value is 0.05. A fit with the pre-period ending in November 2022 gave a gap of 10.1%. math-ph shares aliased papers with mathematics. For breaks, sup-Wald statistics for a change in the slope or level of each deseasonalised log series (fields) or log ratio (contrasts) were computed for every candidate month in the central 90% of the sample, so that the last candidate for arXiv was January 2026, with Newey–West Wald statistics and p values from 999 parametric-bootstrap draws of the no-break model with first-order autoregressive errors; Wald tests at December 2022, November 2024 and November 2025 used the same bootstrap. The first tests, with 15% trimming, could not place a break after December 2024 (arXiv) or August 2025 (bioRxiv and medRxiv) and are not used.

**Terms of use and request rates.** arXiv metadata are released under CC0. The OAI-PMH harvests kept to arXiv's limit of one request every three seconds [2], but arXiv's statistics pages were retrieved with 1-s pauses against a 15-s crawl delay [3]. The arXiv API answered "429 Rate exceeded" to the analysis environment, whose network address may be shared with other clients, so first-version dates were read from the arXivRaw records of the OAI-PMH interface. OSF counts, retrieved for a social-science series that the article does not report, were requested faster than the 100 unauthenticated requests an hour given in the documentation of the osfr R package (OSF's own pages state no figure), whereas the Center for Open Science's terms forbid unreasonable traffic loads [4]. The bioRxiv and medRxiv API states no limit [5]; the record harvests used two to four parallel connections. PubMed requests stayed within three a second [6]. INSPIRE-HEP allows 15 requests in a 5-s window per IP address and makes most of its metadata available under CC0 [7]; the harvester paused 1 s between requests, used pages of 1,000 records and stored no names or e-mail addresses. The scripts now follow every documented limit. No source endorses this work.

**INSPIRE-HEP queries behind the exploratory observation in hep-ex.** Made on 16 October 2026 by an AI agent in a reviewer role through the INSPIRE-HEP literature API [7] (`https://inspirehep.net/api/literature?q=<query>&size=1`, field `hits.total`); they have not been re-run, and the companion's classification of all records by the registered rule supersedes them. Base query: `primarch hep-ex and de YYYY-01-01->YYYY-09-30`. Added clauses: `ac > 300` (more than 300 authors); `ac 1->300 and collaboration:*`; `ac 1->10 and not collaboration:*` (at most 10 authors, no collaboration field); `ac 11->300 and not collaboration:*`; `tc c` (conference papers). The 60 records of January–September 2026 with at most 10 authors, no collaboration field and no conference tag were drawn at random with a fixed seed and classified from titles and abstracts by the same agent, alone and unblinded, so the motivating count is itself unvalidated: 18 were simulation, sensitivity or future-facility studies, 17 machine-learning or AI methods, 7 statistical or analysis methods and software, 6 reviews or talk write-ups, 5 instrumentation papers, 4 reanalyses of existing data, 2 concept studies and 1 a report of new measurements. INSPIRE counts track arXiv's statistics for hep-ex to within 1–2% (717 against 713 in January–September 2022). INSPIRE author counts of 0 mark collaboration papers whose author lists are not yet loaded, so author-count filters miscount recent collaboration papers.

**Dated events** (sources as listed; checked on 16–17 October 2026).

| Date | Event | Source |
|---|---|---|
| 15 Mar 2022 | Contributed papers for the US particle-physics planning exercise Snowmass 2021 due on arXiv | Snowmass Steering Group message of 9 Mar 2022, forwarded at https://mailman.jlab.org/pipermail/hps/2022-March/002209.html |
| 24 May 2023 – 18 Nov 2025 | LIGO–Virgo–KAGRA fourth observing run (O4) | https://ligo.org/ligo-virgo-kagra-collaboration-successfully-wraps-up-its-fourth-observing-run/ |
| 2024 | arXiv limits each submitter to three active submissions | [8] |
| 2022–2024 | BESIII completes its 20 fb⁻¹ data set at the ψ(3770) resonance (second running period 2022–2024) | CERN Courier, 3 May 2024, https://cerncourier.com/a/besiii-passes-milestone-at-the-charm-threshold/ |
| 2024 | LHCb's upgraded detector records 9.56 fb⁻¹, more than Runs 1 and 2 combined | TU Dortmund, 28 Oct 2024, https://e5.physik.tu-dortmund.de/en/details/ende-der-lhcb-proton-proton-kollisions-aufzeichnung-in-2024-46983/ |
| 2024 | The LHC delivers 124 fb⁻¹ each to ATLAS and CMS | CERN, 25 Nov 2024, https://home.cern/record-data-lhc-2024 |
| 1 Jan 2025 | The Gates Foundation expects funded manuscripts to be shared as preprints | https://openaccess.gatesfoundation.org/open-access-policy/ |
| 28 Feb – 8 Apr 2025 | 694 NIH grants terminated (US$1.81 billion), per a JAMA research letter as reported by HPN Online, 9 May 2025 | https://www.hpnonline.com/regulatory/news/55289345/newly-published-study-quantifies-types-of-grants-terminated-by-nih-since-late-february [RECHECK: cite the JAMA research letter itself] |
| 11 Mar 2025 | bioRxiv and medRxiv move to a new independent organisation, openRxiv | [9] |
| 19 Mar 2025 | DESI Data Release 1 and Euclid Quick Data Release Q1 made public | https://data.desi.lbl.gov/doc/releases/; https://www.cosmos.esa.int/web/euclid/euclid-q1-data-release |
| 31 Mar 2025 | Written input to the 2026 update of the European Strategy for Particle Physics due | CERN Courier, 19 Sep 2024, https://cerncourier.com/a/a-decider-for-cerns-next-collider/ |
| 30 Jun 2025 | Rubin Observatory Data Preview 1 released, to data-rights holders only | https://dp1.lsst.io/ |
| 26 Aug 2025 | Fourth gravitational-wave transient catalogue (GWTC-4.0) and O4a strain data released | https://www.ego-gw.it/blog/2025/08/26/gwtc-4-0-updated-gravitational-wave-catalog-released/ |
| 31 Oct 2025 | arXiv computer science accepts review and position papers only after peer review | [10] |
| 28 Nov 2025 | 977 NIH grant awards terminated (US$1.7 billion); NIH made fewer awards in 2025 than its 2020–2024 average | Congressional Research Service, IF13131, 11 Dec 2025, https://www.everycrsreport.com/files/2025-12-11_IF13131_63aaed675c9924bb0867a577571eb87d3451439c.html [RECHECK: cite the Congressional Research Service directly] |
| 2 Dec 2025 | bioRxiv and medRxiv DOIs move to the prefix 10.64898 | bioRxiv and medRxiv API records (this study) |
| 10 Dec 2025; 21 Jan 2026 | arXiv tightens endorsement of new submitters (mathematics; all sections) | [11] |
| 6 Feb 2026 | Final run of RHIC ends | Brookhaven National Laboratory, https://www.bnl.gov/newsroom/news.php?a=122794 |
| 11 Feb 2026 | arXiv requires a full English version of every submission | [12] |
| 8 Mar 2026 (updated 28 Sep 2026) | SocArXiv: generally at most one paper per author per week | [13] |
| 2026, most in July–August | The medRxiv API lists some version-1 preprints twice | medRxiv API records (this study) |
| 22 May 2026 | CERN Council adopts the 2026 update of the European Strategy for Particle Physics | CERN/3997, https://council.web.cern.ch/sites/default/files/c-e-3997-Council%20Resolution%20on%20the%202026%20update%20of%20the%20European%20Strategy%20for%20Particle%20Physics.pdf |
| 1 Jul 2026 | arXiv becomes an independent nonprofit and completes a migration to cloud infrastructure | Cornell Chronicle, 29 Jun 2026, https://news.cornell.edu/node/333261 |
| Jul 2026 | LHC Long Shutdown 3 scheduled to begin, ending Run 3 | CERN, 4 Oct 2024, https://home.cern/updated-schedule-cerns-accelerators |
| Until Oct 2026 | arXiv rate-limits heavy submitters, originally at moderators' discretion; held submissions can spill into the next month | [8] |
| 1 Oct 2026 | arXiv caps submissions at two per submitter per month | [8] |

### References for S2 Appendix

1. Spick M, Onoja A, Harrison C, Stender S, Byrne J, Geifman N. Quantifying new threats to health and biomedical literature integrity from rapidly scaled publications and problematic research. J Clin Epidemiol. 2026;193:112203. doi:10.1016/j.jclinepi.2026.112203
2. arXiv. Terms of use for arXiv APIs [Internet] [cited 2026 Oct 16]. Available from: https://info.arxiv.org/help/api/tou.html
3. arXiv. robots.txt [Internet] [cited 2026 Oct 16]. Available from: https://arxiv.org/robots.txt
4. Center for Open Science. Terms of use [Internet] [cited 2026 Oct 16]. Available from: https://github.com/CenterForOpenScience/cos.io/blob/master/TERMS_OF_USE.md
5. bioRxiv, medRxiv. bioRxiv and medRxiv API [Internet] [cited 2026 Oct 16]. Available from: https://api.biorxiv.org/
6. Sayers E. A general introduction to the E-utilities. 2009 May 26 [updated 2022 Nov 17]. In: Entrez Programming Utilities Help [Internet]. Bethesda (MD): National Center for Biotechnology Information (US); 2010– [cited 2026 Oct 17]. Available from: https://www.ncbi.nlm.nih.gov/books/NBK25497/
7. INSPIRE-HEP. REST API documentation [Internet] [cited 2026 Oct 16]. Available from: https://github.com/inspirehep/rest-api-doc
8. Boboris K. Fair moderation, equitable access, and AI: arXiv's updated rate limit policy [Internet]. arXiv blog; 1 Oct 2026 [cited 2026 Oct 17]. Available from: https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/
9. Naddaf M. Preprint sites bioRxiv and medRxiv launch new era of independence. Nature. 2025 Mar 11. doi:10.1038/d41586-025-00762-4
10. Boboris K. Attention authors: updated practice for review articles and position papers in arXiv CS category [Internet]. arXiv blog; 31 Oct 2025 [cited 2026 Oct 16]. Available from: https://blog.arxiv.org/2025/10/31/attention-authors-updated-practice-for-review-articles-and-position-papers-in-arxiv-cs-category/
11. Boboris K. Attention authors: updated endorsement policy for arXiv Mathematics [Internet]. arXiv blog; 10 Dec 2025, with an edit noting the extension to all sections on 21 Jan 2026 [cited 2026 Oct 16]. Available from: https://blog.arxiv.org/2025/12/10/updated-endorsement-policy-for-arxiv-mathematics/
12. Boboris K. Attention authors: upcoming policy change to non-English language paper submissions [Internet]. arXiv blog; 21 Nov 2025, edited 13 Jan and 11 Feb 2026 [cited 2026 Oct 16]. Available from: https://blog.arxiv.org/2025/11/21/upcoming-policy-change-to-non-english-language-paper-submissions/
13. SocArXiv. AI policy [Internet]. Dated 8 Mar 2026, updated 28 Sep 2026 [cited 2026 Oct 16]. Available from: https://socopen.org/ai-policy/

<!-- SI FILE: S1 Table -->

## S1 Table. Per-person limits on submissions, 2025–2026

*A separate Supporting Information file at submission.* Caps, gates and quotas that restore scarcity by rule. Earlier limits existed (arXiv has limited each submitter to three active submissions since 2024); none of the measures listed predates 2025. "Cap" means a limit on how many items a person may submit, whatever the quality of the work or the conduct of its author.

| Effective | Institution | Type | Measure | What is limited | Stated reason | Source |
|---|---|---|---|---|---|---|
| 25 Sep 2025 | NIH (US) | Cap | At most 6 applications per principal investigator per calendar year (T activity codes and R13 excepted); applications "substantially developed by AI" not considered original | Grant applications | AI "enabled Principal Investigators to submit more than 40 distinct applications in a single application submission round"; the cap is expected to affect "a relatively small number of Principal Investigators" | [1] |
| 31 Oct 2025 | arXiv, computer science | Gate | Review/survey and position papers only after acceptance at a peer-reviewed journal or conference (workshop review does not count) | Unrefereed reviews and position papers | "unmanageable influx"; "hundreds of review articles every month" | [2]; one subfield could lose about half its papers [3] |
| Mar 2026 (updated 28 Sep 2026) | SocArXiv | Cap | Generally at most 1 paper per author per week; no verbatim AI-generated paragraphs; no "superficial, high-level theory synthesis" | Submissions per author | AI-generated content | [4] |
| Jun 2026 | TMLR (journal) | Cap | Yearly per-author submission budget under the Generalized Harmonic Quota Rule (N₁ = 2, N₉ = 9), each submission costing according to its number of authors [5]; doubled for reviewers and action editors; desk-rejected submissions count | Submissions | Submissions tripled in a year, including a 13-fold rise in single-author submissions | [6]; [7] for the date and growth figures |
| 2027 cycle (announced 28 Jul 2026; papers due 25 Sep 2026) | ICLR 2027 | Cap, tiered by prior acceptance | At most 20 submissions per author; at most 1 paper on which no author has had a paper accepted at a major machine-learning conference or journal; excess submissions randomly desk-rejected; each submission must register an author with such an acceptance to review, unless no author has one | Submissions | "The rapid rate of growth in submissions, while exciting, has begun to strain the review system"; more than 62,000 submissions expected (490 a decade ago) | [8]; [7] |
| 1 Oct 2026 | arXiv, all categories | Cap | At most 2 submissions per submitter per calendar month, and 3 active (the 3-active limit dates from 2024); rejected submissions count; described as a "stopgap" | Submissions | 40,363 submissions in Sep 2026 (20,569 in Sep 2024; 9,869 in Sep 2016) | [9] |
| ARR cycles from Oct 2026 | ACL Rolling Review (ACL venues) | Cap, plus a lottery | At most 20 submissions per author and 5 as first or joint first author per cycle; each submission must name a qualified reviewer or chair, and submissions without one enter a lottery for spare reviewing capacity | Submissions (reviewing capacity) | "unsustainable rate of submissions at EMNLP'26"; 38% of ~17,000 May 2026 submissions from authors with no available publication record | [10]; [7] |
| May 2027 conference | AISTATS 2027 | Cap, tiered by prior acceptance | At most 12 submissions per author; at most 3 for authors without an accepted paper at ICLR, ICML, NeurIPS or AISTATS; excess randomly desk-rejected | Submissions | "Peer review is the scarcest resource of a conference … generative AI tools now make it possible to produce far more manuscripts than the community can carefully evaluate" | [11]; [7] |

*Note.* Conduct rules from 2023–2024 (authorship and disclosure rules; the ban on generative AI in NIH peer review) are not rationing and are not listed [12–14]. Not listed either: arXiv's changes to endorsement (from 10 December 2025 in mathematics and 21 January 2026 in all sections) [15] and language (a full English version of every submission from 11 February 2026) [16] [AUTHOR: list the endorsement rule as a gate?]; a one-year ban on submitting for authors who did not check LLM output, announced in May 2026 by the chair of arXiv's computer-science section but not on arXiv's policy pages; and thesis gates based on AI detectors at some Chinese universities, which are not per-person limits. Conference rows were checked against each venue's call or policy on 16 October 2026; TMLR's start date and growth figures rest on a news report. All rows are date-sensitive.

### References for S1 Table

1. National Institutes of Health. NOT-OD-25-132: Supporting fairness and originality in NIH research applications [Internet]. 17 Jul 2025 [cited 2026 Oct 16]. Available from: https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html
2. Boboris K. Attention authors: updated practice for review articles and position papers in arXiv CS category [Internet]. arXiv blog; 31 Oct 2025 [cited 2026 Oct 16]. Available from: https://blog.arxiv.org/2025/10/31/attention-authors-updated-practice-for-review-articles-and-position-papers-in-arxiv-cs-category/
3. Elazar Y, Antoniak M. LLM-generated or human-written? Comparing review and non-review papers on arXiv [Preprint; accepted to Findings of EMNLP 2026]. arXiv:2601.17036v2. 2026 [cited 2026 Oct 16]. Available from: https://arxiv.org/abs/2601.17036
4. SocArXiv. AI policy [Internet]. Dated 8 Mar 2026, updated 28 Sep 2026 [cited 2026 Oct 16]. Available from: https://socopen.org/ai-policy/
5. Shah NB. How many submissions may an author make? A harmonic quota for submissions under coauthorship [Preprint]. arXiv:2606.10293. 2026 [cited 2026 Oct 16]. Available from: https://arxiv.org/abs/2606.10293
6. Transactions on Machine Learning Research. Submission guidelines and editorial policies (authorship quotas) [Internet] [cited 2026 Oct 16]. Available from: https://jmlr.org/tmlr/editorial-policies.html
7. Singh Chawla D. Inundated AI conferences impose submissions caps. Nature. 2026 Oct 13. doi:10.1038/d41586-026-03153-5
8. International Conference on Learning Representations. ICLR 2027 author guidelines; call for papers posted 28 Jul 2026 [Internet] [cited 2026 Oct 16]. Available from: https://iclr.cc/Conferences/2027/AuthorGuidelines
9. Boboris K. Fair moderation, equitable access, and AI: arXiv's updated rate limit policy [Internet]. arXiv blog; 1 Oct 2026 [cited 2026 Oct 17]. Available from: https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/
10. Association for Computational Linguistics. ACL sustainable reviewing policy [Internet]. 11 Sep 2026 [cited 2026 Oct 16]. Available from: https://aclrollingreview.org/sustainable-reviewing-2026
11. AISTATS 2027. Call for papers [Internet] [cited 2026 Oct 16]. Available from: https://virtual.aistats.org/Conferences/2027/CallForPapers
12. Thorp HH. ChatGPT is fun, but not an author. Science. 2023;379:313. doi:10.1126/science.adg7879
13. Ganjavi C, Eppler MB, Pekcan A, Biedermann B, Abreu A, Collins GS, et al. Publishers' and journals' instructions to authors on use of generative artificial intelligence in academic and scientific publishing: bibliometric analysis. BMJ. 2024;384:e077192. doi:10.1136/bmj-2023-077192
14. National Institutes of Health. NOT-OD-23-149: The use of generative artificial intelligence technologies is prohibited for the NIH peer review process [Internet]. 23 Jun 2023 [cited 2026 Oct 16]. Available from: https://grants.nih.gov/grants/guide/notice-files/NOT-OD-23-149.html
15. Boboris K. Attention authors: updated endorsement policy for arXiv Mathematics [Internet]. arXiv blog; 10 Dec 2025, with an edit noting the extension to all sections on 21 Jan 2026 [cited 2026 Oct 16]. Available from: https://blog.arxiv.org/2025/12/10/updated-endorsement-policy-for-arxiv-mathematics/
16. Boboris K. Attention authors: upcoming policy change to non-English language paper submissions [Internet]. arXiv blog; 21 Nov 2025, edited 13 Jan and 11 Feb 2026 [cited 2026 Oct 16]. Available from: https://blog.arxiv.org/2025/11/21/upcoming-policy-change-to-non-english-language-paper-submissions/

<!-- SI FILE: S3 Table -->

## S3 Table. Descriptive heavy-producer measures

*A separate Supporting Information file at submission. Fixed-threshold measures rise mechanically with volume and with namesake collisions, and the concentration shares can also rise under proportional growth (Methods); they describe, and do not test, how output is distributed. Statistics describing fewer than ten authors are suppressed.*

**(A) arXiv mathematics** (primary category math.\*, OAI-PMH metadata harvested on 16 October 2026, from January 2019; a heavy producer has five or more mathematics papers in the quarter).

| Names | Measure | Q3 2022 | Q3 2025 | Q3 2026 | 2026 departure from 2019–2022 trend, percentage points (95% CI) |
|---|---|---|---|---|---|
| All names | Papers with an author who has ≥5 papers in the quarter | 3.39% | 5.30% | 18.14% | 9.23 (5.89 to 12.56) |
| All names | Active authors with ≥5 papers | 0.38% | 0.56% | 2.45% | 1.15 (0.65 to 1.66) |
| All names | Top 1%'s share of fractional output | 4.87% | 5.15% | 6.84% | 1.77 (1.37 to 2.17) |
| All names | Top 10%'s share of fractional output | 25.42% | 26.44% | 32.40% | 4.24 (2.68 to 5.80) |
| Namesake-robust | Papers with an author who has ≥5 papers in the quarter | 0.87% | 1.75% | 5.12% | 3.79 (2.73 to 4.85) |
| Namesake-robust | Active authors with ≥5 papers | 0.13% | 0.29% | 1.16% | 0.73 (0.47 to 0.98) |
| Namesake-robust | Top 1%'s share of fractional output | 4.49% | 4.77% | 6.12% | 1.66 (1.18 to 2.13) |
| Namesake-robust | Top 10%'s share of fractional output | 24.52% | 25.22% | 29.95% | 4.28 (2.88 to 5.68) |

Papers: 8,714 (Q3 2022), 10,846 (Q3 2025) and 19,562 (Q3 2026). Active author names (all names): 15,914, 20,114 and 28,278; with five or more papers: 60, 112 and 693; with ten or more: fewer than ten in 2022 and 2025, and 69 in 2026. January–August windows, all names: 27,078 and 36,097 papers in 2025 and 2026; papers with a heavy producer 18.9% and 26.9%; authors with five or more papers 2.34% and 3.73%; top 1%'s share 6.1% and 7.7%. Counted as list entries (comparable with Nee et al.'s author panel), January–August, all names: 35,308 and 47,142 papers; authors with five or more papers 2.80% and 4.07%. Source: companion file heavy_producers.json.

**(B) arXiv physics, papers with at most 50 authors** (OAI-PMH metadata harvested on 16 October 2026).

| Group and names | Measure | Q3 2022 | Q3 2025 | Q3 2026 | 2026 departure from 2019–2022 trend, percentage points (95% CI) |
|---|---|---|---|---|---|
| Theory, all names | Papers with an author who has ≥5 papers in the quarter | 7.94% | 13.37% | 16.61% | 2.09 (0.06 to 4.13) |
| Theory, all names | Active authors with ≥5 papers | 0.67% | 1.27% | 1.74% | 0.45 (0.19 to 0.72) |
| Theory, all names | Top 1%'s share of fractional output | 5.50% | 5.86% | 6.52% | 0.82 (0.53 to 1.10) |
| Theory, all names | Top 10%'s share of fractional output | 29.21% | 29.54% | 30.88% | −0.30 (−1.11 to 0.50) |
| Theory, namesake-robust | Papers with an author who has ≥5 papers in the quarter | 2.62% | 5.64% | 8.06% | 2.22 (0.31 to 4.13) |
| Theory, namesake-robust | Active authors with ≥5 papers | 0.38% | 0.92% | 1.33% | 0.46 (0.10 to 0.82) |
| Theory, namesake-robust | Top 1%'s share of fractional output | 4.93% | 5.59% | 6.11% | 0.73 (0.36 to 1.10) |
| Theory, namesake-robust | Top 10%'s share of fractional output | 26.82% | 28.18% | 30.27% | 0.71 (−0.55 to 1.97) |
| Experiment, all names | Top 1%'s share of fractional output | 25.56% | 23.14% | 25.57% | 0.13 (−7.08 to 7.34) |
| Experiment, all names | Top 10%'s share of fractional output | 64.70% | 56.56% | 58.55% | 3.21 (−4.66 to 11.08) |

Ordinary least squares on a linear trend, quarter effects and indicators for 2023–2026, Newey–West intervals, which describe uncertainty about the trend, not sampling. Source: companion file heavy_producers.json.

<!-- SI FILE: S4 Table -->

## S4 Table. Published estimates of LLM-assisted writing by field

*A separate Supporting Information file at submission. Literature context: this study runs no marker analysis of its own. The measures differ, so levels cannot be compared across studies; only rankings within a study are informative.*

| Study | Corpus and period | Measure | Results by field |
|---|---|---|---|
| Lin and Zhu (preprint) [1] | 627,384 arXiv papers, 2021–2023 | Share of abstracts classified as AI-generated; increase from the end of 2022 to the end of 2023 [RECHECK: relative or percentage-point increase] | Computer science 22%; electrical engineering and systems science 21%; finance 18%; statistics 15%; economics 11%; quantitative biology (arXiv q-bio, not bioRxiv) 11%; physics 10%; mathematics 3.5% |
| Liang et al. [2] | 1,121,912 preprints and papers on arXiv, bioRxiv and *Nature* portfolio journals, January 2020–September 2024 | Estimated share of LLM-modified sentences, at corpus level | Computer science up to 22%; mathematics and *Nature* portfolio up to 9% [RECHECK: add the bioRxiv series, which can be read in the open preprint version (arXiv:2404.01268), noting its shorter window] |
| Kobak et al. [3] | 15.1 million PubMed abstracts, 2010–2024 | Lower bound on the share of 2024 abstracts processed with LLMs (excess vocabulary) | All abstracts at least 13.5%; computational fields (computation, bioinformatics) about 20%; from below 5% to more than 40% across fields, countries and journals |
| Holzwarth et al. (preprint) [4] | PubMed Central open-access full texts | Share of papers with an excess of LLM-associated vocabulary | 89% of papers by the end of 2025 |
| He and Bu (preprint) [5] | 5,114 journals, more than 5.2 million papers, 2021–2025 | Growth in the share of AI-assisted text in abstracts | Fastest growth in the physical sciences (a domain that includes mathematics and computer science); slower growth in the life and health sciences |

### References for S4 Table

1. Lin CW, Zhu W. Divergent LLM adoption and heterogeneous convergence paths in research writing [Preprint]. arXiv:2504.13629. 2025 [cited 2026 Oct 16]. Available from: https://arxiv.org/abs/2504.13629
2. Liang W, Zhang Y, Wu Z, Lepp H, Ji W, Zhao X, et al. Quantifying large language model usage in scientific papers. Nat Hum Behav. 2025;9(12):2599–2609. doi:10.1038/s41562-025-02273-8
3. Kobak D, González-Márquez R, Horvát EÁ, Lause J. Delving into LLM-assisted writing in biomedical publications through excess vocabulary. Sci Adv. 2025;11(27):eadt3813. doi:10.1126/sciadv.adt3813
4. Holzwarth L, González-Márquez R, Kobak D. Most biomedical publications show signs of LLM-assisted writing [Preprint]. arXiv:2608.10715v1. 2026 [cited 2026 Oct 16]. Available from: https://arxiv.org/abs/2608.10715
5. He Y, Bu Y. Academic journals' AI policies fail to curb the surge in AI-assisted academic writing [Preprint]. arXiv:2512.06705v2. 2026 [cited 2026 Oct 16]. Available from: https://arxiv.org/abs/2512.06705

<!-- SI FILE: S5 Table -->

## S5 Table. All estimates

*A separate Supporting Information file at submission: a spreadsheet with a README, assembled from the companion files within_field_tests.json, round1_tests.json, field_tests.json and heavy_producers.json [ANALYSIS PENDING: companion item 4]. The marker analysis withdrawn by the author (Methods, Deviations) is not part of it; its outputs stay in the deposit. The two parts below are the estimates moved out of the main text in v3.*

**(A) Rows moved from Table 1.**

| | C1 physics: theory / experiment | C2 biology: computational / wet lab | C3 medicine: public dataset / other |
|---|---|---|---|
| Acceleration: 2026 / 2025 | 1.05 (0.89–1.24) | 1.10 (1.06–1.15) | 1.10 (1.03–1.18) |
| Slope change after December 2022, % a year (bootstrap p) | −0.6 (−5.4 to 4.4; 0.86) | 10.8 (5.2 to 16.7; 0.024) | −3.8 (−8.6 to 1.3; 0.27) |
| Trend-adjusted, 2026, as first reported (planned version in Table 1) | 0.98 (0.72–1.33) | 1.48 (1.06–2.07) | 0.87 (0.61–1.24) |
| Rank p of the 2026 coefficient among the contrast's own years, two-sided (n)ᵃ | 0.67 (8; one-sided 0.33); without gr-qc 0.89 | 0.80 (4) | 0.60 |
| Rank p of the 2026/2025 change among all earlier year-on-year changes (n)ᵃ | 0.73 (10) | 0.29 (6) | 0.29 |
| Negative controls | hep-ex / nucl-ex 1.39 (1.19–1.64); six theory pairs 0.85–1.06 | – | – |
| Variants, 2022 base (placebo p) | Theory without gr-qc 1.10 (0.96–1.25; 0.70); hep-ph / hep-ex 0.97 (0.86–1.10; 0.86); hep-th / hep-ex 0.99 (0.87–1.14; 0.95); gr-qc / experiment 1.27 (1.10–1.46; 0.40) | – | With the four further datasets of Spick et al. 1.05 (0.93–1.17); title-only COVID-19 filter 1.07 (0.95–1.21) |
| Variants without planning papers, 2022 base | Theory without gr-qc 1.02 (0.86–1.21); hep-ph / hep-ex 0.88 (0.74–1.04); hep-th / hep-ex 0.87 (0.74–1.03); gr-qc / experiment 1.15 (0.96–1.39) | – | – |

Slope change: change in the slope of the deseasonalised log ratio, with Newey–West intervals; pre-2023 slopes were 0.7% (C1) and −6.7% (C2) a year. Trend-adjusted: departure from the extrapolated pre-2023 relative trend. Theory pairs: hep-th / hep-ph 1.02, hep-th / gr-qc 0.87, hep-th / nucl-th 0.91, hep-ph / gr-qc 0.85, hep-ph / nucl-th 0.89, gr-qc / nucl-th 1.06. Without gr-qc, the C1 contrast is 1.03 (0.91–1.16) against 2017–2019. ᵃ Event-study estimator of Table 1 (first reported); two-sided p is the share of values at least as far from 1 as 2026's, 2026 included, so with n earlier values it cannot fall below 1/(n + 1). Against changes up to 2022 only (n = 3 or 7), every rank p is at least 0.50. The v2 statistic (the 2026 coefficient divided by the SD of the pre-2022 coefficients, referred to a normal distribution) is withdrawn, because it overstated how unusual 2026 was [CONFIRM: companion item 3 (definition)].

**(B) Growth of fractional output by author class (H2), 2025 to 2026.** Names ranked on combined output in the two periods compared.

| Group | Names | Window | Total | Top 1% | Next 9% | Bottom 90% | Bottom 90%'s share of the increase |
|---|---|---|---|---|---|---|---|
| Mathematics | All names | Q3 2025 → Q3 2026 | +80% | +266% | +120% | +57% | 52% |
| Mathematics | All names | Jan–Aug 2025 → Jan–Aug 2026 | +33% | +78% | +41% | +26% | 52% |
| Mathematics | All names | Jul–Aug 2025 → Jul–Aug 2026 | +62% | +135% | +95% | +49% | 58% |
| Mathematics | All names | Q3, names active in 2019–2024 | +70% | +210% | +119% | +47% | 50% |
| Mathematics | All names | Jan–Aug, names active in 2019–2024 | +27% | +76% | +41% | +18% | 46% |
| Mathematics | Namesake-robust | Q3 2025 → Q3 2026 | +56% | +211% | +81% | +41% | 53% |
| Mathematics | Namesake-robust | Jan–Aug 2025 → Jan–Aug 2026 | +26% | +63% | +27% | +22% | 58% |
| Mathematics | Namesake-robust | Jul–Aug 2025 → Jul–Aug 2026 | +45% | +90% | +69% | +35% | 59% |
| Mathematics | Namesake-robust | Q3, names active in 2019–2024 | +46% | +162% | +72% | +33% | 53% |
| Mathematics | Namesake-robust | Jan–Aug, names active in 2019–2024 | +19% | +62% | +28% | +12% | 46% |
| Physics theory (≤50 authors) | All names | Q3 2025 → Q3 2026 | +26% | +44% | +37% | +21% | 54% |
| Physics theory (≤50 authors) | All names | Jan–Aug 2025 → Jan–Aug 2026 | +17% | +28% | +23% | +13% | 47% |
| Physics theory (≤50 authors) | All names | Jul–Aug 2025 → Jul–Aug 2026 | +19% | +40% | +25% | +15% | 56% |
| Physics theory (≤50 authors) | All names | Q3, names active in 2019–2024 | +23% | +57% | +41% | +15% | 44% |
| Physics theory (≤50 authors) | All names | Jan–Aug, names active in 2019–2024 | +15% | +36% | +27% | +8% | 36% |
| Physics theory (≤50 authors) | Namesake-robust | Q3 2025 → Q3 2026 | +25% | +50% | +33% | +20% | 55% |
| Physics theory (≤50 authors) | Namesake-robust | Jan–Aug 2025 → Jan–Aug 2026 | +16% | +21% | +19% | +13% | 54% |
| Physics theory (≤50 authors) | Namesake-robust | Jul–Aug 2025 → Jul–Aug 2026 | +17% | +10% | +26% | +15% | 61% |
| Physics theory (≤50 authors) | Namesake-robust | Q3, names active in 2019–2024 | +21% | +55% | +40% | +12% | 41% |
| Physics theory (≤50 authors) | Namesake-robust | Jan–Aug, names active in 2019–2024 | +12% | +22% | +22% | +7% | 38% |

Source: companion file heavy_producers.json (decomposition and sensitivity_2025_2026). Pairs before ChatGPT's release (third quarters, all names) are in the same file and in Fig 3. The top 1% of the third-quarter 2025 → 2026 pair in mathematics produced 1.08 fractional papers per name in Q3 2025, against 1.64–1.80 in the first quarter of every earlier pair.

<!-- SI FILE: S6 Table -->

## S6 Table. Deviations from the analysis plans

*A separate Supporting Information file at submission. One row per departure from the plan in v1 of this manuscript (commit 697fb25, pushed 16 October 2026, 17:27:53 UTC) or from the plan of the paper-level tests (S1 Text: commit 763aa2b, 18:28:57 UTC, and Amendment 1, 78890e5, 18:47:08 UTC), in the form recommended for reporting deviations [1,2]. Times are UTC, the push times recorded by GitHub for this repository; companion commits are on the analysis branch. "D" labels follow the registration files.*

**(A) The within-field contrasts and H2–H3 (plan in v1).**

| # | Planned | Done | When recorded | What had been seen | Reason | Expected effect on inference |
|---|---|---|---|---|---|---|
| 1 | Period effects against multi-year baselines (2017–2022 arXiv; 2019–2022 bioRxiv; mid-2019 to 2022 medRxiv) | Year-by-group effects with 2022 as the reference year; the plan's pre-trend diagnostic became the primary estimate | Specification committed with the first estimates (companion 37b4b11, 16 Oct 17:43:39); disclosed in v2 (a17a8b9, 23:39:36) | Descriptive growth of every group; [AUTHOR: whether any estimate had been seen when the reference year was chosen] | [AUTHOR] | 2022 was a low year for C1 and C2, which favours H1 there. The planned specification, computed in review after these estimates were known (companion 666be30, 17 Oct 2026), gives 1.05, 1.02 and 1.05; it is primary from v3, and both are reported |
| 2 | Poisson or negative binomial models with Newey–West errors | Pseudo-maximum likelihood with month fixed effects, group-specific calendar-month effects and Driscoll–Kraay errors (12 lags) | Companion 37b4b11 (16 Oct 17:43:39) | Descriptive growth | Month fixed effects absorb platform-wide shocks; pseudo-maximum likelihood is consistent under overdispersion | Intervals measure within-year uncertainty only (narrower); the placebos carry the inference (row 5) |
| 3 | Bonferroni-adjusted intervals; Benjamini–Hochberg adjustment of negative controls | Holm-adjusted p values with the planned Bonferroni (98.3%) intervals; placebo shares for negative controls | Companion 37b4b11; v2 | Descriptive growth; the Holm and Bonferroni results together | Holm is uniformly more powerful than Bonferroni; adjusting negative controls makes problems harder to flag | None on the verdict: only C2 excludes 1 under either |
| 4 | Bai–Perron break tests | sup-Wald single-break tests with 5% trimming, fixed-date Wald tests, AR(1) parametric bootstrap | v2 (a17a8b9, 16 Oct 23:39:36), after the round-1 reviews | Earlier break tests with 15% trimming | 15% trimming could not place a break after December 2024 | The physics break moved from the old boundary to May 2025; timing claims rest on yearly departures |
| 5 | Model intervals as the inference | In-space placebo p as the primary inference | v2 (a17a8b9), after round 1 | All estimates | Few treated units; model intervals omit year-level shocks | Conservative: placebo p values are larger than model p values |
| 6 | A decision rule for each contrast (support only if the adjusted interval excludes 1), none for H1 as a whole | H1 needs support in all three fields | v2 (a17a8b9) | All estimates | H1 is stated as a general claim | None: H1 fails under any rule |
| 7 | No robustness criterion | An estimate is robust only if no single exclusion moves it across 1 | v2 (a17a8b9) | All estimates | Each contrast rests on one component | Labels C1 and C2 as not robust |
| 8 | gr-qc in the theory group | C1 also reported without gr-qc | v2 (a17a8b9) | All estimates | gr-qc includes gravitational-wave experiments, which the rule applied to astro-ph and cond-mat would have excluded | 1.10 against 1.14 (2022 base) |
| 9 | H3 and the second clause of H1 tested with a marker of AI-assisted writing (commit 2cac071, 16 Oct 16:42:22) | Test run (companion f5ab16e, 7ac5647 and 0e239cd, 16 Oct 18:08–19:22) and reported in v2; measure withdrawn by the author, not reported in v3 | Author's decision of 17 Oct, logged in 116910b (08:15:17) | All marker results, as reported in v2 | Its relevance after 2024 cannot be assured: the marker vocabulary drifts as authors and models avoid the words | H3 and the writing part of H1's second clause are untested in this article; results deposited (marker_tests.json, marker_growth_panel.csv) [AUTHOR: R4 recommends the 2024-only test in an S Table] |

**(B) The paper-level tests (plan 763aa2b and Amendment 1 78890e5).**

| # | Planned | Done | When recorded | What had been seen | Reason | Expected effect on inference |
|---|---|---|---|---|---|---|
| D1 | The author's blind validation coding before classification and estimation | Classification and estimation before the coding | 11264ee (16 Oct 18:48:56) | No class share or estimate | The author's request ("supón que está bien y mañana lo valido") | The coder could learn results before coding; mitigated by sealing (D3i), except Test A on medRxiv (D3, second addendum) |
| D2.1 | Full classification | Stratified samples: 15 papers per archive-month in 2017–2024 and 40 in 2025–2026 (HN; Test A alike); at least 150 per Test B category in 2019–2022 | 1de63a9 (16 Oct 18:55:17) | None | About 770,000 papers could not be classified with the available tooling | Sampling error enters the intervals through the bootstrap; expected detectable ratio about 1.15–1.20 for observed labels |
| D2.2 | Temperature 0 | Temperature cannot be set; one classification per paper | 1de63a9 | None | Sub-agent tooling | Decoding noise is not in the intervals; see D3g |
| D2.3 | Model name and version recorded | Not written in the repository | 1de63a9 | None | Repository policy | Must be stated in the article [AUTHOR: model and version] |
| D2.4 | Validation sample from all papers | bioRxiv and medRxiv draws limited to Creative Commons-licensed papers | 1de63a9 | None | The sheet is public | Agreement may not transfer to other papers; licence check in D3h |
| D2.5 | – | Key and model labels of the validation sheet sealed and hash-committed | 1de63a9 | None | Blinding | Depends on the author not opening the sealed files |
| D3a | Labels stored and not re-drawn (D2.2) | The first, date-ordered runs keyed by DOI (900 medRxiv sample papers; 200 bioRxiv and medRxiv validation papers) superseded by blind runs | Done at companion 8ab4d9d (16 Oct 23:43:16); recorded in 8932773 (17 Oct 08:07:23) | No label analysed | DOIs encode posting dates, which the classifier was meant not to see | Better blinding; first-run labels used only for agreement between runs |
| D3b | "At least 2 of 3" units must exceed 1 (applied to Test A) | Test A: supported if the ratio > 1 and its 95% CI excludes 1; contradicted if < 1 and the CI excludes 1; otherwise not supported | Code fixed at 8ab4d9d before any estimate; recorded in 8932773 | None | Test A has one unit per server | Makes "supported" attainable |
| D3c | "Permutation p < 0.05" | One-sided permutation p decides; two-sided also reported | Coded before estimation; recorded in 8932773 | No Test B estimate | Directional prediction | Halves p relative to a two-sided test |
| D3d | Test B: arXiv subcategories with at least 300 papers a year; the sampling design (companion c2f891b, 16 Oct 19:01:12) also put in 23 math.\* subcategories and C1's six archives | Primary: 15 held-out arXiv subcategories with at least 1,200 papers in 2019–2022, plus the bioRxiv and medRxiv categories; the sampling design's set as a sensitivity analysis only | 8932773 (17 Oct 08:07:23) | Outcomes of every category (mathematics computed on 15 Oct) and the archive departures; the Test A (medRxiv) estimate | The plan reserves hep-ex and nucl-ex for exploratory use; mathematics outcomes known and its share of papers with new data near zero; classifier not validated there | Removes known outcomes from the verdict |
| D3e | Trend-based estimands only | Level-based companion estimates (Test A against pooled 2019 + 2022; Test B by category; HN against pooled 2017–2019 + 2022 as a seventh sensitivity analysis); disagreement reported as dependence on the counterfactual | 8932773 | The Test A (medRxiv) trend-based estimate, so post hoc for medRxiv | Class-specific trends are not credible on bioRxiv and medRxiv | Guards against a verdict driven by the end of server adoption |
| D3f | Validation sample by random submission day; full bioRxiv frames | arXiv half drawn by simple random sampling per stratum; bioRxiv frames without epidemiology and clinical trials | 8932773 | None | The arXiv API answered "429 Rate exceeded"; the two categories leave bioRxiv in 2019 | Small |
| D3g | Each paper classified "independently" | Each sub-agent judges a batch of 50 papers in one context; test–retest disagreement propagated by relabelling in each bootstrap draw; the 200 arXiv validation papers classified twice, blind | 8932773; detail in 6e1c119 (17 Oct 08:18:53) | None | Correction of Deviation 2 | Label noise carried in a sensitivity analysis |
| D3h | κ ≥ 0.60 per domain | Also reported: κ with 95% CIs by domain and period, confusion matrices, precision and recall, agreement between runs, misclassification-corrected ratios [3], detectable effects for observed and implied true ratios, Holm-adjusted p across HN, HN-bio, HN-med and HN-dose, a licence check and run records | 8932773 | The Test A (medRxiv) estimate | Round-2 reviews | Secondary; no verdict changes |
| D3i | Classification and estimation before coding (D1) | Remaining estimates written only to compressed, hash-committed files until the author's coding is committed; neither the author nor the coordinating session told any estimate | 8932773 | The Test A (medRxiv) estimate, committed at companion dacd064 (17 Oct 00:11:46) | Restores the registered order in substance | The coding is blind to every estimate except Test A on medRxiv |
| D3j | D2: "The author can revise this choice before results are reported" | Further changes count as pre-specified only if recorded before the relevant estimate | 8932773 | As for D3i | Close an open door | – |
| D3, second addendum | D3 stated that the author had not seen the Test A (medRxiv) estimate | At about 00:12 on 17 Oct, before the hold (00:15), the analysis session reported the point estimate, interval, verdict and detectable effect in its chat with the author | 6e1c119 (17 Oct 08:18:53) | – | Correction | The medRxiv part of the coding may not be blind to that result [AUTHOR: state whether you read it before coding] |
| D3k | Categories below 150 eligible papers "pooled with their closest category or dropped"; code threshold 300 | Dropped; threshold 150 for bioRxiv and medRxiv (28 medRxiv categories enter, 23 are dropped) | 80a2ef2 (17 Oct 08:14:28); completed in 6e1c119 | No Test B estimate; bioRxiv Test B sample not yet drawn | Apply the registered rule without a judgment of closeness | More categories and more power |
| D3l | – | HN sensitivities 8 (without astro-ph; each archive left out in turn) and 9 (astro-ph without papers naming DESI, Euclid, Rubin or LSST) | 80a2ef2 | No HN estimate | 2025 public data releases can move astro-ph papers on the same data from new to no new data | Reported; the verdict is unchanged |
| D3m | – | Sensitivity 10 for HN, Test A and Test B: papers whose title or abstract matches a fixed list of AI and machine-learning terms excluded | 80a2ef2 | No estimate other than Test A (medRxiv) | Papers about machine learning are in the no-new-data class by construction | Reported; the verdict is unchanged |
| D3n | A 2019 placebo for every test | Reported but not interpreted for bioRxiv and medRxiv | 80a2ef2 | As for D3m | 2019 is the first year of both series | None |
| D3o | – | All registered HN sensitivity analyses and sensitivities 7–10 implemented before the HN estimate; Test B computed only once its code covers both sets and the level-based outcome | 80a2ef2 | No HN or Test B estimate | Six registered sensitivity analyses were not wired in the code reviewed in round 2 | Completeness |
| D3p | Test B samples reuse Test A papers in 2019–2022 | 150 papers per category drawn independently of Test A; a paper drawn twice is classified once | 6e1c119 | The medRxiv Test B draws already classified | Kept because the draws had been classified | Efficiency only; each category's sample stays a simple random sample |
| Erratum | §1 of the plan: the 60 hep-ex records were "classified by one person" | They were classified by one AI agent acting as an internal reviewer, not blind to the hypothesis | 8932773 | – | Correction of the record | None on the tests; the motivating count is unvalidated |
| INSPIRE | §10 of the plan: "Report the rule variants" | Four variants defined in the analysis code (no experiment link; prospect wording in titles only; no prospect filter; primary experimental category only) | With the first INSPIRE-HEP estimates (companion 0e239cd; mirrored here at 16 Oct 19:22:12) | The main estimates | Sensitivity of an exploratory rule | Exploratory only; the variants are not registered |

*Note.* The texts of Deviation 3 and of its addenda give their own times as "about 08:20", "about 08:45" and "about 09:05 UTC", later than the push times above, which are authoritative [AUTHOR: correct the stated times with a dated note in the registration files].

### References for S6 Table

1. Willroth EC, Atherton OE. Best laid plans: a guide to reporting preregistration deviations. Adv Methods Pract Psychol Sci. 2024;7(1):25152459231213802. doi:10.1177/25152459231213802
2. Lakens D. When and how to deviate from a preregistration. Collabra Psychol. 2024;10(1):117094. doi:10.1525/collabra.117094
3. Rogan WJ, Gladen B. Estimating prevalence from the results of a screening test. Am J Epidemiol. 1978;107(1):71–76. doi:10.1093/oxfordjournals.aje.a112510
