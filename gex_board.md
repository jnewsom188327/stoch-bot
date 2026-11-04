# GEX + FLOW SCAN - Wed Nov 04, 03:35 PM ET
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
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors
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
| 1 | **SMH** | 503.04 | - | **-** | 25 | - | NEG -$590.8M | - | 532.5 | 500 | +$21.8M | +$26k bull / -$1.1M bear | out (clean 33, ADX 20, RVol 0.8) |
| 2 | **MU** | 796.35 | - | **-** | 25 | - | NEG -$390.1M | - | 850 | 800 | +$127.8M | +$1.7M bull / -$1.2M bear | out (clean 31, ADX 30, RVol 1.5) |
| 3 | **AAPL** | 352.38 | - | **-** | 23 | - | POS +$803.8M | 343.03 | 350 | 350 | -$76.0M | +$158k bull / -$1.0M bear | out (clean 32, ADX 14, RVol 1.0) |
| 4 | **GOOGL** | 291.15 | - | **-** | 22 | - | POS +$111.3M | 282.88 | 290 | 290 | -$25.9M | +$187k bull / +$0 bear | out (clean 36, ADX 13, RVol 0.5) |
| 5 | **MSFT** | 557.94 | - | **-** | 21 | - | POS +$1.1B | - | 550 | 535 | -$17.5M | +$222k bull / -$930k bear | out (clean 29, ADX 22, RVol 1.4) |
| 6 | **MSTR** | 143.54 | - | **-** | 21 | - | POS +$136.7M | - | 135 | 150 | -$9.5M | +$76k bull / +$0 bear | out (clean 32, ADX 27, RVol 0.7) |
| 7 | **TSLA** | 385.74 | - | **-** | 20 | - | NEG -$67.2M | 387.83 | 400 | 385 | -$68.4M | +$1.5M bull / -$201k bear | out (clean 31, ADX 22, RVol 0.9) |
| 8 | **AVGO** | 325.61 | - | **-** | 19 | - | NEG -$104.2M | 344.34 | 340 | 320 | +$5.4M | +$58k bull / -$152k bear | out (clean 29, ADX 26, RVol 0.7) |
| 9 | **CRM** | 227.14 | - | **-** | 19 | - | NEG -$13.0M | - | 240 | 220 | -$193k | +$86k bull / +$0 bear | out (clean 34, ADX 20, RVol 0.8) |
| 10 | **NVDA** | 202.06 | - | **-** | 18 | - | NEG -$127.7M | 203.34 | 210 | 200 | +$10.4M | +$385k bull / -$229k bear | out (clean 30, ADX 25, RVol 1.0) |
| 11 | **AMD** | 483.75 | - | **-** | 18 | - | NEG -$82.3M | - | 490 | 480 | +$45.7M | +$36k bull / -$1.3M bear | out (clean 31, ADX 13, RVol 0.4) |
| 12 | **SMCI** | 29.77 | - | **-** | 18 | - | NEG -$1.7M | - | 32 | 30 | +$2.0M | - | out (clean 34, ADX 26, RVol 0.9) |
| 13 | **META** | 633.27 | - | **-** | 17 | - | POS +$202.5M | 620.99 | 650 | 625 | +$8.5M | +$0 bull / -$98k bear | out (clean 32, ADX 23, RVol 0.9) |
| 14 | **AMZN** | 268.12 | - | **-** | 17 | - | POS +$565.4M | - | 270 | 250 | -$17.7M | +$0 bull / -$181k bear | out (clean 35, ADX 12, RVol 0.9) |
| 15 | **SPY** | 768.30 | - | **-** | 16 | - | NEG -$2.1B | 769.3 | 770 | 767 | -$101.6M | +$0 bull / -$224k bear | out (clean 32, ADX 14, RVol 1.1) |
| 16 | **QQQ** | 693.26 | - | **-** | 16 | - | NEG -$4.7B | 714.61 | 700 | 680 | -$97.3M | +$867k bull / -$1.2M bear | out (clean 32, ADX 16, RVol 0.6) |
| 17 | **ORCL** | 124.50 | - | **-** | 16 | - | NEG -$35.1M | - | 130 | 125 | +$4.0M | - | out (clean 32, ADX 31, RVol 2.2) |
| 18 | **NFLX** | 66.63 | - | **-** | 15 | - | POS +$17.6M | 63.63 | 65 | 65 | -$2.1M | - | out (clean 32, ADX 34, RVol 1.4) |
| 19 | **PLTR** | 171.79 | - | **-** | 15 | - | NEG -$46.5M | - | 165 | 170 | -$1.6M | +$0 bull / -$548k bear | out (clean 26, ADX 15, RVol 0.7) |
| 20 | **SHOP** | 153.32 | - | **-** | 14 | - | NEG -$4.1M | 158.69 | 160 | 150 | -$412k | - | out (clean 33, ADX 29, RVol 0.7) |
| 21 | **ARM** | 191.51 | - | **-** | 11 | - | NEG -$8.1M | - | 200 | 200 | +$906k | - | out (clean 26, ADX 29, RVol 1.1) |
| 22 | **UBER** | 70.61 | - | **-** | 11 | - | POS +$10.2M | 68.46 | 70 | 65 | -$686k | - | out (clean 32, ADX 26, RVol 1.2) |
| 23 | **COIN** | 152.57 | - | **-** | 9 | - | POS +$27.4M | - | 148 | 150 | -$1.3M | - | out (clean 31, ADX 12, RVol 0.4) |
| 24 | **DELL** | 370.20 | - | **-** | 8 | - | NEG -$29.7M | - | 400 | 400 | +$522k | - | out (clean 33, ADX 23, RVol 1.4) |
| 25 | **BABA** | 105.87 | - | **-** | 8 | - | POS +$17.6M | - | 105 | 110 | -$147k | - | out (clean 37, ADX 29, RVol 0.7) |
| 26 | **IWM** | 283.95 | - | **-** | 6 | - | NEG -$129.9M | 284.2 | 285 | 270 | +$8.5M | - | out (clean 35, ADX 14, RVol 0.7) |
| 27 | **HOOD** | 87.80 | - | **-** | 4 | - | POS +$10.7M | - | 90 | 90 | -$790k | - | out (clean 29, ADX 14, RVol 0.5) |

