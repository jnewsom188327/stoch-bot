# GEX + FLOW SCAN - Wed Nov 04, 10:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (6)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:20 | **SMCI** | **CALLS** | FLOW SURGE | 11/06 33C | 0.65 | 0.24 | -3% (1m) | **-63%** | +39% | 32.81 |
| 10:20 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 284C | 0.49 | 0.25 | +2% (22m) | **-49%** | +131% | 284.74 |
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 1.46 | +126% (45m) | **+115%** | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.52 | +168% (52m) | **+153%** | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.02 | +2% (1m) | **-96%** | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.10 | -3% (1m) | **-84%** (done) | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:50:08 ET, last candle SPY 10:49, QQQ 10:49 | no errors

## Flow surges NOT fired - price disagreed (28 today, last 5)
- 10:50 SMCI CALLS: price -1.23 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:50 AAPL PUTS: over EMA 20 - flow says one way, price says the other
- 10:45 AAPL PUTS: price +0.02 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 AAPL PUTS: price +1.07 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:35 GOOGL PUTS: over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BABA** | 106.97 | TREND (flow not with it) | **CALLS** | 64 | 11/06 111C @ 0.54 (delta 0.20) = est +32% at 108.05 | POS +$16.5M | - | 110 | 110 | -$993k | +$57k bull / +$0 bear | LONG (clean 36, ADX 63, RVol 2.6) |
| 2 | **SMCI** | 30.52 | FLOW SURGE | **CALLS** | 55 | 11/06 32C @ 0.42 (delta 0.28) = est +125% at 32.03 | NEG -$484k | 32.03 | 33 | 30 | +$1.6M | +$34k bull / +$0 bear | out (clean 33, ADX 29, RVol 2.6) |
| 3 | **MU** | 804.70 | FLOW SURGE | **CALLS** | 53 | none: 139 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (65 contracts' greeks worked out here) | NEG -$345.0M | - | 850 | 800 | +$82.2M | +$6.6M bull / +$0 bear | out (clean 31, ADX 27, RVol 2.8) |
| 4 | **GOOGL** | 292.81 | TREND (flow not with it) | **CALLS** | 51 | 11/04 295C @ 0.72 (delta 0.29) = est +591% at 300 | POS +$94.7M | 284.39 | 300 | 290 | -$28.3M | +$1.9M bull / +$0 bear | LONG (clean 35, ADX 56, RVol 1.1) |
| 5 | **TSLA** | 388.73 | FLOW SURGE | **PUTS** | 50 | none: 128 puts 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (54 contracts' greeks worked out here) | NEG -$103.0M | 396.52 | 400 | 380 | -$80.1M | +$929k bull / -$1.4M bear | out (clean 30, ADX 22, RVol 2.5) |
| 6 | **AAPL** | 352.99 | FLOW SURGE | **PUTS** | 49 | 11/04 350P @ 0.80 (delta 0.26) = est +91% at 350 | POS +$954.8M | 341.82 | 355 | 350 | -$86.0M | +$703k bull / -$954k bear | out (clean 32, ADX 60, RVol 1.7) |
| 7 | **SMH** | 504.05 | FLOW SURGE | **CALLS** | 48 | none: 156 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (79 contracts' greeks worked out here) | NEG -$528.6M | - | 532.5 | 500 | +$3.3M | +$286k bull / +$0 bear | out (clean 31, ADX 29, RVol 2.0) |
| 8 | **COIN** | 150.00 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 46 | none: 22 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$30.6M | - | 148 | 150 | -$1.1M | +$31k bull / +$0 bear | out (clean 31, ADX 19, RVol 1.3) |
| 9 | **ARM** | 194.02 | FLOW SURGE | **CALLS** | 44 | none: 16 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$6.8M | - | 212.5 | 200 | +$773k | +$27k bull / +$0 bear | out (clean 26, ADX 28, RVol 0.7) |
| 10 | **MSFT** | 552.80 | - | **-** | 30 | - | POS +$994.3M | - | 550 | 535 | -$18.7M | +$666k bull / -$628k bear | out (clean 29, ADX 68, RVol 2.1) |
| 11 | **CRM** | 232.55 | - | **-** | 29 | - | NEG -$5.8M | 238.29 | 240 | 220 | -$280k | +$0 bull / -$104k bear | out (clean 31, ADX 61, RVol 0.9) |
| 12 | **AMZN** | 267.65 | - | **-** | 28 | - | POS +$537.5M | - | 270 | 250 | -$22.4M | +$1.5M bull / +$0 bear | out (clean 35, ADX 57, RVol 1.7) |
| 13 | **UBER** | 71.70 | - | **-** | 27 | - | POS +$12.3M | 68.08 | 70 | 70 | -$1.4M | - | out (clean 31, ADX 61, RVol 1.5) |
| 14 | **IWM** | 282.43 | - | **-** | 26 | - | NEG -$716.2M | 284.63 | 285 | 270 | +$15.1M | +$210k bull / -$91k bear | out (clean 34, ADX 23, RVol 1.2) |
| 15 | **SPY** | 765.40 | - | **-** | 25 | - | NEG -$4.5B | 770.07 | 770 | 750 | -$75.9M | +$593k bull / -$2.1M bear | out (clean 31, ADX 42, RVol 1.8) |
| 16 | **AMD** | 481.52 | - | **-** | 25 | - | NEG -$101.7M | - | 500 | 500 | +$41.4M | +$3.3M bull / -$107k bear | out (clean 32, ADX 22, RVol 1.5) |
| 17 | **QQQ** | 693.28 | - | **-** | 24 | - | NEG -$4.9B | 720.76 | 700 | 680 | -$129.2M | +$5.6M bull / +$0 bear | out (clean 30, ADX 33, RVol 1.4) |
| 18 | **META** | 632.70 | - | **-** | 23 | - | POS +$180.1M | 619.49 | 650 | 625 | +$7.5M | +$1.5M bull / -$664k bear | out (clean 30, ADX 45, RVol 1.1) |
| 19 | **MSTR** | 143.13 | - | **-** | 22 | - | POS +$125.1M | - | 135 | 150 | +$931k | +$883k bull / -$253k bear | out (clean 31, ADX 46, RVol 1.4) |
| 20 | **NVDA** | 202.67 | - | **-** | 21 | - | NEG -$80.9M | 203.97 | 210 | 200 | +$1.7M | +$832k bull / -$31k bear | out (clean 29, ADX 35, RVol 2.1) |
| 21 | **DELL** | 373.70 | - | **-** | 21 | - | NEG -$30.1M | - | 400 | 400 | +$931k | +$370k bull / +$0 bear | out (clean 32, ADX 34, RVol 1.2) |
| 22 | **NFLX** | 66.26 | - | **-** | 20 | - | POS +$18.5M | 62.7 | 65 | 65 | -$2.1M | - | out (clean 30, ADX 68, RVol 1.5) |
| 23 | **PLTR** | 174.52 | - | **-** | 18 | - | NEG -$44.9M | - | 180 | 170 | -$1.8M | +$656k bull / -$31k bear | out (clean 26, ADX 15, RVol 1.2) |
| 24 | **ORCL** | 126.32 | - | **-** | 17 | - | NEG -$30.4M | - | 130 | 125 | -$76k | +$225k bull / -$149k bear | out (clean 35, ADX 15, RVol 2.2) |
| 25 | **HOOD** | 86.22 | - | **-** | 16 | - | POS +$698k | 85.59 | 90 | 90 | -$215k | +$121k bull / +$0 bear | out (clean 29, ADX 18, RVol 1.1) |
| 26 | **AVGO** | 325.27 | - | **-** | 15 | - | NEG -$99.0M | - | 340 | 320 | +$3.9M | - | out (clean 30, ADX 28, RVol 1.4) |
| 27 | **SHOP** | 149.37 | - | **-** | 10 | - | NEG -$8.2M | - | 160 | 135 | -$61k | - | out (clean 35, ADX 26, RVol 1.5) |

## Big prints this scan (94)
- **QQQ** PUT 668 2026-11-06 (2DTE): 6,650 @ 0.77 = **+$512k** SELL | vol 7,107 / OI 0
- **MU** PUT 815 2026-11-04 (0DTE): 599 @ 5.95 = **+$356k** SELL | vol 10,300 / OI 537
- **QQQ** PUT 664 2026-11-06 (2DTE): 6,000 @ 0.57 = **+$342k** SELL | vol 6,357 / OI 0
- **QQQ** CALL 662 2026-11-04 (0DTE): 68 @ 35.42 = **+$241k** BUY | vol 73 / OI 0
- **MU** PUT 840 2026-11-04 (0DTE): 100 @ 24.00 = **+$240k** SELL | vol 3,788 / OI 1,021
- **QQQ** PUT 682 2026-11-06 (2DTE): 1,000 @ 2.22 = **+$222k** SELL | vol 2,686 / OI 8,965
- **QQQ** PUT 676 2026-11-06 (2DTE): 1,350 @ 1.41 = **+$190k** SELL | vol 2,702 / OI 9,134
- **QQQ** PUT 703 2026-11-10 (6DTE): 132 @ 11.89 = **+$157k** SELL | vol 209 / OI 0
- **MU** PUT 815 2026-11-04 (0DTE): 200 @ 6.50 = **+$130k** SELL | vol 10,300 / OI 537
- **META** CALL 625 2026-11-04 (0DTE): 200 @ 6.00 = **+$120k** SELL | vol 1,201 / OI 919
- **MU** PUT 820 2026-11-04 (0DTE): 149 @ 8.00 = **+$119k** SELL | vol 11,816 / OI 1,070
- **SPY** CALL 756 2026-11-06 (2DTE): 90 @ 11.80 = **+$106k** BUY | vol 1,041 / OI 1,403
- **QQQ** PUT 672 2026-11-06 (2DTE): 1,000 @ 1.05 = **+$105k** SELL | vol 1,132 / OI 0
- **MU** PUT 800 2026-11-06 (2DTE): 99 @ 10.36 = **+$103k** SELL | vol 2,940 / OI 3,802
- **AAPL** PUT 352.5 2026-11-06 (2DTE): 261 @ 3.45 = **+$90k** SELL | vol 2,729 / OI 197

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 773 2026-11-06 (2DTE): 3,089 traded vs OI 2,988
- **SPY** CALL 786 2026-11-09 (5DTE): 521 traded vs OI 0
- **SPY** PUT 739 2026-11-05 (1DTE): 529 traded vs OI 0
- **SPY** CALL 783 2026-11-10 (6DTE): 575 traded vs OI 0
- **SPY** PUT 758 2026-11-06 (2DTE): 3,023 traded vs OI 2,763
- **SPY** PUT 765 2026-11-11 (7DTE): 514 traded vs OI 396
- **SPY** CALL 790 2026-11-16 (12DTE): 523 traded vs OI 90
- **SPY** PUT 742 2026-11-16 (12DTE): 503 traded vs OI 0
- **SPY** CALL 768 2026-11-27 (23DTE): 734 traded vs OI 706
- **QQQ** PUT 685 2026-11-10 (6DTE): 514 traded vs OI 444
- **QQQ** PUT 672 2026-11-06 (2DTE): 1,132 traded vs OI 0
- **QQQ** PUT 664 2026-11-06 (2DTE): 6,357 traded vs OI 0
- **QQQ** PUT 668 2026-11-06 (2DTE): 7,107 traded vs OI 0
- **QQQ** PUT 690 2026-11-16 (12DTE): 802 traded vs OI 191
- **QQQ** PUT 690 2026-12-04 (30DTE): 506 traded vs OI 474

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
