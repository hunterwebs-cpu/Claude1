"""Assemble the four public JSON files from the parsed intermediates.

This step adds one thing the parsers deliberately do not: an explicit judgement,
per guideline, about whether a wizard can print a number at all. Anything that
depends on another guideline, on a table the wizard does not hold, on a prior
record, or on a cross reference that can move the case to a different guideline
is marked so the interface hands off to "ask your attorney" instead of showing a
figure that looks authoritative and is not.

Usage:
  python3 tools/_assemble.py <work_dir> <assets/data dir>
where <work_dir> holds appA.json, ch2.json, drugs.json and tax.json.
"""
import sys, os, json, re

EDITION = "November 1, 2024"
SOURCE = ("United States Sentencing Commission, Guidelines Manual, "
          "effective November 1, 2024")
DISCLAIMER = ("Reference data transcribed from the United States Sentencing "
              "Guidelines Manual. It is not legal advice, it does not account "
              "for Chapter Three or Chapter Four adjustments, criminal history, "
              "statutory mandatory minimums, or departures and variances, and it "
              "must not be relied on to make a decision about a case. Talk to a "
              "lawyer.")

# Must match language about the defendant's RECORD, never about the offense of
# conviction. A bare "convicted of" matches "the defendant is convicted of
# 18 U.S.C. § 2252(a)(4)" — which identifies the instant offense, not a prior —
# and wrongly flagged §2G2.2, §2B1.1, §2D1.1, §2A6.1 and §2H4.1 as depending on
# criminal record. §2G2.2's base offense level turns on possession versus
# distribution/receipt; §2B1.1's turns on the statutory maximum.
PRIOR_RECORD_RE = re.compile(
    r"prior convictions?|previously (?:been )?convicted|"
    r"felony convictions?|criminal history|"
    r"sustaining (?:at least )?(?:one|two)", re.I)
OTHER_GUIDELINE_RE = re.compile(r"§2[A-Z]\d+\.\d+")


def handoff_reasons(g):
    """Why a calculator must not print a single number for this guideline."""
    reasons = []
    bol = g.get("base_offense_level")
    if g.get("body_is_prose_instruction"):
        reasons.append("The guideline states an instruction rather than a "
                       "level: the offense level comes from another guideline.")
    if not bol and not g.get("table") and not g.get("body_is_prose_instruction"):
        reasons.append("No base offense level subsection is printed for this "
                       "guideline.")
    if bol:
        derived = [a for a in bol["alternatives"] if a.get("level") is None]
        if derived:
            reasons.append("At least one base offense level is derived from "
                           "another guideline or from a table, not printed as a "
                           "number.")
        if any(PRIOR_RECORD_RE.search(a.get("condition") or "")
               for a in bol["alternatives"]):
            reasons.append("The base offense level depends on prior "
                           "convictions, which requires legal judgement about "
                           "what those convictions count as.")
        if bol["apply_rule"] in ("greatest", "least") and len(bol["alternatives"]) > 1:
            reasons.append("Several base offense levels compete and the manual "
                           "directs applying the " + bol["apply_rule"] + ".")
    if g.get("cross_references"):
        reasons.append("A cross reference can move the case to a different "
                       "guideline entirely, which can change the level "
                       "substantially.")
    stuck = [s["subsection"] for s in g.get("specific_offense_characteristics", [])
             if s.get("adjustment_not_reducible")]
    if stuck:
        reasons.append("These specific offense characteristics do not reduce to "
                       "a fixed adjustment: " + ", ".join(stuck) + ".")
    return reasons


def annotate(ch2):
    for g in ch2["guidelines"]:
        if g["status"] != "active":
            continue
        reasons = handoff_reasons(g)
        bol = g.get("base_offense_level")
        can = bool(bol) and all(a.get("level") is not None
                                for a in bol["alternatives"]) \
            and not g.get("body_is_prose_instruction")
        g["wizard"] = {
            "base_offense_level_is_a_plain_number":
                bool(bol) and can and len(bol["alternatives"]) == 1,
            "base_offense_level_computable_from_this_file": can,
            "handoff_to_attorney": bool(reasons),
            "handoff_reasons": reasons,
            "references_other_guidelines": sorted(set(
                OTHER_GUIDELINE_RE.findall(json.dumps(
                    {k: v for k, v in g.items() if k != "wizard"})))),
        }
    return ch2


