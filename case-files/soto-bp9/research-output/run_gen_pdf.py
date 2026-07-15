#!/usr/bin/env python3
"""Runner that generates the Soto BP-9 memo PDF using a matter-specific template."""
import sys
from pathlib import Path

SKILL_DIR = Path("/home/user/Claude1/.claude/skills/legal-research")
sys.path.insert(0, str(SKILL_DIR))

import gen_pdf  # noqa: E402

gen_pdf.TEMPLATE = Path("/home/user/Claude1/case-files/soto-bp9/templates/legal-memo.tex")

gen_pdf.generate_pdf(
    input_md=Path("/home/user/Claude1/case-files/soto-bp9/research-output/FINAL-MEMO.md"),
    output_pdf=Path("/home/user/Claude1/case-files/soto-bp9/research-output/FINAL-MEMO.pdf"),
    case_number="67133-054",
    case_name_short="In re Soto BP-9",
    memo_date="July 15, 2026",
)
