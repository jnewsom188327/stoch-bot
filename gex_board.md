# GEX + FLOW SCAN - Fri Nov 06, 10:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.82 | +12% (20m) | **+12%** | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.06 | -6% (1m) | **-91%** | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.34 | +32% (4m) | **-15%** | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:50:08 ET, last candle SPY 10:49, QQQ 10:49 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NVDA** | 189.88 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 59 | 11/06 192.5C @ 0.78 (delta 0.28) = est +159% at 193.49 | NEG -$362.1M | - | 200 | 190 | +$15.0M | +$2.5M bull / -$2.4M bear | LONG (clean 34, ADX 26, RVol 1.4) |
| 2 | **TSLA** | 358.13 | TREND (flow not with it) | **CALLS** | 42 | none: 116 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (51 contracts' greeks worked out here) | NEG -$252.4M | - | 370 | 360 | -$53.7M | +$5.5M bull / -$1.2M bear | LONG (clean 35, ADX 43, RVol 0.9) |
| 3 | **META** | 623.83 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 41 | none: 200 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (87 contracts' greeks worked out here) | POS +$16.7M | 623.15 | 650 | 625 | -$12.0M | +$25k bull / -$2.7M bear | out (clean 33, ADX 42, RVol 0.5) |
| 4 | **AAPL** | 344.81 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 40 | 11/06 347.5C @ 0.63 (delta 0.26) = est +343% at 350 | POS +$221.2M | 342.59 | 350 | 345 | -$13.8M | +$350k bull / -$1.5M bear | out (clean 29, ADX 14, RVol 0.8) |
| 5 | **MSTR** | 127.81 | FLIP CROSS up into positive gamma | **CALLS** | 39 | 11/06 131C @ 0.48 (delta 0.21) = est +153% at 130.79 | POS +$2.8M | 127.55 | 135 | 125 | -$6.0M | +$31k bull / -$1.9M bear | out (clean 31, ADX 19, RVol 1.1) |
| 6 | **CRM** | 213.11 | TREND (flow not with it) | **PUTS** | 36 | none: 32 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (23 contracts' greeks worked out here) | NEG -$21.5M | - | 230 | 215 | +$343k | - | SHORT (clean 34, ADX 44, RVol 1.1) |
| 7 | **AMZN** | 263.68 | - | **-** | 23 | - | POS +$397.5M | - | 265 | 265 | -$6.3M | +$31k bull / -$509k bear | out (clean 34, ADX 28, RVol 0.5) |
| 8 | **SMH** | 465.15 | - | **-** | 22 | - | NEG -$477.4M | - | 505 | 465 | +$4.3M | +$1.6M bull / -$888k bear | out (clean 34, ADX 17, RVol 3.0) |
| 9 | **DELL** | 337.72 | - | **-** | 22 | - | NEG -$26.7M | - | 370 | 335 | +$3.3M | +$0 bull / -$65k bear | out (clean 32, ADX 19, RVol 0.6) |
| 10 | **MU** | 692.24 | - | **-** | 22 | - | NEG -$158.5M | - | 700 | 700 | +$78.1M | +$5.4M bull / -$6.5M bear | out (clean 32, ADX 18, RVol 1.7) |
| 11 | **COIN** | 134.69 | - | **-** | 21 | - | NEG -$11.9M | 136.38 | 142 | 135 | -$2.2M | +$117k bull / +$0 bear | out (clean 31, ADX 17, RVol 0.4) |
| 12 | **HOOD** | 79.72 | - | **-** | 20 | - | NEG -$18.9M | 82.62 | 85 | 80 | +$2.4M | +$44k bull / -$108k bear | out (clean 29, ADX 24, RVol 0.7) |
| 13 | **MSFT** | 535.20 | - | **-** | 19 | - | POS +$650.9M | 512.46 | 540 | 540 | -$1.7M | +$0 bull / -$556k bear | out (clean 32, ADX 24, RVol 1.2) |
| 14 | **PLTR** | 161.10 | - | **-** | 19 | - | NEG -$63.7M | - | 165 | 160 | +$1.4M | +$215k bull / +$0 bear | out (clean 28, ADX 33, RVol 0.7) |
| 15 | **SPY** | 740.21 | - | **-** | 18 | - | NEG -$13.5B | 765.98 | 770 | 740 | -$89.8M | +$9.7M bull / -$1.2M bear | out (clean 35, ADX 17, RVol 1.0) |
| 16 | **GOOGL** | 288.05 | - | **-** | 18 | - | POS +$65.7M | 283.86 | 290 | 290 | +$2.0M | +$1.9M bull / +$0 bear | out (clean 34, ADX 22, RVol 0.8) |
| 17 | **IWM** | 272.42 | - | **-** | 17 | - | NEG -$3.0B | 284.74 | 285 | 270 | -$4.2M | +$75k bull / -$80k bear | out (clean 34, ADX 14, RVol 0.8) |
| 18 | **AMD** | 446.00 | - | **-** | 17 | - | NEG -$162.1M | - | 430 | 450 | +$2.4M | +$816k bull / -$832k bear | out (clean 32, ADX 23, RVol 1.3) |
| 19 | **AVGO** | 298.31 | - | **-** | 17 | - | NEG -$134.6M | - | 325 | 300 | -$311k | +$116k bull / -$360k bear | out (clean 31, ADX 20, RVol 1.6) |
| 20 | **BABA** | 108.70 | - | **-** | 17 | - | POS +$28.2M | - | 110 | 110 | -$227k | +$127k bull / -$32k bear | out (clean 34, ADX 17, RVol 0.7) |
| 21 | **ORCL** | 116.62 | - | **-** | 16 | - | NEG -$71.1M | - | 125 | 115 | +$396k | +$30k bull / +$0 bear | out (clean 31, ADX 14, RVol 0.5) |
| 22 | **QQQ** | 660.13 | - | **-** | 15 | - | NEG -$4.7B | - | 700 | 680 | +$8.9M | +$3.3M bull / -$2.6M bear | out (clean 35, ADX 19, RVol 0.9) |
| 23 | **SMCI** | 28.82 | - | **-** | 10 | - | NEG -$4.6M | - | 30 | 30 | +$297k | - | out (clean 35, ADX 31, RVol 0.5) |
| 24 | **ARM** | 172.84 | - | **-** | 9 | - | NEG -$23.6M | - | 190 | 170 | -$525k | - | out (clean 26, ADX 12, RVol 0.9) |
| 25 | **NFLX** | 64.02 | - | **-** | 8 | - | POS +$6.2M | 63.55 | 65 | 65 | -$167k | - | out (clean 32, ADX 24, RVol 0.9) |
| 26 | **UBER** | 69.50 | - | **-** | 7 | - | POS +$10.1M | 68.52 | 70 | 70 | +$110k | - | out (clean 30, ADX 12, RVol 0.6) |
| 27 | **SHOP** | 148.00 | - | **-** | 6 | - | NEG -$4.2M | 151.62 | 150 | 145 | +$8k | - | out (clean 37, ADX 24, RVol 0.6) |

## Big prints this scan (296)
- **MSTR** CALL 132 2026-11-13 (7DTE): 2,500 @ 3.66 = **+$915k** SELL | vol 11,364 / OI 365
- **MSTR** CALL 132 2026-11-13 (7DTE): 2,500 @ 3.66 = **+$915k** SELL | vol 11,364 / OI 365
- **QQQ** PUT 691 2026-11-13 (7DTE): 254 @ 35.00 = **+$889k** BUY | vol 2,115 / OI 2,850
- **TSLA** CALL 375 2026-11-13 (7DTE): 1,100 @ 5.16 = **+$568k** SELL | vol 4,448 / OI 1,716
- **AAPL** PUT 360 2026-11-13 (7DTE): 250 @ 17.45 = **+$436k** BUY | vol 712 / OI 1,394
- **MU** PUT 680 2026-11-06 (0DTE): 293 @ 11.95 = **+$350k** BUY | vol 12,651 / OI 858
- **MU** PUT 700 2026-11-09 (3DTE): 100 @ 32.30 = **+$323k** BUY | vol 3,104 / OI 183
- **MU** PUT 700 2026-11-06 (0DTE): 133 @ 20.00 = **+$266k** BUY | vol 18,228 / OI 2,759
- **MU** PUT 705 2026-11-06 (0DTE): 100 @ 25.46 = **+$255k** BUY | vol 4,611 / OI 0
- **QQQ** PUT 661 2026-11-06 (0DTE): 395 @ 6.16 = **+$243k** BUY | vol 30,665 / OI 371
- **QQQ** PUT 661 2026-11-06 (0DTE): 400 @ 5.99 = **+$240k** BUY | vol 30,665 / OI 371
- **SPY** PUT 755 2026-11-06 (0DTE): 140 @ 16.75 = **+$234k** BUY | vol 1,213 / OI 10,782
- **META** PUT 602.5 2026-11-13 (7DTE): 200 @ 9.50 = **+$190k** BUY | vol 245 / OI 77
- **TSLA** PUT 355 2026-11-06 (0DTE): 1,049 @ 1.80 = **+$189k** BUY | vol 26,657 / OI 4,127
- **QQQ** PUT 645 2026-11-13 (7DTE): 200 @ 8.79 = **+$176k** BUY | vol 751 / OI 2,223

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 739 2026-11-11 (5DTE): 510 traded vs OI 1
- **SPY** CALL 722 2026-11-06 (0DTE): 614 traded vs OI 52
- **SPY** PUT 732 2026-11-10 (4DTE): 570 traded vs OI 191
- **SPY** PUT 720 2026-11-09 (3DTE): 3,580 traded vs OI 3,093
- **SPY** CALL 754 2026-11-10 (4DTE): 502 traded vs OI 121
- **SPY** CALL 719 2026-11-06 (0DTE): 502 traded vs OI 28
- **SPY** PUT 746 2026-11-06 (0DTE): 2,705 traded vs OI 2,669
- **SPY** PUT 685 2026-11-10 (4DTE): 511 traded vs OI 323
- **SPY** PUT 734 2026-11-10 (4DTE): 502 traded vs OI 210
- **SPY** CALL 760 2026-11-12 (6DTE): 524 traded vs OI 489
- **SPY** PUT 710 2026-11-10 (4DTE): 543 traded vs OI 452
- **SPY** CALL 759 2026-11-10 (4DTE): 509 traded vs OI 75
- **SPY** CALL 788 2026-11-11 (5DTE): 1,317 traded vs OI 347
- **SPY** CALL 755 2026-11-13 (7DTE): 1,827 traded vs OI 1,250
- **SPY** CALL 747 2026-11-13 (7DTE): 500 traded vs OI 92

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
