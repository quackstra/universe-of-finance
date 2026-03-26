#!/usr/bin/env bash
# Universe of Finance Runner — orchestrates Scout → Architect → Analyze
#
# Usage:
#   ./run.sh                      # Full pipeline: scout + architect + analyze
#   ./run.sh scout                # Scout only (refresh backlog)
#   ./run.sh architect            # Architect only (design methodology for top pending category)
#   ./run.sh analyze              # Analyze only (execute research for top methodology-ready category)
#   ./run.sh elf-run              # Full autonomous elf run (Steps A-E, 48+ capsules)
#   ./run.sh --category "SLUG"    # Target a specific category
#
# For cron: runs unattended with logging to logs/
set -euo pipefail

UOF_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_DIR="${UOF_DIR}/logs"
BACKLOG="${UOF_DIR}/scout/backlog.yaml"
CATEGORIES_DIR="${UOF_DIR}/categories"
ANALYSIS_DIR="${UOF_DIR}/analysis"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"

NOTES_DIR="${UOF_DIR}/notes"

mkdir -p "$LOG_DIR" "$CATEGORIES_DIR" "$ANALYSIS_DIR" "$NOTES_DIR"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

log() {
    echo "[$(date '+%H:%M:%S')] $*" | tee -a "${LOG_DIR}/run_${TIMESTAMP}.log"
}

check_deps() {
    local missing=0
    for cmd in python3 claude; do
        if ! command -v "$cmd" &>/dev/null; then
            log "ERROR: Required command '$cmd' not found"
            missing=1
        fi
    done
    if [ "$missing" -eq 1 ]; then
        exit 1
    fi
}

# ---------------------------------------------------------------------------
# Stages
# ---------------------------------------------------------------------------

run_scout() {
    log "=== SCOUT: Scanning for transaction categories ==="
    cd "${UOF_DIR}/scout"
    python3 scout.py 2>&1 | tee -a "${LOG_DIR}/run_${TIMESTAMP}.log"
    log "Scout complete. Backlog at: ${BACKLOG}"
}

