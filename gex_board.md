# GEX + FLOW SCAN - Fri Nov 06, 09:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (1)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.38 | -5% (0m) | **-5%** | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:50:08 ET, last candle SPY 09:49, QQQ 09:49 | no errors

## Flow surges NOT fired - price disagreed (5 today, last 5)
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 NVDA PUTS: price +2.17 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DELL** | 349.17 | FLOW SURGE | **PUTS** | 63 | none: 53 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (45 contracts' greeks worked out here) | NEG -$24.0M | - | 370 | 350 | -$1.0M | +$0 bull / -$169k bear | out (clean 33, ADX 30, RVol 4.1) |
| 2 | **AMD** | 456.84 | FLOW SURGE | **PUTS** | 62 | none: 148 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (70 contracts' greeks worked out here) | NEG -$150.7M | - | 430 | 450 | -$19.8M | +$0 bull / -$2.3M bear | out (clean 32, ADX 25, RVol 4.7) |
| 3 | **MU** | 718.30 | FLOW SURGE | **PUTS** | 62 | none: 187 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (62 contracts' greeks worked out here) | NEG -$199.3M | - | 700 | 700 | -$40.8M | +$0 bull / -$16.5M bear | out (clean 32, ADX 22, RVol 4.8) |
| 4 | **ARM** | 176.22 | FLOW SURGE | **PUTS** | 61 | none: 28 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (26 contracts' greeks worked out here) | NEG -$21.8M | - | 190 | 170 | -$739k | +$0 bull / -$48k bear | out (clean 26, ADX 17, RVol 3.6) |
| 5 | **NVDA** | 194.11 | FLOW SURGE | **PUTS** | 60 | 11/06 190P @ 0.77 (delta 0.23) = est +144% at 190 | NEG -$332.5M | - | 210 | 190 | -$23.3M | +$0 bull / -$6.6M bear | LONG (clean 34, ADX 29, RVol 3.6) |
| 6 | **META** | 617.67 | FLOW SURGE | **PUTS** | 60 | none: 196 puts 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (83 contracts' greeks worked out here) | NEG -$84.0M | 622.54 | 650 | 610 | -$12.8M | +$109k bull / -$2.5M bear | out (clean 33, ADX 21, RVol 2.9) |
| 7 | **PLTR** | 163.35 | FLOW SURGE | **PUTS** | 60 | 11/06 160P @ 0.71 (delta 0.24) = est +130% at 160 | NEG -$61.1M | - | 165 | 160 | -$3.0M | +$0 bull / -$923k bear | out (clean 28, ADX 26, RVol 3.1) |
| 8 | **SMCI** | 29.29 | FLOW SURGE | **PUTS** | 60 | 11/06 29.5P @ 0.55 (delta 0.57) = est +103% at 28.4 | NEG -$3.9M | - | 30 | 30 | -$393k | +$0 bull / -$454k bear | LONG (clean 34, ADX 28, RVol 1.9) |
| 9 | **SMH** | 474.30 | FLOW SURGE | **PUTS** | 59 | none: 147 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (62 contracts' greeks worked out here) | NEG -$547.3M | - | 505 | 500 | -$4.8M | +$0 bull / -$3.8M bear | out (clean 34, ADX 24, RVol 5.7) |
| 10 | **TSLA** | 354.24 | FLOW SURGE | **PUTS** | 59 | none: 112 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (54 contracts' greeks worked out here) | NEG -$234.2M | - | 370 | 360 | -$19.1M | +$25k bull / -$4.6M bear | out (clean 34, ADX 24, RVol 3.9) |
| 11 | **AAPL** | 340.99 | FLOW SURGE | **PUTS** | 58 | none: 112 puts 0-7DTE > 12 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +1% at the target (needs +20%) (67 contracts' greeks worked out here) | NEG -$57.0M | 342.11 | 350 | 340 | -$4.5M | +$0 bull / -$1.1M bear | out (clean 30, ADX 25, RVol 3.4) |
| 12 | **QQQ** | 662.68 | FLOW SURGE | **PUTS** | 56 | none: 774 puts 0-7DTE > 39 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (229 contracts' greeks worked out here) | NEG -$5.8B | - | 700 | 680 | -$57.0M | +$0 bull / -$21.9M bear | out (clean 35, ADX 21, RVol 5.2) |
| 13 | **HOOD** | 81.51 | FLOW SURGE | **PUTS** | 52 | 11/06 80P @ 0.65 (delta 0.31) = est +59% at 80 | NEG -$14.4M | 85.59 | 85 | 80 | -$759k | +$0 bull / -$131k bear | out (clean 30, ADX 27, RVol 2.5) |
| 14 | **COIN** | 138.19 | FLOW SURGE | **PUTS** | 48 | none: 52 puts 0-7DTE > 3 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +8% at the target (needs +20%) (45 contracts' greeks worked out here) | POS +$10.3M | 136.4 | 142 | 135 | -$757k | +$0 bull / -$224k bear | out (clean 32, ADX 22, RVol 1.4) |
| 15 | **MSTR** | 129.96 | FLOW SURGE | **PUTS** | 48 | 11/06 126P @ 0.75 (delta 0.23) = est +119% at 126.33 | POS +$28.7M | 126.33 | 135 | 125 | -$1.2M | +$0 bull / -$478k bear | out (clean 32, ADX 20, RVol 2.7) |
| 16 | **NFLX** | 63.86 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 45 | 11/06 64C @ 0.40 (delta 0.46) = est +164% at 65 | POS +$10.1M | 63.48 | 65 | 64 | -$131k | - | out (clean 32, ADX 28, RVol 2.5) |
| 17 | **AMZN** | 261.97 | FLOW SURGE | **PUTS** | 43 | none: 84 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (37 contracts' greeks worked out here) | POS +$351.4M | - | 265 | 260 | -$2.4M | +$78k bull / -$520k bear | out (clean 34, ADX 20, RVol 1.7) |
| 18 | **ORCL** | 118.74 | - | **-** | 32 | - | NEG -$61.6M | - | 125 | 120 | -$358k | +$80k bull / +$0 bear | out (clean 31, ADX 18, RVol 1.8) |
| 19 | **MSFT** | 530.73 | - | **-** | 28 | - | POS +$544.4M | 509.36 | 535 | 535 | -$1.2M | +$113k bull / -$709k bear | out (clean 32, ADX 29, RVol 3.1) |
| 20 | **AVGO** | 305.36 | - | **-** | 28 | - | NEG -$143.2M | - | 330 | 300 | -$808k | +$77k bull / -$104k bear | out (clean 31, ADX 27, RVol 4.6) |
| 21 | **SPY** | 740.63 | - | **-** | 25 | - | NEG -$13.9B | 771.13 | 760 | 740 | -$22.4M | +$0 bull / -$2.2M bear | out (clean 36, ADX 21, RVol 3.9) |
| 22 | **GOOGL** | 287.82 | - | **-** | 25 | - | POS +$51.8M | 284.55 | 290 | 290 | +$1.2M | +$89k bull / -$851k bear | out (clean 34, ADX 24, RVol 3.2) |
| 23 | **BABA** | 108.44 | - | **-** | 24 | - | POS +$19.9M | 106.05 | 110 | 110 | -$121k | - | out (clean 35, ADX 20, RVol 4.1) |
| 24 | **IWM** | 272.44 | - | **-** | 22 | - | NEG -$3.4B | 286.35 | 285 | 270 | -$1.2M | +$0 bull / -$724k bear | out (clean 36, ADX 15, RVol 3.8) |
| 25 | **UBER** | 68.98 | - | **-** | 18 | - | POS +$5.4M | 68.51 | 70 | 70 | -$34k | - | out (clean 29, ADX 15, RVol 3.2) |
| 26 | **SHOP** | 146.60 | - | **-** | 13 | - | NEG -$3.3M | 150.52 | 144 | 145 | -$3k | - | out (clean 37, ADX 18, RVol 2.1) |
| 27 | **CRM** | 216.63 | - | **-** | 9 | - | NEG -$22.5M | - | 230 | 220 | -$1k | - | out (clean 33, ADX 23, RVol 3.4) |

## Big prints this scan (813)
- **QQQ** PUT 691 2026-11-13 (7DTE): 758 @ 36.00 = **+$2.7M** BUY | vol 1,850 / OI 2,850
- **QQQ** PUT 678 2026-11-06 (0DTE): 560 @ 21.70 = **+$1.2M** BUY | vol 4,592 / OI 9,812
- **QQQ** PUT 678 2026-11-06 (0DTE): 448 @ 21.69 = **+$972k** BUY | vol 4,592 / OI 9,812
- **QQQ** PUT 675 2026-11-13 (7DTE): 346 @ 23.06 = **+$798k** BUY | vol 771 / OI 6,980
- **QQQ** PUT 668 2026-11-06 (0DTE): 560 @ 12.45 = **+$697k** BUY | vol 4,595 / OI 11,792
- **MU** CALL 697.5 2026-11-09 (3DTE): 287 @ 24.05 = **+$690k** SELL | vol 336 / OI 0
- **TSLA** CALL 357.5 2026-11-13 (7DTE): 700 @ 9.51 = **+$666k** SELL | vol 2,018 / OI 83
- **QQQ** PUT 691 2026-11-13 (7DTE): 161 @ 36.00 = **+$580k** BUY | vol 1,850 / OI 2,850
- **QQQ** PUT 668 2026-11-06 (0DTE): 448 @ 12.44 = **+$557k** BUY | vol 4,595 / OI 11,792
- **QQQ** PUT 678 2026-11-06 (0DTE): 239 @ 22.05 = **+$527k** BUY | vol 4,592 / OI 9,812
- **QQQ** PUT 650 2026-11-13 (7DTE): 474 @ 10.70 = **+$507k** BUY | vol 1,266 / OI 32,092
- **TSLA** CALL 357.5 2026-11-13 (7DTE): 502 @ 9.51 = **+$477k** SELL | vol 2,018 / OI 83
- **TSLA** CALL 357.5 2026-11-13 (7DTE): 502 @ 9.51 = **+$477k** SELL | vol 2,018 / OI 83
- **QQQ** CALL 660 2026-11-06 (0DTE): 1,035 @ 4.36 = **+$451k** SELL | vol 11,179 / OI 330
- **QQQ** PUT 678 2026-11-06 (0DTE): 192 @ 22.06 = **+$424k** BUY | vol 4,592 / OI 9,812

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 751 2026-11-06 (0DTE): 1,734 traded vs OI 550
- **SPY** CALL 756 2026-11-06 (0DTE): 2,304 traded vs OI 1,623
- **SPY** CALL 736 2026-11-09 (3DTE): 1,307 traded vs OI 2
- **SPY** CALL 734 2026-11-09 (3DTE): 978 traded vs OI 8
- **SPY** CALL 744 2026-11-09 (3DTE): 696 traded vs OI 10
- **SPY** CALL 732 2026-11-06 (0DTE): 1,103 traded vs OI 351
- **SPY** PUT 705 2026-11-06 (0DTE): 3,215 traded vs OI 2,566
- **SPY** PUT 733 2026-11-06 (0DTE): 3,603 traded vs OI 3,122
- **SPY** CALL 730 2026-11-06 (0DTE): 587 traded vs OI 272
- **SPY** PUT 702 2026-11-11 (5DTE): 517 traded vs OI 155
- **SPY** CALL 735 2026-11-09 (3DTE): 1,613 traded vs OI 23
- **SPY** CALL 752 2026-11-06 (0DTE): 1,682 traded vs OI 877
- **SPY** CALL 733 2026-11-09 (3DTE): 1,010 traded vs OI 29
- **SPY** CALL 733 2026-11-06 (0DTE): 1,240 traded vs OI 45
- **SPY** CALL 740 2026-11-09 (3DTE): 879 traded vs OI 53

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
