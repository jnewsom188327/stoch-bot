# GEX + FLOW SCAN - Mon Nov 02, 01:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 1.48 | +291% (43m) | **+128%** (done) | +11% | 692.76 hit |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 1.27 | +111% (58m) | **+79%** (done) | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:10:08 ET, last candle SPY 13:09, QQQ 13:09 | no errors
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
| 1 | **SHOP** | 160.59 | FLOW SURGE | **PUTS** | 42 | none: 16 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$139k | - | 175 | 175 | -$764k | +$0 bull / -$31k bear | out (clean 28, ADX 25, RVol 0.9) |
| 2 | **SMCI** | 31.60 | TREND (flow not with it) | **PUTS** | 36 | none: 13 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$422k | - | 34 | 30 | +$455k | - | SHORT (clean 34, ADX 40, RVol 1.4) |
| 3 | **MSFT** | 520.17 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | 11/02 522.5C @ 0.60 (delta 0.26) = est +315% at 525 | POS +$246.2M | 501.87 | 540 | 520 | -$1.0M | +$114k bull / -$85k bear | out (clean 27, ADX 29, RVol 0.4) |
| 4 | **MU** | 854.88 | - | **-** | 28 | - | NEG -$218.3M | - | 910 | 850 | +$123.3M | +$593k bull / -$3.3M bear | out (clean 31, ADX 38, RVol 1.0) |
| 5 | **AMD** | 483.73 | - | **-** | 27 | - | NEG -$81.8M | - | 500 | 480 | +$33.6M | +$2.9M bull / -$1.7M bear | out (clean 31, ADX 40, RVol 1.6) |
| 6 | **SMH** | 520.71 | - | **-** | 23 | - | NEG -$350.8M | - | 532.5 | 500 | +$3.3M | +$0 bull / -$150k bear | out (clean 31, ADX 22, RVol 1.2) |
| 7 | **AAPL** | 338.07 | - | **-** | 23 | - | POS +$13.1M | 337 | 350 | 330 | +$16.9M | +$111k bull / -$1.3M bear | out (clean 31, ADX 31, RVol 0.9) |
| 8 | **AMZN** | 250.75 | - | **-** | 21 | - | POS +$99.3M | 241.99 | 250 | 250 | -$22.7M | +$43k bull / -$864k bear | out (clean 33, ADX 24, RVol 0.4) |
| 9 | **META** | 611.16 | - | **-** | 19 | - | NEG -$128.2M | 622.47 | 650 | 610 | +$11.1M | +$1.8M bull / -$463k bear | out (clean 29, ADX 24, RVol 0.5) |
| 10 | **MSTR** | 134.03 | - | **-** | 19 | - | POS +$2.8M | - | 135 | 125 | +$3.4M | +$0 bull / -$68k bear | out (clean 26, ADX 19, RVol 0.7) |
| 11 | **IWM** | 281.47 | - | **-** | 18 | - | NEG -$940.4M | 286.56 | 285 | 270 | -$1.2M | +$684k bull / -$453k bear | out (clean 32, ADX 23, RVol 1.7) |
| 12 | **TSLA** | 408.10 | - | **-** | 18 | - | POS +$310.2M | - | 410 | 400 | -$68.5M | +$547k bull / -$1.2M bear | out (clean 30, ADX 22, RVol 0.6) |
| 13 | **ORCL** | 122.75 | - | **-** | 18 | - | NEG -$39.6M | - | 130 | 120 | -$609k | +$0 bull / -$32k bear | out (clean 31, ADX 32, RVol 0.5) |
| 14 | **SPY** | 759.12 | - | **-** | 17 | - | NEG -$9.8B | 774.51 | 800 | 750 | +$15.4M | +$1.7M bull / -$2.2M bear | out (clean 30, ADX 24, RVol 1.1) |
| 15 | **QQQ** | 692.00 | - | **-** | 17 | - | NEG -$5.5B | 732.69 | 720 | 680 | +$41.0M | +$1.1M bull / -$2.4M bear | out (clean 30, ADX 24, RVol 0.7) |
| 16 | **DELL** | 407.63 | - | **-** | 17 | - | NEG -$21.6M | - | 440 | 400 | +$192k | +$150k bull / -$130k bear | out (clean 33, ADX 25, RVol 1.2) |
| 17 | **BABA** | 103.08 | - | **-** | 17 | - | POS +$2.6M | 101.02 | 105 | 100 | -$1.0M | - | out (clean 33, ADX 25, RVol 1.8) |
| 18 | **NVDA** | 206.82 | - | **-** | 16 | - | NEG -$185.6M | 213.67 | 210 | 200 | +$6.4M | +$96k bull / -$706k bear | out (clean 29, ADX 16, RVol 1.0) |
| 19 | **PLTR** | 184.33 | - | **-** | 16 | - | NEG -$11.5M | - | 200 | 180 | +$2.4M | +$89k bull / -$147k bear | out (clean 25, ADX 12, RVol 0.6) |
| 20 | **GOOGL** | 283.48 | - | **-** | 15 | - | NEG -$90.7M | - | 285 | 285 | +$1.4M | +$0 bull / -$196k bear | out (clean 34, ADX 16, RVol 0.4) |
| 21 | **UBER** | 67.31 | - | **-** | 14 | - | NEG -$8.0M | - | 70 | 65 | -$475k | - | out (clean 28, ADX 26, RVol 0.7) |
| 22 | **ARM** | 203.23 | - | **-** | 11 | - | NEG -$6.9M | - | 220 | 200 | +$287k | - | out (clean 24, ADX 18, RVol 0.3) |
| 23 | **AVGO** | 329.79 | - | **-** | 9 | - | NEG -$102.1M | - | 340 | 330 | -$5.2M | - | out (clean 30, ADX 21, RVol 0.4) |
| 24 | **NFLX** | 62.63 | - | **-** | 8 | - | NEG -$19.4M | - | 63 | 60 | -$252k | - | out (clean 28, ADX 27, RVol 0.6) |
| 25 | **COIN** | 139.87 | - | **-** | 8 | - | NEG -$7.9M | - | 150 | 130 | -$390k | - | out (clean 23, ADX 11, RVol 1.0) |
| 26 | **HOOD** | 85.53 | - | **-** | 7 | - | NEG -$8.9M | - | 93 | 90 | -$314k | - | out (clean 32, ADX 26, RVol 0.5) |
| 27 | **CRM** | 232.29 | - | **-** | 5 | - | NEG -$5.2M | 242.38 | 240 | 220 | +$44k | - | out (clean 26, ADX 12, RVol 0.4) |

