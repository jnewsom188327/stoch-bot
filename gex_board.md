# GEX + FLOW SCAN - Fri Oct 30, 01:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:40:08 ET, last candle SPY 13:39, QQQ 13:39 | no errors
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
| 1 | **DELL** | 415.65 | FLOW SURGE | **CALLS** | 54 | none: 66 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (56 contracts' greeks worked out here) | NEG -$44.4M | - | 440 | 420 | +$5.3M | +$43k bull / +$0 bear | SHORT (clean 34, ADX 62, RVol 1.8) |
| 2 | **MSFT** | 520.32 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 37 | 10/30 522.5C @ 0.70 (delta 0.28) = est +43% at 522.61 | POS +$354.7M | 516.46 | 525 | 520 | +$4.4M | +$36k bull / +$0 bear | out (clean 26, ADX 17, RVol 0.5) |
| 3 | **AMD** | 499.36 | - | **-** | 29 | - | NEG -$177.8M | 520.04 | 540 | 500 | +$33.9M | +$736k bull / -$1.5M bear | out (clean 30, ADX 54, RVol 1.3) |
| 4 | **NVDA** | 203.18 | - | **-** | 28 | - | NEG -$381.8M | 209.24 | 210 | 205 | +$33.3M | +$1.1M bull / -$2.7M bear | out (clean 28, ADX 49, RVol 0.8) |
| 5 | **ARM** | 202.72 | - | **-** | 28 | - | NEG -$21.0M | - | 220 | 205 | +$849k | +$0 bull / -$196k bear | out (clean 25, ADX 33, RVol 2.1) |
| 6 | **SPY** | 755.15 | - | **-** | 26 | - | NEG -$14.4B | 767.56 | 800 | 750 | +$169.3M | +$905k bull / -$14.9M bear | out (clean 27, ADX 44, RVol 1.5) |
| 7 | **SMH** | 517.75 | - | **-** | 26 | - | NEG -$616.4M | - | 532.5 | 505 | +$7.5M | +$312k bull / -$586k bear | out (clean 30, ADX 54, RVol 1.0) |
| 8 | **SHOP** | 154.75 | - | **-** | 26 | - | NEG -$12.6M | - | 150 | 157.5 | +$762k | - | out (clean 27, ADX 46, RVol 3.3) |
| 9 | **QQQ** | 688.70 | - | **-** | 25 | - | NEG -$9.9B | 728.7 | 720 | 690 | +$101.5M | +$3.3M bull / -$1.2M bear | out (clean 28, ADX 48, RVol 2.2) |
| 10 | **IWM** | 278.21 | - | **-** | 25 | - | NEG -$1.3B | 281.07 | 278 | 278 | +$11.0M | +$113k bull / +$0 bear | out (clean 28, ADX 45, RVol 1.0) |
| 11 | **MU** | 873.43 | - | **-** | 25 | - | NEG -$293.7M | 919.03 | 880 | 880 | +$65.8M | +$5.5M bull / -$27k bear | out (clean 30, ADX 39, RVol 1.1) |
| 12 | **HOOD** | 83.05 | - | **-** | 22 | - | NEG -$27.1M | - | 85 | 83 | +$1.1M | +$84k bull / -$258k bear | out (clean 31, ADX 50, RVol 0.9) |
| 13 | **COIN** | 138.58 | - | **-** | 19 | - | NEG -$15.2M | - | 140 | 140 | -$3.3M | - | out (clean 27, ADX 48, RVol 3.4) |
| 14 | **MSTR** | 129.53 | - | **-** | 19 | - | NEG -$30.2M | - | 135 | 130 | -$4.6M | +$253k bull / +$0 bear | out (clean 28, ADX 24, RVol 1.0) |
| 15 | **GOOGL** | 279.11 | - | **-** | 18 | - | NEG -$242.7M | - | 280 | 280 | +$236k | +$63k bull / -$75k bear | out (clean 32, ADX 36, RVol 0.6) |
| 16 | **SMCI** | 31.68 | - | **-** | 18 | - | NEG -$4.9M | 32.79 | 32 | 32 | +$775k | - | out (clean 30, ADX 53, RVol 0.7) |
| 17 | **AAPL** | 346.17 | - | **-** | 17 | - | POS +$483.5M | 342.09 | 350 | 345 | +$3.6M | +$3.2M bull / +$0 bear | out (clean 30, ADX 18, RVol 1.3) |
| 18 | **AMZN** | 239.12 | - | **-** | 17 | - | NEG -$174.5M | 244.32 | 250 | 240 | -$4.6M | +$757k bull / -$383k bear | out (clean 31, ADX 13, RVol 1.4) |
| 19 | **META** | 618.35 | - | **-** | 16 | - | NEG -$97.4M | 621.72 | 625 | 625 | +$1.1M | +$345k bull / -$84k bear | out (clean 28, ADX 22, RVol 0.6) |
| 20 | **TSLA** | 398.85 | - | **-** | 15 | - | POS +$444.4M | 387.42 | 400 | 400 | -$13.1M | +$243k bull / -$2.6M bear | out (clean 29, ADX 12, RVol 0.8) |
| 21 | **ORCL** | 130.79 | - | **-** | 14 | - | POS +$16.2M | 129.77 | 130 | 130 | +$2.7M | - | out (clean 34, ADX 31, RVol 0.5) |
| 22 | **UBER** | 64.98 | - | **-** | 14 | - | NEG -$39.5M | 66.12 | 65 | 65 | +$329k | - | out (clean 28, ADX 22, RVol 0.5) |
| 23 | **BABA** | 98.29 | - | **-** | 14 | - | NEG -$44.5M | 99.59 | 100 | 98 | +$523k | - | out (clean 29, ADX 15, RVol 0.6) |
| 24 | **NFLX** | 62.10 | - | **-** | 13 | - | NEG -$27.0M | 62.82 | 62 | 62 | +$1.3M | - | out (clean 30, ADX 20, RVol 0.9) |
| 25 | **AVGO** | 323.40 | - | **-** | 13 | - | NEG -$147.5M | 340.5 | 340 | 320 | +$1.7M | - | out (clean 30, ADX 48, RVol 1.1) |
| 26 | **CRM** | 229.31 | - | **-** | 11 | - | NEG -$27.1M | 237.4 | 230 | 230 | +$293k | - | out (clean 28, ADX 28, RVol 0.5) |
| 27 | **PLTR** | 185.00 | - | **-** | 8 | - | NEG -$59.9M | 188.77 | 185 | 185 | +$1.3M | - | out (clean 26, ADX 30, RVol 0.7) |

## Big prints this scan (79)
- **AMD** CALL 505 2026-11-06 (7DTE): 200 @ 23.20 = **+$464k** SELL | vol 550 / OI 77
- **AAPL** CALL 357.5 2026-11-06 (7DTE): 1,010 @ 3.93 = **+$397k** BUY | vol 4,079 / OI 467
- **AAPL** CALL 357.5 2026-11-06 (7DTE): 1,010 @ 3.93 = **+$397k** BUY | vol 4,079 / OI 467
- **AAPL** CALL 355 2026-11-04 (5DTE): 852 @ 4.15 = **+$354k** BUY | vol 10,158 / OI 12,247
- **AAPL** CALL 357.5 2026-11-06 (7DTE): 700 @ 3.93 = **+$275k** BUY | vol 4,079 / OI 467
- **AAPL** CALL 357.5 2026-11-06 (7DTE): 700 @ 3.93 = **+$275k** BUY | vol 4,079 / OI 467
- **AAPL** CALL 362.5 2026-11-06 (7DTE): 1,010 @ 2.49 = **+$251k** BUY | vol 6,270 / OI 3,975
- **AAPL** CALL 362.5 2026-11-06 (7DTE): 1,010 @ 2.49 = **+$251k** BUY | vol 6,270 / OI 3,975
- **AAPL** CALL 355 2026-11-04 (5DTE): 563 @ 4.15 = **+$234k** BUY | vol 10,158 / OI 12,247
- **QQQ** CALL 691 2026-11-04 (5DTE): 227 @ 8.46 = **+$192k** BUY | vol 662 / OI 0
- **AAPL** CALL 362.5 2026-11-06 (7DTE): 700 @ 2.48 = **+$174k** BUY | vol 6,270 / OI 3,975
- **AAPL** CALL 362.5 2026-11-06 (7DTE): 700 @ 2.48 = **+$174k** BUY | vol 6,270 / OI 3,975
- **SPY** PUT 778 2026-11-06 (7DTE): 75 @ 22.76 = **+$171k** MID | vol 357 / OI 1,073
- **MU** PUT 895 2026-10-30 (0DTE): 82 @ 19.92 = **+$163k** SELL | vol 9,946 / OI 1,347
- **ARM** PUT 210 2026-10-30 (0DTE): 212 @ 7.66 = **+$162k** BUY | vol 805 / OI 558

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 732 2026-11-02 (3DTE): 680 traded vs OI 676
- **SPY** CALL 786 2026-11-03 (4DTE): 704 traded vs OI 172
- **SPY** CALL 786 2026-11-02 (3DTE): 1,705 traded vs OI 596
- **SPY** PUT 725 2026-11-10 (11DTE): 552 traded vs OI 135
- **QQQ** PUT 655 2026-11-03 (4DTE): 624 traded vs OI 250
- **QQQ** PUT 625 2026-11-04 (5DTE): 518 traded vs OI 103
- **QQQ** CALL 694 2026-11-04 (5DTE): 523 traded vs OI 0
- **QQQ** CALL 691 2026-11-04 (5DTE): 662 traded vs OI 0
- **QQQ** PUT 688 2026-11-04 (5DTE): 534 traded vs OI 0
- **QQQ** CALL 711 2026-11-03 (4DTE): 508 traded vs OI 46
- **QQQ** CALL 700 2026-11-11 (12DTE): 506 traded vs OI 5
- **QQQ** CALL 670 2026-11-20 (21DTE): 516 traded vs OI 301
- **QQQ** PUT 660 2026-11-10 (11DTE): 506 traded vs OI 24
- **QQQ** CALL 690 2026-11-13 (14DTE): 530 traded vs OI 196
- **IWM** CALL 284 2026-11-03 (4DTE): 529 traded vs OI 518

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
