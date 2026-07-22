#!/usr/bin/env python3
"""Universe of Finance — stylized report HTML generator.

Converts every analysis/**/*.md into a dark-theme, cross-linked, chart-augmented HTML page
under /reports/ (mirroring the analysis tree). Regenerable and idempotent.

Features
- Strips Jekyll front matter, converts markdown (tables, code, footnotes) to HTML.
- Auto cross-links known topics (categories, country deep dives, concepts) to their report
  pages — first occurrence per page, never inside links/code/headings, never self-links.
- Renders stat chips (TPS / confidence / opacity / rank) and a Chart.js visual where a
  data.json is present.
- Adds breadcrumb, related-links (calcs / methodology / siblings), and back-to-dashboard nav.
"""

import json
import re
import sys
from pathlib import Path

import markdown
from bs4 import BeautifulSoup, NavigableString

ROOT = Path(__file__).resolve().parent.parent
ANALYSIS = ROOT / "analysis"
OUT_ROOT = ROOT / "reports"
BASEURL = "/universe-of-finance"
REPO_BLOB = "https://github.com/quackstra/universe-of-finance/blob/main"

SECTOR_OF_DIR = {
    "payments": "Payments", "traditional-finance": "Traditional Finance",
    "digital-assets": "Digital Assets", "banking": "Banking", "gaming": "Gaming",
    "government": "Government", "emerging": "Emerging", "deep-dives": "Deep Dives",
    "methodology": "Methodology", "timeseries": "Timeseries",
}

# ── canonical numbers (single source: opacity.json + index.html DATA) ─────────
def load_canon():
    op = json.loads((ROOT / "data" / "opacity.json").read_text())
    canon = {}
    for c in op["categories"]:
        canon[c["name"]] = {"tps": c["tps"], "opacity": c["opacity"], "sector": c["sector"]}
    # confidence from the dashboard DATA array
    html = (ROOT / "index.html").read_text()
    m = re.search(r"const DATA = \[(.*?)\];", html, re.S)
    for row in re.finditer(r'name:"([^"]+)".*?confidence:(\d+)', m.group(1)):
        canon.setdefault(row.group(1), {})["confidence"] = int(row.group(2))
    ranks = sorted([n for n in canon if "tps" in canon[n]], key=lambda n: -canon[n]["tps"])
    for i, n in enumerate(ranks):
        canon[n]["rank"] = i + 1
    canon["_total_cats"] = len(ranks)
    return canon

CANON = load_canon()

# data.json uses verbose category names; bridge slug -> canonical short name (opacity.json)
SLUG_TO_NAME = {
    "consumer-cards": "Consumer Cards", "digital-wallets": "Digital Wallets",
    "bank-transfers": "Bank Transfers", "etd": "ETD (Derivatives)", "equity-markets": "Equity Markets",
    "cex": "CEX (Crypto)", "bill-payments": "Bill Payments", "ecommerce": "E-Commerce",
    "atm-withdrawals": "ATM Withdrawals", "iot-m2m": "IoT & M2M", "payroll": "Payroll",
    "government-payments": "Government Payments", "bnpl": "BNPL", "gaming-microtx": "Microtransactions",
    "stablecoins": "Stablecoins", "blockchain-l1-l2": "L1/L2 Blockchain",
    "insurance-premiums": "Insurance Premiums", "commodities": "Commodities",
    "p2p-transfers": "P2P Transfers", "forex": "Forex", "gaming-sales": "Game Sales",
    "remittances": "Remittances", "interbank-rtgs": "Interbank RTGS",
    "securities-settlement": "Securities Settlement", "fixed-income": "Fixed Income",
    "ai-agents": "AI Agents", "rwa-tokenisation": "RWA Tokenisation", "otc-derivatives": "OTC Derivatives",
}

# ── output path + url helpers ────────────────────────────────────────────────
def out_path(md: Path) -> Path:
    rel = md.relative_to(ANALYSIS).with_suffix(".html")
    return OUT_ROOT / rel

def url_for(md: Path) -> str:
    rel = md.relative_to(ANALYSIS).with_suffix(".html")
    return f"{BASEURL}/reports/{rel.as_posix()}"

