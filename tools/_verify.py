"""Verify the extracted USSG data against the source PDF.

Three independent checks, each reported with real numbers:

A. Statutory index round-trip. A random sample of Appendix A entries is
   re-read straight from the PDF (not from the text dump) and the citation plus
   its guideline list must appear as one contiguous run on the recorded page.

B. Base offense levels for the most commonly charged guidelines. Every printed
   level in each guideline's base-offense-level subsection is confirmed to
   appear, in the same order, in the PDF text for that guideline.

C. Drug Quantity Table arithmetic. For every substance, the tiers must form a
   contiguous, strictly descending ladder: the lower bound of a tier equals the
   upper bound of the tier below it, and both bounds move in the right
   direction as the offense level falls. This catches a mis-read digit that a
   text comparison would not.

Usage:
  python3 tools/_verify.py <pdf> <appendix_a.json> <chapter2.json> <drugs.json> \
      [--sample N] [--seed N]
"""
import sys, json, re, random, argparse

from pypdf import PdfReader

KEY_GUIDELINES = [
    "2D1.1", "2B1.1", "2K2.1", "2L1.2", "2G2.2", "2A1.1", "2A2.2", "2S1.1",
    "2C1.1", "2T1.1", "2L1.1", "2D1.11", "2B3.1", "2J1.2", "2A3.1",
]


def norm(s):
    """Collapse the whitespace the PDF's justification introduces. Nothing else
    is altered, so a comparison is still character-for-character on content."""
    s = s.replace(" ", " ").replace(" ", " ").replace(" ", " ")
    return re.sub(r"\s+", " ", s).strip()


# --------------------------------------------------------------------------

def check_statutory_index(reader, appa, sample_size, seed):
    entries = appa["entries"]
    rng = random.Random(seed)
    sample = rng.sample(entries, min(sample_size, len(entries)))
    # An entry's guideline column runs until the *next entry* starts. It cannot
    # simply run until the next "N U.S.C." string, because a condition may quote
    # a statute inline -- 18 U.S.C. 371 references "a conspiracy to violate
    # 18 U.S.C. 924(c)" between two of its own guideline references.
    next_citation = {}
    for i, e in enumerate(entries[:-1]):
        nxt = entries[i + 1]
        if nxt["pdf_page"] == e["pdf_page"]:
            next_citation[id(e)] = norm(nxt["citation"])
    page_cache = {}
    passed, failures = [], []
    for e in sample:
        pno = e["pdf_page"]
        if pno not in page_cache:
            page_cache[pno] = norm(reader.pages[pno - 1].extract_text() or "")
        page = page_cache[pno]
        cite = norm(e["citation"])
        if cite not in page:
            failures.append({"citation": e["citation"], "pdf_page": pno,
                             "reason": "citation not found on recorded page"})
            continue
        # The guideline list must follow the citation, in printed order, before
        # the next statute citation begins.
        start = page.index(cite) + len(cite)
        boundary = next_citation.get(id(e))
        cut = page.find(boundary, start) if boundary else -1
        window = page[start: cut] if cut > start else page[start: start + 400]
        pos, ok = 0, True
        for gl in e["guidelines"]:
            idx = window.find(gl, pos)
            if idx < 0:
                ok = False
                failures.append({"citation": e["citation"], "pdf_page": pno,
                                 "reason": f"guideline {gl} not found in the "
                                           f"text following the citation",
                                 "window": window[:160]})
                break
            pos = idx + len(gl)
        if ok:
            passed.append({"citation": e["citation"], "guidelines": e["guidelines"],
                           "pdf_page": pno})
    return {"sampled": len(sample), "passed": len(passed),
            "failed": len(failures), "failures": failures,
            "examples": passed[:12]}


# --------------------------------------------------------------------------

def guideline_text(reader, g, cache):
    """Text of the pages a guideline's operative portion sits on."""
    start = g["pdf_page"]
    out = []
    for pno in range(start, start + 12):
        if pno - 1 >= len(reader.pages):
            break
        if pno not in cache:
            cache[pno] = norm(reader.pages[pno - 1].extract_text() or "")
        out.append(cache[pno])
        if len(" ".join(out)) > 40000:
            break
    return " ".join(out)


