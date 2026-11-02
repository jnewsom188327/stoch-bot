# GEX + FLOW SCAN - Mon Nov 02, 03:55 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 1.48 | +291% (43m) | **+128%** (done) | +11% | 692.76 hit |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 1.27 | +111% (58m) | **+79%** (done) | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (7 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors
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
| 1 | **MU** | 834.60 | - | **-** | 33 | - | NEG -$212.9M | - | 910 | 850 | +$199.9M | +$4.1M bull / -$2.1M bear | out (clean 31, ADX 48, RVol 2.9) |
| 2 | **SMH** | 509.70 | - | **-** | 31 | - | NEG -$343.8M | - | 532.5 | 500 | +$10.0M | +$37k bull / -$190k bear | out (clean 33, ADX 49, RVol 1.6) |
| 3 | **SHOP** | 154.50 | - | **-** | 30 | - | NEG -$512k | - | 145 | 160 | +$1.1M | +$28k bull / +$0 bear | out (clean 31, ADX 43, RVol 2.9) |
| 4 | **AMD** | 469.68 | - | **-** | 29 | - | NEG -$108.9M | - | 430 | 440 | +$58.3M | +$2.7M bull / -$692k bear | out (clean 33, ADX 56, RVol 1.9) |
| 5 | **MSFT** | 508.19 | - | **-** | 29 | - | POS +$7.5M | 507.1 | 535 | 510 | +$12.7M | +$2.3M bull / +$0 bear | out (clean 29, ADX 67, RVol 2.4) |
| 6 | **PLTR** | 179.66 | - | **-** | 27 | - | NEG -$13.4M | - | 165 | 180 | +$6.8M | +$168k bull / +$0 bear | out (clean 27, ADX 46, RVol 2.2) |
| 7 | **DELL** | 393.30 | - | **-** | 26 | - | NEG -$20.2M | - | 430 | 400 | +$4.0M | +$688k bull / +$0 bear | out (clean 35, ADX 48, RVol 1.6) |
| 8 | **SPY** | 753.08 | - | **-** | 25 | - | NEG -$11.0B | 775.95 | 770 | 750 | +$237.8M | +$10.4M bull / +$0 bear | out (clean 31, ADX 43, RVol 1.8) |
| 9 | **QQQ** | 682.15 | - | **-** | 25 | - | NEG -$5.4B | - | 720 | 680 | +$229.0M | +$2.4M bull / -$208k bear | out (clean 32, ADX 51, RVol 1.7) |
| 10 | **NVDA** | 202.52 | - | **-** | 25 | - | NEG -$240.0M | - | 210 | 200 | +$25.3M | +$671k bull / -$172k bear | out (clean 30, ADX 40, RVol 2.5) |
| 11 | **AAPL** | 338.98 | - | **-** | 24 | - | POS +$27.0M | 336.53 | 350 | 330 | +$28.1M | +$3.7M bull / -$127k bear | out (clean 32, ADX 22, RVol 3.1) |
| 12 | **AMZN** | 245.97 | - | **-** | 24 | - | POS +$24.1M | 243.82 | 250 | 250 | -$13.5M | +$683k bull / +$0 bear | out (clean 34, ADX 46, RVol 1.5) |
| 13 | **MSTR** | 130.48 | - | **-** | 24 | - | NEG -$2.2M | 137.47 | 135 | 125 | +$5.0M | +$36k bull / +$0 bear | out (clean 26, ADX 34, RVol 1.6) |
| 14 | **ORCL** | 119.11 | - | **-** | 22 | - | NEG -$44.0M | - | 130 | 120 | +$1.1M | +$39k bull / +$0 bear | out (clean 32, ADX 34, RVol 4.1) |
| 15 | **IWM** | 279.48 | - | **-** | 20 | - | NEG -$1.4B | 287.11 | 285 | 270 | +$8.0M | +$189k bull / +$0 bear | out (clean 33, ADX 27, RVol 1.3) |
| 16 | **TSLA** | 402.98 | - | **-** | 20 | - | POS +$219.8M | - | 400 | 400 | -$22.0M | +$868k bull / -$2.5M bear | out (clean 32, ADX 40, RVol 1.0) |
| 17 | **AVGO** | 324.12 | - | **-** | 20 | - | NEG -$115.5M | - | 340 | 320 | -$766k | +$125k bull / +$0 bear | out (clean 32, ADX 34, RVol 1.6) |
| 18 | **SMCI** | 30.61 | - | **-** | 20 | - | NEG -$998k | - | 33 | 30 | +$966k | - | out (clean 36, ADX 42, RVol 2.6) |
| 19 | **GOOGL** | 279.38 | - | **-** | 19 | - | NEG -$99.3M | - | 280 | 280 | -$987k | +$216k bull / +$0 bear | out (clean 33, ADX 27, RVol 1.7) |
| 20 | **HOOD** | 84.03 | - | **-** | 19 | - | NEG -$11.3M | - | 85 | 90 | +$719k | +$34k bull / -$87k bear | out (clean 32, ADX 29, RVol 1.0) |
| 21 | **META** | 607.29 | - | **-** | 18 | - | NEG -$145.3M | 622.44 | 650 | 610 | +$13.6M | +$226k bull / +$0 bear | out (clean 28, ADX 14, RVol 1.4) |
| 22 | **CRM** | 225.91 | - | **-** | 18 | - | NEG -$11.0M | - | 240 | 220 | +$148k | - | out (clean 28, ADX 39, RVol 2.5) |
| 23 | **BABA** | 101.68 | - | **-** | 18 | - | POS +$356k | 101.35 | 105 | 100 | -$854k | - | out (clean 33, ADX 46, RVol 1.5) |
| 24 | **ARM** | 198.06 | - | **-** | 16 | - | NEG -$6.5M | - | 200 | 200 | +$268k | - | out (clean 26, ADX 36, RVol 2.0) |
| 25 | **UBER** | 66.52 | - | **-** | 16 | - | NEG -$12.7M | - | 70 | 65 | -$377k | - | out (clean 29, ADX 34, RVol 2.3) |
| 26 | **COIN** | 137.72 | - | **-** | 13 | - | NEG -$8.4M | - | 150 | 130 | -$223k | - | out (clean 25, ADX 33, RVol 2.5) |
| 27 | **NFLX** | 62.36 | - | **-** | 11 | - | NEG -$20.7M | - | 63 | 60 | -$642k | - | out (clean 28, ADX 27, RVol 1.4) |

