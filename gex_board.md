# GEX + FLOW SCAN - Mon Nov 09, 03:25 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 14:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 11/09 681C | 0.67 | 0.92 | +78% (36m) | **+37%** | +28% | 681.56 |
| 11:04 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/09 754C | 0.41 | 0.23 | -2% (0m) | **-44%** (done) | +28% | 752.23 |
| 10:35 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 272.5C | 0.49 | 0.05 | +2% (2m) | **-90%** (done) | +225% | 273.49 |
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.72 | +51% (23m) | **-6%** (done) | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.02 | +13% (6m) | **-96%** (done) | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:25:08 ET, last candle SPY 15:24, QQQ 15:24 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 15:08 | QQQ | 1m AGREE FLIP | FULL | CALLS | up | logged (agree flip) |
| 15:08 | SPY | 1m AGREE FLIP | FULL | CALLS | up | logged (agree flip) |
| 14:39 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | WITH you | **FIRE** QQQ261109C00681000 |
| 11:03 | SPY | 1m WHIPSAW | R1 | CALLS | TURNING away | **FIRE** SPY261109C00754000 |

## Flow surges NOT fired - price disagreed (17 today, last 5)
- 10:55 AVGO PUTS: price +2.40 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 AVGO PUTS: price +1.16 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 QQQ PUTS: price +0.45 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:35 AVGO PUTS: price +1.05 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:30 QQQ PUTS: price +0.53 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **GOOGL** | 289.49 | FLIP CROSS down into negative gamma | **PUTS** | 33 | none: 92 puts 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (33 contracts' greeks worked out here) | NEG -$925k | 289.53 | 290 | 290 | +$4.4M | +$0 bull / -$88k bear | out (clean 31, ADX 23, RVol 0.7) |
| 2 | **MU** | 738.95 | FLIP CROSS up into positive gamma | **CALLS** | 29 | none: 188 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (72 contracts' greeks worked out here) | POS +$9.2M | 736.47 | 750 | 750 | -$14.8M | +$0 bull / -$1.8M bear | out (clean 30, ADX 20, RVol 0.7) |
| 3 | **IWM** | 283.52 | - | **-** | 28 | - | NEG -$336.8M | 284.42 | 285 | 270 | -$25.5M | +$0 bull / -$587k bear | out (clean 35, ADX 52, RVol 0.8) |
| 4 | **TSLA** | 381.09 | - | **-** | 27 | - | POS +$193.3M | - | 380 | 380 | -$94.0M | +$167k bull / -$187k bear | out (clean 33, ADX 41, RVol 0.8) |
| 5 | **SPY** | 755.08 | - | **-** | 25 | - | NEG -$5.3B | 761.75 | 750 | 755 | -$352.2M | +$0 bull / -$4.0M bear | out (clean 31, ADX 35, RVol 0.8) |
| 6 | **AMD** | 513.58 | - | **-** | 25 | - | POS +$56.5M | - | 510 | 500 | -$69.1M | +$79k bull / -$2.6M bear | out (clean 31, ADX 39, RVol 0.8) |
| 7 | **QQQ** | 681.12 | - | **-** | 23 | - | NEG -$1.7B | 696.02 | 680 | 680 | -$261.5M | +$0 bull / -$1.2M bear | out (clean 30, ADX 33, RVol 0.6) |
| 8 | **AVGO** | 322.32 | - | **-** | 23 | - | NEG -$54.9M | - | 340 | 320 | -$7.9M | +$0 bull / -$1.5M bear | out (clean 30, ADX 29, RVol 1.0) |
| 9 | **META** | 646.56 | - | **-** | 22 | - | POS +$236.5M | 613.44 | 650 | 650 | -$12.7M | +$0 bull / -$535k bear | out (clean 33, ADX 36, RVol 0.6) |
| 10 | **AMZN** | 268.74 | - | **-** | 22 | - | POS +$389.9M | - | 270 | 265 | +$19.4M | +$0 bull / -$158k bear | out (clean 32, ADX 21, RVol 0.5) |
| 11 | **SMH** | 489.33 | - | **-** | 21 | - | NEG -$231.9M | - | 500 | 475 | -$3.2M | +$0 bull / -$217k bear | out (clean 29, ADX 26, RVol 0.5) |
| 12 | **AAPL** | 350.96 | - | **-** | 20 | - | POS +$473.7M | 338.89 | 350 | 350 | -$9.2M | +$542k bull / -$99k bear | out (clean 28, ADX 29, RVol 0.8) |
| 13 | **MSFT** | 547.61 | - | **-** | 20 | - | POS +$716.1M | - | 550 | 535 | +$733k | +$0 bull / -$871k bear | out (clean 33, ADX 42, RVol 0.8) |
| 14 | **HOOD** | 84.45 | - | **-** | 20 | - | NEG -$2.3M | - | 85 | 85 | -$2.7M | +$47k bull / +$0 bear | out (clean 29, ADX 24, RVol 0.5) |
| 15 | **NVDA** | 178.01 | - | **-** | 19 | - | NEG -$174.3M | - | 190 | 190 | -$47.9M | +$0 bull / -$2.1M bear | out (clean 32, ADX 19, RVol 1.5) |
| 16 | **PLTR** | 170.47 | - | **-** | 19 | - | POS +$10.5M | - | 165 | 180 | -$1.8M | +$0 bull / -$102k bear | out (clean 29, ADX 28, RVol 0.9) |
| 17 | **COIN** | 137.84 | - | **-** | 14 | - | NEG -$7.2M | - | 140 | 135 | -$2.0M | - | out (clean 31, ADX 19, RVol 0.4) |
| 18 | **SHOP** | 151.86 | - | **-** | 13 | - | POS +$2.1M | - | 150 | 140 | -$92k | - | out (clean 33, ADX 27, RVol 0.3) |
| 19 | **UBER** | 70.97 | - | **-** | 12 | - | POS +$8.8M | 69.01 | 75 | 70 | -$241k | - | out (clean 31, ADX 35, RVol 0.6) |
| 20 | **SMCI** | 29.02 | - | **-** | 11 | - | POS +$181k | - | 30 | 30 | -$645k | - | out (clean 28, ADX 22, RVol 0.8) |
| 21 | **MSTR** | 127.16 | - | **-** | 10 | - | POS +$2.1M | 123.53 | 135 | 120 | -$2.8M | - | out (clean 30, ADX 28, RVol 0.5) |
| 22 | **ARM** | 187.87 | - | **-** | 10 | - | NEG -$3.4M | - | 200 | 200 | +$668k | - | out (clean 26, ADX 21, RVol 1.3) |
| 23 | **ORCL** | 119.83 | - | **-** | 7 | - | NEG -$26.3M | - | 130 | 125 | -$641k | - | out (clean 28, ADX 26, RVol 0.3) |
| 24 | **NFLX** | 63.73 | - | **-** | 6 | - | NEG -$19.1M | 67.47 | 65 | 65 | +$106k | - | out (clean 29, ADX 16, RVol 1.1) |
| 25 | **DELL** | 349.84 | - | **-** | 6 | - | NEG -$7.1M | - | 350 | 340 | +$377k | - | out (clean 32, ADX 21, RVol 0.3) |
| 26 | **CRM** | 215.36 | - | **-** | 6 | - | NEG -$10.9M | - | 195 | 220 | -$38k | - | out (clean 32, ADX 16, RVol 0.7) |
| 27 | **BABA** | 105.82 | - | **-** | 5 | - | POS +$4.2M | 103.66 | 110 | 110 | +$12k | - | out (clean 30, ADX 25, RVol 0.3) |

## Big prints this scan (64)
- **SPY** PUT 755 2026-11-13 (4DTE): 2,000 @ 5.72 = **+$1.1M** BUY | vol 3,800 / OI 6,821
- **SPY** PUT 745 2026-11-13 (4DTE): 4,000 @ 2.62 = **+$1.0M** BUY | vol 13,913 / OI 29,412
- **META** CALL 635 2026-11-11 (2DTE): 228 @ 14.40 = **+$328k** SELL | vol 1,341 / OI 2,118
- **SPY** PUT 756 2026-11-09 (0DTE): 900 @ 2.19 = **+$197k** BUY | vol 48,727 / OI 382
- **QQQ** CALL 677 2026-11-10 (1DTE): 324 @ 5.88 = **+$191k** SELL | vol 12,035 / OI 161
- **AMD** PUT 510 2026-11-13 (4DTE): 100 @ 18.85 = **+$188k** BUY | vol 389 / OI 1,762
- **AMZN** CALL 270 2026-11-13 (4DTE): 428 @ 3.70 = **+$158k** SELL | vol 6,698 / OI 7,386
- **QQQ** CALL 685 2026-11-12 (3DTE): 324 @ 4.46 = **+$145k** SELL | vol 1,182 / OI 2,662
- **AMD** CALL 520 2026-11-13 (4DTE): 100 @ 14.25 = **+$142k** SELL | vol 3,221 / OI 855
- **SPY** PUT 744 2026-11-12 (3DTE): 670 @ 1.92 = **+$129k** BUY | vol 19,128 / OI 211
- **AMD** PUT 490 2026-11-11 (2DTE): 200 @ 6.40 = **+$128k** BUY | vol 1,759 / OI 46
- **QQQ** CALL 650 2026-11-13 (4DTE): 39 @ 31.28 = **+$122k** SELL | vol 380 / OI 2,240
- **AMD** PUT 510 2026-11-11 (2DTE): 80 @ 13.90 = **+$111k** BUY | vol 367 / OI 88
- **AMD** PUT 500 2026-11-11 (2DTE): 111 @ 9.75 = **+$108k** BUY | vol 2,650 / OI 49
- **SPY** PUT 735 2026-11-13 (4DTE): 840 @ 1.21 = **+$102k** BUY | vol 12,844 / OI 4,866

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 727 2026-11-11 (2DTE): 511 traded vs OI 480
- **SPY** PUT 750 2026-11-12 (3DTE): 1,505 traded vs OI 1,501
- **SPY** CALL 746 2026-11-12 (3DTE): 500 traded vs OI 186
- **QQQ** PUT 631 2026-11-11 (2DTE): 1,086 traded vs OI 0
- **QQQ** CALL 713 2026-11-12 (3DTE): 623 traded vs OI 46
- **QQQ** PUT 617 2026-11-11 (2DTE): 531 traded vs OI 0
- **QQQ** CALL 706 2026-11-13 (4DTE): 500 traded vs OI 329
- **QQQ** CALL 690 2026-11-23 (14DTE): 727 traded vs OI 0
- **IWM** CALL 285 2026-11-13 (4DTE): 3,677 traded vs OI 3,631
- **META** PUT 620 2026-11-13 (4DTE): 709 traded vs OI 695
- **AMZN** PUT 265 2026-11-11 (2DTE): 4,002 traded vs OI 3,998
- **PLTR** CALL 187.5 2026-11-13 (4DTE): 5,864 traded vs OI 0
- **MU** CALL 737.5 2026-11-13 (4DTE): 500 traded vs OI 162

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
