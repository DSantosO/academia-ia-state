# Response to the round-1 internal reviews (R1–R4)

- **Manuscript.** Draft v2, 16 October 2026: `paper/plos_one/draft_v2.md`, built from `paper/plos_one/build/draft_v2_keyed.md` by `build/build_v2.py` (references in `build/refs_v2.py`).
- **Reviews.** R1 statistics; R2 scientometrics and preprint data; R3 experimental physics and biology; R4 PLOS ONE Academic Editor (`paper/plos_one/reviews/round1/`). All four were written by AI agents in reviewer roles. They are internal reviews before submission, not peer review, and the article does not describe them as peer review (R4 minor 36).
- **Prepared by** an AI agent (Claude, Anthropic, via Claude Code) from the author's decisions of 16 October 2026 (`paper/brief.md`) and the coordinator's messages. Not yet checked by the author [AUTHOR: approve or amend each response].
- **Sources of new numbers in v2.** The companion analysis only (`paper/plos_one/stats/`; companion commits 37b4b11, f5ab16e, 7ac5647 and 26ce2eb), plus R3's documented INSPIRE-HEP queries, reported as unvalidated. The pre-registration of the paper-level tests is in commits 763aa2b and 78890e5, with deviations in 11264ee and 1de63a9.
- **Locations** refer to section headings of v2. Line numbers in the reviews refer to v1.

**Status codes.**
- **Done**: changed in v2.
- **Partly done**: changed, but not fully as requested; the remainder is explained.
- **Pending**: an analysis not yet run. The label matches an `[ANALYSIS PENDING: …]` marker in v2.
- **Author**: needs the author's decision or information. Matches an `[AUTHOR: …]` marker in v2.
- **Declined**: not done, with the reason.

---

## 1. Main changes in v2

