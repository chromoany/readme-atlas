# Patterns by reader journey

Adapt these outlines; remove sections without evidence or reader purpose. The [source study](source-study.md) separates observed structures from our recommendations.

## Library or SDK

**Use when:** the reader embeds the project in their own code.

Suggested flow: identity and use case → installation and runtime requirement → minimal input/output example → capabilities → API / examples → help / contribution / license.

Expose the main abstraction. Include imports, required setup, and a recognizable result. If a maintained tutorial owns setup, link to it instead of copying an incomplete fragment. Distinguish distribution names from import names.

**Observed:** React provides a component example and routes adoption situations to documentation; Transformers demonstrates tasks through a high-level pipeline; p-limit puts focused API semantics beside usage. **Do not inherit:** their ecosystem size, marketing claims, or supported versions. p-limit's application-defined helpers also illustrate why an abstraction example is not automatically a runnable program.

Check supported consumption boundaries. Kubernetes directs consumers to published components; Prometheus distinguishes its stand-alone program from companion libraries. Do not advertise an internal module as an SDK merely because it can be imported.

## CLI or developer tool

**Use when:** the reader primarily runs commands locally or in automation.

Suggested flow: specific task → screenshot or transcript when useful → installation → first command and output → task recipes → options / compatibility → help / contribution / license.

For interactive tools, explain selection and exit. For file-processing tools, provide or identify example input. Distinguish package names from executables. Group advanced examples by user task rather than internal module.

Separate binary installation from activation or configuration: Starship needs shell setup and suitable font configuration, zoxide needs shell integration, and delta documents Git pager configuration. State what the reader must change to observe the tool; do not perform global configuration changes merely to inspect README prose. See the [CLI and shell studies](studies/cli-shell.md).

**Observed:** uv groups project, script, tool, and interpreter workflows; fzf shows an interactive experience and separates shell integration; GitHub CLI routes installations by OS. **Tradeoff:** copying every platform installer creates a maintenance burden.

## Desktop or web application

**Use when:** the product experience matters more than a programming interface.

Suggested flow: purpose → real screenshot or demo → download / launch → first interaction → supported environments → configuration / help → developer setup / contribution / license.

Put the supported user distribution before a source build unless intentionally developer-only. With no public instance or release, describe the actual local route. Give screenshots task-focused captions.

**Observed:** RustDesk uses product imagery, downloads, and separate build material. **Tradeoff:** a mature application's extensive build recipes need not be copied into a small app's README.

Neovim adds a migration route for existing Vim users; Godot separates editor binaries, engine compilation, and learning demos; Home Assistant separates user setup from component development. Include these secondary routes when the audience actually needs them. A contributor source-tree map is not a first-use tutorial.

## Service or platform

**Use when:** the reader must choose an environment or assemble components.

Suggested flow: problem and scope → deployment choices → first-use route → verification endpoint or UI → capabilities / architecture → operations docs → help / contribution / license.

Label hosted, local development, and self-hosted production distinctly. Link existing deployment docs for extensive setup. Explain required services and configuration before startup. A successful local server does not establish production readiness.

**Observed:** Supabase distinguishes deployment choices and components; Ollama puts installation and initial interaction before API and integrations. **Tradeoff:** integration catalogs aid discovery but can bury onboarding.

### Infrastructure and observability

When commands manage other systems, explain the workflow stages and environment before presenting an action. Keep stable installation, experimental artifacts, local trials, and production operation distinguishable. A running monitoring UI is different from configured targets collecting useful data.

**Observed:** OpenTofu describes execution plans separately from applying changes and qualifies nightlies; Ansible distinguishes release and development branches; Prometheus gives a local container trial and explains source-build UI asset differences. **Limit:** these are documentation observations, not validation of upstream operational claims. Apply only constraints established by the project being documented.

## Systems, database source trees, or embedded software

**Use when:** readers need a role, source-distribution, target-board, or toolchain choice before setup.

Suggested flow: repository purpose → reader role / supported target → appropriate download or setup guide → first build or task → recognizable result → development / support.

State whether the repository is the source distribution rather than an end-user installer. Where setup depends on hardware, link maintained target and toolchain guidance rather than implying every architecture and board combination is supported. Separate a successful build from a flashed or running device.

**Observed:** Linux provides role-specific documentation routes; PostgreSQL identifies its source distribution and links downloads and building; Zephyr links supported boards and getting started. **Tradeoff:** a small single-target tool rarely needs a kernel-sized role map, and a gateway needs a real maintained destination.

The larger [language/build study](studies/languages-build.md) distinguishes downloading a runtime from compiling it, and bootstrapping a build tool from using it. Go identifies a canonical repository outside GitHub; Zig's pinned GitHub README is a relocation notice. Preserve repository authority and migration routes instead of reviving obsolete installation text.

## Specification or interchange format

**Use when:** the repository defines a protocol, schema, file layout, or interchange standard rather than distributing an end-user program.

Suggested flow: scope and motivation → glossary / concepts → format structure → implementation status or consumers → building supporting artifacts when relevant → contribution.

Explain the relationship between a format and implementations. Do not invent a package-install command for a specification. The [data-system study](studies/data-storage.md) includes Parquet's conceptual/layout navigation and Arrow's implementation-status routing. Neither implies every consumer implements every feature.

## Scientific computing or notebook environment

**Use when:** readers install numerical software or launch an interactive computing environment, with optional plotting, tests, or extensions.

