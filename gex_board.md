# GEX + FLOW SCAN - Wed Nov 11, 10:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (9)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:35 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.76 | 1.00 | +43% (4m) | **+32%** | +343% | 527.5 |
| 10:20 | **AVGO** | **CALLS** | TREND + FLOW | 11/11 355C | 0.71 | 0.41 | +8% (8m) | **-42%** | +280% | 356.78 |
| 10:15 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.65 | 0.70 | +14% (3m) | **+8%** | +66% | 282.84 |
| 10:05 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 175C | 0.76 | 1.12 | +82% (34m) | **+47%** | +58% | 175 hit |
| 09:50 | **GOOGL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 292.5C | 0.51 | 0.44 | +39% (28m) | **-14%** | +82% | 291.86 |
| 09:45 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.68 | 0.70 | +85% (6m) | **+3%** | +68% | 282.96 |
| 09:45 | **QQQ** | **CALLS** | FLOW SURGE | 11/11 690C | 0.63 | 0.85 | +62% (51m) | **+35%** | +171% | 689.78 |
| 09:39 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 693C | 0.52 | 0.29 | -10% (0m) | **-44%** (done) | +92% | 690.43 |
| 09:39 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 760C | 0.53 | 0.17 | -2% (0m) | **-68%** (done) | +79% | 758.82 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:40:08 ET, last candle SPY 10:39, QQQ 10:39 | no errors
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
| 1 | **DELL** | 372.44 | FLOW SURGE | **PUTS** | 59 | none: 29 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$225k | 384.46 | 380 | 340 | -$2.4M | +$0 bull / -$305k bear | LONG (clean 36, ADX 61, RVol 2.3) |
| 2 | **MSFT** | 522.09 | FLOW SURGE | **CALLS** | 47 | none: 166 calls 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (68 contracts' greeks worked out here) | POS +$76.2M | 514.87 | 535 | 520 | +$16.2M | +$608k bull / -$119k bear | out (clean 32, ADX 44, RVol 1.7) |
| 3 | **MU** | 807.48 | FLOW SURGE | **PUTS** | 47 | none: 153 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (65 contracts' greeks worked out here) | POS +$156.4M | - | 800 | 800 | -$149.1M | +$0 bull / -$9.0M bear | LONG (clean 33, ADX 61, RVol 1.3) |
| 4 | **AVGO** | 349.41 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 45 | none: 112 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (46 contracts' greeks worked out here) | POS +$95.5M | - | 350 | 340 | +$4.5M | +$100k bull / -$33k bear | out (clean 35, ADX 51, RVol 1.1) |
| 5 | **AMZN** | 266.63 | FLOW SURGE | **CALLS** | 41 | 11/11 267.5C @ 0.71 (delta 0.38) = est +262% at 270 | POS +$417.1M | - | 270 | 265 | +$6.9M | +$52k bull / +$0 bear | out (clean 33, ADX 31, RVol 1.4) |
| 6 | **SMCI** | 30.39 | FLOW SURGE | **PUTS** | 41 | none: 12 puts 0-7DTE > 3 priced 0.40-0.80 > 3 delta 0.2+ > 3 spread ok > 3 liquid > best one only +15% at the target (needs +20%) | POS +$11.7M | - | 30 | 30 | -$385k | +$0 bull / -$36k bear | out (clean 32, ADX 54, RVol 0.9) |
| 7 | **AMD** | 544.20 | TREND (flow not with it) | **CALLS** | 36 | none: 176 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (70 contracts' greeks worked out here) | POS +$123.8M | - | 550 | 500 | -$41.6M | +$131k bull / -$3.6M bear | LONG (clean 33, ADX 40, RVol 1.1) |
| 8 | **MSTR** | 122.33 | FLIP CROSS up into positive gamma | **CALLS** | 28 | none: 24 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$639k | 122.02 | 133 | 120 | +$142k | +$0 bull / -$86k bear | out (clean 28, ADX 16, RVol 0.7) |
| 9 | **PLTR** | 172.63 | - | **-** | 27 | - | POS +$74.2M | - | 170 | 180 | +$1.4M | +$0 bull / -$100k bear | out (clean 30, ADX 42, RVol 0.3) |
| 10 | **SMH** | 505.20 | - | **-** | 26 | - | NEG -$72.6M | - | 500 | 475 | -$1.4M | +$0 bull / -$51k bear | out (clean 31, ADX 40, RVol 1.7) |
| 11 | **ARM** | 197.98 | - | **-** | 26 | - | POS +$3.9M | - | 200 | 200 | -$664k | - | out (clean 29, ADX 59, RVol 0.8) |
| 12 | **TSLA** | 392.58 | - | **-** | 23 | - | POS +$422.5M | - | 400 | 380 | -$15.1M | +$1.4M bull / -$1.9M bear | out (clean 33, ADX 53, RVol 1.0) |
| 13 | **META** | 635.17 | - | **-** | 23 | - | POS +$155.6M | 625.48 | 650 | 625 | +$6.1M | +$336k bull / +$0 bear | out (clean 31, ADX 23, RVol 0.7) |
| 14 | **BABA** | 101.54 | - | **-** | 23 | - | NEG -$17.0M | 106.87 | 110 | 101 | +$412k | - | out (clean 29, ADX 32, RVol 1.1) |
| 15 | **QQQ** | 688.10 | - | **-** | 22 | - | NEG -$344.6M | 689.74 | 700 | 680 | -$33.8M | +$0 bull / -$1.9M bear | out (clean 32, ADX 49, RVol 0.5) |
| 16 | **GOOGL** | 290.93 | - | **-** | 22 | - | POS +$42.8M | 288.9 | 300 | 290 | +$722k | +$103k bull / +$0 bear | out (clean 28, ADX 47, RVol 0.7) |
| 17 | **ORCL** | 126.81 | - | **-** | 22 | - | NEG -$550k | 127.49 | 130 | 125 | +$379k | +$0 bull / -$226k bear | out (clean 28, ADX 48, RVol 0.7) |
| 18 | **AAPL** | 353.37 | - | **-** | 20 | - | POS +$1.4B | 341.22 | 355 | 350 | -$1.0M | +$114k bull / -$84k bear | out (clean 27, ADX 45, RVol 0.7) |
| 19 | **SPY** | 756.93 | - | **-** | 19 | - | NEG -$3.3B | 760.72 | 760 | 750 | +$4.9M | +$0 bull / -$1.5M bear | out (clean 31, ADX 48, RVol 0.5) |
| 20 | **IWM** | 282.20 | - | **-** | 19 | - | NEG -$217.3M | 282.8 | 285 | 270 | -$823k | +$0 bull / -$123k bear | out (clean 34, ADX 39, RVol 0.4) |
| 21 | **NVDA** | 174.82 | - | **-** | 18 | - | NEG -$171.5M | - | 180 | 175 | -$2.8M | +$0 bull / -$2.4M bear | out (clean 34, ADX 30, RVol 1.0) |
| 22 | **HOOD** | 84.30 | - | **-** | 15 | - | POS +$13.8M | - | 85 | 85 | -$298k | - | out (clean 32, ADX 34, RVol 0.7) |
| 23 | **UBER** | 69.28 | - | **-** | 10 | - | POS +$8.0M | 68.32 | 70 | 70 | +$14k | - | out (clean 32, ADX 24, RVol 0.6) |
| 24 | **CRM** | 216.04 | - | **-** | 10 | - | NEG -$11.5M | - | 230 | 220 | -$19k | - | out (clean 31, ADX 27, RVol 0.6) |
| 25 | **COIN** | 136.78 | - | **-** | 9 | - | POS +$22.7M | - | 141 | 135 | +$56k | - | out (clean 28, ADX 30, RVol 1.0) |
| 26 | **SHOP** | 147.88 | - | **-** | 9 | - | POS +$2.4M | 144.74 | 150 | 140 | +$1k | - | out (clean 33, ADX 39, RVol 0.2) |
| 27 | **NFLX** | 63.42 | - | **-** | 6 | - | NEG -$15.3M | 64.57 | 65 | 65 | +$61k | - | out (clean 26, ADX 14, RVol 0.8) |

## Big prints this scan (135)
- **SPY** PUT 760 2026-11-13 (2DTE): 1,837 @ 5.85 = **+$1.1M** BUY | vol 2,828 / OI 6,054
- **MU** CALL 770 2026-11-11 (0DTE): 100 @ 29.25 = **+$292k** SELL | vol 6,398 / OI 1,346
- **MU** CALL 775 2026-11-11 (0DTE): 100 @ 24.85 = **+$248k** SELL | vol 5,367 / OI 627
- **AMD** CALL 522.5 2026-11-13 (2DTE): 100 @ 24.50 = **+$245k** SELL | vol 530 / OI 248
- **NVDA** CALL 180 2026-11-18 (7DTE): 400 @ 5.45 = **+$218k** SELL | vol 3,446 / OI 2,150
- **MU** CALL 800 2026-11-13 (2DTE): 89 @ 19.60 = **+$174k** SELL | vol 7,602 / OI 5,495
- **TSLA** CALL 380 2026-11-11 (0DTE): 100 @ 14.00 = **+$140k** BUY | vol 3,156 / OI 2,178
- **QQQ** PUT 685 2026-11-13 (2DTE): 250 @ 5.28 = **+$132k** BUY | vol 8,522 / OI 23,913
- **QQQ** PUT 686 2026-11-12 (1DTE): 318 @ 4.14 = **+$132k** BUY | vol 5,394 / OI 281
- **QQQ** PUT 685 2026-11-13 (2DTE): 250 @ 5.11 = **+$128k** BUY | vol 8,522 / OI 23,913
- **QQQ** CALL 685 2026-11-11 (0DTE): 496 @ 2.41 = **+$120k** SELL | vol 54,227 / OI 1,366
- **TSLA** PUT 402.5 2026-11-11 (0DTE): 120 @ 9.25 = **+$111k** SELL | vol 328 / OI 121
- **MU** CALL 800 2026-11-13 (2DTE): 49 @ 21.21 = **+$104k** SELL | vol 7,602 / OI 5,495
- **TSLA** CALL 385 2026-11-16 (5DTE): 82 @ 12.50 = **+$102k** BUY | vol 740 / OI 289
- **MU** CALL 800 2026-11-13 (2DTE): 48 @ 21.21 = **+$102k** SELL | vol 7,602 / OI 5,495

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 752 2026-11-19 (8DTE): 780 traded vs OI 205
- **SPY** PUT 755 2026-11-19 (8DTE): 792 traded vs OI 274
- **IWM** PUT 282 2026-11-16 (5DTE): 822 traded vs OI 129
- **IWM** CALL 285 2026-11-17 (6DTE): 791 traded vs OI 188
- **IWM** CALL 285 2026-11-16 (5DTE): 741 traded vs OI 624
- **IWM** CALL 286 2026-11-27 (16DTE): 780 traded vs OI 532
- **SMH** PUT 470 2026-11-13 (2DTE): 1,174 traded vs OI 592
- **NVDA** CALL 167.5 2026-11-20 (9DTE): 511 traded vs OI 131
- **NVDA** CALL 187.5 2026-11-11 (0DTE): 5,268 traded vs OI 5,226
- **AMD** PUT 545 2026-11-11 (0DTE): 501 traded vs OI 12
- **META** PUT 637.5 2026-11-13 (2DTE): 507 traded vs OI 107
- **META** PUT 615 2026-11-11 (0DTE): 822 traded vs OI 813
- **AMZN** PUT 240 2026-11-20 (9DTE): 506 traded vs OI 0
- **AMZN** PUT 272.5 2026-11-13 (2DTE): 587 traded vs OI 585
- **MSFT** CALL 522.5 2026-11-11 (0DTE): 1,314 traded vs OI 31

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
