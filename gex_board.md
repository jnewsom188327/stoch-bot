# GEX + FLOW SCAN - Mon Nov 02, 11:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (1)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 0.67 | +18% (4m) | **-6%** | +12% | 693.07 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:50:08 ET, last candle SPY 11:49, QQQ 11:49 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
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
| 1 | **MU** | 860.62 | FLOW SURGE | **CALLS** | 53 | none: 144 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (55 contracts' greeks worked out here) | NEG -$209.4M | - | 910 | 850 | +$85.4M | +$5.9M bull / +$0 bear | out (clean 30, ADX 25, RVol 3.2) |
| 2 | **TSLA** | 410.11 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 39 | none: 132 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (57 contracts' greeks worked out here) | POS +$307.5M | - | 410 | 400 | -$71.7M | +$1.8M bull / -$108k bear | out (clean 30, ADX 36, RVol 0.5) |
| 3 | **SMCI** | 32.22 | FLIP CROSS down into negative gamma | **PUTS** | 36 | none: 13 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$36k | 33 | 35 | 33 | +$168k | +$30k bull / +$0 bear | SHORT (clean 33, ADX 29, RVol 0.9) |
| 4 | **AMD** | 488.51 | - | **-** | 26 | - | NEG -$82.2M | - | 500 | 480 | +$29.0M | +$1.0M bull / -$358k bear | out (clean 30, ADX 34, RVol 1.0) |
| 5 | **AMZN** | 251.43 | - | **-** | 26 | - | POS +$110.2M | 241.91 | 250 | 250 | -$24.0M | +$154k bull / -$340k bear | out (clean 33, ADX 54, RVol 0.6) |
| 6 | **SMH** | 522.72 | - | **-** | 25 | - | NEG -$341.6M | - | 532.5 | 500 | +$3.2M | +$109k bull / +$0 bear | out (clean 31, ADX 26, RVol 0.6) |
| 7 | **MSTR** | 136.17 | - | **-** | 23 | - | POS +$3.9M | - | 135 | 140 | +$1.8M | +$0 bull / -$84k bear | out (clean 26, ADX 38, RVol 1.7) |
| 8 | **AAPL** | 339.07 | - | **-** | 22 | - | POS +$29.5M | 336.85 | 350 | 330 | +$12.9M | +$2.8M bull / +$0 bear | out (clean 31, ADX 16, RVol 1.2) |
| 9 | **BABA** | 103.29 | - | **-** | 22 | - | POS +$2.8M | 101.06 | 105 | 100 | -$1.2M | - | out (clean 33, ADX 48, RVol 1.1) |
| 10 | **COIN** | 140.12 | - | **-** | 20 | - | NEG -$7.8M | - | 150 | 130 | -$371k | +$0 bull / -$64k bear | out (clean 25, ADX 17, RVol 1.2) |
| 11 | **HOOD** | 86.56 | - | **-** | 20 | - | NEG -$8.9M | - | 93 | 90 | -$627k | +$0 bull / -$31k bear | out (clean 32, ADX 35, RVol 0.4) |
| 12 | **IWM** | 282.50 | - | **-** | 19 | - | NEG -$794.0M | 286.4 | 285 | 270 | -$2.5M | +$0 bull / -$1.6M bear | out (clean 31, ADX 34, RVol 0.5) |
| 13 | **META** | 612.64 | - | **-** | 19 | - | NEG -$131.4M | 626.35 | 650 | 610 | +$9.5M | +$38k bull / -$104k bear | out (clean 29, ADX 26, RVol 0.6) |
| 14 | **SHOP** | 158.57 | - | **-** | 19 | - | NEG -$275k | - | 170 | 160 | -$422k | - | out (clean 28, ADX 19, RVol 1.3) |
| 15 | **NVDA** | 206.91 | - | **-** | 18 | - | NEG -$191.3M | 213.66 | 210 | 200 | +$7.0M | +$91k bull / +$0 bear | out (clean 30, ADX 20, RVol 1.2) |
| 16 | **MSFT** | 524.81 | - | **-** | 18 | - | POS +$354.9M | 500.37 | 540 | 530 | -$3.2M | +$43k bull / -$31k bear | out (clean 26, ADX 20, RVol 0.8) |
| 17 | **ORCL** | 123.49 | - | **-** | 18 | - | NEG -$39.7M | - | 130 | 120 | -$609k | +$30k bull / +$0 bear | out (clean 32, ADX 29, RVol 0.5) |
| 18 | **GOOGL** | 283.16 | - | **-** | 17 | - | NEG -$90.5M | - | 285 | 290 | +$1.7M | +$168k bull / +$0 bear | out (clean 35, ADX 23, RVol 0.7) |
| 19 | **NFLX** | 62.27 | - | **-** | 17 | - | NEG -$23.0M | - | 63 | 60 | +$214k | +$0 bull / -$41k bear | out (clean 29, ADX 15, RVol 1.2) |
| 20 | **UBER** | 67.38 | - | **-** | 17 | - | NEG -$8.0M | - | 70 | 65 | -$463k | - | out (clean 28, ADX 41, RVol 0.8) |
| 21 | **SPY** | 760.01 | - | **-** | 16 | - | NEG -$9.3B | 774.2 | 800 | 750 | -$21.6M | +$553k bull / -$367k bear | out (clean 30, ADX 24, RVol 0.5) |
| 22 | **QQQ** | 693.65 | - | **-** | 16 | - | NEG -$5.6B | 731.23 | 720 | 680 | +$12.0M | +$692k bull / -$9.8M bear | out (clean 30, ADX 21, RVol 0.7) |
| 23 | **AVGO** | 330.69 | - | **-** | 14 | - | NEG -$98.8M | - | 340 | 330 | -$6.0M | - | out (clean 31, ADX 38, RVol 0.4) |
| 24 | **PLTR** | 184.52 | - | **-** | 14 | - | NEG -$11.1M | - | 200 | 180 | -$728k | +$57k bull / +$0 bear | out (clean 25, ADX 11, RVol 0.6) |
| 25 | **DELL** | 414.40 | - | **-** | 14 | - | NEG -$23.9M | - | 440 | 400 | -$41k | +$60k bull / +$0 bear | out (clean 34, ADX 13, RVol 0.7) |
| 26 | **ARM** | 204.67 | - | **-** | 10 | - | NEG -$7.0M | - | 220 | 200 | +$186k | - | out (clean 26, ADX 16, RVol 0.6) |
| 27 | **CRM** | 232.10 | - | **-** | 9 | - | NEG -$5.5M | 242.18 | 240 | 220 | +$90k | - | out (clean 28, ADX 13, RVol 0.5) |

## Big prints this scan (86)
- **IWM** PUT 277 2026-11-06 (4DTE): 15,000 @ 1.10 = **+$1.6M** BUY | vol 39,815 / OI 595
- **AAPL** CALL 350 2026-11-06 (4DTE): 700 @ 3.65 = **+$256k** BUY | vol 13,709 / OI 6,983
- **MU** CALL 840 2026-11-09 (7DTE): 54 @ 45.90 = **+$248k** BUY | vol 258 / OI 0
- **QQQ** PUT 701 2026-11-06 (4DTE): 196 @ 12.48 = **+$245k** SELL | vol 369 / OI 595
- **AMZN** CALL 242.5 2026-11-06 (4DTE): 149 @ 10.49 = **+$156k** SELL | vol 601 / OI 513
- **AMD** PUT 487.5 2026-11-02 (0DTE): 579 @ 2.50 = **+$145k** MID | vol 5,501 / OI 24
- **AMZN** CALL 242.5 2026-11-02 (0DTE): 149 @ 9.07 = **+$135k** MID | vol 2,856 / OI 153
- **SPY** PUT 750 2026-11-04 (2DTE): 990 @ 1.34 = **+$133k** BUY | vol 16,595 / OI 1,303
- **AMD** CALL 510 2026-11-06 (4DTE): 85 @ 15.37 = **+$131k** BUY | vol 1,078 / OI 278
- **MU** CALL 885 2026-11-04 (2DTE): 100 @ 12.65 = **+$126k** BUY | vol 1,509 / OI 10
- **QQQ** PUT 701 2026-11-06 (4DTE): 100 @ 12.52 = **+$125k** SELL | vol 369 / OI 595
- **MU** PUT 860 2026-11-02 (0DTE): 400 @ 2.78 = **+$111k** SELL | vol 18,756 / OI 312
- **QQQ** CALL 684 2026-11-03 (1DTE): 87 @ 11.92 = **+$104k** BUY | vol 219 / OI 0
- **TSLA** PUT 407.5 2026-11-06 (4DTE): 110 @ 8.00 = **+$88k** SELL | vol 3,250 / OI 1,311
- **MU** PUT 895 2026-11-06 (4DTE): 20 @ 43.55 = **+$87k** SELL | vol 220 / OI 327

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 769 2026-11-02 (0DTE): 1,833 traded vs OI 1,830
- **SPY** CALL 830 2026-11-13 (11DTE): 1,091 traded vs OI 348
- **QQQ** CALL 691 2026-11-03 (1DTE): 508 traded vs OI 0
- **QQQ** PUT 694 2026-11-06 (4DTE): 514 traded vs OI 473
- **QQQ** PUT 687 2026-11-20 (18DTE): 1,129 traded vs OI 1,128
- **IWM** PUT 270 2026-11-09 (7DTE): 509 traded vs OI 160
- **NVDA** PUT 215 2026-11-04 (2DTE): 741 traded vs OI 722
- **NVDA** CALL 215 2026-11-06 (4DTE): 11,167 traded vs OI 10,928
- **TSLA** CALL 412.5 2026-11-13 (11DTE): 507 traded vs OI 273
- **TSLA** CALL 415 2026-11-09 (7DTE): 501 traded vs OI 158
- **AAPL** PUT 327.5 2026-11-20 (18DTE): 527 traded vs OI 315
- **AAPL** CALL 347.5 2026-11-06 (4DTE): 633 traded vs OI 603
- **AAPL** PUT 345 2026-11-04 (2DTE): 691 traded vs OI 688
- **AMD** PUT 455 2026-11-06 (4DTE): 599 traded vs OI 0
- **AMD** CALL 500 2026-11-06 (4DTE): 514 traded vs OI 354

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
