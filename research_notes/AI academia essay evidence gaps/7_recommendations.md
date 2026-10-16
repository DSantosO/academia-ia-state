# Recommendations for research evaluation and governance when scholarly output is nearly free

**Verification (16 Oct 2026).**
- **DOIs.** Every DOI below was resolved against the Crossref API (title, venue, date, authors) on 16 Oct 2026.
- **Abstracts.** Abstracts were read through OpenAlex. Where OpenAlex had none, I used Semantic Scholar or a RePEc page.
- **arXiv items.** Checked against their arXiv abstract pages.
- **Web pages and PDFs.** Fetched and read directly. This includes DORA's declaration, CoARA's Agreement (the Science Europe-hosted PDF, because coara.eu reset the connection), the EC's 2026 news item, the DFG FAQ, the ERC Scientific Council's 2024 evaluation document, the CNEAI criteria for 2020 and 2024, the REF 2029 guidance, the EU AI Factories page, the VolkswagenStiftung news item, and the RUG-hosted summary of the Dutch Culture Barometer 2026.
- **Blocked sources.**
  - Springer's site blocks automated access, so I read the *BISE* editorial from its open repository copy at KIT.
  - INFORMS (Gartenberg et al.) and science.org returned bot challenges or HTTP 403.

**Read status of each item:**
- **[full]** full text read or skimmed;
- **[partial]** part of the text read;
- **[abstract]** abstract only;
- **[primary doc]** official policy or guidance text read;
- **[title]** metadata only;
- **[search summary]** known only from a search-engine summary;
- **(note N / audit)** reused from an earlier note in this folder, or from `paper/reviews/citation_audit.md`, with the verification status recorded there.

**Legend used in the tables.**
- **Driver.**
  - **I**: internal (academic incentives);
  - **E**: external (concentration of AI tools and of chat data in a few firms);
  - **A**: affordance, the rival explanation in Box 2 that AI goes where data are.
- **Type.**
  - **Rationing (submission)**: limits what a person may submit;
  - **Rationing (price)**: makes submission costly;
  - **Evaluation-side limit**: limits what *counts*, not what may be communicated;
  - **Reform**: changes what or how evaluation counts in other ways;
  - **Capacity**: buys or automates evaluator time;
  - **Infrastructure**.

---

## Q1. What exactly have the closest pieces proposed?

### Takeaway
The closest pieces agree on the diagnosis but propose different remedies.
- **Concrete remedies:**
  - **Huang et al.** give three, all about exploration: data infrastructure, an end to penalties on pivots, and distance-based indicators.
  - **Hansen** redesigns publishing: tiered publishing, tiered review, paid reviewers, AI screening.
  - **The *BISE* editors** give the most operational journal list: fees with waivers or refundable deposits, portable reviews, bounded AI, strict desk rejection, and verification outputs as "first-class contributions".
- **Diagnosis only:**
  - **Blekhman** asks for evaluation "aligned with [the field's] goals" but names no instrument.
  - **Fourie** diagnoses that review is "rationed, not priced" and models what follows; I found no sentence in which he prescribes pricing.
- **Calls only:**
  - **The *Nature* Editorial** issues a call, plus encouragement to deposit prompt transcripts.
  - **Gartenberg et al.**, from their abstract, say only that institutions "adapt".
- **None of them proposes capping what *counts* as a substitute for AI-era caps on what may be *submitted*.**
- Two further close pieces turned up in this search and must be cited:
  - **Hosseini et al. 2026** (*Research Evaluation*), on "distinctly human contributions";
  - **Lovén 2026 and Ma 2026**, on verification as the new scarcity.

### Cited Findings

