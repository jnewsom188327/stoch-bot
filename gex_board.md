# GEX + FLOW SCAN - Fri Nov 13, 10:05 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:05 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 297.5P | 0.74 | 0.71 | -4% (0m) | **-4%** | +288% | 295 |
| 09:55 | **BABA** | **PUTS** | FLOW SURGE | 11/13 94P | 0.51 | 0.37 | -8% (0m) | **-27%** | +49% | 93.36 |
| 09:45 | **UBER** | **CALLS** | TREND + FLOW | 11/13 70C | 0.59 | 0.22 | +0% (1m) | **-63%** | +32% | 70.7 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 127C | 0.46 | 0.16 | +22% (2m) | **-65%** | +48% | 126.38 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:05:08 ET, last candle SPY 10:04, QQQ 10:04 | no errors

## Flow surges NOT fired - price disagreed (19 today, last 5)
- 10:05 HOOD CALLS: price -0.53 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:05 COIN CALLS: price -1.46 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:05 NFLX PUTS: over EMA 20 - flow says one way, price says the other
- 10:05 IWM CALLS: price -1.12 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 HOOD CALLS: price -0.14 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **GOOGL** | 300.18 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 64 | 11/13 297.5P @ 0.74 (delta 0.27) = est +288% at 295 | POS +$261.2M | 289.39 | 300 | 290 | +$10.0M | +$2.7M bull / +$0 bear | out (clean 30, ADX 30, RVol 2.2) |
| 2 | **DELL** | 340.53 | FLOW SURGE | **CALLS** | 62 | none: 54 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (46 contracts' greeks worked out here) | NEG -$5.1M | 355.28 | 360 | 340 | +$1.4M | +$178k bull / +$0 bear | SHORT (clean 38, ADX 34, RVol 2.1) |
| 3 | **HOOD** | 78.09 | FLOW SURGE | **CALLS** | 59 | 11/13 79C @ 0.55 (delta 0.35) = est +28% at 79 | NEG -$10.1M | 79.84 | 81 | 80 | +$1.1M | +$445k bull / +$0 bear | SHORT (clean 35, ADX 52, RVol 1.9) |
| 4 | **SMH** | 482.50 | FLOW SURGE | **CALLS** | 57 | none: 146 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (63 contracts' greeks worked out here) | NEG -$275.3M | 509.02 | 500 | 475 | +$5.5M | +$1.3M bull / +$0 bear | out (clean 30, ADX 39, RVol 1.8) |
| 5 | **NFLX** | 63.78 | FLOW SURGE | **PUTS** | 56 | 11/13 64P @ 0.51 (delta 0.59) = est +45% at 63.32 | NEG -$1.4M | 63.82 | 65 | 65 | -$567k | +$50k bull / -$63k bear | out (clean 31, ADX 44, RVol 2.5) |
| 6 | **TSLA** | 388.11 | FLOW SURGE | **CALLS** | 54 | none: 124 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (54 contracts' greeks worked out here) | POS +$333.3M | - | 400 | 380 | +$51.4M | +$8.3M bull / -$3.2M bear | out (clean 30, ADX 30, RVol 5.0) |
| 7 | **ORCL** | 122.77 | FLOW SURGE | **CALLS** | 54 | 11/13 125C @ 0.56 (delta 0.26) = est +111% at 125 | POS +$2.4M | 122.05 | 130 | 125 | +$1.4M | +$425k bull / +$0 bear | out (clean 31, ADX 32, RVol 2.4) |
| 8 | **IWM** | 276.22 | FLOW SURGE | **CALLS** | 53 | 11/13 277C @ 0.59 (delta 0.37) = est +56% at 277.33 | NEG -$2.6B | 282.72 | 285 | 275 | +$9.5M | +$885k bull / +$0 bear | SHORT (clean 35, ADX 47, RVol 1.2) |
| 9 | **COIN** | 127.35 | FLOW SURGE | **CALLS** | 53 | 11/13 130C @ 0.64 (delta 0.26) = est +151% at 130.53 | NEG -$12.9M | 130.53 | 140 | 125 | +$1.6M | +$1.3M bull / +$0 bear | out (clean 31, ADX 42, RVol 1.9) |
| 10 | **AVGO** | 344.74 | FLOW SURGE | **CALLS** | 51 | none: 108 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (47 contracts' greeks worked out here) | POS +$81.2M | - | 350 | 340 | +$11.5M | +$1.4M bull / +$0 bear | SHORT (clean 35, ADX 35, RVol 1.5) |
| 11 | **AMD** | 536.60 | FLOW SURGE | **CALLS** | 50 | none: 171 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (72 contracts' greeks worked out here) | POS +$84.4M | - | 550 | 550 | +$34.4M | +$7.3M bull / +$0 bear | SHORT (clean 35, ADX 37, RVol 1.8) |
| 12 | **SPY** | 752.28 | FLOW SURGE | **CALLS** | 48 | none: 664 calls 0-7DTE > 16 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (238 contracts' greeks worked out here) | NEG -$7.2B | 759.13 | 775 | 755 | +$159.1M | +$5.1M bull / +$0 bear | out (clean 32, ADX 33, RVol 1.1) |
| 13 | **QQQ** | 678.39 | FLOW SURGE | **CALLS** | 48 | none: 742 calls 0-7DTE > 23 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (270 contracts' greeks worked out here) | NEG -$2.6B | 689.1 | 700 | 680 | +$141.7M | +$7.9M bull / +$0 bear | out (clean 31, ADX 43, RVol 1.0) |
| 14 | **MU** | 763.52 | FLOW SURGE | **CALLS** | 45 | none: 164 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (80 contracts' greeks worked out here) | NEG -$452k | 763.7 | 800 | 750 | +$41.4M | +$10.2M bull / -$551k bear | out (clean 30, ADX 25, RVol 1.4) |
| 15 | **MSFT** | 519.98 | FLIP CROSS down into negative gamma | **PUTS** | 44 | none: 162 puts 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (89 contracts' greeks worked out here) | NEG -$13.1M | 520.54 | 535 | 520 | -$4.0M | +$1.9M bull / -$445k bear | out (clean 32, ADX 42, RVol 1.5) |
| 16 | **NVDA** | 162.12 | FLOW SURGE | **CALLS** | 43 | none: 64 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (29 contracts' greeks worked out here) | NEG -$257.1M | - | 175 | 160 | +$69.1M | +$11.9M bull / -$363k bear | out (clean 31, ADX 13, RVol 1.3) |
| 17 | **PLTR** | 167.87 | FLOW SURGE | **CALLS** | 43 | 11/13 170C @ 0.74 (delta 0.29) = est +68% at 170 | POS +$80.8M | 158.87 | 170 | 170 | +$946k | +$163k bull / -$25k bear | out (clean 28, ADX 30, RVol 1.6) |
| 18 | **ARM** | 189.19 | FLIP CROSS down into negative gamma | **PUTS** | 39 | none: 30 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (25 contracts' greeks worked out here) | POS +$4k | 189.2 | 200 | 190 | -$199k | - | out (clean 32, ADX 43, RVol 2.2) |
| 19 | **SHOP** | 148.75 | FLOW SURGE | **PUTS** | 37 | none: 42 puts 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 0 spread ok > 0 liquid (38 contracts' greeks worked out here) | POS +$6.0M | 145.11 | 150 | 150 | -$60k | +$0 bull / -$58k bear | out (clean 32, ADX 32, RVol 0.9) |
| 20 | **MSTR** | 110.21 | - | **-** | 29 | - | NEG -$36.7M | - | 120 | 110 | +$2.2M | +$865k bull / -$635k bear | out (clean 30, ADX 35, RVol 2.4) |
| 21 | **META** | 632.81 | - | **-** | 28 | - | POS +$23.6M | 631.56 | 650 | 625 | -$6.2M | +$1.1M bull / -$763k bear | out (clean 29, ADX 43, RVol 2.6) |
| 22 | **UBER** | 69.65 | - | **-** | 27 | - | POS +$15.2M | 68.89 | 70 | 70 | +$222k | - | out (clean 33, ADX 33, RVol 0.8) |
| 23 | **AMZN** | 268.00 | - | **-** | 23 | - | POS +$546.9M | - | 270 | 265 | +$1.4M | +$100k bull / -$323k bear | out (clean 30, ADX 31, RVol 1.1) |
| 24 | **AAPL** | 358.66 | - | **-** | 22 | - | POS +$1.3B | 347.55 | 360 | 360 | +$1.6M | +$524k bull / -$654k bear | out (clean 30, ADX 40, RVol 1.8) |
| 25 | **SMCI** | 26.30 | - | **-** | 22 | - | NEG -$2.3M | 27.65 | 27 | 25 | +$151k | - | out (clean 34, ADX 28, RVol 1.2) |
| 26 | **BABA** | 94.14 | - | **-** | 19 | - | NEG -$18.6M | - | 100 | 95 | -$51k | +$151k bull / -$26k bear | out (clean 28, ADX 21, RVol 1.9) |
| 27 | **CRM** | 217.76 | - | **-** | 13 | - | NEG -$5.9M | 221.83 | 220 | 220 | +$18k | - | out (clean 30, ADX 31, RVol 1.6) |

## Big prints this scan (306)
- **TSLA** CALL 400 2026-11-20 (7DTE): 1,899 @ 9.48 = **+$1.8M** BUY | vol 4,563 / OI 21,808
- **TSLA** CALL 387.5 2026-11-13 (0DTE): 496 @ 11.30 = **+$560k** BUY | vol 1,297 / OI 1,715
- **AVGO** PUT 345 2026-11-20 (7DTE): 500 @ 9.75 = **+$488k** SELL | vol 582 / OI 826
- **TSLA** CALL 390 2026-11-13 (0DTE): 496 @ 9.15 = **+$454k** BUY | vol 5,138 / OI 7,011
- **SMH** CALL 500 2026-11-20 (7DTE): 290 @ 11.80 = **+$342k** BUY | vol 469 / OI 3,710
- **MU** CALL 790 2026-11-20 (7DTE): 100 @ 32.50 = **+$325k** BUY | vol 700 / OI 618
- **SPY** CALL 748 2026-11-13 (0DTE): 342 @ 8.76 = **+$300k** BUY | vol 627 / OI 1,992
- **GOOGL** CALL 292.5 2026-11-13 (0DTE): 276 @ 10.69 = **+$295k** BUY | vol 371 / OI 6,063
- **MU** CALL 780 2026-11-20 (7DTE): 77 @ 37.50 = **+$289k** BUY | vol 395 / OI 1,054
- **MSTR** PUT 112 2026-11-20 (7DTE): 508 @ 5.20 = **+$264k** SELL | vol 1,133 / OI 0
- **MSFT** PUT 510 2026-11-20 (7DTE): 499 @ 5.02 = **+$250k** SELL | vol 2,772 / OI 7,174
- **MSFT** PUT 510 2026-11-20 (7DTE): 485 @ 5.09 = **+$247k** SELL | vol 2,772 / OI 7,174
- **MSTR** PUT 112 2026-11-20 (7DTE): 484 @ 4.95 = **+$240k** SELL | vol 1,133 / OI 0
- **MSFT** PUT 510 2026-11-20 (7DTE): 478 @ 5.00 = **+$239k** SELL | vol 2,772 / OI 7,174
- **MU** PUT 780 2026-11-20 (7DTE): 77 @ 29.35 = **+$226k** SELL | vol 948 / OI 1,660

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 763 2026-11-16 (3DTE): 1,656 traded vs OI 1,588
- **SPY** CALL 762 2026-11-16 (3DTE): 2,721 traded vs OI 2,649
- **SPY** CALL 757 2026-11-17 (4DTE): 503 traded vs OI 417
- **SPY** PUT 745 2026-11-16 (3DTE): 1,458 traded vs OI 1,290
- **SPY** PUT 755 2026-11-17 (4DTE): 589 traded vs OI 400
- **SPY** PUT 736 2026-11-16 (3DTE): 509 traded vs OI 506
- **SPY** PUT 744 2026-11-16 (3DTE): 771 traded vs OI 700
- **SPY** CALL 755 2026-11-13 (0DTE): 6,516 traded vs OI 4,616
- **SPY** PUT 680 2026-11-17 (4DTE): 800 traded vs OI 0
- **SPY** PUT 741 2026-11-13 (0DTE): 8,276 traded vs OI 3,860
- **SPY** PUT 747 2026-11-16 (3DTE): 1,044 traded vs OI 910
- **SPY** PUT 736 2026-11-13 (0DTE): 5,926 traded vs OI 3,861
- **SPY** CALL 768 2026-11-16 (3DTE): 2,656 traded vs OI 2,489
- **SPY** PUT 738 2026-11-16 (3DTE): 517 traded vs OI 398
- **SPY** PUT 761 2026-11-13 (0DTE): 5,602 traded vs OI 5,128

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
