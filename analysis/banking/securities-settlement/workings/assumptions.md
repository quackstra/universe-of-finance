# Securities Settlement — Assumptions

## Scope Assumptions

1. **Settlement vs. clearing**: We count settlement transactions (final transfer of securities ownership and cash), not clearing transactions (trade matching, netting, risk management). NSCC clears; DTC settles. In practice, the NSCC-to-DTC flow is tightly coupled, so the distinction matters mainly for avoiding double-counting.

2. **Netting**: Euroclear reports "netted transactions" (331M). NSCC's CNS system nets extensively — a single net settlement instruction may represent 5-10 underlying trades. We use netted/settled counts, not gross trade counts.

3. **Downstream relationship**: Securities settlement is downstream of trading. The equity-markets capsule covers ~150M+ daily trades globally. After netting, these result in ~5-6M daily settlement instructions across all infrastructure. This is by design — settlement is a compression layer.

4. **DVP cash legs excluded**: Delivery-versus-payment settlement has two legs: securities delivery and cash payment. We count only the securities delivery leg here. The cash leg is counted in the interbank-rtgs capsule (e.g., the ~70 daily NSS transfers from DTCC).

## Data Assumptions

5. **DTCC transaction count**: DTCC does not publish a single headline annual transaction count across all subsidiaries. We estimate ~500M from:
   - DTC: ~1.3M deliveries/day × 250 = 325M
   - Additional NSCC/FICC settlement activity
   - ATP: >350M/year (but overlaps with DTC)
   The range could be 400M-600M.

6. **Euroclear transaction count**: Confirmed at 331M from the 2024 annual results press release. This is the most reliable number in our dataset.

7. **Clearstream annualization**: We extrapolate from 5-month YTD data (98.1M through May 2024) to ~235M annual. This assumes roughly even distribution, though Q4 typically has higher settlement volumes. The estimate could be 200-250M.

8. **T2S overlap**: T2S settles euro-denominated securities and is used by both Euroclear and Clearstream for their euro CSD operations. We estimate ~100M of the ~165M T2S transactions overlap with Euroclear/Clearstream counts. This is a significant source of uncertainty.

9. **DTCC $3.7 quadrillion**: This figure comes from multiple 2025 press reports (Yahoo Finance, Decrypt, Daily Crypto Briefs) all citing DTCC. The 2023 figure was ~$3.0Q (from DTCC 2023 annual report), so $3.7Q represents ~23% growth, consistent with strong 2024 equity markets.

## FX Rate Assumptions

10. **EUR/USD = 1.09**: Used for Euroclear (€1,162T → $1,267T) and Clearstream conversions.

## Projection Assumptions

11. **5% baseline volume CAGR**: Based on Euroclear's confirmed 5.8% CAGR and assumed DTCC volume growth of ~4-5%. Slightly above RTGS growth because securities settlement benefits from:
    - Growth in exchange-traded products (ETFs)
    - Fractional share settlement
    - Emerging market CSD development

12. **8% baseline value CAGR**: Value grows faster due to equity price appreciation, increased government debt issuance, and nominal GDP growth. The 13.1% DTCC value CAGR is unsustainable; we use 8% as a moderated long-term rate.

13. **T+0 not in baseline**: True T+0 (same-day or atomic settlement) would fundamentally change settlement infrastructure. It could either increase transaction counts (if netting windows shrink) or decrease them (if blockchain-based atomic settlement eliminates batch processing). Not modeled in baseline.

## Double-Counting Notes

14. **Settlement vs. trading**: A single equity trade → 1 clearing instruction → typically contributes to 1 net settlement instruction (after CNS netting). We count at the settlement layer.

15. **DTCC value vs. Euroclear value**: These are additive (different markets/geographies) but the total $5Q+ figure should be treated as indicative, not precise, due to:
    - Cross-listed securities settled in multiple CSDs
    - Bridge settlements between Euroclear and Clearstream
    - Repo and securities lending generate additional settlement transactions from the same underlying securities

16. **Relationship to equity-markets capsule**: If equity-markets reports ~40B annual trades, and securities settlement reports ~1.4B transactions, the implied netting ratio is ~28:1. This is plausible — CNS nets aggressively, especially for highly liquid large-cap equities.
