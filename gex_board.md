# GEX + FLOW SCAN - Thu Oct 29, 01:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 284P | 0.65 | 0.22 | +3% (25m) | **-66%** (done) | +232% | 281.86 |
| 10:00 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 145C | 0.79 | 0.84 | +18% (37m) | **+6%** (done) | +139% | 143.92 |
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.68 | +17% (2m) | **-12%** (done) | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.18 | +20% (21m) | **-64%** (done) | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:20:08 ET, last candle SPY 13:19, QQQ 13:19 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 524.23 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 39 | none: 126 puts 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | POS +$525.7M | 502.17 | 525 | 530 | +$27.2M | +$351k bull / -$140k bear | out (clean 28, ADX 10, RVol 0.6) |
| 2 | **AAPL** | 349.93 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 33 | none: 55 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | POS +$649.6M | 340.82 | 350 | 345 | +$2.5M | +$388k bull / +$0 bear | out (clean 29, ADX 23, RVol 0.5) |
| 3 | **IWM** | 284.12 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 24 | 10/29 284P @ 0.40 (delta 0.46) = est +65% at 283.39 | POS +$806.2M | 282.59 | 284 | 270 | -$1.8M | - | out (clean 25, ADX 23, RVol 0.6) |
| 4 | **SMCI** | 34.98 | PINNED between the walls (positive gamma) - chop | **-** | 23 | - | POS +$23.8M | - | 35 | 35 | +$230k | - | out (clean 26, ADX 20, RVol 0.5) |
| 5 | **META** | 631.49 | - | **-** | 22 | - | POS +$17.0M | 629.97 | 650 | 625 | -$14.7M | +$319k bull / +$0 bear | out (clean 27, ADX 41, RVol 0.8) |
| 6 | **GOOGL** | 283.71 | - | **-** | 22 | - | NEG -$190.2M | - | 300 | 290 | -$9.7M | +$83k bull / +$0 bear | out (clean 32, ADX 37, RVol 1.3) |
| 7 | **MU** | 937.79 | - | **-** | 20 | - | POS +$289.0M | - | 950 | 900 | +$28.6M | +$3.1M bull / -$3.2M bear | out (clean 27, ADX 35, RVol 0.4) |
| 8 | **DELL** | 480.01 | - | **-** | 19 | - | POS +$1.1M | 478.63 | 500 | 460 | +$717k | +$257k bull / +$0 bear | out (clean 29, ADX 36, RVol 0.6) |
| 9 | **SPY** | 768.48 | - | **-** | 17 | - | NEG -$5.2B | 772.45 | 770 | 765 | -$106.6M | +$1.1M bull / -$907k bear | out (clean 25, ADX 11, RVol 0.4) |
| 10 | **TSLA** | 404.30 | - | **-** | 17 | - | POS +$487.0M | - | 400 | 400 | -$17.2M | +$629k bull / +$0 bear | out (clean 28, ADX 19, RVol 0.3) |
| 11 | **AMZN** | 246.01 | - | **-** | 17 | - | POS +$13.8M | 242.05 | 265 | 250 | -$6.2M | +$4.8M bull / -$1.1M bear | out (clean 32, ADX 21, RVol 0.7) |
| 12 | **QQQ** | 714.24 | - | **-** | 16 | - | NEG -$5.4B | 725.86 | 720 | 700 | -$67.1M | +$312k bull / -$200k bear | out (clean 26, ADX 15, RVol 0.4) |
| 13 | **SMH** | 560.43 | - | **-** | 15 | - | NEG -$53.6M | 563.18 | 560 | 555 | +$463k | +$58k bull / +$0 bear | out (clean 26, ADX 14, RVol 0.2) |
| 14 | **AMD** | 566.38 | - | **-** | 15 | - | POS +$142.0M | - | 600 | 550 | -$4.3M | +$252k bull / -$79k bear | out (clean 28, ADX 16, RVol 0.4) |
| 15 | **ARM** | 229.25 | - | **-** | 14 | - | POS +$3.3M | 222.25 | 227.5 | 230 | +$1.6M | - | out (clean 24, ADX 13, RVol 0.7) |
| 16 | **UBER** | 65.39 | - | **-** | 14 | - | NEG -$29.9M | 68.63 | 67 | 65 | -$169k | - | out (clean 27, ADX 10, RVol 0.4) |
| 17 | **NFLX** | 61.85 | - | **-** | 11 | - | NEG -$51.3M | 65.28 | 63 | 60 | -$480k | - | out (clean 31, ADX 23, RVol 1.1) |
| 18 | **ORCL** | 137.86 | - | **-** | 9 | - | POS +$116.2M | - | 135 | 140 | +$902k | - | out (clean 32, ADX 36, RVol 0.5) |
| 19 | **CRM** | 230.93 | - | **-** | 9 | - | NEG -$20.1M | - | 240 | 230 | -$228k | - | out (clean 27, ADX 14, RVol 0.8) |
| 20 | **BABA** | 99.44 | - | **-** | 7 | - | NEG -$18.3M | 101.57 | 100 | 100 | -$24k | - | out (clean 29, ADX 26, RVol 0.5) |
| 21 | **AVGO** | 345.15 | - | **-** | 6 | - | POS +$30.9M | 340.61 | 350 | 340 | +$1.9M | - | out (clean 27, ADX 13, RVol 0.4) |
| 22 | **COIN** | 161.67 | - | **-** | 6 | - | POS +$7.4M | - | 170 | 155 | -$240k | - | out (clean 26, ADX 10, RVol 1.0) |
| 23 | **SHOP** | 166.96 | - | **-** | 6 | - | NEG -$5.8M | 172.42 | 175 | 165 | -$32k | - | out (clean 26, ADX 10, RVol 0.4) |
| 24 | **NVDA** | 213.31 | - | **-** | 5 | - | POS +$206.2M | 211.12 | 215 | 210 | -$6.4M | - | out (clean 24, ADX 16, RVol 0.4) |
| 25 | **MSTR** | 142.72 | - | **-** | 5 | - | POS +$30.7M | - | 152.5 | 140 | -$377k | - | out (clean 25, ADX 15, RVol 0.6) |
| 26 | **HOOD** | 91.42 | - | **-** | 5 | - | NEG -$23.3M | 96.88 | 95 | 90 | -$514k | - | out (clean 27, ADX 12, RVol 0.5) |
| 27 | **PLTR** | 193.73 | - | **-** | 4 | - | POS +$18.9M | 191.86 | 200 | 190 | -$245k | - | out (clean 25, ADX 16, RVol 0.4) |

