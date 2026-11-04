# GEX + FLOW SCAN - Wed Nov 04, 12:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (9)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:50 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.40 | 0.38 | -5% (0m) | **-5%** | +109% | 267.48 |
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
Last 1m check 12:50:08 ET, last candle SPY 12:49, QQQ 12:49 | no errors
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
| 1 | **AMZN** | 269.53 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 48 | 11/04 267.5P @ 0.40 (delta 0.23) = est +109% at 267.48 | POS +$554.9M | - | 270 | 250 | -$21.9M | +$0 bull / -$215k bear | LONG (clean 35, ADX 35, RVol 1.2) |
| 2 | **SMH** | 507.79 | FLOW SURGE | **CALLS** | 39 | 11/04 512.5C @ 0.75 (delta 0.21) = est +560% at 517.5 | NEG -$544.9M | - | 532.5 | 500 | +$20.8M | +$57k bull / +$0 bear | out (clean 32, ADX 18, RVol 1.0) |
| 3 | **BABA** | 107.10 | TREND (flow not with it) | **CALLS** | 30 | none: 21 calls 0-7DTE > 3 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +13% at the target (needs +20%) | POS +$16.3M | - | 110 | 110 | -$818k | - | LONG (clean 36, ADX 33, RVol 0.7) |
| 4 | **AAPL** | 353.91 | - | **-** | 29 | - | POS +$1.1B | 342.75 | 355 | 350 | -$79.9M | +$615k bull / -$564k bear | out (clean 32, ADX 43, RVol 0.6) |
| 5 | **MSFT** | 555.59 | - | **-** | 26 | - | POS +$1.0B | - | 550 | 535 | -$17.4M | +$166k bull / -$313k bear | out (clean 29, ADX 49, RVol 1.5) |
| 6 | **TSLA** | 389.87 | - | **-** | 21 | - | NEG -$92.6M | 396.52 | 400 | 380 | -$80.6M | +$0 bull / -$1.8M bear | out (clean 30, ADX 18, RVol 0.5) |
| 7 | **MU** | 810.36 | - | **-** | 21 | - | NEG -$369.0M | - | 850 | 800 | +$101.2M | +$1.6M bull / -$679k bear | out (clean 32, ADX 23, RVol 0.5) |
| 8 | **SMCI** | 30.20 | - | **-** | 20 | - | NEG -$693k | - | 33 | 30 | +$1.9M | - | out (clean 34, ADX 34, RVol 1.2) |
| 9 | **SPY** | 768.72 | - | **-** | 19 | - | NEG -$1.8B | 770.08 | 770 | 750 | -$121.9M | +$395k bull / -$1.5M bear | out (clean 32, ADX 26, RVol 0.6) |
| 10 | **AMD** | 487.06 | - | **-** | 18 | - | NEG -$89.4M | - | 500 | 500 | +$44.0M | +$1.0M bull / +$0 bear | out (clean 32, ADX 9, RVol 0.6) |
| 11 | **DELL** | 374.00 | - | **-** | 18 | - | NEG -$30.6M | - | 400 | 400 | +$1.4M | +$251k bull / +$0 bear | out (clean 33, ADX 23, RVol 1.0) |
| 12 | **NVDA** | 203.50 | - | **-** | 17 | - | NEG -$49.9M | 204.02 | 210 | 200 | +$185k | +$82k bull / -$160k bear | out (clean 30, ADX 24, RVol 1.1) |
| 13 | **META** | 640.92 | - | **-** | 17 | - | POS +$261.0M | 624.41 | 650 | 625 | -$1.7M | +$0 bull / -$735k bear | out (clean 30, ADX 26, RVol 0.9) |
| 14 | **AVGO** | 329.60 | - | **-** | 17 | - | NEG -$84.0M | - | 340 | 330 | +$2.1M | +$26k bull / +$0 bear | out (clean 30, ADX 17, RVol 0.9) |
| 15 | **QQQ** | 696.40 | - | **-** | 16 | - | NEG -$4.6B | 720.09 | 700 | 680 | -$144.0M | +$0 bull / -$520k bear | out (clean 32, ADX 13, RVol 0.5) |
| 16 | **PLTR** | 170.63 | - | **-** | 16 | - | NEG -$50.7M | - | 165 | 170 | -$1.1M | +$240k bull / +$0 bear | out (clean 26, ADX 24, RVol 0.6) |
| 17 | **HOOD** | 88.30 | - | **-** | 16 | - | POS +$3.0M | 84.64 | 90 | 90 | -$942k | +$0 bull / -$33k bear | out (clean 28, ADX 18, RVol 0.4) |
| 18 | **UBER** | 70.81 | - | **-** | 16 | - | POS +$10.3M | 68.47 | 70 | 65 | -$1.1M | - | out (clean 30, ADX 34, RVol 1.1) |
| 19 | **NFLX** | 66.19 | - | **-** | 15 | - | POS +$19.7M | 62.36 | 65 | 65 | -$2.0M | - | out (clean 31, ADX 36, RVol 0.8) |
| 20 | **GOOGL** | 292.31 | - | **-** | 14 | - | POS +$95.5M | 285.34 | 290 | 290 | -$27.1M | - | out (clean 36, ADX 21, RVol 0.4) |
| 21 | **SHOP** | 152.40 | - | **-** | 12 | - | NEG -$5.6M | - | 160 | 150 | -$353k | - | out (clean 34, ADX 24, RVol 0.3) |
| 22 | **COIN** | 152.61 | - | **-** | 11 | - | POS +$28.4M | - | 148 | 155 | -$1.3M | - | out (clean 31, ADX 17, RVol 0.2) |
| 23 | **IWM** | 284.04 | - | **-** | 10 | - | NEG -$198.4M | 284.54 | 285 | 270 | +$9.2M | - | out (clean 35, ADX 18, RVol 1.7) |
| 24 | **CRM** | 226.15 | - | **-** | 10 | - | NEG -$13.2M | - | 240 | 220 | -$123k | - | out (clean 33, ADX 32, RVol 0.6) |
| 25 | **ORCL** | 126.30 | - | **-** | 8 | - | NEG -$31.2M | - | 130 | 125 | +$2.3M | - | out (clean 34, ADX 9, RVol 1.2) |
| 26 | **MSTR** | 145.21 | - | **-** | 7 | - | POS +$124.1M | - | 135 | 150 | +$841k | - | out (clean 31, ADX 32, RVol 0.2) |
| 27 | **ARM** | 196.16 | - | **-** | 7 | - | NEG -$7.1M | - | 212.5 | 200 | +$287k | - | out (clean 26, ADX 21, RVol 0.5) |

