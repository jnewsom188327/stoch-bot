# GEX + FLOW SCAN - Thu Nov 05, 10:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 8.81 | +1029% (58m) | **+1029%** | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.17 | -12% (0m) | **-65%** | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.10 | -4% (0m) | **-87%** (done) | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:50:08 ET, last candle SPY 10:49, QQQ 10:49 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:38 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 64 puts 0-1DTE > 1 priced 0.40-0.80 > 0 delta 0.15+ > 0 spread ok > 0 liquid  |
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (21 today, last 5)
- 10:50 HOOD CALLS: price -1.37 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:50 IWM CALLS: price -2.31 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:45 IWM CALLS: price -1.06 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:40 ORCL CALLS: price -0.25 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:40 IWM CALLS: price -0.79 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMH** | 456.53 | FLOW SURGE | **CALLS** | 69 | none: 86 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$280.0M | - | 500 | 500 | +$42.6M | +$16.9M bull / +$0 bear | SHORT (clean 35, ADX 59, RVol 2.7) |
| 2 | **QQQ** | 654.20 | FLOW SURGE | **CALLS** | 65 | none: 498 calls 0-7DTE > 47 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (210 contracts' greeks worked out here) | NEG -$4.5B | - | 700 | 680 | +$746.8M | +$18.7M bull / +$0 bear | SHORT (clean 35, ADX 63, RVol 2.9) |
| 3 | **IWM** | 275.99 | FLOW SURGE | **CALLS** | 65 | 11/05 278C @ 0.59 (delta 0.28) = est +87% at 277.93 | NEG -$2.2B | 286.8 | 285 | 270 | +$40.6M | +$2.3M bull / +$0 bear | SHORT (clean 35, ADX 47, RVol 3.3) |
| 4 | **AVGO** | 297.16 | FLOW SURGE | **CALLS** | 63 | none: 59 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$103.9M | - | 325 | 300 | +$7.8M | +$252k bull / -$79k bear | out (clean 31, ADX 56, RVol 3.5) |
| 5 | **SPY** | 741.84 | FLOW SURGE | **CALLS** | 61 | none: 663 calls 0-7DTE > 26 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (402 contracts' greeks worked out here) | NEG -$11.6B | 771.36 | 760 | 740 | +$885.2M | +$34.4M bull / +$0 bear | SHORT (clean 35, ADX 64, RVol 2.2) |
| 6 | **AMD** | 414.02 | FLOW SURGE | **CALLS** | 60 | none: 99 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | NEG -$93.8M | - | 430 | 440 | +$46.7M | +$3.0M bull / -$59k bear | SHORT (clean 33, ADX 52, RVol 2.3) |
| 7 | **META** | 587.46 | FLOW SURGE | **CALLS** | 59 | none: 132 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (13 contracts' greeks worked out here) | NEG -$186.1M | - | 600 | 600 | +$46.9M | +$8.1M bull / +$0 bear | SHORT (clean 34, ADX 46, RVol 2.0) |
| 8 | **PLTR** | 154.44 | FLOW SURGE | **CALLS** | 59 | none: 15 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$40.0M | - | 165 | 150 | +$12.6M | +$238k bull / +$0 bear | out (clean 28, ADX 52, RVol 2.5) |
| 9 | **DELL** | 326.27 | FLOW SURGE | **CALLS** | 59 | none: 19 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | NEG -$12.3M | - | 350 | 340 | +$7.1M | +$126k bull / -$116k bear | SHORT (clean 34, ADX 50, RVol 1.7) |
| 10 | **NVDA** | 184.57 | FLOW SURGE | **CALLS** | 58 | none: 36 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$249.5M | - | 200 | 190 | +$59.1M | +$3.0M bull / -$1.5M bear | out (clean 32, ADX 66, RVol 3.8) |
| 11 | **MU** | 678.55 | FLOW SURGE | **CALLS** | 58 | none: 82 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (13 contracts' greeks worked out here) | NEG -$65.3M | - | 700 | 700 | +$164.8M | +$8.4M bull / +$0 bear | out (clean 33, ADX 70, RVol 3.4) |
| 12 | **MSTR** | 126.51 | FLOW SURGE | **CALLS** | 56 | none: 26 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | POS +$31.5M | - | 135 | 125 | +$4.6M | +$281k bull / +$0 bear | SHORT (clean 34, ADX 68, RVol 2.5) |
| 13 | **HOOD** | 76.88 | FLOW SURGE | **CALLS** | 55 | 11/06 81C @ 0.66 (delta 0.22) = est +134% at 80 | NEG -$7.3M | - | 83 | 80 | +$2.2M | +$53k bull / +$0 bear | out (clean 31, ADX 65, RVol 2.8) |
| 14 | **ARM** | 167.47 | FLOW SURGE | **CALLS** | 55 | none: 11 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$5.6M | - | 180 | 180 | +$1.6M | +$30k bull / +$0 bear | out (clean 27, ADX 57, RVol 2.4) |
| 15 | **SMCI** | 26.38 | TREND (flow not with it) | **PUTS** | 54 | 11/06 25.5P @ 0.61 (delta 0.35) = est +38% at 25.57 | NEG -$2.6M | - | 28 | 27 | +$562k | - | SHORT (clean 36, ADX 57, RVol 2.1) |
| 16 | **TSLA** | 345.50 | TREND (flow not with it) | **PUTS** | 53 | none: 74 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | NEG -$144.4M | - | 370 | 350 | +$96.4M | +$3.9M bull / -$1.4M bear | SHORT (clean 35, ADX 55, RVol 3.4) |
| 17 | **COIN** | 136.47 | FLOW SURGE | **CALLS** | 52 | none: 27 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$16.3M | - | 142 | 135 | +$2.0M | +$25k bull / +$0 bear | SHORT (clean 33, ADX 59, RVol 1.2) |
| 18 | **ORCL** | 114.31 | FLOW SURGE | **CALLS** | 52 | none: 23 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$55.4M | - | 125 | 110 | +$2.8M | +$55k bull / +$0 bear | SHORT (clean 33, ADX 50, RVol 1.2) |
| 19 | **GOOGL** | 279.81 | FLOW SURGE | **CALLS** | 50 | none: 69 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | NEG -$12.4M | 280.99 | 285 | 290 | +$10.5M | +$741k bull / +$0 bear | SHORT (clean 35, ADX 27, RVol 1.6) |
| 20 | **AMZN** | 254.57 | FLOW SURGE | **CALLS** | 49 | none: 63 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | POS +$307.2M | - | 260 | 250 | +$33.6M | +$1.6M bull / -$27k bear | SHORT (clean 34, ADX 32, RVol 1.6) |
| 21 | **MSFT** | 537.14 | FLOW SURGE | **CALLS** | 48 | none: 129 calls 0-7DTE > 13 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (13 contracts' greeks worked out here) | POS +$769.8M | - | 540 | 500 | +$19.7M | +$782k bull / +$0 bear | out (clean 32, ADX 54, RVol 1.8) |
| 22 | **SHOP** | 139.14 | TREND (flow not with it) | **PUTS** | 47 | none: 26 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$7.3M | - | 144 | 135 | +$242k | - | SHORT (clean 36, ADX 58, RVol 1.1) |
| 23 | **BABA** | 105.66 | - | **-** | 27 | - | POS +$20.3M | - | 110 | 100 | +$1.2M | - | out (clean 37, ADX 22, RVol 2.3) |
| 24 | **AAPL** | 347.15 | - | **-** | 25 | - | POS +$540.6M | 333.43 | 350 | 330 | +$17.9M | +$1.4M bull / +$0 bear | out (clean 31, ADX 19, RVol 1.8) |
| 25 | **CRM** | 226.19 | - | **-** | 19 | - | NEG -$13.1M | - | 240 | 220 | +$248k | - | out (clean 34, ADX 22, RVol 2.3) |
| 26 | **UBER** | 68.27 | - | **-** | 15 | - | POS +$2.0M | 67.89 | 70 | 65 | +$168k | - | out (clean 32, ADX 18, RVol 1.4) |
| 27 | **NFLX** | 65.62 | - | **-** | 14 | - | POS +$30.0M | 61.89 | 65 | 65 | +$385k | - | out (clean 33, ADX 19, RVol 1.2) |

## Big prints this scan (240)
- **SPY** CALL 740 2026-11-10 (5DTE): 1,600 @ 13.37 = **+$2.1M** BUY | vol 8,046 / OI 44
- **SPY** CALL 740 2026-11-10 (5DTE): 1,343 @ 13.53 = **+$1.8M** BUY | vol 8,046 / OI 44
- **SPY** CALL 740 2026-11-10 (5DTE): 1,020 @ 13.39 = **+$1.4M** BUY | vol 8,046 / OI 44
- **SPY** CALL 740 2026-11-10 (5DTE): 1,019 @ 13.38 = **+$1.4M** BUY | vol 8,046 / OI 44
- **SPY** CALL 740 2026-11-10 (5DTE): 1,019 @ 13.37 = **+$1.4M** BUY | vol 8,046 / OI 44
- **SPY** CALL 750 2026-11-10 (5DTE): 1,600 @ 6.96 = **+$1.1M** BUY | vol 16,489 / OI 289
- **SPY** PUT 755 2026-11-06 (1DTE): 1,094 @ 9.40 = **+$1.0M** SELL | vol 15,735 / OI 8,694
- **SPY** CALL 750 2026-11-10 (5DTE): 1,343 @ 6.93 = **+$931k** BUY | vol 16,489 / OI 289
- **QQQ** PUT 675 2026-11-06 (1DTE): 500 @ 17.01 = **+$850k** SELL | vol 49,541 / OI 46,203
- **SPY** CALL 740 2026-11-10 (5DTE): 581 @ 13.38 = **+$777k** BUY | vol 8,046 / OI 44
- **SPY** CALL 740 2026-11-10 (5DTE): 580 @ 13.40 = **+$777k** BUY | vol 8,046 / OI 44
- **SPY** CALL 750 2026-11-10 (5DTE): 1,020 @ 6.97 = **+$711k** BUY | vol 16,489 / OI 289
- **SPY** CALL 750 2026-11-10 (5DTE): 1,019 @ 6.96 = **+$709k** BUY | vol 16,489 / OI 289
- **SPY** CALL 750 2026-11-10 (5DTE): 1,019 @ 6.96 = **+$709k** BUY | vol 16,489 / OI 289
- **SPY** PUT 749 2026-11-06 (1DTE): 1,094 @ 5.90 = **+$645k** SELL | vol 12,955 / OI 10,969

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 764 2026-11-11 (6DTE): 511 traded vs OI 75
- **SPY** PUT 740 2026-11-06 (1DTE): 26,392 traded vs OI 24,512
- **SPY** CALL 756 2026-11-10 (5DTE): 545 traded vs OI 196
- **SPY** PUT 726 2026-11-09 (4DTE): 529 traded vs OI 46
- **SPY** CALL 770 2026-11-06 (1DTE): 18,360 traded vs OI 17,674
- **SPY** CALL 740 2026-11-10 (5DTE): 8,046 traded vs OI 44
- **SPY** PUT 712 2026-11-05 (0DTE): 835 traded vs OI 13
- **SPY** PUT 680 2026-11-06 (1DTE): 1,541 traded vs OI 0
- **SPY** PUT 745 2026-11-06 (1DTE): 14,963 traded vs OI 14,342
- **SPY** CALL 749 2026-11-09 (4DTE): 642 traded vs OI 35
- **SPY** CALL 748 2026-11-09 (4DTE): 577 traded vs OI 20
- **SPY** PUT 749 2026-11-06 (1DTE): 12,955 traded vs OI 10,969
- **SPY** CALL 800 2026-11-17 (12DTE): 961 traded vs OI 9
- **SPY** PUT 746 2026-11-12 (7DTE): 530 traded vs OI 33
- **SPY** CALL 792 2026-11-27 (22DTE): 587 traded vs OI 538

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
