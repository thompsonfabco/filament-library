# filament-library

Published manufacturer specs for 3D-printer filament, one JSON file per **brand + product line**. It is the
spec library behind [filament-kit](https://github.com/thompsonfabco/filament-kit)'s Bambu Studio preset
generator. Installed filament-kit servers fetch `index.json` from GitHub on a schedule, compare `sha256`s, and
download the entries that changed.

When filament-kit builds a preset, values come from (highest priority first): Spoolman's own data, the user's
local additions, **this library**, then the Bambu Studio system parent preset (`bambu_parent`).

## Layout

```
index.json                       library_version, generated date, every entry with path + sha256
library/<vendor>/<product>.json  one entry per brand + product line (slugs: lower-case, '+' -> 'plus')
schema/entry.schema.json         entry format, schema_version 1
tools/                           stdlib Python: validate, build_index, import_batch, convert_specs (seed)
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
- New entries come from Research-mode replies written to the handoff format in filament-kit's
  `docs/filament-research-handoff.md`. The seed (93 lines) was converted from an earlier research pass; its
  `bambu_parent`s are the parents the SV08 MAX preset generator already uses.

Schema notes: allowed keys are listed in `schema/entry.schema.json`. Beyond the handoff doc's list,
`published_ranges.filament_shrink` (a published shrink range) is accepted, and `_max_volumetric_speed` holds a
published flow rate that names no nozzle or is a range.

## Tools

No `python` on PATH here; use the launcher.

```
py -3.10 -I tools/validate.py                       # every entry (or pass files)
py -3.10 -I tools/import_batch.py reply.json        # add/update from a Research reply; --dry-run to preview
py -3.10 -I tools/build_index.py                    # rebuild index.json (import_batch does this)
```

`library_version` goes up only when an entry is added, removed or changed. Files use LF line endings
(`.gitattributes`) so the hashes match what GitHub serves.

## License

GPLv3, like filament-kit.
