# GEX + FLOW SCAN - Thu Nov 12, 02:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:35 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 754P | 0.59 | 0.17 | +10% (1m) | **-71%** (done) | +70% | 755 |
| 09:50 | **HOOD** | **PUTS** | TREND + FLOW | 11/13 79P | 0.55 | 0.36 | +5% (19m) | **-35%** (done) | +92% | 80 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 130C | 0.75 | 0.72 | +4% (60m) | **-4%** (done) | +59% | 126.9 |
| 09:45 | **SMCI** | **PUTS** | TREND + FLOW | 11/13 27P | 0.42 | 0.23 | -5% (6m) | **-45%** (done) | +57% | 27 |
| 09:45 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 753P | 0.79 | 0.31 | +23% (18m) | **-61%** (done) | +51% | 754.88 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:20:08 ET, last candle SPY 14:19, QQQ 14:19 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 14:15 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 90 puts 0-1DTE > 6 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 10:03 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (7 today, last 5)
- 12:00 SMCI CALLS: price -0.27 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:55 SMCI CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:50 SMCI CALLS: price -0.48 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:45 SMCI CALLS: price -0.74 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:30 IWM CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AMZN** | 269.52 | PINNED between the walls (positive gamma) - chop | **-** | 31 | - | POS +$501.3M | - | 270 | 270 | -$7.8M | +$0 bull / -$702k bear | out (clean 29, ADX 10, RVol 0.7) |
| 2 | **MSFT** | 524.95 | - | **-** | 21 | - | POS +$86.1M | 520.42 | 535 | 520 | -$4.5M | +$0 bull / -$587k bear | out (clean 32, ADX 37, RVol 0.7) |
| 3 | **GOOGL** | 301.40 | - | **-** | 20 | - | POS +$139.4M | 288.2 | 300 | 290 | -$6.3M | +$0 bull / -$1.9M bear | out (clean 30, ADX 26, RVol 1.1) |
| 4 | **ARM** | 200.25 | PINNED between the walls (positive gamma) - chop | **-** | 19 | - | POS +$10.9M | - | 200 | 200 | -$328k | - | out (clean 31, ADX 20, RVol 0.1) |
| 5 | **SPY** | 759.41 | - | **-** | 18 | - | NEG -$1.2B | 760.94 | 760 | 760 | -$140.8M | +$1.5M bull / -$3.8M bear | out (clean 31, ADX 21, RVol 0.5) |
| 6 | **IWM** | 279.76 | - | **-** | 18 | - | NEG -$1.2B | 282.62 | 285 | 275 | -$829k | +$0 bull / -$88k bear | out (clean 34, ADX 38, RVol 0.6) |
| 7 | **AAPL** | 355.87 | - | **-** | 18 | - | POS +$1.1B | 339.37 | 360 | 360 | +$4.2M | +$40k bull / +$0 bear | out (clean 29, ADX 26, RVol 0.7) |
| 8 | **QQQ** | 689.63 | - | **-** | 16 | - | NEG -$172.0M | 690.42 | 700 | 680 | -$99.3M | +$0 bull / -$1.3M bear | out (clean 31, ADX 18, RVol 0.5) |
| 9 | **NVDA** | 164.72 | - | **-** | 16 | - | NEG -$190.1M | - | 170 | 160 | -$65.4M | +$1.3M bull / -$1.4M bear | out (clean 32, ADX 12, RVol 0.8) |
| 10 | **TSLA** | 390.45 | - | **-** | 16 | - | POS +$359.0M | - | 400 | 380 | +$10.9M | +$289k bull / -$238k bear | out (clean 29, ADX 21, RVol 0.2) |
| 11 | **META** | 623.38 | - | **-** | 16 | - | NEG -$12.8M | 624.43 | 650 | 600 | +$1.5M | +$177k bull / -$36k bear | out (clean 28, ADX 22, RVol 0.4) |
| 12 | **AVGO** | 365.36 | - | **-** | 16 | - | POS +$134.7M | - | 380 | 350 | +$8.2M | +$0 bull / -$90k bear | out (clean 34, ADX 9, RVol 0.7) |
| 13 | **AMD** | 581.29 | - | **-** | 15 | - | POS +$197.7M | - | 600 | 550 | -$21.3M | +$0 bull / -$2.7M bear | out (clean 34, ADX 12, RVol 0.6) |
| 14 | **MU** | 795.68 | - | **-** | 13 | - | POS +$107.1M | - | 800 | 850 | +$885k | +$0 bull / -$1.0M bear | out (clean 31, ADX 12, RVol 0.4) |
| 15 | **SMCI** | 27.42 | - | **-** | 11 | - | POS +$1.2M | 26.73 | 30 | 25 | +$1.1M | - | out (clean 34, ADX 22, RVol 1.4) |
| 16 | **BABA** | 94.72 | - | **-** | 9 | - | NEG -$15.4M | - | 100 | 95 | +$311k | - | out (clean 29, ADX 16, RVol 0.9) |
| 17 | **SMH** | 501.68 | - | **-** | 7 | - | NEG -$105.7M | - | 500 | 500 | -$1.7M | - | out (clean 30, ADX 17, RVol 0.6) |
| 18 | **NFLX** | 63.60 | - | **-** | 7 | - | NEG -$9.9M | 64.06 | 65 | 65 | -$188k | - | out (clean 28, ADX 14, RVol 0.5) |
| 19 | **ORCL** | 127.57 | - | **-** | 6 | - | POS +$11.9M | 121.05 | 130 | 125 | -$627k | - | out (clean 30, ADX 8, RVol 0.5) |
| 20 | **UBER** | 69.70 | - | **-** | 6 | - | POS +$15.4M | 68.51 | 70 | 70 | -$52k | - | out (clean 31, ADX 13, RVol 0.3) |
| 21 | **CRM** | 217.60 | - | **-** | 6 | - | NEG -$8.1M | 228.41 | 220 | 220 | +$37k | - | out (clean 29, ADX 18, RVol 0.1) |
| 22 | **DELL** | 374.85 | - | **-** | 5 | - | POS +$5.2M | - | 360 | 380 | +$304k | - | out (clean 37, ADX 21, RVol 0.3) |
| 23 | **HOOD** | 82.79 | - | **-** | 5 | - | POS +$11.6M | 80.11 | 85 | 80 | -$53k | - | out (clean 34, ADX 16, RVol 0.8) |
| 24 | **SHOP** | 147.61 | - | **-** | 5 | - | POS +$4.1M | 143.87 | 150 | 140 | +$406 | - | out (clean 31, ADX 26, RVol 0.3) |
| 25 | **PLTR** | 172.28 | - | **-** | 4 | - | POS +$93.8M | - | 170 | 170 | -$377k | - | out (clean 28, ADX 10, RVol 0.3) |
| 26 | **COIN** | 132.42 | - | **-** | 4 | - | POS +$3.9M | 131.5 | 137 | 135 | +$61k | - | out (clean 30, ADX 14, RVol 0.4) |
| 27 | **MSTR** | 115.75 | - | **-** | 4 | - | NEG -$33.4M | - | 125 | 110 | -$893k | - | out (clean 28, ADX 12, RVol 0.4) |

