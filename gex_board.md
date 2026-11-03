# GEX + FLOW SCAN - Tue Nov 03, 12:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:00:08 ET, last candle SPY 11:59, QQQ 11:59 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SHOP** | 146.17 | FLOW SURGE | **PUTS** | 50 | none: 23 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | NEG -$3.6M | - | 145 | 148 | -$4.1M | +$0 bull / -$44k bear | out (clean 31, ADX 29, RVol 1.6) |
| 2 | **COIN** | 150.09 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 40 | none: 21 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$21.6M | - | 148 | 150 | -$4.1M | - | out (clean 29, ADX 57, RVol 0.5) |
| 3 | **BABA** | 100.05 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 35 | none: 20 calls 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +4% at the target (needs +20%) | POS +$455k | 99.92 | 102 | 100 | +$244k | - | out (clean 36, ADX 61, RVol 0.3) |
| 4 | **META** | 621.50 | - | **-** | 28 | - | NEG -$33.3M | 626.34 | 650 | 610 | -$17.0M | +$402k bull / -$823k bear | out (clean 28, ADX 44, RVol 0.4) |
| 5 | **ORCL** | 125.82 | - | **-** | 27 | - | NEG -$40.4M | - | 135 | 125 | -$6.9M | +$0 bull / -$117k bear | out (clean 33, ADX 35, RVol 0.4) |
| 6 | **MSTR** | 137.07 | - | **-** | 26 | - | POS +$84.2M | - | 135 | 125 | -$5.1M | +$42k bull / +$0 bear | out (clean 29, ADX 38, RVol 0.6) |
| 7 | **MSFT** | 516.23 | - | **-** | 25 | - | POS +$180.9M | 501.9 | 540 | 500 | -$7.6M | +$34k bull / -$227k bear | out (clean 28, ADX 28, RVol 0.4) |
| 8 | **SMCI** | 31.57 | - | **-** | 21 | - | POS +$2.0M | - | 34.5 | 30 | -$877k | +$191k bull / -$370k bear | out (clean 34, ADX 19, RVol 1.3) |
| 9 | **AVGO** | 332.57 | - | **-** | 20 | - | NEG -$64.1M | - | 340 | 340 | +$2.6M | +$57k bull / -$83k bear | out (clean 31, ADX 24, RVol 0.5) |
| 10 | **TSLA** | 398.80 | - | **-** | 19 | - | POS +$204.9M | - | 400 | 400 | +$15.3M | +$986k bull / -$2.0M bear | out (clean 30, ADX 32, RVol 0.5) |
| 11 | **GOOGL** | 279.08 | - | **-** | 19 | - | NEG -$38.1M | 284.56 | 285 | 290 | +$2.8M | +$0 bull / -$30k bear | out (clean 33, ADX 19, RVol 0.5) |
| 12 | **ARM** | 202.76 | - | **-** | 19 | - | NEG -$6.6M | - | 220 | 200 | -$193k | +$0 bull / -$45k bear | out (clean 25, ADX 20, RVol 0.5) |
| 13 | **NVDA** | 208.56 | - | **-** | 18 | - | POS +$129.0M | 203.65 | 210 | 200 | +$6.3M | +$320k bull / -$291k bear | out (clean 30, ADX 25, RVol 1.1) |
| 14 | **SPY** | 755.39 | - | **-** | 17 | - | NEG -$8.9B | 770.68 | 770 | 750 | -$55.9M | +$2.7M bull / -$1.9M bear | out (clean 30, ADX 17, RVol 0.6) |
| 15 | **IWM** | 281.06 | - | **-** | 17 | - | NEG -$1.1B | 287.12 | 285 | 270 | -$2.6M | +$75k bull / -$139k bear | out (clean 32, ADX 21, RVol 0.6) |
| 16 | **SMH** | 521.62 | - | **-** | 17 | - | NEG -$266.3M | - | 532.5 | 500 | +$784k | +$132k bull / +$0 bear | out (clean 31, ADX 22, RVol 0.5) |
| 17 | **AAPL** | 331.22 | - | **-** | 17 | - | NEG -$401.5M | 343.46 | 350 | 330 | -$7.3M | +$265k bull / -$27k bear | out (clean 31, ADX 22, RVol 0.7) |
| 18 | **AMD** | 490.61 | - | **-** | 17 | - | NEG -$66.6M | - | 520 | 500 | +$2.6M | +$1.3M bull / -$1.2M bear | out (clean 32, ADX 27, RVol 0.8) |
| 19 | **DELL** | 407.86 | - | **-** | 17 | - | NEG -$25.9M | - | 440 | 400 | +$1.0M | +$0 bull / -$1.2M bear | out (clean 33, ADX 19, RVol 0.2) |
| 20 | **PLTR** | 173.23 | - | **-** | 16 | - | NEG -$25.5M | - | 165 | 180 | +$881k | +$64k bull / -$87k bear | out (clean 27, ADX 23, RVol 0.8) |
| 21 | **MU** | 855.66 | - | **-** | 16 | - | NEG -$196.7M | - | 900 | 850 | -$13.1M | +$1.4M bull / -$6.6M bear | out (clean 32, ADX 20, RVol 0.5) |
| 22 | **QQQ** | 686.80 | - | **-** | 15 | - | NEG -$5.0B | - | 700 | 680 | -$22.4M | +$3.2M bull / -$20.5M bear | out (clean 30, ADX 18, RVol 0.7) |
| 23 | **AMZN** | 248.26 | - | **-** | 15 | - | POS +$142.6M | 236.15 | 250 | 250 | -$466k | +$108k bull / +$0 bear | out (clean 33, ADX 19, RVol 0.5) |
| 24 | **HOOD** | 85.06 | - | **-** | 14 | - | NEG -$2.8M | - | 90 | 90 | -$53k | +$93k bull / +$0 bear | out (clean 31, ADX 18, RVol 0.2) |
| 25 | **CRM** | 222.76 | - | **-** | 13 | - | NEG -$13.8M | - | 240 | 220 | -$382k | - | out (clean 30, ADX 18, RVol 0.8) |
| 26 | **NFLX** | 62.40 | - | **-** | 8 | - | NEG -$12.7M | 64.37 | 63 | 60 | -$242k | - | out (clean 27, ADX 20, RVol 0.6) |
| 27 | **UBER** | 66.71 | - | **-** | 7 | - | NEG -$8.8M | - | 70 | 65 | -$90k | - | out (clean 29, ADX 13, RVol 0.6) |

