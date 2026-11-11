# GEX + FLOW SCAN - Wed Nov 11, 10:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:20 | **AVGO** | **CALLS** | TREND + FLOW | 11/11 355C | 0.71 | 0.76 | +8% (8m) | **+7%** | +280% | 356.78 |
| 10:15 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.65 | 0.61 | +14% (3m) | **-6%** | +66% | 282.84 |
| 10:05 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 175C | 0.76 | 0.90 | +37% (24m) | **+18%** | +58% | 175 |
| 09:50 | **GOOGL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 292.5C | 0.51 | 0.39 | +39% (28m) | **-24%** | +82% | 291.86 |
| 09:45 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.68 | 0.61 | +85% (6m) | **-10%** | +68% | 282.96 |
| 09:45 | **QQQ** | **CALLS** | FLOW SURGE | 11/11 690C | 0.63 | 0.80 | +37% (43m) | **+27%** | +171% | 689.78 |
| 09:39 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 693C | 0.52 | 0.21 | -10% (0m) | **-60%** | +92% | 690.43 |
| 09:39 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 760C | 0.53 | 0.21 | -2% (0m) | **-60%** | +79% | 758.82 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:30:08 ET, last candle SPY 10:29, QQQ 10:29 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:02 | QQQ | 1m AGREE FLIP | FULL | CALLS | up | logged (agree flip) |
| 09:38 | QQQ | 1m WHIPSAW | R1 R5 | CALLS | TURNING away | **FIRE** QQQ261111C00693000 |
| 09:38 | SPY | 1m WHIPSAW | R1 R5 | CALLS | TURNING away | **FIRE** SPY261111C00760000 |

