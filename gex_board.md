# GEX + FLOW SCAN - Fri Oct 30, 03:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:30:08 ET, last candle SPY 15:29, QQQ 15:29 | no errors
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
| 1 | **ORCL** | 129.70 | PINNED between the walls (positive gamma) - chop | **-** | 34 | - | POS +$46.1M | 128.95 | 130 | 130 | +$2.9M | +$142k bull / +$0 bear | out (clean 34, ADX 21, RVol 0.8) |
| 2 | **DELL** | 419.27 | - | **-** | 29 | - | NEG -$55.6M | - | 440 | 425 | +$8.5M | +$38k bull / -$237k bear | out (clean 34, ADX 31, RVol 2.1) |
| 3 | **COIN** | 140.45 | - | **-** | 28 | - | NEG -$17.5M | - | 140 | 140 | -$4.9M | +$0 bull / -$1.0M bear | out (clean 27, ADX 37, RVol 3.3) |
| 4 | **SPY** | 752.81 | - | **-** | 27 | - | NEG -$17.3B | 771.47 | 800 | 750 | +$273.8M | +$2.9M bull / -$6.3M bear | out (clean 28, ADX 42, RVol 2.7) |
| 5 | **AMD** | 498.16 | - | **-** | 27 | - | NEG -$178.0M | 517.09 | 500 | 500 | +$34.6M | +$0 bull / -$845k bear | out (clean 30, ADX 34, RVol 2.4) |
| 6 | **NVDA** | 202.76 | - | **-** | 26 | - | NEG -$445.2M | 211.73 | 210 | 200 | +$35.4M | +$3.2M bull / -$1.2M bear | out (clean 29, ADX 40, RVol 1.9) |
| 7 | **QQQ** | 687.26 | - | **-** | 24 | - | NEG -$10.7B | - | 720 | 690 | +$114.3M | +$1.4M bull / -$6.9M bear | out (clean 29, ADX 42, RVol 2.3) |
| 8 | **MU** | 868.87 | - | **-** | 23 | - | NEG -$355.7M | - | 880 | 880 | +$68.1M | +$2.5M bull / -$8.2M bear | out (clean 31, ADX 31, RVol 1.4) |
| 9 | **MSTR** | 130.72 | - | **-** | 23 | - | NEG -$21.3M | 134.44 | 135 | 130 | -$10.5M | +$0 bull / -$4.6M bear | out (clean 28, ADX 27, RVol 1.6) |
| 10 | **SMH** | 518.04 | - | **-** | 22 | - | NEG -$603.4M | - | 532.5 | 530 | +$3.0M | +$30k bull / -$770k bear | out (clean 31, ADX 36, RVol 1.9) |
| 11 | **AAPL** | 343.50 | - | **-** | 22 | - | POS +$140.1M | 342.59 | 345 | 345 | +$12.8M | +$124k bull / -$488k bear | out (clean 32, ADX 36, RVol 1.4) |
| 12 | **AVGO** | 323.17 | - | **-** | 22 | - | NEG -$172.7M | - | 340 | 320 | +$2.3M | +$0 bull / -$34k bear | out (clean 30, ADX 36, RVol 1.3) |
| 13 | **IWM** | 278.38 | - | **-** | 21 | - | NEG -$1.2B | 281.05 | 278 | 278 | +$7.9M | +$0 bull / -$951k bear | out (clean 30, ADX 35, RVol 1.3) |
| 14 | **META** | 612.61 | - | **-** | 21 | - | NEG -$206.0M | 618.83 | 615 | 610 | +$7.7M | +$841k bull / -$1.0M bear | out (clean 30, ADX 45, RVol 0.4) |
| 15 | **SMCI** | 32.23 | - | **-** | 21 | - | NEG -$4.8M | 32.59 | 35 | 32 | +$113k | +$0 bull / -$206k bear | out (clean 30, ADX 42, RVol 1.6) |
| 16 | **HOOD** | 83.44 | - | **-** | 21 | - | NEG -$39.9M | - | 85 | 85 | +$1.0M | +$0 bull / -$41k bear | out (clean 31, ADX 39, RVol 1.0) |
| 17 | **GOOGL** | 277.80 | - | **-** | 20 | - | NEG -$197.2M | - | 280 | 280 | +$2.9M | +$35k bull / -$751k bear | out (clean 33, ADX 35, RVol 0.7) |
| 18 | **SHOP** | 156.19 | - | **-** | 20 | - | NEG -$20.2M | - | 160 | 157.5 | +$619k | - | out (clean 28, ADX 32, RVol 2.9) |
| 19 | **TSLA** | 398.00 | - | **-** | 19 | - | POS +$286.2M | 395.9 | 400 | 400 | -$5.2M | +$919k bull / -$1.4M bear | out (clean 30, ADX 25, RVol 1.9) |
| 20 | **MSFT** | 522.17 | - | **-** | 19 | - | POS +$538.0M | 517.96 | 525 | 525 | +$4.5M | +$0 bull / -$527k bear | out (clean 26, ADX 19, RVol 0.9) |
| 21 | **BABA** | 97.80 | - | **-** | 19 | - | NEG -$60.4M | 98.59 | 100 | 98 | +$669k | - | out (clean 31, ADX 36, RVol 1.1) |
| 22 | **PLTR** | 185.63 | - | **-** | 17 | - | NEG -$78.8M | 192.32 | 185 | 185 | +$1.7M | +$0 bull / -$789k bear | out (clean 26, ADX 20, RVol 1.1) |
| 23 | **AMZN** | 239.19 | - | **-** | 16 | - | NEG -$191.4M | 246.87 | 250 | 240 | -$4.6M | +$79k bull / -$221k bear | out (clean 30, ADX 16, RVol 1.2) |
| 24 | **NFLX** | 61.80 | - | **-** | 15 | - | NEG -$33.3M | 62.29 | 62 | 62 | +$1.5M | - | out (clean 30, ADX 36, RVol 1.0) |
| 25 | **UBER** | 65.04 | - | **-** | 13 | - | NEG -$36.6M | 66.21 | 65 | 65 | +$393k | - | out (clean 26, ADX 14, RVol 0.7) |
| 26 | **CRM** | 228.49 | - | **-** | 13 | - | NEG -$27.1M | 235.66 | 230 | 230 | +$346k | - | out (clean 27, ADX 30, RVol 1.2) |
| 27 | **ARM** | 204.88 | - | **-** | 11 | - | NEG -$21.1M | - | 205 | 205 | +$267k | - | out (clean 26, ADX 31, RVol 2.0) |

