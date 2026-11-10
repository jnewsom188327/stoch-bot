# GEX + FLOW SCAN - Tue Nov 10, 03:05 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:33 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 667P | 0.67 | 0.28 | +170% (8m) | **-58%** (done) | +15% | 668.83 hit |
| 12:22 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 667P | 0.66 | 0.79 | +174% (19m) | **+20%** (done) | +11% | 669.29 hit |
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
Last 1m check 15:05:08 ET, last candle SPY 15:04, QQQ 15:04 | no errors
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
| 1 | **AAPL** | 348.20 | - | **-** | 22 | - | POS +$437.6M | 336.45 | 350 | 340 | +$17.2M | +$335k bull / +$0 bear | out (clean 28, ADX 14, RVol 0.4) |
| 2 | **AVGO** | 330.67 | - | **-** | 21 | - | NEG -$10.3M | 341.36 | 340 | 340 | -$12.0M | +$94k bull / +$0 bear | out (clean 34, ADX 32, RVol 0.6) |
| 3 | **AMD** | 514.61 | - | **-** | 18 | - | POS +$44.1M | - | 500 | 500 | -$49.2M | +$252k bull / -$897k bear | out (clean 33, ADX 20, RVol 0.6) |
| 4 | **AMZN** | 271.64 | - | **-** | 18 | - | POS +$486.9M | - | 270 | 265 | -$550k | +$0 bull / -$118k bear | out (clean 34, ADX 33, RVol 0.8) |
| 5 | **SPY** | 748.12 | - | **-** | 17 | - | NEG -$6.9B | 760.04 | 750 | 750 | +$24.7M | +$306k bull / -$802k bear | out (clean 32, ADX 29, RVol 0.4) |
| 6 | **NVDA** | 166.08 | - | **-** | 16 | - | NEG -$150.7M | - | 180 | 170 | +$14.2M | +$1.6M bull / -$116k bear | out (clean 33, ADX 17, RVol 1.3) |
| 7 | **ORCL** | 116.96 | - | **-** | 16 | - | NEG -$25.7M | - | 120 | 120 | +$477k | +$0 bull / -$55k bear | out (clean 27, ADX 17, RVol 0.4) |
| 8 | **QQQ** | 671.59 | - | **-** | 15 | - | NEG -$1.9B | 691.49 | 672 | 680 | -$432k | +$1.0M bull / -$121k bear | out (clean 32, ADX 27, RVol 0.2) |
| 9 | **META** | 642.42 | - | **-** | 15 | - | POS +$252.9M | 607.59 | 650 | 650 | -$446k | +$0 bull / -$117k bear | out (clean 32, ADX 22, RVol 0.5) |
| 10 | **MU** | 711.85 | - | **-** | 15 | - | NEG -$34.5M | - | 750 | 750 | -$20.9M | +$290k bull / -$934k bear | out (clean 30, ADX 18, RVol 0.2) |
| 11 | **IWM** | 279.74 | - | **-** | 14 | - | NEG -$1.1B | 283.26 | 280 | 270 | +$1.6M | +$0 bull / -$70k bear | out (clean 35, ADX 17, RVol 0.3) |
| 12 | **TSLA** | 377.12 | - | **-** | 14 | - | POS +$201.9M | - | 400 | 380 | -$7.2M | +$780k bull / -$899k bear | out (clean 32, ADX 14, RVol 0.5) |
| 13 | **CRM** | 210.59 | - | **-** | 12 | - | NEG -$10.7M | - | 195 | 220 | +$311k | - | out (clean 31, ADX 19, RVol 0.5) |
| 14 | **SHOP** | 144.61 | - | **-** | 12 | - | NEG -$388k | 145.5 | 150 | 140 | -$219k | - | out (clean 32, ADX 22, RVol 0.7) |
| 15 | **MSFT** | 532.43 | - | **-** | 10 | - | POS +$414.1M | 505.64 | 550 | 500 | +$12.2M | - | out (clean 32, ADX 20, RVol 0.3) |
| 16 | **ARM** | 178.39 | - | **-** | 10 | - | NEG -$4.8M | - | 185 | 185 | -$219k | - | out (clean 27, ADX 19, RVol 0.3) |
| 17 | **UBER** | 69.66 | - | **-** | 9 | - | POS +$6.7M | 68.51 | 70 | 70 | -$68k | - | out (clean 33, ADX 22, RVol 0.2) |
| 18 | **GOOGL** | 287.03 | - | **-** | 8 | - | NEG -$17.9M | 288.54 | 300 | 290 | +$2.4M | - | out (clean 29, ADX 19, RVol 0.2) |
| 19 | **HOOD** | 80.48 | - | **-** | 7 | - | POS +$1.5M | 79.42 | 85 | 80 | +$590k | - | out (clean 32, ADX 17, RVol 0.3) |
| 20 | **NFLX** | 62.85 | - | **-** | 6 | - | NEG -$21.5M | 65.27 | 65 | 60 | -$198k | - | out (clean 29, ADX 18, RVol 0.5) |
| 21 | **PLTR** | 165.95 | - | **-** | 6 | - | POS +$51.7M | - | 165 | 170 | -$830k | - | out (clean 28, ADX 15, RVol 0.4) |
| 22 | **BABA** | 102.44 | - | **-** | 6 | - | NEG -$10.4M | 106.29 | 110 | 100 | -$152k | - | out (clean 30, ADX 21, RVol 0.4) |
| 23 | **COIN** | 131.01 | - | **-** | 5 | - | POS +$2.5M | 129.18 | 137 | 135 | +$188k | - | out (clean 28, ADX 17, RVol 0.3) |
| 24 | **DELL** | 330.33 | - | **-** | 5 | - | NEG -$10.9M | - | 350 | 340 | +$928k | - | out (clean 34, ADX 17, RVol 0.2) |
| 25 | **SMCI** | 27.47 | - | **-** | 4 | - | POS +$912k | 26.43 | 30 | 25 | -$44k | - | out (clean 30, ADX 14, RVol 0.5) |
| 26 | **MSTR** | 119.64 | - | **-** | 4 | - | NEG -$26.4M | - | 130 | 110 | +$672k | - | out (clean 29, ADX 11, RVol 0.3) |
| 27 | **SMH** | 480.07 | - | **-** | 3 | - | NEG -$227.1M | - | 500 | 475 | -$88k | - | out (clean 29, ADX 16, RVol 0.1) |

