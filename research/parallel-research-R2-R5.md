# Filament gap-fill: parallel Research runs R2-R5

How to use: open a new chat per run, turn Research on, and paste everything between that run's BEGIN and END lines as the message. Each prompt is self-contained.
When a run finishes, import its JSON with `tools/import_batch.py` (same as earlier batches). R1 (Bambu Lab, Polymaker, eSUN) is running in the original chat.

## R2: sunlu, overture, jayo, kingroon, hatchbox, inland, creality, anycubic, prusament (44 items)

----- BEGIN R2 -----

GAP-FILL RUN R2 of 5 for a filament spec library (feeds an automatic Bambu Studio preset generator; printers Bambu Lab X2D, X1/X1C/X1E, P1S/P1P/P2S; nozzles 0.2/0.4/0.6/0.8 mm). An earlier automated fetch (plain web fetch, no browser) could NOT source the items listed below, mostly because sites blocked it (HTTP 402/403/429), pages were truncated, PDFs were unreadable as text, or it ran out of time. Your job: fill these specific gaps from published manufacturer sources and return JSON entries. Accuracy and sourcing matter more than coverage. Work through every brand listed; if you run out of budget, end with an exact list of items not reached.

ITEMS TO FILL (verbatim from the gap report):

### sunlu
- **SUNLU (all lines written)** - missing: drying hours, filament_max_volumetric_speed. Why: no specs published: SUNLU TDS sheets give the drying temperature but not the drying time, and none publish max volumetric speed

### overture
- **OVERTURE Turbo PLA** - missing: colors. Why: not in current overture3d.com catalogue JSON; product page not fetched (site rate-limited WebFetch with 429) <https://overture3d.com/products/turbo-pla>

### jayo
- **JAYO High Speed PLA** - missing: nozzle temp, bed temp, density. Why: official page has no temps; Amazon brand listing returned 500/truncated page via WebFetch <https://www.amazon.com/JAYO-High-Speed-PLA-Filament/dp/B0CKX12R7J>
- **JAYO ASA** - missing: all (nozzle, bed, density, HDT, tolerance +/-0.02 vs +/-0.03). Why: official shared TPU/ASA listing has no ASA settings; Amazon brand listings too large/truncated for WebFetch (search snippet suggested 250-280C nozzle, 90-110C bed, ~96C heat resistance, unverified); no entry written <https://www.amazon.com/JAYO-Filament-Resistant-Functional-Dimensional/dp/B0GMVGBLXB>
- **JAYO Easy PA (E-PA) / PA Nylon PA6+66** - missing: all. Why: official Easy PA page has empty description; Amazon PA6+66 listing truncated via WebFetch (snippet suggested 250-280C nozzle, 30-50C bed, HDT ~121C, unverified); no entry written <https://us.amazon.com/JAYO-Filament-Resistant-Load-Bearing-Mechanical/dp/B0FXW6P6DN>
- **JAYO High Speed PLA** - missing: all (diameter, nozzle temp, bed temp, density). Why: no specs published in page text (the page tells users to match temperature to speed; values are probably only in images). The reusable-spool page is the same. The Amazon listing B0CKX12R7J was not attempted. <https://store.jayo3d.com/products/moq-5-rolls-jayo-high-speed-pla-1-1kg-3d-printing-filament-bundle>

### kingroon
- **Kingroon PA6-CF / PA-CF Carbon Fiber Nylon** - missing: all. Why: kingroon.com page publishes no settings; the kingroon3d.com PA-CF page shows copied PLA template values (190-210 C), so it is unusable; Amazon listing too large for WebFetch to reach its bullets, and the curl route was refused as bot-check circumvention; search snippet (250-280 C, dry 80C 8-12h, HDT 153 C) not verified <https://www.amazon.com/dp/B0DQPDTD2Z>
- **Kingroon TPU 95A** - missing: confirmation of hardness/TDS match; retraction speed (TDS value printed truncated). Why: Only TDS is labelled 'TPU 90A' in its text but filed under tpu_95a; Amazon listing bullets could not be read (page too large for WebFetch) <https://www.amazon.com/Kingroon-Filament-Flexible-Clog-Free-Accuracy/dp/B0FYMRQXDR>
- **Kingroon PLA Silk Tri-Color (Silk Multicolor PLA)** - missing: all (nozzle 210-230, density 1.32, diameter 1.75, bed 35-45 unverified) - entry dropped. Why: HTTP 429 Too Many Requests on every attempt over ~6 min (WebFetch); no TDS cited <https://kingroon.com/products/kingroon-silk-multicolor-pla ; https://kingroon3d.com/products/kingroon-pla-silk-tri-color-3d-printer-filament>
- **Kingroon PLA Silk Single Color** - missing: all (nozzle 195-230, density 1.21, diameter 1.75, bed 50-70, fan 100%) - entry dropped. Why: HTTP 429 Too Many Requests <https://kingroon.com/products/kingroon-silk-single-color-pla ; https://kingroon3d.com/products/kingroon-pla-silk-single-color-3d-printer-filament>
- **Kingroon PLA Silk Rainbow** - missing: all (nozzle 195-230, density 1.21, diameter 1.75, bed 50-70, fan 100%) - entry dropped. Why: HTTP 429 Too Many Requests <https://kingroon3d.com/products/kingroon3d-silk-rainbow-pla ; https://kingroon.com/products/kingroon-silk-rainbow-pla0123>
- **Kingroon PLA+** - missing: all (nozzle 210-235, density 1.20, diameter 1.75, bed 55-65) - entry dropped. Why: HTTP 429 Too Many Requests <https://kingroon.com/products/kingroon-pla-pluspla ; https://kingroon.com/products/kingroon-10kg-pla-plus-pla-filament-1-75mm ; https://kingroon3d.com/products/kingroon3d-pla-plus-pla-pro-pla-filament>
- **Kingroon HS-PLA** - missing: all (nozzle 190-220, density 1.20, diameter 1.75, bed 50-65) - entry dropped. Why: HTTP 429 Too Many Requests <https://kingroon.com/products/10kg-hs-pla-high-speed-printer-filament-mixed-color-1-75mm-us-in-stock>
- **Kingroon PLA Chameleon** - missing: all (nozzle 200-220, density 1.22, diameter 1.75, bed 50-70, fan 100%) - entry dropped. Why: HTTP 429 Too Many Requests <https://kingroon3d.com/products/kingroon-chameleon-pla-3d-printer-filament>
- **Kingroon PETG Basic** - missing: all (nozzle 230-250, density 1.26, diameter 1.75, bed 70-90, fan 100%) - entry dropped. Why: HTTP 429 Too Many Requests <https://kingroon.com/products/kingroon-petg-basic ; https://kingroon.com/products/10kg-petg-filament-1-75mm-3d-print-materials ; https://kingroon3d.com/products/10kg-1-75mm-petg-filament>
- **Kingroon PA Nylon** - missing: all (nozzle 250-280, diameter 1.75, bed 100-120) - entry dropped. Why: HTTP 429 Too Many Requests <https://kingroon.com/products/copy-of-2kg-pack-pa-nylon-3d-filament ; https://kingroon.com/products/kingroon-pa-nylon-basic-3d-printer-filament>
- **Kingroon PLA Basic / PLA Matte / PLA Silk Dual-Color / PLA Glow / PLA-CF / PLA Wood / PETG-CF / ABS / TPU 95A (kept entries, product-page sources only)** - missing: none of the fields/ranges (all confirmed in TDS PDFs); unverified page-derived notes and conflicts only: PLA Basic _nozzle_by_speed page part + AMS/X1 drying note; PLA Matte _diameter_tolerance +/-0.02 and page 50-600 mm/s claim; PLA-CF and PETG-CF _hardened_nozzle_required quotes; TPU 95A store hardness '95A'; all 'conflicts' strings for these lines. A note saying so was appended to each kept entry's _notes.. Why: HTTP 429 Too Many Requests <kingroon.com and kingroon3d.com product pages cited alongside each TDS>

### hatchbox
- **Hatchbox (all lines) - official site** - missing: verbatim first-hand read of PETG/Rapid PETG/ABS/TPU/Shiny/Glow/CF/Performance/UV/Temp-change pages and the PLA/PETG/ABS material pages. Why: blocked/403 on all direct product/collection/page fetches, 429 rate limit after a few requests; only /collections/pla-1-75mm.atom was readable once. Other values came from search-engine extracts of hatchbox3d.com pages <https://www.hatchbox3d.com/collections/filaments>
- **Hatchbox ABS Glow in the Dark** - missing: bed temp, density, drying, hardened-nozzle guidance. Why: blocked/403; no line-specific bed temp <https://www.hatchbox3d.com/products/3d-abs-1kg1-75-glow>

