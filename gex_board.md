# GEX + FLOW SCAN - Tue Nov 03, 10:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:50:08 ET, last candle SPY 10:49, QQQ 10:49 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **COIN** | 149.51 | FLOW SURGE | **PUTS** | 48 | none: 21 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$20.7M | - | 148 | 150 | -$2.0M | +$0 bull / -$47k bear | out (clean 28, ADX 59, RVol 1.0) |
| 2 | **ORCL** | 125.85 | FLOW SURGE | **PUTS** | 48 | none: 25 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$40.3M | - | 135 | 125 | -$6.9M | +$0 bull / -$28k bear | out (clean 33, ADX 49, RVol 1.1) |
| 3 | **META** | 619.24 | FLOW SURGE | **PUTS** | 40 | none: 149 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$43.8M | 626.09 | 650 | 610 | -$14.9M | +$0 bull / -$567k bear | out (clean 27, ADX 36, RVol 0.4) |
| 4 | **MSTR** | 137.82 | FLOW SURGE | **PUTS** | 39 | none: 26 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$83.7M | - | 135 | 125 | -$3.8M | +$0 bull / -$2.2M bear | out (clean 28, ADX 40, RVol 1.0) |
| 5 | **SHOP** | 145.44 | - | **-** | 31 | - | NEG -$4.0M | - | 145 | 150 | -$4.1M | - | out (clean 32, ADX 49, RVol 3.5) |
| 6 | **MSFT** | 514.85 | - | **-** | 29 | - | POS +$163.9M | 501.27 | 540 | 500 | -$5.5M | +$240k bull / +$0 bear | out (clean 29, ADX 32, RVol 1.1) |
| 7 | **GOOGL** | 278.33 | TREND (flow not with it) | **PUTS** | 29 | none: 66 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$42.1M | 284.31 | 285 | 290 | +$3.4M | +$210k bull / +$0 bear | SHORT (clean 34, ADX 36, RVol 0.6) |
| 8 | **AVGO** | 334.36 | - | **-** | 24 | - | NEG -$41.5M | 351.43 | 340 | 340 | +$2.6M | +$0 bull / -$171k bear | out (clean 31, ADX 35, RVol 0.6) |
| 9 | **PLTR** | 172.44 | - | **-** | 23 | - | NEG -$25.0M | - | 165 | 180 | -$1.1M | +$46k bull / -$514k bear | out (clean 28, ADX 53, RVol 1.9) |
| 10 | **HOOD** | 85.51 | - | **-** | 22 | - | NEG -$2.4M | - | 90 | 90 | -$651k | +$0 bull / -$31k bear | out (clean 31, ADX 24, RVol 1.0) |
| 11 | **SMH** | 521.76 | - | **-** | 21 | - | NEG -$269.9M | - | 532.5 | 500 | +$983k | +$0 bull / -$35k bear | out (clean 33, ADX 31, RVol 0.9) |
| 12 | **AMD** | 490.14 | - | **-** | 20 | - | NEG -$68.2M | - | 520 | 500 | +$4.6M | +$762k bull / -$422k bear | out (clean 33, ADX 40, RVol 0.6) |
| 13 | **BABA** | 100.64 | - | **-** | 20 | - | POS +$2.2M | 99.94 | 102 | 100 | +$162k | - | out (clean 35, ADX 57, RVol 1.1) |
| 14 | **SPY** | 755.42 | - | **-** | 19 | - | NEG -$8.7B | 770.59 | 770 | 750 | -$45.8M | +$0 bull / -$5.8M bear | out (clean 31, ADX 20, RVol 0.8) |
| 15 | **NVDA** | 207.71 | - | **-** | 19 | - | POS +$104.3M | 203.65 | 210 | 200 | +$4.6M | +$332k bull / -$376k bear | out (clean 31, ADX 35, RVol 0.7) |
| 16 | **AAPL** | 328.95 | - | **-** | 19 | - | NEG -$428.0M | 342.32 | 350 | 330 | +$430k | +$826k bull / +$0 bear | out (clean 32, ADX 35, RVol 1.3) |
| 17 | **AMZN** | 246.00 | - | **-** | 19 | - | POS +$125.6M | 236.26 | 250 | 250 | +$1.3M | +$165k bull / +$0 bear | out (clean 34, ADX 24, RVol 0.7) |
| 18 | **TSLA** | 401.96 | - | **-** | 18 | - | POS +$241.9M | - | 400 | 400 | +$10.6M | +$397k bull / -$1.3M bear | out (clean 30, ADX 19, RVol 0.7) |
| 19 | **DELL** | 409.45 | - | **-** | 17 | - | NEG -$25.9M | - | 440 | 400 | +$1.8M | - | out (clean 35, ADX 31, RVol 0.4) |
| 20 | **MU** | 859.00 | - | **-** | 17 | - | NEG -$193.7M | - | 900 | 850 | -$898k | +$1.8M bull / -$1.3M bear | out (clean 32, ADX 30, RVol 0.6) |
| 21 | **QQQ** | 686.86 | - | **-** | 16 | - | NEG -$5.0B | - | 700 | 680 | -$9.8M | +$663k bull / -$976k bear | out (clean 32, ADX 24, RVol 0.6) |
| 22 | **CRM** | 221.35 | - | **-** | 16 | - | NEG -$14.5M | - | 240 | 220 | -$307k | - | out (clean 28, ADX 40, RVol 0.5) |
| 23 | **IWM** | 281.82 | - | **-** | 12 | - | NEG -$892.6M | 287.12 | 285 | 270 | -$5.0M | - | out (clean 33, ADX 24, RVol 0.8) |
| 24 | **ARM** | 205.12 | - | **-** | 12 | - | NEG -$6.5M | - | 220 | 200 | -$170k | - | out (clean 25, ADX 30, RVol 0.4) |
| 25 | **NFLX** | 62.41 | - | **-** | 11 | - | NEG -$12.9M | 64.31 | 63 | 60 | -$221k | - | out (clean 28, ADX 29, RVol 0.8) |
| 26 | **SMCI** | 31.61 | - | **-** | 10 | - | POS +$2.1M | - | 34.5 | 30 | -$245k | - | out (clean 35, ADX 29, RVol 1.0) |
| 27 | **UBER** | 66.73 | - | **-** | 10 | - | NEG -$8.5M | - | 70 | 65 | -$38k | - | out (clean 29, ADX 21, RVol 0.8) |

