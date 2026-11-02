# GEX + FLOW SCAN - Mon Nov 02, 10:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:20:08 ET, last candle SPY 10:19, QQQ 10:19 | no errors

## Flow surges NOT fired - price disagreed (3 today, last 5)
- 10:10 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 10:05 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 09:50 BABA PUTS: price +0.75 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BABA** | 103.65 | TREND (flow not with it) | **CALLS** | 59 | 11/06 108C @ 0.76 (delta 0.23) = est +40% at 105 | POS +$3.1M | 100.99 | 105 | 100 | -$1.2M | - | LONG (clean 33, ADX 55, RVol 3.0) |
| 2 | **SPY** | 762.38 | FLOW SURGE | **PUTS** | 44 | 11/02 759P @ 0.57 (delta 0.22) = est +86% at 760 | NEG -$8.5B | 774.61 | 770 | 750 | -$81.1M | +$264k bull / -$2.5M bear | out (clean 29, ADX 44, RVol 1.0) |
| 3 | **GOOGL** | 285.86 | TREND (flow not with it) | **CALLS** | 42 | 11/02 287.5C @ 0.64 (delta 0.31) = est +314% at 290 | NEG -$66.9M | - | 285 | 290 | -$2.0M | +$362k bull / -$154k bear | LONG (clean 34, ADX 51, RVol 1.1) |
| 4 | **AVGO** | 331.32 | FLOW SURGE | **PUTS** | 41 | none: 104 puts 0-7DTE > 6 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +7% at the target (needs +20%) (42 contracts' greeks worked out here) | NEG -$99.8M | - | 340 | 330 | -$5.1M | +$0 bull / -$353k bear | out (clean 31, ADX 47, RVol 0.7) |
| 5 | **AMZN** | 252.19 | - | **-** | 29 | - | POS +$109.3M | 242.8 | 250 | 250 | -$16.4M | +$0 bull / -$819k bear | out (clean 32, ADX 55, RVol 1.1) |
| 6 | **HOOD** | 86.36 | - | **-** | 28 | - | NEG -$9.2M | - | 93 | 90 | -$1.0M | +$0 bull / -$27k bear | out (clean 32, ADX 59, RVol 0.4) |
| 7 | **SMH** | 529.21 | - | **-** | 27 | - | NEG -$298.1M | - | 532.5 | 500 | +$1.7M | +$0 bull / -$119k bear | out (clean 32, ADX 40, RVol 0.9) |
| 8 | **MSFT** | 526.31 | - | **-** | 27 | - | POS +$377.4M | 498.48 | 540 | 530 | -$4.9M | +$528k bull / -$25k bear | out (clean 26, ADX 23, RVol 1.5) |
| 9 | **MU** | 880.15 | - | **-** | 26 | - | NEG -$214.9M | - | 910 | 900 | +$22.2M | +$1.3M bull / -$4.1M bear | out (clean 30, ADX 27, RVol 1.8) |
| 10 | **IWM** | 282.37 | - | **-** | 25 | - | NEG -$796.2M | 286.45 | 285 | 270 | -$2.1M | +$0 bull / -$252k bear | out (clean 31, ADX 44, RVol 2.0) |
| 11 | **MSTR** | 135.38 | - | **-** | 25 | - | POS +$3.7M | - | 135 | 125 | +$1.2M | +$0 bull / -$199k bear | out (clean 27, ADX 41, RVol 1.5) |
| 12 | **UBER** | 67.23 | - | **-** | 25 | - | NEG -$8.1M | - | 70 | 65 | -$321k | - | out (clean 27, ADX 46, RVol 1.3) |
| 13 | **QQQ** | 697.01 | - | **-** | 24 | - | NEG -$5.7B | 731.79 | 720 | 700 | -$27.5M | +$0 bull / -$302k bear | out (clean 30, ADX 38, RVol 1.5) |
| 14 | **AAPL** | 341.20 | - | **-** | 24 | - | POS +$71.5M | 336.45 | 350 | 330 | +$4.1M | +$754k bull / -$1.0M bear | out (clean 32, ADX 30, RVol 1.7) |
| 15 | **NFLX** | 62.03 | - | **-** | 24 | - | NEG -$24.1M | - | 63 | 60 | +$295k | +$0 bull / -$57k bear | out (clean 30, ADX 27, RVol 1.7) |
| 16 | **PLTR** | 185.97 | - | **-** | 24 | - | NEG -$10.6M | - | 200 | 180 | -$1.7M | +$0 bull / -$43k bear | out (clean 26, ADX 13, RVol 3.1) |
| 17 | **ORCL** | 123.21 | - | **-** | 24 | - | NEG -$39.0M | - | 130 | 120 | -$819k | +$65k bull / -$783k bear | out (clean 33, ADX 41, RVol 2.0) |
| 18 | **META** | 618.68 | - | **-** | 23 | - | NEG -$91.0M | 627.77 | 650 | 600 | -$6.9M | +$2.1M bull / -$383k bear | out (clean 29, ADX 34, RVol 0.7) |
| 19 | **SHOP** | 158.42 | - | **-** | 22 | - | NEG -$466k | - | 170 | 160 | -$105k | - | out (clean 28, ADX 39, RVol 2.9) |
| 20 | **NVDA** | 208.98 | - | **-** | 20 | - | NEG -$171.4M | 215.04 | 210 | 210 | -$578k | +$0 bull / -$716k bear | out (clean 30, ADX 36, RVol 1.4) |
| 21 | **TSLA** | 408.20 | - | **-** | 19 | - | POS +$281.8M | - | 410 | 400 | -$8.8M | +$0 bull / -$4.6M bear | out (clean 29, ADX 29, RVol 1.3) |
| 22 | **AMD** | 505.85 | - | **-** | 19 | - | NEG -$95.3M | - | 550 | 500 | +$1.2M | +$79k bull / -$3.6M bear | out (clean 30, ADX 35, RVol 0.9) |
| 23 | **CRM** | 232.09 | - | **-** | 18 | - | NEG -$4.7M | 241.58 | 240 | 220 | +$81k | - | out (clean 28, ADX 22, RVol 1.9) |
| 24 | **DELL** | 415.38 | - | **-** | 17 | - | NEG -$24.1M | - | 440 | 400 | +$100k | +$0 bull / -$531k bear | out (clean 34, ADX 23, RVol 1.0) |
| 25 | **COIN** | 141.81 | - | **-** | 16 | - | NEG -$9.0M | - | 150 | 130 | -$165k | - | out (clean 26, ADX 36, RVol 2.0) |
| 26 | **ARM** | 203.09 | - | **-** | 16 | - | NEG -$6.9M | - | 220 | 200 | +$273k | - | out (clean 26, ADX 20, RVol 0.6) |
| 27 | **SMCI** | 33.25 | - | **-** | 12 | - | POS +$630k | - | 35 | 33 | +$25k | - | out (clean 32, ADX 46, RVol 1.4) |

## Big prints this scan (132)
- **SPY** PUT 750 2026-11-04 (2DTE): 5,000 @ 1.40 = **+$700k** BUY | vol 5,861 / OI 1,303
- **META** PUT 645 2026-11-09 (7DTE): 174 @ 30.91 = **+$538k** SELL | vol 221 / OI 362
- **META** PUT 645 2026-11-06 (4DTE): 174 @ 29.88 = **+$520k** SELL | vol 224 / OI 588
- **SPY** PUT 761 2026-11-06 (4DTE): 469 @ 6.10 = **+$286k** BUY | vol 1,393 / OI 807
- **META** PUT 640 2026-11-09 (7DTE): 83 @ 26.15 = **+$217k** SELL | vol 183 / OI 822
- **MU** CALL 920 2026-11-06 (4DTE): 208 @ 10.40 = **+$216k** SELL | vol 1,596 / OI 205
- **META** PUT 640 2026-11-06 (4DTE): 83 @ 24.97 = **+$207k** SELL | vol 192 / OI 1,804
- **AMZN** CALL 250 2026-11-02 (0DTE): 929 @ 1.60 = **+$149k** SELL | vol 46,249 / OI 1,035
- **MU** CALL 920 2026-11-06 (4DTE): 138 @ 10.40 = **+$144k** SELL | vol 1,596 / OI 205
- **MU** CALL 920 2026-11-06 (4DTE): 130 @ 10.40 = **+$135k** SELL | vol 1,596 / OI 205
- **MU** PUT 870 2026-11-04 (2DTE): 68 @ 18.95 = **+$129k** BUY | vol 606 / OI 274
- **SPY** PUT 765 2026-11-06 (4DTE): 159 @ 8.00 = **+$127k** BUY | vol 899 / OI 7,871
- **MU** CALL 920 2026-11-06 (4DTE): 120 @ 10.40 = **+$125k** SELL | vol 1,596 / OI 205
- **TSLA** CALL 400 2026-11-04 (2DTE): 129 @ 9.45 = **+$122k** SELL | vol 2,903 / OI 612
- **META** PUT 640 2026-11-09 (7DTE): 45 @ 26.38 = **+$119k** SELL | vol 183 / OI 822

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 761 2026-11-06 (4DTE): 1,393 traded vs OI 807
- **SPY** CALL 780 2026-11-09 (7DTE): 517 traded vs OI 336
- **SPY** CALL 771 2026-11-04 (2DTE): 2,708 traded vs OI 2,669
- **SPY** CALL 765 2026-11-09 (7DTE): 1,302 traded vs OI 1,141
- **SPY** PUT 762 2026-11-03 (1DTE): 548 traded vs OI 524
- **SPY** PUT 759 2026-11-04 (2DTE): 1,357 traded vs OI 1,289
- **SPY** CALL 765 2026-11-10 (8DTE): 626 traded vs OI 262
- **SPY** CALL 759 2026-11-06 (4DTE): 504 traded vs OI 240
- **SPY** CALL 769 2026-11-04 (2DTE): 654 traded vs OI 642
- **SPY** CALL 770 2026-11-11 (9DTE): 533 traded vs OI 261
- **QQQ** PUT 658 2026-11-02 (0DTE): 653 traded vs OI 0
- **QQQ** PUT 680 2026-11-04 (2DTE): 1,613 traded vs OI 670
- **QQQ** CALL 690 2026-11-03 (1DTE): 511 traded vs OI 127
- **QQQ** PUT 681 2026-11-03 (1DTE): 541 traded vs OI 0
- **QQQ** PUT 660 2026-11-02 (0DTE): 1,690 traded vs OI 1,376

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
