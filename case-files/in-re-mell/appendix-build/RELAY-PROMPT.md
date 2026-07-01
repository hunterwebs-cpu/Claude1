# Relay Prompt — Appendix PDF Completion
# In re S. Bradley Mell, No. 26-16834-EJO (Bankr. D.N.J.)
# Paste this entire message into a regular Claude.ai chat session.
# Attach the files listed below BEFORE sending.

---

I need you to insert missing documents into partially-completed PDF appendix volumes for a bankruptcy opposition filing.

The 8 source documents I am attaching may be **ZIP archives of JPEG page scans** with a `.pdf` extension — a common format from court scanning systems. The 7 appendix volumes are real PDFs. The code below handles both formats: it auto-detects each source file and converts ZIP-of-JPEG files to proper PDFs before merging.

## What you have been given

I am attaching **15 files** to this message:

### 7 partially-compiled appendix volumes (valid PDFs, have placeholder tabs for missing docs):
| Filename | Volume | Current pages |
|---|---|---|
| `appendix_vol_I.pdf` | Volume I — Motion/Schedules | 96 pages |
| `appendix_vol_IIa.pdf` | Volume IIa — State Court Pleadings | 183 pages |
| `appendix_vol_IIb.pdf` | Volume IIb — State Court Pleadings | 209 pages |
| `appendix_vol_IIIb.pdf` | Volume IIIb — Pre-Trial Motions | 48 pages |
| `appendix_vol_IVa.pdf` | Volume IVa — Criminal Proceedings | 6 pages |
| `appendix_vol_IVb.pdf` | Volume IVb — Criminal Proceedings | 108 pages |
| `appendix_vol_VIb.pdf` | Volume VIb — Medical Records | 61 pages |

### 8 missing source documents (may be ZIP-of-JPEG — code will handle conversion automatically):
| Attach as this filename | Tab | Description |
|---|---|---|
| `source_A4.pdf` | A-4 | Doc. 8 — Nagel/Rice Motion to Dismiss Bankruptcy Case |
| `source_B3.pdf` | B-3 | Civil Case Jacket — Amended Complaint and Exhibits |
| `source_B10.pdf` | B-10 | Writ of Attachment Release — December 28, 2023 |
| `source_C5.pdf` | C-5 | Whalen Response in Support of Summary Judgment — March 4, 2026 |
| `source_C9.pdf` | C-9 | Whalen Verification — Nagel Committed Extortion |
| `source_D1.pdf` | D-1 | Plea Agreement — United States v. S. Bradley Mell |
| `source_D3.pdf` | D-3 | Mell Memorandum to Roberts — State v. Mell, Corrected Attachments |
| `source_F8.pdf` | F-8 | B.B. Medical Records — Robinson / Gill, January 3, 2018 |

**Rename your local files to exactly the filenames above before attaching.**

---

## Insertion points

Each compiled volume already has a separator tab page as a placeholder. The source content goes immediately after that separator.

| Volume file | Tab | Separator page | Action |
|---|---|---|---|
| `appendix_vol_I.pdf` | A-4 | page 53 of 96 | insert after page 53 |
| `appendix_vol_IIa.pdf` | B-3 | page 183 of 183 | append at end |
| `appendix_vol_IIb.pdf` | B-10 | page 209 of 209 | append at end |
| `appendix_vol_IIIb.pdf` | C-5 | page 2 of 48 | insert after page 2 |
| `appendix_vol_IIIb.pdf` | C-9 | page 48 of 48 | append at end (after C-5 insertion) |
| `appendix_vol_IVa.pdf` | D-1 | page 2 of 6 | insert after page 2 |
| `appendix_vol_IVb.pdf` | D-3 | page 2 of 108 | insert after page 2 |
| `appendix_vol_VIb.pdf` | F-8 | page 61 of 61 | append at end |

---

## Python code to run

Run this in your code execution environment. It installs required packages, auto-converts any ZIP-of-JPEG source files to real PDFs, then merges everything.

