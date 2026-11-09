# GEX + FLOW SCAN - Mon Nov 09, 02:30 PM ET
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
Last 1m check 14:30:08 ET, last candle SPY 14:29, QQQ 14:29 | no errors
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
| 1 | **AMD** | 505.41 | FLIP CROSS down into negative gamma | **PUTS** | 36 | none: 164 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (62 contracts' greeks worked out here) | POS +$29.4M | 520.29 | 500 | 500 | -$61.5M | +$6.9M bull / +$0 bear | out (clean 31, ADX 40, RVol 0.4) |
| 2 | **GOOGL** | 289.83 | PINNED between the walls (positive gamma) - chop | **-** | 31 | - | POS +$22.9M | 288.26 | 290 | 290 | +$4.4M | +$0 bull / -$34k bear | out (clean 31, ADX 26, RVol 0.3) |
| 3 | **SPY** | 751.79 | - | **-** | 23 | - | NEG -$6.0B | 761.47 | 750 | 750 | -$309.1M | +$3.0M bull / +$0 bear | out (clean 32, ADX 34, RVol 0.2) |
| 4 | **TSLA** | 377.55 | - | **-** | 22 | - | POS +$133.4M | - | 380 | 380 | -$90.1M | +$277k bull / +$0 bear | out (clean 33, ADX 19, RVol 0.2) |
| 5 | **QQQ** | 676.77 | - | **-** | 21 | - | NEG -$1.9B | 698.5 | 680 | 680 | -$228.8M | +$108k bull / +$0 bear | out (clean 31, ADX 27, RVol 0.3) |
| 6 | **AMZN** | 267.95 | - | **-** | 20 | - | POS +$368.6M | - | 270 | 265 | +$20.8M | +$152k bull / +$0 bear | out (clean 33, ADX 9, RVol 0.3) |
| 7 | **AVGO** | 318.22 | - | **-** | 20 | - | NEG -$63.6M | - | 340 | 320 | -$6.9M | +$93k bull / +$0 bear | out (clean 30, ADX 22, RVol 0.5) |
| 8 | **SMH** | 483.12 | - | **-** | 19 | - | NEG -$224.1M | - | 485 | 475 | -$2.6M | +$33k bull / +$0 bear | out (clean 29, ADX 20, RVol 0.3) |
| 9 | **AAPL** | 351.24 | - | **-** | 19 | - | POS +$479.6M | 339.08 | 350 | 350 | -$8.4M | +$614k bull / -$339k bear | out (clean 28, ADX 31, RVol 0.5) |
| 10 | **IWM** | 281.88 | - | **-** | 18 | - | NEG -$727.2M | 284.71 | 285 | 270 | -$23.6M | - | out (clean 35, ADX 52, RVol 0.4) |
| 11 | **META** | 642.24 | - | **-** | 18 | - | POS +$162.4M | 614.41 | 650 | 640 | -$11.3M | +$0 bull / -$432k bear | out (clean 32, ADX 20, RVol 0.4) |
| 12 | **HOOD** | 83.87 | - | **-** | 18 | - | NEG -$1.4M | - | 85 | 85 | -$2.3M | +$0 bull / -$28k bear | out (clean 29, ADX 16, RVol 0.3) |
| 13 | **NVDA** | 175.82 | - | **-** | 17 | - | NEG -$191.7M | - | 190 | 190 | -$41.5M | +$375k bull / -$178k bear | out (clean 32, ADX 19, RVol 0.8) |
| 14 | **MSFT** | 544.90 | - | **-** | 16 | - | POS +$654.3M | - | 550 | 540 | +$1.2M | +$29k bull / -$255k bear | out (clean 33, ADX 26, RVol 0.3) |
| 15 | **PLTR** | 168.22 | - | **-** | 15 | - | POS +$11.8M | - | 165 | 170 | -$1.6M | +$252k bull / +$0 bear | out (clean 30, ADX 15, RVol 0.2) |
| 16 | **MU** | 727.25 | - | **-** | 14 | - | NEG -$11.8M | 738.65 | 720 | 750 | +$6.6M | +$748k bull / -$90k bear | out (clean 30, ADX 13, RVol 0.4) |
| 17 | **ORCL** | 118.78 | - | **-** | 14 | - | NEG -$27.6M | - | 125 | 125 | -$405k | +$0 bull / -$27k bear | out (clean 29, ADX 9, RVol 0.2) |
| 18 | **UBER** | 70.85 | - | **-** | 13 | - | POS +$6.9M | 69.16 | 75 | 70 | -$215k | - | out (clean 32, ADX 44, RVol 0.3) |
| 19 | **COIN** | 136.78 | - | **-** | 12 | - | NEG -$6.7M | - | 140 | 135 | -$2.0M | - | out (clean 32, ADX 12, RVol 0.2) |
| 20 | **SMCI** | 28.74 | - | **-** | 12 | - | NEG -$289k | - | 30 | 30 | -$611k | - | out (clean 29, ADX 31, RVol 0.6) |
| 21 | **SHOP** | 151.23 | - | **-** | 11 | - | POS +$1.9M | - | 150 | 140 | -$77k | - | out (clean 33, ADX 25, RVol 0.1) |
| 22 | **ARM** | 185.76 | - | **-** | 9 | - | NEG -$4.7M | - | 185 | 190 | +$758k | - | out (clean 27, ADX 15, RVol 1.1) |
| 23 | **DELL** | 346.53 | - | **-** | 8 | - | NEG -$6.6M | - | 350 | 340 | +$537k | - | out (clean 33, ADX 31, RVol 0.3) |
| 24 | **CRM** | 214.74 | - | **-** | 7 | - | NEG -$10.9M | - | 195 | 220 | -$49k | - | out (clean 33, ADX 20, RVol 0.5) |
| 25 | **MSTR** | 125.43 | - | **-** | 6 | - | POS +$908k | 124.12 | 135 | 120 | -$1.8M | - | out (clean 30, ADX 17, RVol 0.2) |
| 26 | **NFLX** | 63.65 | - | **-** | 5 | - | NEG -$19.4M | - | 65 | 65 | +$167k | - | out (clean 30, ADX 13, RVol 0.4) |
| 27 | **BABA** | 105.14 | - | **-** | 5 | - | POS +$1.4M | 104.4 | 110 | 100 | +$57k | - | out (clean 31, ADX 20, RVol 0.4) |

## Big prints this scan (80)
- **AMD** CALL 500 2026-11-11 (2DTE): 361 @ 18.35 = **+$662k** BUY | vol 6,568 / OI 698
- **AMD** CALL 500 2026-11-11 (2DTE): 349 @ 18.35 = **+$640k** BUY | vol 6,568 / OI 698
- **AAPL** PUT 360 2026-11-13 (4DTE): 500 @ 9.51 = **+$476k** SELL | vol 1,689 / OI 1,594
- **AMD** CALL 500 2026-11-11 (2DTE): 208 @ 18.35 = **+$382k** BUY | vol 6,568 / OI 698
- **AMD** CALL 500 2026-11-11 (2DTE): 200 @ 18.35 = **+$367k** BUY | vol 6,568 / OI 698
- **AMD** CALL 500 2026-11-11 (2DTE): 182 @ 18.35 = **+$334k** BUY | vol 6,568 / OI 698
- **AMD** PUT 507.5 2026-11-11 (2DTE): 194 @ 14.35 = **+$278k** SELL | vol 443 / OI 136
- **AMD** CALL 495 2026-11-11 (2DTE): 111 @ 21.40 = **+$238k** BUY | vol 1,182 / OI 135
- **AMD** CALL 500 2026-11-13 (4DTE): 98 @ 23.68 = **+$232k** BUY | vol 7,518 / OI 1,939
- **AMD** CALL 500 2026-11-11 (2DTE): 119 @ 18.35 = **+$218k** BUY | vol 6,568 / OI 698
- **AMD** CALL 500 2026-11-11 (2DTE): 112 @ 18.35 = **+$206k** BUY | vol 6,568 / OI 698
- **AMD** CALL 500 2026-11-11 (2DTE): 107 @ 18.35 = **+$196k** BUY | vol 6,568 / OI 698
- **AAPL** CALL 342.5 2026-11-09 (0DTE): 199 @ 9.00 = **+$179k** MID | vol 2,243 / OI 398
- **AAPL** CALL 342.5 2026-11-09 (0DTE): 199 @ 9.00 = **+$179k** MID | vol 2,243 / OI 398
- **AAPL** CALL 342.5 2026-11-09 (0DTE): 199 @ 9.00 = **+$179k** MID | vol 2,243 / OI 398

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 707 2026-11-09 (0DTE): 1,112 traded vs OI 421
- **QQQ** PUT 678 2026-11-13 (4DTE): 735 traded vs OI 710
- **TSLA** CALL 380 2026-12-04 (25DTE): 783 traded vs OI 776
- **AAPL** PUT 360 2026-11-13 (4DTE): 1,689 traded vs OI 1,594
- **AVGO** CALL 337.5 2026-11-13 (4DTE): 506 traded vs OI 241

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
