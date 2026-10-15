# Indexed publication counts, researcher denominators and long-run growth baselines (source catalog, state as of 2026-10-15)

Conventions used in these notes:
- **[VERIFIED-QUERY]** = number obtained by me by querying the live endpoint on 2026-10-15 (User-Agent "academia-ia-state research", no key, no email). The link points to the endpoint/query used. Live counts drift daily.
- **[PRIMARY-DOC]** = read directly from the official documentation / original paper.
- **[SECONDARY]** = taken from a search-result summary or a third party; not independently verified.
- Growth rates marked "(my calc)" are computed by me from the cited numbers.
- Note for the report writer: this session's WebSearch quota ran out midway, so several items (STM Report, SCImago, OECD bibliometrics, WoS delisting counts, COKI) remain gaps rather than verified facts.

## 1. PubMed/MEDLINE: reliable annual counts (E-utilities, baseline XML, NLM tables), date fields, record subsets, lags and structural breaks

### Takeaway
PubMed can be counted reliably and for free via E-utilities, but **which date field and which status subset you count changes the level by 10-40% and changes the trend**. `[dp]`/`[pdat]` double-counts items whose e-pub and print dates fall in different years (2024: 1,739,997 by [dp] vs 1,546,982 by entry date [edat]). PubMed's composition has shifted from 91% MEDLINE (2000) to 64% (2024) as PMC-only/non-MEDLINE records grew. MEDLINE indexing went from mostly human to almost fully automated in 2020-2022, a major break for MeSH-based field breakdowns. The most recent 3-9 months are incomplete in status (publisher/in-process). NLM's official "MEDLINE citation counts by year" table was last produced from the January 2023 baseline, and several NLM statistics pages have been retired since 2024.

### Cited Findings

#### Record card: PubMed via NCBI E-utilities (esearch)
- **What is counted:** PubMed bibliographic records (MEDLINE + in-process + publisher-supplied + PubMed-not-MEDLINE, including PMC-only records, books and NIH-pilot preprints). Total on 2026-10-15: `all[sb]` = 41,288,321; database build "Build-2026.10.15.08.07" [VERIFIED-QUERY] — [esearch all[sb]](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=all%5Bsb%5D); [einfo](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi?db=pubmed&retmode=json)
- **Access:** `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&retmode=json&term=...`. Free; no key needed (I used about 0.45 s between calls; NCBI allows ~3 requests/s without a key). The caller's check reproduces: `2024[pdat]` = 1,739,997 [VERIFIED-QUERY] — [esearch 2024[pdat]](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=2024%5Bpdat%5D)
- **Start year / granularity:** Records go back to pre-1947 (OLDMEDLINE). Date fields support year, month (`2025/07[edat]`) and day ranges [VERIFIED-QUERY, monthly queries worked].
- **Licence:** Free. The baseline README asks users to acknowledge NLM and not imply endorsement. Redistributors must keep data current or say it is not current — [PubMed baseline README](https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/README.txt)

