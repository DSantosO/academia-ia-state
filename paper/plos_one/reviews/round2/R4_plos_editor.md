# Reviewer 4: PLOS ONE Academic Editor assessment (round 2)

- **Manuscript:** `paper/plos_one/draft_v2.md` (v2, commit a17a8b9, 16 Oct 2026, 23:39 UTC): "Preprint output in the generative-AI era: pre-specified within-field tests find no robust evidence of an experimental bottleneck".
- **Also read:**
  - my round-1 report and `reviews/round1/response_round1.md`;
  - `paper/brief.md` (latest sections), and the author's critique log `reviews/author_critique.md` (commit 015764e, 23:51 UTC, after v2);
  - `preregistration_new_data_test.md` and `preregistration_amendment1.md`, with Deviations 1 and 2;
  - on the companion branch `claude/happy-lovelace-wqek9b`:
    - the design, scripts and documentation of the paper-level tests up to commit 15df0b1 (19:28 UTC);
    - commit 8ab4d9d (23:43 UTC, after v2), read through the GitHub API;
  - `paper/plos_one/stats/` and the four figure files;
  - the essay drafts and figure files in `paper/`.
- **Reviewer:** an AI agent playing a PLOS ONE Academic Editor who also reviews. This is a simulated review before submission, not a PLOS review. PLOS forbids editors and reviewers to upload submissions to generative-AI tools, so this report must never be presented as, or used in place of, a PLOS review.
- **Date:** 17 October 2026. Line numbers refer to `draft_v2.md`.

**Policy pages consulted on 16 October 2026.** Short quotations are as the pages returned them that day; re-check them in the week of submission.
- Criteria for publication: https://journals.plos.org/plosone/s/criteria-for-publication
- AI tools and technologies: https://journals.plos.org/plosone/s/ethical-publishing-practice#loc-artificial-intelligence-tools-and-technologies
- Submission guidelines: https://journals.plos.org/plosone/s/submission-guidelines. Sections used:
  - personal data from third-party sources;
  - figure captions;
  - statistical reporting;
  - funding and competing interests;
  - supporting information;
  - references;
  - ORCID.
- Registered Reports: https://journals.plos.org/plosone/s/what-we-publish#loc-registered-reports
- Data availability: https://journals.plos.org/plosone/s/data-availability
- Materials, software and code sharing: https://journals.plos.org/plosone/s/materials-software-and-code-sharing
- Competing interests: https://journals.plos.org/plosone/s/competing-interests
- Figures: https://journals.plos.org/plosone/s/figures
- INSPIRE-HEP REST API documentation: https://github.com/inspirehep/rest-api-doc
- Not re-read this round (see round 1): recommended repositories; arXiv API terms; the bioRxiv and medRxiv API; OSF terms.

I found no PLOS ONE page on reporting a preregistration held outside its Registered Reports route. For deviations I therefore use the standard PLOS applies to Registered Reports ("adherence to the protocol and the appropriateness of any deviations") and two published guides:
- Willroth EC, Atherton OE. Best laid plans: a guide to reporting preregistration deviations. Adv Methods Pract Psychol Sci. 2024;7(1). doi:10.1177/25152459231213802
- Lakens D. When and how to deviate from a preregistration. Collabra Psychol. 2024;10(1):117094. doi:10.1525/collabra.117094

**Other evidence.**
- Commit times are from `git log`.
- Push times are from GitHub's repository activity log (`gh api repos/DSantosO/academia-ia-state/activity`), which records them on the server.
- The repository is public.
- Reference metadata were spot-checked in Crossref.
- My own computations are listed in the Appendix.

---

## 1. Summary

v2 answers the central objection of round 1. It reports, in the title, abstract, Results and Conclusions, that the three within-field contrasts fixed before modelling did not support H1:
- physics: inconclusive (1.14; 95% CI 1.00–1.30);
- biology: fragile (1.08; 1.03–1.14);
- medicine: null (1.01; 0.90–1.14).

It makes in-space placebos the primary inference. It labels the arXiv-wide acceleration as exploratory and names its confound in the same paragraph. H2 is rebuilt on measures that do not move under proportional growth. H3 rests on a marker measured in the same groups. The model-release marker is gone from the article's figures, and the ethics, data and AI statements now have the right structure. On its frame, v2 meets criterion 4.

What remains is mostly completion and compliance, plus a set of problems that are new in this round.

1. **The pre-registered paper-level tests are described but have no results** (line 172). Their record has moved on since v2 was written:
   - the first classifier runs were re-done blind;
   - the decision rule for Test A was corrected;
   - Test B's arXiv categories include mathematics and the two experimental archives that the plan reserved for exploratory use.

   None of this is yet recorded in the registration files. Part of the fix is time-critical: it must be recorded before anyone sees an estimate from the classified papers (N1, N2).
2. **"Pre-specified" is still attached to an estimand that the record does not show was pre-specified** (line 158 against line 168; N3).
3. **About a dozen sentences still go beyond the data.** Several now make the opposite error and treat an inconclusive null as an equality: "grew as fast as the rest"; "independently of AI-assisted writing" (N4).
4. **The companion essay drafts contradict the article and still show "Claude Opus 5"** in their figure files. The article cites the essay twice (N5).
5. **Every author-only item is still open:**
   - the model and version;
   - the author's own validation of AI outputs;
   - explicit adoption of the reframed conclusions;
   - the data-protection consultation;
   - who paid for the AI tools;
   - related manuscripts;
   - ORCID;
   - the deposit.
6. **The main text still carries 42 markers:** 21 [AUTHOR], 16 [ANALYSIS PENDING] and 5 [RECHECK].

## 2. Editorial assessment and recommendation

**Scope (criterion 1).** Original quantitative meta-research, in scope. The negative primary result is publishable: "In keeping with our mission to publish all valid research, we consider negative and null results" (criteria page).

**v2 as it stands: not submittable.** An editor would return it without review, because it has:
- unresolved markers;
- an empty AI-validation statement;
- no deposit;
- a Methods subsection on confirmatory tests whose results are absent.

None of this is a rejection on substance.

**With the P0 items in section 7 done: I would send it out**, to:
1. a scientometrician who knows arXiv and bioRxiv metadata;
2. a statistician or econometrician familiar with event studies with few units and with trend extrapolation;
3. if the paper-level tests are reported, a reviewer for measurement with LLM annotators: validation design, and misclassification that differs over time.

I would expect a major-revision decision from reviewers, which is normal at PLOS ONE, and a good chance of eventual acceptance.

**Criterion 4.** The frame is right. What remains are specific sentences (N4), not the thesis. The essay's argument still leaks in at two places:
- "Implications for research evaluation" (lines 317–323);
- the Introduction's premise (line 110).

Both are quick to fix, and the author's own critique log (A1) points the same way.

**The pre-registered tests: report them in full, or take them out.**
- *Option A (recommended).* Complete the validation and the tests, then report them in this article, whatever the result: a Methods subsection, a Results subsection, a deviations table and one abstract sentence. They are the sharpest test in the project. Measuring experimental dependence paper by paper is the right response to the label problem round 1 identified.
- *Option B.* Remove them, keeping one sentence and a link.
- *Not acceptable.* Submitting with confirmatory tests described but not reported.

Under either option, the changes in N1 and N2 must be recorded now. The deviations already recorded do not disqualify the tests. Unrecorded ones would.

**Recommendation: revise before submission.** No further reframing is needed. I would expect one more internal round, to check the paper-level tests and the author-only statements.

## 3. Round-1 issues: status

Status key:
- **Resolved**;
- **Largely resolved**: small fixes left;
- **Partly**: substantial work left;
- **Open (author)**: needs the author.

### 3.1 The items the coordinator asked me to check