# ── link map: term -> (compiled regex, url, css class) ───────────────────────
def build_link_map():
    m = {}  # term(lower) -> url
    # category REPORTs by display name + curated aliases
    cat_report = {}
    for md in ANALYSIS.rglob("REPORT.md"):
        dj = md.parent / "data.json"
        name = None
        if dj.exists():
            try:
                d = json.loads(dj.read_text())
                name = d.get("category") or d.get("country") or d.get("topic")
            except Exception:
                pass
        cat_report[md.parent.name] = url_for(md)
        if name:
            m[name.lower()] = url_for(md)
    # slug-based direct names
    def U(slug_path):  # slug_path relative like 'payments/consumer-cards'
        return f"{BASEURL}/reports/{slug_path}/REPORT.html"
    aliases = {
        "consumer cards": "payments/consumer-cards", "credit cards": "payments/consumer-cards",
        "card networks": "payments/consumer-cards", "debit cards": "payments/consumer-cards",
        "digital wallets": "payments/digital-wallets", "mobile wallets": "payments/digital-wallets",
        "bank transfers": "payments/bank-transfers", "bill payments": "payments/bill-payments",
        "e-commerce": "payments/ecommerce", "ecommerce": "payments/ecommerce",
        "atm withdrawals": "payments/atm-withdrawals", "payroll": "payments/payroll",
        "bnpl": "payments/bnpl", "buy now, pay later": "payments/bnpl",
        "insurance premiums": "payments/insurance-premiums", "p2p transfers": "payments/p2p-transfers",
        "remittances": "payments/remittances", "equity markets": "traditional-finance/equity-markets",
        "exchange-traded derivatives": "traditional-finance/etd", "commodities": "traditional-finance/commodities",
        "foreign exchange": "traditional-finance/forex", "forex": "traditional-finance/forex",
        "fixed income": "traditional-finance/fixed-income", "otc derivatives": "traditional-finance/otc-derivatives",
        "stablecoins": "digital-assets/stablecoins", "defi": "digital-assets/defi",
        "centralised exchanges": "digital-assets/cex", "centralized exchanges": "digital-assets/cex",
        "interbank rtgs": "banking/interbank-rtgs", "securities settlement": "banking/securities-settlement",
        "government payments": "government/government-payments", "ai agents": "emerging/ai-agents",
        "iot": "emerging/iot-m2m", "m2m": "emerging/iot-m2m", "rwa tokenisation": "emerging/rwa-tokenisation",
        "microtransactions": "gaming/gaming-microtx",
    }
    for term, sp in aliases.items():
        m[term] = U(sp)
    # deep dives (country/topic)
    dd = {
        "brazil": "deep-dives/brazil", "china": "deep-dives/china", "india": "deep-dives/india",
        "japan": "deep-dives/japan", "africa": "deep-dives/africa", "middle east": "deep-dives/middle-east",
        "gulf": "deep-dives/middle-east", "opaque markets": "deep-dives/opaque-markets",
        "insurance claims": "deep-dives/insurance-claims", "remittance corridors": "deep-dives/remittance-corridors",
        "hawala": "deep-dives/remittance-corridors", "shadow banking": "deep-dives/opaque-markets",
        "pix": "deep-dives/brazil", "upi": "deep-dives/india",
    }
    for term, sp in dd.items():
        m[term] = U(sp)
    m["united states"] = U("deep-dives/usa"); m["european union"] = U("deep-dives/eu")
    m["united kingdom"] = U("deep-dives/uk")
    # concept pages (cross-cutting docs under analysis/)
    concepts = {
        "mest": "MEST", "mutual economic state transitions": "MEST",
        "ttr": "TTR", "total tokenizable resources": "TTR",
        "peak tps": "PEAK_TPS", "overlap matrix": "OVERLAP_MATRIX",
        "confidence score": "CONFIDENCE_SCORECARD", "executive summary": "EXECUTIVE_SUMMARY",
        "sunset watch": "SUNSET_WATCH",
    }
    for term, fn in concepts.items():
        m[term] = f"{BASEURL}/reports/{fn}.html"
    m["opacity index"] = f"{BASEURL}/opacity-methodology/"
    # compile, longest-first so multi-word terms win
    compiled = []
    for term in sorted(m, key=lambda t: -len(t)):
        rx = re.compile(r"(?<![\w-])(" + re.escape(term) + r")(?![\w-])", re.I)
        compiled.append((rx, m[term]))
    return compiled

