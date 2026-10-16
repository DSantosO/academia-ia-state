# Review of "Generative AI is eroding publication counts as a measure of scientific work: evidence from 1.9 million preprints" (PLOS ONE, draft v1)

**Reviewer 2: scientometrics and preprint data. Round 1, 16 October 2026.**

**Materials examined.**
- The manuscript: `paper/plos_one/draft_v1.md`.
- Its figure data in `paper/figures/`: the companion README, `within_field_quarterly.csv` and `arxiv_math_prolific_robustness.json`.
- The companion branch `claude/happy-lovelace-wqek9b` at commit cb56c25: `data/raw`, `data/processed`, `scripts` and `docs`.
- The formal results added the same day, copied from companion commit 37b4b11: `paper/plos_one/stats/methods.md`, `results.md`, `field_tests.json`, `within_field_tests.json` and the new Fig 2.
- Their update at 18:08 (companion commit f5ab16e), which adds H2 results for physics (`heavy_producers.json`) and H3 marker results (`marker_tests.json`).
- Research notes 6 and 8.

**Conventions.**
- "My calculation" marks a number I computed from the companion's committed files; anyone can reproduce it from those files.
- Everything I checked online carries its URL.
- I have not edited the manuscript.

---

## 1. Summary

The manuscript asks whether the growth in preprint output since generative AI is concentrated where "the work beyond writing is also cheap". It uses:
- monthly counts of new preprints on arXiv, bioRxiv, medRxiv and three OSF servers up to September 2026;
- three within-field contrasts fixed in advance: theory against experiment in arXiv physics; computational against wet-lab bioRxiv categories; medRxiv preprints that name a public dataset against the rest;
- an analysis of heavy producers in arXiv mathematics, with authors matched by name;
- published estimates of how much scientific writing is LLM-assisted.

The draft reads the descriptive data as support for H1 and H2 and concludes that AI is changing what publication counts measure. The formal results now available do not support H1:
- the physics contrast is no larger than the typical difference between two arXiv archives, and it fails its own negative control;
- the biology contrast rests on bioinformatics alone and reverses with a 2019 base;
- the medicine contrast is null.

What survives is an arXiv-wide acceleration since late 2024. It includes experimental archives and is absent from bioRxiv, medRxiv and PubMed.

## 2. Overall assessment and recommendation

**Recommendation: major revision, with a change of question and framing. In its current framing (H1 supported; "eroding publication counts"), I would recommend rejection.**

**What the study does well.** It uses three servers and fixes its contrasts before running the models. It adds negative controls, placebos built from other archives and categories, leave-one-out estimates, minimum detectable effects and an unusually transparent pipeline. The descriptive numbers I recomputed reproduce.

**Why it falls short now.**
- **The conclusions outrun the data.** The title, Abstract, Results headings and Conclusions assert a pattern that the confirmatory tests do not support. That fails PLOS ONE's requirement that conclusions follow from the data.
- **Server mechanics are mixed with production.** Several measures confound research production with properties of the preprint servers themselves:
  - when and how papers are announced;
  - how archives alias categories and cross-list papers;
  - which genres a server accepts;
  - how it screens submissions;
  - how fast each field is adopting preprints.

  These are the standard traps of preprint scientometrics. They matter more here because the main surviving result is a difference between servers.
- **H2 is not yet secure for mathematics.** In the manuscript it rests on name strings with short histories and on a quarterly threshold dominated by the September 2026 spike, and its comparison with Nee et al. is not like for like. The companion's new decomposition, which avoids regression to the mean, exists only for physics. There it shows broad growth with modest concentration at the top.
- **H3 needs to rest on the new marker results.** In the manuscript it is argued from rankings across studies and from arXiv's quantitative-biology archive, while the within-biology evidence the paper cites points the other way. The companion's marker analysis now gives direct evidence:
  - similar relative rises in experimental and non-experimental groups;
  - similar relative rises on arXiv and bioRxiv.

  That evidence should replace the indirect argument, with its limits (word drift after 2024) stated.

**What a revised paper could be.** It would combine:
- a pre-specified test of the experimental-bottleneck hypothesis that comes out negative within fields;
- a careful account of an arXiv-wide acceleration that bioRxiv, medRxiv and PubMed do not show;
- server-level explanations that are tested rather than assumed (Section 7).

That would be useful and publishable. H2 and H3 need the checks in Sections 3 and 5 before they can carry conclusions.

---

## 3. Major issues

### M1. The confirmatory tests do not support H1; the paper must be reframed

**Location.**
- Title.
- Abstract: sentences 3–4, and "Output has grown fastest where the work beyond writing is also cheap, and much less, so far, in experimental work".
- Introduction (H1).
- Results, "Output grew fastest where experiments do not bind (H1)".
- Discussion: the first paragraph and "Why experimental science is less affected so far".
- Conclusions.

**Problem.** The formal estimates (`stats/results.md`):

- **Physics (C1).** The 2026 rate ratio is 1.14 [1.00, 1.30], Holm p = 0.11.
  - The negative control, hep-ex against nucl-ex, is larger: 1.39 [1.19, 1.64].
  - 61% of the 153 pairs of arXiv archives differ at least as much.
  - With 2019 as the base year the ratio is 1.05 [0.90, 1.23].
  - The event-study ratios for 2020 (1.25) and 2021 (1.19) exceed the 2026 value. Relative to experiment, 2022 was a COVID-affected low year for theory, so it is a poor base year.
- **Biology (C2).** The ratio is 1.08 [1.03, 1.14], Holm p = 0.0095.
  - Without bioinformatics it is 0.93 [0.89, 0.97].
  - With a 2019 base it is 0.87 [0.80, 0.95].
  - 20% of the 462 random halvings of the wet-lab categories differ by as much.
  - In January–September 2026, genomics (+6.9%) and systems biology (+5.1%) grew more slowly than cell biology (+12.8%) or microbiology (+11.9%) (companion `biorxiv_categories_growth.csv`).
