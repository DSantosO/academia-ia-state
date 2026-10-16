#!/usr/bin/env bash
# Fetch arXiv per-archive yearly statistics pages (monthly new articles + cross-lists).
# Usage: scripts/fetch_arxiv_years.sh <download_dir> [first_year, default 2019] [last_year, default current]   (the raw pages are not committed)
OUT="$1"; FIRST="${2:-2019}"; LAST="${3:-$(date -u +%Y)}"; mkdir -p "$OUT"
UA="academia-ia-state research"
ARCHIVES="astro-ph cond-mat gr-qc hep-ex hep-lat hep-ph hep-th math-ph nlin nucl-ex nucl-th physics quant-ph math cs econ eess q-bio q-fin stat"
for a in $ARCHIVES; do
  for y in $(seq "$FIRST" "$LAST"); do
    f="$OUT/${a}_${y}.html"
    [ -s "$f" ] && continue
    for t in 1 2 3; do
      code=$(curl -sS --max-time 40 -A "$UA" -o "$f" -w "%{http_code}" "https://arxiv.org/year/$a/$y")
      [ "$code" = "200" ] && break
      sleep $((t*3))
    done
    echo "$a $y $code"
    sleep 1
  done
done
curl -sS --max-time 40 -A "$UA" -o "$OUT/monthly_submissions.csv" "https://arxiv.org/stats/get_monthly_submissions"
