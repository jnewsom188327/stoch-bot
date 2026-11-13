# GEX + FLOW SCAN - Fri Nov 13, 11:15 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (11)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:15 | **ARM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/13 180P | 0.79 | 0.68 | -14% (0m) | **-14%** | +122% | 180 |
| 11:14 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/13 667P | 0.70 | 0.77 | +17% (0m) | **+10%** | +21% | 672.05 |
| 10:36 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/13 743P | 0.61 | 0.35 | +13% (1m) | **-43%** | +46% | 747.53 |
| 10:17 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 11/13 683C | 0.75 | 0.15 | -1% (0m) | **-80%** | +60% | 678.58 |
| 10:15 | **ARM** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 182.5P | 0.74 | 1.28 | +169% (50m) | **+73%** | +96% | 183.6 hit |
| 10:15 | **ORCL** | **CALLS** | FLIP CROSS up into positive gamma | 11/13 124C | 0.65 | 0.37 | +89% (28m) | **-43%** | +66% | 123.68 hit |
| 10:10 | **ORCL** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 120P | 0.46 | 0.15 | +7% (5m) | **-67%** (done) | +63% | 121.25 |
| 10:05 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 297.5P | 0.74 | 3.42 | +396% (33m) | **+362%** (done) | +288% | 295 hit |
| 09:55 | **BABA** | **PUTS** | FLOW SURGE | 11/13 94P | 0.51 | 0.43 | +8% (43m) | **-16%** (done) | +49% | 93.36 |
| 09:45 | **UBER** | **CALLS** | TREND + FLOW | 11/13 70C | 0.59 | 0.06 | +0% (1m) | **-90%** (done) | +32% | 70.7 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 127C | 0.46 | 0.22 | +22% (2m) | **-52%** (done) | +48% | 126.38 |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:15:08 ET, last candle SPY 11:14, QQQ 11:14 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:13 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** QQQ261113P00667000 |
| 11:02 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:35 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** SPY261113P00743000 |
| 10:16 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | TURNING your way | **FIRE** QQQ261113C00683000 |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 11:15 HOOD CALLS: price -0.56 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:15 COIN CALLS: price -1.07 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:10 COIN CALLS: under EMA 20 - flow says one way, price says the other
- 11:05 COIN CALLS: price -0.05 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:55 GOOGL CALLS: under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AVGO** | 339.36 | PINNED between the walls (positive gamma) - chop | **-** | 50 | - | POS +$59.0M | - | 340 | 340 | +$23.6M | +$641k bull / +$0 bear | SHORT (clean 36, ADX 51, RVol 0.6) |
| 2 | **COIN** | 126.83 | FLOW SURGE | **CALLS** | 50 | 11/13 129C @ 0.40 (delta 0.22) = est +246% at 130 | NEG -$19.3M | 133.03 | 137 | 130 | +$3.4M | +$107k bull / +$0 bear | out (clean 31, ADX 43, RVol 1.4) |
| 3 | **ARM** | 184.23 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 47 | 11/13 180P @ 0.79 (delta 0.22) = est +122% at 180 | NEG -$1.8M | 187.81 | 185 | 180 | -$121k | - | SHORT (clean 33, ADX 60, RVol 0.8) |
| 4 | **HOOD** | 77.11 | FLOW SURGE | **CALLS** | 46 | 11/13 77C @ 0.72 (delta 0.53) = est +198% at 79.15 | NEG -$10.5M | 79.15 | 81 | 75 | +$2.8M | +$29k bull / +$0 bear | out (clean 36, ADX 60, RVol 1.3) |
| 5 | **DELL** | 332.76 | FLOW SURGE | **CALLS** | 45 | none: 54 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (46 contracts' greeks worked out here) | NEG -$3.3M | 342.88 | 350 | 340 | +$8.1M | +$35k bull / +$0 bear | out (clean 38, ADX 48, RVol 0.7) |
| 6 | **GOOGL** | 294.63 | FLOW SURGE | **CALLS** | 42 | none: 90 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (41 contracts' greeks worked out here) | POS +$187.8M | 289.51 | 300 | 290 | +$19.8M | +$312k bull / -$28k bear | out (clean 32, ADX 32, RVol 1.2) |
| 7 | **AMZN** | 265.25 | PINNED between the walls (positive gamma) - chop | **-** | 40 | - | POS +$420.0M | 252.58 | 265 | 265 | +$8.1M | +$101k bull / -$25k bear | out (clean 30, ADX 34, RVol 0.6) |
| 8 | **NVDA** | 158.99 | FLOW SURGE | **CALLS** | 38 | none: 64 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (29 contracts' greeks worked out here) | NEG -$273.8M | - | 170 | 160 | +$118.5M | +$6.5M bull / -$346k bear | out (clean 31, ADX 22, RVol 0.8) |
| 9 | **META** | 631.67 | FLIP CROSS up into positive gamma | **CALLS** | 33 | none: 185 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (84 contracts' greeks worked out here) | POS +$4.7M | 631.38 | 630 | 625 | +$8.0M | +$0 bull / -$1.6M bear | out (clean 29, ADX 26, RVol 0.8) |
| 10 | **SMH** | 475.17 | - | **-** | 31 | - | NEG -$322.7M | - | 500 | 475 | +$13.5M | +$950k bull / +$0 bear | out (clean 31, ADX 57, RVol 1.6) |
| 11 | **QQQ** | 672.98 | - | **-** | 29 | - | NEG -$2.8B | 687.32 | 680 | 680 | +$315.1M | +$1.9M bull / -$1.6M bear | out (clean 32, ADX 57, RVol 0.6) |
| 12 | **IWM** | 275.90 | - | **-** | 28 | - | NEG -$2.7B | 282.64 | 285 | 275 | +$20.8M | +$2.0M bull / -$408k bear | out (clean 36, ADX 42, RVol 0.8) |
| 13 | **AMD** | 525.07 | - | **-** | 27 | - | POS +$36.3M | - | 550 | 530 | +$73.0M | +$2.7M bull / -$808k bear | out (clean 35, ADX 51, RVol 0.6) |
| 14 | **MU** | 753.09 | - | **-** | 26 | - | NEG -$22.3M | 762.06 | 750 | 750 | +$80.5M | +$4.2M bull / -$964k bear | out (clean 31, ADX 39, RVol 1.1) |
| 15 | **SPY** | 749.58 | - | **-** | 24 | - | NEG -$8.8B | 760.15 | 750 | 750 | +$257.9M | +$2.0M bull / -$797k bear | out (clean 33, ADX 33, RVol 0.6) |
| 16 | **MSTR** | 109.64 | - | **-** | 23 | - | NEG -$41.8M | - | 110 | 110 | +$4.4M | +$257k bull / -$182k bear | out (clean 31, ADX 35, RVol 0.5) |
| 17 | **TSLA** | 387.55 | - | **-** | 21 | - | POS +$259.0M | 374.66 | 400 | 380 | +$52.3M | +$1.1M bull / -$4.8M bear | out (clean 29, ADX 17, RVol 0.6) |
| 18 | **AAPL** | 357.75 | - | **-** | 21 | - | POS +$1.2B | 347.09 | 360 | 360 | +$11.4M | +$831k bull / -$150k bear | out (clean 30, ADX 24, RVol 0.8) |
| 19 | **ORCL** | 122.67 | - | **-** | 21 | - | POS +$6.3M | 121.31 | 130 | 125 | -$612k | +$216k bull / +$0 bear | out (clean 31, ADX 36, RVol 1.2) |
| 20 | **SHOP** | 146.43 | - | **-** | 20 | - | POS +$2.9M | 144.68 | 150 | 140 | -$81k | +$85k bull / +$0 bear | out (clean 32, ADX 22, RVol 0.5) |
| 21 | **PLTR** | 166.62 | - | **-** | 19 | - | POS +$87.4M | 160.35 | 165 | 165 | +$214k | +$147k bull / -$34k bear | out (clean 29, ADX 40, RVol 0.6) |
| 22 | **SMCI** | 26.07 | - | **-** | 19 | - | NEG -$2.7M | - | 27 | 25 | +$396k | - | out (clean 34, ADX 28, RVol 0.7) |
| 23 | **UBER** | 69.47 | - | **-** | 18 | - | POS +$12.2M | 68.88 | 70 | 70 | +$288k | - | out (clean 33, ADX 17, RVol 0.5) |
| 24 | **MSFT** | 523.09 | - | **-** | 17 | - | POS +$94.8M | 520.78 | 535 | 520 | -$1.2M | +$447k bull / -$654k bear | out (clean 32, ADX 25, RVol 1.0) |
| 25 | **CRM** | 216.02 | - | **-** | 16 | - | NEG -$8.5M | 221.18 | 220 | 220 | +$150k | - | out (clean 28, ADX 19, RVol 0.5) |
| 26 | **NFLX** | 62.72 | - | **-** | 11 | - | NEG -$29.2M | 63.57 | 65 | 60 | +$375k | - | out (clean 32, ADX 32, RVol 0.8) |
| 27 | **BABA** | 94.13 | - | **-** | 5 | - | NEG -$19.6M | - | 100 | 95 | -$5k | - | out (clean 28, ADX 24, RVol 0.5) |

## Big prints this scan (122)
- **GOOGL** PUT 290 2026-11-20 (7DTE): 1,250 @ 3.91 = **+$489k** MID | vol 1,722 / OI 18,375
- **NVDA** PUT 160 2026-11-16 (3DTE): 1,077 @ 3.55 = **+$382k** SELL | vol 40,925 / OI 4,240
- **NVDA** PUT 160 2026-11-16 (3DTE): 1,076 @ 3.55 = **+$382k** SELL | vol 40,925 / OI 4,240
- **NVDA** PUT 160 2026-11-16 (3DTE): 767 @ 3.55 = **+$272k** SELL | vol 40,925 / OI 4,240
- **TSLA** CALL 387.5 2026-11-16 (3DTE): 303 @ 6.79 = **+$206k** BUY | vol 3,149 / OI 346
- **MU** CALL 790 2026-11-20 (7DTE): 78 @ 22.38 = **+$175k** BUY | vol 1,192 / OI 618
- **GOOGL** CALL 292.5 2026-11-13 (0DTE): 599 @ 2.87 = **+$172k** BUY | vol 2,966 / OI 6,063
- **QQQ** PUT 702 2026-11-13 (0DTE): 52 @ 27.34 = **+$142k** SELL | vol 191 / OI 375
- **SPY** PUT 748 2026-11-18 (5DTE): 275 @ 5.12 = **+$141k** SELL | vol 732 / OI 705
- **TSLA** CALL 387.5 2026-11-16 (3DTE): 197 @ 6.70 = **+$132k** BUY | vol 3,149 / OI 346
- **SPY** PUT 752 2026-11-13 (0DTE): 400 @ 2.99 = **+$120k** SELL | vol 127,714 / OI 4,070
- **TSLA** CALL 387.5 2026-11-16 (3DTE): 177 @ 6.70 = **+$119k** BUY | vol 3,149 / OI 346
- **GOOGL** CALL 292.5 2026-11-13 (0DTE): 400 @ 2.87 = **+$115k** BUY | vol 2,966 / OI 6,063
- **SPY** CALL 751 2026-11-13 (0DTE): 590 @ 1.83 = **+$108k** BUY | vol 78,096 / OI 2,050
- **NVDA** CALL 160 2026-11-16 (3DTE): 312 @ 3.20 = **+$100k** BUY | vol 17,039 / OI 919

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 743 2026-11-17 (4DTE): 500 traded vs OI 401
- **SPY** CALL 768 2026-11-18 (5DTE): 817 traded vs OI 800
- **QQQ** PUT 647 2026-11-16 (3DTE): 502 traded vs OI 193
- **QQQ** CALL 675 2026-11-18 (5DTE): 685 traded vs OI 261
- **QQQ** PUT 654 2026-11-13 (0DTE): 3,986 traded vs OI 2,539
- **QQQ** CALL 666 2026-11-13 (0DTE): 568 traded vs OI 549
- **IWM** PUT 277 2026-11-18 (5DTE): 521 traded vs OI 138
- **IWM** PUT 270 2026-12-11 (28DTE): 2,052 traded vs OI 701
- **NVDA** CALL 155 2026-11-13 (0DTE): 2,307 traded vs OI 2,225
- **TSLA** CALL 425 2026-11-13 (0DTE): 3,039 traded vs OI 3,035
- **TSLA** PUT 365 2026-11-16 (3DTE): 504 traded vs OI 284
- **AMD** CALL 525 2026-11-13 (0DTE): 1,507 traded vs OI 1,344
- **META** PUT 640 2026-11-13 (0DTE): 1,026 traded vs OI 1,024
- **META** PUT 627.5 2026-11-16 (3DTE): 556 traded vs OI 53
- **MU** PUT 745 2026-11-20 (7DTE): 534 traded vs OI 252

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
