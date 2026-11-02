# GEX + FLOW SCAN - Mon Nov 02, 02:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 1.48 | +291% (43m) | **+128%** (done) | +11% | 692.76 hit |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 1.27 | +111% (58m) | **+79%** (done) | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:00:08 ET, last candle SPY 13:59, QQQ 13:59 | no errors
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
| 1 | **MU** | 842.78 | FLOW SURGE | **CALLS** | 41 | none: 135 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (56 contracts' greeks worked out here) | NEG -$225.5M | - | 910 | 850 | +$155.5M | +$3.2M bull / +$0 bear | out (clean 30, ADX 44, RVol 0.7) |
| 2 | **SMCI** | 31.16 | TREND (flow not with it) | **PUTS** | 38 | none: 12 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$472k | - | 34 | 30 | +$752k | - | SHORT (clean 35, ADX 47, RVol 1.2) |
| 3 | **AMD** | 477.77 | - | **-** | 26 | - | NEG -$76.0M | - | 500 | 480 | +$43.2M | +$2.4M bull / -$144k bear | out (clean 32, ADX 48, RVol 0.7) |
| 4 | **SMH** | 515.66 | - | **-** | 25 | - | NEG -$347.7M | - | 532.5 | 500 | +$4.4M | +$173k bull / +$0 bear | out (clean 31, ADX 32, RVol 0.9) |
| 5 | **AAPL** | 337.31 | - | **-** | 24 | - | NEG -$452k | 336.98 | 350 | 330 | +$22.5M | +$0 bull / -$512k bear | out (clean 31, ADX 35, RVol 0.9) |
| 6 | **DELL** | 402.89 | TREND (flow not with it) | **PUTS** | 22 | none: 32 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$20.7M | - | 440 | 400 | +$1.0M | - | SHORT (clean 33, ADX 32, RVol 0.5) |
| 7 | **AMZN** | 249.16 | - | **-** | 21 | - | POS +$73.5M | 242.89 | 250 | 250 | -$20.2M | +$242k bull / +$0 bear | out (clean 33, ADX 27, RVol 0.5) |
| 8 | **NFLX** | 62.83 | - | **-** | 21 | - | NEG -$19.2M | - | 63 | 60 | -$657k | +$0 bull / -$63k bear | out (clean 29, ADX 31, RVol 0.7) |
| 9 | **QQQ** | 688.48 | - | **-** | 19 | - | NEG -$5.5B | - | 720 | 680 | +$90.6M | +$7.7M bull / +$0 bear | out (clean 30, ADX 31, RVol 0.5) |
| 10 | **MSFT** | 517.76 | - | **-** | 19 | - | POS +$174.4M | 502.52 | 540 | 500 | -$554k | +$205k bull / +$0 bear | out (clean 27, ADX 37, RVol 0.8) |
| 11 | **TSLA** | 407.00 | - | **-** | 18 | - | POS +$283.0M | - | 410 | 400 | -$66.5M | +$540k bull / -$32k bear | out (clean 30, ADX 20, RVol 0.6) |
| 12 | **PLTR** | 183.45 | - | **-** | 18 | - | NEG -$11.0M | - | 200 | 180 | +$2.8M | +$128k bull / +$0 bear | out (clean 25, ADX 18, RVol 0.9) |
| 13 | **MSTR** | 132.81 | - | **-** | 18 | - | POS +$2.0M | - | 135 | 125 | +$3.6M | +$0 bull / -$86k bear | out (clean 26, ADX 15, RVol 0.6) |
| 14 | **ORCL** | 121.41 | - | **-** | 18 | - | NEG -$36.4M | - | 130 | 120 | +$162k | +$134k bull / -$64k bear | out (clean 32, ADX 36, RVol 0.8) |
| 15 | **SPY** | 757.09 | - | **-** | 17 | - | NEG -$10.4B | 775.26 | 800 | 750 | +$52.9M | +$3.4M bull / +$0 bear | out (clean 30, ADX 28, RVol 0.6) |
| 16 | **IWM** | 280.49 | - | **-** | 17 | - | NEG -$1.2B | 286.83 | 285 | 270 | +$2.2M | +$290k bull / +$0 bear | out (clean 32, ADX 28, RVol 0.7) |
| 17 | **NVDA** | 205.50 | - | **-** | 17 | - | NEG -$226.2M | 215.55 | 210 | 205 | +$10.1M | +$355k bull / +$0 bear | out (clean 28, ADX 21, RVol 0.8) |
| 18 | **META** | 612.42 | - | **-** | 16 | - | NEG -$130.0M | 625.25 | 650 | 610 | +$8.6M | +$600k bull / -$143k bear | out (clean 29, ADX 19, RVol 0.3) |
| 19 | **GOOGL** | 283.67 | - | **-** | 16 | - | NEG -$77.9M | - | 285 | 285 | -$3.6M | +$300k bull / +$0 bear | out (clean 34, ADX 18, RVol 0.4) |
| 20 | **SHOP** | 159.20 | - | **-** | 16 | - | NEG -$394k | - | 175 | 175 | -$637k | - | out (clean 28, ADX 19, RVol 1.5) |
| 21 | **BABA** | 102.80 | - | **-** | 14 | - | POS +$2.0M | 101.19 | 105 | 100 | -$1.0M | - | out (clean 33, ADX 21, RVol 1.0) |
| 22 | **ARM** | 200.88 | - | **-** | 12 | - | NEG -$6.8M | - | 220 | 200 | +$277k | - | out (clean 25, ADX 23, RVol 0.8) |
| 23 | **UBER** | 67.05 | - | **-** | 12 | - | NEG -$8.5M | - | 70 | 65 | -$456k | - | out (clean 27, ADX 24, RVol 0.6) |
| 24 | **AVGO** | 326.95 | - | **-** | 8 | - | NEG -$107.9M | - | 340 | 330 | -$4.3M | - | out (clean 30, ADX 22, RVol 0.3) |
| 25 | **COIN** | 138.63 | - | **-** | 8 | - | NEG -$7.8M | - | 150 | 130 | -$289k | - | out (clean 23, ADX 18, RVol 0.8) |
| 26 | **CRM** | 230.11 | - | **-** | 8 | - | NEG -$6.0M | 242.51 | 240 | 220 | +$54k | - | out (clean 27, ADX 16, RVol 1.3) |
| 27 | **HOOD** | 84.47 | - | **-** | 7 | - | NEG -$11.3M | - | 85 | 90 | -$85k | - | out (clean 32, ADX 32, RVol 0.5) |

## Big prints this scan (103)
- **QQQ** PUT 682 2026-11-04 (2DTE): 2,000 @ 4.61 = **+$922k** SELL | vol 6,452 / OI 0
- **QQQ** PUT 682 2026-11-04 (2DTE): 1,950 @ 4.69 = **+$915k** SELL | vol 6,452 / OI 0
- **QQQ** PUT 675 2026-11-04 (2DTE): 2,000 @ 2.76 = **+$552k** SELL | vol 9,265 / OI 442
- **QQQ** PUT 675 2026-11-04 (2DTE): 1,950 @ 2.82 = **+$550k** SELL | vol 9,265 / OI 442
- **QQQ** PUT 696 2026-11-02 (0DTE): 493 @ 6.50 = **+$320k** SELL | vol 79,127 / OI 0
- **SPY** PUT 767 2026-11-04 (2DTE): 250 @ 10.55 = **+$264k** SELL | vol 3,709 / OI 36,998
- **AMD** PUT 475 2026-11-04 (2DTE): 129 @ 19.20 = **+$248k** SELL | vol 455 / OI 116
- **QQQ** PUT 700 2026-11-03 (1DTE): 200 @ 11.57 = **+$231k** SELL | vol 7,960 / OI 1,423
- **QQQ** PUT 685 2026-11-05 (3DTE): 300 @ 7.08 = **+$212k** SELL | vol 3,159 / OI 1,896
- **QQQ** PUT 685 2026-11-05 (3DTE): 300 @ 7.08 = **+$212k** SELL | vol 3,159 / OI 1,896
- **SPY** PUT 758 2026-11-02 (0DTE): 1,294 @ 1.62 = **+$210k** SELL | vol 367,554 / OI 1,174
- **SPY** PUT 758 2026-11-02 (0DTE): 1,749 @ 1.07 = **+$187k** SELL | vol 367,554 / OI 1,174
- **QQQ** PUT 697 2026-11-03 (1DTE): 200 @ 9.00 = **+$180k** SELL | vol 7,815 / OI 0
- **QQQ** PUT 680 2026-11-04 (2DTE): 426 @ 4.15 = **+$177k** SELL | vol 6,339 / OI 670
- **MU** CALL 880 2026-11-09 (7DTE): 103 @ 16.83 = **+$173k** BUY | vol 522 / OI 7

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 785 2026-11-06 (4DTE): 4,320 traded vs OI 3,659
- **SPY** CALL 761 2026-11-30 (28DTE): 576 traded vs OI 567
- **QQQ** CALL 724 2026-11-06 (4DTE): 659 traded vs OI 632
- **QQQ** PUT 620 2026-11-06 (4DTE): 759 traded vs OI 0
- **QQQ** PUT 678 2026-11-06 (4DTE): 2,033 traded vs OI 672
- **QQQ** CALL 725 2026-11-06 (4DTE): 6,939 traded vs OI 6,936
- **QQQ** CALL 722 2026-11-04 (2DTE): 570 traded vs OI 533
- **QQQ** PUT 677 2026-11-04 (2DTE): 514 traded vs OI 0
- **QQQ** PUT 620 2026-11-03 (1DTE): 648 traded vs OI 0
- **QQQ** CALL 688 2026-11-03 (1DTE): 547 traded vs OI 0
- **IWM** PUT 274 2026-11-03 (1DTE): 505 traded vs OI 404
- **NVDA** PUT 185 2026-11-20 (18DTE): 2,048 traded vs OI 0
- **NVDA** PUT 185 2026-11-06 (4DTE): 3,317 traded vs OI 0
- **NVDA** PUT 185 2026-11-09 (7DTE): 1,564 traded vs OI 0
- **NVDA** PUT 185 2026-11-02 (0DTE): 1,067 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
