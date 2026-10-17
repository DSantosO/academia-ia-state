# Reference database for paper/plos_one/draft_v3.md (Vancouver / PLOS style).
# Starts from refs_v2.py (which starts from refs.py) and adds the references needed for v3.
# Every added entry was checked on 17 Oct 2026 against Crossref (journal articles), the NCBI Books database (the
# E-utilities documentation) or the publisher's page, as noted after each entry. References that v2 cited only in the
# deleted "Implications" proposals (DORA, CoARA, McKiernan et al., Rice et al., the Commission's study and the proposal
# sources) stay in the database but are no longer cited in the article; the build lists only cited keys.
import importlib.util

_here = __file__.rsplit("/", 1)[0]
_spec = importlib.util.spec_from_file_location("refs_v2", _here + "/refs_v2.py")
_refs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_refs)
ACC = "[cited 2026 Oct 17]"
R = dict(_refs.R)

# --- fixes to earlier entries ---
R.update({
# R2 (ref. 68) and R4 minor 21: DOI added; Crossref 17 Oct 2026 (PLOS One 20(11):e0337199, 18 Nov 2025).
"Pruller2025": "Pruller J, Mockridge J, Vousden G. Expectations for Mendelian randomization research in PLOS One. PLoS One. 2025;20(11):e0337199. doi:10.1371/journal.pone.0337199",
"arXiv2026": "Boboris K. Fair moderation, equitable access, and AI: arXiv's updated rate limit policy [Internet]. arXiv blog; 1 Oct 2026 " + ACC + ". Available from: https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/",
})

# --- A1: form as an unreliable cue of quality (author critique A1, follow-up of 17 Oct 2026) ---
R.update({
# Crossref: Social Text, issue 46/47, first page 217, 1996; last page 252 from the author's own list of the article
# (mirror of A. Sokal's home page, read 17 Oct 2026).
"Sokal1996": "Sokal AD. Transgressing the boundaries: toward a transformative hermeneutics of quantum gravity. Soc Text. 1996;(46/47):217–252. doi:10.2307/466856",
# Crossref: Science 342(6154):60–65, 4 Oct 2013. The full text returned HTTP 403; the numbers quoted in the article
# (sent to 304 open-access journals, accepted by 157) were read in two secondary reports (Phys.org, 4 Oct 2013;
# Columbia Journalism Review, 14 Nov 2013), which agree on both. The number of rejections differs between them (98
# against 97) and is not quoted.
"Bohannon2013": "Bohannon J. Who's afraid of peer review? Science. 2013;342(6154):60–65. doi:10.1126/science.342.6154.60",
# Crossref: Scientometrics 94(1):379–396, online 22 Jun 2012, issue Jan 2013.
"LabbeLabbe2013": "Labbé C, Labbé D. Duplicate and fake publications in the scientific literature: how many SCIgen papers in computer science? Scientometrics. 2013;94(1):379–396. doi:10.1007/s11192-012-0781-y",
# Crossref: Nature news, 24 Feb 2014. Content (Springer and IEEE; more than 120 papers; more than 30 conference
# proceedings, 2008–2013; found by C. Labbé) read in reprints of the story and Retraction Watch's report, 17 Oct 2026.
"VanNoorden2014": "Van Noorden R. Publishers withdraw more than 120 gibberish papers. Nature. 2014 Feb 24. doi:10.1038/nature.2014.14763",
})

# --- data sources (R4 minor 3) ---
R.update({
# NCBI Books database (esummary for NBK25497), 17 Oct 2026: chapter dated 26 May 2009, updated 17 Nov 2022.
"NCBIEutils": "Sayers E. A general introduction to the E-utilities. 2009 May 26 [updated 2022 Nov 17]. In: Entrez Programming Utilities Help [Internet]. Bethesda (MD): National Center for Biotechnology Information (US); 2010– " + ACC + ". Available from: https://www.ncbi.nlm.nih.gov/books/NBK25497/",
})

# --- reporting of deviations and misclassification (R1 N6.4; R4 N1) ---
R.update({
# Crossref, 17 Oct 2026.
"Willroth2024": "Willroth EC, Atherton OE. Best laid plans: a guide to reporting preregistration deviations. Adv Methods Pract Psychol Sci. 2024;7(1):25152459231213802. doi:10.1177/25152459231213802",
"Lakens2024": "Lakens D. When and how to deviate from a preregistration. Collabra Psychol. 2024;10(1):117094. doi:10.1525/collabra.117094",
"RoganGladen1978": "Rogan WJ, Gladen B. Estimating prevalence from the results of a screening test. Am J Epidemiol. 1978;107(1):71–76. doi:10.1093/oxfordjournals.aje.a112510",
})

# --- S2 Appendix timeline (R2 N7 and minor 9) ---
R.update({
# Crossref, 17 Oct 2026: Nature news, 11 Mar 2025.
"Naddaf2025": "Naddaf M. Preprint sites bioRxiv and medRxiv launch new era of independence. Nature. 2025 Mar 11. doi:10.1038/d41586-025-00762-4",
})

# --- A3: prior attempts at open, post-publication evaluation ---
# The verified file paper/sources/open_publishing_attempts.md did not exist when v3 was built (17 Oct 2026); the
# Discussion carries [A3 REFS PENDING] markers. Add the verified entries here when the file is ready.
