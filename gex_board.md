# GEX + FLOW SCAN - Thu Nov 12, 02:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:35 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 754P | 0.59 | 0.17 | +10% (1m) | **-71%** (done) | +70% | 755 |
| 09:50 | **HOOD** | **PUTS** | TREND + FLOW | 11/13 79P | 0.55 | 0.36 | +5% (19m) | **-35%** (done) | +92% | 80 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 130C | 0.75 | 0.72 | +4% (60m) | **-4%** (done) | +59% | 126.9 |
| 09:45 | **SMCI** | **PUTS** | TREND + FLOW | 11/13 27P | 0.42 | 0.23 | -5% (6m) | **-45%** (done) | +57% | 27 |
| 09:45 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 753P | 0.79 | 0.31 | +23% (18m) | **-61%** (done) | +51% | 754.88 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:50:08 ET, last candle SPY 14:49, QQQ 14:49 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 14:27 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 14:15 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 90 puts 0-1DTE > 6 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 10:03 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (7 today, last 5)
- 12:00 SMCI CALLS: price -0.27 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:55 SMCI CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:50 SMCI CALLS: price -0.48 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:45 SMCI CALLS: price -0.74 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:30 IWM CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **GOOGL** | 299.74 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 38 | none: 72 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$131.2M | 288.55 | 300 | 290 | -$4.7M | +$90k bull / +$0 bear | out (clean 30, ADX 26, RVol 0.9) |
| 2 | **SMCI** | 27.55 | - | **-** | 21 | - | POS +$1.7M | 26.63 | 30 | 25 | +$1.2M | +$26k bull / +$0 bear | out (clean 34, ADX 23, RVol 1.2) |
| 3 | **MSFT** | 522.83 | - | **-** | 20 | - | POS +$76.0M | 519.18 | 535 | 520 | -$2.9M | +$40k bull / +$0 bear | out (clean 32, ADX 42, RVol 0.6) |
| 4 | **ARM** | 199.90 | PINNED between the walls (positive gamma) - chop | **-** | 20 | - | POS +$9.6M | - | 200 | 200 | -$319k | - | out (clean 31, ADX 24, RVol 0.3) |
| 5 | **SPY** | 757.73 | - | **-** | 18 | - | NEG -$2.5B | 760.67 | 760 | 760 | -$106.7M | +$224k bull / +$0 bear | out (clean 32, ADX 26, RVol 0.5) |
| 6 | **AMZN** | 267.99 | - | **-** | 18 | - | POS +$465.7M | - | 270 | 270 | -$7.0M | +$45k bull / +$0 bear | out (clean 29, ADX 17, RVol 0.6) |
| 7 | **QQQ** | 687.72 | - | **-** | 17 | - | NEG -$453.3M | 690.1 | 700 | 680 | -$73.0M | +$650k bull / +$0 bear | out (clean 31, ADX 25, RVol 0.5) |
| 8 | **SMH** | 500.68 | - | **-** | 17 | - | NEG -$106.3M | - | 500 | 475 | -$1.4M | +$91k bull / +$0 bear | out (clean 31, ADX 22, RVol 0.4) |
| 9 | **META** | 621.86 | - | **-** | 17 | - | NEG -$29.2M | 624.91 | 650 | 600 | +$2.3M | +$47k bull / +$0 bear | out (clean 29, ADX 29, RVol 0.3) |
| 10 | **NVDA** | 163.66 | - | **-** | 16 | - | NEG -$199.4M | - | 170 | 160 | -$60.3M | +$925k bull / -$436k bear | out (clean 32, ADX 13, RVol 0.8) |
| 11 | **TSLA** | 390.52 | - | **-** | 16 | - | POS +$351.5M | - | 400 | 380 | +$10.9M | +$380k bull / -$104k bear | out (clean 29, ADX 22, RVol 0.2) |
| 12 | **AVGO** | 364.12 | - | **-** | 16 | - | POS +$132.1M | - | 350 | 350 | +$8.8M | +$34k bull / +$0 bear | out (clean 34, ADX 10, RVol 0.7) |
| 13 | **AMD** | 586.22 | - | **-** | 15 | - | POS +$196.0M | - | 600 | 550 | -$24.9M | +$0 bull / -$732k bear | out (clean 34, ADX 15, RVol 0.5) |
| 14 | **DELL** | 372.18 | - | **-** | 15 | - | POS +$5.2M | - | 360 | 340 | +$429k | +$72k bull / +$0 bear | out (clean 37, ADX 17, RVol 0.5) |
| 15 | **MSTR** | 115.45 | - | **-** | 14 | - | NEG -$33.7M | - | 125 | 110 | -$568k | +$40k bull / +$0 bear | out (clean 29, ADX 16, RVol 0.3) |
| 16 | **MU** | 793.87 | - | **-** | 13 | - | POS +$101.1M | - | 800 | 800 | +$9.2M | +$4.0M bull / -$57k bear | out (clean 31, ADX 10, RVol 0.5) |
| 17 | **BABA** | 94.52 | - | **-** | 11 | - | NEG -$17.1M | - | 100 | 100 | +$312k | - | out (clean 29, ADX 21, RVol 1.1) |
| 18 | **NFLX** | 63.22 | - | **-** | 9 | - | NEG -$12.4M | 63.79 | 65 | 65 | -$176k | - | out (clean 29, ADX 27, RVol 0.5) |
| 19 | **IWM** | 279.00 | - | **-** | 8 | - | NEG -$1.4B | 282.56 | 285 | 275 | -$88k | - | out (clean 34, ADX 42, RVol 0.3) |
| 20 | **AAPL** | 355.56 | - | **-** | 7 | - | POS +$1.1B | 340.45 | 360 | 350 | +$5.3M | - | out (clean 29, ADX 23, RVol 0.3) |
| 21 | **UBER** | 69.16 | - | **-** | 7 | - | POS +$9.4M | 68.4 | 70 | 70 | -$50k | - | out (clean 32, ADX 17, RVol 0.5) |
| 22 | **SHOP** | 146.84 | - | **-** | 7 | - | POS +$3.4M | 143.93 | 150 | 140 | +$5k | - | out (clean 31, ADX 28, RVol 0.2) |
| 23 | **HOOD** | 82.35 | - | **-** | 6 | - | POS +$10.5M | 80.05 | 85 | 80 | -$4k | - | out (clean 34, ADX 23, RVol 0.7) |
| 24 | **COIN** | 131.79 | - | **-** | 5 | - | POS +$883k | 131.4 | 137 | 135 | +$94k | - | out (clean 30, ADX 19, RVol 0.2) |
| 25 | **ORCL** | 126.89 | - | **-** | 5 | - | POS +$11.6M | 120.86 | 130 | 125 | -$560k | - | out (clean 30, ADX 10, RVol 0.5) |
| 26 | **CRM** | 217.47 | - | **-** | 5 | - | NEG -$8.0M | 225.97 | 220 | 220 | +$41k | - | out (clean 29, ADX 16, RVol 0.1) |
| 27 | **PLTR** | 171.45 | - | **-** | 4 | - | POS +$89.6M | - | 170 | 170 | -$142k | - | out (clean 28, ADX 11, RVol 0.7) |

