# GEX + FLOW SCAN - Tue Nov 10, 03:25 PM ET
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
Last 1m check 15:25:08 ET, last candle SPY 15:24, QQQ 15:24 | no errors
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
| 1 | **AMZN** | 271.75 | TREND (flow not with it) | **CALLS** | 37 | none: 66 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | POS +$492.5M | - | 270 | 265 | -$478k | +$96k bull / -$27k bear | LONG (clean 34, ADX 39, RVol 1.0) |
| 2 | **UBER** | 69.87 | PINNED between the walls (positive gamma) - chop | **-** | 22 | - | POS +$7.3M | 68.56 | 70 | 70 | -$73k | - | out (clean 34, ADX 23, RVol 0.5) |
| 3 | **AVGO** | 332.52 | - | **-** | 21 | - | NEG -$2.2M | 334.32 | 340 | 340 | -$12.3M | +$278k bull / -$249k bear | out (clean 34, ADX 33, RVol 0.7) |
| 4 | **MSFT** | 533.62 | - | **-** | 19 | - | POS +$440.9M | 506.81 | 550 | 535 | +$11.4M | +$234k bull / -$210k bear | out (clean 32, ADX 19, RVol 0.5) |
| 5 | **AMD** | 517.25 | - | **-** | 18 | - | POS +$47.2M | - | 500 | 500 | -$53.6M | +$236k bull / -$1.9M bear | out (clean 33, ADX 22, RVol 0.7) |
| 6 | **SPY** | 749.35 | - | **-** | 17 | - | NEG -$6.4B | 760.42 | 750 | 750 | +$12.6M | +$4.4M bull / -$3.2M bear | out (clean 32, ADX 29, RVol 0.7) |
| 7 | **QQQ** | 674.08 | - | **-** | 16 | - | NEG -$1.9B | 692.76 | 680 | 680 | -$11.0M | +$303k bull / -$1.9M bear | out (clean 32, ADX 27, RVol 0.3) |
| 8 | **NVDA** | 168.49 | - | **-** | 16 | - | NEG -$160.9M | - | 180 | 170 | +$6.7M | +$0 bull / -$4.4M bear | out (clean 33, ADX 14, RVol 1.5) |
| 9 | **META** | 644.51 | - | **-** | 16 | - | POS +$281.6M | - | 650 | 650 | -$1.0M | +$0 bull / -$26k bear | out (clean 32, ADX 28, RVol 0.5) |
| 10 | **PLTR** | 167.18 | - | **-** | 16 | - | POS +$54.4M | - | 165 | 170 | -$891k | +$0 bull / -$57k bear | out (clean 28, ADX 16, RVol 0.3) |
| 11 | **MU** | 718.64 | - | **-** | 16 | - | NEG -$25.4M | - | 750 | 750 | -$24.7M | +$590k bull / -$1.5M bear | out (clean 31, ADX 20, RVol 0.3) |
| 12 | **SMH** | 483.44 | - | **-** | 14 | - | NEG -$204.0M | - | 500 | 475 | -$529k | +$0 bull / -$278k bear | out (clean 30, ADX 15, RVol 0.4) |
| 13 | **TSLA** | 377.80 | - | **-** | 14 | - | POS +$214.7M | - | 400 | 380 | -$7.6M | +$637k bull / -$379k bear | out (clean 32, ADX 11, RVol 0.4) |
| 14 | **ORCL** | 117.82 | - | **-** | 14 | - | NEG -$25.0M | - | 120 | 120 | +$141k | +$48k bull / -$115k bear | out (clean 27, ADX 16, RVol 0.2) |
| 15 | **MSTR** | 120.98 | - | **-** | 13 | - | NEG -$26.1M | - | 130 | 110 | +$306k | +$0 bull / -$104k bear | out (clean 29, ADX 12, RVol 0.4) |
| 16 | **ARM** | 180.65 | - | **-** | 13 | - | NEG -$4.8M | - | 185 | 190 | -$227k | - | out (clean 27, ADX 23, RVol 1.2) |
| 17 | **AAPL** | 348.73 | - | **-** | 12 | - | POS +$428.7M | 337.77 | 350 | 340 | +$17.2M | - | out (clean 28, ADX 13, RVol 0.5) |
| 18 | **SHOP** | 145.64 | - | **-** | 12 | - | POS +$235k | 145.1 | 150 | 140 | -$220k | - | out (clean 32, ADX 22, RVol 0.5) |
| 19 | **CRM** | 212.10 | - | **-** | 11 | - | NEG -$11.8M | - | 230 | 220 | +$307k | - | out (clean 31, ADX 16, RVol 0.4) |
| 20 | **GOOGL** | 287.44 | - | **-** | 7 | - | NEG -$18.0M | 288.95 | 300 | 290 | +$2.3M | - | out (clean 29, ADX 18, RVol 0.3) |
| 21 | **HOOD** | 80.98 | - | **-** | 7 | - | POS +$1.6M | 80.06 | 85 | 80 | +$563k | - | out (clean 32, ADX 14, RVol 0.3) |
| 22 | **BABA** | 102.69 | - | **-** | 7 | - | NEG -$10.0M | 106.26 | 110 | 100 | -$163k | - | out (clean 30, ADX 19, RVol 0.7) |
| 23 | **NFLX** | 62.91 | - | **-** | 6 | - | NEG -$22.9M | 65.35 | 65 | 60 | -$195k | - | out (clean 29, ADX 16, RVol 0.6) |
| 24 | **COIN** | 131.94 | - | **-** | 6 | - | POS +$4.2M | 129.2 | 137 | 135 | +$131k | - | out (clean 28, ADX 17, RVol 0.9) |
| 25 | **DELL** | 333.33 | - | **-** | 5 | - | NEG -$10.7M | - | 350 | 340 | +$740k | - | out (clean 34, ADX 18, RVol 0.4) |
| 26 | **SMCI** | 27.84 | - | **-** | 5 | - | POS +$2.1M | - | 30 | 30 | -$52k | - | out (clean 30, ADX 14, RVol 0.6) |
| 27 | **IWM** | 280.27 | - | **-** | 4 | - | NEG -$929.2M | 283 | 280 | 280 | +$1.5M | - | out (clean 35, ADX 16, RVol 0.4) |

