# GEX + FLOW SCAN - Fri Oct 30, 02:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:30:08 ET, last candle SPY 14:29, QQQ 14:29 | no errors
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
| 1 | **DELL** | 415.29 | FLOW SURGE | **CALLS** | 51 | none: 66 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (55 contracts' greeks worked out here) | NEG -$47.1M | - | 440 | 420 | +$10.1M | +$58k bull / +$0 bear | out (clean 34, ADX 50, RVol 1.8) |
| 2 | **MSFT** | 519.59 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 35 | none: 164 calls 0-7DTE > 9 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -2% at the target (needs +20%) (79 contracts' greeks worked out here) | POS +$238.4M | 517.07 | 525 | 520 | +$5.3M | +$501k bull / +$0 bear | out (clean 26, ADX 14, RVol 0.3) |
| 3 | **TSLA** | 394.89 | PINNED between the walls (positive gamma) - chop | **-** | 34 | - | POS +$333.5M | 384.22 | 395 | 395 | +$10.9M | +$4.6M bull / -$544k bear | out (clean 30, ADX 27, RVol 1.2) |
| 4 | **AMD** | 495.73 | - | **-** | 30 | - | NEG -$177.6M | 521.25 | 500 | 500 | +$38.1M | +$396k bull / +$0 bear | out (clean 29, ADX 45, RVol 1.8) |
| 5 | **SMCI** | 31.48 | - | **-** | 29 | - | NEG -$4.7M | 32.76 | 32 | 32 | +$1.0M | +$28k bull / +$0 bear | out (clean 30, ADX 53, RVol 0.9) |
| 6 | **SPY** | 751.55 | - | **-** | 28 | - | NEG -$16.6B | 771.87 | 750 | 750 | +$294.5M | +$7.1M bull / +$0 bear | out (clean 28, ADX 54, RVol 1.5) |
| 7 | **NVDA** | 201.61 | - | **-** | 28 | - | NEG -$457.8M | 211.66 | 210 | 200 | +$41.7M | +$2.8M bull / +$0 bear | out (clean 28, ADX 56, RVol 1.3) |
| 8 | **QQQ** | 685.24 | - | **-** | 27 | - | NEG -$9.2B | - | 720 | 690 | +$197.5M | +$7.8M bull / +$0 bear | out (clean 29, ADX 54, RVol 2.3) |
| 9 | **SMH** | 513.51 | - | **-** | 27 | - | NEG -$760.9M | - | 532.5 | 505 | +$9.6M | +$5.3M bull / +$0 bear | out (clean 30, ADX 54, RVol 1.2) |
| 10 | **AVGO** | 320.50 | - | **-** | 26 | - | NEG -$157.0M | - | 340 | 320 | +$3.3M | +$85k bull / +$0 bear | out (clean 30, ADX 48, RVol 1.4) |
| 11 | **MU** | 866.24 | - | **-** | 26 | - | NEG -$321.9M | - | 880 | 850 | +$78.5M | +$1.2M bull / +$0 bear | out (clean 31, ADX 44, RVol 0.9) |
| 12 | **ORCL** | 129.94 | PINNED between the walls (positive gamma) - chop | **-** | 26 | - | POS +$16.7M | 129.01 | 130 | 130 | +$2.9M | - | out (clean 34, ADX 27, RVol 0.5) |
| 13 | **AAPL** | 343.15 | - | **-** | 25 | - | POS +$128.6M | 341.45 | 345 | 345 | +$13.7M | +$2.0M bull / -$168k bear | out (clean 32, ADX 38, RVol 2.0) |
| 14 | **HOOD** | 82.60 | - | **-** | 24 | - | NEG -$24.3M | - | 85 | 83 | +$2.2M | +$151k bull / +$0 bear | out (clean 32, ADX 50, RVol 1.0) |
| 15 | **SHOP** | 154.88 | - | **-** | 24 | - | NEG -$13.0M | - | 150 | 157.5 | +$753k | - | out (clean 28, ADX 48, RVol 1.8) |
| 16 | **GOOGL** | 278.12 | - | **-** | 21 | - | NEG -$218.0M | - | 280 | 280 | +$2.9M | +$157k bull / +$0 bear | out (clean 33, ADX 40, RVol 0.6) |
| 17 | **META** | 614.06 | - | **-** | 20 | - | NEG -$165.5M | 619.55 | 615 | 610 | +$6.3M | +$221k bull / -$191k bear | out (clean 29, ADX 38, RVol 0.4) |
| 18 | **PLTR** | 184.44 | - | **-** | 19 | - | NEG -$77.8M | 191.78 | 185 | 185 | +$3.7M | +$330k bull / -$166k bear | out (clean 26, ADX 30, RVol 0.7) |
| 19 | **MSTR** | 129.14 | - | **-** | 18 | - | NEG -$29.3M | - | 135 | 130 | -$2.7M | +$312k bull / +$0 bear | out (clean 29, ADX 28, RVol 0.6) |
| 20 | **ARM** | 199.63 | - | **-** | 18 | - | NEG -$17.3M | - | 200 | 200 | +$1.0M | - | out (clean 26, ADX 36, RVol 1.4) |
| 21 | **BABA** | 97.70 | - | **-** | 18 | - | NEG -$43.1M | 98.92 | 100 | 98 | +$655k | - | out (clean 30, ADX 33, RVol 0.5) |
| 22 | **AMZN** | 237.78 | - | **-** | 16 | - | NEG -$193.6M | 247.02 | 250 | 240 | -$3.6M | +$159k bull / +$0 bear | out (clean 30, ADX 13, RVol 1.0) |
| 23 | **IWM** | 277.24 | - | **-** | 15 | - | NEG -$1.6B | 281.06 | 278 | 278 | +$13.0M | - | out (clean 29, ADX 47, RVol 0.8) |
| 24 | **COIN** | 138.22 | - | **-** | 15 | - | NEG -$14.2M | - | 140 | 140 | -$1.6M | - | out (clean 28, ADX 47, RVol 3.2) |
| 25 | **NFLX** | 62.01 | - | **-** | 13 | - | NEG -$29.3M | 62.5 | 62 | 62 | +$1.4M | - | out (clean 30, ADX 24, RVol 0.7) |
| 26 | **UBER** | 65.00 | - | **-** | 13 | - | NEG -$41.5M | 66.17 | 65 | 65 | +$314k | - | out (clean 28, ADX 21, RVol 0.5) |
| 27 | **CRM** | 229.02 | - | **-** | 12 | - | NEG -$26.0M | 234.23 | 230 | 230 | +$294k | - | out (clean 27, ADX 30, RVol 1.0) |

## Big prints this scan (92)
- **SMH** PUT 500 2026-11-06 (7DTE): 5,400 @ 8.60 = **+$4.6M** SELL | vol 12,117 / OI 35,115
- **SPY** CALL 766 2026-11-06 (7DTE): 4,000 @ 2.66 = **+$1.1M** BUY | vol 5,908 / OI 698
- **SPY** CALL 767 2026-11-06 (7DTE): 4,000 @ 2.35 = **+$940k** BUY | vol 5,069 / OI 4,747
- **QQQ** PUT 692 2026-10-30 (0DTE): 978 @ 5.55 = **+$543k** SELL | vol 190,083 / OI 2,435
- **QQQ** PUT 700 2026-10-30 (0DTE): 259 @ 12.93 = **+$335k** SELL | vol 44,097 / OI 42,068
- **SMH** CALL 520 2026-11-06 (7DTE): 248 @ 12.67 = **+$314k** BUY | vol 1,075 / OI 40
- **SMH** PUT 510 2026-11-06 (7DTE): 248 @ 12.02 = **+$298k** SELL | vol 1,017 / OI 341
- **SPY** PUT 767 2026-11-04 (5DTE): 200 @ 14.90 = **+$298k** SELL | vol 22,326 / OI 29,783
- **SPY** PUT 767 2026-11-04 (5DTE): 199 @ 14.70 = **+$293k** SELL | vol 22,326 / OI 29,783
- **SPY** CALL 725 2026-11-06 (7DTE): 85 @ 30.95 = **+$263k** BUY | vol 108 / OI 37
- **AAPL** PUT 350 2026-10-30 (0DTE): 300 @ 6.85 = **+$206k** MID | vol 13,268 / OI 2,499
- **PLTR** CALL 190 2026-11-06 (7DTE): 200 @ 10.05 = **+$201k** BUY | vol 7,687 / OI 976
- **QQQ** CALL 686 2026-10-30 (0DTE): 753 @ 2.31 = **+$174k** BUY | vol 14,360 / OI 82
- **AAPL** PUT 350 2026-10-30 (0DTE): 250 @ 6.60 = **+$165k** SELL | vol 13,268 / OI 2,499
- **SPY** PUT 759 2026-10-30 (0DTE): 266 @ 6.11 = **+$163k** SELL | vol 238,932 / OI 4,254

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 705 2026-11-02 (3DTE): 3,297 traded vs OI 3,236
- **SPY** CALL 752 2026-11-02 (3DTE): 765 traded vs OI 80
- **SPY** PUT 738 2026-11-06 (7DTE): 1,001 traded vs OI 984
- **SPY** CALL 770 2026-11-12 (13DTE): 584 traded vs OI 0
- **SPY** PUT 740 2026-11-12 (13DTE): 587 traded vs OI 0
- **SPY** PUT 735 2026-11-11 (12DTE): 502 traded vs OI 77
- **QQQ** CALL 713 2026-11-06 (7DTE): 1,534 traded vs OI 503
- **QQQ** PUT 620 2026-11-03 (4DTE): 512 traded vs OI 0
- **QQQ** PUT 630 2026-11-09 (10DTE): 1,188 traded vs OI 1,081
- **SMH** PUT 465 2026-10-30 (0DTE): 502 traded vs OI 0
- **NVDA** PUT 190 2026-10-30 (0DTE): 9,710 traded vs OI 7,418
- **TSLA** CALL 387.5 2026-11-02 (3DTE): 512 traded vs OI 159
- **GOOGL** PUT 272.5 2026-11-06 (7DTE): 500 traded vs OI 0
- **NFLX** PUT 57 2026-11-13 (14DTE): 606 traded vs OI 293
- **AVGO** CALL 325 2026-11-02 (3DTE): 503 traded vs OI 99

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
