# Document Packet Manifest — In re Steven Bradley Mell, Case No. 26-16834-EJO

Prepared for transmittal to debtor's counsel (Sodono). All files retrieved from Google Drive
(primarily the "Whalen Response" folder, ID `1zk4YtetiLq4LWBDyQsQCT3UK59L7zQKN`, plus broader
Drive search) and saved to:

`/home/user/Claude1/case-files/mell-dso/documents-for-sodono/`

Verification method: for every PDF successfully downloaded, the local file's byte size was
diffed against the `fileSize` reported by Google Drive's `get_file_metadata`/`search_files`
calls. All four full-binary downloads below matched **exactly**, confirming byte-perfect,
non-corrupted copies (not re-renders or text reconstructions).

---

## Summary table

| # | Document | Drive File ID | Found? | Local file | Format | Size | Notes |
|---|---|---|---|---|---|---|---|
| 1 | MSA (Marital Settlement Agreement) | `14jwNCtbB4qu2R5Etg1wBuDMFJw_G-cZc` | Yes | `01_MSA.pdf` | PDF, 71 pp | 2,381,549 bytes | Exact byte match to Drive source |
| 2 | Whalen Doc. 23 (Certification + Exhibits 1–4) | `1TL0fe9Gu-GUi6vTM3ruli9KfYC8B35i4` | Yes | `02_Whalen_Doc23_Certification_and_Exhibits_TEXT_EXTRACTION_ONLY.txt` | **Text extraction only** | 76,569 bytes (text) | Source PDF is 17,960,657 bytes (17.9 MB) — exceeds the Drive download tool's 10 MB hard cap. See limitation note below. |
| 3 | Helicopter closing statement | `1jbAmKJFSNBoy6wJ8NKnY0RNZc_HsYbVz` | Yes | `03_Helicopter_Closing_Statement.pdf` | PDF, 17 pp | 2,597,569 bytes | Exact byte match to Drive source |
| 4 | Petition, Doc. 1 (filed 6/12/2026) | `1r8EVuo3dlLCFoK_iWfHmEvUGejgiwXB0` | Yes | `04_Petition_Doc1.pdf` | PDF, 10 pp | 171,802 bytes | Exact byte match; title on Drive was "Br ECF 1" |
| 5 | Schedules, Doc. 11 (filed 6/25/2026) | `1YaOyRwqdv1VLX8LrIVJR1Lx74ilUVkl-` | Yes | `05_Schedules_Doc11.pdf` | PDF, 41 pp | 729,918 bytes | Exact byte match; title on Drive was "118171049370.pdf"; matches docket's "41 pgs" entry exactly |
| 6 | Brad Mell deposition, July 27, 2023 (full) | `1dMlmR-IsR7FHtGDwTVbVGpY3XRPNj7vj` | Yes | `06_Mell_Deposition_2023-07-27_FULL_TEXT_EXTRACTION_ONLY.txt` | **Text extraction only** | 251,251 bytes (text) | Source PDF is 24,688,109 bytes (24.7 MB) — exceeds the 10 MB download cap. See limitation note below. Text extraction is complete (Pages 1–226 + court reporter's certificate all present). |
| 7 | Deposition Exhibit (the one shown re: $800,000 reconciliation) | N/A — embedded in file above | Located, not separable | — | — | Deposition Exhibit 3 (Bates **LGK9293**) exists only as pages embedded within the deposition transcript PDF itself. No standalone copy of this exhibit exists elsewhere in Drive (targeted searches for "LGK9293" and "W.H. Mell balance sheet" returned no separate file). Because the parent transcript exceeds the download size cap, this exhibit could not be extracted as a separate binary. |

---

## Limitation note — files #2 and #6 (binary not retrievable)

The Google Drive `download_file_content` tool used in this session enforces a **hard 10 MB
cap** on binary downloads ("File too large for download, over limit of 10 MB"). This is a
tool/API-level limitation, not a permissions or access issue — both files are owned by the
requesting account and are otherwise fully accessible. Two source documents exceed that cap:

- Doc. 23 (Whalen Certification + Exhibits 1–4): **17,960,657 bytes**
- Brad Mell Deposition, 7/27/2023 (full transcript with exhibits): **24,688,109 bytes**

For both, the actual PDF binary could not be downloaded through the available tooling. As a
fallback, the tool's natural-language full-text extraction (`read_file_content`) was used
instead and saved as plain `.txt` files, clearly labeled `TEXT_EXTRACTION_ONLY` in the
filename so they are not mistaken for the original PDFs. The deposition extraction was
verified to run continuously from Page 1 through Page 226 plus the court reporter's
certificate, i.e., it appears complete, not truncated. The Doc. 23 extraction likewise runs
through the final page (Stipulation of Dismissal) and appears complete.

**These two text files are not suitable substitutes for producing to opposing counsel or the
court as document exhibits** — they lack signatures, formatting, exhibit stamps, letterhead,
and Bates numbers. If Sodono's office needs the actual PDFs, they will need to be retrieved
directly from Drive (e.g., a paralegal downloading via the Drive web UI, which is not subject
to this API cap) or from PACER (Doc. 23 is a bankruptcy court ECF filing, retrievable via
PACER using Case No. 26-16834-EJO).

---

## Deposition testimony detail (Task 5)

**File:** "Brad Mell Depo July 27, 2023.pdf" (Drive ID `1dMlmR-IsR7FHtGDwTVbVGpY3XRPNj7vj`)
**Case:** B.B. v. S. Bradley Mell, et al., Docket No. ESX-L-7200-19 (Superior Court of NJ,
Essex County, Law Division)
**Deponent:** Steven Bradley Mell (remote/Zoom deposition, taken 7/27/2023, ~10:00 a.m. EST)
**Examining attorney for the relevant testimony:** Harry D. McEnroe, Esq. (counsel for
Gulfstream CM/GM), continuing the examination that began with Mr. Borrelli

### a. Page range confirmation

The prior citation of **pp. 168–171** is confirmed as substantially correct, with a slight
refinement: the core exchange runs from **page 168 through page 172** of the transcript
(note: the OCR/text-extraction rendered the two-column transcript+summary-index layout in a
jumbled/interleaved order in places, so page numbers below are drawn from the explicit "Page
NNN" headers embedded in the source text, cross-checked against the surrounding Q&A flow):

- **Page 168** — Discussion opens on whether the W.H. Mell "capital account" books/records
  are in the "Judge Berman boxes"; Mell says he does not know where the records are.
- **Page 168–169** — Q: "...are you saying that you believe she got 60 percent of the 800
  that was not in dispute or are you saying you believe she got 60 percent of the 1.625?"
- **Page 169, lines 1–4** — The key admission (verbatim, quoted below).
- **Page 170–172** — Exhibit 3 is put back in front of the witness; the witness is asked to
  reconcile the $1.6 million figure against the $800,000 shown as the only distribution
  reflected on Exhibit 3.

### b. The key testimony — verbatim, with page/line cites

> **Page 169, Lines 1–4** (A = Mell):
> "A I'm telling you she got 60 percent of the capital account, which is roughly one-six,
> one-seven. Whatever that number was, she got her 60 percent. I'm 100 percent on that."

Immediately preceding, at **Page 168, lines 22–25 / Page 169 (continued)**, counsel's
question:

> "Q ...are you saying that you believe she got 60 percent of the 800 that was not in dispute
> or are you saying you believe she got 60 percent of the 1.625?"

### c. The exhibit used to test/impeach that testimony

The exhibit shown to reconcile the $800,000 figure is **Deposition Exhibit 3**, Bates-stamped
**LGK9293**, first marked earlier in the same deposition at **transcript page 25** (per the
deposition's own exhibit index at the front of the transcript: "Deposition Exhibit 3 ... 25 ...
LGK9293").

**Verbatim marking/introduction language (page 25 of the transcript, at the point the exhibit
was first shown to the witness):**

> "Q Thank you, Mr. Mell. If you could please turn to Exhibit 3.
> (DEPOSITION EXHIBIT NUMBER 3 WAS MARKED FOR IDENTIFICATION.)
> A Okay.
> Q Do you recognize this document?
> A I do."

**Description of the exhibit given immediately after marking (transcript page ~25–26):**

> "Q Can you tell us what it is?
> A The balance sheet of W.H. Mell that says as of December 31st, 2018.
> Q Who prepared this document?
> A I believe our FinOp. ... Dan [Beaton]."

So Exhibit 3 = **"W.H. Mell balance sheet as of December 31, 2018"** (prepared by W.H. Mell's
FINOP, Dan Beaton), Bates LGK9293.

**Where the witness is confronted with it against the $800,000/$1.6M discrepancy (transcript
pages 170–172):**

> "Q Sure. On Exhibit 3, towards the end, there is a reference to distributions under equity.
> Do you see that?
> A Yes, I do.
> Q And the only distribution amount reflected there is $800,000. Do you see that, Mr. Mell?
> A Correct.
> Q So wouldn't we expect to see the — if the capital account was distributed in full, the
> entire 1.6 million, wouldn't we see it there somewhere on Exhibit 3?
> A Well, it wasn't distributed 100 percent in full at this time. Because the broker-dealer
> was still — even though it had withdrawn, it was still winding down.
> Q Okay. So the other 825,000 of the capital account you would expect to see in 2019?
> A No. So if you look — if you look at this balance sheet — and I'm dusting off the cobwebs
> here. So what this shows you is $800,000 was distributed in all of 2018 for everything."

Mell is unable to reconcile the remaining ~$825,000 (i.e., $1.625M capital account balance
minus the $800,000 shown as distributed on Exhibit 3), testifying at transcript page 173:
"Million dollar question. I don't know where the actual books and records are..."

### d. Whether Exhibit 3 exists as a separate downloadable file

**No.** Targeted Drive searches for the Bates number "LGK9293" and for "W.H. Mell balance
sheet" returned no standalone file — Exhibit 3 exists only as pages appended/embedded within
the 24.7 MB deposition transcript PDF itself (consistent with standard Veritext deposition
transcript+exhibits production format). Because that parent PDF exceeds the 10 MB download
cap described above, Exhibit 3 could not be isolated and downloaded separately in this
session. If Sodono's office needs Exhibit 3 as a standalone PDF, it will need to be extracted
from the full transcript PDF (obtainable outside this tool's size cap) or requested from
Veritext/prior counsel of record (Riker Danzig, Mountainside Securities' counsel, marked the
exhibit at the July 27, 2023 deposition).

### Related figures found in the same testimony (context)

- **$1.625 million** — the W.H. Mell capital account balance as of July 28, 2018 (per a
  separate exhibit discussed at transcript page 164, likely Exhibit 5/the MSA-adjacent
  document referenced there — not Exhibit 3).
- **$1,800,000 (~$1.8M)** — total stockholders' equity of W.H. Mell per the Dec. 31, 2017
  statement of financial condition (Exhibit 2), discussed at transcript pages 22–24.
- **60%/40% split** — Mell's repeated testimony (transcript pages 28–29, 78–81, 168–169) that
  W.H. Mell capital account distributions were split 60% to Kimberly Ruggles Mell ("Kim") and
  40% to himself.
- **$825,000** — the gap counsel identifies between the $1.625M capital account balance and
  the $800,000 shown as distributed on Exhibit 3 (transcript pages 165, 172).

---

## Other documents referenced during the search (context only, not part of the requested packet)

- "Bankruptcy filing.pdf" (Drive ID `1t7yDQquMe5-Tz1SEOXBH5_jEdOcyhhhG`) — the *state-court*
  Notice of Filing of Voluntary Petition (with the Notice of Case Filing and Automatic Stay
  order as Exhibits A/B), filed in ESX-L-007200-19. This is **not** the bankruptcy court's
  Doc. 1 petition itself; the actual Doc. 1 was separately located as "Br ECF 1" (item #4
  above).
