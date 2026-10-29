# GEX + FLOW SCAN - Thu Oct 29, 01:50 PM ET
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
Last 1m check 13:50:08 ET, last candle SPY 13:49, QQQ 13:49 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 526.18 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 40 | none: 126 puts 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$572.0M | 502.9 | 525 | 530 | +$25.6M | +$34k bull / -$226k bear | out (clean 28, ADX 12, RVol 0.8) |
| 2 | **AAPL** | 349.53 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 33 | none: 55 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$648.6M | 341.04 | 350 | 345 | +$3.9M | +$70k bull / +$0 bear | out (clean 29, ADX 19, RVol 0.5) |
| 3 | **ARM** | 229.47 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 33 | none: 18 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$3.6M | 221.25 | 227.5 | 230 | +$1.5M | - | out (clean 24, ADX 10, RVol 0.9) |
| 4 | **IWM** | 283.51 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 25 | 10/29 284P @ 0.70 (delta 0.68) = est +68% at 282.82 | POS +$869.0M | 281.09 | 284 | 270 | -$1.0M | - | out (clean 25, ADX 21, RVol 0.8) |
| 5 | **GOOGL** | 282.63 | - | **-** | 22 | - | NEG -$187.9M | - | 300 | 290 | -$8.0M | +$235k bull / +$0 bear | out (clean 32, ADX 38, RVol 1.3) |
| 6 | **DELL** | 477.05 | - | **-** | 22 | - | NEG -$3.9M | 480.53 | 500 | 460 | +$1.6M | +$461k bull / +$0 bear | out (clean 30, ADX 43, RVol 0.7) |
| 7 | **MU** | 936.53 | - | **-** | 20 | - | POS +$288.3M | 881.32 | 950 | 900 | +$28.2M | +$7.4M bull / -$614k bear | out (clean 27, ADX 37, RVol 0.3) |
| 8 | **META** | 627.89 | - | **-** | 19 | - | NEG -$39.3M | 630.66 | 650 | 625 | -$11.3M | +$119k bull / +$0 bear | out (clean 28, ADX 32, RVol 0.6) |
| 9 | **SPY** | 767.43 | - | **-** | 17 | - | NEG -$6.3B | 772.4 | 770 | 765 | -$99.5M | +$104k bull / +$0 bear | out (clean 25, ADX 17, RVol 0.3) |
| 10 | **AMZN** | 245.34 | - | **-** | 17 | - | POS +$8.6M | 242.71 | 265 | 250 | -$5.6M | +$345k bull / -$238k bear | out (clean 31, ADX 19, RVol 0.8) |
| 11 | **QQQ** | 713.50 | - | **-** | 16 | - | NEG -$5.5B | 725.81 | 720 | 700 | -$54.7M | +$945k bull / +$0 bear | out (clean 26, ADX 19, RVol 0.4) |
| 12 | **SMH** | 560.13 | - | **-** | 16 | - | NEG -$49.6M | 562.42 | 560 | 555 | +$627k | +$52k bull / +$0 bear | out (clean 26, ADX 14, RVol 0.4) |
| 13 | **TSLA** | 404.37 | - | **-** | 16 | - | POS +$494.6M | - | 400 | 400 | -$19.6M | +$264k bull / +$0 bear | out (clean 28, ADX 17, RVol 0.3) |
| 14 | **NVDA** | 213.14 | - | **-** | 15 | - | POS +$183.8M | 211.05 | 215 | 210 | -$4.1M | +$137k bull / -$31k bear | out (clean 24, ADX 15, RVol 0.4) |
| 15 | **AMD** | 566.23 | - | **-** | 14 | - | POS +$140.4M | - | 600 | 550 | -$3.5M | +$280k bull / -$361k bear | out (clean 28, ADX 17, RVol 0.3) |
| 16 | **UBER** | 65.19 | - | **-** | 13 | - | NEG -$33.8M | 68.29 | 67 | 65 | -$165k | - | out (clean 27, ADX 12, RVol 0.4) |
| 17 | **SMCI** | 34.84 | - | **-** | 11 | - | POS +$23.1M | - | 35 | 35 | +$242k | - | out (clean 26, ADX 24, RVol 0.4) |
| 18 | **ORCL** | 137.16 | - | **-** | 11 | - | POS +$121.9M | - | 135 | 140 | +$1.0M | - | out (clean 32, ADX 42, RVol 0.6) |
| 19 | **NFLX** | 61.73 | - | **-** | 10 | - | NEG -$51.4M | 64.81 | 63 | 61 | -$448k | - | out (clean 31, ADX 25, RVol 0.7) |
| 20 | **CRM** | 231.84 | - | **-** | 8 | - | NEG -$20.0M | - | 240 | 230 | -$246k | - | out (clean 27, ADX 12, RVol 0.4) |
| 21 | **BABA** | 99.30 | - | **-** | 7 | - | NEG -$19.3M | 101.41 | 100 | 100 | -$26k | - | out (clean 28, ADX 23, RVol 0.7) |
| 22 | **COIN** | 159.97 | - | **-** | 5 | - | POS +$5.0M | 153.42 | 170 | 155 | -$156k | - | out (clean 25, ADX 12, RVol 0.7) |
| 23 | **SHOP** | 166.74 | - | **-** | 5 | - | NEG -$5.4M | 170.58 | 175 | 165 | -$31k | - | out (clean 25, ADX 10, RVol 0.4) |
| 24 | **AVGO** | 345.16 | - | **-** | 4 | - | POS +$35.5M | 340.29 | 350 | 340 | +$424k | - | out (clean 27, ADX 17, RVol 0.4) |
| 25 | **PLTR** | 193.66 | - | **-** | 4 | - | POS +$16.5M | 192.2 | 200 | 190 | -$297k | - | out (clean 25, ADX 16, RVol 0.4) |
| 26 | **MSTR** | 141.69 | - | **-** | 4 | - | POS +$27.0M | - | 152.5 | 140 | +$123k | - | out (clean 25, ADX 14, RVol 0.8) |
| 27 | **HOOD** | 90.87 | - | **-** | 4 | - | NEG -$25.2M | - | 95 | 90 | -$407k | - | out (clean 27, ADX 14, RVol 0.2) |