- **Medicine (C3).** The ratio is 0.99 [0.88, 1.10]. The public-dataset share of non-COVID preprints is flat.
- **The descriptive criterion was already weak.**
  - The test "outside its 2017–2025 range" also flags astro-ph (+15.0% in January–September 2026, against a previous maximum of +12.5%) and cond-mat (+17.8%, against +10.0%). Observation and experiment dominate both archives.
  - hep-ex itself grew by 14.2%; only nucl-ex was flat (+1.8%).
  - The criterion is asymmetric. In 2017–2025 the standard deviation of annual growth was 3.5 points for the theory group but 9.2 for the experimental group, so the experimental series could hardly leave its range. (My calculations from `data/raw/arxiv_archive_monthly.csv`.)

**Why it matters.**
- PLOS ONE criterion 4 requires that conclusions follow from the data.
- The model-based intervals (Driscoll–Kraay, on two aggregated series) ignore heterogeneity between archives and between categories. The placebo benchmarks show that heterogeneity is as large as the effects, so the Holm p-value for C2 overstates the evidence.

**Fix.**
1. **Retitle and rewrite around the negative results.** Rewrite the Abstract and Conclusions to lead with the negative within-field results.
2. **Use the placebos for inference.** Make the placebo distributions (random splits of categories; all pairs of archives) the reference for inference on every contrast. Report the placebo p-value beside the Holm p-value.
3. **Fix the base year.** Treat the 2019 and 2022 bases symmetrically, or leave 2020–2022 out of the reference. Move the event-study panel (new Fig 2D) to the main text.
4. **Withdraw two findings.** Remove "AI is in the writing but not yet in the volume" and "experimental science is less affected so far" as findings. Blekhman's and Hao et al.'s arguments then serve as motivation, not interpretation.
5. **Report the one hint honestly.** The two most experimental or applied arXiv series did not accelerate: nucl-ex (2026 departure from trend 1.00) and physics.\* (1.06). That is compatible with an experimental bottleneck, but it is confounded with community and genre (Section 7).

### M2. arXiv papers are dated by announcement, not submission, so monthly timing and the Q3 headlines depend on moderation throughput

**Location.**
- Methods, "arXiv mathematics metadata" ("dated by the month of its first version, read from its identifier").
- Abstract and Table 2: growth in Q3 2026 against Q3 2025.
- Results (H2): "The rise therefore began seven months before arXiv's cap".
- Robustness checks, "arXiv rule changes".
- Fig 3 and S1 Fig.

**Problem.**

