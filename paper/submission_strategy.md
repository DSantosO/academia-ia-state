# Submission strategy

*Prepared on 15 October 2026 for a sole author affiliated with EMBL and UPF, and updated the same day after the prior-work check (`research_notes/AI academia essay evidence gaps/6_closest_prior_work.md`).*

*Verification: venue facts were checked on each venue's own pages on 15 Oct 2026. Exceptions are marked **(search summary)**: science.org, pnas.org, cell.com and link.springer.com blocked automated access, so for those the source is a search-engine summary of the venue's own page or the parallel venue notes.*

*Evidence and quotes are in three notes files in `research_notes/AI academia essay evidence gaps/`:*
- *`5_submission_strategy.md` (strategy; §8 covers this update);*
- *`4_journal_venues.md` (venue breadth);*
- *`3_testing_acceleration_hypothesis.md` (the test design).*

*No journal publishes acceptance rates for opinion formats, so the odds below are my judgements from the evidence. The scale is:*
- ***high:*** *more likely than not;*
- ***medium:*** *a real chance;*
- ***low:*** *possible but unlikely;*
- ***very low:*** *a long shot.*

## What changed after the prior-work check

**Three new pieces overlap the essay.**
- **Blekhman (2026), "What is biology research for?"**, a *PLOS Biology* Perspective published on 15 October 2026. It makes the essay's core point for biologists: generative AI "has broken this already-flawed proxy completely" and "paper counts are meaningless". Its competing-interests line reads "RB is a member of PLOS Biology's editorial board". [PLOS Biology](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3004075)
  - **Consequence:** a PLOS Biology Essay built on the same premise is now unlikely. PLOS Biology moves from second to third on the essay ladder, and only as an explicit extension of Blekhman.
- **Huang, Hu, Zhang & Lin (2026), "AI can widen science — but only if institutions stop rewarding the already measurable"**, a *Nature* Comment published on 29 September 2026. It states the essay's §4b claim ("acceleration, not exploration") and blames incentives. [Nature](https://www.nature.com/articles/d41586-026-02961-z)
  - **Consequence:** I drop the Nature Perspective enquiry. The odds for an NHB Perspective fall to low.
  - **Consequence:** the Nature Correspondence should reply to Huang et al., not to Braun.
- **Fourie (2026, arXiv)** already says peer review is "rationed, not priced". It was written with Claude Code and Codex, in a division of labour close to yours. (via 6_closest_prior_work.md)
  - **Consequence:** the rationing argument must cite Fourie. The process record must be pitched as *better documentation*, not as a first.

