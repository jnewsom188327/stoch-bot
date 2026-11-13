# GEX + FLOW SCAN - Fri Nov 13, 10:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (9)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:36 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/13 743P | 0.61 | 0.49 | +13% (1m) | **-20%** | +46% | 747.53 |
| 10:17 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 11/13 683C | 0.75 | 0.43 | -1% (0m) | **-43%** | +60% | 678.58 |
| 10:15 | **ARM** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 182.5P | 0.74 | 1.74 | +143% (21m) | **+135%** | +96% | 183.6 |
| 10:15 | **ORCL** | **CALLS** | FLIP CROSS up into positive gamma | 11/13 124C | 0.65 | 1.05 | +62% (25m) | **+62%** | +66% | 123.68 hit |
| 10:10 | **ORCL** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 120P | 0.46 | 0.17 | +7% (5m) | **-63%** | +63% | 121.25 |
| 10:05 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 297.5P | 0.74 | 3.44 | +396% (33m) | **+365%** | +288% | 295 hit |
| 09:55 | **BABA** | **PUTS** | FLOW SURGE | 11/13 94P | 0.51 | 0.44 | +8% (43m) | **-14%** | +49% | 93.36 |
| 09:45 | **UBER** | **CALLS** | TREND + FLOW | 11/13 70C | 0.59 | 0.12 | +0% (1m) | **-80%** | +32% | 70.7 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 127C | 0.46 | 0.15 | +22% (2m) | **-67%** | +48% | 126.38 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:40:08 ET, last candle SPY 10:39, QQQ 10:39 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:35 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** SPY261113P00743000 |
| 10:16 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | TURNING your way | **FIRE** QQQ261113C00683000 |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 10:40 MSTR CALLS: price -0.63 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:40 COIN CALLS: price -0.53 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:40 GOOGL CALLS: price -1.39 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:35 HOOD CALLS: price -0.35 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:35 MSTR CALLS: price -1.55 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **HOOD** | 76.98 | FLOW SURGE | **CALLS** | 64 | none: 30 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (26 contracts' greeks worked out here) | NEG -$12.0M | 79.72 | 80 | 80 | +$2.8M | +$43k bull / +$0 bear | SHORT (clean 36, ADX 62, RVol 3.0) |
| 2 | **COIN** | 125.66 | FLOW SURGE | **CALLS** | 61 | 11/13 128C @ 0.50 (delta 0.24) = est +78% at 127.62 | NEG -$18.4M | 133.18 | 137 | 125 | +$3.5M | +$1.1M bull / +$0 bear | out (clean 32, ADX 48, RVol 2.6) |
| 3 | **DELL** | 339.36 | TREND (flow not with it) | **PUTS** | 57 | none: 54 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (49 contracts' greeks worked out here) | NEG -$8.6M | - | 350 | 340 | +$8.0M | +$0 bull / -$36k bear | SHORT (clean 38, ADX 47, RVol 1.3) |
| 4 | **AVGO** | 340.34 | PINNED between the walls (positive gamma) - chop | **-** | 53 | - | POS +$61.5M | - | 340 | 340 | +$20.6M | +$556k bull / +$0 bear | SHORT (clean 35, ADX 46, RVol 0.9) |
| 5 | **IWM** | 275.93 | TREND (flow not with it) | **PUTS** | 51 | 11/13 275P @ 0.54 (delta 0.34) = est +35% at 275 | NEG -$2.7B | 282.75 | 285 | 275 | +$16.9M | +$0 bull / -$255k bear | SHORT (clean 36, ADX 51, RVol 1.3) |
| 6 | **AMD** | 527.37 | TREND (flow not with it) | **PUTS** | 51 | none: 172 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (76 contracts' greeks worked out here) | POS +$50.6M | - | 550 | 530 | +$68.0M | +$4.4M bull / -$6.6M bear | SHORT (clean 35, ADX 50, RVol 1.4) |
| 7 | **GOOGL** | 294.37 | FLOW SURGE | **CALLS** | 51 | 11/13 297.5C @ 0.59 (delta 0.23) = est +137% at 297.5 | POS +$153.4M | 289.26 | 300 | 290 | +$19.8M | +$2.9M bull / +$0 bear | out (clean 30, ADX 31, RVol 2.1) |
| 8 | **QQQ** | 673.61 | FLOW SURGE | **CALLS** | 49 | none: 750 calls 0-7DTE > 27 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (270 contracts' greeks worked out here) | NEG -$2.7B | 685.92 | 680 | 680 | +$316.4M | +$8.6M bull / -$3.6M bear | out (clean 32, ADX 57, RVol 1.7) |
| 9 | **MSTR** | 108.67 | FLOW SURGE | **CALLS** | 48 | 11/13 111C @ 0.52 (delta 0.25) = est +39% at 110 | NEG -$35.6M | - | 110 | 110 | +$6.5M | +$2.6M bull / +$0 bear | out (clean 31, ADX 43, RVol 1.5) |
| 10 | **AMZN** | 265.00 | PINNED between the walls (positive gamma) - chop | **-** | 45 | - | POS +$420.5M | - | 265 | 265 | +$7.3M | +$7.6M bull / +$0 bear | out (clean 30, ADX 34, RVol 0.9) |
| 11 | **NVDA** | 159.31 | FLOW SURGE | **CALLS** | 42 | none: 68 calls 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -12% at the target (needs +20%) (29 contracts' greeks worked out here) | NEG -$245.4M | - | 175 | 160 | +$118.8M | +$4.8M bull / -$2.4M bear | out (clean 31, ADX 17, RVol 1.2) |
| 12 | **PLTR** | 165.97 | - | **-** | 34 | - | POS +$69.4M | 158.91 | 165 | 165 | +$3.3M | +$0 bull / -$79k bear | out (clean 29, ADX 47, RVol 2.1) |
| 13 | **SMH** | 475.56 | - | **-** | 30 | - | NEG -$313.7M | - | 500 | 475 | +$10.6M | +$3.2M bull / -$1.0M bear | out (clean 31, ADX 52, RVol 1.3) |
| 14 | **MU** | 757.66 | - | **-** | 29 | - | NEG -$4.7M | 759.38 | 800 | 750 | +$79.7M | +$7.8M bull / -$3.8M bear | out (clean 31, ADX 37, RVol 1.5) |
| 15 | **SPY** | 749.89 | - | **-** | 28 | - | NEG -$8.3B | 758.85 | 750 | 750 | +$260.4M | +$1.9M bull / -$6.0M bear | out (clean 33, ADX 39, RVol 1.3) |
| 16 | **TSLA** | 387.62 | - | **-** | 28 | - | POS +$334.0M | - | 400 | 380 | +$65.0M | +$1.2M bull / -$2.3M bear | out (clean 29, ADX 24, RVol 1.8) |
| 17 | **ORCL** | 123.76 | - | **-** | 27 | - | POS +$5.5M | 122.53 | 130 | 125 | +$1.1M | +$0 bull / -$318k bear | out (clean 31, ADX 40, RVol 1.4) |
| 18 | **META** | 625.94 | - | **-** | 25 | - | NEG -$94.0M | 631.86 | 630 | 625 | +$10.9M | +$3.3M bull / -$27k bear | out (clean 29, ADX 33, RVol 2.4) |
| 19 | **AAPL** | 358.71 | - | **-** | 22 | - | POS +$1.3B | 348.13 | 360 | 360 | +$9.8M | +$486k bull / -$485k bear | out (clean 30, ADX 31, RVol 1.0) |
| 20 | **SMCI** | 26.22 | - | **-** | 21 | - | NEG -$2.5M | - | 27 | 25 | +$310k | - | out (clean 34, ADX 30, RVol 1.2) |
| 21 | **MSFT** | 522.88 | - | **-** | 20 | - | POS +$65.3M | 521.21 | 535 | 520 | -$600k | +$0 bull / -$410k bear | out (clean 32, ADX 37, RVol 1.6) |
| 22 | **ARM** | 184.00 | - | **-** | 20 | - | NEG -$2.7M | 190.19 | 185 | 180 | -$24k | +$62k bull / +$0 bear | out (clean 33, ADX 56, RVol 1.1) |
| 23 | **UBER** | 69.31 | - | **-** | 20 | - | POS +$9.6M | 68.88 | 70 | 70 | +$249k | - | out (clean 33, ADX 23, RVol 0.4) |
| 24 | **CRM** | 216.65 | - | **-** | 16 | - | NEG -$8.2M | 221.31 | 220 | 220 | +$80k | - | out (clean 29, ADX 22, RVol 1.3) |
| 25 | **NFLX** | 62.91 | - | **-** | 11 | - | NEG -$26.1M | 63.63 | 65 | 60 | +$97k | - | out (clean 31, ADX 34, RVol 2.0) |
| 26 | **SHOP** | 146.53 | - | **-** | 8 | - | POS +$3.6M | 144.65 | 150 | 140 | -$6k | - | out (clean 31, ADX 29, RVol 1.0) |
| 27 | **BABA** | 93.86 | - | **-** | 6 | - | NEG -$17.4M | - | 100 | 95 | +$4k | - | out (clean 28, ADX 25, RVol 1.0) |

## Big prints this scan (291)
- **AMD** CALL 540 2026-11-20 (7DTE): 1,000 @ 19.15 = **+$1.9M** SELL | vol 1,474 / OI 4,301
- **GOOGL** PUT 300 2026-11-20 (7DTE): 1,000 @ 8.80 = **+$880k** SELL | vol 1,485 / OI 10,076
- **AMD** PUT 530 2026-11-13 (0DTE): 1,000 @ 7.94 = **+$794k** BUY | vol 14,822 / OI 2,056
- **TSLA** PUT 400 2026-11-16 (3DTE): 450 @ 15.10 = **+$680k** BUY | vol 1,535 / OI 281
- **HOOD** CALL 79 2026-11-20 (7DTE): 3,000 @ 2.22 = **+$666k** MID | vol 3,332 / OI 188
- **META** PUT 630 2026-11-16 (3DTE): 635 @ 9.30 = **+$591k** MID | vol 1,791 / OI 212
- **QQQ** CALL 690 2026-11-20 (7DTE): 1,052 @ 4.92 = **+$518k** SELL | vol 4,599 / OI 16,372
- **META** CALL 640 2026-11-20 (7DTE): 505 @ 10.21 = **+$516k** BUY | vol 1,517 / OI 4,178
- **TSLA** PUT 395 2026-11-16 (3DTE): 450 @ 10.85 = **+$488k** BUY | vol 2,253 / OI 218
- **SPY** CALL 750 2026-11-16 (3DTE): 1,160 @ 3.73 = **+$433k** SELL | vol 13,006 / OI 1,280
- **SMH** CALL 460 2026-11-20 (7DTE): 156 @ 26.70 = **+$417k** BUY | vol 158 / OI 1,570
- **SMH** CALL 470 2026-11-20 (7DTE): 156 @ 20.20 = **+$315k** MID | vol 158 / OI 937
- **GOOGL** CALL 290 2026-11-13 (0DTE): 500 @ 6.11 = **+$306k** BUY | vol 1,410 / OI 5,090
- **GOOGL** CALL 290 2026-11-13 (0DTE): 500 @ 6.11 = **+$306k** BUY | vol 1,410 / OI 5,090
- **QQQ** PUT 680 2026-11-20 (7DTE): 200 @ 14.80 = **+$296k** BUY | vol 6,537 / OI 87,076

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 675 2026-11-19 (6DTE): 690 traded vs OI 0
- **SPY** CALL 786 2026-11-19 (6DTE): 2,802 traded vs OI 69
- **SPY** PUT 727 2026-11-13 (0DTE): 2,963 traded vs OI 2,810
- **SPY** PUT 732 2026-11-13 (0DTE): 6,075 traded vs OI 2,616
- **SPY** PUT 731 2026-11-18 (5DTE): 6,103 traded vs OI 597
- **SPY** CALL 746 2026-11-16 (3DTE): 505 traded vs OI 310
- **SPY** CALL 785 2026-11-19 (6DTE): 2,450 traded vs OI 340
- **SPY** PUT 751 2026-11-17 (4DTE): 501 traded vs OI 253
- **SPY** CALL 773 2026-11-18 (5DTE): 741 traded vs OI 665
- **SPY** PUT 695 2026-11-16 (3DTE): 692 traded vs OI 649
- **SPY** PUT 675 2026-11-20 (7DTE): 866 traded vs OI 0
- **QQQ** PUT 642 2026-11-13 (0DTE): 511 traded vs OI 330
- **QQQ** CALL 674 2026-11-16 (3DTE): 579 traded vs OI 153
- **QQQ** CALL 685 2026-11-18 (5DTE): 517 traded vs OI 209
- **QQQ** CALL 670 2026-11-13 (0DTE): 2,033 traded vs OI 1,959

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
