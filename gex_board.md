# GEX + FLOW SCAN - Thu Nov 12, 01:00 PM ET
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
Last 1m check 13:00:08 ET, last candle SPY 12:59, QQQ 12:59 | no errors
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
| 1 | **DELL** | 380.62 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 47 | none: 30 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$6.1M | - | 360 | 380 | -$826k | - | LONG (clean 36, ADX 30, RVol 1.6) |
| 2 | **SPY** | 761.03 | FLIP CROSS down into negative gamma | **PUTS** | 28 | none: 654 puts 0-7DTE > 50 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +13% at the target (needs +20%) (268 contracts' greeks worked out here) | NEG -$231.3M | 761.25 | 760 | 760 | -$142.2M | +$223k bull / -$385k bear | out (clean 31, ADX 12, RVol 0.3) |
| 3 | **GOOGL** | 302.01 | - | **-** | 25 | - | POS +$139.0M | 288.56 | 300 | 290 | -$7.5M | +$38k bull / -$130k bear | out (clean 30, ADX 45, RVol 0.9) |
| 4 | **NFLX** | 63.88 | FLIP CROSS down into negative gamma | **PUTS** | 21 | none: 13 puts 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +13% at the target (needs +20%) (5 contracts' greeks worked out here) | NEG -$1.2M | 63.9 | 65 | 65 | -$228k | - | out (clean 28, ADX 18, RVol 0.5) |
| 5 | **AAPL** | 355.25 | - | **-** | 20 | - | POS +$1.1B | 339.76 | 360 | 350 | +$4.5M | +$67k bull / -$26k bear | out (clean 29, ADX 35, RVol 0.7) |
| 6 | **NVDA** | 164.90 | - | **-** | 18 | - | NEG -$185.8M | - | 170 | 160 | -$77.1M | +$663k bull / -$2.0M bear | out (clean 32, ADX 18, RVol 0.8) |
| 7 | **PLTR** | 172.53 | - | **-** | 18 | - | POS +$97.9M | - | 170 | 170 | -$665k | +$0 bull / -$41k bear | out (clean 28, ADX 19, RVol 0.5) |
| 8 | **AVGO** | 364.21 | - | **-** | 17 | - | POS +$136.8M | - | 350 | 350 | +$7.9M | +$274k bull / +$0 bear | out (clean 35, ADX 17, RVol 0.6) |
| 9 | **SMCI** | 26.95 | - | **-** | 17 | - | NEG -$1.0M | - | 28 | 25 | +$1.4M | - | out (clean 34, ADX 42, RVol 1.0) |
| 10 | **CRM** | 218.44 | - | **-** | 17 | - | NEG -$8.2M | - | 220 | 220 | +$27k | +$34k bull / +$0 bear | out (clean 28, ADX 27, RVol 0.3) |
| 11 | **AMD** | 582.00 | - | **-** | 16 | - | POS +$198.3M | - | 600 | 550 | -$23.6M | +$0 bull / -$5.3M bear | out (clean 34, ADX 20, RVol 0.4) |
| 12 | **MSTR** | 116.93 | - | **-** | 16 | - | NEG -$29.6M | - | 125 | 110 | -$1.8M | +$30k bull / -$40k bear | out (clean 28, ADX 13, RVol 0.5) |
| 13 | **QQQ** | 691.27 | - | **-** | 15 | - | POS +$63.3M | 690.82 | 700 | 680 | -$95.1M | +$121k bull / -$1.5M bear | out (clean 31, ADX 13, RVol 0.3) |
| 14 | **TSLA** | 391.65 | - | **-** | 15 | - | POS +$377.2M | - | 400 | 380 | +$9.4M | +$108k bull / -$397k bear | out (clean 29, ADX 14, RVol 0.3) |
| 15 | **META** | 626.07 | - | **-** | 15 | - | POS +$11.8M | 624.29 | 650 | 600 | +$808k | +$0 bull / -$170k bear | out (clean 28, ADX 20, RVol 0.3) |
| 16 | **MU** | 795.01 | - | **-** | 14 | - | POS +$105.3M | - | 800 | 800 | -$687k | +$0 bull / -$2.1M bear | out (clean 31, ADX 17, RVol 0.5) |
| 17 | **BABA** | 94.66 | - | **-** | 13 | - | NEG -$16.2M | - | 100 | 95 | +$364k | - | out (clean 28, ADX 31, RVol 0.8) |
| 18 | **MSFT** | 528.59 | - | **-** | 11 | - | POS +$217.9M | 521.2 | 535 | 520 | -$5.3M | - | out (clean 30, ADX 28, RVol 0.4) |
| 19 | **ARM** | 200.51 | - | **-** | 8 | - | POS +$10.3M | - | 200 | 200 | -$274k | - | out (clean 31, ADX 21, RVol 0.1) |
| 20 | **UBER** | 69.69 | - | **-** | 8 | - | POS +$15.3M | 68.39 | 70 | 70 | -$83k | - | out (clean 31, ADX 13, RVol 0.2) |
| 21 | **SMH** | 502.64 | - | **-** | 7 | - | NEG -$91.1M | - | 500 | 500 | -$1.8M | - | out (clean 30, ADX 16, RVol 0.4) |
| 22 | **AMZN** | 269.21 | - | **-** | 7 | - | POS +$511.4M | - | 270 | 270 | -$6.7M | - | out (clean 30, ADX 9, RVol 0.7) |
| 23 | **ORCL** | 127.43 | - | **-** | 6 | - | POS +$12.1M | 121.15 | 130 | 125 | -$541k | - | out (clean 30, ADX 16, RVol 0.3) |
| 24 | **IWM** | 280.82 | - | **-** | 4 | - | NEG -$786.2M | 282.62 | 285 | 275 | -$1.3M | - | out (clean 32, ADX 14, RVol 0.3) |
| 25 | **COIN** | 133.57 | - | **-** | 4 | - | POS +$10.2M | 130.43 | 137 | 135 | +$27k | - | out (clean 30, ADX 15, RVol 0.3) |
| 26 | **HOOD** | 83.56 | - | **-** | 4 | - | POS +$14.7M | 79.34 | 85 | 80 | -$112k | - | out (clean 34, ADX 12, RVol 0.2) |
| 27 | **SHOP** | 148.53 | - | **-** | 4 | - | POS +$4.5M | 144.22 | 150 | 140 | -$605 | - | out (clean 30, ADX 16, RVol 0.4) |

## Big prints this scan (48)
- **SMH** PUT 500 2026-11-13 (1DTE): 1,000 @ 4.70 = **+$470k** MID | vol 2,104 / OI 2,527
- **NVDA** CALL 162.5 2026-11-13 (1DTE): 300 @ 5.26 = **+$158k** BUY | vol 91,632 / OI 665
- **NVDA** CALL 160 2026-11-13 (1DTE): 197 @ 6.95 = **+$137k** BUY | vol 129,614 / OI 2,015
- **QQQ** CALL 668 2026-11-13 (1DTE): 50 @ 24.13 = **+$121k** BUY | vol 596 / OI 1,187
- **SPY** PUT 762 2026-11-19 (7DTE): 200 @ 5.87 = **+$117k** SELL | vol 1,169 / OI 0
- **SPY** PUT 762 2026-11-19 (7DTE): 180 @ 5.87 = **+$106k** SELL | vol 1,169 / OI 0
- **MU** CALL 775 2026-11-16 (4DTE): 30 @ 32.90 = **+$99k** SELL | vol 721 / OI 598
- **MU** CALL 775 2026-11-13 (1DTE): 37 @ 25.82 = **+$96k** SELL | vol 6,083 / OI 575
- **NVDA** PUT 165 2026-11-13 (1DTE): 269 @ 3.44 = **+$93k** MID | vol 82,371 / OI 19,300
- **MU** CALL 790 2026-11-13 (1DTE): 50 @ 16.50 = **+$82k** SELL | vol 14,285 / OI 1,225
- **MU** CALL 775 2026-11-13 (1DTE): 30 @ 26.25 = **+$79k** SELL | vol 6,083 / OI 575
- **NVDA** CALL 165 2026-11-13 (1DTE): 189 @ 3.85 = **+$73k** BUY | vol 207,380 / OI 2,999
- **NVDA** CALL 160 2026-11-13 (1DTE): 101 @ 6.95 = **+$70k** BUY | vol 129,614 / OI 2,015
- **NVDA** PUT 165 2026-11-13 (1DTE): 180 @ 3.50 = **+$63k** BUY | vol 82,371 / OI 19,300
- **MU** CALL 820 2026-11-16 (4DTE): 50 @ 11.40 = **+$57k** SELL | vol 640 / OI 119

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 744 2026-11-13 (1DTE): 2,878 traded vs OI 2,796
- **SPY** PUT 757 2026-11-23 (11DTE): 502 traded vs OI 35
- **AAPL** PUT 350 2026-11-27 (15DTE): 1,255 traded vs OI 1,246
- **AMD** CALL 610 2026-11-16 (4DTE): 531 traded vs OI 57
- **AMZN** PUT 252.5 2026-11-16 (4DTE): 693 traded vs OI 304
- **GOOGL** CALL 307.5 2026-11-16 (4DTE): 500 traded vs OI 53

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
