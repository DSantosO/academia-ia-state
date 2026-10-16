<!--
DRAFT v1 (keyed working copy; numbering of references is applied at the end of drafting).
PLOS ONE Research Article. 16 Oct 2026. First full draft written by an AI agent (Claude, via Claude Code) from:
paper/plos_one/skeleton.md; paper/brief.md; paper/figures/README_companion_analysis.md, within_field_quarterly.csv and
arxiv_math_prolific_robustness.json; Table 1, the argument and the audited reference list of paper/draft_full.md;
paper/reviews/final_verification.md and citation_audit.md; research notes 3, 6, 7 and 8. Not yet revised by the author.
WORD COUNT: [to be filled at the end of drafting]
-->

# Generative AI is eroding publication counts as a measure of scientific work: evidence from 1.9 million preprints

<!--
TITLE: the author's choice (skeleton, 16 Oct 2026). The author is not deciding the title now.
- N is provisional: 1,944,974 new preprints, Q1 2020–Q3 2026, in six series (arXiv physics, mathematics and computer
  science; bioRxiv; medRxiv; the social-science servers). Recompute once the final sample is fixed; extending to 2017
  would raise it. [ANALYSIS PENDING: final N]
- "evidence from 1.9 million preprints" sits close to Qi et al.'s "Two-Million Preprints" (ref. Qi2025).
- Reviewers may read "is eroding" as a causal claim; the design is observational (Discussion, Limitations).
Alternatives recorded in the skeleton:
1. Is generative AI making publication counts obsolete? Evidence from preprint servers, 2020–2026 (the skeleton's
   recommended variant; the author prefers no question in the title)
2. Publication counts are losing their meaning: AI-era growth concentrates where experiments are not the bottleneck
3. Generative AI is eroding publication counts as a measure of scientific work: evidence from preprints in physics,
   mathematics, biology and medicine (avoids the closeness to Qi et al.)
