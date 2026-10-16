# Languages and build systems: README studies

Study date: **2026-10-16** (Asia/Hong_Kong client date). These twelve repositories passed the **1,000 GitHub Stars minimum** at selection. Star counts below are dated observations, not a quality score.

**Compare:** Source versus distribution, bootstrap, canonical repositories, release transitions.

This is a focused source-structure review of pinned READMEs. Observations, editorial transfers, and limits are separate; upstream commands and rendered layouts were not exercised in this pass.

| Repository | Stars at selection | README format |
| --- | ---: | --- |
| [rust-lang/rust](#rust-langrust) | 120,338 | markdown |
| [golang/go](#golanggo) | 139,217 | markdown |
| [python/cpython](#pythoncpython) | 77,587 | restructuredtext |
| [ruby/ruby](#rubyruby) | 23,780 | markdown |
| [elixir-lang/elixir](#elixir-langelixir) | 26,697 | markdown |
| [ziglang/zig](#ziglangzig) | 43,283 | markdown |
| [nim-lang/Nim](#nim-langnim) | 18,266 | markdown |
| [ocaml/ocaml](#ocamlocaml) | 6,608 | asciidoc |
| [gradle/gradle](#gradlegradle) | 18,894 | markdown |
| [apache/maven](#apachemaven) | 5,376 | markdown |
| [mesonbuild/meson](#mesonbuildmeson) | 6,648 | markdown |
| [Kitware/CMake](#kitwarecmake) | 8,126 | restructuredtext |

## rust-lang/rust

[Pinned README](https://github.com/rust-lang/rust/blob/3e014ee7cfe452be04a6b454cfb965ea3507e217/README.md)

- **Observed:** The opening identifies a compiler/tooling source tree; quick start links installation while source installation is explicitly discouraged for most readers.
- **Transfer:** State the repository's role and route ordinary users to a maintained distribution.
- **Limit:** Source-tree contents and language values do not make compiler development the normal first-use task.

## golang/go

[Pinned README](https://github.com/golang/go/blob/1eb2e040ee361fc9a59e88be13866df89a3b14b9/README.md)

- **Observed:** The page identifies the canonical source repository and separates binary installation from source installation and contribution.
- **Transfer:** Make repository authority and normal distribution paths visible.
- **Limit:** A GitHub mirror should not be described as the only or canonical source when the project identifies another location.

## python/cpython

[Pinned README](https://github.com/python/cpython/blob/21a36aa79ca0b2af49995fa1b9216b01ef98f195/README.rst)

- **Observed:** The RST title identifies a development version; using Python, contributing, building, documentation, tests, and installing multiple versions are separated.
- **Transfer:** Label development-tree identity and distinguish interpreter use from building/installing the interpreter.
- **Limit:** A development version and source build do not describe the latest stable distribution for ordinary users.

## ruby/ruby

[Pinned README](https://github.com/ruby/ruby/blob/0a1c71148a53007bd6db4658e5f074b2d390cb7c/README.md)

- **Observed:** A language overview leads to obtaining Ruby, Git downloads, source builds, documentation, community, and contribution.
- **Transfer:** Distinguish language adoption, release/source acquisition, and compiler/runtime contribution.
- **Limit:** A Git checkout should not be assumed equivalent to a supported packaged release.

## elixir-lang/elixir

[Pinned README](https://github.com/elixir-lang/elixir/blob/558215b8da28e88b90b4e73f1cfc746e624ce075/README.md)

- **Observed:** The opening routes installation/docs to the website; bug reports, feature proposals, compiling, and contribution have distinct sections.
- **Transfer:** A language-source README can prioritize contributor workflows while keeping users' installation destination clear.
- **Limit:** Reporting or proposing a feature is different from a supported release commitment.

## ziglang/zig

[Pinned README](https://github.com/ziglang/zig/blob/738d2be9d6b6ef3ff3559130c05159ef53336224/README.md)

- **Observed:** The pinned README is a migration notice linking Codeberg and explicitly stating the GitHub repository is not mirrored.
- **Transfer:** For a moved project, clearly identify the new source of truth rather than leave obsolete setup instructions.
- **Limit:** This is evidence of a documentation handoff, not a study of the current compiler's usage or development instructions.

## nim-lang/Nim

[Pinned README](https://github.com/nim-lang/Nim/blob/2a34e3109a8c8085daa5c2b451b203f6c70b26ea/readme.md)

- **Observed:** The source inventory leads to compilation guidance that distinguishes officially supported targets from less regularly tested ones, plus stable-use and build tools.
- **Transfer:** Keep support levels and stable adoption distinct from development-toolchain detail.
- **Limit:** A target that can compile is not automatically regularly tested or equally supported.

## ocaml/ocaml

[Pinned README](https://github.com/ocaml/ocaml/blob/cfa217c8955fe51d4a767c87d6a53ff0177b4ccc/README.adoc)

- **Observed:** An AsciiDoc caution explains a runtime-generation transition; overview, installation, releases, community, and separately maintained components follow.
- **Transfer:** Surface a consequential language/runtime migration before routine setup and map external components accurately.
- **Limit:** The transition notice is snapshot-specific and should not be treated as today's support schedule without refresh.

## gradle/gradle

[Pinned README](https://github.com/gradle/gradle/blob/7cb22acddadd13ae6527d6f16d1762c26a9fbf4e/README.md)

- **Observed:** Getting started routes to installation and language-specific project samples, followed by IDE/CI, learning, community, and contribution resources.
- **Transfer:** Let readers choose an application-language task while keeping build-tool development separate.
- **Limit:** A broad language list does not demonstrate every build plugin or CI integration works in a reader's environment.

## apache/maven

[Pinned README](https://github.com/apache/maven/blob/215988f2f70a7d5e4b82265752f48ea8baead9f5/README.md)

- **Observed:** A build-management overview links documentation and released distributions before a distinct quick-build contributor recipe.
- **Transfer:** Separate obtaining the build tool from compiling its own distribution.
- **Limit:** A tool's source-build recipe is not the procedure for building every project that uses it.

## mesonbuild/meson

[Pinned README](https://github.com/mesonbuild/meson/blob/ee10b5385e94fc1a0adc0b1a7c518c78c94b4d23/README.md)

- **Observed:** Dependencies and earlier-Python compatibility notes precede installation, standalone-script packaging, running, and contributor links.
- **Transfer:** Explain toolchain requirements and distinguish installing the tool from using it to configure/build another project.
- **Limit:** Pinned compatibility mappings are historical evidence and should not be transferred to an unrelated version.

## Kitware/CMake

[Pinned README](https://github.com/Kitware/CMake/blob/4d9c194536259c0a9e47146df78d2a3e9691c877/README.rst)

- **Observed:** The RST README separates building with an installed CMake from bootstrapping CMake from scratch, with platform and contribution guidance.
- **Transfer:** Explain bootstrap prerequisites when a build tool can be built by its own existing installation.
- **Limit:** Supported build-host claims do not imply every generated build system or target project is supported.
