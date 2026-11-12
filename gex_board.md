# GEX + FLOW SCAN - Thu Nov 12, 12:10 PM ET
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
Last 1m check 12:10:08 ET, last candle SPY 12:09, QQQ 12:09 | no errors
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
| 1 | **SMCI** | 26.60 | TREND (flow not with it) | **PUTS** | 52 | 11/13 25.5P @ 0.44 (delta 0.28) = est +134% at 25 | NEG -$1.1M | - | 28 | 25 | +$1.5M | - | SHORT (clean 34, ADX 45, RVol 6.1) |
| 2 | **GOOGL** | 300.69 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 37 | none: 72 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$140.8M | 287.91 | 300 | 290 | -$5.8M | - | out (clean 29, ADX 36, RVol 1.4) |
| 3 | **AMZN** | 269.74 | PINNED between the walls (positive gamma) - chop | **-** | 31 | - | POS +$515.6M | - | 270 | 270 | -$8.4M | +$0 bull / -$408k bear | out (clean 30, ADX 14, RVol 0.5) |
| 4 | **BABA** | 94.75 | - | **-** | 26 | - | NEG -$16.7M | - | 100 | 100 | +$291k | +$62k bull / +$0 bear | out (clean 28, ADX 40, RVol 1.5) |
| 5 | **MSFT** | 528.25 | - | **-** | 21 | - | POS +$190.1M | 520.88 | 535 | 520 | -$4.9M | +$62k bull / +$0 bear | out (clean 31, ADX 30, RVol 0.4) |
| 6 | **NVDA** | 164.38 | - | **-** | 20 | - | NEG -$188.9M | - | 170 | 160 | -$79.4M | +$796k bull / -$3.4M bear | out (clean 32, ADX 22, RVol 1.2) |
| 7 | **AVGO** | 363.88 | - | **-** | 20 | - | POS +$136.2M | - | 350 | 350 | +$6.7M | +$0 bull / -$91k bear | out (clean 35, ADX 26, RVol 1.1) |
| 8 | **DELL** | 371.70 | - | **-** | 20 | - | POS +$4.8M | - | 360 | 340 | -$86k | +$143k bull / +$0 bear | out (clean 36, ADX 25, RVol 2.6) |
| 9 | **MSTR** | 117.50 | - | **-** | 20 | - | NEG -$29.0M | - | 125 | 110 | -$2.0M | +$0 bull / -$75k bear | out (clean 28, ADX 22, RVol 1.4) |
| 10 | **SPY** | 760.95 | - | **-** | 19 | - | NEG -$164.7M | 761.16 | 760 | 760 | -$139.2M | +$0 bull / -$136k bear | out (clean 32, ADX 19, RVol 0.4) |
| 11 | **AMD** | 582.01 | - | **-** | 19 | - | POS +$195.7M | - | 600 | 550 | -$21.7M | +$2.3M bull / -$3.2M bear | out (clean 34, ADX 33, RVol 0.7) |
| 12 | **ARM** | 200.21 | PINNED between the walls (positive gamma) - chop | **-** | 19 | - | POS +$10.2M | - | 200 | 200 | -$258k | - | out (clean 31, ADX 20, RVol 0.2) |
| 13 | **QQQ** | 690.69 | - | **-** | 17 | - | POS +$16.0M | 690.57 | 700 | 680 | -$104.4M | +$562k bull / -$1.5M bear | out (clean 31, ADX 18, RVol 0.4) |
| 14 | **SMH** | 502.11 | - | **-** | 17 | - | NEG -$97.8M | - | 500 | 500 | -$1.3M | +$30k bull / -$79k bear | out (clean 30, ADX 20, RVol 0.5) |
| 15 | **AAPL** | 357.11 | - | **-** | 17 | - | POS +$1.1B | 340.63 | 360 | 360 | +$1.3M | +$39k bull / +$0 bear | out (clean 28, ADX 24, RVol 0.8) |
| 16 | **META** | 625.05 | - | **-** | 17 | - | POS +$4.2M | 624.39 | 650 | 600 | +$1.5M | +$0 bull / -$132k bear | out (clean 28, ADX 28, RVol 0.4) |
| 17 | **TSLA** | 391.10 | - | **-** | 16 | - | POS +$361.7M | - | 400 | 380 | +$9.6M | +$28k bull / -$119k bear | out (clean 29, ADX 17, RVol 0.3) |
| 18 | **MU** | 786.09 | - | **-** | 15 | - | POS +$102.8M | - | 800 | 800 | +$9.0M | +$582k bull / -$1.9M bear | out (clean 31, ADX 18, RVol 0.5) |
| 19 | **UBER** | 69.68 | - | **-** | 10 | - | POS +$15.9M | 68.32 | 70 | 70 | -$81k | - | out (clean 31, ADX 19, RVol 0.4) |
| 20 | **NFLX** | 63.84 | - | **-** | 9 | - | NEG -$4.7M | 64.07 | 65 | 65 | -$201k | - | out (clean 28, ADX 18, RVol 0.6) |
| 21 | **PLTR** | 172.22 | - | **-** | 9 | - | POS +$92.5M | - | 170 | 170 | -$518k | - | out (clean 28, ADX 22, RVol 0.9) |
| 22 | **CRM** | 218.47 | - | **-** | 9 | - | NEG -$8.1M | - | 230 | 220 | -$38k | - | out (clean 29, ADX 26, RVol 0.3) |
| 23 | **SHOP** | 148.52 | - | **-** | 9 | - | POS +$5.1M | 144.02 | 150 | 140 | -$11k | - | out (clean 29, ADX 15, RVol 0.3) |
| 24 | **COIN** | 133.15 | - | **-** | 6 | - | POS +$6.3M | 131.17 | 137 | 135 | +$2k | - | out (clean 29, ADX 25, RVol 1.0) |
| 25 | **ORCL** | 127.10 | - | **-** | 6 | - | POS +$10.7M | 120.89 | 130 | 125 | -$395k | - | out (clean 29, ADX 18, RVol 0.3) |
| 26 | **IWM** | 280.94 | - | **-** | 5 | - | NEG -$716.3M | 282.73 | 285 | 275 | -$1.5M | - | out (clean 34, ADX 21, RVol 0.3) |
| 27 | **HOOD** | 83.39 | - | **-** | 5 | - | POS +$15.3M | 79.11 | 85 | 80 | -$89k | - | out (clean 34, ADX 18, RVol 0.5) |

