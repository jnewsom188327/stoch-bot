# GEX + FLOW SCAN - Tue Nov 10, 12:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:33 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 667P | 0.67 | 1.26 | +170% (8m) | **+88%** | +15% | 668.83 hit |
| 12:22 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 667P | 0.66 | 1.26 | +174% (19m) | **+91%** | +11% | 669.29 hit |
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
Last 1m check 12:50:08 ET, last candle SPY 12:49, QQQ 12:49 | no errors
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
| 1 | **MSFT** | 529.21 | FLOW SURGE | **CALLS** | 57 | none: 126 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (21 contracts' greeks worked out here) | POS +$364.2M | 501.69 | 550 | 500 | +$19.7M | +$3.4M bull / +$0 bear | out (clean 32, ADX 42, RVol 3.1) |
| 2 | **PLTR** | 164.68 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 37 | none: 14 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$49.0M | - | 165 | 170 | -$354k | +$35k bull / +$0 bear | out (clean 28, ADX 38, RVol 0.6) |
| 3 | **AAPL** | 347.32 | FLOW SURGE | **CALLS** | 30 | none: 81 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (17 contracts' greeks worked out here) | POS +$406.5M | 335.84 | 350 | 340 | +$18.1M | +$211k bull / +$0 bear | out (clean 28, ADX 12, RVol 0.5) |
| 4 | **DELL** | 324.28 | TREND (flow not with it) | **PUTS** | 30 | none: 26 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$10.5M | - | 350 | 340 | +$1.3M | - | SHORT (clean 34, ADX 40, RVol 1.1) |
| 5 | **CRM** | 210.26 | - | **-** | 28 | - | NEG -$10.5M | - | 195 | 220 | +$323k | +$36k bull / +$0 bear | out (clean 30, ADX 38, RVol 0.9) |
| 6 | **SHOP** | 142.39 | - | **-** | 25 | - | NEG -$1.6M | 146.72 | 150 | 140 | +$110k | - | out (clean 33, ADX 63, RVol 0.8) |
| 7 | **AMZN** | 268.22 | - | **-** | 22 | - | POS +$457.1M | - | 270 | 265 | +$9.1M | +$42k bull / +$0 bear | out (clean 33, ADX 26, RVol 1.0) |
| 8 | **GOOGL** | 286.08 | - | **-** | 22 | - | NEG -$27.1M | 288.97 | 300 | 290 | +$3.6M | +$43k bull / +$0 bear | out (clean 30, ADX 25, RVol 0.3) |
| 9 | **NVDA** | 167.10 | - | **-** | 20 | - | NEG -$152.9M | - | 180 | 170 | +$17.6M | +$4.7M bull / +$0 bear | out (clean 34, ADX 38, RVol 1.2) |
| 10 | **AMD** | 505.62 | - | **-** | 20 | - | POS +$47.9M | - | 500 | 500 | -$30.4M | +$1.5M bull / +$0 bear | out (clean 33, ADX 33, RVol 1.0) |
| 11 | **SPY** | 745.73 | - | **-** | 19 | - | NEG -$8.1B | 760.07 | 750 | 730 | +$98.3M | +$537k bull / +$0 bear | out (clean 32, ADX 31, RVol 0.4) |
| 12 | **MSTR** | 119.17 | - | **-** | 19 | - | NEG -$25.0M | - | 130 | 110 | +$451k | +$48k bull / +$0 bear | out (clean 29, ADX 36, RVol 0.7) |
| 13 | **QQQ** | 668.55 | - | **-** | 18 | - | NEG -$2.3B | 691.69 | 680 | 680 | +$48.5M | +$254k bull / +$0 bear | out (clean 32, ADX 35, RVol 0.3) |
| 14 | **SMH** | 476.64 | - | **-** | 18 | - | NEG -$224.6M | - | 500 | 475 | +$827k | +$760k bull / +$0 bear | out (clean 30, ADX 31, RVol 0.3) |
| 15 | **AVGO** | 325.76 | - | **-** | 17 | - | NEG -$17.8M | - | 340 | 320 | -$8.2M | +$166k bull / +$0 bear | out (clean 32, ADX 16, RVol 0.5) |
| 16 | **TSLA** | 375.30 | - | **-** | 15 | - | POS +$187.8M | - | 400 | 380 | -$1.9M | +$391k bull / +$0 bear | out (clean 33, ADX 22, RVol 0.3) |
| 17 | **MU** | 705.07 | - | **-** | 15 | - | NEG -$30.6M | - | 750 | 750 | -$510k | +$4.0M bull / +$0 bear | out (clean 30, ADX 28, RVol 0.2) |
| 18 | **HOOD** | 80.28 | - | **-** | 13 | - | POS +$1.9M | 79.09 | 85 | 80 | +$670k | - | out (clean 31, ADX 39, RVol 0.4) |
| 19 | **ARM** | 176.74 | - | **-** | 12 | - | NEG -$4.1M | - | 185 | 185 | -$194k | - | out (clean 28, ADX 31, RVol 0.5) |
| 20 | **COIN** | 130.02 | - | **-** | 11 | - | POS +$1.4M | 129.23 | 137 | 135 | +$255k | - | out (clean 29, ADX 41, RVol 0.6) |
| 21 | **ORCL** | 116.15 | - | **-** | 11 | - | NEG -$24.1M | - | 120 | 110 | +$727k | - | out (clean 28, ADX 36, RVol 0.4) |
| 22 | **UBER** | 69.55 | - | **-** | 10 | - | POS +$6.6M | 68.39 | 70 | 70 | -$52k | - | out (clean 33, ADX 33, RVol 0.4) |
| 23 | **SMCI** | 27.41 | - | **-** | 9 | - | POS +$979k | 26.33 | 30 | 25 | +$49k | - | out (clean 30, ADX 38, RVol 0.5) |
| 24 | **BABA** | 102.76 | - | **-** | 9 | - | NEG -$8.6M | 106.04 | 110 | 100 | -$89k | - | out (clean 30, ADX 42, RVol 0.3) |
| 25 | **IWM** | 279.57 | - | **-** | 7 | - | NEG -$1.2B | 283.71 | 280 | 270 | +$2.8M | - | out (clean 36, ADX 28, RVol 0.4) |
| 26 | **META** | 638.93 | - | **-** | 6 | - | POS +$242.4M | 603.89 | 650 | 650 | +$612k | - | out (clean 32, ADX 22, RVol 0.7) |
| 27 | **NFLX** | 62.70 | - | **-** | 6 | - | NEG -$22.7M | 65.7 | 65 | 60 | -$60k | - | out (clean 30, ADX 22, RVol 0.6) |

## Big prints this scan (69)
- **SMH** PUT 485 2026-11-13 (3DTE): 366 @ 14.50 = **+$531k** SELL | vol 2,183 / OI 308
- **NVDA** CALL 167.5 2026-11-11 (1DTE): 1,000 @ 3.10 = **+$310k** BUY | vol 36,507 / OI 80
- **NVDA** CALL 167.5 2026-11-11 (1DTE): 1,000 @ 3.10 = **+$310k** BUY | vol 36,507 / OI 80
- **NVDA** CALL 167.5 2026-11-11 (1DTE): 701 @ 3.05 = **+$214k** BUY | vol 36,507 / OI 80
- **NVDA** CALL 167.5 2026-11-11 (1DTE): 480 @ 3.05 = **+$146k** BUY | vol 36,507 / OI 80
- **SMH** PUT 485 2026-11-13 (3DTE): 101 @ 14.45 = **+$146k** SELL | vol 2,183 / OI 308
- **QQQ** PUT 660 2026-11-13 (3DTE): 342 @ 3.95 = **+$135k** SELL | vol 16,995 / OI 7,659
- **MSFT** CALL 527.5 2026-11-13 (3DTE): 119 @ 11.25 = **+$134k** BUY | vol 285 / OI 211
- **AVGO** CALL 325 2026-11-11 (1DTE): 234 @ 5.60 = **+$131k** BUY | vol 5,057 / OI 128
- **MSFT** CALL 527.5 2026-11-13 (3DTE): 112 @ 11.25 = **+$126k** BUY | vol 285 / OI 211
- **NVDA** CALL 167.5 2026-11-11 (1DTE): 400 @ 3.10 = **+$124k** BUY | vol 36,507 / OI 80
- **NVDA** CALL 167.5 2026-11-11 (1DTE): 389 @ 3.10 = **+$121k** BUY | vol 36,507 / OI 80
- **NVDA** CALL 167.5 2026-11-11 (1DTE): 337 @ 3.05 = **+$103k** BUY | vol 36,507 / OI 80
- **NVDA** CALL 167.5 2026-11-11 (1DTE): 309 @ 3.05 = **+$94k** BUY | vol 36,507 / OI 80
- **NVDA** CALL 167.5 2026-11-11 (1DTE): 280 @ 3.05 = **+$85k** BUY | vol 36,507 / OI 80

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 760 2026-11-12 (2DTE): 2,490 traded vs OI 2,428
- **SPY** CALL 762 2026-11-20 (10DTE): 1,094 traded vs OI 1,091
- **SPY** PUT 730 2026-11-24 (14DTE): 507 traded vs OI 0
- **QQQ** PUT 675 2026-11-13 (3DTE): 5,034 traded vs OI 5,033
- **QQQ** CALL 689 2026-11-13 (3DTE): 1,297 traded vs OI 1,281
- **QQQ** PUT 633 2026-11-11 (1DTE): 586 traded vs OI 32
- **QQQ** CALL 667 2026-11-11 (1DTE): 514 traded vs OI 115
- **QQQ** CALL 674 2026-11-16 (6DTE): 510 traded vs OI 28
- **QQQ** CALL 692 2026-11-20 (10DTE): 842 traded vs OI 806
- **QQQ** PUT 671 2026-11-20 (10DTE): 510 traded vs OI 6
- **IWM** CALL 284 2026-11-11 (1DTE): 886 traded vs OI 885
- **IWM** CALL 288 2026-11-17 (7DTE): 625 traded vs OI 145
- **NVDA** CALL 155 2026-11-16 (6DTE): 575 traded vs OI 24
- **TSLA** CALL 390 2026-11-13 (3DTE): 3,356 traded vs OI 3,296
- **AMD** PUT 512.5 2026-11-13 (3DTE): 764 traded vs OI 314

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
