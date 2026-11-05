# GEX + FLOW SCAN - Thu Nov 05, 11:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:55 | **BABA** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/06 102P | 0.75 | 0.40 | -5% (9m) | **-47%** | +27% | 103.58 |
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 11.35 | +1355% (60m) | **+1355%** (done) | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.20 | -12% (0m) | **-58%** (done) | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.10 | -4% (0m) | **-87%** (done) | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:20:08 ET, last candle SPY 11:19, QQQ 11:19 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
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
| 1 | **SPY** | 744.04 | TREND (flow not with it) | **PUTS** | 66 | none: 665 puts 0-7DTE > 38 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (233 contracts' greeks worked out here) | NEG -$12.2B | 770.1 | 760 | 750 | +$1.0B | +$105k bull / -$37.1M bear | SHORT (clean 36, ADX 66, RVol 3.1) |
| 2 | **IWM** | 275.51 | TREND (flow not with it) | **PUTS** | 64 | 11/05 274P @ 0.66 (delta 0.31) = est +100% at 273.42 | NEG -$2.3B | 285.91 | 285 | 270 | +$48.0M | +$381k bull / -$595k bear | SHORT (clean 36, ADX 55, RVol 2.7) |
| 3 | **ORCL** | 114.36 | TREND (flow not with it) | **PUTS** | 52 | none: 23 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$56.4M | - | 125 | 115 | +$3.1M | +$56k bull / -$317k bear | SHORT (clean 34, ADX 56, RVol 1.8) |
| 4 | **SMH** | 461.52 | - | **-** | 38 | - | NEG -$318.3M | - | 505 | 500 | +$39.9M | +$0 bull / -$1.6M bear | out (clean 35, ADX 61, RVol 4.0) |
| 5 | **DELL** | 330.23 | - | **-** | 38 | - | NEG -$14.7M | - | 360 | 350 | +$7.2M | +$0 bull / -$322k bear | out (clean 35, ADX 49, RVol 2.4) |
| 6 | **AVGO** | 303.10 | - | **-** | 35 | - | NEG -$123.6M | - | 330 | 300 | +$7.5M | +$0 bull / -$472k bear | out (clean 32, ADX 54, RVol 2.8) |
| 7 | **PLTR** | 156.57 | - | **-** | 34 | - | NEG -$46.2M | - | 165 | 160 | +$11.9M | +$0 bull / -$278k bear | out (clean 28, ADX 50, RVol 1.4) |
| 8 | **QQQ** | 658.81 | - | **-** | 33 | - | NEG -$4.9B | - | 700 | 680 | +$746.2M | +$0 bull / -$29.1M bear | out (clean 35, ADX 65, RVol 2.9) |
| 9 | **MSFT** | 542.05 | - | **-** | 33 | - | POS +$881.9M | - | 540 | 500 | +$18.2M | +$0 bull / -$3.7M bear | out (clean 32, ADX 55, RVol 2.5) |
| 10 | **COIN** | 138.25 | - | **-** | 33 | - | POS +$22.2M | - | 142 | 135 | +$1.9M | +$0 bull / -$38k bear | out (clean 34, ADX 62, RVol 1.0) |
| 11 | **NVDA** | 185.85 | - | **-** | 32 | - | NEG -$272.5M | - | 200 | 190 | +$62.2M | +$0 bull / -$2.5M bear | out (clean 33, ADX 66, RVol 3.1) |
| 12 | **AMD** | 424.36 | - | **-** | 31 | - | NEG -$105.5M | - | 430 | 440 | +$41.5M | +$0 bull / -$1.7M bear | out (clean 34, ADX 54, RVol 1.7) |
| 13 | **ARM** | 169.12 | - | **-** | 31 | - | NEG -$6.7M | - | 180 | 180 | +$1.4M | +$0 bull / -$72k bear | out (clean 28, ADX 57, RVol 2.1) |
| 14 | **TSLA** | 349.42 | - | **-** | 30 | - | NEG -$158.8M | - | 370 | 350 | +$97.9M | +$0 bull / -$3.4M bear | out (clean 35, ADX 55, RVol 2.4) |
| 15 | **AMZN** | 258.30 | - | **-** | 30 | - | POS +$368.3M | - | 265 | 250 | +$29.7M | +$0 bull / -$618k bear | out (clean 34, ADX 35, RVol 1.6) |
| 16 | **MU** | 700.82 | - | **-** | 30 | - | NEG -$104.6M | - | 700 | 750 | +$143.0M | +$0 bull / -$17.6M bear | out (clean 33, ADX 69, RVol 3.9) |
| 17 | **META** | 602.75 | - | **-** | 28 | - | NEG -$112.0M | 621.96 | 650 | 600 | +$24.9M | +$0 bull / -$8.7M bear | out (clean 34, ADX 45, RVol 2.3) |
| 18 | **MSTR** | 130.30 | - | **-** | 28 | - | POS +$71.3M | - | 135 | 125 | +$2.8M | +$0 bull / -$239k bear | out (clean 34, ADX 62, RVol 2.9) |
| 19 | **GOOGL** | 283.44 | - | **-** | 26 | - | POS +$24.8M | 281.39 | 285 | 290 | +$8.7M | +$0 bull / -$232k bear | out (clean 35, ADX 30, RVol 1.2) |
| 20 | **HOOD** | 78.49 | - | **-** | 26 | - | NEG -$7.7M | - | 85 | 80 | +$1.7M | +$0 bull / -$57k bear | out (clean 32, ADX 67, RVol 1.0) |
| 21 | **AAPL** | 346.07 | - | **-** | 24 | - | POS +$565.9M | 334.02 | 350 | 340 | +$15.4M | +$956k bull / -$673k bear | out (clean 31, ADX 22, RVol 2.4) |
| 22 | **BABA** | 106.27 | - | **-** | 23 | - | POS +$20.8M | - | 110 | 100 | +$1.2M | - | out (clean 37, ADX 17, RVol 2.2) |
| 23 | **SHOP** | 141.82 | - | **-** | 22 | - | NEG -$5.2M | - | 144 | 135 | +$208k | - | out (clean 36, ADX 50, RVol 0.6) |
| 24 | **SMCI** | 26.96 | - | **-** | 21 | - | NEG -$2.9M | - | 28 | 27 | +$465k | - | out (clean 36, ADX 56, RVol 1.6) |
| 25 | **CRM** | 223.89 | - | **-** | 18 | - | NEG -$13.6M | - | 240 | 220 | +$452k | - | out (clean 34, ADX 18, RVol 0.8) |
| 26 | **UBER** | 68.35 | - | **-** | 14 | - | POS +$2.5M | 67.91 | 70 | 65 | +$180k | - | out (clean 32, ADX 19, RVol 1.1) |
| 27 | **NFLX** | 65.72 | - | **-** | 10 | - | POS +$30.6M | 61.85 | 65 | 65 | +$251k | - | out (clean 33, ADX 17, RVol 1.3) |

## Big prints this scan (161)
- **QQQ** PUT 635 2026-11-09 (4DTE): 1,000 @ 5.43 = **+$543k** BUY | vol 11,168 / OI 902
- **QQQ** PUT 635 2026-11-09 (4DTE): 981 @ 5.18 = **+$508k** BUY | vol 11,168 / OI 902
- **META** PUT 590 2026-11-06 (1DTE): 499 @ 9.64 = **+$481k** BUY | vol 5,871 / OI 3,807
- **QQQ** PUT 635 2026-11-09 (4DTE): 762 @ 5.66 = **+$431k** BUY | vol 11,168 / OI 902
- **IWM** PUT 272.5 2026-11-06 (1DTE): 2,455 @ 1.50 = **+$368k** BUY | vol 13,192 / OI 10,271
- **MU** PUT 730 2026-11-06 (1DTE): 49 @ 64.85 = **+$318k** BUY | vol 4,342 / OI 1,382
- **MU** PUT 720 2026-11-06 (1DTE): 49 @ 56.95 = **+$279k** BUY | vol 5,225 / OI 607
- **QQQ** PUT 679 2026-11-05 (0DTE): 100 @ 26.80 = **+$268k** BUY | vol 13,964 / OI 134
- **QQQ** PUT 645 2026-11-05 (0DTE): 980 @ 2.50 = **+$245k** BUY | vol 98,789 / OI 1,090
- **QQQ** PUT 675 2026-11-05 (0DTE): 100 @ 22.98 = **+$230k** BUY | vol 33,701 / OI 1,830
- **SPY** PUT 769 2026-11-09 (4DTE): 78 @ 28.62 = **+$223k** BUY | vol 310 / OI 1
- **SPY** PUT 769 2026-11-09 (4DTE): 78 @ 28.53 = **+$223k** BUY | vol 310 / OI 1
- **SMH** PUT 470 2026-11-06 (1DTE): 100 @ 22.00 = **+$220k** BUY | vol 11,888 / OI 11,200
- **QQQ** PUT 645 2026-11-12 (7DTE): 175 @ 12.30 = **+$215k** BUY | vol 875 / OI 1,134
- **SMH** PUT 450 2026-11-06 (1DTE): 190 @ 10.15 = **+$193k** BUY | vol 4,782 / OI 1,652

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 741 2026-11-11 (6DTE): 527 traded vs OI 0
- **SPY** CALL 786 2026-11-06 (1DTE): 1,342 traded vs OI 1,337
- **SPY** CALL 751 2026-11-10 (5DTE): 539 traded vs OI 80
- **SPY** CALL 737 2026-11-09 (4DTE): 514 traded vs OI 0
- **SPY** PUT 741 2026-11-10 (5DTE): 513 traded vs OI 11
- **SPY** CALL 754 2026-11-11 (6DTE): 528 traded vs OI 194
- **SPY** PUT 705 2026-11-05 (0DTE): 4,239 traded vs OI 1,976
- **SPY** PUT 735 2026-11-06 (1DTE): 25,425 traded vs OI 24,589
- **SPY** PUT 690 2026-11-06 (1DTE): 3,862 traded vs OI 3,569
- **SPY** PUT 732 2026-11-12 (7DTE): 501 traded vs OI 36
- **SPY** PUT 741 2026-11-13 (8DTE): 1,034 traded vs OI 1,016
- **SPY** CALL 739 2026-11-13 (8DTE): 542 traded vs OI 14
- **SPY** CALL 742 2026-11-13 (8DTE): 520 traded vs OI 24
- **SPY** PUT 731 2026-11-13 (8DTE): 2,141 traded vs OI 636
- **SPY** PUT 675 2026-11-20 (15DTE): 509 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