## Big prints this scan (73)
- **AMZN** CALL 247.5 2026-11-04 (6DTE): 380 @ 10.25 = **+$390k** BUY | vol 2,901 / OI 42
- **AMZN** PUT 240 2026-10-30 (1DTE): 500 @ 7.00 = **+$350k** SELL | vol 6,415 / OI 8,499
- **SPY** PUT 775 2026-11-02 (4DTE): 522 @ 6.40 = **+$334k** SELL | vol 22,992 / OI 149
- **AMZN** CALL 247.5 2026-11-04 (6DTE): 313 @ 10.25 = **+$321k** BUY | vol 2,901 / OI 42
- **AMZN** PUT 245 2026-10-30 (1DTE): 250 @ 9.35 = **+$234k** BUY | vol 6,544 / OI 3,801
- **AMZN** PUT 245 2026-10-30 (1DTE): 250 @ 9.35 = **+$234k** BUY | vol 6,544 / OI 3,801
- **AMZN** CALL 245 2026-11-04 (6DTE): 184 @ 11.45 = **+$211k** BUY | vol 1,132 / OI 7
- **AMZN** CALL 247.5 2026-11-04 (6DTE): 195 @ 10.25 = **+$200k** BUY | vol 2,901 / OI 42
- **AMZN** CALL 247.5 2026-11-04 (6DTE): 193 @ 10.25 = **+$198k** BUY | vol 2,901 / OI 42
- **SPY** PUT 775 2026-11-02 (4DTE): 291 @ 6.40 = **+$186k** SELL | vol 22,992 / OI 149
- **TSLA** CALL 400 2026-10-30 (1DTE): 220 @ 6.55 = **+$144k** BUY | vol 15,425 / OI 14,892
- **AMZN** CALL 247.5 2026-11-04 (6DTE): 115 @ 10.25 = **+$118k** BUY | vol 2,901 / OI 42
- **AMZN** CALL 247.5 2026-11-04 (6DTE): 114 @ 10.25 = **+$117k** BUY | vol 2,901 / OI 42
- **SPY** PUT 775 2026-11-02 (4DTE): 177 @ 6.40 = **+$113k** SELL | vol 22,992 / OI 149
- **QQQ** CALL 718 2026-11-03 (5DTE): 196 @ 5.27 = **+$103k** BUY | vol 2,099 / OI 147

## New unusual volume (traded more than open interest, 500+)
- **QQQ** CALL 733 2026-10-30 (1DTE): 1,971 traded vs OI 1,956
- **QQQ** PUT 707 2026-11-02 (4DTE): 525 traded vs OI 282
- **IWM** PUT 275 2026-10-29 (0DTE): 646 traded vs OI 635
- **NVDA** CALL 197.5 2026-11-04 (6DTE): 576 traded vs OI 36
- **NVDA** CALL 192.5 2026-11-04 (6DTE): 506 traded vs OI 1
- **NVDA** PUT 222.5 2026-11-06 (8DTE): 583 traded vs OI 145
- **AMD** PUT 585 2026-10-30 (1DTE): 797 traded vs OI 788
- **META** CALL 677.5 2026-10-30 (1DTE): 560 traded vs OI 505
- **AMZN** CALL 247.5 2026-11-04 (6DTE): 2,901 traded vs OI 42
- **AMZN** CALL 237.5 2026-10-30 (1DTE): 520 traded vs OI 343
- **AMZN** CALL 245 2026-11-04 (6DTE): 1,132 traded vs OI 7
- **ORCL** PUT 125 2026-11-06 (8DTE): 508 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
