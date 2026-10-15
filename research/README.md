# Research method

Study date: **2026-10-16**, using the client's Asia/Hong_Kong date.

We selected sixteen recognizable open-source projects across libraries, frameworks, command-line tools, runtimes, desktop applications, platforms, ML, curated lists, and learning resources. Selection was purposive, not a statistical ranking. The sample exposes different reader journeys, including short documentation gateways and READMEs that serve as the main learning resource.

For each repository, we resolved the selected branch to a commit and fetched the README at that immutable commit. [sources.json](sources.json) records the full commit, path, raw URL, SHA-256, byte and line counts, and Markdown ATX heading locations. Setext and HTML headings are not indexed; the heading index is navigation metadata, not the analysis. Mutable web views supported discovery; pinned files govern recorded observations.

We compared opening explanations, first-use routes, examples and results, installation choices, deeper docs, visuals, support, contribution, and license navigation. The [source study](../skills/readme-atlas/references/source-study.md) records original paraphrases and separates observations, recommendations, and transfer limits. Original texts were read in a temporary research cache and are not distributed here.

## Reproduce source verification

From the repository root, with Python 3.10+ and network access:

```bash
python tools/verify_sources.py
```

The tool downloads the sixteen pinned raw READMEs into memory and compares digests and byte counts with the manifest. It does not need GitHub credentials, execute examples, update the manifest, or save upstream files.

To extend the study, add a pinned observation and its scope and limits. To refresh an observation, resolve a new commit, inspect actual changes, and update the manifest and synthesis together. Downloading a newer file alone does not refresh the research.

## Limits

- Popularity does not establish that a README caused adoption; no conversion study was conducted.
- Project maturity, distribution, and audiences explain some structural differences.
- We studied editorial structure, not the correctness of every upstream command or marketing claim.
- Pinned README bytes are stable evidence; external images and sites can change independently.
- Skill decisions are our qualitative synthesis, not requirements endorsed by sampled maintainers.

GitHub rendering and links were checked against [GitHub's README documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes). Codex install paths were checked against [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).
