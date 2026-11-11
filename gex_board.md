# GEX + FLOW SCAN - Wed Nov 11, 03:25 PM ET
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
Last 1m check 15:25:08 ET, last candle SPY 15:24, QQQ 15:24 | no errors
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
| 1 | **META** | 634.44 | PINNED between the walls (positive gamma) - chop | **-** | 33 | - | POS +$142.4M | 630.09 | 635 | 635 | +$6.4M | +$106k bull / +$0 bear | out (clean 30, ADX 43, RVol 0.4) |
| 2 | **MSFT** | 519.71 | FLIP CROSS down into negative gamma | **PUTS** | 33 | none: 162 puts 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (69 contracts' greeks worked out here) | NEG -$18.1M | 520.54 | 535 | 520 | +$15.3M | +$493k bull / +$0 bear | out (clean 32, ADX 19, RVol 0.6) |
| 3 | **IWM** | 282.82 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 26 | none: 340 puts 0-7DTE > 16 priced 0.40-0.80 > 6 delta 0.2+ > 6 spread ok > 6 liquid > best one only +4% at the target (needs +20%) (162 contracts' greeks worked out here) | POS +$173.5M | 282.62 | 283 | 270 | -$4.9M | - | out (clean 35, ADX 25, RVol 0.4) |
| 4 | **AAPL** | 355.02 | PINNED between the walls (positive gamma) - chop | **-** | 26 | - | POS +$3.1B | 343.15 | 355 | 355 | -$654k | +$0 bull / -$223k bear | out (clean 28, ADX 21, RVol 0.3) |
| 5 | **AVGO** | 346.87 | - | **-** | 24 | - | POS +$109.5M | - | 340 | 340 | +$9.7M | +$370k bull / +$0 bear | out (clean 37, ADX 40, RVol 0.8) |
| 6 | **AMD** | 555.40 | - | **-** | 23 | - | POS +$193.5M | - | 550 | 550 | -$90.8M | +$4.2M bull / -$249k bear | out (clean 35, ADX 32, RVol 0.4) |
| 7 | **MU** | 813.15 | - | **-** | 22 | - | POS +$173.2M | - | 800 | 850 | -$194.2M | +$5.6M bull / +$0 bear | out (clean 33, ADX 23, RVol 0.6) |
| 8 | **QQQ** | 691.08 | - | **-** | 19 | - | POS +$489.3M | 689.3 | 700 | 680 | -$128.4M | +$937k bull / +$0 bear | out (clean 33, ADX 31, RVol 0.4) |
| 9 | **SMH** | 508.70 | - | **-** | 19 | - | NEG -$46.8M | 514.76 | 500 | 500 | -$1.6M | +$633k bull / +$0 bear | out (clean 32, ADX 35, RVol 0.5) |
| 10 | **HOOD** | 85.03 | PINNED between the walls (positive gamma) - chop | **-** | 19 | - | POS +$17.6M | - | 85 | 85 | -$552k | - | out (clean 35, ADX 17, RVol 0.4) |
| 11 | **SPY** | 760.06 | - | **-** | 18 | - | NEG -$1.0B | 761.32 | 760 | 750 | -$120.1M | +$2.3M bull / -$129k bear | out (clean 34, ADX 27, RVol 0.2) |
| 12 | **NVDA** | 174.74 | - | **-** | 18 | - | NEG -$194.8M | 180.18 | 175 | 175 | -$20.9M | +$655k bull / -$31k bear | out (clean 34, ADX 31, RVol 0.4) |
| 13 | **PLTR** | 172.78 | - | **-** | 18 | - | POS +$74.2M | - | 170 | 170 | +$1.5M | +$29k bull / +$0 bear | out (clean 29, ADX 17, RVol 0.3) |
| 14 | **MSTR** | 121.28 | - | **-** | 18 | - | NEG -$9.0M | 123.63 | 133 | 120 | +$2.0M | +$28k bull / +$0 bear | out (clean 28, ADX 22, RVol 0.6) |
| 15 | **SHOP** | 149.24 | - | **-** | 17 | - | POS +$3.4M | 145.49 | 150 | 140 | -$477k | - | out (clean 33, ADX 13, RVol 0.3) |
| 16 | **TSLA** | 391.57 | - | **-** | 16 | - | POS +$420.9M | - | 400 | 380 | -$750k | +$1.3M bull / -$286k bear | out (clean 32, ADX 27, RVol 0.3) |
| 17 | **AMZN** | 266.44 | - | **-** | 16 | - | POS +$392.7M | - | 270 | 265 | +$4.2M | +$0 bull / -$29k bear | out (clean 31, ADX 16, RVol 0.5) |
| 18 | **ORCL** | 128.80 | - | **-** | 15 | - | POS +$11.7M | 121.5 | 130 | 125 | +$547k | +$205k bull / +$0 bear | out (clean 30, ADX 18, RVol 0.5) |
| 19 | **ARM** | 203.64 | - | **-** | 14 | - | POS +$6.9M | - | 200 | 200 | -$1.7M | - | out (clean 32, ADX 21, RVol 0.5) |
| 20 | **SMCI** | 30.38 | - | **-** | 13 | - | POS +$15.5M | - | 30 | 30 | -$577k | - | out (clean 34, ADX 36, RVol 0.3) |
| 21 | **BABA** | 101.70 | - | **-** | 13 | - | NEG -$17.1M | 106.42 | 110 | 101 | +$359k | - | out (clean 28, ADX 19, RVol 0.2) |
| 22 | **DELL** | 376.98 | - | **-** | 11 | - | NEG -$1.2M | - | 400 | 400 | -$2.2M | - | out (clean 38, ADX 35, RVol 0.4) |
| 23 | **NFLX** | 64.26 | - | **-** | 10 | - | NEG -$2.6M | 64.43 | 65 | 65 | -$268k | - | out (clean 27, ADX 26, RVol 0.9) |
| 24 | **UBER** | 70.94 | - | **-** | 7 | - | POS +$21.9M | 68.37 | 70 | 70 | -$33k | - | out (clean 32, ADX 27, RVol 0.7) |
| 25 | **COIN** | 136.58 | - | **-** | 6 | - | POS +$24.4M | 128.44 | 141 | 135 | +$62k | - | out (clean 29, ADX 27, RVol 0.4) |
| 26 | **CRM** | 217.32 | - | **-** | 6 | - | NEG -$11.2M | - | 230 | 220 | -$54k | - | out (clean 29, ADX 10, RVol 0.4) |
| 27 | **GOOGL** | 293.94 | - | **-** | 5 | - | POS +$105.3M | 289.33 | 300 | 290 | -$637k | - | out (clean 29, ADX 23, RVol 0.4) |

## Big prints this scan (104)
- **SPY** CALL 746 2026-11-13 (2DTE): 722 @ 15.63 = **+$1.1M** BUY | vol 1,272 / OI 2,295
- **AMD** PUT 550 2026-11-13 (2DTE): 442 @ 10.45 = **+$462k** SELL | vol 4,233 / OI 154
- **AMD** PUT 555 2026-11-11 (0DTE): 1,274 @ 1.73 = **+$220k** BUY | vol 27,179 / OI 0
- **SPY** CALL 758 2026-11-11 (0DTE): 890 @ 2.41 = **+$214k** BUY | vol 321,326 / OI 1,040
- **AAPL** CALL 337.5 2026-11-11 (0DTE): 112 @ 17.30 = **+$194k** MID | vol 147 / OI 135
- **AMD** PUT 560 2026-11-13 (2DTE): 117 @ 15.20 = **+$178k** SELL | vol 2,706 / OI 104
- **MU** CALL 800 2026-11-16 (5DTE): 50 @ 34.50 = **+$172k** BUY | vol 2,076 / OI 273
- **MU** CALL 790 2026-11-13 (2DTE): 47 @ 36.36 = **+$171k** BUY | vol 3,327 / OI 1,404
- **SPY** CALL 750 2026-11-13 (2DTE): 127 @ 11.26 = **+$143k** BUY | vol 4,903 / OI 7,567
- **MU** CALL 810 2026-11-11 (0DTE): 195 @ 7.30 = **+$142k** BUY | vol 36,222 / OI 513
- **QQQ** PUT 684 2026-11-12 (1DTE): 1,000 @ 1.37 = **+$137k** SELL | vol 9,952 / OI 32
- **SPY** CALL 750 2026-11-11 (0DTE): 127 @ 10.18 = **+$129k** SELL | vol 6,398 / OI 2,382
- **QQQ** CALL 670 2026-11-11 (0DTE): 53 @ 21.59 = **+$114k** BUY | vol 589 / OI 1,665
- **MU** CALL 795 2026-11-11 (0DTE): 50 @ 20.40 = **+$102k** BUY | vol 12,457 / OI 466
- **MU** PUT 820 2026-11-13 (2DTE): 45 @ 21.65 = **+$97k** SELL | vol 9,060 / OI 597

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 727 2026-11-13 (2DTE): 1,870 traded vs OI 1,684
- **SPY** PUT 740 2026-11-19 (8DTE): 1,032 traded vs OI 1,031
- **SPY** PUT 759 2026-11-19 (8DTE): 686 traded vs OI 0
- **SPY** PUT 760 2026-11-23 (12DTE): 659 traded vs OI 6
- **QQQ** CALL 740 2026-11-16 (5DTE): 1,914 traded vs OI 1,848
- **QQQ** CALL 700 2026-11-24 (13DTE): 541 traded vs OI 0
- **QQQ** PUT 707 2026-12-04 (23DTE): 500 traded vs OI 7
- **TSLA** PUT 395 2026-11-20 (9DTE): 2,539 traded vs OI 2,536
- **AMD** PUT 557.5 2026-11-13 (2DTE): 540 traded vs OI 4
- **AMD** CALL 500 2026-11-20 (9DTE): 1,065 traded vs OI 0
- **AMD** CALL 500 2026-11-13 (2DTE): 727 traded vs OI 0
- **AMD** PUT 500 2026-11-16 (5DTE): 605 traded vs OI 0
- **AMD** PUT 500 2026-11-20 (9DTE): 1,961 traded vs OI 0
- **AMD** PUT 507.5 2026-11-13 (2DTE): 505 traded vs OI 185
- **META** CALL 660 2026-11-20 (9DTE): 13,663 traded vs OI 13,602

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
