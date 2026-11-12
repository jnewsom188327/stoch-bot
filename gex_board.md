# GEX + FLOW SCAN - Thu Nov 12, 11:50 AM ET
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
Last 1m check 11:50:08 ET, last candle SPY 11:49, QQQ 11:49 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:03 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (5 today, last 5)
- 11:50 SMCI CALLS: price -0.48 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:45 SMCI CALLS: price -0.74 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:30 IWM CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:25 IWM CALLS: price -0.79 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:20 IWM CALLS: price -0.12 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMCI** | 26.71 | FLOW SURGE | **CALLS** | 57 | 11/13 27.5C @ 0.54 (delta 0.37) = est +94% at 28 | NEG -$1.2M | - | 28 | 25 | +$1.6M | +$259k bull / +$0 bear | out (clean 33, ADX 42, RVol 7.8) |
| 2 | **AMD** | 585.54 | TREND (flow not with it) | **CALLS** | 40 | none: 139 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$193.2M | - | 600 | 550 | -$19.6M | +$7.2M bull / -$423k bear | LONG (clean 34, ADX 37, RVol 1.2) |
| 3 | **QQQ** | 690.74 | FLIP CROSS up into positive gamma | **CALLS** | 31 | 11/12 694C @ 0.77 (delta 0.26) = est +168% at 694.97 | POS +$100.4M | 690.49 | 700 | 680 | -$87.9M | +$4.2M bull / -$250k bear | out (clean 31, ADX 24, RVol 0.6) |
| 4 | **AMZN** | 269.34 | PINNED between the walls (positive gamma) - chop | **-** | 31 | - | POS +$499.2M | - | 270 | 270 | -$6.6M | +$253k bull / -$56k bear | out (clean 30, ADX 18, RVol 0.6) |
| 5 | **GOOGL** | 299.22 | - | **-** | 23 | - | POS +$130.6M | 289 | 300 | 290 | -$4.6M | +$117k bull / -$62k bear | out (clean 29, ADX 32, RVol 1.2) |
| 6 | **AVGO** | 364.82 | - | **-** | 22 | - | POS +$132.8M | - | 350 | 350 | +$7.3M | +$3.5M bull / -$176k bear | out (clean 35, ADX 30, RVol 1.9) |
| 7 | **MSFT** | 527.42 | - | **-** | 21 | - | POS +$183.7M | 520.17 | 535 | 520 | -$4.1M | +$36k bull / +$0 bear | out (clean 31, ADX 34, RVol 0.4) |
| 8 | **HOOD** | 83.80 | TREND (flow not with it) | **CALLS** | 21 | 11/13 86C @ 0.66 (delta 0.27) = est +34% at 85 | POS +$15.0M | 79.18 | 85 | 80 | -$93k | - | LONG (clean 34, ADX 22, RVol 0.7) |
| 9 | **SPY** | 760.65 | - | **-** | 20 | - | NEG -$302.1M | 761.27 | 760 | 760 | -$121.6M | +$9.2M bull / -$1.3M bear | out (clean 32, ADX 23, RVol 0.8) |
| 10 | **NVDA** | 164.74 | - | **-** | 20 | - | NEG -$187.8M | - | 170 | 160 | -$74.5M | +$8.6M bull / -$1.6M bear | out (clean 33, ADX 25, RVol 1.3) |
| 11 | **DELL** | 373.36 | - | **-** | 20 | - | POS +$4.4M | - | 360 | 340 | +$595k | +$0 bull / -$423k bear | out (clean 36, ADX 24, RVol 2.4) |
| 12 | **MSTR** | 117.61 | - | **-** | 20 | - | NEG -$29.1M | - | 125 | 110 | -$2.1M | +$136k bull / +$0 bear | out (clean 28, ADX 26, RVol 0.8) |
| 13 | **META** | 625.02 | - | **-** | 19 | - | NEG -$1.1M | 624.45 | 650 | 600 | +$2.3M | +$722k bull / +$0 bear | out (clean 28, ADX 33, RVol 0.5) |
| 14 | **SMH** | 503.62 | - | **-** | 18 | - | NEG -$96.2M | - | 500 | 500 | -$1.3M | +$239k bull / +$0 bear | out (clean 31, ADX 24, RVol 0.7) |
| 15 | **AAPL** | 357.20 | - | **-** | 18 | - | POS +$1.1B | 339.2 | 360 | 360 | +$1.2M | +$173k bull / +$0 bear | out (clean 28, ADX 30, RVol 0.7) |
| 16 | **PLTR** | 171.90 | - | **-** | 18 | - | POS +$92.1M | - | 170 | 170 | -$342k | +$0 bull / -$25k bear | out (clean 28, ADX 26, RVol 0.7) |
| 17 | **ARM** | 201.02 | - | **-** | 18 | - | POS +$9.7M | - | 200 | 200 | -$245k | +$31k bull / +$0 bear | out (clean 31, ADX 20, RVol 0.3) |
| 18 | **IWM** | 281.21 | - | **-** | 17 | - | NEG -$626.0M | 282.74 | 285 | 275 | -$1.5M | +$0 bull / -$197k bear | out (clean 34, ADX 27, RVol 0.6) |
| 19 | **TSLA** | 391.64 | - | **-** | 17 | - | POS +$380.6M | - | 400 | 380 | +$9.8M | +$788k bull / -$356k bear | out (clean 29, ADX 19, RVol 0.4) |
| 20 | **MU** | 787.07 | - | **-** | 17 | - | POS +$94.3M | - | 800 | 800 | +$20.4M | +$2.5M bull / +$0 bear | out (clean 31, ADX 22, RVol 0.7) |
| 21 | **ORCL** | 127.15 | - | **-** | 17 | - | POS +$11.0M | 121.14 | 130 | 125 | -$333k | +$52k bull / +$0 bear | out (clean 29, ADX 22, RVol 0.7) |
| 22 | **SHOP** | 149.37 | - | **-** | 17 | - | POS +$5.2M | 144.08 | 150 | 150 | -$21k | - | out (clean 30, ADX 18, RVol 0.6) |
| 23 | **BABA** | 94.69 | - | **-** | 17 | - | NEG -$17.6M | - | 100 | 100 | +$208k | - | out (clean 29, ADX 47, RVol 2.7) |
| 24 | **NFLX** | 63.55 | - | **-** | 9 | - | NEG -$9.5M | 63.98 | 65 | 65 | -$190k | - | out (clean 28, ADX 20, RVol 0.5) |
| 25 | **UBER** | 69.76 | - | **-** | 9 | - | POS +$16.2M | 68.31 | 70 | 70 | -$55k | - | out (clean 31, ADX 22, RVol 0.4) |
| 26 | **COIN** | 133.46 | - | **-** | 8 | - | POS +$10.1M | 130.12 | 137 | 135 | +$55k | - | out (clean 29, ADX 29, RVol 1.1) |
| 27 | **CRM** | 217.60 | - | **-** | 8 | - | NEG -$9.2M | - | 220 | 220 | -$33k | - | out (clean 29, ADX 21, RVol 0.3) |

