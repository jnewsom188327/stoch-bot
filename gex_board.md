# GEX + FLOW SCAN - Thu Nov 12, 01:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:35 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 754P | 0.59 | 0.17 | +10% (1m) | **-71%** (done) | +70% | 755 |
| 09:50 | **HOOD** | **PUTS** | TREND + FLOW | 11/13 79P | 0.55 | 0.36 | +5% (19m) | **-35%** (done) | +92% | 80 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 130C | 0.75 | 0.72 | +4% (60m) | **-4%** (done) | +59% | 126.9 |
| 09:45 | **SMCI** | **PUTS** | TREND + FLOW | 11/13 27P | 0.42 | 0.23 | -5% (6m) | **-45%** (done) | +57% | 27 |
| 09:45 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 753P | 0.79 | 0.31 | +23% (18m) | **-61%** (done) | +51% | 754.88 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:40:08 ET, last candle SPY 13:39, QQQ 13:38 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:03 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (7 today, last 5)
- 12:00 SMCI CALLS: price -0.27 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:55 SMCI CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:50 SMCI CALLS: price -0.48 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:45 SMCI CALLS: price -0.74 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:30 IWM CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **GOOGL** | 301.98 | - | **-** | 22 | - | POS +$138.6M | 288.2 | 300 | 290 | -$5.8M | +$68k bull / -$234k bear | out (clean 30, ADX 38, RVol 0.9) |
| 2 | **UBER** | 70.08 | PINNED between the walls (positive gamma) - chop | **-** | 22 | - | POS +$16.9M | 68.55 | 70 | 70 | -$82k | - | out (clean 31, ADX 16, RVol 0.5) |
| 3 | **AAPL** | 356.15 | - | **-** | 20 | - | POS +$1.1B | 341.25 | 360 | 360 | +$4.2M | +$32k bull / -$311k bear | out (clean 29, ADX 38, RVol 0.5) |
| 4 | **MSFT** | 526.29 | - | **-** | 20 | - | POS +$123.1M | 521.53 | 535 | 520 | -$4.4M | +$158k bull / -$243k bear | out (clean 31, ADX 28, RVol 0.6) |
| 5 | **BABA** | 94.86 | - | **-** | 20 | - | NEG -$18.8M | - | 100 | 100 | +$299k | +$0 bull / -$44k bear | out (clean 28, ADX 18, RVol 0.9) |
| 6 | **AMZN** | 269.52 | PINNED between the walls (positive gamma) - chop | **-** | 18 | - | POS +$515.6M | - | 270 | 270 | -$6.9M | - | out (clean 29, ADX 9, RVol 0.4) |
| 7 | **SPY** | 760.46 | - | **-** | 16 | - | NEG -$588.3M | 760.99 | 760 | 760 | -$135.3M | +$0 bull / -$772k bear | out (clean 30, ADX 11, RVol 0.4) |
| 8 | **NVDA** | 165.91 | - | **-** | 16 | - | NEG -$186.5M | - | 170 | 160 | -$80.0M | +$185k bull / -$2.6M bear | out (clean 32, ADX 12, RVol 0.5) |
| 9 | **AVGO** | 365.03 | - | **-** | 16 | - | POS +$139.1M | - | 350 | 350 | +$8.1M | +$0 bull / -$28k bear | out (clean 34, ADX 12, RVol 0.4) |
| 10 | **DELL** | 376.64 | - | **-** | 16 | - | POS +$4.7M | - | 360 | 380 | +$231k | +$152k bull / +$0 bear | out (clean 37, ADX 30, RVol 0.4) |
| 11 | **QQQ** | 690.78 | - | **-** | 15 | - | NEG -$22.0M | 690.77 | 700 | 680 | -$87.3M | +$0 bull / -$557k bear | out (clean 30, ADX 10, RVol 0.2) |
| 12 | **TSLA** | 392.09 | - | **-** | 15 | - | POS +$381.5M | - | 400 | 380 | +$9.5M | +$0 bull / -$215k bear | out (clean 28, ADX 13, RVol 0.2) |
| 13 | **AMD** | 581.30 | - | **-** | 15 | - | POS +$196.8M | - | 600 | 550 | -$18.1M | +$256k bull / -$1.2M bear | out (clean 34, ADX 15, RVol 0.4) |
| 14 | **META** | 626.19 | - | **-** | 15 | - | POS +$10.6M | 624.69 | 650 | 600 | +$1.5M | +$0 bull / -$97k bear | out (clean 28, ADX 17, RVol 0.4) |
| 15 | **MSTR** | 116.99 | - | **-** | 15 | - | NEG -$29.1M | - | 125 | 110 | -$1.6M | +$0 bull / -$46k bear | out (clean 28, ADX 10, RVol 0.4) |
| 16 | **MU** | 795.50 | - | **-** | 14 | - | POS +$102.8M | - | 800 | 800 | +$2.4M | +$131k bull / -$463k bear | out (clean 31, ADX 16, RVol 0.3) |
| 17 | **SMCI** | 27.05 | - | **-** | 12 | - | NEG -$894k | - | 28 | 25 | +$1.2M | - | out (clean 34, ADX 32, RVol 0.7) |
| 18 | **NFLX** | 63.73 | - | **-** | 7 | - | NEG -$5.6M | 63.98 | 65 | 65 | -$188k | - | out (clean 28, ADX 16, RVol 0.5) |
| 19 | **ARM** | 201.35 | - | **-** | 7 | - | POS +$10.8M | - | 200 | 200 | -$272k | - | out (clean 31, ADX 16, RVol 0.1) |
| 20 | **IWM** | 280.16 | - | **-** | 6 | - | NEG -$1.1B | 282.62 | 285 | 275 | -$754k | - | out (clean 33, ADX 22, RVol 0.7) |
| 21 | **SMH** | 504.08 | - | **-** | 6 | - | NEG -$95.9M | - | 500 | 500 | -$1.8M | - | out (clean 30, ADX 12, RVol 0.3) |
| 22 | **ORCL** | 127.59 | - | **-** | 6 | - | POS +$10.3M | 122.35 | 130 | 125 | -$588k | - | out (clean 30, ADX 12, RVol 0.2) |
| 23 | **CRM** | 217.84 | - | **-** | 6 | - | NEG -$8.5M | - | 220 | 220 | +$41k | - | out (clean 28, ADX 20, RVol 0.2) |
| 24 | **PLTR** | 172.35 | - | **-** | 5 | - | POS +$91.1M | - | 170 | 170 | -$438k | - | out (clean 28, ADX 13, RVol 0.3) |
| 25 | **SHOP** | 148.13 | - | **-** | 5 | - | POS +$4.8M | 143.94 | 150 | 140 | -$1k | - | out (clean 30, ADX 22, RVol 0.4) |
| 26 | **COIN** | 133.15 | - | **-** | 4 | - | POS +$6.3M | 131.34 | 137 | 135 | +$46k | - | out (clean 29, ADX 10, RVol 0.5) |
| 27 | **HOOD** | 83.48 | - | **-** | 4 | - | POS +$14.9M | 79.11 | 85 | 80 | -$98k | - | out (clean 34, ADX 11, RVol 0.7) |

