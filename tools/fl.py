"""Shared helpers for the filament library tools: paths, slugs, entry I/O and validation (stdlib only)."""
import datetime, json, os, re, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIBRARY = os.path.join(ROOT, "library")
INDEX = os.path.join(ROOT, "index.json")
SCHEMA_VERSION = 1

TOP_KEYS = ["schema_version", "vendor", "product", "material", "colors", "bambu_parent", "fields",
            "published_ranges", "conflicts", "source_quality", "sources", "updated"]
REQUIRED = [k for k in TOP_KEYS if k != "bambu_parent"]
FIELD_KEYS = ["nozzle_temperature_range_low", "nozzle_temperature_range_high", "filament_density",
              "filament_diameter", "filament_soluble", "filament_is_support", "filament_shrink",
              "filament_max_volumetric_speed"]
# filament_shrink is not in the handoff doc's list: the seed records published shrink ranges under it.
RANGE_KEYS = ["bed_all_plates", "cool_plate_temp", "hot_plate_temp", "textured_plate_temp", "chamber_temperatures",
              "fan_max_speed", "fan_min_speed/fan_max_speed", "filament_retraction_length",
              "filament_retraction_speed", "overhang_fan_threshold", "filament_shrink"]
SOURCE_QUALITY = ["official_tds", "official_page", "brand_amazon_listing", "reseller_tds_copy"]


def today():
    return datetime.date.today().isoformat()


def slug(text):
    """'PLA+ 2.0' -> 'pla-plus-2-0'; '+' is spelled out so 'PLA' and 'PLA+' never share a file."""
    s = text.lower().replace("+", " plus ").replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def rel_path(entry):
    return f"library/{slug(entry['vendor'])}/{slug(entry['product'])}.json"


def canonical(entry):
    """Top-level keys in schema order (unknown keys last, so validation still sees them)."""
    out = {k: entry[k] for k in TOP_KEYS if k in entry}
    out.update({k: v for k, v in entry.items() if k not in out})
    return out


def dumps(entry):
    return json.dumps(canonical(entry), indent=2, ensure_ascii=False) + "\n"


def write_entry(entry):
    path = os.path.join(ROOT, rel_path(entry))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(dumps(entry))
    return path


def read_entry(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def library_files():
    out = []
    for dirpath, _, names in os.walk(LIBRARY):
        out += [os.path.join(dirpath, n) for n in names if n.endswith(".json")]
    return sorted(out)


def _num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def validate(entry):
    """List of problems with one entry (empty = valid)."""
    if not isinstance(entry, dict):
        return ["entry is not a JSON object"]
    errs = []
    for k in REQUIRED:
        if k not in entry:
            errs.append(f"missing required key '{k}'")
    for k in entry:
        if k not in TOP_KEYS:
            errs.append(f"unknown top-level key '{k}'")
    if "schema_version" in entry and entry["schema_version"] != SCHEMA_VERSION:
        errs.append(f"schema_version must be {SCHEMA_VERSION}")
    for k in ("vendor", "product", "material", "bambu_parent"):
        if k in entry and not (isinstance(entry[k], str) and entry[k].strip()):
            errs.append(f"'{k}' must be a non-empty string")
    if isinstance(entry.get("bambu_parent"), str) and "@" in entry["bambu_parent"]:
        errs.append("bambu_parent must not carry an '@<printer>' suffix")
    for k in ("vendor", "product"):
        if isinstance(entry.get(k), str) and not slug(entry[k]):
            errs.append(f"'{k}' has no filesystem-safe characters")
    for k in ("colors", "conflicts"):
        if k in entry and not (isinstance(entry[k], list) and all(isinstance(x, str) for x in entry[k])):
            errs.append(f"'{k}' must be a list of strings")
    if "source_quality" in entry and entry["source_quality"] not in SOURCE_QUALITY:
        errs.append(f"source_quality must be one of {', '.join(SOURCE_QUALITY)}")
    src = entry.get("sources")
    if "sources" in entry:
        if not (isinstance(src, list) and src):
            errs.append("at least one source is required")
        else:
            for s in src:
                u = urllib.parse.urlparse(s) if isinstance(s, str) else None
                if not (u and u.scheme in ("http", "https") and u.netloc):
                    errs.append(f"source is not an http(s) URL: {s!r}")
    if "updated" in entry:
        try:
            datetime.date.fromisoformat(entry["updated"])
        except (TypeError, ValueError):
            errs.append("updated must be a YYYY-MM-DD date")

    f = entry.get("fields")
    if "fields" in entry and not isinstance(f, dict):
        errs.append("fields must be an object")
        f = {}
    for k, v in (f or {}).items():
        if k == "temperature_vitrification":
            errs.append("fields.temperature_vitrification is not allowed (Bambu's heat-creep threshold, not Tg); "
                        "put Tg/Vicat/HDT in published_ranges._vitrification/_vicat/_hdt_0.45MPa")
            continue
        if k not in FIELD_KEYS:
            errs.append(f"unknown fields key '{k}'")
            continue
        if not (isinstance(v, list) and len(v) == 1 and isinstance(v[0], str) and v[0].strip()):
            errs.append(f"fields.{k} must be a one-element string array, got {v!r}")
            continue
        s = v[0]
        x = _num(s)
        if k.startswith("nozzle_temperature_range"):
            if x is None or not 150 <= x <= 450:
                errs.append(f"fields.{k} {s!r} is outside 150-450 C")
        elif k == "filament_density":
            if x is None or not 0.5 <= x <= 3.0:
                errs.append(f"fields.filament_density {s!r} is outside 0.5-3.0 g/cm3")
        elif k == "filament_diameter":
            if x not in (1.75, 2.85):
                errs.append(f"fields.filament_diameter {s!r} must be 1.75 or 2.85")
        elif k in ("filament_soluble", "filament_is_support"):
            if s not in ("0", "1"):
                errs.append(f"fields.{k} must be \"0\" or \"1\"")
        elif k == "filament_shrink":
            if not re.fullmatch(r"\d+(\.\d+)?%", s) or not 90 <= float(s[:-1]) <= 110:
                errs.append(f"fields.filament_shrink {s!r} must be a percentage like \"99.6%\"")
        elif k == "filament_max_volumetric_speed":
            if x is None or not 0 < x <= 100:
                errs.append(f"fields.filament_max_volumetric_speed {s!r} must be a number in (0, 100] mm3/s")
    lo = _num((f or {}).get("nozzle_temperature_range_low", [None])[0]) if isinstance(f, dict) else None
    hi = _num((f or {}).get("nozzle_temperature_range_high", [None])[0]) if isinstance(f, dict) else None
    if lo is not None and hi is not None and lo > hi:
        errs.append(f"nozzle range low {lo:g} is above high {hi:g}")

    pr = entry.get("published_ranges")
    if "published_ranges" in entry and not isinstance(pr, dict):
        errs.append("published_ranges must be an object")
        pr = {}
    for k, v in (pr or {}).items():
        if not (k.startswith("_") or k in RANGE_KEYS):
            errs.append(f"unknown published_ranges key '{k}' (note keys must start with '_')")
        if not (isinstance(v, str) and v.strip()):
            errs.append(f"published_ranges.{k} must be a non-empty string, got {v!r}")
    return errs
