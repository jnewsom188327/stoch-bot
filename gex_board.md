# GEX + FLOW SCAN - Fri Oct 30, 01:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:20:08 ET, last candle SPY 13:19, QQQ 13:19 | no errors
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
| 1 | **DELL** | 415.87 | FLOW SURGE | **CALLS** | 51 | none: 66 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (53 contracts' greeks worked out here) | NEG -$44.6M | - | 440 | 425 | +$5.0M | +$223k bull / +$0 bear | SHORT (clean 34, ADX 58, RVol 1.6) |
| 2 | **SHOP** | 155.09 | FLOW SURGE | **CALLS** | 50 | none: 38 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (33 contracts' greeks worked out here) | NEG -$11.1M | 160.98 | 150 | 157.5 | +$710k | +$233k bull / +$0 bear | out (clean 26, ADX 44, RVol 1.6) |
| 3 | **UBER** | 64.84 | FLOW SURGE | **CALLS** | 36 | none: 26 calls 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -1% at the target (needs +20%) (20 contracts' greeks worked out here) | NEG -$34.0M | 65.91 | 65 | 65 | +$387k | +$53k bull / +$0 bear | out (clean 28, ADX 18, RVol 0.5) |
| 4 | **MSFT** | 520.81 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | none: 168 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (72 contracts' greeks worked out here) | POS +$415.1M | 516.4 | 525 | 520 | +$3.6M | +$396k bull / -$618k bear | out (clean 26, ADX 14, RVol 0.3) |
| 5 | **AMD** | 499.27 | - | **-** | 30 | - | NEG -$179.2M | 521.51 | 540 | 500 | +$34.9M | +$3.7M bull / -$110k bear | out (clean 30, ADX 52, RVol 1.2) |
| 6 | **SMCI** | 31.80 | - | **-** | 29 | - | NEG -$5.3M | 32.95 | 32 | 32 | +$711k | +$27k bull / +$0 bear | out (clean 30, ADX 52, RVol 1.0) |
| 7 | **SMH** | 518.41 | - | **-** | 28 | - | NEG -$668.0M | - | 532.5 | 505 | +$8.4M | +$745k bull / -$25k bear | out (clean 30, ADX 54, RVol 1.0) |
| 8 | **NVDA** | 203.51 | - | **-** | 28 | - | NEG -$405.3M | 210.11 | 210 | 205 | +$32.2M | +$3.7M bull / -$976k bear | out (clean 27, ADX 47, RVol 0.9) |
| 9 | **QQQ** | 689.35 | - | **-** | 25 | - | NEG -$10.1B | 726.74 | 720 | 690 | +$87.9M | +$9.3M bull / -$1.4M bear | out (clean 28, ADX 47, RVol 2.2) |
| 10 | **SPY** | 755.42 | - | **-** | 24 | - | NEG -$15.6B | 770.96 | 800 | 750 | +$134.0M | +$4.6M bull / +$0 bear | out (clean 27, ADX 43, RVol 1.2) |
| 11 | **IWM** | 278.39 | - | **-** | 24 | - | NEG -$1.3B | 281.11 | 278 | 278 | +$10.7M | +$809k bull / +$0 bear | out (clean 28, ADX 45, RVol 0.6) |
| 12 | **MU** | 876.09 | - | **-** | 24 | - | NEG -$294.1M | 919.36 | 880 | 880 | +$59.0M | +$7.4M bull / -$1.6M bear | out (clean 30, ADX 36, RVol 0.7) |
| 13 | **HOOD** | 82.98 | - | **-** | 23 | - | NEG -$33.6M | - | 85 | 85 | +$1.6M | +$132k bull / +$0 bear | out (clean 31, ADX 48, RVol 0.6) |
| 14 | **BABA** | 98.32 | - | **-** | 23 | - | NEG -$37.3M | 99.55 | 100 | 98 | +$499k | +$351k bull / +$0 bear | out (clean 29, ADX 13, RVol 0.4) |
| 15 | **AVGO** | 324.04 | - | **-** | 22 | - | NEG -$160.4M | - | 340 | 320 | +$1.6M | +$60k bull / -$188k bear | out (clean 30, ADX 49, RVol 0.7) |
| 16 | **MSTR** | 129.55 | - | **-** | 22 | - | NEG -$24.4M | 134.96 | 135 | 130 | -$5.6M | +$391k bull / +$0 bear | out (clean 28, ADX 20, RVol 2.1) |
| 17 | **NFLX** | 62.12 | - | **-** | 21 | - | NEG -$23.4M | 62.76 | 62 | 62 | +$1.3M | +$27k bull / +$0 bear | out (clean 31, ADX 14, RVol 0.5) |
| 18 | **COIN** | 139.20 | - | **-** | 19 | - | NEG -$15.0M | - | 140 | 140 | -$3.3M | - | out (clean 27, ADX 45, RVol 3.4) |
| 19 | **PLTR** | 184.85 | - | **-** | 18 | - | NEG -$61.9M | 189.75 | 185 | 185 | +$1.7M | +$189k bull / -$198k bear | out (clean 26, ADX 30, RVol 0.8) |
| 20 | **AMZN** | 238.47 | - | **-** | 17 | - | NEG -$188.6M | 245.47 | 250 | 240 | -$4.0M | +$418k bull / -$382k bear | out (clean 31, ADX 15, RVol 1.6) |
| 21 | **GOOGL** | 278.78 | - | **-** | 17 | - | NEG -$239.7M | - | 280 | 280 | +$269k | +$88k bull / +$0 bear | out (clean 32, ADX 31, RVol 0.7) |
| 22 | **ARM** | 202.23 | - | **-** | 17 | - | NEG -$19.7M | - | 220 | 205 | +$717k | - | out (clean 26, ADX 37, RVol 1.6) |
| 23 | **AAPL** | 346.99 | - | **-** | 16 | - | POS +$586.8M | 342.19 | 350 | 345 | -$2.4M | +$547k bull / +$0 bear | out (clean 30, ADX 14, RVol 1.2) |
| 24 | **ORCL** | 130.79 | - | **-** | 15 | - | POS +$19.6M | 129.73 | 130 | 130 | +$2.8M | - | out (clean 34, ADX 33, RVol 0.5) |
| 25 | **TSLA** | 397.81 | - | **-** | 14 | - | POS +$456.3M | 378.74 | 400 | 400 | -$9.3M | +$1.9M bull / +$0 bear | out (clean 28, ADX 12, RVol 0.7) |
| 26 | **META** | 620.18 | - | **-** | 14 | - | NEG -$43.8M | 621.69 | 625 | 625 | -$269k | +$497k bull / -$152k bear | out (clean 28, ADX 20, RVol 0.4) |
| 27 | **CRM** | 229.40 | - | **-** | 11 | - | NEG -$23.1M | 234.74 | 230 | 230 | +$310k | - | out (clean 28, ADX 23, RVol 0.7) |

## Big prints this scan (52)
- **NVDA** CALL 210 2026-11-06 (7DTE): 8,490 @ 2.09 = **+$1.8M** BUY | vol 17,944 / OI 950
- **SPY** CALL 755 2026-11-02 (3DTE): 976 @ 4.23 = **+$413k** BUY | vol 5,370 / OI 58
- **SPY** CALL 755 2026-11-02 (3DTE): 500 @ 4.23 = **+$212k** BUY | vol 5,370 / OI 58
- **SPY** CALL 755 2026-11-02 (3DTE): 500 @ 4.23 = **+$212k** BUY | vol 5,370 / OI 58
- **MU** CALL 890 2026-11-02 (3DTE): 200 @ 10.55 = **+$211k** BUY | vol 3,460 / OI 340
- **MU** CALL 900 2026-11-02 (3DTE): 200 @ 7.05 = **+$141k** BUY | vol 5,569 / OI 165
- **SPY** PUT 767 2026-11-04 (5DTE): 100 @ 12.52 = **+$125k** SELL | vol 16,775 / OI 29,783
- **MU** CALL 890 2026-11-02 (3DTE): 107 @ 10.53 = **+$113k** BUY | vol 3,460 / OI 340
- **SPY** CALL 757 2026-10-30 (0DTE): 1,180 @ 0.89 = **+$105k** BUY | vol 127,310 / OI 786
- **TSLA** PUT 400 2026-10-30 (0DTE): 352 @ 2.38 = **+$84k** SELL | vol 122,670 / OI 4,157
- **MU** CALL 890 2026-11-02 (3DTE): 79 @ 10.53 = **+$83k** BUY | vol 3,460 / OI 340
- **MU** CALL 900 2026-11-02 (3DTE): 107 @ 7.03 = **+$75k** BUY | vol 5,569 / OI 165
- **AMD** PUT 500 2026-10-30 (0DTE): 242 @ 3.05 = **+$74k** SELL | vol 22,890 / OI 3,123
- **AMD** PUT 500 2026-11-04 (5DTE): 32 @ 22.15 = **+$71k** SELL | vol 536 / OI 171
- **META** PUT 650 2026-11-02 (3DTE): 22 @ 29.07 = **+$64k** SELL | vol 47 / OI 180

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 750 2026-11-10 (11DTE): 566 traded vs OI 230
- **SPY** CALL 775 2026-11-13 (14DTE): 1,741 traded vs OI 1,685
- **SPY** PUT 718 2026-11-20 (21DTE): 8,666 traded vs OI 1,210
- **SPY** PUT 722 2026-11-20 (21DTE): 21,981 traded vs OI 18,402
- **QQQ** PUT 691 2026-11-04 (5DTE): 563 traded vs OI 0
- **QQQ** PUT 665 2026-11-02 (3DTE): 3,781 traded vs OI 3,744
- **QQQ** CALL 711 2026-11-06 (7DTE): 513 traded vs OI 437
- **QQQ** PUT 700 2026-10-30 (0DTE): 42,102 traded vs OI 42,068
- **QQQ** CALL 722 2026-11-04 (5DTE): 504 traded vs OI 313
- **QQQ** PUT 669 2026-11-04 (5DTE): 504 traded vs OI 0
- **IWM** CALL 269 2026-11-20 (21DTE): 822 traded vs OI 322
- **SMH** CALL 537.5 2026-11-02 (3DTE): 608 traded vs OI 9
- **SMH** CALL 560 2026-11-06 (7DTE): 502 traded vs OI 371
- **SMH** CALL 537.5 2026-10-30 (0DTE): 821 traded vs OI 792
- **NVDA** PUT 200 2026-11-06 (7DTE): 12,456 traded vs OI 12,116

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
