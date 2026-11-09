# GEX + FLOW SCAN - Mon Nov 09, 02:00 PM ET
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
Last 1m check 14:00:08 ET, last candle SPY 13:59, QQQ 13:59 | no errors
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
| 1 | **META** | 641.00 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 36 | none: 208 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (78 contracts' greeks worked out here) | POS +$172.3M | 612.68 | 650 | 640 | -$10.6M | +$114k bull / -$288k bear | out (clean 32, ADX 24, RVol 0.4) |
| 2 | **GOOGL** | 289.87 | PINNED between the walls (positive gamma) - chop | **-** | 31 | - | POS +$14.9M | 288.42 | 290 | 290 | +$4.6M | +$0 bull / -$47k bear | out (clean 31, ADX 26, RVol 0.4) |
| 3 | **IWM** | 282.28 | - | **-** | 29 | - | NEG -$651.4M | 284.64 | 285 | 270 | -$23.9M | +$0 bull / -$103k bear | out (clean 35, ADX 60, RVol 0.5) |
| 4 | **AAPL** | 350.65 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$448.9M | 338.83 | 350 | 350 | -$6.2M | +$0 bull / -$83k bear | out (clean 27, ADX 21, RVol 0.3) |
| 5 | **MU** | 730.63 | FLIP CROSS down into negative gamma | **PUTS** | 26 | none: 190 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (75 contracts' greeks worked out here) | NEG -$12.3M | 740.54 | 750 | 750 | +$1.9M | +$632k bull / -$1.3M bear | out (clean 31, ADX 16, RVol 0.4) |
| 6 | **SPY** | 752.85 | - | **-** | 25 | - | NEG -$6.4B | 761.84 | 750 | 740 | -$326.2M | +$0 bull / -$1.8M bear | out (clean 32, ADX 42, RVol 0.2) |
| 7 | **AMD** | 507.13 | - | **-** | 25 | - | POS +$29.6M | 522.1 | 500 | 500 | -$66.2M | +$0 bull / -$1.9M bear | out (clean 32, ADX 42, RVol 0.5) |
| 8 | **TSLA** | 377.60 | - | **-** | 23 | - | POS +$125.2M | - | 380 | 380 | -$93.3M | +$0 bull / -$892k bear | out (clean 34, ADX 18, RVol 0.3) |
| 9 | **AVGO** | 319.56 | - | **-** | 23 | - | NEG -$66.7M | - | 340 | 320 | -$7.9M | +$0 bull / -$72k bear | out (clean 31, ADX 30, RVol 0.9) |
| 10 | **QQQ** | 677.68 | - | **-** | 22 | - | NEG -$2.1B | 698.51 | 680 | 680 | -$241.5M | +$0 bull / -$1.3M bear | out (clean 32, ADX 31, RVol 0.3) |
| 11 | **SMH** | 485.18 | - | **-** | 21 | - | NEG -$217.9M | - | 485 | 475 | -$2.9M | +$0 bull / -$47k bear | out (clean 30, ADX 28, RVol 0.2) |
| 12 | **AMZN** | 268.05 | - | **-** | 21 | - | POS +$379.7M | - | 270 | 265 | +$19.8M | +$0 bull / -$27k bear | out (clean 33, ADX 12, RVol 0.3) |
| 13 | **HOOD** | 83.98 | - | **-** | 19 | - | NEG -$1.4M | - | 85 | 85 | -$2.4M | +$0 bull / -$97k bear | out (clean 30, ADX 19, RVol 0.5) |
| 14 | **NVDA** | 176.77 | - | **-** | 18 | - | NEG -$185.3M | - | 190 | 190 | -$48.2M | +$0 bull / -$1.1M bear | out (clean 34, ADX 19, RVol 1.1) |
| 15 | **MSFT** | 543.55 | - | **-** | 15 | - | POS +$619.3M | - | 550 | 540 | +$1.2M | +$59k bull / +$0 bear | out (clean 33, ADX 22, RVol 0.2) |
| 16 | **UBER** | 71.07 | - | **-** | 15 | - | POS +$7.1M | 69.21 | 75 | 70 | -$262k | - | out (clean 33, ADX 55, RVol 0.5) |
| 17 | **COIN** | 137.00 | - | **-** | 13 | - | NEG -$6.6M | - | 140 | 135 | -$2.0M | - | out (clean 33, ADX 13, RVol 0.2) |
| 18 | **SMCI** | 28.89 | - | **-** | 12 | - | NEG -$278k | - | 30 | 30 | -$667k | - | out (clean 29, ADX 26, RVol 0.7) |
| 19 | **SHOP** | 151.52 | - | **-** | 12 | - | POS +$2.0M | - | 150 | 140 | -$86k | - | out (clean 34, ADX 22, RVol 0.1) |
| 20 | **ARM** | 186.78 | - | **-** | 8 | - | NEG -$4.6M | - | 185 | 190 | +$736k | - | out (clean 27, ADX 17, RVol 0.4) |
| 21 | **CRM** | 216.34 | - | **-** | 8 | - | NEG -$11.5M | - | 230 | 220 | -$59k | - | out (clean 34, ADX 19, RVol 0.4) |
| 22 | **PLTR** | 168.56 | - | **-** | 7 | - | POS +$11.8M | - | 165 | 170 | -$1.9M | - | out (clean 30, ADX 19, RVol 0.4) |
| 23 | **DELL** | 346.85 | - | **-** | 7 | - | NEG -$6.6M | - | 350 | 340 | +$456k | - | out (clean 33, ADX 27, RVol 0.4) |
| 24 | **MSTR** | 125.68 | - | **-** | 7 | - | POS +$1.1M | 123.83 | 135 | 120 | -$1.8M | - | out (clean 30, ADX 24, RVol 0.2) |
| 25 | **NFLX** | 63.65 | - | **-** | 6 | - | NEG -$20.2M | - | 65 | 65 | +$178k | - | out (clean 30, ADX 14, RVol 0.5) |
| 26 | **BABA** | 105.52 | - | **-** | 6 | - | POS +$3.1M | 103.88 | 110 | 110 | +$93k | - | out (clean 31, ADX 24, RVol 0.4) |
| 27 | **ORCL** | 118.81 | - | **-** | 5 | - | NEG -$27.1M | - | 125 | 120 | -$452k | - | out (clean 30, ADX 14, RVol 0.3) |

## Big prints this scan (31)
- **AMD** PUT 485 2026-11-13 (4DTE): 200 @ 10.77 = **+$215k** BUY | vol 2,325 / OI 518
- **AMD** PUT 485 2026-11-13 (4DTE): 200 @ 10.72 = **+$214k** BUY | vol 2,325 / OI 518
- **AMD** PUT 485 2026-11-13 (4DTE): 198 @ 10.65 = **+$211k** BUY | vol 2,325 / OI 518
- **MU** CALL 750 2026-11-13 (4DTE): 74 @ 18.80 = **+$139k** SELL | vol 2,196 / OI 1,316
- **SPY** PUT 752 2026-11-13 (4DTE): 246 @ 5.49 = **+$135k** BUY | vol 3,987 / OI 2,043
- **NVDA** CALL 175 2026-11-09 (0DTE): 665 @ 1.84 = **+$122k** SELL | vol 96,506 / OI 296
- **MU** PUT 730 2026-11-09 (0DTE): 239 @ 4.70 = **+$112k** BUY | vol 22,506 / OI 118
- **NVDA** PUT 175 2026-11-13 (4DTE): 250 @ 4.40 = **+$110k** MID | vol 22,614 / OI 5,460
- **MU** CALL 732.5 2026-11-09 (0DTE): 485 @ 2.20 = **+$107k** SELL | vol 15,213 / OI 153
- **QQQ** CALL 680 2026-11-10 (1DTE): 333 @ 3.02 = **+$101k** SELL | vol 20,030 / OI 1,376
- **AMZN** PUT 275 2026-11-09 (0DTE): 123 @ 7.05 = **+$87k** MID | vol 2,693 / OI 37
- **AMD** CALL 512.5 2026-11-11 (2DTE): 72 @ 11.31 = **+$81k** SELL | vol 544 / OI 396
- **TSLA** CALL 365 2026-11-11 (2DTE): 56 @ 14.15 = **+$79k** SELL | vol 1,596 / OI 394
- **PLTR** CALL 165 2026-11-13 (4DTE): 118 @ 6.40 = **+$76k** MID | vol 3,372 / OI 7,991
- **MU** PUT 730 2026-11-09 (0DTE): 157 @ 4.35 = **+$68k** BUY | vol 22,506 / OI 118

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 706 2026-11-10 (1DTE): 531 traded vs OI 131
- **SPY** PUT 704 2026-11-10 (1DTE): 582 traded vs OI 311
- **SPY** CALL 784 2026-11-10 (1DTE): 1,959 traded vs OI 825
- **SPY** CALL 756 2026-11-11 (2DTE): 1,096 traded vs OI 1,082
- **SPY** CALL 766 2026-11-13 (4DTE): 2,137 traded vs OI 1,998
- **SPY** PUT 709 2026-11-09 (0DTE): 583 traded vs OI 238
- **SPY** PUT 703 2026-11-10 (1DTE): 521 traded vs OI 237
- **QQQ** CALL 697 2026-11-10 (1DTE): 511 traded vs OI 163
- **IWM** CALL 290 2026-11-18 (9DTE): 813 traded vs OI 787
- **AAPL** CALL 367.5 2026-11-13 (4DTE): 4,372 traded vs OI 1,799
- **AMD** CALL 512.5 2026-11-11 (2DTE): 544 traded vs OI 396
- **AMZN** PUT 242.5 2026-11-13 (4DTE): 503 traded vs OI 0
- **MU** CALL 727.5 2026-11-13 (4DTE): 501 traded vs OI 163

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
