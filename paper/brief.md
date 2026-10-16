# Author's brief

The author's decisions from the planning conversation (15 Oct 2026). The outline, draft and reviews must follow this file. If a proposal here came from the assistant and not the author, it is marked *(proposal)* and the author can override it.

## Thesis

**Current wording, refined by the author:**

> The academic system is not prepared for a world in which AI is used generally.

In the author's words (translated from Spanish): "The key of what I want to expose is not that writing papers with AI is bad, nor that it produces poor-quality papers. I want to expose that the system is not prepared for a world in which AI is used in a general way."

**What this means:**

- AI makes the things the system counts (papers, reviews, grant applications) almost free to produce. It therefore speeds up a failure that was already under way.
- The failure does not depend on misuse. Even good, legitimate use of AI breaks the system, because the system's signals of merit and its gatekeeping rely on scarcity:
  - the effort of writing;
  - reviewers' time;
  - the time it takes to master a literature.
- The paper is not arguing either of these:
  - that AI-assisted writing is wrong;
  - that AI-made papers are low quality.

**How the thesis evolved:**

1. "AI is destroying the academic system."
2. The author accepted that this was an oversimplification.
3. "Almost free to produce, so it speeds up a failure that was already under way."
4. "The system is not prepared for general AI use; even good use breaks it."

## The paper as its own example (author's decision)

**What the author decided:**

- The paper is made with AI and says so openly, as part of the argument rather than as a confession.
- It should be a well-justified paper made with AI that carries the author's ideas: the good way of using AI. It is still part of the problem it describes, and it should say so.

**Why it is still part of the problem:**

- It is one more paper in a system that counts papers.
- Nobody can read the effort from the text.
- Reviewers cannot see who did what.

**What the paper needs:**

- A "How this paper was made" box or section *(proposal)*.
- A contribution statement in CRediT style *(proposal)*. The division of labour:
  - **The author:** the thesis, the structure, the key judgments, final revision and accountability.
  - **AI agents:** literature search, citation checks, first drafting, and an internal adversarial review.
- The process record: this repository's git history documents every step *(proposal)*.
- A record of the time and cost it took to produce the paper. This could be the paper's most telling data point *(proposal; the author must supply or confirm the figures)*.
- A conflict-of-interest note: the paper is drafted with Claude (Anthropic) while discussing Anthropic's data policy. The author wants to state this openly and use it as evidence of where science is heading.

## Agreed structure

1. **How the system works.** Papers, peer review, metrics, points, grants and publish-or-perish. It was already strained before AI.
2. **AI makes what the system counts almost free to produce.** This speeds up the failure.
   - Emphasise legitimate use over misuse *(proposal, following from the refined thesis)*:
     - writing no longer signals merit (Kusumegi et al. 2025, Science);
     - NIH's cap of six applications per PI;
     - the load on reviewers;
     - AI-written reviews.
   - Treat paper mills and fraud as a secondary amplifier.
3. **What AI could do for science: the ideal.**
   - An optimistic, normative essay. It does not need to be proven, but it should be labelled as a vision.
   - Theme: information overload and interdisciplinarity. AI could help researchers stay knowledgeable across fields.
   - Ground each ideal in a mechanism that already exists. The author asked to keep these references:
     - Sourati & Evans 2023 (human-aware AI aimed at gaps between research communities);
     - Swanson's literature-based discovery;
     - OpenScholar (Asai et al. 2026), which synthesises the literature with correct citations.
4. **What AI is actually doing: acceleration, not exploration, and governance that cannot redirect it.** One section with three sub-parts.
   - **4a. The evidence.** Open with Hao, Xu, Li & Evans 2026 (Nature): AI-using scientists publish about 3× more papers and get about 5× more citations, while the range of topics science covers shrinks. Check the final numbers against the Nature version. Support with Messeri & Crockett 2024 and Kusumegi et al. 2025.
   - **4b. The author's hypothesis:** "scientists use AI to speed up what they already know how to do, not to explore."
     - The author acknowledges this is their own interpretation and will defend it.
     - Present it as an argued hypothesis, not as a finding.
     - Add a box on how it could be tested.
     - Mechanism: the incentives from section 1 steer AI towards producing more of the same.
   - **4c. Governance.** Reform is voluntary (DORA, CoARA), designed before AI, and limited to disclosure rules.
