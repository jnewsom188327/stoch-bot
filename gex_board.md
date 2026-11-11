# GEX + FLOW SCAN - Wed Nov 11, 10:35 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (9)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:35 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.76 | 0.73 | -4% (0m) | **-4%** | +343% | 527.5 |
| 10:20 | **AVGO** | **CALLS** | TREND + FLOW | 11/11 355C | 0.71 | 0.52 | +8% (8m) | **-27%** | +280% | 356.78 |
| 10:15 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.65 | 0.64 | +14% (3m) | **-2%** | +66% | 282.84 |
| 10:05 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 175C | 0.76 | 0.79 | +37% (24m) | **+4%** | +58% | 175 |
| 09:50 | **GOOGL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 292.5C | 0.51 | 0.46 | +39% (28m) | **-10%** | +82% | 291.86 |
| 09:45 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.68 | 0.64 | +85% (6m) | **-6%** | +68% | 282.96 |
| 09:45 | **QQQ** | **CALLS** | FLOW SURGE | 11/11 690C | 0.63 | 0.78 | +37% (43m) | **+24%** | +171% | 689.78 |
| 09:39 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 693C | 0.52 | 0.18 | -10% (0m) | **-65%** | +92% | 690.43 |
| 09:39 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 760C | 0.53 | 0.19 | -2% (0m) | **-64%** | +79% | 758.82 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:35:08 ET, last candle SPY 10:34, QQQ 10:33 | no errors
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
| 1 | **MSFT** | 519.87 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 63 | 11/11 525C @ 0.76 (delta 0.21) = est +343% at 527.5 | POS +$64.2M | 514.34 | 535 | 520 | +$19.3M | +$721k bull / +$0 bear | out (clean 32, ADX 44, RVol 1.7) |
| 2 | **DELL** | 371.13 | FLOW SURGE | **PUTS** | 59 | none: 30 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | NEG -$14k | 379.03 | 380 | 340 | -$2.2M | +$0 bull / -$196k bear | LONG (clean 36, ADX 59, RVol 2.3) |
| 3 | **AMD** | 542.48 | TREND (flow not with it) | **CALLS** | 49 | none: 172 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (81 contracts' greeks worked out here) | POS +$135.4M | - | 550 | 500 | -$41.2M | +$4.7M bull / -$2.9M bear | LONG (clean 33, ADX 39, RVol 1.5) |
| 4 | **MU** | 804.73 | FLOW SURGE | **PUTS** | 49 | none: 157 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (64 contracts' greeks worked out here) | POS +$155.6M | - | 800 | 800 | -$140.1M | +$1.3M bull / -$12.6M bear | LONG (clean 33, ADX 59, RVol 1.5) |
| 5 | **BABA** | 101.39 | FLOW SURGE | **CALLS** | 47 | none: 20 calls 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +13% at the target (needs +20%) | NEG -$16.3M | 106.68 | 110 | 101 | +$397k | +$27k bull / +$0 bear | out (clean 29, ADX 32, RVol 1.1) |
| 6 | **AVGO** | 350.08 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 45 | none: 112 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (47 contracts' greeks worked out here) | POS +$96.9M | - | 350 | 340 | +$4.4M | +$153k bull / -$33k bear | out (clean 35, ADX 51, RVol 1.0) |
| 7 | **AMZN** | 266.43 | FLOW SURGE | **CALLS** | 42 | 11/11 267.5C @ 0.75 (delta 0.36) = est +246% at 270 | POS +$417.4M | - | 270 | 265 | +$6.7M | +$220k bull / +$0 bear | out (clean 33, ADX 30, RVol 1.4) |
| 8 | **SMCI** | 30.22 | FLOW SURGE | **PUTS** | 42 | none: 12 puts 0-7DTE > 2 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +10% at the target (needs +20%) (1 contracts' greeks worked out here) | POS +$11.6M | - | 30 | 30 | -$371k | +$0 bull / -$36k bear | out (clean 32, ADX 52, RVol 1.0) |
| 9 | **PLTR** | 172.47 | - | **-** | 27 | - | POS +$72.7M | - | 170 | 180 | +$1.4M | +$0 bull / -$100k bear | out (clean 30, ADX 41, RVol 0.2) |
| 10 | **ARM** | 197.56 | - | **-** | 25 | - | POS +$3.9M | - | 200 | 200 | -$532k | - | out (clean 29, ADX 58, RVol 0.7) |
| 11 | **SMH** | 504.21 | - | **-** | 24 | - | NEG -$60.7M | - | 500 | 475 | -$1.3M | +$0 bull / -$500k bear | out (clean 31, ADX 39, RVol 1.1) |
| 12 | **TSLA** | 394.27 | - | **-** | 24 | - | POS +$424.3M | - | 400 | 380 | -$21.7M | +$450k bull / -$2.9M bear | out (clean 33, ADX 52, RVol 0.9) |
| 13 | **ORCL** | 126.55 | - | **-** | 24 | - | NEG -$936k | 128.02 | 130 | 125 | +$724k | +$35k bull / +$0 bear | out (clean 28, ADX 47, RVol 0.8) |
| 14 | **META** | 635.13 | - | **-** | 23 | - | POS +$158.2M | 625.75 | 650 | 625 | +$5.6M | +$510k bull / +$0 bear | out (clean 30, ADX 23, RVol 0.7) |
| 15 | **GOOGL** | 290.88 | - | **-** | 22 | - | POS +$38.2M | 289.26 | 300 | 290 | +$810k | +$103k bull / +$0 bear | out (clean 28, ADX 46, RVol 0.8) |
| 16 | **QQQ** | 687.16 | - | **-** | 21 | - | NEG -$351.0M | 689.34 | 700 | 680 | -$25.8M | +$681k bull / -$1.6M bear | out (clean 32, ADX 48, RVol 0.5) |
| 17 | **AAPL** | 353.32 | - | **-** | 21 | - | POS +$1.4B | 341.15 | 355 | 350 | -$1.2M | +$0 bull / -$84k bear | out (clean 27, ADX 45, RVol 0.8) |
| 18 | **SPY** | 756.56 | - | **-** | 19 | - | NEG -$3.6B | 760.73 | 760 | 750 | +$6.3M | +$149k bull / -$434k bear | out (clean 31, ADX 48, RVol 0.4) |
| 19 | **NVDA** | 173.93 | - | **-** | 17 | - | NEG -$181.5M | 184.1 | 180 | 175 | -$1.9M | +$148k bull / -$2.1M bear | out (clean 34, ADX 29, RVol 0.8) |
| 20 | **UBER** | 69.36 | - | **-** | 14 | - | POS +$9.1M | 68.26 | 70 | 70 | +$20k | - | out (clean 32, ADX 24, RVol 0.8) |
| 21 | **HOOD** | 83.94 | - | **-** | 13 | - | POS +$13.9M | - | 85 | 85 | -$212k | - | out (clean 32, ADX 33, RVol 0.8) |
| 22 | **COIN** | 135.60 | - | **-** | 10 | - | POS +$21.5M | - | 141 | 135 | +$83k | - | out (clean 28, ADX 29, RVol 0.8) |
| 23 | **CRM** | 215.11 | - | **-** | 10 | - | NEG -$12.3M | - | 230 | 220 | -$16k | - | out (clean 30, ADX 26, RVol 0.6) |
| 24 | **SHOP** | 147.92 | - | **-** | 9 | - | POS +$2.4M | 144.59 | 150 | 140 | +$1k | - | out (clean 33, ADX 40, RVol 0.2) |
| 25 | **IWM** | 282.05 | - | **-** | 8 | - | NEG -$259.5M | 282.83 | 285 | 270 | -$73k | - | out (clean 35, ADX 38, RVol 0.5) |
| 26 | **NFLX** | 63.45 | - | **-** | 7 | - | NEG -$15.2M | 64.59 | 65 | 65 | +$66k | - | out (clean 27, ADX 14, RVol 0.9) |
| 27 | **MSTR** | 121.87 | - | **-** | 5 | - | NEG -$2.0M | 123.32 | 133 | 120 | +$236k | - | out (clean 28, ADX 14, RVol 0.6) |

## Big prints this scan (106)
- **NVDA** CALL 175 2026-11-16 (5DTE): 875 @ 3.25 = **+$284k** SELL | vol 7,055 / OI 1,029
- **TSLA** CALL 390 2026-11-18 (7DTE): 200 @ 11.76 = **+$235k** MID | vol 700 / OI 293
- **TSLA** CALL 390 2026-11-11 (0DTE): 498 @ 4.25 = **+$212k** SELL | vol 76,299 / OI 2,864
- **TSLA** CALL 387.5 2026-11-13 (2DTE): 200 @ 9.90 = **+$198k** SELL | vol 2,160 / OI 1,401
- **MSFT** CALL 500 2026-11-13 (2DTE): 50 @ 25.00 = **+$125k** BUY | vol 212 / OI 126
- **QQQ** PUT 685 2026-11-13 (2DTE): 250 @ 4.99 = **+$125k** BUY | vol 7,917 / OI 23,913
- **QQQ** CALL 685 2026-11-11 (0DTE): 461 @ 2.70 = **+$124k** SELL | vol 49,589 / OI 1,366
- **NVDA** PUT 170 2026-11-13 (2DTE): 526 @ 2.31 = **+$122k** BUY | vol 17,111 / OI 17,981
- **QQQ** PUT 685 2026-11-13 (2DTE): 242 @ 4.98 = **+$121k** BUY | vol 7,917 / OI 23,913
- **AMD** CALL 522.5 2026-11-13 (2DTE): 50 @ 22.94 = **+$115k** SELL | vol 511 / OI 248
- **AMD** CALL 522.5 2026-11-13 (2DTE): 50 @ 22.94 = **+$115k** SELL | vol 511 / OI 248
- **TSLA** PUT 402.5 2026-11-11 (0DTE): 120 @ 9.50 = **+$114k** MID | vol 320 / OI 121
- **MU** PUT 775 2026-11-11 (0DTE): 398 @ 2.73 = **+$109k** BUY | vol 6,147 / OI 201
- **QQQ** PUT 685 2026-11-13 (2DTE): 200 @ 5.17 = **+$103k** BUY | vol 7,917 / OI 23,913
- **MU** CALL 765 2026-11-11 (0DTE): 32 @ 31.13 = **+$100k** SELL | vol 1,941 / OI 310

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 760 2026-11-16 (5DTE): 1,090 traded vs OI 1,032
- **SPY** PUT 731 2026-11-11 (0DTE): 986 traded vs OI 930
- **SPY** CALL 742 2026-11-12 (1DTE): 513 traded vs OI 505
- **SPY** CALL 794 2026-11-17 (6DTE): 600 traded vs OI 199
- **SPY** CALL 757 2026-11-18 (7DTE): 564 traded vs OI 329
- **QQQ** CALL 681 2026-11-12 (1DTE): 512 traded vs OI 345
- **QQQ** PUT 692 2026-11-11 (0DTE): 513 traded vs OI 167
- **QQQ** PUT 683 2026-11-13 (2DTE): 501 traded vs OI 315
- **QQQ** CALL 702 2026-11-12 (1DTE): 715 traded vs OI 712
- **QQQ** CALL 703 2026-11-12 (1DTE): 627 traded vs OI 199
- **QQQ** PUT 670 2026-11-13 (2DTE): 5,880 traded vs OI 5,816
- **SMH** PUT 500 2026-11-11 (0DTE): 734 traded vs OI 70
- **NVDA** PUT 172.5 2026-11-16 (5DTE): 1,227 traded vs OI 1,223
- **NVDA** CALL 170 2026-12-11 (30DTE): 521 traded vs OI 205
- **TSLA** PUT 380 2026-11-16 (5DTE): 716 traded vs OI 697

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
