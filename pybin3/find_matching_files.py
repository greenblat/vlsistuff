#!/usr/bin/env python3
"""List source files with the same filename as each destination file.

Usage: python3 find_matching_files.py SOURCE_DIRECTORY DESTINATION_DIRECTORY
Matches are case-sensitive and compare names only, including extensions.
Symbolic links to files and directories are ignored during scanning.
Also generates copy_files.py in the current directory (does not execute it).
Only unique matches are copied; running the generated script overwrites targets.
"""

import argparse
import os
import sys
from collections import defaultdict
from pathlib import Path


def directory(value):
    path = Path(value).expanduser().resolve()
    if not path.is_dir():
        raise argparse.ArgumentTypeError(f"Not a directory: {value}")
    return path


def raise_scan_error(error):
    raise error


def scan_files(root):
    """Yield file paths recursively, in deterministic order."""
    for parent, directories, filenames in os.walk(root, onerror=raise_scan_error):
        directories[:] = sorted(
            name for name in directories
            if not (Path(parent) / name).is_symlink()
        )
        for filename in sorted(filenames):
            path = Path(parent) / filename
            if not path.is_symlink() and path.is_file():
                yield path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_directory", type=directory)
    parser.add_argument("destination_directory", type=directory)
    parser.add_argument("--copy-script", type=Path, default=Path("copy_files.py"),
                        help="Generated Python script path (must not already exist)")
    args = parser.parse_args()

    try:
        # Collect destination files first, as requested.
        destination_files = list(scan_files(args.destination_directory))
        wanted_names = {path.name for path in destination_files}
        source_matches = defaultdict(list)
        for path in scan_files(args.source_directory):
            if path.name in wanted_names:
                source_matches[path.name].append(path)
    except OSError as error:
        print(f"Error scanning directories: {error}", file=sys.stderr)
        return 1

    if not destination_files:
        print("No files found in the destination directory.")
    copies = []
    for destination in destination_files:
        print(f"Destination: {destination}")
        matches = source_matches.get(destination.name, [])
        if matches:
            for source in matches:
                print(f"  Source: {source}")
            if len(matches) == 1:
                copies.append((str(matches[0]), str(destination)))
            else:
                print("  Copy skipped: multiple source files have this name.")
        else:
            print("  No matching filename in source directory.")
        print()
    try:
        # Exclusive creation prevents overwriting an existing file or symlink.
        with args.copy_script.expanduser().open("x", encoding="utf-8") as output:
            output.write(COPY_SCRIPT.replace("__COPY_PAIRS__", repr(copies)))
    except OSError as error:
        print(f"Error creating copy script: {error}", file=sys.stderr)
        return 1
    print(f"Copy script: {args.copy_script.expanduser().absolute()}")
    print(f"Scheduled copies: {len(copies)}. Run the generated script to copy files.")
    return 0


COPY_SCRIPT = '''#!/usr/bin/env python3
"""Generated copy plan. Running this script overwrites destination files.

Only filenames with a unique source match are included.
"""
import shutil
import sys
from pathlib import Path

COPIES = __COPY_PAIRS__


def has_symlink(path):
    return any(part.is_symlink() for part in (path, *path.parents))


def main():
    failed = False
    for source_name, destination_name in COPIES:
        source, destination = Path(source_name), Path(destination_name)
        try:
            if has_symlink(source) or has_symlink(destination):
                print(f"Skipped symbolic link: {source} -> {destination}")
                continue
            if not source.is_file() or not destination.is_file():
                raise OSError("Source or destination is no longer a regular file")
            if source.samefile(destination):
                print(f"Skipped same file: {destination}")
                continue
            shutil.copy2(source, destination)
            print(f"Copied: {source} -> {destination}")
        except OSError as error:
            failed = True
            print(f"Copy failed: {source} -> {destination}: {error}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
'''


if __name__ == "__main__":
    sys.exit(main())
