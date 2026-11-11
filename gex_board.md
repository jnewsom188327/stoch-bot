# GEX + FLOW SCAN - Wed Nov 11, 01:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (12)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:40 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 522.5C | 0.73 | 1.07 | +73% (34m) | **+47%** (done) | +146% | 523.2 |
| 11:05 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.64 | 0.36 | +2% (1m) | **-44%** (done) | +363% | 527.5 |
| 10:45 | **AVGO** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/11 345P | 0.78 | 0.10 | +6% (1m) | **-87%** (done) | +149% | 345 |
| 10:35 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.76 | 0.25 | +96% (9m) | **-67%** (done) | +343% | 527.5 |
| 10:20 | **AVGO** | **CALLS** | TREND + FLOW | 11/11 355C | 0.71 | 0.76 | +127% (38m) | **+7%** (done) | +280% | 356.78 |
| 10:15 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.65 | 1.05 | +72% (56m) | **+62%** (done) | +66% | 282.84 hit |
| 10:05 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 175C | 0.76 | 1.54 | +142% (51m) | **+103%** (done) | +58% | 175 hit |
| 09:50 | **GOOGL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 292.5C | 0.51 | 0.62 | +39% (28m) | **+22%** (done) | +82% | 291.86 |
| 09:45 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.68 | 0.64 | +85% (6m) | **-6%** (done) | +68% | 282.96 |
| 09:45 | **QQQ** | **CALLS** | FLOW SURGE | 11/11 690C | 0.63 | 1.23 | +103% (59m) | **+95%** (done) | +171% | 689.78 |
| 09:39 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 693C | 0.52 | 0.29 | -10% (0m) | **-44%** (done) | +92% | 690.43 |
| 09:39 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 760C | 0.53 | 0.17 | -2% (0m) | **-68%** (done) | +79% | 758.82 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:40:08 ET, last candle SPY 13:39, QQQ 13:39 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:02 | QQQ | 1m AGREE FLIP | FULL | CALLS | up | logged (agree flip) |
| 09:38 | QQQ | 1m WHIPSAW | R1 R5 | CALLS | TURNING away | **FIRE** QQQ261111C00693000 |
| 09:38 | SPY | 1m WHIPSAW | R1 R5 | CALLS | TURNING away | **FIRE** SPY261111C00760000 |

