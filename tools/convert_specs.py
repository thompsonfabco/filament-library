"""One-time seed: convert SV08MAX-Orca-Scripts/filament_profiles/specs.json into library/ entries.

    py -3.10 -I tools/convert_specs.py [specs.json] [lines.py]

Both inputs are only read. Changes from the old format (nothing is invented):
- fields.temperature_vitrification -> published_ranges._vitrification ("63 (Vicat)", metric from
  _vitrification_metric).
- fields.filament_max_volumetric_speed objects (nozzle not stated / ranges / conditions) don't fit the
  one-element field, so the published text moves to published_ranges._max_volumetric_speed.
- _hardened_nozzle_required true/false -> "yes"/"no"; the pipeline marker _merged_from_passes is dropped;
  a top-level _note is appended to published_ranges._notes.
- bambu_parent comes from the Bambu Studio template column of lines.py (the parents the generator already
  uses, "|0.4" nozzle suffix stripped); lines with no lines.py row get none and are listed in the report.
- A missing source_quality becomes official_page only when every source is on the vendor's own site.
Writes conversion-report.md beside the library, then rebuilds index.json.
"""
import ast, json, os, sys, urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fl, build_index

DEFAULT_DIR = r"C:\CODING\SV08MAX-Orca-Scripts\filament_profiles"


def load_lines(path):
    """lines.py LINES as data (NAME = literal assignments only, never executed)."""
    with open(path, encoding="utf-8") as fh:
        tree = ast.parse(fh.read(), path)
    names = {}

    def value(node):
        if isinstance(node, ast.Name):
            return names[node.id]
        if isinstance(node, (ast.List, ast.Tuple)):
            return [value(n) for n in node.elts]
        return ast.literal_eval(node)

    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
            names[node.targets[0].id] = value(node.value)
    return {row[0]: row[4].split("|")[0] for row in names["LINES"]}


def mvs_text(d):
    """{'value': '8-12', '_condition': 'at 300-320C', '_nozzle': 'not stated'} -> '8-12 mm3/s (at 300-320C; nozzle not stated)'."""
    d = dict(d)
    qual = d.pop("_qualifier", "")
    if "value" in d:
        val = f"{d.pop('value')} mm3/s"
    else:
        nozzles = [k for k in d if not k.startswith("_")]
        val = ", ".join(f"{d.pop(k)} mm3/s @{k} nozzle" for k in nozzles)
    extra = [f"{k.lstrip('_')} {v}" if k != "_condition" else v for k, v in d.items()]
    return (f"{qual} " if qual else "") + val + (f" ({'; '.join(extra)})" if extra else "")


def convert(old, parents, report):
    name = f"{old['vendor']} {old['product']}"
    e = {k: v for k, v in old.items() if k != "_note"}
    f = dict(e.get("fields", {}))
    pr = {k: v for k, v in e.get("published_ranges", {}).items() if k != "_merged_from_passes"}
    metric = pr.pop("_vitrification_metric", None)
    if "temperature_vitrification" in f:
        v = f.pop("temperature_vitrification")[0]
        if "_vitrification" in pr:
            raise ValueError(f"{name}: has both temperature_vitrification and _vitrification")
        pr["_vitrification"] = f"{v} ({metric})" if metric else v
    elif metric:
        report["notes"].append(f"{name}: _vitrification_metric '{metric}' without a value, dropped")
    mvs = f.get("filament_max_volumetric_speed")
    if isinstance(mvs, dict):
        pr["_max_volumetric_speed"] = mvs_text(f.pop("filament_max_volumetric_speed"))
        report["mvs"].append(f"{name}: {pr['_max_volumetric_speed']}")
    if isinstance(pr.get("_hardened_nozzle_required"), bool):
        pr["_hardened_nozzle_required"] = "yes" if pr["_hardened_nozzle_required"] else "no"
    if old.get("_note"):
        pr["_notes"] = f"{pr['_notes']} {old['_note']}" if pr.get("_notes") else old["_note"]
    e.update(schema_version=fl.SCHEMA_VERSION, fields=f, published_ranges=pr, updated=fl.today())
    if not e.get("source_quality"):
        hosts = {urllib.parse.urlparse(s).netloc for s in e.get("sources", [])}
        own = fl.slug(e["vendor"]).replace("-", "")
        if hosts and all(own in h.replace("-", "") for h in hosts):
            e["source_quality"] = "official_page"
            report["notes"].append(f"{name}: source_quality missing; set official_page (all sources on {', '.join(sorted(hosts))})")
    if name in parents:
        e["bambu_parent"] = parents[name]
    else:
        report["no_parent"].append(name)
    return fl.canonical(e)


def main(argv):
    specs = argv[0] if argv else os.path.join(DEFAULT_DIR, "specs.json")
    lines = argv[1] if len(argv) > 1 else os.path.join(DEFAULT_DIR, "lines.py")
    with open(specs, encoding="utf-8") as fh:
        old = json.load(fh)
    parents = load_lines(lines)
    report = {"no_parent": [], "mvs": [], "notes": [], "invalid": []}
    seen = {}
    for o in old:
        e = convert(o, parents, report)
        path = fl.rel_path(e)
        if path in seen:
            raise SystemExit(f"{path}: both '{seen[path]}' and '{e['vendor']} {e['product']}' map here")
        seen[path] = f"{e['vendor']} {e['product']}"
        errs = fl.validate(e)
        if errs:
            report["invalid"].append(f"{seen[path]}: " + "; ".join(errs))
            continue
        fl.write_entry(e)
    version, _ = build_index.build()

    out = [f"# Seed conversion report ({fl.today()})", "",
           f"Source: `{specs}` ({len(old)} entries); parents from `{lines}`.", "",
           f"- Written: {len(old) - len(report['invalid'])}; rejected: {len(report['invalid'])}; "
           f"index library_version {version}.", ""]
    for key, title in (("invalid", "Rejected (failed validation)"),
                       ("no_parent", "No bambu_parent (no lines.py row for this line)"),
                       ("mvs", "Max volumetric speed moved to published_ranges._max_volumetric_speed"),
                       ("notes", "Other notes")):
        out += [f"## {title} ({len(report[key])})", ""] + [f"- {x}" for x in report[key]] + [""]
    with open(os.path.join(fl.ROOT, "conversion-report.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(out))
    print("\n".join(out))
    return 1 if report["invalid"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
