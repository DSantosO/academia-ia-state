# Section 2: The impact of generative AI / LLMs on academic publishing and evaluation (annotated bibliography)

Verification note: every DOI below was resolved against the Crossref API, and every arXiv ID against the arXiv API, on 2026-10-15. The NIH notices were fetched directly. Items marked "(secondary)" were confirmed only through news coverage or search results, not the primary document. Stance codes: **S** = supports the thesis that AI is disrupting or destroying the system; **N** = nuances it; **C** = challenges it.

## Q1. Detection and prevalence of LLM-written text in papers and reviews

### Takeaway
Several independent methods (distributional MLE, excess vocabulary, marker words, detectors) agree that LLM-modified text went from about zero to a large minority of scientific prose in about two years. Estimates run to roughly 13.5% or more of 2024 biomedical abstracts, around 22% of CS abstracts, and around 20% of ML conference reviews. These are population-level, detector-dependent estimates, not per-document proof.

### Cited Findings
- **Liang, W., Izzo, Z., Zhang, Y., Lepp, H., et al. (2024). "Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews." ICML 2024. arXiv:2403.07183.** Uses a distributional maximum-likelihood estimator and estimates that about 6.5–16.9% of review text at ICLR 2024, NeurIPS 2023, CoRL 2023 and EMNLP 2023 was substantially LLM-modified. LLM-modified reviews were more common near deadlines and among reviewers less likely to respond to author rebuttals. **S** — [arXiv](https://arxiv.org/abs/2403.07183)
- **Liang, W., Zhang, Y., Wu, Z., Lepp, H., Ji, W., Zhao, X., et al. (2025). "Quantifying large language model usage in scientific papers." Nature Human Behaviour. doi:10.1038/s41562-025-02273-8** (preprint: "Mapping the Increasing Use of LLMs in Scientific Papers," arXiv:2404.01268). Measures a steady rise in LLM-modified sentences across arXiv, bioRxiv and Nature-portfolio papers from 2020 to 2024. Growth is fastest in computer science (about 22% of abstract sentences) and higher among authors who post more preprints and in crowded fields. **S** — [DOI](https://doi.org/10.1038/s41562-025-02273-8); [arXiv](https://arxiv.org/abs/2404.01268)
- **Kobak, D., González-Márquez, R., Horvát, E.-Á., & Lause, J. (2025). "Delving into LLM-assisted writing in biomedical publications through excess vocabulary." Science Advances. doi:10.1126/sciadv.adt3813.** Analyses roughly 15M PubMed abstracts from 2010–2024 and finds an unprecedented surge of "style words" ("delves," "showcasing," "underscores"). Gives a lower bound of at least 13.5% of 2024 abstracts processed with LLMs, rising to around 40% in some subgroups (by country, journal and field). **S** — [DOI](https://doi.org/10.1126/sciadv.adt3813)
- **Gray, A. (2024). "ChatGPT 'contamination': estimating the prevalence of LLMs in the scholarly literature." arXiv:2403.16887.** Uses marker-word frequencies in Dimensions data to estimate that at least about 60,000 papers (around 1% of the 2023 literature) were LLM-assisted. This was an early bibliometric signal. **S** — [arXiv](https://arxiv.org/abs/2403.16887)
- **Latona, G. R., Horta Ribeiro, M., Davidson, T. R., Veselovsky, V., & West, R. (2024). "The AI Review Lottery: Widespread AI-Assisted Peer Reviews Boost Paper Scores and Acceptance Rates." arXiv:2405.02150.** Estimates that about 15.8% of ICLR 2024 reviews were AI-assisted. In a quasi-experimental analysis, AI-assisted reviews gave higher scores and raised the acceptance odds of borderline papers. This means the evaluation outcome, not just the prose, is affected. **S** — [arXiv](https://arxiv.org/abs/2405.02150)
- **Kusumegi, K., Yang, X., Ginsparg, P., de Vaan, M., Stuart, T., & Yin, Y. (2025). "Scientific production in the era of large language models." Science 390(6779):1240–1243. doi:10.1126/science.adw3000** (arXiv:2601.13187). Covers 2.1M preprints, 28K review reports and 246M accesses. LLM adoption is associated with higher manuscript output and with gains for non-native English writers. Linguistic complexity is becoming a less reliable signal of quality, so evaluators lose a traditional quality proxy. **N** (efficiency and equity gains, but it erodes quality signals) — [DOI](https://doi.org/10.1126/science.adw3000); [arXiv](https://arxiv.org/abs/2601.13187)
- **Kwon, D. (2025). "Science sleuths flag hundreds of papers that use AI without disclosing it." Nature news, 24 Apr 2025. doi:10.1038/d41586-025-01180-2.** Reports that integrity sleuths (e.g., the Academ-AI tracker) found hundreds of published papers with tell-tale chatbot phrases ("as an AI language model," "regenerate response") but no disclosure. This points to failures at the editorial-screening level. **S** — [DOI](https://doi.org/10.1038/d41586-025-01180-2)
- **Prillaman, M. (2023). "'ChatGPT detector' catches AI-generated papers with unprecedented accuracy." Nature news. doi:10.1038/d41586-023-03479-4.** Covers early domain-specific detectors. This is useful context for how much the prevalence literature depends on contested detection methods. **N** — [DOI](https://doi.org/10.1038/d41586-023-03479-4)

### Inferences
- The studies converge across very different methods (word frequencies, MLE over distributions, supervised detectors), which strengthens the qualitative conclusion despite each method's weaknesses.
- "LLM-modified" mostly means language polishing. Prevalence of AI *text* is not the same as prevalence of AI-*fabricated science*. The position paper should keep these two separate.

### Gaps
- I found no validated per-paper ground truth at scale. Every estimate is a population-level estimate or depends on a detector.
- I did not verify any 2026 update to Kobak et al. for 2025 abstracts.

## Q2. LLM-generated peer reviews, prompt injection, and journal/funder policies

### Takeaway
By the ICLR 2026 cycle, about one in five reviews was flagged as fully AI-generated. Authors have started embedding hidden prompts aimed at AI reviewers. Hallucinated references have passed multi-reviewer peer review at NeurIPS. Funders (NIH, UKRI, ERC) have answered with bans on AI in review. In 2025 NIH also capped applications per PI, explicitly citing AI-enabled mass submission.

### Cited Findings
- **Naddaf, M. (2025). "Major AI conference flooded with peer reviews written fully by AI." Nature news, 27 Nov 2025. doi:10.1038/d41586-025-03506-6.** Reports Pangram Labs' scan of ICLR 2026: about 21% of roughly 75,800 reviews were flagged as fully AI-generated, and more than half showed some AI involvement. Fully AI reviews were longer and gave slightly higher scores. Pangram's accuracy claims were questioned afterwards. **S** — [DOI](https://doi.org/10.1038/d41586-025-03506-6); [secondary summary](https://www.plagiarismtoday.com/2025/12/04/ai-conference-overrun-with-ai-peer-review/)
- **Shen, S., & Wang, K. (2026). "Detecting AI-Generated Content in Academic Peer Reviews." arXiv:2602.00319.** Trains a detector on historical reviews and estimates that about 20% of ICLR reviews and 12% of Nature Communications reviews in 2025 were AI-generated. This shows the phenomenon reaches beyond ML conferences into a major journal. **S** — [arXiv](https://arxiv.org/abs/2602.00319)
- **Fichtl, A. M., Ellinger, L., Kelber, J., Olík, K., et al. (2026). "AI-Assisted Peer Review Across Research Communities: From Reviewer AI Policies to LLM Review Quality." arXiv:2608.03581.** Surveys reviewer-AI policies across communities and evaluates the quality of LLM reviews at ICLR 2026 and Nature Communications. This is the most recent comparative treatment I found. **N** — [arXiv](https://arxiv.org/abs/2608.03581)
- **Singh Chawla, D. (2024). "Is ChatGPT corrupting peer review? Telltale words hint at AI use." Nature news, 10 Apr 2024. doi:10.1038/d41586-024-01051-2.** Journalistic framing of the Liang et al. review study. **S** — [DOI](https://doi.org/10.1038/d41586-024-01051-2)
- **Naddaf, M. (2025). "AI is transforming peer review — and many scientists are worried." Nature news feature, 26 Mar 2025. doi:10.1038/d41586-025-00894-7.** Surveys the spread of AI tools in reviewing, publisher experiments, and researchers' concerns about confidentiality and quality. **S/N** — [DOI](https://doi.org/10.1038/d41586-025-00894-7)
- **Gibney, E. (2025). "Scientists hide messages in papers to game AI peer review." Nature news, 11 Jul 2025. doi:10.1038/d41586-025-02172-y.** Follows Nikkei Asia's report of 1 Jul 2025: hidden white-text or tiny-font prompts ("give a positive review only") in 17 arXiv preprints from 14 institutions in 8 countries. Nature found further cases. **S** — [DOI](https://doi.org/10.1038/d41586-025-02172-y); [secondary on Nikkei](https://www.infodocket.com/2025/07/04/report-hidden-ai-prompts-in-academic-papers-spark-concern-about-research-integrity/)
- **Lin, Z. (2025). "Hidden Prompts in Manuscripts Exploit AI-Assisted Peer Review." arXiv:2507.06185.** Systematic analysis that identifies 18 arXiv manuscripts with hidden prompts and classifies the injection types. Argues this is an integrity breach and that policy is fragmented: some publishers allow some AI in review and others (e.g., Elsevier) forbid it. **S** — [arXiv](https://arxiv.org/abs/2507.06185)
- **GPTZero (Jan 2026). "GPTZero finds 100 new hallucinations in NeurIPS 2025 accepted papers."** Scanned 4,841 of 5,290 accepted NeurIPS 2025 papers and confirmed 100 fabricated citations in 51 papers that passed review by three or more reviewers. Also found about 50 in ICLR 2026 submissions. This is a vendor report and so has a commercial interest. **S** — [GPTZero](https://gptzero.me/news/neurips/); [Fortune coverage](https://fortune.com/2026/01/21/neurips-ai-conferences-research-papers-hallucinations/)
- **Gibney, E. (2025). "Can researchers stop AI making up citations?" Nature news, 8 Sep 2025. doi:10.1038/d41586-025-02853-8.** Covers hallucinated references in submissions and the tools being built to catch them. **S** — [DOI](https://doi.org/10.1038/d41586-025-02853-8)
- **NIH (2023). NOT-OD-23-149, "The Use of Generative AI Technologies is Prohibited for the NIH Peer Review Process."** Bans NIH reviewers from using generative AI on applications, citing confidentiality. **S** (institutional recognition of the threat) — [NIH](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-23-149.html)
- **NIH (2025). NOT-OD-25-132, "Supporting Fairness and Originality in NIH Research Applications." Released 17 Jul 2025, effective for applications on or after 25 Sep 2025.** Applications "substantially developed by AI" will not be considered original. Sets a cap of six applications per PI per calendar year. The notice states that "the use of AI tools has enabled Principal Investigators to submit more than 40 distinct applications in a single application submission round." This is one of the most direct institutional admissions that AI is straining evaluation. **S** — [NIH](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html)
- **UKRI (Sep 2024). "Use of generative artificial intelligence in application preparation and assessment" (policy).** Applicants must use AI with care and transparency. Assessors are prohibited from using generative AI to develop their reviews. Builds on a joint UK funder statement from Sep 2023. **S/N** — [UKRI](https://www.ukri.org/publications/generative-artificial-intelligence-in-application-and-assessment-policy/use-of-generative-artificial-intelligence-in-application-preparation-and-assessment/)
- **ERC Scientific Council (Dec 2023). Statement on the use of AI in grant applications** (secondary). Lets applicants use AI for brainstorming and editing while they remain fully responsible for the content. Restricts evaluators' use. I did not fetch the primary text. **N** — [secondary comparison](https://www.thesify.ai/blog/ai-grant-application-policies)
- **Hosseini, M., & Horbach, S. P. J. M. (2023). "Fighting reviewer fatigue or amplifying bias? Considerations and recommendations for use of ChatGPT and other large language models in scholarly peer review." Research Integrity and Peer Review 8:4. doi:10.1186/s41073-023-00133-5.** An early interpretive piece. LLMs could relieve reviewer fatigue but risk amplifying bias, breaking confidentiality and homogenising judgement. Recommends disclosure and limited use. **N** — [DOI](https://doi.org/10.1186/s41073-023-00133-5)

### Inferences
- Prompt injection plus AI reviewing creates an adversarial loop in which neither side is a human evaluator. This is a strong argument that peer review is being hollowed out rather than only made more efficient.
- In NIH's notice, a major funder explicitly links AI to submission volume. This is primary-source evidence for the "volume overwhelms evaluation" mechanism.

### Gaps
- I did not confirm what action ICLR 2026 took after the Pangram finding (desk rejections, reviewer sanctions) from a primary ICLR statement.
- I found no primary data on how often LLM reviewers actually obey hidden prompts in real venues. Nature notes this is unknown.

## Q3. Paper mills, fabrication at scale, and AI-enabled "formulaic" science

### Takeaway
Organised fraud was growing faster than the legitimate literature before ChatGPT. LLMs lower the cost further, with documented mass production of formulaic papers from open datasets and fabricated papers indexed in Google Scholar. Much of this problem predates AI, so AI acts as an accelerant on an existing system failure.

### Cited Findings
- **Richardson, R. A. K., Hong, S. S., Byrne, J. A., Stoeger, T., & Amaral, L. A. N. (2025). "The entities enabling scientific fraud at scale are large, resilient, and growing rapidly." PNAS 122(32). doi:10.1073/pnas.2420092122.** Documents networks of editors, authors and brokers (paper mills) and journal hijacking. Finds that suspected fraudulent output is growing much faster than the scientific literature overall (doubling roughly every 1.5 years versus about 15 years). **S** (AI not the main focus; the scale argument) — [DOI](https://doi.org/10.1073/pnas.2420092122)
- **Suchak, T., Aliu, A. E., Harrison, C., Zwiggelaar, R., Geifman, N., & Spick, M. (2025). "Explosion of formulaic research articles, including inappropriate study designs and false discoveries, based on the NHANES US national health database." PLOS Biology 23(5):e3003152. doi:10.1371/journal.pbio.3003152.** Found 341 single-factor NHANES papers. The count rose from about 4 per year (2014–2021) to 33, 82 and 190 in 2022, 2023 and 2024. Links the rise to AI-assisted, paper-mill-style production using AI-ready datasets. **S** — [DOI](https://doi.org/10.1371/journal.pbio.3003152)
- **Naddaf, M. (2025). "Low-quality papers based on public health data are flooding the scientific literature." Nature news, 15 Jul 2025. doi:10.1038/d41586-025-02241-2.** Extends the NHANES finding to other open health datasets. **S** — [DOI](https://doi.org/10.1038/d41586-025-02241-2)
- **Haider, J., Söderström, K. R., Ekström, B., & Rödl, M. (2024). "GPT-fabricated scientific papers on Google Scholar: Key features, spread, and implications for preempting evidence manipulation." HKS Misinformation Review. doi:10.37016/mr-2020-156.** Found about 139 questionable, apparently GPT-fabricated papers indexed in Google Scholar, many on policy-relevant topics such as health, environment and computing. Warns of "evidence hacking." **S** — [DOI](https://doi.org/10.37016/mr-2020-156)
- **Cabanac, G., Labbé, C., & Magazinov, A. (2021). "Tortured phrases: A dubious writing style emerging in science." arXiv:2107.06751.** Pre-LLM baseline. Paraphrasing tools produce "tortured phrases" ("counterfeit consciousness" for "artificial intelligence"), which became the basis of the Problematic Paper Screener. Shows that machine-generated fraud predates LLMs. **N** (the problem predates generative AI) — [arXiv](https://arxiv.org/abs/2107.06751)
- **Van Noorden, R. (2023). "More than 10,000 research papers were retracted in 2023 — a new record." Nature news. doi:10.1038/d41586-023-03974-8.** Record retractions, most of them from Hindawi (Wiley) special issues compromised by paper mills and peer-review manipulation. Wiley later closed several Hindawi titles. **S/N** (mass fraud, mostly pre-LLM) — [DOI](https://doi.org/10.1038/d41586-023-03974-8)

### Inferences
- The strongest framing for the position paper is that AI collapses the cost of the outputs paper mills were already selling: text, images, plausible analyses. This turns a niche fraud market into commodity production.

### Gaps
- I did not verify a primary peer-reviewed study that quantifies AI-*generated images* (e.g., western blots) in published papers for 2024–2026. Leave this as a gap rather than cite news anecdotes.
- I did not fetch Wiley's own figure for total Hindawi retractions (more than 11,000 is widely reported).

## Q4. Submission surges, reviewer overload, and gatekeeper responses (arXiv, conferences)

### Takeaway
Gatekeepers have started rationing access. arXiv CS stopped accepting unrefereed review and position papers (31 Oct 2025), NIH capped applications, and ML conferences report submissions doubling. Evidence that AI is the *cause* of the surges is mostly circumstantial and asserted by moderators rather than measured.

### Cited Findings
- **arXiv CS policy change (31 Oct 2025).** arXiv's CS section stopped accepting review, survey and position papers unless they have already been accepted at a peer-reviewed venue. Moderators (e.g., Thomas Dietterich) cited a flood of LLM-generated surveys. The scope is CS only, with other sections possibly to follow. **S** — [404 Media](https://www.404media.co/arxiv-changes-rules-after-getting-spammed-with-ai-generated-research-papers/); [Decrypt](https://decrypt.co/347196/arxiv-blocks-ai-generated-survey-papers-flood-trashy-submissions)
- **Elazar, Y., & Antoniak, M. (2026). "LLM-Generated or Human-Written? Comparing Review and Non-Review Papers on ArXiv." arXiv:2601.17036.** Tests arXiv's premise. Review papers do show higher LLM-detection rates, but the absolute number of LLM-generated *non-review* papers is much larger. Also notes that arXiv provided no quantitative evidence. The policy hits some subfields hard (e.g., Computers & Society, potentially about 50% cuts). **N** (confirms the problem, questions the remedy) — [arXiv](https://arxiv.org/abs/2601.17036)
- **AAAI-26 submissions** (secondary): nearly 29,000 submissions, about double the previous year. This is cited as part of the reviewer-overload debate. **S** (causation to AI not established) — [Tech Policy Press](https://techpolicy.press/can-ai-help-fix-peer-review-instead-of-breaking-it)
- **Hanson, M. A., Barreiro, P. G., Crosetto, P., & Brockington, D. (2024). "The strain on scientific publishing." Quantitative Science Studies 5(4). doi:10.1162/qss_a_00327.** Indexed article output grew about 47% from 2016 to 2022, driven by publishers' special issues and fast turnaround, which strains reviewers. **The strain predates ChatGPT.** **C/N** (supports the claim that AI amplifies pre-existing flaws) — [DOI](https://doi.org/10.1162/qss_a_00327)

### Inferences
- The volume crisis has two layers: a structural, publisher-driven expansion (2016–2022), and an AI-enabled marginal cost collapse (2023 onward). The position paper is stronger if it acknowledges the first layer.

### Gaps
- I found no peer-reviewed causal study that attributes conference submission growth to LLMs specifically. The quantitative series are left to the separate data-sources effort.

## Q5. Autonomous "AI scientists" passing peer review and the authorship question

### Takeaway
Fully AI-generated papers have cleared workshop-level review (Sakana, ICLR 2025 workshop), and in 2025 a whole conference (Agents4Science) used AI as first authors and reviewers. Results show real but limited capability. The milestone matters less for research quality than for showing that peer review cannot reliably tell whether a human did the science.

### Cited Findings
- **Lu, C., Lu, C., Lange, R. T., Foerster, J., Clune, J., & Ha, D. (2024). "The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery." arXiv:2408.06292.** End-to-end pipeline (idea, code, experiments, paper, automated review) at about $15 per paper. **S** — [arXiv](https://arxiv.org/abs/2408.06292)
- **Lu, C., Lu, C., Lange, R. T., Yamada, Y., Hu, S., Foerster, J., et al. (2026). "Towards end-to-end automation of AI research." Nature (published 25 Mar 2026). doi:10.1038/s41586-026-10265-5.** Peer-reviewed write-up of AI Scientist-v2. Reports a fully AI-generated paper that scored 6, 7 and 6 (average 6.33) at the ICLR 2025 "I Can't Believe It's Not Better" workshop, above the acceptance threshold, and was then withdrawn by prior agreement. Framing is narrower than the 2024 "open-ended discovery" claim. Critics note that only 1 of 3 submissions passed, that the workshop had a higher acceptance rate than the main track, and that independent tests found many coding failures. **S/N** — [DOI](https://doi.org/10.1038/s41586-026-10265-5); [Sakana](https://sakana.ai/ai-scientist-nature/)
- **Bianchi, F., Queen, O., Thakkar, N., Sun, E., et al. (2025). "Exploring the use of AI authors and reviewers at Agents4Science." arXiv:2511.15534.** Agents4Science 2025 (virtual, 22 Oct 2025) received 315 submissions with AI agents as first authors. 253 were reviewed by three LLM reviewers, the top 79 also by humans, and 48 were accepted. More than 1,800 attendees registered. Analyses where AI reviewers and AI authors fall short, and argues for transparent experimentation. **N** — [arXiv](https://arxiv.org/abs/2511.15534); [Science News](https://www.sciencenews.org/?p=3161586)
- **Messeri, L., & Crockett, M. J. (2024). "Artificial intelligence and illusions of understanding in scientific research." Nature 627:49–58. doi:10.1038/s41586-024-07146-0.** Interpretive. AI as "oracle," "surrogate," "quant" and "arbiter" risks "monocultures of knowing" and illusions of understanding, producing more but understanding less. Provides the epistemic underpinning for the "destroying" thesis. **S** — [DOI](https://doi.org/10.1038/s41586-024-07146-0)

### Inferences
- Both entries above use "AI as reviewer" and "AI as author" at once. Once both ends are automated, credentialing (authorship as accountability) loses its referent. This is the conceptual core for the position paper.

### Gaps
- I did not verify a 2026 instance of an AI-generated paper accepted at a *main-track* venue or journal without prior disclosure.

## Q6. Interpretive essays: "AI breaks the system" vs "AI exposes pre-existing flaws / harms overstated"

### Takeaway
Commentary has moved from speculative worry (2023) toward a widespread view that generative AI accelerates an already strained, incentive-distorted system. Counter-arguments mostly say AI *exposes* existing problems or offers efficiency and equity gains, rather than denying harm.

### Cited Findings
- **Conroy, G. (2023). "How ChatGPT and other AI tools could disrupt scientific publishing." Nature 622:234–236. doi:10.1038/d41586-023-03144-w.** An early feature built on a Nature survey of researchers. It anticipates paper-mill acceleration, review automation and erosion of trust. **S** — [DOI](https://doi.org/10.1038/d41586-023-03144-w)
- **Naddaf, M. (2025). "How are researchers using AI? Survey reveals pros and cons for science." Nature news, 4 Feb 2025. doi:10.1038/d41586-025-00343-5.** Survey of about 5,000 researchers (Wiley) on acceptable AI uses. There is broad acceptance of AI for editing and translation, but divided views on AI in review and writing. **N** — [DOI](https://doi.org/10.1038/d41586-025-00343-5)
- **Lenharo, M. (2024). "ChatGPT turns two: how the AI chatbot has changed scientists' lives." Nature news, 2 Dec 2024. doi:10.1038/d41586-024-03940-y.** A balanced retrospective: productivity and language benefits alongside integrity risks. **N** — [DOI](https://doi.org/10.1038/d41586-024-03940-y)
- **Dey, D. (2026). "AI Isn't Breaking Peer Review — It Is Exposing That the System Was Already Broken." Springer Nature Research Communities (opinion), 30 Jun 2026.** Argues that overburdened, unpaid reviewing and misaligned incentives are the root causes. Unless incentives are reformed, generic AI reviews will replace human critique. **C/N** (the canonical "exposes, not causes" argument; low-prestige venue) — [Springer Nature Communities](https://communities.springernature.com/posts/ai-isn-t-breaking-peer-review-it-is-exposing-that-the-system-was-already-broken)
- **Kusumegi et al. (2025, Science)** (see Q1). The strongest *empirical* counterweight: LLMs raise productivity and especially benefit non-native English speakers. Harm comes from evaluation systems relying on proxies that AI cheapens. **N/C** — [DOI](https://doi.org/10.1126/science.adw3000)
- **Hanson et al. (2024, QSS)** (see Q4). Empirical support for "the system was already strained." **C/N** — [DOI](https://doi.org/10.1162/qss_a_00327)

### Inferences
- A robust position paper can absorb the counter-argument. If AI "only exposes" flaws, the flaws (publication-count incentives, unpaid review, proxy-based evaluation) are exactly what AI makes unsustainable. So "exposes" and "destroys" are compatible at the system level.

### Gaps
- I did not individually verify specific opinion pieces in Times Higher Education, Retraction Watch, The Scholarly Kitchen or Upstream within the tool budget. The topics are well covered there, but no specific titles or URLs are cited here to avoid unverified references. The report writer should verify any such piece before citing it.
- I did not verify a peer-reviewed essay arguing explicitly that AI harms to publishing are *overstated*. The counter-literature found is "amplifies or exposes" rather than "overstated."

## Entry count and stance summary
32 sources: about 22 support (S), about 9 nuance (N), and 3 challenge or partly challenge (C: Hanson et al. 2024; Dey 2026; Kusumegi et al. 2025 in part). Cabanac et al. (2021) is included as a pre-2022 baseline.
