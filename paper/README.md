# Paper workspace: status

*Updated 16 Oct 2026, about 09:45 UTC. Branch `claude/eloquent-pasteur-cck04w`.*

## What is here

| File | What it is | Status |
|---|---|---|
| `brief.md` | The author's decisions: thesis, structure, positioning, every choice made in conversation. **Authoritative.** | Current |
| `outline.md` | Source-mapped outline: 44 planned paragraphs and a register of 174 claims | Superseded by the drafts; kept for traceability |
| `draft_full.md` | **Master essay**: "The cost was the signal: why academic evaluation is not ready for AI used well". For the Zenodo preprint, with Minerva as fallback. | 6,982 of 7,000 words, counting the 700 reserved for §6; revised and verified |
| `draft_embo.md` | **EMBO Reports, Science & Society**: "Rationing is not reform: academic evaluation after AI made writing cheap" | 3,156 of 3,500 words, counting the 350 reserved for §6; 15 references |
| `correspondence_draft.md` | **Nature Correspondence** replying to Huang et al. (Nature Comment, 29 Sep 2026) | 186 words; 2 references |
| `journals.md`, `submission_strategy.md` | Venue comparison and submission strategy, updated after the check of closest prior work | Current |
| `figures/` | Companion-analysis figures (SVG/PDF/PNG at 85 and 175 mm), with captions and methods in `README_companion_analysis.md` | Year ticks fixed (companion commit cb56c25) |
| `sources/` | Blekhman 2026 (PLOS Biology, CC BY): PDF and summary | — |
| `reviews/` | `referee_report.md` (internal adversarial review), `citation_audit.md`, `final_verification.md`, and `response_to_reviews.md` (point-by-point responses, the "Before submission" checklist and the quotation appendix) | Complete |

The figures:
- **Figure 3:** new preprints by field, index with 2022 = 100.
- **Figure 4:** arXiv mathematics profile, including the share of papers with an author who has 5+ papers. This is the author's key figure.
- **Figure 5:** within-field contrasts (bioRxiv computational vs wet lab; arXiv theory vs experiment).

Research notes are in `../research_notes/`, in two folders: the literature search and the evidence gaps (notes 1–8).

## State of the drafts

- **Checks done:**
  - an internal adversarial review (editor and two referees);
  - a citation audit (89 flagged claims: 57 verified, 23 corrected, 4 softened, 5 unverifiable);
  - a final verification (52 quotations checked, 51 exact and 1 corrected; all 10 rows of Table 1 checked against primary sources).
- **Open sections:**
  - **§4d, "What DORA and CoARA miss"**: empty by design, to discuss. Seed material and the author's position ("obsolete without ever being applied"; defensible wording: "largely unimplemented where measured, and mostly unmeasured") are in `brief.md`.
  - **§6, Recommendations**: a placeholder that awaits the author's own recommendations. The seeds are research note 7 (shortlist S1–S7 and draft text).
- **Markers left:**

  | Marker | Full | EMBO | Correspondence |
  |---|---|---|---|
  | `[AUTHOR]` | 58 | 35 | 7 |
  | `[RECHECK]` | 12 | 1 | 0 |
  | `[CITATION NEEDED]` | 6 | 2 | 0 |

## Submission plan (details in `submission_strategy.md`)

1. **Nature Correspondence** replying to Huang et al., by about 23 Oct. Read Huang et al. in full first. Hold the preprint until this is decided.
2. **Essay** (about 3,500 words), submitted to one journal at a time, in this order:
   1. EMBO Reports, Science & Society;
   2. PLOS Biology, framed as an extension of Blekhman 2026;
   3. NHB Perspective, only if there is no Registered Report;
   4. eLife Feature;
   5. Minerva, at full length.
3. **Full essay and process record on Zenodo.** Not SocArXiv, which bans AI-written paragraphs. Not arXiv, whose CS categories need prior peer review for position papers.
4. **Optional, and the highest-impact route:** a Registered Report that runs the discriminating test, at NHB or as a PLOS Biology preregistered article.
   - It needs no prior access to the test data.
   - It reopens the question of a co-author.

## What only the author can do

1. Send your recommendations for §6, and discuss §4d.
2. Read the key comparisons in full:
   - Huang et al. 2026, all three recommendations;
   - Manabu 2026, the body of the paper;
   - Hosseini et al. 2026;
   - Zheng et al. 2026;
   - every source you will quote.
3. Ask EMBL's open-science office (OSIM) whether an essay falls under IP71 (immediate open access). The answer decides between NHB and PLOS Biology.
4. Fill the `[AUTHOR]` slots:
   - your own hours;
   - the model and version used;
   - your Claude account type and model-improvement setting;
   - personal examples from physics and biology;
   - choices: titles, pledge vs self-imposed cap, whether the endorsement rule counts as a gate, figures for EMBO.
5. Decide: the Correspondence (yes/no), and the Registered Report (yes/no).
6. Revise the text yourself and check the claims you rely on. The argument depends on the human contribution being real and visible, and the AI-use disclosure stays.
7. In the week you submit, re-check the date-sensitive claims (listed in `reviews/response_to_reviews.md`, "Before submission").
8. Zenodo: archive a snapshot of the repository, choose the licence, and decide which notes to make public.

## Process record (for Box 1; author to confirm or update)

- **Timeline (UTC):**
  - 15 Oct, about 21:25: essay requested.
  - 21:34: first literature notes committed.
  - 16 Oct, 00:07: outline.
  - 00:58: first full draft.
  - 01:29: internal review.
  - About 01:30–07:15: pause (usage limit).
  - 07:15–09:45: citation audit, revision, field and recommendations research, companion figures, final verification.
- **Compute (this session, subagents included):** US$267 as of 09:33 UTC on 16 Oct. Tokens: about 5.9M input, 4.4M output and 521M cache reads. The companion analysis session that produced the figures is separate; its cost is in its own record.
- **Work units:** about 20 subagents (research, strategy, outline, drafting, review, audit, verification). 37 commits on this branch before this README.
- **Reading depth** (Box 1): of 174 registered claims, the sources were read as follows:
  - 14 (8%) in full;
  - 35 (20%) as primary documents;
  - 68 (39%) from the abstract only;
  - 8 (5%) from a search extract;
  - 1 from memory.
