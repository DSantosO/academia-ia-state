# Review of "Preprint output in the generative-AI era: pre-specified within-field tests find no robust evidence of an experimental bottleneck" (draft v2)

**Reviewer 1: statistics and causal inference.** Round 2, 17 October 2026.

**Materials consulted.**
- The manuscript, `paper/plos_one/draft_v2.md`, and the response to round 1, `reviews/round1/response_round1.md`.
- `paper/plos_one/stats/` (companion commit 0e239cd):
  - `results.md` and `methods.md`;
  - `within_field_tests.json`, `round1_tests.json`, `field_tests.json`, `marker_tests.json` and `heavy_producers.json`.
- The pre-registration and Amendment 1, with Deviations 1 and 2.
- My round-1 review.
- For the design of the pending tests only, the companion's code on branch `claude/happy-lovelace-wqek9b` at commit 15df0b1 (16 October, 19:28 UTC):
  - `stats_nd_tests.py`, `nd_design.py`, `nd_frames.py` and `classifier_batches.py`;
  - `make_validation_sheet.py` and `classifier_agent_prompt.md`.

  That commit holds code, sampling frames and paper identifiers. It holds no labels and no estimates. I did not look for confirmatory output anywhere, and nothing in this review reports one, so the author's validation coding stays blind.

**Conventions.**
- "My check" marks a computation from the JSON files, with the method stated where it is used. The scripts are in my scratchpad and are not part of the deposit.
- Locations refer to the section headings of v2.

---

## 1. Summary of the changes

### 1.1 What v2 changed

**Framing.**
- H1–H3 are reproduced as recorded before modelling.
- The pre-specified within-field tests are reported plainly as not supporting H1. A decision rule for H1 (support in all three fields) is added and labelled as set after the fact.
- The title, abstract, Discussion and Conclusions are rewritten. Causal verbs, "1.9 million", "without any misuse" and the vendor marker are gone.

**Inference for the contrasts.**
- Methods now describe the model that was run: Poisson pseudo-maximum likelihood (PPML), month fixed effects, group-specific seasonality and Driscoll–Kraay (DK) errors.
- The DK intervals are labelled as within-year uncertainty.
- The in-space placebo p is declared the primary inference.
- Holm p values are reported with the planned Bonferroni (98.3%) intervals, and minimum detectable effects (MDEs) are given at α = 0.05 and α/3.
- A "year-shock" ratio is added.
- A section on deviations from the plan lists the change of reference year and the other departures.

**Table 1 is now a specification summary.** It gives:
- the event-study path and the pre-period coefficients;
- 2019 and pooled bases, and an approximate planned baseline;
- the 2026/2025 ratio and the slope change;
- the trend-adjusted estimate, leave-one-out ranges and negative controls;
- variants of C1.

**New analyses.**
- Snowmass 2021 and European Strategy papers removed from the physics series.
- A split by genre in mathematics and the six particle and nuclear physics archives.
- Departures from trend counted as list entries.
- sup-Wald break tests with 5% trimming, plus fixed-date Wald tests.
- A PubMed comparison of US and non-US articles.
- For H2, a decomposition of growth by author class, ranked on combined output, with pre-ChatGPT pairs of years as a benchmark and four sensitivity variants.
- For H3, Kobak et al.'s style words, with marker difference-in-differences and lower bounds on the share of LLM-processed abstracts.
- "Use vs output": arXiv groups against bioRxiv, plus a category panel.
- An exploratory classification of INSPIRE-HEP records.
- medRxiv duplicates removed.

**Pre-registration.** Paper-level tests are registered:
- on the held-out arXiv archives;
- on bioRxiv and medRxiv;
- as a dose–response across categories.

Two deviations are recorded, and the results wait on the author's blind validation.

**Still pending.**
- 18 [ANALYSIS PENDING] markers. Among them are several analyses I asked for:
  - the planned specification;
  - structure-matched placebos;
  - the split of bioinformatics by AI or machine-learning topic;
  - the bioRxiv split by US and non-US institution;
  - removal of COVID-19 preprints from bioRxiv;
  - dating by first-version submission, with January–August versions of every 2026 estimate;
  - the synthetic control with clean donors;
  - validation of the regular expressions.
- The bioRxiv duplicate check, marked [RECHECK].

### 1.2 Overall judgement

**The central problem of round 1 is solved.** The paper now reports what its pre-specified tests show. The verdict on H1 holds under every reading I can construct:
- the 2022, 2019 and pooled bases, and the approximate planned baseline;
- the in-space placebos;
- in-time calibration;
- the leave-one-out criterion.

On this core I have only one substantive objection: the year-shock ratio is mis-specified (N1).

**The remaining problems are of a different kind:**
- calibration errors that make some exploratory results look stronger than they are (N1, N3);
- exploratory headlines that rest on one counterfactual or one unit (N2–N4);
- funding evidence that is over-read on PubMed and left unreported on medRxiv (N5);
- design and implementation problems in the pending pre-registered tests. These should be fixed before anyone reads their results (N6).

The framing issues are collected in N7.

### 1.3 Numbers checked against `stats/`

I checked 25 groups of numbers. All but the noted items match.

