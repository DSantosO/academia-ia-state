# Referee report: "Even good use breaks it: academic evaluation is not prepared for AI"

**Manuscript:** `paper/draft_full.md`, draft 1 of 16 Oct 2026 (commit e1c8d52). This is the master version: about 6,800 words and 173 references.

**Read against:**
- `paper/brief.md`, the author's intent, treated as authoritative;
- `paper/submission_strategy.md`, the target venues;
- `research_notes/AI academia essay evidence gaps/6_closest_prior_work.md`, for novelty;
- `paper/outline.md` §11, the known weaknesses;
- for checking: the outline's claims register (§7), research notes 1 and 3, and the repository's git log.

**Roles:**
- Editor A, EMBO Reports (Science & Society);
- Referee 1, metascience and research evaluation;
- Referee 2, STS and philosophy of science.

**Date:** 16 Oct 2026.

**Conventions:**
- **¶ numbers** are the paragraph IDs in the draft's HTML comments (¶0.1 to ¶6.3). "Box 1" and "Box 2" follow the master's numbering.
- **Audit:** marks a fact I doubt or could not check. It is a request to the citation audit, not a correction.
- **Suggested wording** is quoted as a block. Square brackets inside it are for the author to fill.

**Disclosure.** This review was written by an AI agent (Claude, Anthropic), the same model family that drafted the essay. It is the "adversarial review" that Box 1 describes, and this file is its record. It is not independent peer review, and it probably shares the drafter's blind spots. Before submission, one human reader from outside the project should read the revised essay (Referee 2, issue 3).

---

## Verdicts at a glance

| Role | Decision | One-line reason |
|---|---|---|
| Editor A, EMBO Reports | Decline in present form; invite a presubmission enquiry for a rewritten essay | This is a master draft at twice the length and more than eleven times the reference limit. The publishable core (rationing, and damage that needs no misuse) is buried in ¶0.3 and §4c. |
| Referee 1 | Major revision | The rationing synthesis is a real contribution. But "legitimacy is irrelevant" claims too much, the rationing category is loose, and Box 2's test is weaker than claimed. |
| Referee 2 | Major revision | The reflexive design could be the essay's most distinctive feature, but so far it is announced rather than shown. §5 does not yet serve the argument, and citations carry too much of the prose. |

**The draft in numbers.** These are automated counts from the repository, made on 16 Oct 2026; the classifications are approximate.

- **Main text including boxes:** 6,773 words. The paragraphs tagged KEEP-3800 alone come to 5,164 words, so deleting the tagged cuts cannot produce a 3,500-word version.
- **References:** 173 entries, about 3,800 words. They include:
  - 29 arXiv preprints and 3 working papers;
  - about 9 news items or features, 10 blogs, 15 company, tracker or dataset pages and 16 policy or legal documents.

  About 40 entries still carry placeholder metadata ([initials to fill], [title to fill], or a title taken from a URL).
- **Citations and quotations:** about 250 in-text citations, roughly one every 27 words, and about 70 direct quotations.
- **Editorial markers in the main text and boxes:** 77 [RECHECK], about 30 [AUTHOR] slots (46 in the whole file) and 6 [CITATION NEEDED].
- **How the claims were read**, from the outline's claims register (174 claims):

  | Basis of the claim | Claims |
  |---|---|
  | Full text, including skims | 14 |
  | Partial text | 8 |
  | Abstract only | 68 |
  | Standfirst or title only | 4 |
  | Primary documents | 40 |
  | Summaries in earlier notes | 15 |
  | Search extracts | 8 |
  | Secondary reports only | 7 |
  | Memory | 1 |
  | Mixed | 9 |

  26 of the claims are from preprints, and 69 are marked for re-checking.
- **Process record:** 17 commits, from 21:34 UTC on 15 October to 00:58 UTC on 16 October 2026. That is about three and a half hours from the first literature notes to the complete draft. It does not cover work done before the first commit.
- **Sentences:** the median is 21 words; one sentence in ten runs to 47 words or more.

---

## Part 1. Editor A: EMBO Reports, Science & Society

### Overall assessment

The subject fits this section exactly: research assessment, peer review and funding under generative AI, argued by a working scientist at a European institute. The author also has an angle our readers have not seen in these pages, made of three parts:
- institutions have responded to cheap output by rationing it, not by changing what they count;
- the damage does not depend on misuse;
- the essay documents its own making.

But this is a master text, not an article for us. It is twice our length, carries more than eleven times our reference limit, is unfinished, and runs five arguments where our format carries one. By the time it is submitted, our readers will have met the premise in *Nature* (the editorial of 25 Mar 2026; Huang et al., 29 Sep 2026) and in *PLOS Biology* (Blekhman, 15 Oct 2026). The enquiry must therefore open with what is new, and what is new here is rationing.

**Desk decision.** Decline without review in present form. Encourage a presubmission enquiry, through eJP, for a rewritten Science & Society essay of at most 3,500 words and 15 references, along the lines below.

**Odds:** medium after such a rewrite, which matches the strategy file; low as the draft stands.

### Major issues

**E1. Format and completeness**
- **Location:** the whole manuscript.
- **Problem:** the manuscript runs to 6,773 words against our 3,500 and 173 references against our 15. It also carries:
  - Table 1 and three figures;
  - about 30 author slots;
  - 77 recheck flags;
  - about 40 incomplete references.

  The KEEP-3800 paragraphs alone come to 5,164 words.
- **Why it matters:** we cannot judge the EMBO version from the master. A version produced by deletion would keep the master's citation-led texture, which a 15-reference essay cannot carry.
- **Fix:** write the EMBO version fresh from the outline's assembly map (§1), using the structure under "What would make it publishable" below. Submit only when every marker in that version is resolved.

**E2. The opening does not say what is new**
- **Location:** the title, the standfirst, and ¶0.1–¶0.4.
- **Problem:** the 529-word introduction runs, in order, through:
  - the exhibit;
  - the shared premise, as four quotations in a single 67-word sentence;
  - four contributions, with rationing third;
  - the AI disclosure;
  - a roadmap.

  The essay's own claim arrives late, as one item in a list.
- **Why it matters:** readers of this section decide on the first paragraph. After Blekhman, "AI breaks the link between effort and merit" is not news to a biologist.
- **Fix:** open with the NIH cap, which most of our readers will have felt. State the rationing claim and the point that the damage needs no misuse. Put the exhibit in one sentence at the end of the paragraph. A possible opening (123 words):

  > In July 2025 the US National Institutes of Health reported that AI tools had let some investigators submit more than 40 applications in a single round, and it capped every investigator at six a year. arXiv now accepts two submissions a month per submitter; AI conferences cap submissions per author, and two of them set the cap by past success. These are the responses with teeth so far, and they share a design: they restore scarcity by decree and leave what is counted unchanged. I argue that this is the wrong repair, because the problem does not depend on misuse. This essay was itself drafted by AI agents under my direction in [X] hours (Box B), and nothing in its text shows that.

**E3. Life-science grounding, and precision about which layer is cheap**
- **Location:**
  - the standfirst ("makes papers … almost free to produce");
  - ¶2.2 (a freelancing platform) and ¶2.3 (ICLR reviews);
  - ¶2.6 (Suchak et al. filed under fraud);
  - ¶4a.2–¶4a.3 (LLM ideation; Kaggle);
  - ¶4c.2 and Table 1 (ICLR, AISTATS, ACL, TMLR, arXiv CS);
  - ¶5.4–¶5.5 (model trackers).
- **Problem 1: the examples come from computer science.** Most of the institutional and empirical detail comes from machine-learning venues and computer-science preprints.
- **Problem 2: the claim about cheapness is too broad for biologists.** Experimentalists will reject the standfirst's claim that AI makes papers "almost free to produce" at once: most of a wet-lab paper's cost is in the experiments. The essay already knows this; ¶6.2 says the essay "shows which layer has become cheap: the writing and synthesis". That insight belongs at the front.
- **Why it matters:** readers recognise an argument through examples from their own field. Biologists apply to NIH, the ERC and national agencies, post on bioRxiv and medRxiv, and review for journals, not for ICLR.
- **Fix:**
  - Say from the start that AI makes the *written* layer cheap. That layer is the whole of a grant application, a review or a review article, but only the text of an experimental paper.
  - Use Suchak et al. (2025, *PLOS Biology*) as the life-science case in which whole papers became cheap because the data were ready-made. The register records single-factor NHANES papers rising from about 4 a year (2014–21) to 190 in 2024. Move it out of the fraud paragraph: formulaic papers are not necessarily fraudulent, and the brief wants legitimate use to lead.
  - Lead with NIH, and use Kobak et al. (2025, PubMed) for how widespread use is.
  - Say whether bioRxiv and medRxiv have changed their rules, and how their volumes have moved. If nothing has changed, say that too.
  - Say what European funders and institutes (ERC, EMBO, national agencies) have and have not done. If they issued guidance but no cap, the contrast is informative. Audit: check the ERC's current AI guidance before describing it.
  - Keep one sentence on conference caps, chosen for the point that some are tiered by past success.

**E4. The exhibit must carry data and meet policy**
- **Location:** ¶0.1, ¶0.3b, Box 1, the AI-use statement and the CRediT statement.
- **Problem:**
  - Box 1 has no figures yet.
  - The AI-use statement leaves blank how the outputs were validated, which is the question publishers now ask.
  - The CRediT statement credits the author with "Writing – original draft", although the essay says the AI drafted.
- **Why it matters:** we can consider an essay drafted with AI and disclosed as such. Check EMBO Press's current AI policy; the strategy assumes Springer Nature's applies. We cannot consider one whose disclosure is incomplete or contradicts itself. Referees will check this first, because the essay invites it.
- **Fix:** see Referee 2, issues 1–3. In our version, Box B should run to at most 250 words and contain numbers.

**E5. A 15-reference essay must be carried by argument**
- **Location:** the whole manuscript.
- **Problem:**
  - Most of the master's paragraphs are a claim followed by several citations.
  - Several load-bearing facts rest on weak sources:
    - the conference caps, on a single *Nature* news story;
    - arXiv's one-year ban, on a secondary report (TechCrunch);
    - the frontier comparisons, on trackers dated 15 Oct 2026.
- **Fix:**
  - Choose 15 references that either carry a load-bearing fact or define the competition (suggested list in Synthesis §4).
  - Cut the tracker numbers.
  - For conference caps, cite each venue's own call, or keep the single news source and say so.

**E6. Overlap and disclosures**
- **Location:** the cover letter and the Data and process availability statement.
- **Problem:** a *Nature* Correspondence making the same two points (rationing and the test) is planned first, and a Zenodo preprint will follow.
- **Fix:**
  - Disclose both in the cover letter.
  - Confirm EMBO Press's preprint policy (audit).
  - State your field. "[AUTHOR: field]" is still empty, and readers of this section expect to know where the author stands.
  - Declare any EMBO roles.

### What would make it publishable here

1. **One argument:** "Rationing is not reform". The caps restore the scarcity of submissions but not the information that scarcity carried. The damage needs no misuse. Institutions should change what they count and read.
2. **A structure of about 3,000 words**, which leaves room for the author's own passages:

   | Part | Words | Content |
   |---|---|---|
   | Opening | ~200 | The E2 paragraph |
   | "The cost was the signal" | ~650 | The written layer and the three scarcities; information and congestion kept apart (Referee 1, issue 2); the gain for non-native writers; Suchak et al. as the life-science case |
   | "Rationing is not reform" | ~800 | A definition; whom the caps bind; tiering by past success; automated evaluation as a fourth response; why reform needs reading capacity |
   | "Will cheap output narrow science?" | ~450 | Huang et al.'s claim; Hao et al. and Zheng et al. in two sentences each; the three drivers in three sentences |
   | Box A: the test | ~200 | |
   | "What institutions can do" | ~400 | Count less and read more; documentation in place of disclosure; institutional accounts and open models; long-horizon funding |
   | Box B: how this essay was made | ~250 | With figures |

