"""Dump the raw text layer of the USSG PDF, one file per page, plus a combined
page-delimited file. Run once; every other script reads the dump, not the PDF.

Usage: python3 tools/_dump_text.py <pdf> <outdir>
"""
import sys, os, json
from pypdf import PdfReader

def main(pdf_path, outdir):
    os.makedirs(outdir, exist_ok=True)
    reader = PdfReader(pdf_path)
    pages = []
    for i, page in enumerate(reader.pages, start=1):
        txt = page.extract_text() or ""
        pages.append(txt)
        with open(os.path.join(outdir, f"p{i:04d}.txt"), "w") as fh:
            fh.write(txt)
    with open(os.path.join(outdir, "all_pages.json"), "w") as fh:
        json.dump(pages, fh)
    print(f"pages={len(pages)} empty={sum(1 for p in pages if not p.strip())}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
