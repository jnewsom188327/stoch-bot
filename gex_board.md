# GEX + FLOW SCAN - Tue Nov 10, 09:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.72 | -6% (0m) | **-6%** | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.65 | +35% (4m) | **+25%** | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:50:08 ET, last candle SPY 09:49, QQQ 09:49 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 279.80 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 77 | 11/10 278P @ 0.43 (delta 0.25) = est +72% at 278.45 | NEG -$1.1B | 284.4 | 285 | 270 | -$575k | +$57k bull / -$219k bear | SHORT (clean 36, ADX 46, RVol 3.5) |
| 2 | **AAPL** | 350.35 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 64 | none: 84 puts 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (32 contracts' greeks worked out here) | POS +$495.1M | 335.58 | 350 | 340 | +$5.5M | +$932k bull / +$0 bear | out (clean 28, ADX 24, RVol 2.1) |
| 3 | **AMZN** | 270.38 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 63 | none: 63 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$464.3M | - | 270 | 265 | +$3.9M | +$30k bull / -$299k bear | out (clean 32, ADX 25, RVol 2.4) |
| 4 | **NVDA** | 171.07 | FLOW SURGE | **CALLS** | 56 | none: 42 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$175.5M | - | 185 | 170 | +$17.7M | +$3.8M bull / +$0 bear | out (clean 32, ADX 28, RVol 3.1) |
| 5 | **AMD** | 517.42 | FLOW SURGE | **PUTS** | 55 | none: 123 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | POS +$43.0M | - | 500 | 500 | -$16.8M | +$0 bull / -$3.6M bear | out (clean 30, ADX 32, RVol 2.6) |
| 6 | **MU** | 717.95 | FLOW SURGE | **PUTS** | 55 | none: 147 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | NEG -$26.4M | - | 750 | 750 | -$14.4M | +$568k bull / -$6.2M bear | out (clean 30, ADX 30, RVol 2.0) |
| 7 | **SPY** | 748.49 | FLOW SURGE | **PUTS** | 53 | 11/10 743P @ 0.77 (delta 0.20) = est +54% at 745.65 | NEG -$7.0B | 760.85 | 750 | 730 | -$29.0M | +$0 bull / -$2.9M bear | out (clean 32, ADX 36, RVol 2.7) |
| 8 | **SMH** | 481.67 | FLOW SURGE | **PUTS** | 53 | none: 114 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$215.2M | - | 500 | 475 | -$934k | +$0 bull / -$362k bear | out (clean 29, ADX 30, RVol 1.8) |
| 9 | **META** | 640.17 | FLOW SURGE | **CALLS** | 53 | none: 153 calls 0-7DTE > 13 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (11 contracts' greeks worked out here) | POS +$239.8M | 605.09 | 650 | 650 | +$1.7M | +$240k bull / -$140k bear | SHORT (clean 34, ADX 37, RVol 2.2) |
| 10 | **GOOGL** | 288.43 | FLOW SURGE | **CALLS** | 52 | none: 69 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (18 contracts' greeks worked out here) | NEG -$15.7M | 289.52 | 300 | 290 | +$426k | +$66k bull / +$0 bear | out (clean 30, ADX 20, RVol 2.8) |
| 11 | **TSLA** | 374.87 | TREND (flow not with it) | **PUTS** | 51 | none: 90 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$182.0M | - | 400 | 380 | +$4.3M | +$120k bull / -$4.4M bear | SHORT (clean 34, ADX 44, RVol 2.0) |
| 12 | **UBER** | 70.02 | PINNED between the walls (positive gamma) - chop | **-** | 51 | - | POS +$7.8M | 68.39 | 70 | 70 | +$13k | - | out (clean 32, ADX 38, RVol 2.1) |
| 13 | **PLTR** | 167.47 | FLOW SURGE | **PUTS** | 50 | none: 13 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$49.9M | - | 165 | 170 | -$968k | +$0 bull / -$602k bear | out (clean 29, ADX 34, RVol 1.9) |
| 14 | **ORCL** | 117.96 | - | **-** | 37 | - | NEG -$24.2M | - | 120 | 120 | +$229k | +$0 bull / -$26k bear | out (clean 29, ADX 38, RVol 1.1) |
| 15 | **MSTR** | 122.62 | - | **-** | 32 | - | POS +$5.0M | 120.1 | 133 | 120 | +$721k | +$0 bull / -$104k bear | out (clean 31, ADX 26, RVol 1.8) |
| 16 | **HOOD** | 81.84 | - | **-** | 32 | - | POS +$3.4M | 79.07 | 85 | 80 | +$238k | +$0 bull / -$91k bear | out (clean 30, ADX 29, RVol 2.3) |
| 17 | **DELL** | 335.04 | - | **-** | 31 | - | NEG -$8.5M | - | 350 | 340 | -$317k | - | out (clean 33, ADX 31, RVol 2.8) |
| 18 | **BABA** | 103.70 | - | **-** | 30 | - | NEG -$6.5M | 105.97 | 110 | 100 | +$31k | - | out (clean 30, ADX 29, RVol 3.2) |
| 19 | **ARM** | 181.44 | - | **-** | 29 | - | NEG -$4.8M | - | 185 | 190 | -$90k | - | out (clean 27, ADX 29, RVol 1.8) |
| 20 | **CRM** | 214.10 | - | **-** | 29 | - | NEG -$10.1M | - | 195 | 220 | -$136k | - | out (clean 31, ADX 24, RVol 2.9) |
| 21 | **NFLX** | 62.80 | - | **-** | 27 | - | NEG -$24.1M | 65.67 | 65 | 60 | +$88k | - | out (clean 29, ADX 28, RVol 2.5) |
| 22 | **QQQ** | 673.51 | - | **-** | 26 | - | NEG -$1.9B | 691.99 | 680 | 680 | -$14.6M | +$0 bull / -$5.5M bear | out (clean 31, ADX 34, RVol 2.4) |
| 23 | **SMCI** | 28.00 | - | **-** | 26 | - | POS +$3.0M | - | 30 | 30 | -$31k | - | out (clean 29, ADX 28, RVol 1.9) |
| 24 | **MSFT** | 541.80 | - | **-** | 22 | - | POS +$644.8M | - | 550 | 535 | +$127k | +$81k bull / -$193k bear | out (clean 33, ADX 40, RVol 1.7) |
| 25 | **AVGO** | 325.82 | - | **-** | 21 | - | NEG -$19.4M | 344.75 | 340 | 320 | +$152k | +$0 bull / -$337k bear | out (clean 30, ADX 27, RVol 3.3) |
| 26 | **SHOP** | 149.89 | - | **-** | 20 | - | POS +$2.8M | 143.29 | 155 | 140 | -$5k | - | out (clean 32, ADX 34, RVol 1.5) |
| 27 | **COIN** | 133.25 | - | **-** | 15 | - | POS +$5.4M | 128.42 | 137 | 135 | +$40k | - | out (clean 32, ADX 24, RVol 2.1) |

## Big prints this scan (405)
- **TSLA** CALL 357.5 2026-11-13 (3DTE): 420 @ 18.32 = **+$769k** SELL | vol 501 / OI 2,514
- **AMD** CALL 495 2026-11-11 (1DTE): 500 @ 15.20 = **+$760k** SELL | vol 547 / OI 166
- **TSLA** CALL 360 2026-11-13 (3DTE): 420 @ 16.35 = **+$687k** SELL | vol 611 / OI 3,304
- **MU** PUT 685 2026-11-13 (3DTE): 300 @ 15.45 = **+$464k** BUY | vol 347 / OI 1,144
- **MU** CALL 715 2026-11-11 (1DTE): 250 @ 18.00 = **+$450k** SELL | vol 465 / OI 244
- **QQQ** PUT 675 2026-11-11 (1DTE): 500 @ 7.60 = **+$380k** BUY | vol 3,416 / OI 627
- **QQQ** PUT 675 2026-11-11 (1DTE): 500 @ 7.28 = **+$364k** BUY | vol 3,416 / OI 627
- **QQQ** PUT 675 2026-11-11 (1DTE): 500 @ 6.83 = **+$342k** BUY | vol 3,416 / OI 627
- **TSLA** PUT 375 2026-11-11 (1DTE): 500 @ 6.55 = **+$328k** BUY | vol 3,414 / OI 346
- **AMD** PUT 505 2026-11-13 (3DTE): 172 @ 17.15 = **+$295k** BUY | vol 253 / OI 276
- **AAPL** CALL 345 2026-11-13 (3DTE): 297 @ 9.10 = **+$270k** BUY | vol 411 / OI 6,919
- **QQQ** PUT 670 2026-11-11 (1DTE): 500 @ 5.23 = **+$262k** BUY | vol 5,194 / OI 452
- **SPY** PUT 747 2026-11-10 (0DTE): 994 @ 2.51 = **+$249k** BUY | vol 20,580 / OI 315
- **QQQ** PUT 670 2026-11-11 (1DTE): 500 @ 4.98 = **+$249k** BUY | vol 5,194 / OI 452
- **MU** PUT 720 2026-11-13 (3DTE): 80 @ 30.80 = **+$246k** BUY | vol 135 / OI 1,457

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 750 2026-11-10 (0DTE): 9,511 traded vs OI 8,042
- **SPY** CALL 763 2026-11-11 (1DTE): 2,140 traded vs OI 744
- **SPY** PUT 729 2026-11-11 (1DTE): 4,031 traded vs OI 401
- **SPY** PUT 744 2026-11-11 (1DTE): 601 traded vs OI 321
- **SPY** PUT 749 2026-11-11 (1DTE): 800 traded vs OI 282
- **SPY** PUT 746 2026-11-11 (1DTE): 1,145 traded vs OI 425
- **SPY** PUT 731 2026-11-10 (0DTE): 1,172 traded vs OI 719
- **SPY** PUT 730 2026-11-10 (0DTE): 6,921 traded vs OI 2,041
- **SPY** CALL 751 2026-11-10 (0DTE): 5,549 traded vs OI 2,011
- **SPY** CALL 755 2026-11-11 (1DTE): 2,179 traded vs OI 1,025
- **SPY** PUT 747 2026-11-11 (1DTE): 1,617 traded vs OI 301
- **SPY** CALL 753 2026-11-10 (0DTE): 7,705 traded vs OI 4,951
- **SPY** CALL 747 2026-11-10 (0DTE): 2,420 traded vs OI 884
- **SPY** PUT 752 2026-11-11 (1DTE): 652 traded vs OI 281
- **SPY** PUT 706 2026-11-10 (0DTE): 850 traded vs OI 843

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
