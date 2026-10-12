// Markdown -> court-formatted .docx for a W.D.N.Y. criminal filing (pro se).
// Adapted from .claude/skills/brief-formatting/scripts/md_to_filing_docx.js:
// federal two-column borderless caption (dashed text rules, no paragraph
// borders), Roman/letter/number headings with tab-stop + hanging indent,
// double-spaced justified body, single-spaced headings/signature block,
// native Word footnotes ([^n] / [^n]: in the markdown), page numbers.
//
// Usage: node md_to_wdny_motion_docx.js <config.json>
// config.json: { mdPath, outPath, court: [..lines..], leftBlock: [{text, indent?, bold?}],
//                rightBlock: [{text, bold?}], titleWrap }
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, Table, TableRow,
  TableCell, WidthType, BorderStyle, VerticalAlign, Footer, PageNumber,
  TabStopType, FootnoteReferenceRun,
} = require('docx');

const HEADING_LEVELS = {
  roman: { left: 1080, hanging: 720 },
  letter: { left: 1440, hanging: 360 },
  number: { left: 2340, hanging: 360 },
};
const FONT = 'Times New Roman';
const SIZE = 24; // 12pt
const DOUBLE = 480;
const SINGLE = 240;
const ROMAN = [[10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']];
function toRoman(num) { let out = ''; for (const [v, s] of ROMAN) { while (num >= v) { out += s; num -= v; } } return out; }
const LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const RULE = '-----------------------------------------------------------------X';

function smarten(text) {
  // Curly quotes/apostrophes; non-breaking space after section/paragraph symbols.
  return text
    .replace(/(^|[\s(\[—])"/g, '$1“')
    .replace(/"/g, '”')
    .replace(/(^|[\s(\[—“])'/g, '$1‘')
    .replace(/'/g, '’')
    .replace(/(§§?|¶¶?) /g, '$1 ');
}

function wrapTitle(text, maxChars = 30) {
  const words = text.split(' '); const lines = []; let cur = '';
  for (const w of words) { const next = cur ? `${cur} ${w}` : w; if (next.length > maxChars && cur) { lines.push(cur); cur = w; } else { cur = next; } }
  if (cur) lines.push(cur); return lines;
}

function inlineRuns(rawText, baseOpts = {}) {
  const runs = [];
  const size = baseOpts.size || SIZE;
  // Smarten the whole paragraph first so quote direction is judged across
  // run boundaries (an apostrophe right after an italic case name must not
  // become an opening quote).
  const text = smarten(rawText);
  const pushPlain = (s) => { if (s) runs.push(new TextRun({ text: s, font: FONT, size, ...baseOpts })); };
  const re = /(\*\*\*(.+?)\*\*\*|\*\*(.+?)\*\*|\*([^*]+?)\*|\[\^(\d+)\])/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    pushPlain(text.slice(last, m.index));
    if (m[2] !== undefined) runs.push(new TextRun({ text: m[2], font: FONT, size, bold: true, italics: true, ...baseOpts }));
    else if (m[3] !== undefined) runs.push(new TextRun({ text: m[3], font: FONT, size, bold: true, ...baseOpts }));
    else if (m[4] !== undefined) runs.push(new TextRun({ text: m[4], font: FONT, size, italics: true, ...baseOpts }));
    else if (m[5] !== undefined) runs.push(new FootnoteReferenceRun(Number(m[5])));
    last = re.lastIndex;
  }
  pushPlain(text.slice(last));
  if (runs.length === 0) runs.push(new TextRun({ text: '', font: FONT, size, ...baseOpts }));
  return runs;
}

function noBorders() { const none = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' }; return { top: none, bottom: none, left: none, right: none }; }

function blockCell(lines, width) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA }, verticalAlign: VerticalAlign.TOP, borders: noBorders(),
    margins: { top: 40, bottom: 40, left: 0, right: 0 },
    children: lines.map((l) => new Paragraph({
      children: [new TextRun({ text: smarten(l.text || ''), font: FONT, size: SIZE, bold: !!l.bold, italics: !!l.italics })],
      indent: l.indent ? { left: l.indent } : undefined,
      spacing: { after: 0, line: SINGLE },
    })),
  });
}

function buildCaption(cfg) {
  const LEFT_W = 5040, RIGHT_W = 4320;
  const children = [];
  for (const line of cfg.court) {
    children.push(new Paragraph({ children: [new TextRun({ text: line, font: FONT, size: SIZE, bold: true })], alignment: AlignmentType.CENTER, spacing: { after: 0, line: SINGLE } }));
  }
  children.push(new Paragraph({ children: [new TextRun({ text: RULE, font: FONT, size: SIZE })], spacing: { before: 240, after: 0, line: SINGLE } }));
  const right = [...cfg.rightBlock];
  const titleLines = cfg.titleLines || (cfg.titleText ? wrapTitle(cfg.titleText, cfg.titleWrap || 26) : []);
  if (titleLines.length) { right.push({ text: '' }); for (const t of titleLines) right.push({ text: t, bold: true }); }
  children.push(new Table({
    width: { size: LEFT_W + RIGHT_W, type: WidthType.DXA }, columnWidths: [LEFT_W, RIGHT_W],
    rows: [new TableRow({ children: [blockCell(cfg.leftBlock, LEFT_W), blockCell(right, RIGHT_W)] })],
  }));
  children.push(new Paragraph({ children: [new TextRun({ text: RULE, font: FONT, size: SIZE })], spacing: { before: 0, after: 360, line: SINGLE } }));
  return children;
}

function convert(cfg) {
  const raw = fs.readFileSync(cfg.mdPath, 'utf-8');
  const lines = raw.split('\n'); const n = lines.length;
  let i = 0;
  while (i < n && !lines[i].startsWith('# ')) i++;
  const titleText = i < n ? lines[i].slice(2).trim() : (cfg.titleText || '');
  i++;
  const children = buildCaption({ ...cfg, titleText });

  // Footnote definitions first pass
  const footnotes = {};
  for (const l of lines) { const m = l.trim().match(/^\[\^(\d+)\]:\s*(.*)$/); if (m) footnotes[m[1]] = m[2]; }

  let h1 = 0, h2 = 0, h3 = 0; let paraBuf = [];
  function flushPara() {
    if (!paraBuf.length) return;
    const text = paraBuf.map((p) => p.trim()).filter(Boolean).join(' '); paraBuf = [];
    if (!text) return;
    children.push(new Paragraph({ children: inlineRuns(text), alignment: AlignmentType.JUSTIFIED, spacing: { line: DOUBLE, after: 0 }, indent: { firstLine: 720 } }));
  }
  function heading(label, text, lvl, opts) {
    children.push(new Paragraph({
      tabStops: [{ type: TabStopType.LEFT, position: lvl.left }], indent: { left: lvl.left, hanging: lvl.hanging },
      children: [new TextRun({ text: `${label}\t`, font: FONT, size: SIZE, bold: true }), ...inlineRuns(text, { bold: true })],
      spacing: { before: opts.before, after: opts.after, line: SINGLE }, keepNext: true,
    }));
  }

  while (i < n) {
    const line = lines[i]; const s = line.trim();
    if (/^-{3,}$/.test(s) || s === '') { flushPara(); i++; continue; }
    if (/^\[\^(\d+)\]:/.test(s)) { flushPara(); i++; continue; }
    if (s.startsWith('#### ')) { flushPara(); h3++; heading(`${h3}.`, s.slice(5).trim(), HEADING_LEVELS.number, { before: 200, after: 120 }); i++; continue; }
    if (s.startsWith('### ')) { flushPara(); h2++; h3 = 0; heading(`${LETTERS[h2 - 1]}.`, s.slice(4).trim(), HEADING_LEVELS.letter, { before: 240, after: 160 }); i++; continue; }
    if (s.startsWith('## ')) { flushPara(); h1++; h2 = 0; h3 = 0; heading(`${toRoman(h1)}.`, s.slice(3).trim(), HEADING_LEVELS.roman, { before: 320, after: 200 }); i++; continue; }
    if (s.startsWith('> ')) {
      flushPara(); const q = [];
      while (i < n && lines[i].trim().startsWith('> ')) { q.push(lines[i].trim().slice(2)); i++; }
      children.push(new Paragraph({ children: inlineRuns(q.join(' ')), alignment: AlignmentType.JUSTIFIED, indent: { left: 1440, right: 1440 }, spacing: { line: SINGLE, before: 120, after: 240 } }));
      continue;
    }
    if (/^_{10,}$/.test(s)) {
      flushPara();
      children.push(new Paragraph({ text: '', spacing: { before: 480, after: 0, line: SINGLE } }));
      children.push(new Paragraph({ children: [new TextRun({ text: s, font: FONT, size: SIZE })], indent: { left: 4680 }, spacing: { line: SINGLE, after: 0 } }));
      i++;
      while (i < n && lines[i].trim() !== '' && !lines[i].trim().startsWith('#')) {
        children.push(new Paragraph({ children: inlineRuns(lines[i].trim()), indent: { left: 4680 }, spacing: { line: SINGLE, after: 0 } })); i++;
      }
      continue;
    }
    if (s.startsWith('Dated:') || s === 'Respectfully submitted,') {
      flushPara();
      const ind = s === 'Respectfully submitted,' ? 4680 : 0;
      children.push(new Paragraph({ text: '', spacing: { before: 240, after: 0, line: SINGLE } }));
      children.push(new Paragraph({ children: inlineRuns(s), indent: { left: ind }, spacing: { line: SINGLE, after: 0 } }));
      i++;
      if (s.startsWith('Dated:') && i < n && lines[i].trim().startsWith('&nbsp;')) {
        children.push(new Paragraph({ children: inlineRuns(lines[i].trim().replace(/(&nbsp;)+/g, '')), indent: { left: 720 }, spacing: { line: SINGLE, after: 0 } })); i++;
      }
      continue;
    }
    paraBuf.push(line); i++;
  }
  flushPara();

  const fnDefs = {};
  for (const [num, text] of Object.entries(footnotes)) {
    fnDefs[num] = { children: [new Paragraph({ children: inlineRuns(text), alignment: AlignmentType.JUSTIFIED, spacing: { line: SINGLE, after: 0 } })] };
  }

  const doc = new Document({
    styles: { default: { document: { run: { font: FONT, size: SIZE } } } },
    footnotes: fnDefs,
    sections: [{
      properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, bottom: 1440, left: 1440, right: 1440 } } },
      footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: SIZE })] })] }) },
      children,
    }],
  });
  return Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(cfg.outPath, buf); console.log('Wrote', cfg.outPath, `(${Object.keys(footnotes).length} footnotes)`); });
}

if (require.main === module) { convert(JSON.parse(fs.readFileSync(process.argv[2], 'utf-8'))); }
module.exports = { convert, buildCaption, wrapTitle };
