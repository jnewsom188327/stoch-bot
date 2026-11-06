# GEX + FLOW SCAN - Fri Nov 06, 11:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.28 | +12% (20m) | **-62%** (done) | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.03 | -6% (1m) | **-96%** (done) | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.36 | +32% (4m) | **-10%** (done) | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:40:08 ET, last candle SPY 11:39, QQQ 11:39 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 344.69 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 37 | none: 108 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (48 contracts' greeks worked out here) | POS +$128.5M | 343.32 | 350 | 345 | -$18.7M | +$434k bull / +$0 bear | out (clean 29, ADX 12, RVol 0.5) |
| 2 | **TSLA** | 361.28 | - | **-** | 24 | - | NEG -$275.4M | - | 370 | 360 | -$72.0M | +$0 bull / -$521k bear | out (clean 35, ADX 38, RVol 0.6) |
| 3 | **COIN** | 133.33 | - | **-** | 22 | - | NEG -$20.2M | 136.88 | 142 | 130 | -$3.0M | +$0 bull / -$994k bear | out (clean 32, ADX 21, RVol 0.6) |
| 4 | **MSTR** | 128.09 | - | **-** | 21 | - | POS +$2.3M | 127.9 | 135 | 125 | -$7.2M | +$0 bull / -$92k bear | out (clean 31, ADX 12, RVol 0.6) |
| 5 | **META** | 621.87 | - | **-** | 20 | - | NEG -$51.3M | 624.02 | 650 | 625 | -$8.3M | +$54k bull / -$765k bear | out (clean 33, ADX 34, RVol 0.7) |
| 6 | **DELL** | 334.81 | - | **-** | 20 | - | NEG -$27.8M | - | 340 | 335 | +$4.3M | +$70k bull / -$110k bear | out (clean 33, ADX 13, RVol 0.5) |
| 7 | **BABA** | 109.34 | - | **-** | 19 | - | POS +$26.2M | 106.33 | 110 | 110 | -$411k | +$0 bull / -$57k bear | out (clean 34, ADX 21, RVol 0.7) |
| 8 | **SMH** | 466.01 | - | **-** | 18 | - | NEG -$573.7M | - | 505 | 470 | +$6.0M | +$0 bull / -$918k bear | out (clean 34, ADX 13, RVol 0.8) |
| 9 | **AMZN** | 263.55 | - | **-** | 18 | - | POS +$383.1M | - | 265 | 265 | -$2.9M | +$0 bull / -$238k bear | out (clean 34, ADX 25, RVol 0.4) |
| 10 | **PLTR** | 162.09 | - | **-** | 18 | - | NEG -$73.3M | - | 165 | 160 | +$2.3M | +$0 bull / -$114k bear | out (clean 28, ADX 26, RVol 0.6) |
| 11 | **HOOD** | 80.09 | - | **-** | 18 | - | NEG -$22.4M | 84.08 | 85 | 80 | +$2.9M | +$0 bull / -$185k bear | out (clean 30, ADX 19, RVol 0.5) |
| 12 | **IWM** | 273.28 | - | **-** | 17 | - | NEG -$3.2B | 284.8 | 285 | 270 | -$5.3M | +$0 bull / -$134k bear | out (clean 34, ADX 18, RVol 0.5) |
| 13 | **NVDA** | 189.20 | - | **-** | 17 | - | NEG -$407.9M | - | 200 | 190 | +$19.0M | +$110k bull / -$1.3M bear | out (clean 34, ADX 16, RVol 0.8) |
| 14 | **MU** | 699.58 | - | **-** | 17 | - | NEG -$207.5M | - | 700 | 700 | +$57.3M | +$103k bull / -$8.3M bear | out (clean 32, ADX 12, RVol 0.8) |
| 15 | **SPY** | 740.67 | - | **-** | 16 | - | NEG -$14.7B | 768.92 | 770 | 740 | -$85.7M | +$0 bull / -$1.0M bear | out (clean 35, ADX 14, RVol 0.8) |
| 16 | **AMD** | 443.98 | - | **-** | 16 | - | NEG -$179.0M | - | 430 | 450 | +$6.7M | +$0 bull / -$780k bear | out (clean 33, ADX 19, RVol 0.9) |
| 17 | **QQQ** | 661.50 | - | **-** | 15 | - | NEG -$6.0B | - | 700 | 680 | +$28.8M | +$0 bull / -$3.3M bear | out (clean 35, ADX 16, RVol 0.6) |
| 18 | **AVGO** | 297.19 | - | **-** | 15 | - | NEG -$145.3M | - | 325 | 300 | +$1.3M | +$183k bull / -$90k bear | out (clean 31, ADX 12, RVol 0.8) |
| 19 | **ORCL** | 116.38 | - | **-** | 15 | - | NEG -$71.0M | - | 125 | 115 | +$566k | +$26k bull / +$0 bear | out (clean 30, ADX 9, RVol 0.4) |
| 20 | **GOOGL** | 287.98 | - | **-** | 14 | - | POS +$61.4M | 285.24 | 290 | 290 | +$368k | +$0 bull / -$602k bear | out (clean 34, ADX 16, RVol 0.5) |
| 21 | **ARM** | 174.06 | - | **-** | 8 | - | NEG -$25.3M | - | 190 | 170 | -$459k | - | out (clean 25, ADX 12, RVol 0.8) |
| 22 | **SHOP** | 149.94 | - | **-** | 8 | - | NEG -$4.2M | 151.77 | 150 | 150 | -$32k | - | out (clean 36, ADX 29, RVol 0.5) |
| 23 | **SMCI** | 28.64 | - | **-** | 7 | - | NEG -$3.5M | 29.84 | 30 | 29 | +$282k | - | out (clean 35, ADX 22, RVol 0.3) |
| 24 | **NFLX** | 64.21 | - | **-** | 6 | - | POS +$5.7M | 63.96 | 64 | 65 | -$295k | - | out (clean 32, ADX 15, RVol 0.5) |
| 25 | **CRM** | 216.51 | - | **-** | 6 | - | NEG -$28.2M | - | 230 | 220 | -$20k | - | out (clean 34, ADX 27, RVol 0.6) |
| 26 | **MSFT** | 536.56 | - | **-** | 5 | - | POS +$705.4M | 511.74 | 540 | 540 | +$915k | - | out (clean 33, ADX 17, RVol 0.6) |
| 27 | **UBER** | 69.60 | - | **-** | 5 | - | POS +$15.0M | 68.72 | 70 | 70 | +$96k | - | out (clean 30, ADX 8, RVol 0.5) |