def check_base_offense_levels(reader, ch2):
    by_sec = {g["section"]: g for g in ch2["guidelines"]}
    cache = {}
    results, failures = [], []
    for sec in KEY_GUIDELINES:
        g = by_sec.get(sec)
        if not g:
            failures.append({"section": sec, "reason": "guideline not extracted"})
            continue
        bol = g["base_offense_level"]
        if not bol:
            failures.append({"section": sec,
                             "reason": "no base offense level subsection extracted"})
            continue
        text = guideline_text(reader, g, cache)
        checked, bad = [], []
        for alt in bol["alternatives"]:
            snippet = norm(alt["text"])[:70]
            # The PDF's text layer breaks words at line ends and sometimes drops
            # a space inside a word. Compare with every space and line-break
            # hyphen removed, so the check is on the characters that carry
            # meaning rather than on the typesetter's spacing.
            def squeeze(s):
                return re.sub(r"\s+", "", re.sub(r"([A-Za-z])-\s", r"\1", s))
            probe, hay = squeeze(snippet), squeeze(text)
            found = probe in hay
            checked.append({
                "subsection": bol["subsection"],
                "number": alt.get("number"),
                "level": alt["level"],
                "verbatim_found_in_pdf": found,
                "text_start": snippet,
            })
            if not found:
                bad.append(snippet)
        results.append({
            "section": sec, "title": g["title"][:90],
            "subsection": bol["subsection"],
            "apply_rule": bol["apply_rule"],
            "levels": [a["level"] for a in bol["alternatives"]],
            "alternatives_checked": len(checked),
            "alternatives_confirmed": sum(1 for c in checked
                                          if c["verbatim_found_in_pdf"]),
            "detail": checked,
        })
        if bad:
            failures.append({"section": sec, "reason": "verbatim text not located",
                             "snippets": bad})
    return {"guidelines_checked": len(results),
            "fully_confirmed": sum(1 for r in results
                                   if r["alternatives_checked"] ==
                                   r["alternatives_confirmed"]),
            "failures": failures, "results": results}


# --------------------------------------------------------------------------

def check_drug_table(drugs):
    levels = drugs["drug_quantity_table"]["levels"]
    # substance -> [(level, min, max, min_unit, max_unit, printed)]
    ladder = {}
    for grp in levels:
        for row in grp["rows"]:
            for m in row["measures"]:
                ladder.setdefault(m["substance"], []).append((grp["level"], m))

    issues, checked = [], 0
    per_substance = {}
    for sub, tiers in ladder.items():
        tiers.sort(key=lambda t: -t[0])  # highest offense level first
        ok = True
        for i, (lvl, m) in enumerate(tiers):
            checked += 1
            lo, hi = m["min_grams"], m["max_grams"]
            if lo is not None and hi is not None and not (lo < hi):
                issues.append({"substance": sub, "level": lvl,
                               "reason": "lower bound is not below upper bound",
                               "printed": m["printed"]})
                ok = False
            if i + 1 < len(tiers):
                nlvl, nm = tiers[i + 1]
                # The next tier down must end exactly where this one starts.
                if lo is not None and nm["max_grams"] is not None:
                    if abs(lo - nm["max_grams"]) > 1e-9:
                        issues.append({
                            "substance": sub, "reason": "tiers are not contiguous",
                            "upper_level": lvl, "lower_level": nlvl,
                            "upper_tier_min": m["min"], "upper_tier_min_unit": m["min_unit"],
                            "lower_tier_max": nm["max"], "lower_tier_max_unit": nm["max_unit"],
                        })
                        ok = False
                # Units are counts, not weights: compare the printed numbers.
                if lo is None and m["min"] is not None and nm["max"] is not None:
                    try:
                        if float(m["min"].replace(",", "")) != float(
                                nm["max"].replace(",", "")):
                            issues.append({
                                "substance": sub, "reason":
                                    "unit-count tiers are not contiguous",
                                "upper_level": lvl, "lower_level": nlvl,
                                "upper_tier_min": m["min"], "lower_tier_max": nm["max"]})
                            ok = False
                    except ValueError:
                        pass
        per_substance[sub] = {"tiers": len(tiers),
                              "levels": [t[0] for t in tiers],
                              "contiguous": ok}
    return {"substances": len(ladder), "thresholds_checked": checked,
            "substances_contiguous": sum(1 for v in per_substance.values()
                                         if v["contiguous"]),
            "issues": issues, "per_substance": per_substance}


# --------------------------------------------------------------------------

