# GEX + FLOW SCAN - Mon Nov 02, 03:05 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 1.48 | +291% (43m) | **+128%** (done) | +11% | 692.76 hit |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 1.27 | +111% (58m) | **+79%** (done) | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (7 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:05:08 ET, last candle SPY 15:04, QQQ 15:04 | no errors
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
| 1 | **TSLA** | 404.35 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 40 | 11/02 402.5P @ 0.41 (delta 0.25) = est +508% at 400 | POS +$244.3M | - | 405 | 400 | -$33.7M | +$1.1M bull / -$1.5M bear | out (clean 32, ADX 39, RVol 1.0) |
| 2 | **SMCI** | 30.87 | TREND (flow not with it) | **PUTS** | 37 | none: 12 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$532k | - | 33 | 30 | +$880k | - | SHORT (clean 36, ADX 53, RVol 1.1) |
| 3 | **BABA** | 102.30 | TREND + FLOW | **PUTS** | 33 | none: 20 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$1.4M | 101.19 | 105 | 100 | -$943k | - | SHORT (clean 33, ADX 37, RVol 0.5) |
| 4 | **MU** | 838.24 | - | **-** | 30 | - | NEG -$202.7M | - | 910 | 850 | +$179.8M | +$1.2M bull / -$2.4M bear | out (clean 32, ADX 53, RVol 1.1) |
| 5 | **SMH** | 512.28 | - | **-** | 29 | - | NEG -$322.1M | - | 532.5 | 500 | +$8.3M | +$36k bull / -$725k bear | out (clean 33, ADX 54, RVol 1.1) |
| 6 | **AMD** | 474.18 | - | **-** | 26 | - | NEG -$68.5M | - | 500 | 480 | +$49.4M | +$816k bull / -$2.2M bear | out (clean 33, ADX 60, RVol 1.0) |
| 7 | **SPY** | 755.34 | - | **-** | 24 | - | NEG -$10.5B | 775.53 | 770 | 750 | +$158.3M | +$113k bull / -$4.6M bear | out (clean 31, ADX 48, RVol 1.3) |
| 8 | **QQQ** | 685.65 | - | **-** | 24 | - | NEG -$5.5B | - | 720 | 680 | +$186.5M | +$674k bull / -$3.2M bear | out (clean 32, ADX 52, RVol 1.0) |
| 9 | **NVDA** | 204.08 | - | **-** | 23 | - | NEG -$238.0M | - | 210 | 205 | +$20.9M | +$0 bull / -$657k bear | out (clean 30, ADX 42, RVol 1.1) |
| 10 | **AMZN** | 248.56 | - | **-** | 23 | - | POS +$62.7M | 242.96 | 250 | 250 | -$17.6M | +$36k bull / -$140k bear | out (clean 34, ADX 43, RVol 0.7) |
| 11 | **PLTR** | 181.31 | - | **-** | 23 | - | NEG -$13.7M | - | 190 | 180 | +$4.7M | +$285k bull / -$166k bear | out (clean 26, ADX 41, RVol 0.9) |
| 12 | **AAPL** | 338.31 | - | **-** | 22 | - | POS +$20.5M | 336.97 | 350 | 330 | +$20.3M | +$0 bull / -$1.4M bear | out (clean 31, ADX 26, RVol 1.3) |
| 13 | **MSFT** | 514.10 | - | **-** | 22 | - | POS +$120.1M | 502.28 | 535 | 500 | +$3.1M | +$91k bull / +$0 bear | out (clean 28, ADX 53, RVol 0.9) |
| 14 | **DELL** | 400.15 | - | **-** | 22 | - | NEG -$20.1M | - | 440 | 400 | +$2.3M | +$0 bull / -$90k bear | out (clean 34, ADX 44, RVol 0.7) |
| 15 | **MSTR** | 131.22 | - | **-** | 22 | - | POS +$1.8M | - | 135 | 125 | +$4.5M | +$27k bull / +$0 bear | out (clean 26, ADX 31, RVol 0.7) |
| 16 | **SHOP** | 157.15 | - | **-** | 22 | - | NEG -$407k | - | 170 | 160 | -$329k | +$32k bull / +$0 bear | out (clean 30, ADX 30, RVol 1.3) |
| 17 | **HOOD** | 84.10 | - | **-** | 21 | - | NEG -$11.3M | - | 85 | 90 | +$766k | +$0 bull / -$63k bear | out (clean 32, ADX 39, RVol 1.0) |
| 18 | **COIN** | 136.91 | - | **-** | 20 | - | NEG -$7.5M | - | 150 | 130 | -$197k | +$0 bull / -$45k bear | out (clean 25, ADX 40, RVol 0.7) |
| 19 | **ORCL** | 119.53 | - | **-** | 20 | - | NEG -$36.1M | - | 130 | 120 | +$642k | +$178k bull / -$38k bear | out (clean 33, ADX 44, RVol 0.9) |
| 20 | **AVGO** | 325.72 | - | **-** | 19 | - | NEG -$111.4M | - | 340 | 330 | -$2.1M | +$0 bull / -$65k bear | out (clean 32, ADX 38, RVol 0.5) |
| 21 | **META** | 612.83 | - | **-** | 17 | - | NEG -$131.3M | 626.19 | 650 | 610 | +$9.6M | +$0 bull / -$163k bear | out (clean 28, ADX 15, RVol 0.8) |
| 22 | **GOOGL** | 283.25 | - | **-** | 17 | - | NEG -$88.7M | - | 285 | 285 | -$2.5M | +$0 bull / -$184k bear | out (clean 33, ADX 21, RVol 0.8) |
| 23 | **ARM** | 199.83 | - | **-** | 16 | - | NEG -$5.6M | - | 200 | 200 | +$295k | - | out (clean 26, ADX 40, RVol 1.6) |
| 24 | **UBER** | 66.61 | - | **-** | 15 | - | NEG -$13.3M | - | 70 | 65 | -$394k | - | out (clean 29, ADX 44, RVol 0.7) |
| 25 | **CRM** | 227.80 | - | **-** | 13 | - | NEG -$7.5M | - | 240 | 220 | +$108k | - | out (clean 28, ADX 35, RVol 0.9) |
| 26 | **IWM** | 280.14 | - | **-** | 10 | - | NEG -$1.2B | 286.88 | 285 | 270 | +$5.0M | - | out (clean 33, ADX 40, RVol 0.7) |
| 27 | **NFLX** | 62.58 | - | **-** | 9 | - | NEG -$21.6M | - | 63 | 60 | -$715k | - | out (clean 29, ADX 21, RVol 0.8) |

