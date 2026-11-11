# GEX + FLOW SCAN - Wed Nov 11, 01:10 PM ET
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
Last 1m check 13:10:08 ET, last candle SPY 13:09, QQQ 13:09 | no errors
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
| 1 | **AMD** | 560.72 | - | **-** | 28 | - | POS +$142.5M | - | 550 | 550 | -$100.4M | +$599k bull / -$6.1M bear | out (clean 34, ADX 51, RVol 0.4) |
| 2 | **DELL** | 382.59 | - | **-** | 27 | - | POS +$2.4M | - | 380 | 380 | -$4.0M | +$0 bull / -$303k bear | out (clean 37, ADX 62, RVol 0.4) |
| 3 | **MU** | 822.30 | - | **-** | 27 | - | POS +$154.9M | - | 800 | 800 | -$219.4M | +$3.6M bull / -$472k bear | out (clean 34, ADX 57, RVol 0.3) |
| 4 | **ORCL** | 129.68 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 27 | none: 26 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$5.1M | 123.98 | 130 | 125 | +$111k | - | out (clean 30, ADX 53, RVol 0.5) |
| 5 | **SMH** | 514.55 | - | **-** | 25 | - | NEG -$13.9M | - | 515 | 500 | -$4.7M | +$68k bull / -$25k bear | out (clean 32, ADX 51, RVol 0.4) |
| 6 | **SPY** | 761.12 | - | **-** | 24 | - | NEG -$514.3M | 761.82 | 760 | 750 | -$137.8M | +$104k bull / -$119k bear | out (clean 33, ADX 55, RVol 0.6) |
| 7 | **QQQ** | 693.79 | - | **-** | 24 | - | POS +$754.4M | 690.48 | 700 | 680 | -$163.4M | +$888k bull / -$317k bear | out (clean 33, ADX 52, RVol 0.4) |
| 8 | **HOOD** | 85.27 | - | **-** | 23 | - | POS +$16.5M | - | 85 | 85 | -$736k | +$35k bull / +$0 bear | out (clean 34, ADX 38, RVol 0.3) |
| 9 | **SHOP** | 149.49 | - | **-** | 22 | - | POS +$3.6M | 145.4 | 150 | 140 | -$476k | - | out (clean 33, ADX 34, RVol 0.2) |
| 10 | **ARM** | 206.09 | - | **-** | 21 | - | POS +$5.6M | - | 200 | 200 | -$2.0M | - | out (clean 31, ADX 62, RVol 0.6) |
| 11 | **MSFT** | 521.37 | - | **-** | 20 | - | POS +$41.9M | 517.91 | 535 | 520 | +$13.4M | +$266k bull / -$37k bear | out (clean 32, ADX 22, RVol 0.4) |
| 12 | **GOOGL** | 294.58 | - | **-** | 20 | - | POS +$111.9M | 289.08 | 300 | 290 | -$481k | +$56k bull / -$32k bear | out (clean 29, ADX 57, RVol 0.5) |
| 13 | **NVDA** | 176.47 | - | **-** | 19 | - | NEG -$135.6M | 180.48 | 180 | 175 | -$25.5M | +$1.2M bull / -$122k bear | out (clean 34, ADX 32, RVol 0.3) |
| 14 | **AAPL** | 354.83 | PINNED between the walls (positive gamma) - chop | **-** | 18 | - | POS +$2.1B | 341.81 | 355 | 355 | +$243k | - | out (clean 27, ADX 32, RVol 0.2) |
| 15 | **AMZN** | 265.89 | - | **-** | 18 | - | POS +$418.7M | - | 270 | 265 | +$4.7M | +$33k bull / -$193k bear | out (clean 32, ADX 22, RVol 0.4) |
| 16 | **COIN** | 137.79 | - | **-** | 18 | - | POS +$26.1M | - | 141 | 135 | +$90k | +$173k bull / +$0 bear | out (clean 29, ADX 29, RVol 1.2) |
| 17 | **MSTR** | 122.56 | - | **-** | 18 | - | POS +$441k | 122.25 | 133 | 120 | +$682k | +$30k bull / +$0 bear | out (clean 28, ADX 25, RVol 1.0) |
| 18 | **SMCI** | 30.96 | - | **-** | 17 | - | POS +$12.7M | - | 30 | 30 | -$732k | - | out (clean 33, ADX 55, RVol 0.5) |
| 19 | **TSLA** | 392.64 | - | **-** | 15 | - | POS +$428.6M | - | 400 | 380 | -$3.5M | +$437k bull / -$111k bear | out (clean 31, ADX 22, RVol 0.4) |
| 20 | **IWM** | 283.38 | - | **-** | 14 | - | POS +$237.9M | 282.88 | 285 | 270 | -$5.6M | - | out (clean 35, ADX 46, RVol 0.3) |
| 21 | **META** | 640.01 | - | **-** | 14 | - | POS +$264.8M | 625.72 | 650 | 635 | -$230k | +$289k bull / -$59k bear | out (clean 31, ADX 15, RVol 0.5) |
| 22 | **BABA** | 101.67 | - | **-** | 13 | - | NEG -$17.3M | 106.49 | 110 | 101 | +$352k | - | out (clean 30, ADX 17, RVol 0.2) |
| 23 | **AVGO** | 353.43 | - | **-** | 12 | - | POS +$101.7M | - | 350 | 350 | +$4.6M | - | out (clean 35, ADX 46, RVol 0.4) |
| 24 | **PLTR** | 172.70 | - | **-** | 12 | - | POS +$77.1M | - | 170 | 170 | +$1.9M | - | out (clean 29, ADX 31, RVol 0.2) |
| 25 | **NFLX** | 63.80 | - | **-** | 9 | - | NEG -$7.7M | 64.37 | 65 | 65 | -$158k | - | out (clean 27, ADX 28, RVol 0.7) |
| 26 | **CRM** | 217.21 | - | **-** | 9 | - | NEG -$11.3M | - | 230 | 220 | -$39k | - | out (clean 29, ADX 24, RVol 0.6) |
| 27 | **UBER** | 70.70 | - | **-** | 8 | - | POS +$18.7M | 68.32 | 70 | 70 | -$346 | - | out (clean 32, ADX 42, RVol 0.2) |

