# GEX + FLOW SCAN - Thu Nov 12, 10:35 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:35 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 754P | 0.59 | 0.58 | -2% (0m) | **-2%** | +70% | 755 |
| 09:50 | **HOOD** | **PUTS** | TREND + FLOW | 11/13 79P | 0.55 | 0.40 | +5% (19m) | **-27%** | +92% | 80 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 130C | 0.75 | 0.55 | -1% (8m) | **-27%** | +59% | 126.9 |
| 09:45 | **SMCI** | **PUTS** | TREND + FLOW | 11/13 27P | 0.42 | 0.32 | -5% (6m) | **-24%** | +57% | 27 |
| 09:45 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 753P | 0.79 | 0.52 | +23% (18m) | **-34%** | +51% | 754.88 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:35:08 ET, last candle SPY 10:34, QQQ 10:34 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:03 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (3 today, last 5)
- 10:30 IWM CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:25 IWM CALLS: price -0.79 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:20 IWM CALLS: price -0.12 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NVDA** | 163.21 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 78 | none: 45 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | NEG -$187.2M | - | 170 | 160 | -$112.1M | +$1.6M bull / -$8.3M bear | SHORT (clean 33, ADX 40, RVol 2.5) |
| 2 | **SPY** | 757.11 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 48 | 11/12 754P @ 0.59 (delta 0.23) = est +70% at 755 | NEG -$2.7B | 760.76 | 760 | 760 | -$2.1M | +$0 bull / -$1.3M bear | SHORT (clean 32, ADX 28, RVol 0.5) |
| 3 | **IWM** | 279.47 | TREND (flow not with it) | **PUTS** | 46 | none: 326 puts 0-7DTE > 20 priced 0.40-0.80 > 6 delta 0.2+ > 6 spread ok > 6 liquid > best one only +17% at the target (needs +20%) (146 contracts' greeks worked out here) | NEG -$1.2B | 282.7 | 285 | 275 | +$7.8M | +$0 bull / -$74k bear | SHORT (clean 35, ADX 56, RVol 0.9) |
| 4 | **DELL** | 355.03 | TREND + FLOW | **PUTS** | 45 | none: 29 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$1.7M | 350.74 | 360 | 340 | -$733k | +$0 bull / -$312k bear | SHORT (clean 37, ADX 37, RVol 1.2) |
| 5 | **MU** | 773.66 | TREND (flow not with it) | **PUTS** | 44 | none: 131 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$84.8M | - | 800 | 750 | +$39.7M | +$1.1M bull / -$12.4M bear | SHORT (clean 32, ADX 43, RVol 1.1) |
| 6 | **SMCI** | 27.90 | TREND + FLOW | **PUTS** | 40 | 11/13 28P @ 0.70 (delta 0.50) = est +68% at 27 | POS +$2.9M | - | 30 | 27 | -$69k | - | SHORT (clean 34, ADX 50, RVol 1.6) |
| 7 | **AMZN** | 269.43 | PINNED between the walls (positive gamma) - chop | **-** | 35 | - | POS +$495.8M | - | 270 | 270 | -$4.8M | +$308k bull / +$0 bear | out (clean 31, ADX 32, RVol 0.8) |
| 8 | **AMD** | 560.33 | - | **-** | 25 | - | POS +$163.1M | - | 600 | 550 | +$31.2M | +$2.0M bull / -$1.7M bear | out (clean 34, ADX 24, RVol 1.7) |
| 9 | **AVGO** | 361.63 | - | **-** | 25 | - | POS +$132.2M | - | 350 | 350 | +$3.3M | +$849k bull / -$52k bear | out (clean 36, ADX 40, RVol 2.6) |
| 10 | **SMH** | 496.33 | - | **-** | 24 | - | NEG -$135.4M | - | 500 | 475 | -$1.0M | +$0 bull / -$90k bear | out (clean 31, ADX 44, RVol 1.4) |
| 11 | **MSFT** | 524.78 | - | **-** | 23 | - | POS +$131.0M | 519.26 | 535 | 520 | -$3.7M | +$60k bull / -$63k bear | out (clean 31, ADX 34, RVol 0.5) |
| 12 | **ORCL** | 125.36 | - | **-** | 23 | - | POS +$9.3M | 120.15 | 130 | 125 | -$551k | +$0 bull / -$30k bear | out (clean 29, ADX 31, RVol 0.8) |
| 13 | **META** | 620.56 | - | **-** | 22 | - | NEG -$25.8M | 624.31 | 650 | 600 | +$1.5M | +$0 bull / -$183k bear | out (clean 29, ADX 57, RVol 0.7) |
| 14 | **TSLA** | 390.27 | - | **-** | 20 | - | POS +$348.8M | - | 400 | 380 | +$12.9M | +$461k bull / -$26k bear | out (clean 29, ADX 27, RVol 0.6) |
| 15 | **AAPL** | 357.63 | - | **-** | 20 | - | POS +$1.1B | 338.4 | 360 | 360 | +$156k | +$242k bull / -$53k bear | out (clean 29, ADX 44, RVol 1.1) |
| 16 | **PLTR** | 169.28 | - | **-** | 20 | - | POS +$83.3M | - | 170 | 170 | -$117k | +$0 bull / -$60k bear | out (clean 28, ADX 41, RVol 0.8) |
| 17 | **COIN** | 130.02 | - | **-** | 20 | - | NEG -$2.6M | 130.89 | 137 | 130 | +$277k | - | out (clean 30, ADX 46, RVol 1.1) |
| 18 | **ARM** | 198.11 | - | **-** | 20 | - | POS +$9.1M | - | 200 | 200 | -$77k | +$0 bull / -$100k bear | out (clean 31, ADX 34, RVol 0.7) |
| 19 | **BABA** | 94.68 | - | **-** | 20 | - | NEG -$15.7M | - | 100 | 95 | +$204k | - | out (clean 29, ADX 55, RVol 3.6) |
| 20 | **QQQ** | 684.94 | - | **-** | 18 | - | NEG -$772.8M | 689.81 | 700 | 680 | -$215k | +$0 bull / -$1.1M bear | out (clean 31, ADX 36, RVol 0.8) |
| 21 | **GOOGL** | 295.31 | - | **-** | 18 | - | POS +$107.3M | 288.4 | 300 | 290 | +$504k | +$0 bull / -$55k bear | out (clean 29, ADX 22, RVol 1.6) |
| 22 | **MSTR** | 114.32 | - | **-** | 16 | - | NEG -$32.2M | - | 125 | 110 | -$1.7M | - | out (clean 27, ADX 38, RVol 1.1) |
| 23 | **NFLX** | 63.36 | - | **-** | 15 | - | NEG -$12.5M | 64.05 | 65 | 65 | -$219k | - | out (clean 27, ADX 40, RVol 0.8) |
| 24 | **SHOP** | 147.75 | - | **-** | 11 | - | POS +$4.7M | 142.99 | 150 | 140 | -$2k | - | out (clean 30, ADX 26, RVol 1.1) |
| 25 | **HOOD** | 81.92 | - | **-** | 9 | - | POS +$8.1M | 80.06 | 85 | 80 | +$51k | - | out (clean 34, ADX 32, RVol 0.9) |
| 26 | **UBER** | 69.55 | - | **-** | 8 | - | POS +$13.1M | 68.24 | 70 | 70 | +$1k | - | out (clean 31, ADX 35, RVol 0.8) |
| 27 | **CRM** | 214.93 | - | **-** | 6 | - | NEG -$8.7M | - | 220 | 220 | -$4k | - | out (clean 28, ADX 28, RVol 0.5) |

## Big prints this scan (154)
- **MU** CALL 780 2026-11-13 (1DTE): 190 @ 15.50 = **+$294k** BUY | vol 5,577 / OI 1,424
- **MU** CALL 770 2026-11-13 (1DTE): 154 @ 17.71 = **+$273k** SELL | vol 4,922 / OI 1,263
- **MU** CALL 780 2026-11-13 (1DTE): 200 @ 13.00 = **+$260k** SELL | vol 5,577 / OI 1,424
- **NVDA** PUT 162.5 2026-11-13 (1DTE): 634 @ 3.50 = **+$222k** BUY | vol 19,990 / OI 20,581
- **MU** PUT 765 2026-11-18 (6DTE): 70 @ 28.13 = **+$197k** BUY | vol 265 / OI 15
- **MU** CALL 770 2026-11-13 (1DTE): 100 @ 18.15 = **+$182k** SELL | vol 4,922 / OI 1,263
- **SPY** PUT 758 2026-11-17 (5DTE): 300 @ 5.42 = **+$163k** BUY | vol 792 / OI 129
- **NVDA** CALL 160 2026-11-13 (1DTE): 271 @ 5.67 = **+$154k** SELL | vol 108,054 / OI 2,015
- **MU** CALL 800 2026-11-13 (1DTE): 200 @ 7.65 = **+$153k** BUY | vol 10,439 / OI 5,964
- **NVDA** PUT 165 2026-11-16 (4DTE): 252 @ 5.55 = **+$140k** SELL | vol 3,549 / OI 2,280
- **NVDA** CALL 160 2026-11-13 (1DTE): 231 @ 6.00 = **+$139k** BUY | vol 108,054 / OI 2,015
- **NVDA** PUT 170 2026-11-16 (4DTE): 147 @ 9.07 = **+$133k** BUY | vol 2,734 / OI 3,775
- **NVDA** PUT 170 2026-11-16 (4DTE): 150 @ 8.65 = **+$130k** SELL | vol 2,734 / OI 3,775
- **NVDA** PUT 170 2026-11-16 (4DTE): 150 @ 8.65 = **+$130k** SELL | vol 2,734 / OI 3,775
- **NVDA** PUT 160 2026-11-13 (1DTE): 500 @ 2.58 = **+$129k** BUY | vol 80,471 / OI 24,121

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 744 2026-11-12 (0DTE): 17,135 traded vs OI 13,012
- **SPY** CALL 762 2026-11-13 (1DTE): 7,594 traded vs OI 7,472
- **SPY** CALL 783 2026-11-16 (4DTE): 1,155 traded vs OI 684
- **SPY** CALL 805 2026-11-16 (4DTE): 1,512 traded vs OI 218
- **SPY** PUT 755 2026-11-13 (1DTE): 10,290 traded vs OI 9,753
- **SPY** PUT 755 2026-11-23 (11DTE): 595 traded vs OI 94
- **QQQ** PUT 642 2026-11-12 (0DTE): 545 traded vs OI 329
- **QQQ** CALL 690 2026-11-13 (1DTE): 10,281 traded vs OI 9,862
- **QQQ** PUT 686 2026-11-17 (5DTE): 519 traded vs OI 50
- **QQQ** PUT 656 2026-11-12 (0DTE): 1,117 traded vs OI 1,038
- **QQQ** PUT 681 2026-11-13 (1DTE): 1,729 traded vs OI 1,683
- **QQQ** CALL 693 2026-11-13 (1DTE): 1,650 traded vs OI 1,589
- **IWM** CALL 291 2026-11-16 (4DTE): 529 traded vs OI 296
- **IWM** PUT 279 2026-11-18 (6DTE): 637 traded vs OI 185
- **IWM** CALL 279 2026-11-12 (0DTE): 2,378 traded vs OI 2,134

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
