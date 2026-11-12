# GEX + FLOW SCAN - Thu Nov 12, 01:30 PM ET
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
Last 1m check 13:30:08 ET, last candle SPY 13:29, QQQ 13:29 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:03 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (7 today, last 5)
- 12:00 SMCI CALLS: price -0.27 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:55 SMCI CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:50 SMCI CALLS: price -0.48 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:45 SMCI CALLS: price -0.74 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:30 IWM CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DELL** | 376.83 | TREND + FLOW | **CALLS** | 36 | none: 30 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$4.5M | - | 360 | 380 | +$189k | +$267k bull / +$0 bear | LONG (clean 37, ADX 30, RVol 0.7) |
| 2 | **GOOGL** | 301.30 | - | **-** | 23 | - | POS +$139.6M | 287.81 | 300 | 290 | -$5.5M | +$151k bull / -$199k bear | out (clean 30, ADX 40, RVol 1.2) |
| 3 | **AAPL** | 355.75 | - | **-** | 21 | - | POS +$1.1B | 341.05 | 360 | 360 | +$4.9M | +$60k bull / -$47k bear | out (clean 29, ADX 40, RVol 0.5) |
| 4 | **UBER** | 69.93 | PINNED between the walls (positive gamma) - chop | **-** | 21 | - | POS +$16.5M | 68.39 | 70 | 70 | -$82k | - | out (clean 31, ADX 15, RVol 0.4) |
| 5 | **BABA** | 94.96 | - | **-** | 20 | - | NEG -$19.2M | - | 100 | 100 | +$291k | +$0 bull / -$44k bear | out (clean 28, ADX 21, RVol 0.9) |
| 6 | **NVDA** | 165.88 | - | **-** | 17 | - | NEG -$183.7M | - | 170 | 160 | -$82.5M | +$28k bull / -$3.2M bear | out (clean 31, ADX 12, RVol 0.7) |
| 7 | **SPY** | 760.50 | - | **-** | 16 | - | NEG -$381.8M | 760.89 | 760 | 760 | -$133.9M | +$603k bull / -$492k bear | out (clean 30, ADX 12, RVol 0.3) |
| 8 | **AVGO** | 364.68 | - | **-** | 16 | - | POS +$134.3M | - | 350 | 350 | +$8.2M | +$0 bull / -$28k bear | out (clean 34, ADX 12, RVol 0.4) |
| 9 | **ORCL** | 127.52 | - | **-** | 16 | - | POS +$10.9M | 121.34 | 130 | 125 | -$557k | +$119k bull / +$0 bear | out (clean 30, ADX 12, RVol 0.3) |
| 10 | **QQQ** | 690.69 | - | **-** | 15 | - | POS +$10.0M | 690.67 | 700 | 680 | -$88.0M | +$1.0M bull / -$954k bear | out (clean 30, ADX 12, RVol 0.4) |
| 11 | **TSLA** | 392.07 | - | **-** | 15 | - | POS +$374.7M | - | 400 | 380 | +$9.8M | +$33k bull / +$0 bear | out (clean 28, ADX 15, RVol 0.2) |
| 12 | **AMD** | 581.86 | - | **-** | 15 | - | POS +$198.2M | - | 600 | 550 | -$19.9M | +$418k bull / -$1.1M bear | out (clean 34, ADX 15, RVol 0.4) |
| 13 | **META** | 624.90 | - | **-** | 15 | - | NEG -$1.5M | 624.37 | 650 | 600 | +$1.8M | +$28k bull / -$97k bear | out (clean 28, ADX 18, RVol 0.4) |
| 14 | **SMCI** | 27.07 | - | **-** | 15 | - | NEG -$876k | - | 28 | 25 | +$1.6M | - | out (clean 34, ADX 36, RVol 0.7) |
| 15 | **MSTR** | 116.94 | - | **-** | 15 | - | NEG -$30.3M | - | 125 | 110 | -$1.7M | +$38k bull / -$46k bear | out (clean 28, ADX 9, RVol 0.5) |
| 16 | **MU** | 796.24 | - | **-** | 14 | - | POS +$105.4M | - | 800 | 800 | +$4.2M | +$239k bull / -$995k bear | out (clean 31, ADX 16, RVol 0.3) |
| 17 | **MSFT** | 526.10 | - | **-** | 9 | - | POS +$89.2M | 520.52 | 535 | 520 | -$4.3M | - | out (clean 30, ADX 25, RVol 0.4) |
| 18 | **NFLX** | 63.67 | - | **-** | 7 | - | NEG -$5.3M | 63.88 | 65 | 65 | -$178k | - | out (clean 28, ADX 17, RVol 0.6) |
| 19 | **ARM** | 201.52 | - | **-** | 7 | - | POS +$10.9M | - | 200 | 200 | -$270k | - | out (clean 31, ADX 19, RVol 0.1) |
| 20 | **SMH** | 504.10 | - | **-** | 6 | - | NEG -$87.0M | - | 500 | 500 | -$1.8M | - | out (clean 30, ADX 12, RVol 0.4) |
| 21 | **AMZN** | 269.31 | - | **-** | 6 | - | POS +$506.1M | - | 270 | 270 | -$6.9M | - | out (clean 29, ADX 10, RVol 0.4) |
| 22 | **CRM** | 217.54 | - | **-** | 6 | - | NEG -$8.9M | - | 220 | 220 | +$30k | - | out (clean 28, ADX 22, RVol 0.1) |
| 23 | **IWM** | 280.40 | - | **-** | 5 | - | NEG -$915.1M | 282.63 | 285 | 275 | -$802k | - | out (clean 32, ADX 21, RVol 0.6) |
| 24 | **PLTR** | 172.05 | - | **-** | 5 | - | POS +$89.3M | - | 170 | 170 | -$408k | - | out (clean 28, ADX 14, RVol 0.5) |
| 25 | **SHOP** | 147.92 | - | **-** | 5 | - | POS +$4.4M | 144.28 | 150 | 140 | -$108 | - | out (clean 30, ADX 21, RVol 0.4) |
| 26 | **COIN** | 133.25 | - | **-** | 4 | - | POS +$7.3M | 131.38 | 137 | 135 | +$58k | - | out (clean 29, ADX 11, RVol 0.6) |
| 27 | **HOOD** | 83.31 | - | **-** | 4 | - | POS +$13.1M | 80.08 | 85 | 80 | -$94k | - | out (clean 34, ADX 11, RVol 0.5) |

