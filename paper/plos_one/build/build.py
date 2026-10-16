"""Build the numbered PLOS ONE draft from the keyed source.

Usage: python3 build.py keyed.md out.md
- Citations are written [@Key] or [@Key1; @Key2]; numbers follow first appearance in the main text.
- <!--REFS:Table1--> in the main text assigns numbers to the keys of the Table 1 block at that point
  (Vancouver rule: references cited only in a table are numbered where the table is first cited).
- Keys first seen in legends or tables after the references get the next numbers in order of appearance.
- The S1 Appendix (after <!-- S1APPENDIX START -->) has its own numbering and list (<!--S1REFERENCES-->).
"""
import re
import sys
import importlib.util

here = __file__.rsplit("/", 1)[0]
spec = importlib.util.spec_from_file_location("refs", here + "/refs.py")
refs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(refs)
R = refs.R

CIT = re.compile(r"\[(@[A-Za-z0-9]+(?:;\s*@[A-Za-z0-9]+)*)\]")
TOKEN = re.compile(r"\[(@[A-Za-z0-9]+(?:;\s*@[A-Za-z0-9]+)*)\]|<!--REFS:Table1-->")


def keys_of(group):
    return [k.strip()[1:] for k in group.split(";")]


def compress(nums):
    nums = sorted(set(nums))
    out, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        if j - i >= 2:
            out.append(f"{nums[i]}–{nums[j]}")
        else:
            out.extend(str(n) for n in nums[i:j + 1])
        i = j + 1
    return "[" + ",".join(out) + "]"


def number(text_main, text_post, table1_keys):
    order = {}

    def add(k):
        if k not in R:
            raise SystemExit(f"missing reference key: {k}")
        if k not in order:
            order[k] = len(order) + 1

    for m in TOKEN.finditer(text_main):
        if m.group(0) == "<!--REFS:Table1-->":
            for k in table1_keys:
                add(k)
        else:
            for k in keys_of(m.group(1)):
                add(k)
    for m in CIT.finditer(text_post):
        for k in keys_of(m.group(1)):
            add(k)
    return order


def replace(text, order):
    return CIT.sub(lambda m: compress([order[k] for k in keys_of(m.group(1))]), text)


def reflist(order):
    return "\n".join(f"{n}. {R[k]}" for k, n in sorted(order.items(), key=lambda x: x[1]))


def strip_markers(s):
    # remove [AUTHOR: ...], [ANALYSIS PENDING...], [RECHECK...] including nested brackets
    out, i = [], 0
    while i < len(s):
        m = re.match(r"\[(AUTHOR|ANALYSIS PENDING|RECHECK)", s[i:])
        if m:
            depth = 0
            j = i
            while j < len(s):
                if s[j] == "[":
                    depth += 1
                elif s[j] == "]":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            i = j + 1
            continue
        out.append(s[i])
        i += 1
    return "".join(out)


def words(s, prose=True):
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    lines = [l for l in s.splitlines() if not l.lstrip().startswith("#")]
    s = "\n".join(lines)
    if prose:
        s = strip_markers(s)
        s = re.sub(r"\[[0-9,–]+\]", " ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    return sum(1 for t in s.split() if re.search(r"[A-Za-z0-9€$&]", t))


def section(text, start, end):
    a = text.index(start)
    b = text.index(end, a)
    return text[a:b]


def main(src, dst):
    text = open(src, encoding="utf-8").read()
    main_part, app = text.split("<!-- S1APPENDIX START -->", 1)
    body, post = main_part.split("## References", 1)
    post = "## References" + post
    t1 = section(post, "<!--TABLE1 START-->", "<!--TABLE1 END-->")
    t1_keys = []
    for m in CIT.finditer(t1):
        for k in keys_of(m.group(1)):
            if k not in t1_keys:
                t1_keys.append(k)
    order = number(body, post, t1_keys)
    body = replace(body, order).replace(" <!--REFS:Table1-->", "").replace("<!--REFS:Table1-->", "")
    post = replace(post, order).replace("<!--REFERENCES-->", reflist(order))
    post = post.replace("<!--TABLE1 START-->\n", "").replace("<!--TABLE1 END-->\n", "")
    # appendix: own numbering
    a_order = {}
    for m in CIT.finditer(app):
        for k in keys_of(m.group(1)):
            if k not in R:
                raise SystemExit(f"missing reference key (appendix): {k}")
            a_order.setdefault(k, len(a_order) + 1)
    app = replace(app, a_order).replace("<!--S1REFERENCES-->", reflist(a_order))
    out = body + post + "<!-- S1 Appendix: a separate Supporting Information file with its own reference list. -->" + app
    # word counts
    abstract = section(out, "## Abstract", "## Introduction")
    maintext = section(out, "## Introduction", "## Acknowledgments")
    sections = {}
    for name, a, b in [("Introduction", "## Introduction", "## Materials and methods"),
                       ("Materials and methods", "## Materials and methods", "## Results"),
                       ("Results", "## Results", "## Discussion"),
                       ("Discussion", "## Discussion", "## Conclusions"),
                       ("Conclusions", "## Conclusions", "## Acknowledgments")]:
        sec = section(out, a, b)
        sections[name] = (words(sec), words(sec, prose=False))
    s1 = out[out.index("## S1 Appendix. Process record"):out.index("### References for S1 Appendix")]
    legends = section(out, "## Figure legends", "## Tables")
    rows = "\n".join(f"| {k} | {v[0]:,} | {v[1]:,} |" for k, v in sections.items())
    report = (
        "WORD COUNTS (computed by script at build time; HTML comments and headings excluded).\n"
        "'Prose' also removes the editorial markers ([AUTHOR: ...], [ANALYSIS PENDING ...], [RECHECK ...]) and numbered "
        "citations; 'raw' keeps them.\n\n"
        "| Section | Prose | Raw |\n|---|---|---|\n" + rows +
        f"\n| **Main text (Introduction to Conclusions)** | **{words(maintext):,}** | **{words(maintext, prose=False):,}** |\n\n"
        f"Abstract: {words(abstract):,} words of prose ({words(abstract, prose=False):,} raw); PLOS ONE limit 300.\n"
        f"Figure legends: {words(legends):,}. S1 Appendix: {words(s1):,}.\n"
        f"References: {len(order)} in the main list; {len(a_order)} in the S1 Appendix list.\n"
        f"Reference keys in the database but not cited: {', '.join(sorted(set(R) - set(order) - set(a_order))) or 'none'}."
    )
    out = out.replace("WORD COUNT: [to be filled at the end of drafting]", report)
    out = out.replace("DRAFT v1 (keyed working copy; numbering of references is applied at the end of drafting).",
                      "DRAFT v1.")
    open(dst, "w", encoding="utf-8").write(out)
    print(report)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
