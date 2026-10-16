# Figure captions (PLOS ONE format)

Captions go in the manuscript, directly after the paragraph that first cites each figure. The figure files are
`docs/figures/plos/Fig1.tif` to `Fig4.tif` (PDF and SVG copies alongside).

**Fig 1. Preprints by field, indexed to 2022.**
Quarterly new preprints by field, each divided by its mean quarterly count in 2022 (2022 = 100), January 2020 to
September 2026. The number in each legend entry is the index in July–September 2026.
- Physics: new submissions to the 13 arXiv physics archives, by primary archive (astro-ph, cond-mat, gr-qc, hep-ex,
  hep-lat, hep-ph, hep-th, math-ph, nlin, nucl-ex, nucl-th, physics, quant-ph).
- Mathematics: arXiv math.
- Computer science: arXiv cs, shown for reference; it includes AI research itself.
- Biology: bioRxiv new preprints.
- Medicine: medRxiv new preprints, excluding those that mention COVID-19 or SARS-CoV-2 in the title or abstract.
- Social sciences: first versions on PsyArXiv, SocArXiv and EdArXiv plus arXiv econ and q-fin.

Dashed vertical lines mark, from left to right, the release of ChatGPT (30 November 2022), arXiv's rule on review
articles in computer science (31 October 2025), the release of Claude Opus 5 (24 July 2026) and arXiv's submission cap
(1 October 2026). They mark dates for reference; they are not estimated break points or causes.

**Fig 2. Within-field contrasts.**
(A–C) Quarterly new preprints, 2022 = 100, for groups within a field that differ in how much of the work is
experimental.
- (A) arXiv physics: theory (hep-th, hep-ph, gr-qc, nucl-th) and experiment (hep-ex, nucl-ex), by primary archive.
- (B) bioRxiv, version-1 preprints: computational (bioinformatics, systems biology, genomics), wet lab (twelve
  categories, see Methods) and all other categories.
- (C) medRxiv, excluding COVID-19: preprints whose title or abstract names a public dataset or design that recurs in
  formulaic papers (NHANES, UK Biobank, Global Burden of Disease, Mendelian randomisation, FAERS, MIMIC, SEER, BRFSS)
  and all other preprints.

(D) Rate ratio of group A to group B in each year relative to 2022 (theory / experiment, computational / wet lab,
public dataset / other), from a Poisson pseudo-maximum-likelihood model with month fixed effects and group-specific
calendar-month effects. Bars are 95% Driscoll–Kraay confidence intervals; logarithmic scale. 2026*: January–September.
Dashed vertical lines in A–C as in Fig 1.

**Fig 3. Concentration of output among authors in mathematics and theoretical physics.**
(A) Share of fractional output (each paper divided equally among its authors) produced by the top 1% of active authors
in each quarter. (B) Share of papers with at least one author who has five or more papers in the same field that
quarter (the measure of Nee, Zhong & Ni 2026).
- Solid lines: all author names. Dashed lines: namesake-robust (full first names only, with the 1% most frequent
  surnames removed).
- The dashed vertical line marks the release of ChatGPT.

(C, D) Growth in fractional output between the third quarters (July–September) of consecutive years, by author class.
Authors are ranked by their combined output in the two years compared: top 1%, next 9% and bottom 90%. Black bars:
all authors. Ranking on both years together avoids regression to the mean. If growth were proportional, every class
would grow at the black-bar rate. The grey background marks pairs that end before ChatGPT's release; they show how far
the classes diverge by chance.

Physics theory is hep-th, hep-ph, gr-qc and nucl-th (primary category), papers with at most 50 authors. Authors are
matched by name strings, because arXiv has no author identifiers.

**Fig 4. AI-associated style words by group.**
Core marker words per 100 abstracts, relative to each group's 2019–2022 mean. The core words are the 261 "style" words
of Kobak et al. (2025) that appeared in fewer than 0.5% of bioRxiv and medRxiv abstracts in 2019–2022.
- bioRxiv: version-1 preprints posted in March and September of each year.
- medRxiv: all version-1 preprints.
- arXiv: papers with primary category in maths, physics theory or physics experiment.
- bioRxiv and medRxiv exclude COVID-19 preprints.
- 2026*: January–September (bioRxiv: March and September).

The word list was built from 2024 text. Its fall after 2024 reflects, at least in part, changes in vocabulary: newer
models and authors avoiding words now read as signs of LLM text. Values after 2024 are therefore lower bounds on
LLM-assisted writing. The markers date changes in style; they do not identify causes.