#### Date fields: definitions [PRIMARY-DOC] and measured differences [VERIFIED-QUERY]
- `[dp]` Publication Date "includes both print and electronic dates of publication". When e-pub and print dates differ, "both dates are searchable", except that an electronic date later than the print date is not included. `[epdat]`/`[ppdat]` search electronic-only and print-only dates. `[crdt]` can be more comprehensive than `[dp]` for checking new citations — [PubMed User Guide](https://pubmed.ncbi.nlm.nih.gov/help/)
- `[edat]` Entry Date is the "date used for PubMed processing, such as 'Most Recent' sort order". `[crdt]` is "the date the PubMed record was first created". `[mhda]` is "the date the citation was indexed with MeSH terms" — [PubMed User Guide](https://pubmed.ncbi.nlm.nih.gov/help/)
- `[pdat]` returned exactly the same counts as `[dp]` for every year tested (1950-2026) [VERIFIED-QUERY] — [esearch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=2024%5Bdp%5D)
- NLM itself warns that items published electronically and in print with two different publication dates "will be counted once in a 2013 [dp] search and again in a 2014 [dp] search". It also warns that live searches return more than its baseline-derived table — [NLM MEDLINE Citation Counts by Year of Publication](https://www.nlm.nih.gov/bsd/medline_cit_counts_yr_pub.html)
- Counts by date field [VERIFIED-QUERY, 2026-10-15] ([esearch endpoint](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=2024%5Bedat%5D)):

| Year | [dp] = [pdat] | [edat] | [crdt] | [mhda] |
|---|---|---|---|---|
| 1950 | 85,773 | 85,782 | 81,618 | 82,595 |
| 1970 | 219,425 | 219,452 | 216,811 | 212,498 |
| 1990 | 410,999 | 411,057 | 403,019 | 388,413 |
| 2000 | 532,636 | 499,203 | 492,088 | 446,780 |
| 2010 | 942,372 | 839,733 | 1,057,960 | 805,873 |
| 2015 | 1,258,185 | 1,091,650 | 1,105,026 | 1,033,853 |
| 2016 | 1,285,555 | 1,136,715 | 1,153,998 | 1,131,767 |
| 2017 | 1,304,375 | 1,135,714 | 1,194,233 | 1,126,630 |
| 2018 | 1,351,720 | 1,180,955 | 1,271,722 | 1,196,451 |
| 2019 | 1,418,988 | 1,243,065 | 1,264,225 | 1,298,647 |
| 2020 | 1,641,225 | 1,443,692 | 1,459,118 | 1,371,056 |
| 2021 | 1,787,564 | 1,542,806 | 1,558,212 | 1,915,591 |
| 2022 | 1,783,568 | 1,540,382 | 1,589,384 | 1,758,615 |
| 2023 | 1,697,549 | 1,499,881 | 1,551,377 | 1,507,589 |
| 2024 | 1,739,997 | 1,546,982 | 1,562,040 | 1,572,796 |
| 2025 | 1,882,044 | 1,700,143 | 1,710,483 | 1,688,898 |
| 2026 (to 15 Oct) | 1,541,148 | 1,382,492 | 1,391,907 | 1,537,363 |

- In 2024, print-date-only `[ppdat]` = 905,688 and electronic-date-only `[epdat]` = 1,344,285 [VERIFIED-QUERY] — [esearch 2024[epdat]](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=2024%5Bepdat%5D)

#### Status subsets: definitions [PRIMARY-DOC] and series [VERIFIED-QUERY]
- Subset definitions from the PubMed User Guide ([PubMed User Guide](https://pubmed.ncbi.nlm.nih.gov/help/)):
  - `publisher[sb]`: "citations recently added to PubMed via electronic submission from a publisher".
  - `inprocess[sb]`: records where "MeSH terms will be assigned if the subject of the article is within the scope of MEDLINE".
  - `medline[sb]`: records "indexed with MeSH terms, Publication Types, Substance Names, etc."
  - `pubmednotmedline[sb]`: records that "will not receive MEDLINE indexing because they are for articles in non-MEDLINE journals". This also covers out-of-scope articles from MEDLINE journals.
  - PMC holds "individual articles and preprints collected for archiving in compliance with funder policies". Selective-deposit records come from non-MEDLINE journals.
- **Syntax trap [VERIFIED-QUERY]:** `2024[dp] AND pubmednotmedline[sb]` = 570,203. The unquoted multi-word form `pubmed not medline[sb]` silently returns 12,217, and the quoted `"pubmed not medline"[sb]` returns 0. Likewise `pmc[sb]` = 0, while `"pubmed pmc"[sb]` = 915,169 for 2024. In 2024, `medline` 1,112,094 + `pubmednotmedline` 570,203 + `inprocess` 43,222 + `publisher` 14,457 + `indatareview` 21 = 1,739,997, which is exactly the 2024[dp] total — [esearch pubmednotmedline](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=2024%5Bdp%5D+AND+pubmednotmedline%5Bsb%5D)
- Annual series by citation status [VERIFIED-QUERY, 2026-10-15] ([esearch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=2024%5Bdp%5D+AND+medline%5Bsb%5D)):

| Year | [dp] total | [dp] MEDLINE | [dp] PubMed-not-MEDLINE | [dp] in-process | [dp] publisher | [edat] total | [edat] MEDLINE | [edat] not-MEDLINE | [edat] preprint[pt] |
|---|---|---|---|---|---|---|---|---|---|
| 2000 | 532,636 | 486,933 | 34,712 | 0 | 10,991 | 499,203 | 466,048 | 23,938 | 0 |
| 2005 | 700,540 | 651,444 | 47,912 | 1 | 1,183 | 691,706 | 643,131 | 47,717 | 0 |
| 2010 | 942,372 | 847,902 | 92,683 | 0 | 1,787 | 839,733 | 752,603 | 85,670 | 0 |
| 2012 | 1,090,513 | 949,113 | 137,968 | 3 | 3,429 | 941,522 | 812,976 | 126,789 | 0 |
| 2013 | 1,150,127 | 997,889 | 150,012 | 2 | 2,224 | 998,664 | 860,438 | 136,261 | 0 |
| 2014 | 1,205,919 | 1,020,137 | 182,202 | 13 | 3,567 | 1,068,128 | 889,285 | 175,500 | 0 |
| 2015 | 1,258,185 | 1,028,382 | 225,219 | 7 | 4,577 | 1,091,650 | 878,667 | 209,496 | 0 |
| 2016 | 1,285,555 | 1,011,065 | 266,143 | 9 | 8,338 | 1,136,715 | 877,333 | 250,376 | 0 |
| 2017 | 1,304,375 | 1,002,622 | 298,475 | 6 | 3,272 | 1,135,714 | 858,066 | 274,457 | 0 |
| 2018 | 1,351,720 | 1,020,542 | 325,150 | 23 | 6,005 | 1,180,955 | 871,325 | 303,721 | 0 |
| 2019 | 1,418,988 | 1,065,792 | 349,164 | 22 | 4,010 | 1,243,065 | 914,720 | 324,904 | 0 |
| 2020 | 1,641,225 | 1,193,401 | 440,114 | 58 | 7,652 | 1,443,692 | 1,034,158 | 401,985 | 1,527 |
| 2021 | 1,787,564 | 1,254,511 | 525,653 | 143 | 7,257 | 1,542,806 | 1,049,837 | 485,417 | 1,385 |
| 2022 | 1,783,568 | 1,222,118 | 549,388 | 198 | 11,864 | 1,540,382 | 1,013,951 | 514,651 | 840 |
| 2023 | 1,697,549 | 1,107,806 | 569,751 | 3,438 | 16,554 | 1,499,881 | 941,388 | 539,752 | 13,957 |
| 2024 | 1,739,997 | 1,112,094 | 570,203 | 43,222 | 14,457 | 1,546,982 | 955,310 | 531,906 | 16,403 |
| 2025 | 1,882,044 | 1,092,670 | 601,202 | 160,724 | 27,367 | 1,700,143 | 963,358 | 565,051 | 19,249 |
| 2026 (to 15 Oct) | 1,541,148 | 776,141 | 444,109 | 134,650 | 186,247 | 1,382,492 | 638,101 | 449,123 | 16,307 |

- Other publication-type counts by [dp] [VERIFIED-QUERY] ([esearch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=2024%5Bdp%5D+AND+journal+article%5Bpt%5D)):
  - `journal article[pt]`: 2016 1,198,316; 2019 1,324,819; 2021 1,663,924; 2022 1,667,418; 2023 1,574,142; 2024 1,620,952; 2025 1,764,223.
  - `review[pt]`: 2024 226,682.
  - `retracted publication[pt]` by publication year: 2021 3,771; 2022 7,275; 2023 2,380; 2024 2,317.
  - `english[la]`: 2024 1,711,067 (98.3% of 2024[dp]).
  - `2025[dp] AND english[la] AND journal article[pt] NOT review[pt] NOT preprint[pt]` = 1,475,197.
  - All years: `preprint[pt]` = 69,668; `journal article[pt]` = 38,663,924.

#### Indexing lag and the 2025-2026 status backlog [VERIFIED-QUERY]
- By entry month, total new records are stable at about 135-160K per month. The MEDLINE-status share for recent months falls while publisher-supplied rises ([esearch monthly edat](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=2026%2F09%5Bedat%5D+AND+publisher%5Bsb%5D)):

| Entry month | Total | MEDLINE | In-process | Publisher |
|---|---|---|---|---|
| 2025-01 | 144,885 | 81,873 | 10,688 | 1,282 |
| 2025-07 | 161,936 | 90,912 | 12,736 | 2,207 |
| 2026-01 | 141,893 | 76,840 | 12,864 | 4,908 |
| 2026-05 | 155,773 | 79,399 | 12,261 | 11,798 |
| 2026-07 | 156,763 | 69,691 | 11,073 | 26,076 |
| 2026-08 | 134,281 | 50,786 | 8,540 | 29,843 |
| 2026-09 | 140,085 | 42,778 | 6,722 | 47,593 |
| 2026-10 (1-15) | 59,977 | 13,232 | 2,695 | 26,739 |

#### Automated MeSH indexing: dated changes [PRIMARY-DOC] and the measured break [VERIFIED-QUERY]
- From the NLM indexing FAQ ([NLM indexing FAQ](https://www.nlm.nih.gov/bsd/indexfaq.html), last reviewed 24 Feb 2023):
  - "As of April 2022, all journals indexed for MEDLINE are done by automated indexing".
  - MTIFL (human curation of algorithm output) began in 2011. MTIA full automation was tested in 2019. MTIX, a neural network, was released in 2024 and trained on MEDLINE citations from 2007-2022.
  - Automated citations are "generally completed within 1 day of receipt". In FY2021, fully human indexing averaged 145 days.
  - IndexingMethod "Automated" means algorithmic indexing. "Curated" means the algorithm's output was reviewed by a human. A missing attribute means fully human indexing.
  - Since February 2023 you can search `indexingmethod_automated` / `indexingmethod_curated`.
- NLM Technical Bulletin, 29 Apr 2024: MTIX "replaces the MTIA" algorithm. "Roughly one-third of articles indexed via automation will also receive human curation". F1 rose from 58% (MTIA) to 74% (MTIX) — [NLM Technical Bulletin ma24](https://www.nlm.nih.gov/pubs/techbull/ma24/ma24_mtix.html)
- Measured break, MEDLINE records by entry year [VERIFIED-QUERY] ([esearch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=2024%5Bedat%5D+AND+medline%5Bsb%5D+AND+indexingmethod_automated)):

| Entry year | MEDLINE | Automated | Curated | Human only |
|---|---|---|---|---|
| 2016 | 877,333 | 37,307 | 133,330 | 706,696 |
| 2019 | 914,720 | 87,833 | 164,380 | 662,507 |
| 2020 | 1,034,158 | 286,655 | 185,912 | 561,591 |
| 2021 | 1,049,837 | 571,724 | 106,084 | 372,029 |
| 2022 | 1,013,951 | 872,659 | 110,949 | 30,343 |
| 2023 | 941,388 | 822,849 | 111,047 | 7,492 |
| 2024 | 955,310 | 709,421 | 239,568 | 6,321 |
| 2025 | 963,358 | 784,404 | 161,875 | 17,079 |

- Unofficial syntaxes such as `automated[im]` (340,821) only match the free-text word "automated" and must not be used [VERIFIED-QUERY] — [esearch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=automated%5Bim%5D)

#### Annual baseline XML (bulk) [VERIFIED-QUERY, directory listing]
- The 2026 baseline is files `pubmed26n0001.xml.gz` to `pubmed26n1334.xml.gz`. File timestamps are 2026-01-29/30, although the README says the baseline "is released in December of each year". The README was last updated January 30, 2026, and the DTD is `pubmed_250101.dtd` — [baseline directory](https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/); [README](https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/README.txt)
- Daily update files run from `pubmed26n1335` to `pubmed26n1683`, with the latest dated 2026-10-15 14:03. They "include new, revised, and deleted citations" — [updatefiles directory](https://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/); [PubMed User Guide](https://pubmed.ncbi.nlm.nih.gov/help/)

#### NLM official statistics pages
- The page "MEDLINE Citation Counts by Year of Publication (as of January 2023)" is derived from the 2023 baseline and was last reviewed May 27, 2023. It counts only the MEDLINE subset — [NLM table](https://www.nlm.nih.gov/bsd/medline_cit_counts_yr_pub.html):
  - Selected totals: 1964 158,922; 1970 211,330; 1980 272,490; 1990 388,119; 2000 485,493; 2010 735,004; 2015 878,403; 2016 862,840; 2017 848,829; 2018 866,938; 2019 903,225; 2020 993,289; 2021 1,063,140; 2022 981,270 (partial at production); 2023 11,731 (partial).
  - Grand total 30,011,769, including pre-1947 records (66,663) and 1947-1963 OLDMEDLINE.
  - The US-publisher share fell from 46% (1990s-2001) to 36% (2021-2022).
  - "As of the 2017 baseline, all OLDMEDLINE subset citations were converted to MEDLINE status".
- The "MEDLINE PubMed Production Statistics" page now says it "is no longer being maintained" and points to an Archive-It copy dated 2025-01-03 — [NLM production stats](https://www.nlm.nih.gov/bsd/medline_pubmed_production_stats.html)
- Also retired: the XML element-descriptions page (archived 2024-02-20) — [NLM elements descriptions](https://www.nlm.nih.gov/bsd/licensee/elements_descriptions.html) — and the "MEDLINE, PubMed, and PMC: how are they different" page — [NLM difference page](https://www.nlm.nih.gov/bsd/difference.html)
- MEDLINE overview (last reviewed Sept 8, 2025): "more than 5,200 worldwide journals" in "about 40 languages", "more than 31 million references", coverage from 1966 plus selected earlier literature, and MEDLARS "originated in 1964" — [NLM MEDLINE overview](https://www.nlm.nih.gov/medline/medline_overview.html)

#### Preprints and PMC deposit policy
- "As of June 2020, PubMed Central (PMC) includes preprints that report NIH-funded research results" [PRIMARY-DOC] — [PubMed User Guide](https://pubmed.ncbi.nlm.nih.gov/help/)
- Phase 2 of the NIH Preprint Pilot launched January 30, 2023. It covers preprints acknowledging NIH support posted on or after January 1, 2023 to bioRxiv, medRxiv, arXiv or Research Square. Phase 1 (June 2020 to June 2022, COVID-19 only) added more than 3,300 preprints [SECONDARY, search summary] — [NCBI Insights](https://ncbiinsights.ncbi.nlm.nih.gov/2023/01/09/next-phase-preprint-pilot/); [PMC NIH preprints page](https://pmc.ncbi.nlm.nih.gov/about/nihpreprints); [Phase 1 evaluation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9774216/)
- Measured: `preprint[pt]` by [dp] was 1,482 (2020), 1,401 (2021), 822 (2022), then 13,200 (2023), 16,059 (2024), 20,952 (2025) [VERIFIED-QUERY] — [esearch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=2024%5Bdp%5D+AND+preprint%5Bpt%5D)
- The 2024 NIH Public Access Policy applies to author accepted manuscripts accepted "on or after July 1, 2025". They must be submitted to PMC and made available "without embargo upon the Official Date of Publication" [PRIMARY-DOC] — [NIH Grants: Public Access](https://grants.nih.gov/policy-and-compliance/policy-topics/public-access)

### Inferences
- **Which date field to use:**
  - `[dp]`/`[pdat]` overstates annual output by about 12% in recent years (2024 [dp]/[edat] = 1.125, my calc) because e-pub and print dates are double-counted across adjacent years. For pre-2000 years [dp] ≈ [edat].
  - For a publication-year series, the cleanest options are (a) parsing the baseline XML and assigning each PMID a single year (e.g., the earliest of ArticleDate and PubDate), or (b) using Europe PMC's single PUB_YEAR (Section 2), which matches PubMed [dp] exactly for 1950 and 1990.
  - For a flow/"arrivals" series, `[edat]` is the best E-utilities proxy.
  - `[crdt]` is distorted by retrospective record creation (2010 crdt 1.06M vs edat 0.84M). `[mhda]` is distorted by MeSH re-indexing (2021 mhda 1.92M spike during the automation transition). Do not use either as a publication proxy.
- **Composition shift:** PubMed-not-MEDLINE grew from 6.5% of [dp] records (2000) to 32.8% (2024) (my calc), while MEDLINE by entry year fell from 1.050M (2021) to 0.941M (2023). "PubMed growth" therefore mixes real output growth with PMC/funder-deposit-driven inclusion of non-MEDLINE journals. For AI-impact analysis, report MEDLINE and non-MEDLINE separately, ideally on a fixed panel of journals indexed before 2022.
- **Field breakdowns via MeSH:** these change regime between 2019 and 2022 (human to automated MTIA, then MTIX in 2024). MeSH-based topic shares around Nov 2022 are confounded by the indexing-method switch and the MTIX upgrade (April 2024).
- **Lag:**
  - Total records by entry month are complete almost immediately.
  - MEDLINE status for the latest ~3 months is incomplete (publisher-supplied grew to 47.6K in Sept 2026). The 2025 [dp] count still has 160,724 in-process records, which suggests a 2025-2026 processing backlog that should be monitored.
  - Treat the latest 12 months of [dp] counts as provisional, because print dates arrive later.
- **2023 dip and 2025 jump:**
  - PubMed fell in 2023 (-4.8% [dp], -2.6% [edat]) and rose sharply in 2025 (+8.2% [dp], +9.9% [edat]) (my calcs).
  - The 2022 spike in `retracted publication[pt]` (7,275) is consistent with mass retractions of 2021-2022 papers.
  - Any post-ChatGPT effect must be separated from post-COVID normalization and publisher-specific shocks (see Section 8, Hanson et al.). This attribution is my hypothesis, not a finding.

### Gaps
- I could not verify whether NLM still publishes any annual MEDLINE/PubMed statistics (citations added per fiscal year) after the production-stats page was retired. The archived copy (Archive-It) was not consulted.
- I could not verify a primary NLM source on predatory or low-quality journals entering PubMed via PMC deposits, or on recent MEDLINE journal-selection (LSTRC) changes. The PubMed guide only confirms that funder-compliance deposits from non-MEDLINE journals create records.
- I found no official count of Phase 2 preprints beyond the `preprint[pt]` counts measured above.
- The reason the 2026 baseline files are dated late January 2026 rather than December 2025 is not documented in the README.

## 2. Europe PMC: coverage and counting via REST API

### Takeaway
Europe PMC's free REST API gives one-call `hitCount` totals per query. PubMed/MEDLINE records (SRC:MED) carry a single PUB_YEAR, so they avoid PubMed's [dp] double counting. The API also adds Agricola, Chinese Biological Abstracts, preprints (SRC:PPR), patents and theses, which **must be excluded by SRC filter**, because the unfiltered "all" count includes patents.

### Cited Findings
- **Endpoint:** `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PUB_YEAR:2024 AND SRC:MED&format=json&pageSize=1` returns `hitCount`. It is free and needs no key. Searchable date/source fields confirmed by the fields endpoint: PUB_YEAR, FIRST_PDATE, E_PDATE, P_PDATE, CREATION_DATE, FIRST_IDATE, INDEX_DATE, SRC, PUB_TYPE, HAS_FT, IN_EPMC, IN_PMC [VERIFIED-QUERY] — [EPMC search](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PUB_YEAR:2024%20AND%20SRC:MED&format=json&pageSize=1); [EPMC fields](https://www.ebi.ac.uk/europepmc/webservices/rest/fields?format=json)
- **Totals on 2026-10-15** [VERIFIED-QUERY]: all 49,018,571; MED 41,178,084; PAT (patents) 4,229,296; PPR (preprints) 1,259,436; AGR (Agricola) 1,026,549; PMC-only 998,618; ETH (theses) 176,799; CBA 142,377; CTX 3,915; HIR 2,868; NBK 5 — [EPMC search SRC:MED](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=SRC:MED&format=json&pageSize=1)
- **Annual counts by PUB_YEAR** [VERIFIED-QUERY] ([EPMC search](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PUB_YEAR:2025%20AND%20SRC:PPR&format=json&pageSize=1)):

| Year | All sources | MED | PPR | AGR | PMC | PUB_TYPE "journal article" | PUB_TYPE "research-article" |
|---|---|---|---|---|---|---|---|
| 1950 | 90,071 | 85,773 | 0 | 168 | 3,968 | 86,075 | 4,020 |
| 1990 | 467,500 | 410,999 | 0 | 18,272 | 6,033 | 400,114 | 22,945 |
| 2000 | 644,946 | 531,007 | 0 | 19,891 | 5,085 | 505,664 | 31,849 |
| 2010 | 1,213,079 | 824,351 | 0 | 22,377 | 9,780 | 786,487 | 163,279 |
| 2015 | 1,136,656 | 1,090,512 | 3,064 | 21,810 | 15,314 | 1,027,217 | 309,165 |
| 2019 | 1,334,261 | 1,230,877 | 48,759 | 24,939 | 23,147 | 1,172,684 | 414,533 |
| 2020 | 1,593,656 | 1,404,455 | 128,326 | 24,686 | 30,483 | 1,325,751 | 510,351 |
| 2021 | 1,782,003 | 1,559,779 | 153,830 | 30,259 | 35,191 | 1,483,959 | 620,436 |
| 2022 | 1,794,826 | 1,576,925 | 147,775 | 30,372 | 39,415 | 1,506,624 | 685,880 |
| 2023 | 1,738,778 | 1,498,048 | 176,118 | 28,625 | 35,911 | 1,419,018 | 616,212 |
| 2024 | 1,797,834 | 1,538,581 | 182,128 | 42,382 | 34,690 | 1,475,791 | 619,064 |
| 2025 | 1,967,103 | 1,676,899 | 187,034 | 67,413 | 35,702 | 1,640,379 | 713,921 |
| 2026 (to 15 Oct) | 1,683,951 | 1,468,195 | 175,479 | 17,083 | 23,143 | 1,397,202 | 530,075 |

- In 2010, "all sources" (1,213,079) exceeds MED + AGR + PMC by about 356K. Patents (SRC:PAT) are the only remaining large source, so the unfiltered count is unusable as a publication series [VERIFIED-QUERY, inference about patents] — [EPMC search](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PUB_YEAR:2010&format=json&pageSize=1)

### Inferences
- **PUB_YEAR is single-valued:** Europe PMC's MED count equals PubMed [dp] exactly for 1950 (85,773) and 1990 (410,999). For 2024 it is 1,538,581, close to PubMed [edat] (1,546,982) and 11.6% below PubMed [dp] (1,739,997). Europe PMC MED by PUB_YEAR is therefore a convenient de-duplicated PubMed publication-year series.
- **Growth rates (my calcs, "all sources" series; non-MED/PPR/AGR/PMC sources add only about 6K/yr after 2015)**: 4.1%/yr in 2015-2019, 10.4%/yr in 2019-2022 (COVID), 3.1%/yr in 2022-2025. Year-on-year: -5.0% in 2023, +2.7% in 2024, +9.0% in 2025 (MED only). This is the same pattern as PubMed.
- **Suitability for AI-impact analysis:** useful as an independent pipeline check on PubMed and for life-science preprint volumes (SRC:PPR). Keep SRC filters explicit, because AGR jumped in 2024-2025 (42K, then 67K), which looks like an ingestion change.

### Gaps
- Europe PMC's search-syntax documentation page returned HTTP 403 to my fetcher. So I could not quote how PUB_YEAR is derived (print vs electronic vs first publication date). The single-year behaviour above is inferred from the data.
- I found no Europe PMC changelog describing the 2024-2025 AGR increase.

## 3. Crossref: journal-article counts by year/type, public data file, caveats

### Takeaway
Crossref is the broadest free source of DOI-registered journal articles (124.5M journal-article records; 6.08M with a 2024 "published" date). The REST API's `facet=published:*` returns a full annual series in one call. Crossref counts grow faster than curated indexes (about 7%/yr in 2010-2019) because publisher membership expands (34,071 members). The series has dated artifacts (default-date spikes in 1970 and 2000, future dates up to 2203) and type-specific bulk registrations (1.46M "component" records dated 2023). **Registration date ≠ publication date.**

### Cited Findings
- **Access and limits:**
  - `https://api.crossref.org/works?rows=0&filter=type:journal-article&facet=published:*`. This is free with no key. Response headers in the public pool: `x-rate-limit-limit: 5`, `x-rate-limit-interval: 1s`, `x-concurrency-limit: 1`, `x-api-pool: public-single`. Facet queries ran in the `public-array` pool with `x-rate-limit-limit: 1` [VERIFIED-QUERY] — [Crossref facet query](https://api.crossref.org/works?rows=0&filter=type:journal-article&facet=published:*)
  - Official limits are Public 5 / concurrency 1; Polite (with `mailto`) 10 / 3; Metadata Plus 150 / no concurrency limit (doc last updated 16 Oct 2025) [PRIMARY-DOC] — [Crossref access & authentication](https://www.crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication/)
- **Size on 2026-10-15** [VERIFIED-QUERY] ([type facet](https://api.crossref.org/works?rows=0&facet=type-name:*)):
  - Total works: 187,710,293.
  - By type: Journal Article 124,505,838; Chapter 24,913,051; Conference Paper 10,114,615; Component 9,445,925; Posted Content 4,137,147; Dataset 3,472,285; Peer Review 1,133,381; Dissertation 1,097,763.
  - Members: 34,071. Journal title records: 172,099 — [members](https://api.crossref.org/members?rows=0); [journals](https://api.crossref.org/journals?rows=0)
- **Journal articles by "published" year** (facet; identical to `from-pub-date/until-pub-date` filter counts) [VERIFIED-QUERY] ([Crossref per-year filter](https://api.crossref.org/works?rows=0&filter=type:journal-article,from-pub-date:2024-01-01,until-pub-date:2024-12-31)):
  - 1900 44,188; 1920 60,357; 1939 115,192; 1945 80,949; 1950 143,740; 1960 239,707.
  - 1969 399,568; **1970 468,291**; 1971 441,552.
  - 1980 615,719; 1990 949,821; 1999 1,293,548; **2000 1,534,170**; 2001 1,414,875; 2005 1,747,851.
  - 2010 2,402,923; 2015 3,344,847; 2016 3,581,958; 2017 3,790,722; 2018 4,099,668; 2019 4,434,415.
  - 2020 4,891,522; 2021 5,277,683; 2022 5,463,177; 2023 5,615,836; 2024 6,082,385; 2025 6,648,216; 2026 (to 15 Oct) 5,447,897.
  - 2027: 40,203. Scattered records are dated up to 2203.
- **Same journal-article set by alternative date filters** [VERIFIED-QUERY] ([created-date filter](https://api.crossref.org/works?rows=0&filter=type:journal-article,from-created-date:2025-01-01,until-created-date:2025-12-31)):

| Year | Published | Created (DOI registration) | Online-pub | Print-pub | With abstract | Posted-content (published) | All types (published) |
|---|---|---|---|---|---|---|---|
| 2000 | 1,534,170 | 0 | 279,918 | 1,456,948 | 251,687 | 3,679 | 1,969,305 |
| 2010 | 2,402,923 | 4,015,762 | 1,914,583 | 2,066,667 | 570,480 | 26,217 | 3,619,005 |
| 2015 | 3,344,847 | 4,135,340 | 2,180,175 | 2,646,201 | 874,728 | 45,111 | 4,736,185 |
| 2019 | 4,434,415 | 5,442,517 | 2,930,721 | 3,129,649 | 1,696,682 | 139,733 | 6,579,045 |
| 2020 | 4,891,522 | 5,727,656 | 3,324,721 | 3,347,949 | 2,182,360 | 294,029 | 7,454,807 |
| 2021 | 5,277,683 | 6,334,538 | 3,644,131 | 3,530,705 | 2,657,728 | 303,874 | 7,654,300 |
| 2022 | 5,463,177 | 6,001,975 | 3,798,951 | 3,456,326 | 2,863,241 | 338,817 | 8,357,070 |
| 2023 | 5,615,836 | 6,261,082 | 4,014,958 | 3,394,983 | 3,084,204 | 720,195 | 10,308,299 |
| 2024 | 6,082,385 | 6,722,922 | 4,362,630 | 3,598,289 | 3,375,018 | 547,940 | 9,016,038 |
| 2025 | 6,648,216 | 7,592,777 | 4,833,180 | 3,822,219 | 3,676,318 | 625,594 | 9,908,386 |

- **The 2023 all-types spike is a type artifact** [VERIFIED-QUERY]. "Component" records with 2023 dates number 1,459,813, against 19,136 for 2022 and 63,859 for 2024. Posted content was 720,195 in 2023, against 338,817 and 547,940. Datasets go the other way: 501,283 for 2022 against 61,000 for 2023 — [type facet 2023](https://api.crossref.org/works?rows=0&filter=from-pub-date:2023-01-01,until-pub-date:2023-12-31&facet=type-name:*)
- **Public Data File** [PRIMARY-DOC]:
  - An annual tar of JSONL covering "all Crossref-registered DOIs". The 2025 file is about 200 GB.
  - Available via Academic Torrents (doi.org/10.13003/nggf-vt1j) or the AWS S3 requester-pays bucket `api-snapshots-reqpays-crossref` (about US$18 estimated transfer).
  - Metadata Plus monthly snapshots are available by the 5th of each month (paid token). Page updated 20 Oct 2025 — [Crossref bulk downloads](https://www.crossref.org/documentation/retrieve-metadata/bulk-downloads/)

### Inferences
- **Growth (my calcs, journal-article by published year):** 7.0%/yr in 2010-2019, 7.3%/yr in 2015-2019, 7.2%/yr in 2019-2022, 6.8%/yr in 2022-2025. Year-on-year: +2.8% in 2023, +8.3% in 2024, +9.3% in 2025. By DOI registration year: 2024 to 2025 +12.9%.
  - Crossref has no 2023 dip (unlike PubMed and Europe PMC) and accelerates in 2024-2025.
  - Part of this growth is coverage expansion (new members, backfile registration, Chinese and regional publishers joining), not output growth.
  - For AI-impact work, build a **fixed panel** (e.g., ISSNs or members with continuous deposits since 2015) before comparing pre/post-Nov 2022 trends.
- **Do not use `created` for publication timing.** 2010 shows 4.0M journal-article DOIs created against 2.4M published, which is backfile registration. Registration also lags online publication.
- **Default dates:** spikes at 1970 and 2000 (likely default dates) and future-dated records mean very early years and the boundary years need cleaning.
- **Type filtering is essential:** "All types" counts are dominated by registration campaigns (components, datasets, peer reviews, posted content). Use `type:journal-article` and treat posted-content separately.
- **Abstract coverage** rose from 26% (2015) to 55% (2024-2025) (my calc). Text-based (LLM-signature) analyses using Crossref abstracts face a time-varying coverage selection.

### Gaps
- I could not retrieve Crossref's official definition of the `published` field and the `from-pub-date` filter. The old GitHub doc now only says "We have moved the main documentation page".
  - From the data, `published` behaves as the earliest available of online/print dates, since its counts lie between and above the online-only and print-only counts. This is unverified.
- Record count and release date of the 2025 Public Data File were not stated on the docs page. The release blog (doi.org/10.64000/7s70g-drz77) was not fetched.
- I found no public Crossref statistic decomposing growth into new members vs existing members.

## 4. OpenAlex: coverage, counting, snapshot, 2025-2026 changes (API keys/pricing, Walden, XPAC, topics) and count stability

### Takeaway
OpenAlex remains the only free, CC0, all-discipline index with a full bulk snapshot. Since early 2026, however, the API is **metered**:
- No key: a $0.10/day budget shared per IP address, exhausted in our environment.
- Free key: $1/day. A `group_by` count costs $0.0001.
- The public S3 snapshot is now **quarterly**.

Counts are not stable across versions:
- The Nov 2025 "Walden" rewrite added ~190M records (mostly excluded from the API's default "core" corpus) and changed 2018-2024 article counts by +1.05% overall (+3.2% for 2024).
- On 6 Oct 2026 every work's topic assignment was regenerated.

Reproducible AI-impact analyses should pin a dated snapshot.

### Cited Findings
- **Keyless API in our environment** [VERIFIED-QUERY]:
  - `works?filter=publication_year:2024&group_by=type` returned HTTP 429: "Insufficient budget. This request has no API key, so it counts against the free daily budget shared by everyone on your network's IP address, and that budget is used up ($0 remaining; resets at midnight UTC)". Headers included `X-RateLimit-Limit-USD: 0.1` and `X-RateLimit-Cost-Required-USD: 0.0001`.
  - A singleton lookup (`/works/W2741809807`) still returned 200 at cost $0.
  - `/rate-limit` returned 401 ("You must provide a valid API key").
  - [OpenAlex group_by query](https://api.openalex.org/works?filter=publication_year:2024&group_by=type)
- **Pricing** [PRIMARY-DOC]:
  - Singleton: free. List+filter: $0.0001. `group_by` on a list: $0.0001. `group_by` on a search: $0.001. Keyword search: $0.001. Semantic search: $0.001. PDF download: $0.01.
  - Budgets: no key $0.10/day; free key $1/day. Page last updated Oct 9, 2026 — [OpenAlex example costs](https://help.openalex.org/access/example-costs/)
  - Rate limits: 10 req/s without a key, 30 with a free key or prepaid, 50 on an annual plan. A 429 results from either the budget or the per-second limit, and the budget resets at midnight UTC — [OpenAlex authentication](https://help.openalex.org/api/authentication/)
  - Annual plans: Member $5,000 ($20/day budget), Member+ $10,000 ($100/day, includes a daily snapshot), Partner from $20,000. No academic discount beyond the free tier. Page last updated Aug 11, 2026 — [OpenAlex pricing](https://help.openalex.org/access/pricing/)
- **Dated policy announcements** [PRIMARY-DOC]:
  - The blog post "New Features and Usage-Based Pricing" (Feb 24, 2026) says "As we announced in January, you'll need an API key for all requests", and that "Every API key gets $1 of free usage per day" — [OpenAlex blog author archive](https://blog.openalex.org/author/jason); [post](https://blog.openalex.org/openalex-api-new-features-and-usage-based-pricing/)
  - The roadmap of Jan 16, 2026 lists 477M works and the Walden rewrite "done". It proposed a credit model that was later superseded by the Feb pricing — [OpenAlex 2026 Roadmap](https://blog.openalex.org/?p=3934)
  - A third-party page dates the key requirement to 13 Feb 2026 [SECONDARY] — [CASRAI news](https://casrai.org/news/openalex-api-keys-mandatory-usage-based-pricing-2026)
- **Snapshot (bulk)** [VERIFIED-QUERY + PRIMARY-DOC]:
  - Location: `s3://openalex` (HTTP listing works anonymously). The README says it is "released once a quarter", with data in `data/jsonl/` and `data/parquet/`, licence CC0. `legacy-data/` is "the frozen pre-2026 layout … not updated" — [S3 README](https://openalex.s3.amazonaws.com/README.txt); [LICENSE](https://openalex.s3.amazonaws.com/LICENSE.txt)
  - Release notes: "Public releases land on the second Wednesday of January, April, July and October".
    - 2026 releases so far: 01-15, 02-03, 02-25, 03-30, 04-29, 05-22, 06-25, 09-23, 10-14.
    - The 2025-11-12 release was the "switch to walden dataset … includes 'xpack' records in works, so full works count is 463M".
    - Earlier 2025 releases were roughly monthly.
    - Content-changing releases include the 2026-06-25 corresponding-author overhaul (+7.04M works) and the 2026-04-29 fix of a "PubMed truncated abstract bug affecting 7M works".
    - [RELEASE_NOTES](https://openalex.s3.amazonaws.com/RELEASE_NOTES.txt)
  - The public snapshot is free (AWS Open Data covers about $70 egress per download); paid plans get daily snapshots.
  - Size: about 626M records in each format. JSONL is about 745 GB (about 615 GB for works) and Parquet about 770 GB as of the Sept 2026 release.
  - The snapshot includes XPAC works. To match the API default (about 327M works vs about 476M with `corpus=all`), filter on `is_xpac`.
  - "Counts and records drift between releases".
  - [OpenAlex snapshot docs](https://help.openalex.org/access/snapshot/)
- **Walden rewrite** [PRIMARY-DOC]:
  - Announced Aug 9, 2025: 50M+ works to be added; goal that citation counts change by no more than 5%; topics for post-migration works use an updated algorithm.
  - Schedule: `data_version=2` beta on Oct 1, default on Nov 1, old data removed from the API on Dec 1.
  - [OpenAlex blog, Aug 2025](https://blog.openalex.org/were-rebuilding-openalex-while-its-running-heres-whats-changing/)
  - Launched Nov 3, 2025 with "190 million new works … from DataCite and thousands of repositories". The OREO comparison tool was removed on Dec 13, 2025 — [Walden launch post](https://blog.openalex.org/openalex-rewrite-walden-launch/)
- **XPAC / expansion corpus** [PRIMARY-DOC]:
  - A "one-time batch" added in Nov 2025 that "hasn't grown since". Mostly datasets and single-repository records with thin metadata.
  - Size: core 320M+, expansion about 190M, all 510M+.
  - The API defaults to core. `include_xpac=true` is deprecated in favour of `corpus=all`.
  - [OpenAlex XPAC docs](https://help.openalex.org/how-to-use-the-api/xpac)
  - Figures for the total conflict across official pages: 463M (snapshot notes, Nov 2025), 477M (roadmap, Jan 2026), 476M (snapshot docs), 510M+ (XPAC docs). They differ by date and scope.
- **Measured effect of Walden on counts** (journal articles and reviews 2018-2024, Sept 2025 snapshot vs Walden snapshot of 2026-02-25):
  - Totals: 34,884,266 vs 35,249,948 (+1.05%).
  - By year: 2018 -0.02%, 2019 +0.23%, 2020 +0.05%, 2021 -0.12%, 2022 +1.67%, 2023 +1.67%, 2024 +3.20%.
  - Repository-type sources rose +540%. Gold OA fell -41.8% and diamond OA rose +249% (reclassification).
  - Walden updates followed on 15 Jan, 3 Feb and 25 Feb 2026.
  - [Haupka 2026, Scholarly Communication Analytics, doi:10.59350/4r6jj-90k30](https://rogue-scholar.org/records/nj8nj-9f827)
- **Topic reclassification** (Oct 6, 2026) [PRIMARY-DOC]:
  - The taxonomy is unchanged: 4,516 topics, 252 subfields, 26 fields, 4 domains. A new classifier uses title, abstract and venue (not citations).
  - Median institution: field mix 97% the same, subfield 92%, topic 78%.
  - Old assignments are kept in release v2.0.0. `/text/topics?version=1` is served until 13 Jan 2027.
  - Snapshot users must fully reload from the Oct 14 snapshot because `updated_date` is unchanged.
  - [OpenAlex topics post](https://blog.openalex.org/same-topics-better-assignments/)
- **Trusted journal lists** (Oct 15, 2026) [PRIMARY-DOC]:
  - New source field `listed_in` and works filter `primary_location.source.listed_in:<list>`, with `group_by` support.
  - 61 lists, e.g., MEDLINE (~5,200 sources), DOAJ (~23,000), CWTS core (~36,000), SciELO, Latindex, national lists.
  - Intended as an allow-list approach to excluding predatory venues ("`listed_in` is not us saying a journal is good").
  - [OpenAlex trusted lists post](https://blog.openalex.org/trusted-journal-lists-come-to-openalex/)
- **Comparative quality:** "OpenAlex is a superset of Scopus and can be a reliable alternative for some analyses, particularly at the country level", but has metadata accuracy and completeness issues — [Alperin et al. 2024, arXiv:2404.17663](https://arxiv.org/abs/2404.17663)

### Inferences
- **Cost of counting:** annual counts by type/field/country are cheap with a free key. 1,000 `group_by` calls cost $0.10, against a $1/day free budget. Keyless counting from shared-IP environments (cloud, proxies) will usually fail. Since we must not request keys, **the S3 snapshot is the practical route** (free, about 0.75 TB). Process it with DuckDB/Spark on Parquet, filtering `is_xpac=false`, `type`, `publication_year`, and optionally `primary_location.source.listed_in`.
- **Stability:**
  - Pin one snapshot date, and archive the manifest plus release notes.
  - Re-running "the same" query across 2025-2026 can shift recent-year article counts by about 1-3% (Walden) and topic/field shares by single-digit to 20+ percentage points (Oct 2026 classifier).
  - Recent-year counts in OpenAlex also keep rising for months as records are ingested.
- **Post-2022 comparisons:** the Walden change is largest for 2024 (+3.2%), so the source drift is concentrated in exactly the post-ChatGPT years. Comparing a pre-Walden 2022 baseline with a post-Walden 2024 count would bias the estimated AI effect upward.

### Gaps
- I could not verify the date when concepts were deprecated in favour of topics (topics introduced around 2024), or whether concepts are still served. The Oct 2026 topics post does not mention concepts.
- I did not verify OpenAlex availability in BigQuery or via the COKI Academic Observatory. GitHub API access to the COKI repo was not enabled in this session.
- No OpenAlex per-year counts were obtained (API budget exhausted; snapshot not downloaded given its size).

## 5. Scopus, Web of Science, Dimensions, Lens.org, Semantic Scholar, DBLP, CORE: access, cost, coverage, curation changes

### Takeaway
Only Dimensions explicitly advertises **no-cost access for non-commercial scientometric research** (Analytics, API and BigQuery). Elsevier's ICSR Lab URL now redirects to the Elsevier homepage, so its status is unverified. Scopus and WoS are subscription-only, and their curation actively removes journals. In Scopus, already-indexed content stays when a title is discontinued. Semantic Scholar's datasets are freely downloadable weekly releases, but its unauthenticated API is throttled (429 from our environment). Lens and CORE need tokens or keys. DBLP's API is behind a bot challenge from scripted clients.

### Cited Findings

#### Scopus (Elsevier)
- [PRIMARY-DOC] Source: [Scopus content policy & selection](https://www.elsevier.com/products/scopus/content/content-policy-and-selection)
  - Covers titles from "more than 7,000 publishers".
  - Titles are selected by the CSAB and re-evaluated after "validated publication concerns or outlier performance". An outlier-detection model "runs regularly to check all Scopus journals".
  - For discontinued titles, content already indexed "remains as a matter of scientific record". The discontinued-sources Excel list is "updated monthly".
  - From publication year 2023, eLife papers moved to the preprints collection.
- The former ICSR Lab URL (`elsevier.com/icsr/icsrlab`, which redirects to `/insights/icsr/lab`) now lands on the Elsevier homepage (HTTP 200 at `https://www.elsevier.com/`) [VERIFIED-QUERY] — [ICSR Lab URL](https://www.elsevier.com/insights/icsr/lab)
- Size benchmark: 27M documents for 2008-2017 — [Visser et al. 2021, QSS](https://arxiv.org/abs/2005.10732)
- Used by NSF NCSES (Section 6) and by SCImago, which Hanson et al. used with an "only WoS journals" filter — [Hanson et al. 2024, arXiv PDF](https://arxiv.org/pdf/2309.15884)

#### Web of Science (Clarivate)
- Hanson et al. note "the significant delistings that Clarivate performed in March 2023 that have had a marked effect on the calculation of impact factor". They cite MDPI (2023), "Clarivate Discontinues IJERPH and JRFM Coverage in Web of Science" — [Hanson et al. 2024, arXiv PDF](https://arxiv.org/pdf/2309.15884)
- CWTS's in-house WoS (SCIE/SSCI/AHCI/CPCI, without ESCI and BkCI) had 23M documents for 2008-2017 — [Visser et al. 2021](https://arxiv.org/abs/2005.10732)
- Clarivate product pages returned HTTP 403 to my client [VERIFIED-QUERY].

#### Dimensions (Digital Science)
- Free access "for non-commercial scientometric research projects" via Dimensions Analytics, the Analytics API and "Dimensions data on Google BigQuery"; ISSI members get special consideration; application by form; "160M+ publications" — [Dimensions scientometric research access](https://www.dimensions.ai/scientometric-research/)
- 36M documents for 2008-2017. Dimensions "relies strongly on data from Crossref", and the documents not in Crossref "typically seem to originate from PubMed" — [Visser et al. 2021](https://arxiv.org/abs/2005.10732)

#### Lens.org
- The scholarly API returned 401 "Missing/Incorrect Authorization Header" without a token [VERIFIED-QUERY] — [Lens API](https://api.lens.org/scholarly/search)
- Access requests require full name, organisation address, official email and a description of intended use. Attribution is required. API 2.19.3, docs last updated Apr 17, 2026 — [Lens API docs](https://docs.api.lens.org/)

#### Semantic Scholar (Ai2)
- Coverage: about 214M papers, 2.49B citations, 79M authors. Unauthenticated requests share "1000 requests per second … among all unauthenticated users". Keys start at 1 request/s — [S2 API product page](https://www.semanticscholar.org/product/api)
- Our two unauthenticated `paper/search/bulk` calls returned HTTP 429 [VERIFIED-QUERY] — [S2 bulk search](https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=&year=2024&fields=year)
- The Datasets API works without a key [VERIFIED-QUERY] — [S2 datasets latest](https://api.semanticscholar.org/datasets/v1/release/latest):
  - Latest release `2026-10-06`. 200 weekly releases since `2022-05-10`.
  - Datasets: papers (200M records in 30 files), abstracts (100M), s2orc_v2 (16M full texts), tldrs (58M), citations, authors, publication-venues.

#### DBLP
- Search API and statistics pages returned an Anubis "Making sure you're not a bot!" page (HTTP 202) to scripted requests from our environment on 2026-10-15 [VERIFIED-QUERY] — [dblp search API](https://dblp.org/search/publ/api?q=year%3A2024%3A&format=json&h=0); [dblp statistics](https://dblp.org/statistics/recordsindblp.html)

#### CORE (Open University / Jisc)
- The unauthenticated v3 search returned HTTP 429 with `x-ratelimit-limit: 10` [VERIFIED-QUERY] — [CORE API v3](https://api.core.ac.uk/v3/search/works?q=yearPublished%3A2024&limit=0)
- The CORE "about" page returned 403 to my fetcher.

### Inferences
- **Cheapest robust option for a multi-database comparison without keys or accounts:**
  - PubMed, Europe PMC and Crossref (live APIs).
  - OpenAlex and Semantic Scholar (bulk snapshots).
  - Dimensions under its scientometric programme, which requires an application.
- Scopus/WoS figures can be cited from published compilations (NCSES, SCImago, Hanson et al.) rather than queried.
- **Curation breaks:** WoS and Scopus delistings (WoS March 2023; Scopus monthly discontinuations) are a non-AI source of post-2022 trend breaks. In WoS, delisted journals' 2023+ content disappears from the index. In Scopus, future content stops but past content stays. Any post-2022 slowdown measured in curated databases can partly reflect curation of high-volume OA journals.

### Gaps
- No verified current information on ICSR Lab eligibility or cost. The page appears removed or relocated; this is unconfirmed.
- No verified number of WoS journals delisted in 2023-2026 (figures often quoted in the press were not verified here), and no current WoS Core Collection size.
- No verified Lens pricing tiers, CORE record counts, or DBLP records-per-year statistics (blocked).
- Semantic Scholar licence terms (the API licence agreement) were not reviewed.

## 6. Official statistical compilations: NSF NCSES S&E Indicators, Stanford AI Index, STM Report, SCImago, OECD

### Takeaway
NSF NCSES is the best official, documented Scopus-based world series. The Indicators 2026 "Discovery" report (July 2025) gives 3,275,079 S&E articles in 2023 (fractional counts, predatory journals filtered, English titles/abstracts, articles plus conference papers). Earlier points are 2,129,076 (2013) and 1,222,350 (2003): a 4.4%/yr growth over 2013-2023 (my calc). The AI Index gives AI-specific publication counts (about 102K in 2013 to over 242K in 2023). The STM Report, SCImago and OECD bibliometric pages could not be verified in this session.

### Cited Findings
- **NCSES Indicators 2024** (NSB-2023-33, Dec 2023), "Publications Output": 3.3M articles in 2022 (Scopus). "From 2012 to 2022, the global yearly publication total grew by 59%". China 27%, US 14% — [NCSES nsb202333](https://ncses.nsf.gov/pubs/nsb202333)
- **NCSES Indicators 2026** has a new thematic structure. The publications material is in "Discovery: R&D Activity and Research Publications" (NSB-2025-7, July 23, 2025). Other reports are "STEM Talent" (nsb20261, Feb 2026), "Translation to Impact" (nsb20262, May 2026) and "The State of U.S. S&E 2026" (May 2026) — [NCSES Indicators hub](https://ncses.nsf.gov/indicators); [Discovery report](https://ncses.nsf.gov/pubs/nsb20257)
- **Discovery report details** [PRIMARY-DOC] — [NCSES publication output chapter](https://ncses.nsf.gov/pubs/nsb20257/publication-output-by-geography-and-scientific-field):
  - World total: 3,275,079 (2023); 2,195,509 (2014); 2,129,076 (2013); 1,222,350 (2003).
  - Fractional counts for 2023: China 932,712; EU-27 558,077; US 430,843; India 228,174; UK 97,536; Japan 96,543.
  - Whole counts for 2023: US 568,973; China 1,003,473.
  - Scope: "conference proceedings and peer-reviewed journal articles with English-language titles and abstracts". Excludes dissertations, preprints, editorials, errata and letters.
  - Filters remove journals lacking substantive peer review ("sometimes referred to as predatory journals").
  - Data were extracted from Scopus in February 2025.
  - Field shares for 2023: health sciences 22.90%, engineering 17.42%, computer and information sciences 12.88%, biological and biomedical 11.85%.
  - Tables are available as a zip — [all tables zip](https://ncses.nsf.gov/pubs/nsb20257/assets/nsb20257-tables.zip)
- **Stanford AI Index 2025:** AI publications rose from about 102,000 (2013) to more than 242,000 (2023). The AI share of computer-science publications rose from 21.6% to 41.8%. The data source is not named on the chapter page — [AI Index 2025 R&D](https://hai.stanford.edu/ai-index/2025-ai-index-report/research-and-development)
- **AI Index 2026:** the report page exists, and Chapter 1 covers publications ("China leads in publication volume…"), but the landing page gives no counts — [AI Index 2026](https://hai.stanford.edu/ai-index/2026-ai-index-report)
- **SCImago:** Hanson et al. downloaded SCImago (Scopus-derived) yearly journal data for 1999-2022 with the "only WoS journals" filter — [Hanson et al. 2024, arXiv PDF](https://arxiv.org/pdf/2309.15884). The SCImago site returned 403 to my client.

### Inferences
- **Level differences:** NCSES (filtered Scopus, articles plus conference papers) gives about 3.3M per year for 2022-2023. Crossref has 5.5-5.6M journal-article DOIs for the same years, a ratio of about 1.7 (my calc). The gap is mostly selectivity (non-Scopus journals, non-research items registered as journal-article) plus NCSES's quality filters.
- **Growth (my calcs from NCSES):** 5.7%/yr in 2003-2013, 4.4%/yr in 2013-2023, 4.5%/yr in 2014-2023. The 2012-2022 +59% implies about 4.7%/yr.
- **Lag:** NCSES has 2 to 2.5 years of lag (2023 data published July 2025). It is useful as a pre-AI baseline and for 2023, but not yet for 2024-2026.

### Gaps
- STM Report: the 2018 PDF URLs I tried returned HTML or 404. I could not verify its headline figures (articles per year, journals, researcher counts, growth rates); quote them only from the original.
- SCImago country-rank coverage years and world totals were not verified (403).
- OECD bibliometric indicators (STI Scoreboard / "Bibliometric indicators" dataset) were not verified.
- The AI Index 2025/2026 publication data source and classification method were not confirmed.

## 7. Denominators: researchers (OECD MSTI, UNESCO UIS, Eurostat), doctorates (NSF SED), active authors

### Takeaway
Free machine-readable denominators are available and were tested live:
- OECD MSTI via SDMX: OECD-total researchers FTE 5.57M (2019) to 6.36M (2023); China 3.18M (2024).
- UNESCO UIS API: world researchers per million inhabitants 1,141 (2015) to 1,486 (2023).
- Eurostat: EU-27 researchers FTE 2.22M (2024).
- NSF SED: 59,015 US research doctorates in 2025; series since 1958.

Researcher numbers grew about 3.4%/yr (OECD FTE 2019-2023; UIS world per-capita 2015-2023) and EU-27 FTE about 3.8%/yr (2013-2024), while indexed output grew 4-7%/yr. This is the "strain" gap. Author-based denominators (unique publishing authors) exist only in studies, e.g., about 15.15M Scopus author IDs over 1996-2011, of whom less than 1% published every year.

### Cited Findings
- **OECD MSTI (SDMX)** [VERIFIED-QUERY]:
  - Dataflow `OECD.STI.STP,DSD_MSTI@DF_MSTI` version 1.3. Measure `T_RS` (Researchers), unit FTE.
  - OECD total: 2019 5,569,477; 2020 5,744,188; 2021 6,060,900; 2022 6,271,163; 2023 6,362,542.
  - USA: 2019 1,522,512; 2020 1,603,719; 2021 1,720,605; 2022 1,737,216; 2023 1,733,124.
  - China: 2019 2,109,460; 2020 2,281,134; 2021 2,405,509; 2022 2,637,193; 2023 3,001,302; 2024 3,179,806.
  - Japan: 2019 681,821; 2024 703,447. Germany: 2019 450,697; 2023 500,166.
  - [OECD SDMX query](https://sdmx.oecd.org/public/rest/data/OECD.STI.STP,DSD_MSTI@DF_MSTI,1.3/USA+OECD+CHN+DEU+JPN.......?startPeriod=2019)
- **UNESCO UIS** [VERIFIED-QUERY]:
  - Public API (no key), version `20260507`. The STI theme had a "February 2026 Data Release". Indicator `RESDEN.INHAB.TFTE` = researchers per million inhabitants (FTE).
  - "SDG: World": 2010 1,010.6; 2015 1,141.1; 2016 1,164.2; 2017 1,194.9; 2018 1,245.6; 2019 1,298.8; 2020 1,339.9; 2021 1,386.4; 2022 1,436.3; 2023 1,486.2.
  - [UIS API query](https://api.uis.unesco.org/api/public/data/indicators?indicator=RESDEN.INHAB.TFTE&geoUnit=SDG%3A%20World&start=2010&end=2024); [UIS version](https://api.uis.unesco.org/api/public/versions/default)
- **Eurostat `rd_p_persocc`** [VERIFIED-QUERY]:
  - EU-27 researchers, FTE, all sectors: 2013 1,476,139; 2015 1,565,287; 2017 1,709,559; 2019 1,853,797; 2020 1,887,380; 2021 1,991,034; 2022 2,087,394; 2023 2,155,632; 2024 2,224,215.
  - Dataset updated 2026-09-29. The time dimension starts in 1980, with sparse early years.
  - [Eurostat API query](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/rd_p_persocc?format=JSON&lang=EN&geo=EU27_2020&unit=FTE&sectperf=TOTAL&prof_pos=RSE&sex=T)
- **NSF Survey of Earned Doctorates** [PRIMARY-DOC] — [NCSES SED](https://ncses.nsf.gov/surveys/earned-doctorates):
  - Latest is 2025 (academic year July 2024 to June 2025), released 25 Sept 2026 (NSF 26-326): 59,015 research doctorates from 460 institutions; 98.6% PhDs; census with a 91.0% response rate.
  - Conducted "since academic year 1958". Table 1-1 gives 1958-2025 totals.
  - Access: Interactive Data Tool, RDAS, restricted microdata.
  - 2025-cycle changes: sex-question wording changed mid-collection (EO 14168), associate's-degree item made optional (10,322 imputed), and field taxonomy updates.
- **Active / continuously publishing authors:**
  - Scopus 1996-2011 had 15,153,100 author identifiers. "Only 150,608 (<1%)" published in every year, and they appear on 41.7% of papers. The total publishing workforce in Scopus is "probably indeed close to 15 million" — [Ioannidis, Boyack & Klavans 2014, PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0101698)
  - Hyperprolific authors: Scopus authors with more than 72 papers (one every 5 days) in a calendar year between 2000 and 2016: "more than 9,000 individuals", counting only full papers (articles, conference papers, substantive comments, reviews) — [Ioannidis, Klavans & Boyack 2018, Nature](https://www.nature.com/articles/d41586-018-06185-8)
- **Denominators used by Hanson et al.:**
  - OECD PhD graduates (37 countries, data to 2020), complemented by NSF data and Zwetsloot et al. for China and India.
  - UNESCO "9.5.2 Researchers per million inhabitants" (Feb 2023 release), projected to 2022 by linear regression.
  - They note results hold "when using global total employed researcher-hours".
  - [Hanson et al. 2024, arXiv PDF](https://arxiv.org/pdf/2309.15884)

### Inferences
- **Growth of researchers (my calcs):** OECD researchers FTE +3.4%/yr in 2019-2023. World researchers per million +3.4%/yr in 2015-2023 (per capita; add about 0.9-1.0%/yr population growth for absolute numbers, an unverified assumption). EU-27 FTE +3.8%/yr in 2013-2024 (1,476,139 to 2,224,215).
  - Multiplying UIS 1,486 per million by a world population of about 8.0 billion gives roughly 11.9M FTE researchers in 2023. This is my rough estimate, not an official UIS total.
- **Papers per researcher** can be computed as, e.g., NCSES world articles / (UIS world researchers per million × population), or Crossref journal articles / OECD+China FTE.
  - Mismatches: different coverage (researchers include business-sector R&D staff who rarely publish), FTE vs headcount, and 1-3 year reporting lags (OECD/UIS 2024 values are mostly missing in 2026).
  - Author-based denominators (unique active authors per year from OpenAlex, Scopus or Dimensions) align better with output. Computing them needs the bulk OpenAlex snapshot or licensed data, and they inherit author-disambiguation changes (e.g., OpenAlex's 2026 author splits and merges in the release notes).
- **SED:** a long, consistent census (US only) back to 1958, useful as a long-run supply indicator.

### Gaps
- I did not verify OECD MSTI's release calendar (OECD webpages returned 403) or a direct UIS indicator for the absolute world researcher headcount/FTE.
- I could not verify the 2024 Ioannidis-Collins-Baas update on extreme publishing behaviour (2000-2022) or any official "active authors per year" statistic from OpenAlex or Scopus.
- SED historical totals (Table 1-1) were not extracted.

## 8. Long-run growth baselines for scientific output (pre-AI)

### Takeaway
Published long-run baselines cluster at **about 3-5% per year for publications** (doubling every 14-24 years), with higher estimates from cited-reference methods:
- Price: doubling every 10-15 years (4.7-7.2%/yr).
- Bornmann & Mutz 2015: 2.96%/yr for WoS publications in 1980-2012 (doubling 23.7 years). Cited-reference phases of <1%, 2-3% and 8-9%.
- Bornmann, Haunschild & Mutz 2021: 4.10%/yr (doubling 17.3 years) across WoS, Scopus, Dimensions and Microsoft Academic.

Recent database-specific growth was faster:
- Scopus∩WoS: +47% in 2016-2022 (Hanson et al.; stated as about 5.6%/yr).
- NCSES/Scopus: about 4.4-4.7%/yr in 2012-2023.
- Crossref journal articles: about 7%/yr in 2010-2019.

### Cited Findings
- Price showed science "is growing exponentially … and doubles in size every 10 to 15 years", based on the SCI 1961 references and the Philosophical Transactions — as summarized in [Bornmann & Mutz 2015, arXiv:1402.4578](https://arxiv.org/abs/1402.4578) (full text PDF)
- **Bornmann & Mutz 2015** (JASIST 66:2215-2222, doi:10.1002/asi.23329):
  - Abstract: three growth phases "from less than 1% up to the middle of the 18th century, to 2 to 3% up to the period between the two world wars, and 8 to 9% to 2010" — [Crossref record](https://api.crossref.org/works/10.1002/asi.23329)
  - Full text: WoS publications 1980-2012 (38,508,986 publications) fit an exponential with a growth rate of **2.96%** and a doubling time of **23.7 years** (Table 1).
  - Cited-reference segmented regression: 0.45% (to about 1753), 2.35% (to about 1926), **8.13%** (to about 2000; doubling 8.9 years), then a negative segment attributed to database characteristics (Table 2).
  - [Bornmann & Mutz 2015 PDF](https://arxiv.org/pdf/1402.4578)
- **Bornmann, Haunschild & Mutz 2021** (Humanities & Social Sciences Communications 8:224, doi:10.1057/s41599-021-00903-w): using Dimensions, Microsoft Academic, WoS and Scopus, "the overall growth rate amounts to 4.10% with a doubling time of 17.3 years". Models with four or five segments fit best, and the segments are linked to industrialization and WWII — [Crossref record with abstract](https://api.crossref.org/works/10.1057/s41599-021-00903-w)
- **Hanson, Barreiro, Crosetto & Brockington 2024** (QSS 5(4):823-843, doi:10.1162/qss_a_00327):
  - Scopus∩WoS (via SCImago "only WoS journals"): "in 2022 the article total was ∼47% higher than in 2016", "~897k more indexed articles per year in 2022 (~2.82m articles) compared to 2016 (~1.92m articles) … a year-on-year exponential growth of ~5.6%".
  - MDPI, Elsevier, Frontiers, Springer and Wiley contributed more than 70% of the increase. MDPI alone contributed about 27%, with 88% special-issue articles and 37-day turnaround in 2022.
  - Data availability: "we were legally advised not to release our data and scripts publicly". A Shiny app and figshare figures are provided instead.
  - [Crossref record](https://api.crossref.org/works/10.1162/qss_a_00327); [arXiv PDF](https://arxiv.org/pdf/2309.15884); [Strain explorer app](https://pagoba.shinyapps.io/strain_explorer/)
- **NCSES (Scopus-based, filtered):** 2012-2022 +59%. World totals: 1,222,350 (2003), 2,129,076 (2013), 3,275,079 (2023) — [NCSES nsb202333](https://ncses.nsf.gov/pubs/nsb202333); [NCSES nsb20257 chapter](https://ncses.nsf.gov/pubs/nsb20257/publication-output-by-geography-and-scientific-field)

### Inferences
- **Recommended pre-AI baseline bands (my synthesis):**
  - Long-run (century scale): 3-4% per year for publications (BHM 2021 4.1%; B&M 2015 publications 2.96%).
  - Recent decade before ChatGPT:
    - Curated databases: 4-6%/yr (NCSES 4.4% for 2013-2023; Scopus∩WoS 2016-2022 endpoint CAGR 6.6%, 5.6% as stated by Hanson et al.).
    - PubMed: 3.0-4.7%/yr ([dp] 2010-2019 4.65%, 2015-2019 3.05%).
    - Crossref journal articles: about 7%/yr (2010-2019).
  - Hanson's endpoint numbers (1.92M to 2.82M) imply a 6.6%/yr compound rate, so their "~5.6%" presumably comes from a fitted model, not endpoints (my calc; discrepancy flagged).
- **Testing for an AI effect:** a post-2022 AI effect should be tested as a deviation from each database's own 2010-2019 (or 2015-2019) trend.
  - Exclude 2020-2021, which carry a COVID-19 surge of about +10-16% (PubMed [dp] 2020 +15.7%).
  - Control for publisher-specific shocks: the 2023 retrenchment of special-issue publishers, Hindawi's closure, WoS delistings.
  - The 2024-2025 acceleration (Crossref +8.3% and +9.3%; PubMed [edat] +3.1% and +9.9%) exceeds the 2015-2019 baselines. But this period also contains the Walden, OpenAlex and indexing changes listed above, so causal attribution is not established.
- **Workload ratio:** with researcher FTE growing about 3.4%/yr and curated output about 4.4-6.6%/yr, papers per researcher rose roughly 1-3%/yr before 2022 (my calc).

### Gaps
- I did not access Price's original texts (Little Science, Big Science 1963; Networks of Scientific Papers 1965) and cite his estimate via Bornmann & Mutz.
- I did not extract Bornmann, Haunschild & Mutz 2021's segment-specific rates and breakpoint years (the full text was blocked by a login redirect).
- I found no published, peer-reviewed estimate of a post-2022 break in total article output attributable to generative AI. That is the other researcher's scope and was not searched here.

## 9. How much do the databases disagree? (levels and trends)

### Takeaway
Levels differ by a factor of about 2-3 between curated indexes (Scopus, WoS) and inclusive ones (Crossref, Dimensions, OpenAlex, formerly Microsoft Academic). Trends also differ: Crossref grows about 2-3 percentage points per year faster than PubMed or NCSES-Scopus and shows no 2023 dip. Peer-reviewed comparisons confirm large level gaps and recommend filters. For AI-impact analysis, effects should be estimated on several sources and on fixed journal panels.

### Cited Findings
- **Visser, van Eck & Waltman 2021** (QSS 2(1):20-41, doi:10.1162/qss_a_00112), documents 2008-2017 — [Visser et al. arXiv PDF](https://arxiv.org/pdf/2005.10732v2); [Crossref record](https://api.crossref.org/works/10.1162/qss_a_00112):
  - Totals: Scopus 27M; CWTS WoS 23M (excluding ESCI and BkCI); Dimensions 36M; Crossref 35M; Microsoft Academic 73M.
  - Overlap with Scopus: about 18M (WoS), 21M (Dimensions), 21M (Crossref), 22M (Microsoft Academic).
  - Microsoft Academic's count is "substantially smaller in 2017 … We do not know why", an example of an unexplained recent-year dip in a database.
- **Martín-Martín et al. 2021** (Scientometrics 126:871-906), covering 3,073,351 citations to 2,515 highly cited 2006 documents: Google Scholar found 88% of all citations, Microsoft Academic 60%, Dimensions 54%, and COCI 28% (the smallest) — [arXiv:2004.14329](https://arxiv.org/abs/2004.14329)
- **Alperin et al. 2024:** "OpenAlex is a superset of Scopus", reliable "particularly at the country level", with metadata accuracy and completeness issues — [arXiv:2404.17663](https://arxiv.org/abs/2404.17663)
- **Culbert et al. 2025** (Scientometrics, doi:10.1007/s11192-025-05293-3): a cleaned set of 16.8M recent publications shared by OpenAlex, WoS and Scopus. OpenAlex has comparable reference counts, more ORCIDs and fewer abstracts — [arXiv:2401.16359](https://arxiv.org/abs/2401.16359)
- **Same-source version drift:** OpenAlex pre- vs post-Walden articles and reviews for 2018-2024 differ by +1.05% overall and +3.20% for 2024 — [Haupka 2026](https://rogue-scholar.org/records/nj8nj-9f827)
- **Cross-source annual counts assembled here** (live queries 2026-10-15 plus NCSES) [VERIFIED-QUERY / PRIMARY-DOC] — [PubMed esearch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=2024%5Bedat%5D); [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PUB_YEAR:2024%20AND%20SRC:MED&format=json&pageSize=1); [Crossref](https://api.crossref.org/works?rows=0&filter=type:journal-article&facet=published:*); [NCSES](https://ncses.nsf.gov/pubs/nsb20257/publication-output-by-geography-and-scientific-field):

| Year | PubMed [dp] | PubMed [edat] | Europe PMC MED (PUB_YEAR) | Crossref journal-article (published) | NCSES Scopus S&E articles |
|---|---|---|---|---|---|
| 2019 | 1,418,988 | 1,243,065 | 1,230,877 | 4,434,415 | n/a here |
| 2022 | 1,783,568 | 1,540,382 | 1,576,925 | 5,463,177 | ≈3.3M (2024 ed.) |
| 2023 | 1,697,549 | 1,499,881 | 1,498,048 | 5,615,836 | 3,275,079 |
| 2024 | 1,739,997 | 1,546,982 | 1,538,581 | 6,082,385 | not yet published |
| 2025 | 1,882,044 | 1,700,143 | 1,676,899 | 6,648,216 | not yet published |

### Inferences
- **Year-on-year changes (my calcs):**

| Period | PubMed [dp] | PubMed [edat] | Europe PMC MED | Crossref journal-article |
|---|---|---|---|---|
| 2022 to 2023 | -4.8% | -2.6% | -5.0% | +2.8% |
| 2023 to 2024 | +2.5% | +3.1% | +2.7% | +8.3% |
| 2024 to 2025 | +8.2% | +9.9% | +9.0% | +9.3% |

- The **sign of the 2023 change differs by source**. That alone shows that conclusions about "AI-era" output depend on the database.
- **Level ratios:** Crossref journal articles divided by NCSES-Scopus is about 1.7 (2023). Inclusive sources keep adding venues (new Crossref members, repositories in OpenAlex), so their trend includes coverage growth.
- **Recommended design for the end use:**
  - Report at least three series: PubMed/Europe PMC MEDLINE (curated, biomedical); Crossref or OpenAlex journal articles on a fixed pre-2022 venue panel (inclusive, all fields); and NCSES/Scopus (curated, all fields; lagged).
  - Pin data versions (OpenAlex snapshot date; Crossref public data file year; PubMed baseline year).
  - Treat 2020-2021 (COVID-19), 2023 (special-issue retrenchment and delistings) and the latest 12 months (lag) as known confounders.

### Gaps
- No peer-reviewed comparison was found (within this session's search budget) that directly compares annual totals and growth rates across PubMed, Crossref, OpenAlex, Scopus and WoS for 2019-2025. The table above is my own assembly and should be presented as such.
- Visser et al.'s year-by-year figures (their Figure 2) were not extracted numerically.
