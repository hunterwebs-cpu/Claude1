// General-purpose converter: SORA filing markdown -> court-formatted .docx,
// using the client's own confirmed caption layout (a borderless 2-column
// table) and the Roman-numeral / letter / number heading scheme, with NO
// "POINT I" / "POINT II" convention -- argument subsections are lettered
// like every other subsection.
//
// Usage: node md_to_ny_filing_docx.js <config.json>
// config.json: { mdPath, outPath, titleText, judge, hearingDate, indexNo,
//                nysidNo, partyBlock: [...] }
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, Table, TableRow,
  TableCell, WidthType, BorderStyle, VerticalAlign, Footer, PageNumber,
  TabStopType,
} = require('docx');

// Indent/tab-stop values (DXA) replicating a real Word multilevel list --
// matched to the client's own memo (word/numbering.xml, abstractNumId=3):
// number sits in the hanging area, a tab jumps to `left`, where both the
// heading text and any wrapped continuation line align. This is what
// produces the tab between "I." and the heading, and the visual stepped
// indent of letters under Roman numerals and numbers under letters.
const HEADING_LEVELS = {
  roman: { left: 1080, hanging: 720 },   // ## top-level (I., II., ...)
  letter: { left: 1440, hanging: 360 },  // ### subheading (A., B., ...)
  number: { left: 2340, hanging: 360 },  // #### sub-subheading (1., 2., ...)
};

const FONT = 'Times New Roman';
const SIZE = 24; // 12pt
const DOUBLE = 480;
const SINGLE = 240;
const ROMAN = [[10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']];
function toRoman(num) {
  let out = '';
  for (const [v, sym] of ROMAN) { while (num >= v) { out += sym; num -= v; } }
  return out;
}
const LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

function wrapTitle(text, maxChars = 28) {
  const words = text.split(' ');
  const lines = [];
  let cur = '';
  for (const w of words) {
    const next = cur ? `${cur} ${w}` : w;
    if (next.length > maxChars && cur) { lines.push(cur); cur = w; }
    else { cur = next; }
  }
  if (cur) lines.push(cur);
  return lines;
}

function inlineRuns(text, baseOpts = {}) {
  const runs = [];
  const pushPlain = (s) => { if (s) runs.push(new TextRun({ text: s, font: FONT, size: SIZE, ...baseOpts })); };
  const re = /(\*\*\*(.+?)\*\*\*|\*\*(.+?)\*\*|\*([^*]+?)\*|\[\^(\d+)\])/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    pushPlain(text.slice(last, m.index));
    if (m[2] !== undefined) runs.push(new TextRun({ text: m[2], font: FONT, size: SIZE, bold: true, italics: true, ...baseOpts }));
    else if (m[3] !== undefined) runs.push(new TextRun({ text: m[3], font: FONT, size: SIZE, bold: true, ...baseOpts }));
    else if (m[4] !== undefined) runs.push(new TextRun({ text: m[4], font: FONT, size: SIZE, italics: true, ...baseOpts }));
    else if (m[5] !== undefined) runs.push(new TextRun({ text: m[5], font: FONT, size: 16, superScript: true, ...baseOpts }));
    last = re.lastIndex;
  }
  pushPlain(text.slice(last));
  if (runs.length === 0) runs.push(new TextRun({ text: '', font: FONT, size: SIZE, ...baseOpts }));
  return runs;
}

function noBorders() {
  const none = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
  return { top: none, bottom: none, left: none, right: none };
}

function cell(text, { width, bold = false, italics = false, leftIndent } = {}) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    verticalAlign: VerticalAlign.TOP,
    borders: noBorders(),
    margins: { top: 40, bottom: 40, left: leftIndent || 0, right: 0 },
    children: [new Paragraph({
      children: text ? [new TextRun({ text, font: FONT, size: SIZE, bold, italics })] : [],
      spacing: { after: 40, line: SINGLE },
    })],
  });
}

