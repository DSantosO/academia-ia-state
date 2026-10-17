# Referee report R3, round 2: experimental physics and biology

**Manuscript.** "Preprint output in the generative-AI era: pre-specified within-field tests find no robust evidence of an experimental bottleneck". PLOS ONE research article, draft v2, 16 October 2026 (`paper/plos_one/draft_v2.md`).

**Reviewer.** R3, an experimental scientist working in particle and nuclear physics and in wet-lab and computational biology. My round-1 report is `reviews/round1/R3_experimental.md`.

**Date.** 17 October 2026.

**Recommendation.** Major revision, but of a different and bounded kind (section 2). The central reframing asked for in round 1 is done, and done well.

**What I read and checked**

- **Documents.** I read:
  - the manuscript v2 and the point-by-point response;
  - `stats/results.md` and `stats/methods.md`;
  - the pre-registration and Amendment 1, with their appendices and both recorded deviations.
- **The companion branch.** On `claude/happy-lovelace-wqek9b`, up to commit 15df0b1, I read the code that will produce the INSPIRE and pre-registered results:
  - `harvest_inspire.py` and the INSPIRE section of `stats_round1.py`;
  - `nd_design.py`, `nd_frames.py` and `classifier_batches.py`;
  - `classifier_agent_prompt.md` and `make_validation_sheet.py`;
  - `stats_nd_tests.py` and `validation/README.md`.

  I also read the companion's INSPIRE harvest, `data/raw/inspire_hep_records.csv.gz`. It holds curated metadata only, with no names. I read everything with `git show` and changed no file in the repository.
- **What I did not read.** I read nothing the companion committed after 15df0b1, from dacd064 onwards, so that nothing in this review can unblind the author's validation coding. My comments on the registered tests concern their design and their code as of 15df0b1, and this review contains no estimate from them.
- **My own checks.**
  1. **Reproduction.** I reproduced the companion's INSPIRE estimates exactly from its own file and code.
  2. **Re-estimation.** I re-estimated them with the estimator the paper uses for C1–C3, under several bases, by document type and by team size.
  3. **INSPIRE queries.** I ran a few live INSPIRE-HEP queries on 17 October 2026.
  4. **Bias calculations.** I worked through the arithmetic of misclassification bias for the registered estimand.

  Details are at the end. Web sources are cited by URL where used.
- **Line numbers** refer to `draft_v2.md`, which holds one paragraph per line.

**A correction to my round-1 report.** In round 1 I wrote that STAR papers with more than 300 authors "fell from 15 to 5" between January–September 2025 and 2026. That was an artefact.

- **Missing author lists.** In the companion's harvest, 15 of STAR's January–September 2026 records have an INSPIRE author count of 0, because their author lists had not yet been loaded.
- **The collaboration field.** Counted by that field, STAR had 19, 20 and 24 records in January–September 2024, 2025 and 2026 (INSPIRE, 17 October 2026). The ">300 authors" counts for the same years are 6, 15 and 5.

The same artefact affects the paper's team-size breakdown (N2). v2 does not quote my STAR figure, but I withdraw it.

---

## 1. Summary of the changes

**Reframing**

- **Title, abstract, Results, Discussion and Conclusions** now report that the three pre-specified contrasts did not support H1:
  - physics 1.14 (1.00–1.30), inconclusive;
  - biology 1.08 (1.03–1.14), fragile;
  - medicine 1.01 (0.90–1.14), null.
- **H1–H3** are reproduced verbatim, as recorded before modelling (l. 122–124).
- **Table 1 (l. 198–221)** is now a full specification summary, giving for each contrast:
  - Holm p and Bonferroni intervals;
  - in-space placebos, as the primary inference;
  - minimum detectable effects;
  - a year-shock calibration;
  - pooled bases, a cleaned 2022 base and the planned baseline;
  - the 2026/2025 acceleration and the slope change;
  - leave-one-out estimates and negative controls.
- **Methods** now describe the model that was run, with a Deviations section (l. 168). "Pre-specified" is defined honestly: fixed before any model was estimated, not before the data were seen (l. 132).

**Analyses added after round 1**

- **Physics:**
  - Snowmass 2021 and European Strategy papers removed (C1 1.06, 0.89–1.25);
  - C1 without gr-qc, and the particle-physics pairs (hep-ph and hep-th against hep-ex);
  - a genre split for mathematics and the six particle and nuclear archives;
  - list entries.
- **Timing and funding:**
  - break tests that can see 2025–2026;
  - US against other PubMed articles.
- **Medicine:** medRxiv duplicates removed, with flag variants.
- **H2 and H3:** H2 rebuilt on a decomposition by author class; H3 rebuilt on marker words measured in the contrasted groups.
- **INSPIRE:** an exploratory classification of 117,950 INSPIRE-HEP records by a curated-metadata rule (l. 299).

**Discussion**

- The Amdahl-type bound is now in Limitations (l. 329).
- Facility, planning and funding events are dated in S2 Appendix (l. 523–545).
- The evaluation material is cut to about 520 words and labelled as interpretation (l. 315–323). The rationing table is now S1 Table.

**Pre-registration**

- A pre-registration of paper-level tests was activated before any paper was classified. Its tests are:
  - HN, on held-out arXiv archives;
  - Amendment 1 Test A (bioRxiv and medRxiv);
  - Amendment 1 Test B, a dose–response across categories.
- It has two deviations. No results are reported (l. 172).
- **Code and data on the companion branch, as of commit 15df0b1.** There were no classifier labels, estimates, validation sheet or sealed files, only:
  - sampling designs;
  - the medRxiv samples;
  - the estimation script.

**Still unfinished.** v2 carries 53 [AUTHOR], 18 [ANALYSIS PENDING] and 9 [RECHECK] markers.

## 2. Recommendation

**Major revision, bounded.** The paper now says what its pre-specified tests show, and it treats experimental fields fairly in tone. I would support publication once four things are done. None of them needs new data collection except the registered tests themselves.

1. **Correct the INSPIRE claim.**
   - The abstract (l. 104) and Conclusions (l. 333) say that "papers reporting new experimental results grew as fast as the rest". That is not robust.
   - It reverses sign in hep-ex and in nucl-ex depending on the baseline and on how proceedings and planning papers are treated.
   - The rule it rests on does not measure the construct of the refined hypothesis.
   - The Discussion contradicts itself about it (N1, N2).
2. **Fix the registered tests before anyone codes the validation sheet or sees an estimate** (N3–N6). At commit 15df0b1 nothing had been classified. A dated Amendment 2 can repair the following, made before classification if that has not yet run, and in any case before the validation coding and before any estimate is unsealed:
   - a decision rule that cannot be met in code;
   - a dose–response test whose arXiv arm includes the archives where the hypothesis was formed, and mathematics;
   - batches ordered by date;
   - a validation plan too small, and too dependent on one invested coder, to detect the bias that matters.

   If this cannot be done before submission, remove the registered tests from this article. Describe them as forthcoming in one sentence and stop citing them in the Discussion as the place where open questions will be settled. One option is to ask PLOS ONE's editorial office whether it would review the plan as a Registered Report. Its Registered Reports "undergo peer review at the study design or protocol stage, prior to conducting experiments, data collection or analysis" (https://journals.plos.org/plosone/s/what-we-publish). That page does not say how analyses of data that already exist are handled.
3. **Finish or drop the pending analyses.** The ones that matter are ranked in section 6.
4. **Trim three remaining inferences beyond the evidence** (N7).

## 3. Round-1 issues: status