| Round-1 issue | Status | Evidence in v2 | What remains |
|---|---|---|---|
| **Title** (Major 1; §3.3) | Largely resolved | Line 65: no causal verb, no unmeasured construct, no "1.9 million". 128 characters; short title 40 | (a) "pre-specified … tests" overstates: the contrasts were pre-specified, the estimand was not (N3). (b) "experimental bottleneck" is the paper's own jargon, and can be read as the wider claim that experiments are not a bottleneck. Options in minor 1. The author chooses |
| **Abstract** (Major 2; §3.4) | Largely resolved | Line 104: all three contrasts with CIs and Holm p; placebo p; the two decisive checks; "The prediction was not supported"; a closing limitation | (a) 302 words by a word-processor count; v2's header gives 298 because the build script drops the four "=" signs. (b) No room for the paper-level result. (c) Three overreaching phrases (N4). Model abstract in N4 |
| **H1 framing** (Major 3; §3.5) | Resolved as a reporting choice | Lines 122–126: H1–H3 verbatim as recorded, each clause mapped to the analysis that tests it. Neutral headings; Table 1 "Reading" row; Fig 2D includes C3 | I accept the response's reason for keeping the recorded wording. One residual: line 196 applies the "support in all three fields" rule without saying that line 168 added it after the fact (N3) |
| **Discussion and implications read like an essay** (Major 7; §3.7) | Partly | The old section on counting outputs and "Why experimental science is less affected" are gone. The Discussion follows the proposed structure (lines 303–329) | "Implications for research evaluation" (526 words; lines 317–323) still keeps three things: the essay's thesis stated as supported (line 319); the DORA/CoARA claim (line 321); and seven untested proposals (line 323), with [AUTHOR: merge your own recommendations]. References 52–67, 16 of 70, are cited only in this subsection. Fixes in N4 and N6 |
| **Deviations from the plan disclosed** (Major 4a, 4b) | Partly | "Deviations from the analysis plan" (line 168); "pre-specified" defined in place (line 132); break tests with 5% trimming; Andrews 1993 cited | The planned specification is still "approximate" (Table 1), with the model estimate pending. The reasons for the change of reference year are [AUTHOR]. Line 158 still calls the 2022-reference estimate "the pre-specified estimate" (N3). The paper-level tests' deviations are incomplete (N1) |
| **Duplicate-figure risk with the companion essay** (Major 9) | Open (author), and now also a consistency problem | `draft_embo.md` (Figs 1–2) and `draft_full.md` (Figs 3–5) still carry the article's data figures; both were last edited at 17:27 (697fb25). `paper/README.md` still lists EMBO Reports as the first essay venue. No essay DOI; no preprint | N5 |
| **AI disclosure: the authors' own ideas** (Major 12) | Partly | Lines 126 and 184 say what originated with the author (H1, the refined hypothesis, the INSPIRE component) and what AI agents proposed (plan, groups, specification, recommendations) | The reframed interpretation and Conclusions were drafted by an AI agent from AI reviews. v2's header says "Not yet revised by the author", so "The interpretations and conclusions are mine" (line 184) becomes true only once the author adopts them. Origin of H2 and H3: [AUTHOR] |
| **AI disclosure: a description of validation** | Open (author) | Line 184 is a placeholder. S1 Appendix's "Code review and re-runs" and "Reading depth" are empty | Policy: "a description of how the user evaluated the validity of the tool's outputs". Also missing from "Use of AI tools": the LLM classifier of the paper-level tests, and the country classifier, which was checked only by an AI agent (S1 Appendix, line 481) |
| **AI disclosure: figure legends** | Resolved | Every legend (lines 192, 223, 235, 243) has the clause | — |
| **AI disclosure: tools named** | Partly | "Claude (Anthropic), via Claude Code" | Model and version, [AUTHOR], for the main session and separately for the classifier's sub-agents, which may run a different model. Deviation 2 says "Repository policy prevents model identifiers from being written here"; the manuscript must still name them |
| **S1 Appendix** (Major 12) | Largely resolved | Rebuilt as an AI-use and verification record: a timeline with commit times and a task table giving the human's role and the checks. Essay material and internal to-do lists removed | Fill the placeholders. Add rows for: the superseded classifier runs and the blind re-runs; agreement between the runs; the author's 400-paper coding; the medRxiv flag coding; the INSPIRE spot-check |
| **Competing interest with Anthropic; model marker** (Major 13) | Largely resolved in the article | I checked the SVGs: no "Opus", "Claude" or "Anthropic" text in Fig1–Fig4, and Fig 1 has three dashed markers, matching its legend. The COI statement is in the form block, with the proposed wording (line 444) | (a) Who paid; any credits: [AUTHOR]. (b) The paper-level classifier is also a Claude model: say so in the COI and AI statements. (c) The essay's figure files in `paper/figures/` still label the marker "Claude Opus 5", against the author's decision to remove it "from all figures" (brief, item 8). See N5 |
| **Ethics: personal data from metadata** (Major 10) | Largely resolved, pending the data-protection officer | Line 180 declares the personal data, the risk, pseudonymisation and suppression below ten. The record-level and aggregate files I inspected on the public companion branch contain no author names, and the scripts blank statistics on fewer than ten authors | The UPF/EMBL data-protection consultation: office, date, outcome, lawful basis and safeguards. A decision on releasing the pseudonymised table |
| **Deposit** (Major 11) | Partly | The Data Availability Statement (line 448) now lists the minimal data set | Nothing is deposited. Record-level identifier tables and the author table are pending; licences are [AUTHOR]. "Reproduce every figure and estimate from the committed data" is not yet true for H2 (Fig 3, S3 Table). The paper-level tests need their own data in the deposit (N1) |
| **Figure format** (minors 24–28) | Partly | TIFF with LZW, RGB, 300 dpi, 2250 px wide (Fig 4: 1653), at most 1830 px high, fonts at 8–11 pt, panels A–D, Fig1.tif naming: all compliant | Font family is Liberation Sans. PLOS: "Use only Arial, Times, or Symbol font in 8-12 point." Re-render, then check with NAAS, the tool the figures page recommends |

### 3.2 Other round-1 major issues

| Issue | Status | Note |
|---|---|---|
| Major 5, H2 | Resolved | Decomposition on combined output; top shares; pre-ChatGPT benchmarks; variants. "Established" dropped; fixed thresholds descriptive only (S3 Table). AI-mention expression and Erdős panel removed; one pipeline; January–August windows |
| Major 6, H3 | Largely resolved | The marker analysis is the H3 test, and published estimates are in S4 Table. The author now doubts the metric (critique log, A2); N4 covers how to handle that without selective reporting |
| Major 8, "consistent with" | Largely resolved | Used once, labelled (line 317). The opposite problem has appeared (N4) |

### 3.3 Round-1 minor issues, grouped

| Group | Done | Still open |
|---|---|---|
| Format | Legend and table placement; form block; Supporting Information as separate files; short title | Markers and HTML comments; e-mail, ORCID and the EMBL unit |
| Methods | arXiv statistics URL; OAI-PMH, OSF and INSPIRE cited; harvest dates reconciled; group caveats; synthetic-control donors (19 candidates, 14 weights, minimum p 0.05); SocArXiv | E-utilities reference; AI as topic in bioinformatics (pending); arXiv q-bio (partly) |
| Introduction (minors 15–19) | All | — |
| Results language | Terminology; "9–13%"; Conclusions on the proposed model | Redundancy (partly) |
| Tables | v1's Table 1 moved to S1 Table with two rows removed; counts; small cells; the H3 table moved | Ranges, pending in S2 Table, which is not yet assembled |
| References | The listed fixes | List length: 70, against a target of 35–40; it falls to 54 with the cut in N4 |
| Other | Internal reviews not called peer review | STROBE-style checklist (optional) |

## 4. New major issues

### N1. The pre-registered paper-level tests: report them in full in this article or remove them, and record the changes made since Deviation 2 before any estimate is seen

**Problem.** Line 172 describes three confirmatory tests and ends "No result of the confirmatory tests is reported here". Two passages lean on them:
- line 309: "which the held-out tests classify directly";
- line 313: "the pre-registered tests examine it in archives where the idea was not formed".

An editor will read confirmatory tests without results as an unfinished study. Results added during review would invite the charge of selective reporting. The deviations that line 172 lists are also no longer complete.

**The record.** All times are 16 October 2026, UTC. GitHub's activity log matches every commit time below to within seconds, which makes the timing checkable by anyone; cite it.

| Time | Event | Commit (push time) |
|---|---|---|
| 16:42 | H1–H3 and the three contrasts recorded | 2cac071 (16:42:22) |
| 17:27 | v1, with the analysis plan | 697fb25 (17:27:53) |
| 17:43 | The companion's specification, scripts and first estimates committed together. These include the trend-adjusted C2 (1.48) and departures from trend for all 18 arXiv archives | companion 37b4b11 (17:43:39) |
| 18:28 | Pre-registration of HN activated | 763aa2b (18:28:57) |
| 18:47 | Amendment 1 (Tests A and B) activated | 78890e5 (18:47:08) |
| 18:48 and 18:55 | Deviations 1 and 2 | 11264ee, 1de63a9 |
| 19:01 | Sampling design, including Test B's list of categories | companion c2f891b (19:01:12) |
| 23:39 | v2 | a17a8b9 |
| 23:43 | First, date-ordered classifier runs superseded by blind runs. They had covered 700 medRxiv papers and the 200 bioRxiv and medRxiv validation papers. The Test A decision rule and the Test B outcome were fixed, and the validation sheet's arXiv half was redrawn | companion 8ab4d9d (23:43:16) |