### inland
- **Inland (all lines) - microcenter.com product pages** - missing: density, drying, Tg/HDT, max volumetric speed for every line (none surfaced in any source). Why: blocked/403 for WebFetch on every microcenter.com URL (product, quickView, catalogue); values were taken from the search-engine index of these pages instead, so each one should be checked against the live page <https://www.microcenter.com/site/content/inland%20filament.aspx>
- **Inland Amazon listings (brand listing route)** - missing: cross-check of all lines. Why: HTTP 500 for most ASINs; pages that do load are about 1.2 MB, so specs only appear at a fixed offset. Only B09FW2HVJJ (Silk) was read <https://www.amazon.com/dp/B00YSZ1MFU>
- **Inland PLA High Speed Silk** - missing: all. Why: blocked/403; search index returned no specs <https://www.microcenter.com/product/668800/inland-175mm-pla-high-speed-silk-3d-printer-filament-10-kg-(22-lbs)-cardboard-spool-shadow>
- **Inland PLA Dual Color Silk** - missing: all. Why: blocked/403; search index returned no specs <https://www.microcenter.com/product/650245/inland-175mm-pla-dual-color-silk-3d-printer-filament-1kg-(22-lbs)-cardboard-spool-black-silver>
- **Inland PLA+ Multi Color (CMYK set)** - missing: all (needs a direct read). Why: ambiguous: two search readings disagree (plate 45-60 vs 45; one reading also gives 40-100 mm/s and calls it high-speed); page blocked/403 <https://www.microcenter.com/product/683865/inland-175mm-pla-3d-printer-filament-multi-color-100-kg-(22-lbs)-per-cardboard-spool-cyan-magenta-yellow-white>
- **Inland ABS UV Luminous (glow)** - missing: all. Why: blocked/403; search index gave no temperatures <https://www.microcenter.com/product/664840/inland-175mm-abs-3d-printer-filament-1kg-(22-lbs)-spool-uv-luminous-white>
- **Inland Fiberon ASA-CF08 (Inland-listed)** - missing: confirmation of brand/product identity; density, drying. Why: not attempted separately: probably Polymaker Fiberon resold under the Inland name. Search index shows 260-280 / 90-100, HDT 103C @0.45MPa <https://www.microcenter.com/product/705077/inland-175-mm-fiberon-asa-cf08-carbon-fiber-3d-printer-filament-05-kg-(11-lbs)-spool-light-gray>
- **Inland (all 19 lines)** - missing: none of the kept values; all were confirmed in the indexed listing text. Why: blocked/403: microcenter.com returns HTTP 403 to WebFetch. I checked every value against Micro Center's own listing text as shown in the search-engine index (WebSearch limited to microcenter.com), not by reading the live page <https://www.microcenter.com/product/...>
- **Inland PLA+** - missing: all (values confirmed from 611532 Black and other PLA+ colour listings). Why: blocked/403 and not found in the search index <https://www.microcenter.com/product/611544/inland-175mm-pla-3d-printer-filament-10-kg-(22-lbs)-spool-white>
- **Inland PLA+** - missing: all (confirmed from 611532). Why: blocked/403; the index shows the title only, with no temperatures <https://www.microcenter.com/product/632388/inland-175mm-pla-pro-3d-printer-filament-10-kg-(22-lbs)-spool-black>
- **Inland PETG-CF** - missing: all (values confirmed from 687104 Black). Why: blocked/403 and not found in the search index <https://www.microcenter.com/product/687109/inland-175mm-petg-cf-3d-printer-filament-1-kg-(22-lbs)-spool-antique-brass>
- **Inland Silk PLA** - missing: nothing in fields; the 190-230 conflict is unverified. Why: not attempted (cited for the conflicts entry only) <https://www.amazon.com/dp/B09FW2HVJJ>

### creality
- **Creality Hyper PETG** - missing: all (nozzle, bed, density, drying, HDT); only 'up to 300 mm/s' and tensile 40-50 MPa are official. Why: no specs in the official page text; the TDS hosted on manuals.plus returned 403; resellers conflict (220-260 or 190-260 nozzle; bed 70-80, 60-80 or 45) <https://store.creality.com/products/hyper-series-petg-3d-printing-filament-1kg>
- **Creality Hyper PLA** - missing: conflict detail only (seller name, bullet tolerance); no fields depend on it. Why: Page read only partly (truncated). The title confirms 'Dimensional Accuracy +/-0.02mm' but the seller and bullet text (+/-0.03) could not be read <https://www.amazon.com/dp/B0CLTY4MML>

### anycubic
- **Anycubic PLA Translucent** - missing: all. Why: blocked/429 on every Anycubic Shopify storefront (store/ca/uk/eu/au) after the first few fetches; guessed TDS filenames on cdn.shopify.com returned 404 <https://store.anycubic.com/products/pla-translucent>
- **Anycubic PETG Translucent** - missing: all (legacy page table shows the same text as PETG; no line-specific TDS read). Why: blocked/429 on storefronts; TDS filename not found by guess (404) <https://store.anycubic.com/products/petg-filament-translucent>
- **Anycubic PLA Special** - missing: all. Why: blocked/429; no TDS URL found <https://store.anycubic.com/products/pla-basic-special-color-filament>
- **Anycubic PLA Silk Dual/Tri-Color** - missing: all. Why: blocked/429; no TDS URL found <https://store.anycubic.com/products/silk-pla-dual-tri-color-filament>
- **Anycubic PET-CF** - missing: all. Why: blocked/429; ANYCUBIC_TDS_PET-CF_V3.0.pdf guesses 404 on all three Anycubic Shopify CDNs <https://store.anycubic.com/products/pet-cf>
- **Anycubic PC** - missing: all. Why: blocked/429 (retried after 1-3 min waits); TDS filename guesses 404 <https://store.anycubic.com/products/pc-filament>
- **Anycubic PVA** - missing: all. Why: blocked/429 on store and ca; TDS guesses 404 (search snippet only: 220-240C print, dry 75-85C 8-12h - not verified from page, not used) <https://store.anycubic.com/products/pva>
- **Anycubic TPU 68D** - missing: all. Why: blocked/429 on store and anycubic.au; TDS guesses 404 (search snippet only: density 1.26, HDT 0.45MPa 183C, speed 40-250 mm/s - not verified, not used) <https://store.anycubic.com/products/tpu-68d>

### prusament
- **Prusament PLA** - missing: density, diameter, max print speed, HDT 0.45/1.80 MPa, diameter tolerance. Why: TDS is published only as a zip over 10 MB; WebFetch refused it (maxContentLength exceeded). No separate download made. <https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-prusament-prod/2024/05/7ca620c4-prusament-pla-plablend.zip>
- **Prusament PLA Blend** - missing: density, diameter, max print speed, HDT 0.45/1.80 MPa, diameter tolerance. Why: same zip over 10 MB, unreadable via WebFetch <https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-prusament-prod/2024/05/7ca620c4-prusament-pla-plablend.zip>
- **Prusament PETG Carbon Fiber** - missing: density, diameter, fan speed, max print speed, HDT 0.45/1.80 MPa. Why: TDS is published only as a zip over 10 MB; WebFetch refused it (maxContentLength exceeded) <https://prusament.com/wp-content/uploads/2023/02/TDS_Prusament-PETG-CF-Black.zip>

HOW TO HANDLE EACH ITEM
- "missing: all" → produce a full new entry for that line.
- "missing: <specific values>" → produce a full entry for that line containing every value you can source (the importer refreshes the library entry by re-importing the full entry under the same vendor + product spelling), and make sure the listed missing values are filled if a source publishes them.
- If a value genuinely isn't published anywhere, leave it out and say so in _notes. If a line is discontinued and not widely sold, list it at the end instead of writing an entry.
- Use EXACTLY the vendor + product spelling used in the item list so the importer matches existing entries.
- The earlier fetch was blocked by many storefronts (Shopify 429 rate limits, Amazon pages too large, Micro Center 403). Try the brand's own TDS PDFs (often on cdn.shopify.com or the brand's wiki/support site), the brand's official Amazon storefront/listing, regional storefronts, and reseller-hosted copies of the official TDS (mark reseller_tds_copy). Read image-only PDFs visually where you can.

