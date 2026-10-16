# Review of "Generative AI is eroding publication counts as a measure of scientific work: evidence from 1.9 million preprints" (draft v1)

**Reviewer 1: statistics and causal inference.** Round 1, 16 October 2026.

**Materials consulted.**
- The manuscript, `paper/plos_one/draft_v1.md`.
- `paper/figures/`: `within_field_quarterly.csv`, `arxiv_math_prolific_robustness.json` and `README_companion_analysis.md`.
- The companion branch `claude/happy-lovelace-wqek9b`, commit cb56c25: `data/processed/*.csv`, the monthly aggregate counts in `data/raw/`, and `scripts/*.py`.
- After they arrived, the companion's formal results, commit 37b4b11: `paper/plos_one/stats/methods.md`, `results.md`, `within_field_tests.json` and `field_tests.json`.

**How this review was written.**
- **Sections 1–6** began as a Stage-1, Registered-Report-style assessment of the analysis plan and of the descriptive results already in v1.
- **The formal estimates** arrived while I was writing. They confirm the main concerns, so I have cross-referenced them in Sections 2–6 and added **Section 7**, on how to reframe the paper.
- **"My check"** marks a quick computation from the companion's aggregate files: pre-period diagnostics, January–September totals and small simulations. These checks are not substitutes for the formal models.
- I did not modify the manuscript.

---

## 1. Summary

**Question and data.** The manuscript asks where scientific output has accelerated since generative AI became widely available. It uses counts of new preprints on arXiv (2016–September 2026), on bioRxiv and medRxiv (2019–2026), and on three OSF social-science servers.

**H1.** H1 ("acceleration is concentrated where the work beyond writing is also cheap") is tested with three within-field contrasts:
- theory against experiment archives in physics;
- computational against wet-lab categories on bioRxiv;
- medRxiv preprints that name widely reused public datasets against the rest.

Each contrast is planned as a confirmatory ratio of rate ratios for 2026 against a pre-2023 baseline. It is supported by event studies, placebo dates, negative controls, leave-one-out estimates and a minimum detectable effect.

**H2 and H3.**
- H2 ("the increase is broad, not a few outliers") is examined through the share of arXiv mathematics papers with an author name that has five or more papers in the quarter, under several namesake-robust variants.
- H3 (AI-assisted writing is widespread across fields) rests on published estimates, with a marker analysis planned.

**Framing.** v1 reports descriptive growth figures. Its title and Conclusions argue that generative AI is eroding publication counts as a measure of scientific work.

## 2. Overall assessment and recommendation

**Strengths.**
- The question matters, and the data assembly is careful. Every descriptive number I re-computed from the companion files reproduces, including the medRxiv figures marked [RECHECK].
- The plan is more disciplined than most bibliometric work:
  - contrasts and groups fixed in advance;
  - a declared confirmatory family;
  - negative controls, leave-one-out estimates and a minimum detectable effect;
  - a frank statement that the descriptive counts were seen first;
  - an unusually candid process record.

**Weaknesses.** As a test of the hypotheses, the plan had structural weaknesses that I would have asked to be fixed at Stage 1. The formal results show that they matter.

- **H1.**
  - *Estimand.* The planned estimand, the 2026 level against a multi-year baseline, does not match a hypothesis about acceleration.
  - *Pre-trend.* The biology contrast has a strong differential pre-trend.
  - *Uncertainty.* The planned uncertainty (count models with autocorrelation-robust errors on two aggregated series) ignores the two dominant sources of uncertainty: year-level shocks to the contrast, and heterogeneity between categories.
  - *Groups.* The groups are archive and category labels that measure "experimental" only loosely.
  - *The analysis as run.* The companion fixed the model specification: Poisson pseudo-maximum likelihood (PPML) with month fixed effects. However, it used 2022 alone as the reference year. This departs from the written plan, and for C1 and C2 it is close to the most favourable pre-period choice.
  - *Results.* None of the three contrasts supports H1 robustly:

    | Contrast | Estimate | What undermines it |
    |---|---|---|
    | C1, physics | 1.14 [1.00, 1.30], Holm p = 0.11 | Carried by one small archive; typical of arbitrary archive pairs |
    | C2, biology | 1.08 [1.03, 1.14] against 2022 | About 1.02 against the plan's baseline, 0.87 against 2019, and 0.93 without bioinformatics |
    | C3, medicine | 0.99 | — |
- **H2.** The heavy-producer share rises mechanically with volume and with namesake collisions.
  - Under simple models, a uniform rise in every author's output reproduces the observed sixfold rise in names with five or more papers.
  - The measure therefore cannot separate "broad" from "a few outliers".
  - "Many established authors" (Conclusions) is not what the data show.
- **H3.** Published estimates from other corpora, mostly for 2023–2024, cannot show that differences in 2026 growth are "not explained" by differences in AI adoption.
- **Causation.**
  - The design has no measure of exposure.
  - Concurrent 2025–2026 shocks (funding, arXiv rules and moderation) are not neutral with respect to experimental intensity.
  - The design can therefore describe where counts changed, but it cannot attribute the change to AI or to the cost of non-writing work.

**Criterion 4.** Three parts of the manuscript do not meet PLOS ONE criterion 4 (conclusions supported by the data):
- the title ("Generative AI is eroding…");
- the abstract's "Output has grown fastest where the work beyond writing is also cheap" and "without any misuse";
- the Conclusions.

**What is worth publishing.** The descriptive and exploratory findings deserve publication, and a pre-specified test that fails is itself a result. They are:
- a broad acceleration across nearly all arXiv archives in 2025–2026, including experimental hep-ex;
- no detectable acceleration on bioRxiv, medRxiv or PubMed;
- a sharp shift in output per author name in arXiv mathematics.

**Recommendation: major revision.** In its current framing I would recommend rejection under criterion 4. A version that does all three of the following could meet PLOS ONE's criteria:
- reports the pre-specified tests as not supporting H1;
- presents the field-level and author-level results as exploratory and descriptive;
- fixes the estimand and the inference (M1, M2 and M5).

Section 7 sets out how.

---

## 3. Major issues

### M1. The estimand does not match H1, and the confirmatory estimate as run uses a different reference period from the plan

**Location.** Methods, *Statistical analysis*, "Rate ratios" and "Event study" (draft lines 155–157); Table 4; companion `methods.md`, "Main model".

**Problem 1: a level contrast for a hypothesis about acceleration.** H1 says that acceleration, a change in growth, is concentrated in non-experimental work. The plan's exp(θ₂₀₂₆), however, is a level contrast: 2026 against the average of a long baseline (2017–2022 for arXiv, 2019–2022 for bioRxiv). It therefore absorbs every pre-existing difference in drift between the groups. Two consequences follow:
- *In biology the contrast cancels itself out.*
  - The January–September log ratio of computational to wet-lab preprints fell every year from 2019 to 2024 (−0.89, −1.08, −1.14, −1.15, −1.17, −1.20), then rose (−1.14 in 2025, −1.05 in 2026) (my check, `within_field_quarterly.csv`).
  - A level contrast against 2019–2022 averages the fall with the rise. It ends up near 1 whatever happened in 2025–2026.
- *In physics, secular trends look like 2026 effects.*
  - Archive pairs have secular trends: gr-qc grew relative to nucl-th by about 5% a year from 2016 to 2025.
  - Measured against the plan's baseline, the January–September ratios for the negative-control pairs gr-qc/nucl-th and hep-ex/nucl-ex are 1.27 and 1.61. Measured against 2023–2024, they are 0.98 and 1.14 (my check).

