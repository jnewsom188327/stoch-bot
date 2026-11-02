# GEX + FLOW SCAN - Mon Nov 02, 11:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:10:08 ET, last candle SPY 11:09, QQQ 11:09 | no errors

## Flow surges NOT fired - price disagreed (5 today, last 5)
- 10:35 SPY PUTS: price +0.32 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:25 SPY PUTS: price +2.69 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:10 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 10:05 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 09:50 BABA PUTS: price +0.75 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSTR** | 135.07 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 47 | none: 27 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$3.1M | - | 135 | 125 | +$2.9M | +$183k bull / +$0 bear | out (clean 27, ADX 40, RVol 1.1) |
| 2 | **AMZN** | 253.26 | - | **-** | 28 | - | POS +$125.9M | 242.39 | 265 | 250 | -$26.1M | +$2.0M bull / -$1.1M bear | out (clean 33, ADX 69, RVol 0.8) |
| 3 | **AVGO** | 332.09 | - | **-** | 27 | - | NEG -$95.6M | - | 340 | 330 | -$6.1M | +$262k bull / +$0 bear | out (clean 32, ADX 53, RVol 0.7) |
| 4 | **UBER** | 67.33 | - | **-** | 27 | - | NEG -$8.3M | - | 70 | 65 | -$275k | +$33k bull / +$0 bear | out (clean 28, ADX 52, RVol 0.8) |
| 5 | **SMH** | 525.85 | - | **-** | 26 | - | NEG -$334.0M | - | 532.5 | 500 | +$2.6M | +$118k bull / +$0 bear | out (clean 31, ADX 38, RVol 0.6) |
| 6 | **TSLA** | 412.49 | - | **-** | 26 | - | POS +$316.8M | - | 410 | 400 | -$93.5M | +$4.3M bull / -$2.9M bear | out (clean 30, ADX 40, RVol 1.6) |
| 7 | **MU** | 870.37 | - | **-** | 26 | - | NEG -$221.8M | - | 910 | 850 | +$48.9M | +$5.5M bull / +$0 bear | out (clean 30, ADX 22, RVol 1.6) |
| 8 | **AMD** | 492.84 | - | **-** | 25 | - | NEG -$90.3M | - | 540 | 500 | +$18.7M | +$3.1M bull / +$0 bear | out (clean 30, ADX 30, RVol 1.4) |
| 9 | **SHOP** | 159.34 | - | **-** | 24 | - | NEG -$432k | - | 175 | 175 | -$430k | - | out (clean 28, ADX 30, RVol 2.9) |
| 10 | **BABA** | 103.58 | - | **-** | 24 | - | POS +$2.8M | 101.15 | 105 | 100 | -$1.2M | - | out (clean 33, ADX 61, RVol 1.4) |
| 11 | **SPY** | 760.85 | - | **-** | 22 | - | NEG -$9.4B | 775.27 | 770 | 750 | -$67.0M | +$3.3M bull / +$0 bear | out (clean 29, ADX 41, RVol 0.7) |
| 12 | **MSFT** | 523.31 | - | **-** | 21 | - | POS +$311.9M | 500.89 | 540 | 530 | -$3.5M | +$430k bull / +$0 bear | out (clean 26, ADX 25, RVol 1.2) |
| 13 | **IWM** | 282.50 | - | **-** | 20 | - | NEG -$835.3M | 286.44 | 285 | 270 | -$1.4M | +$287k bull / -$65k bear | out (clean 31, ADX 44, RVol 0.4) |
| 14 | **AAPL** | 340.65 | - | **-** | 20 | - | POS +$59.0M | 336.74 | 350 | 330 | +$6.9M | +$2.0M bull / -$228k bear | out (clean 31, ADX 19, RVol 1.2) |
| 15 | **SMCI** | 32.44 | - | **-** | 20 | - | POS +$25k | 31.91 | 35 | 33 | +$58k | +$26k bull / +$0 bear | out (clean 33, ADX 34, RVol 1.3) |
| 16 | **NVDA** | 207.35 | - | **-** | 19 | - | NEG -$200.0M | 214.83 | 210 | 200 | +$3.9M | +$787k bull / -$699k bear | out (clean 30, ADX 29, RVol 1.3) |
| 17 | **GOOGL** | 283.36 | - | **-** | 19 | - | NEG -$94.1M | - | 285 | 290 | +$825k | +$28k bull / +$0 bear | out (clean 34, ADX 40, RVol 0.6) |
| 18 | **ORCL** | 123.40 | - | **-** | 19 | - | NEG -$40.0M | - | 130 | 120 | -$517k | +$140k bull / +$0 bear | out (clean 32, ADX 35, RVol 0.6) |
| 19 | **META** | 612.48 | - | **-** | 18 | - | NEG -$132.1M | 626.81 | 650 | 600 | +$3.0M | +$829k bull / -$100k bear | out (clean 29, ADX 27, RVol 0.7) |
| 20 | **PLTR** | 184.86 | - | **-** | 18 | - | NEG -$11.1M | - | 200 | 180 | -$1.8M | +$209k bull / -$44k bear | out (clean 25, ADX 12, RVol 0.7) |
| 21 | **QQQ** | 695.12 | - | **-** | 17 | - | NEG -$5.7B | 731.81 | 720 | 680 | -$5.6M | +$3.6M bull / +$0 bear | out (clean 30, ADX 35, RVol 0.4) |
| 22 | **HOOD** | 86.56 | - | **-** | 12 | - | NEG -$9.2M | - | 93 | 90 | -$648k | - | out (clean 32, ADX 50, RVol 0.5) |
| 23 | **ARM** | 204.72 | - | **-** | 12 | - | NEG -$7.1M | - | 220 | 200 | +$209k | - | out (clean 26, ADX 20, RVol 0.8) |
| 24 | **CRM** | 231.81 | - | **-** | 12 | - | NEG -$5.9M | 242.82 | 240 | 220 | +$98k | - | out (clean 28, ADX 16, RVol 0.9) |
| 25 | **NFLX** | 61.86 | - | **-** | 9 | - | NEG -$24.8M | - | 63 | 60 | +$335k | - | out (clean 30, ADX 17, RVol 0.9) |
| 26 | **COIN** | 140.86 | - | **-** | 7 | - | NEG -$8.0M | - | 150 | 130 | -$84k | - | out (clean 25, ADX 24, RVol 0.8) |
| 27 | **DELL** | 413.86 | - | **-** | 4 | - | NEG -$23.8M | - | 440 | 400 | +$75k | - | out (clean 34, ADX 16, RVol 0.7) |