## Big prints this scan (121)
- **GOOGL** CALL 295 2026-11-13 (7DTE): 976 @ 2.72 = **+$265k** SELL | vol 1,623 / OI 1,680
- **GOOGL** PUT 275 2026-11-13 (7DTE): 976 @ 2.20 = **+$215k** BUY | vol 1,543 / OI 1,554
- **QQQ** CALL 653 2026-11-06 (0DTE): 357 @ 6.01 = **+$215k** SELL | vol 8,117 / OI 0
- **SPY** PUT 735 2026-11-13 (7DTE): 240 @ 8.21 = **+$197k** BUY | vol 8,883 / OI 3,260
- **MU** CALL 700 2026-11-09 (3DTE): 100 @ 19.35 = **+$194k** SELL | vol 2,567 / OI 5
- **SPY** PUT 734 2026-11-13 (7DTE): 240 @ 7.88 = **+$189k** BUY | vol 1,282 / OI 1,344
- **SPY** PUT 738 2026-11-06 (0DTE): 781 @ 2.35 = **+$184k** BUY | vol 117,055 / OI 2,709
- **QQQ** PUT 660 2026-11-09 (3DTE): 200 @ 8.75 = **+$175k** BUY | vol 13,660 / OI 1,084
- **QQQ** PUT 660 2026-11-06 (0DTE): 390 @ 4.20 = **+$164k** BUY | vol 98,922 / OI 12,054
- **QQQ** PUT 660 2026-11-09 (3DTE): 200 @ 8.13 = **+$163k** BUY | vol 13,660 / OI 1,084
- **QQQ** PUT 660 2026-11-09 (3DTE): 200 @ 8.10 = **+$162k** BUY | vol 13,660 / OI 1,084
- **QQQ** PUT 660 2026-11-09 (3DTE): 200 @ 8.00 = **+$160k** BUY | vol 13,660 / OI 1,084
- **QQQ** PUT 660 2026-11-06 (0DTE): 357 @ 4.39 = **+$157k** BUY | vol 98,922 / OI 12,054
- **MU** CALL 680 2026-11-09 (3DTE): 50 @ 31.15 = **+$156k** SELL | vol 1,038 / OI 0
- **MU** CALL 680 2026-11-09 (3DTE): 50 @ 31.10 = **+$156k** SELL | vol 1,038 / OI 0

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 779 2026-11-09 (3DTE): 3,678 traded vs OI 308
- **SPY** CALL 685 2026-11-10 (4DTE): 500 traded vs OI 0
- **SPY** PUT 728 2026-11-11 (5DTE): 508 traded vs OI 187
- **SPY** CALL 766 2026-11-13 (7DTE): 1,291 traded vs OI 1,272
- **SPY** CALL 760 2026-11-13 (7DTE): 2,721 traded vs OI 2,712
- **SPY** CALL 739 2026-11-27 (21DTE): 515 traded vs OI 1
- **QQQ** PUT 661 2026-11-10 (4DTE): 520 traded vs OI 84
- **QQQ** CALL 713 2026-11-12 (6DTE): 1,021 traded vs OI 43
- **QQQ** PUT 657 2026-11-13 (7DTE): 508 traded vs OI 86
- **IWM** CALL 281 2026-11-13 (7DTE): 834 traded vs OI 826
- **IWM** CALL 300 2026-11-20 (14DTE): 506 traded vs OI 0
- **SMH** PUT 457.5 2026-11-06 (0DTE): 506 traded vs OI 219
- **NVDA** CALL 177.5 2026-11-09 (3DTE): 695 traded vs OI 0
- **TSLA** CALL 387.5 2026-11-09 (3DTE): 544 traded vs OI 0
- **TSLA** CALL 382.5 2026-11-06 (0DTE): 1,301 traded vs OI 1,269

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
