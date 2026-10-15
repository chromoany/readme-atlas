# Log Slice

A local Python script that prints log lines for one selected level. Use it to extract INFO, WARN, or ERROR lines from a text log.

## Try it

Requires Python 3.10+. The script uses the standard library; no package installation is needed.

From the README Atlas repository's root:

```bash
cd examples/fixtures/log-slice
python logslice.py sample.log --level ERROR
```

Expected output:

```text
ERROR database unavailable
```

The included [sample.log](sample.log) contains three lines. To filter your own UTF-8 log, replace `sample.log` with its path and choose `INFO`, `WARN`, or `ERROR`.

For argument help:

```bash
python logslice.py --help
```

## Matching behavior

Matching is case-sensitive and requires the level at the beginning of a line followed by a space. A timestamp-prefixed line such as `2026-10-16 ERROR failed` will not match `--level ERROR`.
