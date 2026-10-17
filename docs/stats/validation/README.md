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
