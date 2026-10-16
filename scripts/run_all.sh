#!/usr/bin/env bash
# Reproduce every processed dataset, estimate and figure of the PLOS ONE analysis from the data in data/raw.
#   scripts/run_all.sh            processed series, statistics, results.md and figures (a few minutes)
#   scripts/run_all.sh OAI_DIR    the same, plus the author-level (H2) and arXiv text (H3) inputs, rebuilt from the
#                                 arXiv OAI-PMH harvests in OAI_DIR (oai_math_math.jsonl.gz, oai_physics_hep-th.jsonl.gz,
#                                 ...). The harvests are not in the package because they hold author names; the
#                                 download commands are in deposit/README.md.
# Downloads of the raw data are listed in deposit/README.md; they take many hours because the servers ask for slow
# request rates.
set -euo pipefail
cd "$(dirname "$0")/.."
OAI="${1:-}"

python3 scripts/build_datasets.py data
python3 scripts/analyze_trends.py .
python3 scripts/analyze_within_field.py .
python3 scripts/stats_within_field.py .
python3 scripts/stats_fields.py .
python3 scripts/stats_markers.py .   # writes the core marker list from bioRxiv and medRxiv

if [ -n "$OAI" ]; then
  physics=""
  for a in hep-th hep-ph gr-qc nucl-th hep-ex nucl-ex; do physics="$physics,$OAI/oai_physics_$a.jsonl.gz"; done
  python3 scripts/stats_heavy_producers.py data/processed/stats/heavy_producers.json \
    maths="$OAI/oai_math_math.jsonl.gz" physics="${physics#,}"
  python3 scripts/aggregate_arxiv_text.py data/raw/arxiv_text "$OAI"/oai_*.jsonl.gz \
    --core data/processed/stats/core_marker_words.txt
  gzip -f data/raw/arxiv_text_words.csv
  python3 scripts/stats_markers.py .  # second run reads the arXiv counts built with the core list
fi

python3 scripts/report_stats.py .
python3 scripts/plot_plos.py .
