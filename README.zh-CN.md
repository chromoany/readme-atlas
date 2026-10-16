# README Atlas

**让每个项目都有一条从“看懂”到“用起来”的清晰路线。**

一个用于新建、改写和审查项目 README 的 agent skill，同时关注上手体验与视觉呈现。研究了 **200 个认可度较高的软件与内容项目**的 README，选样时每个仓库均有 **至少 1,000 GitHub Star**，并将观察提炼为按项目类型选择的写作方法：库需要输入输出示例，平台需要部署路线，知识库需要阅读起点。视觉指南覆盖品牌识别、布局、徽章、效果预览和深浅色可读性。

[English](README.md) · [Skill 正文](skills/readme-atlas/SKILL.md) · [逐项目研究](skills/readme-atlas/references/source-study.md)

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

预期产物是适合当前项目的 `README.md`，以及简短的验证说明和未解决事实。skill 要求先检查项目，再决定写什么、如何组织。

也可以这样使用：

```text
使用 $readme-atlas 改进现有 README，保留有用的锚点，
重点补全从安装到第一次成功运行的步骤。
```

```text
使用 $readme-atlas 审查 README.md，不修改文件。
优先指出会让新用户无法开始使用的问题，并给出证据和最小修正建议。
```

```text
使用 $readme-atlas 美化现有 README。
改进首屏、徽章一致性、效果预览、留白和导航，
保留准确命令与项目原有的品牌风格。
```

```text
使用 $readme-atlas 将 README.md 翻译为 README.zh-CN.md。
保持命令、要求和功能状态一致，并添加双向语言入口。
```

## 它如何工作

| 写作决策 | 方法 |
| --- | --- |
| 哪些内容可信 | 检查配置、接口、示例、测试、文档和许可证 |
| 首先呈现什么 | 找到目标读者最小且有意义的成功结果 |
| 选择什么结构 | 根据库、CLI、应用、平台、系统与嵌入式、科学计算环境、ML、资源库、内容归档、规范与交换格式或 skill 调整 |
| 如何呈现得好看 | 选择协调的视觉方向，设计首屏、徽章、配图与阅读节奏 |
| 哪些内容不写 | 删除无依据的承诺和没有读者用途的章节 |
| 如何验证 | 核对命令、检查链接，条件允许时执行首次使用路径并检查实际渲染 |

skill 由 Markdown 指令组成，详细参考资料按需读取，附带 Codex 界面元数据。其他 agent 可以阅读这些指令，但其安装与调用行为尚未在本项目验证。

对于包含徽章的 README，默认排版要求：全部徽章集中在顶部同一可见区域，并将徽章及其上方的标题、Logo、标语、语言切换统一居中。后续正文保持左对齐；下载量、兼容性和社区收录徽章也放在同一组。

## 研究与结论

原始样本包括 React、Vue、Vite、FastAPI、uv、GitHub CLI、Deno、Ollama、Supabase、RustDesk、PyTorch、Transformers、ripgrep、fzf、Awesome 和 System Design Primer。

第一轮扩展新增 Linux、PostgreSQL、Kubernetes、OpenTofu、Ansible、Prometheus、p-limit、Neovim、Godot、NumPy、scikit-learn、JupyterLab、Zephyr、Home Assistant、OWASP Juice Shop 和科技爱好者周刊。

**200 项研究集**保留上述 32 项的固定提交，再增加 168 项有明确重点的 README 结构研究，按 14 组组织：Web 框架、语言与构建、CLI 与 shell、成熟库生态、数据与存储、基础设施、测试与代码质量、创作软件、开发者应用、科学计算与 ML、安全与网络、嵌入式与机器人、文档与学习、内容与领域应用。新增代表包括 Django、Rust、CPython、Axios、DuckDB、Blender、VS Code、OpenSSL、FreeRTOS 和 mdBook。[研究索引](skills/readme-atlas/references/source-study.md#study-index)可按领域进入。

在 **2026-10-16** 核验时，200 个仓库全部通过 Star 门槛，最低为 **1,512**。[筛选证据](research/selection.json)记录了精确数量、日期与重定向后的仓库地址。Star 用于筛选认可度，不作为 README 质量排名。格式范围现覆盖 Markdown、RST、AsciiDoc 和纯文本，也研究了包级 README 指针与仓库迁移告示。

我们的归纳是：围绕读者的下一步决策组织内容；适用时提供完整的首次使用路线；每一项功能和承诺都需要依据。简短的文档入口和很长的学习资源都可能合理，关键在于项目读者需要什么。

此外，视觉研究扩展到十三个项目：原有八个案例覆盖品牌首屏、图表、效果预览、文字层级、终端展示、折叠示例与导航；新增 Prometheus 的架构图、Godot 的编辑器预览、Home Assistant 的 RST 配图、Zephyr 的格式专属图像写法，以及 OpenTofu 的主题与提示块。[视觉指南](skills/readme-atlas/references/visual-design.md)区分源码观察与实际渲染检查，说明各自可借鉴的方法和需要权衡的地方。

[研究记录](skills/readme-atlas/references/source-study.md)区分了“观察到的做法”“可借鉴的方法”和“不能直接照搬的部分”。每份原始 README 都有固定提交链接，[研究清单](research/sources.json)记录了来源与 SHA-256。这是一组定性样本，不能证明某种排版导致项目受欢迎。

## 继续阅读与贡献

- [各类项目的读者路线](skills/readme-atlas/references/patterns.md)
- [视觉设计方法与来源观察](skills/readme-atlas/references/visual-design.md)
- [审查清单](skills/readme-atlas/references/review-checklist.md)
- [改写示例](examples/cli-rewrite.md)
- [研究方法与来源校验](research/README.md)
- [研究集验证记录](research/VALIDATION.md)
- [贡献指南](CONTRIBUTING.md)

发现问题或希望改进时，可以[提交 Issue](https://github.com/chromoany/readme-atlas/issues)，附上对应文件和具体例子。

## 许可证

本仓库原创指令、分析、示例及工具采用 [MIT](LICENSE) 许可证。引用项目保留各自许可证；本仓库提供原文链接，不重新分发其 README。