**What had been seen when each test was registered.** This decides how each test may be described.

| Test | Outcome-side data already examined | Not yet examined | Accurate description |
|---|---|---|---|
| **HN**: cond-mat, astro-ph, quant-ph | Archive totals and their 2026 departures from trend (1.30, 1.34, 1.54; `field_tests.json`, 17:43) | The split by class within each archive | "Held out at paper level". The hypothesis was not formed from these archives, and their composition by class was unseen |
| **Test A, bioRxiv** | Category growth 2022–2026 (`biorxiv_categories_growth.csv`, 08:42); C2, including the trend-adjusted C2 that favoured H1 | The split by class | Not held out. C2 used the same server, and the class without new data overlaps with the computational categories |
| **Test A, medRxiv** | Category growth (08:42); the null result of C3 | The split by class | Not held out. Papers flagged in C3 fall almost entirely in the class without new data, and C3's null was known |
| **Test B** | Every category's growth, including the mathematics subcategories (Q3 2025 to Q3 2026, computed 15 October) and the six particle and nuclear physics archives | The share of papers with new data (the exposure) | "Pre-specified, with outcomes already examined; only the exposure was unmeasured" |

Only HN is held out in the usual sense. Call the set "pre-specified paper-level tests", and keep "held out" for HN. Lines 309 and 313 then need that wording.

**Each deviation or change, assessed.**

| # | Change | Recorded in the registration? | Acceptable? | What the paper must say |
|---|---|---|---|---|
| D1 | Classification and estimation before the author's blind coding | Yes (11264ee) | Yes, with the stated safeguards. Strengthen them: keep the estimates sealed from the author until the coding is committed. Commit only the SHA-256 hash of the results file, and publish the file after the coding commit. That restores most of the protection the original order gave | The order of events, with times. Whether the coding preceded the author's first sight of the estimates. The registered consequence of κ < 0.60 |
| D2.1 | Stratified samples; class shares scale monthly totals | Yes | Yes; a standard design | Sample sizes; the minimum detectable ratio; that the bootstrap redraws the samples. Line 172 omits Test B's samples (about 150 per category in 2019–2022): give the totals |
| D2.2 | Temperature cannot be set; one draw per paper | Yes | Yes, as a limitation. But "classified … independently" is inaccurate: each sub-agent judges 50 papers in one context | Describe the batching. Report agreement between the two runs on 900 papers (D3a). The bootstrap carries sampling error, not decoding noise: say so, or propagate the observed disagreement rate in a sensitivity analysis |
| D2.3 | Classifier identity not written in the repository | Yes | Not acceptable in the paper. PLOS requires "the name(s) of any tools used", and the submission guidelines say "List the name and version of any software package used" | The model identifier of each run, from the run logs, with dates. Justify the use of a proprietary model in Methods: the paper itself cites Palmer et al. [65] on that point |
| D2.4 | Validation sheet limited to bioRxiv and medRxiv preprints under Creative Commons licences | Yes | Acceptable, with checks. The classified samples include papers without a CC licence, so agreement measured on the sheet may not transfer to them | Report the CC share in each classified sample, from the API's licence field. Compare the classifier's share of papers with new data between CC and non-CC papers; this needs no extra coding. Optionally, code about 40 non-CC papers blind, publishing identifiers but not text. After unblinding, publish the key, because the CC BY licences require attribution |
| D3a | 700 medRxiv papers and the 200 bioRxiv and medRxiv validation papers were first classified in batches in date order keyed by DOI, then re-classified blind | No: only in the companion's `methods.md` (8ab4d9d) | Yes. It improves blinding, because DOIs encode posting dates. But it contradicts "Labels are stored and will not be re-drawn" (Deviation 2), and the first runs exposed dates the classifier was meant not to see (Appendix A; line 172) | Record it as Deviation 3, with the time, the reason, and the statement that no first-run label had been analysed. Report the agreement between the runs |
| D3b | Test A decision rule for a single unit | No: companion only | Yes. As of 15df0b1, the code required two of three units to exceed 1, so Test A could never have returned "supported" | Report it as a clarification fixed before estimation |
| D3c | Test B uses a one-sided permutation test | No | Defensible for a directional prediction, but the plan says only "permutation p < 0.05" | State the sidedness as a clarification made before estimation |
| D3d | Test B's arXiv set mixes dating rules. It includes the mathematics subcategories and all six particle and nuclear physics archives, and excludes cs, physics, stat and others | No (`nd_design.py`, 19:01) | Conflicts with §3 of the plan, which says hep-ex and nucl-ex "are reported separately and never pooled with the confirmatory archives" | See N2a |
| D3e | Validation sheet's arXiv half: a simple random sample from arXivRaw instead of a random-day draw, because the arXiv API returned 429. bioRxiv epidemiology and clinical trials dropped from the frames | No | Yes | List them |
| D3f | §1 of the plan says the 60 hep-ex records were "classified by one person". S2 Appendix (line 521) and S1 Appendix (line 484) say an AI agent did it | — | Must be corrected. It misstates who did the work, in a document the paper publishes as S1 Text | A dated erratum note in S1 Text, without editing the registered text: "'one person' should read 'one AI agent, in an internal reviewer role, unblinded'" |

Present these in a deviations table (S6 Table) along the lines the two guides above recommend. Give, for each change:
- the plan's text;
- what was done;
- when it was recorded (commit and UTC time);
- what had been seen by then;
- the reason;
- the expected effect on inference.

**The AI classifier and the author's validation, under PLOS policy.**
- *Acceptable in principle.* PLOS asks that any AI use "to support research reported in a PLOS article" be disclosed, with three elements:
  - "the name(s) of any tools used";
  - "a description of how the tool(s) was/were used";
  - "a description of how the user evaluated the validity of the tool's outputs".

  The author's blind coding of a stratified random sample is exactly such an evaluation. Amendment 1 is right that an AI checking the classifier would be circular.
- *Concerns a reviewer will raise, with fixes.*
  1. **One coder, who formed the hypothesis.** Blinding to dates, servers and labels limits the bias. But abstracts can reveal their period, through facilities, "LLM", or recent surveys, and arXiv comments can give dates. Recruit the optional second coder for 100 papers, and report agreement between the two humans.
  2. **κ ≥ 0.60 is a low bar for estimating ratios of about 1.1–1.2.** What biases the ratio is error that differs between periods, and abstracts written with LLMs since 2023 may be classified differently. Report:
     - confusion matrices by domain and by period (2019–2022 and 2023–2026);
     - κ with 95% CIs;
     - precision and recall for each class.

     As an exploratory sensitivity analysis, add a ratio corrected for misclassification with period-specific sensitivity and specificity: Rogan WJ, Gladen B. Estimating prevalence from the results of a screening test. Am J Epidemiol. 1978;107(1):71–76. doi:10.1093/oxfordjournals.aje.a112510.
  3. **Coverage.** The validation sheet's arXiv half covers cond-mat, astro-ph and quant-ph only. Mathematics and particle-physics papers in Test B are classified with a prompt for "physics or astronomy" papers that was never validated on them.
  4. **What the classifier saw.** It ran as an agent, not as a bare model call. It had:
     - a system prompt from the Claude Code harness, which the author did not control;
     - the run instruction (`scripts/classifier_agent_prompt.md`);
     - file tools.

     Say so. Check the run logs for any tool use other than reading the batch and writing labels; a script that labels by keyword is the obvious risk. Deposit a record of each run: model identifier, time, hash of the batch file, and tools used.
  5. **Training setting.** The samples include abstracts not under open licences, sent to a commercial service. State the account's training setting; line 184 already has the slot.
  6. **Multiplicity.** There are four hypotheses (HN, HN-bio, HN-med and HN-dose) and the plan corrects for none. Judge each against its registered rule, and give Holm-adjusted p-values across the four as a secondary statistic, labelled post hoc.

**How to word it.**

*Methods, replacing line 172 (about 230 words):*

