# Page through one provider/quarter and count first versions vs all records.
import json, sys, time, urllib.request
UA = 'academia-ia-state research'
PAUSE = 36  # OSF API: 100 unauthenticated requests per hour (osfr documentation); one request every 36 s
prov, s, e = sys.argv[1:4]
url = (f"https://api.osf.io/v2/preprints/?filter%5Bprovider%5D={prov}&filter%5Bdate_created%5D%5Bgte%5D={s}"
       f"&filter%5Bdate_created%5D%5Blt%5D={e}&page%5Bsize%5D=100&fields%5Bpreprints%5D=date_created")
ids = []
while url:
    for t in range(5):
        try:
            j = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=120)); break
        except Exception as ex:
            time.sleep(3 * (t + 1))
    ids += [d['id'] for d in j['data']]; url = j['links'].get('next'); time.sleep(PAUSE)
v1 = sum(1 for i in ids if i.endswith('_v1') or '_v' not in i)
print(prov, s, e, 'records', len(ids), 'first_versions', v1, 'suffix_v1', sum(i.endswith('_v1') for i in ids), 'no_suffix', sum('_v' not in i for i in ids))
