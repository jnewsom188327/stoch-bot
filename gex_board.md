# GEX + FLOW SCAN - Mon Nov 02, 11:35 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:35:08 ET, last candle SPY 11:34, QQQ 11:34 | no errors

## Flow surges NOT fired - price disagreed (5 today, last 5)
- 10:35 SPY PUTS: price +0.32 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:25 SPY PUTS: price +2.69 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:10 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 10:05 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 09:50 BABA PUTS: price +0.75 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMCI** | 32.35 | TREND (flow not with it) | **PUTS** | 28 | none: 13 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$49k | 31.43 | 35 | 33 | +$171k | - | SHORT (clean 33, ADX 31, RVol 1.0) |
| 2 | **MU** | 866.50 | - | **-** | 28 | - | NEG -$223.5M | - | 910 | 850 | +$71.5M | +$3.2M bull / +$0 bear | out (clean 30, ADX 22, RVol 2.4) |
| 3 | **AMD** | 491.90 | - | **-** | 27 | - | NEG -$91.6M | - | 540 | 500 | +$26.1M | +$1.4M bull / +$0 bear | out (clean 30, ADX 33, RVol 1.2) |
| 4 | **AMZN** | 251.71 | - | **-** | 27 | - | POS +$109.4M | 242.17 | 250 | 250 | -$24.7M | +$546k bull / +$0 bear | out (clean 33, ADX 61, RVol 0.8) |
| 5 | **SMH** | 524.26 | - | **-** | 25 | - | NEG -$336.2M | - | 532.5 | 500 | +$2.9M | +$2.0M bull / +$0 bear | out (clean 31, ADX 29, RVol 0.9) |
| 6 | **TSLA** | 411.10 | - | **-** | 23 | - | POS +$315.0M | - | 410 | 400 | -$75.2M | +$5.9M bull / +$0 bear | out (clean 30, ADX 39, RVol 0.8) |
| 7 | **BABA** | 103.36 | - | **-** | 23 | - | POS +$3.2M | 100.78 | 105 | 100 | -$1.2M | - | out (clean 33, ADX 54, RVol 1.2) |
| 8 | **SHOP** | 158.39 | - | **-** | 20 | - | NEG -$374k | - | 170 | 160 | -$425k | - | out (clean 28, ADX 22, RVol 1.4) |
| 9 | **AAPL** | 340.48 | - | **-** | 19 | - | POS +$51.2M | 336.93 | 350 | 330 | +$7.7M | +$332k bull / -$245k bear | out (clean 31, ADX 16, RVol 0.9) |
| 10 | **META** | 613.00 | - | **-** | 19 | - | NEG -$125.5M | 625.66 | 650 | 610 | +$7.2M | +$540k bull / -$317k bear | out (clean 29, ADX 28, RVol 0.7) |
| 11 | **SPY** | 760.52 | - | **-** | 18 | - | NEG -$9.5B | 775.42 | 770 | 750 | -$33.5M | +$576k bull / -$797k bear | out (clean 29, ADX 30, RVol 0.5) |
| 12 | **NVDA** | 207.15 | - | **-** | 18 | - | NEG -$208.0M | 215.17 | 210 | 200 | +$6.2M | +$700k bull / +$0 bear | out (clean 29, ADX 22, RVol 1.1) |
| 13 | **GOOGL** | 283.55 | - | **-** | 18 | - | NEG -$92.2M | - | 285 | 290 | +$1.5M | +$57k bull / +$0 bear | out (clean 35, ADX 28, RVol 0.8) |
| 14 | **ORCL** | 123.80 | - | **-** | 18 | - | NEG -$40.1M | - | 130 | 120 | -$492k | +$89k bull / -$27k bear | out (clean 32, ADX 33, RVol 0.7) |
| 15 | **QQQ** | 694.59 | - | **-** | 17 | - | NEG -$5.7B | 731.89 | 720 | 680 | +$14.1M | +$847k bull / +$0 bear | out (clean 29, ADX 25, RVol 0.7) |
| 16 | **IWM** | 282.33 | - | **-** | 17 | - | NEG -$776.0M | 286.25 | 285 | 270 | +$339k | +$937k bull / +$0 bear | out (clean 31, ADX 36, RVol 0.4) |
| 17 | **AVGO** | 331.16 | - | **-** | 15 | - | NEG -$98.2M | - | 340 | 330 | -$5.5M | - | out (clean 31, ADX 45, RVol 0.4) |
| 18 | **PLTR** | 184.84 | - | **-** | 15 | - | NEG -$11.1M | - | 200 | 180 | -$794k | +$60k bull / -$76k bear | out (clean 25, ADX 11, RVol 0.8) |
| 19 | **DELL** | 416.70 | - | **-** | 15 | - | NEG -$23.8M | - | 440 | 400 | -$237k | +$0 bull / -$72k bear | out (clean 34, ADX 14, RVol 1.0) |
| 20 | **UBER** | 67.31 | - | **-** | 15 | - | NEG -$8.2M | - | 70 | 65 | -$240k | - | out (clean 28, ADX 44, RVol 0.7) |
| 21 | **MSTR** | 135.83 | - | **-** | 14 | - | POS +$3.9M | - | 135 | 125 | +$2.4M | - | out (clean 26, ADX 36, RVol 1.4) |
| 22 | **CRM** | 231.64 | - | **-** | 12 | - | NEG -$5.4M | 241.98 | 240 | 220 | +$100k | - | out (clean 28, ADX 15, RVol 0.9) |
| 23 | **HOOD** | 86.32 | - | **-** | 10 | - | NEG -$9.0M | - | 93 | 90 | -$494k | - | out (clean 32, ADX 38, RVol 0.4) |
| 24 | **ARM** | 204.88 | - | **-** | 10 | - | NEG -$7.0M | - | 220 | 200 | +$187k | - | out (clean 26, ADX 19, RVol 0.7) |
| 25 | **MSFT** | 523.58 | - | **-** | 9 | - | POS +$345.2M | 500.77 | 540 | 500 | -$2.9M | - | out (clean 26, ADX 22, RVol 0.9) |
| 26 | **NFLX** | 62.15 | - | **-** | 8 | - | NEG -$23.2M | - | 63 | 60 | +$304k | - | out (clean 29, ADX 15, RVol 1.0) |
| 27 | **COIN** | 140.08 | - | **-** | 8 | - | NEG -$7.8M | - | 150 | 130 | -$178k | - | out (clean 25, ADX 20, RVol 1.1) |