**Huang, Hu, Zhang & Lin (2026), "AI can widen science — but only if institutions stop rewarding the already measurable", *Nature* 658:32–33, Comment, 29 Sep 2026.** [Read: online text through recommendation 2 (cached HTML); recommendations 2–3 as quoted from the print PDF in the audit, R38.]
- **Standfirst:** "Funders, journals and universities must reward the creation of new scientific terrain, not just the efficient mining of old ground." — [doi:10.1038/d41586-026-02961-z](https://doi.org/10.1038/d41586-026-02961-z)
- **Evidence base:** "AI-assisted research spans 4.6% less topical ground than does non-AI work, with this pattern being present in more than 70% of the subfields studied". The authors then write: "To address these concerns, we put forward three recommendations." — [doi](https://doi.org/10.1038/d41586-026-02961-z)
- **(1) "Make new terrain measurable".**
  - "Current funding systems overwhelmingly reward the downstream exploitation of existing data rather than the upstream creation of new data sets and measurement capabilities."
  - "the costs of making predictions with AI models have fallen roughly 100-fold in the past two years, whereas building new observational infrastructure still carries high long-term operational costs".
  - "We call on funders to deliberately subsidize the data infrastructure, especially in neglected domains such as diseases that have been excluded from major cohort studies."
  - — [doi](https://doi.org/10.1038/d41586-026-02961-z)
- **(2) "Stop punishing pivots".**
  - "Universities and funding agencies must stop penalizing researchers who use AI to enter new fields."
  - "Hiring committees assess candidates on a continuous publication record in a single domain and funding agencies often treat preliminary data from the applicant's previous work as a prerequisite for support."
  - Print PDF: "funders must create exploratory grants that have extended evaluation horizons", fellowships for field-crossing work, and panels that judge the proposed pivot.
  - — [doi](https://doi.org/10.1038/d41586-026-02961-z); print-PDF wording per `paper/reviews/citation_audit.md` R38 (audit)
- **(3) "Reward innovation, not just output".** Indicators of "the conceptual distance between a researcher's current and previous work and measures of lasting intellectual disruption, rather than short-term citation accumulation". — [doi](https://doi.org/10.1038/d41586-026-02961-z) (print PDF, audit R38)

**Blekhman (2026), "What is biology research for?", *PLOS Biology* 24:e3004075, Perspective, 15 Oct 2026.** [full; PDF in `paper/sources/`]
- "Therefore, we have to be deliberate about establishing a new way to evaluate biology research. The response cannot be that we stop evaluating ourselves." — [doi:10.1371/journal.pbio.3004075](https://doi.org/10.1371/journal.pbio.3004075)
- "Instead, we could use this surge to acknowledge that paper counts are meaningless, and, as a field, abandon the current incentive system and return our focus to the substance of research." — [doi](https://doi.org/10.1371/journal.pbio.3004075)
- "The biology research community needs to define new ways to evaluate science that are aligned with its goals. This is work for the entire field: journals, funders, universities, and institutions." — [doi](https://doi.org/10.1371/journal.pbio.3004075)
- He warns that evaluation "will fall back on older, cruder proxies, such as journal prestige and impact factor". He lists five goals of biology research (see `paper/sources/Blekhman_2026_summary.md`). — [doi](https://doi.org/10.1371/journal.pbio.3004075)

**Hansen (2026), "Symbolic scarcity and epistemic waste", *Research Integrity and Peer Review* 11:7.** [full, note 6]
- **Tiered publishing.** An integrity-filtered inclusion layer, plus "Prestige curation without scarcity". Metrics would be computed on the curated layer only.
- **Tiered review by "epistemic risk".** Soundness review by "trained graduate students, early-career researchers, staff reviewers"; full expert review for high-risk claims.
- **Reviewer pay and recognition.** "Micro-payments, fellowships, or review-based stipends", and a "reviewer recognition ledger".
- **AI screening at inclusion.** It "uses computational capacity to manage computationally generated volume".
- — [doi:10.1186/s41073-026-00193-3](https://doi.org/10.1186/s41073-026-00193-3)

**Fourie (2026a), arXiv:2607.13844 v3 (31 Aug 2026), "The Value of Peer Review and the Reward to Reputation".** [full, skimmed; conclusion read in full here]
- "Among the 600 highest-ranked economics journals, only 118 charge a submission fee at all, and the median charge among those is 125 dollars." The fee that would clear the queue, "along with the referee pay it would fund, sits well above anything charged today (Fourie and Macdonald, 2026). Review is therefore rationed, not priced." — [arXiv:2607.13844](https://arxiv.org/abs/2607.13844)
- **Conclusion.**
  - "A journal that keeps its stamp scarce by rejecting what it cannot read is not thereby protecting the stamp's value".
  - "a journal that adopts a well-tested screen has not bought a tool with fixed error rates; it has entered an equilibrium in which its own authors' choices set those rates, and in which, whenever some authors game the screen and others do not, its verdict is worth exactly what getting past it costs".
  - "Expert judgment is the resource the journal cannot scale, and it is also the one form of evaluation an author cannot pass in advance".
  - The argument extends to "Grant panels, hiring committees, accreditation bodies and rating agencies".
  - — [arXiv](https://arxiv.org/abs/2607.13844)

**Fourie (2026b), "The Price of Submission", arXiv:2608.14760 (14 Aug 2026).** [abstract]
- "Economics journals ration access to peer review with time and money."
- A July 2026 census of 500 RePEc-ranked journals finds that "113 (22.6 per cent) charge a fee, with incidence falling from 68 per cent in the top 50 to 2 per cent in the bottom 50".
- "a fee reduces system-wide referee demand only when authors stop, shorten their submission chains or switch to journals requiring fewer reports."
- arXiv lists Fourie as sole author, while Fourie 2026a cites this title as "Fourie and Macdonald (2026)".
- — [arXiv:2608.14760](https://arxiv.org/abs/2608.14760)

**Nature Editorial (2026), "AI scientists are changing research — institutions, funders and publishers must respond", *Nature* 651:853–854, 25 Mar 2026.** [full text read here]
- "Universities, funders, publishers and researchers must plan how they will adapt." — [doi:10.1038/d41586-026-00934-w](https://doi.org/10.1038/d41586-026-00934-w)
- "No one has worked out how to account for AI-inflated outputs in hiring and promotion decisions, nor what will happen to early-career researchers if tasks that are crucial to their training as scientists are done by a machine." — [doi](https://doi.org/10.1038/d41586-026-00934-w)
- "Nature already requires transparency in how LLMs are used in submitted articles, and will not accept such models as authors". "For the sake of reproducibility, when a model contributes to the creative part of a study, Nature encourages researchers to submit transcripts of prompts and model responses alongside the final outputs, as one would with data sets." — [doi](https://doi.org/10.1038/d41586-026-00934-w)
- "It is up to the research community to put guard rails in place to ensure that happens." — [doi](https://doi.org/10.1038/d41586-026-00934-w)

**Gartenberg, Hasan, Murray & Pierce (2026), *Organization Science* 37(3):795–812.** [abstract; INFORMS blocked the full text]
- "we cannot make a normative assessment about appropriate or ideal levels of AI usage."
- "Reaching an equilibrium in which AI serves as a critical engine of innovation will require that our institutions and the incentive structures they create adapt."
- — [doi:10.1287/orsc.2026.ed.v37.n3](https://doi.org/10.1287/orsc.2026.ed.v37.n3)

**Hanneke, Hering, Pfeiffer, Reijers & Hinz (2026), "Academic Publishing in the Age of Generative AI", *BISE* 68(4):729–737.** [full; KIT repository copy]
- **Diagnosis.**
  - "From a journal's perspective, Stage 1 GenAI usage undermines writing quality as a screening signal."
  - "Detection tools offer little relief because they cannot reliably distinguish AI-assisted from manual work, and disclosure requirements remain fragile when authors have incentives to underreport."
  - — [doi:10.1007/s12599-026-01013-0](https://doi.org/10.1007/s12599-026-01013-0); [KIT copy](https://publikationen.bibliothek.kit.edu/1000195177)
- **Fees.** "Journals could introduce submission fees (which is commonly done in the Finance discipline) as refundable deposits or in tiered structures with waivers, reviewer payments, or editorial support. These actions would avoid pricing without waivers, which disadvantages early-career and financially constrained researchers." — [KIT copy](https://publikationen.bibliothek.kit.edu/1000195177)
- **Portable reviews.** "transferring manuscripts with reviews reduces repeated referee labor and accelerates decisions. This approach raises effective capacity without requiring more volunteer labor." — [KIT copy](https://publikationen.bibliothek.kit.edu/1000195177)
- **Bounded AI.** "We could deploy AI for checklisting, summarization, and procedural checks in an advisory role, following NeurIPS' checklist-assistant model." — [KIT copy](https://publikationen.bibliothek.kit.edu/1000195177)
- **Strict desk rejection.** "Journals should clarify disclosure expectations and enforce accountability through strict desk-reject policies for violations such as hallucinated sources". — [KIT copy](https://publikationen.bibliothek.kit.edu/1000195177)
- **Verification outputs.**
  - The editors list "well-designed null findings and boundary conditions, evidence packages (data, code, documentation), robustness contributions (sensitivity analyses, alternative specifications), and reusable research infrastructure". (The first item of the list was cut off in my extract.)
  - "When journals treat them as first-class contributions, agentic pipelines become part of the solution instead of a source of congestion."
  - They call a separate track for AI-generated submissions "as of now premature".
  - — [KIT copy](https://publikationen.bibliothek.kit.edu/1000195177)

**Lopez-Lira & Seyfi (2026), SSRN.** [abstract, note 6 and audit R44]
- "Without policy adjustment, submissions flood the system and acceptance rates collapse."
- "Only 3% of the optimal fee internalizes direct review costs; the remaining 97% reflects congestion screening and prestige stabilization".
- — [doi:10.2139/ssrn.6337880](https://doi.org/10.2139/ssrn.6337880)

**Atasu (2026), SSRN.** [abstract, note 6] Proposes "submission and AI-use contingent fees, and reviewer compensation", or a two-track mechanism. — [doi:10.2139/ssrn.6393158](https://doi.org/10.2139/ssrn.6393158)

**Newly found close work (not in note 6)**
- **Hosseini, Earp, Porsdam Mann & Holmes (2026), "Generative AI can and should accelerate research evaluation reform to better recognize 'distinctly human contributions'", *Research Evaluation* 35.** [abstract]
  - Metrics "are becoming even less reliable as GenAI accelerates text-based and computational work while leaving other forms of research labor (e.g. community engagement, in-person mentorship and team development) largely unaffected."
  - "We suggest practical mechanisms for supporting evaluation reform including modified CRediT (Contributor Role Taxonomy) statements, recognition of a broader array of outputs, and strengthened narrative CVs and third-person testimonies. However, we acknowledge that these suggestions, particularly those relying on narrative self-presentation, are themselves vulnerable to GenAI manipulation".
  - "evaluation cannot be reduced to instruments designed to minimize human evaluative effort. GenAI, therefore, does not require entirely new systems of evaluation. Rather, it increases the cost of avoiding what good and ethically sound performance evaluation has always required."
  - — [doi:10.1093/reseval/rvag020](https://doi.org/10.1093/reseval/rvag020)
- **Lovén (2026a), "AI-Augmented Science and the New Institutional Scarcities", arXiv:2605.02566.** [abstract]
  - "Four things become scarce instead: verified signal, legitimacy, authentic provenance, and integration capacity."
  - "The way forward for AI-augmented science is not acceleration but the redesign of its certifying infrastructure around these new scarcities."
  - Its companion, Lovén 2026b (arXiv:2604.22966), closes with an agenda to "build provenance and verification as commons".
  - — [arXiv:2605.02566](https://arxiv.org/abs/2605.02566); [arXiv:2604.22966](https://arxiv.org/abs/2604.22966)
- **Ma (2026), "Toward an Engineering of Science: Rebalancing Generation and Verification in the Age of AI", arXiv:2605.10425.** [abstract] "generation cost itself served as a rough filter; AI weakens that filter without comparably lowering verification cost". Proposes "blueprints", structured research artifacts. — [arXiv:2605.10425](https://arxiv.org/abs/2605.10425)
- **Mo et al. (2026), ICML 2026 Position track, arXiv:2607.26064.** [abstract] "We propose criteria for an adapted verification infrastructure that emphasizes observable-by-default workflows, scalable verification, and clear attribution." — [arXiv:2607.26064](https://arxiv.org/abs/2607.26064)

### Inferences
- **The remedies divide by the scarcity they target.**
  - Huang et al. target exploration.
  - Hansen, *BISE*, Lopez-Lira & Seyfi and Atasu target reviewer capacity, by pricing or redesign.
  - Hosseini et al., Lovén, Ma and Mo et al. target what evaluators can trust: human contributions, provenance, verification.
  - None targets the *number of things counted* per person, which is the lever that removes the incentive to produce more.
- **Fourie should be cited as diagnosis, not prescription.** The brief's gloss "price review rather than ration it" is a fair reading of the implication. In what I read, though, Fourie models the consequences of rationing and of rule-based screens; he does not recommend fees. His point that rule-based screens are gamed until "its verdict is worth exactly what getting past it costs" is a strong argument against relying on AI triage.
- **Hosseini et al. 2026 is the closest prior work on "invisible effort".** Its last sentence, that GenAI "increases the cost of avoiding what good … evaluation has always required", is close to the essay's view that reading is the resource reform depends on. It should join the must-cite list next to Blekhman.
- **Corrections for the draft:**
  - The *BISE* "screening signal" quotation is now confirmed in full text, as is the fee wording "refundable deposits or in tiered structures with waivers". `citation_audit.md` §4.3 had flagged both as not found, so ¶4c.3 can restore "refundable deposits".

### Gaps
- Gartenberg et al.'s body text (INFORMS bot wall) may contain concrete proposals I could not read.
- Huang et al.'s third recommendation rests on the audit's reading of the print PDF. I did not re-read it here.
- "Fourie and Macdonald (2026)" and arXiv's single-author listing of "The Price of Submission" disagree. I did not resolve which is correct.

---

## Q2. Which established reforms apply, and with what evidence of effect?

### Takeaway
- **Evidence is good** for:
  - Registered Reports (less positive-result bias, higher rated rigour);
  - paid review (faster, more completed reviews, no measured loss of quality);
  - long-horizon funding (HHMI investigators explore more and publish more high-impact work);
  - the claim that researchers respond quickly to whatever is counted (UK research assessment).
- **Evidence is thin or absent** for:
  - narrative CVs (28 opinion pieces and 7 experiments);
  - the long-run outcomes of funding lotteries (acceptability and a funder's own report only);
  - the downstream effect of data editors;
  - reviewer-credit ledgers;
  - AI-use disclosure taxonomies;
  - eLife's model;
  - public AI infrastructure.
- **Submission fees** reduce submissions modestly (elasticity about −0.11 per $100), raise equity concerns, and cut total review demand only under conditions.

### Cited Findings

**Responsible-metrics frameworks (DORA, Leiden, Hong Kong, CoARA).** See Q5 for implementation evidence.
- DORA [primary doc] — [sfdora.org/read](https://sfdora.org/read/)
- Leiden Manifesto — [doi:10.1038/520429a](https://doi.org/10.1038/520429a)
- Hong Kong Principles, which reward "peer review and mentoring" among five principles (governance note) — [doi:10.1371/journal.pbio.3000737](https://doi.org/10.1371/journal.pbio.3000737)
- CoARA Agreement (20 Jul 2022) [primary doc] — [Science Europe PDF](https://www.scienceeurope.org/media/y41ks1wh/20220720-rra-agreement.pdf)

**Narrative CVs.**
- A review found 28 opinion pieces and 7 experiments, and concluded that promoters rarely examine how the narrative format itself produces benefits (governance note). — [doi:10.1093/reseval/rvad013](https://doi.org/10.1093/reseval/rvad013)
- Narrative self-presentation is "vulnerable to GenAI manipulation". — [Hosseini et al. 2026](https://doi.org/10.1093/reseval/rvag020)

**Funding lotteries (partial randomisation).**
- **Volkswagen Foundation, "Experiment!".**
  - 2013–2021: 183 projects funded from more than 5,000 applicants, with grants up to €120,000; partial randomisation from 2017.
  - The funder's summary of the evaluators' concluding report: it "evidences some significant positive effects … It can increase diversity among the grantees and reduce the risk of possible bias as present in conventional review procedures."
  - Germany's Wissenschaftsrat (2017), as reported on the same page, advocated "testing innovative selection procedures and systematically evaluating their introduction".
  - This is the funder's own framing (news item, 30 May 2024).
  - — [VolkswagenStiftung](https://www.volkswagenstiftung.de/en/news/news/everyone-equal-lottery-drum)
- **Health Research Council of New Zealand (Explorer Grants).**
  - Survey response rate 39% (126/325). 63% favoured a lottery for Explorer Grants and 25% opposed; for other grant types, 40% favoured and 37% opposed.
  - "Most applicants reported that the lottery did not change the time they spent preparing their application."
  - — [Liu et al. 2020, doi:10.1186/s41073-019-0089-z](https://doi.org/10.1186/s41073-019-0089-z)
- **SNSF.** A lottery among "good but not excellent" proposals near the funding line, chosen with Bayesian expected ranks. — [Heyard et al. 2022, doi:10.1080/2330443X.2022.2086190](https://doi.org/10.1080/2330443X.2022.2086190)
- **Design matters.** Simulations show that how fair a lottery is depends on its type; lotteries that let some proposals bypass the draw vary markedly. — [Feliciani et al. 2024, doi:10.1093/reseval/rvae025](https://doi.org/10.1093/reseval/rvae025)
- **Original proposals and policy analysis.** — [Fang & Casadevall 2016](https://doi.org/10.1128/mBio.00422-16); [Shaw 2024](https://doi.org/10.1093/reseval/rvae035)
- **CoARA's examples include** "Consider post peer review funding applications lottery". — [CoARA Agreement, p. 20](https://www.scienceeurope.org/media/y41ks1wh/20220720-rra-agreement.pdf)

**Limits on how many outputs are evaluated.** Details are in Q3: the UK RAE/REF, DFG, ERC, Spain's CNEAI, China's 2020 reform, and CoARA's "Consider limiting the number of outputs assessed".

**Registered Reports.**
- 96% positive results in the standard literature against 44% in Registered Reports (governance note). — [Scheel et al. 2021](https://doi.org/10.1177/25152459211007467)
- 353 reviewers compared 29 Registered Reports with 57 comparison papers. "RRs outperformed comparison papers on all 19 criteria": rigour of methodology +0.99, analysis +0.97, overall quality +0.66. The novelty (+0.13) and creativity (+0.22) intervals include zero. — [Soderberg et al. 2021, doi:10.1038/s41562-021-01142-4](https://doi.org/10.1038/s41562-021-01142-4)
- Offered by 300+ journals (governance note). — [Chambers & Tzavella 2022](https://doi.org/10.1038/s41562-021-01193-7)

**eLife's publish–review–curate model.**
- The model itself (governance note). — [Eisen et al. 2020](https://doi.org/10.7554/eLife.64910); [Eisen et al. 2022](https://doi.org/10.7554/eLife.83889)
- **Evidence:** no outcome study found. eLife lost its Journal Impact Factor and is only partially indexed in Web of Science. Secondary sources disagree on who initiated the change and when. — [HKUST Library](https://library.hkust.edu.hk/sc/elife-indexing-change/) [search summary]; [The Publication Plan](https://thepublicationplan.com/2025/11/26/over-100-institutions-back-elifes-reviewed-preprint-model/) [search summary]

**Paid peer review.**
- **Critical Care Medicine, quasi-randomised trial** (alternating 2-week blocks; $250 offer; Sep 2023–Mar 2024).
  - 715 invitations. Acceptance was 52.7% with the offer against 47.8% without.
  - Completed reports: "49.8% [206/414] vs. 42.2% [127/301]; p = 0.04".
  - About 1 day faster (11 vs 12 days); "no difference in review quality".
  - An estimated ~$150,000 a year for the journal [search summary; not in the abstract text read].
  - — [Cotton et al. 2025, doi:10.1097/CCM.0000000000006637](https://doi.org/10.1097/CCM.0000000000006637)
- **Biology Open "Fast & Fair"** (Company of Biologists; £220 per manuscript, paid "only if they completed the review on time, and the review met editorial quality expectations").
  - Time to first decision fell from a mean of 37.7 to 5.5 working days.
  - Invitation acceptance 67% vs 23%; non-response 13% vs 39%; completion 98% vs 87%.
  - Fewer low-scoring reports; final acceptance 59% vs 61%.
  - "financial sustainability remains to be tested at scale".
  - Caveats: a preprint, written by the journal's own editors.
  - — [Gorelick & Clark 2026, doi:10.64898/2026.06.02.729548](https://doi.org/10.64898/2026.06.02.729548)
- **Journal of Public Economics field experiment** (1,500 referees).
  - "cash incentives significantly improve speed"; "Cash payments do not crowd out intrinsic motivation".
  - "social incentives have smaller but significant effects … especially effective among tenured professors".
  - "all the treatments have little or no effect on rates of agreement to review, quality of reports, or review times at other journals."
  - — [Chetty, Saez & Sándor 2014, doi:10.1257/jep.28.3.169](https://doi.org/10.1257/jep.28.3.169)

**Submission fees.**
- "a $100 increase in submission fee can reduce the number of yearly submissions by up to 36 (or an elasticity of −0.11)" (core economics journals, panel data for 2008 and 2013). — [Zheng & Kaiser 2016, doi:10.1111/ecin.12277](https://doi.org/10.1111/ecin.12277)
- Fees cut system-wide referee demand only under conditions. — [Fourie 2026b](https://arxiv.org/abs/2608.14760)
- Equity: "The marginalizing effect of journal submission fees in Accounting and Finance" [title only; no abstract available]. — [Oldford, Fiset & Armenakyan 2023, doi:10.1007/s11192-023-04758-7](https://doi.org/10.1007/s11192-023-04758-7)
- *BISE* on waivers (Q1). — [KIT copy](https://publikationen.bibliothek.kit.edu/1000195177)

**Reviewer credit.**
- The only causal evidence found is the social-incentive arm of Chetty et al. — [doi:10.1257/jep.28.3.169](https://doi.org/10.1257/jep.28.3.169)
- Proposals:
  - Hansen's ledger — [doi](https://doi.org/10.1186/s41073-026-00193-3)
  - the Hong Kong Principles — [doi](https://doi.org/10.1371/journal.pbio.3000737)
  - CoARA's example "Value contributions such as peer review and editorial roles" — [CoARA Agreement](https://www.scienceeurope.org/media/y41ks1wh/20220720-rra-agreement.pdf)

**Data or code editors and reproducibility checks.**
- **AEA.** The Data Editor checks provenance, documentation and computational reproducibility of conditionally accepted papers before acceptance [search summary of AEA policy and FAQ]. The checks are run by trained undergraduates. — [AEA FAQ](https://swlb1.aeaweb.org/journals/data/faq) [search summary]; [Vilhuber et al. 2022, arXiv:2204.01540](https://arxiv.org/abs/2204.01540)
- A Data Editor paper reportedly says the AEA verified more than 1,000 articles in its first two years, and that earlier deposit-only policies "improved the availability, but not necessarily the reproducibility" [search summary; not read].
- I found no study of the downstream effect on replication success.

**Funding replication.**
- NWO's 2016 Replication Studies pilot (about €3M) funded reproduction and replication studies [secondary news; search summary]. — [Editage Insights](https://www.editage.com/insights/dutch-organization-launches-worlds-first-national-fund-for-replication-studies)
- A 2025 article, "Replication studies in the Netherlands: lessons learned and recommendations" [title only]. — [Utrecht research portal](https://research-portal.uu.nl/en/publications/replication-studies-in-the-netherlands-lessons-learned-and-recomm-2/)
- AI tools now automate parts of replication:
  - VERITAS, evaluated on 65 papers across four fields — [arXiv:2607.02931](https://arxiv.org/abs/2607.02931)
  - Kubota et al.: "replication is costly and less well rewarded than original research" — [arXiv:2602.18453](https://arxiv.org/abs/2602.18453)

**Long-horizon funding.**
- HHMI "tolerates early failure, rewards long-term success, and gives its appointees great freedom to experiment". Its investigators "produce high-impact articles at a much higher rate than a control group of similarly accomplished NIH-funded scientists", and "the program induces them to explore novel lines of inquiry". — [Azoulay, Graff Zivin & Manso 2011, doi:10.1111/j.1756-2171.2011.00140.x](https://doi.org/10.1111/j.1756-2171.2011.00140.x)

**AI-use disclosure taxonomies.**
- **GAIDeT.** Covers conceptualisation, literature review, methodology, data analysis, writing, supervision and ethical review, with a GitHub-based declaration generator. "Future work should focus on empirical validation". — [Suchikova et al. 2025, doi:10.1080/08989621.2025.2544331](https://doi.org/10.1080/08989621.2025.2544331)
- **Cwik 2026.** "disclosure alone rarely clarifies how AI-assisted work was performed, what information was entered, how outputs were evaluated, or how human responsibility was maintained". Proposes minimal and extended documentation, with OSF templates and prompt-log structures. — [doi:10.1186/s41073-026-00245-8](https://doi.org/10.1186/s41073-026-00245-8)
- **Spain's sexenios now require** declaring GenAI use "siempre que afecte al contenido original de la aportación" [primary doc]. — [CNEAI, Resolución de 9 de diciembre de 2024](https://biblioteca.umh.es/files/2024/12/ResolucionCNEAI_091224.pdf)
- **Publishers' policies are heterogeneous** (governance note). — [Ganjavi et al. 2024](https://doi.org/10.1136/bmj-2023-077192)
- **Counterpoint** (note 6). — [Earp et al. 2026, "Against mandatory prompt disclosure"](https://doi.org/10.1007/s00146-026-03326-w)

**Public or institution-run AI infrastructure, and data infrastructure.**
- **EU AI Factories.**
  - "Currently, 19 AI Factories and 13 Antennas … are being set up".
  - "The AI Factories are open to European users from various sectors, including industry, research, academia and public authorities", while "prioritising access for AI startups and SMEs".
  - [primary doc] — [European Commission](https://digital-strategy.ec.europa.eu/en/policies/ai-factories)
- **RAISE** (Resource for AI Science in Europe). Launched 3 Nov 2025; €107M in the 2026–27 work programme; observers call it "simply too small and too slow" [search summary in note 2]. — [note 2, Q8](./2_chinese_models_and_frontier.md); [CEPIS](https://cepis.org/raise-pilot/) [search summary]
- **Apertus.** A fully open (weights and data) Swiss public model. — [Hernández-Cano et al. 2026, doi:10.18653/v1/2026.acl-long.2172](https://doi.org/10.18653/v1/2026.acl-long.2172)
- **Local models in practice.** Researchers run local models for privacy, reproducibility and cost. One built a university-network system so that GDPR-protected data "could be searched without leaving the university's network" (note 6). — [Brzostowicki 2026, doi:10.1038/d41586-026-03227-4](https://doi.org/10.1038/d41586-026-03227-4)
- **Arguments and caveats.**
  - "Using proprietary language models in academic research requires explicit justification" — [Palmer, Smith & Spirling 2024](https://doi.org/10.1038/s43588-023-00585-1)
  - [Spirling 2023](https://doi.org/10.1038/d41586-023-01295-4)
  - Caveat: [Widder, Whittaker & West 2024](https://doi.org/10.1038/s41586-024-08141-1)
- **Chat data.**
  - Consumer tiers of the major assistants train on chats by default; education and enterprise tiers are excluded by default. — [note 1](./1_chat_data_and_content_policies.md)
  - For example, "All Google Workspace for Education users have added data protection … their chats with Gemini are not human reviewed or used to train AI models" — [Google](https://blog.google/products-and-platforms/products/education/gemini-enterprise-grade-data-protection/) [search extract, note 1]

### Inferences
- **Evidence and urgency are inversely related.** The reforms that most directly cut volume or reading load (evaluation-side limits, lotteries) have the least outcome evidence. The best-evidenced reforms (Registered Reports, paid review) improve quality or speed per paper without reducing the number of papers to be read. Registered Reports add a second review stage per paper, which is my inference and has no source.
- **Paid review buys commitment and speed, not more experts.**
  - Chetty et al. found no effect on agreement rates or quality.
  - Biology Open's gains came from pre-contracted reviewers.
  - Under AI-scale volume, paying reviewers may move scarce expert attention between journals rather than enlarge it. This is an inference.
- **Narrative CVs are the reform most exposed to cheap text.** The essay should say so, citing Bordignon et al. and Hosseini et al.
- **Lotteries suit the AI era for a reason the literature does not stress.** At the margin they spend no extra reading and remove the reward for polish. They do not reduce the number of applications, and could increase it. That is my inference; I found no data.

### Gaps
- I read none of the following directly:
  - the Volkswagen concluding report (only the funder's summary);
  - the AEA Data Editor's quantitative reports;
  - NWO's pilot outcomes;
  - the 2025 Dutch replication article.
- No study of reviewer-recognition ledgers (Publons/ORCID) with causal design was found.
- The costs of Biology Open's model "at scale" are untested by its authors' own account.

---

## Q3. Rationing or reform: what limits submission, what limits what counts, and what precedents exist for evaluation-side limits?

### Takeaway
- **Rationing restricts what may be *submitted*:**
  - NIH's six applications a year;
  - arXiv's two submissions a month;
  - SocArXiv's one a week;
  - the quotas at ICLR and ACL;
  - submission fees, which ration by price.
- **Evaluation-side limits restrict what *counts*:**
  - the UK's RAE and REF (a few outputs per person since 1996; 2.5 × FTE per unit, and an expectation of no more than five per person, in REF 2029);
  - the DFG (publication lists capped since 2010, now at ten);
  - the ERC (up to ten outputs since 2024);
  - Spain's *sexenios* (five contributions per six years);
  - China's 2020 "representative works";
  - CoARA's 2022 Agreement, which suggests "limiting the number of outputs assessed".
- **The best evidence is Moed (2008).**
  - When the RAE counted totals, output rose.
  - When it moved to "quality", UK authors moved to higher-impact journals.
  - Before 2001, units drifted back to quantity through co-authorship.
- **Two national cases add warnings.**
  - Spain's five-item cap was judged by journal quartile until the criteria of 2023, so a cap read through a venue proxy still rewards venue.
  - China's decree moved discretion to institutional leaders.
- **An evaluation-side limit removes the reward for volume only if** all evaluators adopt it and the selected items are read rather than scored by venue.

### Cited Findings

**Submission-side rationing (in force in 2025–2026)**
- **NIH.** Six new, renewal, resubmission or revision applications per PI per calendar year. NIH expects the cap to affect "a relatively small number of Principal Investigators" (draft ¶4c.2b, audit-verified). — [NIH NOT-OD-25-132](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html)
- **arXiv.** Two submissions per month per submitting researcher from 1 Oct 2026 (draft Table 1). — [arXiv blog, 1 Oct 2026](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/)
- **SocArXiv.** One per author per week. — [SocArXiv AI policy](https://socopen.org/ai-policy/)
- **ICLR 2027.** 20 per author, and at most one paper on which no author has a prior acceptance at a major ML venue. — [ICLR 2027 CfP](https://iclr.cc/Conferences/2027/CallForPapers)
- **ACL Rolling Review.** 20 per author, 5 as first author, and a reviewer-or-lottery rule. — [ARR](https://aclrollingreview.org/sustainable-reviewing-2026)
- **Critics.** Rejected papers go elsewhere, and limits can be gamed by co-authors taking turns (note 6). — [Singh Chawla 2026b, doi:10.1038/d41586-026-03194-w](https://doi.org/10.1038/d41586-026-03194-w)
- **Defenders.** Organisers say caps "encourage authors to submit their best work" [search summary; page returned 403]. — [Science news](https://www.science.org/content/article/ai-triggers-tsunami-submissions-computer-science-conferences-impose-caps)
- **Quota design under co-authorship.** — [Shah 2026, arXiv:2606.10293](https://arxiv.org/abs/2606.10293)

**Evaluation-side limits (precedents)**
- **UK RAE.**
  - "When in the RAE 1992 total publications counts were requested, UK scientists substantially increased their article production. When a shift in evaluation criteria in the RAE 1996 was announced from 'quantity' to 'quality', UK authors gradually increased their number of papers in journals with a relatively high citation impact."
  - "during 1997–2000, institutions raised their number of active research staff by stimulating their staff members to collaborate more intensively, or at least to co-author more intensively … evaluated units in a sense shifted back from 'quality' to 'quantity'."
  - — [Moed 2008, doi:10.1007/s11192-008-0108-1](https://doi.org/10.1007/s11192-008-0108-1); abstract at [RePEc](https://ideas.repec.org/a/spr/scient/v74y2008i1d10.1007_s11192-008-0108-1.html)
- **REF 2029** [primary doc].
  - Outputs are "the volume measure, multiplied by 2.5"; there will be "no minimum output requirements for individual staff members".
  - "The expectation is that no more than 5 outputs are associated with a single substantive link"; outputs are decoupled from named staff.
  - — [REF 2029 guidance, section 4](https://2029.ref.ac.uk/guidance/section-4-contributions-to-knowledge-and-understanding-cku-guidance/)
- **DFG.**
  - "In order to prioritise quality over quantity, the number of project-specific publications to be mentioned in funding proposals has been limited." "The number of an applicant's own publications to be highlighted … is limited to ten." The DFG "ratified DORA in 2021" [primary doc]. — [DFG FAQ](https://www.dfg.de/en/basics-topics/publication-communication/publishing/faq)
  - The 2010 rule allowed five publications in CVs and two per year of funding [search summary]. — [Schiermeier 2010, "German paper chase to end", *Nature* 463:1009](https://doi.org/10.1038/4631009a) [title]
- **ERC.** Applicants are asked "to provide a list of up to ten research outputs […] with an emphasis on more recent achievements" [primary doc]. — [ERC Scientific Council, Evaluation of research proposals (Feb 2024)](https://erc.europa.eu/sites/default/files/2024-02/Evaluation_of_research_proposals-.pdf)
- **Spain (CNEAI *sexenios*)** [primary docs].
  - **Before the reform.** 2020 criteria for Química: "las cinco aportaciones deben ser artículos publicados en revistas situadas en el primer cuartil … en el JCR Science Edition". For Biología Celular y Molecular: "Cinco artículos publicados en revistas situadas en primer cuartil" or "Cinco artículos … en segundo cuartil … siempre que el autor tenga un papel relevante en, al menos, tres de ellas". — [Resolución de 30 de octubre de 2020](https://ugt.unizar.es/sites/ugt/files/users/FESP/cneai_convocatoria_2020_criterios.pdf)
  - **After the reform.** 2024 criteria: "Como ya se indicó en la Resolución de criterios de 2023 … atendiendo acuerdos alcanzados en el Pleno de CNEAI en su sesión de 5 de diciembre de 2023, se eliminan las referencias al apartado de mínimos orientativos, de forma que en todos los campos se podrá alcanzar una evaluación positiva presentando cinco aportaciones". Indexing "puede servir como un argumento complementario en la defensa narrativa … pero no así para obtener de forma automática una valoración positiva". — [Resolución de 9 de diciembre de 2024](https://biblioteca.umh.es/files/2024/12/ResolucionCNEAI_091224.pdf)
- **China.**
  - Rewards based directly on SCI indicators were abolished and "representative works" evaluation introduced (audit, R46). — [MOE & MOST 2020](https://www.gov.cn/zhengce/zhengceku/2020-03/03/content_5486229.htm)
  - Discretion moved to institutional leaders and established scholars, which "disproportionately disadvantage[s] early-career scholars" (audit, R48). — [Zhao et al. 2025, doi:10.1007/s10734-025-01480-6](https://doi.org/10.1007/s10734-025-01480-6)
- **CoARA Agreement.** Among its examples: "Consider limiting the number of outputs assessed (moving away from lists of outputs towards limited selection of key accomplishments and why they are important)", citing Cancer Research UK's 2018 DORA implementation (footnote 34) [primary doc]. — [CoARA Agreement, p. 20](https://www.scienceeurope.org/media/y41ks1wh/20220720-rra-agreement.pdf); [CRUK blog](https://news.cancerresearchuk.org/2018/02/20/improving-research-evaluation-dora/) [not opened]
- **Frith (2020).** Proposes slow-science steps, such as limiting the publications considered in evaluation [DOI verified; content per the governance note, not re-read]. — [doi:10.1016/j.tics.2019.10.007](https://doi.org/10.1016/j.tics.2019.10.007)
- **Spanish output under the sexenio system.**
  - The CNEAI incentive system "has led to the maintenance of, and an increase in, the rate of research production" — [Jiménez-Contreras et al. 2003](https://doi.org/10.1016/S0048-7333(02)00008-2)
  - Contested: growth "cannot be attributed indisputably" to the system [Semantic Scholar machine TLDR, not the abstract] — [Osuna et al. 2011](https://doi.org/10.1007/s11192-010-0312-7)

### Inferences
- **The rationing/reform line for the essay.** A submission cap limits what anyone may communicate, and binds the prolific tail first. An evaluation cap limits only what any evaluator will consider, so communication stays free and the reward for the marginal paper falls to zero. That is the distinction the essay needs, and the precedents show it is administratively feasible.
- **Who rations is not who counts.** arXiv, SocArXiv and conference committees ration because they cannot change what hiring and grant panels reward. The evaluation cap belongs with funders, universities and agencies. Once they adopt it, submission caps can become temporary capacity brakes. This follows from ¶4c.2b of the draft.
- **A cap is only as good as the reading behind it.** Spain capped at five but, until the criteria of 2023, judged the five by JCR quartile. A cap read through a venue proxy reproduces Blekhman's predicted fallback to journal prestige. The DFG, the ERC and REF 2029 ask for a selection *and* peer judgement of it.
- **Caps leak at the margin evaluators still count.** Moed's 1997–2000 drift, through co-authorship and staff counts, and Spain's output growth under a five-item cap show that a cap at one evaluator does not remove volume incentives that other evaluators keep. Harmonising the cap across evaluators is therefore part of the recommendation. This is an inference.

### Gaps
- No study evaluates the DFG's 2010 cap or the ERC's 2024 change.
- No study yet measures the effect of the AI-era submission caps.
- I did not verify the NSF or NIH biosketch limits on listed products, so they are omitted.
- The 2010 DFG details rest on a search summary and a *Nature* news title.

---

## Q4. Which recommendations address "invisible effort" directly?

### Takeaway
Five options act on invisible effort directly:
1. **Evaluate fewer outputs, in depth.**
2. **Contribution statements that include delegation to AI.** Examples: CRediT plus GAIDeT; Hosseini et al.'s modified CRediT and third-person testimonies.
3. **Process or provenance records.** Examples: Cwik's documentation; *Nature*'s prompt transcripts; Mo et al.'s "observable-by-default workflows"; sealed git provenance; "epistemic audits".
4. **Oral discussion or proctored tests of understanding** (Payan et al.).
5. **Paying for and crediting verification.** Examples: *BISE*'s "first-class contributions"; CoARA's examples; Lovén's "verified signal"; Ma.

None has outcome evidence. Records add reading cost and are only partly legible: git captured 21.8% of one narrative trace. They work only if bounded by a cap on what is evaluated, and that coupling is the essay's addition.

### Cited Findings
- **Contribution statements.**
  - They carry information beyond author order. Survey data from more than 6,000 corresponding authors show "strongly diverging views about the benefits and limitations of contribution statements". — [Sauermann & Haeussler 2017, doi:10.1126/sciadv.1700404](https://doi.org/10.1126/sciadv.1700404)
  - Contribution taxonomies may be too coarse for human–AI work (draft Box 1; audit). — [Hutchinson 2026, doi:10.1038/d41586-026-03055-6](https://doi.org/10.1038/d41586-026-03055-6)
  - Modified CRediT and "third-person testimonies". — [Hosseini et al. 2026](https://doi.org/10.1093/reseval/rvag020)
  - Task-level delegation records. — [GAIDeT](https://doi.org/10.1080/08989621.2025.2544331)
- **Process records.**
  - "AI-use disclosure communicates that AI was used; documentation makes the AI-assisted workflow traceable, inspectable, and accountable." — [Cwik 2026](https://doi.org/10.1186/s41073-026-00245-8)
  - Prompt transcripts "alongside the final outputs, as one would with data sets" — [Nature Editorial 2026](https://doi.org/10.1038/d41586-026-00934-w)
  - "observable-by-default workflows" — [Mo et al. 2026](https://arxiv.org/abs/2607.26064)
- **Sealed provenance (Zhou & Yu 2026).** "git sealing with an anchor lineage, hash-bound provenance, red-line gates that refuse non-compliant artifacts and log every refusal". In their prospective case, a pre-registered test "returned No-Go, and that project's frozen stopping rule halted the work". — [arXiv:2608.10858](https://arxiv.org/abs/2608.10858)
- **"Epistemic audit"** (Stoyanov 2026): "a structured record of delegation, verification, provenance, and responsibility". — [arXiv:2608.23644](https://arxiv.org/abs/2608.23644)
- **Agent-Native Research Artifact** (Liu et al. 2026): "an exploration graph that preserves the failures compilation discards". — [arXiv:2604.24658](https://arxiv.org/abs/2604.24658)
- **What git history captures.** An audit of two single-investigator repositories (466 and 103 commits) presented at the NeurIPS 2026 Workshop on AI-Native Academia found:
  - "85.6% of the lines ever committed to the prescriptive trace are visible at the current revision … the narrative trace records episodes and shows 21.8%".
  - Counted by revision, "15 of the prescriptive trace's 41 revisions leave no visible line, against 18 of the narrative trace's 41".
  - The commit-trailer finding was cut off in what I read; a search summary says the trailer was unreliable.
  - — [Wu, Huang & Geng 2026](https://neurips.cc/virtual/2026/166237)
- **Oral or proctored tests.** "a proctored assessment approach that measures authors' understanding of research manuscripts"; institutions "can no longer reliably credit expertise based solely on authors' names on submitted work" (audit R15, R66). — [Payan et al. 2026, arXiv:2609.20481](https://arxiv.org/abs/2609.20481)
- **Verification as the scarce resource.**
  - "verified signal, legitimacy, authentic provenance, and integration capacity" — [Lovén 2026a](https://arxiv.org/abs/2605.02566)
  - "generation cost itself served as a rough filter" — [Ma 2026](https://arxiv.org/abs/2605.10425)
  - "verification, selection, and attention" (note 6) — [Nee, Zhong & Ni 2026, arXiv:2609.04872](https://arxiv.org/abs/2609.04872)
  - Verification outputs as "first-class contributions" — [Hanneke et al. 2026](https://publikationen.bibliothek.kit.edu/1000195177)
  - CoARA examples: "Value diverse outputs (FAIR data sets, replication studies, registered reports, pre-prints)" and "Value contributions such as peer review and editorial roles" — [CoARA Agreement](https://www.scienceeurope.org/media/y41ks1wh/20220720-rra-agreement.pdf)

### Inferences
- **The menu for invisible effort is crowded, but its pieces are not joined.** Provenance and verification are argued (Lovén; Ma; Mo et al.; Cwik), and so are proctored tests (Payan) and human-contribution statements (Hosseini et al.). None of these pieces ties the evidence of effort to *what counts in hiring and promotion*, or to a cap that keeps the reading cost bounded.
- **Joining them is the essay's increment.** For the few outputs a researcher puts forward:
  - a record of how each was made;
  - a contribution and delegation statement;
  - a conversation with the panel.
- **The essay is its own test case.** Box 1 already notes that "a record is costly to read". Wu et al. show it is also partial. The recommendation should promise *legibility for what counts*, not a full record of everything.

### Gaps
- No study evaluates any of these instruments in hiring or promotion.
- I found no published use of oral examination of submitted works in faculty hiring, as distinct from job talks; I did not search for it specifically.

---

## Q5. DORA and CoARA: implementation since 2012 and 2022, and whether DORA's text assumes that outputs reflect the work and that evaluators can read them

*(Added at the coordinator's request for the author's §4d critique.)*

### Takeaway
- **Implementation evidence is thin, mostly self-reported, and where measured it shows persistence of metrics.**
  - **Review, promotion and tenure (RPT) documents.** Studies of 2019–2022 find the Journal Impact Factor in 40% of North American research-intensive institutions' documents, mostly supportively (McKiernan et al. 2019). Across 92 biomedical faculties worldwide, publication counts appear in 95% of guidelines and the JIF in 28% (Rice et al. 2020). In seven countries, "problematic practices of quantification continue to dominate" (Pontika et al. 2022). I found no 2023–2026 replication.
  - **Surveys.** Evaluators rely on metrics, "particularly, the number of publications" (Langfeldt et al. 2021). Faculty think peers value prestige and counts (Niles et al. 2020).
  - **Signatories against non-signatories.** I found no study comparing their practice. Claims on that point appear only on an unattributed secondary site.
- **CoARA.**
  - The Agreement is explicitly non-binding.
  - Progress is tracked through signatories' own action plans.
  - The EC's 2026 study finds engagement "broad and growing" and progress "uneven". It "does not aim to assess success or failure". A commentary on it reports that the core commitments trail the supporting ones, and that only about one action plan in six details the rankings commitment.
- **National cases.**
  - **Spain.** Sexenio criteria set Q1/Q2 JCR thresholds (2020) until the criteria of 2023 removed the "mínimos orientativos". ANECA joined DORA and CoARA in 2023, but quartiles remain admissible as complementary evidence.
  - **Netherlands.** The 2026 Culture Barometer reports the greatest change at policy level and the least at system level; only 15% report the hoped-for benefit.
  - **China.** The 2020 decree shifted discretion to leaders.
- **The "obsolete" half.**
  - DORA's 18 recommendations target the journal-level proxy. They repeatedly ask evaluators to assess "scientific content".
  - They never mention volume, workload, time or evaluator capacity, and the preamble asks to *relax* limits on words, figures and references. Only recommendation 8 touches who did the work (author contributions).
  - CoARA adds peer review "central" and an example of "limiting the number of outputs assessed", but likewise does not address AI-cheapened outputs.

### Cited Findings

**Studies of the JIF and metrics in RPT documents**
- **McKiernan et al. 2019** (US and Canada, 129 universities).
  - "40% of research-intensive institutions and 18% of master's institutions mentioned the JIF, or closely related terms."
  - "Of the institutions that mentioned the JIF, 87% supported its use in at least one of their RPT documents, 13% expressed caution about its use, and none heavily criticized it or prohibited its use."
  - "63% of institutions that mentioned the JIF associated the metric with quality".
  - — [doi:10.7554/eLife.47338](https://doi.org/10.7554/eLife.47338)
- **Rice, Raffoul, Ioannidis & Moher 2020.**
  - Of 170 randomly selected universities, 92 had eligible guidelines.
  - Traditional criteria: "peer reviewed publications, authorship order, journal impact factor, grant funding, and national or international reputation were mentioned in 95% … 37% … 28% … 67% … and 48% … of the guidelines". "data sharing (1%; 1)".
  - Open access, registration and reporting guidelines "were not found in any guidelines reviewed".
  - — [doi:10.1136/bmj.m2081](https://doi.org/10.1136/bmj.m2081)
- **Pontika et al. 2022** (143 RPT documents from 107 institutions in Austria, Brazil, Germany, India, Portugal, the UK and the US). "open and responsible research practices are minimally rewarded and problematic practices of quantification continue to dominate." — [doi:10.1162/qss_a_00224](https://doi.org/10.1162/qss_a_00224)
- **Later updates.** A targeted search found no 2023–2026 replication of McKiernan et al. — search on 16 Oct 2026; see Gaps.

**Surveys and field studies of how evaluation actually works**
- **Langfeldt, Reymert & Aksnes 2021** (survey in three countries; cardiology, economics, physics).
  - "a large majority in all the studied fields indicated that metrics were important or partly important in their review of grant proposals and assessments of candidates for academic positions. In these contexts, the citation impact of the publications and, particularly, the number of publications were emphasized."
  - Reviewers who themselves score high on bibliometric indicators rely on metrics more.
  - — [doi:10.1093/reseval/rvaa032](https://doi.org/10.1093/reseval/rvaa032)
- **Niles et al. 2020** (55 US and Canadian institutions). Respondents "most value journal readership, while they believe their peers most value prestige and related metrics such as impact factor". "total number of publications, number of publications per year, and journal name recognition were the most valued factors in RPT." — [doi:10.1371/journal.pone.0228914](https://doi.org/10.1371/journal.pone.0228914)
- **Hammarfelt & Rushforth 2017** (external evaluations for Swedish academic posts in biomedicine and economics). Indicators serve as "judgment devices", a practice they call "citizen bibliometrics". — [doi:10.1093/reseval/rvx018](https://doi.org/10.1093/reseval/rvx018)
- **The reformers' own diagnoses.**
  - DORA's chair, five years on: institutions had signed but not changed practice (governance note). — [Curry 2018, doi:10.1038/d41586-018-01642-w](https://doi.org/10.1038/d41586-018-01642-w)
  - Change is "difficult, but not impossible" — [Hatch & Curry 2020, doi:10.7554/eLife.58654](https://doi.org/10.7554/eLife.58654)
  - UK progress "real but partial" (governance note) — [Curry, Gadd & Wilsdon 2022](https://doi.org/10.6084/m9.figshare.21701624)
- **Critiques.**
  - "Responsible metrics" as a professional reform movement with three coexisting framings that "may not last indefinitely". — [Rushforth & Hammarfelt 2023, doi:10.1162/qss_a_00280](https://doi.org/10.1162/qss_a_00280)
  - CoARA keeps evaluation administrative. — [Baccini 2025](https://doi.org/10.1093/reseval/rvaf024)
  - CoARA is "unsound" (governance note). — [Abramo 2024](https://doi.org/10.1093/reseval/rvae021)

**Do signatories change practice? Decoupling**
- **No primary study found.** I found no peer-reviewed comparison of DORA or CoARA signatories with non-signatories on RPT content or hiring outcomes.
  - A secondary site (CASRAI) claims the JIF still appears at "roughly a quarter to two-fifths of institutions, including some DORA signatories". It also says neither DORA nor CoARA verifies compliance. Both claims are unattributed, so do not cite them. — [CASRAI](https://casrai.org/guides/dora-coara-institutions-rewriting-pt-criteria) [search summary; unverified]
- **CoARA's design.**
  - "Signatories of this Agreement agree to regularly demonstrate progress … with a touch point at end of 2027 or within five years of signing". Action plans are due "by the end of 2023 or within one year of signing".
  - "this Agreement does not have any legally binding effect".
  - [primary doc] — [CoARA Agreement](https://www.scienceeurope.org/media/y41ks1wh/20220720-rra-agreement.pdf)
- **EC study, *Implementing Research Assessment Reform* (25 Jun 2026)** [primary doc: news page].
  - "engagement with CoARA and ARRA is broad and growing … Progress remains uneven across countries and institutions".
  - "The study does not aim to assess success or failure. Rather, it captures a moment of transition".
  - — [European Commission](https://research-and-innovation.ec.europa.eu/news/all-research-and-innovation-news/new-study-assesses-progress-reforming-research-assessment-2026-06-25_en)
- **SwissCore's commentary on that report** (20 Jul 2026) [full; the report PDF itself was not retrieved].
  - The report "draws on quantitative analysis of 263 submitted ARRA action plans, qualitative analysis of 235 of these plans, and in-depth interviews with 15 signatories".
  - "As of early 2026, ARRA counted 921 signatories, 800 of which are formal CoARA members".
  - "coverage of the four core commitments trails behind supporting commitments like resourcing and communication … Commitment 1 (recognising diverse contributions) is addressed specifically in most action plans, while Commitment 4 (avoiding rankings) is detailed in only around one in six".
  - Barriers "include limited staff time, decentralised governance, and reform fatigue". Many institutions wait "on national laws, funder rules, or ministry decisions outside their control".
  - — [SwissCore, "ARRA 3 years on: Grading the grading reform"](https://www.swisscore.org/?p=8232)
- **Signatory counts.**
  - 994 listed CoARA signatories on 16 Oct 2026 (audit R39). — [CoARA signatories](https://coara.eu/agreement/signatories/)
  - 908 signatories and 787 members in Dec 2025 [search summary]. — [CoARA slides, SUHF](https://suhf.se/app/uploads/2025/12/CoARA_Matthias-Girod_Swedish_NC_251205.pdf)

**National cases**
- **Spain.** ANECA joined DORA and CoARA in 2023 ("al que se incorporó ANECA en 2023 a través de su adhesión a la San Francisco Declaration on Research Assessment (DORA) y a los acuerdos y principios de la Coalition for Advancing Research Assessment (CoARA)"). Applicants must now supply "una narración justificativa de los indicios de relevancia e impacto de cada aportación, apoyados por un uso responsable de indicadores cuantitativos". — [CNEAI 2024](https://biblioteca.umh.es/files/2024/12/ResolucionCNEAI_091224.pdf)
  - **Before the reform:** quartile thresholds (Q3, verbatim). — [CNEAI 2020](https://ugt.unizar.es/sites/ugt/files/users/FESP/cneai_convocatoria_2020_criterios.pdf)
  - **After the reform:** the "mínimos orientativos" were removed by the criteria of 2023, following the plenary of 5 Dec 2023. The 2024 annex still lists "Posición (decil, tercil, cuartil)" and "Journal Impact Factor, Citescore, Scimago Journal Rank" among admissible indicators of the "Impacto del medio de difusión". — [CNEAI 2024](https://biblioteca.umh.es/files/2024/12/ResolucionCNEAI_091224.pdf)
  - **Evidence of effect after 2023:** none found (see also note 1 of the earlier literature folder).
- **Netherlands.**
  - **Utrecht.** Dropped the impact factor in hiring and promotion. — [Woolston 2021, doi:10.1038/d41586-021-01759-5](https://doi.org/10.1038/d41586-021-01759-5) [title, audit]
  - **The open letter against it.** Signed by 175 scientists, 142 of them professors [search summary]. — [Nature Index](https://www.nature.com/nature-index/news/scientists-argue-over-use-of-impact-factors-for-evaluating-research); [Poot & Mulder, THE, "Banning journal impact factors is bad for Dutch science"](https://www.timeshighereducation.com/opinion/banning-journal-impact-factors-bad-dutch-science) [title]
  - **Recognition & Rewards Culture Barometer, second measurement (summary dated 5 Jun 2026)** [full summary, two-column PDF; quotations reconstructed across columns].
    - Respondents report "the fewest changes resulting from Recognition & Rewards at the system level, somewhat more at the cultural level, and the greatest changes at the policy level". "many staff members feel that structural changes have yet to materialise".
    - "In 2024, almost half of respondents expected the programme to increase their enjoyment of work; by 2026, only 15% report actually experiencing this benefit". "almost one-third report an increase" in workload.
    - "Without clear and transparent criteria and sufficient resources, there is a risk that the programme will remain largely symbolic or lead to greater subjectivity".
    - "At 42% of institutions, staff can choose between different career pathways".
    - Response rates were low: 14.1% at RUG against 24.6% in 2024 [search summary].
    - — [RUG-hosted summary](https://www.rug.nl/about-ug/policy-and-strategy/recognition-rewards/summary-recognition-rewards-culture-barometer.pdf)
- **China.**
  - The 2020 reform "trusts the institutions to implement the policy within a few months but does not provide the necessary national platforms for coordination". — [Zhang & Sivertsen 2020, doi:10.29024/sar.15](https://doi.org/10.29024/sar.15)
  - Discretion shifted to leaders (*lingdao*) and established scholars (*xuefa*), disadvantaging early-career researchers (audit). — [Zhao et al. 2025](https://doi.org/10.1007/s10734-025-01480-6)
  - A 2022 headline: "China's promised research reform 'little more than PR exercise'" [title]. — [THE](https://www.timeshighereducation.com/node/721809)
  - No bibliometric before/after study found.

**DORA's text: the "obsolete" half** (all quotations verbatim from [sfdora.org/read](https://sfdora.org/read/), read 16 Oct 2026)
- **Preamble.**
  - "It is thus imperative that scientific output is measured accurately and evaluated wisely."
  - "the peer-reviewed research paper will remain a central research output that informs research assessment."
  - The themes include "the need to assess research on its own merits rather than on the basis of the journal in which the research is published; and the need to capitalize on the opportunities provided by online publication (such as relaxing unnecessary limits on the number of words, figures, and references in articles, and exploring new indicators of significance and impact)."
- **1 (general).** "Do not use journal-based metrics, such as Journal Impact Factors, as a surrogate measure of the quality of individual research articles, to assess an individual scientist's contributions, or in hiring, promotion, or funding decisions."
- **2 (funders) and 4 (institutions).** "Be explicit about the criteria used … clearly highlighting, especially for early-stage investigators, that the scientific content of a paper is much more important than publication metrics or the identity of the journal in which it was published."
- **3 and 5.** "consider the value and impact of all research outputs (including datasets and software) in addition to research publications".
- **7 (publishers).** "Make available a range of article-level metrics to encourage a shift toward assessment based on the scientific content of an article rather than publication metrics of the journal in which it was published."
- **8 (publishers).** "Encourage responsible authorship practices and the provision of information about the specific contributions of each author."
- **15 (researchers).** "When involved in committees making decisions about funding, hiring, tenure, or promotion, make assessments based on scientific content rather than publication metrics."
- **17.** "Use a range of article metrics and indicators on personal/supporting statements, as evidence of the impact of individual published articles and other research outputs".
- **What the text does not say.** A word search of DORA's text finds no occurrence of "volume", "workload", "time", "capacity", "burden" or "quantity". "productivity" appears once (recommendation 2). "number of" occurs only about the JIF's deficiencies and about limits on words, figures and references. — [sfdora.org/read](https://sfdora.org/read/)
- **CoARA's Agreement.**
  - Commitment 2: "Base research assessment primarily on qualitative evaluation for which peer review is central".
  - Commitment 10: "Commit resources … whether in the form of budget or staff capacity".
  - The example "Consider limiting the number of outputs assessed".
  - No occurrence of "volume" or "workload".
  - — [CoARA Agreement](https://www.scienceeurope.org/media/y41ks1wh/20220720-rra-agreement.pdf)

### Inferences
- **"Never applied" is stronger than the evidence allows.** The evidence supports "largely unimplemented where it has been measured, and mostly unmeasured":
  - RPT documents and evaluator surveys show metrics and counts persisting.
  - The EC's own study declines to judge success.
  - The Dutch barometer shows change at the policy level more than in practice.
  - No study compares signatories with non-signatories.
  - Suggested wording: "a decade after DORA, the evidence that its signatories changed how they evaluate is thin, and where practice has been measured, counts and journal metrics persist (McKiernan et al. 2019; Rice et al. 2020; Pontika et al. 2022; Langfeldt et al. 2021)".
- **The decoupling evidence is direct but national.**
  - In the Netherlands the barometer is the clearest measure of a gap between commitment and practice: policy level greatest, system level least.
  - In Spain the shift from quartile thresholds to narratives came 11 years after DORA, and quartiles survive as admissible evidence.
  - In China, a decree without platforms moved discretion rather than removing proxies.
- **"Obsolete" can be argued from the text, not only from implementation.**
  - DORA's remedy is to replace a *journal* proxy with reading the paper's "scientific content". That presupposes two things AI removes:
    - **The content is evidence of the researcher's work.** Only recommendation 8, on author contributions, touches who did what.
    - **Committees have time to read.** No recommendation addresses volume or evaluator capacity, and the preamble even asks to relax limits on length.
  - DORA was written against the impact factor, not against cheap papers. In a world of near-free text, "assess the scientific content" is necessary but no longer sufficient.
  - CoARA's example of "limiting the number of outputs assessed" is the clause best suited to the AI era, and it is optional.
- **The EC commentary's barrier list includes "limited staff time"**, the same resource the essay says AI-era volume consumes. This supports ¶4c.1's claim that reform depends on reading capacity.

### Gaps
- No 2023–2026 replication of McKiernan et al. found. A targeted search returned only the 2019 paper and secondary summaries.
- The EUA's 2019 survey of research assessment was not verified (Crossref search failed) and is omitted.
- I did not retrieve the EC 2026 report PDF; its figures come from SwissCore's commentary. I could not reach CoARA's action-plan analysis page (connection reset).
- ANECA's *acreditación* criteria (as opposed to *sexenios*) were not examined.
- I did not open the full Dutch barometer report (5 Jun 2026), and response rates were low.
- DORA's current signer counts were not verified.

---

## Q6. Synthesis: classification, novelty check, menu, shortlist and draft text

### Takeaway
- **24 recommendations** are classified below by actor, driver and type.
- **The essay can claim, after a quick check, three increments** (all hedged as "appears new"):
  1. **Move the cap from submitters to counters.** Use evaluation-side limits as the replacement for AI-era submission rationing, harmonised across evaluators.
  2. **Bound the evidence of effort by the cap.** Attach a process record and a conversation with the panel only to the few outputs that count.
  3. **Monitor model-family concentration** through machine-readable AI-use statements, as the measurable trace of the external driver.
- **Everything else must be credited:** to Huang et al., Hansen, Hanneke et al., CoARA, Hosseini et al., Lovén, Ma, Payan et al., Cwik, Azoulay et al., the lottery funders, and others.

### Cited Findings
**How novelty was checked (16 Oct 2026).**
- **Evaluation caps as the replacement for submission caps.**
  - **Searched:** a web search (extended mode) for "generative AI research assessment evaluate fewer outputs instead of submission caps 'best' papers proposal 2026"; the closest-work inventory in note 6; and the full texts of DORA and CoARA.
  - **Found:**
    - CoARA's example "Consider limiting the number of outputs assessed" — [CoARA Agreement](https://www.scienceeurope.org/media/y41ks1wh/20220720-rra-agreement.pdf)
    - Frith 2020 — [doi](https://doi.org/10.1016/j.tics.2019.10.007)
    - the practice in the RAE/REF, DFG, ERC, CNEAI and China (Q3)
    - Hosseini et al. 2026, with no caps in the abstract — [doi](https://doi.org/10.1093/reseval/rvag020)
    - organisers defending *submission* caps as a push to "best work" — [Science](https://www.science.org/content/article/ai-triggers-tsunami-submissions-computer-science-conferences-impose-caps) [search summary]
  - **Not found:** any 2023–2026 piece proposing evaluation-side caps *instead of* AI-era submission rationing, or arguing that the cap belongs with the evaluators who count.
- **Process records and oral discussion tied to the evaluated set.**
  - **Searched:** "AI-assisted research effort invisible process record provenance version history evaluation hiring oral defence proposal".
  - **Found:**
    - Zhou & Yu — [arXiv:2608.10858](https://arxiv.org/abs/2608.10858)
    - Stoyanov — [arXiv:2608.23644](https://arxiv.org/abs/2608.23644)
    - Liu et al. — [arXiv:2604.24658](https://arxiv.org/abs/2604.24658)
    - Wu et al. — [NeurIPS 2026 workshop](https://neurips.cc/virtual/2026/166237)
    - a statistics preprint's AI-workflow supplement [not opened] — [Cambridge Statslab](https://www.statslab.cam.ac.uk/~qz280/publication/marginal-conditional-error/ai-workflow-supplement.pdf)
    - plus Cwik, Mo et al. and Payan et al. (Q4)
  - **Not found:** any proposal linking records or oral examination to hiring and promotion, or to a cap on what is evaluated.
- **Model-family monitoring.**
  - **Searched:** "monitor which AI models scientists use model monoculture science concentration proposal report model version papers".
  - **Found:**
    - Hodel & West, whose simulations show "diversity improves long-term performance of models, while monoculture accelerates collapse" and who recommend monitoring "(dis)agreement among AI systems" [the second phrase is from a search summary; my abstract extract was cut] — [arXiv:2512.15011](https://arxiv.org/abs/2512.15011)
    - Messeri & Crockett's monocultures (note 6)
    - a simulation paper [not opened] — [arXiv:2608.19390](https://arxiv.org/abs/2608.19390)
    - GAIDeT records the AI version per paper — [doi](https://doi.org/10.1080/08989621.2025.2544331)
  - **Not found:** a proposal to track model-family adoption across the literature as a governance indicator.
- **Checked and *not* new: verification as a countable output.** Anticipated by:
  - [Hanneke et al. 2026](https://publikationen.bibliothek.kit.edu/1000195177)
  - [Lovén 2026a](https://arxiv.org/abs/2605.02566)
  - [Ma 2026](https://arxiv.org/abs/2605.10425)
  - [Mo et al. 2026](https://arxiv.org/abs/2607.26064)
  - [CoARA 2022](https://www.scienceeurope.org/media/y41ks1wh/20220720-rra-agreement.pdf)
- **Limits of the check.**
  - One or two searches per idea, in English only.
  - No systematic scan of the NeurIPS 2026 AI-Native Academia workshop, whose papers are close to this topic.
  - No semantic search in OpenAlex or Semantic Scholar.

### Inferences
- **Notes for the draft** (to pass to the coordinator):
  1. ¶6.1 already contains the seeds (Frith; Payan; Cwik; Azoulay; Huang). The new section should replace ¶6.1, keeping its stance: "proposals, not solutions".
  2. Credit **CoARA 2022** next to Frith 2020 for "limiting the number of outputs assessed".
  3. Add **Hosseini et al. 2026**, **Lovén 2026** and **Ma 2026** to the must-cite list, and **Wu et al. 2026** as a caveat in Box 1.
  4. ¶4c.3:
     - restore "refundable deposits" (confirmed in Hanneke et al.);
     - the [CITATION NEEDED] on fees and poorer researchers can use Hanneke et al.'s waiver sentence now, and Oldford et al. 2023 after the author reads it.
  5. Cite Fourie for diagnosis ("rationed, not priced"; screens priced at the cost of passing them), not as a proposer of fees.
  6. The EMBO version's 15-reference limit: the condensed draft below uses seven references.

### Gaps
- None of the three "appears new" items has outcome evidence. They are design proposals, and should be labelled as such.
- The external-driver recommendations rest on capacity facts and simulations, not evaluations.

### Menu table (24 recommendations)

| # | Recommendation | Actor | Driver | Rationing or reform | Evidence of effect (sources) | Who proposed it (credit) |
|---|---|---|---|---|---|---|
| M1 | Keep per-person submission caps only as temporary capacity brakes, with sunset dates and published data | Funders (NIH); preprint servers (arXiv, SocArXiv); conferences (ICLR, ACL) | I | Rationing (submission) | No outcome evaluation yet. NIH expects to affect "a relatively small number" of PIs ([NIH 2025](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html)). Critics: displacement, co-author turn-taking ([Singh Chawla 2026b](https://doi.org/10.1038/d41586-026-03194-w)) | In force: [NIH](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html), [arXiv](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/), [SocArXiv](https://socopen.org/ai-policy/), [ICLR](https://iclr.cc/Conferences/2027/CallForPapers), [ACL](https://aclrollingreview.org/sustainable-reviewing-2026). Quota design: [Shah 2026](https://arxiv.org/abs/2606.10293). Sunset and evaluation: essay-derived; general principle in Wissenschaftsrat 2017 via [VW](https://www.volkswagenstiftung.de/en/news/news/everyone-equal-lottery-drum) and [Nielsen & Qiu 2022](https://scienceplusplus.org/metascience/) |
| M2 | Submission fees or refundable deposits, tiered, with waivers | Journals | I | Rationing (price) | Elasticity −0.11 per $100 ([Zheng & Kaiser 2016](https://doi.org/10.1111/ecin.12277)). Cuts system demand only if authors stop, shorten chains or switch ([Fourie 2026b](https://arxiv.org/abs/2608.14760)). Equity risk ([Oldford et al. 2023](https://doi.org/10.1007/s11192-023-04758-7), title only) | [Hanneke et al. 2026](https://doi.org/10.1007/s12599-026-01013-0); [Atasu 2026](https://doi.org/10.2139/ssrn.6393158) (AI-use-contingent); [Lopez-Lira & Seyfi 2026](https://doi.org/10.2139/ssrn.6337880) |
| M3 | Pay reviewers, conditional on on-time, adequate reports | Journals; funders (grant review) | I | Capacity | Completion 49.8% vs 42.2%, no quality difference ([Cotton et al. 2025](https://doi.org/10.1097/CCM.0000000000006637)). 5.5 vs 37.7 working days ([Gorelick & Clark 2026](https://doi.org/10.64898/2026.06.02.729548), preprint). Cash speeds reports, no crowd-out ([Chetty et al. 2014](https://doi.org/10.1257/jep.28.3.169)) | [Hansen 2026](https://doi.org/10.1186/s41073-026-00193-3); [Atasu 2026](https://doi.org/10.2139/ssrn.6393158); [Hanneke et al. 2026](https://doi.org/10.1007/s12599-026-01013-0); diagnosis [Fourie 2026a](https://arxiv.org/abs/2607.13844) |
| M4 | Portable reviews; tiered review by epistemic risk; curation without exclusion | Journals; preprint servers | I | Capacity (redesign) | None found | [Hansen 2026](https://doi.org/10.1186/s41073-026-00193-3); [Hanneke et al. 2026](https://doi.org/10.1007/s12599-026-01013-0) (portable reviews) |
| M5 | Bounded AI triage (checklists, procedural checks, advisory only); no delegation of merit judgements | Journals; funders | I | Capacity (automation) | None on outcomes. Rule-based screens are gamed until "its verdict is worth exactly what getting past it costs" ([Fourie 2026a](https://arxiv.org/abs/2607.13844)) | [Hanneke et al. 2026](https://doi.org/10.1007/s12599-026-01013-0); [Hansen 2026](https://doi.org/10.1186/s41073-026-00193-3); [Bhargava et al. 2026](https://doi.org/10.1287/mnsc.2026.00184); [EC living guidelines 2024](https://research-and-innovation.ec.europa.eu/document/2b6cf7e5-36ac-41cb-aab5-0d32050143dc_en) |
| M6 | Registered Reports | Journals; funders | I | Reform (design judged before results) | 44% vs 96% positive results ([Scheel et al. 2021](https://doi.org/10.1177/25152459211007467)). Higher rigour, novelty not lower ([Soderberg et al. 2021](https://doi.org/10.1038/s41562-021-01142-4)) | [Chambers & Tzavella 2022](https://doi.org/10.1038/s41562-021-01193-7); CoARA example |
| M7 | Publish–review–curate (public assessments, no accept/reject) | Journals | I | Reform (redesign) | No outcome study. Lost JIF; partial WoS indexing ([HKUST](https://library.hkust.edu.hk/sc/elife-indexing-change/), secondary) | [Eisen et al. 2022](https://doi.org/10.7554/eLife.83889) |
| M8 | Evaluate at most N self-selected outputs per period, read in depth | Universities; funders; assessment agencies | I | **Evaluation-side limit** | Behaviour follows the rule; drift via co-authorship ([Moed 2008](https://doi.org/10.1007/s11192-008-0108-1)). Discretion shift in China ([Zhao et al. 2025](https://doi.org/10.1007/s10734-025-01480-6)). Spain's cap read by quartile ([CNEAI 2020](https://ugt.unizar.es/sites/ugt/files/users/FESP/cneai_convocatoria_2020_criterios.pdf)) | [CoARA 2022](https://www.scienceeurope.org/media/y41ks1wh/20220720-rra-agreement.pdf); [Frith 2020](https://doi.org/10.1016/j.tics.2019.10.007); practice: [DFG](https://www.dfg.de/en/basics-topics/publication-communication/publishing/faq), [ERC](https://erc.europa.eu/sites/default/files/2024-02/Evaluation_of_research_proposals-.pdf), [CNEAI 2024](https://biblioteca.umh.es/files/2024/12/ResolucionCNEAI_091224.pdf), [REF 2029](https://2029.ref.ac.uk/guidance/section-4-contributions-to-knowledge-and-understanding-cku-guidance/); [Blekhman 2026](https://doi.org/10.1371/journal.pbio.3004075) ("paper counts are meaningless") |
| M9 | Move the cap from submitters to counters: retire submission caps as evaluators adopt M8, and harmonise N across hiring, promotion and funding | Funders; universities; agencies (with preprint servers and conferences) | I | Reform replacing rationing | None (proposal). Moed's drift and Spain suggest single-evaluator caps leak | **Essay-derived; appears new** (see the novelty check) |
| M10 | A process record for each evaluated output: version history, data and code, AI-use documentation | Researchers; universities; funders; journals | I | Reform (evidence of making) | None on effect. Legibility limits: 21.8% of a narrative trace visible ([Wu et al. 2026](https://neurips.cc/virtual/2026/166237)) | [Cwik 2026](https://doi.org/10.1186/s41073-026-00245-8); [Nature Editorial 2026](https://doi.org/10.1038/d41586-026-00934-w); [Mo et al. 2026](https://arxiv.org/abs/2607.26064); [Stoyanov 2026](https://arxiv.org/abs/2608.23644); [Zhou & Yu 2026](https://arxiv.org/abs/2608.10858). Coupling to M8: **essay-derived, appears new** |
| M11 | Oral discussion of the selected outputs; proctored tests of understanding | Universities (hiring, promotion); funders (large grants) | I | Reform (costly signal) | None found | [Payan et al. 2026](https://arxiv.org/abs/2609.20481). Coupling to M8: **essay-derived** |
| M12 | Contribution statements including delegation to AI; third-person testimonies | Journals; universities | I | Reform | Statements add information but views diverge ([Sauermann & Haeussler 2017](https://doi.org/10.1126/sciadv.1700404)). GAIDeT not yet validated | [Hosseini et al. 2026](https://doi.org/10.1093/reseval/rvag020); [Suchikova et al. 2025](https://doi.org/10.1080/08989621.2025.2544331); [Hutchinson 2026](https://doi.org/10.1038/d41586-026-03055-6); DORA rec. 8 |
| M13 | AI-use documentation standards (minimal and extended); declarations in national assessment | Journals; agencies | I (E if the model is named) | Reform (transparency) | Disclosure "fragile" under incentives to underreport ([Hanneke et al. 2026](https://doi.org/10.1007/s12599-026-01013-0)). Policies heterogeneous ([Ganjavi et al. 2024](https://doi.org/10.1136/bmj-2023-077192)) | [Cwik 2026](https://doi.org/10.1186/s41073-026-00245-8); [CNEAI 2024](https://biblioteca.umh.es/files/2024/12/ResolucionCNEAI_091224.pdf); counterpoint [Earp et al. 2026](https://doi.org/10.1007/s00146-026-03326-w) |
| M14 | Narrative CVs | Funders; universities | I | Reform | Thin ([Bordignon et al. 2023](https://doi.org/10.1093/reseval/rvad013)). Exposed to GenAI ([Hosseini et al. 2026](https://doi.org/10.1093/reseval/rvag020)) | DORA/CoARA; Hosseini et al. ("strengthened") |
| M15 | Responsible-metrics commitments (DORA, Leiden, Hong Kong, CoARA), revised for AI-era volume | Universities; funders | I | Reform | Metrics persist in RPT documents ([McKiernan et al. 2019](https://doi.org/10.7554/eLife.47338); [Pontika et al. 2022](https://doi.org/10.1162/qss_a_00224)). "Uneven" ([EC 2026](https://research-and-innovation.ec.europa.eu/news/all-research-and-innovation-news/new-study-assesses-progress-reforming-research-assessment-2026-06-25_en)) | [DORA](https://sfdora.org/read/); [Hicks et al. 2015](https://doi.org/10.1038/520429a); [Moher et al. 2020](https://doi.org/10.1371/journal.pbio.3000737); CoARA; [Blekhman 2026](https://doi.org/10.1371/journal.pbio.3004075) (goal-aligned evaluation) |
| M16 | Partial-randomisation lotteries for the fundable middle | Funders | I | Reform (allocation) | Diversity and less bias (VW, funder's summary). 63% acceptable ([Liu et al. 2020](https://doi.org/10.1186/s41073-019-0089-z)). Fairness depends on design ([Feliciani et al. 2024](https://doi.org/10.1093/reseval/rvae025)) | [Fang & Casadevall 2016](https://doi.org/10.1128/mBio.00422-16); [SNSF method](https://doi.org/10.1080/2330443X.2022.2086190); CoARA example |
| M17 | Long-horizon, failure-tolerant and exploratory grants; stop penalising pivots | Funders; universities (hiring) | I | Reform | HHMI vs NIH ([Azoulay et al. 2011](https://doi.org/10.1111/j.1756-2171.2011.00140.x)) | [Huang et al. 2026](https://doi.org/10.1038/d41586-026-02961-z) |
| M18 | Reward conceptual distance and lasting disruption, not short-window citations | Funders; universities | I | Reform (what counts) | None; the indicator is untested (Goodhart risk is my inference) | [Huang et al. 2026](https://doi.org/10.1038/d41586-026-02961-z) |
| M19 | Count verification as output: signed reviews, replications, reproducibility checks, null results, evidence packages | Universities; funders; journals | I | Reform (what counts) | Social incentives speed reviews ([Chetty et al. 2014](https://doi.org/10.1257/jep.28.3.169)). No formal adoption found | [Hong Kong Principles](https://doi.org/10.1371/journal.pbio.3000737); [Hansen 2026](https://doi.org/10.1186/s41073-026-00193-3); [Hanneke et al. 2026](https://doi.org/10.1007/s12599-026-01013-0); [CoARA](https://www.scienceeurope.org/media/y41ks1wh/20220720-rra-agreement.pdf); [Lovén 2026a](https://arxiv.org/abs/2605.02566); [Ma 2026](https://arxiv.org/abs/2605.10425) |
| M20 | Data and code editors; reproducibility checks before acceptance | Journals | I | Reform (verification) | Run at scale by AEA ([Vilhuber et al. 2022](https://arxiv.org/abs/2204.01540)). No downstream study found | AEA |
| M21 | Fund verification capacity: replication grants and AI-assisted replication tools | Funders; governments | I | Reform (capacity for verification) | NWO pilot, no outcome report found ([Editage](https://www.editage.com/insights/dutch-organization-launches-worlds-first-national-fund-for-replication-studies), secondary). Tools benchmarked ([VERITAS](https://arxiv.org/abs/2607.02931)) | NWO; [Kubota et al. 2026](https://arxiv.org/abs/2602.18453); [Lovén 2026b](https://arxiv.org/abs/2604.22966) ("verification as commons") |
| M22 | Subsidise data infrastructure in neglected domains | Funders; governments | A | Reform (infrastructure) | None. Mechanism: prediction costs down ~100-fold, observation costs high ([Huang et al. 2026](https://doi.org/10.1038/d41586-026-02961-z)) | [Huang et al. 2026](https://doi.org/10.1038/d41586-026-02961-z) |
| M23 | Public or institution-run AI for research (open models on public compute) and contracts that keep researchers' chats out of training | Governments (EU AI Factories, RAISE); universities | E | Infrastructure | No evaluation. 19 AI Factories open to academia but prioritising startups ([EC](https://digital-strategy.ec.europa.eu/en/policies/ai-factories)). Education tiers excluded from training ([note 1](./1_chat_data_and_content_policies.md)) | [Spirling 2023](https://doi.org/10.1038/d41586-023-01295-4); [Palmer et al. 2024](https://doi.org/10.1038/s43588-023-00585-1); [Brzostowicki 2026](https://doi.org/10.1038/d41586-026-03227-4); [Apertus](https://doi.org/10.18653/v1/2026.acl-long.2172); caveat [Widder et al. 2024](https://doi.org/10.1038/s41586-024-08141-1) |
| M24 | Monitor model-family concentration: machine-readable model family and version in AI-use statements, a public index, and funding for model diversity | Journals; funders; metascience units | E | Reform (monitoring) | None. Simulations: diversity slows collapse ([Hodel & West 2025](https://arxiv.org/abs/2512.15011)) | **Essay-derived; appears new.** Adjacent: Hodel & West; [Kleinberg & Raghavan 2021](https://doi.org/10.1073/pnas.2018340118); GAIDeT records version |

### Proposed shortlist for the essay (7)

| # | Shortlisted recommendation (menu rows) | Actor | Driver | Type | Credit | Status |
|---|---|---|---|---|---|---|
| S1 | **Count fewer outputs, and read them; move the cap from submitters to counters** (M8, M9, M1) | Universities, funders, agencies; arXiv and conferences keep only brakes | I | Evaluation-side limit replacing rationing | CoARA 2022; Frith 2020; practice at RAE/REF, DFG, ERC, CNEAI; Blekhman 2026; evidence Moed 2008 | The practice is credited. The substitution and "the cap belongs with the counters" argument **appears new** |
| S2 | **Make effort visible where it counts:** a process record and a conversation with the panel for each selected output (M10, M11, M12) | Researchers; universities; funders | I | Reform | Cwik 2026; Payan et al. 2026; Hosseini et al. 2026; Nature Editorial 2026; Mo et al. 2026; caveat Wu et al. 2026 | The components are credited. Bounding them by the cap **appears new** |
| S3 | **Pay for verification, and count it** (M3, M19, M20, M21) | Journals; funders; universities | I | Capacity + reform | Hansen 2026; Hanneke et al. 2026; Atasu 2026; Hong Kong Principles; CoARA; Lovén 2026; Ma 2026; evidence Cotton et al. 2025, Gorelick & Clark 2026, Chetty et al. 2014 | Credited (not new) |
| S4 | **Reward exploration directly:** exploratory, long-horizon grants; no pivot penalties; distance indicators; lotteries for the fundable middle (M17, M18, M16) | Funders; universities | I | Reform | Huang et al. 2026; Azoulay et al. 2011; Fang & Casadevall 2016; SNSF, HRC, VW | Credited |
| S5 | **Public infrastructure for data and models:** data for neglected domains; institution-run open models; no-training contracts (M22, M23) | Governments; universities; funders | A + E | Infrastructure | Huang et al. 2026; Spirling 2023; Palmer et al. 2024; Brzostowicki 2026; EU AI Factories; Apertus | Credited. Linking it to the external driver is the essay's framing |
| S6 | **Measure the external driver:** model family and version in AI-use statements, tracked across science (M24) | Journals; funders; metascience units | E | Reform (monitoring) | Adjacent: Hodel & West 2025; Kleinberg & Raghavan 2021; GAIDeT | **Appears new** |
| S7 | **Treat the caps as experiments:** sunset dates, published data, evaluation (M1) | NIH; arXiv; conferences | I | Rationing, governed | Nielsen & Qiu 2022; the Wissenschaftsrat principle (via VW) | Partly new; novelty not checked separately. Can be merged into S1 |

### Draft section (~630 words) — DRAFT for the author to merge with their own recommendations

> **Recommendations: ration what counts, not what is said**
>
> The responses so far ration what may be submitted; mine aim at what is counted. Most are borrowed and none rests on strong evidence, so each should be run as an experiment and evaluated (Nielsen & Qiu 2022). They share one premise: when outputs are cheap, the scarce resources are reading, verification and exploration, and evaluation should spend them where they matter. [AUTHOR: merge with your own recommendations.]
>
> *Count fewer outputs, and read them.* Hiring, promotion, grant and national assessments would each consider a few outputs per period, chosen by the researcher. CoARA's agreement already suggests "limiting the number of outputs assessed" (CoARA 2022), and the practice is old. When the UK's Research Assessment Exercise moved from total publication counts to quality in 1996, UK authors shifted to journals with higher citation impact (Moed 2008). The DFG and the ERC now cap the outputs applicants list at ten, and Spain's *sexenios* at five. AI changes the case for it. A cap on what counts removes the reward for volume without limiting what anyone may communicate, and it bounds the reading on which reform depends. It belongs with those who count: if panels capped what they read, the caps of NIH and arXiv could revert to temporary brakes, with sunset dates and published data. Moed's data carry a warning: units later drifted back towards quantity through co-authorship, so a cap at one evaluator will not hold while others still count. And a cap read through journal quartiles, as Spain's was until 2023, only counts venues more selectively.
>
> *Make effort visible where it counts.* For each output put forward, the researcher would supply a record of how it was made (version history, data and code, and documentation of AI use rather than bare disclosure; Cwik 2026) and discuss it with the panel, which tests understanding as a proctored test of authorship would (Payan et al. 2026). Records are costly to read and only partly legible, git histories included (Wu et al. 2026); the cap is what makes reading them affordable, and Box 1 shows both.
>
> *Pay for verification, and count it.* Paying reviewers raised completion and speed without lowering quality in two journal trials (Cotton et al. 2025; Gorelick & Clark 2026). Reviews, replications and data and code checks should be eligible among the outputs that count (Moher et al. 2020; Hanneke et al. 2026). Verification is what cheap generation leaves scarce (Ma 2026; Lovén 2026).
>
> *Reward exploration directly.* Huang et al. (2026) ask funders for exploratory grants with extended evaluation horizons, an end to penalties on pivots, and indicators of conceptual distance from past work. The best evidence that long, failure-tolerant funding moves research towards novel lines comes from HHMI (Azoulay et al. 2011). For the fundable middle of a ranking, a lottery spends no extra reading and removes the premium on polish (Heyard et al. 2022). [AUTHOR: one change you would make as chair of a hiring or grant panel.]
>
> *Answer the external driver in public.* Subsidising data infrastructure in neglected domains answers the pull of data-rich problems (Huang et al. 2026). Institution-run open models on public compute, such as Apertus (Hernández-Cano et al. 2026) or Europe's AI Factories, reduce dependence on a few firms (Palmer et al. 2024). So do contracts that keep researchers' chats out of training, as education licences already do. It should also be measured: if AI-use statements named the model family and version in a machine-readable field, as delegation taxonomies allow (Suchikova et al. 2025), funders could track whether science converges on a few models (Kleinberg & Raghavan 2021).
>
> Some reforms on offer will not survive cheap text: narrative CVs rest on little evidence (Bordignon et al. 2023) and are now cheap to write (Hosseini et al. 2026). What survives spends human judgement on less, rather than asking it to keep up with more.

### Condensed version (~290 words) — DRAFT for the EMBO Reports version

> **What to do instead of rationing**
>
> Caps restore scarcity at the door; I suggest restoring it where evaluation happens.
>
> First, count fewer outputs and read them. Hiring, promotion and grant panels would each consider a few outputs per period, chosen by the researcher. CoARA's agreement suggests this, and Spain's *sexenios* (five contributions) and the ERC (up to ten) already do it. When the UK's research assessment made a similar move in 1996, authors shifted towards higher-impact journals (Moed 2008). A cap on what counts removes the reward for volume without limiting what anyone may say, and it bounds the reading that reform depends on. It belongs with those who count. Preprint servers and conferences ration because they cannot change what panels reward; once panels cap what they read, submission caps can revert to temporary brakes. But a cap read through journal quartiles, as Spain's was until 2023, only counts venues more selectively.
>
> Second, make effort visible where it counts: a record of how each selected output was made, with documented AI use, discussed with the panel (Cwik 2026; Payan et al. 2026).
>
> Third, pay for verification and count it. Paid reviewers completed more reviews, faster and with no loss of quality, in a quasi-randomised trial (Cotton et al. 2025), and reviews, replications and code checks should count among the selected outputs.
>
> Fourth, fund exploration on long horizons and stop penalising pivots (Huang et al. 2026; Azoulay et al. 2011).
>
> Fifth, answer the external driver in public: data infrastructure for neglected domains, institution-run open models, and AI-use statements that name the model, so that convergence on a few models can be tracked.
>
> [AUTHOR: your own recommendations.] None of this has strong evidence, so each step should be run as an experiment and evaluated.

*(Seven references: Moed 2008; Cwik 2026; Payan et al. 2026; Cotton et al. 2025; Huang et al. 2026; Azoulay et al. 2011; and CoARA 2022 if cited formally. Cotton et al. call their design "quasi-randomized".)*
