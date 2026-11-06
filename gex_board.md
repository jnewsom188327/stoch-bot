# GEX + FLOW SCAN - Fri Nov 06, 10:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.33 | -6% (1m) | **-51%** | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.38 | +32% (4m) | **-5%** | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:10:08 ET, last candle SPY 10:09, QQQ 10:09 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NVDA** | 191.71 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 68 | none: 59 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (22 contracts' greeks worked out here) | NEG -$314.9M | 203.17 | 210 | 190 | +$18.3M | +$13.1M bull / -$282k bear | LONG (clean 34, ADX 34, RVol 2.0) |
| 2 | **DELL** | 339.11 | FLOW SURGE | **CALLS** | 52 | none: 49 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (44 contracts' greeks worked out here) | NEG -$26.5M | - | 350 | 350 | +$3.2M | +$178k bull / +$0 bear | out (clean 33, ADX 29, RVol 2.4) |
| 3 | **TSLA** | 357.05 | FLOW SURGE | **PUTS** | 49 | none: 116 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (51 contracts' greeks worked out here) | NEG -$234.4M | - | 370 | 360 | -$66.4M | +$0 bull / -$8.4M bear | LONG (clean 35, ADX 35, RVol 1.0) |
| 4 | **NFLX** | 63.98 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 43 | 11/06 64C @ 0.44 (delta 0.50) = est +138% at 65 | POS +$13.5M | 63.4 | 65 | 64 | -$318k | +$0 bull / -$29k bear | out (clean 32, ADX 27, RVol 1.2) |
| 5 | **AAPL** | 341.40 | FLIP CROSS down into negative gamma | **PUTS** | 34 | none: 112 puts 0-7DTE > 12 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +17% at the target (needs +20%) (54 contracts' greeks worked out here) | NEG -$32.1M | 341.97 | 350 | 340 | -$461k | +$687k bull / -$926k bear | out (clean 30, ADX 22, RVol 1.4) |
| 6 | **GOOGL** | 287.34 | - | **-** | 26 | - | POS +$48.9M | 284.25 | 290 | 290 | +$4.1M | +$159k bull / +$0 bear | out (clean 34, ADX 26, RVol 1.5) |
| 7 | **MU** | 707.78 | - | **-** | 26 | - | NEG -$202.9M | - | 700 | 700 | +$45.2M | +$14.2M bull / -$9.4M bear | out (clean 32, ADX 24, RVol 2.6) |
| 8 | **HOOD** | 79.64 | - | **-** | 26 | - | NEG -$17.2M | 83.26 | 85 | 80 | +$2.0M | +$727k bull / -$293k bear | out (clean 30, ADX 31, RVol 1.3) |
| 9 | **ORCL** | 116.63 | - | **-** | 24 | - | NEG -$55.2M | - | 125 | 115 | +$605k | +$224k bull / +$0 bear | out (clean 31, ADX 17, RVol 1.1) |
| 10 | **AMZN** | 262.44 | - | **-** | 23 | - | POS +$371.5M | - | 265 | 260 | -$3.4M | +$887k bull / -$1.2M bear | out (clean 34, ADX 25, RVol 0.8) |
| 11 | **AVGO** | 301.34 | - | **-** | 23 | - | NEG -$138.9M | - | 330 | 300 | +$1.4M | +$409k bull / -$169k bear | out (clean 31, ADX 27, RVol 2.0) |
| 12 | **SMCI** | 28.68 | TREND (flow not with it) | **CALLS** | 23 | none: 24 calls 0-7DTE > 3 priced 0.40-0.80 > 3 delta 0.2+ > 3 spread ok > 3 liquid > best one only +4% at the target (needs +20%) (20 contracts' greeks worked out here) | NEG -$2.9M | 29.71 | 30 | 29 | -$41k | +$25k bull / -$1.2M bear | LONG (clean 35, ADX 33, RVol 0.7) |
| 13 | **CRM** | 213.51 | - | **-** | 22 | - | NEG -$21.9M | - | 230 | 220 | +$178k | - | out (clean 33, ADX 33, RVol 1.1) |
| 14 | **AMD** | 448.11 | - | **-** | 21 | - | NEG -$159.9M | - | 430 | 450 | -$3.1M | +$5.6M bull / -$10.7M bear | out (clean 32, ADX 29, RVol 2.7) |
| 15 | **PLTR** | 161.35 | - | **-** | 21 | - | NEG -$56.8M | - | 165 | 160 | +$1.0M | +$3.4M bull / -$494k bear | out (clean 28, ADX 34, RVol 1.7) |
| 16 | **ARM** | 171.02 | - | **-** | 21 | - | NEG -$19.7M | - | 180 | 170 | -$364k | +$91k bull / +$0 bear | out (clean 26, ADX 17, RVol 1.0) |
| 17 | **META** | 616.67 | - | **-** | 20 | - | NEG -$108.4M | 622.46 | 650 | 610 | -$3.2M | +$2.3M bull / -$73k bear | out (clean 33, ADX 29, RVol 1.2) |
| 18 | **MSFT** | 531.17 | - | **-** | 20 | - | POS +$602.0M | 509.63 | 535 | 535 | +$540k | +$500k bull / -$134k bear | out (clean 32, ADX 34, RVol 1.2) |
| 19 | **QQQ** | 659.70 | - | **-** | 19 | - | NEG -$4.5B | - | 700 | 680 | +$9.7M | +$11.8M bull / -$4.0M bear | out (clean 35, ADX 24, RVol 1.9) |
| 20 | **SMH** | 466.78 | - | **-** | 19 | - | NEG -$449.1M | - | 505 | 470 | +$37k | +$1.6M bull / -$101k bear | out (clean 34, ADX 24, RVol 3.6) |
| 21 | **SPY** | 739.09 | - | **-** | 18 | - | NEG -$13.1B | 765.73 | 770 | 740 | -$13.3M | +$3.8M bull / -$1.1M bear | out (clean 35, ADX 21, RVol 1.6) |
| 22 | **IWM** | 272.03 | - | **-** | 18 | - | NEG -$3.1B | 284.82 | 285 | 270 | -$2.7M | +$881k bull / +$0 bear | out (clean 35, ADX 13, RVol 1.1) |
| 23 | **UBER** | 69.53 | - | **-** | 17 | - | POS +$9.9M | 68.65 | 70 | 70 | -$98k | - | out (clean 29, ADX 13, RVol 2.1) |
| 24 | **BABA** | 108.53 | - | **-** | 17 | - | POS +$27.6M | 103.42 | 110 | 110 | -$36k | +$0 bull / -$116k bear | out (clean 34, ADX 16, RVol 1.7) |
| 25 | **MSTR** | 126.82 | - | **-** | 16 | - | POS +$3.7M | 126.38 | 135 | 125 | +$212k | +$539k bull / +$0 bear | out (clean 32, ADX 20, RVol 0.9) |
| 26 | **SHOP** | 146.69 | - | **-** | 15 | - | NEG -$4.6M | 151.18 | 144 | 145 | -$76k | - | out (clean 37, ADX 21, RVol 1.7) |
| 27 | **COIN** | 136.27 | - | **-** | 14 | - | POS +$231k | 136.23 | 142 | 135 | -$14k | +$78k bull / +$0 bear | out (clean 32, ADX 18, RVol 0.4) |

## Big prints this scan (249)
- **MU** CALL 722.5 2026-11-06 (0DTE): 499 @ 12.40 = **+$619k** BUY | vol 3,254 / OI 1
- **TSLA** CALL 347.5 2026-11-13 (7DTE): 330 @ 16.73 = **+$552k** SELL | vol 449 / OI 11
- **QQQ** CALL 661 2026-11-09 (3DTE): 350 @ 9.38 = **+$328k** BUY | vol 1,604 / OI 0
- **HOOD** CALL 83 2026-11-13 (7DTE): 1,218 @ 2.61 = **+$318k** BUY | vol 2,532 / OI 426
- **QQQ** CALL 657 2026-11-10 (4DTE): 220 @ 13.98 = **+$308k** BUY | vol 797 / OI 0
- **QQQ** CALL 662 2026-11-09 (3DTE): 350 @ 8.78 = **+$307k** BUY | vol 1,813 / OI 0
- **SMH** CALL 475 2026-11-11 (5DTE): 200 @ 13.60 = **+$272k** BUY | vol 780 / OI 0
- **AVGO** CALL 300 2026-11-06 (0DTE): 500 @ 5.35 = **+$268k** BUY | vol 768 / OI 48
- **MU** PUT 700 2026-11-06 (0DTE): 489 @ 5.40 = **+$264k** SELL | vol 7,726 / OI 2,759
- **SPY** CALL 739 2026-11-06 (0DTE): 569 @ 4.61 = **+$262k** BUY | vol 37,631 / OI 303
- **MU** PUT 700 2026-11-06 (0DTE): 498 @ 5.25 = **+$261k** SELL | vol 7,726 / OI 2,759
- **MU** PUT 717.5 2026-11-06 (0DTE): 196 @ 10.50 = **+$206k** SELL | vol 1,412 / OI 512
- **HOOD** CALL 83 2026-11-13 (7DTE): 782 @ 2.60 = **+$203k** BUY | vol 2,532 / OI 426
- **SPY** CALL 740 2026-11-06 (0DTE): 500 @ 4.00 = **+$200k** BUY | vol 79,204 / OI 314
- **SMH** CALL 475 2026-11-11 (5DTE): 159 @ 12.50 = **+$199k** BUY | vol 780 / OI 0

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 765 2026-11-06 (0DTE): 8,652 traded vs OI 5,800
- **SPY** PUT 741 2026-11-09 (3DTE): 892 traded vs OI 220
- **SPY** CALL 728 2026-11-06 (0DTE): 588 traded vs OI 23
- **SPY** PUT 695 2026-11-11 (5DTE): 542 traded vs OI 471
- **SPY** PUT 731 2026-11-09 (3DTE): 509 traded vs OI 137
- **SPY** PUT 717 2026-11-09 (3DTE): 738 traded vs OI 144
- **SPY** CALL 742 2026-11-10 (4DTE): 525 traded vs OI 3
- **SPY** PUT 675 2026-11-09 (3DTE): 535 traded vs OI 78
- **SPY** PUT 742 2026-11-09 (3DTE): 542 traded vs OI 195
- **SPY** CALL 760 2026-11-11 (5DTE): 720 traded vs OI 521
- **SPY** PUT 742 2026-11-06 (0DTE): 3,363 traded vs OI 2,410
- **SPY** PUT 735 2026-11-06 (0DTE): 26,104 traded vs OI 23,652
- **SPY** CALL 764 2026-11-09 (3DTE): 590 traded vs OI 302
- **SPY** CALL 747 2026-11-11 (5DTE): 569 traded vs OI 2
- **SPY** PUT 716 2026-11-09 (3DTE): 545 traded vs OI 539

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
