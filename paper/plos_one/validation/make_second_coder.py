"""Build the second coder's offline sheet from the author's coding page.
Usage: python3 -I make_second_coder.py IDS_FILE OUT_HTML OUT_MAP_CSV
IDS_FILE: the 100 V-ids drawn by the analysis session (one per line). Order seed: 20261018."""
import json, random, re, sys
SRC = "/tmp/claude-0/-home-user-academia-ia-state/58b1bbe3-08b6-5a3d-b8a3-b20c3e7b34cf/scratchpad/coding/"
ids_file, out_html, out_map = sys.argv[1:4]
vids = [l.strip() for l in open(ids_file) if l.strip()]
assert len(vids) == 100 and len(set(vids)) == 100, len(vids)
sheet = {r["id"]: r for r in json.load(open(SRC + "sheet.json"))}
assert all(v in sheet for v in vids)
order = sorted(vids)
random.Random(20261018).shuffle(order)
items, mapping = [], []
for i, v in enumerate(order, 1):
    sid = "S%03d" % i
    r = sheet[v]
    items.append({"id": sid, "title": r["title"], "abstract": r["abstract"], "comments": r.get("comments"), "label": None, "note": None})
    mapping.append((sid, v))
html = open(SRC + "ndnn_coding_sheet.html", encoding="utf-8").read()
data = json.dumps(items, ensure_ascii=False).replace("</", "<\\/")
html, n = re.subn(r'(<script type="application/json" id="sheet">).*?(</script>)', lambda m: m.group(1) + data + m.group(2), html, count=1, flags=re.S)
assert n == 1
R = [
 ("<title>ND/NN Coding Sheet</title>", "<title>Second Coder Sheet</title>"),
 ('<span class="vid" id="vid">V001</span><span class="of">of 400</span>', '<span class="vid" id="vid">S001</span><span class="of">of 100</span>'),
 ('<span id="count">0 of 400 coded</span>', '<span id="count">0 of 100 coded</span>'),
 ("Labels are being kept in this browser only. Open this page from claude.ai or the Claude app to save them to your account; what you code here is added the next time it opens there.",
  "Your codes are kept in this browser only, so use the same browser on the same computer until you finish. When you are done, open Map and press Save CSV, then send the file to the author."),
 ("Note on V001", "Note on S001"),
 ("All 400 papers", "All 100 papers"),
 ('Not coded <b id="n-0">400</b>', 'Not coded <b id="n-0">100</b>'),
 ("Rows run V001 to V010, V011 to V020, and so on.", "Rows run S001 to S010, S011 to S020, and so on."),
 ("Your codes save to this page's private store as you go, so there is nothing to submit. When you finish, tell Claude in the chat; it reads them from the store and commits them before anyone unseals the classifier's labels. The CSV is a backup.",
  "Your codes are saved in this browser as you go. When you finish, press Save CSV and send the file to the author by email; keep a copy until the author confirms receipt. If Save CSV does not download a file, use Copy CSV and paste the text into the email."),
 ("<li>Until your codes are committed, do not open <code>validation/sealed/</code>, the analysis branch's commit list or its results files.</li>",
  "<li>Code on your own. Please do not discuss these papers, your codes or the study with the author until you have sent your file and the author has confirmed that their own codes are recorded.</li>"),
 ("<li>Afterwards your codes are compared with the classifier's: Cohen's κ for each domain, with κ ≥ 0.60 as the registered threshold.</li>",
  "<li>Your codes will be compared with other codes of the same papers to measure agreement. There are no right proportions to aim for: code each paper on its own merits.</li>"),
 ("var KEY = { labels: 'ndnn.labels.v1', pending: 'ndnn.pending.v1', idx: 'ndnn.idx.v1' };",
  "var KEY = { labels: 'ndnn2.labels.v1', pending: 'ndnn2.pending.v1', idx: 'ndnn2.idx.v1' };"),
 ("filename: 'author_labels.csv'", "filename: 'second_coder_labels.csv'"),
 ("    if (!use) { showCsv(); return; }", "    if (!use) { downloadCsv(); return; }"),
 ("      if (!dl) { showCsv(); return; }", "      if (!dl) { downloadCsv(); return; }"),
 ("  $('save-csv').addEventListener('click', function () {",
  "  function downloadCsv() {\n    try {\n      var blob = new Blob([buildCsv()], { type: 'text/csv;charset=utf-8' });\n      var a = document.createElement('a');\n      a.href = URL.createObjectURL(blob);\n      a.download = 'second_coder_labels.csv';\n      document.body.appendChild(a);\n      a.click();\n      setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 1500);\n      toast('CSV saved');\n    } catch (e) { showCsv(); }\n  }\n  $('save-csv').addEventListener('click', function () {"),
]
for a, b in R:
    c = html.count(a)
    assert c == 1, (c, a[:60])
    html = html.replace(a, b)
assert "V001" not in html.split('id="sheet">')[0] and "of 400" not in html
open(out_html, "w", encoding="utf-8").write(html)
with open(out_map, "w") as f:
    f.write("second_coder_id,validation_id\n")
    for s, v in mapping:
        f.write("%s,%s\n" % (s, v))
print("ok", len(items), "items;", out_html, len(html), "bytes")