5. **"The trajectory we're actually on"** (the author agreed it is more than "limitations").
   - Compute, models and chat data are concentrating in a few companies.
   - Sections 3 and 5 are two sides of the same coin: section 3 is the ideal, section 5 the current trend. They do not contradict each other.
   - Distinguish the internal driver of narrowing (section 4: academic incentives) from the external driver (section 5: corporate control of the tools).
   - **Anthropic as the example of direction.** The author wants to use Anthropic's 2025 change (training on consumer chats by default, with an opt-out) as the example of where US companies are heading.
     - Frame it according to the evidence: did Anthropic lead, or converge late?
     - Do not claim Claude is "the most advanced by far" unless independent trackers support it.
   - **Chinese models as a different direction.**
     - The author's understanding (translated): China is betting on very efficient models that are not yet as powerful but consume much less.
     - Test this against research note 2 and word it accordingly.
     - Also note: open weights but not open data, and state content control.
   - **Open alternatives** (public models, efficient open-weight models that universities could run themselves) are the bridge back to section 3.
6. **Other agreements:**
   - Park et al. 2023 ("papers becoming less disruptive") can be included, but it is not the main topic. Cite it together with its critics.

## Format defaults (the author can override)

- English; about 6,500–7,500 words; essay or perspective format; author–year citations.
- **First person singular ("I")** *(proposal; changed from the earlier "we")*. A single human author is accountable. "We" in an AI-assisted paper could read as naming the AI as a co-author, which COPE and publisher policies do not allow.
- Do not tailor the paper to one journal yet. The target journal will be chosen from `paper/journals.md`. Note where to cut for a 3,000–4,000-word version.

## Authorship (author's decisions)

- **Single author.** The author will write the paper alone, with no co-author.
- **Affiliations:** EMBL (European Molecular Biology Laboratory) and UPF (Universitat Pompeu Fabra, Barcelona).
- **Field:** not stated. It is probably life sciences or computational biology; confirm before the paper says anything about the author's field.
- **Framing:** the author is an outsider to metascience and science studies, but an insider to academia, working at a leading international research institute. If the paper mentions this, it does so in the "How this paper was made" box *(proposal)*.

## Target venue (author's preferences)

- The author wants the greatest possible impact, in a scientific, international venue.
- The author is new to the field and doubts Nature or Science would accept the paper, but wants them seriously considered.
- The submission strategy is in `paper/submission_strategy.md`; the list of venues is in `paper/journals.md`.
- If the strategy recommends a specific format (for example a shorter Perspective or a companion short piece), the outline should say how the full essay maps onto it.

### Working plan from the strategy (15 Oct 2026; the author has not yet confirmed it)

1. **Write one master text:** the full essay, ≤7,000 words, which also fits a Nature Perspective synopsis enquiry. It goes on Zenodo as a preprint, together with the process record. Timing:
   - after the Nature Correspondence (item 4) is published, or after 3 weeks without a reply;
   - SocArXiv bans AI-written paragraphs and arXiv's computer-science categories need prior peer review, so neither is used.
2. **Make one condensed version (~3,800 words) and submit it once.** The ladder:
   - optional Nature Perspective synopsis enquiry →
   - Nature Human Behaviour Perspective →
   - PLOS Biology Essay →
   - EMBO Reports Science & Society (≤3,500 words, 15 references) →
   - eLife Feature →
   - Minerva at full length, as a fallback only.

   Whether NHB or PLOS Biology goes first depends on EMBL's open-science policy (IP71); the author must ask EMBL's open-science office (OSIM).
3. **No parallel second paper.** Two peer-reviewed versions of one argument would invite the irony critique. Both the journal researcher and the strategist agree; the coordinator agrees too.
4. **Optional Nature Correspondence** (<200 words, ≤2 references), replying to Braun's Nature Comment of 1 Sep 2026 on accountability, by about 23 Oct 2026. The Correspondence rule is that a similar point must not appear elsewhere until it is published.
5. **Positioning.** The field is crowded. The paper must cite and set itself apart from:
   - Hansen 2026 (RIPR, "Symbolic scarcity and epistemic waste");
   - Manabu 2026 (Postdigital Science and Education, "The Machine Consumes Itself");
   - the 2026 Nature pieces by Messeri & Crockett, Braun, Hutchinson and Motoki (see `research_notes/.../5_submission_strategy.md` and `6_closest_prior_work.md`).
