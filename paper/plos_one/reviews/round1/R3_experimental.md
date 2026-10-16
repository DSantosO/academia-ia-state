# Referee report R3: experimental physics and biology

**Manuscript.** "Generative AI is eroding publication counts as a measure of scientific work: evidence from 1.9 million preprints". PLOS ONE research article, draft v1, 16 October 2026 (`paper/plos_one/draft_v1.md`).

**Reviewer.** R3, an experimental scientist working in particle and nuclear physics and in wet-lab and computational biology.

**Date.** 16 October 2026.

**Recommendation.** Major revision. The revision has to reframe the central claim, not polish it (section 2).

**What I read and checked**

- **The manuscript and the companion files.** I read the manuscript; `paper/figures/README_companion_analysis.md`, `within_field_quarterly.csv` and `arxiv_math_prolific_robustness.json`; and, on branch `claude/happy-lovelace-wqek9b`, the scripts `harvest_rxiv_categories.py`, `analyze_within_field.py` and `harvest_medrxiv_details.py`, with the raw and processed arXiv, bioRxiv and medRxiv count files.
- **The formal results.** These arrived while I was reviewing: `paper/plos_one/stats/methods.md` and `results.md` (companion commit 37b4b11).
- **My own checks.**
  - I recomputed the descriptive figures from the companion files.
  - I ran a permutation check on the bioRxiv category counts.
  - I queried the INSPIRE-HEP literature API on 16 October 2026 to break the experimental physics archives down.
  - The queries are listed at the end so that they can be reproduced. Web sources are cited by URL where they are used.
- **Line numbers** refer to `draft_v1.md`.

---

## 1. Summary

**The claim.** The manuscript argues that generative AI has raised scientific output where the work beyond writing is cheap: theory, computation and analyses of existing data. It has not done so, or not yet, in experimental work. Publication counts would therefore now stand for different amounts of work in different fields.

**The evidence.** The evidence is counts of new preprints up to Q3 2026:

- three within-field contrasts:
  - arXiv theory archives against arXiv experiment archives;
  - bioRxiv computational categories against wet-lab categories;
  - medRxiv preprints that name a public dataset against the rest;
- an analysis of how arXiv mathematics output is spread across authors;
- published estimates of AI-assisted writing.

**What holds up.** Every descriptive number I checked reproduces exactly from the companion files. The design instinct is right: contrasts within fields, a fixed confirmatory family, and negative controls.

**What does not.** The formal results that arrived during this review do not support the central contrast:

- **Physics.** Experimental high-energy physics departs from its own trend as much as theory does, and the contrast between theory and experiment fails its own negative controls.
- **Biology.** The contrast rests on bioinformatics alone. It reverses without bioinformatics, and it reverses with 2019 as the base year.
- **Medicine.** The contrast is null.

## 2. Overall assessment and recommendation

**The question.** The question is important and the author asks it the right way: within fields, between kinds of work that share preprint culture, incentives and calendars. The manuscript is clearly written and unusually transparent about how it was made. Its handling of COVID-19 in medRxiv and of the 2019 base year is honest.

**The central claim is contradicted by the formal results.** H1 says that output accelerated where experiments are not the bottleneck and "much less, or not yet" in experimental work. The paper's decision rule (l. 153) is that a contrast supports H1 only if its adjusted interval excludes 1. By that rule:

- **C1, physics, fails.** The 2026 rate ratio is 1.14 [1.00, 1.30], with Holm-adjusted p = 0.11.
- **C3, medicine, fails.** The rate ratio is 0.99 [0.88, 1.10].
- **C2, biology, passes formally but is fragile.** The rate ratio is 1.08 [1.03, 1.14]. It reverses without bioinformatics (0.93) and with a 2019 base (0.87). It equals its own minimum detectable effect. Its strongest structural break is in 2020, not in the AI era.

**The negative controls did what negative controls are for.** The two experimental archives diverge from each other more than theory diverges from experiment: hep-ex against nucl-ex gives 1.39 [1.19, 1.64]. By the paper's own criterion (l. 161), this points "to heterogeneity among archives or categories rather than to the cost of experiments."

**The robust pattern is the one the paper set out to avoid.** That pattern lies between servers. arXiv physics and mathematics rise above their trends in 2026; bioRxiv, medRxiv and PubMed do not. This is a comparison between fields, which the Introduction says confounds AI with preprint culture, norms and incentives (l. 99).

**What is solid and worth publishing:**

- the descriptive time series;
- the 2026 rise in arXiv physics and mathematics above trend;
- the absence of such a rise on bioRxiv and in PubMed;
- the heavy-producer analysis of arXiv mathematics, with its namesake checks;
- the honest null for medRxiv;
- the battery of negative controls itself.

**What is not supported:**

- the title's causal framing;
- the abstract's central sentence: "Output has grown fastest where the work beyond writing is also cheap, and much less, so far, in experimental work";
- H1 as stated;
- the Discussion's account of why experimental science is "less affected";
- the policy conclusions built on that account.

**Recommendation: major revision.** The revision should:

1. rewrite the title, abstract, Results and Discussion around what the confirmatory tests show;
2. present the refinement that the data now suggest ("new data at the margin" rather than "experiment") as a hypothesis formed after seeing the data, with a pre-registered test on held-out material;
3. cut the material on evaluation policy back to what preprint counts can support.

If H1 remains the headline claim, I would recommend rejection. PLOS ONE requires that conclusions follow from the data, and here the paper's own confirmatory analyses contradict them.

---

## 2a. As an experimentalist, how do you read this? (added after the formal results arrived)

### What the formal results show for experimental work

All values are from `stats/results.md` unless marked otherwise.

**Physics: the contrast between theory and experiment does not hold**

- **The confirmatory estimate.** The 2026 rate ratio of theory to experiment against 2022 is 1.14 [1.00, 1.30]. That is below the minimum detectable effect of 1.21.
- **The estimate under other specifications:**
  - trend-adjusted: 0.98 [0.72, 1.33];
  - 2019 as base: 1.05 [0.90, 1.23];
  - without nucl-ex: 1.03 [0.91, 1.18].
- **The negative controls:**
  - hep-ex against nucl-ex: 1.39;
  - pairs of theory archives also diverge (hep-th against gr-qc 0.87 [0.82, 0.92]; hep-ph against gr-qc 0.85 [0.80, 0.90]);
  - 61% of all pairs of arXiv archives diverge at least as much as C1.

**How far each physics archive departs from its 2015–2022 trend in 2026:**

| Archive | Departure from trend, 2026 |
|---|---|
| hep-ex | 1.37 |
| hep-lat | 1.39 |
| hep-th | 1.28 |
| hep-ph | 1.28 |
| gr-qc | 1.26 |
| nucl-th | 1.58 |
| nucl-ex | 1.00, the lowest of the 18 archives |

The coordinator's note gives 1.29 for hep-th. I use the 1.28 in `results.md`.

**Biology and medicine**

- **Biology.** C2 is 1.08 [1.03, 1.14], but without bioinformatics it is 0.93 [0.89, 0.97]. bioRxiv as a whole stands at 0.91 [0.71, 1.15] of its trend, and PubMed at 0.93 [0.86, 1.01].
- **Medicine.** C3 is 0.99 [0.88, 1.10].

