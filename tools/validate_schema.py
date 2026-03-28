#!/usr/bin/env python3
"""Universe of Finance — Schema Validator

Reads all 29 data.json files and validates against the target schema.
Exits 0 if all pass, 1 if any fail.
"""

import json
import sys
from pathlib import Path

ANALYSIS_ROOT = Path(__file__).resolve().parent.parent / "analysis"

REQUIRED_TOP_KEYS = ["category", "slug", "sector", "last_updated", "current", "historic", "projections", "overlap", "sources"]
REQUIRED_CURRENT_KEYS = ["avg_tps", "peak_tps", "daily_volume", "annual_volume", "annual_value_usd"]
REQUIRED_METRIC_KEYS = ["value", "source", "url", "confidence"]
VALID_CONFIDENCE = {"high", "medium", "low", "low-medium", "medium-high"}
VALID_OVERLAP_TYPES = {"none", "partial", "full_subset", "high", "complete", "subset"}
REQUIRED_OVERLAP_KEYS = ["overlaps_with", "overlap_type", "overlap_note"]
PROJECTION_SCENARIOS = ["baseline", "high_growth", "conservative"]
REQUIRED_SOURCE_KEYS = ["id", "citation", "url", "accessed"]

ALL_SLUGS = {
    "consumer-cards", "digital-wallets", "bank-transfers", "ecommerce", "p2p-transfers", "remittances",
    "insurance-premiums", "bnpl", "bill-payments", "payroll", "atm-withdrawals",
    "equity-markets", "etd", "forex", "fixed-income", "commodities", "otc-derivatives",
    "cex", "blockchain-l1-l2", "defi", "stablecoins",
    "interbank-rtgs", "securities-settlement",
    "gaming-microtx", "gaming-sales",
    "government-payments",
    "rwa-tokenisation", "iot-m2m", "ai-agents",
}


def validate_file(filepath: Path) -> list[str]:
    """Validate a single data.json file. Returns list of error strings."""
    errors = []
    slug = filepath.parent.name

    try:
        with open(filepath) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return [f"Invalid JSON: {e}"]

    # Top-level keys
    for key in REQUIRED_TOP_KEYS:
        if key not in data:
            errors.append(f"Missing top-level key: {key}")

    # Slug check
    if data.get("slug") != slug:
        errors.append(f"slug mismatch: expected '{slug}', got '{data.get('slug')}'")

    # Sector check
    if "sector" in data and not isinstance(data["sector"], str):
        errors.append(f"sector is not a string: {type(data['sector'])}")

    # last_updated format
    lu = data.get("last_updated", "")
    if not (isinstance(lu, str) and len(lu) == 10 and lu.count("-") == 2):
        errors.append(f"last_updated format invalid: '{lu}' (expected YYYY-MM-DD)")

    # Current metrics
    current = data.get("current", {})
    if not isinstance(current, dict):
        errors.append("current is not a dict")
    else:
        for metric in REQUIRED_CURRENT_KEYS:
            if metric not in current:
                errors.append(f"current.{metric} missing")
            elif not isinstance(current[metric], dict):
                errors.append(f"current.{metric} is not a dict")
            else:
                m = current[metric]
                for mk in REQUIRED_METRIC_KEYS:
                    if mk not in m:
                        errors.append(f"current.{metric}.{mk} missing")
                if "confidence" in m and m["confidence"] not in VALID_CONFIDENCE:
                    errors.append(f"current.{metric}.confidence invalid: '{m['confidence']}'")
                # value should be number or null
                if "value" in m and m["value"] is not None and not isinstance(m["value"], (int, float)):
                    errors.append(f"current.{metric}.value is not number/null: {type(m['value'])}")

    # Historic
    historic = data.get("historic", [])
    if not isinstance(historic, list):
        errors.append("historic is not a list")
    else:
        for i, entry in enumerate(historic):
            if not isinstance(entry, dict):
                errors.append(f"historic[{i}] is not a dict")
                continue
            if "year" not in entry:
                errors.append(f"historic[{i}] missing 'year'")
            for field in ["annual_volume", "avg_tps", "source", "confidence"]:
                if field not in entry:
                    errors.append(f"historic[{i}] missing '{field}'")

    # Projections
    projections = data.get("projections", {})
    if not isinstance(projections, dict):
        errors.append("projections is not a dict")
    else:
        for scenario in PROJECTION_SCENARIOS:
            if scenario not in projections:
                errors.append(f"projections.{scenario} missing")
            elif not isinstance(projections[scenario], list):
                errors.append(f"projections.{scenario} is not a list")
            else:
                for i, entry in enumerate(projections[scenario]):
                    if not isinstance(entry, dict):
                        errors.append(f"projections.{scenario}[{i}] is not a dict")
                        continue
                    if "year" not in entry:
                        errors.append(f"projections.{scenario}[{i}] missing 'year'")

    # Overlap
    overlap = data.get("overlap", {})
    if not isinstance(overlap, dict):
        errors.append("overlap is not a dict")
    else:
        for key in REQUIRED_OVERLAP_KEYS:
            if key not in overlap:
                errors.append(f"overlap.{key} missing")
        if "overlap_type" in overlap and overlap["overlap_type"] not in VALID_OVERLAP_TYPES:
            errors.append(f"overlap.overlap_type invalid: '{overlap['overlap_type']}'")
        if "overlaps_with" in overlap and not isinstance(overlap["overlaps_with"], list):
            errors.append(f"overlap.overlaps_with is not a list")

    # Sources
    sources = data.get("sources", [])
    if not isinstance(sources, list):
        errors.append("sources is not a list")
    elif len(sources) == 0:
        errors.append("sources is empty")
    else:
        for i, s in enumerate(sources):
            if not isinstance(s, dict):
                errors.append(f"sources[{i}] is not a dict")
                continue
            for key in REQUIRED_SOURCE_KEYS:
                if key not in s:
                    errors.append(f"sources[{i}] missing '{key}'")

    return errors


def main():
    found_files = []
    for sector_dir in sorted(ANALYSIS_ROOT.iterdir()):
        if not sector_dir.is_dir():
            continue
        for cat_dir in sorted(sector_dir.iterdir()):
            if not cat_dir.is_dir():
                continue
            data_file = cat_dir / "data.json"
            if data_file.exists():
                found_files.append(data_file)

    # Check we have all 24
    found_slugs = {f.parent.name for f in found_files}
    missing = ALL_SLUGS - found_slugs
    if missing:
        print(f"WARNING: Missing {len(missing)} category directories: {', '.join(sorted(missing))}")

    total_errors = 0
    total_pass = 0

    for filepath in found_files:
        slug = filepath.parent.name
        errors = validate_file(filepath)
        if errors:
            print(f"FAIL  {slug}")
            for e in errors:
                print(f"      {e}")
            total_errors += len(errors)
        else:
            print(f"PASS  {slug}")
            total_pass += 1

    print(f"\n{'=' * 50}")
    print(f"  {total_pass}/{len(found_files)} passed, {total_errors} total errors")
    print(f"{'=' * 50}")

    sys.exit(0 if total_errors == 0 else 1)


if __name__ == "__main__":
    main()
