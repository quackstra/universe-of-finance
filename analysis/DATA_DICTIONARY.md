---
title: "Data Dictionary"
layout: default
nav_order: 5
---

# Universe of Finance — Data Dictionary

> Formal schema documentation for all `data.json` files in the analysis directory.
> Last updated: 2026-03-29.

---

## 1. Overview

Every category in the Universe of Finance taxonomy has a structured `data.json`
file containing transaction throughput measurements, historical data, projections,
source citations, and confidence scores. These files are the single source of
truth for all downstream outputs: the Big Number calculation, confidence
scorecards, time-series charts, executive summaries, and the MEST Advantage
analysis.

### File Organization

```
analysis/
  <sector>/
    <category-slug>/
      data.json          # Category schema (29 files)
      workings/          # Optional: methodology docs, models, raw data
  deep-dives/
    <country-or-region>/
      data.json          # Deep Dive schema (7+ files)
```

There are two distinct schemas:

1. **Category data.json** — One per transaction category (e.g., `consumer-cards`,
   `equity-markets`). Measures global throughput for that category.
2. **Deep Dive data.json** — One per country or region (e.g., `brazil`, `japan`).
   Breaks down a country's contribution across multiple categories.

### How to Use

- **Read a single category:** Parse `analysis/<sector>/<slug>/data.json` and
  access `current.avg_tps.value` for the headline TPS figure.
- **Aggregate globally:** Use `tools/big_number.py` which loads all category
  files, applies overlap deductions, and computes the de-duplicated global TPS.
- **Validate schema:** Run `tools/validate_schema.py` to check all files against
  the required schema.
- **Score confidence:** Run `tools/confidence_score.py` to apply the rubric and
  write scores into each `data.json`.

---

## 2. Category data.json — Schema Reference

The category schema captures global throughput for a single transaction type.

### Top-Level Fields

| Field | Type | Required | Description | Example | Constraints |
|-------|------|----------|-------------|---------|-------------|
| `category` | string | Yes | Human-readable category name | `"Consumer Card Payments"` | Free text |
| `slug` | string | Yes | URL-safe identifier | `"consumer-cards"` | Must match parent directory name; must be in `ALL_SLUGS` set |
| `sector` | string | Yes | Parent sector grouping | `"Payments"` | One of 7 valid sectors (see Section 4) |
| `last_updated` | string | Yes | Date of last data revision | `"2026-03-26"` | Format: `YYYY-MM-DD`, exactly 10 characters |
| `current` | object | Yes | Current-period metrics | See below | Must contain all 5 required metric keys |
| `historic` | array | Yes | Year-by-year historical data | See below | Array of objects; may be empty |
| `projections` | object | Yes | Forward-looking scenarios | See below | Must contain 3 scenario keys |
| `overlap` | object | Yes | Cross-category overlap metadata | See below | Must contain 3 required keys |
| `sources` | array | Yes | Cited references | See below | Non-empty array of source objects |
| `confidence` | object | No | Confidence scoring breakdown | See below | Written by `confidence_score.py` |

### `current` Object

Contains 5 required metric objects, each following the Metric schema.

| Metric Key | Description |
|------------|-------------|
| `avg_tps` | Average transactions per second (annual volume / 31,536,000) |
| `peak_tps` | Estimated peak TPS during high-activity periods |
| `daily_volume` | Average daily transaction count |
| `annual_volume` | Total annual transaction count |
| `annual_value_usd` | Total annual transaction value in USD |

Some categories include additional metrics beyond the required five:

| Optional Metric Key | Used By | Description |
|---------------------|---------|-------------|
| `wash_adjusted` | `cex` | Wash-trading adjustment model with regional breakdown |
| `avg_tps_installment` | `bnpl` | Installment-level TPS (used by `big_number.py`) |
| `annual_volume_installments` | `bnpl` | Annual installment count |

### Metric Object Schema

Each metric in `current` follows this structure:

| Field | Type | Required | Description | Example | Constraints |
|-------|------|----------|-------------|---------|-------------|
| `value` | number or null | Yes | The measured/estimated value | `24501` | Must be number or `null` |
| `source` | string | Yes | Description of how value was derived | `"Nilson Report — Global Network Card Results 2024"` | Free text; may be empty string |
| `url` | string | Yes | URL to source document | `"https://nilsonreport.com/..."` | May be empty string if no URL available |
| `confidence` | string | Yes | Confidence level for this specific metric | `"high"` | One of: `high`, `medium-high`, `medium`, `low-medium`, `low` |
| `note` | string | No | Additional context or caveats | `"Includes purchase volume and cash advances"` | Free text |

### `historic` Array

Array of year-over-year historical data points.

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `year` | integer | Yes | Calendar year | `2024` |
| `annual_volume` | number or null | Yes | Annual transaction count for that year | `772730000000` |
| `avg_tps` | number or null | Yes | Average TPS for that year | `24501` |
| `source` | string | Yes | Source citation | `"Nilson Report"` |
| `confidence` | string | Yes | Confidence for this data point | `"high"` |

Values may be `null` when transaction counts are unavailable (common for
categories where only market value, not transaction count, is published).

### `projections` Object

Contains three scenario arrays, each with projected future data points.

| Scenario Key | Description |
|--------------|-------------|
| `baseline` | Central estimate using moderate growth assumptions |
| `high_growth` | Optimistic scenario with accelerated adoption/growth |
| `conservative` | Pessimistic scenario with slower growth or saturation |

Each scenario is an array of projection objects:

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `year` | integer | Yes | Projected year | `2030` |
| `tps` | number or null | Yes | Projected average TPS | `39239` |
| `annual_volume` | number or null | Yes | Projected annual transaction count | `1238000000000` |

Projection arrays vary in granularity: some have yearly entries, others have
5-year intervals (e.g., 2025, 2030, 2035). Values may be `null` for categories
where projections have not yet been computed.

### `overlap` Object

Documents relationships between categories to enable de-duplication.

| Field | Type | Required | Description | Example | Constraints |
|-------|------|----------|-------------|---------|-------------|
| `overlaps_with` | array of strings | Yes | Slugs of overlapping categories | `["digital-wallets"]` | Each element must be a valid slug; empty array if no overlap |
| `overlap_type` | string | Yes | Nature of the overlap | `"partial"` | One of: `none`, `partial`, `full_subset`, `high`, `complete`, `subset` |
| `overlap_note` | string | Yes | Explanation of the overlap | `"Card-rail transactions processed via digital wallets"` | Free text; may be empty string |

### `sources` Array

Cited references used to build the data. Non-empty; typically 5-20 sources.

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `id` | integer | Yes | Sequential identifier within this file | `1` |
| `citation` | string | Yes | Human-readable citation text | `"Nilson Report — Global Network Card Results 2024"` |
| `url` | string | Yes | URL to the source | `"https://nilsonreport.com/..."` |
| `accessed` | string | Yes | Date the source was accessed | `"2026-03-26"` |

### `confidence` Object

Written by `tools/confidence_score.py`. Provides a 0-100 composite score.

| Field | Type | Description | Range |
|-------|------|-------------|-------|
| `score` | integer | Composite confidence score | 0-100 |
| `source_quality` | integer | Quality of primary data sources | 0-30 |
| `data_recency` | integer | How current the data is | 0-20 |
| `triangulation` | integer | Number of independent methods/sources used | 0-25 |
| `coverage` | integer | Market coverage completeness | 0-25 |
| `notes` | string | Qualitative assessment of data reliability | Free text |

### Category-Specific Extensions

Some categories have additional top-level objects beyond the base schema:

| Object | Used By | Description |
|--------|---------|-------------|
| `network_breakdown` | `consumer-cards` | Per-network transaction breakdown (Visa, Mastercard, etc.) with `global_networks`, `domestic_networks`, and reconciliation data |
| `exchange_breakdown` | `equity-markets` | Per-exchange trade volume breakdown with `tier1_exchanges`, `tier2_sum_billions`, and `regional_summary` |
| `wash_adjusted` (in `current`) | `cex` | Regional wash-trading model with per-region volume shares, wash percentages, and tier cross-check |

These extensions are not validated by `validate_schema.py` but are consumed
by analysis tools and reports.

---

## 3. Deep Dive data.json — Schema Reference

Deep Dive files break down a single country's or region's transaction throughput
across all relevant categories. The schema is fundamentally different from
category files.

### Top-Level Fields

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| `country` | string | Yes | Country or region name | `"Brazil"` |
| `iso_code` | string | Yes | ISO 3166-1 alpha-2 code | `"BR"` |
| `population` | integer | Yes | Population estimate | `213000000` |
| `gdp_usd_trillion` | number | Yes | GDP in trillions of USD | `2.2` |
| `last_updated` | string | Yes | Date of last revision | `"2026-03-29"` |
| `total_tps_contribution` | number | Yes | De-duplicated TPS contribution | `4680` |
| `share_of_global_tps` | string | Yes | Percentage of global total | `"6.3%"` |
| `global_tps_reference` | number | Yes | Global TPS denominator used | `73750` |
| `categories` | object | Yes | Per-category breakdown | See below |
| `de_duplicated_<country>_tps` | object | Yes | De-duplication methodology | See below |
| `key_metrics` | object | Yes | Country-specific headline stats | See below |
| `confidence` | object | Yes | Confidence scoring | Same schema as category confidence |

### `categories` Object

Keys are category slugs. Each value is a category contribution object:

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `<country>_tps` | number | Country's TPS contribution to this category | `2179` |
| `<country>_annual_txns_billions` | number | Annual transactions in billions | `68.7` |
| `share_of_category` | string | This country's share of the global category | `"11.1%"` |
| `share_of_<country>_total` | string | This category's share of the country's total | `"46.6%"` |
| `key_systems` | array of strings | Major payment systems/platforms | `["Pix", "TED", "Boleto"]` |
| `notes` | string | Detailed analytical notes | Free text |
| `sources` | array of objects | Per-category source citations | `[{"citation": "...", "url": "..."}]` |

Note: The field name prefix varies by country (e.g., `brazil_tps`, `japan_tps`,
`india_tps`). This is a country-specific naming convention, not a fixed field name.

### `de_duplicated_<country>_tps` Object

| Field | Type | Description |
|-------|------|-------------|
| `value` | number | De-duplicated TPS after overlap removal |
| `methodology` | string | Detailed description of de-duplication steps |
| `range_low` | number | Lower bound of estimate range |
| `range_high` | number | Upper bound of estimate range |
| `notes` | string | Uncertainty assessment |

### `key_metrics` Object

Country-specific headline statistics. Fields vary by country. Examples:

- Brazil: `pix_txns_per_capita_2024`, `pix_active_users_millions`, `drex_status`
- Japan: `cashless_ratio_2024_pct`, `paypay_users_millions`, `digital_yen_status`
- India: `upi_txns_per_capita`, `jan_dhan_accounts_millions`

### Deep Dive Source Citations (Inline)

Deep dive `sources` within each category use a simplified format:

| Field | Type | Description |
|-------|------|-------------|
| `citation` | string | Short citation text |
| `url` | string | URL to source |

These lack the `id` and `accessed` fields present in category-level sources.

---

## 4. Enums and Controlled Vocabularies

### Valid Sectors (7)

| Sector | Directory Name | Category Count |
|--------|---------------|----------------|
| Payments | `payments/` | 11 |
| Traditional Finance | `traditional-finance/` | 6 |
| Digital Assets | `digital-assets/` | 4 |
| Banking | `banking/` | 2 |
| Gaming | `gaming/` | 2 |
| Government | `government/` | 1 |
| Emerging | `emerging/` | 3 |

