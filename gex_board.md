# GEX + FLOW SCAN - Tue Nov 03, 11:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:20:08 ET, last candle SPY 11:19, QQQ 11:19 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **COIN** | 149.72 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 59 | none: 21 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$20.2M | - | 148 | 150 | -$4.6M | +$0 bull / -$151k bear | out (clean 28, ADX 66, RVol 1.2) |
| 2 | **SHOP** | 144.00 | - | **-** | 37 | - | NEG -$4.0M | - | 145 | 140 | -$3.9M | +$135k bull / +$0 bear | out (clean 32, ADX 42, RVol 1.9) |
| 3 | **BABA** | 100.20 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 37 | none: 20 calls 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +13% at the target (needs +20%) | POS +$882k | 99.93 | 102 | 100 | +$186k | - | out (clean 35, ADX 56, RVol 0.6) |
| 4 | **ORCL** | 125.54 | - | **-** | 30 | - | NEG -$41.6M | - | 135 | 125 | -$6.4M | +$399k bull / +$0 bear | out (clean 33, ADX 51, RVol 0.7) |
| 5 | **TSLA** | 400.35 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$229.3M | - | 400 | 400 | +$12.6M | +$1.3M bull / -$47k bear | out (clean 30, ADX 20, RVol 0.4) |
| 6 | **META** | 619.66 | - | **-** | 29 | - | NEG -$40.4M | 626.21 | 650 | 610 | -$15.1M | +$353k bull / -$626k bear | out (clean 28, ADX 44, RVol 0.6) |
| 7 | **MSTR** | 137.16 | - | **-** | 29 | - | POS +$84.8M | - | 135 | 125 | -$4.3M | +$955k bull / +$0 bear | out (clean 29, ADX 46, RVol 1.2) |
| 8 | **MSFT** | 516.04 | - | **-** | 27 | - | POS +$174.0M | 501.64 | 540 | 500 | -$7.4M | +$466k bull / -$201k bear | out (clean 29, ADX 32, RVol 0.6) |
| 9 | **DELL** | 408.12 | - | **-** | 25 | - | NEG -$26.1M | - | 440 | 400 | +$2.0M | +$0 bull / -$26k bear | out (clean 34, ADX 27, RVol 0.4) |
| 10 | **AVGO** | 333.97 | - | **-** | 23 | - | NEG -$43.4M | 353 | 340 | 340 | +$2.3M | +$0 bull / -$58k bear | out (clean 31, ADX 38, RVol 0.4) |
| 11 | **SMH** | 522.25 | - | **-** | 22 | - | NEG -$263.2M | - | 532.5 | 500 | +$875k | +$92k bull / +$0 bear | out (clean 32, ADX 32, RVol 1.8) |
| 12 | **NVDA** | 208.17 | - | **-** | 21 | - | POS +$118.7M | 203.72 | 210 | 200 | +$5.4M | +$230k bull / -$175k bear | out (clean 30, ADX 34, RVol 1.8) |
| 13 | **IWM** | 281.68 | - | **-** | 20 | - | NEG -$904.6M | 287.04 | 285 | 270 | -$3.9M | +$0 bull / -$67k bear | out (clean 33, ADX 27, RVol 0.7) |
| 14 | **GOOGL** | 278.31 | - | **-** | 20 | - | NEG -$43.1M | 285.03 | 285 | 290 | +$3.1M | +$178k bull / +$0 bear | out (clean 33, ADX 25, RVol 0.3) |
| 15 | **SPY** | 755.83 | - | **-** | 19 | - | NEG -$8.4B | 770.64 | 770 | 750 | -$82.4M | +$1.4M bull / -$1.8M bear | out (clean 31, ADX 23, RVol 0.5) |
| 16 | **AAPL** | 331.01 | - | **-** | 19 | - | NEG -$396.0M | 343.79 | 350 | 330 | -$3.4M | +$0 bull / -$302k bear | out (clean 31, ADX 33, RVol 1.1) |
| 17 | **AMD** | 491.60 | - | **-** | 19 | - | NEG -$68.4M | - | 520 | 500 | +$2.5M | +$319k bull / -$339k bear | out (clean 33, ADX 39, RVol 0.6) |
| 18 | **PLTR** | 172.74 | - | **-** | 19 | - | NEG -$25.5M | - | 165 | 180 | -$355k | +$642k bull / -$117k bear | out (clean 28, ADX 36, RVol 1.4) |
| 19 | **QQQ** | 686.89 | - | **-** | 17 | - | NEG -$5.0B | - | 700 | 680 | -$16.1M | +$436k bull / -$2.7M bear | out (clean 31, ADX 26, RVol 0.5) |
| 20 | **AMZN** | 247.89 | - | **-** | 16 | - | POS +$143.1M | 236.04 | 250 | 250 | -$799k | +$0 bull / -$158k bear | out (clean 33, ADX 20, RVol 0.6) |
| 21 | **MU** | 854.74 | - | **-** | 16 | - | NEG -$196.5M | - | 900 | 850 | -$3.9M | +$4.2M bull / -$27k bear | out (clean 32, ADX 24, RVol 0.5) |
| 22 | **UBER** | 66.89 | - | **-** | 14 | - | NEG -$8.8M | - | 70 | 65 | -$109k | - | out (clean 29, ADX 18, RVol 0.8) |
| 23 | **CRM** | 222.17 | - | **-** | 14 | - | NEG -$15.0M | - | 240 | 220 | -$318k | - | out (clean 29, ADX 28, RVol 0.7) |
| 24 | **NFLX** | 62.59 | - | **-** | 13 | - | NEG -$10.9M | 64.2 | 63 | 60 | -$391k | - | out (clean 28, ADX 27, RVol 0.7) |
| 25 | **ARM** | 203.65 | - | **-** | 12 | - | NEG -$6.7M | - | 220 | 200 | -$240k | - | out (clean 25, ADX 30, RVol 0.4) |
| 26 | **SMCI** | 31.64 | - | **-** | 9 | - | POS +$2.1M | - | 34.5 | 30 | -$248k | - | out (clean 34, ADX 28, RVol 0.9) |
| 27 | **HOOD** | 85.16 | - | **-** | 8 | - | NEG -$2.8M | - | 90 | 90 | -$386k | - | out (clean 31, ADX 26, RVol 0.6) |

