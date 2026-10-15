import re, sys, os, csv, collections
src, out = sys.argv[1], sys.argv[2]
MON = {m: i for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), 1)}
pat = re.compile(r'(\d+)\s*\+\s*(\d+)\s*\((\w{3}) (\d{4})\)')
rows = []
for fn in sorted(os.listdir(src)):
    if not fn.endswith('.html'): continue
    archive, year = fn[:-5].rsplit('_', 1)
    txt = re.sub(r'<[^>]+>', ' ', open(os.path.join(src, fn), encoding='utf-8', errors='replace').read())
    for new, cross, mon, yr in pat.findall(txt):
        if yr != year: continue
        rows.append((archive, int(yr), MON[mon], int(new), int(cross)))
with open(out, 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['archive', 'year', 'month', 'new', 'cross']); w.writerows(sorted(rows))
# validation against official monthly totals
tot = collections.Counter()
for a, y, m, n, c in rows: tot[(y, m)] += n
off = {}
for r in csv.DictReader(open(os.path.join(src, 'monthly_submissions.csv'))):
    y, m = map(int, r['month'].split('-')[:2]); off[(y, m)] = int(r['submissions'])
print('archives:', len({r[0] for r in rows}), 'rows:', len(rows))
bad = 0
for k in sorted(tot):
    d = tot[k] - off.get(k, -1)
    if abs(d) > 0: bad += 1
    if k[1] in (1, 6, 9) or abs(d) > 50: print(k, 'sum_archives=', tot[k], 'official=', off.get(k), 'diff=', d)
print('months with any diff:', bad, 'of', len(tot))