| Round-1 issue | What v2 does (location) | Status | What remains |
|---|---|---|---|
| **M1. Central claim** (title, abstract, H1) | New title. The abstract gives all three contrasts with intervals, placebo p and the two decisive checks (l. 104). Results say "did not support H1" (l. 196). Table 1 is the central display | **Resolved** | The INSPIRE sentence in the abstract and Conclusions (N1) |
| **M2a. gr-qc in theory** | Stated as a misassignment by the paper's own rule (l. 146). C1 without gr-qc is 1.10, 1.02 on the cleaned base and 1.03 against 2017–2019 (placebo p 0.70) (l. 225; Table 1 note) | **Resolved** | – |
| **M2b. hep-ph as "theory"** | The label is kept as pre-specified. The Discussion calls hep-ph "phenomenology fitted to data" (l. 309). hep-ph/hep-ex is 0.97, and 0.88 (0.74–1.04) cleaned | **Resolved** (declining to relabel is acceptable) | – |
| **M2c–e. Archive scopes; small, lumpy experimental group; hep-lat** | MDE 1.21 (1.25 at α/3). Scopes are stated (l. 309). physics.ins-det and physics.data-an are named in S2 Appendix | **Partly resolved** | The reason for leaving out hep-lat is still [AUTHOR] (l. 146). nucl-th/nucl-ex is not reported. Structure-matched placebos are pending (l. 160) |
| **M3. 2022 base (Snowmass) and the range criterion** | Snowmass 2021 and European Strategy papers are removed, using title, abstract and comments: C1 1.06 (0.89–1.25), and hep-ex's departure rises to 1.58. Pooled bases are reported. Range language is gone | **Mostly resolved** | The same cleaning was not applied to the INSPIRE analysis. Its flag reads title and abstract only and finds 61 of the 117 Snowmass papers in hep-ex in January–September 2022 (N1d). C1 was not re-estimated without proceedings |
| **M4. Biology contrast at category level** | C2 is described as fragile in level and confounded with the end of adoption (l. 227) | **Partly resolved** | Pending: structure-matched placebos, the AI-topic split of bioinformatics, and COVID-19 flags on bioRxiv |
| **M5. medRxiv flag** | Spick et al.'s four missing datasets give 1.05. A title-only COVID-19 filter gives 1.07. C3 is called "a weak test of H1" in this venue (l. 229). A coding sheet exists | **Partly resolved** | The sheet codes flagged records only, so it can estimate precision but not recall, which was my round-1 point M5b. C3's slope change is not recomputed after the duplicate correction. Test A on medRxiv supersedes the flag in principle |
| **M6. Alternatives: NIH funding** | PubMed US/non-US: 0.91 in 2026, about 1.7 of the 7 points below trend (l. 295). The prediction for bioRxiv is stated in advance (l. 313, ii) | **Partly resolved** | The bioRxiv US/non-US split is pending |
| **M6. Alternatives: LHC Run 3 and LS3, RHIC, LVK O4 and GWTC-4.0** | Dated in S2 Appendix. Named in Discussion (iii) as "not tested" (l. 313) | **Open** | It can be tested cheaply (section 6, analysis 3). My counts show that collaboration output follows data supply (N2d) |
| **M6. Alternatives: European Strategy** | Removed together with Snowmass. European Strategy input was 5.4% of hep-ex papers in January–September 2025 | **Resolved** | – |
| **M6. Alternatives: instrument time; AI as a topic** | Not mentioned. The AI-topic split is pending for bioinformatics only | **Open** | One sentence on instrument time. AI-topic flags in every NN class (N3) |
| **M7. Mechanism as an Amdahl-style prediction** | The bound is stated with f and s (8% and 54%), and two predictions follow (l. 329). Lags are declined | **Partly resolved** | The bound sits in Limitations. No registered test maps onto it: Test B's dose, the ND share, is not the compressible share (N5c) |
| **M8. H3 in the contrasted groups** | Marker rates for exactly the contrasted groups (Table 2). Kobak et al.'s computational finding is discussed (l. 241) | **Resolved** | Markers by type of paper within hep-ex were not computed. This matters now: hep-ex's composition shifted fast (minor 5) |
| **M9. Fairness of the Discussion** | "Later onset", laboratory automation, "bioRxiv mostly experimental" and "within its historical range" are all removed. nucl-ex's flatness is dated to before 2023 (l. 225) | **Mostly resolved** | Growth in experimental archives is credited to "experimental" papers (section 4.8) |
| **M10. Policy sections tied to the evidence** | Cut to an interpretation-labelled section, with S1 Table and one paragraph of untested proposals | **Partly resolved** | The proposals paragraph (l. 323) and the DORA/CoARA figures (l. 321) are not tied to any finding. "This supports ... the view that evaluation built on counts is not prepared" (l. 319) and "cannot be compared ... as before" (l. 333) overreach (N7) |
| **M11. Plan against run** | Deviations section (l. 168). Approximate planned baselines in Table 1 (1.05, 1.02, 1.05) | **Mostly resolved** | The model estimate under the planned specification is pending |
| **Analysis 2. hep-ex and nucl-ex by mode of production** | INSPIRE classes by author count and document type (l. 299; S5 Table) | **Partly resolved** | Counts by collaboration and a double-coded small-team classification are not done. The size classes need cleaning (N2) |
| **Analysis 3. Pre-registered paper-level test** | Registered, with two deviations. No results in v2 | **In progress** | Design and validation problems to fix before running (N3–N6) |
| **Analyses 6–7. Data-to-paper lags; within-person contrasts with INSPIRE identifiers** | Declined for this version. Lags are stated as a prediction | **Declined** | I still rank data-vintage and lag analyses high (section 6, analysis 3), because they are the only direct test of the mechanism in experimental work |

---

## 4. New major issues

### N1. The INSPIRE result is stated more strongly than the analysis supports, and the Discussion contradicts itself about it

**Location.**

- Abstract (l. 104): "in an exploratory classification of particle and nuclear physics papers, those reporting new experimental results grew as fast as the rest".
- Results (l. 299).
- Principal findings (l. 305): the analysis "did not support its refinement".
- l. 309.
- Conclusions (l. 333).

**(a) The rule separates production modes, not data needs.** ND-INSPIRE requires all of the following:

- a research article;
- in an experimental INSPIRE category;
- linked to an experiment or a collaboration;
- with no prospect wording.

In the companion's own file, for 2017–2026:

| | hep-ex | nucl-ex |
|---|---|---|
| ND records with more than 300 authors | 72% | 55% |
| Records with more than 300 authors that are ND | 97% | 98% |
| Records with at most 10 authors that are NN | 97% | 98% |

"ND against NN" is therefore, to a close approximation, "collaboration papers against small-team papers and proceedings". In hep-ex, ND papers are mostly collaboration analyses of data already on tape. The Discussion acknowledges this (l. 309).

**(b) The NN class combines a rising genre with a falling one.** January–September counts in hep-ex:

| hep-ex, January–September | 2017–2019 mean | 2022 | 2024 | 2025 | 2026 | 2026 / 2017–2019 |
|---|---|---|---|---|---|---|
| ND (research articles, by construction) | 326 | 329 | 425 | 367 | 427 | 1.31 |
| NN research articles (planning papers removed) | 66 | 123 | 172 | 277 | 330 | 4.97 |
| … of which with at most 10 authors | 52 | 86 | 121 | 188 | 249 | 4.82 |
| Conference papers | 178 | 233 | 144 | 127 | 157 | 0.88 |

- **Small-team research articles.** Research articles outside the ND class are overwhelmingly small-team and unlinked. My round-1 sample of such records found mostly simulation, ML and methods papers. Their count grew about fivefold, while proceedings fell.
- **Why the totals match.** The pooled NN class therefore grows at roughly ND's rate only because these two opposite movements offset each other.
- **nucl-ex is different.** It has no small-team surge: NN research articles ran 140–200 a year throughout.

