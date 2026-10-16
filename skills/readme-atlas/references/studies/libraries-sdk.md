# Established libraries and SDK ecosystems: README studies

Study date: **2026-10-16** (Asia/Hong_Kong client date). These twelve repositories passed the **1,000 GitHub Stars minimum** at selection. Star counts below are dated observations, not a quality score.

**Compare:** Module systems, data/type boundaries, installation choices, optional sub-APIs.

This is a focused source-structure review of pinned READMEs. Observations, editorial transfers, and limits are separate; upstream commands and rendered layouts were not exercised in this pass.

| Repository | Stars at selection | README format |
| --- | ---: | --- |
| [axios/axios](#axiosaxios) | 109,302 | markdown |
| [TanStack/query](#tanstackquery) | 50,439 | markdown |
| [reduxjs/redux-toolkit](#reduxjsredux-toolkit) | 11,231 | markdown |
| [ReactiveX/rxjs](#reactivexrxjs) | 31,695 | markdown |
| [trpc/trpc](#trpctrpc) | 40,708 | markdown |
| [chalk/chalk](#chalkchalk) | 23,327 | markdown |
| [debug-js/debug](#debug-jsdebug) | 11,458 | markdown |
| [lodash/lodash](#lodashlodash) | 61,288 | markdown |
| [date-fns/date-fns](#date-fnsdate-fns) | 36,648 | markdown |
| [colinhacks/zod](#colinhackszod) | 44,136 | markdown |
| [jquense/yup](#jquenseyup) | 23,656 | markdown |
| [panva/jose](#panvajose) | 7,828 | markdown |

## axios/axios

[Pinned README](https://github.com/axios/axios/blob/326843a3902d73c9f6af9bad7b55e2412566a251/README.md)

- **Observed:** A long sponsor/maintenance opening precedes browser support, installation channels, examples, request configuration, and a detailed API.
- **Transfer:** Keep runtime/distribution choices and the first meaningful request discoverable within long library documentation.
- **Limit:** Promotional support material is not an unconditional maintenance guarantee, and a request example may contact a real service.

## TanStack/query

[Pinned README](https://github.com/TanStack/query/blob/ee47993724e5b71e65d9f38ae416367d2dd18395/README.md)

- **Observed:** The README describes fetching/caching capabilities, sends readers prominently to documentation, and lists participation and related ecosystem projects.
- **Transfer:** Use a gateway for framework-specific integration while explaining the shared data-management problem.
- **Limit:** A capability inventory does not supply the surrounding framework/provider setup or validate every adapter.

## reduxjs/redux-toolkit

[Pinned README](https://github.com/reduxjs/redux-toolkit/blob/0fd611cc79d44990ac9a040dec4d5cb446233440/packages/toolkit/README.md)

- **Observed:** The actual package README separates new-app templates from existing-app installation and explains purpose, included APIs, and optional RTK Query entry points.
- **Transfer:** Distinguish adopting a preconfigured application from integrating into existing code; label optional sub-APIs.
- **Limit:** Do not infer that every separately named feature requires another package, or that every app needs the optional query layer.

## ReactiveX/rxjs

[Pinned README](https://github.com/ReactiveX/rxjs/blob/54796b38a57e6309f9861e174737479bb3f63f61/README.md)

- **Observed:** The README identifies next-generation development, explicitly qualifies publication status, and separates preview APIs, packages, environment support, and governance.
- **Transfer:** Put package-channel availability before installation assumptions during a major-version transition.
- **Limit:** A planned version or repository package version is not evidence it has been published to the package registry.

## trpc/trpc

[Pinned README](https://github.com/trpc/trpc/blob/10e2ef98f7842b94eb3026e4f9bcfe62cc39b088/README.md)

- **Observed:** The introduction distinguishes importing server type declarations from server code; quickstart gives package-manager alternatives and ecosystem routes.
- **Transfer:** Explain which artifacts cross a client/server boundary before describing end-to-end typing.
- **Limit:** Type sharing does not establish runtime validation, deployment success, or an absence of configuration requirements.

## chalk/chalk

[Pinned README](https://github.com/chalk/chalk/blob/47fc05abd46171b235e24174cd2dba83d25bf037/readme.md)

- **Observed:** Installation flags ESM behavior; chained styling examples lead to color support, stderr handling, and style catalogs.
- **Transfer:** Place module-system and terminal-capability requirements beside the first styling example.
- **Limit:** Source-only inspection does not establish color contrast or identical output in every terminal.

## debug-js/debug

[Pinned README](https://github.com/debug-js/debug/blob/666dbc50680933bde9e7fde3a6c3241102e8f60b/README.md)

- **Observed:** Usage demonstrates namespaced output; Windows notes, Node/browser colors, wildcards, and environment variables have separate sections.
- **Transfer:** Show both instrumentation and the activation mechanism needed to observe logging.
- **Limit:** Shell-specific environment syntax should not be copied between Windows and Unix commands.

## lodash/lodash

[Pinned README](https://github.com/lodash/lodash/blob/2b5e6f7399a7b48005140b5d5c6bc6c0e62919a8/README.md)

- **Observed:** Download choices distinguish core/full builds, installation, motivations, and module formats.
- **Transfer:** Explain which artifact a user should choose before showing package/import examples.
- **Limit:** Published size figures and build differences belong to the pinned upstream distribution, not another bundle.

## date-fns/date-fns

[Pinned README](https://github.com/date-fns/date-fns/blob/717ce0a807ea4c6b540d015b5c408723175b2838/README.md)

- **Observed:** The introduction links version-related time-zone material, highlights modularity and locales, and delegates detail to documentation.
- **Transfer:** Expose consequential date/time capabilities and let readers find the corresponding maintained guide.
- **Limit:** A broad locale or timezone claim does not validate every calendar edge case or a different release.

## colinhacks/zod

[Pinned README](https://github.com/colinhacks/zod/blob/680d19f7d1e042e55934209caeb79bc843b94f44/packages/zod/README.md)

- **Observed:** The root README points to the package README; the target explains schemas, parsing, async variants, errors, and inferred input/output types.
- **Transfer:** Follow repository indirection to the real documentation and distinguish validation outcomes from static inference.
- **Limit:** An introductory placeholder object is not a self-contained success example; package and root paths must remain correctly distinguished.

## jquense/yup

[Pinned README](https://github.com/jquense/yup/blob/ff31eee8a2b10c938bb3a22544d9e33957a8cf01/README.md)

- **Observed:** Getting started separates parsing and validation, followed by schema concepts, TypeScript integration, configuration, and API detail.
- **Transfer:** Explain transformation and assertion as different reader decisions before the API catalog.
- **Limit:** A successful cast is not automatically successful validation; examples must preserve the actual schema semantics.

## panva/jose

[Pinned README](https://github.com/panva/jose/blob/b112a5e6e12f6d74124307c8fe788d4af8a2d05f/README.md)

- **Observed:** Functionality is grouped into token, key, signing, and encryption tasks, with separate runtime and version support sections.
- **Transfer:** Route users by cryptographic task and supported environment rather than an undifferentiated export list.
- **Limit:** Editorial structure does not establish secure application configuration or compatibility beyond the documented matrix.
