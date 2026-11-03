# GEX + FLOW SCAN - Tue Nov 03, 01:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:00:08 ET, last candle SPY 12:59, QQQ 12:59 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 520.36 | FLOW SURGE | **PUTS** | 37 | none: 123 puts 0-7DTE > 16 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$239.6M | 501.46 | 540 | 500 | -$9.7M | +$0 bull / -$385k bear | out (clean 28, ADX 38, RVol 0.8) |
| 2 | **SHOP** | 148.39 | - | **-** | 30 | - | NEG -$3.6M | - | 145 | 148 | -$4.4M | +$41k bull / -$32k bear | out (clean 33, ADX 16, RVol 0.8) |
| 3 | **BABA** | 99.98 | - | **-** | 29 | - | NEG -$578k | 100.25 | 102 | 100 | +$308k | +$28k bull / +$0 bear | out (clean 36, ADX 52, RVol 0.4) |
| 4 | **ORCL** | 127.54 | - | **-** | 27 | - | NEG -$38.0M | - | 135 | 125 | -$8.8M | +$0 bull / -$252k bear | out (clean 33, ADX 37, RVol 0.5) |
| 5 | **META** | 623.02 | - | **-** | 26 | - | NEG -$19.2M | 626.06 | 650 | 610 | -$18.7M | +$299k bull / +$0 bear | out (clean 28, ADX 40, RVol 0.6) |
| 6 | **TSLA** | 397.45 | - | **-** | 19 | - | POS +$189.5M | - | 400 | 400 | +$14.6M | +$84k bull / -$1.6M bear | out (clean 31, ADX 37, RVol 0.3) |
| 7 | **AVGO** | 332.73 | - | **-** | 18 | - | NEG -$63.7M | - | 340 | 340 | +$2.5M | +$126k bull / +$0 bear | out (clean 31, ADX 16, RVol 0.4) |
| 8 | **SMCI** | 31.62 | - | **-** | 18 | - | POS +$2.0M | - | 34.5 | 30 | -$696k | +$51k bull / +$0 bear | out (clean 33, ADX 14, RVol 1.1) |
| 9 | **AMZN** | 249.15 | - | **-** | 17 | - | POS +$158.9M | 236.07 | 250 | 250 | -$1.4M | +$0 bull / -$310k bear | out (clean 32, ADX 21, RVol 0.6) |
| 10 | **SMH** | 520.91 | - | **-** | 16 | - | NEG -$276.9M | - | 532.5 | 500 | +$970k | +$87k bull / +$0 bear | out (clean 31, ADX 15, RVol 0.7) |
| 11 | **NVDA** | 208.41 | - | **-** | 16 | - | POS +$119.7M | 203.76 | 210 | 200 | +$8.0M | +$158k bull / -$339k bear | out (clean 29, ADX 17, RVol 0.5) |
| 12 | **GOOGL** | 280.42 | - | **-** | 16 | - | NEG -$31.9M | 285.14 | 285 | 290 | +$1.2M | +$61k bull / -$157k bear | out (clean 33, ADX 17, RVol 0.8) |
| 13 | **DELL** | 406.97 | - | **-** | 16 | - | NEG -$25.8M | - | 440 | 400 | +$1.1M | +$28k bull / +$0 bear | out (clean 32, ADX 11, RVol 0.2) |
| 14 | **SPY** | 755.69 | - | **-** | 15 | - | NEG -$8.8B | 770.55 | 770 | 750 | -$70.0M | +$915k bull / -$329k bear | out (clean 29, ADX 13, RVol 0.3) |
| 15 | **AAPL** | 331.27 | - | **-** | 15 | - | NEG -$386.4M | 342.51 | 350 | 330 | -$8.0M | +$41k bull / -$380k bear | out (clean 30, ADX 12, RVol 0.7) |
| 16 | **AMD** | 490.76 | - | **-** | 15 | - | NEG -$66.8M | - | 520 | 500 | +$3.8M | +$1.1M bull / -$159k bear | out (clean 31, ADX 18, RVol 0.5) |
| 17 | **QQQ** | 687.00 | - | **-** | 14 | - | NEG -$5.0B | - | 700 | 680 | -$19.4M | +$377k bull / -$730k bear | out (clean 29, ADX 14, RVol 0.4) |
| 18 | **PLTR** | 174.46 | - | **-** | 14 | - | NEG -$25.3M | - | 165 | 180 | -$808k | +$54k bull / -$29k bear | out (clean 27, ADX 14, RVol 0.3) |
| 19 | **MU** | 851.99 | - | **-** | 14 | - | NEG -$201.9M | - | 900 | 850 | -$11.2M | +$2.5M bull / -$982k bear | out (clean 31, ADX 12, RVol 0.2) |
| 20 | **COIN** | 147.12 | - | **-** | 13 | - | POS +$20.4M | - | 148 | 150 | -$2.6M | - | out (clean 29, ADX 35, RVol 0.2) |
| 21 | **HOOD** | 84.89 | - | **-** | 13 | - | NEG -$2.9M | - | 90 | 85 | -$57k | +$64k bull / +$0 bear | out (clean 31, ADX 13, RVol 0.3) |
| 22 | **MSTR** | 136.02 | - | **-** | 11 | - | POS +$81.3M | - | 135 | 125 | -$4.9M | - | out (clean 29, ADX 20, RVol 0.4) |
| 23 | **CRM** | 223.14 | - | **-** | 11 | - | NEG -$14.0M | - | 240 | 220 | -$371k | - | out (clean 30, ADX 13, RVol 0.6) |
| 24 | **NFLX** | 62.76 | - | **-** | 10 | - | NEG -$10.7M | 64.5 | 63 | 60 | -$513k | - | out (clean 27, ADX 25, RVol 0.3) |
| 25 | **UBER** | 66.53 | - | **-** | 8 | - | NEG -$13.8M | - | 70 | 65 | -$96k | - | out (clean 29, ADX 12, RVol 0.9) |
| 26 | **ARM** | 203.10 | - | **-** | 7 | - | NEG -$6.6M | - | 220 | 200 | -$224k | - | out (clean 25, ADX 12, RVol 0.3) |
| 27 | **IWM** | 280.65 | - | **-** | 5 | - | NEG -$1.1B | 287.05 | 285 | 270 | -$1.9M | - | out (clean 32, ADX 20, RVol 0.4) |

