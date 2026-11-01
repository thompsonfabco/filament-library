"""Import a Research-mode reply: `py -3.10 -I tools/import_batch.py <file> [--dry-run]`.

<file> holds a JSON array of entries in the handoff format, or the pasted reply itself (the first ```json
block is used). Each entry is validated, then written to library/<vendor>/<product>.json:
- added: no file yet; updated: the file differs; unchanged: identical apart from `updated`;
- rejected: fails validation, repeats a line already in this batch, or names an existing file's line with
  different spelling (e.g. "Elegoo" vs "ELEGOO": fix the spelling in the batch and import again).
A missing `updated` is set to today; a refresh that omits `bambu_parent` keeps the library's one.
The index is rebuilt when anything was written. Exit status 1 if any entry was rejected.
"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fl, build_index


def load_batch(path):
    with open(path, encoding="utf-8-sig") as fh:
        text = fh.read()
    m = re.search(r"```(?:json)?\s*\n(.*?)```", text, re.S)
    data = json.loads(m.group(1) if m else text)
    return data if isinstance(data, list) else [data]


def main(argv):
    dry = "--dry-run" in argv
    args = [a for a in argv if a != "--dry-run"]
    if len(args) != 1:
        raise SystemExit(__doc__)
    result = {"added": [], "updated": [], "unchanged": [], "rejected": []}
    seen = set()
    for i, e in enumerate(load_batch(args[0]), 1):
        label = f"#{i} {e.get('vendor', '?')} {e.get('product', '?')}" if isinstance(e, dict) else f"#{i}"
        if isinstance(e, dict):
            e.setdefault("updated", fl.today())
        errs = fl.validate(e)
        if errs:
            result["rejected"].append(f"{label}: " + "; ".join(errs))
            continue
        rel = fl.rel_path(e)
        if rel in seen:
            result["rejected"].append(f"{label}: repeats an earlier entry in this batch ({rel})")
            continue
        seen.add(rel)
        path = os.path.join(fl.ROOT, rel)
        old = fl.read_entry(path) if os.path.exists(path) else None
        if old is None:
            kind = "added"
        else:
            if (old["vendor"], old["product"]) != (e["vendor"], e["product"]):
                result["rejected"].append(f"{label}: {rel} already holds '{old['vendor']} {old['product']}'")
                continue
            if "bambu_parent" not in e and "bambu_parent" in old:
                e["bambu_parent"] = old["bambu_parent"]
            same = {k: v for k, v in old.items() if k != "updated"} == {k: v for k, v in e.items() if k != "updated"}
            kind = "unchanged" if same else "updated"
        result[kind].append(f"{label} -> {rel}")
        if kind != "unchanged" and not dry:
            fl.write_entry(e)
    for kind, rows in result.items():
        print(f"{kind}: {len(rows)}")
        for r in rows:
            print(f"  {r}")
    if dry:
        print("dry run: nothing written")
    elif result["added"] or result["updated"]:
        version, _ = build_index.build()
        print(f"index.json: library_version {version}")
    return 1 if result["rejected"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
