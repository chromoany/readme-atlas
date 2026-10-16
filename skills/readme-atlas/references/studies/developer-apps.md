# Editors, terminals, and developer applications: README studies

Study date: **2026-10-16** (Asia/Hong_Kong client date). These twelve repositories passed the **1,000 GitHub Stars minimum** at selection. Star counts below are dated observations, not a quality score.

**Compare:** Source versus branded distribution, configuration, extension and migration routes.

This is a focused source-structure review of pinned READMEs. Observations, editorial transfers, and limits are separate; upstream commands and rendered layouts were not exercised in this pass.

| Repository | Stars at selection | README format |
| --- | ---: | --- |
| [microsoft/vscode](#microsoftvscode) | 193,679 | markdown |
| [zed-industries/zed](#zed-industrieszed) | 91,789 | markdown |
| [helix-editor/helix](#helix-editorhelix) | 46,608 | markdown |
| [lapce/lapce](#lapcelapce) | 38,921 | markdown |
| [wezterm/wezterm](#weztermwezterm) | 29,241 | markdown |
| [alacritty/alacritty](#alacrittyalacritty) | 65,975 | markdown |
| [kovidgoyal/kitty](#kovidgoyalkitty) | 35,298 | asciidoc |
| [git/git](#gitgit) | 63,816 | markdown |
| [git-lfs/git-lfs](#git-lfsgit-lfs) | 14,547 | markdown |
| [go-gitea/gitea](#go-giteagitea) | 58,528 | markdown |
| [laurent22/joplin](#laurent22joplin) | 56,752 | markdown |
| [logseq/logseq](#logseqlogseq) | 45,248 | markdown |

## microsoft/vscode

[Pinned README](https://github.com/microsoft/vscode/blob/5c1cfa69632b837d5b0629e95507156b31cb0423/README.md)

- **Observed:** The page distinguishes the Code - OSS repository from the Visual Studio Code product, then links downloads, contribution, bundled extensions, and dev containers.
- **Transfer:** Separate source identity from branded distribution and clarify extension versus core development.
- **Limit:** An open-source repository license does not automatically describe every distributed product or bundled service.

## zed-industries/zed

[Pinned README](https://github.com/zed-industries/zed/blob/28d0a3547f16b9609b301b48ab363bfca649c864/README.md)

- **Observed:** User installation is followed by platform-specific development links, contribution, and a dedicated licensing section.
- **Transfer:** Make normal downloads and source development independent routes and preserve license distinctions.
- **Limit:** Do not flatten a project's component-specific licensing into an unsupported single claim.

## helix-editor/helix

[Pinned README](https://github.com/helix-editor/helix/blob/ba40e547426b0f9896c8bdc699a4ab11f2b37dbc/README.md)

- **Observed:** The opening explains editor influences and the editing model; features include a scoped language-indentation note before installation/help.
- **Transfer:** Explain interaction differences and qualify language support near the relevant capability.
- **Limit:** Inspiration from another editor does not establish configuration or keybinding compatibility.

## lapce/lapce

[Pinned README](https://github.com/lapce/lapce/blob/f66ffaa95387794205c35864517de70958b9ea8d/README.md)

- **Observed:** Implementation context leads to LSP, modal editing, remote development, plugins, installation, and feedback destinations.
- **Transfer:** Describe user-facing capabilities separately from the technology used to implement them.
- **Limit:** Implementation choices are not evidence of speed or remote-environment compatibility.

## wezterm/wezterm

[Pinned README](https://github.com/wezterm/wezterm/blob/e2a98e1b8af156988ad0ac778658ac27b60a55fb/README.md)

- **Observed:** A concise gateway includes user docs, a captioned screenshot, installation, help, and sponsorship.
- **Transfer:** A small README can combine one meaningful preview with direct user routes.
- **Limit:** A screenshot of one OS does not validate appearance or features on every supported platform.

## alacritty/alacritty

[Pinned README](https://github.com/alacritty/alacritty/blob/29dc55375da817d53540f4caefbe708703c57b07/README.md)

- **Observed:** About/features lead to installation, requirements, configuration, and FAQs.
- **Transfer:** Place terminal/backend requirements near setup and give configuration an explicit destination.
- **Limit:** A sensible-defaults claim does not establish that every user's shell, font, or window system works unchanged.

## kovidgoyal/kitty

[Pinned README](https://github.com/kovidgoyal/kitty/blob/8e99fba8ecfc86501f6851d88fe5a79827240dfd/README.asciidoc)

- **Observed:** The concise AsciiDoc page links the website, FAQ, usage discussions, and package availability.
- **Transfer:** Preserve a compact native-format gateway when the maintained website owns detailed onboarding.
- **Limit:** A package-status badge is not validation of behavior or availability in every distribution.

## git/git

[Pinned README](https://github.com/git/git/blob/f57c9a73884400380bddd172acc88b569834f909/README.md)

- **Observed:** The text-oriented README links tutorials and installed help, contribution paths, and a separate private security channel.
- **Transfer:** Route learners and contributors differently, and preserve a project's chosen security-reporting destination.
- **Limit:** Knowing a source-build path does not establish safe use of every version-control operation.

## git-lfs/git-lfs

[Pinned README](https://github.com/git-lfs/git-lfs/blob/0043a645047926f4bd7f7091299095528253d575/README.md)

- **Observed:** Platform installation and release verification lead to example usage and uninstalling.
- **Transfer:** Show the integration lifecycle after binary installation, including how repository tracking is configured.
- **Limit:** Installing the extension does not automatically convert every existing large file or establish hosting support.

## go-gitea/gitea

[Pinned README](https://github.com/go-gitea/gitea/blob/a36bb47c84fea32bad4b7a79dc314563ae09bc04/README.md)

- **Observed:** The page identifies a self-hosted development service, then distinguishes documentation, building, translating, integrations, and communication.
- **Transfer:** Separate administering the product from compiling it and contributing translations.
- **Limit:** A broad architecture claim needs maintained platform guidance before being reused as a compatibility guarantee.

## laurent22/joplin

[Pinned README](https://github.com/laurent22/joplin/blob/e43be19dbb6849508f2c34711d3a13b3690404b1/README.md)

- **Observed:** A note-taking explanation leads to help/documentation, community channels, and contribution; notes and Markdown are described separately from development.
- **Transfer:** Make user help and community support easy to find without forcing a contributor build route.
- **Limit:** Markdown-based notes do not prove compatibility of every sync backend or export format.

## logseq/logseq

[Pinned README](https://github.com/logseq/logseq/blob/4cf26891c176b6a02c8f4fb35a5046d7774d61e3/README.md)

- **Observed:** The page prominently distinguishes the database version and warns about beta/alpha data-loss risk before use, plugins, and development.
- **Transfer:** Place actual lifecycle/data-migration notices before adoption and distinguish extension from core development.
- **Limit:** These warnings are project-specific; do not invent equivalent risks for unrelated applications.
