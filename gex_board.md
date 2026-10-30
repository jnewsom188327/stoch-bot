# GEX + FLOW SCAN - Fri Oct 30, 02:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:40:08 ET, last candle SPY 14:39, QQQ 14:39 | no errors
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
| 1 | **MSFT** | 519.91 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 37 | none: 164 calls 0-7DTE > 8 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -28% at the target (needs +20%) (80 contracts' greeks worked out here) | POS +$250.1M | 517.24 | 525 | 520 | +$6.7M | +$1.0M bull / +$0 bear | out (clean 26, ADX 16, RVol 0.5) |
| 2 | **ORCL** | 130.22 | PINNED between the walls (positive gamma) - chop | **-** | 35 | - | POS +$12.9M | 129.52 | 130 | 130 | +$2.7M | +$0 bull / -$30k bear | out (clean 34, ADX 28, RVol 0.5) |
| 3 | **TSLA** | 395.23 | PINNED between the walls (positive gamma) - chop | **-** | 34 | - | POS +$339.3M | 383.74 | 395 | 395 | +$10.2M | +$304k bull / -$1.2M bear | out (clean 30, ADX 30, RVol 1.1) |
| 4 | **DELL** | 415.61 | - | **-** | 33 | - | NEG -$44.5M | - | 440 | 420 | +$10.1M | +$0 bull / -$29k bear | out (clean 34, ADX 48, RVol 1.3) |
| 5 | **SPY** | 751.82 | - | **-** | 29 | - | NEG -$15.4B | 767.19 | 750 | 750 | +$318.8M | +$8.4M bull / -$2.9M bear | out (clean 28, ADX 57, RVol 2.1) |
| 6 | **AMD** | 494.34 | - | **-** | 29 | - | NEG -$156.7M | 509.7 | 540 | 500 | +$39.3M | +$1.5M bull / +$0 bear | out (clean 30, ADX 46, RVol 1.8) |
| 7 | **SMH** | 513.17 | - | **-** | 28 | - | NEG -$723.3M | - | 532.5 | 505 | +$10.0M | +$5.7M bull / -$95k bear | out (clean 31, ADX 56, RVol 1.6) |
| 8 | **NVDA** | 201.61 | - | **-** | 28 | - | NEG -$374.7M | 209.3 | 210 | 200 | +$42.9M | +$2.4M bull / -$144k bear | out (clean 29, ADX 58, RVol 1.4) |
| 9 | **QQQ** | 685.04 | - | **-** | 27 | - | NEG -$8.2B | - | 720 | 690 | +$206.9M | +$2.6M bull / -$1.5M bear | out (clean 30, ADX 57, RVol 2.2) |
| 10 | **MU** | 864.31 | - | **-** | 26 | - | NEG -$263.3M | 884.33 | 880 | 850 | +$81.9M | +$2.4M bull / -$653k bear | out (clean 31, ADX 46, RVol 0.9) |
| 11 | **AAPL** | 343.61 | - | **-** | 25 | - | POS +$148.1M | 342.02 | 345 | 345 | +$13.6M | +$877k bull / -$433k bear | out (clean 32, ADX 40, RVol 1.8) |
| 12 | **HOOD** | 82.67 | - | **-** | 25 | - | NEG -$36.3M | - | 85 | 83 | +$2.2M | +$0 bull / -$46k bear | out (clean 32, ADX 51, RVol 1.2) |
| 13 | **SHOP** | 155.18 | - | **-** | 25 | - | NEG -$16.8M | - | 155 | 157.5 | +$724k | - | out (clean 28, ADX 46, RVol 3.3) |
| 14 | **NFLX** | 62.02 | - | **-** | 23 | - | NEG -$30.8M | 62.98 | 62 | 62 | +$1.4M | +$0 bull / -$45k bear | out (clean 30, ADX 24, RVol 0.7) |
| 15 | **META** | 613.52 | - | **-** | 21 | - | NEG -$194.5M | 620.39 | 650 | 610 | +$7.4M | +$280k bull / +$0 bear | out (clean 29, ADX 42, RVol 0.5) |
| 16 | **GOOGL** | 277.89 | - | **-** | 21 | - | NEG -$223.6M | - | 280 | 280 | +$3.6M | +$173k bull / +$0 bear | out (clean 33, ADX 42, RVol 0.6) |
| 17 | **PLTR** | 184.90 | - | **-** | 19 | - | NEG -$79.0M | 192.82 | 185 | 185 | +$3.9M | +$289k bull / -$26k bear | out (clean 26, ADX 29, RVol 0.7) |
| 18 | **SMCI** | 31.51 | - | **-** | 19 | - | NEG -$4.5M | 32.7 | 32 | 32 | +$989k | - | out (clean 30, ADX 54, RVol 1.0) |
| 19 | **MSTR** | 128.72 | - | **-** | 18 | - | NEG -$29.7M | 133.97 | 135 | 130 | -$1.8M | +$1.7M bull / +$0 bear | out (clean 29, ADX 29, RVol 0.7) |
| 20 | **ARM** | 199.71 | - | **-** | 18 | - | NEG -$17.2M | - | 200 | 200 | +$1.1M | - | out (clean 26, ADX 38, RVol 1.4) |
| 21 | **BABA** | 97.73 | - | **-** | 18 | - | NEG -$52.5M | 99.85 | 100 | 98 | +$660k | - | out (clean 30, ADX 37, RVol 0.4) |
| 22 | **AMZN** | 238.12 | - | **-** | 16 | - | NEG -$179.6M | 243.5 | 250 | 240 | -$3.7M | +$298k bull / -$44k bear | out (clean 30, ADX 14, RVol 1.2) |
| 23 | **IWM** | 277.23 | - | **-** | 15 | - | NEG -$1.7B | 279.99 | 278 | 278 | +$14.3M | - | out (clean 29, ADX 50, RVol 0.9) |
| 24 | **AVGO** | 320.53 | - | **-** | 15 | - | NEG -$172.1M | - | 340 | 320 | +$3.7M | - | out (clean 30, ADX 51, RVol 1.1) |
| 25 | **COIN** | 138.29 | - | **-** | 15 | - | NEG -$15.0M | - | 140 | 140 | -$1.6M | - | out (clean 28, ADX 48, RVol 3.1) |
| 26 | **UBER** | 65.05 | - | **-** | 12 | - | NEG -$39.2M | 66.08 | 65 | 65 | +$314k | - | out (clean 27, ADX 18, RVol 0.5) |
| 27 | **CRM** | 229.43 | - | **-** | 12 | - | NEG -$28.8M | 238.74 | 230 | 230 | +$309k | - | out (clean 27, ADX 30, RVol 1.0) |

## Big prints this scan (147)
- **MSTR** CALL 135 2026-11-06 (7DTE): 1,820 @ 3.93 = **+$715k** BUY | vol 9,265 / OI 219
- **MSTR** CALL 135 2026-11-06 (7DTE): 1,820 @ 3.93 = **+$715k** BUY | vol 9,265 / OI 219
- **SPY** CALL 750 2026-11-03 (4DTE): 1,051 @ 6.72 = **+$706k** SELL | vol 3,472 / OI 23
- **AMD** CALL 515 2026-11-06 (7DTE): 370 @ 18.05 = **+$668k** BUY | vol 1,991 / OI 106
- **TSLA** PUT 400 2026-10-30 (0DTE): 1,150 @ 5.10 = **+$586k** BUY | vol 137,141 / OI 4,157
- **SPY** PUT 740 2026-11-03 (4DTE): 3,000 @ 1.87 = **+$561k** SELL | vol 7,791 / OI 730
- **QQQ** PUT 692 2026-10-30 (0DTE): 500 @ 7.00 = **+$350k** BUY | vol 191,473 / OI 2,435
- **SPY** CALL 750 2026-11-03 (4DTE): 500 @ 6.72 = **+$336k** SELL | vol 3,472 / OI 23
- **SPY** CALL 750 2026-11-03 (4DTE): 500 @ 6.72 = **+$336k** SELL | vol 3,472 / OI 23
- **SPY** CALL 750 2026-11-03 (4DTE): 500 @ 6.72 = **+$336k** SELL | vol 3,472 / OI 23
- **QQQ** PUT 708 2026-10-30 (0DTE): 142 @ 23.14 = **+$329k** BUY | vol 2,960 / OI 2,673
- **SPY** PUT 767 2026-11-04 (5DTE): 200 @ 16.05 = **+$321k** BUY | vol 23,985 / OI 29,783
- **SPY** PUT 767 2026-11-04 (5DTE): 200 @ 16.04 = **+$321k** BUY | vol 23,985 / OI 29,783
- **QQQ** PUT 703 2026-11-06 (7DTE): 142 @ 22.41 = **+$318k** MID | vol 482 / OI 347
- **MU** PUT 900 2026-10-30 (0DTE): 90 @ 33.24 = **+$299k** SELL | vol 11,407 / OI 3,632

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 710 2026-11-04 (5DTE): 545 traded vs OI 217
- **SPY** CALL 750 2026-11-05 (6DTE): 516 traded vs OI 14
- **SPY** PUT 744 2026-11-04 (5DTE): 872 traded vs OI 426
- **SPY** CALL 748 2026-10-30 (0DTE): 811 traded vs OI 433
- **SPY** CALL 746 2026-10-30 (0DTE): 1,154 traded vs OI 297
- **SPY** PUT 741 2026-10-30 (0DTE): 2,946 traded vs OI 2,822
- **SPY** CALL 753 2026-11-04 (5DTE): 639 traded vs OI 9
- **SPY** CALL 751 2026-11-02 (3DTE): 879 traded vs OI 12
- **SPY** CALL 750 2026-11-03 (4DTE): 3,472 traded vs OI 23
- **SPY** CALL 747 2026-10-30 (0DTE): 1,480 traded vs OI 432
- **SPY** PUT 728 2026-11-04 (5DTE): 508 traded vs OI 153
- **SPY** CALL 775 2026-11-11 (12DTE): 563 traded vs OI 451
- **SPY** PUT 715 2026-11-10 (11DTE): 561 traded vs OI 51
- **SPY** PUT 761 2026-11-20 (21DTE): 2,500 traded vs OI 1,987
- **SPY** PUT 720 2026-11-20 (21DTE): 46,559 traded vs OI 45,901

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