## Big prints this scan (93)
- **SPY** PUT 767 2026-11-04 (1DTE): 500 @ 11.39 = **+$570k** SELL | vol 5,014 / OI 18,478
- **SPY** PUT 767 2026-11-04 (1DTE): 487 @ 11.41 = **+$556k** SELL | vol 5,014 / OI 18,478
- **MSFT** CALL 522.5 2026-11-04 (1DTE): 1,392 @ 2.86 = **+$398k** BUY | vol 2,745 / OI 112
- **SPY** CALL 757 2026-11-09 (6DTE): 253 @ 6.88 = **+$174k** BUY | vol 778 / OI 0
- **QQQ** PUT 687 2026-11-04 (1DTE): 200 @ 6.22 = **+$124k** SELL | vol 2,466 / OI 343
- **SPY** CALL 756 2026-11-04 (1DTE): 250 @ 4.50 = **+$112k** BUY | vol 8,933 / OI 680
- **AMD** PUT 510 2026-11-04 (1DTE): 32 @ 28.56 = **+$91k** SELL | vol 143 / OI 242
- **META** CALL 590 2026-11-06 (3DTE): 26 @ 34.39 = **+$89k** BUY | vol 28 / OI 20
- **ORCL** CALL 126 2026-11-06 (3DTE): 215 @ 3.95 = **+$85k** BUY | vol 3,960 / OI 194
- **ORCL** CALL 124 2026-11-06 (3DTE): 164 @ 5.10 = **+$84k** BUY | vol 2,715 / OI 187
- **MU** CALL 865 2026-11-04 (1DTE): 50 @ 16.00 = **+$80k** BUY | vol 5,648 / OI 743
- **TSLA** CALL 405 2026-11-06 (3DTE): 100 @ 7.75 = **+$78k** BUY | vol 4,058 / OI 3,643
- **TSLA** CALL 405 2026-11-06 (3DTE): 98 @ 7.55 = **+$74k** BUY | vol 4,058 / OI 3,643
- **ORCL** CALL 126 2026-11-06 (3DTE): 173 @ 3.95 = **+$68k** BUY | vol 3,960 / OI 194
- **META** CALL 625 2026-11-04 (1DTE): 100 @ 6.50 = **+$65k** BUY | vol 5,254 / OI 334

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 757 2026-11-09 (6DTE): 778 traded vs OI 0
- **SPY** PUT 728 2026-11-03 (0DTE): 2,221 traded vs OI 1,543
- **SPY** CALL 760 2026-11-09 (6DTE): 1,099 traded vs OI 1,088
- **SPY** CALL 774 2026-11-05 (2DTE): 689 traded vs OI 0
- **QQQ** CALL 687 2026-11-05 (2DTE): 534 traded vs OI 0
- **QQQ** PUT 660 2026-11-04 (1DTE): 2,956 traded vs OI 2,939
- **QQQ** PUT 698 2026-11-03 (0DTE): 508 traded vs OI 119
- **QQQ** PUT 683 2026-11-05 (2DTE): 503 traded vs OI 0
- **QQQ** CALL 709 2026-11-04 (1DTE): 586 traded vs OI 423
- **QQQ** CALL 710 2026-11-03 (0DTE): 5,426 traded vs OI 5,346
- **IWM** CALL 285 2026-11-13 (10DTE): 1,114 traded vs OI 1,084
- **NVDA** CALL 217.5 2026-11-09 (6DTE): 514 traded vs OI 206
- **NVDA** CALL 220 2026-11-16 (13DTE): 846 traded vs OI 0
- **TSLA** CALL 402.5 2026-11-13 (10DTE): 515 traded vs OI 294
- **AAPL** CALL 330 2026-11-13 (10DTE): 617 traded vs OI 585

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
