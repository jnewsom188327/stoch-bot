# GEX + FLOW SCAN - Tue Nov 03, 10:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:30:08 ET, last candle SPY 10:29, QQQ 10:29 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DELL** | 409.44 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 68 | none: 33 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$26.0M | - | 440 | 400 | +$2.1M | +$128k bull / +$0 bear | LONG (clean 35, ADX 35, RVol 1.0) |
| 2 | **ORCL** | 125.30 | FLOW SURGE | **PUTS** | 54 | none: 25 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$40.5M | - | 135 | 125 | -$5.8M | +$86k bull / -$295k bear | out (clean 33, ADX 45, RVol 2.0) |
| 3 | **BABA** | 100.65 | TREND (flow not with it) | **PUTS** | 52 | none: 20 puts 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -1% at the target (needs +20%) | POS +$1.7M | 100.03 | 102 | 100 | +$96k | +$0 bull / -$28k bear | SHORT (clean 35, ADX 58, RVol 1.4) |
| 4 | **MSTR** | 135.01 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 50 | none: 27 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$77.5M | - | 135 | 125 | -$2.5M | +$0 bull / -$146k bear | out (clean 28, ADX 35, RVol 0.9) |
| 5 | **COIN** | 145.43 | FLOW SURGE | **PUTS** | 47 | none: 23 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$21.0M | - | 148 | 150 | -$1.3M | +$0 bull / -$40k bear | out (clean 27, ADX 52, RVol 1.0) |
| 6 | **META** | 617.85 | FLOW SURGE | **PUTS** | 41 | none: 146 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$55.5M | 626.43 | 650 | 610 | -$12.6M | +$123k bull / -$1.3M bear | out (clean 27, ADX 30, RVol 0.6) |
| 7 | **MSFT** | 514.75 | FLOW SURGE | **PUTS** | 41 | none: 122 puts 0-7DTE > 14 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | POS +$159.5M | 501.14 | 540 | 500 | -$4.4M | +$0 bull / -$200k bear | out (clean 29, ADX 37, RVol 1.1) |
| 8 | **SMCI** | 31.68 | TREND (flow not with it) | **CALLS** | 35 | none: 12 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$2.1M | - | 34.5 | 30 | -$259k | +$25k bull / -$81k bear | LONG (clean 36, ADX 31, RVol 1.7) |
| 9 | **SHOP** | 142.71 | - | **-** | 31 | - | NEG -$4.3M | - | 145 | 140 | -$3.9M | - | out (clean 32, ADX 54, RVol 2.6) |
| 10 | **GOOGL** | 277.93 | TREND (flow not with it) | **PUTS** | 30 | none: 66 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$48.5M | 285.49 | 285 | 290 | +$2.8M | +$90k bull / +$0 bear | SHORT (clean 34, ADX 35, RVol 0.5) |
| 11 | **AVGO** | 333.60 | - | **-** | 27 | - | NEG -$45.4M | 353.41 | 340 | 340 | +$3.1M | +$39k bull / -$95k bear | out (clean 32, ADX 35, RVol 0.9) |
| 12 | **PLTR** | 169.81 | - | **-** | 27 | - | NEG -$28.0M | - | 165 | 180 | +$2.7M | +$181k bull / -$352k bear | out (clean 28, ADX 57, RVol 3.2) |
| 13 | **SMH** | 520.90 | - | **-** | 23 | - | NEG -$276.8M | - | 532.5 | 500 | +$1.2M | +$822k bull / +$0 bear | out (clean 33, ADX 33, RVol 0.7) |
| 14 | **IWM** | 280.96 | - | **-** | 22 | - | NEG -$1.1B | 287.21 | 285 | 270 | -$4.6M | +$0 bull / -$54k bear | out (clean 33, ADX 19, RVol 1.0) |
| 15 | **AMD** | 490.03 | - | **-** | 21 | - | NEG -$69.0M | - | 520 | 500 | +$1.6M | +$312k bull / -$1.2M bear | out (clean 33, ADX 42, RVol 1.3) |
| 16 | **SPY** | 754.59 | - | **-** | 20 | - | NEG -$9.2B | 770.86 | 770 | 750 | -$38.8M | +$653k bull / -$2.3M bear | out (clean 31, ADX 24, RVol 0.8) |
| 17 | **NVDA** | 208.03 | - | **-** | 20 | - | POS +$111.9M | 203.48 | 210 | 200 | +$5.0M | +$147k bull / -$218k bear | out (clean 31, ADX 38, RVol 0.6) |
| 18 | **TSLA** | 401.39 | - | **-** | 20 | - | POS +$235.2M | - | 400 | 400 | +$13.4M | +$1.2M bull / -$263k bear | out (clean 31, ADX 21, RVol 0.7) |
| 19 | **AAPL** | 330.11 | - | **-** | 20 | - | NEG -$397.4M | 342.83 | 350 | 330 | -$7.6M | +$1.1M bull / -$1.2M bear | out (clean 32, ADX 31, RVol 1.2) |
| 20 | **AMZN** | 246.81 | - | **-** | 19 | - | POS +$128.1M | 236.28 | 250 | 250 | +$981k | +$0 bull / -$58k bear | out (clean 33, ADX 25, RVol 0.6) |
| 21 | **MU** | 861.10 | - | **-** | 18 | - | NEG -$190.7M | - | 900 | 850 | -$617k | +$2.6M bull / -$1.2M bear | out (clean 32, ADX 34, RVol 0.9) |
| 22 | **QQQ** | 686.13 | - | **-** | 17 | - | NEG -$5.0B | - | 700 | 680 | -$4.9M | +$101k bull / -$898k bear | out (clean 32, ADX 26, RVol 0.9) |
| 23 | **HOOD** | 84.29 | - | **-** | 17 | - | NEG -$3.5M | - | 90 | 85 | -$128k | +$80k bull / +$0 bear | out (clean 31, ADX 23, RVol 0.7) |
| 24 | **CRM** | 220.65 | - | **-** | 16 | - | NEG -$15.3M | - | 240 | 220 | -$248k | - | out (clean 28, ADX 48, RVol 0.5) |
| 25 | **NFLX** | 62.34 | - | **-** | 12 | - | NEG -$13.8M | 64.8 | 63 | 60 | -$233k | - | out (clean 28, ADX 27, RVol 0.7) |
| 26 | **UBER** | 66.44 | - | **-** | 12 | - | NEG -$13.8M | - | 70 | 65 | -$35k | - | out (clean 29, ADX 24, RVol 0.9) |
| 27 | **ARM** | 204.43 | - | **-** | 9 | - | NEG -$6.4M | - | 220 | 200 | -$83k | - | out (clean 25, ADX 29, RVol 0.4) |