4. When writing is cheap: generative AI accelerates scientific output where experiments are not the bottleneck
5. Generative AI is changing what publication counts measure: evidence from preprint servers, 2020–2026
6. Theory, computation and existing data: where generative AI has accelerated scientific output
7. Generative AI is making current scientific metrics obsolete (the author's first proposal)
-->

[AUTHOR: full name]<sup>1,2,*</sup>

<sup>1</sup> European Molecular Biology Laboratory (EMBL), [AUTHOR: unit, site, city, country]
<sup>2</sup> Universitat Pompeu Fabra (UPF), Barcelona, Spain

\* Corresponding author: [AUTHOR: email]. <!-- EMBL must be the corresponding affiliation for the EMBL–PLOS flat-fee agreement; confirm with the EMBL library. -->

## Abstract

Research evaluation relies on counts of outputs, and those counts carried information partly because outputs were costly to produce. Generative artificial intelligence (AI) lowers that cost even when it is used legitimately. I examined where output has accelerated since generative AI became widely available, using new preprints on arXiv, bioRxiv, medRxiv and three social-science servers (about 1.9 million, 2020 to the third quarter of 2026 [ANALYSIS PENDING: final N]), and contrasted experimental with non-experimental work within fields. In the third quarter of 2026, new preprints grew year on year by 78% in mathematics, 41% in computer science and 26% in physics, but by 10% on bioRxiv, which has grown by 10–13% a year since 2023 with no break in 2026. In January–September 2026, theoretical physics archives grew by 20%, outside their 2017–2025 range (−6% to +6%), while experimental archives grew by 11%, within theirs. Computational biology outgrew wet-lab biology only from 2025 (18% against 8% in 2026), mostly in bioinformatics. In arXiv mathematics, the share of papers with an author who posted five or more papers in the same quarter rose from 5.3% in January 2025 to 19.3% in September 2026 (from 3.0% to 6.2% under a namesake-robust definition); the rise appeared in every team size and across subfields, and 611 of the 693 prolific authors of the third quarter of 2026 had posted mathematics papers before. Published estimates put AI-assisted writing in biology on a par with physics. Output has grown fastest where the work beyond writing is also cheap, and much less, so far, in experimental work. [ANALYSIS PENDING: one sentence with the three confirmatory ratios of rate ratios and their 95% CIs.] These patterns are consistent with AI lowering the cost of counted outputs without any misuse, which would change what publication counts measure; they do not establish that AI caused the growth.

<!-- Abstract: PLOS ONE limit 300 words; see the word count in the header. -->

## Introduction

Decisions on hiring, promotion and funding rely heavily on what can be counted. Publication counts, journal impact factors and grant income dominate the criteria that institutions use to assess researchers [@Moher2018]. Counts are a crude proxy for qualities such as originality and rigour, but they carried some information because the outputs they count were costly to produce. Paper-based evaluation, Blekhman argues, "took hold because a paper took effort to produce, and that effort served as evidence" [@Blekhman2026]. In the language of signalling, "Signals are often informative insofar as they require differential knowledge and effort to produce" [@Cowgill2026].

Generative artificial intelligence (AI) lowers the cost of producing the written part of research outputs, and it does so when it is used legitimately, not only when it is misused. In a study of 2.1 million preprints, the use of large language models (LLMs) "reversed the relationship between writing complexity and paper quality" [@Kusumegi2025], and Hansen argues that "surface quality no longer reliably indicates epistemic merit" [@Hansen2026]. The same reasoning applies to counts. If AI lets researchers produce more papers for the same underlying work, the number of papers changes meaning without anyone misbehaving. For AI used as a research method, a study of 41.3 million natural-science papers found that authors of papers using AI published 3.02 times as many papers and received 4.84 times as many citations, while AI papers covered a 4.63% narrower range of topics; the study concerns mostly machine learning before ChatGPT, and its authors "cannot fully identify the causal linkage between AI adoption and scientific impact" [@Hao2026]. Huang et al. argue that "AI makes extending a familiar research line faster and cheaper than entering unfamiliar terrain, and existing incentive systems reward such speed" [@Huang2026].

Output was already growing faster than the capacity to read it before generative AI: indexed articles were about 47% more numerous in 2022 than in 2016 [@Hanson2024]. Since then, an editorial in *Organization Science* reports that "Submission volume has risen 42% since the late 2022 release of ChatGPT" [@Gartenberg2026]; the US National Institutes of Health (NIH) reported that "the use of AI tools has enabled Principal Investigators to submit more than 40 distinct applications in a single application submission round" [@NIH2025]; and arXiv received 40,363 submissions in September 2026, against 20,569 in September 2024 [@arXiv2026]. The main institutional responses so far have been limits on how many items each person may submit (Table 1). <!--REFS:Table1-->

Several studies have measured how output changed. Qi et al. analysed more than 2.1 million preprints posted on arXiv, bioRxiv, medRxiv and SocArXiv from 2016 to 2025 with interrupted time series. They report that LLMs "have accelerated submission and revision cycles, modestly increased linguistic complexity, and disproportionately expanded AI-related topics, while computationally intensive fields benefit more than others", and they describe LLMs as "selective catalysts" [@Qi2025]. Nee et al. fitted a regularised synthetic control to 2,080 monthly observations for 20 arXiv archives from January 2018 to August 2026 [@Nee2026]. They estimate that arXiv mathematics recorded 11.9% more entries in January–August 2026 than its synthetic counterfactual (9.6% to 14.9% across qualified designs), find growth in 29 of 30 primary mathematics categories, and report a thicker tail of repeat producers in a pseudonymised author panel. The break, they write, is "concentrated in 2026 rather than spread across the years following public access to ChatGPT". Both studies are preprints.

A separate literature estimates how much scientific text is written with AI. At least 13.5% of 2024 PubMed abstracts were processed with LLMs, a lower bound that reached 40% in some subcorpora [@Kobak2025], and other studies estimate the prevalence by field [@Liang2025; @LinZhu2025; @Holzwarth2026]. These estimates rest on word frequencies and classifiers, which measure style rather than purpose.

These studies leave open whether growth in output follows what AI can produce rather than who uses it, in three respects. First, comparisons between fields confound the effect of AI with differences in preprint culture, publication norms and incentives. Contrasts within a field, between experimental and non-experimental work that share these conditions, are a sharper test. Qi et al.'s finding on computationally intensive fields is a between-field result, and Nee et al. neither compare theory with experiment nor cover bioRxiv and medRxiv. Second, aggregate counts do not show whether growth comes from a few outliers or from many researchers producing more, which matters for how counts should be read. Third, it is not known whether AI use translates into output where experiments bind. Blekhman writes that "AI has not yet substantially increased productivity in biology, where the bottlenecks are structural and experimental rather than computational" [@Blekhman2026], but the claim has not been tested with data.

Here I examine new preprints (first versions) on arXiv, bioRxiv, medRxiv and three social-science servers up to the third quarter (Q3) of 2026, the year in which Nee et al. locate the break. I contrast theoretical with experimental physics, computational with wet-lab biology, and medRxiv preprints that name widely reused public datasets with the rest, and I analyse how output is distributed among authors in arXiv mathematics. The study addresses three hypotheses:

- **H1.** The AI-era acceleration of output is concentrated where the work beyond writing is also cheap: theory, computation and analyses of existing data. In experimental work, AI is visible in the writing but much less, or not yet, in the volume of output.
- **H2.** Where output accelerates, the increase is broad: it comes from many established researchers producing more, not from a few outliers.
- **H3.** AI-assisted writing is widespread across fields, including experimental ones, so differences in output growth are not explained by differences in the adoption of AI for writing.

The design is observational. Release dates of AI tools mark when the tools became available, not causes, so the analysis can show whether the pattern of growth is consistent with these hypotheses, not that AI caused it.

## Materials and methods

### Study design

This is an observational study of counts of new preprints, in three parts: comparisons of growth between fields; contrasts within fields between experimental and non-experimental work (H1); and an analysis of how output is distributed among authors in arXiv mathematics (H2). Evidence on the prevalence of AI-assisted writing (H3) comes from published estimates; a marker analysis on the same preprints is planned. Preprint counts measure posting, not publication, quality or the amount of work behind each paper. Because preprint adoption differs between fields, I compare trends within each series, not levels across series. The descriptive counts were examined before the analysis plan was written, so the study was not preregistered. The plan fixes three confirmatory tests before any model is estimated and labels all other analyses exploratory (see Statistical analysis); placebo dates, break tests without a pre-specified date and negative controls limit the scope for choosing favourable comparisons after seeing the data.

### Data sources

*arXiv archives.* Monthly counts of new submissions by primary archive, excluding replacements and cross-lists, were taken from arXiv's per-archive yearly statistics for January 2016 to September 2026 [AUTHOR: URL of the statistics pages]. Physics comprises astro-ph, cond-mat, gr-qc, hep-\*, math-ph, nlin, nucl-\*, physics and quant-ph; mathematics comprises math; computer science comprises cs. Because some categories are aliased across archives (for example math-ph and math.MP), archive sums exceed arXiv's official total by about 5%.

*arXiv mathematics metadata.* For the author-level analysis, the metadata of every arXiv record modified since 1 January 2025 were harvested through arXiv's OAI-PMH interface on 15 October 2026. A paper counts as mathematics when its primary (first-listed) category begins with "math.", and it is dated by the month of its first version, read from its identifier (YYMM.NNNNN). These counts of moderated, announced papers run 6–13% below the per-archive statistics, which also count aliased categories, but agree on the trend (Q3 2026 against Q3 2025: +80% and +78%). October 2026 was incomplete when harvested and is excluded.

*bioRxiv.* Yearly and monthly totals of new papers came from bioRxiv's content statistics [@bioRxiv2026], and monthly totals for 25 subject categories from the bioRxiv application programming interface (API). The category totals match bioRxiv's official monthly totals exactly from July 2019 (January–June 2019 is about 4% lower, because epidemiology and clinical-trials preprints moved to medRxiv). They carry no topic flag, so the bioRxiv series include COVID-19 preprints; in a full read of May–June 2022, these were 5.1% of computational, 5.9% of wet-lab and 2.1% of mixed preprints, so they inflate the 2022 bases of the two contrasted groups by similar amounts.

*medRxiv.* The titles, abstracts and subject categories of new medRxiv preprints, from the server's launch in mid-2019 to September 2026, were retrieved through the medRxiv API. Preprints whose title or abstract matches a regular expression for COVID-19, SARS-CoV-2 or 2019-nCoV (S2 Appendix) are excluded from the medicine series; they were 66% of new medRxiv preprints in 2020 and 5% in 2026.

*Social sciences.* First versions of preprints on PsyArXiv, SocArXiv and EdArXiv were counted through the Open Science Framework (OSF) API, and arXiv's economics (econ) and quantitative-finance (q-fin) archives were added. SSRN and RePEc are not included.

All data were retrieved on 15–16 October 2026. [AUTHOR: confirm the terms of use of each source for redistributing the aggregated counts.]

### Outcomes

The outcome is the number of new preprints (first versions) per month or quarter. For display, each series is indexed to its own 2022 quarterly average (2022 = 100). Year-on-year growth is reported for fields as the change from Q3 2025 to Q3 2026 and, for the within-field contrasts, as the change from January–September of one year to the same months of the year before, so that 2026 can be compared with earlier years; for the arXiv archives, which start in 2016, the 2026 value is compared with the range of the same statistic over 2017–2025. Growth over the last four quarters compares Q4 2025 to Q3 2026 with 2022.

### Groups for the within-field contrasts

*Physics.* Theory comprises the hep-th, hep-ph, gr-qc and nucl-th archives; experiment comprises hep-ex and nucl-ex. Archives that mix theory with observation or experiment, such as astro-ph, cond-mat and quant-ph, are assigned to neither group.

*Biology.* bioRxiv subject categories were assigned to groups before growth was examined: computational (bioinformatics, systems biology, genomics), wet lab (12 categories, from biochemistry to synthetic biology) and mixed (the other ten, of which neuroscience is the largest); the full lists are in S2 Appendix. Genomics is also reported alone, and arXiv's quantitative-biology archive (q-bio) is reported for comparison.

*Medicine.* medRxiv preprints whose title or abstract names a widely reused public dataset or design (NHANES, UK Biobank, Global Burden of Disease, Mendelian randomisation, FAERS, MIMIC-III or MIMIC-IV, SEER or BRFSS) were flagged with a case-insensitive regular expression (S2 Appendix). The list targets datasets and designs associated with formulaic, rapidly scaled analyses [@Suchak2025; @Spick2026] and overlaps with, but differs from, the nine heavily mined datasets identified by Spick et al. [@Spick2026]. The flag was applied to all medRxiv preprints, including those on COVID-19. [AUTHOR: state whether the list was fixed before growth was examined.]

### Heavy producers in arXiv mathematics

arXiv metadata carry no author identifiers, so authors were matched by normalised name strings (accents removed, lower case, characters other than letters dropped). An author name is prolific in a quarter if it appears on five or more mathematics papers first posted in that quarter. The main measure is the share of papers with at least one prolific author, computed by month and by quarter. Namesakes, different people with the same name string, inflate this measure, and so may authors who post finished work in batches. I therefore report three stricter variants: (i) only names whose first given name is written in full are counted (names that begin with an initial are ignored); (ii) as (i), with the 1% most frequent surnames removed (407 surnames, holding 35.7% of author slots); and (iii) as (i), with the 2% most frequent surnames removed (814 surnames; 41.1% of author slots). For Q3 2025 and Q3 2026 I also report the number of authors by papers in the quarter, the prolific share by team size and by primary subcategory, and each prolific author's history since January 2025; histories are left-censored at that date, so an author with no earlier paper is not necessarily new to arXiv. Mentions of AI tools or models, of the Lean proof assistant and of Erdős were matched with regular expressions in titles, abstracts and comments (S2 Appendix). Full texts were not searched, so these counts are lower bounds on mentions of AI use.

### Prevalence of AI-assisted writing

For H3 I compiled published estimates of the prevalence of LLM-assisted writing by field [@Kobak2025; @Liang2025; @LinZhu2025; @Holzwarth2026; @HeBu2025]; because they use different measures (Table 6), only rankings within a study are compared. A marker analysis of the preprints studied here is planned: the excess frequency of LLM-associated words in abstracts, by category and quarter, against a baseline extrapolated from the years before 2023, following Kobak et al. [@Kobak2025]. It estimates prevalence for groups of papers and does not date adoption by an author's first flagged paper, which can create spurious effects [@Renault2026]. [ANALYSIS PENDING: marker analysis, if feasible within the companion analysis.]

### Statistical analysis

The analyses below are being run in the companion analysis; their estimates are marked as pending. Effects are reported as rate ratios with 95% confidence intervals (CIs), not as bare p-values, and only analyses that bear on H1–H3 are included.

*Confirmatory and exploratory tests.* The confirmatory tests are H1's three within-field contrasts in 2026: theory against experiment (physics), computational against wet-lab categories (bioRxiv), and preprints that name a public dataset against other medRxiv preprints, both without COVID-19 preprints. H1 predicts faster growth of the non-experimental group in each. The three tests form one family: each estimate is reported with its 95% CI and a Bonferroni-adjusted (98.3%) CI, and a contrast supports H1 only if the adjusted interval excludes 1. All other analyses are exploratory; where several address one question, as the negative controls and the leave-one-out estimates do, their p-values are adjusted with the Benjamini–Hochberg procedure [@BenjaminiHochberg1995], and no exploratory estimate is used on its own to support a conclusion.

*Rate ratios.* For each contrast, the monthly count of new preprints in group *g* and month *t* is modelled with a Poisson regression with a log link, log E[*y*<sub>*gt*</sub>] = *α*<sub>*g*</sub> + *γ*<sub>*m*(*t*)</sub> + *β*<sub>*p*(*t*)</sub> + *θ*<sub>*p*(*t*)</sub>*D*<sub>*g*</sub>, where *α*<sub>*g*</sub> is a group effect, *γ*<sub>*m*(*t*)</sub> are calendar-month effects for seasonality, *β*<sub>*p*(*t*)</sub> are effects of the periods 2023–2024, 2025 and 2026 against a baseline (2017–2022 for the arXiv archives, 2019–2022 for bioRxiv and mid-2019 to 2022 for medRxiv) and *D*<sub>*g*</sub> indicates the non-experimental group. The quantity of interest is exp(*θ*<sub>2026</sub>), the ratio of the two groups' rate ratios for 2026 against baseline; values above 1 mean faster growth of the non-experimental group. A negative binomial model replaces the Poisson model if the counts are overdispersed. Standard errors are heteroskedasticity- and autocorrelation-consistent (Newey–West) [@NeweyWest1987], with a moving-block bootstrap as a check, and group-specific linear pre-trends are added as a sensitivity analysis. [ANALYSIS PENDING: model choice after the overdispersion check; lag and block lengths.]

*Event study.* Year effects interacted with *D*<sub>*g*</sub>, with 2022 as the reference year, replace the period effects: the coefficients before 2022 test for differential pre-trends, and those for 2023–2026 date any divergence.

*Placebo dates and breaks at unknown dates.* The 2026 interaction is compared with estimates at false break dates within the data before 2023. Breaks in the log ratio of each contrasted pair, and in each field series, are estimated without a pre-specified date by the Bai–Perron procedure for multiple breaks [@BaiPerron1998; @BaiPerron2003] and reported with 95% CIs. [ANALYSIS PENDING: placebo dates as run; minimum segment length; rule for selecting the number of breaks.]

*Negative controls.* H1 predicts no divergence between two series on the same side of a contrast, so the model is also fitted to hep-ex against nucl-ex, to pairs of theory archives (for example hep-th against hep-ph, and gr-qc against nucl-th) and to pairs of wet-lab categories. A divergence as large as in the main contrast would point to heterogeneity among archives or categories rather than to the cost of experiments. [ANALYSIS PENDING: pairs as run.]

*Leave one out.* Each confirmatory contrast is re-estimated without one archive or category at a time, for example without bioinformatics or without hep-th.

*Minimum detectable effect.* For the small experimental physics series (about 430 new submissions a quarter in 2026), the smallest ratio of rate ratios detectable with 80% power at the 5% level is computed from the fitted model, so that a null result can be interpreted. [ANALYSIS PENDING]

*Heavy producers per author.* For arXiv mathematics, the share of active author names with at least five and at least ten mathematics papers in a quarter is computed under each namesake variant, for comparison with Nee et al.'s author panel [@Nee2026], and break dates are estimated for the monthly per-paper share. If feasible, the same measures are computed for the physics theory and experiment archives, where H1 and H2 together predict a rise in theory only. [ANALYSIS PENDING]

*AI-writing markers (H3).* If the marker analysis is feasible, the 2026 growth of each category is regressed on its marker prevalence, its group and their interaction. H3 predicts similar prevalence across groups; H1 predicts a weaker association with output growth in experimental groups. [ANALYSIS PENDING]

For mathematics as a whole, Nee et al.'s synthetic control already provides a counterfactual estimate [@Nee2026], which is not repeated here.

### Robustness checks

These checks are exploratory.

- *Base year.* 2022 was a low year for several series because of the COVID-19 pandemic, so growth is also computed against 2019, and the models are re-estimated without 2020–2021 in the baseline. [ANALYSIS PENDING: models without 2020–2021]
- *Aliased arXiv categories.* Per-archive statistics are compared with the harvested metadata, which count each paper once, by primary category.
- *OSF versions.* Only first versions are counted, so revisions do not inflate the social-science series.
- *arXiv rule changes.* Computer-science review and position papers require prior peer review from 31 October 2025 [@arXiv2025a]; the endorsement of new authors was tightened in mathematics on 10 December 2025 and in all sections on 21 January 2026 [@arXiv2025c]; a full English version of every submission is required from 11 February 2026 [@arXiv2025b]. The models are re-estimated with indicators for these dates. The cap of two submissions per month from 1 October 2026 [@arXiv2026] falls after the study window and was announced and applied on the same day, so it cannot have caused a rush of submissions within the window. [ANALYSIS PENDING]
- *Batch posting.* An author who posts several finished papers at once can cross the five-paper threshold without producing more in that period. [ANALYSIS PENDING: batch-posting check, method to be specified by the companion analysis]
- *COVID-19.* The bioRxiv contrast is compared with the COVID-19 shares of each group in 2022 (Data sources), and the medRxiv contrast uses counts without COVID-19 preprints in both groups. [ANALYSIS PENDING: public-dataset counts without COVID-19 preprints]

### Software and data processing

Data were harvested and processed with Python scripts in the companion analysis (among them harvest_rxiv_categories.py, analyze_within_field.py, robustness_math_prolific.py, plot_paper.py and plot_within_field.py), which write only aggregate counts. [ANALYSIS PENDING: software versions and the scripts for the statistical models.] All scripts and aggregated data will be archived on Zenodo (see Data availability).

### Ethics

The study uses public bibliographic metadata and aggregate counts; no human participants were involved. Author names were processed only to compute aggregate measures; no individual is identified, and only aggregates are reported or released. [AUTHOR: confirm with EMBL's data-protection office whether processing author names from public metadata needs a record under the GDPR.]

### Use of AI tools

This article was prepared with Claude (Anthropic), via Claude Code [AUTHOR: model and version]. Under my direction, AI agents searched the literature, checked references, drafted the text from my brief and skeleton, reviewed drafts adversarially and audited flagged claims against their sources. The harvesting, processing and plotting scripts, and the statistical analyses, were written in a separate AI-assisted session (the companion analysis). I validated the outputs as follows: [AUTHOR: describe, e.g. re-running and reviewing all code; reproducing key counts from the source APIs; reading in full the sources on which the argument depends]. Separate AI agents audited the claims, quotations and rules taken over from the companion essay against their sources, and the bioRxiv index for Q3 2026 (157) was reproduced from bioRxiv's own statistics (13,999 new papers against a 2022 quarterly mean of 8,937.5). The process record, with time, cost, reading depth and the claims new in this article that still need re-checking, is in S1 Appendix. No AI tool is an author.

## Results

### Output grew fastest where experiments do not bind (H1)

#### Growth by field

Fig 1 and Table 2 show new preprints by field. Year on year, Q3 2026 counts were 78% higher than in Q3 2025 in mathematics, 41% in computer science, 29% in medicine (medRxiv without COVID-19 preprints) and 26% in physics, against 10% in biology (bioRxiv) and 6% in the social sciences. Growth since 2022 orders the fields differently: over the last four quarters, biology exceeded its 2022 total by 50%, more than physics (44%) and close to mathematics (59%). Among the natural sciences, biology therefore differs from the other fields in 2026, not in its growth since 2022.

bioRxiv has grown steadily, by 9.5% in 2023, 11.4% in 2024 and 13.0% in 2025, and by 11.7% in January–September 2026 against the same months of 2025 [@bioRxiv2026]; its monthly series shows no break in 2026. Its 2022 base (35,750 new papers) was below its 2020 and 2021 totals (38,717 and 36,866), so growth measured from 2022 starts from a low year. Medicine's 2022 base is also low, because COVID-19 research displaced other work. [ANALYSIS PENDING: Bai–Perron break dates for each field series, with 95% CIs (exploratory).]

#### Theory and experiment in physics

Theory archives (hep-th, hep-ph, gr-qc and nucl-th) grew by 0%, 6%, 6% and 20% in January–September of 2023, 2024, 2025 and 2026, each against the same months of the year before (Fig 2B; Table 3). The 2026 value lies far outside the range of the same statistic over 2017–2025 (−6% to +6%). Experimental archives (hep-ex and nucl-ex) grew by −7%, 7%, 9% and 11%, within their own range (−13% to +22%). Paired by subject, hep-th grew by 24% in 2026 against 14% for hep-ex, and nucl-th by 16% against 2% for nucl-ex. The experimental series is small, with about 430 new submissions a quarter in 2026, and volatile. [ANALYSIS PENDING: confirmatory ratio of rate ratios, theory against experiment, 2026 against baseline, with 95% and Bonferroni-adjusted CIs; event-study coefficients by year; placebo comparison; Bai–Perron break dates for the log ratio; negative controls (hep-ex against nucl-ex; pairs of theory archives); leave-one-archive-out estimates; minimum detectable effect for the experimental series.]

#### Computational and wet-lab biology

Computational bioRxiv categories grew by 7%, 9%, 20% and 18% in January–September of 2023 to 2026; wet-lab categories grew by 9%, 12%, 13% and 8%; and the mixed group by 9%, 11%, 12% and 13% (Fig 2A; Table 3). Computational preprints thus grew slightly more slowly than wet-lab ones in 2023–2024, and faster by 7 points in 2025 and 10 points in 2026. The gap rests mostly on bioinformatics, which grew by 22% in 2025 and 27% in 2026 and made up 63% of the computational group in 2026; genomics grew by 15% and 7%, and systems biology by 21% and 5%. Measured against 2019, wet-lab preprints grew more than computational ones, so the biology contrast is a divergence of 2025–2026, not a long-run difference (see Descriptive robustness checks). arXiv's quantitative-biology archive grew by 19%, 19%, 16% and −7% over the same windows. [ANALYSIS PENDING: confirmatory ratio of rate ratios, computational against wet lab, 2026 against baseline, with 95% and Bonferroni-adjusted CIs; event-study coefficients by year; placebo comparison; break dates; negative controls (pairs of wet-lab categories); leave-one-category-out estimates, including without bioinformatics and without genomics.]

#### Medicine: preprints based on existing data

Without COVID-19 preprints, medRxiv grew by 27% in January–September 2024, 21% in 2025 and 22% in 2026 (each against the same months of the year before), so its growth over these months did not accelerate in 2026, although Q3 2026 alone was 29% above Q3 2025 (Table 2). In 2026, growth was fastest in health informatics (+54%), health systems and quality improvement (+42%), epidemiology (+32%), neurology and radiology (+27%) and oncology (+22%), and close to zero in public and global health (+3%), genetic and genomic medicine (+3%) and infectious diseases (+1%).

Preprints that named one of the public datasets numbered 405 in January–September 2022 (5.0% of all new medRxiv preprints) and 915 in January–September 2026 (6.9%), a 2.3-fold increase against 1.6-fold for all new preprints; in 2026 their share was highest in intensive care (24%; MIMIC) and genetic and genomic medicine (23%). Both counts include COVID-19 preprints, which were 38% of new medRxiv preprints in January–September 2022 and 5% in 2026. Preprints that do not mention COVID-19 grew 2.5-fold over the same months, and from January–September 2023 to the same months of 2026 the flagged preprints and those without COVID-19 both grew 1.9-fold, so the keyword-defined series does not yet show faster growth of preprints that name public datasets. [RECHECK: the 38%, 2.5-fold and 1.9-fold figures were computed for this draft from the companion files within_field_quarterly.csv and medrxiv_public_dataset_quarterly.csv; they are not in the companion README.] [ANALYSIS PENDING: public-dataset counts without COVID-19 preprints; confirmatory ratio of rate ratios, public-dataset against other preprints (both without COVID-19), 2026 against baseline, with 95% and Bonferroni-adjusted CIs; event-study coefficients by year; placebo comparison; break dates.]

The confirmatory estimates, negative controls and leave-one-out ranges for the three contrasts will be summarised in Table 4. [ANALYSIS PENDING: Table 4]

### Heavy producers in arXiv mathematics (H2)

New arXiv mathematics papers rose from 3,197 in January 2025 to 8,360 in September 2026 (S1 Fig), and from 10,846 in Q3 2025 to 19,562 in Q3 2026 (Table 5). The share of papers with at least one prolific author, an author name with five or more mathematics papers in the same quarter, rose from 5.3% in January 2025 to 19.3% in September 2026 (Fig 3A). The monthly share stayed between 3.7% and 6.4% throughout 2025 and in January–February 2026. It then rose to 6.9% in March, 9.4% in April, 11.1% in May, 15.9% in July and 19.2% in September 2026 (values from the robustness script, whose name normalisation differs slightly from the figure's). The rise therefore began seven months before arXiv's cap of 1 October 2026.

The rise survives stricter author matching (Table 5). From Q3 2025 to Q3 2026, the quarterly share rose from 5.3% to 18.1% with all name strings and from 5.2% to 18.0% when only names with a full first name are counted. Removing in addition the 1% most frequent surnames lowers the levels to 1.8% and 5.9%, and removing the 2% most frequent to 1.2% and 4.3%; under every definition the share more than tripled. By month, the strictest series shown in Fig 3A rose from 3.0% in January 2025 to 6.2% in September 2026, roughly a doubling; January 2025 was a high month for this series, whose 2025 values ranged from 1.5% to 3.5%.

Several measures indicate that the rise is broad rather than driven by a few outliers. The number of author names with 5–9 mathematics papers in a quarter rose from 107 in Q3 2025 to 624 in Q3 2026; with 10–19 papers, from 5 to 65; and with 20–49 papers, from 0 to 4; no name had 50 or more in either quarter. Distinct author names rose from 20,108 to 28,279. Of the 693 prolific names of Q3 2026, 143 had been prolific in an earlier quarter, 468 had posted mathematics papers since January 2025 but fewer than five in any quarter, and 82 had posted none since January 2025. The prolific share rose in every team size, from 2.8% to 12.1% for single-author papers and from 11.5% to 28.1% for papers with six or more authors (Table 5). In Q3 2026, papers with a prolific author were most numerous in combinatorics (647 papers; 25% of the subfield) and analysis of partial differential equations (516; 23%), and their share exceeded 13% in each of the twelve subfields with the most such papers, reaching 31% in complex variables (S3 Table).

Between January 2025 and September 2026, single-author papers rose from 30.0% to 37.8% of new mathematics papers, papers mentioning an AI tool or model from 0.09% to 1.97%, and papers mentioning Erdős from 26 to 101 a month (Fig 3B–3D). In Q3 2026, papers with a prolific author mentioned AI tools about as often as other papers (1.9% against 1.6%), the Lean proof assistant somewhat more often (1.6% against 1.0%) and Erdős more often (2.9% against 1.0%). These shares are lower bounds, because only metadata were searched.

Measured per author, the share of active author names with at least five mathematics papers in a quarter rose from 0.6% in Q3 2025 to 2.5% in Q3 2026, and the share with at least ten from 0.02% to 0.24% (computed from the counts in Table 5). In Nee et al.'s pseudonymised author panel, the share of active author units with at least five submissions rose from 2.45% to 3.80%, and with at least ten from 0.21% to 0.49% [@Nee2026]. The units and time windows differ [RECHECK: window and unit of Nee et al.'s panel], so the levels are not comparable, but both measures show a thicker upper tail of output in 2026. [ANALYSIS PENDING: per-author shares under each namesake variant; break date of the monthly per-paper share; if feasible, the same measures for the physics theory and experiment archives.]

### AI-assisted writing across fields (H3)

Every study found that breaks down the prevalence of LLM-assisted writing by field reports it in experimental as well as non-experimental fields (Table 6). By the end of 2023, the share of arXiv abstracts classified as AI-generated had risen, relative to the end of 2022, by 22% in computer science, 11% in quantitative biology (arXiv's q-bio archive, not bioRxiv), 10% in physics and 3.5% in mathematics [@LinZhu2025]. Up to September 2024, LLM-modified text grew most in computer science and least in mathematics [@Liang2025]. In biomedicine, the lower bound for 2024 PubMed abstracts was 13.5% overall and about 20% in computational fields [@Kobak2025], and by the end of 2025, 89% of open-access PubMed Central papers showed an excess of LLM-associated vocabulary [@Holzwarth2026]. One preprint reports slower growth in the life and health sciences than in the physical sciences, a domain that in its classification includes mathematics and computer science [@HeBu2025].

Set against the output results, these estimates give two contrasts. Mathematics, where AI-assisted writing was measured lowest in every arXiv study, had the largest output growth among the natural sciences in 2026. Quantitative biology and physics had similar shares of AI-classified abstracts at the end of 2023 [@LinZhu2025], yet in 2026 physics output accelerated, with the theory archives growing faster than the experimental ones, while bioRxiv output did not. [ANALYSIS PENDING: prevalence of AI-writing markers by group and quarter for the series in this study, and its interaction with experimental intensity in predicting 2026 growth (if feasible).]

### Descriptive robustness checks

Several checks can be made with the descriptive data. Measuring growth from January–September 2019 to the same months of 2026, instead of from 2022, preserves the physics contrast (theory +46%, experiment +34%) but reverses the long-run biology contrast (wet lab +118%, computational +86%), because wet-lab preprints surged in 2020 with COVID-19 research and the late adoption of preprints; the biology result is therefore confined to 2025–2026. The harvested mathematics metadata, which count each paper once, agree with the per-archive series on growth from Q3 2025 to Q3 2026 (80% against 78%). COVID-19 preprints make up similar shares of the 2022 bases of the computational and wet-lab groups (5.1% and 5.9% in May–June 2022). The rise in the mathematics heavy-producer share began in March 2026: after arXiv tightened the endorsement of new mathematics authors on 10 December 2025 [@arXiv2025c], a change that restricts entry rather than easing it, and before the cap of 1 October 2026. [ANALYSIS PENDING: sensitivity to the arXiv rule changes, batch posting and a baseline without 2020–2021 (S4 Table).]

## Discussion

Across preprint servers, output accelerated in 2026 where the work beyond writing is also cheap: in the theory archives of physics, far outside their historical range; in computational biology, from 2025; and in mathematics, where the share of papers with a heavy producer more than tripled within a year, mostly through previously active authors. Experimental physics stayed within its historical range, and bioRxiv, mostly experimental work, kept its steady pace, although AI-assisted writing is common in experimental fields too. Descriptively, these results support H1 and H2 and are consistent with H3; the confirmatory tests are pending. One prediction of H1 is not borne out so far: once COVID-19 preprints are accounted for, medRxiv preprints that name public datasets have not grown faster than other medRxiv preprints.

### Why experimental science is less affected so far

The contrasts are consistent with a simple mechanism: generative AI lowers the cost of the steps that need only text, code or existing data and whose results can be checked cheaply, while experiments cost what they did. Blekhman makes this argument for biology [@Blekhman2026]. For AI used as a research method, Hao et al. find that data availability "appears to be a major impacting factor" in where AI concentrates, while topicality, original impact and funding priority "remain almost unrelated" to it [@Hao2026]. Nee et al. relate the timing of the mathematics break to a capability threshold: "the point at which model performance and available checks make a research task reliable enough for routine workflow adoption" [@Nee2026]. Mathematics fits this account: its results can be checked formally, and papers with a prolific author mentioned the Lean proof assistant and Erdős more often than other papers.

Read together, the results for H1 and H3 suggest that in experimental work AI is in the writing but not yet in the volume. AI-assisted prose is about as common in arXiv's quantitative-biology archive as in physics [@LinZhu2025], and common across biomedicine [@Kobak2025; @Holzwarth2026], yet bioRxiv output kept its pace and experimental physics stayed within its historical range. If this reading is right, the difference between fields lies in what AI can produce, not in who uses it. This is an interpretation; the pending models and negative controls will show whether the contrasts exceed what chance and heterogeneity between series would produce.

Medicine should be the limiting case. Where the data already exist, a biomedical paper needs no new experiment, and the published literature shows the consequence: publications based on nine heavily mined open health datasets reached 3.0 times their 2022 count in 2025 [@Spick2026]; single-factor studies of the US NHANES survey rose from about four a year in 2014–2021 to 190 in 2024 (up to 9 October) [@Suchak2025]; and redundant NHANES publications rose 17-fold between 2022 and 2024 [@Maupin2025]. Letters to the editor, a purely textual output, have grown faster since 2023, with more high-output authors [@Cancellario2026]. In the medRxiv data, health informatics and epidemiology grew fastest in 2026, but the keyword-defined public-dataset series has not outgrown other preprints once COVID-19 is accounted for, so the limiting case rests, for now, on the published literature.

These results describe the situation in 2026, and the binding constraint may move. LLM use is detected later in fields with longer publication timelines, as Kobak et al. note for many biomedical areas [@Kobak2025], and the mathematics break came more than three years after ChatGPT was released [@Nee2026]. Laboratory automation could loosen the experimental bottleneck, first in fields with fast assays. This is speculation, but it means that the data are compatible with a later onset of the acceleration in experimental science, not with immunity to it.

### Counting outputs when AI is used legitimately

The acceleration documented here needs no misuse. In mathematics, most prolific authors had posted papers before, and their papers mentioned AI tools barely more often than other papers. Nothing in these data suggests that the prolific authors misused AI, and nothing in them could separate misuse from legitimate high productivity. Whatever the legitimacy of each paper, a count of papers in 2026 measures something different from a count in 2022, because the cost of producing a paper has fallen unevenly across kinds of work.

The following is an interpretation, not a finding. When AI is used well, the effort behind a paper becomes invisible: a paper that reports real experiments and was written with AI looks like one written without it, and fluent text no longer separates authors who did more work from those who did less. Kusumegi et al.'s finding that LLM use reversed the relationship between writing complexity and paper quality shows this for one signal [@Kusumegi2025], and Blekhman describes how the link between paper and effort has broken [@Blekhman2026]. His concern is the plausible paper produced without research; the concern raised by the present data is real research whose effort no longer shows in the count. A longer argument is set out in a companion essay [@CompanionEssay].

Institutions have so far responded mainly by rationing (Table 1): limits on how many items a person may submit, applied whatever the quality of the work or the conduct of its author. They range from NIH's six applications per investigator a year [@NIH2025] and arXiv's two submissions a month [@arXiv2026] to per-author caps at SocArXiv and at machine-learning venues, two of them tiered by prior acceptance [@SocArXiv2026; @ICLR2027; @AISTATS2027; @ACL2026; @TMLR]. Most caps sit far above what typical researchers submit: NIH expects its cap to affect "a relatively small number of Principal Investigators" [@NIH2025], and even in Q3 2026 only 2.5% of author names in arXiv mathematics had five or more papers in a quarter. Rationing restores the scarcity of submissions but not the information that scarcity carried: a capped researcher reveals which items she considers best, but the count no longer reflects what producing them cost. Review, in Fourie's phrase, is "rationed, not priced" [@Fourie2026], and caps keyed to prior acceptances let past counted success decide who may be counted again, a Matthew effect [@Merton1968] written into the rules.

Reform of what is counted predates generative AI. The San Francisco Declaration on Research Assessment (DORA) asks evaluators to judge research on its own merits rather than by the journal in which it appeared [@DORA], and the Coalition for Advancing Research Assessment (CoARA), whose agreement listed 994 signatories on 16 October 2026, asks for assessment based primarily on qualitative evaluation, with peer review central [@CoARA2022]. Both are largely unimplemented where measured, and mostly unmeasured. The Journal Impact Factor appears in the review, promotion and tenure documents of 40% of research-intensive universities in the United States and Canada, and 87% of the institutions that mention it support its use [@McKiernan2019]. Peer-reviewed publications are a criterion in 95% of the promotion guidelines of 92 biomedical faculties worldwide, and the Journal Impact Factor in 28% [@Rice2020]. A 2026 study for the European Commission found engagement with the reform "broad and growing" but progress uneven [@EC2026], and the searches for this article found no study comparing signatories with non-signatories. Both frameworks also assume that evaluators can read what they assess and that what they read reflects the work behind it. The growth in volume documented here consumes the first of these resources, and legitimate AI use weakens the second.

### Implications for research evaluation

If counts change meaning whatever the legitimacy of the work, remedies need to change what is counted and how it is read, not only who may submit. The proposals below come from published work and are credited to their proposers; none rests on strong evidence of effect, so each would be best introduced as an experiment and evaluated [@NielsenQiu2022]. [AUTHOR: own recommendations to merge.]

1. **Count fewer outputs, and read them; move the cap from those who submit to those who count.** Hiring, promotion and funding panels would each consider a few outputs per period, chosen by the researcher, as CoARA's agreement suggests ("limiting the number of outputs assessed") [@CoARA2022] and as Frith proposed [@Frith2020]; Blekhman concludes that "paper counts are meaningless" [@Blekhman2026]. When the UK's Research Assessment Exercise moved from counting publications to assessing quality, authors shifted towards journals with higher citation impact, but evaluated units later drifted back towards quantity through co-authorship, so a cap at one evaluator does not hold while others still count [@Moed2008]. Once evaluators cap what they read, the submission caps of Table 1 could revert to temporary brakes.
2. **Make effort visible where it counts.** For each selected output, the researcher would supply a record of how it was made, documenting AI use rather than merely disclosing it [@Cwik2026], and discuss it with the panel, which tests understanding as proposed tests of authorship do [@Payan2026; @Hosseini2026]. Such records are costly to read and only partly legible [@Wu2026]; a cap on what counts makes reading them affordable.
3. **Pay for verification, and count it.** Paying reviewers raised the completion of reviews without lowering their quality in a quasi-randomised trial [@Cotton2025] and shortened the time to first decision at a biology journal, in a preprint by its editors [@Gorelick2026]. Reviews, replications and checks of data and code could count among the selected outputs [@Hansen2026; @Hanneke2026]: verification is what cheap generation leaves scarce [@Loven2026; @Ma2026].
4. **Reward exploration directly**, through exploratory grants with extended evaluation horizons, an end to penalties on changing field and indicators of the conceptual distance between a researcher's current and previous work, as Huang et al. propose [@Huang2026]. Long, failure-tolerant funding moved Howard Hughes Medical Institute investigators towards novel lines of inquiry [@Azoulay2011], and partial lotteries among fundable proposals spend no additional reading [@FangCasadevall2016; @Heyard2022].
5. **Build public infrastructure for data and models**: data infrastructure in neglected domains [@Huang2026], open models that institutions can inspect and run themselves [@Spirling2023; @Palmer2024; @HernandezCano2026; @Brzostowicki2026], and contracts that keep researchers' conversations with AI tools out of training data.
6. **Measure the concentration of tools.** If AI-use statements recorded the model family and version in machine-readable form, as delegation taxonomies allow [@Suchikova2025], funders could track whether science converges on a few models, a monoculture that theory and simulations associate with poorer collective outcomes [@Kleinberg2021; @HodelWest2025].
7. **Treat the caps as experiments**, with sunset dates, published data and evaluation of their effects [@NielsenQiu2022].

<!-- D3: shortlist S1–S7 from research note 7 (research_notes/AI academia essay evidence gaps/7_recommendations.md), with credit as in its "Credit" column. Note 7 judged three elements to "appear new" after a quick check (moving the cap from submitters to counters, S1; bounding the evidence of effort by the cap, S2; monitoring model-family concentration, S6). No novelty is claimed here (PLOS ONE does not judge novelty, and the check was not systematic). -->

Looking further ahead, and as speculation, AI could also lower the cost of the resources that evaluation now lacks, reading and checking, for example through syntheses whose citations can be verified [@Asai2026]; whether it does so will depend on what evaluation rewards.

### Limitations

The design is observational: the dates marked in the figures are dates, not causes; other laboratories released models around each marked release; and other changes in 2025–2026, in funding, hiring or conference calendars, could also raise output. The within-field contrasts remove influences common to a field but not those specific to a subfield; slow growth in hep-ex, for example, may reflect the review procedures and data-taking cycles of large collaborations as well as the cost of experiments. Some growth in non-experimental groups reflects AI as a topic rather than as a tool, since much of bioinformatics, like much of computer science, is itself AI research.

The evidence on AI use comes from detectors and marker words, which measure style rather than purpose, are biased against non-native English writers [@Liang2023] and drift as authors drop the words that give them away [@GengTrotta2025]. The published estimates use different measures and cannot be compared in level across studies, and the marker analysis for the series studied here is pending. No measure used here observes AI use in research tasks other than writing.

The heavy-producer measure relies on name strings. Namesakes, batch posting and the left-censoring of author histories at January 2025 affect it despite the stricter variants. Preprints are not publications, and preprint adoption differs between fields; bioRxiv is not intended for opinion pieces, editorials or narrative reviews, the genres that AI makes cheapest, so its counts track primary research and understate any effect on biology's literature as a whole. Changes in the screening policies of bioRxiv and medRxiv, which would affect their counts, were not examined.

arXiv's rule changes of 2025–2026 alter what can be posted, and its cap of 1 October 2026 will break any extension of these series. The experimental physics series is small and volatile. COVID-19 affects the 2022 bases, is removed from medRxiv only through keywords, and is included in the bioRxiv series. The social-science series is small and excludes SSRN and RePEc. The study was not preregistered: the confirmatory tests were fixed before any model was estimated but after the descriptive counts had been seen, so they guard against choosing models after seeing results, not against choosing contrasts.

Finally, the manuscript and the analysis code were produced with AI assistance under my direction, and I reviewed them [AUTHOR: describe the code review]. Errors in generated code could affect the counts; two independent checks agree with them (the bioRxiv index reproduced from bioRxiv's own statistics, and the agreement between per-archive and harvested counts in mathematics), but they do not cover every series.

## Conclusions

In new preprints up to the third quarter of 2026, output accelerated where the work beyond writing is cheap, in mathematics, in theoretical physics and, from 2025, in computational biology, and much less in experimental work, although AI-assisted writing is common there too. In mathematics, the acceleration came from many established authors producing more, not from a few outliers. If the pending model-based analyses confirm these patterns, a publication count now stands for different amounts of work in different fields and years, without any misuse being involved. Evaluation that relies on counts would then need to change what it counts and how it reads, not only how much it accepts.

## Acknowledgments

[AUTHOR: acknowledgements, e.g. anyone who read the draft, checked the code, or checked the passages on Anthropic against primary sources.]

## Data availability

The aggregated counts behind all figures and tables, and the scripts that harvested and processed them, will be deposited on Zenodo (doi:[to be minted]) under [AUTHOR: licence]. The underlying metadata are public: arXiv's per-archive statistics and OAI-PMH interface, the bioRxiv and medRxiv API (api.biorxiv.org) and the OSF API; the scripts re-harvest them. Author name strings are not released; only aggregate measures are. [AUTHOR: PLOS ONE requires the minimal data set to be available without restriction; confirm that the aggregate counts meet this requirement and check each source's terms for redistribution.]

## Funding

[AUTHOR: e.g. "The author received no specific funding for this work." The article-processing charge falls under EMBL's flat-fee agreement with PLOS, which is not research funding; confirm whether it needs mentioning.]

## Competing interests

[AUTHOR: confirm] I have no financial ties to Anthropic or to any other developer of AI tools. This article and its analysis code were prepared with an Anthropic tool (Claude, via Claude Code), and Figs 1 and 3 and S1 Fig mark the release date of an Anthropic model among other dates; other laboratories released models in the same months. A companion essay [@CompanionEssay] discusses Anthropic's data policy. I disclose these as potential non-financial competing interests; S1 Appendix describes how they were handled.

## Author contributions (CRediT)

[AUTHOR: full name]: Conceptualization; Methodology; Investigation (direction and verification of the literature search and of the companion analysis); Formal analysis (direction and review of AI-generated code) [AUTHOR: confirm]; Validation; Visualization (direction) [AUTHOR: confirm]; Writing – review & editing; Project administration. The original draft was generated by an AI tool from my brief and the article's skeleton (Materials and methods, Use of AI tools; S1 Appendix). AI tools are not contributors under CRediT.

## References

<!--REFERENCES-->

## Figure legends

**Fig 1. New preprints by field, Q1 2020–Q3 2026.** New preprints per quarter (first versions only), indexed to each field's 2022 quarterly average (= 100). Physics, mathematics and computer science: new arXiv submissions by primary archive, excluding replacements and cross-lists. Biology: bioRxiv. Medicine: medRxiv, excluding preprints whose title or abstract mentions COVID-19, SARS-CoV-2 or 2019-nCoV (66% of 2020 and 5% of 2026 preprints). Social sciences: first versions on PsyArXiv, SocArXiv and EdArXiv, plus arXiv's econ and q-fin archives. In Q3 2026 the index stood at 162 (physics), 219 (mathematics), 157 (biology), 289 (medicine), 184 (social sciences) and 278 (computer science). Dashed lines mark the release of ChatGPT (30 Nov 2022), arXiv's restriction on computer-science review and position papers (31 Oct 2025), the release of an Anthropic model (24 Jul 2026) and arXiv's cap of two submissions per month (1 Oct 2026); markers are dates, not causes, and other laboratories released models in the same months. Compare trends within a field, not levels across fields. Medicine's 2022 base is low because COVID-19 research displaced other work; aliased arXiv categories put archive sums about 5% above arXiv's official total; the social-science series is small. Data retrieved 15 Oct 2026. File: paper/figures/fig1_index_by_field_175mm (.svg, .pdf, .png; 85-mm versions also available). [AUTHOR: the figure file labels the 24 Jul 2026 marker with the model's name, which the text does not give; decide whether to keep the label, use a neutral label or drop the marker, given the competing-interests statement.]

**Fig 2. Within-field contrasts, Q1 2020–Q3 2026.** New preprints indexed to each group's 2022 quarterly average (= 100). (A) bioRxiv version-1 preprints by subject category: computational (bioinformatics, systems biology, genomics), wet lab (biochemistry; cell, developmental, molecular, plant and cancer biology; microbiology; immunology; physiology; pharmacology and toxicology; pathology; synthetic biology) and mixed (the other ten categories; neuroscience is the largest). The groups were fixed before growth was examined. COVID-19 preprints are included, because the category totals carry no topic flag; they were 5.1% of computational and 5.9% of wet-lab preprints in May–June 2022. (B) New arXiv submissions by primary archive: theory (hep-th, hep-ph, gr-qc, nucl-th) and experiment (hep-ex, nucl-ex). The experimental series is small (about 430 new submissions a quarter in 2026) and volatile. In Q3 2026 the indices stood at 164 (computational), 152 (wet lab), 159 (mixed), 149 (theory) and 119 (experiment). Dashed lines as in Fig 1; the arXiv rule markers apply to panel B only. Data retrieved 16 Oct 2026 from the bioRxiv API (monthly totals per category) and arXiv's statistics. File: paper/figures/fig8_within_field_175mm (.svg, .pdf, .png).

**Fig 3. arXiv mathematics, January 2025–September 2026.** New papers with a primary category in math.\*, by month of first version, from arXiv OAI-PMH metadata harvested on 15 Oct 2026. (A) Share of papers with at least one author who posted five or more mathematics papers in the same quarter: orange, all author names (5.3% in January 2025; 19.3% in September 2026); grey, full first names only, with the 1% most frequent surnames removed (3.0% and 6.2%). (B) Share of single-author papers (30.0% and 37.8%). (C) Share mentioning an AI tool or model in the title, abstract or comments (0.09% and 1.97%). (D) Papers mentioning Erdős (26 and 101 a month). Dashed lines mark arXiv's tighter endorsement rule for new mathematics authors (10 Dec 2025) [@arXiv2025c], the release of an Anthropic model (24 Jul 2026) and arXiv's cap of two submissions per month (1 Oct 2026); markers are dates, not causes. Authors are matched by name strings, so namesakes, and authors who post several finished papers at once, inflate the level of panel A. Keyword matching on metadata undercounts AI use. October 2026 is incomplete and opens a new quarter, so it is excluded. File: paper/figures/fig5_math_profile_175mm (.svg, .pdf, .png). [AUTHOR: as for Fig 1, decide on the label of the Anthropic marker; add one clause on why panel D is shown.]

## Tables

<!--TABLE1 START-->
**Table 1. Per-person limits on submission and related measures, 2025–2026.** Caps, gates and quotas that restore scarcity by rule, and one sanction. Earlier limits existed (arXiv has capped active submissions at three since 2024), and per-author limits on applications and submissions predate generative AI [RECHECK: citation needed, e.g. funders' resubmission rules or pre-2022 conference caps]; none of the measures listed predates 2025. "Cap" means rationing as defined in the Discussion: a limit on how many items a person may submit, whatever the quality of the work or the conduct of its author.

| Effective | Institution | Type | Measure | What is limited | Stated reason | Source |
|---|---|---|---|---|---|---|
| 25 Sep 2025 | NIH (US) | Cap | At most 6 applications per principal investigator per calendar year (T activity codes and R13 excepted); applications "substantially developed by AI" not considered original | Grant applications | AI "enabled Principal Investigators to submit more than 40 distinct applications in a single application submission round"; the cap is expected to affect "a relatively small number of Principal Investigators" | [@NIH2025] (primary) |
| 31 Oct 2025 | arXiv, computer science | Gate | Review/survey and position papers only after acceptance at a peer-reviewed journal or conference (workshop review does not count) | Unrefereed reviews and position papers | "unmanageable influx"; "hundreds of review articles every month" | [@arXiv2025a] (primary); one subfield could lose about half its papers [@ElazarAntoniak2026] |
| May 2026 | arXiv (announced by the chair of its computer-science section) | Sanction (not rationing) | One-year ban where there is "incontrovertible evidence that the authors did not check the results of LLM generation", then prior acceptance at a peer-reviewed venue required | Submission rights of sanctioned authors | Unchecked LLM output (hallucinated references, leftover chatbot text) | [@Dietterich2026] (X thread, 14 May 2026; primary, first post read), quoted in [@Ha2026; @Cole2026]; not on arXiv's policy pages; scope (computer science only or all categories) unclear |
| Mar 2026 (updated 28 Sep 2026) | SocArXiv | Cap | Generally at most 1 paper per author per week; no verbatim AI-generated paragraphs; no "superficial, high-level theory synthesis" | Submissions per author | AI-generated content | [@SocArXiv2026] (primary) |
| 2026 (reported 22 May 2026) | Various Chinese universities | Gate (detector threshold) | Theses above a university-set share of detected AI-generated content may not proceed to blind review and defence | Theses | AI-generated content | [@CCTV2026] (via ScienceNet) |
| Jun 2026 | TMLR (journal) | Cap | Yearly per-author submission budget under the Generalized Harmonic Quota Rule (N₁ = 2, N₉ = 9), each submission costing according to its number of authors [@Shah2026]; doubled for reviewers and action editors; desk-rejected submissions count | Submissions | Submissions tripled in a year, including a 13-fold rise in single-author submissions | [@TMLR] (primary); [@SinghChawla2026a] (news) for the date and growth figures |
| 2027 cycle (announced 28 Jul 2026; papers due 25 Sep 2026) | ICLR 2027 | Cap, tiered by prior acceptance | At most 20 submissions per author; at most 1 paper on which no author has had a paper accepted at a major machine-learning conference or journal; excess submissions randomly desk-rejected; each submission must register an author with such an acceptance to review, unless no author has one | Submissions | "The rapid rate of growth in submissions, while exciting, has begun to strain the review system"; more than 62,000 submissions expected (490 a decade ago) | [@ICLR2027] (primary: author guidelines); [@SinghChawla2026a] (news) |
| 1 Oct 2026 | arXiv, all categories | Cap | At most 2 submissions per submitter per calendar month, and 3 active (the 3-active limit dates from 2024); rejected submissions count; described as a "stopgap" | Submissions | 40,363 submissions in Sep 2026 (20,569 in Sep 2024; 9,869 in Sep 2016) | [@arXiv2026] (primary) |
| ARR cycles from Oct 2026 | ACL Rolling Review (ACL venues) | Cap, plus a lottery | At most 20 submissions per author and 5 as first or joint first author per cycle; each submission must name a qualified reviewer or chair, and submissions without one enter a lottery for spare reviewing capacity | Submissions (reviewing capacity) | "unsustainable rate of submissions at EMNLP'26"; 38% of ~17,000 May 2026 submissions from authors with no available publication record | [@ACL2026] (primary); [@SinghChawla2026a] (news) |
| May 2027 conference | AISTATS 2027 | Cap, tiered by prior acceptance | At most 12 submissions per author; at most 3 for authors without an accepted paper at ICLR, ICML, NeurIPS or AISTATS; excess randomly desk-rejected | Submissions | "Peer review is the scarcest resource of a conference … generative AI tools now make it possible to produce far more manuscripts than the community can carefully evaluate" | [@AISTATS2027] (primary: call for papers); [@SinghChawla2026a] (news) |

*Note.* Conduct rules from 2023–2024 (authorship and disclosure rules; the ban on generative AI in NIH peer review) are not rationing and are not listed [@Thorp2023; @Ganjavi2024; @NIH2023]. arXiv's changes to endorsement (a tighter rule for new authors, in mathematics from 10 Dec 2025 and in all sections from 21 Jan 2026) [@arXiv2025c] and to language requirements (a full English version of every submission from 11 Feb 2026) [@arXiv2025b] are not listed [AUTHOR: list the endorsement rule as a gate?]. Conference rows were checked against each venue's own call or policy on 16 Oct 2026; TMLR's start date and growth figures rest on a news report [@SinghChawla2026a]. False-positive rates reported for thesis detectors are not used, because the reports are anecdotal. All rows are date-sensitive. <!-- Table 1 is the essay's Table 1 (paper/draft_full.md), verified against primary sources in paper/reviews/final_verification.md §3. Omissions left for the author there (§8.5): NIH's stated reason (strain on review); arXiv's stated purpose for the rate limit; AISTATS's 24 Sep 2026 exemption limit and its "Effective" cell (conference date, not submission deadlines); when SocArXiv's weekly limit began; SocArXiv's pause on AI-topic submissions (Nov 2025 to about Feb 2026). -->
<!--TABLE1 END-->

**Table 2. New preprints by field, Q3 2026.**

| Field | Series | Index, Q3 2026 (2022 = 100) | Last four quarters vs 2022 | Q3 2026 vs Q3 2025 |
|---|---|---|---|---|
| Physics | arXiv: astro-ph, cond-mat, gr-qc, hep-\*, math-ph, nlin, nucl-\*, physics, quant-ph | 162 | +44% | +26% |
| Mathematics | arXiv: math | 219 | +59% | +78% |
| Computer science | arXiv: cs | 278 | +146% | +41% |
| Biology | bioRxiv | 157 | +50% | +10% |
| Medicine | medRxiv, excluding COVID-19 preprints | 289 | +139% | +29% |
| Social sciences | PsyArXiv, SocArXiv, EdArXiv (first versions); arXiv econ and q-fin | 184 | +73% | +6% |

Index: Q3 2026 count divided by the field's 2022 quarterly average. Last four quarters: total for Q4 2025 to Q3 2026 against the 2022 total. Compare trends within a field, not levels across fields. Medicine's 2022 base is depressed by COVID-19; bioRxiv's 2022 total (35,750) was below its 2020 and 2021 totals. [ANALYSIS PENDING: counts (n) per field for 2022 and Q3 2026.]

**Table 3. Within-field contrasts: growth of new preprints in January–September of each year, against the same months of the year before.**

| Group | Series | 2023 | 2024 | 2025 | 2026 | Index, Q3 2026 | Range of the same statistic, 2017–2025 |
|---|---|---|---|---|---|---|---|
| Physics, theory | arXiv hep-th, hep-ph, gr-qc, nucl-th | 0% | +6% | +6% | +20% | 149 | −6% to +6% |
| Physics, experiment | arXiv hep-ex, nucl-ex | −7% | +7% | +9% | +11% | 119 | −13% to +22% |
| Biology, computational | bioRxiv: bioinformatics, systems biology, genomics | +7% | +9% | +20% | +18% | 164 | – |
| Biology, wet lab | bioRxiv: 12 categories (Materials and methods) | +9% | +12% | +13% | +8% | 152 | – |
| Biology, mixed | bioRxiv: the other 10 categories | +9% | +11% | +12% | +13% | 159 | – |
| Quantitative biology (comparison) | arXiv q-bio | +19% | +19% | +16% | −7% | – | – |
| Medicine | medRxiv, excluding COVID-19 preprints | +34%<sup>a</sup> | +27% | +21% | +22% | 289 | – |

Paired archives in 2026: hep-th +24% and hep-ex +14%; nucl-th +16% and nucl-ex +2%. Within the computational group, bioinformatics grew by 22% (2025) and 27% (2026) and was 63% of the group in 2026; genomics grew by 15% and 7%, and systems biology by 21% and 5%. The bioRxiv category series start in 2019 and the medRxiv series in mid-2019, so no 2017–2025 range is given for them. Against January–September 2019, theory was +46% and experiment +34% in 2026, and wet-lab +118% and computational +86%. <sup>a</sup> Computed for this draft from within_field_quarterly.csv; not in the companion README [RECHECK].

**Table 4. Within-field contrasts: confirmatory estimates and checks.** [ANALYSIS PENDING: whole table]

| Contrast | Status | Ratio of rate ratios, 2026 vs baseline (95% CI; Bonferroni-adjusted CI) | 2025 vs baseline (95% CI) | Pre-trend (event study) | Placebo dates | Break date of the log ratio (95% CI) | Leave-one-out range |
|---|---|---|---|---|---|---|---|
| Physics: theory vs experiment | Confirmatory | [ANALYSIS PENDING] | [ANALYSIS PENDING] | [ANALYSIS PENDING] | [ANALYSIS PENDING] | [ANALYSIS PENDING] | [ANALYSIS PENDING] |
| Biology: computational vs wet lab | Confirmatory | [ANALYSIS PENDING] | [ANALYSIS PENDING] | [ANALYSIS PENDING] | [ANALYSIS PENDING] | [ANALYSIS PENDING] | [ANALYSIS PENDING] |
| Medicine: public-dataset vs other preprints, both without COVID-19 | Confirmatory | [ANALYSIS PENDING] | [ANALYSIS PENDING] | [ANALYSIS PENDING] | [ANALYSIS PENDING] | [ANALYSIS PENDING] | – |
| Negative control: hep-ex vs nucl-ex | Exploratory | [ANALYSIS PENDING] | [ANALYSIS PENDING] | [ANALYSIS PENDING] | – | [ANALYSIS PENDING] | – |
| Negative controls: pairs of theory archives | Exploratory | [ANALYSIS PENDING] | [ANALYSIS PENDING] | [ANALYSIS PENDING] | – | [ANALYSIS PENDING] | – |
| Negative controls: pairs of wet-lab categories | Exploratory | [ANALYSIS PENDING] | [ANALYSIS PENDING] | [ANALYSIS PENDING] | – | [ANALYSIS PENDING] | – |

Poisson or negative binomial regressions of monthly counts with group × period interactions and calendar-month effects. Ratio of rate ratios: exp(*θ*), the rate ratio of the non-experimental group (in the negative controls, the first-named series) for the period against baseline, divided by that of the comparison group; values above 1 mean faster growth of the non-experimental group. CIs are heteroskedasticity- and autocorrelation-consistent or bootstrap intervals; the Bonferroni adjustment covers the three confirmatory tests (98.3% CIs). Minimum detectable ratio of rate ratios for the physics contrast (80% power, 5% level): [ANALYSIS PENDING].

**Table 5. arXiv mathematics, Q3 2025 and Q3 2026: papers with a prolific author under alternative author-matching rules, and related measures.**

| Measure | Q3 2025 | Q3 2026 |
|---|---|---|
| New mathematics papers | 10,846 | 19,562 |
| Share of papers with a prolific author: all name strings | 5.3% | 18.1% |
| — full first names only | 5.2% | 18.0% |
| — full first names, 1% most frequent surnames removed | 1.8% | 5.9% |
| — full first names, 2% most frequent surnames removed | 1.2% | 4.3% |
| Papers with a prolific author (all name strings), n | 575 | 3,549 |
| Distinct author names | 20,108 | 28,279 |
| Author names with 5–9 papers in the quarter | 107 | 624 |
| — with 10–19 papers | 5 | 65 |
| — with 20–49 papers | 0 | 4 |
| — with 50 or more papers | 0 | 0 |
| Author names with five or more papers, share of distinct names<sup>a</sup> | 0.6% | 2.5% |
| Author names with ten or more papers, share of distinct names<sup>a</sup> | 0.02% | 0.24% |
| Prolific share, single-author papers (n = 3,164; 7,122) | 2.8% | 12.1% |
| — two authors (n = 3,617; 6,197) | 4.2% | 18.5% |
| — three authors (n = 2,572; 4,036) | 7.1% | 23.0% |
| — four or five authors (n = 1,301; 1,976) | 10.2% | 27.9% |
| — six or more authors (n = 192; 231) | 11.5% | 28.1% |
| Papers mentioning an AI tool or model: with a prolific author vs other papers | 0.35% vs 0.23% | 1.92% vs 1.57% |
| Papers mentioning Lean: with a prolific author vs other papers | 0.35% vs 0.05% | 1.63% vs 0.99% |
| Papers mentioning Erdős: with a prolific author vs other papers | 1.57% vs 0.90% | 2.85% vs 1.03% |

A prolific author is an author name with five or more mathematics papers first posted in the quarter. Of the 693 prolific names of Q3 2026, 143 had been prolific in an earlier quarter, 468 had been active earlier with fewer than five papers a quarter, and 82 had no mathematics paper since January 2025 (left-censored at January 2025). In Q3 2026, 2,757 of the 3,549 papers with a prolific author had a newly prolific author [RECHECK: definition of "newly prolific" in robustness_math_prolific.py]. Mentions are matched in titles, abstracts and comments only, so they are lower bounds. Source: the companion analysis (arxiv_math_prolific_robustness.json). <sup>a</sup> Computed from the counts in this table: five or more, 112 of 20,108 and 693 of 28,279; ten or more, 5 of 20,108 and 69 of 28,279.

**Table 6. Published estimates of LLM-assisted writing by field.**

| Study | Corpus and period | Measure | Results by field |
|---|---|---|---|
| Lin and Zhu (preprint) [@LinZhu2025] | 627,384 arXiv papers, 2021–2023 | Share of abstracts classified as AI-generated; increase from the end of 2022 to the end of 2023 | Computer science 22%; electrical engineering and systems science 21%; finance 18%; statistics 15%; economics 11%; quantitative biology 11%; physics 10%; mathematics 3.5% |
| Liang et al. [@Liang2025] | 1,121,912 preprints and papers on arXiv, bioRxiv and *Nature* portfolio journals, January 2020–September 2024 | Estimated share of LLM-modified sentences, at corpus level | Computer science up to 22%; mathematics and *Nature* portfolio up to 9% |
| Kobak et al. [@Kobak2025] | 15.1 million PubMed abstracts, 2010–2024 | Lower bound on the share of 2024 abstracts processed with LLMs (excess vocabulary) | All abstracts at least 13.5%; computational fields (computation, bioinformatics) about 20%; from below 5% to more than 40% across fields, countries and journals |
| Holzwarth et al. (preprint) [@Holzwarth2026] | PubMed Central open-access full texts | Share of papers with an excess of LLM-associated vocabulary | 89% of papers by the end of 2025 |
| He and Bu (preprint) [@HeBu2025] | 5,114 journals, more than 5.2 million papers, 2021–2025 | Growth in the share of AI-assisted text in abstracts | Fastest growth in the physical sciences (a domain that includes mathematics and computer science); slower growth in the life and health sciences |

The measures differ, so levels cannot be compared across studies; only rankings within a study are informative.

## Supporting information

**S1 Appendix. Process record.** How this article and its companion analysis were made: timeline, compute cost, depth to which sources were read, verification steps, division of labour between the author and AI agents, the tool used, a conflict-of-interest note, and the claims and references new in this article that need re-checking.

**S2 Appendix. Definitions and regular expressions.** Assignment of arXiv archives and bioRxiv categories to groups; the regular expressions used to flag COVID-19 preprints, public datasets, and mentions of AI tools, Lean and Erdős; normalisation of author names and the namesake-robust variants.

**S1 Fig. New arXiv mathematics papers per month, January 2025–September 2026.** 3,197 papers in January 2025 and 8,360 in September 2026; Q3 2026 is 80% above Q3 2025 (78% in arXiv's per-archive statistics, which also count aliased categories and run 6–13% higher). Counts are of moderated, announced papers, not submissions. Markers as in Fig 3. File: paper/figures/fig4_math_monthly_175mm (.svg, .pdf, .png).

**S1 Table. Growth by bioRxiv and medRxiv subject category.** New preprints by category for 2022 and January–September 2024–2026, with growth rates, COVID-19 shares and public-dataset shares (companion files biorxiv_categories_growth.csv and medrxiv_categories_growth.csv). [ANALYSIS PENDING: final format]

**S2 Table. Growth by arXiv archive.** January–September growth of hep-th, hep-ph, gr-qc, nucl-th, hep-ex, nucl-ex and q-bio, 2017–2026, with 2017–2025 ranges (from within_field_quarterly.csv). [ANALYSIS PENDING: final format]

**S3 Table. Robustness of the heavy-producer measure.** Quarterly and monthly prolific shares under each author-matching rule, concentration, team size, mentions and subfields (arxiv_math_prolific_robustness.json).

**S4 Table. Placebo dates, break tests and sensitivity analyses.** [ANALYSIS PENDING]

**S1 Data. Aggregated data and scripts.** Aggregated counts for all series and the scripts that produced them (Zenodo, doi:[to be minted]).

<!-- S1APPENDIX START -->

## S1 Appendix. Process record

*How this article was made. Times are UTC. Figures marked [AUTHOR] must be confirmed or completed by the author before submission.*

**Record.** The work ran in AI-assisted sessions in a version-controlled repository, whose history will be archived with the data (doi:[to be minted]). The session that produced this article began at about 21:20 on 15 October 2026. It first produced a companion essay: the literature search started at about 21:27 and the first literature notes were committed at 21:34; my decisions were recorded in the project's brief between 22:25 and 23:25; the agents committed an outline at 00:07 on 16 October, a complete essay draft (6,773 words, 173 references) at 00:58 and an internal adversarial review at 01:29. A usage limit paused the work from about 01:30 to 07:15. Between 07:15 and 09:45 the agents ran a citation audit, revised the essay, researched field differences and recommendations, added the companion analysis's figures and ran a final verification of quotations and rules. My decision to make this research article the main product was recorded at 16:42 on 16 October, when its skeleton, with the title, hypotheses and analysis plan, was committed; a quick novelty check (Nee et al.; Qi et al.) followed at 16:45. An AI agent then wrote this first full draft (v1) from the skeleton, the brief, the companion analysis's outputs and the verified material of the essay, starting at about 16:50 [AUTHOR: add the time v1 was committed]. By 16:45 the branch held 42 commits. The statistical analyses and figures come from a companion analysis, run in a separate AI-assisted session in the same repository; its record is kept separately [AUTHOR: add its timeline].

**Cost.** Compute for this session, subagents included, came to about US$267 by 09:33 on 16 October 2026 (about 5.9 million input tokens, 4.4 million output tokens and 521 million cache-read tokens), with about 20 subagents for research, strategy, outlining, drafting, review, audit and verification. [AUTHOR: update with the final figure, including this draft and the companion analysis.] My own time: [AUTHOR: hours, by phase].

**Reading depth and verification.** For the companion essay, the agents registered 174 factual claims and tagged how each source had been read: 14 (8%) in full, 35 (20%) as a primary document such as a policy or a court notice, 68 (39%) from the abstract alone, 8 (5%) from a search-engine extract and 1 from memory. [RECHECK: the remaining 48 claims are not classified in this tally; complete it from the claims register in paper/outline.md.] Sixty-nine claims were flagged for re-checking. Draft 1 of the essay carried 89 re-check markers, which a separate agent audited against their sources: 57 were verified, 23 corrected and 4 softened, and 5 could not be verified from the drafting environment. A final pass checked 52 quotations (51 verbatim, 1 corrected) and every rule in Table 1 against its primary source. [AUTHOR: add your own reading.] The fluent text shows none of these differences in reading depth.

**New in this article, to re-check.** These items were not covered by the audit or the final verification. Read in this session on 16 October 2026: the arXiv abstract pages of Qi et al., Nee et al., He and Bu, and Hodel and West; Crossref metadata used to complete the reference entries for McKiernan et al., Rice et al., Moed, Cotton et al., Gorelick and Clark, Fang and Casadevall, Heyard et al., Suchikova et al., Liang et al. (2025), Maupin et al., Cancellario et al., Moher et al., Suchak et al., Spick et al., Ganjavi et al., Asai et al. and Hernández-Cano et al.; and the passage of Blekhman (2026) quoted in the Introduction, re-read in the publisher's PDF. Taken from the research notes without a further check: the quotations from Nee et al. (the 2026 break; the capability threshold), DORA and the CoARA agreement; the figures of McKiernan et al., Rice et al., Lin and Zhu, Kobak et al. (computational fields; range), Liang et al. (mathematics), Spick et al., Suchak et al., Maupin et al., Cancellario et al., Moed, Cotton et al., Gorelick and Clark, and He and Bu (life and health sciences). Added from general knowledge, with metadata from Crossref: the methods references of Newey and West and of Bai and Perron. Computed for this draft from the companion files: the medRxiv figures that include or exclude COVID-19 preprints (Results) and the medRxiv growth for 2023 (Table 3).

**Who did what.** I set the question and the thesis, and made the decisions recorded in the brief, among them single authorship, the article as its own documented example, the change of main product from an essay to this research article, the title, and the emphasis on experimental fields [AUTHOR: confirm and complete]. AI agents searched the literature, checked citations, drafted the text (this v1 included), reviewed it adversarially and audited it; in the companion session, AI agents wrote the harvesting, analysis and plotting code under my direction. [AUTHOR: one proposal you rejected; your hours of revision and code review; the sources you read in full.] Contribution taxonomies may be too coarse for sustained interaction of this kind [@Hutchinson2026]; this record documents the work rather than only disclosing it [@Cwik2026].

**Tool.** Claude (Anthropic), via Claude Code [AUTHOR: model and version], on a [AUTHOR: account type] account with model training [AUTHOR: on/off]. Using a proprietary model in research needs explicit justification [@Palmer2024]: [AUTHOR: reason, e.g. no open model available to me could run a multi-step search, verification and drafting workflow of this kind].

**Conflict of interest.** The article was drafted with an Anthropic model, and its figures mark the release date of an Anthropic model; other laboratories released models in the same months. The companion essay discusses Anthropic's data policy and copyright settlement. The internal review came from the same model family. [AUTHOR: name the person or non-Anthropic tool that checked the Anthropic-related passages; confirm that you have no financial ties to Anthropic.]

**Limits of the record.** The record is partial. In one audit of two AI-assisted research repositories, only 21.8% of the narrative trace remained visible in the current version [@Wu2026]; this repository adds a decision log in the brief, but it too is partial. Papers made with AI and disclosed are not new [@Osmanovic2022; @Manabu2026; @Fourie2026]; this record is offered as documentation, not as a first.

### References for S1 Appendix

<!--S1REFERENCES-->

