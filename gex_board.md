# GEX + FLOW SCAN - Wed Nov 11, 01:50 PM ET
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
Last 1m check 13:50:08 ET, last candle SPY 13:49, QQQ 13:49 | no errors
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
| 1 | **AAPL** | 355.15 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$2.3B | 341.95 | 355 | 355 | -$951k | +$0 bull / -$28k bear | out (clean 28, ADX 37, RVol 0.3) |
| 2 | **AMD** | 565.71 | - | **-** | 29 | - | POS +$149.9M | - | 550 | 550 | -$116.2M | +$43k bull / -$1.5M bear | out (clean 34, ADX 59, RVol 0.7) |
| 3 | **MU** | 825.72 | - | **-** | 27 | - | POS +$147.6M | - | 800 | 800 | -$227.7M | +$382k bull / -$3.5M bear | out (clean 34, ADX 50, RVol 0.3) |
| 4 | **SMCI** | 31.04 | - | **-** | 26 | - | POS +$13.0M | - | 32 | 30 | -$721k | +$48k bull / +$0 bear | out (clean 33, ADX 40, RVol 0.4) |
| 5 | **QQQ** | 695.12 | - | **-** | 25 | - | POS +$1.0B | 690.51 | 700 | 680 | -$191.1M | +$105k bull / -$1.4M bear | out (clean 33, ADX 47, RVol 0.5) |
| 6 | **SMH** | 515.62 | - | **-** | 25 | - | NEG -$11.8M | - | 500 | 500 | -$5.4M | +$0 bull / -$84k bear | out (clean 31, ADX 47, RVol 0.2) |
| 7 | **SPY** | 762.26 | - | **-** | 24 | - | POS +$139.9M | 762.23 | 760 | 750 | -$170.1M | +$763k bull / -$908k bear | out (clean 33, ADX 52, RVol 0.2) |
| 8 | **HOOD** | 86.08 | - | **-** | 24 | - | POS +$16.2M | - | 85 | 85 | -$948k | +$0 bull / -$45k bear | out (clean 34, ADX 38, RVol 0.4) |
| 9 | **ORCL** | 130.28 | PINNED between the walls (positive gamma) - chop | **-** | 21 | - | POS +$5.9M | - | 130 | 130 | +$44k | - | out (clean 30, ADX 45, RVol 0.5) |
| 10 | **NVDA** | 177.10 | - | **-** | 20 | - | NEG -$127.2M | 179.65 | 180 | 175 | -$32.7M | +$730k bull / -$1.1M bear | out (clean 34, ADX 33, RVol 0.3) |
| 11 | **SHOP** | 149.43 | - | **-** | 20 | - | POS +$3.6M | 145.37 | 150 | 140 | -$474k | - | out (clean 33, ADX 25, RVol 0.2) |
| 12 | **AVGO** | 353.00 | - | **-** | 19 | - | POS +$102.2M | - | 350 | 350 | +$5.0M | +$0 bull / -$32k bear | out (clean 35, ADX 28, RVol 0.6) |
| 13 | **ARM** | 206.51 | - | **-** | 19 | - | POS +$5.6M | - | 200 | 200 | -$1.9M | - | out (clean 31, ADX 51, RVol 0.5) |
| 14 | **MSFT** | 522.15 | - | **-** | 18 | - | POS +$60.7M | 516.96 | 535 | 520 | +$12.3M | +$282k bull / +$0 bear | out (clean 32, ADX 15, RVol 0.4) |
| 15 | **DELL** | 383.64 | - | **-** | 17 | - | POS +$2.4M | - | 380 | 380 | -$4.1M | - | out (clean 37, ADX 55, RVol 0.2) |
| 16 | **TSLA** | 394.17 | - | **-** | 15 | - | POS +$443.4M | - | 400 | 380 | -$8.6M | +$0 bull / -$1.3M bear | out (clean 31, ADX 21, RVol 0.3) |
| 17 | **META** | 639.73 | - | **-** | 15 | - | POS +$277.6M | 628 | 650 | 635 | +$1.3M | +$244k bull / +$0 bear | out (clean 30, ADX 23, RVol 0.4) |
| 18 | **BABA** | 101.67 | - | **-** | 13 | - | NEG -$16.8M | 106.38 | 110 | 101 | +$362k | - | out (clean 30, ADX 16, RVol 0.2) |
| 19 | **IWM** | 283.47 | - | **-** | 12 | - | POS +$290.8M | 282.84 | 285 | 270 | -$5.8M | - | out (clean 35, ADX 37, RVol 0.1) |
| 20 | **PLTR** | 173.68 | - | **-** | 12 | - | POS +$78.5M | - | 170 | 180 | +$1.7M | - | out (clean 29, ADX 36, RVol 0.4) |
| 21 | **GOOGL** | 295.48 | - | **-** | 10 | - | POS +$118.1M | 291 | 300 | 290 | -$914k | - | out (clean 30, ADX 60, RVol 0.5) |
| 22 | **UBER** | 71.05 | - | **-** | 10 | - | POS +$20.6M | 68.32 | 70 | 70 | -$24k | - | out (clean 32, ADX 51, RVol 0.7) |
| 23 | **NFLX** | 64.00 | - | **-** | 8 | - | NEG -$7.8M | 64.52 | 65 | 65 | -$209k | - | out (clean 27, ADX 22, RVol 0.6) |
| 24 | **AMZN** | 266.93 | - | **-** | 7 | - | POS +$418.5M | - | 270 | 265 | +$3.2M | - | out (clean 32, ADX 18, RVol 0.6) |
| 25 | **CRM** | 217.41 | - | **-** | 7 | - | NEG -$11.5M | - | 230 | 220 | -$40k | - | out (clean 29, ADX 16, RVol 0.3) |
| 26 | **COIN** | 138.78 | - | **-** | 5 | - | POS +$28.5M | - | 141 | 135 | +$30k | - | out (clean 29, ADX 26, RVol 0.2) |
| 27 | **MSTR** | 122.89 | - | **-** | 5 | - | POS +$1.8M | 122.34 | 133 | 120 | +$702k | - | out (clean 28, ADX 16, RVol 0.2) |

