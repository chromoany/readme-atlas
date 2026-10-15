"""Author-created README example fixture. Requires Python 3.10+."""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Print log lines for one level.")
    parser.add_argument("file", type=Path)
    parser.add_argument("--level", required=True, choices=("INFO", "WARN", "ERROR"))
    args = parser.parse_args()
    for line in args.file.read_text(encoding="utf-8").splitlines():
        if line.startswith(args.level + " "):
            print(line)


if __name__ == "__main__":
    main()
