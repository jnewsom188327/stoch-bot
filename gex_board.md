# GEX + FLOW SCAN - Thu Nov 12, 11:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:35 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 754P | 0.59 | 0.12 | +10% (1m) | **-80%** | +70% | 755 |
| 09:50 | **HOOD** | **PUTS** | TREND + FLOW | 11/13 79P | 0.55 | 0.36 | +5% (19m) | **-35%** (done) | +92% | 80 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 130C | 0.75 | 0.72 | +4% (60m) | **-4%** (done) | +59% | 126.9 |
| 09:45 | **SMCI** | **PUTS** | TREND + FLOW | 11/13 27P | 0.42 | 0.23 | -5% (6m) | **-45%** (done) | +57% | 27 |
| 09:45 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 753P | 0.79 | 0.31 | +23% (18m) | **-61%** (done) | +51% | 754.88 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:20:08 ET, last candle SPY 11:19, QQQ 11:19 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:03 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (3 today, last 5)
- 10:30 IWM CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:25 IWM CALLS: price -0.79 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:20 IWM CALLS: price -0.12 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **GOOGL** | 300.03 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 49 | none: 72 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | POS +$133.6M | 286.93 | 300 | 290 | -$3.1M | +$0 bull / -$227k bear | out (clean 29, ADX 28, RVol 2.0) |
| 2 | **AMD** | 592.75 | TREND (flow not with it) | **CALLS** | 39 | none: 138 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$193.0M | - | 600 | 550 | -$43.3M | +$0 bull / -$20.0M bear | LONG (clean 34, ADX 35, RVol 1.9) |
| 3 | **SHOP** | 149.64 | PINNED between the walls (positive gamma) - chop | **-** | 38 | - | POS +$5.9M | 143.72 | 150 | 150 | -$19k | - | out (clean 30, ADX 22, RVol 1.5) |
| 4 | **HOOD** | 84.53 | TREND (flow not with it) | **CALLS** | 33 | none: 16 calls 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +10% at the target (needs +20%) (1 contracts' greeks worked out here) | POS +$17.4M | - | 85 | 85 | -$376k | +$0 bull / -$33k bear | LONG (clean 33, ADX 28, RVol 1.3) |
| 5 | **MSTR** | 118.59 | - | **-** | 28 | - | NEG -$27.8M | - | 125 | 120 | -$3.6M | +$0 bull / -$545k bear | out (clean 27, ADX 31, RVol 2.0) |
| 6 | **SPY** | 762.55 | - | **-** | 24 | - | POS +$867.2M | 761.68 | 760 | 760 | -$156.1M | +$0 bull / -$1.9M bear | out (clean 31, ADX 27, RVol 1.1) |
| 7 | **NVDA** | 166.11 | - | **-** | 24 | - | NEG -$178.8M | - | 170 | 160 | -$118.1M | +$305k bull / -$8.8M bear | out (clean 33, ADX 29, RVol 1.6) |
| 8 | **QQQ** | 693.97 | - | **-** | 23 | - | POS +$677.0M | 690.83 | 700 | 680 | -$135.0M | +$0 bull / -$2.6M bear | out (clean 31, ADX 30, RVol 1.1) |
| 9 | **MSFT** | 528.40 | - | **-** | 23 | - | POS +$221.9M | 519.78 | 535 | 520 | -$4.8M | +$0 bull / -$400k bear | out (clean 31, ADX 35, RVol 0.8) |
| 10 | **ARM** | 204.35 | - | **-** | 22 | - | POS +$10.5M | - | 200 | 200 | -$387k | +$0 bull / -$37k bear | out (clean 31, ADX 23, RVol 0.4) |
| 11 | **AVGO** | 368.60 | - | **-** | 21 | - | POS +$133.6M | - | 380 | 350 | +$4.2M | +$0 bull / -$326k bear | out (clean 35, ADX 34, RVol 1.5) |
| 12 | **IWM** | 281.44 | - | **-** | 20 | - | NEG -$530.6M | 282.79 | 285 | 275 | -$2.2M | +$0 bull / -$52k bear | out (clean 34, ADX 38, RVol 0.6) |
| 13 | **META** | 626.49 | - | **-** | 20 | - | POS +$19.7M | 624.4 | 650 | 600 | +$165k | +$46k bull / -$264k bear | out (clean 28, ADX 42, RVol 1.0) |
| 14 | **AAPL** | 358.33 | - | **-** | 19 | - | POS +$1.2B | 341.03 | 360 | 360 | -$376k | +$89k bull / -$521k bear | out (clean 28, ADX 41, RVol 0.7) |
| 15 | **TSLA** | 392.26 | - | **-** | 17 | - | POS +$378.3M | - | 400 | 380 | +$7.1M | +$181k bull / -$577k bear | out (clean 29, ADX 24, RVol 0.5) |
| 16 | **SMCI** | 28.84 | - | **-** | 17 | - | POS +$4.9M | - | 30 | 30 | -$223k | - | out (clean 33, ADX 36, RVol 2.0) |
| 17 | **MU** | 795.31 | - | **-** | 17 | - | POS +$103.6M | - | 800 | 800 | -$2.9M | +$0 bull / -$4.8M bear | out (clean 31, ADX 30, RVol 0.8) |
| 18 | **BABA** | 94.60 | - | **-** | 17 | - | NEG -$18.3M | - | 100 | 100 | +$212k | - | out (clean 29, ADX 56, RVol 1.5) |
| 19 | **ORCL** | 128.73 | - | **-** | 16 | - | POS +$13.3M | - | 130 | 130 | -$1.2M | - | out (clean 29, ADX 26, RVol 0.7) |
| 20 | **SMH** | 508.69 | - | **-** | 13 | - | NEG -$63.3M | - | 500 | 500 | -$2.3M | - | out (clean 30, ADX 31, RVol 0.7) |
| 21 | **UBER** | 69.82 | - | **-** | 13 | - | POS +$16.5M | 68.34 | 70 | 70 | -$78k | - | out (clean 31, ADX 27, RVol 0.6) |
| 22 | **NFLX** | 63.59 | - | **-** | 12 | - | NEG -$8.9M | 64.12 | 65 | 65 | -$229k | - | out (clean 27, ADX 28, RVol 0.7) |
| 23 | **PLTR** | 172.22 | - | **-** | 12 | - | POS +$89.6M | - | 170 | 170 | -$531k | - | out (clean 27, ADX 35, RVol 0.4) |
| 24 | **COIN** | 134.24 | - | **-** | 11 | - | POS +$13.6M | 129.92 | 137 | 135 | -$67k | - | out (clean 29, ADX 34, RVol 1.7) |
| 25 | **AMZN** | 271.02 | - | **-** | 10 | - | POS +$509.6M | - | 270 | 270 | -$7.5M | - | out (clean 31, ADX 22, RVol 0.7) |
| 26 | **CRM** | 216.83 | - | **-** | 8 | - | NEG -$9.4M | - | 220 | 220 | -$18k | - | out (clean 28, ADX 22, RVol 0.7) |
| 27 | **DELL** | 367.01 | - | **-** | 6 | - | POS +$5.3M | - | 360 | 340 | +$69k | - | out (clean 36, ADX 25, RVol 0.8) |

## Big prints this scan (137)
- **AMD** CALL 590 2026-11-13 (1DTE): 897 @ 11.00 = **+$987k** SELL | vol 10,866 / OI 1,196
- **AMD** CALL 565 2026-11-16 (4DTE): 145 @ 29.20 = **+$423k** SELL | vol 827 / OI 104
- **SPY** CALL 760 2026-11-16 (4DTE): 900 @ 4.21 = **+$379k** SELL | vol 4,809 / OI 1,658
- **NVDA** CALL 160 2026-11-16 (4DTE): 500 @ 7.47 = **+$374k** SELL | vol 15,842 / OI 766
- **NVDA** CALL 160 2026-11-13 (1DTE): 500 @ 6.47 = **+$324k** SELL | vol 120,948 / OI 2,015
- **AMD** CALL 590 2026-11-13 (1DTE): 283 @ 10.85 = **+$307k** SELL | vol 10,866 / OI 1,196
- **AMD** CALL 590 2026-11-13 (1DTE): 226 @ 10.85 = **+$245k** SELL | vol 10,866 / OI 1,196
- **QQQ** PUT 693 2026-11-13 (1DTE): 440 @ 5.29 = **+$233k** BUY | vol 1,487 / OI 706
- **SPY** PUT 755 2026-11-13 (1DTE): 1,724 @ 1.26 = **+$217k** BUY | vol 20,702 / OI 9,753
- **QQQ** PUT 682 2026-11-13 (1DTE): 999 @ 1.83 = **+$183k** BUY | vol 6,480 / OI 2,662
- **NVDA** PUT 170 2026-11-16 (4DTE): 245 @ 7.20 = **+$176k** BUY | vol 3,853 / OI 3,775
- **AAPL** PUT 357.5 2026-11-13 (1DTE): 880 @ 1.70 = **+$150k** BUY | vol 11,985 / OI 867
- **NVDA** CALL 160 2026-11-13 (1DTE): 200 @ 7.25 = **+$145k** SELL | vol 120,948 / OI 2,015
- **SPY** CALL 760 2026-11-12 (0DTE): 917 @ 1.56 = **+$143k** SELL | vol 240,957 / OI 3,834
- **NVDA** CALL 160 2026-11-13 (1DTE): 200 @ 7.00 = **+$140k** SELL | vol 120,948 / OI 2,015

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 786 2026-11-13 (1DTE): 1,486 traded vs OI 1,151
- **SPY** CALL 776 2026-11-17 (5DTE): 603 traded vs OI 305
- **SPY** CALL 777 2026-11-16 (4DTE): 677 traded vs OI 586
- **SPY** CALL 773 2026-11-16 (4DTE): 1,419 traded vs OI 717
- **SPY** PUT 750 2026-11-17 (5DTE): 1,978 traded vs OI 1,863
- **SPY** CALL 771 2026-11-13 (1DTE): 4,007 traded vs OI 3,542
- **SPY** CALL 750 2026-11-12 (0DTE): 2,471 traded vs OI 2,413
- **SPY** CALL 762 2026-11-19 (7DTE): 510 traded vs OI 391
- **SPY** PUT 757 2026-12-11 (29DTE): 512 traded vs OI 227
- **QQQ** PUT 653 2026-11-17 (5DTE): 637 traded vs OI 196
- **QQQ** PUT 670 2026-11-16 (4DTE): 1,096 traded vs OI 1,080
- **QQQ** PUT 665 2026-11-16 (4DTE): 857 traded vs OI 832
- **QQQ** CALL 706 2026-11-13 (1DTE): 1,182 traded vs OI 1,003
- **QQQ** CALL 696 2026-11-16 (4DTE): 519 traded vs OI 192
- **QQQ** CALL 692 2026-11-16 (4DTE): 538 traded vs OI 175

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
