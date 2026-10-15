#!/usr/bin/env python3
"""Verify pinned README bytes without credentials or third-party dependencies."""

from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def verify(source):
    name = source["repository"]
    expected_url = (
        f"https://raw.githubusercontent.com/{name}/"
        f"{source['commit']}/{source['path']}"
    )
    if source["raw_url"] != expected_url:
        return name, "FAIL: raw URL does not match pinned identity"
    request = Request(expected_url, headers={"User-Agent": "readme-atlas-source-verifier"})
    try:
        with urlopen(request, timeout=30) as response:
            content = response.read()
    except (HTTPError, URLError, TimeoutError) as error:
        return name, f"FAIL: could not retrieve source ({error})"
    if hashlib.sha256(content).hexdigest() != source["sha256"]:
        return name, "FAIL: SHA-256 mismatch"
    if len(content) != source["bytes"]:
        return name, "FAIL: byte count mismatch"
    return name, "PASS"


def main():
    manifest = Path(__file__).resolve().parents[1] / "research" / "sources.json"
    sources = json.loads(manifest.read_text(encoding="utf-8"))["sources"]
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(verify, sources))
    for name, status in results:
        print(f"{status} {name}")
    failed = sum(status != "PASS" for _, status in results)
    print(f"{len(results) - failed}/{len(results)} pinned sources verified")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
