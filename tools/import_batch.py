"""Import a Research-mode reply: `py -3 -I tools/import_batch.py <file> [--dry-run]`.

<file> holds a JSON array of entries in the handoff format, or the pasted reply itself (the first ```json
block is used). Each entry is validated, then written to library/<vendor>/<product>.json:
- added: no file yet; updated: the file differs; unchanged: identical apart from `updated`;
- rejected: fails validation, repeats a line already in this batch, or names an existing file's line with
  different spelling (e.g. "Elegoo" vs "ELEGOO": fix the spelling in the batch and import again).
A missing `updated` is set to today; a refresh that omits `bambu_parent` or `orca_parent` keeps the library's one.
--merge: a refresh is laid over the library entry instead of replacing it (for gap-fill replies that
only carry the values they re-read): batch values win, keys it omits are kept, colors/sources/conflicts
are unioned, the old `_notes` are appended, a changed field is recorded in `conflicts`, and a missing
`colors` is taken from the library entry (or [] for a new line).
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


def union(first, second):
    return first + [x for x in second if x not in first]


def merge(old, new):
    m = dict(old)
    m.update({k: v for k, v in new.items() if k not in ("fields", "published_ranges", "colors", "sources", "conflicts")})
    m["fields"] = {**old["fields"], **new.get("fields", {})}
    m["published_ranges"] = {**old["published_ranges"], **new.get("published_ranges", {})}
    old_notes, new_notes = old["published_ranges"].get("_notes"), new.get("published_ranges", {}).get("_notes")
    if old_notes and new_notes and old_notes not in new_notes:
        m["published_ranges"]["_notes"] = f"{new_notes} Earlier entry: {old_notes}"
    changed = [f"{k}: earlier library entry had {'/'.join(v)} (sources: {', '.join(old['sources'])})"
               for k, v in old["fields"].items() if k in new.get("fields", {}) and new["fields"][k] != v]
    m["colors"] = union(new.get("colors", []), old["colors"])
    m["sources"] = union(new.get("sources", []), old["sources"])
    m["conflicts"] = union(union(new.get("conflicts", []), old["conflicts"]), changed)
    return m


def main(argv):
    dry = "--dry-run" in argv
    merging = "--merge" in argv
    args = [a for a in argv if a not in ("--dry-run", "--merge")]
    if len(args) != 1:
        raise SystemExit(__doc__)
    result = {"added": [], "updated": [], "unchanged": [], "rejected": []}
    seen = set()
    for i, e in enumerate(load_batch(args[0]), 1):
        label = f"#{i} {e.get('vendor', '?')} {e.get('product', '?')}" if isinstance(e, dict) else f"#{i}"
        if isinstance(e, dict):
            e.setdefault("updated", fl.today())
            if merging and isinstance(e.get("vendor"), str) and isinstance(e.get("product"), str):
                path = os.path.join(fl.ROOT, fl.rel_path(e))
                old = fl.read_entry(path) if os.path.exists(path) else None
                if old and (old["vendor"], old["product"]) == (e["vendor"], e["product"]):
                    e = merge(old, e)
                else:
                    e.setdefault("colors", [])
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
            for k in fl.PARENT_KEYS:
                if k not in e and k in old:
                    e[k] = old[k]
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
