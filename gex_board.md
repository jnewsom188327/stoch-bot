# GEX + FLOW SCAN - Wed Nov 11, 02:10 PM ET
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
Last 1m check 14:10:08 ET, last candle SPY 14:09, QQQ 14:09 | no errors
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
| 1 | **META** | 635.64 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 37 | none: 204 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (81 contracts' greeks worked out here) | POS +$185.5M | 627.1 | 650 | 635 | +$3.3M | +$372k bull / +$0 bear | out (clean 30, ADX 30, RVol 0.7) |
| 2 | **MSFT** | 520.65 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | 11/11 522.5C @ 0.42 (delta 0.25) = est +46% at 522.55 | POS +$52.6M | 516.82 | 535 | 520 | +$13.2M | +$131k bull / +$0 bear | out (clean 32, ADX 14, RVol 0.3) |
| 3 | **AVGO** | 350.84 | PINNED between the walls (positive gamma) - chop | **-** | 32 | - | POS +$99.8M | - | 350 | 350 | +$6.1M | +$159k bull / +$0 bear | out (clean 35, ADX 24, RVol 0.6) |
| 4 | **AMD** | 562.07 | - | **-** | 28 | - | POS +$141.6M | - | 550 | 550 | -$109.6M | +$2.3M bull / -$2.1M bear | out (clean 34, ADX 59, RVol 0.9) |
| 5 | **DELL** | 380.91 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$2.2M | - | 380 | 380 | -$3.9M | - | out (clean 37, ADX 48, RVol 0.3) |
| 6 | **MU** | 818.83 | - | **-** | 27 | - | POS +$123.9M | - | 800 | 800 | -$219.2M | +$3.2M bull / -$925k bear | out (clean 33, ADX 44, RVol 0.4) |
| 7 | **IWM** | 283.06 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 26 | none: 340 puts 0-7DTE > 15 priced 0.40-0.80 > 6 delta 0.2+ > 6 spread ok > 6 liquid > best one only +6% at the target (needs +20%) (149 contracts' greeks worked out here) | POS +$103.4M | 282.78 | 283 | 270 | -$5.5M | - | out (clean 35, ADX 30, RVol 0.1) |
| 8 | **SPY** | 760.50 | - | **-** | 23 | - | NEG -$1.1B | 761.6 | 760 | 750 | -$154.5M | +$657k bull / +$0 bear | out (clean 33, ADX 46, RVol 0.3) |
| 9 | **QQQ** | 692.78 | - | **-** | 23 | - | POS +$534.5M | 690.24 | 700 | 680 | -$179.1M | +$1.7M bull / -$115k bear | out (clean 32, ADX 40, RVol 0.6) |
| 10 | **SMH** | 512.42 | - | **-** | 22 | - | NEG -$19.4M | - | 500 | 500 | -$4.3M | +$459k bull / -$125k bear | out (clean 31, ADX 40, RVol 0.3) |
| 11 | **PLTR** | 173.22 | - | **-** | 21 | - | POS +$80.4M | - | 170 | 170 | +$1.5M | +$0 bull / -$232k bear | out (clean 29, ADX 36, RVol 0.2) |
| 12 | **NVDA** | 176.09 | - | **-** | 19 | - | NEG -$152.4M | - | 180 | 175 | -$28.6M | +$1.5M bull / -$30k bear | out (clean 34, ADX 30, RVol 0.4) |
| 13 | **ARM** | 205.40 | - | **-** | 19 | - | POS +$5.3M | - | 200 | 200 | -$1.8M | - | out (clean 31, ADX 43, RVol 0.5) |
| 14 | **SHOP** | 148.91 | - | **-** | 19 | - | POS +$3.3M | 145.48 | 150 | 140 | -$459k | - | out (clean 33, ADX 20, RVol 0.3) |
| 15 | **AAPL** | 354.69 | PINNED between the walls (positive gamma) - chop | **-** | 18 | - | POS +$2.3B | 341.17 | 355 | 355 | -$171k | - | out (clean 28, ADX 34, RVol 0.3) |
| 16 | **AMZN** | 266.00 | - | **-** | 18 | - | POS +$390.2M | - | 270 | 265 | +$5.9M | +$376k bull / +$0 bear | out (clean 31, ADX 16, RVol 0.5) |
| 17 | **ORCL** | 129.01 | - | **-** | 18 | - | POS +$3.9M | 125.05 | 130 | 125 | +$262k | +$0 bull / -$27k bear | out (clean 30, ADX 38, RVol 0.4) |
| 18 | **MSTR** | 122.05 | FLIP CROSS down into negative gamma | **PUTS** | 17 | none: 25 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | NEG -$7.1M | 123.6 | 133 | 120 | +$1.2M | - | out (clean 28, ADX 16, RVol 0.3) |
| 19 | **TSLA** | 392.89 | - | **-** | 15 | - | POS +$438.8M | - | 400 | 380 | -$6.1M | +$437k bull / -$264k bear | out (clean 32, ADX 22, RVol 0.3) |
| 20 | **SMCI** | 30.70 | - | **-** | 13 | - | POS +$12.8M | - | 30 | 30 | -$640k | - | out (clean 32, ADX 33, RVol 0.5) |
| 21 | **BABA** | 101.52 | - | **-** | 13 | - | NEG -$16.9M | 106.77 | 110 | 101 | +$363k | - | out (clean 30, ADX 17, RVol 0.3) |
| 22 | **HOOD** | 85.42 | - | **-** | 12 | - | POS +$15.5M | - | 85 | 85 | -$856k | - | out (clean 34, ADX 36, RVol 0.3) |
| 23 | **GOOGL** | 293.75 | - | **-** | 9 | - | POS +$93.5M | 290.13 | 300 | 290 | -$161k | - | out (clean 29, ADX 53, RVol 0.4) |
| 24 | **UBER** | 70.86 | - | **-** | 9 | - | POS +$20.1M | 68.34 | 70 | 70 | -$7k | - | out (clean 32, ADX 50, RVol 0.6) |
| 25 | **NFLX** | 63.94 | - | **-** | 8 | - | NEG -$7.2M | 64.49 | 65 | 65 | -$219k | - | out (clean 27, ADX 20, RVol 0.8) |
| 26 | **CRM** | 217.76 | - | **-** | 7 | - | NEG -$11.4M | - | 230 | 220 | -$54k | - | out (clean 29, ADX 15, RVol 0.3) |
| 27 | **COIN** | 137.60 | - | **-** | 5 | - | POS +$24.8M | - | 141 | 135 | +$97k | - | out (clean 28, ADX 22, RVol 0.3) |

## Big prints this scan (45)
- **AMD** PUT 570 2026-11-11 (0DTE): 500 @ 5.00 = **+$250k** SELL | vol 2,453 / OI 11
- **AMD** PUT 570 2026-11-11 (0DTE): 492 @ 5.05 = **+$248k** SELL | vol 2,453 / OI 11
- **QQQ** CALL 684 2026-11-17 (6DTE): 150 @ 15.62 = **+$234k** BUY | vol 235 / OI 321
- **QQQ** CALL 685 2026-11-17 (6DTE): 150 @ 14.86 = **+$223k** BUY | vol 340 / OI 386
- **QQQ** CALL 681 2026-11-12 (1DTE): 150 @ 14.84 = **+$223k** BUY | vol 971 / OI 345
- **QQQ** CALL 682 2026-11-12 (1DTE): 150 @ 13.90 = **+$208k** BUY | vol 753 / OI 304
- **QQQ** CALL 694 2026-11-11 (0DTE): 1,000 @ 1.62 = **+$162k** BUY | vol 266,200 / OI 797
- **META** CALL 610 2026-11-13 (2DTE): 50 @ 30.33 = **+$152k** BUY | vol 117 / OI 357
- **META** CALL 612.5 2026-11-13 (2DTE): 50 @ 28.07 = **+$140k** BUY | vol 54 / OI 89
- **QQQ** PUT 700 2026-11-12 (1DTE): 200 @ 6.27 = **+$125k** SELL | vol 1,156 / OI 539
- **NVDA** CALL 175 2026-11-11 (0DTE): 439 @ 2.24 = **+$98k** BUY | vol 291,147 / OI 3,333
- **NVDA** CALL 175 2026-11-11 (0DTE): 439 @ 2.24 = **+$98k** BUY | vol 291,147 / OI 3,333
- **TSLA** CALL 380 2026-11-11 (0DTE): 58 @ 14.55 = **+$84k** BUY | vol 4,223 / OI 2,178
- **TSLA** PUT 390 2026-11-16 (5DTE): 150 @ 5.00 = **+$75k** SELL | vol 1,140 / OI 177
- **NVDA** PUT 175 2026-11-18 (7DTE): 100 @ 7.08 = **+$71k** SELL | vol 1,647 / OI 1,849

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 766 2026-11-16 (5DTE): 612 traded vs OI 607
- **SPY** PUT 762 2026-11-16 (5DTE): 500 traded vs OI 152
- **SPY** PUT 746 2026-11-16 (5DTE): 500 traded vs OI 259
- **SPY** PUT 738 2026-11-19 (8DTE): 563 traded vs OI 114
- **SPY** CALL 765 2026-12-11 (30DTE): 634 traded vs OI 394
- **SPY** CALL 801 2026-12-11 (30DTE): 550 traded vs OI 248
- **NVDA** CALL 192.5 2026-11-27 (16DTE): 509 traded vs OI 0
- **TSLA** PUT 395 2026-11-16 (5DTE): 504 traded vs OI 47
- **AMD** PUT 522.5 2026-11-13 (2DTE): 578 traded vs OI 60
- **AMD** PUT 565 2026-11-13 (2DTE): 556 traded vs OI 21
- **GOOGL** CALL 300 2026-11-18 (7DTE): 503 traded vs OI 371
- **SMCI** CALL 32 2026-11-27 (16DTE): 833 traded vs OI 712
- **MU** CALL 750 2026-11-16 (5DTE): 1,009 traded vs OI 482
- **MSTR** CALL 128 2026-11-13 (2DTE): 787 traded vs OI 760
- **MSTR** PUT 120 2026-12-11 (30DTE): 501 traded vs OI 43

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
