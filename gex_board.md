# GEX + FLOW SCAN - Fri Oct 30, 12:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:40:08 ET, last candle SPY 12:39, QQQ 12:39 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
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
| 1 | **AMD** | 503.31 | FLOW SURGE | **CALLS** | 56 | none: 160 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (61 contracts' greeks worked out here) | NEG -$156.6M | 518.96 | 517.5 | 500 | +$30.1M | +$4.7M bull / -$128k bear | out (clean 29, ADX 45, RVol 3.0) |
| 2 | **NVDA** | 204.80 | FLOW SURGE | **CALLS** | 49 | 10/30 205C @ 0.66 (delta 0.46) = est +74% at 206 | NEG -$442.2M | 211.65 | 210 | 205 | +$28.8M | +$1.3M bull / -$53k bear | out (clean 27, ADX 43, RVol 1.8) |
| 3 | **COIN** | 140.44 | - | **-** | 30 | - | NEG -$15.7M | - | 140 | 140 | -$3.6M | +$0 bull / -$144k bear | out (clean 27, ADX 44, RVol 2.9) |
| 4 | **ARM** | 203.84 | - | **-** | 29 | - | NEG -$20.6M | - | 220 | 205 | +$546k | +$0 bull / -$45k bear | out (clean 26, ADX 40, RVol 2.2) |
| 5 | **SMH** | 522.68 | - | **-** | 28 | - | NEG -$599.3M | - | 532.5 | 530 | +$6.5M | +$0 bull / -$158k bear | out (clean 30, ADX 52, RVol 1.6) |
| 6 | **ORCL** | 131.99 | - | **-** | 26 | - | POS +$45.3M | 130.42 | 130 | 130 | +$2.3M | +$98k bull / +$0 bear | out (clean 33, ADX 36, RVol 0.9) |
| 7 | **MSTR** | 134.35 | - | **-** | 25 | - | NEG -$19.0M | 142.02 | 135 | 135 | -$9.5M | +$0 bull / -$4.5M bear | out (clean 28, ADX 15, RVol 1.8) |
| 8 | **AVGO** | 325.94 | - | **-** | 24 | - | NEG -$152.7M | - | 330 | 325 | +$1.8M | +$0 bull / -$40k bear | out (clean 29, ADX 50, RVol 0.8) |
| 9 | **MU** | 884.26 | - | **-** | 24 | - | NEG -$263.5M | 925.53 | 900 | 900 | +$55.7M | +$546k bull / -$1.9M bear | out (clean 30, ADX 35, RVol 0.3) |
| 10 | **SPY** | 757.63 | - | **-** | 23 | - | NEG -$14.0B | 771 | 760 | 760 | +$102.7M | +$393k bull / -$4.4M bear | out (clean 27, ADX 40, RVol 0.8) |
| 11 | **QQQ** | 692.70 | - | **-** | 23 | - | NEG -$10.6B | 728.96 | 720 | 690 | +$62.0M | +$1.1M bull / -$2.1M bear | out (clean 28, ADX 45, RVol 1.4) |
| 12 | **IWM** | 279.13 | - | **-** | 23 | - | NEG -$994.6M | 281.09 | 278 | 278 | +$9.3M | +$88k bull / -$174k bear | out (clean 28, ADX 38, RVol 0.4) |
| 13 | **DELL** | 422.28 | - | **-** | 22 | - | NEG -$53.4M | - | 440 | 425 | +$3.2M | - | out (clean 32, ADX 51, RVol 3.5) |
| 14 | **PLTR** | 186.46 | - | **-** | 20 | - | NEG -$67.9M | 191.78 | 185 | 185 | -$3.0M | +$27k bull / +$0 bear | out (clean 25, ADX 24, RVol 1.0) |
| 15 | **SHOP** | 156.01 | - | **-** | 20 | - | NEG -$17.6M | 162.86 | 160 | 157.5 | +$283k | - | out (clean 27, ADX 49, RVol 1.8) |
| 16 | **AAPL** | 347.54 | - | **-** | 19 | - | POS +$649.5M | 343.13 | 350 | 345 | -$4.8M | +$1.1M bull / -$2.1M bear | out (clean 31, ADX 17, RVol 1.8) |
| 17 | **AMZN** | 240.47 | - | **-** | 19 | - | NEG -$157.5M | 245.74 | 250 | 240 | -$5.5M | +$44k bull / -$632k bear | out (clean 31, ADX 15, RVol 1.8) |
| 18 | **SMCI** | 32.15 | - | **-** | 19 | - | NEG -$3.8M | 32.58 | 35 | 32 | +$641k | - | out (clean 29, ADX 48, RVol 0.7) |
| 19 | **MSFT** | 522.19 | - | **-** | 17 | - | POS +$540.2M | 516.51 | 525 | 525 | +$1.5M | +$0 bull / -$124k bear | out (clean 26, ADX 18, RVol 0.7) |
| 20 | **GOOGL** | 280.49 | - | **-** | 16 | - | NEG -$247.4M | - | 280 | 280 | -$1.2M | +$485k bull / +$0 bear | out (clean 32, ADX 19, RVol 0.9) |
| 21 | **TSLA** | 401.13 | - | **-** | 15 | - | POS +$460.3M | 391.7 | 400 | 400 | -$14.8M | +$323k bull / -$698k bear | out (clean 28, ADX 12, RVol 0.6) |
| 22 | **META** | 621.12 | - | **-** | 14 | - | NEG -$19.2M | 621.85 | 625 | 625 | -$1.1M | +$420k bull / -$222k bear | out (clean 28, ADX 15, RVol 0.6) |
| 23 | **NFLX** | 62.38 | - | **-** | 12 | - | NEG -$24.0M | 63.12 | 63 | 62 | +$1.1M | - | out (clean 31, ADX 14, RVol 0.9) |
| 24 | **HOOD** | 83.84 | - | **-** | 12 | - | NEG -$31.7M | - | 85 | 85 | +$726k | - | out (clean 31, ADX 47, RVol 0.7) |
| 25 | **BABA** | 98.92 | - | **-** | 7 | - | NEG -$39.9M | 100.06 | 100 | 99 | +$95k | - | out (clean 29, ADX 12, RVol 0.7) |
| 26 | **UBER** | 65.14 | - | **-** | 6 | - | NEG -$36.4M | 66.14 | 65 | 65 | +$53k | - | out (clean 28, ADX 8, RVol 0.5) |
| 27 | **CRM** | 230.62 | - | **-** | 4 | - | NEG -$20.4M | 234.72 | 230 | 230 | -$36k | - | out (clean 27, ADX 11, RVol 0.6) |

## Big prints this scan (60)
- **QQQ** PUT 685 2026-11-06 (7DTE): 1,500 @ 7.84 = **+$1.2M** BUY | vol 10,361 / OI 6,316
- **AMD** CALL 525 2026-11-06 (7DTE): 459 @ 16.63 = **+$763k** BUY | vol 2,293 / OI 220
- **MU** PUT 880 2026-10-30 (0DTE): 899 @ 5.00 = **+$450k** BUY | vol 33,875 / OI 2,467
- **SPY** PUT 762 2026-11-04 (5DTE): 480 @ 7.90 = **+$379k** BUY | vol 1,157 / OI 1,128
- **QQQ** PUT 685 2026-11-03 (4DTE): 831 @ 4.30 = **+$357k** BUY | vol 3,232 / OI 2,236
- **SPY** PUT 762 2026-11-04 (5DTE): 450 @ 7.90 = **+$356k** BUY | vol 1,157 / OI 1,128
- **SPY** CALL 759 2026-11-04 (5DTE): 500 @ 4.79 = **+$240k** SELL | vol 3,350 / OI 229
- **AAPL** CALL 352.5 2026-11-04 (5DTE): 290 @ 5.45 = **+$158k** MID | vol 1,915 / OI 413
- **AAPL** CALL 352.5 2026-11-04 (5DTE): 270 @ 5.50 = **+$148k** BUY | vol 1,915 / OI 413
- **QQQ** CALL 692 2026-11-02 (3DTE): 248 @ 5.47 = **+$136k** SELL | vol 3,668 / OI 0
- **AMD** PUT 510 2026-11-02 (3DTE): 100 @ 13.43 = **+$134k** SELL | vol 1,484 / OI 164
- **QQQ** CALL 692 2026-11-02 (3DTE): 240 @ 5.44 = **+$131k** SELL | vol 3,668 / OI 0
- **AMD** PUT 505 2026-11-02 (3DTE): 100 @ 10.58 = **+$106k** SELL | vol 812 / OI 85
- **AMD** PUT 505 2026-11-06 (7DTE): 40 @ 25.58 = **+$102k** SELL | vol 412 / OI 485
- **SPY** PUT 745 2026-11-04 (5DTE): 529 @ 1.91 = **+$101k** BUY | vol 1,807 / OI 792

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 737 2026-10-30 (0DTE): 4,817 traded vs OI 4,816
- **SPY** PUT 762 2026-11-04 (5DTE): 1,157 traded vs OI 1,128
- **SPY** PUT 759 2026-11-03 (4DTE): 2,668 traded vs OI 2,651
- **SPY** PUT 723 2026-11-06 (7DTE): 1,913 traded vs OI 387
- **QQQ** PUT 685 2026-11-03 (4DTE): 3,232 traded vs OI 2,236
- **QQQ** PUT 650 2026-11-03 (4DTE): 1,319 traded vs OI 1,019
- **QQQ** CALL 714 2026-11-04 (5DTE): 510 traded vs OI 33
- **QQQ** CALL 701 2026-11-03 (4DTE): 512 traded vs OI 10
- **SMH** CALL 567.5 2026-11-04 (5DTE): 773 traded vs OI 10
- **NVDA** PUT 187.5 2026-11-02 (3DTE): 1,068 traded vs OI 119
- **AAPL** CALL 357.5 2026-11-06 (7DTE): 508 traded vs OI 467
- **AAPL** PUT 317.5 2026-11-04 (5DTE): 518 traded vs OI 215
- **AMD** PUT 507.5 2026-11-02 (3DTE): 504 traded vs OI 73
- **AMD** CALL 502.5 2026-10-30 (0DTE): 733 traded vs OI 86
- **MSFT** CALL 520 2026-11-06 (7DTE): 503 traded vs OI 303

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
