# GEX + FLOW SCAN - Mon Nov 09, 02:35 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:04 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/09 754C | 0.41 | 0.23 | -2% (0m) | **-44%** (done) | +28% | 752.23 |
| 10:35 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 272.5C | 0.49 | 0.05 | +2% (2m) | **-90%** (done) | +225% | 273.49 |
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.72 | +51% (23m) | **-6%** (done) | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.02 | +13% (6m) | **-96%** (done) | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:35:08 ET, last candle SPY 14:34, QQQ 14:34 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:03 | SPY | 1m WHIPSAW | R1 | CALLS | TURNING away | **FIRE** SPY261109C00754000 |

## Flow surges NOT fired - price disagreed (17 today, last 5)
- 10:55 AVGO PUTS: price +2.40 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 AVGO PUTS: price +1.16 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 QQQ PUTS: price +0.45 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:35 AVGO PUTS: price +1.05 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:30 QQQ PUTS: price +0.53 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AMD** | 506.35 | FLIP CROSS up into positive gamma | **CALLS** | 36 | none: 160 calls 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -100% at the target (needs +20%) (67 contracts' greeks worked out here) | POS +$29.3M | 493.2 | 500 | 500 | -$62.5M | +$6.9M bull / -$138k bear | out (clean 31, ADX 39, RVol 0.4) |
| 2 | **MU** | 727.33 | FLIP CROSS up into positive gamma | **CALLS** | 25 | none: 197 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (78 contracts' greeks worked out here) | POS +$1.7M | 726.63 | 750 | 750 | +$3.8M | +$507k bull / -$1.0M bear | out (clean 30, ADX 13, RVol 0.4) |
| 3 | **SPY** | 752.30 | - | **-** | 23 | - | NEG -$6.0B | 761.7 | 750 | 740 | -$307.0M | +$3.8M bull / +$0 bear | out (clean 31, ADX 32, RVol 0.2) |
| 4 | **TSLA** | 378.60 | - | **-** | 22 | - | POS +$141.3M | - | 380 | 380 | -$90.6M | +$124k bull / +$0 bear | out (clean 33, ADX 21, RVol 0.3) |
| 5 | **QQQ** | 677.49 | - | **-** | 21 | - | NEG -$2.2B | 698.78 | 680 | 680 | -$231.4M | +$401k bull / -$507k bear | out (clean 31, ADX 25, RVol 0.3) |
| 6 | **GOOGL** | 289.62 | PINNED between the walls (positive gamma) - chop | **-** | 21 | - | POS +$12.7M | 289.04 | 290 | 290 | +$4.5M | - | out (clean 31, ADX 26, RVol 0.4) |
| 7 | **AMZN** | 268.01 | - | **-** | 20 | - | POS +$368.1M | - | 270 | 265 | +$20.8M | +$277k bull / +$0 bear | out (clean 32, ADX 9, RVol 0.3) |
| 8 | **AVGO** | 318.94 | - | **-** | 20 | - | NEG -$67.3M | - | 340 | 320 | -$7.1M | +$66k bull / -$28k bear | out (clean 30, ADX 21, RVol 0.5) |
| 9 | **AAPL** | 351.32 | - | **-** | 19 | - | POS +$427.3M | 339.41 | 365 | 350 | -$7.5M | +$782k bull / -$248k bear | out (clean 28, ADX 31, RVol 0.5) |
| 10 | **META** | 643.87 | - | **-** | 19 | - | POS +$175.9M | 615.65 | 650 | 640 | -$11.7M | +$0 bull / -$468k bear | out (clean 32, ADX 22, RVol 0.4) |
| 11 | **IWM** | 282.21 | - | **-** | 18 | - | NEG -$684.4M | 284.59 | 285 | 270 | -$24.2M | - | out (clean 35, ADX 50, RVol 0.3) |
| 12 | **SMH** | 483.77 | - | **-** | 18 | - | NEG -$219.0M | - | 485 | 475 | -$2.6M | +$33k bull / +$0 bear | out (clean 29, ADX 19, RVol 0.3) |
| 13 | **HOOD** | 84.24 | - | **-** | 18 | - | NEG -$1.3M | - | 85 | 85 | -$2.3M | +$0 bull / -$58k bear | out (clean 29, ADX 15, RVol 0.2) |
| 14 | **NVDA** | 175.91 | - | **-** | 17 | - | NEG -$203.3M | - | 190 | 190 | -$40.3M | +$364k bull / -$206k bear | out (clean 32, ADX 20, RVol 0.8) |
| 15 | **MSFT** | 545.21 | - | **-** | 16 | - | POS +$648.2M | - | 550 | 540 | +$1.0M | +$29k bull / -$226k bear | out (clean 33, ADX 27, RVol 0.4) |
| 16 | **PLTR** | 168.65 | - | **-** | 15 | - | POS +$12.0M | - | 165 | 170 | -$1.6M | +$252k bull / +$0 bear | out (clean 30, ADX 14, RVol 0.2) |
| 17 | **ORCL** | 118.86 | - | **-** | 14 | - | NEG -$27.4M | - | 125 | 120 | -$408k | +$0 bull / -$27k bear | out (clean 29, ADX 9, RVol 0.2) |
| 18 | **UBER** | 70.81 | - | **-** | 13 | - | POS +$6.5M | 69.24 | 75 | 70 | -$216k | - | out (clean 32, ADX 42, RVol 0.3) |
| 19 | **COIN** | 136.93 | - | **-** | 12 | - | NEG -$6.7M | - | 140 | 135 | -$2.0M | - | out (clean 32, ADX 11, RVol 0.2) |
| 20 | **SMCI** | 28.79 | - | **-** | 12 | - | NEG -$208k | - | 30 | 30 | -$605k | - | out (clean 29, ADX 32, RVol 0.7) |
| 21 | **SHOP** | 151.31 | - | **-** | 11 | - | POS +$2.0M | - | 150 | 140 | -$77k | - | out (clean 33, ADX 25, RVol 0.1) |
| 22 | **ARM** | 186.04 | - | **-** | 9 | - | NEG -$4.6M | - | 185 | 190 | +$748k | - | out (clean 26, ADX 14, RVol 1.1) |
| 23 | **DELL** | 347.35 | - | **-** | 8 | - | NEG -$6.4M | - | 350 | 340 | +$470k | - | out (clean 33, ADX 30, RVol 0.3) |
| 24 | **CRM** | 214.77 | - | **-** | 7 | - | NEG -$10.8M | - | 195 | 220 | -$41k | - | out (clean 33, ADX 21, RVol 0.6) |
| 25 | **MSTR** | 125.77 | - | **-** | 6 | - | POS +$1.4M | 123.81 | 135 | 120 | -$2.0M | - | out (clean 30, ADX 16, RVol 0.1) |
| 26 | **NFLX** | 63.67 | - | **-** | 5 | - | NEG -$20.7M | - | 65 | 65 | +$166k | - | out (clean 30, ADX 13, RVol 0.4) |
| 27 | **BABA** | 105.18 | - | **-** | 5 | - | POS +$1.9M | 104.21 | 110 | 100 | +$63k | - | out (clean 31, ADX 20, RVol 0.3) |

## Big prints this scan (39)
- **SPY** PUT 755 2026-11-10 (1DTE): 901 @ 4.11 = **+$370k** SELL | vol 5,454 / OI 3,597
- **QQQ** CALL 663 2026-11-10 (1DTE): 190 @ 15.42 = **+$293k** BUY | vol 1,226 / OI 66
- **QQQ** CALL 665 2026-11-09 (0DTE): 190 @ 12.42 = **+$236k** SELL | vol 24,388 / OI 3,005
- **SPY** PUT 753 2026-11-09 (0DTE): 1,978 @ 0.87 = **+$172k** SELL | vol 181,700 / OI 793
- **QQQ** CALL 657 2026-11-09 (0DTE): 76 @ 20.29 = **+$154k** SELL | vol 1,769 / OI 834
- **AMD** CALL 500 2026-11-09 (0DTE): 200 @ 7.00 = **+$140k** BUY | vol 46,874 / OI 1,188
- **MU** CALL 700 2026-11-09 (0DTE): 49 @ 27.65 = **+$135k** SELL | vol 5,907 / OI 761
- **AAPL** CALL 355 2026-11-11 (2DTE): 799 @ 1.65 = **+$132k** BUY | vol 12,274 / OI 505
- **SPY** PUT 745 2026-11-10 (1DTE): 1,242 @ 0.95 = **+$118k** SELL | vol 23,714 / OI 2,145
- **QQQ** CALL 662 2026-11-09 (0DTE): 76 @ 15.32 = **+$116k** SELL | vol 5,170 / OI 851
- **SPY** CALL 750 2026-11-16 (7DTE): 135 @ 8.30 = **+$112k** BUY | vol 2,558 / OI 843
- **AMD** CALL 500 2026-11-11 (2DTE): 60 @ 17.50 = **+$105k** SELL | vol 6,629 / OI 698
- **MU** CALL 700 2026-11-09 (0DTE): 37 @ 27.65 = **+$102k** SELL | vol 5,907 / OI 761
- **MU** PUT 732.5 2026-11-13 (4DTE): 30 @ 30.85 = **+$93k** BUY | vol 381 / OI 246
- **MU** CALL 700 2026-11-09 (0DTE): 32 @ 27.65 = **+$88k** SELL | vol 5,907 / OI 761

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 789 2026-11-12 (3DTE): 789 traded vs OI 394
- **SPY** CALL 765 2026-11-13 (4DTE): 6,680 traded vs OI 6,441
- **QQQ** PUT 679 2026-11-11 (2DTE): 507 traded vs OI 287
- **QQQ** PUT 660 2026-11-13 (4DTE): 7,926 traded vs OI 7,893
- **QQQ** CALL 740 2026-11-20 (11DTE): 508 traded vs OI 0
- **IWM** PUT 276 2026-11-16 (7DTE): 515 traded vs OI 74
- **IWM** PUT 279 2026-11-16 (7DTE): 532 traded vs OI 133
- **IWM** PUT 276 2026-11-10 (1DTE): 1,114 traded vs OI 1,014
- **TSLA** CALL 360 2026-11-13 (4DTE): 1,043 traded vs OI 1,038
- **AMD** PUT 485 2026-11-20 (11DTE): 504 traded vs OI 61
- **AMD** CALL 507.5 2026-11-11 (2DTE): 512 traded vs OI 76
- **META** PUT 607.5 2026-11-11 (2DTE): 597 traded vs OI 596
- **META** PUT 630 2026-11-11 (2DTE): 506 traded vs OI 139
- **AMZN** CALL 290 2026-11-13 (4DTE): 2,074 traded vs OI 2,073
- **MSFT** CALL 542.5 2026-11-13 (4DTE): 504 traded vs OI 472

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