## Big prints this scan (70)
- **SPY** CALL 755 2026-11-05 (3DTE): 1,000 @ 7.44 = **+$744k** SELL | vol 2,420 / OI 87
- **SPY** CALL 755 2026-11-05 (3DTE): 851 @ 7.80 = **+$664k** SELL | vol 2,420 / OI 87
- **QQQ** CALL 670 2026-11-09 (7DTE): 100 @ 25.89 = **+$259k** SELL | vol 226 / OI 0
- **QQQ** CALL 691 2026-11-06 (4DTE): 243 @ 9.90 = **+$241k** SELL | vol 1,204 / OI 87
- **AMD** CALL 500 2026-11-06 (4DTE): 150 @ 16.00 = **+$240k** SELL | vol 1,058 / OI 354
- **QQQ** CALL 691 2026-11-06 (4DTE): 203 @ 10.06 = **+$204k** SELL | vol 1,204 / OI 87
- **QQQ** CALL 690 2026-11-02 (0DTE): 750 @ 2.50 = **+$188k** SELL | vol 22,584 / OI 33
- **QQQ** PUT 700 2026-11-03 (1DTE): 151 @ 10.60 = **+$160k** BUY | vol 6,160 / OI 1,423
- **IWM** CALL 285 2026-11-09 (7DTE): 809 @ 1.77 = **+$143k** SELL | vol 5,252 / OI 0
- **SPY** PUT 760 2026-11-06 (4DTE): 200 @ 6.68 = **+$134k** BUY | vol 8,425 / OI 17,598
- **SPY** CALL 755 2026-11-05 (3DTE): 149 @ 7.80 = **+$116k** SELL | vol 2,420 / OI 87
- **MU** CALL 880 2026-11-06 (4DTE): 75 @ 15.25 = **+$114k** SELL | vol 2,221 / OI 553
- **SPY** PUT 758 2026-11-02 (0DTE): 834 @ 1.37 = **+$114k** BUY | vol 260,524 / OI 1,174
- **QQQ** PUT 680 2026-11-09 (7DTE): 153 @ 6.94 = **+$106k** BUY | vol 1,814 / OI 213
- **QQQ** PUT 690 2026-11-04 (2DTE): 140 @ 7.29 = **+$102k** BUY | vol 3,910 / OI 1,124

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 732 2026-11-06 (4DTE): 721 traded vs OI 718
- **SPY** PUT 770 2026-11-03 (1DTE): 1,239 traded vs OI 1,238
- **SPY** PUT 730 2026-11-13 (11DTE): 3,572 traded vs OI 3,493
- **QQQ** PUT 679 2026-11-04 (2DTE): 502 traded vs OI 0
- **QQQ** PUT 687 2026-11-04 (2DTE): 675 traded vs OI 0
- **QQQ** CALL 695 2026-11-10 (8DTE): 507 traded vs OI 17
- **IWM** PUT 277 2026-11-09 (7DTE): 525 traded vs OI 75
- **IWM** CALL 287.5 2026-11-09 (7DTE): 522 traded vs OI 0
- **IWM** CALL 289 2026-11-04 (2DTE): 934 traded vs OI 841
- **IWM** PUT 277 2026-11-03 (1DTE): 1,175 traded vs OI 1,140
- **IWM** PUT 267 2026-11-27 (25DTE): 1,013 traded vs OI 214
- **SMH** PUT 475 2026-11-06 (4DTE): 774 traded vs OI 583
- **NVDA** CALL 227.5 2026-11-20 (18DTE): 2,908 traded vs OI 1,966
- **TSLA** PUT 375 2026-11-06 (4DTE): 2,626 traded vs OI 2,607
- **TSLA** CALL 407.5 2026-11-13 (11DTE): 507 traded vs OI 268

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
