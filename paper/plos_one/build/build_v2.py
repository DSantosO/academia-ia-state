"""Build the numbered PLOS ONE draft v2 from its keyed source.

Usage: python3 build_v2.py draft_v2_keyed.md ../draft_v2.md

- Citations are written [@Key] or [@Key1; @Key2]. In the manuscript part (everything before
  '<!-- SI FILES START -->') they are numbered by first appearance in reading order. Figure legends and tables sit
  right after the paragraph that first cites them (PLOS ONE), so reading order is citation order.
- <!--REFERENCES--> is replaced by the main reference list.
- After '<!-- SI FILES START -->', each Supporting Information file begins with '<!-- SI FILE: name -->' and has its
  own numbering, listed at '<!--SIREFS-->'.
- Figure legends are wrapped in <!--LEGEND--> ... <!--/LEGEND--> and tables in <!--TABLE--> ... <!--/TABLE-->. The
  wrappers are removed from the output; they only let the word count leave legends and tables out of the main text.
- Checks: figures and tables are first cited in numerical order, each legend or table follows the paragraph that
  first cites it, every key exists, and no model identifier appears.
"""
import re
import sys
import importlib.util

here = __file__.rsplit("/", 1)[0]
spec = importlib.util.spec_from_file_location("refs_v2", here + "/refs_v2.py")
refs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(refs)
R = refs.R

CIT = re.compile(r"\[(@[A-Za-z0-9]+(?:;\s*@[A-Za-z0-9]+)*)\]")
BLOCK = re.compile(r"<!--(LEGEND|TABLE)-->(.*?)<!--/\1-->", re.S)
BANNED = re.compile(r"\b(Opus|Sonnet|Haiku)\b|Claude\s+\d|claude-\d|claude-(opus|sonnet|haiku)", re.I)


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


def number(text):
    order = {}
    for m in CIT.finditer(text):
        for k in keys_of(m.group(1)):
            if k not in R:
                raise SystemExit(f"missing reference key: {k}")
            order.setdefault(k, len(order) + 1)
    return order


def replace(text, order):
    return CIT.sub(lambda m: compress([order[k] for k in keys_of(m.group(1))]), text)


def reflist(order):
    return "\n".join(f"{n}. {R[k]}" for k, n in sorted(order.items(), key=lambda x: x[1]))


