"""Rebuild index.json from library/: `py -3 -I tools/build_index.py`.

index.json goes into filament-kit's release asset, which is how installs get the library. `library_version` goes
up by one (and `generated` is set to today) only when the entry list or a file's sha256 changed, so an unchanged
library rebuilds to an identical index.
"""
import hashlib, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fl


def entries():
    out = []
    for path in fl.library_files():
        with open(path, "rb") as fh:
            raw = fh.read()
        e = json.loads(raw)
        out.append({"vendor": e["vendor"], "product": e["product"], "material": e["material"],
                    "path": os.path.relpath(path, fl.ROOT).replace(os.sep, "/"),
                    "sha256": hashlib.sha256(raw).hexdigest(), "updated": e["updated"]})
    return sorted(out, key=lambda r: r["path"])


def build():
    """Write index.json; returns (library_version, changed)."""
    new = entries()
    old = {}
    if os.path.exists(fl.INDEX):
        with open(fl.INDEX, encoding="utf-8") as fh:
            old = json.load(fh)
    changed = old.get("entries") != new
    index = {"schema_version": fl.SCHEMA_VERSION,
             "library_version": old.get("library_version", 0) + 1 if changed else old["library_version"],
             "generated": fl.today() if changed else old["generated"],
             "count": len(new), "entries": new}
    with open(fl.INDEX, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(index, indent=2, ensure_ascii=False) + "\n")
    return index["library_version"], changed


if __name__ == "__main__":
    version, changed = build()
    print(f"index.json: library_version {version}, {'changed' if changed else 'unchanged'}")