LINKS = build_link_map()
SKIP = {"a", "code", "pre", "h1", "h2", "h3", "script", "style", "table"}

def rewrite_md_links(soup: BeautifulSoup, md: Path):
    """Rewrite intra-repo relative .md links to their generated /reports/ HTML URLs so the
    existing hand-authored cross-references (and #anchors into calcs) work in /reports/."""
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if re.match(r"^[a-z]+://", href) or href.startswith("#") or href.startswith("mailto:"):
            continue
        m = re.match(r"^([^#]+\.md)(#.*)?$", href)
        if not m:
            continue
        rel, anchor = m.group(1), (m.group(2) or "")
        target = (md.parent / rel).resolve()
        try:
            target.relative_to(ANALYSIS)
            a["href"] = url_for(target) + anchor
            continue
        except ValueError:
            pass
        # root-level docs (README/TAXONOMY/about) aren't in /reports/ → send to the dashboard
        a["href"] = f"{BASEURL}/"


def rewrite_images(soup: BeautifulSoup, md: Path):
    """Point relative <img> src (e.g. charts/foo.png in analysis/) at its Pages-absolute
    URL, since /reports/ pages don't sit beside the analysis/ chart assets."""
    for img in soup.find_all("img"):
        src = img.get("src", "")
        if not src or re.match(r"^[a-z]+://", src) or src.startswith("/"):
            continue
        try:
            rel = (md.parent / src).resolve().relative_to(ROOT)
        except ValueError:
            continue
        img["src"] = f"{BASEURL}/{rel.as_posix()}"
        img["loading"] = "lazy"
        img["class"] = img.get("class", []) + ["report-img"]


def autolink(soup: BeautifulSoup, self_url: str):
    for rx, url in LINKS:
        if url == self_url:
            continue
        for node in soup.find_all(string=True):
            if any(p.name in SKIP for p in node.parents):
                continue
            mt = rx.search(str(node))
            if not mt:
                continue
            before, hit, after = str(node)[:mt.start()], mt.group(1), str(node)[mt.end():]
            a = soup.new_tag("a", href=url); a["class"] = "xref"; a.string = hit
            parent = node.parent
            idx = parent.contents.index(node)
            node.extract()
            frag = []
            if before:
                frag.append(NavigableString(before))
            frag.append(a)
            if after:
                frag.append(NavigableString(after))
            for j, f in enumerate(frag):
                parent.insert(idx + j, f)
            break  # link this term once per page

# ── front matter + markdown ──────────────────────────────────────────────────
def split_front_matter(text: str):
    fm = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            for line in text[3:end].splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip().strip('"').strip("'")
            text = text[end + 4:]
    return fm, text.lstrip("\n")

def first_h1(md_text: str):
    m = re.search(r"^#\s+(.+)$", md_text, re.M)
    return m.group(1).strip() if m else None

