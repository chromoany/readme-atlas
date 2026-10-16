# Contributing

Useful contributions improve a real reader decision: selecting an installation path, recognizing success, separating user setup from contributor setup, or removing an unsupported promise.

For instruction changes, include a concrete README request, relevant project facts, and the behavior the revised skill should produce. Prefer small evidence-based corrections to universal rules for one unusual repository.

For research, link the project's own README at an immutable commit. Record repository, path, commit, SHA-256 of raw bytes, and study date in `research/sources.json`. Add an original observation, applicable writing decision, and inference limit in the source study. Do not copy upstream READMEs, logos, or screenshots here.

Select mature, widely recognized projects with **at least 1,000 GitHub Stars**. Record an exact count, observation date, and resolved repository URL in `research/selection.json`; do not count repository aliases twice. Stars determine sample eligibility, not README quality. Put focused observations in the relevant `references/studies/` group and link new groups from the study index. Follow README pointers to their pinned targets rather than studying a symlink path as though it were prose.

Keep the English and Chinese project READMEs consistent. Keep runtime skill references within `skills/readme-atlas` so copying that folder remains sufficient.

From the repository root, verify source integrity:

```bash
python tools/verify_sources.py
python tools/audit_corpus.py
```

Source verification requires Python 3.10+ and network access, with no third-party packages. The corpus audit runs offline and checks selection joins, the Star threshold, source identity, and complete study coverage; it does not refresh Star counts. These tools check provenance, not skill quality. For instruction changes, also inspect links and exercise a realistic README task; distinguish manual review from an independent agent evaluation.
