# Response to the internal review, and record of the revision

**Files revised:**
- `paper/draft_full.md`: the master, now draft 2.
- `paper/draft_embo.md`: new. The EMBO Reports version, written fresh rather than cut from the master.
- `paper/correspondence_draft.md`: new. The *Nature* Correspondence replying to Huang et al.

**Inputs:**
- the internal review (`paper/reviews/referee_report.md`; issue numbers below follow it);
- the completed citation audit (`paper/reviews/citation_audit.md`; R, O and CN numbers follow it);
- the author's decisions of 16 October 2026 (`paper/brief.md`, and messages relayed by the coordinator);
- the author's companion analysis (`paper/figures/README_companion_analysis.md`): commit 41f795d for Figures 3 and 4, and commit 6021b3a for the within-field contrasts (Figure 5);
- research notes 7 (recommendations) and 8 (field differences), in `research_notes/AI academia essay evidence gaps/`.

**Who wrote this.** An AI agent (Claude, Anthropic) wrote this response and the revision. It is the same model family that drafted the essay and wrote the review, and the author has not yet read the revision. Each point below gives three things: what was done (accepted, partly accepted or declined), where, and one line of reasoning. Paragraph IDs (¶) are those of draft 2 of the master, which are listed in its header comment. EMBO locations are given by section heading.

**Date:** 16 October 2026.

---

## 1. Where things stand