# ── stat chips + chart from data.json ────────────────────────────────────────
def chips_and_chart(md: Path):
    """Return (chips_html, chart_html) for REPORT pages that have a data.json."""
    if md.name != "REPORT.md":
        return "", ""
    dj = md.parent / "data.json"
    if not dj.exists():
        return "", ""
    try:
        d = json.loads(dj.read_text())
    except Exception:
        return "", ""
    chips, chart = [], ""
    # category page
    if "slug" in d:
        name = SLUG_TO_NAME.get(d["slug"], d.get("category", ""))
        c = CANON.get(name, {})
        if "tps" in c:
            tps_txt = f"{c['tps']:g}" if c["tps"] < 10 else f"{c['tps']:,.0f}"
            chips.append(("TPS", tps_txt, "blue"))
        if "confidence" in c:
            cls = "green" if c["confidence"] > 70 else "amber" if c["confidence"] >= 50 else "red"
            chips.append(("Confidence", str(c["confidence"]), cls))
        if "opacity" in c:
            oc = "red" if c["opacity"] >= 60 else "amber" if c["opacity"] >= 45 else "green"
            chips.append(("Opacity", str(c["opacity"]), oc))
        if "rank" in c:
            chips.append(("TPS rank", f"#{c['rank']}/{CANON['_total_cats']}", ""))
        # peer chart: this category vs same-sector peers by TPS
        sector = c.get("sector")
        peers = sorted([(n, CANON[n]["tps"]) for n in CANON
                        if isinstance(CANON[n], dict) and CANON[n].get("sector") == sector and "tps" in CANON[n]],
                       key=lambda x: -x[1])
        if len(peers) > 1:
            labels = [p[0] for p in peers]
            vals = [p[1] for p in peers]
            colors = ["#3b82f6" if n == name else "#334155" for n in labels]
            chart = chart_block(f"{sector} — TPS by category (log scale)", labels, vals, colors, log=True)
    else:
        # deep-dive / regional page
        for key, label, cls in [("total_tps_contribution", "TPS contribution", "blue"),
                                 ("share_of_global_tps", "Share of global", "green")]:
            if key in d:
                v = d[key]
                chips.append((label, f"{v:,.0f}" if isinstance(v, (int, float)) else str(v), cls))
        conf = (d.get("confidence") or {}).get("score")
        if conf:
            cls = "green" if conf > 70 else "amber" if conf >= 50 else "red"
            chips.append(("Confidence", str(conf), cls))
        cats = d.get("categories")
        if isinstance(cats, dict) and cats:
            labels, vals = [], []
            for k, v in cats.items():
                tv = v.get("me_tps") or v.get("africa_tps") or v.get("tps") if isinstance(v, dict) else None
                if tv:
                    labels.append(k.replace("-", " ").title()); vals.append(tv)
            if labels:
                chart = chart_block("Regional TPS by category", labels, vals,
                                    ["#3b82f6"] * len(labels), log=False)
    chips_html = ""
    if chips:
        chips_html = '<div class="chips">' + "".join(
            f'<div class="chip"><div class="k">{k}</div><div class="v {cls}">{v}</div></div>'
            for k, v, cls in chips) + "</div>"
    return chips_html, chart

_CHART_ID = [0]
def chart_block(title, labels, values, colors, log=False):
    _CHART_ID[0] += 1
    cid = f"chart{_CHART_ID[0]}"
    cfg = {
        "type": "bar",
        "data": {"labels": labels, "datasets": [{"data": values, "backgroundColor": colors,
                 "borderRadius": 4, "borderWidth": 0}]},
        "options": {
            "indexAxis": "y", "responsive": True, "maintainAspectRatio": False,
            "plugins": {"legend": {"display": False}},
            "scales": {
                "x": ({"type": "logarithmic"} if log else {}) | {"grid": {"color": "rgba(148,163,184,0.1)"},
                      "ticks": {"color": "#9ca3af"}},
                "y": {"grid": {"display": False}, "ticks": {"color": "#cbd5e1", "font": {"size": 11}}},
            },
        },
    }
    return (f'<div class="chart-box"><h3>{title}</h3><div class="chart-canvas">'
            f'<canvas id="{cid}"></canvas></div></div>'
            f'<script>new Chart(document.getElementById("{cid}"),{json.dumps(cfg)});</script>')

# ── related links (siblings: calcs / methodology / report) ───────────────────
def related_links(md: Path):
    links = []
    d = md.parent
    if md.name != "REPORT.md" and (d / "REPORT.md").exists():
        links.append(("← Category report", url_for(d / "REPORT.md")))
    if md.name == "REPORT.md":
        meth = d / "METHODOLOGY.md"
        if meth.exists():
            links.append(("Methodology", url_for(meth)))
        wk = d / "workings"
        if wk.exists():
            for w in sorted(wk.glob("*.md")):
                links.append(("⚙ " + w.stem.replace("_", " ").replace("-", " "), url_for(w)))
    # a workings page → offer siblings
    if d.name == "workings":
        rep = d.parent / "REPORT.md"
        if rep.exists() and md.name != "REPORT.md":
            links.append(("← Back to report", url_for(rep)))
    return links

# ── page template ────────────────────────────────────────────────────────────
def crumb(md: Path):
    parts = md.relative_to(ANALYSIS).parts
    items = [f'<a href="{BASEURL}/">Dashboard</a>']
    if len(parts) > 1:
        sect = SECTOR_OF_DIR.get(parts[0], parts[0].replace("-", " ").title())
        items.append(f'<span class="sep">/</span>{sect}')
    if len(parts) > 2:
        items.append(f'<span class="sep">/</span>{parts[-2].replace("-", " ").title()}')
    return "".join(items)

