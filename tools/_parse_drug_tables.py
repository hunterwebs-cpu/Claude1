"""Parse the §2D1.1(c) Drug Quantity Table and the §2D1.1 Drug Conversion
Tables (Application Note 8(D)) from the USSC Guidelines Manual (Nov 1, 2024).

The Drug Quantity Table is set on PDF pages 160-166; the conversion tables on
PDF pages 172-175. Both are read from the per-page text dump.

Quantities are recorded exactly as printed (value + unit as printed, e.g. "90",
"KG"). A numeric value in grams is also computed for the common weight units so
the wizard can compare quantities, but the printed strings remain authoritative
and are always carried alongside.

Usage: python3 tools/_parse_drug_tables.py <pagedump_dir> <out.json>
"""
import sys, os, json, re

EDITION = "November 1, 2024"
DQT_PAGES = (160, 166)
CONV_PAGES = (172, 175)
BULLET = "⚫"

GROUP_RE = re.compile(r"^\((\d{1,2})\)\s*" + BULLET + r"\s*(.*)$")
LEVEL_RE = re.compile(r"\s*Level\s+(\d{1,2})\s*$")

# "90 KG or more of Heroin"
AT_LEAST_RE = re.compile(
    r"^[Aa]t least ([\d,\.]+)\s*(KG|G|MG|units?)?\s*but less than "
    r"([\d,\.]+)\s*(KG|G|MG|units?)?\s+of\s+(.+)$")
OR_MORE_RE = re.compile(r"^([\d,\.]+)\s*(KG|G|MG|units?)?\s+or more of\s+(.+)$")
LESS_THAN_RE = re.compile(r"^[Ll]ess than ([\d,\.]+)\s*(KG|G|MG|units?)?\s+of\s+(.+)$")

GRAMS = {"KG": 1000.0, "G": 1.0, "MG": 0.001}


def to_grams(value, unit):
    """Convert a printed weight to grams. Returns None for unit counts, which
    are not weights and must not be compared as if they were."""
    if unit not in GRAMS:
        return None
    try:
        return float(value.replace(",", "")) * GRAMS[unit]
    except ValueError:
        return None


def read_pages(pagedir, first, last):
    lines = []
    for pno in range(first, last + 1):
        with open(os.path.join(pagedir, f"p{pno:04d}.txt")) as fh:
            page = fh.read().split("\n")
        for ln in page:
            if re.search(r"Guidelines Manual\s*\(November 1, 20\s*24\)", ln):
                continue
            if ln.strip() in ("§2D1.1", ""):
                lines.append(("", pno))
                continue
            lines.append((ln.rstrip(), pno))
    return lines


# --------------------------------------------------------------------------
# Drug Quantity Table
# --------------------------------------------------------------------------

def parse_quantity_table(pagedir, unparsed):
    lines = read_pages(pagedir, *DQT_PAGES)
    groups, cur, buf = [], None, []

    def flush_entry():
        if not buf:
            return
        text = re.sub(r"\s{2,}", " ", " ".join(x.strip() for x in buf if x.strip())).strip()
        buf.clear()
        if not text:
            return
        text = text.rstrip(";. ")
        # Some rows print two or three alternative measures of the same drug,
        # separated by ", or" (e.g. Methamphetamine / actual / "Ice").
        measures = []
        for piece in re.split(r",\s*or\s+", text):
            piece = piece.strip().rstrip(";. ")
            if not piece:
                continue
            m = AT_LEAST_RE.match(piece)
            if m:
                lo, lounit, hi, hiunit, sub = m.groups()
                unit = hiunit or lounit
                measures.append({
                    "substance": sub.strip(),
                    "printed": piece,
                    "min": lo, "min_unit": lounit or unit,
                    "max": hi, "max_unit": unit,
                    "min_grams": to_grams(lo, lounit or unit),
                    "max_grams": to_grams(hi, unit),
                })
                continue
            m = OR_MORE_RE.match(piece)
            if m:
                lo, unit, sub = m.groups()
                measures.append({
                    "substance": sub.strip(), "printed": piece,
                    "min": lo, "min_unit": unit, "max": None, "max_unit": None,
                    "min_grams": to_grams(lo, unit), "max_grams": None,
                })
                continue
            m = LESS_THAN_RE.match(piece)
            if m:
                hi, unit, sub = m.groups()
                measures.append({
                    "substance": sub.strip(), "printed": piece,
                    "min": None, "min_unit": None, "max": hi, "max_unit": unit,
                    "min_grams": None, "max_grams": to_grams(hi, unit),
                })
                continue
            unparsed.append({"where": "drug quantity table", "text": piece,
                             "reason": "row did not match a printed threshold form"})
        if measures:
            cur["rows"].append({"printed": text, "measures": measures})

    for text, page in lines:
        s = text.strip()
        gm = GROUP_RE.match(s)
        if gm:
            flush_entry()
            if cur:
                groups.append(cur)
            rest = gm.group(2)
            lm = LEVEL_RE.search(rest)
            if not lm:
                unparsed.append({"where": "drug quantity table",
                                 "text": s, "reason": "group has no printed level"})
                cur = None
                continue
            cur = {"group": int(gm.group(1)), "level": int(lm.group(1)),
                   "pdf_page": page, "rows": []}
            buf.append(rest[: lm.start()])
            continue
        if cur is None:
            continue
        if s.startswith(BULLET):
            flush_entry()
            buf.append(s[len(BULLET):])
        elif not s:
            continue
        elif re.match(r"^\*|^CONTROLLED SUBSTANCES", s):
            # "*Notes to Drug Quantity Table:" ends the table. The group in hand
            # is complete and must be kept -- dropping it here silently lost the
            # level 6 group, the lowest tier in the table.
            flush_entry()
            if cur:
                groups.append(cur)
            cur = None
        else:
            buf.append(s)
    flush_entry()
    if cur:
        groups.append(cur)
    return groups