- **Identifiers record announcement.** arXiv assigns the identifier when the paper is announced: "The final arXiv identifier is assigned as part of the automated process when the work is announced" (https://info.arxiv.org/help/availability.html). YYMM is therefore the month of announcement. The per-archive statistics also count announced papers.
- **Papers were being held in 2026.** arXiv's post of 1 October 2026 (https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/) says that:
  - a small share of authors delayed other authors' papers "by days or weeks";
  - rate limiting was already policy before October, applied mostly at moderators' discretion;
  - held submissions can spill into the next month.

  The draft's statement that the cap "cannot have caused a rush" therefore holds for the formal cap, but not for discretionary limits and holds.
- **September 2026 was a spike on arXiv alone.**
  - Year on year: mathematics +110% (8,919 against 4,252), hep-ph +55%, cs +52%. bioRxiv rose only 5.8% (5,049 against 4,770) and medRxiv 11% (my calculations).
  - Mathematics grew 33.5% in January–August but 78% in Q3.
  - The synthetic-control gap for mathematics is near zero until April 2026. It then rises through May–September: 7.6%, 9.5%, 17.1%, 31.0% and 39.8% (`stats/field_tests.json`).
  - arXiv became an independent nonprofit on 1 July 2026 and is completing a migration to cloud infrastructure (Cornell Chronicle, 29 June 2026, https://news.cornell.edu/node/333261). No change to moderation was announced, but the timing should be checked.
- **The January 2025 baseline is not like for like.**
  - The OAI harvest drops records created before 1 January 2025 (`--min-created`). That removes papers submitted in December 2024 but announced in January 2025 under 2501 identifiers.
  - The OAI count is 12.7% below the per-archive count in January 2025 and 11.6% below it in January 2026, against 6.0–8.7% in every other month (my calculation).
  - January 2025 is the starting point of several headline comparisons: 3,197 papers, a 5.3% prolific share, a 30.0% single-author share and 0.09% of papers mentioning AI.
- **The prolific flag cannot date the rise.** It uses whole-quarter totals, so the July and August 2026 values already include September's papers.

**Why it matters.** Break dates, "began in March 2026", the Q3 growth rates and the reading of the cap all depend on how papers are dated.

**Fix.**
1. **Date papers by submission.** Use each paper's v1 submission time (OAI `created`; Atom `published`). Report how long papers took from submission to announcement, by month and archive, for 2024–2026.
2. **Re-run timing on submission dates.** Repeat the break tests and the H2 timing analysis on submission dates, counting each author's papers in a trailing 90-day window.
3. **Change the headline windows.** Lead with growth over January–August, January–September and the trailing twelve months. Keep Q3 against Q3 as a secondary figure.
4. **Reconcile the two arXiv sources.** Compare per-archive and OAI counts month by month, and fix the January 2025 boundary of the harvest.
5. **Ask arXiv for its numbers.** Request monthly moderation statistics by archive for 2024–2026: holds, rejections and reclassifications.

### M3. Count definitions differ between sources and from Nee et al.

**Location.** Methods, "arXiv archives"; Table 2; the N in the title; Results (H2), the comparison with Nee et al.; Introduction, the description of Nee et al.

**Problem.**

- **Nee et al. count list entries, which include cross-lists.** Their archive figures match the companion's counts of new papers plus cross-lists almost exactly. My calculations for January–August 2026 against the same months of 2025:
  - hep-th: +1,037 (+20.5%), against Nee's +1,030 (+20.3%);
  - quant-ph: +3,028 (+30.2%), against Nee's +3,026 (+30.2%);
  - mathematics: 47,142 entries, against Nee's 47,127.

  The manuscript's primary-only counts give different growth: hep-th +23.3% and quant-ph +34.5%.
- **Aliases double-count.** Six pairs of categories are aliases of each other: math-ph/math.MP, cs.IT/math.IT, cs.NA/math.NA, math.ST/stat.TH, eess.SY/cs.SY and econ.GN/q-fin.EC.
  - Because of them, archive sums run about 5% above arXiv's own total.
  - The physics and mathematics series overlap through math-ph.
  - N = 1,944,974 counts some papers twice.
- **Nee et al.'s author panel uses different rules** (https://arxiv.org/html/2609.04872v1, Section 3.2 and Appendix B):

  | | Nee et al. | This manuscript |
  |---|---|---|
  | Source | Atom API | OAI-PMH |
  | Papers | any submission with a math.\* category, cross-lists included | primary category in mathematics only |
  | Author key | exact Unicode-normalised display name, hashed; accents not removed | accents removed, lower case, letters only |
  | Window | January–August 2025 against January–August 2026 | Q3 2025 against Q3 2026 |
  | Threshold | ≥5 submissions in eight months | ≥5 papers in a calendar quarter |
  | Share of author units at or above threshold | 2.45% (1,234 of 50,302) → 3.80% (2,241 of 58,930) | 0.6% → 2.5% |

  The rise is about 1.55-fold in Nee et al. and about 4.4-fold here. That gap is informative; it is not "consistent in direction".

**Fix.**
1. **One record, one primary category.** Build every arXiv series from record-level metadata, assigning each paper to its primary category once, and remove duplicates from N.
2. **Show both definitions.** Report key results with primary-only counts and with entries that include cross-lists.
3. **Replicate Nee et al. before comparing.** On the OAI harvest, reproduce their panel exactly: cross-lists included, exact display names, January–August windows.
4. **Name the unit when citing them.** When citing Nee et al.'s 11.9%, say that it rests on list entries.

### M4. The bioRxiv contrast is confounded by preprint adoption, COVID-19, author-chosen categories and screening

**Location.** Methods, "bioRxiv" and "Groups for the within-field contrasts: Biology"; Results, "Computational and wet-lab biology"; S2 Appendix.

**Problem.**

- **Preprint adoption.** Wet-lab fields adopted bioRxiv later; bioRxiv itself grew 40% in 2019 (research note 8).
  - The 2019 event-study coefficient, 1.24 [1.14, 1.36], shows computational categories already losing ground relative to wet lab between 2019 and 2022, before ChatGPT. The choice of base year therefore decides the sign of C2.
  - Funder mandates also shift adoption. Since 1 January 2025 the Gates Foundation has expected the manuscripts it funds "to be shared promptly in the form of a preprint" (https://openaccess.gatesfoundation.org/open-access-policy/). That bears mostly on global health, infectious disease and microbiology.
- **COVID-19.** The per-category counts include COVID-19 preprints.
  - The draft's shares (5.1% computational, 5.9% wet lab) come from May–June 2022 only, while the reference years before 2022 span the 2020–2021 surge.
  - Even in May–June 2022, COVID-19 preprints were 23% of immunology and 11% of microbiology (my calculation from `data/raw/biorxiv_covid_sample_2022.csv`).
- **Screening inside the baseline.** In 2020, preprint servers stopped posting purely computational COVID-19 drug-repurposing papers. Sources: Kwon, *Nature* 2020;581:130–131, doi:10.1038/d41586-020-01394-6; Muratov et al., *Chem Soc Rev* 2021;50:9121–9151, PMC8371861. That rule acted on the computational categories.
- **Categories.** The submitting author chooses the category.
  - Machine-learning methods papers cluster in bioinformatics, where AI is often the topic rather than the tool.
  - Genomics includes much sequencing work done at the bench.
- **A change of platform.** bioRxiv and medRxiv moved to openRxiv in 2025. Their preprints now carry DOIs with the prefix 10.64898; Crossref lists ref. 63 under that prefix as a bioRxiv preprint. Check for level shifts at the change of submission system.

**Fix.**
1. **Remove COVID-19 papers record by record.** Harvest every record from 2019 onwards; the API returns title, abstract, category, version and date. Build category series without COVID-19 preprints.
2. **Classify papers by content, not category.** Decide for each paper whether it analyses existing data only or reports new bench data. Use a classifier validated on a few hundred hand-coded abstracts, stratified by category, and report its precision and recall.
3. **Set AI-topic papers apart.** Separate papers about AI or machine learning, as the companion already does for computer science.
4. **Normalise by journal output.** Divide each category by journal output in the matching subfield (from OpenAlex or PubMed). That separates the propensity to post preprints from the production of research.
5. **Use category-level permutation inference as the main inference.**

### M5. The medRxiv COVID-19 filter and public-dataset flag are unvalidated, and medRxiv may be the wrong place to look

**Location.** Methods, "medRxiv" and "Groups … Medicine"; Results, "Medicine"; Table 3; S2 Appendix (regular expressions).

**Problem.**

- **The COVID-19 filter removes more than COVID-19 research.**
  - The expression searches title and abstract, so it also drops non-COVID research that mentions the pandemic only as context. Such mentions were commoner in 2021–2023, so the filter inflates later growth.
  - With title-only matches (column `covid_title` of the companion's `medrxiv_covid_monthly.csv`), the index for Q3 2026 is 271 rather than 289, and growth in 2023 is 28.1% rather than 33.5% (my calculation).
  - I drew a sample through the medRxiv API: 883 new preprints posted on 1–15 September 2026. Sixteen matched only in the abstract, and most of these mention the pandemic as context, for example trends "disrupted by COVID-19".
  - The expression also matches "Covidence", a review-screening tool, but only once in the 1,269 abstracts I sampled. That is negligible.
- **The public-dataset list is incomplete and unvalidated.**
  - It omits four of the nine datasets Spick et al. identified: FinnGen, CHARLS, CDC WONDER and TriNetX.
  - It misses KNHANES (excluded by `\bNHANES\b`), NHIS, NIS, eICU, "MIMIC IV" written with a space, and MIMIC-CXR.
  - It includes UK Biobank and the Global Burden of Disease study. Output from both follows data releases and collaborator cycles.
  - Precision and recall are not reported, and the draft does not say when the list was fixed.
- **medRxiv may miss the formulaic papers.**
  - Formulaic secondary-data papers are mostly submitted straight to journals.
  - medRxiv adds health-related screening and requires author declarations.
  - A null result on medRxiv therefore says little about the published literature that Spick et al., Suchak et al. and Maupin et al. document.

**Fix.**
1. **Validate both flags** on hand-coded samples, and report the title-only COVID-19 filter as a bound.
2. **Pre-declare an extended dataset list** as a sensitivity analysis, and state when the list was fixed.
3. **Add a journal version of C3.** Using OpenAlex, compare papers that name the datasets with other papers in the same journals, 2019–2025. This tests where such papers actually appear.
4. **Consider a genre contrast within medRxiv**: systematic reviews and meta-analyses, which need only text and existing data, against trials and other studies that collect new data.

### M6. H2 cannot yet separate "many established authors producing more" from namesakes, newcomers, batch posting and a few high-volume submitters

**Location.** Methods, "Heavy producers"; Results (H2); the Abstract's "611 of 693 prolific authors had posted mathematics papers in earlier quarters"; Table 5; Discussion, "Counting outputs when AI is used legitimately".

**Problem.**

- **Histories are short, and there is no base rate.**
  - Histories go back only to January 2025, six quarters.
  - With name strings, a common name nearly always "has earlier papers", because several people share it.
  - The 611 of 693 has no base rate. What share of all author names in Q3 2026, or of non-prolific ones, had earlier papers?
- **The stricter variants also filter by ancestry.**
  - They drop the 407 most frequent surnames, which hold 35.7% of author slots and are mostly East Asian.
  - The similar threefold rise under every variant is reassuring about namesakes, but it says nothing about who the prolific authors are.
- **Namesake collisions grow with volume.** Papers rose 80% and distinct names 41%, so more different people share a name string by chance. No null model is reported.
- **September and batch posting.** Q3 2026 contains the September spike: 8,360 of its 19,562 papers. Batch posting is not measured.
- **The endorsement change shifts who submits.**
  - Since 10 December 2025 in mathematics, and 21 January 2026 in all sections, automatic endorsement of new submitters requires prior authorship as well as an institutional email (https://blog.arxiv.org/2025/12/10/updated-endorsement-policy-for-arxiv-mathematics/).
  - That shifts submissions towards established, endorsed submitters, which raises the "established" share mechanically. The draft treats the change only as a barrier to newcomers.
- **Two accounts the Discussion has not yet met.** The claim that the acceleration "needs no misuse" must confront:
  - arXiv's own account: a small share of authors submitting many low-quality, thin, "salami" and densely AI-written papers (rate-limit post);
  - Nee et al.'s panel, where concentration rose:
    - Gini 0.272 → 0.313;
    - the most submissions by one author unit 20 → 44;
    - high-output units with no matched earlier activity 90 → 267.
- **A simple cross-sectional description of breadth is already in the data** (my calculation from `arxiv_math_prolific_robustness.json`):
  - Papers with no author above the threshold grew from 10,271 to 16,013 (+56%) between Q3 2025 and Q3 2026.
  - Papers with such an author rose from 575 to 3,549; about 196 to 1,148 under the strictest variant.

  This compares two cross-sections. It does not attribute growth to particular people.
- **The right attribution test exists, for physics only.** The companion's decomposition ranks authors on their combined output in both years, which avoids regression to the mean (`stats/methods.md`, f5ab16e). For physics theory, Q3 2025 → Q3 2026 (all names, ≤50 authors):
  - total output +26.2%;
  - top 1% +47.4%; next 9% +36.9%; bottom 90% +20.4%;
  - shares of the change 12%, 35% and 53%.

  That is broad growth with modest concentration. The draft's phrase "not from a few outliers" should become "broad, with the top growing fastest". This matches the rising Gini in Nee et al. The same analysis is missing for mathematics, the field on which the manuscript's H2 rests.

**Fix.**
1. **Long histories.** The companion's new OAI harvest starts in January 2019, giving up to six years of history; harvesting from 2010 would give fifteen.
   - Define "established" as having a paper before 2023.
   - Compare the prolific authors with the base rate among non-prolific names.
   - Run the combined-output decomposition for mathematics, under each namesake variant.
2. **Bound the namesake error.**
   - Add a simulated null for namesake collisions.
   - Add a subsample matched on identifiers (OpenAlex author IDs or ORCID).
3. **Measure batch posting** from submission times: the share of an author's quarterly papers submitted within seven days.
4. **Decompose the growth.**
   - Separate growth from more active names (the extensive margin) from growth in papers per name (the intensive margin).
   - Report the concentration shares (top 1% and top 10% of fractional output) for mathematics, as the companion now does for physics.
5. **Replicate Nee et al.'s definitions** (M3).
6. **Exclude collaboration papers in physics.** Keep the cut at more than 50 authors. Without it, white papers signed by hundreds of theorists made 16.9% of active theory authors "heavy producers" in Q3 2025, against 1.3% with the cut (`methods.md`).
7. **Use Q4 2026 as a test.**
   - Under a per-submitter cap, broad growth predicts stable totals and a falling heavy-producer share.
   - The cap binds submitters, not co-authors, so the test is imperfect.

### M7. H3 rests on rankings across studies and on arXiv q-bio, and the within-biology evidence cited points the other way

**Location.** The Abstract's "Published estimates put AI-assisted writing in biology on a par with physics"; Introduction (H3); Results (H3); Table 6; Discussion.

**Problem.**

- **"Biology" here is arXiv's quantitative-biology archive.** Lin and Zhu's biology group is q-bio. It is computational and small: 2,655 papers in 2023 against 84,966 in physics, per their Table 1 as recorded in research note 8. It is neither bioRxiv nor wet-lab biology.
- **The direct bioRxiv evidence is missing.** Liang et al. (*Nat Hum Behav* 2025) analyse bioRxiv, but Table 6 omits their bioRxiv series. Their published values for each corpus were not read; the article is not open access.
- **The cited within-biology evidence points the other way.** Kobak et al. find computational fields at about 0.20, against at least 0.135 overall. Within biomedicine, then, LLM-assisted writing is commoner in computational fields. That is exactly the confound the within-field contrast was meant to exclude.
- **Kusumegi et al. are cited selectively.** They estimate that output rose by 36.2% on arXiv, 52.9% on bioRxiv and 59.8% on SSRN after authors adopted LLMs (*Science* 2025;390(6779):1240–1243). The manuscript cites them only for the reversed relationship between complexity and quality. Renault et al. (*PNAS* 2026) argue that this design produces spurious post-adoption dynamics. Both belong in the paper.

**Fix.**
1. **Make the marker analysis core.** Run the marker analysis described in `methods.md` by bioRxiv category and arXiv archive.
   - Add Liang et al.'s distributional estimator as a second method, because Kobak's word list was derived from PubMed.
2. **Read Liang et al.'s values** for bioRxiv and physics.
3. **Rewrite the sentence in the Abstract.**
4. **Reconcile micro and macro.** Explain how the gains Kusumegi et al. associate with adoption on bioRxiv fit with the absence of any aggregate acceleration there.

### M8. Server policies, screening and method changes are incompletely documented; the social-science series should be fixed or dropped

**Location.** Robustness checks, "arXiv rule changes"; Limitations ("… were not examined"); the note to Table 1; Data sources, "Social sciences"; Table 2; Fig 1.

**Problem.**

- **arXiv.**
  - The draft omits:
    - discretionary rate limiting and holds before October 2026;
    - the limit of three active submissions (2024);
    - the one-year ban (May 2026);
    - independence on 1 July 2026.
  - The post on review and position papers itself points research on societal impact to cs.CY and physics.soc-ph (https://blog.arxiv.org/2025/10/31/attention-authors-updated-practice-for-review-articles-and-position-papers-in-arxiv-cs-category/). The paper should test whether AI- and ML-related papers moved into non-CS primary categories.
  - q-bio fell 7% in January–September 2026 after growing 16–19% a year in 2023–2025. The fall coincides with the extension of the endorsement rule on 21 January 2026, and q-bio draws many newcomers.
- **bioRxiv and medRxiv.**
  - I found no published 2025–2026 policy on AI-generated or formulaic papers.
  - openRxiv's Richard Sever has said that bioRxiv also sees more such submissions (https://www.the-scientist.com/arxiv-takes-the-first-step-to-combat-ai-slop-in-submissions-74586).
  - The load on screening is measurable. Under the new prefix, the DOI suffix appears to carry the submission date: 10.64898/2026.08.26.26361384, for example, was posted on 2026-09-01. The monthly lag from submission to posting is a proxy for that load.
  - openRxiv could be asked for monthly counts of declined submissions.
- **OSF.**
  - The counting method switches from API totals to paging `_v1` records exactly at 2025-Q1, the start of the period of interest.
  - SocArXiv "generally" allows no more than one paper per author per week (policy dated 8 March 2026, https://socopen.org/ai-policy/).
  - The README says SocArXiv required ORCID and moved humanities elsewhere in November 2025. Both claims are unsourced; the AI-policy page states neither.
  - EdArXiv rose from about 60 to about 400 preprints a quarter.

**Fix.**
1. **Add a dated timeline** of policies and operations for each server, with sources, and include the dates as indicators in the models.
2. **Validate the OSF method.** Apply the paged `_v1` count to the 2023–2024 quarters; `osf_check_quarter.py` already does this.
3. **Drop or demote the social-science series.** Remove it from Fig 1 and Table 2, or move it to the Supporting Information with explicit caveats.

### M9. Positioning, missing literature and reliance on recent preprints

**Location.** Introduction, paragraphs 4–6; Discussion; references.

**Problem.**

- **Positioning.** The positioning against Nee et al. and Qi et al. has to change; see Section 7.
- **Core scientometric literature is missing.** I checked each DOI or arXiv identifier below in Crossref or on arXiv.
  - Preprint adoption and the servers:
    - Abdill & Blekhman 2019, *eLife* 8:e45133;
    - Sever et al. 2019, bioRxiv 10.1101/833400;
    - Krumholz et al. 2020, *JAMA* 324:1903;
    - Fraser et al. 2021, *PLoS Biol* 19:e3000959;
    - Larivière et al. 2014, *JASIST* 65:1157;
    - Wang, Chen & Glänzel 2020, *J Informetr* 14:101097 (mathematics).
  - Hyperprolific authors:
    - Ioannidis, Klavans & Boyack 2018, *Nature* 561:167;
    - Ioannidis, Collins & Baas 2024, *Scientometrics* 129:5783 (already used in `methods.md`).
  - Author-name disambiguation:
    - Milojević 2013, *J Informetr* 7:767;
    - Kim & Diesner 2016, *JASIST* 67:1446.
  - Growth of science: Bornmann, Haunschild & Mutz 2021, *Humanit Soc Sci Commun* 8:224.
  - GenAI and productivity in the social sciences: Filimonovic, Rutzer & Wunsch 2025, arXiv:2510.02408.
  - Methods now used:
    - Abadie, Diamond & Hainmueller 2010, *JASA* 105:493;
    - Driscoll & Kraay 1998, *Rev Econ Stat* 80:549.
- **The core framing leans on a six-week-old preprint.** Nee et al. was posted in cs.DL on 4 September 2026.
  - Its arXiv record spells the first author's given name "Xiaoshn".
  - It names a submitter, Xiao-Sheng Ni, who differs from the listed author, Xiaomin Ni.
  - The companion reproduces both Nee et al.'s input series and their synthetic-control estimate, so the paper can rest on its own replication.
- **Much of the Discussion is not tested by these data.** Table 1, rationing, DORA/CoARA and the seven recommendations bring in about 25 references, among them an X post and three news items. The study's data do not evaluate any of this. Cut it to one paragraph or move it to the companion essay.
- **Three RECHECK markers I can resolve.**
  - Nee et al.'s panel: windows January–August 2025 against January–August 2026; exact display names; Atom API; cross-lists included.
  - "Newly prolific" in `robustness_math_prolific.py` means a Q3 2026 prolific name whose largest quarterly count from 2025-Q1 to 2026-Q2 was below five, including names with no earlier paper.
  - Ref. 63: Crossref lists it as a bioRxiv preprint, posted 3 June 2026.

### M10. Data availability, reproducibility and terms of use

**Location.** Data availability; Software and data processing; Ethics; S1 Data.

**Problem.**

- **Aggregates cannot be re-checked.** Aggregate counts alone cannot reproduce the regex flags, the namesake variants or the per-author measures.
- **The sources change over time:** arXiv's statistics pages and OAI datestamps, bioRxiv categories and OSF versions.
- **The scripts exceed published request limits.**

  | Script | What it does | Published limit |
  |---|---|---|
  | `harvest_arxiv_oai.py` | sleeps 2 s between requests | arXiv's API terms: "no more than one request every three seconds" over "a single connection" (https://info.arxiv.org/help/api/tou.html) |
  | `fetch_arxiv_years.sh` | sleeps 1 s between requests | arXiv's robots.txt: "Crawl-delay: 15" (https://arxiv.org/robots.txt) |
  | bioRxiv and medRxiv harvests | run 4–6 workers in parallel | the API publishes no terms (https://api.biorxiv.org/) |

- **Licences and personal data.**
  - arXiv metadata are CC0, and the terms allow users to "retrieve, store, transform, and share" them.
  - Hashed author names remain personal data under the GDPR, which treats pseudonymised data as personal data (Recital 26).

**Fix.**
1. **Deposit on Zenodo:**
   - the raw retrievals, with timestamps;
   - record-level lists of identifiers with derived flags for each paper: primary category, submission and announcement dates, number of authors, and the COVID-19, public-dataset, AI, Lean, Erdős and prolific flags;
   - the code, with a pinned environment and a single command that rebuilds everything;
   - a frozen arXiv OAI snapshot (CC0), or at least the identifiers with their datestamps.
2. **Release name strings only with the approval of EMBL's data-protection office.**
3. **Respect the published limits.** Set the scripts' default request rates to them, and state compliance in Methods.
4. **State licences:** CC0 for the data, MIT or BSD for the code.

---

## 4. Minor issues

1. **Title.**
   - "Evidence from 1.9 million preprints" counts aliased papers twice (M3).
   - It also sits close to Qi et al.'s "two-million preprints".
2. **Methods wording.** "Dated by the month of its first version" should read "dated by the month in which its first version was announced" (M2).
3. **hep-lat is unused.** It is in the physics series but in neither group. It is computation-heavy (2026 departure from trend 1.39) and could serve as a computational third arm of C1.
4. **Table 2.**
   - It sets year-on-year growth for Q3 beside "last four quarters against 2022".
   - The 2022 base is depressed for bioRxiv (35,750, below 2020 and 2021) and for medRxiv.
   - Drop the column, or justify it against the caption's own warning about comparing fields.
5. **Table 3, footnote a.** medRxiv's +34% in 2023 is +28% under a title-only COVID-19 filter (M5).
6. **Model-release markers in the figures.**
   - The figure files for Figs 1 and 3 label the 24 July 2026 marker with one vendor's model.
   - Given the competing-interests statement, and given that nothing here tests model releases, drop model markers.
   - If markers are wanted, mark operational events instead, such as arXiv's independence on 1 July 2026.
7. **Two name normalisations.** H2 reports figures from two normalisations (19.3% in the figure, 19.2% in the script). Use one.
8. **Precision of the mention patterns.** Report the precision of the AI, Lean and Erdős patterns on 100 random matches.
   - `\bin Lean\b` and `o[134]` can match text unrelated to AI.
   - An AI mention in the comments field may only acknowledge language editing.
9. **Word boundary.** Add `\b` before `covid`. The effect is negligible (M5).
10. **Which arXiv count is which.** "40,363 submissions in September 2026" is arXiv's figure for all submissions. The series are announced new papers by primary archive. Say which is used where.
11. **Retrieval dates.** Give the date of each retrieval: OAI mathematics on 15 October, OAI physics on 16 October, bioRxiv categories on 16 October, and so on.
12. **Terminology.**
   - Five papers a quarter is about twenty a year; Ioannidis et al.'s "hyperprolific" threshold is 72 a year.
   - Define the term used in the manuscript ("prolific" or "high-output") so readers do not equate the two.
13. **References.**
   - Ref. 4 (Kusumegi et al.): add issue 6779 and the date, 18 December 2025.
   - Ref. 40 (Renault et al.): say that it is a comment on ref. 4.
   - List Spick et al.'s nine datasets in Methods: FAERS, NHANES, UK Biobank, FinnGen, GBD, MIMIC, CHARLS, CDC WONDER and TriNetX.
14. **"Fixed before growth was examined"** (Fig 2 legend). The essay session had already seen growth at field level. State precisely what was known when the groups were fixed.
15. **Partial October 2026.** By about 15 October, arXiv mathematics had 4,513 new papers, on September's pace. Mention it as something to follow up, without drawing conclusions.
16. **medRxiv's early months.** medRxiv opened in June 2019, so a mid-2019–2022 baseline reflects the server's own adoption, as the companion notes. Say so in Methods.

---

## 5. Analyses or data checks to request, ranked by information value

1. **Re-date arXiv papers by submission time.**
   - Measure the time from submission to announcement, by month and archive.
   - Obtain arXiv's moderation statistics.
   - This separates production from throughput for the September 2026 spike, the July–September jump and "began in March". It is cheap: the fields are already harvested. (M2)
2. **Break the arXiv acceleration down by genre and topic,** by archive and month:
   - proceedings: "proceedings", "talk" or "contribution to" in the comments field, or a journal reference to PoS, EPJ Web of Conferences or Journal of Physics: Conference Series;
   - reviews, surveys, lecture notes, comments, replies and white papers: from titles, comments, and MSC 00 or 01 in mathematics;
   - papers about AI or machine learning: cs.\* cross-lists and vocabulary.

   This is the most direct test of why experimental archives accelerate on arXiv but not on bioRxiv, which does not accept reviews, opinion pieces or white papers. (Section 7)
3. **Find who drives the growth.**
   - Long author histories, harvested through OAI from 2010.
   - Growth from more active names against more papers per name, and the contribution of the top 1%.
   - A subsample matched on identifiers (OpenAlex or ORCID).
   - Country composition from OpenAlex affiliations.
   - An exact replication of Nee et al.'s panel. (M3, M6)
4. **Separate the propensity to post from production.**
   - Coverage ratios: the share of journal articles with an arXiv or bioRxiv version, by field, country and year (OpenAlex).
   - Trends in journal output itself.
   - The share of new arXiv papers already published when posted: a journal reference or DOI at v1, or a journal date before v1. (M4, Section 7)
5. **Classify papers by content.**
   - Use a validated classifier to separate experimental from non-experimental content in hep-ex, astro-ph, cond-mat, physics.\* and bioRxiv.
   - Split hep-ex and astro-ph by team size: collaboration papers against small-team papers. (M1, M4)
6. **Rebuild the bioRxiv categories without COVID-19 preprints,** from a record-by-record harvest. Normalise the biology contrast for adoption, and use permutation inference. (M4)
7. **Run a policy event study.**
   - Dates: 31 October 2025, 10 December 2025, 21 January 2026, 11 February 2026, 1 July 2026 and 1 October 2026.
   - The share of first-time submitters by archive (names never seen since 2010).
   - The q-bio decline.
   - Movement of computer-science content into non-CS primary categories.
   - A follow-up on Q4 2026. (M8)
8. **Validate the medRxiv flags.**
   - Validate both flags; give the title-only bound; test an extended dataset list.
   - Run an OpenAlex version of C3, and a contrast of systematic reviews against primary studies. (M5)
9. **Compare servers with similar cultures.**
   - ChemRxiv, mostly experimental chemistry, against arXiv physics.chem-ph.
   - q-bio against bioRxiv bioinformatics.
   - EarthArXiv against physics.ao-ph and physics.geo-ph.

   These separate effects specific to arXiv from effects common to a field. (Section 7)
10. **Run the marker analysis** by category and archive, with two estimators. (M7)
11. **Track thinness and later outcomes,** by archive and for heavy producers:
    - pages and figures (from the comments field), references and the single-author share;
    - journal publication within twelve months (OpenAlex).

    This tests arXiv's own account of "salami" and thin papers. (M6)
12. **Run an out-of-sample test.**
    - Register now, for example on OSF, the bioRxiv and medRxiv contrasts and the arXiv genre decomposition.
    - Test them on data from October 2026 to March 2027.
    - The arXiv cap affects the arXiv series, so treat those with care.

---

## 6. Strengths to keep

- **The design.**
  - Three servers, within-field contrasts, and a confirmatory family fixed before the models were run.
  - Negative controls; placebos across all pairs of archives and across random splits of categories; leave-one-out estimates; minimum detectable effects; Holm adjustment.
  - These are what make the negative results credible, so keep them central.
- **Honest corrections already in the draft:**
  - the medRxiv denominators that included COVID-19 preprints;
  - the reversal of the biology contrast under a 2019 base;
  - mentions of AI treated as lower bounds.
- **Validation steps:**
  - bioRxiv category sums equal the official totals from July 2019;
  - annual OAI counts for hep-th and hep-ph match arXiv's statistics exactly for 2019–2025;
  - the bioRxiv index reproduces from bioRxiv's own statistics;
  - per-archive and OAI growth in mathematics agree.
- **Replication of Nee et al.'s synthetic control** (11.9%) on primary-only counts, and the comparison across archives that puts it in context.
- **The heavy-producer analysis:** namesake variants, the breakdown by team size, and an explicit warning that histories are left-censored.
- **The code and record:** readable, modular scripts that output aggregates only, and the process record.

---

## 7. Addendum after the formal results: what could produce an arXiv-wide acceleration that includes experimental archives, and how to position the paper

*Added at the coordinator's request after the Priority 1 results (`stats/results.md`, `field_tests.json`) arrived.*

### 7.1 The pattern to explain

- **Departures from trend in 2026.**
  - Every arXiv archive except nucl-ex is above its 2015–2022 trend in January–September 2026. The departures run from 1.03 (q-fin) and 1.06 (physics.\*) to 1.81 (math-ph); nucl-ex stands at 1.00.
  - Experimental and observational archives are among them: hep-ex 1.37, astro-ph 1.34 and cond-mat 1.30.
  - q-bio fell from 1.43 in 2025 to 1.26 in 2026.
- **Breaks.** The tests with no pre-specified date put a break in the slope of physics in November 2024 (p = 0.001), and in mathematics in November 2024 too, though more weakly (p = 0.095).
- **Mathematics.**
  - Its synthetic-control gap (11.9%) falls almost entirely in May–September 2026.
  - Among the 18 archives, its departure from trend ranks fifth (rank p = 0.28).
  - Measured by raw gap in the synthetic-control placebos, cs (22.1%), stat (18.7%) and econ (16.7%) exceed it. Only its ratio of post- to pre-period fit error ranks first.
- **The other servers.**
  - bioRxiv stands at 0.91 [0.71, 1.15] and PubMed at 0.93 [0.86, 1.01].
  - medRxiv without COVID-19 grew 27%, 21% and 22% in 2024–2026, with no acceleration.
  - September 2026 spiked on arXiv only (M2).

### 7.2 Candidate explanations and how to tell them apart

| # | Explanation | What it predicts | Check (Section 5) | Assessment |
|---|---|---|---|---|
| 1 | **Announcement throughput.** Moderation holds and the clearing of backlogs; independence and the cloud migration (1 July 2026). | Spikes in counts dated by announcement that are absent when papers are dated by submission; changes in the delay between the two. | 1 | Plausible for September 2026 and the July–September jump. Cannot by itself produce a slope break in late 2024. |
| 2 | **Platform rules.** <ul><li>Endorsement (December 2025 and January 2026) and the English rule (February 2026) restrict entry.</li><li>The gate on review and position papers in CS (October 2025) may push AI- and ML-related papers into stat, math, quant-ph or physics.soc-ph.</li><li>Rate limits at moderators' discretion.</li></ul> | <ul><li>Steps at the policy dates.</li><li>Growth in non-CS archives concentrated, from November 2025, in papers with cs.\* cross-lists or ML vocabulary.</li><li>Fewer first-time submitters.</li></ul> | 7, 2 | Can shape 2026, and plausibly explains q-bio's fall. Cannot explain a slope break in late 2024 that predates every rule; the rules on entry work against acceleration. |
| 3 | **Which genres a server accepts.** <ul><li>arXiv accepts proceedings, reviews (except in CS since October 2025), lecture notes, comments and white papers.</li><li>bioRxiv is "not intended for" narrative reviews, editorials, opinion pieces or white papers (bioRxiv FAQ, as verified in the citation audit).</li><li>AI makes exactly these derivative genres cheapest.</li></ul> | <ul><li>Acceleration concentrated in derivative genres.</li><li>Present in experimental archives, where collaboration proceedings and reviews are common.</li><li>Absent on bioRxiv.</li></ul> | 2 | Plausible and cheap to test. **The single most informative check.** |
| 4 | **Propensity to post, and migration of content.** <ul><li>AI lowers the cost of posting: LaTeX conversion, and translation (arXiv's English rule accepts automated translations faithful to the original).</li><li>Already-published work posted after the fact.</li><li>Moves from other servers, or from journal-only publication.</li><li>ML papers about science choosing a domain primary category.</li></ul> | <ul><li>Rising coverage ratios without matching growth in journal output.</li><li>More v1s already published.</li><li>Growth concentrated among authors and countries that used arXiv little before.</li></ul> | 4, 3 | Plausible. If confirmed, the arXiv acceleration says little about production. |
| 5 | **Who posts.** <ul><li>AI lowers language barriers. Kusumegi et al. report the largest adopter gains for Asian-named authors at Asian institutions: 43.0% on arXiv, 89.3% on bioRxiv.</li><li>arXiv and bioRxiv draw on different populations of authors.</li></ul> | Growth concentrated by country and language, on each server in proportion to those groups' presence there. | 3 | Plausible; testable with OpenAlex. |
| 6 | **Cycles within fields.** <ul><li>Collaboration run cycles: the LHC's Long Shutdown 3 was scheduled to begin at the start of July 2026 (https://home.cern/updated-schedule-cerns-accelerators).</li><li>Conference seasons.</li><li>Releases of survey data.</li></ul> | hep-ex growth concentrated in collaboration papers and timed to those cycles. | 5 (team size) | Plausible for hep-ex; not arXiv-wide. |
| 7 | **AI-enabled production across arXiv fields.** <ul><li>Cheaper writing, coding and analysis, including in experimental work heavy on data analysis: astro-ph surveys, small-team hep-ex analyses, cond-mat simulations.</li><li>A layer specific to mathematics: the wave of Erdős problems and Lean proofs in May–September 2026.</li></ul> | <ul><li>Growth in research articles, not only in derivative genres.</li><li>Growth among established authors.</li><li>Growth correlated with the rise in AI-writing markers across archives.</li><li>bioRxiv's null due to the bottleneck, or to a different population.</li></ul> | 10, 3, 5, 11 | The substantive hypothesis; what remains if explanations 1–6 are ruled out. |
| 8 | **Model artefacts.** <ul><li>Linear trends before 2023 are extrapolated forward.</li><li>Archives whose trend was declining show the largest departures: math-ph (−4.3% a year → 1.81), nucl-th (−2.5% → 1.58) and nlin (−1.1% → 1.52).</li><li>The donors in the synthetic control accelerated too.</li></ul> | Rankings change under other counterfactuals: a 2015–2019 trend, a flat 2019 or 2022 level, or raw year-on-year growth. | Re-estimate | The synthetic control identifies mathematics' excess over an accelerating arXiv, not the effect of AI. |

**Two points cut across the table.**
- **Policy dates come too late.** None of the arXiv policy dates precedes the late-2024 break in physics. The rules on entry (endorsement and English) would dampen growth, not cause it. Policy changes can therefore explain the shape of 2026, but not the acceleration as a whole.
- **The nulls are informative but confounded.** The archives that did not accelerate are nucl-ex (the most purely experimental) and physics.\* (largely applied and experimental physics). That is a modest hint towards a bottleneck, but these archives also differ in genre mix and community. Report it as description, not as support for H1.

### 7.3 Positioning against Nee et al. and Qi et al.

**What is new and defensible.**
1. Within-field falsification tests, fixed in advance, on three servers, with inference from placebos. They come out negative.
2. The 2024–2026 acceleration:
   - is arXiv-wide;
   - began in physics before 2026;
   - includes experimental archives;
   - is absent from bioRxiv, medRxiv and PubMed.
3. The mathematics anomaly replicates, but it is an excess in mid-2026 on top of an arXiv-wide shift.
4. A contribution to measurement. Preprint counts are not comparable indicators of production across servers, because the servers differ in:
   - how papers are dated;
   - which genres they accept;
   - how they screen submissions;
   - how far each field has adopted them.

**Nee et al.**
- **Replication.** Present the 11.9% as an independent replication on a different unit: primary-only counts, against their list entries that include cross-lists.
- **What the synthetic control identifies.** Its donors are other arXiv archives, and these accelerated too. It therefore estimates mathematics' excess over arXiv, not the effect of AI.
- **Their framing.** The ranking against trend (rank p = 0.28) and the departures for hep-ex and astro-ph qualify their emphasis on "theoretical and computational research". Their text reports nucl-ex (+2.6%) but not hep-ex.
- **The author panel.** Compare it only after harmonising definitions (M3). Their panel shows rising concentration and newcomers among high-output units, which bears directly on H2.

**Qi et al.**
- Their design compares servers, so it cannot separate computational intensity from server.
- The within-field nulls suggest that the field differences they report are better described as differences between servers and their author populations.
- Position the paper as the within-field test their design lacks, and drop the echo of their title.

**Kusumegi et al. and Renault et al.**
- Reconcile the gains measured for individual adopters on bioRxiv with the flat aggregate.
- Three explanations to weigh: the adopter-level estimate is inflated (Renault et al.); adoption is concentrated among few authors; or the extra output goes to other venues.

**What the evaluation argument can keep.**
- The thesis of the title, that AI "is eroding publication counts as a measure of scientific work", is not tested by these data. Nor is "needs no misuse".
- A weaker point does follow without H1. arXiv counts rose 30–50% above trend within two years, while bioRxiv and PubMed did not. Counts are therefore not comparable across fields, servers or years, whatever the cause. That is a measurement point evaluators can use.

**Suggested titles.**
- "Where has preprint output accelerated since generative AI? Pre-specified within-field tests across arXiv, bioRxiv and medRxiv"
- "An arXiv-wide acceleration, not an experimental bottleneck: preprint output across servers, 2016–2026"
