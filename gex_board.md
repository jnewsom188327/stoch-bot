# GEX + FLOW SCAN - Thu Nov 12, 11:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:35 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 754P | 0.59 | 0.20 | +10% (1m) | **-66%** | +70% | 755 |
| 09:50 | **HOOD** | **PUTS** | TREND + FLOW | 11/13 79P | 0.55 | 0.36 | +5% (19m) | **-35%** (done) | +92% | 80 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 130C | 0.75 | 0.72 | +4% (60m) | **-4%** (done) | +59% | 126.9 |
| 09:45 | **SMCI** | **PUTS** | TREND + FLOW | 11/13 27P | 0.42 | 0.23 | -5% (6m) | **-45%** (done) | +57% | 27 |
| 09:45 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 753P | 0.79 | 0.31 | +23% (18m) | **-61%** (done) | +51% | 754.88 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:00:08 ET, last candle SPY 10:59, QQQ 10:59 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:03 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (3 today, last 5)
- 10:30 IWM CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:25 IWM CALLS: price -0.79 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:20 IWM CALLS: price -0.12 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **META** | 625.45 | FLIP CROSS up into positive gamma | **CALLS** | 37 | none: 150 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$4.8M | 624.08 | 650 | 600 | +$1.1M | +$0 bull / -$191k bear | out (clean 28, ADX 51, RVol 1.1) |
| 2 | **QQQ** | 691.84 | FLIP CROSS up into positive gamma | **CALLS** | 31 | 11/12 696C @ 0.70 (delta 0.22) = est +479% at 700 | POS +$152.3M | 690.79 | 700 | 680 | -$40.0M | +$0 bull / -$1.4M bear | out (clean 30, ADX 29, RVol 0.5) |
| 3 | **MSTR** | 117.41 | - | **-** | 26 | - | NEG -$29.4M | - | 125 | 110 | -$2.7M | +$0 bull / -$51k bear | out (clean 27, ADX 31, RVol 1.2) |
| 4 | **NVDA** | 165.77 | - | **-** | 25 | - | NEG -$183.9M | - | 170 | 160 | -$94.2M | +$2.1M bull / -$4.2M bear | out (clean 32, ADX 34, RVol 1.9) |
| 5 | **AVGO** | 363.22 | - | **-** | 23 | - | POS +$131.3M | - | 350 | 350 | +$6.8M | +$211k bull / -$36k bear | out (clean 35, ADX 35, RVol 1.4) |
| 6 | **ORCL** | 127.70 | - | **-** | 23 | - | POS +$10.4M | 122.3 | 130 | 125 | -$795k | +$0 bull / -$27k bear | out (clean 29, ADX 24, RVol 0.7) |
| 7 | **IWM** | 280.92 | - | **-** | 22 | - | NEG -$741.8M | 282.78 | 285 | 275 | +$2.7M | +$0 bull / -$182k bear | out (clean 34, ADX 47, RVol 0.8) |
| 8 | **MU** | 789.77 | - | **-** | 22 | - | POS +$93.0M | - | 800 | 800 | +$28.7M | +$102k bull / -$1.9M bear | out (clean 31, ADX 38, RVol 0.9) |
| 9 | **AMZN** | 269.80 | PINNED between the walls (positive gamma) - chop | **-** | 21 | - | POS +$508.2M | - | 270 | 270 | -$4.7M | - | out (clean 31, ADX 23, RVol 0.5) |
| 10 | **MSFT** | 528.11 | - | **-** | 21 | - | POS +$191.0M | 520.84 | 535 | 520 | -$3.0M | +$56k bull / +$0 bear | out (clean 31, ADX 31, RVol 0.6) |
| 11 | **AMD** | 584.00 | - | **-** | 20 | - | POS +$192.8M | - | 600 | 550 | +$15.1M | +$0 bull / -$1.6M bear | out (clean 34, ADX 27, RVol 1.2) |
| 12 | **SPY** | 760.81 | - | **-** | 19 | - | NEG -$622.9M | 761.55 | 760 | 760 | -$53.6M | +$0 bull / -$1.9M bear | out (clean 31, ADX 22, RVol 0.8) |
| 13 | **TSLA** | 391.79 | - | **-** | 19 | - | POS +$371.4M | - | 400 | 380 | +$11.7M | +$146k bull / -$175k bear | out (clean 29, ADX 28, RVol 0.3) |
| 14 | **AAPL** | 358.26 | - | **-** | 19 | - | POS +$1.2B | 340.04 | 360 | 360 | +$11k | +$52k bull / -$64k bear | out (clean 28, ADX 42, RVol 0.6) |
| 15 | **BABA** | 94.61 | - | **-** | 18 | - | NEG -$19.3M | - | 100 | 100 | +$244k | - | out (clean 29, ADX 58, RVol 1.6) |
| 16 | **SMCI** | 28.61 | - | **-** | 14 | - | POS +$4.2M | - | 30 | 30 | -$82k | - | out (clean 33, ADX 46, RVol 1.5) |
| 17 | **NFLX** | 63.38 | - | **-** | 13 | - | NEG -$10.6M | 63.93 | 65 | 65 | -$187k | - | out (clean 27, ADX 36, RVol 0.6) |
| 18 | **COIN** | 132.37 | - | **-** | 13 | - | POS +$3.5M | 130.99 | 137 | 135 | +$150k | - | out (clean 29, ADX 39, RVol 1.0) |
| 19 | **SHOP** | 149.34 | - | **-** | 13 | - | POS +$5.4M | 143.61 | 150 | 140 | -$3k | - | out (clean 30, ADX 22, RVol 1.6) |
| 20 | **SMH** | 506.59 | - | **-** | 12 | - | NEG -$80.5M | - | 500 | 500 | -$1.7M | - | out (clean 30, ADX 35, RVol 0.7) |
| 21 | **ARM** | 203.43 | - | **-** | 10 | - | POS +$10.0M | - | 200 | 200 | -$181k | - | out (clean 30, ADX 29, RVol 0.6) |
| 22 | **GOOGL** | 297.29 | - | **-** | 9 | - | POS +$116.5M | 288.55 | 300 | 290 | +$948k | - | out (clean 28, ADX 20, RVol 1.3) |
| 23 | **HOOD** | 83.57 | - | **-** | 9 | - | POS +$14.5M | 79.17 | 85 | 80 | -$15k | - | out (clean 33, ADX 27, RVol 1.9) |
| 24 | **PLTR** | 171.22 | - | **-** | 8 | - | POS +$90.2M | - | 170 | 170 | -$6k | - | out (clean 27, ADX 42, RVol 0.4) |
| 25 | **DELL** | 364.18 | - | **-** | 8 | - | POS +$4.3M | - | 360 | 340 | +$271k | - | out (clean 36, ADX 31, RVol 0.6) |
| 26 | **UBER** | 69.64 | - | **-** | 8 | - | POS +$14.8M | 68.25 | 70 | 70 | -$6k | - | out (clean 31, ADX 32, RVol 1.0) |
| 27 | **CRM** | 216.40 | - | **-** | 7 | - | NEG -$9.3M | - | 220 | 220 | -$8k | - | out (clean 28, ADX 27, RVol 0.6) |

