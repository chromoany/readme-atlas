# Embedded systems and robotics: README studies

Study date: **2026-10-16** (Asia/Hong_Kong client date). These twelve repositories passed the **1,000 GitHub Stars minimum** at selection. Star counts below are dated observations, not a quality score.

**Compare:** Targets, support tiers, building versus flashing, examples versus physical operation.

This is a focused source-structure review of pinned READMEs. Observations, editorial transfers, and limits are separate; upstream commands and rendered layouts were not exercised in this pass.

| Repository | Stars at selection | README format |
| --- | ---: | --- |
| [FreeRTOS/FreeRTOS](#freertosfreertos) | 7,892 | markdown |
| [espressif/esp-idf](#espressifesp-idf) | 19,256 | markdown |
| [arduino/ArduinoCore-avr](#arduinoarduinocore-avr) | 1,512 | markdown |
| [platformio/platformio-core](#platformioplatformio-core) | 9,530 | restructuredtext |
| [micropython/micropython](#micropythonmicropython) | 22,131 | markdown |
| [RIOT-OS/RIOT](#riot-osriot) | 5,817 | markdown |
| [ARMmbed/mbed-os](#armmbedmbed-os) | 4,877 | markdown |
| [PX4/PX4-Autopilot](#px4px4-autopilot) | 12,813 | markdown |
| [ArduPilot/ardupilot](#ardupilotardupilot) | 16,076 | markdown |
| [ros2/ros2](#ros2ros2) | 6,177 | markdown |
| [petercorke/robotics-toolbox-python](#petercorkerobotics-toolbox-python) | 3,542 | markdown |
| [qemu/qemu](#qemuqemu) | 13,862 | restructuredtext |

## FreeRTOS/FreeRTOS

[Pinned README](https://github.com/FreeRTOS/FreeRTOS/blob/f4fcc3b228643144727e9257ba12db1cb632b6e6/README.md)

- **Observed:** Release information leads to getting started, repository cloning, kernel/library examples, prior releases, learning, and proof tooling.
- **Transfer:** Explain repository assembly and identify which component or demo starts the reader's task.
- **Limit:** Optional proof tools and example libraries are not automatically prerequisites for every embedded application.

## espressif/esp-idf

[Pinned README](https://github.com/espressif/esp-idf/blob/064f8278ef2030a8aef84e478acf2e2a925b5d3d/README.md)

- **Observed:** Support schedules and SoC compatibility precede environment setup, configuration, compiling, flashing, and serial-output viewing.
- **Transfer:** Treat flashing and observing device output as separate steps after a successful build.
- **Limit:** A compiled firmware image does not establish the board was flashed or the application ran.

## arduino/ArduinoCore-avr

[Pinned README](https://github.com/arduino/ArduinoCore-avr/blob/11b9130371e8447920edb65a75706a6c951e51fc/README.md)

- **Observed:** The short README identifies an AVR board platform's source/configuration role and links the platform specification.
- **Transfer:** A component repository can state its exact purpose without inventing a complete end-user IDE tutorial.
- **Limit:** A board-core source tree is not the entire Arduino distribution or support for every board family.

## platformio/platformio-core

[Pinned README](https://github.com/platformio/platformio-core/blob/ff26956ecf0cdd44f6599894f11a83a93189e07f/README.rst)

- **Observed:** The RST page separates getting started, solutions, registry, contribution, and telemetry/privacy policy.
- **Transfer:** Keep the core tool, IDE destination, package discovery, and actual telemetry policy distinguishable.
- **Limit:** A registry link is not evidence that every listed board/framework/toolchain combination was tested.

## micropython/micropython

[Pinned README](https://github.com/micropython/micropython/blob/9e348d293c58ee6d2b8a581be3a199c2b7e2f145/README.md)

- **Observed:** The overview explicitly qualifies its Python subset; setup, design values, repository layout, support tiers, cross-compiler, and dependencies follow.
- **Transfer:** Explain language/runtime differences and tiered hardware support before compatibility assumptions.
- **Limit:** Python-like syntax does not establish full CPython compatibility, and not every port has the same status.

## RIOT-OS/RIOT

[Pinned README](https://github.com/RIOT-OS/RIOT/blob/94e9c05e8e4dc682ccae40ccd8486a4ba737d313/README.md)

- **Observed:** Getting started and features lead into governance, how to ask for help, obtaining the OS, and contribution.
- **Transfer:** Make a first application and an effective support request discoverable for hardware-oriented readers.
- **Limit:** A feature inventory and help checklist do not validate a particular board image or toolchain.

## ARMmbed/mbed-os

[Pinned README](https://github.com/ARMmbed/mbed-os/blob/d723bf9e55415433e108124ee6d36337feddf1b8/README.md)

- **Observed:** Release notes and licensing are separated from developer/contributor getting-started routes, documentation, and product security considerations.
- **Transfer:** Separate building an application from contributing to its OS and preserve actual production guidance.
- **Limit:** The pinned README alone does not establish today's project maintenance status or a product's security.

## PX4/PX4-Autopilot

[Pinned README](https://github.com/PX4/PX4-Autopilot/blob/44159002d376e80d6e68cafa7054aba2a6af47fc/README.md)

- **Observed:** The page groups vehicle support, trying PX4, building, documentation, community, citation, and governance.
- **Transfer:** Let readers choose a trial or source-development route before navigating a broad robotics ecosystem.
- **Limit:** A try/demo route is not evidence of successful deployment or flight on physical hardware.

## ArduPilot/ardupilot

[Pinned README](https://github.com/ArduPilot/ardupilot/blob/8ab6afde107a91df1b5f60ade8f333cb8a61b190/README.md)

- **Observed:** Vehicle-system positioning is followed by project components, user forums, developer information, participation, and maintainers.
- **Transfer:** Distinguish user/vehicle support from firmware contribution and project governance.
- **Limit:** Broad vehicle claims do not validate every control configuration or hardware setup.

## ros2/ros2

[Pinned README](https://github.com/ros2/ros2/blob/eb184ca025af36a5968bb2111e52db5d4a2a926b/README.md)

- **Observed:** A compact ROS overview routes getting started separately from community, developer, and project resources.
- **Transfer:** A project-level gateway can organize roles rather than duplicate each package's setup.
- **Limit:** The umbrella repository is not a single package installation or proof of every robot integration.

## petercorke/robotics-toolbox-python

[Pinned README](https://github.com/petercorke/robotics-toolbox-python/blob/b4e05b4a9babb40d6d5318441bb65a2b37295053/README.md)

- **Observed:** Status, dependencies, installation choices, tutorials, and code examples frame the toolbox's robotics scope.
- **Transfer:** Place ecosystem prerequisites and meaningful example tasks near adoption.
- **Limit:** A simulation/example result should not be described as verification of physical robot operation.

## qemu/qemu

[Pinned README](https://github.com/qemu/qemu/blob/b11de76e085b64469bd9c78c20dedb6301225463/README.rst)

- **Observed:** The RST explanation distinguishes full-machine and user-space emulation and hardware virtualization, followed by builds and contribution.
- **Transfer:** Define related execution modes before showing the reader a setup route.
- **Limit:** Emulation and virtualization capabilities do not imply identical acceleration or guest support on every host.
