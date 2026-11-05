# GEX + FLOW SCAN - Thu Nov 05, 10:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 2.90 | +272% (28m) | **+272%** | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.24 | -12% (0m) | **-50%** | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.20 | -4% (0m) | **-74%** | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:20:08 ET, last candle SPY 10:19, QQQ 10:19 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (11 today, last 5)
- 10:20 BABA CALLS: price -0.42 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:20 HOOD CALLS: price -0.79 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:20 IWM CALLS: price -1.18 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:15 HOOD CALLS: price -0.66 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:15 IWM CALLS: price -1.43 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DELL** | 330.08 | FLOW SURGE | **CALLS** | 69 | none: 20 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$15.1M | - | 360 | 350 | +$5.3M | +$343k bull / +$0 bear | SHORT (clean 33, ADX 46, RVol 2.6) |
| 2 | **SMH** | 464.83 | FLOW SURGE | **CALLS** | 68 | none: 95 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$357.9M | - | 505 | 500 | +$13.2M | +$5.4M bull / +$0 bear | SHORT (clean 34, ADX 49, RVol 3.3) |
| 3 | **QQQ** | 661.36 | FLOW SURGE | **CALLS** | 67 | none: 530 calls 0-7DTE > 44 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (131 contracts' greeks worked out here) | NEG -$5.3B | - | 700 | 680 | +$546.9M | +$53.3M bull / +$0 bear | SHORT (clean 34, ADX 52, RVol 3.2) |
| 4 | **MSFT** | 540.56 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 66 | none: 129 puts 0-7DTE > 15 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (13 contracts' greeks worked out here) | POS +$870.1M | - | 540 | 500 | +$12.8M | +$3.5M bull / -$330k bear | out (clean 31, ADX 44, RVol 2.7) |
| 5 | **AVGO** | 303.96 | FLOW SURGE | **CALLS** | 65 | none: 65 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$125.7M | - | 330 | 300 | +$5.6M | +$43k bull / +$0 bear | out (clean 30, ADX 51, RVol 3.6) |
| 6 | **PLTR** | 156.59 | FLOW SURGE | **CALLS** | 65 | none: 15 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | NEG -$45.8M | - | 165 | 160 | +$11.1M | +$523k bull / +$0 bear | out (clean 28, ADX 44, RVol 3.4) |
| 7 | **SPY** | 748.88 | FLOW SURGE | **CALLS** | 64 | none: 667 calls 0-7DTE > 23 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (253 contracts' greeks worked out here) | NEG -$11.0B | 769.47 | 760 | 750 | +$544.5M | +$13.4M bull / +$0 bear | SHORT (clean 34, ADX 52, RVol 2.4) |
| 8 | **SHOP** | 139.41 | TREND (flow not with it) | **PUTS** | 64 | none: 26 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$6.8M | - | 144 | 135 | +$150k | - | SHORT (clean 35, ADX 52, RVol 3.3) |
| 9 | **NVDA** | 186.27 | FLOW SURGE | **CALLS** | 63 | none: 36 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$276.1M | - | 200 | 190 | +$56.5M | +$7.8M bull / +$0 bear | out (clean 32, ADX 61, RVol 4.8) |
| 10 | **TSLA** | 349.29 | TREND (flow not with it) | **PUTS** | 63 | none: 76 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$160.0M | - | 370 | 350 | +$85.3M | +$506k bull / -$6.5M bear | SHORT (clean 34, ADX 53, RVol 6.7) |
| 11 | **AMD** | 422.05 | FLOW SURGE | **CALLS** | 63 | none: 102 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (11 contracts' greeks worked out here) | NEG -$107.7M | - | 430 | 440 | +$40.7M | +$3.0M bull / -$35k bear | out (clean 32, ADX 43, RVol 3.1) |
| 12 | **MU** | 700.76 | FLOW SURGE | **CALLS** | 63 | none: 94 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$111.8M | - | 700 | 750 | +$153.1M | +$17.7M bull / +$0 bear | out (clean 32, ADX 60, RVol 4.9) |
| 13 | **MSTR** | 131.63 | FLOW SURGE | **CALLS** | 62 | none: 26 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | POS +$76.7M | - | 135 | 125 | +$4.3M | +$371k bull / +$0 bear | SHORT (clean 33, ADX 62, RVol 2.6) |
| 14 | **ARM** | 169.84 | FLOW SURGE | **CALLS** | 59 | none: 12 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$7.1M | - | 180 | 180 | +$1.2M | +$43k bull / +$0 bear | out (clean 27, ADX 52, RVol 3.2) |
| 15 | **HOOD** | 78.90 | FLOW SURGE | **CALLS** | 58 | 11/06 83C @ 0.69 (delta 0.23) = est +31% at 80 | NEG -$7.9M | - | 85 | 80 | +$1.9M | +$45k bull / +$0 bear | out (clean 30, ADX 52, RVol 2.4) |
| 16 | **BABA** | 106.35 | FLOW SURGE | **CALLS** | 58 | 11/06 109C @ 0.73 (delta 0.27) = est +42% at 107.87 | POS +$21.7M | - | 110 | 110 | +$994k | +$162k bull / +$0 bear | out (clean 37, ADX 30, RVol 3.6) |
| 17 | **META** | 597.18 | FLOW SURGE | **CALLS** | 56 | none: 138 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | NEG -$171.3M | 628.26 | 650 | 600 | +$26.0M | +$5.0M bull / +$0 bear | out (clean 33, ADX 36, RVol 2.6) |
| 18 | **IWM** | 278.75 | FLOW SURGE | **CALLS** | 54 | 11/05 281C @ 0.47 (delta 0.25) = est +44% at 280 | NEG -$1.7B | 285.77 | 285 | 270 | +$19.6M | +$159k bull / +$0 bear | SHORT (clean 34, ADX 33, RVol 2.1) |
| 19 | **AMZN** | 257.49 | FLOW SURGE | **CALLS** | 53 | none: 63 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$359.5M | - | 260 | 250 | +$25.4M | +$1.1M bull / +$0 bear | out (clean 34, ADX 23, RVol 2.5) |
| 20 | **SMCI** | 26.82 | TREND (flow not with it) | **PUTS** | 52 | 11/06 25.5P @ 0.40 (delta 0.26) = est +45% at 25.98 | NEG -$3.1M | - | 28 | 27 | +$393k | - | SHORT (clean 35, ADX 50, RVol 1.6) |
| 21 | **AAPL** | 349.70 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 51 | none: 84 puts 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (16 contracts' greeks worked out here) | POS +$683.9M | 333.56 | 350 | 340 | +$8.4M | +$1.5M bull / -$155k bear | out (clean 31, ADX 19, RVol 2.3) |
| 22 | **GOOGL** | 283.68 | FLOW SURGE | **CALLS** | 46 | none: 66 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$31.2M | 281.27 | 285 | 290 | +$8.2M | +$1.9M bull / +$0 bear | out (clean 35, ADX 24, RVol 1.9) |
| 23 | **COIN** | 138.85 | - | **-** | 30 | - | POS +$24.0M | - | 142 | 135 | +$1.6M | - | out (clean 32, ADX 47, RVol 1.3) |
| 24 | **ORCL** | 117.84 | - | **-** | 27 | - | NEG -$57.4M | - | 125 | 120 | +$2.0M | - | out (clean 33, ADX 45, RVol 1.1) |
| 25 | **CRM** | 223.79 | - | **-** | 21 | - | NEG -$14.5M | - | 240 | 220 | +$279k | - | out (clean 34, ADX 17, RVol 2.1) |
| 26 | **UBER** | 68.80 | - | **-** | 16 | - | POS +$5.9M | 67.97 | 70 | 65 | +$126k | - | out (clean 32, ADX 22, RVol 1.3) |
| 27 | **NFLX** | 65.82 | - | **-** | 13 | - | POS +$29.6M | 61.87 | 65 | 65 | +$236k | - | out (clean 33, ADX 22, RVol 1.2) |

## Big prints this scan (348)
- **SPY** PUT 760 2026-11-06 (1DTE): 2,206 @ 8.60 = **+$1.9M** SELL | vol 17,899 / OI 11,725
- **SPY** PUT 760 2026-11-06 (1DTE): 1,714 @ 6.90 = **+$1.2M** SELL | vol 17,899 / OI 11,725
- **SPY** CALL 755 2026-11-10 (5DTE): 1,944 @ 6.05 = **+$1.2M** BUY | vol 4,281 / OI 767
- **QQQ** PUT 685 2026-11-05 (0DTE): 480 @ 20.09 = **+$964k** SELL | vol 8,092 / OI 2,551
- **SMH** PUT 480 2026-11-06 (1DTE): 576 @ 13.50 = **+$778k** SELL | vol 2,051 / OI 4,947
- **QQQ** PUT 685 2026-11-05 (0DTE): 355 @ 20.09 = **+$713k** SELL | vol 8,092 / OI 2,551
- **QQQ** PUT 685 2026-11-05 (0DTE): 355 @ 20.09 = **+$713k** SELL | vol 8,092 / OI 2,551
- **QQQ** PUT 678 2026-11-05 (0DTE): 480 @ 13.49 = **+$648k** SELL | vol 18,378 / OI 265
- **SMH** PUT 475 2026-11-06 (1DTE): 600 @ 10.70 = **+$642k** SELL | vol 1,891 / OI 1,734
- **QQQ** CALL 653 2026-11-06 (1DTE): 391 @ 16.00 = **+$626k** BUY | vol 498 / OI 0
- **SPY** PUT 765 2026-11-05 (0DTE): 495 @ 11.79 = **+$584k** SELL | vol 19,175 / OI 2,962
- **SMH** PUT 480 2026-11-06 (1DTE): 415 @ 12.80 = **+$531k** SELL | vol 2,051 / OI 4,947
- **QQQ** PUT 670 2026-11-05 (0DTE): 867 @ 5.73 = **+$497k** SELL | vol 52,456 / OI 11,268
- **QQQ** PUT 678 2026-11-05 (0DTE): 355 @ 13.49 = **+$479k** SELL | vol 18,378 / OI 265
- **QQQ** PUT 678 2026-11-05 (0DTE): 355 @ 13.49 = **+$479k** SELL | vol 18,378 / OI 265

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 750 2026-11-06 (1DTE): 4,368 traded vs OI 1,460
- **SPY** PUT 675 2026-11-10 (5DTE): 554 traded vs OI 0
- **SPY** PUT 717 2026-11-06 (1DTE): 1,489 traded vs OI 1,160
- **SPY** PUT 729 2026-11-06 (1DTE): 1,652 traded vs OI 1,473
- **SPY** PUT 779 2026-11-05 (0DTE): 727 traded vs OI 0
- **SPY** PUT 718 2026-11-06 (1DTE): 768 traded vs OI 642
- **SPY** PUT 754 2026-11-06 (1DTE): 6,116 traded vs OI 5,579
- **SPY** CALL 752 2026-11-06 (1DTE): 911 traded vs OI 883
- **SPY** CALL 760 2026-11-06 (1DTE): 10,939 traded vs OI 10,142
- **SPY** CALL 779 2026-11-05 (0DTE): 847 traded vs OI 663
- **SPY** PUT 753 2026-11-10 (5DTE): 607 traded vs OI 136
- **SPY** PUT 734 2026-11-06 (1DTE): 1,879 traded vs OI 1,669
- **SPY** CALL 754 2026-11-06 (1DTE): 3,933 traded vs OI 2,472
- **SPY** CALL 774 2026-11-06 (1DTE): 2,515 traded vs OI 2,175
- **SPY** PUT 739 2026-11-06 (1DTE): 2,702 traded vs OI 2,636

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
