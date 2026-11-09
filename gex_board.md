# GEX + FLOW SCAN - Mon Nov 09, 01:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:04 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/09 754C | 0.41 | 0.23 | -2% (0m) | **-44%** (done) | +28% | 752.23 |
| 10:35 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 272.5C | 0.49 | 0.05 | +2% (2m) | **-90%** (done) | +225% | 273.49 |
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.72 | +51% (23m) | **-6%** (done) | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.02 | +13% (6m) | **-96%** (done) | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:50:08 ET, last candle SPY 13:49, QQQ 13:49 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:03 | SPY | 1m WHIPSAW | R1 | CALLS | TURNING away | **FIRE** SPY261109C00754000 |

## Flow surges NOT fired - price disagreed (17 today, last 5)
- 10:55 AVGO PUTS: price +2.40 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 AVGO PUTS: price +1.16 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 QQQ PUTS: price +0.45 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:35 AVGO PUTS: price +1.05 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:30 QQQ PUTS: price +0.53 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AMD** | 509.38 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 42 | none: 164 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (64 contracts' greeks worked out here) | POS +$19.6M | 502.93 | 510 | 500 | -$62.7M | +$0 bull / -$892k bear | out (clean 32, ADX 42, RVol 0.4) |
| 2 | **META** | 641.57 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 36 | 11/09 645C @ 0.62 (delta 0.23) = est +86% at 645 | POS +$167.1M | 614.91 | 650 | 640 | -$10.8M | +$142k bull / -$288k bear | out (clean 32, ADX 28, RVol 0.4) |
| 3 | **GOOGL** | 290.08 | PINNED between the walls (positive gamma) - chop | **-** | 31 | - | POS +$2.6M | 289.84 | 290 | 290 | +$4.6M | +$65k bull / -$120k bear | out (clean 31, ADX 25, RVol 0.4) |
| 4 | **IWM** | 282.40 | - | **-** | 28 | - | NEG -$652.2M | 284.74 | 283 | 270 | -$23.5M | +$0 bull / -$1.1M bear | out (clean 35, ADX 60, RVol 0.4) |
| 5 | **AAPL** | 350.22 | PINNED between the walls (positive gamma) - chop | **-** | 27 | - | POS +$431.5M | 338.93 | 350 | 350 | -$5.6M | +$0 bull / -$83k bear | out (clean 27, ADX 18, RVol 0.2) |
| 6 | **MU** | 731.36 | FLIP CROSS down into negative gamma | **PUTS** | 26 | none: 190 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (68 contracts' greeks worked out here) | NEG -$19.9M | 739.91 | 750 | 750 | +$1.2M | +$28k bull / -$1.7M bear | out (clean 31, ADX 18, RVol 0.4) |
| 7 | **SPY** | 753.20 | - | **-** | 25 | - | NEG -$6.2B | 761.86 | 750 | 740 | -$318.6M | +$429k bull / -$3.9M bear | out (clean 32, ADX 42, RVol 0.3) |
| 8 | **AVGO** | 319.84 | - | **-** | 23 | - | NEG -$68.4M | - | 340 | 320 | -$7.7M | +$40k bull / -$36k bear | out (clean 31, ADX 32, RVol 0.7) |
| 9 | **QQQ** | 678.31 | - | **-** | 22 | - | NEG -$2.2B | 698.8 | 680 | 680 | -$233.0M | +$0 bull / -$1.5M bear | out (clean 32, ADX 30, RVol 0.4) |
| 10 | **TSLA** | 377.85 | - | **-** | 22 | - | POS +$121.8M | - | 380 | 380 | -$92.9M | +$0 bull / -$1.2M bear | out (clean 34, ADX 17, RVol 0.3) |
| 11 | **AMZN** | 268.40 | - | **-** | 21 | - | POS +$395.4M | - | 270 | 265 | +$20.1M | +$0 bull / -$26k bear | out (clean 34, ADX 13, RVol 0.2) |
| 12 | **NVDA** | 177.32 | - | **-** | 19 | - | NEG -$200.2M | - | 190 | 190 | -$50.0M | +$450k bull / -$1.3M bear | out (clean 34, ADX 22, RVol 1.2) |
| 13 | **HOOD** | 84.11 | - | **-** | 19 | - | NEG -$1.5M | - | 85 | 85 | -$2.3M | +$0 bull / -$57k bear | out (clean 30, ADX 22, RVol 0.4) |
| 14 | **MSTR** | 125.52 | - | **-** | 18 | - | POS +$825k | 124.13 | 135 | 120 | -$1.6M | +$0 bull / -$525k bear | out (clean 30, ADX 26, RVol 0.3) |
| 15 | **PLTR** | 168.66 | - | **-** | 17 | - | POS +$12.2M | - | 165 | 170 | -$2.1M | +$0 bull / -$40k bear | out (clean 30, ADX 20, RVol 0.4) |
| 16 | **MSFT** | 543.95 | - | **-** | 15 | - | POS +$617.2M | - | 550 | 540 | +$930k | +$0 bull / -$63k bear | out (clean 33, ADX 23, RVol 0.2) |
| 17 | **UBER** | 71.03 | - | **-** | 14 | - | POS +$7.5M | 69.08 | 75 | 70 | -$225k | - | out (clean 33, ADX 53, RVol 0.5) |
| 18 | **COIN** | 137.06 | - | **-** | 13 | - | NEG -$6.6M | - | 140 | 135 | -$2.0M | - | out (clean 33, ADX 14, RVol 0.2) |
| 19 | **SMCI** | 28.92 | - | **-** | 12 | - | NEG -$2k | 29.27 | 30 | 30 | -$664k | - | out (clean 30, ADX 25, RVol 0.7) |
| 20 | **SHOP** | 151.45 | - | **-** | 12 | - | POS +$2.1M | - | 150 | 140 | -$84k | - | out (clean 34, ADX 21, RVol 0.1) |
| 21 | **SMH** | 486.07 | - | **-** | 10 | - | NEG -$221.1M | - | 485 | 475 | -$2.8M | - | out (clean 31, ADX 27, RVol 0.2) |
| 22 | **ARM** | 187.07 | - | **-** | 9 | - | NEG -$4.6M | - | 185 | 190 | +$762k | - | out (clean 27, ADX 18, RVol 0.5) |
| 23 | **CRM** | 216.56 | - | **-** | 8 | - | NEG -$11.5M | - | 230 | 220 | -$65k | - | out (clean 34, ADX 20, RVol 0.4) |
| 24 | **DELL** | 347.30 | - | **-** | 7 | - | NEG -$6.5M | - | 350 | 340 | +$422k | - | out (clean 33, ADX 26, RVol 0.4) |
| 25 | **NFLX** | 63.65 | - | **-** | 6 | - | NEG -$18.7M | - | 65 | 65 | +$207k | - | out (clean 30, ADX 17, RVol 0.5) |
| 26 | **BABA** | 105.38 | - | **-** | 6 | - | POS +$2.7M | 103.92 | 110 | 110 | +$128k | - | out (clean 31, ADX 26, RVol 0.3) |
| 27 | **ORCL** | 119.11 | - | **-** | 5 | - | NEG -$26.6M | - | 125 | 125 | -$455k | - | out (clean 30, ADX 14, RVol 0.2) |

## Big prints this scan (28)
- **TSLA** CALL 372.5 2026-11-13 (4DTE): 267 @ 11.20 = **+$299k** SELL | vol 1,311 / OI 435
- **META** CALL 635 2026-11-11 (2DTE): 228 @ 12.65 = **+$288k** SELL | vol 874 / OI 2,118
- **NVDA** CALL 177.5 2026-11-11 (2DTE): 750 @ 3.45 = **+$259k** SELL | vol 24,984 / OI 144
- **QQQ** PUT 679 2026-11-13 (4DTE): 112 @ 9.12 = **+$102k** BUY | vol 896 / OI 420
- **SPY** PUT 752 2026-11-16 (7DTE): 160 @ 6.27 = **+$100k** BUY | vol 919 / OI 180
- **AMD** CALL 510 2026-11-11 (2DTE): 71 @ 12.65 = **+$90k** SELL | vol 1,512 / OI 432
- **MU** CALL 720 2026-11-11 (2DTE): 33 @ 26.40 = **+$87k** SELL | vol 2,236 / OI 227
- **NVDA** PUT 177.5 2026-11-09 (0DTE): 450 @ 1.85 = **+$83k** BUY | vol 144,826 / OI 0
- **AMD** CALL 490 2026-11-13 (4DTE): 22 @ 27.80 = **+$61k** SELL | vol 3,302 / OI 1,648
- **AMD** CALL 505 2026-11-13 (4DTE): 30 @ 19.62 = **+$59k** SELL | vol 1,934 / OI 548
- **TSLA** CALL 360 2026-11-11 (2DTE): 32 @ 18.23 = **+$58k** SELL | vol 1,573 / OI 507
- **AAPL** CALL 335 2026-11-09 (0DTE): 40 @ 14.25 = **+$57k** SELL | vol 256 / OI 560
- **AMD** CALL 500 2026-11-13 (4DTE): 25 @ 22.50 = **+$56k** SELL | vol 7,058 / OI 1,939
- **AMD** PUT 505 2026-11-09 (0DTE): 200 @ 2.77 = **+$55k** BUY | vol 5,695 / OI 57
- **NVDA** CALL 177.5 2026-11-11 (2DTE): 153 @ 3.45 = **+$53k** SELL | vol 24,984 / OI 144

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 779 2026-11-11 (2DTE): 1,831 traded vs OI 243
- **SPY** CALL 780 2026-11-11 (2DTE): 4,200 traded vs OI 2,885
- **SPY** PUT 745 2026-11-17 (8DTE): 645 traded vs OI 427
- **SPY** PUT 735 2026-11-17 (8DTE): 843 traded vs OI 673
- **SPY** PUT 700 2026-11-16 (7DTE): 666 traded vs OI 665
- **QQQ** CALL 700 2026-11-23 (14DTE): 3,959 traded vs OI 0
- **QQQ** CALL 677 2026-11-20 (11DTE): 502 traded vs OI 493
- **SMH** CALL 490 2026-11-11 (2DTE): 500 traded vs OI 95
- **NVDA** PUT 195 2026-11-27 (18DTE): 1,160 traded vs OI 0
- **AMD** CALL 560 2026-11-11 (2DTE): 877 traded vs OI 0
- **AMD** CALL 560 2026-11-13 (4DTE): 1,717 traded vs OI 0
- **GOOGL** PUT 287.5 2026-11-11 (2DTE): 504 traded vs OI 70
- **MU** CALL 710 2026-11-13 (4DTE): 686 traded vs OI 642
- **HOOD** CALL 86 2026-11-20 (11DTE): 511 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