## Big prints this scan (63)
- **QQQ** PUT 682 2026-11-13 (1DTE): 1,000 @ 1.60 = **+$160k** SELL | vol 11,186 / OI 2,662
- **NVDA** PUT 160 2026-11-18 (6DTE): 258 @ 5.65 = **+$146k** SELL | vol 8,506 / OI 3,836
- **QQQ** CALL 691 2026-11-12 (0DTE): 628 @ 2.15 = **+$135k** BUY | vol 103,306 / OI 387
- **MU** PUT 775 2026-11-13 (1DTE): 150 @ 9.00 = **+$135k** SELL | vol 6,677 / OI 632
- **QQQ** CALL 670 2026-11-13 (1DTE): 60 @ 22.40 = **+$134k** BUY | vol 626 / OI 2,726
- **QQQ** CALL 693 2026-11-12 (0DTE): 950 @ 1.40 = **+$133k** BUY | vol 133,482 / OI 1,504
- **AMD** CALL 570 2026-11-18 (6DTE): 40 @ 31.89 = **+$128k** BUY | vol 648 / OI 91
- **NVDA** CALL 167.5 2026-11-13 (1DTE): 460 @ 2.54 = **+$117k** BUY | vol 102,551 / OI 6,311
- **NVDA** PUT 160 2026-11-18 (6DTE): 126 @ 5.70 = **+$72k** SELL | vol 8,506 / OI 3,836
- **MU** PUT 795 2026-11-13 (1DTE): 37 @ 18.65 = **+$69k** SELL | vol 2,454 / OI 251
- **AMD** CALL 600 2026-11-13 (1DTE): 95 @ 7.00 = **+$66k** BUY | vol 38,350 / OI 3,062
- **BABA** CALL 95 2026-11-13 (1DTE): 500 @ 1.24 = **+$62k** BUY | vol 3,452 / OI 45
- **NVDA** CALL 170 2026-11-18 (6DTE): 93 @ 6.10 = **+$57k** BUY | vol 12,561 / OI 3,097
- **AMD** CALL 600 2026-11-13 (1DTE): 80 @ 7.00 = **+$56k** BUY | vol 38,350 / OI 3,062
- **AMZN** CALL 270 2026-11-13 (1DTE): 250 @ 2.13 = **+$53k** SELL | vol 22,700 / OI 14,969

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 746 2026-11-13 (1DTE): 3,700 traded vs OI 3,676
- **QQQ** PUT 643 2026-11-16 (4DTE): 543 traded vs OI 48
- **QQQ** CALL 693 2026-11-17 (5DTE): 509 traded vs OI 119
- **QQQ** PUT 652 2026-11-16 (4DTE): 695 traded vs OI 304
- **QQQ** PUT 689 2026-11-16 (4DTE): 502 traded vs OI 25
- **QQQ** PUT 690 2026-11-13 (1DTE): 10,721 traded vs OI 10,654
- **NVDA** CALL 148 2026-11-16 (4DTE): 605 traded vs OI 129
- **NVDA** PUT 172.5 2026-11-18 (6DTE): 500 traded vs OI 0
- **AAPL** PUT 345 2026-11-18 (6DTE): 589 traded vs OI 158
- **META** CALL 660 2026-11-13 (1DTE): 2,495 traded vs OI 2,333
- **META** PUT 625 2026-11-16 (4DTE): 504 traded vs OI 200
- **AMZN** PUT 267.5 2026-11-16 (4DTE): 534 traded vs OI 285
- **MSFT** CALL 540 2026-11-27 (15DTE): 968 traded vs OI 837
- **GOOGL** CALL 315 2026-11-13 (1DTE): 1,548 traded vs OI 1,426
- **PLTR** CALL 182.5 2026-11-20 (8DTE): 1,463 traded vs OI 1,272

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
