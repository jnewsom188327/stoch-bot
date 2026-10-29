# GEX + FLOW SCAN - Thu Oct 29, 12:20 PM ET
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
Last 1m check 12:20:08 ET, last candle SPY 12:19, QQQ 12:19 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 523.94 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 42 | none: 126 puts 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$514.7M | 501.58 | 525 | 530 | +$27.2M | +$0 bull / -$210k bear | out (clean 28, ADX 12, RVol 0.9) |
| 2 | **IWM** | 284.49 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 38 | 10/29 285P @ 0.78 (delta 0.67) = est +27% at 284 | POS +$953.2M | 281.2 | 284 | 270 | -$3.7M | +$973k bull / -$141k bear | out (clean 25, ADX 43, RVol 0.6) |
| 3 | **ARM** | 229.56 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 37 | none: 19 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$3.5M | 222.43 | 227.5 | 230 | +$1.6M | - | out (clean 26, ADX 18, RVol 1.1) |
| 4 | **AAPL** | 349.35 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 36 | none: 55 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$613.6M | 340.92 | 350 | 345 | +$3.0M | +$0 bull / -$348k bear | out (clean 28, ADX 23, RVol 0.8) |
| 5 | **GOOGL** | 284.92 | - | **-** | 25 | - | NEG -$195.3M | - | 300 | 290 | -$10.4M | +$143k bull / -$250k bear | out (clean 32, ADX 42, RVol 1.8) |
| 6 | **META** | 630.17 | - | **-** | 23 | - | NEG -$12.9M | 630.66 | 650 | 625 | -$15.9M | +$939k bull / -$35k bear | out (clean 28, ADX 44, RVol 0.7) |
| 7 | **CRM** | 231.61 | - | **-** | 23 | - | NEG -$20.2M | - | 240 | 230 | -$251k | +$0 bull / -$27k bear | out (clean 27, ADX 29, RVol 0.9) |
| 8 | **AMZN** | 246.28 | - | **-** | 19 | - | POS +$12.2M | 242.63 | 265 | 250 | -$8.5M | +$728k bull / +$0 bear | out (clean 31, ADX 21, RVol 0.7) |
| 9 | **MU** | 945.95 | - | **-** | 19 | - | POS +$354.4M | - | 950 | 950 | +$24.6M | +$1.4M bull / +$0 bear | out (clean 27, ADX 28, RVol 0.6) |
| 10 | **SPY** | 769.23 | - | **-** | 18 | - | NEG -$4.5B | 772.75 | 770 | 765 | -$123.1M | +$619k bull / -$114k bear | out (clean 25, ADX 10, RVol 0.7) |
| 11 | **TSLA** | 405.85 | - | **-** | 17 | - | POS +$515.1M | - | 400 | 400 | -$21.2M | +$147k bull / -$171k bear | out (clean 29, ADX 18, RVol 0.4) |
| 12 | **QQQ** | 715.59 | - | **-** | 16 | - | NEG -$4.8B | 726.49 | 720 | 720 | -$78.2M | +$546k bull / +$0 bear | out (clean 27, ADX 11, RVol 0.4) |
| 13 | **NVDA** | 213.51 | - | **-** | 15 | - | POS +$211.5M | 211.03 | 215 | 210 | -$5.2M | +$172k bull / +$0 bear | out (clean 24, ADX 11, RVol 0.7) |
| 14 | **AMD** | 571.15 | - | **-** | 15 | - | POS +$141.4M | - | 600 | 550 | -$4.3M | +$265k bull / +$0 bear | out (clean 27, ADX 15, RVol 0.4) |
| 15 | **UBER** | 65.35 | - | **-** | 15 | - | NEG -$29.8M | 68.99 | 67 | 65 | -$174k | - | out (clean 28, ADX 14, RVol 0.4) |
| 16 | **SMH** | 562.84 | - | **-** | 13 | - | NEG -$14.0M | 563.41 | 560 | 555 | +$46k | +$76k bull / +$0 bear | out (clean 26, ADX 13, RVol 0.4) |
| 17 | **NFLX** | 62.09 | - | **-** | 13 | - | NEG -$49.7M | - | 63 | 60 | -$492k | - | out (clean 31, ADX 35, RVol 0.5) |
| 18 | **MSTR** | 143.44 | - | **-** | 9 | - | POS +$34.1M | - | 152.5 | 140 | -$598k | - | out (clean 26, ADX 25, RVol 1.4) |
| 19 | **COIN** | 161.12 | - | **-** | 8 | - | POS +$6.9M | - | 170 | 155 | -$295k | - | out (clean 26, ADX 12, RVol 1.2) |
| 20 | **SHOP** | 166.81 | - | **-** | 8 | - | NEG -$5.7M | 172.18 | 175 | 165 | -$42k | - | out (clean 26, ADX 12, RVol 0.3) |
| 21 | **AVGO** | 344.40 | - | **-** | 7 | - | POS +$17.6M | 342.17 | 350 | 340 | +$1.8M | - | out (clean 27, ADX 15, RVol 0.6) |
| 22 | **DELL** | 485.74 | - | **-** | 7 | - | POS +$9.2M | 477.5 | 500 | 500 | +$415k | - | out (clean 29, ADX 28, RVol 0.5) |
| 23 | **SMCI** | 35.32 | - | **-** | 7 | - | POS +$25.6M | - | 35 | 35 | +$136k | - | out (clean 26, ADX 12, RVol 0.4) |
| 24 | **BABA** | 99.56 | - | **-** | 7 | - | NEG -$16.8M | 101.46 | 102 | 100 | -$46k | - | out (clean 28, ADX 15, RVol 0.4) |
| 25 | **HOOD** | 91.78 | - | **-** | 6 | - | NEG -$21.6M | 97.22 | 95 | 90 | -$691k | - | out (clean 28, ADX 17, RVol 0.5) |
| 26 | **ORCL** | 139.58 | - | **-** | 5 | - | POS +$125.4M | - | 135 | 140 | +$87k | - | out (clean 31, ADX 21, RVol 0.6) |
| 27 | **PLTR** | 194.55 | - | **-** | 3 | - | POS +$27.0M | 191.95 | 200 | 190 | -$521k | - | out (clean 25, ADX 9, RVol 0.2) |