## Big prints this scan (81)
- **SPY** PUT 760 2026-11-02 (0DTE): 2,000 @ 1.17 = **+$234k** SELL | vol 207,812 / OI 6,923
- **SPY** CALL 763 2026-11-06 (4DTE): 437 @ 4.80 = **+$210k** SELL | vol 3,531 / OI 907
- **SPY** PUT 759 2026-11-02 (0DTE): 2,000 @ 0.81 = **+$162k** BUY | vol 124,281 / OI 2,439
- **SPY** PUT 761 2026-11-03 (1DTE): 500 @ 3.16 = **+$158k** BUY | vol 12,655 / OI 628
- **SPY** CALL 732 2026-11-06 (4DTE): 50 @ 29.73 = **+$149k** MID | vol 382 / OI 2
- **SPY** PUT 760 2026-11-03 (1DTE): 500 @ 2.71 = **+$136k** BUY | vol 31,548 / OI 1,594
- **AMZN** PUT 250 2026-11-06 (4DTE): 432 @ 3.10 = **+$134k** SELL | vol 6,249 / OI 3,922
- **SPY** PUT 759 2026-11-03 (1DTE): 573 @ 2.30 = **+$132k** BUY | vol 12,003 / OI 2,770
- **SPY** CALL 758 2026-11-02 (0DTE): 375 @ 3.09 = **+$116k** MID | vol 17,963 / OI 150
- **AMD** PUT 500 2026-11-02 (0DTE): 120 @ 7.90 = **+$95k** SELL | vol 7,862 / OI 751
- **MU** CALL 860 2026-11-02 (0DTE): 84 @ 10.94 = **+$92k** BUY | vol 872 / OI 55
- **TSLA** CALL 425 2026-11-06 (4DTE): 187 @ 4.42 = **+$83k** BUY | vol 7,225 / OI 7,204
- **META** CALL 610 2026-11-02 (0DTE): 268 @ 2.87 = **+$77k** SELL | vol 1,560 / OI 108
- **TSLA** CALL 415 2026-11-06 (4DTE): 88 @ 8.59 = **+$76k** BUY | vol 5,266 / OI 2,434
- **AAPL** PUT 325 2026-11-04 (2DTE): 289 @ 2.49 = **+$72k** SELL | vol 4,802 / OI 973

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 820 2026-11-10 (8DTE): 1,607 traded vs OI 0
- **SPY** CALL 762 2026-11-06 (4DTE): 2,313 traded vs OI 2,305
- **SPY** CALL 830 2026-11-10 (8DTE): 680 traded vs OI 0
- **SPY** CALL 825 2026-11-10 (8DTE): 578 traded vs OI 0
- **SPY** CALL 779 2026-11-04 (2DTE): 1,610 traded vs OI 1,515
- **SPY** CALL 761 2026-11-13 (11DTE): 507 traded vs OI 420
- **QQQ** CALL 750 2026-11-09 (7DTE): 849 traded vs OI 423
- **QQQ** CALL 730 2026-11-30 (28DTE): 5,010 traded vs OI 1,459
- **IWM** CALL 291 2026-11-06 (4DTE): 829 traded vs OI 825
- **TSLA** PUT 382.5 2026-11-06 (4DTE): 921 traded vs OI 908
- **TSLA** CALL 425 2026-11-06 (4DTE): 7,225 traded vs OI 7,204
- **AAPL** PUT 312.5 2026-11-04 (2DTE): 576 traded vs OI 105
- **META** PUT 580 2026-11-06 (4DTE): 536 traded vs OI 485
- **META** PUT 610 2026-11-04 (2DTE): 662 traded vs OI 630
- **AMZN** PUT 255 2026-11-04 (2DTE): 583 traded vs OI 151

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
