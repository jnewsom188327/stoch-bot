# GEX + FLOW SCAN - Thu Nov 12, 11:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:35 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 754P | 0.59 | 0.17 | +10% (1m) | **-71%** (done) | +70% | 755 |
| 09:50 | **HOOD** | **PUTS** | TREND + FLOW | 11/13 79P | 0.55 | 0.36 | +5% (19m) | **-35%** (done) | +92% | 80 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 130C | 0.75 | 0.72 | +4% (60m) | **-4%** (done) | +59% | 126.9 |
| 09:45 | **SMCI** | **PUTS** | TREND + FLOW | 11/13 27P | 0.42 | 0.23 | -5% (6m) | **-45%** (done) | +57% | 27 |
| 09:45 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 753P | 0.79 | 0.31 | +23% (18m) | **-61%** (done) | +51% | 754.88 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:40:08 ET, last candle SPY 11:39, QQQ 11:39 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:03 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (3 today, last 5)
- 10:30 IWM CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:25 IWM CALLS: price -0.79 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:20 IWM CALLS: price -0.12 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **GOOGL** | 299.45 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 47 | none: 72 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | POS +$129.2M | 288.73 | 300 | 290 | -$3.6M | +$146k bull / -$28k bear | out (clean 29, ADX 31, RVol 1.7) |
| 2 | **AMD** | 587.37 | TREND (flow not with it) | **CALLS** | 36 | none: 139 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$193.8M | - | 600 | 550 | -$33.5M | +$4.8M bull / -$4.9M bear | LONG (clean 34, ADX 39, RVol 1.7) |
| 3 | **AMZN** | 269.36 | PINNED between the walls (positive gamma) - chop | **-** | 33 | - | POS +$495.3M | - | 270 | 270 | -$6.5M | +$282k bull / +$0 bear | out (clean 31, ADX 20, RVol 0.8) |
| 4 | **HOOD** | 83.82 | TREND (flow not with it) | **CALLS** | 24 | 11/13 86C @ 0.64 (delta 0.28) = est +48% at 85 | POS +$15.5M | 79 | 85 | 80 | -$260k | - | LONG (clean 34, ADX 25, RVol 0.7) |
| 5 | **SPY** | 760.78 | - | **-** | 22 | - | NEG -$419.5M | 761.31 | 760 | 760 | -$135.5M | +$10.1M bull / +$0 bear | out (clean 31, ADX 26, RVol 0.9) |
| 6 | **AVGO** | 365.58 | - | **-** | 22 | - | POS +$134.4M | - | 380 | 350 | +$4.9M | +$597k bull / -$430k bear | out (clean 35, ADX 33, RVol 2.0) |
| 7 | **MSTR** | 117.48 | - | **-** | 22 | - | NEG -$29.2M | - | 125 | 110 | -$2.2M | +$255k bull / +$0 bear | out (clean 28, ADX 29, RVol 1.0) |
| 8 | **NVDA** | 164.93 | - | **-** | 21 | - | NEG -$187.7M | - | 170 | 160 | -$92.4M | +$6.7M bull / -$1.5M bear | out (clean 33, ADX 25, RVol 1.2) |
| 9 | **QQQ** | 691.35 | - | **-** | 20 | - | POS +$95.9M | 690.71 | 700 | 680 | -$109.7M | +$3.9M bull / +$0 bear | out (clean 31, ADX 27, RVol 0.8) |
| 10 | **SMH** | 503.92 | - | **-** | 20 | - | NEG -$93.0M | - | 500 | 500 | -$1.8M | +$32k bull / +$0 bear | out (clean 31, ADX 26, RVol 0.8) |
| 11 | **META** | 624.51 | - | **-** | 19 | - | POS +$4.5M | 624.11 | 650 | 600 | +$2.0M | +$764k bull / +$0 bear | out (clean 28, ADX 36, RVol 0.5) |
| 12 | **PLTR** | 172.29 | - | **-** | 19 | - | POS +$93.2M | - | 170 | 170 | -$450k | +$0 bull / -$25k bear | out (clean 28, ADX 30, RVol 0.5) |
| 13 | **ORCL** | 127.23 | - | **-** | 19 | - | POS +$11.3M | 121.49 | 130 | 125 | -$513k | +$148k bull / +$0 bear | out (clean 29, ADX 25, RVol 0.8) |
| 14 | **ARM** | 201.19 | - | **-** | 19 | - | POS +$10.5M | - | 200 | 200 | -$284k | +$31k bull / +$0 bear | out (clean 31, ADX 19, RVol 0.4) |
| 15 | **AAPL** | 357.82 | - | **-** | 18 | - | POS +$1.1B | 339.31 | 360 | 360 | +$172k | +$62k bull / +$0 bear | out (clean 28, ADX 35, RVol 0.7) |
| 16 | **SHOP** | 149.44 | - | **-** | 18 | - | POS +$5.4M | 144 | 150 | 150 | -$21k | - | out (clean 30, ADX 20, RVol 0.6) |
| 17 | **TSLA** | 392.08 | - | **-** | 17 | - | POS +$375.6M | - | 400 | 380 | +$8.2M | +$445k bull / -$488k bear | out (clean 29, ADX 20, RVol 0.6) |
| 18 | **DELL** | 369.61 | - | **-** | 17 | - | POS +$5.3M | - | 360 | 340 | +$4k | +$0 bull / -$50k bear | out (clean 36, ADX 23, RVol 1.4) |
| 19 | **MU** | 787.48 | - | **-** | 17 | - | POS +$99.6M | - | 800 | 800 | +$13.3M | +$3.4M bull / -$30k bear | out (clean 31, ADX 23, RVol 0.6) |
| 20 | **BABA** | 94.73 | - | **-** | 17 | - | NEG -$15.6M | - | 100 | 95 | +$164k | - | out (clean 29, ADX 49, RVol 2.9) |
| 21 | **SMCI** | 26.55 | - | **-** | 14 | - | NEG -$1.2M | - | 28 | 25 | +$149k | - | out (clean 33, ADX 39, RVol 6.2) |
| 22 | **MSFT** | 528.66 | - | **-** | 13 | - | POS +$208.6M | 520.57 | 535 | 520 | -$4.4M | - | out (clean 31, ADX 36, RVol 0.6) |
| 23 | **NFLX** | 63.65 | - | **-** | 10 | - | NEG -$6.4M | 63.98 | 65 | 65 | -$215k | - | out (clean 28, ADX 22, RVol 0.4) |
| 24 | **UBER** | 69.66 | - | **-** | 9 | - | POS +$15.7M | 68.32 | 70 | 70 | -$56k | - | out (clean 31, ADX 23, RVol 0.4) |
| 25 | **COIN** | 133.47 | - | **-** | 8 | - | POS +$9.2M | 130.02 | 137 | 135 | +$25k | - | out (clean 29, ADX 32, RVol 1.0) |
| 26 | **IWM** | 280.98 | - | **-** | 7 | - | NEG -$714.7M | 282.67 | 285 | 275 | -$1.3M | - | out (clean 34, ADX 30, RVol 0.7) |
| 27 | **CRM** | 217.37 | - | **-** | 7 | - | NEG -$9.2M | - | 220 | 220 | -$20k | - | out (clean 28, ADX 20, RVol 0.3) |

