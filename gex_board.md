# GEX + FLOW SCAN - Mon Nov 02, 01:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 1.48 | +291% (43m) | **+128%** (done) | +11% | 692.76 hit |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 1.27 | +111% (58m) | **+79%** (done) | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:20:08 ET, last candle SPY 13:19, QQQ 13:19 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 12:02 | QQQ | 1m FAILED POP | R3 | PUTS | TURNING away | **FIRE** QQQ261102P00691000 |
| 11:54 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 90 puts 0-1DTE > 5 priced 0.40-0.80 > 3 delta 0.15+ > 3 spread ok > 3 liquid  |
| 11:36 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** QQQ261102P00691000 |
| 11:36 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 90 puts 0-1DTE > 5 priced 0.40-0.80 > 3 delta 0.15+ > 3 spread ok > 3 liquid  |

## Flow surges NOT fired - price disagreed (5 today, last 5)
- 10:35 SPY PUTS: price +0.32 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:25 SPY PUTS: price +2.69 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:10 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 10:05 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 09:50 BABA PUTS: price +0.75 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SHOP** | 160.48 | FLOW SURGE | **PUTS** | 42 | none: 16 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$469k | - | 175 | 175 | -$757k | +$0 bull / -$31k bear | out (clean 28, ADX 26, RVol 0.9) |
| 2 | **DELL** | 407.07 | TREND (flow not with it) | **PUTS** | 36 | none: 33 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$21.7M | - | 440 | 400 | +$440k | +$0 bull / -$130k bear | SHORT (clean 33, ADX 26, RVol 1.3) |
| 3 | **SMCI** | 31.56 | TREND (flow not with it) | **PUTS** | 35 | none: 13 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$409k | - | 34 | 30 | +$590k | +$82k bull / +$0 bear | SHORT (clean 34, ADX 41, RVol 1.1) |
| 4 | **AMZN** | 250.22 | PINNED between the walls (positive gamma) - chop | **-** | 32 | - | POS +$91.8M | 242.19 | 250 | 250 | -$21.9M | +$32k bull / -$156k bear | out (clean 33, ADX 22, RVol 0.4) |
| 5 | **MU** | 853.66 | - | **-** | 28 | - | NEG -$219.8M | - | 910 | 850 | +$131.0M | +$2.9M bull / -$3.9M bear | out (clean 31, ADX 38, RVol 0.8) |
| 6 | **AMD** | 483.20 | - | **-** | 25 | - | NEG -$82.3M | - | 500 | 480 | +$32.0M | +$195k bull / -$3.0M bear | out (clean 31, ADX 41, RVol 1.1) |
| 7 | **MSFT** | 519.93 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 24 | 11/02 522.5C @ 0.41 (delta 0.21) = est +504% at 525 | POS +$240.5M | 502.13 | 540 | 520 | -$1.1M | - | out (clean 27, ADX 30, RVol 0.4) |
| 8 | **AAPL** | 337.78 | - | **-** | 23 | - | POS +$11.0M | 336.82 | 350 | 330 | +$18.2M | +$303k bull / -$979k bear | out (clean 31, ADX 31, RVol 0.9) |
| 9 | **SMH** | 520.55 | - | **-** | 22 | - | NEG -$351.8M | - | 532.5 | 500 | +$3.4M | +$0 bull / -$314k bear | out (clean 31, ADX 23, RVol 0.7) |
| 10 | **ARM** | 203.00 | - | **-** | 20 | - | NEG -$6.9M | - | 220 | 200 | +$251k | +$0 bull / -$38k bear | out (clean 25, ADX 19, RVol 0.3) |
| 11 | **TSLA** | 408.66 | - | **-** | 18 | - | POS +$314.4M | - | 410 | 400 | -$72.3M | +$137k bull / -$1.5M bear | out (clean 30, ADX 20, RVol 0.5) |
| 12 | **MSTR** | 133.71 | - | **-** | 18 | - | POS +$3.1M | - | 135 | 125 | +$3.4M | +$0 bull / -$244k bear | out (clean 26, ADX 17, RVol 0.6) |
| 13 | **QQQ** | 691.74 | - | **-** | 17 | - | NEG -$5.5B | 733.03 | 720 | 680 | +$40.7M | +$366k bull / -$2.4M bear | out (clean 30, ADX 23, RVol 0.6) |
| 14 | **META** | 611.93 | - | **-** | 17 | - | NEG -$129.5M | 625.04 | 650 | 610 | +$10.1M | +$0 bull / -$576k bear | out (clean 29, ADX 21, RVol 0.3) |
| 15 | **ORCL** | 122.34 | - | **-** | 17 | - | NEG -$37.9M | - | 130 | 120 | -$469k | +$32k bull / -$32k bear | out (clean 31, ADX 31, RVol 0.4) |
| 16 | **SPY** | 758.88 | - | **-** | 16 | - | NEG -$9.9B | 774.67 | 800 | 750 | +$11.4M | +$0 bull / -$2.1M bear | out (clean 30, ADX 23, RVol 0.9) |
| 17 | **IWM** | 281.29 | - | **-** | 16 | - | NEG -$994.2M | 286.66 | 285 | 270 | -$1.3M | +$74k bull / -$766k bear | out (clean 32, ADX 22, RVol 0.9) |
| 18 | **NVDA** | 206.69 | - | **-** | 16 | - | NEG -$211.0M | 215.37 | 210 | 200 | +$6.5M | +$831k bull / -$1.2M bear | out (clean 28, ADX 15, RVol 0.9) |
| 19 | **PLTR** | 184.26 | - | **-** | 16 | - | NEG -$11.0M | - | 200 | 180 | +$2.3M | +$190k bull / -$190k bear | out (clean 25, ADX 13, RVol 0.6) |
| 20 | **HOOD** | 85.34 | - | **-** | 16 | - | NEG -$10.4M | - | 93 | 90 | -$309k | +$28k bull / +$0 bear | out (clean 32, ADX 25, RVol 0.5) |
| 21 | **BABA** | 103.02 | - | **-** | 15 | - | POS +$2.6M | 100.97 | 105 | 100 | -$1.0M | - | out (clean 33, ADX 22, RVol 1.1) |
| 22 | **GOOGL** | 283.52 | - | **-** | 14 | - | NEG -$101.7M | - | 285 | 285 | +$401k | +$148k bull / -$1.1M bear | out (clean 33, ADX 15, RVol 0.3) |
| 23 | **UBER** | 67.20 | - | **-** | 13 | - | NEG -$8.5M | - | 70 | 65 | -$509k | - | out (clean 28, ADX 23, RVol 0.6) |
| 24 | **NFLX** | 62.57 | - | **-** | 8 | - | NEG -$20.8M | - | 63 | 60 | -$274k | - | out (clean 28, ADX 28, RVol 0.6) |
| 25 | **AVGO** | 330.03 | - | **-** | 8 | - | NEG -$101.7M | - | 340 | 330 | -$5.1M | - | out (clean 30, ADX 19, RVol 0.4) |
| 26 | **COIN** | 139.66 | - | **-** | 7 | - | NEG -$7.9M | - | 150 | 130 | -$375k | - | out (clean 23, ADX 11, RVol 0.7) |
| 27 | **CRM** | 232.28 | - | **-** | 5 | - | NEG -$4.9M | 241.67 | 240 | 220 | +$45k | - | out (clean 26, ADX 11, RVol 0.4) |

