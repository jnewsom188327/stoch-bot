# GEX + FLOW SCAN - Tue Nov 03, 12:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:50:08 ET, last candle SPY 12:49, QQQ 12:49 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BABA** | 100.00 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 46 | none: 21 calls 0-7DTE > 2 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +4% at the target (needs +20%) | POS +$11k | 100 | 102 | 100 | +$305k | +$28k bull / +$0 bear | out (clean 36, ADX 53, RVol 0.5) |
| 2 | **COIN** | 147.96 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 35 | none: 22 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$20.6M | - | 148 | 150 | -$3.7M | - | out (clean 28, ADX 38, RVol 0.2) |
| 3 | **SHOP** | 148.01 | - | **-** | 30 | - | NEG -$3.8M | - | 145 | 148 | -$4.4M | +$41k bull / -$32k bear | out (clean 32, ADX 17, RVol 0.9) |
| 4 | **META** | 623.25 | - | **-** | 27 | - | NEG -$15.7M | 625.65 | 650 | 610 | -$18.0M | +$362k bull / +$0 bear | out (clean 28, ADX 42, RVol 0.5) |
| 5 | **MSFT** | 519.19 | - | **-** | 27 | - | POS +$227.5M | 501.24 | 540 | 500 | -$8.7M | +$0 bull / -$216k bear | out (clean 28, ADX 34, RVol 0.6) |
| 6 | **ORCL** | 127.21 | - | **-** | 27 | - | NEG -$38.1M | - | 135 | 125 | -$8.2M | +$0 bull / -$97k bear | out (clean 33, ADX 35, RVol 0.6) |
| 7 | **TSLA** | 397.90 | - | **-** | 20 | - | POS +$194.4M | - | 400 | 400 | +$15.5M | +$724k bull / -$1.9M bear | out (clean 31, ADX 38, RVol 0.4) |
| 8 | **AVGO** | 333.40 | - | **-** | 18 | - | NEG -$44.8M | 352.41 | 340 | 340 | +$2.4M | +$59k bull / +$0 bear | out (clean 31, ADX 18, RVol 0.3) |
| 9 | **SMCI** | 31.59 | - | **-** | 18 | - | POS +$2.0M | - | 34.5 | 30 | -$716k | +$0 bull / -$47k bear | out (clean 33, ADX 16, RVol 0.9) |
| 10 | **IWM** | 280.54 | - | **-** | 16 | - | NEG -$1.2B | 287.08 | 285 | 270 | -$1.4M | +$139k bull / +$0 bear | out (clean 32, ADX 20, RVol 0.6) |
| 11 | **SMH** | 520.52 | - | **-** | 16 | - | NEG -$274.4M | - | 532.5 | 500 | +$1.0M | +$119k bull / +$0 bear | out (clean 31, ADX 16, RVol 0.6) |
| 12 | **NVDA** | 208.45 | - | **-** | 16 | - | POS +$118.5M | 203.72 | 210 | 200 | +$8.2M | +$249k bull / -$221k bear | out (clean 29, ADX 18, RVol 0.4) |
| 13 | **AMD** | 490.88 | - | **-** | 16 | - | NEG -$67.2M | - | 520 | 500 | +$3.8M | +$1.2M bull / +$0 bear | out (clean 31, ADX 21, RVol 0.4) |
| 14 | **AMZN** | 249.23 | - | **-** | 16 | - | POS +$158.4M | 236.11 | 250 | 250 | -$1.0M | +$0 bull / -$319k bear | out (clean 32, ADX 20, RVol 0.6) |
| 15 | **GOOGL** | 280.70 | - | **-** | 16 | - | NEG -$28.1M | 284.95 | 285 | 290 | +$1.2M | +$0 bull / -$157k bear | out (clean 32, ADX 17, RVol 0.7) |
| 16 | **SPY** | 755.89 | - | **-** | 15 | - | NEG -$8.7B | 770.47 | 770 | 750 | -$64.0M | +$1.2M bull / -$329k bear | out (clean 30, ADX 13, RVol 0.3) |
| 17 | **AAPL** | 332.62 | - | **-** | 15 | - | NEG -$372.0M | 343.57 | 350 | 330 | -$8.9M | +$0 bull / -$304k bear | out (clean 31, ADX 13, RVol 0.5) |
| 18 | **PLTR** | 173.95 | - | **-** | 14 | - | NEG -$25.3M | - | 165 | 180 | -$624k | +$180k bull / -$29k bear | out (clean 27, ADX 16, RVol 0.4) |
| 19 | **MU** | 852.60 | - | **-** | 14 | - | NEG -$201.8M | - | 900 | 850 | -$13.0M | +$4.8M bull / +$0 bear | out (clean 31, ADX 13, RVol 0.3) |
| 20 | **QQQ** | 687.24 | - | **-** | 13 | - | NEG -$4.9B | - | 700 | 680 | -$12.0M | +$377k bull / +$0 bear | out (clean 29, ADX 13, RVol 0.3) |
| 21 | **HOOD** | 85.10 | - | **-** | 13 | - | NEG -$2.8M | - | 90 | 90 | -$64k | +$64k bull / +$0 bear | out (clean 31, ADX 15, RVol 0.2) |
| 22 | **MSTR** | 136.19 | - | **-** | 12 | - | POS +$81.1M | - | 135 | 125 | -$4.9M | - | out (clean 29, ADX 22, RVol 0.4) |
| 23 | **NFLX** | 62.73 | - | **-** | 11 | - | NEG -$9.8M | 64.13 | 63 | 60 | -$540k | - | out (clean 26, ADX 24, RVol 0.4) |
| 24 | **CRM** | 222.78 | - | **-** | 11 | - | NEG -$13.8M | - | 240 | 220 | -$366k | - | out (clean 30, ADX 12, RVol 0.5) |
| 25 | **UBER** | 66.88 | - | **-** | 8 | - | NEG -$8.6M | - | 70 | 65 | -$107k | - | out (clean 29, ADX 12, RVol 0.7) |
| 26 | **ARM** | 203.12 | - | **-** | 7 | - | NEG -$6.7M | - | 220 | 200 | -$232k | - | out (clean 25, ADX 14, RVol 0.4) |
| 27 | **DELL** | 407.65 | - | **-** | 6 | - | NEG -$26.2M | - | 440 | 400 | +$1.1M | - | out (clean 32, ADX 12, RVol 0.3) |

