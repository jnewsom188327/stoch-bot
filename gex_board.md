# GEX + FLOW SCAN - Wed Nov 11, 11:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (11)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:05 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.64 | 0.46 | +2% (1m) | **-28%** | +363% | 527.5 |
| 10:45 | **AVGO** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/11 345P | 0.78 | 0.35 | +6% (1m) | **-55%** | +149% | 345 |
| 10:35 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.76 | 0.46 | +96% (9m) | **-39%** | +343% | 527.5 |
| 10:20 | **AVGO** | **CALLS** | TREND + FLOW | 11/11 355C | 0.71 | 0.63 | +127% (38m) | **-11%** | +280% | 356.78 |
| 10:15 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.65 | 0.93 | +69% (49m) | **+43%** | +66% | 282.84 hit |
| 10:05 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 175C | 0.76 | 1.54 | +142% (51m) | **+103%** (done) | +58% | 175 hit |
| 09:50 | **GOOGL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 292.5C | 0.51 | 0.62 | +39% (28m) | **+22%** (done) | +82% | 291.86 |
| 09:45 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.68 | 0.64 | +85% (6m) | **-6%** (done) | +68% | 282.96 |
| 09:45 | **QQQ** | **CALLS** | FLOW SURGE | 11/11 690C | 0.63 | 1.23 | +103% (59m) | **+95%** (done) | +171% | 689.78 |
| 09:39 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 693C | 0.52 | 0.29 | -10% (0m) | **-44%** (done) | +92% | 690.43 |
| 09:39 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 760C | 0.53 | 0.17 | -2% (0m) | **-68%** (done) | +79% | 758.82 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:10:08 ET, last candle SPY 11:09, QQQ 11:09 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:02 | QQQ | 1m AGREE FLIP | FULL | CALLS | up | logged (agree flip) |
| 09:38 | QQQ | 1m WHIPSAW | R1 R5 | CALLS | TURNING away | **FIRE** QQQ261111C00693000 |
| 09:38 | SPY | 1m WHIPSAW | R1 R5 | CALLS | TURNING away | **FIRE** SPY261111C00760000 |