Suggested flow: task and environment → core installation → smallest calculation or launch → recognizable result → optional dependencies / extensions → scientific and contributor resources.

Separate runtime dependencies from plotting/examples, test tooling, source builds, and extension development. Do not present running a whole test suite as the first useful scientific result. Link changing requirements to maintained version guidance. Preserve supplied citation destinations without inventing a paper or DOI.

**Observed:** NumPy labels testing and contribution routes; scikit-learn separates dependency purposes and defines RST version substitutions; JupyterLab connects installation to browser launch and distinguishes extension routes. **Limit:** those README structures do not establish reproducible scientific results or tested compatibility in another environment.

## ML or research implementation

**Use when:** hardware, artifacts, datasets, or reproducibility determine usability.

Suggested flow: task and scope → example result → environment and artifacts → smallest inference / reproduction path → evaluation protocol / limitations → models / training docs → supplied citation → license.

State tested software/hardware combinations only with evidence. Identify weights, data downloads, access requirements, and their licenses separately from code licensing when known. For stochastic output, show expected format or behavior rather than promising exact text. Separate small inference from full training or paper reproduction.

**Observed:** PyTorch separates binaries, source builds, and accelerator setup; Transformers explains environments, model download/cache, and task examples. **Do not inherit:** unrelated hardware minimums, model access, or benchmarks.

## Curated list or learning resource

**Use when:** reading, finding, or practicing is the core product.

Suggested flow: scope and learner → start-here route → category index or study sequence → described resources → inclusion / contribution rules → license.

Explain established prerequisites and selection criteria. Separate learning order from reference taxonomy when useful. The README may be the main content; length alone is not a defect.

**Observed:** Awesome organizes categories and links list-authoring guidance; System Design Primer combines study routes, exercises, diagrams, and topic indexes. **Do not force:** package installation, a fake executable quickstart, or SaaS feature sections.

For a periodical, use latest edition → year/month archive → submission route when appropriate. 科技爱好者周刊 demonstrates chronological discovery in Chinese; it does not prescribe a course sequence. Preserve useful edition identifiers and audience vocabulary rather than replacing the archive with generic software headings.

For an exercise application, separate viewing a demo from running a training environment. OWASP Juice Shop provides setup choices and explicitly restricts exercise use of its shared demo. Preserve that restriction when relevant; it is not a general warning requirement for unrelated applications.

## Agent skill

**Use when:** a repository distributes instructions and references to an agent host.

Suggested flow: capability and host → install complete folder → invocation → expected file / report → workflow and boundaries → references / contribution / license.

Make install paths host-specific and retain references and metadata. A prompt is the first interaction; fictional output is not execution evidence. Distinguish instruction portability from verified host compatibility.

**Application:** README Atlas uses this route itself. This is our adaptation, not a separate finding from the thirty-two-project corpus.

## Documentation gateway

**Use when:** maintained documentation already provides complete onboarding.

Keep identity, entry links, important adoption choices, and contribution destinations. A minimal example can clarify the product without duplicating tutorials. Verify start links reach the task.

**Observed:** Vue delegates getting started; Vite explains its two main parts and links onward. **Tradeoff:** an unfamiliar project without maintained docs needs more information locally.

For book or curriculum repositories, separate reading the published material from building its source. mdBook's published user guide also demonstrates its output; the Rust book distinguishes reading from documentation-tool installation. OSSU organizes prerequisites and curriculum sequence, while The Odin Project separates learners from curriculum contributors. See the [documentation and learning studies](studies/docs-learning.md).

Root indirection can be intentional: Next.js, Zod, and Redux Toolkit point to package READMEs. Preserve the real file's relative-link base and the distinction between repository and package entry points. RxJS's pinned README separately qualifies preview/publication status; a version in source metadata is not evidence of a registry release. See the [web framework](studies/web-frameworks.md) and [library ecosystem](studies/libraries-sdk.md) studies.

## Rewrite decisions

| Symptom | Better decision |
| --- | --- |
| Badges but no project sentence | Lead with capability and audience |
| Source build dominates despite binary releases | Put user installation first; retain developer route |
| Installers and deployment modes interleave | Label choices; make one path continuous |
| Snippet assumes a missing file or service | Supply setup or link a complete tutorial |
| Features repeat internal module names | Describe enabled tasks and outcomes |
| Screenshot is decorative or unavailable | Use a real task-focused asset, text example, or no image |
| Performance claim lacks workload or source | Add existing evidence or remove the claim |
| Long README is the actual learning resource | Improve navigation before splitting |
| Translation adds promises | Preserve factual equivalence; fix drift explicitly |
| Internal code is offered as a public SDK | Check supported package boundaries and link the intended distribution |
| Test or plotting dependencies appear mandatory for all users | Separate requirements by task |
| Nightly or retired release is the unlabeled default | Show the project's supported adoption route and lifecycle status |
| Hardware list implies every combination works | Link maintained target/setup guidance and scope verified combinations |
| RST definitions disappear during a visual rewrite | Preserve the file's syntax and resolve its substitutions |
| A publication archive is treated as a software tutorial | Keep newest-edition and chronological navigation |
| A root README is only a path pointer | Follow the pinned target before diagnosing missing documentation |
| A specification is given an invented package quickstart | Explain concepts, layout, and implementation destinations |
| Installing a CLI produces no visible integration | Include the actual activation/configuration step |
| A preview version is described as a published release | Verify the project's stated distribution status |

There is no required badge count, word count, section count, or visual style.
