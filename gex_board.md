# GEX + FLOW SCAN - Wed Nov 11, 12:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (12)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:40 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 522.5C | 0.73 | 0.97 | +73% (34m) | **+33%** | +146% | 523.2 |
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
Last 1m check 12:20:08 ET, last candle SPY 12:19, QQQ 12:19 | no errors
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
| 1 | **DELL** | 381.22 | TREND (flow not with it) | **CALLS** | 45 | none: 30 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$2.2M | - | 380 | 380 | -$3.1M | +$57k bull / +$0 bear | LONG (clean 37, ADX 69, RVol 0.8) |
| 2 | **SHOP** | 149.62 | FLOW SURGE | **PUTS** | 44 | none: 21 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$4.4M | 144.86 | 155 | 140 | -$480k | +$0 bull / -$498k bear | out (clean 33, ADX 40, RVol 1.0) |
| 3 | **MU** | 822.70 | TREND (flow not with it) | **CALLS** | 43 | none: 141 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (61 contracts' greeks worked out here) | POS +$134.2M | - | 800 | 800 | -$217.6M | +$8.5M bull / -$96k bear | LONG (clean 34, ADX 67, RVol 0.6) |
| 4 | **MSFT** | 521.00 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 41 | none: 166 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (69 contracts' greeks worked out here) | POS +$52.0M | 516.16 | 535 | 520 | +$13.2M | +$0 bull / -$53k bear | out (clean 32, ADX 36, RVol 0.6) |
| 5 | **AAPL** | 354.63 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 36 | none: 113 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (59 contracts' greeks worked out here) | POS +$1.9B | 340.52 | 355 | 350 | -$1.2M | +$225k bull / -$91k bear | out (clean 27, ADX 41, RVol 0.5) |
| 6 | **SMCI** | 30.94 | - | **-** | 32 | - | POS +$12.4M | - | 30 | 30 | -$858k | +$36k bull / +$0 bear | out (clean 32, ADX 66, RVol 1.1) |
| 7 | **ARM** | 206.03 | - | **-** | 32 | - | POS +$5.4M | - | 200 | 200 | -$2.0M | +$37k bull / +$0 bear | out (clean 31, ADX 73, RVol 0.9) |
| 8 | **SMH** | 514.49 | - | **-** | 26 | - | NEG -$25.8M | - | 500 | 500 | -$4.4M | +$932k bull / +$0 bear | out (clean 31, ADX 55, RVol 0.6) |
| 9 | **AMD** | 555.36 | - | **-** | 26 | - | POS +$145.7M | - | 550 | 500 | -$72.5M | +$4.2M bull / -$109k bear | out (clean 34, ADX 47, RVol 0.2) |
| 10 | **QQQ** | 693.76 | - | **-** | 25 | - | POS +$693.7M | 690.37 | 700 | 680 | -$162.2M | +$492k bull / -$764k bear | out (clean 33, ADX 56, RVol 0.6) |
| 11 | **SPY** | 760.53 | - | **-** | 24 | - | NEG -$998.6M | 761.8 | 760 | 750 | -$116.2M | +$0 bull / -$4.6M bear | out (clean 32, ADX 55, RVol 0.5) |
| 12 | **IWM** | 283.10 | - | **-** | 22 | - | POS +$85.0M | 282.94 | 285 | 270 | -$4.4M | +$0 bull / -$110k bear | out (clean 34, ADX 42, RVol 0.3) |
| 13 | **AVGO** | 355.27 | - | **-** | 22 | - | POS +$95.6M | - | 350 | 350 | +$5.2M | +$1.0M bull / -$312k bear | out (clean 34, ADX 53, RVol 0.5) |
| 14 | **NVDA** | 176.55 | - | **-** | 21 | - | NEG -$130.9M | 183.63 | 180 | 175 | -$29.8M | +$269k bull / -$3.3M bear | out (clean 34, ADX 34, RVol 0.6) |
| 15 | **ORCL** | 129.56 | - | **-** | 21 | - | POS +$4.6M | 123.86 | 130 | 125 | -$763k | +$0 bull / -$52k bear | out (clean 29, ADX 51, RVol 0.5) |
| 16 | **GOOGL** | 293.36 | - | **-** | 20 | - | POS +$88.3M | 289.36 | 300 | 290 | +$85k | +$345k bull / +$0 bear | out (clean 28, ADX 54, RVol 0.7) |
| 17 | **MSTR** | 123.57 | - | **-** | 18 | - | POS +$2.9M | 122.17 | 133 | 120 | +$505k | +$28k bull / -$81k bear | out (clean 28, ADX 27, RVol 0.8) |
| 18 | **TSLA** | 392.74 | - | **-** | 17 | - | POS +$433.0M | - | 400 | 380 | -$2.4M | +$485k bull / -$79k bear | out (clean 33, ADX 36, RVol 0.4) |
| 19 | **AMZN** | 266.69 | - | **-** | 17 | - | POS +$424.0M | - | 270 | 265 | +$3.6M | +$52k bull / +$0 bear | out (clean 32, ADX 18, RVol 0.3) |
| 20 | **BABA** | 101.73 | - | **-** | 16 | - | NEG -$16.4M | 106.65 | 110 | 101 | +$350k | - | out (clean 30, ADX 29, RVol 0.3) |
| 21 | **HOOD** | 85.26 | - | **-** | 14 | - | POS +$15.5M | - | 85 | 85 | -$764k | - | out (clean 33, ADX 35, RVol 0.4) |
| 22 | **META** | 641.27 | - | **-** | 12 | - | POS +$309.0M | 625.26 | 650 | 635 | -$378k | +$121k bull / -$28k bear | out (clean 31, ADX 10, RVol 0.1) |
| 23 | **PLTR** | 173.15 | - | **-** | 12 | - | POS +$74.7M | - | 170 | 180 | +$1.7M | - | out (clean 29, ADX 31, RVol 0.3) |
| 24 | **CRM** | 217.75 | - | **-** | 11 | - | NEG -$10.9M | - | 230 | 220 | -$49k | - | out (clean 30, ADX 32, RVol 0.3) |
| 25 | **NFLX** | 64.12 | - | **-** | 10 | - | NEG -$5.3M | 64.52 | 65 | 65 | -$175k | - | out (clean 26, ADX 29, RVol 0.6) |
| 26 | **UBER** | 70.56 | - | **-** | 8 | - | POS +$18.7M | 68.29 | 70 | 70 | +$13k | - | out (clean 32, ADX 34, RVol 0.6) |
| 27 | **COIN** | 138.29 | - | **-** | 6 | - | POS +$26.1M | - | 141 | 135 | -$1k | - | out (clean 29, ADX 32, RVol 0.2) |

## Big prints this scan (95)
- **QQQ** CALL 690 2026-11-11 (0DTE): 501 @ 4.05 = **+$203k** SELL | vol 240,646 / OI 2,827
- **AVGO** PUT 352.5 2026-11-16 (5DTE): 301 @ 6.55 = **+$197k** SELL | vol 1,065 / OI 2
- **QQQ** CALL 691 2026-11-11 (0DTE): 499 @ 3.24 = **+$162k** BUY | vol 143,701 / OI 789
- **AVGO** PUT 345 2026-11-16 (5DTE): 415 @ 3.80 = **+$158k** SELL | vol 2,270 / OI 28
- **NVDA** CALL 177.5 2026-11-13 (2DTE): 500 @ 3.07 = **+$154k** SELL | vol 29,889 / OI 4,621
- **AVGO** PUT 345 2026-11-16 (5DTE): 318 @ 3.80 = **+$121k** SELL | vol 2,270 / OI 28
- **NVDA** CALL 172.5 2026-11-13 (2DTE): 200 @ 6.00 = **+$120k** SELL | vol 16,451 / OI 1,001
- **MU** CALL 840 2026-11-13 (2DTE): 81 @ 13.89 = **+$113k** MID | vol 2,623 / OI 1,388
- **AMD** PUT 530 2026-11-13 (2DTE): 232 @ 4.60 = **+$107k** SELL | vol 3,097 / OI 425
- **NVDA** CALL 175 2026-11-11 (0DTE): 500 @ 2.04 = **+$102k** SELL | vol 252,864 / OI 3,333
- **MU** CALL 800 2026-11-16 (5DTE): 25 @ 39.74 = **+$99k** MID | vol 1,829 / OI 273
- **GOOGL** CALL 295 2026-11-13 (2DTE): 353 @ 2.69 = **+$95k** BUY | vol 4,828 / OI 3,570
- **AVGO** PUT 352.5 2026-11-16 (5DTE): 135 @ 6.55 = **+$88k** SELL | vol 1,065 / OI 2
- **NVDA** CALL 175 2026-11-11 (0DTE): 458 @ 1.90 = **+$87k** SELL | vol 252,864 / OI 3,333
- **AVGO** PUT 352.5 2026-11-16 (5DTE): 121 @ 6.55 = **+$79k** SELL | vol 1,065 / OI 2

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 766 2026-11-11 (0DTE): 541 traded vs OI 9
- **SPY** CALL 761 2026-11-16 (5DTE): 665 traded vs OI 221
- **SPY** CALL 769 2026-11-13 (2DTE): 3,607 traded vs OI 3,476
- **SPY** PUT 742 2026-11-17 (6DTE): 1,013 traded vs OI 142
- **SPY** PUT 754 2026-11-19 (8DTE): 746 traded vs OI 29
- **SPY** PUT 756 2026-11-18 (7DTE): 504 traded vs OI 232
- **SPY** CALL 770 2026-11-27 (16DTE): 14,829 traded vs OI 2,178
- **SPY** CALL 788 2026-12-11 (30DTE): 2,603 traded vs OI 341
- **SPY** CALL 774 2026-12-11 (30DTE): 2,582 traded vs OI 157
- **QQQ** CALL 720 2026-11-16 (5DTE): 1,058 traded vs OI 341
- **QQQ** PUT 641 2026-11-20 (9DTE): 2,344 traded vs OI 823
- **IWM** CALL 286 2026-11-11 (0DTE): 4,999 traded vs OI 4,265
- **SMH** PUT 505 2026-11-11 (0DTE): 502 traded vs OI 11
- **AAPL** PUT 355 2026-11-20 (9DTE): 1,564 traded vs OI 1,519
- **AMD** CALL 560 2026-11-16 (5DTE): 518 traded vs OI 83

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
