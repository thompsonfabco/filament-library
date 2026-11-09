# filament-library

Published manufacturer specs for 3D-printer filament, one JSON file per **brand + product line**. It is the
spec library behind [filament-kit](https://github.com/thompsonfabco/filament-kit)'s Bambu Studio preset
generator. Installed filament-kit servers get it from filament-kit's releases, which carry it as a signed
`library.tar.gz`. This repo's own tags and releases are unsigned.

When filament-kit builds a preset, values come from (highest priority first): Spoolman's own data, your own
local additions, **this library**, then the slicer's system parent preset (`bambu_parent`, `orca_parent`).

## Layout

```
index.json                       library_version, generated date, every entry with path + sha256
library/<vendor>/<product>.json  one entry per brand + product line (slugs: lower-case, '+' -> 'plus')
schema/entry.schema.json         entry format, schema_version 1
tools/                           stdlib Python: validate, build_index, import_batch, convert_specs (seed), checks
conversion-report.md             what the one-time seed conversion changed
research/unreachable.md          lines and values the automated fetch could not source (for Research mode)
```

## How entries are sourced

- **Every value has a source** (`sources`, at least one URL) and a `source_quality`, in order of preference:
  `official_tds` > `official_page` > `brand_amazon_listing` > `reseller_tds_copy`.
- **Published ranges are bounds.** Values are copied as printed; nothing is averaged, widened, narrowed or
  filled in. A value no source gives is left out.
- `fields` hold slicer values in Bambu Studio's one-element string array form. `temperature_vitrification` is
  never set there (Bambu uses it as a heat-creep threshold, not Tg); Tg / Vicat / HDT go in
  `published_ranges` (`_vitrification`, `_vicat`, `_hdt_0.45MPa`) with the metric named.
- Conflicting sources: the official value stays in `fields`, the others are listed in `conflicts`.
- New entries come from Research-mode replies written as entries in the schema's format. The seed (93 lines) was
  converted from an earlier research pass; its `bambu_parent`s are the parents an earlier preset generator used.

Schema notes: allowed keys are listed in `schema/entry.schema.json`. `published_ranges.filament_shrink` is a
published shrink range, and `_max_volumetric_speed` holds a published flow rate that names no nozzle or is a range.

## Tools

On Windows use the launcher, as below; elsewhere `python3` does the same.

```
py -3 -I tools/validate.py                       # every entry (or pass files)
py -3 -I tools/import_batch.py reply.json        # add/update from a Research reply; --dry-run to preview,
                                                 # --merge to lay a partial refresh over the existing entry
py -3 -I tools/build_index.py                    # rebuild index.json (import_batch does this)
py -3 -I tools/scan_owner_data.py                # no personal or purchase data in tracked files
py -3 -I tools/check_paths.py                    # no path an earlier version listed has gone
```

`library_version` goes up only when an entry is added, removed or changed. Files use LF line endings
(`.gitattributes`) so the hashes match what GitHub serves.

## Checks

`.github/workflows/ci.yml` runs on every push to `main`, tag and pull request: the tool tests, `validate.py`,
filament-kit's own validator at a pinned tag (`tools/build_library_asset.py --from .`, which also checks paths,
hashes and the index), the owner-data scan and the path check.

`tools/fl.py` is meant to give the same answers as the kit's validator, and an installed kit refuses a library
it cannot validate, so rule changes go in this order: a kit release that accepts the new rule, then the kit tag in
`ci.yml` here, then the data, then the kit picks up the new library.

Entries are never renamed or removed: a rename is an added file with the old one kept.

## License

GPLv3, like filament-kit.
