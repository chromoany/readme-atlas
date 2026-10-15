# Worked example: a local CLI README

This is a small author-created fixture, not an upstream project's code. It illustrates a README Atlas rewrite and is a manual worked example, not an independent agent evaluation.

## Request and repository evidence

Request: improve a Python log-filtering script's README for first-time users. Keep the project local; do not create package publication or performance claims.

Evidence:

- [logslice.py](fixtures/log-slice/logslice.py) accepts a file and a required level, then prints lines beginning with that level followed by a space. It uses only Python's standard library.
- [sample.log](fixtures/log-slice/sample.log) supplies one INFO, one ERROR, and one WARN line.
- The fixture's stated runtime requirement is Python 3.10+. There is no published package, hosted service, benchmark, release binary, or project-specific license file in the fixture.

## Before

The deliberately flawed draft says:

> Log Slice is the fastest, production-ready log platform. Install the published package with `pip install logslice`, then run `logslice`. Works on every operating system.

This invents package publication, an executable, performance evidence, maturity, and universal platform support. It omits the required file, level, and recognizable result.

## After

The [rewritten README](fixtures/log-slice/README.md) uses the CLI journey: a specific explanation, a local execution path, supplied input, exact output, and a precise matching limitation. It avoids an unsupported install command and keeps contributor or production sections out of a tiny local script's first-use path.

## Review findings

| Impact | Evidence | Fix |
| --- | --- | --- |
| Blocking | No package metadata or publication evidence; executable is a Python file | Invoke the actual script from its directory |
| Blocking | Argument parser requires a file and `--level` | Supply the sample path and level |
| Significant | Draft does not show how to recognize success | Show the single expected ERROR line |
| Significant | No benchmark, maturity statement, or platform matrix | Remove the unsupported claims |

## Reproduce the smoke check

From this repository's root:

```bash
python examples/fixtures/log-slice/logslice.py examples/fixtures/log-slice/sample.log --level ERROR
```

Expected output:

```text
ERROR database unavailable
```

This checks the fixture example's behavior on the current environment. It does not establish all-platform support or independently measure skill quality.

Two further manual review cases help inspect the instructions: a review-only request should return findings without editing; a curated-list request should choose navigation instead of inventing an install step. They are suggested evaluation cases, not reported test results.
