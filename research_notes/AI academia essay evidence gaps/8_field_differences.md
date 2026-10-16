# Field differences: is experimental biology less affected by generative AI than physics, mathematics and computer science?

Notes for the essay's field-differences point (`paper/brief.md`, "Author decisions after the citation audit", item 3). Compiled 16 Oct 2026.

**Tags.**
- **[PREPRINT]:** not peer reviewed as of 16 Oct 2026.
- **[BLOG]:** a personal blog or newsletter.
- **[NEWS]:** journalism.
- **[COMPANY]:** company work without peer review.
- **[OWN CALC]:** my own arithmetic on a primary data source.
- **[FIG]:** read off a published figure by eye; approximate.
- **[TOOL]:** a detail extracted from a full text by a fetch tool and not re-read line by line. Re-check before quoting.

**Verification.**
- **Identifiers.** On 16 Oct 2026, every DOI below resolved in Crossref and every arXiv ID in the arXiv API.
- **Abstracts** come from Europe PMC, Crossref or arXiv.
- **Quotations and numbers given verbatim** were re-read in the primary full text:
  - Kobak et al.: PMC XML.
  - Nee et al., Holzwarth et al. and Hao et al.: arXiv HTML.
  - Lin & Zhu, Geng & Trotta, He & Bu, Gao & Wang and Duede et al.: arXiv PDFs.
  - Blekhman: the publisher PDF in `paper/sources/`.

**Reused material.**
- Note 3: entries for Hao, Liang, Kobak, Bianchini, Duede, and Gao & Wang.
- Literature note 2: Suchak; Naddaf.
- The citation audit: R34 on Hao's wording; R71 on the bioRxiv FAQ.
- `paper/figures/README_companion_analysis.md` and `paper/sources/Blekhman_2026_summary.md`.

**Two corrections to inputs.**
1. **Hao et al.'s wording.** Note 3 (Q1, "What drives AI's concentration") says data availability is "the main driver" in Hao et al. The source says it "appears to be a major impacting factor" (audit R34; re-verified below). Do not reuse "main driver".
2. **Liang et al.'s preprint** is arXiv:2404.01268, not a 2402.x identifier.

---

## 1. How prevalent is LLM-modified text, by field?

### Takeaway
On writing, biology is not behind physics.
- **Across fields.** In every study that compares fields, computer science (CS) is highest, mathematics lowest, and biology at or above physics:
  - arXiv quantitative biology 11% against physics 10% (end of 2023);
  - bioRxiv above arXiv physics in Liang et al.'s preprint figure (February 2024).
- **Biomedical journals.** Prose there is now widely LLM-assisted: at least 13.5% of 2024 PubMed abstracts (a lower bound), and 77% of 2025 PMC papers by a newer estimator [PREPRINT].
- **Within biomedicine,** computational fields lead (about 20%).

"Biology is less affected" therefore cannot mean "biologists write with AI less".

### Cited Findings