## Big prints this scan (111)
- **SPY** CALL 750 2026-11-03 (4DTE): 918 @ 7.07 = **+$649k** BUY | vol 22,159 / OI 23
- **META** CALL 612.5 2026-11-02 (3DTE): 699 @ 7.80 = **+$545k** BUY | vol 1,637 / OI 116
- **QQQ** PUT 715 2026-11-06 (7DTE): 150 @ 29.58 = **+$444k** MID | vol 1,244 / OI 10,393
- **NVDA** CALL 207.5 2026-11-06 (7DTE): 1,500 @ 2.94 = **+$441k** BUY | vol 29,143 / OI 171
- **NVDA** CALL 207.5 2026-11-06 (7DTE): 1,500 @ 2.94 = **+$441k** BUY | vol 29,143 / OI 171
- **SPY** PUT 748 2026-11-02 (3DTE): 1,996 @ 1.94 = **+$387k** SELL | vol 18,256 / OI 502
- **QQQ** PUT 710 2026-11-06 (7DTE): 150 @ 25.58 = **+$384k** SELL | vol 1,560 / OI 23,398
- **QQQ** CALL 685 2026-11-02 (3DTE): 453 @ 7.05 = **+$319k** BUY | vol 25,474 / OI 23
- **NVDA** CALL 210 2026-11-06 (7DTE): 1,505 @ 2.06 = **+$310k** BUY | vol 33,223 / OI 950
- **NVDA** CALL 210 2026-11-06 (7DTE): 1,505 @ 2.06 = **+$310k** BUY | vol 33,223 / OI 950
- **IWM** CALL 276 2026-10-30 (0DTE): 1,300 @ 2.25 = **+$292k** SELL | vol 4,345 / OI 2,880
- **MU** CALL 865 2026-11-02 (3DTE): 142 @ 18.70 = **+$266k** BUY | vol 1,362 / OI 463
- **SPY** PUT 770 2026-11-06 (7DTE): 150 @ 17.55 = **+$263k** SELL | vol 4,477 / OI 4,714
- **AAPL** PUT 335 2026-11-06 (7DTE): 490 @ 5.11 = **+$250k** BUY | vol 8,956 / OI 2,538
- **TSLA** CALL 410 2026-11-06 (7DTE): 435 @ 5.75 = **+$250k** BUY | vol 10,014 / OI 2,432

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 745 2026-11-02 (3DTE): 508 traded vs OI 18
- **SPY** CALL 750 2026-11-09 (10DTE): 590 traded vs OI 6
- **SPY** PUT 710 2026-11-10 (11DTE): 501 traded vs OI 50
- **SPY** CALL 754 2026-11-13 (14DTE): 712 traded vs OI 164
- **QQQ** PUT 663 2026-10-30 (0DTE): 2,737 traded vs OI 2,262
- **QQQ** PUT 664 2026-10-30 (0DTE): 1,375 traded vs OI 1,187
- **QQQ** PUT 689 2026-11-06 (7DTE): 926 traded vs OI 912
- **QQQ** CALL 730 2026-11-27 (28DTE): 761 traded vs OI 756
- **QQQ** CALL 690 2026-11-20 (21DTE): 2,560 traded vs OI 2,550
- **IWM** PUT 266 2026-11-06 (7DTE): 513 traded vs OI 511
- **SMH** CALL 540 2026-11-02 (3DTE): 846 traded vs OI 27
- **SMH** PUT 475 2026-11-06 (7DTE): 517 traded vs OI 0
- **NVDA** CALL 220 2026-11-27 (28DTE): 2,995 traded vs OI 2,882
- **NVDA** CALL 182.5 2026-11-06 (7DTE): 617 traded vs OI 0
- **TSLA** PUT 370 2026-11-27 (28DTE): 948 traded vs OI 947

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
