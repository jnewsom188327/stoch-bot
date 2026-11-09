# GEX + FLOW SCAN - Mon Nov 09, 12:50 PM ET
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
Last 1m check 12:50:08 ET, last candle SPY 12:49, QQQ 12:49 | no errors
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
| 1 | **IWM** | 281.69 | - | **-** | 29 | - | NEG -$865.2M | 284.95 | 285 | 270 | -$20.6M | +$0 bull / -$94k bear | out (clean 35, ADX 58, RVol 0.5) |
| 2 | **AVGO** | 320.86 | - | **-** | 29 | - | NEG -$65.2M | - | 340 | 320 | -$8.9M | +$30k bull / -$118k bear | out (clean 31, ADX 54, RVol 1.5) |
| 3 | **MU** | 733.39 | FLIP CROSS up into positive gamma | **CALLS** | 28 | none: 190 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (77 contracts' greeks worked out here) | POS +$7.7M | 726.97 | 750 | 750 | -$9.9M | +$291k bull / -$232k bear | out (clean 31, ADX 29, RVol 0.2) |
| 4 | **SPY** | 752.53 | - | **-** | 27 | - | NEG -$6.2B | 761.6 | 750 | 740 | -$299.3M | +$2.2M bull / -$9.0M bear | out (clean 32, ADX 52, RVol 0.4) |
| 5 | **QQQ** | 677.56 | - | **-** | 25 | - | NEG -$2.1B | 697.97 | 680 | 680 | -$225.3M | +$3.2M bull / -$377k bear | out (clean 32, ADX 43, RVol 0.6) |
| 6 | **TSLA** | 377.61 | - | **-** | 25 | - | POS +$119.9M | - | 380 | 380 | -$91.7M | +$150k bull / +$0 bear | out (clean 34, ADX 30, RVol 0.3) |
| 7 | **AMD** | 502.81 | - | **-** | 25 | - | POS +$22.5M | 489.15 | 500 | 500 | -$53.1M | +$758k bull / -$422k bear | out (clean 32, ADX 47, RVol 0.5) |
| 8 | **CRM** | 216.82 | - | **-** | 23 | - | NEG -$12.8M | - | 230 | 220 | -$81k | +$0 bull / -$26k bear | out (clean 34, ADX 31, RVol 0.6) |
| 9 | **NVDA** | 177.63 | - | **-** | 21 | - | NEG -$199.6M | - | 190 | 190 | -$58.0M | +$722k bull / -$561k bear | out (clean 33, ADX 25, RVol 1.3) |
| 10 | **META** | 642.60 | - | **-** | 20 | - | POS +$165.2M | 616.69 | 650 | 640 | -$8.3M | +$52k bull / -$180k bear | out (clean 32, ADX 34, RVol 0.4) |
| 11 | **AAPL** | 349.31 | PINNED between the walls (positive gamma) - chop | **-** | 18 | - | POS +$392.1M | 339.2 | 350 | 350 | -$4.8M | - | out (clean 27, ADX 26, RVol 0.3) |
| 12 | **MSFT** | 543.91 | - | **-** | 18 | - | POS +$624.9M | - | 550 | 540 | +$1.5M | +$75k bull / +$0 bear | out (clean 34, ADX 32, RVol 0.3) |
| 13 | **GOOGL** | 291.14 | - | **-** | 18 | - | POS +$15.3M | 288.72 | 300 | 290 | +$4.2M | +$26k bull / +$0 bear | out (clean 31, ADX 13, RVol 0.6) |
| 14 | **NFLX** | 63.79 | - | **-** | 15 | - | NEG -$19.2M | - | 65 | 65 | +$63k | +$25k bull / +$0 bear | out (clean 30, ADX 17, RVol 0.6) |
| 15 | **COIN** | 136.63 | - | **-** | 14 | - | NEG -$6.7M | - | 140 | 135 | -$1.9M | - | out (clean 32, ADX 14, RVol 0.6) |
| 16 | **SMCI** | 29.34 | - | **-** | 13 | - | NEG -$10k | - | 30 | 30 | -$961k | - | out (clean 29, ADX 9, RVol 0.4) |
| 17 | **UBER** | 70.41 | - | **-** | 13 | - | POS +$5.5M | 69.07 | 70 | 70 | -$116k | - | out (clean 32, ADX 42, RVol 0.8) |
| 18 | **SMH** | 485.50 | - | **-** | 12 | - | NEG -$219.2M | - | 500 | 475 | -$2.7M | - | out (clean 31, ADX 37, RVol 0.3) |
| 19 | **SHOP** | 150.85 | - | **-** | 12 | - | POS +$2.0M | - | 150 | 140 | -$88k | - | out (clean 34, ADX 21, RVol 0.1) |
| 20 | **AMZN** | 268.69 | - | **-** | 11 | - | POS +$397.4M | - | 270 | 265 | +$20.1M | - | out (clean 34, ADX 12, RVol 0.2) |
| 21 | **PLTR** | 169.49 | - | **-** | 11 | - | POS +$12.1M | - | 165 | 180 | -$2.6M | - | out (clean 30, ADX 35, RVol 0.4) |
| 22 | **HOOD** | 84.01 | - | **-** | 10 | - | NEG -$1.5M | - | 85 | 85 | -$2.0M | - | out (clean 30, ADX 26, RVol 0.5) |
| 23 | **DELL** | 350.81 | - | **-** | 9 | - | NEG -$6.3M | - | 350 | 340 | -$344k | - | out (clean 32, ADX 38, RVol 0.2) |
| 24 | **ARM** | 187.06 | - | **-** | 9 | - | NEG -$4.6M | - | 185 | 190 | +$294k | - | out (clean 27, ADX 33, RVol 0.6) |
| 25 | **MSTR** | 125.39 | - | **-** | 8 | - | POS +$1.0M | 123.97 | 135 | 120 | -$2.2M | - | out (clean 30, ADX 22, RVol 0.2) |
| 26 | **BABA** | 105.48 | - | **-** | 7 | - | POS +$2.7M | 103.94 | 110 | 110 | +$102k | - | out (clean 31, ADX 30, RVol 0.2) |
| 27 | **ORCL** | 119.31 | - | **-** | 6 | - | NEG -$26.3M | - | 125 | 125 | -$453k | - | out (clean 30, ADX 21, RVol 0.3) |

## Big prints this scan (36)
- **SPY** CALL 755 2026-11-13 (4DTE): 1,666 @ 4.85 = **+$808k** BUY | vol 12,110 / OI 2,927
- **AAPL** PUT 360 2026-11-13 (4DTE): 411 @ 11.00 = **+$452k** MID | vol 1,128 / OI 1,594
- **QQQ** CALL 680 2026-11-13 (4DTE): 500 @ 7.54 = **+$377k** SELL | vol 4,902 / OI 1,701
- **SPY** CALL 762 2026-11-13 (4DTE): 1,666 @ 1.89 = **+$315k** BUY | vol 10,676 / OI 2,860
- **SPY** PUT 751 2026-11-13 (4DTE): 289 @ 5.11 = **+$148k** BUY | vol 4,227 / OI 1,084
- **SPY** PUT 754 2026-11-09 (0DTE): 771 @ 1.78 = **+$137k** SELL | vol 30,245 / OI 1,253
- **NVDA** CALL 175 2026-11-09 (0DTE): 372 @ 3.29 = **+$122k** BUY | vol 83,960 / OI 296
- **SPY** CALL 755 2026-11-13 (4DTE): 238 @ 4.85 = **+$115k** BUY | vol 12,110 / OI 2,927
- **SPY** CALL 755 2026-11-13 (4DTE): 238 @ 4.84 = **+$115k** BUY | vol 12,110 / OI 2,927
- **AAPL** PUT 360 2026-11-13 (4DTE): 94 @ 11.00 = **+$103k** MID | vol 1,128 / OI 1,594
- **SPY** PUT 751 2026-11-13 (4DTE): 200 @ 5.09 = **+$102k** MID | vol 4,227 / OI 1,084
- **NVDA** CALL 175 2026-11-09 (0DTE): 312 @ 3.22 = **+$100k** BUY | vol 83,960 / OI 296
- **QQQ** CALL 677 2026-11-09 (0DTE): 501 @ 2.00 = **+$100k** BUY | vol 170,048 / OI 253
- **NVDA** PUT 175 2026-11-13 (4DTE): 226 @ 3.95 = **+$89k** SELL | vol 18,584 / OI 5,460
- **AMD** CALL 510 2026-11-11 (2DTE): 75 @ 11.10 = **+$83k** SELL | vol 1,069 / OI 432

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 767 2026-11-13 (4DTE): 1,591 traded vs OI 1,578
- **SPY** PUT 752 2026-11-12 (3DTE): 552 traded vs OI 238
- **SPY** PUT 743 2026-11-16 (7DTE): 505 traded vs OI 269
- **SPY** CALL 767 2026-11-16 (7DTE): 634 traded vs OI 426
- **SPY** CALL 772 2026-11-20 (11DTE): 4,608 traded vs OI 2,669
- **SPY** CALL 762 2026-11-20 (11DTE): 5,208 traded vs OI 1,094
- **QQQ** CALL 695 2026-11-16 (7DTE): 500 traded vs OI 250
- **QQQ** PUT 638 2026-11-20 (11DTE): 1,458 traded vs OI 0
- **IWM** PUT 282 2026-11-11 (2DTE): 749 traded vs OI 727
- **NVDA** PUT 177.5 2026-11-18 (9DTE): 954 traded vs OI 131
- **NVDA** PUT 180 2026-11-18 (9DTE): 784 traded vs OI 459
- **AAPL** PUT 332.5 2026-11-11 (2DTE): 527 traded vs OI 311
- **NFLX** CALL 66 2026-11-13 (4DTE): 3,543 traded vs OI 3,272
- **PLTR** PUT 170 2026-11-13 (4DTE): 1,196 traded vs OI 1,184
- **MU** CALL 742.5 2026-11-11 (2DTE): 504 traded vs OI 151

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
