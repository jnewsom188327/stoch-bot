# GEX + FLOW SCAN - Mon Nov 02, 11:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:00:08 ET, last candle SPY 10:59, QQQ 10:59 | no errors

## Flow surges NOT fired - price disagreed (5 today, last 5)
- 10:35 SPY PUTS: price +0.32 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:25 SPY PUTS: price +2.69 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:10 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 10:05 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 09:50 BABA PUTS: price +0.75 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BABA** | 103.58 | - | **-** | 34 | - | POS +$2.7M | 101.2 | 105 | 100 | -$1.2M | +$34k bull / +$0 bear | out (clean 33, ADX 62, RVol 1.1) |
| 2 | **AMZN** | 252.98 | - | **-** | 30 | - | POS +$125.5M | 242.14 | 265 | 250 | -$29.0M | +$1.2M bull / -$201k bear | out (clean 33, ADX 68, RVol 0.9) |
| 3 | **TSLA** | 413.04 | - | **-** | 28 | - | POS +$312.1M | - | 410 | 400 | -$104.9M | +$391k bull / -$8.4M bear | out (clean 29, ADX 39, RVol 1.7) |
| 4 | **UBER** | 67.19 | - | **-** | 28 | - | NEG -$8.1M | - | 70 | 65 | -$289k | +$33k bull / +$0 bear | out (clean 28, ADX 54, RVol 0.8) |
| 5 | **AVGO** | 331.57 | - | **-** | 27 | - | NEG -$98.5M | - | 340 | 330 | -$6.0M | +$387k bull / +$0 bear | out (clean 32, ADX 54, RVol 0.6) |
| 6 | **MSTR** | 134.51 | - | **-** | 26 | - | POS +$3.6M | - | 135 | 125 | +$2.6M | +$183k bull / -$117k bear | out (clean 27, ADX 42, RVol 1.1) |
| 7 | **SPY** | 760.98 | - | **-** | 25 | - | NEG -$9.2B | 775.4 | 800 | 750 | -$92.7M | +$2.8M bull / -$476k bear | out (clean 30, ADX 45, RVol 0.9) |
| 8 | **MU** | 873.06 | - | **-** | 25 | - | NEG -$216.7M | - | 910 | 900 | +$42.1M | +$7.2M bull / -$25k bear | out (clean 30, ADX 24, RVol 1.6) |
| 9 | **AMD** | 494.65 | - | **-** | 23 | - | NEG -$91.9M | - | 540 | 500 | +$10.5M | +$2.3M bull / +$0 bear | out (clean 30, ADX 30, RVol 1.3) |
| 10 | **MSFT** | 525.50 | - | **-** | 23 | - | POS +$371.4M | 501.13 | 540 | 530 | -$4.5M | +$271k bull / -$295k bear | out (clean 26, ADX 27, RVol 1.0) |
| 11 | **IWM** | 282.11 | - | **-** | 21 | - | NEG -$824.4M | 286.28 | 285 | 270 | -$2.4M | +$169k bull / -$65k bear | out (clean 31, ADX 47, RVol 0.5) |
| 12 | **NVDA** | 207.25 | - | **-** | 21 | - | NEG -$197.0M | 215.3 | 210 | 200 | +$6.3M | +$1.6M bull / +$0 bear | out (clean 30, ADX 32, RVol 1.3) |
| 13 | **GOOGL** | 284.06 | - | **-** | 20 | - | NEG -$80.2M | - | 285 | 290 | +$328k | +$37k bull / +$0 bear | out (clean 34, ADX 46, RVol 0.6) |
| 14 | **ORCL** | 123.06 | - | **-** | 20 | - | NEG -$39.8M | - | 130 | 120 | -$1.0M | +$190k bull / +$0 bear | out (clean 32, ADX 36, RVol 0.8) |
| 15 | **QQQ** | 695.39 | - | **-** | 19 | - | NEG -$5.6B | 731.34 | 720 | 680 | -$23.4M | +$3.1M bull / +$0 bear | out (clean 30, ADX 39, RVol 0.5) |
| 16 | **AAPL** | 341.03 | - | **-** | 19 | - | POS +$74.2M | 336.18 | 350 | 330 | +$4.5M | +$308k bull / -$779k bear | out (clean 32, ADX 22, RVol 1.1) |
| 17 | **PLTR** | 184.81 | - | **-** | 19 | - | NEG -$11.1M | - | 200 | 180 | -$1.8M | +$41k bull / +$0 bear | out (clean 25, ADX 14, RVol 1.0) |
| 18 | **META** | 614.69 | - | **-** | 16 | - | NEG -$121.0M | 626.56 | 650 | 600 | -$708k | +$341k bull / -$482k bear | out (clean 29, ADX 28, RVol 0.5) |
| 19 | **SHOP** | 159.48 | - | **-** | 16 | - | NEG -$236k | - | 175 | 175 | -$76k | - | out (clean 28, ADX 30, RVol 2.6) |
| 20 | **SMH** | 526.33 | - | **-** | 15 | - | NEG -$330.1M | - | 532.5 | 500 | +$2.0M | - | out (clean 32, ADX 41, RVol 0.7) |
| 21 | **DELL** | 415.20 | - | **-** | 15 | - | NEG -$24.2M | - | 440 | 400 | -$108k | +$37k bull / +$0 bear | out (clean 34, ADX 16, RVol 0.7) |
| 22 | **HOOD** | 86.15 | - | **-** | 13 | - | NEG -$9.0M | - | 93 | 90 | -$752k | - | out (clean 32, ADX 54, RVol 0.5) |
| 23 | **ARM** | 203.64 | - | **-** | 13 | - | NEG -$7.1M | - | 220 | 200 | +$244k | - | out (clean 26, ADX 20, RVol 0.9) |
| 24 | **CRM** | 231.50 | - | **-** | 12 | - | NEG -$4.9M | 241.4 | 240 | 220 | +$98k | - | out (clean 28, ADX 17, RVol 0.8) |
| 25 | **COIN** | 139.95 | - | **-** | 10 | - | NEG -$7.9M | - | 150 | 130 | -$155k | - | out (clean 25, ADX 28, RVol 0.8) |
| 26 | **SMCI** | 32.53 | - | **-** | 10 | - | POS +$12k | 32.3 | 35 | 33 | +$11k | - | out (clean 33, ADX 38, RVol 1.4) |
| 27 | **NFLX** | 61.92 | - | **-** | 9 | - | NEG -$24.9M | - | 63 | 60 | +$298k | - | out (clean 30, ADX 19, RVol 0.9) |

