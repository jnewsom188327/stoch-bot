# GEX + FLOW SCAN - Mon Nov 02, 09:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:50:08 ET, last candle SPY 09:49, QQQ 09:49 | no errors

## Flow surges NOT fired - price disagreed (1 today, last 5)
- 09:50 BABA PUTS: price +0.75 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMCI** | 32.98 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 73 | none: 13 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$549k | - | 35 | 33 | +$213k | +$140k bull / +$0 bear | out (clean 31, ADX 48, RVol 3.7) |
| 2 | **AMZN** | 250.53 | PINNED between the walls (positive gamma) - chop | **-** | 65 | - | POS +$91.7M | 241.81 | 250 | 250 | -$12.8M | +$0 bull / -$84k bear | out (clean 31, ADX 39, RVol 3.4) |
| 3 | **SMH** | 527.02 | FLOW SURGE | **CALLS** | 64 | none: 168 calls 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (68 contracts' greeks worked out here) | NEG -$329.4M | - | 532.5 | 500 | +$2.6M | +$995k bull / -$211k bear | out (clean 31, ADX 37, RVol 4.0) |
| 4 | **GOOGL** | 286.39 | FLOW SURGE | **PUTS** | 64 | none: 92 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (37 contracts' greeks worked out here) | NEG -$68.0M | - | 285 | 290 | -$3.1M | +$0 bull / -$743k bear | LONG (clean 33, ADX 43, RVol 2.6) |
| 5 | **TSLA** | 400.20 | PINNED between the walls (positive gamma) - chop | **-** | 63 | - | POS +$189.6M | - | 400 | 400 | +$20.9M | +$4.0M bull / +$0 bear | out (clean 30, ADX 32, RVol 4.2) |
| 6 | **AMD** | 505.13 | FLOW SURGE | **CALLS** | 63 | none: 164 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (65 contracts' greeks worked out here) | NEG -$95.0M | - | 550 | 500 | +$7.5M | +$6.0M bull / +$0 bear | out (clean 30, ADX 34, RVol 3.9) |
| 7 | **DELL** | 416.02 | FLOW SURGE | **CALLS** | 61 | none: 34 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$24.5M | - | 440 | 400 | +$857k | +$100k bull / +$0 bear | out (clean 34, ADX 26, RVol 3.2) |
| 8 | **MSTR** | 133.59 | FLOW SURGE | **CALLS** | 59 | none: 26 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$2.4M | - | 135 | 125 | +$1.3M | +$244k bull / -$33k bear | out (clean 27, ADX 34, RVol 5.6) |
| 9 | **BABA** | 103.58 | FLOW SURGE | **PUTS** | 59 | 11/06 99P @ 0.69 (delta 0.21) = est +66% at 101.52 | POS +$2.0M | 101.52 | 105 | 100 | -$753k | +$0 bull / -$217k bear | out (clean 32, ADX 41, RVol 6.4) |
| 10 | **ORCL** | 123.78 | FLOW SURGE | **CALLS** | 58 | none: 25 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$39.0M | - | 130 | 120 | +$821k | +$208k bull / +$0 bear | out (clean 32, ADX 31, RVol 3.4) |
| 11 | **MU** | 878.78 | FLOW SURGE | **CALLS** | 57 | none: 149 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (56 contracts' greeks worked out here) | NEG -$211.0M | - | 910 | 900 | +$11.7M | +$5.9M bull / +$0 bear | out (clean 31, ADX 30, RVol 3.9) |
| 12 | **UBER** | 67.00 | FLOW SURGE | **PUTS** | 57 | none: 13 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$8.4M | - | 70 | 65 | -$147k | +$0 bull / -$28k bear | out (clean 26, ADX 30, RVol 1.9) |
| 13 | **AAPL** | 340.36 | FLOW SURGE | **CALLS** | 56 | none: 81 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$45.9M | 337.09 | 350 | 330 | +$2.8M | +$1.2M bull / +$0 bear | out (clean 32, ADX 28, RVol 5.0) |
| 14 | **MSFT** | 524.71 | FLOW SURGE | **PUTS** | 55 | none: 168 puts 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (95 contracts' greeks worked out here) | POS +$352.2M | 497.34 | 540 | 530 | -$1.9M | +$0 bull / -$135k bear | out (clean 26, ADX 22, RVol 4.1) |
| 15 | **COIN** | 140.73 | - | **-** | 31 | - | NEG -$8.1M | - | 150 | 130 | +$162k | - | out (clean 27, ADX 40, RVol 5.0) |
| 16 | **ARM** | 202.14 | - | **-** | 30 | - | NEG -$7.0M | - | 220 | 200 | +$167k | - | out (clean 26, ADX 27, RVol 4.8) |
| 17 | **CRM** | 230.93 | - | **-** | 30 | - | NEG -$4.8M | 241.49 | 240 | 220 | -$7k | - | out (clean 28, ADX 29, RVol 2.3) |
| 18 | **IWM** | 281.39 | - | **-** | 28 | - | NEG -$1.0B | 286.57 | 285 | 270 | +$800k | +$57k bull / +$0 bear | out (clean 31, ADX 36, RVol 3.7) |
| 19 | **PLTR** | 185.27 | - | **-** | 26 | - | NEG -$11.1M | - | 200 | 180 | +$583k | +$258k bull / +$0 bear | out (clean 26, ADX 14, RVol 5.0) |
| 20 | **NFLX** | 62.49 | - | **-** | 25 | - | NEG -$21.4M | - | 63 | 60 | +$181k | - | out (clean 30, ADX 36, RVol 4.6) |
| 21 | **SPY** | 760.32 | - | **-** | 24 | - | NEG -$9.5B | 775.7 | 770 | 750 | -$4.1M | +$0 bull / -$3.2M bear | out (clean 29, ADX 37, RVol 6.8) |
| 22 | **NVDA** | 208.69 | - | **-** | 24 | - | NEG -$166.4M | 215.14 | 210 | 210 | -$1.2M | +$111k bull / -$1.6M bear | out (clean 29, ADX 36, RVol 3.5) |
| 23 | **AVGO** | 328.19 | - | **-** | 24 | - | NEG -$111.8M | - | 340 | 330 | +$291k | +$0 bull / -$108k bear | out (clean 30, ADX 37, RVol 3.3) |
| 24 | **QQQ** | 695.53 | - | **-** | 22 | - | NEG -$5.6B | 733.24 | 720 | 680 | -$285k | +$4.2M bull / -$1.3M bear | out (clean 29, ADX 37, RVol 4.2) |
| 25 | **META** | 615.21 | - | **-** | 22 | - | NEG -$111.6M | 627.47 | 650 | 600 | -$407k | +$273k bull / -$241k bear | out (clean 29, ADX 31, RVol 2.1) |
| 26 | **SHOP** | 158.09 | - | **-** | 21 | - | NEG -$365k | - | 170 | 160 | -$26k | - | out (clean 28, ADX 42, RVol 7.3) |
| 27 | **HOOD** | 86.28 | - | **-** | 20 | - | NEG -$9.1M | - | 93 | 90 | +$133k | - | out (clean 32, ADX 51, RVol 3.4) |

## Big prints this scan (411)
- **QQQ** PUT 728 2026-11-06 (4DTE): 638 @ 33.44 = **+$2.1M** SELL | vol 639 / OI 1,969
- **QQQ** PUT 690 2026-11-06 (4DTE): 638 @ 7.50 = **+$478k** BUY | vol 1,239 / OI 13,512
- **MU** CALL 865 2026-11-02 (0DTE): 225 @ 18.50 = **+$416k** BUY | vol 294 / OI 463
- **SPY** CALL 754 2026-11-06 (4DTE): 410 @ 9.78 = **+$401k** SELL | vol 5,385 / OI 33
- **SPY** CALL 754 2026-11-06 (4DTE): 407 @ 9.75 = **+$397k** SELL | vol 5,385 / OI 33
- **SPY** CALL 754 2026-11-06 (4DTE): 409 @ 9.69 = **+$396k** SELL | vol 5,385 / OI 33
- **SPY** PUT 754 2026-11-06 (4DTE): 1,000 @ 3.92 = **+$392k** BUY | vol 3,051 / OI 1,038
- **SPY** CALL 754 2026-11-06 (4DTE): 396 @ 9.81 = **+$388k** SELL | vol 5,385 / OI 33
- **MU** PUT 900 2026-11-09 (7DTE): 100 @ 38.30 = **+$383k** SELL | vol 101 / OI 131
- **MU** PUT 900 2026-11-06 (4DTE): 100 @ 35.60 = **+$356k** SELL | vol 131 / OI 1,356
- **TSLA** PUT 407.5 2026-11-06 (4DTE): 306 @ 11.10 = **+$340k** SELL | vol 506 / OI 1,311
- **NVDA** CALL 205 2026-11-02 (0DTE): 898 @ 3.25 = **+$292k** SELL | vol 3,631 / OI 254
- **AMD** CALL 510 2026-11-09 (7DTE): 100 @ 26.18 = **+$262k** BUY | vol 215 / OI 2
- **TSLA** CALL 400 2026-11-02 (0DTE): 243 @ 10.70 = **+$260k** BUY | vol 1,536 / OI 1,359
- **AMD** CALL 510 2026-11-09 (7DTE): 100 @ 25.93 = **+$259k** BUY | vol 215 / OI 2

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 740 2026-11-04 (2DTE): 1,689 traded vs OI 1,479
- **SPY** PUT 743 2026-11-02 (0DTE): 1,063 traded vs OI 513
- **SPY** CALL 760 2026-11-04 (2DTE): 703 traded vs OI 255
- **SPY** CALL 754 2026-11-02 (0DTE): 638 traded vs OI 20
- **SPY** PUT 754 2026-11-06 (4DTE): 3,051 traded vs OI 1,038
- **SPY** CALL 759 2026-11-04 (2DTE): 665 traded vs OI 229
- **SPY** CALL 770 2026-11-02 (0DTE): 6,262 traded vs OI 3,857
- **SPY** CALL 759 2026-11-03 (1DTE): 1,072 traded vs OI 33
- **SPY** PUT 756 2026-11-03 (1DTE): 671 traded vs OI 466
- **SPY** CALL 756 2026-11-02 (0DTE): 1,040 traded vs OI 51
- **SPY** CALL 768 2026-11-02 (0DTE): 4,373 traded vs OI 1,395
- **SPY** PUT 705 2026-11-04 (2DTE): 900 traded vs OI 482
- **SPY** CALL 754 2026-11-06 (4DTE): 5,385 traded vs OI 33
- **SPY** PUT 695 2026-11-04 (2DTE): 765 traded vs OI 224
- **SPY** PUT 739 2026-11-03 (1DTE): 516 traded vs OI 375

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