function buildCaption(cfg) {
  const LEFT_W = 4680, RIGHT_W = 4680;
  const children = [];
  children.push(new Paragraph({
    children: [new TextRun({ text: 'State of New York', font: FONT, size: SIZE, bold: true })],
    alignment: AlignmentType.CENTER, spacing: { after: 40, line: SINGLE },
  }));
  children.push(new Paragraph({
    children: [new TextRun({ text: 'Monroe County Supreme & County Courts', font: FONT, size: SIZE, bold: true })],
    alignment: AlignmentType.CENTER, spacing: { after: 40, line: SINGLE },
  }));
  children.push(new Paragraph({
    children: [new TextRun({ text: '-----------------------------------------------------X', font: FONT, size: SIZE })],
    spacing: { before: 120, after: 0, line: SINGLE },
  }));

  const titleLines = wrapTitle(cfg.titleText, 28);
  const leftRows = [
    ['In re: Matter of the Application for a.', cfg.indexLine],
    ['Risk Level Determination Pursuant to.', cfg.hearingLine],
    ['Article 6-C of the Correction Law.', cfg.beforeLine],
    ['(Sex Offender Registration Act) as to:', ''],
    ['', ''],
  ];
  const rows = leftRows.map(([l, r]) => new TableRow({ children: [cell(l, { width: LEFT_W }), cell(r, { width: RIGHT_W })] }));

  const partyNameRows = ['JEFFREY BERNECKY,', 'NYSID No. OS6430'];
  const numMidRows = Math.max(partyNameRows.length, titleLines.length);
  for (let i = 0; i < numMidRows; i++) {
    const l = partyNameRows[i] || '';
    const r = titleLines[i] || '';
    rows.push(new TableRow({
      children: [
        cell(l, { width: LEFT_W, bold: i === 0 }),
        cell(r, { width: RIGHT_W, bold: true }),
      ],
    }));
  }
  rows.push(new TableRow({
    children: [
      cell('Respondent, Pro Se.', { width: LEFT_W, italics: true, leftIndent: 360 }),
      cell('', { width: RIGHT_W }),
    ],
  }));

  children.push(new Table({
    width: { size: LEFT_W + RIGHT_W, type: WidthType.DXA },
    columnWidths: [LEFT_W, RIGHT_W],
    rows,
  }));
  children.push(new Paragraph({ text: '', spacing: { after: 0, line: SINGLE } }));
  children.push(new Paragraph({
    children: [new TextRun({ text: '-----------------------------------------------------X', font: FONT, size: SIZE })],
    spacing: { before: 120, after: 0, line: SINGLE },
  }));
  return children;
}

