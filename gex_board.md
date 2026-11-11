# GEX + FLOW SCAN - Wed Nov 11, 10:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:20 | **AVGO** | **CALLS** | TREND + FLOW | 11/11 355C | 0.71 | 0.59 | -17% (0m) | **-17%** | +280% | 356.78 |
| 10:15 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.65 | 0.68 | +14% (3m) | **+5%** | +66% | 282.84 |
| 10:05 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 175C | 0.76 | 0.55 | -1% (0m) | **-28%** | +58% | 175 |
| 09:50 | **GOOGL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 292.5C | 0.51 | 0.62 | +39% (28m) | **+22%** | +82% | 291.86 |
| 09:45 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.68 | 0.68 | +85% (6m) | **+0%** | +68% | 282.96 |
| 09:45 | **QQQ** | **CALLS** | FLOW SURGE | 11/11 690C | 0.63 | 0.57 | +32% (23m) | **-10%** | +171% | 689.78 |
| 09:39 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 693C | 0.52 | 0.18 | -10% (0m) | **-65%** | +92% | 690.43 |
| 09:39 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 760C | 0.53 | 0.14 | -2% (0m) | **-74%** | +79% | 758.82 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:20:08 ET, last candle SPY 10:19, QQQ 10:19 | no errors
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
| 1 | **DELL** | 368.96 | FLOW SURGE | **PUTS** | 58 | none: 30 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$734k | - | 380 | 340 | -$1.7M | +$0 bull / -$71k bear | LONG (clean 35, ADX 54, RVol 2.3) |
| 2 | **NVDA** | 172.81 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 55 | 11/11 175C @ 0.53 (delta 0.26) = est +117% at 175 | NEG -$195.4M | - | 180 | 170 | +$8.5M | +$3.0M bull / -$485k bear | LONG (clean 34, ADX 26, RVol 0.8) |
| 3 | **AVGO** | 350.47 | TREND + FLOW | **CALLS** | 52 | 11/11 355C @ 0.71 (delta 0.21) = est +280% at 356.78 | POS +$87.2M | - | 350 | 340 | +$3.0M | +$316k bull / +$0 bear | LONG (clean 35, ADX 50, RVol 1.8) |
| 4 | **MSFT** | 522.43 | FLOW SURGE | **CALLS** | 49 | none: 162 calls 0-7DTE > 13 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (82 contracts' greeks worked out here) | POS +$82.6M | 515.38 | 535 | 520 | +$9.4M | +$676k bull / +$0 bear | out (clean 31, ADX 35, RVol 1.6) |
| 5 | **IWM** | 282.01 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 48 | 11/11 282C @ 0.61 (delta 0.51) = est +68% at 282.86 | NEG -$381.9M | 282.86 | 285 | 270 | +$564k | - | LONG (clean 35, ADX 38, RVol 1.1) |
| 6 | **MU** | 797.43 | FLOW SURGE | **PUTS** | 48 | none: 157 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (66 contracts' greeks worked out here) | POS +$166.1M | - | 800 | 800 | -$115.9M | +$0 bull / -$12.3M bear | out (clean 33, ADX 54, RVol 1.7) |
| 7 | **AMD** | 538.38 | FLOW SURGE | **PUTS** | 44 | none: 172 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (80 contracts' greeks worked out here) | POS +$135.0M | - | 550 | 500 | -$43.0M | +$149k bull / -$6.6M bear | out (clean 33, ADX 35, RVol 1.7) |
| 8 | **SMCI** | 29.94 | PINNED between the walls (positive gamma) - chop | **-** | 37 | - | POS +$10.7M | - | 30 | 30 | -$275k | - | out (clean 32, ADX 46, RVol 0.9) |
| 9 | **AMZN** | 268.46 | - | **-** | 30 | - | POS +$478.0M | - | 270 | 265 | +$4.9M | +$26k bull / -$94k bear | out (clean 33, ADX 28, RVol 1.1) |
| 10 | **PLTR** | 171.64 | - | **-** | 30 | - | POS +$73.0M | - | 170 | 170 | +$1.6M | +$0 bull / -$51k bear | out (clean 30, ADX 41, RVol 0.4) |
| 11 | **ORCL** | 125.61 | - | **-** | 27 | - | NEG -$2.1M | 128.27 | 130 | 125 | +$947k | +$38k bull / -$26k bear | out (clean 28, ADX 43, RVol 1.0) |
| 12 | **TSLA** | 393.86 | - | **-** | 25 | - | POS +$410.3M | - | 400 | 380 | -$17.0M | +$0 bull / -$2.7M bear | out (clean 33, ADX 46, RVol 1.0) |
| 13 | **META** | 638.06 | - | **-** | 23 | - | POS +$223.3M | 625.96 | 650 | 625 | +$4.2M | +$360k bull / -$58k bear | out (clean 30, ADX 22, RVol 0.8) |
| 14 | **ARM** | 193.90 | - | **-** | 23 | - | POS +$1.9M | 188.98 | 200 | 200 | -$367k | - | out (clean 29, ADX 53, RVol 0.4) |
| 15 | **BABA** | 101.65 | - | **-** | 23 | - | NEG -$16.4M | 106.83 | 110 | 101 | +$291k | - | out (clean 29, ADX 30, RVol 1.2) |
| 16 | **SPY** | 756.18 | - | **-** | 22 | - | NEG -$4.4B | 761.04 | 760 | 750 | +$25.8M | +$324k bull / -$101k bear | out (clean 32, ADX 46, RVol 0.4) |
| 17 | **GOOGL** | 291.38 | - | **-** | 22 | - | POS +$48.4M | 288.86 | 300 | 290 | +$472k | +$208k bull / +$0 bear | out (clean 28, ADX 43, RVol 0.9) |
| 18 | **AAPL** | 353.69 | - | **-** | 21 | - | POS +$1.4B | 341.03 | 355 | 350 | -$821k | +$293k bull / -$42k bear | out (clean 27, ADX 42, RVol 1.2) |
| 19 | **SMH** | 502.02 | - | **-** | 20 | - | NEG -$79.5M | - | 500 | 475 | +$282k | +$271k bull / -$212k bear | out (clean 31, ADX 36, RVol 0.9) |
| 20 | **QQQ** | 686.46 | - | **-** | 19 | - | NEG -$748.6M | 689.7 | 700 | 680 | +$1.8M | +$212k bull / -$2.2M bear | out (clean 32, ADX 46, RVol 0.5) |
| 21 | **MSTR** | 121.00 | - | **-** | 17 | - | NEG -$9.4M | 123.41 | 133 | 120 | +$372k | +$180k bull / +$0 bear | out (clean 28, ADX 15, RVol 0.5) |
| 22 | **CRM** | 214.36 | - | **-** | 16 | - | NEG -$10.9M | - | 195 | 220 | -$27k | - | out (clean 31, ADX 29, RVol 1.4) |
| 23 | **SHOP** | 148.08 | - | **-** | 14 | - | POS +$2.0M | 145.19 | 150 | 140 | -$3k | - | out (clean 33, ADX 43, RVol 0.4) |
| 24 | **COIN** | 134.65 | - | **-** | 12 | - | POS +$16.2M | 127.15 | 137 | 135 | +$137k | - | out (clean 28, ADX 31, RVol 0.6) |
| 25 | **HOOD** | 83.41 | - | **-** | 11 | - | POS +$11.9M | - | 85 | 80 | -$96k | - | out (clean 32, ADX 31, RVol 0.9) |
| 26 | **NFLX** | 63.37 | - | **-** | 9 | - | NEG -$15.2M | 64.56 | 65 | 65 | +$96k | - | out (clean 27, ADX 17, RVol 1.0) |
| 27 | **UBER** | 69.40 | - | **-** | 8 | - | POS +$8.2M | 68.26 | 70 | 70 | +$4k | - | out (clean 32, ADX 23, RVol 0.7) |

## Big prints this scan (185)
- **AMD** PUT 540 2026-11-11 (0DTE): 969 @ 8.30 = **+$804k** BUY | vol 2,401 / OI 20
- **AMD** CALL 530 2026-11-11 (0DTE): 989 @ 7.75 = **+$766k** SELL | vol 6,638 / OI 457
- **AMD** PUT 530 2026-11-11 (0DTE): 969 @ 3.60 = **+$349k** BUY | vol 6,507 / OI 59
- **QQQ** CALL 656 2026-11-17 (6DTE): 67 @ 31.82 = **+$213k** SELL | vol 74 / OI 58
- **QQQ** CALL 655 2026-11-13 (2DTE): 67 @ 31.66 = **+$212k** BUY | vol 170 / OI 2,108
- **TSLA** CALL 385 2026-11-11 (0DTE): 290 @ 7.10 = **+$206k** SELL | vol 8,612 / OI 2,160
- **AMD** CALL 525 2026-11-13 (2DTE): 96 @ 21.00 = **+$202k** SELL | vol 1,026 / OI 1,343
- **TSLA** CALL 380 2026-11-16 (5DTE): 120 @ 14.45 = **+$173k** SELL | vol 492 / OI 738
- **AMD** CALL 522.5 2026-11-11 (0DTE): 96 @ 15.95 = **+$153k** SELL | vol 802 / OI 258
- **NVDA** CALL 170 2026-11-18 (7DTE): 157 @ 9.68 = **+$152k** SELL | vol 1,300 / OI 224
- **AMD** CALL 540 2026-11-11 (0DTE): 299 @ 4.97 = **+$149k** BUY | vol 8,166 / OI 507
- **MU** CALL 800 2026-11-11 (0DTE): 280 @ 4.90 = **+$137k** SELL | vol 28,772 / OI 2,486
- **AMD** CALL 540 2026-11-13 (2DTE): 100 @ 12.15 = **+$122k** SELL | vol 1,794 / OI 1,314
- **SPY** PUT 756 2026-11-12 (1DTE): 450 @ 2.60 = **+$117k** SELL | vol 9,409 / OI 213
- **MU** CALL 775 2026-11-13 (2DTE): 39 @ 30.00 = **+$117k** SELL | vol 1,689 / OI 466

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 759 2026-11-16 (5DTE): 521 traded vs OI 147
- **SPY** PUT 706 2026-11-12 (1DTE): 621 traded vs OI 409
- **SPY** PUT 740 2026-11-12 (1DTE): 2,845 traded vs OI 2,091
- **SPY** PUT 736 2026-11-12 (1DTE): 615 traded vs OI 467
- **SPY** PUT 707 2026-11-12 (1DTE): 2,016 traded vs OI 1,880
- **SPY** PUT 725 2026-11-18 (7DTE): 513 traded vs OI 420
- **SPY** CALL 755 2026-11-18 (7DTE): 878 traded vs OI 856
- **QQQ** CALL 693 2026-11-12 (1DTE): 1,347 traded vs OI 1,331
- **QQQ** CALL 686 2026-11-13 (2DTE): 566 traded vs OI 454
- **QQQ** PUT 634 2026-11-11 (0DTE): 715 traded vs OI 77
- **QQQ** PUT 667 2026-11-13 (2DTE): 599 traded vs OI 588
- **QQQ** PUT 646 2026-11-18 (7DTE): 1,647 traded vs OI 41
- **IWM** PUT 284 2026-11-11 (0DTE): 529 traded vs OI 509
- **SMH** PUT 497.5 2026-11-11 (0DTE): 503 traded vs OI 11
- **NVDA** CALL 185 2026-11-13 (2DTE): 11,501 traded vs OI 11,002

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
