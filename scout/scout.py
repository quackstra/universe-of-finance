#!/usr/bin/env python3
"""Universe of Finance — Scout Module

Discovers and prioritises transaction categories for research based on
data availability, market scale, and strategic relevance.

Usage:
    python3 scout.py              # Full scan, output to backlog.yaml
    python3 scout.py --dry-run    # Preview without writing
"""

import json
import os
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path

import yaml


SCRIPT_DIR = Path(__file__).parent
CONFIG_PATH = SCRIPT_DIR / "config.yaml"
BACKLOG_PATH = SCRIPT_DIR / "backlog.yaml"
CATEGORIES_DIR = SCRIPT_DIR.parent / "categories"
ANALYSIS_DIR = SCRIPT_DIR.parent / "analysis"


@dataclass
class CategoryEntry:
    """A transaction category to research."""
    name: str
    slug: str
    sector: str
    priority: int
    estimated_scale: str
    known_sources: list[str] = field(default_factory=list)
    score: float = 0.0
    status: str = "pending"  # pending, methodology_done, research_done
    methodology_exists: bool = False
    analysis_exists: bool = False


def load_config() -> dict:
    """Load scout configuration."""
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def check_existing_work() -> tuple[set[str], set[str]]:
    """Check which categories already have methodology or analysis."""
    methodologies: set[str] = set()
    analyses: set[str] = set()

    # Scan categories/ for METHODOLOGY.md files
    if CATEGORIES_DIR.exists():
        for method_file in CATEGORIES_DIR.rglob("METHODOLOGY.md"):
            slug = method_file.parent.name
            methodologies.add(slug)

    # Scan analysis/ for REPORT.md files
    if ANALYSIS_DIR.exists():
        for report_file in ANALYSIS_DIR.rglob("REPORT.md"):
            slug = report_file.parent.name
            analyses.add(slug)

    return methodologies, analyses


def score_category(entry: CategoryEntry, config: dict) -> float:
    """Score a category based on config weights."""
    weights = config.get("scoring", {})

    # Data availability (based on known sources count and confidence)
    source_count = len(entry.known_sources)
    data_score = min(source_count / 3.0, 1.0) * 100

    # Market scale (rough estimate from description)
    scale_scores = {
        "tens of billions/day": 100,
        "billions/day": 85,
        "hundreds of millions/day": 70,
        "millions/day": 55,
        "millions/day but massive value": 60,
        "millions/day high value": 60,
        "tens of millions/day": 65,
        "emerging": 30,
        "nascent": 15,
        "nascent but projected massive": 25,
    }
    market_score = scale_scores.get(entry.estimated_scale, 40)

    # Growth rate (heuristic: emerging > established)
    growth_scores = {
        "nascent but projected massive": 95,
        "nascent": 85,
        "emerging": 80,
        "tens of billions/day": 30,  # mature
        "billions/day": 45,
        "hundreds of millions/day": 50,
        "millions/day": 55,
        "tens of millions/day": 60,
    }
    growth_score = growth_scores.get(entry.estimated_scale, 50)

    # Uniqueness (inverse of how well-covered this is)
    uniqueness_score = 70  # base score, refined as we learn more

    # Radix relevance
    radix_keywords = {"defi", "digital", "token", "blockchain", "l1", "l2",
                      "stablecoin", "crypto", "rwa"}
    radix_score = 80 if any(kw in entry.slug.lower() or kw in entry.name.lower()
                            for kw in radix_keywords) else 30

    total = (
        data_score * weights.get("data_availability_weight", 0.30)
        + market_score * weights.get("market_scale_weight", 0.25)
        + growth_score * weights.get("growth_rate_weight", 0.20)
        + uniqueness_score * weights.get("uniqueness_weight", 0.15)
        + radix_score * weights.get("radix_relevance_weight", 0.10)
    )

    return round(total, 1)


def build_backlog(config: dict) -> list[CategoryEntry]:
    """Build the prioritised research backlog from config."""
    methodologies, analyses = check_existing_work()
    entries: list[CategoryEntry] = []

    for sector, categories in config.get("categories", {}).items():
        sector_name = sector.replace("_", " ").title()
        for cat in categories:
            entry = CategoryEntry(
                name=cat["name"],
                slug=cat["slug"],
                sector=sector_name,
                priority=cat.get("priority", 5),
                estimated_scale=cat.get("estimated_scale", "unknown"),
                known_sources=cat.get("known_sources", []),
                methodology_exists=cat["slug"] in methodologies,
                analysis_exists=cat["slug"] in analyses,
            )

            # Set status
            if entry.analysis_exists:
                entry.status = "research_done"
            elif entry.methodology_exists:
                entry.status = "methodology_done"
            else:
                entry.status = "pending"

            entry.score = score_category(entry, config)
            entries.append(entry)

    # Sort by score (descending), then by priority (ascending)
    entries.sort(key=lambda e: (-e.score, e.priority))

    return entries


def write_backlog(entries: list[CategoryEntry]) -> None:
    """Write the backlog to YAML."""
    output = {
        "generated": "auto-generated by scout.py",
        "total_categories": len(entries),
        "pending": sum(1 for e in entries if e.status == "pending"),
        "methodology_done": sum(1 for e in entries if e.status == "methodology_done"),
        "research_done": sum(1 for e in entries if e.status == "research_done"),
        "categories": [asdict(e) for e in entries],
    }

    with open(BACKLOG_PATH, "w") as f:
        yaml.dump(output, f, default_flow_style=False, sort_keys=False)

    print(f"Backlog written to {BACKLOG_PATH}")
    print(f"  Total: {output['total_categories']}")
    print(f"  Pending: {output['pending']}")
    print(f"  Methodology done: {output['methodology_done']}")
    print(f"  Research done: {output['research_done']}")


def print_backlog(entries: list[CategoryEntry]) -> None:
    """Print backlog summary to stdout."""
    print(f"\n{'Rank':<5} {'Score':<7} {'Status':<18} {'Category'}")
    print("-" * 70)
    for i, entry in enumerate(entries, 1):
        status_icon = {
            "pending": "⬜",
            "methodology_done": "🟡",
            "research_done": "🟢",
        }.get(entry.status, "⬜")
        print(f"{i:<5} {entry.score:<7} {status_icon} {entry.status:<15} {entry.name}")


def main() -> None:
    dry_run = "--dry-run" in sys.argv

    print("=== Universe of Finance — Scout ===")
    print()

    config = load_config()
    entries = build_backlog(config)

    print_backlog(entries)

    if not dry_run:
        print()
        write_backlog(entries)
    else:
        print("\n(dry run — no files written)")


if __name__ == "__main__":
    main()
