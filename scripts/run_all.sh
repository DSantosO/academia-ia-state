#!/usr/bin/env bash
# Reproduce every processed dataset, estimate and figure of the PLOS ONE analysis from the data in data/raw.
#   scripts/run_all.sh            processed series, statistics, results.md and figures (a few minutes)
#   scripts/run_all.sh OAI_DIR    the same, plus the author-level (H2) statistics and the OAI-based review analyses, from the
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

if [ -n "$OAI" ]; then
  physics=""
  for a in hep-th hep-ph gr-qc nucl-th hep-ex nucl-ex; do physics="$physics,$OAI/oai_physics_$a.jsonl.gz"; done
  python3 scripts/stats_heavy_producers.py data/processed/stats/heavy_producers.json \
    maths="$OAI/oai_math_math.jsonl.gz" physics="${physics#,}"
  python3 scripts/stats_round1.py . --oai "$OAI"   # all review sections, including the OAI-based ones
  python3 scripts/stats_h2_round2.py "$OAI"         # H2: independent-window classes, uniform-scaling simulation
  STATS_LAST=2026-08 python3 scripts/stats_round1.py . estimands planned calibration placebos_matched oai breaks --oai "$OAI"
else
  python3 scripts/stats_round1.py .                # review sections that need no OAI harvest
  STATS_LAST=2026-08 python3 scripts/stats_round1.py . estimands planned calibration placebos_matched breaks
fi
# January-August 2026 versions of the 2026 estimates (files *_to_2026-08.json), read by report_stats.py
STATS_LAST=2026-08 python3 scripts/stats_within_field.py .
STATS_LAST=2026-08 python3 scripts/stats_fields.py .

python3 scripts/report_stats.py .
python3 scripts/plot_plos.py .
