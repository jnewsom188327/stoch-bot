# GEX + FLOW SCAN - Wed Nov 11, 03:55 PM ET
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
| 1 | **AVGO** | 345.10 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 45 | none: 108 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (43 contracts' greeks worked out here) | POS +$196.0M | - | 345 | 340 | +$10.4M | +$46k bull / +$0 bear | out (clean 37, ADX 45, RVol 1.0) |
| 2 | **QQQ** | 689.93 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 40 | none: 709 puts 0-7DTE > 58 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -5% at the target (needs +20%) (208 contracts' greeks worked out here) | POS +$299.4M | 689.4 | 690 | 680 | -$112.8M | +$515k bull / +$0 bear | out (clean 33, ADX 34, RVol 0.9) |
| 3 | **MU** | 809.81 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 40 | none: 153 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (57 contracts' greeks worked out here) | POS +$109.3M | - | 810 | 850 | -$180.8M | +$5.0M bull / -$415k bear | out (clean 33, ADX 23, RVol 0.8) |
| 4 | **AAPL** | 355.40 | PINNED between the walls (positive gamma) - chop | **-** | 33 | - | POS +$2.4B | 341.57 | 355 | 355 | -$2.5M | +$0 bull / -$81k bear | out (clean 28, ADX 26, RVol 1.0) |
| 5 | **IWM** | 282.83 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 28 | none: 340 puts 0-7DTE > 15 priced 0.40-0.80 > 6 delta 0.2+ > 6 spread ok > 6 liquid > best one only +5% at the target (needs +20%) (175 contracts' greeks worked out here) | POS +$317.6M | 282.6 | 283 | 270 | -$4.7M | - | out (clean 35, ADX 20, RVol 0.8) |
| 6 | **META** | 631.22 | - | **-** | 23 | - | POS +$32.1M | 630.26 | 650 | 635 | +$8.5M | +$285k bull / +$0 bear | out (clean 30, ADX 46, RVol 0.7) |
| 7 | **AMD** | 551.95 | - | **-** | 22 | - | POS +$181.2M | - | 550 | 550 | -$87.7M | +$806k bull / -$152k bear | out (clean 36, ADX 28, RVol 0.6) |
| 8 | **SPY** | 759.45 | - | **-** | 20 | - | NEG -$1.7B | 761.77 | 760 | 750 | -$115.3M | +$352k bull / -$1.7M bear | out (clean 34, ADX 26, RVol 1.2) |
| 9 | **MSFT** | 520.21 | - | **-** | 20 | - | NEG -$139.8M | 520.57 | 535 | 520 | +$14.3M | +$0 bull / -$112k bear | out (clean 32, ADX 19, RVol 1.1) |
| 10 | **COIN** | 136.03 | - | **-** | 20 | - | POS +$22.1M | 128.46 | 141 | 135 | +$282k | +$163k bull / +$0 bear | out (clean 30, ADX 34, RVol 1.0) |
| 11 | **NVDA** | 174.02 | - | **-** | 19 | - | NEG -$202.5M | 183.79 | 175 | 175 | -$18.1M | +$902k bull / -$178k bear | out (clean 34, ADX 34, RVol 0.6) |
| 12 | **SHOP** | 149.20 | - | **-** | 19 | - | POS +$3.6M | 145.79 | 150 | 140 | -$478k | - | out (clean 32, ADX 13, RVol 1.0) |
| 13 | **SMH** | 506.70 | - | **-** | 18 | - | NEG -$62.8M | 526.63 | 500 | 500 | -$513k | +$118k bull / +$0 bear | out (clean 32, ADX 37, RVol 0.7) |
| 14 | **TSLA** | 388.92 | - | **-** | 17 | - | POS +$460.2M | - | 390 | 380 | +$4.4M | +$881k bull / +$0 bear | out (clean 32, ADX 30, RVol 0.7) |
| 15 | **AMZN** | 266.07 | - | **-** | 16 | - | POS +$363.1M | - | 270 | 265 | +$4.9M | +$53k bull / +$0 bear | out (clean 31, ADX 12, RVol 0.7) |
| 16 | **ORCL** | 127.99 | - | **-** | 16 | - | POS +$11.3M | 120.83 | 130 | 125 | +$808k | +$80k bull / +$0 bear | out (clean 30, ADX 15, RVol 0.9) |
| 17 | **GOOGL** | 293.59 | - | **-** | 15 | - | POS +$60.7M | 291.18 | 300 | 290 | -$546k | +$29k bull / -$26k bear | out (clean 29, ADX 18, RVol 0.6) |
| 18 | **ARM** | 202.73 | - | **-** | 14 | - | POS +$6.9M | - | 200 | 200 | -$1.7M | - | out (clean 32, ADX 19, RVol 1.1) |
| 19 | **SMCI** | 30.30 | - | **-** | 13 | - | POS +$15.8M | - | 30 | 30 | -$507k | - | out (clean 34, ADX 38, RVol 0.7) |
| 20 | **BABA** | 101.53 | - | **-** | 13 | - | NEG -$17.5M | 106.47 | 110 | 101 | +$367k | - | out (clean 28, ADX 16, RVol 0.7) |
| 21 | **DELL** | 374.52 | - | **-** | 12 | - | NEG -$1.3M | - | 400 | 400 | -$2.1M | - | out (clean 38, ADX 33, RVol 1.2) |
| 22 | **NFLX** | 64.44 | - | **-** | 11 | - | NEG -$58k | 64.47 | 65 | 65 | -$299k | - | out (clean 26, ADX 30, RVol 1.1) |
| 23 | **MSTR** | 121.36 | - | **-** | 10 | - | NEG -$8.0M | 123.64 | 133 | 120 | +$2.0M | - | out (clean 28, ADX 23, RVol 1.5) |
| 24 | **CRM** | 217.22 | - | **-** | 10 | - | NEG -$11.1M | - | 230 | 220 | -$57k | - | out (clean 29, ADX 15, RVol 1.5) |
| 25 | **UBER** | 70.73 | - | **-** | 9 | - | POS +$21.0M | 68.31 | 70 | 70 | -$30k | - | out (clean 31, ADX 21, RVol 2.1) |
| 26 | **HOOD** | 84.61 | - | **-** | 8 | - | POS +$17.2M | - | 85 | 85 | -$581k | - | out (clean 35, ADX 15, RVol 1.2) |
| 27 | **PLTR** | 172.46 | - | **-** | 7 | - | POS +$77.4M | - | 170 | 170 | +$1.5M | - | out (clean 29, ADX 15, RVol 0.5) |

## Big prints this scan (71)
- **AMD** PUT 550 2026-11-13 (2DTE): 250 @ 10.10 = **+$252k** SELL | vol 4,876 / OI 154
- **MU** PUT 815 2026-11-13 (2DTE): 100 @ 20.50 = **+$205k** SELL | vol 6,521 / OI 225
- **MU** PUT 815 2026-11-13 (2DTE): 100 @ 20.34 = **+$203k** SELL | vol 6,521 / OI 225
- **SPY** PUT 763 2026-11-11 (0DTE): 640 @ 2.66 = **+$170k** SELL | vol 87,909 / OI 2,103
- **TSLA** CALL 380 2026-11-13 (2DTE): 100 @ 12.70 = **+$127k** BUY | vol 5,458 / OI 8,112
- **NVDA** CALL 180 2026-11-18 (7DTE): 200 @ 5.70 = **+$114k** BUY | vol 9,618 / OI 2,150
- **SMH** CALL 500 2026-11-13 (2DTE): 70 @ 12.95 = **+$91k** BUY | vol 3,149 / OI 4,456
- **NVDA** CALL 175 2026-11-18 (7DTE): 100 @ 7.95 = **+$80k** BUY | vol 8,291 / OI 1,154
- **MU** CALL 820 2026-11-13 (2DTE): 41 @ 17.20 = **+$71k** BUY | vol 9,311 / OI 1,308
- **MU** PUT 800 2026-11-13 (2DTE): 47 @ 14.00 = **+$66k** SELL | vol 7,551 / OI 926
- **MU** PUT 815 2026-11-11 (0DTE): 193 @ 3.10 = **+$60k** SELL | vol 52,471 / OI 91
- **NVDA** PUT 180 2026-11-11 (0DTE): 110 @ 5.25 = **+$58k** SELL | vol 4,454 / OI 3,675
- **NVDA** CALL 182.5 2026-11-16 (5DTE): 448 @ 1.25 = **+$56k** BUY | vol 17,626 / OI 1,598
- **MU** PUT 815 2026-11-13 (2DTE): 25 @ 20.80 = **+$52k** SELL | vol 6,521 / OI 225
- **NVDA** CALL 182.5 2026-11-16 (5DTE): 400 @ 1.25 = **+$50k** BUY | vol 17,626 / OI 1,598

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 772 2026-11-17 (6DTE): 513 traded vs OI 473
- **SPY** PUT 721 2026-11-19 (8DTE): 501 traded vs OI 454
- **QQQ** PUT 647 2026-11-12 (1DTE): 797 traded vs OI 94
- **QQQ** PUT 698 2026-11-12 (1DTE): 503 traded vs OI 14
- **QQQ** CALL 691 2026-11-16 (5DTE): 512 traded vs OI 138
- **QQQ** CALL 712 2026-11-17 (6DTE): 651 traded vs OI 42
- **QQQ** CALL 716 2026-11-17 (6DTE): 1,518 traded vs OI 74
- **TSLA** PUT 405 2026-11-13 (2DTE): 650 traded vs OI 403
- **AAPL** CALL 365 2026-11-13 (2DTE): 11,423 traded vs OI 10,656
- **AMD** PUT 497.5 2026-11-11 (0DTE): 609 traded vs OI 0
- **META** CALL 657.5 2026-11-13 (2DTE): 538 traded vs OI 483
- **AMZN** CALL 277.5 2026-11-13 (2DTE): 3,256 traded vs OI 2,999
- **AMZN** PUT 275 2026-11-11 (0DTE): 509 traded vs OI 103
- **MU** CALL 730 2026-11-20 (9DTE): 540 traded vs OI 0
- **MU** PUT 730 2026-11-13 (2DTE): 2,753 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
