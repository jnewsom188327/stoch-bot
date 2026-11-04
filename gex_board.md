# GEX + FLOW SCAN - Wed Nov 04, 03:05 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 13:05 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 352.5P | 0.58 | 0.89 | +76% (29m) | **+53%** (done) | +57% | 352.38 hit |
| 12:50 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.40 | 0.76 | +100% (55m) | **+90%** (done) | +109% | 267.48 |
| 11:38 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/04 686P | 0.80 | 0.15 | -1% (0m) | **-81%** (done) | +26% | 689.6 |
| 11:21 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/04 685P | 0.67 | 0.12 | +66% (7m) | **-82%** (done) | +25% | 690.3 hit |
| 10:20 | **SMCI** | **CALLS** | FLOW SURGE | 11/06 33C | 0.65 | 0.13 | -3% (1m) | **-80%** (done) | +39% | 32.81 |
| 10:20 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 284C | 0.49 | 0.17 | +2% (22m) | **-65%** (done) | +131% | 284.74 |
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 1.54 | +169% (60m) | **+126%** (done) | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.56 | +168% (52m) | **+160%** (done) | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.06 | +2% (1m) | **-89%** (done) | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.10 | -3% (1m) | **-84%** (done) | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:05:08 ET, last candle SPY 15:04, QQQ 15:04 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 14:01 | QQQ | 1m WHIPSAW | R1 | PUTS | TURNING away | no contract: 82 puts 0-1DTE > 8 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
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
| 1 | **SMH** | 502.57 | FLOW SURGE | **CALLS** | 36 | none: 158 calls 0-7DTE > 9 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -13% at the target (needs +20%) (61 contracts' greeks worked out here) | NEG -$595.7M | - | 532.5 | 500 | +$23.0M | +$25k bull / +$0 bear | out (clean 32, ADX 20, RVol 0.5) |
| 2 | **UBER** | 70.10 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 31 | none: 14 puts 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +20% at the target (needs +20%) | POS +$8.0M | 68.53 | 70 | 65 | -$639k | - | out (clean 31, ADX 24, RVol 1.2) |
| 3 | **AAPL** | 352.29 | - | **-** | 23 | - | POS +$819.6M | 343.24 | 350 | 350 | -$74.7M | +$261k bull / +$0 bear | out (clean 31, ADX 13, RVol 0.8) |
| 4 | **MU** | 798.38 | - | **-** | 22 | - | NEG -$371.4M | - | 850 | 800 | +$122.3M | +$1.0M bull / -$63k bear | out (clean 31, ADX 24, RVol 0.9) |
| 5 | **GOOGL** | 291.70 | - | **-** | 21 | - | POS +$97.7M | 285.28 | 290 | 290 | -$26.3M | +$0 bull / -$70k bear | out (clean 36, ADX 10, RVol 0.3) |
| 6 | **MSTR** | 143.37 | - | **-** | 21 | - | POS +$132.7M | - | 135 | 150 | -$9.4M | +$130k bull / +$0 bear | out (clean 31, ADX 26, RVol 0.4) |
| 7 | **ARM** | 191.21 | - | **-** | 21 | - | NEG -$7.3M | - | 200 | 200 | +$1.1M | +$0 bull / -$28k bear | out (clean 26, ADX 30, RVol 0.4) |
| 8 | **MSFT** | 558.25 | - | **-** | 20 | - | POS +$998.2M | - | 550 | 535 | -$17.7M | +$0 bull / -$767k bear | out (clean 29, ADX 21, RVol 1.2) |
| 9 | **TSLA** | 387.29 | - | **-** | 19 | - | NEG -$107.1M | 393.28 | 400 | 380 | -$76.2M | +$457k bull / -$145k bear | out (clean 31, ADX 16, RVol 0.5) |
| 10 | **AMD** | 482.03 | - | **-** | 19 | - | NEG -$95.2M | - | 500 | 440 | +$50.0M | +$164k bull / -$606k bear | out (clean 32, ADX 15, RVol 0.6) |
| 11 | **META** | 629.24 | - | **-** | 18 | - | POS +$159.9M | 620.31 | 650 | 625 | +$10.9M | +$144k bull / -$193k bear | out (clean 32, ADX 29, RVol 0.3) |
| 12 | **AVGO** | 326.07 | - | **-** | 18 | - | NEG -$108.4M | - | 340 | 320 | +$5.9M | +$89k bull / +$0 bear | out (clean 30, ADX 19, RVol 0.5) |
| 13 | **SMCI** | 29.62 | - | **-** | 18 | - | NEG -$970k | - | 32 | 30 | +$2.1M | - | out (clean 34, ADX 28, RVol 1.0) |
| 14 | **NVDA** | 202.27 | - | **-** | 17 | - | NEG -$106.3M | 203.37 | 210 | 200 | +$10.8M | +$184k bull / +$0 bear | out (clean 30, ADX 17, RVol 1.0) |
| 15 | **AMZN** | 267.82 | - | **-** | 17 | - | POS +$562.8M | - | 270 | 250 | -$17.1M | +$123k bull / +$0 bear | out (clean 36, ADX 15, RVol 0.6) |
| 16 | **DELL** | 367.82 | - | **-** | 17 | - | NEG -$27.6M | - | 400 | 400 | +$921k | +$36k bull / +$0 bear | out (clean 33, ADX 23, RVol 0.8) |
| 17 | **SPY** | 767.38 | - | **-** | 16 | - | NEG -$3.6B | 769.45 | 770 | 767 | -$89.7M | +$6.3M bull / +$0 bear | out (clean 32, ADX 15, RVol 0.6) |
| 18 | **IWM** | 283.31 | - | **-** | 16 | - | NEG -$318.7M | 284.14 | 285 | 270 | +$9.5M | +$65k bull / +$0 bear | out (clean 34, ADX 14, RVol 0.3) |
| 19 | **QQQ** | 692.55 | - | **-** | 15 | - | NEG -$5.2B | 718.5 | 700 | 680 | -$79.3M | +$0 bull / -$144k bear | out (clean 32, ADX 16, RVol 0.5) |
| 20 | **HOOD** | 87.65 | - | **-** | 15 | - | POS +$2.7M | 84.82 | 90 | 90 | -$721k | +$27k bull / +$0 bear | out (clean 29, ADX 13, RVol 0.6) |
| 21 | **NFLX** | 66.59 | - | **-** | 13 | - | POS +$18.1M | 62.83 | 65 | 65 | -$2.1M | - | out (clean 32, ADX 27, RVol 1.1) |
| 22 | **ORCL** | 124.89 | - | **-** | 13 | - | NEG -$34.7M | - | 130 | 125 | +$3.6M | - | out (clean 33, ADX 25, RVol 1.6) |
| 23 | **SHOP** | 152.36 | - | **-** | 11 | - | NEG -$5.3M | - | 160 | 150 | -$384k | - | out (clean 32, ADX 15, RVol 0.5) |
| 24 | **COIN** | 151.84 | - | **-** | 9 | - | POS +$30.1M | - | 149 | 150 | -$1.2M | - | out (clean 31, ADX 12, RVol 0.3) |
| 25 | **CRM** | 227.67 | - | **-** | 7 | - | NEG -$10.7M | 237.7 | 240 | 220 | -$189k | - | out (clean 34, ADX 15, RVol 0.4) |
| 26 | **BABA** | 106.15 | - | **-** | 7 | - | POS +$17.0M | - | 110 | 110 | -$205k | - | out (clean 36, ADX 22, RVol 0.6) |
| 27 | **PLTR** | 171.24 | - | **-** | 3 | - | NEG -$51.1M | - | 165 | 170 | -$990k | - | out (clean 26, ADX 10, RVol 0.4) |

## Big prints this scan (48)
- **AMD** PUT 487.5 2026-11-06 (2DTE): 100 @ 16.40 = **+$164k** SELL | vol 836 / OI 331
- **AMD** PUT 485 2026-11-06 (2DTE): 100 @ 15.05 = **+$150k** MID | vol 2,327 / OI 426
- **MU** PUT 795 2026-11-04 (0DTE): 949 @ 1.55 = **+$147k** SELL | vol 33,100 / OI 1,083
- **QQQ** PUT 692 2026-11-05 (1DTE): 400 @ 3.60 = **+$144k** BUY | vol 15,735 / OI 0
- **AMD** PUT 475 2026-11-06 (2DTE): 100 @ 10.98 = **+$110k** BUY | vol 4,596 / OI 892
- **AMD** PUT 472.5 2026-11-06 (2DTE): 100 @ 9.94 = **+$99k** BUY | vol 525 / OI 183
- **TSLA** CALL 390 2026-11-11 (7DTE): 95 @ 9.90 = **+$94k** BUY | vol 3,978 / OI 87
- **AAPL** CALL 347.5 2026-11-04 (0DTE): 150 @ 4.95 = **+$74k** BUY | vol 28,819 / OI 4,478
- **MSTR** CALL 144 2026-11-06 (2DTE): 190 @ 3.65 = **+$69k** BUY | vol 3,312 / OI 7,237
- **IWM** PUT 290 2026-11-06 (2DTE): 100 @ 6.50 = **+$65k** SELL | vol 344 / OI 59
- **META** CALL 627.5 2026-11-04 (0DTE): 235 @ 2.73 = **+$64k** SELL | vol 5,004 / OI 252
- **AMD** PUT 497.5 2026-11-09 (5DTE): 25 @ 25.35 = **+$63k** BUY | vol 150 / OI 38
- **AMD** PUT 487.5 2026-11-04 (0DTE): 100 @ 6.27 = **+$63k** MID | vol 5,626 / OI 149
- **MU** PUT 800 2026-11-09 (5DTE): 25 @ 22.51 = **+$56k** SELL | vol 1,499 / OI 321
- **NVDA** PUT 207.5 2026-11-06 (2DTE): 100 @ 5.39 = **+$54k** SELL | vol 4,645 / OI 3,670

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 791 2026-11-05 (1DTE): 514 traded vs OI 0
- **SPY** PUT 752 2026-12-04 (30DTE): 507 traded vs OI 296
- **SPY** PUT 770 2026-12-04 (30DTE): 513 traded vs OI 260
- **QQQ** PUT 699 2026-11-06 (2DTE): 2,273 traded vs OI 2,268
- **QQQ** CALL 710 2026-11-09 (5DTE): 1,381 traded vs OI 1,379
- **QQQ** PUT 660 2026-12-04 (30DTE): 793 traded vs OI 741
- **AAPL** CALL 367.5 2026-11-13 (9DTE): 1,025 traded vs OI 874
- **AMD** PUT 462.5 2026-11-06 (2DTE): 507 traded vs OI 87
- **AMD** CALL 515 2026-11-06 (2DTE): 1,800 traded vs OI 1,797
- **AMD** PUT 477.5 2026-11-06 (2DTE): 512 traded vs OI 385
- **MSFT** CALL 582.5 2026-11-06 (2DTE): 570 traded vs OI 78
- **SMCI** PUT 30.5 2026-11-06 (2DTE): 706 traded vs OI 705
- **MSTR** PUT 137 2026-11-06 (2DTE): 501 traded vs OI 341
- **HOOD** PUT 94 2026-11-20 (16DTE): 507 traded vs OI 0
- **UBER** PUT 71 2026-11-13 (9DTE): 509 traded vs OI 385

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
