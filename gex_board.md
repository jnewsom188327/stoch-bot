# GEX + FLOW SCAN - Wed Nov 04, 10:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (6)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:20 | **SMCI** | **CALLS** | FLOW SURGE | 11/06 33C | 0.65 | 0.54 | -17% (0m) | **-17%** | +39% | 32.81 |
| 10:20 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 284C | 0.49 | 0.48 | -2% (0m) | **-2%** | +131% | 284.74 |
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 0.96 | +41% (20m) | **+41%** | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.36 | +127% (30m) | **+127%** | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.07 | +2% (1m) | **-87%** | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.15 | -3% (1m) | **-76%** | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:20:08 ET, last candle SPY 10:19, QQQ 10:19 | no errors

## Flow surges NOT fired - price disagreed (19 today, last 5)
- 10:20 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 10:20 UBER PUTS: price +0.28 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:20 GOOGL PUTS: price +1.36 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:15 BABA PUTS: price +0.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:15 UBER PUTS: price +1.17 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 283.13 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 71 | 11/04 284C @ 0.49 (delta 0.34) = est +131% at 284.74 | NEG -$495.9M | 284.74 | 285 | 270 | +$14.9M | +$379k bull / +$0 bear | LONG (clean 34, ADX 33, RVol 1.4) |
| 2 | **BABA** | 106.83 | FLOW SURGE | **PUTS** | 64 | 11/06 104P @ 0.69 (delta 0.24) = est +36% at 105.66 | POS +$16.5M | - | 110 | 110 | -$1.1M | +$0 bull / -$144k bear | LONG (clean 36, ADX 56, RVol 3.5) |
| 3 | **AMZN** | 268.96 | FLOW SURGE | **PUTS** | 58 | none: 88 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (33 contracts' greeks worked out here) | POS +$541.0M | - | 270 | 250 | -$32.9M | +$917k bull / -$2.0M bear | LONG (clean 34, ADX 59, RVol 2.6) |
| 4 | **UBER** | 71.14 | FLOW SURGE | **PUTS** | 58 | 11/06 70P @ 0.80 (delta 0.35) = est +46% at 70 | POS +$10.4M | 68.03 | 70 | 65 | -$1.2M | +$0 bull / -$88k bear | out (clean 30, ADX 49, RVol 2.2) |
| 5 | **AAPL** | 353.05 | FLOW SURGE | **PUTS** | 57 | none: 108 puts 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (54 contracts' greeks worked out here) | POS +$973.2M | 341.28 | 355 | 350 | -$82.3M | +$350k bull / -$3.9M bear | out (clean 32, ADX 50, RVol 2.5) |
| 6 | **GOOGL** | 295.57 | FLOW SURGE | **PUTS** | 57 | 11/04 292.5P @ 0.68 (delta 0.24) = est +319% at 290 | POS +$123.1M | 280.74 | 300 | 290 | -$33.5M | +$0 bull / -$1.6M bear | LONG (clean 35, ADX 59, RVol 1.6) |
| 7 | **TSLA** | 388.13 | FLOW SURGE | **PUTS** | 54 | none: 124 puts 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (47 contracts' greeks worked out here) | NEG -$74.9M | 394.19 | 400 | 380 | -$70.9M | +$0 bull / -$3.7M bear | out (clean 30, ADX 28, RVol 2.6) |
| 8 | **MSFT** | 553.27 | FLOW SURGE | **PUTS** | 54 | none: 165 puts 0-7DTE > 14 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (92 contracts' greeks worked out here) | POS +$990.1M | - | 550 | 535 | -$24.3M | +$1.0M bull / -$1.9M bear | out (clean 29, ADX 63, RVol 3.6) |
| 9 | **QQQ** | 699.54 | FLOW SURGE | **PUTS** | 46 | none: 616 puts 0-7DTE > 45 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (213 contracts' greeks worked out here) | NEG -$3.9B | 720.55 | 700 | 680 | -$187.8M | +$0 bull / -$4.9M bear | out (clean 30, ADX 39, RVol 1.5) |
| 10 | **SMCI** | 31.92 | FLOW SURGE | **CALLS** | 46 | 11/06 33C @ 0.65 (delta 0.36) = est +39% at 32.81 | POS +$7.1M | - | 34.5 | 30 | +$1.2M | +$293k bull / +$0 bear | out (clean 33, ADX 19, RVol 2.2) |
| 11 | **SHOP** | 149.26 | TREND (flow not with it) | **CALLS** | 46 | none: 21 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$8.9M | - | 160 | 135 | -$119k | - | LONG (clean 35, ADX 30, RVol 2.4) |
| 12 | **COIN** | 152.16 | FLOW SURGE | **PUTS** | 44 | none: 20 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$28.2M | - | 148 | 150 | -$1.1M | +$0 bull / -$33k bear | out (clean 30, ADX 19, RVol 1.7) |
| 13 | **ARM** | 202.58 | FLOW SURGE | **CALLS** | 43 | none: 17 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$5.8M | - | 212.5 | 200 | +$493k | +$141k bull / +$0 bear | out (clean 26, ADX 22, RVol 0.8) |
| 14 | **NFLX** | 66.02 | FLOW SURGE | **PUTS** | 42 | 11/06 65P @ 0.45 (delta 0.31) = est +80% at 65 | POS +$19.2M | 62.25 | 65 | 65 | -$2.0M | +$0 bull / -$28k bear | out (clean 30, ADX 59, RVol 1.3) |
| 15 | **HOOD** | 87.97 | FLOW SURGE | **PUTS** | 38 | none: 17 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$2.7M | 84.71 | 90 | 90 | -$2.2M | +$0 bull / -$171k bear | out (clean 29, ADX 19, RVol 1.2) |
| 16 | **MSTR** | 144.62 | - | **-** | 30 | - | POS +$119.6M | - | 135 | 150 | -$2.3M | +$0 bull / -$307k bear | out (clean 30, ADX 45, RVol 1.7) |
| 17 | **SPY** | 767.82 | - | **-** | 27 | - | NEG -$2.4B | 770.26 | 770 | 750 | -$86.0M | +$1.6M bull / -$4.0M bear | out (clean 31, ADX 44, RVol 1.8) |
| 18 | **DELL** | 388.66 | - | **-** | 27 | - | NEG -$28.9M | - | 400 | 400 | -$1.4M | +$0 bull / -$43k bear | out (clean 33, ADX 34, RVol 1.7) |
| 19 | **SMH** | 516.28 | - | **-** | 26 | - | NEG -$424.5M | - | 532.5 | 500 | +$1.5M | +$91k bull / +$0 bear | out (clean 31, ADX 22, RVol 2.3) |
| 20 | **MU** | 832.93 | - | **-** | 26 | - | NEG -$308.1M | - | 840 | 850 | +$42.1M | +$5.3M bull / -$1.8M bear | out (clean 30, ADX 20, RVol 1.8) |
| 21 | **AMD** | 497.70 | - | **-** | 25 | - | NEG -$49.7M | - | 500 | 500 | +$21.3M | +$1.9M bull / -$1.1M bear | out (clean 32, ADX 30, RVol 2.3) |
| 22 | **META** | 637.18 | - | **-** | 25 | - | POS +$224.1M | 619.7 | 650 | 625 | -$4.1M | +$0 bull / -$473k bear | out (clean 30, ADX 51, RVol 1.8) |
| 23 | **PLTR** | 176.08 | - | **-** | 25 | - | NEG -$39.9M | - | 180 | 180 | -$4.0M | +$0 bull / -$119k bear | out (clean 26, ADX 20, RVol 1.4) |
| 24 | **AVGO** | 331.42 | - | **-** | 23 | - | NEG -$70.3M | 349.66 | 340 | 330 | +$1.7M | +$28k bull / +$0 bear | out (clean 30, ADX 21, RVol 2.1) |
| 25 | **NVDA** | 205.34 | - | **-** | 21 | - | POS +$62.7M | 204.22 | 210 | 200 | -$2.4M | +$349k bull / -$967k bear | out (clean 29, ADX 32, RVol 1.9) |
| 26 | **CRM** | 233.07 | - | **-** | 14 | - | NEG -$5.6M | 238.56 | 240 | 220 | -$72k | - | out (clean 31, ADX 52, RVol 0.9) |
| 27 | **ORCL** | 127.64 | - | **-** | 11 | - | NEG -$26.4M | - | 130 | 125 | -$441k | - | out (clean 35, ADX 21, RVol 2.8) |

## Big prints this scan (210)
- **AAPL** CALL 340 2026-11-04 (0DTE): 490 @ 12.87 = **+$631k** SELL | vol 9,007 / OI 2,790
- **SPY** PUT 763 2026-11-11 (7DTE): 1,367 @ 3.96 = **+$541k** SELL | vol 2,210 / OI 0
- **AAPL** CALL 347.5 2026-11-04 (0DTE): 568 @ 5.67 = **+$322k** SELL | vol 26,776 / OI 4,478
- **SPY** CALL 767 2026-11-09 (5DTE): 500 @ 5.70 = **+$285k** BUY | vol 1,697 / OI 0
- **QQQ** PUT 699 2026-11-04 (0DTE): 1,000 @ 2.74 = **+$274k** BUY | vol 7,452 / OI 132
- **MSFT** PUT 580 2026-11-06 (2DTE): 100 @ 26.50 = **+$265k** SELL | vol 300 / OI 0
- **SPY** CALL 760 2026-11-04 (0DTE): 300 @ 8.15 = **+$244k** BUY | vol 7,776 / OI 3,836
- **MU** PUT 825 2026-11-04 (0DTE): 475 @ 4.75 = **+$226k** SELL | vol 4,635 / OI 526
- **MSFT** CALL 550 2026-11-06 (2DTE): 200 @ 9.50 = **+$190k** BUY | vol 3,288 / OI 3,993
- **SPY** CALL 751 2026-11-04 (0DTE): 100 @ 17.01 = **+$170k** BUY | vol 1,054 / OI 521
- **QQQ** CALL 685 2026-11-04 (0DTE): 110 @ 14.18 = **+$156k** SELL | vol 2,479 / OI 3,466
- **SPY** CALL 755 2026-11-06 (2DTE): 105 @ 14.22 = **+$149k** BUY | vol 856 / OI 3,719
- **NVDA** CALL 200 2026-11-06 (2DTE): 214 @ 6.75 = **+$144k** SELL | vol 1,740 / OI 1,991
- **SPY** CALL 756 2026-11-06 (2DTE): 105 @ 13.37 = **+$140k** BUY | vol 902 / OI 1,403
- **AAPL** CALL 350 2026-11-06 (2DTE): 250 @ 5.50 = **+$138k** SELL | vol 13,053 / OI 30,000

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 774 2026-11-04 (0DTE): 675 traded vs OI 6
- **SPY** CALL 759 2026-11-04 (0DTE): 2,179 traded vs OI 2,093
- **SPY** CALL 796 2026-11-09 (5DTE): 501 traded vs OI 0
- **SPY** CALL 771 2026-11-06 (2DTE): 2,374 traded vs OI 2,000
- **QQQ** CALL 719 2026-11-04 (0DTE): 824 traded vs OI 721
- **QQQ** PUT 705 2026-11-04 (0DTE): 534 traded vs OI 513
- **QQQ** CALL 713 2026-11-05 (1DTE): 550 traded vs OI 0
- **QQQ** PUT 679 2026-11-05 (1DTE): 528 traded vs OI 0
- **QQQ** PUT 664 2026-11-05 (1DTE): 574 traded vs OI 0
- **QQQ** PUT 703 2026-11-04 (0DTE): 872 traded vs OI 845
- **QQQ** CALL 710 2026-11-05 (1DTE): 4,819 traded vs OI 4,415
- **QQQ** PUT 681 2026-11-05 (1DTE): 627 traded vs OI 0
- **QQQ** PUT 640 2026-11-05 (1DTE): 525 traded vs OI 477
- **QQQ** PUT 697 2026-11-06 (2DTE): 750 traded vs OI 657
- **QQQ** CALL 714 2026-11-05 (1DTE): 566 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
