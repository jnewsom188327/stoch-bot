# GEX + FLOW SCAN - Thu Nov 12, 10:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:35 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 754P | 0.59 | 0.53 | +10% (1m) | **-10%** | +70% | 755 |
| 09:50 | **HOOD** | **PUTS** | TREND + FLOW | 11/13 79P | 0.55 | 0.38 | +5% (19m) | **-31%** | +92% | 80 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 130C | 0.75 | 0.67 | -1% (8m) | **-11%** | +59% | 126.9 |
| 09:45 | **SMCI** | **PUTS** | TREND + FLOW | 11/13 27P | 0.42 | 0.24 | -5% (6m) | **-43%** | +57% | 27 |
| 09:45 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 753P | 0.79 | 0.40 | +23% (18m) | **-49%** | +51% | 754.88 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:40:08 ET, last candle SPY 10:39, QQQ 10:39 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:03 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (3 today, last 5)
- 10:30 IWM CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:25 IWM CALLS: price -0.79 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:20 IWM CALLS: price -0.12 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NVDA** | 164.64 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 75 | none: 42 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$179.0M | - | 170 | 160 | -$92.7M | +$1.7M bull / -$12.1M bear | SHORT (clean 33, ADX 38, RVol 2.4) |
| 2 | **IWM** | 279.74 | TREND (flow not with it) | **PUTS** | 44 | 11/12 280P @ 0.76 (delta 0.56) = est +48% at 279 | NEG -$1.1B | 282.62 | 285 | 275 | +$6.7M | +$0 bull / -$74k bear | SHORT (clean 34, ADX 56, RVol 0.8) |
| 3 | **MU** | 775.62 | TREND (flow not with it) | **PUTS** | 42 | none: 128 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$86.9M | - | 800 | 800 | +$40.8M | +$1.1M bull / -$9.5M bear | SHORT (clean 32, ADX 43, RVol 1.0) |
| 4 | **MSTR** | 114.89 | - | **-** | 26 | - | NEG -$32.8M | - | 125 | 110 | -$2.2M | +$0 bull / -$119k bear | out (clean 27, ADX 37, RVol 1.0) |
| 5 | **AVGO** | 361.83 | - | **-** | 25 | - | POS +$132.3M | - | 350 | 350 | +$4.6M | +$942k bull / -$52k bear | out (clean 36, ADX 39, RVol 2.5) |
| 6 | **AMD** | 563.73 | - | **-** | 24 | - | POS +$189.8M | - | 600 | 550 | +$28.9M | +$1.6M bull / -$1.0M bear | out (clean 34, ADX 23, RVol 1.4) |
| 7 | **ORCL** | 126.16 | - | **-** | 24 | - | POS +$8.3M | 119.89 | 130 | 125 | -$691k | +$0 bull / -$30k bear | out (clean 29, ADX 29, RVol 0.6) |
| 8 | **SMH** | 498.70 | - | **-** | 23 | - | NEG -$127.3M | - | 500 | 475 | -$1.2M | +$0 bull / -$129k bear | out (clean 31, ADX 43, RVol 1.2) |
| 9 | **PLTR** | 169.93 | PINNED between the walls (positive gamma) - chop | **-** | 23 | - | POS +$86.6M | - | 170 | 170 | -$73k | - | out (clean 27, ADX 42, RVol 0.7) |
| 10 | **META** | 621.29 | - | **-** | 22 | - | NEG -$24.0M | 624.56 | 650 | 600 | +$1.5M | +$0 bull / -$149k bear | out (clean 29, ADX 57, RVol 0.8) |
| 11 | **MSFT** | 525.10 | - | **-** | 22 | - | POS +$136.3M | 519.26 | 535 | 520 | -$3.5M | +$60k bull / +$0 bear | out (clean 31, ADX 34, RVol 0.5) |
| 12 | **AMZN** | 269.26 | - | **-** | 21 | - | POS +$505.1M | - | 270 | 270 | -$5.4M | +$161k bull / -$94k bear | out (clean 31, ADX 30, RVol 0.7) |
| 13 | **DELL** | 357.30 | - | **-** | 21 | - | POS +$2.6M | 348.12 | 360 | 340 | -$582k | +$29k bull / -$155k bear | out (clean 37, ADX 37, RVol 1.1) |
| 14 | **ARM** | 199.43 | - | **-** | 21 | - | POS +$8.2M | - | 200 | 200 | -$113k | +$0 bull / -$100k bear | out (clean 31, ADX 34, RVol 0.8) |
| 15 | **TSLA** | 390.19 | - | **-** | 20 | - | POS +$348.2M | - | 400 | 380 | +$13.2M | +$532k bull / +$0 bear | out (clean 29, ADX 27, RVol 0.5) |
| 16 | **AAPL** | 357.66 | - | **-** | 20 | - | POS +$1.1B | 339.57 | 360 | 360 | -$252k | +$0 bull / -$106k bear | out (clean 29, ADX 44, RVol 1.0) |
| 17 | **BABA** | 94.63 | - | **-** | 20 | - | NEG -$18.2M | - | 100 | 100 | +$205k | - | out (clean 29, ADX 56, RVol 3.2) |
| 18 | **COIN** | 130.76 | - | **-** | 19 | - | NEG -$1.3M | 130.87 | 137 | 135 | +$265k | - | out (clean 30, ADX 46, RVol 1.1) |
| 19 | **SPY** | 757.89 | - | **-** | 17 | - | NEG -$2.4B | 760.91 | 760 | 760 | -$15.1M | +$0 bull / -$1.1M bear | out (clean 32, ADX 26, RVol 0.5) |
| 20 | **QQQ** | 686.64 | - | **-** | 17 | - | NEG -$651.8M | 690.18 | 700 | 680 | +$2k | +$0 bull / -$240k bear | out (clean 31, ADX 35, RVol 0.6) |
| 21 | **NFLX** | 63.26 | - | **-** | 14 | - | NEG -$15.3M | 64 | 65 | 65 | -$210k | - | out (clean 27, ADX 39, RVol 0.7) |
| 22 | **SMCI** | 28.02 | - | **-** | 14 | - | POS +$3.3M | - | 30 | 27 | -$64k | - | out (clean 34, ADX 50, RVol 1.5) |
| 23 | **SHOP** | 148.13 | - | **-** | 11 | - | POS +$4.5M | 143.51 | 150 | 140 | -$2k | - | out (clean 30, ADX 26, RVol 1.3) |
| 24 | **GOOGL** | 295.69 | - | **-** | 9 | - | POS +$106.1M | 288.66 | 300 | 290 | +$745k | - | out (clean 29, ADX 21, RVol 1.5) |
| 25 | **HOOD** | 82.20 | - | **-** | 9 | - | POS +$8.5M | 80.2 | 85 | 80 | +$36k | - | out (clean 34, ADX 31, RVol 1.0) |
| 26 | **UBER** | 69.73 | - | **-** | 8 | - | POS +$15.9M | 68.25 | 70 | 70 | -$2k | - | out (clean 31, ADX 34, RVol 1.0) |
| 27 | **CRM** | 215.68 | - | **-** | 6 | - | NEG -$8.7M | - | 220 | 220 | -$5k | - | out (clean 28, ADX 28, RVol 0.3) |

