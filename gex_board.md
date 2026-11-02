# GEX + FLOW SCAN - Mon Nov 02, 03:15 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 1.48 | +291% (43m) | **+128%** (done) | +11% | 692.76 hit |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 1.27 | +111% (58m) | **+79%** (done) | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (7 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:15:08 ET, last candle SPY 15:14, QQQ 15:14 | no errors
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
| 1 | **BABA** | 102.21 | TREND + FLOW | **PUTS** | 33 | none: 21 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$1.5M | 101.16 | 105 | 100 | -$944k | - | SHORT (clean 33, ADX 38, RVol 0.5) |
| 2 | **SMH** | 511.13 | - | **-** | 30 | - | NEG -$332.0M | - | 532.5 | 500 | +$8.6M | +$0 bull / -$395k bear | out (clean 33, ADX 52, RVol 1.1) |
| 3 | **MU** | 835.88 | - | **-** | 30 | - | NEG -$218.2M | - | 910 | 850 | +$177.3M | +$179k bull / -$5.6M bear | out (clean 32, ADX 50, RVol 1.2) |
| 4 | **AMD** | 471.48 | - | **-** | 26 | - | NEG -$100.6M | - | 430 | 440 | +$49.4M | +$321k bull / -$574k bear | out (clean 33, ADX 58, RVol 1.1) |
| 5 | **SPY** | 754.39 | - | **-** | 24 | - | NEG -$10.2B | 774.31 | 800 | 750 | +$163.4M | +$491k bull / -$3.2M bear | out (clean 31, ADX 45, RVol 1.4) |
| 6 | **QQQ** | 684.10 | - | **-** | 24 | - | NEG -$5.3B | - | 720 | 680 | +$193.4M | +$1.5M bull / -$2.3M bear | out (clean 32, ADX 50, RVol 0.9) |
| 7 | **AMZN** | 247.82 | - | **-** | 23 | - | POS +$65.1M | 242.7 | 250 | 250 | -$17.6M | +$35k bull / -$157k bear | out (clean 34, ADX 42, RVol 0.7) |
| 8 | **MSFT** | 512.81 | - | **-** | 23 | - | POS +$96.6M | 502.87 | 535 | 510 | +$4.6M | +$1.1M bull / +$0 bear | out (clean 28, ADX 55, RVol 1.0) |
| 9 | **NVDA** | 203.74 | - | **-** | 22 | - | NEG -$234.7M | - | 210 | 200 | +$21.0M | +$0 bull / -$698k bear | out (clean 30, ADX 41, RVol 1.1) |
| 10 | **PLTR** | 180.88 | - | **-** | 22 | - | NEG -$12.9M | - | 165 | 180 | +$4.4M | +$230k bull / -$120k bear | out (clean 27, ADX 42, RVol 0.8) |
| 11 | **AAPL** | 338.33 | - | **-** | 21 | - | POS +$29.4M | 336.55 | 350 | 330 | +$19.4M | +$0 bull / -$197k bear | out (clean 32, ADX 26, RVol 1.3) |
| 12 | **TSLA** | 403.46 | - | **-** | 20 | - | POS +$221.9M | - | 405 | 400 | -$31.1M | +$785k bull / -$2.3M bear | out (clean 32, ADX 38, RVol 0.9) |
| 13 | **COIN** | 135.48 | - | **-** | 20 | - | NEG -$7.0M | - | 140 | 130 | -$173k | +$0 bull / -$36k bear | out (clean 25, ADX 41, RVol 0.7) |
| 14 | **ORCL** | 119.26 | - | **-** | 20 | - | NEG -$43.3M | - | 130 | 120 | +$680k | +$92k bull / -$38k bear | out (clean 33, ADX 43, RVol 0.9) |
| 15 | **HOOD** | 83.98 | - | **-** | 20 | - | NEG -$11.2M | - | 85 | 90 | +$738k | +$0 bull / -$50k bear | out (clean 32, ADX 36, RVol 1.0) |
| 16 | **AVGO** | 324.84 | - | **-** | 19 | - | NEG -$109.4M | - | 340 | 320 | -$2.3M | +$0 bull / -$67k bear | out (clean 32, ADX 36, RVol 0.4) |
| 17 | **ARM** | 199.53 | - | **-** | 18 | - | NEG -$6.2M | - | 200 | 200 | +$295k | - | out (clean 26, ADX 38, RVol 2.6) |
| 18 | **SMCI** | 30.80 | - | **-** | 17 | - | NEG -$931k | - | 33 | 30 | +$871k | - | out (clean 36, ADX 49, RVol 1.1) |
| 19 | **META** | 610.38 | - | **-** | 16 | - | NEG -$124.2M | 621.1 | 650 | 610 | +$9.4M | +$165k bull / -$170k bear | out (clean 28, ADX 15, RVol 0.6) |
| 20 | **GOOGL** | 282.36 | - | **-** | 16 | - | NEG -$94.0M | - | 285 | 290 | -$2.4M | +$209k bull / -$135k bear | out (clean 33, ADX 19, RVol 0.6) |
| 21 | **UBER** | 66.59 | - | **-** | 15 | - | NEG -$12.7M | - | 70 | 65 | -$407k | - | out (clean 29, ADX 42, RVol 0.8) |
| 22 | **CRM** | 226.46 | - | **-** | 14 | - | NEG -$10.0M | - | 240 | 220 | +$113k | - | out (clean 28, ADX 37, RVol 1.3) |
| 23 | **DELL** | 396.98 | - | **-** | 12 | - | NEG -$21.0M | - | 430 | 400 | +$2.3M | - | out (clean 34, ADX 44, RVol 0.7) |
| 24 | **MSTR** | 130.26 | - | **-** | 12 | - | NEG -$1.9M | 136.71 | 135 | 125 | +$4.4M | - | out (clean 26, ADX 32, RVol 0.8) |
| 25 | **SHOP** | 156.92 | - | **-** | 12 | - | NEG -$425k | - | 170 | 160 | -$286k | - | out (clean 30, ADX 32, RVol 1.6) |
| 26 | **IWM** | 279.90 | - | **-** | 10 | - | NEG -$1.2B | 286.93 | 285 | 270 | +$5.5M | - | out (clean 33, ADX 36, RVol 0.9) |
| 27 | **NFLX** | 62.50 | - | **-** | 9 | - | NEG -$21.3M | - | 63 | 60 | -$696k | - | out (clean 29, ADX 22, RVol 0.8) |

