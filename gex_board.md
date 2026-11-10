# GEX + FLOW SCAN - Tue Nov 10, 10:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.34 | +5% (1m) | **-56%** | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.28 | +50% (8m) | **-46%** | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:00:08 ET, last candle SPY 09:59, QQQ 09:59 | no errors

## Flow surges NOT fired - price disagreed (4 today, last 5)
- 10:00 NFLX CALLS: price -0.14 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AAPL CALLS: price -2.97 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 BABA CALLS: price -0.98 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 AAPL CALLS: price -2.88 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 280.68 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 78 | 11/10 280P @ 0.49 (delta 0.36) = est +34% at 280 | NEG -$781.1M | 284.16 | 285 | 270 | -$2.2M | +$57k bull / -$219k bear | SHORT (clean 36, ADX 48, RVol 2.5) |
| 2 | **AMD** | 534.28 | FLOW SURGE | **PUTS** | 56 | none: 129 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$42.5M | - | 550 | 500 | -$58.3M | +$0 bull / -$9.4M bear | out (clean 30, ADX 33, RVol 2.5) |
| 3 | **DELL** | 344.33 | FLOW SURGE | **PUTS** | 55 | none: 28 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$7.3M | - | 350 | 340 | -$938k | +$0 bull / -$104k bear | out (clean 32, ADX 30, RVol 2.2) |
| 4 | **SMH** | 490.28 | FLOW SURGE | **PUTS** | 50 | none: 117 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | NEG -$171.8M | - | 500 | 475 | -$1.7M | +$0 bull / -$399k bear | out (clean 29, ADX 27, RVol 1.3) |
| 5 | **MU** | 737.33 | FLOW SURGE | **PUTS** | 50 | none: 144 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | NEG -$1.9M | - | 750 | 750 | -$33.8M | +$568k bull / -$10.5M bear | out (clean 30, ADX 27, RVol 1.7) |
| 6 | **AAPL** | 348.01 | FLOW SURGE | **CALLS** | 49 | 11/11 352.5C @ 0.69 (delta 0.21) = est +60% at 350 | POS +$417.8M | 335.62 | 350 | 340 | +$9.1M | +$1.2M bull / +$0 bear | out (clean 28, ADX 22, RVol 1.6) |
| 7 | **TSLA** | 376.88 | TREND + FLOW | **PUTS** | 47 | none: 90 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$192.1M | - | 400 | 380 | -$8.3M | +$1.2M bull / -$6.3M bear | SHORT (clean 34, ADX 43, RVol 1.1) |
| 8 | **NFLX** | 62.78 | FLOW SURGE | **CALLS** | 46 | 11/13 64C @ 0.49 (delta 0.32) = est +28% at 63.26 | NEG -$21.5M | 65.36 | 65 | 60 | +$332k | +$29k bull / +$0 bear | out (clean 29, ADX 31, RVol 1.4) |
| 9 | **SPY** | 750.74 | FLOW SURGE | **PUTS** | 43 | none: 672 puts 0-7DTE > 53 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (300 contracts' greeks worked out here) | NEG -$5.7B | 760.61 | 750 | 750 | -$63.5M | +$1.4M bull / -$10.2M bear | out (clean 32, ADX 36, RVol 1.2) |
| 10 | **QQQ** | 679.10 | FLOW SURGE | **PUTS** | 43 | none: 753 puts 0-7DTE > 63 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (326 contracts' greeks worked out here) | NEG -$1.4B | 692.02 | 700 | 680 | -$85.2M | +$0 bull / -$7.4M bear | out (clean 31, ADX 31, RVol 0.9) |
| 11 | **MSTR** | 125.08 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 40 | none: 25 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$11.8M | 120.17 | 133 | 125 | -$310k | +$0 bull / -$425k bear | out (clean 31, ADX 27, RVol 1.1) |
| 12 | **PLTR** | 168.24 | FLOW SURGE | **PUTS** | 39 | none: 14 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$52.3M | - | 165 | 170 | -$1.2M | +$0 bull / -$709k bear | out (clean 28, ADX 36, RVol 0.7) |
| 13 | **AVGO** | 331.71 | - | **-** | 29 | - | NEG -$7.9M | 344.95 | 340 | 340 | -$4.6M | +$0 bull / -$489k bear | out (clean 31, ADX 29, RVol 2.7) |
| 14 | **AMZN** | 271.18 | - | **-** | 28 | - | POS +$476.4M | - | 270 | 265 | +$5.6M | +$464k bull / -$489k bear | out (clean 32, ADX 26, RVol 1.6) |
| 15 | **UBER** | 70.03 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$8.6M | 68.39 | 70 | 70 | +$11k | - | out (clean 32, ADX 40, RVol 0.9) |
| 16 | **ARM** | 185.30 | - | **-** | 26 | - | NEG -$4.2M | - | 185 | 190 | -$151k | - | out (clean 27, ADX 28, RVol 0.6) |
| 17 | **SMCI** | 28.64 | - | **-** | 25 | - | POS +$4.3M | - | 30 | 30 | -$148k | - | out (clean 29, ADX 28, RVol 0.6) |
| 18 | **HOOD** | 82.61 | - | **-** | 25 | - | POS +$4.9M | 78.7 | 85 | 80 | +$230k | +$0 bull / -$118k bear | out (clean 30, ADX 30, RVol 1.6) |
| 19 | **MSFT** | 542.24 | - | **-** | 23 | - | POS +$659.2M | - | 550 | 535 | +$322k | +$291k bull / -$450k bear | out (clean 33, ADX 43, RVol 1.1) |
| 20 | **GOOGL** | 291.00 | - | **-** | 23 | - | POS +$23.4M | 289.01 | 300 | 290 | +$628k | +$243k bull / -$214k bear | out (clean 30, ADX 20, RVol 2.3) |
| 21 | **CRM** | 214.30 | - | **-** | 23 | - | NEG -$10.5M | - | 195 | 220 | -$128k | - | out (clean 31, ADX 27, RVol 0.5) |
| 22 | **SHOP** | 150.81 | - | **-** | 22 | - | POS +$3.6M | 141.85 | 155 | 140 | -$11k | - | out (clean 31, ADX 34, RVol 0.5) |
| 23 | **NVDA** | 173.20 | - | **-** | 21 | - | NEG -$175.6M | - | 185 | 180 | +$2.7M | +$5.7M bull / -$3.4M bear | out (clean 32, ADX 30, RVol 3.0) |
| 24 | **BABA** | 104.30 | - | **-** | 21 | - | NEG -$3.9M | 105.85 | 110 | 105 | +$10k | +$41k bull / +$0 bear | out (clean 29, ADX 32, RVol 2.2) |
| 25 | **ORCL** | 119.33 | - | **-** | 20 | - | NEG -$22.6M | - | 130 | 120 | -$55k | +$0 bull / -$26k bear | out (clean 29, ADX 37, RVol 0.8) |
| 26 | **META** | 643.49 | - | **-** | 19 | - | POS +$263.1M | - | 650 | 650 | -$571k | +$645k bull / -$575k bear | out (clean 34, ADX 35, RVol 0.7) |
| 27 | **COIN** | 135.60 | - | **-** | 15 | - | POS +$12.3M | - | 141 | 135 | -$127k | - | out (clean 32, ADX 25, RVol 0.8) |

## Big prints this scan (211)
- **SPY** PUT 760 2026-11-13 (3DTE): 1,423 @ 12.25 = **+$1.7M** BUY | vol 8,484 / OI 5,844
- **SPY** PUT 760 2026-11-13 (3DTE): 1,002 @ 12.70 = **+$1.3M** BUY | vol 8,484 / OI 5,844
- **SPY** PUT 760 2026-11-13 (3DTE): 618 @ 12.05 = **+$745k** BUY | vol 8,484 / OI 5,844
- **AMD** CALL 550 2026-11-13 (3DTE): 499 @ 6.90 = **+$344k** SELL | vol 1,818 / OI 1,678
- **MU** PUT 710 2026-11-16 (6DTE): 100 @ 25.08 = **+$251k** BUY | vol 444 / OI 403
- **AMD** CALL 550 2026-11-16 (6DTE): 295 @ 8.43 = **+$249k** SELL | vol 1,471 / OI 126
- **AMD** CALL 550 2026-11-16 (6DTE): 295 @ 8.43 = **+$249k** SELL | vol 1,471 / OI 126
- **AMD** CALL 510 2026-11-13 (3DTE): 100 @ 23.12 = **+$231k** SELL | vol 1,163 / OI 747
- **MU** PUT 750 2026-11-13 (3DTE): 42 @ 48.00 = **+$202k** BUY | vol 89 / OI 887
- **AMD** CALL 510 2026-11-13 (3DTE): 95 @ 19.03 = **+$181k** SELL | vol 1,163 / OI 747
- **SPY** PUT 760 2026-11-13 (3DTE): 146 @ 12.05 = **+$176k** BUY | vol 8,484 / OI 5,844
- **NVDA** PUT 167.5 2026-11-13 (3DTE): 500 @ 3.40 = **+$170k** BUY | vol 3,593 / OI 1,236
- **NVDA** PUT 167.5 2026-11-13 (3DTE): 499 @ 3.28 = **+$164k** BUY | vol 3,593 / OI 1,236
- **NVDA** CALL 170 2026-11-11 (1DTE): 375 @ 4.30 = **+$161k** SELL | vol 6,823 / OI 252
- **QQQ** PUT 670 2026-11-12 (2DTE): 280 @ 5.46 = **+$153k** BUY | vol 1,809 / OI 1,092

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 763 2026-11-10 (0DTE): 3,281 traded vs OI 2,662
- **SPY** CALL 747 2026-11-11 (1DTE): 862 traded vs OI 771
- **SPY** PUT 745 2026-11-12 (2DTE): 634 traded vs OI 424
- **SPY** PUT 734 2026-11-11 (1DTE): 689 traded vs OI 316
- **SPY** CALL 750 2026-11-11 (1DTE): 3,223 traded vs OI 2,831
- **SPY** PUT 748 2026-11-12 (2DTE): 585 traded vs OI 537
- **SPY** CALL 743 2026-11-10 (0DTE): 509 traded vs OI 379
- **SPY** CALL 746 2026-11-10 (0DTE): 2,137 traded vs OI 1,836
- **SPY** PUT 722 2026-11-10 (0DTE): 628 traded vs OI 427
- **SPY** PUT 760 2026-11-13 (3DTE): 8,484 traded vs OI 5,844
- **SPY** CALL 756 2026-11-11 (1DTE): 1,206 traded vs OI 1,132
- **SPY** PUT 747 2026-11-12 (2DTE): 556 traded vs OI 405
- **SPY** PUT 733 2026-11-11 (1DTE): 567 traded vs OI 559
- **SPY** PUT 749 2026-11-12 (2DTE): 569 traded vs OI 393
- **SPY** CALL 752 2026-11-11 (1DTE): 2,165 traded vs OI 1,837

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