| # | Claim in v2 (location) | Source | Result |
|---|---|---|---|
| 1 | C1 1.14 (1.00–1.30), Holm p 0.11; C2 1.08 (1.03–1.14), 0.01; C3 1.01 (0.90–1.14), 0.84 (Abstract; Table 1) | `results.md`, H1 table | Matches (C2's Holm p is 0.0095) |
| 2 | Bonferroni 98.3% CIs 0.97–1.34; 1.02–1.16; 0.87–1.17 (Table 1) | My check from the JSON β and SE | Matches (C2 1.015–1.158) |
| 3 | MDEs 1.21/1.25; 1.08/1.09; 1.19/1.22 (Table 1) | My check: exp(2.80·SE) and exp(3.24·SE) | Matches |
| 4 | Placebo p 0.61 (153 pairs) and 0.20 (462 halvings) | `within_field_tests.json`: shares 0.608 and 0.197 | Matches (with +1: 94/154, 92/463) |
| 5 | Year-shock ratio 1.54 (p 0.12), 0.67 (0.50), 0.19 (0.85) (Table 1) | `round1_tests.json`; C3 recomputed from `within_field_tests.json` | Arithmetic matches (C3 0.188, p 0.85). The statistic is mis-specified (N1) |
| 6 | Pooled bases: C1 1.11 and 1.12; C2 0.99 (0.80–1.22); C3 1.01 (0.90–1.13) | `results.md` P1c and P3 | Matches |
| 7 | Base 2019: 1.05; 0.87; 1.01 (0.86–1.19) | `results.md`, sensitivity | Matches. However, the P1c table in `results.md` still gives C3 as 0.99 (0.88–1.10) against 2022 and 0.98 (0.84–1.15) against 2019, with a 2026/2025 ratio of 1.08: these are values from before the duplicate correction (minor 1) |
| 8 | Snowmass papers 16.4% of hep-ex, January–September 2022; C1 cleaned 1.06 (0.89–1.25); hep-ph/hep-ex 0.88; hep-th/hep-ex 0.87 | P1b | Matches |
| 9 | hep-ex departure 1.37 (1.12–1.67), 1.58 (1.38–1.82) cleaned | P1b; `field_tests.json` | Matches |
| 10 | Genres: mathematics 1.69 vs 1.68; six archives 1.27 vs 1.19; experiment 1.08 vs 0.97 | P1f | Matches. The trend window is 2019–2022 (N2) |
| 11 | List entries: physics 1.24, mathematics 1.43; rank p 0.11 vs 0.28 | P1g | Matches |
| 12 | Breaks: physics 2025-05 (p 0.001); the six archives and mathematics at 2026-01; cs, bioRxiv and C1 p = 0.34, 0.17, 0.56 | P1d | Matches |
| 13 | Synthetic control 11.9%, about 8% without September | `field_tests.json`, monthly gaps | Matches: mean log gap 0.113 (exp − 1 = 11.9%); January–August 0.077 (8.0%) |
| 14 | PubMed US/non-US 0.94 (0.92–0.96) and 0.91 (0.89–0.93); US share 19.6% → 18.2% | P1e | Matches. "No comparable decline in 2019–2022" does not (N5) |
| 15 | Mathematics decomposition +266 / +121 / +57% (total +80%); bottom 90% 52% of the increase; 2024→2025 growth 17 / 14 / 12% | `heavy_producers.json` | Matches |
| 16 | Variants: top 1% +78% to +211%, bottom 90% +26% to +49% | `heavy_producers.json` | Matches for variants that change one thing. Combined variants fall outside the range (minor 5) |
| 17 | Theory +44 / +37 / +21% (total +26%); namesake-robust 50 / 33 / 20%; bottom 90% 54% of the increase; earlier bottom-90% growth −0.7% to 8.1% | `results.md` | Matches |
| 18 | Top-1% share 5.15% → 6.84%, +1.77 pp (1.37–2.17); theory +0.82 pp; top-10% share in theory −0.30 pp | `results.md` | Matches |
| 19 | Markers ×2.56, ×2.15, ×2.17, ×2.13, ×2.73, ×1.62; difference-in-differences 1.18 (0.98–1.42), 1.00 (0.81–1.22), 0.75; mathematics/experiment 0.75 (0.62–0.91); LLM lower bounds 4.4%, 7.8%, 8.2% | `results.md`, H3 | Matches |
| 20 | Panel: slope 0.0001 (−0.0023 to 0.0024); interaction 0.0041 (0.0003 to 0.0080), p 0.034; within bioRxiv 0.0011 | `marker_tests.json` | Matches |
| 21 | Use vs output: mathematics markers 0.74 (0.63–0.87), output 2026/2025 1.27 (1.04–1.56); physics 1.07, theory 1.08, experiment 1.02 | `results.md` | Matches |
| 22 | INSPIRE: 1.10 vs 1.23, ratio 1.12 (0.94–1.35), variants 1.04–1.19 (two of five exclude 1); within experiment 1.00 (0.74–1.35), variants 0.75–1.05; hep-ex 1.33; by team size 1.55, 1.42, 0.64 | `results.md`, INSPIRE section | Matches |
| 23 | medRxiv: flagged ×2.40, others ×2.39 since 2022; growth 20.9% and 16.4%; C3 1.05 (extended list) and 1.07 (title-only filter) | `round1_tests.json`, `medrxiv_flags` | Matches (874/364 and 11,036/4,623) |
| 24 | Archive trends: math-ph −4.3%, nucl-th −2.5%, nlin −1.1% a year | `field_tests.json` | Matches |
| 25 | "Placebo p = 0.70" for C1 without gr-qc (Results, physics) | P1c | The value matches, but the text attaches it to the 2017–2019 estimate. It belongs to the 2022 base (minor 2) |

**Two statements in the response do not match v2:**
- The response says the abstract states that the physics test "could detect only ratios above 1.21". The abstract does not mention the MDE.
- The response says the Results state that C1's interval "excludes almost nothing of interest". That phrase is not in v2.

---

## 2. Recommendation

**Major revision.** In round 1 I recommended major revision, and rejection in v1's framing. The trajectory is good: the core is now sound, and most of what remains is cheap.

### 2.1 Criterion 4 (conclusions supported by the data)

| Claim as framed in v2 | Supported? |
|---|---|
| H1 not supported by the pre-specified tests | **Yes, robustly.** |
| H2: growth was broad-based | **Yes.** Every class grew, and the bottom 90% contributed about half the increase. |
| H2: growth was concentrating, and "in mathematics the top 1% of names more than tripled theirs" | **In direction, yes; in reading and magnitude, no.** The top 1% is partly selected on its 2026 output. Part of the rise in the top-1% share is mechanical (N4). |
| H3: AI-associated style words rose in every group | **Yes, robustly.** The rises (×1.6–2.7) are far beyond year-to-year noise. |
| Output did not track the markers ("independently of AI-assisted writing") | **Suggestive, not robust** (N3). It rests on one unit, mathematics. Within biology, markers and output point the same way, and the intervals omit year-level variation. |
| arXiv accelerated against its own trend while bioRxiv and PubMed did not | **For arXiv against its own trend: yes.** The contrast with bioRxiv depends on the counterfactual. In a direct comparison, only mathematics gained unusually on bioRxiv in 2026 (N2). |
| "Experimental particle physics included and not because of reviews, proceedings or white papers" (Abstract) | **No as worded.** The genre analysis found no departure in the experimental archives on its trend window (N2, N7). |
| In particle and nuclear physics, papers reporting new experimental results "grew as fast as the rest" (Abstract) | **Selective.** True within hep-ex and nucl-ex, with a wide interval (0.74–1.35). Across all six archives, the point estimates favour the hypothesis (1.04–1.19) (N7). |
| "This supports … the view that evaluation built on counts is not prepared…" (Implications) | **Too strong.** "Consistent with" is what the data allow (N7). |

### 2.2 What prevents a minor revision
1. **Exploratory headlines that go beyond the evidence.** They appear in the abstract, Principal findings and Conclusions (N2–N4, N7). The fixes are mostly rewording.
2. **Two pending checks that can move numbers in the abstract:**
   - the bioRxiv duplicate check (the medRxiv correction lowered 2026 non-COVID growth from 22% in v1 to 16.4%);
   - dating by first-version submission, with January–August versions.

   In addition, the declared primary inference, the placebos, is not yet matched to each contrast's structure.
3. **Pre-registered tests without results.** They are described, but no result is given, and their implementation has problems that should be corrected before anyone sees a result (N6). At submission, either report them under the safeguards in N6.4, or reduce them to one sentence and publish them separately. The current half-state should not go to the journal.

If these are done, I expect to recommend acceptance.

---

## 3. Round-1 issues: status

### 3.1 Major issues

| Round-1 issue | What v2 did | Status | Evidence and what remains |
|---|---|---|---|
| **M1.** The estimand does not match H1; the reference period was changed | Disclosed in "Deviations from the analysis plan", with the pre-period coefficients that make 2022 a low year. Table 1 gives 2019 and pooled bases, an approximate planned baseline, the 2026/2025 ratio and slope changes. Fig 2D shows the path | **Partly resolved** | (a) The model under the planned specification is pending. (b) The reasons for, and timing of, the change are still [AUTHOR]. (c) Methods still says "the pre-specified estimate is exp(β₂₀₂₆) … relative to 2022", which contradicts the Deviations paragraph (minor 3). (d) The acceleration estimands lack in-time calibration (N1). (e) Symmetric treatment of COVID-19 in bioRxiv is pending |
| **M2.** Model and inference | Model described. DK intervals labelled as within-year. Placebos declared primary. Year-shock ratio added | **Partly resolved** | (a) The placebos are not matched to each contrast's structure (pending). C1's reference set mixes physics with cs, mathematics, q-bio, q-fin and stat. (b) The year-shock ratio is centred on 2022 rather than on the pre-period mean, and uses normal p values with 2–6 degrees of freedom (N1). (c) DK intervals still carry inferential weight in places: C3 "excludes increases of more than 14%", the marker difference-in-differences, use vs output and PubMed |
| **M3.** Parallel trends fail in biology; the 2026 movement in C2 is a wet-lab slowdown | C2 described as it is: fragile, dependent on bioinformatics, a wet-lab slowdown, and acceleration confounded with the end of adoption. Rambachan–Roth declined. PubMed check done | **Partly resolved** | COVID-19 removal and the bioRxiv split by US and non-US institution are pending. The PubMed check is over-read, and an existing medRxiv split is unreported (N5) |
| **M4.** Weak proxies; negative controls and leave-one-out estimates | Each contrast labelled for what it is. Leave-one-out criterion stated and labelled post hoc. Negative controls given as distributions. Paper-level measurement pre-registered, and INSPIRE exploratory | **Resolved** (paper-level tests pending) | – |
| **M5.** No decision rule for H1; false-discovery adjustment on the wrong analyses | Rule added and labelled post hoc. Holm with Bonferroni intervals. Benjamini–Hochberg dropped. Reversals reported | **Resolved for H1** | The same gap recurs in the new pre-registration: no rule combines its four confirmatory tests (N6) |
| **M6.** Power | MDEs at α/3. C1's MDE is in Results and Limitations | **Partly resolved** | (a) MDEs still use within-year SEs. Label them as lower bounds. (b) C3's upper limit is read from DK intervals. (c) The abstract does not mention the MDE, despite the response |
| **M7.** Break tests, placebo dates, rule changes | sup-Wald tests with 5% trimming and fixed dates, with a boundary caveat. Rule indicators declined, as I advised. Endorsement bias handled. January–August done for the synthetic control and the H2 decomposition | **Largely resolved** | January–August versions of the other 2026 estimates are pending. With 5% trimming the physics break moves from 2024-11 (the old boundary) to an interior 2025-05, which confirms that the old date was an artefact |
| **M8.** The heavy-producer measure is mechanical | Symmetric decomposition as the main statistic, benchmarked on pre-ChatGPT pairs. Fixed-threshold measures moved to S3 Table as descriptive. Histories from 2019. Sampling intervals dropped | **Largely resolved** | The decomposition's null is correct (my simulation confirms it). But "the top 1% tripled" is mis-readable, and the concentration shares are not invariant under proportional growth (N4) |
| **M9.** What the design can say about cause | Causal verbs and the vendor marker removed. The argument from legitimacy labelled as interpretation | **Largely resolved** | Residual overstatements in the abstract and Implications (N7) |
| **M10.** Descriptive inferences that do not hold | Range comparisons, year-on-year rankings and monthly endpoints replaced. "No break" replaced by estimates. H3 moved to measured markers. q-bio mentioned. medRxiv reported by window | **Resolved** | – |

### 3.2 Minor issues

| # | Issue | Status | Note |
|---|---|---|---|
| 1 | Describe the model run; data window | Resolved | – |
| 2 | Counts, pre-period coefficients and placebo shares in the table | Resolved | Table 1 |
| 3 | Indexing to 2022 | Partly resolved | Caveat in the legend; Fig 2D on a log scale |
| 4 | Yearly change in the log ratio, with its 2017–2025 range | Pending (S2 Table) | This is now the missing in-time calibration for the acceleration estimands (N1); do it |
| 5 | Rounding slip | Resolved | – |
| 6 | "1.9 million" | Resolved | – |
| 7 | Validate the regular expressions | Pending | The AI-tools expression is moot. The COVID-19 and dataset expressions, and the new keyword rules for Snowmass and genres, are unvalidated |
| 8 | Aliasing; OAI series for the synthetic control; donor count | Partly resolved | Donors reconciled; the clean synthetic control is pending |
| 9 | PubMed as a comparator | Partly resolved | Journal-side changes noted. PubMed was already 0.90 of trend in 2024 (N5) |
| 10 | Equivalence test for H3 | Partly resolved | No margin, acknowledged. But "rose by a similar factor" persists for biology, where the point estimates are 1.19 and 1.18 (N3) |
| 11 | The marker regression is confounded | Partly resolved | Server-specific year effects added. The pooled interaction is identified mainly by the 7-cluster arXiv part, and the panel includes the drift years 2025–2026 (N3) |
| 12 | Relabel "confirmatory" | Partly resolved | "Pre-specified" is defined, but it is still applied to the 2022-referenced estimate (minor 3) |
| 13 | Fig 3 legend | Moot | – |
| 14 | The cap and future physics series | Resolved | – |
| 15 | Data availability | Resolved in the statement | The deposit is pending |

### 3.3 Requested analyses (round-1 §5)

| # | Analysis | Status |
|---|---|---|
| 1 | Planned estimand and specification table | Table done. The planned-specification model is pending |
| 2 | Structure-matched placebos | Pending. They are now the primary inference, so they must be done |
| 3 | Bioinformatics split by AI or machine-learning topic | Pending; lower priority now (Section 6) |
| 4 | US vs non-US for the wet-lab slowdown | PubMed done; bioRxiv pending; a medRxiv split exists but is unreported (N5) |
| 5 | H2: decomposition, null and 2019 histories | Done, apart from the simulation null (Section 3.4) |
| 6 | Pre-registered out-of-sample test | Replaced by a paper-level pre-registration on held-out archives (N6). No 2027 test is registered |
| 7 | January–August sensitivity | Partly done |
| 8 | Rambachan–Roth | Declined (Section 3.4) |
| 9 | Synthetic control with clean donors | Pending |

### 3.4 Declined points: are they justified?

| Declined | Justified? |
|---|---|
| Rambachan–Roth sensitivity | **Yes.** No conclusion now rests on C2's parallel trends, and the bounds could only widen intervals. |
| Fixed-b or small-sample critical values for DK intervals | **Partly.** It is acceptable while the DK intervals are descriptive. It is not acceptable where they still decide a reading: C3's ">14%", the marker difference-in-differences, use vs output and PubMed. Either calibrate those readings in time (N1) or drop the inferential language. |
| End-of-sample instability test (Andrews 2003) | **Acceptable.** The 5% trimming plus fixed dates is a reasonable substitute. The text says that boundary dates may be later, and timing claims rest on yearly departures. |
| Rule-change indicators | **Yes.** This was my own advice. |
| Uniform-scaling simulation null | **Justified for the fixed-threshold measures**, which are now descriptive, because the symmetric decomposition has an analytic null. **Not justified for the concentration shares.** Methods claims they "do not move under proportional growth", and in a noisy count model with an activity threshold they do (N4). The simulation is still needed, now for the shares. |
| Prospective 2027 test | **Acceptable for this submission.** Registering it now costs little and is the only design that is free of everything already seen. |

---

## 4. New major issues

### 4.0 The new analyses at a glance

| Analysis | Correctly specified? | Correctly interpreted? |
|---|---|---|
| **Alternative bases; placebo p as primary** | Bases: yes. They exclude 2020–2021 as I suggested. Placebos: not matched to each contrast's structure, and C1's reference set mixes fields. Placebo p is computed for the 2022 base only. | The verdict on H1 is right. The year-shock ratio is mis-specified (N1). The pooled base for C2 (0.80–1.22) is about four times wider than the 2022 base (1.03–1.14), a direct illustration of the year-level variance that the DK intervals omit. Say so. |
| **Break tests, 5% trimming** | Yes, with an AR(1) bootstrap. The bootstrap null may be too favourable if the residuals are more persistent than AR(1). | Yes. The text says that boundary dates may be later. Avoid "no slope break" for cs, bioRxiv and C1, and say "no detectable" instead. |
| **List entries** | Yes. Note that cross-lists are 67% of hep-ex and 69% of nucl-ex entries in 2026 (`round1_tests.json`), so list entries there mostly measure cross-listing from other archives. | Yes. Rank p has a floor of 1/18. |
| **PubMed check of the US funding shock** | Yes, as a comparison of rates. | **Over-read** (N5). |
| **Snowmass and European Strategy removal** | The idea is right. The keyword rule is unvalidated: the companion's INSPIRE file tags 214 Snowmass records in all of 2022 across its six archives, against 332 flagged by the keywords in January–September 2022 alone. The archive sets differ slightly (hep-lat vs gr-qc), but not by enough to explain the gap. | Removal assumes that white papers were added to regular output. If they displaced it, the cleaned 2022 base is too low. So 1.14 (kept) and 1.06 (removed) bracket the truth, and the 2017–2019 base, free of both Snowmass and COVID-19, gives 1.11 (0.97–1.26). The abstract should give the range, not only 1.06. |
| **Genres** | Yes, within its window. The keyword rules are unvalidated. | Right for mathematics and the six archives taken together. **Not for experiment** (N2). |
| **Symmetric decomposition (H2)** | **Yes.** In my calibrated simulation of uniform ×1.80 growth, the classes grow by +80.8%, +81.0% and +80.2% against +80.4% in total. | Partly. The top 1% is selected partly on 2026 output (N4). |
| **Marker difference-in-differences with OLS t intervals** | OLS treats months as independent. Year-level shocks are likely (N3). | "No detectable difference" is right. "Similar factor" is not, for biology. |
| **Use vs output** | The marker part, yes (2024 is the right year). For the output part, the DK intervals have no in-time calibration. | **Over-read** (N2, N3). |
| **INSPIRE classification** | The rule is applied as registered, without AI, which is good. But: (a) the ratio comes from separate fits, whereas a stacked model with month effects would match the main design; (b) curation lag is untested. If experiment links or collaboration fields are less complete for 2026 records, ND is undercounted in 2026. The no-link variant (0.75 against 1.00 within experiment) is consistent with this, though not proof of it. Report link completeness by year. | **Selective in the abstract** (N7). |
| **medRxiv duplicate correction** | **Yes**, and reported although it changed numbers. | Yes. Propagate it to `round1_tests.json` (minor 1). Its size makes the bioRxiv check urgent (N2). |

### N1. The in-time calibration is mis-specified, and the acceleration estimates have none

**Location.** Table 1, row "2026 coefficient / SD of pre-2022 year coefficients (p)"; Methods, "In-space placebos"; Results on C2 ("As acceleration, however, it moved"); the companion's `year_shock_calibration_2026`.

**Problem 1: the ratio is centred on 2022.**
- The statistic is β₂₀₂₆ divided by the standard deviation of the pre-2022 coefficients, with a normal p value.
- Every coefficient is measured against the same 2022, so the pre-period coefficients have a non-zero mean whenever 2022 is atypical. The paper itself says 2022 was a low year for C1 and C2.
- The question "is 2026 unusual among years?" needs one of two forms:
  - a rank among the years, with the identical estimator;
  - a prediction-interval z, (β₂₀₂₆ − mean)/(SD·√(1 + 1/n)), referred to t with n − 1 degrees of freedom.

**What each version gives** (my check):

| Contrast | Pre-2022 mean (ratio scale) | Reported z (normal p) | Centred z (t p) | Rank p, (r + 1)/(n + 1) |
|---|---|---|---|---|
| C1 (n = 7) | 1.09 | 1.54 (0.12) | 0.50 (0.64, 6 df) | 3/8 = 0.38. The JSON already holds the share, 2 of 7, but the manuscript does not report it |
| C1, non-COVID years only (2015–2019 and 2022) | 1.03 | – | 2.18 (0.08, 5 df) | 1/7 = 0.14, the floor |
| C2 (n = 3) | 1.09 | 0.67 (0.50) | −0.01 (0.99, 2 df) | 2/4 |
| C3, corrected (n = 3) | 0.95 | 0.19 (0.85) | 0.87 (0.48, 2 df) | 3/4 |

- With n = 3, a normal p value is not defensible, and a rank p cannot fall below 1/4.
- None of this changes the verdict on H1. But the row as printed makes C1 look closer to unusual than it is, and its name ("year shock") suggests a calibration it does not provide.

**Problem 2: the acceleration estimands have no in-time calibration.**
- Table 1 and the Results report C2's 2026/2025 ratio as 1.10 (1.06–1.15). That DK interval implies p < 0.001.
- The one-year changes in C2's log ratio (from the event-study coefficients) were:

  | Year | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
  |---|---|---|---|---|---|---|---|
  | Change | −0.178 | −0.051 | +0.012 | −0.026 | −0.033 | +0.041 | **+0.099** |

- 2026 is the largest positive change, but it is smaller in magnitude than 2020's. The rank p is 2/7 = 0.29 two-sided and 1/7 = 0.14 one-sided, the floor.
- C3's 2026 change (+0.097) is the same size. The text attributes it to "a dip in 2025", but describes C2's equal-sized change as movement ("As acceleration, however, it moved"). Apply one reading to both.
- C2's slope change has the same problem. The AR(1) bootstrap p (0.024) is closer to honest than the Newey–West interval, but the pre-2023 slope (−6.7% a year) is driven by the single 2019–2020 drop. A broken-trend model with a short pre-period then reads a level shift as a slope.

**Fix.**
1. Replace the row with the rank-based in-time p, using the identical estimator and stating the attainable floor, plus the centred z.
2. Give the same for 2026/2025 and for the slope changes.
3. The yearly-change column I asked for in round 1 (minor 4, still pending in S2 Table) is exactly this calibration.

### N2. The cross-server divergence depends on the counterfactual; in a direct comparison only mathematics stands out

**Location.** Abstract; Results, "Departures from trend and the comparison between servers"; Discussion, Principal findings (third finding); Conclusions.

**Problem 1: two different trends are being compared.**
- Physics is measured against its own 2015–2022 trend of 2.9% a year. bioRxiv is measured against 12.4% a year, fitted to years in which the server was still being adopted.
- bioRxiv grew 9–13% a year in 2023–2026, roughly its trend rate.
- Whether that is "no acceleration" or "growth that held up after adoption should have slowed" cannot be decided from these data. The text concedes this ("in levels bioRxiv grew more"), but the Abstract, Principal findings and Conclusions still present the contrast as a finding that "withstood the checks".

**Problem 2: in a direct comparison, physics' 2026 gain on bioRxiv is ordinary.**
- The use-vs-output model gives the year-by-year path of each arXiv group relative to bioRxiv (`marker_tests.json`, `use_vs_output.*.output`). The one-year changes are:

  | arXiv group vs bioRxiv | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
  |---|---|---|---|---|---|---|---|
  | Six physics archives | −25.0% | +8.3% | +7.0% | −8.5% | −5.8% | −5.4% | **+7.3%** |
  | Experiment | −34.2% | +13.6% | +25.0% | −14.4% | −8.0% | −3.6% | **+1.6%** |
  | Mathematics | −22.6% | +2.5% | +3.3% | −4.5% | −2.6% | −5.9% | **+27.2%** |

- The 2026 gain of the six physics archives (1.07; 0.99–1.16) is the size of the gains of 2021 and 2022. Experiment gained 2%. Only mathematics moved by an unusual amount.
- "What is specific to arXiv is the acceleration in 2026" is therefore true of mathematics, and of physics only against its own trend.

**Problem 3: "experimental archives included" depends on the archive and on the trend window.**

| Series | 2026 departure | Trend window |
|---|---|---|
| hep-ex | 1.37 (1.12–1.67); 1.58 without planning papers | 2015–2022 |
| nucl-ex | 1.00 | 2015–2022 |
| hep-ex + nucl-ex, all papers (genre analysis) | 0.97 (0.78–1.20) | 2019–2022 |
| hep-ex + nucl-ex, research articles only (genre analysis) | 1.08 (0.92–1.28) | 2019–2022 |
| hep-ex + nucl-ex (INSPIRE, either class) | 1.18 | 2017–2022 |

- The genre analysis is cited in the abstract to show that the acceleration is "not because of reviews, proceedings or white papers". On its own window it found no departure in the experimental archives.
- The genre analysis's trend for experiment (+6.1% a year) is steepened by the 131 white papers of January–September 2022 at the end of its window.

**Problem 4: the bioRxiv duplicate check is unresolved.**
- On medRxiv, removing duplicates lowered 2026 non-COVID growth from 22% (v1; my round-1 check) to 16.4%, so the duplicates were concentrated in recent months.
- Until bioRxiv is checked, every bioRxiv benchmark is provisional:
  - "bioRxiv grew 1.53-fold";
  - "in levels bioRxiv grew more than the physics archives tested";
  - all of use vs output, including mathematics' 1.27;
  - C2, if duplicates differ by category.

**Fix.**
1. Reword (N7).
2. Report the direct comparisons with bioRxiv beside the departures from trend, with in-time calibration.
3. Name the counterfactual in every claim.
4. Restrict "experimental … included" to hep-ex against its 2015–2022 trend, and say that nucl-ex did not accelerate and that the result depends on the window.
5. Resolve the duplicate question before submission.

### N3. Use vs output is suggestive, not robust

**Location.** Abstract ("did not predict output: mathematics had the smallest rise and the largest acceleration"; "counts moved … independently of AI-assisted writing"); Results, H3 and use vs output; Discussion ("Four findings withstood the checks made"); Implications.

**Problem 1: one unit carries it.**
- Mathematics is the only group in which marker rise and acceleration clearly diverge.
- In biology they point the same way. Computational categories' markers rose more than wet-lab categories' in 2023 and 2024 (1.19, 0.99–1.43; 1.18, 0.98–1.42), as Kobak et al. found in PubMed, and computational output also grew more (C2 1.08).
- In physics, markers rose equally in 2024 (1.00), and the output contrast is fragile (1.06–1.14).
- So the pattern across the three fields is one inconsistent, one null and one weakly consistent. "Did not track" is fair for mathematics. "Independently of AI-assisted writing" is not supported.

**Problem 2: "rose by a similar factor" understates the biology result.**
- On annual rates, the computational/wet-lab marker difference-in-differences was +0.03, +0.04, −0.06 and +0.02 in 2019–2022 (SD 0.05 on the log scale), then +0.22 and +0.18 in 2023 and 2024 (my check, from `marker_tests.json` rates).
- Against that spread, 2024 has a centred z of about 2.9 (p ≈ 0.06 with 3 df). The OLS test gives p = 0.076.
- Neither test is significant. But the data show a larger rise in computational categories that is not significant, not a similar one.

**Problem 3: the OLS t intervals treat months as independent, and ignore year-level shocks.**
- In the arXiv theory/experiment difference-in-differences, the annual 2019–2022 values were −0.05, +0.15, +0.08 and −0.11 (SD 0.116 on the log scale).
- Independent monthly noise would give an annual SD of about 0.09, given the OLS SE of 0.10 for a year coefficient.
- The larger observed spread is consistent with year-level shocks, as in the main contrasts. Four years cannot pin down their size, and that is itself the problem.
- Calibrated against year-level variation, two results become borderline:
  - "experimental physics rose more than theory" in 2025–2026 (0.75);
  - mathematics/experiment in 2024 (0.75).

  For both, z is about −2.2 to −2.4, and p is about 0.02–0.10, depending on whether the year-level variance is treated as known or as estimated from four years.
- The companion's own reason for preferring OLS to autocorrelation-robust errors (they "came out about 2.5 times too narrow") is a symptom of the same few-period problem.

**Problem 4: the marker's sensitivity by field is unknown.**
- The list comes from PubMed and was filtered on bioRxiv and medRxiv. How often LLM editing of mathematical prose produces these words is not known.
- S4 Table's independent estimates (Lin and Zhu; Liang et al.) also rank mathematics low, which supports the ranking.
- A corpus-specific check would settle whether "smallest rise" means lower adoption or a less sensitive marker.

**Problem 5: the panel's interaction is not a pooled result.**
- The pooled interaction (0.0041, p = 0.034) is close to the arXiv-only one (0.0051, 7 clusters, two of them with experimental = 1). The bioRxiv-only interaction is 0.0011 (p = 0.53).
- With cluster-robust errors and identifying variation in so few clusters, the pooled p value is unreliable (Cameron, Gelbach & Miller 2008; MacKinnon & Webb 2020).
- The panel also includes 2025–2026, when, by the paper's own account, the markers had drifted.

**Fix.**
1. Rephrase as "output did not track a marker of AI-assisted writing; the clearest case is mathematics".
2. Restrict marker comparisons to 2024.
3. Calibrate the marker difference-in-differences against annual pre-period variation.
4. Run a corpus-specific excess-vocabulary check (Section 6, item 6).
5. Report the panel as descriptive, or use a wild-cluster bootstrap and the 2024 cross-section.

### N4. H2: what the symmetric decomposition can and cannot say

**Location.** Abstract ("in mathematics the top 1% of names more than tripled theirs"); Results, H2; Implications ("the most productive 1% of author names more than tripled their output"); Methods ("[top-1% and top-10% shares] do not move under proportional growth").

**What is right.** Ranking on combined output is the right null for "homogeneous proportional growth".
- Given an author's combined count, the split between the two years is binomial with the growth odds, so every class grows at the total rate.
- A simulation of my own confirms it, with Gamma–Poisson rates, fractional credit and an activity threshold, calibrated roughly to Q3 2025: under uniform ×1.80 growth the classes grow by +80.8%, +81.0% and +80.2%, against +80.4% in total.
- The pre-ChatGPT pairs supply the benchmark for ordinary heterogeneity.
- The rejection of homogeneous growth in mathematics is unambiguous.

**Problem 1: the top 1% is partly selected on its 2026 output.**
- Under heterogeneous growth, ranking on combined output puts names with large 2026 increases into the top class. The decomposition shows that growth became much more heterogeneous. It does not show that previously productive authors produced more.
- The data show the selection directly (my check, `heavy_producers.json`). First-quarter output per name of the top 1%, by pair of years:

  | Pair | Names in the top 1% | Fractional papers per name in the first quarter |
  |---|---|---|
  | 2023→2024 | 304 | 1.73 |
  | 2024→2025 | 333 | 1.64 |
  | 2025→2026 | 417 | **1.08** |

- The 2026 top 1% contains many names that were modest producers in Q3 2025. "The most productive 1% of author names more than tripled their output" reads as "the previously most productive", and the data do not show that.

**Problem 2: the concentration shares are not invariant under proportional growth.**
- With count noise and an activity threshold, the share of the top 1% of active names changes when everyone's rate is scaled.
- My simulation was crude: Gamma–Poisson rates (shape 0.25), team size 1 + Poisson(2), and 17,700 active names against 20,114 observed. Under uniform ×1.80 growth it gave:
  - a top-1% share rising from 4.67% to 5.25%, +0.58 pp (SD 0.09 over 30 replications);
  - active names rising by 46%, against 41% observed.
- The observed rise is 1.69 pp, so a material fraction of it may be mechanical.
- The 2019–2022 trend cannot remove that fraction, because the 2026 volume (+80%) is far outside the fitted range.

**Problem 3: the headline uses the window with the spike.**
- The Q3 figures (+266% against +57%) include the September surge.
- January–August gives +78% against +26% (total +33%), and July–August +135% against +49%. The abstract quotes the most extreme window.

**Problem 4: no verdict on H2 is stated.** On the evidence:
- "broad" is supported;
- "not from a few outliers" is supported, since the top 1% contributed 14% of the increase;
- "established researchers" was not tested.

"Partly supported" is the honest summary.

**Fix.**
1. Rank names on an independent window, for example Q3 2024 to Q2 2025, and decompose Q3 2025 → Q3 2026 growth by those classes. Both compared quarters then lie outside the ranking window, so regression to the mean affects them equally and nothing is selected on the outcome. Also report the share of the increase that came from names newly in the top 1%.
2. Run the uniform-scaling simulation for the shares.
3. In the abstract, use January–August or July–August figures, or give the range.
4. State the verdict on H2.

### N5. The funding checks: PubMed is over-read, and a medRxiv split is unreported

**Location.** Results, last paragraph of "Departures from trend…"; Discussion, explanation (ii).

**Problem 1: PubMed.**
- "After no comparable decline in 2019–2022" is inaccurate. Against 2022, the US/non-US ratio's one-year changes were:

  | Year | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
  |---|---|---|---|---|---|---|---|
  | Change | +6.2% | +2.5% | **−6.5%** | +2.3% | −2.6% | −4.9% | −3.1% |

  The 2021→2022 fall, a reversal of a COVID-era rise, is larger than either 2025's or 2026's.
- The two-year fall from 2024 to 2026 (−7.9%) is the largest two-year fall in the series, so a funding effect is plausible. But it is not established by intervals that again omit year-level variation.
- "Accounts for about 1.7 of the roughly 7 percentage points":
  - assumes that non-US output is the counterfactual for US output;
  - attributes part of a shortfall whose 2026 interval includes 1 (0.86–1.01);
  - attributes part of a shortfall that predates the shock (PubMed was 0.90 of trend in 2024).

**Problem 2: medRxiv.**
- The companion's `medrxiv_flags.by_year_jan_sep` already holds counts by corresponding-institution country.
- My check, all preprints including COVID-19, January–September:

  | Year | US growth | Non-US growth |
  |---|---|---|
  | 2025 | +20.9% | +14.9% |
  | 2026 | +17.7% | +10.1% |

  Against a 2023–2024 base, the US/non-US ratio was 1.03 in 2025 and 1.11 in 2026.
- On medRxiv, US output rose relative to the rest, the opposite of the simple funding prediction. Caveats:
  - the counts include COVID-19 preprints;
  - about 17% of preprints have no country;
  - the classifier was checked by an AI agent, on 150 records.
- The split bears directly on explanation (ii) and has not been reported.

**Fix.**
1. Report the medRxiv split, with its caveats.
2. Correct the PubMed sentence and calibrate it in time.
3. Present the attribution as an accounting exercise under a stated assumption.
4. Keep the prediction for bioRxiv, already stated in the Discussion, fixed before running it.

### N6. The pre-registered tests: design, implementation, deviations and what will make them credible

The plan has real strengths:
- paper-level measurement;
- held-out archives;
- codebooks fixed in advance;
- a sealed validation key;
- a decision rule with a "contradicted" outcome;
- listed sensitivity analyses;
- an exploratory component kept apart.

The problems below are fixable, but most must be fixed **before anyone reads a result**.

#### N6.1 Is the design sound?

**Class counts from samples: sound.**
- Monthly total × sampled class share is a design-unbiased ratio estimator within each stratum, and PPML accepts non-integer counts.
- The allocation samples more densely from 2025 (40 papers a month, against 15 before), whereas the estimand's precision depends mainly on the pre-period trend. Per archive, that is about 1,440 papers in 2017–2024 and 840 in 2025–2026. The choice is acceptable, but it should show up in the power calculation (below).

**A bootstrap that redraws the sample: sound for sampling error, silent on everything else.**
- Resampling papers within strata carries binomial sampling error into the intervals. It carries nothing from classifier error, which is a bias, not noise.
- The month-block bootstrap (`stats_nd_tests.py`) draws pre- and post-period blocks separately, which is a good choice. But the 21 post-period months are rebuilt from two 12-month blocks. That captures trend-parameter uncertainty and variation within the period. It does not capture a shock common to the whole post-period, or misspecification of linear trends extrapolated three to four years ahead.
- The single 2019 placebo needs pre-2019 data. On bioRxiv (from 2019) and medRxiv (from July 2019) it leaves a trend identified from 2022 and from within-year slopes in 2020–2021, so it carries no information.

**κ ≥ 0.60: a reasonable minimum, but not what protects this estimand.** Three problems:
- *Attenuation.* Non-differential misclassification pulls the ratio of rate ratios (RRR) towards 1.
  - Take an ND share of 0.40 and sensitivity = specificity = 0.85, which gives κ ≈ 0.69. A true RRR of 1.20 is then observed as 1.13.
  - The stated "expected MDE of about 1.15–1.20" (Deviation 2) therefore corresponds to true RRRs of roughly 1.23–1.31.
  - That expected MDE has no documented derivation in the scripts. The code computes the MDE after estimation as exp(2.8 × bootstrap SE), a rescaled standard error.
- *Differential misclassification over time.* This is the main threat. The hypothesis concerns the AI era, and an LLM classifier reading LLM-polished abstracts from 2025–2026 may classify them differently from 2018 abstracts. The validation sheet is stratified by period, which is good. Use it: report confusion matrices by period, and fix a rule now for what a difference between periods means.
- *Precision of κ.* With 100 papers per domain for bioRxiv and medRxiv, the SE of κ is about 0.07–0.08 (Fleiss, Cohen & Everitt 1969). A threshold applied to a point estimate is close to a coin flip near 0.60. Report κ with its interval, and per class.

**Batches are ordered in time.**
- `nd_frames.py` writes the classifier input sorted by paper key. For arXiv identifiers and bioRxiv/medRxiv DOIs, that order is close to chronological.
- `classifier_batches.py` splits the input in order into batches of 50.
- Each batch is one sub-agent run with no control of temperature. A batch therefore covers about one month, and batch effects load onto months. Any effect of context specific to batches of 2025–2026 abstracts loads onto the estimand.
- If classification has not started, shuffle across strata and periods before batching. If it has, re-classify a random subset in shuffled batches, as a diagnostic that does not replace the stored labels.

**Trends for bioRxiv and medRxiv are not credible counterfactuals.**
- The script identifies bioRxiv trends from 2019 and medRxiv trends from July 2019. Each unit × class pair has its own 2020–2021 indicator, so the trends rest on 2019 (for medRxiv, the server's first six months) and on 2022.
- This is the trend-adjusted estimator that the paper demoted for C2 (1.48, 1.06–2.07) because its counterfactual "is not credible". The computational/wet-lab log ratio fell every year to 2024 and then rose.
- A "supported" verdict for HN-bio could therefore come from the end of adoption alone.
- For medRxiv, Table 3 itself labels the server's trend "not interpreted".
- The samples already cover 2023–2024. A trend-free estimand, the 2025–2026 NN/ND log ratio minus that of 2023–2024, costs nothing.

**A funding shock acts in the direction of the hypothesis.**
- A US funding shock lowers output that needs new data (trials, new cohorts, wet-lab work) relative to secondary analyses. That has the sign HN-bio, HN-med and HN-dose predict.
- The corresponding-institution country is available on bioRxiv and medRxiv. A non-US sensitivity analysis, declared now, separates the two.

**Of the four confirmatory tests, only HN on the held-out arXiv archives is cleanly confirmatory:**
- Test A on bioRxiv rests on category-level patterns already examined in round 1, such as the bioinformatics acceleration and the wet-lab slowdown, and inherits the adoption and funding problems.
- Test A on medRxiv inherits the adoption problem.
- Test B is discussed under N6.2.

Declare this hierarchy before the results are read.

#### N6.2 Implementation findings to fix before any result is read

1. **Test A can never be "supported".**
   - `hn_like()` applies the HN rule: the pooled interval excludes 1 **and** the unit-specific RRR exceeds 1 in at least two units.
   - Test A is called with a single unit per server (`hn_like(..., "A-medrxiv", ["A-medrxiv"])`, and its strata are months: `nd_frame_counts_medrxiv.csv`). So the condition "at least two units" cannot be met.
   - The registered text ("as in §5–§7") is ambiguous for a single server.
   - Record a clarification now. For example, for Test A the rule reduces to the pooled condition. Or define categories as the units.
2. **Test B includes archives whose outcomes are known, and the hypothesis-generating archives.**
   - `nd_design.py` includes in Test B mathematics subcategories and the archives hep-th, hep-ph, gr-qc, nucl-th, hep-ex and nucl-ex.
   - §3 of the registration says that hep-ex and nucl-ex "are reported separately and never pooled with the confirmatory archives".
   - Test B's outcome is each category's departure from its own trend, for all its papers. That is already known for the six archives (for example nucl-ex 1.00, hep-ex 1.37 and nucl-th 1.58) and predictable for mathematics, whose subcategories inherit the archive's 1.48. Their ND shares are also predictable: near 0 for mathematics, high for the experimental archives.
   - The arXiv slope is therefore largely determined by what was known when the design was fixed. "Negative in at least two of three servers" then needs only one of bioRxiv and medRxiv, both confounded as above.
   - Declare now that confirmatory Test B uses only the held-out archives' subcategories, with the full set as a sensitivity analysis.
3. **One-sided permutation.** `dose_response()` computes a one-sided permutation p. The registration says only "permutation p < 0.05". State it.
4. **Unwired parts.** Test B and three of the six listed sensitivity analyses (dating by announcement, genres, more than 50 authors) are not yet called in `main()`. Run all of them as registered.
5. **Nothing seals the results.** The script prints the pooled results and the decisions, and writes them in plain text to `data/processed/stats/nd_tests.json`. Nothing keeps them from the coder.

#### N6.3 Are Deviations 1 and 2 acceptable, and adequately disclosed?

**Deviation 1** (estimation before validation) **is acceptable only with sealed results.**
- The safeguards blind the validation sheet, not the estimates.
- The coder originated the hypothesis. If the results are visible to them, they will know whether the results favour HN while coding, and κ depends partly on how literally a coder applies the codebook.
- Seal the estimates, by encryption or hash commitment, until κ is computed; log the first access. A second, independent coder on at least 100 papers, optional in the plan, should be made a condition. Inter-human κ also gives the ceiling against which the classifier's κ is judged.

**Deviation 2** (sampled classification; one run per paper) **is acceptable and was recorded before results.** Three points need correcting:
- *The classifier is not identified in the registration* ("[AUTHOR: record the model name and version]"). A registration that does not name its measuring instrument leaves room to choose among runs or models. Commit a hash of the model identifier now, and state the model in the paper.
- *"The author can revise this choice before results are reported"* must be deleted, or restricted to "before any estimate is computed". Under Deviation 1, estimates will exist before results are reported.
- *The manuscript's summary of the deviations* omits two things: the validation frame limited to Creative Commons-licensed papers on bioRxiv and medRxiv, and the unrecorded model.

**Two smaller points.**
- *Validation sampling.* The sheet draws a random day and then one paper from that day (`make_validation_sheet.py`), so papers posted on quiet days are over-represented. Weight κ by daily volume, or note the effect.
- *Provenance.* §1 of the registration says the 60 hep-ex records were "classified by one person". S2 Appendix says an AI agent classified them. Add a dated erratum; do not edit the timestamped text.

**Disclosure.** In outline, v2's Methods disclose both deviations adequately.

#### N6.4 What will make the tests credible

Before anyone reads a result:
1. **Seal the estimates and record the classifier.** Seal the estimates until κ is computed, and keep an access log. Commit a hash of the classifier's identity.
2. **Record a Deviation 3**, with a third-party timestamp: an OSF registration or a Zenodo snapshot, since git dates are author-controlled. It should fix:
   - (a) the decision rule for Test A;
   - (b) Test B's confirmatory category set;
   - (c) a family-wise rule across HN, HN-bio, HN-med and HN-dose. For example, Holm across the four, with no pooled claim about the refined hypothesis unless HN itself is supported;
   - (d) the trend-free estimand as a co-primary check for bioRxiv and medRxiv, with the rule that a verdict stands only if both estimands agree;
   - (e) the non-US sensitivity analysis for bioRxiv and medRxiv;
   - (f) a check for misclassification by period, and a misclassification-corrected sensitivity analysis (matrix method; Rogan & Gladen 1978);
   - (g) a power simulation built from pre-period data, including attenuation, with a stated smallest effect size of interest. The Limitations section's own Amdahl-type bound gives about 8–54%;
   - (h) what failure of κ in one domain means for Test B.
3. **Shuffle the classifier batches, or run the diagnostic** described in N6.1.
4. **After unsealing**, deposit the labels, prompts, sample identifiers, seeds, the validation sheet and its key. Report every test whatever it shows, including where it contradicts the exploratory INSPIRE results.

### N7. Framing: sentences that go beyond, or fall short of, the evidence

| Location | Current text | Problem | Suggested |
|---|---|---|---|
| Abstract | "those reporting new experimental results grew as fast as the rest" | Selective. Within hep-ex and nucl-ex: 1.00 (0.74–1.35). Across all six archives: 1.12 (0.94–1.35), 1.04–1.19 across variants, two of five excluding 1 | "…did not grow detectably more slowly than other papers within the experimental archives (ratio 1.00, 0.74–1.35); across all six archives, papers without new results grew somewhat faster (1.12, 0.94–1.35)" |
| Abstract | "experimental particle physics included and not because of reviews, proceedings or white papers" | Mixes trend windows; the genre analysis found no experimental departure (N2) | "…including hep-ex (1.37 of trend), although not nucl-ex; research articles alone departed as much as all papers in mathematics and in particle and nuclear physics as a whole" |
| Abstract | "did not predict output: mathematics had the smallest rise and the largest acceleration" | One unit; marker sensitivity by field unknown | "rose least in mathematics, which accelerated most" |
| Abstract | "in mathematics the top 1% of names more than tripled theirs" | Selection on 2026 output; window with the spike (N4) | "…the 1% of names with the highest combined output in the two periods grew by 78–266%, depending on the window, against 26–57% for the bottom 90%" |
| Abstract | "counts moved unevenly and independently of AI-assisted writing" | "Independently" is not shown (N3) | "…counts moved unevenly and did not track a marker of AI-assisted writing" |
| Abstract | "physics fell to 1.06 without planning white papers in its 2022 base" | The lowest clean base; 2017–2019 gives 1.11 | "…1.06–1.11 with bases free of planning white papers" |
| Abstract | Holm p values first, placebo p values second | Placebos are declared primary | Lead with the placebo p values |
| Introduction | "as a falsification test" | With an MDE of about 1.21–1.25, the tests cannot falsify moderate effects | "as a test" |
| Methods | "The pre-specified estimate is exp(β₂₀₂₆) … relative to 2022" | Contradicts the Deviations section | "The primary estimate as run (a deviation from the planned multi-year baseline; Deviations)" |
| Results | "excludes increases of more than 14%" (C3) | Read from DK intervals that the paper calls too narrow | "…under within-year uncertainty only" |
| Results | "rose by a similar factor" (H3, biology) | Point estimates 1.19 and 1.18 (N3) | "rose 18–19% more in 2023–2024, a difference that was not significant" |
| Results | "after no comparable decline in 2019–2022" | A fall of 6.5% from 2021 to 2022 (N5) | Correct it, and add the medRxiv split |
| Discussion | "Four findings withstood the checks made" | Findings 2 and 3 did not withstand the checks proposed here | "Two findings are robust (markers rose everywhere; growth was broad but concentrating); two are suggestive (output did not track the marker; arXiv accelerated against its own trend while bioRxiv kept its pre-2023 pace)" |
| Discussion | "…which suggests that the differences between fields reported by Qi et al. partly reflect servers" | Infers absence from a null of low power | "…so the differences between fields reported by Qi et al. could reflect servers as much as computational intensity" |
| Implications | "This supports, at the strength the data allow, the view…"; "counts can no longer be compared … as before" | The design cannot attribute the change | "This is consistent with the view…"; "comparisons of counts across fields and years now need care" |
| Conclusions | "experimental archives and research articles included" | nucl-ex did not accelerate; window dependence | "hep-ex included (nucl-ex not)" |

---

## 5. Minor issues

1. **Inconsistent companion outputs.** In `results.md` (P1c table) and `round1_tests.json`, C3 is still the value from before the duplicate correction: 0.99 (0.88–1.10), with 2026/2025 1.08 and year-shock z −0.19. `within_field_tests.json` and Table 1 use the corrected value, 1.01. S5 Table is built from these files, so regenerate them before assembling it.
2. **A misplaced placebo p.** In "Within-field contrasts (H1)", the physics paragraph ends with "1.03 (0.91–1.16) against 2017–2019 (placebo p = 0.70)". The placebo p belongs to the 2022-base estimate (1.10). No placebo was computed for the other bases. Compute one if the placebo is primary.
3. **"Pre-specified" is used for the 2022 reference** in Methods and in Table 1's title. Use "primary as run", and keep "pre-specified" for the groups and contrasts.
4. **The benchmark sentence.** "Before ChatGPT's release the classes' growth differed by at most nine percentage points" holds for all names. For namesake-robust names, 2020→2021 differed by 14 points (−15.1% against −0.8%).
5. **Variant ranges.** "By 78% to 211%, against 26% to 49%" covers variants that change one thing at a time. Combined variants fall outside: namesake-robust January–August gives +63% against +22%, and established names January–August +76% against +18%. Say so, or give the full range.
6. **MDE rows.** The MDEs use within-year SEs. Label them "lower bounds".
7. **A placebo for C3.** C3 has none. An in-space placebo built from flags for other dataset names, or from random term sets of matched prevalence, is feasible. Otherwise, state that C3's interval is within-year only.
8. **Methods** says the classifier works "from title and abstract". For arXiv, the registered prompt also uses the comments.
9. **The synthetic-control gap.** "11.9%" is exp(mean monthly log gap) − 1, with a mean log gap of 0.113. Say so: Nee et al. may report a different transform.
10. **The archive ranking.** Rank p has a floor of 1/18. The top ranks go to archives with falling pre-2023 trends, as the text notes. A ranking on standardised departures (departure/SE) would complement it.
11. **Break tests.** "Showed no slope break" (cs, bioRxiv, C1) → "no detectable slope break". These tests have little power for breaks near the end of the sample.
12. **The pooled-base interval for C2** (0.80–1.22) is evidence that the 2022-base DK interval omits year-level variance. Say so in the Results; it is the best single demonstration in the paper.
13. **The INSPIRE ratio interval** combines separate fits. Shared shocks make it conservative, while omitted year-level variance makes it optimistic. A stacked model with month effects, as in the main contrasts, would remove both problems.
14. **Fig 2D and Table 1.** Add the rank-based in-time p beside the DK bars (N1).
15. **An undated plan.** The decision rule for H1 and the leave-one-out criterion are both marked "after the fact". Also date the in-space placebo's promotion to primary inference. It is conservative, so this is a matter of record, not of concern.

---

## 6. Requested analyses, ranked by information value

Each item names what it decides. Cost is low for all but item 6.

1. **Fix and seal the pre-registered tests before reading them** (N6.4).
   - *What:* the Test A rule, Test B's confirmatory set, the family-wise rule, the trend-free estimand, the non-US sensitivity analysis, the check of misclassification by period, a power simulation, shuffled batches or the diagnostic, sealing, and the hash of the model.
   - *Decides:* whether the only confirmatory evidence the paper will contain can be interpreted at all.
2. **The bioRxiv duplicate check.**
   - *Decides:* every bioRxiv benchmark, including "bioRxiv grew more than physics in levels" and mathematics' 1.27 gain on bioRxiv. On medRxiv, the same correction moved 2026 growth by about 6 points.
3. **Dating by first-version submission, with January–August versions of every 2026 estimate** (pending).
   - *Why:* the mathematics synthetic-control gap was near zero until April 2026 and reached 0.31 and 0.40 log points in August and September. Mathematics' H2 contrast shrinks from +266%/+57% (Q3) to +78%/+26% (January–August).
   - *Decides:* how much of the 2026 arXiv acceleration reflects holds by moderators and the timing of announcements.
4. **Rank-based in-time calibration, with the identical estimator, for every headline comparison** (N1).
   - *Scope:* C1–C3 levels and the 2026/2025 ratios; arXiv groups against bioRxiv; the marker difference-in-differences; PubMed US/non-US.
   - *Decides:* which "accelerations" are unusual for their series. My checks suggest only mathematics' is.
5. **H2: classes ranked on an independent window, and the uniform-scaling simulation for the concentration shares** (N4).
   - *Decides:* whether "the top 1% tripled" describes established producers or bursts, and how much of the 1.7-point rise in the top-1% share is mechanical.
6. **Marker sensitivity by field.**
   - *What:* a corpus-specific list of excess words (Kobak et al.'s method applied within arXiv mathematics and physics, with 2019–2022 as the baseline), or a distributional estimator. Compare the rises in 2024.
   - *Decides:* whether mathematics' small rise is lower adoption or lower marker sensitivity, which is the premise of the use-vs-output headline.
7. **Structure-matched placebos** (pending), with C1's reference set drawn from physics archives only. State the floor (for example, 1/15 for the 15 four-against-two splits of the six particle and nuclear physics archives).
   - *Decides:* the declared primary inference, which is in the abstract.
8. **The funding question.**
   - *What:* report the medRxiv split; run the bioRxiv split with its prediction stated first; add pre-trends to PubMed.
   - *Decides:* explanation (ii), the only candidate explanation with data already in hand.
9. **For the record.**
   - *What:* the planned-specification model (required, but of little information value: the approximate values already settle it); validation of the Snowmass keyword rule against INSPIRE's tags; link completeness in INSPIRE by year.
   - *Decides:* the transparency record and two measurement questions.

**Lower priority now.**
- The AI/ML split of bioinformatics and the removal of COVID-19 from bioRxiv categories. They matter only if C2 is to be interpreted, which the paper rightly no longer does.
- Run them for completeness. They cannot change the verdict.

**Not requested:**
- Rambachan–Roth bounds;
- fixed-b critical values for intervals that are labelled descriptive;
- further genre or keyword variants;
- new groupings of archives or categories;
- further break tests;
- any re-analysis of the pre-registered tests after unsealing, beyond what is declared beforehand.

---

## 7. Strengths

**Honest reporting of H1.**
- "The prediction was not supported" leads the abstract's findings, and the Conclusions match.
- No contrast is rescued by a new grouping, and the post hoc variants are labelled.

**Table 1** is a model of a specification summary: base, acceleration, placebo, leave-one-out and negative controls side by side, with a one-word reading for each contrast.

**A candid Deviations section.**
- It says that the plan's pre-trend diagnostic became the primary estimate.
- It reports what the planned bases would give.

**The right inferential stance.** Placebos are primary, and the DK intervals are labelled as within-year in the text, the table notes and the figure legends.

**The symmetric decomposition for H2.** It is an elegant and correct null, which my simulation confirms, benchmarked on pre-ChatGPT years and reported with sensitivity variants. It replaced a fixed-threshold measure that could not test anything.

**Checks reported whatever they showed.**
- The Snowmass removal weakened C1, and it was reported.
- The duplicate correction changed medRxiv's growth story, and it was reported.
- The INSPIRE analysis was run by a registered rule without AI.
- The year-shock ratio for C3 was recomputed in the open, and the slope change that could not be recomputed is marked as such.

**A pre-registration with paper-level measurement and held-out archives.**
- Codebooks were fixed in advance and the validation key is sealed.
- The deviations were recorded before any estimate.
- An explicit "contradicted" outcome is defined.

These are the right instruments; N6 is about making sure they work as intended.

**Disclosure control** for author-level statistics, and **[AUTHOR], [ANALYSIS PENDING] and [RECHECK] markers** that make the state of the manuscript legible.

**Accurate numbers.** Every number I checked against `stats/` matches, apart from the items noted in Section 1.3: the stale P1c table, one misplaced placebo p and one inaccurate sentence on PubMed.

---

## References cited in this review (new in round 2)

- Cameron AC, Gelbach JB, Miller DL. Bootstrap-based improvements for inference with clustered errors. Rev Econ Stat. 2008;90(3):414–427.
- Fleiss JL, Cohen J, Everitt BS. Large sample standard errors of kappa and weighted kappa. Psychol Bull. 1969;72(5):323–327.
- MacKinnon JG, Webb MD. Randomization inference for difference-in-differences with few treated clusters. J Econom. 2020;218(2):435–450.
- Rogan WJ, Gladen B. Estimating prevalence from the results of a screening test. Am J Epidemiol. 1978;107(1):71–76.

Methods cited in round 1 and used again here (Andrews 2003; Conley & Taber 2011; Gelman & Stern 2006; Rambachan & Roth 2023) are listed in my round-1 review.
