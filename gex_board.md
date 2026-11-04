# GEX + FLOW SCAN - Wed Nov 04, 12:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:38 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/04 686P | 0.80 | 0.15 | -1% (0m) | **-81%** (done) | +26% | 689.6 |
| 11:21 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/04 685P | 0.67 | 0.12 | +66% (7m) | **-82%** (done) | +25% | 690.3 hit |
| 10:20 | **SMCI** | **CALLS** | FLOW SURGE | 11/06 33C | 0.65 | 0.13 | -3% (1m) | **-80%** (done) | +39% | 32.81 |
| 10:20 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 284C | 0.49 | 0.17 | +2% (22m) | **-65%** (done) | +131% | 284.74 |
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 1.54 | +169% (60m) | **+126%** (done) | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.56 | +168% (52m) | **+160%** (done) | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.06 | +2% (1m) | **-89%** (done) | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.10 | -3% (1m) | **-84%** (done) | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:40:08 ET, last candle SPY 12:39, QQQ 12:39 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:37 | QQQ | 1m FAILED POP | R3 | PUTS | TURNING away | **FIRE** QQQ261104P00686000 |
| 11:20 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** QQQ261104P00685000 |

## Flow surges NOT fired - price disagreed (36 today, last 5)
- 11:50 SMCI CALLS: under EMA 20 - flow says one way, price says the other
- 11:45 SMCI CALLS: under EMA 20 - flow says one way, price says the other
- 11:40 SMCI CALLS: under EMA 20 - flow says one way, price says the other
- 11:35 SMCI CALLS: price -0.19 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:30 SMCI CALLS: price -0.20 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 352.73 | - | **-** | 30 | - | POS +$1.0B | 341.63 | 355 | 350 | -$78.1M | +$4.0M bull / -$33k bear | out (clean 32, ADX 45, RVol 0.7) |
| 2 | **BABA** | 106.95 | TREND (flow not with it) | **CALLS** | 29 | none: 21 calls 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +8% at the target (needs +20%) | POS +$16.5M | - | 110 | 110 | -$845k | - | LONG (clean 36, ADX 36, RVol 0.5) |
| 3 | **SMH** | 506.76 | - | **-** | 27 | - | NEG -$529.0M | - | 532.5 | 500 | +$20.5M | +$31k bull / -$504k bear | out (clean 32, ADX 20, RVol 0.9) |
| 4 | **UBER** | 70.84 | - | **-** | 27 | - | POS +$9.8M | 68.73 | 70 | 70 | -$1.1M | +$118k bull / +$0 bear | out (clean 30, ADX 35, RVol 1.1) |
| 5 | **MSFT** | 554.63 | - | **-** | 25 | - | POS +$1.0B | - | 550 | 535 | -$16.8M | +$310k bull / -$126k bear | out (clean 29, ADX 53, RVol 1.4) |
| 6 | **NFLX** | 65.98 | - | **-** | 25 | - | POS +$21.2M | 62.48 | 65 | 65 | -$2.0M | +$31k bull / +$0 bear | out (clean 31, ADX 38, RVol 0.7) |
| 7 | **AMZN** | 268.79 | - | **-** | 23 | - | POS +$561.2M | - | 270 | 250 | -$20.5M | +$0 bull / -$284k bear | out (clean 35, ADX 33, RVol 1.0) |
| 8 | **TSLA** | 388.69 | - | **-** | 21 | - | NEG -$108.1M | 396.95 | 400 | 380 | -$80.0M | +$0 bull / -$1.4M bear | out (clean 30, ADX 17, RVol 0.5) |
| 9 | **COIN** | 151.56 | - | **-** | 21 | - | POS +$29.3M | - | 148 | 150 | -$1.3M | +$0 bull / -$28k bear | out (clean 31, ADX 16, RVol 0.2) |
| 10 | **SMCI** | 30.09 | - | **-** | 21 | - | NEG -$601k | - | 33 | 30 | +$1.9M | - | out (clean 34, ADX 37, RVol 1.1) |
| 11 | **MU** | 807.71 | - | **-** | 21 | - | NEG -$345.5M | - | 850 | 800 | +$95.3M | +$768k bull / -$1.9M bear | out (clean 32, ADX 25, RVol 0.5) |
| 12 | **IWM** | 284.23 | - | **-** | 20 | - | NEG -$139.0M | 284.59 | 285 | 270 | +$8.7M | +$0 bull / -$924k bear | out (clean 35, ADX 19, RVol 1.7) |
| 13 | **SPY** | 767.97 | - | **-** | 19 | - | NEG -$2.2B | 769.93 | 770 | 750 | -$113.5M | +$224k bull / -$554k bear | out (clean 32, ADX 26, RVol 0.6) |
| 14 | **AMD** | 486.23 | - | **-** | 18 | - | NEG -$88.4M | - | 500 | 500 | +$42.1M | +$450k bull / -$292k bear | out (clean 32, ADX 10, RVol 0.6) |
| 15 | **NVDA** | 202.89 | - | **-** | 17 | - | NEG -$51.1M | 203.63 | 210 | 200 | -$5k | +$279k bull / -$163k bear | out (clean 30, ADX 26, RVol 1.0) |
| 16 | **AVGO** | 327.46 | - | **-** | 17 | - | NEG -$95.2M | - | 340 | 330 | +$1.9M | +$26k bull / +$0 bear | out (clean 30, ADX 19, RVol 0.9) |
| 17 | **PLTR** | 169.89 | - | **-** | 17 | - | NEG -$51.5M | - | 165 | 170 | -$1.0M | +$240k bull / +$0 bear | out (clean 26, ADX 25, RVol 0.6) |
| 18 | **MSTR** | 144.36 | - | **-** | 17 | - | POS +$125.0M | - | 135 | 150 | +$801k | +$0 bull / -$195k bear | out (clean 31, ADX 32, RVol 0.3) |
| 19 | **QQQ** | 695.28 | - | **-** | 16 | - | NEG -$4.6B | 718.52 | 700 | 680 | -$141.4M | +$0 bull / -$735k bear | out (clean 32, ADX 13, RVol 0.4) |
| 20 | **META** | 639.07 | - | **-** | 16 | - | POS +$254.7M | 620.26 | 650 | 625 | -$1.5M | +$127k bull / -$820k bear | out (clean 30, ADX 24, RVol 0.9) |
| 21 | **HOOD** | 87.73 | - | **-** | 16 | - | POS +$2.5M | 85.1 | 90 | 90 | -$960k | +$0 bull / -$60k bear | out (clean 28, ADX 17, RVol 0.5) |
| 22 | **GOOGL** | 291.71 | - | **-** | 15 | - | POS +$105.2M | 282.6 | 290 | 290 | -$27.1M | - | out (clean 36, ADX 22, RVol 0.4) |
| 23 | **SHOP** | 151.23 | - | **-** | 13 | - | NEG -$5.9M | - | 160 | 150 | -$348k | - | out (clean 34, ADX 24, RVol 0.4) |
| 24 | **CRM** | 225.54 | - | **-** | 10 | - | NEG -$12.9M | - | 240 | 220 | -$114k | - | out (clean 33, ADX 35, RVol 0.7) |
| 25 | **ORCL** | 126.39 | - | **-** | 9 | - | NEG -$29.9M | - | 130 | 125 | +$2.2M | - | out (clean 34, ADX 11, RVol 1.2) |
| 26 | **DELL** | 373.15 | - | **-** | 8 | - | NEG -$30.1M | - | 400 | 400 | +$1.2M | - | out (clean 33, ADX 25, RVol 0.9) |
| 27 | **ARM** | 196.08 | - | **-** | 7 | - | NEG -$7.1M | - | 212.5 | 200 | +$265k | - | out (clean 26, ADX 23, RVol 0.5) |

