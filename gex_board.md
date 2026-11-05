# GEX + FLOW SCAN - Thu Nov 05, 03:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 15:00 | **SMCI** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 28.5C | 0.46 | 0.43 | -7% (0m) | **-7%** | +29% | 28.14 |
| 10:55 | **BABA** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/06 102P | 0.75 | 0.33 | -5% (9m) | **-56%** (done) | +27% | 103.58 |
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 11.35 | +1355% (60m) | **+1355%** (done) | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.20 | -12% (0m) | **-58%** (done) | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.10 | -4% (0m) | **-87%** (done) | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:00:08 ET, last candle SPY 14:59, QQQ 14:59 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 13:05 | SPY | 1m WHIPSAW | R1 | CALLS | AGAINST you | no contract: 87 calls 0-1DTE > 8 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid |
| 11:44 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:38 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 64 puts 0-1DTE > 1 priced 0.40-0.80 > 0 delta 0.15+ > 0 spread ok > 0 liquid  |
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (36 today, last 5)
- 12:55 IWM CALLS: price -0.16 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:50 IWM CALLS: price -0.60 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:45 IWM CALLS: price -0.70 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:40 IWM CALLS: price -0.66 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:20 IWM CALLS: under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMCI** | 27.63 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 51 | 11/06 28.5C @ 0.46 (delta 0.34) = est +29% at 28.14 | NEG -$4.2M | - | 30 | 30 | +$134k | - | LONG (clean 35, ADX 26, RVol 1.6) |
| 2 | **MSFT** | 539.21 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 42 | none: 129 puts 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (19 contracts' greeks worked out here) | POS +$839.1M | - | 540 | 500 | +$21.0M | +$0 bull / -$805k bear | out (clean 32, ADX 22, RVol 0.7) |
| 3 | **SPY** | 739.91 | - | **-** | 26 | - | NEG -$13.5B | 769.44 | 760 | 740 | +$1.2B | +$0 bull / -$7.5M bear | out (clean 36, ADX 31, RVol 1.3) |
| 4 | **IWM** | 272.70 | - | **-** | 25 | - | NEG -$2.8B | 286.46 | 285 | 270 | +$54.6M | +$0 bull / -$911k bear | out (clean 36, ADX 28, RVol 1.6) |
| 5 | **PLTR** | 156.15 | - | **-** | 25 | - | NEG -$47.8M | - | 165 | 150 | +$12.0M | +$0 bull / -$464k bear | out (clean 28, ADX 21, RVol 0.7) |
| 6 | **DELL** | 329.79 | - | **-** | 25 | - | NEG -$15.1M | - | 360 | 340 | +$6.3M | +$0 bull / -$35k bear | out (clean 33, ADX 22, RVol 1.3) |
| 7 | **AVGO** | 299.11 | - | **-** | 24 | - | NEG -$112.0M | - | 325 | 300 | +$8.8M | +$0 bull / -$50k bear | out (clean 31, ADX 20, RVol 1.0) |
| 8 | **MU** | 691.12 | - | **-** | 24 | - | NEG -$95.3M | - | 700 | 700 | +$221.6M | +$136k bull / -$7.0M bear | out (clean 32, ADX 23, RVol 2.4) |
| 9 | **QQQ** | 656.84 | - | **-** | 23 | - | NEG -$5.0B | - | 700 | 680 | +$827.9M | +$512k bull / -$8.4M bear | out (clean 35, ADX 25, RVol 1.0) |
| 10 | **TSLA** | 344.53 | - | **-** | 23 | - | NEG -$139.6M | - | 370 | 350 | +$110.9M | +$0 bull / -$3.3M bear | out (clean 35, ADX 22, RVol 1.5) |
| 11 | **SMH** | 459.84 | - | **-** | 22 | - | NEG -$315.3M | - | 505 | 500 | +$28.9M | +$0 bull / -$762k bear | out (clean 34, ADX 23, RVol 0.7) |
| 12 | **NVDA** | 184.38 | - | **-** | 22 | - | NEG -$258.0M | - | 200 | 190 | +$73.3M | +$103k bull / -$902k bear | out (clean 33, ADX 26, RVol 0.8) |
| 13 | **AAPL** | 346.39 | - | **-** | 21 | - | POS +$555.7M | 334.86 | 350 | 340 | +$23.5M | +$0 bull / -$221k bear | out (clean 31, ADX 22, RVol 1.4) |
| 14 | **AMZN** | 261.00 | - | **-** | 20 | - | POS +$405.2M | - | 265 | 250 | +$24.4M | +$490k bull / -$285k bear | out (clean 34, ADX 16, RVol 0.5) |
| 15 | **AMD** | 421.38 | - | **-** | 19 | - | NEG -$108.8M | - | 430 | 440 | +$33.1M | +$0 bull / -$255k bear | out (clean 32, ADX 21, RVol 0.6) |
| 16 | **MSTR** | 130.16 | - | **-** | 18 | - | POS +$66.8M | - | 135 | 125 | +$3.6M | +$0 bull / -$145k bear | out (clean 33, ADX 20, RVol 0.7) |
| 17 | **CRM** | 221.88 | - | **-** | 18 | - | NEG -$16.5M | - | 240 | 220 | +$554k | - | out (clean 34, ADX 18, RVol 1.4) |
| 18 | **META** | 607.52 | - | **-** | 16 | - | NEG -$111.3M | 621.89 | 650 | 600 | +$17.1M | +$43k bull / -$273k bear | out (clean 33, ADX 13, RVol 0.4) |
| 19 | **COIN** | 138.89 | - | **-** | 13 | - | POS +$22.8M | - | 142 | 135 | +$1.5M | - | out (clean 33, ADX 28, RVol 0.8) |
| 20 | **BABA** | 108.35 | - | **-** | 13 | - | POS +$19.9M | - | 110 | 110 | +$836k | - | out (clean 35, ADX 20, RVol 1.5) |
| 21 | **ARM** | 170.74 | - | **-** | 12 | - | NEG -$7.5M | - | 180 | 180 | +$1.4M | - | out (clean 26, ADX 16, RVol 1.0) |
| 22 | **NFLX** | 65.20 | - | **-** | 11 | - | POS +$31.0M | 62.32 | 65 | 65 | +$851k | - | out (clean 32, ADX 22, RVol 0.7) |
| 23 | **HOOD** | 79.02 | - | **-** | 11 | - | NEG -$8.3M | - | 85 | 80 | +$2.0M | - | out (clean 31, ADX 28, RVol 1.4) |
| 24 | **GOOGL** | 285.69 | - | **-** | 10 | - | POS +$31.2M | 281.47 | 290 | 290 | +$8.2M | - | out (clean 34, ADX 18, RVol 0.8) |
| 25 | **UBER** | 68.84 | - | **-** | 10 | - | POS +$5.1M | 68.07 | 70 | 65 | +$192k | - | out (clean 30, ADX 13, RVol 0.9) |
| 26 | **ORCL** | 115.99 | - | **-** | 9 | - | NEG -$58.9M | - | 125 | 115 | +$2.7M | - | out (clean 31, ADX 17, RVol 0.7) |
| 27 | **SHOP** | 145.16 | - | **-** | 7 | - | NEG -$4.9M | - | 144 | 135 | -$138k | - | out (clean 37, ADX 15, RVol 0.3) |

## Big prints this scan (214)
- **QQQ** PUT 688 2026-11-06 (1DTE): 198 @ 32.80 = **+$649k** BUY | vol 1,429 / OI 1,645
- **QQQ** PUT 688 2026-11-06 (1DTE): 198 @ 32.76 = **+$649k** BUY | vol 1,429 / OI 1,645
- **SPY** PUT 757 2026-11-05 (0DTE): 248 @ 19.44 = **+$482k** BUY | vol 59,720 / OI 245
- **QQQ** PUT 677 2026-11-06 (1DTE): 188 @ 22.40 = **+$421k** BUY | vol 3,075 / OI 957
- **QQQ** PUT 677 2026-11-06 (1DTE): 188 @ 22.38 = **+$421k** BUY | vol 3,075 / OI 957
- **QQQ** CALL 669 2026-11-06 (1DTE): 1,459 @ 2.74 = **+$400k** BUY | vol 11,813 / OI 22
- **QQQ** PUT 663 2026-11-05 (0DTE): 404 @ 8.18 = **+$330k** BUY | vol 35,656 / OI 157
- **MU** PUT 700 2026-11-09 (4DTE): 80 @ 37.87 = **+$303k** BUY | vol 4,553 / OI 0
- **QQQ** PUT 684 2026-11-05 (0DTE): 100 @ 30.00 = **+$300k** BUY | vol 4,834 / OI 664
- **QQQ** PUT 681 2026-11-06 (1DTE): 113 @ 26.05 = **+$294k** BUY | vol 1,809 / OI 501
- **QQQ** PUT 681 2026-11-06 (1DTE): 113 @ 26.05 = **+$294k** BUY | vol 1,809 / OI 501
- **QQQ** PUT 681 2026-11-06 (1DTE): 113 @ 26.03 = **+$294k** BUY | vol 1,809 / OI 501
- **QQQ** PUT 681 2026-11-06 (1DTE): 113 @ 25.95 = **+$293k** BUY | vol 1,809 / OI 501
- **IWM** PUT 283 2026-11-05 (0DTE): 264 @ 11.10 = **+$293k** BUY | vol 16,018 / OI 128
- **MU** CALL 670 2026-11-06 (1DTE): 105 @ 27.55 = **+$289k** SELL | vol 7,573 / OI 0

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 778 2026-11-06 (1DTE): 509 traded vs OI 208
- **SPY** PUT 685 2026-11-12 (7DTE): 515 traded vs OI 0
- **SPY** CALL 748 2026-11-12 (7DTE): 981 traded vs OI 1
- **SPY** PUT 726 2026-11-12 (7DTE): 536 traded vs OI 2
- **SPY** PUT 724 2026-11-11 (6DTE): 511 traded vs OI 54
- **SPY** PUT 743 2026-11-27 (22DTE): 583 traded vs OI 564
- **QQQ** CALL 711 2026-11-06 (1DTE): 1,657 traded vs OI 856
- **QQQ** CALL 692 2026-11-11 (6DTE): 785 traded vs OI 41
- **QQQ** CALL 668 2026-11-10 (5DTE): 632 traded vs OI 11
- **QQQ** CALL 678 2026-11-13 (8DTE): 521 traded vs OI 30
- **IWM** CALL 270 2026-11-13 (8DTE): 555 traded vs OI 150
- **SMH** CALL 455 2026-11-06 (1DTE): 535 traded vs OI 1
- **SMH** CALL 470 2026-11-20 (15DTE): 531 traded vs OI 311
- **TSLA** CALL 372.5 2026-11-13 (8DTE): 504 traded vs OI 25
- **AMD** CALL 425 2026-11-20 (15DTE): 513 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
