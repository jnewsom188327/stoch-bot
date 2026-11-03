# GEX + FLOW SCAN - Tue Nov 03, 01:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:50:08 ET, last candle SPY 13:49, QQQ 13:49 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 521.02 | FLOW SURGE | **PUTS** | 37 | none: 126 puts 0-7DTE > 14 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (13 contracts' greeks worked out here) | POS +$254.4M | 501.97 | 540 | 500 | -$12.1M | +$0 bull / -$130k bear | out (clean 29, ADX 42, RVol 0.7) |
| 2 | **ORCL** | 127.17 | - | **-** | 25 | - | NEG -$38.9M | - | 135 | 125 | -$9.6M | +$356k bull / +$0 bear | out (clean 33, ADX 32, RVol 0.4) |
| 3 | **META** | 623.21 | - | **-** | 23 | - | NEG -$20.1M | 625.82 | 650 | 610 | -$17.0M | +$282k bull / -$86k bear | out (clean 28, ADX 30, RVol 0.4) |
| 4 | **AMZN** | 250.83 | - | **-** | 22 | - | POS +$174.5M | - | 250 | 250 | -$4.1M | +$90k bull / -$345k bear | out (clean 33, ADX 39, RVol 0.7) |
| 5 | **NFLX** | 62.98 | - | **-** | 22 | - | NEG -$7.9M | 64.42 | 63 | 60 | -$562k | +$0 bull / -$50k bear | out (clean 28, ADX 32, RVol 0.6) |
| 6 | **SHOP** | 147.66 | - | **-** | 18 | - | NEG -$4.0M | - | 145 | 148 | -$4.3M | - | out (clean 34, ADX 14, RVol 1.0) |
| 7 | **SPY** | 756.08 | - | **-** | 17 | - | NEG -$8.0B | 769.96 | 770 | 750 | -$77.9M | +$0 bull / -$732k bear | out (clean 29, ADX 20, RVol 0.7) |
| 8 | **IWM** | 281.10 | - | **-** | 17 | - | NEG -$1.1B | 286.94 | 285 | 270 | -$5.2M | +$311k bull / -$652k bear | out (clean 32, ADX 19, RVol 0.6) |
| 9 | **TSLA** | 398.64 | - | **-** | 16 | - | POS +$209.2M | - | 400 | 400 | +$14.3M | +$0 bull / -$588k bear | out (clean 31, ADX 21, RVol 0.4) |
| 10 | **GOOGL** | 280.07 | - | **-** | 16 | - | NEG -$34.6M | 285.04 | 285 | 290 | +$2.2M | +$184k bull / +$0 bear | out (clean 32, ADX 16, RVol 0.3) |
| 11 | **PLTR** | 175.70 | - | **-** | 16 | - | NEG -$24.9M | - | 165 | 180 | -$1.7M | +$0 bull / -$218k bear | out (clean 27, ADX 20, RVol 0.6) |
| 12 | **SMH** | 519.96 | - | **-** | 15 | - | NEG -$278.6M | - | 532.5 | 500 | +$984k | +$25k bull / +$0 bear | out (clean 31, ADX 12, RVol 0.5) |
| 13 | **NVDA** | 207.94 | - | **-** | 15 | - | POS +$110.0M | 203.81 | 210 | 200 | +$9.5M | +$293k bull / -$61k bear | out (clean 29, ADX 13, RVol 0.4) |
| 14 | **AMD** | 490.89 | - | **-** | 15 | - | NEG -$68.2M | - | 520 | 500 | +$2.5M | +$304k bull / -$105k bear | out (clean 31, ADX 15, RVol 0.6) |
| 15 | **QQQ** | 687.50 | - | **-** | 14 | - | NEG -$4.9B | - | 700 | 680 | -$14.5M | +$366k bull / -$106k bear | out (clean 29, ADX 16, RVol 0.4) |
| 16 | **AAPL** | 331.70 | - | **-** | 14 | - | NEG -$378.6M | 342.51 | 350 | 330 | -$7.7M | +$124k bull / +$0 bear | out (clean 30, ADX 12, RVol 0.5) |
| 17 | **MU** | 857.55 | - | **-** | 14 | - | NEG -$198.2M | - | 900 | 850 | -$17.6M | +$0 bull / -$2.6M bear | out (clean 31, ADX 10, RVol 0.4) |
| 18 | **BABA** | 100.27 | - | **-** | 14 | - | POS +$960k | 99.94 | 102 | 100 | +$245k | - | out (clean 36, ADX 31, RVol 0.5) |
| 19 | **HOOD** | 85.19 | - | **-** | 13 | - | NEG -$2.7M | - | 90 | 90 | -$53k | +$0 bull / -$34k bear | out (clean 30, ADX 11, RVol 0.5) |
| 20 | **CRM** | 223.03 | - | **-** | 13 | - | NEG -$14.0M | - | 240 | 220 | -$368k | - | out (clean 29, ADX 15, RVol 1.4) |
| 21 | **COIN** | 146.51 | - | **-** | 11 | - | POS +$20.8M | - | 148 | 150 | -$2.3M | - | out (clean 30, ADX 30, RVol 0.3) |
| 22 | **MSTR** | 136.16 | - | **-** | 9 | - | POS +$82.5M | - | 135 | 125 | -$4.7M | - | out (clean 29, ADX 14, RVol 0.1) |
| 23 | **AVGO** | 333.24 | - | **-** | 8 | - | NEG -$62.3M | - | 340 | 340 | +$3.0M | - | out (clean 31, ADX 12, RVol 0.3) |
| 24 | **SMCI** | 31.63 | - | **-** | 8 | - | POS +$2.0M | - | 34.5 | 30 | -$540k | - | out (clean 33, ADX 14, RVol 1.4) |
| 25 | **UBER** | 66.76 | - | **-** | 8 | - | NEG -$8.7M | - | 70 | 65 | -$284k | - | out (clean 29, ADX 14, RVol 0.5) |
| 26 | **DELL** | 408.74 | - | **-** | 5 | - | NEG -$25.8M | - | 440 | 400 | +$655k | - | out (clean 32, ADX 12, RVol 0.2) |
| 27 | **ARM** | 202.43 | - | **-** | 5 | - | NEG -$6.7M | - | 220 | 200 | -$151k | - | out (clean 25, ADX 10, RVol 0.5) |

