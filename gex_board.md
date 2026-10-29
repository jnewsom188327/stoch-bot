# GEX + FLOW SCAN - Thu Oct 29, 12:50 PM ET
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
Last 1m check 12:50:08 ET, last candle SPY 12:49, QQQ 12:49 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 524.00 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 42 | none: 126 puts 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (11 contracts' greeks worked out here) | POS +$527.5M | 501.39 | 525 | 530 | +$27.2M | +$455k bull / -$63k bear | out (clean 28, ADX 11, RVol 1.0) |
| 2 | **IWM** | 284.13 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 35 | 10/30 282P @ 0.44 (delta 0.24) = est +39% at 283.35 | POS +$915.0M | 281.24 | 284 | 270 | -$2.0M | +$93k bull / +$0 bear | out (clean 25, ADX 31, RVol 0.5) |
| 3 | **AAPL** | 349.88 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 35 | none: 55 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (11 contracts' greeks worked out here) | POS +$653.9M | 340.89 | 350 | 345 | +$2.4M | +$26k bull / +$0 bear | out (clean 29, ADX 22, RVol 0.7) |
| 4 | **META** | 633.87 | - | **-** | 24 | - | POS +$47.9M | 630.12 | 650 | 625 | -$20.3M | +$0 bull / -$609k bear | out (clean 28, ADX 46, RVol 1.1) |
| 5 | **GOOGL** | 285.07 | - | **-** | 23 | - | NEG -$203.6M | - | 300 | 290 | -$11.4M | +$290k bull / -$684k bear | out (clean 32, ADX 38, RVol 1.2) |
| 6 | **SMCI** | 35.02 | PINNED between the walls (positive gamma) - chop | **-** | 21 | - | POS +$24.7M | - | 35 | 35 | +$188k | - | out (clean 26, ADX 14, RVol 0.4) |
| 7 | **MU** | 942.18 | - | **-** | 20 | - | POS +$316.1M | - | 950 | 950 | +$26.2M | +$5.5M bull / -$1.9M bear | out (clean 27, ADX 32, RVol 0.7) |
| 8 | **AMZN** | 246.22 | - | **-** | 19 | - | POS +$12.6M | 242.37 | 265 | 250 | -$8.5M | +$118k bull / -$304k bear | out (clean 32, ADX 20, RVol 0.8) |
| 9 | **SPY** | 768.80 | - | **-** | 17 | - | NEG -$4.8B | 772.65 | 770 | 765 | -$112.9M | +$435k bull / -$872k bear | out (clean 25, ADX 10, RVol 0.6) |
| 10 | **TSLA** | 405.08 | - | **-** | 17 | - | POS +$509.1M | - | 400 | 400 | -$20.8M | +$298k bull / -$178k bear | out (clean 28, ADX 14, RVol 0.4) |
| 11 | **MSTR** | 142.84 | - | **-** | 17 | - | POS +$32.1M | - | 152.5 | 140 | -$550k | +$37k bull / +$0 bear | out (clean 26, ADX 19, RVol 0.9) |
| 12 | **QQQ** | 714.97 | - | **-** | 16 | - | NEG -$5.1B | 725.88 | 720 | 720 | -$70.9M | +$743k bull / -$230k bear | out (clean 27, ADX 14, RVol 0.5) |
| 13 | **AMD** | 569.24 | - | **-** | 16 | - | POS +$147.3M | - | 600 | 550 | -$2.1M | +$726k bull / +$0 bear | out (clean 27, ADX 17, RVol 1.0) |
| 14 | **NVDA** | 213.31 | - | **-** | 15 | - | POS +$199.9M | 211.14 | 215 | 210 | -$4.0M | +$437k bull / -$578k bear | out (clean 24, ADX 14, RVol 0.6) |
| 15 | **ARM** | 229.23 | - | **-** | 15 | - | POS +$3.1M | 222.62 | 227.5 | 230 | +$1.6M | - | out (clean 25, ADX 15, RVol 0.6) |
| 16 | **UBER** | 65.46 | - | **-** | 14 | - | NEG -$31.5M | 68.57 | 67 | 65 | -$170k | - | out (clean 28, ADX 12, RVol 0.4) |
| 17 | **NFLX** | 62.02 | - | **-** | 12 | - | NEG -$48.5M | 65.28 | 63 | 60 | -$535k | - | out (clean 30, ADX 30, RVol 0.5) |
| 18 | **CRM** | 230.71 | - | **-** | 11 | - | NEG -$20.1M | - | 240 | 230 | -$236k | - | out (clean 27, ADX 20, RVol 0.8) |
| 19 | **SHOP** | 167.10 | - | **-** | 8 | - | NEG -$6.1M | 172.04 | 175 | 165 | -$48k | - | out (clean 26, ADX 12, RVol 0.4) |
| 20 | **AVGO** | 344.26 | - | **-** | 7 | - | POS +$12.7M | 342.7 | 350 | 340 | +$2.1M | - | out (clean 27, ADX 11, RVol 0.9) |
| 21 | **COIN** | 160.56 | - | **-** | 7 | - | POS +$5.2M | 152.91 | 170 | 155 | -$211k | - | out (clean 26, ADX 11, RVol 1.4) |
| 22 | **DELL** | 484.06 | - | **-** | 7 | - | POS +$8.2M | 477.53 | 500 | 480 | +$236k | - | out (clean 29, ADX 31, RVol 0.3) |
| 23 | **ORCL** | 138.23 | - | **-** | 7 | - | POS +$121.2M | - | 135 | 140 | +$484k | - | out (clean 32, ADX 27, RVol 0.6) |
| 24 | **BABA** | 99.50 | - | **-** | 7 | - | NEG -$18.4M | 102.12 | 100 | 100 | -$24k | - | out (clean 29, ADX 23, RVol 0.7) |
| 25 | **SMH** | 561.18 | - | **-** | 5 | - | NEG -$23.4M | 562.68 | 560 | 555 | +$316k | - | out (clean 26, ADX 12, RVol 0.4) |
| 26 | **HOOD** | 91.31 | - | **-** | 5 | - | NEG -$23.0M | - | 95 | 90 | -$524k | - | out (clean 28, ADX 14, RVol 0.2) |
| 27 | **PLTR** | 194.13 | - | **-** | 4 | - | POS +$19.0M | 192.12 | 200 | 190 | -$344k | - | out (clean 25, ADX 13, RVol 0.4) |

## Big prints this scan (66)
- **SPY** PUT 775 2026-11-02 (4DTE): 944 @ 7.12 = **+$672k** BUY | vol 19,991 / OI 149
- **SPY** CALL 748 2026-10-30 (1DTE): 95 @ 21.00 = **+$200k** SELL | vol 107 / OI 430
- **TSLA** PUT 420 2026-10-30 (1DTE): 119 @ 15.00 = **+$178k** MID | vol 857 / OI 337
- **GOOGL** PUT 285 2026-11-02 (4DTE): 399 @ 4.25 = **+$170k** MID | vol 7,147 / OI 80
- **META** CALL 635 2026-10-30 (1DTE): 269 @ 5.90 = **+$159k** SELL | vol 9,976 / OI 860
- **MU** PUT 940 2026-11-02 (4DTE): 80 @ 19.69 = **+$158k** BUY | vol 753 / OI 108
- **GOOGL** PUT 285 2026-11-02 (4DTE): 334 @ 4.25 = **+$142k** MID | vol 7,147 / OI 80
- **MU** PUT 940 2026-11-02 (4DTE): 70 @ 19.71 = **+$138k** BUY | vol 753 / OI 108
- **QQQ** PUT 711 2026-10-30 (1DTE): 500 @ 2.61 = **+$130k** BUY | vol 9,352 / OI 1,595
- **MU** PUT 935 2026-10-30 (1DTE): 100 @ 11.70 = **+$117k** BUY | vol 4,023 / OI 1,035
- **QQQ** PUT 710 2026-11-03 (5DTE): 272 @ 4.25 = **+$116k** SELL | vol 1,220 / OI 898
- **TSLA** CALL 390 2026-11-04 (6DTE): 63 @ 17.65 = **+$111k** SELL | vol 72 / OI 127
- **TSLA** CALL 390 2026-11-02 (4DTE): 63 @ 16.13 = **+$102k** MID | vol 792 / OI 633
- **QQQ** CALL 713 2026-10-30 (1DTE): 200 @ 5.00 = **+$100k** SELL | vol 5,951 / OI 1,216
- **MU** PUT 940 2026-10-30 (1DTE): 70 @ 13.93 = **+$98k** BUY | vol 6,085 / OI 684

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 774 2026-11-03 (5DTE): 705 traded vs OI 436
- **SPY** PUT 746 2026-11-02 (4DTE): 971 traded vs OI 628
- **SPY** PUT 737 2026-11-03 (5DTE): 891 traded vs OI 241
- **SPY** CALL 756 2026-11-20 (22DTE): 587 traded vs OI 335
- **SPY** PUT 768 2026-11-06 (8DTE): 1,831 traded vs OI 1,575
- **SPY** PUT 755 2026-11-12 (14DTE): 524 traded vs OI 0
- **QQQ** CALL 721 2026-11-04 (6DTE): 505 traded vs OI 65
- **QQQ** PUT 710 2026-11-03 (5DTE): 1,220 traded vs OI 898
- **QQQ** PUT 706 2026-11-04 (6DTE): 504 traded vs OI 55
- **NVDA** CALL 222.5 2026-11-02 (4DTE): 1,919 traded vs OI 1,860
- **AAPL** PUT 340 2026-10-30 (1DTE): 11,025 traded vs OI 10,993
- **AAPL** PUT 335 2026-11-06 (8DTE): 5,774 traded vs OI 2,589
- **META** CALL 665 2026-10-30 (1DTE): 1,156 traded vs OI 1,152
- **META** PUT 632.5 2026-10-30 (1DTE): 782 traded vs OI 567
- **AMZN** CALL 245 2026-11-06 (8DTE): 810 traded vs OI 799

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
