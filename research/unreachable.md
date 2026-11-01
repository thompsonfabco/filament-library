# Gaps from the 2026-11-01 parallel fetch

Lines and values the automated fetch (web search + page fetch, no browser, no logins) could not source.
Hand this to a Research-mode chat with the handoff doc (filament-kit `docs/filament-research-handoff.md`);
its JSON replies go through `tools/import_batch.py`. Entries already in the library are refreshed by
re-importing the full entry (same vendor + product spelling).

- Unreachable / incomplete: 410 items across 34 batches
- Values removed by the source check (not printed in a cited source): 235
- Entries dropped by the source check: 13

## Unreachable or incomplete

### bambu-lab-pla (5)

- **Bambu Lab PLA Basic Gradient** - missing: all (no entry written; may share the PLA Basic entry). Why: no separate TDS found; retailer pages describe it as a PLA Basic series colour using the PLA Basic profile. Bambu store pages (us.store.bambulab.com) return HTTP 402 and eu/uk redirect there <https://stemfinity.com/products/bambu-lab-pla-basic-gradient>
- **Bambu Lab PLA Lite** - missing: official TDS confirmation of nozzle range 190-240, bed 35-65, drying 50C 8h, max volumetric speed 16; diameter not stated by any source; Tg, chamber temp, retraction. Why: no official TDS found and the official store is blocked (402). Entry written from a Bambu PLA Lite product sheet hosted by a reseller (bigdipper.com.ar), plus density from the official PLA Pure TDS comparison table <https://us.store.bambulab.com/products/pla-lite>
- **Bambu Lab PLA Pure** - missing: filament diameter. Why: TDS read fine but does not print a filament diameter <https://store.bblcdn.com/s7/default/ecb663b46ebb4fb984786d33befb8d2f/PLA_Pure_TDS.pdf>
- **Bambu Lab PLA Silk Multi-Color** - missing: confirmation of the current product name only. Why: its TDS file is the same V3.0 'PLA Silk' sheet, so it is folded into the PLA Silk entry rather than given its own entry; the current product page could not be read to confirm the naming (store 402) <https://cdn.shopify.com/s/files/1/0584/7236/6216/files/Bambu_PLA_Silk_Dual_Color_Technical_Data_Sheet.pdf>
- **Bambu Lab official store/filament pages (all lines)** - missing: product-page values (diameter tolerance, colour lists) for all lines. colors left empty except PLA Lite. Why: bambulab.com returned 403; us.store.bambulab.com returned 402; regional stores redirect to the US store <https://bambulab.com/en/filament>

### bambu-lab-other (6)

- **Bambu Lab PETG Matte** - missing: official-host TDS URL; cooling fan range (TDS says only 'Turn on'). Why: Bambu store returns HTTP 402 to fetch; no official-host TDS found. Entry written from the TDS V1.0 copy that 3DJake hosts (reseller_tds_copy) <https://us.store.bambulab.com/products/petg-matte>
- **Bambu Lab PETG Translucent** - missing: official-host TDS URL. Why: Bambu store returns HTTP 402; no official-host TDS found. Entry written from the TDS V1.0 copy that additive-x hosts (reseller_tds_copy) <https://us.store.bambulab.com/products/petg-translucent>
- **Bambu Lab PPA-CF** - missing: official-host TDS URL; cooling fan range (TDS says only 'Turn on'). Why: Bambu store blocked (402/redirect); entry written from the TDS V1.0 copy that additive-x hosts (reseller_tds_copy) <https://eu.store.bambulab.com/en-pl/products/ppa-cf>
- **Bambu Lab TPU for AMS** - missing: whether max print speed is <250 or <=250. Why: the comparison glyph before the printing speed (250 mm/s) would not extract from the PDF <https://cdn.shopify.com/s/files/1/0584/7236/6216/files/Bambu_TPU_for_AMS_Technical_Data_Sheet.pdf>
- **Bambu Lab PAHT-CF** - missing: check of the V3.0 values. Why: not attempted (time): entry uses TDS V2.0; a newer V3.0 seen in search results was not read <https://uwaterloo.ca/rapid-prototyping-centre/sites/default/files/uploads/documents/bambu_paht-cf_technical_data_sheet_v2.pdf>
- **Bambu Lab (all lines)** - missing: confirmation of the full current catalogue and colour lists (colors left empty in every entry); discontinued status of PA-CF, ASA-CF and TPU 95A. Why: blocked: Bambu store and wiki.bambulab.com return HTTP 402 to fetch; the catalogue list was built from TDS file names, Bambu Studio presets and search results, so a 2025-2026 non-PLA launch could be missing <https://us.store.bambulab.com/collections/filament>

### polymaker-a (10)

- **Polymaker PolyLite Metallic PLA Pro** - missing: all. Why: no specs published (the product page reuses the generic PLA Pro text and there is no line-specific TDS) <https://shop.polymaker.com/products/polylite-metallic-pla-pro>
- **Polymaker PolyLite Translucent PETG** - missing: all. Why: no specs published (generic PolyLite PETG page text, no line-specific TDS) <https://shop.polymaker.com/products/polylite-translucent-petg>
- **Polymaker PolyLite Galaxy ABS** - missing: all. Why: no specs published (generic PolyLite ABS page text, no line-specific TDS; a glitter fill may change density) <https://shop.polymaker.com/products/polylite-galaxy-abs>
- **Polymaker PolyLite Metallic ABS** - missing: all. Why: no specs published (generic PolyLite ABS page text, no line-specific TDS) <https://shop.polymaker.com/products/polylite-abs-metallic>
- **Polymaker PolyLite Neon ABS** - missing: all. Why: no specs published (generic PolyLite ABS page text, no line-specific TDS) <https://shop.polymaker.com/products/polylite-neon-abs>
- **Polymaker Galaxy ASA** - missing: all. Why: no specs published (generic ASA page text, no line-specific TDS) <https://shop.polymaker.com/products/polymaker-galaxy-asa>
- **Polymaker PolyTerra PLA** - missing: official source, drying, diameter, colours. Why: no official TDS or product page readable (product removed from Polymaker shop/TDS index; official page renders through JS); used a reseller-hosted copy of TDS V5.1 <https://polymaker.com/the_latest/polyterra-pla/>
- **Polymaker PolyTerra PLA+** - missing: official source, drying, diameter, colours. Why: only a reseller-hosted copy of TDS V5.1 found; no official page <https://cdn.shopify.com/s/files/1/0789/2979/files/PolyTerra_PLA_Plus_EN_V5.1.pdf>
- **Polymaker PolyLite PLA Pro** - missing: drying. Why: TDS does not publish a drying setting <https://cdn.shopify.com/s/files/1/0548/7299/7945/files/Polylite_PLA_Pro_TDS_EN_V5.4.pdf>
- **Polymaker PLA Pro / PETG / ASA / PolyLite PETG / PLA-CF / LW-PLA / CosPLA** - missing: filament_diameter. Why: the TDS and product pages give no filament diameter (product pages show no diameter option)

### polymaker-b (11)

