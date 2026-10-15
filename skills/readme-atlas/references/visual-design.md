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

Vite, uv, and Supabase were also inspected in GitHub's rendered desktop view using the browser's existing dark appearance. The other five observations were checked against their pinned source markup. This pass did not establish how every asset renders on every theme, device, or third-party Markdown renderer. External images can change or fail independently of the pinned README bytes.

## Choose a visual direction

| Direction | Suitable projects | Composition |
| --- | --- | --- |
| Technical and typographic | Libraries, small CLIs, infrastructure, research code | Text title, specific description, compact status links, a readable example, regular headings |
| Branded and compact | Developer platforms, recognizable tools, agent skills | Existing logo or text identity, short tagline, a focused badge group, clear navigation, left-aligned body |
| Demonstration-led | Desktop/web applications, interactive CLIs, visual tools | Identity and purpose, a real task-focused screenshot or short demonstration, a visible try/install route |
| Navigation-led | Curated lists, courses, knowledge collections | Scope, a start-here path, category or study index, consistent entry formatting |

Mix directions only when they remain coherent. Centering the identity area can work well with a left-aligned technical body. Centering long paragraphs, code, or whole documentation sections makes scanning harder. A logo, animation, or badge collection is a design option, not a required asset.

## Compose the opening

Think about the visible README area, excluding GitHub's own navigation chrome. Give it one dominant focal point and a readable sequence:

1. Project identity: a text heading, existing wordmark, or compact logo with a text title.
2. A concise explanation or tagline that remains understandable without the artwork.
3. A small set of genuine status signals and clearly labeled entry links.
4. The appropriate proof or first action: screenshot, command/result, documentation link, or start-here route.

This is a compositional guide, not a mandatory ordering. A CLI may benefit from its command before a preview. Keep important facts, installation, and links as real text so the document still works when images do not load.

Use comfortable spacing between groups; let the renderer's headings and paragraph margins do most of the work. Inspect extra `br` elements before adding more. An oversized banner or a tall empty block can push the project explanation and install link out of view.

## Badges, colors, and icons

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

## Adaptable markup examples

These are author-created patterns, not copied project branding. Replace example names and paths with real project material before publication.

### Compact identity and navigation

```html
<h1 align="center">Project name</h1>
<p align="center">A specific sentence explaining the project.</p>
<p align="center">
  <a href="#quickstart">Quickstart</a> ·
  <a href="docs/README.md">Documentation</a> ·
  <a href="CONTRIBUTING.md">Contribute</a>
</p>
```

Keep the body left-aligned. Add a real logo or a few verified badges if they help the chosen identity; a text-only heading is already a complete option.

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

- **Normal reading width:** identity, purpose, navigation, and a first action are easy to distinguish; whitespace supports the content; images and badges load.
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
