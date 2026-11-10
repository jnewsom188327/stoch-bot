# GEX + FLOW SCAN - Tue Nov 10, 03:15 PM ET
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
Last 1m check 15:15:08 ET, last candle SPY 15:14, QQQ 15:14 | no errors
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
| 1 | **AMZN** | 271.81 | TREND (flow not with it) | **CALLS** | 36 | none: 66 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | POS +$486.4M | - | 270 | 265 | -$245k | +$96k bull / +$0 bear | LONG (clean 34, ADX 36, RVol 1.0) |
| 2 | **SHOP** | 145.15 | FLIP CROSS up into positive gamma | **CALLS** | 23 | none: 23 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$12k | 145.12 | 150 | 140 | -$219k | - | out (clean 32, ADX 21, RVol 0.3) |
| 3 | **AAPL** | 348.26 | - | **-** | 22 | - | POS +$431.2M | 337.2 | 350 | 340 | +$17.2M | +$282k bull / +$0 bear | out (clean 28, ADX 13, RVol 0.4) |
| 4 | **AVGO** | 331.64 | - | **-** | 21 | - | NEG -$4.7M | 335.14 | 340 | 340 | -$12.0M | +$372k bull / -$58k bear | out (clean 34, ADX 32, RVol 0.7) |
| 5 | **MSFT** | 532.96 | - | **-** | 20 | - | POS +$427.8M | 505.96 | 550 | 500 | +$12.4M | +$234k bull / +$0 bear | out (clean 32, ADX 20, RVol 0.4) |
| 6 | **AMD** | 516.71 | - | **-** | 18 | - | POS +$47.3M | - | 500 | 500 | -$50.0M | +$370k bull / -$761k bear | out (clean 33, ADX 21, RVol 0.8) |
| 7 | **SPY** | 748.85 | - | **-** | 17 | - | NEG -$6.7B | 760.64 | 750 | 750 | +$22.4M | +$4.7M bull / -$571k bear | out (clean 32, ADX 28, RVol 0.6) |
| 8 | **NVDA** | 168.19 | - | **-** | 17 | - | NEG -$157.7M | - | 180 | 170 | +$12.7M | +$1.1M bull / -$2.2M bear | out (clean 33, ADX 16, RVol 1.6) |
| 9 | **META** | 643.15 | - | **-** | 16 | - | POS +$270.4M | 607.59 | 650 | 650 | -$659k | +$0 bull / -$115k bear | out (clean 32, ADX 25, RVol 0.5) |
| 10 | **PLTR** | 166.58 | - | **-** | 16 | - | POS +$50.4M | - | 165 | 170 | -$919k | +$0 bull / -$57k bear | out (clean 28, ADX 14, RVol 0.4) |
| 11 | **QQQ** | 673.03 | - | **-** | 15 | - | NEG -$1.9B | 693 | 672 | 680 | -$1.1M | +$1.3M bull / -$253k bear | out (clean 32, ADX 26, RVol 0.3) |
| 12 | **MU** | 715.43 | - | **-** | 15 | - | NEG -$29.6M | - | 750 | 750 | -$21.9M | +$880k bull / -$610k bear | out (clean 31, ADX 18, RVol 0.3) |
| 13 | **SMH** | 482.28 | - | **-** | 14 | - | NEG -$212.5M | - | 500 | 475 | -$181k | +$0 bull / -$106k bear | out (clean 29, ADX 15, RVol 0.3) |
| 14 | **TSLA** | 377.65 | - | **-** | 14 | - | POS +$208.5M | - | 400 | 380 | -$6.3M | +$1.3M bull / +$0 bear | out (clean 32, ADX 12, RVol 0.5) |
| 15 | **ORCL** | 117.36 | - | **-** | 14 | - | NEG -$25.1M | - | 120 | 120 | +$262k | +$48k bull / -$115k bear | out (clean 27, ADX 16, RVol 0.3) |
| 16 | **ARM** | 179.85 | - | **-** | 12 | - | NEG -$5.0M | - | 185 | 190 | -$223k | - | out (clean 27, ADX 20, RVol 1.2) |
| 17 | **CRM** | 211.65 | - | **-** | 11 | - | NEG -$11.2M | - | 195 | 220 | +$310k | - | out (clean 31, ADX 17, RVol 0.3) |
| 18 | **UBER** | 69.72 | - | **-** | 9 | - | POS +$7.6M | 68.48 | 70 | 70 | -$70k | - | out (clean 33, ADX 21, RVol 0.4) |
| 19 | **GOOGL** | 286.99 | - | **-** | 7 | - | NEG -$21.8M | 288.92 | 300 | 290 | +$2.5M | - | out (clean 29, ADX 17, RVol 0.3) |
| 20 | **HOOD** | 80.80 | - | **-** | 7 | - | POS +$1.8M | 79.83 | 85 | 80 | +$587k | - | out (clean 32, ADX 15, RVol 0.3) |
| 21 | **BABA** | 102.51 | - | **-** | 7 | - | NEG -$9.6M | 106.21 | 110 | 100 | -$153k | - | out (clean 30, ADX 22, RVol 0.5) |
| 22 | **NFLX** | 62.85 | - | **-** | 6 | - | NEG -$22.2M | 65.13 | 65 | 60 | -$195k | - | out (clean 29, ADX 16, RVol 0.5) |
| 23 | **COIN** | 131.41 | - | **-** | 5 | - | POS +$3.6M | 129.23 | 137 | 135 | +$186k | - | out (clean 28, ADX 15, RVol 0.3) |
| 24 | **DELL** | 331.27 | - | **-** | 5 | - | NEG -$10.8M | - | 350 | 340 | +$914k | - | out (clean 34, ADX 16, RVol 0.3) |
| 25 | **SMCI** | 27.64 | - | **-** | 5 | - | POS +$1.2M | 26.42 | 30 | 25 | -$44k | - | out (clean 30, ADX 14, RVol 0.7) |
| 26 | **IWM** | 280.08 | - | **-** | 4 | - | NEG -$939.9M | 283.03 | 280 | 280 | +$1.5M | - | out (clean 35, ADX 16, RVol 0.4) |
| 27 | **MSTR** | 120.02 | - | **-** | 4 | - | NEG -$26.1M | - | 130 | 110 | +$550k | - | out (clean 29, ADX 12, RVol 0.3) |

