# Closest prior work (2023–2026) and what the essay adds

**Verification (15 Oct 2026).** I resolved every DOI below against the Crossref API (title, venue, date, authors). I checked arXiv items against their arXiv abstract pages, because the arXiv API returned HTTP 429. SSRN pages were blocked (HTTP 403), so the SSRN items are verified only through their Crossref-registered SSRN DOIs (10.2139/ssrn.*). Each web page was fetched and its title checked. Each item carries a **read status**: **[full]** full text read or skimmed in full; **[partial]** part of the text read (paywall or registration wall); **[abstract]** abstract only; **[standfirst]** headline and standfirst only; **[title]** only the title and metadata verified. OpenAlex was unavailable: the shared free budget for this network was exhausted, and it returned "Insufficient budget … resets at midnight UTC". Semantic Scholar was rate-limited. Discovery therefore relied on web search, Crossref, arXiv pages and citation chaining from the reference lists of Manabu, Fourie and Blekhman, and from the works that cite Manabu and Gartenberg et al.

**Legend used throughout.** The essay's five points:
- **P1** — even legitimate use breaks the system;
- **P2** — "acceleration, not exploration" at the level of the whole system, with a triple-difference test;
- **P3** — governance so far is rationing that restores scarcity by decree;
- **P4** — two drivers of narrowing (internal incentives versus corporate concentration of tools and chat data);
- **P5** — the optimistic vision depends on open, efficient tools.

---

## Q1. What exactly do Manabu (2026) and Hansen (2026) argue?

### Takeaway
Both papers make the essay's core premise: AI makes academic output cheap and so pushes an already failing, metric-driven system past its limits. Neither makes the essay's specific claims P1–P5 in the form the essay plans.
- **Manabu** is a critical-theory essay (Bourdieu, Lyotard, academic capitalism). It argues that LLMs *complete and thereby destroy* publish-or-perish, and it ends with a "postdigital scholarly commons". It was itself drafted with an AI tool (Perplexity, which draws on ChatGPT, Claude and Gemini), as its acknowledgements disclose.
- **Hansen** is a systems analysis in which AI is a late *amplifier*. His "symbolic scarcity" is the *artificial* scarcity created by prestige rejection, and he wants to *remove* it (publish all sound work; curation "without scarcity"; AI triage). That points the opposite way from the essay's reading of caps as rationing.

### Cited Findings

