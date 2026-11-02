# GEX + FLOW SCAN - Mon Nov 02, 02:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 1.48 | +291% (43m) | **+128%** (done) | +11% | 692.76 hit |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 1.27 | +111% (58m) | **+79%** (done) | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (7 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:40:08 ET, last candle SPY 14:39, QQQ 14:39 | no errors
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
| 1 | **MU** | 837.07 | FLOW SURGE | **CALLS** | 42 | none: 133 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (56 contracts' greeks worked out here) | NEG -$214.8M | - | 910 | 850 | +$172.0M | +$2.6M bull / -$56k bear | out (clean 32, ADX 50, RVol 0.8) |
| 2 | **SMH** | 510.67 | FLOW SURGE | **CALLS** | 41 | none: 162 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (66 contracts' greeks worked out here) | NEG -$333.4M | - | 532.5 | 500 | +$7.8M | +$933k bull / +$0 bear | out (clean 32, ADX 49, RVol 0.7) |
| 3 | **SMCI** | 30.62 | TREND (flow not with it) | **PUTS** | 38 | none: 12 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$557k | - | 33 | 30 | +$917k | - | SHORT (clean 36, ADX 55, RVol 1.2) |
| 4 | **BABA** | 102.23 | TREND + FLOW | **PUTS** | 33 | none: 20 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$919k | 101.43 | 105 | 100 | -$962k | - | SHORT (clean 33, ADX 31, RVol 0.6) |
| 5 | **DELL** | 398.62 | TREND (flow not with it) | **PUTS** | 29 | none: 31 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$19.4M | - | 430 | 400 | +$2.6M | - | SHORT (clean 34, ADX 43, RVol 0.7) |
| 6 | **AMD** | 471.75 | - | **-** | 28 | - | NEG -$63.4M | - | 500 | 480 | +$53.6M | +$1.4M bull / +$0 bear | out (clean 32, ADX 59, RVol 1.1) |
| 7 | **QQQ** | 684.61 | - | **-** | 24 | - | NEG -$5.4B | - | 720 | 680 | +$182.4M | +$4.4M bull / +$0 bear | out (clean 32, ADX 48, RVol 1.1) |
| 8 | **AAPL** | 337.06 | - | **-** | 24 | - | NEG -$3.1M | 337.02 | 350 | 330 | +$24.2M | +$265k bull / -$569k bear | out (clean 31, ADX 31, RVol 1.4) |
| 9 | **SHOP** | 157.50 | - | **-** | 24 | - | NEG -$416k | - | 170 | 160 | -$516k | +$145k bull / +$0 bear | out (clean 29, ADX 23, RVol 1.4) |
| 10 | **SPY** | 754.12 | - | **-** | 23 | - | NEG -$10.4B | 775.31 | 770 | 750 | +$156.2M | +$4.6M bull / +$0 bear | out (clean 31, ADX 45, RVol 1.0) |
| 11 | **NVDA** | 203.46 | - | **-** | 22 | - | NEG -$236.0M | - | 210 | 200 | +$18.9M | +$820k bull / +$0 bear | out (clean 30, ADX 38, RVol 1.1) |
| 12 | **AMZN** | 247.88 | - | **-** | 22 | - | POS +$51.1M | 243.63 | 250 | 250 | -$17.1M | +$609k bull / +$0 bear | out (clean 34, ADX 40, RVol 0.6) |
| 13 | **PLTR** | 181.75 | - | **-** | 21 | - | NEG -$14.2M | - | 190 | 180 | +$4.2M | +$1.1M bull / +$0 bear | out (clean 26, ADX 31, RVol 1.1) |
| 14 | **ORCL** | 119.74 | - | **-** | 21 | - | NEG -$35.2M | - | 130 | 120 | +$999k | +$26k bull / +$0 bear | out (clean 32, ADX 43, RVol 0.9) |
| 15 | **IWM** | 279.72 | - | **-** | 20 | - | NEG -$1.3B | 287.06 | 285 | 270 | +$4.8M | +$96k bull / +$0 bear | out (clean 33, ADX 39, RVol 0.6) |
| 16 | **TSLA** | 403.75 | - | **-** | 20 | - | POS +$220.4M | - | 405 | 400 | -$44.7M | +$3.3M bull / +$0 bear | out (clean 31, ADX 33, RVol 0.9) |
| 17 | **MSFT** | 514.86 | - | **-** | 20 | - | POS +$125.6M | 502.38 | 540 | 500 | +$1.9M | +$347k bull / +$0 bear | out (clean 28, ADX 48, RVol 0.6) |
| 18 | **AVGO** | 324.25 | - | **-** | 19 | - | NEG -$116.5M | - | 340 | 320 | -$2.1M | +$28k bull / -$41k bear | out (clean 32, ADX 37, RVol 0.6) |
| 19 | **META** | 609.94 | - | **-** | 17 | - | NEG -$144.8M | 625.16 | 650 | 610 | +$10.6M | +$144k bull / +$0 bear | out (clean 28, ADX 16, RVol 0.6) |
| 20 | **GOOGL** | 281.94 | - | **-** | 15 | - | NEG -$105.4M | - | 285 | 280 | -$2.1M | +$244k bull / +$0 bear | out (clean 33, ADX 18, RVol 0.5) |
| 21 | **ARM** | 198.59 | - | **-** | 15 | - | NEG -$5.7M | - | 200 | 200 | +$311k | - | out (clean 26, ADX 38, RVol 0.8) |
| 22 | **UBER** | 66.61 | - | **-** | 15 | - | NEG -$13.5M | - | 70 | 65 | -$394k | - | out (clean 28, ADX 38, RVol 1.1) |
| 23 | **CRM** | 227.62 | - | **-** | 12 | - | NEG -$7.4M | - | 240 | 220 | +$104k | - | out (clean 28, ADX 33, RVol 0.8) |
| 24 | **MSTR** | 130.70 | - | **-** | 11 | - | POS +$1.5M | - | 135 | 125 | +$4.6M | - | out (clean 26, ADX 23, RVol 0.8) |
| 25 | **HOOD** | 83.69 | - | **-** | 11 | - | NEG -$11.1M | - | 85 | 90 | +$599k | - | out (clean 32, ADX 42, RVol 0.8) |
| 26 | **NFLX** | 62.45 | - | **-** | 9 | - | NEG -$21.5M | - | 63 | 60 | -$605k | - | out (clean 29, ADX 27, RVol 0.8) |
| 27 | **COIN** | 136.11 | - | **-** | 9 | - | NEG -$6.2M | - | 140 | 130 | -$130k | - | out (clean 24, ADX 34, RVol 0.9) |

## Big prints this scan (150)
- **SPY** PUT 760 2026-11-02 (0DTE): 1,995 @ 4.83 = **+$964k** SELL | vol 346,463 / OI 6,923
- **SPY** PUT 759 2026-11-02 (0DTE): 1,995 @ 3.94 = **+$786k** SELL | vol 325,077 / OI 2,439
- **QQQ** CALL 715 2026-11-06 (4DTE): 4,500 @ 1.29 = **+$580k** BUY | vol 9,425 / OI 10,865
- **AMZN** PUT 245 2026-11-06 (4DTE): 1,500 @ 3.00 = **+$450k** SELL | vol 7,249 / OI 3,184
- **TSLA** CALL 397.5 2026-11-04 (2DTE): 315 @ 12.14 = **+$382k** BUY | vol 2,028 / OI 190
- **TSLA** CALL 400 2026-11-04 (2DTE): 315 @ 10.54 = **+$332k** BUY | vol 6,209 / OI 612
- **SPY** PUT 767 2026-11-04 (2DTE): 250 @ 12.64 = **+$316k** SELL | vol 5,216 / OI 36,998
- **TSLA** CALL 405 2026-11-04 (2DTE): 405 @ 7.65 = **+$310k** BUY | vol 7,797 / OI 594
- **SPY** PUT 767 2026-11-04 (2DTE): 250 @ 12.00 = **+$300k** SELL | vol 5,216 / OI 36,998
- **TSLA** CALL 407.5 2026-11-04 (2DTE): 405 @ 6.40 = **+$259k** BUY | vol 6,774 / OI 461
- **GOOGL** PUT 272.5 2026-11-06 (4DTE): 2,000 @ 1.22 = **+$244k** SELL | vol 2,414 / OI 0
- **QQQ** PUT 697 2026-11-03 (1DTE): 200 @ 12.00 = **+$240k** SELL | vol 9,453 / OI 0
- **QQQ** PUT 697 2026-11-03 (1DTE): 200 @ 11.55 = **+$231k** SELL | vol 9,453 / OI 0
- **QQQ** CALL 715 2026-11-06 (4DTE): 1,500 @ 1.28 = **+$192k** BUY | vol 9,425 / OI 10,865
- **AMD** PUT 470 2026-11-04 (2DTE): 92 @ 19.80 = **+$182k** SELL | vol 1,053 / OI 70

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 772 2026-11-06 (4DTE): 1,845 traded vs OI 1,755
- **SPY** PUT 745 2026-11-04 (2DTE): 1,465 traded vs OI 1,423
- **SPY** PUT 740 2026-11-05 (3DTE): 1,799 traded vs OI 1,789
- **SPY** PUT 730 2026-11-06 (4DTE): 6,641 traded vs OI 6,604
- **SPY** CALL 760 2026-11-16 (14DTE): 500 traded vs OI 0
- **QQQ** CALL 703 2026-11-06 (4DTE): 506 traded vs OI 197
- **QQQ** CALL 728 2026-11-03 (1DTE): 878 traded vs OI 526
- **QQQ** CALL 686 2026-11-04 (2DTE): 544 traded vs OI 0
- **QQQ** CALL 682 2026-11-02 (0DTE): 517 traded vs OI 0
- **QQQ** CALL 683 2026-11-02 (0DTE): 626 traded vs OI 0
- **QQQ** PUT 640 2026-11-06 (4DTE): 1,991 traded vs OI 1,805
- **IWM** CALL 305 2026-11-27 (25DTE): 501 traded vs OI 183
- **NVDA** PUT 217.5 2026-11-13 (11DTE): 542 traded vs OI 411
- **NVDA** CALL 222.5 2026-11-04 (2DTE): 1,353 traded vs OI 1,297
- **TSLA** PUT 407.5 2026-11-09 (7DTE): 501 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
