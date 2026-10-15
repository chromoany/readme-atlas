# Validation record

Date: **2026-10-16** (Asia/Hong_Kong client date).

## Initial version

| Check | Result |
| --- | --- |
| Skill Creator `quick_validate.py` | Passed: skill frontmatter, naming, and scaffold checks |
| `python tools/verify_sources.py` | 16/16 immutable README sources matched SHA-256 and byte counts |
| Markdown file checks | 32 local link paths resolved with exact case; code fences closed; no scaffold placeholders |
| Portable skill copy | All 5 files copied to an isolated temporary `.agents/skills/readme-atlas` directory; zero hash mismatches |
| CLI fixture smoke | ERROR filter printed exactly `ERROR database unavailable` |
| CLI fixture help | Documented file argument and required INFO/WARN/ERROR level were present |

The fixture was executed with the available local Python on Windows. The PowerShell folder-copy path was exercised in isolation, without installing into the user's active skill directory. Bash installation syntax was inspected but not executed on macOS or Linux.

The project's own READMEs were manually reviewed against the skill's reader-journey and fact-checking instructions. The worked example is author-produced. No independent agent evaluation or Codex skill-picker UI test was performed, and these checks do not measure README conversion or adoption.

## Visual-design expansion

The same day's follow-up makes visual presentation part of the main workflow and adds `references/visual-design.md`.

| Check | Result |
| --- | --- |
| Skill Creator `quick_validate.py` | Passed after the visual-design update |
| Visual-source identity | All 8 studied raw files matched the original manifest's SHA-256; all 8 pinned citations matched the corpus |
| Upstream rendered inspection | Vite, uv, and Supabase inspected in GitHub's desktop view with the existing dark appearance |
| Markdown and portability | 42 local paths resolved with exact case; fences and reference-style links resolved; runtime skill references remain inside the portable folder |
| Global skill update | Previous 5 files matched the earlier commit before replacement; all 6 updated files matched their source SHA-256 |

The visual reference includes author-created markup examples and identifies its recommendations as synthesis. The five other visual cases were inspected from pinned source. Narrow layouts, light appearance, and every upstream external image were not exhaustively audited; the skill now explicitly asks its users to check relevant rendered views and report unverified ones. No independent agent evaluation was conducted for this expansion.
