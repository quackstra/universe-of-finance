#!/usr/bin/env bash
# Universe of Finance — Research Validation Gates
#
# Usage: ./elves/validation_gates.sh <category-dir>
# Example: ./elves/validation_gates.sh analysis/payments/consumer-cards
#
# Gates:
#   1. data.json exists and is valid JSON
#   2. REPORT.md exists and has content
#   3. All charts referenced in REPORT.md exist
#   4. Every data point in data.json has a source
#   5. Projection sanity checks pass

set -euo pipefail

CATEGORY_DIR="${1:?Usage: $0 <category-dir>}"
PASS=0
FAIL=0

gate() {
    local name="$1"
    shift
    if "$@"; then
        echo "  ✅ PASS: ${name}"
        PASS=$((PASS + 1))
    else
        echo "  ❌ FAIL: ${name}"
        FAIL=$((FAIL + 1))
    fi
}

echo "=== Validation Gates: ${CATEGORY_DIR} ==="
echo ""

# Gate 1: data.json exists and is valid JSON
check_json() {
    local json_file="${CATEGORY_DIR}/data.json"
    [ -f "$json_file" ] && python3 -c "import json; json.load(open('${json_file}'))" 2>/dev/null
}
gate "data.json is valid JSON" check_json

# Gate 2: REPORT.md exists and has content
check_report() {
    local report="${CATEGORY_DIR}/REPORT.md"
    [ -f "$report" ] && [ "$(wc -l < "$report")" -gt 10 ]
}
gate "REPORT.md exists with content" check_report

# Gate 3: All referenced charts exist
check_charts() {
    local report="${CATEGORY_DIR}/REPORT.md"
    if [ ! -f "$report" ]; then return 1; fi
    local missing=0
    while IFS= read -r img; do
        # Extract path from markdown image syntax ![...](path)
        local path
        path=$(echo "$img" | sed -n 's/.*(\([^)]*\)).*/\1/p')
        if [ -n "$path" ] && [[ "$path" != http* ]]; then
            local full_path="${CATEGORY_DIR}/${path}"
            if [ ! -f "$full_path" ]; then
                echo "    Missing chart: ${path}"
                missing=1
            fi
        fi
    done < <(grep -o '!\[.*\](.*\.png)' "$report" 2>/dev/null || true)
    return "$missing"
}
gate "All referenced charts exist" check_charts

# Gate 4: data.json has sources for key metrics
check_sources() {
    local json_file="${CATEGORY_DIR}/data.json"
    if [ ! -f "$json_file" ]; then return 1; fi
    python3 -c "
import json, sys
with open('${json_file}') as f:
    data = json.load(f)
current = data.get('current', {})
missing = []
for key, val in current.items():
    if isinstance(val, dict) and not val.get('source'):
        missing.append(key)
if missing:
    print(f'    Missing sources for: {missing}')
    sys.exit(1)
"
}
gate "Key metrics have sources" check_sources

# Gate 5: Projection sanity checks
check_projections() {
    local json_file="${CATEGORY_DIR}/data.json"
    if [ ! -f "$json_file" ]; then return 1; fi
    python3 -c "
import json, sys
with open('${json_file}') as f:
    data = json.load(f)
projections = data.get('projections', {})
issues = []
for scenario, points in projections.items():
    for point in points:
        tps = point.get('tps', 0)
        if tps < 0:
            issues.append(f'{scenario} {point[\"year\"]}: negative TPS ({tps})')
        # Check for unreasonable CAGR (>100% sustained)
    if len(points) >= 2:
        first = points[0].get('tps', 1)
        last = points[-1].get('tps', 1)
        years = points[-1].get('year', 2030) - points[0].get('year', 2026)
        if first > 0 and years > 0:
            cagr = (last / first) ** (1 / years) - 1
            if cagr > 1.0:
                issues.append(f'{scenario}: CAGR {cagr:.0%} exceeds 100%')
if issues:
    for issue in issues:
        print(f'    ⚠️  {issue}')
    sys.exit(1)
"
}
gate "Projection sanity checks" check_projections

echo ""
echo "Results: ${PASS} passed, ${FAIL} failed"

if [ "$FAIL" -gt 0 ]; then
    echo "❌ VALIDATION FAILED — fix issues before committing"
    exit 1
else
    echo "✅ ALL GATES PASSED — safe to commit"
    exit 0
fi