def meta(extra):
    d = {
        "manual_edition": EDITION,
        "source": SOURCE,
        "source_document": "USSC Guidelines Manual (November 1, 2024), 620pp PDF",
        "generated_by": "tools/ in this repository; see tools/_verify.py for the "
                        "verification that accompanies each build",
        "disclaimer": DISCLAIMER,
    }
    d.update(extra)
    return d


def write(path, payload):
    with open(path, "w") as fh:
        json.dump(payload, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    return os.path.getsize(path)


def main():
    work, outdir = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    appa = json.load(open(os.path.join(work, "appA.json")))
    ch2 = annotate(json.load(open(os.path.join(work, "ch2.json"))))
    drugs = json.load(open(os.path.join(work, "drugs.json")))
    tax = json.load(open(os.path.join(work, "tax.json")))

    sizes = {}

    sizes["ussg-statutory-index.json"] = write(
        os.path.join(outdir, "ussg-statutory-index.json"),
        meta({
            "part": "Appendix A (Statutory Index)",
            "pdf_pages": appa["pdf_pages"],
            "counts": {
                "statutes_indexed": appa["entry_count"],
                "statutes_mapping_to_more_than_one_guideline":
                    sum(1 for e in appa["entries"] if len(e["guidelines"]) > 1),
                "distinct_guidelines_referenced":
                    len({g for e in appa["entries"] for g in e["guidelines"]}),
            },
            "unresolved": appa["unparsed"],
            "entries": appa["entries"],
        }))

    sizes["ussg-guidelines.json"] = write(
        os.path.join(outdir, "ussg-guidelines.json"),
        meta({
            "part": "Chapter Two (Offense Conduct)",
            "pdf_pages": ch2["pdf_pages"],
            "counts": ch2["counts"],
            "extraction_notes": ch2["extraction_notes"],
            "chapter2_parts": ch2["chapter2_parts"],
            "unresolved": ch2["unparsed"],
            "guidelines": ch2["guidelines"],
        }))

    dq = drugs["drug_quantity_table"]
    sizes["ussg-drug-quantity.json"] = write(
        os.path.join(outdir, "ussg-drug-quantity.json"),
        meta({
            "part": "§2D1.1(c) Drug Quantity Table and §2D1.1 comment. (n.8(D)) "
                    "Drug Conversion Tables",
            "counts": drugs["counts"],
            "not_in_the_quantity_table": {
                "note": "The Drug Quantity Table does not name these substances. "
                        "They are handled by converting to Converted Drug Weight "
                        "using the conversion tables, and then reading the "
                        "Converted Drug Weight row of the quantity table.",
                "examples": ["Oxycodone", "Hydrocodone", "MDMA / ecstasy",
                             "Morphine", "Codeine", "Methadone",
                             "Psilocybin mushrooms", "GHB", "Synthetic cannabinoids"],
            },
            "drug_quantity_table": dq,
            "drug_conversion_tables": drugs["drug_conversion_tables"],
            "unresolved": drugs["unparsed"],
        }))

    sizes["ussg-offense-taxonomy.json"] = write(
        os.path.join(outdir, "ussg-offense-taxonomy.json"),
        meta({
            "part": "Plain-English offense taxonomy for the calculator's two "
                    "dropdowns",
            "authorship": "Crime type and offense term labels and descriptions "
                          "are written for a lay reader. Every statute-to-"
                          "guideline mapping is copied from Appendix A.",
            "counts": tax["counts"],
            "unresolved": tax["unresolved"],
            "crime_types": tax["crime_types"],
            "offense_terms": tax["offense_terms"],
        }))

    handoff = [g["section"] for g in ch2["guidelines"]
               if g.get("wizard", {}).get("handoff_to_attorney")]
    computable = [g["section"] for g in ch2["guidelines"]
                  if g.get("wizard", {}).get("base_offense_level_computable_from_this_file")]
    print("written:")
    for k, v in sizes.items():
        print(f"   {k:<34} {v/1024:8.1f} KB")
    print(f"active guidelines: {ch2['counts']['active']}")
    print(f"  base offense level computable from this data: {len(computable)}")
    print(f"  needs an attorney handoff for at least one reason: {len(handoff)}")


if __name__ == "__main__":
    main()
