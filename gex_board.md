# GEX + FLOW SCAN - Mon Nov 09, 11:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:04 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/09 754C | 0.41 | 0.26 | -2% (0m) | **-37%** | +28% | 752.23 |
| 10:35 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 272.5C | 0.49 | 0.12 | +2% (2m) | **-76%** | +225% | 273.49 |
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.72 | +51% (23m) | **-6%** (done) | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.02 | +13% (6m) | **-96%** (done) | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:10:08 ET, last candle SPY 11:09, QQQ 11:09 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:03 | SPY | 1m WHIPSAW | R1 | CALLS | TURNING away | **FIRE** SPY261109C00754000 |

## Flow surges NOT fired - price disagreed (17 today, last 5)
- 10:55 AVGO PUTS: price +2.40 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 AVGO PUTS: price +1.16 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 QQQ PUTS: price +0.45 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:35 AVGO PUTS: price +1.05 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:30 QQQ PUTS: price +0.53 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AVGO** | 319.77 | FLOW SURGE | **PUTS** | 48 | none: 100 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (45 contracts' greeks worked out here) | NEG -$65.0M | - | 340 | 320 | -$9.0M | +$0 bull / -$519k bear | out (clean 31, ADX 68, RVol 1.4) |
| 2 | **COIN** | 138.86 | FLOW SURGE | **PUTS** | 47 | none: 27 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$5.9M | - | 140 | 140 | -$2.4M | +$0 bull / -$300k bear | out (clean 32, ADX 29, RVol 0.8) |
| 3 | **AMD** | 501.34 | FLOW SURGE | **PUTS** | 46 | none: 160 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (74 contracts' greeks worked out here) | POS +$16.1M | 483.86 | 500 | 500 | -$56.1M | +$0 bull / -$2.7M bear | out (clean 33, ADX 57, RVol 2.0) |
| 4 | **TSLA** | 379.25 | PINNED between the walls (positive gamma) - chop | **-** | 45 | - | POS +$119.8M | - | 380 | 380 | -$98.1M | +$526k bull / -$666k bear | LONG (clean 35, ADX 48, RVol 0.5) |
| 5 | **QQQ** | 676.83 | FLOW SURGE | **PUTS** | 43 | 11/09 672P @ 0.78 (delta 0.22) = est +101% at 673.08 | NEG -$2.2B | 699.93 | 680 | 680 | -$252.9M | +$1.1M bull / -$2.5M bear | out (clean 33, ADX 50, RVol 0.9) |
| 6 | **IWM** | 280.83 | FLOW SURGE | **PUTS** | 43 | 11/09 281P @ 0.74 (delta 0.54) = est +74% at 279.77 | NEG -$1.1B | 285.14 | 285 | 270 | -$18.9M | +$0 bull / -$506k bear | out (clean 34, ADX 55, RVol 0.6) |
| 7 | **META** | 640.81 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 42 | none: 204 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (72 contracts' greeks worked out here) | POS +$170.3M | 614.71 | 650 | 640 | -$8.1M | +$0 bull / -$371k bear | out (clean 33, ADX 42, RVol 0.8) |
| 8 | **MSFT** | 540.96 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 40 | none: 176 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (73 contracts' greeks worked out here) | POS +$566.2M | - | 550 | 540 | +$3.0M | +$66k bull / -$42k bear | out (clean 34, ADX 33, RVol 0.6) |
| 9 | **SMH** | 484.69 | - | **-** | 34 | - | NEG -$220.3M | - | 500 | 475 | -$3.9M | +$72k bull / +$0 bear | out (clean 32, ADX 48, RVol 1.8) |
| 10 | **SPY** | 750.56 | - | **-** | 30 | - | NEG -$6.8B | 761.87 | 750 | 740 | -$252.0M | +$2.6M bull / -$1.9M bear | out (clean 33, ADX 52, RVol 0.8) |
| 11 | **PLTR** | 170.13 | - | **-** | 29 | - | POS +$11.8M | - | 165 | 180 | -$4.1M | +$0 bull / -$504k bear | out (clean 30, ADX 51, RVol 1.0) |
| 12 | **NVDA** | 176.89 | - | **-** | 28 | - | NEG -$194.6M | - | 190 | 190 | -$61.5M | +$1.2M bull / -$1.8M bear | out (clean 32, ADX 38, RVol 3.5) |
| 13 | **HOOD** | 84.76 | - | **-** | 27 | - | NEG -$1.3M | - | 85 | 85 | -$3.0M | +$90k bull / -$123k bear | out (clean 30, ADX 62, RVol 0.6) |
| 14 | **AMZN** | 268.47 | - | **-** | 26 | - | POS +$384.7M | - | 270 | 265 | +$19.1M | +$401k bull / +$0 bear | out (clean 35, ADX 27, RVol 0.7) |
| 15 | **MSTR** | 128.26 | - | **-** | 25 | - | POS +$4.6M | - | 135 | 135 | -$3.2M | +$0 bull / -$133k bear | out (clean 30, ADX 24, RVol 0.9) |
| 16 | **AAPL** | 350.90 | - | **-** | 23 | - | POS +$455.0M | 339.2 | 350 | 350 | -$8.5M | +$833k bull / -$74k bear | out (clean 28, ADX 43, RVol 0.5) |
| 17 | **MU** | 739.34 | - | **-** | 23 | - | POS +$1.3M | 735.86 | 750 | 750 | -$33.6M | +$0 bull / -$6.6M bear | out (clean 33, ADX 48, RVol 0.8) |
| 18 | **ARM** | 188.46 | - | **-** | 22 | - | NEG -$4.5M | - | 185 | 190 | +$76k | +$42k bull / +$0 bear | out (clean 27, ADX 55, RVol 1.6) |
| 19 | **GOOGL** | 292.55 | - | **-** | 21 | - | POS +$18.3M | 288.74 | 300 | 290 | +$2.7M | +$26k bull / +$0 bear | out (clean 31, ADX 31, RVol 1.0) |
| 20 | **DELL** | 352.56 | - | **-** | 17 | - | NEG -$6.0M | - | 350 | 340 | -$1.0M | - | out (clean 32, ADX 51, RVol 0.6) |
| 21 | **SMCI** | 29.39 | - | **-** | 17 | - | POS +$11k | 28.72 | 30 | 30 | -$990k | - | out (clean 31, ADX 16, RVol 0.7) |
| 22 | **ORCL** | 118.92 | - | **-** | 11 | - | NEG -$26.0M | - | 125 | 125 | -$789k | - | out (clean 30, ADX 33, RVol 0.5) |
| 23 | **UBER** | 69.58 | - | **-** | 11 | - | POS +$1.6M | 69.17 | 70 | 65 | -$68k | - | out (clean 30, ADX 27, RVol 0.8) |
| 24 | **SHOP** | 150.54 | - | **-** | 10 | - | POS +$1.9M | - | 150 | 140 | -$53k | - | out (clean 35, ADX 14, RVol 0.3) |
| 25 | **BABA** | 105.47 | - | **-** | 9 | - | POS +$2.8M | 103.93 | 110 | 110 | +$109k | - | out (clean 31, ADX 36, RVol 0.7) |
| 26 | **NFLX** | 63.72 | - | **-** | 8 | - | NEG -$20.1M | - | 65 | 65 | +$115k | - | out (clean 31, ADX 18, RVol 0.8) |
| 27 | **CRM** | 214.59 | - | **-** | 8 | - | NEG -$11.0M | - | 195 | 220 | +$16k | - | out (clean 34, ADX 20, RVol 1.0) |

## Big prints this scan (137)
- **SPY** CALL 740 2026-11-10 (1DTE): 1,000 @ 12.00 = **+$1.2M** BUY | vol 3,792 / OI 11,269
- **SPY** PUT 749 2026-11-09 (0DTE): 4,690 @ 1.00 = **+$469k** SELL | vol 92,563 / OI 351
- **MU** CALL 750 2026-11-11 (2DTE): 200 @ 15.60 = **+$312k** SELL | vol 2,183 / OI 955
- **QQQ** PUT 674 2026-11-12 (3DTE): 464 @ 6.56 = **+$304k** SELL | vol 1,303 / OI 86
- **SPY** PUT 744 2026-11-12 (3DTE): 863 @ 3.12 = **+$269k** SELL | vol 10,383 / OI 211
- **MU** CALL 737.5 2026-11-09 (0DTE): 340 @ 6.80 = **+$231k** SELL | vol 4,572 / OI 111
- **AMD** PUT 525 2026-11-09 (0DTE): 85 @ 27.06 = **+$230k** BUY | vol 100 / OI 0
- **MU** CALL 730 2026-11-09 (0DTE): 200 @ 10.60 = **+$212k** SELL | vol 17,912 / OI 259
- **SPY** PUT 756 2026-11-09 (0DTE): 398 @ 5.15 = **+$205k** SELL | vol 12,703 / OI 382
- **MU** CALL 750 2026-11-11 (2DTE): 117 @ 15.72 = **+$184k** SELL | vol 2,183 / OI 955
- **SPY** PUT 750 2026-11-13 (4DTE): 280 @ 6.04 = **+$169k** MID | vol 3,570 / OI 5,645
- **QQQ** PUT 676 2026-11-09 (0DTE): 899 @ 1.86 = **+$167k** SELL | vol 14,929 / OI 98
- **MU** CALL 732.5 2026-11-09 (0DTE): 200 @ 7.80 = **+$156k** SELL | vol 7,036 / OI 153
- **MU** CALL 735 2026-11-13 (4DTE): 51 @ 30.55 = **+$156k** SELL | vol 836 / OI 179
- **NVDA** PUT 185 2026-11-11 (2DTE): 200 @ 7.52 = **+$150k** SELL | vol 1,919 / OI 2,107

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 703 2026-11-11 (2DTE): 500 traded vs OI 197
- **SPY** PUT 733 2026-11-11 (2DTE): 562 traded vs OI 297
- **SPY** CALL 747 2026-11-13 (4DTE): 1,749 traded vs OI 1,737
- **SPY** PUT 745 2026-11-12 (3DTE): 643 traded vs OI 372
- **SPY** CALL 763 2026-11-11 (2DTE): 504 traded vs OI 387
- **SPY** PUT 754 2026-11-09 (0DTE): 1,279 traded vs OI 1,253
- **SPY** PUT 700 2026-11-09 (0DTE): 5,774 traded vs OI 5,259
- **SPY** PUT 738 2026-11-11 (2DTE): 1,621 traded vs OI 1,480
- **SPY** PUT 750 2026-11-16 (7DTE): 624 traded vs OI 502
- **SPY** PUT 748 2026-11-16 (7DTE): 536 traded vs OI 192
- **SPY** CALL 743 2026-11-16 (7DTE): 500 traded vs OI 108
- **SPY** PUT 712 2026-11-16 (7DTE): 951 traded vs OI 175
- **SPY** PUT 716 2026-11-30 (21DTE): 4,009 traded vs OI 487
- **SPY** CALL 745 2026-11-30 (21DTE): 1,009 traded vs OI 1,004
- **SPY** PUT 714 2026-11-30 (21DTE): 2,003 traded vs OI 669

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