## Big prints this scan (42)
- **MU** PUT 785 2026-11-13 (1DTE): 303 @ 10.00 = **+$303k** SELL | vol 10,118 / OI 256
- **SPY** PUT 763 2026-11-16 (4DTE): 344 @ 6.50 = **+$224k** SELL | vol 26,314 / OI 216
- **MU** PUT 800 2026-11-13 (1DTE): 100 @ 17.00 = **+$170k** SELL | vol 6,907 / OI 872
- **QQQ** CALL 682 2026-11-12 (0DTE): 200 @ 6.25 = **+$125k** BUY | vol 11,127 / OI 472
- **QQQ** PUT 688 2026-11-12 (0DTE): 900 @ 1.30 = **+$117k** SELL | vol 225,247 / OI 89
- **QQQ** PUT 688 2026-11-12 (0DTE): 899 @ 1.22 = **+$110k** SELL | vol 225,247 / OI 89
- **NVDA** PUT 160 2026-11-16 (4DTE): 330 @ 2.99 = **+$99k** SELL | vol 43,776 / OI 4,794
- **MU** PUT 785 2026-11-13 (1DTE): 90 @ 10.00 = **+$90k** SELL | vol 10,118 / OI 256
- **NVDA** PUT 165 2026-11-13 (1DTE): 230 @ 3.85 = **+$89k** MID | vol 111,960 / OI 19,300
- **NVDA** CALL 165 2026-11-18 (6DTE): 100 @ 7.95 = **+$80k** BUY | vol 10,780 / OI 517
- **NVDA** CALL 165 2026-11-18 (6DTE): 100 @ 7.60 = **+$76k** BUY | vol 10,780 / OI 517
- **MU** PUT 785 2026-11-13 (1DTE): 76 @ 10.00 = **+$76k** SELL | vol 10,118 / OI 256
- **NVDA** CALL 157.5 2026-11-16 (4DTE): 79 @ 8.92 = **+$70k** BUY | vol 4,404 / OI 102
- **NVDA** PUT 170 2026-11-16 (4DTE): 60 @ 8.20 = **+$49k** SELL | vol 5,378 / OI 3,775
- **META** CALL 625 2026-11-13 (1DTE): 100 @ 4.67 = **+$47k** BUY | vol 4,552 / OI 469

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 759 2026-11-19 (7DTE): 526 traded vs OI 4
- **SPY** CALL 761 2026-11-20 (8DTE): 2,359 traded vs OI 2,350
- **QQQ** PUT 688 2026-11-17 (5DTE): 507 traded vs OI 27
- **AMZN** PUT 265 2026-11-16 (4DTE): 532 traded vs OI 180
- **MSFT** CALL 545 2026-11-13 (1DTE): 2,648 traded vs OI 2,628
- **GOOGL** PUT 297.5 2026-11-16 (4DTE): 547 traded vs OI 5
- **PLTR** PUT 160 2026-11-13 (1DTE): 2,488 traded vs OI 2,475
- **MU** PUT 717.5 2026-11-13 (1DTE): 502 traded vs OI 161
- **MSTR** PUT 118 2026-11-20 (8DTE): 500 traded vs OI 77
- **UBER** CALL 70 2026-11-13 (1DTE): 6,687 traded vs OI 6,117

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