## Big prints this scan (165)
- **QQQ** PUT 695 2026-11-06 (4DTE): 1,500 @ 7.78 = **+$1.2M** SELL | vol 2,936 / OI 12,025
- **MU** CALL 885 2026-11-06 (4DTE): 103 @ 24.30 = **+$250k** BUY | vol 1,140 / OI 237
- **AMD** PUT 500 2026-11-06 (4DTE): 114 @ 21.53 = **+$245k** SELL | vol 907 / OI 1,884
- **MU** CALL 870 2026-11-06 (4DTE): 67 @ 32.20 = **+$216k** BUY | vol 484 / OI 109
- **AMD** PUT 500 2026-11-04 (2DTE): 114 @ 18.88 = **+$215k** SELL | vol 1,090 / OI 212
- **MU** CALL 870 2026-11-06 (4DTE): 63 @ 32.20 = **+$203k** BUY | vol 484 / OI 109
- **SPY** PUT 765 2026-11-06 (4DTE): 304 @ 6.50 = **+$198k** SELL | vol 1,658 / OI 7,871
- **QQQ** PUT 706 2026-11-02 (0DTE): 200 @ 8.54 = **+$171k** SELL | vol 520 / OI 591
- **IWM** CALL 275 2026-11-06 (4DTE): 195 @ 8.69 = **+$169k** BUY | vol 1,242 / OI 4,485
- **TSLA** PUT 412.5 2026-11-02 (0DTE): 450 @ 3.00 = **+$135k** BUY | vol 4,889 / OI 47
- **TSLA** CALL 400 2026-11-06 (4DTE): 75 @ 17.25 = **+$129k** SELL | vol 4,534 / OI 4,780
- **AMZN** PUT 250 2026-11-06 (4DTE): 428 @ 2.80 = **+$120k** SELL | vol 2,890 / OI 3,922
- **MU** CALL 885 2026-11-06 (4DTE): 46 @ 24.30 = **+$112k** BUY | vol 1,140 / OI 237
- **SPY** CALL 765 2026-11-09 (7DTE): 200 @ 5.46 = **+$109k** BUY | vol 2,996 / OI 1,141
- **TSLA** PUT 420 2026-11-02 (0DTE): 120 @ 9.00 = **+$108k** BUY | vol 858 / OI 181

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 765 2026-11-02 (0DTE): 6,352 traded vs OI 6,330
- **SPY** PUT 745 2026-11-05 (3DTE): 797 traded vs OI 794
- **SPY** PUT 760 2026-11-10 (8DTE): 506 traded vs OI 479
- **SPY** CALL 793 2026-11-04 (2DTE): 606 traded vs OI 378
- **SPY** PUT 760 2026-11-04 (2DTE): 2,558 traded vs OI 2,520
- **SPY** CALL 765 2026-11-06 (4DTE): 2,647 traded vs OI 2,617
- **SPY** CALL 795 2026-11-09 (7DTE): 715 traded vs OI 659
- **SPY** CALL 780 2026-11-11 (9DTE): 584 traded vs OI 302
- **SPY** PUT 700 2026-11-11 (9DTE): 964 traded vs OI 58
- **QQQ** CALL 716 2026-11-04 (2DTE): 507 traded vs OI 239
- **QQQ** CALL 686 2026-11-02 (0DTE): 516 traded vs OI 0
- **QQQ** CALL 713 2026-11-06 (4DTE): 732 traded vs OI 689
- **QQQ** CALL 718 2026-11-04 (2DTE): 666 traded vs OI 199
- **QQQ** CALL 700 2026-11-20 (18DTE): 4,141 traded vs OI 3,764
- **IWM** PUT 282.5 2026-11-06 (4DTE): 571 traded vs OI 496

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
