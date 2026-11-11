# GEX + FLOW SCAN - Wed Nov 11, 10:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:45 | **AVGO** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/11 345P | 0.78 | 0.51 | +6% (1m) | **-35%** | +149% | 345 |
| 10:35 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.76 | 1.17 | +96% (9m) | **+54%** | +343% | 527.5 |
| 10:20 | **AVGO** | **CALLS** | TREND + FLOW | 11/11 355C | 0.71 | 0.64 | +8% (8m) | **-10%** | +280% | 356.78 |
| 10:15 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.65 | 0.66 | +14% (3m) | **+2%** | +66% | 282.84 |
| 10:05 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 175C | 0.76 | 1.20 | +82% (34m) | **+58%** | +58% | 175 hit |
| 09:50 | **GOOGL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 292.5C | 0.51 | 0.62 | +39% (28m) | **+22%** | +82% | 291.86 |
| 09:45 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.68 | 0.64 | +85% (6m) | **-6%** (done) | +68% | 282.96 |
| 09:45 | **QQQ** | **CALLS** | FLOW SURGE | 11/11 690C | 0.63 | 1.23 | +103% (59m) | **+95%** (done) | +171% | 689.78 |
| 09:39 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 693C | 0.52 | 0.29 | -10% (0m) | **-44%** (done) | +92% | 690.43 |
| 09:39 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 760C | 0.53 | 0.17 | -2% (0m) | **-68%** (done) | +79% | 758.82 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:50:08 ET, last candle SPY 10:49, QQQ 10:49 | no errors
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
| 1 | **ARM** | 199.98 | PINNED between the walls (positive gamma) - chop | **-** | 53 | - | POS +$4.1M | - | 200 | 200 | -$1.2M | +$0 bull / -$107k bear | out (clean 29, ADX 62, RVol 1.0) |
| 2 | **AMD** | 549.22 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 50 | none: 176 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (85 contracts' greeks worked out here) | POS +$144.8M | - | 550 | 500 | -$55.9M | +$0 bull / -$2.7M bear | LONG (clean 33, ADX 43, RVol 0.9) |
| 3 | **DELL** | 373.59 | FLOW SURGE | **PUTS** | 47 | none: 30 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$75k | 375.89 | 380 | 340 | -$2.8M | +$0 bull / -$250k bear | LONG (clean 36, ADX 64, RVol 1.3) |
| 4 | **MU** | 812.18 | FLOW SURGE | **PUTS** | 45 | none: 149 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (61 contracts' greeks worked out here) | POS +$151.5M | - | 800 | 800 | -$172.8M | +$0 bull / -$8.9M bear | LONG (clean 33, ADX 64, RVol 1.1) |
| 5 | **AMZN** | 266.73 | TREND (flow not with it) | **PUTS** | 42 | 11/11 265P @ 0.44 (delta 0.26) = est +93% at 265 | POS +$427.3M | - | 270 | 265 | +$4.9M | +$140k bull / -$511k bear | SHORT (clean 33, ADX 30, RVol 1.2) |
| 6 | **QQQ** | 689.86 | FLIP CROSS up into positive gamma | **CALLS** | 37 | 11/11 693C @ 0.55 (delta 0.23) = est +222% at 693.79 | POS +$71.4M | 689.81 | 700 | 680 | -$68.8M | +$0 bull / -$3.1M bear | out (clean 32, ADX 51, RVol 0.6) |
| 7 | **MSFT** | 522.67 | - | **-** | 29 | - | POS +$83.1M | 515.53 | 535 | 520 | +$12.1M | +$0 bull / -$1.0M bear | out (clean 32, ADX 44, RVol 1.6) |
| 8 | **SMH** | 507.59 | - | **-** | 28 | - | NEG -$43.9M | - | 500 | 500 | -$1.9M | +$30k bull / -$64k bear | out (clean 31, ADX 42, RVol 2.0) |
| 9 | **AVGO** | 350.88 | - | **-** | 25 | - | POS +$100.3M | - | 350 | 350 | +$4.6M | +$61k bull / +$0 bear | out (clean 35, ADX 50, RVol 1.2) |
| 10 | **PLTR** | 172.45 | - | **-** | 25 | - | POS +$76.8M | - | 170 | 170 | +$1.3M | +$0 bull / -$114k bear | out (clean 30, ADX 42, RVol 0.2) |
| 11 | **SMCI** | 30.51 | - | **-** | 23 | - | POS +$11.9M | - | 30 | 30 | -$476k | - | out (clean 32, ADX 58, RVol 0.9) |
| 12 | **TSLA** | 394.50 | - | **-** | 22 | - | POS +$414.9M | - | 400 | 380 | -$14.5M | +$1.4M bull / -$314k bear | out (clean 32, ADX 54, RVol 0.7) |
| 13 | **ORCL** | 126.31 | - | **-** | 22 | - | NEG -$1.2M | 127.96 | 130 | 125 | +$558k | +$0 bull / -$310k bear | out (clean 28, ADX 49, RVol 0.8) |
| 14 | **BABA** | 101.50 | - | **-** | 22 | - | NEG -$16.8M | 107.04 | 110 | 101 | +$402k | - | out (clean 29, ADX 33, RVol 0.5) |
| 15 | **SPY** | 757.53 | - | **-** | 21 | - | NEG -$3.0B | 760.89 | 760 | 750 | -$18.3M | +$0 bull / -$1.7M bear | out (clean 31, ADX 50, RVol 0.5) |
| 16 | **GOOGL** | 291.45 | - | **-** | 21 | - | POS +$49.4M | 289.2 | 300 | 290 | +$506k | +$0 bull / -$28k bear | out (clean 28, ADX 50, RVol 0.8) |
| 17 | **IWM** | 282.19 | - | **-** | 20 | - | NEG -$261.6M | 282.85 | 285 | 270 | -$1.3M | +$0 bull / -$123k bear | out (clean 34, ADX 40, RVol 0.3) |
| 18 | **NVDA** | 174.88 | - | **-** | 20 | - | NEG -$165.0M | 181.03 | 180 | 175 | -$11.7M | +$680k bull / -$2.2M bear | out (clean 34, ADX 32, RVol 1.1) |
| 19 | **META** | 637.00 | - | **-** | 20 | - | POS +$216.4M | 625.03 | 650 | 625 | +$4.3M | +$220k bull / -$196k bear | out (clean 31, ADX 22, RVol 0.8) |
| 20 | **AAPL** | 353.36 | - | **-** | 19 | - | POS +$1.4B | 340.57 | 355 | 350 | -$559k | +$141k bull / +$0 bear | out (clean 27, ADX 46, RVol 0.4) |
| 21 | **HOOD** | 84.32 | - | **-** | 17 | - | POS +$14.4M | - | 85 | 85 | -$497k | - | out (clean 32, ADX 36, RVol 0.7) |
| 22 | **MSTR** | 122.32 | - | **-** | 16 | - | NEG -$129k | 122.09 | 133 | 120 | +$238k | +$0 bull / -$86k bear | out (clean 28, ADX 18, RVol 0.8) |
| 23 | **UBER** | 69.23 | - | **-** | 14 | - | POS +$7.6M | 68.33 | 70 | 70 | +$66k | - | out (clean 32, ADX 23, RVol 0.6) |
| 24 | **COIN** | 136.75 | - | **-** | 11 | - | POS +$23.2M | - | 141 | 135 | -$149k | - | out (clean 28, ADX 31, RVol 1.0) |
| 25 | **CRM** | 215.99 | - | **-** | 11 | - | NEG -$11.3M | - | 230 | 220 | -$20k | - | out (clean 30, ADX 28, RVol 0.6) |
| 26 | **SHOP** | 147.78 | - | **-** | 8 | - | POS +$2.2M | 144.94 | 150 | 140 | +$985 | - | out (clean 33, ADX 36, RVol 0.2) |
| 27 | **NFLX** | 63.39 | - | **-** | 6 | - | NEG -$14.1M | 64.5 | 65 | 65 | +$64k | - | out (clean 26, ADX 14, RVol 0.7) |

## Big prints this scan (127)
- **MU** CALL 780 2026-11-11 (0DTE): 90 @ 28.58 = **+$257k** SELL | vol 14,290 / OI 2,052
- **QQQ** PUT 688 2026-11-12 (1DTE): 591 @ 4.10 = **+$242k** BUY | vol 3,156 / OI 91
- **QQQ** PUT 688 2026-11-12 (1DTE): 574 @ 4.05 = **+$232k** BUY | vol 3,156 / OI 91
- **MSFT** CALL 500 2026-11-18 (7DTE): 100 @ 23.00 = **+$230k** SELL | vol 209 / OI 5
- **AMD** CALL 550 2026-11-11 (0DTE): 1,000 @ 2.19 = **+$219k** SELL | vol 22,626 / OI 918
- **MU** CALL 785 2026-11-11 (0DTE): 90 @ 24.18 = **+$218k** SELL | vol 8,323 / OI 277
- **QQQ** CALL 687 2026-11-13 (2DTE): 325 @ 5.82 = **+$189k** SELL | vol 3,960 / OI 762
- **QQQ** CALL 685 2026-11-11 (0DTE): 492 @ 3.40 = **+$167k** SELL | vol 60,680 / OI 1,366
- **QQQ** CALL 685 2026-11-11 (0DTE): 500 @ 3.20 = **+$160k** SELL | vol 60,680 / OI 1,366
- **SPY** CALL 753 2026-11-11 (0DTE): 400 @ 3.54 = **+$142k** SELL | vol 8,659 / OI 1,354
- **DELL** CALL 357.5 2026-11-13 (2DTE): 70 @ 20.20 = **+$141k** SELL | vol 130 / OI 170
- **QQQ** PUT 687 2026-11-13 (2DTE): 250 @ 5.42 = **+$136k** BUY | vol 2,914 / OI 679
- **AMD** CALL 555 2026-11-11 (0DTE): 1,000 @ 1.14 = **+$114k** SELL | vol 8,767 / OI 266
- **MU** CALL 780 2026-11-13 (2DTE): 30 @ 36.00 = **+$108k** SELL | vol 2,870 / OI 1,313
- **NVDA** PUT 175 2026-11-11 (0DTE): 556 @ 1.70 = **+$95k** BUY | vol 18,142 / OI 7,572

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 729 2026-11-11 (0DTE): 852 traded vs OI 531
- **SPY** CALL 758 2026-11-13 (2DTE): 2,249 traded vs OI 2,218
- **SPY** PUT 733 2026-11-23 (12DTE): 684 traded vs OI 0
- **SPY** PUT 735 2026-11-23 (12DTE): 1,206 traded vs OI 831
- **QQQ** PUT 684 2026-11-16 (5DTE): 500 traded vs OI 67
- **QQQ** PUT 680 2026-11-16 (5DTE): 620 traded vs OI 589
- **QQQ** PUT 675 2026-11-16 (5DTE): 510 traded vs OI 489
- **QQQ** PUT 687 2026-11-16 (5DTE): 501 traded vs OI 37
- **QQQ** CALL 682 2026-11-12 (1DTE): 500 traded vs OI 304
- **QQQ** CALL 690 2026-11-13 (2DTE): 9,041 traded vs OI 8,488
- **QQQ** CALL 701 2026-11-13 (2DTE): 750 traded vs OI 700
- **QQQ** PUT 664 2026-11-12 (1DTE): 502 traded vs OI 148
- **QQQ** PUT 687 2026-11-17 (6DTE): 500 traded vs OI 40
- **IWM** PUT 282 2026-11-13 (2DTE): 2,035 traded vs OI 1,590
- **NVDA** CALL 157.5 2026-11-13 (2DTE): 659 traded vs OI 204

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