1. **Reframing (all reviewers).** H1–H3 are reproduced verbatim as recorded in the skeleton (commit 2cac071, 16 October 2026, 16:42 UTC). The pre-specified within-field tests are reported plainly as not supporting H1: the physics contrast is inconclusive and underpowered, the biology contrast fragile, and the medicine contrast null. Every estimate is reported with its 95% CI, Holm-adjusted p, Bonferroni (98.3%) interval, minimum detectable effect and in-space placebo p. The placebos are the primary inference.
2. **New title** ("Preprint output in the generative-AI era: pre-specified within-field tests find no robust evidence of an experimental bottleneck"). It is a working title. The reviewers' alternatives are listed in an HTML comment under it, with a 100-character short title [AUTHOR: choose].
3. **New abstract** (293 words). It reports all three contrasts with their intervals, the placebo results, the minimum detectable effect for physics and the dependence of biology on bioinformatics. It adds the marker result (H3), the exploratory departures from trend with their counterfactual named, the H2 decomposition for theoretical physics, and a closing sentence on what the data cannot show.
4. **Methods aligned with the analysis that was run** (`stats/methods.md`): PPML with month fixed effects and group-specific calendar-month effects; Driscoll–Kraay errors labelled as within-year only; Holm adjustment with Bonferroni intervals; placebo-based inference; minimum detectable effects at α = 0.05 and α/3. A section on **Deviations from the analysis plan** lists every change from v1's plan and gives the approximate estimates under the planned baselines. Another section states what "pre-specified" means here: fixed before any model was estimated, not before the data were seen.
5. **Round-1 analyses integrated** (companion commit 26ce2eb): pooled bases; year-shock calibration; acceleration (2026/2025) and slope changes; gr-qc and particle-physics variants of C1; list entries; break tests that admit breaks up to January 2026; the synthetic control in context; PubMed US against non-US articles; the medRxiv title-only COVID-19 filter; archive departures. Removing gr-qc from theory is reported beside the pre-specified C1 as a correction made after the results were seen.
6. **H2 rebuilt.** Shares of fractional output held by the top 1% and top 10%, and a decomposition of growth by author class ranked on combined output, which avoids regression to the mean. Pairs of years before ChatGPT's release serve as the chance benchmark. Growth in theoretical physics is described as "broad-based but concentrating". "Established" and the mechanical fixed-threshold reading are dropped. Mathematics is pending.
7. **H3 rebuilt on the companion's marker analysis** (Kobak et al.'s style words, filtered on baseline data). It leads with 2024 and states the drift of the words after 2024. Within-field and cross-server comparisons are reported, with a caveat on equivalence and the ecological category panel. Published estimates moved to S4 Table.
8. **Field-level divergence reported as exploratory**, with the counterfactual named (each series' own 2015–2022 trend). In levels bioRxiv grew more than the physics archives tested. The Discussion lists six candidate explanations, each with its pending check.
9. **Pre-registered paper-level tests** of the refined hypothesis, which originated with the author: described in Methods and Discussion, with both recorded deviations and no results. R3's INSPIRE-HEP observation in hep-ex appears as one exploratory Results paragraph that motivated them.
10. **Discussion rebuilt.** Principal findings; what the within-field tests show; why arXiv might differ from bioRxiv; a short "Implications for research evaluation" (about 520 words, labelled as interpretation); Limitations; Conclusions on R1's and R4's model. The rationing table (v1 Table 1) is now S1 Table. The seven recommendations are condensed into one paragraph of untested proposals.
11. **PLOS compliance.**
    - Ethics statement for third-party personal data.
    - Terms of use and request rates of every source, including two rates that exceeded documented limits.
    - Data availability statement covering the minimal data set.
    - AI-use disclosure per PLOS policy, including what the author originated and how outputs are to be validated.
    - An AI clause in every figure legend.
    - The competing-interests and funding statements moved to a "submission form" block outside the manuscript.
    - Legends and tables placed after the paragraph that first cites them.
    - S1 Appendix rewritten as an AI-use and verification record for this article only.
12. **References** corrected (R4 minor 34; R2 minor 13). Methods references added: Santos Silva and Tenreyro; Driscoll and Kraay; Holm; Andrews; Abadie et al.; Bertrand et al.; Conley and Taber; Lakens. The scientometric literature R2 verified is added. Data-source documentation is cited. Metadata of added references were read from Crossref or arXiv on 16 October 2026.
13. **Model-release marker removed** from all legends and from the competing-interests text (author's decision, 16 October). Only ChatGPT's release and arXiv's rule dates are marked. The committed Fig1 file still shows the marker, and the companion is re-exporting it.

## 2. Analyses still pending

Each label matches a marker in v2.

| Label in v2 | Requested by | What it decides |
|---|---|---|
| planned specification | R1 M1, analysis 1; R3 M11; R4 Major 4a | The estimate under v1's plan (period effects against 2017–2022 and 2019–2022, Bonferroni intervals). Approximate values (1.05, 1.02, 1.03) are in Table 1 |
| structure-matched placebos | R1 M2, analysis 2; R3 M1, M4a | Whether C2 survives placebos with its own structure: 455 choices of 3 of 15 categories; 4-against-2 draws of physics archives |
| bioinformatics split by AI/ML topic | R1 analysis 3; R3 M4, analysis 4; R4 minor 11 | AI as a topic or as a tool in C2 |
| US vs non-US split on bioRxiv | R1 M3, analysis 4; R3 analysis 5 | Funding shock or AI cost behind the 2026 wet-lab slowdown |
| bioRxiv categories without COVID-19 preprints | R1 M1, M3; R2 M4; R3 minor 7 | Symmetric treatment of COVID-19 in C2 |
| medRxiv flags (validation; extended list) | R1 minor 7; R2 M5; R3 M5 | Precision and recall of the C3 flag and the COVID-19 filter |
| dating by first-version submission, with January–August versions of every 2026 estimate | R2 M2, analysis 1; R1 M7, analysis 7 | Announcement throughput and the September 2026 spike |
| genre decomposition | R2 analysis 2, §7.2 | Whether arXiv's acceleration lies in genres bioRxiv and medRxiv do not take |
| Snowmass and European Strategy papers removed | R3 M3, analysis 1 | Whether 2022 inflates the experimental base |
| synthetic control with the OAI mathematics series, physics-only donors and math-ph excluded | R1 minor 8, analysis 9 | A cleaner replication of Nee et al. |
| maths H2 | R1 M8, analysis 5; R2 M6; R4 Major 5 | The H2 decomposition for mathematics |
| maths H3 markers | R2 M7; R4 Major 6 | Marker rise in mathematics |
| OSF continuity check | R2 M8 | Whether the social-science series is continuous across its change of counting method in 2025 |
| pre-registered test | R3 analysis 3; R2 M4, analysis 5; R1 analysis 6 (in part) | The paper-level test of the refined hypothesis on held-out material |
| INSPIRE | R3 analysis 2, M6 | Reproduction of the hep-ex observation, and the exploratory INSPIRE component |
| record-level identifier and flag tables for the deposit | R2 M10; R4 Major 11 | PLOS's minimal data set |
| software versions and a pinned environment | R2 M10 | Reproducibility |

## 3. Points declined or only partly followed

| Point | Decision and reason |
|---|---|
| Restate H1 "as tested" and delete its second clause (R4 §3.5); restate H2 operationally (R4 Major 5) | **Declined.** H1–H3 are kept verbatim, as recorded before modelling (R1 §7.3; the author's brief). Rewording them would blur what was pre-specified. The Introduction then states which clause each analysis tests; Methods gives the operational definitions. Results report the second clause of H1 as not supported in physics |
| Rambachan–Roth sensitivity (R1 M1, M3, analysis 8) | **Declined.** The pre-specified tests are already reported as not supporting H1. Sensitivity bounds can only widen the intervals, so they cannot change that reading. Dependence on the counterfactual is shown directly: base 2019, pooled bases, the planned baseline, the trend-adjusted variant, the year-shock calibration and the placebos (Table 1) |
| Fixed-b or small-sample critical values for Driscoll–Kraay intervals (R1 M2 fix 4) | **Declined.** The placebos are the primary inference. The Driscoll–Kraay intervals are labelled as within-year uncertainty and reported as secondary. Recomputing them would widen intervals already treated as too narrow, without changing any reading |
| End-of-sample instability test (Andrews 2003; R1 M7; R4 Major 4c) | **Declined.** Replaced by sup-Wald tests with 5% trimming, whose last admissible date is January 2026, and by fixed-date Wald tests. The text says that breaks found at the boundary may be later. Claims about timing rest on yearly departures from trend |
| Indicators for arXiv rule dates in the models (R2 M8 fix 1, analysis 7) | **Declined.** They are nearly collinear with 2026 (R1 M7). The text argues the direction of each rule instead: endorsement and language rules restrict entry. It also reports variants that drop November 2025 to February 2026 or end in October 2025 |
| 2017–2019 as primary or co-primary base; new groupings as primary analyses (R3 M2, M3; R2 minor 3) | **Declined as primary.** Changing the primary estimate or the groups after seeing estimates is the forking path R1 §7.7 warns against. The alternatives are reported alongside: base 2017–2019 and pooled bases; theory without gr-qc as a correction made after the results; hep-ph/hep-ex; hep-th/hep-ex; gr-qc/experiment. Not done: physics.ins-det and physics.data-an as an experimental-methods series, and hep-lat as a third arm. Classifying cond-mat papers is part of the pre-registered tests |
| Poisson mixed model with random slopes by category (R3 M4) | **Declined** in favour of the exact permutation over category assignments that R1 recommends [pending: structure-matched placebos]. The permutation needs no distributional assumptions |
| Classifier for drift in category choice; classification from full JATS text (R3 M4) | **Declined for this version.** The pre-registered tests classify papers from titles and abstracts. Full text is future work |
| Normalising categories by journal output; coverage ratios (R2 M4 fix 4, analysis 4) | **Declined for this version.** This needs a new source (OpenAlex) and a mapping of categories to journal subfields. Propensity to post is named in the Discussion as an untested explanation |
| A journal version of C3; a comparison with registered trials; C3 in PubMed (R2 M5 fix 3; R3 M5, analysis 8) | **Declined for this version.** It needs new data and new flags. C3 is reported as a weak test in this venue. The medRxiv arm of the pre-registered tests classifies new against no new primary data |
| Liang et al.'s distributional estimator (R2 M7 fix 2, analysis 10) | **Declined.** It would need a reimplementation and a reference corpus. Their published bioRxiv values are flagged for the author to read in S4 Table |
| Identifier-matched author subsample (OpenAlex, ORCID); country composition; exact replication of Nee et al.'s panel; batch posting (R2 M6, analysis 3) | **Declined for this version.** The text compares with Nee et al. qualitatively only and names their unit (list entries). Batch posting needs submission times; dating by submission is pending |
| Policy event study with first-time submitters; comparisons with ChemRxiv and EarthArXiv; thinness and later outcomes (R2 analyses 7, 9, 11) | **Declined for this version** (new data). The policy dates are listed in S2 Appendix |
| Lags from data to paper (R3 M7, analysis 6) | **Declined for this version.** Stated in Limitations as a testable prediction of the Amdahl-type bound |
| Within-person contrasts with INSPIRE author identifiers; physics heavy producers with INSPIRE identifiers (R3 analysis 7, minor 15) | **Declined for this version.** The exploratory INSPIRE component of the pre-registration classifies papers by metadata, not by author |
| Uniform-scaling simulation null for fixed-threshold counts (R1 M8 fix 2) | **Declined.** The fixed-threshold measure is now descriptive only (S3 Table). The decomposition on combined output has an analytic null, since every class grows at the total rate under proportional growth, and an empirical benchmark from pairs of years before ChatGPT's release |
| Cut the evaluation material to about 150 words (R3 M10) or to two sentences without DORA and CoARA (R4 Major 7) | **Partly declined.** The author asked for a short section that states the thesis at the strength the data allow. It is about 520 words, labelled as interpretation, with every claim scoped. The rationing table is in S1 Table. The recommendations are one paragraph of untested proposals, credited to their sources. The DORA/CoARA sentence uses wording the author approved and carries R4's caveats: the measurements predate CoARA, and the Commission's study found engagement "broad and growing" |
| Prospective re-test on 2027 data (R1 analysis 6; R2 analysis 12; R4 §3.9) | **Not mentioned.** No registration for 2027 data exists, and R4 asks that none be described before it does. The active pre-registration concerns paper-level tests on data already collected [AUTHOR: decide whether to register a 2027 test] |
| Length of about 5,000–5,500 words (R4 minor 6) | **Partly declined.** The main text is about 6,600 words, because Methods must now report deviations, terms of use, ethics, AI use and the pre-registered tests. PLOS ONE sets no limit |
| Figure changes: log axes and indexing to 2019 (R1 minor 3; R4 minor 26) | **Partly done.** Fig 2D shows the event-study coefficients on a log scale. The figure files belong to the companion; the other changes are requested of it. The Fig 1 legend states how indexing to 2022 biases the comparison |
| Rename the theory group "theory and phenomenology" (R3 M2b) | **Declined.** The pre-specified labels are kept. The Discussion says hep-ph is phenomenology fitted to data |
| STROBE-style checklist (R4 minor 37) | **Optional; not done** [AUTHOR: decide] |

## 4. Decisions and information needed from the author

- Title and short title.
- Why hep-lat was left out of C1; when the medRxiv dataset list was fixed; the reasons for, and timing of, the change of reference year; when the companion fixed its model specification relative to v1.
- Whether to keep Kusumegi et al.'s output-gain estimate (Introduction; Limitations).
- Data-protection consultation (UPF and EMBL): office, date, outcome, lawful basis and safeguards; whether to release a pseudonymised author table and, if not, a non-author contact for access.
- Zenodo DOI and licences (CC BY 4.0 for data; MIT for code, as suggested).
- AI disclosure: model and version; dates; account type; whether training on the author's data was switched off; the author's own validation (code review, re-runs, numbers recomputed, sources read in full); which AI proposals were adopted, modified or rejected; the origin of H2 and H3.
- The classifier's model and version for the pre-registered tests; an OSF Registries DOI, if registered.
- Funding; who paid for the AI tools; any credits from Anthropic; competing-interest statements aligned across venues.
- Related manuscripts (R4 Major 9): the EMBO Reports essay draft uses the same figures; post this article as a preprint; disclose the Zenodo essay and the Nature Correspondence with copies; mint the companion essay's DOI.
- Merge or confirm the shortlist of proposals in "Implications for research evaluation".
- Optional: ask arXiv for monthly moderation statistics (R2 M2 fix 5).
- Resolve every [RECHECK] before submission (quotations; figures from McKiernan et al., Rice et al., the Commission's study and Lin and Zhu; Liang et al.'s bioRxiv series; arXiv's post of 1 October 2026).

---