## Big prints this scan (67)
- **IWM** CALL 285 2026-11-09 (7DTE): 1,500 @ 1.74 = **+$261k** SELL | vol 7,758 / OI 0
- **MSTR** CALL 133 2026-11-06 (4DTE): 420 @ 5.80 = **+$244k** SELL | vol 3,233 / OI 40
- **MSTR** CALL 134 2026-11-06 (4DTE): 420 @ 5.30 = **+$223k** MID | vol 1,987 / OI 87
- **GOOGL** CALL 287.5 2026-11-06 (4DTE): 749 @ 2.88 = **+$216k** SELL | vol 4,008 / OI 375
- **AMZN** PUT 250 2026-11-04 (2DTE): 662 @ 3.10 = **+$205k** MID | vol 10,190 / OI 132
- **NVDA** PUT 207.5 2026-11-04 (2DTE): 574 @ 3.50 = **+$201k** BUY | vol 15,488 / OI 878
- **GOOGL** CALL 285 2026-11-06 (4DTE): 369 @ 3.90 = **+$144k** MID | vol 6,118 / OI 2,236
- **GOOGL** CALL 285 2026-11-06 (4DTE): 320 @ 3.75 = **+$120k** SELL | vol 6,118 / OI 2,236
- **PLTR** PUT 180 2026-11-06 (4DTE): 129 @ 9.25 = **+$119k** SELL | vol 1,945 / OI 3,137
- **SMCI** PUT 32 2026-11-06 (4DTE): 400 @ 2.39 = **+$96k** MID | vol 1,130 / OI 1,812
- **META** CALL 625 2026-11-06 (4DTE): 130 @ 6.70 = **+$87k** SELL | vol 965 / OI 647
- **MU** CALL 855 2026-11-02 (0DTE): 200 @ 4.20 = **+$84k** BUY | vol 10,040 / OI 69
- **SMCI** CALL 32 2026-11-06 (4DTE): 400 @ 2.06 = **+$82k** BUY | vol 1,642 / OI 649
- **TSLA** PUT 407.5 2026-11-04 (2DTE): 100 @ 7.00 = **+$70k** BUY | vol 5,150 / OI 106
- **TSLA** PUT 407.5 2026-11-04 (2DTE): 100 @ 7.00 = **+$70k** BUY | vol 5,150 / OI 106

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 760 2026-11-11 (9DTE): 531 traded vs OI 2
- **QQQ** CALL 718 2026-11-03 (1DTE): 903 traded vs OI 752
- **QQQ** CALL 700 2026-11-27 (25DTE): 500 traded vs OI 203
- **IWM** PUT 275 2026-11-09 (7DTE): 1,805 traded vs OI 537
- **TSLA** PUT 370 2026-11-09 (7DTE): 506 traded vs OI 153
- **AAPL** PUT 310 2026-11-20 (18DTE): 30,683 traded vs OI 17,466
- **AMD** PUT 467.5 2026-11-02 (0DTE): 553 traded vs OI 82
- **AMZN** CALL 275 2026-11-13 (11DTE): 502 traded vs OI 0
- **GOOGL** PUT 280 2026-11-06 (4DTE): 1,304 traded vs OI 1,302
- **MU** PUT 795 2026-11-04 (2DTE): 501 traded vs OI 0
- **MU** PUT 795 2026-11-06 (4DTE): 509 traded vs OI 0
- **MU** PUT 870 2026-11-06 (4DTE): 807 traded vs OI 803

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
