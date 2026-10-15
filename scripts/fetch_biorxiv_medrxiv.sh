#!/usr/bin/env bash
# Download the official monthly content summaries of bioRxiv and medRxiv
# (new papers and revised papers per month).
# Usage: scripts/fetch_biorxiv_medrxiv.sh <out_dir>
set -euo pipefail
OUT="${1:-data/raw}"; mkdir -p "$OUT"
UA="academia-ia-state research"
curl -sS --fail --max-time 60 -A "$UA" -o "$OUT/biorxiv_sum_m.json" "https://api.biorxiv.org/sum/m"
curl -sS --fail --max-time 60 -A "$UA" -o "$OUT/medrxiv_sum_m.json" "https://api.medrxiv.org/sum/m"
