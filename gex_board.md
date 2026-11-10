# GEX + FLOW SCAN - Tue Nov 10, 02:20 PM ET
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
Last 1m check 14:20:08 ET, last candle SPY 14:19, QQQ 14:19 | no errors
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
| 1 | **MSFT** | 533.92 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 39 | none: 126 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (16 contracts' greeks worked out here) | POS +$462.2M | 504.51 | 550 | 535 | +$12.2M | +$0 bull / -$183k bear | out (clean 32, ADX 31, RVol 0.4) |
| 2 | **AMZN** | 270.15 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 35 | none: 63 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$472.4M | - | 270 | 265 | +$3.1M | +$0 bull / -$1.9M bear | out (clean 33, ADX 20, RVol 0.7) |
| 3 | **AVGO** | 330.43 | - | **-** | 20 | - | NEG -$10.8M | 341 | 340 | 340 | -$11.8M | +$0 bull / -$181k bear | out (clean 33, ADX 23, RVol 0.7) |
| 4 | **GOOGL** | 287.01 | - | **-** | 19 | - | NEG -$19.8M | 288.81 | 300 | 290 | +$2.5M | +$0 bull / -$316k bear | out (clean 30, ADX 23, RVol 0.2) |
| 5 | **HOOD** | 80.83 | - | **-** | 19 | - | POS +$2.3M | 79.27 | 85 | 80 | +$552k | +$0 bull / -$26k bear | out (clean 32, ADX 25, RVol 0.3) |
| 6 | **AMD** | 512.62 | - | **-** | 17 | - | POS +$52.7M | - | 500 | 500 | -$47.8M | +$1.5M bull / -$516k bear | out (clean 34, ADX 19, RVol 0.3) |
| 7 | **PLTR** | 166.08 | - | **-** | 17 | - | POS +$52.4M | - | 165 | 170 | -$996k | +$0 bull / -$132k bear | out (clean 28, ADX 18, RVol 0.3) |
| 8 | **SPY** | 748.30 | - | **-** | 16 | - | NEG -$6.7B | 760.26 | 750 | 750 | +$36.6M | +$103k bull / +$0 bear | out (clean 32, ADX 23, RVol 0.4) |
| 9 | **QQQ** | 671.94 | - | **-** | 15 | - | NEG -$2.0B | 692.52 | 680 | 680 | -$7.8M | +$1.2M bull / -$271k bear | out (clean 33, ADX 24, RVol 0.3) |
| 10 | **NVDA** | 168.10 | - | **-** | 15 | - | NEG -$158.2M | - | 180 | 170 | +$4.4M | +$256k bull / -$1.7M bear | out (clean 34, ADX 17, RVol 1.0) |
| 11 | **MU** | 712.28 | - | **-** | 15 | - | NEG -$30.5M | - | 750 | 750 | -$23.6M | +$256k bull / -$1.3M bear | out (clean 31, ADX 19, RVol 0.1) |
| 12 | **META** | 641.40 | - | **-** | 14 | - | POS +$243.6M | 606.95 | 650 | 650 | -$523k | +$0 bull / -$184k bear | out (clean 32, ADX 16, RVol 0.3) |
| 13 | **TSLA** | 377.49 | - | **-** | 13 | - | POS +$193.9M | - | 400 | 380 | -$5.9M | +$65k bull / -$789k bear | out (clean 32, ADX 11, RVol 0.2) |
| 14 | **ARM** | 178.67 | - | **-** | 13 | - | NEG -$4.9M | - | 185 | 185 | -$224k | - | out (clean 28, ADX 20, RVol 1.6) |
| 15 | **CRM** | 210.90 | - | **-** | 13 | - | NEG -$10.9M | - | 195 | 220 | +$311k | - | out (clean 31, ADX 25, RVol 0.3) |
| 16 | **AAPL** | 348.35 | - | **-** | 12 | - | POS +$438.0M | 336.4 | 350 | 340 | +$16.9M | - | out (clean 28, ADX 11, RVol 0.3) |
| 17 | **SHOP** | 144.35 | - | **-** | 11 | - | NEG -$68k | 144.53 | 150 | 140 | -$189k | - | out (clean 33, ADX 25, RVol 0.3) |
| 18 | **UBER** | 69.33 | - | **-** | 10 | - | POS +$5.4M | 68.35 | 70 | 70 | -$53k | - | out (clean 33, ADX 32, RVol 0.2) |
| 19 | **BABA** | 102.63 | - | **-** | 9 | - | NEG -$9.6M | 106.25 | 110 | 100 | -$159k | - | out (clean 31, ADX 30, RVol 0.5) |
| 20 | **DELL** | 330.70 | - | **-** | 7 | - | NEG -$10.9M | - | 350 | 340 | +$910k | - | out (clean 34, ADX 25, RVol 0.4) |
| 21 | **COIN** | 130.93 | - | **-** | 6 | - | POS +$2.4M | 129.06 | 137 | 135 | +$193k | - | out (clean 29, ADX 20, RVol 0.3) |
| 22 | **SMCI** | 27.66 | - | **-** | 6 | - | POS +$1.1M | 26.43 | 30 | 25 | -$64k | - | out (clean 30, ADX 23, RVol 0.3) |
| 23 | **ORCL** | 117.25 | - | **-** | 6 | - | NEG -$24.9M | - | 120 | 120 | +$238k | - | out (clean 28, ADX 26, RVol 0.2) |
| 24 | **NFLX** | 62.81 | - | **-** | 5 | - | NEG -$22.5M | 65.1 | 65 | 60 | -$176k | - | out (clean 29, ADX 17, RVol 0.4) |
| 25 | **IWM** | 280.06 | - | **-** | 4 | - | NEG -$1.0B | 283.39 | 280 | 270 | +$1.8M | - | out (clean 36, ADX 16, RVol 0.4) |
| 26 | **SMH** | 480.94 | - | **-** | 4 | - | NEG -$217.7M | - | 500 | 475 | -$138k | - | out (clean 30, ADX 20, RVol 0.2) |
| 27 | **MSTR** | 120.35 | - | **-** | 4 | - | NEG -$21.1M | - | 132 | 110 | +$300k | - | out (clean 30, ADX 16, RVol 0.5) |

## Big prints this scan (24)
- **AMD** PUT 530 2026-11-11 (1DTE): 130 @ 20.75 = **+$270k** SELL | vol 4,646 / OI 45
- **META** CALL 640 2026-11-11 (1DTE): 170 @ 6.20 = **+$105k** SELL | vol 3,996 / OI 239
- **AMD** PUT 530 2026-11-11 (1DTE): 48 @ 20.75 = **+$100k** SELL | vol 4,646 / OI 45
- **MU** CALL 740 2026-11-11 (1DTE): 199 @ 4.40 = **+$88k** BUY | vol 11,911 / OI 238
- **AMD** CALL 512.5 2026-11-11 (1DTE): 77 @ 10.40 = **+$80k** BUY | vol 5,656 / OI 442
- **NVDA** CALL 172.5 2026-11-16 (6DTE): 241 @ 3.29 = **+$79k** SELL | vol 13,410 / OI 10
- **NVDA** CALL 162.5 2026-11-16 (6DTE): 84 @ 8.65 = **+$73k** SELL | vol 582 / OI 18
- **AMD** PUT 512.5 2026-11-13 (3DTE): 40 @ 16.50 = **+$66k** BUY | vol 899 / OI 314
- **NVDA** CALL 170 2026-11-11 (1DTE): 226 @ 1.90 = **+$43k** SELL | vol 123,957 / OI 252
- **TSLA** PUT 367.5 2026-11-11 (1DTE): 330 @ 1.23 = **+$41k** BUY | vol 12,031 / OI 371
- **NVDA** CALL 170 2026-11-13 (3DTE): 99 @ 3.55 = **+$35k** SELL | vol 27,639 / OI 389
- **AMD** CALL 517.5 2026-11-11 (1DTE): 43 @ 8.15 = **+$35k** BUY | vol 3,867 / OI 13
- **NVDA** CALL 172.5 2026-11-16 (6DTE): 103 @ 3.29 = **+$34k** SELL | vol 13,410 / OI 10
- **NVDA** CALL 172.5 2026-11-16 (6DTE): 100 @ 3.29 = **+$33k** SELL | vol 13,410 / OI 10
- **AMD** CALL 515 2026-11-13 (3DTE): 20 @ 15.70 = **+$31k** BUY | vol 1,943 / OI 758

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 703 2026-11-11 (1DTE): 732 traded vs OI 215
- **SPY** PUT 702 2026-11-11 (1DTE): 1,206 traded vs OI 963
- **SPY** PUT 736 2026-11-12 (2DTE): 627 traded vs OI 623
- **SPY** CALL 770 2026-11-17 (7DTE): 703 traded vs OI 661
- **SPY** CALL 817 2026-11-20 (10DTE): 1,376 traded vs OI 689
- **SPY** CALL 748 2026-11-27 (17DTE): 533 traded vs OI 216
- **QQQ** PUT 648 2026-11-13 (3DTE): 749 traded vs OI 741
- **QQQ** PUT 639 2026-11-11 (1DTE): 501 traded vs OI 91
- **QQQ** CALL 674 2026-11-18 (8DTE): 619 traded vs OI 42
- **IWM** CALL 292.5 2026-11-16 (6DTE): 598 traded vs OI 230
- **IWM** CALL 290 2026-11-16 (6DTE): 1,781 traded vs OI 69
- **IWM** CALL 286 2026-11-16 (6DTE): 514 traded vs OI 424
- **NVDA** CALL 162.5 2026-11-16 (6DTE): 582 traded vs OI 18
- **META** CALL 675 2026-11-13 (3DTE): 503 traded vs OI 398
- **AMZN** CALL 265 2026-11-11 (1DTE): 1,999 traded vs OI 1,889

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