### Valid Category Slugs (29)

Defined in `validate_schema.py` as `ALL_SLUGS`:

**Payments:** `consumer-cards`, `digital-wallets`, `bank-transfers`, `ecommerce`,
`p2p-transfers`, `remittances`, `insurance-premiums`, `bnpl`, `bill-payments`,
`payroll`, `atm-withdrawals`

**Traditional Finance:** `equity-markets`, `etd`, `forex`, `fixed-income`,
`commodities`, `otc-derivatives`

**Digital Assets:** `cex`, `blockchain-l1-l2`, `defi`, `stablecoins`

**Banking:** `interbank-rtgs`, `securities-settlement`

**Gaming:** `gaming-microtx`, `gaming-sales`

**Government:** `government-payments`

**Emerging:** `rwa-tokenisation`, `iot-m2m`, `ai-agents`

### Confidence Levels (Per-Metric)

Used in `current.<metric>.confidence` and `historic[].confidence`:

| Value | Meaning |
|-------|---------|
| `high` | Primary source data with direct measurement |
| `medium-high` | Strong secondary sources with cross-validation |
| `medium` | Industry reports or derived from reliable proxies |
| `low-medium` | Triangulated from partial data across multiple segments |
| `low` | Estimates, extrapolations, or single-source data |

### Confidence Score Bands (Composite)

Used in `confidence.score` (0-100 composite):

| Score Range | Band | Meaning |
|-------------|------|---------|
| 80-100 | High | Primary/regulatory data, recent, well-triangulated, high coverage |
| 60-79 | Medium-High | Good data with some gaps or estimation |
| 40-59 | Medium | Mix of measured and estimated data |
| 20-39 | Low-Medium | Primarily estimated with limited primary sources |
| 0-19 | Low | Pre-market or entirely estimated |

### Confidence Rubric Sub-Scores

| Dimension | Max | 75%+ | 50-74% | 25-49% | <25% |
|-----------|-----|------|--------|--------|------|
| Source Quality | 30 | Primary/regulatory (25-30) | Industry reports (15-24) | Extrapolations (5-14) | Pure estimates (0-4) |
| Data Recency | 20 | <1 year old (16-20) | 1-2 years (10-15) | 2-3 years (5-9) | >3 years (0-4) |
| Triangulation | 25 | 3+ methods (20-25) | 2 methods (10-19) | 1 method (0-9) | — |
| Coverage | 25 | >90% market (20-25) | 50-90% (10-19) | <50% (0-9) | — |

### Overlap Types

| Value | Meaning |
|-------|---------|
| `none` | No overlap with other categories |
| `partial` | Some transactions counted in another category |
| `full_subset` | All transactions are a subset of another category |
| `high` | Most transactions overlap with other categories |
| `complete` | Category is entirely contained within another |
| `subset` | Synonym for `full_subset` |

### Deep Dive Countries/Regions (7+)

| Slug | Entity | ISO Code |
|------|--------|----------|
| `usa` | United States | US |
| `china` | China | CN |
| `india` | India | IN |
| `brazil` | Brazil | BR |
| `eu` | European Union | EU |
| `japan` | Japan | JP |
| `uk` | United Kingdom | GB |
| `africa` | Africa (continent) | — |

---

## 5. Cross-References

### Overlap Network

Categories reference each other through the `overlap` object. The `big_number.py`
tool applies deduction rules to avoid double-counting. Key overlap relationships:

| Category | Overlaps With | Deduction Applied |
|----------|--------------|-------------------|
| `digital-wallets` | `bank-transfers`, `consumer-cards` | Flat: -172B (UPI in bank-transfers) -40B (card-rail overlay) |
| `ecommerce` | `consumer-cards`, `digital-wallets`, `bank-transfers` | -95% (settles on existing rails) |
| `defi` | `blockchain-l1-l2` | Excluded (full subset of L1/L2) |
| `stablecoins` | `blockchain-l1-l2` | Excluded (full subset of L1/L2) |
| `rwa-tokenisation` | `blockchain-l1-l2` | Excluded (full subset of L1/L2) |
| `ai-agents` | `blockchain-l1-l2` | Excluded (full subset of L1/L2) |
| `government-payments` | `bank-transfers` | -60% (flows via ACH/bank transfers) |
| `iot-m2m` | `consumer-cards`, `bank-transfers` | -75% (settles on existing rails) |
| `gaming-microtx` | `consumer-cards`, `digital-wallets` | Incremental: 70 TPS only |
| `gaming-sales` | `consumer-cards`, `digital-wallets` | Incremental: 18 TPS only |
| `bill-payments` | `bank-transfers`, `consumer-cards` | -90% (direct debit/card-on-file) |
| `payroll` | `bank-transfers` | -90% (ACH/BACS/SEPA batch) |
| `insurance-premiums` | `consumer-cards`, `bank-transfers` | -90% (card/direct debit) |
| `bnpl` | `consumer-cards` | Incremental: 460 TPS (3.6x multiplier creates net new installment events) |
| `atm-withdrawals` | (none) | 0% (unique cash-out events) |

### Sector Groupings

Each sector groups related categories. The sector name in `data.json` must match
one of the 7 valid sectors. The `big_number.py` tool aggregates TPS by sector
before computing the global total.

### Deep Dive to Category Mapping

Each deep dive's `categories` object keys are category slugs that reference the
corresponding global category `data.json`. The `share_of_category` field in a
deep dive indicates what percentage of the global category is attributed to
that country.

---

## 6. Tooling

### `validate_schema.py`

**Purpose:** Validates all category `data.json` files against the required schema.

**Usage:**
```bash
cd /home/quackstra/wt-run11
python3 tools/validate_schema.py
```

**What it checks:**
- All 9 required top-level keys are present
- `slug` matches the parent directory name
- `last_updated` is valid `YYYY-MM-DD` format
- All 5 required `current` metrics exist and are well-formed
- Each metric has `value`, `source`, `url`, `confidence`
- Confidence values are in the valid enum set
- `value` is numeric or `null`
- `historic` entries have `year`, `annual_volume`, `avg_tps`, `source`, `confidence`
- `projections` has all 3 scenarios (`baseline`, `high_growth`, `conservative`)
- Each projection entry has a `year` field
- `overlap` has all 3 required keys; `overlap_type` is valid
- `sources` is non-empty; each source has `id`, `citation`, `url`, `accessed`

**Exit code:** 0 if all pass, 1 if any errors found.

**Note:** Deep Dive files use a different schema and are not validated by this
tool. The validator only processes files in `<sector>/<category>/data.json` paths.

### `big_number.py`

**Purpose:** Computes the de-duplicated global financial TPS ("the Big Number").

**Usage:**
```bash
python3 tools/big_number.py              # De-duplicated table (default)
python3 tools/big_number.py --raw        # Raw sums without deduplication
python3 tools/big_number.py --json       # JSON output for programmatic use
python3 tools/big_number.py --sensitivity # Sensitivity analysis
```

**How it works:**
1. Loads all category `data.json` files
2. Extracts `current.avg_tps.value` and `current.annual_volume.value`
3. Applies per-category TPS overrides (forex, fixed-income revised estimates)
4. Applies overlap deduction rules (see Section 5)
5. Aggregates by sector and computes global totals
6. Outputs a formatted table with raw vs. de-duplicated comparison

**Deduction types:**
- `exclude` — Category fully excluded from TPS sum
- `pct` — Reduce TPS/volume by a percentage
- `flat_vol` — Subtract a flat transaction count
- `incremental_tps` — Use a fixed incremental TPS instead of the raw value