## Big prints this scan (66)
- **SPY** CALL 760 2026-11-04 (1DTE): 1,713 @ 2.60 = **+$445k** SELL | vol 24,249 / OI 2,273
- **ORCL** CALL 130 2026-11-06 (3DTE): 1,179 @ 2.55 = **+$301k** BUY | vol 30,396 / OI 3,741
- **QQQ** CALL 680 2026-11-04 (1DTE): 200 @ 12.02 = **+$240k** BUY | vol 2,010 / OI 191
- **MU** PUT 860 2026-11-04 (1DTE): 100 @ 20.84 = **+$208k** BUY | vol 9,321 / OI 273
- **IWM** CALL 280 2026-11-03 (0DTE): 1,498 @ 1.24 = **+$186k** BUY | vol 43,066 / OI 1,006
- **SPY** CALL 765 2026-11-04 (1DTE): 1,713 @ 1.04 = **+$178k** SELL | vol 22,339 / OI 5,211
- **MU** CALL 850 2026-11-04 (1DTE): 100 @ 17.70 = **+$177k** SELL | vol 5,396 / OI 64
- **QQQ** CALL 700 2026-11-06 (3DTE): 335 @ 4.83 = **+$162k** MID | vol 10,874 / OI 13,477
- **MU** PUT 850 2026-11-04 (1DTE): 100 @ 15.69 = **+$157k** BUY | vol 13,308 / OI 414
- **TSLA** CALL 410 2026-11-06 (3DTE): 300 @ 4.45 = **+$134k** SELL | vol 5,329 / OI 9,718
- **MU** CALL 860 2026-11-04 (1DTE): 100 @ 12.85 = **+$128k** SELL | vol 10,752 / OI 60
- **QQQ** PUT 690 2026-11-03 (0DTE): 450 @ 2.80 = **+$126k** SELL | vol 14,484 / OI 3,245
- **GOOGL** PUT 280 2026-11-04 (1DTE): 466 @ 2.53 = **+$118k** SELL | vol 7,821 / OI 684
- **NVDA** CALL 212.5 2026-11-06 (3DTE): 498 @ 2.21 = **+$110k** BUY | vol 10,287 / OI 36,302
- **MU** CALL 855 2026-11-04 (1DTE): 50 @ 16.14 = **+$81k** SELL | vol 6,333 / OI 27

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 755 2026-11-06 (3DTE): 7,037 traded vs OI 6,968
- **SPY** PUT 750 2026-11-16 (13DTE): 569 traded vs OI 0
- **QQQ** PUT 640 2026-11-09 (6DTE): 4,894 traded vs OI 527
- **QQQ** PUT 650 2026-11-17 (14DTE): 556 traded vs OI 0
- **IWM** CALL 291 2026-11-13 (10DTE): 546 traded vs OI 227
- **IWM** CALL 289 2026-11-13 (10DTE): 722 traded vs OI 448
- **IWM** CALL 278 2026-11-03 (0DTE): 558 traded vs OI 555
- **AMD** PUT 475 2026-11-06 (3DTE): 967 traded vs OI 940
- **META** PUT 585 2026-11-13 (10DTE): 974 traded vs OI 126
- **MSFT** PUT 490 2026-11-04 (1DTE): 522 traded vs OI 104
- **SMCI** CALL 32 2026-11-06 (3DTE): 3,566 traded vs OI 3,304

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
