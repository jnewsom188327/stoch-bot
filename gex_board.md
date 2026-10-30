# GEX + FLOW SCAN - Fri Oct 30, 12:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.38 | +25% (7m) | **-48%** | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:20:08 ET, last candle SPY 12:19, QQQ 12:19 | no errors
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
| 1 | **NVDA** | 204.79 | FLOW SURGE | **CALLS** | 43 | 10/30 205C @ 0.71 (delta 0.46) = est +70% at 206.02 | NEG -$441.8M | 211.79 | 210 | 205 | +$23.5M | +$797k bull / +$0 bear | out (clean 26, ADX 41, RVol 1.2) |
| 2 | **ARM** | 203.94 | - | **-** | 32 | - | NEG -$21.2M | - | 220 | 205 | +$638k | +$0 bull / -$33k bear | out (clean 26, ADX 44, RVol 2.0) |
| 3 | **SMH** | 522.46 | - | **-** | 31 | - | NEG -$626.1M | - | 532.5 | 530 | +$6.9M | +$739k bull / +$0 bear | out (clean 29, ADX 51, RVol 3.0) |
| 4 | **DELL** | 423.20 | - | **-** | 31 | - | NEG -$54.0M | - | 440 | 425 | +$2.8M | +$57k bull / +$0 bear | out (clean 32, ADX 50, RVol 3.9) |
| 5 | **AMD** | 505.27 | - | **-** | 30 | - | NEG -$153.2M | 522.9 | 517.5 | 500 | +$24.3M | +$1.3M bull / +$0 bear | out (clean 29, ADX 40, RVol 1.4) |
| 6 | **COIN** | 140.23 | - | **-** | 30 | - | NEG -$16.1M | - | 140 | 140 | -$3.5M | +$67k bull / +$0 bear | out (clean 27, ADX 46, RVol 2.8) |
| 7 | **TSLA** | 400.87 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$408.5M | 394.42 | 400 | 400 | -$10.2M | +$699k bull / -$402k bear | out (clean 29, ADX 13, RVol 0.6) |
| 8 | **MU** | 883.09 | - | **-** | 26 | - | NEG -$275.8M | 933.48 | 900 | 900 | +$63.1M | +$3.1M bull / -$1.7M bear | out (clean 29, ADX 36, RVol 0.5) |
| 9 | **ORCL** | 132.45 | - | **-** | 26 | - | POS +$56.0M | 130.54 | 135 | 130 | +$2.2M | +$0 bull / -$66k bear | out (clean 33, ADX 40, RVol 0.6) |
| 10 | **AVGO** | 325.37 | - | **-** | 25 | - | NEG -$149.4M | - | 330 | 325 | +$2.2M | +$75k bull / +$0 bear | out (clean 30, ADX 52, RVol 0.8) |
| 11 | **SPY** | 757.28 | - | **-** | 24 | - | NEG -$14.5B | 771.49 | 760 | 755 | +$111.9M | +$713k bull / -$474k bear | out (clean 27, ADX 42, RVol 1.0) |
| 12 | **QQQ** | 692.45 | - | **-** | 23 | - | NEG -$10.3B | 726.18 | 720 | 690 | +$67.0M | +$813k bull / -$311k bear | out (clean 28, ADX 45, RVol 1.3) |
| 13 | **MSTR** | 132.79 | - | **-** | 23 | - | NEG -$21.4M | 138.47 | 135 | 130 | -$6.1M | +$0 bull / -$685k bear | out (clean 28, ADX 16, RVol 1.7) |
| 14 | **PLTR** | 186.96 | - | **-** | 20 | - | NEG -$71.1M | 192.85 | 185 | 190 | -$2.8M | +$0 bull / -$27k bear | out (clean 25, ADX 29, RVol 0.8) |
| 15 | **SMCI** | 32.17 | - | **-** | 20 | - | NEG -$3.4M | 32.56 | 35 | 32 | +$659k | - | out (clean 29, ADX 47, RVol 0.8) |
| 16 | **SHOP** | 155.59 | - | **-** | 20 | - | NEG -$14.8M | - | 150 | 157.5 | +$305k | - | out (clean 27, ADX 53, RVol 1.3) |
| 17 | **AAPL** | 347.52 | - | **-** | 19 | - | POS +$646.0M | 342.47 | 350 | 345 | -$4.8M | +$428k bull / -$39k bear | out (clean 32, ADX 20, RVol 1.5) |
| 18 | **MSFT** | 521.63 | - | **-** | 19 | - | POS +$458.8M | 516.02 | 525 | 525 | +$2.2M | +$269k bull / +$0 bear | out (clean 26, ADX 21, RVol 0.7) |
| 19 | **GOOGL** | 280.97 | - | **-** | 19 | - | NEG -$250.7M | - | 280 | 280 | -$3.2M | +$197k bull / -$58k bear | out (clean 32, ADX 14, RVol 0.9) |
| 20 | **AMZN** | 239.13 | - | **-** | 18 | - | NEG -$181.0M | 247.58 | 250 | 240 | -$4.2M | +$212k bull / -$282k bear | out (clean 31, ADX 17, RVol 1.4) |
| 21 | **IWM** | 279.30 | - | **-** | 14 | - | NEG -$936.9M | 281.27 | 278 | 278 | +$9.9M | - | out (clean 28, ADX 40, RVol 0.4) |
| 22 | **META** | 620.54 | - | **-** | 14 | - | NEG -$21.5M | 621.22 | 625 | 625 | -$1.1M | +$1.3M bull / +$0 bear | out (clean 28, ADX 13, RVol 0.7) |
| 23 | **NFLX** | 62.30 | - | **-** | 12 | - | NEG -$25.2M | 62.96 | 62 | 62 | +$1.1M | - | out (clean 31, ADX 15, RVol 0.9) |
| 24 | **HOOD** | 84.02 | - | **-** | 12 | - | NEG -$39.8M | - | 85 | 85 | +$721k | - | out (clean 31, ADX 48, RVol 0.5) |
| 25 | **BABA** | 98.54 | - | **-** | 9 | - | NEG -$36.7M | 99.62 | 100 | 99 | +$134k | - | out (clean 29, ADX 12, RVol 0.4) |
| 26 | **CRM** | 231.47 | - | **-** | 5 | - | NEG -$22.4M | 239.29 | 240 | 230 | -$73k | - | out (clean 27, ADX 10, RVol 0.4) |
| 27 | **UBER** | 65.16 | - | **-** | 3 | - | NEG -$33.2M | 66.18 | 65 | 65 | +$8k | - | out (clean 28, ADX 8, RVol 0.3) |

