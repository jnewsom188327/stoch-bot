# GEX + FLOW SCAN - Fri Oct 30, 02:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:00:08 ET, last candle SPY 13:59, QQQ 13:59 | no errors
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
| 1 | **DELL** | 414.72 | TREND (flow not with it) | **PUTS** | 59 | none: 66 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (56 contracts' greeks worked out here) | NEG -$47.7M | - | 440 | 420 | +$6.4M | +$0 bull / -$93k bear | SHORT (clean 34, ADX 59, RVol 2.1) |
| 2 | **MSFT** | 521.07 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 37 | none: 168 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (75 contracts' greeks worked out here) | POS +$416.8M | 516.82 | 525 | 520 | +$4.1M | +$0 bull / -$463k bear | out (clean 26, ADX 15, RVol 0.8) |
| 3 | **AAPL** | 344.62 | PINNED between the walls (positive gamma) - chop | **-** | 36 | - | POS +$267.1M | 341.92 | 345 | 345 | +$6.4M | +$311k bull / +$0 bear | out (clean 31, ADX 26, RVol 1.4) |
| 4 | **AMD** | 498.22 | - | **-** | 29 | - | NEG -$175.5M | 519.03 | 500 | 500 | +$36.1M | +$873k bull / -$628k bear | out (clean 30, ADX 49, RVol 1.4) |
| 5 | **SPY** | 754.00 | - | **-** | 28 | - | NEG -$16.1B | 771.98 | 800 | 750 | +$211.4M | +$14.4M bull / +$0 bear | out (clean 27, ADX 46, RVol 1.9) |
| 6 | **NVDA** | 202.80 | - | **-** | 28 | - | NEG -$435.3M | 211.86 | 210 | 200 | +$37.8M | +$851k bull / +$0 bear | out (clean 28, ADX 51, RVol 1.0) |
| 7 | **TSLA** | 395.46 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$436.0M | 375.65 | 395 | 395 | -$5.2M | +$1.5M bull / +$0 bear | out (clean 29, ADX 16, RVol 0.7) |
| 8 | **COIN** | 138.12 | - | **-** | 26 | - | NEG -$13.9M | - | 140 | 140 | -$1.6M | +$1.5M bull / +$0 bear | out (clean 28, ADX 50, RVol 3.3) |
| 9 | **MU** | 869.80 | - | **-** | 26 | - | NEG -$300.4M | - | 880 | 880 | +$70.9M | +$5.0M bull / +$0 bear | out (clean 30, ADX 42, RVol 1.1) |
| 10 | **QQQ** | 687.33 | - | **-** | 25 | - | NEG -$9.7B | 727.88 | 720 | 690 | +$143.6M | +$6.5M bull / +$0 bear | out (clean 28, ADX 50, RVol 1.9) |
| 11 | **SMH** | 516.42 | - | **-** | 25 | - | NEG -$672.8M | - | 532.5 | 505 | +$7.4M | +$59k bull / +$0 bear | out (clean 30, ADX 53, RVol 0.7) |
| 12 | **IWM** | 278.18 | - | **-** | 24 | - | NEG -$1.4B | 281 | 278 | 278 | +$11.0M | +$2.1M bull / +$0 bear | out (clean 28, ADX 44, RVol 0.8) |
| 13 | **NFLX** | 62.02 | - | **-** | 24 | - | NEG -$26.0M | 62.41 | 62 | 62 | +$1.4M | +$33k bull / +$0 bear | out (clean 30, ADX 22, RVol 1.0) |
| 14 | **HOOD** | 82.75 | - | **-** | 24 | - | NEG -$30.2M | - | 85 | 83 | +$2.1M | +$649k bull / +$0 bear | out (clean 32, ADX 50, RVol 0.8) |
| 15 | **SHOP** | 154.49 | - | **-** | 24 | - | NEG -$11.9M | - | 150 | 157.5 | +$781k | - | out (clean 27, ADX 49, RVol 1.2) |
| 16 | **AVGO** | 322.70 | - | **-** | 23 | - | NEG -$158.8M | - | 340 | 320 | +$1.9M | +$68k bull / +$0 bear | out (clean 29, ADX 44, RVol 1.1) |
| 17 | **PLTR** | 184.34 | - | **-** | 20 | - | NEG -$74.1M | 193.01 | 185 | 185 | +$4.0M | +$2.3M bull / +$0 bear | out (clean 26, ADX 32, RVol 0.9) |
| 18 | **SMCI** | 31.62 | - | **-** | 19 | - | NEG -$4.4M | 32.77 | 32 | 32 | +$784k | - | out (clean 30, ADX 52, RVol 1.1) |
| 19 | **META** | 615.80 | - | **-** | 18 | - | NEG -$135.7M | 620.18 | 650 | 610 | +$4.7M | +$1.3M bull / +$0 bear | out (clean 28, ADX 28, RVol 0.5) |
| 20 | **GOOGL** | 278.60 | - | **-** | 18 | - | NEG -$232.8M | - | 280 | 280 | +$677k | +$294k bull / +$0 bear | out (clean 32, ADX 39, RVol 0.5) |
| 21 | **MSTR** | 128.89 | - | **-** | 18 | - | NEG -$31.2M | - | 135 | 130 | -$3.5M | +$27k bull / +$0 bear | out (clean 29, ADX 28, RVol 0.6) |
| 22 | **ARM** | 201.16 | - | **-** | 18 | - | NEG -$19.2M | - | 220 | 200 | +$896k | - | out (clean 25, ADX 33, RVol 2.2) |
| 23 | **AMZN** | 239.30 | - | **-** | 16 | - | NEG -$172.9M | 244.93 | 250 | 240 | -$5.0M | +$64k bull / -$220k bear | out (clean 30, ADX 13, RVol 0.9) |
| 24 | **BABA** | 97.98 | - | **-** | 15 | - | NEG -$43.2M | 98.88 | 100 | 98 | +$564k | - | out (clean 29, ADX 21, RVol 0.6) |
| 25 | **UBER** | 64.93 | - | **-** | 14 | - | NEG -$37.1M | 66.24 | 65 | 65 | +$330k | - | out (clean 28, ADX 22, RVol 0.6) |
| 26 | **ORCL** | 130.38 | - | **-** | 13 | - | POS +$14.3M | 129.53 | 130 | 130 | +$2.7M | - | out (clean 34, ADX 29, RVol 0.5) |
| 27 | **CRM** | 229.77 | - | **-** | 12 | - | NEG -$30.4M | 240.11 | 230 | 230 | +$326k | - | out (clean 28, ADX 31, RVol 0.5) |

## Big prints this scan (80)
- **QQQ** PUT 715 2026-10-30 (0DTE): 300 @ 26.35 = **+$790k** SELL | vol 2,914 / OI 22,186
- **SPY** PUT 740 2026-11-06 (7DTE): 2,148 @ 3.17 = **+$681k** SELL | vol 10,694 / OI 5,200
- **QQQ** PUT 715 2026-10-30 (0DTE): 240 @ 26.12 = **+$627k** SELL | vol 2,914 / OI 22,186
- **QQQ** PUT 715 2026-10-30 (0DTE): 230 @ 26.32 = **+$605k** SELL | vol 2,914 / OI 22,186
- **SPY** PUT 740 2026-11-06 (7DTE): 1,669 @ 3.13 = **+$522k** SELL | vol 10,694 / OI 5,200
- **SPY** PUT 735 2026-11-06 (7DTE): 2,148 @ 2.39 = **+$513k** SELL | vol 7,817 / OI 9,769
- **MU** PUT 895 2026-10-30 (0DTE): 200 @ 22.28 = **+$446k** SELL | vol 10,209 / OI 1,347
- **SPY** PUT 735 2026-11-06 (7DTE): 1,669 @ 2.35 = **+$392k** SELL | vol 7,817 / OI 9,769
- **IWM** PUT 279 2026-11-06 (7DTE): 1,000 @ 3.71 = **+$371k** SELL | vol 4,651 / OI 1,724
- **MU** PUT 890 2026-10-30 (0DTE): 200 @ 17.60 = **+$352k** SELL | vol 23,530 / OI 1,303
- **MU** CALL 860 2026-10-30 (0DTE): 200 @ 15.22 = **+$304k** BUY | vol 800 / OI 219
- **IWM** PUT 277 2026-11-06 (7DTE): 1,000 @ 2.87 = **+$287k** SELL | vol 4,061 / OI 523
- **QQQ** PUT 692 2026-10-30 (0DTE): 682 @ 3.75 = **+$256k** SELL | vol 184,491 / OI 2,435
- **MU** CALL 865 2026-10-30 (0DTE): 200 @ 11.02 = **+$220k** BUY | vol 767 / OI 204
- **QQQ** PUT 713 2026-10-30 (0DTE): 86 @ 24.21 = **+$208k** SELL | vol 1,597 / OI 3,537

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 753 2026-11-02 (3DTE): 560 traded vs OI 30
- **SPY** PUT 743 2026-11-04 (5DTE): 501 traded vs OI 172
- **SPY** CALL 756 2026-11-04 (5DTE): 598 traded vs OI 66
- **QQQ** CALL 755 2026-11-27 (28DTE): 664 traded vs OI 476
- **QQQ** PUT 665 2026-11-12 (13DTE): 502 traded vs OI 0
- **QQQ** PUT 670 2026-11-11 (12DTE): 505 traded vs OI 39
- **QQQ** CALL 720 2026-11-10 (11DTE): 501 traded vs OI 58
- **IWM** PUT 275 2026-11-04 (5DTE): 746 traded vs OI 743
- **NVDA** PUT 190 2026-11-04 (5DTE): 920 traded vs OI 914
- **NVDA** CALL 220 2026-11-09 (10DTE): 500 traded vs OI 433
- **NVDA** PUT 190 2026-11-02 (3DTE): 5,700 traded vs OI 5,376
- **META** CALL 615 2026-11-02 (3DTE): 526 traded vs OI 211
- **MSFT** PUT 470 2026-11-06 (7DTE): 560 traded vs OI 501
- **AVGO** CALL 320 2026-11-20 (21DTE): 1,673 traded vs OI 853
- **MU** CALL 865 2026-10-30 (0DTE): 767 traded vs OI 204

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
