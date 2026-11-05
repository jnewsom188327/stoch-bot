# GEX + FLOW SCAN - Thu Nov 05, 12:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:55 | **BABA** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/06 102P | 0.75 | 0.33 | -5% (9m) | **-56%** (done) | +27% | 103.58 |
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 11.35 | +1355% (60m) | **+1355%** (done) | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.20 | -12% (0m) | **-58%** (done) | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.10 | -4% (0m) | **-87%** (done) | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:50:08 ET, last candle SPY 12:49, QQQ 12:49 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:44 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:38 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 64 puts 0-1DTE > 1 priced 0.40-0.80 > 0 delta 0.15+ > 0 spread ok > 0 liquid  |
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (35 today, last 5)
- 12:50 IWM CALLS: price -0.60 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:45 IWM CALLS: price -0.70 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:40 IWM CALLS: price -0.66 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:20 IWM CALLS: under EMA 20 - flow says one way, price says the other
- 12:15 IWM CALLS: price -0.86 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 272.00 | FLOW SURGE | **CALLS** | 55 | 11/05 273C @ 0.60 (delta 0.35) = est +96% at 273.8 | NEG -$2.8B | 286.96 | 285 | 270 | +$61.7M | +$5.3M bull / +$0 bear | SHORT (clean 37, ADX 55, RVol 1.9) |
| 2 | **SPY** | 738.57 | FLOW SURGE | **CALLS** | 47 | none: 659 calls 0-7DTE > 26 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (261 contracts' greeks worked out here) | NEG -$12.9B | 770.02 | 760 | 740 | +$1.2B | +$5.3M bull / +$0 bear | SHORT (clean 36, ADX 57, RVol 1.1) |
| 3 | **MSFT** | 540.88 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 45 | none: 129 puts 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$848.1M | - | 540 | 500 | +$20.7M | +$322k bull / -$37k bear | out (clean 32, ADX 32, RVol 0.7) |
| 4 | **SMH** | 455.18 | FLOW SURGE | **CALLS** | 44 | none: 89 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | NEG -$236.9M | - | 445 | 465 | +$41.1M | +$211k bull / +$0 bear | out (clean 35, ADX 42, RVol 0.8) |
| 5 | **NVDA** | 182.91 | TREND (flow not with it) | **PUTS** | 39 | none: 36 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$241.6M | - | 200 | 190 | +$68.8M | +$1.1M bull / +$0 bear | SHORT (clean 33, ADX 45, RVol 1.4) |
| 6 | **TSLA** | 342.52 | TREND (flow not with it) | **PUTS** | 39 | none: 71 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$131.6M | - | 350 | 350 | +$109.8M | +$1.7M bull / -$519k bear | SHORT (clean 35, ADX 42, RVol 1.5) |
| 7 | **GOOGL** | 284.81 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 39 | none: 69 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$34.7M | 280.69 | 285 | 290 | +$8.5M | +$116k bull / +$0 bear | out (clean 35, ADX 13, RVol 0.7) |
| 8 | **COIN** | 135.33 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 39 | none: 25 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | POS +$11.7M | - | 142 | 135 | +$2.1M | - | out (clean 33, ADX 44, RVol 0.5) |
| 9 | **MU** | 680.62 | TREND (flow not with it) | **PUTS** | 37 | none: 85 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | NEG -$67.2M | - | 700 | 700 | +$216.8M | +$9.3M bull / +$0 bear | SHORT (clean 33, ADX 37, RVol 1.5) |
| 10 | **QQQ** | 653.74 | - | **-** | 28 | - | NEG -$4.6B | - | 700 | 680 | +$806.4M | +$5.2M bull / +$0 bear | out (clean 36, ADX 46, RVol 0.7) |
| 11 | **AVGO** | 298.66 | - | **-** | 28 | - | NEG -$107.0M | - | 325 | 300 | +$8.6M | +$257k bull / +$0 bear | out (clean 32, ADX 32, RVol 1.2) |
| 12 | **AMD** | 415.69 | - | **-** | 24 | - | NEG -$96.0M | - | 430 | 440 | +$35.7M | +$793k bull / -$170k bear | out (clean 34, ADX 38, RVol 0.9) |
| 13 | **AAPL** | 345.16 | - | **-** | 23 | - | POS +$495.1M | 334.47 | 350 | 330 | +$20.5M | +$333k bull / -$355k bear | out (clean 31, ADX 33, RVol 0.9) |
| 14 | **ORCL** | 114.34 | - | **-** | 23 | - | NEG -$56.2M | - | 125 | 115 | +$2.8M | +$27k bull / +$0 bear | out (clean 33, ADX 35, RVol 0.8) |
| 15 | **HOOD** | 77.21 | - | **-** | 23 | - | NEG -$7.9M | - | 83 | 80 | +$2.1M | +$91k bull / +$0 bear | out (clean 32, ADX 42, RVol 0.5) |
| 16 | **MSTR** | 127.75 | - | **-** | 21 | - | POS +$40.8M | - | 135 | 125 | +$3.6M | +$52k bull / +$0 bear | out (clean 34, ADX 35, RVol 0.4) |
| 17 | **AMZN** | 261.07 | - | **-** | 20 | - | POS +$396.4M | - | 265 | 250 | +$22.1M | +$181k bull / +$0 bear | out (clean 35, ADX 14, RVol 0.7) |
| 18 | **PLTR** | 155.46 | - | **-** | 19 | - | NEG -$45.4M | - | 165 | 150 | +$13.2M | - | out (clean 28, ADX 34, RVol 0.6) |
| 19 | **CRM** | 222.22 | - | **-** | 18 | - | NEG -$15.8M | - | 240 | 220 | +$549k | - | out (clean 34, ADX 18, RVol 0.9) |
| 20 | **META** | 606.65 | - | **-** | 17 | - | NEG -$101.1M | 621.28 | 650 | 600 | +$19.9M | +$733k bull / +$0 bear | out (clean 34, ADX 15, RVol 0.5) |
| 21 | **DELL** | 323.69 | - | **-** | 17 | - | NEG -$12.3M | - | 350 | 340 | +$6.3M | - | out (clean 35, ADX 32, RVol 0.6) |
| 22 | **BABA** | 106.67 | - | **-** | 17 | - | POS +$21.5M | - | 110 | 110 | +$1.4M | - | out (clean 37, ADX 16, RVol 0.4) |
| 23 | **NFLX** | 65.42 | - | **-** | 15 | - | POS +$30.6M | 62.04 | 65 | 65 | +$896k | - | out (clean 33, ADX 25, RVol 0.7) |
| 24 | **ARM** | 168.35 | - | **-** | 15 | - | NEG -$6.9M | - | 180 | 180 | +$1.4M | - | out (clean 27, ADX 31, RVol 0.7) |
| 25 | **SMCI** | 26.68 | - | **-** | 14 | - | NEG -$3.0M | - | 28 | 27 | +$453k | - | out (clean 36, ADX 32, RVol 0.8) |
| 26 | **UBER** | 68.46 | - | **-** | 8 | - | POS +$3.6M | 67.94 | 70 | 65 | +$169k | - | out (clean 32, ADX 9, RVol 0.3) |
| 27 | **SHOP** | 143.53 | - | **-** | 8 | - | NEG -$5.3M | - | 144 | 135 | -$131k | - | out (clean 38, ADX 20, RVol 0.4) |

## Big prints this scan (124)
- **IWM** PUT 277 2026-11-06 (1DTE): 2,371 @ 5.14 = **+$1.2M** SELL | vol 15,141 / OI 32,973
- **IWM** PUT 277 2026-11-06 (1DTE): 2,088 @ 5.14 = **+$1.1M** SELL | vol 15,141 / OI 32,973
- **MU** CALL 690 2026-11-06 (1DTE): 100 @ 22.40 = **+$224k** BUY | vol 8,397 / OI 24
- **SPY** PUT 748 2026-11-05 (0DTE): 200 @ 9.44 = **+$189k** SELL | vol 121,840 / OI 735
- **SPY** PUT 735 2026-11-06 (1DTE): 500 @ 3.74 = **+$187k** SELL | vol 39,185 / OI 24,589
- **AMD** CALL 420 2026-11-06 (1DTE): 150 @ 12.25 = **+$184k** BUY | vol 4,241 / OI 51
- **MU** PUT 680 2026-11-06 (1DTE): 100 @ 18.04 = **+$180k** SELL | vol 18,112 / OI 702
- **AAPL** PUT 345 2026-11-09 (4DTE): 350 @ 4.45 = **+$156k** BUY | vol 3,740 / OI 285
- **TSLA** CALL 335 2026-11-06 (1DTE): 120 @ 12.75 = **+$153k** BUY | vol 1,253 / OI 132
- **QQQ** PUT 666 2026-11-06 (1DTE): 100 @ 15.04 = **+$150k** SELL | vol 6,376 / OI 149
- **QQQ** PUT 666 2026-11-06 (1DTE): 100 @ 14.60 = **+$146k** SELL | vol 6,376 / OI 149
- **IWM** PUT 277 2026-11-06 (1DTE): 281 @ 5.15 = **+$145k** SELL | vol 15,141 / OI 32,973
- **SPY** PUT 745 2026-11-05 (0DTE): 200 @ 6.82 = **+$136k** SELL | vol 166,920 / OI 4,460
- **MU** CALL 690 2026-11-06 (1DTE): 50 @ 23.20 = **+$116k** BUY | vol 8,397 / OI 24
- **SPY** PUT 742 2026-11-05 (0DTE): 261 @ 4.44 = **+$116k** SELL | vol 136,861 / OI 1,035

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 740 2026-11-11 (6DTE): 504 traded vs OI 40
- **SPY** CALL 756 2026-11-13 (8DTE): 1,149 traded vs OI 1,147
- **SPY** PUT 733 2026-11-12 (7DTE): 527 traded vs OI 35
- **SPY** CALL 750 2026-11-30 (25DTE): 1,789 traded vs OI 1,714
- **SPY** CALL 747 2026-11-30 (25DTE): 764 traded vs OI 736
- **QQQ** CALL 700 2026-11-06 (1DTE): 19,485 traded vs OI 18,314
- **QQQ** PUT 650 2026-11-18 (13DTE): 536 traded vs OI 0
- **IWM** CALL 272 2026-11-06 (1DTE): 562 traded vs OI 288
- **IWM** CALL 276 2026-11-13 (8DTE): 896 traded vs OI 873
- **IWM** CALL 272.5 2026-11-06 (1DTE): 521 traded vs OI 79
- **IWM** CALL 270 2026-11-05 (0DTE): 621 traded vs OI 12
- **AAPL** PUT 360 2026-11-06 (1DTE): 503 traded vs OI 94
- **AAPL** CALL 355 2026-12-04 (29DTE): 586 traded vs OI 337
- **MSFT** CALL 550 2026-11-06 (1DTE): 4,085 traded vs OI 4,076
- **COIN** PUT 126 2026-11-06 (1DTE): 500 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