## Big prints this scan (71)
- **NVDA** PUT 175 2026-11-11 (1DTE): 281 @ 8.80 = **+$247k** BUY | vol 19,193 / OI 3,758
- **TSLA** PUT 380 2026-11-13 (3DTE): 300 @ 8.15 = **+$244k** BUY | vol 4,120 / OI 1,798
- **AMD** PUT 532.5 2026-11-11 (1DTE): 101 @ 20.60 = **+$208k** BUY | vol 2,282 / OI 0
- **AMD** CALL 500 2026-11-11 (1DTE): 96 @ 20.25 = **+$194k** SELL | vol 4,447 / OI 943
- **NVDA** PUT 175 2026-11-11 (1DTE): 220 @ 8.75 = **+$192k** BUY | vol 19,193 / OI 3,758
- **AMD** CALL 510 2026-11-11 (1DTE): 100 @ 13.10 = **+$131k** SELL | vol 17,388 / OI 407
- **AMD** CALL 510 2026-11-11 (1DTE): 100 @ 13.10 = **+$131k** SELL | vol 17,388 / OI 407
- **SPY** PUT 748 2026-11-10 (0DTE): 1,797 @ 0.71 = **+$128k** BUY | vol 426,290 / OI 832
- **AVGO** PUT 342.5 2026-11-11 (1DTE): 94 @ 12.80 = **+$120k** BUY | vol 204 / OI 5
- **SPY** CALL 743 2026-11-12 (2DTE): 150 @ 7.45 = **+$112k** SELL | vol 827 / OI 758
- **NVDA** PUT 175 2026-11-11 (1DTE): 119 @ 8.80 = **+$105k** BUY | vol 19,193 / OI 3,758
- **NVDA** PUT 175 2026-11-11 (1DTE): 100 @ 8.80 = **+$88k** BUY | vol 19,193 / OI 3,758
- **NVDA** CALL 175 2026-11-13 (3DTE): 500 @ 1.65 = **+$82k** SELL | vol 45,470 / OI 1,191
- **MU** PUT 747.5 2026-11-11 (1DTE): 20 @ 38.50 = **+$77k** BUY | vol 152 / OI 21
- **MU** PUT 747.5 2026-11-11 (1DTE): 20 @ 38.45 = **+$77k** BUY | vol 152 / OI 21

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 743 2026-11-12 (2DTE): 827 traded vs OI 758
- **QQQ** PUT 644 2026-11-11 (1DTE): 516 traded vs OI 61
- **SMH** CALL 505 2026-11-13 (3DTE): 826 traded vs OI 656
- **NVDA** PUT 182.5 2026-11-13 (3DTE): 3,501 traded vs OI 3,487
- **TSLA** PUT 360 2026-11-16 (6DTE): 505 traded vs OI 295
- **MSFT** PUT 522.5 2026-11-13 (3DTE): 603 traded vs OI 596
- **AVGO** CALL 365 2026-11-20 (10DTE): 530 traded vs OI 0
- **SMCI** CALL 30.5 2026-11-13 (3DTE): 747 traded vs OI 0
- **MU** CALL 790 2026-11-13 (3DTE): 1,176 traded vs OI 0
- **MSTR** CALL 133 2026-11-13 (3DTE): 2,266 traded vs OI 0
- **SHOP** CALL 160 2026-11-20 (10DTE): 583 traded vs OI 0
- **SHOP** CALL 160 2026-12-04 (24DTE): 609 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