## Big prints this scan (39)
- **QQQ** CALL 665 2026-11-10 (0DTE): 1,000 @ 6.93 = **+$693k** BUY | vol 6,087 / OI 1,633
- **QQQ** PUT 675 2026-11-10 (0DTE): 1,000 @ 3.27 = **+$327k** SELL | vol 142,379 / OI 718
- **SPY** CALL 748 2026-11-10 (0DTE): 1,062 @ 1.49 = **+$158k** BUY | vol 423,913 / OI 4,785
- **SPY** CALL 748 2026-11-10 (0DTE): 1,334 @ 1.11 = **+$148k** BUY | vol 423,913 / OI 4,785
- **NVDA** CALL 170 2026-11-11 (1DTE): 837 @ 1.65 = **+$138k** BUY | vol 140,888 / OI 252
- **AMD** CALL 510 2026-11-11 (1DTE): 95 @ 13.10 = **+$124k** BUY | vol 16,763 / OI 407
- **AMD** CALL 510 2026-11-11 (1DTE): 100 @ 12.22 = **+$122k** SELL | vol 16,763 / OI 407
- **AMD** PUT 500 2026-11-11 (1DTE): 183 @ 4.30 = **+$79k** SELL | vol 18,330 / OI 49
- **NVDA** CALL 167.5 2026-11-11 (1DTE): 250 @ 2.82 = **+$70k** BUY | vol 72,604 / OI 80
- **NVDA** CALL 165 2026-11-16 (6DTE): 100 @ 6.65 = **+$66k** BUY | vol 2,502 / OI 17
- **NVDA** CALL 165 2026-11-16 (6DTE): 100 @ 6.65 = **+$66k** BUY | vol 2,502 / OI 17
- **TSLA** PUT 367.5 2026-11-13 (3DTE): 210 @ 3.00 = **+$63k** SELL | vol 2,449 / OI 516
- **NVDA** PUT 160 2026-11-11 (1DTE): 657 @ 0.81 = **+$53k** SELL | vol 72,362 / OI 1,293
- **AVGO** CALL 327.5 2026-11-11 (1DTE): 75 @ 7.06 = **+$53k** BUY | vol 5,092 / OI 78
- **NVDA** PUT 160 2026-11-11 (1DTE): 648 @ 0.81 = **+$52k** SELL | vol 72,362 / OI 1,293

## New unusual volume (traded more than open interest, 500+)
- **QQQ** CALL 692 2026-11-12 (2DTE): 505 traded vs OI 334
- **QQQ** PUT 630 2026-11-11 (1DTE): 1,357 traded vs OI 1,353
- **QQQ** CALL 670 2026-11-16 (6DTE): 549 traded vs OI 397
- **QQQ** CALL 674 2026-11-20 (10DTE): 624 traded vs OI 270
- **IWM** PUT 270 2026-12-04 (24DTE): 3,065 traded vs OI 2,002
- **NVDA** CALL 150 2026-11-11 (1DTE): 1,416 traded vs OI 0
- **TSLA** PUT 380 2026-12-04 (24DTE): 674 traded vs OI 672
- **TSLA** CALL 387.5 2026-11-13 (3DTE): 1,254 traded vs OI 1,242
- **META** CALL 665 2026-11-13 (3DTE): 503 traded vs OI 449
- **AMZN** PUT 255 2026-11-13 (3DTE): 2,761 traded vs OI 2,340
- **AMZN** CALL 270 2026-11-16 (6DTE): 530 traded vs OI 428
- **AMZN** CALL 260 2026-11-11 (1DTE): 1,378 traded vs OI 1,288
- **MSFT** PUT 505 2026-11-13 (3DTE): 662 traded vs OI 661
- **HOOD** PUT 78 2026-11-13 (3DTE): 1,248 traded vs OI 1,244

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