RULES
- Every value needs a source. Prefer, in order: official TDS/datasheet PDF → official product page → brand's own marketplace listing → reseller copy of the TDS. Record which in source_quality.
- Published ranges are bounds. Copy as printed ("200-230"). Never invent a midpoint, never widen or narrow a range, never fill a value the sources don't give: leave it out. A single printed value like "250±5" is not a range; record it in published_ranges, not fields.
- When several ranges are given (normal vs high-speed, per grade), record all in published_ranges._nozzle_by_speed and put the HIGHEST range in fields.nozzle_temperature_range_low/high.
- Do NOT set temperature_vitrification in fields. Put Tg / Vicat / HDT under published_ranges (_vitrification, _vicat, _hdt_0.45MPa) with the metric named.
- Conflicting sources: keep the official (newest official) value in fields, list others in conflicts with their source.
- Density g/cm³ (validator accepts 0.5-3.0; put higher values in _notes), diameter mm, temperatures °C (nozzle field floor 150 °C), drying "<temp>C <hours>h" (keep ">" if printed, e.g. "50C >8h").
- bambu_parent: closest Bambu Studio system filament preset; prefer the brand's own system preset if Bambu Studio ships one (e.g. "Overture PLA", "SUNLU PLA+"); otherwise Bambu Lab's own product for that material/variant ("Bambu PLA Basic", "Bambu PLA Matte", "Bambu PETG HF", "Bambu PETG Basic", "Bambu ABS", "Bambu ASA", "Bambu TPU 95A HF", "Bambu PA6-CF", "Bambu PC"); "Generic <material>" only when nothing closer exists. No "@BBL <printer>" suffix. Say in _notes if not confirmed.
- Note printer-relevant info: AMS compatibility, hardened nozzle required, enclosure/chamber needs, minimum nozzle size, max volumetric speed if published. Lines needing >300 °C nozzle are beyond the target printers: still record specs, and say so in _notes.

