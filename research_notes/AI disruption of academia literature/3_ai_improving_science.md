# AI as a means to improve science: information overload, interdisciplinarity, discovery (Section 3)

Verification note: every DOI below was resolved against the Crossref API (title, venue, year, authors, volume/pages checked) or, for preprints, against the arXiv abstract page, on 2026-10-15. Company blogs/white papers are labelled **[non-peer-reviewed]**. "Stance" = relation to the thesis "AI disrupts the current academic system but could help build better science": **Supports / Nuances / Challenges**.

## 1. Information overload, the "burden of knowledge" and barriers to interdisciplinarity

### Takeaway
A well-established science-of-science literature shows that knowledge growth forces narrower specialisation, larger teams and slower canonical progress, and that interdisciplinary work is penalised by funding systems. Together these define the problem that AI literature tools are claimed to solve.

### Cited Findings (annotated bibliography)
- **Jones, B. F. (2009). The burden of knowledge and the "death of the Renaissance man": Is innovation getting harder? *Review of Economic Studies*, 76(1), 283–317. https://doi.org/10.1111/j.1467-937X.2008.00531.x** — As the stock of knowledge grows, innovators need more education and specialise more narrowly. This shows up as later age at first invention, narrower expertise and more teamwork. **Supports** (states the problem AI could ease). — [Crossref/DOI](https://doi.org/10.1111/j.1467-937X.2008.00531.x)
- **Wuchty, S., Jones, B. F., & Uzzi, B. (2007). The increasing dominance of teams in production of knowledge. *Science*, 316(5827), 1036–1039. https://doi.org/10.1126/science.1136099** — Teams increasingly dominate the production of papers and patents and produce the most highly cited work. This is consistent with the "burden of knowledge" pushing towards collaboration. **Supports** (background). — [DOI](https://doi.org/10.1126/science.1136099)
- **Bromham, L., Dinnage, R., & Hua, X. (2016). Interdisciplinary research has consistently lower funding success. *Nature*, 534, 684–687. https://doi.org/10.1038/nature18315** — In Australian Research Council proposals, the more interdisciplinary the project, the lower its probability of being funded. This is evidence that institutions, not only cognitive limits, block interdisciplinarity. **Supports / Nuances**: it implies that AI cannot fix interdisciplinarity without incentive reform. — [DOI](https://doi.org/10.1038/nature18315)
- **Bornmann, L., & Mutz, R. (2015). Growth rates of modern science: A bibliometric analysis based on the number of publications and cited references. *JASIST*, 66(11), 2215–2222. https://doi.org/10.1002/asi.23329** — Reports roughly exponential growth of the scientific literature. The commonly cited figure is about 4% a year, which means output doubles roughly every 17 years (check the exact rate against the paper). Standard quantitative anchor for "information overload". **Supports** (problem framing). — [DOI](https://doi.org/10.1002/asi.23329)
- **Chu, J. S. G., & Evans, J. A. (2021). Slowed canonical progress in large fields of science. *PNAS*, 118(41), e2021636118. https://doi.org/10.1073/pnas.2021636118** — In very large fields, the flood of papers makes new ideas less likely to break through, and citations concentrate on already-canonical works. This is the direct link between overload and stagnation. **Supports** (problem). It also **Nuances**: more AI-boosted output could worsen the deluge. — [DOI](https://doi.org/10.1073/pnas.2021636118)
- **Park, M., Leahey, E., & Funk, R. J. (2023). Papers and patents are becoming less disruptive over time. *Nature*, 613, 138–144. https://doi.org/10.1038/s41586-022-05543-x** — The CD index of disruptiveness has fallen across fields since 1945. The authors link this partly to scientists relying on narrower slices of existing knowledge. **Supports** (problem framing). — [DOI](https://doi.org/10.1038/s41586-022-05543-x)
- **Bloom, N., Jones, C. I., Van Reenen, J., & Webb, M. (2020). Are ideas getting harder to find? *American Economic Review*, 110(4), 1104–1144. https://doi.org/10.1257/aer.20180338** — Research productivity, measured as output per researcher, is falling sharply across many domains. This is the macro version of the burden-of-knowledge argument. **Supports** (problem). — [DOI](https://doi.org/10.1257/aer.20180338)
- **Fortunato, S., Bergstrom, C. T., Börner, K., Evans, J. A., Helbing, D., Milojević, S., et al. (2018). Science of science. *Science*, 359(6379), eaao0185. https://doi.org/10.1126/science.aao0185** — Review of the quantitative study of science, covering team science, citation dynamics and interdisciplinarity. Useful framing reference. **Neutral / background**. — [DOI](https://doi.org/10.1126/science.aao0185)

