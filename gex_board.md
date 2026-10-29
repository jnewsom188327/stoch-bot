# GEX + FLOW SCAN - Thu Oct 29, 10:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 284P | 0.65 | 0.61 | -3% (0m) | **-6%** | +232% | 281.86 |
| 10:00 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 145C | 0.79 | 0.59 | +18% (37m) | **-25%** | +139% | 143.92 |
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.71 | +17% (2m) | **-8%** | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.27 | +20% (21m) | **-46%** | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:50:08 ET, last candle SPY 10:49, QQQ 10:49 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 521.62 | FLOW SURGE | **CALLS** | 44 | none: 126 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | POS +$442.9M | 499.8 | 525 | 530 | +$29.3M | +$515k bull / -$272k bear | out (clean 28, ADX 27, RVol 1.7) |
| 2 | **IWM** | 283.99 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 43 | 10/29 284P @ 0.55 (delta 0.50) = est +267% at 282 | POS +$823.2M | 281.77 | 284 | 270 | -$3.8M | +$94k bull / -$144k bear | out (clean 26, ADX 51, RVol 1.1) |
| 3 | **AMZN** | 245.81 | - | **-** | 29 | - | POS +$11.8M | 242.24 | 265 | 250 | -$10.0M | +$403k bull / -$163k bear | out (clean 31, ADX 40, RVol 1.3) |
| 4 | **GOOGL** | 284.27 | - | **-** | 28 | - | NEG -$198.5M | - | 300 | 290 | -$8.8M | +$1.8M bull / -$297k bear | out (clean 32, ADX 54, RVol 3.8) |
| 5 | **AVGO** | 341.55 | FLIP CROSS down into negative gamma | **PUTS** | 26 | none: 84 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$2.4M | 342.12 | 350 | 340 | +$2.7M | - | out (clean 28, ADX 29, RVol 0.5) |
| 6 | **COIN** | 162.23 | - | **-** | 25 | - | POS +$7.5M | - | 170 | 155 | -$388k | +$29k bull / -$133k bear | out (clean 26, ADX 21, RVol 1.1) |
| 7 | **META** | 622.61 | - | **-** | 24 | - | NEG -$83.5M | 629.1 | 650 | 625 | -$9.8M | +$1.1M bull / -$603k bear | out (clean 28, ADX 46, RVol 0.9) |
| 8 | **ARM** | 226.72 | - | **-** | 24 | - | POS +$3.3M | 221.91 | 227.5 | 220 | +$1.8M | - | out (clean 27, ADX 23, RVol 1.3) |
| 9 | **TSLA** | 404.65 | - | **-** | 23 | - | POS +$487.1M | - | 400 | 400 | -$25.5M | +$1.2M bull / -$1.3M bear | out (clean 29, ADX 29, RVol 0.9) |
| 10 | **AAPL** | 348.94 | - | **-** | 22 | - | POS +$588.5M | 339.94 | 350 | 345 | +$6.1M | +$229k bull / -$206k bear | out (clean 29, ADX 40, RVol 1.0) |
| 11 | **MU** | 946.43 | - | **-** | 22 | - | POS +$352.1M | - | 950 | 950 | +$21.6M | +$3.0M bull / -$693k bear | out (clean 29, ADX 35, RVol 0.8) |
| 12 | **SPY** | 767.85 | - | **-** | 21 | - | NEG -$5.4B | 772.74 | 770 | 765 | -$78.7M | +$741k bull / -$1.5M bear | out (clean 26, ADX 14, RVol 1.1) |
| 13 | **MSTR** | 141.00 | - | **-** | 21 | - | POS +$26.5M | - | 152.5 | 140 | -$1.0M | +$0 bull / -$203k bear | out (clean 26, ADX 16, RVol 1.3) |
| 14 | **UBER** | 65.15 | - | **-** | 21 | - | NEG -$31.9M | 67.99 | 70 | 65 | -$171k | - | out (clean 29, ADX 22, RVol 0.5) |
| 15 | **HOOD** | 90.94 | - | **-** | 20 | - | NEG -$23.3M | - | 95 | 90 | -$1.1M | +$27k bull / +$0 bear | out (clean 29, ADX 13, RVol 0.8) |
| 16 | **QQQ** | 713.41 | - | **-** | 19 | - | NEG -$5.3B | 726.53 | 720 | 700 | -$56.4M | +$463k bull / -$426k bear | out (clean 27, ADX 22, RVol 0.6) |
| 17 | **SMH** | 558.88 | - | **-** | 18 | - | NEG -$66.2M | 563.12 | 560 | 555 | +$249k | +$60k bull / +$0 bear | out (clean 27, ADX 15, RVol 1.3) |
| 18 | **AMD** | 564.35 | - | **-** | 18 | - | POS +$144.8M | - | 600 | 550 | +$675k | +$343k bull / -$190k bear | out (clean 28, ADX 35, RVol 0.5) |
| 19 | **ORCL** | 139.60 | - | **-** | 18 | - | POS +$116.0M | - | 135 | 140 | -$116k | +$139k bull / -$83k bear | out (clean 32, ADX 32, RVol 1.0) |
| 20 | **NVDA** | 213.06 | - | **-** | 17 | - | POS +$185.4M | 210.81 | 215 | 210 | -$2.1M | +$74k bull / -$1.4M bear | out (clean 25, ADX 24, RVol 0.9) |
| 21 | **NFLX** | 61.80 | - | **-** | 17 | - | NEG -$51.8M | - | 63 | 60 | -$464k | - | out (clean 30, ADX 37, RVol 1.0) |
| 22 | **BABA** | 100.06 | - | **-** | 16 | - | NEG -$13.5M | 101.76 | 102 | 100 | -$83k | - | out (clean 28, ADX 21, RVol 0.8) |
| 23 | **CRM** | 230.50 | - | **-** | 14 | - | NEG -$19.1M | - | 240 | 230 | -$212k | - | out (clean 27, ADX 31, RVol 0.7) |
| 24 | **SHOP** | 166.41 | - | **-** | 14 | - | NEG -$5.8M | 172.21 | 175 | 165 | -$65k | - | out (clean 26, ADX 12, RVol 0.4) |
| 25 | **SMCI** | 35.24 | - | **-** | 12 | - | POS +$26.0M | - | 35 | 35 | +$161k | - | out (clean 27, ADX 20, RVol 0.8) |
| 26 | **DELL** | 485.46 | - | **-** | 8 | - | POS +$10.0M | 476.75 | 500 | 500 | +$482k | - | out (clean 30, ADX 29, RVol 0.2) |
| 27 | **PLTR** | 194.31 | - | **-** | 7 | - | POS +$35.0M | 191.53 | 200 | 190 | -$411k | - | out (clean 25, ADX 12, RVol 2.1) |