**What this means.** "Experimental work did not accelerate" is true of nucl-ex and of bioRxiv's wet-lab categories. It is not true of experimental particle physics. Also, bioRxiv's computational categories other than bioinformatics did not accelerate either.

### Is hep-ex "existing data"?

**Partly. Which part matters.**

**The large collaborations analyse stored data.** Their papers are analyses of datasets already collected:

- LHC Run 2 (2015–2018);
- LHC Run 3, which runs from 2022 to mid-2026; CERN scheduled Long Shutdown 3 "to begin at the start of July 2026" (https://home.cern/updated-schedule-cerns-accelerators, 4 October 2024);
- the BESIII and Belle II samples.

For the marginal collaboration paper, data-taking is a sunk cost. What the paper costs is analysts' time, simulation and internal review. In the manuscript's own terms, that is closer to "existing data" than to "new experiments".

**But most of hep-ex's growth does not come from those collaborations.** I split the hep-ex records in INSPIRE-HEP by author count and by whether they carry a collaboration field. The INSPIRE counts track arXiv's per-archive statistics to within 1–2%: 717 against 713 in January–September 2022, and 818 against 817 in 2025.

**Table R1. Primary hep-ex records, January–September (INSPIRE-HEP, 16 Oct 2026)**

| Jan–Sep | All | >300 authors | ≤300 authors, with collaboration field | ≤10 authors, no collaboration | of which not conference papers | 11–300 authors, no collaboration |
|---|---|---|---|---|---|---|
| 2019 | 604 | 221 | 217 | 138 | 83 | 26 |
| 2022 | 717 | 234 | 216 | 181 | 101 | 84 |
| 2023 | 672 | 248 | 186 | 191 | 133 | 46 |
| 2024 | 753 | 327 | 190 | 187 | 128 | 49 |
| 2025 | 818 | 286 | 192 | 259 | 202 | 80 |
| 2026 | 922 | 341 | 148 | 366 | 262 | 67 |

**Where the growth comes from:**

- **Collaboration papers.** Papers with more than 300 authors rose 4% from 2024 to 2026, after a dip in 2025.
- **Small-team records.** Records with at most 10 authors and no collaboration field nearly doubled (187 to 366). Excluding conference papers, they more than doubled (128 to 262).
- **From 2025 to 2026.** The small-team segment alone grew by 107, slightly more than the archive's net growth of 104. Collaboration papers added 55. Collaboration records with 300 or fewer authors lost 44; these are typically talk write-ups on behalf of a collaboration, or papers by smaller collaborations. Mid-size records without a collaboration lost 13.
- **Since 2022.** The small-team segment accounts for 185 of the 205 additional records.
- **Timing.** The small-team rise began in 2025 (128 to 202 non-conference records). That matches the companion's slope break for the physics field series in November 2024.

**What the small-team records are.** I drew a random sample of 60 of the 262 non-conference small-team hep-ex records of January–September 2026 and classified each from its title and abstract. I am a single, unblinded coder, so treat these counts as indicative.

| Type | Records |
|---|---|
| Simulation, sensitivity or future-facility studies (Higgs factories, FCC/CEPC, DUNE/Hyper-K, NICA) | 18 |
| Machine-learning or AI methods, including LLM and agent tools | 17 |
| Statistical or analysis methods and software | 7 |
| Reviews, talk write-ups, perspectives or an interview | 6 |
| Instrumentation or hardware | 5 |
| Reanalyses of existing or archival data (for example archived ALEPH data, combined public atmospheric-neutrino data) | 4 |
| Concept studies | 2 |
| Report of new measurements | 1 |

A keyword classification of all such records gives the same mix in 2024 and 2026:

- ML or AI terms: 26% in both years;
- simulation or future-facility terms: 38% and 42%;
- review terms: 8% in both years.

The segment therefore doubled without changing what it contains. It is not AI as a research topic that drives it.

**Collaboration output is lumpy.** Papers with more than 300 authors in January–September:

| Collaboration | 2024 | 2025 | 2026 |
|---|---|---|---|
| CMS | 86 | 60 | 108 |
| ATLAS | 103 | 62 | 72 |
| LHCb | 37 | 49 | 59 |
| BESIII | 80 | 83 | 95 |

Swings of 40–80% from one year to the next within a single collaboration dwarf any plausible effect of AI on writing. They reflect analysis campaigns, conference deadlines and approval queues.

**The archives are not comparable containers.** arXiv's own taxonomy (https://arxiv.org/category_taxonomy) treats them differently:

- **hep-ex** covers "Results from high-energy/particle physics experiments and prospects for future experimental results". It "Does not include: detectors and instrumentation nor analysis methods to conduct experiments."
- **nucl-ex** excludes the same and also "descriptions of experimental programs (present or future); comments on published results."

Sensitivity studies for future facilities are admitted in hep-ex and excluded from nucl-ex. Much of the methods and ML material filed under hep-ex belongs, by the taxonomy, in physics.ins-det or physics.data-an.

**My reading.** hep-ex's acceleration is mostly computation and writing, done by experimentalists and others without new data and filed under hep-ex. On top of that sits a lumpy rise in collaboration papers on stored datasets. Neither is "AI made experiments cheaper". The pattern fits the spirit of H1, since the growth is where no new data are needed. It refutes the use of the experimental archives as a measure of experimental work.

### What separates nucl-ex?

**It has not grown in a decade.** nucl-ex had 323 new submissions in January–September 2016 and 346 in 2026 (arXiv statistics, companion file). It is the flattest of the 18 archives; the next flattest, math-ph and nucl-th, grew 1.19-fold. Its flat 2026 continues a long trend rather than marking a 2026 event, so it cannot support an inference about AI.

**Its small-team segment is different in kind.** I drew a random sample of 30 of the 77 nucl-ex records of 2026 with at most 10 authors, no collaboration field and no conference tag:

| Type | Records |
|---|---|
| New measurements (half-lives, γ spectroscopy with Gammasphere, reaction cross sections, proton scattering) | 10 |
| Reviews or talk write-ups | 9 |
| Evaluations or reanalyses | 5 |
| Methods or infrastructure | 5 |
| Reply to a comment | 1 |

- **ML or AI terms** appear in 0 of 63 such records in 2024 and 2 of 77 in 2026. In hep-ex's small-team segment the share is 26%.
- **This segment did not grow from 2025 to 2026.** It had 105 records in 2025 and 102 in 2026 (≤10 authors, no collaboration, conference papers included).

**Preprint habits differ.** Of the Physical Review C articles indexed in INSPIRE, 65% (2019) and 66% (2024) have an arXiv version. For Physical Review D the figure is 99%, and for JHEP 100%. INSPIRE indexes only part of PRC, so read this as indicative. Nuclear-physics counts on arXiv therefore depend more on posting habits than particle-physics counts do.

**The facility cycle.**

- **RHIC ended.** RHIC's 25th and final run ended on 6 February 2026 (https://www.bnl.gov/newsroom/news.php?a=122794). The laboratory adds that "The science mission of RHIC will continue until we analyze all the data and publish all the papers."
- **Collaboration counts moved in opposite directions.** Papers by STAR with more than 300 authors fell from 15 to 5 in January–September, while ALICE's rose from 27 to 36. The numbers are small, but heavy-ion output follows run and analysis cycles.

**Conclusion.** nucl-ex is the one archive whose marginal paper usually needs new beam time or a new measurement. It is also the one archive with a decade of zero growth. Both facts point to data acquisition as the constraint, but both predate 2023.

### Is the bottleneck generating new data, rather than "experiment" as such?

**As a working hypothesis, yes.** These data suggest that what matters is whether the marginal paper needs new data, and, in collaborations, a new pass through an approval pipeline. Whether its authors are experimentalists does not seem to matter.

- **Existing data or no new data:** a collaboration paper on Run 2 data, a sensitivity study for FCC-ee, or a population analysis of the GWTC-4.0 catalogue. In the last case the catalogue and the O4a strain data became public on 26 August 2025 (https://www.ego-gw.it/blog/2025/08/26/gwtc-4-0-updated-gravitational-wave-catalog-released/).
- **New data:** a half-life measurement, a phenotype of a mouse knockout, or a new clinical trial.

**Three cautions:**

1. **It is a hypothesis, not a finding.** It was formed after seeing hep-ex accelerate. Relabelling after the fact makes H1 unfalsifiable: every series that grows becomes "existing data" and every flat one "experiment".
2. **Its support in these data is mixed.**
   - Its one pre-specified test is C3, preprints that name public datasets. C3 is null (0.99; minimum detectable effect 1.17).
   - bioRxiv's computational categories other than bioinformatics did not accelerate: genomics grew 7% and systems biology 5% in January–September 2026, against 8% for wet lab.
3. **"New data" hides two constraints that should be separated:**
   - physical acquisition: beam time, samples, animals, patients and allocation cycles;
   - institutional throughput: collaboration review, ethics approval, and journal revision rounds that demand more experiments.

   Both predict flat counts. They make different predictions about the lag from data to paper (M7; analysis 6) and about small-team versus collaboration papers (analysis 2).

### Stories after the fact and testable hypotheses

| Reading | Status now | Testable version: definition, prediction, falsifier |
|---|---|---|
| "hep-ex is really existing-data work" | Relabelled after the fact. Partly contradicted: the growth is small-team computation, not collaboration results | **Definition:** classify papers before counting as new measurement, reanalysis of existing data, or no data (simulation, methods, reviews); validate by blind double coding. **Prediction:** within the same archive, no-data and existing-data papers accelerate and new-measurement papers do not. **Falsifier:** new-measurement papers grow as fast. Run the confirmatory test on held-out archives (cond-mat, astro-ph, quant-ph) |
| "nucl-ex is flat because beam time binds" | Formed after the fact; nucl-ex was flat in 2016–2025 too | **Prediction:** with the same classification, nucl-ex reviews, reanalyses and methods papers grow and measurement papers do not |
| "Collaboration review caps experimental output" | Plausible; untested | **Prediction:** AI shortens the lag from a preliminary result (ATLAS-CONF, CMS-PAS) to the arXiv paper, and from the end of data-taking to the paper, without raising counts. **Falsifier:** lags unchanged since 2023 |
| "Bioinformatics grows because AI is a tool" | Untested; AI as a topic is equally possible | **Test:** split bioinformatics by text flags for AI or ML topics. **Prediction:** if AI is a tool, bioinformatics without ML topics grows too |
| "The 2026 wet-lab slowdown is the experimental bottleneck" | Confounded with the 2025 NIH funding shock (M6) | **Test:** split by the corresponding author's country. **Prediction:** a funding explanation predicts a slowdown concentrated in the US |
| "Experiment will catch up later" | Unfalsifiable as written | **Requirement:** state a horizon and magnitude, pre-register them, and separate the effect from LS3 (from July 2026) and from RHIC's analysis after its final run, for example by comparing LHC with non-LHC experiments |
| "Saved time goes into bigger experimental papers" | Untested | **Prediction:** pages, figures and supplementary items per paper rise after 2023 in experimental groups and not in others |

### What the paper can honestly claim about experimental science now

Suggested wording:

> "In 2026, new arXiv submissions rose above their pre-2023 trends in nearly every physics archive, experimental high-energy physics included; nuclear experiment, which has not grown in a decade, was the exception. bioRxiv, medRxiv and PubMed showed no comparable departure, in computational or in wet-lab categories, bioinformatics excepted. Within the experimental physics archives, the growth came mainly from small-team papers that report simulations, methods or reviews rather than new measurements (exploratory). These data do not show that experimental work has been slower to accelerate than theoretical work. They are compatible with the hypothesis that what limits AI-driven growth in output is the need for new data rather than experiment as such, but that hypothesis was formed after seeing them and remains to be tested."

**For biology,** the data agree with Blekhman's statement that AI "has not yet substantially increased productivity in biology" [2]. They cannot attribute that to experimental bottlenecks, because the computational categories other than bioinformatics did not accelerate either.

**Sentences that should not survive revision:**

- "In experimental work, AI is visible in the writing but much less, or not yet, in the volume of output" (H1, l. 103; also l. 252);
- "Experimental physics stayed within its historical range" (l. 246).

---

## 3. Major issues

### M1. The central claim is not supported by the confirmatory analyses

**Location.**

- Title (l. 53).
- Abstract (l. 83):
  - "Output has grown fastest where the work beyond writing is also cheap, and much less, so far, in experimental work";
  - the sentence comparing 20% with 11%;
  - "Computational biology outgrew wet-lab biology only from 2025".
- H1 (l. 103); Discussion (l. 246, l. 252); Conclusions (l. 298).

**Problem.**

- **By the paper's own rule (l. 153), two of the three contrasts fail and the third is fragile.** Section 2 gives the numbers.
- **By the paper's own negative-control criterion (l. 161), C1 fails:**
  - the divergence between hep-ex and nucl-ex (1.39) exceeds C1 (1.14);
  - pairs of theory archives also diverge with intervals that exclude 1: hep-th against gr-qc 0.87 [0.82, 0.92]; hep-ph against nucl-th 0.89 [0.81, 0.98].
- **The intervals are too narrow for claims about kinds of work.** Pairs of archives of the same type differ "significantly" under the same machinery, so the Driscoll–Kraay intervals on two stacked series cannot support conclusions about kinds of work. The design's real units are archives and categories.
- **With archives as units, physics cannot be tested.** There are 6 archives and 15 ways to split them 4 against 2, so the smallest attainable one-sided p-value is 1/15 ≈ 0.067. In my check on January–September totals, the actual split ranks:
  - 1st of 15 for 2026 against 2025;
  - 2nd against 2022;
  - 7th against the 2017–2022 mean;
  - 5th against 2019.

  For biology, see M4.

**Why it matters.** This is the thesis of the paper. If it stands as written, the title, abstract and Discussion assert what the analyses contradict.

**Fix.**

- Report H1 as not supported at the level of archives and categories, and give the three ratios of rate ratios and the negative controls in the abstract. That fills the [ANALYSIS PENDING] slot honestly.
- Make the negative controls the main result of the section on within-field contrasts. They are a strength of the design.
- Keep the descriptive contrasts, but subordinate them.
- Move the "new data" refinement to the Discussion as a hypothesis, with the test described under analysis 3.
- Retitle around what is observed: where acceleration is and is not seen in 2026. Avoid "eroding", which reads as causal and broader than the evidence.

### M2. The physics groups are not "theory" and "experiment"

**Location.** l. 135; S2 Appendix (l. 564); Table 3; Fig 2B.

**Problem.**

**(a) gr-qc is assigned to theory against the paper's own rule.** l. 135 says archives that mix theory with observation or experiment go into neither group. arXiv describes gr-qc as "Areas of gravitational physics, including experiments and observations related to the detection and interpretation of gravitational waves, experimental tests of gravitational theories, computational general relativity, ..." (https://arxiv.org/category_taxonomy). The timing matters:

- the LIGO–Virgo–KAGRA O4 run "began May 24, 2023 and continued through November 18, 2025" (https://ligo.org/ligo-virgo-kagra-collaboration-successfully-wraps-up-its-fourth-observing-run/);
- GWTC-4.0 and the O4a strain data became public on 26 August 2025.

This is a wave of existing data, labelled as theory. gr-qc grew 20.5% in January–September 2026 and outgrew hep-th and hep-ph (negative controls 0.87 and 0.85). Without gr-qc, C1 is 1.10 [0.96, 1.25].

**(b) hep-ph is theory by definition, but not only theory.** Its description includes "Particle physics: analysis of theory through experimental results", which covers global fits and reinterpretations of published data. It can stay on the non-experimental side, but the group should be called "theory and phenomenology". Its natural partner is hep-ex, and the two grew alike: by 18% and 14% in 2026, and 1.26-fold and 1.31-fold from January–September 2022 to 2026 (arXiv statistics).

**(c) The two experimental archives have different scopes** (section 2a). Both exclude instrumentation and analysis methods. By construction, then, the experimental group leaves out the methods work of experimentalists, which is the part of their work that AI is most likely to speed up.

**(d) The experimental group is not experimental physics.**

- It is two small archives, about 430 records a quarter, with a minimum detectable effect of 1.21.
- They are dominated by a few collaborations whose output is lumpy (Table R1 and the counts by collaboration).
- Table-top experiment in cond-mat, quant-ph and physics.atom-ph or physics.optics is excluded. Those archives also rose above trend in 2026: cond-mat 1.30, quant-ph 1.54, astro-ph 1.34.

**(e) hep-lat is excluded from both groups without a stated reason** (S2 Appendix). Lattice QCD is theory bound by supercomputer allocations, the analogue of instrument time, so it is a natural test case. It departed by 1.39. Its counts swing with the proceedings of the Lattice conference: INSPIRE lists 102 conference papers in January–September 2024, 202 in 2025 and 150 in 2026.

**Why it matters.** The physics contrast measures the taxonomies and production modes of two archives, not the cost of experiments.

**Fix.**

- Define groups by type of paper rather than by archive (analysis 3).
- At a minimum:
  - move gr-qc to "mixed";
  - report hep-ph against hep-ex and nucl-th against nucl-ex as separate contrasts;
  - add physics.ins-det and physics.data-an as a series for experimental methods;
  - split cond-mat into experimental and theoretical papers with a text classifier validated by physicists.
- For particle and nuclear physics, use INSPIRE, which records collaborations, author counts, document types and disambiguated author identifiers (https://github.com/inspirehep/rest-api-doc).

### M3. The 2022 reference year and the range criterion both favour H1 in physics

**Location.** l. 131, l. 155–157, l. 208; Table 3; Abstract.

**Problem.**

**(a) 2022 is an unusual year for experimental physics.** Two things inflate it:

- **Conference write-ups rebounded after COVID-19.** hep-ex conference papers in INSPIRE (January–September) were 195 in 2019, 65 in 2020, 133 in 2021, 237 in 2022 and 142 in 2023.
- **Snowmass white papers.** The US community planning exercise Snowmass 2021 asked for contributed papers on arXiv by 15 March 2022 (Snowmass Steering Group, 9 March 2022, forwarded at https://mailman.jlab.org/pipermail/hps/2022-March/002209.html). In January–September 2022, 113 of 717 hep-ex records (16%) match "snowmass" in INSPIRE, against 204 of 9,914 records (2%) in the theory group. nucl-th has none.

**Removing the Snowmass records changes C1.** On January–September totals, the crude ratio of rate ratios for 2026 against 2022 is:

| Source | Unadjusted | Snowmass records removed from 2022 |
|---|---|---|
| arXiv statistics | 1.12 | 1.02 |
| INSPIRE counts | 1.14 | 1.04 |

The companion's model gives 1.14 unadjusted. The event-study coefficients for 2020 (1.25) and 2021 (1.19) show the asymmetry of the COVID-19 years in the same direction. Every reasonable base gives about 1.02–1.05: 2019, 2022 without Snowmass, and 2023–2024.

**(b) The range criterion is asymmetric.** The abstract and l. 208 compare "outside their range" with "within theirs". That compares a stable series with a volatile one:

| Series | SD of year-on-year growth, 2012–2025 excluding 2020–2022 |
|---|---|
| Theory | 3.3 points |
| Experiment | 8.3 points |
| hep-ex alone | 10.9 points |

The criterion therefore has very different power in the two series. The experimental range (−13% to +22%) is also set by 2020 and 2022. Excluding 2020–2022, the experimental range is −7% to +9%, and 2026's +10.5% lies above it. hep-ex's +14% is its highest growth since at least 2012, apart from the 2021–2022 rebound.

Contrasting "outside" with "inside" is the error described by Gelman and Stern: a difference between significant and not significant is not itself a test of difference (Am Stat 2006;60(4):328–331, doi:10.1198/000313006X152649).

**Why it matters.** The descriptive case for the physics contrast in the abstract rests on this base year and this criterion.

**Fix.**

- Drop the range language. Report the ratio of rate ratios with its interval.
- Make the primary or co-primary reference period one that excludes 2020–2022, for example 2017–2019. Alternatively, keep 2022 but remove the Snowmass contributions, and either remove conference papers or model them as a separate series.
- Report all bases in one table.

### M4. The biology contrast is a bioinformatics effect, tested at the wrong level

**Location.** l. 137, l. 121, l. 212; Table 3; Fig 2A; S2 Appendix (l. 565).

**Problem.**

**(a) The unit of inference is wrong.** Groups are sets of categories, but inference treats two aggregated monthly series as the units. Categories within each group grew very differently from January–September 2025 to 2026:

| Group | Range of growth across categories |
|---|---|
| Wet lab | pathology −13%, developmental biology −5%, cell biology +13%, pharmacology and toxicology +13% |
| Computational | systems biology +5%, genomics +7%, bioinformatics +27% |

There are 455 ways to call 3 of the 15 computational and wet-lab categories "computational". Among them, the actual grouping ranks as follows (my check on January–September sums, one-sided):

| Comparison | Rank of actual grouping | p |
|---|---|---|
| 2026 against 2025 | 48th | ≈ 0.11 |
| 2026 against 2022 | 69th | ≈ 0.15 |
| 2026 against the 2019–2022 mean | 174th | ≈ 0.38 |

The companion's placebo with random halves of the wet-lab categories gives 19.7%.

**(b) Bioinformatics is the whole effect.** Without it, C2 is 0.93. It is 63% of the computational group in 2026. It is also where AI is a research topic, as in protein and genome language models, single-cell foundation models and LLM benchmarks. The README says so; the paper relegates it to one sentence in Limitations (l. 286).

**(c) Authors choose the category.** If papers that use ML are increasingly filed under bioinformatics rather than genomics or neuroscience, that category grows with no change in the amount of computational work.

**(d) Categories are weak proxies for experimental intensity.**

- "Wet-lab" categories contain much reanalysis: cancer biology on public tumour data, pharmacology and toxicology on docking and network pharmacology, microbiology on metagenomics.
- Genomics contains studies that generate new sequencing data.

**(e) The baseline years are disturbed.**

- 2019–2022 contains the COVID-19 surge. In January–September 2020, wet-lab categories grew 58% and computational ones 31%.
- It also contains wet-lab biology's late adoption of bioRxiv. The 2019 event-study coefficient is 1.24 [1.14, 1.36].
- The strongest break in the ratio is in July 2020 (sup-Wald p = 0.001). The 2020 placebo is "significant": 0.85, p = 0.008.
- The COVID-19 check in l. 121 covers only May–June 2022.

**Why it matters.** C2 is the only confirmatory contrast that passes. Read at the level at which the groups were defined, it cannot be told apart from arbitrary groupings of categories.

**Fix.**

- Make inference at category level, with a Poisson mixed model that has random intercepts and period slopes by category, or an exact permutation of category labels.
- Report bioinformatics with and without papers on AI or ML topics.
- Check for drift in category choice: apply a topic classifier trained on 2019–2021 assignments to papers from 2026.
- Classify papers from their full text. The bioRxiv API exposes `author_corresponding_institution`, `type` and the path to the JATS XML full text (https://api.biorxiv.org/), so methods sections and data-availability statements with new accession numbers can be read.
- Flag COVID-19 preprints in every month, as the medRxiv harvester already does.
- Fit a dose–response across categories against a measured experimental intensity, such as the share of papers that deposit new sequencing, proteomics or imaging data.

### M5. The medicine flag does not measure "existing data", and medRxiv is the wrong place to test it

**Location.** l. 139, l. 216–218, l. 254; Table 4.

**Problem.**

**(a) The flag records a mention, not a design.**

- Background sentences in abstracts match, for example "According to the Global Burden of Disease ...".
- Mendelian randomisation is a design based on GWAS summary statistics, and it matches even when mentioned in passing.
- `adverse event reporting system` matches VAERS as well as FAERS.
- No precision or recall is estimated.

**(b) The flag misses most existing-data research:**

- electronic-record and claims databases (CPRD, OpenSAFELY, TriNetX, Optum, MarketScan, VA);
- biobanks other than UK Biobank (FinnGen, All of Us, Million Veteran Program);
- surveys other than NHANES and BRFSS (NHIS, CHARLS, HRS, ELSA; KNHANES matches only through its long name);
- eICU;
- secondary analyses of trials;
- meta-analyses.

**(c) The comparison group is not "experimental".** "Other preprints" contain most of the existing-data work in (b). The medical analogue of an experiment is prospective collection of primary data: registered trials, prospective cohorts and laboratory studies. These can be flagged by registration identifiers such as NCT, ISRCTN and ChiCTR.

**(d) medRxiv is the wrong venue.**

- The formulaic genre built on NHANES and Mendelian randomisation [37,38,45] is a phenomenon of journals.
- medRxiv "is not intended for case reports (single or in series), narrative reviews, scoping reviews, systematic reviews without meta-analyses, editorials, letters, opinion pieces and hypotheses that lack data" (https://www.medrxiv.org/content/about-medrxiv).

**(e) Power is limited.** The minimum detectable effect is 1.17, so the null says nothing about modest effects.

**(f) The fastest-growing category is unexamined.** Health informatics grew 54% in 2026. It is where studies that evaluate LLMs sit: no-data or existing-data work, with AI as the topic.

**Why it matters.** C3 was meant to be "the limiting case" (l. 254). As built, it can neither confirm nor refute the existing-data arm of H1.

**Fix.**

- Hand-code about 200 flagged and 200 unflagged abstracts to estimate precision and recall.
- Fix an expanded list of sources in advance.
- Compare against prospectively registered trials.
- Replicate in PubMed with E-utilities counts by query.
- Split health informatics by AI topic.
- In the Discussion (l. 254), report the null as evidence against the existing-data arm in this venue. Do not move the limiting case to the published literature.

### M6. Alternative explanations get one sentence or none

**Location.** Limitations, l. 286. That passage has one sentence on collaborations and one on AI as a topic. It says nothing about funding, facility schedules, planning cycles, conference cycles or adoption curves.

**Problem.** Each of the following predicts part of the observed pattern without AI.

- **Funding.**
  - The US Congressional Research Service reports that "NIH awarded fewer awards in the 2025 time period compared with the average from 2020 to 2024". It adds that "as of November 28, 2025, HHS had terminated 977 NIH grant awards totaling $1.7 billion" (CRS IF13131, 11 December 2025, https://www.everycrsreport.com/files/2025-12-11_IF13131_63aaed675c9924bb0867a577571eb87d3451439c.html).
  - A funding shock in 2025 should depress US wet-lab output from 2026, more than computational output, because wet-lab costs are reagents, animals and people.
  - That predicts the 2026 wet-lab slowdown (+8%, against +13% in 2025) with no role for AI.
- **COVID-19.**
  - In 2020, hep-ex fell 28%; it then grew 29% in 2021 and 25% in 2022.
  - bioRxiv's wet-lab categories grew 58% in 2020.
  - The event-study and placebo coefficients for 2020–2021 in C1 and C2 are as large as the 2026 effects.
- **Facility schedules.**
  - LHC Run 3 runs until mid-2026, and Long Shutdown 3 starts at the beginning of July 2026.
  - RHIC's final run ended on 6 February 2026.
  - LVK O4 ended on 18 November 2025, and GWTC-4.0 with the O4a data was released on 26 August 2025.
  - These schedules move both experimental output and the availability of data in 2025–2028, which is exactly the window in which "later onset" would be judged.
- **Community planning and conference cycles.**
  - Snowmass 2021 contributions were due in March 2022 (M3).
  - The European Strategy for Particle Physics invited written input "by 31 March 2025" (CERN Courier, 19 September 2024, https://cerncourier.com/a/a-decider-for-cerns-next-collider/). The CERN Council adopted its 2026 update on 22 May 2026 (CERN/3997, https://council.web.cern.ch/sites/default/files/c-e-3997-Council%20Resolution%20on%20the%202026%20update%20of%20the%20European%20Strategy%20for%20Particle%20Physics.pdf).
  - Sensitivity studies for future colliders in hep-ex and hep-ph follow such cycles.
- **Collaboration processes.** Approval pipelines set the output of large collaborations, and that output is lumpy (section 2a).
- **Instrument time.** Beam, synchrotron, cryo-EM and telescope time are allocated in proposal cycles. AI can raise the number of proposals, not the time allocated.
- **Preprint habits and adoption.**
  - Particle theorists post nearly everything to arXiv; the share of PRD and JHEP articles with an arXiv version is 99–100% in INSPIRE, against about 65% for PRC. So a cheaper short note appears on arXiv first in theory.
  - Wet-lab biology was still adopting bioRxiv in 2019–2021.
  - Changes in posting propensity are not changes in output.
- **AI as a topic.** It is present in:
  - machine learning for physics (26% of the small-team hep-ex segment in both 2024 and 2026; unknown for the theory archives);
  - bioinformatics;
  - medRxiv's health informatics.

**Why it matters.** Each alternative is specific, dated and testable, mostly with data the companion already holds. Without these tests, the attribution to the cost of experiments is unearned.

**Fix.**

- Add a table of alternative explanations with the test for each (analyses 1, 2, 4, 5, 9).
- Write one Limitations sentence for each alternative that is not tested.

### M7. The mechanism is stated too strongly and makes no quantitative prediction

**Location.** l. 250: "generative AI lowers the cost of the steps that need only text, code or existing data ... while experiments cost what they did". Also the Abstract and the Conclusions.

**Problem.**

**"Experiments cost what they did" is too strong.** AI and ML have changed parts of experimental work:

- in particle physics: triggers, reconstruction and fast simulation;
- in biology: image segmentation, cryo-EM processing, structure prediction that replaces some structural experiments, protocol design and code to control instruments.

**What AI can compress in an experimental paper:** analysis code, plotting, statistics, literature search, writing, replies to referees, internal notes and talk write-ups.

**Why that need not show up in counts:**

1. **Amdahl's law.** Suppose a fraction f of the effort behind a paper can be compressed by a factor s. Output per unit effort can then rise by at most 1/((1−f) + f/s). The values below are illustrative:

   | f | s | Maximum rise in output per unit effort |
   |---|---|---|
   | 0.15 | 2 | 8% |
   | 0.15 | unlimited | 18% |
   | 0.7 | 2 | 54% |

2. **Fixed publication units.**
   - Collaborations publish one analysis per paper.
   - Biology journals expect a "complete story" and ask for revision experiments.
   - So saved time goes into more experiments, or more content per paper, rather than more papers.
3. **Lags and the drawer.**
   - Experimental projects take years.
   - Savings at the writing stage should still appear as a one-off rise in level.
   - Datasets left unwritten in drawers become cheaper to write up, so a burst is expected.
   - No burst is visible on bioRxiv (0.91 of trend).
4. **People and money.** The binding resources are trained hands and funding.

**Why it matters.** As stated, the mechanism fits any outcome and cannot be tested. Written as a production function, it yields tests.

**Fix.**

- State the mechanism with an explicit compressible share.
- Derive its predictions:
  - a dose–response across types of paper;
  - shorter lags from data to paper in experimental work, even with flat counts;
  - a burst from the drawer;
  - larger papers.
- Test at least one of them (analyses 3 and 6).

### M8. H3 is not measured in the contrasted groups, and the cited evidence partly cuts against it

**Location.** l. 105, l. 147, l. 236–238, l. 252; Table 6; Abstract ("Published estimates put AI-assisted writing in biology on a par with physics").

**Problem.**

**(a) No estimate covers the contrasted groups** (hep-ex, nucl-ex, bioRxiv wet-lab). Lin and Zhu [34] compare arXiv q-bio with physics, not bioRxiv with physics. The abstract's "biology" overreaches.

**(b) The evidence partly contradicts H3.** Kobak et al. [32] report about 20% in computational fields against at least 13.5% overall. Adoption for writing does differ with computational intensity, which is the very thing H3 says does not drive the result.

**(c) The marker analysis has not been reported.** It is specified in `methods.md` but has no results yet. Its planned regression codes "experimental" by category (wet lab = 1; theory = 0; mixed = 0.5). After section 2a, that coding is not credible for hep-ex.

**(d) H3's role changes now that H1 fails.** H3 was there to rule out writing adoption as the cause of differential growth. Within fields, that differential growth is not there.

**Fix.**

- Report marker prevalence with confidence intervals for exactly the contrasted groups. Where possible, also report it by type of paper within hep-ex.
- Revise the abstract sentence.
- Discuss Kobak et al.'s finding for computational fields.

### M9. The Discussion's reading of experimental fields is not fair to them

**Location.** l. 246, l. 252, l. 256.

**Problem.**

- **"Later onset rather than immunity" cannot be tested as written.**
  - Today's data are compatible with any later development. The sentence asserts that experimental science is not immune, which these data cannot show.
  - The framing treats experimental fields as late adopters rather than as fields whose output is produced differently.
  - Any rise in experimental particle or nuclear output in 2027–2028 would coincide with LS3 and with RHIC's analysis after its final run.
- **Laboratory automation.** "Laboratory automation could loosen the experimental bottleneck, first in fields with fast assays" is speculation without a citation. It also describes a different mechanism: generating more data, not cheaper writing. That mechanism would need its own measure.
- **"bioRxiv, mostly experimental work"** is asserted, not measured.
- **"Experimental physics stayed within its historical range"** is contradicted by hep-ex's departure from trend (1.37) and by M3(b).

**Fix.**

- Replace the "later onset" sentence with observable conditions: what would count as acceleration of experimental output, by when, and net of LS3, RHIC's post-run analysis and funding.
- Cite evidence for the automation sentence or cut it.
- Measure the experimental share of bioRxiv or drop "mostly".

### M10. The evaluation and policy sections do not follow from the evidence

**Location.** Introduction (l. 93) and Table 1; Discussion (D2, l. 258–266; D3, l. 268–282); Conclusions (l. 298).

**Problem.**

**What the counts cannot show.**

- D2 covers legitimacy, the invisibility of effort, the critique of rationing, and DORA/CoARA. D3 sets out seven recommendations. None of this is derived from preprint counts.
- The data cannot separate legitimate from illegitimate use; l. 260 says so itself.
- The data contain no measure of evaluation practice, of reading capacity or of the effects of caps. arXiv's cap starts after the study window.

**Claims that rest on H1 or on rhetoric.**

- The companion essay's thesis, that evaluation "is not ready for AI used well", is not tested here.
- With H1 failing, "the cost of producing a paper has fallen unevenly across kinds of work" (l. 260) is no longer supported within fields.
- The sentence on the Matthew effect (l. 264) is rhetoric.

**Scope.** The recommendations are honest about how weak their evidence is (l. 270). But they lie outside a PLOS ONE research article, whose conclusions must follow from its data.

**Why it matters.** Presenting these sections as conclusions of the article will lead editors and readers to discount the empirical work, which is the article's real contribution.

**Fix.**

- Reduce D2 to one paragraph on what counts can and cannot mean.
- Move D3, Table 1 and the critique of rationing to the companion essay [47], leaving a pointer of at most about 150 words.

### M11. The statistical plan in the manuscript is not the one that was run

**Location.** l. 151–171; note to Table 4 (l. 467); `stats/methods.md`.

**Problem.**

| Element | Plan in the manuscript | Analysis as run |
|---|---|---|
| Comparison | Period effects against a baseline: 2017–2022 for arXiv, 2019–2022 for bioRxiv | Event study with 2022 as the reference year |
| Fixed effects | — | Month fixed effects |
| Standard errors | Newey–West | Driscoll–Kraay |
| Model | Poisson, with a negative-binomial fallback | Poisson pseudo-maximum likelihood |
| Multiplicity | Bonferroni, with 98.3% CIs | Holm-adjusted p-values |

- **Both are defensible, but they differ.** The plan itself was fixed after the descriptive counts had been seen (l. 113).
- **The decision rule no longer fits.** It refers to adjusted intervals, which the Holm procedure does not produce directly.
- **The choice of reference year matters** (M3, M4).

**Fix.**

- Publish the plan as written, with a dated table of deviations and their reasons.
- Report the confirmatory estimates under the original specification as well.
- Keep every other analysis labelled exploratory.

---

## 4. Minor issues

**Abstract and Results text**

1. **"Outside their 2017–2025 range ... within theirs" (Abstract)** should be replaced (M3).
2. **"Published estimates put AI-assisted writing in biology on a par with physics" (Abstract)** concerns arXiv q-bio [34], not biology.
3. **l. 208: report hep-ph against hep-ex.** It is the closest pairing of theory and experiment: 18% against 14% in 2026, and equal growth since 2022. Do not report only hep-th against hep-ex.
4. **l. 212 and Table 3: discuss arXiv q-bio.** It fell 7% in 2026 while bioRxiv bioinformatics rose 27%. That cuts against a general acceleration of computational biology and is not discussed.
5. **l. 202: biology's position in 2026.** "Among the natural sciences, biology therefore differs from the other fields in 2026, not in its growth since 2022" should say that bioRxiv shows no departure from its pre-2023 trend (0.91 [0.71, 1.15]).
6. **l. 246 and l. 254 count the failures too low.** "One prediction of H1 is not borne out so far" understates the formal results: two of three contrasts fail and the third is fragile.

**COVID-19, bases and power**

7. **l. 121: the COVID-19 check is too narrow.** It covers two months of one year, while the baseline includes 2020–2021, when COVID-19 shares in immunology and microbiology were much higher. Flag every month, as is done for medRxiv.
8. **Fig 2 legend (l. 406).** The experimental index of 119 rests on a 2022 base inflated by Snowmass and by conference write-ups (M3). Say so.
9. **Table 3: add the experimental range excluding 2020–2022** (−7% to +9%).
10. **l. 165: say that the physics test was underpowered.** Its minimum detectable effect (1.21) is larger than the effect the abstract implies.

**Definitions and scope**

11. **l. 290: medRxiv excludes the cheapest genres too.** Note this for medRxiv as well as for bioRxiv (M5).
12. **S2 Appendix: explain hep-lat.** State why hep-lat is in neither group.
13. **S2 Appendix: name the physics subcategories.** Note that physics.ins-det and physics.data-an fall within the "physics" archive and therefore within the physics field series.
14. **Reconcile the physics field series.** l. 117 lists 9 groups of archives; `methods.md` says "the 13 physics archives".

**Physics heavy producers**

15. **l. 167 and `methods.md`.** Excluding papers with more than 50 authors is right. For particle and nuclear physics, use INSPIRE's author identifiers rather than name strings, and add fractional counting.

**Mathematics and figures**

16. **l. 250: soften the evidence for formal checking.** Mentions of Lean (1.6% against 1.0%) and of Erdős are thin evidence that formal checkability drives the mathematics result.
17. **Figures mark a single company's model release (24 July 2026) among the dates.** Given the competing-interests statement, use neutral markers, mark several releases or none, or drop the marker. The author note at l. 404 already raises this.

**Reporting order**

18. **Limitations (l. 292).** Say plainly in one place both that the contrasts were chosen after the descriptive counts had been seen and that two of the three failed. Reporting this is a strength.

---

## 5. Analyses to request, ranked by information value

These are also my answer to what would convince experimentalists:

- contrasts within the same people, the same collaboration or the same lab (analysis 7);
- methods against results within experiment (analyses 2 and 3);
- the time from data to paper (analysis 6).

### 1. Clean the reference period in physics and report pairs of archives

**What to do:**

- Re-estimate C1 with the Snowmass 2021 contributions removed from 2022.
- Remove conference papers in every year, or model them as their own series.
- Report hep-ph against hep-ex and nucl-th against nucl-ex separately.
- Report each archive's departure from trend on one figure.

**Cost.** Hours, since INSPIRE gives document types and conference links.

**Why it ranks first.** It decides whether any difference between theory and experiment exists in physics. My crude estimate is 1.02–1.04.

### 2. Break down hep-ex and nucl-ex by mode of production

**What to do:**

- Split each archive into papers with more than 300 authors, collaboration write-ups and small-team papers.
- Count separately by collaboration: ATLAS, CMS, LHCb, BESIII, Belle II, ALICE, STAR.
- Within the small-team segment, classify papers as new measurement, reanalysis of existing data, simulation or sensitivity study, method or ML or software, or review. Validate the classification by blind double coding.
- Data sources:
  - the arXiv metadata the companion has already harvested, which give author lists, collaboration names and, in the comments field, page counts and conference information;
  - or INSPIRE.

**Why it matters.** It tells whether experiment grew, or computation filed under experiment.

### 3. A pre-registered, paper-level test of the new-data hypothesis

**What to do:**

- Classify papers as needing new data at the margin or not, using abstracts and, for bioRxiv, the JATS full text (methods sections; data-availability statements with new GEO, SRA, PRIDE or EMPIAR accessions).
- Define the classifier on hep-ex and nucl-ex, where the idea arose.
- Pre-register predictions on the Open Science Framework.
- Test on held-out material:
  - experimental against theoretical papers within cond-mat, astro-ph, quant-ph and physics;
  - bioRxiv papers that deposit new data against those that do not.
- Optionally rank types of paper in advance by compressible share and test whether growth is monotonic in that ranking.

**Why it matters.** It is the only test of the mechanism that is not confounded by the taxonomy of archives and categories.

### 4. Inference at category level for C2, with AI as a topic separated out

**What to do:**

- Fit the mixed model, or run the permutation, described in M4.
- Report bioinformatics with and without papers on ML or AI topics, using the companion's text samples from March and September or a full harvest.
- Check for drift in category choice.

**Why it matters.** It decides whether the only passing confirmatory contrast survives as a claim about groups.

### 5. bioRxiv by the corresponding author's country

**What to do.** Compare US with non-US growth for wet-lab and computational categories in 2023–2026, using the API field `author_corresponding_institution`.

**Why it matters.** It separates the 2025 NIH funding shock from AI as the explanation of the 2026 wet-lab slowdown.

### 6. Time from data to paper in experimental work

**What to do:**

- **Particle physics:** measure the lag from a public preliminary result (ATLAS-CONF, CMS-PAS; both on CDS and INSPIRE) to the arXiv paper, and from the end of data-taking for the dataset used to the arXiv paper.
- **Biology:** measure the lag from the first public release of a deposited dataset (GEO, SRA, PRIDE) to the preprint.

**Why it matters.** This is the mechanism's most direct prediction for experimental fields. It can detect an effect of AI even when counts do not move.

### 7. Contrasts within the same people, using INSPIRE author identifiers

**What to do:**

- For experimentalists in large collaborations, compare their output outside the collaboration (phenomenology, ML, methods, talk write-ups) with their collaboration output, 2019–2026. If AI raises output where no new data are needed, the first should accelerate like theorists' output while the second does not.
- Compute the heavy-producer measures for physics with disambiguated identifiers.

**Why it matters.** It removes the confounds of field, funding and culture in one step.

### 8. C3 in PubMed, with validated flags and a prospective comparison group

**What to do.** Count, by quarter, PubMed records that analyse existing data, using an expanded list fixed in advance and validated by hand coding. Compare them with records that carry trial-registration identifiers.

**Why it matters.** It tests the existing-data arm where the formulaic genre actually lives.

### 9. AI as a topic, flagged in every group

**What to do:**

- Apply topic flags for AI and ML to the theory archives, hep-ex, bioinformatics and medRxiv's health informatics, using the same regular expressions as for mathematics.
- Re-run C1–C3 without these papers.

**Why it matters.** It separates AI as a topic from AI as a tool in all three contrasts.

---

## 6. Strengths to keep

- **The design.** Within-field contrasts, a fixed confirmatory family, negative controls, a placebo across archives and leave-one-out estimates are the right tools. They worked: they showed that C1 reflects heterogeneity between archives. Keep them in the main text and report what they found as a result, not as an embarrassment.
- **Honesty with inconvenient numbers.**
  - The medRxiv comparison was corrected for COVID-19 (the ×2.3 against ×1.6 claim).
  - The null C3 is reported.
  - The reversal of the biology contrast with a 2019 base is in the text.
  - "Dates are not causes" is said repeatedly.
  - Effects are reported as rate ratios with intervals, and minimum detectable effects are given.
- **Reproducible numbers.** Every descriptive figure I checked reproduces exactly from the companion files:
  - theory and experiment growth for 2023–2026, with their ranges for 2017–2025;
  - the paired archives;
  - growth of the three bioRxiv groups, and bioinformatics' 63% share;
  - the figures with 2019 as base;
  - the medRxiv counts of 405 and 915, the 38% COVID-19 share, and the ×2.5 and ×1.9 ratios.
- **The heavy-producer analysis of mathematics.** It uses namesake-robust variants, breaks results down by team size and author history, and states the left-censoring.
- **Transparency.** The AI-use statement and the process record are a model for this kind of work.
- **The question in H3.** Asking whether AI in the writing becomes AI in the volume is a good question. Keep it, measured in the right groups.

---

## Sources consulted on the web (accessed 16 October 2026)

- **arXiv category taxonomy** (https://arxiv.org/category_taxonomy): descriptions of gr-qc, hep-ex, hep-ph, hep-th, hep-lat, nucl-ex, nucl-th and physics.ins-det, quoted in 2a and M2.
- **CERN, updated accelerator schedule, 4 October 2024** (https://home.cern/updated-schedule-cerns-accelerators): LHC Long Shutdown 3 "scheduled to begin at the start of July 2026"; HL-LHC moved to June 2030.
- **Brookhaven National Laboratory, 6 February 2026** (https://www.bnl.gov/newsroom/news.php?a=122794): RHIC's final collisions on 6 February 2026, and analysis to continue.
- **LIGO–Virgo–KAGRA O4 wrap-up** (https://ligo.org/ligo-virgo-kagra-collaboration-successfully-wraps-up-its-fourth-observing-run/): O4 ran from 24 May 2023 to 18 November 2025.
- **EGO, 26 August 2025** (https://www.ego-gw.it/blog/2025/08/26/gwtc-4-0-updated-gravitational-wave-catalog-released/): release of GWTC-4.0 (128 new candidates) and of the O4a strain data.
- **Snowmass Steering Group message of 9 March 2022, forwarded on a JLab list** (https://mailman.jlab.org/pipermail/hps/2022-March/002209.html): contributed papers to arXiv by 15 March 2022.
- **CERN Courier, 19 September 2024** (https://cerncourier.com/a/a-decider-for-cerns-next-collider/): written input to the European Strategy invited "by 31 March 2025"; open symposium 23–27 June 2025; drafting session 1–5 December 2025.
- **CERN Council, CERN/3997, 22 May 2026** (https://council.web.cern.ch/sites/default/files/c-e-3997-Council%20Resolution%20on%20the%202026%20update%20of%20the%20European%20Strategy%20for%20Particle%20Physics.pdf): resolution on the 2026 update of the European Strategy for Particle Physics.
- **Congressional Research Service, IF13131, 11 December 2025** (https://www.everycrsreport.com/files/2025-12-11_IF13131_63aaed675c9924bb0867a577571eb87d3451439c.html): fewer NIH awards in 2025 than the 2020–2024 average; 977 NIH grants terminated by 28 November 2025.
- **medRxiv, About** (https://www.medrxiv.org/content/about-medrxiv): the genres medRxiv is "not intended for".
- **bioRxiv API documentation** (https://api.biorxiv.org/): fields of the details and publications endpoints.
- **INSPIRE REST API documentation** (https://github.com/inspirehep/rest-api-doc): endpoints and rate limits.
- **Gelman A, Stern H.** The difference between "significant" and "not significant" is not itself statistically significant. Am Stat. 2006;60(4):328–331. doi:10.1198/000313006X152649. Metadata verified on Crossref.

## The reviewer's own checks, for reproduction

**Recomputation from the companion files.**

- January–September growth by series and year, and its ranges.
- Ratios of rate ratios under several bases, from `within_field_quarterly.csv` and `data/raw/arxiv_archive_monthly.csv`.
- Growth by bioRxiv category, from `data/raw/biorxiv_category_monthly.csv`.
- The permutation in M4: all 455 choices of 3 "computational" categories among the 15 computational and wet-lab categories. Statistic: the ratio of the two groups' January–September 2026 sums to their base-period sums; one-sided rank.

**INSPIRE-HEP.**

- Endpoint: `https://inspirehep.net/api/literature?q=<query>&size=1` (`hits.total`), queried on 16 October 2026.
- Base query: `primarch hep-ex and de YYYY-01-01->YYYY-09-30` (likewise for nucl-ex and the theory archives).
- Clauses added to the base query:

| Clause | Selects |
|---|---|
| `ac > 300` | records with more than 300 authors |
| `ac 1->300 and collaboration:*` | records with 300 or fewer authors and a collaboration field |
| `ac 1->10 and not collaboration:*` | records with at most 10 authors and no collaboration field |
| `ac 11->300 and not collaboration:*` | records with 11–300 authors and no collaboration field |
| `tc c` | conference papers |
| `snowmass` | records that mention Snowmass |
| `cn "<collaboration>" and ac > 300` | papers of a named collaboration |
| `j <journal> and jy <year>` with `and arxiv_eprints.value:*` | journal articles, with and without an arXiv version |

**Caveats on the INSPIRE checks.**

- Conference tags may lag for recent records.
- "snowmass" matches the term anywhere in a record.
- The samples of 60 hep-ex and 30 nucl-ex records were drawn at random with fixed seeds and classified by me alone, from titles and abstracts.

These checks are meant to show that the requested analyses are feasible and to signal their likely direction. They are not substitutes for the analyses: the companion should redo them from its own arXiv metadata.
