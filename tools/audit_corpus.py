#!/usr/bin/env python3
"""Check corpus joins, selection eligibility, and study coverage without network."""

import json
from pathlib import Path
import re
import sys


def audit(root):
    root = root.resolve()
    manifest = json.loads((root / "research/sources.json").read_text(encoding="utf-8"))
    selection = json.loads((root / "research/selection.json").read_text(encoding="utf-8"))
    sources = manifest["sources"]
    selected = selection["repositories"]
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    source_names = [s["repository"].lower() for s in sources]
    selected_names = [s["repository"].lower() for s in selected]
    require(len(sources) == selection["target_count"], "Corpus size differs from target")
    require(len(source_names) == len(set(source_names)), "Duplicate source repositories")
    require(len(selected_names) == len(set(selected_names)), "Duplicate selection repositories")
    require(set(source_names) == set(selected_names), "Source and selection inventories differ")
    canonical_urls = [s["source_url"].lower().rstrip("/") for s in selected]
    require(len(canonical_urls) == len(set(canonical_urls)), "Duplicate resolved repositories")

    for record in selected:
        name = record["repository"]
        stars = record["stars"]
        require(type(stars) is int and stars >= selection["minimum_stars"], f"{name}: below Star minimum")
        require(record["observed_date"] == selection["observed_date"], f"{name}: selection date differs")
        require(record["source_url"].startswith("https://github.com/"), f"{name}: missing GitHub evidence")

    skill = root / "skills/readme-atlas"
    study_files = [skill / "references/source-study.md"]
    study_files.extend(sorted((skill / "references/studies").glob("*.md")))
    citations = []
    counts = {label: 0 for label in ("Observed", "Transfer", "Limit")}
    for path in study_files:
        text = path.read_text(encoding="utf-8")
        citations.extend(re.findall(r"https://github\.com/[^\s)]+/blob/[0-9a-f]{40}/[^\s)]+", text))
        for label in counts:
            counts[label] += len(re.findall(r"^- \*\*" + label + r":\*\*\s+\S", text, re.M))
    expected_urls = {s["source_url"] for s in sources}
    require(set(citations) == expected_urls, "Pinned study citations differ from manifest")
    require(len(citations) == len(expected_urls), "Duplicate or missing per-project source citations")
    for label, count in counts.items():
        require(count == len(sources), f"{label}: expected {len(sources)} records, found {count}")

    for source in sources:
        name = source["repository"]
        identity = f"{name}/{source['commit']}/{source['path']}"
        require(bool(re.fullmatch(r"[0-9a-f]{40}", source["commit"])), f"{name}: invalid commit")
        require(bool(re.fullmatch(r"[0-9a-f]{64}", source["sha256"])), f"{name}: invalid digest")
        require(source["source_url"] == f"https://github.com/{name}/blob/{source['commit']}/{source['path']}", f"{name}: mismatched citation identity")
        require(source["raw_url"] == f"https://raw.githubusercontent.com/{identity}", f"{name}: mismatched raw identity")
        if "study_file" in source:
            path = (root / source["study_file"]).resolve()
            require(path.is_relative_to(skill.resolve()), f"{name}: study outside portable skill")
            require(path in study_files, f"{name}: missing study file")
            if path.exists():
                text = path.read_text(encoding="utf-8")
                block = re.search(r"^## " + re.escape(name) + r"\n(.*?)(?=^## |\Z)", text, re.M | re.S)
                require(block is not None and source["source_url"] in block[1], f"{name}: citation not in its study entry")

    visual = (skill / "references/visual-design.md").read_text(encoding="utf-8")
    visual_urls = set(re.findall(r"https://github\.com/[^\s)]+/blob/[0-9a-f]{40}/[^\s)]+", visual))
    require(visual_urls <= expected_urls, "Visual study cites sources outside corpus")
    if errors:
        for message in errors:
            print(f"FAIL: {message}")
        return 1
    print(f"PASS: {len(sources)} unique repositories; all >= {selection['minimum_stars']:,} Stars")
    print(f"PASS: {len(sources)} complete study records; {len(study_files)} study files; {len(visual_urls)} visual citations")
    print("Selection is dated evidence; this offline audit does not refresh Star counts or download sources.")
    return 0


if __name__ == "__main__":
    sys.exit(audit(Path(__file__).resolve().parents[1]))