## Big prints this scan (90)
- **MU** CALL 865 2026-11-06 (4DTE): 399 @ 16.00 = **+$638k** SELL | vol 1,795 / OI 39
- **SPY** PUT 756 2026-11-04 (2DTE): 1,000 @ 6.30 = **+$630k** BUY | vol 26,837 / OI 149
- **SPY** CALL 755 2026-11-05 (3DTE): 995 @ 5.85 = **+$582k** SELL | vol 7,385 / OI 87
- **QQQ** PUT 685 2026-11-04 (2DTE): 581 @ 9.00 = **+$523k** BUY | vol 13,012 / OI 935
- **TSLA** CALL 410 2026-11-04 (2DTE): 400 @ 4.45 = **+$178k** SELL | vol 17,614 / OI 1,575
- **QQQ** PUT 685 2026-11-04 (2DTE): 177 @ 9.00 = **+$159k** BUY | vol 13,012 / OI 935
- **SPY** CALL 754 2026-11-02 (0DTE): 978 @ 1.60 = **+$156k** SELL | vol 36,905 / OI 20
- **MU** PUT 840 2026-11-06 (4DTE): 50 @ 30.91 = **+$155k** BUY | vol 1,708 / OI 868
- **MU** PUT 850 2026-11-02 (0DTE): 101 @ 15.17 = **+$153k** BUY | vol 50,221 / OI 658
- **SPY** PUT 754 2026-11-03 (1DTE): 389 @ 3.93 = **+$153k** BUY | vol 25,608 / OI 2,581
- **SPY** PUT 756 2026-11-04 (2DTE): 250 @ 6.05 = **+$151k** BUY | vol 26,837 / OI 149
- **QQQ** PUT 687 2026-11-02 (0DTE): 300 @ 4.55 = **+$136k** BUY | vol 129,507 / OI 0
- **MU** PUT 830 2026-11-06 (4DTE): 50 @ 26.16 = **+$131k** BUY | vol 1,143 / OI 521
- **QQQ** PUT 684 2026-11-03 (1DTE): 200 @ 6.20 = **+$124k** BUY | vol 9,570 / OI 0
- **SPY** PUT 756 2026-11-04 (2DTE): 188 @ 6.51 = **+$122k** BUY | vol 26,837 / OI 149

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 751 2026-11-03 (1DTE): 518 traded vs OI 34
- **SPY** PUT 740 2026-11-03 (1DTE): 6,406 traded vs OI 6,249
- **SPY** PUT 735 2026-11-03 (1DTE): 1,198 traded vs OI 1,186
- **SPY** CALL 779 2026-11-06 (4DTE): 1,049 traded vs OI 1,047
- **SPY** CALL 758 2026-11-13 (11DTE): 501 traded vs OI 190
- **SPY** CALL 765 2026-11-16 (14DTE): 598 traded vs OI 0
- **SPY** PUT 716 2026-11-20 (18DTE): 3,103 traded vs OI 2,586
- **SPY** CALL 825 2026-11-13 (11DTE): 1,096 traded vs OI 1,079
- **QQQ** PUT 681 2026-11-06 (4DTE): 515 traded vs OI 111
- **QQQ** CALL 683 2026-11-03 (1DTE): 861 traded vs OI 0
- **QQQ** CALL 682 2026-11-03 (1DTE): 610 traded vs OI 0
- **QQQ** CALL 680 2026-11-06 (4DTE): 507 traded vs OI 170
- **QQQ** CALL 735 2026-11-06 (4DTE): 12,357 traded vs OI 7,342
- **QQQ** PUT 665 2026-11-09 (7DTE): 603 traded vs OI 192
- **QQQ** CALL 725 2026-11-04 (2DTE): 983 traded vs OI 973

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
