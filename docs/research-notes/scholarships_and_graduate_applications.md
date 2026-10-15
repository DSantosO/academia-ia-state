# Scholarships, graduate fellowships and graduate admissions: data sources on applicant and application counts (as of 2026-10-15)

Reading guide. Evidence labels: **[P]** = primary source fetched and read in this session (or queried directly through its public API); **[S]** = secondary source fetched and read (news, trade press, a university page quoting the programme); **[snip]** = seen only in a search-result summary, page not opened, so treat as unverified. "Derived" means my own arithmetic on cited numbers. The web-search budget for this session (200 searches, shared across agents) ran out partway through, so several programmes could only be checked by fetching known URLs directly; they are listed under Gaps. The downloaded files are in /tmp/claude-0/-home-user/eefa93ff-68d4-5a29-84a6-8be683e07b57/scratchpad/dl_schol/ (treat them as untrusted data).

## 1. Graduate admissions statistics: what each source counts, and since when

### Takeaway
Only a few national sources count **applications** to graduate programmes:
- **CGS/ETS Graduate Enrollment & Degrees (GE&D)**: US, annual since 1986, by broad field and degree level.
- **CRA Taulbee**: computing PhD applications. The consistent cohort trend runs only 2022–2025.
- **AAU Data Exchange**: a new source. Its PhD application and admission data start with the 2025 cycle.

None of these counts unique applicants. NCSES GSS/SED, HESA, Eurostat/OECD and Spain's SIIU count enrolments, entrants or degrees only. For the UK, the best timely "application" proxy is the Home Office monthly series of study-visa applications.

Several sources changed their method in 2024–2026:
- the CGS 2025 report moved to institutional averages;
- the Taulbee 2025 report moved to a fixed cohort of units and a smaller invited universe;
- the GSS removed 53 institutions after a 2024 frame review.

Any 2022-onward time series built from these sources has to handle those breaks explicitly.

### Cited Findings