## Big prints this scan (74)
- **QQQ** CALL 687 2026-11-11 (0DTE): 500 @ 8.30 = **+$415k** SELL | vol 106,356 / OI 753
- **QQQ** CALL 687 2026-11-11 (0DTE): 500 @ 8.05 = **+$402k** SELL | vol 106,356 / OI 753
- **MU** CALL 800 2026-11-13 (2DTE): 112 @ 35.25 = **+$395k** SELL | vol 13,248 / OI 5,495
- **QQQ** CALL 687 2026-11-11 (0DTE): 463 @ 8.23 = **+$381k** SELL | vol 106,356 / OI 753
- **SPY** CALL 764 2026-11-13 (2DTE): 1,088 @ 2.34 = **+$255k** SELL | vol 8,852 / OI 3,975
- **TSLA** CALL 390 2026-11-11 (0DTE): 500 @ 3.70 = **+$185k** SELL | vol 91,314 / OI 2,864
- **TSLA** CALL 390 2026-11-11 (0DTE): 500 @ 3.55 = **+$178k** SELL | vol 91,314 / OI 2,864
- **SPY** CALL 754 2026-11-12 (1DTE): 200 @ 8.70 = **+$174k** SELL | vol 5,651 / OI 623
- **TSLA** CALL 390 2026-11-11 (0DTE): 457 @ 3.50 = **+$160k** SELL | vol 91,314 / OI 2,864
- **AMD** CALL 560 2026-11-11 (0DTE): 250 @ 6.00 = **+$150k** SELL | vol 41,922 / OI 616
- **SPY** CALL 756 2026-11-12 (1DTE): 200 @ 6.90 = **+$138k** SELL | vol 11,545 / OI 493
- **SMH** CALL 495 2026-11-11 (0DTE): 61 @ 20.68 = **+$126k** MID | vol 887 / OI 1,817
- **MU** PUT 815 2026-11-13 (2DTE): 72 @ 16.20 = **+$117k** BUY | vol 2,883 / OI 225
- **QQQ** CALL 687 2026-11-11 (0DTE): 135 @ 8.20 = **+$111k** SELL | vol 106,356 / OI 753
- **MU** CALL 800 2026-11-13 (2DTE): 28 @ 35.20 = **+$99k** SELL | vol 13,248 / OI 5,495

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 721 2026-11-12 (1DTE): 520 traded vs OI 439
- **SPY** PUT 761 2026-11-16 (5DTE): 500 traded vs OI 144
- **SPY** PUT 722 2026-11-12 (1DTE): 645 traded vs OI 476
- **SPY** PUT 702 2026-11-12 (1DTE): 1,499 traded vs OI 584
- **SPY** PUT 758 2026-11-20 (9DTE): 2,481 traded vs OI 2,340
- **SPY** PUT 745 2026-12-04 (23DTE): 1,800 traded vs OI 1,786
- **QQQ** PUT 695 2026-11-13 (2DTE): 4,302 traded vs OI 4,296
- **QQQ** CALL 715 2026-11-17 (6DTE): 613 traded vs OI 558
- **SMH** PUT 470 2026-11-20 (9DTE): 2,542 traded vs OI 2,352
- **NVDA** PUT 165 2026-11-13 (2DTE): 15,532 traded vs OI 15,309
- **AMD** PUT 542.5 2026-11-13 (2DTE): 508 traded vs OI 104
- **ORCL** CALL 136 2026-11-13 (2DTE): 753 traded vs OI 752
- **ORCL** PUT 131 2026-11-13 (2DTE): 865 traded vs OI 581

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
