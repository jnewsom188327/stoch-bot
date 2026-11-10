# GEX + FLOW SCAN - Tue Nov 10, 02:10 PM ET
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
Last 1m check 14:10:08 ET, last candle SPY 14:09, QQQ 14:09 | no errors
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
| 1 | **MSFT** | 535.20 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 40 | none: 129 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$472.5M | 505.28 | 550 | 535 | +$12.2M | +$0 bull / -$286k bear | out (clean 32, ADX 35, RVol 0.5) |
| 2 | **AMZN** | 270.27 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 35 | none: 63 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | POS +$470.6M | - | 270 | 265 | +$3.7M | +$106k bull / -$1.9M bear | out (clean 32, ADX 20, RVol 0.7) |
| 3 | **AAPL** | 348.43 | - | **-** | 22 | - | POS +$432.8M | 336.66 | 350 | 340 | +$17.0M | +$0 bull / -$25k bear | out (clean 28, ADX 11, RVol 0.3) |
| 4 | **GOOGL** | 287.19 | - | **-** | 19 | - | NEG -$17.6M | 288.85 | 300 | 290 | +$2.6M | +$0 bull / -$316k bear | out (clean 30, ADX 26, RVol 0.3) |
| 5 | **AVGO** | 330.83 | - | **-** | 19 | - | NEG -$11.9M | 343.43 | 340 | 340 | -$11.2M | +$0 bull / -$212k bear | out (clean 33, ADX 20, RVol 0.6) |
| 6 | **AMD** | 514.04 | - | **-** | 17 | - | POS +$44.6M | - | 500 | 500 | -$51.4M | +$0 bull / -$808k bear | out (clean 34, ADX 19, RVol 0.3) |
| 7 | **PLTR** | 166.48 | - | **-** | 17 | - | POS +$53.3M | - | 165 | 170 | -$977k | +$0 bull / -$132k bear | out (clean 28, ADX 20, RVol 0.2) |
| 8 | **NVDA** | 168.69 | - | **-** | 16 | - | NEG -$171.3M | - | 185 | 170 | +$7.0M | +$908k bull / -$361k bear | out (clean 34, ADX 18, RVol 0.9) |
| 9 | **SPY** | 748.90 | - | **-** | 15 | - | NEG -$6.4B | 760.08 | 750 | 750 | +$37.4M | +$0 bull / -$1.0M bear | out (clean 32, ADX 22, RVol 0.3) |
| 10 | **QQQ** | 672.55 | - | **-** | 15 | - | NEG -$1.9B | 692.54 | 680 | 680 | -$8.9M | +$0 bull / -$4.0M bear | out (clean 33, ADX 23, RVol 0.2) |
| 11 | **MU** | 714.96 | - | **-** | 15 | - | NEG -$30.9M | - | 750 | 750 | -$23.3M | +$0 bull / -$1.9M bear | out (clean 31, ADX 19, RVol 0.2) |
| 12 | **META** | 640.78 | - | **-** | 14 | - | POS +$241.7M | 607.86 | 650 | 650 | -$138k | +$0 bull / -$142k bear | out (clean 32, ADX 16, RVol 0.3) |
| 13 | **TSLA** | 377.48 | - | **-** | 13 | - | POS +$193.0M | - | 400 | 380 | -$5.6M | +$62k bull / -$807k bear | out (clean 32, ADX 12, RVol 0.2) |
| 14 | **CRM** | 211.41 | - | **-** | 13 | - | NEG -$11.1M | - | 195 | 220 | +$299k | - | out (clean 31, ADX 27, RVol 0.2) |
| 15 | **SHOP** | 144.31 | - | **-** | 12 | - | NEG -$59k | 144.65 | 150 | 140 | -$190k | - | out (clean 33, ADX 28, RVol 0.4) |
| 16 | **ARM** | 179.09 | - | **-** | 11 | - | NEG -$4.8M | - | 185 | 190 | -$222k | - | out (clean 28, ADX 19, RVol 0.9) |
| 17 | **HOOD** | 80.88 | - | **-** | 9 | - | POS +$2.6M | 79.24 | 85 | 80 | +$596k | - | out (clean 31, ADX 28, RVol 0.3) |
| 18 | **UBER** | 69.29 | - | **-** | 9 | - | POS +$5.0M | 68.39 | 70 | 70 | -$48k | - | out (clean 33, ADX 31, RVol 0.3) |
| 19 | **BABA** | 102.76 | - | **-** | 9 | - | NEG -$8.7M | 105.98 | 110 | 100 | -$160k | - | out (clean 31, ADX 35, RVol 0.5) |
| 20 | **DELL** | 331.28 | - | **-** | 7 | - | NEG -$10.7M | - | 350 | 340 | +$861k | - | out (clean 34, ADX 26, RVol 0.3) |
| 21 | **NFLX** | 62.80 | - | **-** | 6 | - | NEG -$23.1M | 65.23 | 65 | 60 | -$151k | - | out (clean 29, ADX 19, RVol 0.3) |
| 22 | **COIN** | 131.06 | - | **-** | 6 | - | POS +$3.0M | 128.97 | 137 | 135 | +$184k | - | out (clean 29, ADX 21, RVol 0.2) |
| 23 | **SMCI** | 27.80 | - | **-** | 6 | - | POS +$3.1M | - | 30 | 30 | -$64k | - | out (clean 30, ADX 24, RVol 0.3) |
| 24 | **ORCL** | 117.61 | - | **-** | 6 | - | NEG -$24.4M | - | 120 | 120 | +$211k | - | out (clean 28, ADX 27, RVol 0.2) |
| 25 | **IWM** | 280.30 | - | **-** | 4 | - | NEG -$903.1M | 283.28 | 280 | 270 | +$1.7M | - | out (clean 36, ADX 16, RVol 0.4) |
| 26 | **SMH** | 481.59 | - | **-** | 4 | - | NEG -$215.1M | - | 500 | 475 | -$129k | - | out (clean 30, ADX 20, RVol 0.2) |
| 27 | **MSTR** | 120.81 | - | **-** | 4 | - | NEG -$20.7M | - | 132 | 110 | +$264k | - | out (clean 30, ADX 17, RVol 0.5) |

