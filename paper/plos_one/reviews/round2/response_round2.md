# Response to the round-2 internal reviews (R1–R4)

- **What this is.** The author's response to the second round of internal review, drafted on 17 October 2026 by an AI agent from the four reviews (`paper/plos_one/reviews/round2/`) and the v3 source. The author is to adopt or amend it [AUTHOR: approve or amend each response]. The reviews were written by AI agents in reviewer roles; they are not peer review.
- **Version answered:** draft v2 (commit a17a8b9). **Version that answers:** draft v3, `paper/plos_one/build/draft_v3_keyed.md`. The brief named commit cc24781; the source was checked at commit d97668a, which includes three later commits: 934267f (INSPIRE paragraph), 27edcd6 (SI tables, bioRxiv record table) and d97668a (second coder; the author's statement on the 00:12 line).
- **Numbers** are copied from the v3 source or the reviews; none was recomputed. [CHECK: …] marks a point that could not be verified from v3.
- **Blinding.** No result of HN, Test A or Test B appears here. No sealed file or other branch was opened.
- **Locations** are section headings of v3. "Registration" is Deviation 3 and its four addenda in the registration files (commits 8932773, 80a2ef2, 6e1c119, 0a49bb7 and 868ef0a); D-labels follow S6 Table.
- **Status codes.** *Done*; *Partly done*; *Pending* (analysis not yet delivered); *Author* (needs the author); *Declined*; *Moot* (the text concerned is gone).

---

## Summary of changes

1. **H1 primary estimate.** The planned specification is now primary (negative binomial after the planned overdispersion check, multi-year base, calendar-month and period effects, Driscoll–Kraay errors): 2026 rate ratios 1.05 (0.93–1.18), 1.02 (0.94–1.11) and 1.05 (0.98–1.13); Holm p 0.83, 0.83, 0.56. The 2022-based estimates (1.14, 1.08, 1.01) are reported as a deviation. The planned model was computed only in review, after those were known; Methods and S6 Table say so.
2. **Calibration.** The v2 year-shock statistic is withdrawn. Rank calibration with the same estimator, and structure-matched placebos, replace it.
3. **H2.** Classes are ranked on an independent window, a uniform-scaling simulation is added, and the verdict is stated: partly supported.
4. **Marker (H3).** Withdrawn entirely (decision A2); a note in Methods keeps the record.
5. **Framing.** The abstract and Introduction follow decision A1; one paragraph engages Blekhman (A3).
6. **Data checks.** Dating by first-version submission; bioRxiv record-level check; genre flags against INSPIRE types; AI-topic split of C2; bioRxiv funding split; INSPIRE analysis rewritten. The social-science series is removed, PubMed is cut to one sentence, Qi et al. are repositioned.
7. **Paper-level tests.** Deviation 3 and its addenda were recorded before any estimate they govern; estimates are sealed; Methods, a Results shell with [SEALED] placeholders and S6 Table are in. No result appears.
8. **Sentences** that went beyond the data are corrected.
9. **Deposit.** Pinned environment, `run_all.sh`, corrected disclosures; S2 Table, S5 Table and the bioRxiv record table assembled.
10. **Not done.** The author's blind coding, the second coder's coding, model and version, data-protection consultation, title, essay revision, data-vintage analysis, within-person contrasts, and smaller items below. The main text is 6,524 prose words, against R4's 5,700–6,000.

---

## 1. Reviewer 1 (statistics and causal inference)

### New major issues

**R1-N1. In-time calibration is mis-specified; acceleration estimates have none.** *Done, with two gaps.*
- The v2 year-shock ratio is withdrawn (S5 Table note). Calibration is by rank with the identical estimator: the 2026 coefficient among the contrast's earlier year coefficients, and the 2026/2025 change among all earlier year-on-year changes. Two-sided, 2026 included, so p cannot fall below 1/(n + 1) (Methods, Calibration; Table 1; S5 Table).
- Rank p of the 2026 coefficient: 0.67, 0.80, 0.60. Of the 2026/2025 change: 0.73, 0.29, 0.29. C2's and C3's equal-sized rises are read alike (Results). R1 allowed rank or a centred z; rank was used.
- Gaps: slope changes keep bootstrap p values only. Fig 2D's legend describes Driscoll–Kraay bars and no rank p; the figure was not checked. [CHECK: Fig 2D.]

**R1-N2. The cross-server divergence depends on the counterfactual; only mathematics stands out; the experimental-archive claim depends on archive and window; bioRxiv duplicates.** *Done.*
- Each claim names its counterfactual. Results note that bioRxiv's 12% trend was fitted to years of adoption; the Discussion says the contrast "depends on the counterfactual".
- Direct comparison with bioRxiv (Results), 2025 to 2026: C1's six archives +7% (1.07; 0.99–1.16), "as much as in 2021 and 2022"; experiment 1.02 (0.93–1.11); mathematics 1.27 (1.04–1.56), its largest gain (rank p 0.14 one-sided, the floor; 0.29 two-sided).
- The experimental-archive claim is limited to hep-ex (1.37; 1.12–1.67), "but not nucl-ex (1.00)", in Results, Principal findings and Conclusions; the abstract has no such clause. The genre window is in S2 Appendix.
- A record-level bioRxiv harvest found 313,161 unique version-1 DOIs from 313,165 listings; monthly counts equal the official totals in 89 of 93 months and are one lower in four (S2 Appendix). No number changed; the [RECHECK] is gone.

**R1-N3. "Use vs output" is suggestive, not robust.** *Moot.* The marker analysis was withdrawn on the author's decision (A2). v2's Fig 4 and Table 2, the H3 Methods and Results, and every marker sentence in the abstract, Discussion and Conclusions are gone, so R1's five problems and the corpus-specific check no longer apply. Methods (Deviations) records the pre-specified marker, the test run and the withdrawal after the results were known, with the author's reason. Results stay in the deposit; S4 Table stays as literature context. [AUTHOR: R4 and R2-N2 advise against dropping a pre-specified test unreported; see §5 item 3.]

**R1-N4. H2: what the symmetric decomposition can and cannot say.** *Done.*
- Names are also ranked on an independent window (July 2024–June 2025). Mathematics, third quarters 2025 to 2026: total +80%; previous top 1% +40%, next 9% +76%, bottom 90% +68%. Names not active in the ranking year supplied half of the increase; names entering the top 1% supplied 13%, names already in it 1%. Physics theory: previous top 1% +2% against +26% (Results, H2; S5 Table).
- Uniform-scaling simulation (lognormal rate pool): uniform growth raises the top-1% share by 0.98 percentage points (SD 0.15), 58% of the observed rise (39% in January–August). The null over-predicts active names (60% against 41%); the shares are labelled descriptive.
- Verdict stated: "H2 is therefore partly supported". The abstract drops "more than tripled". R1 asked for a window robust to September; the abstract still quotes third quarters, but January–August points the same way (+27% against +33%, S5 Table).

**R1-N5. Funding checks: PubMed over-read; medRxiv split unreported.** *Done for PubMed and bioRxiv; Pending (analysis session) for medRxiv.*
- PubMed is one sentence: the query misses about a quarter of articles from large US institutions, at a drifting rate, and 2026 is not unusual (rank p = 0.20). "No comparable decline" and the "about 1.7 of the roughly 7 percentage points" accounting are deleted.
- The bioRxiv split ran against a prediction stated first (Discussion): US wet-lab preprints did not fall relative to non-US ones (2026 against 2023–2024: 1.01; 0.96–1.07). The country classifier is unvalidated.
- R1's medRxiv split (US +17.7%, non-US +10.1% in 2026) is now in the Discussion: US preprints on medRxiv rose relative to non-US ones (2026 against 2023–2024: 1.12; 1.06–1.17).

**R1-N6. The pre-registered tests: design, implementation, deviations.** *Mostly done; four points open.* All recorded before any HN, Test A (bioRxiv) or Test B estimate (Registration; S6 Table B).
- Test A rule: supported if the ratio exceeds 1 and its 95% CI excludes 1 (D3b). Test B's primary set: 15 held-out arXiv subcategories plus the bioRxiv and medRxiv categories; mathematics and the six particle and nuclear archives are sensitivity only (D3d). One-sided p stated (D3c). All registered sensitivity analyses coded before the HN estimate (D3o).
- Level-based companion estimates against pooled bases sit beside each trend-based one; disagreement is reported as dependence on the counterfactual (D3e). R1's 2023–2024 base is not in the registration.
- Blind random-order runs replace date-ordered batches (D3a); test–retest disagreement is propagated (D3g); remaining estimates are sealed (D3i); κ with CIs by domain and period, confusion matrices, corrected ratios and a secondary Holm adjustment are reported (D3h); the "can revise" clause is replaced (D3j); the bootstrap identification error is fixed (D3q); an erratum corrects "classified by one person".
- A second human coder is registered (D3r; Methods; Limitations; S6 Table): a colleague codes a stratified random 100 of the 400 papers. The sheet is built; the coding is not done.
- Open: no non-US sensitivity analysis; no rule for what a failed κ in one domain means for Test B (Deviation 1 covers each domain's results only); no hash of the model identifier; no OSF or Zenodo registration, only GitHub push times [AUTHOR]. D3q (third addendum) is missing from S6 Table, and the S1 Text caption lists two of the four addenda.

**R1-N7. Sentences beyond, or short of, the evidence.** *Done.* All 16 rows handled; three marker rows are Moot.
- Abstract: INSPIRE and genre sentences removed; "more than tripled" replaced; placebo result given in words. "Falsification test" is now "test"; "pre-specified estimate relative to 2022" is now "estimates first reported, a deviation"; C3's bound reads "under within-period uncertainty only, excludes increases of more than 13%".
- The PubMed sentence and "This supports" are deleted; "Four findings withstood" is now "Two descriptive findings held under the checks made"; Conclusions say "(hep-ex) included but not nucl-ex" and "without adjustment".

**Corrections to the round-1 response (R1 §1.3).** Two statements did not match v2. In v3 the minimum detectable effects are in Results and Table 1, not the abstract, and Results call C1 "inconclusive rather than null".

### Requested analyses (§6)

1. Fix and seal the registered tests: *Partly done* (N6).
2. bioRxiv duplicate check: *Done* (N2).
3. Dating by submission; January–August versions: *Done* for the contrasts and H2 (S5 Table: C1 1.10, 0.99–1.23; C2 1.08, 1.02–1.14; C3 1.01); C1 is 1.15 by either dating. January–August departures from trend are not in the text. [CHECK: S5 spreadsheet.]
4. Rank calibration for every headline comparison: *Partly done* (N1).
5. H2 independent window and simulation: *Done* (N4).
6. Marker sensitivity by field: *Moot*.
7. Structure-matched placebos: *Done*. C1 against 15 four-against-two splits (floor 0.067) and 25,740 draws; C2 against 455 assignments.
8. Funding: *Partly done* (N5). PubMed pre-trends were not added because the check was cut.
9. For the record: planned specification *Done*; link completeness by year *Done*; validation of the Snowmass keyword rule against INSPIRE's tags is not in the text. [CHECK: S5 spreadsheet.]
- Lower priority: AI/ML split of bioinformatics *Done* (0.95; 0.90–1.02). COVID-19 removal from bioRxiv categories dropped; the Fig 2 legend and Limitations say they are included.

### Minor issues (§5)

1. *Done* in v3 (C3 2026/2025 1.10; slope change −3.8%, p 0.27). Regenerating the committed companion files: *Pending (analysis session)*. [CHECK: not verifiable here.]
2. *Done.* The 0.70 placebo p is attached to the 2022-base estimate, 1.10.
3. *Done.* "Pre-specified" now means the contrasts and the planned specification.
4. *Not done.* "At most nine percentage points" is unqualified in Results; S5 Table labels the pairs "all names".
5. *Done.* The range sentence is gone; S5 Table lists every variant.
6. *Done.* "Lower bound" in Methods and Table 1.
7. *Declined.* Methods say "No placebo was defined for C3"; no reason is recorded.
8–9. *Done.* Methods name the comments field for arXiv; S2 Appendix gives the transform.
10. *Not done.* No archive rank p is reported.
11. *Done.* "No detectable slope break".
12. *Not done* in Results. The pooled-base interval (0.80–1.22) is in Table 1 but is not set against 1.03–1.14.
13. *Partly.* INSPIRE was redone across four base periods; Methods does not name the estimator. [CHECK: with R3-N1.]
14. *Partly.* Rank p is in Table 1, not Fig 2D. [CHECK: Fig 2D.]
15. *Done.* S6 Table rows 5–7.

---

## 2. Reviewer 2 (scientometrics and preprint data)

### New major issues

**R2-N1. The genre split is not valid as built; the abstract overreaches.** *Partly done.*
- The abstract has no genre clause. Results: papers not flagged as proceedings, white papers, theses or reviews departed from trend as much as all papers in C1's six archives (1.24–1.28 under three keyword rules, against 1.20) and in mathematics (1.69–1.71 against 1.69), whereas in the two experimental archives neither series departed much (1.07–1.11 and 1.01).
- Against INSPIRE's curated types, the proceedings flag has precision 0.89–0.97 and recall 0.63–0.87; the review flag is "unreliable" (precision 0.04–0.57); genre shares by year are "not comparable", because metadata mature as papers are revised (Results; S2 Appendix).
- S2 Appendix adds a revised rule (journal names ignored; "review" only in titles or explicit phrases), a title-only rule as the revision sensitivity, and proceedings shares for revised and unrevised papers. The two six-archive sets are named "C1's six archives" and "INSPIRE's six archives". The stale header notes and the abstract comment were corrected after this draft.
- Not done: hand-coding 200 mathematics papers; mathematics genres stay unvalidated [AUTHOR, if wanted].

**R2-N2. H3's within-field comparison depends on the metric.** *Moot* (marker withdrawn; R1-N3).

**R2-N3. INSPIRE classes depend on curation that changes with record age.** *Done, updated at 934267f; two checks open.*
- Results depend on the base period and on proceedings: 1.03–1.05 including proceedings; for research articles without planning papers, 1.19–1.27 in the six archives (four base periods, every lower bound at least 1.00), 2.12–3.69 in hep-ex and 0.84–1.20 in nucl-ex.
- The link share fell from 0.55–0.68 before 2025 to 0.47–0.49 in 2025–2026, "mostly through composition": records with more than 300 authors carried a collaboration in 99–100% of cases in every year, and only mid-size collaborations show a possible lag, about 0.1 in 2026. Requiring a collaboration instead of a link (R2's sensitivity) gives 2.04 in hep-ex.
- Reading: "consistent with the refined hypothesis in hep-ex, the archive in which it was formed, but not in nucl-ex ... not a held-out test".
- Pending (analysis session, in about three months): a re-harvest to measure lag. Author: the 100-record spot-check. The text does not say that the experimental category follows arXiv categories.

**R2-N4. The PubMed US-affiliation check.** *Done* (R1-N5). It is called "uninformative"; it was not redone with validated countries.

**R2-N5. Snowmass removal: asymmetric cleaning, trend leverage.** *Partly done.* The Discussion now says removal "did not reduce hep-ex's departure"; the cleaned value (1.58) is no longer reported. Not done in the text: other trend windows, the asymmetry caveat.

**R2-N6. List-entry checks.** *Done.* Like-for-like author panel: names with five or more papers 2.80% to 4.07%, against Nee et al.'s 2.45% to 3.80% (Results, H2; S3 Table). Cross-lists are 67–69% of hep-ex and nucl-ex entries.

**R2-N7. bioRxiv duplicates.** *Done; two parts not done.* See R1-N2. medRxiv duplicates are described (below 0.5% until late 2025, rising in 2026, most in July–August); the DOI prefix change and the onset of duplicates are in the dated events. Not done: duplicates under different DOIs on either server; the uniform `type` value.

**R2-N8. Dating by first-version submission.** *Done.* INSPIRE-HEP hep-ex +13.7% by submission against +14.2% by announcement, 2025 to 2026; C1 1.15 either way. Mathematics, September 2026: 8,360 new papers against 5,903 in August; 8,167 submitted in September; 3.0% submitted more than a week before it (0.6% in 2025): "a spike in submissions rather than a release of held papers". First half of October under the cap: 4,030 against 1,836 (2.2 times; lower bounds). Not done: batch posting by heavy producers.

**R2-N9. OSF series.** *Done.* Removed from Fig 1 and Table 2. S2 Appendix says OSF counts were retrieved, at a rate above the documented one, for a series the article does not report. The README correction is the companion's.

**R2-N10. Other integrity issues.** *Done in v3.* Two mathematics series defined (89.9% in 2019, 92.3% in 2026; growth +43.2% and +43.3%); revision censoring stated; corrected C3 values used. Regenerating `round1_tests.json` and `results.md`: *Pending (analysis session)*. [CHECK: not verifiable here.]

**R2-N11. Positioning against Qi et al.** *Done.* The Introduction says Qi et al. measured the share of papers mentioning AI by discipline, and the acceleration of submissions. The Discussion: their finding "concerns the share of papers mentioning AI, not the volume of output, so these contrasts neither corroborate nor refute it"; their bioRxiv acceleration is a recovery. Blekhman is credited for the idea tested. The AI-topic split is done. Pruller et al. has its DOI; Renault et al.'s critique left with Kusumegi's output-gain estimate (A1). Not added: R2's six references. The exact reading of Qi et al.'s Table IV (below the pre-2020 slope, or below the slope before their first, 2020, intervention) is flagged for the author with a [RECHECK] marker in v3.

**R2-N12. Deposit, pipeline, disclosures.** *Partly done.*
- Methods (Software) pins the versions (Python 3.13.16; requirements.txt) and says `run_all.sh` reproduces the count-based outputs. Data availability says the author-level analyses need undeposited harvests with names, and gives the route to reproduce them. The analysis session reports that `run_all.sh` now calls `stats_round1.py` and that `round1_tests.json` and `results.md` were regenerated (companion commit 666be30).
- Record-level tables are listed for arXiv, medRxiv, INSPIRE and now bioRxiv. No heavy-producer flag is released. Pseudonymised table or non-author contact, and the governing framework (EMBL Policy 68 or GDPR): [AUTHOR].
- S2 Appendix now states the 429 answer, the two to four parallel connections, INSPIRE's limit and CC0 terms, and that OSF's figure comes from the osfr documentation. The coding sheet lists DOIs and links only (934267f). Licences: [AUTHOR: confirm].

### Requested checks (§6)

1. Dating: *Done* (N8).
2. Genre claim: *Partly done* (N1).
3. Marker metric: *Moot*.
4. bioRxiv duplicates: *Done*; different-DOI matching not done.
5. INSPIRE diagnostics: *Partly done*. Link shares by year and the collaboration-only variant done; re-harvest *Pending* (analysis session); spot-check *Author*.
6. C2 items: AI-topic split and matched placebos *Done*; bioRxiv without COVID-19 *Declined* (R1 rated it lower priority and unable to change the verdict).
7. medRxiv flags: coding the sheet *Author*; recall sample dropped.
8. Batch posting *Not done*; October *Done*.
9. PubMed with validated countries: *Declined*; the check is no longer used as evidence.
10. Deposit: *Partly done* (N12).
- "Corrections that need no new analysis" (genre sentence, H2 headline, Qi et al., Nee et al. panel, PubMed, C3 slope cell, social sciences, disclosures): *Done*.

### Minor issues (§5)

1. *Done.* The abstract no longer quotes the physics 1.06.
2. *Done.* Results note the falling pre-2023 trends.
3. *Done* (R1-N4).
4. *Done.* S5 Table lists the namesake-robust July–August variant.
5–6. *Moot.*
7. *Partly.* The Fig 1 legend gives each series' third-quarter index and warns about indexing to 2022; no 2.39-fold sentence.
8. *Done.* Methods: latest-version metadata; INSPIRE dated by first-version submission.
9. *Done.* openRxiv, the arXiv post, the prefix change and the medRxiv duplicates are in the dated events.
10. *Done.* The motivating count is called unvalidated.
11. *Partly.* Retrieval dates are in S2 Appendix; the classification samples' dates are not.
12. *Moot.*
13. *Partly.* The cross-list share is in Results, not in the Discussion sentence.
14. *Author.* Precision coding; the recall sample was dropped.
15. *Author.* Spot-check of the country classifier.
16. *Done.* S2 Appendix gives query and dates.
17–19. *Done* (A1; the API statement stands; the build header counts markers).

---

## 3. Reviewer 3 (experimental physics and biology)

### New major issues

**R3-N1. The INSPIRE result is overstated; the Discussion contradicts itself.** *Done, updated at 934267f.*
- The abstract and Conclusions no longer say papers reporting new results "grew as fast as the rest". The Discussion's "did not support its refinement" and "which the held-out tests classify directly" are deleted.
- Results (R2-N3) give the dependence on base period and proceedings. The Discussion adds that the rule counts collaboration analyses of stored data as new results.
- The independent-fit interval (0.74–1.35) and the team-size ratios are not quoted; S6 Table lists the four rule variants as unregistered.
- Results now say that the INSPIRE ratios use the stacked estimator of C1 as first reported, and that planning papers are flagged from arXiv comments as well as INSPIRE's own flag.

**R3-N2. The team-size pattern is mostly an artefact.** *Done by removal; one gap.* Team-size estimates are gone. S2 Appendix says INSPIRE author counts of 0 mark lists not yet loaded, and labels the motivating count (187 to 366) unvalidated. Data-supply facts (LHC 124 fb⁻¹, LHCb 9.56 fb⁻¹, BESIII 2022–2024) are in the dated events; Discussion (i) says the rise "may reflect data supply, which this study did not model". The three-mode description is not written out. Counts by data vintage and lags: *Author* (R3 §6 item 3).

**R3-N3. Codebook validity: "data obtained by the authors", not "new data needed".** *Partly done.*
- Prompts unchanged, as advised; the Discussion says the codebook classes data by who obtained them.
- Registered before any HN or Test B estimate: HN without astro-ph and leave-one-archive-out (D3l); astro-ph without papers naming DESI, Euclid, Rubin or LSST (D3l); AI and machine-learning terms excluded for HN, Test A and Test B (D3m).
- Not registered: the human-coded provenance attribute; ND against NN among papers with at most 10 authors (R3: the frames carry no author counts); expected bias directions; comments stripped of dates; Gaia and GWTC in the astro-ph exclusion. Later additions count as post hoc unless recorded before the relevant estimate (D3j).

**R3-N4. The planned validation would not convince an experimentalist.** *Partly done.*
- Done (R1-N6): sealing; κ by domain and period, confusion matrices, corrected ratios, licence check; blind runs; test–retest relabelling, the 200 arXiv validation papers classified twice (D3a, D3g–D3i). A second human coder for 100 papers is registered (D3r) and described in Methods and Limitations; not yet coded. Limitations name the single coder, label noise outside the intervals, the licence-restricted frame and the proprietary classifier.
- Not done: a validation sample redrawn from the estimation sample by estimation period; a tipping-point analysis; the unclassifiable share by period; κ by archive.

**R3-N5. Test B is not a good test of the mechanism.** *Partly done.* The primary arXiv arm is held-out subcategories only (D3d; R1-N6). The inclusion rule is recorded (150 eligible papers; 28 medRxiv categories enter, 23 are dropped) (D3k). One-sidedness stated (D3c). Not done: precision weighting; R3's two better tests (a gradient over paper types; data-release natural experiments). Test B's exposure is the share judged from abstracts to report new data, not the share depositing it.

**R3-N6. Implementation problems.** *Done* (Registration). Items 1–8: D3b; D3n; D3o (twice); D3a; Methods ("the bootstrap does not carry misclassification") with D3g; D3i and D3k; D3e.

**R3-N7. Inferences beyond the evidence.** *Done, with one conflict.* The Qi et al. sentence, "This supports", the DORA and CoARA figures and the comparability claim are rewritten or deleted. "Archives where the idea was not formed" is now true of HN only; Discussion (i) cites the data-supply facts. Conflict: R3 and R4 asked to move the proposals out; decision A3 asks for one paragraph with the author's own proposal, so it stays (§5 item 4).

**R3 §4.8. Fairness and the wording of H1.** *Done.* "So far" is not used. Principal findings follow R3's sentence: the second clause of H1 "does not describe the experimental particle-physics archive ... although nucl-ex did not; whether experimental work as such responded to AI cannot be determined from counts". No prospective test is registered.

### Requested analyses (§6)

1. Amendment before the validation coding: *Done* as Deviation 3 and addenda; items not adopted are in N3–N5.
2. Redo INSPIRE: *Done* (N1).
3. Collaboration output by data vintage, and lags: *Author* (not done).
4. bioRxiv US against non-US: *Done* (1.01; 0.96–1.07); classifier check [AUTHOR].
5. AI-topic flags in every NN class: *Partly done*. C2 done; HN, Test A and Test B have the sensitivity analysis (D3m), not yet reported.
6. Within-person contrasts with INSPIRE author identifiers: *Author* (personal data; consultation pending).
7. Structure-matched placebos: *Done*.

### Minor issues (§5)

1. *Done.* Conclusions: "(hep-ex) included but not nucl-ex".
2. *Done.* The team-size sentence is gone.
3. *Partly.* The prospect-variant range is not given; variants are listed as unregistered.
4. *Done.* The 0.74–1.35 interval is gone.
5. *Moot.*
6. *Done.* Discussion (i) and the dated events.
7. *Done.* DESI DR1 and Euclid Q1 (19 March 2025), Rubin DP1 (30 June 2025) and GWTC-4.0 are dated in S2 Appendix.
8. *Done.* S2 Appendix.
9. *Open.* See N1.
10. *Done.* Limitations: hep-ex cross-listing fell from September 2025 (about 25% against 40%); no announcement found.
11. *Done* in v3; the committed file is a companion item.
12. *Done.* INSPIRE's limit and CC0 terms cited.
13. *Partly.* Methods give 400 coded papers and Test B's scope; per-domain validation sizes (200, 100, 100) are not in the main text.
14. *Author.* Precision coding; recall dropped.
15. *Author.* Why hep-lat was left out.
16. *Not done.* No instrument-time sentence.
17. *Done.* See N5.
18. No action.

---

## 4. Reviewer 4 (PLOS ONE Academic Editor)

### New major issues

**R4-N1. Paper-level tests: report in full or remove; record changes first.** *Done in form; content sealed.*
- v3 takes R4's Option A in form: a Methods subsection (R4's model paragraph, updated), a Results shell with [SEALED] placeholders, one abstract sentence with placeholders, and S6 Table with R4's columns. S1 Text is re-captioned as the plan, time-stamped in the public repository, "not in a registry".
- D3a–D3f, the erratum and the sealing rule are recorded. "Held out" is kept for HN only. Methods now say the author stated, before coding, that they had not read the Test A (medRxiv) report (fourth addendum; S6 Table).
- Open: Option A or B depends on finishing the coding and unsealing before submission; otherwise use R4's Option B sentence (§5 item 6). Model and version, justification, training setting, run records and number classified: §5 item 11. D3q is missing from S6 Table, and the S1 Text caption lists two of four addenda. The abstract is at 299 words with its placeholders (limit 300).

**R4-N2. Two design problems to settle before any estimate.** *Done* (R1-N6: D3d, D3e). The 2019 placebo is reported, not interpreted, for bioRxiv and medRxiv (D3n).

**R4-N3. "Pre-specified" attached to an estimand not shown to be pre-specified.** *Done, except the title.* The planned specification is primary and Table 1 labels its rows "Planned". Methods: "estimates first reported, a deviation". Results: the all-three-fields rule was "added after the results". Methods say the specification was committed with the first estimates [AUTHOR: §5 item 8]. The title still says "pre-specified within-field tests" [AUTHOR: §5 item 1].

**R4-N4. Sentences beyond the data.** *Done, with two author decisions.* The 12 rows are corrected as in R1-N7, R2-N11 and R3-N7. The opening premise follows A1 ("polish served as a cue of quality"); the effort sentence now reads "form becomes a weaker cue of the quality of the work behind it; this is an interpretation, not a result of this study". The Amdahl paragraph, the DORA/CoARA claim and the seven proposals are cut. [AUTHOR: marker (R1-N3); A3 paragraph (R3-N7).]

**R4-N5. The companion essay contradicts the article and still shows the model marker.** *Pending (scheduled after v3).* v3 cites the essay only as the place the argument is developed; its reference needs a DOI (§5 item 18). The marker label naming the model is in six figure files in `paper/figures/`, outside this article.

**R4-N6. Length, density and structure.** *Partly done.* The main text is 6,524 prose words (6,459 at cc24781), against R4's 5,700–6,000. Moved to the Supporting Information: Table 1's acceleration, slope-change, trend-adjusted, negative-control and variant rows and the H2 decompositions (S5 Table, a spreadsheet); the inventories of checks (S2 Appendix); the deviations (S6 Table). Cut: Table 1 from 18 to 16 rows (R4: 10; the planned rows were added); Implications to 410 words (R4: about 180); the Amdahl paragraph. References: 61 (v2: 70; R4: 54). The overage comes from analyses the reviewers requested. [AUTHOR: §5 item 5; one cut is the INSPIRE paragraph, 273 words, to the Supporting Information.] The v3 header still says Table 1 was cut to 10 rows.

**R4-N7. Pending analyses.** *Done.* Run: planned specification, bioRxiv duplicates, C3 slope change, matched placebos, AI/ML split, dating, bioRxiv US/non-US. Dropped with their mentions: OSF continuity, synthetic-control variants, bioRxiv without COVID-19, medRxiv flag recall. No [ANALYSIS PENDING] marker remains.

### Work that remains (§7.2)

1. Deviation 3 in the registration files: *Done.*
2. Classification, sealing, κ, unsealing, write-up: *Pending* (analysis session; author's coding). Shells are written.
3. bioRxiv duplicate check: *Done.*
4. Planned specification and the two sentences: *Done.* Title: *Author.*
5. Sentence fixes; Implications: *Done.*
6. Record-level tables; versions: *Done*; paper-level data follow unsealing.
7. Arial and NAAS: *Author.* The figures use Liberation Sans; Arial cannot be installed in the analysis container.
8. Markers, SI files, S2 and S5 Tables: *Partly done.* Tables assembled; [AUTHOR] markers remain; the LaTeX build was not checked.
9. Essay: *Pending* (scheduled after v3).
10. Matched placebos, AI/ML split, C3 slope change, dating: *Done.*
11. Length cuts; references: *Partly done.* E-utilities cited; Pruller DOI added; JAMA and CRS [RECHECK] remain.
12. Checks on the licence-restricted frame: *Registered* (D3h); results sealed.
13. Re-harvest within limits; optional analyses: *Declined* (optional; the two exceedances are disclosed instead) or deleted.

### Minor issues (§5)

1. *Author.* v2's title kept; alternatives in a comment.
2. *Author.* E-mail, ORCID, EMBL unit.
3. *Done* for E-utilities and INSPIRE. Open: confirm that the INSPIRE fields used are unrestricted.
4. *Declined* (optional); the two exceedances are disclosed.
5. *Author.* hep-lat; date the medRxiv list was fixed.
6. *Done.* Methods: trend uncertainty, not sampling.
7. *Partly.* Comments are mentioned; the number classified is [AUTHOR: N].
8. *Partly.* Versions given; repository identifier is the Zenodo DOI [AUTHOR].
9. *Partly.* Classifier and validation are item (vi); sub-agent model, training setting and account type are [AUTHOR]. The country classifier is not listed, and S1 Appendix says it is unused, yet the Discussion uses its output.
10. *Done.*
11. *Done.* Placebo counts sit beside each p.
12. *Done.*
13–14. *Moot* (markers; PubMed accounting).
15. *Done.* The [RECHECK] is resolved; "held-out" is true of HN only.
16. *Done.* Limitations.
17. *Author.* See §7.2 item 7.
18. *Done.*
19. *Author.* Essay DOI.
20. *Moot.* The reference is no longer cited.
21. *Done.* DOI 10.1371/journal.pone.0337199.
22. *Partly.* openRxiv resolved; JAMA letter and CRS source are [RECHECK].
23. No action.
24. *Partly.* Plans, Deviations 1–3 with two addenda, erratum, codebooks and run instruction are listed; the third and fourth addenda are not.
25. *Partly.* Contents listed; DOI and author-table decision [AUTHOR].
26. *Author.*
27. *Done.* "Writing – original draft" stays unassigned.
28. *Partly.* Rows moved to S5 Table; the three H1 paragraphs remain dense.

---

## 5. Open items for the author

**Decisions on the text**
1. Title (R4 minor 1; N3): keep "tests", or "contrasts" and a plainer object.
2. Adopt or amend the reframed interpretation and Conclusions. The file is still marked "Not yet revised by the author".
3. Marker (A2): keep the withdrawal note, or add a 2024-only S Table with your reason as a limitation.
4. The A3 paragraph against R3's and R4's request to cut proposals.
5. Length: accept 6,524 words or cut (R4-N6).
6. Paper-level tests: Option A or B (R4-N1); an OSF or Zenodo copy of the plans, labelled as made after classification began; a PLOS Registered Report query (R3); a prospective test (R3 §4.8).
7. Optional: arXiv's endorsement rule as a gate in S1 Table; R2's six references (Malički, Kirkham, Ginsparg, Strotmann, Waltman, Gray); hand-coded mathematics genres.

**Gaps in the record**
8. Why hep-lat was left out; when the medRxiv dataset list was fixed; why and when the reference year changed, and whether any estimate had been seen; whether the logs show the specification preceded the first estimate; the origin of H2 and H3; your field description.
9. Confirm the Methods statement that you had not read the 00:12 status line (fourth addendum). The time and commit of your coding and of unsealing. Corrected times for the addenda (S6 Table note).

**Validation and AI statement**
10. The blind coding of 400 papers, with results sealed until it is committed. The colleague who codes 100 (D3r): name (an [AUTHOR] marker remains in the AI-use statement) and affiliation.
11. Model and version of the main sessions and of the classifier; dates; account type; training setting; who paid, and any credits; number classified; run records; why a proprietary model.
12. Your own validation: code reviewed, re-runs with commit hash, numbers recomputed, sources read, AI proposals rejected; the S1 Appendix fields (reading depth, time and cost).
13. Human checks: the 200-row medRxiv flag sheet, a 100-record INSPIRE spot-check, the 100-record country spot-check.
14. Analyses waiting for you: counts by data vintage and lags (R3 §6 item 3); within-person contrasts with INSPIRE author identifiers (R3 §6 item 6), which need the data-protection consultation.

**Compliance**
15. Data-protection consultation: office, framework (EMBL Policy 68 or GDPR), date, outcome, lawful basis. A pseudonymised author table or a non-author contact.
16. Zenodo deposit: DOI, licences (CC BY 4.0 or CC0; MIT), repository identifier. Re-run `plot_plos.py` with Arial and check with NAAS.
17. Funding and competing-interests statements, aligned with the essay. Name, e-mail, ORCID iD, EMBL unit. CRediT roles; acknowledgements.
18. Related manuscripts (R4-N5): revise the essay, decide on EMBO Reports and the Correspondence, mint the essay's DOI, post this preprint first, write the cover letter.
19. [RECHECK] items: Lin and Zhu (relative or percentage-point), Liang et al.'s bioRxiv series, the JAMA letter, the CRS source. Read each source cited for a number or quotation.

