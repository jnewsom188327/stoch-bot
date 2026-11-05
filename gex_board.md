# GEX + FLOW SCAN - Thu Nov 05, 11:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:55 | **BABA** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/06 102P | 0.75 | 0.34 | -5% (9m) | **-55%** | +27% | 103.58 |
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 11.35 | +1355% (60m) | **+1355%** (done) | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.20 | -12% (0m) | **-58%** (done) | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.10 | -4% (0m) | **-87%** (done) | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:50:08 ET, last candle SPY 11:49, QQQ 11:49 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:44 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:38 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 64 puts 0-1DTE > 1 priced 0.40-0.80 > 0 delta 0.15+ > 0 spread ok > 0 liquid  |
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (26 today, last 5)
- 11:15 IWM CALLS: price -0.15 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:10 IWM CALLS: price -0.10 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:05 IWM CALLS: price -1.05 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:00 IWM CALLS: price -1.16 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:55 IWM CALLS: price -2.06 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMH** | 460.87 | FLOW SURGE | **CALLS** | 59 | none: 92 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$298.3M | - | 505 | 500 | +$38.1M | +$1.1M bull / -$322k bear | out (clean 35, ADX 50, RVol 3.9) |
| 2 | **SPY** | 742.14 | FLOW SURGE | **CALLS** | 50 | none: 663 calls 0-7DTE > 27 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (227 contracts' greeks worked out here) | NEG -$12.2B | 769.37 | 760 | 740 | +$1.0B | +$4.1M bull / -$578k bear | out (clean 36, ADX 60, RVol 1.9) |
| 3 | **IWM** | 274.51 | TREND (flow not with it) | **PUTS** | 49 | 11/05 273P @ 0.62 (delta 0.31) = est +143% at 272 | NEG -$2.5B | 286.48 | 285 | 270 | +$48.9M | - | SHORT (clean 36, ADX 52, RVol 2.2) |
| 4 | **PLTR** | 155.75 | FLOW SURGE | **CALLS** | 43 | none: 15 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | NEG -$42.9M | - | 165 | 150 | +$12.7M | +$435k bull / +$0 bear | out (clean 28, ADX 42, RVol 0.7) |
| 5 | **QQQ** | 658.02 | - | **-** | 30 | - | NEG -$4.8B | - | 700 | 680 | +$707.3M | +$11.6M bull / -$895k bear | out (clean 35, ADX 54, RVol 1.8) |
| 6 | **NVDA** | 186.33 | - | **-** | 30 | - | NEG -$272.2M | - | 200 | 190 | +$54.5M | +$887k bull / -$1.6M bear | out (clean 33, ADX 53, RVol 2.8) |
| 7 | **AVGO** | 302.62 | - | **-** | 30 | - | NEG -$121.5M | - | 330 | 300 | +$7.0M | +$119k bull / +$0 bear | out (clean 31, ADX 39, RVol 1.8) |
| 8 | **MU** | 698.78 | - | **-** | 30 | - | NEG -$100.2M | - | 700 | 750 | +$162.9M | +$10.6M bull / -$1.3M bear | out (clean 34, ADX 50, RVol 3.0) |
| 9 | **SHOP** | 145.39 | TREND (flow not with it) | **CALLS** | 30 | none: 23 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$4.3M | - | 144 | 135 | -$43k | - | LONG (clean 37, ADX 36, RVol 1.2) |
| 10 | **TSLA** | 345.62 | - | **-** | 29 | - | NEG -$148.0M | - | 370 | 350 | +$92.7M | +$3.4M bull / -$131k bear | out (clean 34, ADX 45, RVol 2.1) |
| 11 | **MSFT** | 542.38 | - | **-** | 29 | - | POS +$877.8M | - | 540 | 500 | +$19.1M | +$395k bull / -$184k bear | out (clean 32, ADX 42, RVol 1.1) |
| 12 | **DELL** | 331.23 | - | **-** | 29 | - | NEG -$15.2M | - | 360 | 350 | +$5.7M | +$0 bull / -$25k bear | out (clean 35, ADX 36, RVol 1.4) |
| 13 | **MSTR** | 129.33 | - | **-** | 27 | - | POS +$59.4M | - | 135 | 125 | +$3.7M | +$248k bull / +$0 bear | out (clean 34, ADX 46, RVol 1.8) |
| 14 | **AMD** | 420.77 | - | **-** | 26 | - | NEG -$104.3M | - | 430 | 440 | +$34.0M | +$1.7M bull / -$28k bear | out (clean 33, ADX 44, RVol 1.1) |
| 15 | **AMZN** | 261.41 | - | **-** | 26 | - | POS +$404.0M | - | 265 | 250 | +$24.2M | +$0 bull / -$367k bear | out (clean 34, ADX 25, RVol 1.7) |
| 16 | **AAPL** | 345.18 | - | **-** | 23 | - | POS +$483.8M | 334.4 | 350 | 330 | +$16.5M | +$436k bull / -$30k bear | out (clean 31, ADX 25, RVol 1.8) |
| 17 | **META** | 607.59 | - | **-** | 23 | - | NEG -$88.2M | 621.19 | 650 | 600 | +$18.2M | +$1.1M bull / -$1.3M bear | out (clean 34, ADX 30, RVol 2.2) |
| 18 | **GOOGL** | 283.94 | - | **-** | 23 | - | POS +$24.5M | 281.12 | 285 | 290 | +$8.4M | +$58k bull / +$0 bear | out (clean 35, ADX 22, RVol 0.9) |
| 19 | **HOOD** | 78.33 | - | **-** | 23 | - | NEG -$7.7M | - | 85 | 80 | +$1.7M | +$80k bull / +$0 bear | out (clean 32, ADX 52, RVol 0.6) |
| 20 | **COIN** | 136.06 | - | **-** | 21 | - | POS +$17.0M | - | 142 | 135 | +$1.9M | - | out (clean 33, ADX 52, RVol 0.6) |
| 21 | **BABA** | 106.79 | - | **-** | 20 | - | POS +$19.8M | - | 110 | 110 | +$1.2M | - | out (clean 37, ADX 20, RVol 1.7) |
| 22 | **ARM** | 169.66 | - | **-** | 19 | - | NEG -$7.0M | - | 180 | 180 | +$1.4M | - | out (clean 28, ADX 45, RVol 1.3) |
| 23 | **SMCI** | 26.89 | - | **-** | 17 | - | NEG -$3.1M | - | 28 | 27 | +$407k | - | out (clean 36, ADX 43, RVol 1.1) |
| 24 | **CRM** | 223.41 | - | **-** | 17 | - | NEG -$15.0M | - | 240 | 220 | +$487k | - | out (clean 33, ADX 16, RVol 0.7) |
| 25 | **ORCL** | 114.75 | - | **-** | 16 | - | NEG -$56.3M | - | 125 | 115 | +$2.9M | - | out (clean 34, ADX 47, RVol 0.8) |
| 26 | **NFLX** | 65.60 | - | **-** | 14 | - | POS +$32.5M | 62.09 | 65 | 65 | +$775k | - | out (clean 32, ADX 18, RVol 1.1) |
| 27 | **UBER** | 68.25 | - | **-** | 11 | - | POS +$1.1M | 68 | 70 | 65 | +$172k | - | out (clean 32, ADX 14, RVol 0.7) |

## Big prints this scan (141)
- **QQQ** CALL 660 2026-11-10 (5DTE): 752 @ 13.20 = **+$993k** BUY | vol 3,680 / OI 97
- **QQQ** PUT 655 2026-11-06 (1DTE): 717 @ 6.92 = **+$496k** SELL | vol 17,067 / OI 5,889
- **META** PUT 600 2026-11-06 (1DTE): 482 @ 7.20 = **+$347k** BUY | vol 9,601 / OI 3,434
- **TSLA** PUT 345 2026-11-06 (1DTE): 434 @ 6.05 = **+$263k** SELL | vol 26,464 / OI 1,324
- **META** PUT 590 2026-11-06 (1DTE): 482 @ 4.20 = **+$202k** BUY | vol 6,792 / OI 3,807
- **QQQ** PUT 652 2026-11-06 (1DTE): 369 @ 5.33 = **+$197k** SELL | vol 8,256 / OI 279
- **MU** PUT 670 2026-11-06 (1DTE): 200 @ 9.70 = **+$194k** SELL | vol 15,121 / OI 0
- **MU** PUT 670 2026-11-06 (1DTE): 200 @ 9.45 = **+$189k** SELL | vol 15,121 / OI 0
- **MU** PUT 670 2026-11-06 (1DTE): 200 @ 8.80 = **+$176k** SELL | vol 15,121 / OI 0
- **QQQ** CALL 690 2026-11-12 (7DTE): 500 @ 3.49 = **+$174k** BUY | vol 1,726 / OI 184
- **QQQ** CALL 690 2026-11-12 (7DTE): 476 @ 3.66 = **+$174k** BUY | vol 1,726 / OI 184
- **MU** PUT 700 2026-11-06 (1DTE): 90 @ 19.10 = **+$172k** SELL | vol 26,327 / OI 2,015
- **SPY** PUT 743 2026-11-05 (0DTE): 894 @ 1.92 = **+$172k** SELL | vol 111,591 / OI 1,127
- **MU** CALL 715 2026-11-06 (1DTE): 100 @ 17.10 = **+$171k** BUY | vol 4,178 / OI 5
- **QQQ** PUT 660 2026-11-05 (0DTE): 500 @ 3.40 = **+$170k** SELL | vol 124,418 / OI 2,574

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 745 2026-11-11 (6DTE): 544 traded vs OI 12
- **SPY** CALL 748 2026-11-11 (6DTE): 505 traded vs OI 1
- **SPY** CALL 742 2026-11-10 (5DTE): 501 traded vs OI 2
- **SPY** CALL 771 2026-11-10 (5DTE): 504 traded vs OI 115
- **SPY** PUT 712 2026-11-09 (4DTE): 507 traded vs OI 17
- **SPY** PUT 703 2026-11-05 (0DTE): 697 traded vs OI 18
- **SPY** CALL 763 2026-11-13 (8DTE): 880 traded vs OI 868
- **SPY** PUT 749 2026-11-11 (6DTE): 553 traded vs OI 23
- **SPY** PUT 759 2026-11-11 (6DTE): 553 traded vs OI 72
- **SPY** PUT 742 2026-11-11 (6DTE): 504 traded vs OI 168
- **SPY** CALL 765 2026-11-27 (22DTE): 774 traded vs OI 768
- **QQQ** PUT 657 2026-11-12 (7DTE): 635 traded vs OI 19
- **QQQ** PUT 670 2026-11-10 (5DTE): 511 traded vs OI 451
- **QQQ** CALL 653 2026-11-09 (4DTE): 501 traded vs OI 0
- **QQQ** CALL 687 2026-11-09 (4DTE): 520 traded vs OI 138

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