## Big prints this scan (44)
- **SPY** PUT 782 2026-11-18 (6DTE): 190 @ 23.84 = **+$453k** BUY | vol 330 / OI 80
- **SPY** PUT 782 2026-11-18 (6DTE): 120 @ 23.28 = **+$279k** BUY | vol 330 / OI 80
- **QQQ** PUT 691 2026-11-12 (0DTE): 829 @ 3.29 = **+$273k** BUY | vol 153,261 / OI 46
- **QQQ** PUT 690 2026-11-12 (0DTE): 829 @ 2.55 = **+$211k** BUY | vol 255,879 / OI 443
- **SPY** PUT 779 2026-11-13 (1DTE): 80 @ 20.48 = **+$164k** BUY | vol 206 / OI 28
- **QQQ** CALL 689 2026-11-12 (0DTE): 1,400 @ 1.05 = **+$147k** SELL | vol 117,098 / OI 311
- **QQQ** PUT 688 2026-11-12 (0DTE): 950 @ 1.25 = **+$119k** BUY | vol 179,279 / OI 89
- **NVDA** CALL 170 2026-11-13 (1DTE): 849 @ 1.36 = **+$115k** BUY | vol 202,833 / OI 11,191
- **AMD** PUT 577.5 2026-11-13 (1DTE): 100 @ 11.50 = **+$115k** BUY | vol 3,133 / OI 10
- **SPY** PUT 775 2026-11-13 (1DTE): 70 @ 15.44 = **+$108k** MID | vol 121 / OI 7
- **SPY** CALL 763 2026-11-18 (6DTE): 300 @ 3.39 = **+$102k** SELL | vol 1,347 / OI 738
- **TSLA** CALL 385 2026-11-16 (4DTE): 94 @ 9.50 = **+$89k** MID | vol 1,346 / OI 301
- **IWM** PUT 281 2026-11-12 (0DTE): 500 @ 1.75 = **+$88k** BUY | vol 44,580 / OI 489
- **MU** PUT 790 2026-11-13 (1DTE): 55 @ 14.15 = **+$78k** BUY | vol 12,240 / OI 457
- **MU** PUT 800 2026-11-13 (1DTE): 40 @ 18.30 = **+$73k** BUY | vol 6,246 / OI 872

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 759 2026-11-17 (5DTE): 549 traded vs OI 82
- **SPY** CALL 766 2026-11-17 (5DTE): 806 traded vs OI 784
- **SPY** PUT 752 2026-11-27 (15DTE): 571 traded vs OI 524
- **SPY** PUT 753 2026-11-27 (15DTE): 606 traded vs OI 495
- **QQQ** PUT 720 2026-11-13 (1DTE): 642 traded vs OI 243
- **QQQ** PUT 725 2026-11-13 (1DTE): 987 traded vs OI 208
- **QQQ** PUT 693 2026-11-17 (5DTE): 500 traded vs OI 14
- **QQQ** PUT 667 2026-11-16 (4DTE): 504 traded vs OI 208
- **QQQ** PUT 745 2026-11-20 (8DTE): 2,871 traded vs OI 1,212
- **IWM** PUT 280 2026-11-17 (5DTE): 519 traded vs OI 328
- **IWM** PUT 270 2026-11-24 (12DTE): 621 traded vs OI 53
- **SMH** PUT 545 2026-11-13 (1DTE): 1,452 traded vs OI 0
- **SMH** CALL 527.5 2026-11-20 (8DTE): 1,234 traded vs OI 1,224
- **TSLA** CALL 420 2026-11-16 (4DTE): 613 traded vs OI 604
- **AMZN** CALL 267.5 2026-11-16 (4DTE): 570 traded vs OI 124

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
