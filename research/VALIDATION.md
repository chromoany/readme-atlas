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

## Header layout convention

The user's explicit layout requirements are now part of the skill entrypoint, visual guide, markup example, and review checklist: keep every badge in one visible header group, and center that group plus everything above it. These are README Atlas conventions, not additional findings from the open-source corpus.

- Skill Creator `quick_validate.py` passed for both the repository and global installation. The available Python runtimes lacked PyYAML, so validation loaded a cached PyYAML wheel in isolation without changing either runtime's installed packages.
- Markdown fences were balanced; 43 local link paths resolved after excluding illustrative fenced examples.
- Manual application review of the existing dsh-notify-me README confirmed all eight badges in the centered header, with its title, tagline, and language switch above them; search keywords remained visible in the body. This was a source inspection for this update, not a new browser or independent-agent evaluation.
- The six globally installed skill files were synchronized and checked byte-for-byte against normalized source; English and Chinese project descriptions now explain the convention.

## Learning-range expansion: 16 to 32 projects

The same client date's expansion retains the original sixteen manifest entries and adds sixteen independently pinned README files. The source study now contains thirty-two observation/transfer/limit records. Five additional source-only visual cases bring that reference to thirteen.

| Check | Result |
| --- | --- |
| `python tools/verify_sources.py` | 32/32 pinned files matched SHA-256 and byte counts, including RST and extensionless text |
| Baseline preservation | First 16 manifest entries exactly matched `HEAD:research/sources.json`; no original revision was refreshed |
| Corpus coverage | 32 unique repositories; 32 complete observation/transfer/limit records; 32 source-study citations exactly matched the manifest |
| Visual citations | All 13 pinned visual citations belonged to the corpus |
| Skill Creator `quick_validate.py` | Passed using Python UTF-8 mode and the existing isolated PyYAML wheel; no package installation |
| Markdown and portability | 12 Markdown files inspected; 43 local paths resolved with exact case; fences and reference-style links resolved; skill references stayed inside the portable skill folder |
| Whitespace | `git diff --check` passed |

Manual application review used the pinned source content to check concrete reader requests:

| Reader request | Review outcome reflected in the updated guidance |
| --- | --- |
| Make p-limit's first example independently runnable | Its application-defined helpers need implementations or an explicit illustrative-example label; API brevity alone is insufficient |
| Explain how to embed Kubernetes or Prometheus code | Respect their supported component/library boundaries rather than advertising arbitrary internal imports |
| Improve a Zephyr or Home Assistant README | Preserve RST syntax and direct hardware/user/component readers to the relevant maintained destinations |
| Make scientific installation clearer | Separate scikit-learn's core and plotting/example dependencies, and NumPy's post-install testing requirements |
| Improve 科技爱好者周刊's entry route | Preserve newest-edition and year/month navigation instead of adding a software-installation outline |

These were manual source-based review scenarios, not an independent agent evaluation or upstream runtime tests. No added visual case was audited in a rendered browser view; no upstream software, firmware, cluster, or exercise service was executed. This update changes the repository skill and research only; it does not synchronize the global skill installation. Existing untracked promotion material and the validator-wheel directory were preserved.

## Expansion to 200 with the 1,000-Star selection requirement

Date: **2026-10-16** (Asia/Hong_Kong client date). The original 32 source records were preserved exactly. Another 168 pinned README reviews were added in 14 domain groups of 12. All 200 final repositories received exact GitHub Star-count checks; `golang/website` (444) was excluded and replaced by `rust-lang/mdBook` (22,222). The final observed minimum was **1,512 Stars**.

| Check | Result |
| --- | --- |
| Source integrity | `python tools/verify_sources.py`: **200/200** pinned files matched SHA-256 and byte counts |
| Selection and identity | `python tools/audit_corpus.py`: 200 unique source identities and resolved repositories; all recorded counts met the 1,000-Star minimum |
| Study coverage | 200 complete observed/transfer/limit records and matching immutable citations across 15 study files; 13 visual-source citations remained within the corpus |
| Historical preservation | First 32 complete manifest entries exactly matched the pre-expansion snapshot, including their commits and hashes |
| Root indirection | Next.js, Zod, and Redux Toolkit pointers were followed within their pinned commits; manifests identify the entry and actual document paths |
| Format coverage | 177 Markdown, 17 RST, 3 AsciiDoc, and 3 extensionless text files |
| Skill validation | Skill Creator `quick_validate.py` passed using Python UTF-8 mode and the existing isolated PyYAML wheel |
| Links and markup | 26 Markdown files; 238 exact-case local paths and 172 local anchors resolved; fences and reference-style links passed |
| Portability | All 20 skill files copied to an isolated temporary directory with zero hash mismatches; corpus audit passed there |
| Audit boundary tests | Rejected 999 Stars, accepted exactly 1,000, rejected duplicate resolved repository aliases, and rejected a missing observation record |
| Whitespace | `git diff --check` passed |

The portability check exposed Windows short-path versus resolved-path comparisons in the new audit tool. Resolving the audit root once fixed the mismatch; the portable-copy and boundary cases then passed. These tests used isolated copies and did not modify the real corpus or install packages.

Manual application review checked the new decisions against actual pinned content: shell activation after installing Starship/zoxide/delta; specification navigation in Parquet; reading versus source-building in the Rust book and mdBook; application versus framework development in Selenium/Blender; preview versus publication status in RxJS; canonical or relocated repository destinations in Go/Zig; and journal-input/report-output continuity in hledger. The resulting guidance is in the skill entrypoint, patterns, and checklist.

The new 168 cases received focused README source-structure review, not exhaustive project-code review. No new upstream runtime, browser rendering, responsive/theme audit, or independent-agent evaluation was performed. The visual subset remains 13 cases. Star observations are dated selection evidence and do not measure README effectiveness. The updated repository skill has not been synchronized to the global installation; existing untracked files were preserved.