## Big prints this scan (99)
- **QQQ** PUT 676 2026-11-06 (3DTE): 10,000 @ 6.61 = **+$6.6M** BUY | vol 10,296 / OI 3,630
- **QQQ** PUT 668 2026-11-06 (3DTE): 7,000 @ 4.38 = **+$3.1M** BUY | vol 11,675 / OI 0
- **QQQ** PUT 672 2026-11-06 (3DTE): 5,000 @ 5.41 = **+$2.7M** BUY | vol 7,117 / OI 0
- **QQQ** PUT 682 2026-11-06 (3DTE): 2,500 @ 8.78 = **+$2.2M** BUY | vol 6,370 / OI 990
- **QQQ** PUT 664 2026-11-06 (3DTE): 6,000 @ 3.51 = **+$2.1M** BUY | vol 6,267 / OI 0
- **QQQ** PUT 672 2026-11-06 (3DTE): 2,000 @ 5.40 = **+$1.1M** BUY | vol 7,117 / OI 0
- **DELL** CALL 405 2026-11-06 (3DTE): 470 @ 16.05 = **+$754k** SELL | vol 562 / OI 2
- **META** CALL 620 2026-11-04 (1DTE): 400 @ 8.30 = **+$332k** SELL | vol 8,737 / OI 383
- **QQQ** PUT 680 2026-11-05 (2DTE): 499 @ 6.42 = **+$320k** BUY | vol 2,285 / OI 1,258
- **TSLA** PUT 405 2026-11-04 (1DTE): 264 @ 10.25 = **+$271k** BUY | vol 9,032 / OI 419
- **TSLA** CALL 402.5 2026-11-06 (3DTE): 350 @ 7.30 = **+$256k** SELL | vol 4,472 / OI 5,017
- **MU** CALL 860 2026-11-09 (6DTE): 100 @ 24.74 = **+$247k** SELL | vol 305 / OI 2
- **MU** CALL 860 2026-11-06 (3DTE): 100 @ 21.16 = **+$212k** SELL | vol 2,566 / OI 194
- **QQQ** PUT 686 2026-11-04 (1DTE): 260 @ 7.21 = **+$187k** BUY | vol 7,067 / OI 334
- **QQQ** CALL 684 2026-11-03 (0DTE): 573 @ 3.10 = **+$178k** SELL | vol 23,693 / OI 310

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 729 2026-11-03 (0DTE): 834 traded vs OI 809
- **SPY** PUT 716 2026-11-20 (17DTE): 17,022 traded vs OI 13,441
- **QQQ** CALL 682 2026-11-06 (3DTE): 525 traded vs OI 48
- **IWM** PUT 284 2026-11-03 (0DTE): 541 traded vs OI 150
- **AMZN** CALL 262.5 2026-11-04 (1DTE): 501 traded vs OI 239
- **PLTR** CALL 170 2026-11-20 (17DTE): 4,642 traded vs OI 4,508
- **MU** CALL 840 2026-11-06 (3DTE): 512 traded vs OI 104
- **HOOD** CALL 89 2026-11-13 (10DTE): 502 traded vs OI 280

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