## Big prints this scan (39)
- **SPY** PUT 764 2026-11-18 (6DTE): 498 @ 7.05 = **+$351k** BUY | vol 1,058 / OI 20
- **QQQ** CALL 691 2026-11-12 (0DTE): 1,999 @ 1.00 = **+$200k** SELL | vol 174,267 / OI 387
- **NVDA** PUT 162.5 2026-11-16 (4DTE): 428 @ 3.55 = **+$152k** BUY | vol 18,283 / OI 1,267
- **QQQ** PUT 690 2026-11-12 (0DTE): 648 @ 1.61 = **+$104k** BUY | vol 204,287 / OI 443
- **NVDA** CALL 170 2026-11-13 (1DTE): 500 @ 1.69 = **+$84k** SELL | vol 188,628 / OI 11,191
- **NVDA** CALL 165 2026-11-18 (6DTE): 99 @ 8.46 = **+$84k** SELL | vol 9,798 / OI 517
- **GOOGL** CALL 295 2026-11-13 (1DTE): 115 @ 7.00 = **+$80k** MID | vol 7,848 / OI 3,921
- **META** CALL 630 2026-11-13 (1DTE): 173 @ 3.71 = **+$64k** SELL | vol 5,781 / OI 2,880
- **NVDA** CALL 172.5 2026-11-13 (1DTE): 500 @ 1.10 = **+$55k** MID | vol 90,150 / OI 0
- **DELL** CALL 380 2026-11-13 (1DTE): 69 @ 7.30 = **+$50k** BUY | vol 2,181 / OI 612
- **AMD** PUT 580 2026-11-13 (1DTE): 41 @ 11.95 = **+$49k** BUY | vol 8,833 / OI 4
- **MU** PUT 785 2026-11-13 (1DTE): 40 @ 11.70 = **+$47k** BUY | vol 8,220 / OI 256
- **MU** PUT 785 2026-11-13 (1DTE): 40 @ 11.60 = **+$46k** BUY | vol 8,220 / OI 256
- **MSTR** CALL 117 2026-11-13 (1DTE): 195 @ 2.35 = **+$46k** SELL | vol 1,983 / OI 225
- **BABA** CALL 93 2026-11-13 (1DTE): 195 @ 2.26 = **+$44k** SELL | vol 500 / OI 115

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 748 2026-11-16 (4DTE): 883 traded vs OI 819
- **SPY** CALL 767 2026-11-18 (6DTE): 558 traded vs OI 555
- **SPY** CALL 796 2026-11-18 (6DTE): 518 traded vs OI 253
- **SPY** PUT 748 2026-11-17 (5DTE): 522 traded vs OI 379
- **SPY** PUT 718 2026-11-16 (4DTE): 1,964 traded vs OI 1,538
- **SPY** CALL 769 2026-11-17 (5DTE): 549 traded vs OI 375
- **QQQ** PUT 670 2026-11-18 (6DTE): 866 traded vs OI 863
- **GOOGL** PUT 300 2026-11-16 (4DTE): 916 traded vs OI 145
- **AVGO** PUT 362.5 2026-11-16 (4DTE): 501 traded vs OI 20
- **DELL** CALL 395 2026-11-13 (1DTE): 775 traded vs OI 0
- **SMCI** PUT 26.5 2026-11-27 (15DTE): 505 traded vs OI 11
- **ORCL** PUT 123 2026-11-13 (1DTE): 740 traded vs OI 729
- **HOOD** PUT 82 2026-11-13 (1DTE): 1,206 traded vs OI 1,117
- **BABA** CALL 93 2026-11-13 (1DTE): 500 traded vs OI 115

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
