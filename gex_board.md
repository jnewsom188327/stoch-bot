# GEX + FLOW SCAN - Thu Nov 05, 10:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 0.84 | +56% (6m) | **+8%** | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.31 | -12% (0m) | **-35%** | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.40 | -4% (0m) | **-49%** | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:00:08 ET, last candle SPY 09:59, QQQ 09:59 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (4 today, last 5)
- 10:00 SPY CALLS: price -2.75 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 NFLX CALLS: under EMA 20 - flow says one way, price says the other
- 09:55 IWM CALLS: price -2.39 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:50 NFLX CALLS: price -0.87 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BABA** | 106.76 | TREND + FLOW | **CALLS** | 76 | 11/06 110C @ 0.52 (delta 0.22) = est +66% at 108.3 | POS +$22.4M | - | 110 | 110 | +$458k | +$61k bull / +$0 bear | LONG (clean 37, ADX 36, RVol 7.3) |
| 2 | **TSLA** | 347.32 | FLOW SURGE | **CALLS** | 71 | none: 73 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$151.1M | - | 370 | 350 | +$100.8M | +$7.3M bull / +$0 bear | SHORT (clean 33, ADX 46, RVol 7.2) |
| 3 | **AVGO** | 308.94 | FLOW SURGE | **CALLS** | 65 | none: 67 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$136.9M | - | 330 | 300 | +$4.0M | +$2.0M bull / +$0 bear | out (clean 30, ADX 44, RVol 3.4) |
| 4 | **DELL** | 333.68 | FLOW SURGE | **CALLS** | 65 | none: 20 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$16.2M | - | 360 | 350 | +$3.0M | +$275k bull / +$0 bear | out (clean 33, ADX 38, RVol 3.0) |
| 5 | **SPY** | 754.19 | FLOW SURGE | **CALLS** | 64 | 11/05 760C @ 0.78 (delta 0.20) = est +200% at 760 | NEG -$9.7B | 768.99 | 760 | 750 | +$305.7M | +$18.1M bull / +$0 bear | SHORT (clean 33, ADX 39, RVol 2.6) |
| 6 | **QQQ** | 666.72 | FLOW SURGE | **CALLS** | 63 | none: 550 calls 0-7DTE > 37 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (154 contracts' greeks worked out here) | NEG -$5.9B | - | 700 | 680 | +$272.7M | +$20.5M bull / +$0 bear | SHORT (clean 33, ADX 40, RVol 2.6) |
| 7 | **PLTR** | 157.17 | FLOW SURGE | **CALLS** | 63 | none: 16 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$48.0M | - | 165 | 160 | +$8.8M | +$1.6M bull / +$0 bear | out (clean 27, ADX 34, RVol 4.6) |
| 8 | **MU** | 711.00 | FLOW SURGE | **CALLS** | 63 | none: 100 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | NEG -$134.3M | - | 700 | 750 | +$77.8M | +$13.0M bull / +$0 bear | out (clean 31, ADX 50, RVol 4.5) |
| 9 | **NVDA** | 190.09 | FLOW SURGE | **CALLS** | 62 | none: 39 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$322.1M | - | 200 | 190 | +$27.0M | +$5.5M bull / +$0 bear | out (clean 31, ADX 53, RVol 5.0) |
| 10 | **AMD** | 426.91 | FLOW SURGE | **CALLS** | 61 | none: 102 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | NEG -$117.5M | - | 430 | 440 | +$25.1M | +$4.8M bull / +$0 bear | out (clean 32, ADX 33, RVol 4.3) |
| 11 | **SMH** | 469.98 | FLOW SURGE | **CALLS** | 60 | none: 98 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | NEG -$418.7M | - | 505 | 500 | +$3.4M | +$5.0M bull / +$0 bear | SHORT (clean 33, ADX 39, RVol 4.4) |
| 12 | **META** | 607.99 | FLOW SURGE | **CALLS** | 57 | none: 146 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (30 contracts' greeks worked out here) | NEG -$137.2M | 622.85 | 650 | 600 | +$16.3M | +$1.9M bull / +$0 bear | out (clean 32, ADX 25, RVol 2.2) |
| 13 | **MSFT** | 544.65 | FLOW SURGE | **CALLS** | 57 | none: 129 calls 0-7DTE > 18 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (29 contracts' greeks worked out here) | POS +$924.0M | - | 540 | 535 | +$10.9M | +$1.6M bull / +$0 bear | out (clean 30, ADX 37, RVol 2.5) |
| 14 | **MSTR** | 132.85 | FLOW SURGE | **CALLS** | 54 | none: 27 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$95.4M | - | 135 | 125 | +$2.5M | +$322k bull / +$0 bear | out (clean 33, ADX 53, RVol 2.0) |
| 15 | **AMZN** | 263.08 | FLOW SURGE | **CALLS** | 53 | none: 63 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (19 contracts' greeks worked out here) | POS +$432.0M | - | 265 | 250 | +$8.9M | +$1.0M bull / +$0 bear | out (clean 34, ADX 17, RVol 2.5) |
| 16 | **GOOGL** | 287.13 | FLOW SURGE | **CALLS** | 51 | none: 69 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (16 contracts' greeks worked out here) | POS +$44.2M | 281.94 | 290 | 290 | +$5.8M | +$702k bull / +$0 bear | out (clean 35, ADX 20, RVol 1.9) |
| 17 | **COIN** | 140.76 | FLOW SURGE | **CALLS** | 50 | none: 25 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$28.2M | - | 142 | 135 | +$805k | +$32k bull / +$0 bear | out (clean 31, ADX 34, RVol 1.4) |
| 18 | **SMCI** | 27.30 | TREND (flow not with it) | **PUTS** | 49 | none: 11 puts 0-7DTE > 2 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +6% at the target (needs +20%) (2 contracts' greeks worked out here) | NEG -$3.8M | - | 30 | 27 | +$263k | - | SHORT (clean 34, ADX 41, RVol 1.3) |
| 19 | **SHOP** | 142.65 | TREND (flow not with it) | **PUTS** | 49 | none: 24 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | NEG -$7.4M | - | 144 | 135 | +$70k | - | SHORT (clean 34, ADX 43, RVol 1.2) |
| 20 | **AAPL** | 351.88 | FLOW SURGE | **CALLS** | 46 | none: 84 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (51 contracts' greeks worked out here) | POS +$733.3M | 334.63 | 350 | 340 | +$6.5M | +$1.5M bull / -$240k bear | out (clean 31, ADX 19, RVol 2.7) |
| 21 | **ARM** | 171.28 | - | **-** | 38 | - | NEG -$7.7M | - | 180 | 180 | +$934k | +$58k bull / -$346k bear | out (clean 27, ADX 45, RVol 4.9) |
| 22 | **HOOD** | 79.56 | - | **-** | 31 | - | NEG -$8.0M | - | 85 | 80 | +$1.2M | - | out (clean 30, ADX 40, RVol 2.4) |
| 23 | **ORCL** | 118.05 | - | **-** | 30 | - | NEG -$57.8M | - | 125 | 120 | +$1.4M | - | out (clean 33, ADX 42, RVol 1.4) |
| 24 | **IWM** | 280.45 | - | **-** | 28 | - | NEG -$1.3B | 285.37 | 285 | 270 | +$8.6M | +$152k bull / +$0 bear | out (clean 34, ADX 22, RVol 2.4) |
| 25 | **UBER** | 68.31 | - | **-** | 28 | - | POS +$2.4M | 67.87 | 70 | 65 | +$198k | - | out (clean 32, ADX 24, RVol 2.1) |
| 26 | **NFLX** | 66.00 | - | **-** | 26 | - | POS +$31.7M | 62.31 | 65 | 65 | +$197k | +$84k bull / +$0 bear | out (clean 33, ADX 29, RVol 1.1) |
| 27 | **CRM** | 224.32 | - | **-** | 21 | - | NEG -$14.5M | - | 240 | 220 | -$47k | - | out (clean 34, ADX 17, RVol 0.6) |

## Big prints this scan (398)
- **SPY** CALL 755 2026-11-10 (5DTE): 2,000 @ 8.55 = **+$1.7M** BUY | vol 2,029 / OI 767
- **NVDA** PUT 197.5 2026-11-06 (1DTE): 678 @ 6.55 = **+$444k** SELL | vol 3,643 / OI 7,095
- **SPY** PUT 767 2026-11-06 (1DTE): 500 @ 7.46 = **+$373k** SELL | vol 7,039 / OI 1,033
- **TSLA** CALL 355 2026-11-06 (1DTE): 500 @ 7.35 = **+$368k** BUY | vol 3,203 / OI 272
- **QQQ** PUT 673 2026-11-06 (1DTE): 489 @ 6.73 = **+$329k** SELL | vol 2,140 / OI 135
- **TSLA** CALL 355 2026-11-06 (1DTE): 431 @ 7.40 = **+$319k** BUY | vol 3,203 / OI 272
- **MSFT** CALL 520 2026-11-06 (1DTE): 100 @ 28.00 = **+$280k** BUY | vol 118 / OI 1,465
- **SPY** PUT 764 2026-11-05 (0DTE): 669 @ 4.12 = **+$276k** SELL | vol 27,951 / OI 9
- **SPY** PUT 764 2026-11-05 (0DTE): 500 @ 5.41 = **+$270k** SELL | vol 27,951 / OI 9
- **SPY** CALL 755 2026-11-06 (1DTE): 400 @ 6.70 = **+$268k** BUY | vol 2,374 / OI 4,311
- **SPY** PUT 764 2026-11-05 (0DTE): 500 @ 4.98 = **+$249k** SELL | vol 27,951 / OI 9
- **QQQ** CALL 675 2026-11-06 (1DTE): 350 @ 6.42 = **+$225k** BUY | vol 2,296 / OI 506
- **QQQ** PUT 695 2026-11-05 (0DTE): 89 @ 23.84 = **+$212k** SELL | vol 565 / OI 1,938
- **MSFT** CALL 530 2026-11-11 (6DTE): 88 @ 23.60 = **+$208k** BUY | vol 102 / OI 179
- **QQQ** PUT 690 2026-11-06 (1DTE): 122 @ 17.00 = **+$207k** SELL | vol 1,879 / OI 12,919

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 745 2026-11-05 (0DTE): 9,986 traded vs OI 4,460
- **SPY** PUT 760 2026-11-09 (4DTE): 2,210 traded vs OI 1,984
- **SPY** PUT 762 2026-11-10 (5DTE): 1,017 traded vs OI 10
- **SPY** CALL 772 2026-11-06 (1DTE): 2,045 traded vs OI 1,874
- **SPY** CALL 771 2026-11-06 (1DTE): 3,360 traded vs OI 2,168
- **SPY** PUT 714 2026-11-05 (0DTE): 827 traded vs OI 201
- **SPY** PUT 746 2026-11-09 (4DTE): 502 traded vs OI 96
- **SPY** PUT 737 2026-11-05 (0DTE): 913 traded vs OI 737
- **SPY** CALL 755 2026-11-10 (5DTE): 2,029 traded vs OI 767
- **SPY** PUT 738 2026-11-05 (0DTE): 641 traded vs OI 314
- **SPY** PUT 759 2026-11-09 (4DTE): 559 traded vs OI 142
- **SPY** PUT 758 2026-11-10 (5DTE): 701 traded vs OI 61
- **SPY** PUT 758 2026-11-09 (4DTE): 530 traded vs OI 77
- **SPY** PUT 734 2026-11-05 (0DTE): 2,273 traded vs OI 1,551
- **SPY** PUT 743 2026-11-06 (1DTE): 2,037 traded vs OI 1,527

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
