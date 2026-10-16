# Review the reader's path

Apply relevant checks. Missing optional decoration is not a defect.

## Facts

- Does the description match implemented behavior and intended scope?
- Are package, executable, import, image, and service names correct?
- Do versions and platforms have evidence? Are declarations distinguished from tested combinations?
- Do releases, demos, badges, screenshots, docs, and license destinations exist?
- Are features separated from plans? Are performance claims traceable and qualified?
- Are unknowns omitted or raised explicitly instead of guessed?
- Is the repository's distribution role clear, and are advertised SDKs or extension points supported public interfaces?
- Were root README pointers or symlinks followed, with package-level paths and canonical/migrated repository destinations preserved?
- Are relevant release channels and lifecycle notices accurate, with experimental artifacts distinguished from normal adoption?

## First use

- Can the primary reader choose an installation, adoption, or learning route?
- Are required configuration, credentials, data, services, and substantial downloads or hardware needs explained before use?
- Does a runnable path name the working directory, create inputs, and use the right shell?
- Are commands copyable without prompts or embedded output?
- Does the example show a recognizable result, URL, file, or interaction? Is variable output described honestly?
- Are user installation, contributor development, and production deployment distinguishable?
- Does a documentation gateway reach complete maintained onboarding?
- Does a knowledge repository offer reading or practice instead of artificial installation?
- Are core runtime requirements separated from optional examples, plotting, tests, builds, and extension development?
- Are application-defined helpers supplied for a runnable example, or is the snippet clearly illustrative?
- Does hardware-dependent setup identify the target or link maintained board/toolchain guidance without implying untested combinations?
- If the project restricts a shared demo, is the intended exercise environment clear?
- Does a publication make its latest edition and archive discoverable in the audience's language?
- Does an integrated CLI explain activation/configuration after installing the executable?
- Does a book separate reading from building its source, and does a specification avoid an invented software-install route?

## Presentation

- Is the overall visual direction coherent with the project's identity and audience?
- Does the opening have a clear focal point, useful navigation, and comfortable spacing?
- Are all badges together in one visible header group, including downloads, compatibility, and community/listing badges, with none scattered in the body/footer or hidden in `details`?
- Are the complete badge group and everything before it (title, logo, tagline, language links) centered, with the following body left-aligned?
- Are badge styles, icon roles, accents, and image proportions consistent? Do badges communicate genuine facts?
- Do screenshots demonstrate an actual task, with legible text, useful cropping, captions, and no private data?
- Do visual assets remain legible on the inspected themes? Do navigation, badges, and comparisons work at the inspected reading widths?
- Do optional details stay accessible without hiding installation or the first example?
- Does the opening explain the project and its value to the intended reader?
- Are differentiators concrete and supported?
- Does navigation help? Are useful anchors preserved or given compatibility anchors?
- Are deeper flags, APIs, and platform recipes placed where expected?
- Are fences closed, shell labels correct, tables readable, and image alt text meaningful?
- Do relative links resolve with exact case from the containing file?
- Are language files mutually linked and factually consistent?
- Do help and contribution links name their intended destinations accurately?
- For RST, AsciiDoc, or text READMEs, do native headings, substitutions, image directives, and links survive the edit? Was any format conversion intentional?

## Reporting

Prioritize review findings by reader impact:

| Impact | Meaning | Example |
| --- | --- | --- |
| Blocking | Cannot complete the path or material misrepresentation | Nonexistent package; missing service; invented platform support |
| Significant | Reader must guess or choose among confusing routes | Undocumented configuration; user setup mixed with compilation |
| Editorial | Improve clarity without changing correctness | Repetition; unhelpful caption |

Give each finding a location, evidence, consequence, and smallest useful fix. Do not reduce a review to a score or absent headings.

For create/rewrite tasks, report validation outside the README:

- **Executed:** actual smoke command and observed result.
- **Inspected:** commands or facts traced to repository evidence.
- **Unverified:** concrete step not executed and why.

For visual findings, name the affected view and the reader consequence: unreadable logo on a dark background, primary action buried by a banner, or a table that forces narrow-screen horizontal scrolling. Separate these observed defects from optional style preferences. Use [visual-design.md](visual-design.md) for project-specific choices.

Link checks do not validate software behavior or visual composition; one local smoke run does not establish every platform. List inspected themes and reading widths, or state that the presentation was reviewed from source only.