## Big prints this scan (127)
- **MSTR** CALL 136 2026-11-06 (7DTE): 1,372 @ 4.55 = **+$624k** SELL | vol 11,996 / OI 69
- **SPY** CALL 740 2026-11-06 (7DTE): 175 @ 20.40 = **+$357k** SELL | vol 832 / OI 84
- **SPY** PUT 760 2026-10-30 (0DTE): 1,000 @ 3.00 = **+$300k** SELL | vol 199,837 / OI 33,031
- **MU** PUT 880 2026-10-30 (0DTE): 600 @ 4.20 = **+$252k** SELL | vol 30,294 / OI 2,467
- **META** CALL 645 2026-11-06 (7DTE): 370 @ 6.30 = **+$233k** BUY | vol 1,993 / OI 3,329
- **QQQ** CALL 700 2026-11-06 (7DTE): 260 @ 7.17 = **+$186k** SELL | vol 35,454 / OI 1,011
- **META** CALL 645 2026-11-06 (7DTE): 255 @ 6.65 = **+$170k** BUY | vol 1,993 / OI 3,329
- **MU** PUT 880 2026-10-30 (0DTE): 300 @ 5.50 = **+$165k** BUY | vol 30,294 / OI 2,467
- **MU** PUT 880 2026-10-30 (0DTE): 298 @ 5.50 = **+$164k** BUY | vol 30,294 / OI 2,467
- **QQQ** PUT 700 2026-10-30 (0DTE): 197 @ 7.77 = **+$153k** MID | vol 36,437 / OI 42,068
- **SPY** PUT 780 2026-11-04 (5DTE): 63 @ 22.71 = **+$143k** MID | vol 88 / OI 25
- **MU** PUT 900 2026-11-06 (7DTE): 33 @ 39.20 = **+$129k** SELL | vol 1,217 / OI 1,338
- **AMZN** CALL 240 2026-11-02 (3DTE): 500 @ 2.57 = **+$128k** SELL | vol 8,979 / OI 329
- **QQQ** CALL 700 2026-11-06 (7DTE): 174 @ 7.18 = **+$125k** SELL | vol 35,454 / OI 1,011
- **META** CALL 617.5 2026-10-30 (0DTE): 200 @ 6.05 = **+$121k** BUY | vol 5,250 / OI 489

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 779 2026-11-03 (4DTE): 651 traded vs OI 470
- **SPY** PUT 753 2026-11-04 (5DTE): 510 traded vs OI 301
- **SPY** CALL 785 2026-11-05 (6DTE): 729 traded vs OI 695
- **SPY** CALL 780 2026-11-10 (11DTE): 611 traded vs OI 609
- **QQQ** CALL 699 2026-11-04 (5DTE): 541 traded vs OI 0
- **QQQ** PUT 679 2026-11-04 (5DTE): 555 traded vs OI 0
- **QQQ** CALL 708 2026-11-03 (4DTE): 547 traded vs OI 128
- **QQQ** CALL 725 2026-11-04 (5DTE): 840 traded vs OI 814
- **QQQ** PUT 673 2026-11-04 (5DTE): 552 traded vs OI 0
- **QQQ** PUT 691 2026-11-03 (4DTE): 505 traded vs OI 0
- **QQQ** CALL 725 2026-11-09 (10DTE): 508 traded vs OI 215
- **IWM** PUT 276 2026-10-30 (0DTE): 2,895 traded vs OI 2,484
- **NVDA** CALL 217.5 2026-11-06 (7DTE): 4,619 traded vs OI 4,565
- **NVDA** PUT 207.5 2026-11-06 (7DTE): 2,155 traded vs OI 2,142
- **NVDA** CALL 195 2026-11-04 (5DTE): 524 traded vs OI 34

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
