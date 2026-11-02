# GEX + FLOW SCAN - Mon Nov 02, 03:45 PM ET
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
| 1 | **MSFT** | 509.06 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 48 | none: 158 calls 0-7DTE > 10 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -79% at the target (needs +20%) (68 contracts' greeks worked out here) | POS +$23.8M | 506.53 | 535 | 510 | +$9.1M | +$842k bull / +$0 bear | out (clean 28, ADX 64, RVol 1.6) |
| 2 | **SMH** | 508.20 | FLOW SURGE | **CALLS** | 41 | none: 160 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (62 contracts' greeks worked out here) | NEG -$333.6M | - | 532.5 | 500 | +$10.4M | +$639k bull / +$0 bear | out (clean 33, ADX 51, RVol 0.7) |
| 3 | **MU** | 833.16 | - | **-** | 31 | - | NEG -$244.5M | - | 910 | 850 | +$196.7M | +$5.6M bull / +$0 bear | out (clean 32, ADX 48, RVol 1.6) |
| 4 | **AMD** | 469.15 | - | **-** | 28 | - | NEG -$102.7M | - | 430 | 440 | +$56.4M | +$1.7M bull / +$0 bear | out (clean 33, ADX 58, RVol 1.6) |
| 5 | **SHOP** | 154.49 | - | **-** | 27 | - | NEG -$568k | - | 145 | 160 | +$940k | +$28k bull / +$0 bear | out (clean 31, ADX 39, RVol 1.8) |
| 6 | **QQQ** | 681.35 | - | **-** | 25 | - | NEG -$5.4B | - | 720 | 680 | +$237.7M | +$4.9M bull / +$0 bear | out (clean 32, ADX 51, RVol 1.1) |
| 7 | **NVDA** | 202.06 | - | **-** | 25 | - | NEG -$230.8M | - | 210 | 200 | +$25.1M | +$527k bull / +$0 bear | out (clean 30, ADX 42, RVol 2.0) |
| 8 | **PLTR** | 178.97 | - | **-** | 25 | - | NEG -$13.5M | - | 165 | 180 | +$5.9M | +$451k bull / -$34k bear | out (clean 27, ADX 45, RVol 1.4) |
| 9 | **SPY** | 752.63 | - | **-** | 24 | - | NEG -$10.2B | 774.73 | 800 | 750 | +$219.1M | +$3.4M bull / +$0 bear | out (clean 31, ADX 45, RVol 1.1) |
| 10 | **AMZN** | 246.47 | - | **-** | 24 | - | POS +$49.1M | 242.78 | 250 | 250 | -$14.9M | +$176k bull / +$0 bear | out (clean 34, ADX 45, RVol 1.2) |
| 11 | **DELL** | 395.16 | - | **-** | 24 | - | NEG -$20.2M | - | 430 | 400 | +$3.2M | +$194k bull / +$0 bear | out (clean 35, ADX 47, RVol 0.9) |
| 12 | **AAPL** | 338.31 | - | **-** | 23 | - | POS +$21.7M | 336.7 | 350 | 330 | +$25.8M | +$4.6M bull / -$716k bear | out (clean 32, ADX 24, RVol 1.8) |
| 13 | **MSTR** | 129.92 | - | **-** | 23 | - | NEG -$2.4M | 137.46 | 135 | 125 | +$4.8M | +$98k bull / +$0 bear | out (clean 26, ADX 34, RVol 1.1) |
| 14 | **ORCL** | 118.85 | - | **-** | 22 | - | NEG -$43.1M | - | 130 | 120 | +$1.0M | +$39k bull / -$26k bear | out (clean 32, ADX 34, RVol 3.0) |
| 15 | **TSLA** | 402.04 | - | **-** | 20 | - | POS +$195.7M | - | 400 | 400 | -$19.3M | +$2.4M bull / +$0 bear | out (clean 32, ADX 42, RVol 0.7) |
| 16 | **SMCI** | 30.50 | - | **-** | 20 | - | NEG -$940k | - | 33 | 30 | +$934k | - | out (clean 36, ADX 43, RVol 2.2) |
| 17 | **IWM** | 279.56 | - | **-** | 19 | - | NEG -$1.3B | 286.94 | 285 | 270 | +$7.5M | +$265k bull / +$0 bear | out (clean 33, ADX 30, RVol 0.9) |
| 18 | **AVGO** | 322.96 | - | **-** | 19 | - | NEG -$116.4M | - | 340 | 320 | -$1.0M | +$178k bull / +$0 bear | out (clean 32, ADX 36, RVol 1.0) |
| 19 | **HOOD** | 83.65 | - | **-** | 19 | - | NEG -$11.1M | - | 85 | 90 | +$781k | +$34k bull / +$0 bear | out (clean 32, ADX 31, RVol 0.8) |
| 20 | **META** | 608.78 | - | **-** | 17 | - | NEG -$137.1M | 622.48 | 650 | 610 | +$12.3M | +$797k bull / +$0 bear | out (clean 28, ADX 13, RVol 0.7) |
| 21 | **GOOGL** | 280.81 | - | **-** | 17 | - | NEG -$89.4M | - | 280 | 280 | -$1.5M | +$42k bull / +$0 bear | out (clean 32, ADX 22, RVol 1.1) |
| 22 | **BABA** | 101.71 | - | **-** | 17 | - | POS +$599k | 101.28 | 105 | 100 | -$934k | - | out (clean 33, ADX 44, RVol 1.0) |
| 23 | **ARM** | 197.77 | - | **-** | 15 | - | NEG -$6.3M | - | 200 | 200 | +$276k | - | out (clean 26, ADX 36, RVol 1.8) |
| 24 | **UBER** | 66.48 | - | **-** | 15 | - | NEG -$12.9M | - | 70 | 65 | -$390k | - | out (clean 29, ADX 33, RVol 1.8) |
| 25 | **CRM** | 225.72 | - | **-** | 14 | - | NEG -$10.0M | - | 240 | 220 | +$109k | - | out (clean 28, ADX 39, RVol 1.4) |
| 26 | **COIN** | 136.98 | - | **-** | 11 | - | NEG -$8.3M | - | 150 | 130 | -$208k | - | out (clean 25, ADX 38, RVol 1.4) |
| 27 | **NFLX** | 62.27 | - | **-** | 10 | - | NEG -$22.1M | - | 63 | 60 | -$646k | - | out (clean 28, ADX 27, RVol 1.0) |

## Big prints this scan (101)
- **QQQ** PUT 685 2026-11-06 (4DTE): 398 @ 10.48 = **+$417k** SELL | vol 8,236 / OI 7,773
- **AMD** PUT 490 2026-11-04 (2DTE): 100 @ 32.85 = **+$328k** SELL | vol 1,095 / OI 104
- **AAPL** PUT 325 2026-11-04 (2DTE): 1,000 @ 3.13 = **+$313k** SELL | vol 12,474 / OI 973
- **MU** PUT 850 2026-11-06 (4DTE): 68 @ 34.55 = **+$235k** SELL | vol 4,853 / OI 1,436
- **QQQ** PUT 660 2026-11-06 (4DTE): 597 @ 3.05 = **+$182k** SELL | vol 7,946 / OI 7,945
- **SPY** PUT 754 2026-11-06 (4DTE): 234 @ 6.66 = **+$156k** SELL | vol 13,368 / OI 1,038
- **TSLA** PUT 402.5 2026-11-02 (0DTE): 1,800 @ 0.85 = **+$153k** SELL | vol 165,080 / OI 749
- **TSLA** CALL 405 2026-11-04 (2DTE): 200 @ 7.00 = **+$140k** BUY | vol 10,551 / OI 594
- **MU** CALL 830 2026-11-04 (2DTE): 50 @ 27.58 = **+$138k** BUY | vol 590 / OI 1
- **AMD** PUT 487.5 2026-11-09 (7DTE): 36 @ 34.59 = **+$125k** SELL | vol 104 / OI 0
- **AMD** PUT 487.5 2026-11-06 (4DTE): 36 @ 33.51 = **+$121k** SELL | vol 381 / OI 155
- **AMD** PUT 470 2026-11-04 (2DTE): 50 @ 20.35 = **+$102k** SELL | vol 1,958 / OI 70
- **TSLA** PUT 407.5 2026-11-04 (2DTE): 91 @ 10.50 = **+$96k** SELL | vol 8,004 / OI 106
- **AAPL** PUT 340 2026-11-04 (2DTE): 116 @ 7.95 = **+$92k** SELL | vol 12,714 / OI 2,460
- **MU** CALL 850 2026-11-04 (2DTE): 50 @ 17.28 = **+$86k** BUY | vol 2,175 / OI 41

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 718 2026-11-13 (11DTE): 581 traded vs OI 340
- **SPY** PUT 754 2026-11-13 (11DTE): 1,645 traded vs OI 1,476
- **QQQ** PUT 640 2026-11-05 (3DTE): 519 traded vs OI 0
- **QQQ** CALL 730 2026-11-06 (4DTE): 4,995 traded vs OI 4,808
- **QQQ** PUT 630 2026-11-09 (7DTE): 906 traded vs OI 890
- **QQQ** PUT 660 2026-11-06 (4DTE): 7,946 traded vs OI 7,945
- **QQQ** CALL 701 2026-11-20 (18DTE): 658 traded vs OI 657
- **IWM** PUT 257.5 2026-11-03 (1DTE): 779 traded vs OI 35
- **IWM** PUT 273 2026-11-03 (1DTE): 1,157 traded vs OI 960
- **IWM** CALL 291 2026-11-13 (11DTE): 529 traded vs OI 245
- **SMH** PUT 475 2026-11-04 (2DTE): 1,029 traded vs OI 7
- **NVDA** PUT 190 2026-11-13 (11DTE): 5,384 traded vs OI 5,319
- **AAPL** PUT 360 2026-11-09 (7DTE): 511 traded vs OI 3
- **META** PUT 607.5 2026-11-04 (2DTE): 500 traded vs OI 84
- **AMZN** PUT 250 2026-11-09 (7DTE): 1,332 traded vs OI 1,303

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
