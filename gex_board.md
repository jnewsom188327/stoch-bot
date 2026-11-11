# GEX + FLOW SCAN - Wed Nov 11, 12:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (12)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:40 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 522.5C | 0.73 | 0.93 | +37% (19m) | **+27%** | +146% | 523.2 |
| 11:05 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.64 | 0.34 | +2% (1m) | **-47%** | +363% | 527.5 |
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
Last 1m check 12:00:08 ET, last candle SPY 11:59, QQQ 11:59 | no errors
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
| 1 | **MSFT** | 520.92 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 43 | none: 166 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (88 contracts' greeks worked out here) | POS +$51.2M | 516.64 | 535 | 520 | +$14.9M | +$26k bull / -$137k bear | out (clean 32, ADX 43, RVol 0.6) |
| 2 | **SMH** | 514.56 | FLOW SURGE | **PUTS** | 42 | none: 164 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (67 contracts' greeks worked out here) | NEG -$24.1M | - | 500 | 500 | -$6.1M | +$0 bull / -$95k bear | out (clean 31, ADX 55, RVol 0.7) |
| 3 | **SMCI** | 30.95 | FLOW SURGE | **PUTS** | 42 | none: 13 puts 0-7DTE > 2 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +17% at the target (needs +20%) | POS +$12.6M | - | 30 | 30 | -$849k | +$0 bull / -$31k bear | out (clean 32, ADX 70, RVol 1.1) |
| 4 | **ARM** | 205.96 | FLOW SURGE | **PUTS** | 41 | none: 16 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$5.4M | - | 200 | 200 | -$2.0M | +$0 bull / -$82k bear | out (clean 31, ADX 75, RVol 0.8) |
| 5 | **MU** | 824.99 | FLOW SURGE | **PUTS** | 38 | none: 145 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (57 contracts' greeks worked out here) | POS +$113.4M | - | 800 | 800 | -$233.3M | +$0 bull / -$6.6M bear | LONG (clean 33, ADX 72, RVol 0.5) |
| 6 | **DELL** | 382.12 | TREND (flow not with it) | **CALLS** | 36 | none: 31 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$2.2M | - | 380 | 380 | -$3.8M | - | LONG (clean 36, ADX 71, RVol 0.7) |
| 7 | **AMD** | 556.41 | - | **-** | 27 | - | POS +$137.2M | - | 550 | 550 | -$78.1M | +$0 bull / -$878k bear | out (clean 33, ADX 49, RVol 0.3) |
| 8 | **QQQ** | 693.53 | - | **-** | 26 | - | POS +$653.3M | 690.39 | 700 | 680 | -$159.6M | +$0 bull / -$1.4M bear | out (clean 32, ADX 57, RVol 0.6) |
| 9 | **AAPL** | 354.33 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 25 | none: 109 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (75 contracts' greeks worked out here) | POS +$1.6B | 340.03 | 355 | 350 | -$1.6M | - | out (clean 27, ADX 40, RVol 0.3) |
| 10 | **SPY** | 760.10 | - | **-** | 23 | - | NEG -$1.2B | 761.69 | 760 | 750 | -$93.2M | +$0 bull / -$4.1M bear | out (clean 32, ADX 53, RVol 0.4) |
| 11 | **IWM** | 282.88 | - | **-** | 23 | - | POS +$12.1M | 282.9 | 285 | 270 | -$3.9M | +$106k bull / +$0 bear | out (clean 35, ADX 44, RVol 0.3) |
| 12 | **GOOGL** | 293.19 | - | **-** | 21 | - | POS +$87.8M | 289.39 | 300 | 290 | -$939k | +$0 bull / -$40k bear | out (clean 28, ADX 53, RVol 0.6) |
| 13 | **NVDA** | 176.37 | - | **-** | 20 | - | NEG -$135.8M | 180.5 | 180 | 175 | -$21.6M | +$1.2M bull / -$1.4M bear | out (clean 34, ADX 33, RVol 0.7) |
| 14 | **ORCL** | 128.59 | - | **-** | 20 | - | POS +$3.6M | 124.98 | 130 | 125 | -$549k | +$0 bull / -$51k bear | out (clean 29, ADX 50, RVol 0.4) |
| 15 | **UBER** | 70.11 | PINNED between the walls (positive gamma) - chop | **-** | 20 | - | POS +$16.5M | 68.26 | 70 | 70 | +$33k | - | out (clean 32, ADX 24, RVol 0.4) |
| 16 | **TSLA** | 392.90 | - | **-** | 19 | - | POS +$411.3M | - | 400 | 380 | -$4.1M | +$85k bull / -$1.5M bear | out (clean 32, ADX 44, RVol 0.3) |
| 17 | **MSTR** | 122.66 | - | **-** | 18 | - | POS +$738k | 122.33 | 133 | 120 | +$370k | +$137k bull / -$90k bear | out (clean 28, ADX 27, RVol 1.0) |
| 18 | **BABA** | 101.46 | - | **-** | 18 | - | NEG -$16.3M | 106.43 | 110 | 101 | +$365k | - | out (clean 29, ADX 36, RVol 0.2) |
| 19 | **META** | 641.26 | - | **-** | 13 | - | POS +$308.0M | 623.98 | 650 | 635 | -$746k | +$0 bull / -$57k bear | out (clean 32, ADX 12, RVol 0.2) |
| 20 | **AVGO** | 354.77 | - | **-** | 13 | - | POS +$98.7M | - | 350 | 350 | +$4.6M | - | out (clean 34, ADX 53, RVol 0.6) |
| 21 | **PLTR** | 172.79 | - | **-** | 13 | - | POS +$77.5M | - | 170 | 170 | +$1.8M | - | out (clean 29, ADX 34, RVol 0.3) |
| 22 | **HOOD** | 84.69 | - | **-** | 13 | - | POS +$15.6M | - | 85 | 85 | -$664k | - | out (clean 33, ADX 34, RVol 0.5) |
| 23 | **SHOP** | 149.80 | - | **-** | 12 | - | POS +$4.0M | 145.03 | 155 | 140 | +$25k | - | out (clean 33, ADX 38, RVol 0.4) |
| 24 | **CRM** | 217.35 | - | **-** | 11 | - | NEG -$11.2M | - | 230 | 220 | -$36k | - | out (clean 30, ADX 33, RVol 0.7) |
| 25 | **AMZN** | 267.18 | - | **-** | 7 | - | POS +$432.3M | - | 270 | 265 | +$2.8M | - | out (clean 32, ADX 21, RVol 0.4) |
| 26 | **NFLX** | 63.78 | - | **-** | 6 | - | NEG -$9.4M | 64.5 | 65 | 65 | -$45k | - | out (clean 26, ADX 20, RVol 0.6) |
| 27 | **COIN** | 136.88 | - | **-** | 6 | - | POS +$24.9M | - | 141 | 135 | -$4k | - | out (clean 29, ADX 32, RVol 0.3) |

## Big prints this scan (72)
- **MU** PUT 825 2026-11-11 (0DTE): 300 @ 7.79 = **+$234k** BUY | vol 1,306 / OI 75
- **MU** PUT 820 2026-11-13 (2DTE): 108 @ 19.90 = **+$215k** BUY | vol 3,090 / OI 597
- **MU** CALL 825 2026-11-13 (2DTE): 100 @ 19.35 = **+$194k** SELL | vol 1,853 / OI 428
- **MU** CALL 825 2026-11-13 (2DTE): 98 @ 19.45 = **+$191k** SELL | vol 1,853 / OI 428
- **QQQ** PUT 698 2026-11-13 (2DTE): 170 @ 8.54 = **+$145k** BUY | vol 223 / OI 4,164
- **QQQ** CALL 690 2026-11-11 (0DTE): 489 @ 2.80 = **+$137k** SELL | vol 231,797 / OI 2,827
- **QQQ** CALL 690 2026-11-11 (0DTE): 464 @ 2.95 = **+$137k** SELL | vol 231,797 / OI 2,827
- **SPY** PUT 756 2026-11-12 (1DTE): 1,000 @ 1.26 = **+$126k** BUY | vol 29,176 / OI 213
- **TSLA** PUT 402.5 2026-11-11 (0DTE): 120 @ 10.00 = **+$120k** BUY | vol 744 / OI 121
- **NVDA** CALL 175 2026-11-13 (2DTE): 300 @ 3.59 = **+$108k** SELL | vol 48,021 / OI 8,003
- **MU** PUT 840 2026-11-11 (0DTE): 50 @ 19.50 = **+$98k** BUY | vol 137 / OI 72
- **MU** CALL 800 2026-11-16 (5DTE): 20 @ 39.07 = **+$78k** SELL | vol 1,698 / OI 273
- **MU** CALL 800 2026-11-16 (5DTE): 20 @ 38.60 = **+$77k** SELL | vol 1,698 / OI 273
- **MU** CALL 800 2026-11-16 (5DTE): 20 @ 38.60 = **+$77k** SELL | vol 1,698 / OI 273
- **MU** CALL 800 2026-11-16 (5DTE): 20 @ 38.51 = **+$77k** SELL | vol 1,698 / OI 273

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 761 2026-11-12 (1DTE): 551 traded vs OI 186
- **SPY** CALL 762 2026-11-13 (2DTE): 6,361 traded vs OI 6,301
- **SPY** CALL 770 2026-11-13 (2DTE): 8,409 traded vs OI 8,317
- **QQQ** PUT 694 2026-11-12 (1DTE): 535 traded vs OI 114
- **QQQ** CALL 693 2026-11-13 (2DTE): 1,380 traded vs OI 1,364
- **QQQ** PUT 643 2026-11-13 (2DTE): 546 traded vs OI 225
- **QQQ** CALL 706 2026-11-13 (2DTE): 745 traded vs OI 736
- **QQQ** PUT 634 2026-11-20 (9DTE): 1,027 traded vs OI 205
- **QQQ** CALL 710 2026-12-11 (30DTE): 626 traded vs OI 623
- **NVDA** CALL 180 2026-12-04 (23DTE): 2,101 traded vs OI 2,090
- **TSLA** PUT 390 2026-11-18 (7DTE): 509 traded vs OI 131
- **AMZN** CALL 270 2026-12-04 (23DTE): 1,934 traded vs OI 1,750
- **MSFT** PUT 500 2026-11-20 (9DTE): 12,027 traded vs OI 11,854
- **AVGO** CALL 390 2026-11-13 (2DTE): 3,301 traded vs OI 0
- **AVGO** CALL 390 2026-11-20 (9DTE): 779 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
