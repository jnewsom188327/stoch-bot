# GEX + FLOW SCAN - Fri Oct 30, 03:55 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 15:02 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 46 puts 0-1DTE > 2 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
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
| 1 | **AAPL** | 344.63 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 50 | none: 81 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (43 contracts' greeks worked out here) | POS +$860.3M | 342.59 | 345 | 340 | +$9.7M | +$64k bull / -$3.0M bear | out (clean 32, ADX 29, RVol 2.5) |
| 2 | **SMCI** | 32.83 | FLIP CROSS up into positive gamma | **CALLS** | 38 | none: 26 calls 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 0 spread ok > 0 liquid (17 contracts' greeks worked out here) | POS +$5.4M | 32.56 | 33 | 32 | -$220k | - | out (clean 30, ADX 45, RVol 2.7) |
| 3 | **COIN** | 141.59 | - | **-** | 29 | - | NEG -$18.5M | - | 150 | 140 | -$5.6M | +$0 bull / -$134k bear | out (clean 27, ADX 42, RVol 4.6) |
| 4 | **DELL** | 422.39 | - | **-** | 26 | - | NEG -$67.4M | - | 440 | 425 | +$7.2M | +$52k bull / -$145k bear | out (clean 34, ADX 26, RVol 2.2) |
| 5 | **MSTR** | 130.45 | - | **-** | 25 | - | NEG -$35.9M | 136.37 | 135 | 130 | -$12.7M | +$0 bull / -$1.1M bear | out (clean 27, ADX 27, RVol 4.0) |
| 6 | **SPY** | 756.10 | - | **-** | 24 | - | NEG -$16.9B | 771.52 | 800 | 755 | +$228.4M | +$0 bull / -$9.7M bear | out (clean 28, ADX 33, RVol 6.0) |
| 7 | **NVDA** | 204.93 | - | **-** | 24 | - | NEG -$508.1M | 211.5 | 210 | 205 | +$29.0M | +$29k bull / -$4.8M bear | out (clean 29, ADX 32, RVol 2.4) |
| 8 | **AMD** | 504.83 | - | **-** | 24 | - | NEG -$205.7M | 517 | 550 | 500 | +$28.2M | +$594k bull / -$943k bear | out (clean 30, ADX 28, RVol 3.2) |
| 9 | **QQQ** | 691.25 | - | **-** | 22 | - | NEG -$12.4B | 729.36 | 720 | 690 | +$56.6M | +$336k bull / -$5.5M bear | out (clean 29, ADX 33, RVol 3.7) |
| 10 | **HOOD** | 84.62 | - | **-** | 22 | - | NEG -$51.9M | - | 85 | 85 | +$272k | +$0 bull / -$101k bear | out (clean 31, ADX 40, RVol 2.2) |
| 11 | **IWM** | 279.36 | - | **-** | 21 | - | NEG -$1.4B | 281.18 | 280 | 270 | +$6.4M | +$0 bull / -$56k bear | out (clean 30, ADX 28, RVol 2.2) |
| 12 | **SMH** | 522.64 | - | **-** | 21 | - | NEG -$568.9M | - | 525 | 520 | -$2.6M | +$149k bull / -$5.4M bear | out (clean 31, ADX 31, RVol 2.4) |
| 13 | **MSFT** | 522.31 | - | **-** | 21 | - | POS +$541.9M | 520.66 | 525 | 520 | +$3.3M | +$609k bull / -$217k bear | out (clean 26, ADX 24, RVol 2.2) |
| 14 | **MU** | 883.10 | - | **-** | 21 | - | NEG -$296.9M | 889.68 | 880 | 880 | +$49.9M | +$0 bull / -$4.3M bear | out (clean 31, ADX 26, RVol 1.9) |
| 15 | **TSLA** | 398.97 | - | **-** | 20 | - | POS +$681.4M | 379.98 | 400 | 397.5 | -$14.2M | +$225k bull / -$6.1M bear | out (clean 31, ADX 23, RVol 2.3) |
| 16 | **META** | 615.73 | - | **-** | 20 | - | NEG -$90.0M | 619.39 | 615 | 615 | +$4.8M | +$0 bull / -$1.3M bear | out (clean 30, ADX 37, RVol 0.9) |
| 17 | **AMZN** | 240.55 | - | **-** | 20 | - | NEG -$227.4M | 245.13 | 250 | 240 | -$7.0M | +$0 bull / -$390k bear | out (clean 30, ADX 22, RVol 1.9) |
| 18 | **PLTR** | 185.47 | - | **-** | 20 | - | NEG -$69.2M | 189.9 | 200 | 185 | -$7.4M | +$0 bull / -$335k bear | out (clean 26, ADX 17, RVol 1.9) |
| 19 | **ORCL** | 130.75 | - | **-** | 20 | - | NEG -$100.5M | 131.78 | 131 | 130 | +$2.1M | +$37k bull / +$0 bear | out (clean 33, ADX 20, RVol 1.5) |
| 20 | **GOOGL** | 280.48 | - | **-** | 19 | - | NEG -$275.3M | - | 280 | 280 | +$1.1M | +$0 bull / -$297k bear | out (clean 33, ADX 30, RVol 1.2) |
| 21 | **BABA** | 98.00 | - | **-** | 19 | - | NEG -$58.0M | 100.14 | 100 | 98 | +$664k | - | out (clean 31, ADX 28, RVol 1.9) |
| 22 | **SHOP** | 158.10 | - | **-** | 17 | - | NEG -$32.9M | - | 160 | 157.5 | +$499k | - | out (clean 28, ADX 32, RVol 3.0) |
| 23 | **NFLX** | 62.11 | - | **-** | 15 | - | NEG -$32.7M | 62.5 | 62 | 62 | +$1.4M | - | out (clean 30, ADX 32, RVol 1.6) |
| 24 | **UBER** | 65.13 | - | **-** | 14 | - | NEG -$53.1M | 65.75 | 65 | 65 | +$474k | - | out (clean 26, ADX 15, RVol 1.2) |
| 25 | **CRM** | 229.10 | - | **-** | 13 | - | NEG -$34.7M | 238.11 | 230 | 230 | +$396k | - | out (clean 27, ADX 29, RVol 1.2) |
| 26 | **ARM** | 206.88 | - | **-** | 11 | - | NEG -$24.4M | 217.62 | 220 | 205 | +$30k | - | out (clean 27, ADX 34, RVol 3.4) |
| 27 | **AVGO** | 325.48 | - | **-** | 9 | - | NEG -$137.5M | 329.45 | 330 | 325 | +$625k | - | out (clean 30, ADX 30, RVol 1.7) |

## Big prints this scan (146)
- **TSLA** CALL 387.5 2026-10-30 (0DTE): 1,000 @ 11.31 = **+$1.1M** SELL | vol 7,109 / OI 3,278
- **TSLA** CALL 387.5 2026-10-30 (0DTE): 1,000 @ 11.30 = **+$1.1M** SELL | vol 7,109 / OI 3,278
- **TSLA** CALL 390 2026-10-30 (0DTE): 1,138 @ 8.63 = **+$982k** SELL | vol 25,675 / OI 7,225
- **TSLA** CALL 390 2026-10-30 (0DTE): 1,000 @ 8.63 = **+$863k** SELL | vol 25,675 / OI 7,225
- **SPY** CALL 750 2026-11-03 (4DTE): 996 @ 7.32 = **+$729k** SELL | vol 37,343 / OI 23
- **SPY** CALL 750 2026-11-03 (4DTE): 1,000 @ 7.25 = **+$725k** SELL | vol 37,343 / OI 23
- **NVDA** PUT 210 2026-10-30 (0DTE): 1,000 @ 7.05 = **+$705k** BUY | vol 26,758 / OI 26,115
- **SPY** CALL 750 2026-11-03 (4DTE): 944 @ 7.40 = **+$699k** SELL | vol 37,343 / OI 23
- **AAPL** PUT 357.5 2026-11-04 (5DTE): 415 @ 15.83 = **+$657k** BUY | vol 1,388 / OI 34
- **AAPL** PUT 357.5 2026-11-04 (5DTE): 415 @ 15.83 = **+$657k** BUY | vol 1,388 / OI 34
- **NVDA** PUT 210 2026-10-30 (0DTE): 868 @ 7.00 = **+$608k** BUY | vol 26,758 / OI 26,115
- **NVDA** PUT 210 2026-10-30 (0DTE): 792 @ 7.30 = **+$578k** BUY | vol 26,758 / OI 26,115
- **NVDA** PUT 210 2026-10-30 (0DTE): 787 @ 7.30 = **+$575k** BUY | vol 26,758 / OI 26,115
- **MSFT** CALL 500 2026-10-30 (0DTE): 200 @ 23.52 = **+$470k** BUY | vol 954 / OI 1,225
- **SPY** CALL 754 2026-11-06 (7DTE): 453 @ 7.96 = **+$361k** SELL | vol 7,397 / OI 33

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 781 2026-11-03 (4DTE): 505 traded vs OI 322
- **SPY** CALL 792 2026-11-06 (7DTE): 660 traded vs OI 533
- **SPY** CALL 794 2026-11-06 (7DTE): 1,163 traded vs OI 1,113
- **SPY** CALL 791 2026-11-06 (7DTE): 905 traded vs OI 791
- **QQQ** PUT 630 2026-11-02 (3DTE): 503 traded vs OI 197
- **QQQ** PUT 682 2026-11-04 (5DTE): 505 traded vs OI 0
- **QQQ** PUT 670 2026-11-12 (13DTE): 523 traded vs OI 0
- **QQQ** CALL 709 2026-11-20 (21DTE): 525 traded vs OI 387
- **QQQ** CALL 690 2026-11-09 (10DTE): 500 traded vs OI 0
- **IWM** PUT 274 2026-11-11 (12DTE): 594 traded vs OI 213
- **IWM** PUT 272 2026-11-13 (14DTE): 5,094 traded vs OI 4,332
- **IWM** PUT 260 2026-11-13 (14DTE): 5,332 traded vs OI 2,201
- **IWM** CALL 293 2026-11-06 (7DTE): 1,664 traded vs OI 1,491
- **SMH** PUT 502.5 2026-11-02 (3DTE): 510 traded vs OI 3
- **NVDA** CALL 225 2026-11-09 (10DTE): 654 traded vs OI 473

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
