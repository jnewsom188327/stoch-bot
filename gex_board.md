# GEX + FLOW SCAN - Wed Nov 04, 11:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (6)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:20 | **SMCI** | **CALLS** | FLOW SURGE | 11/06 33C | 0.65 | 0.20 | -3% (1m) | **-69%** | +39% | 32.81 |
| 10:20 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 284C | 0.49 | 0.25 | +2% (22m) | **-49%** | +131% | 284.74 |
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 1.83 | +169% (60m) | **+169%** | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.56 | +168% (52m) | **+160%** (done) | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.06 | +2% (1m) | **-89%** (done) | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.10 | -3% (1m) | **-84%** (done) | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:00:08 ET, last candle SPY 10:59, QQQ 10:59 | no errors

## Flow surges NOT fired - price disagreed (28 today, last 5)
- 10:50 SMCI CALLS: price -1.23 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:50 AAPL PUTS: over EMA 20 - flow says one way, price says the other
- 10:45 AAPL PUTS: price +0.02 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 AAPL PUTS: price +1.07 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:35 GOOGL PUTS: over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMH** | 502.18 | FLOW SURGE | **CALLS** | 56 | none: 154 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (63 contracts' greeks worked out here) | NEG -$520.8M | - | 532.5 | 500 | +$4.6M | +$307k bull / +$0 bear | out (clean 32, ADX 33, RVol 3.8) |
| 2 | **MU** | 800.68 | FLOW SURGE | **CALLS** | 53 | none: 136 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (60 contracts' greeks worked out here) | NEG -$335.2M | - | 850 | 800 | +$104.7M | +$8.5M bull / +$0 bear | out (clean 31, ADX 31, RVol 2.5) |
| 3 | **BABA** | 107.59 | TREND (flow not with it) | **CALLS** | 53 | 11/06 111C @ 0.68 (delta 0.24) = est +29% at 108.68 | POS +$15.7M | - | 110 | 110 | -$1.1M | - | LONG (clean 36, ADX 65, RVol 2.5) |
| 4 | **AMZN** | 266.77 | TREND (flow not with it) | **CALLS** | 52 | 11/04 270C @ 0.46 (delta 0.21) = est +182% at 270 | POS +$544.7M | - | 270 | 250 | -$20.3M | +$943k bull / +$0 bear | LONG (clean 35, ADX 55, RVol 2.0) |
| 5 | **AAPL** | 353.84 | - | **-** | 37 | - | POS +$1.0B | 341.56 | 355 | 350 | -$87.7M | +$741k bull / -$615k bear | out (clean 32, ADX 61, RVol 2.0) |
| 6 | **GOOGL** | 293.65 | - | **-** | 32 | - | POS +$102.1M | 283.49 | 300 | 290 | -$28.7M | +$260k bull / -$28k bear | out (clean 35, ADX 54, RVol 0.9) |
| 7 | **COIN** | 149.72 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 31 | none: 21 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$28.2M | - | 148 | 150 | -$1.1M | - | out (clean 31, ADX 17, RVol 0.7) |
| 8 | **MSFT** | 551.75 | - | **-** | 28 | - | POS +$1.0B | - | 550 | 535 | -$16.0M | +$1.1M bull / +$0 bear | out (clean 29, ADX 67, RVol 1.8) |
| 9 | **UBER** | 72.18 | - | **-** | 28 | - | POS +$13.2M | 67.9 | 75 | 70 | -$1.5M | - | out (clean 31, ADX 64, RVol 1.6) |
| 10 | **TSLA** | 387.55 | - | **-** | 27 | - | NEG -$104.3M | 395.18 | 400 | 380 | -$70.8M | +$3.1M bull / -$107k bear | out (clean 30, ADX 21, RVol 2.3) |
| 11 | **AMD** | 481.98 | - | **-** | 26 | - | NEG -$92.2M | - | 500 | 440 | +$45.4M | +$796k bull / +$0 bear | out (clean 32, ADX 23, RVol 1.8) |
| 12 | **SMCI** | 30.18 | - | **-** | 25 | - | NEG -$383k | 31.55 | 33 | 30 | +$1.6M | - | out (clean 33, ADX 35, RVol 3.9) |
| 13 | **NVDA** | 202.20 | - | **-** | 24 | - | NEG -$55.6M | 203.26 | 210 | 200 | +$5.9M | +$811k bull / +$0 bear | out (clean 30, ADX 38, RVol 2.4) |
| 14 | **SHOP** | 150.37 | - | **-** | 24 | - | NEG -$5.6M | - | 160 | 150 | -$203k | +$0 bull / -$138k bear | out (clean 35, ADX 26, RVol 0.9) |
| 15 | **SPY** | 766.01 | - | **-** | 23 | - | NEG -$3.7B | 770.11 | 770 | 750 | -$66.6M | +$699k bull / +$0 bear | out (clean 31, ADX 40, RVol 1.7) |
| 16 | **ARM** | 193.49 | - | **-** | 23 | - | NEG -$6.5M | - | 200 | 200 | +$818k | - | out (clean 26, ADX 32, RVol 0.8) |
| 17 | **META** | 634.48 | - | **-** | 22 | - | POS +$203.9M | 619.83 | 650 | 625 | +$5.9M | +$27k bull / -$920k bear | out (clean 30, ADX 43, RVol 1.0) |
| 18 | **NFLX** | 66.39 | - | **-** | 21 | - | POS +$19.1M | 62.52 | 65 | 65 | -$2.3M | - | out (clean 31, ADX 70, RVol 1.6) |
| 19 | **MSTR** | 142.96 | - | **-** | 21 | - | POS +$121.0M | - | 135 | 150 | +$357k | +$341k bull / -$164k bear | out (clean 31, ADX 46, RVol 1.3) |
| 20 | **QQQ** | 693.07 | - | **-** | 20 | - | NEG -$4.9B | 719.29 | 700 | 680 | -$76.5M | +$15.5M bull / +$0 bear | out (clean 30, ADX 29, RVol 1.2) |
| 21 | **AVGO** | 324.40 | - | **-** | 17 | - | NEG -$101.7M | - | 340 | 320 | +$4.6M | - | out (clean 30, ADX 31, RVol 1.4) |
| 22 | **PLTR** | 174.02 | - | **-** | 17 | - | NEG -$45.0M | - | 180 | 170 | -$1.0M | +$141k bull / +$0 bear | out (clean 26, ADX 16, RVol 1.3) |
| 23 | **ORCL** | 125.98 | - | **-** | 17 | - | NEG -$31.2M | - | 130 | 125 | +$42k | +$34k bull / +$0 bear | out (clean 35, ADX 14, RVol 2.2) |
| 24 | **CRM** | 231.03 | - | **-** | 17 | - | NEG -$7.2M | 238.23 | 240 | 220 | -$244k | - | out (clean 31, ADX 57, RVol 0.9) |
| 25 | **HOOD** | 86.14 | - | **-** | 16 | - | POS +$842k | 85.98 | 90 | 90 | -$364k | +$39k bull / +$0 bear | out (clean 28, ADX 17, RVol 0.9) |
| 26 | **DELL** | 372.79 | - | **-** | 15 | - | NEG -$30.3M | - | 400 | 400 | +$1.2M | - | out (clean 32, ADX 36, RVol 2.3) |
| 27 | **IWM** | 282.21 | - | **-** | 14 | - | NEG -$622.5M | 284.55 | 285 | 270 | +$14.5M | - | out (clean 34, ADX 21, RVol 1.1) |

## Big prints this scan (144)
- **TSLA** PUT 385 2026-11-09 (5DTE): 473 @ 5.90 = **+$279k** SELL | vol 2,087 / OI 308
- **AMZN** CALL 275 2026-11-06 (2DTE): 2,182 @ 1.26 = **+$275k** BUY | vol 15,518 / OI 8,639
- **SPY** PUT 768 2026-11-05 (1DTE): 757 @ 3.12 = **+$236k** SELL | vol 18,475 / OI 0
- **MU** PUT 840 2026-11-04 (0DTE): 100 @ 21.00 = **+$210k** SELL | vol 4,444 / OI 1,021
- **QQQ** PUT 695 2026-11-04 (0DTE): 990 @ 1.88 = **+$186k** SELL | vol 76,690 / OI 1,605
- **TSLA** PUT 382.5 2026-11-06 (2DTE): 483 @ 3.75 = **+$181k** SELL | vol 3,103 / OI 1,248
- **MU** PUT 810 2026-11-04 (0DTE): 299 @ 5.70 = **+$170k** SELL | vol 11,398 / OI 952
- **TSLA** PUT 385 2026-11-09 (5DTE): 234 @ 6.55 = **+$153k** SELL | vol 2,087 / OI 308
- **SPY** CALL 765 2026-11-11 (7DTE): 200 @ 7.45 = **+$149k** BUY | vol 786 / OI 1,539
- **TSLA** CALL 380 2026-11-06 (2DTE): 114 @ 12.85 = **+$146k** BUY | vol 5,403 / OI 2,084
- **QQQ** CALL 695 2026-11-04 (0DTE): 497 @ 2.82 = **+$140k** BUY | vol 44,070 / OI 2,465
- **MU** CALL 830 2026-11-04 (0DTE): 300 @ 4.50 = **+$135k** BUY | vol 10,155 / OI 291
- **MU** CALL 830 2026-11-04 (0DTE): 300 @ 4.50 = **+$135k** BUY | vol 10,155 / OI 291
- **TSLA** PUT 385 2026-11-09 (5DTE): 226 @ 5.93 = **+$134k** SELL | vol 2,087 / OI 308
- **MSFT** CALL 525 2026-11-06 (2DTE): 42 @ 31.07 = **+$130k** BUY | vol 602 / OI 3,666

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 782 2026-11-06 (2DTE): 2,977 traded vs OI 2,812
- **SPY** PUT 768 2026-11-09 (5DTE): 504 traded vs OI 0
- **SPY** CALL 784 2026-11-10 (6DTE): 552 traded vs OI 0
- **SPY** CALL 782 2026-11-10 (6DTE): 523 traded vs OI 0
- **SPY** PUT 756 2026-11-06 (2DTE): 2,130 traded vs OI 1,867
- **SPY** PUT 770 2026-11-05 (1DTE): 1,734 traded vs OI 1,690
- **SPY** CALL 778 2026-11-06 (2DTE): 2,223 traded vs OI 2,193
- **SPY** PUT 775 2026-11-04 (0DTE): 599 traded vs OI 1
- **SPY** CALL 770 2026-11-13 (9DTE): 3,985 traded vs OI 3,984
- **SPY** CALL 768 2026-11-11 (7DTE): 502 traded vs OI 0
- **QQQ** CALL 721 2026-11-04 (0DTE): 1,084 traded vs OI 1,072
- **QQQ** CALL 716 2026-11-05 (1DTE): 521 traded vs OI 0
- **QQQ** CALL 715 2026-11-09 (5DTE): 2,270 traded vs OI 2,261
- **QQQ** CALL 720 2026-11-13 (9DTE): 2,062 traded vs OI 1,993
- **IWM** PUT 281 2026-11-10 (6DTE): 984 traded vs OI 482

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
