"""Fail if an entry path that any earlier version listed is gone: `py -3 -I tools/check_paths.py`.

Installed kits look saved lines up by product, so a renamed or removed entry loses data for them; a rename must be
an add that keeps the old file. Every commit that changed index.json counts as a version, because a kit release
may have shipped any of them. Needs full history (fetch-depth: 0 in CI). Exit status 1 if a path disappeared.
"""
import json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def git(root, *args):
    return subprocess.run(["git", "-C", root, *args], capture_output=True, check=True).stdout.decode("utf-8")


def paths_of(index_text):
    return {r["path"] for r in json.loads(index_text)["entries"]}


def missing_paths(root=ROOT):
    """{path: library_version it was last seen in} for paths in history but not in the working index.json."""
    with open(os.path.join(root, "index.json"), encoding="utf-8") as fh:
        current = paths_of(fh.read())
    gone = {}
    # newest first, so setdefault keeps the newest version that still listed the path
    for sha in git(root, "log", "--full-history", "--format=%H", "HEAD", "--", "index.json").split():
        try:
            old = json.loads(git(root, "show", f"{sha}:index.json"))
        except subprocess.CalledProcessError:   # the commit that deleted index.json, if one ever does
            continue
        for row in old["entries"]:
            if row["path"] not in current:
                gone.setdefault(row["path"], old["library_version"])
    return gone


def main():
    if git(ROOT, "rev-parse", "--is-shallow-repository").strip() == "true":
        print("shallow clone: earlier versions cannot be read; fetch full history")
        return 1
    gone = missing_paths()
    for path, version in sorted(gone.items()):
        print(f"{path}: listed in library_version {version} but gone (a rename must keep the old file)")
    print(f"{len(gone)} path(s) disappeared")
    return 1 if gone else 0


if __name__ == "__main__":
    sys.exit(main())
