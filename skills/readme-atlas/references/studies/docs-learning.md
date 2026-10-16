# Documentation systems and learning platforms: README studies

Study date: **2026-10-16** (Asia/Hong_Kong client date). These twelve repositories passed the **1,000 GitHub Stars minimum** at selection. Star counts below are dated observations, not a quality score.

**Compare:** Reading versus building, output demonstrations, curricula versus platform contribution.

This is a focused source-structure review of pinned READMEs. Observations, editorial transfers, and limits are separate; upstream commands and rendered layouts were not exercised in this pass.

| Repository | Stars at selection | README format |
| --- | ---: | --- |
| [rust-lang/book](#rust-langbook) | 18,417 | markdown |
| [rust-lang/mdBook](#rust-langmdbook) | 22,222 | markdown |
| [sphinx-doc/sphinx](#sphinx-docsphinx) | 8,061 | restructuredtext |
| [mkdocs/mkdocs](#mkdocsmkdocs) | 22,502 | markdown |
| [squidfunk/mkdocs-material](#squidfunkmkdocs-material) | 27,577 | markdown |
| [facebook/docusaurus](#facebookdocusaurus) | 66,501 | markdown |
| [docsifyjs/docsify](#docsifyjsdocsify) | 31,543 | markdown |
| [11ty/eleventy](#11tyeleventy) | 19,969 | markdown |
| [ossu/computer-science](#ossucomputer-science) | 210,034 | markdown |
| [TheOdinProject/curriculum](#theodinprojectcurriculum) | 13,149 | markdown |
| [freeCodeCamp/freeCodeCamp](#freecodecampfreecodecamp) | 457,131 | markdown |
| [public-apis/public-apis](#public-apispublic-apis) | 489,187 | markdown |

## rust-lang/book

[Pinned README](https://github.com/rust-lang/book/blob/1500248d8f230566e4ec9f27fcbb8fe9e2898ab1/README.md)

- **Observed:** The opening distinguishes reading the book from building its source; requirements, build commands, translations, and spellchecking follow.
- **Transfer:** Separate learners' reading routes from documentation contributors' toolchain requirements.
- **Limit:** A reader should not need to build a book merely because the source repository documents that workflow.

## rust-lang/mdBook

[Pinned README](https://github.com/rust-lang/mdBook/blob/ae0bc6996bf45cd9e93b9222fd4cd264ee69e6d4/README.md)

- **Observed:** The compact overview sends readers to a user guide that doubles as an example output and separately links contribution.
- **Transfer:** A documentation generator can use its own published guide as both onboarding and a truthful product demonstration.
- **Limit:** The demonstration site does not prove every custom theme, preprocessor, or deployment works.

## sphinx-doc/sphinx

[Pinned README](https://github.com/sphinx-doc/sphinx/blob/b04a2101295ac3fb725b16111eda0284b6da4cca/README.rst)

- **Observed:** The RST page explains its markup model, lists output/documentation features, and gives installation plus contribution routes.
- **Transfer:** Explain authoring language and generated outputs before plugin or build detail.
- **Limit:** A documentation engine's capabilities do not prove every extension renders identically.

## mkdocs/mkdocs

[Pinned README](https://github.com/mkdocs/mkdocs/blob/2862536793b3c67d9d83c33e0dd6d50a791928f8/README.md)

- **Observed:** A Markdown-documentation identity leads to features, support, resource links, and contribution.
- **Transfer:** A concise gateway can explain the transformation and distinguish help from contribution.
- **Limit:** The gateway should not imply that merely possessing Markdown files deploys a complete site.

## squidfunk/mkdocs-material

[Pinned README](https://github.com/squidfunk/mkdocs-material/blob/a0f2a2a70ee978c2b0afc80347fed6eb4cec7867/README.md)

- **Observed:** Feature-led sections describe authoring and ownership, followed by pip quickstart, configuration links, adopters, and licensing.
- **Transfer:** Keep theme/framework installation and configuration discoverable beneath the visual product explanation.
- **Limit:** An adopter wall and polished presentation are not evidence of accessibility or responsiveness in another site's theme.

## facebook/docusaurus

[Pinned README](https://github.com/facebook/docusaurus/blob/a3f451ff0e1a4cdf77dbbd2ce52e26878c6a44a9/README.md)

- **Observed:** The introduction links a short tutorial and browser playground, then explains installation, localization, and contribution routes.
- **Transfer:** Offer a low-friction preview alongside a maintained local onboarding route.
- **Limit:** A playground does not establish local build or deployment success.

## docsifyjs/docsify

[Pinned README](https://github.com/docsifyjs/docsify/blob/2d8cb5a74c29797e6016dea857e36d1e339675bf/README.md)

- **Observed:** The introduction explicitly says it turns Markdown into a site without a build process; quickstart offers a template and tutorial.
- **Transfer:** Explain what serving/authoring means for this particular tool instead of assuming every docs system has a build step.
- **Limit:** No-build positioning does not eliminate hosting or runtime requirements.

## 11ty/eleventy

[Pinned README](https://github.com/11ty/eleventy/blob/1027a84f3a4c74422e6aa0f095dd81b1513048e7/README.md)

- **Observed:** The page names the template-to-HTML transformation, installation package choices, tests, roadmap, and plugins.
- **Transfer:** Separate normal installation from maintainer tests and preserve explicit package-identity/migration information.
- **Limit:** Package names observed in this pinned revision should not be guessed from an older product name.

## ossu/computer-science

[Pinned README](https://github.com/ossu/computer-science/blob/33d44a44e3526ede8e862bf1ad50ae5ae7a2f112/README.md)

- **Observed:** The curriculum separates summary, community, prerequisites, introductory/core topics, and learning routes.
- **Transfer:** For a curriculum, expose prerequisites and sequence rather than only a resource taxonomy.
- **Limit:** A degree-style scope statement does not establish accreditation or outcomes for every learner.

## TheOdinProject/curriculum

[Pinned README](https://github.com/TheOdinProject/curriculum/blob/536cb5deb1cc967cd48c406085025b5e26d2ceaa/README.md)

- **Observed:** The introduction describes courses, lessons, and interspersed projects; contribution links target curriculum authors.
- **Transfer:** Distinguish learning through the published curriculum from editing its repository.
- **Limit:** A curriculum repository is not a runnable software application needing a package quickstart.

## freeCodeCamp/freeCodeCamp

[Pinned README](https://github.com/freeCodeCamp/freeCodeCamp/blob/9a24c29939528b76cbfb494ee1f1cca67fa9b04e/README.md)

- **Observed:** The README connects certifications and the learning platform with bug/security reporting and contribution routes.
- **Transfer:** Keep learning/certification routes separate from operating or contributing to the platform codebase.
- **Limit:** A certification description is not a guarantee of employment or individual learning outcomes.

## public-apis/public-apis

[Pinned README](https://github.com/public-apis/public-apis/blob/065455eda4bec6b61984e98b85a585851f7b8cbd/README.md)

- **Observed:** A promotional opening precedes a long category index and API tables.
- **Transfer:** Make taxonomy and meaningful per-entry access information easy to find beneath promotional material.
- **Limit:** A public API listing does not guarantee free access, unchanged terms, uptime, or permission to call it during review.
