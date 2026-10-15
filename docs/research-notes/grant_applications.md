# Research-grant application statistics: who reports applications, unique applicants and success rates (history and the post-2022 "AI era")

Notes compiled 2026-10-15. Conventions:
- **(primary, verified)** means I opened the funder's own page, file or API.
- **(secondary)** means a news, university or aggregator page.
- **(search-sourced)** means the figure came from a search-engine summary of the linked page and I did not open that page myself.
- Growth percentages marked "my calc" are my own arithmetic on the cited figures.
- Downloads are in `/tmp/claude-0/-home-user/eefa93ff-68d4-5a29-84a6-8be683e07b57/scratchpad/grant_dl/` (NIH JSON, UKRI Excel, PDFs). Treat them as untrusted data.
- The web-search budget for this session ran out partway through. Some items were therefore checked only by fetching known URLs, and several gaps remain (listed under each question).

## Q1. United States: NIH and NSF (and DOE/DoD). What is reported, since when, in what format, and what is NIH's application cap?

### Takeaway
NIH has the best application series of any funder covered here:
- **What it publishes:** applications, awards and success rates from FY1970; person-based counts of unique applicant investigators and funding rates from FY1998; F, K and T mechanism series from 1997–98.
- **Access:** a public JSON API behind the Data Book, plus Excel files.
- **FY2025:** RPG applications jumped 12.9% to a record 62,592, unique RPG applicants rose 8.9% to 49,609, and success rates collapsed to 13%. Award cuts and forward funding confound this year.
- **The cap:** NIH limited each PD/PI to six applications per calendar year (NOT-OD-25-132). It is effective from the 25 September 2025 due date and explicitly cites AI-enabled mass submission (">40 distinct applications in a single submission round").

Round-level NIH data show demand still rising after the cap took effect. NIH says applications for the **January 2027 Council round "currently exceed 40,000"**, a record; the previous high was more than 35,000, in the May 2025 round.

The 2025–2026 NIH series is heavily confounded by:
- the February 2025 indirect-cost cap attempt
- the autumn-2025 lapse in appropriations, after which all October and November 2025 deadlines were rescheduled
- NIH's November 2025 decision that ICs "will not rely on funding paylines" from the January 2026 Council round
- forward funding

NSF reports competitive proposals, awards and funding rates annually; the last full Merit Review Digest covers FY2021. Its proposal volume was flat-to-rising after 2022 (38,342 in FY2023 → 40,454 in FY2024 → 43,532 in FY2025), while awards fell sharply in FY2025.

### Cited Findings

