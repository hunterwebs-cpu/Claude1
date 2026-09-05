// Convert the SORA Memorandum of Law markdown into a .docx, WITHOUT the
// caption block (the client is building the caption separately and will
// hand it back to be merged in). Applies the corrected heading numbering
// scheme: Roman numerals for top-level headings, letters for subheadings,
// numbers for sub-subheadings -- while preserving the standard NY brief
// "POINT I" / "POINT II" convention for the ARGUMENT section's own
// sub-headings (kept as-is, not additionally lettered).
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Header, Footer, PageNumber, UnderlineType,
} = require('docx');

const SRC = process.argv[2];
const OUT = process.argv[3];

const raw = fs.readFileSync(SRC, 'utf-8');
const lines = raw.split('\n');
const n = lines.length;

const FONT = 'Times New Roman';
const SIZE = 24; // 12pt, half-point units
const DOUBLE = 480; // line spacing for double-spaced body (240 = single)
const SINGLE = 240;

const ROMAN = [[10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']];
function toRoman(num) {
  let out = '';
  for (const [v, sym] of ROMAN) { while (num >= v) { out += sym; num -= v; } }
  return out;
}
const LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

// ---- inline markdown -> TextRun[] ----
function inlineRuns(text, baseOpts = {}) {
  // Tokenize on **bold**, *italic*, and [^n] footnote refs.
  const runs = [];
  let i = 0;
  const pushPlain = (s) => {
    if (!s) return;
    runs.push(new TextRun({ text: s, font: FONT, size: SIZE, ...baseOpts }));
  };
  const re = /(\*\*\*(.+?)\*\*\*|\*\*(.+?)\*\*|\*([^*]+?)\*|\[\^(\d+)\])/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    pushPlain(text.slice(last, m.index));
    if (m[2] !== undefined) {
      runs.push(new TextRun({ text: m[2], font: FONT, size: SIZE, bold: true, italics: true, ...baseOpts }));
    } else if (m[3] !== undefined) {
      runs.push(new TextRun({ text: m[3], font: FONT, size: SIZE, bold: true, ...baseOpts }));
    } else if (m[4] !== undefined) {
      runs.push(new TextRun({ text: m[4], font: FONT, size: SIZE, italics: true, ...baseOpts }));
    } else if (m[5] !== undefined) {
      runs.push(new TextRun({ text: m[5], font: FONT, size: 16, superScript: true, ...baseOpts }));
    }
    last = re.lastIndex;
  }
  pushPlain(text.slice(last));
  if (runs.length === 0) runs.push(new TextRun({ text: '', font: FONT, size: SIZE, ...baseOpts }));
  return runs;
}

// ---- skip caption: everything before the first "# " line ----
let i = 0;
while (i < n && !lines[i].startsWith('# ')) i++;

const children = [];

// Title
const titleText = lines[i].slice(2).trim();
i++;
children.push(new Paragraph({
  children: inlineRuns(titleText, { bold: true }),
  alignment: AlignmentType.CENTER,
  spacing: { before: 0, after: 80, line: SINGLE },
  border: { bottom: { color: '000000', space: 4, style: 'single', size: 4 } },
}));
children.push(new Paragraph({ text: '', spacing: { after: 160, line: SINGLE } }));

let h1Counter = 0; // Roman: top-level (## )
let h2Letter = 0;  // Letters: subheadings under a non-POINT ## section
let h3Number = 0;  // Numbers: sub-subheadings under a POINT's lettered items
let inArgument = false;
let inPointBlock = false; // true right after "### POINT n", to merge the next ### title line into the same heading block

const footnotes = {}; // num -> text
let paraBuf = [];
let inNotes = false;

function flushPara(opts = {}) {
  if (paraBuf.length === 0) return;
  const text = paraBuf.map((p) => p.trim()).filter(Boolean).join(' ');
  paraBuf = [];
  if (!text) return;
  children.push(new Paragraph({
    children: inlineRuns(text),
    alignment: AlignmentType.JUSTIFIED,
    spacing: { line: DOUBLE, after: 0 },
    indent: { firstLine: 720 },
    ...opts,
  }));
}

while (i < n) {
  const line = lines[i];
  const s = line.trim();

  // horizontal rule
  if (/^-{3,}$/.test(s)) { flushPara(); i++; continue; }

  // blank line -> paragraph break
  if (s === '') { flushPara(); i++; continue; }

  // footnote definition
  let m = s.match(/^\[\^(\d+)\]:\s*(.*)$/);
  if (m) { flushPara(); footnotes[m[1]] = m[2]; i++; continue; }

  // #### -- sub-subheading (numbers), used under POINT II's lettered items
  if (s.startsWith('#### ')) {
    flushPara();
    let text = s.slice(5).trim();
    // Source already prefixes these with "A. ", "B. ", etc. -- strip that
    // and replace with the correct sub-subheading NUMBER per the client's
    // roman/letter/number scheme.
    text = text.replace(/^[A-Z]\.\s*/, '');
    h3Number++;
    children.push(new Paragraph({
      children: inlineRuns(`${h3Number}. ${text}`, { bold: true, italics: true }),
      spacing: { before: 200, after: 120, line: SINGLE },
    }));
    i++; continue;
  }

  // ### -- either a STATEMENT OF FACTS subheading (letters), or POINT I/II
  // and its descriptive title (kept as the NY-convention heading, merged
  // into one block rather than left as a second, unlabeled heading)
  if (s.startsWith('### ')) {
    flushPara();
    const text = s.slice(4).trim();
    if (/^POINT\s+[IVX]+$/i.test(text)) {
      h3Number = 0; // reset sub-subheading numbering for the new Point
      children.push(new Paragraph({
        children: inlineRuns(text, { bold: true }),
        alignment: AlignmentType.CENTER,
        spacing: { before: 280, after: 20, line: SINGLE },
      }));
      inPointBlock = true;
      i++; continue;
    }
    if (inPointBlock) {
      // This is the ALL-CAPS descriptive title directly under "POINT n" --
      // part of the same heading block, not a separately numbered item.
      children.push(new Paragraph({
        children: inlineRuns(text, { bold: true }),
        alignment: AlignmentType.CENTER,
        spacing: { before: 0, after: 200, line: SINGLE },
      }));
      inPointBlock = false;
      i++; continue;
    }
    // Otherwise: an ordinary lettered subheading (e.g. under STATEMENT OF FACTS)
    h2Letter++;
    const label = LETTERS[h2Letter - 1] || String(h2Letter);
    children.push(new Paragraph({
      children: inlineRuns(`${label}. ${text}`, { bold: true, italics: true }),
      spacing: { before: 200, after: 100, line: SINGLE },
    }));
    i++; continue;
  }

  // ## -- top-level heading (Roman numerals)
  if (s.startsWith('## ')) {
    flushPara();
    const heading = s.slice(3).trim();
    if (heading.toUpperCase() === 'NOTES') {
      inNotes = true;
      children.push(new Paragraph({
        border: { top: { color: '000000', space: 4, style: 'single', size: 4 } },
        spacing: { before: 200, after: 0, line: SINGLE },
        text: '',
      }));
      children.push(new Paragraph({
        children: [new TextRun({ text: 'NOTES', font: FONT, size: SIZE, bold: true })],
        alignment: AlignmentType.CENTER,
        spacing: { before: 100, after: 160, line: SINGLE },
      }));
      i++; continue;
    }
    h1Counter++;
    h2Letter = 0; // reset letter numbering for each new top-level section
    inArgument = heading.toUpperCase() === 'ARGUMENT';
    children.push(new Paragraph({
      children: inlineRuns(`${toRoman(h1Counter)}. ${heading}`, { bold: true }),
      spacing: { before: 280, after: 160, line: SINGLE },
    }));
    i++; continue;
  }

  // signature block: a line of underscores
  if (/^_{10,}$/.test(s)) {
    flushPara();
    children.push(new Paragraph({ text: '', spacing: { before: 480, after: 0, line: SINGLE } }));
    children.push(new Paragraph({
      children: [new TextRun({ text: s, font: FONT, size: SIZE })],
      spacing: { line: SINGLE, after: 0 },
    }));
    i++;
    while (i < n && lines[i].trim() !== '' && !lines[i].trim().startsWith('#')) {
      const sig = lines[i].trim();
      if (/^-{3,}$/.test(sig)) break;
      children.push(new Paragraph({
        children: inlineRuns(sig),
        spacing: { line: SINGLE, after: 0 },
      }));
      i++;
    }
    continue;
  }

  // "Dated:" / "Respectfully submitted," lines
  if (s.startsWith('Dated:') || s === 'Respectfully submitted,') {
    flushPara();
    children.push(new Paragraph({ text: '', spacing: { before: 240, after: 0, line: SINGLE } }));
    children.push(new Paragraph({
      children: inlineRuns(s),
      spacing: { line: SINGLE, after: 0 },
    }));
    i++;
    if (s.startsWith('Dated:') && i < n && lines[i].trim().startsWith('&nbsp;')) {
      const venue = lines[i].trim().replace(/(&nbsp;)+/g, '     ');
      children.push(new Paragraph({
        children: inlineRuns(venue),
        spacing: { line: SINGLE, after: 0 },
      }));
      i++;
    }
    continue;
  }

  // NOTES section numbered footnote lines: "[1] text"
  if (inNotes) {
    const fm = s.match(/^\[(\d+)\]\s*(.*)$/);
    if (fm) {
      flushPara();
      children.push(new Paragraph({
        children: [
          new TextRun({ text: `[${fm[1]}] `, font: FONT, size: 20, bold: true }),
          ...inlineRuns(fm[2], { size: 20 }),
        ],
        alignment: AlignmentType.JUSTIFIED,
        spacing: { line: SINGLE, after: 120 },
      }));
      i++; continue;
    }
  }

  paraBuf.push(line);
  i++;
}
flushPara();

if (Object.keys(footnotes).length && !inNotes) {
  children.push(new Paragraph({
    border: { top: { color: '000000', space: 4, style: 'single', size: 4 } },
    spacing: { before: 200, after: 0, line: SINGLE },
    text: '',
  }));
  children.push(new Paragraph({
    children: [new TextRun({ text: 'NOTES', font: FONT, size: SIZE, bold: true })],
    alignment: AlignmentType.CENTER,
    spacing: { before: 100, after: 160, line: SINGLE },
  }));
  Object.keys(footnotes).sort((a, b) => Number(a) - Number(b)).forEach((num) => {
    children.push(new Paragraph({
      children: [
        new TextRun({ text: `[${num}] `, font: FONT, size: 20, bold: true }),
        ...inlineRuns(footnotes[num], { size: 20 }),
      ],
      alignment: AlignmentType.JUSTIFIED,
      spacing: { line: SINGLE, after: 120 },
    }));
  });
}

const doc = new Document({
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 }, // US Letter
        margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 },
      },
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 20 })],
        })],
      }),
    },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(OUT, buf);
  console.log('Wrote', OUT, `(${Object.keys(footnotes).length} footnotes)`);
});
