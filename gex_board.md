# GEX + FLOW SCAN - Wed Nov 04, 10:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 0.60 | -4% (0m) | **-12%** | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.31 | +118% (20m) | **+118%** | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.15 | +2% (1m) | **-72%** | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.18 | -3% (1m) | **-71%** | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:10:08 ET, last candle SPY 10:09, QQQ 10:09 | no errors

## Flow surges NOT fired - price disagreed (11 today, last 5)
- 10:10 SMCI CALLS: price -0.28 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:10 NFLX PUTS: price +0.69 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:10 GOOGL PUTS: price +3.22 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:10 AAPL PUTS: price +0.87 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:05 BABA PUTS: price +0.95 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 283.38 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 76 | 11/04 284C @ 0.50 (delta 0.38) = est +115% at 284.75 | NEG -$465.3M | 284.75 | 285 | 270 | +$13.0M | +$384k bull / +$0 bear | LONG (clean 34, ADX 36, RVol 1.8) |
| 2 | **AMZN** | 270.19 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 76 | 11/04 267.5P @ 0.70 (delta 0.26) = est +248% at 265.58 | POS +$542.2M | - | 270 | 250 | -$37.5M | +$136k bull / -$2.0M bear | LONG (clean 34, ADX 56, RVol 3.3) |
| 3 | **BABA** | 106.77 | FLOW SURGE | **PUTS** | 64 | none: 21 puts 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +17% at the target (needs +20%) | POS +$15.8M | - | 110 | 110 | -$846k | +$0 bull / -$74k bear | LONG (clean 35, ADX 50, RVol 3.7) |
| 4 | **AAPL** | 351.70 | FLOW SURGE | **PUTS** | 59 | 11/04 347.5P @ 0.62 (delta 0.21) = est +28% at 350 | POS +$875.6M | 341.73 | 350 | 350 | -$76.9M | +$0 bull / -$5.6M bear | out (clean 31, ADX 45, RVol 2.8) |
| 5 | **UBER** | 70.96 | FLOW SURGE | **PUTS** | 59 | 11/06 69P @ 0.59 (delta 0.27) = est +33% at 70 | POS +$8.5M | 68.55 | 70 | 65 | -$871k | +$0 bull / -$35k bear | out (clean 30, ADX 44, RVol 2.4) |
| 6 | **MSFT** | 555.07 | FLOW SURGE | **PUTS** | 57 | none: 169 puts 0-7DTE > 13 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (76 contracts' greeks worked out here) | POS +$975.5M | - | 550 | 535 | -$26.1M | +$0 bull / -$3.7M bear | out (clean 29, ADX 59, RVol 3.9) |
| 7 | **GOOGL** | 293.67 | FLOW SURGE | **PUTS** | 57 | 11/04 290P @ 0.55 (delta 0.21) = est +172% at 290 | POS +$97.5M | 284.25 | 300 | 290 | -$21.5M | +$0 bull / -$809k bear | LONG (clean 34, ADX 53, RVol 1.6) |
| 8 | **TSLA** | 386.81 | FLOW SURGE | **PUTS** | 54 | none: 124 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (54 contracts' greeks worked out here) | NEG -$103.5M | 398.77 | 400 | 380 | -$50.1M | +$0 bull / -$4.6M bear | out (clean 31, ADX 30, RVol 2.6) |
| 9 | **SMCI** | 31.81 | FLOW SURGE | **CALLS** | 50 | 11/06 33C @ 0.57 (delta 0.33) = est +52% at 32.75 | POS +$4.3M | - | 34.5 | 30 | +$1.3M | +$83k bull / +$0 bear | out (clean 33, ADX 16, RVol 2.4) |
| 10 | **NFLX** | 65.96 | FLOW SURGE | **PUTS** | 49 | 11/06 65P @ 0.52 (delta 0.32) = est +58% at 65 | POS +$18.8M | - | 65 | 65 | -$2.2M | +$0 bull / -$189k bear | out (clean 30, ADX 54, RVol 1.5) |
| 11 | **ARM** | 202.71 | FLOW SURGE | **CALLS** | 46 | none: 17 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$5.9M | - | 212.5 | 200 | +$200k | +$79k bull / +$0 bear | out (clean 26, ADX 23, RVol 1.4) |
| 12 | **MSTR** | 143.77 | FLOW SURGE | **PUTS** | 45 | none: 24 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$116.2M | - | 135 | 150 | -$2.6M | +$0 bull / -$594k bear | out (clean 30, ADX 39, RVol 1.7) |
| 13 | **COIN** | 150.94 | FLOW SURGE | **PUTS** | 38 | none: 21 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$28.7M | - | 148 | 150 | -$887k | +$0 bull / -$33k bear | out (clean 30, ADX 18, RVol 1.1) |
| 14 | **HOOD** | 87.22 | FLOW SURGE | **PUTS** | 38 | 11/06 83P @ 0.75 (delta 0.21) = est +48% at 85.53 | POS +$1.8M | 85.53 | 90 | 90 | -$1.8M | +$0 bull / -$113k bear | out (clean 29, ADX 16, RVol 1.2) |
| 15 | **QQQ** | 699.49 | - | **-** | 29 | - | NEG -$4.0B | 721.96 | 700 | 680 | -$132.0M | +$9.5M bull / -$11.6M bear | out (clean 30, ADX 35, RVol 1.6) |
| 16 | **SPY** | 767.84 | - | **-** | 28 | - | NEG -$2.4B | 770.3 | 770 | 750 | -$72.3M | +$1.1M bull / -$10.0M bear | out (clean 31, ADX 41, RVol 2.4) |
| 17 | **SMH** | 517.46 | - | **-** | 27 | - | NEG -$402.4M | - | 532.5 | 500 | +$1.7M | +$86k bull / -$29k bear | out (clean 31, ADX 22, RVol 2.9) |
| 18 | **MU** | 836.80 | - | **-** | 27 | - | NEG -$283.7M | - | 850 | 850 | +$33.8M | +$8.7M bull / -$2.9M bear | out (clean 31, ADX 19, RVol 2.4) |
| 19 | **AMD** | 501.29 | - | **-** | 26 | - | NEG -$34.0M | - | 500 | 500 | +$17.9M | +$10.4M bull / -$820k bear | out (clean 32, ADX 31, RVol 8.1) |
| 20 | **PLTR** | 175.43 | - | **-** | 26 | - | NEG -$42.0M | - | 180 | 180 | -$2.9M | +$0 bull / -$506k bear | out (clean 26, ADX 23, RVol 2.1) |
| 21 | **DELL** | 386.38 | - | **-** | 26 | - | NEG -$29.4M | - | 400 | 400 | -$904k | +$836k bull / +$0 bear | out (clean 33, ADX 34, RVol 2.3) |
| 22 | **NVDA** | 205.55 | - | **-** | 22 | - | POS +$69.7M | 204.17 | 210 | 200 | -$2.6M | +$635k bull / -$784k bear | out (clean 29, ADX 32, RVol 2.3) |
| 23 | **META** | 635.50 | - | **-** | 22 | - | POS +$200.7M | 619.31 | 650 | 625 | +$1.1M | +$443k bull / -$371k bear | out (clean 30, ADX 47, RVol 1.5) |
| 24 | **AVGO** | 331.91 | - | **-** | 20 | - | NEG -$70.2M | - | 340 | 330 | +$764k | +$82k bull / -$63k bear | out (clean 30, ADX 20, RVol 1.7) |
| 25 | **ORCL** | 128.25 | - | **-** | 20 | - | NEG -$21.8M | - | 130 | 125 | -$83k | +$256k bull / +$0 bear | out (clean 35, ADX 23, RVol 3.1) |
| 26 | **SHOP** | 148.24 | - | **-** | 16 | - | NEG -$9.7M | - | 160 | 135 | -$50k | - | out (clean 35, ADX 31, RVol 2.9) |
| 27 | **CRM** | 231.68 | - | **-** | 12 | - | NEG -$5.8M | 238.1 | 240 | 220 | -$34k | - | out (clean 30, ADX 47, RVol 0.7) |

## Big prints this scan (216)
- **MSFT** CALL 557.5 2026-11-06 (2DTE): 1,500 @ 3.25 = **+$488k** SELL | vol 2,693 / OI 6,272
- **SPY** CALL 766 2026-11-09 (5DTE): 800 @ 5.76 = **+$461k** SELL | vol 3,764 / OI 0
- **QQQ** PUT 694 2026-11-04 (0DTE): 2,000 @ 2.07 = **+$414k** BUY | vol 14,920 / OI 523
- **MU** CALL 820 2026-11-09 (5DTE): 100 @ 38.20 = **+$382k** BUY | vol 221 / OI 18
- **TSLA** PUT 390 2026-11-04 (0DTE): 480 @ 7.41 = **+$356k** BUY | vol 3,186 / OI 2,517
- **QQQ** CALL 690 2026-11-04 (0DTE): 400 @ 8.13 = **+$325k** SELL | vol 20,788 / OI 3,346
- **MSTR** CALL 140 2026-11-06 (2DTE): 600 @ 4.65 = **+$279k** SELL | vol 2,189 / OI 3,457
- **MSFT** PUT 580 2026-11-06 (2DTE): 90 @ 28.60 = **+$257k** BUY | vol 200 / OI 0
- **SPY** PUT 770 2026-11-06 (2DTE): 450 @ 5.45 = **+$245k** BUY | vol 2,038 / OI 6,117
- **QQQ** CALL 694 2026-11-10 (6DTE): 200 @ 11.85 = **+$237k** SELL | vol 439 / OI 0
- **QQQ** CALL 665 2026-11-04 (0DTE): 68 @ 31.70 = **+$216k** SELL | vol 83 / OI 25
- **SPY** PUT 769 2026-11-06 (2DTE): 435 @ 4.90 = **+$213k** BUY | vol 1,396 / OI 1,155
- **SPY** CALL 772 2026-11-09 (5DTE): 800 @ 2.61 = **+$209k** SELL | vol 4,010 / OI 0
- **QQQ** CALL 670 2026-11-04 (0DTE): 68 @ 26.74 = **+$182k** SELL | vol 110 / OI 10
- **AMD** CALL 490 2026-11-06 (2DTE): 75 @ 23.40 = **+$176k** BUY | vol 1,225 / OI 355

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 751 2026-11-04 (0DTE): 673 traded vs OI 521
- **SPY** CALL 778 2026-11-09 (5DTE): 513 traded vs OI 0
- **SPY** CALL 767 2026-11-09 (5DTE): 697 traded vs OI 0
- **SPY** CALL 784 2026-11-04 (0DTE): 1,657 traded vs OI 462
- **SPY** CALL 770 2026-11-06 (2DTE): 15,682 traded vs OI 15,223
- **SPY** PUT 743 2026-11-05 (1DTE): 547 traded vs OI 0
- **SPY** CALL 774 2026-11-06 (2DTE): 2,087 traded vs OI 1,840
- **SPY** PUT 773 2026-11-04 (0DTE): 586 traded vs OI 277
- **SPY** CALL 759 2026-11-05 (1DTE): 504 traded vs OI 0
- **SPY** CALL 768 2026-11-06 (2DTE): 3,576 traded vs OI 3,380
- **SPY** PUT 766 2026-11-06 (2DTE): 899 traded vs OI 870
- **SPY** CALL 786 2026-11-06 (2DTE): 1,635 traded vs OI 1,194
- **SPY** PUT 756 2026-11-04 (0DTE): 12,868 traded vs OI 12,846
- **SPY** CALL 778 2026-11-16 (12DTE): 1,750 traded vs OI 0
- **SPY** CALL 771 2026-11-16 (12DTE): 1,844 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
