# GEX + FLOW SCAN - Thu Oct 29, 11:50 AM ET
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
Last 1m check 11:50:08 ET, last candle SPY 11:49, QQQ 11:49 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 284.55 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 42 | 10/29 285P @ 0.79 (delta 0.63) = est +34% at 284 | POS +$861.9M | 281.54 | 284 | 270 | -$5.0M | +$860k bull / -$86k bear | out (clean 25, ADX 53, RVol 0.9) |
| 2 | **MU** | 947.85 | PINNED between the walls (positive gamma) - chop | **-** | 33 | - | POS +$368.6M | - | 950 | 950 | +$21.9M | +$866k bull / +$0 bear | out (clean 27, ADX 29, RVol 0.7) |
| 3 | **ORCL** | 139.93 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 33 | none: 26 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$123.3M | - | 135 | 140 | -$125k | +$52k bull / +$0 bear | out (clean 31, ADX 21, RVol 0.6) |
| 4 | **GOOGL** | 285.96 | - | **-** | 28 | - | NEG -$202.7M | - | 300 | 290 | -$13.6M | +$212k bull / -$230k bear | out (clean 32, ADX 47, RVol 2.0) |
| 5 | **META** | 628.30 | - | **-** | 24 | - | NEG -$22.7M | 630 | 650 | 625 | -$18.0M | +$384k bull / -$256k bear | out (clean 28, ADX 47, RVol 0.7) |
| 6 | **AMZN** | 247.66 | - | **-** | 24 | - | POS +$20.2M | 241.29 | 265 | 250 | -$14.5M | +$570k bull / -$498k bear | out (clean 31, ADX 24, RVol 0.8) |
| 7 | **MSFT** | 522.49 | - | **-** | 24 | - | POS +$468.2M | 501.24 | 525 | 530 | +$28.6M | +$98k bull / +$0 bear | out (clean 28, ADX 15, RVol 1.0) |
| 8 | **TSLA** | 405.91 | - | **-** | 20 | - | POS +$529.6M | - | 400 | 400 | -$24.2M | +$355k bull / -$200k bear | out (clean 29, ADX 24, RVol 0.5) |
| 9 | **SPY** | 769.17 | - | **-** | 19 | - | NEG -$4.1B | 772.74 | 770 | 765 | -$128.9M | +$1.0M bull / -$238k bear | out (clean 26, ADX 11, RVol 0.6) |
| 10 | **QQQ** | 716.04 | - | **-** | 18 | - | NEG -$4.5B | 726.32 | 720 | 720 | -$94.6M | +$434k bull / +$0 bear | out (clean 27, ADX 14, RVol 0.5) |
| 11 | **AAPL** | 348.81 | - | **-** | 18 | - | POS +$597.8M | 340.31 | 350 | 345 | +$4.1M | +$0 bull / -$83k bear | out (clean 29, ADX 27, RVol 0.5) |
| 12 | **AVGO** | 344.63 | - | **-** | 18 | - | POS +$31.1M | 340.45 | 350 | 340 | +$1.5M | +$211k bull / -$67k bear | out (clean 27, ADX 18, RVol 0.8) |
| 13 | **HOOD** | 91.77 | - | **-** | 18 | - | NEG -$20.6M | - | 95 | 90 | -$779k | +$57k bull / +$0 bear | out (clean 28, ADX 16, RVol 1.0) |
| 14 | **ARM** | 230.20 | - | **-** | 18 | - | POS +$3.6M | 221.99 | 227.5 | 240 | +$1.5M | - | out (clean 26, ADX 17, RVol 1.6) |
| 15 | **UBER** | 65.45 | - | **-** | 17 | - | NEG -$29.5M | 67.71 | 67 | 65 | -$176k | - | out (clean 29, ADX 19, RVol 0.4) |
| 16 | **NVDA** | 213.87 | - | **-** | 16 | - | POS +$243.8M | 211.16 | 215 | 210 | -$4.4M | +$30k bull / -$55k bear | out (clean 24, ADX 14, RVol 0.8) |
| 17 | **AMD** | 572.43 | - | **-** | 16 | - | POS +$148.1M | - | 600 | 550 | -$5.5M | +$417k bull / -$658k bear | out (clean 27, ADX 19, RVol 0.4) |
| 18 | **NFLX** | 62.20 | - | **-** | 15 | - | NEG -$47.8M | - | 63 | 60 | -$597k | - | out (clean 31, ADX 37, RVol 0.6) |
| 19 | **PLTR** | 194.98 | - | **-** | 15 | - | POS +$33.2M | 191.8 | 200 | 190 | -$1.0M | +$0 bull / -$26k bear | out (clean 25, ADX 9, RVol 0.6) |
| 20 | **SMH** | 563.65 | - | **-** | 14 | - | POS +$20.6M | 562.89 | 570 | 555 | -$90k | +$73k bull / -$100k bear | out (clean 26, ADX 14, RVol 0.5) |
| 21 | **CRM** | 228.99 | - | **-** | 12 | - | NEG -$19.5M | - | 240 | 230 | -$121k | - | out (clean 27, ADX 38, RVol 1.1) |
| 22 | **BABA** | 99.84 | - | **-** | 10 | - | NEG -$14.9M | 101.68 | 102 | 100 | -$85k | - | out (clean 28, ADX 11, RVol 0.5) |
| 23 | **SMCI** | 35.43 | - | **-** | 8 | - | POS +$26.0M | - | 35 | 35 | +$150k | - | out (clean 26, ADX 13, RVol 0.5) |
| 24 | **SHOP** | 166.72 | - | **-** | 8 | - | NEG -$5.0M | 170.64 | 175 | 165 | -$45k | - | out (clean 26, ADX 9, RVol 0.5) |
| 25 | **COIN** | 160.94 | - | **-** | 7 | - | POS +$5.6M | 152.42 | 170 | 155 | -$147k | - | out (clean 26, ADX 15, RVol 1.0) |
| 26 | **DELL** | 486.24 | - | **-** | 7 | - | POS +$11.7M | 477.24 | 500 | 500 | +$386k | - | out (clean 29, ADX 30, RVol 0.4) |
| 27 | **MSTR** | 143.48 | - | **-** | 7 | - | POS +$34.2M | - | 152.5 | 140 | -$607k | - | out (clean 26, ADX 21, RVol 0.9) |

