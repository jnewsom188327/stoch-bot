# GEX + FLOW SCAN - Mon Nov 09, 03:00 PM ET
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
Last 1m check 15:00:08 ET, last candle SPY 14:59, QQQ 14:59 | no errors
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
| 1 | **AMD** | 509.49 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 41 | none: 164 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (68 contracts' greeks worked out here) | POS +$31.6M | 519.78 | 510 | 500 | -$61.8M | +$469k bull / -$1.2M bear | out (clean 30, ADX 39, RVol 0.5) |
| 2 | **MU** | 730.06 | FLIP CROSS down into negative gamma | **PUTS** | 26 | none: 194 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (78 contracts' greeks worked out here) | NEG -$146k | 730.29 | 750 | 750 | -$7.8M | +$684k bull / -$2.3M bear | out (clean 30, ADX 14, RVol 0.4) |
| 3 | **TSLA** | 380.99 | - | **-** | 25 | - | POS +$140.0M | - | 380 | 380 | -$90.9M | +$221k bull / -$1.3M bear | out (clean 33, ADX 34, RVol 0.6) |
| 4 | **SPY** | 753.95 | - | **-** | 24 | - | NEG -$5.8B | 761.77 | 750 | 755 | -$322.7M | +$1.5M bull / -$986k bear | out (clean 31, ADX 33, RVol 0.7) |
| 5 | **QQQ** | 679.08 | - | **-** | 23 | - | NEG -$1.9B | 698.21 | 680 | 680 | -$248.0M | +$483k bull / -$976k bear | out (clean 30, ADX 30, RVol 0.9) |
| 6 | **META** | 643.76 | - | **-** | 21 | - | POS +$193.3M | 613.57 | 650 | 640 | -$12.4M | +$166k bull / -$119k bear | out (clean 32, ADX 31, RVol 0.8) |
| 7 | **AMZN** | 268.50 | - | **-** | 21 | - | POS +$395.3M | - | 270 | 265 | +$20.1M | +$0 bull / -$302k bear | out (clean 32, ADX 15, RVol 0.5) |
| 8 | **AVGO** | 320.34 | - | **-** | 21 | - | NEG -$61.1M | - | 340 | 320 | -$7.5M | +$127k bull / -$155k bear | out (clean 30, ADX 24, RVol 0.6) |
| 9 | **AAPL** | 351.38 | - | **-** | 20 | - | POS +$480.8M | 339.28 | 350 | 350 | -$9.9M | +$39k bull / -$1.1M bear | out (clean 28, ADX 32, RVol 0.6) |
| 10 | **MSTR** | 127.51 | - | **-** | 20 | - | POS +$2.5M | 123.75 | 135 | 120 | -$3.0M | +$0 bull / -$98k bear | out (clean 30, ADX 26, RVol 0.7) |
| 11 | **HOOD** | 84.58 | - | **-** | 20 | - | NEG -$1.2M | - | 85 | 85 | -$2.8M | +$84k bull / -$143k bear | out (clean 28, ADX 22, RVol 0.5) |
| 12 | **IWM** | 283.19 | - | **-** | 19 | - | NEG -$441.2M | 284.58 | 285 | 270 | -$24.5M | - | out (clean 34, ADX 51, RVol 1.3) |
| 13 | **MSFT** | 546.80 | - | **-** | 19 | - | POS +$701.8M | - | 550 | 540 | +$1.0M | +$55k bull / -$30k bear | out (clean 33, ADX 37, RVol 0.7) |
| 14 | **NVDA** | 177.12 | - | **-** | 18 | - | NEG -$183.3M | - | 190 | 190 | -$44.0M | +$263k bull / -$880k bear | out (clean 32, ADX 16, RVol 1.1) |
| 15 | **COIN** | 137.69 | - | **-** | 13 | - | NEG -$6.6M | - | 140 | 135 | -$1.9M | - | out (clean 32, ADX 15, RVol 0.6) |
| 16 | **SHOP** | 151.66 | - | **-** | 13 | - | POS +$1.8M | - | 150 | 140 | -$92k | - | out (clean 33, ADX 28, RVol 0.4) |
| 17 | **SMCI** | 29.02 | - | **-** | 12 | - | POS +$10k | 28.02 | 30 | 30 | -$618k | - | out (clean 28, ADX 25, RVol 1.1) |
| 18 | **UBER** | 70.96 | - | **-** | 12 | - | POS +$7.8M | 69.09 | 75 | 70 | -$242k | - | out (clean 32, ADX 38, RVol 0.5) |
| 19 | **SMH** | 486.23 | - | **-** | 10 | - | NEG -$218.5M | - | 500 | 475 | -$2.8M | - | out (clean 29, ADX 22, RVol 0.5) |
| 20 | **GOOGL** | 288.97 | - | **-** | 10 | - | POS +$9.3M | 287.96 | 290 | 290 | +$4.8M | - | out (clean 31, ADX 25, RVol 0.8) |
| 21 | **ARM** | 187.43 | - | **-** | 8 | - | NEG -$4.6M | - | 185 | 190 | +$673k | - | out (clean 26, ADX 18, RVol 0.6) |
| 22 | **PLTR** | 169.51 | - | **-** | 7 | - | POS +$12.6M | - | 165 | 180 | -$1.7M | - | out (clean 29, ADX 21, RVol 0.5) |
| 23 | **DELL** | 348.52 | - | **-** | 7 | - | NEG -$6.5M | - | 350 | 340 | +$429k | - | out (clean 32, ADX 25, RVol 0.3) |
| 24 | **ORCL** | 119.29 | - | **-** | 6 | - | NEG -$27.1M | - | 125 | 125 | -$541k | - | out (clean 28, ADX 18, RVol 0.2) |
| 25 | **CRM** | 214.54 | - | **-** | 6 | - | NEG -$10.7M | - | 195 | 220 | -$34k | - | out (clean 33, ADX 20, RVol 0.5) |
| 26 | **NFLX** | 63.62 | - | **-** | 5 | - | NEG -$21.2M | - | 65 | 65 | +$107k | - | out (clean 30, ADX 14, RVol 0.7) |
| 27 | **BABA** | 105.39 | - | **-** | 5 | - | POS +$2.5M | 104.08 | 110 | 110 | +$49k | - | out (clean 30, ADX 21, RVol 0.4) |

## Big prints this scan (44)
- **TSLA** CALL 375 2026-11-13 (4DTE): 200 @ 11.75 = **+$235k** SELL | vol 2,050 / OI 2,530
- **TSLA** CALL 375 2026-11-13 (4DTE): 200 @ 11.75 = **+$235k** SELL | vol 2,050 / OI 2,530
- **NVDA** CALL 170 2026-11-16 (7DTE): 195 @ 10.44 = **+$204k** MID | vol 1,173 / OI 34
- **QQQ** CALL 683 2026-11-10 (1DTE): 642 @ 2.88 = **+$185k** BUY | vol 7,694 / OI 111
- **QQQ** PUT 680 2026-11-11 (2DTE): 250 @ 6.18 = **+$154k** SELL | vol 1,393 / OI 451
- **SPY** PUT 752 2026-11-16 (7DTE): 298 @ 5.14 = **+$153k** SELL | vol 1,771 / OI 180
- **QQQ** CALL 678 2026-11-09 (0DTE): 500 @ 2.88 = **+$144k** BUY | vol 341,366 / OI 205
- **MU** CALL 720 2026-11-13 (4DTE): 40 @ 35.75 = **+$143k** BUY | vol 1,993 / OI 408
- **MU** CALL 750 2026-11-11 (2DTE): 100 @ 12.38 = **+$124k** SELL | vol 5,007 / OI 955
- **TSLA** PUT 385 2026-11-09 (0DTE): 240 @ 4.75 = **+$114k** BUY | vol 2,156 / OI 708
- **MU** CALL 755 2026-11-11 (2DTE): 100 @ 10.63 = **+$106k** SELL | vol 1,118 / OI 169
- **SPY** CALL 744 2026-11-09 (0DTE): 100 @ 10.34 = **+$103k** BUY | vol 42,047 / OI 1,677
- **META** CALL 640 2026-11-11 (2DTE): 80 @ 12.45 = **+$100k** BUY | vol 2,909 / OI 97
- **AMD** CALL 510 2026-11-13 (4DTE): 50 @ 19.70 = **+$98k** BUY | vol 3,536 / OI 452
- **AVGO** CALL 325 2026-11-11 (2DTE): 200 @ 4.52 = **+$90k** BUY | vol 1,886 / OI 102

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 754 2026-11-12 (3DTE): 629 traded vs OI 143
- **SPY** PUT 728 2026-11-11 (2DTE): 518 traded vs OI 391
- **SPY** CALL 761 2026-11-12 (3DTE): 577 traded vs OI 576
- **SPY** PUT 736 2026-11-16 (7DTE): 509 traded vs OI 176
- **QQQ** PUT 670 2026-11-12 (3DTE): 1,121 traded vs OI 1,116
- **QQQ** CALL 698 2026-11-10 (1DTE): 512 traded vs OI 312
- **QQQ** PUT 680 2026-11-12 (3DTE): 516 traded vs OI 245
- **QQQ** CALL 703 2026-11-10 (1DTE): 504 traded vs OI 149
- **QQQ** CALL 675 2026-11-12 (3DTE): 501 traded vs OI 309
- **IWM** CALL 286 2026-11-09 (0DTE): 719 traded vs OI 515
- **IWM** CALL 290 2026-11-13 (4DTE): 2,970 traded vs OI 2,891
- **IWM** CALL 289 2026-11-16 (7DTE): 514 traded vs OI 150
- **NVDA** CALL 167.5 2026-11-16 (7DTE): 686 traded vs OI 0
- **HOOD** PUT 87 2026-11-13 (4DTE): 939 traded vs OI 931

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