## Big prints this scan (67)
- **SPY** PUT 775 2026-11-02 (4DTE): 614 @ 6.59 = **+$405k** SELL | vol 8,539 / OI 149
- **TSLA** CALL 412.5 2026-10-30 (1DTE): 2,000 @ 1.69 = **+$338k** BUY | vol 14,618 / OI 4,733
- **MU** CALL 955 2026-10-30 (1DTE): 219 @ 13.30 = **+$291k** BUY | vol 5,536 / OI 878
- **AMD** PUT 562.5 2026-10-30 (1DTE): 391 @ 7.35 = **+$287k** SELL | vol 1,185 / OI 105
- **GOOGL** PUT 295 2026-10-30 (1DTE): 266 @ 9.95 = **+$265k** SELL | vol 5,923 / OI 5,774
- **MU** CALL 970 2026-10-30 (1DTE): 234 @ 7.50 = **+$176k** BUY | vol 4,848 / OI 2,312
- **GOOGL** PUT 290 2026-10-30 (1DTE): 266 @ 5.90 = **+$157k** SELL | vol 5,126 / OI 4,338
- **META** CALL 612.5 2026-10-30 (1DTE): 100 @ 15.60 = **+$156k** BUY | vol 1,827 / OI 95
- **META** CALL 612.5 2026-10-30 (1DTE): 100 @ 15.10 = **+$151k** BUY | vol 1,827 / OI 95
- **SPY** CALL 770 2026-10-29 (0DTE): 1,000 @ 1.45 = **+$145k** BUY | vol 153,538 / OI 1,967
- **QQQ** PUT 716 2026-10-29 (0DTE): 570 @ 2.30 = **+$131k** SELL | vol 38,383 / OI 797
- **AMZN** CALL 247.5 2026-10-30 (1DTE): 130 @ 9.98 = **+$130k** BUY | vol 1,564 / OI 2,330
- **GOOGL** PUT 295 2026-10-30 (1DTE): 116 @ 9.95 = **+$115k** SELL | vol 5,923 / OI 5,774
- **AMZN** CALL 250 2026-10-30 (1DTE): 130 @ 8.79 = **+$114k** BUY | vol 3,590 / OI 7,932
- **TSLA** CALL 420 2026-10-30 (1DTE): 2,000 @ 0.52 = **+$104k** BUY | vol 22,287 / OI 21,999

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 741 2026-10-29 (0DTE): 1,296 traded vs OI 353
- **SPY** PUT 763 2026-10-30 (1DTE): 4,899 traded vs OI 4,871
- **SPY** CALL 769 2026-11-04 (6DTE): 533 traded vs OI 212
- **SPY** CALL 771 2026-11-03 (5DTE): 513 traded vs OI 447
- **SPY** CALL 777 2026-11-02 (4DTE): 517 traded vs OI 336
- **SPY** PUT 756 2026-11-02 (4DTE): 521 traded vs OI 169
- **SPY** CALL 773 2026-11-03 (5DTE): 514 traded vs OI 312
- **SPY** PUT 747 2026-11-06 (8DTE): 1,142 traded vs OI 612
- **SPY** PUT 752 2026-11-06 (8DTE): 1,265 traded vs OI 1,121
- **QQQ** CALL 712 2026-11-04 (6DTE): 500 traded vs OI 126
- **QQQ** PUT 716 2026-11-02 (4DTE): 508 traded vs OI 212
- **QQQ** CALL 730 2026-11-03 (5DTE): 688 traded vs OI 672
- **QQQ** PUT 700 2026-11-05 (7DTE): 875 traded vs OI 665
- **NVDA** CALL 200 2026-10-30 (1DTE): 1,525 traded vs OI 1,178
- **NVDA** CALL 215 2026-11-06 (8DTE): 4,028 traded vs OI 3,077

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