## Big prints this scan (50)
- **NVDA** CALL 172.5 2026-11-13 (3DTE): 1,499 @ 2.43 = **+$364k** SELL | vol 22,045 / OI 58
- **SPY** CALL 754 2026-11-12 (2DTE): 1,698 @ 1.60 = **+$272k** BUY | vol 3,920 / OI 771
- **SPY** PUT 760 2026-11-13 (3DTE): 162 @ 11.74 = **+$190k** BUY | vol 45,268 / OI 5,844
- **SPY** PUT 760 2026-11-13 (3DTE): 162 @ 11.74 = **+$190k** BUY | vol 45,268 / OI 5,844
- **SPY** PUT 760 2026-11-13 (3DTE): 162 @ 11.74 = **+$190k** BUY | vol 45,268 / OI 5,844
- **MSFT** CALL 555 2026-11-13 (3DTE): 2,500 @ 0.66 = **+$165k** BUY | vol 1,896 / OI 2,701
- **NVDA** CALL 172.5 2026-11-16 (6DTE): 500 @ 3.12 = **+$156k** SELL | vol 17,027 / OI 10
- **NVDA** CALL 172.5 2026-11-16 (6DTE): 500 @ 3.10 = **+$155k** SELL | vol 17,027 / OI 10
- **NVDA** CALL 172.5 2026-11-16 (6DTE): 500 @ 3.10 = **+$155k** SELL | vol 17,027 / OI 10
- **QQQ** PUT 676 2026-11-11 (1DTE): 250 @ 5.90 = **+$148k** BUY | vol 4,965 / OI 845
- **NVDA** CALL 172.5 2026-11-16 (6DTE): 467 @ 3.10 = **+$145k** SELL | vol 17,027 / OI 10
- **QQQ** CALL 673 2026-11-12 (2DTE): 185 @ 5.68 = **+$105k** SELL | vol 2,761 / OI 224
- **NVDA** CALL 172.5 2026-11-16 (6DTE): 307 @ 3.10 = **+$95k** SELL | vol 17,027 / OI 10
- **NVDA** CALL 160 2026-11-11 (1DTE): 100 @ 7.95 = **+$80k** SELL | vol 3,012 / OI 34
- **AMD** PUT 515 2026-11-13 (3DTE): 40 @ 16.50 = **+$66k** BUY | vol 1,274 / OI 349

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 710 2026-11-11 (1DTE): 2,227 traded vs OI 1,878
- **SPY** CALL 806 2026-11-13 (3DTE): 1,648 traded vs OI 1,581
- **SPY** CALL 769 2026-11-11 (1DTE): 954 traded vs OI 825
- **SPY** CALL 775 2026-11-19 (9DTE): 648 traded vs OI 586
- **SPY** PUT 714 2026-11-16 (6DTE): 2,204 traded vs OI 63
- **SPY** CALL 750 2026-11-18 (8DTE): 599 traded vs OI 280
- **SPY** CALL 796 2026-11-18 (8DTE): 1,000 traded vs OI 0
- **QQQ** CALL 740 2026-11-30 (20DTE): 629 traded vs OI 0
- **NVDA** PUT 185 2026-11-11 (1DTE): 1,903 traded vs OI 0
- **NVDA** PUT 185 2026-11-13 (3DTE): 3,128 traded vs OI 0
- **NVDA** PUT 185 2026-11-27 (17DTE): 1,536 traded vs OI 0
- **NVDA** CALL 185 2026-11-23 (13DTE): 503 traded vs OI 0
- **NVDA** PUT 185 2026-11-20 (10DTE): 1,286 traded vs OI 0
- **AMZN** PUT 260 2026-11-13 (3DTE): 2,506 traded vs OI 2,484
- **AVGO** PUT 300 2026-11-13 (3DTE): 1,385 traded vs OI 1,252

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
