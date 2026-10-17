# Blind validation sheet for the new-data (ND/NN) classifier

For the active pre-registration (`paper/plos_one/preregistration_new_data_test.md`) and its Amendment 1, on the essay
branch. The author codes the sheet blind; the model's labels are compared with the author's afterwards (Cohen's κ,
precision and recall per class, by domain).

## For the coder

- **File to code:** `sheet.csv` (the same rows are in `sheet.json`). 400 papers, rows in random order.
- **Fill in:** `label` = **ND**, **NN** or **U** for each row; `note` is optional.
- **Classes:** use the codebooks of the pre-registration (Appendix A, physics and astronomy) and of Amendment 1
  (Appendix B, biology and medicine). In short:
  - **ND** — the paper reports new empirical data obtained by the authors;
  - **NN** — it does not (theory, simulation, methods, reviews, reanalysis of existing or public data, prospects);
  - **U** — cannot tell.
- **What the sheet hides:** dates, servers, archives and model labels. Comments appear only for arXiv papers.
- **Do not open `sealed/`** until the coding is finished. It holds the key (paper identifiers, dates, servers) and
  the model's labels. The repository is public, so blinding depends on the coder not opening these files. Their
  SHA-256 hashes below fix their content at the time of commit.

## How the sample was drawn

`scripts/make_validation_sheet.py` (fixed seeds):

| Domain | Papers | Sampling frame | Dating |
|---|---|---|---|
| arXiv | 200 | cond-mat 34 + 34, astro-ph 33 + 33, quant-ph 33 + 33 (2019–2022 + 2023-01 to 2026-09); primary category in the archive; a simple random sample of each stratum from the complete arXivRaw harvest of the archive (the sampling frame of the new-data test) | First-version submission |
| bioRxiv | 100 | 50 + 50 by period; a random day, a random page of that day's records, a random version-1 record | Version-1 posting |
| medRxiv | 100 | 50 + 50 by period; same procedure; COVID-19 preprints (title or abstract) rejected | Version-1 posting |

- bioRxiv and medRxiv draws are limited to preprints under Creative Commons licences, because the sheet republishes
  abstracts in a public repository. arXiv metadata are CC0.
- For bioRxiv and medRxiv, sampling by random day gives every day, not every paper, the same chance, so papers on
  busy days are slightly under-represented. This does not matter for estimating agreement.
- For arXiv, the planned draw by random submission day used the arXiv API, which answered "429 Rate exceeded" from
  this environment. The arXiv half is therefore a simple random sample per stratum from the complete OAI-PMH
  (arXivRaw) harvests, which gives every paper the same chance.

## Classifier

- *Model.* A large language model run as Claude Code sub-agents. The model and version are reported in the manuscript.
  Repository files do not name model versions.
- *Prompts.* The verbatim prompts are in `scripts/classifier_batches.py`. They are checked character by character
  against the registered text.
- *Procedure.* Batches of 50 papers per run, each paper judged on its own, with the label only returned. The
  classifier sees the sheet's pseudonymous ids and the sheet's random order, never DOIs or arXiv identifiers, which
  encode the posting month. The confirmatory samples are classified the same way (`classifier_batches.py split
  --blind`), so the agreement measured here applies to them.
- *Earlier run.* The 200 bioRxiv and medRxiv papers were first classified in batches keyed by DOI. Those labels are
  not used for the sheet; they serve only as a test–retest check of the classifier.
- *Second run (arXiv).* The 200 arXiv papers were classified a second time, blind, with a new random order and new
  pseudonymous ids (4 batches, same prompt). Those labels are not used for the sheet either; they give the arXiv
  test–retest table. The per-server tables (first run by second run) feed the relabelling of Deviation 3 (D3g).
- *Temperature.* Sub-agents do not expose a temperature setting, so the registered "temperature 0" could not be
  applied. This is a deviation.

## Sealed files

| File | SHA-256 |
|---|---|
| `sealed/key.csv.gz` | `0d724ec919547cf000cffd9f03999b70bebb144fc2ace6c066373c41120d15f4` |
| `sealed/model_labels.csv.gz` | `1b8260e5982ca4914f3a00f347a08cf78a6ec9a1e781f194853216d653bca955` |
| `sealed/nd_model_labels_medrxiv.csv.gz` | `6b59301db05da6c36dc4081e520641fa6dd661a421b428b90f5746cd4da165f0` |
| `sealed/classifier_retest_validation.json.gz` | `d7743b8d22c739738fa13d050425d9b84814a29cc27b47e55cafb0c5478388bb` |
| `sealed/classifier_retest_validation_biorxiv.json.gz` | `21fc6d368081c5789c358d0a409d809b4b638cfaf665d6c51506e366d120fcae` |
| `sealed/classifier_retest_validation_medrxiv.json.gz` | `acef560215c611b3303b95741f4a89c52816cd869a8774f891c63a470186c75c` |
| `sealed/model_labels_retest_arxiv.csv.gz` | `ba90122763bb55ceaa6aaca007cf527433fd8d58d624d582e1ac091bd509d1de` |
| `sealed/classifier_retest_validation_arxiv.json.gz` | `9d31b35cb8d6fa2ad60cc7115b3723023cad4c4907a19fdc3ec6ca83cecea43a` |
| `sealed/nd_model_labels_arxiv_batches001-243.csv.gz` | `5377cff70f1b80104226b51c7b2716439bd7b0eed28486a8483fc9d52bb177ec` |

The model labels of the confirmatory samples (`nd_model_labels_*.csv.gz`, one row per sampled paper) are sealed here
too, because a few papers on the sheet may also be in those samples. `nd_model_labels_arxiv_batches001-243.csv.gz`
holds the arXiv labels of the first 243 of 269 blind batches (12,150 papers), sealed when classification was paused;
the complete arXiv file will supersede it.