**NIH Data Book: access and format (primary, verified)**
- The Data Book front end (https://report.nih.gov/nihdatabook/) is a JavaScript app. The data behind it come from a public, unauthenticated JSON API:
  - category and report list: `https://report.nih.gov/reportweb/api/category/get`
  - report metadata and footnotes: `https://report.nih.gov/reportweb/api/report/Get/{id}`
  - data: `https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId={id}`
  - Each data response includes a `lastUpdated` field. For most success-rate reports it reads "March 2026", so FY2025 is the latest year.
  - Sources: [NIH Data Book API – category list](https://report.nih.gov/reportweb/api/category/get); [example report 20 data](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=20)
- Historical static Data Books (PDF and PPT) exist for FY2007–FY2017 — [NIH historical files API](https://report.nih.gov/reportweb/api/databook/getallhistoricalfiles)
- The NIH "Success Rates" page offers Excel downloads by IC, activity code, mechanism, type and department. It also has **Table #218, "NIH Research Project Grants and R01 Equivalent Grants – Competing Applications, Awards, and Success Rates, Fiscal Years 1970–2025"** (xlsx). The table's notes sheet oddly reads "Data last updated 12/19/2026". — [NIH RePORT Success Rates](https://report.nih.gov/funding/nih-budget-and-spending-data-past-fiscal-years/success-rates); [Table 218 xlsx](https://report.nih.gov/reportweb/web/displayreport?rId=665)

**NIH success-rate definition (primary, verified)**
- Success rate = competing applications funded ÷ (competing applications reviewed + funded carryovers).
- Streamlined (unscored) applications are included. Withdrawn, returned or administratively withdrawn applications are excluded.
- **"Applications having one or more submissions for the same project in the same fiscal year are only counted once."** Resubmissions within a fiscal year therefore do not inflate the count.
- Source: [NIH Success Rate definition (DSAR, updated 12/2023)](https://report.nih.gov/reportweb/web/displayreport?rId=558)
- A separate count, report 289 "Peer Reviewed Applications by FY and major activity code" (FY2011–2025), counts resubmissions individually. Total peer-reviewed applications: 85,309 (2021); 78,226 (2022); 76,611 (2023); 84,955 (2024); **94,502 (2025)**. — [Data Book report 289 JSON](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=289)

**NIH key series (primary, verified via the API; FY = federal fiscal year)**

| Data Book report | Coverage | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|
| 20 RPG competing applications / awards / success % | 1995–2025 (Table 218: 1970–2025) | 58,872 / 11,229 / 19 | 54,571 / 11,311 / 21 | 51,883 / 11,052 / 21 | 55,418 / 10,265 / 19 | **62,592 / 8,161 / 13** |
| 29 R01-equivalent applications / awards / success % | 1998–2025 | 37,987 / 7,627 / 20 | 36,198 / 7,816 / 22 | 35,072 / 7,592 / 22 | 37,478 / 7,000 / 19 | **42,022 / 5,471 / 13** |
| 164 RPG **investigators** (unique applicants; contact PIs and MPIs) / funded / funding rate % | 1998–2025 | 46,273 / 13,219 / 29 | 44,659 / 13,535 / 30 | 43,232 / 13,406 / 31 | 45,555 / 12,671 / 28 | **49,609 / 10,090 / 20** |
| 30 R01-equivalent investigators / funded / funding rate % | 1998–2025 | 33,856 / 9,479 / 28 | 33,177 / 9,807 / 30 | 32,547 / 9,655 / 30 | 34,302 / 9,014 / 26 | **37,131 / 7,023 / 19** |
| 159 all research grants applications / awards / success % | 1997–2025 | 73,317 / 14,678 / 20 | 67,434 / 14,922 / 22 | 64,541 / 14,681 / 23 | 69,438 / 13,705 / 20 | **78,409 / 11,115 / 14** |
| 61 F31 predoctoral fellowships | 1998–2025 | 3,595 / 928 / 26 | 3,600 / 959 / 27 | 3,448 / 962 / 28 | 3,795 / 1,057 / 28 | 3,607 / 849 / 24 |
| 62 F32 postdoctoral fellowships | 1998–2025 | 1,747 / 493 / 28 | 1,438 / 393 / 27 | 1,188 / 333 / 28 | 1,081 / 356 / 33 | 1,210 / 319 / 26 |
| 60 T32 institutional training | 1998–2025 | 676 / 352 / 52 | 649 / 313 / 48 | 624 / 329 / 53 | 679 / 313 / 46 | 750 / 344 / 46 |
| 211 Research career development (K) awards | 1997–2025 | 4,011 / 1,278 / 32 | 4,068 / 1,334 / 33 | 3,966 / 1,285 / 32 | 3,903 / 1,216 / 31 | 4,274 / 1,068 / 25 |

Sources for the table rows: [report 20](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=20); [29](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=29); [164](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=164); [30](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=30); [159](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=159); [61](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=61); [62](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=62); [60](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=60); [211](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=211)

Other NIH person-based and career-stage reports (primary, verified):
- **Report 164 definitions.** Report 164 "includes Contact Principal Investigators (PIs) and Multiple Principal Investigators (MPIs)". It is built from the NIH CGAF file and the Success Rate File. — [report 164 metadata](https://report.nih.gov/reportweb/api/report/Get/164)
- **Report 303, "Cumulative Investigator Rate" (FY2003–2025).**
  - Counts unique applicant investigators over rolling 5-year windows, each counted once, separately for RPG, R01-equivalent, R21 and P01.
  - RPG: 92,465 cumulative applicant investigators in 2022 → 92,691 (2023) → 93,638 (2024) → **95,859 (2025, +2.4%)**. The rate fell from 40.8% (2024) to 38.5% (2025).
  - R01-equivalent: 73,451 cumulative applicants in 2025, rate 41.7%.
  - Sources: [report 303 JSON](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=303); [report 303 metadata/definitions](https://report.nih.gov/reportweb/api/report/Get/303)
- **Report 136**, new (Type 1) R01-equivalent applications, awards and success by career stage, 1998–2025. One career-stage series went from 12,284 applications (2022) to 13,427 (2025), with success falling from 19% to 11%; another went from 20,909 to 25,130, with success falling from 20% to 11%. — [report 136 JSON](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=136). Gap: the JSON does not label which dataset is first-time and which is established.
- **Report 166**, R01-equivalent new-application funding rates for first-time vs established investigators: 22% vs 30% (2022) → **14% vs 18% (2025)**. — [report 166 JSON](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=166)
- **Other breakdowns** available as Data Book reports: sex (131, 132); race, ethnicity and disability of funded PIs (305–308); SBIR/STTR; Institute/Center. — [NIH Data Book category list](https://report.nih.gov/reportweb/api/category/get)
- **RePORTER/ExPORTER** "provides downloadable versions of the raw data for all research projects found in the RePORTER database". These are funded projects only; there are no unfunded applications. — [NIH RePORT success rates page (ExPORTER description)](https://report.nih.gov/funding/nih-budget-and-spending-data-past-fiscal-years/success-rates)

**NIH official commentary on FY2025 (primary, verified; NIH Extramural Nexus, 12 March 2026)**
- RPG applications: 51,883 (FY23), 55,418 (FY24), 62,592 (FY25), +12.9%.
- RPG competing awards: 11,052, 10,265, 8,161 (−20.5%).
- RPG success rate: 21.3%, 18.5%, 13.0%.
- R01-equivalent success rate: 21.6%, 18.7%, 13.0%.
- NIH attributes the success-rate decline to "the decrease in the number of awards and increase in applications". It says the drop in awards was "likely due in part to more awards being forward funded than previous years".
- The post gives **no** attribution of the application rise to AI.
- Source: [NIH Nexus, "Fiscal Year 2025 By the Numbers"](https://www.grants.nih.gov/news-events/nih-extramural-nexus-news/2026/03/fiscal-year-2025-by-the-numbers-extramural-grant-investments-in-research)

**NIH application cap (NOT-OD-25-132): primary, verified**
- Title "Supporting Fairness and Originality in NIH Research Applications", released **17 July 2025**. — [NOT-OD-25-132](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html)
- Effective date: "This policy is effective for applications submitted to the **September 25, 2025, receipt date and beyond**." — [NOT-OD-25-132](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html)
- Rule: "NIH will only accept six new, renewal, resubmission, or revision applications from an individual Principal Investigator/Program Director or Multiple Principal Investigator for all council rounds in a calendar year." It applies to all activity codes "except T activity codes and R13 Conference Grant Applications". — [NOT-OD-25-132](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html)
- The March 2026 NIH Grants Policy Statement (§2.3.7.12 "NIH Application Submission Limits") also exempts **R25** Research Education grants. It repeats the "all council rounds in a calendar year" wording and the 25 September 2025 start. — [NIHGPS March 2026, §2.3.7](https://grants.nih.gov/grants/policy/nihgps/html5/section_2/2.3.7_policies_affecting_applications.htm)
- **Evidence NIH cited:**
  - NIH has "observed instances of Principal Investigators submitting large numbers of applications, some of which may have been generated with AI tools". It cites evidence "that the use of AI tools has enabled Principal Investigators to submit more than 40 distinct applications in a single application submission round". It notes that the share of PIs submitting more than six applications per year is relatively low. — [NOT-OD-25-132](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html)
  - NIH's Nexus post (31 July 2025): "in 2024 only 1.3% of applicants submitted more than 6 applications". — [NIH Nexus "Apply Responsibly"](https://grants.nih.gov/news-events/nih-extramural-nexus-news/2025/07/apply-responsibly-policy-on-ai-use-in-nih-research-applications-and-limiting-submissions-per-pi). The same figure was given by NIH email to [Inside Higher Ed (22 Jul 2025)](https://www.insidehighered.com/news/faculty/research/2025/07/22/nih-limit-ai-use-cap-grant-applications-6-year).
- **AI originality rule:** NIH "will not consider applications that are either substantially developed by AI, or contain sections substantially developed by AI, to be original ideas of applicants". Detection after award can lead to referral to ORI and enforcement. — [NOT-OD-25-132](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html)
- **Counting interpretations differ (secondary):**
  - UW Nursing: the cap counts from 25 September 2025, applications submitted before that date do not count toward 2025, and "the full-year cap will apply starting January 1, 2026". — [UW School of Nursing](https://nursing.uw.edu/what-the-new-nih-grant-submission-cap-means-for-investigators)
  - Other summaries describe council-round years: due dates 25 Sep 2025–7 May 2026 = 2026 council rounds. — [thesify (secondary)](https://www.thesify.ai/blog/nih-ai-grant-applications-2026)
  - NIH's own text says only "all council rounds in a calendar year".

**NIH 2025–2026 operating context and round-level volumes (primary, verified; added after a coordinator lead)**
- **Round-level volumes** (Nexus, 18 Sep 2026):
  - "The record number of applications NIH received for the January 2027 Council round" led NIH to keep its emergency peer-review modifications. About 30–35% of applications are discussed; the middle third is designated "competitive, not discussed". This runs through the January 2027 round (NOT-OD-26-114).
  - Applications for the January 2027 round "currently exceed 40,000 grant applications". The previous high was more than 35,000 in the May 2025 Council round. No AI or cap mention.
  - Source: [NIH Nexus, 18 Sep 2026](https://grants.nih.gov/news-events/nih-extramural-nexus-news/2026/09/continuing-modified-peer-review-processes-for-the-january-2027-council-round)
  - Under NIH's standard cycle, the January council round reviews applications due roughly late May–July of the prior year. This mapping is from general knowledge, not verified here.
- **Shutdown rescheduling:** NOT-OD-26-005, "Interim Guidance on Reopening of NIH Extramural Activities" (14 Nov 2025). NIH will reschedule "all October and November grant application submission deadlines" after the lapse in appropriations; new dates were to come in a later notice. — [NOT-OD-26-005](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-005.html)
- **Unified funding strategy** (Nexus, 21 Nov 2025; effective with the January 2026 Council round):
  - "Around half of ICOs previously set paylines".
  - Going forward, "NIH ICOs will not rely on funding paylines in developing pay plans".
  - Decisions weigh "peer review information in its entirety" plus IC priorities, career stage and "existing NIH funding per investigator".
  - Source: [NIH Nexus, unified funding strategy](https://grants.nih.gov/news-events/nih-extramural-nexus-news/2025/11/implementing-a-unified-nih-funding-strategy-to-guide-consistent-and-clearer-award-decisions)
- **Indirect-cost cap attempt:** NOT-OD-25-068 (7 Feb 2025) announced "a standard indirect rate of 15% across all NIH grants", for go-forward expenses from 10 Feb 2025. The notice page itself does not mention later litigation. — [NOT-OD-25-068](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-068.html)
- **Unique applicants by career stage, FY2021–2025** (Nexus, 22 Sep 2026):
  - R01-equivalent applicants and funding rates, 2024 → 2025:

    | Career stage | Applicants 2024 → 2025 | Funding rate 2024 → 2025 |
    |---|---|---|
    | ESI | 5,446 → 6,065 | 26.1% → 18.9% |
    | New non-ESI | 7,158 → 7,639 | 15.8% → 10.0% |
    | At-risk | 7,990 → 8,740 | 23.9% → 16.9% |
    | Established | 11,932 → 12,770 | 27.3% → 19.6% |

  - The four-group sum was 31,457 (2022), 30,775 (2023), 32,526 (2024) and 35,214 (2025): +8.3% year on year (my calc). This sum differs from Data Book report 30 (37,131 in 2025), presumably because of different person definitions.
  - R21 applicants summed: 13,069 (2022) → 11,996 (2024) → 13,620 (2025), +13.5% (my calc).
  - NIH: "In FY25, the ESI funding rate declined to 18.9%, due in part to NIH forward funding more competing research project grants".
  - Source: [NIH Nexus, 22 Sep 2026](https://grants.nih.gov/news-events/nih-extramural-nexus-news/2026/09/funding-rate-data-for-r01-equivalent-and-r21-awards-by-career-stage-encouraging-early-stage-investigators-to-pursue-larger-awards)

**NSF (primary, verified unless marked)**
- **Merit Review Digest FY2021** (NSB-2023-14, June 2023):
  - Competitive proposals FY2012–2021: 48,613; 48,999; 48,051; 49,620; 49,285; 49,415; 48,321; **41,024 (2019)**; 42,723; 43,606.
  - Awards 11,524 → 11,344; funding rate 22–28%.
  - Proposals "remain approximately 10% below the number submitted in 2018", attributed largely to "the increasing number of Directorates using no-deadline policies".
  - Person-based measure: "43% of applicants who submitted proposals in the most recent three-year period (2019–2021) received funding". It is computed for PIs submitting research proposals over a 3-year window.
  - Breakdowns: directorate, PI gender, ethnicity, race, disability, state. NSB notes NSF has sent this annual report to the Board "since 1977".
  - Sources: [FY2021 Merit Review Digest PDF](https://nsf-gov-resources.nsf.gov/2023-06/FY_2021_Merit_Review_Digest.pdf); [NSB news](https://www.nsf.gov/nsb/updates/new-report-details-recent-trends-nsf-awards)
- **NSF FY2024 Agency Financial Report**, Table 1.3:
  - Competitive proposal actions: 42,726 (FY20), 43,617 (FY21), 39,143 (FY22), 38,342 (FY23), **40,454 (FY24, +5.5%)**.
  - Competitive awards: 12,171; 11,349; 10,971; 11,058; 10,591.
  - Funding rate: 28%, 26%, 28%, 29%, 26%.
  - "The NSB intends to publish the subsequent digests for fiscal years 2022, 2023, and 2024 by the end of the calendar year."
  - Source: [NSF FY2024 AFR (nsf25002)](https://nsf-gov-resources.nsf.gov/pubs/2025/nsf25002/pdf/nsf25002.pdf)
- **FY2025:** "43,532 proposals evaluated through a competitive merit review process" and "8,377 competitive awards funded". That implies about 19% (my calc). — [NSF budget page](https://nsf.gov/about/budget)
- **"NSF by the Numbers"** (Tableau dashboards: Trends, Numbers by State, Details, Institution Factsheet):
  - Covers FY2011–FY2025. Codebook v1.0.7 is dated April 2026.
  - Variables: proposals evaluated, new awards, funding rate (= awards ÷ (awards + declines)), by directorate and state.
  - The Institution Factsheet counts distinct PIs and co-PIs on awards over 5 years.
  - No documented bulk download; a Tableau ".csv" export attempt returned an empty file.
  - Sources: [NSF by the Numbers](https://www.nsf.gov/about/about-nsf-by-the-numbers); [codebook](https://nsf.gov/about/about-nsf-by-the-numbers/codebook)
- **SBE directorate funding rate FY2024: 19%** (search-sourced). — [NSF SBE funding rates](https://www.nsf.gov/sbe/funding-rates)

**AI-use evidence spanning NIH and NSF (secondary; context for the AI-impact researcher)**
- A PNAS study published 11 August 2026 (Kellogg/Northwestern) analysed NSF and NIH proposals and awards from 2021–2025. It found LLM use rising from 2023, and heavy-LLM NIH applications about 4 percentage points more likely to be funded, with no such association at NSF. — [Northwestern news](https://news.northwestern.edu/stories/2026/08-2/chatbots-are-changing-who-wins-research-grants-study-finds); [arXiv 2601.15485](https://www.arxiv.org/pdf/2601.15485)

### Inferences
- **Two-thirds people, one-third intensity.** NIH RPG applications rose 12.9% in FY2025 while unique RPG applicant investigators rose 8.9% (my calc). Roughly two-thirds of the surge is more people applying and one-third is more applications per person. The ratio of RPG applications to RPG investigators went from about 1.22 (2022) to 1.26 (2025) (my calc). This is a crude ratio, because applications are counted per project and investigators include MPIs.
- **FY2025 is not clean.** The surge coincides with severe US funding disruption: awards fell 20.5%, forward funding was used, and there were terminations and re-competition. Researchers may submit more applications because success rates collapsed, not only because AI lowers the cost of writing. A simple before/after on NIH FY2025 cannot isolate AI.
- **Cap effects are not yet in the annual data.** FY2026 is the first year under the cap; it ends 30 September 2026 and Data Book updates have appeared around February–March. FY2026 application counts should drop for heavy submitters by construction. That is a structural break for any 2026 comparison.
- **The cap does not appear to have stopped aggregate growth.** NIH's own round-level statement (>40,000 applications for the January 2027 round vs >35,000 in May 2025) suggests demand kept rising. This is consistent with a cap that binds only the ~1.3% of heavy submitters. The round-level count may still be distorted by:
  - the rescheduled October–November 2025 deadlines
  - the end of paylines from January 2026, which may change applicants' expectations
  - possible pent-up resubmissions after FY2025 award cuts
- **FY2025–FY2026 confounders stack up:** indirect-cost cap attempt (Feb 2025), forward funding (FY2025), shutdown rescheduling (Oct–Nov 2025), the application cap (25 Sep 2025), payline removal (Jan 2026 round), and modified peer review through January 2027. Any AI attribution for NIH in 2025–2026 needs a design that conditions on these, for example comparing within-PI behaviour or mechanisms affected differently.
- **NIH series coverage:**
  - application-based: 1970–2025
  - person-based unique applicants: 1998–2025
  - cumulative 5-year applicants: 2003–2025
  - F/K/T: 1997/98–2025
  - all machine-readable
- **The 2003–2007 precedent.** At the end of NIH's budget doubling, RPG applications rose 37% (34,710 → 47,455; my calc from report 20). Large application surges have happened without AI, so a pre-2022 baseline with comparable shocks is useful.
- **NSF has no comparable surge.** FY2025 proposals (43,532) are about the same as FY2021 (43,606) and below 2012–2018 levels (~48–49k). NSF has a structural break in FY2019 from no-deadline policies.

### Gaps
- DOE Office of Science and DoD (CDMRP, ARO, ONR, AFOSR): I found no public application or success-rate series in the time available. Search budget ran out.
- NSF Merit Review Digests for FY2022–FY2024: the AFR says NSB intended to publish them. I could not locate them. Unique-PI counts after FY2021 are therefore unverified.
- NIH council-round-level application counts: only NIH's two narrative figures were found (>35,000 for May 2025; >40,000 for January 2027). No round-by-round series (e.g., CSR receipt statistics) was located, and the new dates for the rescheduled October–November 2025 deadlines were not retrieved.
- The coordinator also flagged 2025 grant terminations as a confounder; I did not verify a primary source on termination counts in this session.
- The exact counting rule for the NIH cap (council-round year vs calendar year) needs the NIH FAQ, which I did not locate. NIH has published no data yet on how many PIs or applications the cap affected.
- In report 136 (career stage), the JSON does not label which dataset is first-time and which is established.

## Q2. Europe: ERC, MSCA, Horizon dashboards, UKRI, DFG, SNSF, NWO, ANR, RCN, VR, Spain, Italy

### Takeaway
Europe shows the clearest post-2022 application surges, though most are confounded by programme rules and budget events.
- **MSCA Postdoctoral Fellowships:** 6,909 evaluated (2022) → 16,836 evaluated / 17,066 received (2025), about +144%. Success fell to 9.6%.
- **ERC:** Starting Grants 2,628 (2023 call) → 4,807 (2026 call); Advanced Grants 1,756 (2023) → 3,458 (2026).
- **UKRI research councils** in 2024–25: EPSRC +43%, MRC +37%, ESRC +55% year on year.
- **SNSF Project Funding:** a record 1,451 applications in October 2025, +54% vs 2021.
- **ANR:** step-1 pre-proposals +15.9% in 2026.
- **Funder responses:** ERC tightened resubmission rules for 2027 and partly reversed them after an outcry; SNSF capped concurrent grants; RCN moved FRIPRO to rolling intake.
- **AI attribution:** no European public funder I checked attributes the rise to AI in its own statistics releases. Wellcome and the RoRI authors do (see Q4).

### Cited Findings

**ERC: per-call statistics (primary unless marked)**
- **Statistics tool:** "Granted projects" and "Evaluated proposals" datasets, filterable by funding scheme, call year and research domain, "possible to export the data in excel format", "updated… each time when new call results are released". — [ERC statistics](https://erc.europa.eu/statistics-0)
- ERIS (the ERC Research Information Service) needs a user account (secondary). — [EU-Büro NCP FAQ](https://eubuero.de/en/ncp-erc-faq-2446.html)
- **Eligible proposals and success rates per Horizon Europe ERC call** (secondary compile of EC Horizon dashboard data by Business Finland, dated 11 Feb 2026; the label is the call year, the date in brackets is the deadline):

  | Scheme | 2021 | 2022 | 2023 | 2024 | 2025 |
  |---|---|---|---|---|---|
  | StG | 4,016, 10% (12 Apr 2021) | 2,838, 14% (13 Jan 2022) | 2,628, 15% (25 Oct 2022) | 3,434, 11% (7 Nov 2023) | 3,884, 12% (15 Oct 2024) |
  | CoG | 2,604, 12% | 2,168, 15% | 2,071, 14% | 2,262, 12% | — |
  | AdG | 1,697, 15% | 1,588, 12% | 1,756, 13% | 2,467, 11% | — |
  | SyG | — | 355, 8% | 387, 7% | 540, 8% | — |

  Source: [Business Finland call-specific success rates (11 Feb 2026)](https://www.businessfinland.fi/globalassets/finnish-customers/horizon-europe/tilastotietoa/call_specific_success_rates_11022026.pdf)
- **ERC "facts and figures" releases** (preliminary submitted counts):
  - **StG 2025:** 3,928 applications ("13% increase"), call closed 15 Oct 2024; budget €751m for ~483 grants. — [ERC StG 2025 applications](https://erc.europa.eu/news-events/news/starting-grants-2025-applications-facts-and-figures)
  - **StG 2026:** 4,807 applications, +22.4%, closed 14 Oct 2025.
    - Domains: PE 1,980; SH 1,568; LS 1,257. Women "nearly 43%" of proposals, the highest since 2007.
    - €705m for ~450 grants.
    - No reason for the increase and no AI mention.
    - Source: [ERC StG 2026 applications](https://erc.europa.eu/news-events/news/starting-grants-2026-applications-facts-and-figures)
  - **CoG 2025:** 3,121 applications, +35% vs previous call and +46% vs 2023, closed 14 Jan 2025. — [ERC CoG 2025 applications](https://erc.europa.eu/news-events/news/applications-erc-consolidator-grants-2025-facts-and-figures)
  - **CoG 2026:** 3,060, −2% vs 2025 and +32% vs 2024; €673m for ~328 grants (search-sourced). — [ERC CoG 2026 applications](https://erc.europa.eu/news-events/news/applications-erc-consolidator-grants-2026-facts-and-figures)
  - **AdG 2025:** 3,329, +31% vs 2024 and +82% vs the year before (search-sourced). — [ERC AdG 2025 applications](https://erc.europa.eu/news-events/news/applications-erc-advanced-grants-2025-facts-and-figures)
    - Results: 319 grants, 9.6% success (secondary). — [EU-Büro](https://www.eubuero.de/en/news-erc-2026-06-26-4593.html)
  - **AdG 2026:** 3,458, +3.9%, closed late August 2026; €747m for ~294 grants (search-sourced). — [ERC AdG 2026 applications](https://erc.europa.eu/news-events/news/applications-erc-advanced-grants-2026-facts-and-figures)
  - **StG 2025 results:** 478 grants, "just over 12%" (search-sourced). — [ERC StG 2025 results](https://erc.europa.eu/news-events/news/erc-2025-starting-grants-results)
- **ERC consolidated applications (StG+CoG+AdG+SyG), as supplied to RoRI:**
  - 7,159 (2022), 7,050 (2023), 8,869 (2024), **11,090 (2025)**, 8,824 (2026, AdG not yet included).
  - Growth 2025/2022: +54.9%.
  - RoRI's note cites the April 2026 ERC President's warning about limits.
  - Source (primary, verified): RoRI "Research funder application data" xlsx, supplementary to Rees & Wilsdon, *Nature* 652, 1119–1121 (2026). — [Nature supplementary xlsx](https://media.nature.com/original/magazine-assets/d41586-026-01297-y/52331462); [article DOI](https://doi.org/10.1038/d41586-026-01297-y)
- **ERC demand management in 2026:**
  - **16 April 2026, open letter from ERC President Maria Leptin:**
    - "the number of applications has been rising dramatically".
    - "Some panels now have more than 250 applications to assess". Historically panels handled about 50–150.
    - "the burden on the reviewers remains high".
    - Announced longer restrictions on unsuccessful applicants for the 2027 calls, possibly also for 2028–2029.
    - No AI mention.
    - Source: [ERC President letter](https://erc.europa.eu/news-events/news/erc-president-explains-stricter-application-measures-amid-rising-demand-funding)
  - **29 April 2026 readjustment:** after the "many concerns" raised, the Scientific Council kept **unchanged** resubmission restrictions for StG/CoG/AdG/ERC Plus.
    - A C score at step 1 in the 2025 or 2026 calls, or a B score at step 1 in 2026, makes an applicant ineligible for 2027.
    - Stricter rules apply to Synergy.
    - 2028 eligibility will be set in WP2028.
    - Source (secondary, Austrian ERA portal): [ERA Portal Austria](https://era.gv.at/news-items/erc-scientific-council-readjusts-rules-for-reapplication/)
  - **New scheme:** the ERC Plus pilot (up to €7m) had its first call open 2 June–2 September 2026 (search-sourced). — [ERC AdG 2026 page / search summary](https://erc.europa.eu/news-events/news/applications-erc-advanced-grants-2026-facts-and-figures)

**MSCA Postdoctoral Fellowships (primary unless marked)**
- **2025 call** (closed 10 Sep 2025): **17,066 proposals** (EF 15,828; GF 1,238), up from 10,360 in 2024 (+64.6%).
  - "the highest number of proposals ever for any funding action in the 40 years" of the Framework Programmes.
  - Budget €404.3m for about 1,650 projects.
  - The release notes "a higher increase of applications from researchers based outside the EU". About half of applicants are based outside the EU.
  - No AI mention.
  - Source: [MSCA news](https://marie-sklodowska-curie-actions.ec.europa.eu/news/msca-postdoctoral-fellowships-2025-proposals)
- UKRO's count is 17,058, "with **21%** of those proposals being from the UK" (secondary). — [UKRO](https://www.ukro.ac.uk/news/msca-postdoctoral-fellowships-2025-receives-record-number-of-17058-proposals/)
- **Series of evaluated and funded proposals and success rate**, from the Spanish NCP (FECYT) presentation of 24 Apr 2026:

  | Call | Evaluated | Funded | Success |
  |---|---|---|---|
  | PF-2021 | 8,247 | 1,156 | 14.02% |
  | PF-2022 | 6,909 | 1,235 | 17.88% |
  | PF-2023 | 7,918 | 1,249 | 15.77% |
  | PF-2024 | 10,212 | 1,696 | 16.61% |
  | **PF-2025** | **16,836** | **1,610** | **9.56%** |

  - EF grew 9,323 → 15,851 (+70%) and GF 1,037 → 1,215 (+17%).
  - ERA Fellowships opt-ins grew 953 → 1,789 (+88%).
  - Source: [FECYT MSCA-PF 2025 results](https://www.horizonteeuropa.es/sites/default/files/noticias/24042026_MSCA-PF%20Resultados%202025.pdf)
- The same Business Finland compile gives eligible PF proposals of 8,250 (2021), 6,911 (2022), 7,919 (2023) and 10,221 (2024). It also gives Doctoral Networks: 1,071; 942; 1,061; 1,405. — [Business Finland compile](https://www.businessfinland.fi/globalassets/finnish-customers/horizon-europe/tilastotietoa/call_specific_success_rates_11022026.pdf)
- **Submitted (received) PF proposals, as used by RoRI:** 7,044 (2022), 8,039 (2023), 10,360 (2024), 17,066 (2025), i.e. +142.3% 2025/2022. The 2022 figure cites the MSCA news "MSCA Postdoctoral Fellowships 2022 receives 7,044 proposals". (primary, verified xlsx) — [RoRI/Nature supplementary xlsx](https://media.nature.com/original/magazine-assets/d41586-026-01297-y/52331462)

**Horizon Europe / Horizon 2020 dashboards**
- The Commission's Horizon dashboard reports eligible proposals, retained proposals and success rates per call. Business Finland's PDF reproduces every call ID with deadline, eligible proposals, retained proposals and success rate. — [Business Finland compile](https://www.businessfinland.fi/globalassets/finnish-customers/horizon-europe/tilastotietoa/call_specific_success_rates_11022026.pdf)
- Aggregate Horizon Europe 2021–2024 (secondary): 88,803 eligible proposals, 16.4% success rate (dashboard frozen 6 Jan 2025). — [EU Monitor](https://www.eumonitor.eu/9353000/1/j4nvirkkkr58fyw_j9vvik7m1c3gyxp/vmo0eitmzttj)

**UKRI (primary, verified Excel)**
- **"UKRI investment and outputs data 2015 to 2026"** (published 16 July 2026; xlsx).
  - Counts applications (by date received), applications assessed and awarded (funding decisions in the financial year), award rate by number and by value.
  - Breakdowns: category (research & innovation / fellowships / training), decision owner (council), funder, lead organisation and region.
  - "The figures presented here include revisions to previously published figures." **Methodological change:** "Applications to Innovate UK that do not meet eligibility criteria are now excluded prior to assessment… applied consistently across the full time series".
  - Time-series breaks are flagged at 2016-17/2017-18 and 2017-18/2018-19, because Innovate UK numbers are only available from 2017-18.
  - Sources: [UKRI statistical publication Apr 2015–Mar 2026](https://www.ukri.org/publications/ukri-investments-and-outputs/statistical-publication-ukri-investment-and-outputs-april-2015-to-march-2026/); [xlsx](https://www.ukri.org/wp-content/uploads/2026/07/160726-UKRI-investments-and-outputs-data-2015-2026.xlsx)
- **UKRI total, revised series:**
  - Applications assessed, 2015-16 → 2025-26: 14,872; 13,593; 14,809; 18,599; 17,368; 37,451 (COVID year); 23,463; 23,593; **28,177 (2023-24); 27,669 (2024-25); 19,082 (2025-26)**.
  - Award rate (%): 44.3; 39.8; 37.4; 30.1; 29.8; 24.2; 26.7; 30.2; 27.0; 20.7; 18.7.
  - Fellowship applications assessed: 1,466 (2021-22) → 1,742 → 1,965 → **2,290 (2025-26)**, with the award rate falling to 18.0%.
  - Source: [UKRI 2015–2026 xlsx](https://www.ukri.org/wp-content/uploads/2026/07/160726-UKRI-investments-and-outputs-data-2015-2026.xlsx)
- **Research councils, applications assessed** (decision owner; 2022-23 → 2023-24 → 2024-25 → 2025-26) and award rate %:

  | Council | Applications assessed | Award rate % |
  |---|---|---|
  | EPSRC | 2,120 → 2,302 → **3,299** → 2,772 | 29.9 → 28.0 → 20.8 → 14.5 |
  | MRC | 1,899 → 2,008 → **2,751** → 2,475 | 28.8 → 32.6 → 18.9 → 12.4 |
  | ESRC | 1,255 → 1,092 → **1,698** → 1,293 | 28.8 → 34.5 → 22.3 → 20.3 |
  | BBSRC | 1,794 → 1,938 → 1,859 → 1,832 | 34.8 → 32.8 → 27.8 → 14.4 |
  | AHRC | 1,500 → 1,529 → 1,383 → 1,522 | 27.5 → 24.3 → 23.1 → 18.8 |
  | NERC | 1,500 → 809 → 1,066 → 853 | — |
  | STFC | 592 → 533 → 610 → 738 | — |
  | Innovate UK | 12,122 → 16,757 → 14,214 → 5,603 | — |

  Source: [UKRI 2015–2026 xlsx, table 2.2](https://www.ukri.org/wp-content/uploads/2026/07/160726-UKRI-investments-and-outputs-data-2015-2026.xlsx)
- **Earlier (2025) edition**, before the Innovate UK revision: applications assessed doubled from 15,436 (2017-18) to 30,550 (2024-25), awards +3% (5,522 → 5,667), award rate 36% → 19%. — [UKRI 2015–2025 xlsx](https://www.ukri.org/wp-content/uploads/2025/08/UKRI-130825-UKRI-InvestmentAndOutputsData-2015-2025.xlsx); [UKRI 2015–2025 PDF](https://www.ukri.org/wp-content/uploads/2025/07/UKRI-220725-InvestmentAndOutputsData-2015-2025-1.pdf)
  - The 2026 edition gives a 2024-25 award rate of 21% (rounded; table: 20.7%). — [UKRI 2026 publication](https://www.ukri.org/publications/ukri-investments-and-outputs/statistical-publication-ukri-investment-and-outputs-april-2015-to-march-2026/)
  - **RoRI used this pre-revision series.** RoRI's UKRI row (24,035; 29,366; 30,998; 29,927 for "2022–2025", i.e., financial years 2021-22 to 2024-25) matches the 2025-edition Table 1 total of applications received. That total includes Innovate UK, before the 2026 revision excluded ineligible Innovate UK applications, so RoRI's UKRI +24.5% is dominated by Innovate UK. — [RoRI/Nature supplementary xlsx](https://media.nature.com/original/magazine-assets/d41586-026-01297-y/52331462); [UKRI 2015–2025 xlsx](https://www.ukri.org/wp-content/uploads/2025/08/UKRI-130825-UKRI-InvestmentAndOutputsData-2015-2025.xlsx)
- **2025-26 budget explanation:** UKRI attributes the fall in awards to:
  - "a shift… towards committing less funding upfront"
  - "adjustments to over-profiling"
  - "pauses to specific funding opportunities" (Ian Chapman's February letter)
  - No mention of AI.
  - Demographic data are in a separate "UKRI equalities monitoring" publication.
  - Source: [UKRI 2026 publication](https://www.ukri.org/publications/ukri-investments-and-outputs/statistical-publication-ukri-investment-and-outputs-april-2015-to-march-2026/)
- **Council demand-management rules** (secondary; Nature Careers, republished 2 Sep 2025):
  - NERC (since 2015) caps applications from institutions with low success rates.
  - NERC and EPSRC "no longer accept uninvited resubmissions" as of 2025.
  - Innovate UK is >56% of assessed applications.
  - Source: [Dementia Researcher (Nature Careers repost)](https://www.dementiaresearcher.nihr.ac.uk/the-grant-funding-lottery/)
- **UK association to Horizon Europe:** "The UK agreed a deal to associate to Horizon Europe on 7 September 2023… All calls in Work Programme 2024 will be covered by association". — [UKRI Horizon Europe page](https://www.ukri.org/apply-for-funding/horizon-europe/)

**DFG (primary, verified PDF)**
- Jahresbericht 2025:
  - "Rund 22.600 Anträge insgesamt wurden im Jahr 2025 von der DFG entschieden". Two-thirds are in Einzelförderung; about 5,300 are in coordinated programmes.
  - About 6,700 new projects were funded.
  - The number-based Förderquote of new proposals in Einzelförderung was **26.9%**, "um fast drei Prozentpunkte gesunken". The amount-based Bewilligungsquote was 22.3%.
  - Explanation offered: inflation-driven cost increases, not AI.
  - Nearly 48,000 written reviews were requested, with a 50% return rate.
  - Charts show Bewilligungsquoten 2016–2025 by gender (Grafik 6) and application counts for career programmes 2022–2025 (Grafik 10).
  - Source: [DFG Jahresbericht 2025](https://www.dfg.de/resource/blob/399666/dfg-jb2025.pdf)
- A DFG letter (November 2024) said the SFB programme's funding rate was lowered because application volume had risen strongly (search-sourced; university-hosted document). — [Heidelberg-hosted DFG SFB note](https://backend.uni-heidelberg.de/de/dokumente/dfg-sfbs-hinweise-zum-bewilligungsschreiben-fuer-das-haushaltsjahr-2025/download)

**SNSF**
- **October 2025 Project Funding call:** a record **1,451 applications** requesting CHF 1.3bn, vs 944 (Project Funding + Sinergia) in 2021. "the rising number of applications is leading to steadily decreasing chances of success". No AI mention; the SNSF "is still analysing the underlying reasons". (primary, 24 Nov 2025) — [SNSF news](https://www.snf.ch/en/aP8IEQcq8CUWFCkF/news/new-record-in-project-funding)
- **Approval rate** fell from 36% (2024) to 30% (2025); the SNSF limited proposals per person and requested amounts. (primary, 28 Apr 2026) — [SNSF news](https://www.snf.ch/en/9EcyLcUUpkxVDGmp/news/)
- **Measures and budget** (secondary):
  - From the 1 April 2026 deadline: at most two concurrent Project Funding grants per researcher and CHF 3m per project.
  - "since October 2021… a 55% increase in applications and a 69% increase in requested funding".
  - The federal budget for SNSF was cut by 5%.
  - Source: [Univ. Fribourg](https://www.unifr.ch/research/en/highlights/news/34146/important-changes-to-snsf-project-funding)
- **Data portal:** data.snf.ch has Key Figures pages (funding instruments, research institutions, disciplines, demographics, internationality) and Datasets; content is JavaScript-rendered. A listed CSV export (`/exportcsv/Application.csv`) returned 404 when tested. (primary, verified structure) — [SNSF Data Portal](https://data.snf.ch/datasets)
- 2020: about 8,200 applications, ~3,300 funded (secondary). — [SNSF press release via presseportal](https://www.presseportal.ch/de/pm/100002863/100869497)

**NWO (Netherlands)**
- **Veni round announced 2026:** 1,392 pre-proposals → 448 invited → 205 awards (14.7%).
- **2025 Talent Programme** (Veni+Vidi+Vici): "more than 2,500" applicants, 393 (16%) successful.
- NWO plan to reduce competition "expected to be completed before the summer of 2027".
- No AI mention.
- Source (secondary): [Resource (WUR), 10 Aug 2026](https://www.resource-online.nl/index.php/wp-json/wp/v2/posts/125816)
- Veni 2024: 1,365 candidates, 469 invited, 200 awards (search-sourced, unverified attribution).
- Veni 2025 subsidy ceiling raised from €45.76m to €62.4m, with up to 195 awards (search-sourced). — [Staatscourant 2026-22057](https://zoek.officielebekendmakingen.nl/stcrt-2026-22057.pdf)

**ANR (France)**
- **AAPG 2026 step 1:** 7,290 eligible pre-proposals (PRC/PRME/JCJC) vs 6,288 in 2025, **+15.9%**. 2,986 were retained (40.9%): PRC 42.1%, PRME 37.2%, JCJC 39.5%.
- No reason given and no AI mention.
- Rule notes: PRCE moves to single-stage evaluation; automatic step-2 invitation for complementary-list projects since AAPG 2022.
- Source (primary, 25 Feb 2026): [ANR AAPG 2026 step-1 results](https://anr.fr/fr/actus/details/news/aapg-appel-a-projets-generique-2026-les-resultats-de-letape-1/)
- AAPG success rate 24.3% in 2023 vs 16% in 2020 (search-sourced). — [ANR activity report 2023](https://anr.fr/fr/actus/details/news/rapport-dactivite-2023-soutenir-toutes-les-recherches-du-laboratoire-a-la-societe-du-local-a-l/)
- A 2005–2019 selection-rate series is in a parliamentary answer (search-sourced). — [Assemblée nationale QE 25552](https://questions.assemblee-nationale.fr/dyn/15/questions/QANR5L15QE25552.pdf)

**Research Council of Norway (FRIPRO)**
- FRIPRO moved in **October 2023** from one annual deadline to rolling intake, with quarantine rules.
- Before (2018–2022): 1,200–2,000 FRIPRO applications per year at 5–10% success.
- Since: "litt over 50 søknader i månaden", about 650 in the last year vs about 580 the year before; success 21% after two years.
- The recent rise is linked to two new calls (top researchers, radical ideas) and reduced quarantine rules.
- Early-career share of applicants rose from ~35% to ~50%.
- Source (secondary: University of Bergen analysis newsletter no. 68, 22 Jun 2026, summarising an RCN analysis): [UiB Analysegruppa nr 68](https://ekstern.filer.uib.no/ledelse/Analysegruppen%20-%20nyhetsbrev/Analysegruppa-teikn-og-tal-i-tida-nr68.pdf)

**Swedish Research Council (VR)**
- **Natural & engineering sciences (NT) project-grant call**, applications 2015–2025: 1,248; 1,231; 1,183; 1,161; 1,196; 1,182; 1,200; 1,109; 1,209; 1,269; **1,374**.
- Success: 23.0 → 24.2 (2022) → 22.6 → 19.8 → **18.1%** (2025).
- Source (secondary compile by SLU, Oct 2025): [SLU VR-NT table](https://internt.slu.se/globalassets/mw/externfinansiering/vr_ntsve_from2015_251030.pdf)
- VR received 1,890 applications at 17% success in a 2025 round (search-sourced; scope unclear). — [KTH news](https://www.kth.se/om/nyheter/centrala-nyheter/kth-forskare-far-155-miljoner-av-vetenskapsradet-1.1437168)

**Spain and Italy**
- **AEI Proyectos de Generación de Conocimiento 2025:**
  - Call budget up to €700m; submission window 20 Nov–16 Dec 2025. — [Ministerio de Ciencia call page](https://www.ciencia.gob.es/en/Convocatorias/2025/PID2025.html)
  - Provisional resolution: €697.6m for 3,422 projects and 1,156 predoctoral contracts, said to exceed the prior edition in applications. No application count given (search-sourced). — [Reservoir](https://www.reservoir.ac/es/actualidad/generacion-conocimiento-2025-697-millones-mayor-convocatoria)
- **Italy PRIN:** the PRIN 2026 call (€260m; deadline 1 June 2026) was announced April 2026 (search-sourced). The only national submission count found is PRIN 2017, with 4,452/4,552 projects reported (secondary). — [Orizzonte Scuola](https://www.orizzontescuola.it/bando-prin-miur-presentati-4452-progetti/)

### Inferences
- **The scale of the MSCA PF jump is unusual.** +144% from 2022 to 2025 (my calc) and +65% in 2025 alone. Strong non-AI confounders apply:
  - UK re-association: 21% of 2025 proposals were UK-hosted, and UK hosts were only covered from WP2024.
  - The note that more applicants came from outside the EU, plausibly including US researchers affected by 2025 funding disruptions.
  - Seal/ERA Fellowship incentives.
- **ERC growth started before 2025 and was uneven.**
  - StG grew 2,628 (2023 call, deadline Oct 2022, just before ChatGPT) → 3,434 (Nov 2023 deadline) → 3,928 → 4,807 (Oct 2025 deadline). About +83% (my calc, eligible vs submitted).
  - CoG and AdG show a step change in 2024–2025 and then plateau in 2026 (CoG −2%, AdG +3.9%).
  - The ERC Scientific Council's resubmission rules were stable, so rule changes do not explain the rise. UK association (WP2024) does explain part of it.
  - The 2021 StG spike (4,016) shows earlier, non-AI volatility from the first Horizon Europe call.
- **ERC call-year labels lag submission dates.** For example, "ERC-2025-STG" closed 15 Oct 2024. Any AI analysis should key on deadline dates, not call labels.
- **UKRI research councils** show a sharp one-year spike in 2024-25 (EPSRC +43%, MRC +37%, ESRC +55% year on year; my calc), then a fall in 2025-26 as UKRI paused opportunities. This is a budget-driven break. Innovate UK dominates UKRI totals, so research-council rows are the relevant academic series.
- **Smaller or stable rises:** NWO Veni was nearly flat (+2%), VR-NT +14% (2023→2025), KAKENHI roughly +6% (see Q3). Increases are not universal. Funders with built-in demand management (pre-proposals, eligibility windows, per-person limits) show smaller rises.

### Gaps
- **ERC statistics export:** I could not test it (JavaScript tool). The 2007–2020 per-call numbers are not reproduced here, though they are available through the tool.
- **No ERC AI attribution:** no ERC statement attributing growth to AI was found. Leptin's letter does not mention AI.
- **ERC 2027 Work Programme:** final text (reported published 22 July 2026) not verified.
- **Swiss association:** Switzerland's Horizon Europe association date (affecting 2025 calls) was not verified in this session.
- **MSCA under Horizon 2020:** Individual Fellowship counts for 2014–2020 were not retrieved. They would extend the MSCA series back before 2021.
- **UKRI applicant counts:** UKRI equalities/diversity data with applicant (person) counts were not retrieved; they are in a separate "UKRI equalities monitoring" publication.
- **DFG:** a numeric time series of application counts (not just rates) was not extracted. The DFG "Zahlen und Fakten" web tables were not accessed.
- **SNSF:** a full application series (data.snf.ch) could not be downloaded; the portal is JavaScript-rendered and the CSV export path returned 404.
- **Spain:** AEI application counts (PID, Ramón y Cajal, Juan de la Cierva), ISCIII, AGAUR and FECYT ICONO were not obtained. The ICONO host failed with 502 via the proxy, and AEI statistics URLs returned 404.
- **Italy:** PRIN 2020/2022/2025 submission counts were not found.

## Q3. Asia-Pacific and others: JSPS KAKENHI, NSFC, ARC, NHMRC, CIHR/NSERC/SSHRC, NRF Korea, HRC NZ, and foundations (Wellcome, HHMI, "la Caixa")

### Takeaway
**Long national series exist for Japan and China.**
- **KAKENHI:** new applications 1996–2025 (~76k → ~95k), roughly 27% adoption.
- **NSFC:** 294,396 (2022) → 384,564 (2024) → 433,426 (2025) → 470,561 (2026). NSFC itself attributes the 2024 jump mainly to a rule allowing General Program resubmission after two consecutive unsuccessful years, and notes a one-proposal-per-program-type limit.
- **KAKENHI after 2022:** a modest post-2022 rise of about +6% (2023→2025) from a pre-2021 peak, so no AI surge is visible. Per-person application limits plausibly cap growth.

**Canada:**
- **CIHR Project Grant:** rising steadily, 2,443 (Spring 2024) → 3,101 (Fall 2025), +27%, with success down to 13.6%.

**Australia:**
- **ARC:** introduced an EOI stage for Discovery Projects 2025, which breaks its series.
- **NHMRC:** publishes downloadable outcomes data.

**Foundations:**
- **Wellcome:** says funders saw 50–100% increases and that AI is "likely" a driver.
- **HHMI and "la Caixa":** publish only occasional counts.

### Cited Findings

**JSPS KAKENHI (Japan)**
- **JSPS series PDF** "科研費の主な研究種目における応募件数、採択件数、採択率の推移" covers FY1996 (H8) to FY2025 (R7). It gives new applications, new adoptions and adoption rate (values read from the chart labels and cross-checked: adoptions ÷ applications = printed rate). (primary, verified PDF; created 2026-03-19)

  | Fiscal year | New applications | New adoptions | Adoption rate |
  |---|---|---|---|
  | 1996 | 75,832 | 19,781 | 26.1% |
  | 2001 | 83,548 | 17,400 | 20.8% |
  | 2006 | 94,440 | 20,085 | 21.3% |
  | 2011 | 91,737 | 26,170 | 28.5% |
  | 2016 | 101,234 | 26,676 | 26.4% |
  | 2017 | 101,247 | 25,313 | 25.0% |
  | 2018 | 103,672 | 25,796 | 24.9% |
  | 2019 | 101,857 | 28,892 | 28.4% |
  | 2020 | 104,158 | 28,569 | 27.4% |
  | 2021 | 95,208 | 26,550 | 27.9% |
  | 2022 | 92,470 | 26,435 | 28.6% |
  | 2023 | 90,089 | 24,809 | 27.5% |
  | 2024 | 94,280 | 25,699 | 27.3% |
  | **2025** | **95,482** | **25,931** | **27.2%** |

  - The FY2025 tally covers 特別推進研究, 新学術領域研究(公募), 学術変革領域研究(A)(B), 基盤研究, 挑戦的研究, 若手研究, 研究活動スタート支援 and 国際共同研究加速基金(国際先導・海外連携).
  - Source: [JSPS 2-1_r7.pdf](https://www.jsps.go.jp/file/storage/kaken_27_kdata_g_4551/2-1_r7.pdf)
- **MEXT FY2025 first allocation** (16 May 2025): 80,146 new applications, 23,109 new adoptions. This excludes categories decided after June, so it is not comparable with the full-year JSPS figure. (primary) — [MEXT FY2025 KAKENHI allocation](https://www.mext.go.jp/a_menu/shinkou/hojyo/1422129_00008.htm)

**NSFC (China)**
- **2025 centralized reception:** 433,426 applications received; 432,434 accepted after screening; 53,159 funded in 10 categories, with others pending. Announced 27 Aug 2025. (secondary, reporting the NSFC notice) — [The Paper](https://www.thepaper.cn/newsDetail_forward_31486184)
- **2026 centralized reception:** **470,561 received**; 469,429 accepted; 69,563 funded (10 categories).
  - Youth Fund C funding +12,046 (+50.1%) and General Program +3,400 (+14.8%), "显著超过申请项数增幅".
  - No AI or rule changes mentioned.
  - Source (secondary, 26 Aug 2026): [Science and Technology Daily](https://www.stdaily.com/web/gdxw/2026-08/26/content_569790.html)
- **NSFC series supplied to RoRI** ("all proposals received during the annual centralized submission period"): 294,396 (2022), 304,333 (2023), **384,564 (2024)**, 433,426 (2025), i.e. +47.2% 2025/2022.
  - NSFC's note: the sharp 2024 rise was "mainly caused by a growth in General Program proposals, due to an NSFC policy change allowing resubmission after two consecutive unsuccessful years".
  - "NSFC applicants in China can submit only one proposal per year within the same program type, so even with AI tools it is not possible to generate and submit multiple applications in the same year."
  - "Not yet clear how much growth is related to AI."
  - Source (primary, verified): [RoRI/Nature supplementary xlsx](https://media.nature.com/original/magazine-assets/d41586-026-01297-y/52331462)

**Australia**
- **ARC Discovery Projects** (search-sourced from ARC selection reports; arc.gov.au was unreachable from this environment):
  - DP24: 2,592 applications, 16.3% success. — [ARC DP24 selection report](https://arc.gov.au/discovery-projects-selection-report-funding-commencing-2024)
  - DP25: 1,133 applications, 47.3% success, after a newly introduced Expression of Interest stage. — [ARC DP25 selection report](https://www.arc.gov.au/funding-research/funding-outcome/selection-outcome-reports/dp25-selection-report-funding-commencing-2025)
  - DP26 EOI outcomes were published. — [ARC DP26 EOI outcomes](https://arc.gov.au/news-and-publications/media/expression-interest-outcomes-discovery-projects-2026)
- **NHMRC Investigator Grants 2025:** 1,715 applications, 13.4% funded rate, 229 grants (search-sourced; site returned 503 to me). — [NHMRC 2025 Investigator Grants outcomes snapshot](https://nhmrc.gov.au/sites/default/files/documents/attachments/grant%20documents/NHMRC-%202025%20Investigator%20Grants%20%E2%80%93%20Outcomes%20snapshot.pdf)
  - "Outcome data can be downloaded from the outcomes webpage" (search-sourced).
- **Funder-supplied series in the RoRI dataset** (primary, verified xlsx; years are as labelled by RoRI; source for all items below: [RoRI/Nature supplementary xlsx](https://media.nature.com/original/magazine-assets/d41586-026-01297-y/52331462)):

  | Funder (series) | 2022 | 2023 | 2024 | 2025 | 2026 (partial) | Funder note |
  |---|---|---|---|---|---|---|
  | ARC, all grant calls combined | 5,485 | 5,988 | 5,287 | **7,912** | 6,998 | "various structural changes to the ARC's portfolio of schemes … will account for some of this growth. AI is also suspected by ARC to be playing a role but the extent of this remains unclear" |
  | NHMRC, MREA competitive schemes combined | 4,421 | 4,433 | 4,842 | 5,310 | n/a | — |
  | CIHR, investigator-initiated Project Grant (two competitions per year) | 3,994 | 4,288 | 5,074 | **5,915** | n/a | "early signs" of a further increase after the spring 2026 competition |
  | Michael Smith Health Research BC (programme withheld) | 128 | 128 | 127 | 173 | 204 | "hard to tease out the impacts of AI from broader funding constraints" |

  - The CIHR 2024 and 2025 values equal the sums of the CIHR competition pages above (2,443+2,631; 2,814+3,101; my check).

**Canada**
- **CIHR Project Grant** results pages, per competition (primary, verified). Applications submitted / funded / success:

  | Competition | Submitted | Funded | Success |
  |---|---|---|---|
  | Spring 2024 | 2,443 | 373 | 15.3% |
  | Fall 2024 | 2,631 | 453 | 17.2% |
  | Spring 2025 | 2,814 | 435 | 15.5% |
  | **Fall 2025** | **3,101** | **421** | **13.6%** |

  - Fall 2025 breakdowns: career stage (ECR 785 submitted, 13.8%), gender, racialized and disability status, pillar, province, language.
  - 55.5% of applications were streamlined, i.e. not discussed (+9.1 pp vs historical).
  - Funded budgets were cut 23.5% across the board.
  - No application cap or AI mention on the page.
  - Sources: [CIHR Spring 2024](https://cihr-irsc.gc.ca/e/53975.html); [Fall 2024](https://cihr-irsc.gc.ca/e/54191.html); [Spring 2025](https://cihr-irsc.gc.ca/e/54393.html); [Fall 2025](https://cihr-irsc.gc.ca/e/54594.html)
- **NSERC Discovery Grants:**
  - A "Competition statistics dashboard" dated 18 June 2025 exists (search-sourced). — [NSERC DG competition results](https://nserc-crsng.canada.ca/en/discovery-grants-competition-results)
  - ECR success rates for flagship programs are reported annually by the Canada Research Coordinating Committee; 2023 ECR 54.7% vs established 60.0% (search-sourced). — [CRCC Annex II](https://www.canada.ca/en/research-coordinating-committee/corporate/annual-progress-summary/annex-2.html)
- **SSHRC Insight Grants 2023–24:** 1,145 eligible applications, 510 awarded, 45% (search-sourced). — [SSHRC facts and figures](https://sshrc-crsh.canada.ca/en/about-sshrc/planning-and-performance-reporting/facts-and-figures.aspx)

**Korea and New Zealand**
- **NRF Korea:** no application or selection-rate statistics found. A news report says the 2026 basic-research budget rose sharply vs 2024 and selected projects nearly doubled, following the 2024 R&D budget cut (search-sourced). — [inews24](https://inews24.com/view/2005472)
- **HRC New Zealand Explorer Grants:**
  - "a random process will be used to select the applications that are offered funding", with a limit of 2 applications per first-named investigator (2025 guidelines; 2026 guidelines keep randomisation) (search-sourced). — [HRC 2025 Explorer Grant guidelines](https://gateway.hrc.govt.nz/funding/downloads/2025_Explorer_Grant_Application_Guidelines.pdf)
  - 2013–2019: 394 applications, 56 funded by lottery (search-sourced). — [Liu et al., Research Integrity and Peer Review 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC6996170/)

**Foundations**
- **Wellcome**: see Q4. Its public article gives no Wellcome-specific count, only that funders saw +50–100%. (primary)
- **Foundation series in the RoRI dataset** (primary, verified xlsx; source for all items below: [RoRI/Nature supplementary xlsx](https://media.nature.com/original/magazine-assets/d41586-026-01297-y/52331462)):
  - **Wellcome**, all schemes combined (grant year 1 Oct–30 Sep): 2,139 (2022), 2,139 (2023), 2,774 (2024), **4,289 (2025)**, i.e. +100.5% vs 2022. Note: "Comparable 2022-23 data also unavailable owing to changes at that time in Wellcome's funding programmes", so 2022 and 2023 carry the same value.
  - **"la Caixa" HealthCare Research Call:** 546, 493, 580, 714, **800 (2026)**. Staff "are seeing more signs of AI usage in applications, and do not prohibit this", alongside "levelling of quality indicators at a higher level than before".
  - **King Baudouin Foundation** (two health calls): 38, 45, 39, 85.
  - **British Academy Postdoctoral Fellowships:** 528, 413, 554, 604, **798 (2025-26 cycle)**. The BA attributes some of the rise to its nationwide Early Career Researcher Network.
- **"la Caixa" Foundation** (2024 calls, results 18 Mar 2025): INPhINIT doctoral 1,502 applications for 60 fellowships; Junior Leader postdoctoral 597 applications for 40 fellowships. No trend data. (primary) — [la Caixa mediahub](https://mediahub.fundacionlacaixa.org/en/research-fellowships/fellowships/phd-fellowships/2025-03-18/caixa-foundation-attracts-retains-talent-phd-young-researchers-6940.html)
- **HHMI:** "Nearly 1,000 eligible scientists submitted applications" for an Investigator competition that selected 26. The year is unclear (secondary). — [GEN](https://genengnews.com/news/hhmi-names-26-new-investigators-while-investing-300m-in-their-work)

### Inferences
- **KAKENHI** applications in FY2025 are still below the FY2018–FY2020 peak (~102–104k). The +6% from 2023 to 2025 is small next to European funders. KAKENHI is a useful "low-surge" comparator.
- **NSFC** growth (+8.6% in 2026) continues a long-run rise, and NSFC is expanding funded numbers (Youth C +50%). Supply-side expansion may draw in more applicants.
- **ARC DP25** EOI introduction makes "applications" before and after 2025 non-comparable; the EOI count is the right post-2025 measure.
- **CIHR's** steady growth (+27% over four competitions; my calc) overlaps with budget cuts to funded grants. CIHR does not attribute it to AI.

### Gaps
- **NSFC:** 2022–2025 counts are now available via the RoRI file. Official NSFC counts for 2015–2021 were not verified; NSFC annual reports and notices exist but were not reached after the search budget ran out. Whether 2025–2026 rule changes beyond the 2024 resubmission rule (e.g., new student or doctoral categories, Youth A/B/C reclassification) affect counts is unverified.
- **KAKENHI:** FY2026 (R8) figures were not verified; a search summary mentioned 95,140 applications and 25,430 adoptions for an R8 allocation but I could not confirm the source. JSPS category reforms (e.g., the FY2018 審査区分 reform) were not checked as breaks.
- **Australia:** ARC EOI counts for DP25/DP26 and NHMRC multi-year outcome tables were not accessible (arc.gov.au unreachable; nhmrc.gov.au 503).
- **NRF Korea:** no application statistics found.
- **HRC NZ:** application volumes for 2023–2026 not found.
- **Wellcome and HHMI:** no systematic public application counts found.

## Q4. Funder data and statements (2023–2026) on AI-generated applications, surges, reviewer burden, demand management and lotteries

### Takeaway
Only a few funders explicitly link the 2023–2026 application surge to generative AI:
- **NIH** (in its cap notice)
- **Wellcome** ("likely")
- **the RoRI researchers** analysing 12 funders: +57% from 2022 to 2025 as an unweighted mean, median +45.7%, pooled +47.6%. They call it "likely" significantly AI-linked, but "not yet possible to pinpoint". Their public supplementary xlsx records funder notes naming non-AI causes for several series.

Other funders cite surges and reviewer burden without naming AI, and responded with demand management:
- **ERC:** resubmission restrictions
- **SNSF:** per-person grant caps
- **RCN:** rolling intake with quarantine
- **Wellcome:** rolling deadlines and random-selection caps
- **NWO:** forthcoming plan
- **EPSRC/NERC:** no uninvited resubmissions

### Cited Findings
- **NIH (July 2025):**
  - AI tools enabled some PIs "to submit more than 40 distinct applications in a single application submission round". — [NOT-OD-25-132](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html)
  - 1.3% of applicants submitted more than six in 2024. — [NIH Nexus](https://grants.nih.gov/news-events/nih-extramural-nexus-news/2025/07/apply-responsibly-policy-on-ai-use-in-nih-research-applications-and-limiting-submissions-per-pi)
  - Response: a cap of six per PI per calendar year from 25 Sep 2025, plus the AI-originality rule.
  - **Reviewer burden (Sep 2026):** a "record number of applications" (>40,000) for the January 2027 Council round led NIH to keep modified review in which about 30–35% of applications are discussed. No AI mention. — [NIH Nexus, 18 Sep 2026](https://grants.nih.gov/news-events/nih-extramural-nexus-news/2026/09/continuing-modified-peer-review-processes-for-the-january-2027-council-round)
- **RoRI / Rees & Wilsdon** (*Nature* 652, 1119–1121, online 27 April 2026; DOI 10.1038/d41586-026-01297-y):
  - The analysis covers 12 multidisciplinary RoRI partner funders in six countries.
  - Application volumes were up **17% (2022→2024)** and **57% (2022→2025)**.
  - The range runs from **+14%** (British Academy postdoctoral fellowships) to **+142%** (MSCA fellowships).
  - Wilsdon: "it's likely that a significant portion of this increase is linked to the use of generative AI". The authors also say it is "not yet possible to pinpoint exactly whether or how changes in application volume and quality are linked to AI use".
  - Sources: [RoRI blog](https://researchonresearch.org/could-agentic-ai-topple-grant-funding-systems/); [Times Higher Education](https://www.timeshighereducation.com/news/research-funders-flooded-ai-assisted-applications); [Tech Xplore/UCL](https://techxplore.com/news/2026-04-agentic-ai-threatens-funding.html)
- **The underlying funder-level data are public** as the article's supplementary xlsx ("Research Funder Application Volumes — 2022–2026 Tracker", gathered "from RoRI partners and publicly available funder datasets"). (primary, verified) — [Nature supplementary xlsx](https://media.nature.com/original/magazine-assets/d41586-026-01297-y/52331462)
  - **The 12 funders/series:** ARC (all calls), British Academy (Postdoctoral Fellowships), CIHR (Project Grant), ERC (StG+CoG+AdG+SyG), King Baudouin Foundation (two calls), "la Caixa" (HealthCare Research Call), Michael Smith Health Research BC, NHMRC (MREA competitive schemes), UKRI (all applications), Wellcome (all schemes), MSCA Postdoctoral Fellowships, and NSFC (centralized submission).
  - **Growth 2025 vs 2022 by funder:** ARC +44.2%; BA +14.4%; CIHR +48.1%; ERC +54.9%; KBF +123.7%; la Caixa +30.8%; MSHR-BC +35.2%; NHMRC +20.1%; UKRI +24.5%; Wellcome +100.5%; MSCA PF +142.3%; NSFC +47.2%.
  - **The headline "57%" is the unweighted mean** of these 12 growth rates (0.572 in the file's TOTAL/AVERAGE row; my check 57.2%). The **median is 45.7%**. **Pooled** applications rose from 349,913 to 516,511, **+47.6%** (my calc).
  - NSFC is 84% of the pooled 2025 total (my calc); pooled growth excluding NSFC is about +49.7% (my calc).
  - **Data-quality flags:**
    - The file's "YoY Growth Summary" sheet is mislabelled: its "YoY" columns reproduce growth vs 2022, not year-on-year changes (e.g., MSCA "YoY 2025/2024" = 1.423, equal to 2025/2022).
    - The UKRI row is the pre-revision total including Innovate UK.
    - The Wellcome 2022 value duplicates 2023.
    - Several 2026 values are partial.
  - **Funder notes flag non-AI causes:**
    - NSFC's 2024 resubmission rule
    - ARC's scheme restructuring
    - Wellcome's programme changes
    - the British Academy's ECR network
    - MSHR-BC's "broader funding constraints"
  - **Notes suggesting AI:** ARC ("AI is also suspected … to be playing a role") and "la Caixa" ("more signs of AI usage in applications").
  - **Competing interest** stated on the article page: Wilsdon directs RoRI, "supported by an international consortium of funder partners, including some for which grant application volume data were analysed". — [Nature article](https://doi.org/10.1038/d41586-026-01297-y)
- **"18 months" warning:** Wilsdon reportedly warned that "we are probably 18 months away from the system collapsing entirely under the sheer volume of applications" (search-sourced; RPN page returned 403 to me). — [Research Professional News, Apr 2026](https://www.researchprofessionalnews.com/rr-news-uk-research-councils-2026-4-grant-systems-could-collapse-with-rise-in-ai-driven-demand/)
- **Associations urging caution:** a group of UK and European research associations urged funders not to rush radical fixes (search-sourced). — [Research Professional News, May 2026](https://www.researchprofessionalnews.com/rr-news-uk-research-councils-2026-5-funders-should-not-rush-radical-changes-amid-ai-grant-review-surge/)
- **Wellcome** (Alyson Fox, Director of Research Funding, 14 July 2026):
  - All funders at an early-2026 meeting of UK and European public funders and foundations reported "an increase in applications of 50%-100% in the most recent funding period".
  - "It is likely that the use of AI is making applying for grants easier and driving up numbers", though there is "no definitive evidence".
  - Changes:
    - Early-Career, Career Development and Discovery Awards move to always-open rolling deadlines.
    - A 12-month wait before resubmission (Career Development/Discovery).
    - The lowest-scoring Early-Career applications cannot resubmit.
    - For themed one-off calls, Wellcome "may cap the number of applications progressing to review" using **random selection** if a threshold is exceeded.
  - Source: [Wellcome](https://wellcome.org/insights/articles/rethinking-future-research-funding)
- **ERC** (16 and 29 April 2026):
  - "rising dramatically"; panels with >250 applications; reviewer burden.
  - Resubmission restrictions extended for 2027, then readjusted to unchanged for StG/CoG/AdG/ERC Plus, with Synergy stricter.
  - No AI mention.
  - Sources: [ERC letter](https://erc.europa.eu/news-events/news/erc-president-explains-stricter-application-measures-amid-rising-demand-funding); [ERA Portal Austria](https://era.gv.at/news-items/erc-scientific-council-readjusts-rules-for-reapplication/)
- **SNSF** (Nov 2025 – Apr 2026): record applications; caps on concurrent grants and on the amount per project; no AI mention. — [SNSF Nov 2025](https://www.snf.ch/en/aP8IEQcq8CUWFCkF/news/new-record-in-project-funding); [SNSF Apr 2026](https://www.snf.ch/en/9EcyLcUUpkxVDGmp/news/)
- **MSCA (Sep 2025):** record proposals; no AI mention. — [MSCA](https://marie-sklodowska-curie-actions.ec.europa.eu/news/msca-postdoctoral-fellowships-2025-proposals)
- **CIHR (Fall 2025):** streamlining (triage) removed 55.5% of applications from discussion, +9.1 pp vs historical. This is a reviewer-burden response. — [CIHR Fall 2025](https://cihr-irsc.gc.ca/e/54594.html)
- **DFG (2025):** about 48,000 written reviews requested, 50% return rate. — [DFG Jahresbericht 2025](https://www.dfg.de/resource/blob/399666/dfg-jb2025.pdf)
- **Lotteries and partial randomisation in force:**
  - HRC NZ Explorer Grants (random selection among fundable applications). — [HRC guidelines](https://gateway.hrc.govt.nz/funding/downloads/2025_Explorer_Grant_Application_Guidelines.pdf)
  - Wellcome's new random-selection cap for themed calls. — [Wellcome](https://wellcome.org/insights/articles/rethinking-future-research-funding)
- **Evidence of AI use in proposals (secondary):** a PNAS study (Aug 2026) found LLM use in NIH/NSF proposals rising from 2023. — [Northwestern](https://news.northwestern.edu/stories/2026/08-2/chatbots-are-changing-who-wins-research-grants-study-finds)

### Inferences
- **Attribution is mostly circumstantial.** It rests on timing (increases "begin soon after the launch of ChatGPT") and on anecdotes such as NIH's >40-application PIs. No funder has published per-applicant evidence that AI-drafted proposals drive volume.
- **The RoRI file itself undercuts a uniform AI story.**
  - The largest rises (MSCA +142%, KBF +124% on tiny bases, Wellcome +101%) come with funder-documented non-AI explanations: UK re-association and non-EU applicants (MSCA), programme changes (Wellcome), and small-number volatility (KBF).
  - NSFC's +47% comes despite a one-proposal-per-program-type limit, and NSFC links the 2024 jump to its resubmission rule.
  - Use the median (+45.7%) or pooled (+47.6%) figure, not the mean (57%), when citing "average" growth.
- **The most informative public micro-signal is person-based data.** NIH's split between applications and unique applicants is the best available; few other funders publish unique-applicant counts. UKRI's diversity data and NSF's 3-year PI funding rate are partial exceptions.
- **Demand-management measures are themselves breaks** in 2024–2027:
  - NIH cap (Sep 2025)
  - ERC eligibility rules (WP2027)
  - SNSF caps (Apr 2026)
  - Wellcome rolling deadlines (Jul 2026)
  - RCN rolling intake (Oct 2023)
  - ARC EOI (DP25)
  - EPSRC/NERC resubmission bans (2025)

  AI-impact estimates using 2026 data must model these explicitly.

### Gaps
- The RoRI dataset gives only 2022–2026 (no pre-2022 baseline). Its series definitions are heterogeneous: single schemes vs whole-funder totals, calendar vs grant years. The "six countries" and the full list of RoRI partners not included were not cross-checked.
- No funder has published counts of AI-flagged or rejected applications.
- No Volkswagen Foundation, British Academy or Swiss partial-randomisation volume data were retrieved in this session.
- The Elsevier "Funding Forward" post and *Nature*'s editorial on the "AI grant flood" (d41586-026-01422-x) could not be accessed (403 or login).

## Q5. Which sources give long, consistent annual series suitable for a multi-funder panel with a 2023–2026 post-period, and what confounders matter?

### Takeaway
The strongest panel backbone is:
- **NIH:** 1970–2025 applications, 1998–2025 unique applicants, JSON/Excel
- **UKRI:** 2015-16 to 2025-26 by council, Excel
- **NSF:** FY2012–FY2025 from digests, AFR and dashboard
- **JSPS KAKENHI:** 1996–2025
- **ERC:** per call since 2007, Excel export
- **MSCA:** PF 2021–2025, plus H2020 IF
- **Per-competition series:** CIHR (2016–), ANR (yearly), NWO (yearly), VR (2015–)

Post-2022 comparisons must handle:
- US 2025 funding shocks and the NIH cap from Sep 2025
- the UK's 2024 Horizon re-association
- Horizon programme-cycle effects
- UKRI's 2025-26 funding pauses and series revision
- rule changes: ARC EOI, RCN rolling intake, SNSF and ERC limits, NSF no-deadline policies
- definitional differences: submitted vs eligible vs evaluated, decision-year vs submission-year, resubmissions collapsed or not

### Cited Findings
- **Panel-readiness summary** (each row's facts are sourced in Q1–Q3):

| Funder / series | Counts | Start → latest | Granularity | Breakdowns | Access / format | Known breaks |
|---|---|---|---|---|---|---|
| NIH RPG and R01-equivalent applications, awards, success | applications (resubmissions within FY collapsed), awards | 1970 → FY2025 | federal FY | IC, activity code, type, sex, career stage | Data Book JSON API; Excel Table 218 — [API](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=20), [xlsx](https://report.nih.gov/reportweb/web/displayreport?rId=665) | cap from 25 Sep 2025 ([NOT-OD-25-132](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html)); FY2025 forward funding ([Nexus](https://www.grants.nih.gov/news-events/nih-extramural-nexus-news/2026/03/fiscal-year-2025-by-the-numbers-extramural-grant-investments-in-research)) |
| NIH unique applicants (RPG, R01-equivalent investigators) | persons (contact PIs + MPIs) | 1998 → FY2025 | FY | funded vs all; career stage | JSON API — [report 164](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=164) | same as above |
| NIH F31/F32/T32/K | applications, awards | 1997/98 → FY2025 | FY | IC, activity code | JSON API — [report 61](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=61) | — |
| NSF competitive proposals | proposals acted on, awards, funding rate; 3-year unique-PI rate | FY2012 (digest; reports since 1977) → FY2025 | FY | directorate, state, PI demographics | PDF digest; AFR; Tableau — [digest](https://nsf-gov-resources.nsf.gov/2023-06/FY_2021_Merit_Review_Digest.pdf), [AFR](https://nsf-gov-resources.nsf.gov/pubs/2025/nsf25002/pdf/nsf25002.pdf), [dashboard](https://www.nsf.gov/about/about-nsf-by-the-numbers) | no-deadline policies from ~FY2019 |
| UKRI | applications received; assessed and awarded by decision year | 2015-16 → 2025-26 | UK financial year | council, category, organisation, region | Excel — [2015–2026 xlsx](https://www.ukri.org/wp-content/uploads/2026/07/160726-UKRI-investments-and-outputs-data-2015-2026.xlsx) | Innovate UK break (2017-18); 2026 revision; 2025-26 funding pauses |
| ERC (StG/CoG/AdG/SyG/PoC) | submitted (press), eligible/evaluated (dashboard), granted | 2007 → 2026 calls | call (deadline date matters) | domain, panel, country, gender | Excel export / dashboard / press — [ERC stats](https://erc.europa.eu/statistics-0) | first Horizon Europe call 2021; UK association (WP2024); 2027 eligibility rules |
| MSCA PF (Horizon Europe) | submitted / eligible / evaluated, funded | 2021 → 2025 (H2020 IF 2014–2020 not retrieved) | annual call | EF/GF, panel, country, nationality | dashboard; press; NCP PDFs — [FECYT](https://www.horizonteeuropa.es/sites/default/files/noticias/24042026_MSCA-PF%20Resultados%202025.pdf) | UK association; ERA Fellowships |
| JSPS KAKENHI | new applications, new adoptions | 1996 → FY2025 (chart); JSPS tables cover more | Japanese FY | category, field, institution | PDF / HTML — [JSPS](https://www.jsps.go.jp/file/storage/kaken_27_kdata_g_4551/2-1_r7.pdf) | category reforms (not checked) |
| NSFC | applications received/accepted, funded | 2025–2026 verified; annual notices go back further | annual centralized reception | programme | notices / news — [stdaily](https://www.stdaily.com/web/gdxw/2026-08/26/content_569790.html) | programme reclassification (Youth A/B/C) |
| CIHR Project Grant | applications submitted, funded | 2016 → Fall 2025 (verified 2024–2025) | competition (2 per year) | career stage, gender, pillar, province | HTML — [Fall 2025](https://cihr-irsc.gc.ca/e/54594.html) | budget cut 23.5% (Fall 2025) |
| ANR AAPG | eligible pre-proposals, step-1 and final selection | yearly (2025–2026 verified) | annual | instrument | HTML / PDF — [ANR](https://anr.fr/fr/actus/details/news/aapg-appel-a-projets-generique-2026-les-resultats-de-letape-1/) | two-stage process; PRCE single-stage from 2026 |
| VR (NT project grants) | applications, success | 2015 → 2025 | annual call | gender, institution | PDF (SLU compile) — [SLU](https://internt.slu.se/globalassets/mw/externfinansiering/vr_ntsve_from2015_251030.pdf) | — |
| RCN FRIPRO | applications, success | 2018 → 2026 | annual, then rolling | career stage | secondary — [UiB](https://ekstern.filer.uib.no/ledelse/Analysegruppen%20-%20nyhetsbrev/Analysegruppa-teikn-og-tal-i-tida-nr68.pdf) | rolling intake and quarantine from Oct 2023 |
| RoRI 12-funder tracker (ARC, BA, CIHR, ERC, KBF, la Caixa, MSHR-BC, NHMRC, UKRI, Wellcome, MSCA PF, NSFC) | applications, heterogeneous definitions per funder | 2022 → 2025 (2026 partial) | annual (funder-specific years) | funder, with funder notes | xlsx (Nature supplementary) — [xlsx](https://media.nature.com/original/magazine-assets/d41586-026-01297-y/52331462) | no pre-2022 baseline; mislabelled YoY sheet; UKRI includes Innovate UK; Wellcome 2022 = 2023 |

- **Specific confounders, sourced:**
  - US FY2025 award collapse and forward funding — [NIH Nexus](https://www.grants.nih.gov/news-events/nih-extramural-nexus-news/2026/03/fiscal-year-2025-by-the-numbers-extramural-grant-investments-in-research)
  - NIH 15% indirect-cost cap attempt (7 Feb 2025) — [NOT-OD-25-068](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-068.html)
  - NIH rescheduling of all October–November 2025 deadlines after the lapse in appropriations — [NOT-OD-26-005](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-005.html)
  - NIH ICs no longer relying on paylines from the January 2026 Council round — [NIH Nexus, Nov 2025](https://grants.nih.gov/news-events/nih-extramural-nexus-news/2025/11/implementing-a-unified-nih-funding-strategy-to-guide-consistent-and-clearer-award-decisions)
  - NIH modified peer review (30–35% discussed) through the January 2027 round — [NIH Nexus, Sep 2026](https://grants.nih.gov/news-events/nih-extramural-nexus-news/2026/09/continuing-modified-peer-review-processes-for-the-january-2027-council-round)
  - NSFC 2024 rule allowing General Program resubmission after two consecutive unsuccessful years, which drove the 2024 jump according to NSFC — [RoRI/Nature xlsx](https://media.nature.com/original/magazine-assets/d41586-026-01297-y/52331462)
  - ARC scheme restructuring and Wellcome programme changes (funder notes) — [RoRI/Nature xlsx](https://media.nature.com/original/magazine-assets/d41586-026-01297-y/52331462)
  - NSF awards falling to 8,377 in FY2025 — [NSF budget](https://nsf.gov/about/budget)
  - UK association to Horizon Europe covering WP2024 calls — [UKRI](https://www.ukri.org/apply-for-funding/horizon-europe/)
  - MSCA 2025 rise led by applicants outside the EU, 21% UK — [MSCA](https://marie-sklodowska-curie-actions.ec.europa.eu/news/msca-postdoctoral-fellowships-2025-proposals), [UKRO](https://www.ukro.ac.uk/news/msca-postdoctoral-fellowships-2025-receives-record-number-of-17058-proposals/)
  - UKRI 2025-26 funding pauses and the Innovate UK definitional revision — [UKRI 2026](https://www.ukri.org/publications/ukri-investments-and-outputs/statistical-publication-ukri-investment-and-outputs-april-2015-to-march-2026/)
  - SNSF 5% budget cut and caps — [Univ. Fribourg](https://www.unifr.ch/research/en/highlights/news/34146/important-changes-to-snsf-project-funding)
  - DFG inflation-driven decline in success rates — [DFG](https://www.dfg.de/resource/blob/399666/dfg-jb2025.pdf)
  - RCN FRIPRO rolling intake — [UiB](https://ekstern.filer.uib.no/ledelse/Analysegruppen%20-%20nyhetsbrev/Analysegruppa-teikn-og-tal-i-tida-nr68.pdf)
  - ARC DP25 EOI (search-sourced) — [ARC DP25](https://www.arc.gov.au/funding-research/funding-outcome/selection-outcome-reports/dp25-selection-report-funding-commencing-2025)
  - NSF no-deadline policies — [NSF digest](https://nsf-gov-resources.nsf.gov/2023-06/FY_2021_Merit_Review_Digest.pdf)
  - COVID-era spikes:
    - UKRI 2020-21: 37,451 assessed — [UKRI xlsx](https://www.ukri.org/wp-content/uploads/2026/07/160726-UKRI-investments-and-outputs-data-2015-2026.xlsx)
    - NIH 2021: 58,872 RPG applications — [NIH report 20](https://report.nih.gov/reportweb/api/databook/GetJsonData?reportId=20)
    - ERC StG 2021: 4,016 eligible — [Business Finland](https://www.businessfinland.fi/globalassets/finnish-customers/horizon-europe/tilastotietoa/call_specific_success_rates_11022026.pdf)

### Inferences
- **Recommended outcome variables:**
  - applications per call/year (submitted, or eligible where possible)
  - unique applicants where available (NIH)
  - success rate as a secondary outcome, because it mixes supply (budget) with demand
- **Timing:** align by submission deadline date, not call label or decision year. Treat the post-period as deadlines from roughly 2023 onward, since ChatGPT was released in late November 2022.
- **Comparator logic:** funders with built-in volume controls (KAKENHI per-person limits, NWO pre-proposals, ERC resubmission bans) show small rises. Funders without them (MSCA, ERC AdG/CoG in 2024–25, UKRI research councils in 2024-25, SNSF, CIHR, ANR) show large rises. That pattern is consistent with lower writing costs (AI), but also with budget shocks and new eligibility (UK re-association).
- **Candidate natural experiments:** a dose-response or difference-in-differences design could exploit:
  - the NIH cap (Sep 2025)
  - ERC eligibility rules (WP2027)
  - SNSF caps (Apr 2026)
  - Wellcome rolling deadlines (Jul 2026)
- **Cleanest single panel:** NIH (FY1998–2025, applications and unique persons), UKRI research councils (2015-16 to 2025-26), ERC by scheme (2007–2026 calls), MSCA PF/IF, KAKENHI (1996–2025), NSF (FY2012–2025) and CIHR. Add ANR, NWO, VR and NSFC as supplementary series.

### Gaps
- The only public cross-funder dataset found is the RoRI/Nature 2022–2026 xlsx. It has no pre-2022 baseline and its series definitions differ by funder, so a pre-period has to be rebuilt from each funder's own sources (NIH, UKRI, ERC, MSCA/H2020, NSFC, CIHR, NHMRC, ARC).
- ERC 2007–2020, MSCA-IF 2014–2020, NSFC 2015–2024 and DFG application counts need retrieval from tools or annual reports not accessed here.
- FY2026 and 2026-call data for NIH, NSF and UKRI will not be published until roughly early-to-mid 2027. The first year under NIH's cap therefore cannot yet be evaluated.
