#!/usr/bin/env python3
"""Build the versions/index.html page listing all archived dashboard snapshots."""

import os
import re
import subprocess
from pathlib import Path

VERSIONS_DIR = Path(__file__).parent.parent / "versions"


def get_version_files():
    """Find all versioned HTML files, sorted newest first."""
    files = []
    for f in VERSIONS_DIR.glob("v*.html"):
        if f.name == "index.html":
            continue
        # Parse: v{num}-{date}-{sha}.html
        m = re.match(r"v(\d+)-(\d{4}-\d{2}-\d{2})-([a-f0-9]+)\.html", f.name)
        if m:
            files.append({
                "filename": f.name,
                "num": int(m.group(1)),
                "date": m.group(2),
                "sha": m.group(3),
            })
    files.sort(key=lambda x: x["num"], reverse=True)
    return files


def get_commit_message(sha: str) -> str:
    """Get commit message for a short SHA."""
    try:
        result = subprocess.run(
            ["git", "log", "--all", "--oneline", f"--grep={sha}", "-1", "--pretty=%s"],
            capture_output=True, text=True, timeout=5
        )
        if result.stdout.strip():
            return result.stdout.strip()
    except Exception:
        pass
    # Fallback: try direct lookup
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--pretty=%s", sha],
            capture_output=True, text=True, timeout=5
        )
        if result.stdout.strip():
            return result.stdout.strip()
    except Exception:
        pass
    return "Dashboard update"


def extract_big_number(filepath: Path) -> str:
    """Try to extract the Big Number TPS from a dashboard HTML file."""
    try:
        content = filepath.read_text()
        # Look for the counter target value
        m = re.search(r'data-target="(\d+)".*?TPS', content)
        if m:
            return f"~{int(m.group(1)):,} TPS"
        # Fallback: look for tps values in DATA array
        tps_vals = re.findall(r'tps:(\d+(?:\.\d+)?)', content)
        if tps_vals:
            return f"{len(tps_vals)} categories"
    except Exception:
        pass
    return ""


