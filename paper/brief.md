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

## Sources

- Earlier bibliography: `reports/AI disruption of academia literature.md` and `research_notes/AI disruption of academia literature/`.
- Gap research: `research_notes/AI academia essay evidence gaps/`. It covers:
  - chat-data policies;
  - Chinese models and the frontier ranking;
  - testing the acceleration hypothesis;
  - journal venues.
- Keep the earlier verification flags. Do not quote a number whose summary was written from memory and not re-checked, unless it is checked again.
