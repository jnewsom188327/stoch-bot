# GEX + FLOW SCAN - Wed Nov 04, 10:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (6)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:20 | **SMCI** | **CALLS** | FLOW SURGE | 11/06 33C | 0.65 | 0.61 | -3% (1m) | **-6%** | +39% | 32.81 |
| 10:20 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 284C | 0.49 | 0.16 | -2% (0m) | **-67%** | +131% | 284.74 |
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 0.89 | +65% (22m) | **+31%** | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.33 | +128% (31m) | **+122%** | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.05 | +2% (1m) | **-91%** | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.15 | -3% (1m) | **-76%** | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:30:08 ET, last candle SPY 10:29, QQQ 10:29 | no errors

## Flow surges NOT fired - price disagreed (22 today, last 5)
- 10:30 AAPL PUTS: price +0.69 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:25 BABA PUTS: price +0.30 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:25 UBER PUTS: price +0.08 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:20 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 10:20 UBER PUTS: price +0.28 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BABA** | 106.65 | TREND (flow not with it) | **CALLS** | 67 | 11/06 110C @ 0.66 (delta 0.24) = est +36% at 107.8 | POS +$16.2M | - | 110 | 110 | -$989k | +$54k bull / +$0 bear | LONG (clean 36, ADX 60, RVol 3.7) |
| 2 | **AMZN** | 269.04 | TREND (flow not with it) | **CALLS** | 56 | none: 88 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (41 contracts' greeks worked out here) | POS +$547.3M | - | 270 | 250 | -$28.6M | +$1.3M bull / +$0 bear | LONG (clean 35, ADX 59, RVol 1.9) |
| 3 | **AAPL** | 353.72 | FLOW SURGE | **PUTS** | 54 | 11/04 350P @ 0.66 (delta 0.22) = est +148% at 350 | POS +$999.3M | 341.31 | 355 | 350 | -$87.0M | +$822k bull / -$3.2M bear | out (clean 32, ADX 54, RVol 2.2) |
| 4 | **GOOGL** | 294.83 | FLOW SURGE | **PUTS** | 54 | none: 92 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (39 contracts' greeks worked out here) | POS +$109.0M | 282.67 | 300 | 290 | -$32.7M | +$306k bull / -$2.3M bear | LONG (clean 35, ADX 61, RVol 1.5) |
| 5 | **TSLA** | 388.84 | FLOW SURGE | **PUTS** | 51 | none: 128 puts 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (57 contracts' greeks worked out here) | NEG -$92.1M | 396.98 | 400 | 380 | -$72.6M | +$0 bull / -$3.7M bear | out (clean 30, ADX 27, RVol 2.4) |
| 6 | **COIN** | 152.24 | FLOW SURGE | **PUTS** | 48 | none: 19 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$28.3M | - | 148 | 150 | -$1.4M | +$0 bull / -$142k bear | out (clean 30, ADX 21, RVol 2.3) |
| 7 | **MU** | 824.98 | FLOW SURGE | **CALLS** | 46 | none: 136 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (58 contracts' greeks worked out here) | NEG -$332.8M | - | 840 | 800 | +$52.1M | +$4.1M bull / +$0 bear | out (clean 30, ADX 22, RVol 1.9) |
| 8 | **IWM** | 281.98 | FLOW SURGE | **CALLS** | 45 | 11/04 282C @ 0.80 (delta 0.50) = est +230% at 284.6 | NEG -$837.0M | 284.6 | 285 | 270 | +$17.9M | +$597k bull / +$0 bear | out (clean 34, ADX 29, RVol 1.2) |
| 9 | **SHOP** | 149.01 | TREND (flow not with it) | **CALLS** | 42 | none: 21 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$9.4M | - | 160 | 135 | -$147k | - | LONG (clean 35, ADX 29, RVol 1.9) |
| 10 | **MSFT** | 552.56 | - | **-** | 31 | - | POS +$1.0B | - | 550 | 535 | -$19.2M | +$2.8M bull / -$111k bear | out (clean 29, ADX 65, RVol 3.3) |
| 11 | **QQQ** | 697.68 | - | **-** | 28 | - | NEG -$4.3B | 720.38 | 700 | 680 | -$166.9M | +$2.2M bull / -$749k bear | out (clean 30, ADX 38, RVol 1.6) |
| 12 | **UBER** | 71.23 | - | **-** | 28 | - | POS +$10.8M | 68.14 | 70 | 65 | -$1.1M | - | out (clean 30, ADX 54, RVol 2.2) |
| 13 | **SMH** | 512.84 | - | **-** | 27 | - | NEG -$474.4M | - | 532.5 | 500 | +$2.0M | +$91k bull / +$0 bear | out (clean 31, ADX 24, RVol 1.8) |
| 14 | **SPY** | 766.55 | - | **-** | 25 | - | NEG -$3.7B | 770.22 | 770 | 750 | -$65.2M | +$2.5M bull / -$212k bear | out (clean 31, ADX 44, RVol 1.9) |
| 15 | **AMD** | 494.20 | - | **-** | 25 | - | NEG -$56.2M | - | 500 | 500 | +$31.0M | +$2.0M bull / -$389k bear | out (clean 32, ADX 26, RVol 1.8) |
| 16 | **META** | 632.01 | - | **-** | 25 | - | POS +$163.8M | 619.91 | 650 | 625 | +$7.6M | +$2.6M bull / -$158k bear | out (clean 30, ADX 50, RVol 1.7) |
| 17 | **AVGO** | 329.08 | - | **-** | 25 | - | NEG -$83.2M | 348.55 | 340 | 330 | +$2.6M | +$28k bull / +$0 bear | out (clean 30, ADX 24, RVol 2.1) |
| 18 | **PLTR** | 176.55 | - | **-** | 23 | - | NEG -$43.0M | - | 180 | 180 | -$4.0M | +$0 bull / -$736k bear | out (clean 25, ADX 18, RVol 1.3) |
| 19 | **HOOD** | 87.83 | - | **-** | 23 | - | POS +$2.7M | 84.63 | 90 | 90 | -$1.7M | +$0 bull / -$179k bear | out (clean 28, ADX 20, RVol 1.3) |
| 20 | **DELL** | 387.80 | - | **-** | 21 | - | NEG -$29.4M | - | 400 | 400 | -$599k | +$0 bull / -$461k bear | out (clean 33, ADX 32, RVol 1.4) |
| 21 | **SMCI** | 32.01 | - | **-** | 21 | - | POS +$6.7M | - | 34.5 | 30 | +$1.3M | - | out (clean 33, ADX 21, RVol 2.1) |
| 22 | **MSTR** | 143.79 | - | **-** | 21 | - | POS +$119.1M | - | 135 | 150 | -$51k | +$201k bull / -$890k bear | out (clean 31, ADX 46, RVol 1.5) |
| 23 | **ARM** | 200.72 | - | **-** | 21 | - | NEG -$6.2M | - | 212.5 | 200 | +$552k | - | out (clean 26, ADX 22, RVol 0.5) |
| 24 | **NVDA** | 204.71 | - | **-** | 20 | - | POS +$20.5M | 204.14 | 210 | 200 | +$2.2M | +$507k bull / -$206k bear | out (clean 29, ADX 33, RVol 1.6) |
| 25 | **NFLX** | 65.98 | - | **-** | 20 | - | POS +$19.3M | 62.35 | 65 | 65 | -$1.9M | - | out (clean 30, ADX 64, RVol 1.5) |
| 26 | **CRM** | 234.16 | - | **-** | 16 | - | NEG -$3.7M | 237.49 | 240 | 220 | -$97k | - | out (clean 31, ADX 57, RVol 1.1) |
| 27 | **ORCL** | 126.97 | - | **-** | 9 | - | NEG -$28.9M | - | 130 | 125 | -$205k | - | out (clean 35, ADX 19, RVol 2.5) |

## Big prints this scan (160)
- **MSFT** PUT 545 2026-11-06 (2DTE): 2,000 @ 2.56 = **+$512k** SELL | vol 4,455 / OI 197
- **MSFT** PUT 540 2026-11-06 (2DTE): 2,000 @ 1.52 = **+$304k** SELL | vol 3,126 / OI 621
- **MSFT** CALL 525 2026-11-06 (2DTE): 99 @ 28.50 = **+$282k** MID | vol 481 / OI 3,666
- **MSFT** PUT 552.5 2026-11-06 (2DTE): 400 @ 5.55 = **+$222k** SELL | vol 978 / OI 0
- **QQQ** PUT 685 2026-11-04 (0DTE): 7,500 @ 0.29 = **+$218k** SELL | vol 38,609 / OI 10,888
- **QQQ** CALL 703 2026-11-06 (2DTE): 400 @ 5.42 = **+$217k** BUY | vol 1,303 / OI 987
- **AMZN** PUT 277.5 2026-11-04 (0DTE): 250 @ 8.00 = **+$200k** SELL | vol 519 / OI 0
- **QQQ** CALL 690 2026-11-04 (0DTE): 180 @ 11.00 = **+$198k** BUY | vol 22,579 / OI 3,346
- **QQQ** CALL 697 2026-11-04 (0DTE): 499 @ 3.84 = **+$192k** BUY | vol 45,889 / OI 930
- **QQQ** PUT 699 2026-11-04 (0DTE): 679 @ 2.47 = **+$168k** SELL | vol 19,089 / OI 132
- **QQQ** CALL 689 2026-11-04 (0DTE): 150 @ 10.36 = **+$155k** BUY | vol 7,904 / OI 616
- **AMD** CALL 472.5 2026-11-04 (0DTE): 57 @ 27.10 = **+$154k** BUY | vol 155 / OI 89
- **META** CALL 620 2026-11-04 (0DTE): 90 @ 17.14 = **+$154k** BUY | vol 772 / OI 931
- **COIN** PUT 157.5 2026-11-06 (2DTE): 166 @ 8.55 = **+$142k** BUY | vol 187 / OI 111
- **AMD** CALL 475 2026-11-04 (0DTE): 57 @ 24.77 = **+$141k** BUY | vol 286 / OI 205

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 771 2026-11-09 (5DTE): 645 traded vs OI 0
- **SPY** PUT 762 2026-11-09 (5DTE): 500 traded vs OI 0
- **SPY** PUT 766 2026-11-09 (5DTE): 500 traded vs OI 0
- **SPY** PUT 770 2026-11-16 (12DTE): 531 traded vs OI 29
- **SPY** PUT 767 2026-11-10 (6DTE): 513 traded vs OI 0
- **QQQ** CALL 703 2026-11-06 (2DTE): 1,303 traded vs OI 987
- **QQQ** PUT 704 2026-11-04 (0DTE): 699 traded vs OI 286
- **QQQ** PUT 678 2026-11-05 (1DTE): 529 traded vs OI 0
- **QQQ** CALL 720 2026-11-09 (5DTE): 1,607 traded vs OI 1,486
- **QQQ** PUT 676 2026-11-05 (1DTE): 549 traded vs OI 0
- **QQQ** PUT 698 2026-11-06 (2DTE): 764 traded vs OI 708
- **QQQ** PUT 672 2026-11-05 (1DTE): 592 traded vs OI 0
- **QQQ** CALL 704 2026-11-06 (2DTE): 734 traded vs OI 729
- **QQQ** CALL 742 2026-11-04 (0DTE): 700 traded vs OI 148
- **IWM** CALL 282 2026-11-04 (0DTE): 1,602 traded vs OI 1,362

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
