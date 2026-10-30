# GEX + FLOW SCAN - Fri Oct 30, 03:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 15:02 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 46 puts 0-1DTE > 2 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 12:45 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:32 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:31 | SPY | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 45 puts 0-1DTE > 1 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |
| 11:05 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 12:40 NVDA CALLS: under EMA 20 - flow says one way, price says the other
- 11:20 ARM CALLS: under EMA 20 - flow says one way, price says the other
- 11:20 COIN PUTS: price +0.22 over the last 15 min - flow says one way, price says the other
- 11:15 MSTR PUTS: price +1.54 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 11:10 MSTR PUTS: price +1.77 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 344.48 | PINNED between the walls (positive gamma) - chop | **-** | 40 | - | POS +$122.1M | 342.45 | 345 | 345 | +$9.7M | +$0 bull / -$771k bear | out (clean 32, ADX 28, RVol 1.8) |
| 2 | **MSFT** | 524.39 | PINNED between the walls (positive gamma) - chop | **-** | 39 | - | POS +$1.4B | 521.94 | 525 | 525 | +$3.3M | +$0 bull / -$293k bear | out (clean 26, ADX 24, RVol 1.7) |
| 3 | **ORCL** | 130.03 | FLIP CROSS down into negative gamma | **PUTS** | 36 | none: 52 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (33 contracts' greeks worked out here) | NEG -$131.9M | 130.49 | 130 | 130 | +$2.1M | +$37k bull / +$0 bear | out (clean 33, ADX 20, RVol 1.4) |
| 4 | **COIN** | 140.78 | - | **-** | 29 | - | NEG -$19.9M | - | 140 | 140 | -$5.6M | +$0 bull / -$134k bear | out (clean 27, ADX 40, RVol 3.8) |
| 5 | **DELL** | 421.47 | - | **-** | 26 | - | NEG -$42.0M | - | 440 | 420 | +$7.2M | +$52k bull / -$118k bear | out (clean 34, ADX 26, RVol 2.0) |
| 6 | **SPY** | 754.30 | - | **-** | 25 | - | NEG -$16.4B | 765.55 | 800 | 755 | +$228.4M | +$0 bull / -$8.6M bear | out (clean 28, ADX 34, RVol 3.7) |
| 7 | **MSTR** | 130.40 | - | **-** | 25 | - | NEG -$36.3M | 131.46 | 135 | 130 | -$12.7M | +$40k bull / -$3.0M bear | out (clean 27, ADX 26, RVol 3.0) |
| 8 | **AMD** | 500.63 | - | **-** | 24 | - | NEG -$173.6M | 509.59 | 550 | 500 | +$28.2M | +$594k bull / -$1.0M bear | out (clean 30, ADX 27, RVol 2.4) |
| 9 | **NVDA** | 203.45 | - | **-** | 23 | - | NEG -$272.0M | 209.05 | 210 | 200 | +$29.0M | +$29k bull / -$1.8M bear | out (clean 29, ADX 32, RVol 1.9) |
| 10 | **QQQ** | 689.20 | - | **-** | 22 | - | NEG -$5.9B | 720.19 | 720 | 680 | +$56.6M | +$336k bull / -$5.6M bear | out (clean 29, ADX 33, RVol 2.8) |
| 11 | **IWM** | 278.72 | - | **-** | 20 | - | NEG -$1.2B | 279.82 | 278 | 278 | +$6.4M | +$0 bull / -$56k bear | out (clean 30, ADX 28, RVol 1.8) |
| 12 | **SMH** | 519.28 | - | **-** | 20 | - | NEG -$666.2M | - | 532.5 | 520 | -$2.6M | +$149k bull / -$4.2M bear | out (clean 31, ADX 30, RVol 2.0) |
| 13 | **MU** | 876.99 | - | **-** | 20 | - | NEG -$289.0M | 885.28 | 880 | 880 | +$49.9M | +$0 bull / -$4.6M bear | out (clean 31, ADX 25, RVol 1.6) |
| 14 | **HOOD** | 83.77 | - | **-** | 20 | - | NEG -$18.0M | - | 85 | 83 | +$272k | +$0 bull / -$266k bear | out (clean 31, ADX 39, RVol 1.6) |
| 15 | **TSLA** | 398.51 | - | **-** | 19 | - | POS +$625.5M | 382.78 | 400 | 397.5 | -$14.2M | +$225k bull / -$2.0M bear | out (clean 31, ADX 23, RVol 1.9) |
| 16 | **META** | 614.25 | - | **-** | 19 | - | NEG -$162.9M | 620.01 | 615 | 610 | +$4.8M | +$0 bull / -$667k bear | out (clean 30, ADX 40, RVol 0.6) |
| 17 | **PLTR** | 186.05 | - | **-** | 19 | - | NEG -$38.9M | 187.21 | 185 | 185 | -$7.4M | +$0 bull / -$437k bear | out (clean 26, ADX 16, RVol 1.5) |
| 18 | **BABA** | 97.79 | - | **-** | 19 | - | NEG -$15.3M | 98.53 | 100 | 97 | +$664k | - | out (clean 31, ADX 29, RVol 1.8) |
| 19 | **AMZN** | 239.94 | - | **-** | 18 | - | NEG -$212.0M | 245.92 | 250 | 240 | -$7.0M | +$0 bull / -$416k bear | out (clean 30, ADX 20, RVol 1.4) |
| 20 | **GOOGL** | 279.34 | - | **-** | 18 | - | NEG -$230.5M | - | 280 | 280 | +$1.1M | +$0 bull / -$251k bear | out (clean 33, ADX 29, RVol 0.9) |
| 21 | **AVGO** | 323.88 | - | **-** | 18 | - | NEG -$92.9M | 331.89 | 330 | 320 | +$625k | +$0 bull / -$64k bear | out (clean 30, ADX 29, RVol 1.2) |
| 22 | **SHOP** | 156.88 | - | **-** | 17 | - | NEG -$766k | 157.16 | 150 | 155 | +$499k | - | out (clean 28, ADX 31, RVol 2.3) |
| 23 | **NFLX** | 61.90 | - | **-** | 14 | - | NEG -$9.4M | 62.04 | 62 | 60 | +$1.4M | - | out (clean 30, ADX 32, RVol 0.9) |
| 24 | **UBER** | 64.98 | - | **-** | 14 | - | NEG -$66.1M | 65.75 | 65 | 65 | +$474k | - | out (clean 26, ADX 16, RVol 1.1) |
| 25 | **SMCI** | 32.52 | - | **-** | 13 | - | NEG -$1.8M | 32.59 | 35 | 32.5 | -$220k | - | out (clean 30, ADX 43, RVol 2.0) |
| 26 | **CRM** | 228.67 | - | **-** | 13 | - | NEG -$26.8M | 232.28 | 230 | 230 | +$396k | - | out (clean 27, ADX 31, RVol 1.2) |
| 27 | **ARM** | 204.96 | - | **-** | 11 | - | NEG -$47.2M | 213.08 | 220 | 205 | +$30k | - | out (clean 27, ADX 33, RVol 2.7) |

## Big prints this scan (119)
- **SPY** CALL 750 2026-11-03 (4DTE): 1,518 @ 6.79 = **+$1.0M** SELL | vol 35,325 / OI 23
- **SPY** PUT 772 2026-10-30 (0DTE): 290 @ 19.17 = **+$556k** BUY | vol 2,198 / OI 2,957
- **MSTR** CALL 135 2026-11-06 (7DTE): 1,250 @ 4.25 = **+$531k** SELL | vol 24,088 / OI 219
- **MSTR** CALL 135 2026-11-06 (7DTE): 1,250 @ 4.25 = **+$531k** SELL | vol 24,088 / OI 219
- **SMH** PUT 542.5 2026-10-30 (0DTE): 195 @ 25.41 = **+$495k** BUY | vol 1,569 / OI 491
- **SMH** PUT 500 2026-11-06 (7DTE): 602 @ 8.09 = **+$487k** BUY | vol 13,978 / OI 35,115
- **QQQ** CALL 685 2026-11-06 (7DTE): 363 @ 13.14 = **+$477k** SELL | vol 5,253 / OI 153
- **SMH** PUT 542.5 2026-10-30 (0DTE): 171 @ 25.65 = **+$439k** BUY | vol 1,569 / OI 491
- **SMH** PUT 542.5 2026-10-30 (0DTE): 165 @ 25.56 = **+$422k** BUY | vol 1,569 / OI 491
- **QQQ** PUT 710 2026-11-04 (5DTE): 169 @ 24.60 = **+$416k** BUY | vol 873 / OI 602
- **SPY** PUT 772 2026-10-30 (0DTE): 205 @ 19.15 = **+$393k** BUY | vol 2,198 / OI 2,957
- **SMH** PUT 500 2026-11-06 (7DTE): 475 @ 8.10 = **+$385k** BUY | vol 13,978 / OI 35,115
- **SPY** PUT 772 2026-10-30 (0DTE): 192 @ 19.18 = **+$368k** BUY | vol 2,198 / OI 2,957
- **SMH** PUT 542.5 2026-10-30 (0DTE): 139 @ 25.42 = **+$353k** BUY | vol 1,569 / OI 491
- **SMH** PUT 542.5 2026-10-30 (0DTE): 114 @ 25.45 = **+$290k** BUY | vol 1,569 / OI 491

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 785 2026-11-04 (5DTE): 503 traded vs OI 391
- **SPY** CALL 795 2026-11-05 (6DTE): 505 traded vs OI 426
- **SPY** PUT 710 2026-11-03 (4DTE): 928 traded vs OI 328
- **SPY** PUT 715 2026-11-03 (4DTE): 3,315 traded vs OI 1,202
- **QQQ** CALL 757 2026-11-06 (7DTE): 554 traded vs OI 448
- **QQQ** PUT 710 2026-11-04 (5DTE): 873 traded vs OI 602
- **QQQ** PUT 685 2026-11-10 (11DTE): 500 traded vs OI 144
- **IWM** CALL 288 2026-11-06 (7DTE): 2,159 traded vs OI 2,122
- **SMH** CALL 570 2026-11-27 (28DTE): 1,021 traded vs OI 781
- **SMH** CALL 555 2026-11-06 (7DTE): 505 traded vs OI 339
- **NVDA** CALL 202.5 2026-11-13 (14DTE): 622 traded vs OI 8
- **TSLA** PUT 372.5 2026-11-02 (3DTE): 900 traded vs OI 886
- **AMD** PUT 487.5 2026-11-02 (3DTE): 500 traded vs OI 23
- **META** PUT 597.5 2026-11-02 (3DTE): 619 traded vs OI 137
- **NFLX** PUT 59 2026-11-06 (7DTE): 1,449 traded vs OI 1,425

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
