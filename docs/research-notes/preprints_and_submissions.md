# Data sources for counting research papers WRITTEN/SUBMITTED over time (preprint servers, conference submissions, publisher submission statistics)

_Status tags: **[V]** = I verified it myself on 2026-10-15 by querying the endpoint or file (User-Agent "academia-ia-state research", no account, no email). **[P]** = primary document (official page, report or blog), read directly or summarised by the fetch/search tool. **[S]** = secondary (news, aggregator, community dataset). The session's shared WebSearch budget ran out partway through. As a result, publisher coverage beyond RELX/Elsevier and Frontiers is incomplete, and several "why did this series break" questions remain open (see Gaps). Downloaded raw files (arXiv CSV, bioRxiv JSON, medRxiv monthly series, NBER dates, cs-conf-stats JSON, RELX/Frontiers/arXiv annual-report PDFs) are in /tmp/claude-0/-home-user/eefa93ff-68d4-5a29-84a6-8be683e07b57/scratchpad/dl_preprints, /tmp/claude-0/-home-user/eefa93ff-68d4-5a29-84a6-8be683e07b57/scratchpad/dl_confstats and /tmp/claude-0/-home-user/eefa93ff-68d4-5a29-84a6-8be683e07b57/scratchpad/dl_pubs._

## 1. arXiv: what the monthly statistics count, bulk/metadata routes, and policy/moderation breaks

### Takeaway
The official CSV gives the number of new arXiv identifiers issued per month, from 1991-07 to the current month. Because identifiers are issued only when a paper is accepted (announced), this is a count of new papers that passed moderation, not of attempted submissions. It excludes replacements and migrated papers. Each paper counts once however many categories it is cross-listed in. It still includes 156 papers that were later deleted. This is the best long monthly series available. From late 2025 onward, however, a cluster of moderation and policy changes adds structural breaks: CS review/position papers (31 Oct 2025), endorsement (Dec 2025/Jan 2026), an English-version requirement (11 Feb 2026), a one-year ban for unchecked LLM output (May 2026) and per-submitter rate limits (1 Oct 2026). The changes coincide with record volume: 40,363 new papers in September 2026, about double September 2024.