**Problem 2: the reference period was changed.**
- The plan defines the confirmatory quantity against the multi-year baseline and uses the event study, with 2022 as reference, as the pre-trend diagnostic.
- The companion reports the 2026 event-study coefficient, relative to 2022, as the confirmatory estimate.
- Where 2022 falls in each contrast's pre-period range:
  - *C1:* 2022 is the lowest theory/experiment year of 2015–2022. Every other pre-period coefficient is between 1.00 and 1.25 relative to it.
  - *C2:* 2022 is near the bottom (2019 = 1.24, 2020 = 1.04, 2021 = 0.99).
  - *C3:* 2022 is at the top.
- What each estimand gives:

  | Estimand | C1 | C2 | C3 |
  |---|---|---|---|
  | Plan's baseline: average of the companion's own event-study coefficients over the plan's baseline years | ≈1.05 | ≈1.02 | ≈1.03 |
  | 2019 as reference (companion) | 1.05 | 0.87 | 0.98 |

**Why it matters.** The only contrast with a Holm-adjusted p below 0.05 is C2 (p = 0.0095). That result depends on a reference period other than the one written in the plan, and close to the one most favourable to H1. This is exactly the forking path that a confirmatory label is meant to close (Gelman & Loken 2014).

**Fix.**
1. **Report the planned quantity as confirmatory.** Report the quantity defined in the plan as the confirmatory estimate. Disclose the change to 2022, with its rationale and timing, and show both.
2. **Show the whole path, not one number.** Replace the single number with the full event-study path and a one-table specification summary for C1–C3 (Section 7.1). The summary should cover references of 2019, the plan's baseline, a non-COVID baseline, 2022 and 2023–2024, and the trend-adjusted estimate. Readers should be able to see that the sign of C2 depends on the reference.
3. **Add an estimand that matches "acceleration".** If H1 keeps the word, add an estimand that measures it: the change in the differential growth rate. Either of these would do:
   - the 2026 coefficient minus the mean of 2023–2025, a second difference that does not depend on the pre-2023 reference;
   - the 2026 departure from a group-specific trend fitted to non-COVID pre-period years.

   Report either with the sensitivity analysis of Rambachan & Roth (2023).
4. **Treat COVID-19 the same way in every contrast.** Either exclude March 2020 to December 2021 from every baseline, or remove COVID-19 preprints from the bioRxiv series as from medRxiv (M3).

### M2. Model specification and inference: the confidence intervals do not measure the uncertainty that matters

**Location.** Line 155 (Poisson or negative binomial, Newey–West errors, moving-block bootstrap); companion `methods.md`, "Main model" and "Cross-checks".

**Problem 1: the plan's model omits time fixed effects.**
- The plan's model has calendar-month effects and four period effects, all common to both groups. Common shocks, and the common trend within the baseline, therefore stay in the residuals.
- I fitted this specification to pre-period data only, with no post-2022 terms, so that no treatment effect was estimated (my check):

  | Pre-period sample | Pearson dispersion | First-order residual autocorrelation |
  |---|---|---|
  | Physics, 2017–2022 | 4.6 | 0.43 |
  | Biology, 2019–2022 | 24 | 0.62 |

**Problem 2: the executed model fixes the specification.**
- The companion's model is PPML with month fixed effects λ_t and group-specific calendar-month effects.
- With two groups, this is equivalent to a binomial model for group A's share of the pair's monthly total.
- It absorbs every common shock and is consistent whatever the variance (Santos Silva & Tenreyro 2006; Wooldridge 1999).
- A negative binomial model is not needed, and with many fixed effects it is not robust to misspecified variance. The Methods should describe the model that was actually run.

**Problem 3: overdispersion remains, so robust errors are required.**
- Extra-Poisson variation remains after month fixed effects. In the pre-period (my check), Pearson dispersion is 2.5–3.2 in physics and 2–5 in biology.
- Model-based Poisson standard errors would therefore be 1.5–2.3 times too small, so robust errors are needed.

**Problem 4: seasonality.**
- Group-specific month effects are right.
- With seasonality common to both groups, comparing a January–September 2026 window with full-year baselines would have caused only a small bias here. The January–September share of annual output was:
  - 0.720 for theory against 0.717 for experiment;
  - 0.739 for computational against 0.745 for wet lab.
- The larger issue is the residual variance.

**Problem 5 (the main one): what Driscoll–Kraay and Newey–West errors measure.**
- The model includes group × year dummies, so the residuals are deviations from each year's mean.
- The autocorrelation-robust estimator therefore measures serial correlation within years. It does not measure how much the yearly means themselves vary.
- "Is 2026 unusual?" is a question about that year-to-year variation in the group ratio.
- The pre-period coefficients show that this variation is real and that the intervals do not cover it:
  - 4 of the 13 pre-2022 year coefficients have p < 0.05 (C1 in 2020 and 2021; C2 in 2019; C3 in 2020), where 0.65 would be expected.
  - These deviations have explanations (COVID-19; the spread of bioRxiv). That is the point: explained year-level shocks happen, and the 2026 interval leaves no room for one.
- This is the classic problem of difference-in-differences with few groups and correlated group-period shocks (Bertrand, Duflo & Mullainathan 2004; Donald & Lang 2007).

**Problem 6: too few effective observations for the 2026 coefficient.**
- β₂₀₂₆ is identified from nine months against twelve reference months.
- With two series, the Driscoll–Kraay estimator reduces to a Newey–West estimator on a single score series. With a 12-lag Bartlett kernel, the variance for that coefficient rests on one or two kernel windows.
- Normal critical values are therefore too liberal (Kiefer & Vogelsang 2005; Lazarus et al. 2018).
- The moving-block bootstrap resamples the same within-year residuals, so it is not an independent check. For C1 it gives 1.11 [1.03, 1.20] against 1.14 [1.00, 1.30].

**Problem 7: aggregation hides heterogeneity between categories.**
- Aggregating each group into one series treats the mix of categories as fixed.
- Heterogeneity between categories, which the companion's in-space placebos show to be large, therefore never enters the interval.

**Why it matters.**
- The time-series intervals make C2 look decisive (Holm p = 0.0095). Yet 20% of random splits of the wet-lab categories diverge as much.
- They make C1 look nearly significant. Yet 61% of arXiv archive pairs diverge at least as much.

**Fix.** Make placebo-based inference primary and the robust intervals secondary:
1. **In-space placebos:** reassignments matched to the structure of each contrast (M4; Section 7.2).
2. **In-time placebos:** apply the identical estimator to each pre-period year against the same reference. This gives the empirical distribution of year-level departures. State the floor on the p-value: with six non-COVID reference years it is 1/7.
3. **A parametric version:** a random group × year effect whose variance is estimated from the pre-period years. For C1, a prediction interval built from the companion's own non-COVID pre-period coefficients gives z ≈ 2.2 with five degrees of freedom (p ≈ 0.08). Including the COVID years, z ≈ 0.6 (my check).
4. **Robust intervals as secondary:** keep the Driscoll–Kraay intervals, label them "within-year uncertainty", and use fixed-b or small-degrees-of-freedom critical values.

### M3. Parallel trends fail in biology, and the 2026 movement in C2 is mainly a wet-lab slowdown

**Location.** Results, "Computational and wet-lab biology" (line 212); Data sources (line 121); Robustness, "COVID-19" (line 182); companion results for C2.

**Problem 1: a strong differential pre-trend.**
- Relative to 2022, the 2019 coefficient is 1.24 [1.14, 1.36] (companion).
- The January–September ratio fell every year until 2024.
- This reflects the late adoption of bioRxiv by wet-lab fields and the 2020 surge of COVID-19 work in wet-lab categories (immunology, microbiology).
- The counterfactual is not identified: estimates for 2026 run from 0.87 (2019 reference) to 1.48 (trend-adjusted).

**Problem 2: COVID-19 is treated asymmetrically.**
- COVID-19 preprints are removed from medRxiv but kept in bioRxiv.
- The bioRxiv adjustment rests on a read of May–June 2022 only, when 23% of immunology and 11% of microbiology preprints were still about COVID-19 (`data/raw/biorxiv_covid_sample_2022.csv`).
- That sample says nothing about 2020–2021, which fall inside the planned baseline.

