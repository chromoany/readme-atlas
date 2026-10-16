# Testing, linting, and formatting: README studies

Study date: **2026-10-16** (Asia/Hong_Kong client date). These twelve repositories passed the **1,000 GitHub Stars minimum** at selection. Star counts below are dated observations, not a quality score.

**Compare:** First test, transformations, configuration, contributor versus user installation.

This is a focused source-structure review of pinned READMEs. Observations, editorial transfers, and limits are separate; upstream commands and rendered layouts were not exercised in this pass.

| Repository | Stars at selection | README format |
| --- | ---: | --- |
| [pytest-dev/pytest](#pytest-devpytest) | 14,600 | restructuredtext |
| [psf/black](#psfblack) | 41,931 | markdown |
| [astral-sh/ruff](#astral-shruff) | 50,108 | markdown |
| [eslint/eslint](#eslinteslint) | 27,563 | markdown |
| [prettier/prettier](#prettierprettier) | 52,374 | markdown |
| [vitest-dev/vitest](#vitest-devvitest) | 17,241 | markdown |
| [jestjs/jest](#jestjsjest) | 45,483 | markdown |
| [microsoft/playwright](#microsoftplaywright) | 97,818 | markdown |
| [cypress-io/cypress](#cypress-iocypress) | 51,047 | markdown |
| [SeleniumHQ/selenium](#seleniumhqselenium) | 34,553 | markdown |
| [google/googletest](#googlegoogletest) | 39,645 | markdown |
| [catchorg/Catch2](#catchorgcatch2) | 21,530 | markdown |

## pytest-dev/pytest

[Pinned README](https://github.com/pytest-dev/pytest/blob/c9c19f8e62c12834ad83193a1869cc82fe9c700e/README.rst)

- **Observed:** A small-test introduction and example lead to feature explanations, documentation, issue reporting, and support routes.
- **Transfer:** Use a minimal test to reveal the testing model, then route deeper installation and tutorial material.
- **Limit:** A sample assertion is illustrative until its file and execution environment are provided.

## psf/black

[Pinned README](https://github.com/psf/black/blob/11cff1312bf96e02bce9a467d0b5a2dd65300642/README.md)

- **Observed:** Installation and usage precede formatting style, pragmatism, configuration, and contribution material.
- **Transfer:** Explain both the first command and the opinionated policy users are choosing.
- **Limit:** Formatting code is a file mutation; an audit should distinguish inspecting usage from applying the formatter.

## astral-sh/ruff

[Pinned README](https://github.com/astral-sh/ruff/blob/5fd851808b7ec109f114fac1d0996a76be464a46/README.md)

- **Observed:** Positioning and testimonials lead to getting started, multiple installation routes, usage, and configuration.
- **Transfer:** Keep linting and formatting actions distinguishable and organize setup by distribution route.
- **Limit:** Speed claims and testimonials do not replace workload evidence for another project's benchmark.

## eslint/eslint

[Pinned README](https://github.com/eslint/eslint/blob/b59d889c7c18d8c73144e6ba46e9e7f3e7da0196/README.md)

- **Observed:** Installation states prerequisites; package-manager routes lead to configuration, version support, and language/formatter FAQs.
- **Transfer:** Treat configuration and version support as adoption decisions rather than optional afterthoughts.
- **Limit:** A formatter and linter solve overlapping but different tasks; avoid implying one necessarily replaces the other.

## prettier/prettier

[Pinned README](https://github.com/prettier/prettier/blob/344d6dc42c8057fbf5573326b52dbc8a43635e7e/README.md)

- **Observed:** A short introduction uses explicit input and output before linking installation and further documentation.
- **Transfer:** For a transformation tool, show the before/after relationship directly.
- **Limit:** A formatting example demonstrates style, not semantic equivalence for arbitrary languages or inputs.

## vitest-dev/vitest

[Pinned README](https://github.com/vitest-dev/vitest/blob/7a825db43e2beca0b219d2eadaec334cb81af0c7/README.md)

- **Observed:** A Vite-based testing identity is followed by a feature inventory, sponsors, credits, and contribution links.
- **Transfer:** Explain ecosystem integration and route detailed onboarding to maintained guides.
- **Limit:** A concise feature gateway is useful only if readers can reach the actual first-test setup.

## jestjs/jest

[Pinned README](https://github.com/jestjs/jest/blob/61050e9323e742539dc2360236671110e37329e6/README.md)

- **Observed:** Getting started leads to command-line execution, configuration generation, and separate Babel, webpack, Vite, Parcel, and TypeScript guidance.
- **Transfer:** Distinguish a minimal first test from transform/bundler integration choices.
- **Limit:** A working JavaScript test does not establish support for every transpiler or module-system configuration.

## microsoft/playwright

[Pinned README](https://github.com/microsoft/playwright/blob/034f230cc68b286055186f4d9783188536f2f3cf/README.md)

- **Observed:** The page asks readers to choose a workflow, then separates testing, CLI, and agent integration with installation and examples.
- **Transfer:** Route different audiences before interleaving their commands and prerequisites.
- **Limit:** Browser automation, test-runner use, and agent integration are distinct routes, not interchangeable setup steps.

## cypress-io/cypress

[Pinned README](https://github.com/cypress-io/cypress/blob/b7e9929be2ca59de285497e20fde463624c8bb53/README.md)

- **Observed:** Browser-testing positioning leads to installing with package-manager examples, a setup animation, and contribution material.
- **Transfer:** Pair a concrete installation route with a preview when setup interaction is part of the product.
- **Limit:** An animation is not proof that the documented installation was executed on all claimed platforms.

## SeleniumHQ/selenium

[Pinned README](https://github.com/SeleniumHQ/selenium/blob/6fc1c2b932c6e115d9b83481e6f2bbc3b340d65d/README.md)

- **Observed:** The installation section explicitly describes contributor development requirements, followed by platform environments and builds.
- **Transfer:** Identify who installation instructions serve; root source instructions may be for contributors.
- **Limit:** Do not rewrite contributor prerequisites as requirements for every Selenium client-library user.

## google/googletest

[Pinned README](https://github.com/google/googletest/blob/b66cffcd5f5d6ee34a4f96d57bf016d9a22cb023/README.md)

- **Observed:** Release announcements precede getting-started links, testing features, supported platforms, related projects, and contributing.
- **Transfer:** Keep release-specific notices distinct from the stable first-test route and feature explanations.
- **Limit:** A platform list and release notice are snapshot facts, not present-day support guarantees.

## catchorg/Catch2

[Pinned README](https://github.com/catchorg/Catch2/blob/08092139210881f01a34e60c5f2fd6afa0ea4024/README.md)

- **Observed:** Concrete assertion and benchmark examples precede a v3 notice and links explaining use.
- **Transfer:** Use small examples to communicate the test vocabulary, then label major-version adoption changes.
- **Limit:** Examples from one major version should not silently become instructions for another.
