# GEX + FLOW SCAN - Thu Oct 29, 12:30 PM ET
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
Last 1m check 12:30:08 ET, last candle SPY 12:29, QQQ 12:28 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 525.23 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 41 | none: 126 puts 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (12 contracts' greeks worked out here) | POS +$530.5M | 501.32 | 525 | 530 | +$26.3M | +$0 bull / -$367k bear | out (clean 28, ADX 12, RVol 0.9) |
| 2 | **IWM** | 284.59 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 38 | 10/29 285P @ 0.80 (delta 0.61) = est +32% at 284 | POS +$822.3M | 282.72 | 284 | 270 | -$3.8M | +$393k bull / -$228k bear | out (clean 25, ADX 40, RVol 0.6) |
| 3 | **AAPL** | 349.46 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 35 | none: 55 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$632.9M | 340.52 | 350 | 345 | +$2.8M | +$0 bull / -$62k bear | out (clean 28, ADX 23, RVol 0.7) |
| 4 | **GOOGL** | 285.43 | - | **-** | 24 | - | NEG -$194.5M | - | 300 | 290 | -$10.7M | +$248k bull / +$0 bear | out (clean 32, ADX 41, RVol 1.3) |
| 5 | **META** | 630.76 | - | **-** | 23 | - | NEG -$3.7M | 630.83 | 650 | 625 | -$16.7M | +$939k bull / -$186k bear | out (clean 28, ADX 43, RVol 0.6) |
| 6 | **AMZN** | 246.46 | - | **-** | 19 | - | POS +$14.1M | 242.29 | 265 | 250 | -$8.4M | +$825k bull / -$65k bear | out (clean 32, ADX 21, RVol 0.7) |
| 7 | **MU** | 942.76 | - | **-** | 19 | - | POS +$323.4M | - | 950 | 950 | +$27.7M | +$3.3M bull / +$0 bear | out (clean 27, ADX 29, RVol 0.4) |
| 8 | **AVGO** | 344.27 | - | **-** | 18 | - | POS +$14.9M | 342.13 | 350 | 340 | +$2.0M | +$26k bull / +$0 bear | out (clean 27, ADX 13, RVol 0.9) |
| 9 | **SPY** | 769.34 | - | **-** | 17 | - | NEG -$4.5B | 772.8 | 770 | 765 | -$119.5M | +$1.3M bull / -$826k bear | out (clean 25, ADX 9, RVol 0.5) |
| 10 | **TSLA** | 405.68 | - | **-** | 17 | - | POS +$522.7M | - | 400 | 400 | -$21.8M | +$100k bull / -$351k bear | out (clean 28, ADX 17, RVol 0.3) |
| 11 | **QQQ** | 715.83 | - | **-** | 16 | - | NEG -$4.9B | 726.4 | 720 | 720 | -$71.9M | +$521k bull / +$0 bear | out (clean 27, ADX 11, RVol 0.4) |
| 12 | **ARM** | 230.27 | - | **-** | 16 | - | POS +$3.5M | 222.38 | 227.5 | 240 | +$1.6M | - | out (clean 25, ADX 18, RVol 0.7) |
| 13 | **NVDA** | 213.56 | - | **-** | 15 | - | POS +$191.1M | 211.19 | 215 | 210 | -$4.1M | +$205k bull / +$0 bear | out (clean 24, ADX 12, RVol 0.7) |
| 14 | **UBER** | 65.36 | - | **-** | 15 | - | NEG -$31.3M | 68.5 | 67 | 65 | -$166k | - | out (clean 28, ADX 14, RVol 0.4) |
| 15 | **SMH** | 562.62 | - | **-** | 14 | - | NEG -$22.3M | 563.15 | 570 | 555 | +$229k | +$107k bull / +$0 bear | out (clean 26, ADX 12, RVol 0.3) |
| 16 | **AMD** | 570.58 | - | **-** | 14 | - | POS +$148.2M | - | 600 | 550 | -$2.9M | +$398k bull / -$38k bear | out (clean 27, ADX 15, RVol 0.4) |
| 17 | **NFLX** | 62.18 | - | **-** | 13 | - | NEG -$49.1M | - | 63 | 60 | -$547k | - | out (clean 31, ADX 34, RVol 0.5) |
| 18 | **CRM** | 230.96 | - | **-** | 12 | - | NEG -$20.2M | - | 240 | 230 | -$253k | - | out (clean 27, ADX 26, RVol 0.6) |
| 19 | **COIN** | 161.04 | - | **-** | 8 | - | POS +$5.4M | 153.34 | 170 | 155 | -$234k | - | out (clean 26, ADX 11, RVol 1.7) |
| 20 | **SMCI** | 35.26 | - | **-** | 8 | - | POS +$25.2M | - | 35 | 35 | +$164k | - | out (clean 26, ADX 11, RVol 0.4) |
| 21 | **MSTR** | 142.98 | - | **-** | 8 | - | POS +$31.7M | - | 152.5 | 140 | -$448k | - | out (clean 26, ADX 24, RVol 1.5) |
| 22 | **SHOP** | 167.16 | - | **-** | 8 | - | NEG -$5.9M | 171.85 | 175 | 165 | -$43k | - | out (clean 26, ADX 11, RVol 0.3) |
| 23 | **DELL** | 484.31 | - | **-** | 7 | - | POS +$8.9M | 477.07 | 500 | 500 | +$490k | - | out (clean 29, ADX 29, RVol 0.4) |
| 24 | **HOOD** | 91.72 | - | **-** | 6 | - | NEG -$21.3M | 97.15 | 95 | 90 | -$627k | - | out (clean 28, ADX 16, RVol 0.4) |
| 25 | **BABA** | 99.50 | - | **-** | 6 | - | NEG -$18.2M | 101.34 | 100 | 100 | -$20k | - | out (clean 28, ADX 18, RVol 0.5) |
| 26 | **ORCL** | 139.59 | - | **-** | 5 | - | POS +$121.8M | - | 135 | 140 | +$117k | - | out (clean 32, ADX 21, RVol 0.5) |
| 27 | **PLTR** | 194.40 | - | **-** | 3 | - | POS +$23.3M | 192.04 | 200 | 190 | -$487k | - | out (clean 25, ADX 10, RVol 0.3) |

## Big prints this scan (47)
- **SPY** PUT 775 2026-11-02 (4DTE): 1,000 @ 6.70 = **+$670k** BUY | vol 18,987 / OI 149
- **MU** CALL 960 2026-10-30 (1DTE): 480 @ 8.32 = **+$399k** BUY | vol 10,749 / OI 2,817
- **MU** CALL 970 2026-10-30 (1DTE): 480 @ 5.32 = **+$255k** BUY | vol 9,862 / OI 2,312
- **SPY** PUT 774 2026-11-02 (4DTE): 250 @ 6.25 = **+$156k** BUY | vol 1,687 / OI 102
- **QQQ** CALL 707 2026-10-29 (0DTE): 173 @ 8.66 = **+$150k** BUY | vol 4,406 / OI 185
- **IWM** PUT 287 2026-10-29 (0DTE): 342 @ 2.73 = **+$93k** BUY | vol 3,111 / OI 0
- **IWM** PUT 287 2026-10-29 (0DTE): 296 @ 2.82 = **+$83k** BUY | vol 3,111 / OI 0
- **TSLA** CALL 405 2026-10-30 (1DTE): 199 @ 3.75 = **+$75k** SELL | vol 45,679 / OI 4,208
- **NVDA** CALL 207.5 2026-10-30 (1DTE): 100 @ 6.29 = **+$63k** MID | vol 883 / OI 589
- **MU** CALL 950 2026-10-30 (1DTE): 50 @ 12.13 = **+$61k** BUY | vol 13,867 / OI 12,588
- **MU** PUT 970 2026-11-04 (6DTE): 15 @ 40.05 = **+$60k** SELL | vol 78 / OI 7
- **MU** PUT 970 2026-11-04 (6DTE): 15 @ 40.05 = **+$60k** SELL | vol 78 / OI 7
- **MU** CALL 920 2026-10-30 (1DTE): 20 @ 30.00 = **+$60k** BUY | vol 251 / OI 1,840
- **META** CALL 620 2026-10-30 (1DTE): 45 @ 12.45 = **+$56k** SELL | vol 7,719 / OI 771
- **GOOGL** CALL 287.5 2026-10-30 (1DTE): 200 @ 2.64 = **+$53k** BUY | vol 18,880 / OI 0

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 767 2026-11-03 (5DTE): 716 traded vs OI 658
- **SPY** PUT 732 2026-11-02 (4DTE): 630 traded vs OI 371
- **SPY** CALL 772 2026-11-04 (6DTE): 501 traded vs OI 347
- **SPY** PUT 758 2026-11-02 (4DTE): 903 traded vs OI 848
- **SPY** CALL 768 2026-11-04 (6DTE): 528 traded vs OI 254
- **SPY** PUT 750 2026-11-05 (7DTE): 1,255 traded vs OI 662
- **SPY** PUT 730 2026-11-10 (12DTE): 522 traded vs OI 124
- **SPY** PUT 753 2026-11-04 (6DTE): 698 traded vs OI 82
- **SPY** PUT 765 2026-11-04 (6DTE): 1,255 traded vs OI 581
- **SPY** PUT 765 2026-11-12 (14DTE): 559 traded vs OI 0
- **QQQ** PUT 715 2026-11-03 (5DTE): 755 traded vs OI 694
- **QQQ** CALL 732 2026-11-03 (5DTE): 565 traded vs OI 291
- **QQQ** CALL 724 2026-10-30 (1DTE): 4,453 traded vs OI 4,390
- **QQQ** PUT 693 2026-10-30 (1DTE): 2,113 traded vs OI 2,077
- **QQQ** PUT 704 2026-11-02 (4DTE): 515 traded vs OI 202

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
