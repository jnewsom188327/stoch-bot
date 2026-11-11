# GEX + FLOW SCAN - Wed Nov 11, 11:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (12)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:40 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 522.5C | 0.73 | 0.59 | +5% (1m) | **-19%** | +146% | 523.2 |
| 11:05 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.64 | 0.22 | +2% (1m) | **-66%** | +363% | 527.5 |
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
Last 1m check 11:50:08 ET, last candle SPY 11:49, QQQ 11:49 | no errors
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
| 1 | **MSFT** | 519.24 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 45 | none: 164 calls 0-7DTE > 7 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -22% at the target (needs +20%) (73 contracts' greeks worked out here) | POS +$45.9M | 514.56 | 535 | 520 | +$16.8M | +$204k bull / +$0 bear | out (clean 32, ADX 46, RVol 0.7) |
| 2 | **SMCI** | 31.00 | FLOW SURGE | **PUTS** | 42 | 11/13 30P @ 0.49 (delta 0.31) = est +24% at 30.54 | POS +$12.3M | - | 30 | 30 | -$862k | +$0 bull / -$117k bear | out (clean 32, ADX 70, RVol 1.1) |
| 3 | **SMH** | 513.91 | FLOW SURGE | **PUTS** | 41 | none: 164 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (69 contracts' greeks worked out here) | NEG -$27.6M | 505.39 | 500 | 500 | -$5.8M | +$0 bull / -$83k bear | out (clean 31, ADX 53, RVol 0.6) |
| 4 | **ARM** | 205.54 | FLOW SURGE | **PUTS** | 41 | none: 17 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$5.1M | - | 200 | 200 | -$1.9M | +$0 bull / -$73k bear | out (clean 30, ADX 74, RVol 0.8) |
| 5 | **DELL** | 381.68 | FLOW SURGE | **PUTS** | 39 | none: 30 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$2.4M | - | 380 | 380 | -$3.6M | +$0 bull / -$37k bear | LONG (clean 36, ADX 70, RVol 0.6) |
| 6 | **MU** | 825.51 | FLOW SURGE | **PUTS** | 38 | none: 142 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (58 contracts' greeks worked out here) | POS +$132.5M | - | 800 | 800 | -$233.4M | +$35k bull / -$5.5M bear | LONG (clean 33, ADX 71, RVol 0.5) |
| 7 | **AMD** | 553.73 | - | **-** | 27 | - | POS +$142.9M | - | 550 | 500 | -$75.2M | +$1.3M bull / -$773k bear | out (clean 33, ADX 48, RVol 0.4) |
| 8 | **QQQ** | 692.92 | - | **-** | 25 | - | POS +$571.2M | 690.22 | 700 | 680 | -$145.5M | +$0 bull / -$1.8M bear | out (clean 32, ADX 56, RVol 0.5) |
| 9 | **PLTR** | 172.54 | - | **-** | 24 | - | POS +$75.9M | - | 170 | 170 | +$1.8M | +$333k bull / +$0 bear | out (clean 29, ADX 37, RVol 0.3) |
| 10 | **SPY** | 759.62 | - | **-** | 23 | - | NEG -$1.6B | 761.5 | 760 | 750 | -$80.1M | +$0 bull / -$1.3M bear | out (clean 32, ADX 52, RVol 0.4) |
| 11 | **AVGO** | 354.46 | - | **-** | 23 | - | POS +$94.2M | - | 350 | 350 | +$5.1M | +$0 bull / -$145k bear | out (clean 34, ADX 52, RVol 0.5) |
| 12 | **IWM** | 282.79 | - | **-** | 22 | - | POS +$1.0M | 282.83 | 285 | 270 | -$3.5M | +$106k bull / +$0 bear | out (clean 35, ADX 44, RVol 0.3) |
| 13 | **GOOGL** | 292.82 | - | **-** | 21 | - | POS +$67.6M | 290.28 | 300 | 290 | -$546k | +$0 bull / -$40k bear | out (clean 28, ADX 53, RVol 0.8) |
| 14 | **ORCL** | 128.57 | - | **-** | 21 | - | POS +$3.6M | 123.79 | 130 | 125 | -$490k | +$154k bull / +$0 bear | out (clean 29, ADX 51, RVol 0.5) |
| 15 | **UBER** | 69.91 | PINNED between the walls (positive gamma) - chop | **-** | 21 | - | POS +$12.9M | 68.46 | 70 | 70 | +$30k | - | out (clean 31, ADX 22, RVol 0.6) |
| 16 | **NVDA** | 175.83 | - | **-** | 20 | - | NEG -$148.6M | 181.62 | 180 | 175 | -$18.7M | +$2.4M bull / -$1.7M bear | out (clean 34, ADX 32, RVol 0.8) |
| 17 | **TSLA** | 393.06 | - | **-** | 19 | - | POS +$429.0M | - | 400 | 380 | -$2.9M | +$763k bull / -$675k bear | out (clean 32, ADX 46, RVol 0.3) |
| 18 | **AAPL** | 354.01 | - | **-** | 19 | - | POS +$1.6B | 341.88 | 355 | 350 | -$1.2M | +$0 bull / -$38k bear | out (clean 27, ADX 40, RVol 0.4) |
| 19 | **MSTR** | 122.87 | - | **-** | 19 | - | POS +$1.6M | 122.2 | 133 | 120 | +$485k | +$163k bull / +$0 bear | out (clean 28, ADX 28, RVol 1.3) |
| 20 | **AMZN** | 266.78 | - | **-** | 18 | - | POS +$420.0M | - | 270 | 265 | +$3.2M | +$0 bull / -$37k bear | out (clean 32, ADX 24, RVol 0.5) |
| 21 | **BABA** | 101.45 | - | **-** | 18 | - | NEG -$16.9M | 106.38 | 110 | 101 | +$370k | - | out (clean 29, ADX 39, RVol 0.3) |
| 22 | **HOOD** | 84.78 | - | **-** | 14 | - | POS +$15.2M | - | 85 | 85 | -$687k | - | out (clean 33, ADX 35, RVol 0.8) |
| 23 | **META** | 641.20 | - | **-** | 13 | - | POS +$297.4M | 627.2 | 650 | 635 | -$296k | +$678k bull / +$0 bear | out (clean 31, ADX 14, RVol 0.3) |
| 24 | **SHOP** | 149.11 | - | **-** | 13 | - | POS +$3.3M | 145.2 | 150 | 140 | +$26k | - | out (clean 33, ADX 38, RVol 0.5) |
| 25 | **CRM** | 217.94 | - | **-** | 12 | - | NEG -$11.1M | - | 230 | 220 | -$47k | - | out (clean 30, ADX 34, RVol 0.8) |
| 26 | **COIN** | 137.02 | - | **-** | 7 | - | POS +$25.1M | - | 141 | 135 | -$8k | - | out (clean 29, ADX 34, RVol 0.4) |
| 27 | **NFLX** | 63.69 | - | **-** | 5 | - | NEG -$11.6M | 64.47 | 65 | 65 | -$27k | - | out (clean 26, ADX 18, RVol 0.6) |

## Big prints this scan (105)
- **NVDA** PUT 175 2026-11-13 (2DTE): 1,254 @ 2.83 = **+$355k** SELL | vol 22,112 / OI 10,522
- **NVDA** PUT 175 2026-11-13 (2DTE): 1,000 @ 2.83 = **+$283k** SELL | vol 22,112 / OI 10,522
- **QQQ** CALL 683 2026-11-11 (0DTE): 300 @ 8.95 = **+$268k** SELL | vol 7,351 / OI 989
- **MU** CALL 795 2026-11-11 (0DTE): 101 @ 25.00 = **+$252k** SELL | vol 12,128 / OI 466
- **QQQ** CALL 685 2026-11-11 (0DTE): 300 @ 7.10 = **+$213k** SELL | vol 65,219 / OI 1,366
- **TSLA** CALL 385 2026-11-13 (2DTE): 198 @ 10.60 = **+$210k** SELL | vol 3,008 / OI 3,249
- **MU** CALL 815 2026-11-11 (0DTE): 200 @ 10.20 = **+$204k** SELL | vol 27,041 / OI 988
- **QQQ** CALL 690 2026-11-13 (2DTE): 300 @ 6.35 = **+$190k** SELL | vol 16,663 / OI 8,488
- **TSLA** CALL 385 2026-11-11 (0DTE): 198 @ 7.95 = **+$157k** SELL | vol 10,238 / OI 2,160
- **QQQ** CALL 687 2026-11-11 (0DTE): 300 @ 5.11 = **+$153k** SELL | vol 102,286 / OI 753
- **NVDA** PUT 175 2026-11-13 (2DTE): 441 @ 2.83 = **+$125k** SELL | vol 22,112 / OI 10,522
- **NVDA** PUT 175 2026-11-13 (2DTE): 438 @ 2.83 = **+$124k** SELL | vol 22,112 / OI 10,522
- **TSLA** PUT 402.5 2026-11-11 (0DTE): 120 @ 10.25 = **+$123k** BUY | vol 502 / OI 121
- **SPY** PUT 761 2026-11-11 (0DTE): 500 @ 2.30 = **+$115k** BUY | vol 12,340 / OI 151
- **SPY** PUT 761 2026-11-11 (0DTE): 500 @ 2.27 = **+$114k** BUY | vol 12,340 / OI 151

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 755 2026-11-16 (5DTE): 1,434 traded vs OI 1,167
- **SPY** PUT 719 2026-11-13 (2DTE): 1,200 traded vs OI 1,028
- **SPY** PUT 718 2026-11-13 (2DTE): 1,293 traded vs OI 914
- **SPY** PUT 726 2026-11-12 (1DTE): 2,735 traded vs OI 642
- **SPY** CALL 760 2026-11-19 (8DTE): 533 traded vs OI 472
- **SPY** CALL 767 2026-12-04 (23DTE): 734 traded vs OI 675
- **SPY** CALL 755 2026-11-25 (14DTE): 527 traded vs OI 0
- **QQQ** PUT 660 2026-11-12 (1DTE): 1,388 traded vs OI 1,382
- **QQQ** CALL 704 2026-11-13 (2DTE): 787 traded vs OI 784
- **QQQ** PUT 730 2026-11-19 (8DTE): 822 traded vs OI 0
- **IWM** PUT 286 2026-11-13 (2DTE): 619 traded vs OI 106
- **SMH** PUT 495 2026-11-11 (0DTE): 500 traded vs OI 19
- **NVDA** CALL 187.5 2026-11-27 (16DTE): 527 traded vs OI 177
- **NVDA** PUT 192.5 2026-11-16 (5DTE): 532 traded vs OI 0
- **NVDA** CALL 165 2026-11-25 (14DTE): 2,548 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
