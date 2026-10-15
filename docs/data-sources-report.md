# Academia's yardsticks bend where LLMs press hardest

**Bottom line:** arXiv, bioRxiv and PubMed can anchor part of this study. They do not cover academia as a whole, though, and none is a stable count of papers written.

**Coverage.** These three sources cover physics, mathematics, computing and the life sciences. They miss the social sciences and humanities (SSH), law and education, where books, national journals and non-English outlets carry much of the output ([Engels et al.](https://doi.org/10.1108/AJIM-05-2018-0127)). Even Web of Science and Scopus favour the natural sciences, engineering and biomedicine, and over-represent English-language journals ([Mongeon & Paul-Hus](https://doi.org/10.1007/s11192-015-1765-5)). Outside economics, SSH preprint servers are small, though growing fast.

**Stability.** Even within their own fields, the three sources are unstable:

- arXiv's headline total is mostly computer science: **46% of 2025 submissions** ([arXiv 2025 Annual Report](https://info.arxiv.org/about/reports/2025_arXiv_annual_report.pdf)).
- Each source counts a filtered population: papers that passed moderation, screened preprints, or indexed records whose 2024 total shifts by **12%** depending on the date field used.
- Each breaks during the period when LLMs spread, including **five arXiv rule changes within a year**.

**What to add.**

- *Papers written:* this needs submission data. Only Elsevier publishes a usable series: **almost 2.7 million submissions in 2022, more than 4.2 million in 2025**.
- *Papers published:* this needs indexes that cover all disciplines, counted over a fixed set of journals: Crossref, a pinned OpenAlex snapshot and NCSES/Scopus. OpenAlex's national and regional journal lists are the main free route into non-English scholarship.

**Grants and scholarships.**

- Grant data are richer and can be split by discipline. NIH alone counts unique applicants (since FY1998).
- UKRI's council series show **social-science (ESRC) applications up 55% in 2024-25, while arts-and-humanities (AHRC) applications fell 10%**.
- ERC applications in the social sciences and humanities grew **32%** in the 2026 Starting Grant call, against 19% in the physical sciences and 16% in the life sciences ([ERC](https://erc.europa.eu/news-events/news/starting-grants-2026-applications-facts-and-figures)).
- Across twelve funders, applications rose by a **median 46%** from 2022 to 2025. Every series overlaps shocks that have nothing to do with LLMs.
- Scholarship applicant counts survive mainly as press releases.

**The social sciences and humanities are not a low-exposure zone.**

- On output and submission measures, SSH effects match or exceed STEM's:
  - On SSRN, the main social-science preprint server, LLM adopters raised their output by **about 60%** compared with similar non-adopters ([Kusumegi et al.](https://arxiv.org/pdf/2601.13187)).
  - *Organization Science* reports submissions **up 42%** since ChatGPT ([Gartenberg et al.](https://doi.org/10.1287/orsc.2026.ed.v37.n3)).
  - About **24% of sentences** in late-2025 sociology abstracts were LLM-modified ([Cao](https://doi.org/10.1177/23780231261460657)).
- On counts of tell-tale "LLM words", growth is smaller in SSH than in STEM ([Kousha & Thelwall](https://doi.org/10.1007/s11192-026-05601-5)). The measure chosen decides how exposed SSH looks.
- US humanities funding is a policy shock in its own right. In 2025 the National Endowment for the Humanities (NEH) terminated about 1,477 grants and cut about 70% of its staff ([NEH](https://www.neh.gov/sites/default/files/NEH%20FY2025%20PAR%20to%20OMB.pdf)).

**How to separate the LLM effect.** Three steps:

1. Measure LLM use directly in text. At least **13.5% of 2024 PubMed abstracts** show LLM processing (a lower bound).
2. Link that measured use (the "dose") to volume across disciplines, countries and people.
3. Exploit dated policy changes, such as NIH's cap of six applications per investigator.

## Seven working assumptions the evidence contradicts

Using long, free, machine-readable series is the right instinct. The problems lie in what those series count, which disciplines they cover and when they break. Each assumption below fails in a specific way with a specific fix, and the sections that follow develop the fixes.

| Working assumption | What the evidence shows | Fix |
|---|---|---|
| arXiv, bioRxiv and PubMed are stable yardsticks | arXiv changed its submission rules five times in one year ([arXiv](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/)). bioRxiv grew 23-fold in 2014–2018 and changed its DOI prefix on 1 Dec 2025 ([bioRxiv API](https://api.biorxiv.org/sum/m); [openRxiv](https://connect.biorxiv.org/news/2025/11/18/preprint_dois)). PubMed's MEDLINE share fell from 91% to 64% between 2000 and 2024 ([E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=2024%5Bdp%5D+AND+medline%5Bsb%5D)) | Fixed counting rules, a marker for each dated break, and analysis windows that end before the breaks |
| These three sources represent academia | They cover physics, mathematics, computing and the life sciences, and arXiv itself is 46% computer science ([arXiv 2025 report](https://info.arxiv.org/about/reports/2025_arXiv_annual_report.pdf)). Outside economics, social-science preprint servers are small: in 2023 PsyArXiv posted 7,089 papers and SocArXiv 2,398, against 39,155 on bioRxiv ([Crossref prefix queries](https://api.crossref.org/prefixes/10.2139/works?filter=type:posted-content&rows=0&facet=published:%2A); [bioRxiv API](https://api.biorxiv.org/sum/m)). Preprints were still only about 4% of research articles in 2021 ([Xie, Shen & Wang](https://arxiv.org/abs/2102.09066)). Web of Science and Scopus themselves under-cover SSH and non-English journals ([Mongeon & Paul-Hus](https://doi.org/10.1007/s11192-015-1765-5)) | Add all-discipline indexes, SSH-specific sources and discipline splits; count arXiv by primary subject archive |
| These counts measure papers written | They count moderated postings and indexed records. arXiv publishes no statistics on submissions its moderators reject | Use submission totals for "written" and fixed-panel indexes for "published" |
| Application counts show how many people apply | Among funders, only NIH publishes unique applicants. Among admissions sources, only LSAC (US law schools) does ([NIH](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=164); [LSAC](https://www.lsac.org/podcast/keeping-data-september-2026)) | Split growth into number of people and applications per person wherever possible |
| Long scholarship series exist | Fellowship applicant numbers are mostly one-off press-release figures | Compile the releases; anchor on CGS/ETS (since 1986) and LSAC |
| LLM exposure starts on 30 Nov 2022 | Researchers' AI use kept climbing between 2024 and 2025: from 37% to 58% (Elsevier survey) and from 45% to 62% (Wiley survey) ([Elsevier](https://www.elsevier.com/about/press-releases/elseviers-global-survey-of-3-000-researchers-reveals-less-than-half-have); [Wiley](https://newsroom.wiley.com/press-releases/press-release-details/2025/AI-Adoption-Jumps-to-84-Among-Researchers-as-Expectations-Undergo-Significant-Reality-Check/default.aspx)) | Model gradual uptake and intensity of use, test several possible start dates, and check fake "placebo" dates where no effect should appear |
| Post-2022 growth is mostly LLM-driven | Funders' own notes cite rule changes, restructuring and budget shocks ([RoRI data](https://media.nature.com/original/magazine-assets/d41586-026-01297-y/52331462)) | Comparison groups, plus policy changes that act as natural experiments |

## PubMed, bioRxiv and arXiv cover STEM and biomedicine, and even there need repairs

All three are free, machine-readable and long enough for trend analysis. Between them they cover the natural sciences, mathematics, computing and biomedicine, with only a thin slice of economics. Within those fields, each counts a filtered population and breaks during the LLM period, so how you correct each source matters more than which one you pick.

### PubMed: the date field alone moves the 2024 total by 12 percent

PubMed is a biomedical index. Its MEDLINE core covers more than 5,200 journals in about 40 languages ([NLM MEDLINE overview](https://www.nlm.nih.gov/medline/medline_overview.html)). It speaks for medicine and the life sciences, not for academia at large.

It also counts bibliographic records, not research articles. Its **41.3 million records** (on 15 October 2026) include ([E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=all%5Bsb%5D)):

- citations indexed for MEDLINE
- records still in process or supplied by publishers
- records outside MEDLINE ("PubMed-not-MEDLINE")
- deposits found only in PubMed Central (PMC)
- since 2023, preprints funded by NIH

**The counting rule drives the answer.** The publication-date field [dp] counts an item under both its electronic and its print date when they fall in different years. So 2024 has **1,739,997 records by [dp] but 1,546,982 by entry date [edat]**. NLM itself documents this double counting ([PubMed User Guide](https://pubmed.ncbi.nlm.nih.gov/help/); [NLM citation counts](https://www.nlm.nih.gov/bsd/medline_cit_counts_yr_pub.html)).

**What PubMed contains has drifted:**

- **PubMed-not-MEDLINE records rose from 6.5% of the total in 2000 to 32.8% in 2024**, driven by deposits from journals outside MEDLINE that comply with funder open-access rules ([E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=2024%5Bdp%5D+AND+pubmednotmedline%5Bsb%5D)).
- NIH's Preprint Pilot lifted preprint records from **822 in 2022 to 13,200 in 2023** ([NCBI Insights](https://ncbiinsights.ncbi.nlm.nih.gov/2023/01/09/next-phase-preprint-pilot/)).

**Subject classification changed method in exactly the period of interest.** Field shares based on MeSH subject headings are affected:

- All MEDLINE journals had moved to automated indexing by April 2022.
- A neural indexer (MTIX) replaced that system in 2024.
- Records indexed only by humans fell from 662,507 (2019) to 7,492 (2023).

([NLM indexing FAQ](https://www.nlm.nih.gov/bsd/indexfaq.html); [NLM Technical Bulletin](https://www.nlm.nih.gov/pubs/techbull/ma24/ma24_mtix.html))

**The most recent months are provisional.** Records still at the publisher-supplied stage reached 47,593 in the September 2026 entry month, because MEDLINE processing is lagging. NLM also no longer maintains its production statistics page ([E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=2026%2F09%5Bedat%5D+AND+publisher%5Bsb%5D); [NLM](https://www.nlm.nih.gov/bsd/medline_pubmed_production_stats.html)).

**The repair:**

1. Count by entry date, or use Europe PMC's single publication year (PUB_YEAR) for MEDLINE-sourced records. That gives 1,538,581 for 2024, within 0.6% of the entry-date count ([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PUB_YEAR:2024%20AND%20SRC:MED&format=json&pageSize=1)).
2. Exclude preprints.
3. Report MEDLINE and non-MEDLINE journals separately, using a fixed set of journals that were already indexed before 2022.
4. Avoid MeSH field shares across 2019–2024.
5. Pin the annual baseline file so results can be reproduced ([PubMed baseline](https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/)).

### bioRxiv and medRxiv: usable only after their early adoption phase

These two servers cover biology (bioRxiv) and the health sciences (medRxiv) only.

**Access.** bioRxiv's summary endpoint needs no key and returns monthly new and revised papers from November 2013. medRxiv's details endpoint gives monthly counts of new papers from June 2019. Both can be filtered by subject category, record the corresponding author's institution, and link preprints to the journal articles they later became ([bioRxiv /sum/m](https://api.biorxiv.org/sum/m); [API documentation](https://api.biorxiv.org/)).

**Coverage** is near-complete. Europe PMC indexes 39,130 bioRxiv preprints for 2023, against 39,155 in the API ([Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=SRC:PPR%20AND%20PUBLISHER:%22bioRxiv%22%20AND%20FIRST_PDATE:%5B2023-01-01%20TO%202023-12-31%5D&format=json&pageSize=1&resultType=idlist)).

**The shape of the series is the trouble.** bioRxiv's path:

- It grew **23-fold from 2014 to 2018** (886 to 20,778 new papers) as researchers adopted it.
- It peaked with COVID in 2020 (38,717).
- It fell in 2021–22.
- It then re-accelerated by **9.5%, 11.4% and 13.0%** in 2023–2025, reaching a record 5,049 papers in September 2026.

medRxiv has only 3.4 years of history before ChatGPT, dominated by COVID ([bioRxiv /sum/m](https://api.biorxiv.org/sum/m); [medRxiv details](https://api.biorxiv.org/details/medrxiv/2025-11-01/2025-11-30/0)).

**Two late-2025 events break derived counts:**

- All papers posted from **1 December 2025 carry DOI prefix 10.64898**, so Crossref counts that use the old 10.1101 prefix collapse ([openRxiv](https://connect.biorxiv.org/news/2025/11/18/preprint_dois)).
- bioRxiv started an opt-in AI review pilot with q.e.d Science on 4 November 2025 ([bioRxiv news](https://connect.biorxiv.org/news/2025/11/04/qed_review_tool)).

**What the counts miss.** Submissions rejected at screening are not published. Links from preprints to journal articles undercount: in one manual check, 37.5% of supposedly unpublished bioRxiv preprints had in fact appeared in journals ([Abdill & Blekhman, eLife](https://elifesciences.org/articles/45133)).

**The repair:**

- Use the API's counts of new papers, never counts by DOI prefix.
- Treat 2019–2022 as the period before LLMs, with an adjustment for COVID.
- Read the share of preprints that reach journals as a lower bound. Recent preprints have not yet had time to be published.

### arXiv: the longest monthly series, and mostly a computer-science one

**What it counts.** arXiv's official CSV counts the new identifiers issued each month since July 1991. That means papers announced after moderation:

- each paper is counted once, whatever other categories it is also listed under (cross-lists)
- revised versions and 2,431 papers migrated from older systems are excluded
- 156 papers deleted later are still included

([arXiv statistics](https://arxiv.org/stats/monthly_submissions); [CSV](https://arxiv.org/stats/get_monthly_submissions))

**Access.** Metadata are free through the API, OAI-PMH (arXiv's preferred bulk route) and a CC0 Kaggle snapshot of about 5.6 GB, updated on 10 October 2026 ([arXiv bulk data](https://info.arxiv.org/help/bulk_data.html); [Kaggle](https://www.kaggle.com/datasets/Cornell-University/arxiv)).

**Disciplines.** arXiv covers physics, mathematics, computer science, statistics, quantitative biology, quantitative finance, economics and electrical engineering. It does not cover the humanities, law or education.

**The total is not a general-academia series:**

- **Computer science accounted for 46% of 2025 submissions**, physics 30% and mathematics 15%.
- cs.AI, the artificial-intelligence category, grew more than sixfold in two years.
- arXiv's own annual report names as drivers of its workload: "LLM and AI as research topics", "marginal and below the bar AI-generated content", and more submissions from students.

([arXiv 2025 Annual Report](https://info.arxiv.org/about/reports/2025_arXiv_annual_report.pdf); [arXiv blog](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/))

The headline series grew **2.2% in 2022, then 12.3%, 17.0% and 16.6% in 2023–2025**, and 30% in January–September 2026. That acceleration mixes AI as a research topic with LLMs as a writing tool ([CSV](https://arxiv.org/stats/get_monthly_submissions)).

**Repair: split by primary archive.**

- For fields beyond computing, count each new paper's first version by its **primary** archive, using OAI-PMH or Kaggle metadata. Use these archives:
  - the physics group (including astro-ph, cond-mat, hep and quant-ph)
  - math, q-bio, q-fin, stat, econ and eess
- Do not use API category queries for this, because they also match cross-lists ([arXiv API example](https://export.arxiv.org/api/query?search_query=cat:cs.CL%20AND%20submittedDate:%5B202211010000%20TO%20202211302359%5D&max_results=1)).
- Treat three groups separately as high-exposure strata:
  - stat.ML (statistical machine learning)
  - the electrical-engineering (eess) categories heavy in machine learning
  - every paper cross-listed to cs

Why separate them: Liang et al. estimate that by September 2024, **18.0% of sentences in electrical engineering and systems science abstracts** were LLM-modified ([Liang et al., Nature Human Behaviour](https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf)). That is close to computer science's 22.5% and far above mathematics' 7.7%. These figures also show that the archives outside computer science received a lower dose, not none, so they cannot serve as fully untreated controls. Only econ and q-fin reach into the social sciences.

The per-archive monthly series has not been built yet. The method is verified, but the counts are not in hand.

**Rule changes.** Four apply to every archive:

- a limit of three active submissions per person (since 2024)
- stricter endorsement of new authors (10 December 2025 for mathematics, 21 January 2026 for all archives)
- a requirement for a full English version of each paper (11 February 2026)
- a limit of two submissions per person per month (1 October 2026)

Two others target computer science only:

- a rule restricting review and position papers (31 October 2025)
- a one-year ban for submitting unchecked LLM output (May 2026, reported in the press)

([arXiv rate-limit post](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/); [arXiv endorsement](https://blog.arxiv.org/2026/01/21/attention-authors-updated-endorsement-policy/); [arXiv English policy](https://blog.arxiv.org/2026/01/13/non-english-paper-submission-guidelines/); [arXiv CS review rule](https://blog.arxiv.org/2025/10/31/attention-authors-updated-practice-for-review-articles-and-position-papers-in-arxiv-cs-category/); [404 Media](https://www.404media.co/new-arxiv-rules-ai-generated-papers-ban/))

Rejected submissions never receive identifiers, so stricter moderation lowers the measured count. For archives outside computer science, the clean window runs from **January 2000 to November 2025**.

| | PubMed | bioRxiv and medRxiv | arXiv |
|---|---|---|---|
| What it counts | Indexed records: MEDLINE, PubMed-not-MEDLINE, PMC-only deposits, NIH-funded preprints | Preprints posted after screening: new papers and revisions | New papers announced after moderation, one per identifier; revisions excluded |
| Disciplines covered | Biomedicine and life sciences (MEDLINE: 5,200+ journals, about 40 languages) | Biology (bioRxiv); health sciences (medRxiv) | Physics, mathematics, computer science, statistics, quantitative biology and finance, economics, electrical engineering |
| Disciplines missed | Most social sciences, humanities, law and education | Everything outside the life and health sciences | Humanities, law, education; little social science beyond economics |
| Coverage and granularity | Records from before 1947, MEDLINE from 1966; day-level entry date; journal, publication type, language, MeSH | bioRxiv from Nov 2013, medRxiv from Jun 2019; day-level; subject category, corresponding institution, link to journal version | Monthly from Jul 1991; first-version timestamps; primary and cross-list categories; authors |
| Access and cost | Free E-utilities API (about 3 requests a second without a key); annual baseline XML plus daily updates; Europe PMC REST | Free REST API, no key needed | Free CSV, API and OAI-PMH; Kaggle snapshot (CC0, about 5.6 GB) |
| Breaks during the LLM period | Date-field double counting (+12% in 2024); not-MEDLINE share 6.5%→32.8%; automated MeSH (2020–22) and MTIX (2024); preprints from 2023; processing backlog in 2025–26 | DOI prefix 10.64898 from 1 Dec 2025; AI review pilot from Nov 2025; COVID surge and 2021–22 decline in the baseline | All archives: endorsement (Dec 2025–Jan 2026), English version (11 Feb 2026), rate limit (1 Oct 2026). Computer science only: review rule (31 Oct 2025), one-year ban (May 2026) |
| Verdict | Main biomedical "published" series: count by entry date or Europe PMC PUB_YEAR, on a fixed set of journals, excluding preprints | Secondary life-science "posted" series; use 2019–2022 as the pre-LLM period | Main long monthly series once split by primary archive; clean window outside computer science Jan 2000–Nov 2025 |

## All-discipline indexes and publisher submissions fill the gap between written and published

### Every index under-covers books, national journals and non-English work

Counts across all of academia start from a structural bias. Bibliographic databases were built around English-language journal articles. They therefore under-represent the monographs, edited volumes and national-language journals that carry much of the humanities and social sciences. Preprinting, meanwhile, is concentrated in physics, computing, biology and economics.

The evidence in hand shows the bias at every layer:

- **NCSES** counts only journal articles and conference papers with English titles and abstracts, so books are excluded by design ([NCSES](https://ncses.nsf.gov/pubs/nsb20257/publication-output-by-geography-and-scientific-field)).
- **Web of Science:** the version used in the standard comparison of databases (maintained by CWTS, the Leiden bibliometrics centre) left out the Book Citation Index ([Visser et al.](https://arxiv.org/abs/2005.10732)).
- **PubMed** is biomedical by design.
- **Web of Science and Scopus** (13,605 and 20,346 active journals, against 63,013 in the Ulrich's periodicals directory) favour the natural sciences, engineering and biomedicine over SSH, and over-represent English-language journals ([Mongeon & Paul-Hus](https://doi.org/10.1007/s11192-015-1765-5)).
- **OpenAlex** covers languages far more evenly than Web of Science, but its language labels are often wrong, which overstates English ([Céspedes et al.](https://doi.org/10.1002/asi.24979)).
- **Books still matter in SSH.** National databases that record every SSH output show that "book publishing is not disappearing", with shares that vary by field and country ([Engels et al.](https://doi.org/10.1108/AJIM-05-2018-0127); [Kulczycki et al.](https://doi.org/10.1007/s11192-018-2711-0)).
- **LLM-use studies:** most estimates come from PubMed, arXiv, bioRxiv, medRxiv, SSRN or the Nature group of journals. Estimates specific to SSH (economics journals, sociology abstracts) appeared only in 2025–26.

Several free routes partly correct the bias, each with its own catch:

- **Crossref** gives yearly counts of books, monographs, edited books and chapters (24.9 million chapter records), but no discipline labels. On 13 March 2024 it announced it would remove its subject codes, which it called "not complete or reliable from the start", so any pipeline that split Crossref counts by subject broke in 2024 ([Crossref blog](https://www.crossref.org/blog/subject-codes-incomplete-and-unreliable-have-got-to-go/)). Some swings are artefacts of how publishers register records, such as the 2023 peak in chapters ([Crossref book chapters](https://api.crossref.org/types/book-chapter/works?rows=0&facet=published:%2A)).
- **OpenAlex** has a new `listed_in` filter covering 61 journal lists, including SciELO, Latindex and national lists. This opens a way into regional and non-English journals ([OpenAlex trusted lists](https://blog.openalex.org/trusted-journal-lists-come-to-openalex/)). Its classification has no separate humanities domain: "Arts and Humanities" is a field inside the "Social Sciences" domain, alongside business, economics and psychology. Its free summary records hold only lifetime totals. Yearly counts by field therefore need either an API key (the free tier allows $1 of queries a day) or processing the roughly 615 GB of work records in the snapshot. The Arts and Humanities total grew 3.4-fold between the April 2024 and October 2026 versions, so pin one snapshot ([OpenAlex fields](https://openalex.s3.amazonaws.com/data/jsonl/fields/updated_date=2026-10-14/part_0000.gz)).
- **Dimensions** classifies each document, including books and chapters, into a standard field scheme (the Australian and New Zealand Fields of Research) ([Porter et al.](https://arxiv.org/abs/2209.00104)).
- **Scopus** classifies whole journals and book series (its ASJC scheme), often into several fields at once ([Elsevier](https://www.elsevier.support/scopus/answer/what-are-scopus-subject-area-categories-and-asjc-codes)).
- **National research-information systems** in Flanders, Finland, Norway, Poland and Slovenia record books and national-language work comprehensively ([Engels et al.](https://doi.org/10.1108/AJIM-05-2018-0127)).

Sources built specifically for the social sciences and humanities are collected in their own section below.

### Publication indexes disagree on levels, trends and even signs

**Crossref** is the broadest free counter across all disciplines. It holds 124.5 million journal-article records, returns a full annual series from one query, and counts **6.65 million articles dated 2025** ([Crossref facet](https://api.crossref.org/works?rows=0&filter=type:journal-article&facet=published:%2A)). It misses outlets that do not register DOIs. Its growth of about 7% a year in 2010–2019 is inflated in three ways:

- coverage expansion: 34,071 member organisations now register DOIs
- spikes at default dates (1970 and 2000)
- bulk registrations of particular record types, such as 1.46 million "component" records dated 2023

Registration dates are not publication dates ([Crossref members](https://api.crossref.org/members?rows=0); [Crossref 2023 type facet](https://api.crossref.org/works?rows=0&filter=from-pub-date:2023-01-01,until-pub-date:2023-12-31&facet=type-name:%2A)).

**OpenAlex** is the only free, all-discipline index whose full data can be downloaded under an open (CC0) licence. Since early 2026, however, its API charges against a daily budget:

- $0.10 a day per IP address without a key
- $1 a day with a free key
- annual plans from $5,000

Its free S3 snapshot is released quarterly and is about 770 GB in Parquet format ([OpenAlex pricing](https://help.openalex.org/access/pricing/); [OpenAlex costs](https://help.openalex.org/access/example-costs/); [OpenAlex snapshot](https://help.openalex.org/access/snapshot/)).

Its counts move between versions. The November 2025 rebuild (called "Walden") changed article counts as follows ([Haupka 2026](https://rogue-scholar.org/records/nj8nj-9f827)):

- 2018–2021: by less than 0.3%
- 2022–2023: up 1.7%
- 2024: up **3.2%**

On 6 October 2026, OpenAlex also re-assigned the topic of every work ([OpenAlex topics](https://blog.openalex.org/same-topics-better-assignments/)). The rebuild's drift falls in the years after ChatGPT, so comparing a pre-rebuild 2022 count with a post-rebuild 2024 count inflates any LLM effect. Pin one snapshot.

**NCSES's Science and Engineering Indicators** offer the best-documented curated world series:

- **3,275,079 articles and conference papers indexed in Scopus in 2023**
- each paper's credit split among its authors' countries ("fractional counting"), with predatory journals filtered out
- 4.4% growth a year since 2013
- science and engineering fields only, with a two-year lag

**Other indexes:**

- Scopus and Web of Science require subscriptions and drop journals from coverage.
- Dimensions grants free access for non-commercial research on research, on application.
- Semantic Scholar's weekly datasets are free to download.

([Scopus policy](https://www.elsevier.com/products/scopus/content/content-policy-and-selection); [Dimensions](https://www.dimensions.ai/scientometric-research/); [Semantic Scholar datasets](https://api.semanticscholar.org/datasets/v1/release/latest))

**The databases disagree even on direction.** From 2022 to 2023 (see the table below):

- Europe PMC's MEDLINE-sourced count fell 5.0%.
- PubMed's count by entry date fell 2.6%.
- Crossref journal articles rose 2.8%.

In 2025, all three rose 8–10%.

**Levels differ by design.** Crossref's 2023 journal-article count is 1.7 times the NCSES/Scopus figure. A comparison of 2008–2017 coverage found 23 million documents in Web of Science, 27 million in Scopus, 35 million in Crossref and 36 million in Dimensions ([Visser et al.](https://arxiv.org/abs/2005.10732)).

**The pre-LLM growth any effect must beat is modest:**

- **2.96% a year** in Web of Science for 1980–2012 ([Bornmann & Mutz](https://arxiv.org/abs/1402.4578))
- **4.10% a year** across four databases ([Bornmann, Haunschild & Mutz](https://api.crossref.org/works/10.1057/s41599-021-00903-w))
- a 47% rise in articles indexed by both Scopus and Web of Science from 2016 to 2022. MDPI, Elsevier, Frontiers, Springer and Wiley supplied over 70% of that increase ([Hanson et al.](https://arxiv.org/pdf/2309.15884)).

**Denominators are free:**

- OECD researcher full-time equivalents (FTEs) rose 3.4% a year in 2019–2023, from 5.57 million to 6.36 million ([OECD MSTI](https://sdmx.oecd.org/public/rest/data/OECD.STI.STP,DSD_MSTI@DF_MSTI,1.3/USA+OECD+CHN+DEU+JPN.......?startPeriod=2019)).
- UNESCO counts 1,141 researchers per million people worldwide in 2015 and 1,486 in 2023 ([UNESCO UIS](https://api.uis.unesco.org/api/public/data/indicators?indicator=RESDEN.INHAB.TFTE&geoUnit=SDG%3A%20World&start=2010&end=2024)).
- Eurostat counts 2.22 million researcher FTEs in the EU-27 (2024) ([Eurostat](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/rd_p_persocc?format=JSON&lang=EN&geo=EU27_2020&unit=FTE&sectperf=TOTAL&prof_pos=RSE&sex=T)).
- NSF's Survey of Earned Doctorates has counted US research doctorates since 1958: 59,015 in 2025 ([NCSES SED](https://ncses.nsf.gov/surveys/earned-doctorates)).

Output grew faster than the number of researchers before 2022, so papers per researcher were already rising about 1–3% a year before any LLM arrived.

| Series (disciplines) | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| [arXiv](https://arxiv.org/stats/get_monthly_submissions) new papers, all archives (46% computer science) | +1.9% | +2.2% | +12.3% | +17.0% | +16.6% |
| [bioRxiv](https://api.biorxiv.org/sum/m) new papers (life sciences) | −4.8% | −3.0% | +9.5% | +11.4% | +13.0% |
| [medRxiv](https://api.biorxiv.org/details/medrxiv/2025-11-01/2025-11-30/0) new papers (health sciences) | −9.5% | −17.4% | +4.9% | +16.5% | +16.8% |
| [PubMed](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=2024%5Bedat%5D) records by entry date (biomedicine) | +6.9% | −0.2% | −2.6% | +3.1% | +9.9% |
| [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PUB_YEAR:2024%20AND%20SRC:MED&format=json&pageSize=1) MEDLINE-sourced records by publication year (biomedicine) | +11.1% | +1.1% | −5.0% | +2.7% | +9.0% |
| [Crossref](https://api.crossref.org/works?rows=0&filter=type:journal-article&facet=published:%2A) journal articles (all disciplines with DOIs) | +7.9% | +3.5% | +2.8% | +8.3% | +9.3% |
| [Elsevier](https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2025-annual-report.pdf) submissions (Elsevier portfolio; rounded figures) | — | ≈+8% | ≈+11% | ≈+17% | ≈+20% |
| [NBER](https://data.nber.org/nber_paper_chapter_metadata/tsv/date.tsv) working papers (economics) | −23.5% | −9.2% | +0.5% | +9.3% | −1.4% |
| [SocArXiv](https://api.osf.io/v2/preprints/?filter%5Bprovider%5D=socarxiv&filter%5Bdate_created%5D%5Bgte%5D=2024-01-01&filter%5Bdate_created%5D%5Blt%5D=2025-01-01&page%5Bsize%5D=1) new papers, first versions only (social sciences) | +17.6% | −14.9% | +2.7% | −5.6% | +42.3% |
| [HAL](https://api.archives-ouvertes.fr/search/?q=%2A:%2A&rows=0&wt=json&fq=level0_domain_s:shs&fq=submitType_s:file&facet=true&facet.field=submittedDateY_i&facet.limit=200&facet.sort=index) full-text deposits, social sciences and humanities (France) | −9.7% | −10.4% | +26.1% | +4.2% | +2.0% |
| [ERIC](https://api.ies.ed.gov/eric/?search=publicationdateyear:2023%20AND%20peerreviewed:T&format=json&rows=0) peer-reviewed records (education; 2025 still incomplete) | +7.9% | −0.8% | −6.2% | +5.9% | −6.8% |
| [Crossref](https://api.crossref.org/types/monograph/works?rows=0&facet=published:%2A) monographs (books, all disciplines) | +11.1% | −0.1% | +10.5% | −7.4% | −1.0% |

*Year-on-year growth, computed from the counts at each linked source. SocArXiv counts before April 2025 include every record, because versions were not listed separately until then.*

### Only Elsevier publishes a usable submission series

No preprint server or index counts papers written. The nearest observable quantity is submissions, including the ones later rejected.

**Elsevier.** The annual reports of RELX, Elsevier's parent company, give the only verified publisher series covering several years ([RELX 2021](https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2021-annual-report.pdf); [RELX 2022](https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2022-annual-report.pdf); [RELX 2025](https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2025-annual-report.pdf)):

| Year | Submissions | Articles published |
|---|---|---|
| 2021 | 2.5 million | — |
| 2022 | almost 2.7 million | 600,000-plus |
| 2023 | almost 3 million | — |
| 2024 | more than 3.5 million | — |
| 2025 | more than 4.2 million | 795,000-plus |

Submission growth rose from roughly 8% to 20% a year. Articles published per submission fell from about 22% to about 19%. RELX credits growth in open access paid for by authors, not AI. It does not define a submission, so transfers between journals and resubmissions may be included.

**Frontiers** publishes ([Frontiers 2024](https://www.frontiersin.org/documents/frontiers-annual-report-2024.pdf); [Frontiers 2025](https://www.frontiersin.org/documents/annual-report-2025.pdf)):

- acceptance shares: 43% in 2024, 42% in 2025
- desk rejections: 65,544 in 2024
- the fact that its research-integrity team made more than half of all 2025 rejections before peer review

**Single journals.** The clearest example comes from the social sciences. The *Journal of Public Administration Research and Theory* (JPART) went from 45–50 submissions a month in autumn 2023 to 119 in April 2026. It attributed the rise "in large part" to generative AI and limited each author to three submissions a year from 1 July 2026 ([JPART policy](https://www.gopmra.org/assets/Secretariat/Policies/jpart-submission-cap-policy.pdf)).

No public dataset of manuscript submissions across publishers was found. Submissions also overstate papers written, because each rejected manuscript that is resubmitted elsewhere is counted again. The ratio of published to submitted papers measures how much the system processes, not the share of papers that eventually appear.

### Social-science preprint counts measure output only after cleaning

Outside physics and biology, preprint counts mostly track three things other than research output:

- how widely a platform is adopted
- links between servers and journal submission systems
- how DOIs are versioned

The servers that matter for the social sciences illustrate this:

- **SSRN** (economics, law and the social sciences): counted through Crossref, postings rose **14-fold between 2020 and 2025** (18,388 to 261,180), too fast to be organic growth ([Crossref SSRN prefix](https://api.crossref.org/prefixes/10.2139/works?filter=type:posted-content&rows=0&facet=published:%2A)).
- SSRN has no public API and blocks scripted access. Its own totals are year-end snapshots, such as 1.77 million full-text papers at the end of 2025 ([Harvard Law School Forum](https://corpgov.law.harvard.edu/2026/01/19/harvard-corporate-faculty-excels-in-ssrns-2025-citation-rankings/)).
- **PsyArXiv, SocArXiv and EdArXiv** (psychology, sociology, education): since April 2025 their host platform, OSF, lists every version of a paper as a separate record, which inflated raw 2025 counts ([PsyArXiv sample](https://api.crossref.org/prefixes/10.31234/works?filter=type:posted-content,from-posted-date:2025-06-01&rows=3)). Counting first versions only, through OSF's free API, still shows strong growth in 2025 ([OSF API](https://api.osf.io/v2/preprints/?filter%5Bprovider%5D=socarxiv&filter%5Bdate_created%5D%5Bgte%5D=2024-01-01&filter%5Bdate_created%5D%5Blt%5D=2025-01-01&page%5Bsize%5D=1)):
  - SocArXiv grew **42%** (2,170 to 3,088 new papers) and is accelerating in 2026.
  - PsyArXiv grew 30% (6,726 to 8,748) and is flat in 2026. Its raw record count, which includes later versions, rose 113%.
  - EdArXiv roughly doubled (280 to 569), and doubled again in 2026.
  - SocArXiv also changed its rules in November 2025 (see the SSH section).
- **NBER working papers** stayed flat at 1,191–1,308 a year from 2022 to 2025. That makes NBER a stable comparison series for economics, although its output is capped by its membership ([NBER metadata](https://data.nber.org/nber_paper_chapter_metadata/tsv/date.tsv)).

Servers spanning many disciplines show similar artefacts:

- Research Square's content is tied to journal submissions.
- Preprints.org rose 3.5-fold in 2023.
- The OSF family of servers switched to versioned DOIs.
- Zenodo "preprints" went from 5,289 (2023) to 134,329 (2025) ([DataCite Zenodo](https://api.datacite.org/dois?client-id=cern.zenodo&resource-type-id=preprint&query=publicationYear:2025&page%5Bsize%5D=1)).

ChemRxiv grew steadily, from 6,029 papers (2022) to 10,085 (2025).

Any Crossref count must strip version suffixes (_vN, /vN, .vN) first so each preprint is counted once.

### Machine-learning conferences serve only as a high-exposure benchmark

Machine-learning conferences sit outside this study. They are useful only as a benchmark of what happens when AI is both the research topic and the writing tool:

- NeurIPS submissions rose from 10,411 in 2022 to 30,709 in 2026.
- ICLR's grew 5.8-fold.
- IJCAI's grew 15%.

([cs-conf-stats](https://github.com/Xovee/cs-conf-stats))

Conferences responded by capping submissions per author: 25 at CVPR and 20 at ICLR 2027 ([ICLR 2027 guidelines](https://iclr.cc/Conferences/2027/AuthorGuidelines); [CVPR 2026 guidelines](https://cvpr.thecvf.com/Conferences/2026/AuthorGuidelines)).

Their published submission funnels are a model for the data on attempted submissions that journals do not release. ICLR 2026 reported 19,525 valid submissions, 779 desk rejections, 5,042 withdrawals and 5,355 acceptances ([ICLR retrospective](https://blog.iclr.cc/2026/03/31/a-retrospective-on-the)).

| Source | Disciplines (and gaps) | What it counts; coverage | Access and cost | Breaks and caveats |
|---|---|---|---|---|
| [Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=SRC:MED&format=json&pageSize=1) | Biomedicine and life sciences; preprints mostly life sciences | PubMed records with a single publication year; preprints in volume from 2019 | Free REST API, one count per query | Unfiltered totals include 4.2M patents; Research Square is about 45% of preprints; indexing lags of months |
| [Crossref](https://www.crossref.org/documentation/retrieve-metadata/bulk-downloads/) | All disciplines that register DOIs; includes 24.9M book chapters and 1.1M dissertations; misses outlets without DOIs | Works by type (124.5M journal articles), from the early 1900s, by day | Free API (5 requests a second, or 10 if you identify yourself); annual file of about 200 GB, free by torrent or about US$18 via Amazon S3; Metadata Plus is a paid tier | Growth in members inflates trends; default dates; bulk registrations of some record types; registration date ≠ publication date |
| [OpenAlex](https://help.openalex.org/access/snapshot/) | All disciplines, including repositories; national and regional journal lists via `listed_in` | Works, authors, institutions, topics (about 327M core works), all years, by day | Open (CC0). API charged against a daily budget since early 2026 ($1 a day with a free key); free quarterly snapshot (about 770 GB in Parquet) | Walden rebuild (Nov 2025); topics re-assigned (Oct 2026); recent years keep filling in for months; pin a snapshot |
| [NCSES Indicators](https://ncses.nsf.gov/pubs/nsb20257/publication-output-by-geography-and-scientific-field) | Science and engineering only; English titles and abstracts; no books | Articles and conference papers indexed in Scopus, with credit split across countries and predatory journals removed; 2003–2023 by country and field | Free reports and zipped tables | Two-year lag |
| Scopus, Web of Science | All disciplines; curated and centred on journals; Web of Science keeps books in a separate index | Indexed documents over decades | Subscription | Journals removed from coverage (Web of Science, March 2023); Scopus keeps past content of discontinued titles |
| [Dimensions](https://www.dimensions.ai/scientometric-research/) | All disciplines | Publications (160M+), grants, and the links between them | Free for non-commercial research on research, on application | Relies heavily on Crossref |
| [Semantic Scholar](https://api.semanticscholar.org/datasets/v1/release/latest) | All disciplines (balance across fields not assessed) | Papers (200M), abstracts, 16M full texts; weekly releases since May 2022 | Free download; API heavily rate-limited | Licence terms not reviewed |
| [RELX/Elsevier](https://www.relx.com/~/media/Files/R/RELX-Group/documents/reports/annual-reports/relx-2025-annual-report.pdf) | Elsevier's portfolio only | Article submissions and articles published; 2021–2025 verified, annual | Free PDFs | Rounded figures; "submission" undefined; confounded by the growth of open access |
| [Frontiers](https://www.frontiersin.org/documents/annual-report-2025.pdf) | Frontiers' portfolio only | Acceptance and rejection shares; desk rejections; 2024–2025 | Free PDFs | Integrity screening now accounts for more than half of rejections |
| SSRN, PsyArXiv, SocArXiv and other servers via [Crossref prefixes](https://api.crossref.org/prefixes/10.2139/works?filter=type:posted-content&rows=0&facet=published:%2A) | Economics, law, social sciences (SSRN); psychology (PsyArXiv); sociology (SocArXiv); chemistry (ChemRxiv); several fields (Research Square, Preprints.org) | Preprint DOIs per server, from the 2010s, by day | Free | SSRN up 14-fold (2020–25); versioned DOIs; postings tied to journal submissions |
| [NBER](https://data.nber.org/nber_paper_chapter_metadata/tsv/date.tsv) | Economics | Working papers by issue date, from the 1970s, by day, with economics subject (JEL) codes | Free TSV files | Output limited by membership and capacity |
| [OECD](https://sdmx.oecd.org/public/rest/data/OECD.STI.STP,DSD_MSTI@DF_MSTI,1.3/USA+OECD+CHN+DEU+JPN.......?startPeriod=2019), [UIS](https://api.uis.unesco.org/api/public/data/indicators?indicator=RESDEN.INHAB.TFTE&geoUnit=SDG%3A%20World&start=2010&end=2024), [Eurostat](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/rd_p_persocc?format=JSON&lang=EN&geo=EU27_2020&unit=FTE&sectperf=TOTAL&prof_pos=RSE&sex=T), [SED](https://ncses.nsf.gov/surveys/earned-doctorates) | All fields and sectors | Researchers (full-time equivalent) and doctorates; SED from 1958, the others annual | Free APIs and tables | Lags of 1–3 years; researchers ≠ publishing authors |

## Funders count applications, and only NIH counts the people

### NIH: the only funder that counts both applications and applicants

NIH funds biomedical and health research and sets the standard every other funder falls short of. The NIH Data Book has a public JSON API that needs no login, alongside an Excel file (Table 218). Together they give:

- applications, awards and success rates for research project grants (RPGs) and R01-equivalent grants, **FY1970–2025**
- unique applicant investigators from **FY1998**
- the pool of applicants over rolling five-year windows, from FY2003
- fellowship, career-development and training series from 1997–98

([NIH Data Book API](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=20); [Table 218](https://report.nih.gov/reportweb/web/displayreport?rId=665); [report 164](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=164); [report 303](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=303))

**FY2025** (computed from the same reports):

- RPG applications rose **12.9%, to a record 62,592**.
- Unique RPG applicants rose **8.9%, to 49,609**. So about 70% of the increase came from more people applying and about 30% from more applications per person.
- The five-year applicant pool grew only 2.4%. That points to existing investigators applying more often, rather than a wave of newcomers.
- Awards fell 20.5%, and the success rate dropped to 13% ([NIH Nexus](https://www.grants.nih.gov/news-events/nih-extramural-nexus-news/2026/03/fiscal-year-2025-by-the-numbers-extramural-grant-investments-in-research)).

**The cap.** From the 25 September 2025 submission deadline, NIH limited each investigator to **six applications per calendar year**. It cited investigators who had used AI tools to submit more than 40 applications in one round, even though only 1.3% of applicants submitted more than six in 2024 ([NOT-OD-25-132](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html); [NIH Nexus](https://grants.nih.gov/news-events/nih-extramural-nexus-news/2025/07/apply-responsibly-policy-on-ai-use-in-nih-research-applications-and-limiting-submissions-per-pi)).

Demand kept rising after the cap. Applications for the January 2027 review round "currently exceed 40,000", above the previous record of more than 35,000 in May 2025 ([NIH Nexus](https://grants.nih.gov/news-events/nih-extramural-nexus-news/2026/09/continuing-modified-peer-review-processes-for-the-january-2027-council-round)).

**Confounding shocks.** FY2025–26 also piles up shocks unrelated to LLMs:

- an attempted cap of 15% on indirect (overhead) costs
- forward funding, which paid several years of grants up front
- the autumn 2025 government shutdown, which rescheduled every October–November deadline
- the end of fixed funding cut-offs ("paylines") from January 2026

([NOT-OD-25-068](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-068.html); [NOT-OD-26-005](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-005.html); [NIH Nexus](https://grants.nih.gov/news-events/nih-extramural-nexus-news/2025/11/implementing-a-unified-nih-funding-strategy-to-guide-consistent-and-clearer-award-decisions))

History counsels caution. RPG applications rose 37% between FY2003 and FY2007 with no LLM involved. They fell 4.9% in FY2023, the first fiscal year after ChatGPT's release ([report 20](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=20)).

### NSF: no surge on Europe's scale

NSF funds the sciences and engineering, including the social, behavioural and economic sciences (SBE), but not the humanities. It reports competitive proposals, awards and funding rates rather than people. Its one person-level measure is that 43% of applicants in 2019–2021 were funded.

Proposals ran at about 48,000–49,600 a year in 2012–2018. They fell about 10% as directorates dropped fixed deadlines, then reached **43,532 in FY2025**, against 8,377 awards ([Merit Review Digest FY2021](https://nsf-gov-resources.nsf.gov/2023-06/FY_2021_Merit_Review_Digest.pdf); [NSF FY2024 Agency Financial Report](https://nsf-gov-resources.nsf.gov/pubs/2025/nsf25002/pdf/nsf25002.pdf); [NSF budget](https://nsf.gov/about/budget)). The SBE directorate funded 19% of its proposals in FY2024 ([NSF SBE](https://www.nsf.gov/sbe/funding-rates)); its divisions are broken down below.

NSF's FY2022–2024 review digests were not located, and its Tableau dashboard has no bulk export ([NSF by the Numbers](https://www.nsf.gov/about/about-nsf-by-the-numbers)).

### Europe: the clearest surges, each tangled with programme events

**MSCA Postdoctoral Fellowships** (EU, all disciplines):

- Evaluated proposals went from **6,909 in 2022 to 16,836 in 2025**, and success fell to 9.6%.
- The 17,066 proposals received in 2025 were "the highest number of proposals ever for any funding action" in 40 years of EU research programmes.
- 21% of them named a host in the UK, after the UK rejoined Horizon Europe, and notably more applicants were based outside the EU.

([FECYT](https://www.horizonteeuropa.es/sites/default/files/noticias/24042026_MSCA-PF%20Resultados%202025.pdf); [MSCA](https://marie-sklodowska-curie-actions.ec.europa.eu/news/msca-postdoctoral-fellowships-2025-proposals); [UKRO](https://www.ukro.ac.uk/news/msca-postdoctoral-fellowships-2025-receives-record-number-of-17058-proposals/); [UKRI](https://www.ukri.org/apply-for-funding/horizon-europe/))

**ERC** (all disciplines, in three domains: physical sciences and engineering, life sciences, and social sciences and humanities):

- Starting Grant applications rose from 2,628 (deadline October 2022) to **4,807 (deadline October 2025)**.
- Some review panels now receive more than 250 applications, against a historical 50–150. That prompted restrictions on resubmitting for 2027.
- Statistics for every call since 2007 can be exported to Excel.
- Call names run a year ahead of their deadlines, so align by deadline date.

([ERC statistics](https://erc.europa.eu/statistics-0); [ERC StG 2026](https://erc.europa.eu/news-events/news/starting-grants-2026-applications-facts-and-figures); [ERC President](https://erc.europa.eu/news-events/news/erc-president-explains-stricter-application-measures-amid-rising-demand-funding); [Business Finland](https://www.businessfinland.fi/globalassets/finnish-customers/horizon-europe/tilastotietoa/call_specific_success_rates_11022026.pdf))

**National funders:**

- **SNSF** (Switzerland) received a record 1,451 project applications in October 2025, against 944 in October 2021, and has limited applications per person since April 2026 ([SNSF](https://www.snf.ch/en/aP8IEQcq8CUWFCkF/news/new-record-in-project-funding); [SNSF](https://www.snf.ch/en/9EcyLcUUpkxVDGmp/news/)).
- **ANR** (France): first-stage pre-proposals rose 15.9% in 2026 ([ANR](https://anr.fr/fr/actus/details/news/aapg-appel-a-projets-generique-2026-les-resultats-de-letape-1/)).
- **Swedish Research Council (VR):** its natural-science and engineering call went from 1,109 applications (2022) to 1,374 (2025) ([SLU compilation](https://internt.slu.se/globalassets/mw/externfinansiering/vr_ntsve_from2015_251030.pdf)).
- **DFG** (Germany) attributes its falling 2025 success rate to inflation ([DFG](https://www.dfg.de/resource/blob/399666/dfg-jb2025.pdf)).

### Splitting by discipline shows the surge is uneven

**UKRI councils.** UKRI's council series is the clearest discipline breakdown available. Applications assessed in 2024-25 changed as follows ([UKRI data](https://www.ukri.org/wp-content/uploads/2026/07/160726-UKRI-investments-and-outputs-data-2015-2026.xlsx)):

| Council | Field | Change in 2024-25 |
|---|---|---|
| ESRC | Social sciences | **+55%** |
| EPSRC | Engineering and physical sciences | +43% |
| MRC | Medical research | +37% |
| NERC | Environmental sciences | +32% |
| BBSRC | Biological sciences | −4% |
| AHRC | Arts and humanities | **−10%** |

Award rates then fell at all five councils that publish them.

**ERC by domain.** The ERC's "facts and figures" releases split every call into physical sciences and engineering (PE), life sciences (LS) and social sciences and humanities (SH). The SH share of applications rose in every scheme, and in the latest call of each scheme SH grew faster than both other domains ([StG 2025](https://erc.europa.eu/news-events/news/starting-grants-2025-applications-facts-and-figures); [StG 2026](https://erc.europa.eu/news-events/news/starting-grants-2026-applications-facts-and-figures); [CoG 2025](https://erc.europa.eu/news-events/news/applications-erc-consolidator-grants-2025-facts-and-figures); [CoG 2026](https://erc.europa.eu/news-events/news/applications-erc-consolidator-grants-2026-facts-and-figures); [AdG 2024](https://erc.europa.eu/news-events/news/applications-erc-advanced-grants-2024-facts-and-figures); [AdG 2025](https://erc.europa.eu/news-events/news/applications-erc-advanced-grants-2025-facts-and-figures)):

| Scheme | SH applications (share of total) | Growth in the latest call: SH / PE / LS |
|---|---|---|
| Starting Grants | 1,187 (30%) → 1,568 (33%), calls closing Oct 2024 and Oct 2025 | **+32%** / +19% / +16% |
| Consolidator Grants | 1,033 (33%) → 1,086 (35.5%), 2025 and 2026 calls | **+5%** / −2% / −10% |
| Advanced Grants | 736 (29%) → 1,013 (30%), calls closing Aug 2024 and Aug 2025 | **+38%** / +26% / +34% |

This pattern fits lower writing costs mattering most in writing-heavy fields. It equally fits shocks specific to SSH elsewhere, such as US humanities and social-science cuts pushing researchers towards European funding.

**SSHRC** (Canada's social sciences and humanities funder) published five years of Insight Grant results ([SSHRC deck, hosted by Western University](https://www.uwo.ca/research/doc/funding/domestic/SSHRC_IG_Webinar_2026_EN.pdf)):

- Eligible applications: 1,084 (October 2021), 1,145 (2022), 1,477 (2023), 1,720 (2024) and 1,973 (2025), up **82%** overall.
- The rise came after ChatGPT. The October 2022 competition, which closed before ChatGPT's release, was up only 6%; the next three were up 29%, 16% and 15%.

It is not clean evidence of an LLM effect, for three reasons ([SSHRC 2025 competition](https://sshrc-crsh.canada.ca/en/funding/opportunities/insight-grants/2025/competition.aspx)):

- The amounts SSHRC awarded rose 48% and then 27%, which made applying more worthwhile.
- The 2025 competition raised the maximum amounts applicants could request.
- Each person may hold only one Insight Grant application at a time, which caps volume per person.

**NSF's SBE directorate** published proposals and success rates by division, but for FY2024 only ([NSF SBE](https://www.nsf.gov/sbe/funding-rates)):

- Behavioral and Cognitive Sciences: 1,219 proposals, 17% funded
- Social and Economic Sciences: 1,159 proposals, 20% funded
- the directorate overall: 19% funded

**NEH** (the US federal humanities funder) has broken its own series ([NEH FY2025 budget justification](https://www.neh.gov/sites/default/files/inline-files/NEH%20FY%202025%20Congressional%20Justification%20%28CJ%29.pdf); [NEH FY2025 report](https://www.neh.gov/sites/default/files/NEH%20FY2025%20PAR%20to%20OMB.pdf); [NEH FY2026 budget request](https://www.humanities.gov/sites/default/files/NEH%20FY%202026%20Congressional%20Justification.pdf); [NEH 2026 fellowships notice](https://apply07.grants.gov/grantsws/rest/opportunity/att/download/350942)):

- It normally receives roughly 3,750 applications a year, two-thirds of them to its research division.
- In FY2025 it received "over 4000 applications" and made 373 awards. In the same year it terminated about 1,477 open grants and cut close to 70% of its staff.
- The FY2026 budget request proposed closing the agency.
- The 2026 Fellowships competition accepts only projects on American history and culture and Western civilization.

NEH counts from FY2025 onward are not comparable with earlier years.

**Other SSH funders:**

- **British Academy:** applications for its postdoctoral fellowships went from 528 (2022) to 604 (2025) and 798 (2026). The Academy partly credits its early-career researcher network ([RoRI data](https://media.nature.com/original/magazine-assets/d41586-026-01297-y/52331462)). Its Small Research Grants drew a reported 1,116 applications in 2024-25, with 21% funded by lottery among proposals above a quality threshold (third-party figure) ([funder directory](https://www.hinchilla.com/funder-directory/the-british-academy-for-the-promotion-of-historical-philosophical-and-philological-studies)).
- **DFG, ANR, NWO and Spain's AEI** publish no SSH application counts that could be found. DFG shows success rates by area only in a chart, and notes that the humanities and social sciences have the highest share of women applicants (41.7%) ([DFG](https://www.dfg.de/resource/blob/399666/dfg-jb2025.pdf)). ANR reports success rates "broadly balanced" across disciplines ([ANR AAPG 2024](https://anr.fr/fr/resultats-de-laapg/aapg-2024/)).

**Grant texts show a second discipline gradient.** Across 221,425 funded grant abstracts, words typical of LLM output ("marker words") rose ([Naser](https://arxiv.org/pdf/2609.13241)):

- at NSF: most in the technology, computing and physical-science directorates; least in geosciences and SBE
- at UKRI: most in Innovate UK and BBSRC; least in AHRC and NERC

BBSRC combines the largest marker rise with falling applications. Using LLMs to write does not automatically raise application volume.

### Asia-Pacific: the longest non-US series and the best low-surge comparator

- **JSPS KAKENHI** (Japan) publishes new applications and awards for **FY1996–2025**. Applications peaked at 104,158 in FY2020 and stood at 95,482 in FY2025, up only 6% since FY2023. The award rate held near 27% ([JSPS](https://www.jsps.go.jp/file/storage/kaken_27_kdata_g_4551/2-1_r7.pdf)).
- **NSFC** (China's natural-science funder): proposals rose from 294,396 (2022) to **470,561 (2026)**. NSFC attributes the 26% jump in 2024 to a rule allowing resubmission to its General Program after two consecutive failures. It also stresses that applicants may submit only one proposal per programme type a year ([RoRI data](https://media.nature.com/original/magazine-assets/d41586-026-01297-y/52331462); [Science and Technology Daily](https://www.stdaily.com/web/gdxw/2026-08/26/content_569790.html)).
- **CIHR** (Canada's health research funder): Project Grant competitions grew from 2,443 applications (spring 2024) to 3,101 (fall 2025), while success fell to 13.6% ([CIHR](https://cihr-irsc.gc.ca/e/54594.html)).
- **ARC** (Australia): a new expression-of-interest stage, introduced for the 2025 round of Discovery Projects, breaks the series ([ARC](https://www.arc.gov.au/funding-research/funding-outcome/selection-outcome-reports/dp25-selection-report-funding-commencing-2025)).

### The only cross-funder dataset is weaker than its headline

The only dataset covering many funders is a tracker by the Research on Research Institute (RoRI), published as supplementary data to a *Nature* comment ([RoRI data](https://media.nature.com/original/magazine-assets/d41586-026-01297-y/52331462); [Nature](https://doi.org/10.1038/d41586-026-01297-y)).

Its widely quoted **57%** growth from 2022 to 2025 is the simple, unweighted average of twelve funders' growth rates:

- the **median is 45.7%**
- pooled applications rose 47.6%, with NSFC supplying 84% of the pooled total (computed from the file)
- growth ranges from +14% (British Academy postdoctoral fellowships) to +142% (MSCA)

The funders' own notes name causes other than AI for several series:

- NSFC's resubmission rule
- restructuring at the ARC
- programme changes at Wellcome
- the British Academy's early-career network
- tight funding at Michael Smith Health Research BC

The file has several problems:

- it has no data before 2022
- its year-on-year sheet is mislabelled
- its UKRI row includes Innovate UK, UKRI's business-innovation agency
- its 2022 Wellcome value duplicates the 2023 one
- co-author Wilsdon directs RoRI, which is funded by a group that includes some of the funders analysed

Only NIH (in its cap notice), Wellcome ("likely") and the RoRI authors attribute the surge to AI. The ERC, MSCA, SNSF, UKRI, ANR and CIHR do not mention AI ([Wellcome](https://wellcome.org/insights/articles/rethinking-future-research-funding)).

| Series | Disciplines | What it counts; coverage | Access and cost | Breaks and caveats | 2022→2025 |
|---|---|---|---|---|---|
| [NIH Data Book](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=20) | Biomedical and health research | Applications (resubmissions within a year counted once), awards, success, from FY1970; unique applicants from FY1998; by institute, grant type, career stage, sex | Free JSON API and Excel | Cap of six per investigator (25 Sep 2025); FY2025 award cuts and forward funding; shutdown; paylines dropped (Jan 2026) | Applications +14.7%; applicants +11.1% |
| [NSF](https://nsf-gov-resources.nsf.gov/pubs/2025/nsf25002/pdf/nsf25002.pdf) | Sciences, engineering and SBE; no humanities | Competitive proposals, awards, funding rate; three-year share of investigators funded; FY2012–2025 by directorate and state | Free PDFs; Tableau dashboard without bulk export | Move away from fixed deadlines (about FY2019); FY2022–24 digests not located; SBE division figures online for FY2024 only | +11.2% |
| [UKRI](https://www.ukri.org/wp-content/uploads/2026/07/160726-UKRI-investments-and-outputs-data-2015-2026.xlsx) | All disciplines, by council (AHRC arts and humanities; ESRC social sciences) | Applications received, assessed and awarded, 2015-16 to 2025-26 | Free Excel | 2026 revision (Innovate UK eligibility); funding pauses in 2025-26 | ESRC +55% and AHRC −10% in 2024-25 alone |
| [ERC](https://erc.europa.eu/statistics-0) | All disciplines, in three domains (physical sciences, life sciences, SSH) | Submitted, eligible, evaluated and granted proposals for calls since 2007, by domain, panel, country, gender | Free statistics tool with Excel export; domain counts in each call's press release | Call names run a year ahead of deadlines; UK rejoining Horizon Europe; 2027 resubmission limits | +54.9% (all schemes); SH grew fastest in the latest calls |
| [MSCA Postdoctoral Fellowships](https://www.horizonteeuropa.es/sites/default/files/noticias/24042026_MSCA-PF%20Resultados%202025.pdf) | All disciplines | Proposals received, evaluated and funded, calls 2021–2025 (earlier ones not retrieved) | European Commission dashboard; PDFs from national contact points | UK rejoining Horizon Europe; inflow from outside the EU | +142% received |
| [British Academy postdoctoral fellowships](https://media.nature.com/original/magazine-assets/d41586-026-01297-y/52331462) | Humanities and social sciences | Postdoctoral fellowship applications, 2022–2026 (RoRI file); Small Research Grants 2024-25 (third-party figure) | Free xlsx | Academy credits its early-career network; small grants allocated by lottery above a quality bar | +14% (then +32% in 2026) |
| [SSHRC Insight Grants](https://www.uwo.ca/research/doc/funding/domestic/SSHRC_IG_Webinar_2026_EN.pdf) | Social sciences and humanities | Eligible applications, success rates and amounts awarded per competition, 2021–2025 | Free (SSHRC slides hosted by a university) | 2025 rise in request ceilings; award budget up 48% then 27%; one application per person at a time | +72% |
| [NEH](https://www.neh.gov/sites/default/files/NEH%20FY2025%20PAR%20to%20OMB.pdf) | Humanities (US) | Applications (normally about 3,750 a year; over 4,000 in FY2025) and awards, in budget documents and annual reports | Free PDFs | About 1,477 grants terminated and close to 70% of staff cut (FY2025); closure proposed; 2026 fellowships limited to American history and Western civilization | Series broken from FY2025 |
| [JSPS KAKENHI](https://www.jsps.go.jp/file/storage/kaken_27_kdata_g_4551/2-1_r7.pdf) | All disciplines | New applications and awards, FY1996–2025, by category | Free PDF and HTML | Changes to grant categories not checked; per-person limits | +3.3% |
| [NSFC](https://www.stdaily.com/web/gdxw/2026-08/26/content_569790.html) | Natural sciences | Proposals received and accepted; awards; 2022–2026 verified | Annual notices; RoRI file | 2024 resubmission rule; one proposal per programme type | +47.2% |
| [CIHR Project Grant](https://cihr-irsc.gc.ca/e/54594.html) | Health | Applications submitted and funded; two competitions a year | Free web pages | 23.5% budget cut (fall 2025); 55.5% of applications not discussed in review | +48.1% |
| SNSF, ANR, VR, DFG | Multidisciplinary (the VR series covers natural sciences and engineering) | Applications or pre-proposals; success; annual | Web pages and PDFs; SNSF's data portal works only in a browser (JavaScript) | Per-person limits at SNSF (Apr 2026); ANR's two-stage process | SNSF +54% (2021→2025); VR +24% |
| [RoRI tracker](https://media.nature.com/original/magazine-assets/d41586-026-01297-y/52331462) | Mixed | Applications to 12 funders, with differing definitions, 2022–2025 (2026 partial) | Free xlsx | No data before 2022; mean vs median; data errors | Median +45.7% |

*The 2022→2025 changes for NIH, NSF, KAKENHI and NSFC are computed from the linked counts; ERC, CIHR and the RoRI median come from the RoRI file.*

## Scholarship applicant counts survive mainly as press releases

### Fellowships

Where each person submits a single application, applications equal people, so programme counts do measure people. But they do so only per programme, only when the programme announces them, and never with duplicates removed across programmes.

**NSF's Graduate Research Fellowship Program (GRFP)** is the richest case. It covers science, engineering and, until now, the social sciences.

- NSF outreach slides give about **16,800 applications in 2016, falling to 12,600 in 2021** ([NSF GRFP slides](https://ws.engr.illinois.edu/sitemanager/getfile.asp?id=4885)).
- NSF reported "nearly 14,000 applicants" for 2026 ([NSF](https://www.nsf.gov/news/nsf-announces-2026-graduate-research-fellowship-program)).
- An official list names every awardee from **1952 to 2026**, with their field but not the applicants. The field mix of awards can therefore be traced back seven decades ([GRFP award list](https://www.research.gov/grfp/AwardeeList.do?method=loadAwardeeList)).

Policy breaks dominate the GRFP series:

- Offers swung from 2,555 (2023) to 1,500 (2025) to 2,597 (2026).
- Second-year graduate students were excluded from 2025.
- The FY2027 call drops the SBE directorate and STEM-education research.

([AIP FYI](https://www.aip.org/fyi/nsf-graduate-research-fellowships-expected-to-fall-next-year))

Elsewhere, the numbers are snapshots from press releases:

| Programme | Reported numbers |
|---|---|
| Rhodes (US) | About 2,800 started applications, 965 endorsed by their universities, 238 finalists, 32 scholars (November 2025) ([Rhodes](https://www.rhodeshouse.ox.ac.uk/media2/ikolktw5/press_release_2025-final.pdf)) |
| Marshall | Publishes a demographic funnel: 1,023 endorsed, 156 shortlisted, 43 selected ([Marshall](https://www.marshallscholarship.org/wp-content/uploads/2026/04/Marshall-Competition-Report-2026_2027.pdf)) |
| Schwarzman | A record "nearly 5,000" candidates in January 2025; a reported 5,800-plus in 2026 ([Schwarzman](https://www.schwarzmanscholars.org/events-and-news/schwarzman-scholars-announces-tenth-class-150-exceptional-scholars-from-38-countries-to-join-prestigious-network-of-1300-young-global-leaders-record-high-applications-indicate-growing-interest-in/); [Harvard Crimson](https://api.thecrimson.com/article/2026/1/17/2027-schwarzman-scholars)) |
| Paul & Daisy Soros | A record 3,070 applications for 2026 ([PD Soros](https://pdsoros.org/meet-the-class-of-2026/)) |
| Hertz | More than 1,450 applicants ([Hertz](https://www.hertzfoundation.org/news/54-finalists-named-for-the-2026-hertz-fellowships/)) |
| "la Caixa" INPhINIT | 1,636 doctoral applications in the round announced in March 2024; 1,502 in March 2025 ([la Caixa 2024](https://mediahub.fundacionlacaixa.org/en/research-fellowships/fellowships/phd-fellowships/2024-03-12/hundred-researchers-receive-doctoral-postdoctoral-fellowships-5663.html); [la Caixa 2025](https://mediahub.fundacionlacaixa.org/en/research-fellowships/fellowships/phd-fellowships/2025-03-18/caixa-foundation-attracts-retains-talent-phd-young-researchers-6940.html)) |

For SSH, the British Academy's postdoctoral fellowships (see the grants section) are the best fellowship series found. In the US humanities, NEH's 2026 Fellowships competition accepts only projects on American history and culture and Western civilization, which breaks any humanities fellowship series ([NEH notice](https://apply07.grants.gov/grantsws/rest/opportunity/att/download/350942)). SSHRC's doctoral and postdoctoral award series were not collected. No current applicant totals were found for Fulbright, Chevening, Gates Cambridge, Knight-Hennessy, DAAD, Erasmus Mundus or Spain's FPU fellowships.

### Graduate admissions

Graduate admissions data count applications, not people, because each applicant applies to several programmes.

- **CGS/ETS Graduate Enrollment and Degrees survey.** Run annually since 1986, it is the only national US source of graduate applications by broad field (11 fields). For fall 2024 it counted **899,141 doctoral and 1,961,548 master's and other applications**. The social and behavioural sciences drew 123,853 doctoral applications, second only to the biological and agricultural sciences, and business drew 276,825 master's applications ([CGS 2025 report](https://cgsnet.org/wp-content/uploads/2025/12/CGS_GED-2025_Report_Final.pdf)). Two caveats: the set of responding institutions changes every year (558, then 536), and the December 2025 report replaced totals with averages by institution size, a change of method during the LLM period ([CGS 2024 report](https://cgsnet.org/wp-content/uploads/2024/12/GED-2024-1.1.pdf)).
- **LSAC** (US law schools) is the only admissions source that publishes both people and applications. For the 2026 cycle it counted 82,487 applicants and 579,839 applications. Applications per applicant therefore rose from 6.61 (2024) to 7.03 (2026), computed from these figures. That is the pattern cheaper, AI-tailored applications would produce, though LSAC offers no explanation ([LSAC](https://www.lsac.org/podcast/keeping-data-september-2026)).
- **GMAC** (business schools) reported applications up 7% in 2025 ([GMAC](https://www.gmac.com/why-gmac/gmac-news/gmac-press-releases/global-demand-for-business-education)).
- **AAU Data Exchange** (55 US research universities) reports PhD applications only from the 2025 cycle. For fall 2026, international applications fell 21% while domestic ones rose 3% ([NAFSA citing AAU](https://www.nafsa.org/sites/default/files/media/document/Fall_2026_International_Student_Economic_Snapshot_NAFSA_JBI.pdf); [College Fix](https://www.thecollegefix.com/ph-d-admissions-fell-15-over-past-year-as-international-applications-drop/)).
- **CRA Taulbee survey:** its data on computing PhD applications serve only as a high-exposure benchmark.

Several sources count enrolments, new entrants or degrees rather than applications ([NCSES GSS](https://ncses.nsf.gov/pubs/nsf26308); [NCSES SED](https://ncses.nsf.gov/pubs/nsf26315); [Eurostat catalogue](https://ec.europa.eu/eurostat/api/dissemination/catalogue/toc/txt?lang=en)):

- NCSES's survey of graduate students (since 1966, science, engineering and health only)
- the Survey of Earned Doctorates (since 1958)
- Eurostat's education statistics

Spain's national statistics report master's and doctoral enrolment but not applications. Catalonia's open data list fellowship recipients for 2004–2023 without applicant counts ([DyC 2023](https://www.ciencia.gob.es/dam/jcr:d2738536-6a67-43bf-b174-a0fb033b3fc4/DyC_2023.pdf); [Catalonia open data](https://analisi.transparenciacatalunya.cat/resource/rsgi-8ymj.json)). For the UK, the timeliest measure of demand is the Home Office's monthly count of study-visa applications, available from January 2022 ([Home Office](https://www.gov.uk/government/statistics/monthly-entry-clearance-visa-applications-july-2026/monthly-entry-clearance-visa-applications-july-2026)).

### No evidence yet links application growth to AI

No primary source attributes a rise in graduate or scholarship applications to generative AI. Record numbers cluster at programmes that are cheap to apply to and open to many people, such as Schwarzman and Soros. Competitions that require university endorsement, such as Rhodes and Marshall, absorb extra volume at the campus stage. That makes the ratio of started applications to endorsed candidates (about 2,800 to 965 at Rhodes) the stage to watch.

**Policy responses are creating new data.** Rhodes now asks applicants to name any generative-AI tool they used and the prompts they gave it. Chevening prohibits AI-written answers and screens for them. Aggregated disclosures could be requested from both ([Rhodes guidance](https://www.rhodeshouse.ox.ac.uk/files/candidate-guidance-genai-and-support-with-applications/); [Chevening](https://www.chevening.org/faqs/can-i-use-ai-to-help-me-write-my-application/)).

**Visa and funding shocks swamp the aggregates:**

- New international enrolment in the US fell 17% in fall 2025 ([PIE News](https://thepienews.com/new-international-enrolments-in-us-down-17-this-fall/)).
- A December 2025 US order restricted entry from 39 countries, and the State Department has not published visa data since September 2025 ([NAFSA](https://www.nafsa.org/sites/default/files/media/document/Fall_2026_International_Student_Economic_Snapshot_NAFSA_JBI.pdf)).
- The UK's January 2024 rule on students' dependants cut dependant visa applications by 87% ([Home Office](https://www.gov.uk/government/statistics/monthly-entry-clearance-visa-applications-july-2026/monthly-entry-clearance-visa-applications-july-2026)).

Series limited to domestic applicants are therefore the cleaner test. Fellowship cycles with October–November 2023 deadlines are the first fully exposed to ChatGPT. Those with October–November 2022 deadlines closed before ChatGPT's release.

| Source | Disciplines | What it counts; coverage | Access and cost | Breaks and caveats |
|---|---|---|---|---|
| [NSF GRFP](https://www.research.gov/grfp/AwardeeList.do?method=loadAwardeeList) | Science, engineering, SBE (SBE dropped from FY2027) | Applications (patchy), offers, honourable mentions; awards 1952–2026 with field; applications 2016–21 and 2026 | Free award list with export; NSF releases | Eligibility cuts (2025, FY2027); offers 2,555→1,500→2,597 |
| [Rhodes US](https://www.rhodeshouse.ox.ac.uk/media2/ikolktw5/press_release_2025-final.pdf), [Marshall](https://www.marshallscholarship.org/wp-content/uploads/2026/04/Marshall-Competition-Report-2026_2027.pdf) | All fields | Started, endorsed, finalists, winners; demographics for Marshall; annual | Free PDFs | University endorsement limits volume; Rhodes Global reportedly suspended for 2026–27 ([Cherwell](https://www.cherwell.org/?p=195130)) |
| Schwarzman, PD Soros, Hertz, "la Caixa" | Varies by programme | Applicants and awardees; annual announcements | Free | One-off figures; "record" framing; no definitions |
| [NEH Fellowships](https://apply07.grants.gov/grantsws/rest/opportunity/att/download/350942) | Humanities (US) | Competition notices; application counts only in NEH budget documents | Free | 2026 competition limited to American history and culture and Western civilization; agency proposed for closure |
| Fulbright, Chevening, Gates Cambridge, Knight-Hennessy, DAAD, Erasmus Mundus, FPU | All fields | Awards; at most application counts for single countries | — | No applicant series found |
| [CGS/ETS GE&D](https://cgsnet.org/wp-content/uploads/2025/12/CGS_GED-2025_Report_Final.pdf) | All graduate fields (11 broad fields, including business and the social and behavioural sciences) | Graduate applications, offers, enrolment, degrees (US); annual since 1986 | Free reports; underlying data not public | 2025 switch to averages by institution size; changing respondents |
| [LSAC](https://www.lsac.org/podcast/keeping-data-september-2026) | Law | Unique applicants and applications; annual cycles | Free summaries | Law only |
| [GMAC](https://www.gmac.com/why-gmac/gmac-news/gmac-press-releases/global-demand-for-business-education) | Business | Changes in applications reported by programmes; annual | Summary free; full report gated | Changing set of respondents |
| [AAU Data Exchange](https://www.nafsa.org/sites/default/files/media/document/Fall_2026_International_Student_Economic_Snapshot_NAFSA_JBI.pdf) | All PhD fields at 55 universities | PhD applications and admissions, from the 2025 cycle | Press releases; data for members only | No data from before LLMs |
| [NCSES GSS](https://ncses.nsf.gov/pubs/nsf26308), [SED](https://ncses.nsf.gov/pubs/nsf26315) | GSS: science, engineering and health; SED: all research doctorates | Enrolled graduate students and postdocs (since 1966); doctorates (since 1958) | Free tables; SED individual-level data licensed | No applications; GSS reviewed which institutions it covers in 2024 |
| [UK Home Office](https://www.gov.uk/government/statistics/monthly-entry-clearance-visa-applications-july-2026/monthly-entry-clearance-visa-applications-july-2026) | All fields (international students only) | Monthly study-visa applications, from Jan 2022 | Free | Dependants rule (1 Jan 2024) |
| [Eurostat education statistics](https://ec.europa.eu/eurostat/api/dissemination/catalogue/toc/txt?lang=en) | All fields | Enrolments, new entrants, graduates by education level, 2013–2024 | Free API | No applications dataset |

## Social sciences and humanities need their own sources

The big indexes and preprint servers under-count the social sciences and humanities, so a study of academia as a whole needs sources built for these fields. Most of the ones below are free and need no key, and most show strong growth in 2025–2026. Almost every one also has a break in that same period: versioning, scope rules, bulk imports, platform migrations or bot traffic. SSH grant and fellowship series (ERC, UKRI's AHRC and ESRC, SSHRC, NSF's SBE directorate, NEH, the British Academy) are covered in the funders section. SSH admissions series (CGS by field, LSAC, GMAC) are in the scholarships section.

### Field-specific publication sources fill the gaps the big indexes leave

| Source | Disciplines | What it counts; coverage | Access and cost | Breaks and caveats |
|---|---|---|---|---|
| [OSF preprint servers](https://api.osf.io/v2/providers/preprints/): SocArXiv, PsyArXiv, EdArXiv, Law Archive | Sociology, psychology, education, law | Preprints by creation date from 2017; new papers can be counted separately from later versions | Free API, no key | Each version listed as a separate record since April 2025, so raw 2025 counts overstate growth (PsyArXiv +113% raw vs +30% new papers); SocArXiv rule changes in Nov 2025 |
| [HAL](https://api.archives-ouvertes.fr/search/?q=%2A:%2A&rows=0&wt=json&facet=true&facet.field=level0_domain_s) (France) | All disciplines; SSH is 39% of 4.7M records, split into law, history, literature, economics, education and more | Deposits by year (all, and full text only), by production year and by document type (articles, chapters, books, theses) | Free search API, no key | Bulk import in 2019; spike across all domains in 2020; French open-access mandates |
| [ERIC](https://api.ies.ed.gov/eric/?search=publicationdateyear:2023&format=json&rows=0) | Education | Records by publication year from at least 1995, with a peer-review flag; abstracts can be used for text analysis | Free API, no key | Selective, so it partly measures indexing policy; 30% drop in 2012–2014; jump in 2021, before ChatGPT; recent years incomplete |
| [RePEc / EconPapers](https://econpapers.repec.org/) | Economics | Totals (1.32M working papers, 3.83M articles, 73,000 books) and annual additions (70,000 working papers in 2025) ([RePEc blog](https://blog.repec.org/2026/01)) | Free web pages; bulk metadata via RePEc's own channels (not tested) | Additions track new archives joining (48 in 2025), not output; usage statistics inflated by AI bots since Oct 2025 ([LogEc](https://logec.repec.org/)) |
| SSRN (its own statistics) | Economics, law, social sciences | Year-end totals only (1.77M full-text papers at end-2025) | No API; scripted access blocked | Crossref counts inflated (14-fold, 2020–25) |
| [Knowledge Commons (KC Works)](https://works.hcommons.org/api/records?size=1) | Humanities and social sciences | Records by creation year (46,437 in total) | Free API, no key | Its 2026 surge (+53% by mid-October) is partly papers diverted from SocArXiv, which has redirected humanities papers here since Nov 2025 |
| [DOAB](https://directory.doabooks.org/download-export?format=csv) and [OAPEN](https://library.oapen.org/download-export?format=csv) | Open-access books, with subject codes (Thema), so SSH titles can be counted | Books and chapters by year of issue | Free CSV export and OAI-PMH harvesting; search API blocked from this environment | Exports stale (last updated Oct 2025); growth driven by funders' open-access book mandates |
| PhilPapers / PhilArchive | Philosophy | About 122,000 works (early 2026) | Scripted access blocked; OAI-PMH harvesting untested | No time series obtained |
| [theses.fr](https://theses.fr/api/v1/theses/recherche/?q=%2A&debut=0&nombre=1), [EThOS](https://ethos.bl.uk/), [TESEO](https://www.ciencia.gob.es/Universidades/TESEO.html) | Doctoral theses (France, UK, Spain) | theses.fr: 568,192 theses with discipline facets. EThOS: 650,000+ UK theses. TESEO: Spanish theses since 1976 | theses.fr free API; EThOS search only; TESEO publishes no statistics | EThOS was offline from Oct 2023 to Jul 2026 after a cyberattack; TESEO blocked scripted access |
| [OpenAlex fields](https://openalex.s3.amazonaws.com/data/jsonl/fields/updated_date=2026-10-14/part_0000.gz) | All SSH fields; Arts and Humanities is a field inside the "Social Sciences" domain | Lifetime totals only in the summary records (Arts and Humanities 45.3M works; Education 9.6M; Law 4.3M; Philosophy 3.6M) | Free snapshot; yearly counts need an API key or the full work files (about 615 GB) | Arts and Humanities total grew 3.4-fold between the 2024 and 2026 versions |
| National research-information systems (Flanders, Finland, Norway, Poland, Slovenia) | All SSH outputs, including books | Complete national records of SSH publications | Varies by country | Definitions differ by country ([Kulczycki et al.](https://doi.org/10.1007/s11192-018-2711-0)) |

HAL is the best place for a STEM-versus-SSH comparison inside one system. Humanities, social sciences and STEM share the same platform, mandates and import shocks there, so a gap between domains is not an artefact of the platform. Full-text SSH deposits rose 34% from 2022 to 2025, against 24% from 2019 to 2022. That is an acceleration, but French open-access mandates confound it ([HAL full-text deposits](https://api.archives-ouvertes.fr/search/?q=%2A:%2A&rows=0&wt=json&fq=level0_domain_s:shs&fq=submitType_s:file&facet=true&facet.field=submittedDateY_i&facet.limit=200&facet.sort=index)).

### LLM evidence in the social sciences is now substantial

**Studies estimating LLM use and its effects:**

- **Economics.** Words typical of AI-written text in 25 top economics journals rose by about 3 percentage points in 2023 and nearly 7 in 2024. The authors call this a conservative estimate ([Feyzollahi & Rafizadeh, Economics Letters](https://doi.org/10.1016/j.econlet.2025.112265); [UMass](https://www.umass.edu/news/article/study-finds-accelerating-adoption-ai-language-models-economics-research-papers)).
- **Sociology.** Applying Liang et al.'s method to 1.49 million sociology abstracts in OpenAlex, Cao found LLM-modified text rose "from near zero before late 2022 to 24.3 percent of abstract sentences in July–December 2025". Uptake was highest in empirical and applied subfields, lowest in theory, and higher among younger scholars and less prestigious institutions and journals ([Cao, Socius](https://doi.org/10.1177/23780231261460657)).
- **SSRN** (economics, law and the social sciences) ([Kusumegi et al.](https://arxiv.org/pdf/2601.13187); [Zhao et al.](https://arxiv.org/pdf/2605.07723)):
  - Researchers who adopted LLMs raised their output by **59.8%** compared with similar non-adopters, the largest effect of the three servers Kusumegi et al. studied.
  - Even authors whose names the study classed as Caucasian, at institutions in English-speaking countries, gained 46.2% on SSRN, against 23.7% on arXiv.
  - SSRN had the highest rate of hallucinated citations of the four sources Zhao et al. checked: **1.91% of references** in August 2025, about five times arXiv's rate.
- **Management.** *Organization Science*'s editors report that "submission volume has risen 42% since the late 2022 release of ChatGPT, while writing quality has declined", with AI-generated writing accounting "for nearly all of these trends". AI-written peer reviews have also increased ([Gartenberg et al.](https://doi.org/10.1287/orsc.2026.ed.v37.n3)).
- **Law.** One SSRN paper reports a sharp rise in AI use in legal scholarship, detected through a telltale "AI idiosyncrasy". Its findings could not be checked ([Conklin & Houston](https://doi.org/10.2139/ssrn.5190385)).

**Journals and preprint servers are reacting:**

- **JPART** (public administration) received 45–50 submissions a month in autumn 2023 (about 575 a year) and 119 in April 2026. It blames this "in large part" on generative AI. From 1 July 2026, each author may make at most three submissions per calendar year, of which at most two may be desk-rejected, and every listed author counts ([JPART policy](https://www.gopmra.org/assets/Secretariat/Policies/jpart-submission-cap-policy.pdf)).
- **SocArXiv** ([SocArXiv announcements](https://socopen.org/category/announcements/); [SocArXiv pause](https://socopen.org/2025/11/27/socarxiv-moratorium-on-ai-topic-papers-policy-in-formation/); [Nature](https://www.nature.com/articles/d41586-026-03194-w)):
  - On 19 November 2025 it reported "record high submission rates" and "many non-research, spam, and AI-generated submissions", with "a lot of junk and AI submissions … in the areas of religion, philosophy, and various language studies".
  - It began requiring an ORCID identifier from submitters and redirected arts and humanities papers to Knowledge Commons.
  - On 27 November 2025 it paused papers on AI topics for 90 days. It published an AI policy on 9 March 2026.
  - *Nature* reports a limit of one submission per author per week. Other reports conflict, and SocArXiv's own site does not state a limit.
- **Philosophy & Public Affairs** banned submissions substantially written by AI in August 2026, after it had published an article largely written by AI as an experiment (reported by a philosophy news blog) ([Daily Nous](https://dailynous.com/2026/08/24/after-experiment-journal-decides-to-prohibit-ai-authored-content/)).
- **Bioethics:** the editor reported a double-digit number of submissions with strong evidence of machine-generated content, and no reliable detection tools ([Daily Nous](https://dailynous.com/2026/07/20/a-scene-from-the-ai-flooding-of-academic-journals/)).
- **Across publishers:** journals on the ScholarOne submission platform reportedly received 33% more submissions in the first quarter of 2026 than a year earlier, after +17% in 2025. This is a secondary report and not specific to SSH ([AcademicJobs](https://www.academicjobs.com/research-publication-news/2026-journal-submissions-surge-33percent-on-scholarone-or-academicjobs-26524)).

### Whether SSH looks exposed depends on the measure

| Measure | What it shows for SSH | Source |
|---|---|---|
| Counts of telltale "LLM words" | Growth much smaller in the social sciences, arts and humanities than in STEM | [Kousha & Thelwall](https://doi.org/10.1007/s11192-026-05601-5) |
| Estimated share of LLM-modified sentences | Sociology 24.3% (late 2025), a similar level to arXiv computer science's 22.5% a year earlier | [Cao](https://doi.org/10.1177/23780231261460657); [Liang et al.](https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf) |
| Output per LLM adopter | SSRN +59.8%, the largest of three servers studied | [Kusumegi et al.](https://arxiv.org/pdf/2601.13187) |
| Journal submissions | *Organization Science* +42% since ChatGPT; JPART up 2.4–2.6-fold | [Gartenberg et al.](https://doi.org/10.1287/orsc.2026.ed.v37.n3); [JPART](https://www.gopmra.org/assets/Secretariat/Policies/jpart-submission-cap-policy.pdf) |
| Grant applications | ERC social sciences and humanities grew fastest in the latest call of every scheme; SSHRC +82% (2021–2025); AHRC −10% in 2024-25 | Funders section |
| LLM words in grant abstracts | Smallest rises at NSF's SBE directorate and UKRI's AHRC | [Naser](https://arxiv.org/pdf/2609.13241) |

One plausible explanation is that SSH abstracts lean on field-specific vocabulary, which dilutes generic markers such as "delve". Writing-heavy production in these fields is nonetheless highly exposed. In short, LLM-word counts will make SSH look less exposed than measures of output and submissions do.

### The humanities have the weakest measured signals and the thinnest instruments

The measured signals for the humanities are weak:

- AHRC applications fell 10% in 2024-25, while ESRC's rose 55%.
- AHRC grant abstracts show the smallest rise in LLM words among UKRI councils.
- Counts of LLM words grew least in arts and humanities.

([UKRI data](https://www.ukri.org/wp-content/uploads/2026/07/160726-UKRI-investments-and-outputs-data-2015-2026.xlsx); [Naser](https://arxiv.org/pdf/2609.13241); [Kousha & Thelwall](https://doi.org/10.1007/s11192-026-05601-5))

The anecdotes point the other way:

- SocArXiv found its junk and AI-generated submissions concentrated in religion, philosophy and language studies.
- *Philosophy & Public Affairs* banned AI-written papers.
- The editor of *Bioethics* reported machine-generated submissions.

No study yet estimates LLM use across the humanities beyond these word-count aggregates. In the US, the NEH disruption dominates any humanities funding series. Low measured exposure in the humanities may therefore reflect weak instruments more than low use.

### SSH offers its own natural experiments

These are dated interventions that can be tested directly:

- **JPART's cap** (1 July 2026). The policy document includes a chart of monthly submissions.
- **SocArXiv's rules** (19 and 27 November 2025, and March 2026). Daily counts are available from the OSF API.
- **Philosophy & Public Affairs' ban** (August 2026).
- **Italy's temporary 2023 ChatGPT ban**, applied to economics output in work described only in a seminar abstract ([RITM seminar](https://www.ritm.universite-paris-saclay.fr/?p=13184)).

Caps, bans and scope rules move volume elsewhere as well as reducing it. SocArXiv's humanities exclusion pushes papers to Knowledge Commons, and a journal's cap pushes submissions to uncapped journals. So these tests need a system-wide denominator, such as HAL or an OpenAlex snapshot.

### Gaps that remain

- No study measures LLM-written text in education research, although ERIC's abstracts would allow it.
- Evidence on law reviews rests on one unverified paper.
- No study estimates LLM use across the humanities beyond counts of LLM words.
- ERC counts for the social sciences and humanities before 2024, and per-panel counts, were not retrieved. They are available from ERC statistics.
- NEH application counts before FY2025 need its budget documents.
- No SSH application counts were found for DFG, ANR, NWO or Spain's AEI.
- No yearly series was found for PhilPapers, or for SSRN by subject network.

## Isolating the LLM effect takes a dose measure, a shock calendar and comparison groups

Volume series alone cannot identify an LLM effect, because LLM uptake, the growth of each field and institutional shocks all move together. A credible approach does three things:

1. It measures each group's LLM use (the "dose") directly.
2. It dates every confounding event.
3. It compares groups that received different doses or faced different rules.

### Dose studies cover STEM best, the social sciences increasingly, and the humanities barely

**Two methods that estimate LLM use across a whole body of text dominate**, and both have public code:

- **Kobak et al.** compared word frequencies in more than 15 million PubMed abstracts (2010–2024) with what earlier years predicted ([Kobak et al., Science Advances](https://arxiv.org/abs/2406.07016v5); [code](https://github.com/berenslab/llm-excess-vocab)). They found that **at least 13.5% of 2024 abstracts** had been processed with LLMs, more than 200,000 papers a year. The share varies:
  - about 5% for UK and Australian authors
  - about 20% for authors in China, South Korea and Taiwan, and for computational biology
  - 20–25% at the publishers MDPI and Frontiers and the journal *Cureus*
- **Liang et al.** fitted a statistical model of word use to 1.12 million arXiv, bioRxiv and Nature-group papers ([Liang et al.](https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf); [code](https://github.com/Weixin-Liang/Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Papers)). By September 2024 they estimated that 7.7% of sentences in mathematics abstracts and 8.9% in Nature-group journals were LLM-modified. Their method found 2.4–3.4% even before ChatGPT existed, which is its false-positive floor.

**Other studies:**

- **Bao et al.** estimated that about 12.6% of arXiv, bioRxiv and medRxiv preprints used ChatGPT by August 2023. The share was 7.7 percentage points higher in countries where ChatGPT was restricted ([Bao et al.](https://arxiv.org/abs/2406.11583)).
- **Kusumegi et al.** linked detected LLM adoption to the output of 168,553 authors on arXiv, bioRxiv and SSRN ([Kusumegi et al., Science](https://arxiv.org/pdf/2601.13187)):
  - adopters' output rose 36.2%, 52.9% and 59.8% respectively, compared with similar non-adopters
  - the rise reached 89% for Asian-named authors at Asian institutions
  - complex writing predicts publication for papers written by people alone, but predicts it negatively for papers written with LLM help
- **Renault et al.** showed that dating an author's adoption from their first flagged paper mechanically creates positive effects. Kusumegi et al.'s reply keeps a positive association under four alternative designs. So the direction of the effect is better established than its size ([Renault et al.](https://arxiv.org/abs/2605.17979); [reply](https://arxiv.org/abs/2607.28968)).
- **Hao et al.** found that natural scientists who use AI as a research method publish 3.02 times as many papers. That answers a different question and belongs in a separate analysis ([Hao et al.](https://arxiv.org/pdf/2412.07727v4)).

Estimates specific to the social sciences now exist for economics journals, sociology abstracts and SSRN (see the SSH section). Nothing yet measures LLM use across the humanities beyond counts of LLM words, and nothing measures it in books.

**Grant texts carry the same signal:**

- **Qian et al.** analysed 5,700 confidential NSF and NIH proposals from two universities, plus 131,000 public awards (2021–2025) ([Qian et al., PNAS](https://arxiv.org/pdf/2601.15485v3)). They found:
  - The share of LLM-written text was flat until late 2022 and rose sharply from 2023.
  - Heavier LLM use went with less distinctive ideas.
  - At NIH only, it went with a funding probability about 4 percentage points higher and about 5% more publications, none of them highly cited ones.
- **Naser** found that LLM marker words in funded abstracts rose after ChatGPT by 51.9% at NSF, 27.3% at NIH and 53.6% at UKRI ([Naser](https://arxiv.org/pdf/2609.13241)).
- **Public award abstracts** are free through NIH RePORTER and the NSF Awards API. In new NIH awards, "delve" rose from 6.5 uses per 10,000 abstracts in FY2021 to 35.1 in FY2024 ([NIH RePORTER API](https://api.reporter.nih.gov/v2/projects/search)).

**Peer review outside machine learning:**

- Shen and Wang classified about **12% of 2025 *Nature Communications* reviews** as AI-generated ([Shen & Wang](https://arxiv.org/abs/2602.00319)).
- The American Association for Cancer Research (AACR), using a commercial detector, flagged LLM text in 23% of 2024 abstract submissions and 5% of peer-review reports across ten journals. Fewer than a quarter of authors disclosed using AI ([InfoDocket summary of Nature](https://www.infodocket.com/2025/09/11/report-ai-tool-detects-llm-generated-text-in-research-papers-and-peer-reviews/)).
- Liang et al. found no significant rise in Nature-group reviews through 2023 ([Liang et al. 2024](https://arxiv.org/abs/2403.07183)).
- Studies of machine-learning conference reviews are secondary evidence. At ICLR, the share went from about 11% of review text modified by LLMs in 2024 to about 20% of reviews classified as AI-generated in 2025 ([Shen & Wang](https://arxiv.org/abs/2602.00319)).

**Surveys trace the adoption curve rather than levels:**

- Wiley: the share of researchers using AI for research and publication rose from 45% to 62% between 2024 and 2025 ([Wiley](https://newsroom.wiley.com/press-releases/press-release-details/2025/AI-Adoption-Jumps-to-84-Among-Researchers-as-Expectations-Undergo-Significant-Reality-Check/default.aspx)).
- Elsevier: from 37% to 58% ([Elsevier](https://www.elsevier.com/about/press-releases/elseviers-global-survey-of-3-000-researchers-reveals-less-than-half-have)).
- *Nature*'s 2025 survey: 28.7% had used AI to edit their papers, and 18.4% did so without disclosing it ([Nature 2025](https://www.nature.com/articles/d41586-025-01463-8)).

**Every instrument has a validity problem that a time series makes worse:**

- Tools that judge individual documents flagged essays by non-native English writers as AI-written 61% of the time, on average across seven tools ([Liang et al. 2023](https://arxiv.org/abs/2304.02819)).
- Marker words drift once they are publicised. In PubMed, the rate of "delve" per abstract fell 51% from 2024 to 2025 while "underscore" rose 70% (computed from E-utilities). A word list frozen in 2024 therefore understates use in 2025–26 ([E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=underscor%2A%5Btiab%5D+AND+2025%5Bdp%5D); [Geng & Trotta](https://arxiv.org/abs/2502.09606)).

**A robust approach:**

1. Re-run the search for over-used words each year, against a fixed baseline from before ChatGPT.
2. Recalibrate the statistical estimators with current models.
3. Subtract the pre-2022 false-positive floor.
4. Report the results as lower bounds.
5. Use 2019–2021 as placebo years, where the measured effect should be zero.
6. Cross-check against the integrity signals below.

Commercial detectors such as Pangram and GPTZero are closed, frequently re-versioned and validated only by their vendors. They suit flagging individual documents, not building a reproducible series.

### Integrity signals give the most specific evidence

Fabricated references and leftover chatbot text are rarer than LLM-styled prose, but far more specific to unchecked LLM use.

**Fabricated references:**

- An audit of 97.1 million references in about 2.5 million PubMed-indexed papers found papers with fabricated references at a rate of **1 in 2,828 in 2023, 1 in 458 in 2025 and 1 in 277 in early 2026** ([Retraction Watch on Topaz et al., Lancet](https://retractionwatch.com/2026/05/07/one-in-277-pubmed-indexed-papers-in-2026-shows-fabricated-references-says-analysis/); [Lancet](https://doi.org/10.1016/S0140-6736%2826%2900603-3)).
- Zhao et al. estimated 146,932 hallucinated citations in 2025 across arXiv, bioRxiv, SSRN and PubMed Central. SSRN had the highest rate. Submissions that arXiv rejected had a rate of 2.2%, 4.5 times that of accepted ones ([Zhao et al.](https://arxiv.org/pdf/2605.07723)). That shows data on rejected submissions exist, even though arXiv does not publish them.

**Formulaic papers built on open datasets** are concentrated and measurable:

- Papers on the US health survey NHANES that link a single factor to an outcome went from about 4 a year (2014–2021) to 190 between January and early October 2024 ([Suchak et al., PLOS Biology](https://pmc.ncbi.nlm.nih.gov/articles/PMC12061153/)).
- Nine open health datasets yielded 23,005 papers in 2025, 11,577 more than a forecast from past trends predicted. Since 2022, work affiliated with China grew 4.2-fold, against 1.9-fold elsewhere ([Spick et al.](https://doi.org/10.1016/j.jclinepi.2026.112203)).
- Papers mining FAERS, the US drug-safety reporting database, rose from about 100 (2021) to about 600 (2024) ([Retraction Watch](https://retractionwatch.com/2025/09/16/exclusive-journal-bans-drug-safety-database-papers-as-they-flood-the-literature/)).

**Retractions.** The Retraction Watch database covers all disciplines and is free and updated daily through Crossref. It has no retraction reason specific to LLMs, and only three records mention ChatGPT or LLMs (computed from the October 2026 file) ([Retraction Watch data](https://gitlab.com/crossref/retraction-watch-data)).

| Instrument | What it measures | Disciplines and coverage | Access and cost | Validity caveats |
|---|---|---|---|---|
| [Over-used words (Kobak)](https://github.com/berenslab/llm-excess-vocab) | Lower bound on the share of abstracts processed with LLMs | Biomedicine: PubMed 2010–2024 (monthly to mid-2025) | MIT-licensed code; free PubMed baseline | Cannot separate LLM use from people adopting LLM words; marker words drift |
| [Statistical word-use model (Liang)](https://github.com/Weixin-Liang/Mapping-the-Increasing-Use-of-LLMs-in-Scientific-Papers) | Share of sentences modified by LLMs | Mathematics, physics, computing, electrical engineering, life sciences: arXiv, bioRxiv and Nature-group journals, 2020–Sep 2024 | Open code; Kaggle arXiv snapshot; bioRxiv API | False-positive floor of 2–3% before ChatGPT; biased at the extremes; needs recalibrating for each model generation |
| [SSH estimates (Cao](https://doi.org/10.1177/23780231261460657); [Feyzollahi & Rafizadeh](https://doi.org/10.1016/j.econlet.2025.112265); [Kousha & Thelwall)](https://doi.org/10.1007/s11192-026-05601-5) | Share of LLM-modified sentences (sociology); share of AI-typical words (economics); growth of LLM words by field | Sociology abstracts in OpenAlex 2018–2025; 25 top economics journals; six databases 2015–2024 | Published papers; methods described in them | Different measures give different answers for SSH; humanities barely covered |
| [Productivity after adoption (Kusumegi)](https://arxiv.org/pdf/2601.13187) | Change in output after detected adoption | STEM, life sciences and social sciences: arXiv, bioRxiv, SSRN, 2018–mid-2024 | Data availability not verified | Bias from dating adoption by the first flagged paper |
| [Grant text (Qian](https://arxiv.org/pdf/2601.15485v3); [Naser)](https://arxiv.org/pdf/2609.13241) | LLM share or marker-word rate in proposals and awards | NIH, NSF (including SBE) and UKRI (including AHRC, ESRC), 2017–2026 | RePORTER and NSF APIs free; proposals need data-use agreements; Dimensions data is commercial | Funded awards only; abstracts of continuing grants reuse old text |
| [Fabricated references (Topaz](https://retractionwatch.com/2026/05/07/one-in-277-pubmed-indexed-papers-in-2026-shows-fabricated-references-says-analysis/); [Zhao)](https://arxiv.org/pdf/2605.07723) | Non-existent or unmatched references, above the normal error rate | Biomedicine (2.5M PubMed papers); arXiv, bioRxiv, SSRN and PMC, 2020–2025 | Can be replicated by matching references against OpenAlex and Semantic Scholar | Errors when extracting references; peripheral vs essential references |
| [Open-dataset floods (Suchak](https://pmc.ncbi.nlm.nih.gov/articles/PMC12061153/); [Spick)](https://doi.org/10.1016/j.jclinepi.2026.112203) | Formulaic papers on public datasets, above trend | Health: NHANES, FAERS, UK Biobank, GBD and others, 2014–2025 | OpenAlex and PubMed queries | LLM role inferred from timing and form, not measured |
| [Leftover chatbot phrases](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22as%20an%20AI%20language%20model%22%20AND%20PUB_YEAR:2025&format=json&resultType=idlist) | Phrases such as "as an AI language model" left in papers | Mostly biomedicine: Europe PMC full text from 2021; the Academ-AI catalogue lists 768 cases | Free | Small counts; some hits are legitimate quotations |
| [Retraction Watch](https://gitlab.com/crossref/retraction-watch-data) | Retractions and their reasons | All disciplines; decades; updated daily | Free CSV via Crossref | No LLM reason code; coding lags |
| [Peer-review text](https://arxiv.org/abs/2602.00319) | AI-generated share of peer reviews | Multidisciplinary science: *Nature Communications* 2022–2025; cancer research: AACR 2021–2024 | Open code (Shen & Wang); commercial tool (AACR) | Few venues; validated by vendors |
| [Researcher surveys](https://www.nature.com/articles/d41586-025-01463-8) | Self-reported AI use | Multidisciplinary samples, 2023–2026 | Free reports; raw data from *Nature* | Samples not comparable across surveys; undisclosed use |

### Every confounder has a date

LLM exposure arrived in waves, not on a single date:

1. ChatGPT (30 November 2022), then GPT-4 and Claude (March 2023)
2. reasoning and "deep research" tools: OpenAI's o1 (September 2024), DeepSeek-R1 (20 January 2025), OpenAI Deep Research (February 2025)
3. GPT-5, Gemini 3 and Claude Opus 4.5 (August–November 2025)
4. Prism, OpenAI's free LaTeX workspace for writing papers (late January 2026)

([Wikipedia: ChatGPT](https://en.wikipedia.org/wiki/ChatGPT); [Wikipedia: list of LLMs](https://en.wikipedia.org/wiki/List_of_large_language_models); [Wikipedia: Claude](https://en.wikipedia.org/wiki/Claude_%28language_model%29); [DeepSeek](https://api-docs.deepseek.com/news/news250120); [OpenAI Prism](https://openai.com/index/introducing-prism/))

Each wave overlaps the shocks and rule changes below. Every model should include them as dated events.

| Date | Shock or rule change | Series it distorts | Source |
|---|---|---|---|
| 2020–2021 | COVID-19 surge: PubMed records +15.7% in 2020; medRxiv went from 913 papers (Jun–Dec 2019) to 14,070 (2020) | All volume series; inflated baseline | [E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&rettype=count&term=2024%5Bdp%5D); [medRxiv API](https://api.biorxiv.org/details/medrxiv/2019-06-01/2019-06-30/0) |
| Feb 2020 | China stops judging researchers by their count of papers in SCI-indexed journals, and stops publication bonuses | Chinese output and choice of journal | [THE](https://www.timeshighereducation.com/node/689974) |
| 2021; 25 Aug 2022; 1 Jul 2025 | Plan S open-access mandate; US OSTP memo requiring federally funded papers to be free immediately; NIH public-access policy | Open-access volumes; PMC deposits and the make-up of PubMed | [cOAlition S](https://www.coalition-s.org/plan_s_principles/); [OSTP](https://bidenwhitehouse.archives.gov/ostp/news-updates/2022/08/25/ostp-issues-guidance-to-make-federally-funded-research-freely-available-without-delay/); [NIH](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-101.html) |
| Sep 2022–2024 | Mass retractions and journal closures at Hindawi; retractions in the Retraction Watch database peaked at 13,298 in 2023 | Open-access special issues; retraction series | [Retraction Watch](https://retractionwatch.com/2023/12/06/wiley-to-stop-using-hindawi-name-amid-18-million-revenue-decline); [RW data](https://gitlab.com/crossref/retraction-watch-data) |
| Mar 2023 | Web of Science drops about 50 journals, including MDPI's IJERPH | Counts based on Web of Science | [Chemistry World](https://chemistryworld.com/news/sanctioning-of-50-journals-raises-concerns-over-special-issues-in-mega-journals/4017315.article) |
| 2020–2022; 2024 | MEDLINE indexing automated; MTIX neural indexer introduced | Field shares based on MeSH subject headings | [NLM](https://www.nlm.nih.gov/bsd/indexfaq.html) |
| Jan 2023 | Phase 2 of NIH's Preprint Pilot adds preprints to PubMed | PubMed totals | [NCBI Insights](https://ncbiinsights.ncbi.nlm.nih.gov/2023/01/09/next-phase-preprint-pilot/) |
| Calls from late 2023 (2024 work programme) | UK rejoins Horizon Europe | ERC and MSCA applications | [UKRI](https://www.ukri.org/apply-for-funding/horizon-europe/) |
| Oct 2023 | Norway's FRIPRO programme drops fixed deadlines and accepts applications on a rolling basis | Applications to the Research Council of Norway | [UiB analysis](https://ekstern.filer.uib.no/ledelse/Analysegruppen%20-%20nyhetsbrev/Analysegruppa-teikn-og-tal-i-tida-nr68.pdf) |
| Oct 2023–Jul 2026 | The UK's national theses service (EThOS) is offline after a cyberattack | UK thesis counts | [EThOS](https://ethos.bl.uk/); [Stirling library news](https://isnews.stir.ac.uk/2026/07/13/ethos-is-back/) |
| 1 Jan 2024 | UK bars dependants for most international students | UK demand for master's courses | [Home Office](https://www.gov.uk/government/statistics/monthly-entry-clearance-visa-applications-july-2026/monthly-entry-clearance-visa-applications-july-2026) |
| 13 Mar 2024 | Crossref announces it will remove its subject codes | Crossref counts split by discipline | [Crossref blog](https://www.crossref.org/blog/subject-codes-incomplete-and-unreliable-have-got-to-go/) |
| 2024 | NSFC allows resubmission after two consecutive failures | NSFC applications (+26% in 2024) | [RoRI data](https://media.nature.com/original/magazine-assets/d41586-026-01297-y/52331462) |
| 2025 Discovery Projects round (run in 2024) | ARC adds an expression-of-interest stage | ARC applications | [ARC](https://www.arc.gov.au/funding-research/funding-outcome/selection-outcome-reports/dp25-selection-report-funding-commencing-2025) |
| 7 Feb 2025 | NIH attempts a 15% cap on indirect costs | US applications | [NIH](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-068.html) |
| Apr 2025 | GRFP awards cut; second-year graduate students excluded | GRFP applications and awards | [AIP FYI](https://www.aip.org/fyi/nsf-graduate-research-fellowships-expected-to-fall-next-year) |
| Apr 2025 | OSF preprint servers (SocArXiv, PsyArXiv, EdArXiv) start listing each version of a paper as a separate record | SSH preprint counts | [SocArXiv news](https://socopen.org/news-and-essays) |
| Apr–Sep 2025 | NEH terminates about 1,477 grants and cuts close to 70% of its staff; its FY2026 budget request (May 2025) proposes closing the agency | US humanities applications and fellowships | [NEH FY2025 report](https://www.neh.gov/sites/default/files/NEH%20FY2025%20PAR%20to%20OMB.pdf); [NEH FY2026 request](https://www.humanities.gov/sites/default/files/NEH%20FY%202026%20Congressional%20Justification.pdf) |
| 5 May 2025 | EU "Choose Europe" package worth €500M to attract researchers | ERC and MSCA applications | [Bloomberg](https://www.bloomberg.com/news/articles/2025-05-05/eu-to-propose-500m-package-to-attract-researchers) |
| 25 Sep 2025 | NIH limits each investigator to six applications a year | NIH applications | [NIH](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html) |
| 1 Oct–12 Nov 2025 | US government shutdown; NIH reschedules all October–November deadlines | NIH counts by submission date | [NIH](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-005.html) |
| Oct 2025 | AI bots start inflating RePEc's usage statistics | Economics download and view counts | [LogEc](https://logec.repec.org/) |
| Oct 2025 competition | SSHRC raises the maximum amounts Insight Grant applicants may request | SSHRC applications | [SSHRC](https://sshrc-crsh.canada.ca/en/funding/opportunities/insight-grants/2025/competition.aspx) |
| Nov 2025 | OpenAlex "Walden" rebuild | OpenAlex counts (+3.2% for 2024) | [Haupka](https://rogue-scholar.org/records/nj8nj-9f827) |
| 19–27 Nov 2025 | SocArXiv requires ORCID identifiers, redirects humanities papers to Knowledge Commons and pauses papers on AI topics | SocArXiv and Knowledge Commons counts | [SocArXiv](https://socopen.org/category/announcements/) |
| 1 Dec 2025 | bioRxiv and medRxiv switch to DOI prefix 10.64898 | Crossref counts by DOI prefix | [openRxiv](https://connect.biorxiv.org/news/2025/11/18/preprint_dois) |
| 10 Dec 2025–1 Oct 2026 | arXiv endorsement, English-version and rate-limit rules | arXiv counts in all archives | [arXiv](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/) |
| 16 Dec 2025 | US restricts entry from 39 countries | US international applications | [NAFSA](https://www.nafsa.org/sites/default/files/media/document/Fall_2026_International_Student_Economic_Snapshot_NAFSA_JBI.pdf) |
| Jan 2026 | NIH stops relying on fixed funding cut-offs (paylines) | How investigators decide whether to apply | [NIH](https://grants.nih.gov/news-events/nih-extramural-nexus-news/2025/11/implementing-a-unified-nih-funding-strategy-to-guide-consistent-and-clearer-award-decisions) |
| Apr 2026 | SNSF limits applications per person; ERC restricts resubmissions for 2027 | SNSF and ERC applications | [SNSF](https://www.snf.ch/en/9EcyLcUUpkxVDGmp/news/); [ERC](https://erc.europa.eu/news-events/news/erc-president-explains-stricter-application-measures-amid-rising-demand-funding) |
| Jul 2026 | JPART caps submissions per author (1 Jul); Wellcome moves to rolling deadlines and selects at random when applications exceed a threshold (14 Jul) | JPART submissions; Wellcome applications | [JPART](https://www.gopmra.org/assets/Secretariat/Policies/jpart-submission-cap-policy.pdf); [Wellcome](https://wellcome.org/insights/articles/rethinking-future-research-funding) |
| Aug 2026 | *Philosophy & Public Affairs* bans submissions substantially written by AI | Philosophy journal submissions | [Daily Nous](https://dailynous.com/2026/08/24/after-experiment-journal-decides-to-prohibit-ai-authored-content/) |
| 25 Aug 2026 | NSF's FY2027 GRFP call drops the SBE directorate and STEM-education research | GRFP applications by field | [AIP FYI](https://www.aip.org/fyi/nsf-graduate-research-fellowships-expected-to-fall-next-year) |
| 6 Oct 2026 | OpenAlex re-assigns the topic of every work | OpenAlex field shares | [OpenAlex](https://blog.openalex.org/same-topics-better-assignments/) |

### Long histories exist for papers and grants, not scholarships

Interrupted time series need enough history before LLMs to estimate the trend and seasonal pattern while leaving out 2020–21. That history exists for papers and grants, including several SSH series. It barely exists for graduate admissions and not at all for fellowship applicants.

| Question | Longest public series | Starts | Usable window before LLMs |
|---|---|---|---|
| Papers posted (physics, mathematics, statistics, economics, quantitative biology) | arXiv by primary archive | Jul 1991, monthly | 2000–2019, leaving out 2020–21 |
| Papers posted (economics) | NBER working papers | 1970s | 2000–2019 |
| Papers posted (sociology, psychology, education) | SocArXiv, PsyArXiv, EdArXiv via the OSF API | 2017 | 2017–2022, while the servers were still being adopted |
| Papers deposited (SSH, France) | HAL, by domain | 2016 or earlier | 2016–2022, with a bulk import in 2019 |
| Papers indexed (education) | ERIC | 1995 or earlier | 2014–2019, after a 2012–2014 drop |
| Papers posted (life and health sciences) | bioRxiv; medRxiv | Nov 2013; Jun 2019 | 2019–2022 only |
| Papers published (biomedicine) | PubMed or Europe PMC (MEDLINE-sourced) | Before 1947; MEDLINE 1966 | 2010–2019 |
| Papers published (all disciplines, inclusive) | Crossref journal articles and chapters; OpenAlex snapshot | Early 1900s | 2010–2019, on a fixed set of journals |
| Papers published (science and engineering, curated) | NCSES/Scopus | 2003 | 2003–2019, with a two-year lag |
| Papers submitted | RELX/Elsevier | 2021 (verified) | None |
| Grant applications (biomedicine) | NIH Table 218 | FY1970 | FY1998–2019 |
| Unique grant applicants | NIH Data Book report 164 | FY1998 | FY1998–2019 |
| Grant applications (all disciplines, outside the US) | KAKENHI; ERC; UKRI | FY1996; 2007; 2015-16 | 1996–2019; 2007–2020; 2015-16 to 2019-20 |
| Grant applications (social sciences and humanities) | UKRI AHRC and ESRC; ERC SSH domain | 2015-16; 2007 calls | 2015-16 to 2019-20; 2007–2020 |
| Grant applications (SSH, Canada) | SSHRC Insight Grants | Oct 2021 competition | 2021–2022 only |
| Grant applications (US humanities) | NEH budget documents and annual reports | FY2016–2024 documents not yet extracted | Up to FY2024; series broken from FY2025 |
| Graduate applications (all fields, including business and the social sciences) | CGS/ETS GE&D | 1986 | Up to fall 2022, using institutions that responded in consecutive years |
| Fellowship applicants | NSF GRFP | Awards 1952; applications patchy | Applications for 2016–2021 only |
| Researcher and doctorate denominators | NSF SED; OECD, UIS, Eurostat | 1958; varies | Full |

### Six designs that separate LLM effects from confounders

| Design | Data | What it isolates | Main threat and mitigation |
|---|---|---|---|
| Interrupted time series with several possible break dates | arXiv non-computer-science archives (2000–Nov 2025), bioRxiv (from 2019), PubMed by entry date, Crossref on a fixed set of journals, NIH, KAKENHI, UKRI councils | Whether and when growth departs from its 2010–2019 trend | COVID, open-access and integrity shocks: leave out 2020–21, add each dated break, test placebo dates and seasonality |
| Dose-response comparison: did growth rise more where LLM use is higher? (difference-in-differences) | Volume by discipline (arXiv archive, UKRI council, ERC domain, NSF directorate, HAL domain, journal field), by country and year, with the LLM share re-estimated for each group (Kobak or Liang methods; marker words in grant texts). HAL compares SSH and STEM on a single platform | Whether volume grows more where measured LLM use is higher | Shocks specific to a country (China's 2020 reform, paper mills) or a discipline (AI as a research topic): add country-by-year and discipline-by-year effects; drop AI-topic categories |
| Author panels, with adoption dated in a separate window | Author records from arXiv, bioRxiv, SSRN and OpenAlex | Change in each person's output after adopting LLMs | Bias from dating adoption by the first flagged paper: date adoption outside the window where output is measured; add comparison groups from before 2022 |
| Splitting growth into people and intensity | NIH applications vs unique applicants (reports 20, 164, 303); LSAC; fellowship funnels | More people applying vs more applications per person | Funding shocks move both: compare grant mechanisms, career stages and activity codes exempt from the cap |
| Policy changes as natural experiments | NIH cap (training, conference and research-education grants exempt); arXiv rate limit (applies to submitters, not co-authors); SNSF and ERC rules; JPART cap; SocArXiv rules (Nov 2025); *Philosophy & Public Affairs* ban (Aug 2026); Italy's temporary 2023 ChatGPT ban (economics) | How strongly volume responds to the cost of submitting or to access to LLMs; size of the group of heavy submitters | Simultaneous US shocks: compare within the same funder or journal. Displacement to uncapped outlets: measure against system-wide totals (HAL, OpenAlex) |
| Funders with volume limits vs funders without | NSFC and KAKENHI (per-person limits) vs MSCA, ERC, UKRI councils, SNSF, CIHR | Whether funders without volume limits grew faster after 2022 | Budget, eligibility and Horizon-Europe-membership shocks: add terms for each funder's events |

No single design is sufficient. A credible LLM effect should show up in four places at once:

1. volume above trend in the groups with the highest LLM use
2. more papers or applications per person
3. rising integrity signals in the same groups
4. a drop in volume when caps raise the cost of submitting

The same discipline applies to handling the data:

- Pin every version: the OpenAlex snapshot date, the Crossref data-file year and the PubMed baseline.
- Strip version suffixes from DOIs.
- Align grant data to deadline dates, not call names or decision years.
- Treat 2020–21 as a separate period.
- Report every result by discipline, so that STEM-heavy sources do not stand in for academia.
- Measure exposure in several ways (LLM-word counts, estimated shares of LLM-modified sentences, output per person, submissions), because the social sciences and humanities look different under each.

## Conclusion

The deepest problem is that the measuring instruments now react to the thing being measured. Every institution that faced a surge in the LLM era answered with caps, rate limits, scope rules, bans or eligibility rules: arXiv, NIH, the ERC, SNSF, SocArXiv, JPART, *Philosophy & Public Affairs* and Wellcome. From late 2025 onward, the public counts of postings, submissions and applications therefore hide exactly the extra volume LLMs generate. The signal is moving into rejections, desk rejections, withdrawals and support tickets, which almost nobody publishes. Zhao et al.'s analysis of submissions arXiv rejected shows such data exist. The most valuable next step is therefore not another public series but negotiated access to data on attempted submissions:

- arXiv's moderation outcomes
- publishers' totals from their manuscript systems
- how many applications each NIH investigator submits
- aggregated AI disclosures from Rhodes applicants

The second lesson is to stop looking for the effect in totals and in STEM alone. The documented LLM footprint is concentrated:

- among authors writing in a second language
- in a handful of open datasets
- at particular publishers
- in a small group of heavy submitters
- among SSRN's social scientists, who show the largest productivity gains and the highest hallucinated-citation rate of any corpus studied so far
- in empirical and applied social-science subfields and less prestigious journals

How exposed the social sciences and humanities look depends on the yardstick. Counts of LLM words make them look less exposed than STEM. Output and submission measures make them look as exposed or more. The humanities have the weakest measured signals and the thinnest instruments, yet SocArXiv and philosophy journals report AI-generated floods concentrated there. Absence of evidence is not yet evidence of absence.

A design that looks for an even rise in total output after 2022 will understate the effect where it exists. Where it does not exist, the same design will mistake COVID rebounds, open-access growth and funding shocks for an LLM effect. The policy changes of 2025–2026, compared discipline by discipline, offer a cleaner test than ChatGPT's release date.
