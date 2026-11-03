# GEX + FLOW SCAN - Tue Nov 03, 03:05 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:05:08 ET, last candle SPY 15:04, QQQ 15:04 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SHOP** | 144.40 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 60 | none: 24 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$4.3M | - | 145 | 148 | -$3.8M | - | SHORT (clean 34, ADX 33, RVol 1.4) |
| 2 | **MSFT** | 522.78 | - | **-** | 29 | - | POS +$285.6M | 501.24 | 540 | 500 | -$13.1M | +$0 bull / -$57k bear | out (clean 28, ADX 42, RVol 1.2) |
| 3 | **ORCL** | 124.59 | - | **-** | 25 | - | NEG -$41.2M | - | 135 | 125 | -$8.7M | +$94k bull / +$0 bear | out (clean 35, ADX 42, RVol 0.6) |
| 4 | **MSTR** | 134.88 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 23 | none: 27 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$81.1M | - | 135 | 125 | -$3.2M | - | out (clean 29, ADX 15, RVol 0.2) |
| 5 | **SMH** | 516.09 | - | **-** | 21 | - | NEG -$302.0M | - | 532.5 | 500 | +$2.9M | +$570k bull / +$0 bear | out (clean 32, ADX 24, RVol 0.8) |
| 6 | **META** | 619.50 | - | **-** | 21 | - | NEG -$44.1M | 625.62 | 650 | 610 | -$14.4M | +$31k bull / +$0 bear | out (clean 29, ADX 26, RVol 0.4) |
| 7 | **AMZN** | 251.33 | - | **-** | 20 | - | POS +$180.9M | - | 250 | 250 | -$3.5M | +$170k bull / +$0 bear | out (clean 33, ADX 35, RVol 0.6) |
| 8 | **COIN** | 145.24 | - | **-** | 20 | - | POS +$21.8M | - | 148 | 150 | -$1.9M | +$42k bull / +$0 bear | out (clean 30, ADX 26, RVol 0.3) |
| 9 | **NVDA** | 206.69 | - | **-** | 19 | - | POS +$75.7M | 203.86 | 210 | 200 | +$15.6M | +$283k bull / +$0 bear | out (clean 29, ADX 26, RVol 0.5) |
| 10 | **AMD** | 486.75 | - | **-** | 18 | - | NEG -$88.8M | - | 520 | 440 | +$10.6M | +$339k bull / -$109k bear | out (clean 32, ADX 24, RVol 0.6) |
| 11 | **ARM** | 200.90 | - | **-** | 18 | - | NEG -$6.5M | - | 220 | 200 | -$130k | +$0 bull / -$58k bear | out (clean 26, ADX 32, RVol 0.4) |
| 12 | **QQQ** | 684.40 | - | **-** | 17 | - | NEG -$5.3B | - | 700 | 680 | +$39.0M | +$616k bull / +$0 bear | out (clean 30, ADX 21, RVol 1.1) |
| 13 | **TSLA** | 398.11 | - | **-** | 16 | - | POS +$199.5M | - | 400 | 400 | +$18.4M | +$209k bull / +$0 bear | out (clean 31, ADX 18, RVol 0.3) |
| 14 | **SPY** | 753.92 | - | **-** | 15 | - | NEG -$9.5B | 769.88 | 770 | 750 | -$9.4M | +$617k bull / +$0 bear | out (clean 30, ADX 21, RVol 0.6) |
| 15 | **IWM** | 280.06 | - | **-** | 15 | - | NEG -$1.2B | 286.92 | 285 | 270 | +$1.2M | +$50k bull / +$0 bear | out (clean 33, ADX 19, RVol 0.6) |
| 16 | **AAPL** | 329.84 | - | **-** | 15 | - | NEG -$426.2M | 342.13 | 350 | 330 | -$6.7M | +$26k bull / +$0 bear | out (clean 30, ADX 16, RVol 0.6) |
| 17 | **PLTR** | 175.50 | - | **-** | 15 | - | NEG -$25.0M | - | 165 | 180 | +$93k | +$0 bull / -$284k bear | out (clean 27, ADX 16, RVol 0.9) |
| 18 | **DELL** | 406.50 | - | **-** | 15 | - | NEG -$26.0M | - | 440 | 400 | +$607k | +$0 bull / -$49k bear | out (clean 32, ADX 16, RVol 0.2) |
| 19 | **HOOD** | 85.22 | - | **-** | 14 | - | NEG -$2.6M | - | 90 | 90 | -$22k | +$60k bull / +$0 bear | out (clean 30, ADX 16, RVol 0.7) |
| 20 | **MU** | 848.85 | - | **-** | 13 | - | NEG -$209.4M | - | 900 | 850 | -$12.4M | +$1.5M bull / +$0 bear | out (clean 31, ADX 11, RVol 0.2) |
| 21 | **UBER** | 66.71 | - | **-** | 11 | - | NEG -$8.6M | - | 70 | 65 | -$414k | - | out (clean 30, ADX 22, RVol 1.1) |
| 22 | **AVGO** | 331.56 | - | **-** | 10 | - | NEG -$72.0M | - | 340 | 340 | +$4.6M | - | out (clean 31, ADX 17, RVol 0.3) |
| 23 | **CRM** | 222.64 | - | **-** | 10 | - | NEG -$14.4M | - | 240 | 220 | -$323k | - | out (clean 29, ADX 12, RVol 0.9) |
| 24 | **GOOGL** | 278.37 | - | **-** | 8 | - | NEG -$44.3M | 284.65 | 285 | 290 | +$3.2M | - | out (clean 34, ADX 25, RVol 0.3) |
| 25 | **NFLX** | 62.85 | - | **-** | 7 | - | NEG -$9.2M | 64.25 | 63 | 60 | -$162k | - | out (clean 28, ADX 28, RVol 0.6) |
| 26 | **SMCI** | 31.77 | - | **-** | 7 | - | POS +$2.1M | - | 34.5 | 30 | +$93k | - | out (clean 33, ADX 14, RVol 2.1) |
| 27 | **BABA** | 100.33 | - | **-** | 6 | - | POS +$772k | 100.05 | 102 | 100 | +$88k | - | out (clean 36, ADX 22, RVol 0.3) |

