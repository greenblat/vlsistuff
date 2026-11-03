#!/usr/bin/env python3
"""Run a Python script on files with a matching extension (not recursive)."""

import argparse
from pathlib import Path
import subprocess
import sys
import traceback


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("script", type=Path, help="Python script accepting a file path")
    parser.add_argument("directory", type=Path, help="Directory of files (not recursive)")
    parser.add_argument(
        "extension", nargs="?", default=".v",
        help="File extension, e.g. v or .v (default: .v; case-sensitive)",
    )
    args = parser.parse_args()

    extension = args.extension.lstrip(".")
    if not extension or any(char in extension for char in "/\\"):
        parser.error("Extension must be nonempty and cannot contain path separators")
    extension = "." + extension
    script = args.script.resolve()
    directory = args.directory.resolve()
    if not script.is_file():
        parser.error(f"Script is not a file: {script}")
    if not directory.is_dir():
        parser.error(f"Not a directory: {directory}")

    try:
        files = sorted(
            path for path in directory.iterdir()
            if path.is_file() and path.name.endswith(extension)
        )
    except OSError:
        print(f"Cannot read directory: {directory}", file=sys.stderr)
        traceback.print_exc()
        return 1
    failed = 0
    for path in files:
        print(f"Processing: {path}", flush=True)
        try:
            result = subprocess.run(
                [sys.executable, str(script), str(path)],
                capture_output=True,
                text=True,
                errors="replace",
            )
        except OSError:
            failed += 1
            print(f"Could not run script for: {path}", file=sys.stderr)
            traceback.print_exc()
            continue

        if result.stdout:
            print(result.stdout, end="", flush=True)
        if result.stderr:
            print(f"Error output for {path}:", file=sys.stderr)
            print(result.stderr, end="", file=sys.stderr, flush=True)
        if result.returncode != 0:
            failed += 1
            print(f"Failed ({result.returncode}): {path}", file=sys.stderr)

    print(f"Processed {len(files)} files; {failed} failed.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