## Big prints this scan (61)
- **TSLA** PUT 397.5 2026-11-06 (3DTE): 300 @ 9.40 = **+$282k** BUY | vol 2,550 / OI 1,483
- **QQQ** CALL 690 2026-11-04 (1DTE): 500 @ 5.54 = **+$277k** BUY | vol 11,680 / OI 2,234
- **TSLA** CALL 400 2026-11-04 (1DTE): 385 @ 5.06 = **+$195k** SELL | vol 14,400 / OI 1,213
- **AMD** CALL 490 2026-11-06 (3DTE): 62 @ 24.08 = **+$149k** BUY | vol 2,061 / OI 257
- **MU** CALL 865 2026-11-04 (1DTE): 100 @ 12.65 = **+$126k** BUY | vol 8,863 / OI 743
- **MSFT** CALL 520 2026-11-06 (3DTE): 200 @ 6.30 = **+$126k** SELL | vol 1,199 / OI 1,299
- **GOOGL** PUT 280 2026-11-04 (1DTE): 449 @ 2.70 = **+$121k** BUY | vol 5,175 / OI 684
- **MU** CALL 870 2026-11-04 (1DTE): 100 @ 10.65 = **+$106k** BUY | vol 9,473 / OI 154
- **AAPL** PUT 335 2026-11-04 (1DTE): 165 @ 5.23 = **+$86k** BUY | vol 8,706 / OI 2,490
- **TSLA** CALL 402.5 2026-11-04 (1DTE): 205 @ 4.02 = **+$82k** SELL | vol 18,374 / OI 1,041
- **TSLA** CALL 397.5 2026-11-04 (1DTE): 125 @ 6.24 = **+$78k** SELL | vol 4,070 / OI 1,004
- **TSLA** PUT 400 2026-11-04 (1DTE): 98 @ 7.95 = **+$78k** BUY | vol 31,682 / OI 1,549
- **MU** CALL 870 2026-11-04 (1DTE): 77 @ 9.90 = **+$76k** BUY | vol 9,473 / OI 154
- **AAPL** PUT 340 2026-11-04 (1DTE): 82 @ 9.03 = **+$74k** BUY | vol 4,317 / OI 7,977
- **AMZN** CALL 250 2026-11-09 (6DTE): 182 @ 3.98 = **+$72k** SELL | vol 1,055 / OI 654

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 769 2026-11-05 (2DTE): 502 traded vs OI 0
- **QQQ** CALL 689 2026-11-06 (3DTE): 536 traded vs OI 191
- **QQQ** PUT 656 2026-11-04 (1DTE): 517 traded vs OI 0
- **QQQ** PUT 654 2026-11-03 (0DTE): 1,096 traded vs OI 0
- **TSLA** PUT 390 2026-11-09 (6DTE): 500 traded vs OI 158
- **META** CALL 670 2026-11-04 (1DTE): 500 traded vs OI 276
- **NFLX** PUT 62 2026-11-06 (3DTE): 3,396 traded vs OI 3,393
- **SMCI** PUT 29 2026-11-06 (3DTE): 1,604 traded vs OI 1,577
- **MU** PUT 830 2026-11-06 (3DTE): 675 traded vs OI 662

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
