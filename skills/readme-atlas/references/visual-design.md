# Visual design for repository READMEs

Use this reference when creating a README, changing its presentation substantially, or reviewing its appearance. Visual quality includes identity, composition, hierarchy, consistency, and a pleasant reading rhythm. Adapt the amount of branding to the project and preserve the user's chosen style.

## Observations from the source corpus

The examples below use the same immutable README revisions as the [source study](source-study.md). Observations describe their markup and content choices; recommendations are our synthesis.

| Project and source area | Observed visual choice | Transferable decision | Tradeoff to consider |
| --- | --- | --- | --- |
| [Vite][vite], opening | Centered theme-aware wordmark, a compact badge group, consistent feature icons | Build recognition with a compact brand area and repeat a small set of visual cues | Its explicit blank space consumes much of a viewport; adjust spacing to your own content |
| [uv][uv], opening / highlights | Status badges, a theme-aware benchmark chart, and a caption identifying the workload | Choose a prominent visual that explains the project's central benefit | A chart needs evidence and readable labels; its appearance does not validate a performance claim |
| [Supabase][supabase], opening / architecture | Theme-specific brand images, linked capability checklist, dashboard screenshot, architecture image | Give visual products an experience preview, and systems a separate explanatory diagram | Dense nested lists and wide client tables need narrow-layout review |
| [RustDesk][rustdesk], opening / screenshots | Centered identity and navigation, multilingual links, product screenshots, download badges | Pair a real product preview with clear entry points | Many language and community links can overwhelm the primary action |
| [React][react], opening | Text title with inline badges, short paragraphs, bold lead-ins for principles | A typographic document can establish a recognizable hierarchy without a banner | Inline badges may wrap awkwardly beside a long title |
| [fzf][fzf], opening / usage | Centered image identity, badge group, terminal preview, extensive navigation and examples | Demonstrate interaction visually, then make deeper tasks easy to locate | The promotional block before the introduction adds distance to first use |
| [Transformers][transformers], opening / quickstart | Theme-aware logo, grouped badges and language links, task examples inside `details` blocks | Keep optional demonstrations available while controlling page density | Essential installation and the primary example should remain visible |
| [Awesome][awesome], opening / contents | Large identity area, generous explicit spacing, sponsor graphics, categorized navigation | Use a stable taxonomy and clear category headings for discovery | The large promotional opening is an editorial tradeoff, not a prerequisite for a curated list |
| [Prometheus][prometheus], opening / architecture | Centered identity and grouped status badges; a separate architecture image before installation | Use a diagram to explain component relationships before readers choose setup | Inspect diagram labels at reading width; the markup alone does not establish legibility |
| [Godot][godot], opening / getting the engine | Centered logo, a large editor screenshot, then separate binary and source-build links | Show a creative tool in use and give its audience a direct download destination | The external screenshot can change independently; footer community badges differ from Atlas's header convention |
| [Home Assistant][homeassistant], opening / integrations | RST image substitutions link interface and integration previews to different destinations | Keep preview destinations tied to reader tasks; retain native image definitions | External branch-based assets are mutable, and substitution markup does not prove rendered contrast |
| [Zephyr][zephyr], opening / resources | RST embeds HTML with light/dark logo sources; resource groups use icons with text labels | Preserve format-specific artwork and label resource roles consistently | Do not copy raw-HTML directives into Markdown or assume all RST renderers accept them |
| [OpenTofu][opentofu], opening / nightly builds | Separate light/dark image links, compact navigation, and a GitHub tip callout for optional event information | Keep adoption links prominent and reserve callouts for distinct secondary information | Empty image alt text loses identity when images are unavailable; GitHub theme fragments are renderer-specific |

Vite, uv, and Supabase were also inspected in GitHub's rendered desktop view using the browser's existing dark appearance. The other five observations were checked against their pinned source markup. This pass did not establish how every asset renders on every theme, device, or third-party Markdown renderer. External images can change or fail independently of the pinned README bytes.

The range expansion adds five more source-only observations: Prometheus, Godot, Home Assistant, Zephyr, and OpenTofu, for thirteen visual cases in total. No additional browser/theme/device rendering audit was performed in this expansion. The sampled badge arrangements vary; Atlas's centered single-group convention is a user-chosen rule, not a consensus found in the corpus.

## Choose a visual direction

