# GEX + FLOW SCAN - Tue Nov 10, 11:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 1.79 | +232% (36m) | **+184%** | +22% | 280 hit |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.62 | +21% (60m) | **-19%** (done) | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.95 | +90% (60m) | **+83%** (done) | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:00:08 ET, last candle SPY 10:59, QQQ 10:59 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 10:15 BABA PUTS: price +0.24 over the last 15 min - flow says one way, price says the other
- 10:10 BABA PUTS: price +0.73 over the last 15 min - flow says one way, price says the other
- 10:00 NFLX CALLS: price -0.14 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AAPL CALLS: price -2.97 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 BABA CALLS: price -0.98 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AMZN** | 269.81 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 38 | none: 63 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (12 contracts' greeks worked out here) | POS +$472.3M | - | 270 | 265 | +$5.5M | +$318k bull / +$0 bear | out (clean 32, ADX 27, RVol 0.6) |
| 2 | **IWM** | 278.45 | TREND (flow not with it) | **PUTS** | 34 | 11/10 278P @ 0.49 (delta 0.39) = est +143% at 276.96 | NEG -$1.3B | 283.61 | 280 | 270 | +$5.8M | - | SHORT (clean 36, ADX 47, RVol 1.1) |
| 3 | **AAPL** | 347.13 | - | **-** | 27 | - | POS +$403.7M | 335.81 | 350 | 340 | +$17.8M | +$107k bull / -$207k bear | out (clean 28, ADX 18, RVol 0.7) |
| 4 | **NVDA** | 168.60 | - | **-** | 24 | - | NEG -$171.8M | - | 185 | 170 | +$16.6M | +$2.2M bull / +$0 bear | out (clean 32, ADX 36, RVol 2.4) |
| 5 | **AMD** | 522.04 | - | **-** | 24 | - | POS +$43.2M | - | 500 | 500 | -$61.4M | +$4.3M bull / +$0 bear | out (clean 31, ADX 28, RVol 1.2) |
| 6 | **UBER** | 69.97 | PINNED between the walls (positive gamma) - chop | **-** | 22 | - | POS +$8.5M | 68.42 | 70 | 70 | -$14k | - | out (clean 33, ADX 40, RVol 0.5) |
| 7 | **AVGO** | 327.02 | - | **-** | 21 | - | NEG -$13.9M | 342.8 | 340 | 320 | -$8.5M | +$361k bull / +$0 bear | out (clean 31, ADX 27, RVol 1.0) |
| 8 | **ARM** | 179.10 | - | **-** | 21 | - | NEG -$4.5M | - | 185 | 190 | -$64k | +$35k bull / +$0 bear | out (clean 27, ADX 30, RVol 1.0) |
| 9 | **SPY** | 746.94 | - | **-** | 20 | - | NEG -$7.4B | 760.15 | 750 | 730 | +$51.8M | +$11.6M bull / +$0 bear | out (clean 32, ADX 33, RVol 1.1) |
| 10 | **MSTR** | 120.42 | - | **-** | 20 | - | NEG -$20.0M | - | 132 | 110 | -$468k | +$366k bull / -$444k bear | out (clean 29, ADX 31, RVol 1.8) |
| 11 | **GOOGL** | 287.68 | - | **-** | 19 | - | NEG -$7.1M | 289.19 | 300 | 290 | +$1.7M | +$28k bull / +$0 bear | out (clean 30, ADX 16, RVol 0.7) |
| 12 | **DELL** | 330.88 | - | **-** | 19 | - | NEG -$11.0M | - | 350 | 340 | +$419k | +$149k bull / +$0 bear | out (clean 32, ADX 29, RVol 1.1) |
| 13 | **ORCL** | 118.32 | - | **-** | 19 | - | NEG -$22.7M | - | 130 | 120 | +$310k | +$136k bull / +$0 bear | out (clean 28, ADX 29, RVol 0.2) |
| 14 | **TSLA** | 376.89 | - | **-** | 18 | - | POS +$194.0M | - | 400 | 380 | -$5.6M | +$698k bull / -$207k bear | out (clean 34, ADX 33, RVol 0.4) |
| 15 | **QQQ** | 672.68 | - | **-** | 16 | - | NEG -$1.9B | 692.19 | 680 | 680 | +$7.6M | +$4.0M bull / +$0 bear | out (clean 31, ADX 25, RVol 0.6) |
| 16 | **SMH** | 480.49 | - | **-** | 16 | - | NEG -$217.2M | - | 500 | 475 | +$334k | +$58k bull / +$0 bear | out (clean 29, ADX 21, RVol 0.7) |
| 17 | **MU** | 708.49 | - | **-** | 16 | - | NEG -$27.6M | - | 750 | 750 | +$2.0M | +$5.0M bull / +$0 bear | out (clean 30, ADX 23, RVol 0.8) |
| 18 | **HOOD** | 80.97 | - | **-** | 16 | - | POS +$2.5M | 79.36 | 85 | 80 | +$691k | - | out (clean 30, ADX 36, RVol 0.6) |
| 19 | **CRM** | 212.65 | - | **-** | 16 | - | NEG -$10.5M | - | 195 | 220 | -$87k | - | out (clean 30, ADX 36, RVol 0.2) |
| 20 | **META** | 641.79 | - | **-** | 14 | - | POS +$255.6M | 603.71 | 650 | 650 | -$6k | +$336k bull / +$0 bear | out (clean 32, ADX 20, RVol 0.4) |
| 21 | **COIN** | 130.62 | - | **-** | 14 | - | POS +$1.9M | 129.41 | 137 | 135 | +$359k | - | out (clean 30, ADX 33, RVol 0.8) |
| 22 | **SHOP** | 148.62 | - | **-** | 14 | - | POS +$2.3M | 144.24 | 150 | 140 | +$15k | - | out (clean 31, ADX 38, RVol 0.5) |
| 23 | **BABA** | 103.51 | - | **-** | 14 | - | NEG -$6.0M | 106.01 | 110 | 100 | -$369k | - | out (clean 29, ADX 34, RVol 0.3) |
| 24 | **PLTR** | 167.06 | - | **-** | 11 | - | POS +$54.1M | - | 165 | 170 | -$254k | - | out (clean 28, ADX 48, RVol 0.9) |
| 25 | **MSFT** | 542.24 | - | **-** | 9 | - | POS +$688.3M | - | 550 | 535 | -$112k | - | out (clean 32, ADX 36, RVol 0.8) |
| 26 | **NFLX** | 62.78 | - | **-** | 8 | - | NEG -$22.9M | 65.3 | 65 | 60 | -$137k | - | out (clean 30, ADX 29, RVol 0.6) |
| 27 | **SMCI** | 27.90 | - | **-** | 7 | - | POS +$3.2M | - | 30 | 30 | +$44k | - | out (clean 28, ADX 23, RVol 0.6) |

## Big prints this scan (78)
- **SPY** PUT 760 2026-11-13 (3DTE): 2,000 @ 11.95 = **+$2.4M** SELL | vol 31,316 / OI 5,844
- **SPY** PUT 760 2026-11-13 (3DTE): 1,792 @ 12.01 = **+$2.2M** SELL | vol 31,316 / OI 5,844
- **MSTR** PUT 123 2026-11-13 (3DTE): 814 @ 5.45 = **+$444k** BUY | vol 3,139 / OI 2,696
- **SPY** PUT 760 2026-11-13 (3DTE): 246 @ 12.06 = **+$297k** SELL | vol 31,316 / OI 5,844
- **SPY** PUT 752 2026-11-10 (0DTE): 500 @ 3.52 = **+$176k** SELL | vol 28,172 / OI 210
- **QQQ** CALL 675 2026-11-10 (0DTE): 500 @ 2.85 = **+$142k** BUY | vol 58,162 / OI 1,728
- **QQQ** PUT 673 2026-11-13 (3DTE): 198 @ 6.69 = **+$132k** SELL | vol 1,534 / OI 173
- **AVGO** PUT 322.5 2026-11-11 (1DTE): 530 @ 2.40 = **+$127k** SELL | vol 1,738 / OI 27
- **QQQ** PUT 675 2026-11-10 (0DTE): 500 @ 2.30 = **+$115k** SELL | vol 103,591 / OI 718
- **SPY** PUT 750 2026-11-13 (3DTE): 200 @ 5.73 = **+$115k** SELL | vol 6,087 / OI 5,505
- **QQQ** PUT 679 2026-11-10 (0DTE): 200 @ 5.10 = **+$102k** SELL | vol 39,801 / OI 91
- **QQQ** CALL 675 2026-11-10 (0DTE): 350 @ 2.90 = **+$102k** BUY | vol 58,162 / OI 1,728
- **QQQ** PUT 680 2026-11-13 (3DTE): 100 @ 10.14 = **+$101k** SELL | vol 2,128 / OI 4,593
- **MSTR** PUT 123 2026-11-13 (3DTE): 191 @ 5.15 = **+$98k** SELL | vol 3,139 / OI 2,696
- **NVDA** CALL 165 2026-11-16 (6DTE): 100 @ 8.40 = **+$84k** BUY | vol 564 / OI 17

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 700 2026-11-10 (0DTE): 2,236 traded vs OI 2,218
- **SPY** PUT 762 2026-11-10 (0DTE): 516 traded vs OI 0
- **SPY** PUT 737 2026-11-12 (2DTE): 506 traded vs OI 374
- **SPY** CALL 765 2026-11-16 (6DTE): 660 traded vs OI 656
- **SPY** PUT 746 2026-11-12 (2DTE): 527 traded vs OI 277
- **SPY** PUT 709 2026-11-12 (2DTE): 784 traded vs OI 404
- **SPY** PUT 708 2026-11-11 (1DTE): 592 traded vs OI 404
- **SPY** PUT 753 2026-11-12 (2DTE): 527 traded vs OI 197
- **SPY** CALL 749 2026-11-16 (6DTE): 509 traded vs OI 308
- **SPY** CALL 769 2026-11-10 (0DTE): 1,814 traded vs OI 1,481
- **SPY** PUT 740 2026-11-17 (7DTE): 525 traded vs OI 455
- **SPY** CALL 811 2026-11-20 (10DTE): 2,435 traded vs OI 725
- **SPY** PUT 749 2026-11-16 (6DTE): 529 traded vs OI 186
- **SPY** PUT 748 2026-11-17 (7DTE): 536 traded vs OI 81
- **QQQ** PUT 652 2026-11-11 (1DTE): 526 traded vs OI 233

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
