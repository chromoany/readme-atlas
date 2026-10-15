# Contributing

Useful contributions improve a real reader decision: selecting an installation path, recognizing success, separating user setup from contributor setup, or removing an unsupported promise.

For instruction changes, include a concrete README request, relevant project facts, and the behavior the revised skill should produce. Prefer small evidence-based corrections to universal rules for one unusual repository.

For research, link the project's own README at an immutable commit. Record repository, path, commit, SHA-256 of raw bytes, and study date in `research/sources.json`. Add an original observation, applicable writing decision, and inference limit in the source study. Do not copy upstream READMEs, logos, or screenshots here.

Keep the English and Chinese project READMEs consistent. Keep runtime skill references within `skills/readme-atlas` so copying that folder remains sufficient.

From the repository root, verify source integrity:

```bash
python tools/verify_sources.py
```

This optional maintainer tool requires Python 3.10+ and network access, with no third-party packages. It checks source digests, not skill quality. For instruction changes, also inspect links and exercise a realistic README task; distinguish manual review from an independent agent evaluation.