## Big prints this scan (83)
- **MU** PUT 840 2026-11-04 (1DTE): 300 @ 10.50 = **+$315k** BUY | vol 3,966 / OI 244
- **SPY** PUT 750 2026-11-05 (2DTE): 720 @ 3.63 = **+$261k** BUY | vol 1,399 / OI 2,622
- **QQQ** CALL 700 2026-11-06 (3DTE): 421 @ 4.32 = **+$182k** SELL | vol 5,635 / OI 13,477
- **SMH** CALL 540 2026-11-06 (3DTE): 347 @ 4.65 = **+$161k** BUY | vol 2,979 / OI 1,935
- **SPY** PUT 745 2026-11-05 (2DTE): 720 @ 2.23 = **+$161k** BUY | vol 1,892 / OI 1,314
- **AAPL** PUT 330 2026-11-06 (3DTE): 398 @ 3.40 = **+$135k** SELL | vol 9,179 / OI 11,856
- **AAPL** PUT 330 2026-11-06 (3DTE): 400 @ 3.15 = **+$126k** SELL | vol 9,179 / OI 11,856
- **MU** PUT 860 2026-11-09 (6DTE): 40 @ 29.21 = **+$117k** SELL | vol 118 / OI 139
- **AMD** PUT 490 2026-11-06 (3DTE): 48 @ 23.35 = **+$112k** BUY | vol 393 / OI 740
- **SPY** CALL 743 2026-11-03 (0DTE): 100 @ 11.00 = **+$110k** SELL | vol 473 / OI 16
- **MU** CALL 875 2026-11-04 (1DTE): 100 @ 11.00 = **+$110k** BUY | vol 2,712 / OI 201
- **SPY** CALL 754 2026-11-03 (0DTE): 545 @ 1.96 = **+$107k** SELL | vol 97,005 / OI 879
- **MU** CALL 875 2026-11-04 (1DTE): 100 @ 10.60 = **+$106k** SELL | vol 2,712 / OI 201
- **MU** PUT 860 2026-11-06 (3DTE): 40 @ 25.85 = **+$103k** SELL | vol 820 / OI 672
- **AMD** CALL 495 2026-11-06 (3DTE): 50 @ 20.55 = **+$103k** BUY | vol 644 / OI 163

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 745 2026-11-05 (2DTE): 1,892 traded vs OI 1,314
- **QQQ** CALL 684 2026-11-06 (3DTE): 583 traded vs OI 61
- **QQQ** CALL 679 2026-11-03 (0DTE): 526 traded vs OI 45
- **QQQ** PUT 692 2026-11-03 (0DTE): 513 traded vs OI 456
- **QQQ** CALL 701 2026-11-04 (1DTE): 522 traded vs OI 183
- **QQQ** PUT 689 2026-11-04 (1DTE): 527 traded vs OI 179
- **QQQ** CALL 685 2026-11-06 (3DTE): 1,474 traded vs OI 1,370
- **QQQ** CALL 690 2026-11-05 (2DTE): 500 traded vs OI 451
- **QQQ** CALL 702 2026-11-06 (3DTE): 756 traded vs OI 707
- **IWM** CALL 285 2026-11-03 (0DTE): 2,167 traded vs OI 2,116
- **IWM** CALL 278 2026-11-04 (1DTE): 612 traded vs OI 236
- **IWM** CALL 281 2026-11-13 (10DTE): 560 traded vs OI 457
- **IWM** PUT 274 2026-11-04 (1DTE): 642 traded vs OI 618
- **SMH** CALL 540 2026-11-06 (3DTE): 2,979 traded vs OI 1,935
- **NVDA** PUT 187.5 2026-11-04 (1DTE): 613 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
