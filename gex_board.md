# GEX + FLOW SCAN - Thu Nov 12, 10:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:50 | **HOOD** | **PUTS** | TREND + FLOW | 11/13 79P | 0.55 | 0.43 | +5% (19m) | **-22%** | +92% | 80 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 130C | 0.75 | 0.55 | -1% (8m) | **-27%** | +59% | 126.9 |
| 09:45 | **SMCI** | **PUTS** | TREND + FLOW | 11/13 27P | 0.42 | 0.28 | -5% (6m) | **-33%** | +57% | 27 |
| 09:45 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 753P | 0.79 | 0.53 | +23% (18m) | **-33%** | +51% | 754.88 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:30:08 ET, last candle SPY 10:29, QQQ 10:29 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:03 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (3 today, last 5)
- 10:30 IWM CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:25 IWM CALLS: price -0.79 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:20 IWM CALLS: price -0.12 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NVDA** | 165.04 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 80 | none: 42 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$178.6M | - | 170 | 160 | -$122.2M | +$0 bull / -$8.7M bear | SHORT (clean 33, ADX 41, RVol 2.6) |
| 2 | **AVGO** | 361.52 | TREND + FLOW | **CALLS** | 48 | none: 81 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$130.4M | - | 350 | 350 | +$2.8M | +$450k bull / -$619k bear | LONG (clean 36, ADX 41, RVol 2.7) |
| 3 | **DELL** | 358.16 | TREND + FLOW | **PUTS** | 47 | none: 29 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | POS +$2.2M | 348.87 | 360 | 340 | -$575k | +$0 bull / -$287k bear | SHORT (clean 37, ADX 37, RVol 1.5) |
| 4 | **IWM** | 279.19 | FLOW SURGE | **CALLS** | 46 | 11/12 280C @ 0.49 (delta 0.35) = est +74% at 280.38 | NEG -$1.3B | 282.67 | 285 | 275 | +$8.6M | +$126k bull / +$0 bear | SHORT (clean 35, ADX 56, RVol 0.9) |
| 5 | **MU** | 778.07 | TREND (flow not with it) | **PUTS** | 45 | none: 128 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$78.2M | - | 800 | 800 | +$36.9M | +$744k bull / -$11.9M bear | SHORT (clean 32, ADX 43, RVol 1.2) |
| 6 | **SMCI** | 28.10 | TREND + FLOW | **PUTS** | 40 | 11/13 28P @ 0.71 (delta 0.50) = est +90% at 27 | POS +$3.0M | - | 30 | 27 | -$76k | - | SHORT (clean 34, ADX 50, RVol 1.6) |
| 7 | **AMZN** | 269.85 | PINNED between the walls (positive gamma) - chop | **-** | 36 | - | POS +$501.6M | - | 270 | 270 | -$3.9M | +$249k bull / +$0 bear | out (clean 31, ADX 33, RVol 0.9) |
| 8 | **PLTR** | 170.10 | PINNED between the walls (positive gamma) - chop | **-** | 35 | - | POS +$87.4M | - | 170 | 170 | -$108k | +$0 bull / -$60k bear | out (clean 28, ADX 40, RVol 0.9) |
| 9 | **QQQ** | 686.29 | TREND (flow not with it) | **PUTS** | 34 | none: 696 puts 0-7DTE > 70 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (231 contracts' greeks worked out here) | NEG -$871.7M | 690.31 | 700 | 680 | +$11.4M | +$619k bull / -$1.6M bear | SHORT (clean 32, ADX 37, RVol 0.8) |
| 10 | **SPY** | 757.43 | TREND (flow not with it) | **PUTS** | 29 | 11/12 754P @ 0.71 (delta 0.24) = est +84% at 754.77 | NEG -$2.9B | 760.77 | 760 | 760 | +$10.4M | +$202k bull / -$2.6M bear | SHORT (clean 32, ADX 28, RVol 0.4) |
| 11 | **AMD** | 561.58 | - | **-** | 26 | - | POS +$162.9M | - | 550 | 550 | +$32.0M | +$2.6M bull / -$1.3M bear | out (clean 34, ADX 26, RVol 1.9) |
| 12 | **HOOD** | 82.05 | TREND (flow not with it) | **PUTS** | 26 | 11/13 79P @ 0.47 (delta 0.21) = est +95% at 80.21 | POS +$6.5M | 80.21 | 85 | 80 | +$92k | - | SHORT (clean 34, ADX 32, RVol 0.8) |
| 13 | **ORCL** | 125.42 | - | **-** | 24 | - | POS +$8.4M | 121.23 | 130 | 125 | -$536k | +$0 bull / -$30k bear | out (clean 29, ADX 31, RVol 0.9) |
| 14 | **SMH** | 497.75 | - | **-** | 23 | - | NEG -$144.4M | - | 500 | 475 | -$736k | +$0 bull / -$449k bear | out (clean 31, ADX 45, RVol 1.3) |
| 15 | **MSFT** | 525.82 | - | **-** | 23 | - | POS +$128.4M | 520.07 | 535 | 520 | -$3.4M | +$456k bull / -$63k bear | out (clean 31, ADX 35, RVol 0.7) |
| 16 | **AAPL** | 357.86 | - | **-** | 22 | - | POS +$1.1B | 338.96 | 360 | 360 | +$1.4M | +$533k bull / +$0 bear | out (clean 29, ADX 45, RVol 1.1) |
| 17 | **META** | 622.14 | - | **-** | 22 | - | NEG -$27.7M | 624.76 | 650 | 600 | +$2.1M | +$136k bull / -$124k bear | out (clean 29, ADX 57, RVol 0.7) |
| 18 | **COIN** | 130.28 | - | **-** | 22 | - | NEG -$3.0M | 130.72 | 137 | 130 | +$296k | - | out (clean 30, ADX 46, RVol 1.3) |
| 19 | **TSLA** | 389.86 | - | **-** | 21 | - | POS +$348.3M | - | 400 | 380 | +$13.4M | +$612k bull / -$26k bear | out (clean 30, ADX 27, RVol 0.7) |
| 20 | **BABA** | 94.67 | - | **-** | 20 | - | NEG -$18.1M | - | 100 | 100 | +$201k | - | out (clean 30, ADX 54, RVol 4.0) |
| 21 | **GOOGL** | 295.64 | - | **-** | 19 | - | POS +$100.4M | 288.68 | 300 | 290 | +$593k | +$0 bull / -$55k bear | out (clean 29, ADX 22, RVol 1.7) |
| 22 | **ARM** | 197.69 | - | **-** | 19 | - | POS +$7.6M | - | 200 | 200 | -$57k | +$0 bull / -$100k bear | out (clean 31, ADX 34, RVol 0.7) |
| 23 | **MSTR** | 114.76 | - | **-** | 17 | - | NEG -$32.6M | - | 125 | 110 | -$1.8M | - | out (clean 27, ADX 39, RVol 1.2) |
| 24 | **NFLX** | 63.24 | - | **-** | 16 | - | NEG -$14.9M | 64.04 | 65 | 65 | -$208k | - | out (clean 27, ADX 40, RVol 1.0) |
| 25 | **UBER** | 69.34 | - | **-** | 11 | - | POS +$12.4M | 68.3 | 70 | 70 | +$16k | - | out (clean 31, ADX 35, RVol 0.7) |
| 26 | **SHOP** | 147.90 | - | **-** | 10 | - | POS +$4.8M | 142.82 | 150 | 140 | -$2k | - | out (clean 30, ADX 27, RVol 1.2) |
| 27 | **CRM** | 215.71 | - | **-** | 7 | - | NEG -$9.3M | - | 220 | 220 | -$11k | - | out (clean 28, ADX 27, RVol 0.4) |

## Big prints this scan (166)
- **MU** CALL 745 2026-11-13 (1DTE): 686 @ 30.63 = **+$2.1M** SELL | vol 735 / OI 1,094
- **MU** CALL 765 2026-11-13 (1DTE): 686 @ 18.07 = **+$1.2M** SELL | vol 1,625 / OI 987
- **AMD** CALL 550 2026-11-13 (1DTE): 500 @ 19.00 = **+$950k** BUY | vol 1,383 / OI 2,719
- **MU** PUT 790 2026-11-13 (1DTE): 100 @ 30.95 = **+$310k** BUY | vol 2,640 / OI 457
- **MU** PUT 765 2026-11-18 (6DTE): 100 @ 30.05 = **+$300k** BUY | vol 253 / OI 15
- **MU** CALL 740 2026-11-18 (6DTE): 60 @ 46.75 = **+$280k** SELL | vol 125 / OI 212
- **MU** CALL 740 2026-11-18 (6DTE): 60 @ 46.65 = **+$280k** SELL | vol 125 / OI 212
- **NVDA** CALL 160 2026-11-13 (1DTE): 500 @ 4.53 = **+$226k** SELL | vol 105,523 / OI 2,015
- **MU** PUT 770 2026-11-13 (1DTE): 106 @ 19.36 = **+$205k** BUY | vol 6,389 / OI 729
- **MU** PUT 780 2026-11-13 (1DTE): 72 @ 24.00 = **+$173k** BUY | vol 5,165 / OI 1,167
- **SPY** PUT 758 2026-11-17 (5DTE): 298 @ 5.51 = **+$164k** BUY | vol 791 / OI 129
- **QQQ** PUT 680 2026-11-12 (0DTE): 886 @ 1.55 = **+$137k** BUY | vol 60,692 / OI 1,005
- **SPY** PUT 758 2026-11-12 (0DTE): 400 @ 3.05 = **+$122k** BUY | vol 30,916 / OI 120
- **SPY** PUT 770 2026-11-17 (5DTE): 85 @ 13.75 = **+$117k** BUY | vol 98 / OI 77
- **NVDA** PUT 160 2026-11-16 (4DTE): 250 @ 4.25 = **+$106k** BUY | vol 12,315 / OI 4,794

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 737 2026-11-16 (4DTE): 636 traded vs OI 564
- **SPY** PUT 758 2026-11-17 (5DTE): 791 traded vs OI 129
- **SPY** PUT 706 2026-11-16 (4DTE): 661 traded vs OI 231
- **SPY** PUT 721 2026-11-12 (0DTE): 1,695 traded vs OI 735
- **SPY** CALL 766 2026-11-13 (1DTE): 3,050 traded vs OI 2,980
- **SPY** PUT 733 2026-11-12 (0DTE): 1,310 traded vs OI 1,306
- **SPY** CALL 775 2026-12-04 (22DTE): 2,439 traded vs OI 1,803
- **QQQ** PUT 686 2026-11-16 (4DTE): 536 traded vs OI 337
- **QQQ** CALL 684 2026-11-16 (4DTE): 503 traded vs OI 110
- **QQQ** PUT 670 2026-11-13 (1DTE): 6,620 traded vs OI 6,470
- **QQQ** CALL 710 2026-11-12 (0DTE): 1,678 traded vs OI 1,633
- **QQQ** PUT 682 2026-11-13 (1DTE): 3,714 traded vs OI 2,662
- **QQQ** CALL 686 2026-11-16 (4DTE): 584 traded vs OI 279
- **QQQ** PUT 639 2026-11-20 (8DTE): 597 traded vs OI 302
- **QQQ** PUT 664 2026-11-20 (8DTE): 651 traded vs OI 180

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