OUTPUT FORMAT
JSON in fenced ```json blocks (one per brand), arrays of entries, then a final list of: items you could not fill (with reason), lines found discontinued.

Entry schema example:
```json
{
  "schema_version": 1,
  "vendor": "ELEGOO",
  "product": "PLA+",
  "material": "PLA",
  "colors": ["Red", "Neon Green", "Yellow"],
  "bambu_parent": "Bambu PLA Basic",
  "fields": {
    "nozzle_temperature_range_low": ["200"],
    "nozzle_temperature_range_high": ["230"],
    "filament_density": ["1.30"],
    "filament_diameter": ["1.75"]
  },
  "published_ranges": {
    "bed_all_plates": "35-65",
    "chamber_temperatures": "20-45",
    "_drying": "50C 8h",
    "_hdt_0.45MPa": "56",
    "_vitrification": "63 (Vicat)",
    "_diameter_tolerance": "+/-0.02",
    "_notes": "Cardboard spool on some colours: wrap edges before AMS use."
  },
  "conflicts": [],
  "source_quality": "official_page",
  "sources": ["https://www.elegoo.com/products/elegoo-pla-plus-3d-printer-filament-1-75mm-colored-1kg"],
  "updated": "2026-11-02"
}
```
Allowed fields keys (one-element string arrays): nozzle_temperature_range_low, nozzle_temperature_range_high, filament_density, filament_diameter, filament_soluble ("1"/"0"), filament_is_support ("1"/"0"), filament_shrink (e.g. "99.6%"), filament_max_volumetric_speed (mm³/s, only if published).
Allowed published_ranges keys: bed_all_plates, cool_plate_temp, hot_plate_temp, textured_plate_temp, chamber_temperatures, fan_max_speed, fan_min_speed/fan_max_speed, filament_retraction_length, filament_retraction_speed, overhang_fan_threshold, and any key starting "_" (_drying, _nozzle_by_speed, _print_speed, _max_print_speed, _hardened_nozzle_required, _min_nozzle, _enclosure, _ams, _fiber_content, _hardness, _hdt_0.45MPa, _vicat, _vitrification, _diameter_tolerance, _annealing, _notes).
source_quality: official_tds | official_page | brand_amazon_listing | reseller_tds_copy. updated: "2026-11-02".

----- END R2 -----

## R3: push-plastic, atomic-filament, fiberlogy, extrudr, spectrum, eryone, geeetech, sovol, qidi-tech, flashforge (44 items)

----- BEGIN R3 -----

GAP-FILL RUN R3 of 5 for a filament spec library (feeds an automatic Bambu Studio preset generator; printers Bambu Lab X2D, X1/X1C/X1E, P1S/P1P/P2S; nozzles 0.2/0.4/0.6/0.8 mm). An earlier automated fetch (plain web fetch, no browser) could NOT source the items listed below, mostly because sites blocked it (HTTP 402/403/429), pages were truncated, PDFs were unreadable as text, or it ran out of time. Your job: fill these specific gaps from published manufacturer sources and return JSON entries. Accuracy and sourcing matter more than coverage. Work through every brand listed; if you run out of budget, end with an exact list of items not reached.

ITEMS TO FILL (verbatim from the gap report):

### push-plastic
- **Push Plastic TPU 100A** - missing: all: nozzle 230-250, bed 60-80, hardness 100A, 0.6mm nozzle advice. Why: blocked/429 Too Many Requests (retried after waiting 60s and again after 150s) <https://www.pushplastic.com/products/tpu-100a-filament-1-75mm-1kg>
- **Push Plastic Carbon Fiber ABS / CF PC+PBT / CF Nylon / CF PETG** - missing: fiber content ~10%. Why: blocked/429 (all pushplastic.com product pages) <https://www.pushplastic.com/products/carbon-fiber-abs-filament-1-75mm-500g>
- **Push Plastic Nylon** - missing: enclosure conflict note. Why: blocked/429 <https://www.pushplastic.com/products/nylon-filament-1-75mm-1kg>
- **Push Plastic High Heat+Tough PLA** - missing: annealing conflict note. Why: blocked/429 <https://www.pushplastic.com/products/high-heat-tough-pla-filament-1-75mm-1kg>
- **Push Plastic PEI 9085** - missing: Tg ~185, product-page print-settings conflict. Why: blocked/429 <https://www.pushplastic.com/products/pei-9085-filament-1-75mm-500g>
- **Push Plastic PEI 1010** - missing: Tg ~215, product-page print-settings conflict. Why: blocked/429 <https://www.pushplastic.com/products/pei-1010-filament-1-75mm-500g>
- **Push Plastic (all 14 kept lines)** - missing: filament_diameter page confirmation, colour lists, 2.85mm availability. Why: blocked/429; filament_diameter 1.75 is supported only by the '1-75mm' slug in each cited product URL, not by reading the page <https://www.pushplastic.com/products/>

### atomic-filament
- **Atomic Filament Flame Retardant ABS FR15U** - missing: density, HDT/Tg, drying. Why: blocked/406 (SABIC resin TDS linked from the product page). Only third-party resin listings found (not used) <https://www.sabic.com/en/products/documents/cycolac-resin_fr15u_americas_technical_data_sheet/en>
- **Atomic Filament Flame Retardant ABS FR15U** - missing: density, HDT. Why: HTTP 406 according to the researcher's note. Not a cited source and not retried. <SABIC CYCOLAC FR15U resin TDS (linked from https://atomicfilament.com/products/flame-retardant-black-abs-filament)>

### fiberlogy
- **Fiberlogy rABS** - missing: all (nozzle temp, bed temp, density, drying, fan, HDT/Vicat). Why: Product page has no spec table. The TDS PDF text is compressed or image-only and could not be read. The alternate page (fiberlogy.com/?p=14646) also has no specs. A search summary quoted 220-250C, 100C bed and 1.05 density for an 'S2' page, but no fetched page confirmed those values, so they were not used. <https://fiberlogy.com/en/filaments/abs-en/rabs-en/ ; TDS https://fiberlogy.com/app/uploads/2026/05/FIBERLOGY_RABS_TDS.pdf>
- **Fiberlogy ASA+AF** - missing: all (nozzle temp, bed temp, density, drying, fan, aramid fiber %). Why: Product page has no spec table: it gives only 'heat resistant up to 94C', a closed chamber and a hardened nozzle. The TDS PDF could not be read (image-only/compressed). The old TDS URL from search (fiberlogy.com/en_US/p/file/.../FIBERLOGY_ASA-AF_TDS.pdf) returned 404. <https://fiberlogy.com/en/filaments/asa-en/asaaf-en/ ; TDS https://fiberlogy.com/app/uploads/2026/07/FIBERLOGY_ASAAF_TDS.pdf>
- **Fiberlogy (all 49 written lines)** - missing: diameter tolerance/ovality (not on product pages); filament_max_volumetric_speed (not published); Tg missing for ABS, ASA, PA, PCTG, CPE, PP-family lines; fan/airflow missing for FiberSatin, FiberSilk, rPLA, FiberWORKS PLA, PVB, BVOH and TPU lines (page shows an ambiguous '75-100%' or '50-75%' figure labelled 'humidity'). Why: Official TDS PDFs are image-based or compressed and not text-extractable, so every entry is sourced from the official product page only <https://fiberlogy.com/app/uploads/2026/05/FIBERLOGY_EASYPLA_TDS.pdf (representative)>
- **Fiberlogy (TDS PDFs for Easy PLA, HS PLA Clear, PLA Matte, PLA Mineral, rPLA, Easy PETG, PETG FR V0, rPETG, rPP, Nylon PA12, PA12+CF, PA12+GF, rNylon, ABS, ABS Plus, Easy ABS, PC/ABS, ASA, ASA Matte, CPE HT, FiberFlex 30D/40D/+CF, MattFlex 40D, HIPS, PCTG, PCTG+CF, PCTG+GF, PEI 9085)** - missing: none from cited sources; the TDS values (diameter, tolerance, TDS temps) could not be cross-checked. Why: image-only PDF or no text layer (pdftotext pulled no spec lines). These TDSs are not cited in the batch; I opened them only to cross-check the pages. <https://fiberlogy.com/app/uploads/2026/05/FIBERLOGY_*_TDS.pdf (linked from each product page)>

### extrudr
- **Extrudr DuraPro ASA Matte** - missing: all. Why: not found as a separate line in the official catalogue (DuraPro ASA is described as matte); only a third-party listing <https://simplyprint.io/filaments/extrudr/durapro-matte-asa>
- **Extrudr (all 26 written lines)** - missing: filament_diameter, drying. Why: the catalogue doesn't state diameter; drying is only in the overview table, whose columns are misaligned, so it wasn't trusted <https://s3.extrudr.com/extrudr-media/product-catalogue/extrudr-Produktkatalog_EN.pdf>

### spectrum
- **Spectrum (all lines except PLA Premium)** - missing: filament_diameter, diameter tolerance. Why: main site and TDS PDFs do not state diameter; only the PLA Premium shop listing was checked (1.75 mm). Scraping the shop search for the rest timed out <https://shop.spectrumfilaments.com/>
- **Spectrum PCTG Premium, PCTG GF10, ASA-X CF10, PA6 Low Warp GF30, ASA Electrically Conductive, PET-G Glitter/Premium (HDT rows)** - missing: HDT. Why: HDT values sit on split lines in the TDS text extraction and could not be read reliably; left out
- **Spectrum PLA Premium** - missing: filament_diameter 1.75 (removed); the shop listing's repeat of 185-215 / bed 0-45 / 1.24 g/cm3 was not checked, but the TDS confirms these values. Why: connection refused (ECONNREFUSED 5.149.162.4:443) <https://shop.spectrumfilaments.com/product-eng-502-Filament-Spectrum-PLA-Premium-1-75mm-DEEP-BLACK-1kg.html>

### eryone
- **Eryone PETG High-Speed Translucent** - missing: all. Why: no specs published as text: the product page shows image-only content and there is no TDS on the files page. Only reseller listings give values, which aren't an allowed source <https://eryone3d.com/products/petg-high-speed-translucent-filament>
- **Eryone PPS CF10** - missing: all. Why: no specs published as text: the product page is image-only and there is no TDS. Only a reseller listing (3dstisk.com) has values (310-350C, bed 80-90C) <https://eryone3d.com/products/pps-cf10-filament-1-75mm-0-03mm-0-5kg>

### geeetech
- **GEEETECH HS-PLA** - missing: all (nozzle, bed, speed, density, tolerance, max volumetric speed). Why: No specs on the official store pages (Black and White pages have only qualitative text; the temperature chart is an image). geeetech.com returned 429 every time, Amazon returned 503. Only reseller values exist: 3djake 210-230C, AliExpress bundle 185-220C. <https://support.geeetech.com/hspla-black-3d-printer-filament-175mm-1kgroll-p-1395.html>
- **GEEETECH Sparkly PLA** - missing: all. Why: Not found on support.geeetech.com. geeetech.com returned 429. Only reseller values (3djake: 180-210C nozzle, 50-67C bed), which are not an allowed source. <https://www.3djake.com/geeetech/pla-sparkly>
- **GEEETECH Carbon Fiber PLA** - missing: diameter tolerance, density, drying, hardened-nozzle statement, official colour list. Why: No official product page was reachable (geeetech.com 429). The entry was written from the GEEETECH wiki only. <https://www.geeetech.com/collections/all>
- **GEEETECH Matte PLA / PLA+ / PETG / PETG Metal / ABS+ / ASA / Luminous PLA / Marble PLA** - missing: density (all lines); bed temp (PLA+); drying (all except PETG Metal); AMS statements; Tg/HDT (except PETG HDT 80C from a staff reply). Why: The current geeetech.com Shopify store was rate-limited (HTTP 429) on every attempt. Entries come from the official legacy store support.geeetech.com and the GEEETECH wiki, so the newer pages may hold updated values. <https://www.geeetech.com/products/pla-matte-3d-printer-filament-1-75mm-1kg-roll>
- **GEEETECH Silk Dual / Tri-Color PLA** - missing: all, if it is a separate line. Why: Not attempted (treated as colourways of the existing Silk PLA line). Not checked whether the temps differ. <https://support.geeetech.com/filament-silksilk-dual-tricolor-c-83_113.html>

### sovol
- **SOVOL PLA Matte Multi-Colors Rainbow** - missing: all. Why: official page specs are image-only; no sovol3d.com product page found; only reseller (robu.in) listings, which conflict (190-210C vs 200-220C) and are not TDS copies; web search budget exhausted <https://www.sovol.tech/products/sovol-matte-pla-filament>
- **SOVOL PLA Glow in Dark** - missing: live-page verification of nozzle 200-240 / bed 50-60; density, tolerance, drying, speed. Why: HTTP 429 on every direct fetch; values taken from search-engine extraction, not verified on the live page <https://www.sovol3d.com/products/sovol-glow-in-dark-pla-filament-1-kg>
- **SOVOL PETG** - missing: live-page verification of nozzle 230-250 / bed 60-80 / speed 50-250; density, drying. Why: HTTP 429 on every direct fetch (also /it/ regional path); values from search-engine extraction, not verified on the live page <https://www.sovol3d.com/products/sovol-petg-3d-filaments-gradient-blue>
- **SOVOL TPU** - missing: verified nozzle range, bed temp, density, drying. Why: Amazon page did not serve feature bullets to fetch; nozzle 220 / bed 50-70 / speed 60 come from a search snippet of the listing; sovol.tech specs image-only <https://www.amazon.com/dp/B0FCS8G941>
- **SOVOL PLA Glow in Dark** - missing: hardened nozzle advice. Why: HTTP 429 <https://www.sovol3d.com/blogs/news/brightest-glow-in-the-dark-filament-tips-sovol-3d-printing>

### qidi-tech
- **QIDI Tech PLA Rapido Metal** - missing: filament_density (only 1.19~1.21 published); no TDS cross-check. Why: image-only PDF (TDS could not be rendered, so the product page was used); density published only as a range <https://drive.google.com/file/d/1dvDjY47IRF-VjIIZqXzXGXfF202Bb4D6/view>
- **QIDI Tech PLA Wood** - missing: filament_density (only 1.22-1.24 published); no TDS cross-check. Why: image-only PDF (TDS could not be rendered, so the product page was used); density published only as a range <https://drive.google.com/file/d/1sLVAUb8BQcEXDONqKQEgaDZnhxQ9F12i/view>
- **QIDI Tech ABS Rapido Metal** - missing: filament_density (only 1.05~1.07 published); no TDS cross-check. Why: image-only PDF (TDS could not be rendered, so the product page was used); density published only as a range <https://drive.google.com/file/d/1o2Y5m-boyDLUKGqOvw_AtCM5114j38Cc/view>
- **QIDI Tech PLA Silk** - missing: no TDS cross-check (entry fully sourced from the product page). Why: image-only PDF (TDS could not be rendered, so the product page was used) <https://drive.google.com/file/d/1Gh5LNF426P8wKZD8cuM95APcqxCYPtQI/view>
- **QIDI Tech PLA Rapido** - missing: density range 1.21~1.23, diameter tolerance, melt temp (removed); other values verified on product page/guide. Why: TDS PDF downloaded but text is outlined vector glyphs (no extractable text, no embedded page images); no PDF renderer available <https://drive.google.com/file/d/1r7PaFrEUKRzsYeIlFKNTs_phSinYLV_q/view>
- **QIDI Tech ABS Rapido** - missing: density, bed 80-100, Vicat, fan 0-50%, diameter tolerance, melt temp (removed). Why: TDS PDF text is outlined/unreadable; product page has no spec table <https://drive.google.com/file/d/1slDSMF4i03Isx5fBOJmIuCyQSAyoDIjA/view>

### flashforge
- **Flashforge HS PLA Multicolor** - missing: all. Why: blocked/429 (Shopify rate limit on every flashforge.com regional storefront); no TDS found <https://eu.flashforge.com/products/hs-pla-multicolor>
- **Flashforge HS PETG** - missing: all (the PETG entry uses the 2021 PETG TDS; unclear whether HS PETG is a separate formulation). Why: blocked/429 on product page; TDS guesses HS_PETG/HS-PETG returned 404 <https://eu.flashforge.com/products/petg>
- **Flashforge PETG Pro** - missing: all except guide-level nozzle/bed/speed. Why: blocked/429; TDS guesses PETG_Pro/PETGPro returned 404. Only figures available are from the Filament Guide (220-240C nozzle, 70-80C bed, 40-60 mm/s), and that alone was judged too thin for an entry <https://flashforge.com/fr/products/petg-pro>
- **Flashforge HS PLA** - missing: drying, diameter, diameter tolerance, product-page nozzle range (search summary said 190-240C, unverified). Why: product page specs not in fetched text / 429; the TDS's recommended-conditions table is empty <https://eu.flashforge.com/products/hs-pla>
- **Flashforge PLA, PLA Pro, PLA Matte, PLA Silk, PLA-CF, PETG, PETG-CF, ABS, ABS Pro, TPU 95A, PC, PVA (entries written)** - missing: filament_diameter and diameter tolerance (not in TDSs), single-value density (TDSs give only ranges), colours, drying for the PLA lines and PVA, confirmation that PC/PVA are still sold. Why: blocked/429 on all storefront pages (flashforge.com, eu., uk., au., ca., enterprise.) <https://flashforge.com/collections/filament>
- **Flashforge other possible lines (glow/luminous, wood, metal, marble, galaxy, burnt titanium, etc.)** - missing: existence and all values. Why: not attempted (the shared web-search budget was used up and the catalogue pages returned 429)
- **Flashforge PLA Silk** - missing: colourway lineup and whether multi-colour variants share the Silk TDS; any page-level drying or diameter values. Why: HTTP 429 Too Many Requests (two attempts) <https://eu.flashforge.com/products/pla-silk>
- **Flashforge PETG-CF** - missing: page HDT (reported 74C). Why: not cited and not read <https://enterprise.flashforge.com/products/petg-cf>

HOW TO HANDLE EACH ITEM
- "missing: all" → produce a full new entry for that line.
- "missing: <specific values>" → produce a full entry for that line containing every value you can source (the importer refreshes the library entry by re-importing the full entry under the same vendor + product spelling), and make sure the listed missing values are filled if a source publishes them.
- If a value genuinely isn't published anywhere, leave it out and say so in _notes. If a line is discontinued and not widely sold, list it at the end instead of writing an entry.
- Use EXACTLY the vendor + product spelling used in the item list so the importer matches existing entries.
- The earlier fetch was blocked by many storefronts (Shopify 429 rate limits, Amazon pages too large, Micro Center 403). Try the brand's own TDS PDFs (often on cdn.shopify.com or the brand's wiki/support site), the brand's official Amazon storefront/listing, regional storefronts, and reseller-hosted copies of the official TDS (mark reseller_tds_copy). Read image-only PDFs visually where you can.

RULES
- Every value needs a source. Prefer, in order: official TDS/datasheet PDF → official product page → brand's own marketplace listing → reseller copy of the TDS. Record which in source_quality.
- Published ranges are bounds. Copy as printed ("200-230"). Never invent a midpoint, never widen or narrow a range, never fill a value the sources don't give: leave it out. A single printed value like "250±5" is not a range; record it in published_ranges, not fields.
- When several ranges are given (normal vs high-speed, per grade), record all in published_ranges._nozzle_by_speed and put the HIGHEST range in fields.nozzle_temperature_range_low/high.
- Do NOT set temperature_vitrification in fields. Put Tg / Vicat / HDT under published_ranges (_vitrification, _vicat, _hdt_0.45MPa) with the metric named.
- Conflicting sources: keep the official (newest official) value in fields, list others in conflicts with their source.
- Density g/cm³ (validator accepts 0.5-3.0; put higher values in _notes), diameter mm, temperatures °C (nozzle field floor 150 °C), drying "<temp>C <hours>h" (keep ">" if printed, e.g. "50C >8h").
- bambu_parent: closest Bambu Studio system filament preset; prefer the brand's own system preset if Bambu Studio ships one (e.g. "Overture PLA", "SUNLU PLA+"); otherwise Bambu Lab's own product for that material/variant ("Bambu PLA Basic", "Bambu PLA Matte", "Bambu PETG HF", "Bambu PETG Basic", "Bambu ABS", "Bambu ASA", "Bambu TPU 95A HF", "Bambu PA6-CF", "Bambu PC"); "Generic <material>" only when nothing closer exists. No "@BBL <printer>" suffix. Say in _notes if not confirmed.
- Note printer-relevant info: AMS compatibility, hardened nozzle required, enclosure/chamber needs, minimum nozzle size, max volumetric speed if published. Lines needing >300 °C nozzle are beyond the target printers: still record specs, and say so in _notes.

OUTPUT FORMAT
JSON in fenced ```json blocks (one per brand), arrays of entries, then a final list of: items you could not fill (with reason), lines found discontinued.

