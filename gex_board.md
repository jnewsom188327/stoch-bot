# GEX + FLOW SCAN - Thu Oct 29, 01:10 PM ET
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
Last 1m check 13:10:08 ET, last candle SPY 13:09, QQQ 13:09 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 524.57 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 40 | none: 126 puts 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | POS +$532.1M | 502.03 | 525 | 530 | +$26.7M | +$29k bull / -$222k bear | out (clean 28, ADX 10, RVol 0.7) |
| 2 | **AAPL** | 349.76 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 34 | none: 55 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$652.7M | 340.57 | 350 | 345 | +$2.2M | +$460k bull / -$549k bear | out (clean 29, ADX 23, RVol 0.6) |
| 3 | **ARM** | 229.66 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 33 | none: 19 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$2.9M | 222.88 | 227.5 | 230 | +$1.6M | - | out (clean 24, ADX 13, RVol 0.7) |
| 4 | **IWM** | 284.32 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 24 | none: 307 puts 0-7DTE > 15 priced 0.40-0.80 > 5 delta 0.2+ > 5 spread ok > 5 liquid > best one only +10% at the target (needs +20%) (129 contracts' greeks worked out here) | POS +$931.8M | 281.25 | 284 | 270 | -$2.4M | - | out (clean 25, ADX 25, RVol 0.5) |
| 5 | **META** | 631.88 | - | **-** | 23 | - | POS +$27.4M | 629.67 | 650 | 625 | -$17.1M | +$1.0M bull / -$312k bear | out (clean 28, ADX 45, RVol 0.9) |
| 6 | **GOOGL** | 284.81 | - | **-** | 23 | - | NEG -$199.0M | - | 300 | 290 | -$10.8M | +$93k bull / +$0 bear | out (clean 32, ADX 37, RVol 1.3) |
| 7 | **MU** | 940.80 | - | **-** | 19 | - | POS +$314.4M | - | 950 | 950 | +$24.3M | +$1.1M bull / -$5.1M bear | out (clean 27, ADX 33, RVol 0.4) |
| 8 | **AMZN** | 246.10 | - | **-** | 18 | - | POS +$13.5M | 242.19 | 265 | 250 | -$8.6M | +$1.2M bull / -$678k bear | out (clean 32, ADX 20, RVol 0.7) |
| 9 | **DELL** | 482.57 | - | **-** | 18 | - | POS +$6.8M | 477.6 | 500 | 480 | +$505k | +$217k bull / -$209k bear | out (clean 29, ADX 33, RVol 0.5) |
| 10 | **SPY** | 768.88 | - | **-** | 17 | - | NEG -$4.7B | 772.47 | 770 | 765 | -$115.2M | +$480k bull / -$1.6M bear | out (clean 25, ADX 9, RVol 0.4) |
| 11 | **QQQ** | 714.82 | - | **-** | 16 | - | NEG -$5.1B | 725.86 | 720 | 720 | -$75.0M | +$209k bull / -$200k bear | out (clean 26, ADX 13, RVol 0.4) |
| 12 | **TSLA** | 403.87 | - | **-** | 16 | - | POS +$497.0M | - | 400 | 400 | -$18.1M | +$671k bull / +$0 bear | out (clean 28, ADX 17, RVol 0.3) |
| 13 | **AMD** | 568.41 | - | **-** | 16 | - | POS +$153.3M | - | 600 | 550 | -$5.4M | +$201k bull / -$2.9M bear | out (clean 27, ADX 14, RVol 0.8) |
| 14 | **NVDA** | 213.30 | - | **-** | 15 | - | POS +$213.0M | 211.05 | 215 | 210 | -$4.6M | +$0 bull / -$109k bear | out (clean 24, ADX 14, RVol 0.4) |
| 15 | **UBER** | 65.48 | - | **-** | 14 | - | NEG -$28.7M | 68.74 | 67 | 65 | -$170k | - | out (clean 28, ADX 11, RVol 0.4) |
| 16 | **NFLX** | 61.99 | - | **-** | 11 | - | NEG -$50.7M | - | 63 | 60 | -$498k | - | out (clean 30, ADX 24, RVol 0.7) |
| 17 | **SMCI** | 35.09 | - | **-** | 10 | - | POS +$25.5M | - | 35 | 35 | +$204k | - | out (clean 26, ADX 17, RVol 0.5) |
| 18 | **CRM** | 231.01 | - | **-** | 10 | - | NEG -$20.7M | - | 240 | 230 | -$245k | - | out (clean 27, ADX 16, RVol 0.9) |
| 19 | **ORCL** | 137.82 | - | **-** | 8 | - | POS +$124.4M | - | 135 | 140 | +$620k | - | out (clean 32, ADX 33, RVol 0.6) |
| 20 | **BABA** | 99.41 | - | **-** | 8 | - | NEG -$19.2M | 101.79 | 100 | 100 | -$28k | - | out (clean 29, ADX 26, RVol 0.7) |
| 21 | **COIN** | 161.06 | - | **-** | 7 | - | POS +$5.7M | 152.98 | 170 | 155 | -$222k | - | out (clean 26, ADX 11, RVol 1.1) |
| 22 | **SHOP** | 167.15 | - | **-** | 7 | - | NEG -$6.2M | 172.44 | 175 | 165 | -$47k | - | out (clean 26, ADX 11, RVol 0.3) |
| 23 | **AVGO** | 344.97 | - | **-** | 6 | - | POS +$33.7M | 340.11 | 350 | 340 | +$1.8M | - | out (clean 27, ADX 12, RVol 0.3) |
| 24 | **MSTR** | 142.77 | - | **-** | 5 | - | POS +$32.3M | - | 152.5 | 140 | -$385k | - | out (clean 25, ADX 16, RVol 0.6) |
| 25 | **HOOD** | 91.39 | - | **-** | 5 | - | NEG -$22.7M | - | 95 | 90 | -$477k | - | out (clean 27, ADX 12, RVol 0.5) |
| 26 | **SMH** | 561.27 | - | **-** | 4 | - | NEG -$29.2M | 562.34 | 560 | 555 | +$305k | - | out (clean 26, ADX 12, RVol 0.3) |
| 27 | **PLTR** | 193.98 | - | **-** | 4 | - | POS +$17.0M | 192.11 | 200 | 190 | -$362k | - | out (clean 25, ADX 14, RVol 0.3) |

## Big prints this scan (49)
- **SPY** CALL 745 2026-10-30 (1DTE): 300 @ 24.27 = **+$728k** MID | vol 326 / OI 2,504
- **SPY** CALL 741 2026-10-30 (1DTE): 200 @ 28.28 = **+$566k** MID | vol 210 / OI 393
- **SPY** CALL 744 2026-10-30 (1DTE): 200 @ 25.17 = **+$503k** MID | vol 204 / OI 476
- **AMZN** PUT 240 2026-10-30 (1DTE): 500 @ 7.05 = **+$352k** MID | vol 5,798 / OI 8,499
- **SPY** CALL 740 2026-10-30 (1DTE): 100 @ 29.45 = **+$294k** SELL | vol 132 / OI 2,320
- **SPY** CALL 742 2026-10-30 (1DTE): 100 @ 27.17 = **+$272k** SELL | vol 116 / OI 452
- **SPY** CALL 747 2026-10-30 (1DTE): 100 @ 22.47 = **+$225k** MID | vol 104 / OI 432
- **QQQ** CALL 708 2026-11-02 (4DTE): 200 @ 10.45 = **+$209k** BUY | vol 878 / OI 277
- **AAPL** CALL 350 2026-11-04 (6DTE): 238 @ 7.30 = **+$174k** BUY | vol 1,713 / OI 863
- **TSLA** PUT 405 2026-10-30 (1DTE): 467 @ 3.45 = **+$161k** SELL | vol 31,297 / OI 2,059
- **TSLA** CALL 400 2026-10-30 (1DTE): 218 @ 6.50 = **+$142k** BUY | vol 15,100 / OI 14,892
- **SPY** PUT 775 2026-11-02 (4DTE): 200 @ 6.78 = **+$136k** SELL | vol 21,992 / OI 149
- **SPY** PUT 775 2026-11-02 (4DTE): 200 @ 6.78 = **+$136k** SELL | vol 21,992 / OI 149
- **MU** CALL 945 2026-10-30 (1DTE): 100 @ 12.65 = **+$126k** BUY | vol 6,513 / OI 759
- **AMZN** CALL 245 2026-10-30 (1DTE): 100 @ 10.75 = **+$108k** BUY | vol 6,295 / OI 2,504

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 749 2026-11-06 (8DTE): 695 traded vs OI 571
- **SPY** CALL 786 2026-11-06 (8DTE): 596 traded vs OI 560
- **SPY** CALL 795 2026-11-06 (8DTE): 2,203 traded vs OI 2,054
- **NVDA** CALL 200 2026-11-04 (6DTE): 508 traded vs OI 68
- **NVDA** CALL 202.5 2026-11-04 (6DTE): 579 traded vs OI 77
- **TSLA** CALL 400 2026-10-30 (1DTE): 15,100 traded vs OI 14,892
- **META** CALL 675 2026-11-02 (4DTE): 563 traded vs OI 460
- **META** PUT 635 2026-10-30 (1DTE): 955 traded vs OI 920
- **META** CALL 685 2026-11-02 (4DTE): 1,057 traded vs OI 0
- **META** CALL 672.5 2026-11-02 (4DTE): 511 traded vs OI 59
- **GOOGL** CALL 280 2026-11-02 (4DTE): 506 traded vs OI 0
- **GOOGL** CALL 302.5 2026-11-06 (8DTE): 502 traded vs OI 8
- **PLTR** CALL 200 2026-10-30 (1DTE): 15,597 traded vs OI 15,523
- **BABA** CALL 101 2026-10-30 (1DTE): 1,730 traded vs OI 1,726

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
