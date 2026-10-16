# Scientific computing and ML: README studies

Study date: **2026-10-16** (Asia/Hong_Kong client date). These twelve repositories passed the **1,000 GitHub Stars minimum** at selection. Star counts below are dated observations, not a quality score.

**Compare:** Optional dependencies, artifacts, reproducible interactions, serving and citation.

This is a focused source-structure review of pinned READMEs. Observations, editorial transfers, and limits are separate; upstream commands and rendered layouts were not exercised in this pass.

| Repository | Stars at selection | README format |
| --- | ---: | --- |
| [scipy/scipy](#scipyscipy) | 15,115 | restructuredtext |
| [pandas-dev/pandas](#pandas-devpandas) | 50,074 | markdown |
| [matplotlib/matplotlib](#matplotlibmatplotlib) | 23,374 | markdown |
| [sympy/sympy](#sympysympy) | 15,017 | markdown |
| [scikit-image/scikit-image](#scikit-imagescikit-image) | 6,613 | markdown |
| [dask/dask](#daskdask) | 13,935 | restructuredtext |
| [apache/spark](#apachespark) | 44,217 | markdown |
| [huggingface/datasets](#huggingfacedatasets) | 22,060 | markdown |
| [vllm-project/vllm](#vllm-projectvllm) | 93,889 | markdown |
| [ggml-org/llama.cpp](#ggml-orgllamacpp) | 131,331 | markdown |
| [mlflow/mlflow](#mlflowmlflow) | 28,404 | markdown |
| [ray-project/ray](#ray-projectray) | 44,037 | restructuredtext |

## scipy/scipy

[Pinned README](https://github.com/scipy/scipy/blob/8456d92b303e3c7f77fec07c6cf3c14593ee68b3/README.rst)

- **Observed:** An RST scientific-computing introduction links documentation, distribution resources, security reporting, and contributions.
- **Transfer:** A mature scientific foundation can use a compact gateway with labeled support and adoption destinations.
- **Limit:** A package overview does not validate numerical accuracy for a particular scientific workload.

## pandas-dev/pandas

[Pinned README](https://github.com/pandas-dev/pandas/blob/8eded316d50e33cc6e0e57bc596b4ba4d6923ff8/README.md)

- **Observed:** Capabilities lead to released binaries, dependencies, source installation, documentation, help, and contribution.
- **Transfer:** Separate ordinary data-analysis use from source-build requirements.
- **Limit:** A capability list is not a reproducible data-analysis example without supplied data and expected behavior.

## matplotlib/matplotlib

[Pinned README](https://github.com/matplotlib/matplotlib/blob/003c1b52dea2208eade88b74af997b1b065de324/README.md)

- **Observed:** Installation delegates to maintained documentation and identifies its source; contribution, contact, and citation follow.
- **Transfer:** Keep installation instructions traceable to their maintained source and preserve supplied citation guidance.
- **Limit:** A plotting library README is not evidence that any particular chart or renderer was tested.

## sympy/sympy

[Pinned README](https://github.com/sympy/sympy/blob/9350380769d772f6fb320052214afc2d488a41a3/README.md)

- **Observed:** Download and documentation routes lead to installation, contribution, tests, experimental parser regeneration, and citation.
- **Transfer:** Separate ordinary symbolic use from developer and experimental-tool maintenance.
- **Limit:** An experimental parser recipe should not be presented as a universal runtime prerequisite.

## scikit-image/scikit-image

[Pinned README](https://github.com/scikit-image/scikit-image/blob/b700edc8005e4ee9e74fc83259f09e8df3213f15/README.md)

- **Observed:** A compact page gives documentation and help links, installation, licensing, and citation.
- **Transfer:** A small scientific gateway can prioritize authoritative install and usage resources over a long feature catalog.
- **Limit:** A citation destination and package install do not establish correctness for a medical or scientific application.

## dask/dask

[Pinned README](https://github.com/dask/dask/blob/6ce3740fa79bfa051ecc74c3641f8c6a46dfdc30/README.rst)

- **Observed:** A very short RST README identifies parallel analytics and delegates to documentation, with license/contribution destinations.
- **Transfer:** Allow a concise gateway when detailed onboarding is maintained elsewhere.
- **Limit:** Shortness alone does not show whether the destination covers the reader's scheduler and environment.

## apache/spark

[Pinned README](https://github.com/apache/spark/blob/a98f67abf9367d2ece88a1242f2979e5564b9e55/README.md)

- **Observed:** Basic setup distinguishes building, interactive Scala/Python shells, example programs, tests, Hadoop-version notes, and configuration.
- **Transfer:** Offer language-specific first interactions while separating build/test and deployment compatibility.
- **Limit:** A local shell example does not validate distributed cluster operation or every Hadoop combination.

## huggingface/datasets

[Pinned README](https://github.com/huggingface/datasets/blob/04737492628dcecf91bff9f6c6cad463194c637e/README.md)

- **Observed:** Installation separates optional modality/framework dependencies; quickstart loads and transforms a dataset.
- **Transfer:** Show the smallest data workflow and identify extra dependencies only for the tasks that need them.
- **Limit:** Code licensing does not automatically cover all downloaded datasets or guarantee network/access availability.

## vllm-project/vllm

[Pinned README](https://github.com/vllm-project/vllm/blob/92dc3dd39332bd8cfe7993d92dbff288e46db8e4/README.md)

- **Observed:** Serving capabilities lead to getting-started links, contribution, citation, and contact; hardware support is described separately.
- **Transfer:** Route serving users to environment-specific onboarding while keeping citation and contributor needs secondary.
- **Limit:** A hardware-family list does not establish every model/backend/version combination or the claimed throughput.

## ggml-org/llama.cpp

[Pinned README](https://github.com/ggml-org/llama.cpp/blob/5e03a1ff450cae37a774684de55d14fb48b1f90b/README.md)

- **Observed:** Quickstart distinguishes shell installers, model download/run, API serving, supported backends, and developer tools.
- **Transfer:** Separate obtaining the runtime, obtaining an artifact, and selecting the first interaction.
- **Limit:** An inference command can download substantial model data; source review does not execute or validate it.

## mlflow/mlflow

[Pinned README](https://github.com/mlflow/mlflow/blob/f3a075eccdfead4827dd217cca9a71dfa782d341/README.md)

- **Observed:** A short getting-started route leads to LLM/agent tasks, model training, language/framework integrations, and hosting choices.
- **Transfer:** Separate the main workflow from the broad integration catalog and identify the deployment route.
- **Limit:** An integration listing or guided wizard is not evidence of every provider's availability or cost.

## ray-project/ray

[Pinned README](https://github.com/ray-project/ray/blob/3e2f0b5c2aa2caa01cf6c08268325bb9a9c62048/README.rst)

- **Observed:** The RST introduction distinguishes a core distributed runtime and AI libraries, then gives installation and participation routes.
- **Transfer:** Explain the framework's layers before readers choose an application-specific entry point.
- **Limit:** Installing the core package does not imply every optional AI library or cluster dependency is present.
