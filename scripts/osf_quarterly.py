# Quarterly NEW-paper counts for OSF social-science preprint servers.
# Before 2025 each preprint is one record, so the API total is the count.
# From early 2025 OSF lists every version as its own record (ids '<base>_vN'),
# so for those quarters we page through and count only '_v1' / unsuffixed ids.
import json, sys, time, urllib.request, csv, datetime
UA = 'academia-ia-state research'
PAUSE = 36  # OSF API: 100 unauthenticated requests per hour (osfr documentation); one request every 36 s
out = sys.argv[1]
PROVIDERS = sys.argv[2:] or ['socarxiv', 'psyarxiv', 'edarxiv']
quarters = []
for y in range(2019, datetime.date.today().year + 1):
    for q in range(4):
        s = datetime.date(y, 3*q+1, 1)
        e = datetime.date(y+1, 1, 1) if q == 3 else datetime.date(y, 3*q+4, 1)
        if s > datetime.date.today(): break
        quarters.append((f"{y}Q{q+1}", s, e))
def get(url):
    for t in range(5):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=120))
        except Exception as ex:
            err = ex; time.sleep(3 * (t + 1))
    raise err
base = "https://api.osf.io/v2/preprints/?filter%5Bprovider%5D={p}&filter%5Bdate_created%5D%5Bgte%5D={s}&filter%5Bdate_created%5D%5Blt%5D={e}"
with open(out, 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['provider', 'quarter', 'new_papers', 'records', 'method'])
    for p in PROVIDERS:
        for qn, s, e in quarters:
            u = base.format(p=p, s=s, e=e)
            if s < datetime.date(2025, 1, 1):
                tot = get(u + "&page%5Bsize%5D=1")['links']['meta']['total']
                w.writerow([p, qn, tot, tot, 'total']); f.flush(); time.sleep(PAUSE); continue
            url = u + "&page%5Bsize%5D=100&fields%5Bpreprints%5D=date_created"
            ids = []
            while url:
                j = get(url); ids += [d['id'] for d in j['data']]
                url = j['links'].get('next'); time.sleep(PAUSE)
            new = sum(1 for i in ids if i.endswith('_v1') or '_v' not in i)
            w.writerow([p, qn, new, len(ids), 'paged_v1']); f.flush()
print('done')