6. **The time-and-cost record is essential.** Without it, the "paper as its own example" is only an anecdote. The author must log their own hours; compute costs can be taken from the session records.

The outline must therefore:
- structure the full essay (≤7,000 words);
- mark the cuts for the ~3,800-word version, and further cuts down to 3,500 words and 15 references for EMBO Reports;
- state the single point the Correspondence would make.

### Update after the prior-work check (15 Oct 2026; supersedes items 2 and 4 above)

- **Revised essay ladder** (about 3,500 words):
  1. EMBO Reports Science & Society (≤3,500 words, ≤15 references). This is now the primary submission.
  2. PLOS Biology, framed as an extension of Blekhman 2026.
  3. NHB Perspective, only if the author does not go empirical.
  4. eLife Feature.
  5. Minerva at full length, as a fallback.

  The Nature Perspective enquiry is dropped: Nature has covered the thesis five times in 2026.
- **Correspondence:** reply to Huang et al. (Nature Comment, 29 Sep 2026), not to Braun.
  - Send by about 23 Oct 2026.
  - The author must read Huang et al. in full first.
  - Hold the preprint until the Correspondence is decided.
- **Empirical option (author to decide):** run the discriminating triple-difference test as a Registered Report, at NHB or as a PLOS Biology preregistered or meta-research article. This is probably the highest-impact path, and it takes months.
  - Registered Reports require *no prior access to the data* used for the test, so preregister before exploring them.
  - The other chat's descriptive arXiv and bioRxiv counts should be kept separate from the test's data, or declared.
- **Wording:** call the test "discriminating", not "decisive", because incentive strength can correlate with how data-rich a field is.

## Positioning after the prior-work check (coordinator's adjustments, 15 Oct 2026)

Source: `research_notes/AI academia essay evidence gaps/6_closest_prior_work.md`. The author's thesis and five-section structure stay. What changes is which claims the essay presents as its own contribution.

**Present as shared ground and cite generously; do not claim these as new:**
- The core premise (AI breaks the link between effort and merit; the system was already strained). Cite:
  - Hansen 2026 (RIPR);
  - Manabu 2026 (PSE);
  - Blekhman 2026 (PLOS Biology Perspective, published 15 Oct 2026);
  - Gartenberg et al. 2026 (Organization Science);
  - the Nature Editorial of 25 Mar 2026;
  - Hanneke et al. 2026 (BISE editorial);
  - Kusumegi et al. 2025;
  - Parrilla 2023.
- "Acceleration, not exploration" (§4b). Huang, Hu, Zhang & Lin (Nature Comment, 29 Sep 2026) state it almost word for word. The author's hypothesis stands, but present it as a view others now share. **The contribution is the decisive test:** a triple difference by the strength of metric incentives, which separates the incentive explanation from the "AI goes where data are" explanation.
- The vision depending on open tools (§3/§5). Cite Spirling, Palmer et al., and the Nature feature on local models.
- **The paper as its own example.** Precedents exist:
  - Osmanovic Thunström 2022;
  - Cotton et al. 2023;
  - Porsdam Mann et al. 2023;
  - Agents4Science 2025;
  - the Sakana AI Scientist;
  - Fourie 2026, which was written with Claude Code and Codex in a similar division of labour;
  - Manabu 2026.

  Present this paper's process record (git history, time and cost, verification steps, the Anthropic conflict of interest) as better documentation, never as a first.

**What the essay can claim as its contribution** (no "first" claims; use hedged wording):
1. **Legitimacy is irrelevant to the mechanism.** The breakdown needs no misuse. Treat the time it takes to master a literature as one of the gatekeeping signals that disappears.
2. **Rationing.** Read the system's responses together (NIH's cap of six applications, arXiv's rules of Oct 2025, May 2026 and Oct 2026, conference caps) as rationing that restores scarcity by decree instead of reforming what is counted. Hansen 2026 is the foil: Hansen wants to abolish scarcity. Fourie 2026 says review is "rationed, not priced".
3. **Two drivers of narrowing:** internal (academic incentives) and external (corporate concentration of the tools and of chat data). Each has been argued separately; the split appears to be new.
4. **The decisive test** for the incentive explanation (Box 2).
5. **A documented, reproducible process record** as evidence of what one evening of AI-assisted work now produces.

**Update §4c.** "Limited to disclosure rules" is out of date. There are now binding caps and proposals for fees and AI triage; these are the rationing evidence.

