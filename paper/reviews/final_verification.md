# Final verification pass: quotations, Table 1, Kusumegi et al., references, consistency and limits

- **Files checked:** `paper/draft_full.md` (master), `paper/draft_embo.md` (EMBO Reports), `paper/correspondence_draft.md` (Nature Correspondence). Lists used: `paper/reviews/response_to_reviews.md`, Appendix A; earlier audit: `paper/reviews/citation_audit.md`.
- **Verifier:** AI agent (Claude, via Claude Code), working for the author. The drafts were edited only to correct errors.
- **Access date:** every source below was read on **16 Oct 2026** unless a row says otherwise.
- **Method:** each source was downloaded and searched for the exact quoted string, after normalising whitespace and line-break hyphens. Pages that blocked access are named, and nothing was circumvented.
- **Commits:** the draft edits are in commit 360e80d ("Work-in-progress: final verification edits to drafts"), made outside this pass. This log was not committed.

## Summary

- **Quotations:** 52 entries were checked (master 44, EMBO 8, Correspondence 0).
  - **OK:** 51. **FIXED:** 1 (M27, attribution). **PARAPHRASED:** 0. **UNVERIFIABLE:** 0.
  - Several OK entries rest on an author version or a secondary source. Their notes say so: M2/E2, M10, M11, M17, M18, E8 and M38.
