# GEX + FLOW SCAN - Wed Nov 11, 01:20 PM ET
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
Last 1m check 13:20:08 ET, last candle SPY 13:19, QQQ 13:19 | no errors
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
| 1 | **ORCL** | 129.93 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 37 | none: 26 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$5.4M | 123.49 | 130 | 125 | +$183k | +$50k bull / +$0 bear | out (clean 30, ADX 50, RVol 0.5) |
| 2 | **AAPL** | 354.90 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$2.2B | 341.94 | 355 | 355 | +$667k | +$526k bull / -$666k bear | out (clean 27, ADX 32, RVol 0.2) |
| 3 | **AMD** | 561.98 | - | **-** | 28 | - | POS +$147.0M | - | 550 | 550 | -$102.6M | +$0 bull / -$5.3M bear | out (clean 34, ADX 53, RVol 0.4) |
| 4 | **DELL** | 383.04 | - | **-** | 27 | - | POS +$2.3M | - | 380 | 380 | -$4.0M | +$0 bull / -$303k bear | out (clean 37, ADX 60, RVol 0.4) |
| 5 | **MU** | 823.84 | - | **-** | 27 | - | POS +$124.0M | - | 800 | 800 | -$221.7M | +$1.1M bull / -$1.5M bear | out (clean 34, ADX 55, RVol 0.2) |
| 6 | **SMH** | 514.86 | - | **-** | 25 | - | NEG -$10.3M | - | 515 | 500 | -$5.3M | +$110k bull / +$0 bear | out (clean 32, ADX 50, RVol 0.3) |
| 7 | **SPY** | 761.64 | - | **-** | 24 | - | NEG -$591.9M | 762.25 | 760 | 750 | -$148.4M | +$0 bull / -$386k bear | out (clean 32, ADX 53, RVol 0.5) |
| 8 | **QQQ** | 694.42 | - | **-** | 24 | - | POS +$752.2M | 690.55 | 700 | 680 | -$171.8M | +$0 bull / -$1.8M bear | out (clean 33, ADX 49, RVol 0.5) |
| 9 | **AVGO** | 353.08 | - | **-** | 21 | - | POS +$98.2M | - | 350 | 350 | +$5.0M | +$30k bull / +$0 bear | out (clean 35, ADX 40, RVol 0.4) |
| 10 | **SHOP** | 149.01 | - | **-** | 21 | - | POS +$3.2M | 145.4 | 150 | 140 | -$475k | - | out (clean 33, ADX 30, RVol 0.2) |
| 11 | **GOOGL** | 294.86 | - | **-** | 20 | - | POS +$111.8M | 290.25 | 300 | 290 | -$940k | +$0 bull / -$45k bear | out (clean 29, ADX 58, RVol 0.6) |
| 12 | **ARM** | 206.72 | - | **-** | 20 | - | POS +$5.8M | - | 200 | 200 | -$1.9M | - | out (clean 31, ADX 59, RVol 0.6) |
| 13 | **NVDA** | 176.79 | - | **-** | 19 | - | NEG -$133.9M | - | 180 | 175 | -$27.7M | +$80k bull / -$589k bear | out (clean 34, ADX 31, RVol 0.3) |
| 14 | **MSFT** | 521.80 | - | **-** | 19 | - | POS +$58.7M | 516.93 | 535 | 520 | +$12.7M | +$0 bull / -$278k bear | out (clean 32, ADX 19, RVol 0.4) |
| 15 | **NFLX** | 63.77 | - | **-** | 19 | - | NEG -$9.0M | 64.47 | 65 | 65 | -$164k | +$36k bull / +$0 bear | out (clean 28, ADX 27, RVol 0.7) |
| 16 | **AMZN** | 266.59 | - | **-** | 18 | - | POS +$398.3M | - | 270 | 265 | +$4.3M | +$0 bull / -$248k bear | out (clean 32, ADX 19, RVol 0.4) |
| 17 | **SMCI** | 31.05 | - | **-** | 17 | - | POS +$12.7M | - | 30 | 30 | -$748k | - | out (clean 33, ADX 52, RVol 0.5) |
| 18 | **MSTR** | 123.00 | - | **-** | 17 | - | POS +$1.8M | 122.22 | 133 | 120 | +$847k | +$92k bull / +$0 bear | out (clean 28, ADX 22, RVol 0.8) |
| 19 | **TSLA** | 393.56 | - | **-** | 15 | - | POS +$411.7M | - | 400 | 380 | -$5.6M | +$85k bull / -$400k bear | out (clean 31, ADX 21, RVol 0.3) |
| 20 | **META** | 640.62 | - | **-** | 14 | - | POS +$267.2M | 628.74 | 650 | 635 | +$726k | +$55k bull / +$0 bear | out (clean 31, ADX 16, RVol 0.4) |
| 21 | **IWM** | 283.52 | - | **-** | 13 | - | POS +$249.8M | 282.93 | 285 | 270 | -$5.8M | - | out (clean 35, ADX 44, RVol 0.3) |
| 22 | **HOOD** | 85.76 | - | **-** | 13 | - | POS +$16.2M | - | 85 | 85 | -$785k | - | out (clean 34, ADX 38, RVol 0.4) |
| 23 | **BABA** | 101.64 | - | **-** | 13 | - | NEG -$16.7M | 106.6 | 110 | 101 | +$351k | - | out (clean 30, ADX 16, RVol 0.2) |
| 24 | **PLTR** | 173.10 | - | **-** | 12 | - | POS +$78.9M | - | 170 | 170 | +$1.8M | - | out (clean 29, ADX 31, RVol 0.2) |
| 25 | **UBER** | 70.66 | - | **-** | 8 | - | POS +$19.1M | 68.27 | 70 | 70 | +$2k | - | out (clean 32, ADX 43, RVol 0.2) |
| 26 | **CRM** | 217.03 | - | **-** | 8 | - | NEG -$11.4M | - | 230 | 220 | -$35k | - | out (clean 29, ADX 21, RVol 0.6) |
| 27 | **COIN** | 138.28 | - | **-** | 7 | - | POS +$27.7M | - | 141 | 135 | +$100k | - | out (clean 29, ADX 27, RVol 0.8) |

