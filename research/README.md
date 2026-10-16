# Research method

Study date: **2026-10-16**, using the client's Asia/Hong_Kong date.

## Selection: 200 recognized projects

The corpus contains **200 software and content repositories**, all with **at least 1,000 GitHub Stars** when selected. We prefer mature, widely recognized projects with meaningful domain or ecosystem roles. The observed minimum was **1,512 Stars**. This is purposive sampling across reader decisions, not a statistical ranking or evidence that a README caused adoption.

[selection.json](selection.json) records the exact count, observation date, and resolved repository URL for every sample. Counts were read from the public GitHub repository page's `stargazerCount` data, rather than rounded badge text. Resolved URLs are checked for duplicates so a repository and its historical alias are not counted twice. These are dated observations; the offline audit does not claim today's counts are unchanged.

One candidate, `golang/website`, had **444 Stars** and was excluded; `rust-lang/mdBook`, observed at **22,222 Stars**, replaced it. The exclusion is retained in the selection record. Five narrow utility candidates were also replaced by established library ecosystems before finalizing the set: Axios, TanStack Query, Redux Toolkit, RxJS, and tRPC.

The original **32 immutable source entries remain unchanged**. The additional **168 projects** are organized into **14 groups of 12**: web frameworks; languages/build systems; CLI/shell tools; established libraries/SDK ecosystems; data/storage; infrastructure; testing/quality; creative/desktop software; developer applications; science/ML; security/networking; embedded/robotics; documentation/learning; and content/domain applications. The [study index](../skills/readme-atlas/references/source-study.md#study-index) provides the complete navigable inventory.

During the earlier 16-to-32 expansion, Terraform was considered but excluded because its [inspected README](https://github.com/hashicorp/terraform/blob/9ec49e06a868cfa161213fac7f74aa03f8937755/README.md#license) links Business Source License 1.1; OpenTofu supplies that infrastructure-as-code case. Content repositories have their own reuse terms; studying a public README does not assert that every linked book, asset, service, or dataset has a software-style license.

## Source identity and formats

For each repository we resolved a default/selected branch to a commit, using Git remote references, GitHub repository metadata, or the repository page's commit identity, then fetched the README at that immutable commit. [sources.json](sources.json) records repository, branch context, full commit, path, raw URL, SHA-256, byte and line counts, and navigation heading metadata. New records also identify their study group/file, source format, and study date.

The corpus contains **177 Markdown**, **17 RST**, **3 AsciiDoc**, and **3 extensionless text** READMEs. Source integrity is byte-based and does not depend on Markdown parsing. New Markdown heading metadata excludes fenced code; the original 32 records are preserved. Setext, HTML, RST, AsciiDoc, and text headings are not exhaustively indexed. The heading index is a navigation aid, not the analysis or a quality score.

For Next.js, Zod, and Redux Toolkit, the apparent root or `.github` README is a symlink/path pointer. We followed the pointer within the same pinned commit and recorded `entry_readme_path` alongside the actual studied file. The main source digest describes the actual document, not its one-line pointer. Zig is intentionally a migration-notice case: its pinned GitHub README links the new upstream and says it is not mirrored; it is not counted as a compiler-usage tutorial.

## Observation depth and synthesis

The original **32 detailed cases** remain in the [source study](../skills/readme-atlas/references/source-study.md). The new **168 focused structural reviews** examine opening explanations, navigation, adoption versus contributor routes, examples/results, requirements, release or migration status, and other project-specific decisions. They are separated into domain references so an ordinary skill invocation need not load all 200 cases.

Every project has an original **observed → transfer → limit** record and an immutable README citation. Editorial transfers are our interpretation, not rules endorsed by the sampled maintainers. Primary source text was read in temporary caches; upstream READMEs, logos, and screenshots are not redistributed in this repository. The skill's reader routes, patterns, and review checklist incorporate the recurring findings rather than merely adding repository names.

The [visual-design reference](../skills/readme-atlas/references/visual-design.md) remains a deeper subset of **13 cases**. In earlier work, Vite, uv, and Supabase were inspected in GitHub's rendered desktop dark appearance; the other visual observations were source-based. The 200-project expansion did not add a browser/theme/device audit. It does not imply that all 200 projects received the same depth of visual inspection.

## Reproduce verification

From the repository root, with Python 3.10+:

```bash
python tools/audit_corpus.py
python tools/verify_sources.py
```

`audit_corpus.py` runs offline. It checks target count, unique source and resolved-repository identities, matching selection inventories, the recorded Star threshold, immutable URL identities, portable study paths, and complete per-project observation/citation coverage. It does not refresh popularity or download upstream files.

`verify_sources.py` requires network access. It downloads the **200 pinned files** into memory and checks SHA-256 and byte counts. It does not need credentials or third-party packages, execute examples, update either manifest, or save upstream files. Matching digests proves source integrity, not command correctness or README effectiveness.

[VALIDATION.md](VALIDATION.md) records the checks and results of each corpus expansion.

To extend the study, apply the selection threshold, inspect the actual pinned document, add its original observation and limits to the relevant group, and update both inventories. To refresh an observation, inspect source changes and revise the synthesis together. Fetching a newer file or Star count alone does not refresh the editorial study.

## Limits

- Stars are a popularity filter, not a causal measure of onboarding, aesthetics, conversion, or quality.
- This intentionally favors recognized projects; it does not represent all open source or every language community.
- The review concerns editorial structure, not every upstream command, marketing claim, or compatibility combination.
- Version, lifecycle, and support details are observations of pinned documents, not present-day guarantees.
- External images, linked websites, downloads, and service terms can change independently of pinned README bytes.
- No added source's software, firmware, cluster, hosted exercise, paid API, or credential-validation workflow was executed.
- Native formats and Chinese learning/community projects broaden the sample without establishing exhaustive format or multilingual coverage.

Earlier renderer and installation guidance was checked against [GitHub's README documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) and [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills). Those earlier checks are not a new product-documentation refresh in this expansion.
