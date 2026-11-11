# GEX + FLOW SCAN - Wed Nov 11, 03:35 PM ET
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
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors
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
| 1 | **MSFT** | 519.97 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 39 | none: 162 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (80 contracts' greeks worked out here) | POS +$4.9M | 519.98 | 535 | 520 | +$15.5M | +$156k bull / +$0 bear | out (clean 32, ADX 21, RVol 0.7) |
| 2 | **META** | 634.76 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 38 | none: 204 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (83 contracts' greeks worked out here) | POS +$159.9M | 628.66 | 650 | 635 | +$6.6M | +$28k bull / +$0 bear | out (clean 30, ADX 44, RVol 0.4) |
| 3 | **SHOP** | 149.63 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 35 | none: 21 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$4.0M | 145.21 | 150 | 140 | -$477k | - | out (clean 32, ADX 13, RVol 0.5) |
| 4 | **AAPL** | 355.11 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$3.4B | 341.07 | 355 | 355 | -$1.2M | +$0 bull / -$218k bear | out (clean 28, ADX 22, RVol 0.5) |
| 5 | **IWM** | 283.17 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 25 | none: 340 puts 0-7DTE > 12 priced 0.40-0.80 > 3 delta 0.2+ > 3 spread ok > 3 liquid > best one only +0% at the target (needs +20%) (163 contracts' greeks worked out here) | POS +$276.6M | 282.7 | 283 | 270 | -$4.9M | - | out (clean 35, ADX 23, RVol 0.4) |
| 6 | **AVGO** | 346.78 | - | **-** | 24 | - | POS +$108.7M | - | 340 | 340 | +$10.1M | +$421k bull / +$0 bear | out (clean 37, ADX 43, RVol 0.9) |
| 7 | **AMD** | 555.76 | - | **-** | 22 | - | POS +$191.4M | - | 550 | 550 | -$89.8M | +$1.4M bull / -$249k bear | out (clean 35, ADX 30, RVol 0.5) |
| 8 | **MU** | 813.41 | - | **-** | 21 | - | POS +$166.7M | - | 800 | 850 | -$187.1M | +$5.8M bull / -$1.1M bear | out (clean 33, ADX 22, RVol 0.7) |
| 9 | **QQQ** | 691.21 | - | **-** | 20 | - | POS +$581.4M | 689.24 | 700 | 680 | -$125.2M | +$2.9M bull / +$0 bear | out (clean 33, ADX 32, RVol 0.5) |
| 10 | **SMH** | 508.31 | - | **-** | 19 | - | NEG -$36.4M | 514.29 | 500 | 500 | -$1.2M | +$443k bull / +$0 bear | out (clean 32, ADX 35, RVol 0.5) |
| 11 | **MSTR** | 121.05 | - | **-** | 19 | - | NEG -$9.6M | 123.65 | 133 | 120 | +$2.1M | +$28k bull / +$0 bear | out (clean 28, ADX 23, RVol 0.8) |
| 12 | **HOOD** | 85.18 | PINNED between the walls (positive gamma) - chop | **-** | 19 | - | POS +$17.5M | - | 85 | 85 | -$548k | - | out (clean 35, ADX 16, RVol 0.4) |
| 13 | **SPY** | 760.31 | - | **-** | 18 | - | NEG -$752.8M | 761.31 | 760 | 750 | -$121.2M | +$1.9M bull / -$129k bear | out (clean 34, ADX 26, RVol 0.3) |
| 14 | **NVDA** | 174.54 | - | **-** | 18 | - | NEG -$219.9M | 181.19 | 175 | 175 | -$19.0M | +$1.2M bull / -$61k bear | out (clean 34, ADX 33, RVol 0.5) |
| 15 | **PLTR** | 173.13 | - | **-** | 17 | - | POS +$75.0M | - | 170 | 180 | +$1.5M | +$0 bull / -$35k bear | out (clean 29, ADX 16, RVol 0.3) |
| 16 | **TSLA** | 391.33 | - | **-** | 16 | - | POS +$421.7M | - | 390 | 380 | -$2.1M | +$46k bull / -$583k bear | out (clean 32, ADX 26, RVol 0.4) |
| 17 | **AMZN** | 266.40 | - | **-** | 16 | - | POS +$435.6M | - | 270 | 265 | +$4.2M | +$0 bull / -$153k bear | out (clean 31, ADX 14, RVol 0.5) |
| 18 | **SMCI** | 30.36 | - | **-** | 13 | - | POS +$15.5M | - | 30 | 30 | -$568k | - | out (clean 34, ADX 37, RVol 0.4) |
| 19 | **ARM** | 203.46 | - | **-** | 13 | - | POS +$6.9M | - | 200 | 200 | -$1.7M | - | out (clean 32, ADX 21, RVol 0.5) |
| 20 | **BABA** | 101.67 | - | **-** | 13 | - | NEG -$16.8M | 106.6 | 110 | 101 | +$360k | - | out (clean 28, ADX 18, RVol 0.3) |
| 21 | **DELL** | 376.59 | - | **-** | 10 | - | NEG -$1.2M | - | 400 | 400 | -$2.1M | - | out (clean 38, ADX 32, RVol 0.5) |
| 22 | **NFLX** | 64.28 | - | **-** | 9 | - | NEG -$340k | 64.32 | 65 | 65 | -$270k | - | out (clean 27, ADX 27, RVol 0.7) |
| 23 | **UBER** | 70.88 | - | **-** | 8 | - | POS +$21.2M | 68.33 | 70 | 70 | -$29k | - | out (clean 32, ADX 24, RVol 1.2) |
| 24 | **COIN** | 136.73 | - | **-** | 7 | - | POS +$24.8M | - | 141 | 135 | +$73k | - | out (clean 29, ADX 28, RVol 0.7) |
| 25 | **CRM** | 217.89 | - | **-** | 7 | - | NEG -$10.8M | - | 230 | 220 | -$57k | - | out (clean 29, ADX 12, RVol 0.6) |
| 26 | **GOOGL** | 294.05 | - | **-** | 5 | - | POS +$108.4M | 289.43 | 300 | 290 | -$668k | - | out (clean 29, ADX 20, RVol 0.5) |
| 27 | **ORCL** | 128.79 | - | **-** | 5 | - | POS +$12.3M | 121.4 | 130 | 125 | +$543k | - | out (clean 30, ADX 16, RVol 0.5) |

## Big prints this scan (48)
- **QQQ** PUT 698 2026-11-11 (0DTE): 395 @ 6.54 = **+$258k** SELL | vol 7,343 / OI 115
- **NVDA** PUT 177.5 2026-11-13 (2DTE): 426 @ 4.60 = **+$196k** SELL | vol 16,871 / OI 4,898
- **QQQ** CALL 699 2026-11-13 (2DTE): 957 @ 2.04 = **+$195k** BUY | vol 6,760 / OI 656
- **TSLA** PUT 390 2026-11-13 (2DTE): 334 @ 4.75 = **+$159k** MID | vol 12,919 / OI 754
- **QQQ** PUT 698 2026-11-11 (0DTE): 225 @ 6.56 = **+$148k** SELL | vol 7,343 / OI 115
- **SMH** CALL 500 2026-11-13 (2DTE): 109 @ 13.45 = **+$147k** BUY | vol 2,910 / OI 4,456
- **QQQ** CALL 665 2026-11-13 (2DTE): 40 @ 27.34 = **+$109k** BUY | vol 222 / OI 2,537
- **AVGO** CALL 330 2026-11-13 (2DTE): 56 @ 18.78 = **+$105k** BUY | vol 1,200 / OI 4,173
- **MU** CALL 775 2026-11-11 (0DTE): 20 @ 40.45 = **+$81k** BUY | vol 5,913 / OI 627
- **MU** CALL 800 2026-11-11 (0DTE): 50 @ 15.80 = **+$79k** BUY | vol 54,013 / OI 2,486
- **MU** CALL 815 2026-11-13 (2DTE): 35 @ 21.25 = **+$74k** BUY | vol 3,820 / OI 280
- **MU** CALL 780 2026-11-11 (0DTE): 20 @ 35.81 = **+$72k** BUY | vol 15,456 / OI 2,052
- **MU** CALL 850 2026-11-13 (2DTE): 84 @ 7.70 = **+$65k** BUY | vol 12,972 / OI 2,705
- **MU** CALL 785 2026-11-11 (0DTE): 20 @ 30.81 = **+$62k** BUY | vol 10,040 / OI 277
- **MU** CALL 850 2026-11-13 (2DTE): 65 @ 7.85 = **+$51k** BUY | vol 12,972 / OI 2,705

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 728 2026-11-12 (1DTE): 537 traded vs OI 530
- **SPY** CALL 799 2026-11-18 (7DTE): 1,160 traded vs OI 61
- **SPY** CALL 800 2026-11-18 (7DTE): 1,287 traded vs OI 148
- **SPY** CALL 763 2026-12-11 (30DTE): 598 traded vs OI 374
- **QQQ** PUT 681 2026-11-13 (2DTE): 1,791 traded vs OI 1,778
- **QQQ** CALL 693 2026-11-16 (5DTE): 521 traded vs OI 193
- **SMH** PUT 457.5 2026-11-20 (9DTE): 560 traded vs OI 0
- **NVDA** PUT 162.5 2026-11-20 (9DTE): 762 traded vs OI 0
- **TSLA** CALL 390 2026-11-20 (9DTE): 3,628 traded vs OI 3,619
- **TSLA** CALL 417.5 2026-11-13 (2DTE): 818 traded vs OI 817
- **AMD** CALL 607.5 2026-11-13 (2DTE): 503 traded vs OI 258
- **AMD** CALL 580 2026-11-16 (5DTE): 504 traded vs OI 124
- **META** PUT 612.5 2026-11-13 (2DTE): 511 traded vs OI 399
- **META** PUT 620 2026-11-13 (2DTE): 1,301 traded vs OI 1,284
- **GOOGL** PUT 282.5 2026-11-13 (2DTE): 1,270 traded vs OI 1,267

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
