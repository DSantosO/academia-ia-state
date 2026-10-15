# Testing the "acceleration, not exploration" hypothesis: evidence, theory, measurement and research designs

Notes for section 4 of the position paper. Compiled 2026-10-15.

**Tags.** **[S]** supports the hypothesis that metric incentives channel AI into exploitation. **[C]** cuts against it. **[N]** nuances it or is ambiguous. **[M]** concerns method or measurement. **[PREPRINT]** marks work not peer reviewed as of 15 Oct 2026, and **[WP]** marks a working paper.

**Verification.** On 2026-10-15 I checked every DOI below against Crossref and every arXiv ID against the arXiv API, except where a line says otherwise. Abstract wording comes from Crossref, Europe PMC, OpenAlex, Semantic Scholar or arXiv, as indicated.

## 1. Hao, Xu, Li & Evans (Nature 2026): do the final numbers match the arXiv version?

### Takeaway
The final Nature abstract reports exactly the figures the author has: 3.02× papers, 4.84× citations, project leadership 1.37 years earlier, 4.63% topic contraction and 22% less engagement. These figures already appear in arXiv v2 (Oct 2025) to v4. The **first arXiv version (Dec 2024) reported very different numbers**, so quote "Nature 2026", never "the 2024 preprint".

The bigger risk for section 4 lies in what the numbers measure, not in the numbers themselves:
- **"AI"** means AI used as a research *method* (ML/DL), in natural-science papers. The generative-AI era is covered only by analyses the authors call "preliminary".
- **"Topic contraction"** compares AI papers with non-AI papers. It does not follow scientists over time.
- **"Engagement"** is citation density among the papers that build on a given paper. It is not a measure of collaboration.