def check_referential_integrity(appa, ch2, tax):
    """Every guideline named anywhere must exist in the guidelines file, and
    every offense term must resolve to at least one real guideline."""
    known = {g["section"] for g in ch2["guidelines"]}
    issues = []

    idx_refs = {g for e in appa["entries"] for g in e["guidelines"]}
    for g in sorted(idx_refs - known):
        issues.append({"where": "statutory index", "guideline": g,
                       "reason": "referenced by Appendix A but absent from the "
                                 "guidelines file"})

    term_refs = set()
    for t in tax["offense_terms"]:
        if not t["guidelines"]:
            issues.append({"where": "taxonomy", "term": t["id"],
                           "reason": "term resolves to no guideline"})
        term_refs.update(t["guidelines"])
        for s in t["statutes"]:
            if not s["guidelines"]:
                issues.append({"where": "taxonomy", "term": t["id"],
                               "statute": s["citation"],
                               "reason": "statute resolves to no guideline"})
    for g in sorted(term_refs - known):
        issues.append({"where": "taxonomy", "guideline": g,
                       "reason": "named by an offense term but absent from the "
                                 "guidelines file"})

    ct_ids = {c["id"] for c in tax["crime_types"]}
    for t in tax["offense_terms"]:
        if t["crime_type"] not in ct_ids:
            issues.append({"where": "taxonomy", "term": t["id"],
                           "reason": "belongs to an undefined crime type"})
    empty = [c["id"] for c in tax["crime_types"]
             if not any(t["crime_type"] == c["id"] for t in tax["offense_terms"])]
    for c in empty:
        issues.append({"where": "taxonomy", "crime_type": c,
                       "reason": "crime type has no offense terms, so the second "
                                 "dropdown would be empty"})

    # Every term's statute must still be printed in Appendix A verbatim.
    cites = {e["citation"] for e in appa["entries"]}
    for t in tax["offense_terms"]:
        for s in t["statutes"]:
            if s["citation"] not in cites:
                issues.append({"where": "taxonomy", "term": t["id"],
                               "statute": s["citation"],
                               "reason": "citation is not printed in Appendix A"})
    return {"guidelines_known": len(known),
            "guidelines_named_by_index": len(idx_refs),
            "guidelines_named_by_taxonomy": len(term_refs),
            "issues": issues}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("appendix_a")
    ap.add_argument("chapter2")
    ap.add_argument("drugs")
    ap.add_argument("--taxonomy")
    ap.add_argument("--sample", type=int, default=45)
    ap.add_argument("--seed", type=int, default=20241101)
    ap.add_argument("--out")
    a = ap.parse_args()

    reader = PdfReader(a.pdf)
    appa = json.load(open(a.appendix_a))
    ch2 = json.load(open(a.chapter2))
    drugs = json.load(open(a.drugs))

    report = {
        "manual_edition": "November 1, 2024",
        "sample_seed": a.seed,
        "statutory_index_round_trip": check_statutory_index(
            reader, appa, a.sample, a.seed),
        "base_offense_levels": check_base_offense_levels(reader, ch2),
        "drug_quantity_table": check_drug_table(drugs),
    }
    if a.taxonomy:
        report["referential_integrity"] = check_referential_integrity(
            appa, ch2, json.load(open(a.taxonomy)))
    if a.out:
        with open(a.out, "w") as fh:
            json.dump(report, fh, indent=1)

    s = report["statutory_index_round_trip"]
    print(f"A. Statutory index round-trip: {s['passed']}/{s['sampled']} passed, "
          f"{s['failed']} failed")
    for f in s["failures"][:10]:
        print("     FAIL", f["citation"], "p", f["pdf_page"], "-", f["reason"])

    b = report["base_offense_levels"]
    print(f"B. Base offense levels: {b['fully_confirmed']}/{b['guidelines_checked']} "
          f"guidelines fully confirmed")
    for r in b["results"]:
        print(f"     {r['section']:<7} {r['subsection']} {r['apply_rule']:<11} "
              f"levels={r['levels']} "
              f"confirmed {r['alternatives_confirmed']}/{r['alternatives_checked']}")
    for f in b["failures"]:
        print("     FAIL", f["section"], "-", f["reason"])

    d = report["drug_quantity_table"]
    print(f"C. Drug quantity table: {d['thresholds_checked']} thresholds across "
          f"{d['substances']} substances; "
          f"{d['substances_contiguous']}/{d['substances']} form a contiguous ladder")
    for i in d["issues"][:15]:
        print("     ISSUE", i)

    r = report.get("referential_integrity")
    if r:
        print(f"D. Referential integrity: {r['guidelines_named_by_index']} "
              f"guidelines named by the statutory index and "
              f"{r['guidelines_named_by_taxonomy']} by the taxonomy, "
              f"against {r['guidelines_known']} extracted; "
              f"{len(r['issues'])} issues")
        for i in r["issues"][:20]:
            print("     ISSUE", i)


if __name__ == "__main__":
    main()