## Big prints this scan (89)
- **MSFT** PUT 535 2026-11-04 (2DTE): 228 @ 21.10 = **+$481k** SELL | vol 290 / OI 393
- **MSFT** PUT 535 2026-11-02 (0DTE): 228 @ 20.69 = **+$472k** SELL | vol 297 / OI 234
- **SPY** CALL 755 2026-11-02 (0DTE): 2,916 @ 1.21 = **+$353k** BUY | vol 99,232 / OI 59
- **SPY** PUT 756 2026-11-02 (0DTE): 990 @ 2.58 = **+$255k** BUY | vol 303,155 / OI 1,385
- **AMD** PUT 480 2026-11-04 (2DTE): 100 @ 24.00 = **+$240k** SELL | vol 1,300 / OI 273
- **GOOGL** CALL 285 2026-11-06 (4DTE): 551 @ 3.80 = **+$209k** BUY | vol 12,771 / OI 2,236
- **SPY** PUT 756 2026-11-02 (0DTE): 882 @ 2.26 = **+$199k** BUY | vol 303,155 / OI 1,385
- **QQQ** PUT 680 2026-11-06 (4DTE): 200 @ 8.68 = **+$174k** SELL | vol 12,187 / OI 25,801
- **QQQ** PUT 680 2026-11-06 (4DTE): 200 @ 8.68 = **+$174k** SELL | vol 12,187 / OI 25,801
- **QQQ** PUT 680 2026-11-06 (4DTE): 200 @ 8.68 = **+$174k** SELL | vol 12,187 / OI 25,801
- **QQQ** PUT 680 2026-11-06 (4DTE): 200 @ 8.67 = **+$173k** SELL | vol 12,187 / OI 25,801
- **SPY** CALL 754 2026-11-02 (0DTE): 1,068 @ 1.51 = **+$161k** SELL | vol 52,187 / OI 20
- **QQQ** CALL 680 2026-11-02 (0DTE): 289 @ 5.44 = **+$157k** BUY | vol 3,239 / OI 24
- **TSLA** PUT 405 2026-11-02 (0DTE): 721 @ 2.00 = **+$144k** BUY | vol 205,124 / OI 876
- **SPY** PUT 750 2026-11-04 (2DTE): 431 @ 3.20 = **+$138k** SELL | vol 24,782 / OI 1,303

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 730 2026-11-20 (18DTE): 3,609 traded vs OI 2,692
- **QQQ** PUT 645 2026-11-06 (4DTE): 6,349 traded vs OI 5,885
- **QQQ** CALL 735 2026-11-05 (3DTE): 579 traded vs OI 564
- **QQQ** PUT 666 2026-11-04 (2DTE): 510 traded vs OI 0
- **QQQ** PUT 650 2026-11-13 (11DTE): 4,730 traded vs OI 4,727
- **IWM** PUT 278 2026-11-06 (4DTE): 4,282 traded vs OI 3,269
- **SMH** CALL 547.5 2026-11-06 (4DTE): 661 traded vs OI 227
- **SMH** PUT 477.5 2026-11-06 (4DTE): 544 traded vs OI 11
- **NVDA** CALL 205 2026-11-09 (7DTE): 513 traded vs OI 65
- **TSLA** CALL 422.5 2026-11-06 (4DTE): 2,305 traded vs OI 2,253
- **MSFT** PUT 500 2026-11-06 (4DTE): 1,660 traded vs OI 1,489
- **AVGO** CALL 325 2026-11-04 (2DTE): 505 traded vs OI 8
- **PLTR** CALL 197.5 2026-11-06 (4DTE): 1,567 traded vs OI 1,406
- **COIN** PUT 135 2026-11-06 (4DTE): 511 traded vs OI 477
- **MU** CALL 895 2026-11-06 (4DTE): 506 traded vs OI 163

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
