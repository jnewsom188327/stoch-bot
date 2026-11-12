# GEX + FLOW SCAN - Thu Nov 12, 09:45 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 130C | 0.75 | 0.69 | -8% (0m) | **-8%** | +59% | 126.9 |
| 09:45 | **SMCI** | **PUTS** | TREND + FLOW | 11/13 27P | 0.42 | 0.37 | -12% (0m) | **-12%** | +57% | 27 |
| 09:45 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 753P | 0.79 | 0.74 | -6% (0m) | **-6%** | +51% | 754.88 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:45:08 ET, last candle SPY 09:44, QQQ 09:44 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NVDA** | 159.91 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 92 | none: 51 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | NEG -$191.2M | - | 170 | 160 | -$24.4M | +$0 bull / -$1.6M bear | SHORT (clean 34, ADX 42, RVol 4.9) |
| 2 | **QQQ** | 686.38 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 76 | none: 702 puts 0-7DTE > 64 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (241 contracts' greeks worked out here) | NEG -$664.9M | 690.2 | 700 | 680 | -$12.9M | - | SHORT (clean 33, ADX 39, RVol 3.3) |
| 3 | **SPY** | 757.35 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 68 | 11/12 753P @ 0.79 (delta 0.23) = est +51% at 754.88 | NEG -$2.9B | 761.21 | 760 | 760 | -$10.1M | - | SHORT (clean 34, ADX 31, RVol 2.6) |
| 4 | **DELL** | 359.38 | TREND + FLOW | **PUTS** | 65 | none: 29 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$2.1M | 350.32 | 360 | 340 | -$296k | - | SHORT (clean 38, ADX 41, RVol 4.2) |
| 5 | **SMCI** | 27.82 | TREND + FLOW | **PUTS** | 62 | 11/13 27P @ 0.42 (delta 0.31) = est +57% at 27 | POS +$2.8M | - | 30 | 27 | -$14k | - | SHORT (clean 34, ADX 45, RVol 3.1) |
| 6 | **AVGO** | 362.90 | TREND + FLOW | **CALLS** | 61 | none: 81 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$132.8M | - | 350 | 350 | +$799k | - | LONG (clean 37, ADX 49, RVol 5.6) |
| 7 | **COIN** | 129.97 | FLIP CROSS down into negative gamma | **PUTS** | 50 | none: 26 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | NEG -$3.2M | 131.75 | 137 | 135 | -$2k | - | out (clean 30, ADX 41, RVol 1.8) |
| 8 | **PLTR** | 170.31 | PINNED between the walls (positive gamma) - chop | **-** | 48 | - | POS +$84.3M | - | 170 | 170 | +$123k | - | out (clean 29, ADX 25, RVol 2.0) |
| 9 | **ORCL** | 124.81 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 48 | 11/13 130C @ 0.75 (delta 0.22) = est +59% at 126.9 | POS +$7.0M | 121.4 | 130 | 125 | -$110k | - | out (clean 30, ADX 23, RVol 2.5) |
| 10 | **UBER** | 70.01 | PINNED between the walls (positive gamma) - chop | **-** | 47 | - | POS +$16.8M | 68.19 | 70 | 70 | +$669 | - | out (clean 32, ADX 29, RVol 2.8) |
| 11 | **AMD** | 569.32 | TREND + FLOW | **CALLS** | 46 | none: 138 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$191.8M | - | 600 | 550 | +$301k | +$0 bull / -$156k bear | LONG (clean 36, ADX 33, RVol 3.3) |
| 12 | **ARM** | 199.90 | PINNED between the walls (positive gamma) - chop | **-** | 43 | - | POS +$8.0M | - | 200 | 200 | -$9k | - | out (clean 32, ADX 24, RVol 3.0) |
| 13 | **MU** | 790.14 | TREND + FLOW | **PUTS** | 40 | none: 122 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$82.0M | - | 800 | 800 | -$1.1M | - | SHORT (clean 33, ADX 31, RVol 1.9) |
| 14 | **IWM** | 280.70 | TREND (flow not with it) | **PUTS** | 39 | 11/12 280P @ 0.60 (delta 0.37) = est +123% at 279 | NEG -$854.3M | 283.05 | 285 | 275 | +$135k | - | SHORT (clean 35, ADX 30, RVol 2.4) |
| 15 | **MSTR** | 112.67 | - | **-** | 31 | - | NEG -$29.8M | - | 120 | 110 | +$293k | - | out (clean 28, ADX 31, RVol 4.2) |
| 16 | **SMH** | 497.48 | - | **-** | 30 | - | NEG -$136.4M | - | 500 | 475 | -$607k | - | out (clean 32, ADX 43, RVol 1.5) |
| 17 | **TSLA** | 393.38 | - | **-** | 29 | - | POS +$360.9M | - | 400 | 380 | -$3.4M | - | out (clean 31, ADX 31, RVol 1.9) |
| 18 | **AMZN** | 272.15 | - | **-** | 29 | - | POS +$520.8M | - | 270 | 270 | -$2.6M | - | out (clean 31, ADX 23, RVol 2.3) |
| 19 | **CRM** | 214.43 | - | **-** | 29 | - | NEG -$9.0M | - | 220 | 220 | +$6k | - | out (clean 28, ADX 22, RVol 2.6) |
| 20 | **SHOP** | 146.99 | - | **-** | 29 | - | POS +$4.0M | 142.9 | 150 | 140 | -$1k | - | out (clean 32, ADX 23, RVol 2.5) |
| 21 | **MSFT** | 523.92 | - | **-** | 25 | - | POS +$100.7M | 518.96 | 535 | 520 | +$542k | - | out (clean 32, ADX 27, RVol 2.5) |
| 22 | **NFLX** | 63.07 | - | **-** | 22 | - | NEG -$15.5M | 64.01 | 65 | 65 | +$7k | - | out (clean 27, ADX 35, RVol 2.2) |
| 23 | **HOOD** | 81.88 | - | **-** | 21 | - | POS +$6.9M | 79.91 | 85 | 80 | -$29k | - | out (clean 35, ADX 24, RVol 3.5) |
| 24 | **GOOGL** | 296.05 | - | **-** | 15 | - | POS +$96.8M | 288.67 | 300 | 290 | +$191k | - | out (clean 30, ADX 24, RVol 3.4) |
| 25 | **AAPL** | 356.90 | - | **-** | 14 | - | POS +$1.1B | 338.63 | 360 | 360 | +$242k | - | out (clean 28, ADX 37, RVol 2.3) |
| 26 | **META** | 626.09 | - | **-** | 14 | - | POS +$14.6M | 623.35 | 650 | 600 | -$22k | - | out (clean 30, ADX 51, RVol 2.6) |
| 27 | **BABA** | 94.39 | - | **-** | 11 | - | NEG -$16.9M | - | 100 | 100 | +$0 | - | out (clean 28, ADX 32, RVol 5.5) |

## Big prints this scan (2)
- **AMD** CALL 560 2026-11-13 (1DTE): 26 @ 15.50 = **+$40k** SELL | vol 264 / OI 2,043
- **AMD** PUT 555 2026-11-13 (1DTE): 26 @ 10.36 = **+$27k** BUY | vol 111 / OI 130

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 746 2026-11-12 (0DTE): 1,841 traded vs OI 872
- **SPY** CALL 767 2026-11-12 (0DTE): 1,730 traded vs OI 1,315
- **SPY** PUT 758 2026-11-12 (0DTE): 1,310 traded vs OI 120
- **SPY** PUT 759 2026-11-12 (0DTE): 1,392 traded vs OI 250
- **SPY** CALL 758 2026-11-12 (0DTE): 2,647 traded vs OI 1,273
- **SPY** CALL 761 2026-11-12 (0DTE): 2,412 traded vs OI 1,601
- **SPY** PUT 753 2026-11-12 (0DTE): 5,812 traded vs OI 457
- **SPY** PUT 763 2026-11-16 (4DTE): 2,002 traded vs OI 216
- **SPY** CALL 763 2026-11-12 (0DTE): 1,937 traded vs OI 1,242
- **SPY** PUT 752 2026-11-12 (0DTE): 5,748 traded vs OI 807
- **SPY** CALL 757 2026-11-12 (0DTE): 2,555 traded vs OI 1,287
- **SPY** PUT 750 2026-11-12 (0DTE): 10,076 traded vs OI 1,864
- **SPY** CALL 756 2026-11-12 (0DTE): 2,552 traded vs OI 849
- **SPY** CALL 760 2026-11-12 (0DTE): 4,191 traded vs OI 3,834
- **SPY** PUT 747 2026-11-12 (0DTE): 2,972 traded vs OI 2,447

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
