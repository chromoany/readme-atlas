# CLI and shell tools: README studies

Study date: **2026-10-16** (Asia/Hong_Kong client date). These twelve repositories passed the **1,000 GitHub Stars minimum** at selection. Star counts below are dated observations, not a quality score.

**Compare:** Shell activation, consequential defaults, integration, task-based examples.

This is a focused source-structure review of pinned READMEs. Observations, editorial transfers, and limits are separate; upstream commands and rendered layouts were not exercised in this pass.

| Repository | Stars at selection | README format |
| --- | ---: | --- |
| [sharkdp/bat](#sharkdpbat) | 60,798 | markdown |
| [sharkdp/fd](#sharkdpfd) | 44,758 | markdown |
| [sharkdp/hyperfine](#sharkdphyperfine) | 29,102 | markdown |
| [eza-community/eza](#eza-communityeza) | 23,570 | markdown |
| [ajeetdsouza/zoxide](#ajeetdsouzazoxide) | 40,126 | markdown |
| [starship/starship](#starshipstarship) | 60,282 | markdown |
| [nushell/nushell](#nushellnushell) | 40,670 | markdown |
| [fish-shell/fish-shell](#fish-shellfish-shell) | 34,297 | restructuredtext |
| [tmux/tmux](#tmuxtmux) | 49,852 | text |
| [jesseduffield/lazygit](#jesseduffieldlazygit) | 83,217 | markdown |
| [dandavison/delta](#dandavisondelta) | 32,507 | markdown |
| [jqlang/jq](#jqlangjq) | 35,831 | markdown |

## sharkdp/bat

[Pinned README](https://github.com/sharkdp/bat/blob/62b439dae330a8c4d053ff7d8526a6e3697000b9/README.md)

- **Observed:** Feature demonstrations lead into usage and integrations with search, diff, and paging tools; language links are near the opening.
- **Transfer:** Explain a terminal tool's role in existing workflows, then show concrete integrations.
- **Limit:** A screenshot or syntax-highlighting example does not establish every terminal or file encoding behaves identically.

## sharkdp/fd

[Pinned README](https://github.com/sharkdp/fd/blob/14dcd92fb76ca0ebc2e82671a275f67c790d25fc/README.md)

- **Observed:** Task headings cover simple searches, roots, extensions, hidden files, ignored files, and command execution.
- **Transfer:** Explain defaults that affect which results users see beside the corresponding recipe.
- **Limit:** An empty search result can reflect filtering defaults; do not present the tool as searching every file unconditionally.

## sharkdp/hyperfine

[Pinned README](https://github.com/sharkdp/hyperfine/blob/c5161524980522320c7d3425e714cc0965a869a5/README.md)

- **Observed:** Benchmark examples expand into warmups, preparation, parameterization, shells, metrics, and result exports.
- **Transfer:** Separate the measured command from preparation and identify the benchmark's execution context.
- **Limit:** Upstream example measurements are not performance evidence for a different project or machine.

## eza-community/eza

[Pinned README](https://github.com/eza-community/eza/blob/471bfbc7b03cbac8c738e8d9050edb06ee79132a/README.md)

- **Observed:** The page distinguishes features from its predecessor, installation, display/filter options, themes, and contributor work.
- **Transfer:** For a successor tool, explain migration-relevant differences and keep optional presentation settings discoverable.
- **Limit:** A feature comparison is a scoped editorial claim; it does not prove drop-in equivalence in every script.

## ajeetdsouza/zoxide

[Pinned README](https://github.com/ajeetdsouza/zoxide/blob/86b443cffcd74d8dce0570792f1647491ffe5974/README.md)

- **Observed:** A smarter-directory-navigation explanation precedes usage, a multi-step installation route, configuration, and integrations.
- **Transfer:** Treat shell initialization as part of onboarding when installing the binary alone is insufficient.
- **Limit:** Interactive completion and integration choices are shell-dependent; one setup should not be labeled universal.

## starship/starship

[Pinned README](https://github.com/starship/starship/blob/91086e827b7ca977aeae54deaceb4d0724e023f6/README.md)

- **Observed:** Installation explicitly separates font prerequisites, obtaining the binary, shell setup, and configuration.
- **Transfer:** Make appearance prerequisites and shell activation part of the first-use route.
- **Limit:** A working executable does not prove the prompt is activated or its glyphs display correctly.

## nushell/nushell

[Pinned README](https://github.com/nushell/nushell/blob/818d4ac0644a03e857062b024c136c5d27ba0ea5/README.md)

- **Observed:** Installation and configuration precede a pipeline philosophy illustrated with structured output; platform support has a dedicated policy link.
- **Transfer:** Use a small example to expose the shell's data model and route support decisions to maintained policy.
- **Limit:** A structured-data shell example should not be presented as interchangeable with POSIX shell syntax.

## fish-shell/fish-shell

[Pinned README](https://github.com/fish-shell/fish-shell/blob/a41603b00224806e230a21c97921991c1c5a586f/README.rst)

- **Observed:** The RST page distinguishes quick start, platform packages, source builds, running the shell, dependencies, and build options.
- **Transfer:** Keep package use and contributor compilation separate while preserving native RST navigation.
- **Limit:** Platform requirements in the pinned file are historical observations, not current compatibility guarantees.

## tmux/tmux

[Pinned README](https://github.com/tmux/tmux/blob/ad98500ab6b893a3a8b47a08216915e415997780/README)

- **Observed:** A plain-text explanation of detach/reattach behavior leads to dependencies, release-tarball builds, and development-source guidance.
- **Transfer:** A concise text README can explain the central interaction and distinguish source distributions.
- **Limit:** Building a terminal multiplexer is not the same task as learning its session commands; link appropriate user help.

## jesseduffield/lazygit

[Pinned README](https://github.com/jesseduffield/lazygit/blob/4c2ce238a925c41b6caee6dcf722984ff081774b/README.md)

- **Observed:** An elevator pitch and long index organize feature demonstrations such as staging, rebase, bisect, and worktrees.
- **Transfer:** For an interactive developer application, group demonstrations by user action rather than internal modules.
- **Limit:** Demonstrating an operation does not authorize a reviewer to perform it on a reader's working tree.

## dandavison/delta

[Pinned README](https://github.com/dandavison/delta/blob/3c2269c6b845913965575f11b0196d70ef5352f3/README.md)

- **Observed:** Getting started distinguishes the git-delta package name from the delta executable and supplies Git configuration before feature previews.
- **Transfer:** State distribution and executable names explicitly and show the integration step needed to see the result.
- **Limit:** Editing global Git configuration is a real configuration change, not a consequence-free rendering check.

## jqlang/jq

[Pinned README](https://github.com/jqlang/jq/blob/6b53f8031161db96387b64b5f412845cd23491f6/README.md)

- **Observed:** Documentation and an online playground precede binaries, Docker, and source builds; git and release-tarball builds differ.
- **Transfer:** Separate trying a tool from building it, and preserve distribution-specific prerequisites.
- **Limit:** A source recipe should not inherit unnecessary bootstrap steps from another distribution route.