## Big prints this scan (124)
- **NVDA** CALL 162.5 2026-11-18 (6DTE): 1,760 @ 9.40 = **+$1.7M** SELL | vol 7,057 / OI 61
- **NVDA** CALL 157.5 2026-11-13 (1DTE): 625 @ 8.00 = **+$500k** SELL | vol 29,989 / OI 250
- **SPY** CALL 738 2026-11-12 (0DTE): 199 @ 18.72 = **+$373k** SELL | vol 416 / OI 216
- **MU** CALL 795 2026-11-13 (1DTE): 349 @ 8.50 = **+$297k** SELL | vol 3,470 / OI 462
- **MU** CALL 775 2026-11-18 (6DTE): 65 @ 31.50 = **+$205k** MID | vol 491 / OI 814
- **NVDA** CALL 160 2026-11-13 (1DTE): 300 @ 6.65 = **+$200k** SELL | vol 110,771 / OI 2,015
- **NVDA** CALL 157.5 2026-11-13 (1DTE): 245 @ 8.00 = **+$196k** SELL | vol 29,989 / OI 250
- **NVDA** PUT 162.5 2026-11-13 (1DTE): 499 @ 3.05 = **+$152k** BUY | vol 25,825 / OI 20,581
- **NVDA** PUT 160 2026-11-18 (6DTE): 195 @ 6.55 = **+$128k** BUY | vol 3,498 / OI 3,836
- **NVDA** CALL 157.5 2026-11-13 (1DTE): 156 @ 8.00 = **+$125k** SELL | vol 29,989 / OI 250
- **NVDA** CALL 165 2026-11-13 (1DTE): 345 @ 3.50 = **+$121k** SELL | vol 125,166 / OI 2,999
- **MSTR** CALL 110 2026-11-13 (1DTE): 240 @ 4.95 = **+$119k** SELL | vol 464 / OI 281
- **NVDA** CALL 157.5 2026-11-13 (1DTE): 135 @ 8.00 = **+$108k** SELL | vol 29,989 / OI 250
- **NVDA** CALL 157.5 2026-11-13 (1DTE): 132 @ 8.00 = **+$106k** SELL | vol 29,989 / OI 250
- **NVDA** CALL 157.5 2026-11-13 (1DTE): 134 @ 7.85 = **+$105k** SELL | vol 29,989 / OI 250

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 723 2026-11-12 (0DTE): 1,097 traded vs OI 491
- **SPY** CALL 757 2026-11-17 (5DTE): 687 traded vs OI 377
- **SPY** CALL 769 2026-11-13 (1DTE): 4,358 traded vs OI 3,716
- **SPY** PUT 704 2026-11-16 (4DTE): 500 traded vs OI 356
- **SPY** CALL 755 2026-11-16 (4DTE): 1,463 traded vs OI 1,459
- **SPY** PUT 713 2026-11-16 (4DTE): 680 traded vs OI 185
- **SPY** PUT 695 2026-11-17 (5DTE): 556 traded vs OI 332
- **SPY** PUT 752 2026-11-13 (1DTE): 3,926 traded vs OI 3,711
- **SPY** PUT 756 2026-11-18 (6DTE): 834 traded vs OI 232
- **SPY** PUT 720 2026-11-19 (7DTE): 990 traded vs OI 671
- **SPY** PUT 757 2026-11-19 (7DTE): 512 traded vs OI 21
- **SPY** PUT 717 2026-11-19 (7DTE): 1,122 traded vs OI 89
- **SPY** CALL 760 2026-11-19 (7DTE): 652 traded vs OI 605
- **SPY** PUT 715 2026-11-25 (13DTE): 1,337 traded vs OI 0
- **SPY** PUT 714 2026-11-25 (13DTE): 838 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