**Problem 3: the 2026 change in C2 is a broad slowdown with one exception, not a computational acceleration.**
- From 2025 to 2026 (January–September), computational growth barely changed (+19.8%, then +18.5%).
- That stability is itself a composite:
  - bioinformatics accelerated (+21.9% to +26.8%);
  - genomics slowed (+15.4% to +6.9%);
  - systems biology slowed (+20.6% to +5.1%).
- Wet-lab growth fell from +12.7% to +8.2%. Growth fell by more than three percentage points in eight of the twelve wet-lab categories, for example:
  - cancer biology, +22.5% to +5.9%;
  - developmental biology, +5.2% to −5.3%;
  - immunology, +15.2% to +7.1% (my check, `biorxiv_categories_growth.csv`).
- A slowdown concentrated in costly experimental work is what a shock to funding or staffing would produce, and 2025 had such shocks. For example, a JAMA research letter, as reported at https://www.hpnonline.com/regulatory/news/55289345/newly-published-study-quantifies-types-of-grants-terminated-by-nih-since-late-february, counted 694 NIH grants terminated between 28 February and 8 April 2025, worth $1.81 billion.
- Within-field differencing removes only shocks that hit both groups in proportion. Funding shocks fall along the experimental axis, the same axis as H1.

**Why it matters.** C2 is the only contrast with Holm p < 0.05.

**Fix.**
1. **Rambachan–Roth sensitivity.** Report the sensitivity analysis of Rambachan & Roth (2023), under relative-magnitude and smoothness restrictions, with breakdown values.
   - 2026 is four years after the 2022 reference, so year-to-year violations of the size seen in 2019–2021 would add up to more than the estimate.
   - I expect the breakdown values to be small.
   - Pre-trend tests alone are not enough (Roth 2022).