## Flow surges NOT fired - price disagreed (7 today, last 5)
- 10:15 BABA CALLS: under EMA 20 - flow says one way, price says the other
- 10:00 MSFT CALLS: price -4.55 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AMZN CALLS: price -0.73 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 AAPL PUTS: price +1.32 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSFT CALLS: price -2.01 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMH** | 515.12 | FLIP CROSS down into negative gamma | **PUTS** | 36 | 11/11 512.5P @ 0.56 (delta 0.24) = est +60% at 512.56 | NEG -$858k | 515.71 | 515 | 500 | -$5.1M | +$0 bull / -$148k bear | out (clean 32, ADX 47, RVol 0.2) |
| 2 | **AMD** | 565.34 | - | **-** | 28 | - | POS +$140.5M | - | 550 | 550 | -$111.6M | +$0 bull / -$2.2M bear | out (clean 34, ADX 57, RVol 0.6) |
| 3 | **MU** | 824.16 | - | **-** | 27 | - | POS +$144.9M | - | 800 | 800 | -$224.4M | +$612k bull / -$1.1M bear | out (clean 34, ADX 52, RVol 0.3) |
| 4 | **SPY** | 761.97 | - | **-** | 24 | - | NEG -$185.9M | 762.16 | 760 | 750 | -$160.5M | +$763k bull / +$0 bear | out (clean 33, ADX 52, RVol 0.3) |
| 5 | **QQQ** | 694.80 | - | **-** | 24 | - | POS +$928.8M | 690.53 | 700 | 680 | -$181.8M | +$105k bull / -$455k bear | out (clean 33, ADX 47, RVol 0.4) |
| 6 | **PLTR** | 173.36 | - | **-** | 22 | - | POS +$80.0M | - | 170 | 180 | +$1.7M | +$0 bull / -$95k bear | out (clean 29, ADX 35, RVol 0.4) |
| 7 | **ORCL** | 130.00 | PINNED between the walls (positive gamma) - chop | **-** | 22 | - | POS +$5.3M | 123.02 | 130 | 130 | +$363k | - | out (clean 30, ADX 46, RVol 0.4) |
| 8 | **GOOGL** | 295.16 | - | **-** | 21 | - | POS +$130.3M | 289.09 | 300 | 290 | -$1.3M | +$0 bull / -$141k bear | out (clean 29, ADX 60, RVol 0.7) |
| 9 | **SHOP** | 149.62 | - | **-** | 21 | - | POS +$3.8M | 145.2 | 150 | 140 | -$475k | - | out (clean 33, ADX 27, RVol 0.2) |
| 10 | **AVGO** | 352.73 | - | **-** | 20 | - | POS +$104.9M | - | 350 | 350 | +$5.2M | +$121k bull / +$0 bear | out (clean 35, ADX 31, RVol 0.6) |
| 11 | **NVDA** | 177.25 | - | **-** | 19 | - | NEG -$122.2M | - | 180 | 175 | -$31.4M | +$132k bull / -$811k bear | out (clean 34, ADX 33, RVol 0.3) |
| 12 | **MSFT** | 521.55 | - | **-** | 19 | - | POS +$58.2M | 517.21 | 535 | 520 | +$13.1M | +$41k bull / -$133k bear | out (clean 32, ADX 17, RVol 0.5) |
| 13 | **ARM** | 206.77 | - | **-** | 19 | - | POS +$5.6M | - | 200 | 200 | -$1.9M | - | out (clean 31, ADX 54, RVol 0.6) |
| 14 | **AAPL** | 355.07 | PINNED between the walls (positive gamma) - chop | **-** | 18 | - | POS +$2.3B | 341.83 | 355 | 355 | -$509k | - | out (clean 28, ADX 35, RVol 0.3) |
| 15 | **DELL** | 384.04 | - | **-** | 17 | - | POS +$2.6M | - | 380 | 380 | -$4.1M | - | out (clean 37, ADX 56, RVol 0.3) |
| 16 | **SMCI** | 31.05 | - | **-** | 17 | - | POS +$12.8M | - | 30 | 30 | -$750k | - | out (clean 33, ADX 44, RVol 0.4) |
| 17 | **TSLA** | 393.77 | - | **-** | 15 | - | POS +$426.7M | - | 400 | 380 | -$6.7M | +$45k bull / -$601k bear | out (clean 31, ADX 20, RVol 0.3) |
| 18 | **META** | 640.06 | - | **-** | 15 | - | POS +$284.1M | 627.41 | 650 | 635 | +$1.2M | +$244k bull / +$0 bear | out (clean 30, ADX 20, RVol 0.3) |
| 19 | **HOOD** | 85.84 | - | **-** | 13 | - | POS +$15.8M | - | 85 | 85 | -$821k | - | out (clean 34, ADX 38, RVol 0.5) |
| 20 | **IWM** | 283.36 | - | **-** | 12 | - | POS +$252.5M | 282.82 | 285 | 270 | -$5.8M | - | out (clean 35, ADX 40, RVol 0.2) |
| 21 | **BABA** | 101.68 | - | **-** | 12 | - | NEG -$17.0M | 106.57 | 110 | 101 | +$351k | - | out (clean 30, ADX 16, RVol 0.1) |
| 22 | **NFLX** | 63.95 | - | **-** | 9 | - | NEG -$8.8M | 64.63 | 65 | 65 | -$222k | - | out (clean 28, ADX 23, RVol 0.7) |
| 23 | **UBER** | 70.91 | - | **-** | 9 | - | POS +$19.9M | 68.31 | 70 | 70 | -$16k | - | out (clean 32, ADX 48, RVol 0.4) |
| 24 | **AMZN** | 266.77 | - | **-** | 7 | - | POS +$408.2M | - | 270 | 265 | +$3.6M | - | out (clean 32, ADX 16, RVol 0.5) |
| 25 | **CRM** | 217.12 | - | **-** | 7 | - | NEG -$11.4M | - | 230 | 220 | -$37k | - | out (clean 29, ADX 17, RVol 0.3) |
| 26 | **COIN** | 138.57 | - | **-** | 5 | - | POS +$28.0M | - | 141 | 135 | +$54k | - | out (clean 29, ADX 25, RVol 0.2) |
| 27 | **MSTR** | 122.81 | - | **-** | 5 | - | POS +$1.2M | 122.32 | 133 | 120 | +$898k | - | out (clean 28, ADX 18, RVol 0.3) |

