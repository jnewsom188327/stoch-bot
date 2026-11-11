# GEX + FLOW SCAN - Wed Nov 11, 12:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (12)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:40 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 522.5C | 0.73 | 0.91 | +48% (21m) | **+25%** | +146% | 523.2 |
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
Last 1m check 12:10:08 ET, last candle SPY 12:09, QQQ 12:09 | no errors
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
| 1 | **DELL** | 380.14 | PINNED between the walls (positive gamma) - chop | **-** | 46 | - | POS +$2.3M | - | 380 | 380 | -$3.6M | - | LONG (clean 36, ADX 70, RVol 0.8) |
| 2 | **MU** | 820.46 | TREND (flow not with it) | **CALLS** | 43 | none: 145 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (60 contracts' greeks worked out here) | POS +$149.1M | - | 800 | 800 | -$221.3M | +$6.7M bull / -$3.1M bear | LONG (clean 34, ADX 70, RVol 0.5) |
| 3 | **MSFT** | 520.62 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 42 | none: 166 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (76 contracts' greeks worked out here) | POS +$47.5M | 515.88 | 535 | 520 | +$14.0M | +$0 bull / -$183k bear | out (clean 32, ADX 40, RVol 0.6) |
| 4 | **ARM** | 204.85 | FLOW SURGE | **PUTS** | 41 | none: 17 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$5.2M | - | 200 | 200 | -$1.9M | +$37k bull / -$57k bear | out (clean 31, ADX 74, RVol 0.9) |
| 5 | **AAPL** | 354.90 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 37 | none: 113 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (64 contracts' greeks worked out here) | POS +$1.8B | 341.19 | 355 | 350 | -$2.1M | +$0 bull / -$30k bear | out (clean 27, ADX 41, RVol 0.4) |
| 6 | **HOOD** | 84.81 | PINNED between the walls (positive gamma) - chop | **-** | 35 | - | POS +$15.5M | - | 85 | 85 | -$751k | +$0 bull / -$54k bear | out (clean 33, ADX 34, RVol 0.4) |
| 7 | **AMD** | 553.48 | - | **-** | 27 | - | POS +$142.2M | - | 550 | 500 | -$76.7M | +$1.5M bull / -$551k bear | out (clean 33, ADX 49, RVol 0.3) |
| 8 | **SMH** | 513.04 | - | **-** | 26 | - | NEG -$19.0M | - | 500 | 500 | -$4.3M | +$932k bull / -$34k bear | out (clean 31, ADX 56, RVol 0.7) |
| 9 | **QQQ** | 692.68 | - | **-** | 25 | - | POS +$580.5M | 689.82 | 700 | 680 | -$158.7M | +$0 bull / -$1.8M bear | out (clean 33, ADX 57, RVol 0.6) |
| 10 | **SHOP** | 149.53 | - | **-** | 25 | - | POS +$3.6M | 145.26 | 150 | 140 | -$479k | - | out (clean 33, ADX 39, RVol 1.1) |
| 11 | **SPY** | 759.92 | - | **-** | 24 | - | NEG -$1.3B | 761.57 | 760 | 750 | -$106.4M | +$0 bull / -$126k bear | out (clean 32, ADX 54, RVol 0.4) |
| 12 | **IWM** | 282.68 | - | **-** | 22 | - | NEG -$47.3M | 282.88 | 285 | 270 | -$4.1M | +$0 bull / -$110k bear | out (clean 34, ADX 42, RVol 0.3) |
| 13 | **AVGO** | 354.45 | - | **-** | 22 | - | POS +$101.5M | - | 350 | 350 | +$4.0M | +$0 bull / -$364k bear | out (clean 34, ADX 54, RVol 0.6) |
| 14 | **SMCI** | 30.80 | - | **-** | 22 | - | POS +$12.3M | - | 30 | 30 | -$825k | - | out (clean 32, ADX 68, RVol 1.2) |
| 15 | **NVDA** | 176.26 | - | **-** | 21 | - | NEG -$128.9M | 181.09 | 180 | 175 | -$28.2M | +$0 bull / -$2.3M bear | out (clean 34, ADX 33, RVol 0.6) |
| 16 | **GOOGL** | 293.11 | - | **-** | 21 | - | POS +$81.0M | 289.08 | 300 | 290 | -$726k | +$142k bull / -$26k bear | out (clean 28, ADX 54, RVol 0.7) |
| 17 | **ORCL** | 128.59 | - | **-** | 21 | - | POS +$4.6M | 123.44 | 130 | 125 | -$601k | +$0 bull / -$27k bear | out (clean 29, ADX 50, RVol 0.5) |
| 18 | **TSLA** | 391.95 | - | **-** | 18 | - | POS +$409.8M | - | 400 | 380 | -$1.6M | +$462k bull / -$212k bear | out (clean 33, ADX 40, RVol 0.3) |
| 19 | **MSTR** | 122.54 | - | **-** | 18 | - | POS +$247k | 122.27 | 133 | 120 | +$630k | +$152k bull / -$90k bear | out (clean 28, ADX 26, RVol 0.7) |
| 20 | **BABA** | 101.66 | - | **-** | 16 | - | NEG -$16.9M | 106.49 | 110 | 101 | +$354k | - | out (clean 29, ADX 32, RVol 0.2) |
| 21 | **META** | 641.09 | - | **-** | 13 | - | POS +$308.1M | 624.45 | 650 | 635 | -$590k | +$121k bull / -$89k bear | out (clean 32, ADX 11, RVol 0.2) |
| 22 | **PLTR** | 172.74 | - | **-** | 13 | - | POS +$77.1M | - | 170 | 180 | +$1.8M | - | out (clean 29, ADX 32, RVol 0.4) |
| 23 | **CRM** | 217.54 | - | **-** | 10 | - | NEG -$11.0M | - | 230 | 220 | -$37k | - | out (clean 30, ADX 32, RVol 0.6) |
| 24 | **UBER** | 70.45 | - | **-** | 9 | - | POS +$16.5M | 68.31 | 70 | 70 | +$27k | - | out (clean 32, ADX 29, RVol 0.5) |
| 25 | **AMZN** | 266.90 | - | **-** | 7 | - | POS +$420.9M | - | 270 | 265 | +$3.0M | - | out (clean 32, ADX 19, RVol 0.4) |
| 26 | **NFLX** | 63.98 | - | **-** | 7 | - | NEG -$7.2M | 64.51 | 65 | 65 | -$53k | - | out (clean 26, ADX 24, RVol 0.6) |
| 27 | **COIN** | 137.17 | - | **-** | 6 | - | POS +$24.6M | - | 141 | 135 | +$10k | - | out (clean 29, ADX 31, RVol 0.2) |

## Big prints this scan (171)
- **AMD** CALL 550 2026-11-13 (2DTE): 500 @ 16.78 = **+$839k** BUY | vol 8,272 / OI 2,554
- **MU** CALL 805 2026-11-11 (0DTE): 199 @ 21.83 = **+$434k** BUY | vol 21,377 / OI 820
- **MU** CALL 805 2026-11-11 (0DTE): 200 @ 21.35 = **+$427k** BUY | vol 21,377 / OI 820
- **MU** CALL 805 2026-11-11 (0DTE): 200 @ 20.77 = **+$415k** BUY | vol 21,377 / OI 820
- **MU** CALL 805 2026-11-11 (0DTE): 200 @ 20.70 = **+$414k** BUY | vol 21,377 / OI 820
- **SMH** CALL 490 2026-11-11 (0DTE): 169 @ 23.76 = **+$402k** MID | vol 905 / OI 1,759
- **SMH** CALL 490 2026-11-11 (0DTE): 150 @ 23.50 = **+$352k** MID | vol 905 / OI 1,759
- **AMD** CALL 575 2026-11-13 (2DTE): 500 @ 6.28 = **+$314k** BUY | vol 4,063 / OI 1,572
- **SMH** CALL 490 2026-11-11 (0DTE): 97 @ 23.95 = **+$232k** BUY | vol 905 / OI 1,759
- **SMH** CALL 490 2026-11-11 (0DTE): 88 @ 23.70 = **+$209k** MID | vol 905 / OI 1,759
- **MU** CALL 805 2026-11-11 (0DTE): 88 @ 21.55 = **+$190k** BUY | vol 21,377 / OI 820
- **SMH** CALL 490 2026-11-11 (0DTE): 75 @ 23.99 = **+$180k** BUY | vol 905 / OI 1,759
- **AVGO** CALL 337.5 2026-11-11 (0DTE): 100 @ 16.97 = **+$170k** SELL | vol 500 / OI 543
- **QQQ** CALL 680 2026-11-13 (2DTE): 101 @ 15.00 = **+$152k** MID | vol 2,771 / OI 4,338
- **MU** CALL 800 2026-11-16 (5DTE): 35 @ 41.52 = **+$145k** BUY | vol 1,801 / OI 273

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 714 2026-11-12 (1DTE): 655 traded vs OI 548
- **SPY** PUT 760 2026-11-13 (2DTE): 7,176 traded vs OI 6,054
- **SPY** PUT 738 2026-11-12 (1DTE): 1,248 traded vs OI 1,124
- **SPY** CALL 817 2026-11-20 (9DTE): 1,000 traded vs OI 689
- **SPY** CALL 769 2026-12-04 (23DTE): 2,637 traded vs OI 370
- **SPY** CALL 783 2026-12-04 (23DTE): 2,528 traded vs OI 623
- **QQQ** PUT 674 2026-11-13 (2DTE): 505 traded vs OI 503
- **QQQ** CALL 741 2026-11-13 (2DTE): 1,100 traded vs OI 273
- **SMH** CALL 520 2026-11-11 (0DTE): 516 traded vs OI 86
- **NVDA** CALL 162.5 2026-11-11 (0DTE): 509 traded vs OI 234
- **NVDA** PUT 182.5 2026-11-18 (7DTE): 861 traded vs OI 544
- **NVDA** CALL 160 2026-11-18 (7DTE): 503 traded vs OI 50
- **TSLA** CALL 415 2026-11-16 (5DTE): 707 traded vs OI 706
- **META** CALL 680 2026-11-13 (2DTE): 1,290 traded vs OI 1,289
- **AMZN** CALL 267.5 2026-11-16 (5DTE): 532 traded vs OI 134

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
