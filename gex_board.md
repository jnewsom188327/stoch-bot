# GEX + FLOW SCAN - Mon Nov 09, 02:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 14:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 11/09 681C | 0.67 | 0.30 | +72% (3m) | **-55%** | +28% | 681.56 |
| 11:04 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/09 754C | 0.41 | 0.23 | -2% (0m) | **-44%** (done) | +28% | 752.23 |
| 10:35 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 272.5C | 0.49 | 0.05 | +2% (2m) | **-90%** (done) | +225% | 273.49 |
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.72 | +51% (23m) | **-6%** (done) | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.02 | +13% (6m) | **-96%** (done) | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:50:08 ET, last candle SPY 14:49, QQQ 14:49 | no errors
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
| 1 | **AMD** | 509.26 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 42 | none: 164 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (57 contracts' greeks worked out here) | POS +$25.6M | 503.41 | 510 | 500 | -$64.4M | +$140k bull / -$1.3M bear | out (clean 30, ADX 41, RVol 0.5) |
| 2 | **TSLA** | 380.30 | PINNED between the walls (positive gamma) - chop | **-** | 37 | - | POS +$143.9M | - | 380 | 380 | -$94.0M | +$0 bull / -$386k bear | out (clean 33, ADX 30, RVol 0.5) |
| 3 | **SPY** | 753.59 | - | **-** | 24 | - | NEG -$5.8B | 761.83 | 750 | 755 | -$319.6M | +$772k bull / -$132k bear | out (clean 31, ADX 34, RVol 0.6) |
| 4 | **QQQ** | 679.06 | - | **-** | 23 | - | NEG -$2.0B | 698.97 | 680 | 680 | -$243.2M | +$293k bull / -$1.6M bear | out (clean 30, ADX 30, RVol 0.8) |
| 5 | **META** | 644.76 | - | **-** | 21 | - | POS +$191.3M | 612.66 | 650 | 640 | -$12.9M | +$0 bull / -$204k bear | out (clean 32, ADX 29, RVol 0.8) |
| 6 | **AMZN** | 268.38 | - | **-** | 21 | - | POS +$406.5M | - | 270 | 265 | +$19.9M | +$126k bull / -$346k bear | out (clean 32, ADX 13, RVol 0.4) |
| 7 | **AVGO** | 320.21 | - | **-** | 21 | - | NEG -$64.1M | - | 340 | 320 | -$7.6M | +$0 bull / -$54k bear | out (clean 30, ADX 23, RVol 0.6) |
| 8 | **SMH** | 485.93 | - | **-** | 20 | - | NEG -$219.4M | - | 485 | 475 | -$2.9M | +$0 bull / -$36k bear | out (clean 29, ADX 22, RVol 0.4) |
| 9 | **AAPL** | 351.22 | - | **-** | 20 | - | POS +$503.3M | 338.53 | 350 | 350 | -$11.3M | +$207k bull / -$1.1M bear | out (clean 28, ADX 32, RVol 0.5) |
| 10 | **IWM** | 282.99 | - | **-** | 19 | - | NEG -$481.9M | 284.77 | 285 | 270 | -$24.8M | - | out (clean 34, ADX 51, RVol 1.1) |
| 11 | **HOOD** | 84.70 | - | **-** | 19 | - | NEG -$1.3M | - | 85 | 85 | -$2.6M | +$0 bull / -$89k bear | out (clean 28, ADX 21, RVol 0.4) |
| 12 | **NVDA** | 176.67 | - | **-** | 18 | - | NEG -$188.8M | - | 190 | 190 | -$42.9M | +$96k bull / -$413k bear | out (clean 32, ADX 17, RVol 1.0) |
| 13 | **MSTR** | 127.83 | - | **-** | 18 | - | POS +$4.4M | - | 135 | 120 | -$2.6M | +$0 bull / -$98k bear | out (clean 30, ADX 21, RVol 0.5) |
| 14 | **MSFT** | 547.30 | - | **-** | 17 | - | POS +$705.0M | - | 550 | 540 | +$76k | +$0 bull / -$30k bear | out (clean 33, ADX 34, RVol 0.6) |
| 15 | **NFLX** | 63.58 | - | **-** | 15 | - | NEG -$20.8M | - | 65 | 65 | +$114k | +$0 bull / -$29k bear | out (clean 30, ADX 14, RVol 0.7) |
| 16 | **MU** | 729.49 | - | **-** | 14 | - | NEG -$4.7M | 740.72 | 750 | 750 | +$623k | +$0 bull / -$2.5M bear | out (clean 30, ADX 15, RVol 0.5) |
| 17 | **SHOP** | 151.94 | - | **-** | 14 | - | POS +$2.1M | - | 150 | 140 | -$91k | - | out (clean 33, ADX 29, RVol 0.3) |
| 18 | **COIN** | 137.54 | - | **-** | 13 | - | NEG -$6.6M | - | 140 | 135 | -$2.0M | - | out (clean 32, ADX 15, RVol 0.5) |
| 19 | **UBER** | 70.90 | - | **-** | 13 | - | POS +$7.6M | 69.15 | 75 | 70 | -$253k | - | out (clean 32, ADX 41, RVol 0.5) |
| 20 | **SMCI** | 28.83 | - | **-** | 12 | - | NEG -$326k | - | 30 | 30 | -$623k | - | out (clean 28, ADX 27, RVol 1.0) |
| 21 | **GOOGL** | 289.14 | - | **-** | 10 | - | POS +$6.8M | 288.43 | 290 | 290 | +$4.6M | - | out (clean 31, ADX 24, RVol 0.7) |
| 22 | **ARM** | 187.24 | - | **-** | 10 | - | NEG -$4.6M | - | 185 | 190 | +$722k | - | out (clean 26, ADX 18, RVol 1.1) |
| 23 | **DELL** | 348.35 | - | **-** | 7 | - | NEG -$6.5M | - | 350 | 340 | +$387k | - | out (clean 32, ADX 28, RVol 0.3) |
| 24 | **CRM** | 214.77 | - | **-** | 7 | - | NEG -$10.9M | - | 195 | 220 | -$44k | - | out (clean 33, ADX 20, RVol 0.5) |
| 25 | **PLTR** | 169.24 | - | **-** | 6 | - | POS +$11.3M | - | 165 | 180 | -$1.7M | - | out (clean 29, ADX 20, RVol 0.5) |
| 26 | **ORCL** | 119.27 | - | **-** | 5 | - | NEG -$27.4M | - | 125 | 125 | -$491k | - | out (clean 28, ADX 15, RVol 0.3) |
| 27 | **BABA** | 105.28 | - | **-** | 5 | - | POS +$1.7M | 104.35 | 110 | 110 | +$33k | - | out (clean 30, ADX 21, RVol 0.5) |

## Big prints this scan (38)
- **AAPL** CALL 355 2026-11-11 (2DTE): 3,754 @ 1.25 = **+$469k** SELL | vol 28,808 / OI 505
- **AMD** CALL 490 2026-11-09 (0DTE): 148 @ 16.00 = **+$237k** SELL | vol 16,482 / OI 399
- **QQQ** CALL 665 2026-11-12 (3DTE): 100 @ 15.65 = **+$156k** SELL | vol 307 / OI 357
- **AAPL** CALL 355 2026-11-11 (2DTE): 1,165 @ 1.32 = **+$154k** MID | vol 28,808 / OI 505
- **AMD** CALL 490 2026-11-13 (4DTE): 50 @ 28.20 = **+$141k** SELL | vol 3,734 / OI 1,648
- **AAPL** CALL 355 2026-11-11 (2DTE): 1,000 @ 1.30 = **+$130k** SELL | vol 28,808 / OI 505
- **AMD** CALL 500 2026-11-09 (0DTE): 200 @ 6.40 = **+$128k** SELL | vol 47,133 / OI 1,188
- **AAPL** CALL 355 2026-11-11 (2DTE): 991 @ 1.29 = **+$128k** SELL | vol 28,808 / OI 505
- **AAPL** CALL 355 2026-11-11 (2DTE): 911 @ 1.30 = **+$118k** SELL | vol 28,808 / OI 505
- **QQQ** CALL 669 2026-11-10 (1DTE): 100 @ 10.29 = **+$103k** SELL | vol 1,416 / OI 159
- **AMD** CALL 490 2026-11-13 (4DTE): 34 @ 28.10 = **+$96k** SELL | vol 3,734 / OI 1,648
- **TSLA** PUT 377.5 2026-11-09 (0DTE): 1,038 @ 0.82 = **+$85k** BUY | vol 78,385 / OI 267
- **AAPL** CALL 355 2026-11-11 (2DTE): 581 @ 1.30 = **+$76k** SELL | vol 28,808 / OI 505
- **MU** CALL 750 2026-11-11 (2DTE): 52 @ 11.29 = **+$59k** SELL | vol 4,668 / OI 955
- **MU** CALL 700 2026-11-09 (0DTE): 20 @ 27.25 = **+$54k** SELL | vol 6,083 / OI 761

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 778 2026-11-11 (2DTE): 913 traded vs OI 822
- **SPY** PUT 753 2026-11-12 (3DTE): 528 traded vs OI 163
- **SPY** CALL 773 2026-11-16 (7DTE): 503 traded vs OI 189
- **SPY** PUT 728 2026-11-16 (7DTE): 510 traded vs OI 307
- **SPY** PUT 750 2026-11-23 (14DTE): 507 traded vs OI 0
- **QQQ** PUT 677 2026-11-17 (8DTE): 525 traded vs OI 37
- **AMD** PUT 465 2026-11-11 (2DTE): 588 traded vs OI 26
- **META** CALL 655 2026-11-11 (2DTE): 1,044 traded vs OI 1,043
- **MU** PUT 750 2026-11-13 (4DTE): 948 traded vs OI 888

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
