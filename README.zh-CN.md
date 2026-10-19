<div align="center">

<img src="assets/readme-atlas-header.png" alt="README Atlas：由路径与罗盘串联的文档插画" width="960">

# README Atlas

**让每个项目都有一条从“看懂”到“用起来”的清晰路线。**

[English](README.md) · [简体中文](README.zh-CN.md)

[![许可证：MIT](https://img.shields.io/badge/License-MIT-35b6bd?style=flat-square)](LICENSE)
[![Codex agent skill](https://img.shields.io/badge/Codex-Agent%20Skill-35b6bd?style=flat-square)](skills/readme-atlas/SKILL.md)

</div>

一个用于**新建、改写、审查和翻译项目 README** 的 agent skill。结合仓库实际内容与 200 个项目的研究，指导准确的内容、清晰的首次使用路线和协调的视觉呈现。

[安装](#安装到-codex) · [第一次使用](#第一次使用) · [改写示例](#看一个改写示例) · [研究与边界](#研究与结论)

## 安装到 Codex

克隆仓库，然后把 **完整的** `skills/readme-atlas` 文件夹复制到用户技能目录。克隆需要 Git；使用 skill 不需要安装 Python 包、提供 API Key 或额外运行时依赖。如果目标技能目录已存在，请先检查再决定是否替换。

**macOS / Linux（Bash）：**

```bash
git clone https://github.com/chromoany/readme-atlas.git
cd readme-atlas
mkdir -p "$HOME/.agents/skills"
cp -R skills/readme-atlas "$HOME/.agents/skills/"
```

**Windows（PowerShell）：**

```powershell
git clone https://github.com/chromoany/readme-atlas.git
Set-Location readme-atlas
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse .\skills\readme-atlas "$HOME\.agents\skills\"
```

如果仅给一个项目使用，则复制到该项目的 `.agents/skills/readme-atlas`。这些路径来自 [Codex 官方技能文档](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)。如果安装后没有出现，请重启 Codex。

## 第一次使用

在 Codex 中打开要编写 README 的项目，发送：

```text
使用 $readme-atlas，检查当前仓库并编写中文 README.md。
目标读者是第一次尝试这个项目的开发者。
所有命令和功能描述都以仓库实际内容为依据。
```

预期产物是适合当前项目的 `README.md`，以及简短的验证说明和未解决事实。agent 先检查仓库，再决定内容与章节。

<details>
<summary>更多使用方式</summary>

**改进已有 README**

```text
使用 $readme-atlas 改进现有 README，保留有用的锚点，
重点补全从安装到第一次成功运行的步骤。
```

**只审查，不修改**

```text
使用 $readme-atlas 审查 README.md，不修改文件。
优先指出会让新用户无法开始使用的问题，并给出证据和最小修正建议。
```

**整理视觉呈现**

```text
使用 $readme-atlas 美化现有 README。
改进首屏、徽章一致性、效果预览、留白和导航，
保留准确命令与项目原有的品牌风格。
```

**翻译 README**

```text
使用 $readme-atlas 将 README.md 翻译为 README.zh-CN.md。
保持命令、要求和功能状态一致，并添加双向语言入口。
```

</details>

## 看一个改写示例

下面是使用本仓库作者编写的 Log Slice 演示脚本制作的手工改写案例。

**改写前——故意写错的草稿：**

> 用 `pip install logslice` 安装已发布的包，然后运行 `logslice`。

**改写后——本地脚本，需要 Python 3.10+：**

从本仓库根目录执行：

```bash
cd examples/fixtures/log-slice
python logslice.py sample.log --level ERROR
```

预期输出：

```text
ERROR database unavailable
```

改写将没有依据的包安装说明替换为实际命令、必需输入和可识别的结果。[查看完整改写案例](examples/cli-rewrite.md)。

这是用于说明方法的手工案例，不是对 skill 的独立效果评测。

## 它如何工作

| 你的任务 | README Atlas 指导 agent 做什么 |
| --- | --- |
| 新建 | 检查仓库、明确读者，并选择有用的首次使用路线 |
| 改写 | 保留准确内容和有用锚点，补齐说明、命令与呈现上的缺口 |
| 审查 | 给出有证据的问题与修正建议；仅审查时不修改文件 |
| 翻译 | 保持各语言版本的命令、链接、要求和功能状态一致 |

视觉指南覆盖首屏、徽章集中排版、效果预览、留白、导航和深浅色可读性。结构跟着项目走：库需要输入输出示例，平台需要部署选择，学习资源需要阅读起点。

skill 由 Markdown 指令、按需读取的参考资料和 Codex 界面元数据组成。目前提供 **Codex** 的安装与调用说明；其他 agent 可以阅读这些指令，但其安装与调用行为尚未在本项目验证。

## 研究与结论

README Atlas 参考了 **200 份固定提交版本的 README**。每项研究分别记录观察到的做法、可借鉴的写作决策，以及适用边界。

| 研究依据 | 范围 |
| --- | --- |
| README 研究 | 32 项详细案例，以及按 14 个领域分组的 168 项重点结构研究 |
| 视觉研究 | 13 个案例，覆盖品牌、预览、文字层级、导航等选择 |
| 来源记录 | 固定提交链接、原文路径、SHA-256 与带日期的筛选记录 |

样本覆盖库、CLI、应用、基础设施、科学计算、嵌入式、学习资源和内容归档，包含 Markdown、RST、AsciiDoc 和纯文本。可从[研究索引](skills/readme-atlas/references/source-study.md#study-index)进入；[研究方法](research/README.md)解释了选样方式和研究深度。

在 **2026-10-16** 核验时，200 个仓库均有至少 **1,000 GitHub Star**。这是研究样本的筛选规则，不是 README 质量评分，也不是使用此 skill 的项目需要达到的门槛。详见[筛选证据](research/selection.json)和[来源清单](research/sources.json)。

这些属于**定性写作研究**，不能证明某种排版导致项目受欢迎或采用率提升。13 个视觉案例的源码与实际渲染检查深度不同，研究集不等于统一的视觉审计。目前没有独立 skill 效果评测或转化率测量。[验证记录](research/VALIDATION.md)区分了已执行检查、手工审查和尚未验证的行为。

## 继续阅读与贡献

- [各类项目的读者路线](skills/readme-atlas/references/patterns.md)
- [视觉设计方法与来源观察](skills/readme-atlas/references/visual-design.md)
- [审查清单](skills/readme-atlas/references/review-checklist.md)
- [完整改写示例](examples/cli-rewrite.md)
- [研究方法与来源校验](research/README.md)
- [研究集验证记录](research/VALIDATION.md)
- [贡献指南](CONTRIBUTING.md)

发现问题或希望改进时，可以[提交 Issue](https://github.com/chromoany/readme-atlas/issues)，附上对应文件和具体例子。贡献应解决真实读者的需求，并保持中英文 README 一致。

## 许可证

作者：[chromoany](https://github.com/chromoany)。

本仓库原创指令、分析、示例及工具采用 [MIT](LICENSE) 许可证。引用项目保留各自许可证；本仓库提供原文链接，不重新分发其 README。
