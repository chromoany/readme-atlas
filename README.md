# README Atlas

**Give every project a clear path from first glance to first use.**

A reusable agent skill for writing, improving, and reviewing repository READMEs, covering both onboarding and visual presentation. It turns observations from **200 widely recognized software and content projects**, each with **at least 1,000 GitHub Stars** at selection, into project-specific writing decisions: a library needs an input/output example, a platform needs deployment choices, and a learning resource needs a starting route. Its visual guide covers identity, layout, badges, previews, and light/dark readability.

[简体中文](README.zh-CN.md) · [Skill instructions](skills/readme-atlas/SKILL.md) · [Source study](skills/readme-atlas/references/source-study.md)

## See a rewrite

A manual worked example using this repository's author-created Log Slice fixture.

**Before — deliberately flawed draft:**

> Install the published package with `pip install logslice`, then run `logslice`.

**After — local script, Python 3.10+:**

From this repository's root:

```bash
cd examples/fixtures/log-slice
python logslice.py sample.log --level ERROR
```

Expected output:

```text
ERROR database unavailable
```

The rewrite replaces an unsupported package install with the actual command, required input, and a recognizable result. [Read the full worked example](examples/cli-rewrite.md).

## Install in Codex

Clone this repository, then copy the **complete** `skills/readme-atlas` folder into your user skill directory. Git is needed for cloning; no Python package, API key, or runtime dependency is needed to use the skill. If that skill directory already exists, review it before replacing it.

**macOS / Linux (Bash):**

```bash
git clone https://github.com/chromoany/readme-atlas.git
cd readme-atlas
mkdir -p "$HOME/.agents/skills"
cp -R skills/readme-atlas "$HOME/.agents/skills/"
```

**Windows (PowerShell):**

```powershell
git clone https://github.com/chromoany/readme-atlas.git
Set-Location readme-atlas
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse .\skills\readme-atlas "$HOME\.agents\skills\"
```

For a repository-scoped installation, copy the folder to that project's `.agents/skills/readme-atlas` instead. These are [Codex's documented skill locations](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills). If the skill does not appear, restart Codex.

## First use

Open the project whose README you want to work on in Codex and send:

```text
Use $readme-atlas to inspect this repository and write README.md.
Target readers: developers trying the project for the first time.
Use repository evidence for every command and feature claim.
```

The expected artifact is a project-specific `README.md`, plus a short note describing what was checked and any unresolved facts. The skill asks the agent to inspect the repository before writing; it does not generate a fixed set of headings.

Other requests:

```text
Use $readme-atlas to improve our existing README. Keep useful anchors
and focus on making the first-run instructions complete.
```

```text
Use $readme-atlas to review README.md without editing it.
Prioritize issues that would prevent a new user from getting started.
```

```text
Use $readme-atlas to polish this README's visual presentation.
Improve the opening, badge consistency, previews, spacing, and navigation
while preserving accurate commands and the project's identity.
```

```text
使用 $readme-atlas，根据仓库实际内容编写中文 README。
保留真实命令，说明运行后应该看到什么，不要编造功能或性能数据。
```

## What the skill does

| Decision | How README Atlas approaches it |
| --- | --- |
| What to say | Inspect manifests, interfaces, examples, tests, docs, and licensing |
| What to show first | Choose the intended reader's smallest useful result |
| How to organize it | Adapt to libraries, CLIs, applications, platforms, systems/embedded software, scientific environments, ML, resources, archives, specifications and interchange formats, or skills |
| How it should look | Choose a coherent visual direction; compose the opening, badges, media, and reading rhythm |
| What to leave out | Remove unsupported claims and sections with no reader purpose |
| How to verify it | Trace commands, check links, run an appropriate smoke path, and inspect rendering when practical |

The skill is instruction-only, with optional references loaded as needed. Codex UI metadata is included. Other agents can read the Markdown instructions, but their installation and invocation behavior has not been verified here.

For READMEs with badges, its layout convention keeps all badges in one visible header group and centers that group plus everything above it (title, logo, tagline, and language links). The following body stays left-aligned; download and community badges stay in the same group.

## What we learned

The original sample includes React, Vue, Vite, FastAPI, uv, GitHub CLI, Deno, Ollama, Supabase, RustDesk, PyTorch, Transformers, ripgrep, fzf, Awesome, and System Design Primer.

The first expansion added Linux, PostgreSQL, Kubernetes, OpenTofu, Ansible, Prometheus, p-limit, Neovim, Godot, NumPy, scikit-learn, JupyterLab, Zephyr, Home Assistant, OWASP Juice Shop, and the Chinese 科技爱好者周刊 archive.

The **200-project corpus** retains those 32 pinned cases and adds 168 focused source-structure studies in 14 groups: web frameworks, languages/build systems, CLI/shell tools, established library ecosystems, data/storage, infrastructure, testing/quality, creative software, developer applications, scientific/ML software, security/networking, embedded/robotics, documentation/learning, and content/domain applications. Examples include Django, Rust, CPython, Axios, DuckDB, Blender, VS Code, OpenSSL, FreeRTOS, and mdBook. The [study index](skills/readme-atlas/references/source-study.md#study-index) routes to the relevant group.

All 200 repositories passed the Star threshold when checked on **2026-10-16**; the observed minimum was **1,512**. [Selection evidence](research/selection.json) records exact counts, dates, and resolved repository URLs. This is a sample of recognized projects, not a ranking of README quality. It now covers Markdown, RST, AsciiDoc, and text, including package README pointers and repository migration notices.

Our synthesis is to organize around the reader's next decision, preserve one complete first-use route where appropriate, and keep every promise tied to evidence. Short documentation gateways and long learning resources can both work; their audiences need different things.

We also studied the visual choices in thirteen of these projects: the original eight cases cover branding, charts, previews, typography, terminal presentation, collapsible examples, and navigation. Five added cases examine Prometheus's architecture image, Godot's editor preview, Home Assistant's RST images, Zephyr's format-specific artwork, and OpenTofu's theme and callout markup. The [visual guide](skills/readme-atlas/references/visual-design.md) separates source observations from rendered checks and explains which tradeoffs to assess.

Read the [per-project observations and transfer limits](skills/readme-atlas/references/source-study.md). Every sampled README is linked at a pinned commit, with retrieval metadata and a SHA-256 digest in [the research manifest](research/sources.json). This is a qualitative sample, not evidence that a layout causes popularity or adoption.

## Explore and contribute

- [Reader journeys and adaptable outlines](skills/readme-atlas/references/patterns.md)
- [Visual design patterns and source observations](skills/readme-atlas/references/visual-design.md)
- [Review checklist](skills/readme-atlas/references/review-checklist.md)
- [Worked example](examples/cli-rewrite.md)
- [Research method and source verification](research/README.md)
- [Corpus validation record](research/VALIDATION.md)
- [Contribution guide](CONTRIBUTING.md)

For a problem or proposed improvement, [open an issue](https://github.com/chromoany/readme-atlas/issues) with the affected file and a concrete example.

## License

[MIT](LICENSE) for this repository's original instructions, analysis, examples, and tooling. Referenced projects retain their own licenses. This repository links to their READMEs rather than redistributing them.