**(c) The ratio depends on the counterfactual and on cleaning.** I applied the estimator the paper uses for C1–C3 to NN against ND. That estimator is a stacked Poisson event study with month fixed effects and Driscoll–Kraay errors (`event_study()` in `stats_round1.py`). For 2026:

| NN / ND, 2026 | Base 2022 | Base 2017–2019 | Base 2019 + 2022 |
|---|---|---|---|
| hep-ex | 1.09 (0.79–1.49) | 1.39 (1.06–1.83) | 1.15 (0.88–1.49) |
| hep-ex, planning papers removed | 1.26 (0.95–1.67) | 1.40 (1.07–1.83) | 1.25 (1.00–1.56) |
| nucl-ex | 1.05 (0.77–1.43) | 0.68 (0.54–0.87) | 0.88 (0.59–1.32) |
| hep-ex + nucl-ex | 1.03 (0.85–1.24) | 1.05 (0.86–1.29) | 1.00 (0.85–1.19) |
| hep-ex + nucl-ex, planning papers removed | 1.12 (0.94–1.34) | 1.06 (0.86–1.29) | 1.05 (0.86–1.29) |
| hep-ex + nucl-ex, research articles only | 1.45 (1.12–1.89) | 1.55 (1.13–2.12) | 1.39 (1.05–1.82) |

- **The archives move in opposite directions.** Against 2017–2019:
  - in hep-ex, papers without new results grew 39% more than those with them;
  - in nucl-ex, they grew 32% less.

  The pooled "1.00" averages these opposite movements.
- **Restricting both classes to research articles.** This is the like-for-like comparison, since ND has no proceedings by construction.
  - In hep-ex, it gives 1.98 (1.39–2.83) against 2022.
  - It gives 1.02 when each class is measured against its own 2017–2022 trend. The trend-based departures are 1.36 for NN and 1.33 for ND.
  - The reason is that research articles outside ND were already growing by 17% a year before 2023.

Whether that pre-2023 growth is extrapolated decides the answer. The paper elsewhere treats extrapolation of group-specific trends as a sensitivity analysis only (l. 162).

**(d) Planning papers were removed in C1 but not here.**

- **The flag misses half of them.** The INSPIRE flag reads titles and abstracts. It finds 61 Snowmass and European Strategy records in hep-ex in January–September 2022. The companion's arXiv flag, which also reads the comments field where Snowmass contributions are declared, finds 117.
- **INSPIRE files them as conference papers.** INSPIRE's own free-text search matches 113 hep-ex records of January–September 2022, and 96 of them are tagged as conference papers.
- **The effect on the estimate.** NN's 2022 level and pre-2023 trend are therefore inflated. This biases the trend-based NN/ND ratio towards 1.

**(e) The interval is not the paper's estimator.**

- **Independent fits.** The reported 1.00 (0.74–1.35) combines two independent field-model fits. In log terms its interval is about 1.6 times wider than the stacked estimate with month fixed effects (0.85–1.24).
- **The variants were not registered.** The registration asks only to "Report the rule variants" (§10). The four variants were defined later, in `stats_round1.py`, so "registered variants of the rule" (l. 299) is inaccurate.
- **One variant is a different construct.** `no_link` (0.75) classes the small-team research articles as ND. It compares research articles with proceedings and is not a variant of the same construct.

**(f) The Discussion contradicts itself.**

- **Two incompatible statements.** l. 305 says the analysis "did not support" the refinement. l. 309 says its rule "does not isolate papers that need new data at the margin". If the rule does not measure the construct, the analysis can neither support it nor fail to.
- **An inaccurate clause.** The same sentence ends "which the held-out tests classify directly". The registered codebook (Appendix A) counts as ND any "new empirical data obtained by the authors", whenever the data were collected. A collaboration's analysis of its own Run 2 data, or the DESI collaboration's analysis of data taken in 2021–2022, is ND under the held-out tests too (N3).

**Why it matters.** The sentence sits in the abstract and the Conclusions. Readers in experimental physics will take it as evidence that experimental work grew like everything else, which this analysis cannot show.

**Fix.**

- **Rewrite the abstract, Results and Conclusions.** Suggested wording for the abstract: "In an exploratory classification of particle and nuclear physics papers by curated metadata, collaboration papers reporting experimental results and all other papers both rose above their pre-2023 levels; their ratio depended on the baseline and on the treatment of proceedings and planning papers, and the rule does not separate analyses that need new data from analyses of data already collected."
- **Delete two passages:** "did not support its refinement" (l. 305) and "which the held-out tests classify directly" (l. 309).
- **Rerun the analysis** as described in section 6, analysis 2.

### N2. The team-size pattern is mostly an artefact; read correctly, the INSPIRE data separate three modes of production

**Location.** l. 299: "Experimental papers with at most 10 authors stood at 1.55 (1.28–1.89) and those with more than 300 at 1.42 (1.10–1.84), while those with 11–300 fell to 0.64 (0.49–0.82)."

**(a) The dip in the middle class comes from 2022.**

- **Against 2017–2019 all three classes grew alike.** January–September counts in hep-ex and nucl-ex grew 1.38-fold for at most 10 authors, 1.36-fold for 11–300 and 1.38-fold for more than 300.
- **The 2022 spike.** The 11–300 class spiked in 2022: 75 conference-tagged records against 6–21 in every other year, plus 34 flagged planning papers. INSPIRE files Snowmass contributions as conference papers. Of the 64 hep-ex conference papers with 11–300 authors in January–September 2022, 53 mention Snowmass (INSPIRE, 17 October 2026).
- **The trend it produces.** The 2017–2022 trend fitted to this class is therefore +10.1% a year. Extrapolated to 2026, it produces the 0.64.
- **After cleaning.** Removing flagged planning papers and conference papers moves the trend-based value to 0.80 (0.67–0.96). The event-study ratio of 11–300 to >300 is 0.96 (0.67–1.36) against 2017–2019, and 1.02 (0.73–1.42) cleaned.

**(b) Missing author lists.** INSPIRE had not yet loaded the author lists of 15 STAR collaboration papers from 2026. Their author count is 0, and the companion's size rule files them as "at most 10 authors". Treat 0 as missing.

- **Effect on the size classes.** It is small here (the small-team trend-based value moves from 1.55 to 1.52), but it is the entire 2026 "jump" in small-team ND papers in nucl-ex (17 records, against 0–9 in earlier years).
- **The general lesson.** Counts filtered by author number are unreliable for recent large-collaboration papers.

**(c) After cleaning, the pattern is monotonic.**

- **Small teams.** With planning papers and proceedings removed, papers with at most 10 authors grew more than those with more than 300: 1.50 (1.12–2.00) against 2022 and 1.51 (1.09–2.09) against 2017–2019.
- **Mid-size and large collaborations** grew alike.
- **All document types together.** With proceedings included, small teams and large collaborations grew alike (0.95–1.04 across bases), because small-team proceedings fell.

**(d) Collaboration output follows data supply.** I counted ATLAS and CMS papers with more than 300 authors and primary hep-ex, January–September, in INSPIRE (17 October 2026). Papers were split by the collision energy named in the abstract:

| ATLAS + CMS, Jan–Sep | 2019 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| All | 126 | 115 | 113 | 164 | 101 | 151 |
| 13 TeV only (stored Run 2 data, 2015–2018) | 106 | 105 | 97 | 146 | 76 | 99 |
| 13.6 TeV (Run 3 data) | 0 | 0 | 3 | 5 | 12 | 36 |