# --------------------------------------------------------------------------
# Drug Conversion Tables
# --------------------------------------------------------------------------

CONV_HEAD_RE = re.compile(r"^([A-Z][A-Z0-9 ,'’\-/\(\)\*\.]{6,})\s+CONVERTED DRUG WEIGHT\s*$")
CONV_ROW_RE = re.compile(
    r"^1\s*(?P<from>gm) of (?P<sub>.+?)\s*=\s*(?P<val>[\d,\.]+)\s*(?P<unit>kg|gm|mg)\.?\s*$",
    re.I)
CONV_UNIT_ROW_RE = re.compile(
    r"^1\s*(?P<from>unit|ml|plant|marihuana plant) of (?P<sub>.+?)\s*=\s*"
    r"(?P<val>[\d,\.]+)\s*(?P<unit>kg|gm|mg)\.?\s*$", re.I)

CONV_G = {"kg": 1000.0, "gm": 1.0, "mg": 0.001}


ROW_COMPLETE_RE = re.compile(r"=\s*[\d,\.]+\s*(kg|gm|mg)\.?\s*$", re.I)
MEASURE_ROW_RE = re.compile(r"^1\s+(\w+)\s*=\s*([\d,\.]+)\s*(\w+)(?:\s*\(liquid\))?\.?\s*$")


def logical_conversion_lines(lines):
    """Join conversion rows that the manual wraps across two lines.

    e.g.  "1 unit of a Schedule III Substance"
          " (except Ketamine) =          1 gm"
    is one row. A row is complete once it ends in "= <number> <unit>".
    """
    out, buf = [], None
    for text, page in lines:
        s = re.sub(r"\s{2,}", " ", text.strip())
        if not s:
            if buf:
                out.append(buf)
                buf = None
            out.append(("", page))
            continue
        if buf:
            joined = (buf[0] + " " + s).strip()
            if ROW_COMPLETE_RE.search(joined):
                out.append((joined, buf[1]))
                buf = None
            else:
                buf = (joined, buf[1])
            continue
        # Only buffer a row that has not reached its "=" yet. A line that
        # already contains "=" is complete as printed, even when its right-hand
        # side is a volume ("1 gm = 1 ml (liquid)") rather than a weight.
        if (re.match(r"^1\s+(gm|unit|ml|plant)\b", s, re.I)
                and "=" not in s):
            buf = (s, page)
            continue
        out.append((s, page))
    if buf:
        out.append(buf)
    return out


