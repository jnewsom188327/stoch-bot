# GEX + FLOW SCAN - Thu Nov 12, 10:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:50 | **HOOD** | **PUTS** | TREND + FLOW | 11/13 79P | 0.55 | 0.46 | +5% (19m) | **-16%** | +92% | 80 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 130C | 0.75 | 0.58 | -1% (8m) | **-23%** | +59% | 126.9 |
| 09:45 | **SMCI** | **PUTS** | TREND + FLOW | 11/13 27P | 0.42 | 0.21 | -5% (6m) | **-50%** | +57% | 27 |
| 09:45 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 753P | 0.79 | 0.65 | +23% (18m) | **-18%** | +51% | 754.88 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:20:08 ET, last candle SPY 10:19, QQQ 10:19 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:03 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (1 today, last 5)
- 10:20 IWM CALLS: price -0.12 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NVDA** | 163.64 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 80 | none: 45 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$184.9M | - | 170 | 160 | -$95.1M | +$6.8M bull / -$8.8M bear | SHORT (clean 33, ADX 44, RVol 2.7) |
| 2 | **IWM** | 279.34 | FLOW SURGE | **CALLS** | 51 | 11/12 279C @ 0.76 (delta 0.60) = est +101% at 280.5 | NEG -$1.4B | 282.79 | 285 | 275 | +$8.4M | +$126k bull / +$0 bear | SHORT (clean 35, ADX 51, RVol 1.3) |
| 3 | **DELL** | 357.53 | TREND + FLOW | **PUTS** | 47 | none: 29 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$2.3M | 347.9 | 360 | 340 | -$794k | +$37k bull / +$0 bear | SHORT (clean 37, ADX 38, RVol 2.4) |
| 4 | **MU** | 777.67 | FLOW SURGE | **CALLS** | 47 | none: 131 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | POS +$78.7M | - | 800 | 800 | +$58.7M | +$5.7M bull / -$1.5M bear | SHORT (clean 32, ADX 42, RVol 1.5) |
| 5 | **META** | 621.15 | FLOW SURGE | **CALLS** | 42 | none: 150 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (13 contracts' greeks worked out here) | NEG -$33.1M | 624.09 | 650 | 600 | +$5.4M | +$571k bull / +$0 bear | out (clean 30, ADX 56, RVol 0.8) |
| 6 | **SMCI** | 28.32 | TREND + FLOW | **PUTS** | 42 | 11/13 27.5P @ 0.44 (delta 0.35) = est +123% at 27 | POS +$3.2M | - | 30 | 27 | -$83k | - | SHORT (clean 34, ADX 51, RVol 1.7) |
| 7 | **AMZN** | 269.87 | PINNED between the walls (positive gamma) - chop | **-** | 41 | - | POS +$493.0M | - | 270 | 270 | -$6.1M | +$900k bull / +$0 bear | out (clean 32, ADX 37, RVol 1.2) |
| 8 | **AVGO** | 364.20 | TREND (flow not with it) | **CALLS** | 41 | none: 81 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | POS +$129.5M | - | 350 | 350 | -$364k | +$182k bull / -$1.3M bear | LONG (clean 36, ADX 43, RVol 2.4) |
| 9 | **AMD** | 563.07 | - | **-** | 29 | - | POS +$158.4M | - | 600 | 550 | +$32.4M | +$3.7M bull / -$26k bear | out (clean 35, ADX 28, RVol 2.4) |
| 10 | **HOOD** | 81.97 | TREND (flow not with it) | **PUTS** | 27 | 11/13 79P @ 0.52 (delta 0.22) = est +85% at 80.07 | POS +$6.4M | 80.07 | 85 | 80 | +$119k | - | SHORT (clean 34, ADX 32, RVol 0.7) |
| 11 | **QQQ** | 686.21 | TREND (flow not with it) | **PUTS** | 25 | none: 696 puts 0-7DTE > 69 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (267 contracts' greeks worked out here) | NEG -$864.8M | 690.18 | 700 | 680 | +$16.0M | +$1.8M bull / -$678k bear | SHORT (clean 32, ADX 38, RVol 0.7) |
| 12 | **AAPL** | 356.72 | - | **-** | 24 | - | POS +$1.1B | 339.81 | 360 | 360 | +$2.3M | +$704k bull / -$56k bear | out (clean 29, ADX 48, RVol 1.3) |
| 13 | **PLTR** | 170.02 | PINNED between the walls (positive gamma) - chop | **-** | 24 | - | POS +$85.8M | - | 170 | 170 | -$30k | - | out (clean 28, ADX 38, RVol 1.0) |
| 14 | **SPY** | 757.11 | TREND (flow not with it) | **PUTS** | 23 | 11/12 753P @ 0.78 (delta 0.23) = est +41% at 755 | NEG -$3.5B | 760.84 | 760 | 760 | +$28.8M | +$1.7M bull / -$1.6M bear | SHORT (clean 32, ADX 30, RVol 0.6) |
| 15 | **GOOGL** | 295.13 | - | **-** | 23 | - | POS +$96.6M | 288.55 | 300 | 290 | +$1.6M | +$255k bull / +$0 bear | out (clean 29, ADX 24, RVol 1.9) |
| 16 | **COIN** | 130.26 | - | **-** | 23 | - | NEG -$4.0M | 130.87 | 137 | 130 | +$270k | - | out (clean 30, ADX 45, RVol 1.2) |
| 17 | **MSTR** | 114.22 | - | **-** | 23 | - | NEG -$33.1M | - | 125 | 110 | -$511k | +$0 bull / -$678k bear | out (clean 27, ADX 39, RVol 1.6) |
| 18 | **TSLA** | 391.45 | - | **-** | 22 | - | POS +$358.3M | - | 400 | 380 | +$15.1M | +$1.4M bull / +$0 bear | out (clean 30, ADX 26, RVol 0.8) |
| 19 | **MSFT** | 524.10 | - | **-** | 22 | - | POS +$96.4M | 518.92 | 535 | 520 | -$2.1M | +$679k bull / +$0 bear | out (clean 31, ADX 36, RVol 0.9) |
| 20 | **BABA** | 94.48 | - | **-** | 22 | - | NEG -$17.4M | - | 100 | 100 | +$229k | - | out (clean 29, ADX 51, RVol 4.2) |
| 21 | **SMH** | 498.37 | - | **-** | 21 | - | NEG -$151.2M | - | 500 | 475 | -$190k | +$746k bull / -$360k bear | out (clean 32, ADX 46, RVol 1.1) |
| 22 | **UBER** | 69.34 | - | **-** | 17 | - | POS +$10.5M | 68.24 | 70 | 70 | +$30k | - | out (clean 31, ADX 34, RVol 0.9) |
| 23 | **SHOP** | 147.62 | - | **-** | 16 | - | POS +$3.0M | 143.93 | 150 | 140 | -$4k | - | out (clean 31, ADX 27, RVol 1.5) |
| 24 | **ORCL** | 125.73 | - | **-** | 12 | - | POS +$9.0M | 121.12 | 130 | 125 | -$358k | - | out (clean 30, ADX 32, RVol 0.9) |
| 25 | **NFLX** | 63.10 | - | **-** | 10 | - | NEG -$15.3M | 64.03 | 65 | 60 | -$35k | - | out (clean 27, ADX 39, RVol 1.0) |
| 26 | **ARM** | 198.18 | - | **-** | 10 | - | POS +$6.8M | - | 200 | 200 | +$66k | - | out (clean 31, ADX 32, RVol 0.7) |
| 27 | **CRM** | 215.66 | - | **-** | 9 | - | NEG -$8.9M | - | 220 | 220 | -$19k | - | out (clean 28, ADX 28, RVol 0.5) |

## Big prints this scan (183)
- **SPY** PUT 763 2026-11-16 (4DTE): 1,999 @ 8.00 = **+$1.6M** BUY | vol 5,019 / OI 216
- **NVDA** PUT 160 2026-11-13 (1DTE): 792 @ 2.94 = **+$233k** BUY | vol 57,864 / OI 24,121
- **QQQ** PUT 686 2026-11-12 (0DTE): 692 @ 3.32 = **+$230k** BUY | vol 35,346 / OI 278
- **QQQ** CALL 686 2026-11-12 (0DTE): 548 @ 3.91 = **+$214k** BUY | vol 29,898 / OI 503
- **NVDA** CALL 160 2026-11-13 (1DTE): 347 @ 5.35 = **+$186k** SELL | vol 95,186 / OI 2,015
- **QQQ** PUT 687 2026-11-12 (0DTE): 459 @ 3.93 = **+$180k** BUY | vol 27,162 / OI 97
- **NVDA** PUT 170 2026-11-13 (1DTE): 200 @ 8.91 = **+$178k** BUY | vol 11,125 / OI 14,967
- **MSFT** CALL 527.5 2026-11-13 (1DTE): 450 @ 3.65 = **+$164k** BUY | vol 3,436 / OI 503
- **QQQ** PUT 687 2026-11-12 (0DTE): 501 @ 3.10 = **+$155k** SELL | vol 27,162 / OI 97
- **QQQ** CALL 687 2026-11-12 (0DTE): 660 @ 2.21 = **+$146k** BUY | vol 47,253 / OI 452
- **MU** PUT 780 2026-11-13 (1DTE): 72 @ 20.00 = **+$144k** BUY | vol 4,131 / OI 1,167
- **MSFT** CALL 527.5 2026-11-13 (1DTE): 448 @ 3.17 = **+$142k** BUY | vol 3,436 / OI 503
- **NVDA** CALL 160 2026-11-13 (1DTE): 260 @ 4.70 = **+$122k** SELL | vol 95,186 / OI 2,015
- **MU** CALL 770 2026-11-13 (1DTE): 57 @ 21.40 = **+$122k** BUY | vol 2,221 / OI 1,263
- **NVDA** PUT 160 2026-11-16 (4DTE): 250 @ 4.80 = **+$120k** BUY | vol 9,267 / OI 4,794

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 749 2026-11-12 (0DTE): 867 traded vs OI 752
- **SPY** PUT 738 2026-11-12 (0DTE): 1,554 traded vs OI 1,457
- **SPY** PUT 753 2026-11-16 (4DTE): 529 traded vs OI 449
- **SPY** CALL 758 2026-11-17 (5DTE): 501 traded vs OI 338
- **SPY** CALL 751 2026-11-12 (0DTE): 1,261 traded vs OI 1,211
- **SPY** CALL 796 2026-11-17 (5DTE): 800 traded vs OI 84
- **SPY** CALL 756 2026-11-13 (1DTE): 5,407 traded vs OI 4,625
- **QQQ** CALL 705 2026-11-13 (1DTE): 3,023 traded vs OI 2,830
- **QQQ** PUT 664 2026-11-13 (1DTE): 759 traded vs OI 345
- **QQQ** PUT 674 2026-11-13 (1DTE): 1,135 traded vs OI 1,094
- **QQQ** PUT 675 2026-11-17 (5DTE): 1,188 traded vs OI 361
- **QQQ** PUT 688 2026-11-16 (4DTE): 514 traded vs OI 20
- **QQQ** PUT 685 2026-11-17 (5DTE): 526 traded vs OI 162
- **QQQ** CALL 706 2026-11-17 (5DTE): 867 traded vs OI 110
- **IWM** PUT 279 2026-11-13 (1DTE): 2,491 traded vs OI 1,770

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
