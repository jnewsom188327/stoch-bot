# GEX + FLOW SCAN - Wed Nov 11, 02:20 PM ET
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
Last 1m check 14:20:08 ET, last candle SPY 14:19, QQQ 14:19 | no errors
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
| 1 | **META** | 635.05 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 39 | none: 204 calls 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (80 contracts' greeks worked out here) | POS +$181.6M | 627.11 | 650 | 635 | +$4.7M | +$845k bull / +$0 bear | out (clean 30, ADX 35, RVol 0.8) |
| 2 | **MSFT** | 520.37 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 35 | none: 162 calls 0-7DTE > 9 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +6% at the target (needs +20%) (66 contracts' greeks worked out here) | POS +$55.8M | 516.4 | 535 | 520 | +$13.5M | +$115k bull / +$0 bear | out (clean 32, ADX 16, RVol 0.3) |
| 3 | **AVGO** | 349.27 | PINNED between the walls (positive gamma) - chop | **-** | 33 | - | POS +$108.3M | - | 350 | 350 | +$7.0M | +$388k bull / +$0 bear | out (clean 35, ADX 26, RVol 0.6) |
| 4 | **DELL** | 379.43 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$2.3M | - | 380 | 380 | -$3.8M | - | out (clean 37, ADX 44, RVol 0.3) |
| 5 | **AMD** | 560.00 | - | **-** | 27 | - | POS +$148.6M | - | 550 | 550 | -$105.2M | +$2.0M bull / +$0 bear | out (clean 34, ADX 53, RVol 0.8) |
| 6 | **IWM** | 282.83 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 26 | 11/11 283P @ 0.45 (delta 0.57) = est +36% at 282.38 | POS +$15.1M | 282.8 | 283 | 270 | -$5.2M | - | out (clean 35, ADX 30, RVol 0.3) |
| 7 | **MU** | 816.74 | - | **-** | 26 | - | POS +$165.1M | - | 800 | 800 | -$212.9M | +$1.9M bull / +$0 bear | out (clean 34, ADX 40, RVol 0.5) |
| 8 | **SPY** | 759.86 | - | **-** | 22 | - | NEG -$1.3B | 761.32 | 760 | 750 | -$127.0M | +$992k bull / +$0 bear | out (clean 33, ADX 42, RVol 0.3) |
| 9 | **QQQ** | 691.86 | - | **-** | 22 | - | POS +$413.7M | 689.88 | 700 | 680 | -$156.9M | +$2.5M bull / +$0 bear | out (clean 32, ADX 38, RVol 0.5) |
| 10 | **HOOD** | 85.19 | PINNED between the walls (positive gamma) - chop | **-** | 22 | - | POS +$16.1M | - | 85 | 85 | -$658k | - | out (clean 34, ADX 32, RVol 0.3) |
| 11 | **SMH** | 510.58 | - | **-** | 21 | - | NEG -$22.7M | 514.38 | 500 | 500 | -$3.7M | +$288k bull / +$0 bear | out (clean 31, ADX 37, RVol 0.2) |
| 12 | **GOOGL** | 293.65 | - | **-** | 19 | - | POS +$98.6M | 289.43 | 300 | 290 | +$121k | +$61k bull / +$0 bear | out (clean 29, ADX 46, RVol 0.4) |
| 13 | **NVDA** | 175.45 | - | **-** | 18 | - | NEG -$164.6M | 180.88 | 180 | 175 | -$24.9M | +$1.4M bull / +$0 bear | out (clean 34, ADX 28, RVol 0.4) |
| 14 | **SHOP** | 148.95 | - | **-** | 18 | - | POS +$3.5M | 145.29 | 150 | 140 | -$449k | - | out (clean 33, ADX 20, RVol 0.3) |
| 15 | **AAPL** | 354.75 | PINNED between the walls (positive gamma) - chop | **-** | 17 | - | POS +$2.4B | 341.95 | 355 | 355 | +$255k | - | out (clean 28, ADX 30, RVol 0.3) |
| 16 | **ARM** | 204.67 | - | **-** | 17 | - | POS +$5.6M | - | 200 | 200 | -$1.8M | - | out (clean 31, ADX 38, RVol 0.4) |
| 17 | **TSLA** | 392.17 | - | **-** | 15 | - | POS +$441.9M | - | 400 | 380 | -$3.2M | +$820k bull / +$0 bear | out (clean 32, ADX 21, RVol 0.3) |
| 18 | **SMCI** | 30.63 | - | **-** | 13 | - | POS +$12.9M | - | 30 | 30 | -$628k | - | out (clean 32, ADX 33, RVol 0.5) |
| 19 | **BABA** | 101.46 | - | **-** | 13 | - | NEG -$17.5M | 106.88 | 110 | 101 | +$373k | - | out (clean 29, ADX 16, RVol 0.4) |
| 20 | **PLTR** | 172.74 | - | **-** | 11 | - | POS +$81.8M | - | 170 | 170 | +$1.6M | - | out (clean 29, ADX 32, RVol 0.2) |
| 21 | **UBER** | 70.88 | - | **-** | 9 | - | POS +$20.3M | 68.28 | 70 | 70 | -$7k | - | out (clean 32, ADX 47, RVol 0.6) |
| 22 | **AMZN** | 265.75 | - | **-** | 8 | - | POS +$402.6M | - | 270 | 265 | +$7.0M | - | out (clean 32, ADX 16, RVol 0.5) |
| 23 | **NFLX** | 63.90 | - | **-** | 8 | - | NEG -$7.6M | 64.48 | 65 | 65 | -$220k | - | out (clean 28, ADX 18, RVol 0.8) |
| 24 | **ORCL** | 128.75 | - | **-** | 8 | - | POS +$4.3M | 124.53 | 130 | 125 | +$368k | - | out (clean 30, ADX 36, RVol 0.3) |
| 25 | **CRM** | 217.82 | - | **-** | 8 | - | NEG -$11.6M | - | 230 | 220 | -$60k | - | out (clean 30, ADX 16, RVol 0.2) |
| 26 | **COIN** | 137.27 | - | **-** | 6 | - | POS +$25.4M | - | 141 | 135 | +$124k | - | out (clean 29, ADX 22, RVol 0.4) |
| 27 | **MSTR** | 121.60 | - | **-** | 6 | - | NEG -$7.8M | 123.63 | 133 | 120 | +$1.3M | - | out (clean 28, ADX 19, RVol 0.3) |

## Big prints this scan (69)
- **QQQ** PUT 709 2026-11-13 (2DTE): 275 @ 14.91 = **+$410k** SELL | vol 280 / OI 46
- **SPY** CALL 750 2026-11-13 (2DTE): 240 @ 12.88 = **+$309k** BUY | vol 4,688 / OI 7,567
- **SPY** PUT 763 2026-11-16 (5DTE): 574 @ 4.33 = **+$249k** SELL | vol 2,179 / OI 216
- **QQQ** PUT 702 2026-11-12 (1DTE): 275 @ 8.22 = **+$226k** SELL | vol 594 / OI 6
- **QQQ** PUT 698 2026-11-11 (0DTE): 476 @ 3.71 = **+$177k** SELL | vol 4,005 / OI 115
- **QQQ** PUT 689 2026-11-12 (1DTE): 1,000 @ 1.75 = **+$175k** SELL | vol 9,072 / OI 32
- **AMD** CALL 577.5 2026-11-18 (7DTE): 100 @ 16.82 = **+$168k** BUY | vol 120 / OI 1
- **AMD** CALL 567.5 2026-11-11 (0DTE): 863 @ 1.85 = **+$160k** BUY | vol 20,443 / OI 610
- **MU** CALL 820 2026-11-13 (2DTE): 69 @ 22.80 = **+$157k** BUY | vol 6,805 / OI 1,308
- **AMD** CALL 580 2026-11-18 (7DTE): 100 @ 15.67 = **+$157k** BUY | vol 181 / OI 43
- **MU** CALL 820 2026-11-13 (2DTE): 68 @ 22.76 = **+$155k** BUY | vol 6,805 / OI 1,308
- **META** PUT 635 2026-11-13 (2DTE): 200 @ 7.68 = **+$154k** SELL | vol 1,424 / OI 1,304
- **QQQ** PUT 695 2026-11-12 (1DTE): 400 @ 3.60 = **+$144k** SELL | vol 10,301 / OI 244
- **META** PUT 632.5 2026-11-13 (2DTE): 200 @ 6.63 = **+$133k** SELL | vol 541 / OI 162
- **MU** CALL 800 2026-11-11 (0DTE): 50 @ 24.00 = **+$120k** BUY | vol 52,813 / OI 2,486

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 773 2026-11-12 (1DTE): 553 traded vs OI 540
- **SPY** PUT 763 2026-11-16 (5DTE): 2,179 traded vs OI 216
- **SPY** PUT 760 2026-11-17 (6DTE): 508 traded vs OI 182
- **QQQ** PUT 702 2026-11-12 (1DTE): 594 traded vs OI 6
- **NVDA** CALL 190 2026-11-13 (2DTE): 37,203 traded vs OI 36,906
- **AAPL** CALL 370 2026-11-18 (7DTE): 871 traded vs OI 180
- **AMD** CALL 592.5 2026-11-11 (0DTE): 538 traded vs OI 0
- **META** PUT 635 2026-11-13 (2DTE): 1,424 traded vs OI 1,304
- **META** CALL 667.5 2026-11-13 (2DTE): 508 traded vs OI 298
- **META** PUT 632.5 2026-11-13 (2DTE): 541 traded vs OI 162
- **AMZN** CALL 267.5 2026-11-13 (2DTE): 7,132 traded vs OI 6,987
- **AMZN** PUT 277.5 2026-11-13 (2DTE): 545 traded vs OI 66
- **MSFT** PUT 517.5 2026-11-20 (9DTE): 519 traded vs OI 410
- **GOOGL** PUT 287.5 2026-11-13 (2DTE): 862 traded vs OI 825
- **AVGO** PUT 315 2026-11-20 (9DTE): 672 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
