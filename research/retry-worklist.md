# Retry worklist (triaged from unreachable.md, 2026-11-01)

These items from unreachable.md failed for reasons another pass could fix: a block (HTTP 402/403/406/429), a fetch limit (truncated page, zip too large, a 404 on a guessed filename), an unreadable PDF, search-snippet values nobody verified, or 'not attempted (time)'. Each batch R1-R5 below is one Research-mode run.
Items whose reason was 'no specs published', 'TDS does not print it', a validator limit or discontinued are under 'Left out' at the end: another pass won't fill them.

- Retryable: 223 items in 5 batches
- Left out (unfillable): 187

## Batch R1: bambu-lab-pla, bambu-lab-other, polymaker-b, esun (45 items)

### bambu-lab-pla
- **Bambu Lab PLA Basic Gradient** - missing: all (no entry written; may share the PLA Basic entry). Why: no separate TDS found; retailer pages describe it as a PLA Basic series colour using the PLA Basic profile. Bambu store pages (us.store.bambulab.com) return HTTP 402 and eu/uk redirect there <https://stemfinity.com/products/bambu-lab-pla-basic-gradient>
- **Bambu Lab PLA Lite** - missing: official TDS confirmation of nozzle range 190-240, bed 35-65, drying 50C 8h, max volumetric speed 16; diameter not stated by any source; Tg, chamber temp, retraction. Why: no official TDS found and the official store is blocked (402). Entry written from a Bambu PLA Lite product sheet hosted by a reseller (bigdipper.com.ar), plus density from the official PLA Pure TDS comparison table <https://us.store.bambulab.com/products/pla-lite>
- **Bambu Lab PLA Silk Multi-Color** - missing: confirmation of the current product name only. Why: its TDS file is the same V3.0 'PLA Silk' sheet, so it is folded into the PLA Silk entry rather than given its own entry; the current product page could not be read to confirm the naming (store 402) <https://cdn.shopify.com/s/files/1/0584/7236/6216/files/Bambu_PLA_Silk_Dual_Color_Technical_Data_Sheet.pdf>
- **Bambu Lab official store/filament pages (all lines)** - missing: product-page values (diameter tolerance, colour lists) for all lines. colors left empty except PLA Lite. Why: bambulab.com returned 403; us.store.bambulab.com returned 402; regional stores redirect to the US store <https://bambulab.com/en/filament>

### bambu-lab-other
- **Bambu Lab PETG Matte** - missing: official-host TDS URL; cooling fan range (TDS says only 'Turn on'). Why: Bambu store returns HTTP 402 to fetch; no official-host TDS found. Entry written from the TDS V1.0 copy that 3DJake hosts (reseller_tds_copy) <https://us.store.bambulab.com/products/petg-matte>
- **Bambu Lab PETG Translucent** - missing: official-host TDS URL. Why: Bambu store returns HTTP 402; no official-host TDS found. Entry written from the TDS V1.0 copy that additive-x hosts (reseller_tds_copy) <https://us.store.bambulab.com/products/petg-translucent>
- **Bambu Lab PPA-CF** - missing: official-host TDS URL; cooling fan range (TDS says only 'Turn on'). Why: Bambu store blocked (402/redirect); entry written from the TDS V1.0 copy that additive-x hosts (reseller_tds_copy) <https://eu.store.bambulab.com/en-pl/products/ppa-cf>
- **Bambu Lab PAHT-CF** - missing: check of the V3.0 values. Why: not attempted (time): entry uses TDS V2.0; a newer V3.0 seen in search results was not read <https://uwaterloo.ca/rapid-prototyping-centre/sites/default/files/uploads/documents/bambu_paht-cf_technical_data_sheet_v2.pdf>
- **Bambu Lab (all lines)** - missing: confirmation of the full current catalogue and colour lists (colors left empty in every entry); discontinued status of PA-CF, ASA-CF and TPU 95A. Why: blocked: Bambu store and wiki.bambulab.com return HTTP 402 to fetch; the catalogue list was built from TDS file names, Bambu Studio presets and search results, so a 2025-2026 non-PLA launch could be missing <https://us.store.bambulab.com/collections/filament>

### polymaker-b
- **Polymaker PC-PBT** - missing: all. Why: not attempted: appears discontinued (TDS only, not sold in the US shop, no product wiki page) <https://cdn.shopify.com/s/files/1/0548/7299/7945/files/Polymaker_PC_PBT_TDS_EN_V5.4.pdf>
- **Polymaker Fiberon PET-GF15** - missing: Tg, Vicat, HDT (entry written with print settings and density). Why: PDF text layer has the thermal table misaligned, so values could not be matched to rows <https://fiberon.polymaker.com/wp-content/uploads/TDS_FIBERON-PET-GF15_V1.0_EN.pdf>
- **Polymaker Fiberon ASA-CF08** - missing: Tg, HDT, chamber temperature value. Why: PDF text layer garbled for most thermal rows; only Vicat (110.8) was clear <https://fiberon.polymaker.com/wp-content/uploads/TDS_FIBERON-ASA-CF08_V1.0_EN.pdf>
- **Polymaker Matte PLA for Production** - missing: HDT 0.45/1.8 MPa. Why: image-only TDS (read visually); the HDT curve legend does not show which load each value belongs to <https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/pla/matte-pla-for-production>
- **Polymaker HT-PLA Pro** - missing: none. Why: The wiki TDS page is image-only (TDS V1.2 JPG). It was checked against TDS V1.4, the PDF linked from the cited shop page, which is now added to sources. All values were found. <https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/pla/ht-pla-pro>

### esun
- **eSUN (all lines) official site** - missing: official_page confirmation for all 47 written entries. Why: blocked/403 on www, eu. and au. esun3d.com; TDS PDFs read from spoolscout-hosted copies instead <https://www.esun3d.com/>
- **eSUN PLA, PLA-Matte Dual, ASA+, ePAHT-CF** - missing: HDT. Why: HDT value not legible in PDF text extraction (two-column layout) <https://assets.spoolscout.com/tds-sds/esun/tds/esun-asa-plus-tds-v1.0-2024-06.pdf>
- **eSUN PETG-Matte** - missing: drying hours. Why: drying duration not legible in text extraction <https://assets.spoolscout.com/tds-sds/esun/tds/esun-petg-matte-tds-v1.0-2025-07.pdf>
- **eSUN ABS Odorless** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/abs-abs-odorless>
- **eSUN ABS-ESD** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/abs-abs-esd>
- **eSUN eABS-HT** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/abs-abs-ht>
- **eSUN eABS-Max** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/abs-eabs-max>
- **eSUN eClean** - missing: all. Why: not attempted (time; cleaning filament) <https://www.spoolscout.com/data-sheets/esun/cleaning-eclean>
- **eSUN ePA** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/nylon-epa>
- **eSUN ePA-GF** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/nylon-glass-fiber-epa-gf>
- **eSUN ePA12** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/nylon-12-epa12>
- **eSUN PC-ESD** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/pc-pc-esd>
- **eSUN PC-HT** - missing: all. Why: not attempted (time); TDS text extraction mostly empty (Chinese/image text) <https://assets.spoolscout.com/tds-sds/esun/tds/esun-pc-ht-tds-v1.0-2024-07.pdf>
- **eSUN PEBA-90A** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/peba-peba-90a>
- **eSUN ePEEK Pro** - missing: all. Why: not attempted (time; beyond Bambu printer range) <https://www.spoolscout.com/data-sheets/esun/peek-epeek-pro>
- **eSUN PEEK-Industrial** - missing: all. Why: not attempted (time; beyond Bambu printer range) <https://www.spoolscout.com/data-sheets/esun/peek-peek-industrial>
- **eSUN PET** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/pet-pet>
- **eSUN PET-FR** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/pet-pet-fr>
- **eSUN PETG Refilament** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/petg-petg-refilament>
- **eSUN PETG-ESD** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/petg-petg-esd>
- **eSUN PLA CMYK** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/pla-pla-cmyk>
- **eSUN PLA-Clear Rainbow** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/pla-pla-clear-rainbow>
- **eSUN PLA-Magic** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/pla-pla-magic>
- **eSUN PLA-Matte Rainbow** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/pla-pla-matte-rainbow>
- **eSUN PLA-Silk Candy** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/pla-pla-silk-candy>
- **eSUN PLA-Silk Rainbow** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/pla-pla-silk-rainbow>
- **eSUN PLA-UV Color Change** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/pla-pla-uv-color-change>
- **eSUN Luminous PLA Rainbow** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/pla-luminous-pla-rainbow>
- **eSUN eTPU-LW** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/tpu-tpu-lw>
- **eSUN TPU-64D** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/tpu-rigidhigh-hardness-tpu-64d>
- **eSUN TPE-83A** - missing: all. Why: not attempted (time) <https://www.spoolscout.com/data-sheets/esun/tpe-tpe-83a>

