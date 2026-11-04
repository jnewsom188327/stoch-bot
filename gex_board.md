# GEX + FLOW SCAN - Wed Nov 04, 10:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (6)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:20 | **SMCI** | **CALLS** | FLOW SURGE | 11/06 33C | 0.65 | 0.48 | -3% (1m) | **-26%** | +39% | 32.81 |
| 10:20 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 284C | 0.49 | 0.40 | -2% (0m) | **-18%** | +131% | 284.74 |
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 1.36 | +100% (40m) | **+100%** | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.59 | +165% (50m) | **+165%** | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.04 | +2% (1m) | **-92%** | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.12 | -3% (1m) | **-81%** | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:40:08 ET, last candle SPY 10:39, QQQ 10:39 | no errors

## Flow surges NOT fired - price disagreed (25 today, last 5)
- 10:40 AAPL PUTS: price +1.07 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:35 GOOGL PUTS: over EMA 20 - flow says one way, price says the other
- 10:35 AAPL PUTS: price +0.85 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:30 AAPL PUTS: price +0.69 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:25 BABA PUTS: price +0.30 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 282.93 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 65 | 11/04 284C @ 0.40 (delta 0.30) = est +154% at 284.61 | NEG -$527.0M | 284.61 | 285 | 270 | +$16.6M | +$741k bull / +$0 bear | LONG (clean 34, ADX 26, RVol 1.1) |
| 2 | **BABA** | 106.83 | TREND (flow not with it) | **CALLS** | 65 | 11/06 110C @ 0.72 (delta 0.25) = est +27% at 107.96 | POS +$15.9M | - | 110 | 110 | -$910k | +$110k bull / +$0 bear | LONG (clean 36, ADX 62, RVol 2.9) |
| 3 | **GOOGL** | 292.61 | TREND (flow not with it) | **CALLS** | 57 | none: 92 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (39 contracts' greeks worked out here) | POS +$100.1M | 282.57 | 300 | 290 | -$29.2M | +$1.4M bull / -$1.3M bear | LONG (clean 35, ADX 59, RVol 1.6) |
| 4 | **TSLA** | 389.37 | FLOW SURGE | **PUTS** | 53 | none: 124 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (54 contracts' greeks worked out here) | NEG -$77.2M | 396.58 | 400 | 380 | -$78.0M | +$784k bull / -$3.7M bear | out (clean 30, ADX 24, RVol 2.9) |
| 5 | **AAPL** | 353.67 | FLOW SURGE | **PUTS** | 53 | 11/04 350P @ 0.61 (delta 0.21) = est +147% at 350 | POS +$1.0B | 341.37 | 355 | 350 | -$90.5M | +$472k bull / -$2.2M bear | out (clean 32, ADX 58, RVol 2.0) |
| 6 | **MU** | 822.75 | FLOW SURGE | **CALLS** | 49 | none: 136 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (61 contracts' greeks worked out here) | NEG -$335.0M | - | 840 | 800 | +$65.8M | +$4.6M bull / +$0 bear | out (clean 30, ADX 24, RVol 2.2) |
| 7 | **SMCI** | 31.64 | FLOW SURGE | **CALLS** | 45 | 11/06 32C @ 0.75 (delta 0.42) = est +53% at 32.56 | POS +$3.5M | - | 34.5 | 30 | +$1.5M | +$34k bull / +$0 bear | out (clean 33, ADX 24, RVol 1.9) |
| 8 | **COIN** | 151.63 | FLOW SURGE | **PUTS** | 44 | none: 20 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$28.0M | - | 148 | 150 | -$1.3M | +$31k bull / -$142k bear | out (clean 30, ADX 21, RVol 2.1) |
| 9 | **CRM** | 233.87 | FLOW SURGE | **PUTS** | 44 | none: 18 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$3.9M | 237.67 | 240 | 220 | -$306k | +$0 bull / -$104k bear | out (clean 31, ADX 61, RVol 1.0) |
| 10 | **ARM** | 198.38 | FLOW SURGE | **CALLS** | 42 | none: 16 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$7.3M | - | 212.5 | 200 | +$728k | +$27k bull / +$0 bear | out (clean 25, ADX 24, RVol 0.5) |
| 11 | **SHOP** | 148.63 | TREND (flow not with it) | **CALLS** | 31 | none: 22 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$9.7M | - | 160 | 135 | -$64k | - | LONG (clean 35, ADX 27, RVol 1.5) |
| 12 | **MSFT** | 554.84 | - | **-** | 30 | - | POS +$989.0M | - | 550 | 535 | -$18.9M | +$2.2M bull / -$208k bear | out (clean 29, ADX 67, RVol 2.2) |
| 13 | **AMZN** | 267.64 | - | **-** | 29 | - | POS +$547.1M | - | 270 | 250 | -$23.1M | +$2.0M bull / +$0 bear | out (clean 35, ADX 59, RVol 1.6) |
| 14 | **UBER** | 71.64 | - | **-** | 28 | - | POS +$11.8M | 67.88 | 70 | 70 | -$1.3M | - | out (clean 30, ADX 58, RVol 1.7) |
| 15 | **SMH** | 511.94 | - | **-** | 27 | - | NEG -$488.4M | - | 532.5 | 500 | +$2.5M | +$89k bull / +$0 bear | out (clean 31, ADX 26, RVol 1.5) |
| 16 | **QQQ** | 697.16 | - | **-** | 26 | - | NEG -$4.4B | 721.67 | 700 | 680 | -$160.1M | +$4.9M bull / +$0 bear | out (clean 30, ADX 37, RVol 1.4) |
| 17 | **SPY** | 767.16 | - | **-** | 25 | - | NEG -$3.1B | 770.27 | 770 | 750 | -$82.1M | +$1.4M bull / -$1.2M bear | out (clean 31, ADX 43, RVol 1.7) |
| 18 | **META** | 630.95 | - | **-** | 25 | - | POS +$154.4M | 619.62 | 650 | 625 | +$9.8M | +$4.0M bull / -$27k bear | out (clean 30, ADX 46, RVol 1.6) |
| 19 | **AMD** | 491.35 | - | **-** | 23 | - | NEG -$61.6M | - | 500 | 500 | +$31.0M | +$2.8M bull / -$107k bear | out (clean 32, ADX 23, RVol 1.3) |
| 20 | **MSTR** | 144.22 | - | **-** | 21 | - | POS +$118.3M | - | 135 | 150 | -$25k | +$648k bull / -$1.1M bear | out (clean 31, ADX 47, RVol 1.5) |
| 21 | **NVDA** | 204.76 | - | **-** | 20 | - | POS +$26.7M | 204.16 | 210 | 200 | +$1.3M | +$424k bull / -$31k bear | out (clean 29, ADX 34, RVol 1.7) |
| 22 | **NFLX** | 66.11 | - | **-** | 20 | - | POS +$18.7M | 62.71 | 65 | 65 | -$2.1M | - | out (clean 30, ADX 66, RVol 1.4) |
| 23 | **DELL** | 384.31 | - | **-** | 20 | - | NEG -$29.2M | - | 400 | 400 | +$443k | +$259k bull / -$418k bear | out (clean 32, ADX 32, RVol 1.2) |
| 24 | **PLTR** | 176.13 | - | **-** | 19 | - | NEG -$42.8M | - | 180 | 180 | -$2.8M | +$532k bull / -$705k bear | out (clean 26, ADX 15, RVol 1.1) |
| 25 | **HOOD** | 87.42 | - | **-** | 19 | - | POS +$2.0M | 85.46 | 90 | 90 | -$812k | +$92k bull / -$96k bear | out (clean 29, ADX 20, RVol 1.3) |
| 26 | **ORCL** | 127.06 | - | **-** | 18 | - | NEG -$28.8M | - | 130 | 125 | -$317k | +$32k bull / -$43k bear | out (clean 35, ADX 17, RVol 2.1) |
| 27 | **AVGO** | 329.25 | - | **-** | 15 | - | NEG -$84.1M | - | 340 | 330 | +$3.0M | - | out (clean 30, ADX 26, RVol 1.8) |

## Big prints this scan (145)
- **SPY** PUT 763 2026-11-11 (7DTE): 2,049 @ 4.47 = **+$916k** BUY | vol 4,286 / OI 0
- **QQQ** PUT 699 2026-11-04 (0DTE): 1,000 @ 3.04 = **+$304k** SELL | vol 32,268 / OI 132
- **QQQ** PUT 700 2026-11-04 (0DTE): 600 @ 4.36 = **+$262k** SELL | vol 33,460 / OI 3,668
- **DELL** PUT 400 2026-11-06 (2DTE): 150 @ 17.25 = **+$259k** SELL | vol 257 / OI 2,408
- **QQQ** PUT 699 2026-11-04 (0DTE): 716 @ 3.40 = **+$243k** SELL | vol 32,268 / OI 132
- **META** CALL 640 2026-11-06 (2DTE): 295 @ 7.01 = **+$207k** BUY | vol 5,220 / OI 6,825
- **TSLA** CALL 370 2026-11-06 (2DTE): 100 @ 20.15 = **+$202k** SELL | vol 2,650 / OI 1,724
- **GOOGL** CALL 290 2026-11-06 (2DTE): 300 @ 6.71 = **+$201k** BUY | vol 8,309 / OI 8,115
- **QQQ** CALL 701 2026-11-06 (2DTE): 400 @ 4.93 = **+$197k** BUY | vol 2,110 / OI 422
- **TSLA** CALL 385 2026-11-04 (0DTE): 353 @ 5.10 = **+$180k** SELL | vol 43,426 / OI 146
- **META** CALL 620 2026-11-04 (0DTE): 100 @ 17.07 = **+$171k** BUY | vol 901 / OI 931
- **META** CALL 632.5 2026-11-04 (0DTE): 300 @ 5.05 = **+$152k** BUY | vol 4,903 / OI 566
- **AMD** CALL 467.5 2026-11-09 (5DTE): 40 @ 36.80 = **+$147k** BUY | vol 299 / OI 76
- **QQQ** PUT 702 2026-11-05 (1DTE): 190 @ 7.23 = **+$137k** SELL | vol 503 / OI 0
- **QQQ** PUT 700 2026-11-04 (0DTE): 495 @ 2.77 = **+$137k** SELL | vol 33,460 / OI 3,668

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 738 2026-11-05 (1DTE): 979 traded vs OI 0
- **SPY** CALL 783 2026-11-05 (1DTE): 878 traded vs OI 0
- **SPY** CALL 777 2026-11-09 (5DTE): 500 traded vs OI 0
- **SPY** CALL 786 2026-11-10 (6DTE): 502 traded vs OI 0
- **SPY** PUT 745 2026-11-13 (9DTE): 73,098 traded vs OI 72,530
- **SPY** PUT 765 2026-11-13 (9DTE): 2,031 traded vs OI 1,843
- **SPY** PUT 765 2026-11-18 (14DTE): 510 traded vs OI 0
- **QQQ** PUT 702 2026-11-05 (1DTE): 503 traded vs OI 0
- **QQQ** PUT 700 2026-11-05 (1DTE): 2,330 traded vs OI 1,713
- **QQQ** PUT 701 2026-11-05 (1DTE): 515 traded vs OI 0
- **QQQ** CALL 698 2026-11-06 (2DTE): 1,106 traded vs OI 1,051
- **QQQ** CALL 718 2026-11-04 (0DTE): 1,743 traded vs OI 881
- **QQQ** PUT 685 2026-11-09 (5DTE): 1,067 traded vs OI 1,057
- **QQQ** CALL 721 2026-11-06 (2DTE): 1,032 traded vs OI 1,014
- **QQQ** PUT 679 2026-11-06 (2DTE): 554 traded vs OI 532

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
