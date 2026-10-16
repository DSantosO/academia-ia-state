# Reviewer 4: PLOS ONE Academic Editor assessment (round 1)

- **Manuscript:** `paper/plos_one/draft_v1.md` (v1, 16 Oct 2026), "Generative AI is eroding publication counts as a measure of scientific work: evidence from 1.9 million preprints".
- **Also read:**
  - `paper/brief.md` and `paper/plos_one/skeleton.md`;
  - the companion analysis's formal results, which arrived during this review: `paper/plos_one/stats/methods.md`, `results.md` and the two JSON files (companion commit 37b4b11);
  - the companion files in `paper/figures/`, and the scripts on branch `claude/happy-lovelace-wqek9b`;
  - the companion essay drafts `paper/draft_full.md` and `paper/draft_embo.md`, and `paper/correspondence_draft.md`, for overlap.
- **Reviewer:** an AI agent playing a PLOS ONE Academic Editor who also reviews. This is a simulated review before submission, not a PLOS review. PLOS forbids editors and reviewers to upload submissions to generative-AI tools, so this report must never be presented as, or used in place of, a PLOS review.
- **Date:** 16 October 2026. Line numbers refer to `draft_v1.md`.

**Policy pages consulted on 16 Oct 2026.** Short quotations below are as the pages returned them that day; re-check them in the week of submission.
- Criteria for publication: https://journals.plos.org/plosone/s/criteria-for-publication
- AI tools and technologies: https://journals.plos.org/plosone/s/ethical-publishing-practice#loc-artificial-intelligence-tools-and-technologies
- Data availability: https://journals.plos.org/plosone/s/data-availability
- Code sharing: https://journals.plos.org/plosone/s/materials-software-and-code-sharing
- Recommended repositories: https://journals.plos.org/plosone/s/recommended-repositories
- Competing interests: https://journals.plos.org/plosone/s/competing-interests
- Submission guidelines: https://journals.plos.org/plosone/s/submission-guidelines. Sections used: manuscript organization, references, figures and tables, supporting information, related manuscripts, personal data from third-party sources (`#loc-personal-data-from-third-party-sources`) and Registered Reports (`#loc-registered-reports`).
- Figures: https://journals.plos.org/plosone/s/figures
- Data-source terms:
  - arXiv API terms of use: https://info.arxiv.org/help/api/tou.html
  - bioRxiv and medRxiv API: https://api.biorxiv.org/
  - OSF terms of use: https://osf.io/terms-of-use/ (located but not read in full)
