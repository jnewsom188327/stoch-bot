# GEX + FLOW SCAN - Fri Nov 06, 12:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:40 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/06 742C | 0.42 | 0.35 | +14% (6m) | **-17%** | +42% | 739.03 |
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.28 | +12% (20m) | **-62%** (done) | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.03 | -6% (1m) | **-96%** (done) | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.36 | +32% (4m) | **-10%** (done) | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:50:08 ET, last candle SPY 12:49, QQQ 12:49 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 12:39 | SPY | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** SPY261106C00742000 |
| 12:38 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:38 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:37 | QQQ | 1m WHIPSAW | R1 R2 | PUTS | WITH you | no contract: 39 puts 0-1DTE > 5 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |
| 12:37 | SPY | 1m WHIPSAW | R1 R2 | PUTS | WITH you | no contract: 43 puts 0-1DTE > 3 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NFLX** | 63.89 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 25 | none: 26 puts 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +10% at the target (needs +20%) (19 contracts' greeks worked out here) | POS +$91k | 63.89 | 64 | 65 | -$305k | - | out (clean 32, ADX 16, RVol 0.7) |
| 2 | **DELL** | 326.36 | - | **-** | 21 | - | NEG -$22.0M | - | 330 | 335 | +$5.0M | +$105k bull / +$0 bear | out (clean 32, ADX 13, RVol 0.5) |
| 3 | **SMH** | 457.64 | - | **-** | 20 | - | NEG -$435.8M | - | 500 | 465 | +$8.5M | +$113k bull / +$0 bear | out (clean 33, ADX 14, RVol 0.8) |
| 4 | **MSTR** | 126.25 | - | **-** | 20 | - | NEG -$12.5M | 127.35 | 135 | 125 | -$7.7M | +$66k bull / +$0 bear | out (clean 31, ADX 16, RVol 0.6) |
| 5 | **TSLA** | 357.10 | - | **-** | 19 | - | NEG -$298.1M | - | 370 | 360 | -$56.9M | +$1.3M bull / -$108k bear | out (clean 35, ADX 26, RVol 0.4) |
| 6 | **IWM** | 272.96 | - | **-** | 18 | - | NEG -$3.3B | 286.19 | 285 | 270 | -$4.4M | +$225k bull / +$0 bear | out (clean 34, ADX 19, RVol 1.2) |
| 7 | **BABA** | 108.63 | - | **-** | 18 | - | POS +$30.2M | - | 110 | 110 | -$417k | +$37k bull / +$0 bear | out (clean 34, ADX 18, RVol 0.7) |
| 8 | **NVDA** | 185.60 | - | **-** | 17 | - | NEG -$369.4M | - | 200 | 190 | +$25.8M | +$1.2M bull / +$0 bear | out (clean 33, ADX 15, RVol 0.8) |
| 9 | **AAPL** | 343.92 | - | **-** | 17 | - | POS +$6.1M | 343.78 | 350 | 345 | -$15.8M | +$29k bull / -$85k bear | out (clean 29, ADX 9, RVol 0.3) |
| 10 | **META** | 616.98 | - | **-** | 17 | - | NEG -$135.6M | 622.87 | 620 | 610 | -$5.4M | +$714k bull / +$0 bear | out (clean 33, ADX 22, RVol 0.7) |
| 11 | **GOOGL** | 285.07 | PINNED between the walls (positive gamma) - chop | **-** | 17 | - | POS +$74.3M | 282.49 | 285 | 285 | +$1.6M | - | out (clean 34, ADX 14, RVol 0.4) |
| 12 | **AVGO** | 291.38 | - | **-** | 17 | - | NEG -$131.3M | - | 320 | 300 | +$4.0M | +$797k bull / +$0 bear | out (clean 31, ADX 17, RVol 0.8) |
| 13 | **PLTR** | 160.34 | - | **-** | 17 | - | NEG -$67.9M | - | 165 | 160 | +$3.4M | +$40k bull / +$0 bear | out (clean 28, ADX 18, RVol 0.5) |
| 14 | **MU** | 681.02 | - | **-** | 17 | - | NEG -$131.2M | - | 700 | 700 | +$69.6M | +$2.2M bull / +$0 bear | out (clean 32, ADX 12, RVol 0.7) |
| 15 | **HOOD** | 78.66 | - | **-** | 17 | - | NEG -$22.2M | - | 85 | 80 | +$2.0M | +$102k bull / +$0 bear | out (clean 30, ADX 19, RVol 0.7) |
| 16 | **SHOP** | 148.79 | - | **-** | 17 | - | NEG -$2.5M | 150.13 | 150 | 150 | -$1.1M | - | out (clean 36, ADX 26, RVol 0.7) |
| 17 | **QQQ** | 654.99 | - | **-** | 16 | - | NEG -$5.2B | - | 700 | 680 | +$48.6M | +$2.2M bull / +$0 bear | out (clean 34, ADX 17, RVol 0.8) |
| 18 | **AMD** | 435.54 | - | **-** | 16 | - | NEG -$180.0M | - | 430 | 440 | +$17.4M | +$486k bull / +$0 bear | out (clean 32, ADX 18, RVol 0.5) |
| 19 | **MSFT** | 532.88 | - | **-** | 16 | - | POS +$632.2M | 513.07 | 535 | 535 | +$3.5M | +$43k bull / +$0 bear | out (clean 34, ADX 12, RVol 0.4) |
| 20 | **SPY** | 736.25 | - | **-** | 15 | - | NEG -$14.2B | 768.86 | 760 | 740 | -$20.7M | +$622k bull / +$0 bear | out (clean 34, ADX 17, RVol 0.7) |
| 21 | **AMZN** | 261.54 | - | **-** | 15 | - | POS +$334.8M | - | 260 | 260 | -$91k | +$177k bull / +$0 bear | out (clean 34, ADX 25, RVol 0.3) |
| 22 | **COIN** | 132.44 | - | **-** | 12 | - | NEG -$23.2M | 136.67 | 141 | 130 | -$3.6M | - | out (clean 32, ADX 18, RVol 0.3) |
| 23 | **ORCL** | 112.06 | - | **-** | 8 | - | NEG -$60.1M | - | 120 | 110 | +$426k | - | out (clean 30, ADX 18, RVol 1.6) |
| 24 | **UBER** | 69.15 | - | **-** | 8 | - | POS +$12.5M | 68.57 | 70 | 65 | +$150k | - | out (clean 30, ADX 19, RVol 0.3) |
| 25 | **SMCI** | 27.86 | - | **-** | 7 | - | NEG -$4.0M | - | 30 | 28 | -$373k | - | out (clean 34, ADX 19, RVol 0.3) |
| 26 | **ARM** | 170.00 | - | **-** | 7 | - | NEG -$23.9M | - | 180 | 170 | -$360k | - | out (clean 25, ADX 14, RVol 0.8) |
| 27 | **CRM** | 214.68 | - | **-** | 7 | - | NEG -$22.0M | - | 230 | 215 | -$200k | - | out (clean 35, ADX 21, RVol 0.8) |

## Big prints this scan (52)
- **AAPL** PUT 357.5 2026-11-13 (7DTE): 134 @ 14.41 = **+$193k** MID | vol 337 / OI 319
- **QQQ** CALL 665 2026-11-06 (0DTE): 3,975 @ 0.47 = **+$187k** BUY | vol 137,222 / OI 64
- **SPY** PUT 768 2026-11-06 (0DTE): 56 @ 28.53 = **+$160k** SELL | vol 367 / OI 4,923
- **QQQ** PUT 660 2026-11-09 (3DTE): 200 @ 7.05 = **+$141k** SELL | vol 18,011 / OI 1,084
- **AAPL** PUT 352.5 2026-11-13 (7DTE): 134 @ 10.51 = **+$141k** MID | vol 426 / OI 1,265
- **QQQ** PUT 660 2026-11-09 (3DTE): 200 @ 7.00 = **+$140k** SELL | vol 18,011 / OI 1,084
- **QQQ** PUT 660 2026-11-09 (3DTE): 195 @ 7.05 = **+$137k** SELL | vol 18,011 / OI 1,084
- **NVDA** PUT 187.5 2026-11-13 (7DTE): 200 @ 6.18 = **+$124k** SELL | vol 5,108 / OI 3,561
- **TSLA** CALL 360 2026-11-06 (0DTE): 500 @ 2.45 = **+$122k** BUY | vol 134,787 / OI 599
- **AAPL** PUT 357.5 2026-11-13 (7DTE): 85 @ 14.41 = **+$122k** MID | vol 337 / OI 319
- **AAPL** PUT 357.5 2026-11-13 (7DTE): 85 @ 14.41 = **+$122k** MID | vol 337 / OI 319
- **TSLA** PUT 370 2026-11-06 (0DTE): 120 @ 10.20 = **+$122k** SELL | vol 1,995 / OI 4,963
- **QQQ** CALL 660 2026-11-09 (3DTE): 203 @ 5.90 = **+$120k** BUY | vol 20,084 / OI 10
- **QQQ** CALL 660 2026-11-09 (3DTE): 200 @ 5.88 = **+$118k** BUY | vol 20,084 / OI 10
- **SPY** CALL 740 2026-11-06 (0DTE): 829 @ 1.25 = **+$104k** BUY | vol 282,178 / OI 314

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 722 2026-11-10 (4DTE): 501 traded vs OI 172
- **SPY** CALL 785 2026-11-12 (6DTE): 1,199 traded vs OI 1,186
- **SPY** CALL 775 2026-11-20 (14DTE): 15,443 traded vs OI 15,111
- **QQQ** PUT 670 2026-11-09 (3DTE): 1,883 traded vs OI 1,869
- **QQQ** PUT 590 2026-11-09 (3DTE): 2,247 traded vs OI 0
- **QQQ** CALL 694 2026-11-09 (3DTE): 502 traded vs OI 295
- **QQQ** CALL 663 2026-11-10 (4DTE): 553 traded vs OI 1
- **QQQ** PUT 590 2026-11-06 (0DTE): 1,780 traded vs OI 0
- **QQQ** PUT 590 2026-11-13 (7DTE): 2,577 traded vs OI 0
- **QQQ** PUT 590 2026-11-20 (14DTE): 1,774 traded vs OI 0
- **SMH** CALL 472.5 2026-11-09 (3DTE): 543 traded vs OI 0
- **NVDA** PUT 167.5 2026-11-13 (7DTE): 2,089 traded vs OI 0
- **NVDA** PUT 167.5 2026-11-11 (5DTE): 740 traded vs OI 0
- **NVDA** PUT 167.5 2026-11-09 (3DTE): 651 traded vs OI 0
- **TSLA** CALL 360 2026-12-04 (28DTE): 502 traded vs OI 136

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
