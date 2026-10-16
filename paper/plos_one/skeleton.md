# PLOS ONE research article: skeleton and analysis plan (draft 0)

*16 Oct 2026. Target: PLOS ONE, Research Article. There is no fee for the author: EMBL's flat-fee agreement covers all PLOS journals for 2025–2026, with EMBL as the corresponding affiliation (confirm with the EMBL library). PLOS ONE judges technical soundness, not novelty. It does not take essays or opinion pieces, so interpretation belongs in the Discussion and must rest on the results or on cited evidence. The full essay goes to Zenodo as a companion preprint and is cited once.*

## Working titles

**Author's proposal (16 Oct):** "Generative AI is making current scientific metrics obsolete".

**Defensible variants that keep the claim:**
- **Is generative AI making publication counts obsolete? Evidence from preprint servers, 2020–2026** (recommended)
- Generative AI is eroding publication counts as a measure of scientific work: evidence from [N] preprints
- Publication counts are losing their meaning: AI-era growth concentrates where experiments are not the bottleneck

Earlier options:

1. When writing is cheap: generative AI accelerates scientific output where experiments are not the bottleneck
2. Generative AI is changing what publication counts measure: evidence from preprint servers, 2020–2026
3. Theory, computation and existing data: where generative AI has accelerated scientific output

## Thesis

Research evaluation relied on outputs being costly to produce. Generative AI lowers that cost even when it is used legitimately, so publication counts change meaning without anyone misbehaving.

The data show where this has already happened. Output has accelerated where the rest of the work is also cheap: theory, computation, existing data. In experimental work, AI is visible in the writing but much less in the volume of output. The acceleration is broad-based, not driven by a fringe. Institutions have responded by rationing, not by reforming what they count.

## Structure and weights (target 4,500–6,000 words plus Supporting Information)

### Introduction (~15%)
- **Framework:** the cost was the signal. Evaluation reads merit through counts of costly outputs, and AI lowers the cost even under legitimate use. Cite Hansen 2026, Blekhman 2026, Kusumegi et al. 2025 (only the reversal between complexity and quality), Hao et al. 2026 and Huang et al. 2026.
- **The gap:**
  - Field-level output studies exist (Nee et al. 2026; Hanson et al. 2024).
  - Prevalence of LLM-written text exists (Kobak et al. 2025; Liang et al. 2025; Lin & Zhu, preprint).
  - What is missing is (a) contrasts within each field between experimental and non-experimental work, (b) the distribution of who produces more, and (c) whether AI *use* translates into *output* where experiments bind.
- **Hypotheses:**
  - **H1.** AI-era acceleration of output is concentrated where the work beyond writing is also cheap: theory, computation, existing data. **In experimental work, AI shows in the writing but much less, or not yet, in output.**
  - **H2.** Where output accelerates, the shift is broad. It comes from many established researchers producing more, not from a few outliers.
  - **H3.** AI-assisted writing is widespread across fields, including experimental ones, so differences in output are not explained by differences in adoption.

### Materials and methods (~20%)
- **Data:** new preprints (first versions) per month or quarter, 2017–2026.
  - arXiv: per-archive annual pages and OAI-PMH metadata.
  - bioRxiv and medRxiv: monthly summaries and subject categories from the API details.
  - PsyArXiv, SocArXiv, EdArXiv: OSF API, first versions only.
  - Data retrieved 15–16 Oct 2026. Code and data go on Zenodo with a DOI.
- **Groups:**
  - Physics: theory (hep-th, hep-ph, gr-qc, nucl-th) vs experiment (hep-ex, nucl-ex).
  - bioRxiv: computational (bioinformatics, systems biology, genomics) vs wet lab vs mixed.
  - medRxiv: papers naming a public dataset (NHANES, UK Biobank, GBD, MIMIC, SEER, FAERS, BRFSS, Mendelian randomisation) vs the rest. COVID-19 is excluded.
- **Designs** (to be finalised in the analysis plan):
  1. Event-study and difference-in-differences contrasts within each field. Outcomes: log new preprints and year-on-year growth. Use placebo dates, plus break tests without a pre-specified date.
  2. Comparison with each series' own 2017–2025 range, and a synthetic control as in Nee et al. 2026.
  3. Heavy-producer distribution in arXiv mathematics, extended to theoretical physics and CS without AI research if feasible. Use a namesake-robust definition (full first names; drop the most frequent surnames), with team-size and subfield breakdowns.
  4. *(New, if feasible.)* Prevalence of LLM writing markers per category per quarter, using excess-vocabulary markers in abstracts in the style of Kobak et al. Cross it with the acceleration, interacted with experimental intensity. The question: does AI use predict output acceleration only where experiments do not bind?
- **Robustness checks:**
  - the 2022 base year (the COVID dip) against 2019;
  - aliases between arXiv archives;
  - OSF versioning;
  - arXiv rule changes: CS review/position papers, 31 Oct 2025; maths endorsement, 10 Dec 2025; English requirement, Feb 2026; the cap, 1 Oct 2026;
  - batch posting;
  - small series (experimental physics, about 430 papers per quarter).
- **AI disclosure (PLOS policy):** the tools, what they did, and how the author validated the outputs. The author re-runs and reviews all code. The process record goes in S1 Appendix.