## Big prints this scan (91)
- **META** CALL 642.5 2026-11-06 (2DTE): 400 @ 7.90 = **+$316k** MID | vol 1,312 / OI 665
- **TSLA** PUT 395 2026-11-04 (0DTE): 240 @ 7.45 = **+$179k** BUY | vol 2,457 / OI 2,219
- **AAPL** PUT 360 2026-11-06 (2DTE): 218 @ 7.45 = **+$162k** SELL | vol 1,234 / OI 3,175
- **SPY** PUT 769 2026-11-10 (6DTE): 214 @ 5.29 = **+$113k** SELL | vol 734 / OI 0
- **MU** PUT 805 2026-11-06 (2DTE): 55 @ 20.40 = **+$112k** BUY | vol 2,216 / OI 615
- **SPY** CALL 768 2026-11-04 (0DTE): 856 @ 1.30 = **+$111k** BUY | vol 356,284 / OI 1,095
- **MU** PUT 825 2026-11-04 (0DTE): 55 @ 20.15 = **+$111k** BUY | vol 7,963 / OI 526
- **QQQ** PUT 694 2026-11-06 (2DTE): 198 @ 5.48 = **+$109k** BUY | vol 2,642 / OI 1,129
- **META** CALL 640 2026-11-04 (0DTE): 484 @ 2.15 = **+$104k** SELL | vol 38,564 / OI 670
- **META** CALL 640 2026-11-04 (0DTE): 500 @ 2.08 = **+$104k** SELL | vol 38,564 / OI 670
- **AAPL** PUT 370 2026-11-06 (2DTE): 60 @ 16.20 = **+$97k** SELL | vol 167 / OI 126
- **MU** CALL 820 2026-11-04 (0DTE): 378 @ 2.22 = **+$84k** BUY | vol 23,586 / OI 31
- **AMD** PUT 497.5 2026-11-06 (2DTE): 41 @ 19.50 = **+$80k** SELL | vol 410 / OI 177
- **META** CALL 640 2026-11-04 (0DTE): 393 @ 2.02 = **+$79k** SELL | vol 38,564 / OI 670
- **TSLA** CALL 382.5 2026-11-06 (2DTE): 78 @ 10.00 = **+$78k** SELL | vol 5,578 / OI 712

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 769 2026-11-09 (5DTE): 500 traded vs OI 0
- **SPY** PUT 728 2026-11-06 (2DTE): 4,249 traded vs OI 3,644
- **SPY** PUT 724 2026-11-05 (1DTE): 500 traded vs OI 0
- **SPY** PUT 769 2026-11-10 (6DTE): 734 traded vs OI 0
- **SPY** PUT 765 2026-11-12 (8DTE): 501 traded vs OI 497
- **SPY** PUT 745 2026-11-30 (26DTE): 3,064 traded vs OI 3,053
- **SPY** CALL 787 2026-11-17 (13DTE): 1,761 traded vs OI 0
- **SPY** CALL 774 2026-11-17 (13DTE): 1,628 traded vs OI 0
- **SPY** PUT 740 2026-12-04 (30DTE): 2,839 traded vs OI 650
- **SPY** PUT 720 2026-12-04 (30DTE): 3,185 traded vs OI 907
- **QQQ** PUT 645 2026-11-05 (1DTE): 631 traded vs OI 538
- **QQQ** CALL 697 2026-11-20 (16DTE): 503 traded vs OI 414
- **IWM** CALL 282.5 2026-11-13 (9DTE): 634 traded vs OI 631
- **SMH** PUT 502.5 2026-11-06 (2DTE): 512 traded vs OI 275
- **NVDA** PUT 222.5 2026-11-09 (5DTE): 526 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