## Flow surges NOT fired - price disagreed (7 today, last 5)
- 10:15 BABA CALLS: under EMA 20 - flow says one way, price says the other
- 10:00 MSFT CALLS: price -4.55 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AMZN CALLS: price -0.73 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 AAPL PUTS: price +1.32 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSFT CALLS: price -2.01 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 520.18 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 50 | none: 162 calls 0-7DTE > 13 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (72 contracts' greeks worked out here) | POS +$60.7M | 515.04 | 535 | 520 | +$13.1M | +$697k bull / +$0 bear | out (clean 32, ADX 44, RVol 1.4) |
| 2 | **AMD** | 548.67 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 49 | none: 176 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (71 contracts' greeks worked out here) | POS +$146.1M | - | 550 | 500 | -$67.1M | +$1.6M bull / -$4.2M bear | out (clean 33, ADX 47, RVol 1.0) |
| 3 | **ARM** | 201.50 | FLOW SURGE | **PUTS** | 42 | none: 16 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$5.1M | - | 200 | 200 | -$1.4M | +$0 bull / -$298k bear | out (clean 30, ADX 67, RVol 0.8) |
| 4 | **MU** | 812.86 | FLOW SURGE | **PUTS** | 41 | none: 149 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (60 contracts' greeks worked out here) | POS +$155.0M | - | 800 | 800 | -$195.6M | +$1.9M bull / -$8.5M bear | LONG (clean 33, ADX 68, RVol 0.8) |
| 5 | **DELL** | 374.17 | TREND (flow not with it) | **CALLS** | 37 | none: 30 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$181k | 382.04 | 380 | 340 | -$2.9M | - | LONG (clean 36, ADX 68, RVol 0.8) |
| 6 | **AMZN** | 266.29 | TREND (flow not with it) | **PUTS** | 35 | 11/11 265P @ 0.55 (delta 0.31) = est +55% at 265 | POS +$408.5M | - | 270 | 265 | +$3.5M | +$0 bull / -$54k bear | SHORT (clean 33, ADX 28, RVol 0.7) |
| 7 | **NVDA** | 175.12 | TREND (flow not with it) | **CALLS** | 32 | 11/11 177.5C @ 0.41 (delta 0.23) = est +153% at 177.5 | NEG -$155.3M | 181.25 | 180 | 175 | -$20.3M | +$382k bull / -$1.7M bear | LONG (clean 34, ADX 35, RVol 1.4) |
| 8 | **SMH** | 508.71 | - | **-** | 29 | - | NEG -$38.1M | - | 500 | 500 | -$2.9M | +$0 bull / -$152k bear | out (clean 31, ADX 47, RVol 1.5) |
| 9 | **HOOD** | 84.32 | - | **-** | 28 | - | POS +$14.3M | - | 85 | 85 | -$785k | +$0 bull / -$27k bear | out (clean 33, ADX 39, RVol 0.9) |
| 10 | **QQQ** | 690.06 | - | **-** | 25 | - | POS +$104.2M | 689.72 | 700 | 680 | -$109.9M | +$2.1M bull / -$4.8M bear | out (clean 32, ADX 55, RVol 0.5) |
| 11 | **AVGO** | 351.28 | - | **-** | 25 | - | POS +$105.3M | - | 350 | 350 | +$4.9M | +$94k bull / -$306k bear | out (clean 34, ADX 52, RVol 1.2) |
| 12 | **SPY** | 757.73 | - | **-** | 22 | - | NEG -$2.8B | 761.05 | 760 | 750 | -$40.7M | +$224k bull / -$106k bear | out (clean 32, ADX 52, RVol 0.5) |
| 13 | **BABA** | 101.14 | - | **-** | 22 | - | NEG -$17.1M | 106.86 | 110 | 101 | +$413k | - | out (clean 29, ADX 36, RVol 0.4) |
| 14 | **TSLA** | 393.77 | - | **-** | 21 | - | POS +$429.9M | - | 400 | 380 | -$12.4M | +$811k bull / -$2.0M bear | out (clean 33, ADX 56, RVol 0.5) |
| 15 | **SMCI** | 30.59 | - | **-** | 21 | - | POS +$12.1M | - | 30 | 30 | -$469k | - | out (clean 32, ADX 64, RVol 0.9) |
| 16 | **AAPL** | 353.37 | - | **-** | 20 | - | POS +$1.4B | 340.44 | 355 | 350 | -$1.5M | +$40k bull / -$91k bear | out (clean 27, ADX 46, RVol 0.5) |
| 17 | **COIN** | 137.59 | - | **-** | 18 | - | POS +$25.5M | - | 141 | 135 | -$49k | +$0 bull / -$75k bear | out (clean 28, ADX 34, RVol 0.7) |
| 18 | **META** | 640.59 | - | **-** | 16 | - | POS +$265.1M | 626.87 | 650 | 625 | +$433k | +$0 bull / -$248k bear | out (clean 31, ADX 19, RVol 0.9) |
| 19 | **PLTR** | 172.81 | - | **-** | 15 | - | POS +$78.6M | - | 170 | 170 | +$1.2M | - | out (clean 30, ADX 44, RVol 0.4) |
| 20 | **UBER** | 69.36 | - | **-** | 13 | - | POS +$8.7M | 68.31 | 70 | 70 | +$62k | - | out (clean 31, ADX 22, RVol 0.6) |
| 21 | **IWM** | 282.62 | - | **-** | 12 | - | NEG -$34.6M | 282.88 | 285 | 270 | -$2.3M | - | out (clean 34, ADX 43, RVol 0.3) |
| 22 | **SHOP** | 149.56 | - | **-** | 12 | - | POS +$3.8M | 144.59 | 150 | 140 | -$7k | - | out (clean 33, ADX 36, RVol 0.4) |
| 23 | **GOOGL** | 291.48 | - | **-** | 11 | - | POS +$50.3M | 289 | 300 | 290 | +$329k | - | out (clean 28, ADX 54, RVol 1.2) |
| 24 | **ORCL** | 127.87 | - | **-** | 10 | - | POS +$3.2M | 124.54 | 130 | 125 | +$82k | - | out (clean 29, ADX 52, RVol 1.1) |
| 25 | **CRM** | 217.07 | - | **-** | 7 | - | NEG -$11.5M | - | 230 | 220 | -$6k | - | out (clean 30, ADX 30, RVol 0.4) |
| 26 | **MSTR** | 123.15 | - | **-** | 6 | - | POS +$2.0M | 122.28 | 133 | 120 | +$112k | - | out (clean 28, ADX 23, RVol 0.6) |
| 27 | **NFLX** | 63.54 | - | **-** | 5 | - | NEG -$13.6M | 64.52 | 65 | 65 | +$10k | - | out (clean 26, ADX 16, RVol 0.9) |

## Big prints this scan (206)
- **AMD** CALL 527.5 2026-11-11 (0DTE): 610 @ 22.13 = **+$1.3M** MID | vol 3,026 / OI 648
- **QQQ** CALL 674 2026-11-12 (1DTE): 299 @ 17.33 = **+$518k** BUY | vol 356 / OI 258
- **QQQ** CALL 675 2026-11-12 (1DTE): 299 @ 16.42 = **+$491k** BUY | vol 619 / OI 505
- **AMD** CALL 527.5 2026-11-11 (0DTE): 190 @ 22.09 = **+$420k** MID | vol 3,026 / OI 648
- **MU** CALL 780 2026-11-13 (2DTE): 84 @ 43.81 = **+$368k** SELL | vol 3,098 / OI 1,313
- **QQQ** CALL 707 2026-11-17 (6DTE): 2,000 @ 1.78 = **+$356k** SELL | vol 12,094 / OI 745
- **QQQ** PUT 702 2026-11-12 (1DTE): 275 @ 12.28 = **+$338k** BUY | vol 280 / OI 6
- **MU** PUT 815 2026-11-13 (2DTE): 100 @ 20.60 = **+$206k** SELL | vol 331 / OI 225
- **QQQ** CALL 685 2026-11-18 (7DTE): 156 @ 13.01 = **+$203k** BUY | vol 436 / OI 218
- **QQQ** CALL 691 2026-11-12 (1DTE): 495 @ 4.02 = **+$199k** BUY | vol 4,904 / OI 310
- **QQQ** CALL 690 2026-11-13 (2DTE): 300 @ 6.18 = **+$185k** BUY | vol 13,744 / OI 8,488
- **TSLA** PUT 397.5 2026-11-11 (0DTE): 500 @ 3.50 = **+$175k** SELL | vol 2,756 / OI 490
- **QQQ** PUT 696 2026-11-11 (0DTE): 275 @ 6.18 = **+$170k** BUY | vol 574 / OI 307
- **AMD** CALL 550 2026-11-11 (0DTE): 300 @ 5.18 = **+$155k** BUY | vol 32,911 / OI 918
- **AMD** CALL 547.5 2026-11-13 (2DTE): 100 @ 15.46 = **+$155k** BUY | vol 769 / OI 390

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 751 2026-11-12 (1DTE): 710 traded vs OI 691
- **SPY** CALL 758 2026-11-17 (6DTE): 505 traded vs OI 124
- **SPY** PUT 709 2026-11-12 (1DTE): 546 traded vs OI 255
- **SPY** CALL 772 2026-11-12 (1DTE): 879 traded vs OI 785
- **SPY** PUT 758 2026-11-13 (2DTE): 3,964 traded vs OI 1,889
- **SPY** CALL 759 2026-11-13 (2DTE): 3,219 traded vs OI 2,941
- **SPY** PUT 735 2026-11-11 (0DTE): 3,604 traded vs OI 3,522
- **SPY** CALL 746 2026-11-11 (0DTE): 592 traded vs OI 591
- **SPY** PUT 749 2026-11-17 (6DTE): 1,034 traded vs OI 275
- **SPY** PUT 758 2026-11-18 (7DTE): 502 traded vs OI 44
- **QQQ** PUT 663 2026-11-12 (1DTE): 503 traded vs OI 431
- **QQQ** PUT 693 2026-11-12 (1DTE): 534 traded vs OI 38
- **QQQ** PUT 695 2026-11-12 (1DTE): 659 traded vs OI 244
- **QQQ** CALL 684 2026-11-13 (2DTE): 712 traded vs OI 625
- **QQQ** CALL 707 2026-11-12 (1DTE): 511 traded vs OI 145

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
