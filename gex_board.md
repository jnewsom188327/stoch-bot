# GEX + FLOW SCAN - Mon Nov 09, 03:15 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 14:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 11/09 681C | 0.67 | 0.78 | +72% (3m) | **+16%** | +28% | 681.56 |
| 11:04 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/09 754C | 0.41 | 0.23 | -2% (0m) | **-44%** (done) | +28% | 752.23 |
| 10:35 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 272.5C | 0.49 | 0.05 | +2% (2m) | **-90%** (done) | +225% | 273.49 |
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.72 | +51% (23m) | **-6%** (done) | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.02 | +13% (6m) | **-96%** (done) | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:15:08 ET, last candle SPY 15:14, QQQ 15:14 | no errors
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
| 1 | **TSLA** | 380.89 | PINNED between the walls (positive gamma) - chop | **-** | 39 | - | POS +$181.6M | - | 380 | 380 | -$92.9M | +$239k bull / -$748k bear | out (clean 33, ADX 38, RVol 0.6) |
| 2 | **META** | 645.40 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 38 | 11/09 647.5C @ 0.63 (delta 0.28) = est +294% at 650 | POS +$226.9M | 613.68 | 650 | 645 | -$12.6M | +$134k bull / -$28k bear | out (clean 33, ADX 33, RVol 0.5) |
| 3 | **GOOGL** | 289.60 | PINNED between the walls (positive gamma) - chop | **-** | 32 | - | POS +$3.4M | 289.3 | 290 | 290 | +$4.7M | +$0 bull / -$31k bear | out (clean 31, ADX 25, RVol 0.6) |
| 4 | **IWM** | 283.53 | - | **-** | 28 | - | NEG -$296.5M | 284.44 | 285 | 270 | -$25.4M | +$0 bull / -$445k bear | out (clean 34, ADX 51, RVol 0.7) |
| 5 | **MU** | 735.24 | FLIP CROSS up into positive gamma | **CALLS** | 27 | none: 191 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (73 contracts' greeks worked out here) | POS +$4.9M | 733.91 | 750 | 750 | -$10.9M | +$239k bull / -$2.2M bear | out (clean 30, ADX 16, RVol 0.5) |
| 6 | **SPY** | 754.90 | - | **-** | 24 | - | NEG -$5.4B | 761.6 | 750 | 755 | -$342.0M | +$257k bull / -$1.6M bear | out (clean 31, ADX 34, RVol 0.6) |
| 7 | **AMD** | 511.49 | - | **-** | 24 | - | POS +$58.9M | - | 500 | 500 | -$65.8M | +$608k bull / -$940k bear | out (clean 30, ADX 37, RVol 0.6) |
| 8 | **QQQ** | 680.63 | - | **-** | 22 | - | NEG -$1.8B | 695.25 | 680 | 680 | -$255.5M | +$699k bull / -$779k bear | out (clean 30, ADX 31, RVol 0.5) |
| 9 | **AVGO** | 322.03 | - | **-** | 21 | - | NEG -$62.7M | - | 340 | 320 | -$7.7M | +$127k bull / -$1.5M bear | out (clean 30, ADX 26, RVol 0.5) |
| 10 | **SMH** | 488.30 | - | **-** | 20 | - | NEG -$233.4M | - | 500 | 475 | -$2.8M | +$0 bull / -$27k bear | out (clean 29, ADX 23, RVol 0.4) |
| 11 | **AAPL** | 351.65 | - | **-** | 20 | - | POS +$531.1M | 338 | 350 | 350 | -$10.3M | +$0 bull / -$145k bear | out (clean 28, ADX 32, RVol 0.5) |
| 12 | **HOOD** | 84.89 | - | **-** | 20 | - | NEG -$1.4M | - | 85 | 85 | -$2.8M | +$84k bull / +$0 bear | out (clean 29, ADX 24, RVol 0.3) |
| 13 | **MSFT** | 547.74 | - | **-** | 19 | - | POS +$730.2M | - | 550 | 535 | +$984k | +$111k bull / -$835k bear | out (clean 33, ADX 40, RVol 0.6) |
| 14 | **NVDA** | 177.64 | - | **-** | 18 | - | NEG -$182.1M | - | 190 | 190 | -$45.6M | +$96k bull / -$761k bear | out (clean 32, ADX 17, RVol 1.1) |
| 15 | **PLTR** | 170.04 | - | **-** | 17 | - | POS +$10.5M | - | 165 | 180 | -$1.7M | +$0 bull / -$102k bear | out (clean 29, ADX 24, RVol 0.4) |
| 16 | **ORCL** | 119.63 | - | **-** | 17 | - | NEG -$26.1M | - | 130 | 125 | -$602k | +$0 bull / -$28k bear | out (clean 28, ADX 22, RVol 0.2) |
| 17 | **COIN** | 138.08 | - | **-** | 13 | - | NEG -$6.8M | - | 140 | 135 | -$2.0M | - | out (clean 32, ADX 17, RVol 0.4) |
| 18 | **SHOP** | 151.78 | - | **-** | 13 | - | POS +$2.1M | - | 150 | 140 | -$92k | - | out (clean 33, ADX 27, RVol 0.3) |
| 19 | **UBER** | 70.94 | - | **-** | 12 | - | POS +$8.5M | 69.04 | 75 | 70 | -$240k | - | out (clean 31, ADX 36, RVol 0.5) |
| 20 | **AMZN** | 268.89 | - | **-** | 11 | - | POS +$408.4M | - | 270 | 265 | +$19.7M | - | out (clean 32, ADX 18, RVol 0.4) |
| 21 | **SMCI** | 29.00 | - | **-** | 11 | - | POS +$242k | - | 30 | 30 | -$622k | - | out (clean 28, ADX 22, RVol 0.8) |
| 22 | **MSTR** | 127.70 | - | **-** | 10 | - | POS +$2.8M | 123.41 | 135 | 120 | -$2.9M | - | out (clean 30, ADX 28, RVol 0.6) |
| 23 | **ARM** | 188.27 | - | **-** | 9 | - | NEG -$3.2M | - | 200 | 200 | +$671k | - | out (clean 26, ADX 19, RVol 0.8) |
| 24 | **DELL** | 348.72 | - | **-** | 6 | - | NEG -$7.1M | - | 350 | 340 | +$422k | - | out (clean 32, ADX 21, RVol 0.2) |
| 25 | **CRM** | 215.69 | - | **-** | 6 | - | NEG -$11.3M | - | 230 | 220 | -$37k | - | out (clean 32, ADX 18, RVol 0.6) |
| 26 | **NFLX** | 63.77 | - | **-** | 5 | - | NEG -$19.9M | 67.5 | 65 | 65 | +$105k | - | out (clean 30, ADX 15, RVol 0.7) |
| 27 | **BABA** | 105.58 | - | **-** | 5 | - | POS +$3.6M | 103.82 | 110 | 110 | +$42k | - | out (clean 30, ADX 22, RVol 0.2) |

## Big prints this scan (48)
- **MSFT** CALL 555 2026-11-13 (4DTE): 2,000 @ 3.59 = **+$718k** SELL | vol 3,052 / OI 1,246
- **QQQ** PUT 681 2026-11-10 (1DTE): 499 @ 5.59 = **+$279k** BUY | vol 907 / OI 65
- **SPY** CALL 753 2026-11-09 (0DTE): 1,993 @ 1.14 = **+$227k** SELL | vol 529,105 / OI 1,206
- **AVGO** CALL 315 2026-11-16 (7DTE): 150 @ 12.30 = **+$184k** SELL | vol 469 / OI 16
- **AVGO** CALL 315 2026-11-16 (7DTE): 150 @ 12.30 = **+$184k** SELL | vol 469 / OI 16
- **AVGO** CALL 315 2026-11-16 (7DTE): 150 @ 12.30 = **+$184k** SELL | vol 469 / OI 16
- **SPY** PUT 754 2026-11-11 (2DTE): 250 @ 4.13 = **+$103k** BUY | vol 1,628 / OI 235
- **AMD** CALL 517.5 2026-11-11 (2DTE): 89 @ 10.20 = **+$91k** SELL | vol 344 / OI 9
- **AVGO** CALL 322.5 2026-11-13 (4DTE): 112 @ 7.40 = **+$83k** SELL | vol 721 / OI 166
- **AVGO** CALL 322.5 2026-11-13 (4DTE): 112 @ 7.40 = **+$83k** SELL | vol 721 / OI 166
- **MSFT** CALL 575 2026-11-13 (4DTE): 2,000 @ 0.36 = **+$72k** SELL | vol 2,725 / OI 1,265
- **MU** PUT 725 2026-11-16 (7DTE): 25 @ 28.60 = **+$72k** BUY | vol 280 / OI 10
- **AVGO** CALL 330 2026-11-13 (4DTE): 150 @ 4.40 = **+$66k** SELL | vol 5,097 / OI 1,228
- **AVGO** CALL 330 2026-11-13 (4DTE): 150 @ 4.40 = **+$66k** SELL | vol 5,097 / OI 1,228
- **AVGO** CALL 330 2026-11-13 (4DTE): 150 @ 4.40 = **+$66k** SELL | vol 5,097 / OI 1,228

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 712 2026-11-12 (3DTE): 649 traded vs OI 638
- **SPY** PUT 714 2026-11-11 (2DTE): 676 traded vs OI 335
- **SPY** CALL 782 2026-11-12 (3DTE): 521 traded vs OI 474
- **SPY** CALL 830 2026-11-17 (8DTE): 2,200 traded vs OI 0
- **SPY** CALL 753 2026-11-17 (8DTE): 617 traded vs OI 63
- **SPY** PUT 723 2026-11-16 (7DTE): 810 traded vs OI 136
- **SPY** PUT 709 2026-11-17 (8DTE): 551 traded vs OI 139
- **QQQ** PUT 670 2026-11-17 (8DTE): 501 traded vs OI 137
- **QQQ** PUT 678 2026-11-20 (11DTE): 1,187 traded vs OI 1,154
- **IWM** CALL 289 2026-11-10 (1DTE): 520 traded vs OI 160
- **IWM** CALL 291 2026-11-12 (3DTE): 715 traded vs OI 108
- **IWM** CALL 286 2026-11-19 (10DTE): 688 traded vs OI 138
- **IWM** PUT 280 2026-11-19 (10DTE): 630 traded vs OI 48
- **IWM** PUT 274 2026-12-04 (25DTE): 3,114 traded vs OI 152
- **AMZN** PUT 242.5 2026-11-11 (2DTE): 1,289 traded vs OI 105

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
