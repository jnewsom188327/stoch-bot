# GEX + FLOW SCAN - Tue Nov 03, 03:35 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SHOP** | 143.62 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 62 | none: 24 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$4.4M | - | 145 | 148 | -$3.8M | - | SHORT (clean 34, ADX 39, RVol 1.5) |
| 2 | **MSFT** | 522.14 | - | **-** | 28 | - | POS +$334.1M | 499.77 | 540 | 500 | -$12.9M | +$316k bull / +$0 bear | out (clean 28, ADX 44, RVol 1.1) |
| 3 | **MSTR** | 135.33 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 24 | none: 27 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$90.1M | - | 135 | 125 | -$3.4M | - | out (clean 29, ADX 15, RVol 0.4) |
| 4 | **ARM** | 202.72 | - | **-** | 24 | - | NEG -$6.5M | - | 220 | 200 | -$867k | +$0 bull / -$686k bear | out (clean 26, ADX 28, RVol 0.5) |
| 5 | **UBER** | 66.89 | - | **-** | 23 | - | NEG -$8.1M | - | 70 | 65 | -$499k | +$0 bull / -$34k bear | out (clean 30, ADX 19, RVol 1.8) |
| 6 | **META** | 619.22 | - | **-** | 21 | - | NEG -$43.3M | 624.63 | 650 | 610 | -$14.3M | +$252k bull / -$255k bear | out (clean 29, ADX 31, RVol 0.4) |
| 7 | **NVDA** | 206.79 | - | **-** | 19 | - | POS +$74.9M | 204.09 | 210 | 200 | +$16.4M | +$0 bull / -$219k bear | out (clean 30, ADX 26, RVol 0.6) |
| 8 | **AVGO** | 332.18 | - | **-** | 19 | - | NEG -$65.7M | - | 340 | 340 | +$4.3M | +$0 bull / -$76k bear | out (clean 30, ADX 14, RVol 0.5) |
| 9 | **SMH** | 518.32 | - | **-** | 18 | - | NEG -$287.5M | - | 532.5 | 500 | +$2.4M | +$0 bull / -$35k bear | out (clean 32, ADX 18, RVol 0.6) |
| 10 | **GOOGL** | 279.04 | - | **-** | 18 | - | NEG -$41.6M | 284.81 | 285 | 290 | +$2.7M | +$0 bull / -$216k bear | out (clean 33, ADX 25, RVol 0.4) |
| 11 | **AMD** | 488.52 | - | **-** | 17 | - | NEG -$85.8M | - | 520 | 440 | +$7.5M | +$190k bull / -$657k bear | out (clean 32, ADX 24, RVol 0.8) |
| 12 | **QQQ** | 685.34 | - | **-** | 16 | - | NEG -$5.1B | - | 700 | 680 | +$32.1M | +$0 bull / -$3.0M bear | out (clean 29, ADX 17, RVol 1.1) |
| 13 | **AAPL** | 330.93 | - | **-** | 16 | - | NEG -$403.0M | 341.42 | 350 | 330 | -$9.3M | +$30k bull / -$27k bear | out (clean 30, ADX 16, RVol 0.8) |
| 14 | **SMCI** | 31.66 | - | **-** | 16 | - | POS +$2.0M | - | 34.5 | 30 | +$349k | +$102k bull / +$0 bear | out (clean 33, ADX 12, RVol 1.5) |
| 15 | **TSLA** | 397.41 | - | **-** | 15 | - | POS +$182.3M | - | 400 | 400 | +$19.0M | +$285k bull / +$0 bear | out (clean 31, ADX 14, RVol 0.3) |
| 16 | **PLTR** | 175.16 | - | **-** | 14 | - | NEG -$17.3M | - | 190 | 180 | +$416k | +$73k bull / -$112k bear | out (clean 27, ADX 15, RVol 0.7) |
| 17 | **ORCL** | 125.46 | - | **-** | 14 | - | NEG -$39.7M | - | 135 | 125 | -$9.3M | - | out (clean 35, ADX 34, RVol 0.9) |
| 18 | **MU** | 850.38 | - | **-** | 13 | - | NEG -$221.7M | - | 900 | 850 | -$13.5M | +$514k bull / -$1.3M bear | out (clean 31, ADX 10, RVol 0.4) |
| 19 | **AMZN** | 252.14 | - | **-** | 11 | - | POS +$216.1M | - | 250 | 250 | -$4.3M | - | out (clean 33, ADX 36, RVol 1.1) |
| 20 | **COIN** | 145.10 | - | **-** | 9 | - | POS +$20.7M | - | 148 | 140 | -$1.9M | - | out (clean 30, ADX 23, RVol 0.4) |
| 21 | **CRM** | 222.24 | - | **-** | 9 | - | NEG -$14.0M | - | 240 | 220 | -$309k | - | out (clean 29, ADX 12, RVol 0.6) |
| 22 | **NFLX** | 63.02 | - | **-** | 7 | - | NEG -$6.5M | 63.87 | 63 | 60 | -$179k | - | out (clean 28, ADX 22, RVol 0.8) |
| 23 | **IWM** | 280.06 | - | **-** | 6 | - | NEG -$1.2B | 286.76 | 280 | 270 | +$1.4M | - | out (clean 33, ADX 23, RVol 0.6) |
| 24 | **BABA** | 100.55 | - | **-** | 6 | - | POS +$1.3M | 100.03 | 102 | 100 | +$84k | - | out (clean 35, ADX 19, RVol 0.5) |
| 25 | **SPY** | 754.12 | - | **-** | 5 | - | NEG -$9.7B | 770.32 | 770 | 750 | -$9.8M | - | out (clean 30, ADX 19, RVol 0.7) |
| 26 | **DELL** | 406.86 | - | **-** | 5 | - | NEG -$26.0M | - | 440 | 400 | +$704k | - | out (clean 32, ADX 13, RVol 0.3) |
| 27 | **HOOD** | 85.09 | - | **-** | 4 | - | NEG -$533k | 85.82 | 90 | 90 | +$16k | - | out (clean 30, ADX 13, RVol 0.7) |

