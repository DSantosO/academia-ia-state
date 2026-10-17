# Review of "Preprint output in the generative-AI era: pre-specified within-field tests find no robust evidence of an experimental bottleneck" (PLOS ONE, draft v2)

**Reviewer 2: scientometrics and preprint data. Round 2, 16–17 October 2026.**

**Materials examined.**
- The revised manuscript, `paper/plos_one/draft_v2.md`.
- The response to round 1, `paper/plos_one/reviews/round1/response_round1.md`.
- The results folder `paper/plos_one/stats/`: `results.md`, `methods.md`, `deposit_README.md` and the JSON files.
- Both pre-registrations: `preregistration_new_data_test.md` and `preregistration_amendment1.md`.
- The companion branch `claude/happy-lovelace-wqek9b` at commit 15df0b1. That is two commits after 0e239cd, the version v2 cites:
  - 11bc67d adds the medRxiv flag coding sheet and an adapter that reads first-version dates from arXivRaw records;
  - 15df0b1 adds the script for the confirmatory ND/NN test and the medRxiv samples (identifiers only).

  I did not examine later commits.
- Record-level files I read:
  - `data/processed/arxiv_paper_flags.csv.gz` and `data/raw/medrxiv_records.csv.gz`;
  - `data/raw/inspire_hep_records.csv.gz`, `pubmed_us_quarterly.json`, `medrxiv_covid_monthly.csv` and `arxiv_archive_monthly.csv`;
  - `heavy_producers.json`, `round1_tests.json` and `core_marker_words.txt`.
- The scripts that produce them. Among these:
  - `stats_round1.py`, `harvest_inspire.py`, `harvest_arxiv_raw.py`, `v1_dates_from_raw.py` and `fetch_arxiv_v1_dates.py`;
  - `harvest_rxiv_records.py`, `rebuild_rxiv_from_records.py`, `harvest_rxiv_categories.py` and `fetch_pubmed_us.py`;
  - `stats_heavy_producers.py`, `osf_continuity.py`, `sample_flags.py`, `make_validation_sheet.py` and `run_all.sh`.

**Conventions.**
- **"My calculation"** marks a number I computed from the companion's committed files. Anyone can reproduce it from those files.
- **Online checks** were made on 16–17 October 2026 and carry their URL. I also collected some data myself:
  - from the bioRxiv and medRxiv API: about 1,300 requests for identifier fields only (DOI, version, date, category, type), with a 1-second pause after each response, over one connection; two single test requests overlapped it (Section 4.2);
  - 16 count-only queries to PubMed E-utilities, one per second;
  - reference metadata from Crossref (16 lookups, one per second) and the arXiv API (two requests).
- **Re-run.** I re-ran the companion's statistics scripts on a copy of the committed data (Section 4.4).
- **Blinding.** I did not open or inspect:
  - any output of the pre-registered paper-level tests;
  - the blind validation sheet;
  - the sealed key or the model labels.

  This review reports no confirmatory estimate of those tests.
- **No edits.** I have not edited the manuscript or the companion.
- **Corrections to my own round-1 review.** Twice below I correct advice I gave in round 1:
  - OAI `created` as the first-version date (M2);
  - my description of Qi et al. (Section 4.3).

---

## 1. Summary of the changes

v2 is a different paper from v1, and a better one. It now reports a falsification test that failed, says so in the title, and keeps the exploratory material apart.

**Framing.**
- **The tests.** H1–H3 are reproduced as recorded before modelling (commit 2cac071). The three pre-specified within-field contrasts are reported as not supporting H1:
  - physics is inconclusive: 1.14 (1.00–1.30), Holm-adjusted p = 0.11;
  - biology is fragile: 1.08 (1.03–1.14), p = 0.01;
  - medicine is null: 1.01 (0.90–1.14).
- **Defined terms.** "Pre-specified" is defined honestly: fixed before any model was estimated, not before the data were seen.
- **New title.** The title no longer asserts a causal claim.
- **Withdrawn findings.** "Eroding", "1.9 million" and "needs no misuse" are gone.

**Inference.**
- **Placebos.** In-space placebos are now the primary inference: placebo p = 0.61 for physics and 0.20 for biology.
- **Reported beside every contrast:**
  - Bonferroni intervals;
  - minimum detectable effects at α and α/3;
  - a year-shock calibration;
  - pooled and alternative base years;
  - acceleration estimates (2026/2025 and slope changes);
  - leave-one-out estimates and negative controls.
- **Deviations.** A Deviations section lists every change from v1's plan.

**New checks.**
- Snowmass 2021 and European Strategy papers removed from the physics base.
- A keyword split by genre in mathematics and six HEP and nuclear archives.
- List entries (cross-lists included), the unit Nee et al. count.
- Break tests that can place a break as late as January 2026.
- The synthetic control, shown in context.
- A PubMed comparison of articles with and without a US affiliation.
- An exploratory classification of 117,950 INSPIRE-HEP records by a registered rule.
- A late correction of medRxiv duplicates.

**H2.**
- H2 rests on concentration shares and on a decomposition of growth by author class, with classes ranked on combined output in both years.
- It now covers mathematics as well as theoretical physics.
- Variants:
  - namesake-robust names;
  - July–August only;
  - names already active in 2019–2024;
  - January–August windows.
- "Established" is dropped as a claim.

**H3.**
- H3 now rests on the companion's measure: Kobak et al.'s style words, filtered on baseline data, with 2024 as the comparison year.
- The drift of the words after 2024 is stated.
- Mathematics and a category panel are added.
- Published estimates from other studies move to S4 Table.

**Exploratory material.**
- The divergence between servers is reported against each series' own trend, with the counterfactual named.
- Candidate explanations are listed, and two of them were checked.

**Pre-registration.** A pre-registered paper-level test was activated, with two recorded deviations. No results are reported yet.

**Compliance.**
- **Statements.** v2 adds an ethics statement for author names, terms of use and request rates for each source (with two past exceedances disclosed), a Data availability statement, an AI-use statement and a dated timeline of policies (S2 Appendix).
- **Markers.** The file still carries 53 [AUTHOR], 18 [ANALYSIS PENDING] and 9 [RECHECK] markers (header of `draft_v2.md`).

**Companion analysis since 0e239cd.** It adds:
- the medRxiv flag coding sheet, 200 rows, not yet coded;
- an arXivRaw adapter for v1 dates. The arXiv API returned "429 Rate exceeded" to the companion (docstrings of `harvest_arxiv_raw.py` and `v1_dates_from_raw.py`);
- the script and medRxiv samples for the confirmatory ND/NN test.

## 2. Recommendation

**Major revision before submission.**

**The framing is now right.**
- Conclusions follow from the pre-specified tests.
- Exploratory material is labelled as such.
- The limitations are stated plainly.

On criterion 4 I would now support the paper.

**Why it is still "major".**
- **Measures not yet valid.** Three claims rest on checks whose measures are not valid as used:
  - the abstract's "not because of reviews, proceedings or white papers" (N1);
  - "similar" adoption of AI-assisted writing within fields (N2);
  - the accounting of the funding shock from PubMed affiliations (N4).
- **An unconfirmed comparator.** The bioRxiv series, the paper's main comparator, has not been checked for the duplication found in medRxiv. My spot check finds none in the months where medRxiv's was worst, but the full check is still to be run (N5).
- **Positioning.** The positioning against Qi et al. misreads their finding (N9). I share the blame: I described Qi et al. wrongly in round 1.
- **The deposit.** The deposit and the disclosures are honest in spirit but wrong in several particulars (N10).

**All of this can be fixed with data in hand.**
- Each problem can be fixed with data already harvested, or by narrowing a sentence.
- The one exception is the bioRxiv record harvest, and its scripts exist.
- One open question can already be closed: dating by submission rather than announcement makes no material difference (N6).

**Before submission.**
- **Resolve every marker.** Do not submit with [ANALYSIS PENDING] or [RECHECK] markers.
- **The pre-registered test.** The paper does not need the test to be publishable. It must either report the test, or describe it in one sentence as registered and pending, with its registration DOI.

---

## 3. Round-1 issues: status table

Status codes: **Resolved**; **Partly**; **Not** resolved; **Open (author)**, needing the author's decision.

