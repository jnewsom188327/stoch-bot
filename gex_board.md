# GEX + FLOW SCAN - Thu Nov 05, 10:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 4.74 | +617% (36m) | **+508%** | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.23 | -12% (0m) | **-52%** | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.10 | -4% (0m) | **-87%** (done) | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:40:08 ET, last candle SPY 10:39, QQQ 10:39 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:38 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 64 puts 0-1DTE > 1 priced 0.40-0.80 > 0 delta 0.15+ > 0 spread ok > 0 liquid  |
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (18 today, last 5)
- 10:40 ORCL CALLS: price -0.25 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:40 IWM CALLS: price -0.79 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:35 HOOD CALLS: price -0.65 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:35 IWM CALLS: price -0.45 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:30 HOOD CALLS: price -0.77 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMH** | 460.48 | FLOW SURGE | **CALLS** | 67 | none: 92 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$315.6M | - | 505 | 500 | +$24.6M | +$11.6M bull / +$0 bear | SHORT (clean 34, ADX 56, RVol 2.6) |
| 2 | **QQQ** | 658.82 | FLOW SURGE | **CALLS** | 65 | none: 522 calls 0-7DTE > 44 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (154 contracts' greeks worked out here) | NEG -$4.9B | - | 700 | 680 | +$650.9M | +$21.2M bull / -$898k bear | SHORT (clean 34, ADX 60, RVol 3.3) |
| 3 | **MSFT** | 540.36 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 64 | none: 129 puts 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$856.4M | - | 540 | 500 | +$16.8M | +$1.1M bull / -$411k bear | out (clean 32, ADX 51, RVol 2.7) |
| 4 | **SMCI** | 26.73 | FLOW SURGE | **CALLS** | 64 | none: 10 calls 0-7DTE > 3 priced 0.40-0.80 > 3 delta 0.2+ > 2 spread ok > 2 liquid > best one only +2% at the target (needs +20%) (4 contracts' greeks worked out here) | NEG -$2.8M | - | 28 | 27 | +$502k | +$91k bull / +$0 bear | SHORT (clean 36, ADX 56, RVol 2.5) |
| 5 | **AVGO** | 301.57 | FLOW SURGE | **CALLS** | 63 | none: 62 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$122.3M | - | 330 | 300 | +$6.4M | +$152k bull / -$79k bear | out (clean 31, ADX 55, RVol 3.4) |
| 6 | **SPY** | 746.00 | FLOW SURGE | **CALLS** | 61 | none: 667 calls 0-7DTE > 26 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (252 contracts' greeks worked out here) | NEG -$11.3B | 769.9 | 760 | 750 | +$715.9M | +$24.1M bull / +$0 bear | SHORT (clean 34, ADX 61, RVol 2.3) |
| 7 | **IWM** | 277.44 | FLOW SURGE | **CALLS** | 61 | 11/05 279C @ 0.68 (delta 0.32) = est +136% at 280 | NEG -$1.9B | 286.14 | 285 | 270 | +$30.4M | +$1.2M bull / +$0 bear | SHORT (clean 35, ADX 43, RVol 2.6) |
| 8 | **META** | 591.87 | FLOW SURGE | **CALLS** | 60 | none: 135 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$170.4M | - | 650 | 600 | +$39.0M | +$6.4M bull / -$26k bear | SHORT (clean 33, ADX 43, RVol 2.3) |
| 9 | **DELL** | 328.98 | FLOW SURGE | **CALLS** | 60 | none: 19 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$14.2M | - | 360 | 350 | +$6.6M | +$211k bull / -$116k bear | SHORT (clean 34, ADX 50, RVol 1.9) |
| 10 | **AMD** | 417.43 | FLOW SURGE | **CALLS** | 58 | none: 99 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | NEG -$97.3M | - | 430 | 440 | +$39.8M | +$1.6M bull / -$59k bear | out (clean 33, ADX 50, RVol 2.8) |
| 11 | **MU** | 690.28 | FLOW SURGE | **CALLS** | 58 | none: 88 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$92.5M | - | 700 | 750 | +$153.9M | +$12.9M bull / -$1.5M bear | out (clean 32, ADX 67, RVol 4.4) |
| 12 | **MSTR** | 129.36 | FLOW SURGE | **CALLS** | 58 | none: 26 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | POS +$63.0M | - | 135 | 125 | +$3.8M | +$396k bull / +$0 bear | SHORT (clean 34, ADX 66, RVol 3.0) |
| 13 | **SHOP** | 140.16 | TREND (flow not with it) | **PUTS** | 58 | none: 25 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$6.4M | - | 144 | 135 | +$185k | - | SHORT (clean 36, ADX 58, RVol 2.3) |
| 14 | **NVDA** | 186.17 | FLOW SURGE | **CALLS** | 57 | none: 36 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$275.2M | - | 200 | 190 | +$50.9M | +$3.7M bull / -$2.4M bear | out (clean 32, ADX 66, RVol 4.3) |
| 15 | **PLTR** | 156.09 | FLOW SURGE | **CALLS** | 56 | none: 15 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$43.4M | - | 165 | 150 | +$11.9M | +$445k bull / +$0 bear | out (clean 28, ADX 50, RVol 2.0) |
| 16 | **ARM** | 169.89 | FLOW SURGE | **CALLS** | 56 | none: 12 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$7.2M | - | 180 | 180 | +$1.2M | +$27k bull / +$0 bear | out (clean 27, ADX 56, RVol 3.0) |
| 17 | **TSLA** | 348.96 | TREND (flow not with it) | **PUTS** | 52 | none: 76 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$156.1M | - | 370 | 350 | +$86.9M | +$4.6M bull / -$530k bear | SHORT (clean 35, ADX 55, RVol 4.1) |
| 18 | **AMZN** | 256.88 | FLOW SURGE | **CALLS** | 50 | none: 63 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$350.4M | - | 260 | 250 | +$28.9M | +$548k bull / -$27k bear | SHORT (clean 34, ADX 29, RVol 1.9) |
| 19 | **COIN** | 138.19 | FLOW SURGE | **CALLS** | 48 | none: 26 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | POS +$22.7M | - | 142 | 135 | +$1.8M | +$92k bull / +$0 bear | out (clean 33, ADX 56, RVol 1.1) |
| 20 | **ORCL** | 116.68 | FLOW SURGE | **CALLS** | 47 | 11/06 122C @ 0.76 (delta 0.21) = est +104% at 120 | NEG -$57.9M | - | 125 | 120 | +$2.0M | +$99k bull / +$0 bear | out (clean 33, ADX 49, RVol 1.1) |
| 21 | **GOOGL** | 283.80 | FLOW SURGE | **CALLS** | 44 | none: 66 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$22.4M | 281.54 | 285 | 290 | +$8.2M | +$133k bull / +$0 bear | SHORT (clean 35, ADX 25, RVol 1.5) |
| 22 | **HOOD** | 78.02 | - | **-** | 32 | - | NEG -$9.1M | - | 85 | 80 | +$1.8M | +$34k bull / +$0 bear | out (clean 31, ADX 62, RVol 2.9) |
| 23 | **BABA** | 105.86 | - | **-** | 28 | - | POS +$21.2M | - | 110 | 100 | +$1.1M | - | out (clean 37, ADX 25, RVol 2.5) |
| 24 | **AAPL** | 349.05 | - | **-** | 23 | - | POS +$655.0M | 333.96 | 350 | 340 | +$12.6M | +$743k bull / -$783k bear | out (clean 31, ADX 18, RVol 1.8) |
| 25 | **CRM** | 227.11 | - | **-** | 19 | - | NEG -$12.1M | - | 240 | 220 | +$239k | - | out (clean 34, ADX 21, RVol 2.8) |
| 26 | **NFLX** | 65.73 | - | **-** | 14 | - | POS +$31.6M | 62.15 | 65 | 65 | +$320k | - | out (clean 33, ADX 19, RVol 1.3) |
| 27 | **UBER** | 68.64 | - | **-** | 14 | - | POS +$5.3M | 67.87 | 70 | 65 | +$122k | - | out (clean 32, ADX 18, RVol 1.6) |

## Big prints this scan (256)
- **SPY** CALL 750 2026-11-10 (5DTE): 2,000 @ 7.11 = **+$1.4M** BUY | vol 8,408 / OI 289
- **SPY** PUT 768 2026-11-06 (1DTE): 500 @ 19.20 = **+$960k** SELL | vol 3,217 / OI 1,973
- **SPY** CALL 755 2026-11-10 (5DTE): 2,000 @ 4.61 = **+$922k** BUY | vol 8,561 / OI 767
- **QQQ** PUT 672 2026-11-05 (0DTE): 699 @ 11.68 = **+$816k** SELL | vol 25,326 / OI 127
- **SPY** PUT 780 2026-11-10 (5DTE): 224 @ 31.60 = **+$708k** SELL | vol 324 / OI 10
- **SPY** PUT 780 2026-11-09 (4DTE): 210 @ 32.00 = **+$672k** SELL | vol 220 / OI 14
- **QQQ** PUT 668 2026-11-05 (0DTE): 699 @ 8.55 = **+$598k** SELL | vol 30,861 / OI 259
- **SPY** PUT 768 2026-11-11 (6DTE): 281 @ 20.10 = **+$565k** SELL | vol 694 / OI 5
- **META** PUT 595 2026-11-09 (4DTE): 499 @ 11.03 = **+$550k** SELL | vol 1,137 / OI 232
- **META** PUT 620 2026-11-06 (1DTE): 200 @ 23.95 = **+$479k** SELL | vol 1,739 / OI 1,512
- **QQQ** PUT 690 2026-11-05 (0DTE): 138 @ 29.92 = **+$413k** SELL | vol 2,717 / OI 1,635
- **TSLA** PUT 350 2026-11-06 (1DTE): 500 @ 7.95 = **+$398k** SELL | vol 30,191 / OI 4,953
- **TSLA** PUT 350 2026-11-06 (1DTE): 493 @ 7.90 = **+$389k** SELL | vol 30,191 / OI 4,953
- **SPY** PUT 768 2026-11-05 (0DTE): 212 @ 18.16 = **+$385k** SELL | vol 5,023 / OI 0
- **META** PUT 595 2026-11-06 (1DTE): 399 @ 8.90 = **+$355k** SELL | vol 4,800 / OI 1,135

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 730 2026-11-05 (0DTE): 8,635 traded vs OI 7,836
- **SPY** CALL 767 2026-11-11 (6DTE): 521 traded vs OI 31
- **SPY** CALL 766 2026-11-11 (6DTE): 672 traded vs OI 65
- **SPY** PUT 723 2026-11-09 (4DTE): 500 traded vs OI 248
- **SPY** CALL 762 2026-11-10 (5DTE): 675 traded vs OI 141
- **SPY** CALL 754 2026-11-10 (5DTE): 516 traded vs OI 135
- **SPY** CALL 752 2026-11-09 (4DTE): 544 traded vs OI 54
- **SPY** CALL 757 2026-11-09 (4DTE): 1,258 traded vs OI 1,237
- **SPY** CALL 756 2026-11-09 (4DTE): 968 traded vs OI 871
- **SPY** PUT 768 2026-11-11 (6DTE): 694 traded vs OI 5
- **SPY** CALL 756 2026-11-30 (25DTE): 1,223 traded vs OI 1,146
- **SPY** PUT 724 2026-11-20 (15DTE): 41,048 traded vs OI 23,729
- **SPY** CALL 756 2026-11-18 (13DTE): 530 traded vs OI 0
- **SPY** CALL 765 2026-11-30 (25DTE): 2,054 traded vs OI 1,818
- **QQQ** CALL 654 2026-11-05 (0DTE): 647 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
