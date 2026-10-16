"""Sampling design for the confirmatory ND/NN tests (pre-registration HN; Amendment 1 Tests A and B; Deviation 2).

Fixed and committed before any growth-by-class estimate is computed. Classifying every paper is not feasible
(about 770,000 papers), so monthly class counts are estimated as total x sampled class share.

HN (held-out arXiv)  cond-mat, astro-ph, quant-ph; papers whose primary category is in the archive, by month of
                     first-version submission (arXiv API submittedDate), January 2017 to September 2026.
                     Simple random sample without replacement per archive-month: 15 papers per month to December 2024,
                     40 per month from January 2025.
Test A (bioRxiv)     version-1 preprints by posting month, January 2019 to September 2026; 15 / 40 per month as above.
Test A (medRxiv)     version-1 preprints without COVID-19 (title or abstract), July 2019 to September 2026; 15 / 40.
Test B (exposure)    150 random papers per category from 2019-2022 (all of them if fewer).
                     Categories, by the data available here:
                       arXiv: primary subcategories of cond-mat and astro-ph, quant-ph, math subcategories, and the
                       archives hep-th, hep-ph, gr-qc, nucl-th, hep-ex and nucl-ex, each with at least 300 new papers a
                       year on average in 2019-2022 (Amendment 1 rule). Other archives (cs, physics.*, stat, eess, q-bio,
                       econ, q-fin) are excluded: their subcategory counts would need a
                       full-arXiv harvest. Dating: held-out subcategories by first-version submission (API);
                       maths subcategories by identifier month from the OAI harvest (2019 on, so their trend window
                       is 2019-2022); the six HEP/nuclear archives by announcement month from arXiv's statistics pages.
                       bioRxiv and medRxiv subject categories with at least 300 eligible preprints in 2019-2022 (medRxiv:
                       non-COVID). Smaller categories are dropped, not pooled, and listed.
Labels               U is excluded from the ND share (primary); in a sensitivity analysis U counts as NN.
Seeds                each stratum's sample uses random.Random(seed) with seed = first 8 bytes of
                     SHA-256("<design>|<stratum>|20261016"), so any stratum can be redrawn independently.
"""
import hashlib
import random

BASE_SEED = 20261016
HN_ARCHIVES = ["cond-mat", "astro-ph", "quant-ph"]
HN_FIRST, LAST = "2017-01", "2026-09"
BIO_FIRST, MED_FIRST = "2019-01", "2019-07"
N_BEFORE_2025, N_FROM_2025 = 15, 40
TESTB_N, TESTB_WINDOW, TESTB_MIN_PER_YEAR, TESTB_MIN_RXIV = 150, ("2019-01", "2022-12"), 300, 300
TESTB_ARXIV_ARCHIVES = ["hep-th", "hep-ph", "gr-qc", "nucl-th", "hep-ex", "nucl-ex"]  # no subcategories


def seed(design, stratum):
    return int.from_bytes(hashlib.sha256(f"{design}|{stratum}|{BASE_SEED}".encode()).digest()[:8], "big")


def per_month(month):
    return N_FROM_2025 if month >= "2025-01" else N_BEFORE_2025


def draw(design, stratum, ids, n):
    """Simple random sample of n identifiers (all of them if fewer), reproducible per stratum."""
    ids = sorted(set(ids))
    if len(ids) <= n:
        return ids
    return sorted(random.Random(seed(design, stratum)).sample(ids, n))