## Big prints this scan (69)
- **MSTR** CALL 140 2026-11-06 (3DTE): 2,500 @ 3.03 = **+$758k** SELL | vol 5,164 / OI 2,913
- **MSTR** CALL 141 2026-11-06 (3DTE): 2,500 @ 2.71 = **+$678k** SELL | vol 4,398 / OI 19,333
- **NVDA** PUT 207.5 2026-11-09 (6DTE): 500 @ 4.70 = **+$235k** BUY | vol 1,528 / OI 81
- **SPY** PUT 765 2026-11-04 (1DTE): 204 @ 11.09 = **+$226k** BUY | vol 347 / OI 1,486
- **AAPL** CALL 325 2026-11-06 (3DTE): 200 @ 7.90 = **+$158k** BUY | vol 997 / OI 419
- **SPY** PUT 760 2026-11-04 (1DTE): 204 @ 7.34 = **+$150k** BUY | vol 1,143 / OI 2,103
- **META** CALL 625 2026-11-04 (1DTE): 249 @ 4.52 = **+$113k** SELL | vol 3,861 / OI 334
- **MU** CALL 860 2026-11-06 (3DTE): 40 @ 26.85 = **+$107k** BUY | vol 1,207 / OI 194
- **AMZN** CALL 245 2026-11-06 (3DTE): 200 @ 5.05 = **+$101k** BUY | vol 510 / OI 10,335
- **MU** PUT 840 2026-11-04 (1DTE): 100 @ 9.50 = **+$95k** SELL | vol 5,103 / OI 244
- **MU** PUT 860 2026-11-06 (3DTE): 32 @ 25.25 = **+$81k** SELL | vol 1,208 / OI 672
- **AAPL** PUT 335 2026-11-04 (1DTE): 100 @ 7.20 = **+$72k** MID | vol 6,060 / OI 2,490
- **TSLA** CALL 400 2026-11-04 (1DTE): 100 @ 7.00 = **+$70k** SELL | vol 4,860 / OI 1,213
- **AMZN** PUT 247.5 2026-11-04 (1DTE): 200 @ 3.20 = **+$64k** SELL | vol 1,875 / OI 158
- **TSLA** CALL 407.5 2026-11-06 (3DTE): 99 @ 6.00 = **+$59k** SELL | vol 1,041 / OI 3,487

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 743 2026-11-03 (0DTE): 506 traded vs OI 16
- **SPY** CALL 750 2026-11-04 (1DTE): 585 traded vs OI 567
- **SPY** PUT 758 2026-11-04 (1DTE): 3,831 traded vs OI 3,815
- **QQQ** CALL 720 2026-11-09 (6DTE): 1,260 traded vs OI 1,120
- **QQQ** CALL 706 2026-11-04 (1DTE): 752 traded vs OI 549
- **QQQ** PUT 667 2026-11-04 (1DTE): 501 traded vs OI 496
- **SMH** PUT 505 2026-11-13 (10DTE): 643 traded vs OI 191
- **NVDA** CALL 210 2026-11-11 (8DTE): 522 traded vs OI 179
- **AAPL** PUT 300 2026-11-06 (3DTE): 2,470 traded vs OI 2,398
- **AAPL** CALL 332.5 2026-11-13 (10DTE): 506 traded vs OI 58
- **AMD** CALL 485 2026-11-13 (10DTE): 500 traded vs OI 98
- **AMD** PUT 470 2026-11-04 (1DTE): 605 traded vs OI 310
- **AMD** CALL 510 2026-11-04 (1DTE): 599 traded vs OI 194
- **META** PUT 595 2026-11-04 (1DTE): 523 traded vs OI 160
- **MSFT** PUT 495 2026-11-04 (1DTE): 507 traded vs OI 402

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
