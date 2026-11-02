# GEX + FLOW SCAN - Mon Nov 02, 03:25 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 1.48 | +291% (43m) | **+128%** (done) | +11% | 692.76 hit |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 1.27 | +111% (58m) | **+79%** (done) | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (7 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:25:08 ET, last candle SPY 15:24, QQQ 15:24 | no errors
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
| 1 | **MU** | 839.68 | - | **-** | 30 | - | NEG -$252.4M | - | 910 | 850 | +$179.1M | +$2.7M bull / -$4.4M bear | out (clean 32, ADX 48, RVol 1.2) |
| 2 | **SMH** | 513.29 | - | **-** | 29 | - | NEG -$352.9M | - | 532.5 | 500 | +$8.8M | +$202k bull / -$167k bear | out (clean 33, ADX 50, RVol 0.9) |
| 3 | **AMD** | 472.28 | - | **-** | 27 | - | NEG -$113.6M | - | 430 | 440 | +$51.8M | +$1.4M bull / -$426k bear | out (clean 33, ADX 57, RVol 1.2) |
| 4 | **QQQ** | 685.26 | - | **-** | 24 | - | NEG -$5.5B | - | 720 | 680 | +$200.6M | +$4.2M bull / -$1.5M bear | out (clean 32, ADX 49, RVol 0.8) |
| 5 | **SPY** | 755.27 | - | **-** | 23 | - | NEG -$10.7B | 775.45 | 800 | 750 | +$170.4M | +$1.7M bull / -$1.3M bear | out (clean 31, ADX 43, RVol 1.2) |
| 6 | **NVDA** | 204.01 | - | **-** | 23 | - | NEG -$258.1M | - | 210 | 200 | +$22.1M | +$296k bull / -$433k bear | out (clean 30, ADX 39, RVol 1.2) |
| 7 | **AMZN** | 247.79 | - | **-** | 23 | - | POS +$49.0M | 243.63 | 250 | 250 | -$16.9M | +$169k bull / -$43k bear | out (clean 34, ADX 41, RVol 0.8) |
| 8 | **MSFT** | 512.96 | - | **-** | 23 | - | POS +$93.4M | 503.22 | 535 | 510 | +$5.6M | +$1.5M bull / +$0 bear | out (clean 28, ADX 57, RVol 1.0) |
| 9 | **PLTR** | 181.52 | - | **-** | 22 | - | NEG -$13.2M | - | 165 | 180 | +$4.2M | +$163k bull / -$213k bear | out (clean 27, ADX 41, RVol 0.8) |
| 10 | **AAPL** | 338.77 | - | **-** | 21 | - | POS +$24.6M | 336.95 | 350 | 330 | +$19.1M | +$98k bull / -$849k bear | out (clean 32, ADX 26, RVol 1.1) |
| 11 | **SHOP** | 157.19 | - | **-** | 21 | - | NEG -$441k | - | 170 | 160 | -$186k | +$29k bull / +$0 bear | out (clean 30, ADX 32, RVol 1.6) |
| 12 | **IWM** | 280.48 | - | **-** | 20 | - | NEG -$1.2B | 286.93 | 285 | 270 | +$5.9M | +$0 bull / -$108k bear | out (clean 33, ADX 32, RVol 1.2) |
| 13 | **COIN** | 136.66 | - | **-** | 20 | - | NEG -$8.4M | - | 150 | 130 | -$178k | +$0 bull / -$36k bear | out (clean 25, ADX 41, RVol 0.6) |
| 14 | **ORCL** | 120.17 | - | **-** | 20 | - | NEG -$43.7M | - | 130 | 120 | +$636k | +$92k bull / +$0 bear | out (clean 33, ADX 38, RVol 1.1) |
| 15 | **TSLA** | 403.86 | - | **-** | 19 | - | POS +$216.9M | - | 405 | 400 | -$26.8M | +$2.8M bull / -$1.2M bear | out (clean 32, ADX 39, RVol 0.7) |
| 16 | **NFLX** | 62.41 | - | **-** | 19 | - | NEG -$22.3M | - | 63 | 60 | -$638k | +$28k bull / +$0 bear | out (clean 29, ADX 23, RVol 0.8) |
| 17 | **HOOD** | 84.40 | - | **-** | 19 | - | NEG -$11.4M | - | 85 | 90 | +$537k | +$0 bull / -$128k bear | out (clean 32, ADX 32, RVol 1.0) |
| 18 | **AVGO** | 325.77 | - | **-** | 18 | - | NEG -$113.3M | - | 340 | 330 | -$2.4M | +$35k bull / -$67k bear | out (clean 32, ADX 34, RVol 0.5) |
| 19 | **SMCI** | 31.04 | - | **-** | 18 | - | NEG -$880k | - | 34 | 30 | +$863k | - | out (clean 36, ADX 45, RVol 1.3) |
| 20 | **ARM** | 200.38 | - | **-** | 17 | - | NEG -$5.6M | - | 200 | 200 | +$268k | - | out (clean 26, ADX 35, RVol 2.7) |
| 21 | **META** | 610.92 | - | **-** | 16 | - | NEG -$146.4M | 626.07 | 650 | 610 | +$10.4M | +$468k bull / -$63k bear | out (clean 28, ADX 13, RVol 0.4) |
| 22 | **GOOGL** | 282.38 | - | **-** | 16 | - | NEG -$101.3M | - | 285 | 290 | -$2.1M | +$239k bull / -$99k bear | out (clean 33, ADX 18, RVol 0.5) |
| 23 | **BABA** | 102.29 | - | **-** | 15 | - | POS +$1.5M | 101.1 | 105 | 100 | -$942k | - | out (clean 33, ADX 39, RVol 0.5) |
| 24 | **UBER** | 66.80 | - | **-** | 14 | - | NEG -$8.1M | - | 70 | 65 | -$399k | - | out (clean 29, ADX 38, RVol 0.9) |
| 25 | **CRM** | 226.84 | - | **-** | 14 | - | NEG -$10.1M | - | 240 | 220 | +$104k | - | out (clean 28, ADX 37, RVol 1.4) |
| 26 | **DELL** | 399.13 | - | **-** | 12 | - | NEG -$21.4M | - | 430 | 400 | +$2.3M | - | out (clean 34, ADX 44, RVol 0.6) |
| 27 | **MSTR** | 131.22 | - | **-** | 12 | - | NEG -$513k | 133.27 | 135 | 125 | +$4.4M | - | out (clean 26, ADX 31, RVol 0.9) |

