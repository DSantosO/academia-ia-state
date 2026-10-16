# Response to the round-1 internal reviews (R1–R4)

- **Manuscript.** Draft v2, 16 October 2026: `paper/plos_one/draft_v2.md`, built from `paper/plos_one/build/draft_v2_keyed.md` by `build/build_v2.py` (references in `build/refs_v2.py`).
- **Reviews.** R1 statistics; R2 scientometrics and preprint data; R3 experimental physics and biology; R4 PLOS ONE Academic Editor (`paper/plos_one/reviews/round1/`). All four were written by AI agents in reviewer roles. They are internal reviews before submission, not peer review, and the article does not describe them as peer review (R4 minor 36).
- **Prepared by** an AI agent (Claude, Anthropic, via Claude Code) from the author's decisions of 16 October 2026 (`paper/brief.md`) and the coordinator's messages. Not yet checked by the author [AUTHOR: approve or amend each response].
- **Sources of new numbers in v2.** The companion analysis only (`paper/plos_one/stats/`; companion commits 37b4b11, f5ab16e, 7ac5647, 26ce2eb and 0e239cd), plus R3's documented INSPIRE-HEP queries, reported as motivation only. Two derived values were computed here from the companion's coefficients, with the method stated in the table note: the Bonferroni intervals and minimum detectable effects at α/3, and C3's year-shock ratio after the medRxiv correction. The pre-registration of the paper-level tests is in commits 763aa2b and 78890e5, with deviations in 11264ee and 1de63a9.
- **Locations** refer to section headings of v2. Line numbers in the reviews refer to v1.

**Status codes.**
- **Done**: changed in v2.
- **Partly done**: changed, but not fully as requested; the remainder is explained.
- **Pending**: an analysis not yet run. The label matches an `[ANALYSIS PENDING: …]` marker in v2.
- **Author**: needs the author's decision or information. Matches an `[AUTHOR: …]` marker in v2.
- **Declined**: not done, with the reason.

---

## 1. Main changes in v2

1. **Reframing (all reviewers).** H1–H3 are reproduced verbatim as recorded in the skeleton (commit 2cac071, 16 October 2026, 16:42 UTC). The pre-specified within-field tests are reported plainly as not supporting H1: physics 1.14 (95% CI 1.00–1.30; Holm p = 0.11), inconclusive and underpowered; biology 1.08 (1.03–1.14; p = 0.01), fragile; medicine 1.01 (0.90–1.14; p = 0.84), null. Each contrast is reported with its Bonferroni (98.3%) interval, minimum detectable effect, in-space placebo p and year-shock calibration. The placebos are the primary inference.
2. **New title** ("Preprint output in the generative-AI era: pre-specified within-field tests find no robust evidence of an experimental bottleneck"). It is a working title. The reviewers' alternatives are listed in an HTML comment under it, with a short title [AUTHOR: choose].
3. **New abstract** (298 words). It gives all three contrasts with intervals and Holm p, the placebo results, and the two checks that decide their reading: physics without the Snowmass base, biology without bioinformatics. It adds the exploratory paper-level result, the marker result (H3), the departures from trend with their counterfactual named, the H2 result and a closing sentence on what the data cannot show.
4. **Methods aligned with the analysis that was run** (`stats/methods.md`): PPML with month fixed effects and group-specific calendar-month effects; Driscoll–Kraay errors labelled as within-year only; Holm adjustment with Bonferroni intervals; placebo-based inference; minimum detectable effects at α = 0.05 and α/3. A section on **Deviations from the analysis plan** lists every change from v1's plan and gives approximate estimates under the planned baselines. Another states what "pre-specified" means here: fixed before any model was estimated, not before the data were seen.
5. **All round-1 analyses delivered by the companion are integrated** (commits 26ce2eb and 0e239cd):
   - pooled bases, year-shock calibration, acceleration (2026/2025) and slope changes;
   - variants of C1: without gr-qc, as a correction made after the results; hep-ph/hep-ex and hep-th/hep-ex;
   - Snowmass 2021 and European Strategy papers removed: C1 1.06 (0.89–1.25); hep-ex's departure from trend 1.58 (1.38–1.82) instead of 1.37;
   - genres in mathematics and the six particle and nuclear physics archives: research articles alone departed as much as all papers or more;
   - list entries; break tests that admit breaks up to January 2026; the synthetic control in context; PubMed US against non-US articles;
   - medRxiv: duplicates removed, a title-only COVID-19 filter, and Spick et al.'s four missing datasets;
   - H2 and H3 for mathematics;
   - the exploratory INSPIRE-HEP classification registered in the pre-registration.
6. **H2 rebuilt** on concentration shares and a decomposition of growth by author class ranked on combined output (no regression to the mean), with pre-ChatGPT pairs of years as the chance benchmark. Theoretical physics: broad-based but concentrating (top 1% +44%, bottom 90% +21%). Mathematics: broad-based but strongly concentrating (top 1% +266%, next 9% +121%, bottom 90% +57%). Mathematics' pattern holds without September, for names active in 2019–2024, for namesake-robust names and for January–August windows. "Established" is dropped as a claim, and the fixed-threshold measures are descriptive only (S3 Table).
7. **H3 rebuilt on the companion's marker analysis** (Kobak et al.'s style words, filtered on baseline data). It leads with 2024 and states the drift of the words after 2024. Markers rose in every group, experimental ones included. They did not predict output: mathematics had the smallest rise (×1.62 in 2024) and the largest acceleration (2026/2025 relative to bioRxiv 1.27, 1.04–1.56). Published estimates are moved to S4 Table.
8. **Field-level divergence reported as exploratory**, with its counterfactual named: each series' own 2015–2022 trend. In levels, bioRxiv grew more than the physics archives tested. Two candidate explanations were checked and do not account for the divergence: genres, and the papers of planning exercises. Four remain open, each with a pending check or stated as untested.
9. **Pre-registered paper-level tests** of the refined hypothesis are described in Methods and Discussion, with both recorded deviations and no results. The refined hypothesis originated with the author. The exploratory INSPIRE component is reported in Results: within hep-ex and nucl-ex, papers reporting new experimental results grew as fast as the rest (ratio 1.00, 0.74–1.35).
10. **Discussion rebuilt** in five parts: principal findings; what the within-field tests show; why arXiv might differ from bioRxiv; a short "Implications for research evaluation" (about 520 words, labelled as interpretation); and Limitations. The Conclusions follow R1's and R4's model. The rationing table (v1 Table 1) is now S1 Table, and the seven recommendations are condensed into one paragraph of untested proposals.
11. **PLOS compliance.**
    - An ethics statement for third-party personal data.
    - Terms of use and request rates for every source, including two retrievals that exceeded documented limits.
    - A data availability statement covering the minimal data set.
    - An AI-use disclosure per PLOS policy, saying what the author originated and how outputs are to be validated.
    - An AI clause in every figure legend.
    - Competing-interests and funding statements in a "submission form" block outside the manuscript.
    - Legends and tables placed after the paragraph that first cites them.
    - S1 Appendix rewritten as an AI-use and verification record for this article only.
12. **References.** Corrected per R4 minor 34 and R2 minor 13. Added: the methods actually used; the scientometric literature R2 verified; and the data-source documentation. Metadata of added references were read from Crossref or arXiv on 16 October 2026.
13. **Model-release marker removed** from all figures (re-exported at companion commit 0e239cd), legends and the competing-interests text, by the author's decision of 16 October. Only ChatGPT's release and arXiv's rule dates are marked.
14. **Late data corrections.** The medRxiv API lists some version-1 preprints twice, and medRxiv's monthly totals include these duplicates. Every medRxiv number now counts each DOI once. Non-COVID growth was 20.9% in 2025 and 16.4% in 2026, so medicine slowed in 2026 rather than accelerated. C3 stays null. bioRxiv is being checked for the same problem, and its totals carry [RECHECK: bioRxiv duplicate check pending].

## 2. Analyses still pending

Each label matches a marker in v2.

