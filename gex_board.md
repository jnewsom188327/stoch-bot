# GEX + FLOW SCAN - Fri Oct 30, 02:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:50:08 ET, last candle SPY 14:49, QQQ 14:49 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 12:45 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:32 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:31 | SPY | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 45 puts 0-1DTE > 1 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |
| 11:05 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 12:40 NVDA CALLS: under EMA 20 - flow says one way, price says the other
- 11:20 ARM CALLS: under EMA 20 - flow says one way, price says the other
- 11:20 COIN PUTS: price +0.22 over the last 15 min - flow says one way, price says the other
- 11:15 MSTR PUTS: price +1.54 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 11:10 MSTR PUTS: price +1.77 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 519.22 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 38 | none: 168 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (75 contracts' greeks worked out here) | POS +$233.6M | 516.31 | 525 | 520 | +$6.6M | +$141k bull / -$145k bear | out (clean 26, ADX 18, RVol 0.6) |
| 2 | **TSLA** | 395.64 | PINNED between the walls (positive gamma) - chop | **-** | 34 | - | POS +$369.5M | 387.93 | 395 | 395 | +$5.1M | +$0 bull / -$5.8M bear | out (clean 30, ADX 30, RVol 1.2) |
| 3 | **ORCL** | 130.09 | PINNED between the walls (positive gamma) - chop | **-** | 34 | - | POS +$27.2M | 128.94 | 130 | 130 | +$2.4M | +$57k bull / -$166k bear | out (clean 34, ADX 26, RVol 0.5) |
| 4 | **DELL** | 415.61 | - | **-** | 32 | - | NEG -$46.7M | - | 440 | 420 | +$10.0M | +$0 bull / -$29k bear | out (clean 34, ADX 44, RVol 1.2) |
| 5 | **SPY** | 751.16 | - | **-** | 29 | - | NEG -$17.2B | 772.07 | 750 | 750 | +$334.1M | +$30.7M bull / -$22.6M bear | out (clean 28, ADX 57, RVol 2.3) |
| 6 | **AMD** | 495.34 | - | **-** | 29 | - | NEG -$180.7M | 520.07 | 500 | 500 | +$38.5M | +$1.7M bull / -$1.1M bear | out (clean 30, ADX 45, RVol 1.9) |
| 7 | **SMH** | 513.30 | - | **-** | 28 | - | NEG -$643.2M | - | 532.5 | 505 | +$9.8M | +$448k bull / -$167k bear | out (clean 31, ADX 54, RVol 1.9) |
| 8 | **NVDA** | 201.53 | - | **-** | 27 | - | NEG -$462.4M | 212.15 | 210 | 200 | +$39.8M | +$2.3M bull / -$1.4M bear | out (clean 29, ADX 59, RVol 1.4) |
| 9 | **QQQ** | 684.49 | - | **-** | 26 | - | NEG -$9.0B | - | 720 | 690 | +$183.7M | +$11.2M bull / -$1.9M bear | out (clean 30, ADX 58, RVol 2.2) |
| 10 | **AVGO** | 320.35 | - | **-** | 25 | - | NEG -$164.9M | - | 340 | 320 | +$3.6M | +$27k bull / -$194k bear | out (clean 30, ADX 52, RVol 1.1) |
| 11 | **COIN** | 137.92 | - | **-** | 25 | - | NEG -$15.5M | - | 140 | 140 | -$1.5M | +$2.1M bull / +$0 bear | out (clean 28, ADX 48, RVol 3.2) |
| 12 | **MU** | 864.38 | - | **-** | 25 | - | NEG -$304.3M | 894.25 | 880 | 850 | +$77.0M | +$1.7M bull / -$1.4M bear | out (clean 31, ADX 46, RVol 0.7) |
| 13 | **HOOD** | 82.20 | - | **-** | 25 | - | NEG -$27.7M | - | 85 | 83 | +$2.3M | +$36k bull / -$46k bear | out (clean 32, ADX 52, RVol 1.1) |
| 14 | **AAPL** | 342.93 | - | **-** | 24 | - | POS +$125.7M | 341.69 | 345 | 345 | +$13.2M | +$266k bull / -$430k bear | out (clean 32, ADX 40, RVol 1.4) |
| 15 | **NFLX** | 61.76 | - | **-** | 23 | - | NEG -$40.5M | 62.63 | 62 | 62 | +$1.4M | +$0 bull / -$45k bear | out (clean 30, ADX 26, RVol 0.7) |
| 16 | **SHOP** | 155.28 | - | **-** | 23 | - | NEG -$16.3M | - | 155 | 157.5 | +$685k | - | out (clean 28, ADX 40, RVol 3.2) |
| 17 | **META** | 611.69 | - | **-** | 22 | - | NEG -$194.4M | 617.46 | 650 | 610 | +$9.1M | +$1.7M bull / +$0 bear | out (clean 30, ADX 46, RVol 0.4) |
| 18 | **GOOGL** | 277.32 | - | **-** | 22 | - | NEG -$209.8M | - | 280 | 280 | +$4.2M | +$238k bull / +$0 bear | out (clean 33, ADX 42, RVol 0.6) |
| 19 | **BABA** | 97.56 | - | **-** | 20 | - | NEG -$44.4M | 98.77 | 100 | 98 | +$662k | - | out (clean 31, ADX 41, RVol 0.7) |
| 20 | **SMCI** | 31.58 | - | **-** | 19 | - | NEG -$4.2M | 32.62 | 32 | 32 | +$955k | - | out (clean 30, ADX 51, RVol 1.1) |
| 21 | **MSTR** | 128.63 | - | **-** | 18 | - | NEG -$33.9M | - | 135 | 130 | -$2.0M | +$1.4M bull / +$0 bear | out (clean 29, ADX 30, RVol 0.8) |
| 22 | **PLTR** | 184.36 | - | **-** | 17 | - | NEG -$80.5M | 192.6 | 185 | 185 | +$1.6M | +$0 bull / -$2.3M bear | out (clean 26, ADX 28, RVol 0.7) |
| 23 | **ARM** | 199.94 | - | **-** | 17 | - | NEG -$16.5M | - | 200 | 200 | +$887k | - | out (clean 26, ADX 37, RVol 1.9) |
| 24 | **AMZN** | 237.41 | - | **-** | 16 | - | NEG -$189.1M | 245.11 | 250 | 240 | -$1.9M | +$2.2M bull / -$122k bear | out (clean 30, ADX 14, RVol 1.4) |
| 25 | **IWM** | 277.25 | - | **-** | 15 | - | NEG -$1.6B | 281.19 | 278 | 278 | +$14.2M | - | out (clean 30, ADX 50, RVol 0.9) |
| 26 | **UBER** | 64.99 | - | **-** | 12 | - | NEG -$41.8M | 66.04 | 65 | 65 | +$317k | - | out (clean 27, ADX 16, RVol 0.5) |
| 27 | **CRM** | 229.43 | - | **-** | 12 | - | NEG -$29.0M | 240.32 | 230 | 230 | +$302k | - | out (clean 27, ADX 28, RVol 1.0) |

## Big prints this scan (182)
- **SPY** PUT 736 2026-11-03 (4DTE): 7,167 @ 1.80 = **+$1.3M** BUY | vol 20,808 / OI 326
- **AMZN** CALL 240 2026-11-06 (7DTE): 1,500 @ 4.31 = **+$646k** BUY | vol 15,052 / OI 729
- **AMZN** CALL 240 2026-11-06 (7DTE): 1,500 @ 4.31 = **+$646k** BUY | vol 15,052 / OI 729
- **SPY** PUT 760 2026-11-06 (7DTE): 455 @ 13.00 = **+$592k** BUY | vol 13,075 / OI 12,995
- **SPY** PUT 762 2026-11-06 (7DTE): 400 @ 13.80 = **+$552k** SELL | vol 1,877 / OI 7,224
- **SPY** PUT 760 2026-11-06 (7DTE): 399 @ 13.10 = **+$523k** BUY | vol 13,075 / OI 12,995
- **QQQ** PUT 697 2026-10-30 (0DTE): 383 @ 11.93 = **+$457k** SELL | vol 64,092 / OI 2,680
- **AMZN** CALL 245 2026-11-06 (7DTE): 1,500 @ 2.47 = **+$370k** BUY | vol 19,309 / OI 833
- **AMZN** CALL 245 2026-11-06 (7DTE): 1,500 @ 2.47 = **+$370k** BUY | vol 19,309 / OI 833
- **SPY** PUT 739 2026-11-04 (5DTE): 1,027 @ 3.20 = **+$329k** BUY | vol 37,274 / OI 128
- **SPY** PUT 767 2026-11-04 (5DTE): 200 @ 16.36 = **+$327k** SELL | vol 25,385 / OI 29,783
- **META** PUT 610 2026-11-04 (5DTE): 267 @ 10.51 = **+$281k** SELL | vol 2,381 / OI 101
- **QQQ** PUT 692 2026-10-30 (0DTE): 388 @ 7.21 = **+$280k** SELL | vol 193,003 / OI 2,435
- **QQQ** PUT 681 2026-11-02 (3DTE): 548 @ 5.08 = **+$278k** SELL | vol 7,278 / OI 0
- **QQQ** PUT 675 2026-11-02 (3DTE): 969 @ 2.82 = **+$273k** SELL | vol 22,409 / OI 4,676

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 730 2026-11-03 (4DTE): 904 traded vs OI 715
- **SPY** PUT 700 2026-11-02 (3DTE): 2,871 traded vs OI 2,788
- **SPY** CALL 783 2026-11-03 (4DTE): 2,558 traded vs OI 2,288
- **SPY** PUT 732 2026-11-03 (4DTE): 628 traded vs OI 208
- **SPY** PUT 727 2026-11-04 (5DTE): 513 traded vs OI 61
- **SPY** PUT 742 2026-10-30 (0DTE): 12,983 traded vs OI 11,667
- **SPY** PUT 731 2026-11-03 (4DTE): 785 traded vs OI 715
- **SPY** CALL 751 2026-11-06 (7DTE): 562 traded vs OI 48
- **SPY** PUT 716 2026-11-20 (21DTE): 13,012 traded vs OI 1,591
- **SPY** PUT 712 2026-11-20 (21DTE): 1,823 traded vs OI 1,690
- **SPY** PUT 739 2026-11-06 (7DTE): 1,278 traded vs OI 1,262
- **SPY** CALL 800 2026-11-12 (13DTE): 512 traded vs OI 0
- **SPY** CALL 761 2026-11-20 (21DTE): 1,332 traded vs OI 1,328
- **SPY** PUT 760 2026-11-06 (7DTE): 13,075 traded vs OI 12,995
- **SPY** CALL 758 2026-11-20 (21DTE): 517 traded vs OI 440

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