KIND = {"REPORT": "Report", "METHODOLOGY": "Methodology"}
def page_kind(md: Path):
    if md.parent.name == "workings":
        return "Workings · calculations"
    return KIND.get(md.stem, "Analysis")

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Universe of Finance</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}/assets/report.css">
{chartjs}</head>
<body>
<div class="topbar"><div class="inner">
  <div class="brand"><a href="{base}/">Universe of Finance</a></div>
  <a class="home-link" href="{base}/">← Interactive dashboard</a>
</div></div>
<div class="wrap">
  <div class="crumb">{crumb}</div>
  <div class="report-head"><span class="kind">{kind}</span><h1>{title}</h1></div>
  {chips}
  {chart}
  <article class="article">
{body}
  </article>
  <div class="related"><h3>Related in this repository</h3><div class="links">{related}</div></div>
  <div class="report-foot">Generated from <a href="{blob}">{src}</a> ·
    <a href="{base}/">Universe of Finance</a> · numbers link to their calculations and sources.</div>
</div>
</body></html>
"""

def build_toc(soup):
    """TOC from h2s that already carry ids (set by the markdown 'toc' extension)."""
    heads = [h for h in soup.find_all("h2") if h.get("id")]
    if len(heads) < 4:
        return ""
    items = "".join(f'<li><a href="#{h["id"]}">{h.get_text()}</a></li>' for h in heads)
    return f'<div class="toc"><div class="toc-title">On this page</div><ul>{items}</ul></div>'

def clean_title(t: str) -> str:
    t = t.strip().strip('"')
    t = re.sub(r"\s*[—-]\s*(REPORT|Report|Analysis)\s*$", "", t)
    return t

def convert(md: Path):
    raw = md.read_text()
    fm, body_md = split_front_matter(raw)
    title = clean_title(fm.get("title") or first_h1(body_md) or md.stem)
    # drop a leading H1 that duplicates the title
    body_md = re.sub(r"^#\s+.+\n", "", body_md, count=1) if first_h1(body_md) else body_md
    md_engine = markdown.Markdown(
        extensions=["tables", "fenced_code", "sane_lists", "attr_list", "footnotes", "toc"],
        extension_configs={"toc": {"permalink": False}})
    html = md_engine.convert(body_md)
    soup = BeautifulSoup(html, "html.parser")
    self_url = url_for(md)
    rewrite_md_links(soup, md)
    rewrite_images(soup, md)
    autolink(soup, self_url)
    toc = build_toc(soup)
    chips, chart = chips_and_chart(md)
    rel = related_links(md)
    related_html = "".join(f'<a href="{u}">{t}</a>' for t, u in rel) or \
        f'<a href="{BASEURL}/">← Dashboard</a>'
    desc = re.sub(r"\s+", " ", soup.get_text())[:180].strip()
    src_rel = md.relative_to(ROOT).as_posix()
    page = TEMPLATE.format(
        title=title, desc=desc.replace('"', "'"), base=BASEURL,
        chartjs='<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>' if chart else "",
        crumb=crumb(md), kind=page_kind(md), chips=chips, chart=chart,
        body=toc + str(soup), related=related_html, blob=f"{REPO_BLOB}/{src_rel}", src=src_rel,
    )
    op = out_path(md)
    op.parent.mkdir(parents=True, exist_ok=True)
    op.write_text(page)
    return op

SECTOR_ORDER = ["Payments", "Traditional Finance", "Digital Assets", "Banking", "Gaming",
                "Government", "Emerging"]

def build_hub():
    """Stylized landing page for /reports/ grouping every generated page."""
    # category reports grouped by sector
    by_sector = {s: [] for s in SECTOR_ORDER}
    deep = []
    for md in sorted(ANALYSIS.rglob("REPORT.md")):
        parts = md.relative_to(ANALYSIS).parts
        dj = md.parent / "data.json"
        title = md.parent.name.replace("-", " ").title()
        if dj.exists():
            try:
                d = json.loads(dj.read_text())
                title = d.get("category") or d.get("country") or d.get("topic") or title
            except Exception:
                pass
        title = clean_title(title)
        if parts[0] == "deep-dives":
            deep.append((title, url_for(md)))
        else:
            sect = SECTOR_OF_DIR.get(parts[0], parts[0])
            by_sector.setdefault(sect, []).append((clean_title(title), url_for(md), CANON.get(SLUG_TO_NAME.get(d.get("slug"), ""), {}) if dj.exists() else {}))
    # cross-cutting + methodology
    cross = [(md.stem.replace("_", " ").title(), url_for(md))
             for md in sorted(ANALYSIS.glob("*.md"))]
    meth = [(md.stem.replace("_", " ").title(), url_for(md))
            for md in sorted((ANALYSIS / "methodology").glob("*.md"))]

    def cat_card(t, u, c):
        chips = ""
        if c.get("tps") is not None:
            oc = "red" if c.get("opacity", 0) >= 60 else "amber" if c.get("opacity", 0) >= 45 else "green"
            chips = (f'<span class="hub-chip">{c["tps"]:,.0f} tps</span>'
                     f'<span class="hub-chip {oc}">opacity {c.get("opacity","?")}</span>')
        return f'<a class="hub-card" href="{u}"><span class="hub-t">{t}</span>{chips}</a>'

    sec_html = ""
    for s in SECTOR_ORDER:
        rows = by_sector.get(s)
        if not rows:
            continue
        rows.sort(key=lambda r: -(r[2].get("tps") or 0))
        sec_html += f'<h2>{s}</h2><div class="hub-grid">' + \
            "".join(cat_card(t, u, c) for t, u, c in rows) + "</div>"
    deep_html = '<h2>Deep Dives</h2><div class="hub-grid">' + \
        "".join(f'<a class="hub-card" href="{u}"><span class="hub-t">{t}</span></a>' for t, u in deep) + "</div>"
    cross_html = '<h2>Cross-cutting analyses</h2><div class="hub-grid">' + \
        "".join(f'<a class="hub-card" href="{u}"><span class="hub-t">{t}</span></a>' for t, u in cross) + "</div>"
    meth_html = '<h2>Methodology</h2><div class="hub-grid">' + \
        "".join(f'<a class="hub-card" href="{u}"><span class="hub-t">{t}</span></a>' for t, u in meth) + "</div>"

    page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Research Library — Universe of Finance</title>
<meta name="description" content="Every Universe of Finance report — category deep-dives, country analyses, methodology and calculations — cross-linked and stylized.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{BASEURL}/assets/report.css">
<style>
.hub-grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(230px,1fr)); gap:12px; margin:12px 0 30px; }}
.hub-card {{ display:flex; flex-direction:column; gap:8px; border:1px solid var(--card-border); background:var(--card);
  border-radius:10px; padding:14px 16px; text-decoration:none; color:var(--text); transition:border-color .15s; }}
.hub-card:hover {{ border-color:var(--accent-blue); }}
.hub-t {{ font-weight:600; font-size:0.95rem; }}
.hub-chip {{ font-family:var(--mono); font-size:0.68rem; color:var(--muted); margin-right:6px; }}
.hub-chip.red {{ color:var(--accent-red); }} .hub-chip.amber {{ color:var(--accent-amber); }} .hub-chip.green {{ color:var(--accent-green); }}
.wrap h2 {{ font-size:1.3rem; margin:34px 0 4px; padding-bottom:6px; border-bottom:1px solid var(--card-border); }}
</style></head>
<body>
<div class="topbar"><div class="inner"><div class="brand"><a href="{BASEURL}/">Universe of Finance</a></div>
<a class="home-link" href="{BASEURL}/">← Interactive dashboard</a></div></div>
<div class="wrap">
  <div class="crumb"><a href="{BASEURL}/">Dashboard</a><span class="sep">/</span>Research Library</div>
  <div class="report-head"><span class="kind">Research Library</span><h1>Every report, cross-linked</h1></div>
  <p style="color:var(--muted);max-width:680px;">29 category analyses, 11 country &amp; thematic deep dives, and the methodology behind every number — each figure links to the calculation that produced it. Opacity scores shown where available.</p>
  {sec_html}{deep_html}{cross_html}{meth_html}
</div></body></html>"""
    (OUT_ROOT / "index.html").write_text(page)

def main():
    mds = sorted(ANALYSIS.rglob("*.md"))
    n = 0
    for md in mds:
        try:
            convert(md)
            n += 1
        except Exception as e:
            print(f"[fail] {md.relative_to(ROOT)}: {e}", file=sys.stderr)
    build_hub()
    print(f"generated {n}/{len(mds)} report pages + hub under {OUT_ROOT.relative_to(ROOT)}/")

if __name__ == "__main__":
    main()