def parse_conversion_tables(pagedir, unparsed):
    """Parse Application Note 8(D)'s Drug Conversion Tables and the measurement
    conversion table that follows them, stopping before Note 9."""
    raw = read_pages(pagedir, *CONV_PAGES)
    # Bound the region: it opens at "(D) Drug Conversion Tables.-" and closes at
    # Note 9, which is a different table (typical weight per unit) and is not
    # part of the conversion tables.
    start = next((i for i, (t, _) in enumerate(raw)
                  if t.strip().startswith("(D) Drug Conversion Tables")), 0)
    end = next((i for i, (t, _) in enumerate(raw)
                if re.match(r"^9\.\s*Determining Quantity Based on Doses", t.strip())),
               len(raw))
    lines = logical_conversion_lines(raw[start:end])

    tables, cur, pending_head = [], None, []
    measurement = {"heading": None, "rows": [], "pdf_page": None}
    in_measure = False

    for text, page in lines:
        s = text
        if not s:
            continue
        if "following table is provided" in s:
            in_measure = True
            measurement["heading"] = s
            measurement["pdf_page"] = page
            if cur:
                tables.append(cur)
                cur = None
            continue
        if in_measure:
            if s.upper() == "MEASUREMENT CONVERSION TABLE":
                measurement["title"] = s
                continue
            m = MEASURE_ROW_RE.match(s)
            if m:
                measurement["rows"].append({
                    "printed": s, "from": "1 " + m.group(1),
                    "value": m.group(2), "unit": m.group(3)})
            else:
                unparsed.append({"where": "measurement conversion table",
                                 "text": s, "reason": "not a measurement row"})
            continue
        if "CONVERTED DRUG WEIGHT" in s:
            head = s.replace("CONVERTED DRUG WEIGHT", "").strip()
            full = " ".join(pending_head + ([head] if head else [])).strip()
            pending_head = []
            if cur:
                tables.append(cur)
            cur = {"category": full, "pdf_page": page, "rows": [], "footnotes": []}
            continue
        if cur is None:
            if s.isupper() and len(s) > 6:
                pending_head.append(s)
            continue
        m = CONV_ROW_RE.match(s) or CONV_UNIT_ROW_RE.match(s)
        if m:
            gd = m.groupdict()
            val = gd["val"]
            unit = gd["unit"].lower()
            cur["rows"].append({
                "printed": s,
                "from_amount": "1 " + gd.get("from", "gm"),
                "substance": gd["sub"].strip(),
                "converted_amount": val,
                "converted_unit": gd["unit"],
                "converted_grams": float(val.replace(",", "")) * CONV_G[unit],
            })
            continue
        if s.startswith("*") or s.startswith("Provided"):
            cur["footnotes"].append(s)
            continue
        if s.isupper() and len(s) > 6:
            pending_head.append(s)
            continue
        if cur["footnotes"]:
            cur["footnotes"][-1] = cur["footnotes"][-1] + " " + s
        else:
            unparsed.append({"where": f"conversion table: {cur['category']}",
                             "text": s,
                             "reason": "line is neither a conversion row nor a footnote"})
    if cur:
        tables.append(cur)
    return tables, measurement


def main():
    pagedir, outpath = sys.argv[1], sys.argv[2]
    unparsed = []
    groups = parse_quantity_table(pagedir, unparsed)
    tables, measurement = parse_conversion_tables(pagedir, unparsed)

    substances = sorted({m["substance"] for g in groups for r in g["rows"]
                         for m in r["measures"]})
    conv_substances = sorted({r["substance"] for t in tables for r in t["rows"]})
    payload = {
        "source": "USSC Guidelines Manual §2D1.1(c) Drug Quantity Table and "
                  "§2D1.1 comment. (n.8(D)) Drug Conversion Tables",
        "manual_edition": EDITION,
        "drug_quantity_table": {
            "guideline": "2D1.1",
            "subsection": "(c)",
            "pdf_pages": list(DQT_PAGES),
            "levels": groups,
            "substances": substances,
        },
        "drug_conversion_tables": {
            "guideline": "2D1.1",
            "commentary": "Application Note 8(D)",
            "pdf_pages": list(CONV_PAGES),
            "tables": tables,
            "substances": conv_substances,
            "measurement_conversion_table": measurement,
        },
        "counts": {
            "quantity_table_levels": len(groups),
            "quantity_table_rows": sum(len(g["rows"]) for g in groups),
            "quantity_table_measures": sum(len(r["measures"]) for g in groups
                                           for r in g["rows"]),
            "quantity_table_substances": len(substances),
            "conversion_tables": len(tables),
            "conversion_rows": sum(len(t["rows"]) for t in tables),
            "conversion_substances": len(conv_substances),
        },
        "unparsed": unparsed,
    }
    with open(outpath, "w") as fh:
        json.dump(payload, fh, indent=1)
    print(json.dumps(payload["counts"], indent=1))
    print("levels:", [(g["group"], g["level"], len(g["rows"])) for g in groups])
    print("unparsed:", len(unparsed))
    for u in unparsed[:20]:
        print("   ", u["where"], "|", u["text"][:90])


if __name__ == "__main__":
    main()
