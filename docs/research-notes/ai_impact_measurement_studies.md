# Measuring the use and impact of generative AI / LLMs on scientific papers, peer review, grant writing and research integrity (2022–2026): studies, methods, datasets

Notes compiled 2026-10-15. Labels used below: **[primary]** = read in the paper, preprint or official page itself; **[secondary]** = news, aggregator or summary report; **[vendor]** = claim by a detector company (Pangram, GPTZero, Grounded AI), not independently validated; **[own query 2026-10-15]** = counts I pulled from free public APIs while researching (User-Agent "academia-ia-state research", no key, no personal data). These are rough replication probes, not peer-reviewed estimates.

Process caveat: the shared web-search budget for this run ran out partway through. Later verification used only direct fetches of known URLs (arXiv pages and PDFs, Crossref and other public APIs). Items I could not verify that way are listed under Gaps.

---

## 1. Corpus-level LLM-usage estimates in papers (Kobak, Liang, Gray, Geng & Trotta, Bao, Kusumegi, 2026 follow-ups)

### Takeaway
Population-level methods agree that LLM-modified text rose sharply from about 5 months after ChatGPT's release (Nov 2022). By 2024:
- At least 13.5% of PubMed abstracts show LLM processing (lower bound; Kobak et al.).
- About 22.5% of sentences in arXiv computer-science abstracts are LLM-modified (Liang et al.), against about 7.7–9% in mathematics and the Nature portfolio.
- Rates are highest in computational fields and in non-English-speaking countries (China, South Korea, Taiwan about 20% versus UK/Australia about 5%).

No peer-reviewed PubMed-wide or arXiv-wide estimate using 2025–2026 data turned up. My own PubMed queries show that single marker words now diverge: "delve" halved in 2025 while "underscore" kept rising. This makes fixed marker lists unreliable for extending the series to 2026.

### Cited Findings

