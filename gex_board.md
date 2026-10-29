# GEX + FLOW SCAN - Thu Oct 29, 11:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 284P | 0.65 | 0.20 | +3% (25m) | **-69%** | +232% | 281.86 |
| 10:00 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 145C | 0.79 | 0.84 | +18% (37m) | **+6%** (done) | +139% | 143.92 |
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.68 | +17% (2m) | **-12%** (done) | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.18 | +20% (21m) | **-64%** (done) | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:30:08 ET, last candle SPY 11:29, QQQ 11:29 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MU** | 951.16 | PINNED between the walls (positive gamma) - chop | **-** | 30 | - | POS +$389.8M | - | 950 | 950 | +$15.3M | +$1.9M bull / +$0 bear | out (clean 28, ADX 30, RVol 0.4) |
| 2 | **ARM** | 229.01 | - | **-** | 29 | - | POS +$3.3M | 222.15 | 227.5 | 240 | +$1.6M | +$0 bull / -$26k bear | out (clean 26, ADX 16, RVol 1.6) |
| 3 | **GOOGL** | 286.92 | - | **-** | 28 | - | NEG -$212.1M | - | 300 | 290 | -$12.3M | +$0 bull / -$407k bear | out (clean 32, ADX 51, RVol 2.3) |
| 4 | **AMZN** | 248.25 | - | **-** | 26 | - | POS +$23.3M | 240.89 | 265 | 250 | -$14.4M | +$0 bull / -$3.5M bear | out (clean 31, ADX 29, RVol 0.9) |
| 5 | **MSFT** | 523.16 | - | **-** | 26 | - | POS +$507.4M | 500.11 | 525 | 530 | +$28.9M | +$773k bull / -$52k bear | out (clean 28, ADX 19, RVol 1.6) |
| 6 | **META** | 628.47 | - | **-** | 25 | - | NEG -$24.5M | 630.84 | 650 | 625 | -$17.1M | +$668k bull / -$1.5M bear | out (clean 28, ADX 48, RVol 1.1) |
| 7 | **IWM** | 284.94 | - | **-** | 23 | - | POS +$978.0M | 281.57 | 284 | 270 | -$6.3M | +$0 bull / -$306k bear | out (clean 25, ADX 52, RVol 1.0) |
| 8 | **SPY** | 770.15 | - | **-** | 20 | - | NEG -$3.4B | 773.21 | 770 | 765 | -$138.0M | +$0 bull / -$3.2M bear | out (clean 26, ADX 11, RVol 0.5) |
| 9 | **TSLA** | 405.79 | - | **-** | 20 | - | POS +$515.1M | - | 400 | 400 | -$25.2M | +$58k bull / -$107k bear | out (clean 29, ADX 25, RVol 0.4) |
| 10 | **QQQ** | 716.63 | - | **-** | 19 | - | NEG -$4.3B | 726.34 | 720 | 720 | -$100.6M | +$0 bull / -$989k bear | out (clean 26, ADX 16, RVol 0.4) |
| 11 | **AAPL** | 348.94 | - | **-** | 19 | - | POS +$602.0M | 340.57 | 350 | 345 | +$6.2M | +$305k bull / -$102k bear | out (clean 29, ADX 30, RVol 0.5) |
| 12 | **AMD** | 572.01 | - | **-** | 18 | - | POS +$147.0M | - | 600 | 550 | -$6.3M | +$72k bull / -$557k bear | out (clean 27, ADX 24, RVol 0.5) |
| 13 | **AVGO** | 344.86 | - | **-** | 18 | - | POS +$36.2M | 340.58 | 350 | 340 | +$1.7M | +$0 bull / -$34k bear | out (clean 27, ADX 20, RVol 0.5) |
| 14 | **HOOD** | 91.67 | - | **-** | 18 | - | NEG -$20.6M | - | 95 | 90 | -$890k | +$0 bull / -$46k bear | out (clean 28, ADX 14, RVol 0.7) |
| 15 | **UBER** | 65.66 | - | **-** | 18 | - | NEG -$24.9M | 67.93 | 67 | 65 | -$187k | - | out (clean 29, ADX 19, RVol 0.4) |
| 16 | **ORCL** | 140.41 | - | **-** | 17 | - | POS +$120.0M | - | 135 | 140 | -$466k | +$99k bull / +$0 bear | out (clean 31, ADX 23, RVol 0.7) |
| 17 | **NVDA** | 213.99 | - | **-** | 16 | - | POS +$281.3M | 211.02 | 215 | 210 | -$3.5M | +$156k bull / -$136k bear | out (clean 24, ADX 18, RVol 0.8) |
| 18 | **NFLX** | 62.23 | - | **-** | 16 | - | NEG -$46.6M | - | 63 | 60 | -$600k | - | out (clean 31, ADX 34, RVol 0.6) |
| 19 | **DELL** | 486.20 | - | **-** | 16 | - | POS +$10.2M | 477.9 | 500 | 500 | +$74k | +$0 bull / -$40k bear | out (clean 30, ADX 30, RVol 0.3) |
| 20 | **SHOP** | 167.43 | - | **-** | 13 | - | NEG -$5.5M | 172.05 | 175 | 165 | -$71k | - | out (clean 26, ADX 8, RVol 0.5) |
| 21 | **BABA** | 100.01 | - | **-** | 13 | - | NEG -$13.4M | 102 | 102 | 100 | -$107k | - | out (clean 28, ADX 13, RVol 0.4) |
| 22 | **CRM** | 228.66 | - | **-** | 12 | - | NEG -$19.9M | - | 240 | 230 | -$133k | - | out (clean 27, ADX 36, RVol 0.9) |
| 23 | **COIN** | 160.91 | - | **-** | 9 | - | POS +$5.4M | 152.61 | 170 | 155 | -$118k | - | out (clean 26, ADX 18, RVol 1.8) |
| 24 | **SMCI** | 35.34 | - | **-** | 8 | - | POS +$25.7M | - | 35 | 35 | +$128k | - | out (clean 26, ADX 13, RVol 0.6) |
| 25 | **MSTR** | 143.12 | - | **-** | 8 | - | POS +$33.0M | - | 152.5 | 140 | -$932k | - | out (clean 26, ADX 18, RVol 1.2) |
| 26 | **PLTR** | 195.21 | - | **-** | 6 | - | POS +$36.3M | 191.86 | 200 | 190 | -$946k | - | out (clean 25, ADX 11, RVol 1.2) |
| 27 | **SMH** | 563.51 | - | **-** | 4 | - | POS +$23.9M | 563.4 | 570 | 555 | -$173k | - | out (clean 26, ADX 12, RVol 0.5) |

