# Instruction given to each classifier run (one sub-agent per batch)

The classifier is a large language model run as a Claude Code sub-agent, one per batch of papers. Every run receives
this instruction, with the two paths filled in. The registered prompt for the domain travels inside the batch file,
verbatim (see `scripts/classifier_batches.py`).

> You are the classifier in a pre-registered study. Read the JSON file at BATCH_PATH. It contains "prompt" (the
> classification instructions) and "papers" (each with an id, a title, an abstract and, for arXiv papers, comments).
> For EACH paper independently, apply the classification instructions exactly as written, using only that paper's
> title, abstract and comments. Do not use any other information: no web access, no other tools except reading that
> file and writing the output, and no knowledge you may have about the specific paper. Write the results to
> LABELS_PATH as CSV with the header `id,label` and one row per paper, in input order; each label must be exactly ND,
> NN or U. Then reply only with `done` followed by the number of rows written.
