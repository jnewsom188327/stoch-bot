# GEX + FLOW SCAN - Mon Nov 09, 10:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.66 | +51% (23m) | **-14%** | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.06 | +13% (6m) | **-88%** | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:30:08 ET, last candle SPY 10:29, QQQ 10:29 | no errors

## Flow surges NOT fired - price disagreed (13 today, last 5)
- 10:30 QQQ PUTS: price +0.53 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:25 SMCI PUTS: price +0.08 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:20 SMCI PUTS: price +0.50 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:15 SPY PUTS: price +0.94 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:10 SMCI PUTS: price +0.22 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AVGO** | 316.66 | FLOW SURGE | **PUTS** | 51 | none: 104 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (41 contracts' greeks worked out here) | NEG -$69.2M | - | 340 | 320 | -$6.0M | +$152k bull / -$278k bear | out (clean 30, ADX 56, RVol 2.0) |
| 2 | **AMZN** | 268.95 | TREND + FLOW | **CALLS** | 50 | none: 88 calls 0-7DTE > 5 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +6% at the target (needs +20%) (48 contracts' greeks worked out here) | POS +$399.5M | - | 270 | 265 | +$14.5M | +$936k bull / +$0 bear | LONG (clean 35, ADX 38, RVol 1.1) |
| 3 | **SMH** | 481.71 | FLOW SURGE | **PUTS** | 49 | none: 152 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (63 contracts' greeks worked out here) | NEG -$228.2M | - | 500 | 475 | -$3.7M | +$0 bull / -$389k bear | out (clean 31, ADX 43, RVol 1.2) |
| 4 | **QQQ** | 674.50 | FLOW SURGE | **PUTS** | 48 | 11/09 670P @ 0.72 (delta 0.22) = est +143% at 670.37 | NEG -$2.1B | 699.03 | 680 | 680 | -$228.5M | +$0 bull / -$3.7M bear | out (clean 32, ADX 42, RVol 1.2) |
| 5 | **IWM** | 279.46 | FLOW SURGE | **PUTS** | 45 | none: 314 puts 0-7DTE > 20 priced 0.40-0.80 > 3 delta 0.2+ > 3 spread ok > 3 liquid > best one only +20% at the target (needs +20%) (124 contracts' greeks worked out here) | NEG -$1.3B | 284.91 | 285 | 270 | -$12.3M | +$0 bull / -$90k bear | out (clean 32, ADX 44, RVol 0.9) |
| 6 | **HOOD** | 85.03 | FLOW SURGE | **PUTS** | 45 | none: 17 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$1.1M | - | 85 | 85 | -$2.9M | +$0 bull / -$574k bear | out (clean 30, ADX 62, RVol 1.2) |
| 7 | **SMCI** | 29.48 | FLOW SURGE | **PUTS** | 44 | 11/13 27P @ 0.47 (delta 0.21) = est +30% at 28.68 | NEG -$56k | - | 30 | 30 | -$1.0M | +$0 bull / -$48k bear | out (clean 31, ADX 25, RVol 0.8) |
| 8 | **SPY** | 749.14 | FLOW SURGE | **PUTS** | 42 | 11/09 746P @ 0.64 (delta 0.24) = est +110% at 746.24 | NEG -$6.9B | 761.4 | 750 | 740 | -$194.2M | +$0 bull / -$6.8M bear | out (clean 32, ADX 42, RVol 0.7) |
| 9 | **TSLA** | 378.07 | FLOW SURGE | **PUTS** | 42 | none: 120 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (54 contracts' greeks worked out here) | POS +$114.8M | - | 400 | 380 | -$90.3M | +$0 bull / -$2.9M bear | LONG (clean 35, ADX 43, RVol 0.8) |
| 10 | **MSTR** | 127.86 | FLOW SURGE | **PUTS** | 41 | none: 25 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$4.3M | - | 135 | 135 | -$2.5M | +$0 bull / -$510k bear | out (clean 29, ADX 26, RVol 1.7) |
| 11 | **META** | 638.00 | TREND (flow not with it) | **CALLS** | 37 | none: 204 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (81 contracts' greeks worked out here) | POS +$146.8M | 614.01 | 650 | 640 | -$4.8M | +$432k bull / -$488k bear | LONG (clean 33, ADX 44, RVol 1.7) |
| 12 | **MSFT** | 541.42 | TREND + FLOW | **CALLS** | 35 | none: 176 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (83 contracts' greeks worked out here) | POS +$572.9M | - | 550 | 540 | +$2.5M | +$0 bull / -$115k bear | LONG (clean 34, ADX 32, RVol 0.9) |
| 13 | **AAPL** | 350.57 | PINNED between the walls (positive gamma) - chop | **-** | 34 | - | POS +$445.2M | 338.57 | 350 | 350 | -$2.8M | +$0 bull / -$1.2M bear | out (clean 27, ADX 35, RVol 0.7) |
| 14 | **NVDA** | 179.15 | - | **-** | 32 | - | NEG -$172.6M | - | 190 | 190 | -$71.0M | +$793k bull / -$2.3M bear | out (clean 32, ADX 39, RVol 4.0) |
| 15 | **AMD** | 491.50 | - | **-** | 31 | - | POS +$2.2M | 489.58 | 500 | 500 | -$37.7M | +$0 bull / -$3.1M bear | out (clean 33, ADX 51, RVol 1.8) |
| 16 | **DELL** | 348.58 | - | **-** | 28 | - | NEG -$6.2M | - | 350 | 340 | -$744k | +$0 bull / -$28k bear | out (clean 32, ADX 44, RVol 1.3) |
| 17 | **PLTR** | 167.94 | - | **-** | 25 | - | POS +$10.6M | - | 165 | 170 | -$2.4M | +$0 bull / -$92k bear | out (clean 29, ADX 42, RVol 0.6) |
| 18 | **COIN** | 136.94 | - | **-** | 22 | - | NEG -$6.1M | - | 140 | 135 | -$1.4M | - | out (clean 31, ADX 19, RVol 0.5) |
| 19 | **SHOP** | 150.82 | - | **-** | 22 | - | POS +$2.0M | - | 150 | 140 | -$65k | - | out (clean 34, ADX 18, RVol 0.6) |
| 20 | **ARM** | 186.43 | - | **-** | 21 | - | NEG -$4.5M | - | 185 | 190 | +$41k | +$0 bull / -$45k bear | out (clean 26, ADX 46, RVol 1.2) |
| 21 | **GOOGL** | 293.56 | - | **-** | 20 | - | POS +$22.9M | 290.97 | 300 | 290 | +$950k | +$151k bull / -$32k bear | out (clean 32, ADX 34, RVol 1.1) |
| 22 | **ORCL** | 118.94 | - | **-** | 20 | - | NEG -$26.8M | - | 125 | 125 | -$283k | +$0 bull / -$266k bear | out (clean 29, ADX 35, RVol 0.5) |
| 23 | **MU** | 730.68 | - | **-** | 19 | - | NEG -$8.8M | - | 750 | 750 | -$6.8M | +$1.3M bull / -$5.0M bear | out (clean 32, ADX 39, RVol 0.8) |
| 24 | **BABA** | 106.09 | - | **-** | 15 | - | POS +$4.1M | 103.71 | 110 | 110 | +$297k | - | out (clean 32, ADX 33, RVol 1.9) |
| 25 | **NFLX** | 63.70 | - | **-** | 11 | - | NEG -$21.1M | - | 65 | 65 | +$155k | - | out (clean 32, ADX 22, RVol 1.2) |
| 26 | **CRM** | 214.96 | - | **-** | 10 | - | NEG -$11.0M | - | 195 | 220 | +$15k | - | out (clean 34, ADX 22, RVol 0.4) |
| 27 | **UBER** | 69.12 | - | **-** | 6 | - | NEG -$1.5M | 69.43 | 70 | 65 | +$4k | - | out (clean 30, ADX 23, RVol 0.5) |

## Big prints this scan (173)
- **SPY** PUT 744 2026-11-12 (3DTE): 1,821 @ 4.15 = **+$756k** BUY | vol 6,194 / OI 211
- **AAPL** CALL 345 2026-11-09 (0DTE): 1,333 @ 4.47 = **+$596k** SELL | vol 4,049 / OI 1,909
- **AMD** PUT 485 2026-11-13 (4DTE): 200 @ 16.98 = **+$340k** BUY | vol 1,206 / OI 518
- **QQQ** CALL 666 2026-11-09 (0DTE): 330 @ 8.15 = **+$269k** SELL | vol 19,873 / OI 290
- **SPY** PUT 756 2026-11-09 (0DTE): 347 @ 7.54 = **+$262k** BUY | vol 5,104 / OI 382
- **SMH** CALL 460 2026-11-13 (4DTE): 99 @ 26.10 = **+$258k** SELL | vol 305 / OI 589
- **SPY** PUT 730 2026-11-12 (3DTE): 1,821 @ 1.40 = **+$255k** BUY | vol 6,143 / OI 1,056
- **NVDA** CALL 177.5 2026-11-11 (2DTE): 486 @ 5.10 = **+$248k** SELL | vol 6,665 / OI 144
- **QQQ** PUT 670 2026-11-09 (0DTE): 1,963 @ 1.25 = **+$245k** BUY | vol 47,958 / OI 1,802
- **QQQ** CALL 674 2026-11-09 (0DTE): 931 @ 2.51 = **+$234k** SELL | vol 55,150 / OI 2,191
- **MSTR** PUT 125 2026-11-13 (4DTE): 553 @ 4.15 = **+$229k** BUY | vol 1,336 / OI 3,204
- **SMH** CALL 460 2026-11-13 (4DTE): 83 @ 27.25 = **+$226k** MID | vol 305 / OI 589
- **SPY** PUT 756 2026-11-09 (0DTE): 300 @ 7.46 = **+$224k** BUY | vol 5,104 / OI 382
- **SPY** PUT 756 2026-11-09 (0DTE): 275 @ 7.97 = **+$219k** BUY | vol 5,104 / OI 382
- **AMD** CALL 480 2026-11-11 (2DTE): 100 @ 20.00 = **+$200k** SELL | vol 986 / OI 161

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 690 2026-11-09 (0DTE): 2,048 traded vs OI 2,043
- **SPY** CALL 735 2026-11-09 (0DTE): 1,224 traded vs OI 1,205
- **SPY** CALL 751 2026-11-11 (2DTE): 623 traded vs OI 500
- **SPY** PUT 714 2026-11-09 (0DTE): 783 traded vs OI 549
- **SPY** CALL 764 2026-11-11 (2DTE): 561 traded vs OI 413
- **SPY** CALL 755 2026-11-11 (2DTE): 690 traded vs OI 670
- **SPY** CALL 752 2026-11-11 (2DTE): 580 traded vs OI 577
- **SPY** PUT 713 2026-11-09 (0DTE): 816 traded vs OI 798
- **SPY** CALL 767 2026-11-19 (10DTE): 547 traded vs OI 0
- **QQQ** PUT 660 2026-11-12 (3DTE): 1,502 traded vs OI 1,418
- **QQQ** CALL 672 2026-11-10 (1DTE): 3,715 traded vs OI 3,642
- **QQQ** PUT 650 2026-11-11 (2DTE): 2,648 traded vs OI 1,203
- **QQQ** PUT 674 2026-11-10 (1DTE): 699 traded vs OI 224
- **QQQ** PUT 657 2026-11-10 (1DTE): 506 traded vs OI 179
- **QQQ** PUT 668 2026-11-13 (4DTE): 506 traded vs OI 345

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