## Big prints this scan (100)
- **AVGO** CALL 362.5 2026-11-13 (1DTE): 1,984 @ 8.10 = **+$1.6M** BUY | vol 8,662 / OI 297
- **AVGO** CALL 367.5 2026-11-13 (1DTE): 1,984 @ 5.41 = **+$1.1M** BUY | vol 5,683 / OI 247
- **SPY** PUT 763 2026-11-16 (4DTE): 2,000 @ 4.99 = **+$998k** BUY | vol 23,586 / OI 216
- **SPY** PUT 762 2026-11-19 (7DTE): 495 @ 6.54 = **+$324k** BUY | vol 620 / OI 0
- **SPY** CALL 758 2026-11-13 (1DTE): 466 @ 5.06 = **+$236k** BUY | vol 19,762 / OI 3,119
- **QQQ** PUT 695 2026-11-12 (0DTE): 499 @ 4.40 = **+$220k** SELL | vol 9,648 / OI 243
- **QQQ** PUT 695 2026-11-12 (0DTE): 454 @ 4.20 = **+$191k** SELL | vol 9,648 / OI 243
- **NVDA** CALL 165 2026-11-13 (1DTE): 500 @ 3.60 = **+$180k** BUY | vol 181,226 / OI 2,999
- **QQQ** CALL 688 2026-11-13 (1DTE): 237 @ 6.53 = **+$155k** MID | vol 8,168 / OI 917
- **NVDA** PUT 160 2026-11-18 (6DTE): 250 @ 5.60 = **+$140k** SELL | vol 7,491 / OI 3,836
- **QQQ** PUT 695 2026-11-12 (0DTE): 310 @ 4.30 = **+$133k** SELL | vol 9,648 / OI 243
- **QQQ** PUT 692 2026-11-12 (0DTE): 520 @ 2.50 = **+$130k** BUY | vol 35,414 / OI 92
- **QQQ** CALL 683 2026-11-12 (0DTE): 150 @ 8.44 = **+$127k** BUY | vol 13,859 / OI 862
- **QQQ** PUT 694 2026-11-13 (1DTE): 253 @ 4.96 = **+$125k** SELL | vol 3,088 / OI 453
- **QQQ** PUT 690 2026-11-13 (1DTE): 300 @ 4.00 = **+$120k** BUY | vol 8,689 / OI 10,654

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 776 2026-11-16 (4DTE): 584 traded vs OI 580
- **SPY** PUT 769 2026-11-12 (0DTE): 523 traded vs OI 0
- **SPY** PUT 752 2026-11-16 (4DTE): 784 traded vs OI 769
- **SPY** PUT 741 2026-11-17 (5DTE): 757 traded vs OI 223
- **SPY** CALL 781 2026-11-16 (4DTE): 1,018 traded vs OI 932
- **SPY** CALL 774 2026-11-13 (1DTE): 2,768 traded vs OI 2,598
- **SPY** PUT 752 2026-11-19 (7DTE): 836 traded vs OI 199
- **SPY** PUT 740 2026-11-19 (7DTE): 1,106 traded vs OI 1,035
- **SPY** PUT 762 2026-11-19 (7DTE): 620 traded vs OI 0
- **SPY** CALL 770 2026-11-27 (15DTE): 2,063 traded vs OI 2,034
- **QQQ** CALL 705 2026-11-16 (4DTE): 1,715 traded vs OI 1,641
- **QQQ** PUT 679 2026-11-16 (4DTE): 906 traded vs OI 107
- **QQQ** CALL 716 2026-11-13 (1DTE): 519 traded vs OI 506
- **QQQ** PUT 676 2026-11-16 (4DTE): 521 traded vs OI 183
- **QQQ** CALL 692 2026-11-20 (8DTE): 1,381 traded vs OI 1,198

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
