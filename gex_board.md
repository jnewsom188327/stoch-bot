# GEX + FLOW SCAN - Tue Nov 10, 10:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.26 | +5% (1m) | **-66%** | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.27 | +50% (8m) | **-48%** | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:10:08 ET, last candle SPY 10:09, QQQ 10:09 | no errors

## Flow surges NOT fired - price disagreed (5 today, last 5)
- 10:10 BABA PUTS: price +0.73 over the last 15 min - flow says one way, price says the other
- 10:00 NFLX CALLS: price -0.14 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AAPL CALLS: price -2.97 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 BABA CALLS: price -0.98 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 AAPL CALLS: price -2.88 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 280.97 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 64 | 11/10 280P @ 0.52 (delta 0.33) = est +49% at 280 | NEG -$785.6M | 284.21 | 285 | 270 | -$2.9M | - | SHORT (clean 36, ADX 45, RVol 2.0) |
| 2 | **AMD** | 536.27 | FLOW SURGE | **PUTS** | 56 | none: 126 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | POS +$41.4M | - | 550 | 500 | -$85.6M | +$0 bull / -$7.0M bear | out (clean 31, ADX 35, RVol 2.6) |
| 3 | **AVGO** | 333.52 | FLOW SURGE | **PUTS** | 53 | none: 78 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$4.2M | 328.61 | 340 | 340 | -$13.3M | +$0 bull / -$602k bear | out (clean 31, ADX 33, RVol 2.9) |
| 4 | **SMH** | 491.86 | FLOW SURGE | **PUTS** | 50 | none: 117 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$179.7M | - | 500 | 475 | -$2.8M | +$0 bull / -$698k bear | out (clean 29, ADX 26, RVol 1.2) |
| 5 | **BABA** | 104.61 | FLOW SURGE | **PUTS** | 50 | 11/13 101P @ 0.66 (delta 0.22) = est +23% at 103.79 | NEG -$1.7M | 105.06 | 110 | 105 | -$485k | +$0 bull / -$134k bear | out (clean 29, ADX 31, RVol 1.7) |
| 6 | **MU** | 741.60 | FLOW SURGE | **PUTS** | 48 | none: 145 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | NEG -$779k | 758.38 | 750 | 750 | -$55.6M | +$0 bull / -$6.1M bear | out (clean 30, ADX 25, RVol 1.3) |
| 7 | **AAPL** | 347.98 | FLOW SURGE | **CALLS** | 46 | none: 84 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (28 contracts' greeks worked out here) | POS +$414.9M | 335.88 | 350 | 340 | +$13.1M | +$370k bull / +$0 bear | out (clean 28, ADX 21, RVol 1.4) |
| 8 | **GOOGL** | 289.92 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 43 | none: 69 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$13.0M | 288.83 | 300 | 290 | -$18k | +$0 bull / -$69k bear | out (clean 30, ADX 19, RVol 2.1) |
| 9 | **SPY** | 751.80 | FLOW SURGE | **PUTS** | 42 | none: 672 puts 0-7DTE > 51 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (255 contracts' greeks worked out here) | NEG -$5.5B | 761.21 | 750 | 750 | -$91.4M | +$0 bull / -$12.8M bear | out (clean 32, ADX 32, RVol 1.0) |
| 10 | **QQQ** | 679.76 | FLOW SURGE | **PUTS** | 42 | none: 753 puts 0-7DTE > 66 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (248 contracts' greeks worked out here) | NEG -$1.5B | 693.37 | 700 | 680 | -$137.9M | +$0 bull / -$1.2M bear | out (clean 31, ADX 28, RVol 0.8) |
| 11 | **TSLA** | 376.13 | TREND + FLOW | **PUTS** | 42 | none: 90 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$192.3M | - | 400 | 380 | -$7.7M | +$379k bull / -$3.2M bear | SHORT (clean 34, ADX 41, RVol 0.8) |
| 12 | **UBER** | 70.11 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$9.1M | 68.44 | 70 | 70 | -$33k | - | out (clean 32, ADX 40, RVol 0.8) |
| 13 | **PLTR** | 168.18 | - | **-** | 27 | - | POS +$53.2M | - | 165 | 170 | -$963k | +$26k bull / -$27k bear | out (clean 28, ADX 37, RVol 0.4) |
| 14 | **DELL** | 343.48 | - | **-** | 25 | - | NEG -$7.5M | - | 350 | 340 | -$855k | +$0 bull / -$107k bear | out (clean 32, ADX 27, RVol 1.2) |
| 15 | **SMCI** | 28.75 | - | **-** | 25 | - | POS +$4.2M | - | 30 | 30 | -$179k | - | out (clean 29, ADX 25, RVol 0.5) |
| 16 | **NVDA** | 174.07 | - | **-** | 23 | - | NEG -$175.8M | - | 185 | 180 | -$11.6M | +$0 bull / -$6.3M bear | out (clean 32, ADX 29, RVol 3.0) |
| 17 | **META** | 644.98 | - | **-** | 21 | - | POS +$274.7M | - | 650 | 650 | -$2.0M | +$0 bull / -$340k bear | out (clean 33, ADX 32, RVol 0.7) |
| 18 | **AMZN** | 272.13 | - | **-** | 21 | - | POS +$483.4M | - | 270 | 265 | +$2.7M | +$104k bull / -$443k bear | out (clean 32, ADX 29, RVol 1.2) |
| 19 | **NFLX** | 62.94 | - | **-** | 21 | - | NEG -$22.0M | 65.24 | 65 | 60 | -$187k | +$29k bull / -$66k bear | out (clean 30, ADX 32, RVol 1.1) |
| 20 | **ARM** | 184.15 | - | **-** | 21 | - | NEG -$4.3M | - | 185 | 190 | -$145k | - | out (clean 27, ADX 25, RVol 0.7) |
| 21 | **MSFT** | 543.09 | - | **-** | 20 | - | POS +$690.0M | - | 550 | 535 | -$51k | +$77k bull / -$52k bear | out (clean 33, ADX 42, RVol 1.1) |
| 22 | **CRM** | 213.38 | - | **-** | 20 | - | NEG -$10.7M | - | 195 | 220 | -$114k | - | out (clean 31, ADX 28, RVol 0.7) |
| 23 | **MSTR** | 124.23 | - | **-** | 18 | - | POS +$8.5M | 120.39 | 133 | 120 | -$323k | +$0 bull / -$477k bear | out (clean 30, ADX 25, RVol 0.8) |
| 24 | **SHOP** | 149.63 | - | **-** | 17 | - | POS +$2.5M | 144.17 | 155 | 140 | -$10k | - | out (clean 31, ADX 34, RVol 0.5) |
| 25 | **ORCL** | 119.65 | - | **-** | 12 | - | NEG -$21.9M | - | 130 | 120 | -$159k | - | out (clean 29, ADX 34, RVol 1.0) |
| 26 | **HOOD** | 82.66 | - | **-** | 12 | - | POS +$4.7M | 78.79 | 85 | 80 | +$151k | - | out (clean 30, ADX 30, RVol 1.7) |
| 27 | **COIN** | 133.98 | - | **-** | 11 | - | POS +$9.9M | - | 141 | 135 | -$111k | - | out (clean 32, ADX 24, RVol 0.6) |

## Big prints this scan (180)
- **TSLA** CALL 357.5 2026-11-13 (3DTE): 174 @ 19.48 = **+$339k** SELL | vol 1,001 / OI 2,514
- **SMH** PUT 485 2026-11-13 (3DTE): 284 @ 11.87 = **+$337k** BUY | vol 523 / OI 308
- **TSLA** CALL 360 2026-11-13 (3DTE): 174 @ 17.43 = **+$303k** SELL | vol 1,321 / OI 3,304
- **SMH** PUT 485 2026-11-13 (3DTE): 196 @ 11.86 = **+$232k** BUY | vol 523 / OI 308
- **NVDA** CALL 172.5 2026-11-16 (6DTE): 500 @ 4.60 = **+$230k** SELL | vol 1,871 / OI 10
- **NVDA** CALL 170 2026-11-16 (6DTE): 370 @ 5.85 = **+$216k** SELL | vol 2,085 / OI 394
- **NVDA** CALL 172.5 2026-11-16 (6DTE): 497 @ 4.35 = **+$216k** SELL | vol 1,871 / OI 10
- **MU** PUT 730 2026-11-13 (3DTE): 66 @ 30.15 = **+$199k** BUY | vol 306 / OI 813
- **SPY** PUT 760 2026-11-13 (3DTE): 147 @ 12.20 = **+$179k** BUY | vol 14,620 / OI 5,844
- **MU** CALL 715 2026-11-11 (1DTE): 83 @ 20.00 = **+$166k** SELL | vol 2,254 / OI 244
- **QQQ** PUT 675 2026-11-10 (0DTE): 490 @ 3.10 = **+$152k** BUY | vol 20,051 / OI 718
- **AVGO** CALL 320 2026-11-11 (1DTE): 143 @ 9.65 = **+$138k** SELL | vol 1,442 / OI 171
- **MU** PUT 730 2026-11-13 (3DTE): 41 @ 31.54 = **+$129k** BUY | vol 306 / OI 813
- **MU** CALL 722.5 2026-11-11 (1DTE): 75 @ 17.00 = **+$128k** SELL | vol 1,047 / OI 85
- **MU** CALL 715 2026-11-11 (1DTE): 50 @ 24.75 = **+$124k** SELL | vol 2,254 / OI 244

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 716 2026-11-10 (0DTE): 505 traded vs OI 433
- **SPY** PUT 750 2026-11-11 (1DTE): 3,548 traded vs OI 3,489
- **SPY** PUT 727 2026-11-11 (1DTE): 930 traded vs OI 674
- **SPY** PUT 757 2026-11-10 (0DTE): 554 traded vs OI 353
- **SPY** PUT 748 2026-11-13 (3DTE): 2,952 traded vs OI 2,268
- **SPY** PUT 740 2026-11-11 (1DTE): 3,343 traded vs OI 2,721
- **SPY** PUT 708 2026-11-10 (0DTE): 1,188 traded vs OI 847
- **SPY** PUT 726 2026-11-11 (1DTE): 661 traded vs OI 314
- **SPY** PUT 722 2026-11-11 (1DTE): 1,073 traded vs OI 665
- **SPY** PUT 744 2026-11-12 (2DTE): 539 traded vs OI 207
- **SPY** CALL 738 2026-11-10 (0DTE): 745 traded vs OI 634
- **QQQ** CALL 689 2026-11-11 (1DTE): 588 traded vs OI 212
- **QQQ** PUT 658 2026-11-11 (1DTE): 535 traded vs OI 311
- **QQQ** CALL 701 2026-11-10 (0DTE): 1,130 traded vs OI 396
- **QQQ** PUT 659 2026-11-11 (1DTE): 518 traded vs OI 174

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