- **Table 1:** 10 rows and 2 rules that are described only in the note and the figures were checked. All 12 match their primary sources in substance.
  - **Fixed in the table:** 3 cells (ban row, ICLR row, ACL row).
  - **Fixed in the note and the Figure 4 caption:** the [RECHECK] on arXiv's endorsement rule is resolved, because the primary source was found (arXiv blog, 10 Dec 2025).
  - **Fixed in the text:** 1 sentence describing a rule (¶2.4, NIH's detection technology).
- **Kusumegi et al.:** the complexity–quality reversal does **not** rely on dating each author's adoption, so it is **kept**. It is a paper-level comparison; see §4.
- **References:** all 8 incomplete entries are completed (§5).
  - **Two references added** to the master: arXiv 2025b and 2025c, the primary sources found for Table 1. The existing arXiv 2025 becomes arXiv 2025a.
  - **One broken URL fixed:** ICLR's author guide. This also affects a link in the Correspondence's fact-check list.
- **Other errors found and fixed:**
  - ¶2.1: Springer Nature's current AI policy no longer exempts copy editing from disclosure.
  - Box 1: Wu et al.'s 21.8% was misread.
  - EMBO: Holzwarth et al.'s date was stated imprecisely.
- **Limits, after the edits:**
  - Master: 6,982 words of 7,000, with §6 counted at its 700-word reserve (headroom 18).
  - EMBO: 3,156 words of 3,500, with its 350-word reserve (headroom 344), and 15 references (limit 15).
  - Correspondence: 186 words of text (limit under 200) and 2 references (limit 2).

---

## 1. Change log

Each change gives the file, its location, the text before and after, the source and the access date (16 Oct 2026 for all).

| # | File | Location | Before | After | Source (URL; accessed 16 Oct 2026) and reason |
|---|---|---|---|---|---|
| C1 | draft_full.md | ¶2.1, last sentence | "Springer Nature does not even ask authors to declare AI-assisted copy editing (Nature Portfolio n.d.)." | "Springer Nature classes polishing language with an LLM as permitted, low-risk use (Nature Portfolio n.d.)." | https://www.nature.com/nature-portfolio/editorial-policies/ai . The page now uses a risk framework. Its Green tier reads "Green-Permitted: Assistive AI use (low risk)", with the example "Using an LLM to polish or refine the language" and "Compliance and disclosure: Permitted. Disclosure enhances trust and transparency…". Under "Authors" it says "Disclose AI use for trust and transparency". No exemption for copy editing remains, so the cited source no longer supports the old sentence. Word count is unchanged (15 words). |
| C2 | draft_full.md | ¶2.4, last sentence | "Enforcing its originality rule would need detectors, which drift as authors drop the words that give them away (Geng & Trotta 2025)." | "NIH says it uses detection technology to identify AI-generated applications, but detectors drift as authors drop the words that give them away (Geng & Trotta 2025)." | NOT-OD-25-132, https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html : "NIH will continue to employ the latest technology in detection of AI-generated content to identify AI generated applications". The internal review (R1 minor 6) had asked whether the notice says this. It does, so "would need detectors" understated the source. +4 words. |
| C3 | draft_full.md | ¶5.2b | "…my research results", one researcher told *Nature* (Brzostowicki 2026). | "…my research results", the neuroscientist Ian Gaudet told *Nature* (Brzostowicki 2026). | https://www.nature.com/articles/d41586-026-03227-4 : "Gaudet, a neuroscientist at Florida Atlantic University in Boca Raton, prefers to stay offline. 'I do not want Claude to start telling people my research results,' he explains." The article names the speaker (Appendix A, M27). +2 words. |
| C4 | draft_full.md | Box 1, Record | "in one audit, git captured only 21.8% of a repository's narrative trace (Wu et al. 2026);" | "in one audit, only 21.8% of a repository's narrative trace remained visible in its current version (Wu et al. 2026);" | https://neurips.cc/virtual/2026/166237 (abstract): "85.6% of the lines ever committed to the prescriptive trace are visible at the current revision … the narrative trace records episodes and shows 21.8%." Git's history holds all committed lines; 21.8% is the share still visible in the current version. +4 words. |
| C5 | draft_full.md | Table 1, May 2026 row, Stated reason | "Unchecked LLM output (hallucinated references, leftover prompts)" | "Unchecked LLM output (hallucinated references, leftover chatbot text)" | The thread as quoted by Cole, *404 Media*, 15 May 2026, https://www.404media.co/new-arxiv-rules-ai-generated-papers-ban/ : "hallucinated references, meta-comments from the LLM ('here is a 200 word summary; would you like me to make any changes?'; 'the data in this table is illustrative, fill it in with the real numbers from your experiments'". Both examples are chatbot output, not prompts. Blekhman (2026) also writes "leftover chatbot instructions", and the change matches ¶2.9's "leftover chatbot text". |
| C6 | draft_full.md | Table 1, ICLR 2027 row, Measure | "…; excess submissions randomly desk-rejected; only authors with such an acceptance may review" | "…; excess submissions randomly desk-rejected; each submission must register an author with such an acceptance to review, unless no author has one" | https://iclr.cc/Conferences/2027/AuthorGuidelines : "all submissions must have at least one author who is registered to review at least 3 papers. The registered reviewer should be qualified to review, and they are qualified if they have at least one accepted publication at one of the following venues"; "If none of the authors are qualified under this definition, then they are exempt from this requirement … such submissions are capped at one per author". The guide also says "All authors who are on 3 or more papers must serve as a reviewer for at least 6 papers", with no condition of qualification. The old wording followed Singh Chawla's news summary ("only authors who have had a paper accepted at a major AI conference can review submissions"), not the primary source the cell cites. |
| C7 | draft_full.md | Table 1, ACL row, Stated reason | "38% of ~17,000 May 2026 submissions from authors with no publication record" | "38% of ~17,000 May 2026 submissions from authors with no available publication record" | https://www.aclweb.org/portal/node/14591 and https://aclrollingreview.org/sustainable-reviewing-2026 : "38% of the ~17K May 2026 submissions came from authors with no available publication record". Dropping "available" turned missing data into a claim about the authors. |
| C8 | draft_full.md | Table 1, note | "arXiv's reported changes to endorsement and language requirements rest on a secondary source and are excluded; the companion analysis marks a tighter endorsement rule for new mathematics authors on 10 Dec 2025 (Figure 4) [RECHECK: primary source for this rule]." | "arXiv's changes to endorsement (a tighter rule for new authors, in mathematics from 10 Dec 2025, the date marked in Figure 4, and in all sections from 21 Jan 2026; arXiv 2025c) and to language requirements (a full English version of every submission from 11 Feb 2026; arXiv 2025b) are not listed [AUTHOR: list the endorsement rule as a gate? It was left out when only a secondary source was known; arXiv's own announcements are now cited]." | Both changes have primary sources on arXiv's blog. **Endorsement:** https://blog.arxiv.org/2025/12/10/updated-endorsement-policy-for-arxiv-mathematics/ ("As of December 10th, 2025, the arXiv Mathematics section will no longer accept institutional email addresses … as the sole qualifier for an automatic endorsement for new authors"; its edit note reads "As of January 21, 2026, the endorsement policy has been updated for all arXiv sections"). See also https://blog.arxiv.org/2026/01/21/attention-authors-updated-endorsement-policy/ . **Language:** https://blog.arxiv.org/2025/11/21/upcoming-policy-change-to-non-english-language-paper-submissions/ ("arXiv will require that all submissions have a full English-language version"; edited notes give the start as 11 Feb 2026) and https://blog.arxiv.org/2026/01/13/non-english-paper-submission-guidelines/ . Whether to list the endorsement rule is left to the author, because the only stated reason for leaving it out (a secondary source) no longer holds. The table is excluded from the word count. |
| C9 | draft_full.md | Figure 4 caption | "(10 Dec 2025) [RECHECK: primary source for this rule]" | "(10 Dec 2025; arXiv 2025c)" | As C8. |
| C10 | draft_full.md | ¶2.5; ¶4c.2; Table 1 (arXiv computer-science row); Data and process availability | "(arXiv 2025)" (3×); "arXiv 2025 (primary)" | "(arXiv 2025a)" (3×); "arXiv 2025a (primary)" | A consequence of C8 and C11: three arXiv blog posts from 2025 are now cited, lettered chronologically as for Garante 2023a/b and Meta 2025a/b. The word count is unchanged. |
| C11 | draft_full.md | References | "arXiv (2025). Attention authors: updated practice for review articles…" | "arXiv (2025a). …" (unchanged otherwise); **added:** "arXiv (2025b). Attention authors: upcoming policy change to non-English language paper submissions (K. Boboris). arXiv blog, 21 Nov 2025 (edited 13 Jan and 11 Feb 2026; policy in effect from 11 Feb 2026). [URL] (accessed 16 Oct 2026)" and "arXiv (2025c). Attention authors: updated endorsement policy for arXiv Mathematics (K. Boboris). arXiv blog, 10 Dec 2025 (with an edit noting the extension to all sections on 21 Jan 2026). [URL] (accessed 16 Oct 2026)" | URLs as in C8. Both posts are by Kat Boboris and were read in full. |
| C12 | draft_full.md | References, Adeyeye | "Adeyeye [initials to fill] (2026)." | "Adeyeye, E. (2026)." | Crossref, https://api.crossref.org/works/10.2139/ssrn.7259758 : author "Elijah Adeyeye"; the title matches the entry. |
| C13 | draft_full.md | References, Bhargava et al. | "Bhargava [initials to fill] et al. (2026). [Title to fill]. *Management Science* 72:7381–7393." | "Bhargava, H. K. et al. (2026). Fighting fire with fire: infusing artificial intelligence into peer review to sustain quality scholarship. *Management Science* 72(9):7381–7393." | Crossref, https://api.crossref.org/works/10.1287/mnsc.2026.00184 : "Fighting Fire with Fire: Infusing Artificial Intelligence into Peer Review to Sustain Quality Scholarship"; eight authors (first: Hemant K. Bhargava); volume 72, issue 9, pages 7381–7393, September 2026. |
| C14 | draft_full.md, draft_embo.md (ref. 6) | References, Hosseini et al. | "Hosseini [initials to fill], … & Holmes [initials to fill] (2026). … *Research Evaluation* 35." | "Hosseini, M., … & Holmes, K. (2026). … *Research Evaluation* 35:rvag020." | Crossref, https://api.crossref.org/works/10.1093/reseval/rvag020 : Mohammad Hosseini, Brian D. Earp, Sebastian Porsdam Mann, Kristi Holmes; volume 35, article rvag020; online 11 Apr 2026. |
| C15 | draft_full.md | References, Hutchinson | "Hutchinson [initials to fill] (2026). … *Nature* (Correspondence), 29 Sep 2026." | "Hutchinson, P. (2026). … *Nature* 658:286 (Correspondence, 29 Sep 2026)." | Crossref, https://api.crossref.org/works/10.1038/d41586-026-03055-6 (Phil Hutchinson; 658(8134):286; online 29 Sep 2026); the article page gives the type as "Correspondence". |
| C16 | draft_full.md | References, Lovén | "Lovén [initials to fill] (2026). … arXiv:2605.02566. Preprint." | "Lovén, L. (2026). … arXiv:2605.02566 (v3). Preprint." | arXiv API, https://export.arxiv.org/api/query?id_list=2605.02566 : Lauri Lovén; v3 of 19 Jul 2026. |
| C17 | draft_full.md | References, Ma | "Ma [initials to fill] (2026)." | "Ma, J. W. (2026)." | arXiv API (id 2605.10425): Jiaqi W. Ma; v1 of 11 May 2026. |
| C18 | draft_full.md | References, Motoki | "Motoki [initials to fill] (2026). … *Nature* (Correspondence), 6 Oct 2026." | "Motoki, F. Y. S. (2026). … *Nature* 658:572 (Correspondence, 6 Oct 2026)." | Crossref, https://api.crossref.org/works/10.1038/d41586-026-03175-z (Fabio Y. S. Motoki; 658(8135):572; online 6 Oct 2026); the article page gives the type as "Correspondence". |
| C19 | draft_full.md | References, Wu et al. | "Wu [initials to fill], Huang [initials to fill] & Geng [initials to fill] (2026). [Title to fill]. Paper at the NeurIPS 2026 Workshop on AI-Native Academia." | "Wu, K., Huang, Z. & Geng, H. (2026). What Git does not record: provenance legibility in two AI-assisted research repositories. Paper at the NeurIPS 2026 Workshop on AI-Native Academia: Authorship, Peer Review, and Conference Governance under AI." | https://neurips.cc/virtual/2026/166237 : "What Git Does Not Record: Provenance Legibility in Two AI-Assisted Research Repositories"; Koutian Wu, Zesen Huang, Hejia Geng; "NeurIPS'26 Workshop on AI-Native Academia: Authorship, Peer Review, and Conference Governance under AI". |
| C20 | draft_full.md | References, ICLR 2027 | "ICLR 2027 author guide; … https://iclr.cc/Conferences/2027/AuthorGuide ;" | "ICLR 2027 author guidelines; … https://iclr.cc/Conferences/2027/AuthorGuidelines ;" | The old URL returns HTTP 404. The ICLR 2027 site links its guide at /Conferences/2027/AuthorGuidelines, page title "ICLR 2027 Author Guidelines". |
| C21 | correspondence_draft.md | Header comment, fact-check links to send to *Nature* | "ICLR 2027 author guide, https://iclr.cc/Conferences/2027/AuthorGuide ;" | "ICLR 2027 author guidelines, https://iclr.cc/Conferences/2027/AuthorGuidelines ;" | As C20. This link is meant to go to *Nature* with the submission. The comment is not part of the text or the word count. |
| C22 | draft_embo.md | "The cost was the signal", paragraph 4 | "…and most biomedical papers published in 2025 show signs of it (ref. 15)." | "…and by the end of 2025 most biomedical papers showed signs of it (ref. 15)." | Holzwarth et al., https://arxiv.org/abs/2608.10715 (abstract): "by the end of 2025, 89% of papers show excess of LLM-associated vocabulary". The source dates the share to the end of 2025, not to all papers published in 2025. +2 words. |
| C23 | draft_embo.md | References, ref. 9 (Kusumegi et al.) | "…*Science* 390:1240–1243. doi:10.1126/science.adw3000" | "…*Science* 390:1240–1243. doi:10.1126/science.adw3000 (author version: arXiv:2601.13187)" | The quotation (E2) could be checked only in the authors' accepted version, https://arxiv.org/abs/2601.13187 ; science.org returns HTTP 403. The master's reference already names the author version, and the EMBO reference now does too. The reference count is unchanged (15). |
| C24 | draft_full.md | ¶2.2 comment (HTML; not counted) | "…so the critique does not reach it [verification pass: confirm in the Science methods]." | "…so the critique does not reach it (confirmed in the final verification pass, 16 Oct 2026: …; see paper/reviews/final_verification.md)." | Records the result of §4. |
| C25 | draft_full.md, draft_embo.md | Word-count comments (HTML; not counted) | Master: §2 1,247/1,292; §5 753/850; Box 1 583/777; raw total 7,576; Table 1 813/828; captions 1716/1771; 153 references. EMBO: 3,154/3,309; headroom 346; "The cost was the signal" 738. | Master: §2 1,251/1,296; §5 755/852; Box 1 577/781; raw total 7,586; Table 1 842/876; captions 1718/1767; 155 references; a method note added. EMBO: 3,156/3,311; headroom 344; "The cost was the signal" 740. | Recounted by script after the edits (§7). The master's prose total stays at 6,982, because the earlier script had overcounted Box 1 by 10 words (§7). |

---

## 2. Quotations: statuses

Statuses: **OK** (verbatim, rightly attributed, context not distorted); **FIXED** (correction applied; see §1); **PARAPHRASED** (quotation marks removed and reworded); **UNVERIFIABLE** (quotation marks removed and flagged). Locations follow Appendix A of `response_to_reviews.md`. Every quotation listed in Appendix A was found, and the visible text holds no other quotation: a script listed every double-quoted string in the three files, and the rest are author options, labels or titles (Appendix A.4).

### 2.1 Master (`draft_full.md`)

| # | Quotation (short) | Where | Attributed to | Status | Source checked | Notes |
|---|---|---|---|---|---|---|
| M1 | "signals are often informative insofar as they require differential knowledge and effort to produce" | ¶1.3 | Cowgill et al. 2026 | OK | *Management Science* abstract via Crossref (doi:10.1287/mnsc.2024.07027) | The source begins with a capital "Signals". The 4–9% figure and the gain for senders from non-English-speaking countries (¶2.2) also match. |
| M2 | "reversed the relationship between writing complexity and paper quality" | ¶2.2 | Kusumegi et al. 2025 | OK | Author version, arXiv:2601.13187v1: abstract and main text ("LLM use has reversed the relationship between writing complexity and paper quality") | science.org returns HTTP 403, and Crossref and PubMed hold only the one-line summary, so the *Science* wording itself could not be read. The quality proxy is publication in a peer-reviewed venue by June 2024 (ICLR 2024 review scores as a check). On the design, see §4. |
| M3 | "the use of AI tools has enabled Principal Investigators to submit more than 40 distinct applications in a single application submission round" | ¶2.4 | NIH 2025 | OK | NOT-OD-25-132 | The source introduces it with "there is evidence that"; "reported that" is fair. |
| M4 | "substantially developed by AI" | ¶2.4; Table 1 | NIH 2025 | OK | NOT-OD-25-132 | The source also covers applications that "contain sections substantially developed by AI". |
| M5 | "a relatively small number of Principal Investigators" | ¶2.4; Table 1 | NIH 2025 | OK | NOT-OD-25-132 ("Based on recent data, this limit will affect a relatively small number of Principal Investigators") | |
| M6 | "Writing a plausible manuscript is now largely rule-based …; judging one is not" | ¶2.5 | Fourie 2026 | OK | arXiv:2607.13844v3 full text | The ellipsis replaces "(Fourie, 2026b)", a self-citation, and the semicolon is kept. |
| M7 | "alien" | ¶3.2 | Sourati & Evans 2023 | OK | Article page abstract: "scientifically promising 'alien' hypotheses unlikely to be imagined or pursued…" | |
| M9 | "can now traverse unfamiliar literature faster" | ¶3.5 | Huang et al. 2026 | OK | Online text and print PDF (media.nature.com magazine-assets) | |
| M10 | "necessarily more preliminary" | ¶4a.1 | Hao et al. 2026 | OK | arXiv:2412.07727v4 ("Just accepted by Nature") and *Nature*'s published Peer Review File (MOESM3), which quotes the revised introduction | The *Nature* main text is paywalled. |
| M11 | "cannot fully identify the causal linkage between AI adoption and scientific impact" | ¶4a.1 | Hao et al. 2026 | OK | As M10 | Said of the whole study, as the draft says. |
| M12 | "collapse into a narrow 'hivemind'" | ¶4a.2 | Bao et al. 2026 | OK | arXiv:2606.08251v3 abstract | The source's double quotation marks around "hivemind" become single ones inside the quotation. |
| M13 | "no evidence of homogenization in approach or intent" | ¶4a.2 | Burtch 2026 | OK | arXiv:2607.13077v3 abstract | |
| M14 | "increasingly published across more intellectually distant fields and entered fields in which they had not previously worked" | ¶4a.4 | Zheng et al. 2026 | OK | arXiv:2607.20923v1 abstract | |
| M15 | "ambiguous or negative" | ¶4a.5 | Castellacci et al. 2026 | OK | arXiv:2607.24879v1 abstract | |
| M16 | "AI makes extending a familiar research line faster and cheaper than entering unfamiliar terrain, and existing incentive systems reward such speed" | ¶4b.1 | Huang et al. 2026 | OK | Online text and print PDF | In the print layout, an illustration credit interrupts the sentence; the wording is unchanged. |
| M17 | "appears to be a major impacting factor" | ¶4b.2 | Hao et al. 2026 | OK | arXiv v4 main text and the Peer Review File ("[Page 6 in the Main Text, Results…]") | The words are in the main text, where they summarise supplementary analyses; they are not in the *Nature* Supplementary Information PDF (MOESM1). "In Hao et al.'s supplementary analyses" is still a fair attribution of the finding. |
| M18 | "remain almost unrelated" | ¶4b.2 | Hao et al. 2026 | OK | As M17 | |
| M19 | "the conceptual distance between a researcher's current and previous work" | ¶4b.2; §6 seeds | Huang et al. 2026 | OK | Print PDF | The source continues "and measures of lasting intellectual disruption…". |
| M20 | "broad and growing" | ¶4c.1 | European Commission 2026 | OK | News item of 25 Jun 2026 ("engagement with CoARA and ARRA is broad and growing"; "Progress remains uneven") | |
| M21 | "perceived double standard" | ¶4c.2b | Singh Chawla 2026a (the journalist's words) | OK | Nature Index, 13 Oct 2026 | |
| M22 | "there are no brakes on the system" | ¶4c.2b | Blekhman 2026 | OK | Local PDF and the live PLOS page (still "an uncorrected proof" on 16 Oct 2026) | The source says "in biology research, there are no brakes on the system". Elsewhere the essay presents Blekhman as writing about biology, and NIH's cap applies there, so the context is not distorted. The author may add "in biology research" (3 words). |
| M24 | "AI support, not AI bans" | §6 seeds | Xuegong Zhang 2026 | OK | Title of the Correspondence of 25 Aug 2026 | |
| M25 | "a tendency towards greater market concentration" | ¶5.1 | Korinek & Vipra 2025 | OK | *Economic Policy* abstract via Crossref ("…a tendency towards greater market concentration and natural monopolies in the future"); NBER abstract | academic.oup.com returns HTTP 403; the journal abstract was read through Crossref. |
| M26 | "On" | ¶5.2; Box 1; Figure 2 | Field 2025 | OK | *The Verge*: "It's automatically set to 'On.'" | Anthropic's own announcement shows the pop-up as an image. Viewed in this pass, its "You can help improve Claude" toggle is switched on, with no "On" label, so the label is *The Verge*'s word, as the draft's attribution says. |
| M27 | "I do not want Claude to start telling people my research results" | ¶5.2b | A researcher quoted by Brzostowicki 2026 | **FIXED** (attribution) | *Nature* technology feature: speaker Ian Gaudet, a neuroscientist at Florida Atlantic University | The wording is verbatim. The speaker is now named (C3). |
| M28 | "uphold core socialist values" | ¶5.4 | CAC et al. 2023 | OK | cac.gov.cn, Art. 4(1): "（一）坚持社会主义核心价值观" | A translation; add "(our translation)" if the journal asks. |
| M29 | "paper counts are meaningless" | §6 seeds | Blekhman 2026 | OK | As M22 | |
| M30 | "Make new terrain measurable" | §6 seeds | Huang et al. 2026 | OK | Print PDF heading | |
| M31 | "Stop punishing pivots" | §6 seeds | Huang et al. 2026 | OK | Print PDF heading | |
| M32 | "exploratory grants that have extended evaluation horizons" | §6 seeds | Huang et al. 2026 | OK | Print PDF ("funders must create exploratory grants that have extended evaluation horizons") | An image caption interrupts the sentence in the print layout. |
| M33 | "Reward innovation, not just output" | §6 seeds | Huang et al. 2026 | OK | Print PDF heading | |
| M34 | "rationed, not priced" | ¶4c.3; §6 seeds | Fourie 2026 | OK | v3 full text ("Review is therefore rationed, not priced.") | |
| M35 | "enabled Principal Investigators to submit more than 40 distinct applications in a single application submission round" | Table 1, NIH row | NIH 2025 | OK | NOT-OD-25-132 | |
| M36 | "unmanageable influx" | Table 1 | arXiv 2025a | OK | arXiv blog, 31 Oct 2025 | |
| M37 | "hundreds of review articles every month" | Table 1 | arXiv 2025a | OK | arXiv blog, 31 Oct 2025 | |
| M38 | "incontrovertible evidence that the authors did not check the results of LLM generation" | Table 1, May 2026 row | Dietterich 2026, as quoted by Ha 2026 and Cole 2026 | OK (wording via two secondary sources, as the table says) | The thread's first post (14 May 2026, 19:03 UTC) was read through X's oEmbed and syndication endpoints and does not contain the words. *404 Media* (15 May) and *TechCrunch* (16 May) quote the same sentence identically. | The later posts could not be opened: X returns HTTP 402 without a login. The table's source cell already says "primary, first post read" and "quoted by Ha 2026 and Cole 2026", so that flag stays. arXiv's Editorial Advisory Council page confirms Dietterich's role: "chair of arXiv Computer Science Editorial Committee, 2025-2027". |
| M39 | "superficial, high-level theory synthesis" | Table 1, SocArXiv row | SocArXiv 2026 | OK | https://socopen.org/ai-policy/ ("Superficial, high-level theory synthesis and systemic reviews") | Only the capital letter changes. The item is barred "whether created by machines or not". |
| M40 | "The rapid rate of growth in submissions, while exciting, has begun to strain the review system" | Table 1, ICLR row | ICLR 2027 | OK | https://iclr.cc/Conferences/2027/AuthorGuidelines ("[Why these new policies? …]") | The URL is corrected (C20). |
| M41 | "stopgap" | Table 1, arXiv 1 Oct 2026 row | arXiv 2026 | OK | arXiv blog, 1 Oct 2026 ("…across all submitters and categories as a stopgap…") | |
| M42 | "unsustainable rate of submissions at EMNLP'26" | Table 1, ACL row | ACL 2026 | OK | ACL portal (11 Sep 2026) and ARR page | |
| M43 | "Peer review is the scarcest resource of a conference … generative AI tools now make it possible to produce far more manuscripts than the community can carefully evaluate" | Table 1, AISTATS row | AISTATS 2027 | OK | https://virtual.aistats.org/Conferences/2027/CallForPapers ("Submission Quotas") | Both passages come from the same paragraph and in this order. The ellipsis omits the sentence on the cost of each submission's reviews and the clause "Over the last few years, the number of submissions to machine learning conferences has grown at an unprecedented rate, and". |
| M44 | "NOT intended for" | Data and process availability | bioRxiv n.d. | OK | https://www.biorxiv.org/about/FAQ ("bioRxiv is NOT intended for: … Editorials, letters, opinion pieces … White papers or policy statements …") | Read on the fifth attempt, after four HTTP 429 refusals. The capitals are the source's. |
| M45 | "permitted with human oversight, verification, and transparency through disclosure" | Data and process availability | Nature Portfolio n.d. (Amber tier) | OK | Nature Portfolio AI policy ("Permitted with human oversight, verification, and transparency through disclosure.") | "Extensive copy editing or writing support" is an Amber example, and the Red tier covers use that "replaces accountable human contribution". The same page led to C1. |
| M46 | "how the user evaluated the validity of the tool's outputs" | Data and process availability | PLOS n.d. | OK | PLOS Biology, Ethical publishing practice | |

### 2.2 EMBO version (`draft_embo.md`)

| # | Quotation (short) | Where | Status | Notes |
|---|---|---|---|---|
| E1 | "no brakes" | Opening, paragraph 2 | OK | As M22, and the EMBO text frames Blekhman as writing for biologists. |
| E2 | "reversed the relationship between writing complexity and paper quality" | "The cost was the signal", paragraph 2 | OK | As M2. The reference now names the author version (C23). |
| E3 | "a relatively small number of Principal Investigators" | "Rationing is not reform", paragraph 1 | OK | As M5. |
| E4 | "perceived double standard" | "Rationing is not reform", paragraph 2 | OK | As M21. |
| E5 | "rationed, not priced" | "Rationing is not reform", paragraph 4; Recommendations seeds | OK | As M34. |
| E6 | "the scarcity of interpretive attention" | "Rationing is not reform", paragraph 4 | OK | Hansen 2026, full text from PMC (PMC12980890): "The bottleneck is no longer the scarcity of research output but the scarcity of interpretive attention." The BMC page returned only a script page. |
| E7 | "AI makes extending a familiar research line…" | "Will cheap output narrow science?", paragraph 1 | OK | As M16. |
| E8 | "appears to be a major impacting factor" | "Will cheap output narrow science?", paragraph 1 | OK | As M17. |

**Close paraphrases (EMBO):**
- "Blekhman (2026) calls arXiv's measures reasonable but aimed at symptoms" matches "These responses are reasonable, but they address symptoms rather than the underlying problem". OK.
- Blekhman's five goals (EMBO "What AI could do"; master ¶3.1) match the source. OK.
- The EMBO cites Blekhman for arXiv's computer-science rule and for the one-year bans. That holds: he reports both ("in 2025 it stopped accepting review and position papers in computer science that had not already passed peer review … in 2026 it announced a 1-year submission ban…").

### 2.3 Correspondence (`correspondence_draft.md`)

- The text has no direct quotations.
- Its first sentence paraphrases the online title of Huang et al. ("AI can widen science — but only if institutions stop rewarding the already measurable"); the print headline is confirmed as "AI can expand horizons — if academia stops favouring the already measurable".
- "the distance-from-past-work indicator that they themselves propose" matches the print PDF ("Possible indicators include the conceptual distance between a researcher's current and previous work").
- The claims about NIH, arXiv and the conference quotas match the primary sources in §3.

### 2.4 Counts

| Version | Entries | OK | FIXED | PARAPHRASED | UNVERIFIABLE |
|---|---|---|---|---|---|
| Master | 44 (M1–M46, without M8 and M23) | 43 | 1 (M27) | 0 | 0 |
| EMBO | 8 | 8 | 0 | 0 | 0 |
| Correspondence | 0 | – | – | – | – |
| **Total** | **52** | **51** | **1** | **0** | **0** |

Several OK statuses carry a qualification:
- **M2/E2:** checked in the authors' accepted version, because *Science* was unreadable.
- **M10, M11, M17, M18, E8:** checked in the accepted author version and *Nature*'s published Peer Review File; the *Nature* main text is paywalled.
- **M38:** wording attested by two outlets quoting the thread; the post containing it is behind a login.

---

## 3. Table 1: the rules against their primary sources

All primary sources were read on 16 Oct 2026. "Status" covers the row and the sentences in the text that describe the rule.

| Row | Who announced it | Date | Exact limit | Scope | Stated reason | Exemptions and details | Status |
|---|---|---|---|---|---|---|---|
| **NIH**, NOT-OD-25-132 | NIH (notice from the Office of the Director; inquiries to the Office of Science Policy) | Released 17 Jul 2025; effective for applications to the 25 Sep 2025 receipt date and after | "NIH will only accept six new, renewal, resubmission, or revision applications from an individual Principal Investigator/Program Director or Multiple Principal Investigator for all council rounds in a calendar year"; applications "substantially developed by AI, or contain[ing] sections substantially developed by AI" are not considered original | All activity codes except T activity codes and R13 conference grants | Large numbers of applications from one PI "may unfairly strain NIH's application review processes"; there is "evidence that the use of AI tools has enabled Principal Investigators to submit more than 40 distinct applications"; the purpose is "fairness and originality" | NIH "will continue to employ the latest technology in detection of AI-generated content to identify AI generated applications"; AI detected after an award can be referred to the Office of Research Integrity | Row confirmed. ¶2.4 **fixed** (C2). The "Stated reason" cell gives the evidence and the expected reach rather than the strain on review; it is accurate, but the author may add the strain. |
| **arXiv, computer science** (31 Oct 2025) | arXiv blog (Kat Boboris) | 31 Oct 2025 | Review/survey articles and position papers "must now be accepted at a journal or a conference and complete successful peer review", with documentation (journal reference and DOI) | arXiv CS category | "unmanageable influx"; "hundreds of review articles every month"; LLMs make such papers "fast and easy to write" | Review at conference workshops "is not enough"; appeals are possible; research papers on science, technology and society (e.g. cs.CY) are unaffected; arXiv calls it a moderation-practice change ("Technically, no!" policy change) | Confirmed (¶2.5, ¶4c.2, Data availability, Figure 3; EMBO through Blekhman). |
| **arXiv, mathematics endorsement** (10 Dec 2025) | arXiv blog (Kat Boboris) | 10 Dec 2025; extended to all sections on 21 Jan 2026 | Institutional email no longer enough on its own for automatic endorsement of new authors. Automatic endorsement needs an institutional email **and** prior authorship of a paper in arXiv Mathematics; otherwise a personal endorsement is required. | All Math categories; math-ph follows the Physics rules | "stemming the flood of low-quality, non-scientific submissions to the arXiv Math section" | Authors already endorsed are unaffected | **Primary source found**; Table 1 note and Figure 4 **fixed** (C8, C9, C11). The EMBO Figure 2 legend's date and description are correct. Not a Table 1 row: whether to add it is an [AUTHOR] decision. |
| **arXiv one-year ban** (May 2026) | Thomas G. Dietterich, chair of arXiv's CS section (Editorial Advisory Council page: "chair of arXiv Computer Science Editorial Committee, 2025-2027"), on X | Thread of 14 May 2026 (first post 19:03 UTC, a Thursday) | "a 1-year ban from arXiv followed by the requirement that subsequent arXiv submissions must first be accepted by [*404 Media*: at] a reputable peer-reviewed venue", where there is "incontrovertible evidence that the authors did not check the results of LLM generation" | Unclear: computer science only, or all of arXiv | Unchecked LLM output: "hallucinated references, meta-comments from the LLM" | One-strike rule; moderators flag and section chairs confirm; appeals allowed (*TechCrunch*, citing *404 Media*). Not on arXiv's moderation, code-of-conduct or blog pages on 16 Oct 2026; the moderation page carries only the general policy on generative-AI tools. | Confirmed as far as readable (see M38). Reason cell **fixed** (C5). |
| **SocArXiv** | SocArXiv (policy page; release post by director Philip N. Cohen, 9 Mar 2026) | Policy dated 8 Mar 2026, updated 28 Sep 2026 | "We generally do not allow authors to post more than one paper per week"; verbatim AI-generated text and other uses barred | All SocArXiv submissions | "we are getting overrun with machine-generated slop" | "People who need to upload multiple papers may contact us to make arrangements" | Confirmed. When the weekly limit began (March text or September update) could not be established: the March release post does not mention it, and archived versions were not checked. Not listed: AI-topic submissions were paused from November 2025 for about three months. |
| **Chinese universities** | CCTV News (Pan, Wu, Wei, Jia & Yang), reposted by ScienceNet | 22 May 2026 | University-set AIGC thresholds of 15–40% (e.g. Sichuan University 20% for humanities and 15% for science, engineering and medicine; Guangxi Normal, Hebei University of Engineering and Nanjing University of Aeronautics and Astronautics 40%); above the limit, "论文将不得参加盲审和答辩" (the thesis may not proceed to blind review and defence) | Theses (the named rules concern undergraduate theses) | AI-generated content; academic integrity | At Nanjing University of Aeronautics and Astronautics, theses that fail are judged by experts through review and defence | Confirmed. |
| **TMLR** | TMLR editorial policies | Quota in force; "June" (2026) only from Singh Chawla 2026a | Generalized Harmonic Quota Rule, N_1 = 2 and N_9 = 9; the budget spent per submission depends on its number of authors | All TMLR submissions | TMLR states none. Singh Chawla reports the quota came "after a tripling of submissions over the past year", including "a 13-fold increase in single-author submissions" | Doubled quotas for reviewers and action editors (N_1 = 4, N_9 = 18); desk-rejected submissions count; circumvention may bring "lifetime bans" | Confirmed. The source cell correctly assigns the date and growth figures to the news piece. |
| **ICLR 2027** | ICLR 2027 programme chairs (call and guides posted "July 28"; Singh Chawla quotes Jacob Andreas as programme chair) | Announced 28 Jul 2026; abstracts due 18 Sep and papers 25 Sep 2026 | "No author may appear as a co-author on more than 20 papers"; "at most one paper in which no author is an eligible reciprocal reviewer"; "we will randomly desk-reject excess submissions until every author is under quota" | ICLR 2027 | M40; Singh Chawla: submissions "look set to exceed 62,000, up from 490 a decade ago" | Qualification means one accepted primary paper at a listed ML, NLP, vision, AI, robotics, KDD or COLT venue by the abstract deadline. Each submission must register a qualified author as reviewer, unless none qualifies; authors on three or more papers review six. | Confirmed (¶4c.2; Figure 1). Measure cell **fixed** (C6); URL **fixed** (C20, C21). |
| **arXiv, all categories** (1 Oct 2026) | arXiv blog (Kat Boboris), with a statement by Dietterich as "Chair of the arXiv Editorial Advisory Council" | Announced and effective 1 Oct 2026 | "up to two submissions per calendar month, with a limit of three total active submissions at any given time"; the three-active limit dates from 2024 | "all submissions, across all categories"; applies "only to submitters" | A "stopgap"; to "equitably distribute our volunteer moderators' time across arXiv authors, and protect the arXiv corpus from a sharp increase in inappropriate submissions"; 9,869 / 20,569 / 40,363 submissions in September 2016 / 2024 / 2026 | Rejected submissions count; papers deleted before announcement do not; submissions on hold carry over only toward the active limit; arXiv's moderation page adds "one per week rate limit after version 5" for replacements | Confirmed (¶4c.2, ¶2.8, Figures 1, 3 and 4, EMBO opening, Correspondence). The "Stated reason" cell lists the September counts rather than the stated purpose; accurate, but the author may add the purpose. |
| **ACL Rolling Review** | ACL Peer Review Standing Committee, approved by the ACL executive; posted on the ACL portal 11 Sep 2026 (Sarvnaz Karimi) and on the ARR site | Applies to ARR submissions from October 2026 (the NAACL/COLING 2026 cycle; deadline 12 Oct) | "authors are capped at 20 total submissions and 5 first-author (including shared first-author) submissions per cycle"; each submission must provide a "qualified service contributor (reviewer or chair)"; "Submissions without service capacity go into a lottery" | Main ARR cycles only (not demo or industry tracks) | M42; "38% of the ~17K May 2026 submissions came from authors with no available publication record" | A contributor may support at most two submissions; non-author contributors may be named if they vouch for the work; the page says the policy "is new" and details are still being worked out | Confirmed. Reason cell **fixed** (C7). |
| **AISTATS 2027** | AISTATS 2027 call for papers | Abstracts due 29 Sep and papers 6 Oct 2026; conference 3–6 May 2027 | "No author may appear as a co-author on more than 12 submissions"; authors without an accepted paper at ICLR, ICML, NeurIPS or AISTATS "may appear as a co-author on at most 3 submissions"; excess randomly desk-rejected | AISTATS 2027 | M43 | Update of 24 Sep 2026: the reviewing exemption for papers whose authors are all unqualified "can only be requested for one paper per author", so an unqualified author "can submit at most one single-author paper" | Confirmed. The 24 Sep exemption limit is not in the row; this is an omission, not an error. The "Effective" cell gives the conference date, while the quotas apply from the September–October 2026 deadlines. Both are left for the author. |
| **arXiv, language rule** (note only) | arXiv blog (Kat Boboris) | Announced 21 Nov 2025; guidelines 13 Jan 2026; in effect 11 Feb 2026 | "all submissions have a full English-language version, either as the original language or as an included translation" | All arXiv | "transparency and fairness in moderation"; to "expand the reach" of non-English papers | Automated translation is acceptable if faithful | Note **fixed** (C8, C11). |

Sentences in the text that describe these rules were checked against the sources above. The results:
- **Master:** ¶0.3, ¶2.4, ¶2.5, ¶2.8, ¶2.9, ¶2.10, ¶4c.2, ¶4c.2b and ¶4c.3b; the Table 1 caption and note; the captions of Figures 1, 3 and 4; Data and process availability. Only ¶2.4 needed a correction (C2).
- **EMBO:** opening; "The cost was the signal", paragraph 2; "Rationing is not reform", paragraphs 1–2; the Figure 1 and 2 legends. All correct.
- **Correspondence:** paragraph 1. Correct.
- **Check behind ¶4c.2b's "fewer than 3%":** 693 prolific author names among 28,279 in Q3 2026 is 2.45%.

---

## 4. Kusumegi et al. (2025): does the complexity–quality reversal rely on dating adoption?

**No. The finding is kept in both versions, and the text is unchanged.**

**What the paper does** (author version, arXiv:2601.13187v1: main text, "LLM use, scientific writing, and publication outcomes", and the Fig. 3 caption):
- **Sample:** 264,125 manuscripts written since 2023 (177,880 on arXiv, 58,958 on bioRxiv, 31,959 on SSRN and 7,243 submitted to ICLR 2024).
- **Groups:** each manuscript is classed as "LLM-assisted" or "non-LLM-assisted" by the detector applied to its own abstract.
- **Measures:** writing complexity is the negative of the Flesch Reading Ease Score. Quality is "publication in a peer reviewed journal or conference by the end of our observation window (June 2024)", or peer-review scores for ICLR.
- **Analysis:** logistic regressions (OLS for ICLR) run separately for the two groups. The authors report that results hold after controlling for preprint month and field (supplement S3.2, S5.9).
- **No adoption date** enters this analysis.

**Where the adoption date is used:**
- The paper dates adoption by first detection only for the author-level event studies: the productivity estimate (Fig. 1–2) and the citation-behaviour estimate (Fig. 4D–I). The authors write "An author's adoption status changes from 0 to 1 for all months subsequent to detected use".
- The drafts already dropped both of those findings.

**What the critique covers:**
- Renault, Bergeaud & Bosquet (arXiv:2605.17979v1; *PNAS* version doi:10.1073/pnas.2618638123) criticise only "dating adoption as the first month in which at least one submitted abstract exceeds an LLM-detection threshold" in the event study.
- Their text never mentions writing complexity, Flesch scores or publication outcomes.

**Limits of this check:**
- The *Science* text and supplement could not be read: science.org returns HTTP 403, and Crossref and PubMed hold only the one-line summary. The design was read in the authors' accepted version, which says it is "the author's version of the work".
- Other caveats are not the critique the author's rule targets, and are not used in the drafts. They include detector-based classification and the possibility that later preprints had less time to be published (the authors control for month).

---

## 5. The eight incomplete references

All eight are completed (C12–C19; Hosseini et al. in both the master and EMBO).

| Entry | Completed with | Source |
|---|---|---|
| Adeyeye | Adeyeye, E. | Crossref (SSRN posted content) |
| Bhargava et al. | Bhargava, H. K. et al.; title; 72(9):7381–7393 | Crossref |
| Hosseini et al. | Hosseini, M. … Holmes, K.; 35:rvag020 | Crossref |
| Hutchinson | Hutchinson, P.; *Nature* 658:286 (Correspondence) | Crossref; nature.com page metadata |
| Lovén | Lovén, L.; v3 | arXiv API |
| Ma | Ma, J. W. | arXiv API |
| Motoki | Motoki, F. Y. S.; *Nature* 658:572 (Correspondence) | Crossref; nature.com page metadata |
| Wu et al. | Wu, K., Huang, Z. & Geng, H.; full title; full workshop name | NeurIPS 2026 virtual page |

The claims these references support were checked against the same records:
- **Adeyeye (¶1.3):** "applies signalling theory to the publication itself" matches the abstract ("Applying signaling theory (Spence, 1973)…").
- **Bhargava et al. (¶4c.3b):** "language models at the front line of review" matches "deploys large language models as a structured, trained, frontline reviewer".
- **Hutchinson (Box 1):** matches "authorship-contribution taxonomies might be too coarse for a growing form of AI use: sustained intellectual interaction".
- **Motoki (¶4b.1, "see also"):** matches; the letter builds on Messeri & Crockett's warning of "scientific monocultures".
- **Lovén and Ma (Box 1, "verification is what cheap generation leaves scarce"):** match their abstracts. Lovén lists "verified signal" first among the things that "become scarce"; Ma writes that AI weakens the filter of generation cost "without comparably lowering verification cost".
- **Hosseini et al. (¶0.3; EMBO opening):** match ("These metrics are becoming even less reliable as GenAI accelerates text-based and computational work").
- **Wu et al.:** fixed in Box 1 (C4).

The `[RECHECK: … not audited]` markers on Adeyeye (¶1.3), Bhargava et al. (¶4c.3b) and Motoki and Messeri & Crockett 2026 (¶4b.1) were left in place. They fall outside this pass's tasks, but the claims match what was read here, so the author may clear them.

---

## 6. Consistency between the versions and with the companion data

Checked against `paper/figures/README_companion_analysis.md` (commits 41f795d and 6021b3a) and, for bioRxiv, against bioRxiv's statistics API (https://api.biorxiv.org/sum/y and /sum/m).

| Item | Master | EMBO | Correspondence | Companion data / source | Result |
|---|---|---|---|---|---|
| Growth over 2022, last four quarters | ¶2.8: +44% physics, +50% biology, +59% mathematics, +146% CS. Figure 3: also +139% medicine, +73% social sciences | Biology +50% ("slightly more than arXiv physics"); Figure 1 legend: +50%, +139%, +59%, +146% | – | README: +44, +59, +50, +139, +73, +146 | Match |
| Year-on-year growth | ¶2.8b: maths +78%, CS +41%, physics +26%. Figure 3: +26, +78, +10, +29, +6, +41 | Text: maths 78%, CS 41%, physics 26%; legend: biology +10%, medicine +29% | – | README: +26, +78, +10, +29, +6, +41 | Match |
| Q3 2026 index values | Figure 3: 162, 219, 157, 289, 184, 278 | Figure 1 legend: 157 (biology), 289 (medicine) | – | README | Match |
| bioRxiv growth "10–13% a year since 2023" | ¶2.8b; Figure 3 | "The cost was the signal", paragraph 4 | – | API: 2023 +9.5% (rounds to 10%), 2024 +11.4%, 2025 +13.0%, January–September 2026 +11.7% | Match (the response file's open "to check" item is resolved) |
| bioRxiv base years | Figure 3: 2020 38,717; 2021 36,866; 2022 35,750 | "below its 2020–21 level" | – | API yearly totals | Match |
| Prolific share in mathematics | 5.3% → 19.3%; 3.0% → 6.2% (strict); 5.2% → 18.0% and 1.8% → 5.9% (Q3 to Q3) | 5.3% → 19.3%; 3.0% → 6.2%; "at least doubled"; "roughly triples within a year" | Optional sentence in a comment: "about 5% to 19%" | README | Match |
| Prolific authors | 611 of 693; 143 / 468 / 82; 107→624, 5→65, 0→4; 20,108→28,279 | 611 of 693 | – | README (143 + 468 = 611; 624 + 65 + 4 = 693) | Match |
| AI-tool mentions | 1.9% against 1.6%; panel c 0.09% → 1.97% | "only 2% of these papers"; 0.09% → 1.97% | – | README | Match (EMBO rounds 1.9% to 2%) |
| Other panels of the mathematics figure | 30.0% → 37.8%; Erdős 26 → 101; 3,197 → 8,360 papers; team sizes 2.8 → 12.1% and 11.5 → 28.1% | Same values | – | README | Match |
| Within-field contrasts (master Figure 5) | Growth figures for 2023–2026, indices 164 / 152 / 159 / 149 / 119, ranges, pairs, bioinformatics +27% and 63% of its group, 2019 comparison, COVID-19 shares | One sentence, no numbers | – | README "Figure 8" | Match |
| medRxiv public datasets | ×2.3 against ×1.6 | Same | – | README | Match |
| Hao et al. | 41.3 million; 310,957 (0.75%); 3.02×; 4.84×; 1.37 years; 4.63%; 22% | 41.3 million; 3.02×; 4.84×; 4.63% | – | *Nature* abstract; arXiv v4 | Match |
| NIH, arXiv rules | 40 applications; 6 a year; 2 a month; 40,363 | Same | Same (40; six a year; two a month) | Primary sources (§3) | Match |
| Process record | 3.5 h; US$153; 174 claims, 14 / 35 / 68 / 8 / 1; 69 flagged; 5 unverifiable; times 21:27, 22:25, 00:07, 00:58, 01:29, 07:15 | Same, where given | – | Brief; response file §6 | Match between versions. The 01:29 vs 01:30:03 question in the response file stays with the author. |

**Not a number, but noted:** the EMBO sentence on Holzwarth et al. (corrected wording, C22) cites ref. 15, the extended essay. The master cites Holzwarth et al. only for biologists using LLMs as much as physicists, not for the share of biomedical papers. To make ref. 15 carry that share, the author could add four words to ¶2.8b of the master, e.g. "…(Lin & Zhu 2025; Holzwarth et al. 2026), most of them by the end of 2025". That would need its own wording check and is not applied here.

---

## 7. Limits (after the edits)

**Method.** A script (scratchpad `scripts/wc.py`, not in the repository) applies the drafts' stated method:
- It counts whitespace-separated tokens that contain a letter, digit, €, $ or &.
- It removes HTML comments.
- "Prose" also removes the editorial markers [RECHECK…], [AUTHOR: …], [CITATION NEEDED: …], [PLACEHOLDER: …], [Zenodo DOI] and [to be minted]. Each marker is removed whole, including nested brackets.
- Section boundaries follow the drafts' own tables. In the master, headings are excluded, as its section rows imply. In the EMBO version, headings are included, as its comment says.

**Check against the recorded counts.** Before any edit, the script reproduced the recorded counts exactly, with one exception:
- In the master's Box 1, the earlier count left 10 words of the nested `[AUTHOR: choose one or both … which is rationing.]` marker in the prose total. That marker contains a bracketed phrase, and removing it whole gives 573 rather than 583.
- So the master's true pre-edit total was 6,972, not 6,982.
- The EMBO count of 3,154 was reproduced once the Recommendations heading is taken as part of its 350-word reserve, as the draft's own section list does.

| Version | Main text (prose) | Limit | Headroom | Other limits |
|---|---|---|---|---|
| Master (§6 counted at its 700-word reserve; §4d heading and placeholder count 0) | **6,982** (raw 7,586); +10 from this pass (¶2.4 +4, ¶5.2b +2, Box 1 +4). By the earlier script it would read 6,992. | ≤7,000 | 18 (8 by the earlier script) | Table 1, captions and references are excluded; 155 references |
| EMBO (350-word reserve for Recommendations; DORA/CoARA section counts its 5-word heading) | **3,156** (raw 3,311); +2 from this pass (C22) | ≤3,500 | 344 | **15 references** (limit 15) |
| Correspondence | **186** words of text; title 10 | <200 | 13 | **2 references** (limit 2) |

The §4d and §6 placeholders were not touched. The header comments of both essays were updated with these counts (C25).

---

## 8. Still unverified, and points for the author

1. **The *Science* text of Kusumegi et al. and its supplement:** science.org returns HTTP 403. The quotation and the design were checked in the authors' accepted version.
2. **The *Nature* main text and SI of Hao et al.:** the main text is paywalled. M10, M11, M17 and M18 were checked in arXiv v4 and in the published Peer Review File. Note that M17 and M18 are main-text sentences, not SI text.
3. **Dietterich's thread after its first post:** X returns HTTP 402. The wording rests on *404 Media* and *TechCrunch*, as Table 1 says. The scope of the ban (computer science only, or all of arXiv) remains unclear, and the ban is still not on arXiv's policy pages or blog.
4. **Other sites that blocked access:** academic.oup.com (Korinek & Vipra: the journal abstract was read through Crossref instead); the BMC page of Hansen (PMC full text read instead). Nothing was circumvented.
5. **Table 1 omissions, left for the author** (accurate as they stand):
   - NIH's stated reason (strain on review);
   - arXiv's stated purpose for the rate limit, and its exemptions for deleted and on-hold submissions;
   - AISTATS's 24 Sep 2026 exemption limit, and its "Effective" cell, which gives the conference date rather than the submission deadlines;
   - whether to list arXiv's endorsement rule (the [AUTHOR] slot in the note, C8);
   - when SocArXiv's weekly limit began;
   - SocArXiv's pause on AI-topic submissions (November 2025 to about February 2026).
6. **Unchanged phrasing worth a look:**
   - Figure 1's "ICLR 2027 expects more than 62,000": the source says submissions "look set to exceed 62,000"; audit R84 verified this.
   - M22: Blekhman's "no brakes" is said of "biology research".
   - The [AUTHOR] slot in ¶5.2b names the setting "Help improve Claude"; the pop-up's label reads "You can help improve Claude".
7. **Markers this pass did not clear:**
   - [RECHECK] on Adeyeye, Bhargava et al., Messeri & Crockett 2026, Motoki 2026 and Lin 2025: the first four match the records read here; Lin 2025 was not checked.
   - NIH's simplified review framework (¶4c.2b).
   - R86, R87 and R89 in Figure 2.
   - [CITATION NEEDED] on Lamont and on pre-AI rationing.
8. **Files outside this pass now partly out of date (not edited):**
   - `paper/reviews/response_to_reviews.md`:
     - item 11 repeats the 21.8% misreading (C4);
     - "NIH and detectors" records the opposite of what the notice says (C2);
     - Appendix A's M40 URL is the broken one (C20);
     - Appendix A.4 and §7's marker list still say the endorsement rule lacks a primary source (C8).
   - `paper/figures/README_companion_analysis.md`: says the May 2026 ban "has no primary source (press reports only)". Dietterich's post on X is the primary source, though only its first post can be read.
   - The drafts' HTML comments: commit 199f5bb, made during this pass, moved the year ticks to 1 January. The comments still call this a "pending figure fix" (master: "How to read this file" and the Figure 5 comment; EMBO: the figure-legend comment). The README's numbers did not change in that commit, so §6 stands.