## Big prints this scan (50)
- **AMD** CALL 500 2026-11-06 (2DTE): 500 @ 7.55 = **+$378k** MID | vol 9,869 / OI 1,495
- **AMD** CALL 500 2026-11-06 (2DTE): 500 @ 7.48 = **+$374k** MID | vol 9,869 / OI 1,495
- **MU** PUT 795 2026-11-11 (7DTE): 127 @ 27.07 = **+$344k** MID | vol 388 / OI 14
- **QQQ** PUT 697 2026-11-05 (1DTE): 500 @ 5.67 = **+$284k** BUY | vol 8,300 / OI 0
- **QQQ** PUT 698 2026-11-04 (0DTE): 500 @ 4.74 = **+$237k** BUY | vol 60,822 / OI 420
- **MU** PUT 830 2026-11-06 (2DTE): 57 @ 39.00 = **+$222k** MID | vol 2,006 / OI 920
- **MSFT** CALL 545 2026-11-04 (0DTE): 97 @ 13.85 = **+$134k** BUY | vol 3,295 / OI 729
- **SPY** CALL 766 2026-11-04 (0DTE): 689 @ 1.66 = **+$114k** SELL | vol 217,565 / OI 1,133
- **MU** PUT 795 2026-11-06 (2DTE): 60 @ 17.90 = **+$107k** BUY | vol 2,179 / OI 678
- **AMD** CALL 480 2026-11-06 (2DTE): 60 @ 15.80 = **+$95k** SELL | vol 2,206 / OI 265
- **PLTR** PUT 170 2026-11-06 (2DTE): 324 @ 2.50 = **+$81k** BUY | vol 21,086 / OI 7,695
- **NVDA** PUT 200 2026-11-09 (5DTE): 294 @ 2.71 = **+$80k** SELL | vol 6,661 / OI 910
- **TSLA** CALL 392.5 2026-11-09 (5DTE): 150 @ 5.00 = **+$75k** SELL | vol 1,269 / OI 175
- **TSLA** CALL 385 2026-11-06 (2DTE): 100 @ 7.35 = **+$74k** BUY | vol 13,001 / OI 1,566
- **TSLA** PUT 387.5 2026-11-06 (2DTE): 100 @ 7.05 = **+$70k** SELL | vol 9,970 / OI 2,978

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 741 2026-11-06 (2DTE): 3,012 traded vs OI 3,009
- **SPY** CALL 771 2026-11-11 (7DTE): 500 traded vs OI 0
- **SPY** PUT 750 2026-12-04 (30DTE): 641 traded vs OI 624
- **SPY** CALL 770 2026-12-04 (30DTE): 852 traded vs OI 817
- **QQQ** PUT 680 2026-11-06 (2DTE): 36,307 traded vs OI 36,002
- **QQQ** PUT 669 2026-11-06 (2DTE): 500 traded vs OI 0
- **QQQ** CALL 695 2026-11-10 (6DTE): 603 traded vs OI 583
- **QQQ** PUT 640 2026-11-09 (5DTE): 699 traded vs OI 628
- **QQQ** CALL 718 2026-11-13 (9DTE): 1,398 traded vs OI 714
- **QQQ** CALL 696 2026-11-13 (9DTE): 514 traded vs OI 191
- **TSLA** PUT 347.5 2026-11-06 (2DTE): 748 traded vs OI 0
- **META** CALL 640 2026-11-13 (9DTE): 811 traded vs OI 561
- **AMZN** PUT 245 2026-11-11 (7DTE): 514 traded vs OI 318
- **AMZN** PUT 262.5 2026-11-09 (5DTE): 537 traded vs OI 0
- **AMZN** PUT 247.5 2026-11-11 (7DTE): 614 traded vs OI 28

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
