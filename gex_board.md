# GEX + FLOW SCAN - Mon Nov 09, 03:55 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 14:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 11/09 681C | 0.67 | 0.55 | +78% (36m) | **-18%** (done) | +28% | 681.56 hit |
| 11:04 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/09 754C | 0.41 | 0.23 | -2% (0m) | **-44%** (done) | +28% | 752.23 |
| 10:35 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 272.5C | 0.49 | 0.05 | +2% (2m) | **-90%** (done) | +225% | 273.49 |
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.72 | +51% (23m) | **-6%** (done) | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.02 | +13% (6m) | **-96%** (done) | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors
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
| 1 | **MSFT** | 545.75 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 40 | none: 176 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (67 contracts' greeks worked out here) | POS +$672.8M | - | 550 | 545 | +$1.4M | +$105k bull / -$78k bear | out (clean 33, ADX 35, RVol 1.1) |
| 2 | **IWM** | 282.56 | - | **-** | 30 | - | NEG -$581.5M | 284.56 | 283 | 270 | -$24.2M | +$135k bull / +$0 bear | out (clean 35, ADX 44, RVol 2.1) |
| 3 | **TSLA** | 378.12 | - | **-** | 28 | - | POS +$195.3M | - | 380 | 380 | -$95.3M | +$233k bull / -$174k bear | out (clean 33, ADX 44, RVol 1.1) |
| 4 | **GOOGL** | 289.03 | FLIP CROSS up into positive gamma | **CALLS** | 27 | none: 92 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (45 contracts' greeks worked out here) | POS +$4.7M | 288.7 | 290 | 290 | +$4.9M | - | out (clean 31, ADX 21, RVol 1.4) |
| 5 | **AMD** | 507.05 | - | **-** | 25 | - | POS +$50.6M | - | 500 | 500 | -$71.0M | +$5.2M bull / +$0 bear | out (clean 31, ADX 38, RVol 1.4) |
| 6 | **AVGO** | 319.15 | - | **-** | 25 | - | NEG -$56.9M | - | 340 | 320 | -$7.7M | +$139k bull / +$0 bear | out (clean 31, ADX 31, RVol 2.2) |
| 7 | **SPY** | 753.24 | - | **-** | 24 | - | NEG -$6.0B | 761.63 | 750 | 740 | -$308.8M | +$8.7M bull / +$0 bear | out (clean 31, ADX 30, RVol 1.7) |
| 8 | **META** | 643.33 | - | **-** | 23 | - | POS +$198.2M | 613.52 | 650 | 640 | -$11.7M | +$739k bull / +$0 bear | out (clean 33, ADX 36, RVol 1.4) |
| 9 | **AMZN** | 268.08 | - | **-** | 23 | - | POS +$328.8M | - | 270 | 265 | +$21.2M | +$512k bull / +$0 bear | out (clean 32, ADX 20, RVol 1.0) |
| 10 | **QQQ** | 679.34 | - | **-** | 22 | - | NEG -$1.7B | 695.41 | 680 | 680 | -$230.8M | +$2.1M bull / +$0 bear | out (clean 31, ADX 32, RVol 0.8) |
| 11 | **NVDA** | 177.99 | - | **-** | 21 | - | NEG -$159.4M | - | 190 | 190 | -$55.5M | +$1.6M bull / -$1.3M bear | out (clean 32, ADX 20, RVol 2.2) |
| 12 | **AAPL** | 351.35 | - | **-** | 20 | - | POS +$443.0M | 338.99 | 365 | 350 | -$12.1M | +$0 bull / -$2.5M bear | out (clean 28, ADX 22, RVol 1.3) |
| 13 | **ORCL** | 119.83 | - | **-** | 20 | - | NEG -$26.3M | - | 130 | 125 | -$582k | +$108k bull / +$0 bear | out (clean 29, ADX 36, RVol 0.8) |
| 14 | **SMH** | 486.28 | - | **-** | 19 | - | NEG -$218.1M | - | 500 | 475 | -$1.5M | +$1.3M bull / -$50k bear | out (clean 29, ADX 30, RVol 0.8) |
| 15 | **MU** | 731.19 | - | **-** | 17 | - | NEG -$13.4M | 733.81 | 800 | 750 | -$14.4M | +$3.5M bull / +$0 bear | out (clean 30, ADX 22, RVol 1.0) |
| 16 | **UBER** | 71.17 | - | **-** | 14 | - | POS +$9.7M | 68.66 | 75 | 70 | -$293k | - | out (clean 32, ADX 36, RVol 1.4) |
| 17 | **SHOP** | 152.25 | - | **-** | 14 | - | POS +$1.9M | - | 150 | 140 | -$89k | - | out (clean 32, ADX 28, RVol 0.7) |
| 18 | **COIN** | 136.78 | - | **-** | 13 | - | NEG -$7.5M | - | 140 | 135 | -$1.9M | - | out (clean 31, ADX 17, RVol 0.9) |
| 19 | **CRM** | 215.06 | - | **-** | 12 | - | NEG -$11.2M | - | 195 | 220 | +$152k | - | out (clean 32, ADX 16, RVol 1.9) |
| 20 | **ARM** | 186.30 | - | **-** | 11 | - | NEG -$4.4M | - | 200 | 200 | +$674k | - | out (clean 26, ADX 20, RVol 1.6) |
| 21 | **PLTR** | 169.86 | - | **-** | 10 | - | POS +$10.5M | - | 165 | 180 | -$1.9M | - | out (clean 29, ADX 30, RVol 1.1) |
| 22 | **SMCI** | 28.70 | - | **-** | 10 | - | POS +$138k | - | 30 | 30 | -$591k | - | out (clean 28, ADX 18, RVol 1.0) |
| 23 | **HOOD** | 83.70 | - | **-** | 10 | - | NEG -$2.3M | - | 85 | 85 | -$2.7M | - | out (clean 29, ADX 20, RVol 0.7) |
| 24 | **NFLX** | 64.11 | - | **-** | 8 | - | NEG -$17.8M | 67.74 | 65 | 65 | +$81k | - | out (clean 29, ADX 23, RVol 1.8) |
| 25 | **MSTR** | 126.25 | - | **-** | 8 | - | POS +$1.3M | 123.76 | 135 | 120 | -$2.6M | - | out (clean 30, ADX 20, RVol 0.6) |
| 26 | **BABA** | 105.38 | - | **-** | 7 | - | NEG -$65k | 105.34 | 110 | 110 | +$55k | - | out (clean 30, ADX 24, RVol 1.1) |
| 27 | **DELL** | 346.20 | - | **-** | 6 | - | NEG -$7.1M | - | 350 | 340 | +$448k | - | out (clean 32, ADX 19, RVol 0.6) |

## Big prints this scan (56)
- **META** CALL 635 2026-11-11 (2DTE): 228 @ 16.20 = **+$369k** BUY | vol 1,580 / OI 2,118
- **QQQ** CALL 649 2026-11-09 (0DTE): 100 @ 32.10 = **+$321k** BUY | vol 225 / OI 0
- **QQQ** CALL 650 2026-11-09 (0DTE): 100 @ 31.10 = **+$311k** BUY | vol 427 / OI 1,963
- **AAPL** CALL 355 2026-11-13 (4DTE): 1,155 @ 1.85 = **+$214k** SELL | vol 16,246 / OI 2,726
- **SPY** PUT 754 2026-11-13 (4DTE): 400 @ 5.19 = **+$208k** SELL | vol 2,367 / OI 1,782
- **SPY** PUT 760 2026-11-11 (2DTE): 190 @ 6.92 = **+$131k** SELL | vol 519 / OI 643
- **SPY** CALL 753 2026-11-10 (1DTE): 300 @ 4.05 = **+$122k** BUY | vol 49,181 / OI 487
- **NVDA** CALL 177.5 2026-11-16 (7DTE): 200 @ 6.05 = **+$121k** SELL | vol 5,308 / OI 12
- **NVDA** CALL 177.5 2026-11-16 (7DTE): 200 @ 6.05 = **+$121k** SELL | vol 5,308 / OI 12
- **NVDA** PUT 175 2026-11-13 (4DTE): 300 @ 3.90 = **+$117k** BUY | vol 27,233 / OI 5,460
- **AMD** CALL 520 2026-11-13 (4DTE): 67 @ 15.90 = **+$107k** BUY | vol 3,700 / OI 855
- **SPY** CALL 754 2026-11-10 (1DTE): 300 @ 3.44 = **+$103k** BUY | vol 40,477 / OI 1,031
- **SPY** PUT 754 2026-11-13 (4DTE): 200 @ 5.12 = **+$102k** SELL | vol 2,367 / OI 1,782
- **SPY** PUT 754 2026-11-13 (4DTE): 200 @ 5.06 = **+$101k** SELL | vol 2,367 / OI 1,782
- **META** CALL 655 2026-11-11 (2DTE): 180 @ 5.45 = **+$98k** BUY | vol 1,454 / OI 1,043

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 756 2026-11-12 (3DTE): 550 traded vs OI 416
- **SPY** CALL 781 2026-11-12 (3DTE): 693 traded vs OI 415
- **SPY** CALL 755 2026-11-12 (3DTE): 2,005 traded vs OI 1,907
- **SPY** CALL 757 2026-11-12 (3DTE): 518 traded vs OI 349
- **SPY** PUT 754 2026-11-13 (4DTE): 2,367 traded vs OI 1,782
- **SPY** PUT 744 2026-11-18 (9DTE): 564 traded vs OI 145
- **QQQ** PUT 655 2026-11-20 (11DTE): 18,652 traded vs OI 17,958
- **IWM** CALL 285 2026-11-17 (8DTE): 501 traded vs OI 134
- **IWM** CALL 292 2026-11-17 (8DTE): 560 traded vs OI 31
- **IWM** CALL 283 2026-11-13 (4DTE): 3,353 traded vs OI 3,055
- **IWM** PUT 275 2026-12-04 (25DTE): 30,648 traded vs OI 1,399
- **SMH** PUT 485 2026-11-09 (0DTE): 504 traded vs OI 35
- **TSLA** CALL 412.5 2026-11-11 (2DTE): 501 traded vs OI 432
- **META** PUT 580 2026-11-20 (11DTE): 1,135 traded vs OI 0
- **META** CALL 647.5 2026-11-13 (4DTE): 505 traded vs OI 77

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
