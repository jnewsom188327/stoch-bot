# GEX + FLOW SCAN - Thu Nov 12, 12:50 PM ET
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
Last 1m check 12:50:08 ET, last candle SPY 12:49, QQQ 12:49 | no errors
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
| 1 | **DELL** | 379.77 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 39 | none: 31 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$5.9M | - | 360 | 380 | -$681k | +$0 bull / -$29k bear | out (clean 36, ADX 27, RVol 1.1) |
| 2 | **SPY** | 761.68 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$199.3M | 761.46 | 760 | 760 | -$145.6M | +$0 bull / -$502k bear | out (clean 31, ADX 13, RVol 0.3) |
| 3 | **GOOGL** | 302.37 | - | **-** | 25 | - | POS +$138.6M | 287.76 | 300 | 290 | -$6.7M | +$38k bull / -$90k bear | out (clean 30, ADX 43, RVol 0.9) |
| 4 | **AMZN** | 269.67 | PINNED between the walls (positive gamma) - chop | **-** | 21 | - | POS +$518.2M | - | 270 | 270 | -$6.8M | - | out (clean 30, ADX 9, RVol 0.8) |
| 5 | **AAPL** | 355.60 | - | **-** | 19 | - | POS +$1.1B | 339.5 | 360 | 360 | +$4.2M | +$327k bull / +$0 bear | out (clean 28, ADX 31, RVol 0.7) |
| 6 | **PLTR** | 172.91 | - | **-** | 19 | - | POS +$90.1M | - | 170 | 170 | -$793k | +$0 bull / -$41k bear | out (clean 28, ADX 19, RVol 0.4) |
| 7 | **NVDA** | 165.46 | - | **-** | 18 | - | NEG -$183.1M | - | 170 | 160 | -$81.7M | +$0 bull / -$3.0M bear | out (clean 32, ADX 20, RVol 0.7) |
| 8 | **SMCI** | 27.09 | - | **-** | 18 | - | NEG -$777k | - | 28 | 25 | +$1.4M | - | out (clean 34, ADX 45, RVol 1.2) |
| 9 | **AVGO** | 365.19 | - | **-** | 17 | - | POS +$132.3M | - | 380 | 350 | +$6.7M | +$0 bull / -$28k bear | out (clean 35, ADX 18, RVol 0.6) |
| 10 | **MSTR** | 116.74 | - | **-** | 17 | - | NEG -$29.9M | - | 125 | 110 | -$1.8M | +$30k bull / -$38k bear | out (clean 28, ADX 14, RVol 0.5) |
| 11 | **QQQ** | 692.18 | - | **-** | 16 | - | POS +$343.7M | 690.72 | 700 | 680 | -$104.9M | +$0 bull / -$2.6M bear | out (clean 31, ADX 14, RVol 0.3) |
| 12 | **AMD** | 582.95 | - | **-** | 16 | - | POS +$198.5M | - | 600 | 550 | -$23.4M | +$584k bull / -$7.8M bear | out (clean 34, ADX 21, RVol 0.5) |
| 13 | **TSLA** | 392.35 | - | **-** | 15 | - | POS +$381.3M | - | 400 | 380 | +$7.8M | +$0 bull / -$319k bear | out (clean 29, ADX 15, RVol 0.3) |
| 14 | **META** | 627.46 | - | **-** | 15 | - | POS +$22.4M | 624.94 | 650 | 600 | +$925k | +$0 bull / -$254k bear | out (clean 28, ADX 22, RVol 0.3) |
| 15 | **BABA** | 94.67 | - | **-** | 15 | - | NEG -$16.9M | - | 100 | 100 | +$372k | - | out (clean 28, ADX 34, RVol 1.1) |
| 16 | **MU** | 795.33 | - | **-** | 14 | - | POS +$106.4M | - | 800 | 800 | +$3.0M | +$0 bull / -$1.4M bear | out (clean 31, ADX 16, RVol 0.5) |
| 17 | **MSFT** | 529.12 | - | **-** | 11 | - | POS +$200.5M | 521.94 | 535 | 520 | -$5.3M | - | out (clean 30, ADX 27, RVol 0.3) |
| 18 | **NFLX** | 63.89 | - | **-** | 9 | - | NEG -$639k | 63.91 | 65 | 65 | -$233k | - | out (clean 28, ADX 18, RVol 0.6) |
| 19 | **UBER** | 69.75 | - | **-** | 9 | - | POS +$15.9M | 68.35 | 70 | 70 | -$83k | - | out (clean 31, ADX 14, RVol 0.3) |
| 20 | **SMH** | 504.60 | - | **-** | 8 | - | NEG -$86.8M | - | 500 | 500 | -$1.8M | - | out (clean 31, ADX 18, RVol 0.6) |
| 21 | **ARM** | 200.88 | - | **-** | 8 | - | POS +$10.9M | - | 200 | 200 | -$274k | - | out (clean 31, ADX 22, RVol 0.2) |
| 22 | **ORCL** | 127.78 | - | **-** | 7 | - | POS +$11.7M | 120.63 | 130 | 125 | -$585k | - | out (clean 30, ADX 16, RVol 0.2) |
| 23 | **CRM** | 218.34 | - | **-** | 7 | - | NEG -$7.9M | - | 220 | 220 | +$20k | - | out (clean 29, ADX 27, RVol 0.6) |
| 24 | **IWM** | 281.02 | - | **-** | 4 | - | NEG -$701.0M | 282.68 | 285 | 275 | -$1.4M | - | out (clean 33, ADX 15, RVol 0.3) |
| 25 | **COIN** | 133.24 | - | **-** | 4 | - | POS +$8.2M | 131.37 | 137 | 135 | +$36k | - | out (clean 30, ADX 16, RVol 0.5) |
| 26 | **HOOD** | 83.61 | - | **-** | 4 | - | POS +$16.2M | 79.37 | 85 | 80 | -$109k | - | out (clean 34, ADX 13, RVol 0.2) |
| 27 | **SHOP** | 148.28 | - | **-** | 4 | - | POS +$5.2M | 143.81 | 150 | 140 | -$405 | - | out (clean 30, ADX 16, RVol 0.4) |

