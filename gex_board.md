# GEX + FLOW SCAN - Wed Nov 04, 01:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 13:05 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 352.5P | 0.58 | 0.57 | +5% (3m) | **-2%** | +57% | 352.38 |
| 12:50 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.40 | 0.21 | +17% (7m) | **-48%** | +109% | 267.48 |
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
Last 1m check 13:10:08 ET, last candle SPY 13:09, QQQ 13:09 | no errors
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
| 1 | **AMZN** | 270.08 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 47 | none: 84 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (35 contracts' greeks worked out here) | POS +$556.9M | - | 270 | 250 | -$22.4M | +$44k bull / -$622k bear | LONG (clean 35, ADX 36, RVol 1.2) |
| 2 | **AAPL** | 353.97 | FLOW SURGE | **PUTS** | 37 | 11/04 352.5P @ 0.67 (delta 0.32) = est +58% at 352.1 | POS +$1.1B | 343.25 | 355 | 350 | -$82.2M | +$228k bull / -$254k bear | out (clean 32, ADX 42, RVol 0.7) |
| 3 | **SMH** | 506.57 | FLOW SURGE | **CALLS** | 34 | none: 156 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (70 contracts' greeks worked out here) | NEG -$542.4M | - | 532.5 | 500 | +$21.0M | +$56k bull / +$0 bear | out (clean 32, ADX 14, RVol 0.4) |
| 4 | **GOOGL** | 292.25 | - | **-** | 24 | - | POS +$106.1M | 283.36 | 290 | 290 | -$27.4M | +$0 bull / -$48k bear | out (clean 36, ADX 21, RVol 0.3) |
| 5 | **TSLA** | 389.23 | - | **-** | 22 | - | NEG -$75.6M | 393.67 | 400 | 380 | -$86.9M | +$580k bull / -$1.7M bear | out (clean 31, ADX 21, RVol 0.7) |
| 6 | **MSFT** | 554.51 | - | **-** | 22 | - | POS +$1.0B | - | 550 | 535 | -$15.9M | +$525k bull / +$0 bear | out (clean 29, ADX 38, RVol 0.7) |
| 7 | **MU** | 807.60 | - | **-** | 20 | - | NEG -$364.3M | - | 850 | 800 | +$100.7M | +$557k bull / -$889k bear | out (clean 32, ADX 19, RVol 0.5) |
| 8 | **MSTR** | 145.34 | - | **-** | 20 | - | POS +$123.5M | - | 135 | 150 | -$3.9M | +$0 bull / -$7.7M bear | out (clean 31, ADX 33, RVol 0.3) |
| 9 | **SPY** | 768.75 | - | **-** | 19 | - | NEG -$2.1B | 770.05 | 770 | 750 | -$128.5M | +$0 bull / -$2.8M bear | out (clean 32, ADX 27, RVol 0.5) |
| 10 | **SMCI** | 30.23 | - | **-** | 19 | - | NEG -$555k | - | 33 | 30 | +$1.9M | - | out (clean 33, ADX 27, RVol 1.1) |
| 11 | **IWM** | 284.15 | - | **-** | 18 | - | NEG -$175.6M | 284.5 | 285 | 270 | +$9.1M | +$111k bull / -$61k bear | out (clean 35, ADX 17, RVol 0.8) |
| 12 | **AMD** | 485.12 | - | **-** | 18 | - | NEG -$95.2M | - | 500 | 500 | +$44.3M | +$404k bull / -$128k bear | out (clean 32, ADX 8, RVol 0.4) |
| 13 | **HOOD** | 88.42 | - | **-** | 17 | - | POS +$3.1M | 84.54 | 90 | 90 | -$932k | +$62k bull / +$0 bear | out (clean 28, ADX 22, RVol 0.7) |
| 14 | **QQQ** | 695.74 | - | **-** | 16 | - | NEG -$4.7B | 719.74 | 700 | 680 | -$140.6M | +$570k bull / +$0 bear | out (clean 32, ADX 12, RVol 0.6) |
| 15 | **META** | 639.22 | - | **-** | 16 | - | POS +$239.2M | 622.61 | 650 | 625 | +$1.2M | +$1.2M bull / +$0 bear | out (clean 31, ADX 26, RVol 0.6) |
| 16 | **NVDA** | 203.68 | - | **-** | 15 | - | NEG -$34.2M | 204.02 | 210 | 200 | -$230k | +$129k bull / -$545k bear | out (clean 30, ADX 19, RVol 1.0) |
| 17 | **UBER** | 71.39 | - | **-** | 15 | - | POS +$12.3M | 68.26 | 70 | 70 | -$1.2M | - | out (clean 30, ADX 27, RVol 0.8) |
| 18 | **NFLX** | 66.13 | - | **-** | 14 | - | POS +$20.3M | 62.34 | 65 | 65 | -$1.9M | - | out (clean 31, ADX 32, RVol 1.1) |
| 19 | **BABA** | 107.16 | - | **-** | 14 | - | POS +$16.2M | - | 110 | 110 | -$804k | - | out (clean 36, ADX 28, RVol 0.9) |
| 20 | **COIN** | 152.90 | - | **-** | 12 | - | POS +$28.4M | - | 148 | 155 | -$1.3M | - | out (clean 31, ADX 20, RVol 0.2) |
| 21 | **SHOP** | 151.46 | - | **-** | 11 | - | NEG -$5.9M | - | 160 | 150 | -$351k | - | out (clean 33, ADX 19, RVol 0.4) |
| 22 | **ARM** | 193.39 | - | **-** | 10 | - | NEG -$6.9M | - | 200 | 200 | +$760k | - | out (clean 26, ADX 20, RVol 0.5) |
| 23 | **ORCL** | 126.32 | - | **-** | 8 | - | NEG -$31.0M | - | 130 | 125 | +$2.4M | - | out (clean 34, ADX 8, RVol 1.1) |
| 24 | **CRM** | 226.63 | - | **-** | 8 | - | NEG -$12.5M | - | 240 | 220 | -$125k | - | out (clean 33, ADX 27, RVol 0.3) |
| 25 | **DELL** | 373.92 | - | **-** | 7 | - | NEG -$30.5M | - | 400 | 400 | +$1.4M | - | out (clean 32, ADX 18, RVol 0.6) |
| 26 | **AVGO** | 328.15 | - | **-** | 6 | - | NEG -$88.9M | - | 340 | 330 | +$2.2M | - | out (clean 30, ADX 16, RVol 0.8) |
| 27 | **PLTR** | 170.81 | - | **-** | 6 | - | NEG -$50.7M | - | 165 | 170 | -$1.3M | - | out (clean 26, ADX 22, RVol 0.5) |

## Big prints this scan (55)
- **META** CALL 632.5 2026-11-06 (2DTE): 296 @ 14.37 = **+$425k** BUY | vol 2,063 / OI 1,305
- **QQQ** CALL 697 2026-11-04 (0DTE): 1,964 @ 1.12 = **+$220k** BUY | vol 172,561 / OI 930
- **AAPL** CALL 340 2026-11-06 (2DTE): 100 @ 14.65 = **+$146k** BUY | vol 3,565 / OI 3,962
- **QQQ** CALL 698 2026-11-04 (0DTE): 1,964 @ 0.74 = **+$145k** BUY | vol 183,187 / OI 1,238
- **AMD** PUT 490 2026-11-04 (0DTE): 210 @ 5.74 = **+$121k** SELL | vol 7,813 / OI 408
- **TSLA** CALL 392.5 2026-11-06 (2DTE): 200 @ 5.80 = **+$116k** BUY | vol 4,774 / OI 718
- **TSLA** CALL 390 2026-11-06 (2DTE): 170 @ 6.80 = **+$116k** BUY | vol 18,563 / OI 2,560
- **TSLA** PUT 400 2026-11-04 (0DTE): 100 @ 10.20 = **+$102k** SELL | vol 1,398 / OI 3,748
- **QQQ** CALL 695 2026-11-05 (1DTE): 200 @ 5.00 = **+$100k** BUY | vol 22,412 / OI 1,194
- **AMD** PUT 500 2026-11-04 (0DTE): 70 @ 13.58 = **+$95k** SELL | vol 4,507 / OI 1,175
- **MSFT** CALL 537.5 2026-11-04 (0DTE): 50 @ 17.55 = **+$88k** BUY | vol 681 / OI 442
- **AMD** CALL 490 2026-11-06 (2DTE): 64 @ 12.95 = **+$83k** BUY | vol 3,588 / OI 355
- **NVDA** PUT 202.5 2026-11-06 (2DTE): 222 @ 2.86 = **+$63k** SELL | vol 22,934 / OI 4,698
- **MU** PUT 800 2026-11-06 (2DTE): 40 @ 15.60 = **+$62k** SELL | vol 8,908 / OI 3,802
- **HOOD** CALL 88 2026-11-06 (2DTE): 270 @ 2.30 = **+$62k** BUY | vol 7,254 / OI 1,496

## New unusual volume (traded more than open interest, 500+)
- **IWM** CALL 287 2026-11-13 (9DTE): 3,127 traded vs OI 3,112
- **IWM** PUT 283 2026-11-10 (6DTE): 514 traded vs OI 53
- **NVDA** CALL 195 2026-11-13 (9DTE): 519 traded vs OI 269
- **AAPL** CALL 365 2026-11-13 (9DTE): 3,145 traded vs OI 3,014
- **AAPL** PUT 325 2026-12-04 (30DTE): 548 traded vs OI 435
- **META** CALL 640 2026-11-09 (5DTE): 502 traded vs OI 91
- **AVGO** PUT 325 2026-11-06 (2DTE): 1,850 traded vs OI 1,819
- **HOOD** CALL 92 2026-12-04 (30DTE): 1,722 traded vs OI 1,350

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