### Cited Findings
**Definition of the official monthly series**
- The stats page says: "This chart displays the number of new submissions received during each month since August 1991 (after 35.2 years)… Total number of submissions as of October 15, 2026 = 3,213,484." It adds: "The total number of submissions excludes 2,431 articles that were migrated to arXiv rather than being submitted directly, and 156 articles that have been deleted. The total number of articles available is 3,215,915." [V] — [arXiv monthly submissions page](https://arxiv.org/stats/monthly_submissions)
- The CSV has the columns `month,submissions,historical_delta` and covers 1991-07 to 2026-10. The current month is partial (2026-10 = 20,611 on Oct 15). The page's chart code plots `data[1]`…`data[length-2]`, so the first month and the current partial month are left off the chart. [V] — [CSV](https://arxiv.org/stats/get_monthly_submissions)
- `historical_delta` is non-zero only from 1991-07 to 2005-09, and it sums to −2,431, which equals the migrated-article count. The `submissions` column sums to 3,213,640, which is the headline total plus the 156 deleted papers. So the `submissions` column already excludes migrated papers and still includes papers deleted later. [V] — [CSV](https://arxiv.org/stats/get_monthly_submissions)
- Each monthly count equals the number of identifiers issued for that YYMM:
  - 2509.26646 exists (v1 timestamp 2025-09-30T17:59:58Z) and 2509.26647 does not. The CSV value for Sept 2025 is 26,646.
  - 2609.40363 exists (2026-09-30T17:59:59Z) and 2609.40364 does not. The CSV value for Sept 2026 is 40,363.
  - [V] — [arXiv API id_list query](https://export.arxiv.org/api/query?id_list=2509.26646,2509.26647,2609.40363,2609.40364)
- Identifier format: "arXiv:YYMM.NNNNN, with 5-digits for the sequence number within the month" (4 digits up to 1412). [P] — [arXiv identifier help](https://info.arxiv.org/help/arxiv_identifier.html)
- arXiv's own published numbers match the CSV exactly: Sept 2016 = 9,869, Sept 2024 = 20,569, Sept 2026 = 40,363. [V]+[P] — [arXiv blog, rate-limit post 2026-10-01](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/); [CSV](https://arxiv.org/stats/get_monthly_submissions)
- Replacements are separate from new submissions. They have their own limit: "a one per week rate limit after version 5". [P] — [arXiv moderation policy](https://info.arxiv.org/help/moderation/index.html)

**Levels and growth (sums of the CSV)** [V] — [CSV](https://arxiv.org/stats/get_monthly_submissions)

| Year | New submissions |
|---|---|
| 2000 | 30,601 |
| 2005 | 46,855 |
| 2010 | 70,131 |
| 2015 | 105,280 |
| 2018 | 140,616 |
| 2019 | 155,866 |
| 2020 | 178,329 |
| 2021 | 181,630 |
| 2022 | 185,692 |
| 2023 | 208,493 |
| 2024 | 244,031 |
| 2025 | 284,486 |
| 2026 (1 Jan–15 Oct) | 291,296 |

- Year-on-year growth: 2021 +1.9%, 2022 +2.2%, 2023 +12.3%, 2024 +17.0%, 2025 +16.6%. Jan–Sep 2026 (270,685) vs Jan–Sep 2025 (208,241) = +30.0%. [V, computed]
- Months around ChatGPT's release:

  | Month | New submissions |
  |---|---|
  | 2022-10 | 17,551 |
  | 2022-11 | 17,271 |
  | 2022-12 | 14,887 |
  | 2023-01 | 13,870 |
  | 2023-05 | 20,092 (first month above 20k) |
  | 2023-10 | 20,710 |

  [V]
- Later months:

  | Month | New submissions |
  |---|---|
  | 2025-09 | 26,646 |
  | 2025-10 | 27,692 (record at the time) |
  | 2026-03 | 30,045 |
  | 2026-05 | 31,604 |
  | 2026-06 | 32,040 |
  | 2026-08 | 31,173 |
  | 2026-09 | 40,363 (record) |

  [V]

**Annual report and moderation-load data**
- 2025 Annual Report, size and staffing [P] — [arXiv 2025 Annual Report PDF](https://info.arxiv.org/about/reports/2025_arXiv_annual_report.pdf):
  - "284,486 submissions in 2025", up from 244,031 (more than +16%), "23,707 submissions per month, on average".
  - "41,000 user support tickets in 2025".
  - 262 moderators, 153 categories, 28 staff.
  - October 2025 (27,692) was the record month: "over 3,000 more than the 2024 record, and over 7,000 more than the 2023 record".
- The same report gives the subject mix for 2025: "in 2025 CS papers comprised 46% (almost half!) of arXiv's submissions. Physics… 30%… math… 15%." [P] — [same report](https://info.arxiv.org/about/reports/2025_arXiv_annual_report.pdf)
- The report names these drivers of moderation load [P] — [same report](https://info.arxiv.org/about/reports/2025_arXiv_annual_report.pdf):
  - "LLM and AI as research topics that also speed up research writing"
  - "Increases in marginal and below the bar AI-generated content"
  - "Increases in high school, undergrad & grad student submissions (pressure to publish)"
  - Overall: "arXiv has seen a surge in lower-quality submissions over the past year".
- Rate-limit post (1 Oct 2026) [P] — [arXiv blog](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/):
  - September 2026 brought "almost 9,000 support tickets for arXiv staff and moderators".
  - Submissions doubled in two years and cs.AI grew "over 6X".
  - Thomas Dietterich is quoted: "a relatively small proportion of authors are submitting a large number of low-quality papers". He also says "AI tools are making it easy for authors to flood arXiv and other repositories with these low-value papers."
- The 2025 annual report blog post is dated 26 Jun 2026. Older reports, budgets and roadmaps are on the reports index. [P] — [blog post](https://blog.arxiv.org/2026/06/26/a-year-in-review-arxivs-2025-annual-report/); [reports index](https://info.arxiv.org/about/reports/index.html)

**Access routes (counts by category, author and date)**
- arXiv API (Atom XML), tested with `search_query=cat:cs.CL AND submittedDate:[202211010000 TO 202211302359]` [V] — [example query](https://export.arxiv.org/api/query?search_query=cat:cs.CL%20AND%20submittedDate:%5B202211010000%20TO%20202211302359%5D&max_results=1):
  - `opensearch:totalResults` = 896.
  - Each entry carries `<published>` (the v1 timestamp) and `<arxiv:primary_category>`.
  - Gotcha: a query encoded with `+` and `max_results=0` returned a spurious `totalResults=1`. Encode spaces as `%20` and use `max_results>=1`.
- OAI-PMH [V]+[P] — [Identify](https://oaipmh.arxiv.org/oai?verb=Identify); [bulk data help](https://info.arxiv.org/help/bulk_data.html):
  - The base URL is now `https://oaipmh.arxiv.org/oai`; the old `export.arxiv.org/oai2` redirects to it.
  - earliestDatestamp is 2005-09-16 and granularity is YYYY-MM-DD.
  - arXiv calls it "the preferred way to bulk-download or keep an up-to-date copy of arXiv metadata", "updated daily".
  - The bulk-data page also lists Kaggle full text, Amazon S3 full text and a KDD-cup dataset.
- Kaggle "arXiv Dataset" (Cornell-University/arxiv): licence "CC0: Public Domain", totalBytes about 5.61 GB, currentVersionNumber 307, lastUpdated 2026-10-10. The subtitle is stale ("1.7M+ papers"). [V] — [Kaggle API metadata](https://www.kaggle.com/api/v1/datasets/view/Cornell-University/arxiv); [dataset page](https://www.kaggle.com/datasets/Cornell-University/arxiv)
- DataCite DOIs (prefix 10.48550) [V] — [DataCite query](https://api.datacite.org/dois?prefix=10.48550&page%5Bsize%5D=1&disable-facets=false):
  - 3,210,897 DOIs in total.
  - Counts by publication year match the CSV: 2021 181,630; 2022 185,691; 2023 208,493; 2024 244,010; 2025 284,486; 2026 288,730 (vs 291,296 in the CSV, a lag of a few days).
  - "Registered" year 2022 = 2,184,325 (the backfile was registered in 2022), so DOI registration dates must not be used as submission dates.
  - Facets are returned only with `disable-facets=false`.

**Policy and moderation timeline (potential structural breaks)**
- Standing rules [P] — [moderation policy](https://info.arxiv.org/help/moderation/index.html); [rate-limit post](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/):
  - Authors must report use of "text-to-text generative AI".
  - AI tools may not be listed as authors.
  - Authors are responsible for "incorrect references".
  - Submitters with previously declined work "should anticipate closer scrutiny".
  - A limit of 3 active submissions per submitter "has applied since 2024".
- 31 Oct 2025, CS category [P] — [arXiv blog p=1740](https://blog.arxiv.org/?p=1740); [S] — [Decrypt](https://decrypt.co/347196/arxiv-blocks-ai-generated-survey-papers-flood-trashy-submissions); [Gigazine](https://gigazine.net/gsc_news/en/20251110-arxiv-update-practice-for-review-articles/):
  - Review articles and position papers must already have been accepted at a peer-reviewed journal or conference, with documentation. Workshop review is "generally considered insufficient". Papers without documentation will likely be rejected.
  - The stated rationale is that generative AI makes non-research papers fast to write.
  - Press reports say arXiv was receiving "hundreds" of such submissions a month.
- English-language rule [P] — [arXiv blog post](https://blog.arxiv.org/2026/01/13/non-english-paper-submission-guidelines/):
  - Announced Nov 2025 and explained in a 13 Jan 2026 post: "The updated policy will go into effect at 2PM ET on Wednesday, February 11, 2026."
  - All new submissions need "a full English-language version, either as the original language or as an included translation". The English translation must come first. Before this, only an English abstract was required.
  - The post was edited on 11 Feb 2026 to confirm the policy was in effect.
- Endorsement [P] — [arXiv endorsement post](https://blog.arxiv.org/2026/01/21/attention-authors-updated-endorsement-policy/); [arXiv blog 2026](https://blog.arxiv.org/2026):
  - From 21 Jan 2026, arXiv "will no longer accept institutional email addresses" as the sole qualifier for endorsing new authors.
  - New submitters to a category now need both an institutional email address and previous authorship on an existing paper in that endorsement domain. Otherwise they must get personal endorsement from an established author.
  - Rationale: a rise in "non-scientific submissions, increasing the rejection rate and requiring excessive moderation and staff effort".
  - The Math section rolled out a similar update in December 2025 (10 Dec 2025 per the blog index).
- May 2026: one-year ban for unchecked LLM output [S] — [The Next Web](https://thenextweb.com/news/arxiv-ai-slop-ban-researchers-preprint); [404 Media](https://www.404media.co/new-arxiv-rules-ai-generated-papers-ban/); [Times Higher Education](https://www.timeshighereducation.com/news/ban-authors-submitting-ai-content-welcome-unenforceable):
  - The trigger is "incontrovertible evidence" that authors did not check LLM output, such as hallucinated references, LLM meta-comments or placeholder text.
  - The penalty is a one-year ban. After it, the author's submissions must first be accepted at a reputable peer-reviewed venue.
  - CS section chair Thomas Dietterich announced it on X. No arXiv blog post on it was found. THE called it "welcome but unenforceable".
- Organisational changes [P] — [arXiv blog 2026](https://blog.arxiv.org/2026/); [page 2](https://blog.arxiv.org/2026/page/2/):
  - arXiv became an independent nonprofit, spun out of Cornell, on 1 Jul 2026 (announced 2 Apr and 30 Jun 2026).
  - First CEO, Penelope Lewis (30 Jul 2026).
  - $17.2M in multiyear philanthropic commitments (23 Sep 2026).
  - Preservation agreements with Portico and TIB (3 Feb 2026).
  - None of these changes submission rules.
- 1 Oct 2026, new rate limits [P] — [arXiv blog](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/); [moderation policy](https://info.arxiv.org/help/moderation/index.html); [S] — [Research Information](https://www.researchinformation.info/news/arxiv-imposes-submission-limits-amid-surge-in-ai-generated-papers/):
  - "up to two submissions per calendar month" per submitter and "three total active submissions", in all categories.
  - Rejected papers count toward the monthly limit, because the limit covers "submissions, not announcements".
  - The limits apply "only to submitters", not co-authors.
  - arXiv describes the policy as a stopgap.

### Inferences
- **Counts are filtered by moderation.** The series equals the number of identifiers issued, and the rate-limit FAQ distinguishes submissions from announcements. Together these imply that the "submissions" column counts announced (accepted) new papers. Submissions rejected or removed before announcement appear to be excluded. So stricter moderation from Oct 2025 onward lowers the measured count relative to papers actually written.
- **Month boundaries follow arXiv's daily cutoff.** The last IDs of September 2025 and September 2026 carry v1 timestamps of 17:59 UTC on the 30th, which is the 14:00 US-Eastern cutoff. Papers submitted after the cutoff on the last weekday of a month get the next month's YYMM.
- **Cross-lists and withdrawals.** Because the count is ID-based, a paper is counted once regardless of cross-lists. A withdrawal is a new version, so withdrawn papers stay counted. Only deletions (156 in 35 years) are removed from the headline total.
- **Counting by category.** API `cat:` queries match the categories assigned to a paper (primary and, probably, cross-lists), so they overstate counts for a single primary category. For primary-category monthly counts, take the first or primary category plus the v1 date from OAI-PMH, Kaggle or full API pages.
- **Field mix as a design lever.** CS is now 46% of submissions and has the confound "AI as a research topic", which the annual report itself names. Physics and math, where arXiv adoption is mature, are natural comparison series for a difference-in-differences design.
- **Seasonality.** Conference deadlines produce peaks in May and Sept/Oct (2023-05, 2023-10, 2025-09/10, 2026-09). Monthly ITS models need seasonal terms or deadline dummies.
- **Rate limit so far.** The 1 Oct 2026 limit has not yet visibly cut volume: 20,611 papers arrived on 1–15 Oct 2026, close to September's daily pace. Caps bind only heavy submitters, but the break should still be modelled.

### Gaps
- arXiv publishes no moderation rejection or on-hold rates that I could find. The 2025 annual report gives support-ticket counts, not rejections.
- I found no official arXiv page for the May 2026 ban; details rest on press coverage of Dietterich's posts. (The English requirement's effective date, 11 Feb 2026, is now confirmed from the primary post.)
- The field list of the Kaggle snapshot and the S3 requester-pays bucket terms were not re-checked this session.
- I did not verify whether arXiv's API `cat:` matching includes cross-lists, or whether the arXiv API Terms of Use (rate-limit etiquette) changed after the July 2026 spin-out.

## 2. bioRxiv and medRxiv: summary and details endpoints, categories, publication linkage, structural breaks

### Takeaway
bioRxiv has a free, keyless monthly summary endpoint from Nov 2013 (new and revised papers). medRxiv has no summary endpoint, but the `details` endpoint returns `count_new_papers` for any date window, so a monthly medRxiv series from June 2019 is easy to build (built and verified here). Both servers have per-category filters and a preprint-to-journal linkage endpoint, `/pubs`. Breaks to model:
- the adoption ramp (2013–2018);
- COVID-19 (2020), with the medRxiv surge and later fall;
- new DOI prefix 10.64898 for all papers posted from 1 Dec 2025, after the move to the openRxiv organisation. This breaks Crossref counts made by prefix.

Growth re-accelerated after 2022: bioRxiv +9.5%, +11.4% and +13.0% in 2023–2025, and medRxiv +4.9%, +16.5% and +16.8%.

### Cited Findings
- `/sum/m` returns JSON under the key "bioRxiv content statistics". Fields: month, new_papers, new_papers_cumulative, revised_papers, revised_papers_cumulative. On 15 Oct 2026 it had 155 rows from 2013-11 to 2026-09 (complete months only). `/sum/y` gives yearly figures. A server segment (`/sum/m/medrxiv`) is silently ignored and still returns bioRxiv figures. [V] — [bioRxiv /sum/m](https://api.biorxiv.org/sum/m)
- bioRxiv new papers per year [V] — [bioRxiv /sum/m](https://api.biorxiv.org/sum/m):

  | Year | New papers |
  |---|---|
  | 2014 | 886 |
  | 2015 | 1,774 |
  | 2016 | 4,718 |
  | 2017 | 11,339 |
  | 2018 | 20,778 |
  | 2019 | 29,179 |
  | 2020 | 38,717 |
  | 2021 | 36,866 |
  | 2022 | 35,750 |
  | 2023 | 39,155 |
  | 2024 | 43,632 |
  | 2025 | 49,318 |
  | 2026 (Jan–Sep) | 40,548 (+11.7% vs Jan–Sep 2025's 36,304) |

  - Revisions: 12,838 in 2022 and 17,893 in 2025.
  - Selected months: 2020-04 3,413; 2022-11 2,993; 2023-11 3,624; 2024-11 3,686; 2025-11 3,884; 2026-03 4,703; 2026-09 5,049 (record).
- `/details/{server}/{start}/{end}/{cursor}` [V] — [bioRxiv Nov 2025](https://api.biorxiv.org/details/biorxiv/2025-11-01/2025-11-30/0); [neuroscience filter](https://api.biorxiv.org/details/biorxiv/2025-11-01/2025-11-30/0?category=neuroscience):
  - Its "messages" block reports `count_new_papers` and `total` (all versions posted in the window).
  - For bioRxiv in Nov 2025: count_new_papers = 3,884 (identical to `/sum/m`) and total = 5,425.
  - Adding `?category=neuroscience` gives 772 new papers.
  - Records carry doi, title, authors, author_corresponding, author_corresponding_institution, date, version, type, license, category, jatsxml, abstract, published and server.
- The API docs describe these endpoints [P] — [bioRxiv API docs](https://api.biorxiv.org/):
  - Interval forms: a date range, the N most recent, or the most recent N days ("Nd").
  - Output as JSON or OAI-PMH XML, with an optional subject-category querystring.
  - `/pubs/[server]/[interval]/[cursor]` (bioRxiv or medRxiv), `/pub/` (bioRxiv only), `/publisher/[DOI prefix]/[interval]` (bioRxiv papers published by a given publisher).
  - `/funder/[server]/[interval]/[ROR]`, with funder metadata only from 2025-04-10.
- medRxiv monthly series, built by me from `/details/medrxiv/…` `count_new_papers`, one call per month [V] — [example](https://api.biorxiv.org/details/medrxiv/2025-11-01/2025-11-30/0):

  | Year | New papers |
  |---|---|
  | 2019 (Jun–Dec; launch month 2019-06 = 32) | 913 |
  | 2020 | 14,070 |
  | 2021 | 12,739 |
  | 2022 | 10,528 |
  | 2023 | 11,049 |
  | 2024 | 12,867 |
  | 2025 | 15,027 |
  | 2026 (Jan–Sep) | 13,173 (+18.6% vs Jan–Sep 2025) |

  - Selected months: 2020-04 1,568; 2020-05 2,082 (COVID peak); 2022-11 871; 2025-11 1,243; 2026-07 1,794.
- `/pubs/biorxiv/2023-01-01/2023-01-31/0` returned total = 1,600 preprint–article pairs. Fields: preprint_doi, preprint_date, preprint_category, preprint_platform, published_doi, published_journal, published_date, and others. [V] — [/pubs example](https://api.biorxiv.org/pubs/biorxiv/2023-01-01/2023-01-31/0)
- Abdill & Blekhman (eLife 2019) [P] — [eLife 8:e45133](https://elifesciences.org/articles/45133):
  - 37,648 preprints posted Nov 2013–Nov 2018; 42.0% published by the end of Nov 2018.
  - In a manual check of 120 "unpublished" preprints, 37.5% had in fact appeared in a journal, so bioRxiv's publication linkage undercounts.
  - Their Rxivist tool provides an API and weekly SQL snapshots on Zenodo.
- openRxiv in Crossref [V] — [Crossref members?query=openRxiv](https://api.crossref.org/members?query=openRxiv); [member works](https://api.crossref.org/members/54368/works?rows=0&facet=published:*):
  - Member 54368, "openRxiv", owns prefix 10.64898.
  - The member holds 445,612 posted-content works, each with `institution` = bioRxiv or medRxiv.
  - By year: 2019 30,088; 2020 52,773; 2021 49,597; 2022 46,237; 2023 50,164; 2024 56,445; 2025 64,303; 2026 56,372 (to 15 Oct).
- New DOI prefix [P] — [openRxiv DOI post, 18 Nov 2025](https://connect.biorxiv.org/news/2025/11/18/preprint_dois); [V] — [bioRxiv details Dec 2025](https://api.biorxiv.org/details/biorxiv/2025-12-01/2025-12-31/0); [Crossref prefix 10.1101](https://api.crossref.org/prefixes/10.1101/works?filter=type:posted-content&rows=0&facet=published:*):
  - The announcement: all new bioRxiv/medRxiv articles use prefix 10.64898 from 1 Dec 2025. Older papers keep 10.1101, with one DOI per article covering all versions.
  - Verified in the API: 10.64898 DOIs appear from December 2025 (e.g., 10.64898/2025.12.10.693562, posted 2025-12-16).
  - In 2026 the API shows a mix, because revisions of older papers keep 10.1101.
  - Crossref `/prefixes/10.1101/works?filter=type:posted-content` now returns only 34 items.
- openRxiv news, 2025–2026 [P] — [connect.biorxiv.org/news](https://connect.biorxiv.org/news/):
  - "q.e.d Science – an AI review tool for authors" (2025-11-04)
  - "Adding funder information to bioRxiv preprints" (2025-09-04)
  - Dryad partnership (2025-09-18)
  - "bioRxiv preprint license update guide" (2026-01-07)
  - "Launching openRxiv Labs" (2026-06-01)
  - "Updating funder information on preprints" (2026-09-03)
  - The news page lists no AI-content screening policy or submission statistics.
- Cross-check against Europe PMC for 2023: bioRxiv 39,130 vs API 39,155, and medRxiv 11,034 vs 11,049. Coverage is near-complete. [V] — [Europe PMC REST](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=SRC:PPR%20AND%20PUBLISHER:%22bioRxiv%22%20AND%20FIRST_PDATE:%5B2023-01-01%20TO%202023-12-31%5D&format=json&pageSize=1&resultType=idlist)

### Inferences
- **Usable pre-period.** bioRxiv's monthly series reaches back to 2013, but 2013–2018 is the adoption ramp: output grew 23x from 2014 to 2018. A "steady-state" pre-period is roughly 2019–2022, and it contains the COVID bump in 2020 and the decline in 2021–22. medRxiv's pre-period is only about 3.4 years and is dominated by COVID.
- **Which counter to use.** For bioRxiv/medRxiv, count with the bioRxiv API or with Crossref member 54368, never with the 10.1101 prefix. Use `count_new_papers` (v1s) rather than `total`, which includes revisions.
- **Linkage outcomes.** `/pubs` supports preprint→journal conversion analyses, but outcomes are right-censored (recent preprints have had less time to be published) and undercounted, per Abdill & Blekhman.
- **What the post-2022 growth could mean.** The re-acceleration in 2023–2025 is consistent with AI-assisted writing. It is also consistent with funder and publisher preprint promotion. These sources cannot separate the two.

### Gaps
- Not verified this session because the search budget was exhausted:
  - the founding or transfer date of openRxiv itself;
  - eLife's 2021 "reviewed preprint" requirement;
  - bioRxiv's direct-transfer programmes (B2J/J2B);
  - any bioRxiv/medRxiv policy on AI-generated or formulaic papers, or published screening and rejection rates.
- The docs extract does not say whether the `/pubs` interval refers to the preprint date or the date a publication was detected.
- I found no bioRxiv/medRxiv statistics on rejected (screened-out) submissions.

## 3. Other preprint servers and cross-server counters (SSRN, Research Square, Preprints.org, ChemRxiv, TechRxiv, OSF family, SciELO, EarthArXiv, Zenodo, NBER/RePEc; Europe PMC; Crossref vs DataCite)

### Takeaway
Most other servers register preprint DOIs with Crossref as type `posted-content`. This makes the Crossref REST API (free, no key) the practical per-server counter: filter by prefix or member, facet by year, or use date filters for months. The raw Crossref counts carry large artefacts, however:
- versioned DOIs (OSF family from 2024–25, Research Square, TechRxiv, Preprints.org);
- adoption and integration shocks, such as SSRN rising 14x from 2020 to 2025 and Preprints.org rising 3.5x in 2023;
- non-preprint posted-content mixed into publisher-level counts (meeting abstracts, news, blogs).

On the DataCite side are arXiv and Zenodo. Zenodo "preprints" jumped 25x in 2025, so they are unusable without filtering. Europe PMC (`SRC:PPR`) is a workable life-science cross-server counter from about 2019, but Research Square dominates it and some items are indexed months late. NBER offers a stable monthly working-paper series back to the 1970s.

### Cited Findings
**Crossref posted-content as a whole** [V] — [Crossref works query](https://api.crossref.org/works?filter=type:posted-content,from-posted-date:2023-01-01,until-posted-date:2023-12-31&rows=0&facet=publisher-name:25)
- Totals by posted-date year: 2010 26,217; 2015 45,111; 2018 107,360; 2020 294,029; 2022 338,817; 2023 720,195; 2024 547,940.
- The 2023 publisher-name facet:

  | Publisher name | 2023 posted-content |
  |---|---|
  | American Association for Cancer Research (AACR) | 265,488 |
  | Elsevier | 153,810 |
  | openRxiv | 50,164 |
  | Research Square Platform LLC | 48,923 |
  | Springer Science and Business Media LLC | 35,497 |
  | Center for Open Science | 31,350 |
  | Copernicus | 23,648 |
  | MDPI | 21,792 |
  | The Conversation Media Group | 18,235 |
  | Wiley | 12,807 |
  | ACS | 7,818 |
  | IEEE | 7,348 |
  | Front Matter | 6,307 |
  | JMIR | 5,564 |
  | Qeios | 1,921 |
  | eLife | 1,640 |
  | California Digital Library | 1,326 |
  | FapUNIFESP (SciELO) | 691 |

**Per-server Crossref counts** (type posted-content, "published" year facet, 2026 to 15 Oct) [V] — [Crossref prefix query pattern, e.g. SSRN](https://api.crossref.org/prefixes/10.2139/works?filter=type:posted-content&rows=0&facet=published:*)
- **SSRN** (10.2139; subtype preprint, group-title "SSRN"): 2012 19,864; 2015 18,753; 2018 12,462; 2019 14,715; 2020 18,388; 2021 33,871; 2022 77,522; 2023 153,810; 2024 210,256; 2025 261,180; 2026 242,395. Total 1,262,105.
- **Research Square** (10.21203; DOIs versioned "…/v1"; sampled 2025 items have group-title "In Review"): 2019 14,025; 2020 68,225; 2021 75,176; 2022 75,680; 2023 82,468; 2024 73,591; 2025 60,377; 2026 77,392.
- **Preprints.org** (MDPI; 10.20944; suffix ".v1"; group-title is the subject area): 2016 943; 2018 5,941; 2019 3,860; 2020 7,012; 2021 7,862; 2022 6,275; 2023 21,790; 2024 28,613; 2025 31,838; 2026 24,424.
- **ChemRxiv** (10.26434): 2017 173; 2018 1,088; 2019 2,873; 2020 4,985; 2021 5,240; 2022 6,029; 2023 7,277; 2024 8,824; 2025 10,085; 2026 10,915.
- **TechRxiv** (IEEE; 10.36227; "/v1" DOIs): 2020 2,105; 2021 3,962; 2022 5,494; 2023 7,342; 2024 4,064; 2025 6,329; 2026 1,520.
- **OSF Preprints** (10.31219): 2017 2,219; 2019 7,652; 2020 14,250; 2021 19,904; 2022 21,846; 2023 20,960; 2024 6,401; 2025 7,340; 2026 1,249. 2025 samples show versioned DOIs (`_v1`, `_v2`, `_v12`) with an `is-version-of` relation.
- **PsyArXiv** (10.31234): 2017 1,295; 2019 3,702; 2020 6,580; 2021 6,987; 2022 6,536; 2023 7,089; 2024 7,497; 2025 14,519; 2026 11,056. Versioned DOIs (e.g., 10.31234/osf.io/6zs2y_v1) appear alongside unversioned ones from Q1 2024 and dominate the 2025 samples.
- **SocArXiv** (10.31235): 2017 1,117; 2019 1,643; 2020 2,302; 2021 2,771; 2022 2,303; 2023 2,398; 2024 2,325; 2025 4,132; 2026 5,164.
- **SciELO Preprints** (10.1590, posted-content only): 2020 509; 2021 512; 2022 616; 2023 691; 2024 780; 2025 966; 2026 1,109.
- **EarthArXiv** (10.31223): 2017 507; 2019 640; 2021 468; 2022 1,015; 2023 913; 2024 864; 2025 1,299; 2026 1,562.
- **Authorea** (Wiley; 10.22541): 2020 11,076; 2021 7,426; 2022 9,345; 2023 12,744; 2024 17,508; 2025 16,229; 2026 6,416.
- **JMIR Preprints** (10.2196, posted-content only): 2017 1,235; 2018 2,599; 2020 5,634; 2022 4,653; 2023 5,564; 2024 5,355; 2025 5,467; 2026 4,190.
- **Qeios** (10.32388): 2022 527; 2023 1,921; 2024 1,840; 2025 1,027; 2026 514.
- **Copernicus/EGU** (10.5194) posted-content (discussion papers, EGUsphere): 2019 7,458; 2020 27,051; 2023 23,648; 2024 12,063; 2025 50,795.
- Sample-DOI checks (versioning, group titles) — [V] — [PsyArXiv sample](https://api.crossref.org/prefixes/10.31234/works?filter=type:posted-content,from-posted-date:2025-06-01&rows=3); [OSF sample](https://api.crossref.org/prefixes/10.31219/works?filter=type:posted-content,from-posted-date:2025-06-01&rows=3)

**DataCite (Zenodo)** [V] — [DataCite preprints](https://api.datacite.org/dois?resource-type-id=preprint&page%5Bsize%5D=1); [Zenodo 2025](https://api.datacite.org/dois?client-id=cern.zenodo&resource-type-id=preprint&query=publicationYear:2025&page%5Bsize%5D=1)
- DOIs with resource-type "preprint": 2,618,954 in total.
- Zenodo (client cern.zenodo) "preprint" DOIs: 702,730 in total. By publication year: 2019 400; 2022 4,743; 2023 5,289; 2025 134,329.

**Europe PMC preprint index (`SRC:PPR`, free REST, no key)** [V] — [Europe PMC REST example](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=SRC:PPR%20AND%20FIRST_PDATE:%5B2023-01-01%20TO%202023-12-31%5D&format=json&pageSize=1&resultType=idlist)
- Counts by FIRST_PDATE year:

  | Year | `SRC:PPR` hits |
  |---|---|
  | 2005 | 0 |
  | 2010 | 0 |
  | 2015 | 3,064 |
  | 2018 | 31,215 |
  | 2019 | 48,759 |
  | 2020 | 128,326 |
  | 2021 | 153,830 |
  | 2022 | 147,774 |
  | 2023 | 176,118 |
  | 2024 | 182,129 |
  | 2025 | 187,033 |
  | 2026 (to mid-Oct) | 175,480 |

- Monthly: 2022-10 12,165; 2022-11 13,167; 2022-12 11,853; 2023-01 13,541.
- 2023 hits by exact PUBLISHER label:

  | PUBLISHER label | 2023 hits |
  |---|---|
  | Research Square | 80,261 |
  | bioRxiv | 39,130 |
  | Preprints.org | 20,291 |
  | medRxiv | 11,034 |
  | Authorea Preprints | 8,294 |
  | PsyArXiv | 7,088 |
  | SSRN | 3,277 |
  | Qeios | 1,270 |
  | arXiv | 1,088 |
  | SciELO Preprints | 658 |
  | "ChemRxiv", "OSF Preprints", "JMIR Preprints", "EarthArXiv", "TechRxiv" | 0 under these exact labels |

- Records carry firstPublicationDate, firstIndexDate, bookOrReportDetails.publisher and versionList.
- Lag example: an Authorea preprint first published 2025-11-30 has firstIndexDate 2026-05-13.
- Europe PMC's "Preprints" information page returned HTTP 403 to automated fetch.

**NBER working papers (free TSV files)** [V] — [NBER metadata directory](https://data.nber.org/nber_paper_chapter_metadata/tsv/); [date.tsv](https://data.nber.org/nber_paper_chapter_metadata/tsv/date.tsv)
- Files: date.tsv (paper, issue_date), abs.tsv, auths.tsv, author_user.tsv, jel.tsv, prog.tsv.
- 35,923 working papers have issue dates. Per year:

  | Year | Working papers |
  |---|---|
  | 2000 | 627 |
  | 2005 | 891 |
  | 2010 | 1,025 |
  | 2015 | 1,020 |
  | 2019 | 1,185 |
  | 2020 | 1,713 |
  | 2021 | 1,311 |
  | 2022 | 1,191 |
  | 2023 | 1,197 |
  | 2024 | 1,308 |
  | 2025 | 1,290 |
  | 2026 (to date) | 1,313 |

**Literature**
- Xie, Shen & Wang (2021): preprints "exponentially increased 63 times in 30 years", yet are still only about 4% of research articles. [P] — [arXiv:2102.09066](https://arxiv.org/abs/2102.09066)

### Inferences
- **Crossref is the best general counter for non-arXiv servers, but only per prefix or member, never publisher-wide.** Aggregate "posted-content" mixes in AACR meeting abstracts, news pieces from The Conversation, Rogue Scholar blog posts via Front Matter, and Copernicus discussion papers. Deduplicate versioned DOIs: strip `_vN` (OSF family), `/vN` (Research Square, TechRxiv) and `.vN` (Preprints.org).
- **Adoption- and integration-confounded series (do not read as paper production):**
  - **SSRN.** The rise from 18k (2020) to 261k (2025) is too large to be organic. Expanded DOI registration or journal-integrated posting at Elsevier are plausible causes, but I could not verify them.
  - **Research Square.** Its "In Review" content is tied to journal submissions.
  - **Preprints.org.** It rose 3.5x in 2023, cause unverified.
  - **OSF Preprints.** Its 2024 fall from about 21k to 6.4k is unexplained.
  - **PsyArXiv and SocArXiv.** Their 2025 doubling coincides with versioned DOIs.
  - **TechRxiv.** It fell to 1,520 in 2026, cause unknown.
  - **Zenodo.** It jumped 25x in 2025.
- **Possible Research Square double-count.** Some 2023 posted-content under "Springer Science and Business Media LLC" (35,497) may be Research Square/In Review DOIs. The prefix total of 82,468 is close to 48,923 + 35,497. This is speculative.
- **Europe PMC fits a life-science pooled index from about 2019.** It needs per-server decomposition, because Research Square makes up about 45% of 2023 hits. Indexing lags mean the last ~6 months are incomplete. It is not a source for arXiv (only about 1k arXiv items a year).
- **NBER.** It is a stable-membership, capacity-limited series and changed little after 2022 (1,191 → 1,197 → 1,308 → 1,290). It is useful as a low-adoption-confound comparison for economics, not as a measure of field-wide output.

### Gaps
- Not tested: ChinaXiv (no count source found), Jxiv (DOIs via the Japan Link Center (JaLC), not Crossref), RePEc (no count endpoint identified), SSRN's native statistics (no public API found), and the native APIs of Research Square, Preprints.org, ChemRxiv and TechRxiv.
- The causes of the SSRN, Preprints.org, OSF, TechRxiv and Zenodo breaks are unverified. Searching for them was not possible after the search budget ran out.
- Europe PMC's official list of indexed servers and their inclusion dates could not be retrieved (HTTP 403).
- The DataCite preprint total (2.62M) is smaller than arXiv's 3.21M DOIs. I did not determine how many arXiv DOIs are typed "Preprint".

## 4. Conference submissions (CS/AI): sources, 2023–2026 numbers, OpenReview access

### Takeaway
The most complete machine-readable source is the community dataset cs-conf-stats (GitHub, `data/conf.json`, 101 venues, updated 8 Oct 2026). It gives main-track submissions and acceptances by year through 2026. Official blogs and press releases confirm the headline 2026 figures for ICLR and CVPR. NeurIPS and ICML 2026 figures are confirmed by institutional relays of the official notifications.

AI and ML submissions exploded after 2022:
- NeurIPS: 10,411 (2022) → 30,709 (2026)
- ICML: 5,630 → 23,918
- ICLR: 3,391 → 19,525
- AAAI: 9,020 → 23,680
- ACL: 3,378 → 12,148

Definitions differ by venue and year, however (valid vs registered, before or after desk rejection and withdrawal). Venues have begun capping submissions per author, which will truncate future counts: CVPR 25 per author; ARR 20, or 5 as first or joint-first author; ICLR 2027 20 per author, plus at most one paper for teams with no eligible reciprocal reviewer. Since late 2025, anonymous OpenReview API access is blocked by a challenge (HTTP 403 `ChallengeRequiredError`).

### Cited Findings
**Community dataset: cs-conf-stats** (main track, submissions/accepted; secondary, curated "from proceedings and the web") [S, V-downloaded] — [cs-conf-stats repo (data/conf.json)](https://github.com/Xovee/cs-conf-stats); [site](https://csconfstats.xoveexu.com/conferences/)

| Venue | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|
| NeurIPS | 6,743/1,428 | 9,467/1,898 | 9,122/2,334 | 10,411/2,672 | 12,343/3,218 | 15,671/4,043 | 21,575/5,290 | 30,709/7,900 |
| ICML | 3,424/774 | 4,990/1,088 | 5,513/1,184 | 5,630/1,235 | 6,538/1,827 | 9,473/2,609 | 12,107/3,260 | 23,918/6,352 |
| ICLR | 1,591/500 | 2,594/687 | 2,997/860 | 3,391/1,095 | 4,938/1,574 | 7,304/2,250 | 11,565/3,710 | 19,525/5,355 |
| AAAI | 7,095/1,150 | 7,737/1,591 | 7,911/1,692 | 9,020/1,349 | 8,777/1,721 | 9,862/2,342 | 12,957/3,032 | 23,680/4,167 |
| IJCAI | 4,752/850 | 4,717/592 | 4,204/587 | 4,537/679 | 4,566/643 | 5,651/791 | 5,348/1,015 | 5,233/713 |
| CVPR | 5,165/1,300 | 6,656/1,470 | 7,015/1,663 | 8,161/2,064 | 9,155/2,359 | 11,532/2,719 | 13,008/2,878 | 16,092/4,071 |
| ICCV (odd yrs) | 4,303/1,075 | – | 6,236/1,617 | – | 8,088/2,160 | – | 11,239/2,698 | – |
| ECCV (even yrs) | – | 5,150/1,360 | – | 5,804/1,645 | – | 8,585/2,387 | – | 10,473/2,883 |
| ACL | 1,740/447 | 2,248/571 | 3,350/710 | 3,378/701 | 4,864/1,074 | 4,407/943 | 8,360/1,699 | 12,148/2,296 |
| EMNLP | 2,876/683 | 3,359/752 | 3,600/840 | 4,190/829 | 4,909/1,047 | 6,105/1,271 | 8,174/1,811 | n/a /2,710 |
| NAACL | 1,733/423 | – | 1,797/477 | 2,103/442 | – | 2,434/565 | 3,099/719 | – |
| KDD | 1,179/174 | 1,279/217 | 1,541/239 | 1,659/254 | 1,416/313 | 2,046/411 | 2,955/552 | 3,252/602 |
| WWW | 1,247/225 | 1,129/219 | 1,736/355 | 1,822/323 | 1,783/365 | 2,008/405 | 2,062/409 | 3,370/678 |
| SIGIR | 426/84 | 555/147 | 720/151 | 793/161 | 822/165 | 791/160 | 1,071/239 | 1,271/233 |
| CHI | 2,958/703 | 3,126/760 | 2,845/747 | 2,579/637 | 3,180/879 | 4,028/1,058 | 4,668/1,249 | 6,725/1,702 |
| AISTATS | 1,111/360 | n/a /423 | 1,527/455 | 1,685/492 | 1,689/496 | 1,980/547 | 1,861/583 | 2,102/590 |
| UAI | 450/118 | 515/142 | 694/205 | 712/230 | 778/243 | 715/200 | 750/230 | 1,087/332 |
| ICRA | 2,916/1,317 | 2,902/1,277 | 3,877/1,690 | 3,263/1,428 | 3,125/1,345 | 3,937/1,760 | 4,153/1,606 | 4,947/1,882 |
| IROS | 2,494/1,108 | 2,996/1,420 | 2,786/1,301 | 3,579/1,716 | 2,760/1,196 | 3,400/1,600 | 4,306/1,991 | 4,348/1,585 |

**Primary and official confirmations, and definitional detail**
- ICLR 2026 (official retrospective, 31 Mar 2026) [P] — [ICLR blog retrospective](https://blog.iclr.cc/2026/03/31/a-retrospective-on-the):
  - 19,525 "valid, format-compliant submissions", excluding abstract registrations.
  - 779 desk-rejected, 5,042 withdrawn, 13,763 decided.
  - 5,355 accepted (27.4%).
  - 18,054 reviewers wrote 76,139 reviews.
  - Papers with confirmed hallucinated references were desk-rejected (no count given).
  - Reviews were run through two LLM detectors.
- NeurIPS [S] — [RIKEN AIP](https://aip.riken.jp/news/neurips2026/); [csconfstats NeurIPS 2026](https://csconfstats.xoveexu.com/conferences/neurips/2026/); [lixin4ever README](https://github.com/lixin4ever/Conference-Acceptance-Rate); [NeurIPS PC reflections 2025](https://blog.neurips.cc/2025/09/30/reflections-on-the-2025-review-process-from-the-program-committee-chairs/):
  - 2026: "30,709 valid paper submissions with a PDF to the NeurIPS Main Track", of which 7,900 were accepted (25.7%), as relayed by RIKEN AIP.
  - 2025: 21,575 submissions, 5,290 accepted (24.5%).
- NeurIPS 2026 workshops: 477 proposals submitted (454 valid), 102 accepted, hosted in Sydney, Paris and Atlanta. [P] — [NeurIPS blog](https://blog.neurips.cc/2026/08/10/announcing-the-neurips-2026-workshops/)
- ICML 2026 [S] — [UCL](https://www.ucl.ac.uk/engineering/news/papers-accepted-icml-2026); [WASP](https://wasp-sweden.org/strong-wasp-presence-at-icml-2026/); [RIKEN AIP](https://aip.riken.jp/news/icml2026/); [Wikipedia ICML](https://en.wikipedia.org/wiki/International_Conference_on_Machine_Learning):
  - 23,918 submissions "that entered reviewing after initial desk rejections and withdrawals"; 6,352 accepted (26.6%); 536 spotlights; 168 orals.
  - Conflicting figures: Wikipedia lists 24,371 submissions, and a community summary gives 24,661.
- CVPR 2026: "a record number of paper submissions—16,092", up 24% on 2025, with 4,089 papers presented (about a quarter). The figures come from a CVPR / IEEE Computer Society / CVF announcement of 26 May 2026. cs-conf-stats gives 4,071 accepted. [P via press release] — [Newswise release](https://www.newswise.com/articles/cvpr-2026-fields-16-000-paper-submissions-on-technical-advances-in-ai)
- AAAI-26: 23,680 submissions, 4,167 accepted (17.6%). 36Kr reports the same figures from acceptance emails. [S] — [cs-conf-stats](https://github.com/Xovee/cs-conf-stats); [36Kr](https://eu.36kr.com/en/p/3442011275122308); [36Kr (alt)](https://eu.36kr.com/de/p/3546803868545153)
- The older community README uses different denominators [S] — [Conference-Acceptance-Rate](https://github.com/lixin4ever/Conference-Acceptance-Rate):
  - ACL'23 910/3,872 and EMNLP'23 901/3,868 (vs 4,864 and 4,909 in cs-conf-stats).
  - ICLR'25 3,706/11,672 (vs 3,710/11,565).
  - The README stops at NeurIPS'25, ICLR'25, CVPR'25, AAAI'25, ICML'24, IJCAI'23 and KDD'23.
- Paper Copilot's statistics pages cover ICLR, ICML, CVPR, AAAI and ECCV to 2026, NeurIPS to 2025, and ACL, EMNLP, NAACL and KDD to 2025. Per-year values load by JavaScript; the GitHub organisation is papercopilot. [S] — [papercopilot statistics](https://papercopilot.com/statistics/)

**Per-author caps and other submission-policy breaks**
- CVPR 2026: "Each author is limited to a maximum of 25 paper submissions. If an author registers more than 25 papers, the Program Chairs (PCs) will desk-reject any submissions exceeding this limit." [V]+[P] — [CVPR 2026 Author Guidelines](https://cvpr.thecvf.com/Conferences/2026/AuthorGuidelines)
- ICLR 2027 quotas [V]+[P] — [ICLR 2027 Author Guidelines](https://iclr.cc/Conferences/2027/AuthorGuidelines):
  - "No author may appear as a co-author on more than 20 papers."
  - "Each author may appear as a co-author on at most one paper in which no author is an eligible reciprocal reviewer." In plain language: if no author on the team has ever had a paper accepted at a major ML venue, they "may submit at most one paper".
  - Excess submissions are randomly desk-rejected.
  - Rationale: "The rapid rate of growth in submissions… has begun to strain the review system."
- Reciprocal reviewing (ICLR 2026 and 2027): "All authors who are on 3 or more papers must serve as a reviewer for at least 6 papers." [P] — [ICLR 2026 Author Guide](https://iclr.cc/Conferences/2026/AuthorGuide); [ICLR 2027 Author Guidelines](https://iclr.cc/Conferences/2027/AuthorGuidelines)
- ICLR 2027 call for papers, "Note for first-time submitters" [P] — [ICLR 2027 CFP](https://iclr.cc/Conferences/2027/CallForPapers):
  - "improved AI tools are expanding the community of researchers".
  - "A typical ICLR paper involves significantly more work than… can be produced autonomously by any current AI agent".
  - "all submissions (even rejected and withdrawn submissions) will remain public with authors' names attached".
- ACL Rolling Review: "There are now caps on maximum submissions by a single author (20) and first or joint-first authors (5), and penalties for system abuse including systematic spamming and account manipulation." The start date is not stated in the extract. [V]+[P] — [ARR CFP](https://aclrollingreview.org/cfp)
- AAAI-26 two-phase review [P] — [AAAI-26 review process](https://aaai.org/conference/aaai/aaai-26/review-process/):
  - Abstract deadline 25 Jul 2025; full papers due 4 Aug 2025.
  - In Phase 1, every paper gets three reviewers; papers with "sufficiently negative reviews" are rejected without author feedback.
  - The remaining papers go to Phase 2, with an author-feedback window of 7–13 Oct 2025.
  - The figure of submissions entering full review is therefore smaller than the number submitted.

**OpenReview access**
- Anonymous requests to both API hosts return HTTP 403. Example: `api2.openreview.net/notes?invitation=ICLR.cc/2026/Conference/-/Submission` and `api.openreview.net/notes?…` return `{"name":"ChallengeRequiredError","message":"Challenge verification required", "details":{"challengeUrl":"https://openreview.net/challenge?redirect=…"}}`. The HTML venue page `openreview.net/group?id=ICLR.cc/2026/Conference` returns 200. [V] — [api2 test URL](https://api2.openreview.net/notes?invitation=ICLR.cc/2026/Conference/-/Submission&limit=1)
- openreview-py offers an API v1 client (`openreview.Client`) and an API v2 client (`openreview.api.OpenReviewClient`). Both take a username/password or a token. The library source defines an error for accounts that require multi-factor verification, which needs an interactive login. [P] — [openreview-py source docs](https://openreview-py.readthedocs.io/en/stable/_modules/openreview/openreview.html); [OpenReview docs](https://docs.openreview.net/)
- Security incident (late Nov 2025) [P] — [OpenReview statement](https://openreview.net/forum/user%7Cstatement_regarding_api_security_incident); [OpenReview initial analysis](https://openreview.net/forum/user%7Cinitial_analysis_of_openreview_api_security_incident); [ICLR incident response](https://blog.iclr.cc/iclr-2026-response-to-security-incident/); [ARR/EACL statement](https://aclrollingreview.org/statement-openreview-data-leakage):
  - A vulnerability in a profile-search API endpoint exposed the identities of anonymous reviewers, authors and area chairs. A patch was deployed within one hour of the report.
  - OpenReview says about 97% of its 3,203 venues were unaffected.
  - ICLR says over ten thousand ICLR 2026 papers (about 45%) were exposed. It reverted scores and reassigned area chairs.
  - ARR/EACL 2026 found 9 papers where an area chair's or senior area chair's identity was compromised.

### Inferences
- **Growth 2022→2026, by venue:**

  | Venue | Growth 2022→2026 |
  |---|---|
  | ICLR | ×5.8 |
  | ICML | ×4.2 |
  | ACL | ×3.6 |
  | NeurIPS | ×2.9 |
  | AAAI | ×2.6 |
  | CHI | ×2.6 |
  | CVPR | ×2.0 |
  | KDD | ×2.0 |
  | WWW | ×1.8 |
  | SIGIR | ×1.6 |
  | ICRA | ×1.5 |
  | UAI | ×1.5 |
  | AISTATS | ×1.25 |
  | IJCAI | ×1.15 |

  Flagship ML/NLP venues accelerate most. The 2022→2023 step is modest; 2024–2026 is steep.
- **Aggregate venue counts overstate unique papers.** Rejected papers cascade through the cycle (NeurIPS → ICLR → ICML → …).
- **Counting stages differ.** ICLR counts valid submissions before withdrawals. ICML 2026 counts after desk rejections and withdrawals. AAAI-26 apparently counts after compliance filtering. NeurIPS counts "valid with PDF". Compare within a venue only, and keep each venue's own definition fixed.
- **Annual granularity.** With one deadline a year there are about 10–15 annual points per venue: enough for descriptive breaks, weak for formal ITS.
- **Programmatic OpenReview harvesting.** It probably now needs an authenticated, challenge-cleared client (unverified). Practical alternatives are cs-conf-stats JSON, Paper Copilot, and the official blogs and press releases.

### Gaps
- A search summary attributed to AAAI's official AAAI-26 page the figures "nearly 29,000" Main Technical Track submissions and "roughly 23,000 remaining under review after policy compliance filtering". I could not capture or fetch that URL, so the definitional gap between 29k and 23.7k is unverified.
- I did not test whether a logged-in openreview-py session bypasses the challenge (no account, by constraint). I found no OpenReview announcement explaining the challenge.
- 2026 numbers for IJCAI, ECCV, ACL, KDD, WWW, SIGIR and CHI come only from cs-conf-stats. Official sources were not fetched, and the dataset's licence was not determined.
- Per-cycle ARR (ACL Rolling Review) statistics were not retrieved.
- Per-author caps were verified only for CVPR 2026, ICLR 2027 and ARR. A coordinator relay of another researcher's findings adds three items I could not confirm on the pages I fetched:
  - the CVPR cap began in 2025 (the CVPR 2025 page failed through the proxy);
  - AISTATS 2027 caps authors at 12 (not found on its CFP or home page);
  - AAAI-26 sent 22,977 papers to full review (not found on the AAAI-26 main, call or review-process pages).
- Submission fees and multi-site formats were not checked.

## 5. Journal and publisher submission statistics; AI or paper-mill surges; desk-rejection data

### Takeaway
Among publishers, I verified a usable submission time series only for Elsevier (RELX annual reports): about 2.5m submissions (2021), almost 2.7m (2022), almost 3m (2023), more than 3.5m (2024) and more than 4.2m (2025). Growth therefore accelerated from about +8% a year to about +20% a year after 2022, while published output rose more slowly (600k → 795k). RELX attributes the growth to "pay-to-publish" open access, not to AI. Frontiers publishes acceptance and rejection shares and desk-rejection counts: 65,544 desk rejections in 2024 and 58% rejected in 2025, with more than half of rejections made by its research-integrity team before peer review. Other publishers could not be verified in this session.

### Cited Findings
- RELX/Elsevier annual reports [P] — [RELX AR 2021](https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2021-annual-report.pdf); [2022](https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2022-annual-report.pdf); [2023](https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2023-annual-report.pdf); [2024](https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2024-annual-report.pdf); [2025](https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2025-annual-report.pdf):
  - **2021:** "Article submission volumes were 2.5m in 2021, in line with the elevated levels of 2020"; over 600,000 articles published.
  - **2022:** "almost 2.7m article submissions, publishing over 600,000 new research articles".
  - **2023:** "almost 3m article submissions, publishing over 630,000 new research articles", and "Article submissions returned to strong growth, with pay-to-publish open access articles continuing to grow particularly strongly".
  - **2024:** "more than 3.5m article submissions", reviewed with "36,000 editors and 1.7 million expert reviewers", with "over 720,000 articles" published; "article submissions growing very strongly across the portfolio, particularly in pay-to-publish".
  - **2025:** "more than 4.2m article submissions", reviewed with "over 37,000 editors and over 1.9m expert reviewers", with "over 795,000 articles" published; "article submissions growing very strongly across the portfolio".
  - The 2019 and 2020 reports were not at the same URL pattern (HTTP 404).
- Frontiers 2024 annual report [P] — [Frontiers annual report 2024](https://www.frontiersin.org/documents/frontiers-annual-report-2024.pdf):
  - On average "only 43% of articles are accepted… 57% of articles are rejected".
  - Of rejections, 55% were by editorial boards and "45% of all rejections were carried out by our research integrity team".
  - "65,544 articles desk-rejected in 2024".
  - Rejection rates "can reach up to 75%" in some fields.
- Frontiers 2025 annual report [P] — [Frontiers annual report 2025](https://www.frontiersin.org/documents/annual-report-2025.pdf):
  - "of the manuscripts submitted in 2025, a total of 42% were accepted… while 58% were rejected. In 2025 more than half of those rejections were carried out by our research integrity team before the manuscript reached the peer review stage".
  - Its AI system (AIRA) "performs a total of 44 quality checks on each submitted manuscript".
  - An auditing division set up in 2022 targets "organized fraud networks and paper mills".
- Moderation and desk-rejection signals outside journals:
  - ICLR 2026: 779 desk rejections (4.0% of 19,525 valid submissions) and 5,042 withdrawals (25.8%). [P] — [ICLR retrospective](https://blog.iclr.cc/2026/03/31/a-retrospective-on-the)
  - arXiv: about 41,000 support tickets in 2025 and almost 9,000 in September 2026 alone. [P] — [arXiv 2025 AR](https://info.arxiv.org/about/reports/2025_arXiv_annual_report.pdf); [rate-limit post](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/)

### Inferences
- **Elsevier growth.** Implied annual growth is about +8% (2022), +11% (2023), +17% (2024) and +20% (2025), from rounded "almost" and "more than" figures. The ratio of published articles to submissions fell from about 22% (2022) to about 19% (2025). That pattern fits submissions growing faster than accepted output, through more low-quality, mass-produced or fraudulent submissions or through cascading resubmissions. RELX does not define "submission": it is unclear whether transfers between Elsevier journals or resubmissions count. Treat the series as a publisher-portfolio count with open-access-expansion confounding.
- **Frontiers.** Integrity screening takes a growing share of rejections (45% in 2024, more than 50% in 2025). Journal "submissions" increasingly include material that integrity screening filters out, so submissions ≠ papers written by researchers in good faith.

### Gaps
- **Not verified (search budget exhausted):** Springer Nature (annual report or progress report), Wiley (10-K "submissions growth"), Taylor & Francis/Informa, MDPI, PLOS, IOP Publishing, eLife, Royal Society, BMJ, IEEE and ACS. Wiley's investor-relations page and MDPI's annual-reports page returned HTTP 403 to scripted requests. My guessed Springer Nature investor-relations URLs returned 404.
- **Reported 2023–2026 surges** attributed to generative AI or paper mills were not verified this session. Examples include formulaic papers built on public datasets, AI-written letters to editors, and journal-specific pauses.
- **No cross-publisher, journal-level submission dataset** (e.g., from manuscript systems) was found to be public.
- **JPART lead (unverified).** A coordinator relay of another researcher's findings reports that the *Journal of Public Administration Research and Theory* caps authors at 3 submissions per year from 1 Jul 2026, after monthly submissions rose from about 45–50 to 119. The OUP instructions page returned HTTP 403 to my fetch, so I could not verify this. If confirmed, it is a journal-level example of AI-era submission inflation followed by a per-author cap.

## 6. Which sources suit an interrupted time series around Nov 2022, and which are adoption-confounded

### Takeaway
Only arXiv combines a long pre-period (monthly since 1991, 274 pre-period months from 2000) with a mature adoption base in several fields. bioRxiv (monthly since 2013) and NBER (monthly-level dates for decades) are secondary options. Conferences and Elsevier are annual only. medRxiv, SSRN, Research Square, Preprints.org, the OSF family, TechRxiv, Zenodo, Europe PMC and aggregate Crossref posted-content are dominated by adoption, integration or versioning shocks.

All preprint series count moderated or accepted postings, not papers written. arXiv's 2025–2026 policy changes contaminate the latest post-period. The cleanest test window for arXiv is roughly Jan 2000 to Oct 2025, with seasonal and COVID controls and physics/math as comparison series.

### Cited Findings
**Coverage and granularity** [V] — [arXiv CSV](https://arxiv.org/stats/get_monthly_submissions); [bioRxiv /sum/m](https://api.biorxiv.org/sum/m); [medRxiv details](https://api.biorxiv.org/details/medrxiv/2019-06-01/2019-06-30/0); [Europe PMC REST](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=SRC:PPR%20AND%20FIRST_PDATE:%5B2019-01-01%20TO%202019-12-31%5D&format=json&pageSize=1&resultType=idlist); [NBER date.tsv](https://data.nber.org/nber_paper_chapter_metadata/tsv/date.tsv)
- arXiv: monthly from 1991-08.
- bioRxiv: monthly from 2013-11.
- medRxiv: monthly from 2019-06.
- Europe PMC preprints: substantive from about 2018–2019 (3,064 in 2015; 31,215 in 2018).
- NBER: issue dates for 35,923 papers.

**Growth before and after 2022**

| Source | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 YTD (Jan–Sep) |
|---|---|---|---|---|---|---|
| arXiv [V] | +1.9% | +2.2% | +12.3% | +17.0% | +16.6% | +30.0% |
| bioRxiv [V] | −4.8% | −3.0% | +9.5% | +11.4% | +13.0% | +11.7% |
| medRxiv [V] | −9.5% | −17.4% | +4.9% | +16.5% | +16.8% | +18.6% |
| Europe PMC preprints [V] | – | −3.9% | +19.2% | +3.4% | +2.7% | – |
| Elsevier submissions [P] | – | ≈+8% | ≈+11% | ≈+17% | ≈+20% | – |
| NBER working papers [V] | – | 1,191 | 1,197 | 1,308 | 1,290 | – |

Sources for the table: arXiv, bioRxiv, medRxiv, Europe PMC and NBER from the endpoints above (computed); Elsevier from the [RELX AR 2025](https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2025-annual-report.pdf) and earlier reports. The NBER row shows counts, not growth rates.

**Structural breaks to encode** (sources in sections 1–4) [P] — [arXiv blog p=1740](https://blog.arxiv.org/?p=1740); [arXiv blog 2026](https://blog.arxiv.org/2026/); [rate-limit post](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/); [openRxiv DOI post](https://connect.biorxiv.org/news/2025/11/18/preprint_dois)
- arXiv: CS review/position-paper rule (31 Oct 2025); endorsement (10 Dec 2025 for math, 21 Jan 2026 for all); English-version requirement (11 Feb 2026); one-year LLM-slop ban (May 2026, press-reported); rate limits (1 Oct 2026).
- Conference per-author caps: CVPR 25 (2026 guidelines); ARR 20, or 5 as first or joint-first author; ICLR 2027 20, plus a one-paper limit for teams with no eligible reciprocal reviewer; AAAI-26 two-phase review with Phase 1 rejections. [P] — [CVPR 2026](https://cvpr.thecvf.com/Conferences/2026/AuthorGuidelines); [ARR CFP](https://aclrollingreview.org/cfp); [ICLR 2027](https://iclr.cc/Conferences/2027/AuthorGuidelines); [AAAI-26](https://aaai.org/conference/aaai/aaai-26/review-process/)
- bioRxiv/medRxiv: DOI prefix 10.64898 from 1 Dec 2025.
- OSF family: DOI versioning from 2024–25 (observed in Crossref).
- COVID: 2020–21 (medRxiv 2020 = 14,070, from 913 in Jun–Dec 2019).

**Arguments about mechanism**
- arXiv's own annual report lists both "LLM and AI as research topics" and "marginal and below the bar AI-generated content" as drivers. [P] — [arXiv 2025 AR](https://info.arxiv.org/about/reports/2025_arXiv_annual_report.pdf)

### Inferences
- **Recommended primary series for the AI-impact study:**
  1. arXiv monthly new submissions, split by primary archive. Compare cs and stat.ML (treated) with physics, math and astro-ph (comparison). Use v1 dates from OAI-PMH or Kaggle; per-category API counts are a quick check.
  2. bioRxiv monthly `new_papers`, split by category through `details?category=`.
  3. Conference submission counts as annual corroboration for AI/ML.
  4. Elsevier annual submissions as a journal-side corroboration.
- **Adoption-confounded (growth ≠ more papers written):**
  - medRxiv (launch plus COVID);
  - SSRN Crossref series (×14 in 2020–2025);
  - Research Square (journal-integrated "In Review");
  - Preprints.org (2023 ×3.5);
  - OSF family (versioning, 2024 drop);
  - TechRxiv (2026 drop);
  - Zenodo (2025 ×25);
  - Europe PMC pooled index (server additions, Research Square share, indexing lag);
  - aggregate Crossref posted-content (non-preprint content).
  - arXiv CS is partly adoption-confounded too: the CS share rose to 46% of arXiv in 2025.
- **Confounders to model:**
  - AI as a research topic, which raises CS output regardless of writing tools;
  - conference-deadline seasonality;
  - COVID shock and rebound (2020–2022);
  - moderation and policy changes that filter what is counted (2025–2026);
  - resubmission cascades (conferences) and integrity-screening volumes (journals).
- **Measurement caveat.** None of these series directly measures papers written. The closest are total submissions including rejections, which almost no preprint server publishes (arXiv counts only announced papers). Conference "valid submissions" with desk-rejection and withdrawal counts (ICLR) and publisher totals (Elsevier) come nearest.

### Gaps
- I did not obtain per-category monthly arXiv series in this session; only the route was verified. I did not run any formal ITS or placebo test.
- Some breaks remain unexplained or undated, chiefly the SSRN, Preprints.org, OSF, TechRxiv and Zenodo shifts and the exact effective date of arXiv's English requirement. The literature on LLM effects on preprint productivity (e.g., studies using arXiv, bioRxiv and SSRN) was not re-verified here because the search budget was exhausted.