Entry schema example:
```json
{
  "schema_version": 1,
  "vendor": "ELEGOO",
  "product": "PLA+",
  "material": "PLA",
  "colors": ["Red", "Neon Green", "Yellow"],
  "bambu_parent": "Bambu PLA Basic",
  "fields": {
    "nozzle_temperature_range_low": ["200"],
    "nozzle_temperature_range_high": ["230"],
    "filament_density": ["1.30"],
    "filament_diameter": ["1.75"]
  },
  "published_ranges": {
    "bed_all_plates": "35-65",
    "chamber_temperatures": "20-45",
    "_drying": "50C 8h",
    "_hdt_0.45MPa": "56",
    "_vitrification": "63 (Vicat)",
    "_diameter_tolerance": "+/-0.02",
    "_notes": "Cardboard spool on some colours: wrap edges before AMS use."
  },
  "conflicts": [],
  "source_quality": "official_page",
  "sources": ["https://www.elegoo.com/products/elegoo-pla-plus-3d-printer-filament-1-75mm-colored-1kg"],
  "updated": "2026-11-02"
}
```
Allowed fields keys (one-element string arrays): nozzle_temperature_range_low, nozzle_temperature_range_high, filament_density, filament_diameter, filament_soluble ("1"/"0"), filament_is_support ("1"/"0"), filament_shrink (e.g. "99.6%"), filament_max_volumetric_speed (mm³/s, only if published).
Allowed published_ranges keys: bed_all_plates, cool_plate_temp, hot_plate_temp, textured_plate_temp, chamber_temperatures, fan_max_speed, fan_min_speed/fan_max_speed, filament_retraction_length, filament_retraction_speed, overhang_fan_threshold, and any key starting "_" (_drying, _nozzle_by_speed, _print_speed, _max_print_speed, _hardened_nozzle_required, _min_nozzle, _enclosure, _ams, _fiber_content, _hardness, _hdt_0.45MPa, _vicat, _vitrification, _diameter_tolerance, _annealing, _notes).
source_quality: official_tds | official_page | brand_amazon_listing | reseller_tds_copy. updated: "2026-11-02".

----- END R3 -----

## R4: 3dxtech (51 items)

----- BEGIN R4 -----

GAP-FILL RUN R4 of 5 for a filament spec library (feeds an automatic Bambu Studio preset generator; printers Bambu Lab X2D, X1/X1C/X1E, P1S/P1P/P2S; nozzles 0.2/0.4/0.6/0.8 mm). An earlier automated fetch (plain web fetch, no browser) could NOT source the items listed below, mostly because sites blocked it (HTTP 402/403/429), pages were truncated, PDFs were unreadable as text, or it ran out of time. Your job: fill these specific gaps from published manufacturer sources and return JSON entries. Accuracy and sourcing matter more than coverage. Work through every brand listed; if you run out of budget, end with an exact list of items not reached.