## Big prints this scan (66)
- **QQQ** PUT 695 2026-11-06 (2DTE): 325 @ 5.71 = **+$186k** BUY | vol 7,706 / OI 8,477
- **SPY** CALL 776 2026-11-11 (7DTE): 716 @ 2.38 = **+$170k** BUY | vol 2,083 / OI 0
- **MU** PUT 785 2026-11-06 (2DTE): 150 @ 10.90 = **+$164k** MID | vol 921 / OI 700
- **SPY** CALL 772 2026-11-06 (2DTE): 716 @ 2.08 = **+$149k** SELL | vol 9,308 / OI 1,788
- **AAPL** PUT 345 2026-11-06 (2DTE): 1,000 @ 1.13 = **+$113k** BUY | vol 22,740 / OI 3,823
- **AMZN** CALL 275 2026-11-09 (5DTE): 700 @ 1.61 = **+$113k** SELL | vol 4,476 / OI 229
- **DELL** CALL 377.5 2026-11-06 (2DTE): 100 @ 10.40 = **+$104k** BUY | vol 296 / OI 5
- **QQQ** PUT 705 2026-11-05 (1DTE): 100 @ 10.25 = **+$102k** BUY | vol 982 / OI 819
- **MU** CALL 820 2026-11-06 (2DTE): 50 @ 15.62 = **+$78k** BUY | vol 3,084 / OI 116
- **MU** CALL 825 2026-11-09 (5DTE): 40 @ 18.75 = **+$75k** BUY | vol 488 / OI 54
- **AAPL** PUT 355 2026-11-06 (2DTE): 150 @ 4.70 = **+$70k** BUY | vol 4,316 / OI 2,094
- **MSFT** CALL 530 2026-11-06 (2DTE): 25 @ 25.88 = **+$65k** SELL | vol 1,717 / OI 5,699
- **MU** PUT 795 2026-11-04 (0DTE): 400 @ 1.60 = **+$64k** BUY | vol 18,725 / OI 1,083
- **TSLA** PUT 387.5 2026-11-06 (2DTE): 100 @ 6.30 = **+$63k** BUY | vol 4,422 / OI 2,978
- **TSLA** CALL 390 2026-11-06 (2DTE): 100 @ 6.00 = **+$60k** SELL | vol 16,638 / OI 2,560

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 776 2026-11-11 (7DTE): 2,083 traded vs OI 0
- **SPY** CALL 785 2026-11-11 (7DTE): 2,334 traded vs OI 1,445
- **SPY** CALL 777 2026-11-27 (23DTE): 2,147 traded vs OI 572
- **SPY** CALL 786 2026-11-27 (23DTE): 1,868 traded vs OI 455
- **QQQ** PUT 652 2026-11-06 (2DTE): 521 traded vs OI 0
- **QQQ** PUT 663 2026-11-05 (1DTE): 590 traded vs OI 0
- **IWM** CALL 293 2026-11-09 (5DTE): 765 traded vs OI 0
- **IWM** PUT 266 2026-11-09 (5DTE): 1,547 traded vs OI 749
- **SMH** CALL 525 2026-11-06 (2DTE): 754 traded vs OI 749
- **NVDA** CALL 207.5 2026-11-16 (12DTE): 576 traded vs OI 0
- **TSLA** PUT 357.5 2026-11-13 (9DTE): 607 traded vs OI 259
- **TSLA** PUT 355 2026-11-13 (9DTE): 762 traded vs OI 743
- **META** CALL 675 2026-11-06 (2DTE): 1,616 traded vs OI 1,602
- **META** CALL 690 2026-11-09 (5DTE): 515 traded vs OI 35
- **AMZN** CALL 270 2026-11-13 (9DTE): 3,833 traded vs OI 3,702

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