## Big prints this scan (72)
- **QQQ** PUT 670 2026-11-04 (1DTE): 1,854 @ 1.93 = **+$358k** BUY | vol 9,968 / OI 4,179
- **QQQ** PUT 660 2026-11-04 (1DTE): 1,854 @ 0.70 = **+$130k** BUY | vol 8,491 / OI 2,939
- **AMD** PUT 490 2026-11-06 (3DTE): 50 @ 22.70 = **+$114k** BUY | vol 950 / OI 740
- **QQQ** PUT 670 2026-11-04 (1DTE): 553 @ 1.90 = **+$105k** BUY | vol 9,968 / OI 4,179
- **AMD** CALL 505 2026-11-06 (3DTE): 49 @ 16.80 = **+$82k** BUY | vol 504 / OI 290
- **MSFT** CALL 512.5 2026-11-04 (1DTE): 75 @ 8.70 = **+$65k** SELL | vol 3,577 / OI 148
- **MU** PUT 860 2026-11-06 (3DTE): 20 @ 31.30 = **+$63k** BUY | vol 3,022 / OI 672
- **MU** PUT 860 2026-11-06 (3DTE): 19 @ 31.30 = **+$59k** BUY | vol 3,022 / OI 672
- **MU** PUT 860 2026-11-06 (3DTE): 19 @ 31.30 = **+$59k** BUY | vol 3,022 / OI 672
- **MU** PUT 860 2026-11-06 (3DTE): 19 @ 31.30 = **+$59k** BUY | vol 3,022 / OI 672
- **ORCL** CALL 130 2026-11-06 (3DTE): 236 @ 2.48 = **+$59k** SELL | vol 22,300 / OI 3,741
- **AMD** CALL 490 2026-11-06 (3DTE): 25 @ 23.20 = **+$58k** MID | vol 2,166 / OI 257
- **MU** PUT 830 2026-11-04 (1DTE): 61 @ 9.50 = **+$58k** BUY | vol 6,641 / OI 430
- **NVDA** PUT 210 2026-11-04 (1DTE): 155 @ 3.70 = **+$57k** BUY | vol 11,327 / OI 2,044
- **MU** PUT 835 2026-11-06 (3DTE): 31 @ 18.50 = **+$57k** SELL | vol 776 / OI 411

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 738 2026-11-05 (2DTE): 514 traded vs OI 0
- **SPY** CALL 815 2026-11-11 (8DTE): 1,000 traded vs OI 0
- **SPY** CALL 810 2026-11-11 (8DTE): 607 traded vs OI 20
- **SPY** CALL 810 2026-11-10 (7DTE): 600 traded vs OI 112
- **SPY** CALL 805 2026-11-11 (8DTE): 805 traded vs OI 62
- **QQQ** PUT 691 2026-11-04 (1DTE): 517 traded vs OI 514
- **QQQ** CALL 717 2026-11-04 (1DTE): 507 traded vs OI 454
- **AAPL** CALL 345 2026-11-13 (10DTE): 4,676 traded vs OI 2,021
- **AAPL** CALL 357.5 2026-11-06 (3DTE): 4,698 traded vs OI 4,692
- **AAPL** CALL 350 2026-11-27 (24DTE): 939 traded vs OI 834
- **AAPL** PUT 335 2026-11-09 (6DTE): 501 traded vs OI 130
- **GOOGL** PUT 277.5 2026-11-06 (3DTE): 964 traded vs OI 940
- **COIN** CALL 160 2026-11-13 (10DTE): 502 traded vs OI 0
- **ORCL** PUT 117 2026-11-13 (10DTE): 727 traded vs OI 375
- **SHOP** PUT 148 2026-11-06 (3DTE): 1,854 traded vs OI 1,846

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