ITEMS TO FILL (verbatim from the gap report):

### 3dxtech
- **3DXTech (all lines) official site** - missing: official product-page print recommendations for every line; all entries fall back to third-party-hosted TDS copies or MatterHackers listings. Why: blocked/429 Too Many Requests on every attempt (www and non-www hosts); pdf.directindustry.com 3DXTech catalogs returned 403; static.dajiqun.com TDS mirror refused the connection <https://www.3dxtech.com/>
- **3DXTech 3DXMAX ASA** - missing: density, HDT. Why: blocked/429 <https://www.3dxtech.com/3dxmax-asa-1kg/>
- **3DXTech CarbonX PLA+CF** - missing: density, Tg, HDT. Why: blocked/429 <https://www.3dxtech.com/carbon-fiber-pla-1/>
- **3DXTech CarbonX ASA+CF** - missing: density, Tg, HDT. Why: blocked/403 <https://pdf.directindustry.com/pdf/3dxtech/carbonx-carbon-fiber-asa-3d-printing-filament/196785-970252.html>
- **3DXTech ezPC** - missing: density. Why: blocked/429 <https://www.3dxtech.com/>
- **3DXTech CarbonX Nylon+CF [Gen3]** - missing: nozzle range, bed range, drying. Why: the TDS gives specimen print conditions only; the product page was blocked (429) <https://asset.conrad.com/media10/add/160267/c1/-/gl/002543874DS00/tehnicni-podatki-2543874-3d-xtech-nyl3010500bk0-carbonx-cf-polyamid-pa6-3d-tiskalnik-filament-pa-poliamid-odporno-na-kemikalije-175-mm-500-g-c.pdf>
- **3DXTech CarbonX PA12+CF** - missing: nozzle range, bed range, drying. Why: the TDS gives specimen conditions only; the product page was blocked (429) <https://datasheet.sic-components.com/CF_PA12_v1.pdf>
- **3DXTech Obsidian PA6+CF** - missing: density, Tg, HDT, tolerance. Why: blocked/429 <https://www.3dxtech.com/>
- **3DXTech CarbonX PEI 1010+CF** - missing: density, HDT. Why: blocked/429 <https://www.3dxtech.com/>
- **3DXTech 3DXSTAT ESD-PLA** - missing: density, drying, Tg, tolerance. Why: blocked/429 <https://www.3dxtech.com/>
- **3DXTech 3DXSTAT ESD-PETG** - missing: density, Tg, HDT. Why: blocked/429 <https://www.3dxtech.com/>
- **3DXTech 3DXSTAT ESD-ABS** - missing: density, Tg, HDT. Why: blocked/429 <https://www.3dxtech.com/>
- **3DXTech 3DXSTAT ESD-PEI** - missing: density, Tg, HDT, Ultem grade confirmation. Why: blocked/429 <https://www.3dxtech.com/>
- **3DXTech 3DXSTAT ESD-PEKK** - missing: density, Tg, HDT. Why: blocked/429 <https://www.3dxtech.com/>
- **3DXTech Firewire FR-ABS** - missing: density, Tg, HDT. Why: blocked/429 <https://3dxtech.com/products/firewire-r-fr-abs>
- **3DXTech Firewire FR-PC/ABS** - missing: density, Tg, HDT. Why: blocked/429 <https://www.3dxtech.com/>
- **3DXTech ThermaX PEEK** - missing: density, Tg, HDT, tolerance. Why: blocked/429 <https://www.3dxtech.com/>
- **3DXTech ThermaX PEI 1010** - missing: density, HDT. Why: blocked/429 <https://www.3dxtech.com/>
- **3DXTech ThermaX PEI 9085** - missing: density, HDT. Why: blocked/429 <https://www.3dxtech.com/>
- **3DXTech ThermaX PPSU** - missing: Tg, HDT. Why: blocked/429 <https://www.3dxtech.com/ppsu-filament>
- **3DXTech ThermaX HTS1** - missing: colors, bed range (only 'up to 160C'), drying, tolerance. Why: blocked/429 <https://www.3dxtech.com/>
- **3DXTech 3DXMAX ABS** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech ECOMAX PLA** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech 3DXMAX HIPS** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech PC/ABS** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech PC/ASA** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech MAX-G PCTG** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech Polycarbonate (PC)** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech HyperLite PP** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech AmideX PA6 Copolymer** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech AmideX PA6-GF30** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech WearX PA6** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech SimuBone** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech EVOLV3D OBC** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech CarbonX PC+CF** - missing: all. Why: blocked/429 (reseller); official site 429 <https://thinkrobotics.com/products/carbonx-pc-cf>
- **3DXTech CarbonX PEKK-A CF15** - missing: all. Why: blocked/403 <https://pdf.directindustry.com/pdf/3dxtech/cf15-pekk-a/196785-970226.html>
- **3DXTech CarbonX HTN+CF (PPA)** - missing: all. Why: connection refused <https://static.dajiqun.com/product-medias/3d-printing-materials/3dxtech/HTN3010750BK0/17628668-17189828.pdf>
- **3DXTech FibreX ABS GF10** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech FibreX PA12+GF30** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech FibreX PP GF30** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech 3DXSTAT ESD-TPU** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech ThermaX PEEK GF20** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech ThermaX PEKK-A** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech ThermaX PEKK-C** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech ThermaX PEI GF30** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech ThermaX PSU** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech ThermaX PPS** - missing: all. Why: not attempted (web search budget exhausted; official site 429) <https://www.3dxtech.com/pps-filament/>
- **3DXTech ThermaX PPE/PS** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech ThermaX TPI (EXTEM)** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech FluorX PVDF** - missing: all. Why: not attempted (web search budget exhausted; official site 429)
- **3DXTech (all lines) official 3dxtech.com product pages / current TDS** - missing: official confirmation of all values; no value removed for this reason. Why: not attempted in check; research pass reported HTTP 429 - all entries rely on MatterHackers listings or third-party-hosted TDS copies (source_quality reseller_tds_copy) <https://www.3dxtech.com>

HOW TO HANDLE EACH ITEM
- "missing: all" → produce a full new entry for that line.
- "missing: <specific values>" → produce a full entry for that line containing every value you can source (the importer refreshes the library entry by re-importing the full entry under the same vendor + product spelling), and make sure the listed missing values are filled if a source publishes them.
- If a value genuinely isn't published anywhere, leave it out and say so in _notes. If a line is discontinued and not widely sold, list it at the end instead of writing an entry.
- Use EXACTLY the vendor + product spelling used in the item list so the importer matches existing entries.
- The earlier fetch was blocked by many storefronts (Shopify 429 rate limits, Amazon pages too large, Micro Center 403). Try the brand's own TDS PDFs (often on cdn.shopify.com or the brand's wiki/support site), the brand's official Amazon storefront/listing, regional storefronts, and reseller-hosted copies of the official TDS (mark reseller_tds_copy). Read image-only PDFs visually where you can.

RULES
- Every value needs a source. Prefer, in order: official TDS/datasheet PDF → official product page → brand's own marketplace listing → reseller copy of the TDS. Record which in source_quality.
- Published ranges are bounds. Copy as printed ("200-230"). Never invent a midpoint, never widen or narrow a range, never fill a value the sources don't give: leave it out. A single printed value like "250±5" is not a range; record it in published_ranges, not fields.
- When several ranges are given (normal vs high-speed, per grade), record all in published_ranges._nozzle_by_speed and put the HIGHEST range in fields.nozzle_temperature_range_low/high.
- Do NOT set temperature_vitrification in fields. Put Tg / Vicat / HDT under published_ranges (_vitrification, _vicat, _hdt_0.45MPa) with the metric named.
- Conflicting sources: keep the official (newest official) value in fields, list others in conflicts with their source.
- Density g/cm³ (validator accepts 0.5-3.0; put higher values in _notes), diameter mm, temperatures °C (nozzle field floor 150 °C), drying "<temp>C <hours>h" (keep ">" if printed, e.g. "50C >8h").
- bambu_parent: closest Bambu Studio system filament preset; prefer the brand's own system preset if Bambu Studio ships one (e.g. "Overture PLA", "SUNLU PLA+"); otherwise Bambu Lab's own product for that material/variant ("Bambu PLA Basic", "Bambu PLA Matte", "Bambu PETG HF", "Bambu PETG Basic", "Bambu ABS", "Bambu ASA", "Bambu TPU 95A HF", "Bambu PA6-CF", "Bambu PC"); "Generic <material>" only when nothing closer exists. No "@BBL <printer>" suffix. Say in _notes if not confirmed.
- Note printer-relevant info: AMS compatibility, hardened nozzle required, enclosure/chamber needs, minimum nozzle size, max volumetric speed if published. Lines needing >300 °C nozzle are beyond the target printers: still record specs, and say so in _notes.

