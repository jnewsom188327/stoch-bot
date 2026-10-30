# GEX + FLOW SCAN - Fri Oct 30, 02:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:20:08 ET, last candle SPY 14:19, QQQ 14:19 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
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
| 1 | **ORCL** | 130.09 | PINNED between the walls (positive gamma) - chop | **-** | 36 | - | POS +$30.8M | 128.87 | 130 | 130 | +$2.7M | +$0 bull / -$62k bear | out (clean 34, ADX 27, RVol 0.7) |
| 2 | **DELL** | 415.78 | - | **-** | 35 | - | NEG -$46.5M | - | 440 | 425 | +$10.0M | +$0 bull / -$87k bear | out (clean 34, ADX 52, RVol 1.9) |
| 3 | **TSLA** | 394.94 | PINNED between the walls (positive gamma) - chop | **-** | 34 | - | POS +$359.5M | 381.84 | 395 | 395 | +$15.3M | +$3.5M bull / -$27k bear | out (clean 29, ADX 25, RVol 1.1) |
| 4 | **MSFT** | 520.89 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | 10/30 522.5C @ 0.76 (delta 0.32) = est +223% at 525 | POS +$368.5M | 517.51 | 525 | 520 | +$4.7M | +$336k bull / +$0 bear | out (clean 26, ADX 13, RVol 0.3) |
| 5 | **SMCI** | 31.48 | - | **-** | 30 | - | NEG -$4.5M | 32.83 | 32 | 32 | +$916k | +$28k bull / +$0 bear | out (clean 30, ADX 52, RVol 1.2) |
| 6 | **AMD** | 497.28 | - | **-** | 29 | - | NEG -$172.0M | 518.1 | 500 | 500 | +$36.8M | +$789k bull / -$472k bear | out (clean 29, ADX 46, RVol 1.5) |
| 7 | **NVDA** | 202.13 | - | **-** | 28 | - | NEG -$458.6M | 212.51 | 210 | 200 | +$38.0M | +$3.0M bull / -$302k bear | out (clean 28, ADX 54, RVol 1.3) |
| 8 | **SPY** | 752.44 | - | **-** | 27 | - | NEG -$16.7B | 772.15 | 750 | 750 | +$266.7M | +$9.6M bull / +$0 bear | out (clean 27, ADX 51, RVol 1.4) |
| 9 | **QQQ** | 685.76 | - | **-** | 26 | - | NEG -$9.4B | - | 720 | 690 | +$179.0M | +$8.6M bull / -$102k bear | out (clean 29, ADX 53, RVol 2.2) |
| 10 | **SMH** | 514.34 | - | **-** | 26 | - | NEG -$735.5M | - | 532.5 | 505 | +$8.2M | +$545k bull / +$0 bear | out (clean 30, ADX 54, RVol 0.9) |
| 11 | **MU** | 865.99 | - | **-** | 26 | - | NEG -$339.0M | - | 880 | 850 | +$75.5M | +$1.7M bull / -$1.2M bear | out (clean 31, ADX 43, RVol 1.0) |
| 12 | **AAPL** | 343.49 | - | **-** | 25 | - | POS +$193.2M | 341.36 | 345 | 345 | +$14.4M | +$1.9M bull / +$0 bear | out (clean 32, ADX 36, RVol 2.0) |
| 13 | **AVGO** | 321.23 | - | **-** | 25 | - | NEG -$165.6M | - | 340 | 320 | +$2.9M | +$140k bull / +$0 bear | out (clean 30, ADX 46, RVol 1.4) |
| 14 | **HOOD** | 82.61 | - | **-** | 24 | - | NEG -$34.2M | - | 85 | 85 | +$2.2M | +$151k bull / +$0 bear | out (clean 32, ADX 50, RVol 0.9) |
| 15 | **SHOP** | 154.56 | - | **-** | 23 | - | NEG -$12.6M | - | 150 | 157.5 | +$756k | - | out (clean 27, ADX 50, RVol 1.4) |
| 16 | **GOOGL** | 277.96 | - | **-** | 21 | - | NEG -$237.9M | - | 280 | 280 | +$2.8M | +$1.1M bull / +$0 bear | out (clean 33, ADX 40, RVol 0.6) |
| 17 | **META** | 614.94 | - | **-** | 19 | - | NEG -$133.6M | 619.58 | 615 | 610 | +$5.6M | +$693k bull / -$154k bear | out (clean 29, ADX 35, RVol 0.4) |
| 18 | **PLTR** | 184.52 | - | **-** | 19 | - | NEG -$77.7M | 192.4 | 185 | 185 | +$3.4M | +$0 bull / -$686k bear | out (clean 26, ADX 30, RVol 0.9) |
| 19 | **ARM** | 200.28 | - | **-** | 17 | - | NEG -$18.4M | - | 220 | 200 | +$994k | - | out (clean 26, ADX 34, RVol 1.5) |
| 20 | **BABA** | 97.81 | - | **-** | 17 | - | NEG -$42.8M | 98.9 | 100 | 98 | +$577k | - | out (clean 30, ADX 29, RVol 0.6) |
| 21 | **COIN** | 137.79 | - | **-** | 16 | - | NEG -$13.7M | - | 140 | 140 | -$1.6M | - | out (clean 28, ADX 47, RVol 3.0) |
| 22 | **AMZN** | 238.21 | - | **-** | 15 | - | NEG -$182.6M | 245.19 | 250 | 240 | -$4.2M | +$257k bull / -$60k bear | out (clean 30, ADX 11, RVol 1.0) |
| 23 | **IWM** | 277.56 | - | **-** | 14 | - | NEG -$1.5B | 281.17 | 278 | 278 | +$12.1M | - | out (clean 29, ADX 45, RVol 0.6) |
| 24 | **NFLX** | 61.96 | - | **-** | 14 | - | NEG -$35.1M | 62.61 | 62 | 62 | +$1.5M | - | out (clean 30, ADX 25, RVol 0.9) |
| 25 | **UBER** | 64.91 | - | **-** | 14 | - | NEG -$39.4M | 66.07 | 65 | 65 | +$331k | - | out (clean 28, ADX 23, RVol 0.5) |
| 26 | **CRM** | 229.27 | - | **-** | 12 | - | NEG -$24.6M | 238.17 | 230 | 230 | +$285k | - | out (clean 28, ADX 29, RVol 0.9) |
| 27 | **MSTR** | 129.09 | - | **-** | 9 | - | NEG -$30.0M | 136.71 | 135 | 130 | -$4.0M | - | out (clean 29, ADX 29, RVol 0.7) |

