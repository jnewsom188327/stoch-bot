# GEX + FLOW SCAN - Mon Nov 09, 03:05 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 14:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 11/09 681C | 0.67 | 0.25 | +72% (3m) | **-63%** | +28% | 681.56 |
| 11:04 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/09 754C | 0.41 | 0.23 | -2% (0m) | **-44%** (done) | +28% | 752.23 |
| 10:35 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 272.5C | 0.49 | 0.05 | +2% (2m) | **-90%** (done) | +225% | 273.49 |
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.72 | +51% (23m) | **-6%** (done) | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.02 | +13% (6m) | **-96%** (done) | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:05:08 ET, last candle SPY 15:04, QQQ 15:04 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
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
| 1 | **AMD** | 509.81 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 41 | none: 164 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (64 contracts' greeks worked out here) | POS +$28.0M | 501.53 | 510 | 500 | -$64.1M | +$679k bull / -$638k bear | out (clean 30, ADX 38, RVol 0.5) |
| 2 | **TSLA** | 380.57 | PINNED between the walls (positive gamma) - chop | **-** | 39 | - | POS +$145.4M | - | 380 | 380 | -$92.0M | +$221k bull / -$932k bear | out (clean 33, ADX 36, RVol 0.6) |
| 3 | **IWM** | 283.23 | - | **-** | 29 | - | NEG -$424.1M | 284.49 | 283 | 270 | -$25.1M | +$0 bull / -$167k bear | out (clean 34, ADX 51, RVol 1.3) |
| 4 | **MU** | 729.90 | FLIP CROSS up into positive gamma | **CALLS** | 26 | none: 194 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (74 contracts' greeks worked out here) | POS +$4.9M | 726.28 | 750 | 750 | -$9.5M | +$684k bull / -$1.8M bear | out (clean 30, ADX 14, RVol 0.5) |
| 5 | **SPY** | 753.93 | - | **-** | 24 | - | NEG -$6.0B | 761.76 | 750 | 755 | -$330.2M | +$1.5M bull / -$1.4M bear | out (clean 31, ADX 33, RVol 0.8) |
| 6 | **QQQ** | 679.06 | - | **-** | 23 | - | NEG -$1.9B | 698.3 | 680 | 680 | -$248.4M | +$699k bull / +$0 bear | out (clean 30, ADX 30, RVol 0.9) |
| 7 | **META** | 644.42 | - | **-** | 21 | - | POS +$193.0M | 614.69 | 650 | 640 | -$12.3M | +$166k bull / -$32k bear | out (clean 32, ADX 31, RVol 0.8) |
| 8 | **AVGO** | 320.80 | - | **-** | 21 | - | NEG -$67.6M | - | 340 | 320 | -$7.6M | +$127k bull / -$129k bear | out (clean 30, ADX 24, RVol 0.6) |
| 9 | **AAPL** | 351.50 | - | **-** | 20 | - | POS +$498.1M | 338.76 | 350 | 350 | -$10.1M | +$0 bull / -$46k bear | out (clean 28, ADX 32, RVol 0.5) |
| 10 | **HOOD** | 84.61 | - | **-** | 20 | - | NEG -$1.3M | - | 85 | 85 | -$2.7M | +$84k bull / -$85k bear | out (clean 28, ADX 22, RVol 0.5) |
| 11 | **MSFT** | 546.89 | - | **-** | 19 | - | POS +$702.1M | - | 550 | 535 | +$1.2M | +$136k bull / +$0 bear | out (clean 33, ADX 38, RVol 0.7) |
| 12 | **NVDA** | 176.94 | - | **-** | 18 | - | NEG -$185.7M | - | 190 | 190 | -$44.4M | +$263k bull / -$788k bear | out (clean 32, ADX 16, RVol 1.2) |
| 13 | **ORCL** | 119.29 | - | **-** | 16 | - | NEG -$27.3M | - | 125 | 125 | -$598k | +$0 bull / -$28k bear | out (clean 28, ADX 19, RVol 0.2) |
| 14 | **COIN** | 137.52 | - | **-** | 13 | - | NEG -$6.7M | - | 140 | 135 | -$1.9M | - | out (clean 32, ADX 15, RVol 0.5) |
| 15 | **SHOP** | 151.65 | - | **-** | 13 | - | POS +$1.7M | - | 150 | 140 | -$92k | - | out (clean 33, ADX 28, RVol 0.4) |
| 16 | **SMCI** | 28.95 | - | **-** | 12 | - | NEG -$67k | - | 30 | 30 | -$622k | - | out (clean 28, ADX 24, RVol 1.0) |
| 17 | **UBER** | 70.94 | - | **-** | 12 | - | POS +$7.5M | 69.19 | 75 | 70 | -$240k | - | out (clean 31, ADX 38, RVol 0.5) |
| 18 | **AMZN** | 268.45 | - | **-** | 11 | - | POS +$398.3M | - | 270 | 265 | +$19.9M | - | out (clean 32, ADX 16, RVol 0.4) |
| 19 | **SMH** | 486.00 | - | **-** | 10 | - | NEG -$214.9M | - | 500 | 475 | -$2.7M | - | out (clean 29, ADX 22, RVol 0.6) |
| 20 | **GOOGL** | 289.16 | - | **-** | 10 | - | POS +$6.4M | 288.62 | 290 | 290 | +$4.9M | - | out (clean 31, ADX 25, RVol 0.7) |
| 21 | **MSTR** | 127.39 | - | **-** | 10 | - | POS +$2.0M | 124.15 | 135 | 120 | -$2.9M | - | out (clean 30, ADX 27, RVol 0.8) |
| 22 | **ARM** | 187.33 | - | **-** | 8 | - | NEG -$4.5M | - | 185 | 190 | +$673k | - | out (clean 26, ADX 19, RVol 0.6) |
| 23 | **PLTR** | 169.41 | - | **-** | 7 | - | POS +$11.2M | - | 165 | 180 | -$1.7M | - | out (clean 29, ADX 22, RVol 0.6) |
| 24 | **DELL** | 347.88 | - | **-** | 6 | - | NEG -$6.5M | - | 350 | 340 | +$431k | - | out (clean 32, ADX 24, RVol 0.3) |
| 25 | **CRM** | 215.20 | - | **-** | 6 | - | NEG -$11.2M | - | 195 | 220 | -$35k | - | out (clean 32, ADX 20, RVol 0.5) |
| 26 | **NFLX** | 63.64 | - | **-** | 5 | - | NEG -$20.2M | - | 65 | 65 | +$106k | - | out (clean 30, ADX 14, RVol 0.7) |
| 27 | **BABA** | 105.44 | - | **-** | 5 | - | POS +$2.6M | 104.08 | 110 | 110 | +$45k | - | out (clean 30, ADX 21, RVol 0.4) |

## Big prints this scan (37)
- **QQQ** CALL 670 2026-11-10 (1DTE): 198 @ 10.91 = **+$216k** BUY | vol 4,477 / OI 1,522
- **SPY** PUT 744 2026-11-12 (3DTE): 957 @ 2.06 = **+$197k** BUY | vol 18,099 / OI 211
- **SPY** CALL 753 2026-11-09 (0DTE): 1,475 @ 1.00 = **+$148k** SELL | vol 510,901 / OI 1,206
- **SPY** CALL 744 2026-11-09 (0DTE): 100 @ 10.11 = **+$101k** SELL | vol 42,249 / OI 1,677
- **NVDA** CALL 170 2026-11-16 (7DTE): 100 @ 9.83 = **+$98k** SELL | vol 1,178 / OI 34
- **MU** CALL 700 2026-11-13 (4DTE): 19 @ 45.65 = **+$87k** SELL | vol 1,163 / OI 556
- **MU** CALL 700 2026-11-13 (4DTE): 17 @ 45.40 = **+$77k** SELL | vol 1,163 / OI 556
- **AMD** CALL 510 2026-11-13 (4DTE): 40 @ 18.94 = **+$76k** BUY | vol 3,608 / OI 452
- **MU** CALL 710 2026-11-13 (4DTE): 19 @ 39.15 = **+$74k** SELL | vol 812 / OI 642
- **AMD** CALL 490 2026-11-13 (4DTE): 24 @ 30.75 = **+$74k** MID | vol 3,789 / OI 1,648
- **AMD** PUT 500 2026-11-11 (2DTE): 73 @ 10.00 = **+$73k** BUY | vol 2,068 / OI 49
- **MU** CALL 710 2026-11-13 (4DTE): 17 @ 38.90 = **+$66k** SELL | vol 812 / OI 642
- **IWM** CALL 271 2026-11-13 (4DTE): 50 @ 12.45 = **+$62k** SELL | vol 103 / OI 304
- **IWM** CALL 273 2026-11-13 (4DTE): 50 @ 10.58 = **+$53k** SELL | vol 107 / OI 255
- **IWM** CALL 283 2026-11-13 (4DTE): 189 @ 2.72 = **+$51k** SELL | vol 2,600 / OI 3,055

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 747 2026-11-11 (2DTE): 1,116 traded vs OI 1,115
- **SPY** PUT 719 2026-11-19 (10DTE): 538 traded vs OI 0
- **SPY** CALL 751 2026-11-20 (11DTE): 925 traded vs OI 887
- **QQQ** PUT 633 2026-11-10 (1DTE): 786 traded vs OI 0
- **IWM** CALL 290 2026-11-11 (2DTE): 726 traded vs OI 687
- **IWM** PUT 280 2026-11-13 (4DTE): 2,461 traded vs OI 2,400
- **IWM** CALL 289 2026-11-11 (2DTE): 505 traded vs OI 417
- **AAPL** CALL 372.5 2026-11-11 (2DTE): 644 traded vs OI 642
- **AMD** PUT 505 2026-11-11 (2DTE): 500 traded vs OI 53
- **GOOGL** CALL 305 2026-11-27 (18DTE): 784 traded vs OI 781
- **MU** PUT 800 2026-11-13 (4DTE): 529 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