## Big prints this scan (68)
- **TSLA** CALL 362.5 2026-11-13 (3DTE): 269 @ 16.80 = **+$452k** SELL | vol 744 / OI 7,929
- **TSLA** CALL 375 2026-11-13 (3DTE): 269 @ 8.30 = **+$223k** SELL | vol 5,713 / OI 5,621
- **AMZN** PUT 270 2026-11-13 (3DTE): 456 @ 4.10 = **+$187k** BUY | vol 8,225 / OI 829
- **QQQ** CALL 673 2026-11-11 (1DTE): 468 @ 3.43 = **+$161k** SELL | vol 7,768 / OI 232
- **AMZN** PUT 270 2026-11-13 (3DTE): 273 @ 4.10 = **+$112k** BUY | vol 8,225 / OI 829
- **QQQ** PUT 670 2026-11-11 (1DTE): 266 @ 4.15 = **+$110k** BUY | vol 41,714 / OI 452
- **AMZN** PUT 272.5 2026-11-13 (3DTE): 193 @ 5.50 = **+$106k** BUY | vol 2,829 / OI 339
- **AMZN** PUT 270 2026-11-13 (3DTE): 250 @ 4.10 = **+$102k** BUY | vol 8,225 / OI 829
- **MSFT** CALL 525 2026-11-11 (1DTE): 100 @ 10.10 = **+$101k** SELL | vol 531 / OI 69
- **AMZN** PUT 270 2026-11-13 (3DTE): 216 @ 4.10 = **+$89k** BUY | vol 8,225 / OI 829
- **AMZN** PUT 270 2026-11-13 (3DTE): 199 @ 4.10 = **+$82k** BUY | vol 8,225 / OI 829
- **AMZN** PUT 270 2026-11-13 (3DTE): 197 @ 4.10 = **+$81k** BUY | vol 8,225 / OI 829
- **AMZN** PUT 270 2026-11-13 (3DTE): 192 @ 4.10 = **+$79k** BUY | vol 8,225 / OI 829
- **AMZN** PUT 270 2026-11-13 (3DTE): 188 @ 4.10 = **+$77k** BUY | vol 8,225 / OI 829
- **AMZN** PUT 270 2026-11-13 (3DTE): 165 @ 4.10 = **+$68k** BUY | vol 8,225 / OI 829

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 764 2026-11-16 (6DTE): 982 traded vs OI 662
- **QQQ** CALL 687 2026-11-12 (2DTE): 501 traded vs OI 137
- **QQQ** CALL 686 2026-11-13 (3DTE): 501 traded vs OI 430
- **AAPL** PUT 315 2026-11-13 (3DTE): 508 traded vs OI 0
- **AMD** CALL 510 2026-11-16 (6DTE): 502 traded vs OI 49
- **AMZN** PUT 267.5 2026-11-20 (10DTE): 502 traded vs OI 384
- **MSFT** CALL 525 2026-11-11 (1DTE): 531 traded vs OI 69
- **AVGO** PUT 327.5 2026-11-13 (3DTE): 502 traded vs OI 188
- **BABA** CALL 103 2026-11-13 (3DTE): 701 traded vs OI 696

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