**Liang et al. (2025), *Nature Human Behaviour***
- **Citation.** Liang, W. et al. (2025). Quantifying large language model usage in scientific papers. *Nature Human Behaviour* 9(12):2599–2609. Online 4 Aug 2025. — [DOI](https://doi.org/10.1038/s41562-025-02273-8); [Europe PMC](https://europepmc.org/article/MED/40760036)
- **Abstract.**
  - **Scope:** "a systematic analysis across 1,121,912 preprints and published papers from January 2020 to September 2024 on arXiv, bioRxiv and Nature portfolio journals, using a population-level framework based on word frequency shifts".
  - **Highest:** "the largest and fastest growth estimated for computer science papers (up to 22%)".
  - **Lowest:** "mathematics papers and the Nature portfolio showed lower evidence of LLM modification (up to 9%)".
  - **Correlates:** estimates were higher "among papers from first authors who post preprints more frequently, papers in more crowded research areas and papers of shorter lengths".
  - — [Europe PMC](https://europepmc.org/article/MED/40760036)
- **What the measure is.** The estimated fraction of *sentences* substantially modified by an LLM, estimated for a whole corpus, not paper by paper. — [arXiv v1](https://arxiv.org/abs/2404.01268v1)
- **What is missing.** The NHB abstract gives no bioRxiv or physics value. The NHB full text redirected to a login page, so I could not read its per-corpus values to September 2024.
- **The preprint [PREPRINT].** "Mapping the increasing use of LLMs in scientific papers", arXiv:2404.01268v1 (1 Apr 2024). It is the only arXiv version. — [arXiv:2404.01268v1](https://arxiv.org/abs/2404.01268v1)
  - **Coverage:** 950,965 papers, January 2020 – February 2024.
  - **Abstract:** CS "up to 17.5%"; "Mathematics papers and the Nature portfolio showed the least LLM modification (up to 6.3%)".
  - **February 2024 values [TOOL]:** electrical engineering and systems science (EESS) 14.4%, mathematics 4.9%, Nature portfolio 6.3%.
  - **November 2022 values [TOOL]:** CS 2.3%, EESS 2.9%, mathematics 2.4%, Nature portfolio 3.1%.
- **Physics, statistics and bioRxiv appear only in Figure 1 of the preprint [FIG].**
  - **Values at February 2024, read by eye:** statistics ≈9%, bioRxiv ≈8.5%, physics ≈6.5%, Nature portfolio ≈6%, mathematics ≈5%.
  - **Ordering:** the bioRxiv line runs above arXiv physics from about mid-2023.
  - **Introductions:** bioRxiv introductions were not analysed, because there is "no bulk download of PDFs".
  - — [arXiv:2404.01268v1 PDF, Fig. 1](https://arxiv.org/pdf/2404.01268v1)

**Kobak et al. (2025), *Science Advances*, and the 2026 follow-up**
- **Citation.** Kobak, D., González-Márquez, R., Horvát, E.-Á. & Lause, J. (2025). Delving into LLM-assisted writing in biomedical publications through excess vocabulary. *Science Advances* 11(27):eadt3813. July 2025; open access, PMC12219543. — [DOI](https://doi.org/10.1126/sciadv.adt3813); [Europe PMC](https://europepmc.org/article/MED/40601754)
- **Headline.** 15,103,888 PubMed abstracts from 2010–2024. "at least 13.5% of 2024 abstracts were processed with LLMs. This lower bound differed across disciplines, countries, and journals, reaching 40% for some subcorpora." — [DOI](https://doi.org/10.1126/sciadv.adt3813)
- **By field.**
  - **Method:** "We assigned papers to the 39 fields based on the journal names". For example, journals with "neuroscience" in the title form the neuroscience field. A subgroup was scored only if it had at least 300 papers in each year from 2018 to 2023.
  - **Result:** "Computational fields like computation and bioinformatics showed Δ ≈ 0.20".
  - **Range:** across fields, countries and journals, the lower bound "ranged from below 5% to more than 40%".
  - **What the text does not give:** it does not name the lowest fields. Their values are only in Fig. 5B.
  - — [Europe PMC full text](https://europepmc.org/article/MED/40601754)
- **By country.** "some English-speaking countries like United Kingdom and Australia showed Δ ≈ 0.05, while countries like China, South Korea, and Taiwan showed Δ ≈ 0.20". — [same](https://europepmc.org/article/MED/40601754)
- **By journal.**
  - **Highest:** Sensors 0.25; Cureus 0.20; MDPI journals pooled 0.21; Frontiers 0.20.
  - **Lowest:** Nature, Science and Cell 0.07; Nature family journals 0.10.
  - **Intersections:** South Korea × Sensors 0.34; "computation papers from China" 0.41.
  - — [same](https://europepmc.org/article/MED/40601754)
- **The authors' explanation.** The 20% bound in computational fields "could be due to computer science researchers being more familiar with and willing to adopt LLM technology". — [same](https://europepmc.org/article/MED/40601754)
- **The authors' caveats** (verbatim):
  - native speakers "may be better at noticing and actively removing unnatural style words from LLM outputs";
  - "publication timelines in computational fields are often shorter than in many biomedical or clinical areas, meaning that any potential increase in LLM usage can be detected earlier in computational journals";
  - "We expect the lower bounds documented here to increase with these longer observation windows";
  - the results "indicate widespread usage in most PubMed-indexed fields, countries, and journals, including the most prestigious ones".
  - — [same](https://europepmc.org/article/MED/40601754)
- **[PREPRINT] Holzwarth, L., González-Márquez, R. & Kobak, D. (2026).** Most biomedical publications show signs of LLM-assisted writing. arXiv:2608.10715v1 (11 Aug 2026). — [arXiv:2608.10715](https://arxiv.org/abs/2608.10715)
  - **Corpus and method:** PubMed Central open-access full texts, with a new frequency-based estimator.
  - **Headline:** "by the end of 2025, 89% of papers show excess of LLM-associated vocabulary".
  - **Full text (verbatim):**
    - **Full papers:** β̂ = 0.77 in all of 2025 and 0.89 in December 2025.
    - **Abstracts:** 0.53 in 2025 and 0.68 in December 2025.
    - **Reading:** "by the end of 2025, 9 out of 10 papers exhibited signs of LLM-assisted writing or editing"; "All sections showed continually increasing estimated LLM usage starting in early 2023".
    - **Methods sections:** lowest, at 0.32 on cropped paragraphs and 0.54 on whole sections (December 2025).
  - **[TOOL] Sample:** 1,194,287 papers from 2017–2025, with no breakdown by field.
  - **[TOOL] Countries:** majority-English-speaking countries are lower (UK 0.28 against China 0.82 in 2025).
  - **[TOOL] Limits:** the method cannot separate editing from generation, and it assumes the human word-frequency trend of 2018–2022 continues.

**Other studies that break prevalence down by discipline**
- **[PREPRINT] Lin, C. W. & Zhu, W. (2025).** Divergent LLM adoption and heterogeneous convergence paths in research writing. arXiv:2504.13629v1 (18 Apr 2025). — [arXiv:2504.13629](https://arxiv.org/abs/2504.13629)
  - **Data and method:** 627,384 arXiv papers from 2021–2023, with fine-tuned classifiers for each discipline and prompt. Adoption is normalised to zero before November 2022.
  - **Result (verbatim):** "By the end of 2023, the share of AI-generated abstracts increased by 22% in Computer Science, 21% in Electrical Engineering and Systems Science (EE&SS), 18% in Finance, 15% in Statistics, 11% in both Economics and Biology, 10% in Physics, and 3.5% in Mathematics compared to the end of 2022."
  - **The authors' reading:** "disciplines more closely tied to computational and quantitative methods demonstrating higher uptake".
  - **What "Biology" means here:** arXiv's quantitative-biology archive. It had 2,655 papers in 2023, against 84,966 in physics (their Table 1).
- **[PREPRINT] Geng, M. & Trotta, R. (2024).** Is ChatGPT transforming academics' writing style? arXiv:2404.08627v2. — [arXiv:2404.08627](https://arxiv.org/abs/2404.08627)
  - **Data:** about 1M arXiv abstracts, May 2018 – January 2024, in four categories only (cs, math, astro-ph, cond-mat).
  - **Results:**
    - **cs:** about 35%, against a GPT-3.5 "revise the following sentences" baseline.
    - **The other three:** "a much smaller uptick in ChatGPT impact in math, while astro and cond-mat both reach values between 10% and 20%, approximately."
- **[PREPRINT] He, Y. & Bu, Y. (2025).** Academic journals' AI policies fail to curb the surge in AI-assisted academic writing. arXiv:2512.06705v2 (20 Jan 2026). — [arXiv:2512.06705](https://arxiv.org/abs/2512.06705)
  - **Data and method:** 5,114 journals and more than 5.2M papers, 2021–2025. A distributional estimator of the kind Liang et al. use, applied to adjectives in abstracts, plus keyword counts.
  - **Domain results:**
    - "physical sciences showed the most significant increase in AI content proportion";
    - social sciences showed "relatively smaller increases";
    - "Physical Sciences" is OpenAlex's domain, which "also includes mathematics, computer science, and related engineering fields".
  - **Monthly growth in the share of AI content** (mean logarithmic increments, Table S4; journals with / without AI policies):
    - Physical Sciences: 0.054 / 0.056
    - Social Sciences: 0.038 / 0.049
    - Life Sciences: 0.034 / 0.037
    - Health Sciences: 0.031 / 0.024
  - **Disclosure:** of the 75k papers published since 2023 in the full-text sample, 76 (about 0.1%) disclosed AI use.
- **[PREPRINT] Gray, A. (2025).** Estimating the prevalence of LLM-assisted text in scholarly writing. arXiv:2512.01560. — [arXiv:2512.01560](https://arxiv.org/abs/2512.01560)
  - **Data:** full text indexed in Dimensions, "across the full range of research".
  - **Result:** LLM tools were likely involved in "more than 10% of all published papers in 2024".
  - **What is missing:** no field breakdown appears in the abstract, and the full text could not be opened.

### Inferences
- **Writing adoption cannot explain why biology's output grows more slowly.**
  - **The ranking is stable.** Within studies, CS and EESS are highest and mathematics lowest. Physics, statistics and biology sit in between, with biology at or above physics in two kinds of data:
    - arXiv data (Lin & Zhu);
    - bioRxiv compared with arXiv (Liang's preprint figure).
  - **Use in biomedical journals** is widespread and rising (Kobak; Holzwarth).
  - **The one contrary signal** is He & Bu's slower growth in the life and health domains. It is measured at a coarse domain level whose "physical sciences" include CS and mathematics.
- **Levels cannot be compared across studies.** Each study measures a different thing, so only rankings within a study mean anything:
  - Liang: a share of sentences;
  - Kobak: a lower bound on the share of abstracts;
  - Holzwarth: a share of papers;
  - Lin & Zhu: a classifier share, normalised to the pre-ChatGPT baseline.
- **The draft's ¶2.1** sets 13.5% (PubMed abstracts, a lower bound) beside 22% (CS, a share of sentences). That is fine for "use is broad", but it must not be read as "biomedicine is lower than CS".
- **The mathematics paradox.**
  - Mathematics has the lowest prevalence of LLM writing in every arXiv study, yet the largest output surge in 2026 (§2).
  - Prevalence of LLM writing therefore does not predict output effects.
  - The mathematics surge is better explained by AI doing research tasks whose results can be checked (§3d) than by AI polishing prose. This is my inference.
- **Field is confounded with language and venue.** Within biomedicine, the highest-prevalence groups are:
  - computational fields;
  - non-English-speaking countries;
  - fast-turnaround journals.

  Field differences in prevalence are therefore partly differences of language and venue, and partly detection lag in slow-publishing fields (Kobak's own caveat).

### Gaps
- **Liang et al. (2025): bioRxiv, physics and statistics.** Their values to September 2024 are not in the abstract, and the full text was paywalled. The preprint figure was read by eye and ends in February 2024. Check the NHB version's Fig. 1 before citing Liang et al. (2025) for a comparison of biology and physics.
- **Kobak's Fig. 5B: wet-lab fields.** Values for wet-lab fields (for example, cell or developmental biology) were not extracted. The text names only computational fields (≈0.20) and gives the overall range (below 5% to above 40%).
- **No breakdown by bioRxiv subject category or physics archive.** I found no study that breaks LLM prevalence down by bioRxiv subject category. None splits the arXiv physics archives in a way that separates theory from experiment.
- **Kusumegi et al. (2025, *Science*).** — [DOI](https://doi.org/10.1126/science.adw3000)
  - They cover arXiv, bioRxiv and SSRN, but their field-level results were not extracted.
  - The author has dropped their productivity claims after Renault et al. (2026, *PNAS*). — [DOI](https://doi.org/10.1073/pnas.2618638123)

---

## 2. How has research output grown by field since 2022?

### Takeaway
Measured cumulatively, biology is not less affected: bioRxiv's last four quarters exceed 2022 by 50%, more than arXiv physics (44%). What sets biology apart is that it shows no acceleration in 2026:
- **bioRxiv** has grown a steady 10–13% a year since 2023.
- **Other fields accelerated**, year on year in Q3 2026:
  - mathematics +78%;
  - CS +41%;
  - medicine +29%;
  - physics +26%.
- **An independent synthetic-control study** dates the mathematics break to 2026.
- **Journal data are thin.** Published data on journal submissions by field are almost absent, and Hanson et al. (2024) has no update for the AI era.

### Cited Findings
- **Companion analysis, Q3 2026.** — [companion README](../../paper/figures/README_companion_analysis.md) (`/home/user/academia-ia-state/paper/figures/README_companion_analysis.md`)

  | Field | Index (2022 = 100) | Last four quarters vs 2022 | Year on year |
  |---|---|---|---|
  | Physics | 162 | +44% | +26% |
  | Mathematics | 219 | +59% | +78% |
  | Biology (bioRxiv) | 157 | +50% | +10% |
  | Medicine excl. COVID-19 (medRxiv) | 289 | +139% | +29% |
  | Social sciences | 184 | +73% | +6% |
  | Computer science | 278 | +146% | +41% |

  - The source's own caveats: preprint adoption differs by field, so "compare trends within a field, not levels across fields"; and medicine's 2022 base is depressed.
- **CS outside AI research.** +47% year on year, per the companion analysis as given in this assignment. This figure is not in the README, and the draft flags it [RECHECK].
- **[OWN CALC] bioRxiv's own statistics,** retrieved 16 Oct 2026. — [bioRxiv API, yearly](https://api.biorxiv.org/sum/y); [monthly](https://api.biorxiv.org/sum/m)
  - **New papers per year:**

    | Year | New papers |
    |---|---|
    | 2018 | 20,778 |
    | 2019 | 29,179 |
    | 2020 | 38,717 |
    | 2021 | 36,866 |
    | 2022 | 35,750 |
    | 2023 | 39,155 |
    | 2024 | 43,632 |
    | 2025 | 49,318 |
    | 2026, Jan–Sep | 40,548 |

  - **Growth:**
    - 2019: +40%
    - 2023: +9.5%
    - 2024: +11.4%
    - 2025: +13.0%
    - Jan–Sep 2026: +11.7% (against 36,304 in Jan–Sep 2025)
    - Q3 2026: +9.9% (13,999 against 12,735)
  - **No break in 2026.**
    - The monthly record is May 2026 (5,165).
    - September 2026 had 5,049 papers, against 4,770 a year earlier (+5.8%).
  - **The 2022 base is a post-COVID dip.** 35,750 is below both 2020 (38,717) and 2021 (36,866).
  - **The companion index reproduces.** Q3 2026 divided by the 2022 quarterly mean (8,937.5) gives 1.57, the companion's 157.
- **[PREPRINT] Nee, X., Zhong, H. & Ni, X. (2026).** The Generative AI Gold Rush in Theoretical and Computational Research. arXiv:2609.04872v1 (4 Sep 2026). In the arXiv metadata the first author's given name is spelled "Xiaoshn". — [arXiv:2609.04872](https://arxiv.org/abs/2609.04872); [HTML](https://arxiv.org/html/2609.04872v1)
  - **Design.** 2,080 monthly observations for twenty arXiv archives, January 2018 – August 2026, with a regularised synthetic control fitted through December 2025.
  - **Mathematics against its counterfactuals.** 47,127 entries in January–August 2026:
    - 33.5% above 2025;
    - 11.9% above the synthetic counterfactual (42,113), and 9.6–14.9% above it across qualified designs;
    - "36.8% above continuation of its own pre-2022 trend".
  - **Timing.** The fitted annual gaps are −0.2% (2022), 0.7% (2023), 1.6% (2024) and −1.9% (2025), then 11.9% (2026). "The break is therefore concentrated in 2026 rather than spread across the years following public access to ChatGPT."
  - **Robustness and breadth.** Mathematics has the largest RMSPE ratio among fifteen eligible placebo archives, and 29 of its 30 math.* categories grew.
  - **Totals.** January–August, year on year: broad physics +16.5%; unique arXiv submissions +26.8%.
- **arXiv's own account (1 Oct 2026).** — [arXiv blog](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/)
  - 40,363 submissions in September 2026, against 20,569 in September 2024.
  - A cap of two submissions per month from 1 Oct 2026, as recorded in note 3.
- **Hanson, M. A., Gómez Barreiro, P., Crosetto, P. & Brockington, D. (2024).** The strain on scientific publishing. *QSS* 5(4):823–843. — [DOI](https://doi.org/10.1162/qss_a_00327)
  - Indexed articles grew about 47% over 2016–2022.
  - A targeted search on 16 Oct 2026 found no update for 2025–26.
- **Journal submissions in one field (management).** Gartenberg, C., Hasan, S., Murray, A. & Pierce, L. (2026). More versus better: artificial intelligence, incentives, and the emerging crisis in peer review. *Organization Science* 37(3):795–812. — [DOI](https://doi.org/10.1287/orsc.2026.ed.v37.n3)
  - "Submission volume has risen 42% since the late 2022 release of ChatGPT … The rise in AI-generated writing accounts for nearly all of these trends".
  - The quotation was verified in the citation audit; I checked the DOI here.
- **What bioRxiv accepts.** bioRxiv is "NOT intended for … Narrative reviews … Editorials, letters, opinion pieces … White papers or policy statements". This wording is as verified in the citation audit (R71). — [bioRxiv FAQ](https://www.biorxiv.org/about/FAQ)

### Inferences
- **"Less affected" holds for one reading only.**
  - **Cumulative growth since 2022:** no. Biology grew 50%, against physics 44% and mathematics 59%.
  - **The 2026 acceleration:** yes. bioRxiv shows no break, while mathematics, CS, physics and medRxiv accelerate.
  - The essay should claim only the second.
- **Two confounds make bioRxiv look stable.**
  - **Preprint uptake.**
    - bioRxiv grew 40% in 2019, before generative AI, as biologists adopted preprints. Part of its growth in 2023–26 may still be uptake rather than output.
    - Its 2022 base is also a post-COVID dip.
    - arXiv physics and mathematics have mature preprint cultures.
    - Year-on-year growth in 2026 is therefore a cleaner contrast than growth since 2022.
  - **Genre.**
    - bioRxiv excludes reviews, letters and opinion pieces, the genres AI makes cheapest, so its counts track primary research.
    - That is the right series for testing the experimental bottleneck.
    - It understates AI's effect on biology's literature as a whole (see the letters in §5).
- **Slow growth is not unique to experimental fields.** The social sciences grew only 6% year on year.
  - Server policies and norms matter: SocArXiv bans AI-written paragraphs, per `paper/brief.md`. So does the small sample.
  - A cross-field comparison of preprint growth is therefore not a clean test of the bottleneck mechanism.
- **Physics' +26% comes mostly from theory-heavy archives** (§4).

### Gaps
- **No journal-submission data by field.** I found no published data on journal submissions by field for biology or physics.
  - A claim of a 33% rise in journal submissions in Q1 2026 was seen only in search results (academicjobs.com, a trade site). It has no identifiable primary source and should not be used.
- **Journal output by field, 2023–2026.** This was not compiled. OpenAlex or Dimensions could supply it.
- **Moderation changes.** I found nothing on whether bioRxiv or medRxiv changed their moderation in 2025–26, for example by declining formulaic or AI-generated submissions. Such a change would depress their counts.
- **Hanson et al.'s field breakdown.** I did not check whether they break growth down by field.

---

## 3. Mechanisms: why would experimental fields be less affected?

### Takeaway
**The best-supported account.** Generative AI cheapens the steps that need only text, code and existing data, and whose results can be checked cheaply. Experiments cost what they always cost.

**Three strands of evidence support it:**
- **Blekhman's bottleneck argument.** It is opinion, but it is concrete and includes an Amdahl's-law illustration.
- **Hao et al.'s finding that data availability "appears to be a major impacting factor".** This concerns AI used as a research method, mostly before ChatGPT.
- **The pattern of AI-for-science successes.** They come where data are abundant and verification is objective:
  - AlphaFold, trained on about 100,000 experimental structures and judged in a blind assessment;
  - Lean-checked mathematics.

**Two further points:**
- **Earlier adoption does not predict the surge.** Uptake of AI as a method before 2022 was slower in mathematics than in biology, medicine or physics, the reverse of the 2026 output surge.
- **Lab automation is not yet proof.** It could loosen the bottleneck, but the 2026 evidence is a company demonstration on a narrow optimisation task.

### Cited Findings

**(a) The experimental bottleneck**
- **Blekhman, R. (2026).** What is biology research for? *PLOS Biology* 24(10):e3004075 (15 Oct 2026). Verbatim from the publisher PDF: — [DOI](https://doi.org/10.1371/journal.pbio.3004075)
  - **The objection he answers:** biology's surge is "smaller than in fields such as machine learning or mathematics".
  - **His answer:** "This is partly true, because AI has not yet substantially increased productivity in biology, where the bottlenecks are structural and experimental rather than computational [7]. The surge is nevertheless just beginning. Computational biology already sees it, because AI can fabricate a computational paper end to end."
  - **On brakes:** "in biology research, there are no brakes on the system".
- **[BLOG] Blekhman, R. (26 Jul 2026).** Why AI will not speed up science (yet). Ran's Substack; Blekhman's ref. 7. — [Substack](https://blekhman.substack.com/p/why-ai-will-not-speed-up-science)
  - **[TOOL] The argument.** It follows Solow's productivity paradox: the reasons are "structural, and they have little to do with how good the AI is".
  - **[TOOL] The bottlenecks he names:**
    - **At the bench:** cell culture; sample collection and shipping; sequencing queues; mouse breeding and ageing; failed experiments that must be repeated; reagent and instrument lead times; waiting lists for core facilities.
    - **Institutional:** 12–18 months from grant submission to award; IRB, IACUC and biosafety approvals; material-transfer and data-use agreements.
    - **People:** hiring and visas.
    - **Publication:** peer review.
  - **[TOOL] Amdahl's law.** If literature review and hypothesis generation are 5% of a project's timeline, a 100-fold speed-up there cuts total duration by less than 5%.
  - **[TOOL] A footnote:** AI "lowers the cost of producing papers without lowering the cost of producing knowledge".
- **AlphaFold's own abstract states the experimental bottleneck.** "Through an enormous experimental effort, the structures of around 100,000 unique proteins have been determined … Structural coverage is bottlenecked by the months to years of painstaking effort required to determine a single protein structure." — Jumper, J. et al. (2021). *Nature* 596(7873):583–589. [DOI](https://doi.org/10.1038/s41586-021-03819-2); [Europe PMC](https://europepmc.org/article/PMC/PMC8371605)

**(b) Data availability**
- **Hao, Q., Xu, F., Li, Y. & Evans, J. A. (2026).** *Nature* 649(8099):1237–1243. Verbatim from the author version (arXiv v4):
  > "factors like inherent topicality, original impact, and funding priority, remain almost unrelated to the disproportionate AI adoption (Supplementary Fig. S22-S24). In contrast, data availability appears to be a major impacting factor, where areas with an abundance of data are increasingly and disproportionately amenable to AI research, contributing to the observed concentration within knowledge space (Supplementary Fig. S25)."

  — [DOI](https://doi.org/10.1038/s41586-025-09922-y); [arXiv v4](https://arxiv.org/html/2412.07727v4)
- **Hao et al.: scope and growth by field** (verbatim from v4). — [arXiv v4](https://arxiv.org/html/2412.07727v4)
  - **Scope:** AI used as a research method, in 41.3M papers on biology, chemistry, geology, materials science, medicine and physics. CS and mathematics are excluded (note 3).
  - **Growth by field, 1980–2025:**
    - **Papers:** the share of AI-augmented papers "surged by 10.70 (geology …) to 51.89 (biology …) times from 1980 to 2025".
    - **Researchers:** the share adopting AI rose from 135.46 times (geology) to 362.16 times (physics).
  - **The generative-AI era:**
    - Growth rates "initially remain consistent with prior trends. A period of time later, however, these growth rates begin to exhibit marked acceleration across disciplines … the mass adoption of generative AI in natural science research requires time".
    - The main text calls this era's results "a preliminary consistency with prior periods".

**(c) AI adoption by field (AI used as a research method)**
- **Gao, J. & Wang, D. (2024).** Quantifying the use and potential benefits of artificial intelligence in scientific research. *Nature Human Behaviour* 8(12):2281–2292. — [DOI](https://doi.org/10.1038/s41562-024-02020-5)
  - The details below come from the preprint version, arXiv:2304.10578v2 [PREPRINT], and may differ from the final text. — [arXiv](https://arxiv.org/abs/2304.10578)
  - **Data:** 74.6M publications and 7.1M patents.
  - **Spread of AI use:**
    - The rise occurs "not only in computer science but also in a wide range of other disciplines …, including, for example, physics, biology, and economics", with "a notably sharp increase in the use of AI since 2015".
    - In CS, the direct AI impact score rose from 0.5% (2000) to 1.3% (2019).
  - **Potential within biology:** the subfield with the largest potential AI impact is "biological system", ranked seventh among fields outside CS; it "happens to be the field for the AlphaFold paper".
  - **Medicine:** "the medicine discipline as a whole is not ranked among the highest in terms of AI benefits, but some of its subfields (e.g., 'nuclear medicine,' 'optometry,' and 'medical physics') show substantial AI benefits".
  - **Skills gap:** "a notable disconnect exists between AI education and its research applications".
- **[PREPRINT] Duede, E., Dolan, W., Bauer, A., Foster, I. & Lakhani, K. (2024).** Oil & water? Diffusion of AI within and across scientific fields. arXiv:2405.15828. — [arXiv](https://arxiv.org/abs/2405.15828)
  - **Scope:** about 80M papers in 20 fields, 1985–2022. AI-engaged publications grew about 13-fold, and "In 2022, nearly 9% of all papers … were identified as AI-engaged".
  - **[TOOL] Growth by field.** Percentage change in the AI-engaged share, 1985–2022, read from the PDF text layer of the Fig. 2 insets (check the mapping against the figure):

    | Field | Change |
    |---|---|
    | Biology | +1,109% |
    | Medicine | +1,389% |
    | Physics | +1,142% |
    | Computer science | +760% |
    | Mathematics | +422% |

- **Bianchini, S., Müller, M. & Pelletier, P. (2022).** *Research Policy* 51(10):104604. Deep learning (DL) is an emerging "general method of invention". — [DOI](https://doi.org/10.1016/j.respol.2022.104604)
  - **The 2020 preprint [PREPRINT]** finds "a transition from interdisciplinary DL applications to disciplinary research within application domains".
  - In the health sciences, "DL adoption is negatively correlated with re-combinatorial novelty".
  - — [arXiv:2009.01575](https://arxiv.org/abs/2009.01575)

**(d) Verification-friendly domains**
- **AlphaFold.** Validated "in the challenging 14th Critical Assessment of protein Structure Prediction (CASP14)", a blind assessment, "demonstrating accuracy competitive with experimental structures in a majority of cases". — [DOI](https://doi.org/10.1038/s41586-021-03819-2)
- **Formal mathematics: [PREPRINT] Sothanaphan, N. (2026).** Resolution of Erdős Problem #728: a writeup of Aristotle's Lean proof. arXiv:2601.07421 (v1 12 Jan 2026; v5 26 Jan 2026). — [arXiv:2601.07421](https://arxiv.org/abs/2601.07421)
  - **The claim:** this is "the first Erdős problem … regarded as fully resolved autonomously by an AI system".
  - **The system:** "a combination of GPT-5.2 Pro by OpenAI and Aristotle by Harmonic, operated by Kevin Barreto. The final result of the system is a formal proof written in Lean".
- **[PREPRINT] Tao, T. (2026).** Mathematics in the age of AI. arXiv:2608.16753v1 (17 Aug 2026). An essay based on Tao's public lecture at ICM 2026, submitted to the ICM proceedings. — [arXiv:2608.16753](https://arxiv.org/abs/2608.16753)
  - **What it does:** it conditions "on the hypothesis that these capabilities will arrive" and asks "what the goals and values of mathematical research actually are".
  - **What it lacks:** the abstract contains no data.
- **[PREPRINT] Nee et al. (2026)** (verbatim). — [arXiv:2609.04872](https://arxiv.org/abs/2609.04872)
  - "A capability threshold denotes the point at which model performance and available checks make a research task reliable enough for routine workflow adoption."
  - The 2026 timing "is consistent with delayed diffusion and capability threshold mechanisms".
  - "The findings locate verification, selection, and attention as central constraints for research governance".
- **Companion data on arXiv mathematics**, January 2025 → September 2026. — [companion README](../../paper/figures/README_companion_analysis.md)
  - Papers mentioning Erdős rose from 26 to 101 a month.
  - Papers mentioning an AI tool rose from 0.09% to 1.97%.
  - In Q3 2026, Lean was mentioned in 1.6% of papers with a prolific author, against 1.0% of the rest.

**(e) Lab automation and self-driving labs**
- **[NEWS; COMPANY] OpenAI and Ginkgo Bioworks** (*Scientific American*, 13 Mar 2026). — [Scientific American](https://www.scientificamerican.com/article/openai-and-ginkgo-bioworks-show-how-ai-can-accelerate-scientific-discovery/)
  - **The set-up:** GPT-5 designed and analysed experiments to optimise cell-free protein synthesis, and Ginkgo's robotic cloud lab ran them.
  - **Scale and result:** "more than 36,000" unique reaction compositions over about two months, cutting the cost of protein production by about 40% against a published benchmark.
  - **The human role:** humans set the objective, and technicians changed an invalid design (a negative volume).
  - **Status:** the report is a PDF on OpenAI's site, with no DOI and no peer review, and its authors are affiliated with the companies.
  - **On verification,** Jiao, on the task: "it's hard to generate a solution, and it's also really hard to verify."
- **Tom, G. et al. (2024).** Self-driving laboratories for chemistry and materials science. *Chemical Reviews* 124:9633–9732. A review, cited by title only as evidence that the field is established in chemistry and materials science. — [DOI](https://doi.org/10.1021/acs.chemrev.4c00055)
- **[BLOG] Blekhman's Substack, [TOOL]: the "Capable" lab.** — [Substack](https://blekhman.substack.com/p/why-ai-will-not-speed-up-science)
  - It goes from AI drug design to data in 24 hours, but only one of its six modules is AI.
  - The speed came from an in-house in vivo facility, pre-approved protocols and automation.

### Inferences
- **The evidence supports a specific mechanism.** It is not "experimental fields resist AI". It is that AI raises output where a field's core product can be made from text, code and existing data, and checked cheaply:
  - **Qualifies:** mathematics (proofs checkable in Lean), CS, theory archives, and open-data epidemiology (§5).
  - **Does not qualify:** wet-lab biology, where each result needs a new, slow, physical experiment.
- **Data availability and verification are related but distinct.**
  - **AlphaFold needed both:** about 100,000 experimental structures and the blind CASP test.
  - **Hao et al.** measured only data availability, and only for AI used as a method.
  - **The 2026 mathematics surge fits verification better.** Mathematics has little "data" in Hao's sense, but its outputs can be checked.
  - **For the draft:** its phrase in §5, "well-posed problems with abundant data", could add "and checkable results".
- **Earlier adoption of AI as a method does not predict generative AI's output effects.**
  - **Before 2022:** in Duede's data, mathematics' growth in AI as a method (+422%) was among the lowest. Biology and medicine grew fast; in Hao's data, biology grew fastest, at 51.89-fold.
  - **The 2026 output surge is the reverse:** mathematics first, biology barely.
  - **Consequence:** arguments from "AI adoption by field" must keep AI as a method separate from generative AI as a means of production.
- **Lab automation is a possible future change, not current evidence.**
  - **The documented case is narrow:** an optimisation with a fast optical readout (GFP fluorescence).
  - **Most of Blekhman's bottlenecks remain:** animals, patients, approvals and slow phenotypes.
  - **The first niches to change** would be those with fast assays: protein engineering, synthetic biology and high-throughput screening. This is my inference.

### Gaps
- **Blekhman's Substack wording** was extracted by a fetch tool. Re-check any quotation against the post before using it.
- **Hao et al.'s measure of data availability** (Supplementary Fig. S25) was not seen, so how it was operationalised is unknown.
- **Field rankings.**
  - Gao & Wang's rankings were not extracted as numbers, and the final NHB version was not read.
  - Duede et al.'s per-field values were read from a PDF text layer.
- **AlphaProof and other olympiad-level results** were not verified here.
- **No study of automation and biological output.** I found no study measuring how much lab automation has raised biological output. Industry announcements are not evidence of change across a field:
  - Ginkgo's cloud lab;
  - NPR's coverage of AI-run labs (May 2026), seen only in search results.

---

## 4. Within-field contrasts: computational vs wet-lab biology, and theory vs experiment in physics

### Takeaway
There is published evidence, but it is thin. It points the same way in both fields.
- **Biomedicine, writing.** The prevalence of LLM writing is highest in computational fields: Δ≈0.20, against an overall lower bound of 13.5%.
- **Biomedicine, output.** I found no published output data by bioRxiv subject category.
- **Physics, output.** In January–August 2026, theory-heavy arXiv archives grew 20–31% (math-ph, quant-ph, hep-th), against 2.6% for nuclear experiment.
  - The source gives no figures for hep-ex or nucl-th, and it does not test the contrast.
  - An informal blog count shows hep-th up only about 13% in early 2026.
- **The companion analysis is needed to settle both contrasts.**

### Cited Findings

**Computational vs wet-lab biology**
- **Kobak et al. (2025).** — [DOI](https://doi.org/10.1126/sciadv.adt3813)
  - "Computational fields like computation and bioinformatics showed Δ ≈ 0.20", against at least 13.5% overall; "computation papers from China" reached 0.41.
  - Their caveat: faster publication in computational journals means uptake is detected there earlier.
- **[PREPRINT] Lin & Zhu (2025).** — [arXiv:2504.13629](https://arxiv.org/abs/2504.13629)
  - arXiv quantitative biology (11%) is level with physics (10%) and economics (11%), and well below CS (22%).
  - Biology, CS and EESS were the most likely to use GPT for comprehensive revisions rather than grammar.
- **Blekhman (2026).** "Computational biology already sees it, because AI can fabricate a computational paper end to end." This is an assertion; the piece gives no data. — [DOI](https://doi.org/10.1371/journal.pbio.3004075)
- **Gao & Wang (2024).** Within biology, the subfield with the largest potential AI impact is "biological system", AlphaFold's subfield. — [DOI](https://doi.org/10.1038/s41562-024-02020-5); [arXiv](https://arxiv.org/abs/2304.10578)

**Theory vs experiment in physics**
- **[PREPRINT] Nee et al. (2026),** verbatim. — [arXiv HTML](https://arxiv.org/html/2609.04872v1)
  > "Growth within physics is heterogeneous. The largest absolute 2026 increases occur in quantum physics (+3,026; +30.2%), condensed matter (+2,470; +15.8%), astronomy and astrophysics (+2,014; +14.7%), the general physics archive (+1,839; +11.1%), high energy theory (+1,030; +20.3%), and mathematical physics (+1,019; +31.1%). Nuclear experiment entries rise 2.6%, while electrical engineering and systems decline 8.6% outside the physics sum."
  - **What is missing:** no figures are given for hep-ex, hep-ph, hep-lat, nucl-th or gr-qc.
  - **No conclusion drawn:** the authors draw no conclusion about theory and experiment. They write only that "This heterogeneity motivates archive level weights".
- **[BLOG] Woit, P. (24 Feb 2026).** "Looks Like it is Happening…", *Not Even Wrong*. — [blog](https://www.math.columbia.edu/~woit/wordpress/?p=15500)
  - **New hep-th submissions by original submission date:**

    | Period | 2022 | 2023 | 2024 | 2025 | 2026 |
    |---|---|---|---|---|---|
    | January | 510 | 490 | 501 | 544 | 617 |
    | 1–15 February | 255 | 221 | 280 | 276 | 311 |

  - **Correction:** an earlier tally by last-modified date had suggested a near doubling.
  - **His conclusion:** "The hep-th arxiv apocalypse is not here yet."
  - **No comparison:** he makes no comparison with hep-ex.
- **[PREPRINT] Geng & Trotta (2024).** — [arXiv:2404.08627](https://arxiv.org/abs/2404.08627)
  - LLM-style text in astro-ph and cond-mat, both mixes of theory and observation, sits at 10–20%, against about 35% in cs.
  - There is no split into theory and experiment.

### Inferences
- **The one published comparison of physics archives fits the bottleneck account, but only weakly.**
  - **What it shows:** theory-heavy archives grew faster in 2026 than nuclear experiment did.
  - **Its limits:** it is a single experimental archive in one preprint, the contrast is not tested, and hep-ex and nucl-th are missing.
  - **Consequence:** the essay can say at most "early figures suggest".
- **The two hep-th figures do not conflict.** Woit's January–February counts (+13%) and Nee's January–August figure (+20.3%) are consistent with growth accelerating through 2026.
- **Design notes for the companion contrasts** (my suggestions):
  - **Physics:** hep-th against hep-ex, nucl-th against nucl-ex, and possibly gr-qc against astro-ph.
    - **hep-ex** output is gated by large collaborations' internal review and data-taking cycles. Slow growth there would reflect collaboration procedure as well as experiment.
    - **astro-ph** is observational but rich in public survey data, so it tests data availability rather than theory against experiment.
  - **Biology:** bioRxiv bioinformatics, genomics and systems biology against cell, developmental and molecular biology, with neuroscience treated as mixed.
  - **A second contrast:** arXiv q-bio against bioRxiv, computational against experimental.
  - **Pre-specification:** fix the category lists and the 2026 year-on-year window before looking at the data. The Registered Report option in `paper/brief.md` requires no prior access to the data.
  - **A clean result** would show computational categories accelerating in 2026 while wet-lab categories do not. Faster growth that began before 2022 would not count.

### Gaps
- **No published bioRxiv subject-category study.** I found no study of output growth by bioRxiv subject category.
- **No published theory-vs-experiment comparison in physics.** I found no comparison of hep-th with hep-ex, or of nucl-th with nucl-ex. Nee et al. report only nucl-ex among the experimental archives.
- **Category data not tested.** I did not test whether bioRxiv's summary endpoint can be split by category; it reported "category: all". Counts by category probably need per-record metadata.

---

## 5. Counter-evidence and nuance

### Takeaway
"Biomedicine is less affected" is wrong as a blanket statement.
- **Where no new experiment is needed, output has surged:**
  - formulaic analyses of open health datasets: nine heavily mined datasets reached 3.0× their 2022 output by 2025;
  - redundant NHANES papers: 17-fold between 2022 and 2024;
  - letters to the editor: anomalous growth since 2023 among newly prolific authors.
- **medRxiv grew 29% year on year,** faster than physics.
- **What this means:** these surges support the mechanism (cheap inputs make cheap papers) but undercut the blanket claim about fields.
- **Lower adoption or later onset?** The evidence favours a later onset, or a different bottleneck:
  - biologists already write with AI as much as physicists do;
  - mathematics' own break came three years after ChatGPT;
  - the authors of the biomedical prevalence studies expect their estimates to rise.

### Cited Findings

**Medicine and open health datasets**
- **Companion analysis: medRxiv, excluding COVID-19.** — [companion README](../../paper/figures/README_companion_analysis.md)
  - The index stands at 289; the last four quarters are 139% above 2022, and growth is 29% year on year.
  - COVID-19 papers were 66% of 2020 papers and 5% of 2026 papers.
- **Suchak, T. et al. (2025).** *PLOS Biology* 23(5):e3003152. — [DOI](https://doi.org/10.1371/journal.pbio.3003152); [Europe PMC](https://europepmc.org/article/MED/40338847)
  - **Scale:** 341 single-factor NHANES papers.
  - **Growth:** the search "identified an average of 4 papers per annum from 2014 to 2021, but 190 in 2024-9 October alone".
  - **Drivers named:** the abstract points to "AI-ready datasets" and to paper mills using "AI-assisted workflows".
- **Spick, M., Onoja, A., Harrison, C., Stender, S., Byrne, J. & Geifman, N. (2026).** Quantifying new threats to health and biomedical literature integrity from rapidly scaled publications and problematic research. *J Clin Epidemiol* 193:112203. Online 23 Feb 2026; the medRxiv preprint is from July 2025. — [DOI](https://doi.org/10.1016/j.jclinepi.2026.112203); [Europe PMC](https://europepmc.org/article/MED/41740900); [preprint DOI](https://doi.org/10.1101/2025.07.07.25331008)
  - **Selection:** "Across 36 datasets, we identify nine showing hallmarks of paper mill exploitation". They are FAERS, NHANES, UK Biobank, FinnGen, the Global Burden of Disease Study, MIMIC, CHARLS, CDC WONDER and TriNetX.
  - **Scale:** in 2025 they had "a combined publication count of 23,005 indexed in the OpenAlex database … an excess of 11,577 publications above the AutoRegressive Integrated Moving Average forecast trend, and … a 3.0×-fold change on the 7655 publication count for these nine datasets in 2022".
  - **Geography:** the fold change was 4.2× for China, against 1.9× for the rest of the world.
  - **Publishers' response:** "publishers are responding by discouraging submissions employing open-access health datasets".
- **Maupin, D., Suchak, T., Barnett, A. & Spick, M. (2025).** Dramatic increases in redundant publications in the Generative AI era. *BMC Medicine* 24:29. Online 9 Dec 2025. — [DOI](https://doi.org/10.1186/s12916-025-04569-y); [Europe PMC](https://europepmc.org/article/MED/41361882)
  - **Scale:** 411 redundant NHANES publications across 156 exposure–outcome pairs, 2021 to July 2025.
  - **Example:** the association between oxidative balance score and chronic kidney disease "was published six times in 1 year".
  - **Growth:** "a 17-fold increase between 2022 and 2024".
  - **Evasion:** synthetic manuscripts written by LLMs evaded a plagiarism checker, with overall similarity scores of 26%, 19% and 14%.
- **[PREPRINT] Maupin, D. et al. (2026).** Drastic changes in collaboration networks and publication patterns in research using the CDC WONDER dataset. medRxiv, 15 Jan 2026. — [DOI](https://doi.org/10.64898/2026.01.13.26343992)
  - **Growth:** "The number of publications using CDC WONDER grew from 88 in 2021 to 1223 in 2025."
  - **Authorship:** the share with an author from Pakistan rose from 0.5% to 27.2%.
  - **Template:** the papers show "formulaic titles and identical methods".
- **[NEWS] Naddaf, M. (15 Jul 2025).** Low-quality papers based on public health data are flooding the scientific literature. *Nature*. — [DOI](https://doi.org/10.1038/d41586-025-02241-2)

**Outputs that are text only: letters to the editor in biomedicine**
- **Cancellario, T., Arrondo, G., Carrión-Nessi, F. S., De Haro, I., García-Manglano, J., Abbritti, M., Rudd, M. & Chaccour, C. (2026).** Robot pen pals: a systematic analysis of recent trends in scientific correspondence. *Research Integrity and Peer Review*, published 6 Oct 2026. Abstract read via Crossref. — [DOI](https://doi.org/10.1186/s41073-026-00259-2)
  - **Data:** more than 780,000 PubMed records of letters to the editor (LTEs), 2005–2025.
  - **Growth:** accelerated growth in 2013 (MEDLINE indexing changes), in 2020 (COVID-19) and in "2023 to date, aligning with the widespread adoption of generative AI".
  - **Authors:** "the post-LLM period is marked by an increase in the prevalence of high-output authors, with newly debuting researchers more likely to produce multiple LTEs in their first year".
  - **Why letters:** their "textual format … makes LTEs particularly easy to generate using large language models".
- **[PREPRINT] The earlier version:** Chaccour, C. et al., Research Square, 3 Nov 2025. — [DOI](https://doi.org/10.21203/rs.3.rs-7992675/v1)
  - One author went from zero letters in 2024 to "more than 80 in 2025".
  - A small group's output "went from the bottom 5% in the period 2005–2022 to the top 5% in 2023–2025".

**Computational biology already affected**
- **Writing:** the prevalence of LLM writing is higher in computational fields (Kobak; see §4). — [Kobak DOI](https://doi.org/10.1126/sciadv.adt3813)
- **Output:** Blekhman asserts that the surge is already under way there. — [Blekhman DOI](https://doi.org/10.1371/journal.pbio.3004075)

**Lower adoption or later onset?**
- **Adoption in writing is not low in biology.** See §1: Lin & Zhu; Liang's preprint figure; Holzwarth et al., who estimate 77% of 2025 PMC papers.
- **Detection lag.** Kobak et al.: "We expect the lower bounds documented here to increase with these longer observation windows." — [DOI](https://doi.org/10.1126/sciadv.adt3813)
- **Late, abrupt breaks happen.** The mathematics break is "concentrated in 2026 rather than spread across the years following public access to ChatGPT … consistent with delayed diffusion and capability threshold mechanisms" (Nee et al., [PREPRINT]). — [arXiv:2609.04872](https://arxiv.org/abs/2609.04872)
- **AI used as a method:** growth rates "initially remain consistent with prior trends" before a "marked acceleration across disciplines … the mass adoption of generative AI in natural science research requires time" (Hao et al., v4). — [arXiv v4](https://arxiv.org/html/2412.07727v4)
- **Blekhman:** "AI has not yet substantially increased productivity in biology"; "The surge is nevertheless just beginning". — [DOI](https://doi.org/10.1371/journal.pbio.3004075)
- **bioRxiv shows no break through September 2026** (§2). — [bioRxiv API](https://api.biorxiv.org/sum/m)

### Inferences
- **Medicine tests the data-availability mechanism within biomedicine, and the mechanism passes.** Output surges in two places:
  - where the data come ready-made (open datasets support formulaic analyses that need no new data collection);
  - where the product is pure text (letters).
- **What this means for medRxiv.** Its fast growth does not contradict the bottleneck account; it supports it. It does rule out the blanket phrasing "biomedicine is less affected".
- **The driver of medRxiv's growth is untested.** That open-dataset papers drive it is a hypothesis, not a finding. The companion could test it by tracking the share of medRxiv preprints that name the nine datasets.
- **The evidence points to a different binding constraint, possibly with later onset, not to lower adoption.**
  - "Lower adoption" is not supported for writing: biologists already use AI for prose.
  - Their counted output is bound by experiments, whose cost AI has not yet cut.
  - Mathematics shows that output can break late and abruptly once the tools cross a field's capability threshold.
  - In experimental biology the equivalent threshold is physical (automation), not only a matter of model capability.
- **Any wording needs "so far".** It is the honest qualifier.

### Gaps
- **Letters: the published figures were not readable.** The quantitative results of the published letters paper could not be read, because the publisher page redirected to a login. These include, for example, the shares of authors and of letters from "prolific debutantes".
  - The press figures (3% of authors, 22% of letters) were seen only in search summaries and are not verified.
- **No breakdown of medRxiv growth by content type.** Open-dataset analyses, systematic reviews and clinical studies were not separated.
- **Server screening not verified.** I did not verify whether bioRxiv or medRxiv decline formulaic or AI-generated submissions, which would mute their counts.

---

## 6. Synthesis: what the essay can say

### Takeaway
The author's intuition holds in two senses, not in general:
- **for output, not for writing;**
- **for experimental work, not for biology or biomedicine as a whole.**

The gaps for each point are listed in §§1–5.

### Cited Findings
All of the evidence below is cited in full in §§1–5.
- **Writing prevalence: biology is at or above physics.**
  - Lin & Zhu [PREPRINT];
  - Liang's preprint figure [FIG];
  - Kobak;
  - Holzwarth [PREPRINT].
- **Output:**
  - **Since 2022:** bioRxiv +50% vs physics +44%, comparing the last four quarters with 2022 (companion analysis).
  - **2026, year on year:** bioRxiv +10%, with steady growth of 10–13% a year since 2023 (bioRxiv API). Mathematics +78%, CS +41%, medRxiv +29% and physics +26% (companion analysis).
  - **The mathematics break** is dated to 2026 by synthetic control (Nee [PREPRINT]).
- **Mechanism:**
  - Blekhman's bottleneck argument;
  - Hao et al.'s "a major impacting factor" for data availability;
  - AlphaFold's ~100,000 experimental structures and the CASP blind test;
  - a Lean-checked Erdős proof (Sothanaphan [PREPRINT]).
- **Within fields:**
  - computational biomedicine leads in LLM writing (Kobak);
  - theory archives outgrew nuclear experiment in 2026 (Nee [PREPRINT]).
- **Within biomedicine:**
  - publications on nine heavily mined open datasets rose 3.0× (Spick);
  - redundant NHANES papers rose 17-fold (Maupin);
  - letters to the editor surged from 2023 (Cancellario).

### Inferences

#### What the essay can say (about 150 words)

> Generative AI has reached biology's writing as much as other fields', but not yet its output. By word-frequency measures, LLM-edited prose was about as common in biology preprints as in physics ones by 2024 (Lin & Zhu 2025, preprint), and most biomedical papers published in 2025 show signs of it (Holzwarth et al. 2026, preprint). Output differs. In the third quarter of 2026, new preprints grew year on year by 78% in mathematics, 41% in computer science and 26% in physics, but by 10% on bioRxiv, which has grown 10–13% a year since 2023 with no break. That is consistent with Blekhman's (2026) view that biology's bottlenecks are experimental: AI cheapens writing and analysis, not experiments. Where no new experiment is needed, biomedical output has surged: publications based on nine heavily mined open health datasets tripled between 2022 and 2025 (Spick et al. 2026). Experimental biology is less affected so far, which may mean a later onset rather than immunity.

**Notes on the paragraph:**
- **Citing Liang et al. (2025).** Add it to the second sentence only after checking the NHB version's Fig. 1. I could read only the April 2024 preprint figure, where bioRxiv is about 8.5% and physics about 6.5% in February 2024.
- **The 10–13% figure** is my own calculation from bioRxiv's content statistics (api.biorxiv.org, accessed 16 Oct 2026). The essay should cite that source or have the companion analysis report it.
- **"Nine heavily mined" is deliberate.** Spick et al. selected those nine datasets from 36 because they departed from trend, so "open health datasets tripled" would overgeneralise.
- **To include the physics point, add one clause:** "and within physics, theory archives grew faster than nuclear experiment (Nee et al. 2026, preprint)". Word it as "early figures suggest".

#### Draft sentences this supports or contradicts

1. **`paper/draft_full.md` ¶2.1 (line 95):** "That layer is the whole of a grant application, a review or a review article, but only part of an experimental paper, whose cost lies mostly in the experiments."
   - **Verdict: supported.**
   - **Evidence:**
     - bioRxiv grows steadily while arXiv accelerates (§2);
     - text-only letters surged in PubMed (Cancellario et al. 2026);
     - Blekhman 2026.
   - **Suggestion:** this sentence is the essay's natural hook for the field contrast. ¶2.8 could refer back to it.
2. **¶2.1:** "Use is broad: at least 13.5% of 2024 PubMed abstracts show signs of processing by large language models (LLMs), up to about 40% in some subgroups (Kobak et al. 2025), as do up to 22% of sentences in computer-science abstracts (Liang et al. 2025)."
   - **Verdict: supported.**
   - **Caveat:** the two numbers use different measures (a lower bound on abstracts, against a share of sentences), so do not let readers infer that biomedicine is lower than CS.
   - **Optional update:** "most 2025 PMC papers" (Holzwarth et al. 2026, preprint).
3. **¶2.8 (line 113):** "new preprints in the four quarters to September 2026 exceeded 2022 levels in every field examined, by 44% in physics, 50% in biology, 59% in mathematics and 146% in computer science (Figure 3); year on year, biology grew by 10% and mathematics by 78%, consistent with Blekhman's (2026) point that biology's bottlenecks are experimental."
   - **Verdict: supported as worded ("consistent with"), but the first clause undercuts the second.** Biology's cumulative growth exceeds physics', so the contrast lies only in 2026.
   - **Suggested addition:** "Biology's preprints have grown steadily, by 10–13% a year since 2023, with no break in 2026, although biologists' prose is as LLM-edited as physicists' (Lin & Zhu 2025, preprint); the difference lies in what AI can produce, not in who uses it."
   - **Also note** that bioRxiv's 2022 base (35,750) sits below its 2020 peak (38,717).
4. **¶2.8:** "an independent estimate that arXiv mathematics is running above its counterfactual trend (Nee et al. 2026 [RECHECK: arXiv abstract only; not audited])"
   - **Verdict: verified.**
   - **Evidence:** 11.9% above the synthetic counterfactual for January–August 2026 (9.6–14.9% across designs).
   - **Complete the reference (line 445):** Nee, X., Zhong, H. & Ni, X. (2026). The Generative AI Gold Rush in Theoretical and Computational Research. arXiv:2609.04872 (v1, 4 Sep 2026). Preprint.
5. **¶2.8:** "see also Tao 2026 [RECHECK: arXiv record not verified; cited via Blekhman 2026]"
   - **Verdict: the record is verified; the use is weak.**
   - **Record:** arXiv:2608.16753v1, 17 Aug 2026. An essay from Tao's ICM 2026 lecture, submitted to the ICM proceedings.
   - **Why the use is weak:** the abstract contains no output data. It "condition[s] on the hypothesis that these capabilities will arrive". Cite Tao for what mathematical research is for, not as evidence of the surge.
   - **Update the reference (line 480):** remove [RECHECK].
6. **¶2.9 (line 118):** "Single-factor association studies built on the US NHANES health survey rose from about four a year in 2014–21 to 190 in 2024".
   - **Verdict: supported, but make it precise.** The source says "190 in 2024-9 October alone", so write "to 190 in 2024 (to 9 October)".
   - **Could be strengthened with:**
     - Spick et al. 2026: nine heavily mined datasets at 3.0× their 2022 output in 2025, with 11,577 publications above the forecast trend;
     - Maupin et al. 2025: redundant NHANES papers rose 17-fold between 2022 and 2024.
7. **¶2.9:** "The template needs no fraud, only a public dataset and a language model, and where the data come ready-made the whole paper becomes cheap."
   - **Verdict: supported** (Spick; Maupin; Suchak; Hao et al.'s finding on data availability).
   - **Suggestion:** this is the biomedical version of the field argument. Link it to ¶2.8, so that medicine's +29% reads as support for the mechanism and not as an anomaly.
8. **¶4b.2 (line 164):** "In Hao et al.'s supplementary analyses, data availability 'appears to be a major impacting factor' in where AI concentrates, while topicality, original impact and funding priority 'remain almost unrelated' to it; incentives were not measured."
   - **Verdict: supported.** Re-verified verbatim in arXiv v4.
   - **The source continues:** "where areas with an abundance of data are increasingly and disproportionately amenable to AI research".
   - **Do not reuse note 3's "main driver".**
9. **§5 (line 217):** "What the tools do well, well-posed problems with abundant data, is the technology's own pull (Hao et al. 2026)".
   - **Verdict: supported for AI used as a method.**
   - **Suggestion:** consider adding "and checkable results". Evidence:
     - AlphaFold and CASP;
     - the Lean proof of Erdős problem #728;
     - Nee et al.'s "capability threshold … available checks".
10. **`paper/draft_embo.md` (line 41):** "new preprints in the four quarters to September 2026 exceeded 2022 levels by 50% on bioRxiv and by 139% on medRxiv once COVID-19 papers are removed, although medicine's 2022 base was depressed by the pandemic … In the last year biology grew by 10%, against 78% for arXiv mathematics, consistent with Blekhman's point that biology's bottlenecks are experimental."
    - **Verdict: supported, with the nuance of item 3.**
    - **Two additions:**
      - bioRxiv's 2022 base was also below its 2020–21 level.
      - This biology-facing version should give medRxiv's +29% year on year, which beats physics, and say where it comes from (open datasets, letters). Otherwise biologists may read it as "biomedicine is unaffected".
11. **`paper/draft_embo.md` (line 37):** "At least 13.5% of PubMed abstracts from 2024 show signs of processing by LLMs, and up to about 40% in some groups (Kobak et al. 2025); most of this is ordinary use, such as language editing, that publishers permit."
    - **Verdict: the first clause is supported. "most of this is ordinary use, such as language editing" is not shown by Kobak et al.**
    - **Why:** word-frequency methods cannot separate editing from generation. Holzwarth et al. 2026 say the same of their method.
    - **Suggested rewording:** "much of this is probably ordinary language editing, which publishers permit".
12. **`paper/draft_embo.md` (line 31):** "And I bring field-level data on where the surge is concentrated."
    - **Verdict: supported.**
    - **Suggestion:** state the finding as writing everywhere, output where experiments are not needed.
13. **¶2.8, last sentence:** "At arXiv, congestion is no longer hypothetical; elsewhere it remains a conditional claim."
    - **Verdict: supported** for bioRxiv, which shows no break.
    - **"Elsewhere" now has partial counter-instances:**
      - management-journal submissions +42% (Gartenberg et al. 2026);
      - the surge in biomedical letters (Cancellario et al. 2026).
    - Consider citing them.
14. **`paper/brief.md`, author decision 3, and `paper/sources/Blekhman_2026_summary.md` (line 42):** "biology is not yet feeling this as much as other fields"; "Biology (bioRxiv) is +10% year on year in Q3 2026, consistent with his experimental-bottleneck point".
    - **Verdict: partly supported.**
      - **True for:** the 2026 acceleration in primary-research output.
      - **False for:**
        - writing prevalence (biology ≈ physics);
        - cumulative growth since 2022 (bioRxiv +50% vs physics +44%);
        - open-data and text-only biomedical outputs.
    - **The wording that holds:** "experimental biology, so far".
