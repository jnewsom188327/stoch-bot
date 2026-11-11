# GEX + FLOW SCAN - Wed Nov 11, 03:00 PM ET
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
Last 1m check 15:00:08 ET, last candle SPY 14:59, QQQ 14:59 | no errors
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
| 1 | **AMD** | 559.02 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 40 | none: 176 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (64 contracts' greeks worked out here) | POS +$138.3M | - | 560 | 550 | -$99.8M | +$1.4M bull / -$69k bear | out (clean 35, ADX 33, RVol 0.3) |
| 2 | **MSFT** | 520.08 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 36 | none: 162 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (61 contracts' greeks worked out here) | POS +$47.5M | 516.55 | 535 | 520 | +$14.4M | +$259k bull / +$0 bear | out (clean 32, ADX 15, RVol 0.5) |
| 3 | **IWM** | 283.00 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 35 | none: 340 puts 0-7DTE > 14 priced 0.40-0.80 > 6 delta 0.2+ > 6 spread ok > 6 liquid > best one only +10% at the target (needs +20%) (153 contracts' greeks worked out here) | POS +$174.2M | 282.69 | 283 | 270 | -$5.1M | +$132k bull / +$0 bear | out (clean 35, ADX 24, RVol 0.3) |
| 4 | **AAPL** | 354.60 | PINNED between the walls (positive gamma) - chop | **-** | 26 | - | POS +$2.7B | 341.11 | 355 | 355 | +$704k | +$95k bull / +$0 bear | out (clean 28, ADX 24, RVol 0.2) |
| 5 | **META** | 635.41 | PINNED between the walls (positive gamma) - chop | **-** | 23 | - | POS +$169.9M | 629.72 | 635 | 635 | +$5.5M | - | out (clean 30, ADX 44, RVol 0.5) |
| 6 | **MU** | 817.55 | - | **-** | 22 | - | POS +$162.5M | - | 800 | 800 | -$201.1M | +$1.5M bull / -$2.1M bear | out (clean 34, ADX 25, RVol 0.3) |
| 7 | **AVGO** | 348.91 | - | **-** | 21 | - | POS +$104.3M | - | 350 | 350 | +$8.7M | +$0 bull / -$266k bear | out (clean 37, ADX 34, RVol 0.5) |
| 8 | **SPY** | 760.43 | - | **-** | 19 | - | NEG -$815.6M | 761.42 | 760 | 750 | -$126.0M | +$176k bull / -$418k bear | out (clean 34, ADX 30, RVol 0.3) |
| 9 | **QQQ** | 692.01 | - | **-** | 19 | - | POS +$430.5M | 690.03 | 700 | 680 | -$139.8M | +$101k bull / +$0 bear | out (clean 33, ADX 30, RVol 0.3) |
| 10 | **SMH** | 510.83 | - | **-** | 19 | - | NEG -$39.7M | 514.69 | 500 | 500 | -$2.6M | +$153k bull / +$0 bear | out (clean 32, ADX 33, RVol 0.4) |
| 11 | **NVDA** | 175.54 | - | **-** | 18 | - | NEG -$185.7M | 182.12 | 175 | 175 | -$22.5M | +$69k bull / -$1.4M bear | out (clean 35, ADX 28, RVol 0.5) |
| 12 | **MSTR** | 121.68 | - | **-** | 18 | - | NEG -$7.7M | 123.6 | 133 | 120 | +$1.8M | +$25k bull / +$0 bear | out (clean 28, ADX 21, RVol 0.4) |
| 13 | **SHOP** | 149.22 | - | **-** | 17 | - | POS +$3.9M | 145.14 | 150 | 140 | -$478k | - | out (clean 33, ADX 15, RVol 0.2) |
| 14 | **TSLA** | 391.73 | - | **-** | 15 | - | POS +$411.2M | - | 400 | 380 | -$1.2M | +$523k bull / +$0 bear | out (clean 32, ADX 22, RVol 0.3) |
| 15 | **AMZN** | 266.27 | - | **-** | 15 | - | POS +$401.3M | - | 270 | 265 | +$3.4M | +$62k bull / -$26k bear | out (clean 31, ADX 16, RVol 0.5) |
| 16 | **ARM** | 204.71 | - | **-** | 14 | - | POS +$5.4M | - | 200 | 200 | -$1.8M | - | out (clean 32, ADX 24, RVol 0.4) |
| 17 | **DELL** | 377.71 | - | **-** | 12 | - | NEG -$144k | 382.12 | 380 | 380 | -$2.3M | - | out (clean 38, ADX 41, RVol 0.4) |
| 18 | **SMCI** | 30.59 | - | **-** | 12 | - | POS +$13.0M | - | 30 | 30 | -$586k | - | out (clean 33, ADX 31, RVol 0.3) |
| 19 | **BABA** | 101.72 | - | **-** | 12 | - | NEG -$17.2M | 106.51 | 110 | 101 | +$355k | - | out (clean 29, ADX 19, RVol 0.1) |
| 20 | **NFLX** | 64.17 | - | **-** | 10 | - | NEG -$4.4M | 64.48 | 65 | 65 | -$280k | - | out (clean 27, ADX 28, RVol 0.9) |
| 21 | **PLTR** | 172.96 | - | **-** | 8 | - | POS +$78.8M | - | 170 | 170 | +$1.5M | - | out (clean 29, ADX 21, RVol 0.3) |
| 22 | **HOOD** | 85.32 | - | **-** | 8 | - | POS +$16.1M | - | 85 | 85 | -$620k | - | out (clean 35, ADX 21, RVol 0.4) |
| 23 | **GOOGL** | 294.14 | - | **-** | 7 | - | POS +$105.4M | 289.49 | 300 | 290 | -$954k | - | out (clean 30, ADX 30, RVol 0.4) |
| 24 | **UBER** | 70.64 | - | **-** | 7 | - | POS +$20.0M | 68.35 | 70 | 70 | -$11k | - | out (clean 32, ADX 35, RVol 0.3) |
| 25 | **CRM** | 217.58 | - | **-** | 6 | - | NEG -$11.1M | - | 230 | 220 | -$55k | - | out (clean 29, ADX 11, RVol 0.3) |
| 26 | **COIN** | 137.27 | - | **-** | 5 | - | POS +$25.5M | - | 141 | 135 | +$37k | - | out (clean 29, ADX 26, RVol 0.3) |
| 27 | **ORCL** | 129.32 | - | **-** | 5 | - | POS +$4.1M | 124.42 | 130 | 125 | +$247k | - | out (clean 30, ADX 24, RVol 0.3) |

## Big prints this scan (44)
- **MU** PUT 825 2026-11-11 (0DTE): 200 @ 8.95 = **+$179k** BUY | vol 20,740 / OI 75
- **SPY** CALL 759 2026-11-11 (0DTE): 900 @ 1.95 = **+$176k** BUY | vol 420,997 / OI 865
- **MU** CALL 810 2026-11-11 (0DTE): 200 @ 8.00 = **+$160k** SELL | vol 35,633 / OI 513
- **SMH** CALL 500 2026-11-13 (2DTE): 108 @ 14.40 = **+$156k** MID | vol 2,445 / OI 4,456
- **AVGO** CALL 332.5 2026-11-13 (2DTE): 57 @ 17.50 = **+$100k** SELL | vol 251 / OI 447
- **NVDA** PUT 177.5 2026-11-13 (2DTE): 194 @ 4.40 = **+$85k** BUY | vol 15,275 / OI 4,898
- **NVDA** PUT 177.5 2026-11-13 (2DTE): 194 @ 4.40 = **+$85k** BUY | vol 15,275 / OI 4,898
- **NVDA** PUT 177.5 2026-11-13 (2DTE): 194 @ 4.40 = **+$85k** BUY | vol 15,275 / OI 4,898
- **NVDA** PUT 177.5 2026-11-13 (2DTE): 176 @ 4.40 = **+$77k** BUY | vol 15,275 / OI 4,898
- **MU** CALL 830 2026-11-16 (5DTE): 39 @ 19.45 = **+$76k** MID | vol 1,176 / OI 106
- **NVDA** CALL 177.5 2026-11-16 (5DTE): 200 @ 3.45 = **+$69k** BUY | vol 12,811 / OI 1,501
- **MU** CALL 850 2026-11-13 (2DTE): 75 @ 8.16 = **+$61k** BUY | vol 10,906 / OI 0
- **MU** CALL 817.5 2026-11-13 (2DTE): 30 @ 20.19 = **+$61k** SELL | vol 1,522 / OI 62
- **MU** CALL 817.5 2026-11-13 (2DTE): 30 @ 19.85 = **+$60k** SELL | vol 1,522 / OI 62
- **NVDA** PUT 177.5 2026-11-13 (2DTE): 126 @ 4.40 = **+$55k** BUY | vol 15,275 / OI 4,898

## New unusual volume (traded more than open interest, 500+)
- **QQQ** PUT 695 2026-11-17 (6DTE): 504 traded vs OI 93
- **IWM** PUT 277 2026-11-12 (1DTE): 563 traded vs OI 562
- **NVDA** CALL 185 2026-12-04 (23DTE): 1,739 traded vs OI 1,729
- **AMZN** CALL 260 2026-11-16 (5DTE): 527 traded vs OI 256
- **SMCI** PUT 28.5 2026-11-13 (2DTE): 694 traded vs OI 444
- **SMCI** CALL 32.5 2026-11-20 (9DTE): 501 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
