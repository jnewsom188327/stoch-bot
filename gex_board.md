# GEX + FLOW SCAN - Wed Nov 11, 12:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (12)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:40 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 522.5C | 0.73 | 1.01 | +73% (34m) | **+38%** | +146% | 523.2 |
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
Last 1m check 12:30:08 ET, last candle SPY 12:29, QQQ 12:29 | no errors
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
| 1 | **DELL** | 382.47 | TREND (flow not with it) | **CALLS** | 44 | none: 31 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$2.4M | - | 380 | 380 | -$3.5M | +$57k bull / -$40k bear | LONG (clean 37, ADX 68, RVol 0.7) |
| 2 | **MSFT** | 521.26 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 40 | none: 166 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (74 contracts' greeks worked out here) | POS +$44.5M | 517.17 | 535 | 520 | +$13.4M | +$52k bull / -$109k bear | out (clean 32, ADX 32, RVol 0.6) |
| 3 | **AAPL** | 354.30 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 35 | none: 109 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (56 contracts' greeks worked out here) | POS +$1.8B | 341.42 | 355 | 350 | +$259k | +$415k bull / -$61k bear | out (clean 27, ADX 38, RVol 0.5) |
| 4 | **ORCL** | 130.32 | PINNED between the walls (positive gamma) - chop | **-** | 35 | - | POS +$5.3M | 122.88 | 130 | 130 | -$590k | +$0 bull / -$25k bear | out (clean 29, ADX 53, RVol 0.7) |
| 5 | **MU** | 823.68 | - | **-** | 29 | - | POS +$143.2M | - | 800 | 800 | -$228.6M | +$670k bull / -$5.5M bear | out (clean 34, ADX 66, RVol 0.5) |
| 6 | **SMH** | 514.83 | - | **-** | 26 | - | NEG -$9.9M | - | 500 | 500 | -$4.9M | +$0 bull / -$27k bear | out (clean 32, ADX 56, RVol 0.6) |
| 7 | **AMD** | 556.53 | - | **-** | 26 | - | POS +$146.9M | - | 550 | 550 | -$76.1M | +$438k bull / -$1.7M bear | out (clean 34, ADX 48, RVol 0.3) |
| 8 | **QQQ** | 694.04 | - | **-** | 25 | - | POS +$728.2M | 690.44 | 700 | 680 | -$164.2M | +$162k bull / -$933k bear | out (clean 33, ADX 56, RVol 0.5) |
| 9 | **SHOP** | 149.86 | - | **-** | 25 | - | POS +$4.4M | 145.07 | 155 | 140 | -$480k | - | out (clean 33, ADX 41, RVol 1.0) |
| 10 | **SPY** | 760.69 | - | **-** | 24 | - | NEG -$951.9M | 761.77 | 760 | 750 | -$123.6M | +$0 bull / -$234k bear | out (clean 32, ADX 56, RVol 0.5) |
| 11 | **AVGO** | 355.39 | - | **-** | 22 | - | POS +$102.5M | - | 350 | 350 | +$4.4M | +$1.0M bull / -$495k bear | out (clean 34, ADX 53, RVol 0.5) |
| 12 | **SMCI** | 31.09 | - | **-** | 22 | - | POS +$12.3M | - | 30 | 30 | -$902k | - | out (clean 32, ADX 65, RVol 1.0) |
| 13 | **ARM** | 205.90 | - | **-** | 22 | - | POS +$5.6M | - | 200 | 200 | -$2.0M | - | out (clean 31, ADX 71, RVol 1.0) |
| 14 | **NVDA** | 176.28 | - | **-** | 20 | - | NEG -$141.6M | - | 180 | 175 | -$25.5M | +$460k bull / -$1.0M bear | out (clean 34, ADX 33, RVol 0.7) |
| 15 | **GOOGL** | 293.36 | - | **-** | 19 | - | POS +$87.1M | 289.29 | 300 | 290 | -$124k | +$203k bull / -$156k bear | out (clean 28, ADX 54, RVol 0.6) |
| 16 | **TSLA** | 393.11 | - | **-** | 17 | - | POS +$436.6M | - | 400 | 380 | -$5.5M | +$60k bull / -$1.1M bear | out (clean 32, ADX 32, RVol 0.4) |
| 17 | **MSTR** | 123.22 | - | **-** | 17 | - | POS +$2.8M | 122.21 | 133 | 120 | +$259k | +$0 bull / -$54k bear | out (clean 28, ADX 28, RVol 0.8) |
| 18 | **HOOD** | 85.44 | - | **-** | 15 | - | POS +$16.1M | - | 85 | 85 | -$840k | - | out (clean 33, ADX 37, RVol 0.6) |
| 19 | **BABA** | 101.72 | - | **-** | 15 | - | NEG -$16.6M | 106.71 | 110 | 101 | +$345k | - | out (clean 30, ADX 27, RVol 0.2) |
| 20 | **UBER** | 70.64 | - | **-** | 14 | - | POS +$17.5M | 68.45 | 70 | 70 | -$114k | - | out (clean 33, ADX 40, RVol 0.5) |
| 21 | **IWM** | 283.36 | - | **-** | 13 | - | POS +$184.3M | 282.96 | 285 | 270 | -$4.7M | - | out (clean 34, ADX 43, RVol 0.4) |
| 22 | **META** | 641.91 | - | **-** | 13 | - | POS +$319.2M | 624.94 | 650 | 635 | -$892k | +$0 bull / -$119k bear | out (clean 31, ADX 10, RVol 0.1) |
| 23 | **PLTR** | 173.23 | - | **-** | 12 | - | POS +$77.7M | - | 170 | 180 | +$1.6M | - | out (clean 29, ADX 31, RVol 0.3) |
| 24 | **NFLX** | 64.08 | - | **-** | 11 | - | NEG -$6.1M | 64.56 | 65 | 65 | -$232k | - | out (clean 27, ADX 32, RVol 0.5) |
| 25 | **CRM** | 218.14 | - | **-** | 11 | - | NEG -$11.1M | - | 230 | 220 | -$50k | - | out (clean 29, ADX 33, RVol 0.4) |
| 26 | **COIN** | 138.02 | - | **-** | 8 | - | POS +$27.3M | - | 141 | 135 | -$157k | - | out (clean 29, ADX 32, RVol 0.3) |
| 27 | **AMZN** | 266.75 | - | **-** | 7 | - | POS +$421.9M | - | 270 | 265 | +$3.7M | - | out (clean 32, ADX 17, RVol 0.4) |

## Big prints this scan (82)
- **AMD** CALL 550 2026-11-11 (0DTE): 748 @ 5.70 = **+$426k** SELL | vol 39,701 / OI 918
- **QQQ** CALL 691 2026-11-12 (1DTE): 430 @ 4.98 = **+$214k** SELL | vol 12,260 / OI 310
- **TSLA** CALL 377.5 2026-11-13 (2DTE): 120 @ 15.50 = **+$186k** SELL | vol 836 / OI 4,591
- **TSLA** CALL 377.5 2026-11-13 (2DTE): 120 @ 15.50 = **+$186k** SELL | vol 836 / OI 4,591
- **MU** CALL 800 2026-11-11 (0DTE): 68 @ 21.75 = **+$148k** SELL | vol 51,094 / OI 2,486
- **MU** CALL 820 2026-11-13 (2DTE): 63 @ 21.20 = **+$134k** SELL | vol 5,135 / OI 1,308
- **MU** CALL 820 2026-11-13 (2DTE): 57 @ 21.20 = **+$121k** SELL | vol 5,135 / OI 1,308
- **MU** CALL 800 2026-11-11 (0DTE): 45 @ 21.78 = **+$98k** SELL | vol 51,094 / OI 2,486
- **MU** CALL 800 2026-11-11 (0DTE): 45 @ 21.77 = **+$98k** SELL | vol 51,094 / OI 2,486
- **MU** CALL 800 2026-11-11 (0DTE): 45 @ 21.75 = **+$98k** SELL | vol 51,094 / OI 2,486
- **TSLA** CALL 377.5 2026-11-13 (2DTE): 60 @ 15.50 = **+$93k** SELL | vol 836 / OI 4,591
- **NVDA** PUT 175 2026-11-11 (0DTE): 2,000 @ 0.43 = **+$86k** SELL | vol 123,009 / OI 7,572
- **MU** PUT 820 2026-11-13 (2DTE): 39 @ 20.65 = **+$81k** BUY | vol 4,282 / OI 597
- **MU** CALL 850 2026-11-13 (2DTE): 84 @ 9.50 = **+$80k** SELL | vol 7,198 / OI 0
- **MU** PUT 845 2026-11-11 (0DTE): 30 @ 25.00 = **+$75k** BUY | vol 124 / OI 162

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 760 2026-11-16 (5DTE): 650 traded vs OI 619
- **SPY** CALL 762 2026-12-11 (30DTE): 502 traded vs OI 231
- **QQQ** CALL 720 2026-11-13 (2DTE): 4,184 traded vs OI 3,797
- **QQQ** PUT 670 2026-11-16 (5DTE): 830 traded vs OI 801
- **TSLA** CALL 415 2026-11-13 (2DTE): 3,064 traded vs OI 3,001
- **AMD** CALL 597.5 2026-11-13 (2DTE): 506 traded vs OI 0
- **GOOGL** CALL 302.5 2026-11-13 (2DTE): 1,460 traded vs OI 1,369
- **DELL** CALL 420 2026-11-13 (2DTE): 500 traded vs OI 0
- **MSTR** CALL 130 2026-12-11 (30DTE): 512 traded vs OI 101
- **ORCL** CALL 133 2026-11-13 (2DTE): 1,113 traded vs OI 1,037
- **ORCL** PUT 128 2026-11-13 (2DTE): 909 traded vs OI 821
- **HOOD** CALL 92 2026-11-13 (2DTE): 610 traded vs OI 0
- **HOOD** CALL 93 2026-11-13 (2DTE): 638 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
