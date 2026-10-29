# GEX + FLOW SCAN - Thu Oct 29, 11:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 284P | 0.65 | 0.22 | +3% (25m) | **-66%** (done) | +232% | 281.86 |
| 10:00 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 145C | 0.79 | 0.84 | +18% (37m) | **+6%** (done) | +139% | 143.92 |
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.68 | +17% (2m) | **-12%** (done) | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.18 | +20% (21m) | **-64%** (done) | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:40:08 ET, last candle SPY 11:39, QQQ 11:39 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 349.22 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 36 | 10/30 345P @ 0.60 (delta 0.20) = est +55% at 347.6 | POS +$603.8M | 340.12 | 350 | 345 | +$4.7M | +$27k bull / -$505k bear | out (clean 29, ADX 28, RVol 0.6) |
| 2 | **MU** | 949.69 | PINNED between the walls (positive gamma) - chop | **-** | 32 | - | POS +$375.9M | - | 950 | 950 | +$17.2M | +$1.2M bull / +$0 bear | out (clean 27, ADX 29, RVol 0.6) |
| 3 | **GOOGL** | 287.66 | - | **-** | 29 | - | NEG -$216.0M | - | 300 | 290 | -$14.1M | +$0 bull / -$394k bear | out (clean 32, ADX 49, RVol 2.4) |
| 4 | **ARM** | 229.81 | - | **-** | 28 | - | POS +$3.8M | 221.15 | 227.5 | 240 | +$1.5M | +$0 bull / -$26k bear | out (clean 26, ADX 16, RVol 1.6) |
| 5 | **AMZN** | 248.85 | - | **-** | 26 | - | POS +$25.1M | 240.99 | 265 | 250 | -$16.0M | +$0 bull / -$1.1M bear | out (clean 31, ADX 26, RVol 0.8) |
| 6 | **META** | 628.91 | - | **-** | 25 | - | NEG -$8.9M | 629.25 | 650 | 625 | -$19.7M | +$536k bull / -$590k bear | out (clean 28, ADX 48, RVol 1.0) |
| 7 | **MSFT** | 523.04 | - | **-** | 24 | - | POS +$500.9M | 500.4 | 525 | 530 | +$28.0M | +$238k bull / -$34k bear | out (clean 27, ADX 17, RVol 1.2) |
| 8 | **IWM** | 285.11 | - | **-** | 23 | - | POS +$941.7M | 281.81 | 284 | 270 | -$7.0M | +$0 bull / -$430k bear | out (clean 25, ADX 53, RVol 0.9) |
| 9 | **SPY** | 770.05 | - | **-** | 21 | - | NEG -$3.7B | 773.06 | 770 | 765 | -$149.4M | +$0 bull / -$2.7M bear | out (clean 25, ADX 12, RVol 0.6) |
| 10 | **TSLA** | 406.48 | - | **-** | 20 | - | POS +$518.1M | - | 400 | 400 | -$26.8M | +$0 bull / -$249k bear | out (clean 29, ADX 25, RVol 0.5) |
| 11 | **QQQ** | 716.87 | - | **-** | 19 | - | NEG -$4.2B | 726.56 | 720 | 720 | -$107.2M | +$0 bull / -$1.5M bear | out (clean 26, ADX 15, RVol 0.4) |
| 12 | **UBER** | 65.58 | - | **-** | 19 | - | NEG -$27.0M | 67.68 | 67 | 65 | -$189k | - | out (clean 29, ADX 20, RVol 0.5) |
| 13 | **AMD** | 573.45 | - | **-** | 18 | - | POS +$147.8M | - | 600 | 550 | -$8.1M | +$72k bull / -$849k bear | out (clean 27, ADX 22, RVol 0.6) |
| 14 | **AVGO** | 344.87 | - | **-** | 17 | - | POS +$33.4M | 340.48 | 350 | 340 | +$1.3M | +$0 bull / -$31k bear | out (clean 27, ADX 19, RVol 0.6) |
| 15 | **NVDA** | 213.97 | - | **-** | 16 | - | POS +$255.4M | 211.02 | 215 | 210 | -$4.9M | +$28k bull / -$438k bear | out (clean 24, ADX 16, RVol 0.8) |
| 16 | **ORCL** | 140.69 | - | **-** | 16 | - | POS +$118.9M | - | 135 | 140 | -$429k | +$99k bull / +$0 bear | out (clean 31, ADX 21, RVol 0.6) |
| 17 | **NFLX** | 62.20 | - | **-** | 15 | - | NEG -$49.1M | - | 63 | 60 | -$635k | - | out (clean 31, ADX 35, RVol 0.4) |
| 18 | **BABA** | 100.04 | - | **-** | 13 | - | NEG -$13.7M | 101.74 | 102 | 100 | -$110k | - | out (clean 28, ADX 11, RVol 0.5) |
| 19 | **CRM** | 229.09 | - | **-** | 12 | - | NEG -$20.2M | - | 240 | 230 | -$122k | - | out (clean 27, ADX 37, RVol 1.0) |
| 20 | **SHOP** | 166.87 | - | **-** | 10 | - | NEG -$5.4M | 172.32 | 175 | 165 | -$59k | - | out (clean 26, ADX 8, RVol 0.5) |
| 21 | **MSTR** | 143.69 | - | **-** | 9 | - | POS +$33.8M | - | 152.5 | 140 | -$865k | - | out (clean 26, ADX 20, RVol 1.2) |
| 22 | **HOOD** | 92.22 | - | **-** | 9 | - | NEG -$19.4M | - | 95 | 90 | -$982k | - | out (clean 28, ADX 16, RVol 1.0) |
| 23 | **COIN** | 161.39 | - | **-** | 8 | - | POS +$6.8M | - | 170 | 155 | -$156k | - | out (clean 26, ADX 16, RVol 1.3) |
| 24 | **SMCI** | 35.48 | - | **-** | 8 | - | POS +$26.4M | - | 35 | 35 | +$130k | - | out (clean 26, ADX 14, RVol 0.5) |
| 25 | **DELL** | 486.49 | - | **-** | 7 | - | POS +$11.7M | 477.27 | 500 | 500 | +$274k | - | out (clean 29, ADX 30, RVol 0.4) |
| 26 | **PLTR** | 195.08 | - | **-** | 6 | - | POS +$36.5M | 191.6 | 200 | 190 | -$1.2M | - | out (clean 25, ADX 10, RVol 0.8) |
| 27 | **SMH** | 564.52 | - | **-** | 5 | - | POS +$29.3M | 562.7 | 570 | 555 | -$301k | - | out (clean 26, ADX 14, RVol 0.3) |