## Big prints this scan (76)
- **SPY** CALL 776 2026-11-04 (6DTE): 3,525 @ 2.40 = **+$846k** SELL | vol 4,146 / OI 199
- **SPY** CALL 774 2026-11-02 (4DTE): 3,525 @ 1.84 = **+$649k** SELL | vol 4,395 / OI 514
- **SPY** PUT 775 2026-11-02 (4DTE): 500 @ 6.20 = **+$310k** BUY | vol 13,971 / OI 149
- **SPY** PUT 775 2026-11-02 (4DTE): 499 @ 6.20 = **+$309k** BUY | vol 13,971 / OI 149
- **META** CALL 605 2026-11-02 (4DTE): 99 @ 26.15 = **+$259k** MID | vol 357 / OI 31
- **META** PUT 625 2026-10-30 (1DTE): 495 @ 4.85 = **+$240k** BUY | vol 4,493 / OI 3,179
- **AMZN** CALL 260 2026-10-30 (1DTE): 428 @ 4.95 = **+$212k** SELL | vol 6,989 / OI 8,994
- **QQQ** CALL 715 2026-10-29 (0DTE): 588 @ 2.84 = **+$167k** SELL | vol 92,696 / OI 884
- **SPY** CALL 770 2026-11-03 (5DTE): 347 @ 4.15 = **+$144k** SELL | vol 5,114 / OI 932
- **SPY** CALL 770 2026-11-03 (5DTE): 303 @ 4.15 = **+$126k** SELL | vol 5,114 / OI 932
- **SPY** PUT 769 2026-10-30 (1DTE): 510 @ 2.36 = **+$120k** BUY | vol 28,417 / OI 5,341
- **QQQ** PUT 716 2026-10-29 (0DTE): 521 @ 2.28 = **+$119k** BUY | vol 58,068 / OI 797
- **AMD** CALL 572.5 2026-10-30 (1DTE): 117 @ 9.81 = **+$115k** SELL | vol 1,580 / OI 294
- **META** CALL 615 2026-11-02 (4DTE): 58 @ 18.70 = **+$108k** BUY | vol 292 / OI 139
- **QQQ** CALL 712 2026-10-29 (0DTE): 200 @ 5.32 = **+$106k** SELL | vol 12,294 / OI 356

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 776 2026-11-04 (6DTE): 4,146 traded vs OI 199
- **SPY** PUT 756 2026-10-30 (1DTE): 5,154 traded vs OI 5,124
- **SPY** PUT 746 2026-10-29 (0DTE): 852 traded vs OI 654
- **SPY** CALL 780 2026-11-10 (12DTE): 525 traded vs OI 181
- **SPY** PUT 765 2026-11-10 (12DTE): 509 traded vs OI 270
- **SPY** CALL 785 2026-11-06 (8DTE): 2,302 traded vs OI 2,276
- **SPY** CALL 770 2026-11-09 (11DTE): 501 traded vs OI 352
- **QQQ** PUT 703 2026-10-30 (1DTE): 2,880 traded vs OI 2,778
- **QQQ** CALL 724 2026-11-02 (4DTE): 505 traded vs OI 198
- **QQQ** PUT 677 2026-10-29 (0DTE): 802 traded vs OI 60
- **QQQ** CALL 725 2026-11-13 (15DTE): 1,778 traded vs OI 1,436
- **IWM** CALL 281 2026-10-30 (1DTE): 6,522 traded vs OI 6,518
- **IWM** CALL 300 2026-11-13 (15DTE): 987 traded vs OI 683
- **TSLA** PUT 407.5 2026-11-06 (8DTE): 542 traded vs OI 390
- **TSLA** CALL 407.5 2026-11-06 (8DTE): 944 traded vs OI 372

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