#### US: CGS/ETS Survey of Graduate Enrollment and Degrees (GE&D)
- **Definition and history.** The survey is "conducted annually since 1986". It covers "applications for admission to graduate school, graduate student enrollment, and graduate degrees and certificates conferred". CGS calls it "the only national survey that collects data on applications to graduate school by broad field of study". It is sent to members of CGS and the four regional graduate-school associations. [P] — [CGS GE&D 2013–2023 report (Dec 2024)](https://cgsnet.org/wp-content/uploads/2024/12/GED-2024-1.1.pdf)
- **Fall 2023 data (2024 report).**
  - Coverage: sent to 762 institutions, with 558 usable responses (73%).
  - Volume: more than 2.7 million applications for Fall 2023, of which about 1.9 million were for master's/other programmes and about 817,000 for doctoral programmes.
  - Acceptance: 21.0% of doctoral applications and 50.6% of master's/other applications were accepted. Doctoral programmes at private non-profit R1s accepted 12.0%.
  - "Master's/other" includes graduate certificates and education-specialist programmes.
  - [P] — [CGS GE&D 2024 report](https://cgsnet.org/wp-content/uploads/2024/12/GED-2024-1.1.pdf)
- **Trend method up to 2024.**
  - Applications rose 5.6% from Fall 2022 to Fall 2023 "at the institutions that responded … in both 2022 and 2023" (a matched-respondent method).
  - By degree level: doctoral +3.7%, master's/other +6.4%.
  - The ten-year average annual growth rate was 3.7% (2013–2023). Appendix C holds the 2013–2023 trend tables.
  - Breakdowns: broad field (11), degree level, Carnegie class, public/private, gender, race/ethnicity, citizenship (US vs temporary resident).
  - [P] — [CGS GE&D 2024 report](https://cgsnet.org/wp-content/uploads/2024/12/GED-2024-1.1.pdf)
- **Fall 2024 data (the "Graduate Enrollment and Degrees 2025" report, published Dec 2025).**
  - Coverage: launched Nov 2024 and sent to 760 institutions; 536 gave usable responses (71%).
  - Applications: 899,141 doctoral and 1,961,548 master's/other. Accepted: 168,015 doctoral (19%) and 1,016,113 master's/other (52%).
  - Top doctoral fields by applications: Biological & Agricultural Sciences 125,185; Social & Behavioral 123,853; Engineering 116,249.
  - Top master's/other fields: Mathematics & Computer Sciences 330,894; Business 276,825; Engineering 206,419.
  - [P] — [CGS GE&D 2025 report](https://cgsnet.org/wp-content/uploads/2025/12/CGS_GED-2025_Report_Final.pdf); [appendices A–E](https://cgsnet.org/wp-content/uploads/2025/12/CGS_GED-2025_Appendices-A-E_Final.pdf); [landing page](https://cgsnet.org/data-insights/admissions-enrollment-and-completion/graduate-enrollment-and-degrees)
- **Method break in the 2025 report.**
  - One- and five-year comparisons are now "based on institutional averages rather than totals", grouped by institution size: small up to 1,050 graduate students, medium 1,051–3,050, large 3,051 or more.
  - CGS says the results are "descriptive … rather than direct longitudinal trends".
  - Results by Carnegie class were dropped because of the new Carnegie system.
  - Average applications per institution:
    - large: 12,776 (2024), 12,221 (2023), 9,645 (2019)
    - medium: 2,695, 2,807, 1,902
    - small: 616, 619, 510
  - Field pattern: average Mathematics & Computer Sciences applications "dropped rather sharply across institution sizes, likely due to a lower international student application base". Doctoral averages rose across all sizes, while master's averages fell at small and medium institutions.
  - [P] — [CGS GE&D 2025 report](https://cgsnet.org/wp-content/uploads/2025/12/CGS_GED-2025_Report_Final.pdf)
- **Derived comparison, master's/other Mathematics & Computer Sciences.** Applications went from 409,358 (Fall 2023, 558 respondents) to 330,894 (Fall 2024, 536 respondents). The respondent sets differ, so this is indicative only. [P] — [2024 report](https://cgsnet.org/wp-content/uploads/2024/12/GED-2024-1.1.pdf); [2025 report](https://cgsnet.org/wp-content/uploads/2025/12/CGS_GED-2025_Report_Final.pdf)
- **CGS forecast (not data).** The 2025 report predicts that "2025 international graduate enrollment will likely see a steep decline". [P] — [CGS GE&D 2025 report](https://cgsnet.org/wp-content/uploads/2025/12/CGS_GED-2025_Report_Final.pdf)
- **Other CGS products in the site feed.**
  - "Preliminary Graduate Enrollment and Degrees Data Dashboard" (11 Sep 2025)
  - "Graduate Enrollment and Degrees Fine Fields 2024 Dashboard" (17 Feb 2026)
  - "2026 Graduate Enrollment and Degrees: Training Webinar" (13 Aug 2026)
  - Downloadable Excel/PDF tables exist for the 2010–2020 edition.
  - [P] — [CGS search feed](https://cgsnet.org/search/graduate+enrollment+and+degrees/feed/rss2/); [figures & tables page](https://cgsnet.org/data-insights/admissions-enrollment-and-completion/graduate-enrollment-and-degrees-downloadable-figures-and-tables)
- **Timing of the Fall 2025 data.** The CGS/ETS 2025 survey reportedly launched 30 Sep 2025, "with results expected later than in past years". [snip] — [ETS CGS survey manual](https://www.ets.org/pdfs/cgs/CGS_NSF_survey_manual_NSF.pdf)

#### US: CGS international admissions surveys, and the 2025 flash survey
- CGS ran a separate international graduate applications/enrolment survey.
  - Editions were found for 2015 and for Fall 2020 (report released 24 Feb 2021). [P, by URL existence] — [2015 copy](https://www.minotstateu.edu/instplan/_documents/surveys/2015_cgs_int_grad_admissions.pdf); [Fall 2020 webinar slides](https://cgsnet.org/wp-content/uploads/2021/11/Webinar-Slides-Fall-2020-Intl-Report-Release-2021.02.24.pdf)
  - For Fall 2018 it reported international applications down about 4%, the second straight annual decline. [snip] — [legacy CGS news](https://legacy.cgsnet.org/news?page=8)
- **Flash survey, "Status of 2025 International Student Admissions" (2 Oct 2025).**
  - Sample: 433 member institutions, 17% response rate.
  - Findings: doctoral students' acceptance of offers "remained steady or rose", while master's acceptance declined.
  - Reasons for declining offers, ranked: visa-related barriers, cost, political unrest, personal safety.
  - The full brief is members-only.
  - [P] — [CGS](https://cgsnet.org/data-infographics/status-of-2025-international-student-admissions)

#### US/Canada: CRA Taulbee Survey (computing)
- **Edition and coverage.** 2025 is the 55th annual edition. The Main Survey was open Oct 2025–Feb 2026, after the 24 Jan 2026 deadline was extended.
  - Response: 141 of 226 invited units (62.3%): 133 US and 8 Canadian.
  - Reference periods: degrees and enrolment are for 2024–25; new students are for 2025–26.
  - [P] — [Taulbee 2025 methods](https://datavisualization.cra.org/TaulbeeReports/2025/methods.html)
- **Frame and method break in 2025.**
  - The invited universe shrank from 314 units (2024; 157 responded, 50%) to 226 units (2025). By unit type: CS 210→176, CE 38→15, CA 36→19, IN 30→16.
  - The data platform changed to Alchemer, with pre-registration and named data liaisons.
  - Trend figures now use "section cohorts" of units that reported in every year 2020–2025. This is "a change from prior years, when trends were reported as the combined totals of all responding units."
  - [P] — [methods](https://datavisualization.cra.org/TaulbeeReports/2025/methods.html); [doctoral section](https://datavisualization.cra.org/TaulbeeReports/2025/doctoral.html)
- **PhD applications, 2025 cross-section.**
  - 47,267 applications reported by 125 units, 77.1% of them international.
  - Breakdowns by gender, and by race/ethnicity for domestic applicants.
  - PhD acceptances: 5,955 (141 units), 71.3% international.
  - [P] — [Taulbee 2025 doctoral](https://datavisualization.cra.org/TaulbeeReports/2025/doctoral.html)
- **PhD applications, cohort trend (63 units).**
  - International: 15,469 (2022) → 29,071 (2025), +87.9%.
  - Domestic: 4,444 → 6,419, +44.4%.
  - New CS doctoral enrolments peaked at 1,714 in 2021 and were 1,446 in 2025, down 15% from 2024.
  - [P] — [Taulbee 2025 doctoral](https://datavisualization.cra.org/TaulbeeReports/2025/doctoral.html)
- **New 2025 items on AI programmes.** Many standalone AI degrees are not counted in Taulbee totals.
  - Among responding units, 15.4% house an AI master's programme and 2.9% an AI doctoral programme.
  - Of 53 units answering the inclusion question for doctoral AI degrees, 44 (83%) do **not** include them in their Taulbee figures.
  - [P] — [Taulbee 2025 AI & DS programs](https://datavisualization.cra.org/TaulbeeReports/2025/ai_ds_programs.html)

#### US: AAU Data Exchange PhD admissions (new, from the 2025 cycle)
- **Fall 2026.** The AAU Data Exchange covers 55 member institutions.
  - International applications to US doctoral programmes fell 21%, "fueling a 17 percent drop in international admissions".
  - Overall doctoral admissions fell 15%, which AAU attributes to federal research funding uncertainty.
  - [P, citing AAU] — [NAFSA/JBI Fall 2026 outlook (PDF, created Aug 2026)](https://www.nafsa.org/sites/default/files/media/document/Fall_2026_International_Student_Economic_Snapshot_NAFSA_JBI.pdf), which cites [AAU release](https://www.aau.edu/newsroom/new-phd-admissions-data-show-threat-us-stem-workforce). The AAU site blocked automated access.
  - Domestic PhD applications rose 3% (55 institutions). [S] — [The College Fix, 14 Aug 2026](https://www.thecollegefix.com/ph-d-admissions-fell-15-over-past-year-as-international-applications-drop/)
- **Fall 2025.** New PhD enrolment reportedly fell 11% at 42 AAU schools. AAU reportedly says no comparable data exist before the 2025 cycle. [snip] — [AAU](https://www.aau.edu/node/37031); [AACN summary](https://www.aacnnursing.org/news-data/all-news/article/rounds-with-leadership-safeguarding-the-future-of-phd-education)

#### US: NCSES Survey of Graduate Students and Postdoctorates (GSS)
- **Definition and history.** An annual census since 1966 of US academic institutions granting research-based master's or doctoral degrees in science, engineering and health (SEH). It counts **enrolled** graduate students (full-time, part-time, first-time full-time) and postdocs. It has no application data. [P] — [NCSES InfoBrief NSF 26-308 (18 Feb 2026)](https://ncses.nsf.gov/pubs/nsf26308)
- **2024 cycle (Fall 2024).** 23,121 organisational units at 635 institutions.
  - Data tables: NSF 26-307, released 18 Feb 2026.
  - Next release listed for 18 Nov 2026.
  - [snip, consistent with InfoBrief] — [NSF 26-307](https://www.ncses.nsf.gov/pubs/nsf26307)
- **Fall 2024 key figures.**
  - Full-time master's: 322,037 (−1.0%). Full-time doctoral: 274,601 (+2.3%).
  - Temporary-visa first-time full-time master's: 77,702 → 61,263 (−21.2%). Temporary-visa full-time doctoral: +5.3%.
  - Postdocs: 69,877, a record (+6.1%).
  - [P] — [NSF 26-308](https://ncses.nsf.gov/pubs/nsf26308)
- **Break.** The 2024 eligibility review dropped 53 institutions (0.8% of graduate students). NCSES publishes "2023adjusted" counts so the years can be compared. [P] — [NSF 26-308](https://ncses.nsf.gov/pubs/nsf26308)

#### US: NCSES Survey of Earned Doctorates (SED)
- **Definition.** An annual census of research-doctorate **recipients** (not applicants). Trend charts run 1958–2024.
- **2024 figures.** *Doctorate Recipients from U.S. Universities: 2024* (NSF 26-315) is dated 13 Mar 2026.
  - 58,131 doctorates in 2024 (+325); 45,929 in S&E.
  - Temporary-visa holders earned 38% of S&E doctorates: 61% in computer and information sciences, 54% in engineering, 51% in mathematics and statistics.
  - [P] — [NSF 26-315](https://ncses.nsf.gov/pubs/nsf26315)
- **Access.** Data tables are public; microdata are restricted and need a licence. [snip] — [data.gov SED 2024](https://catalog.data.gov/dataset/survey-of-earned-doctorates-2024)

#### US context: IIE international enrolment
- **IIE Fall 2025 Snapshot (825 institutions).**
  - New international enrolment −17%; total international graduate enrolment −12%.
  - Of institutions reporting declines, 96% cited visa application concerns and 68% travel restrictions.
  - **Open Doors 2025 (2024/25):** graduate students −3%, new international enrolment −7%.
  - [S] — [The PIE News, 17 Nov 2025](https://thepienews.com/new-international-enrolments-in-us-down-17-this-fall/)

#### Comparators that publish clean application data
- **GMAC Application Trends Survey (graduate business).**
  - 2025 survey: 1,172 programmes at 326 schools in 41 countries, fielded June–Aug 2025, released 21 Oct 2025.
  - Applications +7% globally. US programmes about −1 point.
  - Fewer applications in two-thirds of UK programmes and 84% of Canadian programmes.
  - International applications +42% in East/Southeast Asia and +26% in India.
  - MS Business Analytics declined for a second year.
  - [P] — [GMAC press release](https://www.gmac.com/why-gmac/gmac-news/gmac-press-releases/global-demand-for-business-education)
  - 2024 growth was a record 12%. [snip] — [EFMD blog](https://blog.efmdglobal.org/2025/11/03/gmac-application-trends-survey-2025/)
- **LSAC (US law, JD).** Publishes **both unique applicants and applications**.
  - 2026 cycle: 82,487 applicants (+7.9% vs 2025, +27.4% vs 2024) and 579,839 applications (+10.8%, +35.5%).
  - [P] — [LSAC "Keeping Up to Data", Sept 2026](https://www.lsac.org/podcast/keeping-data-september-2026)
  - Derived applications per applicant: about 6.61 (2024), 6.85 (2025), 7.03 (2026).
  - The 2025 cycle had +18.3% applicants. [snip] — [TaxProf Blog, 26 Aug 2026](https://taxprofblog.aals.org/2026/08/26/increases-in-law-school-applications/?nb=1)

#### UK: HESA (enrolments and entrants) and Home Office (visa applications)
- **HESA 2024/25 student data (released 27 Jan 2026).**
  - 685,565 international students (about −6%), the second consecutive annual fall.
  - Non-EU entrants −5.5%; EU entrants −4.1%.
  - Non-EU taught postgraduate enrolments about −10%; non-EU research postgraduate enrolments +10.5%.
  - Non-EU entrants by country: India −12%, China −5%, Nigeria −33%.
  - HESA counts enrolments and entrants, not applications.
  - [S] — [ICEF Monitor, 28 Jan 2026](https://monitor.icef.com/2026/01/uk-international-student-numbers-fall-for-second-year-especially-in-postgraduate-programmes)
  - The same article also says new international PG students fell about 3% overall, which does not reconcile with the −10%/−8% non-EU/EU figures. Check against HESA.
- **Times Higher Education on the same data.** About 10% fewer postgraduate taught and master's-taught entrants in 2024-25, after a 4% drop the year before. [snip] — [THE](https://www.timeshighereducation.com/news/masters-plunge-10-cent-amid-record-fall-overseas-students)
- **Home Office "Monthly entry clearance visa applications" (provisional; series from Jan 2022; published 13 Aug 2026).**
  - Sponsored-study **main applicants**, year ending July 2026: 381,500 (−11% on the prior year).
  - **Dependants:** 19,200 (−6%), which is 87% below the year ending Dec 2023, "following rule changes that came into effect from 1 January 2024".
  - Applications peak in August.
  - [P] — [gov.uk July 2026 release](https://www.gov.uk/government/statistics/monthly-entry-clearance-visa-applications-july-2026/monthly-entry-clearance-visa-applications-july-2026)
  - Year ending April 2026: 407,200 main applicants (−4%). [snip] — [April 2026 release](https://www.gov.uk/government/statistics/monthly-entry-clearance-visa-applications-april-2026/monthly-entry-clearance-visa-applications-april-2026)

#### EU: Eurostat UOE education statistics (enrolments, entrants, graduates)
- **Datasets (verified through the Eurostat API on 2026-10-15).**
  - Enrolment by ISCED level: `educ_uoe_enrt01`, metadata coverage 2005–2024, last update 06.10.2026.
  - New entrants: `educ_uoe_ent01`, `educ_uoe_ent02` (2012–2024).
  - Graduates: `educ_uoe_grad01`, `educ_uoe_grad02`; doctoral graduates per 1,000 aged 25–34: `educ_uoe_grad06`, `educ_uoe_grad07`.
  - Mobile students by country of origin: `educ_uoe_mobs02` (2012–2024).
  - There is **no applications dataset**.
  - [P] — [Eurostat catalogue (TOC)](https://ec.europa.eu/eurostat/api/dissemination/catalogue/toc/txt?lang=en)
- **ISCED 8 (doctoral) enrolment, `educ_uoe_enrt01`.**
  - EU27: 626,363 (2013) → 726,765 (2024). No EU27 values before 2013.
  - Spain: 23,650 (2013), 55,628 (2016), 85,480 (2018), 99,422 (2024).
  - [P] — [Eurostat API query](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/educ_uoe_enrt01?format=JSON&lang=EN&geo=EU27_2020&geo=ES&isced11=ED8&sex=T&sector=TOT_SEC&worktime=TOTAL&unit=NR)

#### Spain: Ministry "Datos y Cifras del Sistema Universitario Español" (DyC) and SIIU
- **DyC.** An annual synthesis built "dentro del contexto del SIIU".
  - Demand ("demanda" = *preinscritos en primera opción*) and the preference rate are published for **Grado** at public in-person universities only.
  - For Máster and Doctorado it reports enrolment, new entrants, graduates and theses, but no applications.
  - 2021–22: doctoral enrolment 93,652 (+4%), of whom 28% had foreign nationality.
  - [P] — [DyC 2023 (PDF)](https://www.ciencia.gob.es/dam/jcr:d2738536-6a67-43bf-b174-a0fb033b3fc4/DyC_2023.pdf)
- **Programme-level demand.** University quality reports publish demand for individual master's programmes. Example: a Universidad de Cádiz master's reported a 131.43% preference rate (first-choice pre-registrations ÷ places) in 2025–26. [snip] — [UCA](https://ccsociales.uca.es/master-dtur-planificacion-informacion-dirigida-a-futuros-alumnos/)

#### Summary catalogue: admissions and enrolment sources

| Source | Unit counted | Coverage start → latest | Granularity and breakdowns | Access | Breaks | AI-analysis fit |
|---|---|---|---|---|---|---|
| [CGS/ETS GE&D](https://cgsnet.org/data-insights/admissions-enrollment-and-completion/graduate-enrollment-and-degrees) | Applications received (not people), offers, first-time and total enrolment, degrees | Annual since 1986 → Fall 2024 (report Dec 2025); Fall 2025 pending | National; broad field ×11, degree level, citizenship, gender, race; institution size (2025) or Carnegie (≤2024) | Free PDF reports and appendices; older Excel tables; dashboards | 2025 report switched to institutional averages and dropped Carnegie; respondent set varies (558→536) | Medium. Long pre-2022 baseline, but applications ≠ applicants, and the 2025 method break sits inside the post-GenAI window |
| [CRA Taulbee](https://datavisualization.cra.org/TaulbeeReports/2025/) | Department-reported PhD applications and acceptances; new and total enrolment | 55th edition (2025); cohort trend for applications 2022→2025 | Computing units (CS/CE/IN/CA); domestic/international; gender; race (domestic) | Free HTML/Quarto report; dashboard | 2025 cohort method; invited universe 314→226 | High for computing and AI-adjacent fields, but the short pre-period and summing across departments (people counted several times) are drawbacks |
| AAU Data Exchange (via [NAFSA](https://www.nafsa.org/sites/default/files/media/document/Fall_2026_International_Student_Economic_Snapshot_NAFSA_JBI.pdf)) | PhD applications and admissions, domestic/international | 2025 cycle → Fall 2026 | 55 AAU institutions (42 in 2025) | Press releases only; underlying data member-only | Panel size changed 42→55 | Low–medium. No pre-GenAI baseline |
| [NCSES GSS](https://ncses.nsf.gov/pubs/nsf26308) | Enrolled SEH graduate students and postdocs | 1966 → Fall 2024 (next 18 Nov 2026) | Institution/unit, field, visa status, full/part-time | Free data tables | 2024 frame review ("2023adjusted") | Low for applications; useful as an enrolment outcome and visa control |
| [NCSES SED](https://ncses.nsf.gov/pubs/nsf26315) | Research-doctorate recipients | 1958 → 2024 | Field, citizenship, sex, plans | Tables free; microdata licensed | — | Low (lags entry by 5 or more years) |
| [HESA](https://monitor.icef.com/2026/01/uk-international-student-numbers-fall-for-second-year-especially-in-postgraduate-programmes) | Enrolments and entrants by level and domicile | → 2024/25 (Jan 2026) | PGT/PGR, domicile, subject | HESA open data | Start year and Data Futures break not verified (see Gaps) | Low for applications; outcome control |
| [Home Office visa applications](https://www.gov.uk/government/statistics/monthly-entry-clearance-visa-applications-july-2026/monthly-entry-clearance-visa-applications-july-2026) | Study-visa applications (main applicants, dependants) | Monthly from Jan 2022 → Jul 2026 | Monthly; nationality (in tables) | gov.uk release and tables | Dependants rule from 1 Jan 2024 | Medium as an international-demand proxy, not for AI per se |
| [Eurostat UOE](https://ec.europa.eu/eurostat/api/dissemination/catalogue/toc/txt?lang=en) | Enrolments, new entrants, graduates, mobile students by ISCED | 2013 (ISCED 2011) → 2024 | Country, ISCED 6/7/8, sex, field, origin | Free API (JSON/SDMX) | Country reporting shifts (e.g. Spain ISCED 8) | Low (no applications) |
| [Spain DyC/SIIU](https://www.ciencia.gob.es/dam/jcr:d2738536-6a67-43bf-b174-a0fb033b3fc4/DyC_2023.pdf) | Grado demand (first-choice pre-registrations); Máster/Doctorado enrolment only | Annual → DyC 2023 verified | Branch, university, region | Free PDF and SIIU tables | — | Low for graduate level |
| [GMAC ATS](https://www.gmac.com/why-gmac/gmac-news/gmac-press-releases/global-demand-for-business-education) | Programme-reported application volume changes | Annual → 2025 (Oct 2025) | Programme type, region, international/domestic | Summary free; full report gated | Respondent set varies | Medium (business-school comparator) |
| [LSAC](https://www.lsac.org/podcast/keeping-data-september-2026) | Unique applicants **and** applications | → 2026 cycle | National; demographics | Free volume summaries | — | High as a comparator for applications per applicant |

### Inferences
- **Applications are not applicants.** None of the graduate-admissions sources (CGS, Taulbee, AAU) counts unique applicants. An AI-driven rise in applications per applicant (cheaper tailoring of statements) would show up as a "demand" increase. Separating the two needs a source that publishes both, such as LSAC. Within-programme funnel ratios can also help, for example Rhodes US "began application" vs "endorsed".
- **Domestic and international trends diverge.** The Taulbee cohort shows international PhD applications nearly doubling from 2022 to 2025 while new enrolments fell. AAU shows international PhD applications −21% against domestic +3% for Fall 2026. Domestic-only series are therefore the cleaner test bed for any AI effect, because they are less exposed to US visa shocks.
- **Spain's ISCED 8 jump between 2013 and 2018 looks like a reporting or regulatory artefact.** A plausible cause is the transition of doctoral programmes to RD 99/2011 (inference, not verified). Country doctoral series need checking for breaks before use.
- **Method breaks overlap the GenAI window.** CGS 2025 averages and the Taulbee 2025 cohort and frame change both fall in 2024–2026. Any pre/post-ChatGPT comparison must be built on matched or constant-panel data, not on headline totals.

### Gaps
- **OECD Education at a Glance.** oecd.org returned 403 to automated fetches and the search budget was exhausted. From background knowledge (unverified this session), EAG/UOE publish enrolment, entrants and graduates by ISCED level, but no applications. Verify the edition dates (EAG 2025 and 2026).
- **UK postgraduate applications.** I could not verify any comprehensive national series (for example UCAS Postgraduate coverage or DfE initial teacher training application statistics). Background knowledge (unverified) suggests no comprehensive national UK PG applications series exists.
- **HESA details.** Not verified: the series start year, the Data Futures (2022/23) comparability break, and the HESA primary release page itself (hesa.ac.uk returned 403).
- **Taulbee application items.** The first year these were collected was not found; the cohort chart starts in 2022. Older Taulbee PDFs would need checking.
- **CGS GE&D Fall 2025 data.** Not yet located; the Fall 2025 survey was reportedly delayed. Microdata or institution-level files are not public.
- **CGS international survey.** I could not confirm the year it was discontinued, or its first edition (believed 2004; unverified).
- **AAU primary release.** Blocked by Cloudflare. Field breakdowns and the 2025 (42-school) figures are unverified.
- **Spain beyond DyC 2023.** I could not verify the "DyC 2025–2026" edition, or whether SIIU publishes máster pre-registration demand nationally.

## 2. Competitive scholarships and fellowships: which publish applicant counts, and where

### Takeaway
Where they are published, programme applicant counts come almost entirely from **annual press releases**, not statistical series.

Consistent multi-year applicant numbers were found for:
- **NSF GRFP** (applications 2016–2021 in NSF outreach slides; about 14,000 in 2026), plus a public **award and honourable-mention list for every year 1952–2026**;
- **Rhodes (US)**: began / endorsed / finalists / scholars;
- **Marshall**: a detailed demographic funnel report;
- **Schwarzman**: record applicant pools announced each year;
- **Paul & Daisy Soros**: 3,070 in 2026, a record;
- **Hertz**: more than 1,450 applicants in 2026;
- **'la Caixa' INPhINIT**: 1,636 applicants for 65 fellowships in the round announced March 2024.

No current global or national applicant totals were found for Chevening, Fulbright, Gates Cambridge, Knight-Hennessy, DAAD, Erasmus Mundus (student level), FPU/FPI, AGAUR FI, MEXT, CSC (China), Australia Awards, Commonwealth or Churchill.

Several programmes changed eligibility or pool definitions in 2025–2026, which breaks comparability:
- GRFP excluded second-year graduate students (2025) and STEM education and the SBE directorate (FY27);
- the Rhodes Global constituency was suspended for the 2026–27 cycle.

### Cited Findings

#### NSF Graduate Research Fellowship Program (GRFP)
- **Applications (NSF outreach slides):** about 16,800 (2016), 13,200 (2017), 12,400 (2018), 12,200 (2019), 12,800 (2020), 12,600 (2021). Success rates were about 12–17%, with roughly 2,000 fellowships a year in 2010–2021. [P, NSF slides hosted by UIUC] — [NSF GRFP outreach deck](https://ws.engr.illinois.edu/sitemanager/getfile.asp?id=4885)
- **2012–2014:** more than 13,000 applications in 2012 and 2013, and more than 14,000 in 2014 with 2,000 awards. [snip] — [ASA blog, Apr 2014](https://community.amstat.org/blogs/steve-pierson/2014/04/11/11-statisticis-students-award-nsf-graduate-research-fellowship)
- **2026 competition.** Announced 13 Apr 2026: 2,500 fellowship offers from "nearly 14,000 applicants". [P] — [NSF news](https://www.nsf.gov/news/nsf-announces-2026-graduate-research-fellowship-program)
  - Nature reported 2,599 awards, a record.
  - Awards by field: AI/machine learning 103 (+17%); quantum science 53 (+39%); engineering 914 (35%); biological sciences 486 (19%).
  - At least 65 applications were returned without review (Jan–Apr 2026), and the call was issued more than two months late.
  - [S] — [Scientific American/Nature, Apr 2026](https://www.scientificamerican.com/article/nsf-awards-record-number-of-coveted-phd-fellowships-in-surprise-move)
- **Offered awards by year** (official list, queried 2026-10-15): 2010: 2,051; 2012: 2,067; 2014: 2,053; 2016: 2,048; 2018: 2,056; 2019: 2,052; 2020: 2,076; 2021: 2,074; 2022: 2,193; 2023: 2,555; 2024: 2,036; 2025: 1,500; 2026: 2,597.
  - Displayed honourable mentions (a lower bound, because some people opt out of display): 2022: 1,377; 2023: 801; 2024: 1,719; 2025: 2,534; 2026: 1,442.
  - The list covers every award year 1952–2026, with name, baccalaureate institution, field and current institution, and has an export link. It does **not** include applicants.
  - [P] — [research.gov GRFP Award Offers and Honorable Mentions List](https://www.research.gov/grfp/AwardeeList.do?method=loadAwardeeList)
- **2025–2027 changes** [S] — [AIP FYI, 28 Aug 2026](https://www.aip.org/fyi/nsf-graduate-research-fellowships-expected-to-fall-next-year):
  - **2025:** about 2,300 awards were planned, but 1,000 were selected in April 2025, with 500 more about two months later. Second-year PhD students and clinical psychology students were excluded without advance notice, and both exclusions were kept for 2026.
  - **FY2027 solicitation NSF 26-526** (issued 25 Aug 2026): about 1,500 awards estimated, depending on appropriations. STEM Education and Learning is excluded and the SBE directorate removed as a participating directorate. Applicants get fewer than 60 days to apply.
- **Application window for the 2027 competition:** applications due 19–23 Oct 2026. [snip/blog] — [grantedai blog](https://grantedai.com/blog/nsf-26-526-grfp-fy2027-october-19-23-deadlines-1500-fellowships-stem-education-deleted-wildlife-conservation-ineligible-strategy)

#### Rhodes Scholarship
- **US competition (announced 15 Nov 2025, class entering Oxford Oct 2026).** "Nearly 2,800 students began the application process", 965 received college endorsements from more than 264 institutions, 238 finalists were interviewed by 16 committees, and 32 were selected. The global class is "just over 100". [P] — [Rhodes Trust US press release (PDF)](https://www.rhodeshouse.ox.ac.uk/media2/ikolktw5/press_release_2025-final.pdf)
- **Global Rhodes constituency suspended** for the 2026–27 cycle. [snip/S] — [Cherwell, June 2026](https://www.cherwell.org/?p=195130); [Dartmouth fellowships office](https://students.dartmouth.edu/fellowships/postgraduate-opportunities/funding-grad-school-abroad/rhodes-scholarships)

#### Marshall Scholarships
- **"Application Demographics Report – 2026–2027 Cycle"** (applications collected summer 2025).
  - Funnel: 1,023 endorsed applicants (92 for one-year awards, 931 for two-year awards), 156 shortlisted, 43 selected.
  - Breakdowns: 8 US regions; gender (59.0% of endorsed applicants female); ethnicity; Pell-grant status; HBCU; endorsing-institution type (Ivy League 17.2% of endorsed vs 34.9% of those selected); first-choice UK university.
  - Format: Power BI PDF.
  - [P] — [Marshall Competition Report 2026–2027](https://www.marshallscholarship.org/wp-content/uploads/2026/04/Marshall-Competition-Report-2026_2027.pdf)
- **Winners announced 9 Dec 2025:** 43 selected from more than 1,000 applicants. [snip] — [Harvard Crimson](https://www.thecrimson.com/article/2025/12/9/marshall-scholars-2026/)

#### Schwarzman Scholars
- **Class of 2025–26 (announced 15 Jan 2025):** "nearly 5,000 candidates", 150 scholars, 38 countries, 105 universities. This was "the most applications" in the programme's ten-year history. [P] — [Schwarzman release](https://www.schwarzmanscholars.org/events-and-news/schwarzman-scholars-announces-tenth-class-150-exceptional-scholars-from-38-countries-to-join-prestigious-network-of-1300-young-global-leaders-record-high-applications-indicate-growing-interest-in/)
- **Class of 2026–27 (announced 15 Jan 2026):** "just over 5,800" candidates, a record; 150 scholars from 40 countries; about a 2.6% acceptance rate. [snip] — [Harvard Crimson](https://api.thecrimson.com/article/2026/1/17/2027-schwarzman-scholars)

#### Paul & Daisy Soros Fellowships for New Americans
- **Class of 2026:** 3,070 applications, "a new record" and "the most competitive in the Fellowship's 28-year history". 77 finalists and 30 fellows. [P] — [PD Soros](https://pdsoros.org/meet-the-class-of-2026/)

#### Hertz Fellowship
- **2026 cycle:** 54 finalists from "more than 1,450 applicants" (5 Feb 2026). [P] — [Hertz Foundation](https://www.hertzfoundation.org/news/54-finalists-named-for-the-2026-hertz-fellowships/)
- **Final class:** 19 fellows from "nearly 1,500 applicants" at more than 300 universities. [snip] — [Harvard College](https://college.harvard.edu/about/news/brief-harvard-college-students-alumni-awarded-2026-hertz-fellowships)

#### Knight-Hennessy Scholars (Stanford)
- **2025 cohort:** 84 scholars, 25 countries, 46 programmes. The release gives **no applicant count**. [P] — [Knight-Hennessy, 13 May 2025](https://knight-hennessy.stanford.edu/news/knight-hennessy-scholars-announces-2025-cohort-new-scholars)

#### Gates Cambridge
- **Class of 2026:** 68 scholars (51 PhD, 17 MPhil) from 25 countries, announced 16 Apr 2026; the US cohort of 26 was announced in February. No applicant count was found. [snip] — [Gates Cambridge, Class of 2026 story](https://www.gatescambridge.org/our-scholars/blog/shorthand_story/gates-cambridge-class-of-2026/); [US scholars](https://www.gatescambridge.org/about/news/2026-us-scholars-announced)
- **Earlier class sizes:** 2025: 95; 2024: 75; 2023: 77; 2022: 79. [snip] — [Gates Cambridge Class of 2024](https://www.gatescambridge.org/about/news/gates-cambridge-class-of-2024-announced); [Class of 2023](https://www.gatescambridge.org/about/news/gates-cambridge-class-of-2023-announced)

#### Chevening (UK FCDO)
- **Awards:** about 1,500 on offer for 2024/25. [snip] — [gov.uk news](https://www.gov.uk/government/news/chevening-scholarships-to-study-in-britain-british-embassy-welcomes-applications)
- **Applications:** only country-level counts appear in embassy statements, for example "9,800 plus applications" from Nigeria in the 2023/24 cycle. [snip/S] — [Daily Trust via PressReader](https://dailytrust.pressreader.com/article/282063396218436)
- **AI policy:** "Using artificial intelligence software to generate answers to Chevening's essay questions is strictly prohibited"; Chevening "uses tools to detect fraud, plagiarism, and AI-generated content"; applicants confirm they did not use AI. The page is undated. [P] — [Chevening FAQ](https://www.chevening.org/faqs/can-i-use-ai-to-help-me-write-my-application/)

#### Fulbright (US Student Program)
- **No national applicant totals were found.** A single university's committee reports 22 applicants for 2025–26 but only 5 for 2026–27 (deadline early Oct 2025). It cites "significant disruptions to the Fulbright programs in 2025" and applicant concerns over "privacy, safety/security, continuity". This is anecdotal, one campus only. [P] — [James Madison University committee report 2025–26](https://www.jmu.edu/academic-affairs/committees-and-taskforces/_files/pfac_2025-2026_report.pdf)

#### 'la Caixa' Foundation
- **Round announced 12 Mar 2024:** Doctoral INPhINIT 1,636 applications for 65 fellowships; Postdoctoral Junior Leader 547 applications for 40 fellowships. The call year is not stated; it is probably the 2023 call. [P] — [la Caixa media hub](https://mediahub.fundacionlacaixa.org/en/research-fellowships/fellowships/phd-fellowships/2024-03-12/hundred-researchers-receive-doctoral-postdoctoral-fellowships-5663.html)

#### Spain: FPU and FPI/AEI; Catalonia: AGAUR
- **FPU** (national pre-doctoral fellowships): 900 places in the 2024 call (applications 17 Jan–17 Feb 2025) and 870 in the 2025 call. No national application count was found. [snip] — [UGR](https://investigacion.ugr.es/print/pdf/node/4939); [CSIF](https://www.csif.es/es/noticia/portada/nacionaluniversidades/articulo/83786); [Ministry FPU 2024 page](https://www.ciencia.gob.es/Convocatorias/2024/FPU2024.html)
- **FPI-type pre-doctoral contracts.** These are attached to AEI "Generación de Conocimiento" projects. The 2024 call drew 7,190 project applications (+8.68%), and the provisional resolution (July 2025) funded 1,149 pre-doctoral contracts and 3,252 projects. These are project-level counts, not candidate applications. [snip] — [La Moncloa, 29 Jul 2025](https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/ciencia-innovacion-universidades/Paginas/2025/290725-inversion-investigacion.aspx)
- **Catalonia open data ("Estadístiques sobre convocatòries públiques en matèria d'R+D+I").**
  - Covers Generalitat human-resources calls since 2004. "Formació" includes the FI pre-doctoral grants.
  - It gives **recipients** by sex, amount and type of centre for 2004–2023. There are **no application counts**.
  - Derived training-category recipients: 2016: 977; 2019: 920; 2023: 1,009.
  - [P] — [Socrata API rsgi-8ymj](https://analisi.transparenciacatalunya.cat/resource/rsgi-8ymj.json)

#### DAAD and Erasmus Mundus
- **DAAD.**
  - Budget: €742.8 million in 2025. [P] — [DAAD facts & figures](https://www.daad.de/en/the-daad/what-we-do/facts-figures/)
  - Per-university "Förderbilanzen" (recipient counts; the file path indicates "ab 2010") report funded individuals, e.g. TUM 608 in 2024. Applications were not found. [snip] — [DAAD Förderbilanz 2024 (3a)](https://static.daad.de/media/daad_de/pdfs_nicht_barrierefrei/der-daad/foerderung-nach-daad-mitgliedshochschulen/foerderbilanzen-ab-2010/2024_3a_gef%C3%B6rderte_gesamt_absolut.pdf)
- **Erasmus Mundus Joint Masters.** The 2023 call is consortium-level: 94 project applications (+62%), 91 eligible, 34 selected. [P] — [EACEA overview of 2023 selection](https://erasmus-networks.ec.europa.eu/system/files/2025-02/1_Overview%20of%20the%20selection%20results%20EM.pdf)
  - The 2014–2020 statistical factsheets cover scholarship-holder mobility, not student applications. [P] — [EACEA factsheets](https://www.eacea.ec.europa.eu/news-events/news/statistical-factsheets-achievements-erasmus-mundus-joint-master-degrees-2014-2020-2021-05-20_en)

#### Summary: scholarship and fellowship applicant data

| Programme | Applicant metric | Latest | Multi-year availability | Where |
|---|---|---|---|---|
| NSF GRFP | Applications; offers; HM | ~14,000 apps / 2,500–2,597 offers (2026) | Apps: NSF slides 2016–21, releases 2012–14, 2026; awards 1952–2026 (official list) | [NSF](https://www.nsf.gov/news/nsf-announces-2026-graduate-research-fellowship-program); [research.gov](https://www.research.gov/grfp/AwardeeList.do?method=loadAwardeeList) |
| Rhodes (US) | Began / endorsed / finalists / selected | 2,800 / 965 / 238 / 32 (Nov 2025) | Annual US press releases (archive not compiled) | [Rhodes PDF](https://www.rhodeshouse.ox.ac.uk/media2/ikolktw5/press_release_2025-final.pdf) |
| Marshall | Endorsed / shortlisted / selected, with demographics | 1,023 / 156 / 43 (2026–27 cycle) | "Comparison report" format; earlier cycles not checked | [Marshall PDF](https://www.marshallscholarship.org/wp-content/uploads/2026/04/Marshall-Competition-Report-2026_2027.pdf) |
| Schwarzman | Candidates / scholars | ~5,800 / 150 (Jan 2026) | Annual releases ("record" in 2025 and 2026) | [Schwarzman](https://www.schwarzmanscholars.org/events-and-news/schwarzman-scholars-announces-tenth-class-150-exceptional-scholars-from-38-countries-to-join-prestigious-network-of-1300-young-global-leaders-record-high-applications-indicate-growing-interest-in/) |
| PD Soros | Applications / finalists / fellows | 3,070 / 77 / 30 (2026) | Annual class pages | [PD Soros](https://pdsoros.org/meet-the-class-of-2026/) |
| Hertz | Applicants / finalists / fellows | >1,450 / 54 / 19 (2026) | Annual releases | [Hertz](https://www.hertzfoundation.org/news/54-finalists-named-for-the-2026-hertz-fellowships/) |
| 'la Caixa' INPhINIT | Applications / awards | 1,636 / 65 (announced Mar 2024) | Annual award announcements (only one round verified) | [la Caixa](https://mediahub.fundacionlacaixa.org/en/research-fellowships/fellowships/phd-fellowships/2024-03-12/hundred-researchers-receive-doctoral-postdoctoral-fellowships-5663.html) |
| Chevening | Country-level application counts only; ~1,500 awards | — | Ad hoc embassy statements | [Chevening FAQ](https://www.chevening.org/faqs/can-i-use-ai-to-help-me-write-my-application/) |
| Knight-Hennessy, Gates Cambridge | Scholars only | 84 (2025); 68 (2026) | No applicant counts found | [KH](https://knight-hennessy.stanford.edu/news/knight-hennessy-scholars-announces-2025-cohort-new-scholars) |
| Catalonia (AGAUR FI etc.) | Recipients only | 2023 | 2004–2023 | [Socrata](https://analisi.transparenciacatalunya.cat/resource/rsgi-8ymj.json) |

### Inferences
- **GRFP's 2026 pool comes from a narrower eligible population.** Second-year graduate students were excluded from 2025, so "nearly 14,000" applicants in 2026 against about 12,600 in 2021 understates per-eligible-person growth. GRFP application counts therefore have a structural break at 2025. Award counts are also policy-driven and volatile (2,555 → 2,036 → 1,500 → ~2,597 → ~1,500 planned), so award-based success rates are not comparable across 2023–2027.
- **Records cluster in 2025–2026 at programmes with low application costs or broad eligibility.** Schwarzman reported records in 2025 and 2026, and PD Soros in 2026. Programmes that require institutional endorsement (Rhodes US, Marshall) cap volumes at the endorsement stage. The ratio of initiated to endorsed applications (Rhodes: about 2,800 to 965) is the funnel stage most likely to absorb any AI-lowered cost of starting an application.
- **Mapping to ChatGPT exposure** (inference from the cycle timing in these sources):
  - Cycles with deadlines in Oct–Nov 2023 are the first fully exposed. That means GRFP 2024 awards, the Rhodes and Marshall classes beginning 2024, and Schwarzman 2024–25.
  - Cycles with deadlines in Oct–Nov 2022 (GRFP 2023, Rhodes and Marshall classes beginning 2023) are essentially pre-exposure.
  - ChatGPT was released 30 Nov 2022, after those deadlines.

### Gaps
- **No applicant figures verified** (not reachable, or no figures found) for: Fulbright national totals (US Student and Foreign Student), Commonwealth Scholarships (CSC UK), Churchill (homepage has no applicant counts), Gates Cambridge and Knight-Hennessy (recent years), DAAD applications, Erasmus Mundus student scholarship applications, MSCA Doctoral Networks (proposal statistics by call), FPU national applications, AGAUR FI applications, Japan MEXT, China Scholarship Council, Australia Awards.
- **Missing GRFP years.** GRFP application counts for 2022–2025 are missing. NSF news URLs for those years could not be located, and searching was exhausted. NSF budget justifications or the GRFP office would be the place to check.
- **Earlier cycles not compiled.** Earlier Rhodes US releases and earlier Marshall demographic reports were not compiled into a series.
- **Unverified events.** The Fulbright Foreign Scholarship Board resignation (reported mid-2025) and the scale of Fulbright grant cancellations were not verified from primary sources.

## 3. Evidence (2023–2026) of application changes linked to generative AI, and the main confounders

### Takeaway
I found **no primary source that attributes a rise in graduate or scholarship applications to generative AI**. The verified evidence is of three kinds:
- **Policy responses** that create new data, for example Rhodes now records which AI tool, and which prompts, applicants used;
- research on **detecting** AI-written statements;
- record applicant pools in 2025–2026 at several fellowships, which are consistent with lower application costs but also with other explanations.

Meanwhile, US international demand and PhD intakes fell sharply in 2025–2026 because of visa and immigration policy and federal funding cuts. The UK's January 2024 dependants rule did the same for UK taught master's demand. These shocks dominate post-2022 aggregates and have to be modelled out.

### Cited Findings

#### AI policies (2024–2026) that shape or record applicant behaviour
- **Rhodes Trust guidance (last updated May 2026).**
  - Applicants attest that each statement is their "own work". They must declare who helped: faculty, advisors, friends and family, alumni, or "GenAI tools such as ChatGPT, Gemini, Grammarly", and "if you used GenAI, tell us which tool was used, and how you asked it to help/what prompts were used".
  - Unacceptable uses include "generating substantive content". GenAI is banned during interviews.
  - [P] — [Rhodes House guidance (PDF)](https://www.rhodeshouse.ox.ac.uk/files/candidate-guidance-genai-and-support-with-applications/)
- **Chevening.** AI-generated answers are "strictly prohibited", with detection tools and an attestation requirement. [P] — [Chevening FAQ](https://www.chevening.org/faqs/can-i-use-ai-to-help-me-write-my-application/)
- **Cornell graduate admissions.** Applicants must disclose any GenAI use; AI is banned during interviews. [snip] — [Cornell Graduate School](https://gradschool.cornell.edu/admissions/application-steps/important-application-policies/use-of-generative-ai-in-graduate-admissions-applications/)
- **CGS AI best-practices brief (Mar 2026).**
  - It frames AI as a tool to "process larger volumes" of applications.
  - It describes a Georgia Tech pilot (early 2025) of a machine-learning tool that predicts applicant success from application portfolios.
  - It offers no data on AI-written applications.
  - Its "applications … up 5.6%" figure reuses the one-year 2022→2023 GE&D change.
  - [P] — [CGS brief](https://cgsnet.org/wp-content/uploads/2026/03/Best-Practices-Brief-AI_Final-1.0.pdf)

#### Research on AI-written application materials
- **Scientific Reports (Nov 2024).** Detection models for AI-generated or AI-revised statements of intent and recommendation letters, using Fordham master's programmes in CS and data science. A universal detector "appears to be beyond current technology", but task-specific models reach high accuracy. [snip] — [DOAJ record](https://doaj.org/article/4dbc2ddc04474d2eba426256a1b6e537)
- **ETS research report (Gooch & Haviland).** A NAGAP pulse survey (Feb 2025) on acceptable AI use in graduate admissions by institutions and applicants. Its figures were not accessible (HTTP 502). [snip] — [ETS RR](https://rr.ets.org/index.php/etsrr/article/view/41)
- **Anecdotal.**
  - A Boston University professor reports near-identical AI-style inquiry emails from prospective students (op-ed, July 2026). [snip] — [Express Tribune](https://tribune.com.pk/story/2619331/bad-advice-to-aspiring-students)
  - UC Berkeley warned in Mar 2026 of fake AI-generated inquiries to faculty. [snip] — [Berkeley Security](https://security.berkeley.edu/node/2111)

#### 2023–2026 application patterns compatible with several explanations
- **Computing PhDs (Taulbee cohort, 2022 → 2025).** International applications +87.9% and domestic +44.4%, while new CS doctoral enrolments fell 15% in 2025. [P] — [Taulbee 2025](https://datavisualization.cra.org/TaulbeeReports/2025/doctoral.html)
- **Department-level examples.** Penn State EE PhD applications went 195 (2024) → 247 (2025) → 174 (2026 cohort). Texas A&M reported about −50% applications for Fall 2026. USC domestic applications rose about 15% while international applications fell. [S] — [IEEE Spectrum, 25 Mar 2026](https://spectrum.ieee.org/us-engineering-phd-enrollment-drop)
- **Fellowship records.** Schwarzman reported records in 2025 (~5,000) and 2026 (~5,800). PD Soros had 3,070 in 2026, a record. GRFP had about 14,000 applicants in 2026 despite tighter eligibility. [P] — [Schwarzman](https://www.schwarzmanscholars.org/events-and-news/schwarzman-scholars-announces-tenth-class-150-exceptional-scholars-from-38-countries-to-join-prestigious-network-of-1300-young-global-leaders-record-high-applications-indicate-growing-interest-in/); [PD Soros](https://pdsoros.org/meet-the-class-of-2026/); [NSF](https://www.nsf.gov/news/nsf-announces-2026-graduate-research-fellowship-program)
- **Applications per applicant (LSAC).** Rose modestly, from about 6.6 (2024) to about 7.0 (2026, derived). LSAC offers no explanation for this. [P] — [LSAC](https://www.lsac.org/podcast/keeping-data-september-2026)

#### Confounders, with dates
- **US funding and PhD intakes.**
  - AAU Fall 2026: doctoral admissions −15%, international PhD applications −21%, international admissions −17%, attributed to federal research-funding uncertainty. [P, citing AAU] — [NAFSA/JBI](https://www.nafsa.org/sites/default/files/media/document/Fall_2026_International_Student_Economic_Snapshot_NAFSA_JBI.pdf)
  - Department examples: UCLA scaled back after a more-than-$580M grant suspension (Aug 2025); Penn State lost DARPA CHIMES funding. [S] — [IEEE Spectrum](https://spectrum.ieee.org/us-engineering-phd-enrollment-drop)
  - Reported intake cuts: Caltech −40% new graduate students; MIT about 500 fewer. [snip] — [Becker's](https://www.beckershospitalreview.com/quality/hospital-physician-relationships/phd-programs-shrink-amid-federal-spending-cuts/)
- **US visa and immigration policy.**
  - A 16 Dec 2025 executive order restricts entry from 39 countries, with no F or J exceptions.
  - State Department non-immigrant visa issuance data have **not been published since September 2025**.
  - Common App international submissions −9% for 2026–27.
  - [P] — [NAFSA/JBI](https://www.nafsa.org/sites/default/files/media/document/Fall_2026_International_Student_Economic_Snapshot_NAFSA_JBI.pdf)
  - Visa approvals were paused for citizens of 75 countries in late Jan 2026, and a four-year cap on student visas was proposed. [S] — [IEEE Spectrum](https://spectrum.ieee.org/us-engineering-phd-enrollment-drop)
  - IIE Fall 2025: new international enrolment −17%; 96% of institutions with declines cite visa concerns. [S] — [PIE News](https://thepienews.com/new-international-enrolments-in-us-down-17-this-fall/)
  - CGS (Oct 2025): visa barriers were the top reason offers were declined. [P] — [CGS](https://cgsnet.org/data-infographics/status-of-2025-international-student-admissions)
- **US fellowship policy.**
  - GRFP: award cut (April 2025), eligibility changes (2025 and FY27), late call and applications returned without review (2026). [S] — [AIP FYI](https://www.aip.org/fyi/nsf-graduate-research-fellowships-expected-to-fall-next-year); [SciAm/Nature](https://www.scientificamerican.com/article/nsf-awards-record-number-of-coveted-phd-fellowships-in-surprise-move)
  - Fulbright disruptions in 2025. [P, one campus] — [JMU](https://www.jmu.edu/academic-affairs/committees-and-taskforces/_files/pfac_2025-2026_report.pdf)
- **UK.**
  - Dependants rule from 1 Jan 2024: dependant visa applications are 87% below the year ending Dec 2023. [P] — [Home Office](https://www.gov.uk/government/statistics/monthly-entry-clearance-visa-applications-july-2026/monthly-entry-clearance-visa-applications-july-2026)
  - HESA 2024/25: non-EU taught PG enrolments −10%; Nigeria −33%, India −12%. [S] — [ICEF](https://monitor.icef.com/2026/01/uk-international-student-numbers-fall-for-second-year-especially-in-postgraduate-programmes)
- **Market diversion.** GMAC 2025: Canada and UK programmes lost applicants while Asia and continental Europe gained. [P] — [GMAC](https://www.gmac.com/why-gmac/gmac-news/gmac-press-releases/global-demand-for-business-education)
- **Post-COVID rebound.** The CGS 2024 report describes interest as "high three years removed from the COVID-19 pandemic". Taulbee new CS doctoral enrolment peaked in 2021. [P] — [CGS 2024](https://cgsnet.org/wp-content/uploads/2024/12/GED-2024-1.1.pdf); [Taulbee](https://datavisualization.cra.org/TaulbeeReports/2025/doctoral.html)
- **Pool-definition changes.** Rhodes Global constituency suspended (2026–27) [snip — [Cherwell](https://www.cherwell.org/?p=195130)]. Taulbee and CGS method changes, and the GSS frame review (see section 1).

### Inferences
- **Identification approaches.** Credible AI-impact designs probably need:
  1. **Domestic-only** application series, to strip out visa shocks (Taulbee domestic; AAU domestic; GE&D citizenship splits);
  2. **funnel ratios** within programmes (initiated ÷ endorsed for Rhodes; endorsed ÷ shortlisted for Marshall; applications ÷ applicants for LSAC);
  3. **cross-programme contrasts**, comparing essay-heavy fellowships against test- or nomination-gated ones, and Chevening's prohibition-plus-detection regime against Rhodes's disclosure regime;
  4. event timing anchored on deadline cycles: Oct–Nov 2023 is the first fully exposed cycle for most fellowships.
- **Rhodes disclosure data.** Rhodes's new tool-and-prompt disclosure (May 2026 guidance) is a potential **direct measure** of GenAI use by applicants, if the Trust were to publish aggregates. It could be requested.
- **CS and AI-adjacent fields give opposite signals.** Applications surged while enrolments fell, and new AI degrees often sit outside Taulbee counts. A naive "AI boom → more applications" reading conflates field demand with AI-written applications.

### Gaps
- **No admissions or scholarship office statistic linking volume increases to GenAI was found.** This includes Chevening, Rhodes, Fulbright, UCAS postgraduate and graduate schools. The search budget ran out before searching residency or medical-school studies and Times Higher Education or University World News coverage, which may contain quantitative evidence such as detector-based prevalence of AI text in personal statements.
- **Missing survey figures.** The ETS/NAGAP survey results and any CGS survey of deans on AI in admissions could not be accessed.
- **Missing policy timeline.** The date Chevening introduced its AI prohibition and detection is unknown (the page is undated).

## 4. (Optional) Academic job-market application data

### Takeaway
No verified public source gives **applicants per faculty or postdoc posting** with history. Professional bodies publish **posting counts** or hiring outcomes instead:
- AEA JOE listing graphs and annual reports;
- the CRA Taulbee faculty hiring and fill rates;
- historic AMS data and anecdotes on applications per job.

Applicant-side data (for example EconJobMarket, MathJobs or AJO application counts) were not found publicly.

### Cited Findings
- **AEA Committee on the Job Market.** Publishes JOE job-listing graphs "updated weekly", a "Survey of Hiring Plans of US Economics Departments, Fall 2025" (1 Dec 2025), guidance for the 2025–26 cycle (2 Sep 2025) and the 2026–27 cycle (9 Sep 2026), and annual year-end reports in *AEA Papers and Proceedings*. The page gives no applicant counts. [P] — [AEA committee page](https://www.aeaweb.org/about-aea/committees/adhoc-job-market)
- **JOE annual Director's report.** Appears in *AEA P&P* (2026, vol. 116, pp. 822–824); access is gated. [snip] — [RePEc](https://econpapers.repec.org/RePEc:aea:apandp:v:116:y:2026:p:822-824)
- **CRA Taulbee 2025, faculty hiring outcomes (not applicants).**
  - Fill rates: assistant professors 78% (303 of 388 searches); associate 57%; full 72%; teaching professors 80%.
  - Of 98 units with an unfilled post, 46% cited declined offers and 21% the inability to find a qualified candidate.
  - [P] — [Taulbee 2025 faculty growth & attrition](https://datavisualization.cra.org/TaulbeeReports/2025/faculty_ga.html)
- **AMS.** A 2012 AMS Committee on the Profession report said MathJobs increased applications per job (no measured figure). Older AMS Employment Register ratios of applicants per position from the late 1980s–1990s are reported on a Purdue page. [snip] — [AMS CoProf 2012](https://community.ams.org/CoProf2012RepCouncil.pdf); [Purdue page](https://www.math.purdue.edu/~jlipman/Employment.html)

### Inferences
- **Proxy for applications.** Without applicant-side data, the only feasible public proxy for "applications per posting" is listing counts combined with survey-based supply (new PhDs from the SED; candidate surveys). Platform operators (AEA JOE Network, EJM, MathJobs, AJO, EURAXESS) would have to supply application counts directly.

### Gaps
- **Not verified because of the search limit:** MLA Job Information List reports, AMS Annual Survey recruitment data after 2018, Academic Jobs Online or MathJobs statistics, and EURAXESS posting statistics. None is known to publish applications per posting.
- **Gated JOE figures.** JOE listing counts for 2025–26 and their decline are behind the AEA graphs page or paywalled P&P reports, and were not extracted.
