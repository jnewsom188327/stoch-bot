# GEX + FLOW SCAN - Mon Nov 09, 10:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:35 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 272.5C | 0.49 | 0.29 | +2% (2m) | **-41%** | +225% | 273.49 |
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.57 | +51% (23m) | **-26%** | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.09 | +13% (6m) | **-81%** | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:50:08 ET, last candle SPY 10:49, QQQ 10:49 | no errors

## Flow surges NOT fired - price disagreed (16 today, last 5)
- 10:40 AVGO PUTS: price +1.16 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 QQQ PUTS: price +0.45 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:35 AVGO PUTS: price +1.05 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:30 QQQ PUTS: price +0.53 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:25 SMCI PUTS: price +0.08 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AMZN** | 269.50 | TREND + FLOW | **CALLS** | 48 | none: 84 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (35 contracts' greeks worked out here) | POS +$398.9M | - | 270 | 265 | +$16.4M | +$337k bull / -$104k bear | LONG (clean 35, ADX 34, RVol 0.9) |
| 2 | **SMH** | 483.60 | FLOW SURGE | **PUTS** | 46 | none: 152 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (61 contracts' greeks worked out here) | NEG -$215.8M | - | 500 | 475 | -$4.0M | +$0 bull / -$139k bear | out (clean 32, ADX 45, RVol 0.9) |
| 3 | **AMD** | 495.17 | FLIP CROSS up into positive gamma | **CALLS** | 46 | none: 156 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (70 contracts' greeks worked out here) | POS +$3.4M | 492.46 | 500 | 500 | -$37.4M | +$886k bull / -$220k bear | out (clean 33, ADX 53, RVol 1.3) |
| 4 | **SPY** | 750.25 | FLOW SURGE | **PUTS** | 42 | 11/09 748P @ 0.72 (delta 0.28) = est +109% at 747.63 | NEG -$6.6B | 761.39 | 750 | 740 | -$236.0M | +$138k bull / -$4.1M bear | out (clean 32, ADX 48, RVol 0.6) |
| 5 | **QQQ** | 675.88 | FLOW SURGE | **PUTS** | 42 | 11/09 672P @ 0.67 (delta 0.22) = est +149% at 672.05 | NEG -$2.1B | 698.71 | 680 | 680 | -$244.3M | +$303k bull / -$3.0M bear | out (clean 32, ADX 46, RVol 0.6) |
| 6 | **META** | 639.76 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 42 | none: 204 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (92 contracts' greeks worked out here) | POS +$160.3M | 611.42 | 650 | 640 | -$6.2M | +$136k bull / -$304k bear | out (clean 33, ADX 43, RVol 0.9) |
| 7 | **TSLA** | 378.52 | FLOW SURGE | **PUTS** | 39 | none: 120 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (56 contracts' greeks worked out here) | POS +$117.5M | - | 380 | 380 | -$95.4M | +$432k bull / -$1.2M bear | LONG (clean 35, ADX 46, RVol 0.5) |
| 8 | **MSTR** | 128.49 | FLOW SURGE | **PUTS** | 39 | none: 26 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$4.6M | - | 135 | 135 | -$3.1M | +$0 bull / -$185k bear | out (clean 29, ADX 25, RVol 1.5) |
| 9 | **AAPL** | 350.76 | PINNED between the walls (positive gamma) - chop | **-** | 38 | - | POS +$467.0M | 338.21 | 350 | 350 | -$10.1M | +$41k bull / -$518k bear | out (clean 28, ADX 40, RVol 0.7) |
| 10 | **NVDA** | 178.69 | - | **-** | 30 | - | NEG -$174.5M | - | 190 | 190 | -$63.2M | +$3.2M bull / -$2.1M bear | out (clean 32, ADX 39, RVol 2.9) |
| 11 | **HOOD** | 84.92 | - | **-** | 27 | - | NEG -$1.3M | - | 85 | 85 | -$2.5M | +$306k bull / +$0 bear | out (clean 30, ADX 65, RVol 0.6) |
| 12 | **PLTR** | 168.56 | - | **-** | 26 | - | POS +$11.6M | - | 165 | 170 | -$2.9M | +$109k bull / -$85k bear | out (clean 29, ADX 46, RVol 0.6) |
| 13 | **SHOP** | 149.90 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 25 | none: 21 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$1.0M | 143.25 | 150 | 140 | -$29k | - | out (clean 34, ADX 14, RVol 0.4) |
| 14 | **MSFT** | 541.55 | - | **-** | 23 | - | POS +$580.5M | - | 550 | 540 | +$2.8M | +$0 bull / -$49k bear | out (clean 34, ADX 33, RVol 0.7) |
| 15 | **COIN** | 138.09 | - | **-** | 23 | - | NEG -$6.4M | - | 140 | 135 | -$2.2M | - | out (clean 31, ADX 23, RVol 0.6) |
| 16 | **AVGO** | 318.04 | - | **-** | 22 | - | NEG -$66.6M | - | 340 | 320 | -$7.3M | - | out (clean 30, ADX 62, RVol 1.1) |
| 17 | **IWM** | 280.35 | - | **-** | 21 | - | NEG -$1.1B | 284.98 | 285 | 270 | -$14.5M | - | out (clean 33, ADX 50, RVol 0.5) |
| 18 | **GOOGL** | 293.38 | - | **-** | 21 | - | POS +$20.9M | 289.66 | 300 | 290 | +$2.1M | +$62k bull / +$0 bear | out (clean 32, ADX 34, RVol 1.0) |
| 19 | **MU** | 734.30 | - | **-** | 20 | - | POS +$907k | 732.24 | 750 | 750 | -$12.5M | +$970k bull / -$3.1M bear | out (clean 32, ADX 44, RVol 0.6) |
| 20 | **SMCI** | 29.45 | - | **-** | 19 | - | POS +$23k | 31.1 | 30 | 30 | -$978k | - | out (clean 31, ADX 19, RVol 0.7) |
| 21 | **ORCL** | 118.59 | - | **-** | 19 | - | NEG -$26.6M | - | 125 | 120 | -$267k | +$76k bull / +$0 bear | out (clean 30, ADX 34, RVol 0.5) |
| 22 | **BABA** | 105.90 | - | **-** | 18 | - | POS +$2.6M | 104.37 | 110 | 110 | +$16k | +$0 bull / -$82k bear | out (clean 31, ADX 33, RVol 1.0) |
| 23 | **DELL** | 349.81 | - | **-** | 16 | - | NEG -$6.2M | - | 350 | 340 | -$772k | - | out (clean 32, ADX 47, RVol 0.7) |
| 24 | **ARM** | 187.71 | - | **-** | 11 | - | NEG -$4.5M | - | 185 | 190 | -$63k | - | out (clean 26, ADX 50, RVol 1.2) |
| 25 | **NFLX** | 63.66 | - | **-** | 9 | - | NEG -$19.9M | - | 65 | 65 | +$149k | - | out (clean 31, ADX 21, RVol 0.9) |
| 26 | **UBER** | 69.32 | - | **-** | 7 | - | NEG -$619k | 69.46 | 70 | 65 | -$23k | - | out (clean 30, ADX 23, RVol 0.6) |
| 27 | **CRM** | 214.81 | - | **-** | 6 | - | NEG -$10.9M | - | 195 | 220 | +$5k | - | out (clean 34, ADX 23, RVol 0.6) |

## Big prints this scan (97)
- **SPY** CALL 730 2026-11-10 (1DTE): 986 @ 20.00 = **+$2.0M** SELL | vol 2,045 / OI 5,480
- **QQQ** CALL 670 2026-11-09 (0DTE): 1,977 @ 5.91 = **+$1.2M** SELL | vol 55,417 / OI 4,213
- **SPY** CALL 754 2026-11-10 (1DTE): 1,796 @ 1.64 = **+$295k** SELL | vol 13,680 / OI 1,031
- **MU** CALL 735 2026-11-11 (2DTE): 123 @ 20.45 = **+$252k** SELL | vol 990 / OI 160
- **COIN** CALL 140 2026-11-13 (4DTE): 520 @ 3.94 = **+$205k** MID | vol 3,880 / OI 473
- **COIN** CALL 140 2026-11-13 (4DTE): 520 @ 3.94 = **+$205k** MID | vol 3,880 / OI 473
- **SMH** CALL 472.5 2026-11-09 (0DTE): 162 @ 11.10 = **+$180k** MID | vol 763 / OI 152
- **NVDA** CALL 177.5 2026-11-11 (2DTE): 315 @ 5.50 = **+$173k** BUY | vol 8,265 / OI 144
- **NVDA** CALL 180 2026-11-11 (2DTE): 400 @ 4.25 = **+$170k** BUY | vol 16,685 / OI 390
- **QQQ** CALL 679 2026-11-10 (1DTE): 500 @ 3.26 = **+$163k** SELL | vol 1,563 / OI 123
- **SMH** CALL 460 2026-11-13 (4DTE): 50 @ 27.80 = **+$139k** SELL | vol 380 / OI 589
- **SPY** PUT 756 2026-11-09 (0DTE): 200 @ 6.60 = **+$132k** BUY | vol 7,515 / OI 382
- **MU** CALL 735 2026-11-11 (2DTE): 60 @ 20.33 = **+$122k** SELL | vol 990 / OI 160
- **MU** CALL 732.5 2026-11-09 (0DTE): 155 @ 7.65 = **+$119k** SELL | vol 5,337 / OI 153
- **NVDA** PUT 170 2026-11-13 (4DTE): 500 @ 2.21 = **+$110k** SELL | vol 13,594 / OI 10,619

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 752 2026-11-10 (1DTE): 545 traded vs OI 285
- **SPY** CALL 746 2026-11-11 (2DTE): 1,063 traded vs OI 1,058
- **SPY** PUT 743 2026-11-11 (2DTE): 547 traded vs OI 406
- **SPY** CALL 782 2026-11-17 (8DTE): 1,500 traded vs OI 113
- **QQQ** PUT 612 2026-11-09 (0DTE): 1,184 traded vs OI 0
- **QQQ** PUT 665 2026-11-23 (14DTE): 608 traded vs OI 0
- **IWM** PUT 282 2026-11-09 (0DTE): 509 traded vs OI 310
- **IWM** PUT 273 2026-11-09 (0DTE): 2,074 traded vs OI 2,069
- **TSLA** CALL 367.5 2026-11-13 (4DTE): 509 traded vs OI 197
- **TSLA** PUT 342.5 2026-11-11 (2DTE): 554 traded vs OI 220
- **TSLA** CALL 392.5 2026-11-13 (4DTE): 575 traded vs OI 559
- **TSLA** CALL 390 2026-11-16 (7DTE): 507 traded vs OI 307
- **AAPL** CALL 367.5 2026-11-11 (2DTE): 551 traded vs OI 145
- **AAPL** CALL 350 2026-11-13 (4DTE): 4,152 traded vs OI 4,089
- **AMD** PUT 470 2026-11-11 (2DTE): 506 traded vs OI 91

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