## Big prints this scan (55)
- **SPY** CALL 764 2026-11-18 (7DTE): 1,076 @ 4.84 = **+$521k** BUY | vol 1,973 / OI 2,086
- **AMD** PUT 570 2026-11-11 (0DTE): 496 @ 6.80 = **+$337k** BUY | vol 1,066 / OI 11
- **SPY** CALL 764 2026-11-18 (7DTE): 499 @ 4.85 = **+$242k** BUY | vol 1,973 / OI 2,086
- **SMH** CALL 500 2026-11-13 (2DTE): 116 @ 18.35 = **+$213k** MID | vol 1,338 / OI 4,456
- **NVDA** CALL 175 2026-11-18 (7DTE): 200 @ 9.30 = **+$186k** MID | vol 7,521 / OI 1,154
- **TSLA** CALL 390 2026-11-11 (0DTE): 480 @ 3.70 = **+$178k** SELL | vol 89,236 / OI 2,864
- **QQQ** CALL 695 2026-11-11 (0DTE): 1,677 @ 0.77 = **+$129k** SELL | vol 279,244 / OI 1,616
- **META** CALL 640 2026-11-11 (0DTE): 500 @ 2.56 = **+$128k** BUY | vol 18,054 / OI 1,118
- **QQQ** PUT 695 2026-11-12 (1DTE): 300 @ 3.50 = **+$105k** SELL | vol 6,538 / OI 244
- **NVDA** PUT 172.5 2026-11-16 (5DTE): 400 @ 2.50 = **+$100k** MID | vol 4,159 / OI 1,223
- **TSLA** CALL 390 2026-11-11 (0DTE): 264 @ 3.70 = **+$98k** SELL | vol 89,236 / OI 2,864
- **NVDA** CALL 175 2026-11-11 (0DTE): 397 @ 2.20 = **+$87k** BUY | vol 282,553 / OI 3,333
- **MU** CALL 800 2026-11-13 (2DTE): 20 @ 34.77 = **+$70k** SELL | vol 13,057 / OI 5,495
- **TSLA** CALL 390 2026-11-11 (0DTE): 164 @ 3.70 = **+$61k** SELL | vol 89,236 / OI 2,864
- **MU** CALL 810 2026-11-11 (0DTE): 40 @ 14.50 = **+$58k** SELL | vol 34,037 / OI 513

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 776 2026-11-16 (5DTE): 529 traded vs OI 423
- **SPY** CALL 776 2026-11-18 (7DTE): 1,876 traded vs OI 1,779
- **SPY** CALL 785 2026-11-27 (16DTE): 1,874 traded vs OI 1,083
- **QQQ** PUT 697 2026-11-12 (1DTE): 529 traded vs OI 29
- **QQQ** CALL 706 2026-11-20 (9DTE): 1,837 traded vs OI 1,792
- **IWM** CALL 285 2026-11-19 (8DTE): 544 traded vs OI 202
- **IWM** CALL 283 2026-11-19 (8DTE): 916 traded vs OI 106
- **IWM** CALL 289 2026-11-19 (8DTE): 561 traded vs OI 115
- **NVDA** PUT 170 2026-11-18 (7DTE): 1,353 traded vs OI 1,341
- **NVDA** CALL 192.5 2026-11-18 (7DTE): 501 traded vs OI 0
- **NVDA** CALL 160 2026-11-11 (0DTE): 500 traded vs OI 203
- **AMD** PUT 530 2026-11-16 (5DTE): 517 traded vs OI 10
- **AMD** PUT 570 2026-11-11 (0DTE): 1,066 traded vs OI 11
- **GOOGL** PUT 282.5 2026-11-11 (0DTE): 542 traded vs OI 540
- **MU** CALL 870 2026-11-18 (7DTE): 718 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
