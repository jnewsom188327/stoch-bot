# GEX + FLOW SCAN - Fri Oct 30, 11:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.78 | +7% (5m) | **+7%** | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:30:08 ET, last candle SPY 11:29, QQQ 11:29 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:05 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 11:20 ARM CALLS: under EMA 20 - flow says one way, price says the other
- 11:20 COIN PUTS: price +0.22 over the last 15 min - flow says one way, price says the other
- 11:15 MSTR PUTS: price +1.54 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 11:10 MSTR PUTS: price +1.77 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:55 AAPL PUTS: price +1.23 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMCI** | 32.41 | FLIP CROSS down into negative gamma | **PUTS** | 35 | 10/30 33P @ 0.77 (delta 0.75) = est +23% at 32 | NEG -$212k | 32.44 | 35 | 32 | +$622k | - | out (clean 28, ADX 41, RVol 0.8) |
| 2 | **COIN** | 139.92 | - | **-** | 34 | - | NEG -$14.4M | - | 150 | 140 | -$4.6M | +$28k bull / +$0 bear | out (clean 27, ADX 52, RVol 3.4) |
| 3 | **META** | 621.73 | FLIP CROSS down into negative gamma | **PUTS** | 30 | none: 199 puts 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (93 contracts' greeks worked out here) | NEG -$25.2M | 622.3 | 625 | 625 | -$3.9M | +$2.6M bull / +$0 bear | out (clean 28, ADX 16, RVol 0.7) |
| 4 | **SMH** | 526.00 | - | **-** | 28 | - | NEG -$569.8M | - | 530 | 530 | +$4.8M | +$32k bull / +$0 bear | out (clean 28, ADX 47, RVol 1.5) |
| 5 | **NVDA** | 206.19 | - | **-** | 28 | - | NEG -$408.6M | 212.04 | 210 | 205 | +$14.3M | +$2.2M bull / -$166k bear | out (clean 26, ADX 39, RVol 1.2) |
| 6 | **DELL** | 430.16 | - | **-** | 28 | - | NEG -$60.9M | - | 440 | 425 | +$1.2M | +$36k bull / +$0 bear | out (clean 32, ADX 48, RVol 4.2) |
| 7 | **MSTR** | 131.66 | - | **-** | 28 | - | NEG -$20.4M | 137.66 | 135 | 130 | -$5.8M | +$26k bull / -$123k bear | out (clean 27, ADX 28, RVol 1.9) |
| 8 | **AMD** | 511.84 | - | **-** | 26 | - | NEG -$111.1M | 523.84 | 517.5 | 500 | +$12.1M | +$421k bull / -$60k bear | out (clean 28, ADX 37, RVol 1.1) |
| 9 | **AMZN** | 239.82 | - | **-** | 26 | - | NEG -$154.0M | 246.45 | 250 | 240 | -$11.3M | +$319k bull / -$798k bear | out (clean 32, ADX 17, RVol 2.6) |
| 10 | **ARM** | 204.41 | - | **-** | 26 | - | NEG -$19.2M | - | 220 | 205 | +$488k | - | out (clean 26, ADX 48, RVol 3.1) |
| 11 | **GOOGL** | 282.44 | - | **-** | 25 | - | NEG -$254.9M | - | 280 | 280 | -$4.1M | +$27k bull / -$379k bear | out (clean 32, ADX 21, RVol 1.2) |
| 12 | **MU** | 890.13 | - | **-** | 25 | - | NEG -$246.2M | 927.82 | 900 | 900 | +$38.2M | +$2.7M bull / +$0 bear | out (clean 29, ADX 32, RVol 0.6) |
| 13 | **IWM** | 279.74 | - | **-** | 24 | - | NEG -$732.3M | 281.25 | 280 | 270 | +$7.4M | +$854k bull / +$0 bear | out (clean 27, ADX 37, RVol 0.6) |
| 14 | **NFLX** | 62.51 | - | **-** | 24 | - | NEG -$21.1M | 63.38 | 63 | 63 | +$902k | +$49k bull / +$0 bear | out (clean 31, ADX 24, RVol 0.5) |
| 15 | **SPY** | 758.53 | - | **-** | 23 | - | NEG -$13.9B | 771.94 | 760 | 760 | +$65.2M | +$4.5M bull / +$0 bear | out (clean 26, ADX 40, RVol 1.0) |
| 16 | **AAPL** | 347.69 | - | **-** | 22 | - | POS +$703.9M | 342.21 | 350 | 345 | -$6.1M | +$70k bull / -$42k bear | out (clean 31, ADX 27, RVol 1.2) |
| 17 | **PLTR** | 186.21 | - | **-** | 22 | - | NEG -$70.3M | 193.27 | 185 | 185 | -$2.1M | +$186k bull / +$0 bear | out (clean 25, ADX 35, RVol 1.2) |
| 18 | **ORCL** | 131.65 | - | **-** | 22 | - | POS +$49.8M | 128.79 | 130 | 130 | +$2.5M | - | out (clean 33, ADX 43, RVol 0.5) |
| 19 | **QQQ** | 694.73 | - | **-** | 21 | - | NEG -$10.0B | 726.91 | 720 | 690 | +$23.3M | +$4.0M bull / +$0 bear | out (clean 27, ADX 43, RVol 1.0) |
| 20 | **TSLA** | 401.14 | - | **-** | 20 | - | POS +$449.5M | 389.95 | 400 | 400 | -$23.0M | +$3.0M bull / -$243k bear | out (clean 29, ADX 22, RVol 1.1) |
| 21 | **MSFT** | 521.74 | - | **-** | 20 | - | POS +$472.5M | 515.47 | 525 | 525 | +$2.0M | +$29k bull / +$0 bear | out (clean 26, ADX 25, RVol 0.8) |
| 22 | **SHOP** | 156.33 | - | **-** | 19 | - | NEG -$14.1M | 163.86 | 150 | 157.5 | +$201k | - | out (clean 26, ADX 50, RVol 1.5) |
| 23 | **AVGO** | 326.99 | - | **-** | 14 | - | NEG -$127.5M | 344.01 | 330 | 330 | +$1.2M | - | out (clean 29, ADX 51, RVol 0.7) |
| 24 | **HOOD** | 84.03 | - | **-** | 12 | - | NEG -$41.6M | - | 85 | 85 | +$491k | - | out (clean 31, ADX 52, RVol 0.8) |
| 25 | **CRM** | 232.30 | - | **-** | 7 | - | NEG -$22.4M | 241.11 | 240 | 230 | -$70k | - | out (clean 28, ADX 13, RVol 0.7) |
| 26 | **UBER** | 65.31 | - | **-** | 4 | - | NEG -$30.6M | 66.4 | 70 | 65 | -$10k | - | out (clean 28, ADX 10, RVol 0.3) |
| 27 | **BABA** | 99.01 | - | **-** | 4 | - | NEG -$34.3M | 100.54 | 100 | 99 | -$17k | - | out (clean 29, ADX 15, RVol 0.3) |

## Big prints this scan (81)
- **NVDA** CALL 212.5 2026-11-06 (7DTE): 2,500 @ 1.95 = **+$488k** BUY | vol 17,890 / OI 1,349
- **NVDA** CALL 212.5 2026-11-06 (7DTE): 2,500 @ 1.95 = **+$488k** BUY | vol 17,890 / OI 1,349
- **IWM** PUT 275 2026-11-06 (7DTE): 2,496 @ 1.50 = **+$374k** SELL | vol 9,694 / OI 9,610
- **QQQ** CALL 696 2026-10-30 (0DTE): 962 @ 2.28 = **+$219k** BUY | vol 110,790 / OI 757
- **SPY** PUT 760 2026-10-30 (0DTE): 1,000 @ 2.15 = **+$215k** SELL | vol 183,399 / OI 33,031
- **IWM** PUT 275 2026-11-06 (7DTE): 1,397 @ 1.50 = **+$210k** SELL | vol 9,694 / OI 9,610
- **QQQ** CALL 696 2026-10-30 (0DTE): 942 @ 2.22 = **+$209k** BUY | vol 110,790 / OI 757
- **QQQ** CALL 696 2026-10-30 (0DTE): 962 @ 2.15 = **+$207k** BUY | vol 110,790 / OI 757
- **QQQ** PUT 695 2026-10-30 (0DTE): 959 @ 1.94 = **+$186k** SELL | vol 127,029 / OI 18,389
- **QQQ** PUT 695 2026-10-30 (0DTE): 910 @ 2.03 = **+$185k** SELL | vol 127,029 / OI 18,389
- **TSLA** PUT 402.5 2026-10-30 (0DTE): 788 @ 2.11 = **+$166k** SELL | vol 18,589 / OI 1,561
- **META** CALL 635 2026-11-06 (7DTE): 175 @ 9.00 = **+$158k** BUY | vol 1,070 / OI 1,061
- **META** CALL 620 2026-10-30 (0DTE): 266 @ 5.40 = **+$144k** BUY | vol 16,292 / OI 1,308
- **QQQ** PUT 678 2026-11-06 (7DTE): 320 @ 4.40 = **+$141k** SELL | vol 3,233 / OI 658
- **QQQ** PUT 678 2026-11-06 (7DTE): 300 @ 4.41 = **+$132k** SELL | vol 3,233 / OI 658

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 771 2026-11-03 (4DTE): 623 traded vs OI 605
- **SPY** CALL 773 2026-11-03 (4DTE): 507 traded vs OI 356
- **SPY** CALL 763 2026-11-06 (7DTE): 962 traded vs OI 903
- **QQQ** PUT 702 2026-10-30 (0DTE): 2,957 traded vs OI 2,900
- **QQQ** PUT 693 2026-11-03 (4DTE): 574 traded vs OI 0
- **QQQ** CALL 699 2026-11-03 (4DTE): 509 traded vs OI 0
- **QQQ** PUT 647 2026-10-30 (0DTE): 2,878 traded vs OI 2,614
- **QQQ** PUT 678 2026-11-06 (7DTE): 3,233 traded vs OI 658
- **IWM** PUT 278 2026-10-30 (0DTE): 26,399 traded vs OI 26,111
- **IWM** CALL 283 2026-10-30 (0DTE): 21,452 traded vs OI 21,265
- **IWM** PUT 275 2026-11-06 (7DTE): 9,694 traded vs OI 9,610
- **NVDA** CALL 205 2026-11-13 (14DTE): 1,494 traded vs OI 426
- **NVDA** CALL 217.5 2026-11-02 (3DTE): 1,568 traded vs OI 1,560
- **NVDA** CALL 187.5 2026-11-04 (5DTE): 570 traded vs OI 7
- **TSLA** PUT 370 2026-11-06 (7DTE): 1,762 traded vs OI 1,758

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