## Big prints this scan (25)
- **AMD** PUT 490 2026-11-04 (1DTE): 217 @ 20.27 = **+$440k** MID | vol 2,343 / OI 134
- **SPY** PUT 760 2026-11-05 (2DTE): 255 @ 7.93 = **+$202k** SELL | vol 9,510 / OI 2,551
- **SPY** PUT 757 2026-11-03 (0DTE): 431 @ 2.40 = **+$103k** SELL | vol 113,130 / OI 971
- **AMZN** PUT 247.5 2026-11-06 (3DTE): 343 @ 2.33 = **+$80k** SELL | vol 2,782 / OI 558
- **PLTR** PUT 172.5 2026-11-06 (3DTE): 183 @ 3.80 = **+$70k** BUY | vol 5,450 / OI 1,049
- **NVDA** CALL 205 2026-11-04 (1DTE): 157 @ 3.85 = **+$60k** BUY | vol 6,710 / OI 2,680
- **ARM** CALL 192.5 2026-11-06 (3DTE): 36 @ 16.05 = **+$58k** SELL | vol 51 / OI 23
- **DELL** CALL 392.5 2026-11-06 (3DTE): 21 @ 23.35 = **+$49k** SELL | vol 79 / OI 0
- **MU** PUT 850 2026-11-04 (1DTE): 30 @ 16.19 = **+$49k** SELL | vol 16,806 / OI 414
- **MU** PUT 850 2026-11-06 (3DTE): 19 @ 24.60 = **+$47k** SELL | vol 4,099 / OI 1,813
- **AMD** PUT 487.5 2026-11-06 (3DTE): 20 @ 22.02 = **+$44k** BUY | vol 542 / OI 265
- **COIN** CALL 148 2026-11-06 (3DTE): 100 @ 4.25 = **+$42k** BUY | vol 901 / OI 8,235
- **MU** PUT 850 2026-11-04 (1DTE): 24 @ 16.90 = **+$41k** SELL | vol 16,806 / OI 414
- **AMD** CALL 505 2026-11-04 (1DTE): 35 @ 11.10 = **+$39k** BUY | vol 574 / OI 118
- **MU** PUT 850 2026-11-04 (1DTE): 23 @ 16.15 = **+$37k** SELL | vol 16,806 / OI 414

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 770 2026-11-06 (3DTE): 13,750 traded vs OI 13,665
- **SPY** PUT 710 2026-11-17 (14DTE): 534 traded vs OI 0
- **QQQ** CALL 675 2026-11-03 (0DTE): 500 traded vs OI 18
- **QQQ** PUT 640 2026-11-05 (2DTE): 500 traded vs OI 0
- **QQQ** PUT 676 2026-11-05 (2DTE): 501 traded vs OI 0
- **QQQ** PUT 679 2026-11-06 (3DTE): 552 traded vs OI 528
- **IWM** PUT 277 2026-11-05 (2DTE): 771 traded vs OI 680
- **SMH** CALL 550 2026-11-20 (17DTE): 1,914 traded vs OI 1,887
- **NVDA** CALL 207.5 2026-11-11 (8DTE): 518 traded vs OI 152
- **AMD** CALL 505 2026-11-04 (1DTE): 574 traded vs OI 118
- **META** CALL 630 2026-11-13 (10DTE): 506 traded vs OI 323
- **MSFT** CALL 575 2026-11-06 (3DTE): 659 traded vs OI 0
- **MSTR** PUT 135 2026-11-06 (3DTE): 2,022 traded vs OI 1,986

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
