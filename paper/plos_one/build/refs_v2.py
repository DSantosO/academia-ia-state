# Reference database for paper/plos_one/draft_v2.md (Vancouver / PLOS style).
# Starts from refs.py (v1) and applies the round-1 fixes (R4 minor 34; R2 minor 13) and the additions requested by
# R1, R2 and R4. Metadata of every added journal article were read from Crossref on 16 Oct 2026 (identifiers named by
# the reviewers); arXiv entries from the arXiv abstract pages on 16 Oct 2026. Holm 1979 is not registered in Crossref;
# its entry follows Reviewer 1's reference list.
import importlib.util

_here = __file__.rsplit("/", 1)[0]
_spec = importlib.util.spec_from_file_location("refs", _here + "/refs.py")
_refs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_refs)
ACC = _refs.ACC
R = dict(_refs.R)

# --- fixes to v1 entries ---
R.update({
"Blekhman2026": "Blekhman R. What is biology research for? PLoS Biol. 2026;24(10):e3004075. doi:10.1371/journal.pbio.3004075",
"Kusumegi2025": "Kusumegi K, Yang X, Ginsparg P, de Vaan M, Stuart T, Yin Y. Scientific production in the era of large language models. Science. 2025;390(6779):1240–1243. doi:10.1126/science.adw3000",
"Hao2026": "Hao Q, Xu F, Li Y, Evans JA. Artificial intelligence tools expand scientists' impact but contract science's focus. Nature. 2026;649:1237–1243. doi:10.1038/s41586-025-09922-y",
"Rice2020": "Rice DB, Raffoul H, Ioannidis JPA, Moher D. Academic criteria for promotion and tenure in biomedical sciences faculties: cross sectional analysis of international sample of universities. BMJ. 2020;369:m2081. doi:10.1136/bmj.m2081",
"Nee2026": "Nee X, Zhong H, Ni X. The generative AI gold rush in theoretical and computational research [Preprint]. arXiv:2609.04872v1 [cs.DL]. 2026 " + ACC + ". Available from: https://arxiv.org/abs/2609.04872",
"Gorelick2026": "Gorelick DA, Clark A. Expanded implementation of Fast & Fair paid peer review reduces time to first decision without reducing review quality in a biology journal [Preprint]. bioRxiv. 2026. doi:10.64898/2026.06.02.729548",
"SinghChawla2026a": "Singh Chawla D. Inundated AI conferences impose submissions caps. Nature. 2026 Oct 13. doi:10.1038/d41586-026-03153-5",
"ACL2026": "Association for Computational Linguistics. ACL sustainable reviewing policy [Internet]. 11 Sep 2026 " + ACC + ". Available from: https://aclrollingreview.org/sustainable-reviewing-2026",
"NeweyWest1987": "Newey WK, West KD. A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. Econometrica. 1987;55(3):703–708. doi:10.2307/1913610",
})

# --- data sources, platform documentation ---
R.update({
"arXivStats": "arXiv. Yearly submission statistics, one page per archive and year (for example, hep-th in 2025) [Internet] " + ACC + ". Available from: https://arxiv.org/year/hep-th/2025",
"arXivAPITerms": "arXiv. Terms of use for arXiv APIs [Internet] " + ACC + ". Available from: https://info.arxiv.org/help/api/tou.html",
"arXivRobots": "arXiv. robots.txt [Internet] " + ACC + ". Available from: https://arxiv.org/robots.txt",
"arXivAvailability": "arXiv. Availability of submissions [Internet] " + ACC + ". Available from: https://info.arxiv.org/help/availability.html",
"arXivTaxonomy": "arXiv. Category taxonomy [Internet] " + ACC + ". Available from: https://arxiv.org/category_taxonomy",
"bioRxivAPI": "bioRxiv, medRxiv. bioRxiv and medRxiv API [Internet] " + ACC + ". Available from: https://api.biorxiv.org/",
"bioRxivFAQ": "bioRxiv. Frequently asked questions [Internet]. Cold Spring Harbor Laboratory " + ACC + ". Available from: https://www.biorxiv.org/about/FAQ",
"medRxivAbout": "medRxiv. About medRxiv [Internet] " + ACC + ". Available from: https://www.medrxiv.org/content/about-medrxiv",
"INSPIREAPI": "INSPIRE-HEP. REST API documentation [Internet] " + ACC + ". Available from: https://github.com/inspirehep/rest-api-doc",
"OSFTerms": "Center for Open Science. Terms of use [Internet] " + ACC + ". Available from: https://github.com/CenterForOpenScience/cos.io/blob/master/TERMS_OF_USE.md",
"Pruller2025": "Pruller J, Mockridge J, Vousden G. Expectations for Mendelian randomization research in PLOS One. PLoS One. 2025;20(11):e0337199.",
})