run_architect() {
    local category="${1:-}"

    if [ -z "$category" ]; then
        # Pick top pending category from backlog
        if [ ! -f "$BACKLOG" ]; then
            log "No backlog found. Run scout first."
            return 1
        fi
        category=$(python3 -c "
import yaml
with open('${BACKLOG}') as f:
    data = yaml.safe_load(f)
for cat in data.get('categories', []):
    if cat.get('status') == 'pending':
        print(cat['slug'])
        break
")
    fi

    if [ -z "$category" ]; then
        log "All categories have methodologies. Run scout to refresh."
        return 0
    fi

    # Look up category details from backlog
    local cat_name
    cat_name=$(python3 -c "
import yaml
with open('${BACKLOG}') as f:
    data = yaml.safe_load(f)
for cat in data.get('categories', []):
    if cat['slug'] == '${category}':
        print(cat['name'])
        break
")

    local cat_sector
    cat_sector=$(python3 -c "
import yaml
with open('${BACKLOG}') as f:
    data = yaml.safe_load(f)
for cat in data.get('categories', []):
    if cat['slug'] == '${category}':
        print(cat['sector'].lower().replace(' ', '-'))
        break
")

    log "=== ARCHITECT: Designing methodology for '${cat_name}' (${category}) ==="

    # Ensure category directory exists
    local cat_dir="${CATEGORIES_DIR}/${cat_sector}/${category}"
    mkdir -p "$cat_dir"

    local architect_prompt
    architect_prompt="$(cat <<PROMPT
You are the Universe of Finance Research Architect. Read and follow the
instructions in architect/SKILL.md exactly.

Your task: design a research methodology for the transaction category
"${cat_name}" (slug: ${category}, sector: ${cat_sector}).

Before you start:
1. Read TAXONOMY.md to understand the full transaction taxonomy
2. Read architect/SKILL.md for your instructions and output format
3. Read architect/references/methodology.md for research patterns
4. Read architect/references/quality_gates.md for quality criteria

Remember:
- Define "transaction" precisely for this category
- Identify real, verifiable data sources (not hallucinated)
- Design three projection scenarios with explicit assumptions
- Flag double-counting risks with adjacent categories
- Be honest about data gaps

Write the methodology to: ${cat_dir}/METHODOLOGY.md
PROMPT
)"

    cd "${UOF_DIR}"
    claude --print -p "$architect_prompt" 2>&1 | tee -a "${LOG_DIR}/architect_${TIMESTAMP}.log"

    log "Architect complete for '${cat_name}'"
}

run_analyze() {
    local category="${1:-}"

    if [ -z "$category" ]; then
        # Pick top methodology-ready category
        if [ ! -f "$BACKLOG" ]; then
            log "No backlog found. Run scout first."
            return 1
        fi
        category=$(python3 -c "
import yaml
with open('${BACKLOG}') as f:
    data = yaml.safe_load(f)
for cat in data.get('categories', []):
    if cat.get('status') == 'methodology_done':
        print(cat['slug'])
        break
")
    fi

    if [ -z "$category" ]; then
        log "No categories ready for analysis. Run architect first."
        return 0
    fi

    # Look up category details
    local cat_name cat_sector
    cat_name=$(python3 -c "
import yaml
with open('${BACKLOG}') as f:
    data = yaml.safe_load(f)
for cat in data.get('categories', []):
    if cat['slug'] == '${category}':
        print(cat['name'])
        break
")
    cat_sector=$(python3 -c "
import yaml
with open('${BACKLOG}') as f:
    data = yaml.safe_load(f)
for cat in data.get('categories', []):
    if cat['slug'] == '${category}':
        print(cat['sector'].lower().replace(' ', '-'))
        break
")

    log "=== ANALYZE: Researching '${cat_name}' (${category}) ==="

    # Find the methodology file
    local method_file="${CATEGORIES_DIR}/${cat_sector}/${category}/METHODOLOGY.md"
    if [ ! -f "$method_file" ]; then
        log "ERROR: No methodology found at ${method_file}"
        return 1
    fi

    # Ensure analysis output directory exists
    local analysis_dir="${ANALYSIS_DIR}/${cat_sector}/${category}"
    mkdir -p "${analysis_dir}/charts"

    local analyze_prompt
    analyze_prompt="$(cat <<PROMPT
You are a Universe of Finance research Elf. Read and follow the instructions
in elves/survival_guide.md exactly.

Your task: execute the research methodology for "${cat_name}" and produce
a complete analysis report.

Before you start:
1. Read elves/survival_guide.md for your rules and protocol
2. Read the methodology at ${method_file} carefully
3. Read architect/references/quality_gates.md for validation criteria

Your outputs go to: ${analysis_dir}/
- REPORT.md — full research report
- data.json — structured data
- charts/ — generated visualisations

Follow the methodology precisely. Every number needs a source. Tag confidence
levels honestly. Generate all three projection scenarios.

After completing research, run validation: ./elves/validation_gates.sh ${analysis_dir}
Commit with prefix [UoF] ${category}:
PROMPT
)"

    cd "${UOF_DIR}"
    claude --print -p "$analyze_prompt" 2>&1 | tee -a "${LOG_DIR}/analyze_${TIMESTAMP}.log"

    log "Analysis complete for '${cat_name}'"
}

run_elf_run() {
    log "=== ELF RUN: Full autonomous research session (Steps A-E) ==="

    local elf_prompt
    elf_prompt="$(cat <<'PROMPT'
You are a Universe of Finance research Elf executing a full autonomous
research run. Follow the protocol in elves/run_protocol.md exactly.

## Your session protocol (Steps A-E):

### Step A: Review & Orient
1. Read notes/last_session.md (if it exists) for continuity
2. Read notes/research_agenda.md for your work queue
3. Read analysis/README.md to see completed work
4. Read TAXONOMY.md for the full category structure
5. Read elves/survival_guide.md for your rules

### Step B: Research — Produce 48+ Research Capsules
Follow inside-out priority (biggest categories today first).
For each category:
- If no METHODOLOGY.md exists, create one following architect/SKILL.md
- Collect data, cite sources with hyperlinks, show calculations
- Write REPORT.md (clean, reader-facing) + data.json + workings/
- Run elves/validation_gates.sh on each completed category
- Commit with prefix [UoF]

### Step C: Taxonomy Review
After 48+ capsules, assess whether TAXONOMY.md needs new sectors,
categories, splits, or merges. Update if needed.

### Step D: Retrospective
Review prior research for stale data, cross-category conflicts,
confidence upgrades, and double-counting issues.

### Step E: Session Notes
Write notes/last_session.md and notes/research_agenda.md for the
next run. Commit with prefix [UoF] session-notes:

## Critical rules:
- CITE HEAVILY — hyperlink directly to sources, leave nothing relevant out
- SHOW ALL MATH — explain calculations and assumptions in workings/ files
- CONFIDENCE TAG every number (green/yellow/red)
- Inside-out: biggest TODAY first, expand outward
PROMPT
)"

    cd "${UOF_DIR}"
    claude -p "$elf_prompt" 2>&1 | tee -a "${LOG_DIR}/elf_run_${TIMESTAMP}.log"

    log "Elf run complete."
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

main() {
    check_deps

    local mode="${1:-all}"
    local category=""

    # Parse flags
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --category)
                category="$2"
                shift 2
                ;;
            scout|architect|analyze|elf-run|all)
                mode="$1"
                shift
                ;;
            *)
                shift
                ;;
        esac
    done

    log "Universe of Finance Runner — mode: ${mode}, timestamp: ${TIMESTAMP}"

    case "$mode" in
        scout)
            run_scout
            ;;
        architect)
            run_architect "$category"
            ;;
        analyze)
            run_analyze "$category"
            ;;
        elf-run)
            run_elf_run
            ;;
        all)
            run_scout
            run_architect "$category"
            run_analyze "$category"
            ;;
        *)
            echo "Usage: $0 [scout|architect|analyze|elf-run|all] [--category SLUG]"
            exit 1
            ;;
    esac

    log "Universe of Finance Runner complete."
}

main "$@"