def build_html(versions: list) -> str:
    """Generate the versions index HTML."""
    rows = ""
    for v in versions:
        msg = get_commit_message(v["sha"])
        meta = extract_big_number(VERSIONS_DIR / v["filename"])
        badge = f'<span class="meta">{meta}</span>' if meta else ""
        is_latest = " latest" if v == versions[0] else ""
        latest_badge = '<span class="latest-badge">LATEST</span>' if v == versions[0] else ""
        rows += f"""
      <tr class="version-row{is_latest}">
        <td class="version-num">v{v['num']}</td>
        <td class="version-date">{v['date']}</td>
        <td class="version-sha"><code>{v['sha']}</code></td>
        <td class="version-msg">{msg} {badge}</td>
        <td class="version-link">
          {latest_badge}
          <a href="{v['filename']}" class="view-btn">View Snapshot</a>
        </td>
      </tr>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Universe of Finance — Version History</title>
<meta name="description" content="Browse every version of the Universe of Finance dashboard, from the first research run to the latest.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

:root {{
  --bg: #0a0e1a;
  --card: #111827;
  --card-border: #1e293b;
  --accent-blue: #3b82f6;
  --accent-green: #10b981;
  --text: #f9fafb;
  --muted: #9ca3af;
  --font: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --mono: 'JetBrains Mono', 'Fira Code', monospace;
}}

body {{
  font-family: var(--font);
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
}}

.container {{
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 24px;
}}

/* Header */
.header {{
  padding: 60px 0 40px;
  text-align: center;
}}

.header h1 {{
  font-size: 2.5rem;
  font-weight: 800;
  letter-spacing: -0.03em;
  margin-bottom: 12px;
}}

.header h1 span {{
  background: linear-gradient(135deg, var(--accent-blue), var(--accent-green));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}}

.header p {{
  color: var(--muted);
  font-size: 1.1rem;
  max-width: 600px;
  margin: 0 auto;
}}

.back-link {{
  display: inline-block;
  margin-bottom: 32px;
  color: var(--accent-blue);
  text-decoration: none;
  font-size: 0.95rem;
  transition: opacity 0.2s;
}}
.back-link:hover {{ opacity: 0.8; }}

/* Table */
.versions-card {{
  background: var(--card);
  border: 1px solid var(--card-border);
  border-radius: 16px;
  overflow: hidden;
  margin-bottom: 60px;
}}

.versions-table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 0.95rem;
}}

.versions-table th {{
  text-align: left;
  padding: 16px 20px;
  font-weight: 600;
  color: var(--muted);
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border-bottom: 1px solid var(--card-border);
  background: rgba(255,255,255,0.02);
}}

.versions-table td {{
  padding: 14px 20px;
  border-bottom: 1px solid rgba(255,255,255,0.04);
  vertical-align: middle;
}}

.version-row:hover {{
  background: rgba(59,130,246,0.05);
}}

.version-row.latest {{
  background: rgba(16,185,129,0.06);
}}

.version-num {{
  font-family: var(--mono);
  font-weight: 600;
  color: var(--accent-blue);
  white-space: nowrap;
}}

.version-date {{
  font-family: var(--mono);
  color: var(--muted);
  white-space: nowrap;
}}

.version-sha code {{
  font-family: var(--mono);
  font-size: 0.85rem;
  background: rgba(255,255,255,0.06);
  padding: 3px 8px;
  border-radius: 4px;
  color: var(--accent-blue);
}}

.version-msg {{
  max-width: 400px;
}}

.meta {{
  display: inline-block;
  font-size: 0.75rem;
  color: var(--accent-green);
  background: rgba(16,185,129,0.12);
  padding: 2px 8px;
  border-radius: 4px;
  margin-left: 8px;
}}

.version-link {{
  text-align: right;
  white-space: nowrap;
}}

.view-btn {{
  display: inline-block;
  background: var(--accent-blue);
  color: white;
  padding: 8px 18px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 500;
  font-size: 0.85rem;
  transition: all 0.2s;
}}
.view-btn:hover {{
  background: #2563eb;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(59,130,246,0.3);
}}

.latest-badge {{
  display: inline-block;
  font-size: 0.7rem;
  font-weight: 700;
  color: var(--accent-green);
  border: 1px solid var(--accent-green);
  padding: 2px 8px;
  border-radius: 4px;
  margin-right: 10px;
  letter-spacing: 0.05em;
}}

/* Stats */
.stats-row {{
  display: flex;
  gap: 20px;
  margin-bottom: 40px;
  flex-wrap: wrap;
}}

.stat-card {{
  background: var(--card);
  border: 1px solid var(--card-border);
  border-radius: 12px;
  padding: 24px;
  flex: 1;
  min-width: 200px;
  text-align: center;
}}

.stat-card .num {{
  font-family: var(--mono);
  font-size: 2rem;
  font-weight: 700;
  color: var(--accent-blue);
}}

.stat-card .label {{
  color: var(--muted);
  font-size: 0.85rem;
  margin-top: 4px;
}}

/* Footer */
footer {{
  text-align: center;
  padding: 40px 0;
  color: var(--muted);
  font-size: 0.85rem;
}}
footer a {{ color: var(--accent-blue); text-decoration: none; }}
footer a:hover {{ text-decoration: underline; }}

/* Responsive */
@media (max-width: 768px) {{
  .header h1 {{ font-size: 1.8rem; }}
  .versions-table {{ font-size: 0.85rem; }}
  .versions-table th, .versions-table td {{ padding: 10px 12px; }}
  .version-msg {{ max-width: 200px; }}
  .stats-row {{ flex-direction: column; }}
}}

/* Empty state */
.empty-state {{
  text-align: center;
  padding: 80px 20px;
  color: var(--muted);
}}
.empty-state p {{ font-size: 1.1rem; }}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <a href="../index.html" class="back-link">&larr; Back to Dashboard</a>
    <h1>Version <span>History</span></h1>
    <p>Every snapshot of the Universe of Finance dashboard, from the first research run to the latest. Browse how the data evolved over time.</p>
  </div>

  <div class="stats-row">
    <div class="stat-card">
      <div class="num">{len(versions)}</div>
      <div class="label">Total Snapshots</div>
    </div>
    <div class="stat-card">
      <div class="num">{versions[0]['date'] if versions else '—'}</div>
      <div class="label">Latest Version</div>
    </div>
    <div class="stat-card">
      <div class="num">{versions[-1]['date'] if versions else '—'}</div>
      <div class="label">First Version</div>
    </div>
  </div>

  {"" if not versions else f'''<div class="versions-card">
    <table class="versions-table">
      <thead>
        <tr>
          <th>Version</th>
          <th>Date</th>
          <th>Commit</th>
          <th>Description</th>
          <th></th>
        </tr>
      </thead>
      <tbody>{rows}
      </tbody>
    </table>
  </div>'''}

  {"<div class='empty-state'><p>No versions archived yet. Versions will appear here after the next dashboard update.</p></div>" if not versions else ""}
</div>

<footer>
  <p><a href="../index.html">Universe of Finance</a> &middot; <a href="https://github.com/quackstra/universe-of-finance" target="_blank" rel="noopener">GitHub</a></p>
  <p style="margin-top:8px;">&copy; 2026 Universe of Finance &middot; CC BY 4.0</p>
</footer>
</body>
</html>"""


def main():
    VERSIONS_DIR.mkdir(exist_ok=True)
    versions = get_version_files()
    html = build_html(versions)
    (VERSIONS_DIR / "index.html").write_text(html)
    print(f"Built version index with {len(versions)} entries")


if __name__ == "__main__":
    main()