| Direction | Suitable projects | Composition |
| --- | --- | --- |
| Technical and typographic | Libraries, small CLIs, infrastructure, research code | Text title, specific description, compact status links, a readable example, regular headings |
| Branded and compact | Developer platforms, recognizable tools, agent skills | Existing logo or text identity, short tagline, a focused badge group, clear navigation, left-aligned body |
| Demonstration-led | Desktop/web applications, interactive CLIs, visual tools | Identity and purpose, a real task-focused screenshot or short demonstration, a visible try/install route |
| Navigation-led | Curated lists, courses, knowledge collections | Scope, a start-here path, category or study index, consistent entry formatting |

Mix directions only when they remain coherent. For a README with badges, apply the centered header convention below and keep long paragraphs, code, and documentation sections in the left-aligned body. A logo, animation, or badge collection is a design option, not a required asset.

## Compose the opening

Think about the visible README area, excluding GitHub's own navigation chrome. Give it one dominant focal point and a readable sequence:

1. Project identity: a text heading, existing wordmark, or compact logo with a text title.
2. A concise explanation or tagline that remains understandable without the artwork.
3. A small set of genuine status signals and clearly labeled entry links.
4. The appropriate proof or first action: screenshot, command/result, documentation link, or start-here route.

This is a compositional guide, not a mandatory ordering. A CLI may benefit from its command before a preview. Keep important facts, installation, and links as real text so the document still works when images do not load.

Use comfortable spacing between groups; let the renderer's headings and paragraph margins do most of the work. Inspect extra `br` elements before adding more. An oversized banner or a tall empty block can push the project explanation and install link out of view.

## Badges, colors, and icons

- Keep every badge together in one visible header group: version, download counts, license, platform, size, compatibility, build status, and community/listing badges when present. Do not scatter them across sections, place downloads in the footer, or hide badges inside `details`. Allow the group to wrap naturally on narrow screens; together does not mean forced onto one row.
- Center the complete badge group and every element before it, including the project title, logo, tagline, and language links. End the centered container immediately after the badges; keep subsequent navigation and body text left-aligned unless the current request specifies otherwise. This layout is an explicit README Atlas convention, not a claim that every studied project uses it.
- Select badges that answer real questions: version, build state, license, supported runtime, or a relevant community destination. Preserve semantic colors for statuses such as pass/fail.
- Use a consistent badge style and label convention. Avoid repeating the same fact through several badges. A compact wrapping group is easier to maintain than a wide single-row layout.
- Give each badge a real destination and useful alt text. A static "passing" image is not a CI result. Remove a badge whose source or claim is unavailable.
- Reuse the project's accent color for identity or navigation cues where supported. Avoid arbitrary multicolor decoration competing with the content.
- If icons or emoji help navigation, keep their role consistent. Pair them with readable words; meaning should not depend on the glyph alone.

A small version/build/license group is a reasonable starting point. There is no universal badge quota, palette, or required star-history chart.

## Screenshots, demonstrations, and diagrams

Choose media by the question it answers:

| Reader question | Useful visual |
| --- | --- |
| What will using this app feel like? | Actual product screenshot, focused on one meaningful task |
| What changes when I run this interactive command? | Short real terminal demonstration or a small input/output transcript |
| Which services do I need? | Labeled architecture or deployment diagram |
| What does the claimed performance mean? | Evidence-backed chart with workload, units, baseline, and method link |
| What is this project's identity? | Original or authorized logo / illustration |

Crop away irrelevant desktop chrome and private data before publication; preserve enough context to understand the task. Keep text legible at the displayed width. Avoid shrinking a full desktop screenshot into unreadable thumbnail cells. Use descriptive alt text and a caption explaining what to notice. Link to the full-size asset if details matter.

Prefer one strong preview to a large undifferentiated gallery. Use animation when interaction is the point; provide a useful static or text explanation as well. Optimize image dimensions and file size for the displayed result. Never fabricate UI, benchmark results, or product behavior to make a screenshot more attractive.

Use repository-relative asset paths when the project owns the images. When imagery depends on background contrast, provide light/dark variants or a deliberately neutral background. Keep a fallback image for renderers that do not select the themed source.

## Rhythm and information density

- Use a consistent heading hierarchy and concise section labels. Preserve useful existing section anchors.
- Split paragraphs that combine different reader decisions. Use bold lead-ins to aid scanning, rather than bolding most of the page.
- Use short tables for comparisons and mappings. Long prose, galleries, or multi-column feature cards usually read better as stacked sections on narrow screens.
- Separate runnable commands from output, and label code fences so syntax highlighting helps rather than misleads.
- Keep prerequisite warnings beside the action they constrain. Reserve callouts for consequential facts so ordinary prose retains its weight.
- Use `details` for optional platform recipes, additional task examples, or deep implementation notes. Keep the primary installation route and first example expanded.
- Place sponsor, contributor, and ecosystem material where it serves the project's goals without accidentally hiding the main path.