| Output | Limit | Now | Notes |
|---|---|---|---|
| Master, main text with Boxes 1–2 | 7,000 words | 6,982 | Counts the empty Section 6 at its reserve of 700 words. The empty Section 4d has no text and no reserve. Headroom is 18 words, so the [AUTHOR] passages need offsetting cuts (the cheapest are listed in the file's header). |
| Master, references | none | 153 | Draft 1 had 173. |
| EMBO version, main text with both boxes | 3,500 words | 3,154 | Counts Recommendations at its reserve of 350 words. Headroom is 346 words. |
| EMBO version, references | 15 | 15 | Two preprints. Hosseini et al. replaced Asai et al. on 16 October. |
| EMBO version, standfirst | about 60 words | 63 | |
| Correspondence, text | under 200 words | 186 | The title adds 10 words. |
| Correspondence, references | 2 | 2 | |

All counts are by script: tokens containing a letter, digit, €, $ or &, with HTML comments and bracketed editorial markers removed.

**The main changes:**
1. **The core claim is recalibrated** (R1-2).
   - The information mechanism and the congestion mechanism are now separate.
   - The effort is "invisible", not "gone".
   - The claim is stated for the written layer only.
   - The damage "does not depend on misuse".
2. **Rationing is tightened** (R1-3).
   - Rationing is defined, and Table 1 now separates caps, a gate and a sanction.
   - The text says whom the caps bind and what a cap does restore.
   - Tiered caps are presented as a Matthew effect.
   - Automated evaluation is added as a fourth answer.
   - The text notes that those who ration are mostly not those who count.
3. **The exhibit has become evidence** (R2-1 to R2-3).
   - Box 1 gives the real process record: times, cost and the reading-depth tally.
   - It records who did what, and justifies the proprietary tool in a slot for the author.
   - The CRediT statement is corrected, and "independently" is deleted.
4. **The author's companion data are used** (Figures 3, 4 and 5 in the master; Figures 1 and 2 in the EMBO version).
   - In arXiv mathematics, the share of papers with an author posting five or more a quarter rose from 5.3% to 19.3%.
   - The rise comes from hundreds of established authors, so the reply to the review's "tail" objection no longer rests on argument alone.
   - **Field differences** (research note 8; Figure 5): biology has grown as much as physics since 2022 and parts from it only in 2026. Output accelerates where the rest of the work is also cheap (theory, computation, existing data). So experimental biology is less affected so far, possibly with a later onset; it is not immune.
5. **The EMBO version is a rewrite on "rationing is not reform".** It opens with the NIH cap and leads with the life sciences, the written layer and the contributions.
6. **The author's decisions are applied** (Section 3 below):
   - a misuse subsection;
   - an extended engagement with Blekhman;
   - the mathematics panel as the key figure;
   - Kusumegi et al.'s output gain dropped;
   - an empty Section 4d for a critique of DORA and CoARA;
   - a Section 6, Recommendations, still to be written, with words reserved, whose seeds point to research note 7;
   - the field differences, worded at the strength of the evidence;
   - the closest work added (Hosseini et al.; Lovén; Ma), and the partiality of the process record stated (Wu et al.).

   The author's field is now also stated.
7. **The texture is changed.**
   - Citations are down from about 250 to about 160 in the master's main text: about one every 39 words, against one every 27.
   - Direct quotations in the main text and boxes are down from about 70 to 25.
   - The machine rhythm is broken up (R2-7).

---

## 2. Major issues, point by point

### Editor A (EMBO Reports)

**E1. Format and completeness.** *Accepted.*
- **Where:** `paper/draft_embo.md`, written from the review's plan for this venue ("What would make it publishable here"). It has 15 references and two figures; Table 1 is left to the Zenodo record.
- **Why:** a version cut from the master would keep its citation-led texture, which 15 references cannot carry.
- **Still open:** the EMBO version has no [RECHECK] markers. It has [AUTHOR] slots and one [CITATION NEEDED], and it should be submitted only when they are resolved.

**E2. The opening does not say what is new.** *Accepted for the EMBO version; declined for the master.*
- **EMBO opening:** it starts with the NIH cap, then the written layer, then the claim that the damage does not depend on misuse. The exhibit is the last sentence of the first paragraph.
- **Master:** it keeps the exhibit first, because the brief makes the essay its own example from the start, and R2-1 itself says to keep it there in the master.
- **What changed in the master's opening:**
  - ¶0.2 paraphrases instead of stringing four quotations;
  - ¶0.3 puts rationing first;
  - the roadmap (¶0.4) is gone.

**E3. Life-science grounding, and which layer is cheap.** *Mostly accepted.*
- **Where:**
  - the written layer: the standfirst, ¶2.1, the EMBO opening and the conclusion of both versions;
  - Suchak et al.: moved out of the fraud paragraph into the grey zone of the misuse subsection (¶2.9; EMBO "Misuse is the visible tip"), as formulaic output that "needs no fraud";
  - NIH as the lead (EMBO) and Kobak et al. for prevalence (both versions);
  - bioRxiv and medRxiv volumes from the companion analysis (¶2.8, Figure 3; EMBO Figure 1): biology +50% over 2022 and +10% year on year; medicine, without COVID-19 papers, +139%;
  - the experimental biologist's objection, now answered with data (¶2.8b; EMBO "The cost was the signal", paragraph 4). Biologists write with AI as much as physicists, but bioRxiv shows no 2026 break, and within fields output accelerates where the rest of the work is cheap (Figure 5). Where no new experiment is needed, biomedicine surges: medRxiv preprints naming a public dataset grew 2.3-fold, against 1.6-fold overall;
  - the experimental bottleneck, in Blekhman's terms (¶2.8b; EMBO);
  - one sentence on tiered conference caps (EMBO opening).
- **Why:** readers recognise an argument through their own field. Experimentalists would reject "papers almost free to produce".
- **Partly open:**
  - **bioRxiv's rules:** only its FAQ, which excludes opinion pieces, is cited (Data availability). Whether bioRxiv or medRxiv have AI-specific limits was not established.
  - **European funders:** the EMBO version says they have issued guidance but no caps, under an [AUTHOR: confirm] marker. ERC guidance was not checked here.
  - **The master** keeps the machine-learning review evidence (¶2.3), now named as such, because public review data exist only there.

**E4. The exhibit must carry data and meet policy.** *Accepted. One policy check left for the author.*
- **Box 1 (master)** gives:
  - the record (session from 21:20 UTC on 15 October; outline 00:07; draft 00:58; review 01:29; a pause for a usage limit; revision from about 07:15);
  - the cost: about US$153 by 01:30, subagents included;
  - the reading-depth tally;
  - who did what.
- **Box 2 (EMBO)** gives the same figures in 248 words, and says that the record is partial.
- **AI-use statement:** it says what the tool did, and leaves the validation sentence to the author.
- **CRediT:** "Writing – original draft" is no longer claimed.
- **Why:** referees will check the disclosure first.
- **Open:** EMBO Press's current AI policy was not checked here (author action, Section 8).

**E5. A 15-reference essay must be carried by argument.** *Accepted.*
- **EMBO references:** the list follows the review's Synthesis §4 with one swap. Hosseini et al. (2026), the closest prior work on invisible effort (research note 7), replaces Hanneke et al., whose distinction between evaluation and production stays in the master (¶0.3). Asai et al., in the first EMBO draft's list, is now cited through the extended version (ref. 15).
- **Trackers:** cut. ¶5.5 is gone; ¶5.4 no longer gives the compute ratio or the human-preference ranking; the EMBO version has none.
- **Conference caps:**
  - In the master, Table 1's rows were rebuilt from each venue's own call (audit R80–R83).
  - The EMBO version cites the single news source, which E5 allowed.
- **arXiv ban:** it is now attributed to its primary source, Dietterich's X thread (R40), and classed as a sanction.
- **Why:** with 15 references, each one must carry a load-bearing fact or define the competition.

**E6. Overlap and disclosures.** *Partly done; the rest needs the author.*
- **Done:**
  - The EMBO Competing-interests section has a slot for the cover-letter disclosure of the Correspondence and the Zenodo preprint.
  - The Correspondence's header tells the author to hold the preprint until *Nature* decides.
  - The field is stated (author's decision: physics and biology).
- **Open (author):**
  - any EMBO roles;
  - EMBO Press's preprint policy.

### Referee 1 (metascience and research evaluation)

**R1-1. Novelty against the closest work.** *Accepted. One reading task left for the author.*
- **Where:** ¶0.3 now names the precedent of each contribution and the increment over it:
  - Blekhman: prestige as the fallback, against rationing already under way;
  - Fourie: rationing of evaluators' attention, against rationing of access to evaluation;
  - Hanneke et al.: the scarce resources of evaluation, against the production costs that served as signals;
  - Huang et al.: their hypothesis, against the triple difference;
  - the external driver.
- **Hansen:**
  - the distinction from his symbolic scarcity is stated once (¶1.3);
  - his AI screening at inclusion is engaged (¶4c.3b; EMBO).
- **Blekhman:**
  - the four differences (author's decision) appear in ¶0.3, ¶2.7, ¶2.8, ¶4c.2b and ¶4c.5;
  - his proposal to abandon the incentive system was engaged in the former ¶6.1, and is now a seed for Section 6 in both versions.
- **Huang et al.:**
  - read in full by the audit, from the print PDF;
  - their three recommendations are credited in ¶4b.2, Box 2, the Section 6 seeds and the Correspondence;
  - "I reached it independently" is deleted.
- **Additions:**
  - Adeyeye (¶1.3; SSRN abstract only, marked [RECHECK]);
  - Nee et al. (¶2.8; verified by research note 8);
  - Messeri & Crockett 2026 and Motoki 2026 (¶4b.1; titles only, marked [RECHECK]);
  - Hutchinson (Box 1);
  - Hosseini et al. 2026 (¶0.3; EMBO opening, paragraph 2), the closest prior work on invisible effort;
  - Lovén 2026 and Ma 2026 (Box 1), on verification as the new scarce resource.
- **Dropped:** Hakobyan was added and then cut for length.
- **Why:** a metascience referee checks each claim of novelty against these works first.
- **Open:** Manabu's body is still unread, so only claims in his abstract are used (¶0.2; EMBO). The author should read the PDF through EMBL or UPF.

**R1-2. Two mechanisms merged.** *Accepted.*
- **Where:**
  - ¶2.7 (information) and ¶2.8–¶2.8b (congestion);
  - ¶1.3, on differential cost;
  - the standfirst ("the damage does not depend on misuse");
  - EMBO, "The cost was the signal".
- **"Invisible", not "gone":** ¶2.7 says the signals have not disappeared, only the differences in cost on which they relied.
- **Congestion:** now partly evidenced by the companion data (¶2.8–¶2.8b): "At arXiv, congestion is no longer hypothetical; in experimental biology it has yet to show."
- **Why:** this is the hinge of the thesis. The information claim holds by construction; the congestion claim needed evidence.

**R1-3. The rationing category is loose and its scope unmeasured.** *Accepted, except (c), which needs sources.*
- **(a)** The text now says a cap "applies to" every investigator, and that caps "bind only the tail" (¶2.4, ¶4c.2b; EMBO).
- **(b)** Table 1 has a Type column. The arXiv peer-review rule is a gate and the one-year ban a sanction (¶4c.2).
- **(d)** A cap restores a little information: which six applications an investigator thinks best (¶4c.2b; EMBO).
- **(e)** Automated evaluation is the fourth answer (¶4c.3b; EMBO "Rationing is not reform"; Figure 1c).
- **(f)** Those who ration are mostly not those who count (¶4c.2b; EMBO).
- **Pricing (¶4c.3):** "refundable deposits" are restored. The equity point is now sourced to Hanneke et al.'s sentence on waivers. Both are confirmed in their full text (research note 7). Fourie is cited for his diagnosis only, not as a proposer of fees.
- **(c) Rationing predates AI.** This is stated in ¶4c.2b and the caption of Table 1, but marked [CITATION NEEDED]. The IJCAI, CVPR, ERC and NSF precedents are not in the research notes, and the rules forbid supplying them from memory.
  - Table 1's title now reads 2025–2026, and its caption notes arXiv's limit on active submissions, in place since 2024.
  - Whether NIH's simplified review framework changed what NIH counts is marked [RECHECK] in ¶4c.2b; it is not in the notes either.
- **Why:** this is the cleanest contribution and the most exposed to precise objections.

**R1-4. Uneven handling of evidence.** *Accepted.*
- **(a)** The ¶3.4 restatement of Hao et al. is gone, and the text says "3.02 times as many papers" (¶4a.1).
- **(b)** §4 is retitled "Is AI narrowing science, and can governance redirect it?", which covers Section 4c as well. The roadmap is gone.
- **(c)** Kusumegi et al.: superseded by the author's decision (Section 3, item 4).
- **(d)** ¶2.1 now says that detectors "measure style rather than purpose", and that much use is permitted.
- **(e)** The distribution shift: the argument is replaced by the companion analysis of authors (Figure 4) and Nee et al.; the within-field contrasts (Figure 5) add where the growth comes from. arXiv's cap was announced and applied on the same day, so September 2026 has no rush ahead of the cap.
- **(f)** Zheng et al.'s result is turned into a prediction in Box 2: the fields that movers enter should be more concentrated.
- **(g)** Galdin & Silbert are dropped for length; Cowgill et al. lead (¶2.2).
- **Why:** the essay promises to say how strong the evidence is, so it must do so evenly.
- **Open:** the full text of Zheng et al. has not been read; the audit checked the abstract only.

**R1-5. Box 2's test does not discriminate.** *Accepted. Two choices left for the author.*
- **(a)** Career stage is a secondary moderator, flagged as changed by AI use itself.
- **(b)** The language confound is handled by conditioning on language. It now rests on detector bias and on Zheng et al., not on Kusumegi et al.'s contested gains.
- **(c)** Data availability is measured by topic.
- **(d)** A prediction at the level of the system is added.
- **(e)** The falsification clause is now consistent with ¶4a.4.
- **(f)** AI use comes from disclosure statements, coded by task.
- **(g)** The minimum detectable effect is left as an [AUTHOR] slot.
- **Main variation:** dated CoARA action plans within one country and field, with selection into signing modelled. The box claims discrimination only "under stated assumptions".
- **Author's choice:** commit to running the test, or offer it to the field (¶4b.3, Box 2).
- **Why:** contribution 2 survives only if the design survives a methods referee.
- **Not done:** the power calculation needs a pre-specified effect, which only the author (with a collaborator) can set.

**R1-6. The reform movements are allies.** *Accepted. Now in tension with an author decision.*
- **Where:**
  - ¶4c.1 is rewritten along the lines the review proposed;
  - the last sentence of draft 1's ¶4c.4 is rescued into ¶4c.1, and into the EMBO "Rationing is not reform", paragraph 4;
  - the bibliometric counter-pull is named (Abramo 2024, ¶4c.5);
  - Registered Reports and Curry 2018 are dropped;
  - the CoARA count is dated: 994 on 16 October 2026 (R39).
- **Author decision:** an empty Section 4d, "What DORA and CoARA miss". See Section 3, item 6.
- **Why:** many readers of this section work on DORA and CoARA, and the essay's own remedy is theirs.

**R1-7. Too much rests on preprints, news and abstracts.** *Accepted.*
- **Where:**
  - the audit checked every load-bearing claim in the review's table against primary sources wherever this environment could reach them;
  - preprint labels are in the reference list;
  - ¶4a.2 has fewer ideation preprints;
  - the EMBO version has two preprints (Fourie; Zheng et al.).
- **Why:** claims of novelty and the load-bearing facts cannot rest on abstracts.
- **Open:** a few interpretive claims still rest on abstracts: Manabu, Zheng et al., and the draft-2 additions marked [RECHECK].

### Referee 2 (STS and philosophy of science)

**R2-1. The exhibit is a device, not an argument.** *Accepted; (d) is left as an author choice.*
- **(a)** The numbers are in ¶0.1 and Box 1.
- **(b)** The exhibit's point is now its cost and its reading-depth tally.
- **(c)** It is linked to the documentation remedy and to that remedy's limit (Box 1, "Who did what"; Section 6 seeds).
- **(d)** Box 1 offers both commitments as [AUTHOR: choose]: the pledge not to count the essay, and the self-imposed cap. It notes that the cap is itself rationing.
- **Why (d) is not fully accepted:** the task asked for both to be offered. On the essay's own argument, the pledge is the consistent choice.

**R2-2. The human's contribution is not shown.** *Accepted.*
- **(a)** Box 1, "Who did what", gives the thesis's four steps, the decisions recorded in the brief, the agents' proposals the author accepted, and a slot for one the author rejected. It cites Hutchinson.
- **(b)** CRediT is corrected.
- **(c)** Verification is no longer claimed in the past tense: "[AUTHOR: confirm once done]".
- **(d)** "Independently" is deleted.
- **Why:** an essay about unreadable effort cannot misstate its own division of labour.
- **Left to the author:** whether to mark, in the Zenodo version, the sentences they wrote themselves.

**R2-3. Tool choice and conflict of interest.** *Accepted. Independent checks pending.*
- **Where:**
  - Box 1, "Tool", has a slot for the reason the author used a proprietary model, and ¶3.6 points to it;
  - the unfavourable facts are now reported "as the sources state them";
  - ¶5.5 is cut.
- **Pending (author):**
  - a person, or a tool not made by Anthropic, should check the Anthropic passages (Section 5, Figure 2, Box 1);
  - one human reader from outside the project should read the essay.
- **Why:** disclosure is not verification, and the reviewer is the same model family.

**R2-4. §3 is disconnected from evaluation.** *Mostly accepted.*
- **Hook:** Blekhman's five goals open Section 3 (author's decision).
- **(a)** Evidence levels are stated for Swanson ("stayed marginal"), OpenScholar ("on its benchmark"; the Asai et al. quotation is now a paraphrase) and the pivot evidence.
- **(b)** Checkable synthesis also serves evaluators (¶3.3; EMBO "What AI could do").
- **(c)** The illusion of understanding (¶3.3, citing Messeri & Crockett 2024).
- **(d)** ¶3.6 now points forward to Section 4.
- **Not done:** Collins & Evans (2007), which is not in the notes.
- **Why:** the ideal must serve the essay's subject, evaluation.

**R2-5. §5 is off the thesis and quick to date.** *Mostly accepted; the heading is partly declined.*
- **(a)** §5 is rebuilt around the three-level map (¶5.6) and around confidentiality and appropriation (¶5.2b).
- **(b)** Trackers are removed: ¶5.5 is cut; ¶5.4 lost the compute ratio, the human-preference ranking and the per-token prices; and ¶5.1 lost its clause on capability trackers.
- **(c) Corrections:**
  - Apple (¶5.2; Figure 2 caption);
  - X: now only in Figure 2, and about public posts, not chats;
  - "at every firm whose terms were checked";
  - the Bartz wording;
  - "new or resumed" chats;
  - transparency scores dropped;
  - the energy comparison reworded;
  - content rules set by the Chinese state, now quoted from their source (¶5.4).
- **(d)** China:
  - the 2020 reform is reduced to one clause in ¶4c.1, keeping its verified sources;
  - ¶5.4 is now three sentences.
- **Heading partly declined:** "The current trajectory: who owns the tools, and what they learn from users". It keeps the brief's word "trajectory" and drops the informal "we're actually on" and the generic "we". The review's version is offered as an alternative in a comment.
- **Moved:** the recommendation in ¶5.2b, on institutional accounts, is now a Section 6 seed (author's decision).

**R2-6. The two drivers do not match the rival explanation.** *Accepted.*
- **Where:** ¶5.6, replaced with the three-level version (incentives; the technology's own pull; who builds the tools), with these points:
  - the mechanism is the concentration of models more than their ownership;
  - convergence can be tested only where papers name the model they used (Dunivin 2026).
- **EMBO:** the first paragraph of "Will cheap output narrow science?" on drivers.
- **Why:** affordance needed a place, and the external mechanism does not depend on ownership.

**R2-7. Citation-carried prose with a machine rhythm.** *Largely accepted.*
- **(a) Density:** about 160 citations and 25 direct quotations in the master's main text and boxes. The median sentence is 19 words (was 21), and the 90th percentile is 40 words (was 47).
- **(b) The claims register:** it goes to the Zenodo record (Data availability).
- **(c) Rhythm:**
  - the paragraph-final maxims are varied;
  - the triad of scarcities is named once;
  - the staged dialogue and "Hence Zenodo" are gone.
- **(d) Repetition:** the Hansen distinction and the Hao cautions are each stated once.
- **(e) Hedging:** the performative hedges and the throat-clearing are cut.
- **(f) "We":** removed.
- **(g) [AUTHOR] slots:** revised as the review's table suggested. The suspected-AI-review slot is cut; the preregistration is flagged as a decision; redaction and the CC BY question about the notes are added to Data availability.
- **Declined:** the marker-word joke is cut from the master too (the review wanted it kept there). This was for length.

**R2-8. Signalling theory alone.** *Partly accepted.*
- **Where:** a sentence on panels as deliberation in ¶1.3 and in EMBO "The cost was the signal".
- **Not done:** Lamont (2009) is marked [CITATION NEEDED], because it is not in the notes and was not supplied from memory.

---

## 3. Author decisions of 16 October 2026

These were decided by the author, not proposed by the review. They are recorded here as author decisions.

**1. Blekhman (2026), engaged and extended.**
- **The four differences:**
  - **Real research loses its signal too:** ¶0.3, ¶2.7; EMBO opening.
  - **Rationing is the fallback, not prestige:** ¶0.3, ¶4c.5.
  - **The caps are brakes, crude ones,** answering his "no brakes": ¶4c.2b; EMBO.
  - **Field-level data:** ¶2.8–¶2.8b; Figures 3–5.
- **Section 3's hook:** his five goals of biology research.
- **Tao (2026):** verified by research note 8 (arXiv:2608.16753v1, an essay from his ICM 2026 lecture). Its abstract has no output data, so it is no longer cited for the mathematics surge. ¶3.1 cites it only as the parallel to Blekhman's question.

**2. Misuse subsection, "Misuse is the visible tip".**
- **Where:** the end of Section 2 (¶2.9–¶2.10, 244 words) and the EMBO version (124 words). Suchak et al.'s count of 190 runs only to 9 October 2024, and both versions now say so (research note 8).
- **The argument:**
  - misuse is real and well documented;
  - the grey zone of formulaic output (Suchak et al.);
  - gatekeepers cannot separate misuse from legitimate high output, so they ration volume for everyone;
  - misuse is where the problem becomes visible, not where it ends.
- **Sources:** one clause each, not a review.
- **Constraint kept:** the text says that nothing in the data suggests the prolific mathematicians misuse AI. Their papers mention AI tools about as often as the rest (1.9% against 1.6%).

**3. The arXiv mathematics panel as the key figure.** Master Figure 4; EMBO Figure 2; ¶2.8.
- **Numbers:** confirmed at commit 41f795d, so no companion markers remain on them.
- **Exclusions:** October 2026 (2.9%) and first-time authors.
- **Caveats stated:**
  - namesakes (the stricter matching is reported);
  - team size (the rise appears at every size);
  - batch posting (added in this pass);
  - timing: the rise begins seven months before the cap.
- **Wording:** "consistent with AI-assisted production", and strong circumstantial evidence, not proof.
- **Date markers:** dates, not causes. Box 1 discloses that one marker is an Anthropic model release.

**4. Kusumegi et al. (2025): the output-gain claim is dropped.** The author's rule is: "if the results are not clear, we leave it". Renault, Bergeaud & Bosquet (*PNAS* 2026) show that dating adoption by the first month in which a paper is flagged ties the timing to output, which "alone creates spurious evidence of productivity gains". Simulations and placebos give the same pattern. Each of Kusumegi's findings was checked against that critique:
- **Output gain (23.7–89.3%): dropped** from ¶2.2 and ¶4a.5. This is the finding the critique targets.
- **Larger gains for non-native writers: dropped** (¶2.2; Box 2). They are a breakdown of the same contested output estimate. They are replaced by evidence already in the notes:
  - Amano et al. (2023) on the costs non-native scientists pay;
  - Cowgill et al. (2026), where access to ChatGPT made screening *more* accurate for senders from non-English-speaking countries (peer-reviewed; experimental).
  - In Box 2, the language confound now rests on detector bias (Liang et al. 2023) and on Zheng et al.
- **Adopters cite more diverse work: dropped** (¶4a.4). According to research note G3, citation diversity is an outcome of the same within-author event study, with the same adoption dating, so the critique plausibly applies. An author's references can also scale mechanically with output.
  - This was evidence *against* the essay's narrowing hypothesis. Dropping it applies the rule symmetrically. ¶4a.4 still gives the contrary evidence, through Zheng et al.
- **Writing complexity no longer tracks quality: kept** (¶2.2; EMBO "The cost was the signal").
  - According to note G3, this compares papers with and without detected LLM use and does not date adoption, so the timing critique does not reach it. No other critique of it is in the notes.
  - It does not carry the argument alone: in the master, Cowgill et al.'s experiment leads.
  - **Verification pass:** confirm in the *Science* methods (science.org was blocked here) that the complexity analysis is at the level of papers, and note which proxy for quality it uses (R1-4c).
- **Box 2 keeps Renault et al.** as a methods point ("Adoption must be dated independently of output").

**5. Section 6, Recommendations: a placeholder with words reserved.**
- **Master:** "## 6. Recommendations", after Section 5 and before the Conclusion. 700 words are reserved, and the master was trimmed to stay within 7,000 including the reserve.
- **EMBO:** "## Recommendations". 350 words are reserved.
  - It is placed after "Will cheap output narrow science?", which in this version also carries the master's Section 5 material. The order therefore matches the master (rationing; DORA/CoARA; drivers; recommendations; conclusion), and this is also "after the rationing material".
  - Move it directly after "Rationing is not reform" if preferred.
- **Seed lists** (not counted; with sources):
  - the former ¶6.1 in full;
  - the institutional-accounts recommendation from ¶5.2b;
  - the EMBO draft's "three changes";
  - Huang et al.'s three recommendations, credited to them;
  - the proposals of Blekhman, Hansen and Fourie;
  - an index of the others' proposals that Section 4c analyses.
- **Reference budget:** the EMBO seeds note that the version is already at 15 references.
- **Research note 7 is now done:** a menu of 24 recommendations, a shortlist S1–S7, and draft text of about 630 words (master) and 290 words (EMBO). Both placeholders point to it ("Seeds: see research note 7"). Section 6 itself waits for the author's own recommendations.
- **Trims made to fund the reserve in the master:**
  - draft 1's ¶4c.4 (China) reduced to one clause in ¶4c.1, which also removes the unverifiable Shu et al. quotation (R47);
  - ¶5.4 compressed;
  - smaller cuts across ¶0.2 to ¶5.7 and in both boxes, each noted in the paragraph's comment. Among them: the sentence on Thakkar et al.'s review-feedback trial (¶2.3), the closing sentence of ¶2.7, Wiley's licensing figure (¶5.3), per-token prices (¶5.4) and the tracker clause (¶5.1);
  - 16 references that were no longer cited were removed (Section 7).

**6. Section 4d, "What DORA and CoARA miss": empty.**
- **Where:**
  - master: after Section 4c;
  - EMBO: after "Rationing is not reform".
- **Content:** the body is only "[PLACEHOLDER: critique of DORA/CoARA, to be written after discussion with the author]". It has no text and no word reserve.
- **Unchanged:** the existing sentences on DORA and CoARA stay where they are (¶4c.1, ¶4c.5; EMBO "Rationing is not reform").
- **Tension with the review:** R1-6 asked to treat the reform movements as allies, and draft 2 does. A critique section could undo that with the readers most likely to agree.
- **The author's position** (recorded in the brief on 16 October): DORA has become obsolete without ever having been applied.
  - **Never applied:** journal-level metrics still drive evaluation.
  - **Obsolete:** DORA's remedy assumes that an output reflects the work behind it, and that evaluators have time to read it. Generative AI breaks both assumptions.
- **Suggested friendly version:** DORA and CoARA are right about what to stop counting, but their remedy, read more, assumes a reading capacity that AI-era volume consumes. Draft 2's ¶4c.1 already states the second half ("reform depends on the resource that AI-era volume consumes"). Section 4d could develop that point rather than oppose the movements.
- **Sentences to reconcile when Section 4d is written:**
  - **¶4c.1:** it reports that Utrecht University changed practice (Woolston 2021) and that the European Commission found engagement "broad and growing". "Never applied" contradicts both; the approved wording below does not.
  - **EMBO "Rationing is not reform", paragraph 4:** it says "The reform movements are the natural allies."
  - **The Section 6 seed:** "Count less, read what is counted" is CoARA's programme.

  These stay as they are for now, as instructed.
- **Approved wording** (coordinator, 16 October): wherever the text says or implies that DORA or CoARA were not applied, write "largely unimplemented where measured, and mostly unmeasured". The evidence (research note 7, Q5) is to be verified before use:
  - the Journal Impact Factor appears in the review, promotion and tenure documents of 40% of research-intensive US and Canadian institutions, 87% of them supportive (McKiernan et al. 2019);
  - publication counts appear in 95% of biomedical promotion guidelines (Rice et al. 2020);
  - no study compares signatories with non-signatories.

  Neither draft says or implies "never applied", so no sentence was changed. The wording and the evidence are recorded in the comments of both placeholders.
- **Word budget:** none was reserved. In the master, any text in Section 4d needs offsetting cuts (headroom is 18 words); the EMBO version has 346 words of headroom.

**7. The author's field: physics and biology.**
- **Where:** stated in ¶0.3b ("a researcher in physics and biology, an insider to academic evaluation and an outsider to metascience") and in the EMBO opening, paragraph 2. Draft 1's "[AUTHOR: field]" slot had been dropped in draft 2.
- **Field differences, applied from research note 8** (its "What the essay can say" paragraph and sentence list) and from the companion analysis's within-field contrasts:
  - **The verdict:** the author's view holds for output, not for writing, and for experimental work, not for biology or biomedicine as a whole. The essays therefore say "experimental biology is less affected so far, which may mean a later onset rather than immunity".
  - **¶2.8b (master; new):**
    - since 2022 biology has grown no less than physics, and the fields part only in 2026;
    - bioRxiv has grown 10–13% a year since 2023 with no break, although biologists write with LLMs about as much as physicists (Lin & Zhu 2025; Holzwarth et al. 2026);
    - the mechanism: AI cheapens the steps that need only text, code or existing data and can be checked cheaply, and experiments cost what they did;
    - within fields (Figure 5), theoretical physics grew by 20% in 2026, far outside its range since 2017, while experiment stayed within its own; computational biology has outgrown wet-lab biology only since 2025, mostly in bioinformatics, much of which is itself AI research;
    - where no experiment is needed, biomedicine surges: nine heavily mined open health datasets tripled their publications between 2022 and 2025 (Spick et al. 2026), and medRxiv preprints naming a public dataset grew 2.3-fold, against 1.6-fold overall.
  - **EMBO:** the same contrast is in "The cost was the signal", paragraph 4. It answers the experimental biologist's objection that the review raised. The within-field contrast is one sentence there, because the version has no third figure slot.
  - **Other fixes from note 8:**
    - Suchak's 190 runs to 9 October 2024;
    - Nee et al.'s reference is completed, and its figure (about 12% above the counterfactual, January–August 2026) is in ¶2.8;
    - Tao is used only as a parallel to Blekhman's question;
    - the EMBO sentence "most of this is ordinary use, such as language editing" is deleted, because Kobak et al. cannot tell editing from generation;
    - bioRxiv's 2022 base is noted in the figure captions;
    - "checkable results" is added to the technology's pull (¶5.6).
  - **Not applied:**
    - Liang et al.'s preprint identifier: no Liang 2024 or 2025 entry remains in either draft, so there is nothing to correct;
    - Holzwarth et al. in ¶2.1: it was optional, and is used in ¶2.8b instead;
    - Maupin et al. (17-fold redundant NHANES papers): left out for length;
    - Gartenberg et al.'s 42% and the biomedical letters (Cancellario et al.) for "elsewhere": left out for length.
  - **To check:** the 10–13% a year is research note 8's own calculation from bioRxiv's statistics API, cited as "bioRxiv 2026"; confirm it or have the companion analysis report it.
- **Pending:** confirm the wording of the field.

**8. Quotations and Table 1 get a final verification pass.** Appendix A lists every direct quotation in the three outputs, with location, speaker and source URL. Table 1's Source column gives the primary source of each row; the URLs are in the master's reference list (Appendix A.4).

**9. The recommendations research (research note 7) is applied where the coordinator asked.**
- **Pointer:** both Recommendations placeholders now say "Seeds: see research note 7 (shortlist S1–S7 and draft text)", and the seed lists are kept.
- **¶4c.3, pricing:**
  - "refundable deposits" is restored;
  - the [CITATION NEEDED] on fees and poorer researchers is replaced by Hanneke et al.'s sentence on waivers;
  - both are in the full text of Hanneke et al. 2026 (KIT repository copy, https://publikationen.bibliothek.kit.edu/1000195177), which is now noted in the reference;
  - Hanneke et al.'s "screening signal" quotation is also confirmed there, but is not restored, for length.
- **Fourie** is cited for his diagnosis only ("rationed, not priced"), never as a proposer of fees. His second paper, on submission fees at economics journals, is not needed and is not cited.

**10. The closest work is now cited.**
- **Hosseini et al. 2026** (*Research Evaluation*), on "distinctly human contributions": in contribution 2 of ¶0.3, and in the EMBO positioning paragraph and reference list.
- **Lovén 2026 and Ma 2026,** on verification as the new scarce resource: in Box 1, where the record shows that remedy's limit.

**11. The process record is partial, and Box 1 says so.** A NeurIPS 2026 workshop audit found that git captured only 21.8% of one repository's narrative trace (Wu et al. 2026). Box 1 adds that this record includes the decision log kept in the brief, and that it too is partial. EMBO Box 2 says the same in one sentence (ref. 15).

**12. The within-field contrasts are Figure 5 of the master** (companion commit 6021b3a; caption from the README's "Figure 8" section, with the caveats that much of bioinformatics is itself AI research, that experiment is a small series, and that the divergence dates from 2025–2026, not before). Figure 5 replaces the [FIGURE PENDING] note. It is first cited in ¶2.8b, after Figures 3 and 4, so the numbering follows first citation.
- **Pending figure fix:** in Figures 3–5 and S1, the year ticks sit at mid-year, so the ChatGPT marker (30 November 2022) appears just right of the "2022" label. The companion session has been asked to move the ticks to 1 January.

---

## 4. Review points declined or only partly accepted

| Point | What was not done | Why |
|---|---|---|
| E2, master | The exhibit stays first in the master. | The brief makes the essay its own example from the start; R2-1 agrees for the master. |
| E3 | AI-specific rules at bioRxiv and medRxiv, and ERC guidance, are not established. | Not in the notes and not checked here; flagged for the author. |
| R1-3c, R2-8 | Pre-AI rationing precedents and Lamont (2009) are [CITATION NEEDED]. | Not in the research notes; the rules forbid supplying facts from memory. |
| R1-5g | No minimum detectable effect. | It requires a pre-specified effect and a power analysis that only the author and a collaborator can set. |
| R2-1d | Both the pledge and the self-imposed cap are offered. | The task required both as options; the box notes that the cap is rationing. |
| R2-4c | Collins & Evans (2007) not added. | Not in the notes. |
| R2-5 | The §5 heading keeps "trajectory". | It is the brief's word; the review's version is listed as an alternative. |
| R2-7c | The marker-word joke is cut from the master as well. | Length. |
| R1-1, R1-3e | Hakobyan (2026) added, then cut. | Length; its claim rested on an abstract that was not audited. |
| R1-4g | Galdin & Silbert dropped. | Length; Cowgill et al. carry the point with a peer-reviewed experiment. |
| R1-6 | Section 4d will critique DORA and CoARA. | Author's decision (Section 3, item 6). |
| Synthesis §4 | Hanneke et al. replaced by Hosseini et al. among the EMBO references (Asai et al. held the slot in the first EMBO draft). | Hosseini et al. is the closest prior work on invisible effort; Hanneke's distinction is kept in the master. |
| Synthesis §6 | The conclusion no longer ranks proposals. | The proposals moved to Section 6 (author's decision); the conclusion keeps the asymmetry ending. |

---

## 5. Minor points

**Applied:**
- **Quan et al.:** worded as in the abstract (O-08).
- **Butler (2003):** cut. It was sourced from memory and the audit could not verify it (R04).
- **Fanelli's "mistaken":** verified.
- **Thakkar et al.:** "updated", not "improved" (the sentence was later cut for length).
- **NIH and detectors:** ¶2.4 no longer implies that NIH uses detectors.
- **arXiv's computer-science rule:** shows that texts shaped like syntheses became cheap, not mastery (¶2.5).
- **¶4b.1:** "has support", not "well founded".
- **Shah:** cited for fairer quotas (Table 1; Section 6 seeds).
- **Pricing hedge:** the performative hedge is gone, and the claim is now sourced to Hanneke et al.'s sentence on waivers.
- **"None changes how researchers are counted":** applied (¶4c.5).
- **Lock-in:** softened to "the more they favour the incumbents" (¶4c.5).
- **"By rule":** used in Table 1.
- **Herbert et al.:** the comparison is out of Box 1.
- **Table 1:** title fixed.
- **Standfirst:** "caps on submissions", not "caps authors".
- **EMBO wording:** generic "AI conferences"; the triple difference explained in Box 1; no "affordance" or "knowledge extent".
- **Informal heading:** fixed.
- **Section 4's title:** changed.
- **Stack Overflow sentence:** cut.
- **Venue policy:** moved to Data availability.
- **Fourie as the closest precedent:** stated plainly in Box 1.
- **Line notes:** most of R1's and R2's line notes are applied verbatim or nearly so.

**Kept, as the review advised:**
- "Imagine every field with a patient reader…" (¶3.2);
- the researcher's quotation in *Nature* (¶5.2b).

---

## 6. Verification of the review's figures

**Reading-depth tally.** The tally in Box 1 was recounted independently from the outline's claims register (174 claims).
- **Confirmed:** 14 claims (8%) rest on a source read in full and 68 (39%) on an abstract only.
- **Differs:** I count 35 (20%) resting on a primary document, against the review's 40; ten partial readings were classed differently.
- **Also in the register:** 8 claims (5%) rest on a search-engine extract and one on memory.
- **The audit:** 69 claims were flagged for re-checking, and the audit checked every one. Five could not be verified from this environment.

**Process record.** The record in Box 1 was checked against the git history.
- The first commit is at 21:34 UTC on 15 October.
- The outline is at 00:07, and the complete draft at 00:58 on 16 October.
- The review file was committed at 01:30:03. Box 1 uses the brief's figure, 01:29; confirm which time you want.

The cost, about US$153 by 01:30, comes from the session's cost record as relayed by the coordinator.

---

## 7. How the citation audit was applied

**Applied** (all three outputs):
- the replacement wording for every VERIFIED, CORRECTED and DOWNGRADE row that still has a sentence in draft 2;
- the O-items: misquotations fixed (O-02, O-03; the sentence with O-01 is gone), paraphrases tightened (O-04, O-16 to O-19) and citations completed;
- the CN items: missing sources found, such as MOST 2020 and the bioRxiv FAQ;
- the reference corrections in §5: the Korinek & Vipra DOI, Castellacci's eight authors, Singh Chawla 2026a as *Nature Index* news, the Garante entries, and published versions in place of preprint labels;
- Huang et al.'s three recommendations (R38), credited in all three outputs.

**Not applied, and why:**
- **R04 (Butler 2003):** unverifiable, so the sentence is cut.
- **R47 (Shu et al. 2022):** the quotation was confirmed only through *Times Higher Education*. The audit suggested attributing it "as quoted in Lem 2022". Instead, the sentence was cut when ¶4c.4 was reduced to one clause.
- **R86, R87, R89** (Figure 2 caption: Google's assistant default in 2023; Microsoft's dates; OpenAI's advertising dates): kept with [RECHECK]. The sources (the Internet Archive, microsoft.com, openai.com) could not be reached from this environment; the author should check them in a browser.
- **R06, R09, R17 (Kusumegi et al.):** the audit's wording reported the output gain as "contested". The author's decision supersedes it (Section 3, item 4). The output gain, its breakdown by author background (R09) and "adopters appear to produce more" (R17) are dropped.
- **R76 (more diverse citing, verified):** also dropped, under the same decision.
- **O-01 (Dietterich's "small proportion of authors"):** moot. The sentence went when ¶2.6b was rewritten around the companion data.
- **R54, O-21, R59 and R60** (compute ratio, human-preference ranking, tracker history): moot. These passages were cut, and no tracker numbers remain.
- **R57 (one Alibaba flagship went proprietary):** applied, but without the model's name, under the rule against model identifiers.
- **Xu (2026), the end of the CAS journal table (§4.3):** dropped. The source (sfdora.org) could not be read.
- **Hanneke et al.'s "screening signal" and "refundable deposits" (§4.3):** both are now confirmed in the full text (KIT repository copy; research note 7). "Refundable deposits" is restored in ¶4c.3. The screening-signal quotation is confirmed but not restored, for length.
- **Microsoft (2024) blog:** not added. The audit said to add it only after reading it, and microsoft.com returned 403. The Microsoft FAQ is cited instead, with "dates as reported" and R87.
- **OpenAI (n.d.):** removed. The pages could not be read.
- **Russo vs Russo Latona:** the first author's name differs between Crossref and arXiv. This is left as an [AUTHOR] note in the reference list.
- **References the audit verified but draft 2 no longer cites:** removed for length. In this pass they were:
  - Bianchi et al. 2025; Dell'Acqua et al. 2026; Hakobyan 2026; Hatch & Curry 2020; Kapoor & Narayanan 2025;
  - Liang et al. 2025; Lu et al. 2024; Porsdam Mann et al. 2023; Shu et al. 2022;
  - Storey 2026; UKRI 2024; Xizhe Zhang 2026;
  - Bornmann et al. 2021; OpenRouter 2026; Singh Chawla 2026b; Thakkar et al. 2025.

  Several more were removed earlier in draft 2.

**Markers that remain in the master:**
- **Unverifiable:** R86, R87 and R89 (Figure 2 caption).
- **Draft-2 text the audit did not check (descriptive [RECHECK: …] notes):**
  - Adeyeye (¶1.3);
  - Lin 2025 (¶2.9);
  - Messeri & Crockett 2026 and Motoki 2026 (¶4b.1);
  - NIH's simplified review framework (¶4c.2b);
  - Bhargava et al. (¶4c.3b);
  - the primary source of arXiv's endorsement rule (Table 1 note; Figure 4).
- **[CITATION NEEDED]:**
  - Lamont (¶1.3);
  - pre-AI rationing (¶4c.2b; Table 1).

  The article-processing-charges item is resolved by Hanneke et al.; the [RECHECK] notes on Nee et al., Tao and the companion's fig. 7 are gone (the first two verified by research note 8; the fig. 7 clause cut).
- **Incomplete reference entries:** Adeyeye, Bhargava et al., Hosseini et al., Hutchinson, Lovén, Ma, Motoki and Wu et al. still need initials or titles.

The EMBO version has no [RECHECK] markers and one [CITATION NEEDED] (pre-AI rationing).

---

## 8. Actions only the author can take

**Fill the [AUTHOR] slots:**
- your hours, by phase;
- the final cost, including revision and the companion analysis;
- the account type and the setting for training on chats;
- the model and version;
- why you used a proprietary tool;
- one agent proposal you rejected;
- the sources you read in full;
- the validation sentence of the AI-use statement;
- the panel recommendation;
- the non-native-writer sentence;
- the example from your own field;
- where the hypothesis came from (no claim of priority);
- whether EMBL and UPF have signed DORA or CoARA, and whether they provide AI accounts excluded from training, or an institutional model service;
- the minimum detectable effect;
- commit to the test or offer it;
- the commitment in Box 1 (the pledge is the choice consistent with the argument);
- the label of the Anthropic marker in the figure files, and why it is kept;
- one clause on why panel d of the mathematics figure is shown;
- whether you accept the rewording of "efficient models that consume much less";
- the wording of your field;
- name, site and email.

**Write the new sections:**
- Section 6 (Recommendations), in your own words, from the seeds and research note 7;
- Section 4d, after deciding its content, using the approved wording ("largely unimplemented where measured, and mostly unmeasured") once McKiernan et al. 2019 and Rice et al. 2020 are verified. Keep within the budgets: the master has 18 words of headroom.

**Read:**
- Huang et al. in full (before sending the Correspondence);
- Manabu's body;
- the full text of Zheng et al.;
- the Minerva text of Shu et al., only if you want China's reform back in.

**Check:**
- the three unverifiable Figure 2 claims (R86, R87, R89);
- the incomplete reference entries;
- the [CITATION NEEDED] items, if you know sources you have read;
- EMBO Press's AI policy and preprint policy, whether boxes count towards the 3,500 words, and the reference style;
- the ERC's and your national funders' AI guidance (EMBO "Rationing is not reform");
- the bioRxiv growth rates (10–13% a year since 2023), which research note 8 calculated from bioRxiv's statistics API;
- the corrected figures, once the companion session moves the year ticks to 1 January.

**Get outside eyes:**
- a person, or a tool not made by Anthropic, to check the Anthropic passages (Section 5, Figure 2, Box 1) against the primary pages;
- one human reader from outside the project.

**Decide:**
- the title (alternatives are in each file's header);
- the preregistration;
- whether to mark your own sentences in the Zenodo version;
- what to redact from the record, and whether the research notes, which quote paywalled articles at length, can be released under CC BY;
- how EMBL's policy IP71 applies (ask OSIM).

**Timing:**
- send the Correspondence by about 23 October 2026;
- hold the Zenodo preprint until *Nature* decides, and declare the Correspondence in the EMBO cover letter.

---

## 9. Before submission: date-sensitive re-checks

This is the audit's list (its §7), adapted to draft 2. Re-pull or re-read each item in the week of submission, because each can change without notice. Model names are omitted here, as in the drafts; the audit file has the figures.

1. **Capability trackers** (¶5.4, ¶5.7):
   - Epoch AI's estimate that Chinese models trail by about seven months (data insight of 2 January 2026);
   - Epoch AI's 6–12-month lag for small open models.

   The tracker scores, the leader on the capability index, the compute ratio, the human-preference ranking and the per-token prices are no longer in the text.
2. **Counts:**
   - CoARA signatories (994 on 16 October 2026; ¶4c.1);
   - arXiv monthly submissions (40,363 for September 2026 is fixed, but later months may be cited);
   - ICLR 2027 submissions: "more than 62,000" expected, and the final number follows the deadline (Table 1; Figure 1 caption).
3. **Rules that are new or provisional** (Table 1 and text):
   - arXiv's rate limit (a "stopgap");
   - the one-year ban (announced on X, not on arXiv's policy pages);
   - the ACL Rolling Review policy (its page says "Work in progress!");
   - the ICLR 2027 and AISTATS 2027 quotas (AISTATS posted updates on 24 and 30 September 2026);
   - TMLR's quotas;
   - SocArXiv's AI policy (updated 28 September 2026);
   - NIH NOT-OD-25-132;
   - the Chinese thesis-detector rules (CCTV 2026);
   - arXiv's endorsement rule for new mathematics authors (Figure 4; primary source still to find).
4. **Chat-data policies** (¶5.2, ¶5.2b, Figure 2, Box 1):
   - Anthropic's consumer terms and retention;
   - Google's activity default;
   - Microsoft: the FAQ cited covers only the older Copilot app, and a new app has been available since 18 August 2026;
   - Mistral: the page is dated 31 August 2026;
   - Meta: posts updated on 27 March, 8 June and 30 September 2026;
   - OpenAI's training and advertising pages, which were not read here;
   - Apple;
   - Proton.
5. **Litigation and licensing:**
   - the Bartz settlement (first payments expected by 15 November 2026);
   - Wiley's licensing deals (The Bookseller 2024).
6. **Publication status of preprints still cited:**
   - Fourie (v3), Bao et al. (v3), Burtch (v3), Zheng et al., Payan et al., Shah, Castellacci et al., Chesterman & Loy, Dunivin;
   - Shen & Wang, Jegham et al., Lopez-Lira & Seyfi, Atasu;
   - Elazar & Antoniak: accepted at Findings of EMNLP 2026; add pages and DOI when published;
   - draft-2 additions: Adeyeye, Nee et al., Tao, Lin, Lin & Zhu, Holzwarth et al., Lovén, Ma, and Wu et al. (a workshop paper).
7. **Versions of record:**
   - Blekhman: it was an uncorrected proof when read. Re-check "there are no brakes on the system", "paper counts are meaningless" and the five goals.
   - Hao et al.: check "appears to be a major impacting factor" and "remain almost unrelated" in the *Nature* Supplementary Information, not only arXiv v4.
   - Kusumegi et al. against Renault et al.: watch for a reply or correction in *Science* or *PNAS*. None was registered on 16 October 2026.
8. **Reports:** the AI Index 2026 (Stanford HAI) and the Stanford CRFM transparency index. If newer editions appear, say which one is cited.
9. **Companion data** (added to the audit's list):
   - preprint counts were retrieved on 15 October 2026, and a re-pull would complete October and open a new quarter;
   - the within-field counts (commit 6021b3a) were retrieved on 16 October 2026;
   - keep or update the commit references (41f795d; 6021b3a);
   - the bioRxiv yearly growth rates (bioRxiv 2026) come from its statistics API and should be re-pulled;
   - fig. 7 of the companion analysis (computer science outside AI research) is no longer cited.

---

## Appendix A. Direct quotations, for the final verification pass

**Scope.** Every double-quoted passage in the visible text of the three outputs. HTML comments are excluded; the references are excluded except as sources. "Audit" gives the row of `citation_audit.md` that last checked the passage. "Not audited" means the passage is new in draft 2, or was not on the audit's list. Line positions are given by paragraph ID (master) or section and paragraph number (EMBO).

### A.1 Master (`paper/draft_full.md`)

| # | Quotation | Where | Attributed to | Source | Audit and notes |
|---|---|---|---|---|---|
| M1 | "signals are often informative insofar as they require differential knowledge and effort to produce" | ¶1.3 | Cowgill, Hernández-Lagos & Wright (2026), *Management Science* | https://doi.org/10.1287/mnsc.2024.07027 | §4.2 (verbatim in the abstract) |
| M2 | "reversed the relationship between writing complexity and paper quality" | ¶2.2 | Kusumegi et al. (2025), *Science* | https://doi.org/10.1126/science.adw3000 ; read in the author version, https://arxiv.org/abs/2601.13187 | R06 (verbatim in the author version). Check the *Science* text and the quality proxy. |
| M3 | "the use of AI tools has enabled Principal Investigators to submit more than 40 distinct applications in a single application submission round" | ¶2.4 | NIH, NOT-OD-25-132 (2025) | https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html | §4.2 |
| M4 | "substantially developed by AI" | ¶2.4; Table 1 (NIH row) | NIH 2025 | as M3 | §4.2 |
| M5 | "a relatively small number of Principal Investigators" | ¶2.4; Table 1 (NIH row) | NIH 2025 | as M3 | O-16 |
| M6 | "Writing a plausible manuscript is now largely rule-based …; judging one is not" | ¶2.5 | Fourie (2026), arXiv preprint | https://arxiv.org/abs/2607.13844 (v3) | R16. The ellipsis replaces a self-citation, "(Fourie, 2026b)". |
| M7 | "alien" | ¶3.2 | Sourati & Evans (2023), *Nature Human Behaviour* | https://doi.org/10.1038/s41562-023-01648-z | Not audited; a one-word term ("alien" hypotheses). |
| M9 | "can now traverse unfamiliar literature faster" | ¶3.5 | Huang, Hu, Zhang & Lin (2026), *Nature* Comment | https://doi.org/10.1038/d41586-026-02961-z (print PDF) | R19 |
| M10 | "necessarily more preliminary" | ¶4a.1 | Hao, Xu, Li & Evans (2026), *Nature* | https://doi.org/10.1038/s41586-025-09922-y ; author version https://arxiv.org/abs/2412.07727v4 | R22 (arXiv v4). Check the *Nature* text. |
| M11 | "cannot fully identify the causal linkage between AI adoption and scientific impact" | ¶4a.1 | Hao et al. (2026) | as M10 | R22. The source reads "we cannot…" and says it of the whole study. |
| M12 | "collapse into a narrow 'hivemind'" | ¶4a.2 | Bao et al. (2026), arXiv preprint | https://arxiv.org/abs/2606.08251 (v3) | R25 |
| M13 | "no evidence of homogenization in approach or intent" | ¶4a.2 | Burtch (2026), arXiv preprint | https://arxiv.org/abs/2607.13077 (v3) | R29. Source: "I find no evidence of homogenization in approach or intent." |
| M14 | "increasingly published across more intellectually distant fields and entered fields in which they had not previously worked" | ¶4a.4 | Zheng, Hong, Liu & Ni (2026), arXiv preprint | https://arxiv.org/abs/2607.20923 | R30 (abstract) |
| M15 | "ambiguous or negative" | ¶4a.5 | Castellacci et al. (2026), arXiv preprint | https://arxiv.org/abs/2607.24879 | R32 (abstract) |
| M16 | "AI makes extending a familiar research line faster and cheaper than entering unfamiliar terrain, and existing incentive systems reward such speed" | ¶4b.1 | Huang et al. (2026) | as M9 | R02, R33 |
| M17 | "appears to be a major impacting factor" | ¶4b.2 | Hao et al. (2026), supplementary analyses (Supplementary Figs S22–S24 in the author version) | as M10 | R34. Check the *Nature* Supplementary Information. |
| M18 | "remain almost unrelated" | ¶4b.2 | Hao et al. (2026) | as M10 | R34 |
| M19 | "the conceptual distance between a researcher's current and previous work" | ¶4b.2; Section 6 seeds | Huang et al. (2026), third recommendation | as M9 | R38. The source sentence continues "and measures of lasting intellectual disruption…". |
| M20 | "broad and growing" | ¶4c.1 | European Commission, DG Research and Innovation, news item, 25 Jun 2026 | https://research-and-innovation.ec.europa.eu/news/all-research-and-innovation-news/new-study-assesses-progress-reforming-research-assessment-2026-06-25_en | O-03 |
| M21 | "perceived double standard" | ¶4c.2b | Singh Chawla (2026a), *Nature Index* (the journalist's words, not a critic's) | https://doi.org/10.1038/d41586-026-03153-5 | O-02 |
| M22 | "there are no brakes on the system" | ¶4c.2b | Blekhman (2026), *PLOS Biology* | https://doi.org/10.1371/journal.pbio.3004075 | Read in full from the publisher's XML (uncorrected proof). Re-check against the version of record. |
| M24 | "AI support, not AI bans" | Section 6 seeds (moved out of ¶4c.3b for length) | Xuegong Zhang (2026), *Nature* (words from the title) | https://doi.org/10.1038/d41586-026-02631-0 | Not audited |
| M25 | "a tendency towards greater market concentration" | ¶5.1 | Korinek & Vipra (2025), *Economic Policy* | https://doi.org/10.1093/epolic/eiae057 | O-17. Checked against the NBER abstract only; check the journal text. |
| M26 | "On" (the state of the training toggle) | ¶5.2; Box 1 (Conflict of interest); Figure 2 caption | Field (2025), *The Verge* | https://www.theverge.com/anthropic/767507/anthropic-user-data-consumers-ai-models-training-privacy | A secondary source (review, part 5, C10). Confirm against Anthropic's own pages if possible. |
| M27 | "I do not want Claude to start telling people my research results" | ¶5.2b | A researcher quoted by Brzostowicki (2026), *Nature* technology feature | https://doi.org/10.1038/d41586-026-03227-4 | §4.2. Name the speaker if the article does. |
| M28 | "uphold core socialist values" | ¶5.4 | CAC et al. (2023), Interim Measures, Art. 4(1); a translation of 坚持社会主义核心价值观 | https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm | §4.2. A translation; mark "(our translation)" if the journal asks. |
| M29 | "paper counts are meaningless" | Section 6 seeds | Blekhman (2026) | as M22 | §4.2 (uncorrected proof) |
| M30 | "Make new terrain measurable" | Section 6 seeds | Huang et al. (2026), heading of recommendation 1 | as M9 | R38 |
| M31 | "Stop punishing pivots" | Section 6 seeds | Huang et al. (2026), heading of recommendation 2 | as M9 | R38 |
| M32 | "exploratory grants that have extended evaluation horizons" | Section 6 seeds | Huang et al. (2026) | as M9 | R38, O-14. The source reads "funders must create exploratory grants that have…". |
| M33 | "Reward innovation, not just output" | Section 6 seeds | Huang et al. (2026), heading of recommendation 3 | as M9 | R38 |
| M34 | "rationed, not priced" | ¶4c.3; Section 6 seeds | Fourie (2026) | as M6 | R43. The source reads "Review is therefore rationed, not priced". |
| M35 | "enabled Principal Investigators to submit more than 40 distinct applications in a single application submission round" | Table 1 (NIH row) | NIH 2025 | as M3 | A shorter form of M3 |
| M36 | "unmanageable influx" | Table 1 (arXiv computer-science row) | arXiv (2025), blog | https://blog.arxiv.org/2025/10/31/attention-authors-updated-practice-for-review-articles-and-position-papers-in-arxiv-cs-category/ | Table 1 rows checked against primary sources (R78) |
| M37 | "hundreds of review articles every month" | Table 1 (arXiv computer-science row) | arXiv (2025) | as M36 | §4.2 |
| M38 | "incontrovertible evidence that the authors did not check the results of LLM generation" | Table 1 (May 2026 row) | Thomas G. Dietterich, chair of arXiv's computer-science section, X thread of 14 May 2026 | https://x.com/tdietterich/status/2055000956144935055 ; as quoted by Ha (2026), https://techcrunch.com/2026/05/16/research-repository-arxiv-will-ban-authors-for-a-year-if-they-let-ai-do-all-the-work , and Cole (2026), https://www.404media.co/new-arxiv-rules-ai-generated-papers-ban/ | R40, R79. Only the thread's first post could be read; check the full thread. ¶4c.2 now paraphrases it. |
| M39 | "superficial, high-level theory synthesis" | Table 1 (SocArXiv row) | SocArXiv (2026), AI policy | https://socopen.org/ai-policy/ | §4.2. The source capitalises "Superficial". |
| M40 | "The rapid rate of growth in submissions, while exciting, has begun to strain the review system" | Table 1 (ICLR 2027 row) | ICLR 2027 Author Guide | https://iclr.cc/Conferences/2027/AuthorGuide | R82 |
| M41 | "stopgap" | Table 1 (arXiv, 1 Oct 2026 row) | arXiv (2026), blog | https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/ | O-05 |
| M42 | "unsustainable rate of submissions at EMNLP'26" | Table 1 (ACL row) | ACL (2026), Sustainable Reviewing Policy | https://www.aclweb.org/portal/node/14591 ; https://aclrollingreview.org/sustainable-reviewing-2026 | R81 |
| M43 | "Peer review is the scarcest resource of a conference … generative AI tools now make it possible to produce far more manuscripts than the community can carefully evaluate" | Table 1 (AISTATS 2027 row) | AISTATS 2027 call for papers | https://virtual.aistats.org/Conferences/2027/CallForPapers | R83. The ellipsis joins two passages; check their order and the omission. |
| M44 | "NOT intended for" | Data and process availability | bioRxiv FAQ | https://www.biorxiv.org/about/FAQ | R71, CN4 |
| M45 | "permitted with human oversight, verification, and transparency through disclosure" | Data and process availability | Nature Portfolio, AI editorial policy (the "Amber" tier) | https://www.nature.com/nature-portfolio/editorial-policies/ai | O-20 |
| M46 | "how the user evaluated the validity of the tool's outputs" | Data and process availability | PLOS, *PLOS Biology* ethical publishing practice | https://journals.plos.org/plosbiology/s/ethical-publishing-practice | §4.2 |

Rows M8 (Asai et al.) and M23 (Fourie's sentence on the journal's stamp) were removed in the last pass: the first is now a paraphrase, and the second was cut from ¶4c.3. The IDs of the other rows are unchanged.

### A.2 EMBO version (`paper/draft_embo.md`)

| # | Quotation | Where | Attributed to | Source | Audit and notes |
|---|---|---|---|---|---|
| E1 | "no brakes" | Opening, paragraph 2 | Blekhman (2026); a fragment of "there are no brakes on the system" | as M22 | as M22 |
| E2 | "reversed the relationship between writing complexity and paper quality" | "The cost was the signal", paragraph 2 | Kusumegi et al. (2025) | as M2 | as M2 |
| E3 | "a relatively small number of Principal Investigators" | "Rationing is not reform", paragraph 1 | NIH 2025 | as M3 | O-16 |
| E4 | "perceived double standard" | "Rationing is not reform", paragraph 2 | Singh Chawla (2026a) (the journalist's words) | as M21 | O-02 |
| E5 | "rationed, not priced" | "Rationing is not reform", paragraph 4; Recommendations seeds | Fourie (2026) | as M6 | R43 |
| E6 | "the scarcity of interpretive attention" | "Rationing is not reform", paragraph 4 | Hansen (2026), *Research Integrity and Peer Review* | https://doi.org/10.1186/s41073-026-00193-3 | §4.2 |
| E7 | "AI makes extending a familiar research line faster and cheaper than entering unfamiliar terrain, and existing incentive systems reward such speed" | "Will cheap output narrow science?", paragraph 1 | Huang et al. (2026) | as M9 | R02, R33 |
| E8 | "appears to be a major impacting factor" | "Will cheap output narrow science?", paragraph 1 | Hao et al. (2026), supplementary analyses | as M10 | R34 |

**Close paraphrases worth checking with the quotations:**
- "Blekhman (2026) calls arXiv's measures reasonable but aimed at symptoms" ("Rationing is not reform", paragraph 2). The source says they are "reasonable, but they address symptoms rather than the underlying problem".
- Blekhman's five goals ("What AI could do").

### A.3 Correspondence (`paper/correspondence_draft.md`)

The text has no direct quotations. Its first sentence paraphrases the title of Huang et al.'s Comment ("AI can widen science — but only if institutions stop rewarding the already measurable"). Its last sentence refers to their distance indicator ("the conceptual distance between a researcher's current and previous work"; M19) without quoting it. The header comment quotes their three recommendations for the author; that text will not be sent.

### A.4 Quoted strings that are not quotations of a source

These are listed so the verification pass can skip them, or check only what is noted.

- **Options for the author inside [AUTHOR] slots:** ¶4b.3; Box 2; Box 1 (Commitments); ¶C.1; EMBO Box 1 and Box 2. They are the author's own possible wording.
- **"Cap"** (Table 1 caption): the essay's own label.
- **"open"** (¶3.6): scare quotes, echoing the title of Widder et al. (2024), "Why 'open' AI systems are actually closed".
- **"Help improve Claude"** (¶5.2b, inside an [AUTHOR] slot): the name of Anthropic's setting for model improvement. Check the label in the current settings.
- **"AI is destroying the academic system"** (Box 1): the author's first thesis as recorded in `paper/brief.md`, translated from the Spanish planning conversation.
- **"efficient models that consume much less"** (¶5.4, inside an [AUTHOR] slot): the author's wording in the brief, translated.
- **"Will cheap output narrow science?"** (EMBO Recommendations seeds): a section title.

**Table 1 rows and their primary sources** (for the separate check of Table 1):

| Row | Primary source |
|---|---|
| NIH | NOT-OD-25-132 (URL as M3) |
| arXiv, computer science | arXiv blog, 31 Oct 2025 (URL as M36) |
| arXiv ban | Dietterich's X thread (M38) |
| SocArXiv | https://socopen.org/ai-policy/ |
| Chinese universities | CCTV via ScienceNet, https://news.sciencenet.cn/htmlnews/2026/5/565116.shtm |
| TMLR | https://jmlr.org/tmlr/editorial-policies.html ; the start date and growth figures come from Singh Chawla 2026a |
| ICLR 2027 | https://iclr.cc/Conferences/2027/AuthorGuide and /CallForPapers |
| arXiv, all categories | arXiv blog, 1 Oct 2026 (URL as M41) |
| ACL Rolling Review | URLs as M42 |
| AISTATS 2027 | URL as M43 |

The Table 1 note also cites Elazar & Antoniak (https://arxiv.org/abs/2601.17036, v2) and the endorsement rule, which still lacks a primary source.
