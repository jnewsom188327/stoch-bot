# GEX + FLOW SCAN - Wed Nov 04, 03:55 PM ET
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
| 1 | **AAPL** | 349.87 | PINNED between the walls (positive gamma) - chop | **-** | 43 | - | POS +$998.5M | 343.14 | 350 | 350 | -$72.7M | +$429k bull / +$0 bear | out (clean 32, ADX 20, RVol 1.7) |
| 2 | **SMH** | 501.86 | FLOW SURGE | **CALLS** | 42 | none: 154 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (61 contracts' greeks worked out here) | NEG -$616.6M | - | 532.5 | 500 | +$24.1M | +$147k bull / +$0 bear | out (clean 33, ADX 19, RVol 1.4) |
| 3 | **UBER** | 69.96 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 36 | 11/06 69P @ 0.61 (delta 0.35) = est +26% at 69.38 | POS +$7.1M | 68.56 | 70 | 65 | -$597k | - | out (clean 31, ADX 27, RVol 1.9) |
| 4 | **NFLX** | 66.49 | - | **-** | 27 | - | POS +$21.9M | - | 65 | 65 | -$2.0M | +$28k bull / +$0 bear | out (clean 33, ADX 37, RVol 2.6) |
| 5 | **MU** | 796.69 | - | **-** | 26 | - | NEG -$418.8M | - | 800 | 800 | +$133.6M | +$3.0M bull / -$917k bear | out (clean 31, ADX 31, RVol 2.0) |
| 6 | **ARM** | 191.01 | - | **-** | 25 | - | NEG -$8.1M | - | 200 | 200 | +$1.3M | +$800k bull / +$0 bear | out (clean 26, ADX 30, RVol 2.1) |
| 7 | **MSTR** | 142.67 | - | **-** | 24 | - | POS +$138.5M | - | 135 | 150 | -$8.8M | +$66k bull / +$0 bear | out (clean 32, ADX 32, RVol 1.7) |
| 8 | **ORCL** | 124.48 | - | **-** | 24 | - | NEG -$35.7M | - | 130 | 120 | +$3.6M | +$62k bull / +$0 bear | out (clean 33, ADX 28, RVol 2.2) |
| 9 | **GOOGL** | 289.19 | - | **-** | 23 | - | POS +$109.0M | 282.83 | 290 | 290 | -$25.5M | +$168k bull / +$0 bear | out (clean 36, ADX 18, RVol 0.7) |
| 10 | **NVDA** | 200.62 | - | **-** | 22 | - | NEG -$226.6M | 203.05 | 210 | 200 | +$17.3M | +$969k bull / +$0 bear | out (clean 30, ADX 32, RVol 2.1) |
| 11 | **TSLA** | 385.42 | - | **-** | 22 | - | NEG -$78.2M | 387.02 | 400 | 385 | -$69.9M | +$1.3M bull / -$305k bear | out (clean 32, ADX 26, RVol 1.5) |
| 12 | **MSFT** | 555.56 | - | **-** | 20 | - | POS +$1.1B | - | 550 | 535 | -$14.4M | +$1.5M bull / +$0 bear | out (clean 29, ADX 20, RVol 1.5) |
| 13 | **AVGO** | 325.06 | - | **-** | 20 | - | NEG -$114.5M | - | 340 | 320 | +$5.6M | +$192k bull / +$0 bear | out (clean 30, ADX 26, RVol 1.2) |
| 14 | **AMD** | 482.21 | - | **-** | 19 | - | NEG -$91.1M | - | 500 | 480 | +$46.0M | +$410k bull / -$226k bear | out (clean 31, ADX 12, RVol 1.2) |
| 15 | **AMZN** | 267.05 | - | **-** | 19 | - | POS +$545.2M | - | 270 | 250 | -$16.4M | +$370k bull / +$0 bear | out (clean 35, ADX 12, RVol 1.9) |
| 16 | **COIN** | 151.24 | - | **-** | 19 | - | POS +$32.2M | - | 149 | 155 | -$1.1M | +$32k bull / +$0 bear | out (clean 31, ADX 11, RVol 0.6) |
| 17 | **SMCI** | 29.62 | - | **-** | 19 | - | NEG -$1.8M | - | 32 | 30 | +$2.1M | - | out (clean 33, ADX 24, RVol 1.7) |
| 18 | **SPY** | 766.36 | - | **-** | 18 | - | NEG -$4.8B | 769.42 | 770 | 767 | -$88.0M | +$1.3M bull / +$0 bear | out (clean 32, ADX 14, RVol 1.8) |
| 19 | **QQQ** | 691.13 | - | **-** | 17 | - | NEG -$5.4B | 716.79 | 690 | 680 | -$82.3M | +$992k bull / +$0 bear | out (clean 33, ADX 16, RVol 1.3) |
| 20 | **META** | 628.20 | - | **-** | 17 | - | POS +$165.9M | 621.23 | 650 | 625 | +$10.5M | +$857k bull / +$0 bear | out (clean 33, ADX 20, RVol 1.0) |
| 21 | **CRM** | 226.73 | - | **-** | 17 | - | NEG -$12.9M | - | 240 | 220 | +$46k | +$28k bull / +$0 bear | out (clean 34, ADX 16, RVol 1.7) |
| 22 | **PLTR** | 170.14 | - | **-** | 16 | - | NEG -$50.4M | - | 165 | 170 | -$1.3M | +$74k bull / +$0 bear | out (clean 26, ADX 16, RVol 1.2) |
| 23 | **SHOP** | 152.53 | - | **-** | 14 | - | NEG -$4.6M | 158.79 | 160 | 150 | -$292k | - | out (clean 33, ADX 29, RVol 1.8) |
| 24 | **BABA** | 105.50 | - | **-** | 10 | - | POS +$16.5M | 99.18 | 105 | 100 | -$102k | - | out (clean 37, ADX 32, RVol 1.6) |
| 25 | **DELL** | 370.14 | - | **-** | 9 | - | NEG -$29.7M | - | 400 | 400 | +$519k | - | out (clean 33, ADX 18, RVol 2.3) |
| 26 | **IWM** | 283.73 | - | **-** | 8 | - | NEG -$306.5M | 284.17 | 285 | 270 | +$8.7M | - | out (clean 35, ADX 13, RVol 1.5) |
| 27 | **HOOD** | 87.40 | - | **-** | 5 | - | POS +$9.7M | 82.61 | 90 | 90 | -$663k | - | out (clean 29, ADX 15, RVol 0.8) |

## Big prints this scan (93)
- **MU** PUT 790 2026-11-06 (2DTE): 191 @ 16.63 = **+$318k** BUY | vol 3,907 / OI 488
- **TSLA** PUT 400 2026-11-04 (0DTE): 200 @ 15.25 = **+$305k** BUY | vol 3,691 / OI 3,748
- **TSLA** PUT 400 2026-11-04 (0DTE): 200 @ 15.10 = **+$302k** MID | vol 3,691 / OI 3,748
- **TSLA** PUT 400 2026-11-04 (0DTE): 200 @ 14.70 = **+$294k** MID | vol 3,691 / OI 3,748
- **TSLA** PUT 400 2026-11-04 (0DTE): 200 @ 14.60 = **+$292k** MID | vol 3,691 / OI 3,748
- **TSLA** PUT 400 2026-11-04 (0DTE): 200 @ 14.35 = **+$287k** MID | vol 3,691 / OI 3,748
- **QQQ** PUT 695 2026-11-04 (0DTE): 1,000 @ 2.50 = **+$250k** SELL | vol 247,721 / OI 1,605
- **QQQ** CALL 692 2026-11-09 (5DTE): 259 @ 7.85 = **+$203k** BUY | vol 869 / OI 0
- **TSLA** CALL 380 2026-11-06 (2DTE): 198 @ 9.97 = **+$197k** BUY | vol 8,072 / OI 2,084
- **MSFT** CALL 540 2026-11-06 (2DTE): 100 @ 18.85 = **+$188k** BUY | vol 3,468 / OI 12,180
- **MSFT** CALL 540 2026-11-04 (0DTE): 100 @ 17.95 = **+$180k** BUY | vol 2,071 / OI 2,281
- **MU** PUT 800 2026-11-06 (2DTE): 74 @ 21.57 = **+$160k** BUY | vol 13,179 / OI 3,802
- **QQQ** PUT 690 2026-11-05 (1DTE): 500 @ 2.50 = **+$125k** SELL | vol 28,435 / OI 1,609
- **MU** PUT 835 2026-11-06 (2DTE): 27 @ 43.56 = **+$118k** SELL | vol 808 / OI 795
- **MSFT** CALL 550 2026-11-06 (2DTE): 108 @ 10.86 = **+$117k** BUY | vol 6,050 / OI 3,993

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 746 2026-11-06 (2DTE): 2,213 traded vs OI 2,202
- **SPY** PUT 690 2026-11-06 (2DTE): 1,766 traded vs OI 0
- **SPY** PUT 705 2026-11-13 (9DTE): 11,163 traded vs OI 11,025
- **SPY** PUT 690 2026-11-13 (9DTE): 3,092 traded vs OI 0
- **SPY** PUT 742 2026-11-13 (9DTE): 7,058 traded vs OI 6,832
- **SPY** CALL 780 2026-11-11 (7DTE): 1,123 traded vs OI 1,109
- **SPY** PUT 690 2026-11-20 (16DTE): 1,052 traded vs OI 0
- **QQQ** CALL 703 2026-11-13 (9DTE): 551 traded vs OI 550
- **QQQ** PUT 684 2026-11-11 (7DTE): 547 traded vs OI 0
- **QQQ** PUT 680 2026-11-27 (23DTE): 7,939 traded vs OI 7,805
- **QQQ** CALL 700 2026-11-27 (23DTE): 3,085 traded vs OI 922
- **IWM** PUT 282 2026-11-11 (7DTE): 881 traded vs OI 73
- **IWM** PUT 260 2026-11-13 (9DTE): 12,778 traded vs OI 11,709
- **IWM** PUT 284 2026-11-13 (9DTE): 535 traded vs OI 131
- **SMH** PUT 482.5 2026-11-06 (2DTE): 525 traded vs OI 246

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
