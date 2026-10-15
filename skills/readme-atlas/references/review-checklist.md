# Review the reader's path

Apply relevant checks. Missing optional decoration is not a defect.

## Facts

- Does the description match implemented behavior and intended scope?
- Are package, executable, import, image, and service names correct?
- Do versions and platforms have evidence? Are declarations distinguished from tested combinations?
- Do releases, demos, badges, screenshots, docs, and license destinations exist?
- Are features separated from plans? Are performance claims traceable and qualified?
- Are unknowns omitted or raised explicitly instead of guessed?

## First use

- Can the primary reader choose an installation, adoption, or learning route?
- Are required configuration, credentials, data, services, and substantial downloads or hardware needs explained before use?
- Does a runnable path name the working directory, create inputs, and use the right shell?
- Are commands copyable without prompts or embedded output?
- Does the example show a recognizable result, URL, file, or interaction? Is variable output described honestly?
- Are user installation, contributor development, and production deployment distinguishable?
- Does a documentation gateway reach complete maintained onboarding?
- Does a knowledge repository offer reading or practice instead of artificial installation?

## Presentation

- Does the opening explain the project and its value to the intended reader?
- Are differentiators concrete and supported?
- Does navigation help? Are useful anchors preserved or given compatibility anchors?
- Are deeper flags, APIs, and platform recipes placed where expected?
- Are fences closed, shell labels correct, tables readable, and image alt text meaningful?
- Do relative links resolve with exact case from the containing file?
- Are language files mutually linked and factually consistent?
- Do help and contribution links name their intended destinations accurately?

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

Link checks do not validate software behavior; one local smoke run does not establish every platform.