| Label in v2 | Requested by | What it decides |
|---|---|---|
| planned specification | R1 M1, analysis 1; R3 M11; R4 Major 4a | The estimate under v1's plan (period effects against 2017–2022 and 2019–2022, Bonferroni intervals). Approximate values (1.05, 1.02, 1.05) are in Table 1 |
| structure-matched placebos | R1 M2, analysis 2; R3 M1, M4a | Whether C1 and C2 survive placebos with their own structure: 4-against-2 draws of physics archives; 455 choices of 3 of 15 categories |
| bioinformatics split by AI/ML topic | R1 analysis 3; R3 M4, analysis 4; R4 minor 11 | Whether AI is a topic or a tool in C2 |
| US vs non-US split on bioRxiv | R1 M3, analysis 4; R3 analysis 5 | Whether a funding shock or AI cost lies behind the 2026 wet-lab slowdown |
| bioRxiv categories without COVID-19 preprints | R1 M1, M3; R2 M4; R3 minor 7 | Symmetric treatment of COVID-19 in C2 |
| medRxiv flags (hand-coded validation of the regular expressions) | R1 minor 7; R2 M5; R3 M5 | Precision and recall of the C3 flag and the COVID-19 filter. A coding sheet exists; the extended list and the title-only bound are done |
| dating by first-version submission, with January–August versions of every 2026 estimate | R2 M2, analysis 1; R1 M7, analysis 7 | Announcement throughput and the September 2026 spike |
| synthetic control with the OAI mathematics series, physics-only donors and math-ph excluded | R1 minor 8, analysis 9 | A cleaner replication of Nee et al. |
| OSF continuity check | R2 M8 | Whether the social-science series is continuous across its change of counting method in 2025 |
| pre-registered test | R3 analysis 3; R2 M4, analysis 5; R1 analysis 6 (in part) | The confirmatory paper-level tests on held-out material |
| record-level identifier and flag tables for the deposit | R2 M10; R4 Major 11 | PLOS's minimal data set |
| software versions and a pinned environment | R2 M10 | Reproducibility |

**Pending items without a label:**
- C3's slope change on the corrected medRxiv series. The Table 1 cell reads "not yet recomputed".
- bioRxiv duplicate check. It carries a [RECHECK] marker.
- Assembly of S2 Table (growth by archive and category) from the companion files.

**Completed since the first version of this response** (companion commit 0e239cd):
- Snowmass and European Strategy papers removed;
- genre decomposition (mathematics and particle and nuclear physics; cond-mat, astro-ph and quant-ph are excluded until the held-out test is run);
- mathematics H2 and H3;
- the exploratory INSPIRE-HEP classification;
- the medRxiv extended dataset list and title-only bound;
- the medRxiv duplicate correction.

## 3. Points declined or only partly followed

