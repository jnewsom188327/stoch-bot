# GEX + FLOW SCAN - Mon Nov 02, 01:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 1.48 | +291% (43m) | **+128%** (done) | +11% | 692.76 hit |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 1.27 | +111% (58m) | **+79%** (done) | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:50:08 ET, last candle SPY 13:49, QQQ 13:49 | no errors
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
| 1 | **MU** | 845.95 | FLOW SURGE | **CALLS** | 41 | none: 137 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (56 contracts' greeks worked out here) | NEG -$225.6M | - | 910 | 850 | +$147.8M | +$5.6M bull / +$0 bear | out (clean 31, ADX 41, RVol 0.8) |
| 2 | **AAPL** | 336.94 | FLIP CROSS up into positive gamma | **CALLS** | 40 | none: 81 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$1.2M | 336.79 | 350 | 330 | +$23.3M | +$3.3M bull / -$44k bear | out (clean 31, ADX 37, RVol 1.0) |
| 3 | **SMCI** | 31.14 | TREND (flow not with it) | **PUTS** | 35 | none: 12 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$423k | - | 34 | 30 | +$727k | - | SHORT (clean 34, ADX 46, RVol 1.0) |
| 4 | **AMZN** | 249.56 | PINNED between the walls (positive gamma) - chop | **-** | 32 | - | POS +$75.9M | 243.58 | 250 | 250 | -$20.5M | +$47k bull / -$31k bear | out (clean 33, ADX 25, RVol 0.4) |
| 5 | **AMD** | 479.11 | - | **-** | 26 | - | NEG -$77.2M | - | 500 | 480 | +$40.9M | +$4.7M bull / +$0 bear | out (clean 32, ADX 46, RVol 0.7) |
| 6 | **SMH** | 517.12 | - | **-** | 24 | - | NEG -$355.2M | - | 532.5 | 500 | +$4.2M | +$226k bull / +$0 bear | out (clean 31, ADX 29, RVol 0.7) |
| 7 | **DELL** | 404.40 | TREND (flow not with it) | **PUTS** | 22 | none: 32 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$20.6M | - | 440 | 400 | +$770k | - | SHORT (clean 33, ADX 31, RVol 0.6) |
| 8 | **MSFT** | 518.47 | - | **-** | 19 | - | POS +$195.2M | 501.79 | 540 | 500 | -$965k | +$62k bull / -$140k bear | out (clean 27, ADX 35, RVol 0.9) |
| 9 | **NFLX** | 62.77 | - | **-** | 19 | - | NEG -$19.0M | - | 63 | 60 | -$518k | +$0 bull / -$97k bear | out (clean 28, ADX 28, RVol 0.6) |
| 10 | **QQQ** | 689.64 | - | **-** | 18 | - | NEG -$5.5B | - | 720 | 680 | +$64.4M | +$1.5M bull / +$0 bear | out (clean 30, ADX 28, RVol 0.4) |
| 11 | **SPY** | 757.46 | - | **-** | 17 | - | NEG -$10.1B | 774.4 | 770 | 750 | +$47.0M | +$2.4M bull / +$0 bear | out (clean 30, ADX 26, RVol 0.6) |
| 12 | **NVDA** | 205.84 | - | **-** | 17 | - | NEG -$207.9M | 214.73 | 210 | 205 | +$8.5M | +$890k bull / +$0 bear | out (clean 28, ADX 18, RVol 1.0) |
| 13 | **TSLA** | 407.66 | - | **-** | 17 | - | POS +$310.0M | - | 410 | 400 | -$66.0M | +$669k bull / +$0 bear | out (clean 30, ADX 19, RVol 0.5) |
| 14 | **GOOGL** | 284.08 | - | **-** | 17 | - | NEG -$85.8M | - | 285 | 285 | -$4.6M | +$96k bull / -$1.4M bear | out (clean 34, ADX 19, RVol 0.3) |
| 15 | **PLTR** | 183.63 | - | **-** | 17 | - | NEG -$11.1M | - | 200 | 180 | +$2.6M | +$28k bull / +$0 bear | out (clean 25, ADX 17, RVol 0.7) |
| 16 | **META** | 613.27 | - | **-** | 16 | - | NEG -$124.2M | 625.76 | 650 | 610 | +$8.5M | +$60k bull / -$321k bear | out (clean 29, ADX 20, RVol 0.3) |
| 17 | **SHOP** | 159.40 | - | **-** | 15 | - | NEG -$457k | - | 175 | 175 | -$644k | - | out (clean 28, ADX 20, RVol 0.6) |
| 18 | **BABA** | 102.76 | - | **-** | 13 | - | POS +$1.9M | 101.29 | 105 | 100 | -$1.0M | - | out (clean 33, ADX 21, RVol 0.4) |
| 19 | **UBER** | 67.09 | - | **-** | 12 | - | NEG -$8.5M | - | 70 | 65 | -$473k | - | out (clean 27, ADX 23, RVol 0.5) |
| 20 | **ARM** | 202.34 | - | **-** | 11 | - | NEG -$6.9M | - | 220 | 200 | +$257k | - | out (clean 25, ADX 21, RVol 0.6) |
| 21 | **AVGO** | 328.12 | - | **-** | 8 | - | NEG -$103.4M | - | 340 | 330 | -$4.7M | - | out (clean 30, ADX 19, RVol 0.3) |
| 22 | **MSTR** | 133.09 | - | **-** | 8 | - | POS +$2.4M | - | 135 | 125 | +$3.6M | - | out (clean 25, ADX 15, RVol 0.4) |
| 23 | **ORCL** | 121.50 | - | **-** | 8 | - | NEG -$36.9M | - | 130 | 120 | -$200k | - | out (clean 32, ADX 36, RVol 0.7) |
| 24 | **IWM** | 280.55 | - | **-** | 7 | - | NEG -$1.1B | 286.82 | 285 | 270 | +$1.7M | - | out (clean 32, ADX 26, RVol 0.7) |
| 25 | **COIN** | 138.77 | - | **-** | 7 | - | NEG -$7.8M | - | 150 | 130 | -$304k | - | out (clean 23, ADX 15, RVol 0.8) |
| 26 | **CRM** | 231.00 | - | **-** | 7 | - | NEG -$6.1M | 242.54 | 240 | 220 | +$50k | - | out (clean 26, ADX 12, RVol 1.2) |
| 27 | **HOOD** | 84.81 | - | **-** | 6 | - | NEG -$10.3M | - | 93 | 90 | -$159k | - | out (clean 32, ADX 29, RVol 0.3) |

## Big prints this scan (88)
- **SPY** CALL 755 2026-11-05 (3DTE): 529 @ 7.75 = **+$410k** BUY | vol 5,593 / OI 87
- **SPY** CALL 755 2026-11-06 (4DTE): 300 @ 8.91 = **+$267k** BUY | vol 1,686 / OI 911
- **SPY** CALL 755 2026-11-06 (4DTE): 300 @ 8.87 = **+$266k** BUY | vol 1,686 / OI 911
- **SPY** CALL 756 2026-11-06 (4DTE): 300 @ 8.26 = **+$248k** BUY | vol 1,427 / OI 188
- **SPY** CALL 755 2026-11-05 (3DTE): 319 @ 7.75 = **+$247k** BUY | vol 5,593 / OI 87
- **SPY** CALL 756 2026-11-06 (4DTE): 300 @ 8.22 = **+$247k** BUY | vol 1,427 / OI 188
- **SPY** PUT 755 2026-11-06 (4DTE): 450 @ 4.91 = **+$221k** SELL | vol 8,064 / OI 6,105
- **META** CALL 620 2026-11-06 (4DTE): 150 @ 9.55 = **+$143k** SELL | vol 2,047 / OI 1,057
- **MU** PUT 855 2026-11-02 (0DTE): 198 @ 6.50 = **+$129k** SELL | vol 26,896 / OI 310
- **QQQ** PUT 691 2026-11-03 (1DTE): 258 @ 4.71 = **+$122k** SELL | vol 10,820 / OI 0
- **MU** PUT 855 2026-11-02 (0DTE): 200 @ 5.90 = **+$118k** SELL | vol 26,896 / OI 310
- **SPY** CALL 755 2026-11-05 (3DTE): 152 @ 7.75 = **+$118k** BUY | vol 5,593 / OI 87
- **QQQ** PUT 713 2026-11-06 (4DTE): 49 @ 23.98 = **+$118k** SELL | vol 108 / OI 53,763
- **SPY** PUT 758 2026-11-03 (1DTE): 400 @ 2.91 = **+$116k** SELL | vol 30,297 / OI 494
- **QQQ** CALL 689 2026-11-02 (0DTE): 440 @ 2.50 = **+$110k** BUY | vol 9,453 / OI 0

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 769 2026-11-06 (4DTE): 2,123 traded vs OI 2,107
- **SPY** PUT 728 2026-11-04 (2DTE): 523 traded vs OI 333
- **SPY** PUT 753 2026-11-04 (2DTE): 952 traded vs OI 931
- **SPY** CALL 759 2026-11-20 (18DTE): 509 traded vs OI 394
- **QQQ** CALL 720 2026-11-10 (8DTE): 539 traded vs OI 456
- **IWM** PUT 282 2026-11-05 (3DTE): 547 traded vs OI 540
- **NVDA** CALL 190 2026-11-09 (7DTE): 558 traded vs OI 5
- **AAPL** CALL 335 2026-11-04 (2DTE): 530 traded vs OI 179
- **AMD** PUT 455 2026-11-02 (0DTE): 531 traded vs OI 0
- **MSFT** CALL 542.5 2026-11-06 (4DTE): 844 traded vs OI 841
- **COIN** PUT 140 2026-11-06 (4DTE): 599 traded vs OI 598
- **DELL** PUT 380 2026-11-06 (4DTE): 504 traded vs OI 215
- **HOOD** PUT 82 2026-11-06 (4DTE): 1,016 traded vs OI 1,015

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
