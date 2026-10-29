# GEX + FLOW SCAN - Thu Oct 29, 01:40 PM ET
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
Last 1m check 13:40:08 ET, last candle SPY 13:39, QQQ 13:39 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 525.64 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 40 | none: 126 puts 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$550.0M | 502.95 | 525 | 530 | +$26.3M | +$0 bull / -$88k bear | out (clean 27, ADX 11, RVol 0.8) |
| 2 | **IWM** | 283.81 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 34 | 10/29 284P @ 0.49 (delta 0.58) = est +72% at 283.13 | POS +$878.9M | 281.07 | 284 | 270 | -$1.5M | +$58k bull / +$0 bear | out (clean 25, ADX 20, RVol 0.7) |
| 3 | **ARM** | 229.96 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | none: 19 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$3.2M | 221.69 | 227.5 | 230 | +$1.5M | - | out (clean 24, ADX 11, RVol 1.1) |
| 4 | **AAPL** | 349.82 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 33 | none: 55 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | POS +$658.1M | 340.66 | 350 | 345 | +$3.9M | +$79k bull / -$31k bear | out (clean 29, ADX 22, RVol 0.4) |
| 5 | **SMCI** | 34.94 | PINNED between the walls (positive gamma) - chop | **-** | 23 | - | POS +$23.5M | - | 35 | 35 | +$230k | - | out (clean 26, ADX 22, RVol 0.4) |
| 6 | **GOOGL** | 283.57 | - | **-** | 22 | - | NEG -$187.4M | - | 300 | 290 | -$8.7M | +$202k bull / +$0 bear | out (clean 32, ADX 37, RVol 1.3) |
| 7 | **DELL** | 479.57 | - | **-** | 21 | - | NEG -$273k | 479.13 | 500 | 480 | +$1.1M | +$437k bull / +$0 bear | out (clean 30, ADX 40, RVol 0.6) |
| 8 | **META** | 626.63 | - | **-** | 20 | - | NEG -$37.8M | 629.26 | 650 | 625 | -$13.3M | +$472k bull / +$0 bear | out (clean 28, ADX 34, RVol 0.7) |
| 9 | **MU** | 938.87 | - | **-** | 20 | - | POS +$296.8M | 883.47 | 950 | 900 | +$27.9M | +$3.0M bull / -$1.7M bear | out (clean 27, ADX 36, RVol 0.4) |
| 10 | **SPY** | 768.17 | - | **-** | 17 | - | NEG -$5.6B | 772.37 | 770 | 765 | -$107.2M | +$1.3M bull / +$0 bear | out (clean 25, ADX 14, RVol 0.4) |
| 11 | **TSLA** | 404.79 | - | **-** | 17 | - | POS +$498.4M | - | 400 | 400 | -$19.7M | +$104k bull / -$793k bear | out (clean 28, ADX 17, RVol 0.3) |
| 12 | **AMZN** | 246.03 | - | **-** | 17 | - | POS +$12.1M | 242.41 | 265 | 250 | -$6.1M | +$33k bull / -$887k bear | out (clean 31, ADX 19, RVol 0.8) |
| 13 | **QQQ** | 714.25 | - | **-** | 16 | - | NEG -$5.3B | 725.52 | 720 | 700 | -$64.6M | +$348k bull / -$364k bear | out (clean 26, ADX 17, RVol 0.5) |
| 14 | **SMH** | 560.99 | - | **-** | 16 | - | NEG -$54.9M | 563.55 | 560 | 555 | +$576k | +$108k bull / +$0 bear | out (clean 26, ADX 14, RVol 0.4) |
| 15 | **NVDA** | 213.49 | - | **-** | 15 | - | POS +$218.7M | 211.11 | 215 | 210 | -$6.8M | +$51k bull / -$165k bear | out (clean 24, ADX 15, RVol 0.4) |
| 16 | **AMD** | 567.11 | - | **-** | 15 | - | POS +$140.7M | - | 600 | 550 | -$3.7M | +$504k bull / -$345k bear | out (clean 28, ADX 17, RVol 0.3) |
| 17 | **AVGO** | 345.42 | - | **-** | 14 | - | POS +$36.0M | 340.41 | 350 | 340 | +$427k | +$0 bull / -$5.0M bear | out (clean 27, ADX 16, RVol 0.4) |
| 18 | **UBER** | 65.29 | - | **-** | 13 | - | NEG -$30.3M | 68.51 | 67 | 65 | -$168k | - | out (clean 27, ADX 10, RVol 0.5) |
| 19 | **NFLX** | 61.78 | - | **-** | 11 | - | NEG -$51.7M | 65.02 | 63 | 60 | -$467k | - | out (clean 31, ADX 24, RVol 1.0) |
| 20 | **ORCL** | 137.35 | - | **-** | 10 | - | POS +$123.8M | - | 135 | 140 | +$936k | - | out (clean 32, ADX 40, RVol 0.4) |
| 21 | **CRM** | 231.24 | - | **-** | 8 | - | NEG -$20.5M | - | 240 | 230 | -$229k | - | out (clean 27, ADX 11, RVol 0.5) |
| 22 | **COIN** | 160.47 | - | **-** | 6 | - | POS +$4.8M | 153.68 | 170 | 155 | -$192k | - | out (clean 25, ADX 10, RVol 0.8) |
| 23 | **BABA** | 99.41 | - | **-** | 6 | - | NEG -$18.4M | 101.29 | 100 | 100 | -$26k | - | out (clean 28, ADX 24, RVol 0.4) |
| 24 | **SHOP** | 166.84 | - | **-** | 5 | - | NEG -$4.8M | 170.38 | 175 | 165 | -$32k | - | out (clean 25, ADX 9, RVol 0.5) |
| 25 | **PLTR** | 193.96 | - | **-** | 4 | - | POS +$17.9M | 192.05 | 200 | 190 | -$323k | - | out (clean 25, ADX 16, RVol 0.4) |
| 26 | **MSTR** | 142.24 | - | **-** | 4 | - | POS +$28.5M | - | 152.5 | 140 | -$242k | - | out (clean 25, ADX 12, RVol 0.7) |
| 27 | **HOOD** | 91.19 | - | **-** | 4 | - | NEG -$24.3M | - | 95 | 90 | -$456k | - | out (clean 27, ADX 12, RVol 0.2) |