> *Pre-specified paper-level tests.* After the H1 results were known, I formed a refined hypothesis, prompted by an exploratory count made by an AI agent during internal review (Results): within a field, papers that report no new empirical data grew faster in January 2025–September 2026, relative to their 2017–2022 trends, than papers that do. Its tests were written with AI assistance, approved by me and time-stamped in the project's public repository before any paper was classified (commits 763aa2b and 78890e5, pushed at 18:28 and 18:47 UTC on 16 October 2026; S1 Text); they were not entered in a registry. HN compares the two classes in arXiv cond-mat, astro-ph and quant-ph, whose totals, but not their composition, had been examined. Test A repeats the comparison on bioRxiv and medRxiv, whose categories had been examined in C2 and C3; Test B relates each category's departure from trend to its share of papers with new data, outcomes that had been examined. Papers were classified by [model, version] (Anthropic), run as Claude Code sub-agents in batches of 50, in random order, under pseudonymous identifiers, from the title, abstract and (for arXiv) comments; class shares in stratified random samples scale monthly totals, and the bootstrap redraws the samples. A domain's results are confirmatory only if the classifier agrees with my blind coding of 400 papers at Cohen's κ ≥ 0.60; I coded the sheet before seeing any estimate [if so]. S6 Table lists every deviation from the plan, when it was recorded and what had been seen by then.

*Results: a new subsection after the INSPIRE paragraph (template):*

> The classifier agreed with my coding at κ = [ ] (95% CI [ ]) for arXiv, [ ] for bioRxiv and [ ] for medRxiv, and two runs of the classifier on 900 papers agreed at κ = [ ] (S1 Text). Relative to their 2017–2022 trends, papers without new data in cond-mat, astro-ph and quant-ph stood at [ ] in January 2025–September 2026 and papers with new data at [ ], a ratio of [ ] (95% CI [ ]; minimum detectable ratio [ ]), above 1 in [ ] of the three archives. By the registered rule HN was [supported / not supported / contradicted]. [Test A and Test B likewise, each with its level-based estimate beside the trend-based one (N2b), and labelled "not held out".]

**Elsewhere in the paper.**
- *Abstract:* one sentence of at most 35 words (see the model abstract in N4).
- *Title:* unchanged by the result. A supported HN would show that archive labels were the wrong unit, not that H1 was right. Say this in one Discussion sentence, whichever way the result goes.
- *S1 Text caption* (line 418): "Analysis plan for the paper-level tests", not "Pre-registration", unless "in the project's public repository" follows.
- *Data:* add to the deposit and to the Data Availability Statement:
  - the samples;
  - both sets of classifier labels;
  - the validation sheet with the author's codes, and the key;
  - the run instruction and the prompts;
  - the run records.

**If the tests cannot be completed before submission (Option B).**
- Delete the subsection at line 172, S1 Text and the four [ANALYSIS PENDING: pre-registered test] markers.
- Replace them with one sentence in the Discussion: "A paper-level test of this hypothesis on archives not used to form it was specified in a time-stamped plan before any paper was classified (repository commit 763aa2b) and will be reported separately."
- Keep the INSPIRE analysis, labelled exploratory.
- Any OSF registration made now would post-date the first classifier runs. If the author makes one, describe it as an archived copy, not as evidence of timing.

### N2. Two design problems in the registered tests, to settle and record before any estimate is seen

**(a) Test B's arXiv set lets known outcomes drive the verdict.** The design file (`nd_design.py`, companion commit c2f891b, 19:01) puts three kinds of category in Test B.
- **The mathematics subcategories.** By my count from `arxiv_math_subcategories.csv`, 24–26 of the 30 listed subcategories had at least 75–90 papers in Q3 2025. That is roughly the 300 a year Test B requires, although its threshold uses 2019–2022 averages, which were lower. Their growth from Q3 2025 to Q3 2026 (median +80%) was computed on 15 October. Their share of papers with new data can be expected to be near zero.
- **hep-ex and nucl-ex.** §3 of the plan reserves them for exploratory use, and their departures (1.37 and 1.00) were known.
- **The held-out subcategories** of cond-mat and astro-ph, and quant-ph.

Mathematics would make up roughly half of the arXiv categories, all at one end of the exposure, with the largest outcomes already known. The arXiv slope is close to determined before any paper is classified. The validation sheet also does not cover mathematics or particle physics (N1, concern 3).

*Fix, recorded before estimation.* Make the confirmatory Test B the held-out arXiv subcategories together with the bioRxiv and medRxiv categories. Report mathematics and the six particle and nuclear physics archives as a sensitivity analysis. Excluding hep-ex and nucl-ex simply returns to §3 of the plan. If the author prefers the registered set, report both versions, and state in advance that a "supported" verdict needs both. Whatever set is used, describe Test B as "pre-specified, with outcomes already examined".

**(b) The registered estimand extrapolates class-specific trends, which the paper itself treats as not credible on bioRxiv and medRxiv.**
- The paper rejects such trends three times:
  - line 162 says group-specific trends "cannot credibly be extrapolated from years shaped by COVID-19 and bioRxiv's adoption";
  - Table 1 calls the trend-adjusted estimate "a sensitivity analysis only";
  - Table 3 says the medRxiv trend is "dominated by the adoption of a new server; not interpreted".
- Yet Test A estimates departures from class-specific linear trends, identified from 2019–2022 on bioRxiv and from July 2019 to 2022 on medRxiv, with one indicator for 2020–2021. Test B does the same for each category.
- When Amendment 1 was drafted (18:45), the trend-adjusted C2 (1.48; 1.06–2.07) was known to favour H1, while the level-based C2 did not. My round-1 report had warned against reviving it.

The amendment gives a plausible reason: consistency with the arXiv plan ("as in §5–§7"). A reviewer will still ask the question, so answer it in advance.

*Fix, recorded before estimation as part of Deviation 3:*
1. Add a level-based companion estimate for Tests A and B: 2025–2026 against a pooled 2019 and 2022 base, with no class-specific trends.
2. Report it beside the registered estimate.
3. State now that if the two disagree, the result will be reported as dependent on the counterfactual.
4. Report the 2019 placebo, noting that for medRxiv the trend rests mostly on months of server adoption and COVID-19.

### N3. "Pre-specified" is still attached to an estimand that the record does not show was pre-specified

- **Two lines contradict each other.** Line 158: "The pre-specified estimate is exp(β2026)". Line 168: the analysis "used year-by-group effects with 2022 as the reference, turning the plan's pre-trend diagnostic into the primary estimate". Both cannot be true.
- **Only v1's plan is time-stamped** (697fb25, 17:27). The companion's specification first appears together with its first estimates (37b4b11, 17:43). Its `methods.md` says only that "the three confirmatory contrasts were fixed before the formal analysis". Line 132 asks [AUTHOR: state when the companion fixed its model specification]. Unless the session logs show the specification preceded estimation, write that it was committed with the first estimates.
- **The planned estimate is still approximate** (Table 1, "Planned baseline (approximate)": 1.05, 1.02, 1.05). Run it: it is the only estimand time-stamped before modelling. It will not change the conclusion, so reporting it costs nothing.
- **Line 196** says "H1 fails the rule that it needs support in all three fields". Write "fails the rule, added after the results (Methods), that …".

*Fixes.*
- Line 158: "The primary estimate, which departs from the plan (Deviations), is exp(β2026) …".
- Table 1: add the model estimate under the planned specification, as a row labelled "Planned specification (pre-specified)".
- Title: "pre-specified within-field contrasts", not "tests".

### N4. Sentences that still go beyond the data (criterion 4)

The criteria page says "authors should avoid overstating their conclusions". Several of these sentences are new in v2, and they overstate nulls rather than effects.