**Kobak, González-Márquez, Horvát & Lause, "Delving into LLM-assisted writing in biomedical publications through excess vocabulary", *Science Advances* 11(27): eadt3813, 2 Jul 2025 (arXiv 2406.07016, v1 11 Jun 2024; v5 3 Jul 2025 = journal version) [primary]**
- **Data:** >15 million PubMed abstracts, 2010–2024. The filtered PubMed baseline holds 24,814,136 complete English abstracts of 250–4,000 characters. — [arXiv abs](https://arxiv.org/abs/2406.07016v5); [paper PDF](https://arxiv.org/pdf/2406.07016v5)
- **Method ("excess vocabulary"):** no ground-truth LLM corpus is needed. Each word's observed frequency in year Y is compared with a conservative counterfactual linearly extrapolated from years Y−3 and Y−2, skipping Y−1: q = p₋₂ + 2·max{p₋₂ − p₋₃, 0}. For 2024 the counterfactual comes from 2021–2022. — [paper PDF](https://arxiv.org/pdf/2406.07016v5)
- **Headline:** at least 13.5% of 2024 abstracts were processed with LLMs, a lower bound. It was computed as the average frequency gap of two non-overlapping marker sets (rare and common style words), (Δcommon + Δrare)/2 = 0.135. — [PDF](https://arxiv.org/pdf/2406.07016v5)
- **Scale:** with about 1.5M papers indexed per year, this implies LLMs assisted at least 200,000 papers per year. — [PDF](https://arxiv.org/pdf/2406.07016v5)
- **Comparison with Covid:** Covid content words in 2021 gave Δ = 0.069, so LLM usage in 2024 was more than twice the size of the 2021 Covid literature. 379 style words had highly elevated frequencies in 2024. — [PDF](https://arxiv.org/pdf/2406.07016v5)
- **Heterogeneity (lower bound ranged from below 5% to over 40%):**

  | Subgroup | Δ (lower bound) |
  |---|---|
  | Computation, bioinformatics | ≈0.20 |
  | China, South Korea, Taiwan | ≈0.20 |
  | United Kingdom, Australia | ≈0.05 |
  | *Sensors* (MDPI) | 0.25 |
  | MDPI (all) | 0.21 |
  | *Cureus* | 0.20 |
  | Frontiers | 0.20 |
  | South Korea papers in *Sensors* | 0.34 |
  | Computation papers from China | 0.41 |
  | Inferred gender of first/last author | 0.09 (male) vs 0.07–0.08 (female) |

  Nature, Science, Cell and the Nature family were lower. — [PDF](https://arxiv.org/pdf/2406.07016v5)
- **Version difference:** earlier versions said "at least 10%" from about 14M abstracts (v2), so check which version is cited. — [arXiv v2](https://arxiv.org/abs/2406.07016v2)
- **Code and data:** [github.com/berenslab/llm-excess-vocab](https://github.com/berenslab/llm-excess-vocab), MIT licence.
  - `results/excess_words.csv` has 900 annotated excess words for 2013–2024.
  - `results/yearly-counts.csv.gz` is a 362,442 × 15 word-by-year count matrix.
  - Scripts build the corpus from the NCBI PubMed baseline XML.
  - Script 07 links retractions using PubMed and Retraction Watch data.
  - A July 2025 update added six more months of PubMed data and switched to monthly excess values. No 2026 results are shown.

**Liang et al. (14 authors, Stanford/Zou lab), "Quantifying large language model usage in scientific papers", *Nature Human Behaviour*, published 4 Aug 2025 (received 2 May 2024, accepted 19 Jun 2025), DOI 10.1038/s41562-025-02273-8 [primary]**
- **Data:** 1,121,912 papers from Jan 2020 to Sep 2024: 861,253 arXiv, 205,094 bioRxiv and 55,565 from 15 Nature-portfolio journals. Up to 2,000 papers were sampled per month and category. — [PDF](https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf); [DOI](https://doi.org/10.1038/s41562-025-02273-8)
- **Method:** the "distributional GPT quantification" framework, a maximum-likelihood mixture model.
  - Word-occurrence probabilities come from known human text and from LLM text generated with a two-stage process (summarise a pre-ChatGPT paragraph into an outline, then expand it with an LLM).
  - It estimates the fraction α of LLM-modified sentences in a corpus without classifying individual documents.
  - It uses the full vocabulary.
  - Validation error was under 3.5%. — [PDF](https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf)
- **Sep 2024 estimates of α (abstracts / introductions):**

  | Category | Abstracts (95% CI) | Introductions (95% CI) |
  |---|---|---|
  | Computer science | 22.5% (21.7–23.3) | 19.6% (19.2–20.0) |
  | Electrical engineering & systems science | 18.0% (16.7–19.3) | 18.4% |
  | Mathematics | 7.7% (7.1–8.3) | 4.1% |
  | Nature portfolio | 8.9% (8.2–9.6) | 9.4% |

  — [PDF](https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf)
- **Pre-ChatGPT baseline (Nov 2022), read as the false-positive floor:** 2.4% (CS), 2.9% (EESS), 2.5% (math), 3.4% (Nature portfolio). After subtracting it, the relative increase is still about 19% for arXiv CS abstracts. — [PDF](https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf)
- **Correlates:**
  - First authors with ≥3 preprints in 2023: 22.9% (abstracts, Sep 2024), versus about 20% (CI 19.2–20.8%) for ≤2 preprints.
  - Papers in more crowded areas (closer embedding neighbours) score higher.
  - Shorter papers (≤5,000 words): 22.0%.
  - Only 2 of 200 randomly sampled Feb-2024 arXiv CS papers disclosed LLM use. — [PDF](https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf)
- **Regions:**
  - bioRxiv: higher estimated usage for corresponding authors in China and Continental Europe than in North America and the UK.
  - arXiv CS: absolute estimates were similar across regions by the end of the study, but China showed the largest relative increase.
  - Africa and South America had too few papers to estimate. — [PDF](https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf)
- **Code and data:**
  - Code: [github.com/Weixin-Liang/Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Papers](https://github.com/Weixin-Liang/Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Papers).
  - arXiv metadata: [Kaggle Cornell-University/arxiv](https://www.kaggle.com/datasets/Cornell-University/arxiv). LaTeX was parsed with [s2orc-doc2json](https://github.com/allenai/s2orc-doc2json).
  - bioRxiv: [rbiorxiv](https://github.com/nicholasmfraser/rbiorxiv).
  - Baseline detectors compared: Fast-DetectGPT, MAGE and RADAR. — [PDF](https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf)
- **Earlier version:** the COLM-2024 preprint "Mapping the Increasing Use of LLMs in Scientific Papers" covered data to Feb 2024. It reported a range of about 7% (Nature portfolio) to 17% (CS) in early 2024, as summarised by Kobak et al. — [Kobak PDF](https://arxiv.org/pdf/2406.07016v5); [arXiv 2404.01268](https://arxiv.org/abs/2404.01268)

**Gray, "ChatGPT 'contamination': estimating the prevalence of LLMs in the scholarly literature", arXiv 2403.16887 (25 Mar 2024) [primary]**
- Uses disproportionately LLM-associated keywords.
- Estimates that at least 60,000 papers, "slightly over 1% of all articles", published in 2023 were LLM-assisted. — [arXiv](https://arxiv.org/abs/2403.16887)
- Kobak et al. note that Gray found a roughly 2-fold rise in 2023 for "intricate" and "meticulously". — [Kobak PDF](https://arxiv.org/pdf/2406.07016v5)

**Geng & Trotta, "Is ChatGPT transforming academics' writing style?", arXiv 2404.08627 (v1 12 Apr 2024, v2 8 Nov 2024) [primary]**
- 1 million arXiv abstracts, May 2018–Jan 2024.
- Uses word-frequency mixtures calibrated on GPT-3.5 "revise the following sentences" outputs.
- Estimated LLM-style share is about 35% in computer science. The definition differs from Liang's α, so the two are not directly comparable. — [arXiv](https://arxiv.org/abs/2404.08627)

**Bao, Sun & Teplitskiy, "Where there's a will there's a way: ChatGPT is used more for science in countries where it is prohibited", arXiv 2406.11583 (Jun 2024) [primary]**
- A word-usage classifier trained on pre/post-ChatGPT "polished" abstracts beat GPTZero and ZeroGPT on validation sets.
- Applied to arXiv, bioRxiv and medRxiv: about 12.6% of preprints used ChatGPT by Aug 2023.
- Use was 7.7 percentage points higher in countries where ChatGPT is restricted (e.g., China, Russia).
- Use was associated with more views and downloads but not with citations or journal placement. — [arXiv](https://arxiv.org/abs/2406.11583)

**Kusumegi, Yang, Ginsparg, de Vaan, Stuart & Yin, "Scientific production in the era of large language models", *Science* 390(6779): 1240–1243, 18 Dec 2025, DOI 10.1126/science.adw3000 (author version arXiv 2601.13187, 19 Jan 2026) [primary]**
- **Data:** 2.1M preprints, Jan 2018–Jun 2024: arXiv 1.2M, bioRxiv 221K, SSRN 676K.
- **Detection:** a distributional detector applied to every abstract. The human word distribution comes from pre-2023 abstracts; the LLM distribution comes from GPT-3.5-turbo-0125 rewrites of those abstracts. An author counts as an "adopter" from the first month a manuscript exceeds threshold τ. — [arXiv PDF](https://arxiv.org/pdf/2601.13187); [DOI](https://doi.org/10.1126/science.adw3000)
- Productivity and quality results are in section 2. Code/data availability is not stated in the arXiv author version (see Gaps).

**2026 follow-ups found (each is detailed in the relevant section below)**
- Shen & Wang 2026: peer reviews (§3).
- Naser 2026: grants (§5).
- Qian et al. PNAS 2026: grants (§5).
- Zhao et al. 2026: hallucinated citations (§4).
- Spick et al. JCE 2026: open-dataset floods (§4).
- Topaz et al. Lancet 2026: fabricated citations (§4).
- Renault et al. 2026 and Kusumegi et al. 2026 reply: productivity (§2).
- Hao et al. Nature 2026 (§2).

**My PubMed marker-word probe [own query 2026-10-15]**
- Method: hits for each word in title/abstract by publication year, divided by PubMed records with abstracts, via [E-utilities esearch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=delv*%5Btiab%5D+AND+2025%5Bdp%5D).
- Denominators (records with abstracts): 1,594,188 (2022), 1,559,511 (2024), 1,687,109 (2025), 1,368,223 (2026 to date).
- Rates per 10,000 abstracts:

  | Word | 2022 | 2023 | 2024 | 2025 | 2026 (partial) | 2025 vs 2024 |
  |---|---|---|---|---|---|---|
  | "delv*" | 3.9 | 18.8 | 66.3 | 32.4 | 10.3 | −51% |
  | "intricat*" | 15.3 | — | 106.3 | 77.5 | 39.9 | −27% |
  | "showcas*" | 12.0 | — | 55.0 | 39.7 | 20.1 | −28% |
  | "meticulous*" | 7.1 | — | 33.0 | 25.6 | 19.6 | −22% |
  | "underscor*" | 37.3 | 77.8 | 325.9 | 554.5 | 525.4 | +70% |
  | "notabl*" | 158.2 | — | 478.8 | 600.2 | 537.6 | +25% |
  | "pivotal" | 56.6 | — | 172.2 | 178.9 | 144.0 | +4% |

  ("—" = computed but not carried into these notes.)
- Caveats: 2026 is a partial year; indexing-lag composition effects apply; [tiab] matching is crude.

### Inferences
- The highest-quality, replicable corpus-level series are Kobak's (PubMed; data-driven discovery of excess words each year; lower bound) and Liang's (arXiv/bioRxiv/Nature; mixture MLE with baseline false-positive floor). Both publish code. Both stop at 2024 (Kobak's repo extends to mid-2025).
- The divergence in my 2025–2026 PubMed counts reproduces Geng & Trotta's "human–LLM coevolution" (§6). Widely publicised markers ("delve", "intricate", "showcase", "meticulous") fell after 2024 while less-publicised LLM-favoured words ("underscore", "notably", "pivotal") kept rising or held level. Extending a fixed 2024 marker list to 2025–2026 would understate usage. Re-running Kobak-style excess-word discovery per year, or re-calibrating Liang's distributions with current-generation model outputs, is needed.
- Country patterns are consistent across methods: higher in China, South Korea and Taiwan, lower in UK and Australia (Kobak; Liang bioRxiv; Bao). This fits LLMs used as English-language editing tools. It is not by itself evidence of misconduct.

### Gaps
- I found no peer-reviewed 2025- or 2026-data update of Kobak's PubMed lower bound or of Liang's arXiv/bioRxiv α series. Kobak's repo mentions a July 2025 monthly update but gives no numbers in its README.
- Gray (2024): the abstract page does not name the bibliographic database or list the marker words, so the data source could not be verified.
- Kusumegi et al.: data/code availability (Science supplementary materials) could not be checked. The arXiv author version has no availability statement.
- The Liang COLM-2024 numbers (950,965 papers; "up to 17.5%" CS) came only from a search summary and were not checked against the paper.

---

## 2. Productivity and quality effects of LLM / AI adoption (output per author, language/region differences, citations, acceptance; AI-as-research-tool)

### Takeaway
Observational studies associate LLM adoption with:
- 24–89% more preprints per author, with the largest gains for Asian-named authors (Kusumegi et al., *Science* 2025).
- A reversal of the link between writing complexity and quality.
- More diverse citing.

A 2026 comment (Renault, Bergeaud & Bosquet) shows the "first-detection" adoption timing can mechanically create such gains. The authors' 2026 reply re-estimates with four designs not exposed to that artifact and keeps a positive association, so the causal size remains contested.

For AI used as a research method (not writing), Hao et al. (*Nature*, Jan 2026) find AI-using natural scientists publish 3.02× more papers and get 4.84× more citations, while AI adoption shrinks collective topic breadth by 4.63%.

### Cited Findings

**Kusumegi et al., *Science* 2025 (arXiv 2601.13187) [primary]**
- **Productivity:** stacked difference-in-differences event study of 168,553 authors (Jan 2022–Jul 2024; arXiv 109,965, bioRxiv 43,218, SSRN 15,370). Adoption is associated with higher output relative to matched non-adopters: +36.2% (arXiv), +52.9% (bioRxiv), +59.8% (SSRN). — [arXiv PDF](https://arxiv.org/pdf/2601.13187)
- **By name/affiliation (inferred native-language proxy):**
  - Asian-named authors at Asian institutions: from 43.0% (arXiv) to 89.3% (bioRxiv) and 88.9% (SSRN).
  - Caucasian-named authors at institutions in English-speaking countries: 23.7% (arXiv) to 46.2% (SSRN).
  - The difference between Asian-named authors in Asia and in US/UK/CA/AU institutions is significant only in bioRxiv. — [arXiv PDF](https://arxiv.org/pdf/2601.13187)
- **Quality signal reversal:**
  - Complexity is measured as the additive inverse of Flesch Reading Ease. It is higher in LLM-assisted manuscripts (P<0.001).
  - In non-LLM papers, complexity predicts publication in a peer-reviewed venue by June 2024 (positive association).
  - In LLM-assisted papers the association becomes negative.
  - The pattern replicates with ICLR 2024 review scores (28K referee reports, 7,243 submissions) and with lexical, morphological and promotional-language measures. — [arXiv PDF](https://arxiv.org/pdf/2601.13187)
- **Reading and citing (246M arXiv accesses; diff-in-diff around Bing Chat's Feb 2023 launch, Google referrals as control):**
  - Bing users accessed books at a 26.3% higher rate.
  - LLM adopters are 11.9% more likely to cite books (not significant in SSRN).
  - They cite documents 0.379 years younger.
  - Cited documents have 2.34% lower citation impact. — [arXiv PDF](https://arxiv.org/pdf/2601.13187)
- **Stated limitations:**
  - No causal identification.
  - The abstract-only detector misses heavily edited text.
  - It cannot tell which co-author used the LLM.
  - Self-selection.
  - Adoption time may be endogenous to productivity. — [arXiv PDF](https://arxiv.org/pdf/2601.13187)

**Renault, Bergeaud & Bosquet, "Comment on Scientific production in the era of large language models", arXiv 2605.17979 (18 May 2026) [primary]**
- Dating adoption by the first flagged month mechanically ties treatment to output: more papers in a month make a flag more likely.
- Their simulation, with no true effect, yields a spurious positive post-treatment trend.
- Three placebos reproduce similar positive patterns: random paper-level assignment, neutral keyword flags, and a pre-ChatGPT window. — [arXiv](https://arxiv.org/abs/2605.17979)
- One secondary search summary called this a PNAS paper; arXiv lists no journal reference.

**Kusumegi et al., "A robust association between LLM use and scientific productivity: assessing stopping-time selection", arXiv 2607.28968 (31 Jul 2026; reply to Renault et al.) [primary]**
- Concedes the artifact is real but says it is small: the observed association stays well above a placebo recalibrated to the detector's flag rate.
- A positive association persists under four alternative designs: year-split before/after, a conservative diff-in-diff control, an intensity-based specification, and a rank-based measure with a fixed flag rate.
- Pre-ChatGPT placebo data give nulls. — [arXiv](https://arxiv.org/abs/2607.28968)

**Hao, Xu, Li & Evans, "Artificial intelligence tools expand scientists' impact but contract science's focus", *Nature*, published 14 Jan 2026, DOI 10.1038/s41586-025-09922-y (arXiv 2412.07727 v1 10 Dec 2024 → v4 29 Nov 2025) [primary]**
- **Scope:** AI as a research method (ML, deep learning, generative AI), not LLM writing.
- **Data:** 41,298,433 OpenAlex papers, 1980–2025, in biology, chemistry, geology, materials science, medicine and physics. Patterns were corroborated with Web of Science.
- **Detection:** a fine-tuned BERT classifier identified 310,957 AI-augmented papers (0.75%), with F1 = 0.875 against expert labels (expert agreement Fleiss κ = 0.964). — [arXiv PDF v4](https://arxiv.org/pdf/2412.07727v4); [Crossref record](https://api.crossref.org/works/10.1038/s41586-025-09922-y)
- **Results:**
  - AI-adopting scientists publish 3.02× more papers per year and receive 4.84× more citations.
  - Junior scientists using AI become project leaders 1.37 years earlier.
  - AI adoption contracts the median collective "knowledge extent" by 4.63%, seen in more than 70% of 200+ subfields.
  - AI research spawns 22.00% less follow-on engagement. — [arXiv PDF v4](https://arxiv.org/pdf/2412.07727v4)
- Press coverage of the final version uses the 41.3M-paper and 0.75% figures. — [HPCwire](https://www.hpcwire.com/2026/01/16/ai-for-science-study-good-for-the-goose-but-what-about-the-gander/)

**Other productivity/quality associations**
- **Zhao et al. 2026 [primary]:** authors who cite hallucinated references had, from pre-2023 to 2025, productivity increases relative to matched non-hallucination-citing authors of 1.93× (arXiv), 2.22× (bioRxiv), 3.13× (SSRN) and 1.33× (PMC). — [arXiv PDF](https://arxiv.org/pdf/2605.07723)
- **Liang et al. NHB 2025 [primary]:** higher LLM-modification for prolific first authors, crowded fields and shorter papers. These are correlations only. — [PDF](https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf)
- **Bao et al. 2024 [primary]:** ChatGPT use is associated with more views and downloads but not with citations or journal placement. — [arXiv](https://arxiv.org/abs/2406.11583)
- **McCreery & Naser, "LLM-assisted writing in engineering is associated with higher citations as evidenced from 1.17 million papers", *Journal of Informetrics* 20 (2026) 101842 (Sep 2026) [primary metadata only]:** title-level claim; abstract not retrieved. — [Crossref/DOI](https://doi.org/10.1016/j.joi.2026.101842)
- **Qian et al., PNAS 2026 (grants) [primary]:** at NIH, moving from the 25th to the 75th percentile of LLM involvement goes with about 4 percentage points higher funding probability and about 5% more publications. The gain is concentrated in non-hit papers. No associations at NSF. — [arXiv PDF](https://arxiv.org/pdf/2601.15485v3); details in §5.
- **Latona et al. 2024 [primary]:** AI-assisted ICLR 2024 reviews raise scores and acceptance. — [arXiv](https://arxiv.org/abs/2405.02150); details in §3.

### Inferences
- The best-identified evidence on output per author (Kusumegi) supports a positive association that is largest for non-native English speakers. Its magnitude is under active methodological dispute (stopping-time selection). Replications should date adoption in a window separate from the window where output is measured, and add pre-ChatGPT placebo cohorts.
- "Quality" findings point the same way across studies. More LLM-polished text is less informative about merit (Kusumegi). Extra output concentrates in non-hit work (Qian at NIH; Hao's narrowing of topics). Hallucination-citing authors are unusually productive (Zhao).
- Hao et al. measure AI-as-method rather than LLM writing. Their 3×/4.8× ratios are cross-sectional comparisons between AI adopters and others, not causal effects of LLMs.

### Gaps
- No randomized or natural-experiment estimate of LLM writing assistance on publication or citation outcomes was found.
- McCreery & Naser (JOI 2026): only the title was verified, not the effect size or method.
- No study found that measures acceptance-rate effects of LLM-written manuscripts at journals (as opposed to LLM-assisted reviews).

---

## 3. Peer review: LLM-written or LLM-assisted reviews (ICLR, NeurIPS, CoRL, EMNLP, ICML, journals)

### Takeaway
LLM-modified review text rose from about 2% before ChatGPT to 6.5–16.9% across ICLR 2024, NeurIPS 2023, CoRL 2023 and EMNLP 2023 (Liang et al., distributional). Classifier-based studies give:
- About 20% of ICLR 2025 reviews and 12% of Nature Communications 2025 reviews classified AI-generated (Shen & Wang 2026).
- 21% of ICLR 2026 reviews (15,899 of 75,800) "fully AI-generated" according to Pangram's EditLens [vendor]. Authors' own accusations matched these labels 86% of the time.

AI-assisted reviews score papers higher. In ICLR 2024 borderline papers, receiving one went with +4.9 pp acceptance. Journal evidence is thinner (AACR via Pangram: 5% of 2024 review reports) and comes mostly from vendor tools or secondary reports.

### Cited Findings

**Liang et al., "Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews", arXiv 2403.07183, ICML 2024 (v1 11 Mar 2024; v4 19 May 2026) [primary]**
- Distributional MLE over expert-written and AI-generated reference texts.
- Between 6.5% and 16.9% of review text could have been substantially modified by LLMs, beyond spell-checking. — [arXiv](https://arxiv.org/abs/2403.07183)
- **By venue (α before → after ChatGPT):**

  | Venue | Before | After |
  |---|---|---|
  | ICLR (2024) | 1.6% | 10.6% |
  | NeurIPS (2023) | 1.9% | 9.1% |
  | CoRL (2023) | 2.4% | 6.5% |
  | EMNLP (2023) | — | ≈16.9% |
  | Nature-portfolio reviews (2019–2023) | no significant increase | no significant increase |

  — [arXiv PDF v2](https://arxiv.org/pdf/2403.07183v2)
- **Correlates:**
  - Higher in reviews submitted within 3 days of the deadline.
  - Higher in reviews with lower self-reported confidence.
  - Higher for reviewers less likely to respond to author rebuttals.
  - Higher AI modification correlates with homogenised review content. — [arXiv PDF v2](https://arxiv.org/pdf/2403.07183v2)
- Applying ChatGPT only as an editor to reviews raised α much less than the effect seen in the real corpus. — [arXiv PDF v2](https://arxiv.org/pdf/2403.07183v2)

**Latona, Horta Ribeiro, Davidson, Veselovsky & West, "The AI Review Lottery", arXiv 2405.02150 (3 May 2024) [primary]**
- Using GPTZero, at least 15.8% of ICLR 2024 reviews were AI-assisted.
- Within pairs of reviews of the same paper, the AI-assisted review gave the higher score in 53.4% of pairs (p=0.002).
- In a matched study of borderline papers, those receiving an AI-assisted review were 4.9 pp more likely to be accepted (p=0.024). — [arXiv](https://arxiv.org/abs/2405.02150)

**Shen & Wang, "Detecting AI-Generated Content in Academic Peer Reviews", arXiv 2602.00319 (30 Jan 2026; v2 23 Mar 2026) [primary]**
- **Detector:** Longformer + LoRA trained on 2021 reviews versus synthetic reviews from the DeepSeek Reasoner API. About 500 papers are sampled per year, giving roughly 2,000 reviews per year.
- **ICLR share classified AI-generated:**

  | Year | AI-detected / reviews | Share |
  |---|---|---|
  | 2022 | 2 / 1,937 | 0.10% |
  | 2023 | 0 / 1,887 | 0.00% |
  | 2024 | 133 / 1,818 | 7.32% |
  | 2025 | 392 / 1,961 | 19.99% |

- **Nature Communications:** about 12% of 2025 reviews; the sharpest growth came between Q3 and Q4 2024.
- Code: [github.com/sy-shen/AI_Review](https://github.com/sy-shen/AI_Review). — [arXiv](https://arxiv.org/abs/2602.00319); [PDF](https://arxiv.org/pdf/2602.00319v2)

**ICLR 2026, Pangram analysis (Nov 2025)**
- Pangram's EditLens classified 15,899 of all 75,800 reviews of the 19,490 ICLR 2026 submissions (21%) as fully AI-generated. Labels are downloadable at iclr.pangram.com, as cited in the peer-reviewed paper below; the page itself did not render for me. — [Baumann et al. arXiv PDF](https://arxiv.org/pdf/2605.03202v2) [primary citing vendor data]
- Secondary reports add that more than half of reviews showed some AI involvement, and that 199 submissions (about 1%) were fully AI-generated. — [hyper.ai](https://hyper.ai/en/stories/267bbf4513e22ff5912134b478153928); [Slashdot summary of Nature](https://tech.slashdot.org/story/25/11/28/139247) [secondary/vendor]
- **Independent check (Baumann, Pei, Koyejo & Hovy, "Stop Automating Peer Review Without Rigorous Evaluation", arXiv 2605.03202, ICML 2026 position track, May 2026) [primary]:**
  - They searched all 159,775 author comments on ICLR 2026 submissions and found 58 cases where authors accused a specific review of being AI-generated.
  - Of these, 50 (86.2%) were independently flagged by Pangram as fully AI-generated.
  - AI reviewers show "hivemind" agreement (within-paper similarity +8.7% to +9.8% versus humans).
  - LLM rewriting of a paper ("paper laundering") raises AI-review scores by +0.45 (p<0.0001). — [arXiv PDF](https://arxiv.org/pdf/2605.03202v2)
- **Abdulhai et al., "How LLMs Distort Our Written Language", arXiv 2603.18161 (18 Mar 2026; v2 26 Aug 2026) [primary]:** in reviews from "a recent top AI conference", 21% were AI-generated. LLM-generated reviews placed less weight on clarity and significance and gave scores on average about one point higher. — [arXiv](https://arxiv.org/abs/2603.18161)

**Conference enforcement data (brief)**
- **ICLR 2026 (blog, 19 Nov 2025):**
  - Papers with extensive undisclosed LLM use are desk-rejected.
  - Hallucinated references count as Code of Ethics violations, and papers containing them are desk-rejected.
  - Detection tools flag items, but action requires concrete evidence found by an area chair or senior area chair.
  - Reviewers who post fabricated reviews may have their own submissions desk-rejected.
  - No counts were published in that post. — [ICLR blog](https://blog.iclr.cc/2025/11/19/iclr-2026-response-to-llm-generated-papers-and-reviews/)
- **ICML 2026:** using watermarked PDFs, ICML desk-rejected 497 papers (about 2% of submissions) after flagging about 1% of reviews as violating a no-LLM policy the reviewers had agreed to. This is cited by Baumann et al. from Agarwal et al. 2026. — [Baumann et al. PDF](https://arxiv.org/pdf/2605.03202v2)
- **ICLR 2025 randomized trial (Thakkar et al., arXiv 2504.09737):**
  - A "Review Feedback Agent" gave LLM feedback on more than 20,000 randomly chosen reviews (about half of ICLR 2025's), 15 Oct–12 Nov 2024.
  - 26.6% of reviewers who received feedback updated their reviews.
  - 12,222 feedback items were incorporated. — [ICLR blog](https://blog.iclr.cc/2025/04/15/leveraging-llm-feedback-to-enhance-review-quality/); [arXiv](https://arxiv.org/abs/2504.09737)
  - Code reportedly at github.com/zou-group/review_feedback_agent (search-summary claim, not opened).

**Hidden prompt injection aimed at LLM reviewers**
- A July 2025 commentary found 18 arXiv manuscripts with hidden prompts meant to manipulate AI-assisted review, one more than Nikkei Asia reported. — [Lin, arXiv 2507.06185](https://arxiv.org/abs/2507.06185) [primary per search summary; abstract not re-opened]
- Experimental work shows such injections can push frontier AI reviewers to full scores. — [Zhou et al., arXiv 2511.01287](https://arxiv.org/abs/2511.01287) [search summary]

**Journals, AACR with Pangram (reported in *Nature*, Sep 2025)**
- The AACR screened 46,500 abstracts, 46,021 methods sections and 29,544 peer-review comments submitted to 10 AACR journals, 2021–2024.
- In 2024 submissions, 23% of abstracts and 5% of peer-review reports contained text "probably generated" by LLMs.
- Fewer than 25% of authors disclosed AI use despite a disclosure requirement. — [InfoDocket summary of Nature d41586-025-02936-6](https://www.infodocket.com/2025/09/11/report-ai-tool-detects-llm-generated-text-in-research-papers-and-peer-reviews/) [secondary/vendor tool]
- Another secondary excerpt reports a different measure: 36% of 7,177 manuscripts submitted Jan–Jun 2025 were flagged in the abstract, while only 9% of all submissions disclosed AI use. The disclosure numbers conflict across secondary sources. — [mirror of Nature text](https://scribe.disroot.org/comment/6840992) [secondary, unverified]

### Inferences
- Classifier and vendor estimates for 2025–2026 (about 20–21% of ICLR reviews) are several times the 2023–2024 distributional estimates (about 10%). Part of this is real growth. Part is definitional: "fully AI-generated review" versus "fraction of sentences substantially modified". Use one method consistently for a time series.
- The author-complaint validation (50 of 58 matched) is the only independent check of Pangram's ICLR labels I found. It speaks to recall on obvious cases, not to the false-positive rate.
- Reviews are an attractive target for replication: venue, deadline timing and reviewer confidence give natural covariates. The main data access is now hampered (see §7, OpenReview challenge).

### Gaps
- Pangram's own ICLR methodology post (thresholds, false-positive estimates) could not be retrieved: the web-search budget was exhausted and iclr.pangram.com returned no static content.
- No systematic, non-vendor estimate for journal peer reviews beyond Nature Communications (Shen & Wang) and the Liang 2024 null for Nature-portfolio reviews.
- No counts were found of desk rejections or reviewer sanctions actually applied at ICLR 2026. A follow-up post was promised.

---

## 4. Research integrity: formulaic floods on open datasets, hallucinated references, leftover chatbot phrases, paper mills, retractions

### Takeaway
Three integrity signals are now measured at scale.

**(1) Open-data paper floods.**
- NHANES single-factor papers went from about 4 per year (2014–2021) to 190 in Jan–Oct 2024.
- Nine open health datasets produced 23,005 papers in 2025, 11,577 above ARIMA trend.
- FAERS disproportionality papers went from about 100 (2021) to 600 (2024).

**(2) Fabricated or hallucinated references.**
- About 1 in 277 PubMed papers in early 2026, versus 1 in 2,828 in 2023 (Lancet audit).
- An estimated 146,932 hallucinated citations in 2025 across arXiv, bioRxiv, SSRN and PubMed Central (Zhao et al.).
- About 1% of NeurIPS 2025 accepted papers (GPTZero, vendor).

**(3) Leftover chatbot phrases.**
- Hundreds of documented cases: Academ-AI 768, Retraction Watch list 95.

Retraction data (Retraction Watch, open via Crossref) has no LLM-specific reason code, so it is weak for tracking AI-specific retractions.

### Cited Findings

#### 4a. Formulaic papers built on open datasets

**Suchak, Aliu, Harrison, Zwiggelaar, Geifman & Spick, "Explosion of formulaic research articles, including inappropriate study designs and false discoveries, based on the NHANES US national health database", *PLOS Biology*, May 2025 (PMC12061153) [primary]**
- 341 NHANES papers each reporting a single predictor associated with a health condition.
- About 4 per year in 2014–2021, then 190 in 2024 up to 9 Oct.
- China-affiliated primary authors: 2 of 25 papers in 2014–2020 versus 292 of 316 in 2021–2024.
- Depression (28 papers): with Benjamini–Yekutieli false-discovery correction, an estimated 15 of 28 associations would lose significance.
- Systemic immune-inflammation index: 10 of 14 papers used unexplained subsets of NHANES years.
- PubMed NHANES-related papers overall rose from 4,926 (2023) to 7,876 (2024). — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12061153/)

**Spick, Onoja, Harrison, Stender, Byrne & Geifman, "Quantifying new threats to health and biomedical literature integrity from rapidly scaled publications and problematic research", medRxiv 10.1101/2025.07.07.25331008 (v1 9 Jul 2025; v2 16 Jan 2026) → *Journal of Clinical Epidemiology* 2026, DOI 10.1016/j.jclinepi.2026.112203 [primary]**
- Scientometric screen of 36 open datasets in OpenAlex. Nine show "hallmarks of paper mill exploitation": FAERS, NHANES, UK Biobank, FinnGen, Global Burden of Disease, MIMIC, CHARLS, CDC WONDER and TriNetX.
- These nine had 23,005 OpenAlex-indexed publications in 2025, an excess of 11,577 above the ARIMA forecast. This is a 3.0× fold change on 7,655 in 2022.
- Fold change was 4.2× for China versus 1.9× for the rest of the world, with more formulaic titles.
- The authors attribute part of the surge to "AI-assisted and formulaic workflows". — [bioRxiv/medRxiv API record](https://api.biorxiv.org/details/medrxiv/10.1101/2025.07.07.25331008); [DOI](https://doi.org/10.1016/j.jclinepi.2026.112203)

**FAERS (pharmacovigilance) flood (Retraction Watch, 16 Sep 2025) [secondary, with primary counts reported]**
- FAERS-mining studies in PubMed: about 100 (2021) and 600 (2024).
- *Expert Opinion on Drug Safety* published 174 FAERS studies in 2024, nearly 60% of its output. About 80% of its 2019–2025 disproportionality studies had China-based authors.
- In late July 2025 the journal stopped considering unsolicited FAERS-type disproportionality studies.
- *Frontiers in Pharmacology*: about 30 such studies (2023) versus more than 120 (2024). It rejected 739 FAERS submissions after July 2024, and Frontiers required external validation for health-dataset studies from May 2025.
- Matt Spick links generative AI plus open databases to automated paper-mill output. — [Retraction Watch](https://retractionwatch.com/2025/09/16/exclusive-journal-bans-drug-safety-database-papers-as-they-flood-the-literature/)
- Bibliometric preprint (CC BY): Khouri et al., "The Rising Misuse of Pharmacovigilance Reporting Systems", Zenodo, 14 Sep 2025. Counts are given only in a figure. — [Zenodo](https://zenodo.org/records/17116885) [primary]

**Mendelian randomization / UK Biobank**
- An editorial argues that public GWAS summary statistics have led to an "explosion of low-quality two-sample MR studies". — [Stender, Gellert-Kristensen & Davey Smith, *Lipids in Health and Disease*, Sep 2024](https://research.regionh.dk/en/publications/reclaiming-mendelian-randomization-from-the-deluge-of-papers-and-/) [search summary]
- A meta-epidemiological review found reporting problems across 116 UK Biobank MR articles. — [Gibson et al.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10086297/) [search summary]
- UK Biobank and FinnGen are in Spick's nine-dataset list above.

#### 4b. Hallucinated or fabricated references

**Topaz, Roguin, Gupta, Zhang, Peltonen, "Fabricated citations: an audit across 2·5 million biomedical papers", *The Lancet*, May 2026, DOI 10.1016/S0140-6736(26)00603-3; authors' reply DOI 10.1016/S0140-6736(26)01589-8 (Sep 2026) [primary metadata; findings via Retraction Watch]**
- About 97.1M references checked in about 2.5M PubMed-indexed papers. 4,046 fabricated references found in 2,810 papers. Retraction Watch prints 4,046; other secondary summaries print 4,406, so the discrepancy is unresolved.
- Rate: about 1 in 2,828 papers (2023), 1 in 458 (2025), 1 in 277 (first 7 weeks of 2026). This is a 12-fold rise in two years, with the steepest rise in mid-2024.
- Reviews had a 57% higher rate than other article types.
- One unnamed publisher's rate was more than 14 times that of the most selective journals.
- 91% of problematic papers had only one or two fabricated references.
- Over 98% had "no publisher action" as of Feb 2026.
- AI was used to separate fabrications from formatting errors; a critic says it was validated on 500 records. — [Crossref/DOI](https://doi.org/10.1016/S0140-6736%2826%2900603-3); [Retraction Watch, 7 May 2026](https://retractionwatch.com/2026/05/07/one-in-277-pubmed-indexed-papers-in-2026-shows-fabricated-references-says-analysis/)

**Zhao, Wang, Stuart, De Vaan, Ginsparg & Yin, "LLM hallucinations in the wild: Large-scale evidence from non-existent citations", arXiv 2605.07723 (8 May 2026) [primary]**
- **Corpora (111M references in 2.5M papers):**
  - arXiv: 1,465,145 preprints, Jan 2020–Aug 2025.
  - bioRxiv: 261,928 preprints, 21.2M citation records.
  - SSRN: 421,698 preprints, 26.8M citations via Crossref.
  - PubMed Central: a random sample of 374,807 papers from 2020–2025, 19.2M citations.
- **Verification:** an Elasticsearch index over Semantic Scholar plus OpenAlex. After refinement, the pipeline's unmatched baseline is 1.54%. "Hallucinated" means excess unmatched citations above the pre-LLM baseline; individual references are not classified. — [arXiv PDF](https://arxiv.org/pdf/2605.07723)
- **Rates and volumes (Aug 2025):**

  | Corpus | Hallucination rate | Monthly volume |
  |---|---|---|
  | arXiv | 0.39% | 3,353 |
  | bioRxiv | 0.21% | 478 |
  | SSRN | 1.91% | 767 |
  | PMC | 0.27% | 8,140 |

  The steepest rise starts in mid-2024. Extrapolated to the year end, this gives 146,932 hallucinated citations in 2025 across the four corpora. — [arXiv PDF](https://arxiv.org/pdf/2605.07723)
- **Correlates:**
  - Field-level estimated LLM-writing use correlates with hallucination rate (r = 0.441).
  - Hallucinated references disproportionately credit already prominent and male scholars.
  - arXiv-rejected submissions had a 2.2% rate by Aug 2025, 4.5× that of accepted ones.
  - Of hallucinations in 2,241 bioRxiv preprints traced to PMC, 85.3% persisted into the published version. — [arXiv PDF](https://arxiv.org/pdf/2605.07723)
- *Nature* news on SSRN being the highest-rate site: "Hallucinated citations highest in social sciences preprints site", 14 May 2026. — [DOI](https://doi.org/10.1038/d41586-026-01545-1) [secondary, metadata only]

**Nature with Grounded AI (Naddaf & Quill), "Hallucinated citations are polluting the scientific literature. What can be done?", *Nature*, 1 Apr 2026, DOI 10.1038/d41586-026-00969-z [secondary/vendor]**
- At least tens of thousands of 2025 publications probably contain AI-generated invalid references. — [DOI](https://doi.org/10.1038/d41586-026-00969-z); [Retraction Watch citing it](https://retractionwatch.com/2026/05/07/one-in-277-pubmed-indexed-papers-in-2026-shows-fabricated-references-says-analysis/)
- Blog-level details: more than 4,000 publications from five publishers; 65 of the 100 most suspicious had at least one invalid reference; a back-of-envelope extrapolation to 110,000+. — [Boing Boing](https://boingboing.net/2026/04/08/science-now-with-110000-made-up-sources.html/amp) [secondary, unverified]

**Conference papers**
- **GPTZero [vendor]:**
  - NeurIPS 2025: 4,841 of 5,290 accepted papers scanned; at least 100 human-verified hallucinated citations in 51 papers (the table header says 53); published 21 Jan 2026. Its tool claims a very low false-negative rate but a higher false-positive rate, so every flag was human-verified. — [GPTZero](https://gptzero.me/news/neurips/)
  - ICLR 2026 (Dec 2025): 300 sampled submissions, 90 flagged, 50 confirmed with at least one hallucinated citation. — [GPTZero](https://gptzero.me/news/arxiv-ban/)
- **Sakai, Kamigaito & Watanabe, "HalluCitation Matters", arXiv 2601.18724 (26 Jan 2026) [primary]:** across all ACL, NAACL and EMNLP 2024–2025 papers, nearly 300 papers contain at least one non-existent reference. Most are from 2025, about half at EMNLP 2025, and more than 100 were accepted EMNLP 2025 main/Findings papers. — [arXiv](https://arxiv.org/abs/2601.18724)
- **arXiv policy (brief):** on 14 May 2026 arXiv's CS section announced a one-year ban for submitting unchecked AI-generated content, including hallucinated citations. — [GPTZero summary](https://gptzero.me/news/arxiv-ban/) [vendor-reported]

**Tool validity**
- Badalova & Mayr (arXiv 2607.22693, Jul 2026) evaluated five hallucinated-reference checkers: CheckIfExist, HalluCiteChecker, Hallucinator, HalRef and RefChecker. All give "useful early warnings" but are limited by reference-extraction errors, incomplete metadata and database coverage. — [arXiv](https://arxiv.org/abs/2607.22693) [primary abstract]

#### 4c. Leftover chatbot phrases, case datasets

- **Academ-AI (Alex Glynn), arXiv 2411.15218 (v1 Nov 2024: 500 cases; v2 15 Nov 2025: 768 cases), published in IntelliSys 2026 (LNNS vol. 2077, DOI 10.1007/978-3-032-32729-1_19) [primary]:**
  - Suspected undeclared AI use is identified mainly by chatbot phrasing.
  - Cases appear in journals, proceedings and textbooks of major publishers, and more often in journals with higher citation metrics and higher article processing charges.
  - Very few cases are corrected, and corrections are often inadequate. — [arXiv](https://arxiv.org/abs/2411.15218v2)
- **Retraction Watch "Papers and peer reviews with evidence of ChatGPT writing" list:** 95 entries (92 papers, 2 peer reviews, 1 author response), 3 marked retracted. It is built with Guillaume Cabanac's search strategy. — [Retraction Watch list](https://retractionwatch.com/papers-and-peer-reviews-with-evidence-of-chatgpt-writing/) [primary, accessed 2026-10-15]
- **Problematic Paper Screener (Cabanac, Labbé et al.):** a ChatGPT-fingerprint detector, one of nine detectors, listed more than 70 papers with signs such as "Regenerate response" as of Jan 2025. — [The Conversation, republished](https://cobbcountycourier.com/2025/01/problematic-paper-screener-trawling-for-fraud-in-the-scientific-literature/); [PPS paper](https://arxiv.org/abs/2210.04895)
- **Europe PMC full-text phrase hits by publication year [own query 2026-10-15]** — [Europe PMC REST example](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22as%20an%20AI%20language%20model%22%20AND%20PUB_YEAR:2025&format=json&resultType=idlist):

  | Phrase | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 YTD |
  |---|---|---|---|---|---|---|
  | "as an AI language model" | 0 | 2 | 155 | 257 | 507 | 460 |
  | "regenerate response" | 0 | 0 | 22 | 21 | 16 | 7 |
  | "as of my last knowledge update" | 0 | 0 | 2 | 10 | 2 | 0 |

  These are unscreened. Many "as an AI language model" hits are probably legitimate quotations in papers about ChatGPT, so the counts are upper bounds on leftovers.

#### 4d. Retraction Watch database (open via Crossref)

- **Access:** Crossref acquired the database in Sep 2023 and made it public. It is a CSV in a GitLab repo, updated every working day.
  - Fields include Reason (controlled vocabulary), RetractionNature, Country, Publisher, and Original/Retraction DOI and PubMed IDs.
  - The older Labs API CSV route is retired in favour of git clone. — [GitLab repo](https://gitlab.com/crossref/retraction-watch-data); [Crossref docs](https://crossref.org/documentation/retrieve-metadata/retraction-watch/)
  - Latest commit seen: 2026-10-14, "Retraction Watch data for 2026-10-14". — [GitLab API](https://gitlab.com/api/v4/projects/crossref%2Fretraction-watch-data/repository/commits?per_page=1) [own query]
- **Crossref REST** lists 76,260 works carrying a retraction update (all sources) as of 2026-10-15. — [api.crossref.org](https://api.crossref.org/v1/works?filter=update-type:retraction&rows=0) [own query]
- **My analysis of the 2026-10-14 CSV (67.5 MB; 67,776 retractions, 3,732 expressions of concern, 1,543 corrections, 163 reinstatements) [own query]:**
  - Retractions by retraction year: 3,913 (2021), 5,591 (2022), 13,298 (2023, the Hindawi/Wiley mass retractions), 6,497 (2024), 5,995 (2025), 2,096 (2026 to Oct 14, likely lagged).
  - There is **no LLM-specific reason code**. The closest is "Computer-Aided Content or Computer-Generated Content", which also covers SCIgen and tortured phrases.

  | Retraction year | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 YTD |
  |---|---|---|---|---|---|---|
  | Computer-Aided/Generated Content | 481 | 383 | 5,551 | 1,453 | 1,275 | 194 |
  | Paper Mill | 815 | 934 | 6,782 | 1,805 | 1,115 | 3 |
  | Concerns/Issues about Referencing/Attributions | 239 | 711 | 7,650 | 2,479 | 2,874 | 551 |

  - Only 3 retraction records mention ChatGPT, LLMs or generative AI in the Notes field.
  - Kobak et al.'s repo shows how to join PubMed and Retraction Watch data. — [repo](https://github.com/berenslab/llm-excess-vocab)

### Inferences
- The most specific signals of unchecked LLM use (non-existent references, chatbot boilerplate) are rising fastest from mid-2024. That timing matches AI search and agentic tools generating citations, as Zhao et al. suggest. These signals complement the less specific vocabulary-based estimates.
- Open-dataset floods are concentrated in a few datasets (NHANES, FAERS, UK Biobank, GBD and others) and in China-affiliated authorship. They show a 2022 inflection. LLM involvement there is inferred from timing, formulaic titles and journal reports, not measured directly.
- The Retraction Watch data is useful for paper-mill and referencing trends but cannot isolate generative-AI retractions without text-mining notices. The 2026 "Paper Mill" count of 3 suggests coding lags, so recent years should not be compared naively.

### Gaps
- The Topaz Lancet methods (AI verifier, validation set, definitions) were seen only via Retraction Watch. The 4,046 vs 4,406 discrepancy is unresolved.
- No quantitative growth series for MR or GBD floods by themselves (beyond Spick's combined nine-dataset counts). Khouri et al.'s FAERS counts are in a figure only.
- Academ-AI's live case count (academ-ai.info) and the PPS live ChatGPT-fingerprint count were not retrieved.
- A widely repeated claim that 2.6% of 2025 papers at three CS conferences (about 18,000 papers) had potentially hallucinated citations, versus 0.3% in 2024, was seen only in a search summary. It is unverified.

---

## 5. Grant writing: LLM use in applications and funded-award abstracts (NIH, NSF, UKRI, ERC/CORDIS)

### Takeaway
Two 2026 studies measure LLM signals in grants:
- **Qian et al. (PNAS, Aug 2026):** distributional α on 5.7K confidential NSF/NIH proposals and 131K public awards. α rises sharply from 2023 with a bimodal distribution. Higher α goes with less distinctive ideas. At NIH only, it also goes with higher funding probability (about +4 pp, 25th→75th percentile) and more, but non-hit, publications.
- **Naser (arXiv, Sep 2026):** 221,425 funded abstracts. Marker rates rose 27% (NIH), 52% (NSF) and 54% (UKRI) after ChatGPT. NSF and UKRI rates are now falling from 2024–2025 peaks while NIH's keeps climbing.

No ERC/CORDIS-specific study was found.

### Cited Findings

**Qian, Wen, Furnas, Bai, Shao & Wang, "The rise of large language models and the direction and impact of US federal research funding", *PNAS* 123(33): e2601439123, published 11 Aug 2026 (arXiv 2601.15485 v1 21 Jan 2026 → v3 5 Jul 2026) [primary]**
- **Data:**
  - D1: 1.6K NSF and D2: 4.1K NIH confidential proposal submissions (funded, unfunded, pending) from two large US R1 universities, request start dates 2021–2025.
  - D3: 57K NSF and D4: 74K NIH public awards (start 2021–2025) from Dimensions, linked to publications. — [arXiv PDF v3](https://arxiv.org/pdf/2601.15485v3); [Crossref/PNAS](https://doi.org/10.1073/pnas.2601439123)
- **Method:** the Liang et al. distributional estimator. Human distribution from 2021 award abstracts; LLM distribution from GPT-3.5-turbo-0125 rewrites. α is estimated per corpus-month and per grant. — [arXiv PDF v3](https://arxiv.org/pdf/2601.15485v3)
- **Findings:**
  - α is flat before late 2022 and rises sharply from 2023 at both submission and award stages. NIH is lower on average than NSF.
  - Among 2023–2025 grants α is bimodal: one mode near 0 and one around 10–15%.
  - Moving from the 25th to the 75th percentile of α corresponds to about 5 points lower distinctiveness percentile (NSF awards) and about 4 points (NIH). Distinctiveness is measured with SPECTER2 against the prior year's funded work.
  - NIH proposals: about +4 pp funding probability (25th→75th percentile α), within investigator.
  - NIH awards: about 5% more publications, not significant for top-5% or top-1% papers.
  - NSF: no significant association with success or output. — [arXiv PDF v3](https://arxiv.org/pdf/2601.15485v3)
- **Availability:** confidential D1–D2 require a data use agreement with the universities. Project page: [northwestern-cssi.github.io/llmfunding](https://northwestern-cssi.github.io/llmfunding/). The underlying D3–D4 come from Dimensions, a commercial database. — [arXiv PDF v3](https://arxiv.org/pdf/2601.15485v3)
- Press framing: "Large language models reduce originality of research proposals". — [Times Higher Education](https://www.timeshighereducation.com/news/large-language-models-reduce-originality-research-proposals) [secondary]

**Naser, "LLM Signals in Funded Grants: Evidence from International Funding Agencies", arXiv 2609.13241 (3 Sep 2026; brief report, single author) [primary]**
- **Data:** 221,425 funded grant abstracts, late 2017 to mid-2026: NSF n=96,020; NIH n=80,496; UKRI n=44,909.
- **Method:** frequency of a 68-element lexical marker set from prior work, per 100,000 tokens.
- **Marker rate, pre → post ChatGPT:**

  | Agency | Pre | Post | Change | Cohen's d |
  |---|---|---|---|---|
  | NSF | 274.7 | 417.1 | +51.9% | 0.348 |
  | NIH | 266.6 | 339.3 | +27.3% | 0.210 |
  | UKRI | 224.1 | 344.3 | +53.6% | 0.280 |

  — [arXiv PDF](https://arxiv.org/pdf/2609.13241)
- **Share above pre-ChatGPT tails:** taking the pre-ChatGPT 95th and 99th percentile marker rates as thresholds, the post-period excess is 4.0–8.4% (NSF), 1.4–3.7% (NIH) and 2.8–6.8% (UKRI). The author reads this as a lower bound on substantial assistance: about 1 in 12–25 NSF, 1 in 27–71 NIH and 1 in 15–36 UKRI funded proposals. — [arXiv PDF](https://arxiv.org/pdf/2609.13241)
- **Where the rise concentrates:**
  - NSF: technology translation, computer and information science, and mathematical and physical sciences are largest; geosciences and social, behavioural and economic sciences smallest.
  - UKRI: Innovate UK and BBSRC largest; AHRC and NERC smallest.
  - NIH: NIGMS and NCI lead; NIA trails.
- Sentence length, abstract length and sentence count are flat, so the shift is lexical.
- NSF and UKRI marker rates in recent 2026 quarters are well below their 2024–2025 peaks, while NIH continues to rise. The author cautions this could reflect newer models, writer adaptation, disciplinary mix or incomplete harvest.
- Data available on request. — [arXiv PDF](https://arxiv.org/pdf/2609.13241)

**My NIH RePORTER probe [own query 2026-10-15]**
- Source: [NIH RePORTER API v2](https://api.reporter.nih.gov/v2/projects/search) (POST; no key; returns `abstract_text`; `award_types` filter works).
- New (type-1) awards with "delve/delves/delving" in the abstract:

  | Fiscal year | Hits / type-1 awards | Per 10k |
  |---|---|---|
  | FY2021 | 13 / 20,138 | 6.5 |
  | FY2022 | 17 / 20,220 | 8.4 |
  | FY2023 | 27 / 19,646 | 13.7 |
  | FY2024 | 65 / 18,503 | 35.1 |
  | FY2025 | 51 / 15,438 | 33.0 |

- FY2024 has 83,538 projects of all types. All-type counts dilute the signal because continuation awards reuse old abstracts.
- The [NSF Awards API](https://api.nsf.gov/services/v1/awards.json?keyword=delve&dateStart=01/01/2024&dateEnd=12/31/2024&printFields=id,title,date) also returns `abstractText` without a key.

**Policy context (brief, covered elsewhere)**
- NSF encourages disclosure of generative-AI use.
- In September 2025 the NIH activated a policy treating applications "substantially developed by AI" as violating originality expectations. — [Times Higher Education](https://www.timeshighereducation.com/news/large-language-models-reduce-originality-research-proposals) [secondary]

### Inferences
- Funded-award abstracts are public, reasonably long and versioned by fiscal year, which makes them good for replication (NIH RePORTER, NSF API, UKRI Gateway to Research). Restrict to new/competing awards and to the application date rather than the fiscal year, or the LLM-era signal is diluted and lagged.
- The NIH-only success association (Qian) and the NIH-only continued marker rise (Naser) are consistent. Neither establishes causality. Agencies differ in review culture, abstract templates and policy timing.
- A falling marker rate (NSF, UKRI 2026) is not evidence of falling use. It mirrors the "delve" decline in PubMed (§1, §6).

### Gaps
- No study using ERC/CORDIS project abstracts or Horizon Europe applications was found. The search budget ran out before a targeted search, so this is unverified absence, not confirmed absence.
- No study with unfunded applications at agency scale (only Qian's two universities).
- Naser's methods detail (exact marker list) and data are only "on request".

---

## 6. Validity: detector false positives, bias against non-native writers, vocabulary drift, editing/translation tools, and which methods are most robust

### Takeaway
Per-document detectors have documented bias: an average 61% false-positive rate on non-native TOEFL essays across 7 detectors in 2023. Vendor accuracy claims (Pangram, GPTZero) are not independently established for scientific text.

Corpus-level methods are more robust but have their own weaknesses:
- Liang's distributional MLE has a non-zero pre-ChatGPT floor (about 2–3%) and biases at the extremes.
- Kobak's excess vocabulary is an explicit lower bound and cannot separate LLM use from humans adopting LLM-style words.

Humans demonstrably adopt and then avoid LLM marker words (spoken-language evidence; "delve" collapse). For a 2022–2026 time series the most defensible choice is a combination:
- Data-driven excess-word discovery refreshed each year, plus a distributional estimator re-calibrated with current models.
- Pre-ChatGPT placebo and baseline subtraction.
- Reporting as lower bounds.
- Cross-checks with high-specificity signals (fabricated references, chatbot phrases).

### Cited Findings

**Detector bias (Liang, Yuksekgonul, Mao, Wu & Zou, "GPT detectors are biased against non-native English writers", *Patterns* 2023, arXiv 2304.02819) [primary per search summary]**
- 7 detectors, 91 TOEFL essays and 88 US 8th-grade essays.
- Average false-positive rate on TOEFL essays was 61.22%, against near-perfect accuracy on native essays.
- 18 of 91 (19.78%) TOEFL essays were flagged by all seven detectors, and 89 of 91 (97.80%) by at least one.
- Having GPT-4 enrich the essays' vocabulary cut the false-positive rate to 11.77%. The mechanism is low perplexity of constrained vocabulary. — [arXiv](https://arxiv.org/abs/2304.02819)

**Corpus-method biases (Liang et al., NHB 2025) [primary]**
- The estimator "systematically overestimates LLM usage at the lower end and underestimates it at the higher end".
- It is not a direct measure of use.
- Author-population or style shifts (e.g., more multilingual scholars) could bias it.
- Pre-ChatGPT 2022 estimates were low (2.4–3.4%) despite many multilingual authors, which they read as low bias against language learners.
- LLM "proofreading" of text changed estimates little. — [PDF](https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf)
- The 2024 peer-review paper likewise found only slight α increases when reviews were merely edited by ChatGPT. — [arXiv PDF v2](https://arxiv.org/pdf/2403.07183v2)

**Excess vocabulary limits (Kobak et al. 2025) [primary]**
- It cannot distinguish frequency increases due to direct LLM use from people adopting LLM-preferred words, or between different LLMs.
- It is a lower bound because abstracts processed by LLMs may contain no marker words. — [PDF](https://arxiv.org/pdf/2406.07016v5)

**Vocabulary drift / coevolution**
- **Geng & Trotta, "Human-LLM Coevolution: Evidence from Academic Writing", arXiv 2502.09606 (Feb 2025; ACL Findings 2025):** in arXiv abstracts, words flagged as ChatGPT-overused (e.g., "delve") dropped markedly soon after being publicised in early 2024, while others (e.g., "significant") kept rising. Writers adapt by selecting or editing outputs, which makes detection harder. Frequency analysis remains viable if word lists are updated. — [arXiv](https://arxiv.org/abs/2502.09606) [primary]
- **Yakura et al., "Empirical evidence of Large Language Model's influence on human spoken communication", arXiv 2409.01754 (v4 16 Jul 2026) [primary]:**
  - Synthetic-control analysis of 737,083 hours of unscripted speech from 824,634 podcast episodes shows abrupt post-ChatGPT rises in "delve", "showcase", "boast", "intricacies" and "meticulous".
  - A preregistered experiment (n=496) showed brief chatbot exposure makes people adopt its words. — [arXiv](https://arxiv.org/abs/2409.01754)
- **My PubMed probe [own query]:**
  - Relative to 2024, the 2025 rate fell for "delv*" (−51%), "showcas*" (−28%), "intricat*" (−27%) and "meticulous*" (−22%).
  - It rose for "underscor*" (+70%), "notabl*" (+25%) and "pivotal" (+4%).
  - All were elevated 3–17× in 2024 versus 2022. — [E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=underscor*%5Btiab%5D+AND+2025%5Bdp%5D)
- **Naser 2026:** the marker rate is "a contemporary measurement of a moving phenomenon, not a stable instrument". It depends on which models are in use, which words they overproduce, and what writers know about the markers. — [arXiv PDF](https://arxiv.org/pdf/2609.13241) [primary]

**Adoption-timing artifact**
- First-detection adoption dating creates stopping-time selection bias in productivity event studies. — [Renault et al. 2026](https://arxiv.org/abs/2605.17979)
- The bias is acknowledged but argued to be small. — [Kusumegi et al. reply 2026](https://arxiv.org/abs/2607.28968) [primary]

**Vendor detector claims (treat cautiously)**
- Pangram advertises a false-positive rate of about 1 in 10,000 and cites third-party evaluations (University of Chicago, University of Maryland, University of Houston/UC Berkeley). These were seen only on affiliate or aggregator pages. — [CASRAI guide](https://www.casrai.org/guides/most-accurate-ai-detector) [secondary/vendor, unverified]
- Nature reportedly described a Pangram-CEO preprint claiming 99.85% accuracy. — [search-summarised; see AACR item in §3] [vendor]
- Pangram's blog reports detection rates for new models, e.g., 1,105 of 1,107 Claude Opus 5 samples (99.82%), Jul 2026. — [Pangram blog index](https://www.pangram.com/blog) [vendor]
- GPTZero states its hallucination checker has a low false-negative but higher false-positive rate and needs human verification. — [GPTZero](https://gptzero.me/news/neurips/) [vendor]
- ICLR 2026 explicitly required area-chair-verified "concrete evidence" because detectors produce false positives. — [ICLR blog](https://blog.iclr.cc/2025/11/19/iclr-2026-response-to-llm-generated-papers-and-reviews/)
- The only independent real-world check found is the author-complaint agreement of 86.2% (50 of 58). — [Baumann et al.](https://arxiv.org/pdf/2605.03202v2)

**Validity of hallucination counts**
- Topaz et al. do not separate critical from peripheral references, and miss inaccurate-but-real citations. — [Retraction Watch critics](https://retractionwatch.com/2026/05/07/one-in-277-pubmed-indexed-papers-in-2026-shows-fabricated-references-says-analysis/)
- Zhao et al. use excess-over-baseline rather than per-reference classification, and validate manually. — [arXiv PDF](https://arxiv.org/pdf/2605.07723)

### Inferences
- **Most robust for a 2022–2026 corpus series:**
  1. Kobak-style excess-word discovery, re-run each year on the full corpus. Report Δ as a lower bound with two independent marker sets. Do not freeze the 2024 list.
  2. A Liang-style distributional MLE, re-calibrated yearly with text from the then-dominant models, with the Nov-2022 α subtracted as a false-positive floor.
  3. Placebo years (e.g., 2019–2021) for any marker set.
  4. Stratification by field, country and journal, because composition shifts (e.g., Spick's 3× surge in some datasets) can move aggregate rates.
  5. Cross-validation against high-specificity indicators: unmatched references above baseline, chatbot boilerplate.
- Per-document commercial detectors are useful for flagging but unsuitable as the sole instrument for a reproducible time series. They are closed and frequently re-versioned (Pangram 3 → Pangram 4 in 2026), and false-positive rates are vendor-reported, with known non-native-writer bias in earlier tools.
- Machine translation and grammar tools probably raise distributional estimates somewhat. The only direct evidence found (proofreading tests) suggests the effect is small relative to observed growth.

### Gaps
- The independent evaluations of Pangram (e.g., a University of Chicago study often cited as Jabarian & Imas) could not be opened; the search budget was exhausted.
- No study found that directly quantifies how DeepL or Google-Translate translation of non-English drafts, or Grammarly-style editing, shifts excess-vocabulary or distributional estimates on scientific abstracts.
- No independent false-positive rate estimate exists for EditLens on peer reviews or on non-native scientific prose.

---

## 7. Reusable public datasets, code and API endpoints for replication on arXiv, bioRxiv/medRxiv and PubMed (and extension to 2026)

### Takeaway
All three target corpora are openly reachable:
- **PubMed:** baseline XML plus E-utilities.
- **bioRxiv/medRxiv:** api.biorxiv.org.
- **arXiv:** Kaggle/OAI bulk metadata. Its search API is unsuitable for counting.

Reference implementations exist on GitHub for Kobak (MIT) and Liang. Integrity datasets are open: Retraction Watch via Crossref GitLab (daily), the Retraction Watch ChatGPT list, Academ-AI and the PPS. Grant abstracts are open via NIH RePORTER and NSF APIs. OpenReview review data is currently behind an anti-bot challenge for anonymous API calls.

### Cited Findings

**Code and data from the studies**

| Study | Code / data |
|---|---|
| Kobak et al. 2025 | [github.com/berenslab/llm-excess-vocab](https://github.com/berenslab/llm-excess-vocab) (MIT): 900 excess words, 362,442-word × year counts, PubMed-baseline pipeline, PubMedBERT/t-SNE scripts, retraction join |
| Liang et al. NHB 2025 | [Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Papers](https://github.com/Weixin-Liang/Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Papers); inputs from Kaggle arXiv, s2orc-doc2json, rbiorxiv — [NHB PDF](https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf) |
| Shen & Wang 2026 (review detector) | [github.com/sy-shen/AI_Review](https://github.com/sy-shen/AI_Review) — [PDF](https://arxiv.org/pdf/2602.00319v2) |
| Pangram ICLR 2026 review labels (EditLens) | iclr.pangram.com, per [Baumann et al.](https://arxiv.org/pdf/2605.03202v2) [vendor] |
| Qian et al. 2026 (grants) | [northwestern-cssi.github.io/llmfunding](https://northwestern-cssi.github.io/llmfunding/); public awards via Dimensions (commercial); proposals need a data use agreement — [PDF](https://arxiv.org/pdf/2601.15485v3) |
| Naser 2026 | data on request — [PDF](https://arxiv.org/pdf/2609.13241) |
| Spick et al. 2026 | OpenAlex-based counts — [medRxiv record](https://api.biorxiv.org/details/medrxiv/10.1101/2025.07.07.25331008) |
| Hao et al. 2026 | OpenAlex corpus; no code link in the arXiv v4 text — [PDF](https://arxiv.org/pdf/2412.07727v4) |
| Zhao et al. 2026 | Semantic Scholar + OpenAlex verification index; no code link on the abstract page — [arXiv](https://arxiv.org/abs/2605.07723) |

**Integrity datasets**
- Retraction Watch CSV: [gitlab.com/crossref/retraction-watch-data](https://gitlab.com/crossref/retraction-watch-data), updated every working day; field and vocabulary docs in the README.
- Crossref REST `filter=update-type:retraction`: 76,260 works on 2026-10-15. — [api.crossref.org](https://api.crossref.org/v1/works?filter=update-type:retraction&rows=0) [own query]
- Retraction Watch ChatGPT-writing list (95 entries). — [Retraction Watch](https://retractionwatch.com/papers-and-peer-reviews-with-evidence-of-chatgpt-writing/)
- Academ-AI (768 cases in v2). — [arXiv](https://arxiv.org/abs/2411.15218v2)
- Problematic Paper Screener. — [PPS paper](https://arxiv.org/abs/2210.04895)

**Endpoints tested on 2026-10-15 [own query]**

| Endpoint | Result |
|---|---|
| PubMed E-utilities esearch `rettype=count` | Works without key; occasional throttling, so use retries |
| Europe PMC REST | Full-text phrase search with `PUB_YEAR` filter works; returns `hitCount` |
| bioRxiv/medRxiv API `/details/{server}/{DOI}` | Works; returns abstract, versions and published-journal DOI |
| arXiv API | `abs:delve` with `max_results=0` returned totalResults=1, so not usable for corpus counts; use bulk metadata (Kaggle/OAI) as Liang et al. did |
| NIH RePORTER v2 | POST works without key; includes `abstract_text`; `award_types` and `advanced_text_search` filters work |
| NSF Awards API | Returns `abstractText` without key |
| OpenReview API v2 (ICLR 2026 submissions) | HTTP 403 "ChallengeRequiredError" for anonymous requests |

Links: [E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=hasabstract+AND+2025%5Bdp%5D) · [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22regenerate%20response%22%20AND%20PUB_YEAR:2024&format=json&resultType=idlist) · [bioRxiv API example](https://api.biorxiv.org/details/medrxiv/10.1101/2025.07.07.25331008) · [arXiv API](https://export.arxiv.org/api/query?search_query=abs:delve&max_results=0) · [RePORTER](https://api.reporter.nih.gov/v2/projects/search) · [NSF API](https://api.nsf.gov/services/v1/awards.json?keyword=delve&dateStart=01/01/2024&dateEnd=12/31/2024&printFields=id,title,date) · [OpenReview](https://api2.openreview.net/notes?invitation=ICLR.cc/2026/Conference/-/Submission&limit=1)

Raw outputs from my queries are saved in `/tmp/claude-0/-home-user/eefa93ff-68d4-5a29-84a6-8be683e07b57/scratchpad/dl_api/` (pubmed_delve_counts.txt, pubmed_marker_counts.txt, pubmed_marker_counts_fill.txt, europepmc_phrases.txt) and `/tmp/claude-0/-home-user/eefa93ff-68d4-5a29-84a6-8be683e07b57/scratchpad/dl_rw/retraction_watch.csv`.

### Inferences
- **Minimal replication stack for 2022–2026:**
  - **PubMed:** baseline XML plus daily updates, through Kobak's pipeline. Kobak's counterfactual for year Y uses Y−3 and Y−2. Applied naively to 2025–2026, it would put LLM-era years (2022–2023 for 2025; 2023–2024 for 2026) into the baseline. For cumulative LLM-era tracking, keep a fixed pre-ChatGPT base (extrapolated from 2021–2022) and report rolling year-over-year excess separately to capture newly emerging markers.
  - **arXiv:** Kaggle or OAI metadata, through Liang's code (re-generate the LLM reference distribution with 2025–2026 models).
  - **bioRxiv/medRxiv:** the date-range endpoint of api.biorxiv.org, through both.
  - **Integrity overlays:** reference verification against OpenAlex or Semantic Scholar, following Zhao's approach; Europe PMC full-text phrase counts with manual screening; and the Retraction Watch CSV joined on DOI/PMID.
- For peer-review series, OpenReview access will likely need authenticated or approved access, or published label dumps such as Pangram's ICLR file. Plan for this constraint.

### Gaps
- I did not open Kusumegi et al.'s *Science* supplementary data or code. Their stopping-time reply (arXiv 2607.28968) may include replication material; unverified.
- Not checked: Bao et al.'s code; Liang 2024's peer-review code; the Thakkar review-agent repository (search-summary claim only); live Academ-AI and PPS download formats.
- Not tested: CORDIS bulk data, UKRI Gateway to Research API, OpenAlex API, Kaggle arXiv snapshot freshness.
