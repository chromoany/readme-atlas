# Source study: sixteen README journeys

Study date: **2026-10-16**. These are original qualitative observations from pinned README files, followed by our editorial interpretation. They are not claims about conversion rates or prescriptions from the upstream maintainers.

## Synthesis

The transferable pattern is a sequence of reader decisions: understand the project, decide whether it fits, take a useful first action, recognize progress, then find deeper help. The form varies substantially:

- React, Vue, and Vite delegate much of onboarding to maintained documentation.
- FastAPI and Deno demonstrate an executable path and an observable result.
- uv and fzf organize substantial material around workflows and interactions.
- Supabase separates deployment choices and component explanations.
- Awesome and System Design Primer make navigation and learning the product itself.

Our recommendation is to choose a reader journey before choosing headings. Borrow the mechanism that serves that reader, not the whole page's length, visual style, or marketing vocabulary.

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

Evidence-first fact checking, translation consistency, scope preservation, and the agent-skill distribution route are author-designed workflow safeguards. They complement the observations; they are not findings that all sixteen READMEs implement.

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
