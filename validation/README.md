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
- *Temperature.* Sub-agents do not expose a temperature setting, so the registered "temperature 0" could not be
  applied. This is a deviation.

## Sealed files

| File | SHA-256 |
|---|---|
| `sealed/key.csv.gz` | (added when the file is committed) |
| `sealed/model_labels.csv.gz` | (added when the file is committed) |
