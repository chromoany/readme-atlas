# Creative and desktop software: README studies

Study date: **2026-10-16** (Asia/Hong_Kong client date). These twelve repositories passed the **1,000 GitHub Stars minimum** at selection. Star counts below are dated observations, not a quality score.

**Compare:** Downloads versus building, development-tree status, target users, media workflows.

This is a focused source-structure review of pinned READMEs. Observations, editorial transfers, and limits are separate; upstream commands and rendered layouts were not exercised in this pass.

| Repository | Stars at selection | README format |
| --- | ---: | --- |
| [blender/blender](#blenderblender) | 20,938 | markdown |
| [GNOME/gimp](#gnomegimp) | 6,517 | text |
| [obsproject/obs-studio](#obsprojectobs-studio) | 77,602 | restructuredtext |
| [audacity/audacity](#audacityaudacity) | 18,747 | markdown |
| [mltframework/shotcut](#mltframeworkshotcut) | 15,432 | markdown |
| [KDE/kdenlive](#kdekdenlive) | 5,871 | markdown |
| [darktable-org/darktable](#darktable-orgdarktable) | 13,281 | markdown |
| [RawTherapee/RawTherapee](#rawtherapeerawtherapee) | 4,230 | markdown |
| [FreeCAD/FreeCAD](#freecadfreecad) | 34,344 | markdown |
| [prusa3d/PrusaSlicer](#prusa3dprusaslicer) | 9,412 | markdown |
| [openscad/openscad](#openscadopenscad) | 10,455 | markdown |
| [KDE/krita](#kdekrita) | 10,551 | markdown |

## blender/blender

[Pinned README](https://github.com/blender/blender/blob/e2e58a974edb3a5e949aa273d7ff940b5c5797c8/README.md)

- **Observed:** The source README explicitly points to a separate end-user readme and keeps project, development, and license destinations concise.
- **Transfer:** A source repository can state its role and route users to a more suitable product entry point.
- **Limit:** Absence of inline end-user setup is not automatically a defect when a maintained destination is supplied.

## GNOME/gimp

[Pinned README](https://github.com/GNOME/gimp/blob/d8d30252dd7b3dace58233a1b8cfc87cabcd1a63/README)

- **Observed:** The plain-text page identifies a development branch and groups web resources, contributing, discussion, and customization.
- **Transfer:** Make development-tree status and user-help destinations clear without requiring a graphic-heavy header.
- **Limit:** A development-branch identity does not establish that readers are using the stable application.

## obsproject/obs-studio

[Pinned README](https://github.com/obsproject/obs-studio/blob/1ad6110186096e0bef0c269120fd14f7b6d4b183/README.rst)

- **Observed:** The RST page explains capturing/recording/streaming, then gives quick links and contribution routes; translations have a specific channel.
- **Transfer:** Differentiate using the application, building it, contributing code, and contributing translations.
- **Limit:** Do not route translation contributions through ordinary code pull requests when the project specifies another workflow.

## audacity/audacity

[Pinned README](https://github.com/audacity/audacity/blob/b482a5e3ee5443c0a438908aaf1caf09250171a9/README.md)

- **Observed:** A compact application description is followed by an explicit major-structural-change notice and license link.
- **Transfer:** Expose consequential repository transitions before readers follow developer assumptions.
- **Limit:** A structural-change notice is a pinned maintainer statement; it does not prove a release is finished or unavailable.

## mltframework/shotcut

[Pinned README](https://github.com/mltframework/shotcut/blob/4078c6b9795331a9b70e06d78ef06186d331a770/README.md)

- **Observed:** Installation links are separate from dependencies and detailed build instructions, with a warning that builds target testers/contributors.
- **Transfer:** Lead users to the distribution and reserve source-build detail for the intended technical audience.
- **Limit:** A build warning belongs to this project; do not copy it into every desktop README.

## KDE/kdenlive

[Pinned README](https://github.com/KDE/kdenlive/blob/d10b2ccb41ba567c371a3d698763dfe6c1079705/README.md)

- **Observed:** A product explanation links the main site, then devotes sections to contribution, technology stack, and developer setup.
- **Transfer:** Let the repository serve contributors while keeping the user's product destination visible.
- **Limit:** A technology-stack section does not teach a first editing task or validate product claims.

## darktable-org/darktable

[Pinned README](https://github.com/darktable-org/darktable/blob/976fdb2d0c5f4cd936ab03e4a8bc9b32fd5b8d97/README.md)

- **Observed:** The page separates platform/hardware requirements, optional AI features, release versus development installation, upgrades, and troubleshooting.
- **Transfer:** Keep optional features and migration requirements distinct from basic installation.
- **Limit:** Source inspection cannot validate camera/lens compatibility, upgraded data, or every acceleration path.

## RawTherapee/RawTherapee

[Pinned README](https://github.com/RawTherapee/RawTherapee/blob/b2ee504c47e5e6d5e054395aa12bf1fe43bd1c3c/README.md)

- **Observed:** A preview and explicit target-audience section lead to resource links and compilation/branch guidance.
- **Transfer:** Name the creative workflow and intended input types before source-development detail.
- **Limit:** A preview does not prove compatibility with all camera formats or establish rendering quality.

## FreeCAD/FreeCAD

[Pinned README](https://github.com/FreeCAD/FreeCAD/blob/4a1904f8db57d4a31e44cdb1dd984d4c98447c10/README.md)

- **Observed:** An overview leads to installation, compiling, reporting issues, and usage/help sections.
- **Transfer:** Distinguish obtaining the modeler, developing it, and requesting help with an actual modeling task.
- **Limit:** A successful installation is not a completed parametric-model workflow or proof of format interoperability.

## prusa3d/PrusaSlicer

[Pinned README](https://github.com/prusa3d/PrusaSlicer/blob/30ef59195e0f3ee6f270b185bb5f9fb5f349f81f/README.md)

- **Observed:** The opening explains model-to-print instructions; installation, features, bug reporting, and technical stack are separated.
- **Transfer:** Explain the input/output workflow and identify where end-user setup differs from building the application.
- **Limit:** Printer-family support statements do not prove every machine/profile combination has been tested.

## openscad/openscad

[Pinned README](https://github.com/openscad/openscad/blob/5a864f17b6b022904004704f64e6168d2cfb8435/README.md)

- **Observed:** The introduction explicitly distinguishes script-driven solid modeling from an interactive modeler; getting started precedes extensive platform builds.
- **Transfer:** Clarify the interaction model early so readers can decide whether the tool fits.
- **Limit:** A CAD label alone does not imply a graphical direct-manipulation workflow.

## KDE/krita

[Pinned README](https://github.com/KDE/krita/blob/ed1d147e96795a379620b4ea1054976ec1d4fca4/README.md)

- **Observed:** User manual and developer builds are separate; repository status and nightly build categories are explicitly labeled.
- **Transfer:** Distinguish user documentation, stable/unstable artifacts, and contributor builds.
- **Limit:** Do not infer a project's present maintenance or contribution policies from an older pinned file.