### Cited Findings
- **Citation.** Hao, Q., Xu, F., Li, Y. & Evans, J. A. (2026). Artificial intelligence tools expand scientists' impact but contract science's focus. *Nature* 649(8099): 1237–1243. Published online 14 Jan 2026; the issue is dated 29 Jan 2026. PMID 41535462. — [DOI](https://doi.org/10.1038/s41586-025-09922-y); [Europe PMC](https://europepmc.org/article/MED/41535462)
- **Final abstract** (Europe PMC copy of the Nature abstract): "Scientists who engage in AI-augmented research publish 3.02 times more papers, receive 4.84 times more citations and become research project leaders 1.37 years earlier than those who do not. By contrast, AI adoption shrinks the collective volume of scientific topics studied by 4.63% and decreases scientists' engagement with one another by 22%." The abstract also gives 41.3 million papers and a classifier F1 of 0.875. — [Europe PMC](https://europepmc.org/article/MED/41535462)
- **Version history (arXiv API):**
  - **v1 (10 Dec 2024)** has different numbers throughout. It analyses "67.9 million research papers across six major fields" with F1 = 0.876. Adopters "publish 67.37% more papers, receive 3.16 times more citations, and become team leaders 4 years earlier". AI research "contracts the diameter of scientific topics" and "diminishes follow-on scientific engagement", with no percentages given. — [arXiv v1](https://arxiv.org/abs/2412.07727v1)
  - **v2 (4 Oct 2025)** switches to the final numbers: 41.3M papers, 3.02×, 4.84×, "1.37 years (15.75%) earlier", 4.63%, and "22.00% when they build upon AI-augmented work". — [arXiv v2](https://arxiv.org/abs/2412.07727v2)
  - **v3 (18 Nov 2025)** and **v4 (29 Nov 2025)**, titled "Just accepted by Nature", carry the same numbers as the final paper. — [v3](https://arxiv.org/abs/2412.07727v3); [v4](https://arxiv.org/abs/2412.07727v4)
  - **v4 versus final.** Only the wording differs: "22.00%" becomes "22%", "Thereby" becomes "By consequence", and "appear to automate established fields" becomes "seem to automate established fields". — [v4](https://arxiv.org/abs/2412.07727v4); [Europe PMC](https://europepmc.org/article/MED/41535462)
- **Data and AI identification** (v4 full text, the accepted version). All of the following come from [arXiv v4 HTML](https://arxiv.org/html/2412.07727v4):
  - **Source and scope.** OpenAlex. 66,117,158 English papers from 1980–2025 were filtered to **41,298,433** in biology, chemistry, geology, materials science, medicine and physics. Computer science and mathematics are excluded.
  - **AI papers.** **310,957** papers (0.75%) are classed as AI-augmented.
  - **Classifier.** AI use is identified by a fine-tuned BERT classifier on titles and abstracts. It was validated against 1,320 papers labelled by 12 experts (Fleiss' κ = 0.964).
  - **What counts as AI use.** The target is papers that "use AI to support natural science research". The visible text does not say whether writing assistance alone counts.
  - **Eras.** ML (1980–2014), DL (2015–2022) and generative AI (GAI, 2023 onwards). The GAI-era analyses are called "preliminary".
- **How the two "collective" numbers are built.** Both come from [arXiv v4 HTML](https://arxiv.org/html/2412.07727v4).
  - **Topic contraction (4.63%).** "Knowledge extent" is the maximum Euclidean distance from the centroid in SPECTER 2.0 embedding space. It is computed on 1,000 AI and 1,000 non-AI papers per field, resampled 1,000 times. 4.63% is the contraction in median knowledge extent. Knowledge entropy is also lower for AI papers.
  - **Engagement (22%).** "Follow-on engagement" is the density of citation links among papers that cite the same original paper, EG = 2k/[n(n−1)]. AI papers score 22.00% lower.
- **Career effects.** All points come from [arXiv v4 HTML](https://arxiv.org/html/2412.07727v4).
  - **Definitions.** The "project leader" is the last author. Time to leadership comes from a birth–death model.
  - **Matching.** A matched comparison is in the Supplementary Notes: 11,019 adopters matched to 1,926 non-adopters on early-career citations and productivity.
  - **Causality.** The authors write: "we cannot fully identify the causal linkage between AI adoption and scientific impact."
- **What drives AI's concentration** (authors' analysis). Data availability is the main driver. Topicality, original impact and funding are "almost unrelated". The authors describe the result as "collective hill-climbing". — [arXiv v4 HTML](https://arxiv.org/html/2412.07727v4)
- **Coverage (NPR, 17 Feb 2026).**
  - Evans: "Individual scientists have a shared problem, which is survival, right?" and "there's kind of a narrowing of science around what it is that these tools can do". He also calls the collective effect "a kind of a public goods problem".
  - NPR's caveat: "Because this study analyzed existing work, scientists can't say for sure that AI is the definitive cause of this pattern."
  - Steven Salzberg (Johns Hopkins): "When you have a hammer, you go around looking for nails, and that's what AI is right now."
  - — [NPR story, Public Radio East copy](https://www.publicradioeast.org/2026-02-17/ai-is-helping-individual-scientists-study-suggests-but-not-science)
- **Other coverage found** but not readable (403/405 errors): [HPCwire, Jan 2026](https://www.hpcwire.com/2026/01/16/ai-for-science-study-good-for-the-goose-but-what-about-the-gander/); [Chemistry World](https://www.chemistryworld.com/news/ai-research-tools-benefit-individual-scientists-but-may-slow-scientific-progress/4022803.article).

### Inferences
- **Numbers.** Section 4 can use the five numbers as published, attributed to *Nature* (2026). Anyone citing the 2024 preprint would report "67% more papers / 3.16× citations / 4 years earlier". The paper should cite the final version only.
- **Wording the 22%.** Avoid "22% less engagement between scientists". Better: "work that builds on AI-augmented papers is 22% less interconnected by citation". It measures citation-network density, not collaboration or contact.
- **Wording the 4.63%.** It compares AI and non-AI paper sets. It shows that AI papers occupy a narrower region of topic space. It does **not** show that adopters narrowed their own agendas.
- **What Hao et al. actually test.** The paper is about AI *as a method* (ML/DL), largely before ChatGPT. It supports "AI gravitates to data-rich, established areas". It does not directly test the paper's claim that generative AI makes papers almost free to produce.
- **The incentive reading is the author's (and Evans's) interpretation, not something Hao et al. test.** Their own analysis of what drives AI's concentration points to data availability (technological affordance). The incentive story is supported by Evans's framing in interviews ("survival", "public goods problem"), not by a test in the paper.

### Gaps
- **Methods source.** The Nature full text and SI were paywall-redirected, so the methods details come from arXiv v4. Small changes between v4 and the final Methods/SI cannot be excluded.
- **News & Views.** I found no *Nature* News & Views on the paper.
- **Unverified critique.** Search-engine summaries attribute to Molly Crockett (Princeton) a critique that citation-based "impact" may reflect hype and economic incentives rather than quality. I could not open the underlying article, so verify the quote before using it.
- **GAI-era results.** The generative-AI-era robustness results were in the part of the v4 text I could not read (the page was truncated).

## 2. Empirical studies bearing on exploitation versus exploration with AI

### Takeaway
The evidence is mixed and less direct than section 4 implies.

**Pointing toward concentration in established directions and reduced collective diversity:**
- studies of AI used *as a method* (Hao; the Bianchini preprint);
- studies of LLM-*generated ideas* (Si; Liu; Bao);
- lab studies of creativity (Doshi & Hauser; Anderson; Padmakumar & He; Meincke).

**Pointing the other way, at the individual level:**
- The one large within-author study of the LLM era (Zheng et al. 2026, a preprint) finds that **more** scientists entered new and more distant fields after 2022.
- Kusumegi et al. (Science 2025) find that adopters cite **more diverse** literature.

No study yet links *measured individual use of generative AI for research tasks* to a change in exploration with credible identification.

### Cited Findings

**(a) AI as a research method**
- **[S] Hao et al. (2026)** — see Q1.
- **[S/N] Bianchini, S., Müller, M. & Pelletier, P. (2022).** Artificial intelligence in science: an emerging general method of invention. *Research Policy* 51(10): 104604.
  - **Published abstract.** Neural-network AI is diffusing across the sciences as an emerging "general method of invention", with "a prominent impact on scientific discovery, but a high degree of uncertainty and ambiguity associated with this impact". — [DOI](https://doi.org/10.1016/j.respol.2022.104604); [OpenAlex abstract](https://api.openalex.org/works/doi:10.1016/j.respol.2022.104604)
  - **2020 preprint ("Deep Learning in Science") [PREPRINT].** In health sciences, "DL adoption is negatively correlated with re-combinatorial novelty, but positively correlated with expectation as well as variance of citation performance". It also finds "a transition from interdisciplinary DL applications to disciplinary research within application domains". — [arXiv:2009.01575](https://arxiv.org/abs/2009.01575)
- **[N] Duede, E., Dolan, W., Bauer, A., Foster, I. & Lakhani, K. (2024).** Oil & water? Diffusion of AI within and across scientific fields. **[PREPRINT]**
  - Covers about 80M publications in 20 fields, 1985–2022. AI-engaged publications grew about 13×, and engagement broadened within disciplines.
  - But there is a "semantic tension": AI-engaged work is "spreading out over fields, but not mixing well with non-AI-engaged work".
  - — [arXiv:2405.15828](https://arxiv.org/abs/2405.15828)
- **[N] Gao, J. & Wang, D. (2024).** Quantifying the use and potential benefits of AI in scientific research. *Nature Human Behaviour* 8(12): 2281–2292.
  - AI use and benefits are widespread and have grown rapidly since 2015.
  - There is a gap between AI education and AI application.
  - Disciplines with higher proportions of women or Black scientists reap fewer benefits.
  - — [DOI](https://doi.org/10.1038/s41562-024-02020-5)

**(b) LLM-era bibliometric evidence**
- **[S] Liang, W. et al. (2025).** Quantifying large language model usage in scientific papers. *Nature Human Behaviour* 9(12): 2599–2609.
  - Covers 1,121,912 papers from Jan 2020 to Sep 2024 (arXiv, bioRxiv, Nature portfolio).
  - LLM-modified content reaches up to 22% in computer science and up to 9% in mathematics and the Nature portfolio.
  - Estimates are higher for first authors who post preprints more often, for "papers in more crowded research areas" and for shorter papers.
  - — [DOI](https://doi.org/10.1038/s41562-025-02273-8); [Europe PMC](https://europepmc.org/article/MED/40760036)
- **[S/C] Kusumegi, K., Yang, X., Ginsparg, P., de Vaan, M., Stuart, T. & Yin, Y. (2025).** Scientific production in the era of large language models. *Science* 390(6779): 1240–1243.
  - Covers 2.1M preprints, 28K review reports and 246M accesses.
  - Adopters' output rises 23.7–89.3%, "depending on scientific field and author background".
  - LLM use "reversed the relationship between writing complexity and paper quality".
  - **[C]** Adopters "access and cite more diverse prior work, including books and younger, less-cited documents".
  - — [DOI](https://doi.org/10.1126/science.adw3000); [author version, arXiv:2601.13187](https://arxiv.org/abs/2601.13187)
- **[M] Renault, T., Bergeaud, A. & Bosquet, C. (2026).** Comment on "Scientific production in the era of large language models". **[PREPRINT]**
  - Kusumegi et al. date adoption to the first month in which an abstract is flagged. That timing is mechanically tied to output, because months with more papers are more likely to contain a flagged one.
  - A simulation with no causal effect still produces a positive post-adoption path.
  - Three placebos (random paper-level assignment, neutral keyword flags, a pre-ChatGPT window) produce similar positive patterns.
  - — [arXiv:2605.17979](https://arxiv.org/abs/2605.17979)
- **[C] Zheng, X., Hong, X., Liu, J. & Ni, C. (2026).** Scientific exploration, collaboration and labor division in the large language model era. **[PREPRINT]**
  - **Data.** PubMed Central full text linked to OpenAlex histories for **775,323 scientists**, plus CRediT contribution statements from 137,120 papers.
  - **Main result.** After 2022, scientists "increasingly published across more intellectually distant fields and entered fields in which they had not previously worked". This was most pronounced among established scientists and those from non-English-speaking low- and middle-income countries.
  - **Selection.** Authors with stronger AI-writing signals "were already more interdisciplinary and exploratory before" LLMs, and the gap widened after 2022.
  - **AI-heavy authors and collaborators.** Their interdisciplinarity became "less closely tied to the disciplinary diversity of their collaborators".
  - **Team roles.** Contributors reported narrower role sets. Software and validation roles rose; conceptual and management roles fell.
  - — [arXiv:2607.20923](https://arxiv.org/abs/2607.20923)
- **[S] Bao, H., Wu, S., Liu, X., Li, S., Cao, S. & Evans, J. A. (2026).** Contemporary AI lacks the imagination to diverge or negate in science. **[PREPRINT]**
  - **Survey.** Authors of 121,640 preprints were invited; 6,749 scientists returned 25,139 rating sets on LLM ideas derived from their own papers.
  - **Model behaviour.** Non-reasoning LLMs "collapse into a narrow 'hivemind'". Reasoning models explore more widely, but "no model spontaneously proposes null hypotheses".
  - **Scientists' preferences.** Scientists "reward ideas resembling their own and prize probability over novelty".
  - **Macro pattern.** Across 39M papers from 2010–2025, "following ChatGPT's release, null claims are sharply suppressed and ideas contract".
  - — [arXiv:2606.08251](https://arxiv.org/abs/2606.08251)
- **[S/N] Safari, A. & Babaei, S. (2026).** Research novelty in Information Systems journals after ChatGPT (v3; v1 was titled "Do LLMs reduce research novelty?"). **[PREPRINT]**
  - **Data.** 13,847 articles from 44 A*/A IS journals, 2020–2025.
  - **Measure.** SPECTER2 semantic distance from each article's nearest recent predecessors.
  - **Result.** Articles whose first authors are at institutions in non-English-dominant countries show a **0.176 SD larger post-2022 decline** in relative novelty, about 7 percentile points.
  - **Authors' caveat.** "Because individual LLM use is not observed, the result identifies a heterogeneous post-2022 shift rather than an effect of LLM adoption."
  - — [arXiv:2603.22510](https://arxiv.org/abs/2603.22510)
- **[C/N] Filimonovic, D., Rutzer, C. & Wunsch, C. (2025).** Can GenAI improve academic performance? Evidence from the social and behavioral sciences. **[PREPRINT]**
  - Uses a matched author panel and difference-in-differences.
  - GenAI adoption is associated with "sizable increases" in output and "moderate gains" in journal impact factor.
  - Effects are largest for early-career researchers, technically complex subfields and authors from non-English-speaking countries.
  - — [arXiv:2510.02408](https://arxiv.org/abs/2510.02408)
- **[N] Lin, C. W. & Zhu, W. (2025).** Divergent LLM adoption and heterogeneous convergence paths in research writing. **[PREPRINT]**
  - Covers 627K arXiv papers, using fine-tuned discipline-specific detectors.
  - A difference-in-differences finds that LLMs "drive convergence in academic writing". Early adopters, male researchers, non-native speakers and juniors shift most, toward the style of established researchers.
  - — [arXiv:2504.13629](https://arxiv.org/abs/2504.13629)
- **[N] Bao, H., Sun, M. & Teplitskiy, M. (2025).** Where there's a will there's a way: ChatGPT is used more for science in countries where it is prohibited. *Quantitative Science Studies* 6: 716–731.
  - ChatGPT was used in about 12.6% of preprints by Aug 2023, with 7.7% higher use in restricted countries.
  - Use correlates with more views and downloads, "but not citations or journal placement".
  - — [DOI](https://doi.org/10.1162/qss_a_00368); [arXiv:2406.11583](https://arxiv.org/abs/2406.11583)
- **[S] Volume and "thin" papers: arXiv's own account (1 Oct 2026).**
  - September 2026 brought 40,363 submissions, against 20,569 in Sep 2024 and 9,869 in Sep 2016.
  - The post (paraphrased by the fetch tool, not a verbatim quotation) says AI tools make it easier to produce thin, narrow-scope papers, "salami" papers split from one piece of work, and dense AI-written papers.
  - From 1 Oct 2026, submitters may make at most two submissions per calendar month.
  - — [arXiv blog](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/)
- **[S] NIH notice NOT-OD-25-132 (17 Jul 2025).**
  - NIH cites AI tools having "enabled Principal Investigators to submit more than 40 distinct applications in a single application submission round".
  - Applications "substantially developed by AI" are not treated as original.
  - From 25 Sep 2025, NIH accepts at most six applications per PI per calendar year (T activity codes and R13 excepted).
  - — [NIH notice](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html)

**(c) Experiments on ideation and creativity** (LLM-generated ideas and lab tasks)
- **[N] Si, C., Yang, D. & Hashimoto, T. (2024).** Can LLMs generate novel research ideas? **[PREPRINT]** (arXiv; venue not verified here)
  - **Design.** 49 experts wrote ideas; 79 expert reviewers produced 298 reviews.
  - **Novelty.** AI ideas were rated more novel: 5.64 vs 4.84 on a 10-point scale (p < 0.01), though slightly weaker on feasibility.
  - **[S] Diversity.** Of 4,000 seed ideas generated per topic, only about **200 (≈5%) were non-duplicates**; "increasing the number of generated ideas simply leads to repeating duplicate ideas".
  - — [arXiv:2409.04109](https://arxiv.org/abs/2409.04109); [full text](https://arxiv.org/html/2409.04109v1)
- **[S] Si, C., Hashimoto, T. & Yang, D. (2025).** The ideation–execution gap. **[PREPRINT]**
  - 43 experts each spent more than 100 hours executing randomly assigned ideas.
  - After execution, scores for LLM ideas "decrease significantly more than expert-written ideas on all evaluation metrics" (p < 0.05). On many metrics the ranking flips in favour of human ideas.
  - — [arXiv:2506.20803](https://arxiv.org/abs/2506.20803)
- **[S] Liu, Z., Butler, K., Machlanski, D., Bueno, D. & Tsaftaris, S. A. (2026).** LLMs extend known research but do not create new research directions. **[PREPRINT]** (posted 12 Oct 2026)
  - Compares 26.9M human papers across 1,325 topics with 524,308 LLM hypotheses from eight models.
  - LLM ideas lie up to 16% further from existing work, but have a **15–23% lower median "orthogonal novelty score"**, a measure of new *direction*. They "move further from what is already known, but remain within established directions".
  - — [arXiv:2610.17439](https://arxiv.org/abs/2610.17439)
- **[S] Doshi, A. R. & Hauser, O. P. (2024).** Generative AI enhances individual creativity but reduces the collective diversity of novel content. *Science Advances* 10(28): eadn5290.
  - Access to AI ideas made stories more creative, especially for less creative writers.
  - But AI-enabled stories "are more similar to each other". The authors describe this as "a social dilemma".
  - — [DOI](https://doi.org/10.1126/sciadv.adn5290)
- **[S] Anderson, B. R., Shah, J. H. & Kreminski, M. (2024).** Homogenization effects of LLMs on human creative ideation. *Creativity & Cognition '24*, 413–425.
  - In a study of 36 participants, different users "produce less semantically distinct ideas with ChatGPT" than with an alternative creativity-support tool.
  - ChatGPT users produced more, and more detailed, ideas but "felt less responsible" for them.
  - — [DOI](https://doi.org/10.1145/3635636.3656204); [arXiv:2402.01536](https://arxiv.org/abs/2402.01536)
- **[S] Padmakumar, V. & He, H. (2024).** Does writing with language models reduce content diversity? (ICLR 2024)
  - Writing with InstructGPT, but not base GPT-3, significantly increased similarity between different authors' essays.
  - The effect came from model-contributed text.
  - — [arXiv:2309.05196](https://arxiv.org/abs/2309.05196)
- **[S] Meincke, L., Nave, G. & Terwiesch, C. (2025).** ChatGPT decreases idea diversity in brainstorming. *Nature Human Behaviour* 9(6): 1107–1109. — [DOI](https://doi.org/10.1038/s41562-025-02173-x)
  - Per the authors' institute summary: ChatGPT ideas were significantly less diverse in 37 of 45 comparisons, and in one task 94% of ChatGPT-assisted ideas shared overlapping concepts. This is a secondary summary; the paper's own metrics were not read. — [Wharton Mack Institute](https://mackinstitute.wharton.upenn.edu/2025/new-in-nature-chatgpt-decreases-idea-diversity-in-brainstorming/)
- **[N] Kumar, H., Vincentius, J., Jordan, E. & Anderson, A. (2025).** Human creativity in the age of LLMs (CHI 2025).
  - Two preregistered experiments with 1,100 participants.
  - LLM help boosts creativity while it is available but "may inadvertently hinder independent creative performance" afterwards.
  - — [DOI](https://doi.org/10.1145/3706598.3714198); [arXiv:2410.03703](https://arxiv.org/abs/2410.03703)
- **[N, weak] Kosmyna, N. et al. (2025).** Your brain on ChatGPT: accumulation of cognitive debt when using an AI assistant for essay writing. **[PREPRINT]** (v2, 31 Dec 2025; 216 pages)
  - **Design.** 54 participants in sessions 1–3, but only 18 completed session 4. EEG plus NLP analysis of essays.
  - **Findings.** LLM users showed the weakest brain connectivity and the lowest sense of ownership, and "struggled to accurately quote their own work". Within each group, essays showed homogeneity in named entities, n-grams and topics.
  - — [arXiv:2506.08872](https://arxiv.org/abs/2506.08872)
  - **Critique.** Stankovic et al. (2025) **[PREPRINT]** comment raises five concerns: "limited sample size", reproducibility of the analyses, "methodological issues related to the EEG analysis", "inconsistencies in the reporting of results", and "limited transparency". — [arXiv:2601.00856](https://arxiv.org/abs/2601.00856)
- **[N] Sourati, Z., Ziabari, A. S. & Dehghani, M. (2025).** The homogenizing effect of LLMs on human expression and thought. **[PREPRINT]**, review article. It synthesises evidence that LLMs "reflect and reinforce dominant styles". — [arXiv:2508.01491](https://arxiv.org/abs/2508.01491)

**(d) Evidence from other kinds of knowledge work** (closest causal designs)
- **[S] Yeverechyahu, D., Mayya, R. & Oestreicher-Singer, G.** The impact of LLMs on open-source innovation: evidence from GitHub Copilot. **[PREPRINT/WP]** (v4, May 2026)
  - **Natural experiment.** Copilot supported Python but not R.
  - **Result.** Contributions rose 28–40%. Incremental contributions rose significantly more than substantive ones in every specification, a gap that widened after a model upgrade.
  - **Interpretation.** LLMs "function more effectively when existing context helps define the problem", "tilting collaborative innovation toward exploitation of established codebases rather than exploration of new functionality".
  - — [arXiv:2409.08379](https://arxiv.org/abs/2409.08379); [SSRN DOI](https://doi.org/10.2139/ssrn.4684662)
- **[C] Hoffmann, M., Boysel, S., Nagle, F., Peng, S. & Xu, K. (2024).** Generative AI and the nature of work. **[WP]** (HBS Working Paper 25-021)
  - A regression-discontinuity design on Copilot access for open-source maintainers.
  - Developers shifted toward coding and away from project management.
  - The stated mechanisms are more autonomous work and "an increase in exploration activities rather than exploitation".
  - Funded in part by GitHub, and two authors are from Microsoft and GitHub.
  - This summary is based on search-result quotations of the abstract; I did not read the full text. — [SSRN DOI](https://doi.org/10.2139/ssrn.5007084); [Marginal Revolution summary](https://marginalrevolution.com/marginalrevolution/2024/11/generative-ai-and-the-nature-of-work.html)
- **[C] Dell'Acqua, F. et al. (2025).** The cybernetic teammate. NBER Working Paper w33641. **[WP]**
  - A field experiment with 776 Procter & Gamble professionals.
  - Individuals with AI matched teams without AI.
  - "AI breaks down functional silos": with AI, R&D and commercial staff produced "balanced solutions, regardless of their professional background".
  - — [DOI](https://doi.org/10.3386/w33641)
- **[N] Dell'Acqua, F. et al.** Navigating the jagged technological frontier. *Organization Science* (2026, per Semantic Scholar).
  - 758 consultants took part.
  - On tasks inside AI's capability frontier: 12.2% more tasks completed, 25.1% faster, higher quality.
  - On a task outside the frontier: 19% less likely to produce correct solutions.
  - — [DOI](https://doi.org/10.1287/orsc.2025.21838)
- **[N] Brynjolfsson, E., Li, D. & Raymond, L. (2025).** Generative AI at work. *QJE* 140(2): 889–942.
  - Among 5,172 customer-support agents, productivity rose 15%, with the largest gains for novices.
  - AI "improves English fluency, particularly among international agents".
  - — [DOI](https://doi.org/10.1093/qje/qjae044)

**(e) Evidence that AI can widen participation or support exploration**
- **[C, context] Amano, T. et al. (2023).** The manifold costs of being a non-native English speaker in science. *PLOS Biology* 21(7): e3002184.
  - A survey of 908 environmental scientists.
  - Non-native speakers spend more effort on reading, writing and presenting in English.
  - Language barriers deter them from attending or presenting at conferences.
  - — [DOI](https://doi.org/10.1371/journal.pbio.3002184)
- **[C]** In the LLM era, gains for non-English-speaking contexts appear in Filimonovic et al. (2025) and Zheng et al. (2026), above.
  - Safari & Babaei (2026) find the **opposite** sign for semantic novelty in non-English-dominant affiliations. — [arXiv:2603.22510](https://arxiv.org/abs/2603.22510)
- **[C] Ludwig, J. & Mullainathan, S. (2024).** Machine learning as a tool for hypothesis generation. *QJE* 139(2): 751–827.
  - A procedure for producing "novel, interpretable hypotheses" from high-dimensional data, applied to judges' jailing decisions.
  - It shows that AI can be built for exploration.
  - — [DOI](https://doi.org/10.1093/qje/qjad055)
- **[C/N] Sourati, J. & Evans, J. A. (2023).** Accelerating science with human-aware artificial intelligence. *Nature Human Behaviour* 7(10): 1682–1696.
  - AI that models the distribution of human expertise can target discoveries that existing communities are unlikely to reach.
  - The summary is from the earlier notes in this repository; only the DOI was re-verified.
  - — [DOI](https://doi.org/10.1038/s41562-023-01648-z)
- **[C, analogue] Jo, S., Jung, W.-S., Yoon, J. & Kim, H. (2025).** AI and market entrant game developers. **[PREPRINT]**
  - Using AI-disclosure statements on games, it finds that "relatively more independent developers entered the market" as generative AI became accessible.
  - This is an analogue for AI enabling entry into new areas.
  - — [arXiv:2509.14907](https://arxiv.org/abs/2509.14907)

### Inferences
**Scorecard**

| Kind of AI use | Evidence for exploitation | Evidence against | Verdict |
|---|---|---|---|
| AI as a research method (ML/DL) | Strongest: Hao; Bianchini preprint; Duede's "oil and water" | — | Mostly pre-ChatGPT |
| LLM-generated ideas | Strong: duplication and "hivemind"; ideas stay in established directions; scores fall after execution | Ideas are rated more novel before execution | — |
| Lab creativity tasks | Consistent: individual gain, loss of collective diversity | — | Tasks are not research choices |
| Individual scientists' LLM-era behaviour | Weak or indirect: Liang's "crowded areas" correlation; Safari's post-2022 decline; Bao's macro contraction | **Contrary**: Zheng et al. find more distant-field publishing and new-field entry; Kusumegi et al. find more diverse citing | Mixed |

- **The author's weakest point.** The best LLM-era within-person data (Zheng et al.) point toward *more* individual exploration. The best support for narrowing comes from AI-as-method (Hao) and from experiments.
- **Reconciling individual and collective results.** Individual exploration and collective contraction can coexist. If many scientists move into the *same* AI-amenable areas, each author's distance from their own earlier work rises while field-level diversity falls: individual exploration combined with collective herding. Zheng's "distant fields" and Hao's "toward areas richest in data" are compatible on this reading.
  - **Consequence for testing.** The hypothesis should be stated at the system level (March's sense of exploration), not as "scientists don't try new things".
  - **What to measure.** Designs should measure both distance-to-self and where movers land.
- **Two mechanisms besides incentives.** Both predict exploitation regardless of metric incentives:
  - **Technological affordance.** AI does best on well-posed, context-rich, data-rich problems (Copilot; the jagged frontier; Hao's data-availability result).
  - **Selection.** AI-heavy authors were already different before LLMs (Zheng; Liang's frequent preprinters).

  The *incentive* channel has only indirect support: Evans's "survival" framing; Liang's crowded-area and frequent-preprinter correlations; NIH's 40-application PIs; arXiv's account of "salami" papers; Bao et al.'s "prize probability over novelty". These show AI being used to produce *volume*, which is consistent with metric pressure, but none separates incentives from affordance.
- **The language-barrier dimension cuts both ways.** AI lowers the cost of entry for non-native speakers (Amano; Brynjolfsson; Filimonovic; Zheng). But Safari & Babaei find larger *semantic-novelty* declines for exactly these authors. Part of this may be measurement: LLM polishing pulls abstracts toward a common style (Lin & Zhu), which could compress embedding distances. See Q4.

### Gaps
- **Status of the key studies.** The key LLM-era studies are 2026 preprints (Zheng, Bao, Safari & Babaei, Liu, Renault). None was peer reviewed as of 15 Oct 2026.
- **Bianchini.** I could not confirm that the negative-novelty correlation in the 2020 preprint survives in the 2022 *Research Policy* version, whose abstract does not mention it.
- **Kusumegi breakdown.** I did not verify the breakdown of the 23.7–89.3% range by author background, such as non-native speakers.
- **Unverified details.**
  - Si et al. 2024: the publication venue.
  - Kosmyna et al.: participant population and task, beyond the abstract.
  - Hoffmann et al.: the exact definition of "exploration" (I saw summaries only).
  - Meincke et al.: the paper's own metrics (I relied on a secondary summary).
- **Missing evidence.** I found no study that measures generative-AI use for *research tasks* (ideation, analysis, coding) rather than writing, at scale and per author.
- **Not re-verified.** Toner-Rodgers' 2024 MIT preprint on AI in materials discovery, reportedly disowned by MIT in 2025, was not re-checked here. Do not cite it without checking its current status.

## 3. Theory: exploration versus exploitation, tradition and innovation, novelty and disruption

### Takeaway
**Core mechanism.** March (1991) supplies it: adaptive processes refine exploitation faster than exploration, which is "effective in the short run but self-destructive in the long run".

**Supporting work.** The science-of-science literature shows that:
- scientists' research strategies are conservative;
- short-window metrics and grant evaluators penalise novelty;
- the penalty for pivoting to new areas is large and growing.

Together these give the hypothesis a strong theoretical prior.

**Two cautions:**
- Journals' acceptance decisions *favour* novelty (Teplitskiy et al. 2022).
- The "declining disruption" result that often frames this debate is actively contested in *Nature* (2026 Matters Arising and Reply).

### Cited Findings
- **March, J. G. (1991).** Exploration and exploitation in organizational learning. *Organization Science* 2(1): 71–87. "Adaptive processes, by refining exploitation more rapidly than exploration, are likely to become effective in the short run but self-destructive in the long run." — [DOI](https://doi.org/10.1287/orsc.2.1.71)
- **Foster, J. G., Rzhetsky, A. & Evans, J. A. (2015).** Tradition and innovation in scientists' research strategies. *ASR* 80(5): 875–908.
  - Based on millions of MEDLINE abstracts.
  - "High-risk innovation strategies are rare and reflect a growing focus on established knowledge."
  - "An innovative publication is more likely to achieve high impact than a conservative one, but the additional reward does not compensate for the risk of failing to publish."
  - — [DOI](https://doi.org/10.1177/0003122415601618)
- **Rzhetsky, A., Foster, J. G., Foster, I. T. & Evans, J. A. (2015).** Choosing experiments to accelerate collective discovery. *PNAS* 112(47): 14569–14574.
  - Biomedical scientists pursue "conservative research strategies exploring the local neighborhood of central, important molecules".
  - Such strategies "probably serve scientific careers" but "slow scientific advance".
  - — [DOI](https://doi.org/10.1073/pnas.1509757112)
- **Uzzi, B., Mukherjee, S., Stringer, M. & Jones, B. (2013).** Atypical combinations and scientific impact. *Science* 342(6157): 468–472.
  - Covers 17.9M papers.
  - The highest-impact papers combine mostly conventional combinations of prior work with a dose of novel ones.
  - — [DOI](https://doi.org/10.1126/science.1240474)
- **Wang, J., Veugelers, R. & Stephan, P. (2017).** Bias against novelty in science. *Research Policy* 46(8): 1416–1436.
  - Covers about 1M articles.
  - Highly novel papers have "more than a triple probability" of being top-1% cited over a long window, with higher variance.
  - But they appear in journals with lower-than-expected impact factors and "are less cited when using a short time window".
  - Hence funding decisions based on short-term citations and impact factors "may be biased against novelty".
  - — [DOI](https://doi.org/10.1016/j.respol.2017.06.006) (abstract via [Semantic Scholar](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.respol.2017.06.006?fields=title,abstract))
- **Funk, R. J. & Owen-Smith, J. (2017).** A dynamic network measure of technological change. *Management Science* 63(3): 791–817.
  - Introduces the consolidation–destabilisation (CD) index.
  - Applied to university patents: "federal research funding pushes campuses to create inventions that are more destabilizing, deeper commercial ties lead them to produce technologies that consolidate the status quo."
  - This is evidence that incentive regimes shape whether outputs consolidate or disrupt.
  - — [DOI](https://doi.org/10.1287/mnsc.2015.2366)
- **Wu, L., Wang, D. & Evans, J. A. (2019).** Large teams develop and small teams disrupt science and technology. *Nature* 566: 378–382. Cited by title only. — [DOI](https://doi.org/10.1038/s41586-019-0941-9)
- **Leahey, E., Lee, J. & Funk, R. J. (2023).** What types of novelty are most disruptive? *ASR* 88(3): 562–597. "New methods tend to be more disruptive, whereas new theories tend to be less disruptive." — [DOI](https://doi.org/10.1177/00031224231168074)
- **Park, M., Leahey, E. & Funk, R. J. (2023).** Papers and patents are becoming less disruptive over time. *Nature* 613: 138–144. — [DOI](https://doi.org/10.1038/s41586-022-05543-x)
- **Critiques of Park et al. (2023) and the replies:**
  - **Petersen, A. M., Arroyave, F. & Pammolli, F. (2024)** argue the decline is an artefact of "citation inflation": longer reference lists and more self-citation make the measure drift toward zero over time. *QSS* 5(4): 936–953. — [DOI via arXiv metadata](https://doi.org/10.1162/qss_a_00333); [arXiv:2306.01949](https://arxiv.org/abs/2306.01949)
  - **The same authors, *J. Informetrics* 19(1): 101605 (2025)**, run a quasi-experiment comparing PNAS and PNAS Plus papers. In SciSciNet data, disruption "incrementally increased from 2005–2015". — [DOI](https://doi.org/10.1016/j.joi.2024.101605)
  - **Macher, J. T., Rutzer, C. & Weder, R. (2024).** *Research Policy* 53(5): 104992. "88 percent" of the patent CD decline over 1980–2010 is explained by truncating citations before 1976, and highly disruptive patents have *increased* since 1980. — [DOI](https://doi.org/10.1016/j.respol.2024.104992)
  - **Holst, V., Algaba, A., Tori, F., Wenmackers, S. & Ginis, V.** The 2024 preprint said dataset artefacts (entries with zero references) are "the hidden drivers" of the decline. It was published as a *Nature* Matters Arising with a softer title: "Dataset artefacts can partially drive the measured decline in disruption", *Nature* 656: E7–E13 (Aug 2026). — [arXiv:2402.14583](https://arxiv.org/abs/2402.14583); [DOI](https://doi.org/10.1038/s41586-026-10787-y)
  - **Park, Leahey & Funk, Reply.** *Nature* 656: E14–E21 (Aug 2026). The preprint version argues that Holst's data include about 20% non-research content, and that the decline "has been documented in nearly 100 studies". — [DOI](https://doi.org/10.1038/s41586-026-10788-x); [arXiv:2503.00184](https://arxiv.org/abs/2503.00184)
  - **Leibel, C. & Bornmann, L. (2024).** *Scientometrics* 129: 601–639. A review: disruption indices suffer "time-sensitive biases, and several data-induced biases". Variant DI5 shows higher convergent validity than the original DI1. More validation is needed before use in research evaluation. — [DOI](https://doi.org/10.1007/s11192-023-04873-5)
- **Incentives against exploration:**
  - **[S] Hill, R., Yin, Y., Stein, C., Wang, X., Wang, D. & Jones, B. F. (2025).** The pivot penalty in research. *Nature* 642: 999–1006. The impact of new work "steeply declines the further a researcher moves from their previous work". The penalty "has been growing in magnitude over the past five decades" and appears across fields, career stages and funding contexts, including COVID-19 pivots. — [DOI](https://doi.org/10.1038/s41586-025-09048-1); [Europe PMC](https://europepmc.org/article/MED/40437087)
  - **[S] Azoulay, P., Graff Zivin, J. & Manso, G. (2011).** *RAND J. Econ.* 42(3): 527–554. HHMI investigators (tolerance of early failure, long horizons) produce more high-impact papers than comparable NIH-funded scientists (short cycles, "unforgiving of failure"), and their research direction shifts toward "novel lines of inquiry". — [DOI](https://doi.org/10.1111/j.1756-2171.2011.00140.x)
  - **[S] Myers, K. (2020).** The elasticity of science. *AEJ: Applied* 12(4): 103–134. Inducing a scientist to change direction even slightly "requires a substantial amount of funding"; "the switching costs of science are large". — [DOI](https://doi.org/10.1257/app.20180518)
  - **[S] Boudreau, K. J., Guinan, E., Lakhani, K. R. & Riedl, C. (2016).** *Management Science* 62(10): 2765–2783. In a randomised evaluation of grant proposals (2,130 evaluator–proposal pairs), evaluators gave lower scores to "highly novel" proposals. — [DOI](https://doi.org/10.1287/mnsc.2015.2285)
  - **[S] Packalen, M. & Bhattacharya, J. (2020).** *PNAS* 117(22): 12011–12016. NIH has become "more conservative" in funding work that builds on the newest ideas. — [DOI](https://doi.org/10.1073/pnas.1910160117)
  - **[C] Teplitskiy, M., Peng, H., Blasco, A. & Lakhani, K. R. (2022).** *PNAS* 119(47): e2118046119. At Cell, Cell Reports and 47 IOP journals, "higher novelty is consistently associated with higher acceptance". The top novelty quintile is 6.5 percentage points more likely to be accepted, and editors "select strongly for novelty". — [DOI](https://doi.org/10.1073/pnas.2118046119)
  - **[S] Chu, J. S. G. & Evans, J. A. (2021).** *PNAS* 118(41): e2021636118. Across 1.8B citations to 90M papers, a "deluge of papers" leads to "ossification of canon". — [DOI](https://doi.org/10.1073/pnas.2021636118)
- **A historical precedent: online access narrowed citation.** **[S] Evans, J. A. (2008).** Electronic publication and the narrowing of science and scholarship. *Science* 321: 395–399. As journals came online, "fewer journals and articles were cited". Online search "may accelerate consensus and narrow the range of findings and ideas built upon". — [DOI](https://doi.org/10.1126/science.1150473)
- **Monoculture.** **Kleinberg, J. & Raghavan, M. (2021).** *PNAS* 118(22): e2018340118. When many actors use the same algorithm, decisions can get worse even if the algorithm is more accurate. — [DOI](https://doi.org/10.1073/pnas.2018340118)

### Inferences
- **The hypothesis in March's terms.** Generative AI lowers the cost of *exploitation* (writing up, extending and re-analysing work near existing expertise) more than the cost of *exploration*. Metrics that count outputs over short windows reward exactly that.
  - **The incentive gradient** comes from Wang et al. (short-window bias), Hill et al. (a large and growing pivot penalty), Boudreau et al. (evaluators penalise novelty) and Myers (high switching costs).
  - **That scientists respond to such gradients** is shown by Foster et al., Rzhetsky et al. and Azoulay et al.
  - **A precedent:** an efficiency technology once before narrowed what scientists build on (Evans 2008).
- **The main rival theory is technological affordance, not incentives.** AI works best where problems are well-posed and data-rich (Hao's data-availability result; Copilot; the jagged frontier), so it would produce exploitation even under neutral incentives.
  - **What separates the two theories is heterogeneity.** The incentive theory predicts a *stronger* link between AI and exploitation where metric pressure is high: untenured staff, publication-count regimes, short grant cycles. The affordance theory predicts a link that is uniform, or that varies with data richness.
  - **Funk & Owen-Smith and Azoulay et al.** show that incentive regimes do shift how consolidating and how novel outputs are. That makes the heterogeneity test plausible.
- **A third route: crowding.** AI-driven growth in output could ossify fields (Chu & Evans) even if each author explores. This is narrowing caused by the acceleration itself, through scarce attention. It fits the paper's wider "deluge" thesis but is a different mechanism from "scientists choose exploitation".
- **Don't present Park et al. as settled.** If it is used, cite the 2026 Matters Arising and Reply exchange.
- **Teplitskiy et al. limits the claim.** It weakens the claim that *all* evaluation penalises novelty. Where bias against novelty appears, it lies in short-window metrics and grant panels, which is precisely where AI-cheapened outputs are counted.

### Gaps
- **No formal model.** I found no formal model of how cheaper paper production changes the exploration–exploitation balance within a metric-driven career. Bao et al. (2026) include agent-based simulations, but I read only the abstract.
- **Pivot measure.** Hill et al.'s exact operationalisation of "pivot size" was not checked beyond the abstract.
- **Franzoni, Stephan & Veugelers (2022).** "Funding risky research", *Entrepreneurship and Innovation Policy and the Economy* 1: 103–133 ([DOI](https://doi.org/10.1086/719252)). Only the title and DOI were verified, not the content.

## 4. Measurement: AI use and exploration

### Takeaway
**Measuring AI use.** Every scalable measure of AI use detects *writing* assistance, mostly at population level. None observes AI used for research choices in individual papers. The measures are also biased or unstable in time:
- detectors misfire on non-native writers;
- authors adapt once marker words become known;
- dating adoption from the "first flagged paper" creates artefacts;
- disclosure statements are under-specified and skewed toward writing.

**Measuring exploration.** These measures are richer, but the text-based ones (embeddings of abstracts) may be compressed by the very LLM polishing under study. Reference-based measures and topic-entry measures are needed as cross-checks.

### Cited Findings
**Measuring AI use**
- **Excess vocabulary.**
  - **Kobak, D. et al. (2025).** *Science Advances* 11(27): eadt3813. Covers more than 15M PubMed abstracts from 2010–2024. "At least 13.5% of 2024 abstracts were processed with LLMs", reaching 40% in some subcorpora. — [DOI](https://doi.org/10.1126/sciadv.adt3813)
  - **Geng, M. & Trotta, R. (2024).** **[PREPRINT]** Covers 1M arXiv abstracts. About 35% of CS abstracts show LLM style, relative to a GPT-3.5 "revise the following sentences" baseline. — [arXiv:2404.08627](https://arxiv.org/abs/2404.08627)
- **Detector drift.** **Geng, M. & Trotta, R. (2025).** **[PREPRINT]** A "marked drop" in "delve" began soon after it was publicised in early 2024, while "significant" kept rising. Humans and LLMs "coevolve", which complicates detection. — [arXiv:2502.09606](https://arxiv.org/abs/2502.09606)
- **Distributional estimator.**
  - **Liang, W. et al. (2024, ICML).** **[conference paper]** A corpus-level maximum-likelihood estimator. It finds 6.5–16.9% of review text at four AI conferences substantially LLM-modified, with more such text near deadlines and in lower-confidence reviews. — [arXiv:2403.07183](https://arxiv.org/abs/2403.07183)
  - The NHB 2025 extension operates "on the corpus level", not on individual papers. — [arXiv:2404.01268](https://arxiv.org/abs/2404.01268); [DOI](https://doi.org/10.1038/s41562-025-02273-8)
- **Classifiers.**
  - **Bao, Sun & Teplitskiy (2025).** A classifier trained on pre- and post-ChatGPT "polished" abstracts outperformed GPTZero and ZeroGPT on validation sets, including papers with self-reported AI use. — [DOI](https://doi.org/10.1162/qss_a_00368)
  - **Lin & Zhu (2025).** Discipline-specific fine-tuned detectors. — [arXiv:2504.13629](https://arxiv.org/abs/2504.13629)
  - **Latona et al. (2024).** **[PREPRINT]** GPTZero gives a lower bound of 15.8% AI-assisted reviews at ICLR 2024. Borderline papers that received such a review were 4.9 percentage points more likely to be accepted. — [arXiv:2405.02150](https://arxiv.org/abs/2405.02150)
- **Detector bias.** **Liang, W., Yuksekgonul, M., Mao, Y., Wu, E. & Zou, J. (2023).** GPT detectors are biased against non-native English writers. *Patterns* 4(7): 100779. — [DOI](https://doi.org/10.1016/j.patter.2023.100779)
- **Timing artefact.** Renault et al. (2026): a first-detection adoption date is mechanically tied to output. — [arXiv:2605.17979](https://arxiv.org/abs/2605.17979)
- **Disclosure statements.**
  - **Ganjavi, C. et al. (2024).** *BMJ* 384: e077192. By Oct 2023, 87% of the top-100 journals and 24% of the top-100 publishers had guidance on generative AI. Almost all of them barred AI from authorship. — [DOI](https://doi.org/10.1136/bmj-2023-077192)
  - **Mohapatra, A. & Pruthi, D. (2026).** **[PREPRINT; accepted to EMNLP 2026 Findings]** CS venue policies "remain highly under-specified". In 13,867 disclosure statements from EMNLP 2025 and ICLR 2026, there is a "large disconnect" from what researchers expect: writing assistance, which researchers rate as least necessary to disclose, is disclosed often. — [arXiv:2608.23271](https://arxiv.org/abs/2608.23271)
  - **Ahmetoglu, Y. et al. (2026).** CHIWORK '26: disclosure statements "remain rare and inconsistent". — [arXiv:2604.02760](https://arxiv.org/abs/2604.02760)
- **AI as a method (keyword or classifier).** All three studies below (Hao, Bianchini, Duede) measure AI used as a method, not writing assistance.
  - Hao et al. use a BERT classifier trained on AI-venue papers (F1 = 0.875). — [arXiv v4 HTML](https://arxiv.org/html/2412.07727v4)
  - Bianchini et al. derive deep-learning search terms with NLP on arXiv. — [arXiv:2009.01575](https://arxiv.org/abs/2009.01575)
  - Duede et al. measure "AI engagement" across 20 fields. — [arXiv:2405.15828](https://arxiv.org/abs/2405.15828)
- **Detector-based prevalence at a venue: ICLR 2026.** Nature news reported Pangram's analysis. — [Naddaf, *Nature* news, 27 Nov 2025, DOI](https://doi.org/10.1038/d41586-025-03506-6)
  - Secondary coverage gives the figures. About 21% of 75,800 reviews (15,899) were flagged as fully AI-generated, and over half showed some AI involvement.
  - Of the papers, 199 (1%) were fully AI-written, and 9% had more than half AI text.
  - I could not open the Nature article; the figures are detector estimates. — [hyper.ai](https://hyper.ai/en/stories/267bbf4513e22ff5912134b478153928); [HowAIWorks](https://howaiworks.ai/blog/iclr-2026-ai-generated-peer-reviews-controversy)

**Measuring exploration**
- **Distance from the author's own earlier work:**
  - Hill et al. (2025): "pivot" size, measuring how far researchers move from their existing work. — [DOI](https://doi.org/10.1038/s41586-025-09048-1)
  - Zheng et al. (2026): publishing in "intellectually distant fields" and entering fields new to the author (OpenAlex). — [arXiv:2607.20923](https://arxiv.org/abs/2607.20923)
  - Myers (2020): change of topic in response to funding. — [DOI](https://doi.org/10.1257/app.20180518)
- **Embedding-based distance at the field level:**
  - Hao et al. (2026): "knowledge extent" and entropy in SPECTER 2.0 space. — [arXiv v4 HTML](https://arxiv.org/html/2412.07727v4)
  - Safari & Babaei (2026): SPECTER2 distance to nearest recent predecessors. — [arXiv:2603.22510](https://arxiv.org/abs/2603.22510)
  - Liu et al. (2026) separate *distance* from *direction* (their "orthogonal novelty score"); LLM ideas score high on distance but low on direction. — [arXiv:2610.17439](https://arxiv.org/abs/2610.17439)
- **Exploration strategy in knowledge networks.** Foster et al. (2015) classify strategies: introducing new chemicals or new relationships (innovation) versus deepening known ones (tradition), and bridging versus consolidating clusters. — [DOI](https://doi.org/10.1177/0003122415601618)
- **Atypical combinations and recombinant novelty:**
  - Uzzi et al. (2013): z-scores of pairs of cited journals. — [DOI](https://doi.org/10.1126/science.1240474)
  - Wang, Veugelers & Stephan (2017): first-ever combinations of cited journals, weighted by difficulty. — [DOI](https://doi.org/10.1016/j.respol.2017.06.006)
  - Fontana, Iori, Montobbio & Sinatra (2020): assess "new and atypical combinations" against novelty and interdisciplinarity. *Research Policy* 49(7): 104063. — [DOI](https://doi.org/10.1016/j.respol.2020.104063)
  - Bornmann, Tekles, Zhang & Ye (2019): validation of novelty indicators against F1000Prime. *J. Informetrics* 13(4): 100979; a corrigendum was published in 2024. — [DOI](https://doi.org/10.1016/j.joi.2019.100979); [corrigendum](https://doi.org/10.1016/j.joi.2024.101544)
  - Shibayama, Yin & Matsumoto (2021): word-embedding distance between cited references, validated against self-reported novelty. *PLOS ONE* 16(7): e0254034; a correction was published. — [DOI](https://doi.org/10.1371/journal.pone.0254034); [correction](https://doi.org/10.1371/journal.pone.0341474)
- **Novelty measured in the text itself.** Arts, S., Melluso, N. & Veugelers, R. (2025) use NLP to detect new ideas in publication text, validated on Nobel-winning papers versus review articles. *Review of Economics and Statistics*. — [DOI](https://doi.org/10.1162/rest_a_01561)
- **Disruption (CD index).** Funk & Owen-Smith (2017); the variant-choice advice of Leibel & Bornmann (2024); the time biases identified by Petersen et al. and Macher et al.; and Leahey et al.'s finding that new *methods* score as more disruptive. — see Q3
- **Interdisciplinarity:**
  - Stirling (2007), the general diversity framework (variety, balance, disparity). *J. R. Soc. Interface* 4(15): 707–719. — [DOI](https://doi.org/10.1098/rsif.2007.0213)
  - Porter & Rafols (2009), measuring and mapping interdisciplinarity in six fields over time. *Scientometrics* 81(3): 719–745. — [DOI](https://doi.org/10.1007/s11192-008-2197-2)
  - Leydesdorff, Wagner & Bornmann (2019), Rao–Stirling diversity versus relative variety and the Gini coefficient. *J. Informetrics* 13(1): 255–269. — [DOI](https://doi.org/10.1016/j.joi.2018.12.006)
- **A new outcome: the share of null claims.** Bao et al. (2026) report null claims "sharply suppressed" after ChatGPT. — [arXiv:2606.08251](https://arxiv.org/abs/2606.08251)

### Inferences
- **Use three kinds of exploration measure, not one:**
  1. **Distance from the author's own earlier work.** Measure it with SPECTER2 distance from the centroid of the author's pre-period papers, the change in reference profile (pivot), and the number of topics and fields new to the author.
  2. **Novelty against the field.** Measure it with atypical or first-ever reference combinations, novelty in the text itself, and Liu et al.'s *direction* score.
  3. **Diversity of the whole system.** Measure it with knowledge extent and entropy (as in Hao), Rao–Stirling diversity, and how concentrated citations are.

  The hypothesis predicts falls in (3) and in (1) per unit of output. Zheng-type results show (1) can rise while (3) falls.
- **Text-based outcomes may be contaminated by the treatment.** LLM polishing makes texts converge (Lin & Zhu; Padmakumar & He), so distances between abstract embeddings can shrink mechanically after 2022 even if the science is unchanged. This threatens Safari & Babaei and any GAI-era extension of Hao.
  - **Remedy: a "paraphrase calibration".** Pass a random sample of pre-2022 abstracts through a standard "polish" prompt (as in Geng & Trotta's baseline) and measure how far the novelty and distance metrics move. Use measures based on reference lists as the primary outcomes.
- **Measuring AI use** (no single measure suffices):
  1. **Author-level marker scores** computed on a *fixed* set of papers (for example, the share of an author's 2023–24 papers above a threshold), not the date of the first flag, which follows Renault et al.'s critique.
  2. **Disclosure statements** where they are mandatory (ICLR 2026, EMNLP 2025). They should be coded by task (writing, coding, ideation), given Mohapatra & Pruthi's finding that disclosures over-represent writing.
  3. **Exposure proxies that do not come from the author's own text.** Geographic restrictions are weak instruments: Bao et al. found restricted countries used ChatGPT *more*.
- **The detector bias against non-native writers matters here.** The treatment measure is then correlated with language background, which also predicts both the size of the AI benefit (Filimonovic) and changes in measured novelty (Safari & Babaei). Stratify by language context, or condition on it.
- **CD index.** If used, prefer DI5-type variants, restrict to research articles, fix the citation window, and compare within cohorts. The new-method effect (Leahey et al.) means AI-*method* papers may look "disruptive" even when their topic is exploitation.

### Gaps
- **No ground truth.** There is no validated per-paper ground truth for LLM use in research tasks other than writing.
- **Disclosure rules after 2023.** I did not verify current disclosure mandates at specific publishers (Elsevier, Springer Nature, Science) after Ganjavi et al.'s October 2023 snapshot.
- **OpenAlex topics.** I did not verify the current OpenAlex "Topics" taxonomy, which would be used for new-to-author topics, or how stable it is over time.

## 5. Research designs using open data, threats to validity, and whether anyone has run them

### Takeaway
Three designs are feasible now with open data:
- **(A)** a within-author difference-in-differences;
- **(B)** a field-level dose-response event study;
- **(C)** a study of submissions and evaluation at venues whose submissions are public.

Parts of each have already been run (Kusumegi; Zheng; Filimonovic; Safari & Babaei; Bao et al.; Hao). None yet combines adoption timing that is independent of output, exploration outcomes based on reference lists, and a test of the incentive *mechanism*. The decisive missing test is **heterogeneity by incentive intensity** (a triple difference). Without it, even a clean narrowing result cannot separate "metric incentives" from "AI works best on data-rich, well-posed problems".

### Cited Findings
- **OpenAlex access.** The claim that "OpenAlex needs an API key since 2026" needs nuance.
  - **API.** The current help page says "you can make basic queries with no key at all". A free key "raises your daily budget 10×", to $1 a day, and is required for cursor paging beyond the first page. Per-second limits are 10 requests without a key and 30 with a free key. — [OpenAlex authentication](https://help.openalex.org/api-reference/authentication)
  - **My test.** A keyless single-record API call on 2026-10-15 returned HTTP 200.
  - **Snapshot.** The full snapshot is free, "no AWS account needed", in `s3://openalex`, updated "quarterly … on the second Wednesday of January, April, July and October". — [OpenAlex snapshot](https://help.openalex.org/download-all-data/openalex-snapshot)
- **Semantic Scholar.** It provides "SPECTER2 embeddings" and the free S2AG bulk dataset. Unauthenticated requests are limited to 1,000 per second, shared among all unauthenticated users. — [Semantic Scholar API](https://www.semanticscholar.org/product/api)
- **Feasibility precedents** using open corpora:
  - PubMed: 15M abstracts. — [Kobak](https://doi.org/10.1126/sciadv.adt3813)
  - PubMed Central full text with CRediT statements, linked to OpenAlex. — [Zheng](https://arxiv.org/abs/2607.20923)
  - arXiv, bioRxiv and medRxiv preprints. — [Bao, Sun & Teplitskiy](https://doi.org/10.1162/qss_a_00368)
  - arXiv, bioRxiv and Nature portfolio. — [Liang 2025](https://doi.org/10.1038/s41562-025-02273-8)
  - 41.3M OpenAlex natural-science papers. — [Hao](https://arxiv.org/html/2412.07727v4)
- **arXiv rule changes** (each is a structural break in the data):
  - **31 Oct 2025.** CS review/survey and position papers must first be accepted at a peer-reviewed journal or conference; workshop review does not count. The stated reason is the "unmanageable influx" of such papers and "hundreds of review articles every month". — [arXiv blog](https://blog.arxiv.org/?p=1740); date per [Decrypt](https://decrypt.co/347196/arxiv-blocks-ai-generated-survey-papers-flood-trashy-submissions)
    - **Effect on the data** (Elazar & Antoniak 2026, **[PREPRINT]**). The policy hits subfields unevenly: "Computers & Society potentially facing cuts of 50%". Non-review LLM-generated papers are estimated to be almost 6× more numerous than review ones. — [arXiv:2601.17036](https://arxiv.org/abs/2601.17036)
  - **May 2026.** A "one-strike" one-year ban for "incontrovertible evidence that the authors did not check the results of LLM generation", such as hallucinated references or leftover prompts. After a ban, submissions must first be accepted at a peer-reviewed venue. — [TechCrunch, 16 May 2026](https://techcrunch.com/2026/05/16/research-repository-arxiv-will-ban-authors-for-a-year-if-they-let-ai-do-all-the-work)
  - **1 Oct 2026.** At most two submissions per submitter per calendar month, across all categories. The limit of three active submissions has applied since 2024. Rejected submissions count. — [arXiv blog](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/)
  - **Endorsement tightening and a full-English-version requirement** are reported only by a secondary source and were not verified. — [CASRAI](https://casrai.org/news/arxiv-2026-endorsement-english-ai-policy-changes)
- **Conference data and randomisation precedents:**
  - ICLR 2025 ran a randomised trial of an LLM "Review Feedback Agent" on more than 20,000 reviews; 27% of reviewers who received feedback updated their reviews. — [Thakkar et al. 2025, arXiv:2504.09737](https://arxiv.org/abs/2504.09737) **[PREPRINT]**
  - Matched analysis of AI-assisted reviews at ICLR 2024. — [Latona et al.](https://arxiv.org/abs/2405.02150)
  - Disclosure statements from ICLR 2026 and EMNLP 2025 have already been analysed. — [Mohapatra & Pruthi](https://arxiv.org/abs/2608.23271)
- **Grants.** NIH applications are not public, but NIH has documented AI-enabled mass submission (more than 40 applications in a round) and capped PIs at six per year from 25 Sep 2025. — [NIH NOT-OD-25-132](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html)
- **Shocks inside the pre-period.** Hill et al. document large COVID-19 pivots and their penalties. — [DOI](https://doi.org/10.1038/s41586-025-09048-1)

### Inferences

#### Design A: within-author difference-in-differences around Nov 2022, with LLM-use intensity as treatment and exploration as outcome
- **Sample.**
  - Disambiguated authors (OpenAlex snapshot; Semantic Scholar author IDs as a robustness check) with at least five papers in a clean baseline of 2016–2019.
  - Treat 2020–22 separately because of COVID pivots.
  - Use corpora less exposed to arXiv's 2025–26 rule changes: PubMed/PMC and journal-indexed OpenAlex works, with arXiv as a secondary corpus. End the window before Oct 2026, or model the cap explicitly.
- **Treatment intensity.**
  - The share of the author's papers in a *fixed* window (for example, the first k papers after Mar 2023) whose marker or classifier score exceeds a threshold. This should be scored with a detector validated separately for non-native writers.
  - Use disclosure statements where they exist.
  - **Avoid first-detection timing** (Renault et al.). Use continuous intensity × post with author fixed effects and field × year fixed effects.
- **Outcomes, per author-year:**
  - SPECTER2 distance of new papers from the author's 2016–19 centroid (mean and 90th percentile);
  - the number and share of OpenAlex topics and subfields new to the author;
  - the change in reference profile (pivot) relative to the author's own baseline;
  - atypical-combination z-scores (Uzzi) and first-ever journal pairs (Wang et al.);
  - Rao–Stirling diversity of references;
  - the share of papers *about* LLMs, handled separately (see threats).
- **Prediction if the hypothesis holds.** Output rises, but distance-to-self and new-topic counts *per unit of output* fall or stay flat, and system-level diversity falls.
- **Mechanism test (triple difference).** Interact intensity with measures of incentive pressure:
  - career stage (before or after first last-author paper, as a proxy for tenure);
  - national or institutional evaluation regimes that count publications (the regimes are documented in earlier note 1 in this repository, *AI disruption of academia literature*);
  - funder type, using funder IDs in OpenAlex or Crossref, with long-horizon HHMI-type funders against short-cycle grants (Azoulay et al.);
  - field crowding (Liang).

  The incentive hypothesis predicts larger effects under higher pressure. The affordance hypothesis predicts effects that track data availability instead.
- **Threats to validity:**
  - **Selection.** Heavy AI users were already more exploratory (Zheng) and post more preprints (Liang). Use matching on pre-trends and event-study plots, and treat results as associations unless an exposure shock exists.
  - **Detector error.** Detectors are biased toward flagging non-native writers (Liang 2023), drift as authors avoid "delve" (Geng & Trotta 2025), and capture writing, not research use.
  - **Timing artefact.** Adoption dated from detection is mechanically tied to output (Renault et al.).
  - **Productivity confound.** More papers from the same expertise lower the per-paper average distance mechanically. Report both intensive measures (per paper) and extensive ones (per author-year, frontier distance, count of new topics), and normalise by output.
  - **Text compression.** LLM polishing shrinks embedding distances. Run the paraphrase calibration and use reference-based outcomes as primary.
  - **Shocks.** COVID pivots, and "LLMs as a research topic" (many authors newly *study* LLMs, which reads as exploration). Exclude or flag papers whose subject is AI.
  - **Platform rules.** arXiv's Oct 2025 CS review rule, May 2026 bans and Oct 2026 two-a-month cap change which papers are posted, especially for heavy AI users, so attrition differs between groups.
- **Has it been run? Partly.**
  - Kusumegi et al. (2025): within-author event study. Outcomes are output, citation diversity and access. The design is challenged by Renault et al.
  - Filimonovic et al. (2025): difference-in-differences on output and journal impact factor.
  - Zheng et al. (2026): exploration and interdisciplinarity, stratified by AI-writing signal. It **found increases**, but is descriptive or correlational.
  - Lin & Zhu (2025): difference-in-differences on writing convergence.
  - **Not found:** a preregistered within-author difference-in-differences with exposure timing independent of output, exploration outcomes based on reference lists, and an incentive-heterogeneity test.

#### Design B: field-level event study / dose–response (fields with high vs low LLM uptake)
- **Units.** OpenAlex subfields, arXiv categories or MeSH areas × quarter, 2016–2026.
- **Exposure.**
  - Field-level LLM-modification share from the Liang estimator or Kobak's excess-word lower bound, estimated on a held-out random half of the field's papers so the exposure is not computed from the same texts as the outcome.
  - Or *predicted* exposure from pre-2022 field traits, such as the share of authors from non-English-dominant countries (Safari & Babaei's contrast) or the field's preprint intensity.
- **Outcomes.**
  - Hao-style knowledge extent and entropy;
  - the rate of new topic or concept "births";
  - the share of papers with atypical reference combinations;
  - Rao–Stirling diversity;
  - concentration of citations in already-cited work (Chu & Evans);
  - the share of null claims (Bao et al. 2026);
  - DI5-type disruption within cohorts.
- **Identification.**
  - Pre-trends over 2016–2022; dose–response in uptake; placebo break dates (for example, Nov 2020).
  - Control for growth in field output, because crowding narrows fields by itself (Chu & Evans).
  - Separate entry by new authors from changes among incumbents.
- **Threats to validity:**
  - Field-specific shocks: the AI-topic boom, COVID, funding changes.
  - Composition: new entrants, and arXiv's rule changes reshaping CS subfields (Elazar & Antoniak).
  - Text compression.
  - Ecological inference: a field-level association does not tell us *who* narrows.
- **Has it been run? Partly.**
  - Hao et al.: AI-method papers vs non-AI papers by field, with the generative-AI era "preliminary".
  - Bao et al. (2026): 39M papers from 2010–2025; post-ChatGPT contraction and suppression of null claims, apparently a before/after pattern rather than dose–response by uptake (abstract only).
  - Safari & Babaei (2026): one field (IS), with language context as a proxy for exposure. The authors say explicitly that this is not an estimate of an adoption effect.
  - Liang et al. (2025) supply exposures by field.
  - **Not found:** a multi-field dose–response event study that links measured LLM uptake to topic-space outcomes, with pre-trends and placebo dates.

#### Design C: submissions and evaluation at venues whose submissions are public (OpenReview), plus a grant-policy natural experiment
- **Data.**
  - ICLR 2024–2026 on OpenReview: all submissions including rejected ones, reviews, scores and decisions.
  - ICLR 2026 and EMNLP 2025 AI-use disclosure statements, coded by task.
  - Detector scores (Pangram-style, with known accuracy disputes).
  - Authors' histories from Semantic Scholar or OpenAlex.
- **Tests.**
  1. Are AI-assisted submissions (disclosure or detection) closer to their authors' own earlier work than non-assisted ones, within author and topic?
  2. **The incentive channel at the evaluation stage.** Is the score penalty for exploratory submissions (large distance from the author's own work; atypical references) larger or smaller for AI-assisted submissions, and for submissions that received AI-assisted reviews? If evaluation rewards incremental AI-assisted work more, that directly supports "metric incentives channel AI into exploitation".
- **Randomised extension.** Partner with a venue (precedent: the ICLR 2025 trial of review feedback) to randomise an ideation or "exploration" aid, or a structured disclosure form, and track the novelty of later submissions.
- **Grant arm.** NIH's six-application cap from 25 Sep 2025 is a natural experiment on volume incentives. Compare PIs who submitted many applications before the cap with others, before and after, on the distinctiveness of the projects they win. NIH RePORTER covers funded awards only, so results are selected on success.
- **Threats to validity:**
  - Results come from ML/NLP only, so they may not generalise.
  - Disclosures are under-specified and socially desirable answers are likely (Mohapatra & Pruthi; Ahmetoglu et al.).
  - Detector accuracy is disputed.
  - Venue AI policies changed between years.
  - Reviewers' own AI use (Latona; Liang 2024) contaminates the outcome.
  - The productivity confound reappears as many submissions per author.
- **Has it been run? Partly.**
  - Prevalence of AI in reviews and papers: Liang 2024; Latona 2024; the Pangram analysis of ICLR 2026.
  - Disclosure content: Mohapatra & Pruthi 2026.
  - Randomised trial of LLM review feedback: Thakkar et al. 2025.
  - **Not found:** any study linking AI use at the submission level to exploration relative to the author's own earlier work, and to evaluation outcomes.

#### Cross-cutting recommendations
- Pre-register the analyses, and use placebo cut-offs before Nov 2022.
- Make outcomes based on reference lists primary, and calibrate text-based measures with the paraphrase test.
- Report results per paper *and* per author-year.
- Separate AI as the *topic* of a paper from AI as a *tool*.
- Treat the language background of authors as a moderator, not noise.

#### Draft text box (≈350 words)

> **Box 4.x — How this hypothesis could be tested**
>
> We claim that metric incentives channel generative AI into exploitation: scientists use it to do faster what they already know how to do, not to explore unfamiliar questions. Hao et al. (2026) are consistent with this but cannot settle it. Their "AI" is mostly machine learning used as a method, studied largely before ChatGPT. Their contraction compares AI papers with other papers rather than following scientists over time. And in their data, data availability rather than incentives best predicts where AI concentrates. The claim makes three testable predictions.
>
> *Within scientists:* after adopting generative AI, a scientist's output should grow faster than its distance from that scientist's earlier work. A difference-in-differences around November 2022 could test this, using OpenAlex or Semantic Scholar publication histories. It would measure each new paper's distance from the author's earlier papers through reference lists, embeddings and topics new to the author. Adoption must be measured independently of output: dating it from the first AI-flagged paper creates spurious effects (Renault et al. 2026).
>
> *Across incentive regimes:* if incentives rather than the technology drive narrowing, the link between AI use and exploitation should be stronger where counting is harsher, such as untenured researchers, publication quotas and short grant cycles. It should be weaker under long-horizon funding of the kind that encourages exploration (Azoulay et al. 2011). This comparison separates our claim from the rival view that AI simply works best on data-rich, well-posed problems.
>
> *In evaluation:* venues that publish every submission with its reviews and AI disclosures, such as ICLR, can show whether AI-assisted incremental work is rewarded more than exploratory work.
>
> The hypothesis is falsifiable. It would be weakened if AI users moved further from their earlier work than comparable non-users, and early evidence points that way. Zheng et al. (2026) report more entry into new fields after 2022, and Kusumegi et al. (2025) find that adopters cite more diverse literature. Measurement is treacherous. LLM polishing makes abstracts more alike and so mimics narrowing. Detectors misclassify non-native writers. arXiv's 2025–26 rules (a peer-review requirement for CS reviews and a cap of two submissions a month) change who appears in the data. Credible tests should therefore be preregistered, rely on reference-based outcomes and include placebo dates before 2022.

### Gaps
- **How "new" the designs are.** I searched arXiv and the web for designs A–C. Very recent or non-English work may be missing, so "not found" means not found in these searches, not "does not exist".
- **OpenAlex key timing.** I could not establish the exact date when OpenAlex introduced keyed budgets. The help page carries no start date.
- **Unverified arXiv details.** arXiv's endorsement and English-language changes are known only from a secondary source. Whether the May 2026 ban rule covers all categories or only CS was not stated in the source I read.
- **ICLR 2026 figures.** These come from secondary coverage of Pangram's analysis. The *Nature* news article and Pangram's own post were not opened.
- **Data that could not be checked or does not exist.** NIH RePORTER access details were not checked in this session. No open data on *unfunded* grant applications was found.
