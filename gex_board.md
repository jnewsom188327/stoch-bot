# GEX + FLOW SCAN - Wed Nov 11, 03:15 PM ET
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
Last 1m check 15:15:08 ET, last candle SPY 15:14, QQQ 15:14 | no errors
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
| 1 | **MSFT** | 519.79 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 37 | 11/11 520C @ 0.67 (delta 0.46) = est +103% at 521.38 | POS +$627k | 519.53 | 535 | 520 | +$14.7M | +$345k bull / +$0 bear | out (clean 32, ADX 17, RVol 0.5) |
| 2 | **META** | 634.72 | PINNED between the walls (positive gamma) - chop | **-** | 32 | - | POS +$178.8M | 628.41 | 635 | 635 | +$5.6M | +$52k bull / +$0 bear | out (clean 30, ADX 43, RVol 0.3) |
| 3 | **IWM** | 283.00 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 25 | none: 340 puts 0-7DTE > 14 priced 0.40-0.80 > 6 delta 0.2+ > 6 spread ok > 6 liquid > best one only +10% at the target (needs +20%) (152 contracts' greeks worked out here) | POS +$194.3M | 282.67 | 283 | 270 | -$5.1M | - | out (clean 35, ADX 24, RVol 0.3) |
| 4 | **AMD** | 556.53 | - | **-** | 23 | - | POS +$187.2M | - | 550 | 550 | -$94.3M | +$7.6M bull / +$0 bear | out (clean 35, ADX 32, RVol 0.4) |
| 5 | **AVGO** | 347.51 | - | **-** | 23 | - | POS +$98.0M | - | 350 | 340 | +$9.2M | +$174k bull / -$100k bear | out (clean 37, ADX 37, RVol 0.7) |
| 6 | **MU** | 815.58 | - | **-** | 21 | - | POS +$164.0M | - | 800 | 850 | -$199.9M | +$2.1M bull / -$738k bear | out (clean 34, ADX 23, RVol 0.4) |
| 7 | **QQQ** | 691.44 | - | **-** | 19 | - | POS +$570.1M | 689.32 | 700 | 680 | -$135.6M | +$814k bull / +$0 bear | out (clean 33, ADX 30, RVol 0.3) |
| 8 | **SMH** | 509.12 | - | **-** | 19 | - | NEG -$28.6M | 512.85 | 500 | 500 | -$2.1M | +$354k bull / +$0 bear | out (clean 32, ADX 34, RVol 0.4) |
| 9 | **SPY** | 760.27 | - | **-** | 18 | - | NEG -$833.9M | 761.31 | 760 | 750 | -$122.5M | +$607k bull / +$0 bear | out (clean 34, ADX 27, RVol 0.2) |
| 10 | **NVDA** | 174.98 | - | **-** | 18 | - | NEG -$209.4M | 178.93 | 175 | 175 | -$21.4M | +$851k bull / -$442k bear | out (clean 35, ADX 30, RVol 0.4) |
| 11 | **MSTR** | 121.77 | - | **-** | 18 | - | NEG -$7.0M | 123.63 | 133 | 120 | +$1.8M | +$25k bull / +$0 bear | out (clean 28, ADX 22, RVol 0.6) |
| 12 | **SHOP** | 149.28 | - | **-** | 17 | - | POS +$3.4M | 145.52 | 150 | 140 | -$478k | - | out (clean 33, ADX 14, RVol 0.3) |
| 13 | **AAPL** | 354.96 | PINNED between the walls (positive gamma) - chop | **-** | 16 | - | POS +$3.4B | 342.88 | 355 | 355 | +$506k | - | out (clean 28, ADX 22, RVol 0.2) |
| 14 | **TSLA** | 391.06 | - | **-** | 15 | - | POS +$447.9M | - | 390 | 380 | -$970k | +$1.5M bull / +$0 bear | out (clean 32, ADX 26, RVol 0.3) |
| 15 | **ORCL** | 129.16 | - | **-** | 15 | - | POS +$12.1M | 121.42 | 130 | 125 | +$325k | +$120k bull / +$0 bear | out (clean 30, ADX 20, RVol 0.4) |
| 16 | **ARM** | 204.11 | - | **-** | 14 | - | POS +$6.8M | - | 200 | 200 | -$1.7M | - | out (clean 32, ADX 21, RVol 0.5) |
| 17 | **BABA** | 101.72 | - | **-** | 13 | - | NEG -$17.0M | 106.42 | 110 | 101 | +$358k | - | out (clean 28, ADX 18, RVol 0.2) |
| 18 | **SMCI** | 30.46 | - | **-** | 12 | - | POS +$15.6M | - | 30 | 30 | -$585k | - | out (clean 33, ADX 34, RVol 0.3) |
| 19 | **DELL** | 378.30 | - | **-** | 11 | - | POS +$876k | 363.33 | 400 | 400 | -$2.3M | - | out (clean 38, ADX 37, RVol 0.4) |
| 20 | **NFLX** | 64.22 | - | **-** | 9 | - | NEG -$3.6M | 64.48 | 65 | 65 | -$254k | - | out (clean 27, ADX 27, RVol 0.8) |
| 21 | **PLTR** | 172.56 | - | **-** | 8 | - | POS +$77.9M | - | 170 | 170 | +$1.5M | - | out (clean 29, ADX 19, RVol 0.3) |
| 22 | **HOOD** | 85.26 | - | **-** | 7 | - | POS +$17.6M | - | 85 | 85 | -$576k | - | out (clean 35, ADX 18, RVol 0.4) |
| 23 | **UBER** | 71.07 | - | **-** | 7 | - | POS +$20.8M | 68.56 | 70 | 70 | -$14k | - | out (clean 32, ADX 30, RVol 0.5) |
| 24 | **CRM** | 217.40 | - | **-** | 7 | - | NEG -$11.5M | - | 230 | 220 | -$56k | - | out (clean 29, ADX 12, RVol 0.5) |
| 25 | **AMZN** | 266.29 | - | **-** | 6 | - | POS +$386.0M | - | 270 | 265 | +$4.0M | - | out (clean 31, ADX 15, RVol 0.5) |
| 26 | **GOOGL** | 293.84 | - | **-** | 6 | - | POS +$99.9M | 289.61 | 300 | 290 | -$719k | - | out (clean 30, ADX 25, RVol 0.4) |
| 27 | **COIN** | 137.14 | - | **-** | 5 | - | POS +$25.4M | - | 141 | 135 | +$39k | - | out (clean 29, ADX 25, RVol 0.3) |

## Big prints this scan (54)
- **AMD** PUT 547.5 2026-11-13 (2DTE): 517 @ 8.75 = **+$452k** SELL | vol 1,669 / OI 42
- **AMD** CALL 565 2026-11-13 (2DTE): 197 @ 10.85 = **+$214k** BUY | vol 7,430 / OI 457
- **AMD** CALL 565 2026-11-13 (2DTE): 190 @ 10.85 = **+$206k** BUY | vol 7,430 / OI 457
- **MU** PUT 825 2026-11-11 (0DTE): 200 @ 8.40 = **+$168k** SELL | vol 21,284 / OI 75
- **SMH** CALL 500 2026-11-13 (2DTE): 106 @ 14.55 = **+$154k** BUY | vol 2,665 / OI 4,456
- **AMD** CALL 572.5 2026-11-13 (2DTE): 190 @ 7.85 = **+$149k** BUY | vol 1,630 / OI 298
- **AMD** CALL 565 2026-11-13 (2DTE): 136 @ 10.85 = **+$148k** BUY | vol 7,430 / OI 457
- **AMD** CALL 572.5 2026-11-13 (2DTE): 179 @ 7.85 = **+$141k** BUY | vol 1,630 / OI 298
- **SPY** PUT 755 2026-11-13 (2DTE): 750 @ 1.40 = **+$105k** SELL | vol 30,682 / OI 9,468
- **SPY** PUT 755 2026-11-13 (2DTE): 750 @ 1.38 = **+$104k** SELL | vol 30,682 / OI 9,468
- **TSLA** PUT 390 2026-11-13 (2DTE): 166 @ 4.60 = **+$76k** SELL | vol 11,183 / OI 754
- **TSLA** PUT 390 2026-11-13 (2DTE): 166 @ 4.60 = **+$76k** SELL | vol 11,183 / OI 754
- **MSFT** PUT 520 2026-11-13 (2DTE): 149 @ 5.00 = **+$74k** SELL | vol 6,522 / OI 3,792
- **AMD** PUT 547.5 2026-11-13 (2DTE): 83 @ 8.75 = **+$73k** SELL | vol 1,669 / OI 42
- **TSLA** PUT 390 2026-11-13 (2DTE): 157 @ 4.60 = **+$72k** SELL | vol 11,183 / OI 754

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 805 2026-11-16 (5DTE): 898 traded vs OI 218
- **SPY** CALL 773 2026-11-13 (2DTE): 2,516 traded vs OI 2,022
- **SPY** CALL 774 2026-11-18 (7DTE): 572 traded vs OI 136
- **SPY** CALL 780 2026-11-23 (12DTE): 502 traded vs OI 182
- **QQQ** PUT 655 2026-11-12 (1DTE): 1,586 traded vs OI 1,489
- **IWM** PUT 282.5 2026-11-13 (2DTE): 1,563 traded vs OI 1,533
- **TSLA** PUT 387.5 2026-11-16 (5DTE): 501 traded vs OI 61
- **META** PUT 622.5 2026-11-13 (2DTE): 500 traded vs OI 319
- **AMZN** PUT 277.5 2026-11-16 (5DTE): 638 traded vs OI 15
- **AMZN** CALL 287.5 2026-11-20 (9DTE): 853 traded vs OI 352
- **AMZN** PUT 275 2026-11-16 (5DTE): 529 traded vs OI 14
- **GOOGL** CALL 297.5 2026-11-16 (5DTE): 647 traded vs OI 277
- **UBER** CALL 71 2026-11-13 (2DTE): 3,475 traded vs OI 3,446

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
