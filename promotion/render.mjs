// Rebuild source-based article illustrations and a local reading preview.
// Uses the existing Codex runtime; does not install packages.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';
import { spawnSync } from 'node:child_process';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.dirname(here);
const runtime = path.join(process.env.USERPROFILE, '.cache/codex-runtimes/codex-primary-runtime/dependencies');
const req = createRequire(path.join(runtime, 'node/node_modules/_article.cjs'));
const { chromium } = req('playwright');
const { marked } = await import(pathToFileURL(req.resolve('marked')).href);
const read = rel => fs.readFileSync(path.join(root, rel), 'utf8');
const esc = s => String(s).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const corpus = JSON.parse(read('research/sources.json'));
const selection = JSON.parse(read('research/selection.json'));
const groups = [
  ['web-frameworks','Web 框架'], ['languages-build','语言与构建'],
  ['cli-shell','CLI 与 Shell'], ['libraries-sdk','库与 SDK'],
  ['data-storage','数据与存储'], ['infrastructure','基础设施'],
  ['quality-testing','测试与代码质量'], ['creative-desktop','创作软件'],
  ['developer-apps','开发者应用'], ['science-ml','科学计算与 ML'],
  ['security-network','安全与网络'], ['embedded-robotics','嵌入式与机器人'],
  ['docs-learning','文档与学习'], ['content-domain','内容与领域应用'],
].map(([key, label]) => ({label, count:corpus.sources.filter(s => s.study_group === key).length}));
const expanded = groups.reduce((sum,g) => sum+g.count,0);
const foundational = corpus.sources.length-expanded;
if (corpus.sources.length !== 200 || foundational !== 32 || expanded !== 168 || groups.some(g=>g.count!==12)) {
  throw new Error('Research counts changed. Update article and illustrations together.');
}
const worked = read('examples/cli-rewrite.md');
const before = worked.match(/## Before\s+The deliberately flawed draft says:\s+> (.+)/)[1];
const fixture = read('examples/fixtures/log-slice/README.md');
const intro = fixture.match(/# Log Slice\s+(.+)/)[1];
const requirement = fixture.match(/Requires Python[^\r\n]+/)[0];
const cmd = fixture.match(/```bash\s+([\s\S]*?)```/)[1].trim();
const expected = fixture.match(/```text\s+([\s\S]*?)```/)[1].trim();
const args = ['examples/fixtures/log-slice/logslice.py','examples/fixtures/log-slice/sample.log','--level','ERROR'];
const executed = spawnSync(path.join(runtime,'python/python.exe'),args,{cwd:root,encoding:'utf8'});
if (executed.status!==0 || executed.stdout.trim()!==expected) throw new Error('Fixture output does not match its README');
fs.mkdirSync(path.join(here,'assets'),{recursive:true});
fs.writeFileSync(path.join(here,'assets/run-evidence.json'),JSON.stringify({command:'python '+args.join(' '),stdout:executed.stdout,exitCode:executed.status},null,2)+'\n');

const css = `
*{box-sizing:border-box}body{margin:0;color:#172b2b;font-family:"Microsoft YaHei","Segoe UI",sans-serif;background:#fff}
.figure{width:1280px;padding:62px 68px 42px;background:#f5f3ed}.eyebrow{font-size:22px;letter-spacing:2px;color:#566661;margin-bottom:20px}.title{font-size:48px;line-height:1.35;font-weight:700;margin:0 0 22px}.sub{font-size:26px;line-height:1.6;color:#52625d}.foot{font-size:21px;color:#65716a;margin-top:32px;line-height:1.6;border-top:1px solid #d5dcd2;padding-top:22px}
.stat{display:flex;align-items:baseline;gap:24px;margin:24px 0 18px}.stat strong{font-family:"Segoe UI",sans-serif;font-size:122px;line-height:1.1;letter-spacing:-6px;color:#185a4b}.stat span{font-size:30px}.bar{display:flex;height:68px;margin-bottom:25px;color:white;font-size:24px;font-weight:600}.bar div{display:flex;align-items:center;justify-content:center}.base{background:#6b8a75}.expand{background:#185a4b}.group-label{font-size:24px;font-weight:700;margin:24px 0 15px}.groups{display:grid;grid-template-columns:repeat(4,1fr);gap:0 24px}.group{border-top:1px solid #cdd6cc;font-size:25px;padding:15px 0;display:flex;justify-content:space-between;align-items:baseline;gap:8px}.group small{font-size:21px;color:#5b7063}.formats{display:flex;gap:24px;align-items:center;margin-top:24px;font-size:24px;color:#425a50}.formats b{font-weight:600;color:#185a4b}
.compare{display:grid;grid-template-columns:.9fr 1.1fr;gap:32px;margin-top:30px}.panel{padding:26px 28px;background:#fff;border-top:5px solid #185a4b;min-width:0}.panel.bad{border-color:#bd7657;background:#f7ece5}.label{font-size:25px;font-weight:700;margin-bottom:22px}.bad .label{color:#955238}.source{font-size:18px;color:#68766b;margin-bottom:18px;word-break:break-all}.quote{font-size:29px;line-height:1.65;font-family:"Segoe UI",sans-serif;margin:0}.annotation{font-size:25px;line-height:1.65;margin-top:28px;border-top:1px solid #d6c5bc;padding-top:20px;color:#75523e}.panel.good p{font-size:23px;line-height:1.55;margin:0 0 19px}.panel pre{font-size:21px;line-height:1.6;margin:14px 0 20px;white-space:pre-wrap;overflow-wrap:anywhere;padding:18px;background:#edf2ed;color:#234a40;font-family:Consolas,monospace}.smallcap{font-size:22px;color:#52625d;margin:12px 0}
.terminal{background:#122c2b;color:#edf4ed;padding:46px;margin-top:30px}.terminal .tlabel{color:#9dbcb3;font-size:23px;margin-bottom:28px}.terminal pre{font-family:Consolas,"Microsoft YaHei",monospace;font-size:26px;line-height:1.9;white-space:pre-wrap;overflow-wrap:anywhere;margin:0}.terminal .output{color:#a5d9a9;margin-top:30px;padding-top:25px;border-top:1px solid #43635b}.run-note{margin-top:26px;font-size:25px;line-height:1.7;color:#425a50}
`;
const doc = body => `<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><style>${css}</style></head><body>${body}</body></html>`;
const formats = corpus.sources.reduce((acc,s) => {const ext=path.extname(s.path).toLowerCase();const fmt=['.md','.markdown'].includes(ext)?'Markdown':ext==='.rst'?'RST':['.adoc','.asc','.asciidoc'].includes(ext)?'AsciiDoc':'纯文本';acc[fmt]=(acc[fmt]||0)+1;return acc;},{});
const figures = [
  ['01-corpus', `<main class="figure"><div class="eyebrow">README ATLAS / RESEARCH NOTES</div><h1 class="title">不同的项目，README 从哪里开始？</h1><div class="stat"><strong>${corpus.sources.length}</strong><span>项 README 研究</span></div><div class="bar"><div class="base" style="width:${foundational/corpus.sources.length*100}%">详细案例 ${foundational}</div><div class="expand" style="flex:1">${expanded} 个结构研究 · ${groups.length} 组 × 12 项</div></div><div class="group-label">新增研究按领域整理</div><div class="groups">${groups.map(g=>`<div class="group"><span>${g.label}</span><small>${g.count}</small></div>`).join('')}</div><div class="formats">${Object.entries(formats).map(([f,n])=>`<span><b>${f}</b> ${n}</span>`).join('')}</div><div class="foot">来源：research/sources.json · research/selection.json<br>选样门槛 ≥ 1,000 Star，日期 ${selection.observed_date}。Star 用于筛选样本。</div></main>`],
  ['02-rewrite', `<main class="figure"><div class="eyebrow">README ATLAS / WORKED EXAMPLE</div><h1 class="title">把第一次使用，写到能照着做</h1><div class="sub">仓库内手工改写示例 · Log Slice</div><div class="compare"><section class="panel bad"><div class="label">示例草稿</div><div class="source">examples/cli-rewrite.md · Before</div><p class="quote">${esc(before)}</p><div class="annotation">没有发布包，却给出包安装命令。<br><br>“最快”“生产就绪”和全平台支持，都缺少依据。<br><br>缺少实际参数和运行结果。</div></section><section class="panel good"><div class="label">改写后的 README（节选）</div><div class="source">examples/fixtures/log-slice/README.md</div><p>${esc(intro)}</p><p>${esc(requirement)}</p><div class="smallcap">从 README Atlas 仓库根目录执行</div><pre>${esc(cmd)}</pre><div class="smallcap">预期输出</div><pre>${esc(expected)}</pre><div class="smallcap">只匹配行首的日志级别 + 空格。</div></section></div><div class="foot">文字摘自仓库示例文件；手工演示，不是自动生成效果的评测。</div></main>`],
  ['03-run', `<main class="figure"><div class="eyebrow">README ATLAS / LOCAL EXECUTION</div><h1 class="title">这条命令，实际跑一下</h1><div class="sub">仓库附带脚本与样例文件 · 本地 Windows / Python 环境</div><div class="terminal"><div class="tlabel">COMMAND / 从 README Atlas 仓库根目录执行</div><pre>python examples/fixtures/log-slice/logslice.py\n  examples/fixtures/log-slice/sample.log --level ERROR</pre><div class="tlabel output">STDOUT / 实际输出</div><pre>${esc(executed.stdout.trimEnd())}</pre></div><div class="run-note">上方命令为阅读而换行，实际按一行执行。<br>样例包含 INFO、WARN、ERROR 三行，筛选后留下这一行。</div><div class="foot">本图整理自实际运行记录；退出码 ${executed.status}。原始记录见 assets/run-evidence.json。</div></main>`]
];

const browser = await chromium.launch({headless:true,channel:'chrome'});
try {
  const page = await browser.newPage({viewport:{width:1280,height:1000},deviceScaleFactor:1.5});
  for(const [name,body] of figures){
    await page.setContent(doc(body));
    await page.evaluate(()=>document.fonts.ready);
    const overflow = await page.evaluate(()=>Array.from(document.querySelectorAll('.figure,.panel,.group')).filter(el=>el.scrollWidth>el.clientWidth+1).map(el=>el.className));
    if(overflow.length) throw new Error(name+' overflow: '+overflow.join(','));
    await page.locator('.figure').screenshot({path:path.join(here,'assets',name+'.png')});
    console.log('Rendered '+name);
  }
  const markdown=read('promotion/zhihu-article.md').replaceAll('](promotion/assets/','](assets/');
  const previewCSS=`*{box-sizing:border-box}body{margin:0;background:#f3f1eb;color:#252b29;font:18px/1.95 "Microsoft YaHei","Segoe UI",sans-serif}article{max-width:850px;padding:56px 66px 70px;margin:36px auto;background:#fff}h1{font-size:31px;line-height:1.55;margin:0 0 35px}h2{font-size:24px;margin:45px 0 22px;line-height:1.5}p{margin:20px 0}a{color:#17644e;text-underline-offset:4px}img{width:100%;height:auto;display:block;margin:28px 0 8px}p:has(>em:only-child){font-size:14px;line-height:1.8;color:#6a726e;margin-top:8px}pre{padding:22px;background:#f2f5f2;border-left:3px solid #2c6a53;font:14px/1.9 Consolas,monospace;white-space:pre-wrap;overflow-wrap:anywhere}code{font-family:Consolas,monospace}p code{font-size:.88em;background:#f0f4ef;padding:2px 4px}@media(max-width:650px){body{font-size:17px}article{margin:0;padding:28px 20px}h1{font-size:26px}h2{font-size:22px}pre{font-size:12px;padding:16px}}`;
  fs.writeFileSync(path.join(here,'preview.html'),`<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>README Atlas · 知乎文章预览</title><style>${previewCSS}</style></head><body><article>${marked.parse(markdown)}</article></body></html>`);
  for(const width of [1100,390]){
    await page.setViewportSize({width,height:900});
    await page.goto(pathToFileURL(path.join(here,'preview.html')).href);
    await page.evaluate(()=>document.fonts.ready);
    const check=await page.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth,images:Array.from(document.images).map(i=>({loaded:i.complete&&i.naturalWidth>0,width:i.naturalWidth}))}));
    if(check.overflow||check.images.some(i=>!i.loaded)) throw new Error('Preview validation failed: '+JSON.stringify(check));
    console.log('Preview '+width+'px: '+JSON.stringify(check));
  }
} finally {await browser.close();}