| Location | Text | Problem | Fix |
|---|---|---|---|
| Abstract; line 305; Conclusions (line 333) | Papers reporting new experimental results "grew as fast as the rest"; the analysis "did not support its refinement" | Within hep-ex and nucl-ex the ratio is 1.00, with a 95% CI of 0.74–1.35. Across the six archives it is 1.12 (0.94–1.35), and two of five registered rule variants exclude 1, in the direction of the refined hypothesis. The rule also counts collaboration analyses of earlier data as new results (line 309), so it is not a clean test | "did not grow detectably more slowly than the rest (ratio 1.00; 95% CI 0.74–1.35), in a comparison that cannot isolate papers needing new data" |
| Abstract; line 271; line 313 | "counts moved unevenly and independently of AI-assisted writing"; "The marker rise did not predict output growth"; "it shows only that measured AI-assisted writing does not explain them" | Rests on an ecological panel of 28 units whose arXiv part, seven clusters, line 154 itself calls "descriptive". The marker drifts after 2024, and the coefficient is given in units no reader can interpret | "Output growth did not track the rise in AI-associated style words". Give the panel slope for a meaningful change, for example a doubling of the marker rate |
| Abstract; line 275 | "not because of reviews, proceedings or white papers"; "The acceleration is not a matter of genre" | Genres come from unvalidated keywords (line 327) | "not explained by the shares of reviews, proceedings and white papers identified by keyword" |
| Line 305 | "Four findings withstood the checks made" | Two of the four are exploratory or ecological | "Four descriptive findings held under the checks made" |
| Line 309 | "Within fields, computational intensity did not predict where output grew, which suggests that the differences … reported by Qi et al. … partly reflect servers" | C1 is inconclusive, with a detectable effect of 1.21. C2 is positive at its 2022 base | "did not robustly predict …, which is compatible with differences between fields partly reflecting servers" |
| Line 110 | Counts "carried some information because the outputs they count were costly to produce" | A premise stated as fact. The author rejects the cost framing (critique log, A1): evaluation values results, polish was costly, and polish was a cue of quality | Rewrite in line with A1, marked as the motivating premise |
| Line 317 | "If fluent text can be produced cheaply …, its quality no longer indicates the effort behind a paper" | Labelled as interpretation, but frames writing as a cue of effort, which A1 rejects | "… form becomes a weaker cue of the quality of the work behind it", still labelled as interpretation |
| Line 319 | "This supports, at the strength the data allow, the view that evaluation built on counts is not prepared for widespread use of AI [5]" | The same paragraph says the causes are "not yet attributable". Growth of unknown cause cannot support a claim about AI | Delete. Keep: "Whatever their cause, these shifts mean that counts from 2025–2026 should not be compared across servers or with earlier years without adjustment" |
| Line 321 | Reforms "remain largely unimplemented where measured, and mostly unmeasured" | Rice et al.'s 95% shows that publications are a criterion for promotion, which neither DORA nor CoARA forbids. McKiernan et al. predates CoARA. The Commission's study finds engagement "broad and growing". Nothing in this study's data bears on the claim | Delete. Keep the two sentences on caps and the sentence on reading capacity |
| Line 323 | Seven untested proposals, with 13 references and [AUTHOR: merge your own recommendations] | Policy material that the data do not test: criterion 1 excludes "Opinion pieces". The AI policy requires conclusions to be the author's own ideas, and these proposals came from AI agents | One sentence: "Proposals to change what is counted have been made elsewhere [one or two citations]; these data do not test them." |
| Line 329 | The Amdahl-type bound, and "Whether experimental work will show the effect later …" | Not a limitation. It reintroduces the "later onset" rescue of H1 | Move one sentence to the Discussion as a labelled, testable prediction, or cut it |
| Line 333 | "preprint counts from 2026 cannot be compared with those of earlier years, or across servers, as before" | Implies they could be compared before | "should not be compared … without adjustment" |

**The H3 marker and the author's pending decision (critique log, A2).** The author writes that the marker should not be used, because "we can't be sure it remains relevant". H3 was recorded before modelling, and its test has been run. Dropping it after seeing the result would be selective reporting.
- *Acceptable option.* Keep the H3 test, restricted to 2024 (the year the word list was built from), in the Results or an S Table. State the author's reason for doubting it as a limitation.
- *Then remove from the abstract and the Conclusions:* "AI-associated style words … did not predict output" and "independently of AI-assisted writing".
- *If the author keeps the marker in the main text:* restrict comparisons to 2024, as Table 2's note already advises.

**Model abstract.** It runs to 284 words by a word-processor count. The opening sentence follows the author's A1, and its wording is the author's to choose.

> Research evaluation judges results, but producing a polished, submittable paper has required substantial skilled work, and generative artificial intelligence (AI) makes polish cheap. If AI raised output mainly where no new experiments are needed, preprints should have grown faster in theoretical, computational and secondary-data work than in experimental work within the same field. I tested this with three contrasts fixed before modelling, in monthly counts of new preprints on arXiv (2015–2026), bioRxiv and medRxiv (2019–2026). Relative to 2022, the January–September 2026 rate ratios were 1.14 (95% CI 1.00–1.30; Holm-adjusted p = 0.11) for theoretical against experimental physics, 1.08 (1.03–1.14; p = 0.01) for computational against wet-lab biology and 1.01 (0.90–1.14; p = 0.84) for medRxiv preprints naming widely reused datasets against others. The first two were typical of arbitrary splits of archives or categories (placebo p = 0.61 and 0.20) and fell to 1.06 without planning white papers in the physics base and to 0.93 without bioinformatics. The prediction was not supported. In a test specified before any paper was classified, papers without new data in three held-out arXiv archives grew [faster than / not detectably faster than] papers with new data (ratio [ ]; 95% CI [ ]). Against their 2015–2022 trends, arXiv physics and mathematics stood 32% and 48% higher in 2026, experimental particle physics included, whereas bioRxiv (0.91) and PubMed (0.93) did not, although bioRxiv grew more than the physics archives tested since 2022. Output grew in every class of authors, fastest among the most productive; in mathematics the top 1% of author names more than tripled theirs. The design cannot attribute these changes to AI, but counts moved unevenly across servers in 2025–2026, which limits comparisons across fields and years.

If a 2024 marker sentence stays (about 20 words), cut the clause on bioRxiv's growth in levels.

### N5. The companion essay contradicts the article and still shows the model marker

**Contradicted claims.** `draft_embo.md` (lines 41 and 43, and the legend of its Figure 2) and `draft_full.md` (the legends of Figs 3–5) state results that v2 refutes or withdraws:
- "theoretical physics has outgrown experimental physics in 2026";
- "computational biology has outgrown wet-lab biology since 2025";
- "Experimental biology is less affected so far";
- bioRxiv shows "no break in 2026";
- the growth "came from hundreds of established mathematicians";
- AI mentions are "a lower bound".

**The marker.**
- The essays' legends describe "the release of an Anthropic model (24 Jul 2026)".
- Six SVG files in `paper/figures/` (the fig1, fig4 and fig8 series) still contain the text "Claude Opus 5".
- These files were last changed before the author's decision (199f5bb, 09:31).
- The companion re-exported its own copies without the marker (0c17d0f), but they were not copied here.

**Why it matters.**
- The article cites the essay twice (ref 5; lines 110 and 319). A reviewer who opens it will find the author asserting the opposite of the article's results.
- The perceived competing interest that removing the marker fixed would return.
- The repository is public, so the drafts are already visible.

**Fix, before either document is posted.**
1. Revise the essay's empirical paragraphs to cite the article, or its preprint, for the data.
2. Replace its data figures with a schematic or with the marker-free files. That also removes the duplicate-figure problem: under criterion 2, figures "should not have been published in any previous publications".
3. Post the article's preprint first.
4. Decide on EMBO Reports.
5. Disclose the essay and the Correspondence in the cover letter, with copies.

### N6. Length, density and structure

PLOS sets no limit ("Manuscripts can be any length"), so this is about reviewability and criterion 5, not compliance.

The main text has 7,126 words of prose. On top of that there are:
- 822 words of figure legends;
- 989 words of tables;
- 478 words of table notes, 259 of them under Table 1.

The Methods run to about 2,600 words. Reviewers will find the evidence, but tire before they weigh it.

