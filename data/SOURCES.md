---
title: "Data Sources — Live Layer"
layout: default
---

# Live Layer — Data Sources

Every feed the site renders, with its URL, cadence, method, license, and fetch-viability.
This is the audit trail for the **measured** half of the Universe of Finance. Where a feed
*cannot* be fetched cleanly, that refusal is documented here — an unfetchable feed is itself
an opacity signal.

Payload contract (every feed): `value · unit · source_url · retrieved_at · period_covered · method`.
`method` ∈ { `ledger`, `api`, `published_stat`, `estimate` }.

---

## Tier 1 — Exact, real-time (ledger-verified)

Fetched **server-side** by `tools/fetch_live_data.py` in GitHub Actions (no CORS limits on
the runner) every 15 minutes → committed to `data/live/chains.json`. Bitcoin is *also*
fetched **client-side** from the browser (mempool.space sends permissive CORS headers) to
upgrade its badge to true "seconds ago" liveness.

| Feed | Endpoint | Method | Cadence | License / notes |
|------|----------|--------|---------|-----------------|
| **Bitcoin** | `https://mempool.space/api/v1/blocks` | ledger | 15 min + client-side | mempool.space open API; CORS-friendly. TPS from tx count over recent block span. |
| **Ethereum** | `https://ethereum-rpc.publicnode.com` (`eth_getBlockByNumber`) | ledger | 15 min | PublicNode free RPC, keyless. TPS from latest block tx count ÷ block time. |
| **Solana** | `https://api.mainnet-beta.solana.com` (`getRecentPerformanceSamples`) | ledger | 15 min | Solana public RPC, keyless. Reports **total** TPS incl. consensus votes; `non_vote_tps` also captured. |
| **Radix** | `https://mainnet.radixdlt.com/stream/transactions` | ledger | 15 min | Babylon Gateway public API, keyless. TPS from recent transaction-stream span. |
| **XRP Ledger** | `https://xrplcluster.com` (`ledger` method) | ledger | 15 min | Community full-history cluster, keyless. TPS from latest validated ledger tx count ÷ ~4s close. |

**Verification (2026-07):** all five endpoints returned real data on test — BTC ~3.7 tps,
ETH ~120 tps, Solana ~3,266 tps (~1,582 non-vote), Radix ~0.4 tps, XRPL ~6 tps.

**Graceful degradation:** if any endpoint is unreachable at fetch time, the script keeps the
**last committed value** and flags it `stale` with `last_error`/`last_attempt`. Never blank,
never fabricated.

---

## Tier 2 — Exact, published on a lag (RTP & wholesale systems)

These systems publish **exact** counts — but monthly or annually, not live. That lag is the
content: the badges read "as of 2024/2025 · N days stale". Curated in
`data/published/systems.json`, TPS annualized to a calendar-second basis for comparability.

| Feed | Source | Method | Latest figure | Fetch viability |
|------|--------|--------|---------------|-----------------|
| **UPI (India)** | [NPCI product statistics](https://www.npci.org.in/what-we-do/upi/product-statistics) | published_stat | 228.3B txns (2025); Dec 2025 = 21.63B/mo | HTML page, no clean JSON API. Monthly, ~10-day lag. **Manual.** |
| **Pix (Brazil)** | [BCB Pix statistics](https://www.bcb.gov.br/en/financialstability/pixstatistics) | published_stat | 79.8B txns (2025), R$35.36T | Open OData API exists (`olinda.bcb.gov.br/.../Pix_DadosAbertos`) **but returned HTTP 400/500 on verification 2026-07** — not stable enough to ship. **Manual** until fixed. *(API instability = opacity signal.)* |
| **UK Faster Payments** | [Pay.UK](https://www.wearepay.uk/what-we-do/payment-systems/faster-payment-system/) | published_stat | ~5.2B/yr (2024); Sept 2024 = 430M/mo | Monthly PDF/HTML. **Manual.** |
| **Fedwire Funds** | [FRB Services annual stats](https://www.frbservices.org/resources/financial-services/wires/volume-value-stats/annual-stats.html) | published_stat | ~210.7M/yr (2024); 836,322 txns/day | Annual publication → a full-year lag is structural. **Manual.** |

### Tier-2 candidates evaluated, not yet integrated
- **TIPS (ECB)** — volumes available via ECB Data Portal; growing fast (+402% YoY per prior
  UoF research) but small absolute count. Needs endpoint verification before integration.
- **CHIPS (The Clearing House)** — annual stats published as PDF; ~$1.8Q/yr value, low count.
  No machine-readable feed found. Candidate for a manual `published_stat` row.

---

## Tier 3 — Aggregates only (the dark half)

No live feed exists — that absence **is** the exhibit. These appear in the leaderboard as
period-2024 estimates with "as of 2024" data-age badges and high opacity scores (see the
Opacity Index). Examples: card-network volumes (Visa/Mastercard quarterly earnings
aggregates), cash (≈ unmeasured), informal/hawala transfers (≈ unmeasured), China WMPs.

---

## Refusals & limits (documented on purpose)

- **BCB Olinda Pix OData API** — returned HTTP 400/500 on `$top`/`$orderby` queries during
  verification (2026-07-20). Shipped as a manual figure rather than a fragile fetcher.
- **NAIC Statistical Compilation** (US insurance claims counts) — paywalled (~$500+). Cannot
  fetch; insurance-claims figures remain modeled estimates (see the Insurance Claims deep dive).
- **No ToS-violating scraping.** Where a system publishes only rendered HTML/PDF with no open
  data endpoint, it is curated manually from the cited page, not scraped programmatically.

---

*Cadence summary: Tier-1 chains every 15 min (Actions) + client-side live for Bitcoin;
Tier-2 published stats checked manually against primary sources. Opacity Index recomputes on
any data change.*