OUTPUT FORMAT
JSON in fenced ```json blocks (one per brand), arrays of entries, then a final list of: items you could not fill (with reason), lines found discontinued.

Entry schema example:
```json
{
  "schema_version": 1,
  "vendor": "ELEGOO",
  "product": "PLA+",
  "material": "PLA",
  "colors": ["Red", "Neon Green", "Yellow"],
  "bambu_parent": "Bambu PLA Basic",
  "fields": {
    "nozzle_temperature_range_low": ["200"],
    "nozzle_temperature_range_high": ["230"],
    "filament_density": ["1.30"],
    "filament_diameter": ["1.75"]
  },
  "published_ranges": {
    "bed_all_plates": "35-65",
    "chamber_temperatures": "20-45",
    "_drying": "50C 8h",
    "_hdt_0.45MPa": "56",
    "_vitrification": "63 (Vicat)",
    "_diameter_tolerance": "+/-0.02",
    "_notes": "Cardboard spool on some colours: wrap edges before AMS use."
  },
  "conflicts": [],
  "source_quality": "official_page",
  "sources": ["https://www.elegoo.com/products/elegoo-pla-plus-3d-printer-filament-1-75mm-colored-1kg"],
  "updated": "2026-11-02"
}
```
Allowed fields keys (one-element string arrays): nozzle_temperature_range_low, nozzle_temperature_range_high, filament_density, filament_diameter, filament_soluble ("1"/"0"), filament_is_support ("1"/"0"), filament_shrink (e.g. "99.6%"), filament_max_volumetric_speed (mm³/s, only if published).
Allowed published_ranges keys: bed_all_plates, cool_plate_temp, hot_plate_temp, textured_plate_temp, chamber_temperatures, fan_max_speed, fan_min_speed/fan_max_speed, filament_retraction_length, filament_retraction_speed, overhang_fan_threshold, and any key starting "_" (_drying, _nozzle_by_speed, _print_speed, _max_print_speed, _hardened_nozzle_required, _min_nozzle, _enclosure, _ams, _fiber_content, _hardness, _hdt_0.45MPa, _vicat, _vitrification, _diameter_tolerance, _annealing, _notes).
source_quality: official_tds | official_page | brand_amazon_listing | reseller_tds_copy. updated: "2026-11-02".

----- END R4 -----

## R5: kexcelled, colorfabb, formfutura, amazon-basics (39 items)

----- BEGIN R5 -----

GAP-FILL RUN R5 of 5 for a filament spec library (feeds an automatic Bambu Studio preset generator; printers Bambu Lab X2D, X1/X1C/X1E, P1S/P1P/P2S; nozzles 0.2/0.4/0.6/0.8 mm). An earlier automated fetch (plain web fetch, no browser) could NOT source the items listed below, mostly because sites blocked it (HTTP 402/403/429), pages were truncated, PDFs were unreadable as text, or it ran out of time. Your job: fill these specific gaps from published manufacturer sources and return JSON entries. Accuracy and sourcing matter more than coverage. Work through every brand listed; if you run out of budget, end with an exact list of items not reached.

ITEMS TO FILL (verbatim from the gap report):

### kexcelled
- **Kexcelled catalogue / product pages (kexcelled3d.com)** - missing: product-page values (colours, drying, AMS notes); all entries use the official TDS instead. Why: HTTP 429 on every Shopify storefront (kexcelled3d.com, kexcelled.com, myshopify and reseller Shopify stores), even after waiting; catalogue built from search results, daemon3dprint listing and an OFD audit issue <https://kexcelled3d.com/collections/filaments>
- **Kexcelled K9 PPA CF15** - missing: all. Why: not found (TDS filename guesses 404; product page 429) <https://cdn.shopify.com/s/files/1/0958/0111/4939/files/THE_K9_PPA_CF15_TDS.pdf>
- **Kexcelled K5 PLA Metal** - missing: all. Why: not found (404) <https://cdn.shopify.com/s/files/1/0958/0111/4939/files/THE_K5_PLA_Metal_TDS.pdf>
- **Kexcelled K5 PLA Pro** - missing: all. Why: not found (404) <https://cdn.shopify.com/s/files/1/0958/0111/4939/files/THE_K5_PLA_Pro_TDS.pdf>
- **Kexcelled K5 PETG ESD** - missing: all. Why: not found (404) <https://cdn.shopify.com/s/files/1/0958/0111/4939/files/THE_K5_PETG_ESD_TDS.pdf>
- **Kexcelled K5 ABS Pro** - missing: all. Why: not found (404) <https://cdn.shopify.com/s/files/1/0958/0111/4939/files/THE_K5_ABS_Pro_TDS.pdf>
- **Kexcelled K8 TPU Matte** - missing: all. Why: not found (404) <https://cdn.shopify.com/s/files/1/0958/0111/4939/files/THE_K8_TPU_Matte_TDS.pdf>
- **Kexcelled K8 TPU Air** - missing: all. Why: not found (404) <https://cdn.shopify.com/s/files/1/0958/0111/4939/files/THE_K8_TPU_Air_TDS.pdf>
- **Kexcelled K8 PP** - missing: all. Why: not found (404) <https://cdn.shopify.com/s/files/1/0958/0111/4939/files/THE_K8_PP_TDS.pdf>
- **Kexcelled K10 PPS CF10** - missing: all. Why: not found (404) <https://cdn.shopify.com/s/files/1/0958/0111/4939/files/THE_K10_PPS_CF10_TDS.pdf>
- **Kexcelled K5 PLA Magic / Color Change / Gradient / Streams / Coffee / Tea; K5 ABS Color Change** - missing: all. Why: not attempted (time)
- **Kexcelled K9 PEBA; K6 UCM 300; soft TPU grades 60A-80A** - missing: all. Why: not attempted (time)
- **Kexcelled K11/K12 PEEK, PEEK PRO, PEEK CF10, PEEK GF10, PEEK Ultra, PEKK, PPSU, PEI 1010, PEI 9085** - missing: all. Why: not attempted (time); these also need nozzle temperatures far above Bambu printers' limits

### colorfabb
- **ColorFabb HT** - missing: all (deliberately skipped). Why: not written: category returns 404 and HT Clear has no product page, so it looks discontinued (TDS still in the download folder) <https://colorfabb.com/filaments/materials/co-polyester-filaments/colorfabb-ht>

### formfutura
- **Formfutura EasyFil PLA** - missing: all. Why: not attempted (time); on sale (40% off), likely being replaced by EasyFil ePLA <https://formfutura.com/filaments/easyfil-pla>
- **Formfutura BioFil - Wood** - missing: all. Why: not attempted (time); page values were seen (180-200C, bed 40-50C, nozzle >= 0.8mm) but the TDS was not read <https://formfutura.com/filaments/biofil-wood>
- **Formfutura MetalFil - Ancient Bronze** - missing: all. Why: not attempted (time); density 3.5 is also outside the validator range <https://formfutura.com/filaments/metalfil-ancient-bronze>
- **Formfutura MetalFil - Brass** - missing: all. Why: not attempted (time); page gives a single 190C print temp and density 3.5 <https://formfutura.com/filaments/metalfil-brass>
- **Formfutura ReForm - Organic rPLA** - missing: all. Why: not attempted (time) <https://formfutura.com/filaments/reform-organic-rpla>
- **Formfutura ABSpro Flame Retardant** - missing: all. Why: not attempted (time) <https://formfutura.com/filaments/abspro-flame-retardant>
- **Formfutura EasyFil ABS - Glow in the Dark** - missing: all. Why: not attempted (time) <https://formfutura.com/filaments/easyfil-abs-glow-in-the-dark>
- **Formfutura ReForm - rApollo** - missing: all. Why: not attempted (time) <https://formfutura.com/filaments/reform-rapollo>
- **Formfutura ApolloX Kevlar** - missing: all. Why: not attempted (time) <https://formfutura.com/filaments/apollox-kevlar>
- **Formfutura ApolloX Flame Retardant** - missing: all. Why: not attempted (time) <https://formfutura.com/filaments/apollox-flame-retardant>
- **Formfutura STYX PA6-GF30** - missing: all. Why: not attempted (time) <https://formfutura.com/filaments/styx-pa6-gf30>
- **Formfutura LUVOCOM 3F PAHT 9936 / PAHT 9825 / PAHT CF 9891 / PAHT CF 9742 / PAHT KK 50056 FR / PP CF 9928 / PPS CF 9938** - missing: all. Why: not attempted (time)
- **Formfutura LUVOCOM 3F PEKK 50082 / PEEK 9581 / PEEK CF 9676 / PEI 50236, PEI ULTEM 1010, PEI ULTEM 9085, PPSU** - missing: all. Why: not attempted (time); ultra-high-temperature grades beyond Bambu printer capability
- **Formfutura ReForm - rTPU 85A** - missing: all. Why: not attempted (time) <https://formfutura.com/filaments/reform-rtpu-85a>
- **Formfutura ReForm - rTPU 90A** - missing: all. Why: not attempted (time) <https://formfutura.com/filaments/reform-rtpu-90a>
- **Formfutura FlexiFil TPC 30D** - missing: all. Why: not attempted (time) <https://formfutura.com/filaments/flexifil-tpc-30d>
- **Formfutura BioFil - PCL** - missing: all. Why: not attempted (time); print temp 95-130C is below the library's 150C field floor <https://formfutura.com/filaments/biofil-pcl>
- **Formfutura AthenaX CF10** - missing: all. Why: not attempted (time) <https://formfutura.com/filaments/athenax-cf10>
- **Formfutura AthenaX GF10** - missing: all. Why: not attempted (time) <https://formfutura.com/filaments/athenax-gf10>
- **Formfutura Atlas Support** - missing: all. Why: not attempted (time); page values were seen (180-210C, bed 0-60C, density 1.23) <https://formfutura.com/filaments/atlas-support>
- **Formfutura COMPOST3D 2** - missing: all. Why: not attempted (time); the TDS was read (190-230C, bed 40-60C, density 1.20-1.25) but the material is a hemicellulose compound with no clear Bambu material or parent <https://formfutura.com/web/content/342993?download=true>

### amazon-basics
- **Amazon Basics PLA** - missing: nozzle temp, bed temp, density, diameter tolerance, drying. Why: official manual copy returned 403 (HTML and PDF); the Amazon listing B07SZLYWS2 gives no temperatures <https://manuals.plus/amazon-basics/b09yrd4ztw-pla-3d-printer-filament-manual.pdf>
- **Amazon Basics PETG** - missing: all. Why: mirror sites returned 403, Amazon search returned 503, Amazon ASIN not found (web search budget used up) <https://www.desertcart.lk/products/705048331-amazon-basics-petg-3d-printer-filament-1-75-mm-yellow>
- **Amazon Basics TPU** - missing: all (incl. Shore hardness). Why: reseller page returned 403; Amazon ASIN not found (web search budget used up) <https://www.ypc.co.uk/product/amazon-basics-tpu-3d-printer-filament-1-75-mm-blue-1-kg-spool-2-2-lbs/>
- **Amazon Basics PLA** - missing: nozzle temp, bed temp, density, diameter tolerance. Why: blocked/403 (as the researcher reported; it is not a cited source and was not retried) <manuals.plus copy of the Amazon Basics PLA manual (B09YRD4ZTW / B07SZLYWS2)>

HOW TO HANDLE EACH ITEM
- "missing: all" → produce a full new entry for that line.
- "missing: <specific values>" → produce a full entry for that line containing every value you can source (the importer refreshes the library entry by re-importing the full entry under the same vendor + product spelling), and make sure the listed missing values are filled if a source publishes them.
- If a value genuinely isn't published anywhere, leave it out and say so in _notes. If a line is discontinued and not widely sold, list it at the end instead of writing an entry.
- Use EXACTLY the vendor + product spelling used in the item list so the importer matches existing entries.
- The earlier fetch was blocked by many storefronts (Shopify 429 rate limits, Amazon pages too large, Micro Center 403). Try the brand's own TDS PDFs (often on cdn.shopify.com or the brand's wiki/support site), the brand's official Amazon storefront/listing, regional storefronts, and reseller-hosted copies of the official TDS (mark reseller_tds_copy). Read image-only PDFs visually where you can.

RULES
- Every value needs a source. Prefer, in order: official TDS/datasheet PDF → official product page → brand's own marketplace listing → reseller copy of the TDS. Record which in source_quality.
- Published ranges are bounds. Copy as printed ("200-230"). Never invent a midpoint, never widen or narrow a range, never fill a value the sources don't give: leave it out. A single printed value like "250±5" is not a range; record it in published_ranges, not fields.
- When several ranges are given (normal vs high-speed, per grade), record all in published_ranges._nozzle_by_speed and put the HIGHEST range in fields.nozzle_temperature_range_low/high.
- Do NOT set temperature_vitrification in fields. Put Tg / Vicat / HDT under published_ranges (_vitrification, _vicat, _hdt_0.45MPa) with the metric named.
- Conflicting sources: keep the official (newest official) value in fields, list others in conflicts with their source.
- Density g/cm³ (validator accepts 0.5-3.0; put higher values in _notes), diameter mm, temperatures °C (nozzle field floor 150 °C), drying "<temp>C <hours>h" (keep ">" if printed, e.g. "50C >8h").
- bambu_parent: closest Bambu Studio system filament preset; prefer the brand's own system preset if Bambu Studio ships one (e.g. "Overture PLA", "SUNLU PLA+"); otherwise Bambu Lab's own product for that material/variant ("Bambu PLA Basic", "Bambu PLA Matte", "Bambu PETG HF", "Bambu PETG Basic", "Bambu ABS", "Bambu ASA", "Bambu TPU 95A HF", "Bambu PA6-CF", "Bambu PC"); "Generic <material>" only when nothing closer exists. No "@BBL <printer>" suffix. Say in _notes if not confirmed.
- Note printer-relevant info: AMS compatibility, hardened nozzle required, enclosure/chamber needs, minimum nozzle size, max volumetric speed if published. Lines needing >300 °C nozzle are beyond the target printers: still record specs, and say so in _notes.

OUTPUT FORMAT
JSON in fenced ```json blocks (one per brand), arrays of entries, then a final list of: items you could not fill (with reason), lines found discontinued.