### Inferences
- The problem framing (overload, then specialisation, then teams, then stagnation and lower disruptiveness) is robust and well cited. However, Bromham et al. show that some barriers are institutional, such as funding panels. This supports the position paper's argument that AI must come together with academic reform.
- Chu & Evans imply a paradox: if AI raises paper output without raising attention capacity, it may worsen the "deluge" problem it promises to solve.

### Gaps
- I did not fetch Bornmann & Mutz's full text in this session, so the exact growth-rate figure should be checked against the paper before quoting it.

## 2. Literature-based discovery and AI-assisted literature review/synthesis tools: accuracy and hallucinated citations

### Takeaway
Swanson's literature-based discovery (LBD) is the classic precedent. Modern retrieval-augmented systems (OpenScholar, PaperQA2) now report citation accuracy comparable to experts, while general-purpose LLMs fabricate many citations. Independent, field-wide evaluations of commercial tools such as Elicit and Consensus remain thin.

### Cited Findings (annotated bibliography)
- **Swanson, D. R. (1986). Fish oil, Raynaud's syndrome, and undiscovered public knowledge. *Perspectives in Biology and Medicine*, 30(1), 7–18. https://doi.org/10.1353/pbm.1986.0087** — The founding LBD paper. It linked two literatures that did not cite each other ("undiscovered public knowledge") to hypothesise that fish oil could treat Raynaud's syndrome. This is the classic argument that synthesis across fragmented literatures can itself produce discoveries. **Supports** (essential classic). — [DOI](https://doi.org/10.1353/pbm.1986.0087)
- **Smalheiser, N. R., & Torvik, V. I. (2008). The place of literature-based discovery in contemporary scientific practice. In *Literature-based Discovery* (Information Science and Knowledge Management), pp. 13–22. Springer. https://doi.org/10.1007/978-3-540-68690-3_2** — Reflects on why LBD remained marginal in practice despite its promise. **Nuances**: the tools existed but adoption and validation lagged. — [DOI](https://doi.org/10.1007/978-3-540-68690-3_2)
- **Asai, A., He, J., Shao, R., Shi, W., Singh, A., Chang, J. C., Lo, K., Soldaini, L., … Hajishirzi, H. (2026). Synthesizing scientific literature with retrieval-augmented language models. *Nature*, 650, 857–863. https://doi.org/10.1038/s41586-025-10072-4** (OpenScholar; published 4 Feb 2026; arXiv 2024). Key points:
  - **System:** an open retrieval-augmented model over about 45 million open-access papers.
  - **Fabricated citations:** GPT-4o fabricated citations in 78–90% of cases.
  - **OpenScholar's citation accuracy:** reported to be on par with human experts.
  - **Correctness:** OpenScholar-8B beat GPT-4o by 6.1% and PaperQA2 by 5.5% on multi-paper synthesis.
  - **Benchmark:** introduces ScholarQABench, with 2,967 expert queries across computer science, physics, neuroscience and biomedicine.
  - **Authors' caveat:** full automation of literature synthesis is not yet possible.

  **Supports** (with explicit caveats). — [Crossref/DOI](https://doi.org/10.1038/s41586-025-10072-4); [UW news](https://www.washington.edu/news/2026/02/04/in-a-study-ai-model-openscholar-synthesizes-scientific-research-and-cites-sources-as-accurately-as-human-experts/); [Nature Asia press release](https://www.natureasia.com/en/info/press-releases/detail/9228)
- **Skarlinski, M. D., Cox, S., Laurent, J. M., Braza, J. D., et al. (2024). Language agents achieve superhuman synthesis of scientific knowledge. arXiv:2409.13740. https://arxiv.org/abs/2409.13740** (PaperQA2, FutureHouse; **preprint, not peer-reviewed**) — An agent for literature QA, summarisation and contradiction detection. The authors claim it matches or exceeds PhD/postdoc experts on retrieval and summarisation tasks. The "superhuman" framing is the authors' own and should be treated with caution. **Supports**. — [arXiv](https://arxiv.org/abs/2409.13740)
- **Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. *Scientific Reports*, 13, 14045. https://doi.org/10.1038/s41598-023-41032-5** — Systematic check of citations in ChatGPT-generated literature reviews. A substantial share were fabricated, especially with GPT-3.5, and many of the real ones contained errors; GPT-4 did better but was still flawed. **Challenges** the naive use of general chatbots for literature work. — [DOI](https://doi.org/10.1038/s41598-023-41032-5)

### Inferences
- The evidence splits by architecture. General LLMs without retrieval are unreliable for citations (Walters & Wilder; Asai et al.'s 78–90% figure). Retrieval-grounded systems built specifically for science approach expert-level citation accuracy on curated benchmarks. That is a benchmark result, not proof of field-wide reliability.
- Swanson-style "undiscovered public knowledge" is the conceptual bridge between "managing overload" and "enabling interdisciplinarity". Retrieval-augmented systems are its modern descendants.

### Gaps
- **Commercial tools.** I found no independent peer-reviewed evaluation of Elicit, Consensus or Semantic Scholar's AI features within the tool budget of this session. The report writer should not cite accuracy figures for these tools unless a further search finds them. Semantic Scholar is mainly relevant as the open corpus behind tools such as OpenScholar, and no dedicated citation was verified here.
- **Systematic-review automation.** Studies comparing LLM screening with human screening were not covered.

## 3. AI-driven discovery: flagship cases and a cautionary tale

### Takeaway
AlphaFold is the clearest validated success: a peer-reviewed paper followed by a Nobel Prize. Agentic "AI scientist" systems (Google co-scientist, FutureHouse Robin, Sakana AI Scientist, AlphaEvolve) show real but narrow, mostly preclinical or computational results, often reported through company channels. The Toner-Rodgers case shows how hype about AI-accelerated discovery can outrun verification.

### Cited Findings (annotated bibliography)
- **Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M., Ronneberger, O., et al. (2021). Highly accurate protein structure prediction with AlphaFold. *Nature*, 596, 583–589. https://doi.org/10.1038/s41586-021-03819-2** — Near-experimental accuracy in protein structure prediction at CASP14. In 2024 Hassabis and Jumper shared half of the Nobel Prize in Chemistry "for protein structure prediction"; the other half went to David Baker for computational protein design. The nobelprize.org press release could not be fetched in this session (HTTP 403), so the citation rests on the public record. **Supports** (strongest exemplar). — [DOI](https://doi.org/10.1038/s41586-021-03819-2); [Nobel press release](https://www.nobelprize.org/prizes/chemistry/2024/press-release/)
- **Wang, H., Fu, T., Du, Y., Gao, W., Huang, K., Liu, Z., et al. (2023). Scientific discovery in the age of artificial intelligence. *Nature*, 620, 47–60. https://doi.org/10.1038/s41586-023-06221-2** — Broad review of how AI helps with hypothesis generation, experimental design, data collection and analysis. It also covers challenges: data quality, generalisation and interpretability. **Supports / Nuances**. — [DOI](https://doi.org/10.1038/s41586-023-06221-2)
- **Krenn, M., Pollice, R., Guo, S. Y., Aldeghi, M., Cervera-Lierta, A., Friederich, P., et al. (2022). On scientific understanding with artificial intelligence. *Nature Reviews Physics*, 4, 761–769. https://doi.org/10.1038/s42254-022-00518-3** — Separates AI as a "computational microscope", AI as a "resource of inspiration" and AI as an "agent of understanding". The authors argue that the first two already exist and the third does not yet. **Nuances**: discovery is not the same as understanding. — [DOI](https://doi.org/10.1038/s42254-022-00518-3)
- **Gottweis, J., Weng, W.-H., Daryin, A., Tu, T., et al. (2025). Towards an AI co-scientist / Accelerating scientific discovery with Co-Scientist. arXiv:2502.18864. https://arxiv.org/abs/2502.18864** (**preprint**; the arXiv page title now reads "Accelerating scientific discovery with Co-Scientist") and Google Research blog, 19 Feb 2025 **[non-peer-reviewed]**.
  - **System:** a multi-agent system on Gemini 2.0 that uses generate–debate–evolve loops.
  - **AML:** in vitro validation of drug-repurposing candidates for acute myeloid leukaemia.
  - **Liver fibrosis:** epigenetic targets tested in hepatic organoids; full results were deferred to a later report.
  - **Antimicrobial resistance:** the cf-PICI hypothesis was a *re-discovery* of a finding the team had already validated but not yet published.
  - **Caveats:** small expert evaluations (15 and 11 research goals, 7 experts), and the Elo-based self-evaluation "is not based on an independent ground truth".

  **Supports, with caveats**. — [arXiv](https://arxiv.org/abs/2502.18864); [Google blog](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/)
- **Ghareeb, A. E., Chang, B., Mitchener, L., Yiu, A., et al. (2025). Robin: A multi-agent system for automating scientific discovery. arXiv:2505.13400. https://arxiv.org/abs/2505.13400** (FutureHouse; **preprint**). Robin combines the Crow, Falcon and Finch agents. For dry age-related macular degeneration it proposed boosting RPE phagocytosis and identified ripasudil, a ROCK inhibitor already approved for glaucoma, as a candidate (repurposing).
  - **Who did what:** humans ran the wet-lab experiments, so the work is AI-directed rather than AI-performed.
  - **Evidence level:** the validation is preclinical, in cell culture.
  - **Publication status:** FutureHouse's page states a Nature version appeared on 19 May 2026. **I could not confirm its DOI via Crossref, so cite the arXiv version unless verified.**

  **Supports, with caveats**. — [arXiv](https://arxiv.org/abs/2505.13400); [FutureHouse announcement](https://www.futurehouse.org/research-announcements/demonstrating-end-to-end-scientific-discovery-with-robin-a-multi-agent-system) [non-peer-reviewed]
- **Lu, C., Lu, C., Lange, R. T., Yamada, Y., Hu, S., et al. (2026). Towards end-to-end automation of AI research. *Nature*, 651, 914–919. https://doi.org/10.1038/s41586-026-10265-5** (Sakana "The AI Scientist"; earlier arXiv:2408.06292, 2024). The system generates ideas, writes code, runs experiments, writes the manuscript and reviews it. One AI-generated manuscript passed first-round review at a top machine-learning conference *workshop* that had a 70% acceptance rate (per the abstract). **Supports**, with **Challenges** from the independent evaluation below. — [Crossref/DOI](https://doi.org/10.1038/s41586-026-10265-5)
- **Beel, J., Kan, M.-Y., & Baumgart, M. (2025). Evaluating Sakana's AI Scientist: Bold claims, mixed results, and a promising future? arXiv:2502.14297. https://arxiv.org/abs/2502.14297** (**preprint**) — Independent evaluation:
  - **Novelty:** literature reviews misjudged novelty, for example calling micro-batching for SGD novel.
  - **Experiments:** 42% failed because of coding errors.
  - **Citations:** papers had a median of 5 citations, mostly outdated.
  - **Results:** some numerical results were hallucinated.
  - **Overall:** quality like "a rushed undergraduate paper", though very fast and cheap.

  **Challenges** (and supports the "paper-mill" concern). — [arXiv](https://arxiv.org/abs/2502.14297)
- **Novikov, A., Vũ, N., Eisenberger, M., Dupont, E., et al. (2025). AlphaEvolve: A coding agent for scientific and algorithmic discovery. arXiv:2506.13131. https://arxiv.org/abs/2506.13131** (**preprint**) and DeepMind blog, 14 May 2025 **[non-peer-reviewed]**. Reported results:
  - **Matrix multiplication:** a 4×4 complex-valued algorithm using 48 scalar multiplications, beating Strassen (1969) in that setting.
  - **Open maths problems:** on more than 50 problems it matched the state of the art in about 75% and improved on it in about 20%.
  - **Compute savings:** a Borg scheduling heuristic recovers about 0.7% of Google's worldwide compute.

  **Supports**, in domains with automatic evaluators. — [arXiv](https://arxiv.org/abs/2506.13131); [DeepMind blog](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)
- **Toner-Rodgers, A. (2024). Artificial intelligence, scientific discovery, and product innovation. arXiv:2412.17866 (withdrawn).** **CAUTIONARY TALE.** The paper claimed that AI in a US corporate materials-R&D lab yielded 44% more materials, 39% more patents and 17% more product innovation.
  - **MIT statement:** on 16 May 2025 MIT said it had "no confidence in the provenance, reliability or validity of the data and … in the veracity of the research". It asked for withdrawal from arXiv and from the *Quarterly Journal of Economics*.
  - **Current status:** the arXiv page now shows withdrawal.
  - **Downstream citation:** reporting indicates the paper was cited even in EU policy speeches after it was discredited.

  **Challenges**: it shows how eagerness for AI-productivity evidence can bypass scrutiny. — [arXiv record](https://arxiv.org/abs/2412.17866); [TechCrunch](https://techcrunch.com/2025/05/17/mit-disavows-doctoral-students-paper-on-ai-productivity-benefits); [The Decoder](https://the-decoder.com/mit-says-a-high-profile-ai-productivity-study-used-data-that-cannot-be-trusted/); [Science|Business](https://sciencebusiness.net/news/ai/research-commissioner-appears-cite-discredited-study-ai-speech)
- **Bianchini, S., Müller, M., & Pelletier, P. (2022). Artificial intelligence in science: An emerging general method of invention. *Research Policy*, 51(10), 104604. https://doi.org/10.1016/j.respol.2022.104604** — Bibliometric evidence that deep learning is spreading across scientific fields as a "general method of invention", with heterogeneous effects. **Supports / Nuances**. — [DOI](https://doi.org/10.1016/j.respol.2022.104604)

### Inferences
- **Where AI succeeds.** Validated discovery is concentrated where there are large curated datasets and automatic evaluators: protein structures (PDB/CASP), algorithms and maths. That pattern is consistent with Hao et al.'s "move toward data-rich areas" finding (Section 4).
- **Evidence status of agentic systems.** Most "AI scientist" evidence in 2025–26 is preprints or company announcements with in vitro or workshop-level validation. Only AlphaFold has full peer review plus broad community uptake and recognition.

### Gaps
- **Robin.** The DOI of the 2026 Nature paper is not verified.
- **Co-scientist.** I found no peer-reviewed journal version of the full paper (only follow-on preprints).

## 4. Evidence on productivity vs. narrowing, and on human-aware AI for interdisciplinarity

### Takeaway
The best large-scale evidence (Hao, Xu, Li & Evans, Nature 2026) finds that AI boosts individual careers but contracts the collective range of topics and reduces engagement between scientists. Sourati & Evans show that AI designed to target "blind spots" between communities could instead widen exploration. Design choices therefore matter.

### Cited Findings (annotated bibliography)
- **Hao, Q., Xu, F., Li, Y., & Evans, J. A. (2026). Artificial intelligence tools expand scientists' impact but contract science's focus. *Nature*, 649, 1237–1243. https://doi.org/10.1038/s41586-025-09922-y** (online 14 Jan 2026; arXiv:2412.07727). Figures from the arXiv abstract (**check them against the final Nature text**):
  - **Data:** 41.3 million natural-science papers.
  - **Individual gains:** AI-using scientists publish 3.02× more papers, receive 4.84× more citations and become project leaders 1.37 years earlier.
  - **Collective costs:** AI adoption shrinks the collective volume of topics studied by 4.63% and reduces scientists' engagement with one another by 22%.
  - **Interpretation:** AI work drifts to data-rich areas and "automate[s] established fields rather than explore[s] new ones".

  **Nuances / Challenges**. This is the central evidence for "AI disrupts but could narrow science". — [Crossref/DOI](https://doi.org/10.1038/s41586-025-09922-y); [arXiv](https://arxiv.org/abs/2412.07727)
- **Sourati, J., & Evans, J. A. (2023). Accelerating science with human-aware artificial intelligence. *Nature Human Behaviour*, 7, 1682–1696. https://doi.org/10.1038/s41562-023-01648-z** — Models that account for the distribution of human expertise predict future discoveries better. Steered towards "alien", non-human-reachable hypotheses, the same approach can generate promising directions that the communities as they are now organised would miss. **Supports** the interdisciplinarity thesis: AI as a bridge across disconnected communities. — [DOI](https://doi.org/10.1038/s41562-023-01648-z)
- **Gao, J., & Wang, D. (2024). Quantifying the use and potential benefits of artificial intelligence in scientific research. *Nature Human Behaviour*, 8, 2281–2292. https://doi.org/10.1038/s41562-024-02020-5** — Finds that AI use in research is widespread and associated with citation advantages across fields. It also finds a gap between where AI could benefit research and where AI expertise is located, plus demographic disparities in who benefits. **Supports / Nuances**. — [DOI](https://doi.org/10.1038/s41562-024-02020-5)
- **Duede, E., Dolan, W., Bauer, A., Foster, I., & Lakhani, K. (2024). Oil & water? Diffusion of AI within and across scientific fields. arXiv:2405.15828. https://arxiv.org/abs/2405.15828** (**preprint**; arXiv lists 5 authors) — Tracks AI engagement across about 20 fields. It finds rapid diffusion and an AI citation premium, together with conceptual "distance" between AI experts and domain scientists. **Nuances**. Only the arXiv metadata was verified, so check the details in the full text before quoting. — [arXiv](https://arxiv.org/abs/2405.15828)
- **Messeri, L., & Crockett, M. J. (2024). Artificial intelligence and illusions of understanding in scientific research. *Nature*, 627, 49–58. https://doi.org/10.1038/s41586-024-07146-0** — Sets out four visions of AI in science: Oracle, Surrogate, Quant and Arbiter. It warns of "illusions of explanatory depth, exploratory breadth and objectivity", and of "scientific monocultures" in which AI-friendly methods and questions crowd out others. **Challenges** (the homogenisation critique). — [DOI](https://doi.org/10.1038/s41586-024-07146-0)

### Inferences
- **Empirical tension.** AI rewards individuals, which drives adoption, while it may narrow the collective range of science. This mirrors the publish-or-perish incentive problem the position paper diagnoses: individual incentives against collective goods.
- **Design matters.** Sourati & Evans suggest that homogenisation is not inevitable. AI aimed at gaps between communities could support interdisciplinarity. This is the "could build better science" side of the argument.

### Gaps
- I could not access the full Nature text of Hao et al. (paywall redirect), so it is not confirmed whether the final published numbers equal the arXiv abstract figures.

## 5. Policy/vision reports and counter-arguments (overhype, homogenisation, reproducibility)

### Takeaway
Institutional reports (OECD 2023, SAPEA/EU 2024, Royal Society 2024, DeepMind 2024) are broadly optimistic but each flags risks: reproducibility, opacity, concentration of compute and narrowing. Critics (Narayanan & Kapoor; Messeri & Crockett; Kapoor & Narayanan on leakage) argue that AI may amplify the productivity–progress paradox.

### Cited Findings (annotated bibliography)
- **OECD (2023). *Artificial Intelligence in Science: Challenges, Opportunities and the Future of Research*. OECD Publishing, Paris. https://doi.org/10.1787/a8d820bd-en** (published 26 June 2023). An edited volume of expert essays on how AI could raise research productivity, which the volume argues is declining, including through literature-mining and support for interdisciplinarity. It also covers policy needs. **Supports**. — [DOI](https://doi.org/10.1787/a8d820bd-en)
- **The Royal Society (2024). *Science in the age of AI: How artificial intelligence is changing the nature and method of scientific research*. London: Royal Society** (May 2024; working group chaired by Alison Noble). Based on engagement with more than 100 scientists. It recommends access to AI infrastructure, open-science alignment and capacity for oversight. It warns that opaque "black-box" tools could undermine the reliability of findings and trust. **Supports / Nuances**. — [Royal Society project page](https://royalsociety.org/news-resources/projects/science-in-the-age-of-ai/); [press release](https://royalsociety.org/news/2024/05/ai-research-tools-could-undermine-trust-accuracy-scientific-findings/)
- **SAPEA (2024). *Successful and timely uptake of artificial intelligence in science in the EU*. Evidence Review Report No. 13. Berlin: SAPEA. https://doi.org/10.5281/zenodo.10849580** (15 April 2024). It underpins Scientific Opinion No. 15 of the EU Group of Chief Scientific Advisors, a response to the Commission's July 2023 request. **Supports** (policy uptake). I did not read the full text, so cite the specific recommendations only after checking them. — [SAM page](https://scientificadvice.eu/scientific-outputs/ai-in-science-evidence-review-report/); [PDF via ALLEA](https://allea.org/wp-content/uploads/2024/04/ai-in-science-err.pdf)
- **Google DeepMind (2024). *A new golden age of discovery: Seizing the AI for Science opportunity*.** November 2024 policy essay **[non-peer-reviewed, corporate]**. It names five opportunity areas, including *knowledge synthesis*, and five sets of "ingredients", and it discusses risks to creativity and reliability. **Supports** (industry vision; label as advocacy). — [PDF](https://storage.googleapis.com/deepmind-media/DeepMind.com/Assets/Docs/a-new-golden-age-of-discovery_nov-2024.pdf); [DeepMind AI-for-science policy page](https://deepmind.google/public-policy/ai-for-science/). The PDF was not opened in this session; the summary comes from secondary descriptions.
- **Narayanan, A., & Kapoor, S. (2025). Why an overreliance on AI-driven modelling is bad for science. *Nature*, 640, 312–314 (Comment). https://doi.org/10.1038/d41586-025-01067-2** — Argues that AI-based modelling is spreading faster than validation norms and is spreading flawed or irreproducible results. **Challenges**. — [DOI](https://doi.org/10.1038/d41586-025-01067-2)
- **Kapoor, S., & Narayanan, A. (2025). Could AI slow science? Confronting the production–progress paradox.** Essay, *AI Snake Oil / AI as Normal Technology* newsletter, 16 July 2025 **[non-peer-reviewed]**. Argues that publications and researchers have grown exponentially while progress has not. AI could worsen bottlenecks: quantity-rewarding incentives, entrenched flawed theories and limited collective attention. The authors call for meta-science and reform by institutions and funders. **Challenges**, and strongly aligned with the position paper's "academic system" critique. Only secondary summaries were read. — [Princeton CITP summary](https://citp.princeton.edu/news/2025/could-ai-slow-science-confronting-production-progress-paradox)
- **Kapoor, S., & Narayanan, A. (2023). Leakage and the reproducibility crisis in machine-learning-based science. *Patterns*, 4(9), 100804. https://doi.org/10.1016/j.patter.2023.100804** — Documents data leakage affecting hundreds of papers across about 17 fields that use machine learning, leading to overoptimistic results. **Challenges**. The "17 fields / hundreds of papers" figures are from memory of the paper and should be confirmed. — [DOI](https://doi.org/10.1016/j.patter.2023.100804)
- **Messeri & Crockett (2024)**, Section 4 above: the homogenisation and "monoculture" critique. **Challenges**.
- **Beel et al. (2025)** and the **Toner-Rodgers withdrawal**, Section 3 above: empirical challenges to overclaims. **Challenges**.

### Inferences
- **Common ground.** The pro and con sides largely agree on the facts: AI raises output, and validated breakthroughs are concentrated in data-rich and well-evaluated domains. They disagree on whether institutions will adapt.
- **The pivot for the position paper.** This supports the position paper's framing that AI's benefit for science is conditional on reforming incentives: funding of interdisciplinary work (Bromham), evaluation beyond output counts (Chu & Evans; Kapoor & Narayanan), and design of AI for exploration rather than exploitation (Sourati & Evans vs. Hao et al.).

### Gaps
- **Unverified numbers.** The European Commission's own "European strategy for AI in science" documents (2025) were not checked. The full texts of the SAPEA report and the DeepMind essay were not read, so their specific recommendations should be quoted only after checking. The "17 fields" figure for Kapoor & Narayanan (2023) also needs confirming.
- **Peer-reviewed critiques.** No peer-reviewed quantitative study was found that tests whether AI literature tools reduce *or* entrench citation concentration (the Matthew effect). This is an open empirical question worth flagging in the paper.