## Big prints this scan (91)
- **QQQ** PUT 690 2026-11-02 (0DTE): 999 @ 4.52 = **+$452k** SELL | vol 254,675 / OI 2,736
- **NVDA** PUT 205 2026-11-04 (2DTE): 500 @ 3.55 = **+$178k** SELL | vol 18,494 / OI 1,782
- **MSFT** PUT 510 2026-11-06 (4DTE): 250 @ 6.30 = **+$158k** SELL | vol 1,379 / OI 1,340
- **SPY** CALL 750 2026-11-02 (0DTE): 298 @ 5.25 = **+$156k** BUY | vol 4,871 / OI 75
- **MU** PUT 850 2026-11-06 (4DTE): 43 @ 33.92 = **+$146k** SELL | vol 4,654 / OI 1,436
- **QQQ** PUT 715 2026-11-02 (0DTE): 50 @ 28.96 = **+$145k** SELL | vol 117 / OI 3,259
- **QQQ** PUT 715 2026-11-03 (1DTE): 50 @ 28.96 = **+$145k** SELL | vol 95 / OI 620
- **MU** CALL 835 2026-11-02 (0DTE): 200 @ 7.20 = **+$144k** BUY | vol 4,478 / OI 8
- **QQQ** CALL 686 2026-11-03 (1DTE): 250 @ 5.30 = **+$132k** BUY | vol 6,877 / OI 0
- **MU** CALL 860 2026-11-04 (2DTE): 100 @ 12.75 = **+$128k** MID | vol 2,534 / OI 37
- **MU** PUT 840 2026-11-06 (4DTE): 43 @ 28.75 = **+$124k** SELL | vol 1,954 / OI 868
- **TSLA** PUT 400 2026-11-04 (2DTE): 200 @ 5.80 = **+$116k** SELL | vol 13,608 / OI 1,553
- **MU** PUT 835 2026-11-06 (4DTE): 43 @ 26.45 = **+$114k** SELL | vol 1,136 / OI 325
- **QQQ** PUT 685 2026-11-09 (7DTE): 100 @ 11.15 = **+$112k** SELL | vol 2,310 / OI 430
- **MU** PUT 850 2026-11-06 (4DTE): 32 @ 33.92 = **+$109k** SELL | vol 4,654 / OI 1,436

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 737 2026-11-03 (1DTE): 1,207 traded vs OI 1,182
- **SPY** CALL 775 2026-11-04 (2DTE): 3,767 traded vs OI 3,750
- **SPY** PUT 752 2026-11-13 (11DTE): 1,441 traded vs OI 1,111
- **QQQ** CALL 745 2026-11-05 (3DTE): 1,316 traded vs OI 1,248
- **QQQ** CALL 753 2026-11-06 (4DTE): 2,034 traded vs OI 394
- **QQQ** CALL 718 2026-11-13 (11DTE): 524 traded vs OI 109
- **QQQ** PUT 682 2026-11-13 (11DTE): 1,433 traded vs OI 37
- **QQQ** PUT 717 2026-11-30 (28DTE): 606 traded vs OI 236
- **IWM** CALL 279 2026-11-06 (4DTE): 533 traded vs OI 422
- **IWM** CALL 278 2026-11-03 (1DTE): 1,223 traded vs OI 308
- **SMH** PUT 495 2026-11-04 (2DTE): 654 traded vs OI 10
- **SMH** CALL 512.5 2026-11-02 (0DTE): 518 traded vs OI 0
- **SMH** CALL 540 2026-11-06 (4DTE): 513 traded vs OI 221
- **AAPL** CALL 340 2026-11-27 (25DTE): 1,601 traded vs OI 384
- **MSFT** PUT 510 2026-11-06 (4DTE): 1,379 traded vs OI 1,340

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
