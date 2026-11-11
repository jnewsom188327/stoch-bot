# GEX + FLOW SCAN - Wed Nov 11, 02:50 PM ET
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
Last 1m check 14:50:08 ET, last candle SPY 14:49, QQQ 14:49 | no errors
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
| 1 | **META** | 635.59 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 39 | none: 204 calls 0-7DTE > 11 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +8% at the target (needs +20%) (83 contracts' greeks worked out here) | POS +$191.2M | 627.63 | 650 | 635 | +$5.0M | +$0 bull / -$35k bear | out (clean 30, ADX 42, RVol 0.6) |
| 2 | **MSFT** | 520.38 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 36 | none: 162 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (64 contracts' greeks worked out here) | POS +$50.4M | 515.95 | 535 | 520 | +$13.3M | +$0 bull / -$162k bear | out (clean 32, ADX 14, RVol 0.5) |
| 3 | **IWM** | 283.09 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 35 | none: 340 puts 0-7DTE > 15 priced 0.40-0.80 > 5 delta 0.2+ > 5 spread ok > 5 liquid > best one only -3% at the target (needs +20%) (156 contracts' greeks worked out here) | POS +$181.6M | 282.76 | 283 | 270 | -$5.2M | +$132k bull / +$0 bear | out (clean 35, ADX 25, RVol 0.3) |
| 4 | **AAPL** | 354.76 | PINNED between the walls (positive gamma) - chop | **-** | 27 | - | POS +$2.7B | 342.08 | 355 | 355 | +$338k | +$40k bull / -$477k bear | out (clean 28, ADX 27, RVol 0.2) |
| 5 | **AMD** | 559.62 | - | **-** | 25 | - | POS +$151.1M | - | 550 | 550 | -$102.8M | +$1.0M bull / -$170k bear | out (clean 34, ADX 38, RVol 0.3) |
| 6 | **MU** | 817.72 | - | **-** | 23 | - | POS +$167.9M | - | 800 | 800 | -$200.1M | +$2.6M bull / -$1.7M bear | out (clean 34, ADX 29, RVol 0.5) |
| 7 | **AVGO** | 348.89 | - | **-** | 22 | - | POS +$105.4M | - | 350 | 350 | +$8.9M | +$186k bull / -$63k bear | out (clean 36, ADX 34, RVol 0.5) |
| 8 | **SPY** | 760.62 | - | **-** | 20 | - | NEG -$748.3M | 761.66 | 760 | 750 | -$133.0M | +$0 bull / -$730k bear | out (clean 34, ADX 33, RVol 0.4) |
| 9 | **QQQ** | 692.47 | - | **-** | 20 | - | POS +$519.0M | 689.91 | 700 | 680 | -$147.7M | +$0 bull / -$863k bear | out (clean 33, ADX 31, RVol 0.4) |
| 10 | **SMH** | 510.77 | - | **-** | 20 | - | NEG -$42.1M | - | 500 | 500 | -$2.6M | +$279k bull / +$0 bear | out (clean 32, ADX 35, RVol 0.5) |
| 11 | **NVDA** | 175.49 | - | **-** | 19 | - | NEG -$168.2M | 178.79 | 175 | 175 | -$22.8M | +$390k bull / -$1.8M bear | out (clean 35, ADX 30, RVol 0.7) |
| 12 | **SHOP** | 149.50 | - | **-** | 18 | - | POS +$3.8M | 145.28 | 150 | 140 | -$478k | - | out (clean 33, ADX 17, RVol 0.2) |
| 13 | **MSTR** | 121.98 | - | **-** | 17 | - | NEG -$7.4M | 123.66 | 133 | 120 | +$1.7M | +$97k bull / +$0 bear | out (clean 28, ADX 20, RVol 0.3) |
| 14 | **AMZN** | 266.78 | - | **-** | 16 | - | POS +$408.1M | - | 270 | 265 | +$3.1M | +$0 bull / -$78k bear | out (clean 31, ADX 16, RVol 0.6) |
| 15 | **ARM** | 204.58 | - | **-** | 15 | - | POS +$5.4M | - | 200 | 200 | -$1.8M | - | out (clean 31, ADX 27, RVol 0.4) |
| 16 | **TSLA** | 391.79 | - | **-** | 14 | - | POS +$423.7M | - | 400 | 380 | -$3.0M | +$225k bull / -$28k bear | out (clean 32, ADX 20, RVol 0.3) |
| 17 | **DELL** | 377.16 | - | **-** | 13 | - | NEG -$60k | 379.69 | 380 | 380 | -$2.2M | - | out (clean 38, ADX 42, RVol 0.7) |
| 18 | **BABA** | 101.79 | - | **-** | 13 | - | NEG -$17.6M | 106.32 | 110 | 101 | +$361k | - | out (clean 29, ADX 17, RVol 0.2) |
| 19 | **SMCI** | 30.62 | - | **-** | 12 | - | POS +$12.6M | - | 30 | 30 | -$589k | - | out (clean 33, ADX 31, RVol 0.4) |
| 20 | **NFLX** | 64.25 | - | **-** | 11 | - | NEG -$3.9M | 64.54 | 65 | 65 | -$342k | - | out (clean 28, ADX 26, RVol 1.0) |
| 21 | **PLTR** | 173.23 | - | **-** | 9 | - | POS +$75.8M | - | 170 | 180 | +$1.6M | - | out (clean 29, ADX 22, RVol 0.2) |
| 22 | **GOOGL** | 294.46 | - | **-** | 8 | - | POS +$109.3M | 290.25 | 300 | 290 | -$990k | - | out (clean 30, ADX 33, RVol 0.4) |
| 23 | **HOOD** | 85.28 | - | **-** | 8 | - | POS +$15.8M | - | 85 | 85 | -$593k | - | out (clean 35, ADX 24, RVol 0.5) |
| 24 | **UBER** | 70.88 | - | **-** | 8 | - | POS +$19.9M | 68.43 | 70 | 70 | -$14k | - | out (clean 32, ADX 39, RVol 0.3) |
| 25 | **CRM** | 217.40 | - | **-** | 7 | - | NEG -$11.4M | - | 230 | 220 | -$55k | - | out (clean 29, ADX 11, RVol 0.3) |
| 26 | **ORCL** | 129.31 | - | **-** | 6 | - | POS +$4.0M | 124.55 | 130 | 125 | +$243k | - | out (clean 30, ADX 26, RVol 0.4) |
| 27 | **COIN** | 137.44 | - | **-** | 5 | - | POS +$25.2M | - | 141 | 135 | +$23k | - | out (clean 29, ADX 24, RVol 0.4) |

## Big prints this scan (59)
- **AMD** PUT 547.5 2026-11-13 (2DTE): 480 @ 7.95 = **+$382k** SELL | vol 1,055 / OI 42
- **NVDA** PUT 175 2026-11-11 (0DTE): 5,969 @ 0.55 = **+$328k** BUY | vol 275,276 / OI 7,572
- **SPY** CALL 759 2026-11-11 (0DTE): 1,000 @ 1.76 = **+$176k** SELL | vol 414,088 / OI 865
- **MU** PUT 825 2026-11-11 (0DTE): 200 @ 8.65 = **+$173k** BUY | vol 20,229 / OI 75
- **SMH** CALL 500 2026-11-13 (2DTE): 102 @ 15.00 = **+$153k** BUY | vol 2,320 / OI 4,456
- **IWM** PUT 281 2026-11-13 (2DTE): 1,865 @ 0.71 = **+$132k** SELL | vol 4,872 / OI 1,693
- **NVDA** CALL 167.5 2026-11-13 (2DTE): 130 @ 8.65 = **+$112k** SELL | vol 4,870 / OI 195
- **MU** CALL 815 2026-11-11 (0DTE): 200 @ 5.20 = **+$104k** BUY | vol 33,253 / OI 988
- **SPY** CALL 759 2026-11-11 (0DTE): 585 @ 1.76 = **+$103k** SELL | vol 414,088 / OI 865
- **AMD** PUT 547.5 2026-11-13 (2DTE): 120 @ 7.95 = **+$95k** SELL | vol 1,055 / OI 42
- **MU** PUT 785 2026-11-13 (2DTE): 100 @ 8.35 = **+$84k** BUY | vol 1,071 / OI 261
- **AMD** CALL 545 2026-11-16 (5DTE): 30 @ 26.65 = **+$80k** BUY | vol 261 / OI 38
- **AMD** CALL 545 2026-11-16 (5DTE): 30 @ 26.60 = **+$80k** BUY | vol 261 / OI 38
- **NVDA** CALL 182.5 2026-11-16 (5DTE): 450 @ 1.62 = **+$73k** SELL | vol 12,861 / OI 1,598
- **MU** PUT 780 2026-11-13 (2DTE): 99 @ 7.20 = **+$71k** BUY | vol 4,006 / OI 1,187

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 762 2026-11-17 (6DTE): 549 traded vs OI 306
- **QQQ** PUT 652 2026-11-12 (1DTE): 500 traded vs OI 297
- **IWM** CALL 290 2026-11-16 (5DTE): 529 traded vs OI 514
- **NVDA** PUT 175 2026-11-25 (14DTE): 500 traded vs OI 0
- **AAPL** PUT 340 2026-11-13 (2DTE): 8,853 traded vs OI 8,796
- **DELL** PUT 380 2026-11-13 (2DTE): 502 traded vs OI 304
- **MU** PUT 780 2026-11-16 (5DTE): 572 traded vs OI 36
- **MSTR** PUT 124 2026-11-13 (2DTE): 790 traded vs OI 786

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
