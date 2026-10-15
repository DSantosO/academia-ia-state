# Humanities, social sciences, economics, law and education (SSH): data sources for publishing volume, grant/scholarship applications and LLM impact

*Evidence tags:*
- **[V]** I verified it myself in this session (query, download or parse, run 15 Oct 2026).
- **[P]** I read it in a primary document (official page, PDF, or a paper's abstract or metadata).
- **[S]** It is a secondary claim (news, blog, aggregator, search-engine summary, or a third-party copy) that I did not confirm in the original.

"My calc" marks my own arithmetic. Items already covered in the sibling notes are cross-referenced, not repeated.

## 1. All-discipline counters with field breakdowns (OpenAlex snapshot entities, Dimensions FoR, Scopus ASJC, Crossref book/thesis types) and documented SSH coverage biases

### Takeaway
**OpenAlex snapshot entity files.** The S3 snapshot does carry free, keyless records for domains, fields and subfields, but they hold only lifetime `works_count` and `cited_by_count`. They have no `counts_by_year`, in either the 2026 layout or the frozen legacy layout.
- Yearly SSH counts in OpenAlex must come from aggregating the ~615 GB works files, or from the metered API, whose keyless budget was exhausted (HTTP 429).
- Where `counts_by_year` does exist (e.g., publishers), it covers only 2014–2026.
- Field stocks also changed by 1.4–7× between the April 2024 and October 2026 versions. OpenAlex field counts are therefore not comparable across versions.

**Crossref.** It gives free yearly counts for book, book-chapter, monograph and edited-book, but no discipline tags: `subject` is now empty.

**Documented biases.** WoS and Scopus favour natural sciences, engineering and biomedicine over SSH, and English over other languages. OpenAlex is more linguistically balanced but mislabels language.

### Cited Findings

#### OpenAlex snapshot: domain/field/subfield entity records
- **Layout (Oct 2026 release).** `data/jsonl/` and `data/parquet/` contain `domains/`, `fields/`, `subfields/`, `topics/`, `concepts/`, `works/` and other entities. `legacy-data/` contains `domains/`, `fields/`, `subfields/`, `concepts/` and more. Anonymous HTTP listing works. [V] — [S3 listing](https://openalex.s3.amazonaws.com/?list-type=2&prefix=data/jsonl/&delimiter=/)
- **Manifests.** Domains: 4 records, release date 2026-10-14. Subfields: 252 records in two partitions (2026-10-13 and 2026-10-14). [V] — [domains manifest](https://openalex.s3.amazonaws.com/data/jsonl/domains/manifest.json); [subfields manifest](https://openalex.s3.amazonaws.com/data/jsonl/subfields/manifest.json)
- **No yearly counts in the entity records.** Keys in the domain, field and subfield records:
  - Domain: `cited_by_count, created_date, description, display_name, display_name_alternatives, fields, id, ids, siblings, updated_date, works_api_url, works_count`.
  - Field: the same plus `domain` and `subfields`.
  - Subfield: also `field` and `topics`.
  - None has `counts_by_year`. The legacy-layout records (e.g., `legacy-data/domains/updated_date=2024-04-01`) also lack it.
  - [V] — [domains 2026-10-14](https://openalex.s3.amazonaws.com/data/jsonl/domains/updated_date=2026-10-14/part_0000.gz); [fields 2026-10-14](https://openalex.s3.amazonaws.com/data/jsonl/fields/updated_date=2026-10-14/part_0000.gz); [subfields 2026-10-14](https://openalex.s3.amazonaws.com/data/jsonl/subfields/updated_date=2026-10-14/part_0000.gz); [legacy domains](https://openalex.s3.amazonaws.com/legacy-data/domains/updated_date=2024-04-01/part_000.gz)
- **Taxonomy placement.** OpenAlex has no separate humanities domain. The "Social Sciences" domain (id 2) contains six fields: Arts and Humanities (12); Business, Management and Accounting (14); Decision Sciences (18); Economics, Econometrics and Finance (20); Psychology (32); Social Sciences (33). Its `works_api_url` is `works?filter=topics.domain.id:2`, i.e., any of a work's assigned topics, not only the primary topic. [V] — [domains file](https://openalex.s3.amazonaws.com/data/jsonl/domains/updated_date=2026-10-14/part_0000.gz)
- **Lifetime `works_count`, release of 2026-10-14** [V] — [fields file](https://openalex.s3.amazonaws.com/data/jsonl/fields/updated_date=2026-10-14/part_0000.gz); [subfields file](https://openalex.s3.amazonaws.com/data/jsonl/subfields/updated_date=2026-10-14/part_0000.gz)
  - Domains: Social Sciences 141,021,744; Physical Sciences 159,164,265; Health Sciences 62,125,705; Life Sciences 55,049,605. These sum to 417,361,319 (my calc), more than the ~327M "core" works documented in indexed_publications_and_denominators.md §4. Counts therefore overlap across domains.
  - SSH fields: Social Sciences 61,100,473; Arts and Humanities 45,287,490; Business/Management/Accounting 11,892,092; Psychology 10,213,042; Economics, Econometrics and Finance 8,882,473; Decision Sciences 3,646,174.
  - Selected subfields: Sociology and Political Science 13,735,198; Political Science and IR 12,329,408; Education 9,635,360; History 8,966,781; Literature and Literary Theory 8,276,105; Economics and Econometrics 5,709,927; Law 4,314,743; Philosophy 3,647,257; Language and Linguistics 4,318,560; Religious studies 2,759,577; Finance 1,734,494; Public Administration 797,383.
- **Version break.** Legacy records dated 2024-04-01 compared with 2026-10-14 records (my calc):
  - Arts and Humanities 13,485,134 → 45,287,490 (×3.36)
  - Social Sciences field 32,062,906 → 61,100,473 (×1.91)
  - Psychology ×1.81; Economics ×1.55
  - Medicine ×1.42; Computer Science ×1.46; Physics and Astronomy 7,186,862 → 50,456,478 (×7.0)
  - Social Sciences domain 64,995,390 → 141,021,744 (×2.17)
  - These coincide with the Nov 2025 Walden/XPAC rewrite and the topic re-assignment (6 Oct 2026) already documented in indexed_publications_and_denominators.md §4.
  - [V] — [legacy fields 2024-04-01](https://openalex.s3.amazonaws.com/legacy-data/fields/updated_date=2024-04-01/part_000.gz)
- **Concepts no longer carry yearly counts.** `data/jsonl/concepts/` (61,252 records; 19 level-0) was refreshed on 2026-10-14 but `counts_by_year` is empty for every concept I checked (Sociology, Economics, Philosophy, Art, History, Political science, Psychology, Business, Law…). Concept `works_count` still exists, e.g., Philosophy 46,890,763 and Economics 22,318,597. [V] — [concepts 2026-10-14](https://openalex.s3.amazonaws.com/data/jsonl/concepts/updated_date=2026-10-14/part_0000.gz)
- **How far back `counts_by_year` goes (entities that have it).** Across all 10,713 publisher records (94 partitions) of the current snapshot, `counts_by_year` spans 2014–2026, e.g., Elsevier BV 2014–2026. It is a rolling recent window, not a full history. [V] — [publishers manifest](https://openalex.s3.amazonaws.com/data/jsonl/publishers/manifest.json)
- **Keyless API.** `works?filter=primary_topic.field.id:12&group_by=publication_year` returned HTTP 429 ("Insufficient budget… no API key… $0 remaining; resets at midnight UTC"; `x-ratelimit-limit-usd: 0.1`). The error text tells agents to request a key by POSTing an email; I did not, per constraints. [V] — [query](https://api.openalex.org/works?filter=primary_topic.field.id:12&group_by=publication_year). Pricing and key history are in indexed_publications_and_denominators.md §4.

#### Crossref work types useful for SSH (books, chapters, monographs, dissertations)
- **Yearly counts by type** (REST API facet `published`, query of 15 Oct 2026; 2026 is partial) [V] — [book-chapter](https://api.crossref.org/types/book-chapter/works?rows=0&facet=published:*); [book](https://api.crossref.org/types/book/works?rows=0&facet=published:*); [monograph](https://api.crossref.org/types/monograph/works?rows=0&facet=published:*); [edited-book](https://api.crossref.org/types/edited-book/works?rows=0&facet=published:*)

  | Type (all-time total) | 2015 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 YTD |
  |---|---|---|---|---|---|---|---|---|---|---|
  | book-chapter (24,913,794) | 705,013 | 900,606 | 1,082,888 | 1,194,476 | 1,078,445 | 1,113,716 | 1,386,317 | 1,101,510 | 1,064,147 | 771,258 |
  | book (855,901) | 29,135 | 50,680 | 38,331 | 39,445 | 40,968 | 37,671 | 29,307 | 30,526 | 33,589 | 24,104 |
  | monograph (816,650) | 23,287 | 28,402 | 28,653 | 31,335 | 34,808 | 34,773 | 38,431 | 35,595 | 35,234 | 28,315 |
  | edited-book (589,986) | 14,943 | 20,590 | 23,378 | 30,427 | 27,832 | 34,937 | 43,158 | 43,090 | 49,265 | 33,966 |

  - `reference-entry` (931,337 total) spikes in 2020 (129,706, vs 11–15k in neighbouring years), a deposit artefact. [V] — [reference-entry](https://api.crossref.org/types/reference-entry/works?rows=0&facet=published:*)
- **Dissertations are not countable by publication year in Crossref.** The `published` facet is empty and per-year `from-pub-date` filters return 0.
  - By DOI-registration year: 2015 71,499; 2018 72,449; 2019 54,726; 2020 40,954; 2021 134,126; 2022 75,122; 2023 75,835; 2024 70,735; 2025 138,905. That is deposit batches, not output.
  - Registrants are concentrated: ABES/France 194,782; Universidade de São Paulo 129,387; Chulalongkorn 79,080; Unicamp 67,405; EKT/Greece 58,465; Iowa State 29,896. Total 1,097,764.
  - [V] — [created-date query](https://api.crossref.org/types/dissertation/works?rows=0&filter=from-created-date:2025-01-01,until-created-date:2025-12-31); [publisher facet](https://api.crossref.org/types/dissertation/works?rows=0&facet=publisher-name:8)
- **No discipline tags.** `subject` came back as an empty list even for a 2015 Springer journal article (Scientometrics). [V] — [example record](https://api.crossref.org/works/10.1007/s11192-015-1765-5)
  - This is deliberate. Crossref's blog (Patrick Polischuk, 13 Mar 2024) says the subject codes came from a Labs experiment adding Scopus All Subject Journal Classification codes and were "not complete or reliable from the start". Crossref would deprecate the feature "in the coming weeks", "removing this data from our index, so the subject element will simply be empty". [P] — [Crossref blog](https://www.crossref.org/blog/subject-codes-incomplete-and-unreliable-have-got-to-go/)
  - This is a 2024 break for any older pipeline that split Crossref counts by subject. A discipline split now needs a join to OpenAlex, DOAB/Thema or publisher/ISBN mappings.

#### Dimensions (ANZSRC Fields of Research) and Scopus (ASJC)
- **Dimensions FoR.** Digital Science built "an improved machine learning training set" and mapped it from FoR 2008 to FoR 2020 codes "so that Dimensions classification approach for the ANZSRC codes could be improved and updated". (Porter et al., arXiv 2209.00104 v2, 21 Jan 2023.) [P] — [arXiv abstract](https://arxiv.org/abs/2209.00104)
  - Search summaries add that classification is at document level, with journal-level fallback, using a two-level scheme (22 divisions / 157 groups). I did not verify this. [S] — [Altmetric help, FoR filter](https://help.altmetric.com/en/articles/9804289)
  - Because FoR is applied per document, Dimensions can count SSH books and chapters, not just journals. Access and cost details are in indexed_publications_and_denominators.md.
- **Scopus ASJC.** "Serial titles are classified using the ASJC (All Science Journal Classification) scheme. This is done by in-house experts at the moment the serial title is set up for Scopus coverage; the classification is based on the aims and scope of the title, and on the content it publishes." The "Social Sciences" supergroup lists Arts and Humanities; Business, Management and Accounting; Decision Sciences; Economics, Econometrics and Finance; Psychology; Social Sciences. Page last updated 15 Aug 2024. [P] — [Elsevier Scopus support](https://www.elsevier.support/scopus/answer/what-are-scopus-subject-area-categories-and-asjc-codes)
  - Scopus field counts are therefore source-level (journal or series) and multi-assigned, not article-level.
  - A 2015 Elsevier workshop deck said book content matters mainly for SSH and A&H (421 book series, 28k volumes, dated). [S] — [UI workshop deck 2015](https://research.ui.ac.id/research/wp-content/uploads/2015/05/Journal-Editors-Workshop-UI-28-May-2015-FINAL_for-Printing.pdf)

#### Documented SSH coverage biases (bibliometric literature)
- **Mongeon & Paul-Hus (Scientometrics, online 19 Oct 2015).** They compared active journals in WoS (13,605) and Scopus (20,346) with Ulrich's (63,013). Either database "may introduce biases that favor Natural Sciences and Engineering as well as Biomedical Research to the detriment of Social Sciences and Arts and Humanities. Similarly, English-language journals are overrepresented." [P: abstract via Semantic Scholar] — [DOI](https://doi.org/10.1007/s11192-015-1765-5); [S2 API](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s11192-015-1765-5?fields=title,abstract,year)
- **Martín-Martín, Thelwall, Orduna-Malea & Delgado López-Cózar (Scientometrics, online 21 Sep 2020).**
  - Data: 3,073,351 citations to 2,515 highly cited 2006 English-language documents, across 252 subject categories.
  - Google Scholar found 88% of all citations.
  - Microsoft Academic "had coverage gaps in some areas, such as Physics and some Humanities categories".
  - Dimensions found 54% of citations, with "some coverage gaps".
  - [P: abstract] — [DOI](https://doi.org/10.1007/s11192-020-03690-4)
- **Visser, van Eck & Waltman (QSS 2021).** A large-scale comparison of Scopus, WoS, Dimensions, Crossref and Microsoft Academic (2008–2017), including differences "per document type, and … per discipline". It is a methods anchor for choosing a denominator. [P: abstract] — [DOI](https://doi.org/10.1162/qss_a_00112)
- **Céspedes et al. (JASIST, 14 Jan 2025).**
  - "OpenAlex exhibits a far more balanced linguistic coverage than WoS. However, language metadata are not always accurate, which leads OpenAlex to overestimate the place of English while underestimating that of other languages."
  - Based on manual validation of 6,836 articles.
  - [P: abstract] — [DOI](https://doi.org/10.1002/asi.24979)
- **Kulczycki et al. (Scientometrics, 26 Mar 2018).**
  - Data: 74,022 peer-reviewed 2014 SSH publications in eight national databases (CZ, DK, FI, Flanders, NO, PL, SK, SI), plus 272,376 for 2011–2014.
  - Language and publication-type patterns differ by field and by country. They are stable in Western and Nordic countries and changing in Central and Eastern Europe.
  - [P: abstract] — [DOI](https://doi.org/10.1007/s11192-018-2711-0)
- **Engels, Istenič Starčič, Kulczycki, Pölönen & Sivertsen (Aslib JIM, 31 Oct 2018).**
  - Using comprehensive national databases (VABB-SHW Flanders, VIRTA Finland, NSI Norway, PBN Poland, COBISS Slovenia), "book publishing is not disappearing from an SSH".
  - Shares of monographs and chapters vary by field and country.
  - [P: abstract] — [DOI](https://doi.org/10.1108/AJIM-05-2018-0127)
- **Classic references (metadata only).** Sivertsen & Larsen, "Comprehensive bibliographic coverage of the SSH in a citation index" (Scientometrics, 2012). Archambault et al., "Benchmarking scientific output in the SSH: the limits of existing databases" (Scientometrics, 2006). Their abstracts were unavailable via Crossref and Semantic Scholar, so I cite them for existence only. [P: metadata] — [Sivertsen & Larsen](https://doi.org/10.1007/s11192-011-0615-3); [Archambault et al.](https://doi.org/10.1007/s11192-006-0115-z)

### Inferences
- **Yearly SSH counts from OpenAlex without a key** require scanning the works snapshot. Filter `is_xpac=false`, group by `primary_topic.field.id` (or `.subfield.id`) and `publication_year`, and pin one release.
  - Use primary-topic fields, not entity `works_count`, which overlaps across domains via `topics.*`.
  - For humanities, read field 12 and its subfields. The "Social Sciences" domain mixes humanities, economics, business and psychology.
- **The ×3.4 jump in the Arts and Humanities stock** between the 2024 and 2026 versions makes OpenAlex A&H shares especially version-sensitive. Pre/post-2022 comparisons must use a single snapshot. The 6 Oct 2026 topic re-assignment matters too: field mix is 97% stable at the median institution, but individual fields can move more.
- **Crossref's book-type series are free and yearly but have no discipline tag.** Their 2023 chapter peak and the 2024 drop look like deposit artefacts, not output.
  - Edited-book DOIs doubled 2019→2025 (+111%, my calc), more likely from wider DOI adoption by book publishers than from AI.
  - For SSH books, DOAB/OAPEN (Thema codes, Q2) or national CRIS databases (VABB, NSI/Cristin, VIRTA, PBN) are better.
- **Coverage biases imply under-counting of SSH output**, especially books, non-English work and national journals, in WoS and Scopus and to a lesser extent OpenAlex. Any AI-era change measured on these indexes partly reflects indexing policy for SSH.

### Gaps
- I did not verify OpenAlex documentation stating which entities have `counts_by_year`, or the exact window rule. The 2014–2026 range was observed on publisher records only; authors, sources and institutions were not checked.
- I did not obtain a current Scopus Content Coverage Guide (the Elsevier PDF URL returned 404), so I have no current SSH share of Scopus titles.
- The ANZSRC 2020 SSH divisions (Economics, Education, History, Human Society, Language, Law, Philosophy, Psychology, Creative Arts, Commerce) are from background knowledge; I did not check the Dimensions mapping or division list this session.
- The exact day Crossref's `subject` data went empty after the 13 Mar 2024 announcement was not established.

## 2. SSH-specific publication, preprint, book and thesis sources: counts over time, access, breaks

### Takeaway
Several SSH sources give free yearly counts:
- HAL (keyless facets by domain and year)
- ERIC (keyless counts by year and peer-review flag)
- The OSF family (keyless API; versions must be removed since April 2025)
- Knowledge Commons/KC Works (InvenioRDM API)
- theses.fr (API with facets)
- DOAB/OAPEN (CSV export; REST blocked for us)

RePEc gives native stock counts and annual additions via EconPapers and its blog, and SSRN gives year-end totals.

Most show a strong 2025–2026 rise, but nearly every series has a contemporaneous break: versioning, scope rules, bulk imports, platform migrations or bot traffic. PhilPapers/PhilArchive, SSRN, OATD and DART-Europe blocked direct access (403).

### Cited Findings

#### SSRN (native statistics only; Crossref series already in preprints_and_submissions.md §3)
- **End-2025 total.** "As of the end of 2025, its electronic library contained over 1,771,791 full-text documents by more than 2,543,222 authors." (Harvard Law School Forum post, 19 Jan 2026, quoting SSRN figures.) [P: verified in the post's feed] — [HLS Forum post](https://corpgov.law.harvard.edu/2026/01/19/harvard-corporate-faculty-excels-in-ssrns-2025-citation-rankings/); [feed copy](https://corpgov.law.harvard.edu/2026/01/19/harvard-corporate-faculty-excels-in-ssrns-2025-citation-rankings/feed/)
- **Undated homepage counters (search snippets).** 1,889,856 abstracts, 1,730,972 full-text papers and 2,765,682 authors; another snapshot shows 1,912,733 abstracts and 1,753,766 full-text papers, with 380–385M downloads to date and 52.9M in the last 12 months. These are inconsistent with each other and with the end-2025 figure. [S] — [papers.ssrn.com](https://papers.ssrn.com/)
- **Access.** ssrn.com returned HTTP 403 to scripted requests; no public API was found (consistent with preprints_and_submissions.md). [V]
- **AI-impact evidence that uses SSRN.** It is already in ai_impact_measurement_studies.md:
  - Kusumegi et al., *Science* 2025: SSRN adopters +59.8% output, vs arXiv +36.2% and bioRxiv +52.9%.
  - Zhao et al. 2026: SSRN has the highest hallucinated-citation rate (1.91%).

#### RePEc / IDEAS / EconPapers / LogEc (economics)
- **Stock, 15 Oct 2026 (EconPapers)** [V] — [EconPapers](https://econpapers.repec.org/)
  - 1,323,265 working papers (1,117,470 downloadable) in 5,934 series
  - 3,828,117 journal articles in 4,739 journals
  - 73,429 books; 341,650 chapters; 6,098 software items
  - "a total of 5,572,559 searchable working papers, articles and software items"
- **IDEAS** indexes "over 5,500,000 items of research", with metadata from "over 2,400 participating archives". IDEAS search offers a publication-year filter (the dropdown lists 2026 back to at least 1993). [V] — [IDEAS](https://ideas.repec.org/)
- **Annual additions (RePEc blog year-end posts)** [P]:
  - 2019: 66,000 working papers and 167,000 articles (search-relayed figure). [S] — [blog 2019](https://blog.repec.org/page/13/)
  - 2021: "added 439,000 research items, including 123,000 working papers and 303,000 journal articles". — [blog Jan 2022](https://blog.repec.org/2022/01)
  - 2024: "100 working papers series, 45,000 working papers, 120 journals, 200,000 articles, … 2,500 new books and 20,000 new book chapters (numbers rounded)". — [blog Jan 2025](https://blog.repec.org/2025/01)
  - 2025: "48 new RePEc archives … 220 new working paper series, 70,000 new working papers, 260 new journals, 260,000 new journal articles, 56,000 new book chapters, 7,000 new books … 4,200 NEP reports were issued". — [blog 11 Jan 2026](https://blog.repec.org/2026/01)
  - Milestones: first million items January 2011, second December 2017, third December 2019. — [blog Dec 2019](https://blog.repec.org/2019/12)
- **Usage-statistics break (LogEc).** Sept 2026: 355,302 downloads and 2,223,081 abstract views. "Since October 2025 there has been a large increase in traffic at RePEc services. We believe this is due to AI tools and robots that are masquerading as real users. The statistics on abstract views are… influenced by this while the download statistics should still be a reliable indicator of human interest." Bot-detection algorithms were also updated in January 2022. [V] — [LogEc](https://logec.repec.org/)
  - The 2025 look-back adds that RePEc "struggled with AI bots" and that its sites are being rewritten from scratch (2026). [P] — [blog Jan 2026](https://blog.repec.org/2026/01)
- **Catalog entry.**
  - Counts metadata records deposited by participating archives (working papers, articles, books, chapters).
  - Annual additions reflect archive onboarding, not production year.
  - Stocks are free (HTML); bulk metadata is via RePEc's FTP/OAI (not tested).
  - Breaks: archive onboarding waves; AI-bot traffic in usage data from Oct 2025.
  - Suitability: working-paper additions are a rough flow (45k in 2024 → 70k in 2025, +56%, my calc) confounded by new archives (48 in 2025).

#### OSF-hosted SSH preprint servers (native API; Crossref DOI series in preprints_and_submissions.md §3)
- **Access.** `api.osf.io/v2/preprints/?filter[provider]=<id>&filter[date_created][gte]=…` returns `links.meta.total` without a key. 32 preprint providers are listed, including socarxiv, psyarxiv, edarxiv, lawarxiv, lawarchive, mindrxiv, metaarxiv, lissa, thesiscommons, acctrt. [V] — [providers](https://api.osf.io/v2/providers/preprints/); [example](https://api.osf.io/v2/preprints/?filter%5Bprovider%5D=socarxiv&filter%5Bdate_created%5D%5Bgte%5D=2024-01-01&filter%5Bdate_created%5D%5Blt%5D=2025-01-01&page%5Bsize%5D=1)
- **All records by `date_created` year (versions included)** [V]:

  | Provider | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 to 15 Oct |
  |---|---|---|---|---|---|---|---|---|---|---|
  | SocArXiv | 1,165 | 1,262 | 1,589 | 2,235 | 2,629 | 2,238 | 2,299 | 2,170 | 4,140 | 5,170 |
  | PsyArXiv | 992 | 2,357 | 3,588 | 6,248 | 6,733 | 6,299 | 6,722 | 6,726 | 14,317 | 11,091 |
  | EdArXiv | 0 | 0 | 72 | 514 | 243 | 217 | 324 | 280 | 702 | 1,372 |
  | Law Archive (lawarchive) | 376 | 478 | 197 | 136 | 6 | 0 | 11 | 29 | 158 | 450 |
  | MetaArXiv | 19 | 15 | 51 | 102 | 102 | 146 | 92 | 72 | 190 | 270 |
  | Thesis Commons | 94 | 233 | 176 | 386 | 393 | 586 | 301 | 310 | 288 | 102 |

  - LawArXiv (≤67/yr), MindRxiv (0 since 2023), LISSA and Accounting Research & Thought are negligible.
- **Versioning break (April 2025).** The API lists every version as its own record (IDs `xxxxx_v1`, `_v2`, …).
  - In a sample of 100 PsyArXiv records created in March 2025, 40 were v2+ and there were 91 distinct base IDs. [V] — [March-2025 page](https://api.osf.io/v2/preprints/?filter%5Bprovider%5D=psyarxiv&filter%5Bdate_created%5D%5Bgte%5D=2025-03-01&filter%5Bdate_created%5D%5Blt%5D=2025-04-01&page%5Bsize%5D=100)
  - SocArXiv announced "New versioning capacity" on 13 Apr 2025, adding that new versions are moderated. [P] — [SocOpen news](https://socopen.org/news-and-essays)
- **New papers only (v1 records, full paging)** [V]:
  - SocArXiv: 2023 2,299; 2024 2,170; 2025 **3,088** (of 4,140 records); 2026 to 15 Oct **3,850** (of 5,170).
  - EdArXiv: 2023 324; 2024 280; 2025 **569** (of 702); 2026 to 15 Oct **1,129** (of 1,372).
  - PsyArXiv: 2025 **8,748** (of 14,317 records; 5,569 later versions; 10,455 distinct base IDs); 2026 to 15 Oct **6,805** (of 11,093).
    - The 2024 figure (6,726) is all v1. I infer this rather than paging it: versions created in 2025+ carry their own `date_created`, and every SocArXiv/EdArXiv record dated 2023–2024 was v1.
    - [V] — [PsyArXiv 2025 query (paged)](https://api.osf.io/v2/preprints/?filter%5Bprovider%5D=psyarxiv&filter%5Bdate_created%5D%5Bgte%5D=2025-01-01&filter%5Bdate_created%5D%5Blt%5D=2026-01-01&page%5Bsize%5D=100)
  - My calc, new-paper growth:
    - SocArXiv +42% in 2025; 2026 annualises to ~4,880 (another +58%).
    - EdArXiv roughly doubled in 2025 and again in 2026.
    - PsyArXiv +30% in 2025 (6,726 → 8,748); 2026 annualises to ~8,620 (flat).
  - Raw versus v1 growth, 2024→2025: SocArXiv +91% vs +42%; PsyArXiv +113% vs +30%; EdArXiv +151% vs +103%. Versions are 25%, 39% and 19% of 2025 records respectively.
  - Cross-check: SocArXiv's own 17 Feb 2026 post says 355 new papers accepted in 30 days imply "an annual pace of about 4,300 papers, which would be 37% above the 2025 pace", i.e., ~3,140 in 2025. That matches my 3,088. [P] — [SocOpen news](https://socopen.org/news-and-essays)
- **SocArXiv scope and policy breaks** [P] — [Announcements](https://socopen.org/category/announcements/); [moratorium post](https://socopen.org/2025/11/27/socarxiv-moratorium-on-ai-topic-papers-policy-in-formation/)
  - 19 Nov 2025: ORCID required; arts and humanities papers now rejected and redirected to Knowledge Commons (education and law still accepted).
  - 27 Nov 2025: 90-day pause on AI-topic papers.
  - 9 Mar 2026: AI policy published.
  - Details are in Q4.

#### HAL (France) — SHS domain
- **Access.** Keyless Solr API (`api.archives-ouvertes.fr/search`) with facets on `level0_domain_s` (shs), `level1_domain_s` (shs.droit, shs.eco…), `docType_s`, `submittedDateY_i` (deposit year), `producedDateY_i` (production year) and `submitType_s` (file = full text). Free. [V] — [domain facet](https://api.archives-ouvertes.fr/search/?q=*:*&rows=0&wt=json&facet=true&facet.field=level0_domain_s)
- **Size (15 Oct 2026).** 4,703,138 records in total, of which SHS 1,832,151 (39.0%, my calc). [V]
  - SHS document types: ART 693,402; COMM 365,503; COUV (chapters) 327,653; OUV (books) 103,246; THESE 40,773; HDR 2,595.
  - SHS sub-domains: droit 239,666; hist 213,696; litt 142,738; archeo 129,699; socio 119,823; eco 101,751; geo 96,595; langue 89,294; edu 87,242; gestion 86,331; scipo 82,910; art 79,802; phil 47,963; psy 35,346.
  - [V] — [docType facet](https://api.archives-ouvertes.fr/search/?q=*:*&rows=0&wt=json&fq=level0_domain_s:shs&facet=true&facet.field=docType_s); [level1 facet](https://api.archives-ouvertes.fr/search/?q=*:*&rows=0&wt=json&fq=level0_domain_s:shs&facet=true&facet.field=level1_domain_s)
- **SHS deposits by year** (all records / full-text only) [V] — [deposit-year facet](https://api.archives-ouvertes.fr/search/?q=*:*&rows=0&wt=json&fq=level0_domain_s:shs&facet=true&facet.field=submittedDateY_i&facet.limit=200&facet.sort=index); [full-text](https://api.archives-ouvertes.fr/search/?q=*:*&rows=0&wt=json&fq=level0_domain_s:shs&fq=submitType_s:file&facet=true&facet.field=submittedDateY_i&facet.limit=200&facet.sort=index)
  - 2016 51,873 / 20,763
  - 2017 82,160 / 23,765
  - 2018 97,566 / 34,483
  - 2019 168,035 / 31,278
  - 2020 179,093 / 47,826
  - 2021 145,375 / 43,203
  - 2022 138,893 / 38,731
  - 2023 180,116 / 48,827
  - 2024 177,417 / 50,881
  - 2025 188,474 / 51,880
  - 2026 to 15 Oct 137,545 / 37,213
- **SHS by production year:** 2018 98,419; 2019 101,571; 2020 88,664; 2021 103,973; 2022 104,470; 2023 99,940; 2024 94,964; 2025 86,469 (deposit lag). [V] — [production-year facet](https://api.archives-ouvertes.fr/search/?q=*:*&rows=0&wt=json&fq=level0_domain_s:shs&facet=true&facet.field=producedDateY_i&facet.limit=300&facet.sort=index)
- **Breaks** [V]:
  - SHS articles deposited went from 32,492 (2018) to 91,330 (2019), consistent with a bulk import (cause unverified).
  - All-domain deposits spiked to 576,985 in 2020, vs 352,363 in 2019 and 317,526 in 2021.
  - [all-domain deposits](https://api.archives-ouvertes.fr/search/?q=*:*&rows=0&wt=json&facet=true&facet.field=submittedDateY_i&facet.limit=200&facet.sort=index)
- **Suitability.** Full-text SHS deposits are the cleaner flow: +26% in 2023 and +34% from 2022 to 2025 (my calc), against +24% from 2019 to 2022. That suggests acceleration but is confounded by French open-access mandates; the national open-science plan is not checked here.

#### ERIC (education; IES)
- **Access.** Keyless API `api.ies.ed.gov/eric/?search=…&format=json`, returning `numFound`. It supports fields such as `publicationdateyear` and `peerreviewed:T`. [V] — [example](https://api.ies.ed.gov/eric/?search=publicationdateyear:2023&format=json&rows=0)
- **Records by publication year** (total / peer-reviewed) [V] — [peer-reviewed query example](https://api.ies.ed.gov/eric/?search=publicationdateyear:2023%20AND%20peerreviewed:T&format=json&rows=0)

  | Year | Total | Peer-reviewed |
  |---|---|---|
  | 1995 | 33,209 | 17,525 |
  | 2000 | 32,119 | 16,990 |
  | 2005 | 31,071 | 24,805 |
  | 2010 | 46,066 | 33,367 |
  | 2011 | 46,404 | — |
  | 2012 | 50,789 | 37,403 |
  | 2013 | 43,302 | — |
  | 2014 | 35,530 | 29,322 |
  | 2015 | 36,934 | 31,940 |
  | 2016 | 42,497 | 35,882 |
  | 2017 | 44,978 | 36,109 |
  | 2018 | 45,565 | 36,931 |
  | 2019 | 45,971 | 38,659 |
  | 2020 | 49,002 | 41,791 |
  | 2021 | 56,014 | 45,100 |
  | 2022 | 55,707 | 44,738 |
  | 2023 | 53,560 | 41,965 |
  | 2024 | 55,539 | 44,446 |
  | 2025 | 45,591 (incomplete) | 41,431 |
  | 2026 to 15 Oct | 21,608 | 19,594 |

- **Breaks** (my calc on the table):
  - A drop from 2012 to 2014 (−30%), probably a source-list change (cause unverified).
  - A rise in the peer-reviewed share from 53% (2000) to 78% (2023).
  - A 2021 jump of +14% that predates ChatGPT.
  - Indexing lag for 2025–2026.
- **Suitability.** ERIC is selective, so it measures indexing policy as much as output. It is useful as a curated education counter with an abstract corpus for LLM-marker studies.

#### PhilPapers / PhilArchive (philosophy)
- philpapers.org and philarchive.org returned HTTP 403 to curl and WebFetch. [V]
- PhilArchive homepage snapshots from early 2026 show about 122,097–122,465 works and 6,146 topics. [S] — [PhilArchive](https://philarchive.org/)
- No time series or API was verified. OAI-PMH exists per PhilPapers documentation (not tested).

#### Open-access books: DOAB and OAPEN
- **REST APIs blocked.** `directory.doabooks.org/rest/search` and `library.oapen.org/rest/search` answered "You address is not allowed to access this API." [V] — [DOAB REST](https://directory.doabooks.org/rest/search?query=dc.date.issued:2023&expand=metadata&limit=1)
- **What works.** OAI-PMH (`/oai/request`) and full CSV exports. [V] — [DOAB OAI](https://directory.doabooks.org/oai/request?verb=Identify); [DOAB CSV export](https://directory.doabooks.org/download-export?format=csv); [OAPEN CSV export](https://library.oapen.org/download-export?format=csv)
- **The CSV exports are stale.** The latest `dc.date.accessioned` is 2025-10-22 (DOAB, 280.8 MB) and 2025-10-24 (OAPEN, 112.3 MB), even though they were served on 15 Oct 2026. [V]
- **DOAB** (102,078 records: 92,260 books, 9,818 chapters) [V]:
  - By `dc.date.issued`: 2015 3,142; 2018 6,666; 2019 6,687; 2020 8,923; 2021 8,076; 2022 9,114; 2023 10,090; 2024 6,556; 2025 5,946 (lagged).
  - SSH-only titles, coded by me as Thema/BIC top-level A, C, D, H, J, K, L, N or Q and no M/P/T/R/U: 2019 2,410; 2020 3,078; 2021 3,447; 2022 3,559; 2023 3,730; 2024 3,067; 2025 2,772.
  - `dc.date.accessioned` piles up in 2021 (43,407), a platform-migration artefact, so DOAB "date added" is unusable before 2021.
- **OAPEN** (42,938 records: 36,434 books, 6,504 chapters) [V]:
  - Issued 2019 2,507; 2020 3,210; 2021 3,838; 2022 4,482; 2023 5,083; 2024 4,392; 2025 3,140.
  - Accessioned 2018 2,220; 2019 3,767; 2020 4,587; 2021 4,483; 2022 7,066; 2023 5,546; 2024 5,981; 2025 5,222 (to 24 Oct).
  - Most common Thema top levels: J (society and social sciences) 15,162; N (history/archaeology) 6,741; K (economics/business) 3,938; D (literature) 3,766.
- **Suitability.** Subject-coded OA-book counts. Driven by funder OA-book mandates and publisher programmes, so they have weak AI identification.

#### Knowledge Commons (hcommons.org) — KC Works
- **Access.** Keyless InvenioRDM API at `works.hcommons.org/api/records`, with aggregations by resource type, language, file type and access. [V] — [API](https://works.hcommons.org/api/records?size=1)
- **Size (15 Oct 2026).** 46,437 records: textDocument 40,208; presentation 2,413; English 32,802; Spanish 4,622; German 1,129. [V]
- **Records by `created` year:** 2016 435; 2018 2,419; 2020 2,829; 2021 4,976; 2022 3,114; 2023 6,140; 2024 4,557; 2025 6,117; 2026 to 15 Oct 9,370. [V] — [example year query](https://works.hcommons.org/api/records?size=1&q=created:%5B2025-01-01%20TO%202025-12-31%5D)
- **Break.** Since 19 Nov 2025 SocArXiv redirects rejected arts and humanities papers to KC Works. [P] — [SocArXiv announcement](https://socopen.org/category/announcements/)
  - The 2026 surge (+53% over all of 2025 by mid-October, my calc) is therefore partly a diversion from SocArXiv.
  - The newest record seen carried an SSRN DOI (10.2139/ssrn.5394533), so cross-posting occurs. [V]

#### Theses databases
- **theses.fr (France, ABES).** Keyless API.
  - `recherche` returns 568,192 records. The facets give: defended ("soutenue") 487,165, of which 172,018 are accessible online; in progress ("enCours") 81,027; language fr 427,232 and en 87,909.
  - Facets include *Disciplines* (4,000 free-text values) and *Domaines thématiques* (98), plus institutions and doctoral schools.
  - [V] — [search](https://theses.fr/api/v1/theses/recherche/?q=*&debut=0&nombre=1); [facets](https://theses.fr/api/v1/theses/facets/?q=*)
  - ABES is also the largest Crossref dissertation-DOI registrant (194,782). [V]
- **EThOS (British Library).** Back online: "EThOS (E-Theses Online Service) is now available again following restoration work", with "metadata of over 650,000 UK doctoral theses". It is a discovery-only platform (Hyku, provided by CoSector, University of London). [V] — [ethos.bl.uk](https://ethos.bl.uk/)
  - Stirling University's library dated the restoration notice 13 Jul 2026. Theses go back to "the 1700s onwards", and EThOS no longer handles digitisation requests. [P] — [Stirling IS News](https://isnews.stir.ac.uk/2026/07/13/ethos-is-back/)
  - Secondary reports say: all previous records were restored plus ~14,000 added; a Sept 2025 BL update targeted end-2025; THE (Jan 2026) reported no firm timeline. [S] — [feedbagel repost](https://feedbagel.com/post/ethos-records-restored); [THE](https://www.stg.timeshighereducation.com/node/741086)
  - It had been offline since the October 2023 cyberattack.
- **TESEO (Spain).** "contiene una base de datos con información de las tesis doctorales publicadas desde el año 1976". The ministry page publishes no statistics. [P] — [Ministerio TESEO page](https://www.ciencia.gob.es/Universidades/TESEO.html)
  - The TESEO query app returned HTTP 426 to curl. [V]
  - A move to a new TESEO platform from 26 Nov 2025 is claimed only in a search summary (unverified). [S]
  - Coverage of about 87.3% of Spanish theses comes from an older study. [S] — [REDC article](https://redc.revistas.csic.es/index.php/redc/article/download/913/1308/3224)
- **OATD and DART-Europe** returned HTTP 403, so I could not verify them. [V]
- **ProQuest Dissertations & Theses Global** is paid and was not tested.

### Inferences
- **Usable keyless SSH flow series with 2015+ history:** HAL SHS (full-text deposits), ERIC (by year, peer-reviewed flag), OSF servers (deduplicated to v1), KC Works, theses.fr, and the DOAB/OAPEN exports (books, Thema-coded).
  - RePEc and SSRN give stocks and annual additions only.
  - PhilArchive and SSRN require archived snapshots or partnerships.
- **The 2025–2026 SSH preprint surge is real after deduplication**, but heterogeneous: SocArXiv v1 +42% in 2025 and accelerating in 2026; EdArXiv v1 about ×2 in 2025 and again in 2026; PsyArXiv v1 +30% in 2025 and flat in 2026. Three things confound it:
  - versioning (raw record counts more than double the true 2025 growth for PsyArXiv and SocArXiv);
  - SocArXiv's Nov 2025 scope and ORCID rules (which reduce counts) and its humanities diversion to KC Works (which inflates KC);
  - moderation backlogs.
- **For a STEM-vs-SSH difference-in-differences:**
  - Pair OSF SSH servers (v1) with arXiv/bioRxiv, which are in the sibling notes.
  - Use HAL full-text deposits by domain within one system: shs vs info/sdv/phys.
  - HAL is especially attractive because SHS and STEM share the same platform, mandates and import shocks.
- **RePEc and LogEc usage data after Oct 2025 are contaminated by AI bots**, by the operators' own account. Abstract-view series should not be used as demand measures for 2025–2026.

### Gaps
- **OSF v1 counts before 2023** were not paged; earlier years predate versioning, so all records are presumably v1. MetaArXiv and Law Archive 2025–2026 were not deduplicated.
- **SSRN** has no official per-year series by network (e.g., LSN, ERN, SSRN Education). I found no SSRN statement on AI-generated submissions or screening.
- **HAL:** I did not establish the cause of the 2019 SHS article import or the 2020 all-domain spike.
- **ERIC:** I did not establish the cause of the 2013–2014 drop.
- **PhilPapers/PhilArchive:** blocked; no historical counts.
- **OATD, DART-Europe, ProQuest:** unverified.
- **theses.fr:** I did not extract a per-year defended-theses series by discipline; the API supports it via filters, which I did not test.
- **Spain:** I found no official national thesis statistics by branch for 2020–2025.

## 3. SSH grants and scholarships: who publishes application counts by discipline, and since when

### Takeaway
**Long or official SSH series:**
- **ERC** publishes submitted proposals by domain (SH) for every call press release (verified for 2024–2026 calls).
- **SSHRC** Insight Grant competition statistics (2021–2025) show eligible applications up 82%.
- **UKRI's** investment-and-outputs workbook splits AHRC and ESRC (already in grant_applications.md).
- **NSF SBE** publishes division-level actions and awards for the latest fiscal year only.

**US humanities break.** NEH is the largest structural break in US humanities funding. In FY2025 it received "over 4000 applications" but terminated ~1,477 grants and cut ~70% of staff. The FY2026 request proposed closing it, and 2026 fellowships were restricted to American history and culture and Western civilization themes.

**Partial or missing:** DFG, ANR, NWO and AEI publish SSH breakdowns only partially (charts or pooled figures) or I could not find them. The British Academy figures available are secondary.

### Cited Findings

#### ERC — Social Sciences and Humanities (SH) domain, submitted proposals per call
Preliminary submitted counts from ERC "facts and figures" releases. [P] — [StG 2025](https://erc.europa.eu/news-events/news/starting-grants-2025-applications-facts-and-figures); [StG 2026](https://erc.europa.eu/news-events/news/starting-grants-2026-applications-facts-and-figures); [CoG 2025](https://erc.europa.eu/news-events/news/applications-erc-consolidator-grants-2025-facts-and-figures); [CoG 2026](https://erc.europa.eu/news-events/news/applications-erc-consolidator-grants-2026-facts-and-figures); [AdG 2024](https://erc.europa.eu/news-events/news/applications-erc-advanced-grants-2024-facts-and-figures); [AdG 2025](https://erc.europa.eu/news-events/news/applications-erc-advanced-grants-2025-facts-and-figures)

| Call (closing) | Total | SH (share) | PE | LS |
|---|---|---|---|---|
| StG 2025 (15 Oct 2024) | 3,928 | 1,187 (30%) | 1,660 | 1,081 |
| StG 2026 (14 Oct 2025) | 4,807 | 1,568 (33%) | 1,980 | 1,257 |
| CoG 2025 | 3,121 | 1,033 (33%) | 1,268 | 820 |
| CoG 2026 | 3,060 | 1,086 (35.5%) | 1,238 | 736 |
| AdG 2024 (29 Aug 2024) | 2,534 | 736 (29.0%, my calc) | 1,068 | 730 |
| AdG 2025 (28 Aug 2025) | 3,329 | 1,013 (30.4%, my calc) | 1,341 | 975 |

- **Growth, my calc:**
  - StG 2025→2026: SH +32.1% vs PE +19.3% and LS +16.3%.
  - CoG 2025→2026: SH +5.1% vs PE −2.4% and LS −10.2%.
  - AdG 2024→2025: SH +37.6% vs PE +25.6% and LS +33.6%.
- Call totals and success rates are in grant_applications.md.
- Panel-level (SH1–SH8) statistics exist in ERC per-call statistics documents; I did not retrieve them.

#### SSHRC (Canada) — Insight Grants competition statistics
Source: SSHRC Insight Grants webinar deck (2026), hosted by Western University, table "Insight Grant results (2021–2025)". [P, university-hosted copy] — [UWO-hosted SSHRC deck](https://www.uwo.ca/research/doc/funding/domestic/SSHRC_IG_Webinar_2026_EN.pdf)

| Competition | Eligible apps (Stream A / B / total) | Success rate A / B | Awarded A / B |
|---|---|---|---|
| Oct 2021 | 427 / 657 / 1,084 | 56.44% / 48.55% | $19.45M / $77.22M |
| Oct 2022 | 413 / 732 / 1,145 | 50.60% / 41.12% | $17.24M / $72.23M |
| Oct 2023 | 508 / 969 / 1,477 | 40.75% / 30.55% | $16.93M / $69.39M |
| Oct 2024 | 642 / 1,078 / 1,720 | 44.9% / 37.6% | $24.34M / $103.34M |
| Oct 2025 | 884 / 1,089 / 1,973 | 45.5% / 37.3% | $40.10M / $122.62M |

- **Growth, my calc:** eligible applications +82% (2021→2025), +72% (2022→2025), +16% (2023→2024) and +15% (2024→2025).
- **Consistency check.** The Oct 2022 figure (1,145) matches the "Insight Grants 2023–24: 1,145 eligible applications" already in grant_applications.md.
- **Break in stream definitions.** The 2024 competition used Stream A $7,000–$100,000 and Stream B $100,001–$400,000; the 2025 competition used $10,000–$125,000 and $125,001–$500,000. [P] — [SSHRC IG 2024 competition](https://sshrc-crsh.canada.ca/en/funding/opportunities/insight-grants/2024/competition.aspx); [IG 2025 competition](https://sshrc-crsh.canada.ca/en/funding/opportunities/insight-grants/2025/competition.aspx)
- **Demand-management rules.** "Individuals can apply, as an applicant, for only one Insight Grant at a time." Since 2017 an exception lets unsuccessful February IDG applicants apply to the October IG. [P] — [IG 2024 competition](https://sshrc-crsh.canada.ca/en/funding/opportunities/insight-grants/2024/competition.aspx)

#### NEH (US) — application volumes and the 2025–2026 break
- **Typical volume (FY2025 Congressional Justification, Mar 2024).** "The Research Division receives around 2,500 applications a year—two-thirds of all applications received by the Agency—and issues almost 300 awards annually." That implies roughly 3,750 applications a year agency-wide (my calc). [P] — [NEH FY2025 CJ](https://www.neh.gov/sites/default/files/inline-files/NEH%20FY%202025%20Congressional%20Justification%20(CJ).pdf)
- **FY2025 (Performance and Accountability Report)** [P] — [NEH FY2025 PAR](https://www.neh.gov/sites/default/files/NEH%20FY2025%20PAR%20to%20OMB.pdf)
  - "The Endowment's grant programs received over 4000 applications in fiscal year 2025."
  - "NEH awarded more than $32 million in direct grant funding through 373 grant awards."
  - "the Administration initiated an agency-wide Reduction-In-Force (RIF) of close to 70% of NEH's staff."
  - "In the second half of FY 2025… NEH terminated approximately 1,477 open grant awards"; NEH is "legally enjoined from de-obligating funds".
  - A $40M supplemental appropriation (PL 119-21, July FY2025) went to the National Garden of American Heroes and America's 250th.
  - The report also cautions: "The volume of applications received by NEH typically fluctuates year over year… dependent on… the availability of appropriations, administrative and operational priorities and the number of available grant programs."
- **FY2026 President's request (May 2025)** [P] — [NEH FY2026 CJ](https://www.humanities.gov/sites/default/files/NEH%20FY%202026%20Congressional%20Justification.pdf)
  - It "proposes to terminate the National Endowment for the Humanities" with "$38 million to conduct an orderly shutdown".
  - It assumes "NEH will not invite or accept applications for grant programs that require panel review in FY 2026", with a maximum of ~59 staff.
- **2026 Fellowships notice (grants.gov).** Deadline 22 Apr 2026. "The 2026 Fellowships competition will accept only projects for research in American history and culture and Western civilization." Anticipated FY2027 funding is about $3.6M, with announcement in January 2027. [P] — [NEH 2026 Fellowships NOFO](https://apply07.grants.gov/grantsws/rest/opportunity/att/download/350942)
- **Court ruling on terminations.** A secondary report says a court found the mass termination of ~1,400 NEH grants unconstitutional (First and Fifth Amendments) and rescinded the termination letters. [S, unverified] — [grantedai listing](https://grantedai.com/grants/landmarks-of-american-history-and-culture-and-summer-institutes-national-endowment-for-the-humanities-b365b23a)

#### AHRC / ESRC (UKRI)
- **Confirmed: the UKRI workbook splits by council.** Table 2.2 of the UKRI 2015–2026 investments-and-outputs workbook gives applications assessed and award rates for each council.
  - AHRC: 1,500 → 1,529 → 1,383 → 1,522 (2022-23 to 2025-26).
  - ESRC: 1,255 → 1,092 → **1,698** → 1,293.
  - This is already extracted in grant_applications.md (Q2). [P via sibling note] — [UKRI xlsx](https://www.ukri.org/wp-content/uploads/2026/07/160726-UKRI-investments-and-outputs-data-2015-2026.xlsx)
  - The ESRC spike in 2024-25 (+55%) coincides with UKRI-wide opportunity changes and pauses, so it is budget-driven per the sibling note.

#### British Academy
- **Postdoctoral Fellowships** (528 → 798 in the 2025-26 cycle, per the RoRI dataset) are already in grant_applications.md.
- **Small Research Grants (BA/Leverhulme), 2024-25 round.** A third-party funder directory reports 1,116 applications, 231 grants and a 21% success rate. Funding is allocated by lottery among applications above a quality threshold. [S] — [hinchilla funder directory](https://www.hinchilla.com/funder-directory/the-british-academy-for-the-promotion-of-historical-philosophical-and-philological-studies)
- The BA news page ("record number of small research grants") returned HTTP 403, so official figures are unverified. [V] — [BA news](https://www.thebritishacademy.ac.uk/news/the-british-academy-awards-a-record-number-of-small-research-grants-to-support-uk-shape-research/)

#### NSF SBE (US) and GRFP
- **SBE funding rates, FY2024 only** (page published and last updated 10 Jan 2025). Proposal actions / awards / rate by division:
  - Behavioral and Cognitive Sciences 1,219 / 206 / 17%
  - Social and Economic Sciences 1,159 / 229 / 20%
  - SBE Office of Multidisciplinary Activities 243 / 69 / 28%
  - Overall 19%. Actions are counted by decision year, not receipt year.
  - [P] — [NSF SBE funding rates](https://www.nsf.gov/sbe/funding-rates)
- **GRFP change.** GRFP removed the SBE directorate (and STEM Education) from the FY2027 solicitation NSF 26-526 (25 Aug 2026). This is already verified in scholarships_and_graduate_applications.md. The break affects any GRFP series by field from 2027.
- **SBE budget.** An advocacy PDF claims SBE's FY2026 spend plan was cut to about $94M (−58% vs FY2024), with some figures marked "rumored". [S, unverified] — [advocacy PDF](https://cdn.fs.pathlms.com/Y6WJKzozTcuXoGHWBNBH)

#### DFG (Germany) — Geistes- und Sozialwissenschaften (GSW)
- The DFG Jahresbericht 2025 reports funding and approval rates in Einzelförderung by Wissenschaftsbereich for 2022–2025 (Grafik 9), but only as a chart whose values I could not reliably attribute to areas. [P] — [DFG Jahresbericht 2025](https://www.dfg.de/resource/blob/399666/dfg-jb2025.pdf)
- Text facts from the same report [P]:
  - The share of women among applicants is highest in GSW (41.7%).
  - Most Heisenberg Programme fundees are in GSW.
  - The Sozial- und Verhaltenswissenschaften subject area grew "deutlich sowohl absolut als auch prozentual" in approved volume in 2025.

#### ANR (France)
- **AAPG 2024 (final results, 25 Apr 2025).** 7,017 eligible proposals; 1,713 selected; 24.4% success (24.3% in 2023).
  - "Les taux de succès sont globalement équilibrés entre les domaines disciplinaires", with higher rates for NuMA.
  - The national "Sciences Humaines et Sociales" plan funded 9 projects (€3.9M).
  - No SHS submission count is given.
  - [P] — [ANR AAPG 2024 results](https://anr.fr/fr/resultats-de-laapg/aapg-2024/)
  - AAPG 2026 step-1 figures are in grant_applications.md.

#### NWO (Netherlands) — SSH domain (SGW)
- **Vici 2025, all domains.** 384 pre-proposals, about 10% funded. Vici 2023: 266 applications, 34 awarded. [S] — [Erasmus Magazine](https://www.erasmusmagazine.nl/en/?p=196376)
- I found no SGW-specific counts.

#### Spain — AEI
- **PID2024.** Application window 9–31 Jan 2025; budget €675M. [S] — [Ministerio PID2024 page](https://www.ciencia.gob.es/Convocatorias/2024/PID2024.html)
- Application totals (7,190 for 2024; PGC 2025) are in grant_applications.md and scholarships_and_graduate_applications.md.
- I found no applications by area (e.g., Ciencias Sociales, Humanidades).

### Inferences
- **The clearest SSH demand signal is ERC SH.** Its share of submissions rose in every scheme in the 2025–2026 calls (StG 30% → 33%, CoG 33% → 35.5%), and SH grew faster than PE and LS in StG 2026 and CoG 2026.
  - Consistent with lower writing costs mattering more in writing-intensive fields. It is equally consistent with SH-specific budget shocks elsewhere, e.g., US NEH/NSF SBE cuts pushing researchers to European funding, and UK re-association.
- **SSHRC's rise is concentrated after ChatGPT** (my calc): eligible Insight Grant applications were nearly flat from Oct 2021 to Oct 2022 (+5.6%), then rose +29% (Oct 2023), +16% (Oct 2024) and +15% (Oct 2025). The timing fits an AI effect, but it is not clean evidence because of two confounders:
  - SSHRC's own award totals jumped (Stream A+B: $86.3M in Oct 2023 → $127.7M in Oct 2024 (+48%) → $162.7M in Oct 2025 (+27%)), which raises expected returns to applying.
  - The 2025 stream re-banding raised the request ceilings.
- **NEH application counts after FY2025 are not comparable with earlier years.** Programme closures, thematic restrictions (2026 fellowships), staff cuts and the shutdown proposal dominate any AI signal. US humanities funding should be treated as a policy shock in any AI analysis.
- **For STEM-vs-SSH comparisons inside one funder,** use ERC (PE/LS/SH, every call since 2007), UKRI (council split, 2015-16 onward), NSF (directorate funding rates; latest year only on the web; earlier years need budget documents) and SSHRC vs NSERC/CIHR.

### Gaps
- ERC SH counts for calls before 2024 (2007–2023) and per-panel SH1–SH8 counts were not retrieved; they need ERC statistics PDFs or the ERC dashboard.
- NEH application counts by programme and year before FY2025 were not extracted. Budget justifications for FY2016–2024 and NEH annual reports would be needed. NEH's FY2026 actual application volume is unknown.
- British Academy: I have only secondary figures for 2024-25 Small Research Grants, and no Mid-Career Fellowship or Knowledge Frontiers series.
- DFG GSW application counts (not just rates) and ANR SHS submission counts were not found.
- NWO SGW and AEI by-area breakdowns were not found.
- NSF SBE proposal counts for FY2025 and earlier were not obtained (web page shows FY2024 only).
- SSHRC's official competition-statistics page (as opposed to the university-hosted deck) was not located, and SSHRC doctoral and postdoctoral award series were not collected. I did not verify any 2024–2025 changes to the tri-agency scholarship programmes in this session.

## 4. LLM-impact evidence specific to SSH (2023–2026): prevalence studies, submission surges and caps, editor statements, STEM vs SSH exposure

### Takeaway
SSH-specific evidence is now substantial, but mostly 2025–2026 and heterogeneous in method.
- **Economics:** AI-marker language in 25 top economics journals rose by about 3 pp in 2023 and about 7 pp in 2024.
- **Sociology:** an estimated 24.3% of abstract sentences were LLM-modified in late 2025.
- **SSRN** shows the largest adopter productivity gain (+59.8%, in the sibling notes).
- **Organization Science** submissions are up 42% since ChatGPT, attributed almost entirely to AI-generated writing.
- **JPART:** 45–50 submissions a month in autumn 2023 vs 119 in April 2026, followed by a cap from 1 Jul 2026.
- **Philosophy & Public Affairs** banned AI-authored content.
- **SocArXiv** restricted scope and paused AI-topic papers.

On STEM vs SSH exposure, the marker-word evidence points to less growth in SSH (Kousha & Thelwall), while the submission and productivity evidence points to strong SSH effects. Exposure is not clearly lower in SSH; it differs by measure.

### Cited Findings

#### Prevalence and productivity studies with SSH coverage
- **Economics — Feyzollahi & Rafizadeh, "The adoption of Large Language Models in economics research", *Economics Letters* (Apr 2025).** [P: metadata] — [DOI](https://doi.org/10.1016/j.econlet.2025.112265)
  - Data: 25 top economics journals over 24 years. Method: 25 AI-associated terms against a control set of traditional economics terms.
  - Result: AI-characteristic language rose by "nearly 5 percentage points" in 2023–24, "from about 3 percentage points in 2023 to nearly 7 in 2024". The authors call the estimates conservative.
  - [S: UMass news, 19 May 2025] — [UMass Amherst news](https://www.umass.edu/news/article/study-finds-accelerating-adoption-ai-language-models-economics-research-papers)
- **Sociology — Cao, "Visualizing the Adoption of Large Language Models across Sociology Subfields", *Socius* (Jun 2026).** [P: abstract] — [DOI](https://doi.org/10.1177/23780231261460657)
  - Data: 1.49M sociology abstracts in OpenAlex (Jan 2018–Dec 2025), with Liang et al.'s distributional α estimator.
  - Estimated LLM modification rose "from near zero before late 2022 to 24.3 percent of abstract sentences in July–December 2025".
  - "Empirical and applied areas show the highest estimated uptake, while theory-oriented subfields remain lowest."
  - Uptake is higher among younger scholars, less prestigious institutions and less prestigious outlets.
- **Cross-field — Kousha & Thelwall, *Scientometrics* (3 Apr 2026; arXiv 2509.09596).** [P: abstract] — [DOI](https://doi.org/10.1007/s11192-026-05601-5); [arXiv](https://arxiv.org/abs/2509.09596)
  - They track 12 LLM-associated terms in Scopus, WoS, PubMed, PMC, Dimensions and OpenAlex (2015–2024), plus 2.4M PMC full texts.
  - "Growth in LLM-term usage was much higher in STEM fields than in social sciences and arts and humanities."
  - Largest increases 2022–2024: delve +1,500%, underscore +1,000%, intricate +700%.
- **Management / organisation studies — Gartenberg, Hasan, Murray & Pierce, "More Versus Better: AI, Incentives, and the Emerging Crisis in Peer Review", *Organization Science* editorial (May 2026).** [P: abstract] — [DOI](https://doi.org/10.1287/orsc.2026.ed.v37.n3); [Wharton PDF](https://faculty.wharton.upenn.edu/wp-content/uploads/2026/04/More-Versus-Better.pdf)
  - "Submission volume has risen 42% since the late 2022 release of ChatGPT, while writing quality has declined. The rise in AI-generated writing accounts for nearly all of these trends."
  - AI-generated writing in reviews has also increased.
  - Editors in other disciplines report similar patterns, "not limited to our journal or to the social sciences".
- **Law — Conklin & Houston, "Measuring the Rapidly Increasing Use of Artificial Intelligence in Legal Scholarship" (SSRN, 2025).** [P: metadata] — [DOI](https://doi.org/10.2139/ssrn.5190385)
  - The method uses a detectable "AI idiosyncrasy" in legal scholarship and reports a sharp rise. The abstract was not retrieved (SSRN 403), so the findings are unverified. [S]
- **Economics working papers — Renault.** A seminar abstract describes OpenAlex-based estimates of LLM use in economics articles and working papers. It reports heterogeneity across fields, institutions and countries, and uses Italy's temporary 2023 ChatGPT ban as a quasi-natural experiment. [S] — [RITM seminar page](https://www.ritm.universite-paris-saclay.fr/?p=13184)
- **SSRN in multi-server studies** (already detailed in ai_impact_measurement_studies.md):
  - Kusumegi et al., *Science* 2025: 676K SSRN preprints; adopters +59.8% output vs +36.2% arXiv and +52.9% bioRxiv; Asian-named authors at Asian institutions +88.9% on SSRN.
  - Zhao et al. 2026: hallucinated-citation rate highest in SSRN (1.91%).

#### Journal and preprint-server submission surges, caps and policies in SSH
- **JPART (public administration).** Verified independently:
  - "When the current editors took over in autumn 2023, the journal received roughly 45 to 50 submissions per month, corresponding to around 575 submissions per year… In April 2026, JPART received 119 submissions." The journal attributes the rise "in large part" to generative AI ("the problem largely relates to Generative AI").
  - Cap from 1 Jul 2026, per author per calendar year: at most 3 submissions, of which at most 2 may be desk-rejected. It counts every listed author and resets on 1 Jan 2027.
  - [P/V] — [PMRA policy PDF](https://www.gopmra.org/assets/Secretariat/Policies/jpart-submission-cap-policy.pdf). Also in ai_policy_timeline_surveys_confounders.md; preprints_and_submissions.md had it as unverified.
- **SocArXiv (sociology and social science preprints)** [P] — [SocOpen announcements](https://socopen.org/category/announcements/); [moratorium](https://socopen.org/2025/11/27/socarxiv-moratorium-on-ai-topic-papers-policy-in-formation/); [news and essays](https://socopen.org/news-and-essays); [22 Feb 2026 essay](https://socopen.org/2026/02/22/where-should-socarxiv-draw-the-ai-line/)
  - **19 Nov 2025.** "SocArXiv is experiencing record high submission rates… we are receiving many non-research, spam, and AI-generated submissions."
    - New rules: an ORCID requirement for the submitting author; arts and humanities papers rejected and redirected to Knowledge Commons.
    - "a lot of junk and AI submissions are in the areas of religion, philosophy, and various language studies."
  - **27 Nov 2025.** "In light of record submission rates and a large volume of AI-generated slop papers…", a 90-day pause on AI-topic papers and a policy committee.
  - **17 Feb 2026.** 500 uploads of 454 unique papers in 30 days; an annual pace of ~4,300, 37% above 2025.
  - **22 Feb 2026.** An essay on where to "draw the AI line" (an arms race is unwinnable).
  - **9 Mar 2026.** AI policy published, aiming at "reducing the volume of LLM-generated content".
  - **Per-author weekly cap: conflicting reports.**
    - *Nature* (15 Oct 2026; in ai_policy_timeline_surveys_confounders.md) reports one submission per author per week.
    - A Bluesky post relayed by an aggregator says "two papers per week… we assume they are LLM-generated and reject them all". [S] — [aiweekly.co](https://aiweekly.co/fr/alerts/arxiv-limite-deux-soumissions-par-mois-pour-contrer-la-flambe-des-papiers-ia)
    - The SocOpen site (latest post 9 Mar 2026) does not state a cap.
- **Philosophy & Public Affairs (Aug 2026).**
  - After publishing an article "largely written by an AI", submitted as an experiment by Simon Goldstein, the journal prohibits "the submission of AI-authored content", meaning papers "substantially written by AI".
  - Authors must declare they did not use AI to author the paper and must describe AI use in the research. The journal will use detection software; false declarations lead to rejection or retraction and a submission ban.
  - [S: Daily Nous, 24 Aug 2026] — [Daily Nous](https://dailynous.com/2026/08/24/after-experiment-journal-decides-to-prohibit-ai-authored-content/)
- **Bioethics / medical ethics (philosophy-adjacent; Jul 2026).**
  - *Bioethics* editor Udo Schuklenk: "We recently received a double-digit number of submissions from authors in the Far East… where we had strong evidence of machine generated content." He also said: "We don't currently have detection tools available to assist us in making reliable determinations."
  - A *Journal of Medical Ethics* article was retracted after critics documented fabricated references.
  - [S: Daily Nous, 20 Jul 2026, quoting the editorial doi:10.1111/bioe.70100] — [Daily Nous](https://dailynous.com/2026/07/20/a-scene-from-the-ai-flooding-of-academic-journals/)
- **Unnamed philosophy journal.** A blog reports that over 40% of recent submissions were significantly or entirely AI-generated, and 60–80% more likely to be desk-rejected. [S, unverified, journal not named] — [realnous substack](https://realnous.substack.com/p/time-for-slow-philosophy)
- **Cross-publisher context.** ScholarOne journals reportedly saw +33% submissions in Q1 2026 vs Q1 2025, after +17% in 2025. This is secondary and not SSH-specific. [S] — [AcademicJobs news](https://www.academicjobs.com/research-publication-news/2026-journal-submissions-surge-33percent-on-scholarone-or-academicjobs-26524)
- **Usage-side contamination.** RePEc/LogEc attribute traffic increases since Oct 2025 to "AI tools and robots that are masquerading as real users". [V] — [LogEc](https://logec.repec.org/)
- **Other SSH items already in ai_policy_timeline_surveys_confounders.md:**
  - the *[in education]* submission closure to 10 Aug 2026;
  - a Chronicle piece (Aug 2026) on editors seeing submissions "doubled or even tripled".

### Inferences
- **Exposure by measure:**
  - **Marker-word measures** (Kousha & Thelwall) show smaller growth in SSH than in STEM.
  - **Distributional estimates in sociology** (24.3% of sentences, Jul–Dec 2025) use the same α-estimator family as Liang et al. Liang et al. put arXiv computer science at 22.5% to Sep 2024 (ai_impact_measurement_studies.md). The two are similar in level, but the sociology window is about a year later, so this does not show that sociology matches CS at the same date.
  - **Output and submission measures** (SSRN +59.8% per adopter; Organization Science +42%; JPART about ×2.4–2.6 from autumn 2023 to April 2026, my calc 119 vs 45–50 a month) are as large as or larger than STEM benchmarks.
  - A plausible reconciliation (my inference): SSH abstracts lean on discipline-specific vocabulary, which dilutes generic "delve/underscore" markers, while writing-intensive production is highly exposed.
  - Within SSH, empirical and applied subfields and lower-prestige venues adopt more than theory-oriented work (Cao).
- **Best SSH natural experiments with dated interventions:**
  - JPART (cap on 1 Jul 2026; monthly series in the policy PDF's Figure 1);
  - SocArXiv (19 Nov 2025 rules, 27 Nov 2025 moratorium, Mar 2026 AI policy; daily OSF API data);
  - Philosophy & Public Affairs (Aug 2026 ban);
  - the Italian 2023 ChatGPT ban, applied to economics output (Renault).
- **Selection and displacement:** SocArXiv's humanities exclusion shifts volume to KC Works, and caps at single journals shift submissions to uncapped journals. Analyses need system-level denominators (HAL, OpenAlex snapshot).

### Gaps
- No direct measurement of LLM-generated text in **education** research (e.g., ERIC abstracts) was found.
- Law-review evidence is limited to the Conklin & Houston title (findings unverified).
- No systematic humanities-wide prevalence study (history, literature, philosophy) beyond marker-word aggregates was found.
- I did not verify the original Chronicle, Times Higher Education or Inside Higher Ed stories on SSH journal floods in this session. No search of Retraction Watch for SSH paper-mill or AI cases was done.
- The JPART monthly series exists only as a figure; no data table was located.
- The SocArXiv per-author cap remains unverified on the primary site.
