# Data systems and formats: README studies

Study date: **2026-10-16** (Asia/Hong_Kong client date). These twelve repositories passed the **1,000 GitHub Stars minimum** at selection. Star counts below are dated observations, not a quality score.

**Compare:** Server/client interaction, formats versus products, trials versus clusters.

This is a focused source-structure review of pinned READMEs. Observations, editorial transfers, and limits are separate; upstream commands and rendered layouts were not exercised in this pass.

| Repository | Stars at selection | README format |
| --- | ---: | --- |
| [valkey-io/valkey](#valkey-iovalkey) | 27,440 | markdown |
| [duckdb/duckdb](#duckdbduckdb) | 42,191 | markdown |
| [apache/arrow](#apachearrow) | 17,208 | markdown |
| [apache/parquet-format](#apacheparquet-format) | 2,617 | markdown |
| [apache/kafka](#apachekafka) | 33,973 | markdown |
| [nats-io/nats-server](#nats-ionats-server) | 20,881 | markdown |
| [rabbitmq/rabbitmq-server](#rabbitmqrabbitmq-server) | 13,928 | markdown |
| [ClickHouse/ClickHouse](#clickhouseclickhouse) | 50,442 | markdown |
| [seaweedfs/seaweedfs](#seaweedfsseaweedfs) | 35,509 | markdown |
| [apache/cassandra](#apachecassandra) | 10,123 | asciidoc |
| [etcd-io/etcd](#etcd-ioetcd) | 52,368 | markdown |
| [tikv/tikv](#tikvtikv) | 16,908 | markdown |

## valkey-io/valkey

[Pinned README](https://github.com/valkey-io/valkey/blob/035b8d61d0e8fc3558e566ec76088c07562b080c/README.md)

- **Observed:** The quick-start source README expands into build options, allocator/platform details, running, TLS, RDMA, and interaction.
- **Transfer:** Separate optional transport/build capabilities from the smallest server-use route.
- **Limit:** Optional build flags and best-effort platform notes do not imply identical support in every binary distribution.

## duckdb/duckdb

[Pinned README](https://github.com/duckdb/duckdb/blob/e08224d653fcade680e471709e9a9035223989df/README.md)

- **Observed:** A compact installation gateway is followed by CSV/Parquet SQL examples and distinct development/build instructions.
- **Transfer:** Show a concrete data interaction without making source compilation the default adoption route.
- **Limit:** The example references user-supplied files; it is not independently runnable without creating or identifying them.

## apache/arrow

[Pinned README](https://github.com/apache/arrow/blob/740237e342c647967279abf6b36f2e2fafe46181/README.md)

- **Observed:** The page explains in-memory analytics and library capabilities, then links implementation status and contribution paths.
- **Transfer:** A multi-language foundation should expose implementation status rather than imply universal feature parity.
- **Limit:** A format's scope does not prove that every language binding implements every feature.

## apache/parquet-format

[Pinned README](https://github.com/apache/parquet-format/blob/53b8bd8576827080d4382fa457003f45b41cda6e/README.md)

- **Observed:** The README moves from motivation and modules into building, glossary, parallelization, file layout, types, and encodings.
- **Transfer:** For a specification repository, make concepts and format navigation the primary product.
- **Limit:** A format description is not an installer or a runtime library; do not force package onboarding onto it.

## apache/kafka

[Pinned README](https://github.com/apache/kafka/blob/f7a6dfe076929c3b761bfb9fbb97f786ff9503e8/README.md)

- **Observed:** The source README foregrounds build artifacts, documentation generation, unit/integration tests, and contributor commands while linking the user quickstart.
- **Transfer:** Label a source-tree workflow so users do not confuse building the project with operating a broker.
- **Limit:** Contributor test commands and source prerequisites are not the complete deployment procedure.

## nats-io/nats-server

[Pinned README](https://github.com/nats-io/nats-server/blob/b55d969381aa05a7a59c563797b454d1b6b5fa37/README.md)

- **Observed:** A communications-system explanation leads to documentation, contact, contribution, roadmap, and security-reporting destinations.
- **Transfer:** A concise server gateway can route adoption, contribution, and private security reporting distinctly.
- **Limit:** A linked audit is scoped evidence, not a blanket guarantee that a deployment is secure.

## rabbitmq/rabbitmq-server

[Pinned README](https://github.com/rabbitmq/rabbitmq-server/blob/031917f8db4ef2f4f79b055294ce4847b9083e9a/README.md)

- **Observed:** Installation links supported series and platform guides; tutorials, commercial support, community help, licensing, and source packaging are separate.
- **Transfer:** Distinguish release eligibility, learning, operational help, and building the broker.
- **Limit:** Commercial capabilities and community eligibility should not be silently merged into the open-source feature list.

## ClickHouse/ClickHouse

[Pinned README](https://github.com/ClickHouse/ClickHouse/blob/a21868cbdc79ca11850fc2eb5755e79dc4832600/README.md)

- **Observed:** A short installation section offers a separate hosted route; useful links, community calls, and dated events follow.
- **Transfer:** Label local and hosted adoption choices clearly and keep time-sensitive community material secondary.
- **Limit:** A hosted offer or event date in a pinned README is not a current pricing or availability guarantee.

## seaweedfs/seaweedfs

[Pinned README](https://github.com/seaweedfs/seaweedfs/blob/e6cf190596e77333e8c9b765e5999a7c1697cb8a/README.md)

- **Observed:** Quick start has one-command, Docker, Compose, Helm, source-build, and scale-out routes before detailed positioning.
- **Transfer:** Make a multi-component system's simplest trial continuous and label substantial deployment alternatives.
- **Limit:** One quick-start process does not establish a production-scale, durable storage deployment.

## apache/cassandra

[Pinned README](https://github.com/apache/cassandra/blob/275a3a5143959427d65ff4344de279ab55b31112/README.asc)

- **Observed:** The AsciiDoc README connects a one-node server startup to an interactive CQL session, table creation, insertion, and visible query output.
- **Transfer:** A database quickstart should complete a small write/read loop and identify where the client runs.
- **Limit:** A one-node example is not a production cluster, and displayed snapshot output is not freshly executed evidence.

## etcd-io/etcd

[Pinned README](https://github.com/etcd-io/etcd/blob/f22475263b89fbc231e1589839427c354bcf237c/README.md)

- **Observed:** An early main-branch warning precedes getting started, running, TCP ports, local clustering, and client setup.
- **Transfer:** Distinguish stable releases from development and connect server startup to client interaction.
- **Limit:** A local cluster and example ports do not validate production resilience or arbitrary network exposure.

## tikv/tikv

[Pinned README](https://github.com/tikv/tikv/blob/67ffce0c137b7c171405a76df8bc8e9f04a19ce6/README.md)

- **Observed:** A software-stack explanation leads to playground, binary, Docker Compose, cluster, and source-build choices.
- **Transfer:** Differentiate an exploratory playground from a deployed cluster and explain required components.
- **Limit:** A convenient playground should not be described as proof of production readiness or all transaction claims.
