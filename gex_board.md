# GEX + FLOW SCAN - Wed Nov 04, 10:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 0.65 | -4% (0m) | **-4%** | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 0.76 | +42% (9m) | **+27%** | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.29 | +2% (1m) | **-45%** | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.34 | -3% (1m) | **-46%** | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:00:08 ET, last candle SPY 09:59, QQQ 09:59 | no errors

## Flow surges NOT fired - price disagreed (5 today, last 5)
- 10:00 BABA PUTS: price +0.63 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 NFLX PUTS: price +0.54 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 GOOGL PUTS: price +2.25 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 AMZN PUTS: price +2.12 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 NVDA PUTS: price +4.27 over the last 15 min - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 284.06 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 84 | 11/04 285C @ 0.52 (delta 0.34) = est +44% at 284.95 | NEG -$224.6M | 284.95 | 285 | 270 | +$7.4M | +$2.0M bull / -$102k bear | LONG (clean 34, ADX 38, RVol 3.1) |
| 2 | **AMZN** | 270.49 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 76 | 11/04 267.5P @ 0.68 (delta 0.25) = est +258% at 265.7 | POS +$541.2M | - | 270 | 250 | -$32.0M | +$1.5M bull / -$10.5M bear | LONG (clean 34, ADX 52, RVol 5.6) |
| 3 | **GOOGL** | 292.36 | FLOW SURGE | **PUTS** | 63 | 11/04 290P @ 0.69 (delta 0.27) = est +92% at 290 | POS +$100.8M | 282.29 | 300 | 290 | -$16.2M | +$0 bull / -$1.9M bear | LONG (clean 34, ADX 47, RVol 2.4) |
| 4 | **BABA** | 106.39 | FLOW SURGE | **PUTS** | 63 | 11/06 103P @ 0.64 (delta 0.22) = est +27% at 105.29 | POS +$15.5M | - | 110 | 110 | -$524k | +$0 bull / -$40k bear | LONG (clean 35, ADX 44, RVol 4.5) |
| 5 | **AAPL** | 351.69 | FLOW SURGE | **PUTS** | 60 | none: 112 puts 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (70 contracts' greeks worked out here) | POS +$850.3M | 341.33 | 350 | 350 | -$67.8M | +$0 bull / -$11.3M bear | out (clean 31, ADX 39, RVol 3.6) |
| 6 | **MSFT** | 553.12 | FLOW SURGE | **PUTS** | 57 | none: 165 puts 0-7DTE > 14 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (96 contracts' greeks worked out here) | POS +$978.2M | - | 550 | 535 | -$20.2M | +$0 bull / -$7.4M bear | out (clean 28, ADX 54, RVol 5.2) |
| 7 | **MSTR** | 139.88 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 53 | none: 26 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$121.8M | - | 135 | 140 | -$1.0M | +$0 bull / -$717k bear | out (clean 30, ADX 34, RVol 1.9) |
| 8 | **QQQ** | 697.69 | FLOW SURGE | **PUTS** | 52 | none: 612 puts 0-7DTE > 42 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (262 contracts' greeks worked out here) | NEG -$3.9B | 718.78 | 700 | 680 | -$107.5M | +$0 bull / -$9.9M bear | out (clean 30, ADX 32, RVol 2.5) |
| 9 | **NFLX** | 65.73 | FLOW SURGE | **PUTS** | 51 | 11/06 65P @ 0.54 (delta 0.33) = est +39% at 65 | POS +$19.2M | 62.36 | 65 | 65 | -$1.8M | +$0 bull / -$184k bear | out (clean 30, ADX 48, RVol 1.7) |
| 10 | **COIN** | 147.27 | FLOW SURGE | **PUTS** | 41 | none: 22 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$31.8M | - | 148 | 150 | -$722k | +$0 bull / -$202k bear | out (clean 30, ADX 18, RVol 1.5) |
| 11 | **HOOD** | 85.62 | FLOW SURGE | **PUTS** | 37 | none: 17 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$431k | 85.79 | 90 | 90 | -$989k | +$0 bull / -$165k bear | out (clean 29, ADX 16, RVol 1.5) |
| 12 | **SMCI** | 32.38 | - | **-** | 32 | - | POS +$8.1M | - | 34.5 | 33 | +$884k | +$0 bull / -$37k bear | out (clean 33, ADX 14, RVol 3.3) |
| 13 | **UBER** | 69.78 | - | **-** | 32 | - | POS +$5.3M | 68.66 | 70 | 65 | -$628k | - | out (clean 30, ADX 37, RVol 2.5) |
| 14 | **SMH** | 516.37 | - | **-** | 30 | - | NEG -$404.1M | - | 532.5 | 500 | +$1.7M | +$58k bull / -$2.4M bear | out (clean 31, ADX 22, RVol 4.4) |
| 15 | **TSLA** | 383.11 | - | **-** | 30 | - | NEG -$98.0M | 390.16 | 400 | 380 | -$25.0M | +$302k bull / -$13.1M bear | out (clean 31, ADX 31, RVol 4.4) |
| 16 | **ARM** | 203.72 | - | **-** | 29 | - | NEG -$5.8M | - | 212.5 | 200 | +$104k | +$0 bull / -$177k bear | out (clean 26, ADX 25, RVol 1.6) |
| 17 | **MU** | 836.00 | - | **-** | 28 | - | NEG -$266.8M | - | 850 | 850 | +$27.9M | +$2.9M bull / -$9.9M bear | out (clean 31, ADX 20, RVol 3.4) |
| 18 | **PLTR** | 173.63 | - | **-** | 27 | - | NEG -$44.2M | - | 180 | 170 | -$2.6M | +$0 bull / -$1.3M bear | out (clean 26, ADX 24, RVol 3.7) |
| 19 | **SPY** | 767.26 | - | **-** | 26 | - | NEG -$2.5B | 770.3 | 770 | 750 | -$40.3M | +$766k bull / -$11.4M bear | out (clean 30, ADX 37, RVol 2.7) |
| 20 | **AMD** | 498.54 | - | **-** | 26 | - | NEG -$49.5M | - | 500 | 500 | +$14.0M | +$4.4M bull / -$4.1M bear | out (clean 32, ADX 31, RVol 9.3) |
| 21 | **META** | 630.66 | - | **-** | 25 | - | POS +$157.3M | 619.84 | 650 | 625 | +$2.8M | +$4.0M bull / -$455k bear | out (clean 30, ADX 43, RVol 2.1) |
| 22 | **ORCL** | 126.29 | - | **-** | 25 | - | NEG -$27.5M | - | 130 | 125 | +$706k | +$324k bull / -$76k bear | out (clean 35, ADX 26, RVol 3.8) |
| 23 | **DELL** | 381.44 | - | **-** | 23 | - | NEG -$29.4M | - | 400 | 400 | -$263k | +$138k bull / +$0 bear | out (clean 33, ADX 31, RVol 3.5) |
| 24 | **NVDA** | 205.06 | - | **-** | 22 | - | POS +$54.1M | 204.18 | 210 | 200 | -$1.0M | +$257k bull / -$1.8M bear | out (clean 29, ADX 32, RVol 4.5) |
| 25 | **AVGO** | 331.99 | - | **-** | 20 | - | NEG -$65.8M | 345.5 | 340 | 330 | -$308k | +$56k bull / -$315k bear | out (clean 30, ADX 21, RVol 2.3) |
| 26 | **SHOP** | 145.87 | - | **-** | 12 | - | NEG -$11.1M | - | 160 | 135 | -$9k | - | out (clean 34, ADX 34, RVol 3.4) |
| 27 | **CRM** | 230.85 | - | **-** | 10 | - | NEG -$8.6M | 240.23 | 240 | 220 | -$7k | - | out (clean 30, ADX 41, RVol 1.2) |

## Big prints this scan (460)
- **SPY** CALL 737 2026-11-06 (2DTE): 225 @ 29.31 = **+$659k** SELL | vol 227 / OI 270
- **SPY** CALL 739 2026-11-06 (2DTE): 225 @ 27.35 = **+$615k** SELL | vol 249 / OI 303
- **QQQ** PUT 720 2026-11-06 (2DTE): 202 @ 25.56 = **+$516k** BUY | vol 419 / OI 5,428
- **AAPL** CALL 347.5 2026-11-04 (0DTE): 1,654 @ 3.12 = **+$516k** SELL | vol 24,775 / OI 4,478
- **AAPL** CALL 347.5 2026-11-04 (0DTE): 1,556 @ 3.19 = **+$496k** SELL | vol 24,775 / OI 4,478
- **MSFT** CALL 542.5 2026-11-04 (0DTE): 465 @ 9.35 = **+$435k** SELL | vol 1,425 / OI 442
- **QQQ** CALL 690 2026-11-06 (2DTE): 499 @ 8.66 = **+$432k** SELL | vol 3,306 / OI 3,092
- **SPY** PUT 768 2026-11-05 (1DTE): 940 @ 4.43 = **+$416k** BUY | vol 3,691 / OI 0
- **QQQ** CALL 694 2026-11-06 (2DTE): 500 @ 8.13 = **+$406k** SELL | vol 1,452 / OI 566
- **MSFT** CALL 542.5 2026-11-04 (0DTE): 475 @ 8.30 = **+$394k** SELL | vol 1,425 / OI 442
- **SPY** CALL 766 2026-11-06 (2DTE): 788 @ 4.70 = **+$370k** SELL | vol 4,492 / OI 5,917
- **SPY** CALL 766 2026-11-06 (2DTE): 787 @ 4.70 = **+$370k** SELL | vol 4,492 / OI 5,917
- **QQQ** CALL 700 2026-11-06 (2DTE): 998 @ 3.70 = **+$369k** SELL | vol 11,991 / OI 14,914
- **QQQ** CALL 694 2026-11-06 (2DTE): 500 @ 7.31 = **+$366k** SELL | vol 1,452 / OI 566
- **MU** CALL 800 2026-11-04 (0DTE): 79 @ 46.00 = **+$363k** BUY | vol 181 / OI 48

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 771 2026-11-04 (0DTE): 545 traded vs OI 442
- **SPY** PUT 772 2026-11-04 (0DTE): 734 traded vs OI 266
- **SPY** CALL 772 2026-11-06 (2DTE): 2,824 traded vs OI 1,788
- **SPY** PUT 737 2026-11-04 (0DTE): 2,624 traded vs OI 2,466
- **SPY** PUT 755 2026-11-04 (0DTE): 11,739 traded vs OI 10,610
- **SPY** PUT 768 2026-11-04 (0DTE): 3,295 traded vs OI 1,133
- **SPY** CALL 776 2026-11-04 (0DTE): 7,905 traded vs OI 5,386
- **SPY** CALL 792 2026-11-05 (1DTE): 1,006 traded vs OI 0
- **SPY** CALL 779 2026-11-06 (2DTE): 1,991 traded vs OI 1,945
- **SPY** PUT 744 2026-11-04 (0DTE): 1,273 traded vs OI 1,223
- **SPY** PUT 769 2026-11-04 (0DTE): 1,187 traded vs OI 645
- **SPY** CALL 777 2026-11-04 (0DTE): 6,385 traded vs OI 2,762
- **SPY** PUT 743 2026-11-04 (0DTE): 1,377 traded vs OI 1,182
- **SPY** PUT 765 2026-11-05 (1DTE): 3,348 traded vs OI 2,969
- **SPY** PUT 746 2026-11-04 (0DTE): 4,263 traded vs OI 2,676

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
