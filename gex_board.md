# GEX + FLOW SCAN - Thu Oct 29, 11:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 284P | 0.65 | 0.53 | +3% (25m) | **-18%** | +232% | 281.86 |
| 10:00 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 145C | 0.79 | 0.78 | +18% (37m) | **-1%** | +139% | 143.92 |
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.68 | +17% (2m) | **-12%** (done) | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.18 | +20% (21m) | **-64%** (done) | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:00:08 ET, last candle SPY 10:59, QQQ 10:59 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **ARM** | 227.03 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 46 | none: 18 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$3.8M | 221.37 | 227.5 | 220 | +$1.9M | - | out (clean 27, ADX 22, RVol 1.6) |
| 2 | **IWM** | 284.10 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 43 | 10/29 284P @ 0.61 (delta 0.47) = est +295% at 281.61 | POS +$785.9M | 281.61 | 284 | 270 | -$2.7M | +$173k bull / +$0 bear | out (clean 25, ADX 51, RVol 1.1) |
| 3 | **MSFT** | 521.17 | FLOW SURGE | **CALLS** | 43 | none: 126 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (28 contracts' greeks worked out here) | POS +$473.9M | 499.4 | 525 | 530 | +$30.2M | +$787k bull / +$0 bear | out (clean 28, ADX 25, RVol 1.8) |
| 4 | **AAPL** | 349.20 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 41 | 10/30 345P @ 0.65 (delta 0.21) = est +58% at 347.28 | POS +$603.6M | 340.11 | 350 | 345 | +$5.9M | +$361k bull / -$48k bear | out (clean 29, ADX 38, RVol 0.9) |
| 5 | **MU** | 952.20 | PINNED between the walls (positive gamma) - chop | **-** | 34 | - | POS +$385.7M | - | 950 | 950 | +$20.6M | +$3.2M bull / -$564k bear | out (clean 28, ADX 35, RVol 0.6) |
| 6 | **AMZN** | 246.00 | - | **-** | 28 | - | POS +$14.9M | 241.75 | 265 | 250 | -$9.8M | +$502k bull / +$0 bear | out (clean 31, ADX 40, RVol 1.4) |
| 7 | **GOOGL** | 284.63 | - | **-** | 27 | - | NEG -$196.3M | - | 300 | 290 | -$7.1M | +$1.7M bull / +$0 bear | out (clean 32, ADX 55, RVol 3.5) |
| 8 | **META** | 625.96 | - | **-** | 24 | - | NEG -$52.1M | 631.06 | 650 | 625 | -$12.0M | +$621k bull / -$261k bear | out (clean 28, ADX 46, RVol 0.8) |
| 9 | **COIN** | 160.92 | - | **-** | 22 | - | POS +$5.6M | 152.47 | 170 | 155 | -$267k | +$61k bull / +$0 bear | out (clean 26, ADX 20, RVol 1.2) |
| 10 | **SPY** | 768.70 | - | **-** | 20 | - | NEG -$4.9B | 772.94 | 770 | 765 | -$75.9M | +$1.6M bull / +$0 bear | out (clean 26, ADX 14, RVol 1.1) |
| 11 | **TSLA** | 405.31 | - | **-** | 20 | - | POS +$491.4M | - | 400 | 400 | -$18.7M | +$3.5M bull / +$0 bear | out (clean 29, ADX 28, RVol 0.8) |
| 12 | **QQQ** | 714.42 | - | **-** | 19 | - | NEG -$4.9B | 726.17 | 720 | 700 | -$54.9M | +$669k bull / -$191k bear | out (clean 27, ADX 22, RVol 0.6) |
| 13 | **UBER** | 65.39 | - | **-** | 19 | - | NEG -$30.6M | 68.28 | 67 | 65 | -$160k | - | out (clean 29, ADX 20, RVol 0.5) |
| 14 | **ORCL** | 140.56 | - | **-** | 18 | - | POS +$116.7M | - | 135 | 140 | -$220k | +$39k bull / +$0 bear | out (clean 31, ADX 30, RVol 1.1) |
| 15 | **HOOD** | 90.99 | - | **-** | 18 | - | NEG -$23.5M | - | 95 | 90 | -$901k | +$64k bull / +$0 bear | out (clean 28, ADX 12, RVol 0.9) |
| 16 | **SMH** | 561.02 | - | **-** | 17 | - | NEG -$46.4M | 564.56 | 560 | 555 | +$203k | +$60k bull / +$0 bear | out (clean 26, ADX 14, RVol 1.3) |
| 17 | **NVDA** | 213.95 | - | **-** | 17 | - | POS +$264.1M | 210.9 | 215 | 210 | -$2.3M | +$289k bull / -$172k bear | out (clean 24, ADX 23, RVol 0.8) |
| 18 | **AMD** | 567.74 | - | **-** | 17 | - | POS +$141.8M | - | 600 | 550 | -$527k | +$314k bull / -$28k bear | out (clean 28, ADX 34, RVol 0.4) |
| 19 | **PLTR** | 195.14 | - | **-** | 17 | - | POS +$36.1M | 191.71 | 200 | 190 | -$406k | +$61k bull / +$0 bear | out (clean 25, ADX 12, RVol 2.2) |
| 20 | **MSTR** | 141.72 | - | **-** | 17 | - | POS +$27.3M | - | 152.5 | 140 | -$443k | +$86k bull / -$33k bear | out (clean 25, ADX 14, RVol 1.3) |
| 21 | **NFLX** | 61.85 | - | **-** | 14 | - | NEG -$53.5M | - | 63 | 60 | -$398k | - | out (clean 31, ADX 34, RVol 0.8) |
| 22 | **BABA** | 99.88 | - | **-** | 14 | - | NEG -$15.5M | 102.27 | 102 | 100 | -$78k | - | out (clean 28, ADX 19, RVol 0.7) |
| 23 | **AVGO** | 342.77 | - | **-** | 13 | - | POS +$3.5M | 342.75 | 350 | 340 | +$2.7M | - | out (clean 28, ADX 27, RVol 0.4) |
| 24 | **CRM** | 230.16 | - | **-** | 13 | - | NEG -$19.2M | - | 240 | 230 | -$180k | - | out (clean 27, ADX 32, RVol 0.7) |
| 25 | **SHOP** | 166.16 | - | **-** | 13 | - | NEG -$4.8M | 171.26 | 175 | 165 | -$62k | - | out (clean 26, ADX 12, RVol 0.4) |
| 26 | **SMCI** | 35.27 | - | **-** | 12 | - | POS +$25.9M | - | 35 | 35 | +$155k | - | out (clean 26, ADX 18, RVol 1.0) |
| 27 | **DELL** | 486.03 | - | **-** | 6 | - | POS +$11.3M | 477.48 | 500 | 500 | +$106k | - | out (clean 30, ADX 30, RVol 0.3) |

## Big prints this scan (63)
- **TSLA** PUT 410 2026-10-30 (1DTE): 382 @ 6.20 = **+$237k** SELL | vol 4,623 / OI 1,090
- **QQQ** CALL 707 2026-10-29 (0DTE): 214 @ 8.97 = **+$192k** BUY | vol 751 / OI 185
- **QQQ** CALL 708 2026-11-02 (4DTE): 185 @ 10.31 = **+$191k** SELL | vol 474 / OI 277
- **SPY** PUT 775 2026-11-02 (4DTE): 270 @ 6.90 = **+$186k** SELL | vol 8,945 / OI 149
- **AMZN** CALL 240 2026-10-30 (1DTE): 100 @ 13.43 = **+$134k** MID | vol 889 / OI 742
- **MU** PUT 975 2026-10-30 (1DTE): 45 @ 29.10 = **+$131k** BUY | vol 424 / OI 292
- **SPY** CALL 770 2026-10-29 (0DTE): 878 @ 1.34 = **+$118k** BUY | vol 183,615 / OI 1,967
- **TSLA** CALL 405 2026-10-30 (1DTE): 200 @ 5.10 = **+$102k** BUY | vol 35,835 / OI 4,208
- **TSLA** CALL 405 2026-10-30 (1DTE): 180 @ 4.90 = **+$88k** BUY | vol 35,835 / OI 4,208
- **NVDA** CALL 210 2026-10-30 (1DTE): 174 @ 4.75 = **+$83k** BUY | vol 3,059 / OI 3,049
- **IWM** CALL 287 2026-10-30 (1DTE): 1,724 @ 0.46 = **+$79k** BUY | vol 8,598 / OI 5,900
- **NVDA** PUT 212.5 2026-11-04 (6DTE): 255 @ 2.99 = **+$76k** BUY | vol 3,355 / OI 260
- **MSFT** PUT 525 2026-10-30 (1DTE): 100 @ 5.78 = **+$58k** SELL | vol 6,183 / OI 1,940
- **NVDA** PUT 212.5 2026-11-04 (6DTE): 190 @ 2.99 = **+$57k** BUY | vol 3,355 / OI 260
- **MSTR** CALL 140 2026-10-30 (1DTE): 100 @ 5.62 = **+$56k** BUY | vol 1,010 / OI 1,673

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 781 2026-11-02 (4DTE): 1,362 traded vs OI 600
- **SPY** PUT 770 2026-10-30 (1DTE): 13,405 traded vs OI 13,054
- **SPY** PUT 766 2026-11-02 (4DTE): 1,183 traded vs OI 1,181
- **SPY** PUT 742 2026-10-29 (0DTE): 697 traded vs OI 629
- **SPY** PUT 769 2026-11-04 (6DTE): 505 traded vs OI 226
- **QQQ** CALL 707 2026-10-29 (0DTE): 751 traded vs OI 185
- **QQQ** CALL 737 2026-11-04 (6DTE): 701 traded vs OI 279
- **IWM** PUT 272 2026-11-02 (4DTE): 501 traded vs OI 356
- **NVDA** PUT 230 2026-11-02 (4DTE): 508 traded vs OI 187
- **NVDA** CALL 202.5 2026-11-02 (4DTE): 565 traded vs OI 238
- **NVDA** CALL 210 2026-10-30 (1DTE): 3,059 traded vs OI 3,049
- **NVDA** CALL 212.5 2026-11-06 (8DTE): 1,274 traded vs OI 1,244
- **TSLA** PUT 385 2026-10-30 (1DTE): 3,898 traded vs OI 3,837
- **TSLA** PUT 410 2026-11-20 (22DTE): 1,173 traded vs OI 1,158
- **TSLA** CALL 392.5 2026-11-02 (4DTE): 1,030 traded vs OI 667

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
