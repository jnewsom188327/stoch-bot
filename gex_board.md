# GEX + FLOW SCAN - Thu Nov 05, 11:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:55 | **BABA** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/06 102P | 0.75 | 0.60 | -11% (0m) | **-20%** | +27% | 103.58 |
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 11.35 | +1355% (60m) | **+1355%** (done) | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.20 | -12% (0m) | **-58%** (done) | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.10 | -4% (0m) | **-87%** (done) | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:00:08 ET, last candle SPY 10:59, QQQ 10:59 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:38 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 64 puts 0-1DTE > 1 priced 0.40-0.80 > 0 delta 0.15+ > 0 spread ok > 0 liquid  |
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (23 today, last 5)
- 11:00 IWM CALLS: price -1.16 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:55 IWM CALLS: price -2.06 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:50 HOOD CALLS: price -1.37 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:50 IWM CALLS: price -2.31 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:45 IWM CALLS: price -1.06 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMH** | 452.52 | FLOW SURGE | **CALLS** | 69 | none: 86 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$195.5M | - | 445 | 465 | +$43.9M | +$1.5M bull / +$0 bear | SHORT (clean 35, ADX 62, RVol 2.7) |
| 2 | **QQQ** | 653.30 | FLOW SURGE | **CALLS** | 65 | none: 492 calls 0-7DTE > 49 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (142 contracts' greeks worked out here) | NEG -$4.4B | - | 700 | 680 | +$785.2M | +$8.1M bull / +$0 bear | SHORT (clean 35, ADX 66, RVol 3.3) |
| 3 | **IWM** | 275.80 | FLOW SURGE | **CALLS** | 65 | 11/05 278C @ 0.55 (delta 0.26) = est +315% at 280 | NEG -$2.2B | 286.84 | 285 | 270 | +$44.3M | +$2.4M bull / +$0 bear | SHORT (clean 36, ADX 51, RVol 3.4) |
| 4 | **SPY** | 741.91 | FLOW SURGE | **CALLS** | 64 | none: 663 calls 0-7DTE > 30 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (246 contracts' greeks worked out here) | NEG -$11.6B | 771.28 | 760 | 740 | +$1.0B | +$34.4M bull / +$0 bear | SHORT (clean 35, ADX 67, RVol 2.5) |
| 5 | **AVGO** | 295.27 | FLOW SURGE | **CALLS** | 63 | none: 56 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$100.4M | - | 320 | 300 | +$8.6M | +$284k bull / +$0 bear | out (clean 32, ADX 58, RVol 4.0) |
| 6 | **MU** | 670.74 | FLOW SURGE | **CALLS** | 63 | none: 76 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (13 contracts' greeks worked out here) | NEG -$52.9M | - | 700 | 700 | +$184.6M | +$7.6M bull / +$0 bear | SHORT (clean 33, ADX 73, RVol 3.3) |
| 7 | **META** | 594.47 | TREND (flow not with it) | **PUTS** | 60 | none: 135 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | NEG -$168.9M | - | 650 | 600 | +$41.1M | +$3.6M bull / -$3.6M bear | SHORT (clean 34, ADX 49, RVol 2.2) |
| 8 | **NVDA** | 183.60 | FLOW SURGE | **CALLS** | 58 | none: 33 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$240.6M | - | 200 | 190 | +$66.0M | +$3.4M bull / +$0 bear | out (clean 33, ADX 68, RVol 3.3) |
| 9 | **PLTR** | 155.05 | FLOW SURGE | **CALLS** | 57 | none: 16 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$44.1M | - | 165 | 150 | +$12.2M | +$139k bull / +$0 bear | out (clean 28, ADX 53, RVol 2.3) |
| 10 | **AMD** | 410.77 | FLOW SURGE | **CALLS** | 54 | none: 99 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (15 contracts' greeks worked out here) | NEG -$89.0M | - | 430 | 440 | +$47.8M | +$2.6M bull / +$0 bear | SHORT (clean 33, ADX 55, RVol 1.7) |
| 11 | **DELL** | 321.29 | TREND (flow not with it) | **PUTS** | 54 | none: 18 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | NEG -$11.3M | - | 350 | 340 | +$7.2M | - | SHORT (clean 34, ADX 52, RVol 2.0) |
| 12 | **GOOGL** | 280.35 | FLOW SURGE | **CALLS** | 53 | none: 69 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$2.6M | 280.91 | 285 | 290 | +$10.9M | +$295k bull / +$0 bear | SHORT (clean 35, ADX 30, RVol 1.9) |
| 13 | **MSTR** | 127.58 | TREND (flow not with it) | **PUTS** | 53 | none: 26 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | POS +$39.9M | - | 135 | 125 | +$5.0M | - | SHORT (clean 34, ADX 68, RVol 2.6) |
| 14 | **MSFT** | 537.02 | FLOW SURGE | **CALLS** | 52 | none: 129 calls 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$765.7M | - | 540 | 500 | +$20.7M | +$506k bull / +$0 bear | out (clean 32, ADX 58, RVol 2.4) |
| 15 | **TSLA** | 344.05 | TREND (flow not with it) | **PUTS** | 51 | none: 74 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$131.9M | - | 370 | 350 | +$99.5M | +$2.1M bull / +$0 bear | SHORT (clean 35, ADX 57, RVol 2.8) |
| 16 | **AMZN** | 254.76 | FLOW SURGE | **CALLS** | 51 | none: 63 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$310.8M | - | 260 | 250 | +$33.4M | +$2.1M bull / +$0 bear | SHORT (clean 35, ADX 35, RVol 1.9) |
| 17 | **SMCI** | 26.22 | TREND (flow not with it) | **PUTS** | 50 | 11/06 25.5P @ 0.66 (delta 0.37) = est +35% at 25.36 | NEG -$2.1M | - | 28 | 27 | +$598k | - | SHORT (clean 36, ADX 59, RVol 1.7) |
| 18 | **COIN** | 136.31 | TREND (flow not with it) | **PUTS** | 48 | none: 26 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$16.0M | - | 142 | 135 | +$2.2M | - | SHORT (clean 33, ADX 62, RVol 1.3) |
| 19 | **ORCL** | 113.36 | TREND (flow not with it) | **PUTS** | 48 | none: 22 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$49.0M | - | 120 | 110 | +$4.4M | - | SHORT (clean 34, ADX 54, RVol 1.5) |
| 20 | **SHOP** | 140.06 | TREND (flow not with it) | **PUTS** | 42 | none: 25 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$6.8M | - | 144 | 135 | +$243k | - | SHORT (clean 36, ADX 58, RVol 0.7) |
| 21 | **HOOD** | 76.57 | - | **-** | 32 | - | NEG -$7.3M | - | 83 | 80 | +$2.3M | +$53k bull / +$0 bear | out (clean 31, ADX 69, RVol 1.9) |
| 22 | **UBER** | 68.33 | FLIP CROSS up into positive gamma | **CALLS** | 30 | 11/06 70C @ 0.43 (delta 0.26) = est +127% at 70 | POS +$1.7M | 67.99 | 70 | 65 | +$184k | - | out (clean 32, ADX 19, RVol 1.0) |
| 23 | **BABA** | 105.48 | - | **-** | 26 | - | POS +$20.4M | - | 105 | 100 | +$1.3M | - | out (clean 37, ADX 20, RVol 2.1) |
| 24 | **AAPL** | 348.12 | - | **-** | 25 | - | POS +$607.7M | 333.26 | 350 | 330 | +$16.9M | +$894k bull / -$86k bear | out (clean 31, ADX 21, RVol 2.2) |
| 25 | **ARM** | 165.48 | - | **-** | 25 | - | NEG -$5.2M | - | 180 | 180 | +$1.7M | - | out (clean 27, ADX 59, RVol 2.6) |
| 26 | **CRM** | 226.39 | - | **-** | 19 | - | NEG -$14.1M | - | 240 | 220 | +$304k | - | out (clean 34, ADX 21, RVol 2.0) |
| 27 | **NFLX** | 65.89 | - | **-** | 13 | - | POS +$29.8M | 62.12 | 65 | 65 | +$348k | - | out (clean 33, ADX 19, RVol 1.3) |

## Big prints this scan (213)
- **SPY** CALL 740 2026-11-10 (5DTE): 2,000 @ 12.06 = **+$2.4M** BUY | vol 10,091 / OI 44
- **SPY** PUT 760 2026-11-05 (0DTE): 499 @ 15.18 = **+$757k** SELL | vol 74,543 / OI 3,384
- **META** PUT 587.5 2026-11-11 (6DTE): 400 @ 14.32 = **+$573k** BUY | vol 409 / OI 0
- **META** PUT 585 2026-11-11 (6DTE): 400 @ 13.27 = **+$531k** BUY | vol 454 / OI 13
- **SPY** PUT 755 2026-11-05 (0DTE): 499 @ 10.48 = **+$523k** SELL | vol 93,470 / OI 2,900
- **META** PUT 592.5 2026-11-06 (1DTE): 499 @ 10.05 = **+$501k** BUY | vol 4,588 / OI 242
- **SPY** PUT 740 2026-11-06 (1DTE): 1,494 @ 3.26 = **+$487k** SELL | vol 30,382 / OI 24,512
- **META** PUT 592.5 2026-11-06 (1DTE): 449 @ 9.96 = **+$447k** BUY | vol 4,588 / OI 242
- **META** CALL 592.5 2026-11-06 (1DTE): 461 @ 9.68 = **+$446k** SELL | vol 1,286 / OI 26
- **SPY** PUT 755 2026-11-05 (0DTE): 350 @ 10.41 = **+$364k** SELL | vol 93,470 / OI 2,900
- **META** PUT 587.5 2026-11-06 (1DTE): 400 @ 8.29 = **+$332k** BUY | vol 2,642 / OI 337
- **SPY** PUT 735 2026-11-06 (1DTE): 1,494 @ 2.15 = **+$321k** SELL | vol 19,207 / OI 24,589
- **SPY** PUT 760 2026-11-05 (0DTE): 200 @ 15.19 = **+$304k** SELL | vol 74,543 / OI 3,384
- **SPY** PUT 760 2026-11-05 (0DTE): 200 @ 15.01 = **+$300k** SELL | vol 74,543 / OI 3,384
- **SPY** PUT 760 2026-11-05 (0DTE): 200 @ 15.01 = **+$300k** SELL | vol 74,543 / OI 3,384

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 720 2026-11-05 (0DTE): 2,867 traded vs OI 2,619
- **SPY** PUT 701 2026-11-05 (0DTE): 503 traded vs OI 97
- **SPY** CALL 738 2026-11-05 (0DTE): 541 traded vs OI 3
- **SPY** PUT 730 2026-11-06 (1DTE): 14,147 traded vs OI 13,922
- **SPY** CALL 737 2026-11-05 (0DTE): 506 traded vs OI 4
- **SPY** CALL 750 2026-11-11 (6DTE): 572 traded vs OI 82
- **SPY** CALL 736 2026-11-05 (0DTE): 512 traded vs OI 1
- **SPY** CALL 744 2026-11-06 (1DTE): 852 traded vs OI 183
- **SPY** PUT 721 2026-11-06 (1DTE): 2,407 traded vs OI 2,389
- **SPY** PUT 765 2026-11-11 (6DTE): 501 traded vs OI 397
- **SPY** PUT 762 2026-11-11 (6DTE): 511 traded vs OI 13
- **SPY** CALL 766 2026-11-13 (8DTE): 1,674 traded vs OI 1,391
- **SPY** CALL 767 2026-11-13 (8DTE): 863 traded vs OI 812
- **SPY** CALL 751 2026-11-13 (8DTE): 535 traded vs OI 280
- **SPY** PUT 733 2026-11-13 (8DTE): 546 traded vs OI 489

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
