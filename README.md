<div align="center">

<img src="assets/readme-atlas-header.png" alt="README Atlas: document panels connected by a path and compass" width="960">

# README Atlas

**Give every project a clear path from first glance to first use.**

[English](README.md) · [简体中文](README.zh-CN.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-35b6bd?style=flat-square)](LICENSE)
[![Codex agent skill](https://img.shields.io/badge/Codex-Agent%20Skill-35b6bd?style=flat-square)](skills/readme-atlas/SKILL.md)

</div>

An agent skill for **writing, improving, reviewing, and translating repository READMEs**. It combines repository evidence with a study of 200 projects to guide accurate content, clear first use, and coherent visual presentation.

[Install](#install-in-codex) · [First use](#first-use) · [See a rewrite](#see-a-rewrite) · [Research and limits](#what-we-learned)

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

Expect a project-specific `README.md` and a short delivery note describing what was checked and any unresolved facts. The agent inspects the repository before choosing content and headings.

<details>
<summary>More ways to use the skill</summary>

**Improve an existing README**

```text
Use $readme-atlas to improve our existing README. Keep useful anchors
and focus on making the first-run instructions complete.
```

**Review without editing**

```text
Use $readme-atlas to review README.md without editing it.
Prioritize issues that would prevent a new user from getting started.
```

**Polish the presentation**

```text
Use $readme-atlas to polish this README's visual presentation.
Improve the opening, badge consistency, previews, spacing, and navigation
while preserving accurate commands and the project's identity.
```

**Write in Chinese**

```text
使用 $readme-atlas，根据仓库实际内容编写中文 README。
保留真实命令，说明运行后应该看到什么，不要编造功能或性能数据。
```

</details>

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

This fixture is a manual illustration of the method, not an independent evaluation of the skill.

## What the skill does

| Your task | What README Atlas guides the agent to do |
| --- | --- |
| Create | Inspect the repository, identify the reader, and choose a useful first-use route |
| Improve | Preserve accurate content and useful anchors; fix gaps in explanation, commands, and presentation |
| Review | Report concrete findings with evidence and proposed fixes; keep files unchanged for a review-only request |
| Translate | Preserve commands, links, requirements, and feature status across language versions |

Visual guidance covers the opening, grouped badges, previews, spacing, navigation, and light/dark readability. Structure follows the project: a library needs an input/output example, a platform needs deployment choices, and a learning resource needs a starting route.

The skill consists of Markdown instructions, references loaded as needed, and Codex UI metadata. Installation and invocation are documented for **Codex**. Other agents can read the instructions, but their installation and invocation behavior has not been verified here.

## What we learned

README Atlas draws on **200 pinned README studies** across software and content repositories. Each case records an observation, a transferable writing decision, and a limit on applying it.

| Evidence | Coverage |
| --- | --- |
| README study | 32 detailed cases plus 168 focused source-structure reviews in 14 domain groups |
| Visual study | 13 cases covering branding, previews, typography, navigation, and related choices |
| Provenance | Immutable commit links, source paths, SHA-256 digests, and dated selection records |

The corpus spans libraries, CLIs, applications, infrastructure, scientific software, embedded systems, learning resources, and content archives. It includes Markdown, RST, AsciiDoc, and plain-text READMEs. Start with the [study index](skills/readme-atlas/references/source-study.md#study-index); the [research method](research/README.md) explains selection and review depth.

All 200 repositories had at least **1,000 GitHub Stars when checked on 2026-10-16**. This is a sample-selection rule, not a README quality score or a requirement for projects using the skill. See the [selection evidence](research/selection.json) and [source manifest](research/sources.json).

This is **qualitative editorial research**. It does not establish that a layout causes popularity or adoption. The 13 visual cases received different levels of source and rendered inspection; the corpus is not a uniform visual audit. No independent skill evaluation or conversion measurement has been performed. The [validation record](research/VALIDATION.md) separates executed checks, manual review, and unverified behavior.

## Explore and contribute

- [Reader journeys and adaptable outlines](skills/readme-atlas/references/patterns.md)
- [Visual design patterns and source observations](skills/readme-atlas/references/visual-design.md)
- [Review checklist](skills/readme-atlas/references/review-checklist.md)
- [Full worked example](examples/cli-rewrite.md)
- [Research method and source verification](research/README.md)
- [Corpus validation record](research/VALIDATION.md)
- [Contribution guide](CONTRIBUTING.md)

For a problem or proposed improvement, [open an issue](https://github.com/chromoany/readme-atlas/issues) with the affected file and a concrete example. Contributions should improve a real reader decision and keep the English and Chinese READMEs consistent.

## License

Created by [chromoany](https://github.com/chromoany).

[MIT](LICENSE) for this repository's original instructions, analysis, examples, and tooling. Referenced projects retain their own licenses. This repository links to their READMEs rather than redistributing them.