### Results (~35%)
1. **Field-level growth since 2022 (Fig 1).** Q3 2026 index, with 2022 = 100:

   | Field | Index | Year on year |
   |---|---|---|
   | Medicine (excl. COVID) | 289 | +29% |
   | CS | 278 | +41% |
   | Mathematics | 219 | +78% |
   | Social sciences | 184 | +6% |
   | Physics | 162 | +26% |
   | Biology (bioRxiv) | 157 | +10% |

   bioRxiv grows steadily, with no break in 2026: +9.5% in 2023, +11.4% in 2024, +13.0% in 2025, +11.7% in Jan–Sep 2026.
2. **Experimental vs non-experimental work within fields (Fig 2). This is the core result for H1.** Growth Jan–Sep against the same months a year earlier:

   | Group | 2023 | 2024 | 2025 | 2026 |
   |---|---|---|---|---|
   | Physics theory | 0% | +6% | +6% | +20% |
   | Physics experiment | −7% | +7% | +9% | +11% |
   | bioRxiv computational | +7% | +9% | +20% | +18% |
   | bioRxiv wet lab | +9% | +12% | +13% | +8% |

   - **Physics.** Theory's 2026 growth is far outside its 2017–2025 range (−6% to +6%). Experiment stays within its own range (−13% to +22%). Pairs in 2026: hep-th +24% vs hep-ex +14%; nucl-th +16% vs nucl-ex +2%.
   - **Biology.** Computational work pulls ahead only from 2025, mostly in bioinformatics (+27% in 2026). Caveat: part of bioinformatics *is* AI research.
   - **Medicine.** medRxiv excluding COVID grows steadily (+21% in 2025, +22% in 2026). Papers naming a public dataset grow ×2.3, against ×1.6 for all preprints. Health informatics is +54%, epidemiology +32%. Where data already exist, even biomedicine accelerates.
   - **Reading for H1:** in experimental work the AI era is *visible in the writing but barely in the volume*. Growth stays at its historical pace.
3. **AI-assisted writing is widespread (H3).**
   - At the end of 2023: CS 22%, quantitative biology 11%, physics 10%, mathematics 3.5% (Lin & Zhu, preprint).
   - At least 13.5% of 2024 PubMed abstracts (Kobak et al. 2025).
   - Most 2025 PubMed Central papers (Holzwarth et al. 2026, preprint).
   - With design 4: our own marker prevalence by category.
4. **Who produces more (H2; Fig 3).** arXiv mathematics:
   - The heavy-producer share rose from 5.3% (Jan 2025) to 19.3% (Sep 2026); under the strict namesake-robust definition, from 3.0% to 6.2%.
   - In Q3 2026 there were 693 prolific authors. Of these, 143 were already prolific, 468 were previously active below five papers a quarter, and 82 were new.
   - The rise appears in every team size and every subfield, and starts in Mar 2026, seven months before arXiv's cap.
   - AI-tool mentions: 0.09% → 1.97% (a lower bound).

### Discussion (~25%)
- **D1. Why experimental science is less affected, so far (~5%).**
  - Mechanism: AI cheapens the steps that need only text, code or existing data and that can be checked cheaply; experiments cost what they did (Blekhman 2026). Hao et al. 2026 find that data availability "appears to be a major impacting factor".
  - Medicine shows the limiting case: once the data exist, output accelerates.
  - Lab automation could change this later. That would mean a later onset, not immunity.
- **D2. The system is not prepared for good use (~10%). This carries the essay's thesis as an interpretation of the results.**
  - The acceleration needs no misuse: H2 shows established researchers producing more. Counts therefore change meaning whatever the legitimacy of the work.
  - The effort becomes invisible: a paper with real experiments written with AI looks the same as one written by hand. This is an interpretation, not a finding; cite Kusumegi et al. (reversal) and Blekhman.
  - Institutional responses have been rationing: the NIH cap of six applications per researcher, arXiv's two submissions a month, and conference quotas (Table 1). Rationing restores scarcity but not the information that scarcity carried.
  - DORA and CoARA, in one paragraph: "largely unimplemented where measured, and mostly unmeasured" (McKiernan et al. 2019; Rice et al. 2020). Their remedy assumes reading capacity that the volume consumes.
- **D3. Implications (~5%).**
  - Count fewer outputs and read them, placing the cap with the evaluators who count, not with the servers that receive submissions.
  - Make effort visible for the outputs that count.
  - Reward exploration (Huang et al. 2026).
  - Measure model concentration in AI-use statements.
  - Add one sentence of outlook: what AI could do for science.
  - The author's own recommendations will be merged here.
- **D4. Limitations (~5%).**
  - Correlational design; markers are dates, not causes.
  - Detector and marker biases.
  - Namesakes, despite the robustness checks.
  - Preprints are not publications, and adoption differs by field.
  - arXiv's rule changes.
  - Small experimental series.
  - Part of the analysis code was produced with AI assistance and reviewed by the author.

### Supporting Information
- S1 Appendix: the process record (how the paper was made, time and cost, reading depth).
- S1 Table: rules and caps (Table 1 from the essay).
- S2–S4: per-category tables and robustness checks.
- Data and code: Zenodo DOI.

## Next steps
1. **Novelty check** against Nee et al. 2026 (arXiv:2609.04872) and any 2026 within-field studies.
2. **Analysis plan** (designs 1–4): exact specifications, inference, placebo dates, power for the small series.
3. **Run the analysis** in the companion session (data and scripts already exist there). The author reviews the code.
4. **Write.**