## Big prints this scan (56)
- **AMZN** CALL 260 2026-10-30 (1DTE): 860 @ 5.43 = **+$467k** BUY | vol 9,719 / OI 8,994
- **SPY** PUT 775 2026-11-02 (4DTE): 500 @ 5.70 = **+$285k** SELL | vol 14,973 / OI 149
- **SPY** PUT 775 2026-11-02 (4DTE): 464 @ 5.70 = **+$264k** SELL | vol 14,973 / OI 149
- **QQQ** PUT 710 2026-11-04 (6DTE): 400 @ 4.70 = **+$188k** SELL | vol 1,036 / OI 364
- **META** CALL 615 2026-11-02 (4DTE): 100 @ 18.50 = **+$185k** BUY | vol 409 / OI 139
- **META** CALL 600 2026-11-02 (4DTE): 54 @ 31.45 = **+$170k** BUY | vol 101 / OI 55
- **SPY** CALL 770 2026-10-29 (0DTE): 1,000 @ 1.68 = **+$168k** BUY | vol 290,693 / OI 1,967
- **AMD** CALL 575 2026-10-30 (1DTE): 150 @ 9.91 = **+$149k** BUY | vol 3,396 / OI 2,077
- **QQQ** CALL 716 2026-10-29 (0DTE): 444 @ 3.22 = **+$143k** BUY | vol 103,785 / OI 381
- **IWM** PUT 284 2026-10-30 (1DTE): 1,283 @ 0.91 = **+$117k** SELL | vol 41,651 / OI 301
- **QQQ** CALL 707 2026-10-29 (0DTE): 119 @ 9.80 = **+$117k** MID | vol 2,983 / OI 185
- **QQQ** CALL 707 2026-10-29 (0DTE): 106 @ 9.79 = **+$104k** MID | vol 2,983 / OI 185
- **QQQ** CALL 707 2026-10-29 (0DTE): 94 @ 11.00 = **+$103k** BUY | vol 2,983 / OI 185
- **TSLA** CALL 405 2026-10-30 (1DTE): 207 @ 4.85 = **+$100k** BUY | vol 43,146 / OI 4,208
- **SMH** CALL 560 2026-10-30 (1DTE): 89 @ 8.23 = **+$73k** BUY | vol 731 / OI 4,995

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 780 2026-10-29 (0DTE): 529 traded vs OI 61
- **SPY** CALL 790 2026-11-02 (4DTE): 920 traded vs OI 485
- **SPY** PUT 747 2026-10-29 (0DTE): 563 traded vs OI 494
- **QQQ** CALL 739 2026-10-30 (1DTE): 1,300 traded vs OI 1,060
- **QQQ** PUT 690 2026-11-03 (5DTE): 1,219 traded vs OI 1,120
- **QQQ** CALL 714 2026-11-03 (5DTE): 501 traded vs OI 63
- **QQQ** PUT 680 2026-10-29 (0DTE): 2,407 traded vs OI 2,116
- **QQQ** CALL 729 2026-11-02 (4DTE): 513 traded vs OI 125
- **IWM** PUT 285 2026-11-02 (4DTE): 580 traded vs OI 0
- **NVDA** PUT 207.5 2026-11-04 (6DTE): 533 traded vs OI 443
- **TSLA** CALL 410 2026-11-06 (8DTE): 1,903 traded vs OI 1,877
- **AMD** PUT 570 2026-11-02 (4DTE): 509 traded vs OI 56
- **META** CALL 627.5 2026-11-02 (4DTE): 551 traded vs OI 131
- **AMZN** CALL 260 2026-10-30 (1DTE): 9,719 traded vs OI 8,994
- **AMZN** CALL 257.5 2026-11-06 (8DTE): 504 traded vs OI 422

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