- To check the overlap claims: the arXiv abstract pages of Nee et al. (https://arxiv.org/abs/2609.04872) and Qi et al. (https://arxiv.org/abs/2510.17882).

---

## 1. Summary

The manuscript asks whether the growth in new preprints since generative AI became available is concentrated in non-experimental work within fields (H1), comes from many authors rather than a few (H2), and is unrelated to how much AI-assisted writing a field shows (H3). It draws on arXiv, bioRxiv, medRxiv and OSF counts to September 2026, with an author-name analysis of arXiv mathematics.

As written, the title, abstract and Discussion present an interpretive thesis that the observational design cannot test: AI "is eroding" publication counts, institutions are "rationing", and seven recommendations follow. Now that the formal results are in, the paper's own confirmatory tests do not support that thesis either:
- **Physics.** The theory–experiment contrast is not significant after correction, and it is smaller than the divergence between the two experimental archives.
- **Biology.** The computational–wet-lab contrast reverses with a 2019 base year or without bioinformatics.
- **Medicine.** The medRxiv contrast is null.

What survives is descriptive and exploratory:
- an acceleration across arXiv in 2026 that includes experimental high-energy physics;
- no departure from trend on bioRxiv or in PubMed;
- a sharp rise in the share of arXiv mathematics papers with a heavy producer.

That is a publishable PLOS ONE paper, but only if it is rebuilt around those results, with the essay's thesis, the rationing argument and the recommendations moved to the companion essay.

## 2. Editorial assessment and recommendation

**v1 as it stands: not reviewable.** It would be returned to the author without review. It still contains:
- [ANALYSIS PENDING] slots;
- an empty validation statement in the AI disclosure;
- data that have not been deposited;
- [RECHECK] and [AUTHOR] markers.

This is not a desk rejection on scope: the paper is original quantitative meta-research, which PLOS ONE publishes (criterion 1).

**v1 with the formal results inserted but the v1 framing kept: desk rejection under criterion 4.** That framing is the title, the abstract, H1, "Why experimental science is less affected", D2, D3 and the Conclusions. The criteria page says: "Submissions will be rejected if the interpretation of results is unjustified or inappropriate." The title and conclusions would contradict the paper's own confirmatory tests.

Discussion sections D2 and D3 would also count against the paper. Together they run to 1,096 words and carry 36 of the 79 references. They read as the companion essay rather than as a discussion of these data, and PLOS ONE does not consider "commentaries, essays, opinion pieces, policy papers" (criterion 1).

**Reframed as set out in section 3: I would send it out for review.** I would invite:
1. a scientometrician who knows arXiv and bioRxiv metadata;
2. a statistician or econometrician familiar with event studies with few units and with breaks at the end of a sample;
3. ideally, a meta-research or research-integrity reviewer for the heavy-producer measure and its ethics.

**Recommendation: major revision before submission.** The blocking items are marked ✗ in the checklist (section 6). With them fixed, I would expect a major-revision decision from reviewers and an eventual acceptance. The data work is careful, and the honest reporting of the medRxiv null is exactly what PLOS ONE values.

---

## 3. Given these results: how should the title, the abstract, H1 and the Discussion be reframed to satisfy criterion 4?

*(Added at the coordinator's request after the companion's formal results arrived. Estimates are from `stats/results.md` unless marked as the reviewer's own check.)*

### 3.1 What the formal results show, set against what v1 claims

| v1 claim (location) | Formal result | Verdict |
|---|---|---|
| Output accelerated "where the work beyond writing is also cheap", "much less" in experimental work (title; abstract; line 198 heading; line 246; Conclusions) | **C1 physics**, theory/experiment, 2026 relative to 2022: 1.14 [1.00, 1.30], p = 0.056, Holm p = 0.11. **C2 biology**, computational/wet lab: 1.08 [1.03, 1.14], Holm p = 0.0095. **C3 medicine**, public-dataset/other: 0.99 [0.88, 1.10], Holm p = 0.82 | Not supported |
| Experimental physics "within its historical range" (abstract; line 208) | Departure from the 2015–2022 trend in 2026: hep-ex 1.37 [1.12, 1.67], above hep-th 1.28 [1.18, 1.40] and hep-ph 1.29 [1.12, 1.47]. Of the six archives in C1, only nucl-ex is at trend (1.00 [0.82, 1.22]). C1 without nucl-ex: 1.03 [0.91, 1.18] | Contradicted. C1 rests on one small archive |
| Theory–experiment contrast reflects the cost of experiments (line 250) | Negative control hep-ex vs nucl-ex: 1.39 [1.19, 1.64], larger than C1. 61% of the 153 pairs of arXiv archives diverge at least as much as C1 | Fails the paper's own rule at line 161 ("A divergence as large as in the main contrast would point to heterogeneity…") |
| "Computational biology outgrew wet-lab biology … from 2025" (abstract; line 212) | C2 with 2019 as base: 0.87 [0.80, 0.95]. Without bioinformatics: 0.93 [0.89, 0.97]. Pre-period 2019: 1.24 [1.14, 1.36]. 19.7% of the 462 random splits of the wet-lab categories diverge as much | Fragile: depends on the 2022 reference year and on one category |
| Medicine as "the limiting case" (line 254) | C3 null with a precise interval (excludes more than about +10%) | Contradicted for medRxiv, as v1 already says honestly |
| bioRxiv shows "no break in 2026" (abstract; line 204) | bioRxiv 2026 relative to trend: 0.91 [0.71, 1.15]. The break tests cannot place a break in 2026 (Major issue 4c) | "No detectable departure from trend; the test cannot assess 2026" |
| Mathematics (abstract; Results) | 1.48 [1.26, 1.73] above trend in 2026. Synthetic-control gap 11.9%, replicating Nee et al. But maths ranks 5th of 18 arXiv archives (rank p = 0.28) | Real, but not exceptional within arXiv |
| (not in v1) | Physics was above trend from 2024: 1.05, 1.14 and 1.32 for 2024–2026. In 2026, 14 of 18 arXiv archives have intervals above 1. Computer science is not above its 21%-a-year trend (1.15 [0.97, 1.37]). PubMed: 0.93 [0.86, 1.01] | The main surviving finding, exploratory and between servers |

The result that survives, arXiv against bioRxiv, is a comparison between servers. It confounds field with platform: rules, moderation, endorsement and community norms. That is exactly the weakness the Introduction gives (line 99) for preferring within-field contrasts.

The paper therefore cannot attribute the arXiv acceleration to the cost of experiments. Experimental hep-ex accelerated like theory, which argues against that mechanism at the archive level. A caveat applies all the same: much of hep-ex consists of collaboration analyses of data already collected, with long internal review. hep-ex is therefore an imperfect proxy for work where "experiments bind", and that imperfection belongs in the Discussion.

### 3.2 Is a paper whose confirmatory tests are null or fragile acceptable to PLOS ONE?

**Yes.** The criteria page states: "In keeping with our mission to publish all valid research, we consider negative and null results" (criterion 1). Novelty and impact are not criteria. What the editor and reviewers will check is criterion 3 ("Sample sizes must be large enough to produce robust results, where applicable") and criterion 4 (conclusions match the data, implications "clearly identified as hypotheses instead of conclusions").

To be acceptable, the paper must be framed as follows.

1. **Lead with the question and the answer, not the thesis.** The question: "Is the post-2022 growth in preprints concentrated in non-experimental work within fields?" The answer: "Not robustly. The 2026 acceleration is broad across arXiv, experimental archives included, and absent on bioRxiv and in PubMed."
2. **Report all three pre-specified contrasts everywhere they are summarised:** abstract, Results, Discussion and Conclusions. Give the estimates, 95% CIs and adjusted p-values, so that no supportive subset is selected.
3. **Say "inconclusive" or "no robust evidence", not "no effect", where power is limited.** Report the minimum detectable effects: 1.21 (C1), 1.08 (C2) and 1.17 (C3). C1 is inconclusive; its interval runs to 1.30. C3 is the informative null. C2 is nominally significant but not robust.
4. **Do not promote exploratory results into confirmatory ones.** The field-level departures, the arXiv–bioRxiv difference and the trend-adjusted C2 (1.48 [1.06, 2.07]) are exploratory. The companion dropped the trend-adjusted C2 as a headline estimate, and the author must not revive it because it favours H1. List every analysis tried, including those dropped, in S4 Table with the reason.
5. **Report deviations from the plan** (Major issue 4) and the estimate under the specification planned in v1.
6. **Keep the essay's thesis out of the conclusions.** It may motivate the Introduction in one or two sentences and be cited once, to the companion essay, in the Discussion.

A paper framed this way is arguably more useful than v1. It is a pre-specified test of a plausible mechanism, an "experimental bottleneck" that Blekhman asserts and v1 adopts. It fails in a way that tells readers something: the 2026 surge is a property of arXiv, not of theory or computation as such.

### 3.3 Title

The v1 title fails on four counts. "Is eroding" is causal. "As a measure of scientific work" names a construct that is not measured. "Publication counts" describes preprints, which v1 itself says are not publications. And the main finding is now null. Options with no question, as the author prefers:

1. **Preprint growth in the generative-AI era: an arXiv-wide acceleration and no robust difference between experimental and non-experimental work within fields** (recommended; 154 characters, within the 250-character limit)
2. No robust difference between experimental and non-experimental preprint growth within fields after generative AI, 2015–2026
3. Preprint output after generative AI: acceleration across arXiv in 2026, not concentrated in theoretical or computational work

**Short title** (required, at most 100 characters): "Preprint growth after generative AI".

**Drop "evidence from 1.9 million preprints".** The number:
- is not the analytic sample of any test;
- changes with every redefinition of the sample (the formal analyses use arXiv from 2010 or 2015);
- sits close to Qi et al.'s title.

### 3.4 Abstract: a model within the 300-word limit (289 words)

> Research evaluation relies on counts of outputs. If generative artificial intelligence (AI) lowered the cost of producing papers mainly where research needs no new experiments, output should have grown faster in theoretical, computational and secondary-data work than in experimental work within the same field. I tested this prediction in monthly counts of new preprints on arXiv (2015–2026), bioRxiv and medRxiv (2019–2026), using three contrasts fixed before any model was estimated, but after descriptive counts had been seen: theoretical against experimental physics, computational against wet-lab biology, and medRxiv preprints naming widely reused public datasets against other medRxiv preprints. Relative to 2022, the January–September 2026 rate ratios were 1.14 (95% CI 1.00–1.30; Holm-adjusted p = 0.11), 1.08 (1.03–1.14; p = 0.01) and 0.99 (0.88–1.10; p = 0.82). The biology contrast reversed with 2019 as the base year (0.87) or without bioinformatics (0.93), and one in five random splits of wet-lab categories diverged as much; the two experimental physics archives diverged more from each other (1.39) than theory did from experiment. At field level, arXiv physics and mathematics were 32% and 48% above their 2015–2022 trends in January–September 2026, and 14 of 18 arXiv archives were above trend, among them experimental high-energy physics (1.37; 1.12–1.67); bioRxiv (0.91; 0.71–1.15) and PubMed (0.93; 0.86–1.01) were not. In arXiv mathematics, the share of papers with an author name on five or more papers in a quarter rose from 5.3% in Q3 2025 to 18.1% in Q3 2026 (1.8% to 5.9% under a namesake-robust definition). The 2026 acceleration is thus concentrated on arXiv rather than in non-experimental work within fields. The design is observational: it cannot attribute the growth to AI, separate legitimate from problematic use, or show whether the work behind each paper has changed.

When the formal H2 results arrive, replace the mathematics sentence with the fractional-output decomposition (Major issue 5). Keep the abstract below 300 words.

### 3.5 H1

**Do not rewrite H1 to fit the results.** Replacing it with "arXiv accelerates more than bioRxiv" would be HARKing. State it as it was tested, and note in S2 Appendix that the v1 wording also included the clause on writing. The tested statement:

> **H1 (pre-specified).** Within a field, the 2026 rate of new preprints relative to 2022 is higher in groups whose research needs no new experiments (theoretical physics; computational biology; medRxiv analyses of widely reused public datasets) than in experimental groups (experimental physics; wet-lab biology; other medRxiv preprints).

Remove two clauses from the hypothesis:
- "AI is visible in the writing but much less, or not yet, in the volume of output". The first half belongs to H3; the second makes H1 unfalsifiable in time.

Move "later onset in experimental work" to the Discussion as a separate hypothesis, to be tested on 2027 data (section 3.9). Results: "H1 was not robustly supported (Table 4)."

### 3.6 Results

- **Headings.** Replace "Output grew fastest where experiments do not bind (H1)" (line 198) with "Within-field contrasts (H1)". Add "Departures from trend by field and archive (exploratory)".
- **Table 4 is now the central display.** For each contrast it should give:
  - the 2023–2026 event-study coefficients;
  - the pre-period coefficients, which show the parallel-trend problem: C1 1.25 (2020) and 1.19 (2021); C2 1.24 (2019);
  - base 2019;
  - the specification planned in v1 (2017–2022 period baseline);
  - the trend-adjusted estimate;
  - the minimum detectable effect;
  - the negative-control percentile (C1: 61% of archive pairs; C2: 19.7% of wet-lab splits);
  - the leave-one-out range.
- **Plot the coefficients.** Plot the event-study coefficients for C1–C3 with their CIs, as a new Fig 2 or a panel. Replace the "range of the same statistic" comparisons, which are asymmetric (Major issue 3).
- **Report the arXiv-wide finding as exploratory, with its confound** (between-server comparison) stated in the same paragraph.

### 3.7 Discussion

**Proposed structure, about 1,100 words in total:**

| Subsection | Words |
|---|---|
| Principal findings | ≈150 |
| Why the within-field contrasts are inconclusive or fragile | ≈300 |
| An arXiv-wide acceleration: candidate explanations | ≈250 |
| What this means for output counts (hypothesis, labelled) | ≈120 |
| Limitations | ≈300 |

Notes on the subsections:
- **Why the contrasts are inconclusive or fragile.** Cover power; heterogeneity among archives and categories; the 2022 reference year; group definitions (hep-ph is phenomenology tied to experiment; gr-qc includes analysis of gravitational-wave data; genomics); and AI as topic versus tool in bioinformatics.
- **Candidate explanations for the arXiv-wide acceleration.** These include AI use across arXiv communities, experimental collaborations among them; arXiv's 2025–2026 rule changes and possible displacement between archives; changes in primary-category choice; and changes in funding or the job market. Note that computer science is not above its own steep trend.
- **Delete:**
  - "Why experimental science is less affected so far" (lines 248–256);
  - "AI is in the writing but not yet in the volume" (line 252);
  - the medicine "limiting case" paragraph (line 254), whose support now comes only from literature on formulaic, often problematic NHANES papers. That evidence also sits awkwardly with the "needs no misuse" framing;
  - D2 and D3 in their current form (Major issue 7).

**Model opening paragraph:**

> None of the three pre-specified within-field contrasts supports H1 robustly. The theory–experiment contrast in physics (2026 rate ratio relative to 2022, 1.14; 95% CI 1.00–1.30) is not significant after correction for three tests, is smaller than the divergence between the two experimental archives (1.39), and is matched or exceeded by 61% of pairs of arXiv archives. The computational–wet-lab contrast in biology (1.08; 1.03–1.14) is nominally significant but reverses when 2019 is the base year (0.87) or bioinformatics is removed (0.93), and one in five random splits of wet-lab categories diverges as much. The medRxiv contrast is null (0.99; 0.88–1.10). Growth in 2026 was instead broad across arXiv: 14 of 18 archives were above their 2015–2022 trends, experimental high-energy physics among them (1.37; 1.12–1.67), whereas bioRxiv and PubMed were not. Because this difference lies between servers, it confounds field with platform, the limitation that motivated the within-field design.

**Model interpretation paragraph, which replaces D2:**

> These results do not show that generative AI changed what publication counts measure. They show that counts on arXiv rose 32–48% above their pre-2023 trends in physics and mathematics within about two years, unevenly across servers but not, at the precision available, between experimental and non-experimental work within fields. If such growth reflects a falling cost of producing papers rather than more research, counts would correspond to different amounts of work across servers and years. This is a hypothesis: testing it requires measures of research inputs, or of the work behind each paper, which this study does not have. A broader argument, that evaluation built on costly outputs is unprepared for widespread and legitimate AI use, is developed in a companion essay [47].

**Model implications paragraph, which replaces D3 (about 80 words, plus the pre-registration sentence in section 3.9):**

> For users of output counts, the implication is practical: counts from 2023 onwards should not be compared across servers, or with earlier years, without adjustment, and per-author distributions such as those in Table 5 can show whether growth is broad or concentrated. Whether evaluators should cap the outputs they assess, rather than the items authors may submit, is an open question that could be tested experimentally [55].

### 3.8 Conclusions: a model

> Between 2023 and September 2026, new preprints grew faster than their pre-2023 trends across arXiv, in experimental as well as theoretical archives, but not on bioRxiv or in PubMed. Within fields, growth in 2026 was not robustly faster in non-experimental than in experimental work. In arXiv mathematics, the share of papers with an author name on five or more papers in a quarter more than tripled within a year. The design cannot attribute these changes to generative AI.

Adjust the mathematics sentence to the formal H2 results.

### 3.9 Is it appropriate to mention pre-registering the within-field contrasts on 2027 data?

**Yes, as one or two sentences of future work, under five conditions.**

1. **Register it before citing it.** Register before any 2027 data are retrieved, in a public registry that issues a DOI (OSF Registries, for example), and cite the DOI. A git commit is a useful timestamp but not a registry. Do not describe a registration that does not yet exist. If it is not done before submission, write "I plan to…" or leave it out.
2. **Do not use it to rescue H1.** No promissory language such as "the effect is expected to appear in experimental work later". Present it as a new, independent test.
3. **Handle arXiv's cap of 1 October 2026 explicitly.** The manuscript itself says the cap "will break any extension of these series" (line 292), and the cap may bear differently on individual theorists and on collaboration submitters. The cleanest 2027 contrasts are on bioRxiv and medRxiv. For arXiv, the registration must model the cap or restrict the test.
4. **Improve the design rather than repeat it.**
   - Use more units: classify individual papers as experimental or non-experimental within archives and categories, with a classifier validated before 2027, instead of two small archives.
   - Use a multi-year pre-2020 baseline instead of 2022.
   - Pre-specify the negative-control criterion, for example that the contrast must exceed the 95th percentile of random splits within a group.
   - Base the power analysis on the 2026 minimum detectable effects.
5. **A PLOS ONE Registered Report Protocol is possible,** since the journal "consider[s] preregistered research including both" protocols and the articles reporting outcomes. The submission guidelines then require that data "collected, modified or processed" for the study be handled "only after your Registered Report Protocol is accepted for publication". The author must therefore not harvest 2027 data until acceptance. An OSF registration is faster.

**Suggested sentence:**

> The same contrasts will be re-tested on 2027 data under an analysis plan registered before those data were retrieved (OSF Registries, doi:[ID]); because arXiv capped submissions at two per submitter per month from 1 October 2026, the arXiv contrasts in that test are not directly comparable with those reported here.

---

## 4. Major issues

### Major issue 1. The title claims causation, an unmeasured construct and a finding the data do not show

- **Location:** line 53.
- **Problem:**
  - "Is eroding" is causal. The abstract's own last sentence says the data "do not establish that AI caused the growth", and the Introduction (line 107) says the design is observational.
  - "Publication counts as a measure of scientific work" is a statement about validity. The study measures no work, inputs or quality per paper.
  - The data are preprints.
  - With C1–C3 null or fragile, the central finding the title implies has not been shown.
- **Criterion:** 4 ("authors should avoid overstating their conclusions").
- **Fix:** one of the titles in section 3.3, and a short title.

### Major issue 2. The abstract reports selectively and states interpretations as findings

- **Location:** line 83.
- **Problems:**
  1. **The premise is stated as fact.** "Counts … carried information partly because outputs were costly to produce, and generative AI lowers that cost even under legitimate use." The study does not test this.
  2. **"Output has grown fastest where the work beyond writing is also cheap, and much less, so far, in experimental work."** The study does not measure the cost of work, and the claim is now contradicted (section 3.1).
  3. **"Experimental archives grew by 11%, within theirs [their range]."** The range comparison is asymmetric (Major issue 3).
  4. **Inconvenient results are left out.**
     - The medRxiv contrast does not support H1. The Discussion admits this (line 246); the abstract does not.
     - Medicine grew 29% year on year in Q3 2026, faster than physics.
  5. **"Published estimates put AI-assisted writing in biology on a par with physics."** This rests on one preprint (Lin and Zhu [34]) about arXiv quantitative biology, not bioRxiv, and on the change between the end of 2022 and the end of 2023, not on prevalence.
  6. **Monthly end points.** The heavy-producer comparison runs from January 2025 to September 2026, the series' peak month. The quarterly comparison (Q3 2025 to Q3 2026: 5.3% to 18.1%; 1.8% to 5.9% under the strictest variant) is cleaner. For the grey series, January 2025 "was a high month" (line 226).
  7. **"Consistent with AI lowering the cost of counted outputs without any misuse."** The data cannot speak to misuse, as line 260 admits.
  8. **Word limit.** The pending sentence with three ratios would take the abstract over 300 words.
- **Criterion:** 4; submission guidelines (abstract of at most 300 words, "summarize results and their significance").
- **Fix:** the model abstract in section 3.4.

### Major issue 3. How the H1 results are reported in Results and Discussion

- **Locations:** line 198 (heading), 208, 212, 246, 250–256 and 298.
- **The "range" criterion is asymmetric.** Theory's 2017–2025 range is narrow (−6% to +6%) because the series is large. Experiment's range is wide (−13% to +22%) because the series is small (about 430 papers a quarter), so almost any value falls "within" it.

  The reviewer's check from `within_field_quarterly.csv`:
  - experimental growth in January–September 2026 (+10.5%) is the second-highest of 2017–2026;
  - in Q3 2026 alone, hep-ex grew 25.1% year on year (324 against 259 papers), against 26.0% for the theory group.

  The formal in-space analysis confirms this: hep-ex is 1.37 [1.12, 1.67] above trend.
- **The paper's own falsification rule is not applied.** Line 161 says a negative-control divergence "as large as in the main contrast would point to heterogeneity among archives or categories rather than to the cost of experiments".
  - C1: hep-ex against nucl-ex gives 1.39, which is larger than C1 (1.14), and 61% of arXiv archive pairs diverge as much.
  - C2: 19.7% of random splits of the wet-lab categories diverge as much.

  By the paper's own rule, neither contrast supports H1.
- **Headings and conclusions assert the hypothesis.** Examples: "Output grew fastest where experiments do not bind"; "Why experimental science is less affected so far"; "Descriptively, these results support H1 and H2" (line 246).
- **Criterion:** 4; 3.
- **Fix:**
  - Retitle as in section 3.6.
  - Report C1–C3 with the negative-control percentiles.
  - Replace the range comparisons with model-based departures.
  - Delete line 246's "support H1 and H2 and are consistent with H3".
  - Suggested Results sentence for physics:

    > In January–September 2026, theory archives grew by 20% and experimental archives by 11% against the same months of 2025. Relative to 2022, the theory/experiment rate ratio was 1.14 (95% CI 1.00–1.30; Holm-adjusted p = 0.11); the two experimental archives diverged more from each other (hep-ex/nucl-ex 1.39; 1.19–1.64) than theory from experiment, and the contrast fell to 1.03 (0.91–1.18) without nucl-ex.

### Major issue 4. The statistical plan: deviations, the meaning of "confirmatory", and two tools that cannot answer the question

- **Location:** Methods, "Statistical analysis" (lines 151–171), against `stats/methods.md`.
- **Criteria:** 3 ("described in sufficient detail") and 4.

**(a) Undeclared deviations from the plan in v1.**

| | v1 plan (lines 153–159) | Analysis actually run |
|---|---|---|
| Reference | Periods 2023–2024, 2025 and 2026 against a 2017–2022 baseline (arXiv) | Year-by-group event study with 2022 as reference |
| Multiplicity | Bonferroni-adjusted 98.3% CIs | Holm-adjusted p-values |
| Model | Poisson, switching to negative binomial if overdispersed | Poisson pseudo-maximum likelihood (PPML) with month fixed effects |
| Standard errors | Newey–West | Driscoll–Kraay |
| Breaks | Bai–Perron | Single-break sup-Wald with parametric bootstrap |
| Negative controls | Benjamini–Hochberg | Share of placebo pairs at least as extreme |

Several changes are improvements: month fixed effects, Driscoll–Kraay standard errors, and the share of placebo pairs. The change of reference year matters, though.
- The pre-period coefficients show that 2022 is not a neutral reference: C1 1.25 (2020) and 1.19 (2021); C2 1.24 (2019).
- With 2019 as base, C1 is 1.05 [0.90, 1.23] and C2 is 0.87 [0.80, 0.95].
- The reviewer's crude check against the baseline planned in v1 (January–September totals, 2026 against the 2017–2022 mean) gives about 1.05 for C1. For C2 it gives about 1.03 against 2019–2022. These are not model estimates.

Fix: describe the model actually used, and add a paragraph on deviations.

> *Deviations from the analysis plan.* The plan (commit [hash], [date, time]) specified period effects against a 2017–2022 baseline, Bonferroni-adjusted intervals and Bai–Perron break tests. The analysis (commit 37b4b11) used year-by-group effects with 2022 as reference, month fixed effects, Driscoll–Kraay standard errors, Holm-adjusted p-values and single-break sup-Wald tests, because [reasons]. Estimates under the planned specification are reported in S4 Table; they do not change the conclusions.

Then report the planned estimate. If it changes a conclusion, say so.

**(b) "Confirmatory."** The plan was written after the descriptive counts had been seen (line 113), and the descriptive growth rates are in effect the effect sizes. In common usage, "confirmatory" implies specification before seeing the data. Either use "pre-specified primary contrasts", or keep "confirmatory" and define it in place:

> confirmatory here means fixed before any model was estimated, not before the data were seen; the tests therefore protect against choosing models after seeing results, not against choosing contrasts.

Line 292 already says the second half; it belongs in the Methods.

**(c) The break tests cannot detect a break in 2025–2026.** The sup-Wald statistic is computed over "the central 70% of the sample". For the arXiv series (January 2015 to September 2026; 141 months), the last admissible break date is therefore about December 2024. For bioRxiv and medRxiv it is about August 2025.

The physics "slope break at 2024-11 (p = 0.001)" lies one month before the boundary. It marks the latest date the test can return, not an estimated onset. The mathematics break at 2024-11 (p = 0.095) is at the same place. The coordinator's summary, "accelerate from late 2024", partly inherits this artefact. The yearly departures are better evidence: physics 1.05 (2024), 1.14 (2025), 1.32 (2026); mathematics 1.04 (not significant), 1.08, 1.48. On this evidence, mathematics accelerated mainly in 2026.

Fix:
- report the admissible window;
- use an end-of-sample instability test (Andrews 2003, Econometrica 71(6):1661–94) or a predictive (Chow-type) test for 2026;
- delete "no break in 2026" (line 204);
- cite the method actually used. The sup-Wald test is Andrews (1993, Econometrica 61(4):821–56), not Bai and Perron [43,44]. Check the metadata in Crossref before use.

**(d) The placebo dates are descriptive.** With two or three placebo years, no informative p-value is possible. In the pre-period, placebo level shifts are as large as the 2026 estimate (C1: 1.19 in 2019, 1.16 in 2020). Say so.

**(e) Negative controls (line 153).** v1 adjusts their p-values with Benjamini–Hochberg. For a falsification test this points the wrong way: adjustment makes "passing" easier. The companion's metric, the share of placebo pairs at least as extreme, is right. Update the Methods, and pre-specify the decision rule.

**(f) Few units.** Each contrast has two series. Driscoll–Kraay standard errors handle dependence over time but not shocks specific to one group. The in-space placebos are the more honest inference. Present them as the main check, not as an afterthought.

### Major issue 5. H2: the heavy-producer measure supports less than the text claims

- **Locations:** H2 (line 104); Methods (line 143); Results (lines 224–232); Discussion (lines 246, 260); Conclusions (line 298); Table 5; Fig 3.
- **Criteria:** 3 and 4.

**Problems.**
1. **H2 is not defined operationally.** "Broad" and "many established researchers … not … a few outliers" have no stated measure.
2. **"Established" is unsupported.** "611 of 693 prolific names had posted mathematics papers since January 2025" means at least one paper in the 18 months before Q3 2026 (January 2025 to June 2026), with censoring on the left.
3. **The per-paper share rises mechanically with volume.** Once production per author rises, more authors cross a fixed threshold of five.
   - The direct test of "broad" is a decomposition of the increase.
   - From Table 5's own counts, papers with a prolific name account for 2,974 of the 8,716 additional papers from Q3 2025 to Q3 2026 (34%). About two-thirds of the growth came from papers with no prolific name, which is actual evidence of breadth and is not reported.
   - The companion's decomposition of fractional output (`methods.md`, H2: "share of the change in fractional output … contributed by authors with five or more papers"; top 1%) is the right test. Report it as the H2 result.
4. **Wilson intervals and z-tests treat papers as independent.** The companion itself calls them "a guide only". Do not report p-values from them; present H2 descriptively.
5. **The stricter namesake variants exclude 36–41% of author slots**, the most frequent surnames. That exclusion is unlikely to be neutral by world region. Report what is excluded, in aggregate, and say that the levels describe a different population.
6. **The AI-mention regular expression counts topics as well as tools.** It matches "large language models", "LLMs" and "AI systems/models", and it is case-insensitive (`re.I` in `analyze_math.py`). The counts are therefore not "lower bounds" (lines 143, 230, Table 5): they mix false positives (topic mentions) with false negatives (undisclosed use). The Lean pattern, also case-insensitive, matches "lean proof" and "in lean". Relabel the measure "papers using AI-related terms" and drop "lower bound".
7. **Fig 3D (Erdős) is unexplained.** The legend note says so. The Discussion still uses Erdős mentions as support (line 250). Either explain and cite why Erdős mentions index AI-assisted work, or remove the panel and the claim.
8. **Line 260 uses mention rates to argue against misuse.** "Their papers mentioned AI tools barely more often than other papers". Metadata mentions cannot speak to misuse, because undisclosed use is invisible. Delete.
9. **Two pipelines give 19.3% and 19.2%** for September 2026 (line 224; S2 Appendix). Use one.
10. **The comparison with Nee et al. needs aligned windows.** The comparison is flagged [RECHECK] (line 232). The companion computes January–August windows for comparability; use them.

**Fix: operational H2.**

> H2. Where output accelerates, most of the increase comes from authors below the heavy-producer threshold: authors with five or more papers in a quarter account for less than half of the change in fractional output.

Then report that share under each namesake variant, with no p-values. Remove "established" throughout, or define it, for example as at least one paper in each of three earlier quarters.

### Major issue 6. H3 is not tested by this study, and the comparison crosses populations

- **Locations:** line 105; Methods (lines 145–147); Results (lines 234–238); Table 6; line 252.
- **Criterion:** 4.

**Problems.**
1. **H3 rests on a table of published estimates in the Results section (Table 6).** It is not a result of this study.
2. **The key comparison mixes populations and years.** It sets AI-writing in arXiv q-bio at the end of 2023 (a preprint) against output on bioRxiv in 2026. q-bio is not bioRxiv. q-bio's own output fell 7% in January–September 2026 year on year, yet it is 1.26 [1.13, 1.40] above its trend. Neither fact is discussed.
3. **Table 6 omits Liang et al.'s bioRxiv estimates,** although it says their corpus includes bioRxiv. These are the most direct published comparison for H3.
4. **Lin and Zhu's figures (22%, 11%, 10%, 3.5%)** do not say whether they are percentage-point or relative changes.
5. **Mathematics cuts against the writing measure.** Mathematics has the lowest AI-writing estimates and the highest growth (line 238). Writing markers therefore do not index AI use where it drives output. That undercuts the "AI is in the writing but not in the volume" logic (line 252).

**Fix.**
- **If the companion's marker analysis is completed** (`methods.md`, H3), report it as the H3 result, with its own limits.
- **If not,** demote H3 from the hypotheses to background, under "Prevalence of AI-assisted writing (context)". Move Table 6 to the Introduction or the Supporting Information, and remove the abstract sentence.

### Major issue 7. D2 and D3: what an editor would cut or soften

- **Locations:**
  - "Counting outputs when AI is used legitimately", lines 258–266 (583 words);
  - "Implications for research evaluation", lines 268–282 (513 words).
- **Weight.** Together these are 1,096 words, against 657 for the H1 Results.
  - 13 references are first cited in D2, 23 (refs 55–77) in D3, and 10 more only in the tables.
  - So 46 of 79 references support Table 1 or the interpretive sections.
- **Criteria:**
  - 4: implications must be "clearly identified as hypotheses instead of conclusions", and "authors should avoid overstating their conclusions";
  - 1: no "commentaries, essays, opinion pieces, policy papers";
  - the PLOS AI policy: "statements in the article reporting hypotheses, interpretations, results, conclusions" must "represent the authors' own ideas". D3 is derived from an AI-written research note (`[AUTHOR: own recommendations to merge]`; comment at line 280).

**Sentence by sentence.**

| Location | Text | Problem | Action |
|---|---|---|---|
| line 260 | "The acceleration documented here needs no misuse." | The data cannot show this, and the next sentence concedes it | Replace: "These data cannot distinguish legitimate from problematic use." |
| line 260 | "a count of papers in 2026 measures something different from a count in 2022, because the cost of producing a paper has fallen unevenly across kinds of work" | Cost is not measured. The within-field results do not show unevenness across kinds of work | Cut, or recast as the hypothesis in the model paragraph of section 3.7 |
| line 262 | Effort becomes invisible; the AI-written experimental paper | An essay argument about papers whose counts these data show did not change | Cut; cite the companion essay once |
| line 264 | Rationing paragraph; "a Matthew effect written into the rules" | Argument and rhetoric. Comparing "2.5% of author names" against arXiv's per-submitter cap mixes authorship with submission | Keep at most two descriptive sentences (below) |
| line 266 | DORA and CoARA "largely unimplemented where measured, and mostly unmeasured" | Overreach. McKiernan et al. (2016–2017 documents, US and Canada; 40% mention the JIF) and Rice et al. (2017–2018) predate CoARA. The paragraph's own EC source says engagement is "broad and growing". "The searches for this article found no study…" refers to a non-systematic search. "Consumes the first of these resources" is not measured | Cut. If one sentence is kept: "Reforms such as DORA and CoARA assume that evaluators can read what they assess; whether the volume growth documented here affects that assumption was not examined." |
| lines 270–278 | Seven recommendations | Items 4–6 (exploration grants; open models and contracts on chat data; monitoring model families) have no link to these data. Items 1–3 and 7 are policy proposals from the literature | Cut to the two-sentence implications paragraph in section 3.7. Move the list to the essay |
| line 282 | "as speculation, AI could also lower the cost of… reading and checking" | Speculation | Cut |

**Acceptable two-sentence version of the rationing point**, with Table 1 moved to S1 Table:

> Several funders, preprint servers and conferences introduced per-person limits on submissions in 2025–2026 (S1 Table). Such caps limit volume; whether they preserve information about the work behind each item has not been evaluated.

This also removes the overlap with the planned Nature Correspondence (Major issue 9).

### Major issue 8. How "consistent with" is used

- **Locations:**
  - abstract, last sentence;
  - line 107 ("consistent with these hypotheses");
  - line 232 (Nee et al.);
  - line 246 ("consistent with H3");
  - line 250 ("consistent with a simple mechanism").
- **Problem.** The phrase hedges the abstract's main interpretive claim, while the headings and Conclusions assert the same claims outright. Examples: "Output grew fastest where…"; "Why experimental science is less affected"; "In mathematics, the acceleration came from many established authors" (line 298). "Consistent with" is informative only if the alternatives are named and shown to be less consistent. Here they are not. At line 246, "consistent with H3" is used for a hypothesis the study did not test.
- **Criterion:** 4.
- **Fix:** a rule. Use "consistent with X" only with "and with Y and Z", and only with the analysis that separates them; otherwise write "does not distinguish between". Make the hedging uniform across headings, abstract, Discussion and Conclusions. A rewrite for the abstract:

> These patterns are consistent with generative AI having lowered the cost of some kinds of research output, but also with arXiv-specific changes in rules, moderation and category choice in 2025–2026, and with field-specific shifts in funding and hiring; the design does not distinguish between them.

### Major issue 9. Overlap with the companion essays: figures and data already used elsewhere

- **Location:** whole manuscript; reference [47]; Table 1; Figs 1–3, S1 Fig.
- **Problem.**
  - The Zenodo essay (`draft_full.md`) contains the same field-index, mathematics-profile and within-field figures, with the same numbers (its Figs 3, 4, 5 and S1), and the same Table 1.
  - The EMBO Reports essay (`draft_embo.md`) contains the field-index and mathematics figures, with the same numbers.
  - The README still lists the EMBO submission.
  - PLOS ONE: "All figures included in manuscripts should be original, and should not have been published in any previous publications"; "currently under consideration for publication elsewhere" is not considered. Authors must confirm that the manuscript "or any related manuscript, is not currently under consideration" elsewhere, and include a copy of related work. Preprints are allowed.
  - Verbatim text overlap is low. In the abstract and the main sections, the reviewer measured at most 5% of 10-word sequences shared with the Zenodo essay, and at most 4% with the EMBO draft. Overlap is higher only in the short boilerplate statements (competing interests; CRediT). So the problem is figures and results, not recycled text.
- **Criterion:** 2; submission guidelines (related manuscripts).
- **Fix.**
  1. Decide before submission. Do not submit the EMBO essay with these figures while the PLOS article is under consideration. Replace its data figures with a schematic and cite the article or its preprint.
  2. Post this article as a preprint before or with the Zenodo essay, so that the essay cites the article for the results rather than presenting them as its own.
  3. Disclose the Zenodo essay, and any EMBO submission, in the cover letter and the submission form, with copies.
  4. Ref [47] must exist, with a DOI, before submission. "Unpublished or unaccepted work should not appear in the reference list."
  5. Align the competing-interest declarations across venues. The Correspondence draft says "no competing interests"; this article declares a non-financial interest.

### Major issue 10. Ethics: processing author names from third-party metadata

- **Locations:** Ethics (line 190); Methods (line 143); Data availability (line 306); Table 5.
- **Problem.** The ethics statement says "no human participants were involved". PLOS's guidance on personal data from third-party sources applies instead (submission guidelines, `#loc-personal-data-from-third-party-sources`):
  - for observational studies, consulting an ethics or data-protection committee is recommended;
  - where personal identifying information was accessed, "an Ethics or Data Protection Committee should oversee data anonymization";
  - the ethics statement must "declare any potential risks to individuals or individual privacy";
  - data must be handled "according to company/website Terms and Conditions";
  - "Terms of Use contracts do not qualify as informed consent".

  The risks here are concrete:
  - **Re-identification.** Small cells (four names with 20–49 papers in Q3 2026) can be identified trivially by anyone re-running the released code on public metadata.
  - **Reputational harm.** The article links heavy production with AI, despite its disclaimers.
  - **Legal framework.** UPF, a Spanish public university, is subject to the GDPR. EMBL is an intergovernmental organisation with its own data-protection rules. The author should ask both data-protection officers which framework applies, and record a lawful basis and safeguards for research. Questions to raise include the Article 89 safeguards and the Article 14(5)(b) exemption from informing data subjects. These are questions for the officers, not conclusions of this review.
- **Terms of use.**
  - arXiv: metadata are CC0, but the terms limit legacy APIs (including OAI-PMH) to "no more than one request every three seconds" over a single connection, and forbid presenting a project as endorsed by arXiv.
  - bioRxiv and medRxiv: the API page states no terms, but each record carries its own licence field. Abstracts must not be redistributed unless their licence allows it; counts and DOIs are fine.
  - OSF and PubMed (NCBI): check their terms. The reviewer did not read them in full.
- **Criterion:** 6.
- **Fix.**
  - Pseudonymise names at ingestion with a salted hash. Keep only the variables the namesake variants need: whether the first name is an initial, and the frequency rank of the surname.
  - Delete or restrict the raw strings.
  - Merge cells describing fewer than ten names.
  - Obtain a statement from the data-protection officers or ethics committee.
  - Model ethics statement:

> *Ethics statement.* This study analysed publicly available bibliographic metadata and aggregate counts. For the analysis of arXiv mathematics [and physics], author name strings from arXiv metadata (released under CC0) were processed only to count papers per name within calendar quarters. Names were pseudonymised at ingestion and the raw strings [deleted after processing / held on access-controlled storage until (date)]; no name is reported, released data contain no names, and table cells describing fewer than ten names are merged. [EMBL's / UPF's Data Protection Officer] reviewed the processing on [date] and [determined that no further approval was required / approved it under (reference)]. The main risk to individuals, re-identification of heavy producers from public metadata, is mitigated by reporting aggregates only. Data were retrieved in accordance with the terms of use of each source (arXiv API terms; bioRxiv/medRxiv API; OSF; NCBI).

### Major issue 11. Data availability: the plan does not yet cover PLOS's minimal data set

- **Locations:** Data availability (line 306); Software (line 186); S1 Data (line 525).
- **Problem.** PLOS requires "the data required to replicate all study findings reported in the article", including "the values used to build graphs", and code that "underpins the findings" made "available without restrictions upon publication". The current plan, "aggregated counts" plus scripts that "re-harvest" the sources, falls short in five ways:
  1. **Aggregates suffice only for the H1 models**, whose inputs are monthly counts by archive and category.
  2. **They do not suffice for the rest:**
     - the medRxiv keyword flags (needs, per preprint: DOI, date, category, COVID-19 flag, public-dataset flag);
     - the bioRxiv COVID-19 sample for May–June 2022 (classification per preprint);
     - H2 (needs paper-level data with author keys);
     - H3 (marker counts per abstract or per group-month, and the word list);
     - the PubMed counts, a source the formal analyses add but the Methods do not describe.
  3. **Re-harvesting is not replication.** Records change: withdrawals, recategorisation, edits to author lists. Deposit a frozen snapshot of identifiers and derived variables.
  4. **The OAI-PMH harvests are not in the companion repository.** It has no harvest files, and its `.gitignore` excludes only caches.
  5. **The repository snapshot needs a check before archiving.** If the repository history is archived "with the data" (S1 Appendix), check it for personal data, for copyrighted full texts or long quotations in the research notes, and for strategy files the author may not want public.
- **Third-party restrictions.** None prevents depositing counts and identifiers: arXiv metadata are CC0, and facts and identifiers from bioRxiv and medRxiv are fine. The only restriction is the author's own, for privacy, on author-level data. If that table is withheld, the Data Availability Statement must explain why and name a contact who is not an author. PLOS: "it is not acceptable for an author to be the sole named individual responsible for ensuring data access".
- **Licences.** PLOS requires repository licences "not … more restrictive than the Creative Commons Attribution (CC BY) license" and encourages an open-source licence for code. Zenodo is on PLOS's list of recommended repositories.
- **Criterion:** 7; data-availability and code-sharing policies.
- **Fix.** Deposit before submission, with a private link for reviewers if needed. Model statement:

> The data underlying the findings are available from Zenodo (https://doi.org/10.5281/zenodo.[ID]; CC BY 4.0), with the code (MIT licence) that harvested, processed and analysed them: monthly counts of new preprints by arXiv archive (2010–2026), bioRxiv subject category (2019–2026) and medRxiv (2019–2026); for medRxiv, the DOI, posting date, subject category and COVID-19 and public-dataset flags of each preprint; for arXiv mathematics [and physics], a paper-level table (arXiv identifier, month, primary category, number of authors, keyword flags) and a pseudonymised author–paper table with the variables needed for the namesake-robust variants; PubMed quarterly counts; and the values behind every figure and table. Source metadata are available from arXiv (OAI-PMH, CC0; per-archive statistics at https://arxiv.org/year/<archive>/<year>), the bioRxiv and medRxiv API (https://api.biorxiv.org), the OSF API and PubMed, as retrieved on 15–16 October 2026. [If the author–paper table is withheld: it is available to qualified researchers from (non-author contact, e.g. EMBL Data Protection Office, email), because it allows heavy producers to be identified.]

### Major issue 12. The AI-use disclosure against PLOS's AI policy, and the place of S1 Appendix

- **Locations:** "Use of AI tools" (line 194); CRediT (line 318); S1 Appendix (lines 529–557); figure legends.
- **What the policy requires** (https://journals.plos.org/plosone/s/ethical-publishing-practice#loc-artificial-intelligence-tools-and-technologies):
  - disclosure "in the body of the article", in Methods or Acknowledgements;
  - "the name(s) of any tools used";
  - "a description of how the tool(s) was/were used";
  - "a description of how the user evaluated the validity of the tool's outputs";
  - disclosure of AI use for code;
  - disclosure in the legend of AI use for figure preparation;
  - authors accountable that "the content (including references and methodology descriptions) is accurate and valid";
  - hypotheses, interpretations, results and conclusions must "represent the authors' own ideas".

**Assessment of the current text.**

| Requirement | Status | Comment |
|---|---|---|
| Tools named | Partly | Claude via Claude Code is named; model and version are [AUTHOR]. Version is not strictly required, but it is needed here (Major issue 13) |
| How used | Yes | Clear: search, reference checking, drafting, adversarial review, audits, all code. Add "every section of the text, all code, all figures" for "which parts were affected" |
| Validation by the user | **No** | The only validation described is by "separate AI agents" plus one reproduced number (the bioRxiv index). An AI auditing AI is not the user evaluating the outputs |
| Ideas are the author's | **Not shown** | The record says the groups were "proposed by the essay session" (companion README), the statistical plan "follows the coordinator's message", D3 comes from "research note 7", and the hypotheses were committed in an AI-drafted skeleton. The author must say which elements began as AI proposals and confirm that they were adopted after evaluation |
| References accurate | **Not yet** | S1 Appendix lists items "taken from the research notes without a further check", including quotations from Nee et al., DORA and CoARA and figures from 13 sources. For the essay, 39% of claims were sourced "from the abstract alone". Before submission, the author must check every source cited for a number, quotation or methods claim |
| Figure legends | **No** | The figures were made by AI-written plotting code; add one clause to each legend |

**Does S1 Appendix belong?** Only as a supplement, and in a much reduced form.
- It cannot replace the disclosure in the body.
- As written it is mostly about the essay: 174 claims, 89 markers, 52 quotations and US$267 are the essay session's numbers.
- It includes an internal to-do list ("New in this article, to re-check"), which must be resolved and removed, not published.
- It carries argument and precedent citations: Hutchinson; Osmanovic Thunström; "this record is offered as documentation, not as a first".
- It splits the conflict-of-interest note away from the competing-interests statement.

**Restructure it as "S1 Appendix. AI use and verification record".** It should contain:
- a table by task: task; tool and version; human role; how the output was checked; outcome;
- the reading depth for the 79 references of this article;
- the code-review and re-run log, with commit hashes;
- time and cost for this article and its companion analysis, if the author wishes;
- a link to the archived history.

Move "the paper as its own example" and the precedents to the essay.

**Model Methods text:**

> *Use of AI tools.* I used Claude [model, version] (Anthropic) through Claude Code between 15 October and [date] 2026, on a [account type] account [with model training on my data switched off]. AI agents (i) searched the literature and checked references; (ii) wrote all code for data harvesting, processing, statistical analysis and figures, in a separate session; (iii) drafted the text of every section from my outline and decisions; and (iv) produced internal critical reviews of drafts. [The hypotheses, the definitions of the contrasted groups and the analysis plan were proposed by me / were proposed by an AI agent and adopted by me after (how evaluated); state which.] The interpretation and conclusions are mine. I evaluated the outputs as follows: I re-ran all scripts in a clean environment (commit [hash]) and obtained identical outputs; I reviewed line by line the code that defines groups, flags, author matching and the models; I recomputed [list key numbers] independently from the source APIs; I read in full every source cited for a number, quotation or methods claim and checked every reference against its DOI or URL. Checks performed by AI agents are listed in S1 Appendix but are not counted as validation. No AI tool is an author; I take responsibility for the content.

- **Criterion:** PLOS AI policy; criterion 6 (research integrity).

### Major issue 13. Competing interests: the Anthropic marker, who paid, and where the statement goes

- **Locations:** Competing interests (line 314); S1 Appendix ("Conflict of interest"); the 24 July 2026 marker in Figs 1–3 and S1 Fig.
- **Problems.**
  1. **The only model release marked is an Anthropic model.** The figure files label it "Claude Opus 5", while the text says "an Anthropic model". No other laboratory's release is marked. In an article written with that vendor's tool, the marker invites the reading that this release explains the 2026 surge. That is a perceived competing interest by PLOS's definition: "anything that interferes with, or could reasonably be perceived as interfering with" the work. The marker also has no analytic role. The formal results show physics above trend from 2024, and no test uses 24 July 2026.
  2. **Who paid?** The statement does not say who paid for the Claude account or the compute (at least US$267). Free or discounted access from Anthropic would be a financial interest.
  3. **Placement.** The submission guidelines say competing interests "should not be in your manuscript file" and funding should not be included in it; both are entered in the submission form.
  4. **Consistency across venues** (Major issue 9).
- **Fix.** Remove the model marker from all figures; ChatGPT's release and the arXiv rule dates are enough. If release markers are wanted, mark several labs' releases neutrally, with sources. Then use this wording in the submission form:

> I have no financial relationship with Anthropic or any other developer of AI tools [AUTHOR: confirm; state who paid for the Claude subscription or API use, and whether any credits were received from Anthropic]. I used Anthropic's Claude to draft this article and to write its analysis code (Methods). Because the article studies changes in scientific output in the period in which such tools became available, I declare this use as a potential non-financial competing interest. Anthropic had no role in the study design, data collection and analysis, decision to publish, or preparation of the manuscript, beyond the use of its commercially available product.

---

## 5. Minor issues

**Format and structure** (submission guidelines)
1. Figure legends must sit "immediately following the paragraph in which the figure is first cited"; tables likewise. Both are currently at the end (lines 402–507).
2. Funding and competing interests go in the submission form, not the manuscript file. So do the Data Availability Statement and the CRediT contributions; keep them out of the file or mirror the form exactly.
3. S1 and S2 Appendix must be separate files. Only the captions go at the end of the manuscript.
4. Remove the HTML comments and every [AUTHOR], [RECHECK] and [ANALYSIS PENDING] marker.
5. Missing items:
   - a short title;
   - the corresponding author's e-mail and ORCID iD (required);
   - the full EMBL affiliation.
6. PLOS has no length limit ("Manuscripts can be any length"). After the restructuring in section 3, aim for about 5,000–5,500 words: Introduction about 700, Methods about 1,800, Results about 1,500, Discussion about 1,100.

**Methods and data**

7. Fill the arXiv statistics URL (line 117) from `methods.md` (`https://arxiv.org/year/<archive>/<year>`). Cite the OAI-PMH interface, the OSF API and PubMed (E-utilities), with access dates. PLOS requires all third-party sources to be acknowledged in the Methods. PubMed is new in the formal analyses and is absent from v1's Data sources.
8. Reconcile the harvest dates and coverage. v1 says mathematics, harvested 15 October; `methods.md` says mathematics and six physics archives, harvested 16 October, from January 2019.
9. **Group definitions.**
   - Answer [AUTHOR] at line 139 on whether the medRxiv list was fixed before growth was examined.
   - Document "groups fixed before growth was examined" (line 137) with a timestamp.
   - Justify the classification itself:
     - hep-ph is phenomenology closely tied to experiment;
     - gr-qc includes analysis of gravitational-wave data;
     - genomics includes much sequencing at the bench;
     - hep-ex is dominated by collaboration analyses of data already collected.
10. **Synthetic control.** `methods.md` says 15 donors; `results.md` reports "permutation over 20 units" and lists 14 weights. Reconcile. With 20 units, p = 0.05 is the smallest attainable value; say so.
11. **AI as topic.** C2 depends on bioinformatics. Flag AI-topic papers by keywords in the title or abstract, and re-estimate C2 without them.
12. **arXiv q-bio.** Discuss its metrics (−7% year on year; 1.26 above trend). Consider substitution between servers after the endorsement rule was extended to all arXiv sections in January 2026; it is testable.
13. **Social sciences.** SocArXiv's cap (generally one paper per author per week) and its ban on verbatim AI-generated paragraphs (Table 1) bear directly on the social-science series. Note them, or drop the series from any H1 reading.
14. **The RECHECK figures on medRxiv reproduce from the companion files.** In January–September 2022, COVID-19 preprints were 38.2% of the total. From 2022 to 2026, non-COVID preprints grew 2.51-fold; from 2023 to 2026, flagged preprints grew 1.88-fold, as did non-COVID preprints. Non-COVID growth in 2023 was +33.5%. Remove the flags once the companion confirms (lines 218, 454).

**Introduction**

15. "The main institutional responses so far have been limits…" (line 93): "main" is unsupported. Write "Several institutions have responded by limiting…".
16. "The claim has not been tested with data" (line 99): write "I am not aware of a direct test".
17. "Output was already growing faster than the capacity to read it" (line 93) paraphrases Hanson et al. [8] more strongly than their data, which are growth in indexed articles. State what they measured.
18. **The gap statement** ("Second…", line 99) understates prior work:
    - Nee et al. report a "pseudonymized Mathematics author panel";
    - the abstract of Qi et al. mentions "collaboration and productivity metrics".

    Say what this study adds: a per-paper measure, namesake variants, team size and the decomposition.
19. The main text has 20 direct quotations. A research article should paraphrase most of them.

**Results and language**

20. **Redundancy.** The same numbers recur in the abstract, Results, figure legends, table notes, Discussion and Conclusions. For example, theory's +20% against its ±6% range appears five times. Legends should describe the figure, not restate results. Cut the repeated "markers are dates, not causes" and the COVID-19 shares, which appear in four places.
21. **Terminology.** "Prolific author" is defined as a name string; use "prolific name", or define "author" once. Use "new preprints (first versions)" consistently, not "new submissions" and "new papers" by turns.
22. The abstract (line 83) says bioRxiv "has grown by 10–13% a year since 2023", but line 204 gives 9.5% for 2023. Write "9.5–13%".
23. The Conclusions (line 298) repeat the unsupported claims ("many established authors"; "without any misuse being involved"). Use the model in section 3.8.

**Figures** (https://journals.plos.org/plosone/s/figures)

24. **Format and fonts.**
    - Files must be TIFF or EPS, named Fig1.tif and so on.
    - Fonts must be Arial, Times or Symbol at 8–12 pt. The current SVGs use DejaVu Sans at 6–7 pt.
    - Width (175 mm) and resolution (300 dpi) are compliant.
    - Panel labels in the files are lower-case (a, b); the legends use (A), (B). Make them consistent; PLOS style is upper-case.
25. **Fig 2.** It starts in 2020, so it cannot show the "2017–2025 range" the text relies on. Replace it with, or add, a panel of event-study coefficients by year for C1–C3 with their CIs. Include C3, so that the null contrast is visible. At present only the contrasts that once supported H1 are plotted.
26. **Fig 1 and Fig 2.** Consider log-scaled y-axes for the index plots, so that equal growth rates have equal slopes.
27. **Fig 3.**
    - Relabel panel C "AI-related terms" (Major issue 5).
    - Explain or remove panel D.
    - Consider replacing panels B–D with the distribution of papers per name in Q3 2025 and Q3 2026 under the strictest variant, which is the direct H2 display.
28. **AI disclosure in the legends.** Add one clause to each: "Produced with plotting code written with AI assistance and reviewed by the author (Methods)."

**Tables**

29. **Table 1.** Move it to S1 Table (Major issue 7). Two rows should go:
    - the "Various Chinese universities" thesis-detector row, which is a gate on theses, not a per-person limit, and so fails the table's own definition;
    - the arXiv ban row, which rests on an X thread and two news reports [14–16] and "is not on arXiv's policy pages".

    The caption still carries "[RECHECK: citation needed]".
30. **Table 2 and Table 3.** Add counts (n). Give the 2017–2025 ranges for every arXiv series.
31. **Table 5.** Merge the 20–49 bin into "10 or more" (small cell; Major issue 10). Give n under each namesake variant.
32. **Table 6.** Move it out of the Results (Major issue 6).

**References** (Vancouver; https://journals.plos.org/plosone/s/submission-guidelines#loc-references)

33. **The format is largely right:**
    - numbered in order of first citation, including where tables are first cited;
    - six authors then "et al.";
    - full DOIs;
    - preprints identified by DOI or arXiv URL, as PLOS allows.
34. **Fixes:**

    | Ref | Fix |
    |---|---|
    | [2] | Delete "(uncorrected proof when read…)"; cite the final version |
    | [3] | NLM style for an article ahead of print: "Manage Sci. 2026 Apr 27. doi:…" |
    | [4], [6] | Delete the parenthetical notes on the author versions |
    | [21] | Cite as a *Nature* news item: "Nature. 2026 Oct 13. doi:…" |
    | [23], [36] | One URL each |
    | [41]–[44] | Delete the RECHECK notes. The metadata match the standard citations. Replace [43,44] if Bai–Perron is not the method used, and add the methods actually used: Holm 1979; Driscoll and Kraay 1998; Santos Silva and Tenreyro 2006 (PPML); Abadie, Diamond and Hainmueller 2010; Andrews 1993/2003. Verify each in Crossref |
    | [46] | Add volume and article number |
    | [47] | Must exist with a DOI before submission |
    | [53] | Add the volume: BMJ. 2020;369:m2081 |
    | [63] | Identify the server and check the DOI prefix 10.64898 |
35. **Reliance on preprints and news.**
    - 14 of 79 references are preprints: [13, 19, 30, 31, 34, 35, 39, 47, 48, 59, 63, 65, 66, 76].
    - Five are news or social media: [14, 15, 16, 18, 21].
    - About 16 are institutional web pages. These are legitimate primary sources for policies.
    - The empirical anchors that are preprints are Nee [31], Qi [30], Lin and Zhu [34], Holzwarth [35] and He and Bu [39]. They carry H2's comparison and most of H3. Hedge the claims that depend on them, and update to versions of record where published.

    After the cuts in Major issue 7 and the move of Table 1 to the Supporting Information, the list should fall to about 35–40 references, with fewer preprints and no social media.

**Other**

36. **The AI used in this review.** The "four reviewers … two rounds" are simulated AI reviews. Do not describe them in the article as peer review. The disclosure's "reviewed drafts adversarially" is the right wording.
37. **Reporting guideline.** PLOS mandates none for bibliometric studies. A voluntary STROBE-style checklist in the Supporting Information would help reviewers check design, data sources, bias and study size; this is optional.

---

## 6. Compliance checklist

✓ met · ✗ not met (blocks submission) · ? open or depends on a decision. Statuses refer to v1 plus the formal results.

| Requirement (source) | Status | Note |
|---|---|---|
| **Criterion 1:** original research, not essay or opinion (criteria) | ✓ / ? | Original meta-research ✓. D2 and D3 read as an essay (Major issue 7) |
| **Criterion 2:** not published or under consideration elsewhere; original figures (criteria) | ? | Zenodo preprint allowed; EMBO essay with the same figures is a conflict (Major issue 9) |
| **Criterion 3:** technical standard, described in detail (criteria) | ? | Sound core; deviations undeclared; break tests blind to 2025–2026; C1 underpowered (Major issue 4) |
| **Criterion 4:** conclusions supported; implications labelled as hypotheses (criteria) | ✗ | Title, abstract, D1–D3 and Conclusions (Major issues 1–3, 7, 8) |
| **Criterion 5:** intelligible English (criteria) | ✓ | Clear; dense with numbers; repetitive (Minor issue 20) |
| **Criterion 6:** ethics; third-party personal data statement (criteria; `#loc-personal-data-from-third-party-sources`) | ✗ | No committee or officer oversight; risks not declared (Major issue 10) |
| **Criterion 7:** minimal data set and code (data-availability and code-sharing policies) | ✗ | H2, medRxiv flags, H3 and PubMed data not covered; nothing deposited (Major issue 11) |
| Data Availability Statement names the repository and DOI (data availability) | ? | Placeholder acceptable at submission; content must change |
| Licence no more restrictive than CC BY; code licence (data availability; code sharing) | ✗ | [AUTHOR: licence] |
| Zenodo acceptable (recommended repositories) | ✓ | |
| AI disclosure in the body of the article (AI policy) | ✓ | Methods, "Use of AI tools" |
| AI: tools named | ✓ / ? | Model and version missing |
| AI: how used, and which parts | ✓ | Add "every section, all code, all figures" |
| AI: how the user evaluated validity | ✗ | Only AI-on-AI audits described |
| AI: hypotheses and interpretations are the author's own | ? | Must be stated (Major issue 12) |
| AI: disclosed in figure legends | ✗ | Minor issue 28 |
| AI not listed as an author | ✓ | |
| Competing interests declared, in the submission form (competing interests; guidelines) | ✗ | In the manuscript file; payment unstated; model marker (Major issue 13) |
| Funding statement in the form, PLOS wording (guidelines) | ✗ | Placeholder |
| Ethics statement adequate (guidelines) | ✗ | Major issue 10 |
| Third-party sources acknowledged in the Methods (guidelines) | ✗ | URL missing; OAI-PMH, OSF and PubMed not cited (Minor issue 7) |
| Related manuscripts disclosed, with copies (guidelines) | ? | Zenodo and EMBO essays; Nature Correspondence |
| Title of at most 250 characters, sentence case (guidelines) | ✓ | Content must change |
| Short title of at most 100 characters (guidelines) | ✗ | Missing |
| Abstract of at most 300 words, no citations (guidelines) | ✓ / ✗ | 274 now; over 300 once the pending sentence is added |
| Section order: Introduction, Methods, Results, Discussion, optional Conclusions (guidelines) | ✓ | |
| Figure legends after the first-citing paragraph (guidelines) | ✗ | At the end |
| Tables after the first-citing paragraph, in the manuscript (guidelines) | ✗ | At the end |
| Figures in TIFF or EPS, Arial/Times/Symbol at 8–12 pt, named Fig1.tif (figures) | ✗ | DejaVu Sans at 6–7 pt; SVG, PDF and PNG |
| Figure width, resolution, RGB (figures) | ✓ | 175 mm; 300 dpi |
| Supporting Information named S1…, captions at the end, separate files (guidelines) | ✓ / ✗ | Names ✓; appendices inline ✗ |
| References: Vancouver, numbered in order, square brackets, six authors et al. (guidelines) | ✓ | Fixes in Minor issue 34 |
| No unpublished work in the reference list (guidelines) | ✗ | Ref [47] has no DOI yet |
| Preprints cited with a DOI or arXiv URL (guidelines) | ✓ | |
| CRediT contributions in the submission system (guidelines) | ✓ / ? | Draft present; confirm the [AUTHOR] items |
| Corresponding author e-mail and ORCID iD (guidelines) | ✗ | Placeholders |
| Data-source terms complied with (arXiv API terms; bioRxiv API; OSF) | ? | arXiv CC0 ✓; state rate-limit compliance; check OSF and NCBI |
| Null results acceptable (criteria, criterion 1) | ✓ | If framed as in section 3 |
| Analysis plan time-stamped; deviations reported (good practice; criteria 3 and 4) | ✗ | Major issue 4a |

---

## 7. Strengths to keep

1. **The within-field design.** Contrasting experimental with non-experimental work inside a field is the right idea, and sharper than comparisons between fields. Its null result is informative because the design was good.
2. **Integrity in reporting.** v1 reports the medRxiv null and corrects the essay's ×2.3 against ×1.6 comparison for COVID-19 (header note, lines 38–43), including in the essay drafts. Keep this reflex throughout the reframing.
3. **The formal analysis is careful.** It has:
   - month fixed effects;
   - Driscoll–Kraay errors;
   - correction for multiple testing;
   - negative controls in space and within groups (462 splits; 153 archive pairs);
   - leave-one-out estimates;
   - minimum detectable effects;
   - sensitivity to the base year;
   - an independent replication of Nee et al.'s 11.9% synthetic-control gap.

   Few bibliometric papers do this much.
4. **COVID-19 handling.** It is explicit and quantified: the medRxiv exclusion, the bioRxiv sample from May–June 2022, and a 2019 base.
5. **The heavy-producer analysis is unusually transparent about its limits.** It has namesake variants, team size, subfields, left-censoring, and scripts that print aggregates only (verified in `robustness_math_prolific.py`).
6. **Openness about AI use.** The disclosure is ambitious, a single human author is accountable, and no AI is an author. With validation added, this can be a model disclosure.
7. **Writing and figures.** The prose is clear and precise. The figures use a palette safe for colour blindness, label lines directly, and carry honest caveats in the legends.
8. **Limitations.** The section (lines 286–294) is candid about detector bias, the limits of preprints and the absence of preregistration.

---

## Appendix: the reviewer's own checks (reproducible from repository files)

- **Growth rates.** Recomputed from `paper/figures/within_field_quarterly.csv`:
  - January–September growth matches Table 3;
  - experimental archives' 2026 growth (+10.5%) is the second-highest of 2017–2026;
  - Q3 2026 year on year: hep-ex +25.1%, theory +26.0%, experiment +17.6%.
- **Crude ratios of rate ratios** (January–September totals; not model estimates):
  - 2026 against 2017–2022: theory/experiment about 1.05;
  - 2026 against 2019–2022: computational/wet lab about 1.03;
  - 2026 against 2022 alone: about 1.12 and about 1.11.
- **medRxiv RECHECK figures.** Reproduced from `medrxiv_public_dataset_quarterly.csv` (companion branch) and the quarterly file (Minor issue 14).
- **H2 decomposition** from Table 5: (3,549 − 575) / (19,562 − 10,846) = 34%.
- **Admissible break dates under 15% trimming:**
  - arXiv series from January 2015: 2016-10 to 2024-12;
  - bioRxiv: 2020-02 to 2025-08;
  - medRxiv: 2020-08 to 2025-08.
- **Word counts** (prose, without markers or citations):
  - D2: 583;
  - D3: 513;
  - Results on H1: 657;
  - main text: 6,979 (header of v1).
- **References.** First citations: 23 in D3, 13 in D2, 10 only in tables.
- **Quotations:** 20 in the main text.
- **Text overlap** with the essays: at most 5% of 10-word sequences in the abstract and main sections; higher only in the boilerplate statements.
- **Figure fonts.** The SVG files use DejaVu Sans at 6–7 pt.
- **Scripts.** `analyze_math.py` compiles the AI and Lean patterns with `re.I`.
