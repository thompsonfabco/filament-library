"""Validate library entries: `py -3 -I tools/validate.py [file.json ...]` (default: every file in library/).

Also checks that each file sits at the path its vendor + product slug to, so one line never has two files.
Exit status 1 if anything is invalid.
"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fl


def check_file(path):
    try:
        entry = fl.read_entry(path)
    except (OSError, ValueError) as e:
        return [f"unreadable: {e}"]
    errs = fl.validate(entry)
    if not errs:
        rel = os.path.relpath(os.path.abspath(path), fl.ROOT).replace(os.sep, "/")
        if rel.startswith("library/") and rel != fl.rel_path(entry):
            errs.append(f"file should be at {fl.rel_path(entry)}")
    return errs


def main(argv):
    paths = argv or fl.library_files()
    bad = 0
    for p in paths:
        errs = check_file(p)
        if errs:
            bad += 1
            print(f"{os.path.relpath(p, fl.ROOT)}:")
            for e in errs:
                print(f"  - {e}")
    print(f"{len(paths) - bad}/{len(paths)} entries valid")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