# --- scientometrics and preprints (R2, M9; identifiers verified by R2; metadata from Crossref/arXiv) ---
R.update({
"Abdill2019": "Abdill RJ, Blekhman R. Tracking the popularity and outcomes of all bioRxiv preprints. eLife. 2019;8:e45133. doi:10.7554/eLife.45133",
"Sever2019": "Sever R, Hindle S, Roeder T, Fereres S, Fernández Gayol O, Ghosh S, et al. bioRxiv: the preprint server for biology [Preprint]. bioRxiv. 2019. doi:10.1101/833400",
"Krumholz2020": "Krumholz HM, Bloom T, Sever R, Rawlinson C, Inglis JR, Ross JS. Submissions and downloads of preprints in the first year of medRxiv. JAMA. 2020;324(18):1903–1905. doi:10.1001/jama.2020.17529",
"Fraser2021": "Fraser N, Brierley L, Dey G, Polka JK, Pálfy M, Nanni F, et al. The evolving role of preprints in the dissemination of COVID-19 research and their impact on the science communication landscape. PLoS Biol. 2021;19(4):e3000959. doi:10.1371/journal.pbio.3000959",
"Lariviere2014": "Larivière V, Sugimoto CR, Macaluso B, Milojević S, Cronin B, Thelwall M. arXiv e-prints and the journal of record: an analysis of roles and relationships. J Assoc Inf Sci Technol. 2014;65(6):1157–1169. doi:10.1002/asi.23044",
"WangChenGlanzel2020": "Wang Z, Chen Y, Glänzel W. Preprints as accelerator of scholarly communication: an empirical analysis in mathematics. J Informetr. 2020;14(4):101097. doi:10.1016/j.joi.2020.101097",
"Ioannidis2018": "Ioannidis JPA, Klavans R, Boyack KW. Thousands of scientists publish a paper every five days. Nature. 2018;561(7722):167–169. doi:10.1038/d41586-018-06185-8",
"Ioannidis2024": "Ioannidis JPA, Collins TA, Baas J. Evolving patterns of extreme publishing behavior across science. Scientometrics. 2024;129(9):5783–5796. doi:10.1007/s11192-024-05117-w",
"Milojevic2013": "Milojević S. Accuracy of simple, initials-based methods for author name disambiguation. J Informetr. 2013;7(4):767–773. doi:10.1016/j.joi.2013.06.006",
"KimDiesner2016": "Kim J, Diesner J. Distortive effects of initial-based name disambiguation on measurements of large-scale coauthorship networks. J Assoc Inf Sci Technol. 2016;67(6):1446–1461. doi:10.1002/asi.23489",
"Bornmann2021": "Bornmann L, Haunschild R, Mutz R. Growth rates of modern science: a latent piecewise growth curve approach to model publication numbers from established and new literature databases. Humanit Soc Sci Commun. 2021;8:224. doi:10.1057/s41599-021-00903-w",
"Filimonovic2025": "Filimonovic D, Rutzer C, Wunsch C. Can GenAI improve academic performance? Evidence from the social and behavioral sciences [Preprint]. arXiv:2510.02408. 2025 " + ACC + ". Available from: https://arxiv.org/abs/2510.02408",
})

# --- statistical methods (R1, R4) ---
R.update({
"SantosSilva2006": "Santos Silva JMC, Tenreyro S. The log of gravity. Rev Econ Stat. 2006;88(4):641–658. doi:10.1162/rest.88.4.641",
"DriscollKraay1998": "Driscoll JC, Kraay AC. Consistent covariance matrix estimation with spatially dependent panel data. Rev Econ Stat. 1998;80(4):549–560. doi:10.1162/003465398557825",
"Holm1979": "Holm S. A simple sequentially rejective multiple test procedure. Scand J Stat. 1979;6(2):65–70.",
"Andrews1993": "Andrews DWK. Tests for parameter instability and structural change with unknown change point. Econometrica. 1993;61(4):821–856. doi:10.2307/2951764",
"Abadie2010": "Abadie A, Diamond A, Hainmueller J. Synthetic control methods for comparative case studies: estimating the effect of California's tobacco control program. J Am Stat Assoc. 2010;105(490):493–505. doi:10.1198/jasa.2009.ap08746",
"Bertrand2004": "Bertrand M, Duflo E, Mullainathan S. How much should we trust differences-in-differences estimates? Q J Econ. 2004;119(1):249–275. doi:10.1162/003355304772839588",
"ConleyTaber2011": "Conley TG, Taber CR. Inference with \"difference in differences\" with a small number of policy changes. Rev Econ Stat. 2011;93(1):113–125. doi:10.1162/rest_a_00049",
"GelmanStern2006": "Gelman A, Stern H. The difference between \"significant\" and \"not significant\" is not itself statistically significant. Am Stat. 2006;60(4):328–331. doi:10.1198/000313006X152649",
"Lakens2017": "Lakens D. Equivalence tests: a practical primer for t tests, correlations, and meta-analyses. Soc Psychol Personal Sci. 2017;8(4):355–362. doi:10.1177/1948550617697177",
})