## Big prints this scan (40)
- **TSLA** CALL 400 2026-10-30 (1DTE): 200 @ 7.30 = **+$146k** SELL | vol 13,846 / OI 14,892
- **META** CALL 615 2026-11-04 (6DTE): 50 @ 22.10 = **+$110k** BUY | vol 151 / OI 11
- **META** CALL 630 2026-10-30 (1DTE): 100 @ 7.00 = **+$70k** BUY | vol 18,648 / OI 2,036
- **MSFT** PUT 520 2026-10-30 (1DTE): 199 @ 3.45 = **+$69k** BUY | vol 11,032 / OI 2,175
- **MSFT** PUT 550 2026-11-02 (4DTE): 25 @ 27.05 = **+$68k** MID | vol 89 / OI 26
- **META** CALL 620 2026-10-30 (1DTE): 50 @ 13.50 = **+$68k** BUY | vol 7,603 / OI 771
- **META** CALL 620 2026-10-30 (1DTE): 50 @ 13.05 = **+$65k** BUY | vol 7,603 / OI 771
- **META** CALL 620 2026-10-30 (1DTE): 50 @ 13.05 = **+$65k** BUY | vol 7,603 / OI 771
- **TSLA** CALL 410 2026-11-02 (4DTE): 177 @ 3.65 = **+$65k** MID | vol 3,802 / OI 1,173
- **MU** PUT 985 2026-11-02 (4DTE): 15 @ 41.90 = **+$63k** SELL | vol 31 / OI 3
- **NVDA** PUT 220 2026-10-30 (1DTE): 100 @ 6.12 = **+$61k** SELL | vol 2,196 / OI 9,145
- **GOOGL** CALL 287.5 2026-10-30 (1DTE): 199 @ 3.00 = **+$60k** BUY | vol 17,851 / OI 0
- **MU** CALL 970 2026-10-30 (1DTE): 91 @ 6.50 = **+$59k** BUY | vol 8,999 / OI 2,312
- **MU** PUT 985 2026-10-30 (1DTE): 15 @ 38.18 = **+$57k** SELL | vol 297 / OI 377
- **META** PUT 620 2026-10-30 (1DTE): 200 @ 2.66 = **+$53k** SELL | vol 5,883 / OI 1,672

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 770 2026-11-03 (5DTE): 946 traded vs OI 941
- **SPY** CALL 785 2026-11-02 (4DTE): 595 traded vs OI 543
- **SPY** PUT 760 2026-10-30 (1DTE): 32,525 traded vs OI 31,744
- **QQQ** CALL 722 2026-11-03 (5DTE): 1,138 traded vs OI 290
- **IWM** CALL 269 2026-11-20 (22DTE): 1,021 traded vs OI 340
- **IWM** PUT 285 2026-11-27 (29DTE): 512 traded vs OI 192
- **TSLA** CALL 415 2026-11-02 (4DTE): 987 traded vs OI 983
- **AMD** CALL 570 2026-11-02 (4DTE): 500 traded vs OI 385
- **AMD** CALL 597.5 2026-11-02 (4DTE): 500 traded vs OI 24
- **AMD** CALL 610 2026-10-30 (1DTE): 2,030 traded vs OI 1,671
- **META** CALL 635 2026-11-04 (6DTE): 509 traded vs OI 112
- **AMZN** PUT 245 2026-10-30 (1DTE): 3,817 traded vs OI 3,801
- **AMZN** PUT 227.5 2026-11-02 (4DTE): 575 traded vs OI 140
- **GOOGL** PUT 287.5 2026-11-06 (8DTE): 543 traded vs OI 31
- **NFLX** CALL 64 2026-10-30 (1DTE): 8,359 traded vs OI 8,352

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