### `confidence_score.py`

**Purpose:** Applies the confidence rubric to all categories and writes scores.

**Usage:**
```bash
python3 tools/confidence_score.py            # Score and update all files
python3 tools/confidence_score.py --dry-run  # Preview without writing
```

**How it works:**
1. Loads all `data.json` files from the analysis directory
2. Looks up hand-scored confidence values from an internal `SCORES` dictionary
3. Computes composite score: `source_quality + data_recency + triangulation + coverage`
4. Writes the `confidence` object back into each `data.json`
5. Generates `analysis/CONFIDENCE_SCORECARD.md` with a ranked table

---

## 7. JSON Schema (Category data.json)

A formal JSON Schema for programmatic validation of category `data.json` files:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "universe-of-finance-category-data",
  "title": "Universe of Finance — Category data.json",
  "type": "object",
  "required": [
    "category", "slug", "sector", "last_updated",
    "current", "historic", "projections", "overlap", "sources"
  ],
  "properties": {
    "category": {
      "type": "string",
      "description": "Human-readable category name"
    },
    "slug": {
      "type": "string",
      "description": "URL-safe identifier matching parent directory",
      "enum": [
        "consumer-cards", "digital-wallets", "bank-transfers", "ecommerce",
        "p2p-transfers", "remittances", "insurance-premiums", "bnpl",
        "bill-payments", "payroll", "atm-withdrawals", "equity-markets",
        "etd", "forex", "fixed-income", "commodities", "otc-derivatives",
        "cex", "blockchain-l1-l2", "defi", "stablecoins", "interbank-rtgs",
        "securities-settlement", "gaming-microtx", "gaming-sales",
        "government-payments", "rwa-tokenisation", "iot-m2m", "ai-agents"
      ]
    },
    "sector": {
      "type": "string",
      "enum": [
        "Payments", "Traditional Finance", "Digital Assets",
        "Banking", "Gaming", "Government", "Emerging"
      ]
    },
    "last_updated": {
      "type": "string",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}$",
      "description": "ISO 8601 date (YYYY-MM-DD)"
    },
    "current": {
      "type": "object",
      "required": ["avg_tps", "peak_tps", "daily_volume", "annual_volume", "annual_value_usd"],
      "properties": {
        "avg_tps": { "$ref": "#/$defs/metric" },
        "peak_tps": { "$ref": "#/$defs/metric" },
        "daily_volume": { "$ref": "#/$defs/metric" },
        "annual_volume": { "$ref": "#/$defs/metric" },
        "annual_value_usd": { "$ref": "#/$defs/metric" }
      },
      "additionalProperties": true
    },
    "historic": {
      "type": "array",
      "items": { "$ref": "#/$defs/historicEntry" }
    },
    "projections": {
      "type": "object",
      "required": ["baseline", "high_growth", "conservative"],
      "properties": {
        "baseline": { "type": "array", "items": { "$ref": "#/$defs/projectionEntry" } },
        "high_growth": { "type": "array", "items": { "$ref": "#/$defs/projectionEntry" } },
        "conservative": { "type": "array", "items": { "$ref": "#/$defs/projectionEntry" } }
      }
    },
    "overlap": {
      "type": "object",
      "required": ["overlaps_with", "overlap_type", "overlap_note"],
      "properties": {
        "overlaps_with": {
          "type": "array",
          "items": { "type": "string" }
        },
        "overlap_type": {
          "type": "string",
          "enum": ["none", "partial", "full_subset", "high", "complete", "subset"]
        },
        "overlap_note": { "type": "string" }
      }
    },
    "sources": {
      "type": "array",
      "minItems": 1,
      "items": { "$ref": "#/$defs/sourceEntry" }
    },
    "confidence": { "$ref": "#/$defs/confidenceBlock" }
  },
  "$defs": {
    "metric": {
      "type": "object",
      "required": ["value", "source", "url", "confidence"],
      "properties": {
        "value": {
          "oneOf": [
            { "type": "number" },
            { "type": "null" }
          ]
        },
        "source": { "type": "string" },
        "url": { "type": "string" },
        "confidence": {
          "type": "string",
          "enum": ["high", "medium-high", "medium", "low-medium", "low"]
        },
        "note": { "type": "string" }
      }
    },
    "historicEntry": {
      "type": "object",
      "required": ["year", "annual_volume", "avg_tps", "source", "confidence"],
      "properties": {
        "year": { "type": "integer" },
        "annual_volume": {
          "oneOf": [{ "type": "number" }, { "type": "null" }]
        },
        "avg_tps": {
          "oneOf": [{ "type": "number" }, { "type": "null" }]
        },
        "source": { "type": "string" },
        "confidence": { "type": "string" }
      }
    },
    "projectionEntry": {
      "type": "object",
      "required": ["year"],
      "properties": {
        "year": { "type": "integer" },
        "tps": {
          "oneOf": [{ "type": "number" }, { "type": "null" }]
        },
        "annual_volume": {
          "oneOf": [{ "type": "number" }, { "type": "null" }]
        }
      }
    },
    "sourceEntry": {
      "type": "object",
      "required": ["id", "citation", "url", "accessed"],
      "properties": {
        "id": { "type": "integer" },
        "citation": { "type": "string" },
        "url": { "type": "string", "format": "uri" },
        "accessed": {
          "type": "string",
          "pattern": "^\\d{4}-\\d{2}-\\d{2}$"
        }
      }
    },
    "confidenceBlock": {
      "type": "object",
      "properties": {
        "score": { "type": "integer", "minimum": 0, "maximum": 100 },
        "source_quality": { "type": "integer", "minimum": 0, "maximum": 30 },
        "data_recency": { "type": "integer", "minimum": 0, "maximum": 20 },
        "triangulation": { "type": "integer", "minimum": 0, "maximum": 25 },
        "coverage": { "type": "integer", "minimum": 0, "maximum": 25 },
        "notes": { "type": "string" }
      }
    }
  }
}
```

---

## 8. Changelog — Schema Evolution

### Run 1-4 (Initial)
- Established base category schema with `category`, `slug`, `sector`,
  `last_updated`, `current`, `historic`, `projections`, `overlap`, `sources`.
- Initial 24 categories across 7 sectors.

### Run 5
- Added 5 new payment categories: `insurance-premiums`, `bnpl`, `bill-payments`,
  `payroll`, `atm-withdrawals`. Total categories: 29.
- Added `REVISED_TPS_OVERRIDES` in `big_number.py` for `forex` and `fixed-income`.
- Added new deduction types: `incremental_tps` for gaming and BNPL categories.
- Added `avg_tps_installment` and `annual_volume_installments` optional fields
  in BNPL `current` object.

### Run 6
- Added overlap deductions for the 5 new Run 5 categories in `big_number.py`.
- Refined `VALID_OVERLAP_TYPES` to include `high`, `complete`, `subset`.

### Run 7-8
- Introduced Deep Dive schema (USA first, then China, India).
- Deep Dives use country-specific field naming (e.g., `usa_tps`, `india_tps`).
- Added `de_duplicated_<country>_tps` object with `range_low`/`range_high`.
- Added `key_metrics` object for country-specific headline statistics.

### Run 9
- Added `confidence` object to all category files via `confidence_score.py`.
- Introduced 4-dimension scoring rubric (source_quality, data_recency,
  triangulation, coverage).
- Added Brazil and EU deep dives.

### Run 10
- Added Japan and UK deep dives.
- Confidence uplift for AI Agents, Microtransactions, Bill Payments.
- Added `wash_adjusted` with regional breakdown model to CEX `current` object.
- Added `network_breakdown` to `consumer-cards` with global/domestic networks.
- Added `exchange_breakdown` to `equity-markets` with per-exchange data.