## Big prints this scan (125)
- **SPY** PUT 758 2026-11-04 (2DTE): 980 @ 7.67 = **+$752k** SELL | vol 9,713 / OI 3,730
- **SPY** PUT 767 2026-11-04 (2DTE): 500 @ 14.37 = **+$718k** SELL | vol 8,480 / OI 36,998
- **TSLA** CALL 390 2026-11-06 (4DTE): 195 @ 17.40 = **+$339k** SELL | vol 1,322 / OI 1,216
- **AMD** CALL 470 2026-11-02 (0DTE): 2,299 @ 1.27 = **+$292k** BUY | vol 11,197 / OI 3
- **MU** PUT 840 2026-11-09 (7DTE): 70 @ 35.49 = **+$248k** BUY | vol 247 / OI 16
- **SPY** PUT 758 2026-11-02 (0DTE): 500 @ 4.93 = **+$246k** SELL | vol 418,337 / OI 1,174
- **MU** CALL 800 2026-11-06 (4DTE): 50 @ 48.87 = **+$244k** SELL | vol 426 / OI 53
- **TSLA** CALL 390 2026-11-02 (0DTE): 195 @ 11.80 = **+$230k** SELL | vol 935 / OI 736
- **MU** PUT 840 2026-11-06 (4DTE): 70 @ 32.50 = **+$228k** BUY | vol 2,297 / OI 868
- **AMD** PUT 490 2026-11-02 (0DTE): 100 @ 22.30 = **+$223k** MID | vol 15,035 / OI 121
- **SPY** PUT 757 2026-11-02 (0DTE): 500 @ 4.01 = **+$200k** SELL | vol 358,731 / OI 3,983
- **MSFT** CALL 510 2026-11-06 (4DTE): 250 @ 8.00 = **+$200k** BUY | vol 380 / OI 135
- **MU** PUT 840 2026-11-06 (4DTE): 60 @ 32.63 = **+$196k** BUY | vol 2,297 / OI 868
- **SPY** PUT 745 2026-11-06 (4DTE): 450 @ 4.18 = **+$188k** SELL | vol 15,389 / OI 12,695
- **SPY** PUT 745 2026-11-06 (4DTE): 450 @ 4.18 = **+$188k** SELL | vol 15,389 / OI 12,695

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 730 2026-11-04 (2DTE): 1,666 traded vs OI 1,416
- **SPY** PUT 739 2026-11-04 (2DTE): 632 traded vs OI 315
- **SPY** PUT 755 2026-11-11 (9DTE): 769 traded vs OI 758
- **QQQ** PUT 630 2026-11-04 (2DTE): 706 traded vs OI 695
- **QQQ** CALL 680 2026-11-10 (8DTE): 570 traded vs OI 60
- **QQQ** CALL 681 2026-11-03 (1DTE): 870 traded vs OI 0
- **QQQ** CALL 704 2026-11-06 (4DTE): 500 traded vs OI 359
- **QQQ** CALL 683 2026-11-06 (4DTE): 563 traded vs OI 26
- **QQQ** PUT 683 2026-11-06 (4DTE): 995 traded vs OI 939
- **QQQ** CALL 680 2026-11-27 (25DTE): 552 traded vs OI 126
- **SMH** CALL 515 2026-11-06 (4DTE): 506 traded vs OI 14
- **SMH** CALL 520 2026-11-20 (18DTE): 547 traded vs OI 237
- **NVDA** CALL 202.5 2026-11-09 (7DTE): 519 traded vs OI 0
- **TSLA** CALL 400 2026-11-11 (9DTE): 500 traded vs OI 139
- **TSLA** CALL 390 2026-11-02 (0DTE): 935 traded vs OI 736

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
