# GEX + FLOW SCAN - Mon Nov 02, 03:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 1.48 | +291% (43m) | **+128%** (done) | +11% | 692.76 hit |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 1.27 | +111% (58m) | **+79%** (done) | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (7 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:00:08 ET, last candle SPY 14:59, QQQ 14:59 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 14:28 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | TURNING your way | no contract: 75 calls 0-1DTE > 6 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid |
| 14:26 | QQQ | 1m WHIPSAW | R1 R2 | PUTS | WITH you | no contract: 75 puts 0-1DTE > 4 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 14:16 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | no contract: 92 puts 0-1DTE > 6 priced 0.40-0.80 > 3 delta 0.15+ > 3 spread ok > 3 liquid  |
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
| 1 | **MU** | 838.44 | FLOW SURGE | **CALLS** | 42 | none: 133 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (50 contracts' greeks worked out here) | NEG -$221.1M | - | 910 | 850 | +$180.9M | +$2.5M bull / -$284k bear | out (clean 32, ADX 54, RVol 0.9) |
| 2 | **TSLA** | 404.85 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 41 | 11/02 402.5P @ 0.42 (delta 0.23) = est +493% at 400 | POS +$244.7M | - | 405 | 400 | -$33.1M | +$3.9M bull / -$376k bear | out (clean 32, ADX 39, RVol 1.1) |
| 3 | **SMCI** | 30.89 | TREND (flow not with it) | **PUTS** | 36 | none: 12 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$498k | - | 33 | 30 | +$922k | - | SHORT (clean 36, ADX 56, RVol 1.0) |
| 4 | **BABA** | 102.37 | TREND + FLOW | **PUTS** | 33 | none: 20 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$1.9M | 100.91 | 105 | 100 | -$937k | - | SHORT (clean 33, ADX 37, RVol 0.5) |
| 5 | **SMH** | 512.44 | - | **-** | 30 | - | NEG -$337.8M | - | 532.5 | 500 | +$8.6M | +$631k bull / -$463k bear | out (clean 33, ADX 55, RVol 0.9) |
| 6 | **AMD** | 474.95 | - | **-** | 26 | - | NEG -$72.7M | - | 500 | 480 | +$50.6M | +$904k bull / -$2.1M bear | out (clean 33, ADX 62, RVol 0.9) |
| 7 | **SPY** | 755.29 | - | **-** | 24 | - | NEG -$10.6B | 775.35 | 800 | 750 | +$165.3M | +$1.4M bull / -$2.7M bear | out (clean 31, ADX 50, RVol 1.1) |
| 8 | **QQQ** | 685.65 | - | **-** | 24 | - | NEG -$5.5B | - | 720 | 680 | +$201.8M | +$2.0M bull / -$2.2M bear | out (clean 32, ADX 54, RVol 0.9) |
| 9 | **NVDA** | 204.18 | - | **-** | 23 | - | NEG -$247.1M | - | 210 | 200 | +$21.5M | +$379k bull / -$392k bear | out (clean 30, ADX 44, RVol 1.0) |
| 10 | **AAPL** | 337.51 | - | **-** | 23 | - | POS +$8.1M | 336.95 | 350 | 330 | +$21.8M | +$0 bull / -$1.5M bear | out (clean 31, ADX 27, RVol 1.3) |
| 11 | **AMZN** | 248.52 | - | **-** | 23 | - | POS +$60.1M | 243.66 | 250 | 250 | -$17.3M | +$103k bull / -$26k bear | out (clean 34, ADX 45, RVol 0.6) |
| 12 | **PLTR** | 181.19 | - | **-** | 23 | - | NEG -$14.0M | - | 190 | 180 | +$5.0M | +$372k bull / -$81k bear | out (clean 26, ADX 40, RVol 0.9) |
| 13 | **MSFT** | 514.59 | - | **-** | 22 | - | POS +$113.6M | 502.56 | 535 | 500 | +$3.2M | +$149k bull / +$0 bear | out (clean 28, ADX 52, RVol 0.9) |
| 14 | **DELL** | 401.68 | - | **-** | 22 | - | NEG -$20.2M | - | 440 | 400 | +$2.3M | +$30k bull / -$90k bear | out (clean 34, ADX 45, RVol 0.6) |
| 15 | **MSTR** | 130.86 | - | **-** | 22 | - | POS +$1.4M | - | 135 | 125 | +$4.4M | +$27k bull / +$0 bear | out (clean 26, ADX 31, RVol 0.6) |
| 16 | **SHOP** | 157.40 | - | **-** | 22 | - | NEG -$258k | - | 170 | 160 | -$346k | +$103k bull / +$0 bear | out (clean 30, ADX 30, RVol 1.3) |
| 17 | **ORCL** | 119.83 | - | **-** | 21 | - | NEG -$36.4M | - | 130 | 120 | +$727k | +$178k bull / +$0 bear | out (clean 33, ADX 44, RVol 0.9) |
| 18 | **HOOD** | 84.25 | - | **-** | 21 | - | NEG -$11.3M | - | 85 | 90 | +$767k | +$55k bull / -$63k bear | out (clean 32, ADX 41, RVol 0.9) |
| 19 | **COIN** | 136.78 | - | **-** | 20 | - | NEG -$7.4M | - | 150 | 130 | -$122k | +$0 bull / -$45k bear | out (clean 25, ADX 40, RVol 0.7) |
| 20 | **AVGO** | 325.48 | - | **-** | 19 | - | NEG -$113.0M | - | 340 | 320 | -$2.1M | +$0 bull / -$65k bear | out (clean 32, ADX 40, RVol 0.4) |
| 21 | **META** | 611.62 | - | **-** | 17 | - | NEG -$137.0M | 625.75 | 650 | 610 | +$10.2M | +$0 bull / -$56k bear | out (clean 28, ADX 15, RVol 0.7) |
| 22 | **GOOGL** | 283.07 | - | **-** | 17 | - | NEG -$96.3M | - | 285 | 290 | -$2.2M | +$0 bull / -$148k bear | out (clean 33, ADX 22, RVol 0.8) |
| 23 | **ARM** | 199.89 | - | **-** | 16 | - | NEG -$5.5M | - | 200 | 200 | +$297k | - | out (clean 26, ADX 41, RVol 1.3) |
| 24 | **UBER** | 66.65 | - | **-** | 15 | - | NEG -$12.9M | - | 70 | 65 | -$390k | - | out (clean 29, ADX 45, RVol 0.6) |
| 25 | **CRM** | 228.42 | - | **-** | 13 | - | NEG -$6.3M | 242.07 | 240 | 220 | +$109k | - | out (clean 28, ADX 36, RVol 0.7) |
| 26 | **IWM** | 280.15 | - | **-** | 10 | - | NEG -$1.2B | 286.91 | 285 | 270 | +$4.8M | - | out (clean 33, ADX 42, RVol 0.5) |
| 27 | **NFLX** | 62.66 | - | **-** | 9 | - | NEG -$20.1M | - | 63 | 60 | -$704k | - | out (clean 29, ADX 23, RVol 0.7) |

## Big prints this scan (111)
- **SPY** PUT 767 2026-11-04 (2DTE): 490 @ 13.47 = **+$660k** BUY | vol 5,969 / OI 36,998
- **AAPL** PUT 350 2026-11-04 (2DTE): 297 @ 14.94 = **+$444k** BUY | vol 1,667 / OI 6,659
- **SPY** PUT 767 2026-11-04 (2DTE): 230 @ 13.48 = **+$310k** BUY | vol 5,969 / OI 36,998
- **AAPL** PUT 342.5 2026-11-04 (2DTE): 297 @ 10.07 = **+$299k** BUY | vol 3,172 / OI 452
- **QQQ** PUT 705 2026-11-06 (4DTE): 125 @ 23.28 = **+$291k** BUY | vol 969 / OI 5,386
- **SPY** PUT 756 2026-11-02 (0DTE): 1,061 @ 2.59 = **+$275k** BUY | vol 295,159 / OI 1,385
- **QQQ** PUT 705 2026-11-02 (0DTE): 125 @ 20.89 = **+$261k** BUY | vol 1,742 / OI 1,897
- **SMH** PUT 530 2026-11-06 (4DTE): 75 @ 24.34 = **+$183k** BUY | vol 164 / OI 443
- **SPY** CALL 755 2026-11-02 (0DTE): 1,794 @ 1.00 = **+$179k** SELL | vol 53,715 / OI 59
- **QQQ** PUT 705 2026-11-09 (7DTE): 72 @ 24.06 = **+$173k** BUY | vol 143 / OI 503
- **QQQ** PUT 705 2026-11-03 (1DTE): 81 @ 21.10 = **+$171k** BUY | vol 413 / OI 646
- **SPY** PUT 755 2026-11-03 (1DTE): 407 @ 4.14 = **+$168k** BUY | vol 35,405 / OI 3,155
- **SPY** PUT 754 2026-11-03 (1DTE): 465 @ 3.41 = **+$159k** BUY | vol 23,041 / OI 2,581
- **QQQ** CALL 700 2026-11-06 (4DTE): 356 @ 4.26 = **+$152k** SELL | vol 18,885 / OI 1,051
- **QQQ** PUT 687 2026-11-06 (4DTE): 125 @ 12.12 = **+$152k** BUY | vol 1,051 / OI 337

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 717 2026-11-06 (4DTE): 555 traded vs OI 349
- **SPY** PUT 715 2026-11-05 (3DTE): 744 traded vs OI 743
- **SPY** CALL 747 2026-11-02 (0DTE): 510 traded vs OI 28
- **QQQ** CALL 706 2026-11-04 (2DTE): 502 traded vs OI 27
- **QQQ** PUT 655 2026-11-05 (3DTE): 535 traded vs OI 499
- **QQQ** PUT 684 2026-11-06 (4DTE): 584 traded vs OI 246
- **QQQ** PUT 650 2026-11-05 (3DTE): 687 traded vs OI 671
- **IWM** CALL 287 2026-11-06 (4DTE): 1,967 traded vs OI 1,026
- **IWM** PUT 277 2026-11-12 (10DTE): 515 traded vs OI 29
- **IWM** PUT 260 2026-11-09 (7DTE): 1,009 traded vs OI 927
- **META** CALL 650 2026-11-06 (4DTE): 2,338 traded vs OI 2,250
- **GOOGL** PUT 267.5 2026-11-06 (4DTE): 511 traded vs OI 0
- **AVGO** PUT 335 2026-11-02 (0DTE): 504 traded vs OI 270
- **PLTR** PUT 180 2026-11-06 (4DTE): 3,251 traded vs OI 3,137
- **DELL** PUT 415 2026-11-06 (4DTE): 501 traded vs OI 311

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
