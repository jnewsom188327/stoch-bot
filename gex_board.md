# GEX + FLOW SCAN - Fri Oct 30, 01:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:50:08 ET, last candle SPY 13:49, QQQ 13:49 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 12:45 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:32 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:31 | SPY | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 45 puts 0-1DTE > 1 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |
| 11:05 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 12:40 NVDA CALLS: under EMA 20 - flow says one way, price says the other
- 11:20 ARM CALLS: under EMA 20 - flow says one way, price says the other
- 11:20 COIN PUTS: price +0.22 over the last 15 min - flow says one way, price says the other
- 11:15 MSTR PUTS: price +1.54 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 11:10 MSTR PUTS: price +1.77 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DELL** | 416.93 | TREND (flow not with it) | **PUTS** | 58 | none: 66 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (52 contracts' greeks worked out here) | NEG -$49.1M | - | 440 | 425 | +$5.2M | +$0 bull / -$68k bear | SHORT (clean 34, ADX 60, RVol 2.1) |
| 2 | **AAPL** | 345.52 | PINNED between the walls (positive gamma) - chop | **-** | 35 | - | POS +$420.5M | 342.16 | 345 | 345 | +$4.5M | +$4.9M bull / +$0 bear | out (clean 31, ADX 21, RVol 1.3) |
| 3 | **NVDA** | 203.01 | - | **-** | 28 | - | NEG -$440.3M | 211.52 | 210 | 200 | +$35.7M | +$1.5M bull / +$0 bear | out (clean 28, ADX 50, RVol 0.8) |
| 4 | **AMD** | 500.40 | - | **-** | 28 | - | NEG -$183.2M | 520.61 | 550 | 500 | +$32.6M | +$576k bull / -$1.7M bear | out (clean 30, ADX 51, RVol 1.3) |
| 5 | **SPY** | 754.68 | - | **-** | 27 | - | NEG -$16.0B | 771.94 | 800 | 750 | +$197.3M | +$5.1M bull / +$0 bear | out (clean 27, ADX 44, RVol 1.6) |
| 6 | **ARM** | 202.15 | - | **-** | 27 | - | NEG -$20.3M | - | 220 | 205 | +$868k | +$33k bull / -$196k bear | out (clean 25, ADX 32, RVol 1.9) |
| 7 | **SMH** | 517.40 | - | **-** | 26 | - | NEG -$632.1M | - | 532.5 | 505 | +$7.2M | +$224k bull / -$372k bear | out (clean 30, ADX 53, RVol 0.9) |
| 8 | **SHOP** | 154.66 | - | **-** | 26 | - | NEG -$13.6M | - | 150 | 157.5 | +$778k | - | out (clean 27, ADX 47, RVol 3.1) |
| 9 | **QQQ** | 688.34 | - | **-** | 25 | - | NEG -$10.3B | - | 720 | 690 | +$119.9M | +$4.6M bull / +$0 bear | out (clean 28, ADX 48, RVol 1.8) |
| 10 | **IWM** | 278.19 | - | **-** | 25 | - | NEG -$1.3B | 281.21 | 278 | 278 | +$11.4M | +$0 bull / -$62k bear | out (clean 28, ADX 44, RVol 1.2) |
| 11 | **MU** | 872.58 | - | **-** | 25 | - | NEG -$315.4M | 921.07 | 880 | 880 | +$65.9M | +$3.6M bull / -$404k bear | out (clean 30, ADX 40, RVol 1.1) |
| 12 | **NFLX** | 62.07 | - | **-** | 23 | - | NEG -$23.5M | 62.72 | 62 | 62 | +$1.3M | +$0 bull / -$33k bear | out (clean 30, ADX 21, RVol 0.9) |
| 13 | **AVGO** | 324.09 | - | **-** | 23 | - | NEG -$158.5M | - | 340 | 320 | +$1.4M | +$0 bull / -$26k bear | out (clean 29, ADX 45, RVol 1.2) |
| 14 | **HOOD** | 82.90 | - | **-** | 23 | - | NEG -$35.5M | - | 85 | 85 | +$1.3M | +$0 bull / -$60k bear | out (clean 32, ADX 50, RVol 0.8) |
| 15 | **MSFT** | 521.91 | - | **-** | 20 | - | POS +$508.6M | 517.83 | 525 | 525 | +$4.6M | +$0 bull / -$292k bear | out (clean 26, ADX 17, RVol 0.8) |
| 16 | **GOOGL** | 279.08 | - | **-** | 18 | - | NEG -$224.6M | - | 280 | 280 | +$155k | +$63k bull / -$75k bear | out (clean 32, ADX 37, RVol 0.6) |
| 17 | **PLTR** | 184.56 | - | **-** | 18 | - | NEG -$74.8M | 192.31 | 185 | 185 | +$1.4M | +$503k bull / +$0 bear | out (clean 26, ADX 30, RVol 0.7) |
| 18 | **SMCI** | 31.77 | - | **-** | 18 | - | NEG -$4.7M | 33.01 | 32 | 32 | +$760k | - | out (clean 30, ADX 52, RVol 0.8) |
| 19 | **MSTR** | 129.34 | - | **-** | 18 | - | NEG -$27.5M | - | 135 | 130 | -$3.9M | +$58k bull / +$0 bear | out (clean 28, ADX 26, RVol 0.6) |
| 20 | **AMZN** | 239.46 | - | **-** | 17 | - | NEG -$172.6M | 245.23 | 250 | 240 | -$5.5M | +$693k bull / -$181k bear | out (clean 30, ADX 13, RVol 1.3) |
| 21 | **META** | 618.23 | - | **-** | 16 | - | NEG -$87.3M | 620.97 | 625 | 625 | +$2.5M | +$259k bull / +$0 bear | out (clean 28, ADX 24, RVol 0.6) |
| 22 | **COIN** | 138.48 | - | **-** | 16 | - | NEG -$14.9M | - | 140 | 140 | -$1.7M | - | out (clean 27, ADX 49, RVol 3.1) |
| 23 | **TSLA** | 397.70 | - | **-** | 15 | - | POS +$381.2M | 391.74 | 400 | 400 | -$8.9M | +$810k bull / -$948k bear | out (clean 29, ADX 12, RVol 0.7) |
| 24 | **UBER** | 64.97 | - | **-** | 14 | - | NEG -$34.9M | 66.15 | 65 | 65 | +$332k | - | out (clean 28, ADX 21, RVol 0.5) |
| 25 | **BABA** | 98.15 | - | **-** | 14 | - | NEG -$32.1M | 98.94 | 100 | 98 | +$546k | - | out (clean 29, ADX 18, RVol 0.6) |
| 26 | **ORCL** | 130.84 | - | **-** | 13 | - | POS +$49.7M | 128.73 | 130 | 130 | +$2.6M | - | out (clean 34, ADX 28, RVol 0.5) |
| 27 | **CRM** | 229.12 | - | **-** | 12 | - | NEG -$25.6M | 237.45 | 230 | 230 | +$299k | - | out (clean 28, ADX 31, RVol 0.4) |

## Big prints this scan (70)
- **SPY** PUT 760 2026-11-06 (7DTE): 1,136 @ 9.43 = **+$1.1M** SELL | vol 11,463 / OI 12,995
- **SPY** PUT 752 2026-11-06 (7DTE): 1,211 @ 6.24 = **+$756k** SELL | vol 4,694 / OI 1,360
- **SPY** PUT 765 2026-11-06 (7DTE): 507 @ 12.66 = **+$642k** SELL | vol 5,556 / OI 6,242
- **SPY** PUT 747 2026-11-06 (7DTE): 1,211 @ 4.70 = **+$569k** SELL | vol 2,855 / OI 629
- **SPY** PUT 760 2026-11-06 (7DTE): 507 @ 9.76 = **+$495k** SELL | vol 11,463 / OI 12,995
- **TSLA** PUT 397.5 2026-11-04 (5DTE): 500 @ 7.70 = **+$385k** SELL | vol 2,890 / OI 304
- **SPY** PUT 752 2026-11-06 (7DTE): 499 @ 6.23 = **+$311k** SELL | vol 4,694 / OI 1,360
- **QQQ** PUT 720 2026-10-30 (0DTE): 90 @ 31.50 = **+$284k** SELL | vol 1,648 / OI 22,475
- **SPY** PUT 767 2026-11-04 (5DTE): 200 @ 12.98 = **+$260k** SELL | vol 18,327 / OI 29,783
- **MSFT** CALL 520 2026-11-06 (7DTE): 250 @ 9.44 = **+$236k** SELL | vol 795 / OI 303
- **SPY** PUT 747 2026-11-06 (7DTE): 499 @ 4.69 = **+$234k** SELL | vol 2,855 / OI 629
- **QQQ** PUT 690 2026-10-30 (0DTE): 941 @ 2.29 = **+$215k** SELL | vol 270,710 / OI 65,738
- **SPY** PUT 754 2026-11-02 (3DTE): 450 @ 3.20 = **+$144k** SELL | vol 18,646 / OI 800
- **QQQ** PUT 695 2026-10-30 (0DTE): 200 @ 6.65 = **+$133k** SELL | vol 175,234 / OI 18,389
- **SPY** CALL 755 2026-11-06 (7DTE): 165 @ 8.00 = **+$132k** BUY | vol 3,165 / OI 907

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 695 2026-11-02 (3DTE): 1,089 traded vs OI 1,074
- **SPY** PUT 700 2026-11-05 (6DTE): 736 traded vs OI 357
- **SPY** PUT 734 2026-10-30 (0DTE): 3,418 traded vs OI 2,315
- **SPY** CALL 785 2026-11-02 (3DTE): 1,961 traded vs OI 989
- **SPY** PUT 759 2026-11-20 (21DTE): 2,247 traded vs OI 2,149
- **SPY** CALL 780 2026-11-12 (13DTE): 539 traded vs OI 0
- **SPY** CALL 785 2026-11-11 (12DTE): 526 traded vs OI 132
- **SPY** PUT 719 2026-11-06 (7DTE): 574 traded vs OI 329
- **QQQ** CALL 730 2026-11-06 (7DTE): 5,046 traded vs OI 4,533
- **QQQ** CALL 684 2026-10-30 (0DTE): 538 traded vs OI 58
- **QQQ** PUT 675 2026-11-03 (4DTE): 1,851 traded vs OI 1,833
- **QQQ** CALL 730 2026-11-12 (13DTE): 515 traded vs OI 0
- **QQQ** CALL 735 2026-11-13 (14DTE): 2,229 traded vs OI 1,857
- **NVDA** PUT 215 2026-11-02 (3DTE): 3,161 traded vs OI 3,137
- **NVDA** CALL 205 2026-11-09 (10DTE): 521 traded vs OI 35

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