- **Run 2 sits on its pre-AI plateau.** Papers on stored Run 2 data ran at 74–106 a year in 2019–2023, peaked in 2024 and stood at 99 in 2026.
- **Run 1 decayed fast.** Run 1 output (8 TeV, not 13 TeV), for comparison, fell from 130 in 2015 to 10 in 2018.
- **The 2026 rise has two sources.** It comes partly from Run 3 data and partly from a recovery of Run 2 papers after a weak 2025.
- **Data supply behind the rise:**
  - **2024 luminosity.** In 2024 the LHC delivered "124 inverse femtobarns for both the ATLAS and the CMS experiments" (CERN, 25 November 2024, https://home.cern/record-data-lhc-2024).
  - **LHCb.** LHCb's upgraded detector recorded 9.56 fb⁻¹ in 2024, "higher than the sum of integrated luminosities from Run 1 and Run 2" (https://e5.physik.tu-dortmund.de/en/details/ende-der-lhcb-proton-proton-kollisions-aufzeichnung-in-2024-46983/). LHCb papers with more than 300 authors went from 37 in 2024 to 56 in 2026.
  - **BESIII.** BESIII completed "its 15-year campaign to collect 20 fb–1 of e+e– collision data at the ψ(3770) resonance", in "two main running periods, 2010–2011 and 2022–2024" (CERN Courier, 3 May 2024, https://cerncourier.com/a/besiii-passes-milestone-at-the-charm-threshold/). BESIII papers with more than 300 authors rose steadily from 30 in 2017 to 95 in 2026.

These are rough counts from abstract text. Some papers name neither energy, and dates are INSPIRE's earliest date. They show that the question can be answered (section 6, analysis 3).

**(e) How I read the INSPIRE data as an experimentalist.** Three modes of production moved differently:

1. **Small-team work without new data rose strongly.** In hep-ex, research articles by small teams with no experiment link grew fivefold over 2017–2019. They were already growing by about 17% a year before 2023. AI as a tool cannot be separated from ML as a topic, or from a trend that predates ChatGPT.
2. **Collaboration analyses rose with new data.**
   - The 2025–2026 rise in large-collaboration papers tracks new data: Run 3, LHCb Upgrade I and the BESIII samples.
   - Output from stored Run 2 data stayed within its pre-2023 range.
   - Stored collaboration data are where an AI speed-up of "existing-data" analysis would be easiest to see. There is no sign of one. That fits my round-1 point that collaboration review caps output whatever writing costs.
3. **Mid-size collaborations and small nuclear experiments stayed flat.**
   - ND papers with 11–300 authors in hep-ex ran at 68–99 a year throughout.
   - nucl-ex was flat in every class.

**What this means for the new-data hypothesis.**

- **What fits it.** The pattern fits the spirit of the hypothesis: the only strong growth is in work that needs neither new data nor a pass through a collaboration's approval pipeline.
- **What the registered rule shows.** The registered classes (ND = experimental results, NN = everything else) cut across these three modes. That is why the ND/NN ratio is near 1 and fragile.
- **The verdict.** The INSPIRE analysis therefore neither supports nor refutes the hypothesis.
- **The constraints are two.** In collaboration science the binding constraint on stored-data analyses appears to be institutional throughput, and on new analyses data supply. "New data or not" is the wrong single cut.

**Fix.**

- **Replace the size sentence** with the cleaned estimates and this three-mode description, labelled exploratory.
- **Hold production mode fixed in the held-out test.** Add a pre-specified comparison of ND and NN among papers with at most 10 authors (N3).

### N3. Codebook validity: the registered boundary is "data obtained by the authors", not "new data needed at the margin"

**Location.** Pre-registration, Appendix A. Amendment 1, Appendix B. Methods, l. 172.

**The prompts work as genre classifiers.** An experimentalist would agree with most ND/NN labels for typical papers. Rule 3 ("Fabricating and measuring a device or sample is ND; designing or simulating one is NN") and rule 2 (archival data are NN unless the authors obtained new observations) match how physicists and astronomers sort their own work.

**They do not operationalise the hypothesis.** The hypothesis states "what AI can accelerate is work that needs no new data" (§2). The ND definition turns on who obtained the data, not on whether this paper needed a new acquisition. The edge cases the question asks about:

| Case | Registered codebook, as written | Hypothesis ("new data at the margin") | Expected agreement between human and model | Likely bias on the NN/ND ratio |
|---|---|---|---|---|
| Collaboration analysis of its own stored data (LHC Run 2; LIGO O3; a survey team on its own earlier data) | ND ("obtained by the authors") | Existing data | High | Towards 1 |
| The same survey after public release, analysed by non-members | NN (rule 2) | Existing data | High | Towards support in astro-ph in 2025–2026 (below) |
| Reanalysis of public data (GEO, Gaia, CMS Open Data, NHANES) | NN | Existing data | High | – |
| A lab's own previously collected data (neural recordings; a post hoc analysis of the authors' own trial) | bioRxiv: ND ("data they generated"), but its NN list includes "reanalysis". medRxiv: probably NN ("secondary analysis") | Existing data | Low | Inconsistent across servers |
| Instrument or detector paper with test-beam, commissioning or collision data | ND (rule 3) | New data | Moderate | – |
| Instrument design or simulation only | NN | No data | High | – |
| Methods or ML paper with a demonstration dataset | ND if the data are new (rule 1); NN if public | Usually cheap data | Low: abstracts rarely say whether demonstration data are new | Noise |
| Experiment run on cloud quantum hardware | ND (new measurements) | New but cheap data | Moderate | Towards 1 in quant-ph |
| Observational astronomy with the authors' own telescope time | ND | New data | High | – |
| Archival astronomy | NN | Existing data | High | – |
| Data released only to data-rights holders (Rubin DP1) | Ambiguous | Existing data | Low | Noise |
| Clinical: retrospective chart review at the authors' hospital | NN (records) | Existing records, but with real ethics and extraction cost | Moderate | – |
| Diagnostic study measuring stored biobank samples with a new assay | ND ("newly collected … measurements")? | New measurements | Low | – |
| LLM-evaluation study in health informatics | Not covered (NN or U) | No data; AI as the topic | Low | Towards support |
| Genome assembly from new sequencing | ND | New but cheap, templated data | High | Towards 1 |
| Review, perspective, white paper | NN | No data | High | – |

**Four mechanisms deserve particular attention.**

1. **Public data releases flip the class of papers on the same data, at known dates, inside the post-period.**
   - **DESI DR1.** DESI's first data release went public on 19 March 2025 (https://data.desi.lbl.gov/doc/releases/). Its spectra were "taken between May 2021 and June 2022" (https://data.desi.lbl.gov/doc/releases/dr1/). Collaboration papers on those spectra are ND; papers by everyone else after March 2025 are NN.
   - **Euclid Q1.** It was released on 19 March 2025 (https://www.cosmos.esa.int/web/euclid/euclid-q1-data-release).
   - **Rubin DP1.** It was released on 30 June 2025, but "Only Rubin data rights holders may have an account in the Rubin Science Platform (RSP) and access to Data Preview 1" (https://dp1.lsst.io/).
   - **GWTC-4.0** with the O4a strain data followed on 26 August 2025.
   - **Consequence.** NN papers in astro-ph should rise in 2025–2026 without any role for AI. astro-ph is the held-out archive most exposed to this.
2. **AI as a topic is NN by construction.** "Machine-learning methods or software" are NN. ML for materials, astronomy and HEP, and LLM-evaluation studies in medicine, grew for topical reasons. In my round-1 sample, 17 of 60 small-team hep-ex records were ML or AI methods papers.
3. **Cheap data are ND.** Cloud-hardware experiments, commercial sequencing and templated genome notes need new data but little incompressible effort. They weaken the link between ND and the incompressible share.
4. **Dates leak.** The arXiv input includes comments ("Accepted in …", "Proceedings of …", "Contribution to Snowmass 2021"). So "without date or server" (l. 172) is not quite true for arXiv, either for the classifier or for the human coder. That matters for the differential misclassification discussed in N4.

**Where the test is cleanest.** cond-mat and quant-ph laboratory experiments come closest to the hypothesis. There, ND papers are mostly small-team new acquisitions and NN papers are mostly small-team theory and computation, in the same production mode and the same journals. astro-ph is the most confounded arm.

**Fix.** Keep the registered prompts unchanged, since changing them now would be a deviation. Register as Amendment 2, before classification if it has not yet run, and in any case before the validation coding:

1. **A human-coded secondary attribute on the validation sample:**
   - data provenance: new acquisition for this paper, the authors' own stored data, public data, or no data;
   - acquisition mode: facility time, own laboratory, cloud or commercial, or clinical recruitment.

   This estimates, by period and archive, how much of ND is stored-data analysis.
2. **Pre-specified sensitivity analyses:**
   - excluding AI- and ML-topic papers, with a validated keyword flag;
   - excluding astro-ph papers that name DESI, Euclid, Rubin or LSST, Gaia, or GWTC;
   - reporting astro-ph separately.
3. **ND against NN among papers with at most 10 authors**, to hold production mode fixed. The frames built by `nd_frames.py` carry no author counts, so these must be added.
4. **The expected direction of each bias in the table above**, written down before the results.
5. **Comments without dates and journal references** (or no comments) for both classifier and coder, or a check that labels do not change when comments are removed.

### N4. The planned validation would not convince an experimentalist

**Location.** Pre-registration §4; Amendment 1, Validation; Deviations 1 and 2; Methods, l. 172.

**(a) One invested coder, deciding confirmatory status after the estimates exist.**

- **Who codes, and when.** The author formed the hypothesis. Under Deviation 1 the author will code after the estimates are computed.
- **The incentive problem.** κ ≥ 0.60 decides whether results stay confirmatory. Whatever the coder's integrity, results that support the hypothesis then create an incentive to clear the threshold, and results that contradict it an incentive to miss it.
- **Blinding to period is partial.** Comments carry venues and dates. Abstracts carry era cues: JWST, Run 3, 13.6 TeV, O4, and LLM style itself.

**(b) κ ≥ 0.60 is too low a bar for this estimand.**

- **What κ = 0.60 means.** It corresponds roughly to sensitivity and specificity of 0.80 at an ND prevalence of 0.4 (κ = 0.59), or 0.85 at a prevalence of 0.2 or 0.8 (κ = 0.60).
- **Attenuation.** Non-differential misclassification at 0.80 shrinks a true NN/ND ratio of 1.20 to an observed 1.11, and a true 1.50 to 1.26.
- **What the test can detect.** The expected minimum detectable effect of 1.15–1.20 (Deviation 2) applies to the observed ratio. The detectable true ratio is about 1.35 or more. A null would then say little.

**(c) The quantity that matters is drift between periods, and the validation cannot detect it.** Suppose the true ratio is 1, ND prevalence is 0.4, and sensitivity and specificity are 0.85 in the pre-period. A shift of 5 percentage points in one error rate in 2025–2026 produces an observed ratio of 0.89–1.13. At bioRxiv-like prevalence (80% ND), a 5-point fall in sensitivity alone produces 1.21, which exceeds the expected MDE.

Plausible sources of such drift:

- LLM-written abstracts, which are more templated;
- the classifier's familiarity with older papers;
- chronologically ordered batches (d).

The validation cannot pick this up:

- **Its size.** It has about 100 papers per period per domain: 50 and 50 for bioRxiv and for medRxiv; 34/33/33 per archive and period for arXiv.
- **Its periods** are 2019–2022 and 2023–2026, which do not match the estimation windows (trend 2017–2022, post-period 2025–2026).
- **What detection would need.** Detecting a difference between error rates of 0.15 and 0.20 needs about 900 papers of one class per period. Detecting 0.15 against 0.30 needs about 120.

**(d) The labels validated are not the labels used.**

- **Separate sample and run.** The validation sheet is a separate random sample (`make_validation_sheet.py`), and its model labels come from a separate classifier run.
- **Chronological batches.** The estimation input `classifier_input_full.json` is sorted by paper key, that is by arXiv identifier or DOI, which means by date. It is cut into batches of 50 in that order (`classifier_batches.py`).
- **The consequence.** Each sub-agent context holds papers from the same few months. With temperature not settable, any run-to-run or context effect is confounded with calendar time.

**(e) κ by domain hides problems.**

- **The prevalence paradox.** With a high ND prevalence on bioRxiv, κ can fail despite high accuracy, or pass with poor recall of the minority class.
- **Pooling across archives.** For arXiv, one κ pools cond-mat, astro-ph and quant-ph, although astro-ph's survey and archival cases are much harder.

**(f) Blinding is not yet in place, and the frame differs.**

- **No hashes yet.** `validation/README.md` shows the SHA-256 hashes as "(added when the file is committed)". At commit 15df0b1 neither the sheet nor `sealed/` existed.
- **A narrower frame.** The bioRxiv and medRxiv validation frame is restricted to Creative Commons licences. If funder mandates make primary-data studies more often CC-BY, the restriction selects on class.

**Fix.** Register, before the validation coding begins:

1. **Sealed estimates.** Compute and seal the estimates, committing their hash, so that the coder codes before seeing them. This restores the registered order in substance.
2. **Independent coders.** Add at least one independent coder per domain who has not seen the results, as a mandatory rather than optional step. I suggest a condensed-matter or AMO experimentalist, an observational astronomer and a clinical epidemiologist. Report human–human κ as the ceiling for model–human κ.
3. **A validation sample matched to the estimates:**
   - drawn from the estimation sample, with the labels actually used;
   - stratified by the estimation periods (2017–2022 and 2025–2026);
   - stratified by model label, oversampling the minority class.
4. **Error rates and a corrected estimate:**
   - sensitivity and specificity by period and archive, with intervals;
   - a misclassification-corrected ratio with period-specific confusion matrices, with the validation uncertainty propagated by bootstrap;
   - a tipping-point analysis giving the drift in sensitivity or specificity needed to move the ratio to 1.
5. **Batch checks:**
   - shuffle batch composition across months, if classification has not yet run;
   - in any case, re-classify a random 10% in shuffled batches as a test–retest check, without replacing labels;
   - report the U share by period.

With these in place, κ ≥ 0.60 can remain as a floor.

### N5. Test B, as designed, is not a good test of the mechanism

**Location.** Amendment 1, Test B; Deviation 2; `nd_design.py`.

**(a) Its arXiv arm is not held out.**

- **What `nd_design.py` includes:**
  - the subcategories of cond-mat and astro-ph, and quant-ph;
  - "math subcategories";
  - "the archives hep-th, hep-ph, gr-qc, nucl-th, hep-ex and nucl-ex".
- **Mathematics:**
  - ND ≈ 0 by definition;
  - its 2026 departure of 1.48 is already reported;
  - it carries its own shocks: the endorsement rule of 10 December 2025 and the September 2026 spike.
- **The six physics archives** are where the hypothesis was formed and the INSPIRE analysis was run.
- **When this was chosen.** Amendment 1 names "arXiv subcategories with at least 300 new papers a year" but not these. The design script chose them after archive-level growth was known.
- **The consequence.** About half of the arXiv arm consists of mathematics categories that sit at zero exposure with known high outcomes. The arXiv slope is close to negative by construction, and one more server suffices for "negative in at least 2 of the 3 servers".

**(b) It is ecological, and confounded where exposure is low.** Low-ND categories are where AI is the topic: bioinformatics, health informatics, cond-mat.dis-nn. Categories also differ in adoption history and propensity to post.

**(c) The exposure is not the dose in the Amdahl sense.**

- **Wrong quantity.** The share of papers reporting new data is not the incompressible share of effort. Cheap-data categories such as genomics and cloud-hardware quant-ph have high ND and high compressibility.
- **Measurement error.** The share is estimated from 150 papers per category, with a standard error of about 0.04. That attenuates the slope.

**(d) The outcome relies on trends the paper rejects elsewhere.**

- **bioRxiv and medRxiv.** Trends are fitted to 2019–2022. With a 2020–2021 indicator, they rest mainly on 2019 and 2022. The manuscript itself calls such extrapolation not credible for C2 (l. 162), and labels medRxiv's trend "not interpreted" (Table 3).
- **Inconsistent dating.** Mathematics is dated by announcement month with a 2019–2022 window, the six HEP archives by announcement, and the held-out archives by first-version submission.

**(e) The inclusion rule changed without being recorded.**

- **What the deviation says.** Deviation 2 drops or pools categories with fewer than 150 eligible papers.
- **What the code does.** `nd_design.py` keeps only categories with at least 300 and drops the rest. For medRxiv this leaves 15 categories. It drops 13 that have 163–285 eligible papers, among them health systems, obstetrics, ophthalmology and respiratory medicine.
- **Unrecorded.** This is a further deviation and is not recorded.

**(f) Some inference details are unstated.**

- **One-sided test.** The permutation p-value is one-sided in the code (`stats_nd_tests.py`), which the amendment does not state.
- **Unweighted slope.** The slope is unweighted, so categories of very different precision count equally.
- **Power.** "The main gain in power" is asserted, not calculated. Power is set by between-category heterogeneity, which pre-2023 placebo years could calibrate on arXiv.

**Is it a good test?** A gradient is the right kind of test, but this one runs between categories that differ in much else.

**Two better tests:**

1. **A within-category gradient over types of paper.** Rank types in advance by expected compressible share:
   - reviews and perspectives;
   - ML methods and theory;
   - simulation;
   - reanalysis of public data;
   - collaboration analysis of stored data;
   - new laboratory measurement;
   - facility-based new measurement (beam or telescope time);
   - prospective clinical study.

   Classify the samples into these types (the human-coded attribute in N3), and test monotonicity within archives.
2. **Natural experiments in data supply.** The data available without new acquisition change on a known date for a known subfield: DESI DR1, GWTC-4.0, CMS Open Data releases. Lags from release to paper are the mechanism's most direct prediction.

**Fix.**

- Restrict the confirmatory arXiv arm to held-out subcategories.
- Report mathematics and the six HEP and nuclear archives separately, as non-confirmatory.
- Record the change in the inclusion rule.
- Weight by precision and state that the test is one-sided.
- Otherwise, demote Test B to exploratory.

### N6. Implementation problems to fix in a dated Amendment 2

These points refer to the code at commit 15df0b1, when no labels or estimates existed. I have not read later commits; if the code has changed since, check whether each point still applies. Fixed before any estimate is seen, they cost no confirmatory status:

1. **Test A can never be "supported" in code.** `hn_like()` requires the unit-specific ratio to exceed 1 in at least 2 units, but Test A has one unit per server. The registered rule for Test A needs stating, for example "ratio > 1 with a 95% interval excluding 1".
2. **The 2019 placebo and the "trend 2017–2019 only" variant mean nothing for bioRxiv and medRxiv.** Their series start in 2019, and with a 2020–2021 indicator the placebo compares 2019 with 2022 through within-year slopes. Declare no placebo for Test A, or specify one that the data can support.
3. **Test B is not implemented.** `main()` never calls `dose_response()`, and no outcomes are computed. Fix the outcome code before labels exist.
4. **Only three of the six registered sensitivity analyses are wired.** The three are: excluding September 2026, U as NN, and the 2017–2019 trend. Announcement dating, excluding reviews and white papers, and excluding papers with more than 50 authors are not. The last cannot be run from the frames as built.
5. **Chronological batches** (N4d).
6. **The bootstrap does not carry misclassification.** The docstring says "sampling and classification noise enter the intervals". Resampling classified papers carries the sampling noise of class shares, not systematic misclassification. Say so in Methods.
7. **Sealing, and the Test B inclusion rule** (N4f; N5e).
8. **The estimand should be co-reported.** Report the estimate both against class-specific trends, as registered, and as level ratios against pooled bases (2017–2019; 2019 + 2022), as for C1–C3. N1c shows how far the two can diverge when one class had a steep pre-2023 trend.

### N7. Three inferences still go beyond the evidence

1. **The inference about Qi et al.** l. 309 says that "Within fields, computational intensity did not predict where output grew, which suggests that the differences between fields reported by Qi et al. [11] partly reflect servers and their author populations".
   - **Why it fails.** Contrasts based on labels that the same paragraph calls weak proxies, with an MDE of 1.21 in physics, cannot carry this.
   - **Suggested wording.** "These label-based contrasts could not detect a difference, so they neither corroborate nor refute Qi et al.'s between-field finding."
2. **The inference about evaluation.** l. 319 says "This supports, at the strength the data allow, the view that evaluation built on counts is not prepared for widespread use of AI". The data contain no measure of evaluation.
   - **Keep** the two data-tied points: counts moved unevenly across servers; and measured AI-assisted writing cannot be used to adjust them.
   - **Move** the proposals paragraph (l. 323) and the DORA/CoARA figures (l. 321) to the companion essay, with a one-sentence pointer.
3. **The comparability claim.** l. 333 says the data "show that preprint counts from 2026 cannot be compared with those of earlier years, or across servers, as before". The data show that 2026 counts departed from their trends by amounts that differ across servers and archives, for reasons not yet identified.
   - **Suggested wording.** "Comparisons of 2026 counts with earlier years or across servers need series-specific baselines."
4. **Two smaller points of the same kind:**
   - l. 313 (iv) says the registered tests examine the question "in archives where the idea was not formed". Test B includes those archives (N5a).
   - l. 313 (iii) says the timing of facility cycles "was not tested". It can be tested, and the first counts point to data supply (N2d).

### 4.8 Fairness to experimental fields, and the wording of H1

**Is the Discussion now fair?** In tone, yes:

- the "late adopter" framing is gone;
- the rise of the experimental archives is reported;
- marker words rose in experiment as in theory;
- nucl-ex's flatness is dated to before 2023.

**Two residual problems:**

1. **The paper credits experimental work with growth that is mostly non-experimental work filed in experimental archives:**
   - "experimental particle physics included" in the abstract (l. 104);
   - "Experimental papers with at most 10 authors stood at 1.55" (l. 299);
   - "in hep-ex, as large a departure of output from trend" as the evidence against H1's second clause (l. 271).

   In hep-ex, 97% of records with at most 10 authors are outside the ND class. Fairness cuts both ways: experimentalists should not be called slow, but they should not be credited with output that is simulation and ML filed under hep-ex. Write "the experimental particle-physics archive (hep-ex)" where the archive is meant.
2. **Collaboration output is read without its data-supply context** (N2d).

**Is "not supported so far" the right wording?** No. "So far" implies an expectation that support will come. It reintroduces the "later onset" reading that I asked to remove in round 1, and it has no registered horizon. I would write:

> "H1 was not supported by its pre-specified tests: the physics contrast was inconclusive, the biology contrast fragile and the medicine contrast null. Its second clause does not describe the experimental particle-physics archive, whose output departed from its trend as much as the theory archives did; whether experimental work as such responded to AI cannot be determined from counts."

If the author wants a forward-looking statement, register a prospective test first:

- a horizon, for example 2027–2028;
- a magnitude;
- covariates for LS3 (from July 2026), RHIC's post-run analysis and US funding.

Then cite it.

---

## 5. Minor issues

**Abstract and Results text**

1. **Abstract, l. 104.** Replace "experimental particle physics included" with "the experimental particle-physics archive (hep-ex) included" (section 4.8).
2. **l. 299.** "Experimental papers with at most 10 authors" should read "papers with at most 10 authors in hep-ex and nucl-ex (97–98% of them outside the ND class)". Report the size classes with author count 0 treated as missing.
3. **l. 299, "from curated metadata and without AI".** The prospect flag is a regular expression on titles and abstracts, written after the registration. It matches phrases common in measurement abstracts ("prospects", "future measurements", "expected sensitivity"). The prospect variants show the ND/NN ratio barely moves (0.97–1.05), so say that.
4. **l. 299, the interval 0.74–1.35.** It comes from independent fits. Label it as such or replace it with the stacked estimate (N1e).
5. **l. 241, l. 271 and Table 2: markers in "physics experiment".** hep-ex's composition shifted fast: research articles outside ND went from 172 in 2024 to 330 in 2026. The larger rise in 2025–2026 (theory/experiment 0.75) may therefore reflect composition rather than how experimentalists write. Compute marker rates by INSPIRE class within hep-ex by matching arXiv identifiers. This was my round-1 M8 request.
6. **l. 313 (iii).** Add the data-supply facts with their sources (N2d), and add them to the S2 Appendix timeline.
7. **S2 Appendix timeline (l. 523–545).** Add DESI DR1 (19 March 2025), Euclid Q1 (19 March 2025) and Rubin DP1 (30 June 2025, data-rights holders only). They bear on the held-out astro-ph arm (N3).

**Data, code and documentation**

8. **INSPIRE author counts.** Treat `author_count` 0 as missing (N2b). In S2 Appendix (l. 521), note that the `ac` filters miscount recent collaboration papers whose author lists are not yet loaded. My round-1 STAR figure is an example.
9. **INSPIRE planning-paper flag.** Match arXiv identifiers to the OAI harvest, so that comments are read as they are in P1b.
10. **hep-ex's composition changed in 2026, for reasons I could not find.** In January–September:
    - papers cross-listed to physics.ins-det fell from 135 in 2025 to 43 in 2026;
    - cross-lists to cs or stat rose from 20 to 49.

    These are the arXiv categories in the INSPIRE harvest. I found no arXiv announcement about cross-listing. Find the cause before reading hep-ex's 2026 composition, since instrument papers are ND under Appendix A rule 3.
11. **`results.md`, table P1c.** The C3 row (0.99, 0.88–1.10; 2026/2025 1.08) seems to predate the duplicate correction. v2 uses 1.01 and 1.10. Regenerate it.
12. **Methods l. 142, [RECHECK] on INSPIRE.** The API documentation says:
    - "every IP address is allowed 15 requests in a 5s window";
    - "most of the metadata is available under a CC0 license, but restrictions apply to some fields, and bulk collection of email addresses is not allowed";
    - the maximum page size is 1000 (https://github.com/inspirehep/rest-api-doc).

    `harvest_inspire.py` pauses 1 s between requests, uses pages of 1000 and stores no names or e-mail addresses. It complies, so cite the documentation and remove the marker.
13. **Methods l. 172 should state:**
    - the validation size per domain (200, 100, 100) and its periods;
    - that Test B adds exposure samples of 150 per category (2,250 for medRxiv alone);
    - that Test B includes mathematics and the six HEP and nuclear archives;
    - that arXiv input includes comments.
14. **medRxiv flag check.** The coding sheet samples flagged records only, so it estimates precision but not recall. Either add unflagged secondary-data studies or let Test A replace the flag check.
15. **hep-lat.** The reason is still [AUTHOR] (l. 146).
16. **Instrument time.** Beam, telescope, synchrotron and cryo-EM time are allocated in proposal cycles. AI can raise the number of proposals, not the time allocated. One sentence in Discussion (iii) or Limitations.
17. **Response document, R3-M4 ("Dose–response against measured experimental intensity: Pending").** The amendment's exposure is the ND share judged from abstracts. It is not the intensity I asked for, the share of papers depositing new GEO, SRA, PRIDE or EMPIAR data. Say so.
18. **S2 Appendix description of my round-1 sample (l. 521).** It is accurate. The harvest corroborates it: 97% of hep-ex records with at most 10 authors are NN-INSPIRE, and only 3% are ND.

## 6. Requested analyses, ranked by information value

### 1. A dated Amendment 2 before the validation coding (fixes in N3–N6)

**What to do.**

- Fix the Test A decision rule, the placebo for bioRxiv and medRxiv, and the code for Test B.
- Restrict Test B's confirmatory arXiv arm to held-out subcategories.
- Shuffle batches or, if classification has run, re-classify a shuffled 10% subset.
- Keep the estimates sealed until the coding is done.
- Draw the validation from the estimation sample, by estimation period, with an independent second coder.
- Pre-specify:
  - the misclassification correction and the tipping-point analysis;
  - the AI-topic and data-release sensitivity analyses;
  - the comparison among papers with at most 10 authors;
  - level-based ratios against pooled bases.

**Cost.** Hours.

**Why it ranks first.** It decides whether the registered tests can be read at all.

### 2. Redo the INSPIRE exploratory analysis

**What to do.**

- Use the C1 estimator under every base: 2022, 2017–2019, and the pooled bases.
- Remove planning papers using arXiv comments.
- Restrict both classes to research articles, and report proceedings separately.
- Treat author count 0 as missing.
- Report hep-ex and nucl-ex separately.

**Cost.** Hours.

**Why it ranks second.** It decides what the abstract and Conclusions can say about experimental physics.

### 3. Collaboration output by data vintage, and lags

This is Amendment 1's exploratory measure of data-normalised output.

**What to do.**

- For ATLAS, CMS, LHCb, ALICE, BESIII and Belle II, count papers per year by dataset. Identify the dataset by:
  - collision energy or luminosity string in the abstract;
  - the BESIII samples.
- Normalise by the integrated luminosity available.
- Model each dataset's lifecycle against Run 1 and pre-2023 Run 2.
- Measure lags from the end of data-taking, or from the public CONF/PAS note, to the arXiv paper.

**Cost.** One to three days. My counts in N2d show that it can be done.

**Why it matters.** It is the most direct test of "AI speeds analysis of existing data" in a setting where the data are fixed and well documented. It also separates data supply from institutional throughput.

### 4. bioRxiv, US against non-US authors (pending)

**Cost.** Hours; the classifier already exists.

**Why it matters.** It separates the 2025 US funding shock from AI as the cause of the 2026 wet-lab slowdown.

### 5. AI-as-topic flags in every NN class

**What to do.**

- Flag AI and ML topics in bioinformatics, health informatics, small-team hep-ex, cond-mat and quant-ph.
- Validate the flag on a sample.
- Re-run C2, and the held-out estimates as a sensitivity analysis, without these papers.

**Cost.** Hours to days.

**Why it matters.** It separates topic from tool. The confound affects every NN class.

### 6. Contrasts within the same people, using INSPIRE author identifiers

**What to do.** Compare the output of collaboration members outside the collaboration with their collaboration output, 2017–2026.

**Cost.** Days.

**Why it matters.** It holds people fixed. It tests directly whether the same experimentalists produced more work that needs no new data.

### 7. Structure-matched placebos for C1 and C2 (pending)

**Cost.** Hours.

**Why it matters.** Its value is modest now that H1 is reported as not supported, but it completes the description of C1 and C2.

### Analyses I do not ask for

- **Rambachan–Roth bounds and fixed-b critical values.** I agree with declining both.
- **OpenAlex journal output**, for this article.
- **Recall of the medRxiv flag**, if Test A runs.

## 7. Strengths

- **The reframing is complete and honest.**
  - H1 is kept as recorded and reported as not supported.
  - Table 1 is a model of how to show one estimate under every reasonable specification, with the negative controls in view.
- **Inconvenient checks are reported.**
  - Removing the Snowmass and European Strategy papers made hep-ex's acceleration larger, against the narrative of v1, and the paper reports this plainly.
  - The medRxiv duplicates were found and corrected, though they changed a headline growth rate.
- **Registration discipline is unusually good for a project of this kind:**
  - the plan was activated before classification;
  - deviations are dated;
  - the sampling design is fixed in code with seeds per stratum;
  - the estimation code was written before any label existed;
  - hash-sealing of the validation key is planned;
  - archives are held out;
  - results are labelled "pending human validation".

  The problems I raise in N3–N6 are fixable precisely because this was done in the right order.
- **The INSPIRE classification uses curated metadata without AI**, which is the right instinct. It is reproducible: I reproduced every reported number exactly from the committed file. The harvest kept within INSPIRE's documented limits and stored no names.
- **H2 and H3 are now measured correctly.**
  - H2 uses a decomposition on combined output, which avoids regression to the mean.
  - H3 uses marker rates in exactly the contrasted groups, with the drift of the words stated.
- **Transparency.**
  - The AI-use statement says what the author originated.
  - The internal reviews are not presented as peer review.
  - S2 Appendix gives a dated timeline of facility, planning and funding events with sources.

---

## Sources consulted on the web (accessed 16–17 October 2026)

**Particle and nuclear physics: data supply**

- **CERN, 25 November 2024** (https://home.cern/record-data-lhc-2024): 2024 integrated luminosity "reached 124 inverse femtobarns for both the ATLAS and the CMS experiments".
- **TU Dortmund, 28 October 2024** (https://e5.physik.tu-dortmund.de/en/details/ende-der-lhcb-proton-proton-kollisions-aufzeichnung-in-2024-46983/): LHCb recorded 9.56 fb⁻¹ in 2024, "higher than the sum of integrated luminosities from Run 1 and Run 2".
- **CERN Courier, 3 May 2024, "BESIII passes milestone at the charm threshold"** (https://cerncourier.com/a/besiii-passes-milestone-at-the-charm-threshold/): the 20 fb⁻¹ ψ(3770) campaign completed, in "two main running periods, 2010–2011 and 2022–2024".

**Astronomy: 2025 public data releases**

- **DESI data releases** (https://data.desi.lbl.gov/doc/releases/): "Data Release 1 (DR1) — March 19, 2025".
- **DESI DR1 documentation** (https://data.desi.lbl.gov/doc/releases/dr1/): Main Survey spectra "taken between May 2021 and June 2022".
- **ESA, Euclid Quick Data Release Q1** (https://www.cosmos.esa.int/web/euclid/euclid-q1-data-release): released 19 March 2025.
- **Rubin Observatory DP1** (https://dp1.lsst.io/): released 30 June 2025; "Only Rubin data rights holders may have an account in the Rubin Science Platform (RSP) and access to Data Preview 1".

**Data source and journal**

- **INSPIRE-HEP REST API documentation** (https://github.com/inspirehep/rest-api-doc): the rate limit, the CC0 statement and the maximum page size, quoted in minor issue 12.
- **PLOS ONE, What we publish** (https://journals.plos.org/plosone/s/what-we-publish): Registered Reports "undergo peer review at the study design or protocol stage, prior to conducting experiments, data collection or analysis".

**Not found.** A search for a 2025–2026 arXiv change to cross-listing turned up no such announcement (minor issue 10).

**From my round-1 report, not re-checked:**

- the CERN schedule for LS3 (https://home.cern/updated-schedule-cerns-accelerators);
- RHIC's final run (https://www.bnl.gov/newsroom/news.php?a=122794);
- LVK O4 (https://ligo.org/ligo-virgo-kagra-collaboration-successfully-wraps-up-its-fourth-observing-run/);
- GWTC-4.0 (https://www.ego-gw.it/blog/2025/08/26/gwtc-4-0-updated-gravitational-wave-catalog-released/).

## The reviewer's own checks, for reproduction

**Data and code**

- **Data.** The companion's file `data/raw/inspire_hep_records.csv.gz`, added in companion commit 0e239cd on `claude/happy-lovelace-wqek9b`. I read it with `git show`; no repository file was changed.
- **Dates.** The file contains 117,950 records dated 2017–2026. Seven carry a year-only date and drop out of every monthly series.

**Reproduction.** The companion's `inspire_classes()` (main rule) and `field_model()` from `stats_fields.py` reproduce `results.md` exactly:

- ND 1.18 (0.94–1.48) and NN 1.18 (0.96–1.44) in hep-ex + nucl-ex;
- by team size: at most 10 authors 1.55, 11–300 authors 0.64, more than 300 authors 1.42.

**Re-estimation**

- **Estimator.** The companion's `event_study()` from `stats_round1.py`: Poisson pseudo-maximum likelihood, month fixed effects, group-specific calendar-month effects, Driscoll–Kraay errors (`hac-groupsum`, 12 lags).
- **Bases:** {2022}, {2017, 2018, 2019}, {2017, 2018, 2019, 2022} and {2019, 2022}.

**Definitions**

- **Research article.** The document or publication type includes "article" and none of: conference paper, proceedings, review, thesis, lectures, book, book chapter, activity report, note. This is the companion's definition.
- **Planning papers.** The harvest's `snowmass` or `european_strategy` flag, which reads title and abstract.
- **Proceedings removed.** Records whose document type includes "conference paper" are dropped.
- **Missing author counts.** `author_count` "0" is treated as missing; the companion's rule treats it as at most 10.
- **Counts.** January–September of each year, by the harvest's `date` field (INSPIRE `preprint_date`).

**INSPIRE-HEP live queries** (17 October 2026)

- **Endpoint.** `https://inspirehep.net/api/literature?q=<query>&size=1`, reading `hits.total`, at most one request per second.
- **ATLAS and CMS by collision energy.**
  - Base query: `(collaboration:ATLAS or collaboration:CMS) and primarch hep-ex and ac > 300 and de YYYY-01-01->YYYY-09-30`.
  - Added to the base query: `and abstracts.value:"13.6 TeV"`; `and abstracts.value:"13 TeV" and not abstracts.value:"13.6 TeV"`; `and abstracts.value:"8 TeV" and not abstracts.value:"13 TeV"`.
  - The same base query with `collaboration:LHCb` for LHCb.
  - The query for papers on Run 2 data in 2015 failed and is not used.
- **STAR.** `collaboration:STAR and de YYYY-01-01->YYYY-09-30 and (primarch nucl-ex or primarch hep-ex)`, with and without `and ac > 300`.
- **Snowmass in INSPIRE.** `primarch hep-ex and de 2022-01-01->2022-09-30 and snowmass`, with `and tc c`, `and ac 11->300`, or both.
- **Caveats:**
  - `de` is INSPIRE's earliest date, close to the arXiv first version for these records;
  - energies are matched in abstracts only, and some papers name neither energy;
  - free-text "snowmass" matches anywhere in a record.

**Misclassification arithmetic**

- **The model.** Two classes. The observed ND count is Se·ND + (1 − Sp)·NN, and the observed NN count is (1 − Se)·ND + Sp·NN. Sensitivity and specificity may differ between the pre-period and the post-period. The observed ratio is (NN_post/NN_pre)/(ND_post/ND_pre).
- **κ** against the truth is computed from Se, Sp and prevalence.
- **Sample sizes** use the normal approximation for two proportions, at 80% power and α = 0.05.

**What these checks are for.** They show the direction and size of the problems and that the fixes are feasible. They are not substitutes for the companion's own analyses.