## Big prints this scan (141)
- **SPY** PUT 755 2026-11-09 (7DTE): 1,725 @ 3.79 = **+$654k** SELL | vol 5,430 / OI 964
- **TSLA** CALL 400 2026-11-06 (4DTE): 214 @ 17.95 = **+$384k** BUY | vol 5,198 / OI 4,780
- **SPY** PUT 765 2026-11-05 (3DTE): 407 @ 6.50 = **+$265k** SELL | vol 3,320 / OI 2,269
- **AMZN** CALL 247.5 2026-11-06 (4DTE): 322 @ 7.95 = **+$256k** SELL | vol 2,412 / OI 475
- **SPY** PUT 765 2026-11-05 (3DTE): 393 @ 6.50 = **+$255k** SELL | vol 3,320 / OI 2,269
- **AMD** PUT 505 2026-11-04 (2DTE): 84 @ 25.20 = **+$212k** SELL | vol 585 / OI 43
- **NVDA** CALL 205 2026-11-04 (2DTE): 454 @ 4.45 = **+$202k** BUY | vol 3,286 / OI 108
- **AMZN** CALL 247.5 2026-11-06 (4DTE): 197 @ 8.00 = **+$158k** SELL | vol 2,412 / OI 475
- **TSLA** CALL 415 2026-11-04 (2DTE): 200 @ 7.15 = **+$143k** BUY | vol 8,467 / OI 907
- **TSLA** CALL 400 2026-11-06 (4DTE): 79 @ 17.95 = **+$142k** BUY | vol 5,198 / OI 4,780
- **SPY** CALL 763 2026-11-06 (4DTE): 253 @ 5.45 = **+$138k** BUY | vol 2,329 / OI 907
- **QQQ** PUT 697 2026-11-02 (0DTE): 666 @ 2.07 = **+$138k** SELL | vol 36,103 / OI 0
- **QQQ** PUT 706 2026-11-02 (0DTE): 141 @ 9.44 = **+$133k** SELL | vol 755 / OI 591
- **IWM** CALL 275 2026-11-06 (4DTE): 138 @ 8.54 = **+$118k** BUY | vol 1,440 / OI 4,485
- **SPY** PUT 755 2026-11-09 (7DTE): 287 @ 3.79 = **+$109k** SELL | vol 5,430 / OI 964

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 780 2026-11-02 (0DTE): 4,267 traded vs OI 3,710
- **SPY** PUT 755 2026-11-04 (2DTE): 7,845 traded vs OI 5,864
- **SPY** PUT 765 2026-11-05 (3DTE): 3,320 traded vs OI 2,269
- **SPY** PUT 760 2026-11-11 (9DTE): 514 traded vs OI 196
- **SPY** PUT 700 2026-11-12 (10DTE): 1,275 traded vs OI 1,026
- **SPY** CALL 765 2026-11-13 (11DTE): 1,150 traded vs OI 1,101
- **SPY** PUT 690 2026-11-13 (11DTE): 3,303 traded vs OI 3,268
- **SPY** CALL 761 2026-11-20 (18DTE): 2,299 traded vs OI 1,344
- **SPY** CALL 762 2026-11-20 (18DTE): 501 traded vs OI 433
- **QQQ** PUT 692 2026-11-06 (4DTE): 607 traded vs OI 606
- **QQQ** CALL 692 2026-11-03 (1DTE): 507 traded vs OI 0
- **IWM** PUT 276 2026-11-02 (0DTE): 764 traded vs OI 713
- **IWM** PUT 270 2026-11-16 (14DTE): 3,068 traded vs OI 0
- **IWM** PUT 270 2026-11-27 (25DTE): 2,764 traded vs OI 2,701
- **NVDA** CALL 202.5 2026-11-13 (11DTE): 623 traded vs OI 18

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
