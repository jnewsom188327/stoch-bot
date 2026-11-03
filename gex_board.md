# GEX + FLOW SCAN - Tue Nov 03, 02:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:50:08 ET, last candle SPY 14:49, QQQ 14:49 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SHOP** | 144.65 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 56 | none: 23 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$4.2M | - | 145 | 148 | -$3.9M | +$41k bull / +$0 bear | SHORT (clean 34, ADX 28, RVol 1.1) |
| 2 | **MSFT** | 521.56 | - | **-** | 28 | - | POS +$261.6M | 502.19 | 540 | 500 | -$12.7M | +$157k bull / -$40k bear | out (clean 28, ADX 41, RVol 0.7) |
| 3 | **ORCL** | 124.52 | - | **-** | 25 | - | NEG -$41.0M | - | 135 | 120 | -$9.0M | +$129k bull / +$0 bear | out (clean 35, ADX 38, RVol 0.7) |
| 4 | **META** | 620.83 | - | **-** | 20 | - | NEG -$40.7M | 626.45 | 650 | 610 | -$15.0M | +$31k bull / -$223k bear | out (clean 29, ADX 22, RVol 0.4) |
| 5 | **AMZN** | 251.45 | - | **-** | 20 | - | POS +$180.2M | - | 250 | 250 | -$3.3M | +$0 bull / -$164k bear | out (clean 33, ADX 37, RVol 0.6) |
| 6 | **SMH** | 516.81 | - | **-** | 19 | - | NEG -$305.7M | - | 532.5 | 500 | +$2.2M | +$73k bull / +$0 bear | out (clean 32, ADX 19, RVol 0.6) |
| 7 | **NFLX** | 63.06 | - | **-** | 19 | - | NEG -$7.2M | 64.26 | 63 | 60 | -$284k | +$53k bull / +$0 bear | out (clean 28, ADX 33, RVol 0.6) |
| 8 | **AVGO** | 331.65 | - | **-** | 19 | - | NEG -$72.3M | - | 340 | 340 | +$4.2M | +$705k bull / +$0 bear | out (clean 30, ADX 13, RVol 0.3) |
| 9 | **NVDA** | 206.81 | - | **-** | 18 | - | POS +$84.2M | 203.68 | 210 | 200 | +$14.8M | +$369k bull / -$45k bear | out (clean 29, ADX 22, RVol 0.5) |
| 10 | **AMD** | 486.93 | - | **-** | 17 | - | NEG -$88.9M | - | 520 | 440 | +$9.7M | +$836k bull / +$0 bear | out (clean 32, ADX 19, RVol 0.6) |
| 11 | **GOOGL** | 279.15 | - | **-** | 17 | - | NEG -$39.8M | 284.63 | 285 | 290 | +$3.0M | +$56k bull / +$0 bear | out (clean 33, ADX 21, RVol 0.3) |
| 12 | **SMCI** | 31.79 | - | **-** | 17 | - | POS +$2.0M | - | 34.5 | 30 | -$48k | +$27k bull / -$68k bear | out (clean 33, ADX 16, RVol 2.1) |
| 13 | **QQQ** | 685.21 | - | **-** | 16 | - | NEG -$5.1B | - | 700 | 680 | +$25.6M | +$119k bull / +$0 bear | out (clean 30, ADX 16, RVol 1.1) |
| 14 | **TSLA** | 398.26 | - | **-** | 16 | - | POS +$199.3M | - | 400 | 400 | +$17.6M | +$592k bull / +$0 bear | out (clean 31, ADX 18, RVol 0.3) |
| 15 | **MSTR** | 135.47 | - | **-** | 16 | - | POS +$81.1M | - | 135 | 125 | -$3.2M | +$153k bull / +$0 bear | out (clean 29, ADX 11, RVol 0.3) |
| 16 | **PLTR** | 174.51 | - | **-** | 15 | - | NEG -$25.3M | - | 165 | 180 | +$1.2M | +$67k bull / -$293k bear | out (clean 28, ADX 16, RVol 0.9) |
| 17 | **DELL** | 406.00 | - | **-** | 15 | - | NEG -$26.3M | - | 440 | 400 | +$675k | +$0 bull / -$54k bear | out (clean 32, ADX 13, RVol 0.2) |
| 18 | **HOOD** | 85.36 | - | **-** | 15 | - | NEG -$2.6M | - | 90 | 90 | -$169k | +$0 bull / -$28k bear | out (clean 30, ADX 16, RVol 0.6) |
| 19 | **SPY** | 754.74 | - | **-** | 14 | - | NEG -$9.1B | 770.15 | 770 | 750 | -$24.6M | +$1.4M bull / +$0 bear | out (clean 30, ADX 16, RVol 0.4) |
| 20 | **IWM** | 280.32 | - | **-** | 13 | - | NEG -$1.2B | 286.82 | 285 | 270 | +$418k | +$388k bull / +$0 bear | out (clean 33, ADX 15, RVol 0.3) |
| 21 | **AAPL** | 331.63 | - | **-** | 13 | - | NEG -$391.9M | 342.08 | 350 | 330 | -$7.4M | +$96k bull / -$138k bear | out (clean 30, ADX 10, RVol 0.2) |
| 22 | **MU** | 849.19 | - | **-** | 13 | - | NEG -$210.0M | - | 900 | 850 | -$13.6M | +$1.8M bull / +$0 bear | out (clean 31, ADX 9, RVol 0.2) |
| 23 | **UBER** | 66.66 | - | **-** | 12 | - | NEG -$13.4M | - | 70 | 65 | -$431k | - | out (clean 30, ADX 17, RVol 1.4) |
| 24 | **COIN** | 145.81 | - | **-** | 10 | - | POS +$21.2M | - | 148 | 150 | -$2.1M | - | out (clean 30, ADX 25, RVol 0.3) |
| 25 | **CRM** | 222.72 | - | **-** | 10 | - | NEG -$14.0M | - | 240 | 220 | -$317k | - | out (clean 29, ADX 14, RVol 0.8) |
| 26 | **ARM** | 200.88 | - | **-** | 7 | - | NEG -$6.6M | - | 220 | 200 | -$76k | - | out (clean 26, ADX 26, RVol 0.4) |
| 27 | **BABA** | 100.53 | - | **-** | 6 | - | POS +$1.6M | 99.99 | 102 | 100 | +$67k | - | out (clean 36, ADX 24, RVol 0.2) |