## Big prints this scan (148)
- **SPY** CALL 754 2026-11-06 (7DTE): 474 @ 8.22 = **+$390k** BUY | vol 4,957 / OI 33
- **SPY** CALL 754 2026-11-06 (7DTE): 464 @ 8.35 = **+$387k** BUY | vol 4,957 / OI 33
- **TSLA** CALL 382.5 2026-10-30 (0DTE): 293 @ 13.00 = **+$381k** BUY | vol 2,815 / OI 5,226
- **SPY** CALL 754 2026-11-06 (7DTE): 422 @ 8.27 = **+$349k** BUY | vol 4,957 / OI 33
- **SPY** CALL 754 2026-11-06 (7DTE): 405 @ 8.26 = **+$335k** BUY | vol 4,957 / OI 33
- **SPY** PUT 767 2026-11-04 (5DTE): 205 @ 14.41 = **+$295k** SELL | vol 21,439 / OI 29,783
- **QQQ** PUT 692 2026-10-30 (0DTE): 500 @ 5.50 = **+$275k** SELL | vol 188,837 / OI 2,435
- **QQQ** PUT 692 2026-10-30 (0DTE): 500 @ 5.50 = **+$275k** SELL | vol 188,837 / OI 2,435
- **QQQ** PUT 705 2026-10-30 (0DTE): 145 @ 18.18 = **+$264k** SELL | vol 9,214 / OI 18,002
- **TSLA** CALL 382.5 2026-10-30 (0DTE): 202 @ 12.90 = **+$261k** MID | vol 2,815 / OI 5,226
- **SPY** PUT 767 2026-11-04 (5DTE): 177 @ 14.38 = **+$255k** SELL | vol 21,439 / OI 29,783
- **TSLA** CALL 382.5 2026-10-30 (0DTE): 156 @ 13.00 = **+$203k** BUY | vol 2,815 / OI 5,226
- **SPY** CALL 754 2026-11-06 (7DTE): 243 @ 8.28 = **+$201k** BUY | vol 4,957 / OI 33
- **TSLA** CALL 382.5 2026-10-30 (0DTE): 154 @ 12.90 = **+$199k** MID | vol 2,815 / OI 5,226
- **SPY** CALL 754 2026-11-06 (7DTE): 231 @ 8.28 = **+$191k** BUY | vol 4,957 / OI 33

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 753 2026-11-03 (4DTE): 672 traded vs OI 5
- **SPY** PUT 690 2026-11-02 (3DTE): 758 traded vs OI 716
- **SPY** PUT 700 2026-11-04 (5DTE): 558 traded vs OI 527
- **SPY** PUT 730 2026-11-12 (13DTE): 516 traded vs OI 0
- **SPY** PUT 746 2026-11-06 (7DTE): 1,101 traded vs OI 1,077
- **SPY** PUT 755 2026-11-10 (11DTE): 1,571 traded vs OI 1,513
- **QQQ** CALL 682 2026-10-30 (0DTE): 524 traded vs OI 83
- **QQQ** CALL 685 2026-11-06 (7DTE): 686 traded vs OI 153
- **QQQ** CALL 704 2026-11-04 (5DTE): 500 traded vs OI 50
- **QQQ** PUT 670 2026-11-13 (14DTE): 4,498 traded vs OI 4,224
- **QQQ** PUT 712 2026-11-20 (21DTE): 5,134 traded vs OI 3,871
- **IWM** PUT 270 2026-11-11 (12DTE): 803 traded vs OI 18
- **IWM** CALL 281 2026-11-03 (4DTE): 711 traded vs OI 690
- **IWM** PUT 250 2026-11-06 (7DTE): 655 traded vs OI 0
- **IWM** PUT 250 2026-11-20 (21DTE): 915 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