Entry schema example:
```json
{
  "schema_version": 1,
  "vendor": "ELEGOO",
  "product": "PLA+",
  "material": "PLA",
  "colors": ["Red", "Neon Green", "Yellow"],
  "bambu_parent": "Bambu PLA Basic",
  "fields": {
    "nozzle_temperature_range_low": ["200"],
    "nozzle_temperature_range_high": ["230"],
    "filament_density": ["1.30"],
    "filament_diameter": ["1.75"]
  },
  "published_ranges": {
    "bed_all_plates": "35-65",
    "chamber_temperatures": "20-45",
    "_drying": "50C 8h",
    "_hdt_0.45MPa": "56",
    "_vitrification": "63 (Vicat)",
    "_diameter_tolerance": "+/-0.02",
    "_notes": "Cardboard spool on some colours: wrap edges before AMS use."
  },
  "conflicts": [],
  "source_quality": "official_page",
  "sources": ["https://www.elegoo.com/products/elegoo-pla-plus-3d-printer-filament-1-75mm-colored-1kg"],
  "updated": "2026-11-02"
}
```
Allowed fields keys (one-element string arrays): nozzle_temperature_range_low, nozzle_temperature_range_high, filament_density, filament_diameter, filament_soluble ("1"/"0"), filament_is_support ("1"/"0"), filament_shrink (e.g. "99.6%"), filament_max_volumetric_speed (mm³/s, only if published).
Allowed published_ranges keys: bed_all_plates, cool_plate_temp, hot_plate_temp, textured_plate_temp, chamber_temperatures, fan_max_speed, fan_min_speed/fan_max_speed, filament_retraction_length, filament_retraction_speed, overhang_fan_threshold, and any key starting "_" (_drying, _nozzle_by_speed, _print_speed, _max_print_speed, _hardened_nozzle_required, _min_nozzle, _enclosure, _ams, _fiber_content, _hardness, _hdt_0.45MPa, _vicat, _vitrification, _diameter_tolerance, _annealing, _notes).
source_quality: official_tds | official_page | brand_amazon_listing | reseller_tds_copy. updated: "2026-11-02".

----- END R5 -----