3. **Two personal elements, no more:** what AI changed for you as a non-native writer (¶2.2), and what you would change on a hiring or grant panel (¶6.1).
4. **Fifteen references** (Synthesis §4) and one figure (Figure 1). Table 1 moves to the Zenodo record.
5. **Register:** assertive about the institutional diagnosis, modest about narrowing.

### Minor issues

- **Standfirst:** it says "AI conferences cap authors"; they cap submissions per author.
- **Acronyms:** spell out ICLR and AISTATS at first use, or refer to them generically ("two large AI conferences").
- **Jargon:** define "triple difference" in one clause for biologists. Drop "knowledge extent", "affordance" and "natural-monopoly-like" from our version.
- **Heading:** "The trajectory we're actually on" is too informal for a heading here.
- **Limits to check:**
  - whether boxes count towards our 3,500 words (the outline assumes they do);
  - whether a data-availability link can sit outside the reference count. If it can, the Zenodo record frees a reference slot.

### Line-level notes on the opening and frame

- **Title:** "Even good use breaks it". "It" has no referent until the subtitle, and "breaks" claims more than the evidence shows. See Synthesis §5.
- **Standfirst, sentence 1:** "Generative AI makes papers, reviews and grant applications almost free to produce, and it does so when it is used well, not only when it is abused."
  - The second half is the essay's best hook; keep it.
  - "Almost free" is defensible for grant applications and reviews, which are text only, but not for experimental papers (E3). Write: "makes the writing of papers, grant applications and reviews cheap".
- **¶0.2:** "Much of this is shared ground, stated early (Carrigan 2023; Kingsley 2023) and more forcefully since: publish-or-perish is being 'completed, and thereby destroyed' by large language models … and 'paper counts are meaningless' (Blekhman 2026)."
  - Four quotations in one sentence read as a citation list. Paraphrase:

    > Much of this is shared ground: since 2023, commentators have argued that cheap AI output completes and so destroys publish-or-perish (Manabu 2026), that polish no longer indicates merit (Hansen 2026) and that paper counts have become meaningless (Blekhman 2026).

- **¶0.3:** "What I add is narrower." Keep it; the tone is right. In our version, list rationing first.

---

## Part 2. Referee 1: metascience and research evaluation

### Overall assessment

The essay is better informed, and more candid about its evidence, than most opinion pieces in this crowded field:
- it marks its preprints;
- it gives the contrary evidence a full hearing (¶4a.4);
- it concedes the tail objection (¶2.6b).

Its reading of the 2025–26 caps as rationing is a genuine synthesis, and relevant to policy.

My concerns are about rigour at exactly the points where the essay claims its contributions:
- "Legitimacy is irrelevant" runs two mechanisms together and claims more than the evidence shows.
- The rationing category lumps caps, gates and a sanction together, and the essay never shows whom the caps actually bind.
- Box 2's test does not yet discriminate, and its falsification clause contradicts ¶4a.4.
- The reform movements are treated as a foil when they are the essay's natural allies.
- Too many interpretive claims about the key papers rest on their abstracts.

None of this is fatal. A referee at EMBO Reports, PLOS Biology or Minerva would raise all of it.

The author's stated position as an outsider to metascience is honest. It also raises the bar for Box 2, which proposes a method that specialists will judge on its merits.

### Major issues

**R1-1. Novelty against the closest work is under-specified, and overstated in two places**

**Location:** standfirst; ¶0.3; ¶1.3; ¶4b.1; ¶4c.3; Box 1 (Precedents).

**Hansen 2026** (*RIPR*; read in full)
- **What it already says:**
  - symbolic scarcity, the prestige produced by rejection, is "not epistemically necessary";
  - "surface quality no longer reliably indicates epistemic merit";
  - "the scarcity of interpretive attention";
  - it proposes tiered publishing, tiered review, reviewer pay and **AI screening at inclusion**.
- **What the essay adds:** the scarcity AI removed is a scarcity of costly *inputs*, not a symbolic one; abolishing symbolic scarcity still leaves cheap output to be evaluated.
- **Verdict and fix:**
  - The distinction holds and is useful, but the essay states it twice, almost word for word (¶1.3 and ¶4c.3). Keep one.
  - Acknowledge that Hansen's "surface quality" sentence is the signal argument in brief.
  - Engage his AI-screening proposal. It is the response the essay leaves out (R1-3e).

**Manabu 2026** (*PSE*; abstract and reference list only)
- **What it already says:** publish-or-perish is "completed, and thereby destroyed"; "the apprenticeship pathway … is being severed"; it proposes a "postdigital scholarly commons". It was drafted with Perplexity.
- **What the essay adds:** the split between legitimate use and misuse; rationing; the test; the two drivers.
- **Verdict and fix:**
  - **You cannot claim to differ from a paper whose body you have not read.** Three quotations come from its abstract.
  - Read the PDF through EMBL or UPF before any submission.
  - If the body discusses caps or legitimate use, revise ¶0.3.

**Blekhman 2026** (*PLOS Biology*; read in full)
- **What it already says:** effort "served as evidence"; "paper counts are meaningless"; a predicted fallback to "older, cruder proxies"; AI firms "selling the tokens".
- **What the essay adds:**
  - rationing as a second fallback, already under way;
  - legitimate use, where Blekhman frames the problem as papers made without research;
  - the test.
- **Verdict and fix:**
  - The difference is clear. But Blekhman's own proposal, to abandon the incentive system and acknowledge that counts are meaningless, is cited without being engaged. Say whether you agree.
  - The PLOS Biology route depends on that answer.

**Huang et al. 2026** (*Nature* Comment; read to about two-thirds)
- **What it already says:**
  - the hypothesis, "almost word for word";
  - "not technological, but institutional";
  - the data channel ("100-fold");
  - its remedies: data infrastructure, an end to pivot penalties, and a third recommendation not yet seen.
- **What the essay adds:** only the discriminating test, and naming the rival mechanism explicitly.
- **Verdict and fix:**
  - Read the Comment in full. The "which lever" framing (¶4b.3) and the Correspondence depend on the third recommendation.
  - Delete "I reached it independently" (¶4b.1). The process record begins on 15 Oct 2026, after Huang et al. appeared (29 Sep), so it cannot support a claim of priority (Referee 2, issue 2).

**Fourie 2026** (arXiv; skimmed in full)
- **What it already says:**
  - review is "rationed, not priced";
  - rationing by capacity lowers the stamp's value;
  - the argument extends to "grant panels, hiring committees, accreditation bodies";
  - it was written with Claude Code and Codex.
- **What the essay adds:**
  - rationing applied to *per-author quotas* at NIH, arXiv and conferences;
  - the claim that caps restore scarcity but not information;
  - tiering by past success.
- **Verdict and fix:**
  - Fourie already generalises beyond journals, so "extending Fourie" must say how.
  - Fourie rations evaluators' *attention*; per-author quotas ration *access* to evaluation. Say so in one sentence.

**Also in the notes, but not cited:**
- **Hanneke et al. 2026** (*BISE*) name "three limited resources: editorial attention, reviewer time, and audience attention". That is close to the essay's three scarcities, and a bare "cf." undersells it.
  - Make the difference explicit. The essay's scarcities sit on the *production* side and served as signals; Hanneke's sit on the *evaluation* side and are capacities.
  - That difference is the real novelty of contribution 1.
- **Adeyeye 2026** (SSRN) applies Spence's signalling theory to the publication signal, which "worked precisely because producing it convincingly has been costly". It is the nearest competitor on the cost-as-signal framing; cite it and say how the essay differs.
- **Hakobyan 2026** models reviewer effort collapsing once AI enters both sides of review.
- **Nee, Zhong & Ni 2026** give the best counterfactual evidence on submission volume (R1-4e).

**Missing from the brief's positioning list:** the brief says the paper must cite and set itself apart from the 2026 *Nature* pieces by Messeri & Crockett, Braun, Hutchinson and Motoki. The draft cites Braun only.
- Messeri & Crockett's 2026 Comment is in the outline (master only) but not in the draft.
- Hutchinson's Correspondence is directly relevant to Box 1 (Referee 2, issue 2).

**Why it matters:** a metascience referee will check each contribution against these works first. "Narrower" is the right register, but the claims are not yet precise enough.

**Fix:** rewrite ¶0.3 so that each contribution names its closest precedent and the exact increment over it. For contribution 1:

> First, I locate the failure on the production side of evaluation. Hanneke et al. (2026) name the scarce resources of evaluation (editorial attention, reviewer time, audience attention); I argue that three costs of *producing* outputs (writing effort, an expert's review time and years in a literature) also served as signals of merit, and that honest use lowers all three.

**R1-2. "Legitimacy is irrelevant to the mechanism" merges two mechanisms and claims more than the evidence supports**

**Location:**
- the standfirst and the title;
- ¶0.3 ("First");
- ¶2.5 ("judgement remains scarce");
- ¶2.6b ("no one has shown that ordinary use alone would overload a gate");
- ¶2.7 ("With all three scarcities gone, the system cannot read merit from what it counts"; "no level of legitimate use restores the signal").

**Problem (a): two mechanisms run as one.** The essay runs an *information* mechanism (costly outputs revealed the inputs behind them) and a *congestion* mechanism (cheap outputs overload fixed gates) as a single claim.
- **For information,** the claim is close to true by construction: cheaper production weakens what an output reveals, disclosed or not.
- **For congestion,** the claim needs ordinary, honest users to raise volume enough to overload the gates. ¶2.6b concedes that nobody has shown this, and adds that "if the tail carried the whole load, targeted sanctions would be the better tool".
- **The result:** the standfirst and ¶0.3 claim legitimacy-irrelevance for both mechanisms, while the rationing section rests on congestion.

**Problem (b): only differential cost carries information.** A signal separates strong from weak producers only insofar as its cost *differs* between them. The essay itself quotes "require differential knowledge and effort" (¶1.3, Cowgill et al.).
- If AI lowered everyone's cost in proportion, rankings would survive, and the signal would become noisier rather than disappear.
- The evidence cited supports "degraded", not "gone":
  - Cowgill et al. find a 4–9% loss in screening accuracy;
  - Kusumegi et al. find that the relation between writing complexity and quality reversed.
- Neither shows that merit can no longer be read.

**Problem (c): "gone" contradicts "invisible".** ¶2.5 says, rightly, that "judgement remains scarce" but "is now invisible in the text". ¶2.7 then says that "all three scarcities [are] gone".

**Why it matters:** this is the first contribution and the hinge of the thesis. A sceptical referee will test it first.

**Fix:** state two claims of different strength.
- **The information claim, firmly,** but on the condition that AI narrows the *differences* in cost. That condition is plausible for prose and synthesis, where AI helps weaker producers more.
- **The congestion claim, conditionally.**

Replacement for the opening of ¶2.7 (about 150 words):

> With all three costs lowered, what the system counts reveals less about the work behind it, whoever answers for the output. The claim is narrower than it sounds. The signals are not gone: judgement and mastery remain scarce, and some writers still write better than others. But AI narrows the cost differences on which the signals relied, so a fluent paper, a competent review or a well-cited synthesis no longer separates those who did the work from those who did less of it (Cowgill et al. 2026). That holds whether or not the use is disclosed, which is why the remedies on offer do not reach it. Gartenberg et al. (2026) decline to say what level of AI use is appropriate; my point is that no rule about appropriate use restores the signal. Whether honest use also overloads the gates is a separate, empirical question (¶2.6b).

In the standfirst, change "legitimacy is irrelevant to the mechanism" to "the damage to the signals does not depend on misuse".

**R1-3. Rationing is the cleanest contribution, but the category is loose and its scope unmeasured**

**Location:** ¶2.4 ("the cap binds every investigator"); ¶2.6b; ¶4c.2; ¶4c.3; ¶4c.5; Table 1 (title and caption); standfirst; Figure 1c.

**Problems:**

- **(a) "Binds" is ambiguous.** A cap *applies* to everyone but *binds* only those who would otherwise exceed it.
  - NIH's six applications a year and arXiv's two submissions a month (24 a year) sit far above what most researchers submit; arXiv itself blames "a relatively small proportion of authors".
  - The essay shows neither that these caps cut total volume much nor that they constrain ordinary researchers.
  - Audit: does NIH report the share of PIs above six applications a year? Does arXiv report the share of submitters above two a month?
  - The tiered caps at ICLR and AISTATS are the exception: they do bind ordinary newcomers.
- **(b) Table 1 mixes different kinds of measure:**
  - volume caps (NIH, arXiv's monthly limit, SocArXiv, conference quotas);
  - a *gate*: arXiv's requirement that computer-science reviews and position papers pass peer review first is a certification rule, not a limit on quantity;
  - a *sanction*: arXiv's one-year ban for unchecked LLM output targets misuse, so it cuts against the essay's own framing. It is also sourced to TechCrunch only, and its scope is unknown;
  - tiered caps, which combine rationing with past success.
- **(c) Rationing is older than the essay implies.**
  - Table 1's caption says "No such measure was found before 2025", yet its title covers 2023–2026.
  - Funders have long limited applications. Audit: the ERC's resubmission restrictions; NSF's per-PI limits in some programmes.
  - I believe some AI conferences capped submissions per author before ChatGPT. Audit: IJCAI, from about 2020; CVPR, possibly from 2025.
- **(d) A cap restores some information.** ¶4c.2 says "The information that scarcity carried does not return". In part it does: an author limited to six applications reveals which six she thinks best.
  - Market design uses scarce signals in exactly this way. Audit: Coles, Kushnir & Niederle (2013) on preference signalling; the AEA job-market signalling service.
  - What a cap cannot restore is what costly production revealed *across* authors.
- **(e) A fourth response is missing.** ¶4c.3 sets rationing against pricing and redesign. It omits the response institutions are most likely to adopt: automated evaluation, meaning AI triage, AI-assisted review and screening at inclusion. Others already propose or model it:
  - Hansen proposes screening at inclusion;
  - Bhargava et al. (2026, *Management Science*; in the notes) propose LLMs as front-line reviewers;
  - Xuegong Zhang (2026, *Nature*) argues for "AI support, not AI bans";
  - Hakobyan models it.
- **(f) Those who ration are mostly not those who count.**
  - arXiv and conference committees cannot change what hiring panels count.
  - Universities, funders and assessment agencies can, and most have neither rationed nor reformed.
  - NIH is the only institution in Table 1 that does both jobs. Audit: whether NIH introduced a simplified review framework for applications due from January 2025. If it did, "leaving what is counted unchanged" needs qualifying for NIH, although that change was not a response to AI.

**Why it matters:** the outline calls this the essay's cleanest contribution. A referee who shows that the category lumps a sanction in with a gate, and that most of the caps bind only the tail, will reduce it to "some institutions introduced caps".

**Fixes:**

1. **Define rationing** at the start of ¶4c.2:

   > By rationing I mean a limit on how many items a person may submit in a period, applied whatever the quality of the work or the conduct of its author. NIH's six applications a year, arXiv's two submissions a month and the per-author quotas of AI conferences are rationing in this sense; arXiv's peer-review requirement for computer-science reviews is a gate, and its reported one-year ban for unchecked LLM output is a sanction.

   Add a "Type" column to Table 1 and drop the sanction from the rationing count.
2. **Say whom the caps bind, and why they still matter:**

   > Most of these caps sit far above what typical researchers submit [audit: shares above each cap], so for now they bind the tail. Their significance is what they reveal: faced with cheap output, institutions reached first for quantity limits, not for changes in what they count.

3. **Add the precedents,** and correct the caption and title of Table 1:

   > Rationing is not new: funders have long limited applications [audit], and some conferences capped submissions per author before ChatGPT [audit]. What is new is the trigger, the reach (preprint servers now ration too) and the tiering by past success.

4. **Replace the information sentence in ¶4c.2:**

   > A cap restores the scarcity of submissions, and with it a little information: an author limited to six applications reveals which six she thinks best. It cannot restore what costly production revealed across authors, and what is counted stays the same. Where caps are tiered by past acceptances (ICLR 2027; AISTATS 2027), they fuse rationing with the fallback Blekhman predicts: past counted success decides who may be counted again, a Matthew effect written into the rules (Merton 1968).

5. **Add the fourth response to ¶4c.3** (about 100 words):

   > There is a fourth answer, and it is the one institutions are most likely to reach for: automate the reading. Publishers already screen submissions with software, reviewers use AI to draft reports (Section 2), and proposals to put language models at the front line of review are circulating (Hansen 2026; Bhargava et al. 2026). If AI cheapens evaluation as fast as production, volume becomes manageable; but a judgement that a model makes about text a model helped write measures what models find plausible, not what a community has judged. Automated triage can sort for integrity and fit; it cannot supply the judgement whose scarcity the caps conceal.

6. **Make the point about who rations and who counts:**

   > The institutions that ration and the institutions that count are mostly different, and the caps relieve the pressure on the second without changing what they do.

**R1-4. The evidence is handled carefully for Hao et al., less carefully elsewhere**

**Location:** ¶2.1, ¶2.2, ¶2.6b, ¶3.4, ¶4a.1–¶4a.5, ¶4b.2, Box 2.

**(a) Hao et al.** The three cautions in ¶4a.1 are exemplary.
- **¶3.4 drops them.** It restates the headline without the cautions, and in words that suggest generative AI: "AI, as scientists use it, contracts the focus of science". Replace with:

  > The same group finds that AI used as a research method has so far concentrated in data-rich, established areas (Hao et al. 2026).

- **"Times more":** write "3.02 times as many papers", not "3.02 times more papers".
- **Audit:** the data-availability analysis comes from arXiv v4; check it against the final Methods.

**(b) The §4 heading promises a finding the section withholds.**
- "What AI is actually doing" leads up to ¶4a.5's honest verdict: "Whether AI narrows science overall is not established".
- The roadmap in ¶0.4 claims more: "Sections 4 and 5 explain why it is not doing so".
- **Fix:** retitle §4 "Is AI narrowing science? Evidence, a hypothesis and a test". Change the roadmap to "Sections 4 and 5 ask whether it is doing so, and what stands in the way".

**(c) Kusumegi et al.** The register says this paper was read from the abstract only, and that the breakdown by author background was not verified. Read the full text, and audit three points:
- **The range.** What does "23.7–89.3%" span: platforms, author groups? If it reflects variation across groups, say so: "by between 23.7% and 89.3%, depending on [platform and author group]".
- **The wording.** Check "reversed the relationship between writing complexity and paper quality" against the paper.
- **The quality proxy.** Which proxy was used (later journal publication?) limits what "prose stops indicating quality" can mean.

**(d) Prevalence measured by detectors.** "These estimates rest on detectors that … mostly capture polishing, which is the point" (¶2.1) is an inference that no source supports. Detectors measure style, not purpose.
- **Audit:** do Kobak et al. or Liang et al. say that the use they detect is mostly polishing?
- **If not, write:**

  > These estimates rest on detectors that misfire on non-native English writers (Liang et al. 2023) and measure style, not purpose: they cannot tell polishing from generation. What they establish is that use is common, and much of it, such as language editing, is permitted under publishers' rules [audit: current Springer Nature and Elsevier wording].

**(e) The distribution shift in ¶2.6b.**
- **The argument:** cheap output shifts the whole distribution, and the tail merely shows it first.
- **The evidence offered cannot support it.** That arXiv's monthly total doubled between 2024 and 2026 does not distinguish a shift of the whole distribution from a growing tail, and arXiv's own diagnosis points to the tail.
- **Better evidence:**
  - Cite Nee, Zhong & Ni (2026, in note G6). arXiv mathematics in 2026 ran 11.9% above a synthetic counterfactual, and the share of authors with five or more submissions rose from 2.45% to 3.80%.
  - Better still, replace the optional Figure 3 (monthly totals) with per-author percentiles: the median, 90th and 99th percentile of submissions per author per year, 2016–2026. That would answer the outline's weakness 1 directly. If the Registered Report goes ahead, declare these data, as the draft already notes.
- **Audit:** when the 1 Oct 2026 cap was announced. If it was announced before September, the September 2026 count may include submissions made ahead of the cap, and a 12-month average is the safer comparison.

**(f) Zheng et al.**
- **The problem:** the reconciliation in ¶4a.4 ("each moves further from their own past work while the diversity of the system falls") is clever, but as written nothing could falsify it.
- **The fix:** turn it into a prediction in Box 2. Among AI adopters who move into new fields, the fields they enter should be more concentrated than those entered by non-adopters who move (for example, a higher Herfindahl index).
- **Read the full text.** The register records the abstract only.

**(g) Preprints are treated asymmetrically.**
- ¶2.2 counts Galdin & Silbert, a preprint, among the "cleaner designs", while calling Kusumegi "disputed" on the strength of another preprint.
- Lead with Cowgill et al., which is experimental and peer-reviewed.
- Describe Galdin & Silbert as quasi-experimental, and mark it as a preprint in the reference list rather than in the sentence.

**R1-5. Box 2's test does not yet discriminate, and its falsification clause contradicts ¶4a.4**

**Location:** Box 2 (all four paragraphs); ¶4b.3; ¶0.3 ("Second"); the standfirst.

**Problems:**
- **(a) A moderator that the treatment changes.** The career-stage proxy (before or after a first last-author paper) is itself affected by AI use: Hao et al. find that AI users become project leaders 1.37 years earlier. Moving to last authorship also changes a scientist's topics for reasons unrelated to incentives, such as supervising more varied projects or changing labs.
- **(b) Language confounds the country comparison.** Regimes that count publications are common in countries where English is not the first language, and AI's gains are largest for non-native writers (Kusumegi et al.; Filimonovic et al.; Zheng et al.). A triple difference across countries would pick up a language effect.
- **(c) "Data availability measured and interacted" is undefined.** Say how you would measure it at the level of the topic.
- **(d) Wrong level.** The hypothesis is now stated as one "about the system" (¶4a.5), but the design compares authors with themselves. Of the three measures in Box 2, only "the diversity of the whole system" operates at the level of the hypothesis, and the triple difference does not use it.
- **(e) The falsification clause contradicts the essay.** "It is weakened if AI users move further from their earlier work than comparable non-users" conflicts with ¶4a.4, which argues that individuals moving further is *compatible* with narrowing across the system.
- **(f) The treatment is mismeasured.** Detector-based "intensity of AI use" captures help with writing. The hypothesis is about AI used to do research faster.
- **(g) Power.** No minimum detectable effect is given for the triple interaction. A null result on an interaction term is weak evidence unless the study is powered for it.

**Why it matters:** Box 2 is contribution 2, and it is the essay's main claim to originality on narrowing; note G6 says "the test is new". If the test cannot discriminate, the contribution shrinks to "someone should study this".

**Fix:**
- **Claim less.** Call the test "discriminating under stated assumptions".
- **Change the sources of incentive variation.** Make dated changes in *what is counted* the main source of variation in incentives. Keep career stage only as a secondary source, flagged as possibly affected by AI use.
- **Use CoARA within a country.** Within one country and field, compare CoARA signatories that have dated action plans with institutions that have not signed. This also ties the test to the reform movement (R1-6); handle selection into signing.
- **Measure use from disclosures.** Where they exist, use AI-use disclosure statements, which many journals now require, rather than detectors alone. Mohapatra & Pruthi analysed those for ICLR 2026 and EMNLP 2025 (note G3).
- **Add the prediction about where movers land** (R1-4f).
- **State a minimum detectable effect.**
- **Commit or offer.** Given the outsider stance, either commit to running the test (with a scientometrics collaborator, as the strategy suggests) or offer it plainly to the field. A half-commitment ("I plan to") draws the most scrutiny for the least credit.
- **Replace the falsification paragraph with:**

  > The hypothesis can fail in three ways. It fails at the level of the system if the fields AI adopters enter are no more concentrated than those non-adopters enter, so that individual moves (Zheng et al. 2026) add up to wider, not narrower, coverage. It fails as an incentive explanation if, within fields and with data availability held fixed, the link between AI use and exploitation does not grow with incentive intensity in a sample powered to detect [pre-specified effect]. And it is confounded if the effect tracks data availability rather than incentives. The data are open (OpenAlex; Semantic Scholar). [I will preregister the analysis before accessing the data / I offer this design to the field.]

**R1-6. The reform movements are treated as a foil; they are the essay's allies**

**Location:** ¶4c.1; ¶4c.4 (last sentence); ¶4c.5; ¶6.1.

**Problem:**
- **(a) The essay's own remedy is the reform agenda.** ¶6.1's first proposal, "count less and read more", is the programme of DORA and CoARA: qualitative judgement, with peer review at its centre and responsible metrics in support.
  - Calling reform "voluntary and uneven" and "not designed for machine-scale output" misses the point. Reading a few chosen outputs withstands cheap production better than counting does.
  - AI vindicates the reform agenda.
- **(b) The best idea is in a paragraph cut from every short version.** The last sentence of ¶4c.4 reads: "without capacity for qualitative judgement, discretion migrates to gatekeepers, and AI-era volume consumes exactly that capacity". This is the real difficulty: reform depends on the very resource that AI-era volume uses up.
- **(c) The bibliometric counter-argument goes unanswered.** Abramo (2024), cited only in passing, argues that assessment centred on peer review is unsound. AI may make metrics and automated assessment *more* attractive to evaluators short of money and time, not less; Blekhman's predicted fallback is one version of this risk. Name it.
- **(d) Some examples are in the wrong category or imprecise:**
  - Registered Reports (Scheel et al.) reform publishing, not research assessment; drop them from ¶4c.1.
  - "600 to more than 830 signatories, depending on the source" needs one dated figure from CoARA's own site (audit).
  - Curry (2018) is old evidence for a claim about 2026. The European Commission study of 2026 is the right source; keep it.

**Why it matters:** many readers of this section work on DORA and CoARA. Audit: check whether EMBL or EMBO have signed either; if so, say so. An essay that sounds dismissive of reform loses its natural allies and misdescribes its own proposal.

**Fix:** replace ¶4c.1 and the opening of ¶4c.5 with something like this (about 120 words):

> Reform that changes what is counted exists, and AI strengthens its case. DORA (2012) and CoARA (2022) ask evaluators to read a researcher's work rather than count it, and some institutions have done so (Woolston 2021); progress is "broad and increasing" but "uneven" (European Commission 2026). Reading a few chosen outputs withstands cheap production in a way that counting does not: a panel that reads three papers is not swamped when output doubles. But reform depends on the resource that AI-era volume consumes, expert attention, and where that capacity is missing, discretion moves to whoever holds the gate. The caps of 2025–26 do not touch this. By keeping counts meaningful a little longer, they lower the pressure to stop counting.

**R1-7. Too much rests on preprints, news and abstracts**

**Location:** throughout.
- Of the 173 references, 29 are arXiv preprints and 3 are working papers.
- In the claims register, 26 claims are from preprints, and 68 of the 174 claims rest on abstracts only.

**Problem:**
- In a fast-moving field, preprints are unavoidable. What matters is which claims carry the argument, and whether the essay applies its own standard ("I state how strong the evidence is") evenly.
- Several interpretive claims about the essay's key interlocutors rest on abstracts or on partial reading.
- ¶4a.2 piles four preprints on LLM ideation (Si 2024 and 2025; Bao 2026; Liu 2026) into a paragraph the argument does not need. Liu et al. was posted on 12 Oct 2026, four days before the draft.

**Fix:** audit the load-bearing claims before any submission.

| Load-bearing claim | Where | Current support | Action |
|---|---|---|---|
| NIH capped applications because AI enabled 40 or more in a round | ¶2.4, ¶4c.2 | NIH notice (primary) | Keep; add the share of PIs affected (audit) |
| arXiv's monthly cap; September 2026 volume | ¶2.6b, ¶4c.2 | arXiv blog (primary) | Keep; check when the cap was announced (R1-4e) |
| Conference quotas (ICLR, AISTATS, ACL, TMLR) | ¶4c.2, Table 1 | One *Nature* news story | Check each venue's own call, or write "reported by" |
| arXiv's one-year ban | ¶4c.2, Table 1 | TechCrunch only; scope unknown | Take it out of the rationing list; keep it only as "reported", or cut it |
| Honest use erodes the writing signal | ¶2.2 | Kusumegi (*Science*; abstract only; disputed); Galdin & Silbert (preprint); Cowgill (peer-reviewed) | Read Kusumegi in full; lead with Cowgill |
| Reviews no longer certify an expert's time | ¶2.3 | Latona, Shen & Wang (preprints); Liang 2024 (conference paper) | Keep, but say these are machine-learning venues |
| Time spent mastering a literature worked as a gatekeeping signal | ¶2.5 | Conceptual; Manabu (abstract); arXiv's computer-science rule | Label it as conceptual; add evidence that syntheses were commissioned from recognised experts, e.g. invitation-only review journals (audit) |
| AI concentrates where data are rich | ¶4a.1, ¶4b.2 | Hao (*Nature*; Methods taken from arXiv v4) | Keep; check against the final Methods |
| Individual exploration is rising | ¶4a.4 | Zheng (preprint; abstract only) | Read in full; keep |
| Others now share the hypothesis | ¶4b.1 | Huang (partly read) | Read in full |
| Review is "rationed, not priced" | ¶4c.3 | Fourie (preprint; skimmed) | Acceptable as a conceptual source |
| The premise is shared (Manabu) | ¶0.2, ¶2.5 | Abstract only | Read the body |

Two further changes:
- Move the "preprint" labels from the running text into the reference list. This saves about 80 words.
- In the EMBO version, keep no more than three preprints among the 15 references.

### Minor issues

1. **¶1.1, Quan et al. 2017.** The draft says "Chinese universities paid up to US$165,000 per Web of Science paper". Audit: I believe the maximum was paid for a single *Nature* or *Science* paper, and that typical rewards were far lower. If so, write "paid cash for Web of Science papers, up to US$165,000 for one in *Nature* or *Science*".
2. **¶1.1, Butler 2003.** This finding is contested. Audit: van den Besselaar, Heyman & Sandström (2017, *Journal of Informetrics*) re-analysed the Australian case, and Butler replied. The draft cites Park et al. together with their critics; do the same here, or drop Butler.
3. **¶1.1, Fanelli 2018.** Audit: is "mistaken" Fanelli's own word?
4. **¶1.2, Hanson et al. 2024.** "Outpacing the growth in practising scientists": the register says the workforce figures were not re-extracted (audit).
5. **¶2.3, Thakkar et al.** The draft says "AI can also improve reviews", but Thakkar et al. report that 27% of reviewers *updated* their reviews. Audit whether they measured improvement; if not, write "change".
6. **¶2.4, NIH.** "The originality rule rests on detectors": audit whether NIH's notice says it will use detection technology.
7. **¶2.5, arXiv's rule.** It shows that outputs shaped like syntheses have become cheap, not that mastery has. Say so; this is the essay's own point ("Summarising is not mastery").
8. **¶4b.1.** "The mechanism is well founded" claims too much. The evidence shows a bias against novelty in short-window metrics and in panels; it does not show that AI is channelled by that bias. Write "The mechanism has good support".
9. **¶4c.3, Shah.** Shah's "fairer quotas" improve rationing rather than replace it. Move the citation.
10. **¶4c.3, pricing.** "Pricing has its own cost, by my inference rather than any finding: fees weigh most on the poorest researchers." There is published evidence on article-processing charges and authors' geography (audit; cite one study), so the hedge is unnecessary.
11. **¶4c.5, scope.** "None changes what is counted in response to cheap output" is too broad. NIH's originality rule changes eligibility, and ICLR's rule changes who may review. Write "none changes how researchers are counted for hiring, promotion or funding".
12. **¶4c.5, lock-in.** "The window to change what is counted is now" rests on two conference caps. Either show the lock-in or soften the claim (see the line notes).
13. **"By decree".** The phrase suits a funder or a state. For arXiv and conferences, "by rule" is more accurate; Table 1's caption already uses it. Keep "scarcity by decree" as the essay's phrase if you like it, but define it once.
14. **Box 1, Herbert et al.** "For comparison, one Australian grant proposal took 34 working days" sets a grant proposal against an essay, which cannot be compared. Drop the comparison, or compare with your own estimate of the time it would take to write this essay unaided, labelled as an estimate.
15. **Table 1.** The title covers "2023–2026", but the caption says no measure was found before 2025 (R1-3c).

### Line-level notes on precision

- **¶2.7.** "With all three scarcities gone, the system cannot read merit from what it counts, whoever answers for the output." Replace with:

  > With all three costs lowered, what the system counts reveals less about the work behind it, whoever answers for the output.

- **¶2.7.** "my point is that no level of legitimate use restores the signal" should read:

  > my point is that no rule about legitimate use restores the signal

- **¶2.4.** "Forty applications in a round looks like abuse, but the cap binds every investigator." Replace with:

  > Forty applications in a round looks like abuse, and the cap is set where only such outliers reach it; what makes it rationing rather than a sanction is that it applies to every investigator, whatever their conduct.

- **¶4c.2.** "The binding responses to AI-era volume have been caps (Table 1)." Replace with:

  > The responses with teeth have been caps (Table 1).

- **¶4c.2.** "Yet a cap restores only the scarcity of submissions. The information that scarcity carried does not return, and what is counted stays the same." Replace with the wording in R1-3, fix 4.
- **¶4c.5.** "None changes what is counted in response to cheap output, so the default is a fallback." Replace with:

  > None of them changes how researchers are counted, so evaluation falls back on what it already has.

- **¶4c.5.** "but caps keyed to past acceptances lock in incumbents, so the window to change what is counted is now." Replace with:

  > and the longer caps keyed to past acceptances stay in place, the more they favour the incumbents whose agreement any change would need.

- **¶4b.1.** "I reached it independently, but it is now shared. Huang et al. (2026) state it almost word for word" should read:

  > Huang et al. (2026) state it almost word for word

- **¶4a.1.** "The largest study finds individual gains and collective contraction, for a narrower kind of AI, and with a narrower design, than its headlines suggest." Replace with:

  > The largest study finds individual gains and collective contraction, but for AI used as a research method, and by comparing papers rather than following scientists.

- **Box 2.** "A discriminating test is a triple difference." Replace with:

  > A triple difference could discriminate between the two, under the assumptions stated below.

- **Standfirst.** "propose a test that discriminates between incentives and the pull of data-rich problems" should read:

  > propose a test that could tell incentives from the pull of data-rich problems

---

## Part 3. Referee 2: STS and philosophy of science

### Overall assessment

This is an intelligent, self-aware essay. In a field where the premise is now common, its decision to be its own example is the most original thing about it. But the reflexive design is so far *announced* rather than *shown*:
- the figures that would make it evidence do not exist yet;
- the contribution statement repeats the conventional disclaimer, in which the author set the judgements and the AI did the rest, that the essay itself calls unreadable;
- the CRediT statement contradicts the AI-use statement.

§3 is disciplined rather than utopian, but it is not yet tied to the essay's thesis about evaluation.

§5 is the weakest section:
- it is long, and full of numbers that will date within weeks;
- it joins two different issues, the concentration of the tools and chat data, under the heading of narrowing, and then disclaims the link.

The two-driver frame is a useful taxonomy, but its categories do not line up with the essay's own rival explanation, affordance.

Sentence by sentence, the prose is clear. But citations and quotations carry it, and its recognisable rhythm (paragraph-final maxims, "X, not Y") will strike some readers as machine-made. In an essay about whether effort can be read from a text, that matters.

### Major issues

**R2-1. The exhibit: currently closer to a device than to an argument**

**Location:** ¶0.1, ¶0.3b, ¶2.1 (last two sentences), ¶2.7 (last sentence), ¶6.2, Box 1 and the AI-use statement.

**Problem:**
- **(a) No data yet.** The exhibit's evidential value depends on figures that do not exist. The draft's fallback ("if the figures are unremarkable, cut this sentence") is prudent, but it would remove the one datum that is specific to AI.
- **(b) It is unclear what the exhibit is evidence of.** The essay makes three claims about itself:
  - Its effort cannot be read from the text. This was always true: evaluation never read effort directly; it inferred effort from the output.
  - It is one more countable item. This is true of any paper.
  - It was cheap. This is still pending.

  Only the third claim depends on AI. The repository suggests it may be striking: the visible commits span about three and a half hours, from the first literature notes to the complete draft. That span covers only the machine phase. Work done before the first commit, such as the bibliography in `reports/`, is not included.
- **(c) The exhibit is not linked to the remedy it prototypes.** ¶6.1 proposes "documentation of how the work was done in place of bare disclosure (Cwik 2026)". The process record *is* that documentation: it is a small test of one remedy. It also shows that remedy's limit: someone has to read the record, and reading is now the scarce resource. The essay never says this. That is a missed argument, not just a missed flourish.
- **(d) The self-imposed cap contradicts the thesis.** In ¶6.2 the author offers "a self-imposed cap": "one Correspondence, this essay and its preprint, and nothing more". That is rationing, which the essay argues does not restore the signal. The response consistent with the thesis is the optional pledge not to count the essay in formal evaluation, because that changes what is counted.

**Why it matters:** done well, the exhibit is what sets this essay apart from Fourie's footnote and Manabu's acknowledgement. Done as now, readers sceptical of AI will read it as a gimmick, and everything else as a confession.

**Fix:**
- **Report the numbers,** split into the agent phase and the author phase: hours, days, sessions, cost and commits.
  - Define what the record covers: which sessions count, and whether the earlier bibliography is included.
  - Never claim "one evening" unless the record shows it.
- **Report the depth of reading.** The register's tally (14 of 174 claims from full text; 68 from abstracts) is the thesis in miniature: a fluent text whose polish hides how its sources were read. Update the tally after the audit and report it.
- **Add to Box 1:**

  > The record that accompanies this essay is a small test of one remedy discussed in Section 6, documentation in place of disclosure (Cwik 2026). It shows what the text cannot: [the hours; the share of sources read in full; the proposals I took from the agents]. It also shows the remedy's limit. A record is costly to read, and reading is now the scarce resource.

- **In ¶6.2, drop the publication cap,** or present it as the irony it is. Make the pledge the main gesture:

  > I will not list this essay as a research output in any formal evaluation [ANECA *sexenios* included]; on this essay's argument, that is the one change a single author can make to what is counted.

- **Placement.** Keep the exhibit at the start of the master, as the brief intends. In the EMBO version, put it in the last sentence of the first paragraph (E2): it is still "from the start", but after the claim.

**R2-2. Box 1 and the contribution statement do not yet show the human's intellectual contribution**

**Location:** ¶0.3b, Box 1 (Process), the CRediT statement, the AI-use statement and ¶4b.1.

**Problem:**
- **(a) The division of labour is generic.** "I set the thesis, structure and key judgements; AI agents searched … drafted … reviewed" almost repeats Fourie's footnote ("I chose the question, assumptions and argument …"). The essay has better evidence than this and does not use it. The brief records:
  - how the thesis evolved, in four steps, from "AI is destroying the academic system" to the present claim;
  - several structural choices marked as the assistant's "(proposal)": the process box, the CRediT statement, the time-and-cost record, the first person singular, and the emphasis on legitimate use over misuse;
  - a repositioning of the contributions after the prior-work check that the AI ran.

  Honest documentation would say which key judgements were the author's, which were AI proposals the author accepted, and which proposals the author rejected. That is more interesting than the disclaimer. It is also evidence for Hutchinson's point (*Nature* Correspondence, 29 Sep 2026; outline §12) that taxonomies of contribution are "too coarse" for "sustained intellectual interaction". Cite it.
- **(b) CRediT is misapplied.** CRediT defines "Writing – original draft" as writing the initial draft. By the essay's own account, the AI generated the initial draft from the author's outline. Claiming that role in an essay about unreadable effort is the kind of inaccuracy a referee will seize on.
- **(c) The verification claims are in the past tense but not yet true.** Box 1 says that "weakly read claims could be re-checked [confirm]" and that "I … checked every quotation against its source [confirm]". The text still holds 77 recheck flags, and several quotations come from abstracts (Manabu) or from partial reading (Huang).
- **(d) The record contradicts the priority claim.** "I reached it independently" (¶4b.1) cannot be supported by a record that starts on 15 Oct 2026, after Huang et al. appeared.

**Fix:**
- **Rewrite Box 1's Process paragraph** (about 150 words; the numbers in brackets come from the current register and must be updated):

  > Over [D] days I set the question and thesis in a planning conversation (in Spanish), which the record keeps as the author's brief. AI agents (Claude [model, version], via Claude Code, on a [account type] account with model training [on/off]) then searched the literature, wrote notes on six evidence gaps, resolved DOIs against Crossref, DataCite and arXiv, and tagged each of [174] claims by how its source had been read: [14] from full text, [40] from primary documents, [68] from abstracts, the rest from summaries, extracts or secondary reports. They drafted an outline and a first draft from my structure in about [3.5] hours. Several framings were the agents' proposals that I accepted, among them [the contribution list, the first person, this box]; I rejected [example]. I then spent [X] hours revising, reading in full the [k] sources the argument rests on, and checking each quotation. The version history ([DOI]) records each step.

- **Correct the CRediT statement:**

  > [Name]: Conceptualization; Methodology (design of the AI-assisted workflow); Investigation (direction and verification of the literature search); Validation; Writing – review & editing; Project administration. The initial draft was generated by an AI tool from my outline (Box 1). AI tools are not contributors under CRediT.

- **Complete the AI-use statement** with what you actually did and how far it reached. For example: "I read in full the [k] sources on which the argument depends; for the others I checked each quotation against the text recorded in the claims register (full text, abstract or primary document)."
- **Optionally, mark your own sentences.** In the Zenodo version, mark the sentences you wrote yourself, such as the [AUTHOR] passages, so that the record makes legible what the text hides. This is in the spirit of the thesis.

**R2-3. The tool choice and the conflict of interest: transparent, but not yet independent**

**Location:** ¶0.3b, ¶3.6, ¶5.2, ¶5.5, Box 1 (Conflict of interest) and the Competing interests statement.

**Problem:**
- **(a) The essay fails its own standard.** ¶3.6 says that using a proprietary model in research "needs explicit justification" (Palmer et al. 2024) and that open models are the ethical way forward. The essay was made with a proprietary model, and Box 1 does not justify that choice.
- **(b) Disclosure is not verification.** The conflict is disclosed well:
  - it appears in the opening, in Box 1 and under Competing interests;
  - the unfavourable facts are reported: Anthropic converged late, the toggle was pre-set, retention rose to five years, and Claude Code is covered.

  But the conflicted tool researched and drafted the very passages where the conflict bites (¶5.2, ¶5.3, Figure 2). This review comes from the same tool.
- **(c) "I report the unfavourable facts as I found them."** The agents found them. Write "as the sources state them".
- **(d) ¶5.5 draws attention to the conflict without serving the argument.** It exists because the brief forbids a claim ("the most advanced by far"). The essay makes no claim about the frontier, so a paragraph denying one only points at the conflict.

**Fix:**
- **Add to Box 1:**

  > Why a proprietary model. Section 3 argues that research should use tools it can inspect (Palmer et al. 2024). I used a proprietary one because [reason]. By my own standard this needs justifying, and it is a compromise; [say whether any step could have been done with an open model].

- **Have the Anthropic-related claims checked independently.** A person, or a tool not made by Anthropic, outside the drafting loop should check ¶5.2, ¶5.3, Figure 2 and Box 1 against the primary pages. Say so in Box 1.
- **Find one human reader from outside the project before submission.** That is the only real answer to "the reviewer is the same model".
- **Cut ¶5.5 in every version.** If the brief's concern must be met, half a clause will do: "the lead among a few US firms changes within weeks (Epoch AI 2026)".

**R2-4. §3, the ideal: not utopian, and earned in the master, but disconnected from evaluation**

**Location:** ¶3.1–¶3.6; the last sentence of ¶2.5.

**Assessment.** §3 keeps its own rule ("each ideal rests on a mechanism that already works somewhere") better than most visions do. Its change of register is honest ("the part of this essay I would most like to be right about"), and its tone is restrained. It is not too utopian. But:

- **(a) The mechanisms are uneven.**
  - Swanson's literature-based discovery stayed marginal for 40 years. The claim that language models now make checking cheap is asserted, not shown.
  - OpenScholar is a benchmark result.
  - The cheap pivot rests on a preprint (Zheng et al.).

  State, for each ideal, where it works, on what evidence and at what scale.
- **(b) The ideal belongs to an individual; the essay is about institutions.** The ideal is a researcher who stays literate across fields, but the essay's subject is evaluation. The missing link is that AI could cheapen *reading* as well as writing. Checkable synthesis is what evaluators need, and it is the one exit that does not lead to rationing. Add one sentence:

  > Checkable synthesis also serves evaluators: a review whose every citation can be verified in seconds lowers the cost of reading, the scarcity that now matters most.

- **(c) The ideal's main risk is in the bibliography but not in the section.** Messeri & Crockett (2024), cited only in §4b, argue that AI tools create "illusions of understanding". That is ¶2.5's point ("Summarising is not mastery") seen from the user's side. Add:

  > The risk is the one Messeri & Crockett (2024) call the illusion of understanding: a fluent synthesis of a neighbouring field can make a researcher feel literate in it before they are.

  Optionally, for the master: much of the burden of knowledge is tacit and social, and AI supplies information, not membership of a community. Audit: Collins & Evans (2007), *Rethinking Expertise*, on interactional expertise.
- **(d) ¶3.6 bridges to §5, not to §4.** End §3 with a pointer forward: "Section 4 asks whether AI is being used this way".

**In the short versions,** keep two sentences, one each from ¶3.3 and ¶3.6, as the payoff in "What institutions can do", as the outline proposes.

**R2-5. §5 (concentration, chat data, the China contrast): mostly fair on the facts, but off the thesis and quick to date**

**Location:** ¶5.1–¶5.7, Figure 2 and Box 1.

**Problem (a): relevance.** §5 spends about a sixth of the essay (1,035 words) on industry structure, chat-data policy, publishers' licensing, litigation, China and the race at the frontier. It ends by saying "No study yet links chat-data harvesting to the homogenisation of science, and I claim no such link".

The section is doing two different jobs:
- **an external driver of narrowing,** which needs only ¶5.1, ¶5.6 and the evidence on monoculture;
- **the political economy of the tools** on which §3's ideal depends: ownership, confidentiality and appropriation.

Chat data belongs to the second job. For researchers, the issue is less narrowing than the risk that unpublished results typed into a personal account become training data. The draft makes this point well ("the same researcher is outside the training data on a university licence and inside it on a personal account"), then moves on.

**Problem (b): currency.** These numbers will be stale before review ends:
- the Epoch ECI scores (166.82 against 166.41), and the three changes of leader in September;
- the leader on Arena;
- the shares of Hugging Face downloads;
- the gap between open and closed models.

A peer-reviewed essay should not rest on quantities that go out of date within weeks.

**Problem (c): specific inaccuracies and imprecisions.**
- **Figure 2's caption** calls Anthropic "the last major US developer to commit to the contrary". Apple, a major US developer, still uses opt-in only, as ¶5.2 itself says. Write: "the last of the major US AI labs to switch (Apple still trains only on opt-in data)".
- **"Meta, X, Microsoft and Mistral do the same" (¶5.2).** X trained on users' *posts*, not their chats, and research note 1 did not find a training opt-out for Meta AI users outside the EU. Write: "Meta, Microsoft and Mistral also train on consumer chats by default, and X trained its model on users' posts".
- **"Enterprise, API, government and education accounts are excluded everywhere."** Write "at every company reviewed".
- **"Though training itself was ruled fair use (Bartz v. Anthropic 2026)" (¶5.3).** Write: "though a district court had ruled that training on lawfully acquired books was fair use" (audit).
- **Fairness to Anthropic.** Audit: did the 2025 change apply only to new or resumed chats and coding sessions? If so, say so.
- **Transparency scores (¶5.4).** "DeepSeek 32, Alibaba 26 out of 100", given without the US firms' scores on the same index, implies a contrast that may not exist. Give the range (audit) or drop the scores.
- **Energy (¶5.4).** Jegham et al. compare the *same* model on different infrastructure. The comparison says something about data centres and nothing about whether Chinese *models* are efficient. Write:

  > Lower energy use is not established either: in one modelled comparison, the same DeepSeek model used about four times as much energy per long query on DeepSeek's servers as on Azure (Jegham et al. 2025, preprint), which says more about data centres than about models.

- **"Chinese weights carry state-shaped content" (¶5.7).** Cite the rule, or soften the phrase to "carry content rules set by the state (CAC et al. 2023)".

**Problem (d): the China material closest to the thesis sits in the wrong section.** China's 2020 change to *what is counted* (¶4c.4) is a natural experiment in reform by decree; the licensing of Chinese models (¶5.4) is not. Both paragraphs are in the master only. In the master, keep ¶4c.4 once its sources are fixed, and compress ¶5.4 to two sentences.

**Fix:**
- **Rebuild §5** around the three-level map in R2-6.
- **Compress ¶5.2** to "even the holdout converged", plus the two-tier point turned into a recommendation:

  > For science, the issue is less narrowing than confidentiality and appropriation: unpublished results typed into a personal account may become training data, and a university licence is the difference. Institutions can act now, by providing accounts that are excluded from training and saying so.

- **Cut ¶5.5,** and cut ¶5.3 except for one sentence on publishers' licensing.
- **Move every tracker number** to a dated note in the Zenodo record.
- **Retitle the section** "The external driver: who owns the tools, and what they learn from us" (the outline's second alternative).

**R2-6. The two drivers do not line up with the essay's own rival explanation**

**Location:** ¶0.3 ("Fourth"), ¶4b.2, ¶5.6, Box 2 (the optional extension) and the standfirst.

**Problem:**
- **(a) Three candidate drivers, sorted by two binaries.** §4b sets incentives against *affordance*, the fact that AI works best on well-posed problems with abundant data. §5 sets internal drivers against external ones. Affordance is neither: it is partly intrinsic to machine learning and partly shaped by firms, which build for benchmarks and markets. The essay never says where affordance belongs.
- **(b) The external mechanism does not depend on who owns the model.** "Shared models make outputs alike whatever the incentives (Kleinberg & Raghavan 2021; Bommasani et al. 2022)" describes algorithmic monoculture, and ¶3.6 concedes that monoculture arises "whoever owns it".
  - A single open model could create a monoculture too: Qwen accounts for about half of open-weight choices in science (Dunivin 2026).
  - So the mechanism of narrowing is model concentration, not corporate control.
  - Corporate control matters to narrowing through firms' choices of training data and defaults, and to appropriation through chat data.
- **(c) It is doubtful that the model family can be identified paper by paper.** Dunivin probably identifies models *used as research tools*, not models used to write or to generate ideas (audit). If so, "convergence by model family" can be tested only for papers that use LLMs as a method.

**Fix:** keep the brief's distinction between internal and external drivers, and place affordance explicitly. Replacement for ¶5.6 (about 130 words):

> Narrowing therefore has candidate drivers at three levels. What researchers are rewarded for is the internal driver (Section 4; Huang et al. 2026). What the tools do well, well-posed problems with abundant data, is the technology's affordance (Hao et al. 2026). Who builds the tools, on what data and with what defaults, is the external driver: a few firms shape a few model families, and shared models make outputs alike whatever the incentives (Kleinberg & Raghavan 2021). The three leave different traces: narrowing that grows with incentive intensity, narrowing that tracks data availability, and convergence by model family. Box 2 separates the first two; the third is testable where papers name the model they used. No study yet links any of them to the homogenisation of science as a whole.

**R2-7. The prose: clear sentence by sentence, but carried by citation, and with a recognisable machine rhythm**

**Location:** throughout.

**(a) Density.**
- About 250 in-text citations in 6,800 words, one every 27 words.
- About 70 direct quotations.
- One sentence in ten runs to 47 words or more.
- Many paragraphs follow one template: a claim, four to six citations, then a caveat (¶1.1, ¶2.1, ¶4a.2, ¶5.2, ¶4c.2).

The argument is too often made in other people's sentences. ¶0.2 strings four quotations into one 67-word sentence, and ¶1.1 strings four findings into one 63-word sentence.

**(b) Are 173 references too many for an essay?** Yes, for every target venue:
- EMBO Reports allows 15.
- PLOS Biology essays take 30–60.
- Minerva counts references within its 8,000–10,000 words. This list alone runs to about 3,800 words, so the outline's trim to about 90 references is the minimum.

Only the Zenodo record can carry them all. There is also a reflexive point: 173 references assembled cheaply are expensive to check, so a referee asked to verify them bears exactly the cost the essay describes.

**Recommendation:**
- Publish the claims register, with each claim's read status, as the evidence supplement in the Zenodo record, and link to it from Box 1. It then serves as part of the exhibit as well as the cure for over-citation.
- In the master's main text, allow no more than two citations per claim and one quotation per paragraph.

**(c) A machine-like texture.** An automated search found none of the usual LLM marker words (delve, showcase, underscore, pivotal, intricate, notably, crucial, comprehensive, meticulous), so the joke in ¶2.1 is safe as far as vocabulary goes. But the syntax has a recognisable rhythm:
- **Paragraph-final maxims:**
  - "which is the problem in miniature";
  - "This essay is the case in point";
  - "Design matters, and adoption follows incentives.";
  - "The claim concerns control, not legality.";
  - "The lesson concerns mechanism, not regime";
  - "Hence Zenodo.".
- **Antithesis:** about one sentence in five turns on "not", "nor", "rather than" or "instead of".
- **Staged dialogue:** "I grant this."; "Hence my question:"; "That last point is part of the argument."; "The contrary evidence deserves a full hearing".
- **The repeated triad:** the three scarcities are spelled out in full in the standfirst and ¶0.3 (word for word), in ¶1.3 and in the Figure 1 caption.

Each device works on its own; together they form a signature. How to break it:
- Let some paragraphs end on evidence.
- Name the triad once ("the three scarcities") and refer back to it after that.
- Keep the best maxim, "The technology lowers the price of moving; evaluation still charges it" (¶3.5); it earns its place.
- Write the [AUTHOR] passages in your own idiom. They will break the rhythm usefully.

**(d) Repetition across sections:**
- **The distinction from Hansen** appears twice (¶1.3 and ¶4c.3). Keep the ¶1.3 version.
- **The cautions on Hao** appear twice (¶4a.1 and Box 2). The box can say "for the reasons in Section 4a".
- **The argument about effort as a signal** recurs in the standfirst, ¶0.2, ¶0.3, ¶1.3, ¶2.2, ¶2.7, ¶6.2 and Box 1.

**(e) Hedging.** Most hedges are substantive and well judged ("That reconciliation is my own reading"; "I state narrowing as a second-order risk"). A few are performative ("by my inference rather than any finding") or self-referential throat-clearing ("This section changes register."). The bigger problem is over-signposting, not over-hedging.

**(f) "We".** The brief chose "I" deliberately, so avoid the two generic uses of "we": "the best we have" (¶4a.4) and "what we tell the tools" (¶5.2 and the §5 heading). Write "what users tell the tools".

**(g) The [AUTHOR] slots.** Most are well placed. A few should be cut or changed.

| Slot | Verdict |
|---|---|
| ¶0.1: time and cost | Good, if the figures are striking; otherwise leave them to Box 1, as drafted. |
| ¶0.1: why you made the essay this way; Spanish and English | Keep it to one sentence, and move the language note to Box 1. |
| ¶2.2: you as a non-native writer | The best slot. It gives your personal stake and supports "Part of the loss is a gain". Keep it in every version. |
| ¶2.3: a review you suspected was AI-written | Cut it. It cannot be verified, reads as an accusation and adds nothing. |
| ¶2.5: a background section drafted in an evening | Keep it, but frame it around what you could not yet judge; that supports "Summarising is not mastery". |
| ¶3.5: a cross-field connection | Master only. |
| ¶4b.1: where the hypothesis came from | Keep the story, but drop any claim of priority (R2-2d). |
| ¶5.2: account type and model-improvement setting | Essential in every version, whatever it says. |
| ¶5.4: accepting the rewording of "consume much less" | Accept it; the evidence supports it. |
| ¶5.7: an EMBL or UPF model service | Good if verified. "UPF reportedly provides Gemini" rests on a search summary. |
| ¶6.1: what you would change on a panel | The second-best slot. Make it the concrete recommendation. |
| ¶6.2: the pledge | Make the pledge the main gesture (R2-1d). |
| ¶0.3, ¶4b.3 and Box 2: the preregistration | This is a decision, not a slot. Settle it before the Correspondence. |
| Data availability: redaction | Also check whether the research notes, which contain long verbatim quotations from paywalled articles, can be released under CC BY. |

**R2-8. The essay's model of evaluation draws on signalling theory alone**

**Location:** ¶1.1, ¶1.3 and ¶2.7.

**Problem:** the essay treats evaluation as the reading of costly signals. Studies of how panels actually work describe deliberation instead: plural criteria, negotiated standards of excellence, and judgement formed in conversation. Audit: Lamont (2009), *How Professors Think*. To an STS reader, the signalling model alone will look thin.

**Fix:** one sentence in ¶1.3, which also strengthens the case for "count less, read more":

> Evaluation is not only the reading of signals; panels deliberate, weigh plural criteria and negotiate what counts as excellence (Lamont 2009). But deliberation needs a manageable docket, and cost is what kept it manageable.

### Minor issues

1. **§4's structure.** Rationing, the essay's cleanest contribution, sits under "What AI is actually doing", but caps are what institutions do, not what AI does. Keep the brief's structure in the master and retitle §4 (R1-4b). The EMBO version already promotes rationing to its own section, as the assembly map does.
2. **The marker-word joke in ¶2.1** ("Finding none would prove nothing") cuts both ways, because telling a model to avoid marker words is now routine. Keep it in the master and cut it from the short versions.
3. **¶3.2:** "Imagine every field with a patient reader who knows what the next field over has already found." This is the essay's best image; keep it in the master.
4. **¶5.2:** the researcher's quotation from *Nature* ("I do not want Claude to start telling people my research results") is the most vivid evidence in §5. Keep it in the master.
5. **¶5.3:** the sentence on Stack Overflow is tangential; cut it.
6. **Box 1, "Venue policy":** this is process administration, not argument. Move it to the Data availability statement, and replace "Hence Zenodo." with "These rules are why the preprint is on Zenodo."
7. **Box 1, "Precedents":** the list is fair. Say plainly that Fourie (2026) used the same tools in nearly the same division of labour; that is the precedent readers will know.

### Line-level notes on the prose

- **¶0.1.** "Nothing in the text shows what it cost or who did which part of the work, and to the system that will evaluate it, it is one more countable item." Replace with:

  > The text does not show what it cost or who did what. To the system that will evaluate it, it is one more item to count.

- **¶0.1.** "Hence my question: if a careful, fully disclosed use of AI still yields an output whose effort no reader can see, what is academic evaluation measuring?" Replace with:

  > If careful, disclosed use of AI yields a text whose effort no reader can see, what does counting such texts measure?

- **¶0.3b.** "That last point is part of the argument." Replace with:

  > How the essay was made is part of its evidence.

- **¶0.4.** "Sections 4 and 5 explain why it is not doing so" should read:

  > Sections 4 and 5 ask whether it is doing so, and what stands in the way

- **¶2.3.** "I grant this. A review simply no longer certifies an expert's time, and cheap reviews now meet cheap papers." Replace with:

  > Granted; but a review no longer shows that an expert spent time on the paper, and cheap reviews now meet cheap papers.

- **¶2.7.** "This essay is the case in point: disclosed, accountable and still unreadable as evidence of effort." Replace with:

  > This essay is disclosed and accountable, and its text still says nothing about the effort behind it.

- **¶3.4.** "Design matters, and adoption follows incentives." Replace with:

  > Whether AI finds blind spots or reinforces them depends on how it is built and on what its users are rewarded for.

- **¶4c.3.** "Two scarcities need separating. His is symbolic, produced by rejection; the one AI removed is a scarcity of costly inputs." Delete; it repeats ¶1.3.
- **¶5.2.** "Opt-out is a form of consent, and no company publishes how many users keep the default; the point is structural." Replace with:

  > Opt-out is consent of a kind, and no company says how many users keep the default. The point is structural:

- **¶5.6.** "They predict different things, narrowing that varies with incentive intensity (Box 2) or convergence by model family, now identifiable paper by paper …; and though entangled, since firms build for the market academia creates, they are separable in analysis and partly in data." Replace it with the R2-6 paragraph. If you keep the sentence, split it:

  > They predict different patterns. Narrowing driven by incentives should vary with how hard counting bites (Box 2); narrowing driven by shared models should show as convergence by model family, whatever the incentives. The two are entangled, since firms build for the market academia creates, but each leaves its own trace.

- **¶5.7.** "Open is not independent (Widder et al. 2024), and Chinese weights carry state-shaped content." Replace with:

  > Open is not independent (Widder et al. 2024), and Chinese open weights carry content rules set by the state (CAC et al. 2023).

- **¶6.3.** "Once countable output costs almost nothing, the system will have to answer deliberately." Replace it with the ending in Synthesis §6.
- **§5 heading.** "The trajectory we're actually on: concentration of the tools and of what we tell them" should read:

  > The external driver: who owns the tools, and what they learn from us

---

## Part 4. Synthesis

### 1. The ten changes, ranked by how much each raises the odds of acceptance and the quality of the paper

1. **Rewrite the EMBO version; do not compress it.**
   - **What:** build it around "rationing is not reform"; open with NIH; say which layer AI makes cheap; anchor it in the life sciences (including Suchak et al.); 15 references; one figure.
   - **Why first:** without this there is no submission. The KEEP-3800 text alone runs to 5,164 words, and the citation-led style cannot survive a 15-reference limit.
   - **Where:** E1–E3, E5; Synthesis §2 and §4.
2. **Recalibrate the core claim.**
   - **What:** say which layer is cheap (the writing and synthesis, not the experiments); split the information mechanism from the congestion mechanism; make the claim conditional on differences in cost; write "invisible", not "gone"; align the title and standfirst.
   - **Why:** the thesis hinges on it, and it is the first thing any referee will test.
   - **Where:** R1-2, E3.
3. **Tighten the rationing argument.**
   - **What:**
     - define rationing;
     - sort Table 1 into caps, gates and a sanction;
     - show whom the caps bind;
     - add the pre-AI precedents;
     - correct "the information does not return";
     - present tiered caps as rationing fused with the fallback to prestige;
     - add automated evaluation as the fourth response;
     - note that those who ration are mostly not those who count.
   - **Why:** it is the cleanest contribution, and the one most exposed to precise objections.
   - **Where:** R1-3.
4. **Turn the exhibit into evidence.**
   - **What:**
     - report time by phase, cost, the account setting and the tally of how sources were read;
     - report which AI proposals were adopted;
     - link the record to the documentation remedy, and to that remedy's limit;
     - fix the CRediT statement;
     - justify the proprietary tool;
     - delete "independently".
   - **Why:** it turns the most distinctive feature from a device into an argument, and removes an integrity flaw that referees would find.
   - **Where:** R2-1, R2-2, R2-3.
5. **Read the interlocutors in full and resolve the load-bearing flags.**
   - **What:** read Huang, Manabu, Kusumegi, Zheng and Gartenberg in full; check each venue's own call for the conference caps; take the TechCrunch-only ban out of the rationing list; cite the 2026 *Nature* pieces the brief names (Messeri & Crockett, Hutchinson, Motoki).
   - **Why:** claims of novelty cannot rest on abstracts. This is a precondition for submission.
   - **Where:** R1-1, R1-7.
6. **Make the reform movements allies.**
   - **What:** argue that AI vindicates "count less, read more" but raises the price of reading; bring the last sentence of ¶4c.4 into the main line; answer the bibliometric counter-argument.
   - **Why:** fairness; this readership; and it fixes the logic of the conclusion.
   - **Where:** R1-6.
7. **Fix Box 2.**
   - **What:**
     - deal with the moderator that AI use itself changes (career stage) and with the language confound;
     - use dated reforms or CoARA dates as the source of incentive variation;
     - define data availability;
     - add the prediction about where movers land;
     - make the falsification clause consistent with ¶4a.4;
     - write "discriminating under stated assumptions";
     - commit to running the test, or offer it to the field.
   - **Why:** contribution 2 survives only if the design survives a methods referee.
   - **Where:** R1-5.
8. **Rebuild §5 on a three-level map of drivers.**
   - **What:** treat chat data as a matter of confidentiality and of two account tiers, with a recommendation to institutions; cut ¶5.5 and the tracker numbers; correct the wording on Apple, "do the same", Bartz, energy and the transparency scores.
   - **Why:** coherence and currency; it also removes factual exposure.
   - **Where:** R2-5, R2-6.
9. **Revise the title, standfirst and conclusion.**
   - **What:** a new title; a 60-word standfirst; a conclusion that ranks its proposals and ends on the asymmetry between the cost of making and the cost of judging; the pledge in place of the self-imposed cap.
   - **Why:** editors read the title and standfirst first, and readers keep the ending.
   - **Where:** §5 and §6 below.
10. **Rework the prose.**
    - **What:**
      - halve the citations and quotations in the master, and move the evidence to the published claims register;
      - one claim per sentence;
      - remove the duplicated passages;
      - vary the triad and the paragraph endings;
      - cut the anecdote slots to two or three;
      - add one sentence on panels as deliberation.
    - **Why:** readability. An essay about whether effort can be read should not read as machine-made.
    - **Where:** R2-7, R2-8.

### 2. What to cut first to reach 3,500 words

The figures are approximate savings against the master's 6,773 words. Make the cuts in this order; each loses the least for the words it saves.

| Order | Cut | Keep | Saves |
|---|---|---|---|
| 1 | §5: ¶5.1, ¶5.3, ¶5.4 and ¶5.5 entirely | The three-level ¶5.6 in about 100 words; "even the holdout converged" and the two-tier recommendation in about 80 | ~850 |
| 2 | §3: ¶3.1, ¶3.2, ¶3.4 and ¶3.5 | ¶3.3 and ¶3.6, one sentence each, moved into "What institutions can do" | ~500 |
| 3 | §1: ¶1.1 and ¶1.4 | The pivot of ¶1.3 in about 100 words; one clause of ¶1.2 | ~420 |
| 4 | §4a: ¶4a.2 and ¶4a.3 (the ideation preprints and the homogenisation experiments) | Hao and Zheng in two sentences each; the verdict of ¶4a.5 | ~410 |
| 5 | §4b: the evidence list in ¶4b.1 (March, Wang, Boudreau, Foster, Teplitskiy, Packalen) and the examples from outside science in ¶4b.2 | The hypothesis with Huang; the rival in two sentences; one sentence of ¶4b.3 | ~270 |
| 6 | §2: ¶2.6 (fraud; Suchak moves into the main line), the marker-word sentences of ¶2.1, the vendor and trial details of ¶2.3, Galdin & Silbert | The core of ¶2.2, including "Part of the loss is a gain"; ¶2.4 with ¶2.6b merged in two sentences; ¶2.5; the revised ¶2.7 | ~440 |
| 7 | §4c: ¶4c.4 (China); ¶4c.1 compressed; Table 1 moved to Zenodo | ¶4c.2 and ¶4c.3 with the R1-3 additions; the reform paragraph of R1-6 | ~300 |
| 8 | Boxes: Box 1's "Venue policy" and most of its "Precedents"; Box 2's measurement paragraph and its extension | Box B in about 220 words (process with numbers; tool and account; time and cost; one sentence each on the conflict of interest and on Fourie). Box A in about 200 words (design; control for data availability; falsification) | ~390 |
| 9 | Introduction: the roadmap (¶0.4); ¶0.2 cut to two sentences; ¶0.3b folded into the last sentence of the opening | The E2 opening and a 60-word contribution paragraph | ~280 |
| 10 | Conclusion: the list in ¶6.1 cut to one ranked proposal and two short ones; ¶6.3 | The ending in §6 below | ~165 |

**The arithmetic:**
- The cuts total about 4,000 words, which leaves about 2,750.
- The additions recommended here bring that to about 3,100. They are the definition of rationing, the split between information and congestion, the fourth response, the reform paragraph, the sentence on which layer is cheap, and Suchak et al.
- That leaves about 400 words for the author's own passages and as margin.

**For the master** (at most 7,000 words, for Zenodo and Minerva), make room for the [AUTHOR] text by cutting ¶5.5, most of ¶5.3, ¶4a.3, ¶1.4, the duplicated distinction from Hansen and the roadmap. That frees about 400 words.

### 3. What is strongest, and must survive every cut

1. **The conceptual core in ¶1.3:** "Why did the gates work at all? Because what they counted was costly to produce, and the cost carried information." Keep it with the distinction from Hansen's symbolic scarcity, stated once.
2. **The rationing analysis** (¶4c.2–¶4c.3), once tightened: the caps restore the scarcity of submissions but not what costly production revealed, and tiered caps write the Matthew effect into the rules.
3. **"Part of the loss is a gain" (¶2.2):** polished English partly signalled that the author was a native speaker. The point is humane, rarely made, and the author's own stake.
4. **The candour about evidence:**
   - ¶4a.4, the full hearing for the contrary evidence;
   - ¶4a.5, "the evidence supports less than the headlines";
   - ¶2.6b, the concession on the tail.

   Keep at least one sentence of each; they buy credibility with sceptical readers.
5. **The last sentence of ¶4c.4:** "without capacity for qualitative judgement, discretion migrates to gatekeepers, and AI-era volume consumes exactly that capacity". It is the essay's best answer to why reform is hard now, and it must be rescued from a paragraph that every short version cuts.
6. **The point about two tiers of account (¶5.2):** "outside the training data on a university licence and inside it on a personal account". It is the one place where §5 gives institutions something to do.
7. **"A cheap essay does not prove that research is cheap. It shows which layer has become cheap" (¶6.2).** Move this insight up front as well (E3).
8. **The core of Box 2,** once fixed: a triple difference within fields, with data availability measured, and an honest falsification clause.

### 4. Suggested 15 references for the EMBO version

Each reference either carries a load-bearing fact or defines the competition that the brief's positioning requires:

1. NIH 2025 (NOT-OD-25-132)
2. arXiv 2026 (rate-limit policy)
3. Singh Chawla 2026a (conference caps), or the ICLR 2027 call itself
4. Blekhman 2026
5. Huang et al. 2026
6. Fourie 2026
7. Hansen 2026
8. Manabu 2026, once the body has been read
9. Hanneke et al. 2026, the closest precedent for the three scarcities
10. Kusumegi et al. 2025
11. Kobak et al. 2025, for prevalence in PubMed
12. Suchak et al. 2025, for formulaic biomedical papers made cheap by ready-made data
13. Hao et al. 2026
14. Zheng et al. 2026
15. The Zenodo record

**Departures from the outline's core list:**
- **Dropped:** Gartenberg et al., Hanson et al. and Brzostowicki.
- **Added:** Hanneke et al., Kobak et al. and Suchak et al.

**If EMBO allows a data link outside the reference count,** use the freed slot for one of:
- Cowgill et al. 2026, for the mechanism of differential cost;
- Brzostowicki 2026, on chat data and local models;
- CoARA 2022.

**Keep Manabu even if he cannot be read in time;** the brief's positioning requires it. In that case cite only claims his abstract states, and say so in the Zenodo version.

### 5. The title and the standfirst

**Verdict on the title.** "Even good use breaks it: academic evaluation is not prepared for AI".
- **Strengths:**
  - it puts the thesis first;
  - it is memorable;
  - it flags the counter-intuitive claim that misuse is not needed.
- **Weaknesses:**
  - "it" has no referent until the subtitle;
  - "breaks" claims more than the evidence shows (R1-2);
  - "not prepared for AI" is the generic frame of a dozen pieces from 2026;
  - it says nothing about rationing, which is what is new.

**Alternatives:**
1. *The cost was the signal: why academic evaluation is not ready for AI used well.* This puts the mechanism first. Recommended for the master and the Zenodo record.
2. *Rationing is not reform: academic evaluation after AI made writing cheap.* This puts the contribution first. Recommended for EMBO Reports.
3. *Scarcity by decree: AI, academic merit and the turn to rationing* (the outline's second option). A good alternative for EMBO, although the standfirst would then have to explain "by decree".
4. *Cheap to make, costly to judge: AI and the rationing of academic evaluation.* This names the asymmetry, which ties the exhibit, the fourth response and the conclusion together.
5. *This paper was cheap to make* (the outline's third option). Use it only if the time-and-cost figures, including the author's hours, are striking. The git record suggests they may be, but the irony then needs careful handling.

**Verdict on the standfirst.** At 156 words it is an abstract, not a standfirst:
- it lists five contributions;
- it uses jargon ("legitimacy is irrelevant to the mechanism"; "an internal driver of the narrowing that may follow");
- it claims that papers are "almost free to produce", which experimentalists will reject (E3).

The second half of its first sentence is the best hook in the essay; keep it.

**EMBO standfirst** (60 words):

> Generative AI makes the writing of papers, grant applications and reviews cheap, even when it is used honestly, and academic evaluation read merit partly from that cost. Funders, preprint servers and conferences are responding with caps. Caps restore scarcity, but not the information it carried. Institutions should change what they count and read, and test what is narrowing AI-era science.

**Master standfirst** (about 130 words):

> Academic evaluation inferred merit partly from what its outputs cost to produce: the writing of papers and grant applications, an expert's time on a review, the years of reading behind a synthesis. Generative AI lowers those costs even when it is used openly and well, so the outputs reveal less about the work behind them. Institutions have answered mainly with caps (NIH on applications, arXiv on submissions, AI conferences on submissions per author) that restore the scarcity of submissions but not the information it carried, and in two cases allocate it by past success. I argue that evaluation must change what it counts and reads, propose a test of whether incentives or the pull of data-rich problems drive AI-era narrowing, and document how this essay was itself made with AI agents.

### 6. Does the conclusion land?

**Not yet.**

**¶6.1** lists five proposals, mostly borrowed and each hedged, in no particular order. It reads as a literature summary at the point where the reader wants the author's judgement. The essay's own diagnosis implies an order:
1. If reading is now the scarce resource, economise on it: count less, and read what is counted. This is CoARA's programme, and it is now urgent.
2. Make documentation the new costly signal, with this essay as the prototype, and admit that it shifts the cost onto the reader.
3. Fund exploration over long horizons, and use Box 2 to learn whether that is the right lever.

**¶6.2** is the strongest paragraph. Keep its last two sentences, and replace the self-imposed cap with the pledge (R2-1d).

**¶6.3** ends on other people's questions (Manabu's and Blekhman's), and on a vague sentence ("the system will have to answer deliberately"). An essay troubled by unreadable authorship should end in the author's own words.

A possible ending, in about 95 words (check the bracketed comparison against the record before using it):

> This essay took [X] hours of my time and [€Y] to make. Judging it properly, by reading it and checking its sources, could take a referee [as long / longer]. That asymmetry, not misuse, is what academic evaluation now has to be designed around. Rationing buys time by making outputs scarce again; it does not buy back the information their cost once carried. The time should be spent changing what is counted, and the first change is cheap: count less, and read what is counted. I will not list this essay as a research output in any formal evaluation.

---

## Part 5. Flags for the citation audit

### A. Load-bearing: resolve before any submission

1. **Huang et al. 2026:** read the Comment in full. The third recommendation has not been seen, and ¶4b.2, ¶4b.3, Box 2 and the Correspondence depend on it.
2. **Manabu 2026:** read the body. Three quotations come from the abstract (¶0.2, ¶2.5, ¶6.3), and the claims of novelty depend on the body.
3. **Kusumegi et al. 2025** (¶2.2, ¶2.6b):
   - what the 23.7–89.3% range spans;
   - the exact wording of "reversed the relationship …";
   - which proxy for quality was used;
   - the breakdown by author background.
4. **Kobak et al. 2025; Liang et al. 2024 and 2025:** do they describe the use they detect as "mostly polishing"? If not, revise ¶2.1.
5. **NIH NOT-OD-25-132:**
   - does the notice say NIH will use technology to detect AI-generated text (¶2.4)?
   - does NIH report the share of PIs who submit more than six applications a year (R1-3a)?
   - separately: NIH's simplified review framework of 2025 (R1-3f).
6. **arXiv:**
   - when the 1 Oct 2026 cap was announced (September's count may include submissions made ahead of the cap; ¶2.6b);
   - any data on the share of submitters above two a month.
7. **The conference caps (ICLR 2027, AISTATS 2027, ACL, TMLR):** check each venue's own call. Also check "490 a decade ago" against ICLR's own statistics.
8. **arXiv's one-year ban (May 2026):** sourced to TechCrunch only, with unknown scope. Take it out of the rationing list.
9. **Rationing before 2025** (these determine the wording of Table 1's caption):
   - per-author caps at IJCAI (from about 2020) and at CVPR (2025);
   - the ERC's resubmission restrictions;
   - NSF's per-PI limits.
10. **Hao et al. 2026:** check the analysis of data availability and the quotation "almost unrelated" against the final Methods in *Nature*, not against arXiv v4.
11. **Zheng et al. 2026:** read the full text. Where do the movers land, and how is AI use measured?
12. **Gartenberg et al. 2026:** read from the abstract only; check "nearly all".
13. **Positioning:** add Messeri & Crockett 2026 (*Nature* 653:675–676), Hutchinson 2026 and Motoki 2026, which the brief names but the draft does not cite.

### B. Internal inconsistencies: fix in the text, no source needed

1. The **Figure 2 caption** ("the last major US developer to commit to the contrary") conflicts with Apple's opt-in policy, given in ¶5.2.
2. The **Table 1** title covers "2023–2026", but its caption says no measure was found before 2025.
3. The **falsification clause in Box 2** conflicts with the reconciliation in ¶4a.4.
4. **¶2.7** ("all three scarcities gone") conflicts with ¶2.5 ("judgement remains scarce").
5. **¶0.4** ("explain why it is not doing so") conflicts with ¶4a.5 ("not established").
6. The **CRediT statement** ("Writing – original draft") conflicts with ¶0.3b and the AI-use statement.
7. **¶4b.1** ("I reached it independently") conflicts with a process record that begins on 15 Oct 2026.
8. **¶6.2** proposes a self-imposed publication cap, which is rationing, in an essay that criticises rationing.

### C. Peripheral: fix or cut

1. **Quan et al. 2017:** is US$165,000 the maximum paid for a *Nature* or *Science* paper (¶1.1)?
2. **Butler 2003:** the re-analysis by van den Besselaar, Heyman & Sandström (2017), and Butler's reply (¶1.1).
3. **Fanelli 2018:** is "mistaken" his word?
4. **Hanson et al. 2024:** the comparison with the growth of the workforce.
5. **Thakkar et al. 2025:** did reviews "improve", or were they only "updated"?
6. **Fees and equity:** cite one study on article-processing charges and equity for ¶4c.3.
7. **CoARA:** a dated count of signatories from coara.eu. Also, whether EMBL or EMBO have signed DORA or CoARA.
8. **Bartz v. Anthropic:** the wording of the fair-use ruling (a district court; lawfully acquired books).
9. **Anthropic's change of August–October 2025:** did it apply only to new or resumed chats and coding sessions?
10. **The Verge:** the toggle pre-set to "On" rests on a secondary source.
11. **FMTI, December 2025:** the US firms' scores, for comparison.
12. **Jegham et al.:** the comparison is of the same model on different infrastructure.
13. **Dunivin 2026:** what exactly is identified paper by paper.
14. **The default-on dates for Microsoft and OpenAI:** these rest on search extracts and secondary sources only.
15. **¶4c.4, China:** the search summaries, and the reference whose authors are still to be filled in.
16. **"UPF reportedly provides Gemini and NotebookLM":** a search summary only.
17. **Literature suggested in this review:** verify before citing.
    - Coles, Kushnir & Niederle 2013 and the AEA job-market signalling service (R1-3d);
    - Collins & Evans 2007 (R2-4);
    - Lamont 2009 (R2-8);
    - the evidence on invitation-only review journals (R1-7).
18. **EMBO Press:** its current AI policy and preprint policy (E4, E6).
