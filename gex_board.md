# GEX + FLOW SCAN - Mon Nov 02, 02:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 1.48 | +291% (43m) | **+128%** (done) | +11% | 692.76 hit |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 1.27 | +111% (58m) | **+79%** (done) | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (7 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:50:08 ET, last candle SPY 14:49, QQQ 14:49 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 14:28 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | TURNING your way | no contract: 75 calls 0-1DTE > 6 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid |
| 14:26 | QQQ | 1m WHIPSAW | R1 R2 | PUTS | WITH you | no contract: 75 puts 0-1DTE > 4 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 14:16 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | no contract: 92 puts 0-1DTE > 6 priced 0.40-0.80 > 3 delta 0.15+ > 3 spread ok > 3 liquid  |
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
| 1 | **SMH** | 508.94 | FLOW SURGE | **CALLS** | 42 | none: 158 calls 0-7DTE > 5 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 0 liquid (65 contracts' greeks worked out here) | NEG -$322.1M | - | 532.5 | 500 | +$9.3M | +$981k bull / +$0 bear | out (clean 33, ADX 53, RVol 0.7) |
| 2 | **MU** | 832.10 | FLOW SURGE | **CALLS** | 42 | none: 131 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (57 contracts' greeks worked out here) | NEG -$202.9M | - | 910 | 850 | +$177.3M | +$5.2M bull / +$0 bear | out (clean 32, ADX 53, RVol 0.9) |
| 3 | **SMCI** | 30.54 | TREND (flow not with it) | **PUTS** | 38 | none: 13 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$535k | - | 33 | 30 | +$964k | - | SHORT (clean 36, ADX 56, RVol 1.2) |
| 4 | **BABA** | 102.12 | TREND + FLOW | **PUTS** | 35 | none: 21 puts 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +5% at the target (needs +20%) | POS +$978k | 101.37 | 105 | 100 | -$944k | - | SHORT (clean 33, ADX 35, RVol 0.8) |
| 5 | **DELL** | 398.16 | TREND (flow not with it) | **PUTS** | 30 | none: 31 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$19.3M | - | 430 | 400 | +$2.5M | +$30k bull / +$0 bear | SHORT (clean 34, ADX 46, RVol 0.9) |
| 6 | **AMD** | 470.91 | - | **-** | 28 | - | NEG -$63.7M | - | 500 | 500 | +$55.4M | +$1.2M bull / -$587k bear | out (clean 33, ADX 62, RVol 1.1) |
| 7 | **QQQ** | 682.89 | - | **-** | 25 | - | NEG -$5.2B | - | 720 | 680 | +$214.7M | +$7.4M bull / +$0 bear | out (clean 32, ADX 52, RVol 1.1) |
| 8 | **SPY** | 753.36 | - | **-** | 24 | - | NEG -$10.4B | 775.42 | 770 | 750 | +$181.2M | +$5.1M bull / +$0 bear | out (clean 31, ADX 49, RVol 1.2) |
| 9 | **AAPL** | 337.30 | - | **-** | 24 | - | POS +$2.3M | 337.09 | 350 | 330 | +$23.3M | +$0 bull / -$1.0M bear | out (clean 31, ADX 30, RVol 1.5) |
| 10 | **NVDA** | 203.22 | - | **-** | 23 | - | NEG -$234.9M | - | 210 | 200 | +$22.7M | +$1.3M bull / -$60k bear | out (clean 30, ADX 42, RVol 1.1) |
| 11 | **AMZN** | 247.45 | - | **-** | 23 | - | POS +$48.2M | 242.86 | 250 | 250 | -$16.7M | +$651k bull / +$0 bear | out (clean 34, ADX 43, RVol 0.6) |
| 12 | **PLTR** | 180.34 | - | **-** | 23 | - | NEG -$13.7M | - | 190 | 180 | +$4.9M | +$1.0M bull / +$0 bear | out (clean 26, ADX 36, RVol 1.2) |
| 13 | **SHOP** | 156.62 | - | **-** | 22 | - | NEG -$413k | - | 170 | 160 | -$401k | +$71k bull / +$0 bear | out (clean 30, ADX 26, RVol 1.2) |
| 14 | **IWM** | 279.39 | - | **-** | 21 | - | NEG -$1.3B | 287.06 | 285 | 270 | +$5.4M | +$54k bull / +$0 bear | out (clean 33, ADX 42, RVol 0.7) |
| 15 | **MSFT** | 513.29 | - | **-** | 21 | - | POS +$111.0M | 502.33 | 535 | 510 | +$3.0M | +$266k bull / +$0 bear | out (clean 28, ADX 50, RVol 0.8) |
| 16 | **ORCL** | 118.73 | - | **-** | 21 | - | NEG -$34.2M | - | 130 | 120 | +$1.0M | +$35k bull / +$0 bear | out (clean 33, ADX 45, RVol 0.8) |
| 17 | **HOOD** | 83.45 | - | **-** | 21 | - | NEG -$11.1M | - | 85 | 90 | +$826k | +$55k bull / +$0 bear | out (clean 33, ADX 43, RVol 0.8) |
| 18 | **TSLA** | 402.42 | - | **-** | 20 | - | POS +$199.6M | - | 400 | 400 | -$35.9M | +$6.7M bull / +$0 bear | out (clean 32, ADX 37, RVol 0.9) |
| 19 | **META** | 609.56 | - | **-** | 17 | - | NEG -$145.2M | 625.61 | 650 | 610 | +$11.0M | +$101k bull / -$114k bear | out (clean 28, ADX 16, RVol 0.7) |
| 20 | **GOOGL** | 281.39 | - | **-** | 17 | - | NEG -$87.9M | - | 280 | 280 | -$1.8M | +$244k bull / +$0 bear | out (clean 33, ADX 22, RVol 0.8) |
| 21 | **ARM** | 198.74 | - | **-** | 16 | - | NEG -$5.6M | - | 200 | 200 | +$310k | - | out (clean 26, ADX 41, RVol 1.0) |
| 22 | **UBER** | 66.49 | - | **-** | 15 | - | NEG -$13.6M | - | 70 | 65 | -$390k | - | out (clean 28, ADX 42, RVol 1.0) |
| 23 | **CRM** | 227.62 | - | **-** | 13 | - | NEG -$6.9M | - | 240 | 220 | +$112k | - | out (clean 28, ADX 36, RVol 0.8) |
| 24 | **MSTR** | 129.91 | - | **-** | 12 | - | POS +$1.4M | - | 135 | 125 | +$4.6M | - | out (clean 26, ADX 27, RVol 0.8) |
| 25 | **NFLX** | 62.54 | - | **-** | 10 | - | NEG -$20.9M | - | 63 | 60 | -$655k | - | out (clean 29, ADX 26, RVol 0.9) |
| 26 | **AVGO** | 323.19 | - | **-** | 9 | - | NEG -$115.4M | - | 340 | 320 | -$1.8M | - | out (clean 32, ADX 40, RVol 0.6) |
| 27 | **COIN** | 135.69 | - | **-** | 8 | - | NEG -$6.2M | - | 140 | 130 | -$11k | - | out (clean 25, ADX 38, RVol 0.7) |

## Big prints this scan (119)
- **QQQ** CALL 675 2026-11-02 (0DTE): 500 @ 10.35 = **+$518k** BUY | vol 591 / OI 11
- **TSLA** CALL 397.5 2026-11-04 (2DTE): 290 @ 12.34 = **+$358k** BUY | vol 2,352 / OI 190
- **TSLA** CALL 402.5 2026-11-04 (2DTE): 380 @ 9.11 = **+$346k** BUY | vol 2,459 / OI 427
- **TSLA** CALL 400 2026-11-04 (2DTE): 315 @ 10.70 = **+$337k** BUY | vol 6,608 / OI 612
- **TSLA** CALL 405 2026-11-04 (2DTE): 380 @ 7.75 = **+$294k** BUY | vol 8,507 / OI 594
- **TSLA** CALL 400 2026-11-02 (0DTE): 500 @ 5.20 = **+$260k** BUY | vol 36,038 / OI 1,359
- **QQQ** PUT 688 2026-11-02 (0DTE): 500 @ 3.14 = **+$157k** SELL | vol 133,198 / OI 0
- **QQQ** CALL 687 2026-11-04 (2DTE): 200 @ 7.75 = **+$155k** BUY | vol 549 / OI 0
- **SPY** PUT 754 2026-11-03 (1DTE): 469 @ 3.10 = **+$145k** SELL | vol 17,715 / OI 2,581
- **SPY** PUT 755 2026-11-03 (1DTE): 411 @ 3.48 = **+$143k** SELL | vol 32,133 / OI 3,155
- **QQQ** PUT 700 2026-11-03 (1DTE): 100 @ 14.06 = **+$141k** SELL | vol 8,239 / OI 1,423
- **QQQ** PUT 695 2026-11-02 (0DTE): 139 @ 9.81 = **+$136k** SELL | vol 153,182 / OI 8,691
- **SPY** PUT 756 2026-11-02 (0DTE): 590 @ 2.29 = **+$135k** SELL | vol 289,169 / OI 1,385
- **MU** CALL 860 2026-11-04 (2DTE): 98 @ 13.00 = **+$127k** BUY | vol 2,068 / OI 37
- **SMH** PUT 515 2026-11-06 (4DTE): 88 @ 14.45 = **+$127k** SELL | vol 861 / OI 1,152

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 754 2026-11-04 (2DTE): 519 traded vs OI 3
- **SPY** CALL 755 2026-11-09 (7DTE): 557 traded vs OI 44
- **SPY** PUT 737 2026-11-04 (2DTE): 2,914 traded vs OI 185
- **SPY** CALL 748 2026-11-02 (0DTE): 583 traded vs OI 12
- **SPY** PUT 756 2026-11-27 (25DTE): 542 traded vs OI 335
- **SPY** CALL 768 2026-11-27 (25DTE): 822 traded vs OI 721
- **SPY** PUT 757 2026-11-27 (25DTE): 545 traded vs OI 275
- **QQQ** PUT 615 2026-11-06 (4DTE): 548 traded vs OI 0
- **QQQ** CALL 689 2026-11-04 (2DTE): 554 traded vs OI 0
- **QQQ** CALL 675 2026-11-02 (0DTE): 591 traded vs OI 11
- **TSLA** PUT 362.5 2026-11-06 (4DTE): 660 traded vs OI 0
- **AAPL** PUT 335 2026-11-09 (7DTE): 607 traded vs OI 126
- **AAPL** CALL 355 2026-11-09 (7DTE): 505 traded vs OI 126
- **AAPL** PUT 335 2026-11-06 (4DTE): 7,345 traded vs OI 7,284
- **AMD** CALL 472.5 2026-11-02 (0DTE): 537 traded vs OI 12

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
