# GEX + FLOW SCAN - Tue Nov 10, 10:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 0.79 | +57% (14m) | **+25%** | +22% | 280 hit |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.27 | +5% (1m) | **-65%** | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.42 | +50% (8m) | **-19%** | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:30:08 ET, last candle SPY 10:29, QQQ 10:29 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 10:15 BABA PUTS: price +0.24 over the last 15 min - flow says one way, price says the other
- 10:10 BABA PUTS: price +0.73 over the last 15 min - flow says one way, price says the other
- 10:00 NFLX CALLS: price -0.14 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AAPL CALLS: price -2.97 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 BABA CALLS: price -0.98 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 347.03 | FLOW SURGE | **CALLS** | 44 | none: 84 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (14 contracts' greeks worked out here) | POS +$383.5M | 335.85 | 350 | 340 | +$19.6M | +$334k bull / +$0 bear | out (clean 28, ADX 22, RVol 1.1) |
| 2 | **AMD** | 532.49 | - | **-** | 34 | - | POS +$40.9M | - | 550 | 500 | -$92.4M | +$6.7M bull / -$73k bear | out (clean 31, ADX 37, RVol 2.4) |
| 3 | **GOOGL** | 290.26 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 29 | none: 69 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$11.0M | 288.91 | 300 | 290 | +$826k | - | out (clean 30, ADX 17, RVol 1.2) |
| 4 | **IWM** | 279.83 | TREND (flow not with it) | **PUTS** | 28 | 11/10 279P @ 0.52 (delta 0.35) = est +109% at 278.33 | NEG -$1.1B | 284 | 285 | 270 | +$1.7M | +$950k bull / +$0 bear | SHORT (clean 36, ADX 43, RVol 0.8) |
| 5 | **ARM** | 182.03 | - | **-** | 27 | - | NEG -$5.1M | - | 185 | 190 | -$155k | +$27k bull / +$0 bear | out (clean 27, ADX 24, RVol 0.7) |
| 6 | **AVGO** | 331.20 | - | **-** | 26 | - | NEG -$11.4M | 344.6 | 340 | 340 | -$9.6M | +$1.7M bull / -$94k bear | out (clean 31, ADX 34, RVol 2.1) |
| 7 | **HOOD** | 81.59 | - | **-** | 26 | - | POS +$3.2M | 79.31 | 85 | 80 | +$500k | +$28k bull / +$0 bear | out (clean 30, ADX 31, RVol 0.8) |
| 8 | **NVDA** | 171.42 | - | **-** | 21 | - | NEG -$182.9M | - | 185 | 170 | +$9.1M | +$4.0M bull / +$0 bear | out (clean 32, ADX 29, RVol 1.9) |
| 9 | **TSLA** | 376.73 | - | **-** | 21 | - | POS +$193.7M | - | 400 | 380 | -$8.9M | +$226k bull / -$507k bear | out (clean 34, ADX 39, RVol 0.4) |
| 10 | **MU** | 724.66 | - | **-** | 21 | - | NEG -$12.8M | - | 750 | 750 | -$29.2M | +$6.9M bull / +$0 bear | out (clean 30, ADX 22, RVol 0.9) |
| 11 | **SPY** | 749.33 | - | **-** | 20 | - | NEG -$6.3B | 760.41 | 750 | 730 | -$46.0M | +$4.5M bull / +$0 bear | out (clean 32, ADX 30, RVol 0.6) |
| 12 | **QQQ** | 675.95 | - | **-** | 20 | - | NEG -$1.7B | 691.81 | 680 | 680 | -$67.4M | +$3.1M bull / +$0 bear | out (clean 31, ADX 23, RVol 0.7) |
| 13 | **SMH** | 485.77 | - | **-** | 20 | - | NEG -$197.0M | - | 500 | 475 | -$1.0M | +$428k bull / +$0 bear | out (clean 29, ADX 21, RVol 0.8) |
| 14 | **AMZN** | 272.11 | - | **-** | 20 | - | POS +$481.4M | - | 270 | 265 | +$2.7M | +$90k bull / -$132k bear | out (clean 33, ADX 32, RVol 0.9) |
| 15 | **ORCL** | 119.38 | - | **-** | 20 | - | NEG -$23.4M | - | 130 | 120 | -$175k | +$26k bull / -$76k bear | out (clean 28, ADX 28, RVol 0.7) |
| 16 | **UBER** | 70.15 | PINNED between the walls (positive gamma) - chop | **-** | 20 | - | POS +$9.6M | 68.3 | 70 | 70 | -$10k | - | out (clean 33, ADX 39, RVol 0.3) |
| 17 | **MSFT** | 542.49 | - | **-** | 19 | - | POS +$671.5M | - | 550 | 535 | -$17k | +$161k bull / +$0 bear | out (clean 33, ADX 41, RVol 0.8) |
| 18 | **BABA** | 103.98 | - | **-** | 19 | - | NEG -$5.8M | 106.07 | 110 | 100 | -$474k | - | out (clean 29, ADX 30, RVol 1.1) |
| 19 | **META** | 643.01 | - | **-** | 17 | - | POS +$260.0M | - | 650 | 650 | -$900k | +$513k bull / -$67k bear | out (clean 33, ADX 26, RVol 0.8) |
| 20 | **DELL** | 336.01 | - | **-** | 17 | - | NEG -$8.7M | - | 350 | 340 | +$95k | +$64k bull / +$0 bear | out (clean 32, ADX 27, RVol 0.8) |
| 21 | **MSTR** | 122.43 | - | **-** | 17 | - | POS +$3.1M | 120.69 | 133 | 120 | +$305k | +$137k bull / +$0 bear | out (clean 30, ADX 24, RVol 0.5) |
| 22 | **CRM** | 213.09 | - | **-** | 17 | - | NEG -$10.7M | - | 195 | 220 | -$91k | - | out (clean 31, ADX 34, RVol 0.7) |
| 23 | **PLTR** | 167.13 | - | **-** | 12 | - | POS +$52.7M | - | 165 | 170 | -$562k | - | out (clean 28, ADX 41, RVol 0.5) |
| 24 | **NFLX** | 62.95 | - | **-** | 11 | - | NEG -$21.2M | 65.4 | 65 | 60 | -$220k | - | out (clean 30, ADX 32, RVol 1.0) |
| 25 | **COIN** | 132.96 | - | **-** | 9 | - | POS +$5.1M | 128.49 | 137 | 135 | +$110k | - | out (clean 31, ADX 26, RVol 0.5) |
| 26 | **SMCI** | 28.39 | - | **-** | 9 | - | POS +$3.7M | - | 30 | 30 | -$71k | - | out (clean 28, ADX 22, RVol 0.4) |
| 27 | **SHOP** | 148.95 | - | **-** | 8 | - | POS +$2.2M | 144.39 | 150 | 140 | -$743 | - | out (clean 31, ADX 36, RVol 0.4) |

## Big prints this scan (110)
- **SPY** PUT 760 2026-11-13 (3DTE): 669 @ 10.25 = **+$686k** SELL | vol 20,743 / OI 5,844
- **SPY** PUT 760 2026-11-13 (3DTE): 420 @ 10.25 = **+$430k** SELL | vol 20,743 / OI 5,844
- **AMD** CALL 510 2026-11-13 (3DTE): 97 @ 33.40 = **+$324k** BUY | vol 1,840 / OI 747
- **SPY** PUT 760 2026-11-13 (3DTE): 245 @ 10.25 = **+$251k** SELL | vol 20,743 / OI 5,844
- **AVGO** CALL 330 2026-11-11 (1DTE): 340 @ 7.10 = **+$241k** BUY | vol 4,273 / OI 600
- **AMD** CALL 530 2026-11-13 (3DTE): 100 @ 22.30 = **+$223k** BUY | vol 2,094 / OI 1,599
- **QQQ** CALL 680 2026-11-10 (0DTE): 1,000 @ 2.18 = **+$218k** BUY | vol 93,875 / OI 2,411
- **QQQ** PUT 680 2026-11-10 (0DTE): 499 @ 3.00 = **+$150k** SELL | vol 18,846 / OI 670
- **IWM** CALL 281 2026-11-11 (1DTE): 884 @ 1.56 = **+$138k** BUY | vol 3,831 / OI 455
- **SPY** PUT 760 2026-11-13 (3DTE): 126 @ 10.25 = **+$129k** SELL | vol 20,743 / OI 5,844
- **AMD** CALL 525 2026-11-16 (6DTE): 49 @ 26.27 = **+$129k** BUY | vol 178 / OI 65
- **MU** CALL 750 2026-11-11 (1DTE): 99 @ 12.75 = **+$126k** BUY | vol 5,237 / OI 728
- **QQQ** CALL 679 2026-11-11 (1DTE): 250 @ 4.90 = **+$122k** BUY | vol 3,135 / OI 135
- **MU** CALL 755 2026-11-11 (1DTE): 95 @ 11.15 = **+$106k** BUY | vol 1,937 / OI 179
- **SPY** PUT 760 2026-11-13 (3DTE): 101 @ 10.25 = **+$104k** SELL | vol 20,743 / OI 5,844

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 731 2026-11-12 (2DTE): 631 traded vs OI 280
- **SPY** PUT 751 2026-11-13 (3DTE): 1,601 traded vs OI 1,037
- **SPY** PUT 755 2026-11-10 (0DTE): 3,862 traded vs OI 3,607
- **SPY** CALL 752 2026-11-13 (3DTE): 1,684 traded vs OI 1,264
- **SPY** PUT 749 2026-11-13 (3DTE): 1,160 traded vs OI 1,028
- **SPY** CALL 768 2026-11-16 (6DTE): 1,758 traded vs OI 438
- **SPY** CALL 767 2026-11-10 (0DTE): 1,929 traded vs OI 1,786
- **SPY** PUT 745 2026-11-24 (14DTE): 503 traded vs OI 0
- **QQQ** CALL 691 2026-11-11 (1DTE): 768 traded vs OI 570
- **QQQ** PUT 638 2026-11-13 (3DTE): 540 traded vs OI 111
- **QQQ** PUT 690 2026-11-10 (0DTE): 580 traded vs OI 533
- **QQQ** PUT 670 2026-11-13 (3DTE): 4,580 traded vs OI 4,369
- **QQQ** PUT 642 2026-11-11 (1DTE): 552 traded vs OI 126
- **QQQ** PUT 625 2026-11-11 (1DTE): 734 traded vs OI 688
- **QQQ** CALL 694 2026-11-11 (1DTE): 511 traded vs OI 481

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
