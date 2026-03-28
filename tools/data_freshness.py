#!/usr/bin/env python3
"""Universe of Finance — Data Freshness Checker

Reads all data.json files, extracts source dates, and flags stale data.
Outputs a markdown table and writes analysis/DATA_FRESHNESS.md.
"""

import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

ANALYSIS_ROOT = Path(__file__).resolve().parent.parent / "analysis"
OUTPUT_FILE = ANALYSIS_ROOT / "DATA_FRESHNESS.md"

# Thresholds in days
STALE_DAYS = 365       # 12 months
CRITICAL_DAYS = 730    # 24 months


def parse_date(date_str: str) -> date | None:
    """Parse a date string in various formats."""
    if not date_str:
        return None

    # Try common formats
    for fmt in ("%Y-%m-%d", "%Y-%m", "%Y/%m/%d", "%B %Y", "%b %Y", "%Y"):
        try:
            return datetime.strptime(date_str.strip(), fmt).date()
        except ValueError:
            continue

    # Try extracting year-month-day from longer strings
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", date_str)
    if m:
        try:
            return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            pass

    # Try extracting just a year
    m = re.search(r"(20\d{2})", date_str)
    if m:
        return date(int(m.group(1)), 6, 15)  # Mid-year approximation

    return None


def extract_source_dates(data: dict) -> list[date]:
    """Extract all date-like fields from sources."""
    dates = []

    # Check top-level last_updated
    if "last_updated" in data:
        d = parse_date(data["last_updated"])
        if d:
            dates.append(d)

    # Check sources array
    for source in data.get("sources", []):
        for field in ("accessed", "date", "published"):
            if field in source and source[field]:
                d = parse_date(str(source[field]))
                if d:
                    dates.append(d)

    return dates


def classify_staleness(oldest: date, today: date) -> str:
    """Classify staleness of a date."""
    age_days = (today - oldest).days
    if age_days > CRITICAL_DAYS:
        return "CRITICAL"
    elif age_days > STALE_DAYS:
        return "STALE"
    return "FRESH"


def generate_report() -> str:
    """Generate the data freshness report."""
    today = date.today()
    rows = []

    for sector_dir in sorted(ANALYSIS_ROOT.iterdir()):
        if not sector_dir.is_dir():
            continue
        for cat_dir in sorted(sector_dir.iterdir()):
            if not cat_dir.is_dir():
                continue
            data_file = cat_dir / "data.json"
            if not data_file.exists():
                continue

            with open(data_file) as f:
                data = json.load(f)

            category = data.get("category", cat_dir.name)
            slug = data.get("slug", cat_dir.name)
            sector = data.get("sector", sector_dir.name)
            source_dates = extract_source_dates(data)
            num_sources = len(data.get("sources", []))

            if not source_dates:
                rows.append({
                    "sector": sector,
                    "category": category,
                    "slug": slug,
                    "newest": None,
                    "oldest": None,
                    "num_sources": num_sources,
                    "status": "NO DATES",
                    "age_days": None,
                })
                continue

            newest = max(source_dates)
            oldest = min(source_dates)
            status = classify_staleness(oldest, today)
            age_days = (today - oldest).days

            rows.append({
                "sector": sector,
                "category": category,
                "slug": slug,
                "newest": newest,
                "oldest": oldest,
                "num_sources": num_sources,
                "status": status,
                "age_days": age_days,
            })

    # Sort: CRITICAL first, then STALE, then FRESH
    status_order = {"CRITICAL": 0, "STALE": 1, "NO DATES": 2, "FRESH": 3}
    rows.sort(key=lambda r: (status_order.get(r["status"], 99), -(r["age_days"] or 0)))

    # Build markdown
    lines = []
    lines.append("# Data Freshness Report")
    lines.append("")
    lines.append(f"> Generated: {today.isoformat()}")
    lines.append(f"> Thresholds: STALE = >{STALE_DAYS} days ({STALE_DAYS // 30} months), "
                 f"CRITICAL = >{CRITICAL_DAYS} days ({CRITICAL_DAYS // 30} months)")
    lines.append("")

    # Summary counts
    fresh = sum(1 for r in rows if r["status"] == "FRESH")
    stale = sum(1 for r in rows if r["status"] == "STALE")
    critical = sum(1 for r in rows if r["status"] == "CRITICAL")
    no_dates = sum(1 for r in rows if r["status"] == "NO DATES")

    lines.append("## Summary")
    lines.append("")
    lines.append(f"| Status | Count |")
    lines.append(f"|--------|-------|")
    lines.append(f"| FRESH (<{STALE_DAYS // 30} months) | {fresh} |")
    lines.append(f"| STALE ({STALE_DAYS // 30}-{CRITICAL_DAYS // 30} months) | {stale} |")
    lines.append(f"| CRITICAL (>{CRITICAL_DAYS // 30} months) | {critical} |")
    lines.append(f"| NO DATES | {no_dates} |")
    lines.append(f"| **Total** | **{len(rows)}** |")
    lines.append("")

    # Main table
    lines.append("## Detail")
    lines.append("")
    lines.append("| Status | Sector | Category | Sources | Newest Date | Oldest Date | Age (days) |")
    lines.append("|--------|--------|----------|---------|-------------|-------------|------------|")

    for r in rows:
        status_icon = {
            "FRESH": "FRESH",
            "STALE": "**STALE**",
            "CRITICAL": "**CRITICAL**",
            "NO DATES": "NO DATES",
        }.get(r["status"], r["status"])

        newest_str = r["newest"].isoformat() if r["newest"] else "—"
        oldest_str = r["oldest"].isoformat() if r["oldest"] else "—"
        age_str = str(r["age_days"]) if r["age_days"] is not None else "—"

        lines.append(
            f"| {status_icon} | {r['sector']} | {r['category']} | "
            f"{r['num_sources']} | {newest_str} | {oldest_str} | {age_str} |"
        )

    lines.append("")

    # Recommendations
    if critical or stale:
        lines.append("## Recommendations")
        lines.append("")
        if critical:
            lines.append(f"### CRITICAL ({critical} categories)")
            lines.append("")
            lines.append("These categories have source data older than 24 months. "
                         "Research may be based on outdated figures that have shifted significantly.")
            lines.append("")
            for r in rows:
                if r["status"] == "CRITICAL":
                    lines.append(f"- **{r['category']}** ({r['sector']}): oldest source is {r['oldest']}, "
                                 f"{r['age_days']} days old")
            lines.append("")
        if stale:
            lines.append(f"### STALE ({stale} categories)")
            lines.append("")
            lines.append("These categories have source data older than 12 months. "
                         "Consider refreshing sources in the next research run.")
            lines.append("")
            for r in rows:
                if r["status"] == "STALE":
                    lines.append(f"- **{r['category']}** ({r['sector']}): oldest source is {r['oldest']}, "
                                 f"{r['age_days']} days old")
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("*Generated by `tools/data_freshness.py`. Run periodically to track data decay.*")

    return "\n".join(lines)


def main():
    report = generate_report()

    # Print to stdout
    print(report)

    # Write to file
    OUTPUT_FILE.write_text(report)
    print(f"\nReport written to: {OUTPUT_FILE}", file=sys.stderr)


if __name__ == "__main__":
    main()
