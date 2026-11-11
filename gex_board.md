# GEX + FLOW SCAN - Wed Nov 11, 12:50 PM ET
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
Last 1m check 12:50:08 ET, last candle SPY 12:49, QQQ 12:49 | no errors
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
| 1 | **SHOP** | 149.65 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 39 | none: 21 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$3.7M | 145.45 | 150 | 140 | -$479k | - | out (clean 33, ADX 40, RVol 0.2) |
| 2 | **AAPL** | 354.61 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 33 | none: 113 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (66 contracts' greeks worked out here) | POS +$2.0B | 342.13 | 355 | 350 | +$898k | +$344k bull / -$298k bear | out (clean 27, ADX 33, RVol 0.2) |
| 3 | **SMCI** | 31.16 | - | **-** | 28 | - | POS +$12.5M | - | 32 | 30 | -$748k | +$39k bull / +$0 bear | out (clean 33, ADX 63, RVol 0.5) |
| 4 | **MU** | 824.10 | - | **-** | 28 | - | POS +$109.4M | - | 800 | 800 | -$224.4M | +$2.5M bull / -$1.8M bear | out (clean 34, ADX 63, RVol 0.4) |
| 5 | **AMD** | 560.24 | - | **-** | 27 | - | POS +$138.0M | - | 550 | 550 | -$86.7M | +$0 bull / -$3.0M bear | out (clean 34, ADX 49, RVol 0.4) |
| 6 | **DELL** | 382.37 | - | **-** | 27 | - | POS +$2.2M | - | 380 | 380 | -$3.4M | +$63k bull / +$0 bear | out (clean 37, ADX 66, RVol 0.4) |
| 7 | **SMH** | 515.32 | - | **-** | 26 | - | NEG -$16.9M | - | 515 | 500 | -$5.0M | +$32k bull / -$77k bear | out (clean 32, ADX 55, RVol 0.5) |
| 8 | **QQQ** | 694.28 | - | **-** | 25 | - | POS +$652.7M | 691.68 | 700 | 680 | -$170.2M | +$242k bull / -$115k bear | out (clean 33, ADX 57, RVol 0.5) |
| 9 | **SPY** | 761.22 | - | **-** | 24 | - | NEG -$810.3M | 762.01 | 760 | 750 | -$137.4M | +$0 bull / -$650k bear | out (clean 32, ADX 59, RVol 0.4) |
| 10 | **AVGO** | 355.49 | - | **-** | 22 | - | POS +$91.6M | - | 350 | 350 | +$4.0M | +$30k bull / -$425k bear | out (clean 35, ADX 53, RVol 0.6) |
| 11 | **ARM** | 206.34 | - | **-** | 22 | - | POS +$5.6M | - | 200 | 200 | -$2.0M | - | out (clean 31, ADX 67, RVol 0.9) |
| 12 | **MSFT** | 521.40 | - | **-** | 21 | - | POS +$60.5M | 516.36 | 535 | 520 | +$12.9M | +$26k bull / -$43k bear | out (clean 32, ADX 25, RVol 0.5) |
| 13 | **NVDA** | 176.57 | - | **-** | 20 | - | NEG -$136.7M | - | 180 | 175 | -$28.6M | +$335k bull / -$3.1M bear | out (clean 34, ADX 34, RVol 0.6) |
| 14 | **GOOGL** | 293.95 | - | **-** | 20 | - | POS +$98.8M | 290.43 | 300 | 290 | -$206k | +$0 bull / -$25k bear | out (clean 28, ADX 56, RVol 0.7) |
| 15 | **COIN** | 138.56 | - | **-** | 20 | - | POS +$27.3M | - | 141 | 135 | -$262k | +$0 bull / -$92k bear | out (clean 29, ADX 33, RVol 0.7) |
| 16 | **ORCL** | 130.51 | - | **-** | 20 | - | POS +$5.4M | 124.42 | 130 | 130 | -$96k | +$214k bull / -$32k bear | out (clean 30, ADX 57, RVol 0.7) |
| 17 | **AMZN** | 266.20 | - | **-** | 18 | - | POS +$405.7M | - | 270 | 265 | +$4.7M | +$306k bull / +$0 bear | out (clean 32, ADX 18, RVol 0.4) |
| 18 | **TSLA** | 392.99 | - | **-** | 17 | - | POS +$413.6M | - | 400 | 380 | -$7.1M | +$165k bull / -$486k bear | out (clean 32, ADX 29, RVol 0.3) |
| 19 | **HOOD** | 85.69 | - | **-** | 15 | - | POS +$16.0M | - | 85 | 85 | -$919k | - | out (clean 34, ADX 41, RVol 0.6) |
| 20 | **IWM** | 283.63 | - | **-** | 14 | - | POS +$259.3M | 282.97 | 285 | 270 | -$5.8M | - | out (clean 35, ADX 46, RVol 0.4) |
| 21 | **META** | 643.88 | - | **-** | 14 | - | POS +$322.1M | 628.24 | 650 | 650 | -$2.0M | +$0 bull / -$71k bear | out (clean 31, ADX 13, RVol 0.3) |
| 22 | **BABA** | 101.66 | - | **-** | 14 | - | NEG -$17.1M | 106.67 | 110 | 101 | +$349k | - | out (clean 30, ADX 21, RVol 0.1) |
| 23 | **PLTR** | 173.23 | - | **-** | 12 | - | POS +$77.6M | - | 170 | 180 | +$1.7M | - | out (clean 29, ADX 32, RVol 0.3) |
| 24 | **NFLX** | 63.99 | - | **-** | 11 | - | NEG -$7.7M | 64.56 | 65 | 65 | -$223k | - | out (clean 27, ADX 34, RVol 0.7) |
| 25 | **UBER** | 70.49 | - | **-** | 9 | - | POS +$17.9M | 68.31 | 70 | 70 | +$29k | - | out (clean 32, ADX 40, RVol 0.4) |
| 26 | **CRM** | 217.34 | - | **-** | 9 | - | NEG -$10.7M | - | 230 | 220 | -$41k | - | out (clean 29, ADX 29, RVol 0.4) |
| 27 | **MSTR** | 123.42 | - | **-** | 7 | - | POS +$3.6M | 122.14 | 133 | 120 | +$126k | - | out (clean 28, ADX 29, RVol 0.8) |

## Big prints this scan (51)
- **NVDA** PUT 177.5 2026-11-13 (2DTE): 786 @ 4.05 = **+$318k** MID | vol 6,289 / OI 4,898
- **AAPL** PUT 352.5 2026-11-13 (2DTE): 969 @ 2.02 = **+$196k** BUY | vol 12,955 / OI 1,070
- **MU** CALL 800 2026-11-11 (0DTE): 50 @ 25.50 = **+$128k** BUY | vol 51,407 / OI 2,486
- **SPY** CALL 750 2026-11-13 (2DTE): 100 @ 11.89 = **+$119k** SELL | vol 3,962 / OI 7,567
- **NVDA** CALL 180 2026-11-16 (5DTE): 400 @ 2.87 = **+$115k** BUY | vol 19,671 / OI 4,762
- **QQQ** CALL 685 2026-11-11 (0DTE): 114 @ 9.40 = **+$107k** BUY | vol 66,388 / OI 1,366
- **AAPL** PUT 352.5 2026-11-13 (2DTE): 504 @ 2.02 = **+$102k** BUY | vol 12,955 / OI 1,070
- **MU** PUT 850 2026-11-11 (0DTE): 30 @ 26.00 = **+$78k** SELL | vol 113 / OI 0
- **TSLA** CALL 392.5 2026-11-13 (2DTE): 120 @ 6.00 = **+$72k** BUY | vol 8,841 / OI 1,321
- **MU** CALL 820 2026-11-11 (0DTE): 76 @ 8.08 = **+$61k** BUY | vol 49,027 / OI 598
- **MU** CALL 825 2026-11-16 (5DTE): 20 @ 26.78 = **+$54k** BUY | vol 654 / OI 715
- **MU** CALL 825 2026-11-16 (5DTE): 20 @ 26.53 = **+$53k** BUY | vol 654 / OI 715
- **NVDA** CALL 180 2026-11-16 (5DTE): 183 @ 2.88 = **+$53k** BUY | vol 19,671 / OI 4,762
- **NVDA** PUT 180 2026-11-18 (7DTE): 50 @ 10.22 = **+$51k** BUY | vol 869 / OI 1,343
- **AMD** CALL 572.5 2026-11-16 (5DTE): 47 @ 10.60 = **+$50k** SELL | vol 93 / OI 3

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 716 2026-11-12 (1DTE): 688 traded vs OI 528
- **SPY** PUT 780 2026-11-16 (5DTE): 879 traded vs OI 3
- **SPY** CALL 777 2026-11-13 (2DTE): 3,200 traded vs OI 3,077
- **SPY** CALL 760 2026-11-18 (7DTE): 825 traded vs OI 790
- **SPY** PUT 755 2026-11-18 (7DTE): 1,065 traded vs OI 962
- **QQQ** CALL 715 2026-11-12 (1DTE): 536 traded vs OI 526
- **QQQ** PUT 696 2026-11-12 (1DTE): 563 traded vs OI 43
- **QQQ** CALL 715 2026-11-25 (14DTE): 6,178 traded vs OI 0
- **SMH** CALL 542.5 2026-11-13 (2DTE): 536 traded vs OI 218
- **SMH** CALL 555 2026-11-13 (2DTE): 676 traded vs OI 0
- **NVDA** CALL 165 2026-11-16 (5DTE): 502 traded vs OI 255
- **NVDA** CALL 170 2026-12-04 (23DTE): 1,045 traded vs OI 1,000
- **NVDA** CALL 190 2026-11-23 (12DTE): 1,013 traded vs OI 960
- **AMD** PUT 525 2026-11-16 (5DTE): 502 traded vs OI 7
- **GOOGL** PUT 292.5 2026-11-13 (2DTE): 579 traded vs OI 183

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