| Point | Decision and reason |
|---|---|
| Restate H1 "as tested" and delete its second clause (R4 §3.5); restate H2 operationally (R4 Major 5) | **Declined.** H1–H3 are kept verbatim, as recorded before modelling (R1 §7.3; the author's brief). Rewording them would blur what was pre-specified. The Introduction then states which clause each analysis tests, and Methods gives the operational measures. Results report the second clause of H1 as not supported in physics |
| Rambachan–Roth sensitivity (R1 M1, M3, analysis 8) | **Declined.** The pre-specified tests are already reported as not supporting H1. Sensitivity bounds can only widen the intervals, so they cannot change that reading. Dependence on the counterfactual is shown directly in Table 1: base 2019, pooled bases, the planned baseline, a cleaned 2022 base, the trend-adjusted variant, the year-shock calibration and the placebos |
| Fixed-b or small-sample critical values for Driscoll–Kraay intervals (R1 M2 fix 4) | **Declined.** The placebos are the primary inference. The Driscoll–Kraay intervals are labelled as within-year uncertainty and treated as secondary. Recomputing them would widen intervals already treated as too narrow, without changing any reading |
| End-of-sample instability test (Andrews 2003; R1 M7; R4 Major 4c) | **Declined.** Replaced by sup-Wald tests with 5% trimming, whose last admissible date is January 2026, and by fixed-date Wald tests. The text says that breaks at that boundary may be later. Claims about timing rest on yearly departures from trend |
| Indicators for arXiv rule dates in the models (R2 M8 fix 1, analysis 7) | **Declined.** They are nearly collinear with 2026 (R1 M7). The text argues the direction of each rule instead: endorsement and language rules restrict entry. Variants that drop November 2025 to February 2026, or end in October 2025, are in S5 Table |
| 2017–2019 as primary or co-primary base; new groupings as primary analyses (R3 M2, M3; R2 minor 3) | **Declined as primary.** Changing the primary estimate or the groups after seeing estimates is the forking path R1 §7.7 warns against. The alternatives are reported beside the pre-specified estimate: base 2017–2019 and pooled bases; a cleaned 2022 base; theory without gr-qc; hep-ph/hep-ex; hep-th/hep-ex; gr-qc/experiment. Not done: physics.ins-det and physics.data-an as an experimental-methods series, hep-lat as a third arm, and nucl-th/nucl-ex as a separate contrast. Classifying cond-mat papers is part of the pre-registered tests |
| Poisson mixed model with random slopes by category (R3 M4) | **Declined** in favour of the exact permutation over category assignments that R1 recommends [pending: structure-matched placebos]. The permutation needs no distributional assumptions |
| Classifier for drift in category choice; classification from full JATS text (R3 M4) | **Declined for this version.** The pre-registered tests classify papers from titles and abstracts. Full text is future work |
| Normalising categories by journal output; coverage ratios (R2 M4 fix 4, analysis 4) | **Declined for this version.** It needs a new source (OpenAlex) and a mapping of categories to journal subfields. Propensity to post is named in the Discussion as an untested explanation |
| A journal version of C3; comparison with registered trials; C3 in PubMed; health informatics split by AI topic (R2 M5 fix 3; R3 M5, analysis 8) | **Declined for this version** (new data and new flags). C3 is reported as a weak test in this venue. The medRxiv arm of the pre-registered tests classifies papers with new primary data against those without |
| Liang et al.'s distributional estimator (R2 M7 fix 2, analysis 10) | **Declined.** It would need a reimplementation and a reference corpus. Their published bioRxiv values are flagged for the author to read (S4 Table) |
| Identifier-matched author subsample (OpenAlex, ORCID); country composition; exact replication of Nee et al.'s panel; batch posting; a Q4 2026 test (R2 M6, analysis 3) | **Declined for this version.** The January–August window gives a close comparison with Nee et al.: the share of names with five or more papers rose from 2.34% to 3.73%, against their 2.45% to 3.80%. Batch posting needs submission times, and dating by submission is pending. Q4 2026 is not yet complete |
| Policy event study with first-time submitters; comparisons with ChemRxiv and EarthArXiv; thinness and later outcomes (R2 analyses 7, 9, 11) | **Declined for this version** (new data). The policy dates are listed in S2 Appendix |
| Lags from data to paper (R3 M7, analysis 6) | **Declined for this version.** Stated in Limitations as a testable prediction of the Amdahl-type bound |
| Within-person contrasts with INSPIRE author identifiers; physics heavy producers with INSPIRE identifiers (R3 analysis 7, minor 15) | **Declined for this version.** The INSPIRE component classifies papers by curated metadata, not authors |
| Uniform-scaling simulation null for fixed-threshold counts (R1 M8 fix 2) | **Declined.** The fixed-threshold measure is descriptive only (S3 Table). The decomposition on combined output has an analytic null (every class grows at the total rate under proportional growth) and an empirical benchmark from pairs of years before ChatGPT's release |
| Cut the evaluation material to about 150 words (R3 M10) or to two sentences without DORA and CoARA (R4 Major 7) | **Partly declined.** The author asked for a short section stating the thesis at the strength the data allow. It is about 520 words, labelled as interpretation, with every claim scoped. The rationing table is S1 Table, and the recommendations are one paragraph of untested proposals, credited to their sources. The DORA/CoARA sentence uses wording the author approved and carries R4's caveats: the measurements predate CoARA, and the Commission's study found engagement "broad and growing" |
| Prospective re-test on 2027 data (R1 analysis 6; R2 analysis 12; R4 §3.9) | **Not mentioned.** No registration for 2027 data exists, and R4 asks that none be described before it does. The active pre-registration tests paper-level hypotheses on data already collected, in archives and servers not used to form them [AUTHOR: decide whether to register a 2027 test] |
| Length of about 5,000–5,500 words (R4 minor 6) | **Partly declined.** The main text is about 7,100 words. Methods must now report deviations, terms of use, ethics, AI use and the pre-registered tests, and Results carry the round-1 analyses the reviewers asked for. PLOS ONE sets no limit |
| Figure changes: log axes and indexing to 2019 (R1 minor 3; R4 minor 26) | **Partly done.** Fig 2D shows the event-study coefficients on a log scale. The figure files belong to the companion, and the other changes are requested of it. The Fig 1 legend states how indexing to 2022 biases the comparison |
| Rename the theory group "theory and phenomenology" (R3 M2b) | **Declined.** The pre-specified labels are kept. The Discussion says that hep-ph is phenomenology fitted to data |
| Add `\b` before `covid` in the COVID-19 expression (R2 minor 9) | **Not done.** R2 judged the effect negligible; the note is passed to the companion with the flag validation |
| Mention the partial October 2026 counts (R2 minor 15) | **Declined.** The month was incomplete at harvest, and its dating by announcement is pending |
| STROBE-style checklist (R4 minor 37) | **Optional; not done** [AUTHOR: decide] |

## 4. Decisions and information needed from the author

- **Title** and short title.
- **Gaps in the record:** why hep-lat was left out of C1; when the medRxiv dataset list was fixed; the reasons for, and timing of, the change of reference year; when the companion fixed its model specification relative to v1.
- **Kusumegi et al.:** whether to keep their output-gain estimate (Introduction; Limitations).
- **Data-protection consultation** (UPF and EMBL): office, date, outcome, lawful basis and safeguards. Whether to release a pseudonymised author table and, if not, a non-author contact for access.
- **Zenodo deposit:** DOI and licences (CC BY 4.0 for data and MIT for code, as suggested).
- **AI disclosure:**
  - model and version, dates, account type, and whether training on the author's data was switched off;
  - the author's own validation: code review, re-runs, numbers recomputed, sources read in full;
  - which AI proposals were adopted, modified or rejected, and the origin of H2 and H3;
  - a spot-check of the INSPIRE classes (S1 Appendix).
- **Pre-registered tests:** the classifier's model and version, and an OSF Registries DOI, if registered.
- **Funding and competing interests:** who paid for the AI tools; any credits from Anthropic; statements aligned across venues.
- **Related manuscripts** (R4 Major 9):
  - the EMBO Reports essay draft uses the same figures;
  - post this article as a preprint;
  - disclose the Zenodo essay and the Nature Correspondence, with copies;
  - mint the companion essay's DOI.
- **Recommendations:** merge or confirm the shortlist of proposals in "Implications for research evaluation".
- **Optional:** ask arXiv for monthly moderation statistics (R2 M2 fix 5).
- **[RECHECK] items** to resolve before submission:
  - quotations;
  - the figures from McKiernan et al., Rice et al., the Commission's study and Lin and Zhu;
  - Liang et al.'s bioRxiv series;
  - arXiv's post of 1 October 2026;
  - INSPIRE's request rate and terms;
  - the bioRxiv duplicate check.

---

## 5. Reviewer 1 (statistics)

### Major issues

**R1-M1. The estimand does not match H1, and the reference period differs from the plan.**
- **Report the planned quantity as confirmatory.** *Partly done; pending.*
  - The change to 2022 is disclosed as a deviation, with the pre-period coefficients that make 2022 a low year for C1 and C2 (Methods, Deviations from the analysis plan).
  - Approximate values under the planned baselines are in Table 1 (1.05, 1.02, 1.05). They are labelled as not model estimates.
  - The model estimate under the planned specification is pending [planned specification].
  - Every reading (pre-specified, pooled, planned) points the same way, so the conclusion that H1 is not supported does not depend on it. [AUTHOR: reasons for, and timing of, the change of reference year.]
- **Show the whole path and a specification summary.** *Done.* Table 1 gives:
  - the event-study coefficients for 2023–2025;
  - the pre-period coefficients outside 0.9–1.1;
  - bases 2019, pooled and approximate planned, plus a cleaned 2022 base for C1;
  - the trend-adjusted estimate.

  Fig 2D shows the full path. A 2023–2024 base was not computed.
- **An estimand that matches "acceleration".** *Done.* The 2026/2025 ratio, and the change in slope of the deseasonalised log ratio after December 2022 and November 2024 (Table 1; Methods, Robustness and acceleration). The Rambachan–Roth analysis is declined (Section 3).
- **Treat COVID-19 the same way in every contrast.** *Pending* [bioRxiv categories without COVID-19 preprints]. The asymmetry is stated in Methods and in Limitations. For medRxiv, a title-only filter gives a bound: C3 1.07 (0.95–1.21).

**R1-M2. Model specification and inference.**
- **Describe the model actually run.** *Done* (Methods, Within-field contrasts): PPML, month fixed effects, group-specific calendar-month effects, Driscoll–Kraay errors with 12 lags. The negative-binomial sentence is gone.
- **In-space placebos as primary inference.** *Done* (Methods; Results; Table 1): 0.61 for C1 and 0.20 for C2. Placebos matched to each contrast's structure are *pending* [structure-matched placebos]. Methods states what the placebos answer: whether the experimental split predicts divergence better than arbitrary splits.
- **In-time placebos and a parametric version.** *Done.*
  - The pre-period coefficients of the same estimator are reported (Table 1).
  - The year-shock ratio (2026 coefficient over the SD of the pre-2022 year coefficients) is 1.54 (p = 0.12) for C1, 0.67 (0.50) for C2 and 0.19 (0.85) for C3.
  - The share of pre-2022 years at least as large (2 of 7 for C1) is in S5 Table.
- **Robust intervals as secondary.** *Done.* They are labelled "within-year uncertainty", and the Results state that 4 of 13 pre-period year coefficients have p < 0.05. Fixed-b critical values are declined (Section 3).

**R1-M3. Parallel trends fail in biology; the 2026 movement in C2 is a wet-lab slowdown.**
- **Rambachan–Roth sensitivity.** *Declined* (Section 3).
- **Remove COVID-19 from bioRxiv.** *Pending.*
- **Test the funding explanation.** *Pending* [US vs non-US split on bioRxiv]. Its prediction is stated before the analysis (Discussion, explanation ii): a funding shock would depress US wet-lab output first. The PubMed check is done: US articles fell relative to others from 2025 (0.91 in 2026), which accounts for about 1.7 of the roughly 7 points by which PubMed fell below trend.
- **Describe C2 as it is.** *Done* (Results). C2 is fragile in level and rests on bioinformatics (0.93 without it). Its slope rose after December 2022 (10.8% a year), but its strongest break is in July 2020, during adoption. In 2026 the movement was mainly a wet-lab slowdown (13% to 8%) while computational growth held (20% and 18%).

**R1-M4. The contrasts are weak proxies; negative controls and leave-one-out estimates need restating.**
- **Report each contrast for what it is.** *Done.* C1 is inconclusive and depends on nucl-ex and on the 2022 base. C2 depends on bioinformatics. C3 is a weakly targeted null (Table 1, "Reading"; Results).
- **State a robustness criterion for leave-one-out.** *Done* (Methods): "robust only if no single exclusion moves it across 1", stated as set after the estimates were seen. C1 and C2 fail it.
- **Measure experimental intensity at paper level for any prospective test.** *Done* in two ways:
  - the pre-registered tests classify individual papers [pending];
  - the exploratory INSPIRE classification found papers reporting new experimental results growing as fast as the rest within hep-ex and nucl-ex (1.00, 0.74–1.35).

**R1-M5. Multiple testing and the decision rule for H1.**
- **Decision rule.** *Done* (Methods, Deviations). Per-contrast claims are under Holm control, and H1 as a general claim needs support in all three fields, a rule stated after the fact and labelled as such.
- **Holm p with Bonferroni intervals.** *Done* (Table 1).
- **Negative controls and placebos unadjusted, as distributions.** *Done.* Benjamini–Hochberg is dropped and the change is listed as a deviation.
- **Direction.** *Done.* Reversals are reported (C2 0.87 against 2019; 0.93 without bioinformatics). The C1 particle-physics pairs fall below 1 once the base is cleaned (0.88; 0.87), although their intervals include 1.

**R1-M6. Power.**
- **Report MDEs at Holm's level.** *Done:* 1.25, 1.09 and 1.22 at α/3, beside 1.21, 1.08 and 1.19 at α = 0.05 (Table 1).
- **Report MDEs with year-level variance.** *Partly done.* Year-level variation is shown by the year-shock calibration rather than folded into a new MDE.
- **Interpret nulls through their upper limits.** *Done.* C3 excludes increases above 14%; C1's interval runs to 1.30 and "excludes almost nothing of interest" (Results).
- **Abstract.** *Done.* It states that the physics test could detect only ratios above 1.21 (α = 0.05, as R4 asked); 1.25 at α/3 is in Table 1.

**R1-M7. Break tests, placebo dates and arXiv's rule changes.**
- **2026 breaks.** *Done.*
  - The companion's sup-Wald tests now use 5% trimming, with January 2026 as the last admissible month, plus fixed-date Wald tests.
  - The Results say that breaks found at that boundary may be later, and timing claims rest on yearly departures. The physics slope break is in May 2025; particle and nuclear physics and mathematics break at the January 2026 boundary.
  - The Andrews (2003) test is declined (Section 3).
- **Placebo dates.** *Done.* They are descriptive, in S5 Table. The year-shock calibration uses the identical estimator.
- **Rule-change indicators.** *Declined*, as R1 itself argues. The direction of each rule is argued in the Discussion, and the drop-window variants are in S5 Table.
- **The endorsement rule biases the H2 share upwards.** *Done.*
  - The Results say so for the fixed-threshold measures.
  - A decomposition restricted to names active in 2019–2024 removes newcomers; the top 1% still grew by 210% and the bottom 90% by 48%.
- **September 2026.** *Partly done.*
  - The synthetic-control excess is about 8% without September.
  - The mathematics decomposition is repeated for July–August and for January–August.
  - January–August versions of every 2026 estimate are *pending* [dating by first-version submission, and January–August versions].

**R1-M8. The heavy-producer measure is mechanical.**
- **Decomposition as the main statistic.** *Done* for physics theory and mathematics (Results, H2; Fig 3C–D).
- **Uniform-scaling null.** *Declined* (Section 3).
- **Longer histories.** *Done.* Histories from 2019, a variant restricted to names active in 2019–2024, and "established" dropped as a claim.
- **Annual windows.** *Partly done.* January–August windows are reported; full-year 2026 is not yet available.
- **Mention comparisons clustered by author.** *Moot.* Mentions of AI, Lean and Erdős are no longer used.
- **Drop the sampling intervals.** *Done.* "The data are a population, so shares carry no sampling intervals."

**R1-M9. What the design can say about causes.**
- **Causal verbs.** *Done.* They are removed from the title, abstract and text.
- **Vendor marker.** *Done.* It is removed from all figures.
- **Legitimacy.** *Done.* "Needs no misuse" is gone. The Implications section is labelled as interpretation, and the Introduction and Discussion each state that the design cannot attribute the changes.

**R1-M10. Descriptive inferences that do not hold.**
- **Range comparisons.** *Done.* Removed and replaced by rate ratios and their intervals.
- **Year-on-year rankings.** *Done.* Replaced by departures from trend; computer science stands at 1.15 (0.97–1.37) against its 21%-a-year trend.
- **Endpoints.** *Done.* Third quarters and January–August windows replace monthly endpoints.
- **"No break" on bioRxiv.** *Done.* Replaced by the estimate (0.91, 0.71–1.15) and the slope-break test (p = 0.17).
- **Wrong corpus for H3.** *Done.* H3 rests on the companion's markers; Lin and Zhu are in S4 Table with the q-bio caveat.
- **q-bio.** *Done.* It fell 7% in 2026 but stands at 1.26 of trend (Results).
- **The medRxiv window.** *Done.* C3 is reported under several bases and with unique DOIs: the flagged and other non-COVID preprints grew 2.40-fold and 2.39-fold since 2022.

### Minor issues

1. **Describe the model run; data window.** *Done* (Methods; arXiv from 2010, models from 2015).
2. **Counts, pre-period coefficients and placebo shares in the contrasts table.** *Done* (Table 1).
3. **Indexing to 2022.** *Partly done* (Fig 2D on log scale; legend caveat). Log axes and an index to 2019 are requested of the companion.
4. **Yearly change in the log ratio with its 2017–2025 range.** *Pending.* It goes into S2 Table, which is still to be assembled from the companion files.
5. **Rounding slip.** *Done* ("9–13% a year").
6. **"1.9 million".** *Done* (removed).
7. **Validate the regular expressions.** *Pending* [medRxiv flags]. The AI-tools expression is no longer used and was removed from S2 Appendix.
8. **Aliased categories; OAI series for the synthetic control; donor count.** *Partly done.*
   - The aliasing is stated in Methods and S2 Appendix.
   - The synthetic control with the OAI series and clean donors is pending.
   - S2 Appendix reconciles the donors: 19 candidates, 14 with positive weight, and the minimum attainable rank p of 0.05.
9. **PubMed as a comparator.** *Partly done.* Limitations note journal-side changes such as PLOS ONE's pre-screen for Mendelian randomisation studies (April 2024). Publication lags are not modelled.
10. **Equivalence test for H3.** *Partly done.* No margin was set in advance, so "similar" is defined as no detectable difference, with the size of differences the 2024 intervals allow (about 20% in physics, 40% in biology).
11. **The marker regression is confounded.** *Done.* It has server-specific year effects and the H1-predicted sign (negative) stated in advance. It is called ecological, and its arXiv part (seven clusters) descriptive. The interaction came out positive (0.0041; p = 0.034).
12. **Relabel "confirmatory".** *Done* ("pre-specified", defined in Methods).
13. **Fig 3 legend and monthly shares.** *Moot.* Fig 3 now shows quarterly measures and decompositions.
14. **The cap and future physics series.** *Done* (Limitations: the cap breaks the continuity of arXiv series, and any extension must model it).
15. **Data availability with the JSON files and model scripts.** *Done* (submission-form block).

### Analyses requested (§5)

1. **Planned estimand and specification table.** *Partly done* (Table 1); the model estimate is pending.
2. **Structure-matched placebos.** *Pending.*
3. **Bioinformatics split by AI or machine-learning topic.** *Pending.*
4. **US against non-US for the wet-lab slowdown.** *Pending* (the PubMed version is done).
5. **H2 decomposition, null and 2019 histories.** *Done*, except the simulation null (declined).
6. **Preregistered out-of-sample test of C2 and C3.**
   - A 2027 test is *not registered*.
   - A different pre-registration is active and *pending*. It tests paper-level hypotheses on held-out archives and on bioRxiv and medRxiv, including a dose–response across categories.
7. **January–August sensitivity.** *Partly done* (synthetic control; mathematics decomposition); the rest is pending.
8. **Rambachan–Roth.** *Declined.*
9. **Synthetic control with clean donors.** *Pending.*

R1's list of analyses to drop is followed:
- Benjamini–Hochberg on falsification tests: dropped.
- Central-trimmed break tests: replaced.
- The marker regression: rebuilt with server effects.
- Trend-adjusted estimates: sensitivity only.
- MDEs at 5% alone: α/3 added.
- No new grouping is presented as primary.
- No subfield search in mathematics.

### Section 7 (reframing)

- **7.1–7.3.** *Done.* H1–H3 are kept as recorded and the outcome is reported plainly. H2 is reported as a described distribution with a decomposition, and H3 rests on measured markers, with no claim of equivalence.
- **7.4. Title.** *Done.* A working title without a causal verb or "1.9 million"; R1's options are listed in the comment under it.
- **7.5. Abstract.** *Done* along R1's sketch. Every deletion was made. All additions were made, with the decomposition in place of the fixed-threshold share.
- **7.6. Discussion and Conclusions.** *Done.*
  - "Why might arXiv differ from bioRxiv?" lists candidate explanations without choosing among them.
  - The medicine "limiting case" and "needs no misuse" are gone.
  - Implications are kept short and labelled (author's decision; Section 3).
  - Limitations add every item R1 listed.
- **7.7. Further analyses.** The analyses added after the results were seen are labelled as such in Methods and Results and are reported whatever they showed:
  - gr-qc removed;
  - Snowmass and European Strategy papers removed;
  - genres;
  - the INSPIRE classification.

  None replaces a pre-specified estimate.

---

## 6. Reviewer 2 (scientometrics and preprint data)

### Major issues

**R2-M1. The confirmatory tests do not support H1; reframe.**
- **Retitle; lead with the negative results.** *Done* (title, abstract, Results, Conclusions).
- **Placebos for inference.** *Done.* The placebo p is reported beside the Holm p.
- **Base year.** *Done.* 2019, pooled bases (2017–2019 and 2019+2022) and a 2022 base cleaned of Snowmass papers are in Table 1. The event-study panel is in the main text (Fig 2D).
- **Withdraw two findings.** *Done.* "AI is in the writing but not yet in the volume" and "experimental science is less affected" are gone. Blekhman's argument is motivation only.
- **Report the hint honestly.** *Done.* nucl-ex (1.00) and the physics archive (1.06) are named as the archives that did not accelerate. The paper-level INSPIRE analysis then shows that, within experiment, papers reporting new results grew as fast as the rest.

**R2-M2. arXiv papers are dated by announcement.**
- **Date by submission; re-run timing.** *Pending* [dating by first-version submission]. The companion found that OAI `created` is the latest version's date, so first-version dates come from the arXiv API.
- **Headline windows.** *Done.* January–September comparisons lead; third quarters are used only for the author-level decomposition, with July–August and January–August variants.
- **Reconcile the two arXiv sources.** *Partly done.* Annual hep-th and hep-ph counts from the harvest match arXiv's statistics for 2019–2025. The January 2025 boundary no longer enters any comparison, because the mathematics harvest now starts in 2019.
- **Ask arXiv for moderation statistics.** *Author* (optional).
- **Holds and the cap.** *Done* (Discussion, explanation i, with [RECHECK] against arXiv's post).

**R2-M3. Count definitions differ between sources and from Nee et al.**
- **One record, one primary category; remove duplicates from N.** *Done.* N is no longer used, and the aliasing (archive sums about 5% above arXiv's total) is stated.
- **Both definitions.** *Done.* New submissions and list entries are both reported (physics 1.24, mathematics 1.43 on list entries; mathematics ranks second of 18 on entries and fifth on new submissions).
- **Replicate Nee et al. before comparing.** *Partly done.*
  - The synthetic control is replicated (11.9%), with its excess about 8% without September.
  - On January–August windows, the share of names with five or more papers rose from 2.34% to 3.73%, against their 2.45% to 3.80%.
  - An exact replication of their panel is declined (Section 3).
- **Name the unit.** *Done.* The Introduction says "list entries".

**R2-M4. The bioRxiv contrast is confounded.**
- **Remove COVID-19 record by record.** *Pending.*
- **Classify papers by content.** *Pending* (pre-registered amendment 1, Test A on bioRxiv, validated against the author's blind coding).
- **Set AI-topic papers apart.** *Pending* [bioinformatics split by AI/ML topic].
- **Normalise by journal output.** *Declined* (Section 3).
- **Category-level permutation as the main inference.** *Pending* [structure-matched placebos]. The 462 wet-lab halvings are already the primary inference for C2.
- **Gates Foundation mandate; the 2020 screening of COVID-19 repurposing papers; the move to openRxiv.** *Not examined*, apart from duplicates. medRxiv's API lists some version-1 preprints twice; those are now removed, and bioRxiv is being checked for the same problem [RECHECK].

**R2-M5. The medRxiv filter and flag are unvalidated.**
- **Validate both flags; title-only bound.**
  - Validation: *pending*, with a coding sheet prepared.
  - Title-only bound: *done*. C3 is 1.07 (0.95–1.21), and the third-quarter 2026 index is 241 against 257. Growth from 2025 to 2026 is 15.6% against 16.4%.
- **Extended dataset list.** *Done.* Adding FinnGen, CHARLS, CDC WONDER and TriNetX gives C3 1.05 (0.93–1.17). The time the original list was fixed is still to be stated [AUTHOR].
- **Journal version of C3.** *Declined* (Section 3).
- **Genre contrast within medRxiv.** *Pending* through the pre-registered medRxiv test, which classifies new primary data against secondary analyses and reviews.
- **medRxiv may be the wrong place.** *Done.* C3 is called a weak test in this venue (Results).

**R2-M6. H2 cannot yet separate breadth from namesakes, newcomers, batch posting and a few submitters.**
- **Long histories; "established"; decomposition for mathematics.** *Done.*
  - Histories from 2019.
  - A variant for names active in 2019–2024.
  - Concentration shares for mathematics: the top 1%'s share rose from 5.15% to 6.84%, 1.77 points above trend.
  - "Established" dropped as a claim.
- **Namesake error.** *Partly done.* A namesake-robust variant, which describes a different population (Methods), gives the same pattern (top 1% +211%, bottom 90% +41%). The simulated null and an identifier-matched subsample are declined.
- **Batch posting.** *Declined for this version* (needs submission times).
- **Extensive and intensive margins.** *Done* in the decomposition by class.
- **Exclude collaboration papers in physics.** *Done* (more than 50 authors).
- **Q4 2026.** Not yet available.
- **The two accounts the Discussion had not met.** *Done.*
  - "Needs no misuse" is deleted.
  - arXiv's account of heavy submitters is in explanation (i).
  - The Discussion notes that Nee et al.'s panel shows rising concentration, as the decomposition here does.

**R2-M7. H3 argued from rankings across studies.**
- **Rebuild H3 on the marker results.** *Done.* It leads with 2024, reports each group, and adds mathematics and the category panel; Table 6 is moved to S4 Table.
- **Liang et al.'s estimator.** *Declined* (Section 3). Their bioRxiv values carry [RECHECK] in S4 Table.
- **Abstract sentence.** *Done.* It now rests on the markers.
- **Reconcile micro and macro.** *Done* in Limitations, which name R2's three possibilities: overestimated adopter gains [Renault et al.], gains confined to few authors, or output published elsewhere. The study lacks author-level bioRxiv data to choose among them.

**R2-M8. Server policies and the social-science series.**
- **Dated timeline.** *Done.* S2 Appendix lists server policies, facility schedules, planning exercises and funding events, with sources. Rule indicators in the models are declined.
- **Validate the OSF method.** *Pending* [OSF continuity check].
- **Demote the social-science series.** *Done.* It is shown for reference only, its trend is flagged and not interpreted, and SocArXiv's per-author limit is noted.

**R2-M9. Positioning and literature.**
- **Positioning.** *Done.* The article is framed as a within-field falsification test of the computational-intensity account of Qi et al., and as a replication and extension of Nee et al. on a different count unit.
- **Core literature.** *Done.* Abdill and Blekhman; Sever et al.; Krumholz et al.; Fraser et al.; Larivière et al.; Wang, Chen and Glänzel; Ioannidis et al. (2018, 2024); Milojević; Kim and Diesner; Bornmann et al.; Filimonovic et al.; Abadie et al.; Driscoll and Kraay. Metadata were read from Crossref or arXiv.
- **Reliance on a six-week-old preprint.** *Done.* The paper rests on its own replication. The arXiv spelling of Nee's given name is flagged in the header note.
- **Discussion material not tested by these data.** *Partly declined* (Section 3).
- **The three RECHECK markers R2 resolved.** *Used.*

**R2-M10. Data availability, reproducibility and terms of use.**
- **Record-level identifiers and flags.** *Pending* [record-level identifier and flag tables].
- **Pinned environment.** *Pending* [software versions and a pinned environment].
- **Raw retrievals and an OAI snapshot.** *Partly done.* The deposit README lists the raw files and retrieval dates; a frozen OAI snapshot is not yet included.
- **Request limits.** *Done.*
  - Methods states the rates actually used, including the two that exceeded documented limits.
  - The scripts now comply.
  - INSPIRE's rate carries [RECHECK].
- **Names only with data-protection approval.** *Author.*
- **Licences.** *Author* (CC BY 4.0 and MIT suggested).

### Minor issues

1. **Title.** *Done.*
2. **"Dated by announcement".** *Done* (Methods).
3. **hep-lat as a third arm.** *Declined* (Section 3).
4. **v1 Table 2 growth columns.** *Done.* Replaced by departures from trend.
5. **v1 Table 3 footnote (+34% against +28%).** *Superseded.* After the duplicate correction, non-COVID medRxiv growth is 20.9% in 2025 and 16.4% in 2026.
6. **Model-release markers.** *Done* (removed).
7. **Two name normalisations.** *Done.* One pipeline (heavy_producers.json); S3 Table is rebuilt from it.
8. **Precision of mention patterns.** *Moot* for AI, Lean and Erdős (no longer used); pending for the medRxiv flags.
9. **`\b` before covid.** *Not done* (Section 3).
10. **Which arXiv count is which.** *Done.* "Submissions of all kinds" in the Introduction; new submissions by primary archive in Methods.
11. **Retrieval dates.** *Done* (Methods).
12. **Terminology.** *Done.* A heavy producer has about 20 papers a year, far below the thresholds for extreme output.
13. **References and Spick's datasets.** *Done*, except one detail. Kusumegi et al.'s issue number is added, and the overlap with Spick et al.'s nine datasets is listed in S2 Appendix. The text presents Renault et al. as a critique of Kusumegi et al.'s design, but the reference does not label it as a comment [AUTHOR: confirm its article type in PNAS].
14. **"Fixed before growth was examined".** *Done* (Methods, Study design): the groups were defined before their growth was computed, but the hypotheses and the choice of primary contrasts were recorded when descriptive growth was known.
15. **Partial October 2026.** *Declined* (Section 3).
16. **medRxiv's early months.** *Done.* Its trend reflects adoption and is not interpreted.

### Analyses requested (§5)

1. **Re-date by submission.** *Pending.*
2. **Genre and topic breakdown.** *Done* for genres in mathematics and the six particle and nuclear physics archives: research articles alone departed as much or more. The AI topic remains pending for bioinformatics. cond-mat, astro-ph and quant-ph are held back for the pre-registered test.
3. **Who drives the growth.** *Partly done* (decomposition; 2019 histories; Nee-comparable windows). Identifiers, country and an exact Nee replication are declined.
4. **Propensity to post against production.** *Declined for this version.* Named as untested in the Discussion.
5. **Classify papers by content; split hep-ex and astro-ph by team size.**
   - Classification: *pending* in the pre-registered tests.
   - INSPIRE classes and team size for the particle and nuclear archives: *done* (exploratory).
6. **bioRxiv without COVID-19; permutation inference.** *Pending.*
7. **Policy event study.** *Declined* (Section 3).
8. **medRxiv flags.** *Partly done* (title-only and extended list); validation pending.
9. **Servers with similar cultures.** *Declined* (Section 3).
10. **Extend the marker analysis.** *Done* (2024 as the main year; mathematics added; category panel). Liang et al.'s estimator is declined.
11. **Thinness and later outcomes.** *Declined* (Section 3).
12. **Out-of-sample test.** *Not registered* (Section 3). The active pre-registration is the registered test.

### Section 7 (addendum)

- **7.1–7.2. The pattern and its candidate explanations.** *Done.* The Discussion takes up R2's table.
  - Explanations checked: genres; planning cycles (R2's cycles within fields).
  - Explanations open, with pending checks: dating and holds; funding; facility cycles; AI-enabled production.
  - Explanations named as untested: platform rules; propensity to post; who posts.
  - The model artefacts R2 lists are reported:
    - archives with falling trends have the largest departures (Table 3 note);
    - the synthetic control measures an excess over an accelerating arXiv.
- **7.3. Positioning against Nee et al., Qi et al., Kusumegi et al. and Renault et al.** *Done* as R2 proposed. The weaker evaluation point ("counts are not comparable across fields, servers or years, whatever the cause") is the one the Implications section makes.

---

## 7. Reviewer 3 (experimental physics and biology)

### Section 2a (reading after the formal results)

- **What the paper can honestly claim about experimental work.** *Done* along R3's suggested wording, with three updates from the new analyses:
  - Removing Snowmass and European Strategy papers raises hep-ex's 2026 departure from trend to 1.58 (1.38–1.82).
  - Within particle physics, experiment grew at least as much as theory (hep-ph/hep-ex 0.88; hep-th/hep-ex 0.87).
  - In the exploratory INSPIRE classification, papers reporting new experimental results grew as fast as the rest within hep-ex and nucl-ex (1.00, 0.74–1.35). Small-team papers (1.55) and papers with more than 300 authors (1.42) stood above trend, while those with 11–300 authors fell (0.64).
- **"New data at the margin" as a hypothesis, not a finding.** *Done.* The refined hypothesis is stated as formed after seeing the data. It is tested on held-out archives and servers under an active pre-registration, and the results are pending.
- **Two cautions now in the Discussion.**
  - The INSPIRE rule counts collaboration analyses of data collected before 2023 as new results, so it does not isolate papers that need new data at the margin.
  - nucl-ex's flatness predates 2023.
- **Sentences that should not survive revision.** *Done.* Both are removed.

### Major issues

**R3-M1. The central claim is not supported.**
- **H1 not supported, with ratios and negative controls in the abstract.** *Done.*
- **Negative controls central.** *Done* (Table 1; Results).
- **Archive-level permutation.** *Pending* [structure-matched placebos, including all 4-against-2 draws of the physics archives].
- **The new-data refinement as a hypothesis with a pre-registered test.** *Done* (Methods; Discussion).
- **Retitle, avoiding "eroding".** *Done.*

**R3-M2. The physics groups are not "theory" and "experiment".**
- **(a) gr-qc.** *Done* as a correction made after the results were seen: without gr-qc, C1 is 1.10, 1.02 on the cleaned base and 1.03 against 2017–2019. The pre-specified estimate is reported first.
- **(b) hep-ph.** The label is kept, which is *declined* (Section 3). The Discussion says hep-ph is phenomenology fitted to data, and hep-ph/hep-ex is reported (0.97; 0.88 on the cleaned base).
- **(c) Archive scopes.** *Done* (Discussion; S2 Appendix names physics.ins-det and physics.data-an).
- **(d) The experimental group is small and lumpy.** *Done.* The MDE is 1.21 (1.25 at α/3). The INSPIRE breakdown by team size shows the lumpiness.
- **(e) hep-lat.** *Author:* reason to be stated.
- **Fixes not taken: groups by paper type; separate contrasts; a methods series; a cond-mat classifier.**
  - Paper-level groups: *pending* in the pre-registered tests.
  - nucl-th/nucl-ex: *not done*.
  - The physics.ins-det and physics.data-an series: *declined* (Section 3).
  - The cond-mat classifier: *pending*, as a pre-registered held-out test.
- **INSPIRE.** *Done.* It is the exploratory component.

**R3-M3. The 2022 reference year and the range criterion favour H1.**
- **Snowmass.** *Done.* Removing Snowmass and European Strategy papers gives C1 1.06 (0.89–1.25), close to R3's crude 1.02–1.04. Snowmass made up 16.4% of hep-ex's January–September 2022 papers, and European Strategy inputs 5.4% of its 2025 papers.
- **Conference papers.** *Partly done.* The genre split removes proceedings, reviews, theses and white papers for the departures from trend (experiment, research articles only: 1.08, against 0.97 for all papers). C1 was not re-estimated without proceedings.
- **Range language.** *Done* (dropped).
- **A primary base excluding 2020–2022.** *Declined as primary* (Section 3). Reported in Table 1.
- **All bases in one table.** *Done* (Table 1).

**R3-M4. The biology contrast is a bioinformatics effect, tested at the wrong level.**
- **Category-level inference.** *Pending* (permutation over category assignments). The mixed model is declined.
- **Bioinformatics with and without AI or machine-learning topics.** *Pending.*
- **Category-choice drift; full text.** *Declined for this version* (Section 3).
- **COVID-19 flags in every month.** *Pending.*
- **Dose–response against measured experimental intensity.** *Pending.* Part of the pre-registered amendment: a dose–response across categories of all three servers, with intensity measured as the share of papers reporting new data.

**R3-M5. The medicine flag does not measure "existing data".**
- **Hand-code flagged and unflagged abstracts.** *Pending.* A coding sheet is prepared.
- **Expanded list fixed in advance.** *Done* as a sensitivity analysis with Spick et al.'s four missing datasets (1.05). It was fixed after the original results, not before.
- **Registered trials; PubMed replication; health informatics.** *Declined for this version* (Section 3).
- **Report the null as evidence against the existing-data arm in this venue.** *Done* in Results ("a weak test of H1 … in this venue"). The published formulaic literature is cited only as the reason for the flag, not as support.

**R3-M6. Alternative explanations get one sentence or none.**
- *Done* in the Discussion, "Why might arXiv differ from bioRxiv?". Every alternative R3 dated is named with its status:
  - **Checked:** planning cycles; genres.
  - **Open, with a pending check or stated as untested:** funding; facility schedules; announcement and holds; who posts and the propensity to post; AI-enabled production.
  - **In S2 Appendix:** the dates of the funding events, LHC Run 3 and LS3, RHIC's final run, the LVK O4 run and GWTC-4.0, Snowmass and the European Strategy.
  - **Not mentioned:** instrument-time allocation.
  - **AI as a topic:** pending for bioinformatics.

**R3-M7. The mechanism is stated too strongly and makes no quantitative prediction.**
- *Done.* The Limitations state the Amdahl-type bound with R3's illustrative values (8% and 54%) and derive two predictions:
  - larger gains for types of paper with a larger compressible share, which the pre-registered dose–response tests;
  - shorter lags from data to paper in experimental work even where counts are flat (not tested).
- "Experiments cost what they did" is gone.

**R3-M8. H3 is not measured in the contrasted groups.**
- **Markers for exactly the contrasted groups.** *Done* (Table 2: theory, experiment, computational, wet lab, medRxiv, mathematics). Markers by type of paper within hep-ex were not computed.
- **Revise the abstract sentence.** *Done.*
- **Discuss Kobak et al.'s computational finding.** *Done.* Computational categories started higher, as in Kobak et al., but rose by a similar factor.
- **H3's role now that H1 fails.** *Done.* H3's surviving content is that writing adoption is ubiquitous and does not track output. Mathematics, with the smallest rise, had the largest acceleration.

**R3-M9. The Discussion is not fair to experimental fields.**
- **"Later onset".** *Done.* It is replaced by testable predictions (Limitations), and facility cycles are named as confounders (Discussion iii). No horizon is set, because no test of later onset is registered.
- **Laboratory automation; "bioRxiv mostly experimental"; "experimental physics within its range".** *Done.* All three are removed.

**R3-M10. The evaluation and policy sections do not follow from the evidence.**
- *Partly declined* (Section 3). D2 is reduced to an interpretation-labelled paragraph on what counts can and cannot mean. D3 is condensed to one paragraph of untested proposals. Table 1 is S1 Table. The Matthew-effect rhetoric and "needs no misuse" are gone.

**R3-M11. The statistical plan in the manuscript is not the one that was run.**
- *Done.* There is a Deviations section, listing each element R3 tabulated. Estimates under the original specification are approximate in Table 1, and the model estimate is pending [planned specification]. Every other analysis is labelled exploratory.

### Minor issues

1. **Range language in the abstract.** *Done* (removed).
2. **"Biology on a par with physics".** *Done* (removed; H3 now rests on the markers).
3. **hep-ph against hep-ex.** *Done* (Results; Table 1 note).
4. **arXiv q-bio.** *Done* (Results).
5. **bioRxiv's position in 2026.** *Done.* No departure from trend (0.91, 0.71–1.15).
6. **Counting the failures.** *Done:* "two failed and the third is fragile" (Limitations).
7. **COVID-19 check too narrow.** *Pending.*
8. **Fig 2's experimental index rests on an inflated 2022 base.** *Done* in Results (Snowmass share and the cleaned base). The figure itself is unchanged.
9. **Experimental range excluding 2020–2022.** *Moot.* Range comparisons are dropped.
10. **Underpowered physics test.** *Done* (MDE in the abstract, Results and Limitations).
11. **medRxiv excludes the cheapest genres too.** *Done* (Discussion cites both servers' scope).
12. **Explain hep-lat.** *Author.*
13. **Name the physics subcategories.** *Done* (S2 Appendix).
14. **Reconcile the physics field series.** *Done* (13 archives, listed in S2 Appendix).
15. **INSPIRE author identifiers; fractional counting.** *Partly done.* Fractional counting is done; INSPIRE identifiers are declined for this version.
16. **Lean and Erdős.** *Done* (removed).
17. **Single-company marker.** *Done* (removed).
18. **Say in one place that the contrasts were chosen after the counts were seen and that two failed.** *Done* (Limitations).

### Analyses requested (§5)

1. **Clean the reference period; report pairs of archives.** *Done* (Snowmass removed; hep-ph/hep-ex and hep-th/hep-ex; archive departures in the Table 3 note). Conference papers are handled only through the genre split.
2. **Break down hep-ex and nucl-ex by mode of production.** *Partly done.* Done in the INSPIRE exploratory analysis: by author count (≤10, 11–300, >300) and document type (S5 Table), and by INSPIRE class. Counts by named collaboration, and double-coded classification of the small-team segment, are not done.
3. **A pre-registered paper-level test.** *Pending* (active pre-registration with two recorded deviations).
4. **Category-level inference for C2, with AI topic separated.** *Pending.*
5. **bioRxiv by the corresponding author's country.** *Pending.*
6. **Lags from data to paper.** *Declined for this version.* Stated as a prediction.
7. **Within-person contrasts with INSPIRE identifiers.** *Declined for this version.*
8. **C3 in PubMed.** *Declined for this version.*
9. **AI as a topic in every group.** *Partly pending* (bioinformatics). Not done for the theory archives or for health informatics.

---

## 8. Reviewer 4 (PLOS ONE Academic Editor)

### Section 3 (reframing for criterion 4)

- **3.1. What the results show.** *Reflected throughout.* The surviving finding is reported as exploratory and between servers, with its confound stated in the same paragraph. The caveat that hep-ex is largely analysis of data already collected is in the Discussion.
- **3.2. Framing points 1–6.** *Done.*
  - Lead with the question and the answer.
  - All three contrasts wherever results are summarised (abstract, Results, Discussion, Conclusions).
  - "Inconclusive" or "null", with MDEs.
  - No exploratory result promoted, and every analysis tried listed in S5 Table, including those dropped.
  - Deviations reported.
  - The essay's thesis cited once in the Introduction and once, scoped, in the Discussion.
- **3.3. Title.** *Done.* A working title that names the pre-specified tests and their result without a causal verb, with R4's three options listed. Short title: "Preprint output in the generative-AI era" [AUTHOR: choose].
- **3.4. Abstract.** *Done* on R4's model (298 words). The mathematics sentence is replaced by the decomposition, and the paper-level and marker results are added.
- **3.5. H1.** *Declined* to rewrite (Section 3). The tested statement and the clause-by-analysis mapping follow the hypotheses. "Later onset" is a prediction in Limitations.
- **3.6. Results.**
  - *Done:* headings as proposed; the contrasts table as the central display, with every row R4 listed; event-study coefficients plotted for C1–C3 (Fig 2D); the arXiv-wide finding reported as exploratory with its confound.
  - *Partly done:* the planned specification is approximate, with the model estimate pending.
- **3.7. Discussion.** *Done* in R4's structure: principal findings; why the contrasts are inconclusive or fragile; candidate explanations for the arXiv-wide acceleration; implications, labelled; limitations. It runs to about 1,500 words rather than 1,100, because of the author's Implications section and the new results. All four deletions R4 listed are made.
- **3.8. Conclusions.** *Done* on R4's model, updated with the new results.
- **3.9. A 2027 test.** *Not mentioned.* No registration exists (Section 3).

### Major issues

**R4-Major 1. Title.** *Done.*

**R4-Major 2. The abstract reports selectively.**
1. **The premise stated as fact.** *Done.* AI "can lower the cost of writing"; the cost premise is now a conditional prediction.
2. **Claim of uneven cost.** *Done* (removed).
3. **Range comparison.** *Done* (removed).
4. **Inconvenient results.** *Done.* All contrasts are given. On medicine: growth slowed from 20.9% in 2025 to 16.4% in 2026 after the duplicate correction (Results).
5. **"Biology on a par with physics".** *Done* (removed).
6. **Monthly end points.** *Done* (third quarters and January–August windows).
7. **"Without any misuse".** *Done* (removed).
8. **Word limit.** *Done* (298 words).

**R4-Major 3. How the H1 results are reported.**
- **Range criterion.** *Done* (removed).
- **The paper's own falsification rule.** *Done.* Negative controls and placebo percentiles are reported, and the reading follows from them.
- **Headings and conclusions.** *Done* (rewritten).
- **R4's suggested physics sentence.** *Used*, with the cleaned-base result added.

**R4-Major 4. The statistical plan.**
- **(a) Deviations.** *Done* (Methods, Deviations, as R4's model paragraph); the planned estimate is pending. [AUTHOR: reasons for the change of reference year.]
- **(b) "Confirmatory".** *Done* ("pre-specified", defined in place).
- **(c) Break tests.** *Done.* 5% trimming with the admissible window stated; fixed-date tests; "no break in 2026" deleted; Andrews (1993) cited for sup-Wald. The Andrews (2003) test is declined (Section 3).
- **(d) Placebo dates are descriptive.** *Done* (S5 Table). The year-shock calibration replaces them in the main text.
- **(e) Negative controls.** *Done* (placebo shares; no adjustment).
- **(f) Few units.** *Done.* The in-space placebos are the primary inference.

**R4-Major 5. H2.**
1. **H2 not defined operationally.** *Done* in Methods. The measures are the top-1% and top-10% shares and the decomposition by class; H2's wording is kept (Section 3).
2. **"Established" unsupported.** *Done.* Dropped as a claim; a sensitivity analysis is restricted to names active in 2019–2024.
3. **Mechanical rise of the per-paper share; report the decomposition.** *Done.* The decomposition is the H2 result. In mathematics the bottom 90% contributed 52% of the increase, and the top 1% grew fastest.
4. **Wilson intervals and z-tests.** *Done* (removed; shares are descriptive).
5. **Namesake variants exclude many slots.** *Done* (Methods: "describes a different population").
6. **AI-mention expression.** *Done* (no longer used; removed from S2 Appendix).
7. **Fig 3D (Erdős).** *Done* (removed; Fig 3 rebuilt).
8. **Mention rates against misuse.** *Done* (deleted).
9. **Two pipelines.** *Done* (one pipeline).
10. **Aligned windows with Nee et al.** *Done* (January–August windows).

**R4-Major 6. H3 not tested; populations crossed.** *Done.*
- The companion's marker analysis is the H3 result, with its limits: PubMed-derived words, drift after 2024, sampling of bioRxiv months, and an ecological panel.
- Table 6 is S4 Table.
- Liang et al.'s bioRxiv series is flagged [RECHECK], and so is whether Lin and Zhu's figures are relative or percentage-point increases.
- The point that mathematics cuts against the writing measure is now a finding: smallest marker rise, largest acceleration.

**R4-Major 7. D2 and D3.**
- *Partly declined* (Section 3: the author's decision to keep a short Implications section).
- R4's sentence-by-sentence actions:
  - "needs no misuse": deleted;
  - "cost has fallen unevenly": deleted;
  - effort made invisible: recast as one sentence labelled as interpretation;
  - rationing: R4's two descriptive sentences, with S1 Table;
  - Matthew effect: deleted;
  - recommendations: condensed into one paragraph of untested proposals, to be introduced as evaluated experiments;
  - speculation about AI lowering the cost of reading: deleted.
- DORA/CoARA: the approved wording is kept, with R4's caveats (measurements predating CoARA; "broad and growing") and R4's own suggested sentence on reading capacity.

**R4-Major 8. "Consistent with".** *Done.* It is used once, in the Implications section, in a sentence labelled as interpretation. The Discussion lists the alternatives and states that the design does not choose among them.

**R4-Major 9. Overlap with the companion essays.** *Author.* Listed in the header note:
- the EMBO Reports figures;
- a preprint of this article;
- disclosure of related manuscripts with copies;
- a DOI for the companion essay;
- aligned competing-interest statements.

**R4-Major 10. Ethics.** *Done* on R4's model.
- Personal data, pseudonymisation and no names reported.
- Cells below ten authors suppressed.
- Risks declared.
- Terms of use.
- [AUTHOR: data-protection office consultation (UPF/EMBL), lawful basis, safeguards; whether to release a pseudonymised author table.]

**R4-Major 11. Data availability.** *Partly done.*
- The statement covers the minimal data set R4 lists, and the deposit README documents sources, terms and request rates.
- Pending: record-level identifier and flag tables; a pinned environment.
- [AUTHOR: Zenodo DOI; licences; non-author contact if the author table is withheld.]

**R4-Major 12. AI disclosure and S1 Appendix.**
- *Done:* tools named; uses and the parts affected; ideas the author originated (H1; the refined hypothesis; the INSPIRE component) against AI proposals adopted or modified (analysis plan, group definitions, specification, candidate recommendations); a clause in every legend.
- S1 Appendix is rebuilt as R4 proposed: a task table with human role and checks, a timeline with commit times, and slots for code review, reading depth and costs. Essay material and internal to-do lists are removed.
- *Author:* model and version; the author's own validation.

**R4-Major 13. Competing interests.** *Done.*
- The model-release marker is removed from figures and text.
- R4's wording is used, in the submission-form block outside the manuscript.
- [AUTHOR: who paid; any credits from Anthropic.]

### Minor issues

**Format and structure**

1. **Legends and tables placement.** *Done* (after the first-citing paragraph; checked by the build script).
2. **Form statements.** *Done* (separate block).
3. **SI as separate files.** *Done* (marked in v2).
4. **Remove HTML comments and markers.** *Author*, before submission.
5. **Short title; e-mail and ORCID; EMBL affiliation.** *Partly done.* The short title is proposed; the rest is [AUTHOR].
6. **Length.** *Partly declined* (Section 3).

**Methods and data**

7. **arXiv statistics URL; cite OAI-PMH, OSF API and PubMed with access dates.** *Partly done.*
   - The arXiv statistics pages, API terms, robots.txt, OSF terms and INSPIRE API are cited.
   - PubMed's E-utilities are named, without a reference [AUTHOR: add the NCBI documentation].
   - Retrieval dates are given.
8. **Harvest dates and coverage.** *Done.*
9. **Group definitions.** *Done.* The classification caveats are in Methods and Discussion. The fixation time of the medRxiv list, and a timestamp for "fixed before growth was examined", are [AUTHOR] or described in Study design.
10. **Synthetic control donors.** *Done* (19 candidates, 14 weights; minimum attainable p of 0.05 stated).
11. **AI as topic.** *Pending.*
12. **arXiv q-bio.** *Partly done.* Discussed in Results; the substitution test is not done.
13. **Social sciences.** *Done.* SocArXiv's limit is noted, and the series is for reference only.
14. **medRxiv RECHECK figures.** *Superseded.* The figures change with the duplicate correction and are reported from the corrected series.

**Introduction**

15. **"Main" responses.** *Done* ("Several").
16. **"Not tested with data".** *Done.* The claim is gone; the article is framed as a falsification test.
17. **Hanson et al.** *Done* (what they measured: indexed articles).
18. **The gap statement.** *Done.* The Introduction says what this study adds: within-field contrasts, a replication of Nee et al. on a different unit, and decompositions by author class.
19. **Quotations.** *Done.* The main text paraphrases.

**Results and language**

20. **Redundancy.** *Partly done.* Legends describe the figures, and repeated caveats are cut. Some numbers recur between abstract, Results and Conclusions by design.
21. **Terminology.** *Done.* "Author names" and "heavy producer" are defined; "new preprints (first versions)" is used.
22. **"9.5–13%".** *Done* ("9–13%").
23. **Conclusions.** *Done.*

**Figures**

24. **Format and fonts.** *Partly done.* TIFF files exist. The fonts are Liberation Sans, metric-compatible with Arial; the figures are to be re-rendered with Arial. Panel labels are upper-case.
25. **Fig 2 event-study panel including C3.** *Done* (Fig 2D).
26. **Log-scaled axes.** Requested of the companion.
27. **Fig 3.** *Done.* Rebuilt with concentration shares and decompositions for mathematics and physics theory; panel D (Erdős) is gone.
28. **AI clause in legends.** *Done.*

**Tables**

29. **v1 Table 1.** *Done.* Moved to S1 Table, with the thesis-detector and arXiv-ban rows removed and mentioned in its note.
30. **Counts and ranges.** *Partly done.* Counts are in Table 1; ranges go into S2 Table, which is still to be assembled.
31. **v1 Table 5.** *Done.* Cells under ten authors are suppressed (S3 Table).
32. **v1 Table 6.** *Done* (S4 Table).

**References**

33–34. **Fixes.** *Done* for every reference still cited:
- Blekhman's final version;
- Kusumegi et al. without the note;
- Singh Chawla as a Nature news item;
- one URL each;
- methods references added and verified;
- Rice et al.'s volume.

References no longer cited are dropped: Cowgill et al.; Hao et al.; Cancellario et al.; Gorelick et al.; the bioRxiv statistics pages. The companion essay's DOI is [AUTHOR].

35. **Reliance on preprints and news.** *Partly done.*
- Social-media sources are gone.
- The claims that rest on the preprints of Nee et al., Qi et al., Lin and Zhu, Holzwarth et al., and He and Bu are hedged.
- The list has 70 references, not 35–40, because R1, R2 and R4 asked for methods references and the scientometric literature.

**Other**

36. **AI reviews are not peer review.** *Done.*
37. **STROBE-style checklist.** *Optional* [AUTHOR].

### Compliance checklist (§6)

| Item | Status |
|---|---|
| Criterion 4 | Addressed by the reframing |
| Criterion 3 | Addressed: deviations declared, break tests able to see 2025–2026, power stated |
| Criterion 6: ethics | Statement written; officer consultation is [AUTHOR] |
| Criterion 7: minimal data | Statement covers it; deposit and record-level tables pending |
| Licences | [AUTHOR] |
| AI validation by the user | [AUTHOR] |
| AI disclosure in legends | Done |
| Competing interests in the form | Done; payment [AUTHOR] |
| Funding | [AUTHOR] |
| Third-party sources acknowledged | Done, except a PubMed E-utilities reference |
| Related manuscripts | [AUTHOR] |
| Short title | Proposed |
| Corresponding author's e-mail and ORCID | [AUTHOR] |
| Abstract ≤ 300 words | Done (298) |
| Legends and tables after first citation | Done |
| Figure fonts | Arial re-render pending |
| SI separate files | Done |
| References | Done; companion essay DOI [AUTHOR] |
| Data-source terms | Stated, with two past exceedances disclosed and INSPIRE [RECHECK] |
| Plan timestamped; deviations reported | Done |

---

## 9. Remaining weaknesses, as the reviewers would see them

1. **No exposure measure, and server-level confounding.** The surviving pattern lies between servers, and the design cannot attribute it. Two explanations were ruled out (genres; planning papers). Announcement dating, funding, facility cycles and AI-enabled production remain open, and the data on posting propensity and author populations are not examined.
2. **Underpowered, label-based contrasts.** C1 cannot detect ratios below about 1.21, and every contrast rests on one archive or category. The test that would answer the refined question is pending: paper-level classification in held-out archives and servers, by a classifier validated against the author's coding. Its two deviations mean that confirmatory status depends on that validation.
3. **Dependence on AI, and on corrections found late.**
   - The code, the text and the internal reviews were produced by AI agents. The author's own validation is not yet recorded.
   - The medRxiv duplicates were found late and bioRxiv is unchecked. One Table 1 cell for C3 (slope change) is not yet recomputed, and another (year-shock ratio) was recomputed here, not by the companion.
   - The regular expressions and genre keywords are unvalidated, and the INSPIRE classes have not been spot-checked by a person.
