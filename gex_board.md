# GEX + FLOW SCAN - Wed Nov 04, 11:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (7)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:21 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/04 685P | 0.67 | 0.88 | +66% (7m) | **+31%** | +25% | 690.3 hit |
| 10:20 | **SMCI** | **CALLS** | FLOW SURGE | 11/06 33C | 0.65 | 0.13 | -3% (1m) | **-80%** (done) | +39% | 32.81 |
| 10:20 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 284C | 0.49 | 0.17 | +2% (22m) | **-65%** (done) | +131% | 284.74 |
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 1.54 | +169% (60m) | **+126%** (done) | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.56 | +168% (52m) | **+160%** (done) | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.06 | +2% (1m) | **-89%** (done) | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.10 | -3% (1m) | **-84%** (done) | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:30:08 ET, last candle SPY 11:29, QQQ 11:29 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:20 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** QQQ261104P00685000 |

## Flow surges NOT fired - price disagreed (32 today, last 5)
- 11:30 SMCI CALLS: price -0.20 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:25 SMCI CALLS: price -0.14 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:20 SMCI CALLS: under EMA 20 - flow says one way, price says the other
- 11:15 SMCI CALLS: price -0.11 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:50 SMCI CALLS: price -1.23 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMCI** | 29.88 | FLOW SURGE | **CALLS** | 64 | 11/06 30.5C @ 0.73 (delta 0.42) = est +53% at 30.8 | NEG -$904k | - | 32 | 30 | +$1.9M | +$64k bull / +$0 bear | SHORT (clean 33, ADX 46, RVol 2.7) |
| 2 | **GOOGL** | 289.63 | PINNED between the walls (positive gamma) - chop | **-** | 43 | - | POS +$88.5M | 282.45 | 290 | 290 | -$26.1M | +$363k bull / +$0 bear | out (clean 35, ADX 42, RVol 0.7) |
| 3 | **META** | 625.83 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 40 | none: 200 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (86 contracts' greeks worked out here) | POS +$97.2M | 619.8 | 650 | 625 | +$8.5M | +$643k bull / +$0 bear | out (clean 30, ADX 32, RVol 0.9) |
| 4 | **AAPL** | 351.25 | - | **-** | 33 | - | POS +$837.3M | 341.45 | 350 | 350 | -$76.1M | +$774k bull / -$34k bear | out (clean 32, ADX 56, RVol 1.5) |
| 5 | **ARM** | 193.02 | - | **-** | 33 | - | NEG -$6.8M | - | 200 | 200 | +$846k | +$0 bull / -$46k bear | out (clean 26, ADX 39, RVol 0.9) |
| 6 | **NFLX** | 66.04 | - | **-** | 28 | - | POS +$19.1M | 62.53 | 65 | 65 | -$2.1M | +$34k bull / +$0 bear | out (clean 31, ADX 65, RVol 0.9) |
| 7 | **SMH** | 502.76 | - | **-** | 27 | - | NEG -$521.8M | - | 532.5 | 500 | +$4.0M | +$0 bull / -$357k bear | out (clean 32, ADX 39, RVol 1.3) |
| 8 | **DELL** | 368.31 | - | **-** | 27 | - | NEG -$27.3M | - | 400 | 400 | +$2.2M | +$544k bull / +$0 bear | out (clean 33, ADX 42, RVol 3.1) |
| 9 | **MU** | 803.39 | - | **-** | 27 | - | NEG -$329.6M | - | 850 | 800 | +$97.9M | +$118k bull / -$13.3M bear | out (clean 31, ADX 37, RVol 1.5) |
| 10 | **UBER** | 71.66 | - | **-** | 26 | - | POS +$12.1M | 68.1 | 70 | 70 | -$1.4M | - | out (clean 31, ADX 62, RVol 2.3) |
| 11 | **AMZN** | 265.35 | - | **-** | 25 | - | POS +$540.2M | - | 270 | 250 | -$17.5M | +$479k bull / +$0 bear | out (clean 35, ADX 45, RVol 1.3) |
| 12 | **MSFT** | 552.60 | - | **-** | 25 | - | POS +$995.9M | - | 550 | 535 | -$14.5M | +$423k bull / -$158k bear | out (clean 28, ADX 64, RVol 1.2) |
| 13 | **TSLA** | 382.50 | - | **-** | 24 | - | NEG -$118.1M | 390.22 | 400 | 380 | -$59.4M | +$4.4M bull / +$0 bear | out (clean 30, ADX 24, RVol 1.7) |
| 14 | **SHOP** | 151.34 | - | **-** | 24 | - | NEG -$5.0M | - | 160 | 150 | -$320k | +$0 bull / -$29k bear | out (clean 34, ADX 30, RVol 0.4) |
| 15 | **AVGO** | 325.75 | - | **-** | 23 | - | NEG -$96.0M | - | 340 | 320 | +$2.8M | +$0 bull / -$355k bear | out (clean 30, ADX 35, RVol 1.5) |
| 16 | **ORCL** | 125.76 | - | **-** | 23 | - | NEG -$31.0M | - | 130 | 125 | +$2.3M | +$1.2M bull / +$0 bear | out (clean 35, ADX 15, RVol 2.5) |
| 17 | **IWM** | 281.79 | - | **-** | 22 | - | NEG -$856.8M | 284.5 | 285 | 270 | +$14.7M | +$0 bull / -$159k bear | out (clean 34, ADX 17, RVol 1.3) |
| 18 | **NVDA** | 201.85 | - | **-** | 21 | - | NEG -$86.9M | 203.34 | 210 | 200 | +$3.4M | +$400k bull / -$460k bear | out (clean 30, ADX 39, RVol 1.8) |
| 19 | **AMD** | 483.25 | - | **-** | 21 | - | NEG -$86.5M | - | 500 | 440 | +$38.9M | +$416k bull / -$2.2M bear | out (clean 32, ADX 20, RVol 1.0) |
| 20 | **BABA** | 106.46 | - | **-** | 21 | - | POS +$16.2M | - | 110 | 110 | -$813k | - | out (clean 36, ADX 58, RVol 2.4) |
| 21 | **SPY** | 764.19 | - | **-** | 20 | - | NEG -$5.1B | 769.83 | 770 | 750 | -$49.9M | +$3.5M bull / -$1.1M bear | out (clean 32, ADX 31, RVol 1.2) |
| 22 | **MSTR** | 143.69 | - | **-** | 20 | - | POS +$120.9M | - | 135 | 150 | +$376k | +$200k bull / -$145k bear | out (clean 31, ADX 43, RVol 0.9) |
| 23 | **PLTR** | 169.83 | - | **-** | 19 | - | NEG -$50.2M | - | 165 | 170 | -$1.8M | +$554k bull / -$289k bear | out (clean 26, ADX 18, RVol 1.7) |
| 24 | **QQQ** | 690.57 | - | **-** | 17 | - | NEG -$5.3B | 719.3 | 700 | 680 | -$53.5M | +$4.9M bull / -$5.4M bear | out (clean 31, ADX 23, RVol 0.9) |
| 25 | **HOOD** | 86.78 | - | **-** | 16 | - | POS +$1.9M | 85.01 | 90 | 90 | -$1.0M | +$28k bull / -$158k bear | out (clean 28, ADX 14, RVol 0.7) |
| 26 | **CRM** | 227.33 | - | **-** | 14 | - | NEG -$9.4M | 239.04 | 240 | 220 | -$197k | - | out (clean 31, ADX 42, RVol 0.6) |
| 27 | **COIN** | 151.45 | - | **-** | 13 | - | POS +$30.2M | - | 148 | 150 | -$1.3M | - | out (clean 31, ADX 16, RVol 0.6) |

## Big prints this scan (103)
- **QQQ** PUT 685 2026-11-09 (5DTE): 1,505 @ 4.68 = **+$704k** SELL | vol 3,861 / OI 1,057
- **SPY** PUT 770 2026-11-05 (1DTE): 956 @ 5.24 = **+$501k** SELL | vol 8,004 / OI 1,690
- **SPY** PUT 770 2026-11-05 (1DTE): 853 @ 5.32 = **+$454k** SELL | vol 8,004 / OI 1,690
- **QQQ** PUT 690 2026-11-04 (0DTE): 2,000 @ 1.34 = **+$268k** SELL | vol 126,397 / OI 3,140
- **MU** CALL 805 2026-11-09 (5DTE): 100 @ 25.00 = **+$250k** SELL | vol 516 / OI 59
- **QQQ** PUT 690 2026-11-06 (2DTE): 391 @ 5.36 = **+$210k** SELL | vol 8,675 / OI 13,671
- **SMH** PUT 502.5 2026-11-11 (7DTE): 150 @ 13.20 = **+$198k** MID | vol 221 / OI 0
- **AMD** PUT 485 2026-11-06 (2DTE): 131 @ 14.88 = **+$195k** BUY | vol 1,161 / OI 426
- **SMH** PUT 510 2026-11-06 (2DTE): 150 @ 12.90 = **+$194k** MID | vol 811 / OI 1,304
- **QQQ** CALL 692 2026-11-04 (0DTE): 486 @ 3.22 = **+$156k** BUY | vol 36,621 / OI 681
- **QQQ** CALL 687 2026-11-05 (1DTE): 140 @ 8.80 = **+$123k** BUY | vol 652 / OI 0
- **AAPL** CALL 350 2026-11-04 (0DTE): 340 @ 3.40 = **+$116k** BUY | vol 58,560 / OI 7,478
- **MU** PUT 810 2026-11-04 (0DTE): 100 @ 11.43 = **+$114k** BUY | vol 14,761 / OI 952
- **MU** CALL 805 2026-11-09 (5DTE): 46 @ 23.94 = **+$110k** SELL | vol 516 / OI 59
- **MU** CALL 805 2026-11-09 (5DTE): 46 @ 23.94 = **+$110k** SELL | vol 516 / OI 59

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 743 2026-11-06 (2DTE): 1,368 traded vs OI 1,363
- **SPY** PUT 748 2026-11-06 (2DTE): 1,617 traded vs OI 1,616
- **SPY** PUT 734 2026-11-04 (0DTE): 2,377 traded vs OI 1,140
- **QQQ** PUT 693 2026-11-09 (5DTE): 603 traded vs OI 0
- **IWM** CALL 283 2026-11-06 (2DTE): 1,632 traded vs OI 1,561
- **IWM** CALL 283 2026-11-13 (9DTE): 3,353 traded vs OI 3,092
- **SMH** CALL 520 2026-11-06 (2DTE): 1,629 traded vs OI 1,301
- **SMH** CALL 527.5 2026-11-06 (2DTE): 626 traded vs OI 463
- **SMH** CALL 535 2026-11-06 (2DTE): 653 traded vs OI 223
- **TSLA** CALL 377.5 2026-11-13 (9DTE): 506 traded vs OI 5
- **MSFT** CALL 605 2026-11-20 (16DTE): 910 traded vs OI 0
- **GOOGL** PUT 295 2026-11-06 (2DTE): 885 traded vs OI 846
- **PLTR** PUT 175 2026-11-06 (2DTE): 4,602 traded vs OI 4,401
- **COIN** CALL 157.5 2026-11-06 (2DTE): 800 traded vs OI 792
- **DELL** PUT 360 2026-11-06 (2DTE): 527 traded vs OI 497

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
