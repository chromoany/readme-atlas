# Web frameworks: README studies

Study date: **2026-10-16** (Asia/Hong_Kong client date). These twelve repositories passed the **1,000 GitHub Stars minimum** at selection. Star counts below are dated observations, not a quality score.

**Compare:** App scaffolding, library/framework adoption, migration, help routes.

This is a focused source-structure review of pinned READMEs. Observations, editorial transfers, and limits are separate; upstream commands and rendered layouts were not exercised in this pass.

| Repository | Stars at selection | README format |
| --- | ---: | --- |
| [django/django](#djangodjango) | 91,345 | restructuredtext |
| [pallets/flask](#palletsflask) | 74,910 | markdown |
| [encode/starlette](#encodestarlette) | 12,665 | markdown |
| [expressjs/express](#expressjsexpress) | 69,571 | markdown |
| [honojs/hono](#honojshono) | 32,551 | markdown |
| [nestjs/nest](#nestjsnest) | 76,854 | markdown |
| [sveltejs/svelte](#sveltejssvelte) | 88,384 | markdown |
| [angular/angular](#angularangular) | 101,061 | markdown |
| [vercel/next.js](#vercelnextjs) | 143,027 | markdown |
| [nuxt/nuxt](#nuxtnuxt) | 60,954 | markdown |
| [withastro/astro](#withastroastro) | 63,263 | markdown |
| [remix-run/react-router](#remix-runreact-router) | 56,614 | markdown |

## django/django

[Pinned README](https://github.com/django/django/blob/d430084791a61b31cecec132bce3dca19194f7f2/README.rst)

- **Observed:** The RST introduction recommends an ordered documentation route: installation, numbered tutorials, deployment guidance, and building the docs.
- **Transfer:** For a mature framework, preserve a recommended learning sequence and separate deployment from introductory study.
- **Limit:** A linked tutorial sequence is a gateway, not evidence that deployment was executed in this study.

## pallets/flask

[Pinned README](https://github.com/pallets/flask/blob/d086db856be187255b8ec61ef409357393020f32/README.md)

- **Observed:** A lightweight-framework explanation leads quickly to a small named-file web example, followed by donation and contribution material.
- **Transfer:** Let a compact example expose the programming model before extensive ecosystem detail.
- **Limit:** An intentionally flexible framework does not supply every production or application-structure decision automatically.

## encode/starlette

[Pinned README](https://github.com/encode/starlette/blob/7b2948fe7b7fff28bb018607d54cd4dfa518910e/README.md)

- **Observed:** Installation explicitly calls for an ASGI server; examples lead into optional dependencies and framework-versus-toolkit modularity.
- **Transfer:** Name companion runtime requirements and distinguish optional capabilities from the core installation.
- **Limit:** Installing the library alone does not necessarily start an HTTP server or enable every optional feature.

## expressjs/express

[Pinned README](https://github.com/expressjs/express/blob/a419aa7350389a275ab45fde2e849ed1f02449ef/Readme.md)

- **Observed:** Node prerequisites and installation are separated from quick start, examples, philosophy, contribution, and tests.
- **Transfer:** Make runtime prerequisites explicit and keep users' first application distinct from framework-development validation.
- **Limit:** Contributor tests and community positioning are not proof of the reader's production application behavior.

## honojs/hono

[Pinned README](https://github.com/honojs/hono/blob/3362244401515a1530616aefb87eb388152f82a3/README.md)

- **Observed:** A route-handler example precedes a project-creation quickstart, features, documentation, migration, and contribution.
- **Transfer:** Explain the abstraction briefly and route users to runtime-specific scaffolding and migration guidance.
- **Limit:** A listed runtime family does not establish every adapter/version combination or an independent server start command.

## nestjs/nest

[Pinned README](https://github.com/nestjs/nest/blob/1c2f689518412cbc6a6bc09662dd5cfed779f2bf/Readme.md)

- **Observed:** Description and philosophy lead to getting started; questions are routed separately from issue reporting, observability, and consulting.
- **Transfer:** Label help channels by purpose so support requests and reproducible bugs reach the intended destination.
- **Limit:** Community and commercial support routes should not be presented as equivalent promises.

## sveltejs/svelte

[Pinned README](https://github.com/sveltejs/svelte/blob/40bb08482f4857d91221638dec544a532bc35389/README.md)

- **Observed:** The compact README explains a compiler-based model and delegates learning to the website; roadmap and contribution follow.
- **Transfer:** Explain the distinguishing abstraction and use a maintained documentation gateway instead of duplicating a full app tutorial.
- **Limit:** A compiler explanation does not by itself create a working project or validate performance claims.

## angular/angular

[Pinned README](https://github.com/angular/angular/blob/92e5aa8f154096a756757d0e295cde4299788650/README.md)

- **Observed:** Documentation topics and local-development links lead to prerequisites, CLI project setup, quickstart, ecosystem, and upgrading.
- **Transfer:** Separate creating an application, learning features, upgrading, and contributing to the framework.
- **Limit:** An ecosystem list and generated-project route do not verify every integration or upgrade path.

## vercel/next.js

[Pinned README](https://github.com/vercel/next.js/blob/a6d4c15991fd2f69c14eea4e8b655b596bc162bf/packages/next/README.md)

- **Observed:** The root README points to the package README, whose getting-started section links a course and showcase before docs, community, contribution, and security.
- **Transfer:** Follow the actual package-level entry document and separate learning, examples, and contributor routes.
- **Limit:** A showcase or promotional build claim is not evidence of a user's first successful local build.

## nuxt/nuxt

[Pinned README](https://github.com/nuxt/nuxt/blob/f1d555065d13353e520b390e10972cd24cca7e00/README.md)

- **Observed:** A feature explanation and index lead to getting started, an app.vue example, docs, modules, contributor development, and professional support.
- **Transfer:** Distinguish authoring an application from extending modules or developing the framework.
- **Limit:** A rendering/deployment feature list does not establish all providers work without their documented configuration.

## withastro/astro

[Pinned README](https://github.com/withastro/astro/blob/c2c43a99f4d50676456c137ff88359579f78bf5c/README.md)

- **Observed:** Installation explicitly distinguishes the recommended scaffold from manual package installation, then offers starter previews, docs, and a directory map.
- **Transfer:** Label the recommended adoption path and leave manual setup as a clearly separate alternative.
- **Limit:** A bare package install is not automatically equivalent to a generated working site.

## remix-run/react-router

[Pinned README](https://github.com/remix-run/react-router/blob/9da0ec9f3e68053d8deb6c6ee4a8d36f809f9335/README.md)

- **Observed:** The short README offers separate framework and library starting routes, a package inventory, and previous-version guidance.
- **Transfer:** Route readers by level of adoption before listing monorepo packages.
- **Limit:** Choosing the library route should not silently inherit framework scaffolding or deployment assumptions.
