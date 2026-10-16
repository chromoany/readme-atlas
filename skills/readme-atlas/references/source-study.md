# Source study: 200 README journeys

Study date: **2026-10-16**. These are original qualitative observations from pinned README files, followed by our editorial interpretation. They are not claims about conversion rates or prescriptions from the upstream maintainers.

## Study index

The corpus contains **200 repositories**, each with at least **1,000 GitHub Stars** when checked on **2026-10-16**. The observed minimum was **1,512**. Mature, widely recognized projects and domain relevance guided selection; Stars are an eligibility filter, not a README-quality score.

The original **32 detailed cases** remain below with their pinned revisions unchanged. An additional **168 focused source-structure reviews** are split into fourteen groups. Every case separates observed content, an editorial transfer, and a limit. Read the relevant group rather than loading the whole corpus for an ordinary README task.

| Study group | Projects | Reader decisions |
| --- | ---: | --- |
| [Foundational studies](#fastapi) | 32 | Original detailed cases and transfer limits below |
| [Web frameworks](studies/web-frameworks.md) | 12 | App scaffolding, library/framework adoption, migration, help routes |
| [Languages and build systems](studies/languages-build.md) | 12 | Source versus distribution, bootstrap, canonical repositories, release transitions |
| [CLI and shell tools](studies/cli-shell.md) | 12 | Shell activation, consequential defaults, integration, task-based examples |
| [Established libraries and SDK ecosystems](studies/libraries-sdk.md) | 12 | Module systems, data/type boundaries, installation choices, optional sub-APIs |
| [Data systems and formats](studies/data-storage.md) | 12 | Server/client interaction, formats versus products, trials versus clusters |
| [Infrastructure and cloud-native projects](studies/infrastructure.md) | 12 | Toolkit layers, stable versus experimental adoption, operational scope |
| [Testing, linting, and formatting](studies/quality-testing.md) | 12 | First test, transformations, configuration, contributor versus user installation |
| [Creative and desktop software](studies/creative-desktop.md) | 12 | Downloads versus building, development-tree status, target users, media workflows |
| [Editors, terminals, and developer applications](studies/developer-apps.md) | 12 | Source versus branded distribution, configuration, extension and migration routes |
| [Scientific computing and ML](studies/science-ml.md) | 12 | Optional dependencies, artifacts, reproducible interactions, serving and citation |
| [Security and network tools](studies/security-network.md) | 12 | Scan inputs, reporting channels, external validation, operating context |
| [Embedded systems and robotics](studies/embedded-robotics.md) | 12 | Targets, support tiers, building versus flashing, examples versus physical operation |
| [Documentation systems and learning platforms](studies/docs-learning.md) | 12 | Reading versus building, output demonstrations, curricula versus platform contribution |
| [Content, multilingual learning, and domain applications](studies/content-domain.md) | 12 | Topic navigation, audience language, domain formats, user versus author workflows |

## Synthesis

The transferable pattern is a sequence of reader decisions: understand the project, decide whether it fits, take a useful first action, recognize progress, then find deeper help. The form varies substantially:

- React, Vue, and Vite delegate much of onboarding to maintained documentation.
- FastAPI and Deno demonstrate an executable path and an observable result.
- uv and fzf organize substantial material around workflows and interactions.
- Supabase separates deployment choices and component explanations.
- Awesome and System Design Primer make navigation and learning the product itself.
- Linux routes readers by role; PostgreSQL identifies a source distribution and delegates installation.
- Kubernetes and Prometheus distinguish product use from supported code reuse.
- OpenTofu and Ansible distinguish release channels; Zephyr routes hardware-dependent setup to maintained guidance.
- p-limit keeps a focused API near its example; JupyterLab distinguishes installation, launch, and extension development.
- The Chinese-language 科技爱好者周刊 makes the newest issue and chronological archive the primary interaction.

Our recommendation is to choose a reader journey before choosing headings. Borrow the mechanism that serves that reader, not the whole page's length, visual style, or marketing vocabulary.

The follow-up [visual-design study](visual-design.md) examines identity areas, badges, screenshots, theme-aware assets, navigation, whitespace, and collapsible sections in thirteen of these projects. It distinguishes source observations from rendered browser checks and turns them into adaptable design decisions.

The larger sample adds several recurring decisions: distinguish a tool's use from building its source (Selenium, Blender, CMake); separate activation/configuration from installing a binary (Starship, zoxide, delta); preserve preview-versus-published status (RxJS); and identify canonical or relocated sources (Go, Zig). Specification documents (Parquet), curricula (OSSU), and domain-data examples (hledger) call for different first interactions. The linked group studies contain each case's evidence and limits.

## Expanded coverage

During the earlier 16-to-32 expansion, the original sixteen revisions remained unchanged. That second set added the following contrasts, selected for a different reader decision rather than a star threshold. Each project below has an observation, a transferable decision, and a limit later in this file.

| Added domain / contrast | Projects | Reader decision being studied |
| --- | --- | --- |
| Systems and hardware | Linux, Zephyr | Choose a role, board, or toolchain route |
| Database source distribution | PostgreSQL | Obtain a release or build the source tree |
| Infrastructure and operations | Kubernetes, OpenTofu, Ansible, Prometheus | Choose supported adoption, release channel, and operational scope |
| Focused library | p-limit | Understand one abstraction and its API limits |
| Editor and creative application | Neovim, Godot | Download, migrate, extend, or develop the product |
| Scientific software and notebooks | NumPy, scikit-learn, JupyterLab | Separate runtime use, optional dependencies, tests, and extensions |
| Security training | OWASP Juice Shop | Choose a training setup and understand demo restrictions |
| Chinese editorial archive | 科技爱好者周刊 | Read the newest issue, browse history, or submit a resource |

This set includes Markdown, reStructuredText, and an extensionless text README. The Chinese archive is a content repository, not another software-installation example. These additions broaden contrasts without making the corpus representative of all open source; large mature projects still dominate.

## FastAPI

[Pinned README][fastapi]

- **Observed:** positioning and benefits lead to installation; the example proceeds through file creation, server execution, checking a JSON response, and interactive API documentation. Sponsor and testimonial sections precede installation.
- **Transfer:** make the quickstart a complete loop with a recognizable result, then demonstrate a richer capability.
- **Limit:** the long tutorial, social proof, and sponsor placement reflect this project's editorial choices. A new library need not reproduce them or adopt its performance claims.

## uv

[Pinned README][uv]

- **Observed:** the opening identifies the tool, adds a scoped performance visual, lists capabilities, and provides installation. Later transcripts group projects, scripts, tools, Python versions, and a pip-compatible interface.
- **Transfer:** organize examples by jobs users perform; connect an action with its output and deeper docs.
- **Limit:** its benchmark and replacement claims belong to uv. A comparable-looking chart does not establish another project's speed or compatibility.

## GitHub CLI

[Pinned README][gh]

- **Observed:** a terminal screenshot grounds the product; supported environments, documentation, and installation routes are explicit. OS-specific details live in linked files, and source builds are separate.
- **Transfer:** distinguish the user's install path from contributor compilation, and use labeled links for substantial platform alternatives.
- **Limit:** the signing notice, enterprise support, and binary attestation material address this distribution. They are not required sections for every CLI.

## Ollama

[Pinned README][ollama]

- **Observed:** platform downloads and installation lead to initial interaction, model use, and REST/Python/JavaScript interfaces. A large categorized integration list appears later.
- **Transfer:** lead with the primary interaction and progressively expose integrations.
- **Limit:** model availability, resource needs, integrations, and privacy statements must be checked for the project being documented. A large ecosystem catalog can burden a smaller README.

## React

[Pinned README][react]

- **Observed:** a concise identity and a few principles lead to distinct adoption links, a documentation map, a small component example with its visible result, and contribution destinations.
- **Transfer:** let a minimal example explain the main abstraction while complete setup stays in maintained onboarding docs.
- **Limit:** the small example assumes a surrounding application environment. It is not evidence that an isolated JSX block is a complete quickstart for an unfamiliar tool.

## Vue

[Pinned README][vue]

- **Observed:** getting started is delegated almost immediately to the documentation site. Much of the remaining page covers sponsorship, questions, issues, contribution, and license.
- **Transfer:** a mature repository can use its README as a routing page when onboarding already exists elsewhere.
- **Limit:** a new project without a maintained documentation site cannot achieve the same onboarding simply by removing setup instructions.

## Vite

[Pinned README][vite]

- **Observed:** a compact branded opening and capabilities lead to an explanation of the development server and production build, documentation, a package table, contribution, and license.
- **Transfer:** explain the product's main parts and make monorepo packages discoverable without reproducing all documentation.
- **Limit:** the package table serves a multipackage repository; a single small package usually does not need one. Visual branding does not replace a precise explanation.

## Deno

[Pinned README][deno]

- **Observed:** the runtime is identified before OS-specific installation choices. The first program names a file, shows a web server, gives a run command, and identifies the local URL.
- **Transfer:** name the created file and the success destination, and distinguish shell-specific setup.
- **Limit:** runtime permissions and installer commands are Deno-specific. Copy the continuity of the example, not its environment assumptions.

## Supabase

[Pinned README][supabase]

- **Observed:** capabilities link to their own docs, a dashboard image illustrates the platform, support destinations are labeled by purpose, and the architecture section distinguishes hosted, self-hosted, and local development routes.
- **Transfer:** explain deployment choices and show how components fit together when those choices matter to adoption.
- **Limit:** its scope, large client table, support structure, and hosted service cannot be assumed for another platform. The README alone is not a self-contained production installation guide.

## RustDesk

[Pinned README][rustdesk]

- **Observed:** product imagery, language links, download destinations, and community access coexist with dependencies, platform build instructions, structure, and screenshots.
- **Transfer:** give application users a visible download route while preserving a separate route for source developers.
- **Limit:** extensive build recipes and notices address this application's context. They are not a universal amount of detail, and their currency was not established by this editorial study.

## PyTorch

[Pinned README][pytorch]

- **Observed:** the opening defines two core capabilities, then a topic index and explanations lead to binary installation, source prerequisites, accelerator-specific build paths, and additional resources.
- **Transfer:** make binary use, source development, and hardware-specific setup distinguishable; route changing compatibility decisions to maintained guidance.
- **Limit:** this project's substantial build matrix and maturity do not justify copying its prerequisites or broad performance language into another ML project.

## Transformers

[Pinned README][transformers]

- **Observed:** positioning and multilingual links precede explicit environment requirements, installation, and a high-level inference quickstart. The prose identifies model download/cache behavior, and expandable examples cover more modalities.
- **Transfer:** surface artifact requirements and begin with a small task; disclose advanced examples progressively.
- **Limit:** model access and compute needs vary. A generated sample sentence is illustrative output, not a deterministic guarantee for another setup.

## ripgrep

[Pinned README][ripgrep]

- **Observed:** the opening specifies search behavior and defaults. Quick links, screenshots, benchmark workloads and caveats, reasons to use or avoid the tool, installation, and builds serve readers with different questions.
- **Transfer:** explain consequential defaults and suitability limits; attach workload and environment context to comparisons.
- **Limit:** extensive benchmark discussion is useful for a performance-oriented search tool but unnecessary without comparable evidence or a reader need.

## fzf

[Pinned README][fzf]

- **Observed:** product imagery and highlights lead to a detailed index, installation, shell integration, usage, and advanced examples. Usage explains how input becomes a selected output.
- **Transfer:** communicate an interactive tool's experience and data flow, then organize optional integrations separately.
- **Limit:** its lengthy reference material and promotional content are editorial choices. New tools may benefit from a shorter path and linked reference docs.

## Awesome

[Pinned README][awesome]

- **Observed:** list-definition, contribution, and list-creation links accompany a category index and a broad set of grouped destinations, sometimes with short descriptions.
- **Transfer:** for curated resources, make scope, taxonomy, and contribution rules discoverable; navigation is the primary interaction.
- **Limit:** breadth, sponsor content, and the absence of software installation suit this repository. A learning sequence may be better than its category taxonomy for a course.

## System Design Primer

[Pinned README][primer]

- **Observed:** learning and interview motivations lead to study routes, flashcards, exercises, a large topic index, diagrams, tradeoffs, and deeper reading. The README carries substantial teaching content.
- **Transfer:** separate a recommended learning route from reference lookup; support complex material with diagrams and worked exercises.
- **Limit:** this is a counterexample to a blanket short-README rule. Its length should not become the default for a software package with separate docs.

## Linux

[Pinned README][linux]

- **Observed:** a short quick-start link group leads to essential documentation and explicit role routes for developers, researchers, administrators, maintainers, hardware vendors, and others. The extensionless README is text with underlined headings, rather than a Markdown badge layout.
- **Transfer:** when audiences have different jobs, name those jobs and route each to the relevant maintained guide; preserve a usable text outline.
- **Limit:** these roles and contribution requirements belong to a kernel project. They do not justify a large audience matrix or mandatory kernel build in an unrelated README.

## PostgreSQL

[Pinned README][postgres]

- **Observed:** the compact page identifies a source-code distribution, summarizes database capabilities, and links copyright, version documentation, source-building guidance, downloads, and the website. It contains no inline SQL quickstart.
- **Transfer:** state what the repository distributes and label source-building and release-download destinations separately.
- **Limit:** this source-tree gateway assumes extensive external documentation. It does not establish that a new database can omit connection setup or a first query without a maintained alternative.

## Kubernetes

[Pinned README][kubernetes]

- **Observed:** separate use and development sections lead to user documentation and contributor material. The README directs library consumers to published components and explicitly excludes importing the root Kubernetes module as a supported library route.
- **Transfer:** make supported consumption boundaries visible; distinguish running a product, embedding published packages, and compiling its source.
- **Limit:** the included build commands are developer actions, not cluster-installation instructions. Its governance and community sections reflect a large project.

## OpenTofu

[Pinned README][opentofu]

- **Observed:** an opening installation link and help channels precede explanations of configuration, execution plans, resource graphs, and change automation. A separate nightly section calls builds experimental and unsuitable for production. Security reporting and licensing have their own destinations.
- **Transfer:** explain consequential workflow stages and distinguish the normal adoption route from experimental artifacts.
- **Limit:** the README delegates setup; it is not an end-to-end infrastructure tutorial. Its feature descriptions do not validate another tool's safety claims or authorize executing changes to infrastructure.

## Ansible

[Pinned README][ansible]

- **Observed:** design principles precede a use section linking released installation. Development-branch use is qualified, and branch information distinguishes active development from stable releases. Help, contribution, coding guidance, and roadmap destinations are separate.
- **Transfer:** describe release channels in terms of the reader's choice, and label community support versus contribution paths.
- **Limit:** the principles contain aspirational and comparative language. They are positioning, not measurements or promises to transplant into another project.

## Prometheus

[Pinned README][prometheus]

- **Observed:** a collection/query/alert explanation and architecture image lead to binaries, a Docker trial with a local URL, and source builds. Build recipes explain UI asset differences. A dedicated section qualifies internal Go code reuse and names reusable companion libraries.
- **Transfer:** distinguish a working product from a supported embedding API; retain build differences that affect the first visible result.
- **Limit:** launching a trial container does not establish useful monitoring coverage or production operation. Its extensive build and module-version details serve this repository's specific distribution.

## p-limit

[Pinned README][p-limit]

- **Observed:** a one-sentence concurrency purpose leads to installation, a short usage example, and API details on counts, queue clearing, and concurrency. Recipes and an FAQ distinguish a limiter from a full queue. The usage example calls application-defined functions.
- **Transfer:** for a focused package, explain the main abstraction quickly and keep consequential semantics near the relevant API.
- **Limit:** the initial snippet is illustrative until its called functions are supplied. Clearing queued work and cancelling running work are different behaviors; visual brevity does not make the example independently runnable.

## Neovim

[Pinned README][neovim]

- **Observed:** goals and capabilities lead to package releases, a separate source-build section, a Vim migration link, and a source-tree map. License prose distinguishes newer contributions from material inherited from Vim.
- **Transfer:** offer migration guidance to an established audience, while separating user distribution from contributor navigation.
- **Limit:** its developer-oriented map is not a first editing tutorial. Its component licensing should not be flattened to a single badge without reading the relevant license material.

## Godot

[Pinned README][godot]

- **Observed:** identity and engine positioning lead to an editor screenshot. Getting the engine separates binary downloads from source compilation. Community, documentation, class reference, demos, and learning resources are linked onward.
- **Transfer:** show the real creative environment, then distinguish downloading the tool from building it and finding learning material.
- **Limit:** the screenshot does not teach a first game or establish export compatibility. Engine licensing statements do not automatically describe third-party assets or a user's finished game.

## NumPy

[Pinned README][numpy]

- **Observed:** identity and labeled project destinations precede a short capability list, test prerequisites, a test command, and several contribution routes, including non-code work. User tutorials are delegated to documentation.
- **Transfer:** label testing as validation after installation, and make useful non-code contribution paths discoverable when they exist.
- **Limit:** running the test suite is not an array-programming quickstart. Optional test dependencies should not be promoted to ordinary runtime requirements.

## scikit-learn

[Pinned README][sklearn]

- **Observed:** the RST README separates runtime dependencies, plotting/example dependencies, user installation, development, tests, help, and citation. Dependency versions use substitutions defined within the file; tests are explicitly run outside the source directory.
- **Transfer:** distinguish core use from optional examples and contributor validation; preserve format-specific definitions that make requirements readable.
- **Limit:** dependency versions and test location are snapshot-specific facts. The installation section is not a model-training tutorial, and source markup inspection does not verify rendered substitutions.

## JupyterLab

[Pinned README][jupyterlab]

- **Observed:** installation alternatives lead to a launch command and the expected browser opening, with PATH troubleshooting. Prebuilt versus source extensions, an older major version's maintenance status, extension development, and core contribution are distinguished.
- **Transfer:** connect install to launch and recognizable success; distinguish using extensions from developing them, and place relevant lifecycle notices near adoption.
- **Limit:** browser compatibility and maintenance dates need fresh evidence when documenting another release. A linked hosted demo is not evidence that it was exercised in this study.

## Zephyr

[Pinned README][zephyr]

- **Observed:** the RST README identifies resource-constrained use and multiple architectures, links supported boards, and routes setup to a getting-started guide. Resources group development, community, and security destinations. Embedded HTML supplies theme-specific logo sources.
- **Transfer:** route hardware-dependent adoption to maintained board and setup guidance instead of implying one universal command.
- **Limit:** a supported-board link does not establish that every architecture/board/toolchain combination works. No firmware was built or flashed for this editorial study.

## Home Assistant

[Pinned README][homeassistant]

- **Observed:** the concise RST page links a demo, installation, tutorials, and docs; substituted image references show the interface and integrations. Architecture and component-development links serve extension authors separately from users.
- **Transfer:** a visual application can use a concise gateway with distinct use and extension routes; preserve image substitutions and their destinations when editing RST.
- **Limit:** the privacy-oriented positioning is not a verification of every integration's behavior. Screenshots or integration links do not prove compatibility with a reader's devices.

## OWASP Juice Shop

[Pinned README][juiceshop]

- **Observed:** security-training positioning and a screenshot slideshow precede source, packaged, container, and Vagrant routes. Compatibility distinguishes supported and tested runtime versions. A demo notice excludes that shared instance from personal hacking exercises; some challenges have additional AI-provider dependencies.
- **Transfer:** distinguish a preview from an environment intended for reader exercises, and put task-dependent prerequisites near setup.
- **Limit:** these restrictions follow this deliberately vulnerable training application. They are not a generic warning template for ordinary apps; code and companion-book licenses also differ.

## 科技爱好者周刊 (ruanyf/weekly)

[Pinned README][weekly]

- **Observed:** a Chinese opening states the weekly publishing rhythm and resource-submission destination. The archive groups issues by year and month in reverse chronological order, using issue numbers and descriptive article titles.
- **Transfer:** for an ongoing publication, prioritize the newest edition and stable history navigation; retain the audience's language and submission vocabulary.
- **Limit:** an issue archive is not a prerequisite-based curriculum or a software package. A stated schedule is an editorial commitment, not evidence that every future issue will appear on time.

## From observations to skill decisions

| Evidence | Editorial inference used by the skill |
| --- | --- |
| FastAPI / Deno show a result after execution | Include recognizable success in runnable onboarding |
| Vue / Vite route readers outward | Permit a concise documentation gateway |
| uv / fzf group practical workflows | Organize deeper examples by user task |
| GitHub CLI / PyTorch separate installation and builds | Distinguish users from source contributors |
| Supabase presents deployment choices | Label hosted, local, and self-hosted routes |
| Transformers explains downloads and task examples | State artifact needs before expensive first use |
| ripgrep describes defaults and limitations | Make material fit and evidence boundaries explicit |
| Awesome / Primer prioritize discovery and learning | Do not require software installation for every repository |
| Linux names audience roles; PostgreSQL labels source distribution | Route by reader job and repository purpose |
| Kubernetes / Prometheus qualify internal code reuse | Do not imply every importable module is a supported public API |
| OpenTofu / Ansible / JupyterLab distinguish release or maintenance status | Label experimental and obsolete routes when relevant |
| p-limit uses undefined application helpers in a compact example | Distinguish an abstraction example from a self-contained runnable path |
| scikit-learn / NumPy separate use and test dependencies | Keep optional examples and development requirements distinct |
| Zephyr links board/setup guidance; Home Assistant separates component authors | Match setup to hardware or extension roles |
| Juice Shop restricts a shared demo | Preserve actual exercise and demo-use boundaries |
| Weekly groups editions by year/month | Use chronological navigation for publications |

Evidence-first fact checking, translation consistency, scope preservation, and the agent-skill distribution route are author-designed workflow safeguards. They complement the observations; they are not findings that all 200 READMEs implement. The centered single-group badge convention also remains an author-defined convention; several added projects arrange badges differently.

Source links below pin the README file, not the external sites or assets it references. Upstream text and assets retain their own licenses.

[fastapi]: https://github.com/fastapi/fastapi/blob/0b919816378eaa773df7ce4204414c712c9fdbea/README.md
[uv]: https://github.com/astral-sh/uv/blob/b8993e0a3b15f37e6b523bc5d02d2e7128713cad/README.md
[gh]: https://github.com/cli/cli/blob/59e9f78eacdf2554f8534d166808c3e9b8c7ebcb/README.md
[ollama]: https://github.com/ollama/ollama/blob/d919272e53593d1d55d40e1180eaa06dfbede3ac/README.md
[react]: https://github.com/facebook/react/blob/098d2e87a1f7142947418d15f63f975b58c4685b/README.md
[vue]: https://github.com/vuejs/core/blob/bf5f0dd877dd3c23ce85c2cbc1dd771567e84c8c/README.md
[vite]: https://github.com/vitejs/vite/blob/928e721b36690ac0f3f118290a21fc0cc4349055/README.md
[deno]: https://github.com/denoland/deno/blob/a18ce33715e30cd2b0d99c7e322ef11a65490e4d/README.md
[supabase]: https://github.com/supabase/supabase/blob/991653aa36a727f009f72d75fc2388c135b4d242/README.md
[rustdesk]: https://github.com/rustdesk/rustdesk/blob/e400bb75546cebf4f72a5ef3cf6e4a3efa2c3aa7/README.md
[pytorch]: https://github.com/pytorch/pytorch/blob/88ea2d6a53c70dc7d7669ced28a93f112daaa6a7/README.md
[transformers]: https://github.com/huggingface/transformers/blob/b0cdc61e607f39403e248b11c35aef4edfa7d216/README.md
[ripgrep]: https://github.com/BurntSushi/ripgrep/blob/3fce3b5bb0236da2df6d99672afb8a719642eca7/README.md
[fzf]: https://github.com/junegunn/fzf/blob/c8c2d0828a94a00879ceb6f95112a42e3ea322cf/README.md
[awesome]: https://github.com/sindresorhus/awesome/blob/bc98e517ddca672f55f9857d714fc3ea3c3540b2/readme.md
[primer]: https://github.com/donnemartin/system-design-primer/blob/ae9bbd7b02d90b9866215de185217d33f39ab733/README.md
[linux]: https://github.com/torvalds/linux/blob/2f2f7eeef8b0a1a9b9ca998231419873ccae8d4e/README
[postgres]: https://github.com/postgres/postgres/blob/ba51d62be465c420b0fbe3b0efd0ccd488e79922/README.md
[kubernetes]: https://github.com/kubernetes/kubernetes/blob/aa155223ce49a2fc150a3b78278dad3a4881f7eb/README.md
[opentofu]: https://github.com/opentofu/opentofu/blob/105b18bb846f80760ee983c8e49044b2bd30f0a4/README.md
[ansible]: https://github.com/ansible/ansible/blob/b458cf1c9d5189614e10e56256263597eb9ce3b0/README.md
[prometheus]: https://github.com/prometheus/prometheus/blob/466be3beb37099c28804608966f894b0dbad9993/README.md
[p-limit]: https://github.com/sindresorhus/p-limit/blob/a8a6fbec4e0e866d6d779b10889bb4f5567e70eb/readme.md
[neovim]: https://github.com/neovim/neovim/blob/be5167e21cfbb5d566c09a67c1852d0e18c62c38/README.md
[godot]: https://github.com/godotengine/godot/blob/4d10419cacd6d3009976e8f9fd3abd970fd58018/README.md
[numpy]: https://github.com/numpy/numpy/blob/12cf5b9bf2d7fb4ba0d2671a101f0e23074b9c4e/README.md
[sklearn]: https://github.com/scikit-learn/scikit-learn/blob/d0e22aee7bbef7b310a2f08227c214ff6df9a526/README.rst
[jupyterlab]: https://github.com/jupyterlab/jupyterlab/blob/5d3ae70270ffd602eac1be77ca24ed7a88ad518a/README.md
[zephyr]: https://github.com/zephyrproject-rtos/zephyr/blob/c136c73d7be3305d2c07ee5726d4c6d0d985068b/README.rst
[homeassistant]: https://github.com/home-assistant/core/blob/f1f9fb4ef0413632ece929c8753a42b6c57a8049/README.rst
[juiceshop]: https://github.com/juice-shop/juice-shop/blob/399fba76194305a312693eee44f4df64bdf0c3ce/README.md
[weekly]: https://github.com/ruanyf/weekly/blob/b9d8eb2ac3d55e82e095daebaa7df530995f2dd2/README.md
