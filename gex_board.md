# GEX + FLOW SCAN - Mon Nov 09, 10:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:35 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 272.5C | 0.49 | 0.41 | +2% (2m) | **-16%** | +225% | 273.49 |
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.63 | +51% (23m) | **-18%** | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.12 | +13% (6m) | **-75%** | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:40:08 ET, last candle SPY 10:39, QQQ 10:39 | no errors

## Flow surges NOT fired - price disagreed (16 today, last 5)
- 10:40 AVGO PUTS: price +1.16 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 QQQ PUTS: price +0.45 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:35 AVGO PUTS: price +1.05 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:30 QQQ PUTS: price +0.53 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:25 SMCI PUTS: price +0.08 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AMZN** | 270.10 | TREND + FLOW | **CALLS** | 50 | 11/09 272.5C @ 0.46 (delta 0.24) = est +232% at 273.33 | POS +$407.6M | - | 270 | 265 | +$14.4M | +$445k bull / -$75k bear | LONG (clean 35, ADX 36, RVol 1.1) |
| 2 | **QQQ** | 674.49 | FLOW SURGE | **PUTS** | 46 | 11/09 670P @ 0.72 (delta 0.21) = est +122% at 670.59 | NEG -$2.1B | 698.99 | 680 | 680 | -$240.7M | +$184k bull / -$2.4M bear | out (clean 32, ADX 44, RVol 1.0) |
| 3 | **SMH** | 480.85 | FLOW SURGE | **PUTS** | 46 | none: 152 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (59 contracts' greeks worked out here) | NEG -$230.3M | - | 500 | 475 | -$3.7M | +$0 bull / -$258k bear | out (clean 31, ADX 44, RVol 0.9) |
| 4 | **AVGO** | 316.58 | FLOW SURGE | **PUTS** | 46 | 11/09 312.5P @ 0.69 (delta 0.22) = est +152% at 312.5 | NEG -$67.9M | - | 340 | 320 | -$6.6M | +$82k bull / -$154k bear | out (clean 30, ADX 59, RVol 1.3) |
| 5 | **META** | 638.77 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 45 | none: 208 calls 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (78 contracts' greeks worked out here) | POS +$146.7M | 615.86 | 650 | 640 | -$4.0M | +$510k bull / +$0 bear | out (clean 33, ADX 43, RVol 1.5) |
| 6 | **SPY** | 749.46 | FLOW SURGE | **PUTS** | 42 | 11/09 746P @ 0.60 (delta 0.22) = est +98% at 746.77 | NEG -$7.0B | 761.77 | 750 | 740 | -$214.1M | +$0 bull / -$4.9M bear | out (clean 32, ADX 45, RVol 0.6) |
| 7 | **IWM** | 279.97 | FLOW SURGE | **PUTS** | 42 | 11/09 280P @ 0.72 (delta 0.50) = est +64% at 279 | NEG -$1.3B | 285.21 | 285 | 270 | -$13.2M | +$0 bull / -$104k bear | out (clean 33, ADX 48, RVol 0.6) |
| 8 | **MSFT** | 541.35 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 42 | 11/09 545C @ 0.76 (delta 0.24) = est +162% at 545.65 | POS +$575.1M | - | 550 | 540 | +$2.7M | +$0 bull / -$59k bear | out (clean 34, ADX 32, RVol 0.8) |
| 9 | **TSLA** | 377.70 | FLOW SURGE | **PUTS** | 41 | none: 124 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (54 contracts' greeks worked out here) | POS +$113.0M | - | 400 | 380 | -$94.9M | +$166k bull / -$1.4M bear | LONG (clean 35, ADX 45, RVol 0.6) |
| 10 | **AAPL** | 350.79 | PINNED between the walls (positive gamma) - chop | **-** | 39 | - | POS +$459.5M | 337.26 | 350 | 350 | -$10.8M | +$0 bull / -$4.7M bear | out (clean 28, ADX 38, RVol 0.8) |
| 11 | **SHOP** | 150.00 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 34 | none: 22 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$1.0M | 143.26 | 150 | 140 | -$54k | - | out (clean 34, ADX 16, RVol 0.6) |
| 12 | **NVDA** | 178.17 | - | **-** | 31 | - | NEG -$174.7M | - | 190 | 190 | -$69.7M | +$2.2M bull / -$2.9M bear | out (clean 32, ADX 39, RVol 3.6) |
| 13 | **AMD** | 490.34 | - | **-** | 30 | - | POS +$1.2M | 489.28 | 500 | 500 | -$37.8M | +$782k bull / -$2.6M bear | out (clean 33, ADX 52, RVol 1.3) |
| 14 | **HOOD** | 84.97 | - | **-** | 28 | - | NEG -$1.2M | - | 85 | 85 | -$2.7M | +$25k bull / -$264k bear | out (clean 30, ADX 64, RVol 0.8) |
| 15 | **MSTR** | 128.26 | - | **-** | 27 | - | POS +$4.6M | - | 135 | 135 | -$2.6M | +$0 bull / -$349k bear | out (clean 29, ADX 25, RVol 1.6) |
| 16 | **PLTR** | 167.80 | - | **-** | 26 | - | POS +$10.4M | - | 165 | 170 | -$2.5M | +$109k bull / +$0 bear | out (clean 29, ADX 44, RVol 0.5) |
| 17 | **COIN** | 138.01 | - | **-** | 23 | - | NEG -$6.1M | - | 140 | 135 | -$1.5M | - | out (clean 31, ADX 21, RVol 0.6) |
| 18 | **GOOGL** | 293.42 | - | **-** | 20 | - | POS +$25.9M | 289.84 | 300 | 290 | +$1.6M | +$189k bull / +$0 bear | out (clean 32, ADX 34, RVol 0.9) |
| 19 | **SMCI** | 29.33 | - | **-** | 20 | - | NEG -$29k | - | 30 | 30 | -$981k | - | out (clean 31, ADX 22, RVol 0.7) |
| 20 | **MU** | 729.05 | - | **-** | 20 | - | NEG -$7.2M | 742.27 | 750 | 750 | -$7.7M | +$3.8M bull / -$3.7M bear | out (clean 32, ADX 42, RVol 0.7) |
| 21 | **ORCL** | 118.51 | - | **-** | 20 | - | NEG -$26.7M | - | 125 | 120 | -$291k | +$30k bull / +$0 bear | out (clean 30, ADX 36, RVol 0.5) |
| 22 | **BABA** | 106.13 | - | **-** | 19 | - | POS +$3.8M | 103.96 | 110 | 110 | -$83k | +$0 bull / -$111k bear | out (clean 31, ADX 33, RVol 1.2) |
| 23 | **DELL** | 348.20 | - | **-** | 18 | - | NEG -$6.2M | - | 350 | 340 | -$866k | - | out (clean 32, ADX 46, RVol 1.1) |
| 24 | **ARM** | 186.53 | - | **-** | 11 | - | NEG -$4.5M | - | 185 | 190 | +$22k | - | out (clean 26, ADX 48, RVol 1.4) |
| 25 | **NFLX** | 63.73 | - | **-** | 10 | - | NEG -$20.1M | - | 65 | 65 | +$172k | - | out (clean 32, ADX 21, RVol 0.7) |
| 26 | **UBER** | 69.28 | - | **-** | 6 | - | NEG -$260k | 69.32 | 70 | 65 | -$6k | - | out (clean 30, ADX 22, RVol 0.5) |
| 27 | **CRM** | 215.29 | - | **-** | 6 | - | NEG -$11.4M | - | 195 | 220 | -$6k | - | out (clean 34, ADX 24, RVol 0.4) |

## Big prints this scan (102)
- **AMD** CALL 510 2026-11-13 (4DTE): 479 @ 11.45 = **+$548k** BUY | vol 2,170 / OI 452
- **SPY** CALL 740 2026-11-10 (1DTE): 322 @ 10.51 = **+$338k** SELL | vol 2,609 / OI 11,269
- **NVDA** PUT 185 2026-11-09 (0DTE): 500 @ 6.07 = **+$304k** SELL | vol 5,615 / OI 2,768
- **NVDA** PUT 180 2026-11-13 (4DTE): 500 @ 6.02 = **+$301k** SELL | vol 7,680 / OI 7,865
- **MU** CALL 700 2026-11-09 (0DTE): 100 @ 29.85 = **+$298k** SELL | vol 5,120 / OI 761
- **SPY** PUT 732 2026-11-13 (4DTE): 1,250 @ 1.99 = **+$249k** BUY | vol 1,549 / OI 2,290
- **SPY** PUT 756 2026-11-09 (0DTE): 300 @ 7.01 = **+$210k** BUY | vol 6,663 / OI 382
- **SPY** PUT 756 2026-11-09 (0DTE): 300 @ 6.94 = **+$208k** BUY | vol 6,663 / OI 382
- **NVDA** PUT 182.5 2026-11-11 (2DTE): 295 @ 6.70 = **+$198k** MID | vol 1,586 / OI 1,031
- **QQQ** CALL 642 2026-11-13 (4DTE): 56 @ 34.66 = **+$194k** SELL | vol 56 / OI 0
- **QQQ** CALL 659 2026-11-09 (0DTE): 120 @ 15.47 = **+$186k** SELL | vol 1,158 / OI 403
- **QQQ** CALL 644 2026-11-13 (4DTE): 56 @ 32.90 = **+$184k** BUY | vol 56 / OI 0
- **QQQ** CALL 660 2026-11-09 (0DTE): 120 @ 14.49 = **+$174k** SELL | vol 3,542 / OI 6,104
- **NVDA** CALL 172.5 2026-11-09 (0DTE): 272 @ 6.05 = **+$165k** SELL | vol 11,929 / OI 0
- **NVDA** PUT 185 2026-11-09 (0DTE): 250 @ 6.49 = **+$162k** SELL | vol 5,615 / OI 2,768

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 732 2026-11-11 (2DTE): 1,821 traded vs OI 607
- **SPY** PUT 726 2026-11-11 (2DTE): 966 traded vs OI 281
- **SPY** PUT 749 2026-11-16 (7DTE): 585 traded vs OI 192
- **SPY** PUT 729 2026-11-13 (4DTE): 1,442 traded vs OI 1,387
- **SPY** CALL 750 2026-11-17 (8DTE): 559 traded vs OI 556
- **SPY** PUT 745 2026-11-16 (7DTE): 582 traded vs OI 438
- **SPY** CALL 745 2026-11-16 (7DTE): 803 traded vs OI 781
- **QQQ** CALL 717 2026-11-09 (0DTE): 530 traded vs OI 143
- **QQQ** CALL 674 2026-11-11 (2DTE): 535 traded vs OI 91
- **QQQ** PUT 659 2026-11-11 (2DTE): 521 traded vs OI 173
- **QQQ** PUT 610 2026-11-09 (0DTE): 2,277 traded vs OI 2,198
- **QQQ** CALL 690 2026-11-13 (4DTE): 2,911 traded vs OI 2,890
- **QQQ** CALL 688 2026-11-13 (4DTE): 511 traded vs OI 504
- **IWM** CALL 284 2026-11-13 (4DTE): 1,333 traded vs OI 1,222
- **IWM** CALL 285 2026-11-11 (2DTE): 864 traded vs OI 774

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