## Flow surges NOT fired - price disagreed (7 today, last 5)
- 10:15 BABA CALLS: under EMA 20 - flow says one way, price says the other
- 10:00 MSFT CALLS: price -4.55 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AMZN CALLS: price -0.73 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 AAPL PUTS: price +1.32 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSFT CALLS: price -2.01 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 519.83 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 64 | none: 162 calls 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (74 contracts' greeks worked out here) | POS +$65.7M | 513.59 | 535 | 520 | +$16.7M | +$602k bull / +$0 bear | out (clean 31, ADX 41, RVol 1.8) |
| 2 | **DELL** | 372.71 | FLOW SURGE | **PUTS** | 59 | none: 29 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$421k | - | 380 | 340 | -$2.0M | +$0 bull / -$267k bear | LONG (clean 35, ADX 58, RVol 2.3) |
| 3 | **AVGO** | 350.82 | TREND + FLOW | **CALLS** | 49 | 11/11 355C @ 0.67 (delta 0.22) = est +319% at 357.07 | POS +$90.8M | - | 350 | 350 | +$4.1M | +$213k bull / -$33k bear | LONG (clean 35, ADX 51, RVol 1.4) |
| 4 | **MU** | 806.49 | FLOW SURGE | **PUTS** | 47 | none: 153 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (69 contracts' greeks worked out here) | POS +$149.7M | - | 800 | 800 | -$130.6M | +$1.3M bull / -$17.4M bear | out (clean 33, ADX 57, RVol 1.7) |
| 5 | **BABA** | 101.38 | FLOW SURGE | **CALLS** | 47 | none: 20 calls 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +18% at the target (needs +20%) | NEG -$16.1M | 106.87 | 110 | 101 | +$384k | +$27k bull / +$0 bear | out (clean 29, ADX 31, RVol 1.1) |
| 6 | **IWM** | 281.96 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 46 | 11/11 282C @ 0.60 (delta 0.49) = est +56% at 282.72 | NEG -$303.5M | 282.72 | 285 | 270 | +$145k | - | LONG (clean 35, ADX 38, RVol 0.9) |
| 7 | **GOOGL** | 290.62 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 44 | 11/11 292.5C @ 0.49 (delta 0.27) = est +96% at 292.44 | POS +$34.1M | 289.12 | 300 | 290 | +$1.2M | +$30k bull / +$0 bear | out (clean 28, ADX 45, RVol 0.9) |
| 8 | **NVDA** | 174.20 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 42 | none: 56 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (22 contracts' greeks worked out here) | NEG -$179.9M | - | 180 | 175 | +$1.1M | +$1.5M bull / -$1.7M bear | LONG (clean 34, ADX 28, RVol 0.8) |
| 9 | **AMZN** | 266.49 | FLOW SURGE | **CALLS** | 41 | none: 88 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (35 contracts' greeks worked out here) | POS +$421.5M | - | 270 | 265 | +$5.9M | +$220k bull / +$0 bear | out (clean 33, ADX 29, RVol 1.3) |
| 10 | **AMD** | 543.72 | TREND (flow not with it) | **CALLS** | 39 | none: 176 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (73 contracts' greeks worked out here) | POS +$121.3M | - | 550 | 500 | -$38.2M | +$4.8M bull / -$7.9M bear | LONG (clean 33, ADX 37, RVol 1.6) |
| 11 | **COIN** | 134.72 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 29 | none: 27 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$16.6M | 127.24 | 137 | 135 | +$112k | - | out (clean 28, ADX 29, RVol 0.8) |
| 12 | **PLTR** | 172.16 | - | **-** | 27 | - | POS +$73.9M | - | 170 | 170 | +$1.5M | +$0 bull / -$151k bear | out (clean 30, ADX 41, RVol 0.3) |
| 13 | **ORCL** | 125.93 | - | **-** | 26 | - | NEG -$2.4M | 128.46 | 130 | 125 | +$929k | +$35k bull / -$26k bear | out (clean 28, ADX 46, RVol 0.8) |
| 14 | **TSLA** | 393.80 | - | **-** | 24 | - | POS +$413.1M | - | 400 | 380 | -$17.9M | +$450k bull / -$4.5M bear | out (clean 33, ADX 50, RVol 1.0) |
| 15 | **ARM** | 197.78 | - | **-** | 24 | - | POS +$3.9M | - | 200 | 200 | -$520k | - | out (clean 29, ADX 56, RVol 0.5) |
| 16 | **META** | 635.85 | - | **-** | 23 | - | POS +$173.9M | 626.06 | 650 | 625 | +$5.2M | +$709k bull / -$58k bear | out (clean 30, ADX 22, RVol 0.6) |
| 17 | **SMH** | 505.21 | - | **-** | 22 | - | NEG -$76.1M | - | 500 | 475 | -$941k | +$271k bull / -$449k bear | out (clean 31, ADX 38, RVol 0.9) |
| 18 | **SPY** | 756.54 | - | **-** | 21 | - | NEG -$3.7B | 760.81 | 760 | 750 | +$15.2M | +$372k bull / -$434k bear | out (clean 31, ADX 47, RVol 0.4) |
| 19 | **QQQ** | 687.88 | - | **-** | 21 | - | NEG -$463.3M | 689.93 | 700 | 680 | -$17.9M | +$893k bull / -$1.9M bear | out (clean 32, ADX 48, RVol 0.5) |
| 20 | **AAPL** | 353.49 | - | **-** | 21 | - | POS +$1.4B | 340.97 | 355 | 350 | -$1.3M | +$227k bull / -$84k bear | out (clean 27, ADX 44, RVol 1.0) |
| 21 | **SMCI** | 30.27 | - | **-** | 21 | - | POS +$11.4M | - | 30 | 30 | -$281k | - | out (clean 32, ADX 50, RVol 1.0) |
| 22 | **MSTR** | 120.68 | - | **-** | 17 | - | NEG -$22.6M | - | 132 | 120 | +$472k | +$61k bull / +$0 bear | out (clean 28, ADX 14, RVol 0.5) |
| 23 | **UBER** | 69.20 | - | **-** | 13 | - | POS +$8.0M | 68.26 | 70 | 70 | +$17k | - | out (clean 32, ADX 24, RVol 0.7) |
| 24 | **HOOD** | 83.67 | - | **-** | 11 | - | POS +$13.3M | - | 85 | 80 | -$122k | - | out (clean 32, ADX 32, RVol 0.9) |
| 25 | **CRM** | 214.53 | - | **-** | 10 | - | NEG -$11.5M | - | 230 | 220 | -$13k | - | out (clean 31, ADX 27, RVol 1.1) |
| 26 | **SHOP** | 148.00 | - | **-** | 10 | - | POS +$2.1M | 144.87 | 150 | 140 | +$1k | - | out (clean 33, ADX 41, RVol 0.2) |
| 27 | **NFLX** | 63.37 | - | **-** | 8 | - | NEG -$14.4M | 64.48 | 65 | 65 | +$83k | - | out (clean 27, ADX 15, RVol 1.1) |

## Big prints this scan (202)
- **AMD** PUT 540 2026-11-11 (0DTE): 959 @ 5.40 = **+$518k** BUY | vol 4,788 / OI 20
- **AMD** CALL 522.5 2026-11-13 (2DTE): 100 @ 26.39 = **+$264k** SELL | vol 410 / OI 248
- **QQQ** CALL 665 2026-11-18 (7DTE): 99 @ 24.78 = **+$245k** SELL | vol 126 / OI 424
- **MU** CALL 770 2026-11-11 (0DTE): 86 @ 26.05 = **+$224k** SELL | vol 6,106 / OI 1,346
- **AMD** CALL 527.5 2026-11-13 (2DTE): 97 @ 22.00 = **+$213k** SELL | vol 652 / OI 263
- **AMD** CALL 525 2026-11-13 (2DTE): 80 @ 25.30 = **+$202k** MID | vol 1,201 / OI 1,343
- **QQQ** CALL 684 2026-11-11 (0DTE): 603 @ 3.25 = **+$196k** SELL | vol 12,887 / OI 694
- **MU** PUT 790 2026-11-13 (2DTE): 100 @ 19.50 = **+$195k** BUY | vol 801 / OI 468
- **SPY** CALL 740 2026-11-18 (7DTE): 100 @ 18.08 = **+$181k** SELL | vol 101 / OI 495
- **TSLA** CALL 377.5 2026-11-11 (0DTE): 100 @ 16.00 = **+$160k** MID | vol 1,100 / OI 688
- **TSLA** CALL 390 2026-11-11 (0DTE): 442 @ 3.60 = **+$159k** SELL | vol 74,929 / OI 2,864
- **SPY** PUT 756 2026-11-12 (1DTE): 500 @ 2.90 = **+$145k** BUY | vol 11,421 / OI 213
- **MU** CALL 790 2026-11-11 (0DTE): 146 @ 9.75 = **+$142k** SELL | vol 12,033 / OI 453
- **TSLA** CALL 400 2026-11-13 (2DTE): 454 @ 3.00 = **+$136k** SELL | vol 15,264 / OI 11,714
- **QQQ** PUT 685 2026-11-13 (2DTE): 250 @ 5.21 = **+$130k** BUY | vol 6,164 / OI 23,913

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 765 2026-11-13 (2DTE): 6,996 traded vs OI 6,883
- **SPY** PUT 748 2026-11-16 (5DTE): 550 traded vs OI 532
- **SPY** PUT 764 2026-11-11 (0DTE): 547 traded vs OI 31
- **SPY** CALL 830 2026-11-19 (8DTE): 5,499 traded vs OI 100
- **QQQ** PUT 621 2026-11-12 (1DTE): 611 traded vs OI 147
- **QQQ** PUT 671 2026-11-13 (2DTE): 505 traded vs OI 457
- **QQQ** CALL 696 2026-11-12 (1DTE): 1,202 traded vs OI 1,189
- **IWM** CALL 281 2026-11-17 (6DTE): 509 traded vs OI 151
- **IWM** CALL 286 2026-11-12 (1DTE): 1,337 traded vs OI 333
- **SMH** CALL 517.5 2026-11-13 (2DTE): 593 traded vs OI 419
- **NVDA** CALL 172.5 2026-11-18 (7DTE): 507 traded vs OI 231
- **NVDA** CALL 190 2026-11-18 (7DTE): 4,856 traded vs OI 4,101
- **TSLA** CALL 420 2026-11-13 (2DTE): 4,729 traded vs OI 4,264
- **TSLA** PUT 397.5 2026-11-11 (0DTE): 595 traded vs OI 490
- **TSLA** CALL 402.5 2026-11-13 (2DTE): 2,160 traded vs OI 1,935

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