```python
import subprocess, sys

# Install required packages
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "pypdf", "Pillow"], check=True)

import os
import zipfile
import io
from pypdf import PdfReader, PdfWriter
from PIL import Image

# ---------------------------------------------------------------------------
# Step 1: Auto-convert source files (ZIP-of-JPEG → PDF if needed)
# ---------------------------------------------------------------------------

def zip_jpeg_to_pdf(src_path, out_path):
    """Convert a ZIP archive of JPEG scans to a proper PDF."""
    with zipfile.ZipFile(src_path) as zf:
        names = sorted([
            n for n in zf.namelist()
            if n.lower().endswith(('.jpg', '.jpeg', '.png', '.tif', '.tiff'))
            and not n.startswith('__MACOSX')
        ])
        if not names:
            raise ValueError(f"{src_path}: ZIP contains no image files")

        images = []
        for name in names:
            data = zf.read(name)
            img = Image.open(io.BytesIO(data))
            if img.mode not in ('RGB', 'L'):
                img = img.convert('RGB')
            images.append(img)

    # Save as multi-page PDF
    images[0].save(
        out_path, format='PDF', save_all=True,
        append_images=images[1:], resolution=150
    )
    print(f"  Converted {len(images)}-page ZIP-of-JPEG → {out_path}")


def prepare_source(path):
    """Return a path to a valid PDF version of the source file."""
    # Check magic bytes
    with open(path, 'rb') as f:
        magic = f.read(4)

    if magic == b'%PDF':
        print(f"  {os.path.basename(path)}: already a valid PDF")
        return path

    if magic[:2] == b'PK':  # ZIP magic
        out = path.replace('.pdf', '_converted.pdf')
        zip_jpeg_to_pdf(path, out)
        return out

    raise ValueError(
        f"{os.path.basename(path)}: unrecognized format (magic={magic!r}). "
        "Expected PDF or ZIP-of-JPEG."
    )


SOURCE_FILES = [
    "source_A4.pdf", "source_B3.pdf", "source_B10.pdf",
    "source_C5.pdf", "source_C9.pdf",
    "source_D1.pdf", "source_D3.pdf", "source_F8.pdf",
]

print("=== Step 1: Preparing source files ===")
ready = {}  # tab -> converted path
for sf in SOURCE_FILES:
    if not os.path.exists(sf):
        print(f"  MISSING: {sf} — skipping")
        ready[sf] = None
        continue
    try:
        ready[sf] = prepare_source(sf)
    except Exception as e:
        print(f"  ERROR on {sf}: {e}")
        ready[sf] = None


# ---------------------------------------------------------------------------
# Step 2: Merge into appendix volumes
# ---------------------------------------------------------------------------

def insert_after(vol_path, src_path, cut, out_path):
    """Insert src_path pages after 1-indexed page cut of vol_path."""
    vol = PdfReader(vol_path)
    src = PdfReader(src_path)
    n, s = len(vol.pages), len(src.pages)
    w = PdfWriter()
    for i in range(cut):
        w.add_page(vol.pages[i])
    for pg in src.pages:
        w.add_page(pg)
    for i in range(cut, n):
        w.add_page(vol.pages[i])
    with open(out_path, 'wb') as f:
        w.write(f)
    print(f"  OK  {out_path}  ({n} + {s} = {n+s} pages)")


print("\n=== Step 2: Building fixed volumes ===")

# Vol I — A-4 after page 53
if ready.get("source_A4.pdf"):
    insert_after("appendix_vol_I.pdf", ready["source_A4.pdf"], 53, "FIXED_appendix_vol_I.pdf")
else:
    print("  SKIP Vol I (source_A4.pdf not ready)")

# Vol IIa — B-3 at end
if ready.get("source_B3.pdf"):
    insert_after("appendix_vol_IIa.pdf", ready["source_B3.pdf"], 183, "FIXED_appendix_vol_IIa.pdf")
else:
    print("  SKIP Vol IIa (source_B3.pdf not ready)")

# Vol IIb — B-10 at end
if ready.get("source_B10.pdf"):
    insert_after("appendix_vol_IIb.pdf", ready["source_B10.pdf"], 209, "FIXED_appendix_vol_IIb.pdf")
else:
    print("  SKIP Vol IIb (source_B10.pdf not ready)")

# Vol IIIb — C-5 after page 2, then C-9 at end
if ready.get("source_C5.pdf") or ready.get("source_C9.pdf"):
    vol3b = PdfReader("appendix_vol_IIIb.pdf")   # 48 pages
    w = PdfWriter()

    # Cover + C-5 separator (pages 1-2, indices 0-1)
    w.add_page(vol3b.pages[0])
    w.add_page(vol3b.pages[1])

    # C-5 content (if available)
    c5_pages = 0
    if ready.get("source_C5.pdf"):
        c5 = PdfReader(ready["source_C5.pdf"])
        for pg in c5.pages:
            w.add_page(pg)
        c5_pages = len(c5.pages)
    else:
        print("  NOTE: source_C5.pdf missing — C-5 slot will remain empty")

    # C-6 through C-8 content (original pages 3-47, indices 2-46)
    for i in range(2, 47):
        w.add_page(vol3b.pages[i])

    # C-9 separator (original page 48, index 47)
    w.add_page(vol3b.pages[47])

    # C-9 content (if available)
    c9_pages = 0
    if ready.get("source_C9.pdf"):
        c9 = PdfReader(ready["source_C9.pdf"])
        for pg in c9.pages:
            w.add_page(pg)
        c9_pages = len(c9.pages)
    else:
        print("  NOTE: source_C9.pdf missing — C-9 slot will remain empty")

    total = 48 + c5_pages + c9_pages
    with open("FIXED_appendix_vol_IIIb.pdf", 'wb') as f:
        w.write(f)
    print(f"  OK  FIXED_appendix_vol_IIIb.pdf  ({total} pages)")
else:
    print("  SKIP Vol IIIb (both C-5 and C-9 sources missing)")

# Vol IVa — D-1 after page 2
if ready.get("source_D1.pdf"):
    insert_after("appendix_vol_IVa.pdf", ready["source_D1.pdf"], 2, "FIXED_appendix_vol_IVa.pdf")
else:
    print("  SKIP Vol IVa (source_D1.pdf not ready)")

# Vol IVb — D-3 after page 2
if ready.get("source_D3.pdf"):
    insert_after("appendix_vol_IVb.pdf", ready["source_D3.pdf"], 2, "FIXED_appendix_vol_IVb.pdf")
else:
    print("  SKIP Vol IVb (source_D3.pdf not ready)")

# Vol VIb — F-8 at end
if ready.get("source_F8.pdf"):
    insert_after("appendix_vol_VIb.pdf", ready["source_F8.pdf"], 61, "FIXED_appendix_vol_VIb.pdf")
else:
    print("  SKIP Vol VIb (source_F8.pdf not ready)")

print("\n=== Done. Download all FIXED_*.pdf files that were produced. ===")
```

---

## Expected output

The code produces up to 7 fixed volumes (one per source file successfully processed):
- `FIXED_appendix_vol_I.pdf`
- `FIXED_appendix_vol_IIa.pdf`
- `FIXED_appendix_vol_IIb.pdf`
- `FIXED_appendix_vol_IIIb.pdf`
- `FIXED_appendix_vol_IVa.pdf`
- `FIXED_appendix_vol_IVb.pdf`
- `FIXED_appendix_vol_VIb.pdf`

If any source file is missing or unreadable, that volume is skipped and a SKIP message is printed — the other volumes still complete.

Please provide all produced `FIXED_*.pdf` files as downloads when done.

---

## Volumes already complete (do NOT attach or modify these):

- `appendix_vol_IIIa.pdf` — 414 pages, complete
- `appendix_vol_Va.pdf` — complete
- `appendix_vol_Vb.pdf` — complete
- `appendix_vol_VIa.pdf` — complete
- `appendix_vol_VII.pdf` — 49 case law authorities, complete
- `appendix_vol_VIII_SEALED.pdf` — confidential; separate sealed protocol