GitHub READMEs have a host-controlled font, content width, and sanitization rules. Work with headings, lists, tables, images, links, and simple supported HTML. Custom CSS, scripts, or website-style layout systems are not a portable README design foundation. See the [GFM specification](https://github.github.com/gfm/#what-is-github-flavored-markdown-).

For an existing RST or text README, adapt the same hierarchy and reader decisions using its native format. Preserve substitution definitions, directives, and text navigation; do not convert formats solely to reproduce a sampled header. Theme-aware image syntax and callouts depend on the renderer, so report source-only observations separately from displayed results.

## Adaptable markup examples

These are author-created patterns, not copied project branding. Replace example names and paths with real project material before publication.

### Centered identity and one badge group

```markdown
<div align="center">

# Project name

**A specific sentence explaining the project.**

English | [简体中文](README.zh-CN.md)

[![Version](https://img.shields.io/badge/version-1.0.0-blue?style=flat-square)](package.json)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)

</div>

[Quickstart](#quickstart) · [Documentation](docs/README.md) · [Contribute](CONTRIBUTING.md)
```

The example badge values are illustrative; replace them with verified project facts. Place any other real badges in that same group. An existing logo belongs inside the centered container above the badges. Keep blank lines around the Markdown inside the HTML container, preserve existing heading anchors, and verify GitHub's rendered result. For a README without badges, a text-only heading remains a complete option.

### Theme-aware artwork

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/logo-on-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/images/logo-on-light.svg">
  <img src="docs/images/logo-on-light.svg" alt="Project name" width="240">
</picture>
```

Vite, uv, and Transformers demonstrate this source-selection approach. Check actual contrast and scaling in the target renderer; a `picture` element alone does not prove that the artwork looks good.

### Optional deeper example

````markdown
<details>
<summary>Additional platform example</summary>

Explain the optional case here.

```bash
example-command
```

</details>
````

Leave blank lines around Markdown inside HTML containers, and verify the result in GitHub rather than assuming another renderer behaves identically.

## Visual review

For a substantial visual change, inspect the rendered page where practical:

- **Normal reading width:** identity, purpose, navigation, and a first action are easy to distinguish; whitespace supports the content; images and badges load; every badge is in the same visible group, with the group and everything before it centered.
- **Narrow layout:** badge and link groups wrap cleanly; tables and code do not force the whole document wider; screenshot text remains useful.
- **Light/dark appearance:** logos, transparent backgrounds, diagrams, and chart labels remain legible. Theme-specific assets actually select as intended.
- **Reading without media:** the project explanation, install route, and essential results remain understandable through text and alt descriptions.

Distinguish observed rendering defects from design suggestions and source-only concerns. Report which views were inspected. Do not claim a responsive or theme audit from Markdown syntax checks alone.

[vite]: https://github.com/vitejs/vite/blob/928e721b36690ac0f3f118290a21fc0cc4349055/README.md
[uv]: https://github.com/astral-sh/uv/blob/b8993e0a3b15f37e6b523bc5d02d2e7128713cad/README.md
[supabase]: https://github.com/supabase/supabase/blob/991653aa36a727f009f72d75fc2388c135b4d242/README.md
[rustdesk]: https://github.com/rustdesk/rustdesk/blob/e400bb75546cebf4f72a5ef3cf6e4a3efa2c3aa7/README.md
[react]: https://github.com/facebook/react/blob/098d2e87a1f7142947418d15f63f975b58c4685b/README.md
[fzf]: https://github.com/junegunn/fzf/blob/c8c2d0828a94a00879ceb6f95112a42e3ea322cf/README.md
[transformers]: https://github.com/huggingface/transformers/blob/b0cdc61e607f39403e248b11c35aef4edfa7d216/README.md
[awesome]: https://github.com/sindresorhus/awesome/blob/bc98e517ddca672f55f9857d714fc3ea3c3540b2/readme.md
[prometheus]: https://github.com/prometheus/prometheus/blob/466be3beb37099c28804608966f894b0dbad9993/README.md
[godot]: https://github.com/godotengine/godot/blob/4d10419cacd6d3009976e8f9fd3abd970fd58018/README.md
[homeassistant]: https://github.com/home-assistant/core/blob/f1f9fb4ef0413632ece929c8753a42b6c57a8049/README.rst
[zephyr]: https://github.com/zephyrproject-rtos/zephyr/blob/c136c73d7be3305d2c07ee5726d4c6d0d985068b/README.rst
[opentofu]: https://github.com/opentofu/opentofu/blob/105b18bb846f80760ee983c8e49044b2bd30f0a4/README.md