## Big prints this scan (170)
- **SPY** PUT 766 2026-11-16 (4DTE): 1,885 @ 5.32 = **+$1.0M** SELL | vol 8,015 / OI 116
- **SPY** PUT 766 2026-11-16 (4DTE): 1,620 @ 5.38 = **+$872k** SELL | vol 8,015 / OI 116
- **SPY** PUT 766 2026-11-16 (4DTE): 1,594 @ 5.30 = **+$845k** SELL | vol 8,015 / OI 116
- **SPY** PUT 766 2026-11-16 (4DTE): 1,357 @ 5.30 = **+$719k** SELL | vol 8,015 / OI 116
- **SPY** PUT 763 2026-11-16 (4DTE): 1,885 @ 3.77 = **+$711k** SELL | vol 21,322 / OI 216
- **SPY** PUT 763 2026-11-16 (4DTE): 1,620 @ 3.83 = **+$620k** SELL | vol 21,322 / OI 216
- **SPY** PUT 763 2026-11-16 (4DTE): 1,594 @ 3.76 = **+$599k** SELL | vol 21,322 / OI 216
- **SPY** PUT 763 2026-11-16 (4DTE): 1,357 @ 3.76 = **+$510k** SELL | vol 21,322 / OI 216
- **SPY** PUT 766 2026-11-16 (4DTE): 500 @ 5.30 = **+$265k** SELL | vol 8,015 / OI 116
- **SPY** PUT 766 2026-11-16 (4DTE): 478 @ 5.30 = **+$253k** SELL | vol 8,015 / OI 116
- **NVDA** CALL 165 2026-11-13 (1DTE): 500 @ 4.47 = **+$224k** BUY | vol 174,615 / OI 2,999
- **QQQ** PUT 703 2026-11-13 (1DTE): 223 @ 9.94 = **+$222k** SELL | vol 305 / OI 157
- **SPY** PUT 766 2026-11-16 (4DTE): 370 @ 5.29 = **+$196k** SELL | vol 8,015 / OI 116
- **AMD** CALL 565 2026-11-16 (4DTE): 60 @ 32.00 = **+$192k** BUY | vol 904 / OI 104
- **SPY** PUT 763 2026-11-16 (4DTE): 500 @ 3.76 = **+$188k** SELL | vol 21,322 / OI 216

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 762 2026-11-16 (4DTE): 621 traded vs OI 153
- **SPY** CALL 790 2026-11-18 (6DTE): 513 traded vs OI 302
- **SPY** CALL 762 2026-11-18 (6DTE): 504 traded vs OI 342
- **SPY** CALL 797 2026-11-17 (5DTE): 1,201 traded vs OI 318
- **SPY** CALL 788 2026-11-13 (1DTE): 1,561 traded vs OI 1,085
- **SPY** CALL 769 2026-11-16 (4DTE): 874 traded vs OI 865
- **SPY** CALL 772 2026-11-13 (1DTE): 7,030 traded vs OI 2,958
- **SPY** PUT 720 2026-11-23 (11DTE): 511 traded vs OI 173
- **SPY** PUT 750 2026-11-18 (6DTE): 664 traded vs OI 662
- **SPY** PUT 760 2026-11-19 (7DTE): 514 traded vs OI 120
- **QQQ** CALL 715 2026-11-12 (0DTE): 1,452 traded vs OI 668
- **QQQ** PUT 678 2026-11-16 (4DTE): 503 traded vs OI 173
- **QQQ** PUT 696 2026-11-13 (1DTE): 516 traded vs OI 481
- **QQQ** PUT 631 2026-11-13 (1DTE): 667 traded vs OI 216
- **IWM** CALL 290 2026-11-17 (5DTE): 630 traded vs OI 465

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