## Big prints this scan (59)
- **AMD** PUT 577.5 2026-11-13 (2DTE): 200 @ 24.10 = **+$482k** BUY | vol 429 / OI 0
- **AMD** PUT 575 2026-11-13 (2DTE): 200 @ 22.67 = **+$453k** BUY | vol 895 / OI 15
- **AMD** PUT 575 2026-11-13 (2DTE): 200 @ 22.45 = **+$449k** BUY | vol 895 / OI 15
- **AMD** PUT 572.5 2026-11-13 (2DTE): 200 @ 21.02 = **+$420k** BUY | vol 443 / OI 1
- **QQQ** CALL 672 2026-11-11 (0DTE): 75 @ 22.11 = **+$166k** MID | vol 548 / OI 159
- **MU** CALL 810 2026-11-11 (0DTE): 100 @ 15.70 = **+$157k** BUY | vol 33,652 / OI 513
- **QQQ** PUT 697 2026-11-11 (0DTE): 441 @ 3.43 = **+$151k** BUY | vol 4,643 / OI 29
- **QQQ** CALL 687 2026-11-12 (1DTE): 152 @ 8.60 = **+$131k** MID | vol 6,979 / OI 198
- **AMD** PUT 577.5 2026-11-13 (2DTE): 50 @ 24.50 = **+$122k** BUY | vol 429 / OI 0
- **TSLA** PUT 402.5 2026-11-11 (0DTE): 120 @ 10.00 = **+$120k** MID | vol 1,248 / OI 121
- **SPY** CALL 752 2026-11-16 (5DTE): 108 @ 11.06 = **+$119k** SELL | vol 425 / OI 634
- **AMD** PUT 575 2026-11-13 (2DTE): 50 @ 22.77 = **+$114k** BUY | vol 895 / OI 15
- **MU** CALL 820 2026-11-11 (0DTE): 150 @ 6.30 = **+$94k** BUY | vol 50,812 / OI 598
- **AMD** PUT 577.5 2026-11-13 (2DTE): 37 @ 24.49 = **+$91k** BUY | vol 429 / OI 0
- **AMD** PUT 577.5 2026-11-13 (2DTE): 37 @ 24.49 = **+$91k** BUY | vol 429 / OI 0

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 718 2026-11-12 (1DTE): 1,113 traded vs OI 612
- **SPY** PUT 767 2026-11-11 (0DTE): 503 traded vs OI 6
- **SPY** CALL 762 2026-11-20 (9DTE): 5,595 traded vs OI 5,577
- **QQQ** CALL 672 2026-11-11 (0DTE): 548 traded vs OI 159
- **QQQ** PUT 637 2026-11-13 (2DTE): 615 traded vs OI 294
- **QQQ** CALL 694 2026-11-17 (6DTE): 516 traded vs OI 78
- **NVDA** PUT 187.5 2026-11-13 (2DTE): 3,500 traded vs OI 3,493
- **TSLA** CALL 380 2026-11-16 (5DTE): 739 traded vs OI 738
- **TSLA** CALL 395 2026-11-18 (7DTE): 504 traded vs OI 171
- **AMD** PUT 575 2026-11-13 (2DTE): 895 traded vs OI 15
- **MSFT** CALL 530 2026-11-16 (5DTE): 513 traded vs OI 44
- **AVGO** PUT 332.5 2026-11-13 (2DTE): 500 traded vs OI 180
- **ORCL** PUT 122 2026-11-13 (2DTE): 501 traded vs OI 326

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