## Big prints this scan (29)
- **MU** CALL 940 2026-10-30 (1DTE): 250 @ 13.20 = **+$330k** SELL | vol 7,145 / OI 2,522
- **MU** PUT 930 2026-11-02 (4DTE): 146 @ 15.47 = **+$226k** MID | vol 769 / OI 136
- **MU** PUT 920 2026-11-02 (4DTE): 163 @ 11.57 = **+$189k** BUY | vol 757 / OI 123
- **AMZN** CALL 240 2026-10-30 (1DTE): 88 @ 13.18 = **+$116k** MID | vol 3,338 / OI 742
- **SPY** CALL 767 2026-10-29 (0DTE): 482 @ 2.15 = **+$104k** BUY | vol 40,867 / OI 1,002
- **DELL** PUT 490 2026-10-30 (1DTE): 50 @ 13.94 = **+$70k** SELL | vol 417 / OI 639
- **TSLA** CALL 405 2026-10-30 (1DTE): 200 @ 3.45 = **+$69k** BUY | vol 52,388 / OI 4,208
- **TSLA** PUT 407.5 2026-10-30 (1DTE): 133 @ 4.75 = **+$63k** MID | vol 8,594 / OI 835
- **MU** CALL 900 2026-11-02 (4DTE): 12 @ 45.51 = **+$55k** BUY | vol 1,140 / OI 169
- **MU** CALL 940 2026-10-30 (1DTE): 40 @ 13.63 = **+$55k** BUY | vol 7,145 / OI 2,522
- **AMD** CALL 567.5 2026-10-30 (1DTE): 45 @ 9.20 = **+$41k** SELL | vol 2,804 / OI 740
- **MU** CALL 930 2026-11-02 (4DTE): 15 @ 24.85 = **+$37k** BUY | vol 416 / OI 269
- **MU** CALL 900 2026-11-02 (4DTE): 8 @ 45.51 = **+$36k** BUY | vol 1,140 / OI 169
- **TSLA** CALL 405 2026-10-30 (1DTE): 100 @ 3.45 = **+$34k** BUY | vol 52,388 / OI 4,208
- **MU** PUT 950 2026-10-30 (1DTE): 17 @ 19.61 = **+$33k** SELL | vol 12,339 / OI 2,369

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 732 2026-11-03 (5DTE): 522 traded vs OI 54
- **SPY** PUT 734 2026-11-03 (5DTE): 512 traded vs OI 155
- **SPY** PUT 767 2026-11-04 (6DTE): 11,572 traded vs OI 11,544
- **IWM** PUT 281 2026-11-02 (4DTE): 529 traded vs OI 93
- **NVDA** CALL 210 2026-11-06 (8DTE): 905 traded vs OI 900
- **TSLA** CALL 420 2026-11-04 (6DTE): 849 traded vs OI 809
- **TSLA** PUT 387.5 2026-11-02 (4DTE): 583 traded vs OI 376
- **AMD** PUT 520 2026-11-02 (4DTE): 509 traded vs OI 287
- **AVGO** CALL 362.5 2026-10-30 (1DTE): 1,021 traded vs OI 1,015
- **ORCL** PUT 130 2026-11-06 (8DTE): 1,566 traded vs OI 1,500

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