## Big prints this scan (91)
- **SPY** PUT 763 2026-11-16 (4DTE): 1,642 @ 6.30 = **+$1.0M** BUY | vol 9,031 / OI 216
- **QQQ** CALL 660 2026-11-13 (1DTE): 200 @ 27.50 = **+$550k** SELL | vol 379 / OI 2,581
- **QQQ** PUT 685 2026-11-12 (0DTE): 1,200 @ 1.65 = **+$198k** BUY | vol 79,244 / OI 462
- **NVDA** CALL 165 2026-11-13 (1DTE): 500 @ 3.86 = **+$193k** SELL | vol 148,812 / OI 2,999
- **SPY** PUT 763 2026-11-16 (4DTE): 279 @ 6.30 = **+$176k** BUY | vol 9,031 / OI 216
- **QQQ** CALL 660 2026-11-13 (1DTE): 50 @ 28.20 = **+$141k** SELL | vol 379 / OI 2,581
- **QQQ** CALL 660 2026-11-13 (1DTE): 50 @ 27.65 = **+$138k** SELL | vol 379 / OI 2,581
- **MU** PUT 765 2026-11-18 (6DTE): 50 @ 24.90 = **+$124k** BUY | vol 331 / OI 15
- **QQQ** PUT 687 2026-11-12 (0DTE): 600 @ 1.96 = **+$118k** BUY | vol 38,570 / OI 97
- **SPY** CALL 757 2026-11-13 (1DTE): 290 @ 4.00 = **+$116k** SELL | vol 14,762 / OI 1,638
- **NVDA** PUT 160 2026-11-13 (1DTE): 584 @ 1.96 = **+$114k** BUY | vol 111,104 / OI 24,121
- **AMD** CALL 560 2026-11-13 (1DTE): 60 @ 16.50 = **+$99k** SELL | vol 5,578 / OI 2,043
- **NVDA** CALL 170 2026-11-13 (1DTE): 500 @ 1.93 = **+$96k** BUY | vol 119,677 / OI 11,191
- **TSLA** CALL 385 2026-11-16 (4DTE): 100 @ 9.65 = **+$96k** SELL | vol 787 / OI 301
- **NVDA** CALL 170 2026-11-13 (1DTE): 500 @ 1.92 = **+$96k** MID | vol 119,677 / OI 11,191

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 742 2026-11-16 (4DTE): 2,367 traded vs OI 1,398
- **SPY** PUT 726 2026-11-12 (0DTE): 1,424 traded vs OI 1,090
- **SPY** CALL 799 2026-11-16 (4DTE): 683 traded vs OI 148
- **SPY** CALL 765 2026-11-13 (1DTE): 9,832 traded vs OI 9,365
- **QQQ** PUT 675 2026-11-13 (1DTE): 7,466 traded vs OI 7,294
- **QQQ** CALL 690 2026-11-16 (4DTE): 1,358 traded vs OI 1,234
- **QQQ** CALL 695 2026-11-16 (4DTE): 715 traded vs OI 691
- **QQQ** PUT 660 2026-11-16 (4DTE): 797 traded vs OI 790
- **QQQ** PUT 692 2026-11-13 (1DTE): 504 traded vs OI 368
- **QQQ** PUT 680 2026-11-18 (6DTE): 601 traded vs OI 574
- **QQQ** CALL 686 2026-11-20 (8DTE): 598 traded vs OI 591
- **IWM** PUT 272 2026-11-20 (8DTE): 16,987 traded vs OI 15,760
- **IWM** CALL 284 2026-11-16 (4DTE): 639 traded vs OI 619
- **IWM** CALL 280 2026-11-16 (4DTE): 587 traded vs OI 441
- **IWM** CALL 284 2026-12-04 (22DTE): 1,194 traded vs OI 272

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
