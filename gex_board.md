# GEX + FLOW SCAN - Wed Nov 11, 10:15 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (7)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:15 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.65 | 0.63 | -3% (0m) | **-3%** | +66% | 282.84 |
| 10:05 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 175C | 0.76 | 0.38 | -1% (0m) | **-50%** | +58% | 175 |
| 09:50 | **GOOGL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 292.5C | 0.51 | 0.50 | +14% (6m) | **-2%** | +82% | 291.86 |
| 09:45 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.68 | 0.64 | +85% (6m) | **-6%** | +68% | 282.96 |
| 09:45 | **QQQ** | **CALLS** | FLOW SURGE | 11/11 690C | 0.63 | 0.43 | +32% (23m) | **-32%** | +171% | 689.78 |
| 09:39 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 693C | 0.52 | 0.11 | -10% (0m) | **-79%** | +92% | 690.43 |
| 09:39 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 760C | 0.53 | 0.10 | -2% (0m) | **-81%** | +79% | 758.82 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:15:08 ET, last candle SPY 10:14, QQQ 10:14 | no errors
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
| 1 | **NVDA** | 172.19 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 56 | 11/11 175C @ 0.52 (delta 0.23) = est +142% at 175 | NEG -$168.9M | 180.83 | 180 | 170 | +$6.4M | +$2.7M bull / -$1.7M bear | LONG (clean 34, ADX 26, RVol 1.0) |
| 2 | **DELL** | 367.76 | FLOW SURGE | **PUTS** | 54 | none: 29 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$931k | - | 380 | 340 | -$1.2M | +$0 bull / -$40k bear | LONG (clean 35, ADX 52, RVol 1.9) |
| 3 | **AVGO** | 348.73 | TREND + FLOW | **CALLS** | 52 | none: 112 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (45 contracts' greeks worked out here) | POS +$99.4M | - | 350 | 340 | +$2.1M | +$256k bull / -$182k bear | LONG (clean 35, ADX 50, RVol 1.9) |
| 4 | **MSFT** | 524.16 | FLOW SURGE | **CALLS** | 49 | none: 166 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (69 contracts' greeks worked out here) | POS +$133.3M | 514.64 | 535 | 520 | +$7.6M | +$751k bull / +$0 bear | out (clean 31, ADX 32, RVol 1.7) |
| 5 | **MU** | 791.76 | FLOW SURGE | **PUTS** | 49 | none: 161 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (68 contracts' greeks worked out here) | POS +$162.9M | - | 800 | 800 | -$100.2M | +$0 bull / -$10.9M bear | out (clean 32, ADX 52, RVol 1.8) |
| 6 | **BABA** | 101.76 | FLOW SURGE | **CALLS** | 49 | 11/13 105C @ 0.48 (delta 0.21) = est +22% at 102.43 | NEG -$16.0M | 107.1 | 110 | 101 | +$300k | +$112k bull / +$0 bear | out (clean 29, ADX 30, RVol 1.3) |
| 7 | **IWM** | 281.87 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 48 | 11/11 282C @ 0.65 (delta 0.47) = est +66% at 282.84 | NEG -$373.6M | 282.84 | 285 | 270 | +$248k | +$0 bull / -$91k bear | LONG (clean 35, ADX 38, RVol 1.2) |
| 8 | **AMD** | 535.93 | FLOW SURGE | **PUTS** | 48 | none: 172 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (73 contracts' greeks worked out here) | POS +$135.2M | - | 550 | 500 | -$46.2M | +$0 bull / -$4.6M bear | out (clean 33, ADX 34, RVol 1.9) |
| 9 | **GOOGL** | 290.68 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 41 | 11/11 292.5C @ 0.59 (delta 0.29) = est +86% at 292.55 | POS +$33.7M | 289.15 | 300 | 290 | +$420k | +$178k bull / -$28k bear | out (clean 28, ADX 41, RVol 1.0) |
| 10 | **PLTR** | 171.75 | FLOW SURGE | **CALLS** | 38 | none: 14 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$72.3M | - | 170 | 170 | +$1.6M | +$60k bull / +$0 bear | out (clean 30, ADX 41, RVol 0.5) |
| 11 | **AMZN** | 268.48 | - | **-** | 29 | - | POS +$492.7M | - | 270 | 265 | +$4.2M | +$26k bull / -$94k bear | out (clean 33, ADX 28, RVol 0.9) |
| 12 | **ORCL** | 125.40 | - | **-** | 26 | - | NEG -$2.3M | 127.87 | 130 | 125 | +$843k | +$38k bull / -$76k bear | out (clean 28, ADX 42, RVol 0.9) |
| 13 | **ARM** | 192.99 | - | **-** | 23 | - | POS +$1.4M | 189.53 | 200 | 200 | -$343k | - | out (clean 28, ADX 51, RVol 0.5) |
| 14 | **SPY** | 755.39 | - | **-** | 22 | - | NEG -$4.4B | 760.58 | 760 | 750 | +$19.1M | +$207k bull / -$101k bear | out (clean 32, ADX 46, RVol 0.5) |
| 15 | **TSLA** | 393.08 | - | **-** | 22 | - | POS +$417.1M | - | 400 | 380 | -$6.1M | +$0 bull / -$921k bear | out (clean 32, ADX 43, RVol 0.9) |
| 16 | **META** | 637.97 | - | **-** | 22 | - | POS +$235.8M | 624.09 | 650 | 625 | +$3.2M | +$370k bull / -$101k bear | out (clean 30, ADX 24, RVol 1.0) |
| 17 | **SMH** | 500.02 | - | **-** | 21 | - | NEG -$71.0M | - | 500 | 475 | +$330k | +$271k bull / -$240k bear | out (clean 31, ADX 35, RVol 1.1) |
| 18 | **AAPL** | 353.30 | - | **-** | 21 | - | POS +$1.3B | 340.05 | 355 | 350 | -$587k | +$688k bull / -$124k bear | out (clean 27, ADX 41, RVol 1.5) |
| 19 | **SMCI** | 29.74 | - | **-** | 21 | - | POS +$10.4M | - | 30 | 30 | -$218k | - | out (clean 32, ADX 44, RVol 0.9) |
| 20 | **QQQ** | 685.35 | - | **-** | 19 | - | NEG -$771.3M | 689.26 | 700 | 680 | +$630k | +$0 bull / -$8.0M bear | out (clean 32, ADX 46, RVol 0.6) |
| 21 | **CRM** | 215.40 | - | **-** | 17 | - | NEG -$10.9M | - | 230 | 220 | -$29k | - | out (clean 31, ADX 31, RVol 1.2) |
| 22 | **COIN** | 134.63 | - | **-** | 15 | - | POS +$16.0M | 126.92 | 137 | 135 | +$183k | - | out (clean 29, ADX 31, RVol 0.6) |
| 23 | **MSTR** | 121.38 | - | **-** | 15 | - | NEG -$9.0M | 123.44 | 133 | 120 | +$118k | +$228k bull / +$0 bear | out (clean 28, ADX 15, RVol 0.7) |
| 24 | **SHOP** | 148.55 | - | **-** | 14 | - | POS +$2.9M | 144.55 | 150 | 140 | -$3k | - | out (clean 33, ADX 44, RVol 0.4) |
| 25 | **HOOD** | 83.11 | - | **-** | 13 | - | POS +$10.3M | 78.67 | 85 | 80 | -$137k | - | out (clean 32, ADX 30, RVol 1.0) |
| 26 | **NFLX** | 63.37 | - | **-** | 11 | - | NEG -$13.9M | 64.6 | 65 | 65 | +$115k | - | out (clean 27, ADX 18, RVol 1.1) |
| 27 | **UBER** | 69.36 | - | **-** | 7 | - | POS +$8.8M | 68.27 | 70 | 70 | +$2k | - | out (clean 33, ADX 23, RVol 0.7) |

## Big prints this scan (152)
- **MU** CALL 800 2026-11-13 (2DTE): 250 @ 14.90 = **+$372k** SELL | vol 4,217 / OI 5,495
- **SMH** CALL 480 2026-11-13 (2DTE): 100 @ 24.08 = **+$241k** BUY | vol 169 / OI 753
- **MU** CALL 770 2026-11-11 (0DTE): 100 @ 19.15 = **+$192k** SELL | vol 5,605 / OI 1,346
- **QQQ** CALL 680 2026-11-11 (0DTE): 331 @ 5.60 = **+$185k** SELL | vol 4,869 / OI 2,402
- **SPY** CALL 738 2026-11-12 (1DTE): 85 @ 18.29 = **+$155k** MID | vol 87 / OI 200
- **AMD** CALL 510 2026-11-13 (2DTE): 50 @ 29.55 = **+$148k** SELL | vol 507 / OI 1,364
- **AMD** CALL 530 2026-11-13 (2DTE): 80 @ 16.50 = **+$132k** SELL | vol 1,544 / OI 1,882
- **MU** PUT 770 2026-11-11 (0DTE): 400 @ 2.93 = **+$117k** BUY | vol 6,235 / OI 34
- **MU** CALL 775 2026-11-13 (2DTE): 48 @ 24.30 = **+$117k** SELL | vol 1,503 / OI 466
- **MU** CALL 775 2026-11-13 (2DTE): 45 @ 25.05 = **+$113k** SELL | vol 1,503 / OI 466
- **SPY** CALL 758 2026-11-12 (1DTE): 500 @ 2.13 = **+$106k** BUY | vol 5,638 / OI 940
- **NVDA** CALL 175 2026-11-16 (5DTE): 314 @ 3.35 = **+$105k** BUY | vol 4,461 / OI 1,029
- **QQQ** CALL 695 2026-11-18 (7DTE): 200 @ 5.23 = **+$105k** SELL | vol 352 / OI 259
- **NVDA** CALL 170 2026-11-18 (7DTE): 100 @ 9.85 = **+$98k** BUY | vol 965 / OI 224
- **NVDA** CALL 170 2026-11-18 (7DTE): 100 @ 9.70 = **+$97k** MID | vol 965 / OI 224

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 760 2026-11-17 (6DTE): 516 traded vs OI 292
- **SPY** PUT 759 2026-11-12 (1DTE): 503 traded vs OI 243
- **SPY** PUT 749 2026-11-13 (2DTE): 1,412 traded vs OI 1,348
- **SPY** PUT 708 2026-11-12 (1DTE): 1,105 traded vs OI 720
- **SPY** CALL 810 2026-11-18 (7DTE): 602 traded vs OI 50
- **QQQ** CALL 685 2026-11-12 (1DTE): 2,154 traded vs OI 1,947
- **QQQ** PUT 642 2026-11-11 (0DTE): 600 traded vs OI 268
- **QQQ** CALL 684 2026-11-12 (1DTE): 1,026 traded vs OI 985
- **QQQ** CALL 703 2026-11-16 (5DTE): 1,196 traded vs OI 206
- **QQQ** PUT 668 2026-11-12 (1DTE): 506 traded vs OI 192
- **QQQ** PUT 658 2026-11-12 (1DTE): 633 traded vs OI 372
- **QQQ** CALL 692 2026-11-13 (2DTE): 612 traded vs OI 579
- **QQQ** PUT 670 2026-11-12 (1DTE): 1,513 traded vs OI 1,495
- **QQQ** PUT 622 2026-11-20 (9DTE): 2,105 traded vs OI 86
- **IWM** PUT 274 2026-11-13 (2DTE): 1,194 traded vs OI 1,142

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