## Big prints this scan (45)
- **QQQ** CALL 700 2026-11-04 (1DTE): 2,000 @ 1.65 = **+$330k** SELL | vol 19,226 / OI 1,725
- **QQQ** CALL 707 2026-11-04 (1DTE): 2,719 @ 0.65 = **+$177k** SELL | vol 8,983 / OI 528
- **AMD** CALL 500 2026-11-04 (1DTE): 90 @ 12.55 = **+$113k** SELL | vol 3,632 / OI 218
- **QQQ** CALL 687 2026-11-03 (0DTE): 3,602 @ 0.29 = **+$104k** SELL | vol 312,443 / OI 581
- **META** CALL 635 2026-11-06 (3DTE): 180 @ 5.40 = **+$97k** BUY | vol 2,225 / OI 1,669
- **NVDA** CALL 202.5 2026-11-06 (3DTE): 138 @ 6.50 = **+$90k** SELL | vol 1,129 / OI 1,926
- **PLTR** PUT 170 2026-11-06 (3DTE): 300 @ 2.43 = **+$73k** SELL | vol 16,919 / OI 2,434
- **AMD** CALL 500 2026-11-04 (1DTE): 53 @ 13.00 = **+$69k** SELL | vol 3,632 / OI 218
- **META** CALL 620 2026-11-04 (1DTE): 100 @ 6.67 = **+$67k** BUY | vol 11,526 / OI 383
- **META** CALL 620 2026-11-04 (1DTE): 100 @ 6.58 = **+$66k** MID | vol 11,526 / OI 383
- **MU** PUT 845 2026-11-04 (1DTE): 38 @ 13.92 = **+$53k** BUY | vol 7,702 / OI 274
- **MU** PUT 845 2026-11-04 (1DTE): 30 @ 14.57 = **+$44k** BUY | vol 7,702 / OI 274
- **MU** PUT 840 2026-11-06 (3DTE): 20 @ 20.85 = **+$42k** BUY | vol 1,430 / OI 1,144
- **MU** PUT 845 2026-11-06 (3DTE): 18 @ 22.95 = **+$41k** BUY | vol 1,406 / OI 631
- **AVGO** CALL 340 2026-11-04 (1DTE): 200 @ 1.99 = **+$40k** SELL | vol 4,251 / OI 1,354

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 730 2026-11-06 (3DTE): 9,485 traded vs OI 8,886
- **SPY** CALL 740 2026-11-13 (10DTE): 514 traded vs OI 155
- **SPY** CALL 770 2026-11-11 (8DTE): 805 traded vs OI 628
- **QQQ** CALL 722 2026-11-30 (27DTE): 4,975 traded vs OI 870
- **SMH** CALL 520 2026-11-04 (1DTE): 549 traded vs OI 38
- **NVDA** CALL 187.5 2026-11-09 (6DTE): 502 traded vs OI 4
- **NVDA** PUT 212.5 2026-11-13 (10DTE): 1,396 traded vs OI 693
- **AMZN** PUT 252.5 2026-11-06 (3DTE): 508 traded vs OI 472
- **MSFT** PUT 470 2026-11-06 (3DTE): 673 traded vs OI 0
- **MSFT** PUT 525 2026-11-04 (1DTE): 570 traded vs OI 555
- **MSFT** PUT 470 2026-11-20 (17DTE): 892 traded vs OI 0
- **MSFT** PUT 510 2026-11-06 (3DTE): 1,287 traded vs OI 1,075
- **PLTR** PUT 175 2026-11-13 (10DTE): 723 traded vs OI 719
- **MU** PUT 895 2026-11-16 (13DTE): 586 traded vs OI 0
- **MU** PUT 855 2026-11-16 (13DTE): 552 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
