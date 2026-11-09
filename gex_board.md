# GEX + FLOW SCAN - Mon Nov 09, 12:00 PM ET
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
Last 1m check 12:00:08 ET, last candle SPY 11:59, QQQ 11:59 | no errors
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
| 1 | **IWM** | 281.28 | FLOW SURGE | **PUTS** | 41 | 11/09 281P @ 0.42 (delta 0.42) = est +77% at 280.43 | NEG -$970.8M | 284.94 | 285 | 270 | -$20.5M | +$0 bull / -$165k bear | out (clean 35, ADX 61, RVol 0.6) |
| 2 | **AMD** | 498.93 | PINNED between the walls (positive gamma) - chop | **-** | 37 | - | POS +$11.8M | 491.99 | 500 | 500 | -$48.6M | +$106k bull / -$2.1M bear | out (clean 32, ADX 50, RVol 0.4) |
| 3 | **AAPL** | 350.43 | PINNED between the walls (positive gamma) - chop | **-** | 33 | - | POS +$447.6M | 338.7 | 350 | 350 | -$5.3M | +$0 bull / -$26k bear | out (clean 28, ADX 34, RVol 0.6) |
| 4 | **MU** | 734.01 | FLIP CROSS down into negative gamma | **PUTS** | 32 | none: 190 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (75 contracts' greeks worked out here) | NEG -$4.0M | 737.46 | 750 | 750 | -$9.6M | +$0 bull / -$2.7M bear | out (clean 32, ADX 40, RVol 0.6) |
| 5 | **TSLA** | 377.52 | - | **-** | 27 | - | POS +$112.9M | - | 380 | 380 | -$90.6M | +$45k bull / -$876k bear | out (clean 34, ADX 38, RVol 0.3) |
| 6 | **AVGO** | 318.48 | - | **-** | 27 | - | NEG -$67.8M | - | 340 | 320 | -$7.1M | +$0 bull / -$418k bear | out (clean 31, ADX 56, RVol 0.7) |
| 7 | **PLTR** | 169.62 | - | **-** | 27 | - | POS +$10.8M | - | 165 | 180 | -$4.7M | +$0 bull / -$62k bear | out (clean 30, ADX 46, RVol 0.5) |
| 8 | **SPY** | 751.14 | - | **-** | 26 | - | NEG -$6.8B | 761.84 | 750 | 740 | -$243.0M | +$0 bull / -$860k bear | out (clean 32, ADX 49, RVol 0.5) |
| 9 | **NVDA** | 176.49 | - | **-** | 26 | - | NEG -$194.3M | - | 190 | 190 | -$42.5M | +$0 bull / -$3.4M bear | out (clean 32, ADX 41, RVol 3.0) |
| 10 | **QQQ** | 676.84 | - | **-** | 25 | - | NEG -$2.3B | 697.7 | 680 | 680 | -$210.0M | +$0 bull / -$1.5M bear | out (clean 32, ADX 44, RVol 0.5) |
| 11 | **SHOP** | 150.36 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 25 | none: 21 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$1.7M | - | 150 | 140 | -$50k | - | out (clean 34, ADX 16, RVol 0.2) |
| 12 | **SMH** | 484.31 | - | **-** | 23 | - | NEG -$224.3M | - | 500 | 475 | -$2.5M | +$0 bull / -$317k bear | out (clean 31, ADX 38, RVol 0.5) |
| 13 | **AMZN** | 268.46 | - | **-** | 23 | - | POS +$394.6M | - | 270 | 265 | +$20.5M | +$28k bull / -$80k bear | out (clean 34, ADX 15, RVol 0.4) |
| 14 | **HOOD** | 84.42 | - | **-** | 23 | - | NEG -$1.4M | - | 85 | 85 | -$2.0M | +$0 bull / -$76k bear | out (clean 31, ADX 40, RVol 0.8) |
| 15 | **META** | 641.82 | - | **-** | 21 | - | POS +$163.1M | 615.24 | 650 | 640 | -$7.3M | +$0 bull / -$25k bear | out (clean 32, ADX 36, RVol 0.6) |
| 16 | **DELL** | 352.36 | - | **-** | 21 | - | NEG -$6.3M | - | 350 | 340 | -$479k | +$0 bull / -$80k bear | out (clean 32, ADX 45, RVol 0.3) |
| 17 | **GOOGL** | 291.31 | - | **-** | 20 | - | POS +$13.6M | 288.9 | 300 | 290 | +$4.0M | +$0 bull / -$100k bear | out (clean 31, ADX 18, RVol 1.1) |
| 18 | **MSTR** | 127.06 | - | **-** | 20 | - | POS +$1.6M | 123.78 | 135 | 120 | -$2.6M | +$0 bull / -$124k bear | out (clean 30, ADX 18, RVol 0.7) |
| 19 | **MSFT** | 541.87 | - | **-** | 19 | - | POS +$569.8M | - | 550 | 540 | +$2.5M | +$101k bull / +$0 bear | out (clean 33, ADX 27, RVol 0.3) |
| 20 | **BABA** | 105.74 | - | **-** | 19 | - | POS +$3.5M | 103.81 | 110 | 110 | +$143k | +$0 bull / -$129k bear | out (clean 32, ADX 37, RVol 0.5) |
| 21 | **COIN** | 137.82 | - | **-** | 16 | - | NEG -$6.5M | - | 140 | 135 | -$2.1M | - | out (clean 32, ADX 20, RVol 0.3) |
| 22 | **ORCL** | 119.00 | - | **-** | 15 | - | NEG -$26.8M | - | 125 | 125 | -$260k | +$0 bull / -$50k bear | out (clean 30, ADX 22, RVol 0.2) |
| 23 | **UBER** | 69.70 | - | **-** | 14 | - | POS +$1.8M | 69.23 | 70 | 70 | -$136k | - | out (clean 31, ADX 32, RVol 1.1) |
| 24 | **SMCI** | 29.38 | - | **-** | 13 | - | NEG -$20k | - | 30 | 30 | -$895k | - | out (clean 30, ADX 9, RVol 0.7) |
| 25 | **ARM** | 188.37 | - | **-** | 11 | - | NEG -$4.5M | - | 185 | 190 | +$163k | - | out (clean 27, ADX 49, RVol 0.9) |
| 26 | **NFLX** | 63.61 | - | **-** | 7 | - | NEG -$21.0M | - | 65 | 65 | +$163k | - | out (clean 31, ADX 16, RVol 0.5) |
| 27 | **CRM** | 215.53 | - | **-** | 5 | - | NEG -$11.6M | - | 195 | 220 | +$10k | - | out (clean 34, ADX 18, RVol 0.6) |

## Big prints this scan (49)
- **MU** CALL 750 2026-11-13 (4DTE): 100 @ 21.00 = **+$210k** SELL | vol 1,680 / OI 1,316
- **SPY** CALL 750 2026-11-10 (1DTE): 450 @ 3.44 = **+$155k** SELL | vol 26,666 / OI 8,230
- **QQQ** CALL 680 2026-11-11 (2DTE): 250 @ 4.21 = **+$105k** SELL | vol 5,167 / OI 577
- **IWM** CALL 275 2026-11-13 (4DTE): 130 @ 7.10 = **+$92k** SELL | vol 988 / OI 2,257
- **NVDA** PUT 185 2026-11-11 (2DTE): 77 @ 11.17 = **+$86k** BUY | vol 3,195 / OI 2,107
- **DELL** CALL 357.5 2026-11-13 (4DTE): 70 @ 11.45 = **+$80k** SELL | vol 100 / OI 78
- **NVDA** CALL 180 2026-11-16 (7DTE): 200 @ 4.00 = **+$80k** SELL | vol 4,016 / OI 138
- **AMD** CALL 500 2026-11-13 (4DTE): 40 @ 18.95 = **+$76k** BUY | vol 5,228 / OI 1,939
- **MSFT** CALL 545 2026-11-11 (2DTE): 182 @ 4.00 = **+$73k** BUY | vol 1,394 / OI 110
- **AVGO** PUT 315 2026-11-09 (0DTE): 610 @ 1.15 = **+$70k** BUY | vol 11,560 / OI 48
- **AVGO** PUT 315 2026-11-09 (0DTE): 610 @ 1.07 = **+$65k** BUY | vol 11,560 / OI 48
- **MU** PUT 770 2026-11-13 (4DTE): 12 @ 51.50 = **+$62k** BUY | vol 212 / OI 0
- **NVDA** PUT 175 2026-11-09 (0DTE): 373 @ 1.60 = **+$60k** BUY | vol 171,919 / OI 2,927
- **NVDA** PUT 177.5 2026-11-09 (0DTE): 200 @ 2.96 = **+$59k** BUY | vol 85,703 / OI 0
- **NVDA** CALL 175 2026-11-13 (4DTE): 100 @ 5.90 = **+$59k** SELL | vol 14,847 / OI 627

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 740 2026-11-13 (4DTE): 8,910 traded vs OI 8,834
- **SPY** CALL 748 2026-11-20 (11DTE): 511 traded vs OI 405
- **QQQ** PUT 669 2026-11-11 (2DTE): 715 traded vs OI 100
- **QQQ** PUT 646 2026-11-10 (1DTE): 502 traded vs OI 131
- **QQQ** PUT 640 2026-11-16 (7DTE): 805 traded vs OI 791
- **TSLA** PUT 367.5 2026-11-16 (7DTE): 537 traded vs OI 19
- **TSLA** CALL 410 2026-11-27 (18DTE): 536 traded vs OI 0
- **TSLA** CALL 355 2026-11-09 (0DTE): 502 traded vs OI 401
- **AMD** CALL 490 2026-11-27 (18DTE): 580 traded vs OI 294
- **AMD** CALL 540 2026-11-11 (2DTE): 542 traded vs OI 0
- **AMD** CALL 487.5 2026-11-13 (4DTE): 504 traded vs OI 174
- **META** PUT 645 2026-11-09 (0DTE): 508 traded vs OI 362
- **AMZN** PUT 270 2026-11-23 (14DTE): 500 traded vs OI 0
- **AMZN** PUT 262.5 2026-11-13 (4DTE): 1,005 traded vs OI 969
- **AVGO** CALL 340 2026-11-11 (2DTE): 500 traded vs OI 146

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
