# GEX + FLOW SCAN - Fri Oct 30, 01:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:00:08 ET, last candle SPY 12:59, QQQ 12:59 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 12:45 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:32 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:31 | SPY | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 45 puts 0-1DTE > 1 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |
| 11:05 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 12:40 NVDA CALLS: under EMA 20 - flow says one way, price says the other
- 11:20 ARM CALLS: under EMA 20 - flow says one way, price says the other
- 11:20 COIN PUTS: price +0.22 over the last 15 min - flow says one way, price says the other
- 11:15 MSTR PUTS: price +1.54 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 11:10 MSTR PUTS: price +1.77 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AMD** | 501.32 | FLOW SURGE | **CALLS** | 47 | none: 160 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (66 contracts' greeks worked out here) | NEG -$175.9M | 522.41 | 520 | 500 | +$33.0M | +$3.2M bull / -$285k bear | out (clean 29, ADX 49, RVol 1.5) |
| 2 | **NVDA** | 203.96 | FLOW SURGE | **CALLS** | 44 | 10/30 205C @ 0.42 (delta 0.31) = est +42% at 205 | NEG -$410.1M | 210.17 | 210 | 205 | +$32.6M | +$1.8M bull / -$38k bear | out (clean 27, ADX 45, RVol 1.1) |
| 3 | **DELL** | 417.78 | - | **-** | 31 | - | NEG -$50.3M | - | 440 | 425 | +$3.9M | +$366k bull / +$0 bear | out (clean 33, ADX 54, RVol 1.6) |
| 4 | **SHOP** | 155.78 | - | **-** | 31 | - | NEG -$15.2M | 162.98 | 150 | 157.5 | +$281k | +$0 bull / -$149k bear | out (clean 27, ADX 44, RVol 2.2) |
| 5 | **COIN** | 139.72 | - | **-** | 29 | - | NEG -$16.2M | - | 140 | 140 | -$3.4M | +$67k bull / +$0 bear | out (clean 27, ADX 43, RVol 2.6) |
| 6 | **SMCI** | 31.82 | - | **-** | 29 | - | NEG -$2.7M | 32.26 | 35 | 32 | +$645k | +$49k bull / +$0 bear | out (clean 30, ADX 49, RVol 0.9) |
| 7 | **TSLA** | 399.27 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$488.5M | 381.25 | 400 | 400 | -$9.6M | +$709k bull / -$412k bear | out (clean 28, ADX 11, RVol 0.7) |
| 8 | **SMH** | 519.95 | - | **-** | 27 | - | NEG -$612.6M | - | 532.5 | 520 | +$6.9M | +$43k bull / +$0 bear | out (clean 30, ADX 53, RVol 1.2) |
| 9 | **QQQ** | 690.54 | - | **-** | 25 | - | NEG -$10.4B | 730.99 | 720 | 690 | +$83.0M | +$4.7M bull / -$167k bear | out (clean 28, ADX 45, RVol 1.8) |
| 10 | **AVGO** | 324.32 | - | **-** | 25 | - | NEG -$165.1M | - | 340 | 320 | +$2.1M | +$59k bull / +$0 bear | out (clean 30, ADX 50, RVol 1.1) |
| 11 | **SPY** | 755.88 | - | **-** | 24 | - | NEG -$15.1B | 771.86 | 800 | 750 | +$124.2M | +$2.1M bull / +$0 bear | out (clean 27, ADX 40, RVol 1.0) |
| 12 | **IWM** | 278.44 | - | **-** | 24 | - | NEG -$1.2B | 281.19 | 278 | 278 | +$10.2M | +$704k bull / +$0 bear | out (clean 28, ADX 42, RVol 0.6) |
| 13 | **MU** | 880.48 | - | **-** | 24 | - | NEG -$284.9M | 932.75 | 880 | 880 | +$58.5M | +$1.1M bull / -$152k bear | out (clean 30, ADX 34, RVol 0.6) |
| 14 | **MSTR** | 131.60 | - | **-** | 24 | - | NEG -$18.7M | 135.49 | 135 | 130 | -$8.5M | +$2.2M bull / -$169k bear | out (clean 28, ADX 14, RVol 2.3) |
| 15 | **HOOD** | 83.49 | - | **-** | 23 | - | NEG -$40.2M | - | 85 | 85 | +$1.4M | +$434k bull / +$0 bear | out (clean 31, ADX 46, RVol 0.6) |
| 16 | **NFLX** | 62.30 | - | **-** | 21 | - | NEG -$22.2M | 62.62 | 62 | 62 | +$1.1M | +$69k bull / -$80k bear | out (clean 31, ADX 12, RVol 0.8) |
| 17 | **ARM** | 203.10 | - | **-** | 20 | - | NEG -$21.3M | - | 205 | 205 | +$771k | - | out (clean 26, ADX 38, RVol 2.1) |
| 18 | **PLTR** | 185.22 | - | **-** | 19 | - | NEG -$74.3M | 192.68 | 185 | 185 | +$1.7M | +$2.5M bull / +$0 bear | out (clean 25, ADX 26, RVol 1.2) |
| 19 | **AAPL** | 346.96 | - | **-** | 18 | - | POS +$577.2M | 341.91 | 350 | 345 | -$3.7M | +$443k bull / -$870k bear | out (clean 31, ADX 14, RVol 1.8) |
| 20 | **AMZN** | 239.07 | - | **-** | 18 | - | NEG -$184.3M | 246.77 | 250 | 240 | -$2.6M | +$518k bull / -$123k bear | out (clean 31, ADX 15, RVol 1.9) |
| 21 | **MSFT** | 521.32 | - | **-** | 18 | - | POS +$473.9M | 515.71 | 525 | 520 | +$3.1M | +$793k bull / -$33k bear | out (clean 26, ADX 16, RVol 0.5) |
| 22 | **GOOGL** | 279.72 | - | **-** | 17 | - | NEG -$253.6M | - | 280 | 280 | -$704k | +$56k bull / -$39k bear | out (clean 32, ADX 25, RVol 0.7) |
| 23 | **ORCL** | 131.05 | - | **-** | 16 | - | POS +$29.1M | 129.33 | 130 | 130 | +$2.7M | - | out (clean 33, ADX 34, RVol 0.6) |
| 24 | **UBER** | 64.93 | - | **-** | 9 | - | NEG -$40.0M | 66.27 | 65 | 65 | +$76k | - | out (clean 28, ADX 12, RVol 0.9) |
| 25 | **BABA** | 98.50 | - | **-** | 7 | - | NEG -$36.5M | 99.51 | 100 | 98 | +$77k | - | out (clean 29, ADX 11, RVol 1.1) |
| 26 | **CRM** | 229.82 | - | **-** | 5 | - | NEG -$23.3M | 236.81 | 240 | 230 | +$12k | - | out (clean 27, ADX 17, RVol 0.8) |
| 27 | **META** | 621.30 | - | **-** | 4 | - | NEG -$15.9M | 621.82 | 625 | 625 | -$411k | - | out (clean 28, ADX 17, RVol 0.5) |

## Big prints this scan (62)
- **AMD** CALL 500 2026-11-06 (7DTE): 250 @ 27.00 = **+$675k** BUY | vol 645 / OI 342
- **AMD** PUT 522.5 2026-10-30 (0DTE): 225 @ 19.90 = **+$448k** SELL | vol 1,135 / OI 615
- **QQQ** PUT 695 2026-11-03 (4DTE): 419 @ 8.00 = **+$335k** SELL | vol 3,494 / OI 890
- **AMD** PUT 522.5 2026-10-30 (0DTE): 164 @ 19.70 = **+$323k** SELL | vol 1,135 / OI 615
- **AMD** PUT 522.5 2026-10-30 (0DTE): 136 @ 19.70 = **+$268k** SELL | vol 1,135 / OI 615
- **SPY** CALL 756 2026-11-02 (3DTE): 500 @ 4.50 = **+$225k** BUY | vol 7,258 / OI 45
- **QQQ** PUT 685 2026-11-03 (4DTE): 509 @ 3.92 = **+$200k** SELL | vol 4,382 / OI 2,236
- **SPY** CALL 756 2026-11-02 (3DTE): 442 @ 4.50 = **+$199k** BUY | vol 7,258 / OI 45
- **MU** CALL 885 2026-10-30 (0DTE): 387 @ 4.90 = **+$190k** BUY | vol 11,600 / OI 369
- **TSLA** PUT 395 2026-11-06 (7DTE): 257 @ 7.00 = **+$180k** SELL | vol 6,842 / OI 2,235
- **SPY** CALL 750 2026-10-30 (0DTE): 200 @ 7.80 = **+$156k** BUY | vol 1,672 / OI 4,510
- **QQQ** PUT 690 2026-11-06 (7DTE): 130 @ 9.40 = **+$122k** SELL | vol 7,351 / OI 13,228
- **QQQ** PUT 690 2026-11-06 (7DTE): 130 @ 9.40 = **+$122k** SELL | vol 7,351 / OI 13,228
- **SPY** PUT 770 2026-11-06 (7DTE): 84 @ 13.58 = **+$114k** SELL | vol 1,931 / OI 4,714
- **QQQ** PUT 690 2026-11-06 (7DTE): 120 @ 9.40 = **+$113k** SELL | vol 7,351 / OI 13,228

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 755 2026-11-06 (7DTE): 977 traded vs OI 907
- **SPY** CALL 785 2026-11-06 (7DTE): 2,699 traded vs OI 2,370
- **QQQ** PUT 676 2026-10-30 (0DTE): 2,459 traded vs OI 2,438
- **QQQ** PUT 673 2026-10-30 (0DTE): 1,218 traded vs OI 1,204
- **QQQ** CALL 713 2026-11-03 (4DTE): 506 traded vs OI 143
- **QQQ** PUT 640 2026-11-06 (7DTE): 1,467 traded vs OI 1,360
- **NVDA** PUT 202.5 2026-11-13 (14DTE): 523 traded vs OI 377
- **NVDA** PUT 192.5 2026-11-06 (7DTE): 1,021 traded vs OI 1,016
- **NVDA** CALL 190 2026-11-06 (7DTE): 684 traded vs OI 681
- **TSLA** PUT 365 2026-10-30 (0DTE): 3,216 traded vs OI 3,213
- **TSLA** PUT 375 2026-10-30 (0DTE): 4,091 traded vs OI 4,053
- **AMD** CALL 545 2026-11-02 (3DTE): 515 traded vs OI 164
- **AMD** CALL 500 2026-11-06 (7DTE): 645 traded vs OI 342
- **META** PUT 595 2026-11-02 (3DTE): 513 traded vs OI 224
- **META** PUT 625 2026-10-30 (0DTE): 3,172 traded vs OI 3,166

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