**Manabu, T. (2026). "The Machine Consumes Itself: Artificial Intelligence and the End of Publish-or-Perish." *Postdigital Science and Education*. [abstract + acknowledgements + reference list + metadata; the article is paywalled]**
- **Publication facts.** Article type "Research", pp. 1–24. Received 28 Apr 2026, revised 27 May 2026, accepted 28 May 2026, published 9 Jun 2026. The author is listed only as "London, United Kingdom", with no institution. — [doi:10.1007/s42438-026-00666-0](https://doi.org/10.1007/s42438-026-00666-0); [Springer page](https://link.springer.com/article/10.1007/s42438-026-00666-0)
- **Thesis (abstract).** Publish-or-perish "is not being disrupted by Large Language Models (LLMs). Instead, the publish-or-perish model is being completed, and thereby destroyed, by LLMs—if not now, then in the very near future." — [doi](https://doi.org/10.1007/s42438-026-00666-0)
- **Mechanism (abstract).**
  - Academia is "a field whose dominant doxa is metric productivism, with publication counts functioning as symbolic capital" (Bourdieu).
  - That doxa is "the signature of market logics colonizing knowledge production" (Slaughter and Leslie, Peters and Jandrić, the Leiden Manifesto).
  - "the postmodern reduction of legitimacy to performativity is now literally instantiated by machines that play the language game of academic publishing, and … the apprenticeship pathway to scholarly identity is being severed" (Lyotard; Lave and Wenger).
  - "The crisis is incremental and existential: the relation between publication, labour, judgement, and recognition on which publish-or-perish depends is becoming increasingly untenable."
  - — [doi](https://doi.org/10.1007/s42438-026-00666-0)
- **Proposal (abstract).** "The paper closes by sketching a postdigital scholarly commons grounded in contribution, dialogue, and situated practice. What is scholarship for, after the machine?" — [doi](https://doi.org/10.1007/s42438-026-00666-0)
- **Evidence base, inferred from the reference list (full text not read).**
  - The paper has no original data ("No datasets were generated or analysed").
  - Empirical sources it cites:
    - Kusumegi et al. 2025 (*Science*); Kobak et al. 2025 (*Science Advances*); Liang et al. 2024 (ICML); Shen & Wang 2026 (arXiv);
    - Pangram's claim that 21% of ICLR reviews were AI-generated; GPTZero's claim of 100 hallucinated citations in NeurIPS 2025 papers;
    - Retraction Watch on paper mills; Tang & Cai 2025 (*JAMA Network Open*); Pataranutaporn et al. 2025 (IZA).
  - It also cites Big Tech critiques: Lindebaum et al. 2025 (*Organization Studies*) and Ashraf et al. 2025 (SRHE blog, "Who gets to decide what counts as knowledge? Big tech, AI, and the future of epistemic agency in higher education").
  - The reference list contains no NIH, arXiv-cap or open-weight-model sources.
  - — [Springer page, references](https://link.springer.com/article/10.1007/s42438-026-00666-0)
- **AI-use disclosure (acknowledgements, under the PSE GenAI policy).**
  - "drafted with the assistance of Perplexity, a Large Language Model (LLM) that leverages a variety of other LLMs (ChatGPT, Claude, Gemini and its own Sonar 2)".
  - The tool was used for: "(a) drafting and structuring sections of the manuscript from author-supplied outlines, along with support in determining the theoretical framework and arguments; (b) assistance with identifying and suggesting relevant literature for inclusion; (c) improving clarity, flow, and phrasing of prose."
  - "The intellectual argument and analytical positions are the author's own." The author verified every reference by hand.
  - — [Springer page](https://link.springer.com/article/10.1007/s42438-026-00666-0); PSE's policy: [Jandrić 2026, "GenAI and Academic Writing", PSE 8:372–386](https://doi.org/10.1007/s42438-026-00641-9)
- **Reception so far.**
  - The Springer page showed 4,619 accesses and 3 citations on 15 Oct 2026. — [Springer page](https://link.springer.com/article/10.1007/s42438-026-00666-0)
  - All three citing works are PSE papers (Semantic Scholar):
    - Cachipuendo-Contero 2026, "GenAI and Scholarly Knowledge: Language Relief at The Cost of Infrastructural Dependency" — [doi:10.1007/s42438-026-00672-2](https://doi.org/10.1007/s42438-026-00672-2) [title];
    - Holster 2026, "What are Human Researchers for?" — [doi:10.1007/s42438-026-00703-y](https://doi.org/10.1007/s42438-026-00703-y) [title];
    - "Reconsidering Student GenAI Disclosure Through Postdigital Agency" — [doi:10.1007/s42438-026-00679-9](https://doi.org/10.1007/s42438-026-00679-9) [title].

**Hansen, T. (2026). "Symbolic scarcity and epistemic waste: a systems theory of academic publishing failure." *Research Integrity and Peer Review* 11:7. [full; open access, CC BY 4.0]**
- **Publication facts.** Labelled "REVIEW". Received 11 Jul 2025, accepted 6 Feb 2026, published 12 Mar 2026. One author (University of South-Eastern Norway). Only 11 references. — [doi:10.1186/s41073-026-00193-3](https://doi.org/10.1186/s41073-026-00193-3)
- **Thesis.** Publishing operates under "symbolic scarcity": rejection is a performance of prestige. "This form of symbolic scarcity is not epistemically necessary." The scarcity is reputational, not technical. — [doi](https://doi.org/10.1186/s41073-026-00193-3)
- **Mechanism: three failure modes.**
  - "(1) a structural decoupling between epistemic contribution and publication outcomes driven by novelty-oriented symbolic selection;
  - (2) systematic waste of reviewer labor due to non-transferable and repetitive evaluation processes; and
  - (3) declining scalability of existing review infrastructures as generative AI lowers the cost of manuscript production while increasing evaluative load."
  - The analysis is explicitly "[r]ather than attributing dysfunction to individual actors or emerging technologies".
  - — [doi](https://doi.org/10.1186/s41073-026-00193-3)
- **AI section ("The coming tsunami: AI-accelerated submissions").**
  - LLMs assist with "literature consolidation, argument structuring, and stylistic refinement", and this raises submissions. Hansen calls this "a structural transition from scarcity in scientific output to rapid acceleration, a trend that places acute strain on the one element of the publishing system that has not been automated: human judgment."
  - "as surface quality becomes computationally cheap, the evaluative bottleneck will migrate deeper into the review pipeline."
  - "High selectivity has long served as a signal of quality, but when AI-generated manuscripts are polished … surface quality no longer reliably indicates epistemic merit."
  - "The bottleneck is no longer the scarcity of research output but the scarcity of interpretive attention."
  - "The central risk, however, is not a collapse of truthfulness but a collapse of integration."
  - — [doi](https://doi.org/10.1186/s41073-026-00193-3)
- **Evidence.** The paper is conceptual: "No data was used for this production". It concedes that "Empirical evidence on AI-driven changes to desk-rejection or acceptance rates remains limited". Its conclusion: "These developments do not indicate a collapse of the system". — [doi](https://doi.org/10.1186/s41073-026-00193-3)
- **Proposals.**
  - **Tiered publishing.** An integrity-filtered inclusion layer, plus "Prestige curation without scarcity", which relocates prestige "from the act of exclusion to the act of curation". Metrics would be computed on the curated layer only.
  - **Tiered review by "epistemic risk".** Soundness review by "trained graduate students, early-career researchers, staff reviewers"; full expert review for high-risk claims.
  - **Reviewer pay and recognition.** "Micro-payments, fellowships, or review-based stipends", and an optional "reviewer recognition ledger".
  - **AI screening at inclusion.** "uses computational capacity to manage computationally generated volume".
  - — [doi](https://doi.org/10.1186/s41073-026-00193-3)
- **AI-use disclosure.** "used ChatGPT 4o in order to improve the language of the paper." — [doi](https://doi.org/10.1186/s41073-026-00193-3)

### Inferences
- **How far Manabu overlaps the essay: high on the core premise, low on the five points.**
  - The essay's thesis 3, "almost free to produce, so it speeds up a failure that was already under way", is a plainer restatement of Manabu's "completed, and thereby destroyed".
  - The differences are in register and mechanism. Manabu argues from critical theory (doxa, performativity, apprenticeship). The essay works with concrete scarcities, signals and testable claims.
  - From the abstract, Manabu does not separate legitimate use from misuse (P1). He proposes no test (P2) and does not cite rationing measures (P3).
  - He touches P4 only through citations (Lindebaum et al. 2025; Ashraf et al. 2025). His "postdigital scholarly commons" is about institutions, not open tools (P5).
- **How far Hansen overlaps the essay: high on mechanism vocabulary, opposite on governance.**
  - His phrases "scarcity of interpretive attention" and "surface quality no longer reliably indicates epistemic merit" partly anticipate P1's signal argument.
  - His "symbolic scarcity" is the scarcity the essay would call prestige gatekeeping, and he wants it abolished.
  - The essay's claim is different: the scarcity the system relied on was in costly inputs (writing effort, reviewer time, mastery time). AI removes it, and institutions are now restoring it by decree. Hansen's paper is therefore a foil for P3 more than a precursor.
  - He was received in July 2025, before NIH's cap took effect and before arXiv's 2026 rules, so he could not discuss them.
- **Both are reflexivity precedents of a weak kind.** Manabu is AI-drafted and says so, but in an acknowledgement, not as part of the argument. Hansen used AI only for language editing.

### Gaps
- **Manabu's full text is unread** (subscription only; I found no open version). I cannot confirm whether the body:
  - separates legitimate from illegitimate use;
  - mentions NIH's or arXiv's caps;
  - discusses Big Tech in depth;
  - reflects on his own AI use.
  - The author should get the PDF through EMBL or UPF library access before submitting.
- **Hansen's citing works** could not be listed (Semantic Scholar rate limit).

---

## Q2. What other works (2023–2026) argue that generative AI breaks academic signalling or evaluation because outputs become cheap?

### Takeaway
The premise is now crowded.
- **Early statements (2023):** Carrigan on the LSE Impact Blog said gen-AI accelerates academic overproduction. Kingsley (also LSE Impact) said AI is a "scapegoat" holding "a mirror" to a broken system. Parrilla (*Nature*) said ChatGPT shows the grant system is broken.
- **2025–2026 wave:** Gartenberg et al. (*Organization Science*, journal data: +42% submissions); a *Nature* editorial (AI papers "shred" the effort–value correlation); Blekhman (*PLOS Biology*, published 15 Oct 2026: "paper counts are meaningless"); the *BISE* editors ("Stage 1" prompting "undermines writing quality as a screening signal"); Lang et al. ("enslopification"); Arndt & Zhang; Adeyeye (SSRN, signalling theory); Castellacci et al. (private versus social returns).
- **A formal economics literature (2025–2026)** models the costly-signal and certification mechanisms:
  - Galdin & Silbert, and Cowgill et al. (labour markets);
  - Hakobyan, Fourie, Lopez-Lira & Seyfi, Atasu, Shah (peer review, journals, quotas).

### Cited Findings

**A. Essays and editorials with nearly the essay's core premise (cheap outputs plus a system already under strain)**
- **Carrigan (2023), LSE Impact Blog, 14 Mar 2023 [full].**
  - Standfirst: ChatGPT as an "efficiency tool[] opens the door to further growth and acceleration in research outputs, but also raises questions about the value of these products of academic labour."
  - He asks: "Is there a risk that the capacity to automate aspects of the writing process will simply lead to more writing?"
  - "These are conditions in which technologies which change the time:output ratio could prove extremely seductive."
  - This is the earliest clear statement of "AI speeds up a pre-existing acceleration".
  - — [LSE Impact Blog](https://blogs.lse.ac.uk/impactofsocialsciences/2023/03/14/generative-ai-and-the-unceasing-acceleration-of-academic-writing/)
- **Kingsley (2023), "Generative AI – the latest scapegoat for research assessment", LSE Impact Blog, 13 Oct 2023 [full].**
  - "ChatGPT is simply holding a mirror to issues already plaguing the current scholarly publishing system".
  - "These concerns have an underlying assumption – the current system is working. We need to ask: is it?"
  - "The singular driver for almost all questionable research practices is the current emphasis on the published article as the only output that counts."
  - This is the canonical "exposes, not causes" essay.
  - — [LSE Impact Blog](https://blogs.lse.ac.uk/impactofsocialsciences/2023/10/13/generative-ai-the-latest-scapegoat-for-research-assessment/)
- **Parrilla (2023), "ChatGPT use shows that the grant-application system is broken", *Nature* 623:443 (Nature Careers Community column, 13 Oct 2023) [standfirst].**
  - Standfirst: "The fact that artificial intelligence can do much of the work makes a mockery of the process. It's time to make it easier for scientists to ask for research funding."
  - Search snippets (not verified against the full text) say he used ChatGPT himself on a proposal.
  - — [doi:10.1038/d41586-023-03238-5](https://doi.org/10.1038/d41586-023-03238-5)
- **Gartenberg, Hasan, Murray & Pierce (2026), "More Versus Better: Artificial Intelligence, Incentives, and the Emerging Crisis in Peer Review", *Organization Science* 37(3):795–812 (editorial essay by the journal's AI Task Force) [abstract].**
  - "Submission volume has risen 42% since the late 2022 release of ChatGPT, while writing quality has declined. The rise in AI-generated writing accounts for nearly all of these trends."
  - AI-written reviews show "lower writing quality and less topical diversity".
  - "we cannot make a normative assessment about appropriate or ideal levels of AI usage."
  - "the current state of AI tools, amplified by existing publish-or-perish incentives, appears to be pushing the system toward an equilibrium of more rather than better research."
  - By mid-October 2026 Semantic Scholar listed at least 30 citing works.
  - — [doi:10.1287/orsc.2026.ed.v37.n3](https://doi.org/10.1287/orsc.2026.ed.v37.n3)
- **Nature Editorial (2026), "AI scientists are changing research — institutions, funders and publishers must respond", *Nature* 651:853–854, 25 Mar 2026 [partial; open page].**
  - "the effects of being able to generate research papers quickly and cheaply are rippling through the scientific ecosystem".
  - "AI-generated papers shred the long-standing (if rough) correlation between authors applying effort and the work having value. No one has worked out how to account for AI-inflated outputs in hiring and promotion decisions".
  - "There is a risk that the ease of AI-based investigations could skew science towards certain fields and types of research, particularly in data-rich domains — potentially reducing scientific diversity."
  - — [doi:10.1038/d41586-026-00934-w](https://doi.org/10.1038/d41586-026-00934-w)
- **Blekhman (2026), "What is biology research for?", *PLOS Biology* 24:e3004075, Perspective, published 15 Oct 2026 (today) [full].**
  - "In the age of generative artificial intelligence (AI), the assumption that writing a paper requires doing science no longer holds true."
  - The paper "has come loose from the science it was meant to represent".
  - Paper-based evaluation "took hold because a paper took effort to produce, and that effort served as evidence".
  - "Generative AI has broken this already-flawed proxy completely. A plausible paper can now be produced in a day".
  - "there are no brakes on the system: scientists will keep generating more and more papers because their careers depend on it; publishers will keep publishing them …; and AI companies will happily keep selling the tokens that enable it."
  - He predicts that evaluation "will fall back on older, cruder proxies, such as journal prestige and impact factor, which would undo the past decade of research assessment reform".
  - He proposes that the field "acknowledge that paper counts are meaningless" and "abandon the current incentive system".
  - The author sits on *PLOS Biology*'s editorial board and writes from biology, which is likely the essay author's field.
  - — [doi:10.1371/journal.pbio.3004075](https://doi.org/10.1371/journal.pbio.3004075)
- **Hanneke, Hering, Pfeiffer, Reijers & Hinz (2026), "Academic Publishing in the Age of Generative AI", *Business & Information Systems Engineering* 68(4):729–737, editorial, open access [full, skimmed].**
  - Journals "turn a growing universe of ideas into credible scientific signals". "This task rests on three limited resources: editorial attention, reviewer time, and audience attention".
  - "GenAI reduces the effort required to create manuscripts." "When the costs of producing submission-ready manuscripts decrease substantially, the work on the reviewers' side increases inversely."
  - **"Stage 1 GenAI usage undermines writing quality as a screening signal."** Stage 1 is "simple prompting", whose human objective is to "Improve research content and speed".
  - "Detection tools offer little relief … and disclosure requirements remain fragile".
  - They propose submission fees and treating agentic pipelines as first-class contributions.
  - — [doi:10.1007/s12599-026-01013-0](https://doi.org/10.1007/s12599-026-01013-0)
- **Lang, Moffett & Vasudevan (2025), "The Architecture of Academic Overproduction: Toward Post-AI Scholarship", in *Digital Humanism* (LNCS), pp. 483–498, open access (CC BY-NC-ND) [full, skimmed].**
  - Generative AI will "further intensify these dynamics through both 'flattening' (the homogenization and proliferation of scholarly writing) and 'enslopification,' defined as the mass production of low-quality academic content optimized for metrics rather than insight".
  - "Rather than simply blaming digital technologies or AI, we argue that quantification pressures, institutional incentives, and the commodification of research have primed the academy for a crisis of relevance and authenticity."
  - — [doi:10.1007/978-3-032-11108-1_36](https://doi.org/10.1007/978-3-032-11108-1_36)
- **Arndt & Zhang (2026), "Too Much to Review? When Production Outpaces Consumption", *Canadian Journal of Administrative Sciences* 43 [abstract].**
  - "The adoption of generative AI has led to a steep increase in submissions that exposes a structural imbalance beneath it. We argue that this imbalance is not technological in nature, but reflects a deeper misalignment that performativity has brought to scholarly work."
  - — [doi:10.1002/cjas.70082](https://doi.org/10.1002/cjas.70082)
- **Kapoor & Narayanan (2025), "Could AI slow science? Confronting the production-progress paradox", essay, 16 Jul 2025 [full, mostly read].**
  - "Even if individual scientists benefit from adopting AI, it doesn't mean science as a whole will benefit."
  - "So far, on balance, AI has been an unhealthy shock to science, stretching many of its processes to the breaking point."
  - Funders and companies "are simply trying to accelerate production, which is like adding lanes to a highway when the slowdown is actually caused by a toll booth."
  - "career incentives lead to researchers publishing more papers, and disincentivize novel research".
  - — [AI Snake Oil essay](https://www.aisnakeoil.com/p/could-ai-slow-science); [Princeton CITP listing](https://citp.princeton.edu/news/2025/could-ai-slow-science-confronting-production-progress-paradox) (returned HTTP 403 to automated fetch; known only from search results)
- **Castellacci, Ciarli, Gao, Marino, Marzi & Riccaboni (2026), arXiv:2607.24879 [abstract].**
  - "AI-assisted work shows measurable gains in publication volume and citation share, while the evidence on novelty, disruption, and breakthrough output remains ambiguous or negative."
  - "the divergence between private and social returns arises through three analytically distinct mechanisms, namely information asymmetry, negative externalities on a shared knowledge base, and depletion of research capacity".
  - They propose "Responsible Research with AI" (disclosure, differentiation, narrative, proportionality).
  - — [arXiv:2607.24879](https://arxiv.org/abs/2607.24879)
- **Adeyeye (2026), "The Devaluation of the Publication Signal: A Secondary-Data Analysis of AI's Impact on Academic Credentialing, 2022 to 2026, with Projections to 2036", SSRN preprint [abstract].**
  - Applies Spence's signalling theory. The publication signal "has worked precisely because producing it convincingly has been costly". Gen-AI "lowered the cost of producing something that resembles a publication without a corresponding increase in genuine scholarly effort".
  - Concludes that publication count "is likely to stop functioning sufficiently on its own".
  - — [doi:10.2139/ssrn.7259758](https://doi.org/10.2139/ssrn.7259758)
- **Dey (2026), "AI Isn't Breaking Peer Review—It Is Exposing That the System Was Already Broken", Springer Nature Research Communities, 30 Jun 2026 [full].**
  - "The real challenge is not AI itself, but an overburdened, unpaid review system."
  - "The real question is not 'Who is using AI?' but 'Why has the system reached a point where reviewers feel they need AI to complete their reviews?'"
  - — [Springer Nature Communities](https://communities.springernature.com/posts/ai-isn-t-breaking-peer-review-it-is-exposing-that-the-system-was-already-broken)

**B. Costly signalling and "effort as signal" (formal and empirical)**
- **Galdin & Silbert (2025), "Making Talk Cheap: Generative AI and Labor Market Signaling", arXiv:2511.08785 [abstract].**
  - LLMs "disrupt markets that traditionally relied on writing as a costly signal of quality (e.g., job applications, college essays)".
  - On Freelancer.com, employers valued customised applications "before LLMs are introduced, but not after".
  - Without costly signalling, "workers in the top quintile … are hired 19% less often, workers in the bottom quintile are hired 14% more often".
  - This is the cleanest evidence for the mechanism, from a non-academic market.
  - — [arXiv:2511.08785](https://arxiv.org/abs/2511.08785)
- **Cowgill, Hernández-Lagos & Wright (2026), "Does AI Cheapen Talk?", *Management Science* (articles in advance) [abstract].**
  - "Signals are often informative insofar as they require differential knowledge and effort to produce."
  - Senders' access to ChatGPT "lowers screening accuracy by 4%–9%". It improves accuracy for senders from non-English-speaking countries.
  - — [doi:10.1287/mnsc.2024.07027](https://doi.org/10.1287/mnsc.2024.07027)
- **Kusumegi et al. (2025), *Science* 390:1240–1243 [verified in `research_notes/AI disruption of academia literature/2_ai_impact_on_academia.md`; DOI re-checked here].** LLM adoption raises output and helps non-native writers. Linguistic complexity becomes a less reliable signal of quality. — [doi:10.1126/science.adw3000](https://doi.org/10.1126/science.adw3000)
- **Hakobyan (2026), "Buying the Right to Monitor: Editorial Design in AI-Assisted Peer Review", arXiv:2604.23645 [abstract].**
  - AI enters "both sides of the market".
  - "when AI capability crosses a critical threshold, reviewer effort collapses discontinuously". Authors benefit from a weakened "rat race", while editors face "degraded signal informativeness".
  - After the transition, editors "must loosen acceptance standards while investing in AI detection".
  - — [arXiv:2604.23645](https://arxiv.org/abs/2604.23645)
- **Payan, Gyevnár, Kasirzadeh & Shah (2026), "greCAPTCHA", arXiv:2609.20481 [abstract].** "institutions evaluating submissions can no longer reliably credit expertise based solely on authors' names on submitted work". They propose a proctored test of authors' understanding as a new, costly signal. — [arXiv:2609.20481](https://arxiv.org/abs/2609.20481)

**C. Economics of attention, certification and journal policy**
- **Fourie (2026), "The Value of Peer Review and the Reward to Reputation", arXiv:2607.13844 (v3, 31 Aug 2026) [full, skimmed].**
  - "Writing a plausible manuscript is now largely rule-based …; judging one is not."
  - "whatever part of writing can be reduced to rules, anyone can produce, and whatever part of evaluation can be reduced to rules, anyone can pass."
  - "Review is therefore rationed, not priced."
  - "A journal that keeps its stamp scarce by rejecting what it cannot read is not thereby protecting the stamp's value".
  - "Rationing expert attention is therefore not a back-office decision … It sets what a credential is worth".
  - The point extends to "Grant panels, hiring committees, accreditation bodies".
  - — [arXiv:2607.13844](https://arxiv.org/abs/2607.13844)
- **Lopez-Lira & Seyfi (2026), "One Prompt, One Paper: Should Academic Journals Expand Capacity with Generative AI?", SSRN [abstract].**
  - "Without policy adjustment, submissions flood the system and acceptance rates collapse."
  - With optimal fees, "Only 3% of the optimal fee internalizes direct review costs; the remaining 97% reflects congestion screening and prestige stabilization".
  - Fourie cites a different title for it ("…Optimal Journal Policy and the AI Submission Flood"), so versions differ.
  - — [doi:10.2139/ssrn.6337880](https://doi.org/10.2139/ssrn.6337880)
- **Atasu (2026), "AI and Publication Commons", SSRN / INSEAD working paper [abstract].**
  - AI "can reduce the cost of producing academic content, and increase submissions", "congesting reviewer capacity and in turn, degrading review accuracy".
  - Proposes "submission and AI-use contingent fees, and reviewer compensation", or a two-track mechanism.
  - — [doi:10.2139/ssrn.6393158](https://doi.org/10.2139/ssrn.6393158)
- **Shah (2026), "How Many Submissions May an Author Make? A Harmonic Quota…", arXiv:2606.10293 [abstract].**
  - Evaluators "are increasingly using author-level submission limits to manage growing submission loads". Shah designs fairer quotas and notes their use in "other scarce-resource allocation settings".
  - — [arXiv:2606.10293](https://arxiv.org/abs/2606.10293)
- **Nee, Zhong & Ni (2026), arXiv:2609.04872 [abstract].**
  - arXiv mathematics in 2026 had "47,127 list entries, 33.5% above 2025 and 11.9% above a synthetic counterfactual". The share of authors with five or more submissions rose from 2.45% to 3.80%.
  - "The findings locate verification, selection, and attention as central constraints for research governance."
  - — [arXiv:2609.04872](https://arxiv.org/abs/2609.04872)
- **Bhargava et al. (2026), *Management Science* 72:7381–7393 [abstract].** Author AI use "has accelerated production of academic articles and increased submission rates to journals, thereby straining review capacity". They propose LLM front-line reviewers. — [doi:10.1287/mnsc.2026.00184](https://doi.org/10.1287/mnsc.2026.00184)
- **Shan et al. (2026), ICML 2026 Position track, arXiv:2605.09915 [abstract].** "Agentic Denominator Gaming": AI agents flood submissions to dilute fixed acceptance rates. "durable protection will require system-level policy and incentive reforms". This is a misuse framing. — [arXiv:2605.09915](https://arxiv.org/abs/2605.09915)
- **Sankaralingam (2025), arXiv:2512.14104 [abstract].** Conferences fail under "two irreconcilable roles: (1) rapid dissemination of all sound research and (2) scarce credentialing". He proposes an "Impact Market". — [arXiv:2512.14104](https://arxiv.org/abs/2512.14104)
- **Zhang, Xuegong (2026), "The future of peer review requires AI support, not AI bans", *Nature* 656:1070 [standfirst; article type not confirmed].** "Submission volumes are rising … it's becoming harder to get reviewers". Argues against blanket bans on reviewer AI use. — [doi:10.1038/d41586-026-02631-0](https://doi.org/10.1038/d41586-026-02631-0)

**D. "The paper or the CV is obsolete"**
- **Blekhman (2026)**, above: "paper counts are meaningless". — [doi](https://doi.org/10.1371/journal.pbio.3004075)
- **Nature Editorial (2026)**, above: AI-inflated outputs and hiring/promotion. — [doi](https://doi.org/10.1038/d41586-026-00934-w)
- **Payan et al. (2026)**, above: names on papers no longer credit expertise. — [arXiv](https://arxiv.org/abs/2609.20481)
- I found no 2023–2026 essay arguing specifically that the **CV** is obsolete. Somers (2018, *The Atlantic*), "The scientific paper is obsolete", predates generative AI; it is already in `research_notes/AI disruption of academia literature/4_governance_and_reform.md`.

**E. Coverage of the venues named in the brief**
- ***Nature* opinion and news.**
  - Spirling 2023 (World View) — [doi:10.1038/d41586-023-01295-4](https://doi.org/10.1038/d41586-023-01295-4)
  - Parrilla 2023 (Careers column)
  - Xizhe Zhang 2026 (World View; see Q4)
  - Huang et al. 2026 (Comment; see Q4)
  - Editorial, 25 Mar 2026
  - Storey 2026 (News & Views on Hao et al.) — [doi:10.1038/d41586-025-04092-3](https://doi.org/10.1038/d41586-025-04092-3)
  - Singh Chawla 2026 (news on arXiv's cap; see Q4)
  - Brzostowicki 2026 (technology feature on local models; see Q4)
- ***PLOS Biology*.**
  - Blekhman 2026 (Perspective).
  - Suchak et al. 2025 (research article): AI-ready datasets such as NHANES enable "large numbers of formulaic single-factor analyses". — [doi:10.1371/journal.pbio.3003152](https://doi.org/10.1371/journal.pbio.3003152)
  - Routledge & Pariente 2025, "On improving the sustainability of peer review" — [doi:10.1371/journal.pbio.3003127](https://doi.org/10.1371/journal.pbio.3003127) [title]
- ***eLife*.** I found no essay on this topic.
- ***Postdigital Science and Education*.**
  - Manabu 2026.
  - Jandrić 2026 (the journal's GenAI policy) — [doi](https://doi.org/10.1007/s42438-026-00641-9)
  - Hayes 2026, "Good Scars and Bad Scars: Beyond 'Algorithmic Insistence' in Academic Peer Review" — [doi:10.1007/s42438-026-00651-7](https://doi.org/10.1007/s42438-026-00651-7) [title]
  - Jandrić & Forsler 2026 on the form of the scholarly article — [doi:10.1007/s42438-026-00652-6](https://doi.org/10.1007/s42438-026-00652-6) [abstract]
  - Cachipuendo-Contero 2026 [title]
  - Holster 2026 [title]
- ***Research Integrity and Peer Review*.**
  - Hansen 2026.
  - Cwik 2026, "Disclosure is not documentation" — [doi:10.1186/s41073-026-00245-8](https://doi.org/10.1186/s41073-026-00245-8) [abstract]
  - Hosseini & Horbach 2023 on LLMs in peer review (verified in `4_journal_venues.md` in this folder).
- ***Learned Publishing*, *Minerva*, Upstream.** Searches found nothing that makes the essay's thesis (see Gaps).
- **LSE Impact Blog.** Carrigan 2023; Kingsley 2023.
- **A large 2026 wave in management and information-systems journals.** Beyond Gartenberg, Arndt & Zhang, Bhargava and Hanneke:
  - Manning 2026 (see Q4).
  - "Research Integrity Matters, But It Is Undermined by Generative AI" (*Information Systems Journal*), listed among Gartenberg's citing works [title only].

### Inferences
- **The core premise is no longer new.** "AI makes counted outputs cheap and accelerates a failure already under way" is shared by at least a dozen pieces from 2023–2026. The 2023 LSE posts and Parrilla came first. Manabu, Gartenberg et al., the *Nature* editorial and Blekhman state it most forcefully.
- **The signal argument is partly made.**
  - The legitimate-use version appears only in pieces: Kusumegi (empirical); *BISE* "Stage 1"; Parrilla (grants); Galdin & Silbert and Cowgill (non-academic markets).
  - The more common framing is "plausible papers without real research" (Blekhman; Adeyeye; Hansen's "shallow"; Shan et al.'s malicious agents).
- **The economics literature gives the essay formal backing.** Fourie, Lopez-Lira & Seyfi, Atasu, Hakobyan and Galdin & Silbert supply the models behind informal claims the essay makes. Citing them would strengthen the essay and stop it appearing to rediscover their results.
- **Blekhman (published today, in biology, in *PLOS Biology*) is now arguably the closest prior work for a life-sciences reader.** It should be cited alongside Manabu and Hansen.

### Gaps
- OpenAlex (shared budget exhausted) and Semantic Scholar (rate-limited) were largely unavailable, so this inventory cannot be guaranteed complete. The fast-growing management, information-systems and economics editorial literature citing Gartenberg et al. (30 or more items) was sampled, not read.
- Not covered:
  - site-level searches of *Learned Publishing*, *Minerva*, *eLife* and Upstream;
  - non-English literature;
  - Times Higher Education and The Scholarly Kitchen. For the latter, only the title of Bruno's 18 Mar 2026 guest post was verified — [Scholarly Kitchen](https://scholarlykitchen.sspnet.org/2026/03/18/guest-post-could-ai-help-fix-peer-review-or-will-it-only-make-things-worse/).
- Parrilla's full text was not read (paywall). The claim that he used ChatGPT on his own proposal comes from search snippets only.

---

## Q3. Has anyone published a reflexive or "demonstration" paper written openly with AI about AI in academia, and how was it received?

### Takeaway
Yes, several. The essay cannot claim to be the first.
- **Stunts revealed after the fact:** Osmanovic Thunström 2022 (GPT-3 writes about itself); Cotton et al. 2023 (a paper on ChatGPT and cheating, written by ChatGPT).
- **A "proof of principle" with formal open peer commentary:** Porsdam Mann et al. 2023 (AUTOGEN, a personalised LLM for academic writing).
- **Whole venues and systems:** Agents4Science 2025 (AI as first authors and reviewers); Sakana's AI Scientist, published in *Nature* in 2026 with an editorial.
- **AI-agent-assisted papers about evaluation, disclosed:**
  - Fourie 2026: "Claude Code and OpenAI's Codex assisted with derivations, drafting, literature search, computational verification and adversarial review". This is nearly the brief's own division of labour.
  - Manabu 2026, drafted with Perplexity.
- **Reception has ranged** from media alarm (Cotton) to structured debate (AUTOGEN) and cautious welcome with criticism (*Nature* on the AI Scientist).
- **What I did not find:** a paper that makes its own production record (version history, time, cost, a conflict-of-interest note) part of the evidence for its thesis.

### Cited Findings
- **Osmanovic Thunström (2022) [title; before the 2023–2026 window].** Scientific American essay "We Asked GPT-3 to Write an Academic Paper about Itself—Then We Tried to Get It Published". It is the precedent for "AI writes about AI in academia". — [Scientific American](https://www.scientificamerican.com/article/we-asked-gpt-3-to-write-an-academic-paper-about-itself-mdash-then-we-tried-to-get-it-published/)
- **Cotton, Cotton & Shipway (2023/2024), "Chatting and cheating: Ensuring academic integrity in the era of ChatGPT", *Innovations in Education and Teaching International* 61:228–239 [metadata + news coverage].**
  - The Guardian/Observer reported: "What readers – and indeed the peer reviewers who cleared it for publication – did not know was that the paper itself had been written by … ChatGPT."
  - Cotton told the paper: "We wanted to show that ChatGPT is writing at a very high level … This is an arms race."
  - A Dutch university news item seen only in search results disputes that readers were not told. I did not read the paper's disclosure.
  - — [doi:10.1080/14703297.2023.2190148](https://doi.org/10.1080/14703297.2023.2190148); [The Guardian, 19 Mar 2023](https://www.theguardian.com/technology/2023/mar/19/ai-makes-plagiarism-harder-to-detect-argue-academics-in-paper-written-by-chatbot)
- **Porsdam Mann, Earp, Møller, Vynn & Savulescu (2023), "AUTOGEN: A Personalized Large Language Model for Academic Enhancement—Ethics and Proof of Principle", *American Journal of Bioethics* 23:28–41 [metadata].**
  - Received open peer commentary, including Erler (2023), "Publish with AUTOGEN or Perish? Some Pitfalls to Avoid in the Pursuit of Academic Enhancement via Personalized Large Language Models", *AJOB* 23:94–96.
  - The authors replied: "AUTOGEN and the Ethics of Co-Creation with Personalized LLMs—Reply to the Commentaries" (2024).
  - — [doi:10.1080/15265161.2023.2233356](https://doi.org/10.1080/15265161.2023.2233356); [Erler doi:10.1080/15265161.2023.2250291](https://doi.org/10.1080/15265161.2023.2250291); [reply doi:10.1080/15265161.2024.2308175](https://doi.org/10.1080/15265161.2024.2308175)
- **Bianchi, Queen, Thakkar, Sun & Zou (2025), "Exploring the use of AI authors and reviewers at Agents4Science", arXiv:2511.15534 [abstract].** "the first conference in which AI agents serve as both primary authors and reviewers, with humans as co-authors and co-reviewers". — [arXiv:2511.15534](https://arxiv.org/abs/2511.15534)
- **Lu et al. (2026), "Towards end-to-end automation of AI research", *Nature* 651:914–919, and the *Nature* editorial of 25 Mar 2026 [editorial partly read].**
  - "The AI Scientist produced three papers, one of which, following peer review, reached the bar for acceptance at a workshop".
  - Peer review led the *Nature* version to tone "down the authors' original statements about automating the entire research process (humans helped to filter the most promising outputs)".
  - — [doi:10.1038/s41586-026-10265-5](https://doi.org/10.1038/s41586-026-10265-5); [Editorial doi:10.1038/d41586-026-00934-w](https://doi.org/10.1038/d41586-026-00934-w)
- **Fourie (2026), arXiv:2607.13844 [full, skimmed].**
  - Title-page note: "I chose the question, assumptions and argument. Anthropic's Claude Code and OpenAI's Codex assisted with derivations, drafting, literature search, computational verification and adversarial review. I reviewed every claim and remain responsible for all errors."
  - The arXiv comment field reads "AI use disclosed in the paper".
  - — [arXiv:2607.13844](https://arxiv.org/abs/2607.13844)
- **Manabu (2026)**: drafted with Perplexity, disclosed in the acknowledgements (Q1). — [doi](https://doi.org/10.1007/s42438-026-00666-0)
- **The disclosure-design debate the essay's "How this paper was made" box enters:**
  - *Nature* "encourages researchers to submit transcripts of prompts and model responses alongside the final outputs" when a model contributes creatively — [Editorial](https://doi.org/10.1038/d41586-026-00934-w)
  - Earp, Schüklenk, Savulescu & Porsdam Mann (2026), "Against mandatory prompt disclosure in AI-assisted scholarship", *AI & Society*. They support detailed disclosure "when it is needed to assess the scientific validity or reproducibility of a study" — [doi:10.1007/s00146-026-03326-w](https://doi.org/10.1007/s00146-026-03326-w) [abstract]
  - Cwik (2026): "disclosure alone rarely clarifies how AI-assisted work was performed" — [doi:10.1186/s41073-026-00245-8](https://doi.org/10.1186/s41073-026-00245-8) [abstract]

### Inferences
- **The "paper as its own example" design has precedents, so it should be pitched as an *improvement in documentation*, not as a first.**
  - Fourie's footnote matches the brief's planned division of labour almost word for word (author: question and argument; agents: drafting, literature search, adversarial review).
  - What would distinguish the essay is making the record *evidence for the thesis*:
    - the git history as an auditable process record;
    - time and cost as a measured instance of "almost free to produce";
    - the Anthropic conflict of interest.
  - None of the precedents found does that.
- **Reception lessons.**
  - Covert or after-the-fact reveals (Cotton) get framed as integrity scandals.
  - Upfront proofs of principle (AUTOGEN) attract critical commentary, but within a scholarly frame.
  - Venue-level showcases (*Nature*/AI Scientist) are published with editorial caveats.
  - Openness up front, plus a process record, puts the essay in the second or third pattern, not the first.

### Gaps
- No reception data (commentaries, rejections, reviews) exist yet for Fourie or Manabu beyond the counts in Q1. I did not verify how Agents4Science papers were received beyond the organisers' report.
- I did not find, and so cannot rule out, other 2026 papers openly co-written with AI agents about academia. This is a fast-moving category.

---

## Q4. Has anyone argued the essay's five points?

### Takeaway
- **P1 (legitimate use breaks the system): partly anticipated, substantially.**
- **P2 (acceleration, not exploration): the claim has already been made** (*Nature* Comment by Huang et al., 29 Sep 2026; Xizhe Zhang's World View, Jun 2026; Kapoor & Narayanan 2025; Messeri & Crockett 2024). **The triple-difference test is new.**
- **P3 (rationing): partly anticipated** (Fourie's "rationed, not priced"; the fee and quota models; arXiv-cap critics). Reading NIH, arXiv and conference caps together as "restoring scarcity by decree" appears new.
- **P4 (two drivers): partly anticipated on each side.** The explicit internal/external decomposition, with chat data as a channel, appears new.
- **P5 (open tools): largely anticipated as general advocacy.** It is new only as the condition linking open tools to the exploration vision.

### Cited Findings

**P1 — even legitimate use breaks the system. Verdict: partly anticipated (substantially).**
- *BISE* editors: "Stage 1 GenAI usage [ad hoc prompting to 'Improve research content and speed'] undermines writing quality as a screening signal." The three scarce resources are "editorial attention, reviewer time, and audience attention". — [doi:10.1007/s12599-026-01013-0](https://doi.org/10.1007/s12599-026-01013-0)
- Kusumegi et al.: legitimate gains (output; help for non-native writers) erode the complexity signal. — [doi:10.1126/science.adw3000](https://doi.org/10.1126/science.adw3000)
- Parrilla: ChatGPT's usefulness for grant documents shows the process is broken. — [doi:10.1038/d41586-023-03238-5](https://doi.org/10.1038/d41586-023-03238-5)
- Galdin & Silbert, and Cowgill et al.: legitimate use destroys costly signals, outside academia. — [arXiv:2511.08785](https://arxiv.org/abs/2511.08785); [doi:10.1287/mnsc.2024.07027](https://doi.org/10.1287/mnsc.2024.07027)
- Fourie: "Writing a plausible manuscript is now largely rule-based". — [arXiv:2607.13844](https://arxiv.org/abs/2607.13844)
- Gartenberg et al. decline to judge "appropriate or ideal levels of AI usage" yet find the system pushed to "more rather than better". — [doi](https://doi.org/10.1287/orsc.2026.ed.v37.n3)
- Hansen: legitimate assistance ("literature consolidation, argument structuring, and stylistic refinement") drives volume, and "surface quality no longer reliably indicates epistemic merit". — [doi](https://doi.org/10.1186/s41073-026-00193-3)
- **Contrast.** Blekhman, Adeyeye, Shan et al. and the *Nature* editorial frame the problem mainly as papers produced *without* real research (low effort, slop, malicious agents). — [Blekhman](https://doi.org/10.1371/journal.pbio.3004075); [Adeyeye](https://doi.org/10.2139/ssrn.7259758); [Shan et al.](https://arxiv.org/abs/2605.09915)
- **The "time to master a literature" scarcity.** Huang et al. treat it as an *opportunity*: "AI tools reduce the informational cost of pivoting … But evaluation systems still penalize pivots". Manabu's severed "apprenticeship pathway" is related. I found no one treating the loss of mastery time as the loss of a *gatekeeping signal*. — [doi:10.1038/d41586-026-02961-z](https://doi.org/10.1038/d41586-026-02961-z); [Manabu](https://doi.org/10.1007/s42438-026-00666-0)

**P2 — "acceleration, not exploration" at the level of the whole system. Verdict: the claim has already been made; the test is new.**
- **Huang, Hu, Zhang & Lin (2026), "AI can widen science — but only if institutions stop rewarding the already measurable", *Nature* 658:32–33, Comment, online 29 Sep 2026 [partial; text cut by a registration wall after the second of three recommendations].**
  - "individual researchers are becoming more productive, while the scientific enterprise as a whole is exploring a narrower range of ideas."
  - "The problem is not technological, but institutional. AI tools expand scientists' capacity to explore, but systemic incentives mean that researchers use this capability to focus more intensely on problems that institutions can easily recognize, evaluate and reward".
  - "These dynamics did not originate with AI … But AI is accelerating these changes".
  - "AI makes extending a familiar research line faster and cheaper than entering unfamiliar terrain, and existing incentive systems reward such speed."
  - They *also* invoke the data channel: "funding systems overwhelmingly reward the downstream exploitation of existing data". AI prediction costs "have fallen roughly 100-fold in the past two years".
  - Recommendations seen: subsidise new data infrastructure; stop penalising pivots.
  - — [doi:10.1038/d41586-026-02961-z](https://doi.org/10.1038/d41586-026-02961-z)
- **Xizhe Zhang (2026), "Will AI spark a scientific renaissance — or a diffuse monoculture?", *Nature* 654:843, World View, 22 Jun 2026 [standfirst].** Enrichment "will depend not only on model capability, but also on whether researchers, reviewers and funders reward originality over speed." — [doi:10.1038/d41586-026-01954-2](https://doi.org/10.1038/d41586-026-01954-2)
- **Kapoor & Narayanan (2025)**, above: individual gains are not system gains; the incentive feedback loop. — [essay](https://www.aisnakeoil.com/p/could-ai-slow-science)
- **Messeri & Crockett (2024), *Nature* 627:49–58 [abstract].** AI tools risk "scientific monocultures, in which some types of methods, questions and viewpoints come to dominate alternative approaches" and "a phase of scientific enquiry in which we produce more but understand less." — [doi:10.1038/s41586-024-07146-0](https://doi.org/10.1038/s41586-024-07146-0)
- **Hao, Xu, Li & Evans (2026), *Nature* 649:1237–1243, with Storey's News & Views.**
  - AI "automates established fields rather than supporting the exploration of new ones" (Storey).
  - Per `3_testing_acceleration_hypothesis.md` in this folder, the authors' own analysis finds data availability the main driver of where AI concentrates ("collective hill-climbing").
  - — [doi:10.1038/s41586-025-09922-y](https://doi.org/10.1038/s41586-025-09922-y); [Storey doi:10.1038/d41586-025-04092-3](https://doi.org/10.1038/d41586-025-04092-3); [arXiv v4](https://arxiv.org/html/2412.07727v4)
- **Also:** the *Nature* editorial's skew toward "data-rich domains"; Gartenberg et al.'s "more rather than better"; Castellacci et al.'s ambiguous or negative novelty evidence; Lang et al.'s "flattening". — [Editorial](https://doi.org/10.1038/d41586-026-00934-w); [Gartenberg](https://doi.org/10.1287/orsc.2026.ed.v37.n3); [Castellacci](https://arxiv.org/abs/2607.24879); [Lang](https://doi.org/10.1007/978-3-032-11108-1_36)
- **Caution on homogenisation evidence.** Burtch (2026) finds AI "homogeniz[es] how Kaggle contestants express their solutions, not the problem-solving strategies they employ" (syntax, not semantics). — [arXiv:2607.13077](https://arxiv.org/abs/2607.13077)
- **Test.** I found no proposed or run test that separates metric incentives from data affordance by exploiting variation in incentive strength. This matches `3_testing_acceleration_hypothesis.md` in this folder, which also found none.

**P3 — governance is rationing that restores scarcity by decree. Verdict: partly anticipated; the cross-institution synthesis appears new.**
- **Fourie** frames review as "rationed, not priced". He analyses "rationing by capacity" (rejecting unread papers) and argues that keeping a stamp scarce this way can *lower* its value. He extends the logic to grant panels and hiring. The frame is journal-level and model-based; he does not discuss NIH or arXiv. — [arXiv:2607.13844](https://arxiv.org/abs/2607.13844)
- **Pricing as the alternative to rationing.**
  - Lopez-Lira & Seyfi: 97% of the optimal fee is "congestion screening and prestige stabilization" — [doi](https://doi.org/10.2139/ssrn.6337880)
  - Atasu: fees plus reviewer compensation — [doi](https://doi.org/10.2139/ssrn.6393158)
  - *BISE*: submission fees "as refundable deposits or in tiered structures" — [doi](https://doi.org/10.1007/s12599-026-01013-0)
- **Quota design.** Shah treats author-level limits as allocating a scarce resource. — [arXiv:2606.10293](https://arxiv.org/abs/2606.10293)
- **News coverage of the caps: Singh Chawla (2026), "ArXiv versus AI slop: will capping preprint submissions work?", *Nature* news, 15 Oct 2026 [partial].**
  - arXiv "announced a cap of two papers per month for each submitting researcher, which began on 1 October".
  - "In September, 40,000 preprints were uploaded … up from about 30,000 between March and July". About 300 volunteer moderators check about 1,000 manuscripts a day. The backlog is "holding up too many legitimate papers".
  - "SocArXiv … now also restricts submissions to one article per author per week". "some major AI conferences and journals have turned to similar submission quotas".
  - Critics: rejected papers "will simply go somewhere else and become someone else's problem" (Khalil); limits can be gamed by co-authors taking turns (Galitski).
  - — [doi:10.1038/d41586-026-03194-w](https://doi.org/10.1038/d41586-026-03194-w)
- **Opposed or orthogonal positions.**
  - Hansen would abolish symbolic scarcity ("Prestige curation without scarcity") — [doi](https://doi.org/10.1186/s41073-026-00193-3)
  - Hakobyan: editors "must loosen acceptance standards" — [arXiv](https://arxiv.org/abs/2604.23645)
  - Blekhman predicts a fallback to "older, cruder proxies, such as journal prestige" — a non-decree route back to scarcity — [doi](https://doi.org/10.1371/journal.pbio.3004075)
- **Not found:** any work reading NIH's six-application cap, arXiv's rules and conference quotas *together* as decree-based restoration of a lost cost.

**P4 — two drivers of narrowing. Verdict: each driver partly anticipated; the decomposition appears new.**
- **The internal driver (incentives)** is made by Huang et al., Xizhe Zhang, Kapoor & Narayanan, and Gartenberg et al. (see P2).
- **The external driver (corporate control of tools).**
  - **Chesterman & Loy (2026), arXiv:2601.05574 [abstract].** "the centre of gravity in AI research has moved decisively from universities to private laboratories with privileged access to data, compute, and engineering talent. As frontier models become increasingly proprietary and opaque, universities face growing difficulty interrogating, reproducing, or contesting the systems on which scientific inquiry increasingly depends." — [arXiv:2601.05574](https://arxiv.org/abs/2601.05574)
  - **Manning (2026), *Critical Perspectives on International Business* [abstract].** AI's "democratizing effect" coexists with rising "efficiency pressures". "Investments by powerful institutions and corporations, particularly in the USA, Western Europe and China, reinforce and exploit these dynamics". One scenario is "a higher-pressure version of today's system … dominated by resource-rich universities". — [doi:10.1108/cpoib-06-2026-0166](https://doi.org/10.1108/cpoib-06-2026-0166)
  - **Lindebaum et al. (2025), *Organization Studies* [abstract].** LLMs alter "who produces knowledge, how knowledge is produced … and what kind of knowledge is produced", toward "organized immaturity". — [doi:10.1177/01708406251392002](https://doi.org/10.1177/01708406251392002)
  - **Cachipuendo-Contero (2026), PSE: "Language Relief at The Cost of Infrastructural Dependency" [title only].** — [doi:10.1007/s42438-026-00672-2](https://doi.org/10.1007/s42438-026-00672-2)
- **The chat-data angle.** Brzostowicki (2026), a *Nature* technology feature, reports:
  - "A 2025 analysis found that the six AI developers studied — Amazon, Anthropic, Google, Meta, Microsoft and OpenAI — trained their models on users' input data by default".
  - One researcher: "I do not want Claude to start telling people my research results".
  - — [doi:10.1038/d41586-026-03227-4](https://doi.org/10.1038/d41586-026-03227-4)
- **A different, third sense of "monoculture":** Traberg, Roozenbeek & van der Linden (2026), "AI is turning research into a scientific monoculture", *Communications Psychology* [title only; per search results, it concerns topical convergence on studying AI]. — [doi:10.1038/s44271-026-00428-5](https://doi.org/10.1038/s44271-026-00428-5)

**P5 — the optimistic vision depends on open, efficient tools. Verdict: largely anticipated as advocacy; modestly new as the conditional link.**
- Spirling (2023), *Nature* 616:413, World View: "Why open-source generative AI models are an ethical way forward for science" [title]. — [doi:10.1038/d41586-023-01295-4](https://doi.org/10.1038/d41586-023-01295-4)
- Palmer, Smith & Spirling (2023/2024), *Nature Computational Science* 4:2–3: "Using proprietary language models in academic research requires explicit justification" [title]. — [doi:10.1038/s43588-023-00585-1](https://doi.org/10.1038/s43588-023-00585-1)
- Widder, Whittaker & West (2024), *Nature* 635:827–833: "Why 'open' AI systems are actually closed, and why this matters" [title]. A caveat to any open-model optimism. — [doi:10.1038/s41586-024-08141-1](https://doi.org/10.1038/s41586-024-08141-1)
- Brzostowicki (2026): researchers run local models (Qwen, Nemotron via Ollama) for privacy, reproducibility and cost. One built a university-network system "so that papers, reports and study data protected under the European Union's General Data Protection Regulation could be searched without leaving the university's network". — [doi:10.1038/d41586-026-03227-4](https://doi.org/10.1038/d41586-026-03227-4)
- Stanford HAI (2026), "Open-Weight Models Aren't Enough. We Need Truly Open Source AI Models for Science and Society" [title; author per search summary, not verified]. — [Stanford HAI](https://hai.stanford.edu/news/open-weight-models-arent-enough-we-need-truly-open-source-ai-models-for-science-and-society)
- **A partial counterpoint.** Chesterman & Loy argue universities should not compete "at the technological frontier" but focus on judgement roles. — [arXiv:2601.05574](https://arxiv.org/abs/2601.05574)

### Inferences
- **P2 is the essay's biggest exposure.** Brief §4b calls "scientists use AI to speed up what they already know how to do, not to explore" the author's "own interpretation". A *Nature* Comment published two weeks ago states it almost verbatim and attributes it to incentives. The essay can still contribute by:
  1. naming the competing explanation (data affordance). Huang et al. blend it with the incentive story: they recommend data infrastructure *and* criticise incentives. Hao et al.'s own analysis favours affordance;
  2. proposing the discriminating test.
- **P1 is defensible if narrowed.** The novelty is to make legitimacy *irrelevant* to the failure mechanism and to treat the loss of mastery time as the loss of a gatekeeping signal. Writing effort and reviewer time as scarce resources are already named (*BISE*; Hansen; Fourie).
- **P3 is the essay's cleanest novel synthesis**, provided it cites Fourie (rationing versus pricing) and the fee and quota models. The economics literature argues for *pricing* or redesign instead of rationing. That gives the essay a ready counter-proposal, and its critique of decrees is then not purely negative.
- **P4 and P5 need citations, not novelty claims.** The two-driver decomposition can be presented as an analytic distinction that clarifies an existing debate.

### Gaps
- I read Huang et al. only to about two-thirds and did not see their third recommendation. Xizhe Zhang's World View was read to the standfirst only.
- **NIH cap commentary.** I found none that frames the cap as rationing. Science's news story "Fearful of AI-generated grant proposals, NIH limits scientists to six applications per year" appeared in search results but was not read.
- **Conference caps.** I did not verify specific conference quota policies myself; the *Nature* news item and Shah (2026) assert they exist.
- **P2's empirical premise.** The tests in research note 3 rely on outcome definitions that Burtch-style results (syntax ≠ ideas) caution against.

---

## Q5. What does the essay add? Overlap matrix, contribution paragraph, and passages in the brief that must change

### Takeaway
The essay's honest contribution is not the premise, which is shared with Manabu, Hansen, Gartenberg et al., Blekhman, the *Nature* editorial and others. It has four parts:
1. **Legitimacy-independence**, organised around three scarcities, including mastery time.
2. **A discriminating test** for the already-stated "acceleration, not exploration" claim.
3. **Reading the 2025–2026 caps as rationing by decree**, extending Fourie.
4. **Separating internal and external drivers of narrowing.**

The paper's own documented production is a fifth, supporting element. It has precedents (Fourie; Manabu; Cotton), so it should be pitched as better documentation, not as a first.

### Cited Findings
- Closest overall: Manabu 2026 — [doi](https://doi.org/10.1007/s42438-026-00666-0); Hansen 2026 — [doi](https://doi.org/10.1186/s41073-026-00193-3); Gartenberg et al. 2026 — [doi](https://doi.org/10.1287/orsc.2026.ed.v37.n3); Blekhman 2026 — [doi](https://doi.org/10.1371/journal.pbio.3004075)
- Closest on P2: Huang et al. 2026 — [doi](https://doi.org/10.1038/d41586-026-02961-z)
- Closest on P3: Fourie 2026 — [arXiv](https://arxiv.org/abs/2607.13844)
- Closest on P1: *BISE* editorial 2026 — [doi](https://doi.org/10.1007/s12599-026-01013-0)

### Inferences
- A submission to *PSE* must engage Manabu directly; one to *RIPR* must engage Hansen; one to *PLOS Biology* must engage Blekhman. A *Nature* or *Science* piece must engage Huang et al. and the 25 Mar 2026 editorial.
- Blekhman's piece and the arXiv-cap news both appeared on 15 Oct 2026, so the field is moving weekly. Re-run this search right before submission.

### Gaps
- Matrix cells for Manabu rest on the abstract and reference list, not the body text.
- Matrix cells for items marked [abstract], [standfirst] or [title] may understate overlap.

### Overlap matrix

Key: ● point made; ◐ partly made or adjacent; ○ not addressed (as far as read); ? cannot judge from what was read. Columns:
- **Core** — "cheap outputs speed up a pre-existing failure";
- **P1** — legitimate use breaks it;
- **P2** — acceleration, not exploration (the claim);
- **P2-test** — a test separating incentives from data affordance;
- **P3** — rationing restores scarcity;
- **P4** — two drivers;
- **P5** — open, efficient tools;
- **Read** — read status. "note 2" = `research_notes/AI disruption of academia literature/2_ai_impact_on_academia.md`; "note 3" = `3_testing_acceleration_hypothesis.md` in this folder.

| Prior work | Core | P1 | P2 | P2-test | P3 | P4 | P5 | Read |
|---|---|---|---|---|---|---|---|---|
| Manabu 2026 (*PSE*) | ● | ? | ? | ○ | ○ (none in refs) | ◐ (cites Big Tech critiques) | ○ | abstract + refs |
| Hansen 2026 (*RIPR*) | ● | ◐ | ○ | ○ | ○ (opposite: abolish scarcity) | ○ | ○ | full |
| Gartenberg et al. 2026 (*Org Sci*) | ● | ◐ | ◐ ("more vs better") | ○ | ? | ○ | ○ | abstract |
| *Nature* Editorial, Mar 2026 | ● | ◐ (effort–value link) | ◐ (data-rich skew) | ○ | ○ | ○ | ○ | partial |
| Blekhman 2026 (*PLOS Biol*) | ● | ◐ (effort proxy; "no research") | ○ | ○ | ◐ (fallback to prestige) | ◐ ("AI companies … selling tokens") | ○ | full |
| Huang et al. 2026 (*Nature* Comment) | ◐ | ○ | ● | ○ (blends both mechanisms) | ○ | ◐ (internal only) | ○ | partial |
| X. Zhang 2026 (*Nature* World View) | ○ | ○ | ◐ | ○ | ○ | ○ | ○ | standfirst |
| Kapoor & Narayanan 2025 | ● | ○ | ● | ○ | ○ | ○ | ○ | full |
| Messeri & Crockett 2024 (*Nature*) | ○ | ○ | ● ("produce more, understand less") | ○ | ○ | ○ | ○ | abstract |
| Hao et al. 2026 + Storey 2026 (*Nature*) | ○ | ○ | ● (empirical) | ◐ (drivers analysis favours data) | ○ | ○ | ○ | abstract; note 3 |
| Carrigan 2023 (LSE) | ● | ◐ (efficiency use) | ○ | ○ | ○ | ○ | ○ | full |
| Kingsley 2023 (LSE) | ● | ○ | ○ | ○ | ○ | ○ | ○ | full |
| Dey 2026 (SN Communities) | ◐ | ○ | ○ | ○ | ○ | ○ | ○ | full |
| Arndt & Zhang 2026 (*CJAS*) | ● | ? | ○ | ○ | ? | ○ | ○ | abstract |
| Lang, Moffett & Vasudevan 2025 | ● | ○ | ◐ ("flattening") | ○ | ○ | ○ | ○ | full (skim) |
| Parrilla 2023 (*Nature*) | ◐ | ◐ (grants) | ○ | ○ | ○ | ○ | ○ | standfirst |
| *BISE* editorial 2026 | ● | ● (Stage 1 erodes the signal) | ○ | ○ | ◐ (fees) | ○ | ○ | full (skim) |
| Kusumegi et al. 2025 (*Science*) | ○ | ◐ (evidence) | ○ | ○ | ○ | ○ | ○ | note 2 |
| Galdin & Silbert 2025; Cowgill et al. 2026 | ○ | ◐ (non-academic analogue) | ○ | ○ | ○ | ○ | ○ | abstract |
| Adeyeye 2026 (SSRN) | ● | ◐ (framed as "no genuine effort") | ○ | ○ | ○ | ○ | ○ | abstract |
| Hakobyan 2026 (arXiv) | ◐ | ◐ | ○ | ○ | ◐ (loosen, not ration) | ○ | ○ | abstract |
| Fourie 2026 (arXiv) | ◐ | ◐ | ○ | ○ | ◐ (rationing, journal level) | ○ | ○ | full (skim) |
| Lopez-Lira & Seyfi 2026; Atasu 2026 | ◐ | ○ | ○ | ○ | ◐ (pricing) | ○ | ○ | abstract |
| Shah 2026; Singh Chawla 2026 | ○ | ○ | ○ | ○ | ◐ (quota design; cap critics) | ○ | ○ | abstract; partial |
| Castellacci et al. 2026 (arXiv) | ◐ | ○ | ◐ | ○ | ○ | ○ | ○ | abstract |
| Chesterman & Loy 2026; Manning 2026 | ○ | ○ | ○ | ○ | ○ | ◐ (external driver) | ◐ / ○ | abstract |
| Lindebaum et al. 2025 | ○ | ○ | ○ | ○ | ○ | ◐ | ○ | abstract |
| Spirling 2023; Palmer et al. 2024; Brzostowicki 2026 | ○ | ○ | ○ | ○ | ○ | ◐ (Brzostowicki: chat data) | ● / ◐ | title; partial |

The essay's position for comparison: Core ● (shared premise), P1 ●, P2 ●, P2-test ●, P3 ●, P4 ●, P5 ●. On novelty after this review: P2-test and the P3 synthesis are new; P1 and P4 are new only in emphasis or decomposition; Core, the P2 claim and P5 are already made.

### Draft contribution paragraph (about 150 words)

> Several recent papers argue that generative AI strains academic evaluation by making its outputs cheap (Manabu 2026; Hansen 2026; Gartenberg et al. 2026; Blekhman 2026); others argue that it speeds up established lines of work rather than opening new ones (Huang et al. 2026). I build on this work in four ways. First, I locate the failure in legitimate use: signals of merit rest on three scarcities, the effort of writing, reviewers' time and the time needed to master a literature, and honest use erodes all three. Second, I turn "acceleration, not exploration" into a testable claim, with a triple-difference design that separates metric incentives from the pull of data-rich problems. Third, extending Fourie (2026), I read NIH's application cap, arXiv's monthly limit and conference quotas as rationing that restores scarcity by decree. Fourth, I separate the internal driver of narrowing (incentives) from an external one (corporate control of tools and chat data). This essay is itself a documented case of such use.

(About 160 words. It claims no "first" and names the closest precedent for each contribution. If space allows, add "cf. Kusumegi et al. 2025; Hanneke et al. 2026" after the first contribution.)

### Passages in the brief that must change

1. **Thesis → "What this means", first bullet:** "AI makes the things the system counts (papers, reviews, grant applications) almost free to produce. It therefore speeds up a failure that was already under way."
   - **Status:** already made, by Carrigan 2023, Kingsley 2023, Lang et al. 2025, Manabu 2026, Hansen 2026, Gartenberg et al. 2026, the *Nature* Editorial of Mar 2026, Arndt & Zhang 2026 and Blekhman 2026.
   - **Change:** present it as the shared starting premise, with these citations, not as the paper's contribution.
2. **Thesis → second bullet:** "The failure does not depend on misuse. Even good, legitimate use of AI breaks the system, because the system's signals of merit and its gatekeeping rely on scarcity…"
   - **Status:** partly made.
     - *BISE* 2026 says "Stage 1" prompting "undermines writing quality as a screening signal" and names three limited resources (editorial attention, reviewer time, audience attention).
     - Hansen speaks of the "scarcity of interpretive attention".
     - Also Kusumegi 2025, Parrilla 2023, Galdin & Silbert 2025, Cowgill et al. 2026 and Fourie 2026.
   - **Change:** keep the claim, but cite these sources. Claim novelty only for (a) making legitimacy explicitly irrelevant to the mechanism and (b) the "time to master a literature" scarcity as a gatekeeping signal.
3. **"The paper as its own example":** "The paper is made with AI and says so openly, as part of the argument rather than as a confession."
   - **Status:** precedents exist: Osmanovic Thunström 2022; Cotton et al. 2023; Porsdam Mann et al. 2023; Agents4Science 2025. Fourie 2026 uses nearly the same division of labour (Claude Code and Codex for drafting, literature search, adversarial review). Manabu 2026 was drafted with Perplexity.
   - **Change:** acknowledge these. Pitch the novelty as an auditable process record (git history, time and cost, the conflict of interest) offered as evidence.
4. **"A record of the time and cost … This could be the paper's most telling data point."**
   - **Status:** cost-per-paper figures already circulate. The AI Scientist was reported at about US$15 per paper (`research_notes/AI disruption of academia literature/2_ai_impact_on_academia.md`, citing arXiv:2408.06292), and Blekhman writes "A plausible paper can now be produced in a day".
   - **Change:** frame the figure as the first such record for a human-led, legitimate-use essay only if no counterexample turns up. I found none, but the search was not exhaustive.
5. **Structure §2, "writing no longer signals merit (Kusumegi et al. 2025, Science)".**
   - **Status:** no longer a single-source point.
   - **Change:** add Galdin & Silbert 2025, Cowgill et al. 2026, the *BISE* editorial 2026 and the *Nature* Editorial 2026, and note Hakobyan's model of the review side.
6. **§4 title and §4b:** "The author's hypothesis: 'scientists use AI to speed up what they already know how to do, not to explore.' … The author acknowledges this is their own interpretation", and "Mechanism: the incentives from section 1 steer AI towards producing more of the same."
   - **Status:** already made, almost verbatim, by Huang et al. 2026 (*Nature* Comment, 29 Sep 2026). Also by Xizhe Zhang 2026 (*Nature* World View), Kapoor & Narayanan 2025, Messeri & Crockett 2024 and Gartenberg et al. 2026.
   - **Change:** reword along the lines of "a hypothesis several commentators now advance (cite), which no one has tested". Move the "how it could be tested" box from an aside to the contribution itself. State that Huang et al. blend the incentive and data-cost mechanisms, which the triple difference separates.
7. **§4c:** "Reform is voluntary (DORA, CoARA), designed before AI, and limited to disclosure rules."
   - **Status:** outdated as a description of the 2025–2026 landscape.
     - Binding caps now exist: NIH's six applications; arXiv's two per month from 1 Oct 2026; SocArXiv's one per week; conference quotas.
     - Fee, AI-triage and redesign proposals exist: Lopez-Lira & Seyfi; Atasu; *BISE*; Hansen; Bhargava et al.; Xuegong Zhang 2026; Payan et al.; Cwik.
   - **Change:** rewrite §4c around P3, citing Fourie's "rationed, not priced". Contrast rationing with pricing and redesign. Note Blekhman's warning that evaluation may fall back on prestige proxies and undo DORA.
8. **§5:** "Distinguish the internal driver of narrowing … from the external driver (section 5: corporate control of the tools)."
   - **Status:** each driver has been described separately (Huang et al.; Chesterman & Loy 2026; Manning 2026; Lindebaum et al. 2025).
   - **Change:** cite these, and present the decomposition, together with chat data as a channel (Brzostowicki 2026), as the analytic contribution.
9. **§5:** "Open alternatives … are the bridge back to section 3."
   - **Status:** anticipated by Spirling 2023, Palmer, Smith & Spirling 2024 and Brzostowicki 2026. Widder et al. 2024 is a caveat.
   - **Change:** cite these, and claim only the conditional link between openness and the exploration vision.
10. **§3 theme:** "AI could help researchers stay knowledgeable across fields."
    - **Status:** Huang et al. 2026 make the same point ("AI tools reduce the informational cost of pivoting") and note that institutions penalise pivots. Xizhe Zhang 2026 says tasks that once needed "large, interdisciplinary teams" can be done by smaller groups.
    - **Change:** cite both. This also links §3 to §4, since the barrier is institutional.
11. **Venue notes** (`paper/journals.md` and the "Target venue" discussion).
    - **Change:** add Blekhman 2026 (*PLOS Biology*, 15 Oct 2026) and Huang et al. 2026 (*Nature*) to the list of must-cite, must-differentiate works alongside Manabu and Hansen. A *PLOS Biology* or *Nature* submission will be read against them.