2. **Remove COVID-19 from bioRxiv.** Remove COVID-19 preprints from the bioRxiv series, using titles and abstracts from the details endpoint as was done for medRxiv.
3. **Test the funding explanation directly.**
   - The bioRxiv details endpoint returns `author_corresponding_institution` (verified at https://api.biorxiv.org/), so the contrast can be split into US and non-US corresponding institutions.
   - A funding shock predicts a wet-lab slowdown concentrated in preprints with US corresponding institutions.
   - The AI-cost mechanism predicts similar contrasts in both.
   - Write the prediction down before running the analysis.
4. **Describe C2 as it is:** a 2025 acceleration in bioinformatics, followed by a 2026 slowdown in most other categories.

### M4. The contrasts are weak proxies for "the cost of work beyond writing", and the negative controls and leave-one-out estimates need restating

**Location.** Groups for the within-field contrasts (lines 135–139); Negative controls (line 161); Leave one out (line 163); Results (lines 208–218).

**Problem 1: physics.**
- The two experimental archives diverge from each other more than the contrast does: hep-ex against nucl-ex is 1.39 [1.19, 1.64], against 1.14 for C1 (companion).
- Two of the six theory-archive pairs diverge as much as C1: hep-th/gr-qc 0.87 and hep-ph/gr-qc 0.85.
- hep-ex accelerated:
  - it grew 14.2% in January–September 2026, above the theory group's 2017–2025 maximum of +5.9% (my check);
  - it stood 1.37 times above its 2015–2022 trend, against 1.28 for hep-th and hep-ph (companion).
- C1 is carried by nucl-ex: +1.8% growth on 346 papers in January–September 2026. Without nucl-ex, C1 is 1.03.
- The labels are also impure:
  - gr-qc contains gravitational-wave data analysis by large collaborations;
  - hep-ph includes phenomenology fitted to experimental data;
  - hep-ex output follows the review cycles of large collaborations.

**Problem 2: biology.**
- Bioinformatics was 63% of the computational group in 2026. Without it, C2 is 0.93 [0.89, 0.97] (companion): genomics and systems biology grew more slowly than the wet-lab categories.
- If the mechanism were the cost of non-writing work, dropping one computational category should not reverse the sign.
- Growth in bioinformatics may reflect AI as a research topic, which the manuscript itself notes (line 286).

**Problem 3: medicine.**
- The comparison group, "all other medRxiv preprints", is itself largely non-experimental: registries, electronic records, cohorts, modelling and systematic reviews.
- The contrast therefore separates named datasets from other secondary-data research, for which H1 predicts little difference.
- C3's null result (0.99 [0.88, 1.10]) is informative about the dataset flag but is not a strong test of H1.

**Problem 4: negative controls.**
- H1 predicts no divergence between theory archives only if the effect is the same for every archive on one side of the contrast.
- A single pair cannot calibrate the main contrast (compare Lipsitch et al. 2010 on what makes a valid negative control).
- Under a level estimand, secular trends dominate the comparison (M1).
- The companion's in-space placebo distributions are the right construction.

**Problem 5: leave-one-out estimates.** They are not hypothesis tests, and adjusting them with Benjamini–Hochberg (line 153) has no meaning.

**Why it matters.** The contrasts were meant to hold field conditions fixed while varying the cost of experiments. As built, they also vary archive identity, collaboration structure and topic, and each result depends on a single component.

**Fix.**
- Report each contrast for what it is:
  - C1: inconclusive, and dependent on nucl-ex;
  - C2: dependent on bioinformatics;
  - C3: a weakly targeted null.
- State a robustness criterion for leave-one-out before applying it, for example "no single exclusion moves the estimate across 1". C1 and C2 both fail it.
- For any prospective test, measure experimental intensity in pre-period text or at the level of individual papers, not by archive label.

### M5. Multiple testing: there is no decision rule for H1, and the false-discovery adjustment is applied to the wrong analyses

**Location.** Line 153; Table 4 note; companion `methods.md`, "Multiple comparisons".

**Problem 1: no rule turns three contrasts into a verdict on H1.**
- If H1 needs support in all three fields (an intersection–union test), no adjustment is needed and H1 fails (Berger & Hsu 1996).
- If H1 counts as supported when any one field supports it (a union–intersection test), family-wise control is needed. Holm's method (Holm 1979) is fine here and uniformly more powerful than Bonferroni. Only C2 passes, and C2 fails the plan's own robustness logic (M1, M3, M4).

**Problem 2: intervals and p-values do not match.** The plan specifies Bonferroni-adjusted 98.3% intervals, but the companion reports Holm p-values with unadjusted 95% intervals.

**Problem 3: the larger multiplicity is left untouched.**
- Holm and Bonferroni handle multiplicity across the three tests.
- The bigger multiplicity is across specifications: reference period, groupings and windows. Neither method addresses it.
- The remedies are the specification table (M1) and placebo-based inference (M2).

**Problem 4: Benjamini–Hochberg on falsification tests works against the paper's purpose.**
- Line 153 applies Benjamini–Hochberg adjustment to the negative controls and placebo tests.
- These are falsification tests: a missed signal favours the author's claim.
- Adjusting them makes problems less likely to be flagged.

**Problem 5: the direction is not addressed.** H1 is directional, but the plan does not say what happens if an estimate is significantly below 1. That outcome is not hypothetical: C2 against 2019 is 0.87 [0.80, 0.95].

**Fix.**
- State the decision rule for H1. I suggest per-field claims under Holm control, plus an explicit statement that H1 as a general claim needs support in all three fields.
- Report Holm p-values together with Bonferroni-adjusted intervals.
- Report negative controls and placebos unadjusted, as distributions, against a criterion stated in advance.

### M6. Power: the physics and medicine contrasts could not detect plausible effects, and the minimum detectable effect is computed at the wrong level and from the wrong variance

**Location.** Line 165; Table 4 note; companion "Precision".

**Problem 1: wrong significance level.**
- The companion's minimum detectable effects (MDEs; 1.21, 1.08 and 1.17 for C1–C3) use α = 0.05.
- The confirmatory family uses Holm's method, whose first step is at α/3. At α/3 the same standard errors give 1.25, 1.09 and 1.20 (my check).

**Problem 2: wrong variance.**
- The MDEs use Driscoll–Kraay standard errors, which leave out year-level variation (M2).
- Using the standard deviation of the January–September log ratio of theory to experiment over 2016–2025 (0.072), the realistic MDE for C1 is about 1.28–1.36 at α/3. The range runs from a normal approximation to a t-distribution with 9 degrees of freedom.
- A plain Poisson model would have given 1.11.

**Problem 3: exaggeration.**
- With an MDE near 1.3 and plausible effects near 1.1, a significant C1 would have overstated the effect.
- If the true ratio is 1.10, power is about 12%, and significant estimates average 1.25. That is a 2.3-fold exaggeration on the log scale (Gelman & Carlin 2014; my simulation).

**Problem 4: wrong timing.**
- An MDE "computed from the fitted model" after the results are known is just a rescaled standard error.
- A design-based MDE comes from pre-period variance and should be fixed before the estimate.

**Fix.**
- Report MDEs at the family's α and with year-level variance.
- Interpret null results through their upper confidence limits:
  - C3's 95% upper limit of 1.10 excludes large effects of the dataset flag.
  - C1's upper limit of 1.30 excludes almost nothing of interest.
- State in the abstract that the physics contrast could not detect ratios below about 1.25.

### M7. Break tests, placebo dates and arXiv's rule changes

**Location.** Line 159; Robustness, "arXiv rule changes" (line 180); Results, lines 204 and 242; the companion's break tests for the contrasts and for the field series.

**Problem 1: a 2026 break cannot be detected.**
- With 15% trimming (Bai–Perron's usual setting, and the companion's "central 70%"), the last admissible break in a monthly series from January 2015 to September 2026 falls at about the end of 2024. For bioRxiv (2019–2026) it falls at about mid-2025.
- A break in 2026 therefore cannot be detected; the procedure can only place breaks earlier.
- The companion's physics slope break at 2024-11 (p = 0.001) lies two months inside that boundary. It is a boundary solution, compatible with a later break.
- So "a broad arXiv acceleration from late 2024" is not supported by this test. The evidence on timing is the year-specific departures from trend: physics 1.05, 1.14 and 1.32 in 2024, 2025 and 2026.
- Options:
  - If a test without a pre-specified date is wanted, use an end-of-sample instability test (Andrews 2003) for the last 9 or 21 months.
  - Otherwise, drop the unknown-date tests: they add length without adding information.
  - If Bai–Perron is kept for earlier breaks:
    - use seasonal dummies as regressors that do not break;
    - use autocorrelation-robust statistics;
    - select the number of breaks with the UDmax/WDmax tests followed by sequential sup-F(ℓ+1|ℓ) tests rather than BIC (Bai & Perron 2003, the manuscript's reference 44).

**Problem 2: the placebo dates do not calibrate the main estimate.**
- The companion's placebo estimator (a group trend plus a level shift, pre-2023 data only) differs from the main estimator (a year effect relative to 2022), so it cannot calibrate it. Use the identical estimator at each pre-period year.
- With four to six non-COVID pre-period years, the placebo p-value cannot fall below 1/5 to 1/7. Say so.

**Problem 3: rule-change indicators cannot separate rules from 2026.**
- Group-specific indicators for 31 October 2025, 10 December 2025, 21 January 2026 and 11 February 2026 are almost collinear with the 2026 effect, so "indicators for these dates" cannot separate the two.
- Argue the direction of each rule's effect instead.
- The companion's "drop November 2025 to February 2026" variant (C1 = 1.17) and "sample to October 2025" variant are the right kind of check.

**Problem 4: the endorsement rule biases the H2 share upwards.**
- The endorsement rule for new mathematics authors (10 December 2025) restricts entry.
- For the share of papers with a prolific author, this removes newcomers' papers from the denominator and so raises the share.
- The manuscript (line 242) presents the rule as evidence against a rule-change explanation, but its likely bias runs in the direction of the finding, though it is probably small.

**Problem 5: September 2026 is an outlier.**
- New mathematics papers jumped from 5,903 in August to 8,360 in September, +42% in one month.
- The synthetic-control gap is about zero in January–April 2026 but 0.31 and 0.40 log points in August and September (companion).
- The claim that the 1 October cap "cannot have caused a rush" (line 180) holds only if there was no advance signal.
- Report every 2026 estimate for January–August as a sensitivity analysis.

### M8. The heavy-producer measure (H2) is dominated by mechanical effects of volume and does not test "broad versus a few outliers"

**Location.** Methods, "Heavy producers" (line 143) and "Heavy producers per author" (line 167); Results, lines 224–232; Table 5; Fig 3A; Abstract; Discussion (lines 246 and 260); Conclusions (line 298).

**Problem 1: volume alone raises the share.**
- The share of papers with an author name that has five or more papers in a window rises convexly with the number of papers per window.
- I calibrated simple mixture models to the Q3 2025 aggregates (20,108 names; 112 with five or more papers; 5 with ten or more). I used three calibrations of Gamma–Poisson and lognormal–Poisson mixtures. Author slots were estimated from the team-size table.
- I then multiplied every author's rate by the observed growth (×1.66 in author slots, ×1.80 in papers). The models predict about 470–1,250 names with five or more papers in Q3 2026, against 693 observed (my check).
- So a sixfold rise in prolific names is what a uniform, proportional increase would produce. That uniform increase is precisely the "broad" scenario.
- Names with ten or more papers (69 observed, against 10–63 predicted) sit at or above the upper end. That is the kind of signal a proper null model would test.
- The partial October 2026 quarter, with a share of 2.9%, shows the same mechanics in reverse.

**Problem 2: namesakes scale with volume too, and the strict variants change the population.**
- Removing the 407 most frequent surnames, which hold 35.7% of author slots, removes mostly common East Asian surnames.
- The strict series therefore describes a different set of authors, not the same set with fewer collisions.

**Problem 3: "established" is not shown.**
- Author histories are left-censored at January 2025.
- The "earlier quarters" in `robustness_math_prolific.py` (`q < "2026-Q3"`) include January–June 2026, which is inside the acceleration.
- So "611 of 693 prolific authors had posted mathematics papers in earlier quarters" does not show that they were established before 2026.

**Problem 4: most of the growth did not come from prolific authors.**
- Of the 8,716 additional papers from Q3 2025 to Q3 2026, 5,742 (66%) had no prolific author under the all-names definition, and about 89% had none under the strict variant.
- Distinct names rose 41% and papers per name (fractional output) rose 28% (my check from Table 5).
- At quarterly resolution, therefore, about three-fifths of the growth (on the log scale) comes from more names being active, not from active names producing more.
- "The acceleration came from many established authors producing more" (Conclusions) is not what the data show.

**Problem 5: the base quarter matters.**
- Q3 2025 is the lowest quarter of 2025 for both strict variants.
- Against the 2025 mean, the strict shares rose 2.6-fold and 2.9-fold, not "more than tripled under every definition".

**Problem 6: the monthly shares are not month-specific.** The monthly shares in Fig 3A classify a July paper using counts that include September.

**Problem 7: the mention comparisons are naive.**
- The comparisons of mentions (AI tools, Lean, Erdős) treat papers as independent, but a few prolific authors can produce many Erdős or Lean papers.
- The AI regular expression also matches "claude", a common French given name in dedications in the comments field, and bare "o1"/"o3" tokens. Validate a sample.

**Problem 8: the intervals describe no sampling process.**
- The data are the full population of arXiv mathematics papers, so the Wilson intervals describe no sampling process.
- The companion itself notes that they are too narrow.

**Fix.**
1. **Main H2 statistic:** decompose the change in fractional output into more active names and more output per name. Report the share contributed by authors with five or more papers and by the top 1%. The companion has already specified this; report it in the main text.
2. **A uniform-scaling null:**
   - Simulate Q3 2026 from each name's 2025 rate multiplied by the aggregate growth.
   - Compare the observed upper tail with the simulated one: five or more papers, ten or more, and the top 1%'s share of the increase.
   - "Broad" predicts agreement; "a few outliers" predicts an excess at the top.
3. **Longer histories:** use the companion's harvest from January 2019 to define "established" as active before 2023, and to estimate how the prolific share responds to volume over 2019–2024.
4. **Annual windows,** to blunt batch posting and quarter-end effects.
5. **Mention comparisons clustered by author,** or counts of distinct authors.
6. **Drop the sampling intervals.**

### M9. What the design can and cannot say about AI as the cause

**Location.** Title; Abstract; Introduction (line 107); Discussion (lines 246–282); Limitations (line 286); figure legends (dated markers).

**Problem 1: no exposure measure.**
- There is no measure of AI exposure; the "treatment" is the calendar year.
- Every 2025–2026 change is bundled into it: AI capabilities, arXiv's rule changes and moderation load, funding shocks, conference cycles and server-specific dynamics.
- Within-field differencing removes shocks only if they hit both groups in proportion. The most plausible concurrent shocks do not: funding (M3) and arXiv's rules (M7).

**Problem 2: the mechanism is assumed, not measured.** The cost of work beyond writing is assigned through labels.

**Problem 3: the figure markers invite causal reading.**
- The figures mark one vendor's release date among many.
- With many releases each month, any monthly series will seem to bend near some release.

**What the design can and cannot show.**
- It can show where and when counts changed, and whether the change lines up with experimental intensity within a server. It does not line up.
- It cannot attribute the change to AI, establish the cost mechanism, or say anything about misuse or legitimacy. Line 260 concedes this; the abstract's "without any misuse" does not.

**Fix.**
- Remove causal verbs.
- Either remove the vendor marker, or mark a vendor-neutral list of releases specified in advance and state the rule for choosing them.
- Move the argument about legitimate use to the companion essay, or label it clearly as argument (Section 7.6).

### M10. Descriptive inferences in the Results and Abstract that do not hold

**Location.** Abstract; Results, lines 202–218 and 224–226; Table 3; Discussion, line 246.

**Problem 1: comparing ranges instead of testing the difference.**
- "Theory grew 20%, outside its 2017–2025 range; experiment grew 11%, within its range" compares two significance statements. It does not test the difference (Gelman & Stern 2006).
- The difference itself is ordinary:
  - The 2026 change in the January–September log ratio of theory to experiment was +0.082. The 2017–2025 changes had a standard deviation of 0.100 (z ≈ 0.9).
  - The 2026 log ratio (2.35) lies within its 2016–2025 range (2.23–2.44) (my check).
- Experiment is "within its range" because the series is small and volatile; hep-ex alone grew 14.2%.

**Problem 2: year-on-year growth misranks fields.**
- Year-on-year growth ranks fields that have different trends.
- Computer science's +41% is 1.15 [0.97, 1.37] times its 2015–2022 trend (companion), which is not an exceptional acceleration.

**Problem 3: the endpoints flatter the rise.** The abstract's "from 5.3% in January 2025 to 19.3% in September 2026 (3.0% to 6.2%)" runs from a high month to the largest month of 2026.
- January 2025 (2.97%) is the second-highest month of the strict series in 2025, whose 2025 values ranged from 1.5% to 3.5%.
- September 2026 had both the most papers (8,360) and the highest share.

**Problem 4: "no break" for bioRxiv was never tested.**
- "No break in 2026" for bioRxiv (abstract; line 204) was asserted before any test, and the field-level test cannot detect a 2026 break (M7).
- The companion's trend departure for bioRxiv, 0.91 [0.71, 1.15], is compatible with anything from −29% to +15%.

**Problem 5: the AI-writing comparison rests on the wrong corpus and year.** "Published estimates put AI-assisted writing in biology on a par with physics" rests on arXiv's q-bio archive at the end of 2023 (Lin & Zhu [34]). It concerns neither bioRxiv biology nor 2026.

**Problem 6: contrary evidence is not discussed.**
- arXiv q-bio is the computational-biology archive, where H1 predicts acceleration.
- It fell 7% in January–September 2026 (Table 3), yet sits 1.26 times above its trend (companion).
- This contrary, or at best ambiguous, evidence is not discussed.

**Problem 7: the medRxiv conclusion depends on the window.**
- The flagged series grew 27% year on year in 2026, against 22% for all non-COVID medRxiv preprints. From 2023 to 2026, the two grew at the same rate, 1.88-fold (my check; the flag counts include COVID-flagged preprints).
- This is the same sensitivity to the window as in the other contrasts.

**Fix.**
- Report contrasts directly: the difference in log growth, with its historical distribution.
- Use full series or annual averages for the H2 endpoints.
- Replace "no break" with the estimate and its interval.
- Correct the q-bio statement and discuss q-bio.

---

## 4. Minor issues

1. **Describe the model actually run.** The Methods should describe:
   - PPML;
   - month fixed effects;
   - group-specific seasonality;
   - Driscoll–Kraay errors with 12 lags;
   - Holm adjustment.

   Drop the negative-binomial sentence. The data window should also match the companion's: arXiv counts from 2010, with models from 2015, not January 2016.
2. **Table 4 needs more detail.** Add:
   - the counts behind each estimate (C1: 1,484 against 142 new papers a month in 2026; C2: 698 against 1,994);
   - the pre-period event-study coefficients;
   - the in-space placebo shares.
3. **Indexing to 2022.** Figs 1–2 and Tables 2–3 are indexed to 2022, a year distorted by COVID-19 in several series. For display, show log counts with the pre-2023 trends, or index to 2019 alongside 2022.
4. **Table 3's missing column.** Table 3 should add, for each contrasted pair, the yearly change in the log ratio with its 2017–2025 range. That is the quantity H1 is about.
5. **A rounding slip.** The abstract says bioRxiv grew "10–13% a year since 2023", but 2023 was 9.5%.
6. **The title's 1.9 million.** The figure is provisional and is not the sample of any test. The confirmatory evidence is a few hundred group-months.
7. **Validate the regular expressions.** Check each on a random sample of about 100 matches and report its precision:
   - AI tools ("claude"; "o1"/"o3");
   - public datasets ("adverse event reporting system" also matches VAERS; the case-insensitive `\bSEER\b` matches the word "seer");
   - COVID-19.
8. **Aliased categories.**
   - Per-archive mathematics counts include aliased categories (math-ph/math.MP).
   - Analyses specific to mathematics should use the OAI series by primary category. This matters most for the synthetic control, which uses math-ph as a donor with weight 0.12.
   - `methods.md` says 15 donors, while `field_tests.json` lists 19.
9. **PubMed as a comparator.**
   - PubMed counts journal articles, with publication lags and journal-side supply shocks. For example, PLOS ONE introduced a pre-screen for Mendelian randomisation studies in April 2024 (https://pmc.ncbi.nlm.nih.gov/articles/PMC12626271/).
   - A 2026 effect on experimental work would barely appear in 2026 PubMed records.
   - Policy changes of the same kind could affect the medRxiv public-dataset series, and the manuscript notes that screening policies were not examined (line 290).
10. **H3 needs an equivalence test.** "H3 predicts similar prevalence across groups" is a claim of equality. It needs an equivalence margin and test (Lakens 2017), not a non-significant difference.
11. **The marker regression is confounded.** The planned regression of growth on the change in marker prevalence (specified by the companion) has two problems:
    - It mixes bioRxiv categories with arXiv archives, so experimental intensity is confounded with server.
    - If the marginal papers are the AI-written ones, marker change and growth move together mechanically.

    Either add server × year fixed effects and state the predicted signs in advance, or drop the regression.
12. **Relabel "confirmatory".** Call the tests "primary (fixed after descriptive inspection, before modelling)". Line 113 already says this honestly.
13. **Fig 3's legend** should say that the monthly share uses quarterly author counts.
14. **Future physics series.** The cap of two submissions per submitter will hit submitters for large collaborations in hep-ex, so any extension of the physics series must model it (line 292 notes the break).
15. **Data availability.** The statement should include the statistical JSON files and the model scripts.

---

## 5. Analyses to request, ranked by information value

Each item names the alternative it addresses or the error it corrects. None is meant to fill space.

1. **The pre-specified estimand and a specification table.**
   - *What:* report C1–C3 under the plan's baseline (confirmatory), alongside references of 2019, a non-COVID baseline, 2022 and 2023–2024, and the trend-adjusted estimate. Disclose the change to 2022.
   - *Why:* it decides what the paper may claim.
   - *Cost:* no new data.
2. **Placebo-based primary inference, with assignments matched to each contrast's structure.**
   - *C2:* all 455 ways of choosing 3 of the 15 C2 categories as "computational", aggregated as in the real groups.
   - *C1:* all draws of 4 and 2 archives from the physics archives.
   - *In time:* the identical estimator at each pre-period year.
   - *Why:* it decides how C2 is interpreted. The current 6-against-6 wet-lab halves are less noisy than a 3-category group dominated by one category, so the reported 20% probably understates the placebo p-value.
3. **Bioinformatics split by AI or machine-learning topic.**
   - *What:* a keyword rule fixed in advance.
   - *Why:* bioinformatics is the sole driver of C2, so this is the most direct test of AI as a topic against AI as a tool.
   - *Predictions:*
     - if non-AI bioinformatics also accelerated, that supports the cost mechanism;
     - if only AI-topic bioinformatics did, the C2 signal is about topic.
4. **US against non-US corresponding institutions for the 2026 wet-lab slowdown** (M3).
   - *Why:* it separates a funding shock from the AI-cost mechanism, the main alternative explanation for C2's 2026 movement.
5. **H2: decomposition, a uniform-scaling null and 2019 histories** (M8).
   - *Why:* this turns H2 from a description into a test.
   - *Cost:* low; the harvest from January 2019 already exists.
6. **A preregistered out-of-sample test of C2 and C3** on bioRxiv and medRxiv data for October 2026 to June 2027.
   - These servers are unaffected by arXiv's cap.
   - Before the data exist, fix and timestamp on OSF:
     - the estimator;
     - the reference period;
     - the decision rule;
     - the predictions.
   - *Timing:* it cannot be done for this submission, but committing to it now is the only route to a genuinely confirmatory test.
7. **A January–August 2026 sensitivity analysis for every 2026 estimate** (M7).
   - Without September, the synthetic-control gap for mathematics falls from 11.9% to about 8%, assuming the monthly gaps in `field_tests.json` are log differences, as the methods imply.
8. **Rambachan–Roth sensitivity for C1 and C2,** with breakdown values (M3).
9. **If the synthetic control is kept, rerun it with clean donors:**
   - use the OAI mathematics series;
   - use a donor pool of physics archives only;
   - exclude math-ph because of aliasing;
   - leave mathematics out of the placebo runs.

   Report it beside the ranking of departures from trend (Abadie 2021, on choosing the donor pool).

**Not requested, and to drop:**
- Benjamini–Hochberg adjustment of falsification tests.
- Bai–Perron or central-trimmed sup-Wald tests for breaks in 2026.
- The marker-growth regression in its current form.
- Trend-adjusted estimates as headlines.
- MDEs "from the fitted model" at the 5% level.
- Any new grouping of archives or categories.
- Any search through subfields of mathematics.

---

## 6. Points that are already strong and should be kept

**The plan's discipline.**
- Falsifiable hypotheses stated before modelling.
- An explicit statement that the descriptive counts were seen first (line 113), with the matching limitation (line 292).
- The design idea of contrasts within a field.
- bioRxiv groups fixed before growth was examined.

**Its safeguards.**
- A confirmatory/exploratory split.
- Leave-one-out estimates and negative controls.
- A planned minimum detectable effect.
- The principle that no exploratory estimate alone supports a conclusion (line 153). Enforce it in the revision: the field-level and synthetic-control results are exploratory.

**Careful data work.** Several checks hold, and all reproduce from the companion files:
- bioRxiv category sums match the official monthly totals from July 2019.
- The OAI and per-archive mathematics series agree (+80% and +78%).
- Every descriptive number I re-computed reproduces exactly, including:
  - bioRxiv: 9.5%, 11.4%, 13.0% and 11.7% growth; 35,750 / 38,717 / 36,866 papers;
  - Table 3;
  - the medRxiv [RECHECK] figures: 38.2% COVID-19 in January–September 2022; ×2.51 without COVID-19; ×1.88 for both groups from 2023; +33.5% in 2023.

**The self-correction of the companion README's ×2.3 against ×1.6 comparison** for medRxiv. It was the right call and was verified.

**Candour on H2.**
- The namesake-robust variants.
- Stratification by team size.
- The caveats on left-censoring and batch posting.
- The statement that metadata mentions are lower bounds.

**The process record (S1 Appendix) and the [RECHECK] markers.**

**The companion's analysis.**
- PPML with month fixed effects and group-specific seasonality.
- The in-space placebos and leave-one-out estimates.
- The "Analyses tried and dropped" section:
  - the bootstrap over papers was dropped for the right reason;
  - the trend-adjusted C2 was demoted for the right reason;
  - the trend fits for medRxiv and the social sciences were flagged.

  Keep it in the Supporting Information.

**A candid Limitations section.**

---

## 7. Given these results, how should H1, the title, the abstract and the Discussion be reframed?

### 7.1 What the formal results show

| | C1 physics: theory/experiment | C2 biology: computational/wet lab | C3 medicine: public dataset/other |
|---|---|---|---|
| 2026 vs 2022 as run: 95% CI; Holm p | 1.14 [1.00, 1.30]; 0.11 | 1.08 [1.03, 1.14]; 0.0095 | 0.99 [0.88, 1.10]; 0.82 |
| 2026 vs the plan's baseline (approximate; from the event-study coefficients) | ≈1.05 | ≈1.02 | ≈1.03 |
| 2026 vs 2019 | 1.05 [0.90, 1.23] | 0.87 [0.80, 0.95] | 0.98 [0.84, 1.15] |
| Trend-adjusted | 0.98 [0.72, 1.33] | 1.48 [1.06, 2.07] | 0.85 [0.60, 1.19] |
| Leave-one-out range | 1.03 (no nucl-ex) to 1.43 (no hep-ex) | 0.93 (no bioinformatics) to 1.14 (no genomics) | – |
| Negative controls and in-space placebos | hep-ex vs nucl-ex 1.39; 61% of 153 arXiv archive pairs at least as extreme | 20% of 462 wet-lab half-splits at least as extreme | – |
| MDE (80% power) at α = 0.05 / α/3 | 1.21 / 1.25 | 1.08 / 1.09 | 1.17 / 1.20 |

**None of the three contrasts supports H1 robustly.**
- **C1 is inconclusive.** Its interval touches 1. It is carried by nucl-ex. It is smaller than the divergence between the two experimental archives. And it is typical of arbitrary pairs of arXiv archives.
- **C2 is distinguishable from 1 only against 2022.**
  - It disappears against the plan's own baseline and reverses against 2019 or without bioinformatics.
  - Its 2026 movement is a slowdown in most categories, with bioinformatics the exception (M3).
- **C3 is null.** It rules out large effects of the dataset flag, but it is a weak test of H1 (M4).

**At field level (exploratory):**
- Physics and mathematics were 1.05/1.04 times their 2015–2022 trends in 2024, 1.14/1.08 in 2025 and 1.32/1.48 in 2026.
- In 2026, 14 of 18 arXiv archives were at least 1.25 times their trend (point estimates), including experimental hep-ex (1.37) and hep-lat (1.39).
- nucl-ex (1.00), q-fin (1.03), physics (1.06) and cs (1.15) were the exceptions.
- bioRxiv (0.91 [0.71, 1.15]), medRxiv and PubMed (0.93 [0.86, 1.01]) show no detectable acceleration, with wide intervals and, for medRxiv, an unreliable trend.

**In short:** in 2025–2026 output accelerated across arXiv as a whole, and within arXiv the acceleration does not follow experimental intensity.

### 7.2 The robustness design: what works and what does not

**PPML with month fixed effects and group-specific seasonality.** Keep it.
- *Strengths:*
  - It is the right estimator: equivalent to a binomial model for the share, consistent under any variance, and it absorbs common shocks (M2).
  - It weights months by the information they carry, which for C1 is dominated by the small experimental series. That is appropriate.
- *Weakness:* the problem lies in the estimand it was asked for (the 2022 reference), not in the estimator.

**Driscoll–Kraay errors (Bartlett kernel, 12 lags).** These are the weak point (M2).
- *Weakness 1:* with two series and month fixed effects, they reduce to a Newey–West estimator on one score series.
- *Weakness 2:* they measure serial correlation within years. They miss the year-level shocks that the pre-period itself displays: 4 of 13 pre-period years have p < 0.05.
- *Weakness 3:* for a nine-month coefficient, the effective degrees of freedom are few.
- *Weakness 4:* the block bootstrap and the OLS fit to the log ratio share the same limitation.
- *Consequence:* the cross-check for C1 (OLS on the log ratio, 1.11 [1.02, 1.21], p = 0.013) must not be quoted as support.
- *Fix:* report the intervals as "within-year uncertainty" and make placebo-based inference primary.

**Holm correction.** Technically fine.
- *Strength:* it is more powerful than Bonferroni with the same control.
- *Weakness 1:* it answers a secondary question. The decision rule for H1 is missing (M5).
- *Weakness 2:* the larger multiplicity is the choice of specification, which Holm does not touch.
- *Fix:*
  - align it with the plan's Bonferroni intervals;
  - state the decision rule;
  - note that C2's Holm p of 0.0095 belongs to an estimand that departs from the plan.

**In-space placebos.** The most informative part of the design; put them in the main text.
- *What they show:* the heterogeneity between units that the time-series intervals ignore. On that evidence, C1 is unremarkable and C2 sits around the 80th percentile.
- *Improvement 1: match the structure.* C2 is 3 categories against 12, with one category holding 63% of the group. Reassignments should reproduce this (Section 5, item 2), in the spirit of randomisation inference for few treated units (Conley & Taber 2011; MacKinnon & Webb 2020).
- *Improvement 2: say what the placebos answer.* Placebos built from units that may themselves be "treated" are not a pure null distribution. What they answer is "is the theory/experiment or computational/wet-lab split more predictive of 2026 divergence than arbitrary splits?" That is the right question for H1. The answer is no for C1 and weakly for C2.

**Synthetic control for mathematics.** Report it as exploratory and as a partial replication of Nee et al.
- *Its p-value is the minimum attainable.* The rank p of 0.05 is the smallest possible with 20 units.
- *The donors were treated too.* The arXiv-wide acceleration also reached the donors, so the 11.9% is mathematics' excess over a weighted mix of archives that accelerated as well. It is not the effect of AI on mathematics.
- *Three donor problems:*
  - math-ph (weight 0.12) shares aliased papers with the per-archive mathematics series;
  - non-physics donors have their own shocks: cs has its review-paper gate, and econ, eess and stat have their own dynamics;
  - mathematics should be excluded from the placebo runs' donor pools.
- *The gap sits in the last months.* It is about zero through April 2026 and 0.31 and 0.40 log points in August and September. The January–August gap is about 8%, so the apparent agreement with Nee et al.'s 11.9% for January–August is not like for like.
- *It ranks mathematics differently from the other method.*
  - Ranked by departure from trend, mathematics is 5th of 18 (rank p = 0.28).
  - Three donors (cs 22%, stat 19%, econ 17%) had larger raw 2026 gaps than mathematics. Mathematics is most extreme only on the ratio of post- to pre-period fit error, because its pre-period fit was good.
  - Report both methods.

**Unknown-date break tests and placebo dates.**
- They cannot detect a 2026 break, and the "late 2024" physics break is a boundary solution.
- The placebo estimator differs from the main one (M7).
- Either use end-of-sample tests or drop the timing claim.

**Trend-adjusted variant.** Rightly demoted. Its spread for C2, from 0.87 to 1.48 across defensible counterfactuals, is itself the finding: the data do not identify C2's counterfactual.

**Minimum detectable effects.** Report them at α/3 and with year-level variance (M6).

### 7.3 Reframing H1 (and H2, H3)

**H1: keep it and report the outcome.**
- Keep H1–H3 in the Introduction exactly as fixed in the skeleton, dated 16 October 2026, 16:42.
- Report the outcome plainly: "The pre-specified within-field tests did not support H1."
- Do not rewrite H1 to fit the results, for example as a hypothesis about differences between servers. That would be hypothesising after the results are known.
- If the author wants to discuss servers, pose it as a new, exploratory question, answer it with the field-level analyses, and list the competing explanations (Section 7.6).
- H1's second clause ("in experimental work, AI is visible in the writing but much less, or not yet, in the volume") is contradicted within arXiv: hep-ex accelerated as much as theory. Its writing half is untested until the marker results are reported.

**H2: a descriptive question unless the null model is run.**
- Without the uniform-scaling null, present H2 as a descriptive question: how did the distribution of output across author names change in arXiv mathematics?
- If the null is run, H2 becomes a test and can be reported as one.

**H3: background only, unless measured with an equivalence test.**
- Keep it as background from published estimates, or measure it with markers and an equivalence test.
- Do not claim that differences in growth "are not explained by" differences in adoption.

### 7.4 Title

**Principles:**
- Describe what was measured and tested.
- Use no causal verb.
- Drop "1.9 million".

**Options:**
1. "Preprint output in 2025–2026: a broad acceleration on arXiv, and no consistent difference between experimental and non-experimental work within fields"
2. "Where preprint output accelerated in 2025–2026: pre-specified tests on arXiv, bioRxiv and medRxiv"
3. "Did preprint output accelerate where experiments are not the bottleneck? Pre-specified tests on arXiv, bioRxiv and medRxiv" (a question, which the author prefers to avoid; listed for completeness)

### 7.5 Abstract

**Delete:**
- "Output has grown fastest where the work beyond writing is also cheap";
- "Published estimates put AI-assisted writing in biology on a par with physics";
- "without any misuse";
- the range comparison of theory and experiment;
- "no break in 2026";
- the monthly endpoints for H2.

**Add:**
- the pre-specified contrasts, with their estimates, intervals and Holm p-values;
- the robustness results that decide their interpretation: leave-one-out, base year and placebo shares;
- the exploratory field-level result;
- H2 as a description, with the decomposition;
- a closing sentence on what cannot be inferred.

**A sketch, to be filled with the final confirmatory numbers:**

> I tested whether preprint output accelerated most where the work beyond writing is cheap, using monthly counts of new preprints on arXiv (2015–September 2026), bioRxiv and medRxiv (2019–2026). Three within-field contrasts were specified before modelling: theory against experiment archives in physics; computational against wet-lab categories on bioRxiv; and medRxiv preprints naming widely reused public datasets against the rest. None supported the prediction robustly. The physics rate ratio for 2026 was [x] ([CI]; Holm p = [p]); it depended on one small archive and was smaller than the divergence between the two experimental archives. The biology ratio was [x] ([CI]); it reversed against a 2019 baseline and without bioinformatics, and 20% of random splits of wet-lab categories diverged as much. The medicine ratio was [x] ([CI]). In exploratory analyses, 2026 output was at least 25% above its 2015–2022 trend in 14 of 18 arXiv archives, including experimental particle physics, but not detectably on bioRxiv, medRxiv or PubMed. In arXiv mathematics, the share of papers with an author name posting five or more papers in a quarter rose from 5.3% to 18.1% between Q3 2025 and Q3 2026; [decomposition result]. The 2025–2026 acceleration was a feature of arXiv broadly rather than of non-experimental work within fields; these data cannot identify its causes.

### 7.6 Discussion and Conclusions

**First paragraph (line 246).** Replace it with the principal findings of Section 7.1.

**"Why experimental science is less affected so far" (lines 248–256).** The results do not show this within fields. Delete the subsection, or rewrite it as "Why might arXiv differ from bioRxiv and medRxiv?" and list the candidate explanations without choosing among them:
- platform factors: rules, moderation load and community norms;
- AI tools may help most with mathematics, theory and code, which pervade arXiv, including the analysis work of experimental physics;
- publication lags and journal-first habits in biomedicine;
- funding shocks;
- AI as a research topic.

Say plainly that this design cannot separate them, and point to the prospective test (Section 5, item 6).

**The medicine paragraph (line 254).**
- C3 is null.
- The published NHANES and Mendelian-randomisation literature concerns journals.
- Keep it as context, not as support.

**"Counting outputs when AI is used legitimately" (lines 258–266).**
- Delete "The acceleration documented here needs no misuse"; the data are silent on misuse.
- Keep at most one paragraph, labelled as interpretation, or move the argument to the companion essay.

**Implications (lines 268–282).**
- The seven-point list does not follow from these findings.
- Cut it to one short paragraph about what the data do support: counts of arXiv preprints, and of papers per author name in mathematics, changed abruptly in 2026. Comparisons of counts across years and servers therefore need care, whatever the cause.
- Move the list to the essay.

**Limitations (lines 284–294).** Add:
- the departure from the planned reference period;
- that the robust intervals omit year-level and between-category variation;
- the minimum detectable effects;
- the dependence of each contrast on a single archive or category;
- the mechanics of H2;
- that the data are a population, not a sample;
- the end-of-sample limits on timing claims;
- the vendor marker.

**Conclusions (line 298).** Replace them with a statement aligned with Section 7.1, for example:

> Pre-specified within-field tests did not show that the 2025–2026 acceleration of preprint output was concentrated in non-experimental work. The acceleration was broad across arXiv, including experimental physics, and was not detectable on bioRxiv, medRxiv or PubMed. In arXiv mathematics, the distribution of output across author names shifted sharply in 2026 [with the decomposition result]. Counts of preprints from 2026 are therefore not directly comparable with earlier years on arXiv, whatever the cause, and these data cannot attribute the change to generative AI.

### 7.7 Further analyses: informative, not fishing

**Three criteria.** An analysis is worth adding only if:
- it targets a named alternative explanation for a result the paper relies on;
- its prediction under each explanation is written down before it is run;
- it will be reported whatever it shows.

**What passes.** By these criteria, four analyses from Section 5 qualify:
- item 3: the split of bioinformatics by AI topic;
- item 4: the split by country for the wet-lab slowdown;
- item 5: the H2 decomposition and uniform-scaling null;
- item 6: the preregistered prospective test.

Items 1, 2, 7, 8 and 9 report or correct what was already run.

**Fishing, to avoid:**
- New groupings of archives or categories presented as primary. Examples: reassigning hep-lat, cond-mat, physics.\* or genomics, or using the per-archive ranking of 2026 departures to define new "experimental" and "non-experimental" sets.
- New reference years or windows chosen after seeing estimates.
- More unknown-date break tests.
- More negative-control pairs beyond the structured placebo distributions.
- Subfield-by-subfield searches in mathematics.
- Alternative standard-error estimators tried until one gives p < 0.05.
- Treating the field-level pattern as confirmation of a modified H1.

---

## References cited in this review

**Methods literature**
- Abadie A. Using synthetic controls: feasibility, data requirements, and methodological aspects. J Econ Lit. 2021;59(2):391–425.
- Abadie A, Diamond A, Hainmueller J. Synthetic control methods for comparative case studies. J Am Stat Assoc. 2010;105(490):493–505.
- Andrews DWK. End-of-sample instability tests. Econometrica. 2003;71(6):1661–1694.
- Bai J, Perron P. Computation and analysis of multiple structural change models. J Appl Econom. 2003;18(1):1–22 (manuscript reference 44).
- Berger RL, Hsu JC. Bioequivalence trials, intersection–union tests and equivalence confidence sets. Stat Sci. 1996;11(4):283–319.
- Bertrand M, Duflo E, Mullainathan S. How much should we trust differences-in-differences estimates? Q J Econ. 2004;119(1):249–275.
- Conley TG, Taber CR. Inference with "difference in differences" with a small number of policy changes. Rev Econ Stat. 2011;93(1):113–125.
- Donald SG, Lang K. Inference with difference-in-differences and other panel data. Rev Econ Stat. 2007;89(2):221–233.
- Driscoll JC, Kraay AC. Consistent covariance matrix estimation with spatially dependent panel data. Rev Econ Stat. 1998;80(4):549–560.
- Gelman A, Carlin J. Beyond power calculations: assessing type S (sign) and type M (magnitude) errors. Perspect Psychol Sci. 2014;9(6):641–651.
- Gelman A, Loken E. The statistical crisis in science. Am Sci. 2014;102(6):460–465.
- Gelman A, Stern H. The difference between "significant" and "not significant" is not itself statistically significant. Am Stat. 2006;60(4):328–331.
- Holm S. A simple sequentially rejective multiple test procedure. Scand J Stat. 1979;6(2):65–70.
- Kiefer NM, Vogelsang TJ. A new asymptotic theory for heteroskedasticity-autocorrelation robust tests. Econom Theory. 2005;21(6):1130–1164.
- Lakens D. Equivalence tests: a practical primer for t tests, correlations, and meta-analyses. Soc Psychol Personal Sci. 2017;8(4):355–362.
- Lazarus E, Lewis DJ, Stock JH, Watson MW. HAR inference: recommendations for practice. J Bus Econ Stat. 2018;36(4):541–559.
- Lipsitch M, Tchetgen Tchetgen E, Cohen T. Negative controls: a tool for detecting confounding and bias in observational studies. Epidemiology. 2010;21(3):383–388.
- MacKinnon JG, Webb MD. Randomization inference for difference-in-differences with few treated clusters. J Econom. 2020;218(2):435–450.
- Rambachan A, Roth J. A more credible approach to parallel trends. Rev Econ Stud. 2023;90(5):2555–2591.
- Roth J. Pretest with caution: event-study estimates after testing for parallel trends. Am Econ Rev Insights. 2022;4(3):305–322.
- Santos Silva JMC, Tenreyro S. The log of gravity. Rev Econ Stat. 2006;88(4):641–658.
- Wooldridge JM. Distribution-free estimation of some nonlinear panel data models. J Econom. 1999;90(1):77–97.

**Web sources checked on 16 October 2026**
- bioRxiv API documentation; the details endpoint returns `author_corresponding_institution`: https://api.biorxiv.org/
- Pruller J, Mockridge J, Vousden G. Expectations for Mendelian randomization research in PLOS One. PLoS One. 2025;20(11):e0337199. States that MR pre-screening began in April 2024: https://pmc.ncbi.nlm.nih.gov/articles/PMC12626271/
- HPN Online, 9 May 2025, reporting a JAMA research letter (694 NIH grants terminated, 28 February–8 April 2025, $1.81 billion): https://www.hpnonline.com/regulatory/news/55289345/newly-published-study-quantifies-types-of-grants-terminated-by-nih-since-late-february
