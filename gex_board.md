# GEX + FLOW SCAN - Thu Nov 05, 11:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:55 | **BABA** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/06 102P | 0.75 | 0.59 | -5% (9m) | **-21%** | +27% | 103.58 |
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 11.35 | +1355% (60m) | **+1355%** (done) | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.20 | -12% (0m) | **-58%** (done) | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.10 | -4% (0m) | **-87%** (done) | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:10:08 ET, last candle SPY 11:09, QQQ 11:09 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:38 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 64 puts 0-1DTE > 1 priced 0.40-0.80 > 0 delta 0.15+ > 0 spread ok > 0 liquid  |
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (25 today, last 5)
- 11:10 IWM CALLS: price -0.10 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:05 IWM CALLS: price -1.05 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:00 IWM CALLS: price -1.16 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:55 IWM CALLS: price -2.06 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:50 HOOD CALLS: price -1.37 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMH** | 453.61 | FLOW SURGE | **CALLS** | 69 | none: 86 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$208.7M | - | 445 | 465 | +$43.5M | +$264k bull / -$215k bear | SHORT (clean 35, ADX 65, RVol 3.6) |
| 2 | **DELL** | 323.25 | TREND (flow not with it) | **PUTS** | 67 | none: 18 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$12.0M | - | 350 | 340 | +$7.6M | +$0 bull / -$322k bear | SHORT (clean 35, ADX 53, RVol 2.4) |
| 3 | **SPY** | 741.90 | TREND (flow not with it) | **PUTS** | 65 | none: 663 puts 0-7DTE > 27 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (223 contracts' greeks worked out here) | NEG -$11.8B | 770.09 | 760 | 740 | +$1.0B | +$13.6M bull / -$24.5M bear | SHORT (clean 36, ADX 68, RVol 2.6) |
| 4 | **QQQ** | 654.29 | TREND (flow not with it) | **PUTS** | 65 | none: 498 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (117 contracts' greeks worked out here) | NEG -$4.6B | - | 700 | 680 | +$776.4M | +$5.3M bull / -$14.8M bear | SHORT (clean 35, ADX 68, RVol 3.1) |
| 5 | **IWM** | 275.28 | FLOW SURGE | **CALLS** | 65 | 11/05 278C @ 0.51 (delta 0.23) = est +92% at 277.43 | NEG -$2.3B | 286.28 | 285 | 270 | +$50.2M | +$140k bull / -$76k bear | SHORT (clean 36, ADX 54, RVol 3.1) |
| 6 | **GOOGL** | 281.41 | FLIP CROSS up into positive gamma | **CALLS** | 61 | none: 66 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$11.3M | 280.72 | 285 | 290 | +$9.4M | +$28k bull / -$141k bear | SHORT (clean 35, ADX 32, RVol 1.8) |
| 7 | **COIN** | 135.04 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 61 | none: 25 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$12.5M | - | 142 | 135 | +$2.1M | - | SHORT (clean 34, ADX 64, RVol 1.2) |
| 8 | **MU** | 675.12 | FLOW SURGE | **CALLS** | 60 | none: 82 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | NEG -$65.0M | - | 700 | 700 | +$173.0M | +$9.3M bull / -$6.8M bear | SHORT (clean 34, ADX 74, RVol 2.8) |
| 9 | **NVDA** | 184.02 | FLOW SURGE | **CALLS** | 56 | none: 33 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$250.3M | - | 200 | 190 | +$65.9M | +$2.9M bull / -$1.4M bear | out (clean 33, ADX 69, RVol 3.0) |
| 10 | **PLTR** | 155.86 | FLOW SURGE | **CALLS** | 54 | none: 15 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$43.2M | - | 165 | 150 | +$12.3M | +$290k bull / -$163k bear | out (clean 28, ADX 52, RVol 2.0) |
| 11 | **ORCL** | 113.01 | FLOW SURGE | **CALLS** | 54 | none: 23 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$49.3M | - | 120 | 110 | +$4.6M | +$287k bull / -$50k bear | SHORT (clean 34, ADX 56, RVol 1.5) |
| 12 | **META** | 595.76 | TREND (flow not with it) | **PUTS** | 53 | none: 138 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | NEG -$154.1M | 629.36 | 650 | 600 | +$30.2M | +$0 bull / -$9.1M bear | SHORT (clean 34, ADX 49, RVol 1.9) |
| 13 | **AMD** | 412.84 | FLOW SURGE | **CALLS** | 51 | none: 99 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (12 contracts' greeks worked out here) | NEG -$91.3M | - | 430 | 440 | +$46.1M | +$1.6M bull / -$1.1M bear | SHORT (clean 34, ADX 58, RVol 1.5) |
| 14 | **AMZN** | 255.84 | FLOW SURGE | **CALLS** | 49 | none: 60 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$335.9M | - | 260 | 250 | +$31.5M | +$396k bull / -$257k bear | SHORT (clean 35, ADX 37, RVol 1.8) |
| 15 | **MSTR** | 126.96 | TREND (flow not with it) | **PUTS** | 49 | none: 25 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$36.4M | - | 135 | 125 | +$4.0M | +$232k bull / -$63k bear | SHORT (clean 34, ADX 67, RVol 2.6) |
| 16 | **TSLA** | 345.25 | TREND (flow not with it) | **PUTS** | 47 | none: 71 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$137.9M | - | 370 | 350 | +$103.0M | +$2.4M bull / -$2.2M bear | SHORT (clean 35, ADX 58, RVol 2.2) |
| 17 | **SMCI** | 26.31 | TREND (flow not with it) | **PUTS** | 45 | 11/06 25.5P @ 0.55 (delta 0.32) = est +41% at 25.45 | NEG -$2.2M | - | 28 | 27 | +$556k | - | SHORT (clean 36, ADX 61, RVol 1.5) |
| 18 | **AVGO** | 297.96 | - | **-** | 38 | - | NEG -$109.5M | - | 325 | 300 | +$8.3M | +$304k bull / -$438k bear | out (clean 32, ADX 59, RVol 3.5) |
| 19 | **MSFT** | 537.66 | - | **-** | 34 | - | POS +$783.9M | - | 540 | 500 | +$19.7M | +$428k bull / -$2.2M bear | out (clean 32, ADX 59, RVol 2.3) |
| 20 | **ARM** | 165.47 | - | **-** | 33 | - | NEG -$5.3M | - | 180 | 180 | +$1.6M | +$0 bull / -$44k bear | out (clean 28, ADX 60, RVol 2.0) |
| 21 | **SHOP** | 140.94 | - | **-** | 25 | - | NEG -$5.5M | - | 144 | 135 | +$236k | - | out (clean 36, ADX 55, RVol 0.6) |
| 22 | **BABA** | 105.44 | - | **-** | 24 | - | POS +$21.4M | - | 110 | 100 | +$1.2M | - | out (clean 37, ADX 19, RVol 2.0) |
| 23 | **AAPL** | 348.17 | - | **-** | 23 | - | POS +$624.6M | 333.45 | 350 | 340 | +$13.2M | +$1.2M bull / -$759k bear | out (clean 31, ADX 21, RVol 2.4) |
| 24 | **HOOD** | 76.88 | - | **-** | 18 | - | NEG -$7.4M | - | 83 | 80 | +$2.1M | - | out (clean 32, ADX 71, RVol 1.2) |
| 25 | **CRM** | 225.47 | - | **-** | 18 | - | NEG -$13.8M | - | 240 | 220 | +$330k | - | out (clean 34, ADX 20, RVol 1.5) |
| 26 | **UBER** | 68.09 | - | **-** | 15 | - | NEG -$1.1M | 68.47 | 70 | 65 | +$199k | - | out (clean 32, ADX 20, RVol 1.0) |
| 27 | **NFLX** | 65.73 | - | **-** | 10 | - | POS +$30.9M | 62.28 | 65 | 65 | +$247k | - | out (clean 33, ADX 18, RVol 1.3) |

## Big prints this scan (485)
- **SPY** PUT 755 2026-11-05 (0DTE): 855 @ 16.42 = **+$1.4M** BUY | vol 96,905 / OI 2,900
- **SPY** PUT 750 2026-11-05 (0DTE): 855 @ 11.96 = **+$1.0M** BUY | vol 161,480 / OI 6,007
- **SPY** PUT 754 2026-11-05 (0DTE): 699 @ 13.65 = **+$954k** BUY | vol 74,645 / OI 908
- **SPY** PUT 752 2026-11-05 (0DTE): 699 @ 11.85 = **+$828k** BUY | vol 79,576 / OI 392
- **SPY** PUT 740 2026-11-06 (1DTE): 1,000 @ 7.67 = **+$767k** BUY | vol 37,319 / OI 24,512
- **QQQ** PUT 635 2026-11-09 (4DTE): 935 @ 7.49 = **+$700k** BUY | vol 7,077 / OI 902
- **QQQ** CALL 663 2026-11-09 (4DTE): 995 @ 6.60 = **+$657k** SELL | vol 9,520 / OI 0
- **QQQ** CALL 660 2026-11-10 (5DTE): 616 @ 9.76 = **+$601k** SELL | vol 1,794 / OI 97
- **META** PUT 582.5 2026-11-09 (4DTE): 480 @ 11.65 = **+$559k** BUY | vol 1,075 / OI 72
- **QQQ** PUT 650 2026-11-05 (0DTE): 886 @ 6.06 = **+$537k** BUY | vol 87,261 / OI 3,473
- **SPY** PUT 719 2026-11-06 (1DTE): 3,284 @ 1.60 = **+$525k** BUY | vol 7,827 / OI 881
- **META** CALL 590 2026-11-06 (1DTE): 500 @ 10.40 = **+$520k** SELL | vol 1,280 / OI 58
- **META** CALL 592.5 2026-11-06 (1DTE): 500 @ 10.33 = **+$516k** SELL | vol 2,374 / OI 26
- **SPY** PUT 765 2026-11-06 (1DTE): 200 @ 25.05 = **+$501k** BUY | vol 11,398 / OI 6,355
- **META** PUT 585 2026-11-09 (4DTE): 400 @ 12.49 = **+$500k** BUY | vol 948 / OI 45

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 722 2026-11-06 (1DTE): 2,389 traded vs OI 2,206
- **SPY** PUT 739 2026-11-10 (5DTE): 552 traded vs OI 58
- **SPY** CALL 739 2026-11-06 (1DTE): 1,081 traded vs OI 304
- **SPY** PUT 746 2026-11-10 (5DTE): 505 traded vs OI 15
- **SPY** CALL 730 2026-11-05 (0DTE): 573 traded vs OI 15
- **SPY** CALL 765 2026-11-09 (4DTE): 3,433 traded vs OI 3,432
- **SPY** CALL 745 2026-11-09 (4DTE): 742 traded vs OI 98
- **SPY** PUT 723 2026-11-06 (1DTE): 2,811 traded vs OI 2,355
- **SPY** PUT 740 2026-11-10 (5DTE): 993 traded vs OI 902
- **SPY** PUT 704 2026-11-05 (0DTE): 881 traded vs OI 43
- **SPY** PUT 701 2026-11-09 (4DTE): 504 traded vs OI 406
- **SPY** PUT 756 2026-11-10 (5DTE): 597 traded vs OI 342
- **SPY** PUT 706 2026-11-05 (0DTE): 657 traded vs OI 155
- **SPY** CALL 735 2026-11-05 (0DTE): 840 traded vs OI 27
- **SPY** PUT 724 2026-11-06 (1DTE): 4,297 traded vs OI 3,725

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
