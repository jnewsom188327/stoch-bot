# GEX + FLOW SCAN - Fri Nov 13, 12:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (12)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:30 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 292.5P | 0.56 | 0.19 | +23% (10m) | **-66%** | +237% | 290.96 |
| 11:15 | **ARM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/13 180P | 0.79 | 0.11 | +18% (40m) | **-86%** | +122% | 180 |
| 11:14 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/13 667P | 0.70 | 0.16 | +59% (9m) | **-77%** | +21% | 672.05 hit |
| 10:36 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/13 743P | 0.61 | 0.22 | +13% (1m) | **-64%** (done) | +46% | 747.53 |
| 10:17 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 11/13 683C | 0.75 | 0.18 | -1% (0m) | **-76%** (done) | +60% | 678.58 |
| 10:15 | **ARM** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 182.5P | 0.74 | 1.47 | +169% (50m) | **+99%** (done) | +96% | 183.6 hit |
| 10:15 | **ORCL** | **CALLS** | FLIP CROSS up into positive gamma | 11/13 124C | 0.65 | 0.35 | +89% (28m) | **-46%** (done) | +66% | 123.68 hit |
| 10:10 | **ORCL** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 120P | 0.46 | 0.15 | +7% (5m) | **-67%** (done) | +63% | 121.25 |
| 10:05 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 297.5P | 0.74 | 3.42 | +396% (33m) | **+362%** (done) | +288% | 295 hit |
| 09:55 | **BABA** | **PUTS** | FLOW SURGE | 11/13 94P | 0.51 | 0.43 | +8% (43m) | **-16%** (done) | +49% | 93.36 |
| 09:45 | **UBER** | **CALLS** | TREND + FLOW | 11/13 70C | 0.59 | 0.06 | +0% (1m) | **-90%** (done) | +32% | 70.7 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 127C | 0.46 | 0.22 | +22% (2m) | **-52%** (done) | +48% | 126.38 |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:10:08 ET, last candle SPY 12:09, QQQ 12:09 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:13 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** QQQ261113P00667000 |
| 11:02 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:35 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** SPY261113P00743000 |
| 10:16 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | TURNING your way | **FIRE** QQQ261113C00683000 |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 11:45 HOOD CALLS: price -0.30 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:40 HOOD CALLS: under EMA 20 - flow says one way, price says the other
- 11:35 HOOD CALLS: under EMA 20 - flow says one way, price says the other
- 11:25 HOOD CALLS: price -0.54 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:20 HOOD CALLS: price -0.21 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **ARM** | 189.94 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 57 | none: 30 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (26 contracts' greeks worked out here) | POS +$556k | 189.42 | 200 | 190 | -$3.7M | +$0 bull / -$1.2M bear | out (clean 33, ADX 48, RVol 1.7) |
| 2 | **AMZN** | 265.44 | PINNED between the walls (positive gamma) - chop | **-** | 38 | - | POS +$400.5M | 254.02 | 265 | 265 | +$8.9M | +$124k bull / -$190k bear | out (clean 30, ADX 32, RVol 0.6) |
| 3 | **META** | 633.53 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 35 | none: 185 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (82 contracts' greeks worked out here) | POS +$24.1M | 632.3 | 630 | 635 | +$6.0M | +$26k bull / -$25k bear | out (clean 29, ADX 25, RVol 0.5) |
| 4 | **MU** | 762.94 | FLIP CROSS down into negative gamma | **PUTS** | 33 | none: 164 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (73 contracts' greeks worked out here) | NEG -$39.1M | 776.67 | 760 | 750 | +$71.1M | +$84k bull / -$1.3M bear | out (clean 30, ADX 27, RVol 0.5) |
| 5 | **GOOGL** | 295.46 | - | **-** | 30 | - | POS +$207.0M | 289.73 | 300 | 290 | +$19.7M | +$0 bull / -$63k bear | out (clean 32, ADX 28, RVol 0.8) |
| 6 | **DELL** | 339.27 | - | **-** | 29 | - | NEG -$8.7M | - | 350 | 340 | +$7.0M | +$0 bull / -$400k bear | out (clean 38, ADX 47, RVol 1.5) |
| 7 | **AVGO** | 345.47 | - | **-** | 28 | - | POS +$87.2M | 328.86 | 350 | 340 | +$19.5M | +$0 bull / -$302k bear | out (clean 36, ADX 33, RVol 0.4) |
| 8 | **HOOD** | 77.86 | - | **-** | 28 | - | NEG -$15.6M | 80.24 | 85 | 80 | +$2.9M | +$0 bull / -$148k bear | out (clean 36, ADX 44, RVol 1.0) |
| 9 | **AMD** | 527.72 | - | **-** | 25 | - | POS +$44.8M | - | 530 | 530 | +$63.0M | +$489k bull / -$3.3M bear | out (clean 36, ADX 46, RVol 0.5) |
| 10 | **QQQ** | 677.66 | - | **-** | 24 | - | NEG -$3.1B | 690.81 | 680 | 680 | +$265.9M | +$0 bull / -$634k bear | out (clean 32, ADX 38, RVol 0.5) |
| 11 | **SMH** | 482.44 | - | **-** | 24 | - | NEG -$341.4M | - | 500 | 475 | +$10.8M | +$0 bull / -$540k bear | out (clean 31, ADX 39, RVol 0.3) |
| 12 | **IWM** | 276.91 | - | **-** | 23 | - | NEG -$2.5B | 282.81 | 285 | 275 | +$19.7M | +$0 bull / -$51k bear | out (clean 36, ADX 23, RVol 0.6) |
| 13 | **SPY** | 752.01 | - | **-** | 21 | - | NEG -$8.2B | 760.66 | 750 | 750 | +$258.3M | +$1.6M bull / -$2.6M bear | out (clean 33, ADX 24, RVol 0.5) |
| 14 | **NVDA** | 160.62 | - | **-** | 21 | - | NEG -$291.0M | - | 175 | 160 | +$102.8M | +$392k bull / -$3.8M bear | out (clean 31, ADX 16, RVol 0.5) |
| 15 | **COIN** | 127.96 | - | **-** | 21 | - | NEG -$22.6M | 132.76 | 140 | 130 | +$3.6M | - | out (clean 30, ADX 32, RVol 0.9) |
| 16 | **MSTR** | 109.79 | - | **-** | 19 | - | NEG -$46.6M | - | 110 | 110 | +$4.1M | +$0 bull / -$1.9M bear | out (clean 30, ADX 28, RVol 0.3) |
| 17 | **TSLA** | 391.86 | - | **-** | 18 | - | POS +$393.2M | 381.43 | 400 | 390 | +$48.3M | +$0 bull / -$400k bear | out (clean 29, ADX 13, RVol 0.5) |
| 18 | **AAPL** | 358.74 | - | **-** | 18 | - | POS +$1.3B | 347.44 | 360 | 360 | +$12.5M | +$140k bull / -$88k bear | out (clean 30, ADX 15, RVol 0.5) |
| 19 | **PLTR** | 168.60 | - | **-** | 16 | - | POS +$88.2M | 162.87 | 170 | 170 | -$862k | +$0 bull / -$70k bear | out (clean 29, ADX 25, RVol 0.2) |
| 20 | **MSFT** | 524.23 | - | **-** | 14 | - | POS +$107.1M | 522.16 | 535 | 520 | -$1.2M | +$271k bull / -$243k bear | out (clean 31, ADX 17, RVol 0.3) |
| 21 | **UBER** | 69.60 | - | **-** | 14 | - | POS +$15.1M | 68.97 | 70 | 70 | +$280k | - | out (clean 33, ADX 13, RVol 0.4) |
| 22 | **NFLX** | 62.24 | - | **-** | 12 | - | NEG -$42.0M | 63.41 | 65 | 62 | +$551k | - | out (clean 32, ADX 37, RVol 0.8) |
| 23 | **CRM** | 217.82 | - | **-** | 10 | - | NEG -$7.1M | 222.01 | 220 | 220 | +$77k | - | out (clean 28, ADX 19, RVol 0.9) |
| 24 | **SMCI** | 26.41 | - | **-** | 9 | - | NEG -$3.2M | - | 27 | 27 | +$187k | - | out (clean 34, ADX 25, RVol 0.4) |
| 25 | **ORCL** | 124.17 | - | **-** | 8 | - | NEG -$1.3M | 124.45 | 125 | 125 | -$1.0M | - | out (clean 31, ADX 27, RVol 0.5) |
| 26 | **SHOP** | 147.35 | - | **-** | 6 | - | POS +$3.2M | 145.92 | 150 | 140 | +$45k | - | out (clean 31, ADX 17, RVol 0.4) |
| 27 | **BABA** | 94.05 | - | **-** | 6 | - | NEG -$20.8M | - | 100 | 95 | +$38k | - | out (clean 27, ADX 24, RVol 0.3) |

## Big prints this scan (103)
- **MSTR** CALL 112 2026-11-20 (7DTE): 5,000 @ 3.70 = **+$1.9M** SELL | vol 8,775 / OI 0
- **SPY** CALL 750 2026-11-16 (3DTE): 1,755 @ 3.91 = **+$686k** SELL | vol 38,657 / OI 1,280
- **SPY** CALL 750 2026-11-16 (3DTE): 1,056 @ 3.62 = **+$382k** SELL | vol 38,657 / OI 1,280
- **SPY** CALL 750 2026-11-16 (3DTE): 915 @ 3.75 = **+$343k** SELL | vol 38,657 / OI 1,280
- **AMD** PUT 520 2026-11-13 (0DTE): 589 @ 4.75 = **+$280k** BUY | vol 19,875 / OI 1,013
- **SMH** PUT 500 2026-11-20 (7DTE): 99 @ 27.90 = **+$276k** BUY | vol 691 / OI 9,935
- **SPY** CALL 750 2026-11-16 (3DTE): 738 @ 3.63 = **+$268k** SELL | vol 38,657 / OI 1,280
- **QQQ** PUT 688 2026-11-13 (0DTE): 150 @ 14.39 = **+$216k** BUY | vol 16,151 / OI 4,861
- **SPY** PUT 755 2026-11-16 (3DTE): 270 @ 6.59 = **+$178k** BUY | vol 14,931 / OI 2,248
- **SPY** PUT 755 2026-11-16 (3DTE): 237 @ 7.19 = **+$170k** BUY | vol 14,931 / OI 2,248
- **AMD** CALL 522.5 2026-11-16 (3DTE): 100 @ 13.80 = **+$138k** SELL | vol 297 / OI 61
- **AMD** CALL 522.5 2026-11-16 (3DTE): 100 @ 12.60 = **+$126k** SELL | vol 297 / OI 61
- **SPY** CALL 750 2026-11-16 (3DTE): 328 @ 3.73 = **+$122k** SELL | vol 38,657 / OI 1,280
- **AMD** CALL 550 2026-11-20 (7DTE): 80 @ 13.53 = **+$108k** SELL | vol 3,469 / OI 5,879
- **QQQ** PUT 680 2026-11-13 (0DTE): 150 @ 6.74 = **+$101k** BUY | vol 87,057 / OI 11,590

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 734 2026-11-17 (4DTE): 634 traded vs OI 629
- **SPY** PUT 727 2026-11-17 (4DTE): 515 traded vs OI 357
- **SPY** PUT 765 2026-11-27 (14DTE): 942 traded vs OI 805
- **QQQ** CALL 689 2026-11-17 (4DTE): 502 traded vs OI 263
- **QQQ** PUT 643 2026-11-13 (0DTE): 1,582 traded vs OI 778
- **QQQ** CALL 674 2026-11-18 (5DTE): 530 traded vs OI 214
- **QQQ** PUT 676 2026-11-17 (4DTE): 514 traded vs OI 148
- **QQQ** CALL 740 2026-11-18 (5DTE): 551 traded vs OI 403
- **QQQ** CALL 745 2026-11-18 (5DTE): 510 traded vs OI 156
- **QQQ** PUT 648 2026-11-23 (10DTE): 501 traded vs OI 56
- **IWM** PUT 267.5 2026-11-19 (6DTE): 721 traded vs OI 275
- **SMH** PUT 455 2026-11-16 (3DTE): 548 traded vs OI 547
- **SMH** PUT 435 2026-11-13 (0DTE): 705 traded vs OI 0
- **TSLA** PUT 370 2026-11-18 (5DTE): 520 traded vs OI 209
- **AMD** CALL 580 2026-11-18 (5DTE): 656 traded vs OI 255

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
