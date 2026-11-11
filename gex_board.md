# GEX + FLOW SCAN - Wed Nov 11, 10:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (6)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:05 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 175C | 0.76 | 0.41 | -1% (0m) | **-46%** | +58% | 175 |
| 09:50 | **GOOGL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 292.5C | 0.51 | 0.51 | +14% (6m) | **+0%** | +82% | 291.86 |
| 09:45 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.68 | 0.61 | +85% (6m) | **-10%** | +68% | 282.96 |
| 09:45 | **QQQ** | **CALLS** | FLOW SURGE | 11/11 690C | 0.63 | 0.55 | +32% (23m) | **-13%** | +171% | 689.78 |
| 09:39 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 693C | 0.52 | 0.20 | -10% (0m) | **-62%** | +92% | 690.43 |
| 09:39 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 760C | 0.53 | 0.21 | -2% (0m) | **-60%** | +79% | 758.82 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:10:08 ET, last candle SPY 10:09, QQQ 10:09 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:02 | QQQ | 1m AGREE FLIP | FULL | CALLS | up | logged (agree flip) |
| 09:38 | QQQ | 1m WHIPSAW | R1 R5 | CALLS | TURNING away | **FIRE** QQQ261111C00693000 |
| 09:38 | SPY | 1m WHIPSAW | R1 R5 | CALLS | TURNING away | **FIRE** SPY261111C00760000 |

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 10:00 MSFT CALLS: price -4.55 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AMZN CALLS: price -0.73 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 AAPL PUTS: price +1.32 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSFT CALLS: price -2.01 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:50 NVDA CALLS: price -1.77 over the last 15 min - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DELL** | 368.28 | TREND (flow not with it) | **CALLS** | 56 | none: 30 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$1.2M | - | 380 | 340 | -$1.0M | +$68k bull / +$0 bear | LONG (clean 35, ADX 50, RVol 2.0) |
| 2 | **AVGO** | 350.80 | TREND + FLOW | **CALLS** | 53 | none: 112 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (47 contracts' greeks worked out here) | POS +$87.2M | - | 350 | 340 | +$1.0M | +$1.4M bull / -$398k bear | LONG (clean 35, ADX 50, RVol 2.1) |
| 3 | **MSFT** | 525.92 | FLOW SURGE | **CALLS** | 49 | none: 168 calls 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (64 contracts' greeks worked out here) | POS +$170.9M | 514.39 | 535 | 520 | +$5.3M | +$663k bull / +$0 bear | out (clean 31, ADX 29, RVol 1.8) |
| 4 | **MU** | 792.15 | FLOW SURGE | **PUTS** | 49 | none: 161 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (71 contracts' greeks worked out here) | POS +$162.2M | - | 800 | 800 | -$86.0M | +$0 bull / -$9.5M bear | out (clean 32, ADX 50, RVol 1.8) |
| 5 | **AMD** | 543.34 | FLOW SURGE | **PUTS** | 47 | none: 176 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (72 contracts' greeks worked out here) | POS +$119.4M | - | 550 | 500 | -$37.9M | +$0 bull / -$4.0M bear | out (clean 33, ADX 32, RVol 1.8) |
| 6 | **BABA** | 101.77 | FLOW SURGE | **CALLS** | 47 | none: 20 calls 0-7DTE > 2 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +16% at the target (needs +20%) (1 contracts' greeks worked out here) | NEG -$15.6M | 106.83 | 110 | 101 | +$304k | +$112k bull / +$0 bear | out (clean 29, ADX 30, RVol 1.0) |
| 7 | **NVDA** | 172.40 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 46 | 11/11 175C @ 0.45 (delta 0.23) = est +160% at 175 | NEG -$173.3M | - | 180 | 170 | +$6.7M | +$2.9M bull / -$3.2M bear | LONG (clean 34, ADX 27, RVol 1.1) |
| 8 | **GOOGL** | 290.59 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 43 | 11/11 292.5C @ 0.53 (delta 0.27) = est +98% at 292.52 | POS +$27.6M | 289.08 | 300 | 290 | +$530k | +$232k bull / -$28k bear | out (clean 28, ADX 40, RVol 1.1) |
| 9 | **PLTR** | 171.75 | FLOW SURGE | **CALLS** | 39 | none: 14 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$73.0M | - | 170 | 170 | +$1.7M | +$60k bull / +$0 bear | out (clean 30, ADX 42, RVol 0.6) |
| 10 | **AMZN** | 269.01 | - | **-** | 33 | - | POS +$506.7M | - | 270 | 265 | +$4.8M | +$88k bull / -$94k bear | out (clean 33, ADX 28, RVol 0.9) |
| 11 | **IWM** | 281.92 | TREND (flow not with it) | **CALLS** | 28 | 11/11 282C @ 0.56 (delta 0.48) = est +78% at 282.81 | NEG -$408.5M | 282.81 | 285 | 270 | -$129k | +$0 bull / -$91k bear | LONG (clean 35, ADX 38, RVol 1.2) |
| 12 | **ORCL** | 125.85 | - | **-** | 27 | - | NEG -$3.3M | 129.23 | 130 | 125 | +$800k | +$118k bull / -$50k bear | out (clean 28, ADX 41, RVol 1.7) |
| 13 | **SPY** | 755.89 | - | **-** | 22 | - | NEG -$4.4B | 761.08 | 760 | 750 | +$16.9M | +$100k bull / -$494k bear | out (clean 32, ADX 46, RVol 0.4) |
| 14 | **SMH** | 501.17 | - | **-** | 22 | - | NEG -$73.3M | - | 500 | 475 | +$280k | +$0 bull / -$240k bear | out (clean 30, ADX 35, RVol 2.0) |
| 15 | **META** | 637.44 | - | **-** | 22 | - | POS +$231.4M | 622.93 | 650 | 625 | +$2.5M | +$1.3M bull / -$43k bear | out (clean 31, ADX 25, RVol 1.1) |
| 16 | **ARM** | 193.29 | - | **-** | 22 | - | POS +$1.4M | 189.25 | 200 | 200 | -$279k | - | out (clean 28, ADX 50, RVol 0.5) |
| 17 | **AAPL** | 353.18 | - | **-** | 21 | - | POS +$1.3B | 340.36 | 355 | 350 | -$1.2M | +$460k bull / -$588k bear | out (clean 27, ADX 40, RVol 1.6) |
| 18 | **QQQ** | 686.10 | - | **-** | 20 | - | NEG -$776.0M | 689.7 | 700 | 680 | +$5.6M | +$1.0M bull / -$8.0M bear | out (clean 32, ADX 46, RVol 0.7) |
| 19 | **SMCI** | 29.77 | - | **-** | 20 | - | POS +$10.4M | - | 30 | 30 | -$188k | - | out (clean 31, ADX 42, RVol 1.1) |
| 20 | **TSLA** | 392.12 | - | **-** | 19 | - | POS +$398.6M | - | 400 | 380 | +$516k | +$202k bull / -$1.4M bear | out (clean 32, ADX 40, RVol 0.8) |
| 21 | **COIN** | 133.78 | - | **-** | 17 | - | POS +$14.3M | 126.91 | 137 | 135 | +$208k | - | out (clean 29, ADX 31, RVol 0.6) |
| 22 | **CRM** | 215.50 | - | **-** | 17 | - | NEG -$10.2M | - | 230 | 220 | -$30k | - | out (clean 31, ADX 30, RVol 1.2) |
| 23 | **MSTR** | 121.10 | - | **-** | 15 | - | NEG -$8.2M | 123.33 | 133 | 120 | +$69k | +$221k bull / +$0 bear | out (clean 28, ADX 15, RVol 0.8) |
| 24 | **NFLX** | 63.45 | - | **-** | 14 | - | NEG -$13.6M | 64.49 | 65 | 65 | +$162k | - | out (clean 28, ADX 19, RVol 1.1) |
| 25 | **SHOP** | 148.48 | - | **-** | 14 | - | POS +$3.1M | 144.3 | 150 | 140 | -$3k | - | out (clean 33, ADX 44, RVol 0.4) |
| 26 | **HOOD** | 83.13 | - | **-** | 12 | - | POS +$9.1M | 78.92 | 85 | 80 | -$106k | - | out (clean 32, ADX 29, RVol 1.0) |
| 27 | **UBER** | 69.32 | - | **-** | 8 | - | POS +$9.7M | 68.21 | 70 | 70 | +$3k | - | out (clean 33, ADX 23, RVol 0.7) |

## Big prints this scan (217)
- **QQQ** PUT 680 2026-11-12 (1DTE): 1,202 @ 2.57 = **+$309k** BUY | vol 4,422 / OI 429
- **MSFT** CALL 500 2026-11-13 (2DTE): 100 @ 30.50 = **+$305k** BUY | vol 110 / OI 126
- **QQQ** CALL 683 2026-11-12 (1DTE): 413 @ 5.76 = **+$238k** SELL | vol 1,514 / OI 730
- **QQQ** PUT 676 2026-11-12 (1DTE): 1,202 @ 1.66 = **+$200k** BUY | vol 2,779 / OI 240
- **QQQ** PUT 687 2026-11-11 (0DTE): 445 @ 4.32 = **+$192k** BUY | vol 31,179 / OI 220
- **QQQ** PUT 685 2026-11-11 (0DTE): 632 @ 2.97 = **+$188k** BUY | vol 46,765 / OI 484
- **MU** CALL 800 2026-11-16 (5DTE): 100 @ 18.20 = **+$182k** SELL | vol 943 / OI 273
- **MU** CALL 800 2026-11-16 (5DTE): 100 @ 17.49 = **+$175k** SELL | vol 943 / OI 273
- **MU** CALL 760 2026-11-13 (2DTE): 50 @ 34.18 = **+$171k** SELL | vol 799 / OI 1,430
- **MU** CALL 770 2026-11-13 (2DTE): 57 @ 26.20 = **+$149k** SELL | vol 1,242 / OI 1,107
- **GOOGL** PUT 290 2026-11-13 (2DTE): 480 @ 3.04 = **+$146k** SELL | vol 1,226 / OI 2,908
- **AMD** CALL 517.5 2026-11-11 (0DTE): 100 @ 14.57 = **+$146k** SELL | vol 391 / OI 1,052
- **MU** CALL 770 2026-11-11 (0DTE): 72 @ 18.05 = **+$130k** SELL | vol 5,271 / OI 1,346
- **MU** CALL 770 2026-11-11 (0DTE): 100 @ 12.10 = **+$121k** SELL | vol 5,271 / OI 1,346
- **MU** CALL 780 2026-11-13 (2DTE): 57 @ 20.85 = **+$119k** SELL | vol 1,675 / OI 1,313

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 736 2026-11-11 (0DTE): 1,056 traded vs OI 1,047
- **SPY** CALL 770 2026-11-12 (1DTE): 3,166 traded vs OI 2,833
- **SPY** CALL 768 2026-11-12 (1DTE): 988 traded vs OI 754
- **SPY** CALL 756 2026-11-16 (5DTE): 556 traded vs OI 472
- **SPY** CALL 759 2026-11-16 (5DTE): 576 traded vs OI 367
- **SPY** CALL 820 2026-11-18 (7DTE): 2,400 traded vs OI 302
- **SPY** CALL 830 2026-11-18 (7DTE): 600 traded vs OI 265
- **SPY** CALL 825 2026-11-18 (7DTE): 3,600 traded vs OI 210
- **SPY** PUT 755 2026-11-25 (14DTE): 504 traded vs OI 0
- **SPY** PUT 715 2026-11-25 (14DTE): 588 traded vs OI 0
- **QQQ** PUT 636 2026-11-11 (0DTE): 822 traded vs OI 120
- **QQQ** PUT 633 2026-11-11 (0DTE): 974 traded vs OI 943
- **QQQ** PUT 654 2026-11-11 (0DTE): 623 traded vs OI 391
- **QQQ** PUT 653 2026-11-11 (0DTE): 658 traded vs OI 653
- **QQQ** PUT 632 2026-11-11 (0DTE): 542 traded vs OI 399

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
