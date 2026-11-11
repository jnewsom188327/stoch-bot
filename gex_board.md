# GEX + FLOW SCAN - Wed Nov 11, 02:00 PM ET
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
Last 1m check 14:00:08 ET, last candle SPY 13:59, QQQ 13:59 | no errors
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
| 1 | **SMH** | 514.77 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 40 | none: 164 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (68 contracts' greeks worked out here) | POS +$5.3M | 513.94 | 515 | 500 | -$4.9M | +$194k bull / -$209k bear | out (clean 31, ADX 45, RVol 0.1) |
| 2 | **ORCL** | 130.03 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 36 | none: 26 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$4.9M | 124.95 | 130 | 125 | +$182k | +$0 bull / -$27k bear | out (clean 30, ADX 42, RVol 0.4) |
| 3 | **AAPL** | 354.98 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$2.2B | 341.09 | 355 | 355 | -$529k | +$0 bull / -$28k bear | out (clean 28, ADX 36, RVol 0.3) |
| 4 | **AMD** | 565.77 | - | **-** | 29 | - | POS +$143.3M | - | 550 | 550 | -$115.7M | +$719k bull / -$3.0M bear | out (clean 34, ADX 61, RVol 0.8) |
| 5 | **IWM** | 283.45 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 27 | 11/11 284P @ 0.72 (delta 0.71) = est +38% at 283 | POS +$255.8M | 282.79 | 283 | 270 | -$5.7M | - | out (clean 35, ADX 34, RVol 0.2) |
| 6 | **MU** | 825.43 | - | **-** | 27 | - | POS +$104.3M | - | 800 | 800 | -$224.1M | +$1.7M bull / -$4.3M bear | out (clean 33, ADX 49, RVol 0.3) |
| 7 | **SPY** | 762.08 | - | **-** | 24 | - | NEG -$123.1M | 762.16 | 760 | 750 | -$168.3M | +$0 bull / -$908k bear | out (clean 33, ADX 50, RVol 0.2) |
| 8 | **QQQ** | 694.70 | - | **-** | 24 | - | POS +$774.9M | 691.73 | 700 | 680 | -$187.0M | +$247k bull / -$1.4M bear | out (clean 32, ADX 45, RVol 0.5) |
| 9 | **SMCI** | 30.95 | - | **-** | 24 | - | POS +$12.8M | - | 30 | 30 | -$704k | +$48k bull / +$0 bear | out (clean 32, ADX 35, RVol 0.3) |
| 10 | **HOOD** | 86.00 | - | **-** | 23 | - | POS +$16.0M | - | 85 | 85 | -$911k | +$0 bull / -$45k bear | out (clean 34, ADX 39, RVol 0.4) |
| 11 | **PLTR** | 173.72 | - | **-** | 21 | - | POS +$78.1M | - | 170 | 180 | +$1.4M | +$0 bull / -$232k bear | out (clean 29, ADX 37, RVol 0.2) |
| 12 | **SHOP** | 149.24 | - | **-** | 20 | - | POS +$3.4M | 145.38 | 150 | 140 | -$474k | - | out (clean 33, ADX 22, RVol 0.2) |
| 13 | **NVDA** | 176.88 | - | **-** | 19 | - | NEG -$131.3M | - | 180 | 175 | -$31.8M | +$791k bull / -$806k bear | out (clean 34, ADX 33, RVol 0.3) |
| 14 | **ARM** | 206.34 | - | **-** | 19 | - | POS +$5.7M | - | 200 | 200 | -$1.9M | - | out (clean 31, ADX 48, RVol 0.4) |
| 15 | **MSFT** | 521.41 | - | **-** | 18 | - | POS +$67.8M | 516.42 | 535 | 520 | +$12.7M | +$342k bull / +$0 bear | out (clean 32, ADX 14, RVol 0.4) |
| 16 | **AVGO** | 352.59 | - | **-** | 18 | - | POS +$103.9M | - | 350 | 350 | +$5.8M | +$108k bull / -$32k bear | out (clean 35, ADX 24, RVol 0.5) |
| 17 | **META** | 637.44 | - | **-** | 17 | - | POS +$255.1M | 625.98 | 650 | 635 | +$2.4M | +$46k bull / +$0 bear | out (clean 30, ADX 26, RVol 0.6) |
| 18 | **AMZN** | 266.59 | - | **-** | 17 | - | POS +$405.2M | - | 270 | 265 | +$4.0M | +$301k bull / +$0 bear | out (clean 32, ADX 17, RVol 0.6) |
| 19 | **DELL** | 383.61 | - | **-** | 17 | - | POS +$2.4M | - | 380 | 380 | -$4.0M | - | out (clean 37, ADX 53, RVol 0.2) |
| 20 | **TSLA** | 394.34 | - | **-** | 16 | - | POS +$411.1M | - | 400 | 380 | -$8.6M | +$26k bull / -$1.2M bear | out (clean 32, ADX 23, RVol 0.4) |
| 21 | **BABA** | 101.68 | - | **-** | 13 | - | NEG -$17.1M | 106.53 | 110 | 101 | +$359k | - | out (clean 30, ADX 17, RVol 0.2) |
| 22 | **UBER** | 71.05 | - | **-** | 10 | - | POS +$21.1M | 68.29 | 70 | 70 | -$30k | - | out (clean 32, ADX 53, RVol 0.6) |
| 23 | **GOOGL** | 294.94 | - | **-** | 9 | - | POS +$128.9M | 289.23 | 300 | 290 | -$575k | - | out (clean 29, ADX 58, RVol 0.4) |
| 24 | **NFLX** | 63.95 | - | **-** | 8 | - | NEG -$8.6M | 64.57 | 65 | 65 | -$218k | - | out (clean 27, ADX 21, RVol 0.7) |
| 25 | **CRM** | 217.35 | - | **-** | 7 | - | NEG -$11.2M | - | 230 | 220 | -$42k | - | out (clean 29, ADX 15, RVol 0.4) |
| 26 | **COIN** | 138.44 | - | **-** | 5 | - | POS +$26.7M | - | 141 | 135 | +$62k | - | out (clean 28, ADX 25, RVol 0.2) |
| 27 | **MSTR** | 122.80 | - | **-** | 5 | - | POS +$262k | 122.33 | 133 | 120 | +$802k | - | out (clean 28, ADX 15, RVol 0.2) |

## Big prints this scan (70)
- **MU** CALL 810 2026-11-11 (0DTE): 249 @ 14.81 = **+$369k** BUY | vol 34,526 / OI 513
- **MU** CALL 810 2026-11-11 (0DTE): 181 @ 14.98 = **+$271k** BUY | vol 34,526 / OI 513
- **MU** CALL 815 2026-11-11 (0DTE): 249 @ 10.31 = **+$257k** MID | vol 30,811 / OI 988
- **SMH** CALL 500 2026-11-13 (2DTE): 103 @ 18.85 = **+$194k** BUY | vol 1,574 / OI 4,456
- **MU** CALL 815 2026-11-11 (0DTE): 181 @ 10.48 = **+$190k** BUY | vol 30,811 / OI 988
- **MU** PUT 815 2026-11-13 (2DTE): 100 @ 15.36 = **+$154k** SELL | vol 3,029 / OI 225
- **QQQ** PUT 689 2026-11-12 (1DTE): 883 @ 1.54 = **+$136k** SELL | vol 7,007 / OI 32
- **AMZN** CALL 270 2026-11-16 (5DTE): 500 @ 2.60 = **+$130k** BUY | vol 2,284 / OI 443
- **AMD** CALL 570 2026-11-13 (2DTE): 106 @ 12.20 = **+$129k** BUY | vol 3,589 / OI 870
- **AVGO** PUT 355 2026-11-13 (2DTE): 150 @ 7.45 = **+$112k** MID | vol 584 / OI 281
- **QQQ** CALL 693 2026-11-11 (0DTE): 500 @ 2.22 = **+$111k** BUY | vol 227,715 / OI 759
- **AVGO** PUT 355 2026-11-13 (2DTE): 149 @ 7.27 = **+$108k** SELL | vol 584 / OI 281
- **AMZN** CALL 270 2026-11-16 (5DTE): 412 @ 2.51 = **+$103k** BUY | vol 2,284 / OI 443
- **PLTR** CALL 175 2026-11-13 (2DTE): 465 @ 2.11 = **+$98k** SELL | vol 14,270 / OI 5,598
- **PLTR** CALL 175 2026-11-13 (2DTE): 465 @ 2.11 = **+$98k** SELL | vol 14,270 / OI 5,598

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 705 2026-11-12 (1DTE): 1,319 traded vs OI 430
- **SPY** PUT 704 2026-11-12 (1DTE): 620 traded vs OI 574
- **SPY** CALL 791 2026-11-16 (5DTE): 562 traded vs OI 292
- **SPY** CALL 763 2026-11-17 (6DTE): 511 traded vs OI 111
- **SPY** CALL 773 2026-11-20 (9DTE): 4,678 traded vs OI 4,332
- **SPY** CALL 783 2026-11-20 (9DTE): 3,614 traded vs OI 3,594
- **SPY** PUT 759 2026-12-04 (23DTE): 530 traded vs OI 394
- **SPY** CALL 770 2026-12-11 (30DTE): 1,268 traded vs OI 823
- **QQQ** PUT 699 2026-11-12 (1DTE): 554 traded vs OI 21
- **QQQ** PUT 677 2026-11-13 (2DTE): 1,622 traded vs OI 1,619
- **QQQ** PUT 636 2026-11-13 (2DTE): 558 traded vs OI 168
- **SMH** PUT 487.5 2026-11-13 (2DTE): 1,089 traded vs OI 246
- **SMH** PUT 507.5 2026-11-11 (0DTE): 663 traded vs OI 11
- **SMH** PUT 492.5 2026-11-11 (0DTE): 586 traded vs OI 129
- **SMH** PUT 512.5 2026-11-11 (0DTE): 598 traded vs OI 13

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
