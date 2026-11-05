# GEX + FLOW SCAN - Thu Nov 05, 12:00 PM ET
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
Last 1m check 12:00:08 ET, last candle SPY 11:59, QQQ 11:59 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:44 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:38 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 64 puts 0-1DTE > 1 priced 0.40-0.80 > 0 delta 0.15+ > 0 spread ok > 0 liquid  |
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (28 today, last 5)
- 12:00 IWM CALLS: price -0.69 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:55 IWM CALLS: price -1.66 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:15 IWM CALLS: price -0.15 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:10 IWM CALLS: price -0.10 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:05 IWM CALLS: price -1.05 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 274.11 | FLOW SURGE | **CALLS** | 55 | 11/05 276C @ 0.40 (delta 0.25) = est +129% at 276.11 | NEG -$2.6B | 286.32 | 285 | 270 | +$50.7M | +$142k bull / +$0 bear | SHORT (clean 36, ADX 52, RVol 1.9) |
| 2 | **SMH** | 460.70 | FLOW SURGE | **CALLS** | 53 | none: 92 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$317.1M | - | 505 | 500 | +$39.4M | +$1.4M bull / +$0 bear | out (clean 35, ADX 48, RVol 2.0) |
| 3 | **SPY** | 742.20 | FLOW SURGE | **CALLS** | 48 | none: 663 calls 0-7DTE > 28 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (232 contracts' greeks worked out here) | NEG -$12.6B | 769.42 | 760 | 740 | +$1.1B | +$4.2M bull / +$0 bear | out (clean 36, ADX 58, RVol 1.6) |
| 4 | **PLTR** | 155.42 | FLOW SURGE | **CALLS** | 41 | none: 16 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$44.0M | - | 165 | 150 | +$13.0M | +$187k bull / +$0 bear | out (clean 28, ADX 41, RVol 0.5) |
| 5 | **DELL** | 329.59 | TREND (flow not with it) | **PUTS** | 37 | none: 20 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | NEG -$15.0M | - | 360 | 340 | +$5.9M | - | SHORT (clean 35, ADX 33, RVol 1.2) |
| 6 | **SHOP** | 144.78 | TREND (flow not with it) | **CALLS** | 31 | none: 23 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$4.6M | - | 144 | 135 | -$108k | +$0 bull / -$28k bear | LONG (clean 37, ADX 35, RVol 1.1) |
| 7 | **NVDA** | 186.24 | - | **-** | 30 | - | NEG -$262.4M | - | 200 | 190 | +$56.2M | +$1.1M bull / -$259k bear | out (clean 33, ADX 50, RVol 2.2) |
| 8 | **QQQ** | 657.50 | - | **-** | 29 | - | NEG -$5.0B | - | 700 | 680 | +$726.2M | +$13.9M bull / +$0 bear | out (clean 35, ADX 52, RVol 1.5) |
| 9 | **MSFT** | 542.48 | - | **-** | 29 | - | POS +$875.4M | - | 540 | 500 | +$19.1M | +$189k bull / -$133k bear | out (clean 32, ADX 39, RVol 1.3) |
| 10 | **MU** | 695.19 | - | **-** | 29 | - | NEG -$97.3M | - | 700 | 750 | +$174.0M | +$13.6M bull / +$0 bear | out (clean 34, ADX 47, RVol 1.9) |
| 11 | **TSLA** | 344.54 | - | **-** | 28 | - | NEG -$133.0M | - | 370 | 350 | +$96.1M | +$2.6M bull / +$0 bear | out (clean 34, ADX 44, RVol 1.9) |
| 12 | **AMD** | 419.40 | - | **-** | 25 | - | NEG -$103.5M | - | 430 | 440 | +$36.1M | +$436k bull / +$0 bear | out (clean 33, ADX 42, RVol 0.9) |
| 13 | **ORCL** | 114.76 | - | **-** | 25 | - | NEG -$54.9M | - | 125 | 115 | +$2.8M | +$118k bull / +$0 bear | out (clean 34, ADX 44, RVol 0.9) |
| 14 | **AAPL** | 345.41 | - | **-** | 24 | - | POS +$498.0M | 334.51 | 350 | 330 | +$18.0M | +$622k bull / +$0 bear | out (clean 31, ADX 27, RVol 1.8) |
| 15 | **AMZN** | 262.15 | - | **-** | 24 | - | POS +$406.7M | - | 265 | 250 | +$22.0M | +$0 bull / -$480k bear | out (clean 35, ADX 23, RVol 1.6) |
| 16 | **GOOGL** | 284.76 | - | **-** | 23 | - | POS +$27.8M | 281.24 | 290 | 290 | +$8.2M | +$30k bull / -$48k bear | out (clean 35, ADX 20, RVol 1.0) |
| 17 | **COIN** | 135.49 | - | **-** | 22 | - | POS +$14.6M | - | 142 | 135 | +$2.0M | - | out (clean 33, ADX 51, RVol 0.6) |
| 18 | **META** | 606.50 | - | **-** | 21 | - | NEG -$99.8M | 621.76 | 650 | 600 | +$19.5M | +$988k bull / -$711k bear | out (clean 34, ADX 26, RVol 1.6) |
| 19 | **AVGO** | 303.16 | - | **-** | 19 | - | NEG -$119.3M | - | 330 | 300 | +$7.2M | - | out (clean 31, ADX 36, RVol 1.4) |
| 20 | **BABA** | 107.21 | - | **-** | 19 | - | POS +$20.5M | - | 110 | 110 | +$1.2M | - | out (clean 37, ADX 21, RVol 1.0) |
| 21 | **ARM** | 169.51 | - | **-** | 17 | - | NEG -$7.1M | - | 180 | 180 | +$1.4M | - | out (clean 27, ADX 42, RVol 1.0) |
| 22 | **CRM** | 223.12 | - | **-** | 17 | - | NEG -$15.3M | - | 240 | 220 | +$494k | - | out (clean 34, ADX 16, RVol 0.6) |
| 23 | **SMCI** | 26.84 | - | **-** | 16 | - | NEG -$3.1M | - | 28 | 27 | +$432k | - | out (clean 36, ADX 40, RVol 0.9) |
| 24 | **MSTR** | 128.84 | - | **-** | 16 | - | POS +$52.4M | - | 135 | 125 | +$3.8M | - | out (clean 34, ADX 44, RVol 1.6) |
| 25 | **NFLX** | 65.62 | - | **-** | 14 | - | POS +$32.4M | 62.03 | 65 | 65 | +$768k | - | out (clean 32, ADX 18, RVol 0.8) |
| 26 | **HOOD** | 78.00 | - | **-** | 14 | - | NEG -$9.2M | - | 85 | 80 | +$1.8M | - | out (clean 32, ADX 49, RVol 0.6) |
| 27 | **UBER** | 68.46 | - | **-** | 10 | - | POS +$4.1M | 67.98 | 70 | 65 | +$172k | - | out (clean 32, ADX 14, RVol 0.6) |

## Big prints this scan (134)
- **QQQ** PUT 688 2026-11-05 (0DTE): 1,000 @ 27.94 = **+$2.8M** SELL | vol 2,680 / OI 629
- **QQQ** PUT 686 2026-11-05 (0DTE): 1,000 @ 25.97 = **+$2.6M** SELL | vol 5,558 / OI 273
- **TSLA** PUT 345 2026-11-06 (1DTE): 695 @ 6.10 = **+$424k** SELL | vol 27,998 / OI 1,324
- **QQQ** PUT 655 2026-11-06 (1DTE): 500 @ 5.97 = **+$298k** SELL | vol 18,611 / OI 5,889
- **QQQ** PUT 655 2026-11-06 (1DTE): 500 @ 5.97 = **+$298k** SELL | vol 18,611 / OI 5,889
- **QQQ** CALL 660 2026-11-06 (1DTE): 364 @ 7.44 = **+$271k** BUY | vol 22,631 / OI 333
- **MU** CALL 700 2026-11-06 (1DTE): 112 @ 23.10 = **+$259k** BUY | vol 16,153 / OI 61
- **QQQ** PUT 660 2026-11-05 (0DTE): 500 @ 3.98 = **+$199k** SELL | vol 132,417 / OI 2,574
- **MU** PUT 670 2026-11-06 (1DTE): 197 @ 9.15 = **+$180k** SELL | vol 16,740 / OI 0
- **SPY** CALL 746 2026-11-05 (0DTE): 794 @ 2.23 = **+$177k** BUY | vol 69,429 / OI 1
- **MU** PUT 670 2026-11-06 (1DTE): 183 @ 9.20 = **+$168k** SELL | vol 16,740 / OI 0
- **SPY** CALL 748 2026-11-05 (0DTE): 1,350 @ 1.20 = **+$162k** BUY | vol 70,299 / OI 81
- **QQQ** CALL 651 2026-11-06 (1DTE): 120 @ 13.19 = **+$158k** BUY | vol 1,598 / OI 0
- **TSLA** PUT 350 2026-11-06 (1DTE): 200 @ 7.90 = **+$158k** SELL | vol 38,525 / OI 4,953
- **SPY** CALL 746 2026-11-05 (0DTE): 610 @ 2.55 = **+$156k** BUY | vol 69,429 / OI 1

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 722 2026-11-10 (5DTE): 510 traded vs OI 134
- **SPY** PUT 725 2026-11-10 (5DTE): 1,514 traded vs OI 1,511
- **SPY** CALL 780 2026-11-09 (4DTE): 2,989 traded vs OI 2,707
- **SPY** PUT 721 2026-11-10 (5DTE): 504 traded vs OI 51
- **SPY** PUT 730 2026-11-10 (5DTE): 1,318 traded vs OI 1,302
- **SPY** CALL 800 2026-11-10 (5DTE): 1,714 traded vs OI 1,132
- **SPY** CALL 747 2026-11-12 (7DTE): 506 traded vs OI 0
- **SPY** PUT 731 2026-11-17 (12DTE): 545 traded vs OI 0
- **SPY** PUT 742 2026-11-16 (11DTE): 598 traded vs OI 61
- **SPY** PUT 727 2026-11-12 (7DTE): 520 traded vs OI 22
- **SPY** CALL 768 2026-11-16 (11DTE): 511 traded vs OI 67
- **SPY** CALL 757 2026-11-12 (7DTE): 569 traded vs OI 60
- **SPY** PUT 742 2026-11-12 (7DTE): 502 traded vs OI 40
- **SPY** CALL 750 2026-11-16 (11DTE): 600 traded vs OI 221
- **SPY** CALL 752 2026-11-20 (15DTE): 1,529 traded vs OI 1,240

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