## Big prints this scan (47)
- **AMZN** CALL 260 2026-10-30 (1DTE): 428 @ 5.14 = **+$220k** SELL | vol 8,107 / OI 8,994
- **MSFT** CALL 525 2026-10-30 (1DTE): 459 @ 4.30 = **+$197k** MID | vol 9,739 / OI 17,429
- **SPY** CALL 770 2026-10-29 (0DTE): 931 @ 1.41 = **+$131k** SELL | vol 264,921 / OI 1,967
- **SPY** CALL 770 2026-10-29 (0DTE): 760 @ 1.41 = **+$107k** SELL | vol 264,921 / OI 1,967
- **META** PUT 637.5 2026-10-30 (1DTE): 76 @ 11.75 = **+$89k** BUY | vol 124 / OI 414
- **IWM** PUT 284 2026-10-30 (1DTE): 949 @ 0.91 = **+$86k** BUY | vol 33,771 / OI 301
- **MU** CALL 950 2026-10-30 (1DTE): 56 @ 14.98 = **+$84k** BUY | vol 11,300 / OI 12,588
- **AMD** CALL 575 2026-10-30 (1DTE): 84 @ 8.80 = **+$74k** SELL | vol 2,857 / OI 2,077
- **AMD** CALL 577.5 2026-10-30 (1DTE): 93 @ 7.75 = **+$72k** SELL | vol 740 / OI 365
- **AMD** CALL 580 2026-10-30 (1DTE): 103 @ 6.65 = **+$68k** SELL | vol 2,698 / OI 2,027
- **AMD** CALL 577.5 2026-10-30 (1DTE): 76 @ 7.75 = **+$59k** SELL | vol 740 / OI 365
- **MSFT** PUT 525 2026-10-30 (1DTE): 100 @ 5.85 = **+$58k** MID | vol 7,573 / OI 1,940
- **AMD** CALL 580 2026-10-30 (1DTE): 83 @ 6.85 = **+$57k** SELL | vol 2,698 / OI 2,027
- **NVDA** CALL 215 2026-10-30 (1DTE): 440 @ 1.26 = **+$55k** SELL | vol 73,526 / OI 36,103
- **AAPL** CALL 360 2026-11-04 (6DTE): 200 @ 2.62 = **+$52k** SELL | vol 1,692 / OI 576

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 741 2026-11-02 (4DTE): 561 traded vs OI 511
- **QQQ** PUT 715 2026-10-30 (1DTE): 21,520 traded vs OI 21,359
- **QQQ** PUT 680 2026-11-04 (6DTE): 689 traded vs OI 346
- **QQQ** PUT 699 2026-10-30 (1DTE): 2,370 traded vs OI 2,366
- **QQQ** PUT 685 2026-11-05 (7DTE): 697 traded vs OI 684
- **IWM** CALL 290 2026-11-04 (6DTE): 603 traded vs OI 120
- **NVDA** CALL 225 2026-11-09 (11DTE): 511 traded vs OI 417
- **AMD** CALL 577.5 2026-10-30 (1DTE): 740 traded vs OI 365
- **MSFT** CALL 540 2026-11-27 (29DTE): 505 traded vs OI 315
- **GOOGL** CALL 315 2026-11-13 (15DTE): 500 traded vs OI 0
- **GOOGL** PUT 265 2026-11-02 (4DTE): 502 traded vs OI 59
- **AVGO** CALL 347.5 2026-10-30 (1DTE): 1,339 traded vs OI 1,314
- **AVGO** PUT 342.5 2026-11-06 (8DTE): 500 traded vs OI 147
- **AVGO** PUT 342.5 2026-10-30 (1DTE): 941 traded vs OI 913
- **UBER** CALL 65 2026-11-06 (8DTE): 509 traded vs OI 162

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
