#!/usr/bin/env bash
# Rebuild every USSG data file in assets/data/ from the Guidelines Manual PDF,
# then verify the result against that same PDF.
#
#   ./tools/_build_all.sh /path/to/glm-2024.pdf [work_dir]
#
# When a new manual edition is published, update the page ranges and EDITION
# constants at the top of each parser, drop in the new PDF, and run this. The
# verification step at the end is what tells you whether the ranges are right --
# it re-reads the PDF independently of the parsers.
#
# Requires: pypdf. If pypdf fails on import, run: pip install --force-reinstall cffi
set -euo pipefail

PDF="${1:?usage: _build_all.sh <guidelines-manual.pdf> [work_dir]}"
WORK="${2:-$(mktemp -d)}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DATA="$ROOT/assets/data"

echo "==> text dump"
python3 "$ROOT/tools/_dump_text.py"        "$PDF"        "$WORK/pages"
echo "==> Appendix A (Statutory Index)"
python3 "$ROOT/tools/_parse_appendix_a.py" "$WORK/pages" "$WORK/appA.json"
echo "==> Chapter Two (Offense Conduct)"
python3 "$ROOT/tools/_parse_chapter2.py"   "$WORK/pages" "$WORK/ch2.json" "$WORK/appA.json"
echo "==> Drug Quantity and Conversion Tables"
python3 "$ROOT/tools/_parse_drug_tables.py" "$WORK/pages" "$WORK/drugs.json"
echo "==> offense taxonomy"
python3 "$ROOT/tools/_build_taxonomy.py"   "$WORK/appA.json" "$WORK/ch2.json" "$WORK/tax.json"
echo "==> assemble"
python3 "$ROOT/tools/_assemble.py"         "$WORK" "$DATA"
echo "==> verify"
python3 "$ROOT/tools/_verify.py" "$PDF" \
    "$DATA/ussg-statutory-index.json" \
    "$DATA/ussg-guidelines.json" \
    "$DATA/ussg-drug-quantity.json" \
    --taxonomy "$DATA/ussg-offense-taxonomy.json" \
    --sample 2000 --out "$WORK/verification-report.json"
echo
echo "work dir: $WORK"
