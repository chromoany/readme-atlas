# Patterns by reader journey

Adapt these outlines; remove sections without evidence or reader purpose. The [source study](source-study.md) separates observed structures from our recommendations.

## Library or SDK

**Use when:** the reader embeds the project in their own code.

Suggested flow: identity and use case → installation and runtime requirement → minimal input/output example → capabilities → API / examples → help / contribution / license.

Expose the main abstraction. Include imports, required setup, and a recognizable result. If a maintained tutorial owns setup, link to it instead of copying an incomplete fragment. Distinguish distribution names from import names.

**Observed:** React provides a component example and routes adoption situations to documentation; Transformers demonstrates tasks through a high-level pipeline. **Do not inherit:** their ecosystem size, marketing claims, or supported versions.

## CLI or developer tool

**Use when:** the reader primarily runs commands locally or in automation.

Suggested flow: specific task → screenshot or transcript when useful → installation → first command and output → task recipes → options / compatibility → help / contribution / license.

For interactive tools, explain selection and exit. For file-processing tools, provide or identify example input. Distinguish package names from executables. Group advanced examples by user task rather than internal module.

**Observed:** uv groups project, script, tool, and interpreter workflows; fzf shows an interactive experience and separates shell integration; GitHub CLI routes installations by OS. **Tradeoff:** copying every platform installer creates a maintenance burden.

## Desktop or web application

**Use when:** the product experience matters more than a programming interface.

Suggested flow: purpose → real screenshot or demo → download / launch → first interaction → supported environments → configuration / help → developer setup / contribution / license.

Put the supported user distribution before a source build unless intentionally developer-only. With no public instance or release, describe the actual local route. Give screenshots task-focused captions.

**Observed:** RustDesk uses product imagery, downloads, and separate build material. **Tradeoff:** a mature application's extensive build recipes need not be copied into a small app's README.

## Service or platform

**Use when:** the reader must choose an environment or assemble components.

Suggested flow: problem and scope → deployment choices → first-use route → verification endpoint or UI → capabilities / architecture → operations docs → help / contribution / license.

Label hosted, local development, and self-hosted production distinctly. Link existing deployment docs for extensive setup. Explain required services and configuration before startup. A successful local server does not establish production readiness.

**Observed:** Supabase distinguishes deployment choices and components; Ollama puts installation and initial interaction before API and integrations. **Tradeoff:** integration catalogs aid discovery but can bury onboarding.

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

## Agent skill

**Use when:** a repository distributes instructions and references to an agent host.

Suggested flow: capability and host → install complete folder → invocation → expected file / report → workflow and boundaries → references / contribution / license.

Make install paths host-specific and retain references and metadata. A prompt is the first interaction; fictional output is not execution evidence. Distinguish instruction portability from verified host compatibility.

**Application:** README Atlas uses this route itself. This is our adaptation, not a separate finding from the sixteen-project corpus.

## Documentation gateway

**Use when:** maintained documentation already provides complete onboarding.

Keep identity, entry links, important adoption choices, and contribution destinations. A minimal example can clarify the product without duplicating tutorials. Verify start links reach the task.

**Observed:** Vue delegates getting started; Vite explains its two main parts and links onward. **Tradeoff:** an unfamiliar project without maintained docs needs more information locally.

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

There is no required badge count, word count, section count, or visual style.
