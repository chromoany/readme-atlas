// Rebuild the English article illustrations from the same repository sources.
// Uses the existing Codex runtime; does not install packages.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';
import { spawnSync } from 'node:child_process';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.dirname(here);
const runtime = path.join(process.env.USERPROFILE, '.cache/codex-runtimes/codex-primary-runtime/dependencies');
const req = createRequire(path.join(runtime, 'node/node_modules/_article.cjs'));
const { chromium } = req('playwright');
const read = rel => fs.readFileSync(path.join(root, rel), 'utf8');
const esc = s => String(s).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const corpus = JSON.parse(read('research/sources.json'));
const selection = JSON.parse(read('research/selection.json'));
const groups = [
  ['web-frameworks', 'Web frameworks'], ['languages-build', 'Languages & build'],
  ['cli-shell', 'CLI & shell'], ['libraries-sdk', 'Libraries & SDKs'],
  ['data-storage', 'Data & storage'], ['infrastructure', 'Infrastructure'],
  ['quality-testing', 'Testing & QA'], ['creative-desktop', 'Creative & desktop'],
  ['developer-apps', 'Developer apps'], ['science-ml', 'Science & ML'],
  ['security-network', 'Security & network'], ['embedded-robotics', 'Embedded & robots'],
  ['docs-learning', 'Docs & learning'], ['content-domain', 'Content & domain'],
].map(([key, label]) => ({ label, count: corpus.sources.filter(s => s.study_group === key).length }));
const expanded = groups.reduce((sum, g) => sum + g.count, 0);
const foundational = corpus.sources.length - expanded;
if (corpus.sources.length !== 200 || foundational !== 32 || expanded !== 168 || groups.some(g => g.count !== 12)) {
  throw new Error('Research counts changed. Update article and illustrations together.');
}
const worked = read('examples/cli-rewrite.md');
const before = worked.match(/## Before\s+The deliberately flawed draft says:\s+> (.+)/)[1];
const fixture = read('examples/fixtures/log-slice/README.md');
const intro = fixture.match(/# Log Slice\s+(.+)/)[1];
const requirement = fixture.match(/Requires Python[^\r\n]+/)[0];
const cmd = fixture.match(/```bash\s+([\s\S]*?)```/)[1].trim();
const expected = fixture.match(/```text\s+([\s\S]*?)```/)[1].trim();
const args = ['examples/fixtures/log-slice/logslice.py', 'examples/fixtures/log-slice/sample.log', '--level', 'ERROR'];
const executed = spawnSync(path.join(runtime, 'python/python.exe'), args, { cwd: root, encoding: 'utf8' });
if (executed.status !== 0 || executed.stdout.trim() !== expected) throw new Error('Fixture output does not match its README');
fs.mkdirSync(path.join(here, 'assets'), { recursive: true });

const css = `
*{box-sizing:border-box}body{margin:0;color:#172b2b;font-family:"Segoe UI",system-ui,sans-serif;background:#fff}
.figure{width:1280px;padding:62px 68px 42px;background:#f5f3ed}.eyebrow{font-size:22px;letter-spacing:2px;color:#566661;margin-bottom:20px}.title{font-size:48px;line-height:1.35;font-weight:700;margin:0 0 22px}.sub{font-size:26px;line-height:1.6;color:#52625d}.foot{font-size:21px;color:#65716a;margin-top:32px;line-height:1.6;border-top:1px solid #d5dcd2;padding-top:22px}
.stat{display:flex;align-items:baseline;gap:24px;margin:24px 0 18px}.stat strong{font-family:"Segoe UI",sans-serif;font-size:122px;line-height:1.1;letter-spacing:-6px;color:#185a4b}.stat span{font-size:30px}.bar{display:flex;height:68px;margin-bottom:25px;color:white;font-size:24px;font-weight:600}.bar div{display:flex;align-items:center;justify-content:center;white-space:nowrap;padding:0 10px}.base{background:#6b8a75}.expand{background:#185a4b}.group-label{font-size:24px;font-weight:700;margin:24px 0 15px}.groups{display:grid;grid-template-columns:repeat(4,1fr);gap:0 24px}.group{border-top:1px solid #cdd6cc;font-size:25px;padding:15px 0;display:flex;justify-content:space-between;align-items:baseline;gap:8px}.group small{font-size:21px;color:#5b7063}.formats{display:flex;gap:24px;align-items:center;margin-top:24px;font-size:24px;color:#425a50}.formats b{font-weight:600;color:#185a4b}
.compare{display:grid;grid-template-columns:.9fr 1.1fr;gap:32px;margin-top:30px}.panel{padding:26px 28px;background:#fff;border-top:5px solid #185a4b;min-width:0}.panel.bad{border-color:#bd7657;background:#f7ece5}.label{font-size:25px;font-weight:700;margin-bottom:22px}.bad .label{color:#955238}.source{font-size:18px;color:#68766b;margin-bottom:18px;word-break:break-all}.quote{font-size:29px;line-height:1.65;font-family:"Segoe UI",sans-serif;margin:0}.annotation{font-size:25px;line-height:1.65;margin-top:28px;border-top:1px solid #d6c5bc;padding-top:20px;color:#75523e}.panel.good p{font-size:23px;line-height:1.55;margin:0 0 19px}.panel pre{font-size:21px;line-height:1.6;margin:14px 0 20px;white-space:pre-wrap;overflow-wrap:anywhere;padding:18px;background:#edf2ed;color:#234a40;font-family:Consolas,monospace}.smallcap{font-size:22px;color:#52625d;margin:12px 0}
.terminal{background:#122c2b;color:#edf4ed;padding:46px;margin-top:30px}.terminal .tlabel{color:#9dbcb3;font-size:23px;margin-bottom:28px}.terminal pre{font-family:Consolas,monospace;font-size:26px;line-height:1.9;white-space:pre-wrap;overflow-wrap:anywhere;margin:0}.terminal .output{color:#a5d9a9;margin-top:30px;padding-top:25px;border-top:1px solid #43635b}.run-note{margin-top:26px;font-size:25px;line-height:1.7;color:#425a50}
`;
const doc = body => `<!doctype html><html lang="en"><head><meta charset="utf-8"><style>${css}</style></head><body>${body}</body></html>`;
const formats = corpus.sources.reduce((acc, s) => {
  const ext = path.extname(s.path).toLowerCase();
  const fmt = ['.md', '.markdown'].includes(ext) ? 'Markdown' : ext === '.rst' ? 'RST' : ['.adoc', '.asc', '.asciidoc'].includes(ext) ? 'AsciiDoc' : 'Plain text';
  acc[fmt] = (acc[fmt] || 0) + 1;
  return acc;
}, {});
const figures = [
  ['01-corpus-en', `<main class="figure"><div class="eyebrow">README ATLAS / RESEARCH NOTES</div><h1 class="title">Where does a README start, project by project?</h1><div class="stat"><strong>${corpus.sources.length}</strong><span>READMEs studied</span></div><div class="bar"><div class="base" style="width:${foundational / corpus.sources.length * 100}%">Cases ${foundational}</div><div class="expand" style="flex:1">${expanded} structure studies · ${groups.length} groups × 12</div></div><div class="group-label">Collected by domain</div><div class="groups">${groups.map(g => `<div class="group"><span>${g.label}</span><small>${g.count}</small></div>`).join('')}</div><div class="formats">${Object.entries(formats).map(([f, n]) => `<span><b>${f}</b> ${n}</span>`).join('')}</div><div class="foot">Source: research/sources.json · research/selection.json<br>Selection threshold ≥ 1,000 stars, sampled ${selection.observed_date}. Stars are a sampling filter, not a quality score.</div></main>`],
  ['02-rewrite-en', `<main class="figure"><div class="eyebrow">README ATLAS / WORKED EXAMPLE</div><h1 class="title">Write the first run so it can be followed</h1><div class="sub">Manual rewrite inside the repository · Log Slice</div><div class="compare"><section class="panel bad"><div class="label">Draft</div><div class="source">examples/cli-rewrite.md · Before</div><p class="quote">${esc(before)}</p><div class="annotation">Ships an install command for a package that was never published.<br><br>"Fastest", "production-ready" and all-platform support: no evidence behind any of them.<br><br>No real arguments, and no result to recognise.</div></section><section class="panel good"><div class="label">Rewritten README (excerpt)</div><div class="source">examples/fixtures/log-slice/README.md</div><p>${esc(intro)}</p><p>${esc(requirement)}</p><div class="smallcap">Run from the README Atlas repository root</div><pre>${esc(cmd)}</pre><div class="smallcap">Expected output</div><pre>${esc(expected)}</pre><div class="smallcap">Matches only a line-initial level followed by a space.</div></section></div><div class="foot">Text quoted from the repository examples; a manual demonstration, not a measurement of generated output.</div></main>`],
  ['03-run-en', `<main class="figure"><div class="eyebrow">README ATLAS / LOCAL EXECUTION</div><h1 class="title">Run that command once</h1><div class="sub">Bundled script and sample file · local Windows / Python</div><div class="terminal"><div class="tlabel">COMMAND / from the README Atlas repository root</div><pre>python examples/fixtures/log-slice/logslice.py\n  examples/fixtures/log-slice/sample.log --level ERROR</pre><div class="tlabel output">STDOUT / actual output</div><pre>${esc(executed.stdout.trimEnd())}</pre></div><div class="run-note">The command is wrapped here for reading; run it as one line.<br>The sample holds one INFO, one WARN and one ERROR line; only one survives the filter.</div><div class="foot">Built from an actual run; exit code ${executed.status}. Raw record in assets/run-evidence.json.</div></main>`],
];

const browser = await chromium.launch({ headless: true, channel: 'chrome' });
try {
  const page = await browser.newPage({ viewport: { width: 1280, height: 1000 }, deviceScaleFactor: 1.5 });
  for (const [name, body] of figures) {
    await page.setContent(doc(body));
    await page.evaluate(() => document.fonts.ready);
    const overflow = await page.evaluate(() => Array.from(document.querySelectorAll('.figure,.panel,.group')).filter(el => el.scrollWidth > el.clientWidth + 1).map(el => el.className));
    if (overflow.length) throw new Error(name + ' overflow: ' + overflow.join(','));
    await page.locator('.figure').screenshot({ path: path.join(here, 'assets', name + '.png') });
    console.log('Rendered ' + name);
  }
} finally { await browser.close(); }