- **Polymaker Wood PLA** - missing: nozzle temp, bed temp, drying, thermal (entry not written). Why: no specs published: no wiki page or TDS found; the shop page gives only density 0.8 g/cm3 and spool dimensions <https://shop.polymaker.com/products/polymaker-wood-pla>
- **Polymaker PC-PBT** - missing: all. Why: not attempted: appears discontinued (TDS only, not sold in the US shop, no product wiki page) <https://cdn.shopify.com/s/files/1/0548/7299/7945/files/Polymaker_PC_PBT_TDS_EN_V5.4.pdf>
- **Polymaker Fiberon PET-GF15** - missing: Tg, Vicat, HDT (entry written with print settings and density). Why: PDF text layer has the thermal table misaligned, so values could not be matched to rows <https://fiberon.polymaker.com/wp-content/uploads/TDS_FIBERON-PET-GF15_V1.0_EN.pdf>
- **Polymaker Fiberon ASA-CF08** - missing: Tg, HDT, chamber temperature value. Why: PDF text layer garbled for most thermal rows; only Vicat (110.8) was clear <https://fiberon.polymaker.com/wp-content/uploads/TDS_FIBERON-ASA-CF08_V1.0_EN.pdf>
- **Polymaker Fiberon PA612-CF15** - missing: Tg. Why: TDS publishes Tg as N/A <https://cdn.shopify.com/s/files/1/0548/7299/7945/files/TDS_FIBERON_PA612-CF15_V1.1_EN.pdf>
- **Polymaker Matte PLA for Production** - missing: HDT 0.45/1.8 MPa. Why: image-only TDS (read visually); the HDT curve legend does not show which load each value belongs to <https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/pla/matte-pla-for-production>
- **Polymaker PolyMax PLA** - missing: single density value (range kept in published_ranges). Why: TDS gives density only as a range (1.17-1.24) <https://cdn.shopify.com/s/files/1/0548/7299/7945/files/PolyMax_PLA_TDS_EN_V5.4.pdf>
- **Polymaker PolyFlex TPU95** - missing: single density value, max volumetric speed. Why: TDS gives density only as a range (1.20-1.24) <https://cdn.shopify.com/s/files/1/0548/7299/7945/files/PolyFlex_TPU95_TDS_EN_V5.4.pdf>
- **Polymaker PolySupport for PLA / PolySupport for PA12 / PolyDissolve S1 / PolyFlex TPU90/95/95-HF** - missing: Tg, Vicat, HDT (PolySupport for PA12 has Vicat and HDT); max volumetric speed for TPU lines. Why: TDS does not publish thermal properties for these lines
- **Polymaker Panchroma lines (all except CoPE)** - missing: per-line density (group values used, matched through the wiki's printing-profile grouping); Tg and HDT not published. Why: the Panchroma TDS gives density and Vicat only per group (Basic/CoPE/Matte/Satin/Silk/Others), not per line <https://cdn.shopify.com/s/files/1/0548/7299/7945/files/TDS_PANCHROMA_V2.pdf>
- **Polymaker HT-PLA Pro** - missing: none. Why: The wiki TDS page is image-only (TDS V1.2 JPG). It was checked against TDS V1.4, the PDF linked from the cited shop page, which is now added to sources. All values were found. <https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/pla/ht-pla-pro>

### esun (36)

- **eSUN (all lines) official site** - missing: official_page confirmation for all 47 written entries. Why: blocked/403 on www, eu. and au. esun3d.com; TDS PDFs read from spoolscout-hosted copies instead <https://www.esun3d.com/>
- **eSUN (all 47 written lines)** - missing: filament_diameter, diameter tolerance. Why: TDS does not state filament diameter/tolerance
- **eSUN PLA, PLA-Matte Dual, ASA+, ePAHT-CF** - missing: HDT. Why: HDT value not legible in PDF text extraction (two-column layout) <https://assets.spoolscout.com/tds-sds/esun/tds/esun-asa-plus-tds-v1.0-2024-06.pdf>
- **eSUN PETG-Basic** - missing: nozzle range low/high, drying duration. Why: nozzle printed as single value 250+/-5C, not a range <https://assets.spoolscout.com/tds-sds/esun/tds/esun-petg-basic-tds-v1.0-2024-07.pdf>
- **eSUN PETG-Matte** - missing: drying hours. Why: drying duration not legible in text extraction <https://assets.spoolscout.com/tds-sds/esun/tds/esun-petg-matte-tds-v1.0-2025-07.pdf>
- **eSUN PLA-Metal** - missing: density. Why: density printed as '<1.24' (not a point value) <https://assets.spoolscout.com/tds-sds/esun/tds/esun-pla-metal-tds-v1.0-2026-12.pdf>
- **eSUN older v4.0 TDS lines (PLA+HS, ePLA-HS, PLA, ST, CF, GF, LW, Lite, Luminous, Stars, Gloss, Silk Magic/Mystic, Twinkling, Marble, Chameleon, PETG+HS, ABS, ABS+, eABS+HS, eABS-CF/GF, ASA+, HIPS)** - missing: drying. Why: no drying recommendation published (N/A) in TDS
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
- **eSUN PEBA-LW** - missing: all. Why: no TDS link found <https://www.spoolscout.com/data-sheets/esun/peba-peba-lw>
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

### sunlu (7)

- **SUNLU ABS 2.0** - missing: all. Why: no specs published: the product page has no parameter table and no TDS link. A web search found only the standard ABS / High Speed ABS figures, none for ABS 2.0 <https://www.sunlu.com/products/ABS2.0>
- **SUNLU (all lines written)** - missing: drying hours, filament_max_volumetric_speed. Why: no specs published: SUNLU TDS sheets give the drying temperature but not the drying time, and none publish max volumetric speed
- **SUNLU PP** - missing: density. Why: no specs published (the TDS and the page both print density as '/') <https://media.sunlu.com/prod/20260413/fbfe6e74-b29f-4f0f-a9b3-84aaa6b2fc85.pdf?filename=TDS>
- **SUNLU PCL** - missing: nozzle fields, bed temp, retraction, drying, HDT. Why: no specs published; the published nozzle range 75-85C is below the validator's 150C floor, so it is kept only in published_ranges <https://media.sunlu.com/prod/20260414/9c709eea-12c7-4a05-b5cd-227c63c700b8.pdf?filename=TDS>
- **SUNLU PVA** - missing: drying. Why: no specs published (the TDS prints drying temperature as '/') <https://media.sunlu.com/prod/20260330/6f3c0e89-fa56-46b2-ab3d-601ee6b70cf9.pdf?filename=TDS>
- **SUNLU Silk TPU** - missing: HDT, Tg, Vicat. Why: no specs published <https://media.sunlu.com/prod/20260330/04545ebf-ef5c-4fd9-b425-42a06d39c7c0.pdf?filename=TDS>
- **SUNLU PLA Galaxy / PLA Rainbow / PLA Transparent Rainbow / Silk PLA+ Rainbow** - missing: full colour list. Why: not found: the page shows only the default colour name, with no colour table <https://www.sunlu.com/products/galaxy-pla-filament>

### elegoo (7)

- **ELEGOO PET-CF** - missing: diameter (page never states 1.75 mm), diameter tolerance. Why: no specs published <https://us.elegoo.com/products/pet-cf>
- **ELEGOO PLA Glow** - missing: diameter, diameter tolerance. Why: no specs published <https://us.elegoo.com/products/pla-glow>
- **ELEGOO PC-FR** - missing: diameter, diameter tolerance. Why: no specs published <https://us.elegoo.com/products/pc-fr>
- **ELEGOO PLA Wood** - missing: diameter, diameter tolerance. Why: no specs published <https://us.elegoo.com/products/pla-wood>
- **ELEGOO ASA-CF** - missing: diameter, diameter tolerance. Why: no specs published <https://us.elegoo.com/products/asa-cf>
- **ELEGOO Rapid TPU 95A / TPU 95A** - missing: Vicat and HDT (listed as N/A). Why: no specs published <https://us.elegoo.com/products/rapid-tpu-filament-1-75mm-colored-1kg>
- **ELEGOO (all lines)** - missing: official TDS PDFs (none linked from product pages); max volumetric speed; retraction/fan settings. Why: no specs published

### overture (7)

- **OVERTURE Turbo PLA** - missing: colors. Why: not in current overture3d.com catalogue JSON; product page not fetched (site rate-limited WebFetch with 429) <https://overture3d.com/products/turbo-pla>
- **OVERTURE Air PLA** - missing: colors, official product page. Why: no current official product page found; only TDS plus reseller listing
- **OVERTURE Easy Nylon** - missing: drying temp/time. Why: no specs published <https://overture3d.com/cdn/shop/files/OVERTURE_EASY_NYLON_TDS_EN_V5.1_b6ce0042-6686-42dd-a5ab-696d2cc734b8.pdf>
- **OVERTURE PLA / Silk PLA / Super PLA+ / Easy PLA / Rock PLA / Turbo PLA / Air PLA / Eco PLA / High Speed TPU 95A / ABS** - missing: drying temp/time, max volumetric speed. Why: no specs published in TDS or product page
- **OVERTURE Glow PLA / Shimmer PLA** - missing: line-specific density/temps if they differ from Easy PLA. Why: no line-specific TDS (Glow page links Easy PLA TDS, Shimmer page mis-links Easy Nylon TDS); folded into Easy PLA entry <https://overture3d.com/products/overture-glow-pla>
- **OVERTURE Carbon Fiber PLA** - missing: all (not written). Why: appears discontinued (not in catalogue, no current listings found); TDS v1.1 Jan 2024 exists but not written <https://cdn.shopify.com/s/files/1/0207/3624/5824/files/OVERTURE_CF_PLA_TDS_EN.pdf>
- **OVERTURE Eco PLA** - missing: diameter. Why: not found (redirects to the overture3d.com homepage) <https://overture3d.com/products/overture-eco-pla-filament-1-75mm-1>

### jayo (15)

- **JAYO (all lines)** - missing: density, drying, Tg/HDT for every line except PA6-CF/PA6-GF/PA12-CF HDT. Why: no specs published: JAYO publishes no density on any product page; the lab-report blog post describes TDS-style data but links no PDF/table (images only) <https://jayo3d.com/blogs/news/properties-parameters-of-jayo-filaments>
- **JAYO High Speed PLA** - missing: nozzle temp, bed temp, density. Why: official page has no temps; Amazon brand listing returned 500/truncated page via WebFetch <https://www.amazon.com/JAYO-High-Speed-PLA-Filament/dp/B0CKX12R7J>
- **JAYO High Speed PLA+** - missing: nozzle temp, bed temp, density. Why: no specs published in text (temps likely in images only) <https://store.jayo3d.com/products/jayo-high-speed-pla-1-1kg-3d-printing-filament-bundle>
- **JAYO High Speed PLA+ 2.0** - missing: all. Why: only appears as a variant option in a collection listing; no product page or specs; no entry written <https://store.jayo3d.com/products/jayo-basic-filament-collection-pla-pla-matte-high-speed-series>
- **JAYO High Speed Marble PLA** - missing: nozzle temp, bed temp, density. Why: no specs published (only speed and tolerance) <https://store.jayo3d.com/products/reusable-spool-jayo-high-speed-marble-pla-600mm-s-high-speed-3d-printer-non-toxic-filament-1-1kg-roll-reusable-spool>
- **JAYO PLA Galaxy** - missing: nozzle temp, bed temp, density, abrasiveness. Why: no specs published (only diameter/tolerance) <https://store.jayo3d.com/products/reusable-spooljayo-pla-galaxy-3d-printer-filament-1-75mm-glitter-sparkle-pla-colorful-twinkling-1-1kg-galaxy-green-black-purple-for-fdm-printer>
- **JAYO Dual-Color Matte PLA** - missing: nozzle temp, bed temp, density. Why: no specs published (only diameter/tolerance) <https://store.jayo3d.com/products/moq-4-jayo-dual-color-matte-pla-3d-printing-filament-1-75mm-1-1kg-spool-2-4-lbs-dimensional-accuracy-0-02mm>
- **JAYO PLA Rainbow / PLA Transparent Rainbow** - missing: nozzle temp, bed temp, density. Why: no specs published (only tolerance); may just be colourways of JAYO PLA (already in library); no entry written <https://store.jayo3d.com/products/reusable-spool-jayo-pla-rainbow-1-1kg-3d-filament>
- **JAYO PETG Glow** - missing: all. Why: listing sells PETG Glow but publishes only PLA Glow settings; no entry written <https://store.jayo3d.com/products/moq-4-rolls-jayo-pla-glow-in-the-dark-luminous-3d-printer-filament-1-75mm-1-1kg>
- **JAYO ASA** - missing: all (nozzle, bed, density, HDT, tolerance +/-0.02 vs +/-0.03). Why: official shared TPU/ASA listing has no ASA settings; Amazon brand listings too large/truncated for WebFetch (search snippet suggested 250-280C nozzle, 90-110C bed, ~96C heat resistance, unverified); no entry written <https://www.amazon.com/JAYO-Filament-Resistant-Functional-Dimensional/dp/B0GMVGBLXB>
- **JAYO Easy PA (E-PA) / PA Nylon PA6+66** - missing: all. Why: official Easy PA page has empty description; Amazon PA6+66 listing truncated via WebFetch (snippet suggested 250-280C nozzle, 30-50C bed, HDT ~121C, unverified); no entry written <https://us.amazon.com/JAYO-Filament-Resistant-Load-Bearing-Mechanical/dp/B0FXW6P6DN>
- **JAYO PLA Meta** - missing: density, diameter tolerance. Why: no specs published beyond temps/speed <https://store.jayo3d.com/products/reusable-spooljayo-1-1kg-pla-meta-3d-printer-filament>
- **JAYO High Speed Matte PLA** - missing: density, diameter tolerance. Why: no specs published <https://store.jayo3d.com/products/jayo-high-speed-matte-pla-1-1kg-reusable-spool-3d-printing-filament>
- **JAYO PA6-CF / PA6-GF / PA12-CF** - missing: density, drying, diameter tolerance, HDT load (0.45 vs 1.8 MPa). Why: no specs published <https://store.jayo3d.com/products/jayo-1kg-pa6-cf-nylon-carbon-fiber-3d-printer-filament-1-75mm-heat-resistant>
- **JAYO High Speed PLA** - missing: all (diameter, nozzle temp, bed temp, density). Why: no specs published in page text (the page tells users to match temperature to speed; values are probably only in images). The reusable-spool page is the same. The Amazon listing B0CKX12R7J was not attempted. <https://store.jayo3d.com/products/moq-5-rolls-jayo-high-speed-pla-1-1kg-3d-printing-filament-bundle>

### kingroon (16)

- **Kingroon PA6-CF / PA-CF Carbon Fiber Nylon** - missing: all. Why: kingroon.com page publishes no settings; the kingroon3d.com PA-CF page shows copied PLA template values (190-210 C), so it is unusable; Amazon listing too large for WebFetch to reach its bullets, and the curl route was refused as bot-check circumvention; search snippet (250-280 C, dry 80C 8-12h, HDT 153 C) not verified <https://www.amazon.com/dp/B0DQPDTD2Z>
- **Kingroon TPU 85A Rainbow** - missing: all. Why: sold only as variants on the TPU page; no specs published for 85A <https://kingroon.com/products/kingroon-tpu>
- **Kingroon HS-PETG (bulk listing)** - missing: all (PETG HS TDS entry written separately). Why: no specs published on the page; could not confirm it is the same product as the PETG HS TDS <https://kingroon.com/products/10kg-hs-petg-high-speed-printer-filament-1-75mm-for-us-only>
- **Kingroon PA Nylon Basic (current listing)** - missing: density, drying, HDT; confirmation that the older listing matches current product. Why: current page has no specs; entry 'PA Nylon' uses an older kingroon.com PA6 listing; Amazon B0H3JN8D78 unavailable <https://kingroon.com/products/kingroon-pa-nylon-basic-3d-printer-filament>
- **Kingroon TPU 95A** - missing: confirmation of hardness/TDS match; retraction speed (TDS value printed truncated). Why: Only TDS is labelled 'TPU 90A' in its text but filed under tpu_95a; Amazon listing bullets could not be read (page too large for WebFetch) <https://www.amazon.com/Kingroon-Filament-Flexible-Clog-Free-Accuracy/dp/B0FYMRQXDR>
- **Kingroon Refill PLA** - missing: density, drying, HDT. Why: page gives only nozzle/bed/tolerance <https://kingroon.com/products/10kg-pla-refill-filament-with-no-spool>
- **Kingroon PLA Silk Tri-Color / Single Color / Rainbow, PLA+, HS-PLA, PETG Basic, PLA Chameleon** - missing: official TDS; retraction, chamber, max speed for most. Why: no TDS published on wiki.kingroon.com (probed filename variants); entries are product-page sourced
- **Kingroon PLA Silk Tri-Color (Silk Multicolor PLA)** - missing: all (nozzle 210-230, density 1.32, diameter 1.75, bed 35-45 unverified) - entry dropped. Why: HTTP 429 Too Many Requests on every attempt over ~6 min (WebFetch); no TDS cited <https://kingroon.com/products/kingroon-silk-multicolor-pla ; https://kingroon3d.com/products/kingroon-pla-silk-tri-color-3d-printer-filament>
- **Kingroon PLA Silk Single Color** - missing: all (nozzle 195-230, density 1.21, diameter 1.75, bed 50-70, fan 100%) - entry dropped. Why: HTTP 429 Too Many Requests <https://kingroon.com/products/kingroon-silk-single-color-pla ; https://kingroon3d.com/products/kingroon-pla-silk-single-color-3d-printer-filament>
- **Kingroon PLA Silk Rainbow** - missing: all (nozzle 195-230, density 1.21, diameter 1.75, bed 50-70, fan 100%) - entry dropped. Why: HTTP 429 Too Many Requests <https://kingroon3d.com/products/kingroon3d-silk-rainbow-pla ; https://kingroon.com/products/kingroon-silk-rainbow-pla0123>
- **Kingroon PLA+** - missing: all (nozzle 210-235, density 1.20, diameter 1.75, bed 55-65) - entry dropped. Why: HTTP 429 Too Many Requests <https://kingroon.com/products/kingroon-pla-pluspla ; https://kingroon.com/products/kingroon-10kg-pla-plus-pla-filament-1-75mm ; https://kingroon3d.com/products/kingroon3d-pla-plus-pla-pro-pla-filament>
- **Kingroon HS-PLA** - missing: all (nozzle 190-220, density 1.20, diameter 1.75, bed 50-65) - entry dropped. Why: HTTP 429 Too Many Requests <https://kingroon.com/products/10kg-hs-pla-high-speed-printer-filament-mixed-color-1-75mm-us-in-stock>
- **Kingroon PLA Chameleon** - missing: all (nozzle 200-220, density 1.22, diameter 1.75, bed 50-70, fan 100%) - entry dropped. Why: HTTP 429 Too Many Requests <https://kingroon3d.com/products/kingroon-chameleon-pla-3d-printer-filament>
- **Kingroon PETG Basic** - missing: all (nozzle 230-250, density 1.26, diameter 1.75, bed 70-90, fan 100%) - entry dropped. Why: HTTP 429 Too Many Requests <https://kingroon.com/products/kingroon-petg-basic ; https://kingroon.com/products/10kg-petg-filament-1-75mm-3d-print-materials ; https://kingroon3d.com/products/10kg-1-75mm-petg-filament>
- **Kingroon PA Nylon** - missing: all (nozzle 250-280, diameter 1.75, bed 100-120) - entry dropped. Why: HTTP 429 Too Many Requests <https://kingroon.com/products/copy-of-2kg-pack-pa-nylon-3d-filament ; https://kingroon.com/products/kingroon-pa-nylon-basic-3d-printer-filament>
- **Kingroon PLA Basic / PLA Matte / PLA Silk Dual-Color / PLA Glow / PLA-CF / PLA Wood / PETG-CF / ABS / TPU 95A (kept entries, product-page sources only)** - missing: none of the fields/ranges (all confirmed in TDS PDFs); unverified page-derived notes and conflicts only: PLA Basic _nozzle_by_speed page part + AMS/X1 drying note; PLA Matte _diameter_tolerance +/-0.02 and page 50-600 mm/s claim; PLA-CF and PETG-CF _hardened_nozzle_required quotes; TPU 95A store hardness '95A'; all 'conflicts' strings for these lines. A note saying so was appended to each kept entry's _notes.. Why: HTTP 429 Too Many Requests <kingroon.com and kingroon3d.com product pages cited alongside each TDS>

### hatchbox (10)

- **Hatchbox (all lines) - official site** - missing: verbatim first-hand read of PETG/Rapid PETG/ABS/TPU/Shiny/Glow/CF/Performance/UV/Temp-change pages and the PLA/PETG/ABS material pages. Why: blocked/403 on all direct product/collection/page fetches, 429 rate limit after a few requests; only /collections/pla-1-75mm.atom was readable once. Other values came from search-engine extracts of hatchbox3d.com pages <https://www.hatchbox3d.com/collections/filaments>
- **Hatchbox (all lines) - TDS** - missing: density (except PLA), drying, Tg/HDT/Vicat, max volumetric speed, shrink for every line. Why: no specs published (no Hatchbox TDS found); only a PLA SDS exists
- **Hatchbox PLA Refill** - missing: bed temp, density, drying. Why: no specs published beyond print temperature <https://www.hatchbox3d.com/products/3d-rs-pla1kg-red>
- **Hatchbox Matte PLA / Silk PLA / Wood PLA / Shiny PLA / PLA Glow in the Dark / PLA Carbon Fiber / PLA Pro+ / PLA Max V2 / Performance PLA / PLA UV Color Changing / PLA Temperature Color Changing** - missing: bed temp, density, drying; CF and Glow lines: fibre content and hardened-nozzle requirement. Why: product pages only say 'No Heating Bed Required'; no line-specific data <https://www.hatchbox3d.com/pages/pla-material>
- **Hatchbox Rapid PETG** - missing: bed temp, density, drying, max volumetric speed. Why: no specs published beyond temp and speed <https://www.hatchbox3d.com/products/3d-rpd-petg1kg-wht>
- **Hatchbox TPU** - missing: bed temp, density, drying, retraction. Why: no specs published beyond temp and hardness <https://www.hatchbox3d.com/products/3d-tpu-1kg1-75-blk>
- **Hatchbox ABS Glow in the Dark** - missing: bed temp, density, drying, hardened-nozzle guidance. Why: blocked/403; no line-specific bed temp <https://www.hatchbox3d.com/products/3d-abs-1kg1-75-glow>
- **Hatchbox PETG / ABS (Amazon listing)** - missing: cross-check of Amazon listing values. Why: Amazon page hides product details for bots ('add to cart to see details'); 1.5 MB page, bullets not reachable <https://www.amazon.com/HATCHBOX-3D-Filament-Dimensional-Accuracy/dp/B00J0GMMP6>
- **Hatchbox PLA Metal** - missing: all. Why: not found on hatchbox3d.com (only in third-party OFD/SimplyPrint list); may be same as Shiny PLA or discontinued <https://simplyprint.io/filaments/hatchbox/pla-metal>
- **Hatchbox PLA Basic** - missing: all. Why: not found on hatchbox3d.com (only in third-party OFD/SimplyPrint list) <https://simplyprint.io/filaments/hatchbox/pla-basic>

### inland (15)

- **Inland (all lines) - microcenter.com product pages** - missing: density, drying, Tg/HDT, max volumetric speed for every line (none surfaced in any source). Why: blocked/403 for WebFetch on every microcenter.com URL (product, quickView, catalogue); values were taken from the search-engine index of these pages instead, so each one should be checked against the live page <https://www.microcenter.com/site/content/inland%20filament.aspx>
- **Inland Amazon listings (brand listing route)** - missing: cross-check of all lines. Why: HTTP 500 for most ASINs; pages that do load are about 1.2 MB, so specs only appear at a fixed offset. Only B09FW2HVJJ (Silk) was read <https://www.amazon.com/dp/B00YSZ1MFU>
- **Inland PLA High Speed Silk** - missing: all. Why: blocked/403; search index returned no specs <https://www.microcenter.com/product/668800/inland-175mm-pla-high-speed-silk-3d-printer-filament-10-kg-(22-lbs)-cardboard-spool-shadow>
- **Inland PLA Dual Color Silk** - missing: all. Why: blocked/403; search index returned no specs <https://www.microcenter.com/product/650245/inland-175mm-pla-dual-color-silk-3d-printer-filament-1kg-(22-lbs)-cardboard-spool-black-silver>
- **Inland Glitter PLA** - missing: all. Why: not found in official sources (only a third-party SimplyPrint DB)
- **Inland Galaxy PLA** - missing: all. Why: not found in official sources (only a third-party SimplyPrint DB)
- **Inland PLA+ Multi Color (CMYK set)** - missing: all (needs a direct read). Why: ambiguous: two search readings disagree (plate 45-60 vs 45; one reading also gives 40-100 mm/s and calls it high-speed); page blocked/403 <https://www.microcenter.com/product/683865/inland-175mm-pla-3d-printer-filament-multi-color-100-kg-(22-lbs)-per-cardboard-spool-cyan-magenta-yellow-white>
- **Inland ABS UV Luminous (glow)** - missing: all. Why: blocked/403; search index gave no temperatures <https://www.microcenter.com/product/664840/inland-175mm-abs-3d-printer-filament-1kg-(22-lbs)-spool-uv-luminous-white>
- **Inland Fiberon ASA-CF08 (Inland-listed)** - missing: confirmation of brand/product identity; density, drying. Why: not attempted separately: probably Polymaker Fiberon resold under the Inland name. Search index shows 260-280 / 90-100, HDT 103C @0.45MPa <https://www.microcenter.com/product/705077/inland-175-mm-fiberon-asa-cf08-carbon-fiber-3d-printer-filament-05-kg-(11-lbs)-spool-light-gray>
- **Inland (all 19 lines)** - missing: none of the kept values; all were confirmed in the indexed listing text. Why: blocked/403: microcenter.com returns HTTP 403 to WebFetch. I checked every value against Micro Center's own listing text as shown in the search-engine index (WebSearch limited to microcenter.com), not by reading the live page <https://www.microcenter.com/product/...>
- **Inland PLA+** - missing: all (values confirmed from 611532 Black and other PLA+ colour listings). Why: blocked/403 and not found in the search index <https://www.microcenter.com/product/611544/inland-175mm-pla-3d-printer-filament-10-kg-(22-lbs)-spool-white>
- **Inland PLA+** - missing: all (confirmed from 611532). Why: blocked/403; the index shows the title only, with no temperatures <https://www.microcenter.com/product/632388/inland-175mm-pla-pro-3d-printer-filament-10-kg-(22-lbs)-spool-black>
- **Inland PETG-CF** - missing: all (values confirmed from 687104 Black). Why: blocked/403 and not found in the search index <https://www.microcenter.com/product/687109/inland-175mm-petg-cf-3d-printer-filament-1-kg-(22-lbs)-spool-antique-brass>
- **Inland Silk PLA** - missing: nothing in fields; the 190-230 conflict is unverified. Why: not attempted (cited for the conflicts entry only) <https://www.amazon.com/dp/B09FW2HVJJ>
- **Inland TPU for MFS** - missing: none removed; the kept 210-230 / 25-60 matches the cited 701526 listing, and the alternative is recorded as a conflict. Why: search index text conflicts: one result gives 220-240 / bed 30-35 / Shore D 62 for this item, another gives 210-230 / 25-60 / 90A <https://www.microcenter.com/product/701526/inland-175mm-tpu-3d-printer-filament-10-kg-(22-lbs)-cardboard-spool-black>

### creality (20)

- **Creality Hyper PLA** - missing: density (resellers say 1.25), drying, HDT/Vicat. Why: store page specs are images or loaded by JavaScript; Amazon listing has no temperatures or density in its text <https://store.creality.com/products/hyper-series-pla-3d-printing-filament-1kg>
- **Creality Soleyin Ultra PLA** - missing: density, diameter tolerance, drying, HDT. Why: store page specs are images; only a Creality blog gives temperatures <https://store.creality.com/products/soleyin-ultra-pla-3d-printing-filament-1kg>
- **Creality Hyper PETG** - missing: all (nozzle, bed, density, drying, HDT); only 'up to 300 mm/s' and tensile 40-50 MPa are official. Why: no specs in the official page text; the TDS hosted on manuals.plus returned 403; resellers conflict (220-260 or 190-260 nozzle; bed 70-80, 60-80 or 45) <https://store.creality.com/products/hyper-series-petg-3d-printing-filament-1kg>
- **Creality Hyper ABS** - missing: all. Why: no specs in the official page text; only resellers (230-270 nozzle, 75-95 bed, HDT 76 vs 80 conflict) <https://store.creality.com/products/hyper-abs>
- **Creality Hyper PC** - missing: all. Why: no specs in the official page text (US/EU); no TDS found <https://store.creality.com/products/hyper-pc-filament-1-75mm-1kg>
- **Creality Hyper PLA CF** - missing: all. Why: no specs in the official page text (US/JP); resellers give 190-230 nozzle, 45 bed <https://store.creality.com/products/hyper-pla-cf>
- **Creality Hyper Rainbow PLA** - missing: all. Why: no specs in the official page text <https://store.creality.com/products/hyper-rainbow-pla-3d-printing-filament-1kg>
- **Creality Hyper PLA Luminous** - missing: all (including whether a hardened nozzle is needed). Why: no specs in the official page text <https://store.creality.com/products/hyper-luminous-pla-3d-printing-filament-1kg>
- **Creality Hyper PLA Stardust** - missing: all. Why: no specs in the official page text <https://store.creality.com/products/hyper-pla-rfid-stardust-3d-printing-filament-1kg>
- **Creality Hyper PLA Lightweight** - missing: nozzle range, bed, exact density, drying. Why: official page gives only 'density around 0.8 g/cm3' and foaming notes; a reseller (PB Tech) gives 210-270 nozzle <https://store.creality.com/products/hyper-lightweight-pla-3d-printing-filament-1kg>
- **Creality Soleyin Basic PETG** - missing: all. Why: no specs in the official page text; a Creality blog gives only 'up to 200 mm/s' <https://store.creality.com/products/soleyin-basic-petg-3d-printing-filament-1kg>
- **Creality Ender Fast PLA** - missing: all published ranges. Why: no specs in the official page text; only K2 Plus profile values (220C/50C, 23 mm3/s) <https://store.creality.com/products/ender-fast-1-75mm-pla-3d-printing-filament-pack-2kg>
- **Creality CR-PLA Fluo** - missing: all published ranges. Why: appears only in the K2 Plus profile table; no product page found <https://store.creality.com/blogs/all/creality-k2-plus-filament-parameters-settings>
- **Creality HP Ultra PLA** - missing: current status, density. Why: in the official parameter table (190-230, bed none-60) but not on the current store; not written as possibly discontinued <https://store.creality.com/uk/blogs/basics/creality-filaments-parameter-reference-table>
- **Creality HP-HIPS** - missing: current status, density. Why: in the official parameter table (220-260, bed 70-110) but not on the current store; not written as possibly discontinued <https://store.creality.com/uk/blogs/basics/creality-filaments-parameter-reference-table>
- **Creality CR-PA Carbon** - missing: current status, density, drying. Why: in the official parameter table (230-260, bed 80-90, env 60-80) but not on the current store; not written as likely discontinued <https://store.creality.com/uk/blogs/basics/creality-filaments-parameter-reference-table>
- **Creality CR-PLA / CR-PLA Matte / CR-TPU / CR-Wood / CR-PLA Carbon / Ender-PLA / Ender-PLA+ / HP-TPU / HP-ASA / CR-Silk (written)** - missing: density, drying, HDT/Vicat, diameter tolerance; TPU Shore hardness; HP-ASA density. Why: only Creality's parameter table is available; no TDS <https://store.creality.com/uk/blogs/basics/creality-filaments-parameter-reference-table>
- **Creality Hyper PLA** - missing: conflict detail only (seller name, bullet tolerance); no fields depend on it. Why: Page read only partly (truncated). The title confirms 'Dimensional Accuracy +/-0.02mm' but the seller and bullet text (+/-0.03) could not be read <https://www.amazon.com/dp/B0CLTY4MML>
- **Creality CR-PLA Carbon** - missing: none (covered by parameter table). Why: no specs published on product page <https://store.creality.com/products/cr-pla-carbon-3d-printing-filament-1kg>
- **Creality Ender-PLA** - missing: none (covered by parameter table). Why: no specs published on product page (pack/colours only) <https://store.creality.com/products/ender-pla-value-pack-2-spools-pack>

### anycubic (9)

- **Anycubic PLA Translucent** - missing: all. Why: blocked/429 on every Anycubic Shopify storefront (store/ca/uk/eu/au) after the first few fetches; guessed TDS filenames on cdn.shopify.com returned 404 <https://store.anycubic.com/products/pla-translucent>
- **Anycubic PETG Translucent** - missing: all (legacy page table shows the same text as PETG; no line-specific TDS read). Why: blocked/429 on storefronts; TDS filename not found by guess (404) <https://store.anycubic.com/products/petg-filament-translucent>
- **Anycubic PLA Special** - missing: all. Why: blocked/429; no TDS URL found <https://store.anycubic.com/products/pla-basic-special-color-filament>
- **Anycubic PLA Silk Dual/Tri-Color** - missing: all. Why: blocked/429; no TDS URL found <https://store.anycubic.com/products/silk-pla-dual-tri-color-filament>
- **Anycubic PET-CF** - missing: all. Why: blocked/429; ANYCUBIC_TDS_PET-CF_V3.0.pdf guesses 404 on all three Anycubic Shopify CDNs <https://store.anycubic.com/products/pet-cf>
- **Anycubic PC** - missing: all. Why: blocked/429 (retried after 1-3 min waits); TDS filename guesses 404 <https://store.anycubic.com/products/pc-filament>
- **Anycubic PVA** - missing: all. Why: blocked/429 on store and ca; TDS guesses 404 (search snippet only: 220-240C print, dry 75-85C 8-12h - not verified from page, not used) <https://store.anycubic.com/products/pva>
- **Anycubic TPU 68D** - missing: all. Why: blocked/429 on store and anycubic.au; TDS guesses 404 (search snippet only: density 1.26, HDT 0.45MPa 183C, speed 40-250 mm/s - not verified, not used) <https://store.anycubic.com/products/tpu-68d>
- **Anycubic (several written lines)** - missing: filament_diameter for ABS, TPU 95A, PLA Matte, PLA Metal, PLA Marble, PLA Silk, PLA-CF, PLA Galaxy, PA6-CF; colour lists for PLA Basic, ABS, ASA, TPU 95A, PLA Matte, PLA Glow, PLA Metal, PLA Marble, PLA-CF, PA6-CF. Why: TDS does not state filament diameter and the product page could not be re-read

### prusament (6)

- **Prusament PETG Tungsten 75%** - missing: filament_density in fields (the TDS gives 4 g/cm3; recorded in _notes). Why: sourced, but the library validator rejects filament_density above 3.0 g/cm3 <https://prusament.com/wp-content/uploads/2023/03/TDS_Prusament-PETG-Tungsten-75_EN-1.pdf>
- **Prusament (all 24 lines)** - missing: drying for most lines (only PETG V0, PC Space Grade, PA11, PEI 1010, TPU 95A and PVB give one); Tg and Vicat (only HDT is published, plus Vicat A for TPU); max volumetric speed (only PA11 gives one); retraction and shrink. Why: not published by Prusament
- **Prusament Woodfill** - missing: base material type (material set to 'Wood-filled biobased polymer blend'; bambu_parent Bambu PLA Wood is my nearest-match choice). Why: base polymer not published (the TDS says only 'Biobased Polymer Blend') <https://prusament.com/materials/prusament-woodfill/>
- **Prusament PLA** - missing: density, diameter, max print speed, HDT 0.45/1.80 MPa, diameter tolerance. Why: TDS is published only as a zip over 10 MB; WebFetch refused it (maxContentLength exceeded). No separate download made. <https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-prusament-prod/2024/05/7ca620c4-prusament-pla-plablend.zip>
- **Prusament PLA Blend** - missing: density, diameter, max print speed, HDT 0.45/1.80 MPa, diameter tolerance. Why: same zip over 10 MB, unreadable via WebFetch <https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-prusament-prod/2024/05/7ca620c4-prusament-pla-plablend.zip>
- **Prusament PETG Carbon Fiber** - missing: density, diameter, fan speed, max print speed, HDT 0.45/1.80 MPa. Why: TDS is published only as a zip over 10 MB; WebFetch refused it (maxContentLength exceeded) <https://prusament.com/wp-content/uploads/2023/02/TDS_Prusament-PETG-CF-Black.zip>

### siraya-tech (6)

- **Siraya Tech Flex TPU 95A Matte** - missing: nozzle temp, bed temp, density, drying, retraction, print speed. Why: no specs published (no TDS; product page gives only max flow 15 mm3/s, +/-0.03 tolerance) <https://siraya.tech/products/flex-tpu-95a-matte-filament>
- **Siraya Tech Flex TPU Air 95A** - missing: nozzle temp, bed temp, density, diameter, drying, retraction, print speed. Why: no specs published (no TDS; product page gives only max flow 12 mm3/s and 75A-95A hardness) <https://siraya.tech/products/flex-tpu-air-95a-filament>
- **Siraya Tech Rebound PEBA Air 95A** - missing: density (unfoamed filament). Why: no specs published for this value <https://siraya.tech/pages/siraya-tech-rebound-peba-air-70a-95a-tds>
- **Siraya Tech Rebound PEBA 95A** - missing: retraction length/speed. Why: no specs published for this value <https://siraya.tech/pages/siraya-tech-rebound-peba-95a-tds>
- **Siraya Tech Fibreheart ASA-GF** - missing: print speed, fan speed, diameter. Why: no specs published for these values <https://siraya.tech/pages/siraya-tech-fibreheart-asa-gf-tds>
- **Siraya Tech Flex TPU 85A / Flex TPU 95A / Flex TPU 64D / Fibreheart ABS-CF / ABS-CF Core / ABS-GF / PET-GF / PPA / PPA-CF Core** - missing: diameter tolerance (and diameter); ABS-GF also fibre content. Why: no specs published (TDS does not state these)

### push-plastic (13)

- **Push Plastic Matte ABS** - missing: nozzle temp, bed temp, density, drying, HDT. Why: no specs published (the product page only says it prints like normal ABS; no print-settings sheet or TDS) <https://www.pushplastic.com/products/matte-abs-filament-1-75mm-1kg>
- **Push Plastic HIPS** - missing: nozzle temp, bed temp, density, drying. Why: no specs published (the TDS has only mechanical data and HDT; no print-settings sheet) <https://cdn.shopify.com/s/files/1/0260/7421/files/Push_Plastic_HIPS_Technical_Data_sheet.pdf>
- **Push Plastic Nylon** - missing: density, HDT. Why: no specs published (no TDS for unfilled Nylon) <https://www.pushplastic.com/pages/learn>
- **Push Plastic TPU 100A** - missing: density, drying, HDT (only TPU 98A values exist). Why: the official TDS and print-settings sheet name TPU 98A, not 100A, so they were recorded as conflicts only <https://cdn.shopify.com/s/files/1/0260/7421/files/Technical_Data_Sheet_TPU98A_v1.0.pdf>
- **Push Plastic Carbon Fiber PC+PBT** - missing: HDT. Why: no specs published (the TDS has no thermal section) <https://cdn.shopify.com/s/files/1/0260/7421/files/CF_PC_PBT_TDS.pdf>
- **Push Plastic PEI 1010** - missing: density, HDT. Why: no specs published (no filament or resin density on the site; the SDS gives none) <https://cdn.shopify.com/s/files/1/0260/7421/files/Ultem_1010_MSDS.pdf>
- **Push Plastic TPU 100A** - missing: all: nozzle 230-250, bed 60-80, hardness 100A, 0.6mm nozzle advice. Why: blocked/429 Too Many Requests (retried after waiting 60s and again after 150s) <https://www.pushplastic.com/products/tpu-100a-filament-1-75mm-1kg>
- **Push Plastic Carbon Fiber ABS / CF PC+PBT / CF Nylon / CF PETG** - missing: fiber content ~10%. Why: blocked/429 (all pushplastic.com product pages) <https://www.pushplastic.com/products/carbon-fiber-abs-filament-1-75mm-500g>
- **Push Plastic Nylon** - missing: enclosure conflict note. Why: blocked/429 <https://www.pushplastic.com/products/nylon-filament-1-75mm-1kg>
- **Push Plastic High Heat+Tough PLA** - missing: annealing conflict note. Why: blocked/429 <https://www.pushplastic.com/products/high-heat-tough-pla-filament-1-75mm-1kg>
- **Push Plastic PEI 9085** - missing: Tg ~185, product-page print-settings conflict. Why: blocked/429 <https://www.pushplastic.com/products/pei-9085-filament-1-75mm-500g>
- **Push Plastic PEI 1010** - missing: Tg ~215, product-page print-settings conflict. Why: blocked/429 <https://www.pushplastic.com/products/pei-1010-filament-1-75mm-500g>
- **Push Plastic (all 14 kept lines)** - missing: filament_diameter page confirmation, colour lists, 2.85mm availability. Why: blocked/429; filament_diameter 1.75 is supported only by the '1-75mm' slug in each cited product URL, not by reading the page <https://www.pushplastic.com/products/>

### atomic-filament (9)

- **Atomic Filament Flame Retardant ABS FR15U** - missing: density, HDT/Tg, drying. Why: blocked/406 (SABIC resin TDS linked from the product page). Only third-party resin listings found (not used) <https://www.sabic.com/en/products/documents/cycolac-resin_fr15u_americas_technical_data_sheet/en>
- **Atomic Filament Carbon Fiber PLA** - missing: density, bed temp, Tg, drying. Why: no specs published (no CF TDS; the PLA SDS does not cover fibre fill)
- **Atomic Filament Carbon Fiber PETG** - missing: density, Tg. Why: no specs published (no CF TDS)
- **Atomic Filament Carbon Fiber PCTG PRO** - missing: density, Tg, drying, minimum nozzle size. Why: no specs published (no CF TDS)
- **Atomic Filament Carbon Fiber ABS** - missing: density, Tg, minimum nozzle size. Why: no specs published (no CF TDS)
- **Atomic Filament Carbon Fiber ASA** - missing: density. Why: no specs published (only the generic ASA SDS, specific gravity '1.07~', not CF-specific)
- **Atomic Filament PCTG PRO** - missing: drying. Why: no specs published (FAQ drying table covers PETG, not PCTG) <https://atomicfilament.com/pages/atomic-filament-faq>
- **Atomic Filament PLA / Silk PLA / Extreme Impact PLA / Hi-Flow Pro PLA / MeltMiser PLA** - missing: drying; bed temp for Impact/Hi-Flow/MeltMiser; max volumetric speed for Hi-Flow Pro. Why: no specs published (no PLA TDS; density and Tg come from the generic PLA SDS; bed temp printed only on 2 PLA pages and on Silk pages)
- **Atomic Filament Flame Retardant ABS FR15U** - missing: density, HDT. Why: HTTP 406 according to the researcher's note. Not a cited source and not retried. <SABIC CYCOLAC FR15U resin TDS (linked from https://atomicfilament.com/products/flame-retardant-black-abs-filament)>

### fiberlogy (5)

- **Fiberlogy rABS** - missing: all (nozzle temp, bed temp, density, drying, fan, HDT/Vicat). Why: Product page has no spec table. The TDS PDF text is compressed or image-only and could not be read. The alternate page (fiberlogy.com/?p=14646) also has no specs. A search summary quoted 220-250C, 100C bed and 1.05 density for an 'S2' page, but no fetched page confirmed those values, so they were not used. <https://fiberlogy.com/en/filaments/abs-en/rabs-en/ ; TDS https://fiberlogy.com/app/uploads/2026/05/FIBERLOGY_RABS_TDS.pdf>
- **Fiberlogy ASA+AF** - missing: all (nozzle temp, bed temp, density, drying, fan, aramid fiber %). Why: Product page has no spec table: it gives only 'heat resistant up to 94C', a closed chamber and a hardened nozzle. The TDS PDF could not be read (image-only/compressed). The old TDS URL from search (fiberlogy.com/en_US/p/file/.../FIBERLOGY_ASA-AF_TDS.pdf) returned 404. <https://fiberlogy.com/en/filaments/asa-en/asaaf-en/ ; TDS https://fiberlogy.com/app/uploads/2026/07/FIBERLOGY_ASAAF_TDS.pdf>
- **Fiberlogy (all 49 written lines)** - missing: diameter tolerance/ovality (not on product pages); filament_max_volumetric_speed (not published); Tg missing for ABS, ASA, PA, PCTG, CPE, PP-family lines; fan/airflow missing for FiberSatin, FiberSilk, rPLA, FiberWORKS PLA, PVB, BVOH and TPU lines (page shows an ambiguous '75-100%' or '50-75%' figure labelled 'humidity'). Why: Official TDS PDFs are image-based or compressed and not text-extractable, so every entry is sourced from the official product page only <https://fiberlogy.com/app/uploads/2026/05/FIBERLOGY_EASYPLA_TDS.pdf (representative)>
- **Fiberlogy (TDS PDFs for Easy PLA, HS PLA Clear, PLA Matte, PLA Mineral, rPLA, Easy PETG, PETG FR V0, rPETG, rPP, Nylon PA12, PA12+CF, PA12+GF, rNylon, ABS, ABS Plus, Easy ABS, PC/ABS, ASA, ASA Matte, CPE HT, FiberFlex 30D/40D/+CF, MattFlex 40D, HIPS, PCTG, PCTG+CF, PCTG+GF, PEI 9085)** - missing: none from cited sources; the TDS values (diameter, tolerance, TDS temps) could not be cross-checked. Why: image-only PDF or no text layer (pdftotext pulled no spec lines). These TDSs are not cited in the batch; I opened them only to cross-check the pages. <https://fiberlogy.com/app/uploads/2026/05/FIBERLOGY_*_TDS.pdf (linked from each product page)>
- **Fiberlogy rASA** - missing: filament_diameter (not published on the page). Why: the page links no TDS PDF; the page itself was readable <https://fiberlogy.com/en/filaments/asa-en/rasa-en/>

### fillamentum (5)

- **Fillamentum Flexfill TPE 90A** - missing: official TDS, print speed, fan, Tg/Vicat/HDT. Why: no TDS linked on the product page; values taken from the product page only <https://shop.fillamentum.com/products/flexfill-tpe-90a-traffic-black>
- **Fillamentum PETG HFFR** - missing: print speed, fan, colours. Why: page and TDS give no print speed, fan or colour list <https://shop.fillamentum.com/products/petg-hffr>
- **Fillamentum PETG** - missing: Tg. Why: TDS lists Tg and melting temperature as '-' <https://fillamentum.com/wp-content/uploads/2023/02/TDS_PETG_EN_30012023.pdf>
- **Fillamentum OrCA (0rCA)** - missing: print speed, fan. Why: the page and guide publish no print speed or fan values <https://shop.fillamentum.com/products/orca>
- **Fillamentum ABS Extrafill / HIPS Extrafill / ASA Extrafill** - missing: Tg; HDT at 0.45 MPa for ABS. Why: the TDSs give HDT at 1.8 MPa only (ABS) and no Tg

### extrudr (9)

- **Extrudr PETG Glow in the Dark** - missing: all. Why: not in the official Extrudr product catalogue; only reseller listings found, which give conflicting temperatures <https://www.3djake.com/extrudr/mf-petg-glow-in-the-dark>
- **Extrudr DuraPro ASA Matte** - missing: all. Why: not found as a separate line in the official catalogue (DuraPro ASA is described as matte); only a third-party listing <https://simplyprint.io/filaments/extrudr/durapro-matte-asa>
- **Extrudr BioFusion Silk** - missing: all. Why: only a third-party listing; not in the official catalogue <https://simplyprint.io/filaments/extrudr>
- **Extrudr GreenTEC Matte** - missing: all. Why: only a third-party listing; not in the official catalogue (GreenTEC itself is described as matte) <https://simplyprint.io/filaments/extrudr>
- **Extrudr (all 26 written lines)** - missing: filament_diameter, drying. Why: the catalogue doesn't state diameter; drying is only in the overview table, whose columns are misaligned, so it wasn't trusted <https://s3.extrudr.com/extrudr-media/product-catalogue/extrudr-Produktkatalog_EN.pdf>
- **Extrudr DuraPro PC/PBT CF** - missing: density, HDT. Why: this product's properties table repeats the DuraPro PA12 table, so it isn't reliable <https://s3.extrudr.com/extrudr-media/product-catalogue/extrudr-Produktkatalog_EN.pdf>
- **Extrudr TPU Flex Hard CF** - missing: max volumetric speed. Why: max volumetric speed isn't printed for this product <https://s3.extrudr.com/extrudr-media/product-catalogue/extrudr-Produktkatalog_EN.pdf>
- **Extrudr Flax / Pearl / Wood** - missing: max volumetric speed. Why: not published <https://s3.extrudr.com/extrudr-media/product-catalogue/extrudr-Produktkatalog_EN.pdf>
- **Extrudr Pearl** - missing: nozzle_temperature_range_low (field only). Why: the published low bound of 140 C is below the validator's 150 C floor, so that field was removed; the full range is kept in published_ranges._nozzle_published <https://s3.extrudr.com/extrudr-media/product-catalogue/extrudr-Produktkatalog_EN.pdf>

### spectrum (5)

- **Spectrum AquaPrint** - missing: material, filament density (TDS prints nozzle 190-215, bed 25-70, fan 0-50%, speed 20-50 mm/s, Tg 60-65). Why: TDS read, but the base polymer is not published (it says only 'water-soluble support', compared against PVA) and it gives bulk density (0.6-0.9), not filament density; no entry written so the material is not guessed <https://spectrumfilaments.com/wp-content/uploads/2024/02/en_tds_spectrum_aquaprint.pdf>
- **Spectrum Prografen PLA Graphene Light / Graphene Strong, Prografen PET-G Graphene Light / Graphene Strong** - missing: density, diameter, Tg/HDT/Vicat, drying. Why: no TDS linked on the official product pages; entries written from product page only <https://spectrumfilaments.com/en/filament/prografen-pla-graphene-light/>
- **Spectrum (all lines except PLA Premium)** - missing: filament_diameter, diameter tolerance. Why: main site and TDS PDFs do not state diameter; only the PLA Premium shop listing was checked (1.75 mm). Scraping the shop search for the rest timed out <https://shop.spectrumfilaments.com/>
- **Spectrum PCTG Premium, PCTG GF10, ASA-X CF10, PA6 Low Warp GF30, ASA Electrically Conductive, PET-G Glitter/Premium (HDT rows)** - missing: HDT. Why: HDT values sit on split lines in the TDS text extraction and could not be read reliably; left out
- **Spectrum PLA Premium** - missing: filament_diameter 1.75 (removed); the shop listing's repeat of 185-215 / bed 0-45 / 1.24 g/cm3 was not checked, but the TDS confirms these values. Why: connection refused (ECONNREFUSED 5.149.162.4:443) <https://shop.spectrumfilaments.com/product-eng-502-Filament-Spectrum-PLA-Premium-1-75mm-DEEP-BLACK-1kg.html>

### eryone (17)

- **Eryone PETG High-Speed Translucent** - missing: all. Why: no specs published as text: the product page shows image-only content and there is no TDS on the files page. Only reseller listings give values, which aren't an allowed source <https://eryone3d.com/products/petg-high-speed-translucent-filament>
- **Eryone PPS CF10** - missing: all. Why: no specs published as text: the product page is image-only and there is no TDS. Only a reseller listing (3dstisk.com) has values (310-350C, bed 80-90C) <https://eryone3d.com/products/pps-cf10-filament-1-75mm-0-03mm-0-5kg>
- **Eryone PA6-GF** - missing: density, line-specific nozzle/bed, drying, HDT. Why: no line-specific TDS. Only the combined Nylon & Nylon-CF/GF listing has values (250-280C, bed 100-120C), which may not apply to the GF grade <https://eryone3d.com/products/nylon-filament>
- **Eryone PA12-GF** - missing: density, line-specific nozzle/bed, drying, HDT. Why: no line-specific TDS; only the combined Nylon listing <https://eryone3d.com/products/nylon-filament>
- **Eryone PLA High-Speed** - missing: density, drying, Vicat/HDT. Why: the TDS linked as 'PLA High-Speed' is actually the Hyper-Speed PLA+ sheet. The entry was written from the product page <https://cdn.shopify.com/s/files/1/0252/0412/9841/files/ERYONE-PLA_HP-TDS.pdf>
- **Eryone PLA Silk** - missing: density, drying. Why: no TDS for single-colour silk; entry is from the product page only <https://eryone3d.com/products/silk-pla>
- **Eryone PLA Ultra Silk** - missing: density, drying. Why: no TDS; entry is from the product page only <https://eryone3d.com/products/advanced-silk-pla>
- **Eryone PLA Metallic** - missing: density, drying. Why: no TDS; entry is from the product page only <https://eryone3d.com/products/pla-metallic-filament>
- **Eryone PLA Light-Weight** - missing: density, drying. Why: no TDS; entry is from the product page only <https://eryone3d.com/products/pla-light-weight-filament>
- **Eryone PLA Lite Matte** - missing: density, drying, print speed. Why: no TDS; the product page gives only 'typical settings' <https://eryone3d.com/products/pla-lite-matte-filament-1-75mm-0-03mm-1kg>
- **Eryone PLA Rainbow** - missing: bed temp, density, drying. Why: no TDS. The pages give only the nozzle range, and the Lagoon page swaps its bed and speed labels <https://eryone3d.com/products/pla-classical-rainbow>
- **Eryone PETG Matte** - missing: density, drying, print speed. Why: no TDS; the product page gives only 'print settings' <https://eryone3d.com/products/petg-matte-filament-1-75mm-0-03mm-1kg>
- **Eryone PETG Lite** - missing: density, drying. Why: no TDS; the product page gives only 'typical settings' <https://eryone3d.com/products/petg-lite-filament-1-75mm-0-03mm-1kg>
- **Eryone TPU (95A), TPU 85A, TPU 90A, TPU Rainbow** - missing: density, drying (TPU Rainbow also missing hardness). Why: no TDS (only High-Speed TPU has one); entries are from the product pages <https://eryone3d.com/products/tpu>
- **Eryone PA (Nylon)** - missing: density, drying, PA6 vs PA12 base. Why: no TDS; values come from the combined Nylon & CF/GF listing <https://eryone3d.com/products/nylon-filament>
- **Eryone ABS-PC Alloy** - missing: single density value. Why: density is published only as a range (1.05-1.11), so it was not put in fields <https://eryone3d.com/products/abs-pc-alloy-material-filament>
- **Eryone PP-CF** - missing: single density value. Why: density is published only as a range (0.95~1.01), so it was not put in fields <https://cdn.shopify.com/s/files/1/0252/0412/9841/files/ERYONE-PP_CF-TDS.pdf>

### amolen (9)

- **AMOLEN PLA Basic Dual Color High Speed** - missing: density, drying, Tg/Vicat/HDT. Why: no specs published <https://www.amolen.com/products/pla-basic-dual>
- **AMOLEN PLA Silk Quad Color** - missing: density. Why: no specs published <https://www.amolen.com/products/pla-silk-quad-color-1-75mm-1kg-2-2lb>
- **AMOLEN PLA Silk Glow In The Dark** - missing: density. Why: no specs published <https://www.amolen.com/products/pla-silk-basic-glow-in-the-dark-1-75mm-1kg-2-2lb>
- **AMOLEN PLA S-Series Glow-in-the-Dark** - missing: density. Why: no specs published <https://www.amolen.com/products/pla-s-series-glow-in-the-dark-1-75mm-1kg-2-2lb>
- **AMOLEN PLA Temperature Color Change** - missing: density. Why: no specs published <https://www.amolen.com/products/pla-temperature>
- **AMOLEN PLA Carbon Fiber** - missing: density. Why: no specs published <https://www.amolen.com/products/pla-carbon-fiber-pack>
- **AMOLEN PETG Transparent Rainbow** - missing: density, drying, Tg/Vicat/HDT, colours. Why: no specs published <https://www.amolen.com/products/petg-transparent-rainbow>
- **AMOLEN ABS** - missing: density, drying, HDT. Why: no specs published <https://www.amolen.com/products/abs-filament-1-75-mm-1kg>
- **AMOLEN ABS Glow In The Dark** - missing: density, drying, HDT. Why: no specs published <https://www.amolen.com/products/abs-glow-in-the-dark-filament-1-75mm-1kg-2-2lb>

### geeetech (6)

- **GEEETECH HS-PLA** - missing: all (nozzle, bed, speed, density, tolerance, max volumetric speed). Why: No specs on the official store pages (Black and White pages have only qualitative text; the temperature chart is an image). geeetech.com returned 429 every time, Amazon returned 503. Only reseller values exist: 3djake 210-230C, AliExpress bundle 185-220C. <https://support.geeetech.com/hspla-black-3d-printer-filament-175mm-1kgroll-p-1395.html>
- **GEEETECH Sparkly PLA** - missing: all. Why: Not found on support.geeetech.com. geeetech.com returned 429. Only reseller values (3djake: 180-210C nozzle, 50-67C bed), which are not an allowed source. <https://www.3djake.com/geeetech/pla-sparkly>
- **GEEETECH Carbon Fiber PLA** - missing: diameter tolerance, density, drying, hardened-nozzle statement, official colour list. Why: No official product page was reachable (geeetech.com 429). The entry was written from the GEEETECH wiki only. <https://www.geeetech.com/collections/all>
- **GEEETECH Matte PLA / PLA+ / PETG / PETG Metal / ABS+ / ASA / Luminous PLA / Marble PLA** - missing: density (all lines); bed temp (PLA+); drying (all except PETG Metal); AMS statements; Tg/HDT (except PETG HDT 80C from a staff reply). Why: The current geeetech.com Shopify store was rate-limited (HTTP 429) on every attempt. Entries come from the official legacy store support.geeetech.com and the GEEETECH wiki, so the newer pages may hold updated values. <https://www.geeetech.com/products/pla-matte-3d-printer-filament-1-75mm-1kg-roll>
- **GEEETECH Silk Dual / Tri-Color PLA** - missing: all, if it is a separate line. Why: Not attempted (treated as colourways of the existing Silk PLA line). Not checked whether the temps differ. <https://support.geeetech.com/filament-silksilk-dual-tricolor-c-83_113.html>
- **GEEETECH Carbon Fiber PLA** - missing: all. Why: not found (no official GEEETECH product page; only a generic wiki material section and 3djake reseller listings) <https://wiki.geeetech.com/index.php/Filament>

### sovol (7)

- **SOVOL PLA Matte Multi-Colors Rainbow** - missing: all. Why: official page specs are image-only; no sovol3d.com product page found; only reseller (robu.in) listings, which conflict (190-210C vs 200-220C) and are not TDS copies; web search budget exhausted <https://www.sovol.tech/products/sovol-matte-pla-filament>
- **SOVOL PLA Glow in Dark** - missing: live-page verification of nozzle 200-240 / bed 50-60; density, tolerance, drying, speed. Why: HTTP 429 on every direct fetch; values taken from search-engine extraction, not verified on the live page <https://www.sovol3d.com/products/sovol-glow-in-dark-pla-filament-1-kg>
- **SOVOL PETG** - missing: live-page verification of nozzle 230-250 / bed 60-80 / speed 50-250; density, drying. Why: HTTP 429 on every direct fetch (also /it/ regional path); values from search-engine extraction, not verified on the live page <https://www.sovol3d.com/products/sovol-petg-3d-filaments-gradient-blue>
- **SOVOL TPU** - missing: verified nozzle range, bed temp, density, drying. Why: Amazon page did not serve feature bullets to fetch; nozzle 220 / bed 50-70 / speed 60 come from a search snippet of the listing; sovol.tech specs image-only <https://www.amazon.com/dp/B0FCS8G941>
- **SOVOL Rapid PETG** - missing: nozzle temp, bed temp, density, drying, volumetric speed. Why: Amazon feature bullets not served to fetch; no Sovol site page found <https://www.amazon.com/dp/B0H1H3MJFH>
- **SOVOL PLA Basic** - missing: density, diameter tolerance, drying. Why: no published values beyond the sovol3d.com spec table (read directly) <https://www.sovol.tech/products/sovol-pla-basic-filament-1.75mm>
- **SOVOL PLA Glow in Dark** - missing: hardened nozzle advice. Why: HTTP 429 <https://www.sovol3d.com/blogs/news/brightest-glow-in-the-dark-filament-tips-sovol-3d-printing>

### qidi-tech (9)

- **QIDI Tech PLA Rapido Metal** - missing: filament_density (only 1.19~1.21 published); no TDS cross-check. Why: image-only PDF (TDS could not be rendered, so the product page was used); density published only as a range <https://drive.google.com/file/d/1dvDjY47IRF-VjIIZqXzXGXfF202Bb4D6/view>
- **QIDI Tech PLA Wood** - missing: filament_density (only 1.22-1.24 published); no TDS cross-check. Why: image-only PDF (TDS could not be rendered, so the product page was used); density published only as a range <https://drive.google.com/file/d/1sLVAUb8BQcEXDONqKQEgaDZnhxQ9F12i/view>
- **QIDI Tech ABS Rapido Metal** - missing: filament_density (only 1.05~1.07 published); no TDS cross-check. Why: image-only PDF (TDS could not be rendered, so the product page was used); density published only as a range <https://drive.google.com/file/d/1o2Y5m-boyDLUKGqOvw_AtCM5114j38Cc/view>
- **QIDI Tech PLA Silk** - missing: no TDS cross-check (entry fully sourced from the product page). Why: image-only PDF (TDS could not be rendered, so the product page was used) <https://drive.google.com/file/d/1Gh5LNF426P8wKZD8cuM95APcqxCYPtQI/view>
- **QIDI Tech PLA Matte Rapido** - missing: filament_density (only 1.40~1.45 published). Why: no single value published: TDS gives density only as a range <https://drive.google.com/file/d/1c1ovAy5v74V4XCC-CLGtm06ZBYTVO9QY/view>
- **QIDI Tech ASA-Aero** - missing: filament_density. Why: the only published density (1.03) is measured by ISO 845, the foamed-plastics method, so it is not a filament density <https://drive.google.com/file/d/15phWOoaQqLDTHUFiHklw-YodWG2iMFCh/view>
- **QIDI Tech PLA Rapido** - missing: density range 1.21~1.23, diameter tolerance, melt temp (removed); other values verified on product page/guide. Why: TDS PDF downloaded but text is outlined vector glyphs (no extractable text, no embedded page images); no PDF renderer available <https://drive.google.com/file/d/1r7PaFrEUKRzsYeIlFKNTs_phSinYLV_q/view>
- **QIDI Tech ABS Rapido** - missing: density, bed 80-100, Vicat, fan 0-50%, diameter tolerance, melt temp (removed). Why: TDS PDF text is outlined/unreadable; product page has no spec table <https://drive.google.com/file/d/1slDSMF4i03Isx5fBOJmIuCyQSAyoDIjA/view>
- **QIDI Tech PPS-CF** - missing: diameter, diameter tolerance (removed). Why: Only TDS page 1 has extractable text (nozzle/bed/fan/speed verified); remaining pages unreadable <https://drive.google.com/file/d/1DTDb7ew0Uv_E0KyMK8YkJJ4p9OL6M9Gt/view>

### flashforge (9)

- **Flashforge HS PLA Multicolor** - missing: all. Why: blocked/429 (Shopify rate limit on every flashforge.com regional storefront); no TDS found <https://eu.flashforge.com/products/hs-pla-multicolor>
- **Flashforge HS PETG** - missing: all (the PETG entry uses the 2021 PETG TDS; unclear whether HS PETG is a separate formulation). Why: blocked/429 on product page; TDS guesses HS_PETG/HS-PETG returned 404 <https://eu.flashforge.com/products/petg>
- **Flashforge PETG Pro** - missing: all except guide-level nozzle/bed/speed. Why: blocked/429; TDS guesses PETG_Pro/PETGPro returned 404. Only figures available are from the Filament Guide (220-240C nozzle, 70-80C bed, 40-60 mm/s), and that alone was judged too thin for an entry <https://flashforge.com/fr/products/petg-pro>
- **Flashforge HS PLA** - missing: drying, diameter, diameter tolerance, product-page nozzle range (search summary said 190-240C, unverified). Why: product page specs not in fetched text / 429; the TDS's recommended-conditions table is empty <https://eu.flashforge.com/products/hs-pla>
- **Flashforge PLA, PLA Pro, PLA Matte, PLA Silk, PLA-CF, PETG, PETG-CF, ABS, ABS Pro, TPU 95A, PC, PVA (entries written)** - missing: filament_diameter and diameter tolerance (not in TDSs), single-value density (TDSs give only ranges), colours, drying for the PLA lines and PVA, confirmation that PC/PVA are still sold. Why: blocked/429 on all storefront pages (flashforge.com, eu., uk., au., ca., enterprise.) <https://flashforge.com/collections/filament>
- **Flashforge other possible lines (glow/luminous, wood, metal, marble, galaxy, burnt titanium, etc.)** - missing: existence and all values. Why: not attempted (the shared web-search budget was used up and the catalogue pages returned 429)
- **Flashforge PLA Silk** - missing: colourway lineup and whether multi-colour variants share the Silk TDS; any page-level drying or diameter values. Why: HTTP 429 Too Many Requests (two attempts) <https://eu.flashforge.com/products/pla-silk>
- **Flashforge ABS / ABS Pro** - missing: enclosure requirement. Why: the PDF was readable as text, but the 'Print with Enclosure' row has no text values (likely icons) and no PDF renderer was available <https://wiki.flashforge.com/resource/filament_tips/flashforge_filament_guide.pdf>
- **Flashforge PETG-CF** - missing: page HDT (reported 74C). Why: not cited and not read <https://enterprise.flashforge.com/products/petg-cf>

### kexcelled (15)

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
- **Kexcelled K5 ABS Metal (older TDS 'ABS K5P')** - missing: all (not written). Why: only a 2022 reseller TDS copy found; could not confirm it is the current line <https://3dprinteq.dk/wp-content/uploads/KEXCELLED-ABS-K5P-Technical-Date-Sheet-EN-1-1.pdf>
- **Kexcelled K5 PLA Magic / Color Change / Gradient / Streams / Coffee / Tea; K5 ABS Color Change** - missing: all. Why: not attempted (time)
- **Kexcelled K9 PEBA; K6 UCM 300; soft TPU grades 60A-80A** - missing: all. Why: not attempted (time)
- **Kexcelled K11/K12 PEEK, PEEK PRO, PEEK CF10, PEEK GF10, PEEK Ultra, PEKK, PPSU, PEI 1010, PEI 9085** - missing: all. Why: not attempted (time); these also need nozzle temperatures far above Bambu printers' limits
- **All 38 written Kexcelled lines** - missing: drying, colours, max volumetric speed, fibre content (CF/GF lines), hardened-nozzle requirement; most densities are ranges, so filament_density is unset except K5 ABS, K5 ABS Rapid, K3 ASA, K6 HIPS. Why: no specs published in the TDS

### 3dxtech (56)

- **3DXTech (all lines) official site** - missing: official product-page print recommendations for every line; all entries fall back to third-party-hosted TDS copies or MatterHackers listings. Why: blocked/429 Too Many Requests on every attempt (www and non-www hosts); pdf.directindustry.com 3DXTech catalogs returned 403; static.dajiqun.com TDS mirror refused the connection <https://www.3dxtech.com/>
- **3DXTech 3DXMAX ASA** - missing: density, HDT. Why: blocked/429 <https://www.3dxtech.com/3dxmax-asa-1kg/>
- **3DXTech 3DXMAX PETG** - missing: colors, drying, diameter tolerance, current-revision check. Why: only an older TDS (Rev 2.1) on a third-party CDN could be read <https://cdn.shopify.com/s/files/1/0965/1648/files/PETG_Filament_v2.1.pdf>
- **3DXTech CarbonX PLA+CF** - missing: density, Tg, HDT. Why: blocked/429 <https://www.3dxtech.com/carbon-fiber-pla-1/>
- **3DXTech CarbonX ASA+CF** - missing: density, Tg, HDT. Why: blocked/403 <https://pdf.directindustry.com/pdf/3dxtech/carbonx-carbon-fiber-asa-3d-printing-filament/196785-970252.html>
- **3DXTech CarbonX ezPC+CF** - missing: nozzle range, bed range, density, Tg, HDT. Why: only single values published (275C / bed 95C), no range <https://www.matterhackers.com/store/l/3dxtech-carbonx-black-ezpccf-filament/sk/MKWN4KHH>
- **3DXTech ezPC** - missing: density. Why: blocked/429 <https://www.3dxtech.com/>
- **3DXTech CarbonX Nylon+CF [Gen3]** - missing: nozzle range, bed range, drying. Why: the TDS gives specimen print conditions only; the product page was blocked (429) <https://asset.conrad.com/media10/add/160267/c1/-/gl/002543874DS00/tehnicni-podatki-2543874-3d-xtech-nyl3010500bk0-carbonx-cf-polyamid-pa6-3d-tiskalnik-filament-pa-poliamid-odporno-na-kemikalije-175-mm-500-g-c.pdf>
- **3DXTech CarbonX PA12+CF** - missing: nozzle range, bed range, drying. Why: the TDS gives specimen conditions only; the product page was blocked (429) <https://datasheet.sic-components.com/CF_PA12_v1.pdf>
- **3DXTech Obsidian PA6+CF** - missing: density, Tg, HDT, tolerance. Why: blocked/429 <https://www.3dxtech.com/>
- **3DXTech CarbonX PEEK CF20** - missing: nozzle range, bed range, chamber, drying. Why: the TDS gives specimen conditions only <https://cdn.shopify.com/s/files/1/1339/4265/files/CF20_PEEK_v1.pdf>
- **3DXTech CarbonX PEI 9085+CF** - missing: nozzle range, bed range, drying. Why: the TDS gives specimen conditions only <https://cdn.shopify.com/s/files/1/0658/0033/9668/files/CF_Ultem_9085.pdf>
- **3DXTech CarbonX PEI 1010+CF** - missing: density, HDT. Why: blocked/429 <https://www.3dxtech.com/>
- **3DXTech 3DXSTAT ESD-PLA** - missing: density, drying, Tg, tolerance. Why: blocked/429 <https://www.3dxtech.com/>
- **3DXTech 3DXSTAT ESD-PETG** - missing: density, Tg, HDT. Why: blocked/429 <https://www.3dxtech.com/>
- **3DXTech 3DXSTAT ESD-ABS** - missing: density, Tg, HDT. Why: blocked/429 <https://www.3dxtech.com/>
- **3DXTech 3DXSTAT ESD-PEI** - missing: density, Tg, HDT, Ultem grade confirmation. Why: blocked/429 <https://www.3dxtech.com/>
- **3DXTech 3DXSTAT ESD-PEI 9085** - missing: nozzle range, bed range, drying. Why: the TDS gives specimen conditions only <https://cdn.shopify.com/s/files/1/0658/0033/9668/files/ESD_Ultem9085_v1_tds.pdf>
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

### protopasta (8)

- **Protopasta Composite Metal PETG (Iron / Copper / Steel)** - missing: all. Why: no specs published (only 'standard temperatures in the Generic PETG profile', avoid <2 mm3/s, density '~2x PETG') <https://proto-pasta.com/blogs/stories/endless-exploration-ex16-sept-2026-metal-petg>
- **Protopasta Glass Fiber HTPLA** - missing: nozzle range, density, bed temp. Why: no TDS, SDS or Material Data Table row; only one print temperature (240C at up to 24 mm3/s) <https://proto-pasta.com/products/white-glass-fiber-htpla>
- **Protopasta High Density Iron HTPLA** - missing: nozzle range, density, bed temp. Why: no TDS/SDS; only one print temperature (200C at up to 24 mm3/s) <https://proto-pasta.com/blogs/stories/endless-exploration-ex10-september-2025-high-density-metal-htpla>
- **Protopasta High Density Stainless Steel HTPLA** - missing: nozzle range, density, bed temp. Why: no TDS/SDS; only one print temperature (200C at up to 24 mm3/s) <https://proto-pasta.com/blogs/stories/endless-exploration-ex10-september-2025-high-density-metal-htpla>
- **Protopasta PCTG / High Strength CF PCTG / High Impact CF PCTG / Glass Fiber PCTG** - missing: density; max volumetric speed (CF/GF variants); exact bed range (only 70+/80+). Why: no TDS or SDS published for PCTG; values come from the product pages and blog <https://proto-pasta.com/pages/material-data-table>
- **Protopasta High Strength CF / High Impact CF / Glass Fiber HTPETG** - missing: nozzle low bound, density, drying temp/time. Why: no TDS or SDS published; only an upper nozzle temperature (300C) and bed 100+C <https://proto-pasta.com/blogs/stories/endless-exploration-ex14-may-2026-high-temp-petg>
- **Protopasta Flexible TPU** - missing: nozzle high bound, density, drying temp/time, max volumetric speed. Why: no TDS/SDS; only 'printing starting at 240 C' plus blog speed/temp points <https://proto-pasta.com/products/clear-flexible-tpu>
- **Protopasta Calcium Carbonate PLA** - missing: nozzle range, bed temp, max volumetric speed. Why: the Material Data Table row has no print temperatures; only the SDS density was published <https://proto-pasta.com/pages/material-data-table>

### colorfabb (9)

- **ColorFabb LW-BVOH** - missing: all. Why: no specs published (page has marketing text only; no TDS in the download folder) <https://colorfabb.com/lw-bvoh>
- **ColorFabb PVOH** - missing: all. Why: no products listed (category empty, probably discontinued) <https://colorfabb.com/filaments/materials/support-materials/pvoh>
- **ColorFabb PETG Regrind** - missing: all. Why: no products listed (category empty, probably discontinued) <https://colorfabb.com/filaments/materials/co-polyester-filaments/petg-regrind>
- **ColorFabb nGen** - missing: all (deliberately skipped). Why: not written: category lists only nGen-CF10 and nGen Clear has no product page, so it looks discontinued (TDS still in the download folder) <https://colorfabb.com/filaments/materials/co-polyester-filaments/ngen>
- **ColorFabb HT** - missing: all (deliberately skipped). Why: not written: category returns 404 and HT Clear has no product page, so it looks discontinued (TDS still in the download folder) <https://colorfabb.com/filaments/materials/co-polyester-filaments/colorfabb-ht>
- **ColorFabb PLA Color On Demand** - missing: all (deliberately skipped). Why: custom-colour order service rather than a product line; TDS exists but was not written <https://colorfabb.com/custom-colored-pla-filament>
- **ColorFabb PLA-HP / PLA Vibers / nGen-CF10 / PET Flex Max / LW-PET / LW-PET Flex / LW-PET Flex Max / allPHA** - missing: density. Why: entries written; the official TDS gives no density (allPHA prints N/A)
- **ColorFabb bronzeFill / copperFill / steelFill** - missing: density in fields. Why: entries written; TDS densities (3.9 / 4 / 3.13) are above the validator's 0.5-3.0 limit, so they were moved to _notes
- **ColorFabb rPLA, corkFill, stoneFill, rPETG, PA-CF Low Warp, PLA Vertigo, PLA Chameleon** - missing: rPLA/corkFill/stoneFill/rPETG: density; rPETG: Tg, tolerance, speed; PA-CF Low Warp: drying, nozzle requirement. Why: entries written from the product page only; no TDS published

### formfutura (27)

- **Formfutura MetalFil - Classic Copper** - missing: filament_density field (value recorded in _notes only). Why: published density 3.4 g/cc exceeds the library validator's 0.5-3.0 range <https://formfutura.com/web/content/256597?download=true>
- **Formfutura High Gloss PLA ColorMorph** - missing: drying, HDT/Tg, print speed (page values only). Why: the TDS linked on the page is the plain High Gloss PLA datasheet, not a ColorMorph one <https://formfutura.com/web/content/256568?download=true>
- **Formfutura EasyFil PLA - Glow in the Dark** - missing: drying, HDT/Tg, print speed range. Why: no TDS linked on the product page <https://formfutura.com/filaments/easyfil-pla-glow-in-the-dark>
- **Formfutura ABSpro** - missing: Formfutura-branded TDS (thermal values are from the Flashforge-branded sheet only). Why: the linked TDS is a Flashforge-branded 'ABS Pro' datasheet; fields use Formfutura page values instead <https://formfutura.com/web/content/254657?download=true>
- **Formfutura AquaSolve - PVA** - missing: Formfutura-branded TDS, drying. Why: the linked TDS is a Flashforge-branded PVA datasheet; fields use Formfutura page values instead <https://formfutura.com/web/content/256478?download=true>
- **Formfutura EasyFil ePETG / HDglass / CarbonFil CF03 / Kratos PC / ApolloX CF10 / STYX PA6 / STYX PA6-CF15 / AthenaX / Python Flex TPU 90A & 98A** - missing: drying temperature/time for most of these; print speed range. Why: TDS gives material properties only, with no print settings; print settings taken from product pages
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

### amazon-basics (6)

- **Amazon Basics PLA** - missing: nozzle temp, bed temp, density, diameter tolerance, drying. Why: official manual copy returned 403 (HTML and PDF); the Amazon listing B07SZLYWS2 gives no temperatures <https://manuals.plus/amazon-basics/b09yrd4ztw-pla-3d-printer-filament-manual.pdf>
- **Amazon Basics Silk PLA** - missing: nozzle temp, bed temp, density, drying. Why: listing gives no temperatures or density; no TDS found <https://www.amazon.com/dp/B08894NK7S>
- **Amazon Basics PETG** - missing: all. Why: mirror sites returned 403, Amazon search returned 503, Amazon ASIN not found (web search budget used up) <https://www.desertcart.lk/products/705048331-amazon-basics-petg-3d-printer-filament-1-75-mm-yellow>
- **Amazon Basics TPU** - missing: all (incl. Shore hardness). Why: reseller page returned 403; Amazon ASIN not found (web search budget used up) <https://www.ypc.co.uk/product/amazon-basics-tpu-3d-printer-filament-1-75-mm-blue-1-kg-spool-2-2-lbs/>
- **Amazon Basics ABS** - missing: all. Why: not found; current availability unconfirmed
- **Amazon Basics PLA** - missing: nozzle temp, bed temp, density, diameter tolerance. Why: blocked/403 (as the researcher reported; it is not a cited source and was not retried) <manuals.plus copy of the Amazon Basics PLA manual (B09YRD4ZTW / B07SZLYWS2)>

## Values removed by the source check

- [bambu-lab-other] ASA-CF: _notes sentence 'A retailer reports this line as discontinued; still listed by resellers.' - not in any cited source (the cited Welectron page shows only 'Out of stock', not discontinued)
- [bambu-lab-other] TPU 95A HF: _hardness '95A (Shore)' reworded to '95A (from product name; TDS does not state a Shore value)' - the V1.0 TDS never prints a Shore hardness for the HF line (only TPU 95A and TPU for AMS TDS do)
- [polymaker-a] PolyLite PLA Pro: nozzle_temperature_range_high 220 - the cited TDS PDF now serves V5.5, which prints 190-230; the older V5.4 wiki value (190-220) was moved to conflicts
- [polymaker-a] PolyLite PLA Pro: filament_density 1.22 - the V5.5 TDS PDF prints 1.23; 1.22 (wiki V5.4) was moved to conflicts
- [polymaker-a] PolyLite PLA Pro: filament_retraction_speed 30-60 - the V5.5 TDS prints 20-40; 30-60 (wiki V5.4) was moved to conflicts
- [polymaker-a] PolyLite PLA Pro: _print_speed 30-70 mm/s - the V5.5 TDS prints 50-200 mm/s; the old value was moved to conflicts
- [polymaker-a] PolyLite PLA Pro: _vicat 62.7 / _hdt_0.45MPa 59.3 - the V5.5 TDS prints 63 / 59; the old values were moved to conflicts. _drying 55C 6h and _enclosure Not needed were added because the V5.5 TDS prints them
- [polymaker-a] PolyLite ABS: filament_density 1.12 - the current TDS PDF at the cited URL is V5.5 and prints 1.04 g/cm3; 1.12 (wiki V5.4 text) was moved to conflicts
- [polymaker-a] ASA: _enclosure 'Needed (ambient temperature)' changed to 'Needed' to match the V6.0 TDS now served at the cited URL (the wiki V5.4 text has the longer wording). Notes now say V6.0
- [polymaker-a] Notes only: dropped the unverified TDS dates '(2026-04)' on LW-PLA and '(2026-03)' on PETG. PolyTerra PLA version is now marked as coming from the file name. CosPLA notes now give the version B values printed in the same TDS (bed 30-60, speed 50-200, density 1.22)
- [polymaker-b] Matte PLA for Production: filament_retraction_length 1-3 - the official TDS (Matte PLA_TDS_Polymaker.pdf, linked from the cited wiki TDS page) prints 1 mm, so it is now 1; the wiki's 1-3 is moved to conflicts
- [polymaker-b] ABS Pro: filament_retraction_length 1-3 / filament_retraction_speed 20-40 - the TDS (TDS_Polymaker_ABS_Pro_V1) prints 1 mm / 20 mm/s, so it is now 1 / 20; the wiki's 1-3 / 20-40 is moved to conflicts
- [polymaker-b] ABS Max: filament_retraction_length 1-3 / filament_retraction_speed 20-40 - the TDS V1.1 prints 1 mm / 20 mm/s (direct drive), so it is now '1 (direct drive)' / '20 (direct drive)'; the wiki values are moved to conflicts
- [polymaker-b] PolyFlex TPU90: _ams 'Bambu does not support 90A TPU in the AMS; feed externally' - no cited source says this; replaced with the wiki/shop statement 'very soft, direct drive extruder recommended'
- [polymaker-b] HT-PLA Pro: conflicts entry 'Spool label pictured on the TDS appears to read 210-230 C (too small to confirm)' - could not be confirmed; the TDS V1.4 PDF and the wiki both print 230 C only. Removed
- [polymaker-b] Fiberon ASA-CF08: chamber_temperatures 'enclosure recommended' - the TDS prints 'Chamber temperature: Room temp.', so it is now 'room temperature'; the wiki's 'Enclosure Recommended' is moved to conflicts and _enclosure 'recommended' is kept
- [polymaker-b] HT-PLA-GF: _fiber_content 'glass fibre (percentage not published)' - corrected to '12% glass fibre (TDS)' because the cited TDS V1.1 prints 12%
- [polymaker-b] Panchroma Neon PLA / Panchroma UV Shift PLA: _ams (AMS-compatible only) - expanded with the wiki's own warning that the abrasive additive means Polymaker does not recommend printing them in an AMS with plastic gears and tubes
- [polymaker-b] Panchroma Dual Silk PLA: _ams reworded to match the wiki ('compatible with AMS and other multi-material systems'); the wiki page does not mention hardened spool edges
- [esun] PLA-ST: _hdt_0.45MPa 52 - TDS v4.0 Nov 2021 prints HDT as N/A
- [esun] PLA-Silk Mystic: _hdt_0.45MPa 54.7 - TDS v4.0 Nov 2022 prints HDT as N/A (54.7 belongs to the sibling Silk Magic TDS)
- [esun] eTwinkling: _hdt_0.45MPa 67 - current TDS v4.0 prints HDT as N/A; 67 appears only in the 2019 datasheet, which is already listed in conflicts
- [esun] ePA12-CF: _hdt_0.45MPa 160 - TDS prints HDT 94.1C (0.45MPa); 160C is the short-term use temperature. Replaced with 94.1
- [esun] PLA Basic: _print_speed 300 - TDS prints '<300'. Corrected to '<300'
- [esun] PLA-HF: _max_print_speed '900 (varies by machine)' - TDS prints '<900'. Corrected
- [esun] PLA-Matte / PLA-Silk / PLA-Rock / PLA-Clear: _drying '50C 8h' - TDS prints '50C >8H'. Corrected to '50C >8h'
- [esun] PETG+ / PET-Luminous / PET-Basic: _drying '60C 8h' - TDS prints '60C >8H'. Corrected to '60C >8h'
- [esun] PETG-Matte / PETG-Basic: _drying '60C (duration not legible)' - TDS prints only '60C', with no duration. Note reworded
- [esun] ePA12-CF / ePAHT-CF: _drying '70C 12h' - TDS prints '70C/>12H'. Corrected to '70C >12h'
- [esun] eTPU-95A / TPU-HS: _drying '55C 4h' - TDS prints '55C/>4H'. Corrected to '55C >4h'
- [esun] PVA: _drying '45C 10h' - TDS prints '45C/>10H'. Corrected to '45C >10h'
- [esun] PLA-Matte, PLA-Silk, PLA-Clear: _print_speed '200' -> '<200'; PLA-Rock '250' -> '<250'; PLA-Metal, PETG+, PET-Luminous '250' -> '<=250'; PET-Basic '250' -> '<250' (as printed)
- [esun] ADDED (printed in the cited TDS): PLA _hdt 53; PLA-Lite _hdt 53 (note had said 'not published'); ASA+ _hdt 95.5; ePAHT-CF _hdt 190; ePC _hdt 80; PET-CF _vitrification '70 (Tg)'; filament_max_volumetric_speed 4 for PETG-Basic, PET-CF, eABS-CF and eABS-GF, and 10 for ASA+ (each printed as 'Maximum volumetric flow rate' in the TDS print-test block, Bambu P1S 0.4 mm)
- [elegoo] PLA Basic: filament_diameter 1.75 - the cited page's text never prints the diameter. 1.75mm appears only in image filenames and other products' listings
- [elegoo] PLA-CF: filament_diameter 1.75 - the cited page's text never prints the diameter. 1.75mm appears only in image filenames and other products' listings
- [elegoo] Rapid TPU 95A: filament_diameter 1.75 - the cited page's text never prints the diameter. 1.75mm appears only in image filenames and other products' listings
- [elegoo] ABS: filament_diameter 1.75 - the cited page's text never prints the diameter. 1.75mm appears only in image filenames
- [elegoo] PLA Sparkle: filament_diameter 1.75 - the cited page's text never prints the diameter. 1.75mm appears only in image filenames and other products' listings
- [elegoo] PC: filament_diameter 1.75 - the cited page's text never prints the diameter. 1.75mm appears only in image filenames and other products' listings
- [elegoo] PETG-GF: filament_diameter 1.75 - the cited page's text never prints the diameter. 1.75mm appears only in image filenames and other products' listings
- [overture] Turbo PLA: filament_diameter 1.75 - not printed in the Turbo PLA TDS; the cited product page overture3d.com/products/turbo-pla now redirects to the homepage, so the value has no readable source. Dead page URL removed from sources and the note saying the page is live corrected
- [overture] Air PLA: filament_diameter 1.75 - the only cited source is the TDS, which does not print a diameter
- [overture] Eco PLA: filament_diameter 1.75 - not printed in the Eco PLA TDS; the cited product page overture-eco-pla-filament-1-75mm-1 now redirects to the homepage. Dead URL removed from sources and the note corrected
- [overture] PLA, Easy PLA: _notes melt index load corrected from 2.16 kg to 2.15 kg, as the TDS prints it (correction to a note, not a removed value)
- [jayo] High Speed PLA: filament_diameter 1.75 - not printed on either cited page (entry dropped)
- [jayo] High Speed Matte PLA: filament_diameter 1.75 - neither cited page states a diameter in its text, title or options (the temperature tiers and bed temperature are verified and kept)
- [jayo] TPU Silk 98A: _print_speed 50-200 mm/s - not printed; the page gives only the two tiers 50-100 and 100-200 mm/s, so this was a widened union (_nozzle_by_speed is kept)
- [jayo] ABS: conflicts text '(same values on the 5KG large-spool page)' - that page is not cited and was not verified; the conflict entry itself is verified and kept
- [jayo] TPU 95A: _ams 'not suited to AMS; feed from external spool' - JAYO does not print this; reworded to say JAYO does not state AMS compatibility, plus the general external-spool guidance
- [jayo] PLA+: _notes claim of a cardboard-spool version - not stated in the text of any cited page; reworded (AMS Lite compatibility on the reusable-spool page is verified)
- [jayo] Multi-Color Silk PLA+: _notes 'US/UK/EU' bundle pages - only the US and EU pages were checked; changed to 'US/EU'
- [hatchbox] Hatchbox PLA: conflicts entry 'Amazon listing text quoted by search results: 180-210 C' - not in any cited source and could not be verified, so removed (the matching 180-210 C conflict from the official PLA material page stays)
- [hatchbox] Hatchbox PLA Temperature Color Changing: conflict rewritten (no field changed). The retail Exclusive Release page, which is a cited source, also prints 180-210 C, so it is now named alongside the wholesale page. Fields keep 180-220 C from the Purple/Salmon Red/Orange page.
- [hatchbox] All entries: '_notes' no longer claim hatchbox3d.com returns 403 or that values came from search-engine extracts. Every cited page was fetched directly via its Shopify .json/HTML, and the garbled degree signs (Â°) were cleaned up. No numeric value was changed.
- [inland] Inland PETG+: nozzle_temperature_range_low 210 - the cited Black listing (626528) prints 230-250 in its key features. 210-250 belongs to the Blue sibling (626535), so it is now 230 and 210-250 is moved to conflicts
- [inland] Inland PETG+: bed_all_plates 80-100 - the cited Black listing prints 80 in its key features and 50-80 in its specs table. 80-100 belongs to the Blue sibling (626535), so it is now 80, with 80-100 and 50-80 moved to conflicts
- [creality] HP-TPU: _ams note reworded, not removed. The direct-drive extruder tip on Creality's filament-type page is shared by CR-TPU and HP-TPU, not specific to HP-TPU. No numeric values removed: every fields/published_ranges value was found in a cited Creality source for its own line (parameter reference table, PLA guide, K1 and K2 Plus tables, product pages; diameters 1.75 from product titles).
- [prusament] PLA: filament_density 1.24 - only source is the official TDS inside a zip over 10 MB that could not be read; the product page does not print it
- [prusament] PLA: filament_diameter 1.75 - not printed on the readable product page (zip TDS unreadable)
- [prusament] PLA: _max_print_speed 'up to 200 mm/s' - page only says 'Fast'; zip TDS unreadable
- [prusament] PLA: _hdt_0.45MPa 55 (ISO 75) - page gives 'temperature resistance 55 C' without naming HDT; zip TDS unreadable
- [prusament] PLA: _hdt_1.80MPa 55 (ISO 75) - zip TDS unreadable, not on page
- [prusament] PLA: _diameter_tolerance +/-0.02 - zip TDS unreadable, not on page
- [prusament] PLA Blend: filament_density 1.24 - Blend TDS only inside the unreadable zip
- [prusament] PLA Blend: filament_diameter 1.75 - not on readable page
- [prusament] PLA Blend: _max_print_speed 'up to 200 mm/s' - zip TDS unreadable
- [prusament] PLA Blend: _hdt_0.45MPa 55 (ISO 75) - zip TDS unreadable
- [prusament] PLA Blend: _hdt_1.80MPa 52.5 (ISO 75) - zip TDS unreadable
- [prusament] PLA Blend: _diameter_tolerance +/-0.03 - zip TDS unreadable
- [prusament] PETG Carbon Fiber: filament_density 1.27 - TDS only inside an unreadable zip over 10 MB; the product page does not print it
- [prusament] PETG Carbon Fiber: filament_diameter 1.75 - not on readable product page
- [prusament] PETG Carbon Fiber: _fan_speed 50 - not on product page; zip TDS unreadable
- [prusament] PETG Carbon Fiber: _max_print_speed 'up to 200 mm/s' - zip TDS unreadable
- [prusament] PETG Carbon Fiber: _hdt_0.45MPa 96 (ISO 75) - zip TDS unreadable
- [prusament] PETG Carbon Fiber: _hdt_1.80MPa 80 (ISO 75) - zip TDS unreadable
- [prusament] PLA / PLA Blend / PETG Carbon Fiber: source_quality changed from official_tds to official_page, and the zip removed from sources, because the zip could not be read
- [prusament] PETG Ultraglow: _ams reworded - the product page names PTFE tubes and Nextruder or hardened gears, not 'feeder gears' or the AMS
- [prusament] PEI 1010: _drying 'before every print' wording dropped - TDS/page print only '150C 6-8h' plus keeping it in a dry box while printing
- [push-plastic] Carbon Fiber ABS: _fiber_content ~10% - not printed in the CF ABS TDS or print-settings sheet; product page unreachable (only retailer pages that aren't cited mention 10%)
- [push-plastic] Carbon Fiber PC+PBT: _fiber_content ~10% - not in the CF PC+PBT TDS or print sheet; product page unreachable
- [push-plastic] Carbon Fiber PETG: _fiber_content ~10% - not in the CF PETG TDS or print sheet; product page unreachable
- [push-plastic] Carbon Fiber Nylon: _fiber_content ~10% - not in the TDS or print sheet; kept only the TDS base polymer 'PA6/66 + Carbon Fiber' with the loading marked as not stated
- [push-plastic] Nylon: conflicts entry (product page says no heated chamber needed) and the matching _enclosure parenthetical - product page unreachable
- [push-plastic] High Heat+Tough PLA: conflicts entry (product page annealing 100-120C up to 30 min) - product page unreachable
- [push-plastic] PEI 9085: _vitrification ~185 (Tg, product page) - product page unreachable
- [push-plastic] PEI 9085: conflicts entry (product page 350C extruder / 150C+ bed / 30mm/s) - product page unreachable
- [push-plastic] PEI 1010: _vitrification ~215 (Tg, product page) - product page unreachable
- [push-plastic] PEI 1010: conflicts entry (product page 375C / 160C+ bed / 30mm/s) - product page unreachable
- [push-plastic] ABS: _notes claim that the site says Bambu needs custom profiles and only publishes PETG Bambu profiles - not checkable
- [push-plastic] All entries: _notes 'Also sold in 2.85mm' - only on product pages, which were unreachable
- [push-plastic] HIPS: _notes 'soluble in d-limonene' - not in the HIPS TDS; product page unreachable
- [atomic-filament] Carbon Fiber PETG: _drying 65C 8-16h - only the Atomic FAQ's general PETG row prints it, not this CF line (a generic material table)
- [atomic-filament] Carbon Fiber ABS: _drying 80C 4-8h - only the Atomic FAQ's general ASA/ABS row prints it, not this CF line
- [atomic-filament] Carbon Fiber ABS: _diameter_tolerance +/-0.02 - not printed on either cited CF ABS page (1 kg or 3.5 kg)
- [atomic-filament] Carbon Fiber ASA: _drying 80C 4-8h - FAQ is not among this entry's sources, and the FAQ row is the general ASA/ABS value, not specific to CF
- [atomic-filament] PCTG PRO: _diameter_tolerance +/-0.02 - not printed on any cited PCTG PRO page (only on the CF PCTG sample coil, which is a sibling line); claims in _notes about 'nearly ZERO warpage', odor and 'runs on PETG PRO settings' also removed because the cited pages do not print them
- [atomic-filament] PETG PRO: conflicts entry corrected - the Starry Night page prints nozzle 240-265C, not 232-245C (only the Indigo Golden Sparkle page gives 232-245C)
- [fiberlogy] Fiberlogy HS PLA Clear: filament_diameter 1.75 - not printed on the cited product page (the page's linked TDS PDF is not cited)
- [fiberlogy] Fiberlogy PLA FiberSatin: filament_diameter 1.75 - not printed on the cited product page (the linked TDS prints 1.75 but is not cited)
- [fiberlogy] Fiberlogy PLA FiberWood: filament_diameter 1.75 - not printed on the cited product page (the linked TDS prints 1.75/2.85 but is not cited)
- [fiberlogy] Fiberlogy PLA Impact: filament_diameter 1.75 - not printed on the cited product page (the linked TDS prints 1.75 but is not cited)
- [fiberlogy] Fiberlogy PLA Matte: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy PLA Mineral: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy PLA+CF: filament_diameter 1.75 - not printed on the cited product page (the linked TDS prints 1.75 but is not cited)
- [fiberlogy] Fiberlogy rPLA: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy Velvet PLA: filament_diameter 1.75 - not printed on the cited product page (the linked TDS prints 1.75 but is not cited)
- [fiberlogy] Fiberlogy FiberWORKS PLA: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy FiberWORKS PETG: filament_diameter 1.75 - not printed on the cited product page (the linked TDS prints 1.75 but is not cited)
- [fiberlogy] Fiberlogy Easy PETG: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy PETG ESD: filament_diameter 1.75 - not printed on the cited product page (the linked TDS prints 1.75 but is not cited)
- [fiberlogy] Fiberlogy PETG FR V0: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy PETG Matte: filament_diameter 1.75 - not printed on the cited product page (the linked TDS prints 1.75 but is not cited)
- [fiberlogy] Fiberlogy PETG+CF: filament_diameter 1.75 - not printed on the cited product page (the linked TDS prints 1.75 but is not cited)
- [fiberlogy] Fiberlogy PETG+PTFE: filament_diameter 1.75 - not printed on the cited product page (the linked TDS prints 1.75 but is not cited)
- [fiberlogy] Fiberlogy rPETG: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy PP: filament_diameter 1.75 - not printed on the cited product page (the linked TDS prints 1.75 but is not cited)
- [fiberlogy] Fiberlogy rPP: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy Nylon PA12: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy Nylon PA12+CF: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy Nylon PA12+GF: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy rNylon: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy ABS: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy ABS ESD: filament_diameter 1.75 - not printed on the cited product page (the linked TDS prints 1.75 but is not cited)
- [fiberlogy] Fiberlogy ABS Plus: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy ABS+GF: filament_diameter 1.75 - not printed on the cited product page (the linked TDS prints 1.75 but is not cited)
- [fiberlogy] Fiberlogy Easy ABS: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy PC/ABS: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy ASA: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy ASA Matte: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy rASA: filament_diameter 1.75 - not printed on the cited product page (page links no TDS)
- [fiberlogy] Fiberlogy CPE HT: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy CPE HT+Ag Antibac: filament_diameter 1.75 - not printed on the cited product page (the linked TDS prints 1.75 but is not cited)
- [fiberlogy] Fiberlogy FiberFlex 30D: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy FiberFlex Aero: filament_diameter 1.75 - not printed on the cited product page (the linked TDS prints 1.75 but is not cited)
- [fiberlogy] Fiberlogy FiberFlex+CF: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy MattFlex 40D: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy HIPS: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy PCTG: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy PCTG+CF: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy PCTG+GF: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy PEI 9085: filament_diameter 1.75 - not printed on the cited product page
- [fiberlogy] Fiberlogy BVOH: filament_diameter 1.75 - not printed on the cited product page (the linked TDS prints 1.75 but is not cited)
- [fiberlogy] Fiberlogy MattFlex 40D: _hardness 40D (Shore, per product name) - the page never states a Shore hardness; the value comes only from the product name
- [fiberlogy] Fiberlogy FiberFlex 30D: _ams clause 'soft TPU in AMS is generally not recommended' - not on the page; moved to _notes and marked as a checker note
- [fillamentum] ASA CF10 Carbon: _fiber_content "10% carbon fibre (CF10)" - no cited source states a fibre percentage; the 10 % on the product page is elongation at break. Changed to 'percentage not stated'.
- [fillamentum] ASA CF10 Carbon: _enclosure "heated chamber required" - the 2025 guide says 'Not needed but recommended' (it advises a closed heated chamber if possible). Note corrected.
- [fillamentum] OrCA: _diameter_tolerance +/-0.05 - this comes from the product page and is contradicted by the official TDS (20/07/2023), which gives +/-0.1. Changed to +/-0.1 and moved the page value to conflicts.
- [fillamentum] PLA Extrafill: _notes 'Also sold in 2.85 mm on some colours' - not printed in any cited source (the page lists only 1.75 mm). Sentence removed.
- [fillamentum] CPE CF112 Carbon: _fiber_content 'percentage not stated' - corrected to 12.5 % as printed in the cited printing guide (not a new slicer value).
- [fillamentum] Nylon CF15 Carbon: _fiber_content - added 15 % as printed in the cited printing guide.
- [fillamentum] Nylon AF80 Aramid: _fiber_content - added 8 % as printed in the cited printing guide.
- [fillamentum] Flexfill TPU 92A: _hardness 92 Shore A kept from the product page; added a conflict because the TDS (26/08/2019) prints 91 Shore A.
- [spectrum] Spectrum PLA Premium: filament_diameter 1.75 - not printed in the TDS or on the official product page; the only source was the official shop listing (shop.spectrumfilaments.com), which refused the connection, so the value is unverified. The _notes text that quoted that shop listing was replaced with a note saying the shop could not be reached.
- [spectrum] Spectrum PET CF15: _layer_height '>= 0.20 mm' changed to '0.20 mm' - the TDS prints a plain 0.20mm layer height, not a minimum.
- [eryone] TPU: textured_plate_temp 55-70 - the page says 'PEI Magnetic Print Surface: 55~70', which does not say which Bambu plate it means. The value was moved out of the slicer key to the note key _bed_pei_magnetic.
- [eryone] TPU 85A: textured_plate_temp 55-70 - same PEI magnetic surface wording. Moved to _bed_pei_magnetic.
- [eryone] TPU 90A: textured_plate_temp 55-70 - same PEI magnetic surface wording. Moved to _bed_pei_magnetic.
- [eryone] PLA Silk Rainbow / PLA Carbon Fiber / PLA Marble / ABS-CF: the cited TDS does not print filament_diameter 1.75. Kept by adding the official product page that does print 1.75mm (eryone3d.com/products/macaron-rainbow-pla-filament, /pla-carbon-fiber-filament, /marble-pla, and the combined ABS & ABS-CF listing /abs-filament). No new values were added.
- [eryone] Conflicts added from the cited pages (official TDS values kept in fields): PLA bed 55-70; PLA+ nozzle 200-230 (FAQ); PLA Carbon Fiber bed 60-80; ABS+ nozzle 230-270 and bed 80-100; ABS-CF bed 80-110; ASA Light-Weight nozzle 220-280 (page header); PETG nozzle 215-230 and bed 80-100 (older text); PETG-CF nozzle 200-240 and bed 70-90/75-85; TPU nozzle 200-220 (spec header).
- [eryone] All other fields and published_ranges values were found in the TDS PDFs (read with pdftotext) or on the eryone3d.com product pages. Every bambu_parent is in bambu_studio_presets.txt.
- [amolen] PLA Silk Triple Color: _diameter_tolerance +/-0.02 - only the variety-pack page prints it; the 1 kg product page prints 1.75mm +/-0.03mm. Replaced it with +/-0.03 and moved +/-0.02 (pla-silk-triple-pack) to conflicts.
- [geeetech] GEEETECH Marble PLA: _print_speed 30-60 mm/s - comes only from the generic Marble PLA section of the GEEETECH wiki, not the product page
- [geeetech] GEEETECH Marble PLA: _hardened_nozzle_required - generic wiki material advice, not on the product page; moved into _notes with the source named
- [geeetech] GEEETECH Luminous PLA: _hardened_nozzle_required - generic wiki luminous-blend advice, not on the product page; moved into _notes with the source named
- [geeetech] GEEETECH Carbon Fiber PLA: nozzle 200-230, bed_all_plates 50-60, _min_nozzle 0.4 - generic wiki material table only; entry dropped
- [sovol] SOVOL PLA Glow in Dark: _hardened_nozzle_required 'recommended (Sovol blog...)' - Sovol blog unreachable (HTTP 429); search only attributes the abrasion warning to a third-party guide
- [sovol] SOVOL PETG: _notes claim 'higher softening point than regular PETG' - not found in readable part of the Amazon listing
- [sovol] SOVOL TPU: nozzle_temperature_range_low 220 - not printed in any readable cited source (Amazon bullets not served; search found no Sovol source)
- [sovol] SOVOL TPU: nozzle_temperature_range_high 220 - same as above
- [sovol] SOVOL TPU: bed_all_plates 50-70 - not found in any readable cited source
- [sovol] SOVOL TPU: _print_speed 60 - not found in any readable cited source
- [sovol] SOVOL Rapid PETG: _max_print_speed 300 - titles say only 'High Speed'; no mm/s figure found in a readable source
- [qidi-tech] PLA Rapido: _diameter_tolerance +/-0.03 - only in TDS, whose text is outlined/unreadable
- [qidi-tech] PLA Rapido: _notes TDS density range 1.21~1.23 and melt ~160C - TDS unreadable; note rewritten (Tg 60 and Vicat 73 kept from product page, HDT 59 attributed to filament guide, print speed <=300 attributed to filament guide); source_quality official_tds -> official_page, TDS URL removed from sources
- [qidi-tech] PLA Matte Rapido: bed_all_plates 30-60 - only in unreadable TDS (guide prints textured/smooth 45-60, cool 30-45, which stay)
- [qidi-tech] PLA Matte Rapido: _vitrification ~60 (Tg) - only in unreadable TDS
- [qidi-tech] PLA Matte Rapido: _vicat 57 - only in unreadable TDS
- [qidi-tech] PLA Matte Rapido: _diameter_tolerance +/-0.03 - only in unreadable TDS; also dropped TDS density-range/melt note; source_quality -> official_page, TDS URL removed
- [qidi-tech] PETG-Tough: cool_plate_temp 60-80 (filament guide) - the guide gives no Cool Plate value for PETG-Tough (only textured/smooth 70-80)
- [qidi-tech] ABS Rapido: filament_density 1.05 - only in unreadable TDS; product page has no spec table
- [qidi-tech] ABS Rapido: bed_all_plates 80-100 - only in unreadable TDS (guide 90-110 kept as textured_plate_temp; guide conflict entry removed since nothing contradicts it now)
- [qidi-tech] ABS Rapido: _vicat 95 - only in unreadable TDS
- [qidi-tech] ABS Rapido: _diameter_tolerance +/-0.03 - only in unreadable TDS
- [qidi-tech] ABS Rapido: fan_min_speed/fan_max_speed 0-50% - only in unreadable TDS; replaced by the guide's printed 0-80% for this line; source_quality -> official_page, TDS URL removed
- [qidi-tech] PLA Wood: _print_speed '30-60 mm/s (filament guide)' - guide prints 40-80 mm/s for PLA-Wood; corrected
- [qidi-tech] PPS-CF: filament_diameter 1.75 - not printed on the product page or the readable TDS page
- [qidi-tech] PPS-CF: _diameter_tolerance +/-0.05 - not printed in any readable source
- [qidi-tech] PEBA 95A: filament_diameter 1.75 - not printed in the TDS or on the product page
- [qidi-tech] TPU-Aero: _notes printed-part density '0.88-0.93 ... 0.50-0.54' - 0.88/0.50 are the TDS flow ratios, not densities; rewritten as 0.93 g/cm3 (240C) to 0.54 g/cm3 (270C)
- [qidi-tech] ABS-GF25: _notes '0.5 kg spool sold as clearance' - not in sources; replaced with TDS spool sizes 500 g/1 kg/2.5 kg/3 kg
- [flashforge] Flashforge ABS: _enclosure 'Filament Guide marks Print with Enclosure for ABS' - the Filament Guide's text layer has no enclosure value (row is likely icon-only), so it could not be confirmed
- [flashforge] Flashforge ABS Pro: _enclosure 'Filament Guide marks Print with Enclosure for ABS Pro' - same reason, not confirmable in the guide text
- [flashforge] Flashforge PETG-CF: conflicts entry 'search-engine summary of enterprise.flashforge.com/products/petg-cf quoted HDT 74C' - source never read, so it is not a citable conflict
- [flashforge] Flashforge HS PLA: conflicts entry 'search-engine summary of eu.flashforge.com/products/hs-pla quoted nozzle 190-240C, drying 50C 5h' - source never read, so it is not a citable conflict
- [flashforge] Flashforge PETG: _notes sentence claiming the EU store lists 'HS PETG' at /products/petg - not in any cited source
- [flashforge] Flashforge PLA Silk: source https://eu.flashforge.com/products/pla-silk and the _notes claim about its single/dual/triple/rainbow colourways - page returned HTTP 429 twice, so the claim was replaced with a statement that it is unverified
- [flashforge] Flashforge PLA Matte / PLA-CF / PETG-CF / PC: _notes water absorption '<0.5%'/'<0.5%'/'<0.8%'/'<0.8%' corrected to the TDS-printed '0.5%'/'0.5%'/'0.8%'/'0.8%'
- [kexcelled] K8 OBC: _notes claim 'Kexcelled catalogue says it inherits PP's flexibility and chemical resistance' - not in the cited TDS (the catalogue is not a cited source). Replaced it with what the TDS prints: chemical name 'Olefin Block Copolymers' and its listed characteristics. No fields or ranges changed.
- [3dxtech] 3DXMAX PETG: filament_diameter 1.75 - cited TDS Rev 2.1 does not print a filament diameter
- [3dxtech] CarbonX Nylon+CF [Gen3]: filament_diameter 1.75 - cited Conrad TDS Rev 3.0 / Gen2 TDS do not print a filament diameter (only in Conrad URL slug)
- [3dxtech] CarbonX PA12+CF: filament_diameter 1.75 - cited TDS Rev 1.0 does not print a filament diameter
- [3dxtech] CarbonX PEEK CF20: filament_diameter 1.75 - cited TDS Rev 1.0 does not print a filament diameter
- [3dxtech] CarbonX PEI 9085+CF: filament_diameter 1.75 - cited TDS Rev 1.0 does not print a filament diameter
- [3dxtech] 3DXSTAT ESD-PC: filament_diameter 1.75 - cited TDS does not print a filament diameter
- [3dxtech] 3DXSTAT ESD-PEI 9085: filament_diameter 1.75 - cited TDS Rev 1 does not print a filament diameter
- [3dxtech] CarbonX Nylon+CF [Gen3]: _hardened_nozzle_required yes - TDS lists only a 0.4mm specimen nozzle; no hardened-nozzle requirement printed
- [3dxtech] CarbonX PA12+CF: _hardened_nozzle_required yes - TDS lists only a 0.4mm specimen nozzle; no hardened-nozzle requirement printed
- [3dxtech] CarbonX PEEK CF20: _hardened_nozzle_required yes - TDS lists only a 0.4mm specimen nozzle; no hardened-nozzle requirement printed
- [3dxtech] CarbonX PEI 9085+CF: _hardened_nozzle_required yes - TDS lists only a 0.4mm specimen nozzle; no hardened-nozzle requirement printed
- [3dxtech] ezPC: _hdt_0.45MPa 112 - MatterHackers listing prints HDT 112C with no test load; the 0.45MPa load came from an uncited aggregator (note reworded to 'HDT 112C, no load stated')
- [protopasta] Carbon Fiber PLA: _notes claim 'same settings, supply limited' for Recycled CF PLA - not printed on any cited source (replaced with Recycled CF PLA page's 'wear resistant nozzle recommended')
- [protopasta] Magnetic Iron PLA: _notes '45 wt% iron (EX10 blog)' - EX10 blog is not a cited source for this entry; kept TDS-backed ferromagnetic/rustable/brittle/abrasive wording
- [protopasta] Stainless Steel PLA: _notes '60 wt% 400-series stainless' and 'Blue/Burgundy/Gold variants are the same 60 wt% composite' - not in the cited TDS/SDS/Material Data Table
- [protopasta] High Density Iron HTPLA: _notes 'Protopasta recommends hard steel nozzles for its metal composites' - no cited source says this for this line; reworded as not stated, with the steel nozzle used in EX10
- [protopasta] High Density Stainless Steel HTPLA: _notes 'lowest ultimate strength' and 'hard steel nozzle advised' - not in the cited page/blog text
- [protopasta] Static Dissipative Carbon Fiber PLA: _notes 'product page: 1e4-1e6 ohm' - no product page is cited; replaced with the TDS figure 'typically 1e4-1e7 ohm'
- [protopasta] Carbon Fiber PETG: _notes 'Recycled Carbon Fiber PETG is from the same waste stream (wear resistant nozzle recommended)' - not on the cited CF PETG page/SDS/Material Data Table
- [protopasta] High Strength Carbon Fiber PCTG: _hardened_nozzle_required 'Protopasta recommends hard steel nozzles for its CF materials' - not on the cited PCTG page/EX12 blog; reworded as not stated, citing the CF PLA/PETG rows only as context
- [protopasta] High Impact Carbon Fiber PCTG: _hardened_nozzle_required - same as High Strength CF PCTG
- [protopasta] Flexible TPU: _notes 'Clear Rigid TPU (70D) is discontinued' - not printed in the cited page or EX3 blog
- [protopasta] c-Matte PLA: _notes 'based on HFPLA; low nozzle wear (brass-like hardness)' - those statements are on the Calcium Carbonate PLA page, a sibling line; replaced with the SDS's 10 wt% calcium carbonate
- [colorfabb] LW-ASA: filament_density 1.07 - not printed in the LW-ASA TDS (its density row reads '140 g/cm3', apparently a misprint); 1.07 is the sibling ASA TDS value
- [colorfabb] rPLA: filament_diameter 1.75 - nominal diameter not printed on cited page colorfabb.com/rpla-semi-matte-black (only tolerance +/-0.10)
- [colorfabb] corkFill: filament_diameter 1.75 - nominal diameter not printed on cited page colorfabb.com/corkfill (only tolerance)
- [colorfabb] stoneFill: filament_diameter 1.75 - nominal diameter not printed on cited page colorfabb.com/stonefill-light-gray (only tolerance)
- [colorfabb] PLA Vertigo: filament_diameter 1.75 - nominal diameter not printed on cited page colorfabb.com/pla-vertigo-star-night (only tolerance)
- [colorfabb] PLA Chameleon: filament_diameter 1.75 - nominal diameter not printed on cited page colorfabb.com/pla-chameleon-nebula (only tolerance)
- [colorfabb] PETG Semi Matte: filament_diameter 1.75 - nominal diameter not printed on cited page colorfabb.com/petg-semi-matte-black (only tolerance)
- [colorfabb] rPETG: filament_diameter 1.75 - no diameter or tolerance printed on cited page colorfabb.com/rpetg-burnt-amber
- [colorfabb] PA-CF Low Warp: filament_diameter 1.75 - nominal diameter not printed on cited page colorfabb.com/pa-cf-low-warp (only tolerance)
- [formfutura] ABSpro: _drying "80C 5h" - not in the cited TDS (254657 is Formfutura's own ABSpro TDS, which prints 'Recommended, 50-60 C, 12 h'); replaced with the TDS value
- [formfutura] ABSpro: conflict 'Flashforge-branded TDS: nozzle 220-240C, bed 80-110C, density 1.08-1.1, HDT 85C at 0.455 MPa, speed 40-60 mm/s' - the cited TDS is Formfutura's own and prints none of these; removed. Added TDS-printed _print_speed 25-100 mm/s, _enclosure Yes, _hdt 85 (HDT A, ASTM D648), _vicat 93; source_quality changed to official_tds
- [formfutura] AquaSolve - PVA: conflict 'Flashforge-branded TDS: nozzle 210-230C, density 1.25-1.26, HDT 55C, fan 50-100%' - the cited TDS (256478) is Formfutura's own AquaSolve PVA TDS v2, which prints none of these; removed
- [formfutura] AquaSolve - PVA: nozzle_temperature_range_low/high 190/210 (product page) - replaced by the official TDS's 180-205C; the page's 190-210 moved to conflicts. Added _vicat 60.2 (ISO 306) from the TDS; source_quality changed to official_tds
- [formfutura] CarbonFil: _fiber_content '10% carbon fibre (product page)' - contradicted by the official TDS ('15% carbon fiber reinforced'); TDS value kept, page's 10% moved to conflicts

## Entries dropped by the source check

- [jayo] JAYO High Speed PLA: neither cited official page prints a diameter or any temperature in text (title, body and variant options checked). Its only field, filament_diameter 1.75, was unsourced, so the entry had no sourced values left.
- [kingroon] PLA Silk Tri-Color
- [kingroon] PLA Silk Single Color
- [kingroon] PLA Silk Rainbow
- [kingroon] PLA+
- [kingroon] HS-PLA
- [kingroon] PLA Chameleon
- [kingroon] Refill PLA
- [kingroon] PETG Basic
- [kingroon] PA Nylon
- [push-plastic] Push Plastic Matte ABS - its only source is the product page, which returned HTTP 429 on every try; the only value it had was diameter 1.75
- [push-plastic] Push Plastic TPU 100A - nozzle 230-250, bed 60-80, 100A hardness and 0.6mm nozzle advice all come only from the product page, which returned HTTP 429; the cited TPU 98A sheet and TDS describe a different hardness, so they don't support values for this line
- [geeetech] GEEETECH Carbon Fiber PLA - the only cited source is the generic material-guide section on wiki.geeetech.com. No GEEETECH product page exists for this line (the only listings found are on the 3djake reseller), so it has no sourced values for this product line.

## Still open after Research gap-fill runs R1-R5 (2026-11-02)

R1-R5 (brand groups as in `research/parallel-research-R2-R5.md`) added 92 lines and refreshed 66; they were imported
with `import_batch.py --merge`, so values a reply did not re-read were kept. What the replies could not fill:

### R1

- **Bambu PLA Lite:** no official Bambu-hosted TDS was found; search returned only the bigdipper.com.ar sheet and third-party databases. The existing values remain reseller-sourced.
- **Bambu PLA Silk Multi-Color:** the current product name was not confirmed this run.
- **Bambu PAHT-CF V3.0 values:** the wiki.bambulab.com V3.0 PDF returned a client error, so the check is still pending. V2.0 extras (HDT 170 °C at 1.8 MPa, fan 0-40%, chamber 45-60 °C, from a reseller copy) are recorded in `_notes` only.
- **Bambu PETG Matte and PPA-CF fan range:** neither TDS publishes one; both say only "Turn on".
- **Bambu store product pages and catalogue for all lines:** not systematically read. Diameter tolerance was captured only for PLA Basic Gradient, PETG Matte, PPA-CF and PAHT-CF. The discontinued status of ASA-CF and TPU 95A was not confirmed. PETG Matte is the only 2026 launch identified (dated 28 September 2026 by Bambu's own forum post).
- **Polymaker Fiberon PET-GF15:** Tg and Vicat are filled; HDT values conflict between sources and are listed in `conflicts`. The original TDS PDF could not be fetched.
- **Polymaker Matte PLA for Production HDT:** not reached.
- **eSUN HDT for PLA, PLA-Matte Dual, ASA+ and ePAHT-CF; PETG-Matte drying hours:** not reached.
- **eSUN lines not reached:** ePA-GF (only a 2017 news note giving a distortion temperature of 120 °C), PLA-UV Color Change (the parameter table did not load), PLA-Magic (density 1.21 only, too little for an entry). Not attempted: PLA CMYK, PLA-Clear Rainbow, Luminous PLA Rainbow, eClean, ePEEK Pro, PEEK-Industrial and PETG Refilament.
- **eSUN official_page upgrade for previously written entries:** esun3d.com is reachable now, but those entries were not re-imported this run.
- **Polymaker PC-PBT:** Polymaker's wiki says "PC-PBT is currently not being manufactured or sold and is discontinued."
- **eSUN ABS Odorless:** the official page says "This product has been discontinued and is out of stock." Its last published figures: density 1.04, HDT 73 °C, extruder 240-250 °C, bed 95-110 °C.
- **eSUN PET:** the official page says it is discontinued and points to PET-Basic.
- **Bambu PA-CF:** Bambu's store says "PA-CF was discontinued" and PAHT-CF is its upgrade.

### R2

- **SUNLU (all lines written) - drying hours, filament_max_volumetric_speed** - Still unpublished: SUNLU product pages/TDS give drying temperature only; store.sunlu.com dryer guide has no per-material time table in text (comparison table is an image); no SUNLU source publishes max volumetric speed. No SUNLU entries re-written since no new values were found.
- **OVERTURE Turbo PLA - colors** - Partly filled: only 'Plaster White' confirmed on an official Turbo PLA page; the main product URL redirects and the line appears renamed 'High Speed PLA' (unconfirmed). Amazon B07PGY2JP1 colour list recorded in _notes only.
- **JAYO High Speed PLA - nozzle temp, bed temp, density** - Not published in any text source (jayo3d.com page, JAYO Official Store Amazon B0DGSSGWVJ / B0DHRXQT74); possibly in images only.
- **JAYO ASA - nozzle, bed, density, HDT** - JAYO Official Store Amazon listing B0GMVGBLXB has no temps/density/HDT in bullets or technical details; only diameter and +/-0.02 tolerance (tolerance question resolved).
- **JAYO Easy PA (E-PA) / PA Nylon PA6+66 - density, drying, tolerance value** - Not published in the JAYO Official Store listing; temps/bed/HDT/speed were filled.
- **Creality Hyper PETG - density, HDT** - No official TDS reachable; not on official page or the Creality CL Store Amazon listing.
- **Creality Hyper PLA - nozzle/bed temp ranges, density** - Not in the Amazon bullets or store.creality.com page text (only K2 Plus single slicer values, kept in _notes). Conflict detail (seller, tolerance) resolved.
- **Prusament PETG Carbon Fiber - density, fan speed, max print speed, HDT 0.45/1.80 MPa** - Official TDS only as zip on prusament.com (blocked from sandbox, too large for WebFetch); no reseller TDS copy found. Reseller product page values noted in conflicts only.
- **Kingroon TPU 95A - retraction speed** - The only TPU TDS prints it truncated in the source itself ('10- 30mm/'); no other official source gives it.
- **Kingroon TPU 95A - hardness/TDS match** - TDS (filename ..._tpu_95a_...) is titled 'TPU 90A' with no Shore value; store page says 95A. Mismatch remains unresolved; entry written with this flagged.
- **Kingroon PA6-CF / PA-CF - drying, diameter tolerance, hardened nozzle, enclosure** - Only on Amazon B0DQPDTD2Z, whose seller (Hongshengqi) is not confirmed as Kingroon's official store; recorded in conflicts/_notes only.
- **Kingroon PLA Basic _nozzle_by_speed** - kingroon3d.com PLA Basic page (read 2026-11-02) shows only one nozzle range (190-210); speed-dependent ranges not found, so not confirmed.
- **Kingroon PLA Silk Dual-Color / PLA Glow / PLA Wood / ABS - product-page notes and colours** - Entries written from TDS; their product pages were not re-read this run (rate-limit budget), so page-derived notes and colour lists were not re-confirmed.
- **Inland PLA High Speed Silk** - microcenter.com returns 403 to WebFetch, so not attempted further; the line is not sold on Amazon by Micro Center (Amazon search found only Inland PLA+, PLA+ High Speed and PLA Basics) and no Inland TDS PDF exists
- **Inland PLA Dual Color Silk** - microcenter.com returns 403 to WebFetch, so not attempted further; the line is not sold on Amazon by Micro Center (Amazon search found only Inland PLA+, PLA+ High Speed and PLA Basics) and no Inland TDS PDF exists
- **Inland PLA+ Multi Color (CMYK set)** - microcenter.com returns 403 to WebFetch, so not attempted further; the line is not sold on Amazon by Micro Center (Amazon search found only Inland PLA+, PLA+ High Speed and PLA Basics) and no Inland TDS PDF exists; the plate 45-60 vs 45 conflict stays open (the single-colour PLA+ Amazon listing says bed 45-60, but the CMYK set listing itself was not read)
- **Inland ABS UV Luminous (glow)** - microcenter.com returns 403 to WebFetch, so not attempted further; the line is not sold on Amazon by Micro Center (Amazon search found only Inland PLA+, PLA+ High Speed and PLA Basics) and no Inland TDS PDF exists
- **Inland PETG-CF** - microcenter.com returns 403 to WebFetch, so not attempted further; the line is not sold on Amazon by Micro Center (Amazon search found only Inland PLA+, PLA+ High Speed and PLA Basics) and no Inland TDS PDF exists
- **Inland Silk PLA** - Amazon B09FW2HVJJ read: bullets give nozzle 190-230, bed 60-80, tolerance +/-0.05 in the bullet (title says +/-0.03), wax-sealed cardboard spool edge for AMS/CFS. Listing is currently unavailable with no seller shown, so it does not qualify as brand_amazon_listing; no entry written. Use these as verified conflict text for the existing entry.
- **Inland (all lines) - density, drying, Tg/HDT, max volumetric speed** - Not published in any Inland source reached (Micro Center Amazon listings for PLA+, PLA+ High Speed, PLA Basics carry none; no Inland TDS found). Only filled for Fiberon ASA-CF08, from Polymaker's TDS.
- **Inland Amazon listings (brand listing route) - other lines** - B00YSZ1MFU (Translucent PETG) is unavailable with no bullets. Inland PLA Basics (B0F2GNJ7WJ, sold by Micro Center) gives +/-0.02 and spool size but no temperatures. Other Inland lines are not on Amazon.
- **Inland (all 19 lines) - live-page check** - microcenter.com returns 403 to WebFetch, so not attempted further; the line is not sold on Amazon by Micro Center (Amazon search found only Inland PLA+, PLA+ High Speed and PLA Basics) and no Inland TDS PDF exists; kept values could not be re-checked against the live page
- **Hatchbox (all lines) - bed temps, density, drying, HDT** - Hatchbox FAQ says no technical data is available for their filaments; product pages give only print temperature, +/-0.03, and 'no heated bed required' for PLA/PETG/TPU.
- **Hatchbox PLA/PETG/ABS material (info) pages** - Not reached: hatchbox3d.com HTML pages and collection .atom feeds returned client errors/rate limits; only product .js endpoints were readable.
- **Anycubic TPU 68D** - drying temp/time, HDT, Vicat, max volumetric speed, diameter tolerance not published (page fields blank)
- **Anycubic PVA** - max volumetric speed and HDT printed as '/'; diameter tolerance not published
- **Anycubic PET-CF** - diameter tolerance not published
- **Anycubic PLA Silk Dual/Tri-Color** - diameter tolerance not published; diameter only via FAQ compatibility statement
- **All 8 Anycubic lines** - TDS PDFs not obtainable: page download buttons expose no URLs to WebFetch; values come from official product-page spec tables instead

### R3

- **Push Plastic High Heat+Tough PLA:** the annealing conflict note was not found. Only other brands' annealing guidance turned up (e.g. 3D-Fuel Tough Pro PLA+ at 110-120 °C), and I did not borrow it.
- **Push Plastic (all 14 lines):** I did not get a complete colour list per line. Confirmed colours: Nylon Black/Natural/White; CF lines Black.
- **Push Plastic Carbon Fiber PETG:** nozzle and bed are unconfirmed because the block label was not visible (see the entry).
- **Atomic FR15U:** I have resin data only. The filament-level HDT has not been published.
- **Fiberlogy:** official diameter tolerance and ovality are not published on brand pages (only reseller copies, ±0.02/+0.01). The ASA+AF aramid percentage is not published. max_volumetric_speed is not published. Tg for ABS, ASA, PA, PCTG, CPE and PP lines is not on the pages (they give Vicat/HDT). I did not attempt the image-only TDS PDFs.
- **Extrudr (DuraPro ASA Matte; diameter and drying for all 26 lines):** not reached (budget).
- **Spectrum (diameter and tolerance for all lines; HDT rows; PLA Premium shop check):** not reached (budget).
- **QIDI Tech (PLA Rapido Metal, PLA Wood, ABS Rapido Metal, PLA Silk, PLA Rapido, ABS Rapido):** not reached (budget).
- **Flashforge PETG-CF page HDT (reported 74 °C):** not read. Note that 74 °C is also the HDT in the original PETG TDS, so it may be a carry-over.
- **Flashforge "other possible lines" (glow, wood, marble, galaxy, etc.):** not attempted. The flashforge.com menu does show additional lines: PLA Multicolor (Burnt Titanium), HS PETG Metallic, ASA-CF, PET-CF and PET-GF.
- **Flashforge PLA/PLA Pro/Matte/Silk/PLA-CF/PETG/PETG-CF/ABS/ABS Pro/TPU/PC/PVA:** single-value density, colours, and confirmation that PC/PVA are still sold were not reached.
- **GEEETECH Carbon Fiber PLA; Matte PLA/PLA+/PETG/PETG Metal/ABS+/ASA/Luminous/Marble; Silk Dual/Tri-Color:** not reached.
- **SOVOL TPU and PLA Matte Rainbow:** temperatures are not published as text by Sovol (image-only on sovol.tech).
- None confirmed. The Fiberlogy S1-spool ABS SKU is marked "LAST ITEMS! … old-style spool… not compatible with the BambuLab AMS". Only that spool format is ending; the ABS line continues on S2/S3 spools, which Fiberlogy says are AMS-compatible.

### R4

- **CarbonX PEI 1010+CF:** density and HDT are not in any source read this run. The official TDS (CarbonX_CF_Ultem_TDS_v3.pdf) is on the hub, but it could not be fetched.
- **ThermaX PEI 9085:** density and HDT not retrieved (THERMAX_PEI_9085_TDS_v4.pdf not read). The only official value found is drying, 130C 4-6h.
- **Firewire FR-PC/ABS:** density, Tg and HDT not retrieved. The only official value found is drying, 80C 6h.
- **3DXTech PC/ASA:** no print or thermal values retrieved. An older official drying page gives a 110C max for 4h.
- **HyperLite PP, EVOLV3D OBC, FibreX PP GF30, ThermaX TPI (EXTEM), ThermaX PEKK-C:** the TDS PDFs are listed on the official hub but could not be read. The only densities found were secondary and unverified: HyperLite PP 0.81, FibreX PP+GF30 1.12, TPI 1.3.
- **CarbonX PEKK-A CF15:** only secondary data. A GitHub PR reports nozzle 360-390C, bed 120-140C and density 1.33. All3DP gives Tg 160 and HDT 150. The official drying value is 120C 6-8h.
- **ThermaX PEEK GF20 (FibreX PEEK+GF20):** the official page gives hardened steel with a 0.4mm minimum nozzle and drying 130C 4h. The drying table says 150C 3h. Nozzle/bed (375-410 / 130-145) and density 1.44 are secondary only.
- **ECOMAX PLA:** 3DXTech still has a live "ECOMAX® TOUGH PLA" product page (3dxtech.com/products/ecomax-r-tough-pla; SKU PLA04UN100750GY02; black, dark grey and white; 750 g; "Bambu AMS compatible"; "Ideal for printing without a heated bed, no enclosure required"), which confirms the ECOMAX → Tough PLA mapping. Its print temperatures were not retrieved, so no entry was written; the drying table lists "Tough PLA" at 65C 4h. 3DXTech also sells a separate "Economy PLA" (190-220C nozzle, 23-60C bed, drying 45C 4h).
- **Value-only gaps that remain:** ThermaX PEEK tolerance; ESD-PLA tolerance; Obsidian PA6+CF Tg and tolerance; HTS1 bed range beyond "up to 160C" and tolerance; ESD-PEI Tg/HDT; ESD-TPU density; ESD-ABS official nozzle/bed (not verified this run).
- AmideX PA6-GF30 is now FibreX Nylon 6+GF30. Its entry is written under the legacy name.
- AmideX PA6 Copolymer is now AmideX Nylon 6-66. Its entry is written under the legacy name, and the mapping is inferred.
- Obsidian PA6+CF is now Obsidian Nylon 6+CF V2, a reformulation. The entry uses V2 data.
- ECOMAX PLA is still listed as ECOMAX® Tough PLA (confirmed on the official product page). No entry was written because its print temperatures were not retrieved.

### R5

- **Kexcelled K8 PP:** listed in Kexcelled's Functional collection, but no product page, TDS or reseller values were found. Do not confuse it with K8 OBC (210–250 °C, density 0.90–0.92).
- **Kexcelled K8 TPU Matte:** no published values. Kexcelled's news post "Kexcelled Announces Groundbreaking Material Launches at Formnext 2025" names it "THE K8™ TPU 95A Matte", built on its "proven 95A formulation", not 90A.
- **Kexcelled K5 PETG ESD:** Kexcelled sells it as K6 PETG ESD; no published values found.
- **Kexcelled K5 ABS Pro:** no product by this name exists in Kexcelled's listings; the item may mean plain K5 ABS. Not filled pending clarification.
- **Kexcelled catalogue / product pages:** kexcelled3d.com pages are now reachable through search results (e.g., K9 PC FR: density 1.18–1.20, spool heat-resistant to 70 °C, White/Black). A full colour/AMS refresh was not done.
- **Kexcelled K5 PLA Magic / Color Change / Gradient / Streams / Coffee / Tea; K5 ABS Color Change; K9 PEBA; K6 UCM 300; soft TPU 60A–80A; K11/K12 PEEK, PEEK PRO, PEEK CF10, PEEK GF10, PEEK Ultra, PEKK, PPSU, PEI 1010, PEI 9085:** not reached (budget).
- **Formfutura EasyFil PLA, ReForm Organic rPLA, AthenaX GF10, BioFil PCL, COMPOST3D 2, all LUVOCOM 3F grades (PAHT 9936/9825/CF 9891/CF 9742/KK 50056 FR, PP CF 9928, PPS CF 9938, PEKK 50082, PEEK 9581, PEEK CF 9676, PEI 50236, PEI ULTEM 1010/9085, PPSU):** not reached (budget). For AthenaX GF10, only third-party values were seen (250–290 °C / 85–100 °C), not used.
- **Amazon Basics PLA (both lines):** not filled; no first-party temperature, density or tolerance source was reachable.
- **Discontinued (likely):** ColorFabb HT. The category returns 404 and HT Clear has no product page; the TDS remains in the download folder.
