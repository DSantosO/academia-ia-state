# medRxiv flag check (round-1 item P3)

`medrxiv_flag_coding_sheet.csv` holds random samples of 50 medRxiv preprints for each flag rule, drawn with a fixed seed
by `scripts/sample_flags.py`:

| Flag | Rule |
|---|---|
| `covid_title` | the COVID-19 pattern matches the title |
| `covid_abstract_only` | the pattern matches the abstract but not the title |
| `public_dataset` | one of the original public datasets or designs is named in the title or abstract |
| `public_spick4` | one of FinnGen, CHARLS, CDC WONDER or TriNetX is named, and none of the original list |

`pool_size` is the number of preprints the rule flags.

The sheet holds DOIs and DOI links only, no titles or abstracts. **How to code.** Open each preprint (`link`). Enter 1 in `true_positive` if the flag is right, otherwise 0:
- for COVID-19 flags, the preprint studies COVID-19;
- for dataset flags, it analyses data from the named source.

A passing mention does not count. Precision per rule is the mean of `true_positive`.

`coder` and `note` are free text.

# Country classifier spot check (round-2 item 10)

`country_spot_check_sheet.csv` holds 100 version-1 preprints of 2025–2026, drawn with a fixed seed by
`scripts/sample_country_check.py`: per server (bioRxiv, medRxiv), 20 that `scripts/classify_country.py` assigned to the
US, 20 assigned elsewhere (`non-US`) and 10 with no country (`unknown`). The classifier reads the corresponding author's
institution string from the bioRxiv/medRxiv API; so far it was checked by an AI agent only.

The sheet holds DOIs and DOI links only. **How to code.** Open each preprint (`link`), find the corresponding author's
institution and enter `US`, `non-US` or `unclear` in `true_country`. Precision per class is the share of rows whose
`true_country` equals `assigned`; for `unknown` rows, record the true country to estimate what the missing group holds.
`coder` and `note` are free text.
