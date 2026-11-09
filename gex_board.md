# GEX + FLOW SCAN - Mon Nov 09, 09:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:50:08 ET, last candle SPY 09:49, QQQ 09:49 | no errors

## Flow surges NOT fired - price disagreed (1 today, last 5)
- 09:50 SPY PUTS: price +3.67 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 541.49 | TREND + FLOW | **CALLS** | 69 | none: 176 calls 0-7DTE > 14 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (80 contracts' greeks worked out here) | POS +$569.5M | - | 550 | 540 | +$2.5M | +$1.1M bull / +$0 bear | LONG (clean 34, ADX 30, RVol 2.5) |
| 2 | **TSLA** | 376.20 | FLOW SURGE | **PUTS** | 64 | none: 120 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (58 contracts' greeks worked out here) | POS +$102.1M | - | 400 | 380 | -$53.1M | +$0 bull / -$2.3M bear | LONG (clean 34, ADX 32, RVol 3.3) |
| 3 | **NVDA** | 177.42 | FLOW SURGE | **PUTS** | 59 | none: 60 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (25 contracts' greeks worked out here) | NEG -$177.2M | - | 190 | 190 | -$32.2M | +$400k bull / -$13.9M bear | out (clean 32, ADX 32, RVol 10.8) |
| 4 | **SMH** | 477.12 | FLOW SURGE | **PUTS** | 58 | none: 152 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (68 contracts' greeks worked out here) | NEG -$250.7M | - | 500 | 475 | -$1.5M | +$0 bull / -$181k bear | out (clean 31, ADX 26, RVol 2.5) |
| 5 | **META** | 641.88 | FLOW SURGE | **PUTS** | 58 | none: 204 puts 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (84 contracts' greeks worked out here) | POS +$180.0M | 609.71 | 650 | 650 | -$9.8M | +$76k bull / -$2.0M bear | out (clean 33, ADX 38, RVol 3.9) |
| 6 | **IWM** | 278.56 | FLOW SURGE | **PUTS** | 57 | none: 311 puts 0-7DTE > 22 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +16% at the target (needs +20%) (141 contracts' greeks worked out here) | NEG -$1.5B | 285.2 | 285 | 270 | -$2.7M | +$0 bull / -$72k bear | out (clean 32, ADX 28, RVol 3.2) |
| 7 | **AMD** | 488.52 | FLOW SURGE | **PUTS** | 57 | none: 156 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (65 contracts' greeks worked out here) | NEG -$19.8M | - | 500 | 440 | -$11.2M | +$0 bull / -$2.8M bear | out (clean 32, ADX 36, RVol 5.1) |
| 8 | **QQQ** | 671.92 | FLOW SURGE | **PUTS** | 56 | none: 785 puts 0-7DTE > 58 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (227 contracts' greeks worked out here) | NEG -$2.3B | 701.06 | 680 | 680 | -$68.4M | +$0 bull / -$2.8M bear | out (clean 32, ADX 26, RVol 2.4) |
| 9 | **PLTR** | 167.72 | FLOW SURGE | **PUTS** | 56 | none: 13 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$9.8M | - | 165 | 170 | -$1.8M | +$0 bull / -$627k bear | out (clean 28, ADX 30, RVol 3.7) |
| 10 | **SPY** | 747.09 | FLOW SURGE | **PUTS** | 55 | 11/09 742P @ 0.79 (delta 0.21) = est +27% at 745 | NEG -$7.8B | 761.91 | 750 | 740 | -$52.6M | +$0 bull / -$969k bear | out (clean 32, ADX 24, RVol 2.5) |
| 11 | **AVGO** | 312.90 | FLOW SURGE | **PUTS** | 54 | none: 100 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (45 contracts' greeks worked out here) | NEG -$70.4M | - | 340 | 300 | -$1.4M | +$0 bull / -$278k bear | out (clean 30, ADX 32, RVol 4.7) |
| 12 | **AMZN** | 272.43 | TREND + FLOW | **CALLS** | 49 | none: 84 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (30 contracts' greeks worked out here) | POS +$411.7M | - | 270 | 265 | +$2.1M | +$845k bull / -$1.1M bear | LONG (clean 36, ADX 36, RVol 3.2) |
| 13 | **SMCI** | 28.80 | - | **-** | 30 | - | NEG -$313k | - | 30 | 30 | -$37k | - | out (clean 32, ADX 33, RVol 2.0) |
| 14 | **UBER** | 68.96 | - | **-** | 29 | - | NEG -$2.1M | 69.47 | 70 | 65 | +$23k | - | out (clean 31, ADX 25, RVol 2.2) |
| 15 | **COIN** | 136.11 | - | **-** | 28 | - | NEG -$6.3M | - | 140 | 135 | -$116k | - | out (clean 31, ADX 22, RVol 1.9) |
| 16 | **MSTR** | 126.07 | - | **-** | 28 | - | POS +$1.9M | 122.06 | 135 | 120 | -$450k | +$0 bull / -$395k bear | out (clean 30, ADX 39, RVol 3.0) |
| 17 | **HOOD** | 83.91 | - | **-** | 28 | - | NEG -$1.3M | - | 85 | 85 | -$349k | +$0 bull / -$243k bear | out (clean 30, ADX 43, RVol 2.1) |
| 18 | **BABA** | 106.08 | - | **-** | 28 | - | POS +$3.9M | 103.72 | 110 | 110 | -$272k | - | out (clean 32, ADX 25, RVol 3.6) |
| 19 | **GOOGL** | 293.37 | - | **-** | 27 | - | POS +$15.7M | 290.45 | 300 | 290 | +$1.4M | +$634k bull / -$60k bear | out (clean 32, ADX 28, RVol 3.2) |
| 20 | **ARM** | 183.60 | - | **-** | 27 | - | NEG -$4.5M | - | 185 | 190 | -$101k | - | out (clean 25, ADX 29, RVol 2.4) |
| 21 | **DELL** | 344.07 | - | **-** | 25 | - | NEG -$7.0M | - | 350 | 340 | +$82k | +$0 bull / -$488k bear | out (clean 31, ADX 27, RVol 2.3) |
| 22 | **NFLX** | 63.29 | - | **-** | 24 | - | NEG -$21.7M | - | 65 | 65 | +$81k | - | out (clean 32, ADX 31, RVol 2.2) |
| 23 | **AAPL** | 348.86 | - | **-** | 22 | - | POS +$377.6M | 337.71 | 350 | 350 | -$1.1M | +$121k bull / -$380k bear | out (clean 27, ADX 26, RVol 1.8) |
| 24 | **ORCL** | 119.00 | - | **-** | 20 | - | NEG -$27.0M | - | 125 | 120 | -$76k | +$0 bull / -$146k bear | out (clean 29, ADX 23, RVol 1.4) |
| 25 | **MU** | 719.31 | - | **-** | 19 | - | NEG -$31.6M | - | 750 | 750 | -$899k | +$0 bull / -$9.3M bear | out (clean 31, ADX 20, RVol 2.4) |
| 26 | **CRM** | 215.47 | - | **-** | 19 | - | NEG -$10.7M | - | 195 | 220 | -$5k | - | out (clean 34, ADX 23, RVol 3.4) |
| 27 | **SHOP** | 148.86 | - | **-** | 18 | - | POS +$1.4M | 140.05 | 150 | 140 | +$3k | - | out (clean 34, ADX 19, RVol 2.2) |

## Big prints this scan (664)
- **QQQ** CALL 665 2026-11-13 (4DTE): 500 @ 10.95 = **+$548k** SELL | vol 1,309 / OI 1,738
- **NVDA** PUT 170 2026-11-11 (2DTE): 1,000 @ 5.45 = **+$545k** BUY | vol 3,089 / OI 3,513
- **AMD** CALL 500 2026-11-13 (4DTE): 498 @ 10.50 = **+$523k** SELL | vol 1,451 / OI 1,939
- **NVDA** PUT 180 2026-11-13 (4DTE): 446 @ 11.42 = **+$509k** BUY | vol 4,234 / OI 7,865
- **QQQ** CALL 665 2026-11-13 (4DTE): 500 @ 10.06 = **+$503k** SELL | vol 1,309 / OI 1,738
- **NVDA** PUT 180 2026-11-16 (7DTE): 300 @ 11.95 = **+$358k** BUY | vol 831 / OI 618
- **MU** CALL 705 2026-11-11 (2DTE): 130 @ 24.00 = **+$312k** SELL | vol 231 / OI 160
- **NVDA** PUT 180 2026-11-13 (4DTE): 268 @ 11.41 = **+$306k** BUY | vol 4,234 / OI 7,865
- **NVDA** PUT 180 2026-11-13 (4DTE): 268 @ 11.40 = **+$306k** BUY | vol 4,234 / OI 7,865
- **AMD** PUT 475 2026-11-09 (0DTE): 300 @ 10.00 = **+$300k** BUY | vol 390 / OI 110
- **NVDA** PUT 170 2026-11-13 (4DTE): 446 @ 6.38 = **+$285k** BUY | vol 5,180 / OI 10,619
- **NVDA** PUT 180 2026-11-13 (4DTE): 229 @ 11.41 = **+$261k** BUY | vol 4,234 / OI 7,865
- **DELL** PUT 340 2026-11-13 (4DTE): 120 @ 21.70 = **+$260k** BUY | vol 121 / OI 104
- **AMZN** CALL 265 2026-11-13 (4DTE): 300 @ 8.58 = **+$257k** SELL | vol 695 / OI 2,784
- **SPY** CALL 743 2026-11-09 (0DTE): 892 @ 2.79 = **+$249k** SELL | vol 15,463 / OI 1,035

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 755 2026-11-09 (0DTE): 6,181 traded vs OI 2,236
- **SPY** PUT 742 2026-11-10 (1DTE): 906 traded vs OI 411
- **SPY** PUT 733 2026-11-09 (0DTE): 2,114 traded vs OI 973
- **SPY** PUT 718 2026-11-09 (0DTE): 2,501 traded vs OI 490
- **SPY** CALL 756 2026-11-09 (0DTE): 1,920 traded vs OI 1,537
- **SPY** CALL 744 2026-11-10 (1DTE): 1,185 traded vs OI 586
- **SPY** CALL 745 2026-11-10 (1DTE): 1,561 traded vs OI 886
- **SPY** PUT 723 2026-11-09 (0DTE): 789 traded vs OI 532
- **SPY** CALL 743 2026-11-10 (1DTE): 1,605 traded vs OI 333
- **SPY** PUT 740 2026-11-09 (0DTE): 6,759 traded vs OI 5,702
- **SPY** PUT 735 2026-11-09 (0DTE): 4,683 traded vs OI 3,156
- **SPY** CALL 747 2026-11-10 (1DTE): 598 traded vs OI 485
- **SPY** PUT 732 2026-11-09 (0DTE): 2,016 traded vs OI 1,201
- **SPY** CALL 738 2026-11-09 (0DTE): 1,086 traded vs OI 906
- **SPY** PUT 730 2026-11-09 (0DTE): 3,769 traded vs OI 3,600

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