## Big prints this scan (47)
- **MSFT** PUT 525 2026-11-18 (6DTE): 200 @ 6.45 = **+$129k** SELL | vol 1,984 / OI 88
- **QQQ** PUT 685 2026-11-16 (4DTE): 320 @ 3.97 = **+$127k** BUY | vol 4,461 / OI 435
- **NVDA** PUT 160 2026-11-16 (4DTE): 499 @ 2.47 = **+$123k** MID | vol 37,904 / OI 4,794
- **NVDA** PUT 165 2026-11-13 (1DTE): 375 @ 3.02 = **+$113k** SELL | vol 93,593 / OI 19,300
- **NVDA** PUT 162.5 2026-11-13 (1DTE): 499 @ 2.05 = **+$102k** BUY | vol 117,811 / OI 20,581
- **NVDA** PUT 162.5 2026-11-13 (1DTE): 418 @ 2.05 = **+$86k** BUY | vol 117,811 / OI 20,581
- **TSLA** CALL 385 2026-11-16 (4DTE): 70 @ 10.25 = **+$72k** SELL | vol 1,127 / OI 301
- **NVDA** PUT 162.5 2026-11-13 (1DTE): 341 @ 2.03 = **+$69k** MID | vol 117,811 / OI 20,581
- **AMD** CALL 580 2026-11-13 (1DTE): 50 @ 13.10 = **+$66k** BUY | vol 16,500 / OI 977
- **MSFT** PUT 525 2026-11-13 (1DTE): 200 @ 3.25 = **+$65k** BUY | vol 4,000 / OI 1,167
- **NVDA** PUT 160 2026-11-16 (4DTE): 259 @ 2.47 = **+$64k** MID | vol 37,904 / OI 4,794
- **MSFT** PUT 527.5 2026-11-13 (1DTE): 124 @ 4.30 = **+$53k** BUY | vol 2,779 / OI 988
- **MSFT** PUT 527.5 2026-11-13 (1DTE): 121 @ 4.30 = **+$52k** BUY | vol 2,779 / OI 988
- **DELL** CALL 370 2026-11-13 (1DTE): 40 @ 12.40 = **+$50k** BUY | vol 1,600 / OI 623
- **NVDA** PUT 160 2026-11-13 (1DTE): 375 @ 1.32 = **+$50k** MID | vol 211,238 / OI 24,121

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 775 2026-11-16 (4DTE): 2,376 traded vs OI 2,319
- **SPY** PUT 747 2026-11-16 (4DTE): 648 traded vs OI 642
- **SPY** CALL 715 2026-11-13 (1DTE): 501 traded vs OI 55
- **SPY** CALL 760 2026-11-24 (12DTE): 538 traded vs OI 447
- **QQQ** PUT 668 2026-11-16 (4DTE): 626 traded vs OI 291
- **QQQ** CALL 681 2026-11-13 (1DTE): 988 traded vs OI 987
- **QQQ** CALL 694 2026-11-17 (5DTE): 521 traded vs OI 129
- **QQQ** PUT 680 2026-11-17 (5DTE): 503 traded vs OI 350
- **QQQ** PUT 661 2026-11-13 (1DTE): 873 traded vs OI 868
- **QQQ** PUT 663 2026-11-13 (1DTE): 791 traded vs OI 753
- **IWM** CALL 285 2026-11-19 (7DTE): 655 traded vs OI 217
- **IWM** PUT 279 2026-11-16 (4DTE): 1,217 traded vs OI 1,195
- **TSLA** CALL 415 2026-11-16 (4DTE): 1,240 traded vs OI 1,029
- **GOOGL** CALL 320 2026-12-11 (29DTE): 513 traded vs OI 510
- **GOOGL** CALL 320 2026-11-13 (1DTE): 3,775 traded vs OI 3,711

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
