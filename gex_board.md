# GEX + FLOW SCAN - Mon Nov 09, 11:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:04 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/09 754C | 0.41 | 0.21 | -2% (0m) | **-49%** | +28% | 752.23 |
| 10:35 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 272.5C | 0.49 | 0.05 | +2% (2m) | **-90%** (done) | +225% | 273.49 |
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.72 | +51% (23m) | **-6%** (done) | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.02 | +13% (6m) | **-96%** (done) | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:50:08 ET, last candle SPY 11:49, QQQ 11:49 | no errors
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
| 1 | **IWM** | 281.37 | FLOW SURGE | **PUTS** | 41 | 11/09 281P @ 0.42 (delta 0.39) = est +74% at 280.45 | NEG -$961.2M | 285.04 | 285 | 270 | -$20.1M | +$0 bull / -$73k bear | out (clean 35, ADX 60, RVol 0.6) |
| 2 | **META** | 640.91 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 40 | none: 208 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (82 contracts' greeks worked out here) | POS +$159.5M | 616.78 | 650 | 640 | -$6.7M | +$0 bull / -$221k bear | out (clean 32, ADX 36, RVol 0.8) |
| 3 | **AMD** | 498.82 | PINNED between the walls (positive gamma) - chop | **-** | 39 | - | POS +$11.3M | 491.21 | 500 | 500 | -$46.8M | +$1.1M bull / -$1.4M bear | out (clean 32, ADX 52, RVol 0.6) |
| 4 | **AAPL** | 349.45 | PINNED between the walls (positive gamma) - chop | **-** | 33 | - | POS +$406.2M | 339.27 | 350 | 350 | -$5.0M | +$91k bull / +$0 bear | out (clean 28, ADX 35, RVol 0.7) |
| 5 | **MU** | 734.41 | FLIP CROSS up into positive gamma | **CALLS** | 32 | none: 191 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (79 contracts' greeks worked out here) | POS +$1.3M | 732.45 | 750 | 750 | -$5.3M | +$2.6M bull / -$1.8M bear | out (clean 32, ADX 42, RVol 0.6) |
| 6 | **PLTR** | 169.65 | - | **-** | 28 | - | POS +$11.1M | - | 165 | 180 | -$4.5M | +$26k bull / +$0 bear | out (clean 30, ADX 47, RVol 0.8) |
| 7 | **SPY** | 750.97 | - | **-** | 27 | - | NEG -$6.7B | 761.9 | 750 | 740 | -$233.6M | +$1.5M bull / -$1.4M bear | out (clean 32, ADX 49, RVol 0.5) |
| 8 | **TSLA** | 377.34 | - | **-** | 27 | - | POS +$118.2M | - | 380 | 380 | -$89.5M | +$444k bull / -$763k bear | out (clean 34, ADX 39, RVol 0.5) |
| 9 | **AVGO** | 317.94 | - | **-** | 27 | - | NEG -$67.1M | - | 340 | 320 | -$6.4M | +$103k bull / -$159k bear | out (clean 31, ADX 58, RVol 0.9) |
| 10 | **QQQ** | 676.50 | - | **-** | 26 | - | NEG -$2.2B | 699.12 | 680 | 680 | -$199.7M | +$625k bull / -$2.2M bear | out (clean 32, ADX 45, RVol 0.5) |
| 11 | **NVDA** | 176.39 | - | **-** | 25 | - | NEG -$193.1M | - | 190 | 190 | -$34.6M | +$1.0M bull / -$2.4M bear | out (clean 32, ADX 43, RVol 3.9) |
| 12 | **HOOD** | 84.14 | - | **-** | 24 | - | NEG -$1.5M | - | 85 | 85 | -$2.0M | +$29k bull / +$0 bear | out (clean 31, ADX 43, RVol 0.8) |
| 13 | **SMH** | 484.23 | - | **-** | 23 | - | NEG -$226.6M | - | 500 | 475 | -$2.3M | +$0 bull / -$52k bear | out (clean 31, ADX 38, RVol 0.6) |
| 14 | **AMZN** | 268.51 | - | **-** | 23 | - | POS +$393.6M | - | 270 | 265 | +$20.1M | +$0 bull / -$80k bear | out (clean 34, ADX 17, RVol 0.5) |
| 15 | **GOOGL** | 291.46 | - | **-** | 20 | - | POS +$17.4M | 288.55 | 300 | 290 | +$3.9M | +$0 bull / -$127k bear | out (clean 31, ADX 20, RVol 1.2) |
| 16 | **MSTR** | 126.45 | - | **-** | 20 | - | POS +$1.8M | 123.36 | 135 | 120 | -$2.5M | +$27k bull / -$124k bear | out (clean 30, ADX 20, RVol 0.6) |
| 17 | **MSFT** | 541.63 | - | **-** | 19 | - | POS +$578.7M | - | 550 | 540 | +$2.2M | +$0 bull / -$63k bear | out (clean 33, ADX 27, RVol 0.4) |
| 18 | **COIN** | 137.64 | - | **-** | 16 | - | NEG -$6.3M | - | 140 | 135 | -$2.0M | - | out (clean 32, ADX 21, RVol 0.3) |
| 19 | **UBER** | 69.80 | - | **-** | 15 | - | POS +$2.3M | 69.2 | 70 | 70 | -$157k | - | out (clean 31, ADX 32, RVol 1.0) |
| 20 | **SMCI** | 29.36 | - | **-** | 14 | - | NEG -$148 | - | 30 | 30 | -$887k | - | out (clean 30, ADX 10, RVol 0.7) |
| 21 | **DELL** | 351.53 | - | **-** | 11 | - | NEG -$6.2M | - | 350 | 340 | -$436k | - | out (clean 32, ADX 45, RVol 0.4) |
| 22 | **ARM** | 188.73 | - | **-** | 11 | - | NEG -$4.5M | - | 185 | 190 | +$129k | - | out (clean 27, ADX 50, RVol 1.1) |
| 23 | **BABA** | 105.45 | - | **-** | 11 | - | POS +$2.3M | 104.15 | 110 | 110 | +$285k | - | out (clean 32, ADX 39, RVol 0.8) |
| 24 | **SHOP** | 150.57 | - | **-** | 10 | - | POS +$1.6M | - | 150 | 140 | -$52k | - | out (clean 35, ADX 16, RVol 0.2) |
| 25 | **CRM** | 214.97 | - | **-** | 7 | - | NEG -$11.3M | - | 195 | 220 | +$19k | - | out (clean 34, ADX 16, RVol 0.8) |
| 26 | **NFLX** | 63.71 | - | **-** | 6 | - | NEG -$20.7M | - | 65 | 65 | +$127k | - | out (clean 31, ADX 16, RVol 0.5) |
| 27 | **ORCL** | 118.88 | - | **-** | 5 | - | NEG -$26.7M | - | 125 | 125 | -$25k | - | out (clean 30, ADX 23, RVol 0.4) |

## Big prints this scan (118)
- **NVDA** PUT 180 2026-11-11 (2DTE): 450 @ 7.75 = **+$349k** BUY | vol 9,154 / OI 2,044
- **NVDA** PUT 180 2026-11-11 (2DTE): 405 @ 7.50 = **+$304k** BUY | vol 9,154 / OI 2,044
- **QQQ** CALL 657 2026-11-13 (4DTE): 139 @ 21.65 = **+$301k** SELL | vol 446 / OI 419
- **NVDA** PUT 180 2026-11-11 (2DTE): 333 @ 7.40 = **+$246k** BUY | vol 9,154 / OI 2,044
- **QQQ** PUT 680 2026-11-16 (7DTE): 200 @ 12.22 = **+$244k** BUY | vol 778 / OI 284
- **TSLA** PUT 380 2026-11-09 (0DTE): 504 @ 3.50 = **+$176k** BUY | vol 20,675 / OI 1,625
- **AMD** CALL 490 2026-11-13 (4DTE): 75 @ 22.85 = **+$171k** SELL | vol 2,411 / OI 1,648
- **AMD** PUT 497.5 2026-11-13 (4DTE): 85 @ 19.20 = **+$163k** BUY | vol 217 / OI 151
- **QQQ** CALL 675 2026-11-09 (0DTE): 790 @ 1.82 = **+$144k** SELL | vol 123,697 / OI 1,713
- **SPY** PUT 749 2026-11-10 (1DTE): 440 @ 3.09 = **+$136k** BUY | vol 13,592 / OI 438
- **MU** CALL 720 2026-11-09 (0DTE): 100 @ 13.00 = **+$130k** SELL | vol 8,746 / OI 643
- **MU** PUT 732.5 2026-11-09 (0DTE): 200 @ 6.45 = **+$129k** BUY | vol 3,267 / OI 101
- **SPY** PUT 748 2026-11-13 (4DTE): 230 @ 5.55 = **+$128k** BUY | vol 2,871 / OI 2,181
- **MU** PUT 747.5 2026-11-13 (4DTE): 31 @ 38.80 = **+$120k** BUY | vol 64 / OI 109
- **SPY** PUT 760 2026-11-13 (4DTE): 100 @ 11.95 = **+$120k** BUY | vol 573 / OI 5,777

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 719 2026-11-10 (1DTE): 575 traded vs OI 307
- **SPY** CALL 760 2026-11-12 (3DTE): 1,169 traded vs OI 1,153
- **SPY** PUT 757 2026-11-09 (0DTE): 808 traded vs OI 807
- **SPY** CALL 765 2026-11-09 (0DTE): 3,759 traded vs OI 3,698
- **SPY** PUT 751 2026-11-13 (4DTE): 1,417 traded vs OI 1,084
- **QQQ** CALL 696 2026-11-10 (1DTE): 537 traded vs OI 86
- **QQQ** PUT 667 2026-11-11 (2DTE): 526 traded vs OI 102
- **QQQ** CALL 701 2026-11-10 (1DTE): 1,310 traded vs OI 281
- **QQQ** CALL 678 2026-11-20 (11DTE): 530 traded vs OI 368
- **SMH** PUT 475 2026-11-09 (0DTE): 518 traded vs OI 209
- **AAPL** PUT 355 2026-11-09 (0DTE): 705 traded vs OI 700
- **AMD** PUT 500 2026-11-11 (2DTE): 581 traded vs OI 49
- **META** PUT 640 2026-11-13 (4DTE): 526 traded vs OI 525
- **GOOGL** CALL 295 2026-11-13 (4DTE): 2,056 traded vs OI 2,015
- **MU** PUT 740 2026-11-11 (2DTE): 623 traded vs OI 66

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