## Big prints this scan (42)
- **AVGO** CALL 335 2026-11-04 (1DTE): 476 @ 3.85 = **+$183k** BUY | vol 3,920 / OI 121
- **SPY** PUT 755 2026-11-10 (7DTE): 229 @ 7.55 = **+$173k** SELL | vol 2,440 / OI 2,333
- **SPY** PUT 755 2026-11-10 (7DTE): 171 @ 7.56 = **+$129k** SELL | vol 2,440 / OI 2,333
- **PLTR** CALL 180 2026-11-06 (3DTE): 462 @ 2.46 = **+$114k** SELL | vol 35,613 / OI 502
- **MU** CALL 850 2026-11-06 (3DTE): 29 @ 25.25 = **+$73k** BUY | vol 2,480 / OI 341
- **AMD** CALL 492.5 2026-11-09 (6DTE): 35 @ 20.90 = **+$73k** BUY | vol 167 / OI 1
- **META** CALL 635 2026-11-06 (3DTE): 111 @ 6.05 = **+$67k** MID | vol 1,809 / OI 1,669
- **AMD** PUT 470 2026-11-04 (1DTE): 50 @ 11.53 = **+$58k** MID | vol 2,037 / OI 310
- **AMD** PUT 487.5 2026-11-06 (3DTE): 25 @ 21.95 = **+$55k** SELL | vol 507 / OI 265
- **AMD** PUT 467.5 2026-11-04 (1DTE): 50 @ 10.63 = **+$53k** SELL | vol 352 / OI 55
- **MU** PUT 850 2026-11-04 (1DTE): 32 @ 16.35 = **+$52k** SELL | vol 16,005 / OI 414
- **AMD** PUT 485 2026-11-06 (3DTE): 25 @ 20.70 = **+$52k** MID | vol 1,324 / OI 432
- **MU** CALL 850 2026-11-06 (3DTE): 20 @ 25.25 = **+$50k** BUY | vol 2,480 / OI 341
- **MU** CALL 850 2026-11-06 (3DTE): 20 @ 25.25 = **+$50k** BUY | vol 2,480 / OI 341
- **MU** CALL 850 2026-11-06 (3DTE): 20 @ 25.25 = **+$50k** BUY | vol 2,480 / OI 341

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 695 2026-11-06 (3DTE): 1,890 traded vs OI 1,777
- **SPY** PUT 755 2026-11-10 (7DTE): 2,440 traded vs OI 2,333
- **SPY** PUT 725 2026-11-17 (14DTE): 568 traded vs OI 0
- **SPY** CALL 772 2026-11-27 (24DTE): 847 traded vs OI 818
- **QQQ** CALL 712 2026-11-04 (1DTE): 1,091 traded vs OI 1,033
- **QQQ** PUT 625 2026-11-04 (1DTE): 1,407 traded vs OI 1,395
- **PLTR** PUT 172.5 2026-11-13 (10DTE): 512 traded vs OI 241
- **SMCI** CALL 31 2026-11-06 (3DTE): 783 traded vs OI 765
- **MU** PUT 840 2026-11-06 (3DTE): 1,156 traded vs OI 1,144
- **HOOD** PUT 79 2026-11-06 (3DTE): 1,503 traded vs OI 1,500
- **BABA** CALL 105 2026-11-13 (10DTE): 1,360 traded vs OI 1,278

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
