# README Atlas

An agent skill for writing, improving, reviewing, and translating repository READMEs.

The skill works from repository evidence: manifests, entry points, examples, CI configuration, and existing documentation are read before any prose is written. Every command, feature claim, and environment requirement in the resulting README has to be traceable to a file in the repository. When the evidence is missing, the claim is removed instead of being reworded, which is the failure mode readers complain about most in generated READMEs.

Guidance is distilled from a study of 200 open-source projects, recorded in `references/` with the source list in `research/sources.json`. The corpus is treated as evidence of editorial choices, not as a template to copy.

## Install as a plugin

```text
/plugin marketplace add chromoany/readme-atlas
/plugin install readme-atlas@readme-atlas
```

## Install as a skill

```bash
npx skills add chromoany/readme-atlas
```

The skill is instruction-only: Markdown instructions, references loaded as needed, and optional agent metadata. It has no runtime, network access, or API key requirement.

## License

MIT. See [LICENSE](LICENSE).