**Use** the draft 163-word contribution paragraph in the note as the starting point.

## Author decisions, 16 Oct 2026

- **Blekhman 2026** (PLOS Biology; summary in `paper/sources/`). Include it and extend it. The author finds it interesting but limited. The essay should go beyond it on four points:
  - **Real research loses its signal too.** Blekhman's case is the hollow paper with no research behind it. The essay's case is real research whose effort becomes invisible.
  - **The fallback is rationing.** Blekhman predicts a return to journal prestige; the essay shows rationing is the fallback already under way.
  - **The caps are brakes.** Blekhman says the system has "no brakes"; the caps are brakes, just crude ones.
  - **Field-level data.** Blekhman has no data of his own; the essay does.

  Use his five goals of biology research as the hook for section 3.
- **Misuse.** Add a short subsection at the end of section 2: "Misuse is the visible tip". About 250–350 words in the full version and 100–150 in the EMBO version. Do not over-cite, since misuse is well researched.
  - **Key point:** gatekeepers cannot separate misuse from legitimate high output, so they ration by volume. Misuse is where the problem becomes visible, not where it ends.
  - **Constraint:** never imply that prolific authors in the arXiv mathematics data are misusing AI.
- **The arXiv mathematics figure** (share of papers with an author who has 5 or more papers in the quarter) is the author's key figure. The author reads it as a sign of AI-assisted production. The essay words it as "consistent with" that reading, pending robustness checks (name homonyms, team size, concentration).

## Author decisions after the citation audit (16 Oct 2026)

1. **Kusumegi et al. 2025: drop the productivity/output-gain claim.** The critique by Renault, Bergeaud & Bosquet (PNAS, Aug 2026) is now peer-reviewed. The author's rule: "if the results are not clear, we leave it". Kusumegi's other findings stay only if that critique does not plausibly apply to them.
2. **Add a "Recommendations" section** (§6, before the Conclusion). It draws on a research pass (`research_notes/.../7_recommendations.md`) and on the author's own recommendations, which are still to come. Credit prior proposers: Huang et al. made three recommendations; also Blekhman, Hansen and Fourie.
3. **Field differences.** The author's field is physics and biology. Their view is that biology is not yet feeling this as much as other fields. Check it against the evidence: `research_notes/.../8_field_differences.md`, plus companion-analysis contrasts (bioRxiv computational vs wet-lab categories; arXiv theory vs experiment archives). Word it at the strength the evidence supports.
4. **Quotations and Table 1** (the conference and arXiv rules) get a final, careful verification against primary sources after the revision.
5. **A critique of DORA and CoARA** goes in as §4d, "What DORA and CoARA miss". The author wants it and will discuss the content later, so the section is left EMPTY in both drafts. The referee advised treating them as allies; the critique can be friendly.

   Seed material for that discussion (not in the drafts):
   - **Voluntary, uneven, pre-AI.** Uptake is voluntary and uneven; the European Commission's 2026 baseline study calls engagement "broad and growing" but progress uneven. Neither framework was designed for generative AI.
   - **Their remedy assumes reading capacity.** "Count less, read more" assumes reviewers and panels have time to read, and AI-era volume consumes exactly that capacity.
   - **Attacked from both sides.** Some call the reform administrative capture (Baccini 2025); others call it anti-metric "bibliometric denialism" (Abramo 2024; Torres-Salinas et al. 2023). The reform also has a professionalised evaluation community behind it (Rushforth & Hammarfelt 2023).
   - **Narrative CVs rest on thin evidence** (Bordignon et al. 2023), and early signs suggest they may disadvantage non-native writers. That disadvantage may now be offset, or reversed, by LLM writing help.
   - **Plenty of signatures, little evidence of effect.** CoARA has 994 signatories, but there is no study showing that DORA signatories changed how they hire.

   Sources are in `research_notes/AI disruption of academia literature/4_governance_and_reform.md` and `paper/reviews/citation_audit.md`.

## Sources

- Earlier bibliography: `reports/AI disruption of academia literature.md` and `research_notes/AI disruption of academia literature/`.
- Gap research: `research_notes/AI academia essay evidence gaps/`. It covers:
  - chat-data policies;
  - Chinese models and the frontier ranking;
  - testing the acceleration hypothesis;
  - journal venues.
- Keep the earlier verification flags. Do not quote a number whose summary was written from memory and not re-checked, unless it is checked again.
