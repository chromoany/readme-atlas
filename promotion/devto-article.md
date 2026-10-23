# A README skill that deletes claims it cannot source

An agent writing a README usually gets the shape right and the facts wrong. The sections are all there — install, quickstart, configuration, license — but the install command points at a package that was never published, the config key is one the code does not read, and a feature still on the roadmap is described in present tense.

I built a skill that treats this as an evidence problem before it treats it as a writing problem.

## Evidence first, prose second

Before writing a sentence, the skill builds a fact map from the repository: package manifests, entry points, example scripts, tests, CI config, and any existing docs. The README is then written only from what that map supports.

When something cannot be sourced, the claim is removed rather than reworded. Rewording is how the invented install command survives a second draft — it gets vaguer, not truer. The skill also records what it could not verify, so an unreleased feature shows up as a limitation instead of a feature.

## The structure part came from 200 repositories

Removing bad claims does not tell you where to put the good ones, so I studied how real projects organize onboarding: 200 repositories, all with at least 1,000 stars, each pinned to a specific commit and logged with a link back to the source.

32 of them are full case studies — how the README is organized, what is worth copying, what breaks if you copy it. The other 168 are structure studies, grouped into 14 domains with 12 projects each: web frameworks, CLIs, editors, databases, embedded, and so on. React and Vite do not open the same way as Linux or Zephyr, and a weekly newsletter should not open like either.

In practice the skill reads the group that matches the project instead of applying a template. A desktop app gets a screenshot early. A CLI gets a command and its output. A script gets three lines and a code block.

![Study corpus: 32 case studies plus 14 groups of structural studies](https://raw.githubusercontent.com/chromoany/readme-atlas/main/promotion/assets/01-corpus.png)

## A deliberately small demo

The repository ships a tiny Python script that filters log lines, plus a README draft that gets the facts wrong on purpose: it calls itself the fastest, production-ready logging platform and tells you to run `pip install logslice`. There is no published package and no benchmark — only a local script.

![Before and after: invented package install and performance claims replaced with the real script usage](https://raw.githubusercontent.com/chromoany/readme-atlas/main/promotion/assets/02-rewrite.png)

The rewritten version says it is a local script, that it needs Python 3.10+, that nothing has to be installed. It gives the command and the expected output, and adds the caveat that the log level has to be at the start of the line.

![Running the example: filtering for ERROR prints the matching line](https://raw.githubusercontent.com/chromoany/readme-atlas/main/promotion/assets/03-run.png)

Small, but it is the exact failure people hit: copy a command, get an error, close the tab.

## Install

The skill is plain Markdown — instructions plus reference files loaded on demand. No runtime, no API key.

```bash
npx skills add chromoany/readme-atlas
```

That installs into the agents the skills CLI detects and links into Claude Code and Codex. You can also copy the `skills/readme-atlas` folder into an agent's skill directory.

Then ask for what you want:

```text
Use $readme-atlas to review README.md without editing files.
Find where a new user following it would get stuck, with evidence.
```

```text
Use $readme-atlas to rewrite the README in Chinese.
Every command and feature claim must be traceable to the repository.
```

## What it does not do

Three honest limits, since they are the parts I am least sure about.

The 200-repository study is about structure, not quality. It tells you whether a README's shape matches what readers of that kind of project expect, not whether the project is worth using.

"Delete the unsourced claim" is aggressive. For install commands and config keys I think it is right — a wrong command is worse than a missing one. For roadmap-ish claims, keeping the sentence and marking it unverified is often better. That split is a judgment call in the instructions, not something I measured.

And it is instructions, not a linter. There is no CI check that fails when a claim is unsourced; the agent has to actually look at the repository. That is slower than generating text, and it is the point.

Repo, MIT licensed: [chromoany/readme-atlas](https://github.com/chromoany/readme-atlas)

If you try it on a project, the useful feedback is where it still guessed — a command it wrote without checking, a section it placed by template rather than by reader.