def strip_markers(s):
    """Remove [AUTHOR: ...], [ANALYSIS PENDING...], [RECHECK...], [PENDING ...] including nested brackets."""
    out, i = [], 0
    while i < len(s):
        if re.match(r"\[(AUTHOR|ANALYSIS PENDING|RECHECK|PENDING)", s[i:]):
            depth, j = 0, i
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
    s = BLOCK.sub(" ", s)
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    s = "\n".join(l for l in s.splitlines() if not l.lstrip().startswith("#"))
    if prose:
        s = strip_markers(s)
        s = re.sub(r"\[[0-9,–]+\]", " ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    return sum(1 for t in s.split() if re.search(r"[A-Za-z0-9€$&]", t))


def block_words(s, kind):
    return sum(words(m.group(2).replace("<!--", "").replace("-->", ""), prose=True)
               for m in BLOCK.finditer(s) if m.group(1) == kind)


def section(text, start, end):
    a = text.index(start)
    b = text.index(end, a)
    return text[a:b]


def check_order(body):
    """Figures/tables: first citation in numerical order; legend/table right after the citing paragraph."""
    warnings = []
    plain = BLOCK.sub(lambda m: " " * len(m.group(0)), body)  # same offsets, blocks blanked
    for kind, pat_cite, pat_block in [
        ("Fig", r"(?<![S\d] )\bFigs? (\d)", r"\*\*Fig (\d)\."),
        ("Table", r"(?<!S\d )\bTables? (\d)\b", r"\*\*Table (\d)\."),
    ]:
        first = {}
        for m in re.finditer(pat_cite, plain):
            n = int(m.group(1))
            first.setdefault(n, m.start())
        nums = sorted(first, key=lambda n: first[n])
        if nums != sorted(nums):
            warnings.append(f"{kind}: first citations out of order: {nums}")
        for m in re.finditer(pat_block, body):
            n = int(m.group(1))
            if n not in first:
                warnings.append(f"{kind} {n}: legend/table present but never cited in the text")
                continue
            if m.start() < first[n]:
                warnings.append(f"{kind} {n}: legend/table placed before its first citation")
                continue
            para_end = body.find("\n\n", first[n])
            gap = body[para_end:m.start()]
            gap = BLOCK.sub("", gap).strip()
            gap = re.sub(r"<!--.*?-->", "", gap, flags=re.S).strip()
            if gap.lstrip("<!-").startswith(("LEGEND", "TABLE")):
                gap = ""
            if gap:
                warnings.append(f"{kind} {n}: not immediately after the citing paragraph "
                                f"(intervening text starts: {gap[:60]!r})")
    return warnings


def main(src, dst):
    text = open(src, encoding="utf-8").read()
    manuscript, si = text.split("<!-- SI FILES START -->", 1)
    order = number(manuscript)
    body_for_checks = manuscript[manuscript.index("## Introduction"):manuscript.index("## References")]
    warnings = check_order(body_for_checks)
    manuscript = replace(manuscript, order).replace("<!--REFERENCES-->", reflist(order))
    # SI files: own numbering
    parts = re.split(r"(<!-- SI FILE: [^>]*-->)", si)
    out_si, si_counts = [parts[0]], {}
    for i in range(1, len(parts), 2):
        head, chunk = parts[i], parts[i + 1]
        o = number(chunk)
        si_counts[head[13:-4].strip()] = len(o)
        chunk = replace(chunk, o).replace("<!--SIREFS-->", reflist(o) if o else "")
        out_si += [head, chunk]
    out = manuscript + "<!-- SI FILES START -->" + "".join(out_si)
    # word counts (before removing the block wrappers)
    sections = {}
    for name, a, b in [("Introduction", "## Introduction", "## Materials and methods"),
                       ("Materials and methods", "## Materials and methods", "## Results"),
                       ("Results", "## Results", "## Discussion"),
                       ("Discussion", "## Discussion", "## Conclusions"),
                       ("Conclusions", "## Conclusions", "## Acknowledgments")]:
        sec = section(out, a, b)
        sections[name] = (words(sec), words(sec, prose=False))
    maintext = section(out, "## Introduction", "## Acknowledgments")
    abstract = section(out, "## Abstract", "## Introduction")
    legends_w = block_words(maintext, "LEGEND")
    tables_w = block_words(maintext, "TABLE")
    rows = "\n".join(f"| {k} | {v[0]:,} | {v[1]:,} |" for k, v in sections.items())
    nocom = re.sub(r"<!--.*?-->", "", out, flags=re.S)  # markers counted outside HTML comments
    pending = sorted(set(re.findall(r"\[ANALYSIS PENDING: ([^\]]*)\]", nocom)) - {"..."})
    report = (
        "WORD COUNTS (computed by build_v2.py; HTML comments, headings, figure legends and tables excluded).\n"
        "'Prose' also removes the editorial markers ([AUTHOR: ...], [ANALYSIS PENDING: ...], [RECHECK: ...]) and numbered "
        "citations; 'raw' keeps them.\n\n"
        "| Section | Prose | Raw |\n|---|---|---|\n" + rows +
        f"\n| **Main text (Introduction to Conclusions)** | **{words(maintext):,}** | **{words(maintext, prose=False):,}** |\n\n"
        f"Abstract: {words(abstract):,} words of prose ({words(abstract, prose=False):,} raw); PLOS ONE limit 300.\n"
        f"Figure legends in the main text: {legends_w:,} words. Tables in the main text: {tables_w:,} words.\n"
        f"References: {len(order)} in the main list; SI lists: "
        + ", ".join(f"{k} {v}" for k, v in si_counts.items()) + ".\n"
        f"Markers outside HTML comments: [AUTHOR] {nocom.count('[AUTHOR')}, "
        f"[ANALYSIS PENDING] {nocom.count('[ANALYSIS PENDING')}, [RECHECK] {nocom.count('[RECHECK')}."
    )
    out = out.replace("WORD COUNT: [filled at build time]", report)
    out = re.sub(r"<!--/?(LEGEND|TABLE)-->\n?", "", out)
    bad = [m.group(0) for m in BANNED.finditer(out)]
    if bad:
        warnings.append(f"model identifiers found: {sorted(set(bad))}")
    open(dst, "w", encoding="utf-8").write(out)
    print(report)
    print("\nDistinct [ANALYSIS PENDING] labels:")
    for p in pending:
        print(" -", p)
    print("\nChecks:", "OK" if not warnings else "")
    for w in warnings:
        print(" WARNING:", w)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