| Section (prose words now) | Target | What to cut or move |
|---|---|---|
| Introduction (800) | about 600 | Compress the list of writing-prevalence studies (line 116) to one sentence plus S4 Table. Resolve the Kusumegi sentence (line 114) |
| Methods: Data sources (414) | about 250 | Move the details of request rates and terms (line 142) to S2 Appendix and the deposit README. Keep one sentence: "Retrieval followed each source's terms, except two earlier retrievals that exceeded documented rates (S2 Appendix)" |
| Methods: Statistical analysis (662) | about 400 | Keep the model, inference, placebo definition and detectable effects. Move the robustness list and the inventory of exploratory analyses (lines 162–164) to S2 Appendix, referenced from S5 Table |
| Methods: H2 (262) and H3 (239) | about 300 together | Move the sensitivity variants and the derivation of the lower bound out of the main text; the derivation is already in S2 Appendix |
| Methods: Deviations (184) | about 150, plus S6 Table | Put a deviations table (planned, done, when recorded, what had been seen, reason) in the Supporting Information. Keep a three-sentence summary in the main text |
| Methods: paper-level tests (260) | about 230 (the N1 model), or one sentence (Option B) | — |
| Methods: Ethics (112) and AI use (163) | keep; AI use grows by about 60 words | Required in the body |
| Results: H1 (820, plus a 259-word table note) | about 600 | Cut Table 1 from 18 rows to about 10. Keep: estimate; Holm p and Bonferroni CI; placebo p; detectable effect; event study 2023–2025; pre-period coefficients; bases 2019 and pooled; planned specification; leave-one-out; reading. Move the year-shock ratio, slope change, trend-adjusted estimate and the variant list in the note to S5 Table. In lines 225–229, keep only the checks that decide each reading |
| Results: departures from trend (643) | about 450 | Shorten the break-test and synthetic-control paragraph (line 293) to two sentences. Shorten the US PubMed paragraph (line 295) to one, or move it to S5 Table |
| Discussion: Implications (526) | about 180 | N4 |
| Discussion: Limitations (439) | about 340 | Move or cut the Amdahl paragraph (line 329) |

The outcome would be:
- about 5,700–6,000 words of main text;
- 54 references, after dropping the 16 cited only in the Implications subsection;
- one dense table fewer.

S5 Table should be a spreadsheet with a README, not a set of JSON files. Both S2 Table and S5 Table are captioned but not yet built; assemble them before submission.

### N7. Pending analyses: decide which to run and which to drop

Sixteen [ANALYSIS PENDING] markers remain in the main text, and not all are needed. Delete the mention of any analysis that will not be run.

| Pending analysis | Matters because | Recommendation |
|---|---|---|
| bioRxiv duplicate check | It affects every bioRxiv number, C2 and Fig 1 | **Run** (P0) |
| Planned specification | N3 | **Run** (P0) |
| Pre-registered tests | N1 | **Run with validation**, or remove (P0) |
| Record-level identifier and flag tables; pinned environment and software versions | Criterion 7. PLOS: "List the name and version of any software package used" | **Run** (P0) |
| C3 slope change on the corrected series | A Table 1 cell reads "not yet recomputed" | Run, or drop the row (P0) |
| Structure-matched placebos | The primary inference for C1 and C2 | Run (P1; cheap) |
| Bioinformatics split by AI/ML topic | The reading of C2 | Run (P1; cheap) |
| medRxiv flag validation | C3 rests on unvalidated expressions | Needs a human coder for the 200-row sheet (P1). Otherwise call C3 "unvalidated" |
| Dating by first-version submission | The September 2026 mathematics spike; Discussion, explanation (i) | Run if feasible (P1). Otherwise drop the sentences that depend on it |
| US against non-US on bioRxiv | Discussion, explanation (ii) | Optional. Its country classifier was checked only by an AI agent (S1 Appendix), so a person must check it before use. Otherwise drop the mention |
| bioRxiv categories without COVID-19; synthetic-control variant; OSF continuity | Secondary | Drop the mentions, or run them (P2). If the OSF check is not run, consider removing the social-science series from Fig 1 |

## 5. Minor issues

**Title and front matter**
1. **Title.** Two options:
   - "Preprint growth in the generative-AI era: pre-specified within-field contrasts show no robust difference between experimental and non-experimental work" (151 characters);
   - v2's title, with "contrasts" for "tests" and a plainer object than "experimental bottleneck".

   The author decides.
2. **Front matter.**
   - Add the corresponding author's e-mail and ORCID iD. PLOS says the corresponding author "must provide an ORCID iD at the time of submission".
   - Add the EMBL unit and site, with EMBL as the corresponding affiliation, as the flat-fee agreement requires (line 100).

**Methods**
3. **References for data sources.**
   - Cite the NCBI E-utilities documentation (line 140). PLOS: "All data sources must be acknowledged clearly in the Materials and Methods section."
   - Resolve the INSPIRE [RECHECK] (line 142). INSPIRE allows "15 requests in a 5s window" per IP address, and the companion's harvester pauses 1 s between requests, so the rate was within the limit. INSPIRE states that "most of the metadata is available under a CC0 license" but "restrictions apply to some fields". Confirm that the fields used are unrestricted: categories, document type, experiments, collaborations, author counts, and title and abstract, used for flags only.
4. **Re-harvest within limits (optional, P2).** Consider re-harvesting the arXiv statistics pages and the OSF counts within their documented limits before the deposit, so that the deposited data were obtained in compliance. For arXiv that is about 18 archives × 17 years ≈ 306 pages, or about 77 minutes at a 15-s delay.
5. **Line 146.** Answer the two [AUTHOR] items: why hep-lat is left out, and when the medRxiv list was fixed.
6. **Line 150** says shares "carry no sampling intervals", but S3 Table and line 233 give departures from trend with Newey–West intervals. Say what those intervals mean for a population: uncertainty about the trend, not sampling.
7. **Line 172** (if kept). Give the total number of papers classified, including Test B's samples. Say that arXiv inputs include comments, which can reveal dates ("accepted in …", conference names).
8. **Line 176.** Give the software versions and the code's repository identifier. PLOS: "Provide the repository identifier for any code used in the analysis."
9. **Line 184.** Add:
   - the paper-level classifier and its validation, as item (vi);
   - the country classifier, if its results are used;
   - the model of the sub-agents;
   - the training setting.

   Suggested wording for (vi):

   > (vi) classified about [N] papers by whether they report new empirical data (Methods); I evaluated these labels by coding a blind stratified random sample of 400 papers [and a colleague coded 100 of them] (S1 Text).

**Results**
10. **Line 196.** Label the "all three fields" rule as post hoc (N3).
11. **Table 1.**
    - Remove the "not yet recomputed" cell, or recompute it.
    - Explain footnote ᵃ in one clause.
    - Give the number of placebos beside each placebo p.
12. **Line 233.** "Ranked on their combined output" is clear. Add that names new in 2026 can enter the top 1%, and point to the variant restricted to names active in 2019–2024.
13. **Table 2.** The 2019–2022 column mixes rates (words per 100 abstracts) with shares (the rows marked ᵃ). Split the column, or label each row.
14. **Line 295.** "Accounts for about 1.7 of the roughly 7 percentage points" is arithmetic, not attribution; write "corresponds to".

**Discussion**
15. **Line 313.**
    - Explanation (i): resolve the [RECHECK] on arXiv's post of 1 October 2026.
    - Explanation (iv): "the pre-registered tests examine it in archives where the idea was not formed" is true of HN only (N1).
16. **Line 327.** If the paper-level tests are reported, add their limits:
    - a single human coder;
    - label noise outside the CIs;
    - the validation frame;
    - a proprietary classifier.

**Figures**
17. Re-render Fig1–Fig4 in Arial, and check them with NAAS ("a free, simple-to-use tool called NAAS", in the words of the figures page).
18. **Fig 1.** The marker for the cap of 1 October 2026 sits at the right edge, after the data end. Say so in the legend, or drop it.

**References**
19. **Ref 5** (the companion essay) must have a DOI before submission. PLOS does not allow "Unavailable and unpublished work, including manuscripts that have been submitted but not yet accepted".
20. **Ref 66.** Add the article number, 2544331. Crossref gives volume 33, issue 3, first published 8 August 2025.
21. **Ref 68.** Add doi:10.1371/journal.pone.0337199. The editorial confirms the date of the pre-screen: "we introduced a specific pre-screening for adherence of MR studies to our publication criteria in April 2024".
22. **S2 Appendix** (lines 531 and 535).
    - Cite the JAMA research letter itself, not HPN Online's report of it.
    - Cite the Congressional Research Service directly, not the everycrsreport.com mirror.
    - Resolve the openRxiv [RECHECK] (line 545).
23. **Spot-check.** I checked 12 references in Crossref: refs 2, 3, 4, 8, 14, 16, 41, 60, 61, 63, 66 and 68. All match, apart from the gaps in items 20 and 21.

**Supporting information and form**
24. **S1 Text** must contain:
    - the two plans with their deviations;
    - Deviation 3 (N1, N2);
    - the erratum (D3f);
    - the codebooks;
    - the run instruction.
25. **Data Availability Statement** (line 448). "Will be added" will not do at publication: PLOS requires data to be "publicly available without restriction at the time of publication". If the author table is withheld, name a non-author contact, because "it is not acceptable for an author to be the sole named individual responsible for ensuring data access".
26. **Funding** (line 440). Use PLOS's wording, and say who paid for the AI tools.
27. **CRediT** (line 452). "Writing – original draft" is unassigned. That is honest, since an AI drafted the text; keep it consistent with the AI statement.