## Big prints this scan (100)
- **QQQ** CALL 680 2026-11-13 (2DTE): 500 @ 15.73 = **+$786k** SELL | vol 3,418 / OI 4,338
- **AAPL** CALL 342.5 2026-11-13 (2DTE): 610 @ 12.52 = **+$764k** MID | vol 1,378 / OI 2,151
- **AAPL** CALL 347.5 2026-11-13 (2DTE): 610 @ 7.89 = **+$481k** BUY | vol 2,620 / OI 1,885
- **QQQ** CALL 687 2026-11-11 (0DTE): 300 @ 6.81 = **+$204k** SELL | vol 103,542 / OI 753
- **SMH** PUT 510 2026-11-18 (7DTE): 136 @ 11.65 = **+$158k** MID | vol 154 / OI 3
- **AAPL** CALL 355 2026-11-13 (2DTE): 610 @ 2.53 = **+$154k** MID | vol 18,260 / OI 10,645
- **QQQ** CALL 685 2026-11-11 (0DTE): 175 @ 8.60 = **+$150k** SELL | vol 66,817 / OI 1,366
- **SPY** CALL 759 2026-11-13 (2DTE): 301 @ 4.88 = **+$147k** SELL | vol 6,886 / OI 2,941
- **QQQ** CALL 700 2026-11-13 (2DTE): 500 @ 2.58 = **+$129k** SELL | vol 21,969 / OI 14,124
- **MU** CALL 785 2026-11-13 (2DTE): 28 @ 45.13 = **+$126k** SELL | vol 1,909 / OI 272
- **TSLA** PUT 402.5 2026-11-11 (0DTE): 120 @ 10.25 = **+$123k** BUY | vol 1,376 / OI 121
- **QQQ** PUT 694 2026-11-11 (0DTE): 1,000 @ 1.20 = **+$120k** BUY | vol 86,845 / OI 92
- **SPY** CALL 762 2026-11-16 (5DTE): 301 @ 3.97 = **+$119k** SELL | vol 1,252 / OI 2,883
- **AAPL** CALL 342.5 2026-11-13 (2DTE): 89 @ 12.41 = **+$110k** SELL | vol 1,378 / OI 2,151
- **MU** CALL 785 2026-11-11 (0DTE): 28 @ 37.28 = **+$104k** SELL | vol 9,822 / OI 277

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 775 2026-11-16 (5DTE): 2,488 traded vs OI 2,254
- **SPY** PUT 751 2026-11-13 (2DTE): 3,383 traded vs OI 3,200
- **SPY** CALL 755 2026-11-13 (2DTE): 5,906 traded vs OI 5,872
- **QQQ** PUT 696 2026-11-13 (2DTE): 571 traded vs OI 489
- **QQQ** PUT 690 2026-11-13 (2DTE): 11,507 traded vs OI 10,639
- **QQQ** PUT 680 2026-11-18 (7DTE): 567 traded vs OI 562
- **IWM** CALL 285 2026-11-12 (1DTE): 4,658 traded vs OI 4,634
- **IWM** PUT 285 2026-11-11 (0DTE): 522 traded vs OI 287
- **SMH** PUT 465 2026-11-11 (0DTE): 505 traded vs OI 151
- **NVDA** PUT 167.5 2026-11-20 (9DTE): 1,235 traded vs OI 1,216
- **TSLA** PUT 397.5 2026-11-13 (2DTE): 509 traded vs OI 290
- **AAPL** CALL 347.5 2026-11-13 (2DTE): 2,620 traded vs OI 1,885
- **META** PUT 605 2026-11-13 (2DTE): 524 traded vs OI 403
- **MSFT** PUT 475 2026-11-13 (2DTE): 532 traded vs OI 0
- **ORCL** CALL 142 2026-11-20 (9DTE): 535 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