## Big prints this scan (44)
- **MU** CALL 930 2026-11-04 (6DTE): 640 @ 31.32 = **+$2.0M** BUY | vol 1,009 / OI 53
- **MU** CALL 940 2026-11-04 (6DTE): 640 @ 26.12 = **+$1.7M** BUY | vol 1,151 / OI 50
- **MU** CALL 930 2026-11-04 (6DTE): 352 @ 31.32 = **+$1.1M** BUY | vol 1,009 / OI 53
- **MU** CALL 940 2026-11-04 (6DTE): 352 @ 26.12 = **+$919k** BUY | vol 1,151 / OI 50
- **AMD** CALL 565 2026-10-30 (1DTE): 253 @ 11.05 = **+$280k** BUY | vol 3,392 / OI 956
- **QQQ** PUT 716 2026-10-30 (1DTE): 266 @ 4.60 = **+$122k** SELL | vol 18,358 / OI 4,780
- **QQQ** CALL 715 2026-10-30 (1DTE): 300 @ 4.06 = **+$122k** BUY | vol 21,537 / OI 10,337
- **AMZN** PUT 235 2026-10-30 (1DTE): 200 @ 5.00 = **+$100k** SELL | vol 9,123 / OI 5,203
- **MU** CALL 950 2026-10-30 (1DTE): 100 @ 9.50 = **+$95k** BUY | vol 19,060 / OI 12,588
- **DELL** CALL 480 2026-10-30 (1DTE): 104 @ 8.10 = **+$84k** BUY | vol 592 / OI 1,229
- **DELL** CALL 480 2026-10-30 (1DTE): 100 @ 8.10 = **+$81k** BUY | vol 592 / OI 1,229
- **NVDA** PUT 212.5 2026-10-30 (1DTE): 532 @ 1.24 = **+$66k** SELL | vol 73,380 / OI 5,164
- **TSLA** CALL 402.5 2026-11-02 (4DTE): 100 @ 6.45 = **+$64k** BUY | vol 2,311 / OI 240
- **META** CALL 620 2026-11-04 (6DTE): 30 @ 18.20 = **+$55k** BUY | vol 397 / OI 106
- **MSFT** CALL 525 2026-11-02 (4DTE): 85 @ 6.30 = **+$54k** SELL | vol 1,706 / OI 132

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 815 2026-11-06 (8DTE): 1,129 traded vs OI 1,124
- **QQQ** CALL 725 2026-10-30 (1DTE): 15,667 traded vs OI 15,651
- **QQQ** PUT 687 2026-10-30 (1DTE): 3,676 traded vs OI 3,498
- **NVDA** CALL 215 2026-11-27 (29DTE): 1,676 traded vs OI 1,675
- **META** PUT 620 2026-11-04 (6DTE): 510 traded vs OI 199
- **MSFT** CALL 525 2026-10-30 (1DTE): 17,475 traded vs OI 17,429
- **DELL** CALL 500 2026-10-30 (1DTE): 3,181 traded vs OI 2,790
- **MU** CALL 945 2026-11-02 (4DTE): 501 traded vs OI 220
- **MSTR** CALL 142 2026-10-30 (1DTE): 1,465 traded vs OI 1,462

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
