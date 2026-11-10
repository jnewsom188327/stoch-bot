# GEX + FLOW SCAN - Tue Nov 10, 01:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:33 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 667P | 0.67 | 0.76 | +170% (8m) | **+13%** | +15% | 668.83 hit |
| 12:22 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 667P | 0.66 | 0.76 | +174% (19m) | **+15%** | +11% | 669.29 hit |
| 11:18 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 668P | 0.74 | 0.69 | +84% (38m) | **-7%** (done) | +18% | 672.3 hit |
| 11:17 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.60 | 0.36 | +38% (32m) | **-40%** (done) | +41% | 746.01 hit |
| 11:12 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 669P | 0.74 | 1.07 | +135% (44m) | **+45%** (done) | +38% | 671.74 hit |
| 11:12 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.64 | 0.38 | +30% (37m) | **-41%** (done) | +40% | 745.88 |
| 11:06 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.68 | 0.60 | +22% (43m) | **-12%** (done) | +49% | 745.54 |
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 1.39 | +232% (36m) | **+121%** (done) | +22% | 280 hit |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.62 | +21% (60m) | **-19%** (done) | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.95 | +90% (60m) | **+83%** (done) | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (9 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:00:08 ET, last candle SPY 12:59, QQQ 12:59 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 12:32 | QQQ | 1m FAILED POP | R3 R4 | PUTS | WITH you | **FIRE** QQQ261110P00667000 |
| 12:21 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** QQQ261110P00667000 |
| 11:23 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 11:17 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** QQQ261110P00668000 |
| 11:16 | SPY | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** SPY261110P00744000 |
| 11:14 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | 5-minute cooldown |
| 11:11 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** QQQ261110P00669000 |
| 11:11 | SPY | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** SPY261110P00744000 |
| 11:05 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** SPY261110P00744000 |

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 10:15 BABA PUTS: price +0.24 over the last 15 min - flow says one way, price says the other
- 10:10 BABA PUTS: price +0.73 over the last 15 min - flow says one way, price says the other
- 10:00 NFLX CALLS: price -0.14 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AAPL CALLS: price -2.97 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 BABA CALLS: price -0.98 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 530.76 | FLOW SURGE | **CALLS** | 47 | none: 126 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$381.2M | 502.66 | 550 | 500 | +$18.3M | +$2.8M bull / -$625k bear | out (clean 32, ADX 45, RVol 2.1) |
| 2 | **PLTR** | 165.29 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 39 | none: 14 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$48.5M | - | 165 | 170 | -$612k | +$35k bull / -$34k bear | out (clean 28, ADX 36, RVol 0.8) |
| 3 | **CRM** | 209.62 | - | **-** | 27 | - | NEG -$10.3M | - | 195 | 220 | +$296k | +$36k bull / +$0 bear | out (clean 30, ADX 39, RVol 0.7) |
| 4 | **AMD** | 510.05 | - | **-** | 21 | - | POS +$47.9M | - | 500 | 500 | -$40.5M | +$481k bull / -$5.4M bear | out (clean 33, ADX 31, RVol 1.1) |
| 5 | **AMZN** | 268.71 | - | **-** | 21 | - | POS +$451.1M | - | 270 | 265 | +$8.4M | +$0 bull / -$87k bear | out (clean 33, ADX 25, RVol 0.9) |
| 6 | **DELL** | 326.30 | - | **-** | 21 | - | NEG -$10.4M | - | 350 | 340 | +$994k | +$0 bull / -$27k bear | out (clean 33, ADX 40, RVol 0.9) |
| 7 | **NVDA** | 167.73 | - | **-** | 20 | - | NEG -$154.3M | - | 180 | 170 | +$13.9M | +$3.5M bull / -$1.3M bear | out (clean 34, ADX 36, RVol 1.2) |
| 8 | **ORCL** | 116.57 | - | **-** | 20 | - | NEG -$24.4M | - | 120 | 120 | +$493k | +$0 bull / -$38k bear | out (clean 28, ADX 38, RVol 0.3) |
| 9 | **SPY** | 746.62 | - | **-** | 18 | - | NEG -$8.2B | 760.55 | 750 | 730 | +$69.0M | +$109k bull / -$2.8M bear | out (clean 32, ADX 30, RVol 0.4) |
| 10 | **MSTR** | 119.86 | - | **-** | 18 | - | NEG -$25.6M | - | 130 | 110 | +$232k | +$0 bull / -$30k bear | out (clean 29, ADX 34, RVol 0.7) |
| 11 | **QQQ** | 670.05 | - | **-** | 17 | - | NEG -$2.2B | 692.57 | 680 | 680 | +$24.1M | +$240k bull / -$1.3M bear | out (clean 32, ADX 34, RVol 0.3) |
| 12 | **AVGO** | 327.44 | - | **-** | 17 | - | NEG -$16.6M | 343.91 | 340 | 320 | -$8.8M | +$131k bull / -$321k bear | out (clean 32, ADX 14, RVol 0.4) |
| 13 | **IWM** | 279.62 | - | **-** | 16 | - | NEG -$1.2B | 283.62 | 280 | 270 | +$2.4M | +$0 bull / -$60k bear | out (clean 36, ADX 25, RVol 0.4) |
| 14 | **SMH** | 479.22 | - | **-** | 16 | - | NEG -$224.8M | - | 500 | 475 | +$345k | +$760k bull / -$34k bear | out (clean 30, ADX 29, RVol 0.3) |
| 15 | **MU** | 708.18 | - | **-** | 16 | - | NEG -$33.0M | - | 750 | 750 | -$5.5M | +$1.6M bull / -$1.9M bear | out (clean 30, ADX 27, RVol 0.2) |
| 16 | **TSLA** | 376.05 | - | **-** | 15 | - | POS +$187.4M | - | 400 | 380 | -$5.4M | +$276k bull / -$590k bear | out (clean 32, ADX 21, RVol 0.3) |
| 17 | **META** | 641.42 | - | **-** | 15 | - | POS +$241.1M | 604.31 | 650 | 650 | +$213k | +$0 bull / -$28k bear | out (clean 32, ADX 20, RVol 0.7) |
| 18 | **AAPL** | 347.58 | - | **-** | 14 | - | POS +$406.6M | 336.04 | 350 | 340 | +$18.1M | - | out (clean 28, ADX 13, RVol 0.4) |
| 19 | **SHOP** | 143.46 | - | **-** | 13 | - | NEG -$1.1M | 146.08 | 150 | 140 | +$31k | - | out (clean 33, ADX 61, RVol 1.0) |
| 20 | **HOOD** | 80.50 | - | **-** | 12 | - | POS +$1.6M | 79.23 | 85 | 80 | +$643k | - | out (clean 31, ADX 38, RVol 0.4) |
| 21 | **ARM** | 177.86 | - | **-** | 12 | - | NEG -$4.8M | - | 185 | 190 | -$205k | - | out (clean 28, ADX 29, RVol 0.4) |
| 22 | **GOOGL** | 286.35 | - | **-** | 11 | - | NEG -$30.0M | 289.2 | 300 | 290 | +$3.3M | - | out (clean 30, ADX 26, RVol 0.3) |
| 23 | **COIN** | 130.70 | - | **-** | 10 | - | POS +$1.2M | 129.45 | 137 | 135 | +$203k | - | out (clean 29, ADX 40, RVol 0.5) |
| 24 | **UBER** | 69.60 | - | **-** | 10 | - | POS +$6.7M | 68.37 | 70 | 70 | -$51k | - | out (clean 33, ADX 31, RVol 0.3) |
| 25 | **BABA** | 102.67 | - | **-** | 10 | - | NEG -$9.7M | 106.45 | 110 | 100 | -$84k | - | out (clean 30, ADX 42, RVol 0.7) |
| 26 | **SMCI** | 27.55 | - | **-** | 8 | - | POS +$959k | 26.36 | 30 | 25 | -$13k | - | out (clean 30, ADX 37, RVol 0.5) |
| 27 | **NFLX** | 62.74 | - | **-** | 6 | - | NEG -$24.0M | 65.52 | 65 | 60 | -$93k | - | out (clean 30, ADX 22, RVol 0.5) |

## Big prints this scan (112)
- **AMD** CALL 510 2026-11-11 (1DTE): 615 @ 7.20 = **+$443k** SELL | vol 12,450 / OI 407
- **AMD** CALL 510 2026-11-11 (1DTE): 604 @ 7.20 = **+$435k** SELL | vol 12,450 / OI 407
- **SPY** PUT 760 2026-11-13 (3DTE): 280 @ 14.59 = **+$409k** BUY | vol 39,052 / OI 5,844
- **QQQ** CALL 665 2026-11-10 (0DTE): 999 @ 3.55 = **+$355k** SELL | vol 3,685 / OI 1,633
- **SPY** CALL 749 2026-11-11 (1DTE): 2,166 @ 1.62 = **+$351k** SELL | vol 17,188 / OI 446
- **QQQ** CALL 665 2026-11-10 (0DTE): 795 @ 3.80 = **+$302k** SELL | vol 3,685 / OI 1,633
- **MU** PUT 725 2026-11-11 (1DTE): 100 @ 29.95 = **+$300k** BUY | vol 3,685 / OI 61
- **NVDA** CALL 167.5 2026-11-13 (3DTE): 500 @ 4.50 = **+$225k** SELL | vol 10,166 / OI 18
- **AMD** CALL 510 2026-11-11 (1DTE): 263 @ 7.20 = **+$189k** SELL | vol 12,450 / OI 407
- **SPY** PUT 746 2026-11-10 (0DTE): 900 @ 2.09 = **+$188k** BUY | vol 341,995 / OI 242
- **SPY** PUT 746 2026-11-10 (0DTE): 1,000 @ 1.86 = **+$186k** BUY | vol 341,995 / OI 242
- **SPY** PUT 750 2026-11-10 (0DTE): 354 @ 4.82 = **+$171k** BUY | vol 122,514 / OI 1,541
- **QQQ** PUT 660 2026-11-13 (3DTE): 300 @ 5.10 = **+$153k** BUY | vol 19,531 / OI 7,659
- **AMD** CALL 510 2026-11-11 (1DTE): 208 @ 7.20 = **+$150k** SELL | vol 12,450 / OI 407
- **SPY** PUT 745 2026-11-10 (0DTE): 979 @ 1.34 = **+$131k** BUY | vol 357,423 / OI 1,663

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 746 2026-11-16 (6DTE): 514 traded vs OI 263
- **SPY** PUT 743 2026-11-13 (3DTE): 1,471 traded vs OI 1,440
- **SPY** CALL 794 2026-11-16 (6DTE): 2,400 traded vs OI 570
- **SPY** PUT 704 2026-11-12 (2DTE): 705 traded vs OI 589
- **SPY** PUT 727 2026-11-12 (2DTE): 515 traded vs OI 397
- **SPY** CALL 795 2026-11-16 (6DTE): 501 traded vs OI 240
- **SPY** CALL 792 2026-11-16 (6DTE): 1,400 traded vs OI 47
- **SPY** CALL 820 2026-11-17 (7DTE): 4,820 traded vs OI 136
- **SPY** CALL 765 2026-11-17 (7DTE): 509 traded vs OI 335
- **QQQ** PUT 685 2026-11-11 (1DTE): 535 traded vs OI 527
- **QQQ** PUT 626 2026-11-11 (1DTE): 537 traded vs OI 117
- **QQQ** CALL 664 2026-11-10 (0DTE): 523 traded vs OI 400
- **QQQ** PUT 650 2026-11-12 (2DTE): 1,627 traded vs OI 1,569
- **QQQ** PUT 668 2026-11-16 (6DTE): 592 traded vs OI 83
- **IWM** CALL 279 2026-11-13 (3DTE): 1,168 traded vs OI 1,161

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