function convert(cfg) {
  const raw = fs.readFileSync(cfg.mdPath, 'utf-8');
  const lines = raw.split('\n');
  const n = lines.length;
  let i = 0;
  while (i < n && !lines[i].startsWith('# ')) i++; // skip any old caption
  i++; // skip the "# TITLE" line itself -- title now lives in the caption table

  const children = buildCaption(cfg);

  let h1Counter = 0, h2Letter = 0, h3Number = 0;
  const footnotes = {};
  let paraBuf = [];
  let inNotes = false;

  function flushPara() {
    if (paraBuf.length === 0) return;
    const text = paraBuf.map((p) => p.trim()).filter(Boolean).join(' ');
    paraBuf = [];
    if (!text) return;
    children.push(new Paragraph({
      children: inlineRuns(text),
      alignment: AlignmentType.JUSTIFIED,
      spacing: { line: DOUBLE, after: 0 },
      indent: { firstLine: 720 },
    }));
  }

  while (i < n) {
    const line = lines[i];
    const s = line.trim();

    if (/^-{3,}$/.test(s)) { flushPara(); i++; continue; }
    if (s === '') { flushPara(); i++; continue; }

    let m = s.match(/^\[\^(\d+)\]:\s*(.*)$/);
    if (m) { flushPara(); footnotes[m[1]] = m[2]; i++; continue; }

    if (s.startsWith('#### ')) {
      flushPara();
      let text = s.slice(5).trim().replace(/^[0-9]+\.\s*/, '');
      h3Number++;
      const lvl = HEADING_LEVELS.number;
      children.push(new Paragraph({
        tabStops: [{ type: TabStopType.LEFT, position: lvl.left }],
        indent: { left: lvl.left, hanging: lvl.hanging },
        children: [
          new TextRun({ text: `${h3Number}.\t`, font: FONT, size: SIZE, bold: true, italics: true }),
          ...inlineRuns(text, { bold: true, italics: true }),
        ],
        spacing: { before: 200, after: 100, line: SINGLE },
      }));
      i++; continue;
    }

    if (s.startsWith('### ')) {
      flushPara();
      let text = s.slice(4).trim().replace(/^[A-Z]\.\s*/, '');
      h2Letter++; h3Number = 0;
      const label = LETTERS[h2Letter - 1] || String(h2Letter);
      const lvl = HEADING_LEVELS.letter;
      children.push(new Paragraph({
        tabStops: [{ type: TabStopType.LEFT, position: lvl.left }],
        indent: { left: lvl.left, hanging: lvl.hanging },
        children: [
          new TextRun({ text: `${label}.\t`, font: FONT, size: SIZE, bold: true, italics: true }),
          ...inlineRuns(text, { bold: true, italics: true }),
        ],
        spacing: { before: 200, after: 100, line: SINGLE },
      }));
      i++; continue;
    }

    if (s.startsWith('## ')) {
      flushPara();
      const heading = s.slice(3).trim();
      if (heading.toUpperCase() === 'NOTES') {
        inNotes = true;
        children.push(new Paragraph({
          border: { top: { style: BorderStyle.SINGLE, size: 4, space: 4, color: '000000' } },
          spacing: { before: 200, after: 0, line: SINGLE }, text: '',
        }));
        children.push(new Paragraph({
          children: [new TextRun({ text: 'NOTES', font: FONT, size: SIZE, bold: true })],
          alignment: AlignmentType.CENTER, spacing: { before: 100, after: 160, line: SINGLE },
        }));
        i++; continue;
      }
      if (heading.startsWith('(') && heading.endsWith(')')) {
        children.push(new Paragraph({
          children: inlineRuns(heading, { italics: true }),
          alignment: AlignmentType.CENTER,
          spacing: { before: 0, after: 240, line: SINGLE },
        }));
        i++; continue;
      }
      h1Counter++; h2Letter = 0; h3Number = 0;
      {
        const lvl = HEADING_LEVELS.roman;
        children.push(new Paragraph({
          tabStops: [{ type: TabStopType.LEFT, position: lvl.left }],
          indent: { left: lvl.left, hanging: lvl.hanging },
          children: [
            new TextRun({ text: `${toRoman(h1Counter)}.\t`, font: FONT, size: SIZE, bold: true }),
            ...inlineRuns(heading, { bold: true }),
          ],
          spacing: { before: 280, after: 160, line: SINGLE },
        }));
      }
      i++; continue;
    }

    if (/^_{10,}$/.test(s)) {
      flushPara();
      children.push(new Paragraph({ text: '', spacing: { before: 480, after: 0, line: SINGLE } }));
      children.push(new Paragraph({ children: [new TextRun({ text: s, font: FONT, size: SIZE })], spacing: { line: SINGLE, after: 0 } }));
      i++;
      while (i < n && lines[i].trim() !== '' && !lines[i].trim().startsWith('#')) {
        const sig = lines[i].trim();
        if (/^-{3,}$/.test(sig)) break;
        children.push(new Paragraph({ children: inlineRuns(sig), spacing: { line: SINGLE, after: 0 } }));
        i++;
      }
      continue;
    }

    if (s.startsWith('Dated:') || s === 'Respectfully submitted,') {
      flushPara();
      children.push(new Paragraph({ text: '', spacing: { before: 240, after: 0, line: SINGLE } }));
      children.push(new Paragraph({ children: inlineRuns(s), spacing: { line: SINGLE, after: 0 } }));
      i++;
      if (s.startsWith('Dated:') && i < n && lines[i].trim().startsWith('&nbsp;')) {
        const venue = lines[i].trim().replace(/(&nbsp;)+/g, '     ');
        children.push(new Paragraph({ children: inlineRuns(venue), spacing: { line: SINGLE, after: 0 } }));
        i++;
      }
      continue;
    }

    if (inNotes) {
      const fm = s.match(/^\[(\d+)\]\s*(.*)$/);
      if (fm) {
        flushPara();
        children.push(new Paragraph({
          children: [new TextRun({ text: `[${fm[1]}] `, font: FONT, size: 20, bold: true }), ...inlineRuns(fm[2], { size: 20 })],
          alignment: AlignmentType.JUSTIFIED, spacing: { line: SINGLE, after: 120 },
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
      border: { top: { style: BorderStyle.SINGLE, size: 4, space: 4, color: '000000' } },
      spacing: { before: 200, after: 0, line: SINGLE }, text: '',
    }));
    children.push(new Paragraph({
      children: [new TextRun({ text: 'NOTES', font: FONT, size: SIZE, bold: true })],
      alignment: AlignmentType.CENTER, spacing: { before: 100, after: 160, line: SINGLE },
    }));
    Object.keys(footnotes).sort((a, b) => Number(a) - Number(b)).forEach((num) => {
      children.push(new Paragraph({
        children: [new TextRun({ text: `[${num}] `, font: FONT, size: 20, bold: true }), ...inlineRuns(footnotes[num], { size: 20 })],
        alignment: AlignmentType.JUSTIFIED, spacing: { line: SINGLE, after: 120 },
      }));
    });
  }

  const doc = new Document({
    sections: [{
      properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } },
      footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 20 })] })] }) },
      children,
    }],
  });

  return Packer.toBuffer(doc).then((buf) => {
    fs.writeFileSync(cfg.outPath, buf);
    console.log('Wrote', cfg.outPath, `(${Object.keys(footnotes).length} footnotes)`);
  });
}

if (require.main === module) {
  const cfgPath = process.argv[2];
  const cfg = JSON.parse(fs.readFileSync(cfgPath, 'utf-8'));
  convert(cfg);
}
module.exports = { convert, buildCaption, wrapTitle };