**What still belongs to the essay** (see the brief's new "Positioning" section):
- reading the caps as **rationing** that restores scarcity by decree;
- a **test** that separates incentives from the pull of data-rich problems;
- the **split between internal and external drivers** of narrowing;
- **legitimacy is irrelevant** to the mechanism;
- a **documented process record**.

**What the strategy now recommends:**
1. Send the Correspondence as a reply to Huang et al.
2. Make **EMBO Reports Science & Society** the first target for the essay. None of the new pieces is in that venue.
3. **A new option, probably the highest-impact one:** run the test as a Registered Report. Nature Human Behaviour accepts secondary analyses of existing data if you have not yet looked at the data.

## Recommendation

The prior-work check changes where your effort pays off most. The essay's premise has now been published in *Nature* (Huang et al., 29 Sep), and so has its "acceleration, not exploration" hypothesis; for biologists the premise also appeared in *PLOS Biology* today (Blekhman). A well-argued essay alone is therefore an opinion piece in a crowded field, with modest odds at top venues, whatever its quality. What remains yours is narrower and stronger. You read NIH's cap, arXiv's rules and conference quotas together as rationing that restores scarcity by decree. You have a test that separates incentives from the pull of data-rich problems. You split the internal and external drivers of narrowing, and you have a documented process record. This week, send a Nature Correspondence of under 200 words that replies to Huang et al. with the rationing point and the test. Before touching any data, write a time-stamped preregistration of the test; it is cheap and makes the design yours. Publish the repositioned essay once, condensed to about 3,500 words. Start with EMBO Reports Science & Society, which is fast, free, open access and untouched by the new pieces. Go to PLOS Biology only after an enquiry that presents the essay as an explicit extension of Blekhman. Post the full essay and the process record on Zenodo. If you can give it several months of computational work, run the test as a Registered Report. That empirical paper, not the essay, is now your realistic route to Nature-portfolio impact. It is also the best answer to the irony critique, because it adds evidence rather than one more opinion.

## The empirical option: run the test

**The design** (from `3_testing_acceleration_hypothesis.md` §5):
- **Basic comparison:** a within-author difference-in-differences around November 2022. Treatment is the intensity of LLM use; the outcome is exploration, measured by distance from the author's own earlier work and by topics new to the author. Reference-based outcomes are primary.
- **The triple difference:** that comparison is run again across incentive intensity:
  - career stage;
  - evaluation regimes that count publications;
  - short- versus long-horizon funding;
  - field crowding.
- **Predictions:** if incentives drive narrowing, AI users narrow more where counting is harsher. If AI simply goes where data are, the effect tracks data availability instead.
- **Data:** the OpenAlex snapshot is free and updated quarterly, and Semantic Scholar offers embeddings.
- **Novelty:** that note and the prior-work check both found **no study** that runs this incentive-heterogeneity test.

**Venues that fit, verified on their own pages:**
- **Nature Human Behaviour, Registered Report.** "We also welcome submissions proposing secondary analyses of existing data sets, provided that the authors have had no prior access to the data in question." Protocols are "provisionally accepted for publication before ... data analysis ... commences". [NHB content types](https://www.nature.com/nathumbehav/content)
- **PLOS Biology, Preregistered Research Article.** These are "peer reviewed prior to conducting experiments, data collection or analysis" and "provisionally accepted". [PLOS Biology](https://journals.plos.org/plosbiology/s/what-we-publish)
- **PLOS Biology, Meta-Research Article.** For work that explores "the systems that evaluate and reward individual scientists or institutions". [PLOS Biology](https://journals.plos.org/plosbiology/s/what-we-publish)
- **Precedents:** comparable empirical work has landed at the top. Hao et al. (2026) is in *Nature*, Kusumegi et al. (2025) in *Science*, and Liang et al. (2025) in *NHB*.

**Impact compared with the essay: much higher, if the design holds.**
- Empirical papers on this topic are cited and covered far more than opinion pieces. Kusumegi et al. had 81 citations within ten months; Hanson et al. have 293.
- An empirical paper is judged on data and methods, so being outside the field matters less.
- A Registered Report makes a null result publishable. That matters, because early evidence points the other way: Zheng et al. (2026) report *more* entry into new fields after 2022, and Kusumegi et al. find more diverse citations among adopters.
- The test could therefore falsify §4b. It would still be a contribution.

**Effort: high.** My estimate is several months of part-time work for a computationally skilled researcher; this is a judgement, not a sourced figure. The work involves:
- disambiguating authors at scale;
- measuring LLM use without the known detector biases;
- building reference-based exploration measures;
- coding incentive regimes;
- handling the threats listed in note 3: selection, detection timing, the productivity confound, text compression, COVID, and arXiv's 2025–26 rule changes.

EMBL's computing resources make this feasible. Scientometrics reviewers will be demanding.

**Risks:**
- **Scooping.** Several well-resourced groups work on this data (Evans, Yin and Ginsparg, Zou, Teplitskiy).
- **Prior access.** The "no prior access" rule means you must not explore the data before submitting Stage 1.
- **Timeliness.** The essay loses currency while the study runs.

**Verdict.** If you can commit the time, do both. The short essay and the Correspondence carry the rationing argument and *announce* the test now. The Registered Report carries the evidence later. A Registered Report is a distinct contribution, so it does not feed the "one more paper" critique the way a second essay would.

**If you do not have the months, skip the empirical paper.** Present the test as a box in the essay and offer it to the field.

**An empirical study is a new decision about authorship.** The single-author choice was made for the essay. For an empirical paper, a scientometrics co-author would raise the odds considerably.

## Submission ladder for the essay (condensed to about 3,500 words)

| Step | Venue and format | Length | Odds | AI policy | Cost | First decision |
|---|---|---|---|---|---|---|
| 1 | **EMBO Reports, Science & Society** (enquiry through eJP) | ≤3,500 words, **≤15 refs** | Medium | Presumed compatible (Springer Nature platform) | No APC for this type | Median 5 days |
| 2 | **PLOS Biology Essay**, only as an extension of Blekhman, after an email enquiry | ~3,500–4,000 words, 30–60 refs | Low–medium (was medium) | Compatible; must describe how outputs were validated | Free (magazine) | ~6 days; review ~42 days |
| 3 | **NHB Perspective**, only if you are *not* doing the Registered Report | 3,000–4,000 words, ~100 refs | Low (was low–medium) | Compatible (Springer Nature "Amber" tier, with disclosure) | Free, but subscription-only | Median 6 days |
| 4 | **eLife Feature** (pitch by email) | <2,000 words, ≤20 refs | Medium | Compatible; describe in Methods | Free | Not stated |
| 5 | **Minerva**, full length (fallback) | 8,000–10,000 words incl. refs | Medium | Compatible; document in Methods "or a suitable alternative part" | Free subscription route; OA via EMBL DEAL or UPF quota | Median 9 days |
| — | ~~Nature Perspective enquiry~~ | — | Dropped | — | — | — |

### Step 1: EMBO Reports, Science & Society

**Why it is first now**
- It is the European life-science forum on research policy and culture.
- Its recent AI pieces take other angles: "Gen AI and research integrity: Where to now?" (2025) and "Peer-review ownership in the AI era" (2026). None of the new close pieces appeared there.
- It is open access, has no APC for this article type, and decides fast: median 5 days to first decision, corrected JIF 6.4. (via 4_journal_venues.md)

**Odds: medium.**
- Review is editor-led ("may be peer-reviewed at the editors' discretion"), and working scientists are its normal authors.
- But the premise is now everywhere, so the first paragraph must say what is new: rationing by decree, and the test.

**Format**
- ≤3,500 words and **≤15 references**. The full bibliography lives in the preprint.
- Presubmission enquiries go through eJP only. "Presubmission enquiries sent via email will not be considered." (via 4_journal_venues.md)

**A 15-reference core** (suggested; adapt):
- Blekhman 2026; Huang et al. 2026; Fourie 2026; Hansen 2026; Manabu 2026; Gartenberg et al. 2026;
- the *Nature* editorial of 25 Mar 2026;
- Kusumegi et al. 2025; Hao et al. 2026;
- NIH NOT-OD-25-132; arXiv's 2025–26 policies;
- Hanson et al. 2024; Smaldino & McElreath 2016;
- one source on the external driver (e.g. Brzostowicki 2026);
- your Zenodo record.

**EMBL and EMBO.** EMBL "was created in 1974 as a 'Special Project' of EMBC ... Today, EMBL is an independent organization", separate from EMBO. (search summary) An EMBL affiliation is not in itself a competing interest (my reading). Declare any EMBO roles.

### Step 2: PLOS Biology, only as an extension of Blekhman

**Why it is still on the ladder.** Your own community reads it. It is open access and free for magazine articles. The Blekhman piece shows the editors want this debate.

**Why the odds dropped to low–medium**
- They published the premise today, from a member of their own editorial board.
- Editors rarely run a second essay on the same thesis within months unless it clearly advances it.

**How to pitch it.** Send a presubmission email to biology_editors@plos.org. Say that Blekhman predicts evaluation will fall back on "older, cruder proxies, such as journal prestige". Argue that the institutional fallback already under way is a different one: rationing by decree. Then add the test.

**Alternative form: a Formal Comment.** These are "peer-reviewed and indexed in PubMed", run to 1,000 words, and "are considered exclusively by invitation". Ask at plosbiology@plos.org. But the format is described as being for "research findings associated with specific articles", so it may not apply to a Perspective. Ask first. Pursue one PLOS piece, not both. [PLOS Biology: what we publish](https://journals.plos.org/plosbiology/s/what-we-publish)

**AI policy and timing**
- PLOS requires disclosure of "the name(s) of any tools used", how they were used, and "how the user evaluated the validity of the tool's outputs". [PLOS AI policy](https://journals.plos.org/plosbiology/s/ethical-publishing-practice)
- Decisions take about 6 days on average, and review about 42 days. [Journal information](https://journals.plos.org/plosbiology/s/journal-information)

### Step 3: NHB Perspective, only if you are not doing the Registered Report

**Odds: low.**
- The format is open: 3,000–4,000 words, about 100 references, peer reviewed. [NHB content types](https://www.nature.com/nathumbehav/content)
- But Huang et al. in *Nature* already carries the incentive claim. NHB editors would see the test as the contribution, and the natural home for a test is a Registered Report.
- If you go empirical, save NHB for that paper and do not spend it on the essay.

**Before submitting, check with EMBL.** EMBL's open-science policy (IP71) applies to "research articles". NHB non-primary content is subscription-only. Ask EMBL's open-science office (OSIM) whether an essay counts. [EMBL IP71](https://www.embl.org/documents/wp-content/uploads/2021/12/Internal_Policy_IP71_Open_Science_and_Open_Access_Pub03122021_Rev01072025.pdf)

### Steps 4 and 5: eLife Feature and Minerva

**eLife Feature**
- Format: "below 2000 words, two display items ... and 20 references".
- No fee. Pitch by email to features@elifesciences.org. [eLife](https://elife-rp.msubmit.net/html/elife-rp_author_instructions.html)
- **Odds: medium.** The format is too short to carry the test, so the piece would lose much of its depth.

**Minerva** (fallback for the full essay)
- **Format and reach:** 8,000–10,000 words including references, double-blind review, JIF 2.9. Reach is low outside science studies. (via `journals.md`)
- **Odds: medium.**
- **Use it if:** steps 1–4 all fail, or you want the five-section argument peer-reviewed at full length.

**Still avoid:**
- **Cell Press titles.** Elsevier's "limited, supportive" wording is a grey zone for drafting by agents.
- **Issues in Science and Technology, Times Higher Education and SocArXiv**, which reject AI-drafted text.
- **MDPI and Frontiers.**

## The Nature/Science question

**The honest answer has changed.** In 2026 Nature's magazine sections have already covered the essay's thesis from several angles:
- the 25 Mar Editorial on AI papers and the effort–value link;
- Zhang's World View (22 Jun);
- Messeri & Crockett's Comment (19 May);
- Braun's Comment (1 Sep);
- Huang et al.'s Comment (29 Sep).

**Nature**
- **Comment, World View and Opinion stay closed:** "Unsolicited contributions are not accepted." [Nature: other submissions](https://www.nature.com/nature/for-authors/other-subs)
- **The Perspective enquiry, which was very low before, is now not worth sending.**
- **Correspondence is the one open door, and it now has a better target** (next section). It brings a Nature-branded marker of the argument but little reach: recent examples drew 1,300–5,700 accesses, and Huang et al.'s Comment itself had 2,685 by 15 Oct. [Nature metrics](https://www.nature.com/articles/d41586-026-02961-z/metrics)

**Science**
- **The editorial page** remains a very long shot. It takes 720 words, no references, exclusive. Thorp: "We don't take most of what we get." [Thorp](https://www.science-forever.com/p/what-we-look-for-in-editorials-for)
- **Letters** need something "published in Science in the past 3 months" or a recent event of general interest. I verified no recent Science piece to hang a Letter on. (search summary)

**PNAS.** Opinions of about 1,500–2,000 words accept proposals and are screened with Pangram, an AI-text detector. This remains an alternative, not a lead. (search summary)

**The realistic route to Nature-family impact is now empirical.** An NHB Registered Report is the main option. Nature or Science are possible only if the result is striking, as with Hao et al. (*Nature*) and Kusumegi et al. (*Science*).

## The companion short piece: reply to Huang et al.

**Why Huang et al. rather than Braun**
- Nature's Correspondence page sets **no time limit** for responses. It states only that silence after 3 weeks means no.
- Huang et al. is two weeks old; Braun is six weeks old. Two Correspondences on the same theme (Hutchinson, 29 Sep; Motoki, 6 Oct) have appeared since Braun's Comment; whether they reply to it is not verified, because they are paywalled.
- More importantly, Huang et al. make exactly the claim your test addresses. Their recommendations seen so far (subsidising new data infrastructure; no longer penalising pivots) correspond to the two rival explanations, data affordance and incentives. Your test tells which lever matters.

**The point to make, in under 200 words with two references** (Huang et al., plus NIH's notice or Nature's 15 Oct news on arXiv's cap):
1. Huang et al. ask institutions to stop rewarding the already measurable.
2. So far institutions have rationed instead. NIH caps applicants at six a year, arXiv at two submissions a month, and AI conferences use quotas. This restores scarcity by decree and leaves what is rewarded untouched.
3. Whether incentives or the pull of data-rich problems drive narrowing can be tested: compare AI adopters' exploration where counting is harsher (untenured researchers, publication-counting regimes, short grant cycles) with where it is softer. That is a triple difference with open bibliometric data, and it says which of their levers to pull.

**Mechanics**
- Nature allows "further citations ... for fact-checking purposes", so add links for the caps.
- Read Huang et al. in full first. The prior-work check saw only two of their three recommendations.
- Write it yourself; if you use AI, add the required one-line footnote.
- **Send by 23 Oct. If you have not heard by about 13 Nov, it is declined.**

**Holding back the preprint.** Nature says "An article making a similar point to the Correspondence should not be published in another outlet until the Correspondence is published". Hold the public preprint until the Correspondence is decided.

**Output cap**
- Without the empirical study: one Correspondence, one essay, one preprint.
- With it: add the Registered Report, which is the only further paper that adds evidence.
- Say so in the paper.

## How the essay maps onto the 3,500-word version

| Full essay | EMBO Reports version (~3,500 words) | Correspondence |
|---|---|---|
| §1 The system and its pre-AI strain | ~300 words: shared premise, citing Blekhman, Hansen, Manabu, Gartenberg et al. and the *Nature* editorial | — |
| §2 Cheap outputs; legitimacy is irrelevant | ~800 words: the three scarcities, including the time it takes to master a literature | — |
| §4c, rewritten as **rationing** | ~800 words: NIH cap, arXiv's rules of Oct 2025, May 2026 and Oct 2026, conference quotas; extends Fourie; pricing as the counter-proposal | Point 2 |
| §4a–b, acceleration and **the test** | ~800 words plus a box: Huang et al. as the claim, Hao et al. as the evidence, the triple difference (preregistration DOI if done) | Point 3 |
| §5 Two drivers (internal and external) | ~400 words | — |
| §3 The ideal | ~200 words as the payoff, or cut | — |
| Box: How this paper was made | ~250 words: time, cost, record DOI, the Anthropic note; presented as documentation, not a first | Footnote |

**Wording note:** call the test "discriminating" rather than "decisive". Incentive intensity can correlate with how data-rich a field is, and reviewers will say so.

## Next steps

| When | What |
|---|---|
| **By 23 Oct 2026** | Read Huang et al. in full, plus Blekhman, Fourie, Hutchinson and Motoki. Write and send the **Nature Correspondence**. Email **EMBL OSIM** (osim@embl.org, per `journals.md`) with two questions: does IP71 cover a peer-reviewed essay, and are there AI guidelines for authors? **Decide whether to go empirical.** |
| By 30 Oct | Compile the **time-and-cost record**. If going empirical, write a **time-stamped preregistration** of the triple-difference design *before* touching any data, because NHB's "no prior access" rule applies. |
| 26 Oct–13 Nov | Finish the repositioned full essay. Cut the 3,500-word EMBO version. Archive the process record. Draft the cover letter. |
| ~13–16 Nov | Once the Correspondence is decided, post the **full essay and record on Zenodo**. Send an **EMBO Reports** presubmission enquiry through eJP, then submit. |
| Dec 2026–Feb 2027 | If EMBO declines: PLOS Biology enquiry (as a Blekhman extension), then eLife, then Minerva. |
| Nov 2026–Mar 2027, if empirical | Write the Stage 1 Registered Report (rationale, hypotheses, design, analysis plan, robustness and placebo checks) for **NHB**, or a PLOS Biology Preregistered Research Article. |
| Spring 2027 | **Metascience 2027** (Montreal, 14–16 June; call not yet published). Present the design, or the Stage 1 protocol if accepted. |
| At each acceptance | Contact the **EMBL Press Office** (media@embl.org) and UPF communications. Do not solicit media before acceptance (Nature Portfolio policy). |

### Presubmission enquiry angle

> Recent pieces argue that AI breaks the link between effort and merit (Blekhman, *PLOS Biology*, 2026) and that incentives steer it towards exploiting familiar work (Huang et al., *Nature*, 2026). I take two further steps. First, the institutional response so far is rationing: NIH's cap of six applications per investigator, arXiv's monthly limit and conference quotas restore scarcity by decree while leaving what is counted unchanged. Extending Fourie (2026), I argue that pricing or redesign would do better. Second, the incentive explanation can be tested against its main rival, that AI simply flows to data-rich problems, with a triple difference that compares AI adopters' exploration across harsher and softer counting regimes [preregistered: DOI]. The essay was made with AI agents under my direction and documents its own production ([hours], [€], record DOI).

### Cover letter: five bullets

- **What it adds** to Blekhman (2026), Huang et al. (2026), Fourie (2026) and Gartenberg et al. (2026): the institutional response is rationing by decree, not reform of what is counted.
- **A discriminating test.** A triple difference by the strength of metric incentives separates the incentive explanation from the pull of data-rich problems [preregistration DOI].
- **Legitimacy is irrelevant to the mechanism.** Honest, disclosed use erodes three scarcities: writing effort, reviewer time and the time it takes to master a literature.
- **A documented case.** The paper was made with AI agents under my direction and is disclosed under [journal]'s policy. The process record is archived [DOI], with time and cost reported. This is better documentation of a practice others have also disclosed (e.g. Fourie 2026), not a first.
- **Vantage point and disclosures.**
  - I am a life scientist at EMBL and UPF, outside metascience.
  - A related Correspondence is with *Nature*.
  - EMBL and EMBO are separate organisations; list any EMBO roles.
  - Transparency note: the paper was drafted with Claude (Anthropic) and discusses Anthropic's data policy.

## What would change the recommendation

- **No time for data work.** Skip the empirical option and keep the test as a box. The essay and Correspondence plan stands, and the essay's ceiling is EMBO Reports or PLOS Biology.
- **A co-author.**
  - For an empirical study, a scientometrics co-author raises the odds at NHB and PNAS, and at Nature or Science if the results are striking.
  - For the essay, a co-author would still change the single-author design.
- **Someone runs the test first.** Then the essay's second contribution weakens. Keep the rationing synthesis and cite them.
- **The Huang Correspondence.** If it is published, cite it in every later cover letter. If it is declined, the PLOS Formal Comment enquiry becomes the short-piece alternative, provided the points do not repeat.
- **OSIM's answer on IP71.** If subscription-only publication is a problem, it only matters for the NHB steps.
- **Your field.** If computational or machine learning, the empirical route is the obvious choice, and NMI or NCS become alternatives to NHB. If wet-lab biology, EMBO Reports and eLife fit best.
- **A new Nature or Science piece on caps or rationing.** Reply to that instead.
- **The time-and-cost figures.** If they are striking, lead every pitch with them.
- **Career evaluation (ANECA).** If it matters, prefer peer-reviewed article types. A Registered Report is the strongest of these.

## Key sources (accessed 15 Oct 2026)

**New prior work**
- [Blekhman 2026, PLOS Biology](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3004075)
- [Huang et al. 2026, Nature](https://www.nature.com/articles/d41586-026-02961-z)
- [Nature Editorial, 25 Mar 2026](https://www.nature.com/articles/d41586-026-00934-w)
- [Fourie 2026](https://arxiv.org/abs/2607.13844)

**Nature and Nature Human Behaviour**
- [Nature other submissions](https://www.nature.com/nature/for-authors/other-subs)
- [Nature Portfolio AI policy](https://www.nature.com/nature-portfolio/editorial-policies/ai)
- [Nature press and embargo policy](https://www.nature.com/nature-portfolio/editorial-policies/press-and-embargo-policies)
- [NHB content types (including Registered Reports)](https://www.nature.com/nathumbehav/content)

**PLOS Biology**
- [What we publish (Formal Comments, Preregistered and Meta-Research Articles)](https://journals.plos.org/plosbiology/s/what-we-publish)
- [PLOS AI policy](https://journals.plos.org/plosbiology/s/ethical-publishing-practice)

**Other venues and policies**
- [EMBO Reports guidelines](https://link.springer.com/journal/44319/submission-guidelines)
- [eLife](https://elife-rp.msubmit.net/html/elife-rp_author_instructions.html)
- [EMBL IP71](https://www.embl.org/documents/wp-content/uploads/2021/12/Internal_Policy_IP71_Open_Science_and_Open_Access_Pub03122021_Rev01072025.pdf)
- [EMBL OA agreements](https://www.embl.org/about/info/szilard-library/open-access/open-access-agreements-with-publishers/)
- [Thorp on Science editorials](https://www.science-forever.com/p/what-we-look-for-in-editorials-for)
- [SocArXiv AI policy](https://socopen.org/ai-policy/)
- [Metascience 2027](https://metascience.info/)
