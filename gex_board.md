# GEX + FLOW SCAN - Thu Oct 29, 01:00 PM ET
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
Last 1m check 13:00:08 ET, last candle SPY 12:59, QQQ 12:59 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 524.90 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 41 | none: 126 puts 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$537.0M | 501.96 | 525 | 530 | +$26.9M | +$89k bull / -$82k bear | out (clean 28, ADX 11, RVol 0.9) |
| 2 | **AAPL** | 349.80 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 34 | none: 55 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (12 contracts' greeks worked out here) | POS +$654.3M | 340.45 | 350 | 345 | +$1.5M | +$72k bull / -$549k bear | out (clean 29, ADX 23, RVol 0.6) |
| 3 | **IWM** | 284.48 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 24 | 10/29 285P @ 0.73 (delta 0.70) = est +34% at 284 | POS +$933.6M | 281.84 | 284 | 270 | -$2.2M | - | out (clean 25, ADX 28, RVol 0.4) |
| 4 | **META** | 634.48 | - | **-** | 24 | - | POS +$41.7M | 630.87 | 650 | 625 | -$18.6M | +$823k bull / -$718k bear | out (clean 28, ADX 47, RVol 1.2) |
| 5 | **GOOGL** | 284.50 | - | **-** | 23 | - | NEG -$192.0M | - | 300 | 290 | -$10.8M | +$60k bull / -$33k bear | out (clean 32, ADX 38, RVol 1.4) |
| 6 | **MU** | 944.68 | - | **-** | 20 | - | POS +$323.0M | - | 950 | 950 | +$22.1M | +$1.3M bull / -$3.7M bear | out (clean 27, ADX 32, RVol 0.8) |
| 7 | **AMZN** | 246.45 | - | **-** | 18 | - | POS +$13.8M | 242.19 | 265 | 250 | -$8.0M | +$693k bull / -$117k bear | out (clean 32, ADX 20, RVol 0.7) |
| 8 | **SPY** | 769.55 | - | **-** | 17 | - | NEG -$4.3B | 772.81 | 770 | 765 | -$116.8M | +$328k bull / -$1.6M bear | out (clean 25, ADX 9, RVol 0.6) |
| 9 | **TSLA** | 404.87 | - | **-** | 17 | - | POS +$491.9M | - | 400 | 400 | -$20.2M | +$331k bull / -$178k bear | out (clean 28, ADX 15, RVol 0.4) |
| 10 | **DELL** | 484.54 | - | **-** | 17 | - | POS +$7.7M | 477.47 | 500 | 480 | +$258k | +$0 bull / -$209k bear | out (clean 29, ADX 32, RVol 0.3) |
| 11 | **QQQ** | 716.21 | - | **-** | 16 | - | NEG -$4.8B | 726.38 | 720 | 720 | -$76.6M | +$116k bull / -$230k bear | out (clean 26, ADX 13, RVol 0.4) |
| 12 | **AMD** | 571.86 | - | **-** | 16 | - | POS +$146.9M | - | 600 | 550 | -$6.5M | +$142k bull / -$2.8M bear | out (clean 27, ADX 15, RVol 0.9) |
| 13 | **NVDA** | 213.67 | - | **-** | 15 | - | POS +$226.8M | 211.23 | 215 | 210 | -$4.6M | +$108k bull / -$568k bear | out (clean 24, ADX 14, RVol 0.5) |
| 14 | **ARM** | 229.25 | - | **-** | 15 | - | POS +$3.0M | 223.07 | 227.5 | 220 | +$1.6M | - | out (clean 24, ADX 15, RVol 0.6) |
| 15 | **UBER** | 65.48 | - | **-** | 14 | - | NEG -$30.4M | 68.06 | 67 | 65 | -$170k | - | out (clean 28, ADX 11, RVol 0.4) |
| 16 | **NFLX** | 62.15 | - | **-** | 12 | - | NEG -$52.0M | - | 63 | 60 | -$533k | - | out (clean 30, ADX 27, RVol 0.6) |
| 17 | **CRM** | 231.31 | - | **-** | 11 | - | NEG -$20.3M | - | 240 | 230 | -$235k | - | out (clean 27, ADX 18, RVol 1.0) |
| 18 | **SMCI** | 35.13 | - | **-** | 9 | - | POS +$25.9M | - | 35 | 35 | +$197k | - | out (clean 26, ADX 16, RVol 0.5) |
| 19 | **SHOP** | 167.85 | - | **-** | 9 | - | NEG -$5.1M | 171.5 | 175 | 165 | -$61k | - | out (clean 26, ADX 11, RVol 0.3) |
| 20 | **ORCL** | 137.87 | - | **-** | 8 | - | POS +$119.1M | - | 135 | 140 | +$485k | - | out (clean 32, ADX 30, RVol 0.6) |
| 21 | **BABA** | 99.46 | - | **-** | 7 | - | NEG -$18.3M | 101.67 | 100 | 100 | -$20k | - | out (clean 29, ADX 25, RVol 0.8) |
| 22 | **AVGO** | 345.30 | - | **-** | 6 | - | POS +$30.7M | 340.7 | 350 | 340 | +$1.9M | - | out (clean 27, ADX 12, RVol 0.3) |
| 23 | **COIN** | 160.89 | - | **-** | 6 | - | POS +$5.3M | 153.42 | 170 | 155 | -$186k | - | out (clean 26, ADX 11, RVol 0.8) |
| 24 | **MSTR** | 143.00 | - | **-** | 6 | - | POS +$33.0M | - | 152.5 | 140 | -$448k | - | out (clean 26, ADX 18, RVol 0.8) |
| 25 | **HOOD** | 91.42 | - | **-** | 5 | - | NEG -$23.2M | - | 95 | 90 | -$472k | - | out (clean 27, ADX 13, RVol 0.3) |
| 26 | **SMH** | 562.64 | - | **-** | 4 | - | NEG -$16.7M | 563.48 | 570 | 555 | +$294k | - | out (clean 26, ADX 12, RVol 0.4) |
| 27 | **PLTR** | 194.44 | - | **-** | 4 | - | POS +$26.0M | 192.02 | 200 | 190 | -$420k | - | out (clean 25, ADX 13, RVol 0.3) |

## Big prints this scan (49)
- **AMZN** CALL 250 2026-10-30 (1DTE): 350 @ 8.40 = **+$294k** BUY | vol 8,328 / OI 7,932
- **META** CALL 630 2026-10-30 (1DTE): 250 @ 8.95 = **+$224k** SELL | vol 21,236 / OI 2,036
- **AAPL** CALL 335 2026-10-30 (1DTE): 80 @ 14.60 = **+$117k** SELL | vol 895 / OI 3,239
- **MU** PUT 940 2026-10-30 (1DTE): 89 @ 12.12 = **+$108k** BUY | vol 6,578 / OI 684
- **MU** CALL 970 2026-10-30 (1DTE): 237 @ 4.50 = **+$107k** SELL | vol 11,602 / OI 2,312
- **DELL** PUT 500 2026-10-30 (1DTE): 52 @ 18.37 = **+$96k** MID | vol 361 / OI 812
- **AMD** CALL 600 2026-11-04 (6DTE): 69 @ 12.60 = **+$87k** SELL | vol 436 / OI 337
- **MU** CALL 940 2026-11-02 (4DTE): 40 @ 21.52 = **+$86k** MID | vol 1,332 / OI 115
- **MSFT** CALL 527.5 2026-10-30 (1DTE): 234 @ 3.50 = **+$82k** SELL | vol 8,178 / OI 644
- **META** CALL 620 2026-11-02 (4DTE): 40 @ 18.20 = **+$73k** MID | vol 792 / OI 109
- **AAPL** PUT 350 2026-11-04 (6DTE): 100 @ 7.15 = **+$72k** SELL | vol 6,797 / OI 755
- **MU** PUT 940 2026-10-30 (1DTE): 50 @ 12.77 = **+$64k** BUY | vol 6,578 / OI 684
- **MU** PUT 940 2026-10-30 (1DTE): 50 @ 12.77 = **+$64k** BUY | vol 6,578 / OI 684
- **AAPL** CALL 347.5 2026-10-30 (1DTE): 187 @ 3.40 = **+$64k** MID | vol 9,495 / OI 7,887
- **META** CALL 620 2026-11-02 (4DTE): 31 @ 18.50 = **+$57k** BUY | vol 792 / OI 109

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 807 2026-11-03 (5DTE): 632 traded vs OI 6
- **QQQ** CALL 716 2026-11-04 (6DTE): 500 traded vs OI 62
- **TSLA** PUT 405 2026-11-20 (22DTE): 1,620 traded vs OI 1,070
- **AAPL** PUT 330 2026-11-06 (8DTE): 9,458 traded vs OI 9,449
- **AAPL** CALL 352.5 2026-11-20 (22DTE): 734 traded vs OI 361
- **AMZN** CALL 250 2026-10-30 (1DTE): 8,328 traded vs OI 7,932
- **DELL** CALL 495 2026-10-30 (1DTE): 865 traded vs OI 407
- **MU** CALL 935 2026-10-30 (1DTE): 1,153 traded vs OI 1,088

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