### Major issues

| Round-1 issue | Status | Evidence | What remains |
|---|---|---|---|
| **M1. Reframe; H1 not supported** | Resolved | Title, Abstract, Results, Conclusions; placebo p beside Holm p; bases 2019, pooled and cleaned; Fig 2D; the two findings withdrawn; the nucl-ex and `physics` "hint" reported as description | The Abstract's "not because of reviews, proceedings or white papers" (N1) |
| **M2a. Date by v1 submission** | Partly in v2; answerable now | Marked [ANALYSIS PENDING]. The companion found that OAI `created` is the latest version's date. **I recommended `created` in round 1; that advice was wrong.** The arXiv API returned 429; an arXivRaw adapter was added | My calculations from committed files settle the question for mathematics and HEP (N6). Report them and remove the marker |
| **M2b. Headline windows** | Partly | January–September comparisons lead; H2 gives July–August and January–August variants | The Abstract's "more than tripled" (+266%) is the Q3 figure, which includes the September spike; January–August gives +78% (Section 5, item 3) |
| **M2c. Reconcile the arXiv sources; the January 2025 boundary** | Resolved for HEP; partly for mathematics | The harvest now starts in 2019. My calculation: the flag table matches arXiv's statistics pages exactly for hep-ex and hep-th (January–September 2019, 2022, 2026) | Mathematics: the OAI primary-math series is 89.9–92.3% of the statistics-page "math" counts (N8) |
| **M2d. Ask arXiv for moderation statistics** | Open (author) | Optional | – |
| **M3a. One record, one primary category; N** | Resolved in the text | N removed; aliasing stated (archive sums about 5% above arXiv's total) | The two definitions of mathematics, unlabelled (N8) |
| **M3b. Report both count definitions** | Resolved | New submissions and list entries; mathematics ranks fifth on new submissions and second on entries | – |
| **M3c. Replicate Nee et al. before comparing** | Partly | The synthetic control is replicated (11.9%; about 8% without September). The author panel is compared on January–August windows with primary-only papers: 2.34% → 3.73% against Nee's 2.45% → 3.80% | The like-for-like variant is already computed: list entries, January–August, all names, 2.80% → 4.07% (`heavy_producers.json`, `maths_list_entries`). It is not reported. The text cites the variant that happens to be numerically closest (N9) |
| **M3d. Name the unit when citing Nee et al.** | Resolved | "list entries" in the Introduction | – |
| **M4. bioRxiv confounds** (adoption, COVID-19, author-chosen categories, screening) | Not resolved; acknowledged | Pending: COVID-19 removal record by record, content classification (Test A), the AI-topic split and structure-matched permutation. Declined: normalisation by journal output. Not examined: the Gates mandate, the 2020 screening of drug-repurposing papers, the platform change | Duplicate listings: my spot check finds none on bioRxiv; a full check is still needed (N5). The cautious reading of C2 ("fragile in level; acceleration confounded with the end of adoption") is appropriate |
| **M5a. Validate the medRxiv flags** | Not (pending) | A coding sheet of 200 rows (50 per rule) is committed, uncoded | Coding the flagged sample gives precision only; recall needs a sample of unflagged preprints (Section 6, item 10) |
| **M5b. Title-only bound; extended list** | Resolved | C3 1.07 (0.95–1.21) with title-only matching; 1.05 (0.93–1.17) with Spick et al.'s four datasets | When the list was fixed (marked [AUTHOR]) |
| **M5c. medRxiv as the venue; genre contrast; a journal version of C3** | Partly | "A weak test of H1 … in this venue"; the journal version declined; the genre contrast is part of Test A | Acceptable |
| **M5d. The medRxiv duplicate correction** (new in v2) | Resolved for duplicates under the same DOI | Every series counts each DOI once; my re-run reproduces the corrected C3 values in Table 1 | Duplicates cluster after the change of DOI prefix and peak in July–August 2026. Duplicates under different DOIs are unchecked. The committed `round1_tests.json` and `results.md` still hold pre-correction C3 values (N8, N10) |
| **M6. H2 artefacts** (namesakes, newcomers, batch posting, a few submitters) | Largely resolved | Histories from 2019; the combined-output decomposition for mathematics and theory; namesake-robust and established-name variants; collaboration papers (>50 authors) excluded; fixed-threshold measures moved to S3 Table | Declined: an identifier-matched subsample and a simulated namesake null. Batch posting was declined for lack of submission dates, which now exist (N6). The abstract's headline uses Q3 (Section 5, item 3) |
| **M7. H3 on the companion's own markers** | Resolved in structure; new metric issue | Rebuilt on Kobak et al.'s style words; 2024 leads; drift stated; mathematics and the panel added; Table 6 moved to S4 Table | Relative rises versus absolute excess (N2); Liang et al.'s bioRxiv values still [RECHECK], and the open preprint can be read (Section 4.3) |
| **M8a. Server-policy timeline** | Largely resolved | S2 Appendix, dated and sourced | Two [RECHECK] items can be closed now: arXiv's post and openRxiv (Section 5, item 9). Add the medRxiv DOI-prefix change (2 December 2025) and the onset of duplicates |
| **M8b. Rule-date indicators in the models** | Acceptable as declined | Nearly collinear with 2026; window-drop variants in S5 Table | – |
| **M8c. Validate the OSF method; demote the social-science series** | Not resolved | Continuity check pending; OSF access is blocked | Remove the series from Fig 1 and Table 3 (N7) |
| **M9a. Positioning against Nee et al.** | Resolved | Replication on a different unit; "an excess over an accelerating arXiv" | Report the list-entry author panel (M3c) |
| **M9b. Positioning against Qi et al.** | Not resolved, and my round-1 advice was wrong | v2 presents itself as the within-field test of Qi et al.'s "computationally intensive fields benefited more" | Qi et al.'s claim concerns the share of AI-related papers by discipline, not the volume of output (N9) |
| **M9c. Core scientometric literature** | Resolved | All the references I listed are added; I re-verified the new ones (Section 4.3) | A few useful additions (Section 4.3) |
| **M9d. Discussion material the data do not test** | Partly; author's decision | "Implications" shortened to about 520 words and labelled as interpretation; proposals cut to one paragraph | Acceptable if the [RECHECK] figures are verified |
| **M10a. Record-level identifiers and flags** | Partly; more exists than v2 says | v2 says the tables "will be added". Already committed: arXiv flags (453,067 rows), medRxiv records (89,700), INSPIRE records (117,960), medRxiv ND samples (4,080) | Missing: bioRxiv records, complete v1 dates, OAI datestamps. A heavy-producer flag must **not** be released (N10) |
| **M10b. Respect request limits; state compliance** | Partly | Commendably frank about arXiv's statistics pages (1 s pauses against a 15 s crawl delay) and about OSF | Three inaccuracies: "no request was refused" against the 429; an OSF file claimed but absent; parallel connections to the bioRxiv API not in Methods (N10) |
| **M10c. Pinned environment; a single rebuild command** | Not resolved | Pinned environment pending | `run_all.sh` does not run `stats_round1.py`, the source of many v2 numbers (N10) |
| **M10d. Names only with data-protection approval** | Open (author) | Ethics statement drafted | Say which framework governs: EMBL's Internal Policy 68, or the GDPR at UPF (N10) |
| **M10e. Licences** | Open (author) | CC BY 4.0 for data and MIT for code proposed | Consider CC0 for tables derived from CC0 sources. Titles and abstracts appear in the validation sheets (N10) |

### Minor issues

| # | Issue | Status |
|---|---|---|
| 1 | Title | Resolved |
| 2 | "Dated by announcement" | Resolved (Methods, ref. 33) |
| 3 | hep-lat as a third arm | Declined; acceptable if the reason is stated (marked [AUTHOR]) |
| 4 | v1 Table 2 growth columns | Resolved (replaced by departures from trend) |
| 5 | v1 Table 3 footnote | Superseded by the duplicate correction |
| 6 | Model-release markers | Resolved |
| 7 | Two name normalisations | Resolved: one pipeline |
| 8 | Precision of the mention patterns | Moot for AI, Lean and Erdős; pending for the medRxiv flags |
| 9 | `\b` before `covid` | Not done; negligible |
| 10 | Which arXiv count is which | Resolved |
| 11 | Retrieval dates | Resolved for the sources named; INSPIRE and arXivRaw dates still to add |
| 12 | Terminology ("heavy producer") | Resolved |
| 13 | References | Mostly resolved; ref. 68 lacks its DOI; Renault et al.'s article type is open |
| 14 | "Fixed before growth was examined" | Resolved (Study design) |
| 15 | Partial October 2026 | Declined because dating was pending. Dating is now settled for unrevised papers, and October is informative about H2 (N6) |
| 16 | medRxiv's early months | Resolved |

### Analyses requested in round 1, ranked as then

| # | Analysis | Status |
|---|---|---|
| 1 | Re-date by submission | Pending in v2; answerable now (N6) |
| 2 | Genre and topic breakdown | Partly: genres done for mathematics and six HEP archives, with validity problems (N1); AI topic pending |
| 3 | Who drives the growth | Largely done (decomposition, 2019 histories). Identifiers and country declined. A Nee-comparable list-entry panel exists but is unreported |
| 4 | Propensity to post | Declined; named as untested |
| 5 | Content classification; team size | Pre-registered test pending; team size done with INSPIRE |
| 6 | bioRxiv without COVID-19; permutation | Pending |
| 7 | Policy event study | Declined |
| 8 | medRxiv flags | Partly (bounds done; validation pending) |
| 9 | Servers with similar cultures | Declined |
| 10 | Marker extension | Done, with a metric issue (N2) |
| 11 | Thinness and later outcomes | Declined |
| 12 | Out-of-sample test | A different test is registered (paper level, held-out archives); no 2027 test |

---

## 4. New major issues

### 4.1 The new data checks: are the measures valid?

#### N1. The genre split is not valid as built, and the Abstract applies it beyond its coverage

**Location.**
- Abstract: "experimental particle physics included and not because of reviews, proceedings or white papers".
- Results, "Departures from trend": "The acceleration is not a matter of genre".
- Discussion, first explanation checked.
- Methods, Exploratory analyses.

**Coverage.**
- The split covers mathematics and six archives: hep-th, hep-ph, gr-qc, nucl-th, hep-ex and nucl-ex.
- **Share of physics.** In January–September 2026 these six produced 19.4% of new papers in the 13 arXiv physics archives, and 18.8% of the 2025→2026 increase.
- **The held-out archives.** cond-mat, astro-ph and quant-ph produced 57.8% of physics output and 62.1% of the increase (my calculation from `arxiv_archive_monthly.csv`).
- Holding these three out until the confirmatory test is finished is correct, but then the Abstract cannot speak of "arXiv physics" here.

**The labels depend on revision.**
- **Current metadata.** The rules search the comments field (and titles) of OAI metadata, which carry the latest version's comments.
- **Genre and revision are linked.** Genre labels are strongly associated with revision. In 2019–2022, proceedings were:
  - 11.2% of unrevised theory papers against 1.6% of revised ones;
  - 31.0% of unrevised experimental papers against 4.1% of revised ones.
- **The revised share is right-censored**, because recent papers have not yet been revised. Papers with a later version:

  | Group | 2019–2023 | 2026 |
  |---|---|---|
  | Mathematics | 46–48% | 18.5% |
  | Theory | 55–58% | 27.8% |
  | Experiment | 48–55% | 26.5% |

  (My calculation from `arxiv_paper_flags.csv.gz`; "revised" means the latest version was submitted after the month of the identifier.)
- **Consequence.** Any label added or removed at revision changes with a paper's age, and so with calendar time in the series. Examples: a journal reference, "accepted at", "invited review".

**The patterns match journal names** (`GENRES` in `stats_round1.py`).
- `proceedings|\bproc\.` matches "Proc. Amer. Math. Soc.", "Proceedings of the Royal Society A" and "Proc. Natl. Acad. Sci."
- `\breview\b` matches "Physical Review" and "Reviews of Modern Physics" in comments.
- `conference` matches research papers "accepted at" a conference.

**Validation against INSPIRE's curated document types.** My calculation covers the five archives present in both tables, January–September 2019–2026; 99.85% of papers are matched.

| Keyword class | INSPIRE reference | Precision | Recall |
|---|---|---|---|
| "proceedings" | conference papers | 89–97% | 63–87% |
| "review" | publication types review, lectures, introductory | 4–18% | 30–45% |

- **Proceedings.** Recall is lowest in 2022, when Snowmass contributions were labelled white papers; it is 90% if they are added.
- **Reviews.** The INSPIRE review type is itself assigned late: 1.2% of 2019 papers against 0.3% of 2026 papers.
- **Proceedings shares agree over time.** In these five archives, INSPIRE's conference-paper share falls from 12.3% in 2022 to 6.4% in 2026, and the keyword share from 8.5% to 5.9%. Both are near 7% in 2020–2021 and 2023–2025, so the fall is mostly relative to 2022, a year with many proceedings.
- **Other classes.** The white-paper class is, in effect, the Snowmass and European Strategy keyword. Nothing validates the mathematics classes.

**Two different "six archives".** The genre split and C1 use gr-qc. The INSPIRE classification uses hep-lat instead (`HEP6` in `stats_round1.py` against `ARCH` in `harvest_inspire.py`). Methods calls the INSPIRE set "those six archives".

**What follows.**
- **Supported.** In particle and nuclear physics, "proceedings fell as a share, and research articles alone departed from trend as much as all papers" is supported, and INSPIRE corroborates it.
- **Not established:** that reviews are not involved; any genre result for mathematics; anything about the rest of physics.

**Fix.**
1. **The Abstract.** Write: "… in mathematics and particle and nuclear physics, papers not declared as proceedings or white papers departed from trend as much as all papers." Drop "reviews" unless that class is validated.
2. **Report the INSPIRE validation** above for HEP.
3. **Fix the patterns.**
   - Exclude journal names: "Physical Review", "Phys. Rev.", "Rev. Mod. Phys.", "Proc. Amer. Math. Soc.", "Proceedings of the … Society/Academy" and "Proc. Natl. Acad. Sci."
   - Restrict "review" to titles and to explicit phrases ("review article", "invited review").
4. **Hand-code mathematics.** Code 200 mathematics papers stratified by year and by revision status, and report precision and recall per class.
5. **Show the revision effect.** As a sensitivity analysis, classify within each year only from fields that do not change at revision (titles), or report shares separately for revised and unrevised papers.
6. **Name the sets.** Use "C1's six archives" and "INSPIRE's six archives" consistently.

#### N2. H3's comparisons within fields depend on an unjustified choice of metric; under Kobak et al.'s own metric, the conclusion changes

**Location.**
- Results, H3: "Within fields the rise did not differ detectably in 2024"; "Computational categories started higher (38.6 against 27.7), as in Kobak et al. [15], but rose by a similar factor".
- Table 2.
- Abstract.
- Discussion, "Implications": "at least 4% of mathematics, 6% of experimental and 11% of theoretical physics abstracts".

**Problem.**
- **Which metric.** The tests between groups compare *relative* rises (rate divided by the 2019–2022 baseline). Kobak et al.'s method, and the lower bound the paper itself uses for arXiv, rest on the *absolute* excess: observed frequency minus counterfactual frequency.
- **Why it matters.** Suppose LLM processing adds about the same number of marker words to a share *f* of abstracts. The relative rise is then 1 + *f*·*k*/baseline, so a group with a higher baseline shows a smaller relative rise for the same *f*.
- **The baselines differ.** By 39% within biology (38.6 against 27.7) and by 28% within physics (15.0 against 11.7).

**Absolute excess in 2024**, core words per 100 abstracts above the 2019–2022 mean (my arithmetic from Table 2):

| Group | Excess | Comparison |
|---|---|---|
| bioRxiv computational | +60.3 | 1.9 times wet lab |
| bioRxiv wet lab | +31.8 | |
| bioRxiv mixed | +30.0 | |
| medRxiv | +46.0 | |
| arXiv physics theory | +17.6 | 1.33 times experiment |
| arXiv physics experiment | +13.2 | |
| arXiv mathematics | +9.9 | |

- **The paper's own lower bounds agree with the absolute metric:** at least 10.8% of theory abstracts against at least 6.1% of experimental abstracts in 2024 (Table 2).
- **Results and Discussion disagree.** Results report the relative metric ("did not differ"); "Implications" reports the lower bounds (6% against 11%).
- **"As in Kobak et al." attaches to the wrong quantity.** Kobak et al. found more LLM use in computational fields, about 20% against at least 13.5% overall. That finding concerns the excess, not the baseline, and the companion's data reproduce it under the absolute metric.

**What still holds, under every metric.**
- Markers rose in every group, experimental ones included.
- Mathematics had the smallest rise and the largest acceleration: +9.9 absolute; lower bound 4.4%.
- The category panel uses the absolute change (Δmarker) and finds no association with output growth.

So the claim at the level of servers and the mathematics result survive. The claim within fields ("similar" adoption, H3's "differences in output are not explained by differences in adoption") does not survive the change of metric.

**Asymmetries in measurement to state.**
1. **Text versions differ by server.**
   - arXiv text is the latest version's title and abstract; bioRxiv and medRxiv text is version 1.
   - Share of 2019–2022 arXiv papers whose latest version dates from 2023 or later (my calculation):

     | Group | Latest version 2023 or later | 2024 or later |
     |---|---|---|
     | Theory | 9.3% | 2.1% |
     | Experiment | 10.3% | 1.8% |
     | Mathematics | 14.7% | 6.6% |

   - Some baseline abstracts may therefore postdate ChatGPT. This biases the arXiv rises downwards, mathematics' most. The effect is small, and too small to explain mathematics' low rise.
2. **The core list was filtered on biomedical baseline frequencies** and then applied to arXiv, where baseline rates are about half as high.
3. **Drift differs by corpus.**
   - From 2025 to 2026, bioRxiv wet lab fell from ×2.30 to ×1.57, while arXiv experiment fell only from ×2.95 to ×2.57.
   - The paper states this; it rules out comparisons after 2024.
4. **Drift examples.** S2 Appendix and `methods.md` illustrate drift with "crucial" and "insights", which are not core words (`core_marker_words.txt`). "delve", "intricate" and "underscores" are core words.

**Fix.**
1. **Report both metrics.** For every group, report the absolute excess and Kobak-style lower bounds, bioRxiv and medRxiv included. Their text features would need re-aggregating by abstract: the medRxiv record harvest exists, and so does the March/September bioRxiv harvest.
2. **State H3's within-field result under both metrics.** Either justify one as primary or treat both as co-primary.
3. **Add a baseline sensitivity for arXiv:** papers whose latest version predates 2023.
4. **Correct two sentences:** the "as in Kobak et al." sentence, and the drift examples.

#### N3. The INSPIRE classes rest on curation that changes with the age of a record

**What is valid.**
- **Dating.** Records are dated by `preprint_date`, a submission date: 4.7% fall on Saturdays and 6.2% on Sundays, days on which arXiv does not announce.
- **Coverage** is 99.1–100% of arXiv's counts for INSPIRE's six archives in January–September of 2019, 2022 and 2024–2026 (my calculation).
- The rule was fixed in the pre-registration, and its variants are reported.
- The NN/ND intervals come from independent fits, which is conservative.

**Problems.**
1. **The experimental category is not independent curation.**
   - 98.4–99.8% of records with a primary category of hep-ex or nucl-ex carry Experiment-HEP or Experiment-Nucl (my calculation).
   - This is consistent with INSPIRE assigning categories from arXiv categories, cross-lists included.
   - In practice, "ND" means a research article in or cross-listed to an experimental archive, linked to an experiment or a collaboration, and without wording about prospects.
2. **Curation changes with record age.** For records with a primary category of hep-ex or nucl-ex (my calculation):

   | Share of records | 2017–2024 | 2025 | 2026 |
   |---|---|---|---|
   | Linked to an accelerator experiment | 0.55–0.69 | 0.48 | 0.47 |
   | With a collaboration field | 0.56–0.67 | 0.51 | 0.49 |
   | Typed as conference paper | 0.18–0.34 | 0.16 | 0.16 |

   - Part of this is real, since small-team papers grew. Part may be curation that has not happened yet.
   - ND requires a link, so a curation lag would undercount ND in 2025–2026 and bias NN/ND upwards.
   - The conclusion that ND papers grew as fast as the rest is therefore, if anything, conservative. But the class is a proxy for "collaboration measurement papers", not "new data", as the Discussion says of collaboration analyses of old data.
3. **No person has checked the classes** (S1 Appendix).

**Fix.**
1. **Report link and type shares by year**, as above.
2. **Add a sensitivity analysis on collaborations.** Restrict ND to records with a collaboration taken from the author list, which is less exposed to lag. The `no_link` variant already gives NN/ND 0.75 (0.51–1.09) within experiment.
3. **Measure the lag.** Re-harvest in three months.
4. **Spot-check 100 records**, stratified by class and year.

#### N4. The PubMed US-affiliation check does not measure what the text says

**Location.**
- Results, last paragraph of "Departures from trend".
- Discussion, explanation (ii).
- S2 Appendix.

**Problem.**
1. **The query misses about a quarter of US articles, and the miss rate drifts.** The companion counts US articles with `usa[ad] OR "united states"[ad]`. I tested how often articles from large US institutions match neither term (my PubMed E-utilities counts of 17 October 2026, `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count`, each term restricted to `"YYYY/01/01"[edat] : "YYYY/09/30"[edat]` and `"journal article"[pt]`):

   | Institution term | 2019 | 2022 | 2024 | 2026 |
   |---|---|---|---|---|
   | `"harvard medical school"[ad]` | 38.8% | 26.7% | 26.0% | 24.4% |
   | `"johns hopkins"[ad]` | 37.2% | 25.9% | 25.5% | 24.4% |

   Because the miss rate falls, the measured US count rises over time by construction.
2. **"Non-US" is not non-US.** It is total minus US, so it includes records without any affiliation.
3. **The pre-period contradicts the text.** The text says "after no comparable decline in 2019–2022". In fact the US share of January–September journal articles fell by more in 2022 than in either recent year:

   | Year | 2021 | 2022 | 2024 | 2025 | 2026 |
   |---|---|---|---|---|---|
   | US share | 20.86% | 19.65% | 19.58% | 18.78% | 18.28% |
   | Change (points) | | −1.21 | | −0.79 | −0.50 |

   (My calculation from `pubmed_us_quarterly.json`.) The pre-period coefficients show the same thing: 1.060 in 2021, 0.990 in 2022.
4. **The accounting assumes a trend it has not shown.** "About 1.7 of the roughly 7 percentage points" assumes that the non-US series is on trend. The US share also falls secularly, as output grows elsewhere.

**Fix.**
- **Delete** "no comparable decline" and the accounting sentence.
- **If the check is kept:**
  - assign countries by a validated method (OpenAlex institution country codes from ROR, or a parser for US states, ZIP codes and institutions, checked on a sample);
  - report the miss rate;
  - compare the US with other large producers.
- **The bioRxiv test.** The bioRxiv US/non-US test (pending) is better placed: it uses the corresponding author's institution, and its classifier needs a human check, not one by an AI agent.

#### N5a. Removing Snowmass and European Strategy papers is valid, but one reading is an artefact of the trend

**The identification is adequate** (my calculation):
- 117 of 713 hep-ex papers in January–September 2022 (16.4%), 78 of them in March 2022, the deadline;
- all 141 hep-ex papers flagged for Snowmass are white papers under the genre rule;
- 44 of 817 hep-ex papers in January–September 2025 are European Strategy inputs.

**Two caveats.**
1. **The cleaning is asymmetric within the trend window.**
   - Flags exist only from 2019, when the harvest starts. The 2015–2018 trend years keep their planning papers, for example the inputs to the European Strategy due in December 2018, while 2019–2022 lose theirs.
   - The C1 contrast cleaned against 2017–2019 (1.11) is unaffected in practice, but this should be said.
2. **hep-ex's departure rises from 1.37 to 1.58 mostly through trend leverage.**
   - Removing 16% of the last year of an eight-year log-linear fit tilts the slope.
   - For annual points, the change in the 2026 prediction is about δ·[1/8 + (3.5 × 7.5)/42] = 0.75δ, with δ = ln(1 − 0.164) ≈ −0.18. That lowers the counterfactual by about 13% and multiplies the departure by about 1.14: 1.37 × 1.14 ≈ 1.57.
   - The Discussion's "removing the papers of planning exercises … made hep-ex's acceleration larger" therefore describes the fragility of an extrapolated linear trend more than it describes hep-ex.

**Fix.**
- Report cleaned results against bases that avoid 2022, as Table 1 does for C1.
- Show hep-ex's departure under other trend windows: 2015–2021 and 2017–2022.
- Reword the Discussion's sentence.

#### N5b. The list-entry checks are valid; two notes

- **The unit is right.** List entries are the correct unit for comparison with Nee et al., and the departures and ranks are reported.
- **Note 1: the author panel.** The list-entry version of H2 exists but is not reported (M3c).
- **Note 2: cross-lists dominate the experimental archives.** In 2026, 67% of hep-ex entries and 69% of nucl-ex entries were cross-lists (`round1_tests.json`, `crosslists`). A list-entry version of anything involving the experimental group mostly measures papers from other archives.

### 4.2 Data integrity risks still open

#### N5. bioRxiv duplicates: my spot check finds none, but the official totals cannot rule them out, and the full check is still needed

**Why it matters.**
- **Duplicates in medRxiv.** The medRxiv API lists some version-1 preprints on two days, and medRxiv's official monthly totals include the duplicates (`rebuild_rxiv_from_records.py`).
- **The bioRxiv counts would include them too.** The bioRxiv category counts are the API's `count_new_papers` (`harvest_rxiv_categories.py --counts`), a count on the server side that would include duplicates of the same kind.
- **Agreement with official totals proves nothing here.** "Category sums equal bioRxiv's official totals" holds whether or not duplicates are present, because both come from the same API. (I listed it as a strength in round 1; it validates coverage, not uniqueness.)

**The medRxiv pattern** (my calculation from `medrxiv_covid_monthly.csv` and `medrxiv_records.csv.gz`).
- **Before the platform change.** Duplicate listings were 0–0.4% of listings until October 2025.
- **The DOI prefix changed:** the last 10.1101 DOI is dated 1 December 2025 and the first 10.64898 DOI 2 December 2025.
- **After the change.** Duplicates then rose:

  | Month | Nov 2025 | Jan 2026 | Jun 2026 | Jul 2026 | Aug 2026 | Sep 2026 |
  |---|---|---|---|---|---|---|
  | Duplicate share of listings | 0.6% | 1.0% | 2.1% | 9.9% | 17.9% | 4.0% |

- **Screening lag.** The lag from the date in the DOI suffix to posting also lengthened, from a median of 1–2 days (90th percentile 2–5) to 2–3 days (90th percentile 5–8).
- **For context.** openRxiv, the new home of both servers, was announced on 11 March 2025 (https://www.nature.com/articles/d41586-025-00762-4; press release at https://www.infodocket.com/2025/03/11/openrxiv-launch-to-sustain-and-expand-preprint-sharing-in-life-and-health-sciences-usa/).

**My spot check of bioRxiv.**
- **Method.** I listed every bioRxiv record (all versions) that the API returns for three windows. I then counted DOIs that appear as version 1 more than once. Fields read: DOI, version, date, category, type. The API page is https://api.biorxiv.org/; the endpoint is `details/biorxiv/<start>/<end>/<cursor>`.
- **Results:**

  | Window | Version-1 listings | Unique DOIs | Duplicates |
  |---|---|---|---|
  | 1 June – 30 September 2026 | 18,498 | 18,498 | 0 |
  | 1 July – 11 August 2025 (harvest stopped on 12 August) | 5,429 | 5,429 | 0 |
  | 24 November – 7 December 2025, around the prefix change | 1,844 | 1,844 | 0 |

  - **The months that matter are clean.** The first window contains July and August 2026, when medRxiv's duplicates peaked, and has none.
  - **No re-listing under the new prefix.** In the window around the change, no DOI suffix appears under both prefixes.
  - **The prefix change.** bioRxiv's new prefix 10.64898 starts on 2 December 2025, the same day as medRxiv's. A few 10.1101 listings follow on 2–3 December.
  - **Agreement with the companion.** My monthly counts of version-1 listings equal the companion's category sums for July, August and September 2026 (4,676; 4,274; 5,049). June differs by three (4,499 against 4,496).
- **Control on medRxiv.** The same procedure on medRxiv for 1–15 August 2026 reproduces the companion's finding:
  - 705 version-1 listings for 596 unique DOIs, an excess of 15.5%;
  - 102 DOIs listed more than once, 94 of them on different dates.

  So the duplication was still visible in the API when I checked. Every medRxiv listing, including those of late November 2025, carries the `type` "PUBLISHAHEADOFPRINT", a value I did not see on bioRxiv. The field cannot be used to filter duplicates, so the companion's correction at DOI level is the right one.
- **Reading.**
  - The duplication appears specific to medRxiv. The bioRxiv series used in v2 is unlikely to be affected in mid-2026, and a correction would not change bioRxiv's 2026 numbers, Table 3 or C2 in those months.
  - **What my check cannot see.** It covers 26 weeks. It cannot detect a duplicate whose second listing falls outside a window, nor duplicates under different DOIs.

**Fix.**
1. **Complete the check over the whole series.** Run the existing record harvester (`harvest_rxiv_records.py biorxiv`, 2019–2026) and `rebuild_rxiv_from_records.py biorxiv`, which writes DOI-unique category counts. Then either replace the [RECHECK] with "no duplicates found", or re-estimate whatever moves (Fig 1, Fig 2B, C2 and its placebos, Table 3, the comparisons between servers).
2. **Check duplicates under different DOIs on both servers.** Match on normalised title plus first author within 90 days.
3. **Report the medRxiv anomaly descriptively.** Give the duplicate share by month and the uniform `type` value. Both are useful to anyone using the official totals.
4. **Add the events to the S2 Appendix timeline:**
   - the prefix change (2 December 2025, both servers);
   - the onset of medRxiv duplicates (2026).

#### N6. Dating by v1 submission for mathematics and HEP: the companion's own files already answer it

**The question.** v2 marks dating by submission [ANALYSIS PENDING] and lists announcement dating among the open explanations.

**Two committed sources already settle it for the archives that matter.**

**(a) INSPIRE records, dated by first-version submission, against arXiv's statistics pages, dated by announcement** (my calculation; January–September growth, 2025 → 2026):

| Archive | By announcement | By v1 submission |
|---|---|---|
| hep-ex | +14.2% | +13.7% |
| hep-ph | +18.1% | +18.5% |
| hep-th | +23.7% | +23.9% |
| nucl-ex | +1.8% | +1.5% |
| nucl-th | +15.7% | +17.4% |
| hep-lat | +5.5% | +5.7% |

- Monthly counts for September 2026 are also nearly identical, for example hep-ph 740 against 741.
- **Papers announced in a later month than submitted:** 2.5% of INSPIRE records overall, and 1.9–3.3% in each year from 2017 to 2026, with no rise in 2026.
- **The dates are submission dates.** INSPIRE's `preprint_date` falls on a Saturday for 4.7% of records and on a Sunday for 6.2%, days on which arXiv does not announce.

**(b) The arXiv flag table.**
- **Coverage.** `v1_submitted` is filled for papers never revised, or revised within the month of their identifier (`load_oai`). That is 94% of the 8,360 mathematics papers of September 2026.
- **Spill-over.** Among them:
  - 4.5% were submitted before September, against 5.0% in September 2025;
  - 2.7% were submitted more than seven days before 1 September, against 0.8% in September 2025 and 0.2–1.2% in other months of 2026.
- **Counted by v1 month.** Among papers with a known v1 date, 7,697 were submitted in September 2026 and 7,842 were announced in it, a difference of 1.8%.
- **Reading.** The September 2026 spike in mathematics is a spike in submissions, not a release of held papers. Holds rose, but they explain a few per cent at most.

**Caution.**
- **Use `v1_submitted` only for lags within a month.** Do not use it as a sample for growth: its coverage falls with paper age (about 50% for 2019–2023, more than 80% for 2026) because revisions are right-censored.
- **Complete it for revised papers** with the arXivRaw adapter.

**October 2026 is informative now.**
- By the harvest of 16 October, 4,574 mathematics papers had October identifiers.
- 4,339 of them, with known v1 dates, were submitted in October. That is September's pace, under the new cap of two submissions per submitter.

That is a cheap first look at the Q4 test of H2 that I proposed in round 1. The cap binds submitters, not co-authors, so it is suggestive only.

**Fix.**
- Report (a) and (b), and complete (b) for revised papers.
- Remove the [ANALYSIS PENDING] marker, and the announcement item from Limitations and the Discussion.
- Add one sentence on October.
- With v1 dates, batch posting by heavy producers becomes measurable: the share of an author's quarterly papers submitted within seven days.

#### N7. OSF is blocked: take the social-science series out of the main text

**Why.**
- The continuity check across the 2025 change of counting method cannot be run.
- The series is "not interpreted".
- After the switch, SocArXiv rises from 490 first versions (2025 Q1, counted by paging) to 1,324 (2026 Q3), with SocArXiv's own per-author limit in force since March 2026 (`osf_quarterly.csv`).

**The deposit README is inconsistent.** It says that `osf_continuity.csv` "was retrieved at the 36 s pace", but no such file exists in the branch, and v2 calls the check pending.

**Fix.**
- Remove the series from Fig 1 and Table 3; at most, keep it in S2 Table with the caveat.
- Correct the README.

#### N8. Other integrity issues

1. **Two definitions of "mathematics".**
   - **The gap.** The OAI series of primary math.\* papers is 89.9% of the statistics-page "math" count in January–September 2019, and 92.3% in 2026 (24,667 against 27,450; 44,457 against 48,151).
   - **Not math-ph alone.** The gap is 2.6–3.3 times math-ph's own count. It presumably consists of papers whose primary category is an alias with a canonical name outside math, such as math-ph/math.MP and cs.IT/math.IT.
   - **Growth agrees:** +43.2% against +43.3% from 2025 to 2026.
   - **Which uses which:**
     - Fig 1, Table 3, the synthetic control and the rank use the statistics pages;
     - H2, H3, the genre split and the September count of 8,360 use OAI.
   - **Fix.** Say so in Methods.
2. **Revision censoring affects every OAI field used as a time series:** comments (genre), abstracts (markers), author lists (H2) and categories. Add one sentence to Methods, and treat the 2026 cohort's metadata as less mature.
3. **The committed `round1_tests.json` and `results.md` are stale for C3.**
   - **The stale values.** They hold pre-correction values:
     - 2026: 0.99 (0.88–1.10);
     - 2026/2025: 1.08 (1.01–1.14);
     - year-shock z: −0.19;
     - slope change after December 2022: −4.5% a year, p = 0.17.
   - **My re-run on the corrected data** reproduces v2's Table 1:
     - 2026: 1.01 (0.90–1.14);
     - 2026/2025: 1.10 (1.03–1.18);
     - z = 0.19;
     - bases 2019 and pooled: 1.01.
   - **It also fills the cell marked "not yet recomputed".** The slope change after December 2022 is −3.8% a year (−8.6 to +1.3; bootstrap p = 0.27), and after November 2024 −2.0% (−8.2 to +4.5; p = 0.66).
   - **Consequence.** `results.md`, as committed, gives two different C3 estimates in two sections.
4. **The medRxiv correction works on DOIs only** (N5).

### 4.3 Positioning and literature

#### N9. The positioning against Qi et al. misreads their finding, and I contributed to the error

**The framing in v2.**
- The Introduction says Qi et al. "report that computationally intensive fields benefited more than others [11]".
- It then frames the article "as a falsification test of the account in which computational intensity governs where output grows".
- It adds that the finding "rests on comparisons between servers and fields".

**What Qi et al. measure.** Their claim concerns a different quantity.
- **The measure.** Research question 5 ("Recomposition. Has it altered the disciplinary balance of scientific output?") measures "the share of AI-related manuscripts … defined as the proportion of documents per discipline".
- **The finding.** Finding 5 reads: "AI adoption is highly uneven across disciplines: exceeding 50% in computer science", "remaining below 20% in physics and mathematics" (https://arxiv.org/html/2510.17882v1).
- **The comparison.** Disciplines are taken from "repository-specific subject taxonomies", so the comparison runs across fields within each repository, not between servers.

**My round-1 review was wrong** to say that "their design compares servers" and to propose the paper as "the within-field test their design lacks".

**What Qi et al. report about volume.**
- Interrupted time series up to August 2025 give "significant post-ChatGPT slope increases in all repositories, most notably in arXiv", followed by bioRxiv.
- Their Table IV, as read from the HTML version, gives slope changes of +477.38 a month (SE 70.32) for arXiv and +29.60 (SE 5.61) for bioRxiv.
- Their text reads: "arXiv and bioRxiv exhibiting accelerated accumulation after ChatGPT, whereas medRxiv and SocArXiv remain relatively flat".

v2 reports that bioRxiv did not depart from its own trend (0.91). That contrast with Qi et al. is a different counterfactual for the same server, and it needs one sentence of reconciliation.

**Fix.**
1. **Describe Qi et al.'s finding accurately:** AI-related topics, by discipline, within repositories.
2. **Re-target the falsification framing** to the hypothesis as stated (Blekhman; H1), citing Qi et al. as motivation that AI's footprint differs across fields.
3. **Note that Qi et al.'s measure is AI as topic.** This is exactly why the AI-topic split of bioinformatics, still pending, matters for C2.
4. **Reconcile the bioRxiv result.** Qi et al.'s volume model finds a post-ChatGPT slope increase on bioRxiv to August 2025; v2's trend model, with a different pre-period and a COVID-19 indicator, does not. Say which counterfactual each uses.

#### Nee et al.

- **The text is accurate.** I re-read the abstract (https://arxiv.org/abs/2609.04872; still v1 on 17 October 2026): 47,127 list entries, 11.9% above the synthetic counterfactual, 9.6–14.9% across designs, and 2.45% → 3.80% of author units with at least five submissions. v2's account of these is accurate.
- **One remaining fix: report the like-for-like panel.**
  - The `maths_list_entries` variant (January–August, all names) gives 35,308 → 47,142 papers. That matches Nee's 47,127 entries for 2026 within 15.
  - It also gives 2.80% → 4.07% of names with at least five papers.
  - The remaining difference from Nee's 2.45% → 3.80% comes from the name key: the companion folds accents and keeps letters only, while Nee et al. keep exact Unicode-normalised names.
  - **The relative rise is similar:** 1.45-fold (list entries), 1.59-fold (primary only), 1.55-fold (Nee).
  - **Fix.** Report the list-entry figure as the comparison and the primary-only figure as a variant.

#### Accuracy of the references

**Verified.** I checked every reference added in v2, plus the preprints the argument rests on, against Crossref or the arXiv API on 17 October 2026. All resolve, with correct authors, titles, venues, volumes and pages. They include:
- Qi et al., Nee et al. (v1), Lin and Zhu, Holzwarth et al., He and Bu (v2), Elazar and Antoniak (v2), Shah and Filimonovic et al.;
- Kusumegi et al., Renault et al. (PNAS 123(33):e2618638123, published 11 August 2026), Spick et al. (J Clin Epidemiol 193:112203) and Gartenberg et al. (Organ Sci 37(3):795–812);
- Liang et al. (Nat Hum Behav 9(12):2599–2609), Blekhman (PLoS Biol 24(10):e3004075, 15 October 2026), Hansen, Hanson et al. and Geng and Trotta;
- Ioannidis et al. 2024, Bornmann et al. and Pruller et al.

**Points to fix.**
- **Ref. 68 (Pruller et al.)** lacks its DOI: 10.1371/journal.pone.0337199 (PLOS One 20(11):e0337199, 18 November 2025). Check that it supports "from April 2024".
- **Renault et al.** Crossref lists the item as a journal article. Whether PNAS labels it a Letter has to be checked on the PNAS page ([AUTHOR], as the response says).
- **Liang et al.'s bioRxiv values ([RECHECK]).** They can be read in the open preprint version, Liang et al., "Mapping the increasing use of LLMs in scientific papers", arXiv:2404.01268 (950,965 papers, January 2020 to February 2024, arXiv, bioRxiv and Nature portfolio; https://arxiv.org/abs/2404.01268). Note that its window differs from the journal version's.
- **"As in Kobak et al."** misstates what Kobak et al. found (N2).

#### Literature still missing

All verified on Crossref or arXiv; each supports a sentence the paper already makes.

| Reference | Supports |
|---|---|
| Malički M, Jerončić A, ter Riet G, et al. Preprint servers' policies, submission requirements, and transparency in reporting and research integrity recommendations. JAMA. 2020;324(18):1901–1903. doi:10.1001/jama.2020.17195 | "servers screen submissions and differ in the genres they accept"; the cites are now the bioRxiv FAQ, medRxiv's About page and Sever et al. |
| Kirkham JJ, Penfold NC, Murphy F, et al. Systematic examination of preprint platforms for use in the medical and biomedical sciences setting. BMJ Open. 2020;10(12):e041849. doi:10.1136/bmjopen-2020-041849 | The same sentence |
| Ginsparg P. Lessons from arXiv's 30 years of information sharing. Nat Rev Phys. 2021;3(9):602–603. doi:10.1038/s42254-021-00360-z | arXiv's moderation and announcement process |
| Strotmann A, Zhao D. Author name disambiguation: what difference does it make in author-based citation analysis? JASIST. 2012;63(9):1820–1833. doi:10.1002/asi.22695 | Effects of name matching on author-level measures, beside Milojević and Kim and Diesner |
| Waltman L, van Eck NJ. Field-normalized citation impact indicators and the choice of an appropriate counting method. J Informetr. 2015;9(4):872–894. doi:10.1016/j.joi.2015.08.001 | Fractional counting, which H2 uses |
| Gray A. ChatGPT "contamination": estimating the prevalence of LLMs in the scholarly literature. arXiv:2403.16887. 2024 | An early estimate of prevalence, for S4 Table |

### 4.4 Deposit, reproducibility and disclosure

#### N10. The deposit plan is close to what PLOS needs, but the statement, the pipeline and the disclosures do not yet match the files

1. **The single rebuild command misses `stats_round1.py`.**
   - **The gap.** `run_all.sh` does not call it, and the deposit README does not list it. Its output, `round1_tests.json`, supplies:
     - Table 1's rows on placebos, pooled bases, Snowmass cleaning, acceleration and slope changes;
     - the list-entry results;
     - the INSPIRE, PubMed, genre and medRxiv-flag results.
   - **A cumulative file.** The script also merges each section into the existing JSON, so the committed file is the cumulative product of runs on different inputs. That is how the stale C3 values survived (N8, item 3).
   - **Missing harvest commands.** The README lacks the commands for INSPIRE, the medRxiv records, PubMed by US affiliation and arXivRaw.
   - **My re-run** of `build_datasets.py`, `analyze_trends.py`, `analyze_within_field.py`, `stats_within_field.py`, `stats_fields.py`, `stats_markers.py`, `stats_round1.py` (all sections that need no OAI harvest) and `report_stats.py`:
     - It ran on a copy of the committed data, with numpy 2.5.3, pandas 3.0.5, scipy 1.18.1 and statsmodels 0.15.0.
     - It reproduced byte for byte `within_field_tests.json`, `field_tests.json`, `marker_tests.json`, `core_marker_words.txt`, `marker_growth_panel.csv` and every file in `data/processed/` that I checked.
     - `round1_tests.json` and `results.md` changed, and only in the C3 estimands.

     This is a good result for the pipeline and a bad one for the committed state.
   - **Fix.**
     - Add `stats_round1.py`, with all its sections, to `run_all.sh`.
     - Regenerate from scratch rather than merging.
     - Pin the environment.
     - List every harvest command.
2. **Record-level tables: more exists than v2 says, and less than PLOS needs.**
   - **Already committed:**
     - `arxiv_paper_flags.csv.gz`: identifier, identifier month, v1 date where known, latest-version date, primary category, number of authors, genre and planning flags;
     - `medrxiv_records.csv.gz`: DOI, date, category, country of the corresponding institution, COVID-19 and dataset flags;
     - `inspire_hep_records.csv.gz`: curated INSPIRE fields, no names;
     - the medRxiv ND samples.
   - **Missing:**
     - a bioRxiv record table: DOI, v1 date, category, duplicate flag, licence and COVID-19 flag;
     - complete v1 dates;
     - the OAI datestamp of each arXiv record, so that a re-harvest can be restricted to the same versions;
     - the term that triggered each genre label;
     - the ND/NN labels and samples, once the test is run.
   - **Fix.** Update the Data availability statement to list what is deposited.
3. **Author-level privacy.**
   - **Do not release a heavy-producer flag at paper level.** In round 1 I asked for a "prolific" flag in the record-level table; I withdraw that request. Joined to arXiv's public author lists, such a flag identifies the heavy producers directly.
   - **Hashing does not protect here.** A salted hash of name strings keyed by paper identifier can be linked just as easily, so it gives little protection.
   - **Two defensible options:**
     - **(a) Release nothing at author level.** Rely on the public CC0 source plus the exact list of records (identifiers and OAI datestamps) and the code. Anyone can then reproduce H2, apart from later changes to the metadata.
     - **(b) Controlled access through a named contact who is not an author.** PLOS accepts this when legal or ethical restrictions apply.
   - **Name the framework in the Ethics statement.** EMBL applies its own Internal Policy No. 68 on data protection, with a Data Protection Officer and a Data Protection Committee as supervisory body (https://www.embl.org/documents/document/internal-policy-no-68-on-general-data-protection/; https://www.embl.org/info/data-protection/). UPF is bound by the GDPR. The statement should say which framework governs this processing, and record the advice received.
4. **The request-pacing disclosure is frank, with three errors and one gap.** Disclosing the 1 s pauses against arXiv's 15 s crawl delay, and the OSF retrievals faster than documented, is exemplary. But:
   - **(i) "No request was refused" (Methods)** is contradicted by the companion's own record. The arXiv API "answered '429 Rate exceeded' from this environment" (`harvest_arxiv_raw.py`, `v1_dates_from_raw.py`). State it, and say that the environment's network address may be shared, which can trigger rate limits even for a compliant client.
   - **(ii) The OSF file.** The README claims `osf_continuity.csv` was retrieved; it is absent (N7).
   - **(iii) Parallel connections.** The bioRxiv and medRxiv harvests used two to four parallel connections (deposit README). Methods says only that the API "states no limit". I confirm the API page states no terms or limits (https://api.biorxiv.org/, read 17 October 2026), but Methods should report the parallelism.
   - **(iv) The gap: INSPIRE.** Replace the [RECHECK] with the documented limit and the pacing used.
     - The limit: "every IP address is allowed 15 requests in a 5s window" (https://github.com/inspirehep/rest-api-doc).
     - The pacing: at most one request a second (`harvest_inspire.py`).
     - The licence: "most of the metadata is available under a CC0 license", with "bulk collection of email addresses" not allowed. The harvest collects none.
   - **OSF's documented limit.** The rate cited for OSF (100 unauthenticated requests an hour) comes from the osfr vignette (https://packages.ropensci.org/osfr/doc/auth.html), not from OSF's own documentation. Say so.
5. **Licences and third-party text.**
   - **Data licence.** CC BY 4.0 is acceptable to PLOS, but tables derived from CC0 sources (arXiv, INSPIRE) can stay CC0, which avoids adding conditions.
   - **Titles in the coding sheet.** The medRxiv coding sheet (`docs/stats/validation/medrxiv_flag_coding_sheet.csv`) publishes 200 titles. That contradicts "No titles, abstracts or author names are redistributed". Either drop the titles (keeping DOIs and links) or correct the statement.
   - **Abstracts in the ND validation sheet.** That sheet will republish abstracts, restricted to Creative Commons-licensed bioRxiv and medRxiv preprints. CC BY licences require attribution, which a blinded sheet withholds: the identifiers sit in `sealed/`. Keep the sheet out of the public repository until coding is finished, then publish it with attribution, and correct "Abstracts are not redistributed" in Methods.

---

## 5. Minor issues

1. **The Abstract on physics.** "Physics fell to 1.06 without planning white papers in its 2022 base": the same cleaning against 2017–2019 gives 1.11 (Table 1). Give both or neither.
2. **"14 of the 18 arXiv archives stood at least 1.25 times their trends."** Correct. The note to Table 3 should say that the largest departures are in archives whose pre-2023 trend was falling: math-ph, nucl-th and nlin.
3. **H2 headline.**
   - The Abstract's "in mathematics the top 1% of names more than tripled theirs" is the Q3 figure (+266%).
   - January–August gives +78%; July–August +135%; namesake-robust January–August +63%.
   - Results says "by 78% to 211%" across four variants. Variants that combine two restrictions run lower (namesake-robust established names, January–August: top 1% +62%, bottom 90% +12%).
   - Lead with a window that is robust to September, or say "in the third quarter".
4. **One H2 variant contradicts "fastest at the top".** In theoretical physics, the namesake-robust July–August variant has the top 1% growing least (+10%, against +26% for the next 9% and +15% for the bottom 90%). "Fastest at the top" holds in the main specification but not in every variant; say so.
5. **Table 2.** State in the table that ratios of rises are relative to each group's baseline (N2), and add a row with absolute excess.
6. **"crucial" and "insights"** are not core words (N2, item 4).
7. **Fig 1.** "Indexing to 2022 favours series whose 2022 count was low" is good. Add that medRxiv grew 2.39-fold in levels since 2022, more than any arXiv series (my calculation: 4,987 → 11,910 non-COVID preprints in January–September).
8. **Methods: the arXiv harvest.**
   - The OAI `created` field gives the latest version's date. The OAI metadata (abstracts, comments, authors, categories) are current, not first-version.
   - INSPIRE is dated by `preprint_date`, a submission date.
9. **S2 Appendix timeline.** Close two [RECHECK] items and add two events.
   - **arXiv's post of 1 October 2026** (https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/) says:
     - "Rate-limiting is an established arXiv policy, with limiting originally primarily left to moderator discretion";
     - "If your allotted submissions from a previous month are on hold in the next month, they do not count against your submission limit for next month";
     - papers of authors who submit quality work "can be delayed for days or weeks". That sentence comes from a quoted statement by Thomas Dietterich.

     The row "Until Oct 2026" is therefore supported.
   - **openRxiv** was announced on 11 March 2025 (sources in N5).
   - **Add:** the medRxiv DOI prefix 10.64898 from 2 December 2025, and the onset of duplicate listings in 2026.
10. **S2 Appendix, INSPIRE queries.** R3's queries were made by an AI agent and have not been re-run. The rule-based classification supersedes them, but the sample classification of 60 records (1 of 60 reporting new measurements) still motivates the pre-registration. Say that this motivating number is unvalidated.
11. **"Data were retrieved on 15–16 October 2026."** Add the dates of the INSPIRE and arXivRaw harvests, and of the ND samples.
12. **Retrieval of version-1 abstracts.** The marker counts for bioRxiv and medRxiv use version-1 text; arXiv's use the latest version (N2). Say so in Methods.
13. **"Archive and category labels are weak proxies"** (Discussion). Add that 67–69% of hep-ex and nucl-ex list entries are cross-lists (N5b).
14. **medRxiv flag validation.** Precision from the coding sheet will not give recall. Add 100 randomly sampled unflagged non-COVID preprints.
15. **Country of the corresponding institution.** `medrxiv_records.csv.gz` already carries a US/non-US flag, and the bioRxiv split is pending. Its classifier was checked by an AI agent on 150 records; have a person check it before use.
16. **"PubMed requests stayed within three a second".** True of the scripts. Add the date and query of the US-affiliation retrieval.
17. **Kusumegi et al.** Keep the output-gain sentence with Renault et al.'s critique ([AUTHOR] in the Introduction). Limitations already uses both, and removing one would leave the other unexplained.
18. **"The bioRxiv and medRxiv API states no limit"** is accurate as of 17 October 2026 (https://api.biorxiv.org/).
19. **Word counts.** The header's "Markers outside HTML comments: [AUTHOR] 53, [ANALYSIS PENDING] 18, [RECHECK] 9" is a useful check; keep it in the build until all reach zero.

---

## 6. Requested checks, ranked by information value

| Rank | Check | Why it matters | Cost |
|---|---|---|---|
| 1 | **Close the dating question** (N6): report INSPIRE against the statistics pages, and the unrevised-paper lags for mathematics; complete revised papers with arXivRaw; add October 2026 | Removes an [ANALYSIS PENDING] marker, an open explanation and a Limitation; gives a first look at the cap | Low; the data are committed |
| 2 | **De-duplicate bioRxiv** (N5): record harvest, `rebuild_rxiv_from_records.py`, re-estimate everything that uses bioRxiv; check duplicates under different DOIs on both servers | bioRxiv is the comparator for the main exploratory finding and the server for C2 | Moderate (the record harvest); the scripts exist |
| 3 | **Narrow and validate the genre claim** (N1): Abstract wording, INSPIRE validation, journal-name exclusions, 200 hand-coded mathematics papers, a sensitivity analysis on revision | The Abstract makes a claim the check does not support | Low to moderate |
| 4 | **Marker metric** (N2): absolute excess and lower bounds for every group, bioRxiv and medRxiv included; a baseline sensitivity for arXiv | Decides whether H3's within-field reading survives | Low (re-aggregation) |
| 5 | **Rewrite the positioning against Qi et al.** (N9) | Accuracy of the framing | None |
| 6 | **Report the like-for-like Nee panel** (M3c) | Exact replication of the author-level comparison | None (already computed) |
| 7 | **Delete or redo the PubMed accounting** (N4) | Removes a claim the measure cannot carry | None to delete; moderate to redo |
| 8 | **Deposit and pipeline** (N10): `stats_round1.py` in `run_all.sh`, regeneration from scratch, pinned environment, complete record tables, accurate disclosure | PLOS's minimal data set; reproducibility; accurate statements | Low |
| 9 | **INSPIRE diagnostics** (N3): link and type shares by year, the collaboration-only sensitivity, a re-harvest to measure lag, a spot check of 100 records | Validity of the exploratory component that motivates the pre-registration | Low |
| 10 | **medRxiv flags**: code the sheet (precision) and 100 unflagged preprints (recall) | Validity of C3 | Low (author time) |
| 11 | **Pending round-1 items for C2**: bioRxiv without COVID-19 record by record; the AI-topic split of bioinformatics; structure-matched placebos | C2 is the only contrast whose model interval excludes 1 | Moderate |
| 12 | **Batch posting by heavy producers**, now measurable with v1 dates | Separates breadth from a few heavy submitters, which arXiv's own account emphasises | Low |
| 13 | **Remove OSF from the main text** (N7) | Removes an unvalidated series | None |

---

## 7. Strengths

- **Honest reframing.** The paper now says plainly that a pre-specified falsification test failed, and it keeps the failed hypothesis visible rather than rewriting it. That is rare and valuable.
- **Inference.**
  - Placebos are the primary inference.
  - The year-shock calibration and the minimum detectable effects make the nulls interpretable.
  - The Deviations section is a model of disclosure.
- **The H2 decomposition** on combined output avoids regression to the mean. It has an analytic null (every class grows at the total rate under proportional growth) and an empirical one (pairs of years before ChatGPT's release). This is the right design, and it is now reported for mathematics.
- **H3 rests on a measured marker, with its drift documented** instead of being read as falling use. The mathematics result (smallest rise, largest acceleration) holds under every metric I tried.
- **New checks that changed conclusions.** Snowmass cleaning, list entries, the medRxiv duplicate correction and the INSPIRE component were all reported whatever they showed. Several moved estimates against the author's prior.
- **A pipeline that reproduces.**
  - My re-run reproduced the main statistics byte for byte with different package versions.
  - The only differences traced to a stale committed file, not to the code.
  - Record-level tables already exist for arXiv, medRxiv and INSPIRE.
- **Transparency about terms of use.** The two retrievals faster than documented limits are disclosed without being asked, and the scripts were corrected.
- **The pre-registration** names held-out archives, fixes the classifier prompts, and records deviations before results are seen. It is the right next step for a hypothesis formed after seeing the data.