## Big prints this scan (37)
- **QQQ** CALL 690 2026-11-12 (0DTE): 1,000 @ 2.07 = **+$207k** SELL | vol 207,392 / OI 1,788
- **AMD** CALL 600 2026-11-16 (4DTE): 200 @ 7.90 = **+$158k** SELL | vol 4,046 / OI 186
- **AMD** CALL 600 2026-11-16 (4DTE): 192 @ 8.00 = **+$154k** SELL | vol 4,046 / OI 186
- **QQQ** PUT 692 2026-11-16 (4DTE): 200 @ 6.57 = **+$131k** BUY | vol 1,017 / OI 112
- **QQQ** PUT 690 2026-11-12 (0DTE): 788 @ 1.52 = **+$120k** BUY | vol 151,366 / OI 443
- **QQQ** PUT 690 2026-11-12 (0DTE): 616 @ 1.69 = **+$104k** BUY | vol 151,366 / OI 443
- **TSLA** CALL 377.5 2026-11-13 (1DTE): 64 @ 14.70 = **+$94k** SELL | vol 301 / OI 4,895
- **META** PUT 635 2026-11-13 (1DTE): 70 @ 12.95 = **+$91k** BUY | vol 549 / OI 1,158
- **TSLA** CALL 380 2026-11-16 (4DTE): 64 @ 13.70 = **+$88k** SELL | vol 136 / OI 750
- **TSLA** PUT 405 2026-11-13 (1DTE): 60 @ 13.50 = **+$81k** MID | vol 338 / OI 396
- **NVDA** CALL 165 2026-11-13 (1DTE): 235 @ 3.35 = **+$79k** SELL | vol 203,589 / OI 2,999
- **AMD** CALL 590 2026-11-13 (1DTE): 93 @ 6.90 = **+$64k** SELL | vol 20,866 / OI 1,196
- **NVDA** CALL 160 2026-11-13 (1DTE): 100 @ 6.00 = **+$60k** SELL | vol 128,904 / OI 2,015
- **NVDA** CALL 165 2026-11-13 (1DTE): 172 @ 3.10 = **+$53k** SELL | vol 203,589 / OI 2,999
- **AMD** CALL 600 2026-11-16 (4DTE): 60 @ 7.90 = **+$47k** SELL | vol 4,046 / OI 186

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 791 2026-11-17 (5DTE): 699 traded vs OI 185
- **SPY** CALL 770 2026-11-23 (11DTE): 500 traded vs OI 439
- **QQQ** CALL 691 2026-11-18 (6DTE): 504 traded vs OI 73
- **NVDA** PUT 155 2026-11-23 (11DTE): 526 traded vs OI 215
- **AMD** CALL 550 2026-11-13 (1DTE): 2,722 traded vs OI 2,719
- **META** CALL 690 2026-11-20 (8DTE): 1,556 traded vs OI 0
- **AMZN** CALL 287.5 2026-11-16 (4DTE): 551 traded vs OI 100
- **AVGO** CALL 365 2026-11-20 (8DTE): 2,342 traded vs OI 2,193
- **MU** PUT 790 2026-11-16 (4DTE): 508 traded vs OI 33

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
