# GEX + FLOW SCAN - Wed Nov 11, 01:00 PM ET
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
Last 1m check 13:00:08 ET, last candle SPY 12:59, QQQ 12:59 | no errors
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
| 1 | **MSFT** | 520.49 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 37 | none: 166 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (73 contracts' greeks worked out here) | POS +$78.6M | 515.34 | 535 | 520 | +$13.2M | +$164k bull / +$0 bear | out (clean 32, ADX 23, RVol 0.4) |
| 2 | **AAPL** | 354.61 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$1.9B | 341.79 | 355 | 355 | +$553k | +$0 bull / -$298k bear | out (clean 27, ADX 32, RVol 0.2) |
| 3 | **MU** | 822.70 | - | **-** | 28 | - | POS +$136.2M | - | 800 | 800 | -$223.8M | +$3.0M bull / -$436k bear | out (clean 34, ADX 61, RVol 0.4) |
| 4 | **AMD** | 559.68 | - | **-** | 27 | - | POS +$148.3M | - | 550 | 550 | -$93.0M | +$517k bull / -$2.5M bear | out (clean 34, ADX 51, RVol 0.4) |
| 5 | **DELL** | 382.63 | - | **-** | 27 | - | POS +$2.2M | - | 380 | 380 | -$3.5M | +$63k bull / +$0 bear | out (clean 37, ADX 64, RVol 0.4) |
| 6 | **SMCI** | 31.10 | - | **-** | 27 | - | POS +$12.7M | - | 32 | 30 | -$746k | +$39k bull / +$0 bear | out (clean 33, ADX 61, RVol 0.5) |
| 7 | **SMH** | 515.15 | - | **-** | 25 | - | NEG -$5.3M | - | 515 | 500 | -$4.8M | +$100k bull / +$0 bear | out (clean 32, ADX 54, RVol 0.4) |
| 8 | **SPY** | 761.18 | - | **-** | 24 | - | NEG -$509.9M | 761.82 | 760 | 750 | -$143.3M | +$104k bull / -$119k bear | out (clean 33, ADX 58, RVol 0.4) |
| 9 | **QQQ** | 694.06 | - | **-** | 24 | - | POS +$762.9M | 690.42 | 700 | 680 | -$168.8M | +$574k bull / -$166k bear | out (clean 33, ADX 55, RVol 0.5) |
| 10 | **HOOD** | 85.61 | - | **-** | 24 | - | POS +$15.9M | - | 85 | 85 | -$794k | +$35k bull / +$0 bear | out (clean 34, ADX 41, RVol 0.3) |
| 11 | **SHOP** | 149.54 | - | **-** | 23 | - | POS +$3.9M | 145.4 | 155 | 140 | -$479k | - | out (clean 33, ADX 38, RVol 0.2) |
| 12 | **AVGO** | 354.96 | - | **-** | 22 | - | POS +$91.9M | - | 350 | 350 | +$4.4M | +$30k bull / +$0 bear | out (clean 35, ADX 51, RVol 0.4) |
| 13 | **ORCL** | 130.28 | PINNED between the walls (positive gamma) - chop | **-** | 22 | - | POS +$5.6M | 124.21 | 130 | 130 | +$30k | - | out (clean 30, ADX 57, RVol 0.6) |
| 14 | **ARM** | 206.96 | - | **-** | 21 | - | POS +$5.6M | - | 200 | 200 | -$2.0M | - | out (clean 31, ADX 65, RVol 0.8) |
| 15 | **GOOGL** | 294.19 | - | **-** | 20 | - | POS +$99.7M | 289.05 | 300 | 290 | -$165k | +$56k bull / -$57k bear | out (clean 29, ADX 56, RVol 0.6) |
| 16 | **NVDA** | 176.50 | - | **-** | 19 | - | NEG -$131.9M | 183.13 | 180 | 175 | -$26.5M | +$1.2M bull / -$132k bear | out (clean 34, ADX 34, RVol 0.4) |
| 17 | **AMZN** | 265.90 | - | **-** | 19 | - | POS +$416.5M | - | 270 | 265 | +$4.8M | +$33k bull / +$0 bear | out (clean 32, ADX 21, RVol 0.5) |
| 18 | **TSLA** | 392.91 | - | **-** | 16 | - | POS +$413.3M | - | 400 | 380 | -$5.0M | +$428k bull / +$0 bear | out (clean 32, ADX 26, RVol 0.3) |
| 19 | **IWM** | 283.56 | - | **-** | 14 | - | POS +$269.8M | 282.96 | 285 | 270 | -$6.0M | - | out (clean 35, ADX 48, RVol 0.3) |
| 20 | **META** | 642.76 | - | **-** | 14 | - | POS +$310.9M | 627.81 | 650 | 635 | -$1.1M | +$55k bull / -$59k bear | out (clean 31, ADX 14, RVol 0.3) |
| 21 | **BABA** | 101.57 | - | **-** | 13 | - | NEG -$16.5M | 106.61 | 110 | 101 | +$348k | - | out (clean 30, ADX 19, RVol 0.2) |
| 22 | **PLTR** | 173.11 | - | **-** | 12 | - | POS +$77.7M | - | 170 | 180 | +$1.8M | - | out (clean 29, ADX 32, RVol 0.2) |
| 23 | **NFLX** | 63.91 | - | **-** | 11 | - | NEG -$6.1M | 64.4 | 65 | 65 | -$209k | - | out (clean 27, ADX 32, RVol 0.8) |
| 24 | **COIN** | 138.55 | - | **-** | 9 | - | POS +$27.7M | - | 141 | 135 | -$208k | - | out (clean 29, ADX 32, RVol 0.9) |
| 25 | **CRM** | 217.20 | - | **-** | 9 | - | NEG -$10.9M | - | 230 | 220 | -$40k | - | out (clean 29, ADX 26, RVol 0.4) |
| 26 | **MSTR** | 123.16 | - | **-** | 8 | - | POS +$2.6M | 122.23 | 133 | 120 | +$561k | - | out (clean 28, ADX 27, RVol 1.1) |
| 27 | **UBER** | 70.51 | - | **-** | 8 | - | POS +$18.6M | 68.35 | 70 | 70 | +$3k | - | out (clean 32, ADX 41, RVol 0.4) |

## Big prints this scan (70)
- **SPY** PUT 780 2026-11-16 (5DTE): 130 @ 18.66 = **+$243k** MID | vol 1,360 / OI 3
- **AMD** CALL 555 2026-11-11 (0DTE): 281 @ 6.84 = **+$192k** BUY | vol 29,517 / OI 266
- **AMD** PUT 555 2026-11-11 (0DTE): 974 @ 1.86 = **+$181k** BUY | vol 10,339 / OI 0
- **MU** PUT 805 2026-11-16 (5DTE): 96 @ 18.05 = **+$173k** SELL | vol 352 / OI 51
- **NVDA** PUT 177.5 2026-11-13 (2DTE): 297 @ 3.90 = **+$116k** SELL | vol 8,198 / OI 4,898
- **SPY** CALL 740 2026-11-13 (2DTE): 50 @ 21.85 = **+$109k** MID | vol 641 / OI 3,390
- **AMD** CALL 540 2026-11-13 (2DTE): 41 @ 26.05 = **+$107k** SELL | vol 4,600 / OI 1,314
- **SPY** PUT 780 2026-11-16 (5DTE): 56 @ 18.60 = **+$104k** MID | vol 1,360 / OI 3
- **SPY** PUT 780 2026-11-16 (5DTE): 56 @ 18.60 = **+$104k** MID | vol 1,360 / OI 3
- **SPY** CALL 760 2026-11-11 (0DTE): 625 @ 1.66 = **+$104k** BUY | vol 506,374 / OI 3,774
- **SPY** PUT 780 2026-11-16 (5DTE): 55 @ 18.66 = **+$103k** MID | vol 1,360 / OI 3
- **MU** CALL 800 2026-11-11 (0DTE): 41 @ 24.00 = **+$98k** BUY | vol 51,657 / OI 2,486
- **AMD** CALL 537.5 2026-11-13 (2DTE): 30 @ 28.40 = **+$85k** BUY | vol 1,196 / OI 199
- **MU** CALL 820 2026-11-13 (2DTE): 37 @ 23.00 = **+$85k** BUY | vol 5,660 / OI 1,308
- **AMD** CALL 560 2026-11-13 (2DTE): 60 @ 13.74 = **+$82k** SELL | vol 4,021 / OI 1,480

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 791 2026-11-13 (2DTE): 2,248 traded vs OI 1,988
- **SPY** PUT 717 2026-11-12 (1DTE): 552 traded vs OI 493
- **SPY** PUT 737 2026-11-12 (1DTE): 516 traded vs OI 506
- **SPY** CALL 765 2026-11-17 (6DTE): 570 traded vs OI 568
- **QQQ** PUT 700 2026-11-12 (1DTE): 598 traded vs OI 539
- **QQQ** CALL 721 2026-11-17 (6DTE): 536 traded vs OI 277
- **QQQ** PUT 625 2026-11-18 (7DTE): 2,450 traded vs OI 252
- **QQQ** CALL 696 2026-11-20 (9DTE): 3,177 traded vs OI 3,161
- **SMH** PUT 510 2026-11-11 (0DTE): 510 traded vs OI 18
- **NVDA** CALL 185 2026-11-20 (9DTE): 10,526 traded vs OI 10,083
- **TSLA** CALL 415 2026-11-18 (7DTE): 501 traded vs OI 112
- **AMD** CALL 562.5 2026-11-13 (2DTE): 503 traded vs OI 273
- **AMD** CALL 605 2026-11-13 (2DTE): 516 traded vs OI 0
- **AMD** PUT 555 2026-11-13 (2DTE): 507 traded vs OI 95
- **AMD** CALL 575 2026-11-20 (9DTE): 964 traded vs OI 960

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
