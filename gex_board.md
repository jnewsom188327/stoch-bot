# GEX + FLOW SCAN - Thu Nov 05, 10:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 1.58 | +115% (14m) | **+103%** | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.25 | -12% (0m) | **-48%** | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.24 | -4% (0m) | **-69%** | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:10:08 ET, last candle SPY 10:09, QQQ 10:09 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 10:10 IWM CALLS: price -0.72 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:05 SPY CALLS: price -3.47 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 SPY CALLS: price -2.75 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 NFLX CALLS: under EMA 20 - flow says one way, price says the other
- 09:55 IWM CALLS: price -2.39 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DELL** | 332.45 | FLOW SURGE | **CALLS** | 71 | none: 21 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | NEG -$15.4M | - | 360 | 340 | +$4.4M | +$296k bull / +$0 bear | SHORT (clean 33, ADX 43, RVol 3.0) |
| 2 | **QQQ** | 664.01 | FLOW SURGE | **CALLS** | 66 | none: 544 calls 0-7DTE > 42 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (234 contracts' greeks worked out here) | NEG -$5.6B | - | 700 | 680 | +$442.0M | +$46.0M bull / +$0 bear | SHORT (clean 34, ADX 47, RVol 2.8) |
| 3 | **TSLA** | 350.22 | FLOW SURGE | **CALLS** | 66 | none: 76 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$164.2M | - | 370 | 350 | +$102.4M | +$8.1M bull / -$2.4M bear | SHORT (clean 34, ADX 50, RVol 8.0) |
| 4 | **SMH** | 467.95 | FLOW SURGE | **CALLS** | 65 | none: 95 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$390.7M | - | 505 | 500 | +$7.8M | +$5.1M bull / +$0 bear | SHORT (clean 33, ADX 44, RVol 3.9) |
| 5 | **PLTR** | 157.24 | FLOW SURGE | **CALLS** | 64 | none: 16 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$48.2M | - | 165 | 150 | +$9.9M | +$1.0M bull / +$0 bear | out (clean 27, ADX 39, RVol 5.0) |
| 6 | **SPY** | 751.92 | FLOW SURGE | **CALLS** | 63 | none: 668 calls 0-7DTE > 21 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (255 contracts' greeks worked out here) | NEG -$10.5B | 769.52 | 760 | 750 | +$418.1M | +$15.0M bull / +$0 bear | SHORT (clean 33, ADX 46, RVol 2.4) |
| 7 | **NVDA** | 188.27 | FLOW SURGE | **CALLS** | 63 | none: 39 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$308.8M | - | 200 | 190 | +$41.1M | +$4.4M bull / +$0 bear | out (clean 31, ADX 57, RVol 4.8) |
| 8 | **AMD** | 426.91 | FLOW SURGE | **CALLS** | 63 | none: 102 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | NEG -$115.5M | - | 430 | 440 | +$34.8M | +$3.0M bull / +$0 bear | out (clean 32, ADX 39, RVol 4.0) |
| 9 | **MU** | 709.21 | FLOW SURGE | **CALLS** | 63 | none: 100 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | NEG -$130.1M | - | 700 | 750 | +$119.0M | +$15.0M bull / +$0 bear | out (clean 32, ADX 55, RVol 4.5) |
| 10 | **META** | 601.36 | FLOW SURGE | **CALLS** | 61 | none: 141 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | NEG -$144.7M | 623.61 | 650 | 600 | +$24.4M | +$3.6M bull / +$0 bear | out (clean 33, ADX 31, RVol 2.6) |
| 11 | **ARM** | 170.66 | FLOW SURGE | **CALLS** | 61 | none: 13 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$7.5M | - | 180 | 180 | +$1.1M | +$35k bull / +$0 bear | out (clean 27, ADX 49, RVol 3.4) |
| 12 | **BABA** | 106.39 | FLOW SURGE | **CALLS** | 60 | 11/06 109C @ 0.65 (delta 0.25) = est +50% at 107.92 | POS +$21.2M | - | 110 | 110 | +$845k | +$239k bull / +$0 bear | out (clean 37, ADX 33, RVol 5.4) |
| 13 | **SHOP** | 140.75 | TREND (flow not with it) | **PUTS** | 59 | none: 25 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$7.0M | - | 144 | 135 | +$94k | - | SHORT (clean 35, ADX 48, RVol 2.2) |
| 14 | **MSFT** | 544.91 | FLOW SURGE | **CALLS** | 54 | none: 129 calls 0-7DTE > 15 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | POS +$929.6M | - | 550 | 500 | +$12.6M | +$4.2M bull / +$0 bear | out (clean 31, ADX 41, RVol 2.3) |
| 15 | **MSTR** | 131.91 | FLOW SURGE | **CALLS** | 54 | none: 27 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (11 contracts' greeks worked out here) | POS +$79.9M | - | 135 | 125 | +$3.5M | +$384k bull / +$0 bear | out (clean 33, ADX 58, RVol 2.0) |
| 16 | **AMZN** | 259.88 | FLOW SURGE | **CALLS** | 53 | none: 63 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$400.6M | - | 265 | 250 | +$17.5M | +$2.9M bull / +$0 bear | out (clean 34, ADX 19, RVol 2.5) |
| 17 | **IWM** | 279.85 | FLOW SURGE | **CALLS** | 52 | 11/05 281C @ 0.63 (delta 0.34) = est +85% at 281.45 | NEG -$1.5B | 285.58 | 285 | 270 | +$14.9M | +$386k bull / +$0 bear | SHORT (clean 34, ADX 28, RVol 2.0) |
| 18 | **COIN** | 140.35 | FLOW SURGE | **CALLS** | 52 | none: 25 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$25.1M | - | 142 | 135 | +$1.2M | +$32k bull / +$0 bear | out (clean 32, ADX 41, RVol 1.5) |
| 19 | **GOOGL** | 285.57 | FLOW SURGE | **CALLS** | 50 | none: 69 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$38.5M | 281.41 | 290 | 290 | +$7.9M | +$680k bull / +$0 bear | out (clean 35, ADX 21, RVol 1.8) |
| 20 | **SMCI** | 27.05 | TREND (flow not with it) | **PUTS** | 50 | 11/06 26.5P @ 0.61 (delta 0.39) = est +42% at 26.24 | NEG -$3.2M | - | 28 | 27 | +$340k | - | SHORT (clean 35, ADX 46, RVol 1.3) |
| 21 | **AAPL** | 348.23 | FLOW SURGE | **CALLS** | 46 | none: 84 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$635.2M | 333.96 | 350 | 340 | +$11.3M | +$1.7M bull / +$0 bear | out (clean 31, ADX 20, RVol 2.4) |
| 22 | **AVGO** | 305.95 | - | **-** | 32 | - | NEG -$129.9M | - | 330 | 300 | +$4.8M | - | out (clean 30, ADX 47, RVol 3.2) |
| 23 | **HOOD** | 79.50 | - | **-** | 32 | - | NEG -$7.9M | - | 85 | 80 | +$1.9M | - | out (clean 30, ADX 47, RVol 2.5) |
| 24 | **ORCL** | 118.66 | - | **-** | 29 | - | NEG -$53.0M | - | 130 | 120 | +$1.9M | - | out (clean 33, ADX 44, RVol 1.2) |
| 25 | **NFLX** | 65.92 | - | **-** | 23 | - | POS +$27.3M | - | 65 | 65 | +$212k | +$78k bull / +$0 bear | out (clean 33, ADX 25, RVol 1.1) |
| 26 | **UBER** | 68.44 | - | **-** | 23 | - | POS +$3.9M | 67.95 | 70 | 65 | +$179k | - | out (clean 32, ADX 24, RVol 1.3) |
| 27 | **CRM** | 224.58 | - | **-** | 15 | - | NEG -$14.9M | - | 240 | 220 | -$42k | - | out (clean 34, ADX 17, RVol 0.9) |

## Big prints this scan (353)
- **QQQ** PUT 675 2026-11-06 (1DTE): 12,500 @ 9.33 = **+$11.7M** SELL | vol 43,766 / OI 46,203
- **QQQ** PUT 675 2026-11-06 (1DTE): 8,315 @ 10.28 = **+$8.5M** SELL | vol 43,766 / OI 46,203
- **QQQ** PUT 675 2026-11-06 (1DTE): 8,308 @ 10.03 = **+$8.3M** SELL | vol 43,766 / OI 46,203
- **QQQ** PUT 675 2026-11-06 (1DTE): 1,888 @ 9.21 = **+$1.7M** SELL | vol 43,766 / OI 46,203
- **QQQ** PUT 675 2026-11-06 (1DTE): 1,301 @ 10.32 = **+$1.3M** SELL | vol 43,766 / OI 46,203
- **QQQ** PUT 675 2026-11-06 (1DTE): 1,215 @ 10.13 = **+$1.2M** SELL | vol 43,766 / OI 46,203
- **MSFT** CALL 540 2026-11-06 (1DTE): 1,000 @ 9.10 = **+$910k** BUY | vol 3,401 / OI 10,669
- **MU** PUT 700 2026-11-06 (1DTE): 750 @ 11.25 = **+$844k** SELL | vol 9,378 / OI 2,015
- **MSFT** CALL 540 2026-11-06 (1DTE): 794 @ 9.10 = **+$723k** BUY | vol 3,401 / OI 10,669
- **QQQ** PUT 675 2026-11-06 (1DTE): 539 @ 9.21 = **+$496k** SELL | vol 43,766 / OI 46,203
- **MU** PUT 680 2026-11-06 (1DTE): 750 @ 6.15 = **+$461k** SELL | vol 2,837 / OI 702
- **QQQ** PUT 675 2026-11-06 (1DTE): 451 @ 10.13 = **+$457k** SELL | vol 43,766 / OI 46,203
- **QQQ** CALL 659 2026-11-05 (0DTE): 420 @ 10.62 = **+$446k** BUY | vol 755 / OI 0
- **QQQ** CALL 672 2026-11-10 (5DTE): 500 @ 8.52 = **+$426k** BUY | vol 2,039 / OI 43
- **QQQ** PUT 675 2026-11-06 (1DTE): 361 @ 10.32 = **+$373k** SELL | vol 43,766 / OI 46,203

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 754 2026-11-09 (4DTE): 1,014 traded vs OI 864
- **SPY** CALL 777 2026-11-06 (1DTE): 3,147 traded vs OI 2,875
- **SPY** CALL 769 2026-11-06 (1DTE): 3,276 traded vs OI 3,039
- **SPY** PUT 752 2026-11-06 (1DTE): 3,856 traded vs OI 3,799
- **SPY** PUT 747 2026-11-06 (1DTE): 3,080 traded vs OI 2,718
- **SPY** CALL 771 2026-11-09 (4DTE): 829 traded vs OI 240
- **SPY** CALL 758 2026-11-06 (1DTE): 2,170 traded vs OI 1,673
- **SPY** PUT 757 2026-11-06 (1DTE): 4,627 traded vs OI 4,586
- **SPY** PUT 737 2026-11-06 (1DTE): 1,837 traded vs OI 1,597
- **SPY** CALL 756 2026-11-06 (1DTE): 2,441 traded vs OI 1,814
- **SPY** PUT 751 2026-11-09 (4DTE): 507 traded vs OI 185
- **SPY** PUT 753 2026-11-06 (1DTE): 3,667 traded vs OI 3,354
- **SPY** PUT 744 2026-11-06 (1DTE): 2,838 traded vs OI 2,755
- **SPY** PUT 773 2026-11-06 (1DTE): 639 traded vs OI 598
- **SPY** PUT 741 2026-11-06 (1DTE): 3,601 traded vs OI 3,242

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
