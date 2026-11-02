# GEX + FLOW SCAN - Mon Nov 02, 01:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 1.66 | +291% (43m) | **+155%** | +11% | 692.76 hit |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 1.27 | +111% (58m) | **+79%** (done) | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:00:08 ET, last candle SPY 12:59, QQQ 12:59 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 12:02 | QQQ | 1m FAILED POP | R3 | PUTS | TURNING away | **FIRE** QQQ261102P00691000 |
| 11:54 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 90 puts 0-1DTE > 5 priced 0.40-0.80 > 3 delta 0.15+ > 3 spread ok > 3 liquid  |
| 11:36 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** QQQ261102P00691000 |
| 11:36 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 90 puts 0-1DTE > 5 priced 0.40-0.80 > 3 delta 0.15+ > 3 spread ok > 3 liquid  |

## Flow surges NOT fired - price disagreed (5 today, last 5)
- 10:35 SPY PUTS: price +0.32 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:25 SPY PUTS: price +2.69 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:10 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 10:05 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 09:50 BABA PUTS: price +0.75 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MU** | 852.84 | FLOW SURGE | **CALLS** | 43 | none: 139 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (56 contracts' greeks worked out here) | NEG -$231.4M | - | 910 | 850 | +$129.9M | +$1.6M bull / -$487k bear | out (clean 31, ADX 39, RVol 1.1) |
| 2 | **BABA** | 102.92 | TREND + FLOW | **PUTS** | 43 | none: 21 puts 0-7DTE > 3 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +10% at the target (needs +20%) | POS +$2.4M | 100.97 | 105 | 100 | -$983k | - | SHORT (clean 33, ADX 28, RVol 1.7) |
| 3 | **AMZN** | 250.49 | PINNED between the walls (positive gamma) - chop | **-** | 34 | - | POS +$92.4M | 242.63 | 250 | 250 | -$22.5M | +$43k bull / -$802k bear | out (clean 33, ADX 27, RVol 0.5) |
| 4 | **SMCI** | 31.66 | TREND (flow not with it) | **PUTS** | 33 | none: 13 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$420k | - | 34 | 30 | +$440k | - | SHORT (clean 33, ADX 39, RVol 1.2) |
| 5 | **AMD** | 482.58 | - | **-** | 28 | - | NEG -$82.4M | - | 500 | 480 | +$37.8M | +$3.7M bull / +$0 bear | out (clean 31, ADX 38, RVol 1.5) |
| 6 | **SMH** | 520.01 | - | **-** | 25 | - | NEG -$354.2M | - | 532.5 | 500 | +$3.7M | +$189k bull / +$0 bear | out (clean 31, ADX 23, RVol 1.3) |
| 7 | **AAPL** | 338.11 | - | **-** | 23 | - | POS +$9.6M | 337.06 | 350 | 330 | +$14.3M | +$0 bull / -$1.9M bear | out (clean 31, ADX 31, RVol 1.1) |
| 8 | **MSTR** | 134.09 | - | **-** | 20 | - | POS +$3.0M | - | 135 | 125 | +$3.6M | +$0 bull / -$96k bear | out (clean 26, ADX 21, RVol 0.6) |
| 9 | **META** | 610.30 | - | **-** | 19 | - | NEG -$147.3M | 626.26 | 650 | 610 | +$11.9M | +$1.8M bull / -$436k bear | out (clean 29, ADX 25, RVol 0.6) |
| 10 | **AVGO** | 329.27 | - | **-** | 19 | - | NEG -$106.2M | - | 340 | 330 | -$4.8M | +$120k bull / +$0 bear | out (clean 30, ADX 23, RVol 0.4) |
| 11 | **SHOP** | 160.08 | - | **-** | 19 | - | NEG -$375k | - | 175 | 175 | -$753k | - | out (clean 28, ADX 24, RVol 0.8) |
| 12 | **SPY** | 758.27 | - | **-** | 18 | - | NEG -$10.2B | 775.53 | 800 | 750 | +$35.5M | +$1.7M bull / -$102k bear | out (clean 30, ADX 25, RVol 1.0) |
| 13 | **QQQ** | 691.99 | - | **-** | 18 | - | NEG -$5.6B | - | 720 | 680 | +$63.9M | +$8.5M bull / -$334k bear | out (clean 30, ADX 24, RVol 0.6) |
| 14 | **IWM** | 281.20 | - | **-** | 18 | - | NEG -$1.0B | 286.59 | 285 | 270 | +$745k | +$684k bull / +$0 bear | out (clean 31, ADX 25, RVol 1.5) |
| 15 | **TSLA** | 408.73 | - | **-** | 18 | - | POS +$298.9M | - | 410 | 400 | -$64.1M | +$831k bull / -$351k bear | out (clean 30, ADX 24, RVol 0.5) |
| 16 | **NFLX** | 62.62 | - | **-** | 18 | - | NEG -$21.2M | - | 63 | 60 | -$290k | +$0 bull / -$26k bear | out (clean 28, ADX 26, RVol 0.6) |
| 17 | **ORCL** | 122.25 | - | **-** | 18 | - | NEG -$37.9M | - | 130 | 120 | -$396k | +$84k bull / +$0 bear | out (clean 31, ADX 33, RVol 0.6) |
| 18 | **NVDA** | 206.53 | - | **-** | 17 | - | NEG -$212.2M | 215.17 | 210 | 200 | +$8.6M | +$239k bull / +$0 bear | out (clean 29, ADX 17, RVol 0.8) |
| 19 | **MSFT** | 519.85 | - | **-** | 17 | - | POS +$218.6M | 502.05 | 540 | 500 | -$1.2M | +$114k bull / -$327k bear | out (clean 27, ADX 29, RVol 0.4) |
| 20 | **DELL** | 408.56 | - | **-** | 17 | - | NEG -$21.6M | - | 440 | 400 | +$434k | +$521k bull / +$0 bear | out (clean 33, ADX 23, RVol 0.8) |
| 21 | **GOOGL** | 282.92 | - | **-** | 16 | - | NEG -$93.0M | - | 285 | 290 | +$2.2M | +$0 bull / -$142k bear | out (clean 34, ADX 16, RVol 0.4) |
| 22 | **PLTR** | 184.70 | - | **-** | 16 | - | NEG -$11.1M | - | 200 | 180 | +$2.6M | +$89k bull / +$0 bear | out (clean 25, ADX 12, RVol 0.5) |
| 23 | **UBER** | 67.22 | - | **-** | 14 | - | NEG -$8.4M | - | 70 | 65 | -$469k | - | out (clean 28, ADX 28, RVol 0.6) |
| 24 | **ARM** | 203.29 | - | **-** | 12 | - | NEG -$7.0M | - | 220 | 200 | +$300k | - | out (clean 25, ADX 19, RVol 0.8) |
| 25 | **COIN** | 140.26 | - | **-** | 8 | - | NEG -$7.8M | - | 150 | 130 | -$355k | - | out (clean 23, ADX 13, RVol 1.1) |
| 26 | **CRM** | 232.67 | - | **-** | 7 | - | NEG -$5.1M | 242.29 | 240 | 220 | +$68k | - | out (clean 27, ADX 11, RVol 0.3) |
| 27 | **HOOD** | 85.39 | - | **-** | 6 | - | NEG -$10.3M | - | 93 | 90 | -$130k | - | out (clean 32, ADX 26, RVol 0.5) |

## Big prints this scan (89)
- **META** PUT 595 2026-11-06 (4DTE): 1,900 @ 6.00 = **+$1.1M** SELL | vol 2,483 / OI 2,342
- **SPY** PUT 765 2026-11-05 (3DTE): 500 @ 9.00 = **+$450k** SELL | vol 6,483 / OI 2,269
- **SPY** PUT 765 2026-11-05 (3DTE): 500 @ 8.95 = **+$448k** SELL | vol 6,483 / OI 2,269
- **AMD** PUT 500 2026-11-04 (2DTE): 136 @ 31.00 = **+$422k** SELL | vol 1,601 / OI 212
- **QQQ** PUT 675 2026-11-09 (7DTE): 750 @ 5.30 = **+$398k** SELL | vol 1,570 / OI 427
- **AMZN** CALL 240 2026-11-04 (2DTE): 233 @ 10.45 = **+$243k** SELL | vol 2,257 / OI 154
- **QQQ** PUT 696 2026-11-02 (0DTE): 399 @ 5.25 = **+$209k** SELL | vol 77,236 / OI 0
- **QQQ** PUT 700 2026-11-03 (1DTE): 199 @ 10.26 = **+$204k** BUY | vol 5,517 / OI 1,423
- **AMD** PUT 500 2026-11-04 (2DTE): 64 @ 31.00 = **+$198k** SELL | vol 1,601 / OI 212
- **AAPL** CALL 350 2026-11-06 (4DTE): 700 @ 2.78 = **+$195k** SELL | vol 24,348 / OI 6,983
- **MU** PUT 875 2026-11-02 (0DTE): 80 @ 24.10 = **+$193k** BUY | vol 14,578 / OI 366
- **SPY** PUT 758 2026-11-02 (0DTE): 1,424 @ 1.35 = **+$192k** SELL | vol 235,785 / OI 1,174
- **AMD** PUT 495 2026-11-09 (7DTE): 62 @ 30.67 = **+$190k** SELL | vol 231 / OI 2
- **AMD** CALL 495 2026-11-04 (2DTE): 102 @ 16.70 = **+$170k** BUY | vol 554 / OI 0
- **AMZN** CALL 240 2026-11-04 (2DTE): 162 @ 10.50 = **+$170k** SELL | vol 2,257 / OI 154

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 749 2026-11-04 (2DTE): 740 traded vs OI 722
- **SPY** PUT 715 2026-11-03 (1DTE): 1,236 traded vs OI 1,202
- **SPY** PUT 733 2026-11-04 (2DTE): 507 traded vs OI 120
- **SPY** PUT 743 2026-11-04 (2DTE): 512 traded vs OI 225
- **SPY** PUT 759 2026-11-13 (11DTE): 764 traded vs OI 711
- **SPY** CALL 762 2026-11-30 (28DTE): 900 traded vs OI 602
- **SPY** PUT 764 2026-11-30 (28DTE): 643 traded vs OI 577
- **QQQ** PUT 645 2026-11-09 (7DTE): 503 traded vs OI 109
- **QQQ** CALL 685 2026-11-06 (4DTE): 544 traded vs OI 166
- **QQQ** PUT 685 2026-11-05 (3DTE): 1,931 traded vs OI 1,896
- **QQQ** CALL 690 2026-11-05 (3DTE): 769 traded vs OI 18
- **QQQ** PUT 695 2026-11-10 (8DTE): 500 traded vs OI 388
- **QQQ** CALL 708 2026-11-20 (18DTE): 1,351 traded vs OI 787
- **IWM** CALL 278 2026-11-02 (0DTE): 800 traded vs OI 796
- **IWM** CALL 283 2026-11-13 (11DTE): 2,341 traded vs OI 2,281

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
