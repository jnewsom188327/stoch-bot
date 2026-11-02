# GEX + FLOW SCAN - Mon Nov 02, 01:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 1.48 | +291% (43m) | **+128%** (done) | +11% | 692.76 hit |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 1.27 | +111% (58m) | **+79%** (done) | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:40:08 ET, last candle SPY 13:39, QQQ 13:39 | no errors
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
| 1 | **MU** | 849.32 | FLOW SURGE | **CALLS** | 41 | none: 138 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (62 contracts' greeks worked out here) | NEG -$225.1M | - | 910 | 850 | +$141.4M | +$7.6M bull / -$64k bear | out (clean 31, ADX 38, RVol 0.9) |
| 2 | **SMCI** | 31.38 | TREND (flow not with it) | **PUTS** | 34 | none: 13 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$443k | - | 34 | 30 | +$681k | - | SHORT (clean 34, ADX 43, RVol 1.0) |
| 3 | **AMZN** | 249.84 | PINNED between the walls (positive gamma) - chop | **-** | 32 | - | POS +$77.4M | 243.77 | 250 | 250 | -$20.5M | +$138k bull / +$0 bear | out (clean 33, ADX 24, RVol 0.4) |
| 4 | **AMD** | 480.65 | - | **-** | 26 | - | NEG -$77.3M | - | 500 | 480 | +$39.0M | +$7.0M bull / +$0 bear | out (clean 32, ADX 44, RVol 0.7) |
| 5 | **AAPL** | 336.61 | - | **-** | 25 | - | NEG -$9.9M | 336.88 | 350 | 330 | +$24.0M | +$1.9M bull / +$0 bear | out (clean 31, ADX 35, RVol 1.0) |
| 6 | **DELL** | 406.24 | TREND (flow not with it) | **PUTS** | 23 | none: 32 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$21.3M | - | 440 | 400 | +$754k | +$30k bull / +$0 bear | SHORT (clean 33, ADX 29, RVol 0.8) |
| 7 | **MSFT** | 519.42 | - | **-** | 18 | - | POS +$206.2M | 502.45 | 540 | 500 | -$1.2M | +$0 bull / -$140k bear | out (clean 27, ADX 33, RVol 0.8) |
| 8 | **QQQ** | 690.57 | - | **-** | 17 | - | NEG -$5.7B | - | 720 | 680 | +$56.8M | +$1.0M bull / +$0 bear | out (clean 30, ADX 25, RVol 0.3) |
| 9 | **TSLA** | 407.87 | - | **-** | 17 | - | POS +$297.0M | - | 410 | 400 | -$68.8M | +$728k bull / +$0 bear | out (clean 30, ADX 18, RVol 0.4) |
| 10 | **META** | 613.78 | - | **-** | 17 | - | NEG -$125.8M | 626.74 | 650 | 610 | +$9.0M | +$0 bull / -$225k bear | out (clean 29, ADX 20, RVol 0.3) |
| 11 | **GOOGL** | 284.61 | - | **-** | 17 | - | NEG -$85.4M | - | 285 | 285 | -$4.4M | +$0 bull / -$2.7M bear | out (clean 34, ADX 18, RVol 0.2) |
| 12 | **PLTR** | 184.05 | - | **-** | 17 | - | NEG -$11.3M | - | 200 | 180 | +$2.5M | +$0 bull / -$101k bear | out (clean 25, ADX 14, RVol 0.7) |
| 13 | **SPY** | 758.38 | - | **-** | 16 | - | NEG -$10.1B | 775.33 | 800 | 750 | +$35.6M | +$1.5M bull / +$0 bear | out (clean 30, ADX 23, RVol 0.6) |
| 14 | **NVDA** | 206.34 | - | **-** | 16 | - | NEG -$216.7M | 215.49 | 210 | 200 | +$7.8M | +$812k bull / +$0 bear | out (clean 28, ADX 15, RVol 1.1) |
| 15 | **HOOD** | 85.17 | - | **-** | 16 | - | NEG -$10.5M | - | 93 | 90 | -$184k | +$32k bull / +$0 bear | out (clean 32, ADX 27, RVol 0.4) |
| 16 | **SHOP** | 159.73 | - | **-** | 16 | - | NEG -$581k | - | 175 | 175 | -$701k | - | out (clean 28, ADX 21, RVol 0.7) |
| 17 | **BABA** | 102.83 | - | **-** | 14 | - | POS +$1.9M | 101.28 | 105 | 100 | -$1.0M | - | out (clean 33, ADX 20, RVol 0.7) |
| 18 | **SMH** | 518.88 | - | **-** | 13 | - | NEG -$358.1M | - | 532.5 | 500 | +$3.8M | - | out (clean 31, ADX 25, RVol 0.4) |
| 19 | **UBER** | 67.14 | - | **-** | 12 | - | NEG -$8.6M | - | 70 | 65 | -$481k | - | out (clean 28, ADX 22, RVol 0.5) |
| 20 | **ARM** | 203.00 | - | **-** | 10 | - | NEG -$6.9M | - | 220 | 200 | +$261k | - | out (clean 25, ADX 20, RVol 0.4) |
| 21 | **NFLX** | 62.60 | - | **-** | 8 | - | NEG -$19.9M | - | 63 | 60 | -$339k | - | out (clean 28, ADX 27, RVol 0.5) |
| 22 | **MSTR** | 133.35 | - | **-** | 8 | - | POS +$2.0M | - | 135 | 125 | +$3.7M | - | out (clean 25, ADX 15, RVol 0.5) |
| 23 | **AVGO** | 329.19 | - | **-** | 7 | - | NEG -$104.8M | - | 340 | 330 | -$4.7M | - | out (clean 31, ADX 17, RVol 0.3) |
| 24 | **COIN** | 139.09 | - | **-** | 7 | - | NEG -$7.9M | - | 150 | 130 | -$319k | - | out (clean 23, ADX 12, RVol 0.6) |
| 25 | **ORCL** | 121.73 | - | **-** | 7 | - | NEG -$37.1M | - | 130 | 120 | -$310k | - | out (clean 32, ADX 33, RVol 0.5) |
| 26 | **IWM** | 280.88 | - | **-** | 6 | - | NEG -$1.1B | 286.77 | 285 | 270 | +$974k | - | out (clean 32, ADX 23, RVol 0.6) |
| 27 | **CRM** | 231.59 | - | **-** | 6 | - | NEG -$5.7M | 242.23 | 240 | 220 | +$47k | - | out (clean 26, ADX 10, RVol 0.8) |

## Big prints this scan (61)
- **QQQ** PUT 691 2026-11-06 (4DTE): 1,000 @ 9.34 = **+$934k** SELL | vol 5,732 / OI 15,392
- **AMD** CALL 502.5 2026-11-06 (4DTE): 460 @ 16.05 = **+$738k** BUY | vol 1,794 / OI 11
- **AMD** CALL 502.5 2026-11-06 (4DTE): 459 @ 16.05 = **+$737k** BUY | vol 1,794 / OI 11
- **AMD** CALL 502.5 2026-11-06 (4DTE): 300 @ 16.06 = **+$482k** BUY | vol 1,794 / OI 11
- **AMD** CALL 502.5 2026-11-06 (4DTE): 300 @ 16.06 = **+$482k** BUY | vol 1,794 / OI 11
- **AMD** PUT 460 2026-11-06 (4DTE): 189 @ 14.18 = **+$268k** SELL | vol 3,825 / OI 2,857
- **GOOGL** CALL 285 2026-11-06 (4DTE): 600 @ 4.05 = **+$243k** SELL | vol 11,460 / OI 2,236
- **GOOGL** CALL 287.5 2026-11-06 (4DTE): 600 @ 2.99 = **+$179k** SELL | vol 6,916 / OI 375
- **GOOGL** CALL 287.5 2026-11-06 (4DTE): 550 @ 2.95 = **+$162k** SELL | vol 6,916 / OI 375
- **GOOGL** CALL 285 2026-11-06 (4DTE): 331 @ 4.05 = **+$134k** SELL | vol 11,460 / OI 2,236
- **SPY** PUT 758 2026-11-03 (1DTE): 400 @ 2.85 = **+$114k** SELL | vol 28,364 / OI 494
- **MU** PUT 840 2026-11-06 (4DTE): 50 @ 21.50 = **+$108k** SELL | vol 1,014 / OI 868
- **QQQ** PUT 680 2026-11-09 (7DTE): 157 @ 6.63 = **+$104k** SELL | vol 2,785 / OI 213
- **GOOGL** CALL 285 2026-11-06 (4DTE): 237 @ 4.09 = **+$97k** SELL | vol 11,460 / OI 2,236
- **MU** PUT 830 2026-11-06 (4DTE): 50 @ 17.70 = **+$88k** SELL | vol 798 / OI 521

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 809 2026-11-06 (4DTE): 1,775 traded vs OI 1,023
- **SPY** CALL 808 2026-11-06 (4DTE): 1,566 traded vs OI 1,117
- **SPY** PUT 735 2026-11-16 (14DTE): 1,224 traded vs OI 0
- **SPY** PUT 740 2026-11-16 (14DTE): 1,201 traded vs OI 0
- **QQQ** CALL 710 2026-11-10 (8DTE): 509 traded vs OI 407
- **AAPL** CALL 340 2026-11-09 (7DTE): 597 traded vs OI 57
- **AAPL** CALL 337.5 2026-11-06 (4DTE): 501 traded vs OI 397
- **AMD** CALL 502.5 2026-11-06 (4DTE): 1,794 traded vs OI 11
- **MU** PUT 835 2026-11-06 (4DTE): 558 traded vs OI 325
- **MU** PUT 835 2026-11-04 (2DTE): 688 traded vs OI 169
- **MU** PUT 865 2026-11-06 (4DTE): 884 traded vs OI 878
- **MSTR** PUT 135 2026-11-06 (4DTE): 1,647 traded vs OI 1,645

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