## Batch R2: sunlu, overture, jayo, kingroon, hatchbox, inland, creality, anycubic, prusament (44 items)

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

## Batch R3: push-plastic, atomic-filament, fiberlogy, extrudr, spectrum, eryone, geeetech, sovol, qidi-tech, flashforge (44 items)

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

## Batch R4: 3dxtech (51 items)

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

## Batch R5: kexcelled, colorfabb, formfutura, amazon-basics (39 items)

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

## Left out (unfillable)

- [bambu-lab-pla] **Bambu Lab PLA Pure** - missing: filament diameter. Why: TDS read fine but does not print a filament diameter <https://store.bblcdn.com/s7/default/ecb663b46ebb4fb984786d33befb8d2f/PLA_Pure_TDS.pdf>
- [bambu-lab-other] **Bambu Lab TPU for AMS** - missing: whether max print speed is <250 or <=250. Why: the comparison glyph before the printing speed (250 mm/s) would not extract from the PDF <https://cdn.shopify.com/s/files/1/0584/7236/6216/files/Bambu_TPU_for_AMS_Technical_Data_Sheet.pdf>
- [polymaker-a] **Polymaker PolyLite Metallic PLA Pro** - missing: all. Why: no specs published (the product page reuses the generic PLA Pro text and there is no line-specific TDS) <https://shop.polymaker.com/products/polylite-metallic-pla-pro>
- [polymaker-a] **Polymaker PolyLite Translucent PETG** - missing: all. Why: no specs published (generic PolyLite PETG page text, no line-specific TDS) <https://shop.polymaker.com/products/polylite-translucent-petg>
- [polymaker-a] **Polymaker PolyLite Galaxy ABS** - missing: all. Why: no specs published (generic PolyLite ABS page text, no line-specific TDS; a glitter fill may change density) <https://shop.polymaker.com/products/polylite-galaxy-abs>
- [polymaker-a] **Polymaker PolyLite Metallic ABS** - missing: all. Why: no specs published (generic PolyLite ABS page text, no line-specific TDS) <https://shop.polymaker.com/products/polylite-abs-metallic>
- [polymaker-a] **Polymaker PolyLite Neon ABS** - missing: all. Why: no specs published (generic PolyLite ABS page text, no line-specific TDS) <https://shop.polymaker.com/products/polylite-neon-abs>
- [polymaker-a] **Polymaker Galaxy ASA** - missing: all. Why: no specs published (generic ASA page text, no line-specific TDS) <https://shop.polymaker.com/products/polymaker-galaxy-asa>
- [polymaker-a] **Polymaker PolyTerra PLA** - missing: official source, drying, diameter, colours. Why: no official TDS or product page readable (product removed from Polymaker shop/TDS index; official page renders through JS); used a reseller-hosted copy of TDS V5.1 <https://polymaker.com/the_latest/polyterra-pla/>
- [polymaker-a] **Polymaker PolyTerra PLA+** - missing: official source, drying, diameter, colours. Why: only a reseller-hosted copy of TDS V5.1 found; no official page <https://cdn.shopify.com/s/files/1/0789/2979/files/PolyTerra_PLA_Plus_EN_V5.1.pdf>
- [polymaker-a] **Polymaker PolyLite PLA Pro** - missing: drying. Why: TDS does not publish a drying setting <https://cdn.shopify.com/s/files/1/0548/7299/7945/files/Polylite_PLA_Pro_TDS_EN_V5.4.pdf>
- [polymaker-a] **Polymaker PLA Pro / PETG / ASA / PolyLite PETG / PLA-CF / LW-PLA / CosPLA** - missing: filament_diameter. Why: the TDS and product pages give no filament diameter (product pages show no diameter option)
- [polymaker-b] **Polymaker Wood PLA** - missing: nozzle temp, bed temp, drying, thermal (entry not written). Why: no specs published: no wiki page or TDS found; the shop page gives only density 0.8 g/cm3 and spool dimensions <https://shop.polymaker.com/products/polymaker-wood-pla>
- [polymaker-b] **Polymaker Fiberon PA612-CF15** - missing: Tg. Why: TDS publishes Tg as N/A <https://cdn.shopify.com/s/files/1/0548/7299/7945/files/TDS_FIBERON_PA612-CF15_V1.1_EN.pdf>
- [polymaker-b] **Polymaker PolyMax PLA** - missing: single density value (range kept in published_ranges). Why: TDS gives density only as a range (1.17-1.24) <https://cdn.shopify.com/s/files/1/0548/7299/7945/files/PolyMax_PLA_TDS_EN_V5.4.pdf>
- [polymaker-b] **Polymaker PolyFlex TPU95** - missing: single density value, max volumetric speed. Why: TDS gives density only as a range (1.20-1.24) <https://cdn.shopify.com/s/files/1/0548/7299/7945/files/PolyFlex_TPU95_TDS_EN_V5.4.pdf>
- [polymaker-b] **Polymaker PolySupport for PLA / PolySupport for PA12 / PolyDissolve S1 / PolyFlex TPU90/95/95-HF** - missing: Tg, Vicat, HDT (PolySupport for PA12 has Vicat and HDT); max volumetric speed for TPU lines. Why: TDS does not publish thermal properties for these lines
- [polymaker-b] **Polymaker Panchroma lines (all except CoPE)** - missing: per-line density (group values used, matched through the wiki's printing-profile grouping); Tg and HDT not published. Why: the Panchroma TDS gives density and Vicat only per group (Basic/CoPE/Matte/Satin/Silk/Others), not per line <https://cdn.shopify.com/s/files/1/0548/7299/7945/files/TDS_PANCHROMA_V2.pdf>
- [esun] **eSUN (all 47 written lines)** - missing: filament_diameter, diameter tolerance. Why: TDS does not state filament diameter/tolerance
- [esun] **eSUN PETG-Basic** - missing: nozzle range low/high, drying duration. Why: nozzle printed as single value 250+/-5C, not a range <https://assets.spoolscout.com/tds-sds/esun/tds/esun-petg-basic-tds-v1.0-2024-07.pdf>
- [esun] **eSUN PLA-Metal** - missing: density. Why: density printed as '<1.24' (not a point value) <https://assets.spoolscout.com/tds-sds/esun/tds/esun-pla-metal-tds-v1.0-2026-12.pdf>
- [esun] **eSUN older v4.0 TDS lines (PLA+HS, ePLA-HS, PLA, ST, CF, GF, LW, Lite, Luminous, Stars, Gloss, Silk Magic/Mystic, Twinkling, Marble, Chameleon, PETG+HS, ABS, ABS+, eABS+HS, eABS-CF/GF, ASA+, HIPS)** - missing: drying. Why: no drying recommendation published (N/A) in TDS
- [esun] **eSUN PEBA-LW** - missing: all. Why: no TDS link found <https://www.spoolscout.com/data-sheets/esun/peba-peba-lw>
- [sunlu] **SUNLU ABS 2.0** - missing: all. Why: no specs published: the product page has no parameter table and no TDS link. A web search found only the standard ABS / High Speed ABS figures, none for ABS 2.0 <https://www.sunlu.com/products/ABS2.0>
- [sunlu] **SUNLU PP** - missing: density. Why: no specs published (the TDS and the page both print density as '/') <https://media.sunlu.com/prod/20260413/fbfe6e74-b29f-4f0f-a9b3-84aaa6b2fc85.pdf?filename=TDS>
- [sunlu] **SUNLU PCL** - missing: nozzle fields, bed temp, retraction, drying, HDT. Why: no specs published; the published nozzle range 75-85C is below the validator's 150C floor, so it is kept only in published_ranges <https://media.sunlu.com/prod/20260414/9c709eea-12c7-4a05-b5cd-227c63c700b8.pdf?filename=TDS>
- [sunlu] **SUNLU PVA** - missing: drying. Why: no specs published (the TDS prints drying temperature as '/') <https://media.sunlu.com/prod/20260330/6f3c0e89-fa56-46b2-ab3d-601ee6b70cf9.pdf?filename=TDS>
- [sunlu] **SUNLU Silk TPU** - missing: HDT, Tg, Vicat. Why: no specs published <https://media.sunlu.com/prod/20260330/04545ebf-ef5c-4fd9-b425-42a06d39c7c0.pdf?filename=TDS>
- [sunlu] **SUNLU PLA Galaxy / PLA Rainbow / PLA Transparent Rainbow / Silk PLA+ Rainbow** - missing: full colour list. Why: not found: the page shows only the default colour name, with no colour table <https://www.sunlu.com/products/galaxy-pla-filament>
- [elegoo] **ELEGOO PET-CF** - missing: diameter (page never states 1.75 mm), diameter tolerance. Why: no specs published <https://us.elegoo.com/products/pet-cf>
- [elegoo] **ELEGOO PLA Glow** - missing: diameter, diameter tolerance. Why: no specs published <https://us.elegoo.com/products/pla-glow>
- [elegoo] **ELEGOO PC-FR** - missing: diameter, diameter tolerance. Why: no specs published <https://us.elegoo.com/products/pc-fr>
- [elegoo] **ELEGOO PLA Wood** - missing: diameter, diameter tolerance. Why: no specs published <https://us.elegoo.com/products/pla-wood>
- [elegoo] **ELEGOO ASA-CF** - missing: diameter, diameter tolerance. Why: no specs published <https://us.elegoo.com/products/asa-cf>
- [elegoo] **ELEGOO Rapid TPU 95A / TPU 95A** - missing: Vicat and HDT (listed as N/A). Why: no specs published <https://us.elegoo.com/products/rapid-tpu-filament-1-75mm-colored-1kg>
- [elegoo] **ELEGOO (all lines)** - missing: official TDS PDFs (none linked from product pages); max volumetric speed; retraction/fan settings. Why: no specs published
- [overture] **OVERTURE Air PLA** - missing: colors, official product page. Why: no current official product page found; only TDS plus reseller listing
- [overture] **OVERTURE Easy Nylon** - missing: drying temp/time. Why: no specs published <https://overture3d.com/cdn/shop/files/OVERTURE_EASY_NYLON_TDS_EN_V5.1_b6ce0042-6686-42dd-a5ab-696d2cc734b8.pdf>
- [overture] **OVERTURE PLA / Silk PLA / Super PLA+ / Easy PLA / Rock PLA / Turbo PLA / Air PLA / Eco PLA / High Speed TPU 95A / ABS** - missing: drying temp/time, max volumetric speed. Why: no specs published in TDS or product page
- [overture] **OVERTURE Glow PLA / Shimmer PLA** - missing: line-specific density/temps if they differ from Easy PLA. Why: no line-specific TDS (Glow page links Easy PLA TDS, Shimmer page mis-links Easy Nylon TDS); folded into Easy PLA entry <https://overture3d.com/products/overture-glow-pla>
- [overture] **OVERTURE Carbon Fiber PLA** - missing: all (not written). Why: appears discontinued (not in catalogue, no current listings found); TDS v1.1 Jan 2024 exists but not written <https://cdn.shopify.com/s/files/1/0207/3624/5824/files/OVERTURE_CF_PLA_TDS_EN.pdf>
- [overture] **OVERTURE Eco PLA** - missing: diameter. Why: not found (redirects to the overture3d.com homepage) <https://overture3d.com/products/overture-eco-pla-filament-1-75mm-1>
- [jayo] **JAYO (all lines)** - missing: density, drying, Tg/HDT for every line except PA6-CF/PA6-GF/PA12-CF HDT. Why: no specs published: JAYO publishes no density on any product page; the lab-report blog post describes TDS-style data but links no PDF/table (images only) <https://jayo3d.com/blogs/news/properties-parameters-of-jayo-filaments>
- [jayo] **JAYO High Speed PLA+** - missing: nozzle temp, bed temp, density. Why: no specs published in text (temps likely in images only) <https://store.jayo3d.com/products/jayo-high-speed-pla-1-1kg-3d-printing-filament-bundle>
- [jayo] **JAYO High Speed PLA+ 2.0** - missing: all. Why: only appears as a variant option in a collection listing; no product page or specs; no entry written <https://store.jayo3d.com/products/jayo-basic-filament-collection-pla-pla-matte-high-speed-series>
- [jayo] **JAYO High Speed Marble PLA** - missing: nozzle temp, bed temp, density. Why: no specs published (only speed and tolerance) <https://store.jayo3d.com/products/reusable-spool-jayo-high-speed-marble-pla-600mm-s-high-speed-3d-printer-non-toxic-filament-1-1kg-roll-reusable-spool>
- [jayo] **JAYO PLA Galaxy** - missing: nozzle temp, bed temp, density, abrasiveness. Why: no specs published (only diameter/tolerance) <https://store.jayo3d.com/products/reusable-spooljayo-pla-galaxy-3d-printer-filament-1-75mm-glitter-sparkle-pla-colorful-twinkling-1-1kg-galaxy-green-black-purple-for-fdm-printer>
- [jayo] **JAYO Dual-Color Matte PLA** - missing: nozzle temp, bed temp, density. Why: no specs published (only diameter/tolerance) <https://store.jayo3d.com/products/moq-4-jayo-dual-color-matte-pla-3d-printing-filament-1-75mm-1-1kg-spool-2-4-lbs-dimensional-accuracy-0-02mm>
- [jayo] **JAYO PLA Rainbow / PLA Transparent Rainbow** - missing: nozzle temp, bed temp, density. Why: no specs published (only tolerance); may just be colourways of JAYO PLA (already in library); no entry written <https://store.jayo3d.com/products/reusable-spool-jayo-pla-rainbow-1-1kg-3d-filament>
- [jayo] **JAYO PETG Glow** - missing: all. Why: listing sells PETG Glow but publishes only PLA Glow settings; no entry written <https://store.jayo3d.com/products/moq-4-rolls-jayo-pla-glow-in-the-dark-luminous-3d-printer-filament-1-75mm-1-1kg>
- [jayo] **JAYO PLA Meta** - missing: density, diameter tolerance. Why: no specs published beyond temps/speed <https://store.jayo3d.com/products/reusable-spooljayo-1-1kg-pla-meta-3d-printer-filament>
- [jayo] **JAYO High Speed Matte PLA** - missing: density, diameter tolerance. Why: no specs published <https://store.jayo3d.com/products/jayo-high-speed-matte-pla-1-1kg-reusable-spool-3d-printing-filament>
- [jayo] **JAYO PA6-CF / PA6-GF / PA12-CF** - missing: density, drying, diameter tolerance, HDT load (0.45 vs 1.8 MPa). Why: no specs published <https://store.jayo3d.com/products/jayo-1kg-pa6-cf-nylon-carbon-fiber-3d-printer-filament-1-75mm-heat-resistant>
- [kingroon] **Kingroon TPU 85A Rainbow** - missing: all. Why: sold only as variants on the TPU page; no specs published for 85A <https://kingroon.com/products/kingroon-tpu>
- [kingroon] **Kingroon HS-PETG (bulk listing)** - missing: all (PETG HS TDS entry written separately). Why: no specs published on the page; could not confirm it is the same product as the PETG HS TDS <https://kingroon.com/products/10kg-hs-petg-high-speed-printer-filament-1-75mm-for-us-only>
- [kingroon] **Kingroon PA Nylon Basic (current listing)** - missing: density, drying, HDT; confirmation that the older listing matches current product. Why: current page has no specs; entry 'PA Nylon' uses an older kingroon.com PA6 listing; Amazon B0H3JN8D78 unavailable <https://kingroon.com/products/kingroon-pa-nylon-basic-3d-printer-filament>
- [kingroon] **Kingroon Refill PLA** - missing: density, drying, HDT. Why: page gives only nozzle/bed/tolerance <https://kingroon.com/products/10kg-pla-refill-filament-with-no-spool>
- [kingroon] **Kingroon PLA Silk Tri-Color / Single Color / Rainbow, PLA+, HS-PLA, PETG Basic, PLA Chameleon** - missing: official TDS; retraction, chamber, max speed for most. Why: no TDS published on wiki.kingroon.com (probed filename variants); entries are product-page sourced
- [hatchbox] **Hatchbox (all lines) - TDS** - missing: density (except PLA), drying, Tg/HDT/Vicat, max volumetric speed, shrink for every line. Why: no specs published (no Hatchbox TDS found); only a PLA SDS exists
- [hatchbox] **Hatchbox PLA Refill** - missing: bed temp, density, drying. Why: no specs published beyond print temperature <https://www.hatchbox3d.com/products/3d-rs-pla1kg-red>
- [hatchbox] **Hatchbox Matte PLA / Silk PLA / Wood PLA / Shiny PLA / PLA Glow in the Dark / PLA Carbon Fiber / PLA Pro+ / PLA Max V2 / Performance PLA / PLA UV Color Changing / PLA Temperature Color Changing** - missing: bed temp, density, drying; CF and Glow lines: fibre content and hardened-nozzle requirement. Why: product pages only say 'No Heating Bed Required'; no line-specific data <https://www.hatchbox3d.com/pages/pla-material>
- [hatchbox] **Hatchbox Rapid PETG** - missing: bed temp, density, drying, max volumetric speed. Why: no specs published beyond temp and speed <https://www.hatchbox3d.com/products/3d-rpd-petg1kg-wht>
- [hatchbox] **Hatchbox TPU** - missing: bed temp, density, drying, retraction. Why: no specs published beyond temp and hardness <https://www.hatchbox3d.com/products/3d-tpu-1kg1-75-blk>
- [hatchbox] **Hatchbox PETG / ABS (Amazon listing)** - missing: cross-check of Amazon listing values. Why: Amazon page hides product details for bots ('add to cart to see details'); 1.5 MB page, bullets not reachable <https://www.amazon.com/HATCHBOX-3D-Filament-Dimensional-Accuracy/dp/B00J0GMMP6>
- [hatchbox] **Hatchbox PLA Metal** - missing: all. Why: not found on hatchbox3d.com (only in third-party OFD/SimplyPrint list); may be same as Shiny PLA or discontinued <https://simplyprint.io/filaments/hatchbox/pla-metal>
- [hatchbox] **Hatchbox PLA Basic** - missing: all. Why: not found on hatchbox3d.com (only in third-party OFD/SimplyPrint list) <https://simplyprint.io/filaments/hatchbox/pla-basic>
- [inland] **Inland Glitter PLA** - missing: all. Why: not found in official sources (only a third-party SimplyPrint DB)
- [inland] **Inland Galaxy PLA** - missing: all. Why: not found in official sources (only a third-party SimplyPrint DB)
- [inland] **Inland TPU for MFS** - missing: none removed; the kept 210-230 / 25-60 matches the cited 701526 listing, and the alternative is recorded as a conflict. Why: search index text conflicts: one result gives 220-240 / bed 30-35 / Shore D 62 for this item, another gives 210-230 / 25-60 / 90A <https://www.microcenter.com/product/701526/inland-175mm-tpu-3d-printer-filament-10-kg-(22-lbs)-cardboard-spool-black>
- [creality] **Creality Hyper PLA** - missing: density (resellers say 1.25), drying, HDT/Vicat. Why: store page specs are images or loaded by JavaScript; Amazon listing has no temperatures or density in its text <https://store.creality.com/products/hyper-series-pla-3d-printing-filament-1kg>
- [creality] **Creality Soleyin Ultra PLA** - missing: density, diameter tolerance, drying, HDT. Why: store page specs are images; only a Creality blog gives temperatures <https://store.creality.com/products/soleyin-ultra-pla-3d-printing-filament-1kg>
- [creality] **Creality Hyper ABS** - missing: all. Why: no specs in the official page text; only resellers (230-270 nozzle, 75-95 bed, HDT 76 vs 80 conflict) <https://store.creality.com/products/hyper-abs>
- [creality] **Creality Hyper PC** - missing: all. Why: no specs in the official page text (US/EU); no TDS found <https://store.creality.com/products/hyper-pc-filament-1-75mm-1kg>
- [creality] **Creality Hyper PLA CF** - missing: all. Why: no specs in the official page text (US/JP); resellers give 190-230 nozzle, 45 bed <https://store.creality.com/products/hyper-pla-cf>
- [creality] **Creality Hyper Rainbow PLA** - missing: all. Why: no specs in the official page text <https://store.creality.com/products/hyper-rainbow-pla-3d-printing-filament-1kg>
- [creality] **Creality Hyper PLA Luminous** - missing: all (including whether a hardened nozzle is needed). Why: no specs in the official page text <https://store.creality.com/products/hyper-luminous-pla-3d-printing-filament-1kg>
- [creality] **Creality Hyper PLA Stardust** - missing: all. Why: no specs in the official page text <https://store.creality.com/products/hyper-pla-rfid-stardust-3d-printing-filament-1kg>
- [creality] **Creality Hyper PLA Lightweight** - missing: nozzle range, bed, exact density, drying. Why: official page gives only 'density around 0.8 g/cm3' and foaming notes; a reseller (PB Tech) gives 210-270 nozzle <https://store.creality.com/products/hyper-lightweight-pla-3d-printing-filament-1kg>
- [creality] **Creality Soleyin Basic PETG** - missing: all. Why: no specs in the official page text; a Creality blog gives only 'up to 200 mm/s' <https://store.creality.com/products/soleyin-basic-petg-3d-printing-filament-1kg>
- [creality] **Creality Ender Fast PLA** - missing: all published ranges. Why: no specs in the official page text; only K2 Plus profile values (220C/50C, 23 mm3/s) <https://store.creality.com/products/ender-fast-1-75mm-pla-3d-printing-filament-pack-2kg>
- [creality] **Creality CR-PLA Fluo** - missing: all published ranges. Why: appears only in the K2 Plus profile table; no product page found <https://store.creality.com/blogs/all/creality-k2-plus-filament-parameters-settings>
- [creality] **Creality HP Ultra PLA** - missing: current status, density. Why: in the official parameter table (190-230, bed none-60) but not on the current store; not written as possibly discontinued <https://store.creality.com/uk/blogs/basics/creality-filaments-parameter-reference-table>
- [creality] **Creality HP-HIPS** - missing: current status, density. Why: in the official parameter table (220-260, bed 70-110) but not on the current store; not written as possibly discontinued <https://store.creality.com/uk/blogs/basics/creality-filaments-parameter-reference-table>
- [creality] **Creality CR-PA Carbon** - missing: current status, density, drying. Why: in the official parameter table (230-260, bed 80-90, env 60-80) but not on the current store; not written as likely discontinued <https://store.creality.com/uk/blogs/basics/creality-filaments-parameter-reference-table>
- [creality] **Creality CR-PLA / CR-PLA Matte / CR-TPU / CR-Wood / CR-PLA Carbon / Ender-PLA / Ender-PLA+ / HP-TPU / HP-ASA / CR-Silk (written)** - missing: density, drying, HDT/Vicat, diameter tolerance; TPU Shore hardness; HP-ASA density. Why: only Creality's parameter table is available; no TDS <https://store.creality.com/uk/blogs/basics/creality-filaments-parameter-reference-table>
- [creality] **Creality CR-PLA Carbon** - missing: none (covered by parameter table). Why: no specs published on product page <https://store.creality.com/products/cr-pla-carbon-3d-printing-filament-1kg>
- [creality] **Creality Ender-PLA** - missing: none (covered by parameter table). Why: no specs published on product page (pack/colours only) <https://store.creality.com/products/ender-pla-value-pack-2-spools-pack>
- [anycubic] **Anycubic (several written lines)** - missing: filament_diameter for ABS, TPU 95A, PLA Matte, PLA Metal, PLA Marble, PLA Silk, PLA-CF, PLA Galaxy, PA6-CF; colour lists for PLA Basic, ABS, ASA, TPU 95A, PLA Matte, PLA Glow, PLA Metal, PLA Marble, PLA-CF, PA6-CF. Why: TDS does not state filament diameter and the product page could not be re-read
- [prusament] **Prusament PETG Tungsten 75%** - missing: filament_density in fields (the TDS gives 4 g/cm3; recorded in _notes). Why: sourced, but the library validator rejects filament_density above 3.0 g/cm3 <https://prusament.com/wp-content/uploads/2023/03/TDS_Prusament-PETG-Tungsten-75_EN-1.pdf>
- [prusament] **Prusament (all 24 lines)** - missing: drying for most lines (only PETG V0, PC Space Grade, PA11, PEI 1010, TPU 95A and PVB give one); Tg and Vicat (only HDT is published, plus Vicat A for TPU); max volumetric speed (only PA11 gives one); retraction and shrink. Why: not published by Prusament
- [prusament] **Prusament Woodfill** - missing: base material type (material set to 'Wood-filled biobased polymer blend'; bambu_parent Bambu PLA Wood is my nearest-match choice). Why: base polymer not published (the TDS says only 'Biobased Polymer Blend') <https://prusament.com/materials/prusament-woodfill/>
- [siraya-tech] **Siraya Tech Flex TPU 95A Matte** - missing: nozzle temp, bed temp, density, drying, retraction, print speed. Why: no specs published (no TDS; product page gives only max flow 15 mm3/s, +/-0.03 tolerance) <https://siraya.tech/products/flex-tpu-95a-matte-filament>
- [siraya-tech] **Siraya Tech Flex TPU Air 95A** - missing: nozzle temp, bed temp, density, diameter, drying, retraction, print speed. Why: no specs published (no TDS; product page gives only max flow 12 mm3/s and 75A-95A hardness) <https://siraya.tech/products/flex-tpu-air-95a-filament>
- [siraya-tech] **Siraya Tech Rebound PEBA Air 95A** - missing: density (unfoamed filament). Why: no specs published for this value <https://siraya.tech/pages/siraya-tech-rebound-peba-air-70a-95a-tds>
- [siraya-tech] **Siraya Tech Rebound PEBA 95A** - missing: retraction length/speed. Why: no specs published for this value <https://siraya.tech/pages/siraya-tech-rebound-peba-95a-tds>
- [siraya-tech] **Siraya Tech Fibreheart ASA-GF** - missing: print speed, fan speed, diameter. Why: no specs published for these values <https://siraya.tech/pages/siraya-tech-fibreheart-asa-gf-tds>
- [siraya-tech] **Siraya Tech Flex TPU 85A / Flex TPU 95A / Flex TPU 64D / Fibreheart ABS-CF / ABS-CF Core / ABS-GF / PET-GF / PPA / PPA-CF Core** - missing: diameter tolerance (and diameter); ABS-GF also fibre content. Why: no specs published (TDS does not state these)
- [push-plastic] **Push Plastic Matte ABS** - missing: nozzle temp, bed temp, density, drying, HDT. Why: no specs published (the product page only says it prints like normal ABS; no print-settings sheet or TDS) <https://www.pushplastic.com/products/matte-abs-filament-1-75mm-1kg>
- [push-plastic] **Push Plastic HIPS** - missing: nozzle temp, bed temp, density, drying. Why: no specs published (the TDS has only mechanical data and HDT; no print-settings sheet) <https://cdn.shopify.com/s/files/1/0260/7421/files/Push_Plastic_HIPS_Technical_Data_sheet.pdf>
- [push-plastic] **Push Plastic Nylon** - missing: density, HDT. Why: no specs published (no TDS for unfilled Nylon) <https://www.pushplastic.com/pages/learn>
- [push-plastic] **Push Plastic TPU 100A** - missing: density, drying, HDT (only TPU 98A values exist). Why: the official TDS and print-settings sheet name TPU 98A, not 100A, so they were recorded as conflicts only <https://cdn.shopify.com/s/files/1/0260/7421/files/Technical_Data_Sheet_TPU98A_v1.0.pdf>
- [push-plastic] **Push Plastic Carbon Fiber PC+PBT** - missing: HDT. Why: no specs published (the TDS has no thermal section) <https://cdn.shopify.com/s/files/1/0260/7421/files/CF_PC_PBT_TDS.pdf>
- [push-plastic] **Push Plastic PEI 1010** - missing: density, HDT. Why: no specs published (no filament or resin density on the site; the SDS gives none) <https://cdn.shopify.com/s/files/1/0260/7421/files/Ultem_1010_MSDS.pdf>
- [atomic-filament] **Atomic Filament Carbon Fiber PLA** - missing: density, bed temp, Tg, drying. Why: no specs published (no CF TDS; the PLA SDS does not cover fibre fill)
- [atomic-filament] **Atomic Filament Carbon Fiber PETG** - missing: density, Tg. Why: no specs published (no CF TDS)
- [atomic-filament] **Atomic Filament Carbon Fiber PCTG PRO** - missing: density, Tg, drying, minimum nozzle size. Why: no specs published (no CF TDS)
- [atomic-filament] **Atomic Filament Carbon Fiber ABS** - missing: density, Tg, minimum nozzle size. Why: no specs published (no CF TDS)
- [atomic-filament] **Atomic Filament Carbon Fiber ASA** - missing: density. Why: no specs published (only the generic ASA SDS, specific gravity '1.07~', not CF-specific)
- [atomic-filament] **Atomic Filament PCTG PRO** - missing: drying. Why: no specs published (FAQ drying table covers PETG, not PCTG) <https://atomicfilament.com/pages/atomic-filament-faq>
- [atomic-filament] **Atomic Filament PLA / Silk PLA / Extreme Impact PLA / Hi-Flow Pro PLA / MeltMiser PLA** - missing: drying; bed temp for Impact/Hi-Flow/MeltMiser; max volumetric speed for Hi-Flow Pro. Why: no specs published (no PLA TDS; density and Tg come from the generic PLA SDS; bed temp printed only on 2 PLA pages and on Silk pages)
- [fiberlogy] **Fiberlogy rASA** - missing: filament_diameter (not published on the page). Why: the page links no TDS PDF; the page itself was readable <https://fiberlogy.com/en/filaments/asa-en/rasa-en/>
- [fillamentum] **Fillamentum Flexfill TPE 90A** - missing: official TDS, print speed, fan, Tg/Vicat/HDT. Why: no TDS linked on the product page; values taken from the product page only <https://shop.fillamentum.com/products/flexfill-tpe-90a-traffic-black>
- [fillamentum] **Fillamentum PETG HFFR** - missing: print speed, fan, colours. Why: page and TDS give no print speed, fan or colour list <https://shop.fillamentum.com/products/petg-hffr>
- [fillamentum] **Fillamentum PETG** - missing: Tg. Why: TDS lists Tg and melting temperature as '-' <https://fillamentum.com/wp-content/uploads/2023/02/TDS_PETG_EN_30012023.pdf>
- [fillamentum] **Fillamentum OrCA (0rCA)** - missing: print speed, fan. Why: the page and guide publish no print speed or fan values <https://shop.fillamentum.com/products/orca>
- [fillamentum] **Fillamentum ABS Extrafill / HIPS Extrafill / ASA Extrafill** - missing: Tg; HDT at 0.45 MPa for ABS. Why: the TDSs give HDT at 1.8 MPa only (ABS) and no Tg
- [extrudr] **Extrudr PETG Glow in the Dark** - missing: all. Why: not in the official Extrudr product catalogue; only reseller listings found, which give conflicting temperatures <https://www.3djake.com/extrudr/mf-petg-glow-in-the-dark>
- [extrudr] **Extrudr BioFusion Silk** - missing: all. Why: only a third-party listing; not in the official catalogue <https://simplyprint.io/filaments/extrudr>
- [extrudr] **Extrudr GreenTEC Matte** - missing: all. Why: only a third-party listing; not in the official catalogue (GreenTEC itself is described as matte) <https://simplyprint.io/filaments/extrudr>
- [extrudr] **Extrudr DuraPro PC/PBT CF** - missing: density, HDT. Why: this product's properties table repeats the DuraPro PA12 table, so it isn't reliable <https://s3.extrudr.com/extrudr-media/product-catalogue/extrudr-Produktkatalog_EN.pdf>
- [extrudr] **Extrudr TPU Flex Hard CF** - missing: max volumetric speed. Why: max volumetric speed isn't printed for this product <https://s3.extrudr.com/extrudr-media/product-catalogue/extrudr-Produktkatalog_EN.pdf>
- [extrudr] **Extrudr Flax / Pearl / Wood** - missing: max volumetric speed. Why: not published <https://s3.extrudr.com/extrudr-media/product-catalogue/extrudr-Produktkatalog_EN.pdf>
- [extrudr] **Extrudr Pearl** - missing: nozzle_temperature_range_low (field only). Why: the published low bound of 140 C is below the validator's 150 C floor, so that field was removed; the full range is kept in published_ranges._nozzle_published <https://s3.extrudr.com/extrudr-media/product-catalogue/extrudr-Produktkatalog_EN.pdf>
- [spectrum] **Spectrum AquaPrint** - missing: material, filament density (TDS prints nozzle 190-215, bed 25-70, fan 0-50%, speed 20-50 mm/s, Tg 60-65). Why: TDS read, but the base polymer is not published (it says only 'water-soluble support', compared against PVA) and it gives bulk density (0.6-0.9), not filament density; no entry written so the material is not guessed <https://spectrumfilaments.com/wp-content/uploads/2024/02/en_tds_spectrum_aquaprint.pdf>
- [spectrum] **Spectrum Prografen PLA Graphene Light / Graphene Strong, Prografen PET-G Graphene Light / Graphene Strong** - missing: density, diameter, Tg/HDT/Vicat, drying. Why: no TDS linked on the official product pages; entries written from product page only <https://spectrumfilaments.com/en/filament/prografen-pla-graphene-light/>
- [eryone] **Eryone PA6-GF** - missing: density, line-specific nozzle/bed, drying, HDT. Why: no line-specific TDS. Only the combined Nylon & Nylon-CF/GF listing has values (250-280C, bed 100-120C), which may not apply to the GF grade <https://eryone3d.com/products/nylon-filament>
- [eryone] **Eryone PA12-GF** - missing: density, line-specific nozzle/bed, drying, HDT. Why: no line-specific TDS; only the combined Nylon listing <https://eryone3d.com/products/nylon-filament>
- [eryone] **Eryone PLA High-Speed** - missing: density, drying, Vicat/HDT. Why: the TDS linked as 'PLA High-Speed' is actually the Hyper-Speed PLA+ sheet. The entry was written from the product page <https://cdn.shopify.com/s/files/1/0252/0412/9841/files/ERYONE-PLA_HP-TDS.pdf>
- [eryone] **Eryone PLA Silk** - missing: density, drying. Why: no TDS for single-colour silk; entry is from the product page only <https://eryone3d.com/products/silk-pla>
- [eryone] **Eryone PLA Ultra Silk** - missing: density, drying. Why: no TDS; entry is from the product page only <https://eryone3d.com/products/advanced-silk-pla>
- [eryone] **Eryone PLA Metallic** - missing: density, drying. Why: no TDS; entry is from the product page only <https://eryone3d.com/products/pla-metallic-filament>
- [eryone] **Eryone PLA Light-Weight** - missing: density, drying. Why: no TDS; entry is from the product page only <https://eryone3d.com/products/pla-light-weight-filament>
- [eryone] **Eryone PLA Lite Matte** - missing: density, drying, print speed. Why: no TDS; the product page gives only 'typical settings' <https://eryone3d.com/products/pla-lite-matte-filament-1-75mm-0-03mm-1kg>
- [eryone] **Eryone PLA Rainbow** - missing: bed temp, density, drying. Why: no TDS. The pages give only the nozzle range, and the Lagoon page swaps its bed and speed labels <https://eryone3d.com/products/pla-classical-rainbow>
- [eryone] **Eryone PETG Matte** - missing: density, drying, print speed. Why: no TDS; the product page gives only 'print settings' <https://eryone3d.com/products/petg-matte-filament-1-75mm-0-03mm-1kg>
- [eryone] **Eryone PETG Lite** - missing: density, drying. Why: no TDS; the product page gives only 'typical settings' <https://eryone3d.com/products/petg-lite-filament-1-75mm-0-03mm-1kg>
- [eryone] **Eryone TPU (95A), TPU 85A, TPU 90A, TPU Rainbow** - missing: density, drying (TPU Rainbow also missing hardness). Why: no TDS (only High-Speed TPU has one); entries are from the product pages <https://eryone3d.com/products/tpu>
- [eryone] **Eryone PA (Nylon)** - missing: density, drying, PA6 vs PA12 base. Why: no TDS; values come from the combined Nylon & CF/GF listing <https://eryone3d.com/products/nylon-filament>
- [eryone] **Eryone ABS-PC Alloy** - missing: single density value. Why: density is published only as a range (1.05-1.11), so it was not put in fields <https://eryone3d.com/products/abs-pc-alloy-material-filament>
- [eryone] **Eryone PP-CF** - missing: single density value. Why: density is published only as a range (0.95~1.01), so it was not put in fields <https://cdn.shopify.com/s/files/1/0252/0412/9841/files/ERYONE-PP_CF-TDS.pdf>
- [amolen] **AMOLEN PLA Basic Dual Color High Speed** - missing: density, drying, Tg/Vicat/HDT. Why: no specs published <https://www.amolen.com/products/pla-basic-dual>
- [amolen] **AMOLEN PLA Silk Quad Color** - missing: density. Why: no specs published <https://www.amolen.com/products/pla-silk-quad-color-1-75mm-1kg-2-2lb>
- [amolen] **AMOLEN PLA Silk Glow In The Dark** - missing: density. Why: no specs published <https://www.amolen.com/products/pla-silk-basic-glow-in-the-dark-1-75mm-1kg-2-2lb>
- [amolen] **AMOLEN PLA S-Series Glow-in-the-Dark** - missing: density. Why: no specs published <https://www.amolen.com/products/pla-s-series-glow-in-the-dark-1-75mm-1kg-2-2lb>
- [amolen] **AMOLEN PLA Temperature Color Change** - missing: density. Why: no specs published <https://www.amolen.com/products/pla-temperature>
- [amolen] **AMOLEN PLA Carbon Fiber** - missing: density. Why: no specs published <https://www.amolen.com/products/pla-carbon-fiber-pack>
- [amolen] **AMOLEN PETG Transparent Rainbow** - missing: density, drying, Tg/Vicat/HDT, colours. Why: no specs published <https://www.amolen.com/products/petg-transparent-rainbow>
- [amolen] **AMOLEN ABS** - missing: density, drying, HDT. Why: no specs published <https://www.amolen.com/products/abs-filament-1-75-mm-1kg>
- [amolen] **AMOLEN ABS Glow In The Dark** - missing: density, drying, HDT. Why: no specs published <https://www.amolen.com/products/abs-glow-in-the-dark-filament-1-75mm-1kg-2-2lb>
- [geeetech] **GEEETECH Carbon Fiber PLA** - missing: all. Why: not found (no official GEEETECH product page; only a generic wiki material section and 3djake reseller listings) <https://wiki.geeetech.com/index.php/Filament>
- [sovol] **SOVOL Rapid PETG** - missing: nozzle temp, bed temp, density, drying, volumetric speed. Why: Amazon feature bullets not served to fetch; no Sovol site page found <https://www.amazon.com/dp/B0H1H3MJFH>
- [sovol] **SOVOL PLA Basic** - missing: density, diameter tolerance, drying. Why: no published values beyond the sovol3d.com spec table (read directly) <https://www.sovol.tech/products/sovol-pla-basic-filament-1.75mm>
- [qidi-tech] **QIDI Tech PLA Matte Rapido** - missing: filament_density (only 1.40~1.45 published). Why: no single value published: TDS gives density only as a range <https://drive.google.com/file/d/1c1ovAy5v74V4XCC-CLGtm06ZBYTVO9QY/view>
- [qidi-tech] **QIDI Tech ASA-Aero** - missing: filament_density. Why: the only published density (1.03) is measured by ISO 845, the foamed-plastics method, so it is not a filament density <https://drive.google.com/file/d/15phWOoaQqLDTHUFiHklw-YodWG2iMFCh/view>
- [qidi-tech] **QIDI Tech PPS-CF** - missing: diameter, diameter tolerance (removed). Why: Only TDS page 1 has extractable text (nozzle/bed/fan/speed verified); remaining pages unreadable <https://drive.google.com/file/d/1DTDb7ew0Uv_E0KyMK8YkJJ4p9OL6M9Gt/view>
- [flashforge] **Flashforge ABS / ABS Pro** - missing: enclosure requirement. Why: the PDF was readable as text, but the 'Print with Enclosure' row has no text values (likely icons) and no PDF renderer was available <https://wiki.flashforge.com/resource/filament_tips/flashforge_filament_guide.pdf>
- [kexcelled] **Kexcelled K5 ABS Metal (older TDS 'ABS K5P')** - missing: all (not written). Why: only a 2022 reseller TDS copy found; could not confirm it is the current line <https://3dprinteq.dk/wp-content/uploads/KEXCELLED-ABS-K5P-Technical-Date-Sheet-EN-1-1.pdf>
- [kexcelled] **All 38 written Kexcelled lines** - missing: drying, colours, max volumetric speed, fibre content (CF/GF lines), hardened-nozzle requirement; most densities are ranges, so filament_density is unset except K5 ABS, K5 ABS Rapid, K3 ASA, K6 HIPS. Why: no specs published in the TDS
- [3dxtech] **3DXTech 3DXMAX PETG** - missing: colors, drying, diameter tolerance, current-revision check. Why: only an older TDS (Rev 2.1) on a third-party CDN could be read <https://cdn.shopify.com/s/files/1/0965/1648/files/PETG_Filament_v2.1.pdf>
- [3dxtech] **3DXTech CarbonX ezPC+CF** - missing: nozzle range, bed range, density, Tg, HDT. Why: only single values published (275C / bed 95C), no range <https://www.matterhackers.com/store/l/3dxtech-carbonx-black-ezpccf-filament/sk/MKWN4KHH>
- [3dxtech] **3DXTech CarbonX PEEK CF20** - missing: nozzle range, bed range, chamber, drying. Why: the TDS gives specimen conditions only <https://cdn.shopify.com/s/files/1/1339/4265/files/CF20_PEEK_v1.pdf>
- [3dxtech] **3DXTech CarbonX PEI 9085+CF** - missing: nozzle range, bed range, drying. Why: the TDS gives specimen conditions only <https://cdn.shopify.com/s/files/1/0658/0033/9668/files/CF_Ultem_9085.pdf>
- [3dxtech] **3DXTech 3DXSTAT ESD-PEI 9085** - missing: nozzle range, bed range, drying. Why: the TDS gives specimen conditions only <https://cdn.shopify.com/s/files/1/0658/0033/9668/files/ESD_Ultem9085_v1_tds.pdf>
- [protopasta] **Protopasta Composite Metal PETG (Iron / Copper / Steel)** - missing: all. Why: no specs published (only 'standard temperatures in the Generic PETG profile', avoid <2 mm3/s, density '~2x PETG') <https://proto-pasta.com/blogs/stories/endless-exploration-ex16-sept-2026-metal-petg>
- [protopasta] **Protopasta Glass Fiber HTPLA** - missing: nozzle range, density, bed temp. Why: no TDS, SDS or Material Data Table row; only one print temperature (240C at up to 24 mm3/s) <https://proto-pasta.com/products/white-glass-fiber-htpla>
- [protopasta] **Protopasta High Density Iron HTPLA** - missing: nozzle range, density, bed temp. Why: no TDS/SDS; only one print temperature (200C at up to 24 mm3/s) <https://proto-pasta.com/blogs/stories/endless-exploration-ex10-september-2025-high-density-metal-htpla>
- [protopasta] **Protopasta High Density Stainless Steel HTPLA** - missing: nozzle range, density, bed temp. Why: no TDS/SDS; only one print temperature (200C at up to 24 mm3/s) <https://proto-pasta.com/blogs/stories/endless-exploration-ex10-september-2025-high-density-metal-htpla>
- [protopasta] **Protopasta PCTG / High Strength CF PCTG / High Impact CF PCTG / Glass Fiber PCTG** - missing: density; max volumetric speed (CF/GF variants); exact bed range (only 70+/80+). Why: no TDS or SDS published for PCTG; values come from the product pages and blog <https://proto-pasta.com/pages/material-data-table>
- [protopasta] **Protopasta High Strength CF / High Impact CF / Glass Fiber HTPETG** - missing: nozzle low bound, density, drying temp/time. Why: no TDS or SDS published; only an upper nozzle temperature (300C) and bed 100+C <https://proto-pasta.com/blogs/stories/endless-exploration-ex14-may-2026-high-temp-petg>
- [protopasta] **Protopasta Flexible TPU** - missing: nozzle high bound, density, drying temp/time, max volumetric speed. Why: no TDS/SDS; only 'printing starting at 240 C' plus blog speed/temp points <https://proto-pasta.com/products/clear-flexible-tpu>
- [protopasta] **Protopasta Calcium Carbonate PLA** - missing: nozzle range, bed temp, max volumetric speed. Why: the Material Data Table row has no print temperatures; only the SDS density was published <https://proto-pasta.com/pages/material-data-table>
- [colorfabb] **ColorFabb LW-BVOH** - missing: all. Why: no specs published (page has marketing text only; no TDS in the download folder) <https://colorfabb.com/lw-bvoh>
- [colorfabb] **ColorFabb PVOH** - missing: all. Why: no products listed (category empty, probably discontinued) <https://colorfabb.com/filaments/materials/support-materials/pvoh>
- [colorfabb] **ColorFabb PETG Regrind** - missing: all. Why: no products listed (category empty, probably discontinued) <https://colorfabb.com/filaments/materials/co-polyester-filaments/petg-regrind>
- [colorfabb] **ColorFabb nGen** - missing: all (deliberately skipped). Why: not written: category lists only nGen-CF10 and nGen Clear has no product page, so it looks discontinued (TDS still in the download folder) <https://colorfabb.com/filaments/materials/co-polyester-filaments/ngen>
- [colorfabb] **ColorFabb PLA Color On Demand** - missing: all (deliberately skipped). Why: custom-colour order service rather than a product line; TDS exists but was not written <https://colorfabb.com/custom-colored-pla-filament>
- [colorfabb] **ColorFabb PLA-HP / PLA Vibers / nGen-CF10 / PET Flex Max / LW-PET / LW-PET Flex / LW-PET Flex Max / allPHA** - missing: density. Why: entries written; the official TDS gives no density (allPHA prints N/A)
- [colorfabb] **ColorFabb bronzeFill / copperFill / steelFill** - missing: density in fields. Why: entries written; TDS densities (3.9 / 4 / 3.13) are above the validator's 0.5-3.0 limit, so they were moved to _notes
- [colorfabb] **ColorFabb rPLA, corkFill, stoneFill, rPETG, PA-CF Low Warp, PLA Vertigo, PLA Chameleon** - missing: rPLA/corkFill/stoneFill/rPETG: density; rPETG: Tg, tolerance, speed; PA-CF Low Warp: drying, nozzle requirement. Why: entries written from the product page only; no TDS published
- [formfutura] **Formfutura MetalFil - Classic Copper** - missing: filament_density field (value recorded in _notes only). Why: published density 3.4 g/cc exceeds the library validator's 0.5-3.0 range <https://formfutura.com/web/content/256597?download=true>
- [formfutura] **Formfutura High Gloss PLA ColorMorph** - missing: drying, HDT/Tg, print speed (page values only). Why: the TDS linked on the page is the plain High Gloss PLA datasheet, not a ColorMorph one <https://formfutura.com/web/content/256568?download=true>
- [formfutura] **Formfutura EasyFil PLA - Glow in the Dark** - missing: drying, HDT/Tg, print speed range. Why: no TDS linked on the product page <https://formfutura.com/filaments/easyfil-pla-glow-in-the-dark>
- [formfutura] **Formfutura ABSpro** - missing: Formfutura-branded TDS (thermal values are from the Flashforge-branded sheet only). Why: the linked TDS is a Flashforge-branded 'ABS Pro' datasheet; fields use Formfutura page values instead <https://formfutura.com/web/content/254657?download=true>
- [formfutura] **Formfutura AquaSolve - PVA** - missing: Formfutura-branded TDS, drying. Why: the linked TDS is a Flashforge-branded PVA datasheet; fields use Formfutura page values instead <https://formfutura.com/web/content/256478?download=true>
- [formfutura] **Formfutura EasyFil ePETG / HDglass / CarbonFil CF03 / Kratos PC / ApolloX CF10 / STYX PA6 / STYX PA6-CF15 / AthenaX / Python Flex TPU 90A & 98A** - missing: drying temperature/time for most of these; print speed range. Why: TDS gives material properties only, with no print settings; print settings taken from product pages
- [amazon-basics] **Amazon Basics Silk PLA** - missing: nozzle temp, bed temp, density, drying. Why: listing gives no temperatures or density; no TDS found <https://www.amazon.com/dp/B08894NK7S>
- [amazon-basics] **Amazon Basics ABS** - missing: all. Why: not found; current availability unconfirmed
