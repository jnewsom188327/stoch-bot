# GEX + FLOW SCAN - Mon Nov 02, 10:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:00:08 ET, last candle SPY 09:59, QQQ 09:59 | no errors

## Flow surges NOT fired - price disagreed (1 today, last 5)
- 09:50 BABA PUTS: price +0.75 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **ORCL** | 122.61 | FLOW SURGE | **CALLS** | 61 | none: 24 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$37.0M | - | 130 | 120 | +$1.7M | +$317k bull / +$0 bear | out (clean 32, ADX 37, RVol 3.3) |
| 2 | **BABA** | 103.53 | FLOW SURGE | **PUTS** | 59 | none: 20 puts 0-7DTE > 3 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +17% at the target (needs +20%) (1 contracts' greeks worked out here) | POS +$3.1M | 100.89 | 105 | 100 | -$1.1M | +$0 bull / -$605k bear | out (clean 32, ADX 47, RVol 6.0) |
| 3 | **MU** | 873.64 | FLOW SURGE | **CALLS** | 58 | none: 148 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (59 contracts' greeks worked out here) | NEG -$201.2M | - | 910 | 850 | +$28.5M | +$11.7M bull / -$205k bear | out (clean 30, ADX 28, RVol 3.0) |
| 4 | **TSLA** | 400.31 | PINNED between the walls (positive gamma) - chop | **-** | 57 | - | POS +$197.0M | - | 400 | 400 | +$47.5M | +$8.6M bull / +$0 bear | out (clean 30, ADX 28, RVol 2.2) |
| 5 | **SMH** | 525.51 | FLOW SURGE | **CALLS** | 55 | none: 168 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (79 contracts' greeks worked out here) | NEG -$321.8M | - | 532.5 | 500 | +$2.6M | +$1.2M bull / -$211k bear | out (clean 31, ADX 37, RVol 2.2) |
| 6 | **AMZN** | 250.19 | PINNED between the walls (positive gamma) - chop | **-** | 54 | - | POS +$89.1M | 241.94 | 250 | 250 | -$17.7M | +$279k bull / -$1.6M bear | out (clean 31, ADX 45, RVol 1.9) |
| 7 | **AAPL** | 340.38 | FLOW SURGE | **CALLS** | 53 | none: 81 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$45.1M | 336.75 | 350 | 330 | +$4.3M | +$2.1M bull / +$0 bear | out (clean 32, ADX 30, RVol 3.5) |
| 8 | **SMCI** | 33.01 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 52 | none: 13 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$582k | - | 35 | 33 | +$135k | +$140k bull / +$0 bear | out (clean 32, ADX 46, RVol 1.5) |
| 9 | **UBER** | 66.89 | FLOW SURGE | **PUTS** | 51 | none: 13 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$8.2M | - | 70 | 65 | -$236k | +$0 bull / -$28k bear | out (clean 27, ADX 36, RVol 1.3) |
| 10 | **META** | 617.07 | FLOW SURGE | **PUTS** | 48 | none: 194 puts 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (89 contracts' greeks worked out here) | NEG -$87.4M | 625.76 | 650 | 600 | -$6.4M | +$273k bull / -$708k bear | out (clean 29, ADX 31, RVol 1.5) |
| 11 | **AMD** | 503.66 | FLOW SURGE | **CALLS** | 46 | none: 160 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (72 contracts' greeks worked out here) | NEG -$92.2M | - | 550 | 500 | +$7.9M | +$6.9M bull / -$555k bear | out (clean 30, ADX 34, RVol 1.6) |
| 12 | **ARM** | 201.10 | FLOW SURGE | **CALLS** | 46 | none: 16 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$6.4M | - | 220 | 200 | +$329k | +$38k bull / +$0 bear | out (clean 26, ADX 25, RVol 0.6) |
| 13 | **DELL** | 410.93 | FLOW SURGE | **CALLS** | 44 | none: 33 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$23.3M | - | 440 | 400 | +$1.1M | +$180k bull / +$0 bear | out (clean 34, ADX 27, RVol 1.5) |
| 14 | **MSTR** | 133.17 | FLOW SURGE | **CALLS** | 43 | none: 27 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$2.5M | - | 135 | 125 | +$1.7M | +$664k bull / -$33k bear | out (clean 27, ADX 35, RVol 1.4) |
| 15 | **GOOGL** | 285.56 | TREND (flow not with it) | **CALLS** | 42 | none: 92 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (40 contracts' greeks worked out here) | NEG -$73.4M | - | 285 | 290 | -$3.3M | +$124k bull / -$2.0M bear | LONG (clean 33, ADX 47, RVol 1.8) |
| 16 | **MSFT** | 525.77 | - | **-** | 35 | - | POS +$367.3M | 500.36 | 540 | 530 | -$5.8M | +$617k bull / -$286k bear | out (clean 27, ADX 23, RVol 2.7) |
| 17 | **SPY** | 760.46 | - | **-** | 29 | - | NEG -$9.2B | 774.61 | 800 | 750 | -$34.9M | +$0 bull / -$3.9M bear | out (clean 29, ADX 39, RVol 1.2) |
| 18 | **IWM** | 282.79 | - | **-** | 28 | - | NEG -$729.7M | 286.61 | 285 | 270 | -$1.9M | +$57k bull / +$0 bear | out (clean 31, ADX 39, RVol 2.8) |
| 19 | **AVGO** | 328.61 | - | **-** | 28 | - | NEG -$103.4M | - | 340 | 330 | -$2.4M | +$0 bull / -$273k bear | out (clean 30, ADX 40, RVol 1.3) |
| 20 | **NVDA** | 207.94 | - | **-** | 24 | - | NEG -$165.4M | 214.03 | 210 | 210 | +$2.9M | +$2.6M bull / -$1.6M bear | out (clean 30, ADX 36, RVol 2.5) |
| 21 | **NFLX** | 61.90 | - | **-** | 22 | - | NEG -$23.8M | - | 63 | 60 | +$345k | - | out (clean 30, ADX 35, RVol 3.0) |
| 22 | **COIN** | 140.75 | - | **-** | 22 | - | NEG -$8.0M | - | 150 | 130 | +$161k | - | out (clean 26, ADX 36, RVol 1.8) |
| 23 | **PLTR** | 184.38 | - | **-** | 21 | - | NEG -$10.9M | - | 200 | 180 | -$451k | +$258k bull / -$167k bear | out (clean 26, ADX 13, RVol 3.4) |
| 24 | **QQQ** | 694.70 | - | **-** | 20 | - | NEG -$5.5B | 731.22 | 720 | 680 | +$4.6M | +$5.5M bull / -$2.0M bear | out (clean 30, ADX 37, RVol 1.3) |
| 25 | **HOOD** | 86.36 | - | **-** | 19 | - | NEG -$8.9M | - | 93 | 90 | -$541k | - | out (clean 32, ADX 54, RVol 0.6) |
| 26 | **CRM** | 229.97 | - | **-** | 19 | - | NEG -$6.2M | 242.73 | 240 | 220 | +$36k | - | out (clean 28, ADX 28, RVol 1.6) |
| 27 | **SHOP** | 158.43 | - | **-** | 14 | - | NEG -$361k | - | 170 | 160 | +$8k | - | out (clean 28, ADX 41, RVol 4.4) |

## Big prints this scan (222)
- **NVDA** CALL 205 2026-11-04 (2DTE): 798 @ 5.55 = **+$443k** BUY | vol 1,876 / OI 108
- **QQQ** CALL 700 2026-11-06 (4DTE): 589 @ 7.40 = **+$436k** BUY | vol 3,497 / OI 1,051
- **MSFT** CALL 525 2026-11-04 (2DTE): 470 @ 7.60 = **+$357k** BUY | vol 973 / OI 227
- **NVDA** CALL 205 2026-11-02 (0DTE): 991 @ 3.50 = **+$347k** BUY | vol 6,364 / OI 254
- **AMD** CALL 515 2026-11-09 (7DTE): 165 @ 20.13 = **+$332k** MID | vol 369 / OI 4
- **NVDA** CALL 207.5 2026-11-02 (0DTE): 1,982 @ 1.63 = **+$323k** BUY | vol 21,185 / OI 510
- **AMD** CALL 515 2026-11-06 (4DTE): 165 @ 18.85 = **+$311k** SELL | vol 428 / OI 108
- **QQQ** CALL 700 2026-11-06 (4DTE): 408 @ 7.40 = **+$302k** BUY | vol 3,497 / OI 1,051
- **AMD** CALL 497.5 2026-11-09 (7DTE): 100 @ 29.13 = **+$291k** MID | vol 107 / OI 0
- **TSLA** CALL 400 2026-11-02 (0DTE): 445 @ 6.35 = **+$283k** BUY | vol 4,924 / OI 1,359
- **SPY** PUT 754 2026-11-06 (4DTE): 677 @ 3.81 = **+$258k** BUY | vol 6,117 / OI 1,038
- **TSLA** PUT 410 2026-11-02 (0DTE): 432 @ 5.25 = **+$227k** SELL | vol 4,575 / OI 492
- **MU** PUT 915 2026-11-02 (0DTE): 62 @ 35.00 = **+$217k** SELL | vol 104 / OI 255
- **AMZN** CALL 245 2026-11-06 (4DTE): 277 @ 7.63 = **+$211k** SELL | vol 1,555 / OI 1,666
- **TSLA** CALL 400 2026-11-02 (0DTE): 268 @ 6.50 = **+$174k** BUY | vol 4,924 / OI 1,359

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 737 2026-11-02 (0DTE): 3,112 traded vs OI 1,225
- **SPY** CALL 772 2026-11-02 (0DTE): 1,451 traded vs OI 1,166
- **SPY** CALL 752 2026-11-02 (0DTE): 652 traded vs OI 84
- **SPY** PUT 752 2026-11-03 (1DTE): 2,643 traded vs OI 1,628
- **SPY** CALL 769 2026-11-02 (0DTE): 3,327 traded vs OI 2,587
- **SPY** PUT 757 2026-11-03 (1DTE): 533 traded vs OI 386
- **SPY** CALL 771 2026-11-02 (0DTE): 1,329 traded vs OI 1,305
- **SPY** CALL 773 2026-11-02 (0DTE): 1,042 traded vs OI 1,016
- **SPY** CALL 753 2026-11-02 (0DTE): 598 traded vs OI 31
- **SPY** PUT 750 2026-11-05 (3DTE): 2,976 traded vs OI 1,759
- **SPY** CALL 775 2026-11-12 (10DTE): 6,236 traded vs OI 282
- **QQQ** CALL 704 2026-11-03 (1DTE): 543 traded vs OI 46
- **QQQ** PUT 674 2026-11-03 (1DTE): 602 traded vs OI 0
- **QQQ** CALL 687 2026-11-02 (0DTE): 711 traded vs OI 0
- **QQQ** PUT 665 2026-11-03 (1DTE): 905 traded vs OI 889

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