**Language**
28. **Density.**
    - The abstract has 30 numeric tokens in 17 clauses.
    - The three Results paragraphs at lines 225–229 run to 117–182 words, with 14–23 decimal numbers each.

    Move every estimate that does not decide a reading to S5 Table.

## 6. Compliance checklist

Key: ✓ met · ✗ not met (blocks submission) · ? open, or depends on a decision. The status refers to v2 together with the companion record up to 8ab4d9d.

| Requirement (source) | Status | Fix before submission |
|---|---|---|
| **Criterion 1:** original research, not "Letters, commentaries, or essays" or "Opinion pieces" ([criteria](https://journals.plos.org/plosone/s/criteria-for-publication)) | ✓ | Cut the essay remnants in the Implications subsection (N4) |
| **Criterion 2:** results and figures not published elsewhere, and not "under consideration for publication elsewhere" (criteria) | ? | Revise or hold the essay; decide on EMBO; post the article's preprint first (N5) |
| **Criterion 3:** a "high technical standard", "described in sufficient detail" (criteria) | ? | Planned specification; bioRxiv duplicate check; software versions; full reporting of the classifier (N1, N3, N7) |
| **Criterion 4:** conclusions supported; "avoid overstating their conclusions"; implications "clearly identified as hypotheses" (criteria) | ? | The sentences in N4 |
| **Criterion 5:** intelligible (criteria) | ✓ | Dense; cut as in N6 |
| **Criterion 6:** ethics and research integrity (criteria) | ✗ | Data-protection consultation; the author's validation of AI outputs; the erratum to the registration (D3f) |
| **Criterion 7:** data availability and reporting standards (criteria; [data availability](https://journals.plos.org/plosone/s/data-availability)) | ✗ | Deposit with a DOI; record-level tables; the author table or a non-author contact; licences |
| AI use disclosed in the body ([AI policy](https://journals.plos.org/plosone/s/ethical-publishing-practice#loc-artificial-intelligence-tools-and-technologies)) | ✓ | — |
| AI: "the name(s) of any tools used" (AI policy); "the name and version of any software package used" ([submission guidelines](https://journals.plos.org/plosone/s/submission-guidelines)) | ✗ | Model and version, for the main session and for the classifier's sub-agents |
| AI: "how the tool(s) was/were used", and the parts affected | ? | Add the classifier and the country classifier |
| AI: "how the user evaluated the validity of the tool's outputs" | ✗ | The author's code review, re-runs, recomputed numbers and sources read; the 400-paper coding |
| AI: hypotheses, interpretations and conclusions "represent the authors' own ideas" | ? | The author adopts the reframed conclusions; cut or rewrite the recommendations the AI proposed |
| AI: figure preparation disclosed "in the figure legend" | ✓ | — |
| AI: code generation disclosed | ✓ | — |
| AI not an author; internal reviews not called peer review | ✓ | — |
| Competing interests listed at submission ([competing interests](https://journals.plos.org/plosone/s/competing-interests)), not in the manuscript file (guidelines) | ? | Payment and credits; mention the Claude classifier; align with the essay |
| Funding in the submission form, not the file (guidelines) | ✗ | Statement missing |
| Ethics statement for personal data from third-party sources: declare "potential risks"; Terms of Use "do not qualify as informed consent" (guidelines) | ? | Risk declared ✓; data-protection outcome ✗ |
| Third-party data sources acknowledged in Methods (guidelines) | ? | E-utilities reference |
| Source terms of use followed (arXiv, OSF, INSPIRE) | ? | Two past exceedances disclosed ✓; INSPIRE within its rate ✓; INSPIRE field licences to confirm |
| Related manuscripts not under consideration elsewhere, and disclosed (guidelines) | ✗ | Decide on the essay and EMBO; cover letter with copies |
| Title of at most 250 characters; short title of at most 100 (guidelines) | ✓ | 128 and 40 |
| Abstract of at most 300 words (guidelines) | ? | 302 by a word-processor count; model abstract in N4 (284) |
| Figure captions "immediately following the paragraph in which the figure is first cited" (guidelines) | ✓ | — |
| Tables after the paragraph that first cites them (guidelines) | ✓ | — |
| Figures: "TIFF or EPS only"; "LZW compression is required"; RGB; width at most 2250 px and height at most 2625 px at 300 dpi ([figures](https://journals.plos.org/plosone/s/figures)) | ✓ | — |
| Figures: "only Arial, Times, or Symbol font in 8-12 point" (figures) | ✗ | Liberation Sans; re-render |
| Supporting Information named with "S" and a number; captions at the end; separate files (guidelines) | ? | S2 Table and S5 Table not yet assembled; split the files |
| References in Vancouver style, numbered, with correct metadata (guidelines) | ✓ | Refs 66 and 68 |
| No "unavailable and unpublished work" in the references (guidelines) | ✗ | Ref 5 needs a DOI |
| Corresponding author's ORCID iD and e-mail (guidelines) | ✗ | — |
| Code "available without restrictions upon publication", in a repository that issues persistent identifiers, with a licence ([code sharing](https://journals.plos.org/plosone/s/materials-software-and-code-sharing)) | ? | Zenodo DOI; MIT licence to confirm |
| Data licence no more restrictive than CC BY (data availability) | ? | CC BY 4.0 to confirm |
| Analysis plan time-stamped and deviations reported (criteria 3 and 4; good practice) | ? | H1: largely ✓, except the label at line 158 (N3). Paper-level tests: ✗ until Deviation 3 is recorded and reported (N1, N2) |
| Deviations judged by "adherence to the protocol and the appropriateness of any deviations": the standard PLOS ONE applies to Registered Reports, a useful bar here ([what we publish](https://journals.plos.org/plosone/s/what-we-publish#loc-registered-reports)) | ✗ | A deviations table (S6 Table) |
| Markers and HTML comments removed | ✗ | 42 markers in the main text, and 38 more in the form block and the Supporting Information |
| Null results acceptable (criterion 1) | ✓ | — |

## 7. Pre-submission to-do list, prioritised

Key:
- **P0** blocks submission;
- **P1** is needed for a clean first review;
- **P2** is desirable;
- **T** must happen before anyone sees an estimate from the classified papers.

### 7.1 Author-only

| Priority | Item |
|---|---|
| **T, P0** | Approve the record of Deviation 3 (D3a–D3f in N1) and the two design decisions in N2: Test B's arXiv set, and the level-based companion estimate. Ask that the estimates be kept sealed, with only their hash committed, until your coding is committed |
| **T, P0** | Code the 400-paper sheet blind, before opening any estimate. Do not open the sealed key or labels. If possible, ask a colleague to code 100 papers |
| P0 | Read v2 and make it yours. Choose the title. Adopt or change the reframed interpretation and Conclusions; the file still says "Not yet revised by the author". Decide on the marker (A2), following N4 so that nothing pre-specified disappears unreported |
| P0 | AI statement. Give the model and version for the main session and for the classifier's sub-agents (from the run logs), the dates, the account type and the training setting. Describe your own validation: code reviewed line by line; the pipeline re-run with identical outputs; numbers recomputed from the source APIs; sources read in full; AI proposals you rejected |
| P0 | Data-protection consultation (UPF or EMBL): office, date, outcome, lawful basis. Decide on the pseudonymised author table, and name a non-author contact |
| P0 | Funding and competing interests: who paid for Claude; any credits from Anthropic |
| P0 | Related manuscripts: decide on EMBO; approve the revised essay (N5); mint its DOI; post the article's preprint; write the cover letter, with copies |
| P0 | Corresponding-author e-mail, ORCID iD and EMBL unit |
| P0 | Zenodo deposit (an account action): DOI, licences, and a private link for reviewers if needed |
| P0 | Read every source cited for a number or quotation, and resolve the [RECHECK] items that need reading: McKiernan et al.; Rice et al.; the Commission's study; Lin and Zhu; Liang et al.'s bioRxiv series; the arXiv post of 1 October 2026 |
| P1 | Human checks: the 200-row medRxiv flag sheet; a spot-check of the INSPIRE classes (for example, 100 records); the country classifier, if it is used |
| P1 | Fill the gaps in the record: why hep-lat is left out; when the medRxiv list was fixed; why the reference year changed; when the companion's specification was fixed (N3) |
| P1 | Decide on Kusumegi et al. (line 114, and Limitations at line 327) under your own rule: "if the results are not clear, we leave it" |
| P1 | The Implications subsection: accept the cut in N4, or replace the proposals with your own, in at most two sentences |
| P2 | An OSF copy of the plans, labelled as made after classification began; a test on 2027 data; a STROBE-style checklist |

### 7.2 Work that remains (agents and the companion, for the author's approval)

| Priority | Item |
|---|---|
| **T, P0** | Write Deviation 3 into both registration files, with times: D3a–D3f; Test B's set (N2a); the level-based companion estimate (N2b); the sealing procedure |
| P0 | Complete the classification; compute the estimates and seal them. After the author's coding, compute: κ with CIs; confusion matrices by period; agreement between runs. Then unseal, and write N1's Methods, Results, abstract sentence and S6 Table. Or apply Option B |
| P0 | bioRxiv duplicate check, then update every affected number |
| P0 | Model estimate under the planned specification. Fix lines 158 and 196, and the title's wording (N3) |
| P0 | The sentence fixes in N4, and the Implications cut |
| P0 | Record-level identifier and flag tables; the data of the paper-level tests; a pinned environment; software versions in Methods |
| P0 | Re-render the figures in Arial and check them with NAAS |
| P0 | Remove markers and comments; split the Supporting Information into files; assemble S2 Table and S5 Table; build the LaTeX version (brief, item 7) |
| P0 | The essay: revise its empirical paragraphs to match the article; replace its figures with marker-free files or a schematic (N5) |
| P1 | Structure-matched placebos; the bioinformatics AI/ML split; the C3 slope change; dating by first-version submission, or drop the sentences that depend on it (N7) |
| P1 | The length cuts in N6. References: E-utilities; refs 66 and 68; the S2 Appendix sources |
| P1 | Checks on the CC frame: the CC share in each classified sample; the classifier's share of papers with new data, for CC and non-CC papers |
| P2 | Re-harvest the arXiv statistics pages and OSF counts within documented limits. Run the optional analyses, or delete their mentions (N7) |

**Suggested order.**
1. Record Deviation 3.
2. Finish the classification.
3. Compute and seal the estimates.
4. The author codes the sheet, and the coding is committed.
5. Compute κ.
6. Unseal the estimates.
7. Write up.

In parallel, the author completes the compliance statements, and the agents make the text and figure fixes.

## 8. Strengths

1. **Honest reframing.** v2 reports a failed pre-specified hypothesis in its title, abstract and Conclusions. All three contrasts and their checks appear wherever results are summarised. That is what criterion 4 asks for, and it is uncommon.
2. **Inference designed for few units.** The analysis has:
   - placebos as the primary inference;
   - minimum detectable effects;
   - Bonferroni intervals beside Holm p-values;
   - a calibration against shocks from year to year;
   - leave-one-out estimates;
   - negative controls.

   Table 1's "Reading" row tells the reader what each contrast can bear.
3. **A verifiable record.** Plans, deviations and analyses carry commit hashes, and GitHub's server-side push times confirm them. Few observational papers can show when their hypotheses were fixed.
4. **H2 done properly.**
   - a decomposition that does not move under proportional growth;
   - classes ranked on combined output;
   - pre-ChatGPT pairs of years as the benchmark for chance;
   - stricter matching of names as a variant;
   - measures that rise mechanically with volume demoted to S3 Table.
5. **Self-correction.** The project corrects itself as a habit:
   - the medRxiv duplicates were found and removed;
   - planning white papers were tested;
   - genres were separated;
   - the request-rate exceedances were disclosed;
   - the classifier was re-run blind once batches keyed by DOI were seen to leak dates (8ab4d9d).
6. **Privacy built into the code.** No names are in the public files, and the scripts, not a person, blank statistics on fewer than ten authors.
7. **AI disclosure in the right places.**
   - a clause in every legend;
   - a task table that gives the human's role;
   - internal reviews labelled as not peer review;
   - an explicit rule that an AI may not validate the AI classifier.
8. **A better measure where it matters.** Measuring experimental dependence paper by paper answers the label problem identified in round 1. The exploratory INSPIRE-HEP component uses curated metadata, with no AI.

---

## Appendix: the reviewer's own checks (reproducible from the repository and public APIs)

- **Timeline.** Commit times are from `git log`; push times from `gh api repos/DSantosO/academia-ia-state/activity`, all on 16 October 2026:

  | Commit | Push time (UTC) |
  |---|---|
  | 2cac071 | 16:42:22 |
  | 697fb25 | 17:27:53 |
  | companion 37b4b11 | 17:43:39 |
  | 763aa2b | 18:28:57 |
  | 369ec3b | 18:45:09 |
  | 78890e5 | 18:47:08 |
  | 11264ee | 18:48:56 |
  | 1de63a9 | 18:55:17 |
  | companion c2f891b | 19:01:12 |
  | companion 15df0b1 | 19:28:51 |
  | a17a8b9 | 23:39:36 |
  | companion 8ab4d9d | 23:43:16 |
  | 015764e | 23:51:07 |

  The repository's visibility is "public".
- **When outcomes were first computed:**
  - `arxiv_math_subcategories.csv`: 2f458de, 15 October, 22:56;
  - `biorxiv_categories_growth.csv` and `medrxiv_categories_growth.csv`: 6021b3a, 16 October, 08:42;
  - archive departures in `field_tests.json`: 37b4b11, 17:43.
- **The test scripts.**
  - In `stats_nd_tests.py` at 15df0b1, a Test A decision required `sum(by_unit > 1) >= 2` with a single unit, so it could never return "supported". This was corrected at 8ab4d9d ("fixed here before any estimate").
  - Test B uses a one-sided permutation test (`p_permutation_one_sided`).
  - Test B's arXiv set comes from `nd_design.py` at c2f891b: the mathematics subcategories, plus hep-th, hep-ph, gr-qc, nucl-th, hep-ex and nucl-ex.
  - Mathematics and particle-physics papers get the "arxiv" prompt (`nd_frames.py`).
  - The validation sheet's arXiv half covers cond-mat, astro-ph and quant-ph only (`make_validation_sheet.py`).
- **Mathematics subcategories** (`arxiv_math_subcategories.csv`). Of 30 listed, 26 had at least 75 papers in Q3 2025 and 24 had at least 90. The median change from Q3 2025 to Q3 2026 among the 26 was +80%.
- **Personal data.** The headers of these files show no author names:
  - `inspire_hep_records.csv.gz`;
  - `arxiv_paper_flags.csv.gz`;
  - `medrxiv_records.csv.gz`;
  - `nd_samples_medrxiv.csv.gz`;
  - the text-feature files.

  `heavy_producers.json` holds aggregates only, with fields describing fewer than ten authors suppressed.
- **Word counts** (my script, excluding HTML comments, headings, tables and legends, and removing markers and citations):

  | Section | Words |
  |---|---|
  | Introduction | 800 |
  | Methods | about 2,640 |
  | Results, prose | about 2,030 |
  | Results, table notes | 478 (Table 1: 259) |
  | Discussion | 1,556 (Implications 526; Limitations 439) |
  | Conclusions | 132 |
  | Abstract (split on whitespace) | 302 tokens, four of them "=" |
- **References cited only in "Implications for research evaluation":** 52–67, 16 of 70. The proposals paragraph (line 323) cites 13 distinct references.
- **Figures.**
  - SVG fonts: Liberation Sans at 8, 9 and 11 px (matplotlib writes points as px).
  - TIFFs: 2250 × 1240, 2250 × 1830, 2250 × 1594 and 1653 × 1003 px; RGB; 300 dpi; LZW.
  - Panel labels: A–D.
  - No "Opus", "Claude" or "Anthropic" in Fig1–Fig4.
  - "Claude Opus 5" appears in six SVGs in `paper/figures/`, the fig1, fig4 and fig8 series.
- **Crossref** (16 October):
  - Refs 2, 3, 4, 8, 14, 16, 41, 60, 61, 63, 66 and 68 match. Ref 66 lacks its article number (2544331) and ref 68 its DOI.
  - The PLOS ONE editorial on Mendelian randomisation confirms the pre-screen began in April 2024.
  - Verified before citing them here: Willroth and Atherton 2024; Lakens 2024; Rogan and Gladen 1978.
- **INSPIRE.** The documented limit is "15 requests in a 5s window". The companion's `harvest_inspire.py` sleeps 1 s between requests.
