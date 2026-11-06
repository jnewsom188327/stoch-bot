# GEX + FLOW SCAN - Fri Nov 06, 02:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:40 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/06 742C | 0.42 | 0.26 | +14% (6m) | **-38%** (done) | +42% | 739.03 |
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.28 | +12% (20m) | **-62%** (done) | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.03 | -6% (1m) | **-96%** (done) | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.36 | +32% (4m) | **-10%** (done) | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (11 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:00:08 ET, last candle SPY 13:59, QQQ 13:59 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 13:17 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 13:16 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 13:11 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 39 puts 0-1DTE > 4 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 13:11 | SPY | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 44 puts 0-1DTE > 4 priced 0.40-0.80 > 3 delta 0.15+ > 3 spread ok > 3 liquid  |
| 13:00 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 40 puts 0-1DTE > 4 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 13:00 | SPY | 1m FAILED POP | R3 | PUTS | TURNING away | no contract: 44 puts 0-1DTE > 4 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 12:39 | SPY | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** SPY261106C00742000 |
| 12:38 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:38 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:37 | QQQ | 1m WHIPSAW | R1 R2 | PUTS | WITH you | no contract: 39 puts 0-1DTE > 5 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 344.71 | FLIP CROSS down into negative gamma | **PUTS** | 28 | none: 108 puts 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (62 contracts' greeks worked out here) | NEG -$15.9M | 344.84 | 345 | 345 | -$17.6M | +$32k bull / -$53k bear | out (clean 28, ADX 8, RVol 0.3) |
| 2 | **MSFT** | 534.02 | PINNED between the walls (positive gamma) - chop | **-** | 27 | - | POS +$681.6M | 513.28 | 535 | 535 | +$2.5M | +$0 bull / -$950k bear | out (clean 34, ADX 15, RVol 0.5) |
| 3 | **ORCL** | 115.59 | - | **-** | 22 | - | NEG -$84.3M | - | 116 | 115 | -$5.5M | +$0 bull / -$32k bear | out (clean 30, ADX 20, RVol 0.3) |
| 4 | **COIN** | 134.10 | - | **-** | 21 | - | NEG -$24.2M | 137.16 | 142 | 135 | -$3.3M | +$0 bull / -$102k bear | out (clean 32, ADX 21, RVol 0.4) |
| 5 | **DELL** | 329.91 | - | **-** | 20 | - | NEG -$29.8M | - | 335 | 335 | +$5.7M | +$206k bull / +$0 bear | out (clean 30, ADX 16, RVol 0.3) |
| 6 | **MSTR** | 128.14 | - | **-** | 19 | - | NEG -$9.7M | 128.79 | 135 | 125 | -$6.7M | +$319k bull / -$46k bear | out (clean 30, ADX 19, RVol 0.4) |
| 7 | **TSLA** | 359.55 | - | **-** | 18 | - | NEG -$334.6M | - | 360 | 360 | -$54.7M | +$2.8M bull / -$173k bear | out (clean 35, ADX 21, RVol 0.2) |
| 8 | **ARM** | 173.81 | - | **-** | 18 | - | NEG -$27.4M | - | 190 | 170 | -$765k | +$0 bull / -$60k bear | out (clean 26, ADX 15, RVol 0.2) |
| 9 | **SMH** | 464.30 | - | **-** | 17 | - | NEG -$619.2M | - | 505 | 465 | +$6.3M | +$0 bull / -$252k bear | out (clean 32, ADX 16, RVol 0.5) |
| 10 | **AVGO** | 292.87 | - | **-** | 17 | - | NEG -$131.7M | - | 320 | 300 | +$1.6M | +$0 bull / -$454k bear | out (clean 31, ADX 20, RVol 1.3) |
| 11 | **QQQ** | 659.20 | - | **-** | 16 | - | NEG -$6.1B | - | 700 | 680 | +$40.1M | +$341k bull / -$1.5M bear | out (clean 34, ADX 17, RVol 1.2) |
| 12 | **IWM** | 274.23 | - | **-** | 16 | - | NEG -$3.4B | 285.52 | 275 | 275 | -$5.7M | +$0 bull / -$87k bear | out (clean 33, ADX 18, RVol 0.3) |
| 13 | **META** | 618.06 | - | **-** | 16 | - | NEG -$116.8M | 623.24 | 620 | 610 | -$7.1M | +$155k bull / -$40k bear | out (clean 33, ADX 19, RVol 0.2) |
| 14 | **MU** | 692.28 | - | **-** | 16 | - | NEG -$205.5M | - | 700 | 700 | +$71.7M | +$168k bull / -$4.3M bear | out (clean 32, ADX 12, RVol 0.5) |
| 15 | **BABA** | 109.10 | - | **-** | 16 | - | POS +$35.7M | - | 110 | 110 | -$439k | +$98k bull / -$27k bear | out (clean 34, ADX 13, RVol 0.3) |
| 16 | **SPY** | 738.80 | - | **-** | 15 | - | NEG -$15.8B | 768.8 | 760 | 740 | -$42.7M | +$205k bull / -$3.4M bear | out (clean 34, ADX 18, RVol 0.7) |
| 17 | **NVDA** | 187.56 | - | **-** | 15 | - | NEG -$422.2M | - | 200 | 190 | +$23.1M | +$0 bull / -$5.4M bear | out (clean 33, ADX 14, RVol 0.4) |
| 18 | **AMD** | 445.65 | - | **-** | 15 | - | NEG -$182.7M | - | 430 | 450 | +$6.7M | +$26k bull / -$574k bear | out (clean 31, ADX 17, RVol 0.7) |
| 19 | **AMZN** | 262.62 | - | **-** | 15 | - | POS +$354.1M | - | 265 | 260 | -$1.9M | +$155k bull / +$0 bear | out (clean 35, ADX 19, RVol 0.3) |
| 20 | **HOOD** | 79.80 | - | **-** | 15 | - | NEG -$29.1M | 83.07 | 85 | 80 | +$2.0M | +$452k bull / -$59k bear | out (clean 30, ADX 18, RVol 0.3) |
| 21 | **SHOP** | 149.34 | - | **-** | 15 | - | NEG -$3.5M | 150.95 | 150 | 150 | -$1.1M | - | out (clean 36, ADX 18, RVol 0.6) |
| 22 | **GOOGL** | 286.06 | - | **-** | 14 | - | POS +$94.5M | 283.03 | 285 | 285 | +$1.5M | +$0 bull / -$265k bear | out (clean 33, ADX 14, RVol 0.4) |
| 23 | **UBER** | 69.13 | - | **-** | 11 | - | POS +$10.0M | 68.51 | 70 | 70 | +$266k | - | out (clean 30, ADX 29, RVol 0.2) |
| 24 | **CRM** | 214.46 | - | **-** | 8 | - | NEG -$22.0M | - | 230 | 215 | -$208k | - | out (clean 34, ADX 22, RVol 1.0) |
| 25 | **NFLX** | 63.83 | - | **-** | 6 | - | POS +$21.6M | 63.38 | 64 | 64 | -$400k | - | out (clean 32, ADX 14, RVol 0.4) |
| 26 | **PLTR** | 160.51 | - | **-** | 6 | - | NEG -$86.6M | - | 165 | 160 | +$3.6M | - | out (clean 27, ADX 11, RVol 0.4) |
| 27 | **SMCI** | 28.34 | - | **-** | 6 | - | NEG -$4.2M | 29.55 | 30 | 28 | -$431k | - | out (clean 33, ADX 16, RVol 0.3) |

## Big prints this scan (40)
- **MSFT** CALL 530 2026-11-06 (0DTE): 1,000 @ 3.80 = **+$380k** SELL | vol 4,035 / OI 5,634
- **HOOD** CALL 82 2026-11-13 (7DTE): 1,106 @ 2.32 = **+$257k** MID | vol 9,128 / OI 386
- **MU** CALL 670 2026-11-06 (0DTE): 100 @ 19.45 = **+$194k** SELL | vol 3,028 / OI 0
- **MU** CALL 670 2026-11-06 (0DTE): 100 @ 18.90 = **+$189k** SELL | vol 3,028 / OI 0
- **MU** CALL 670 2026-11-06 (0DTE): 100 @ 18.00 = **+$180k** SELL | vol 3,028 / OI 0
- **HOOD** CALL 82 2026-11-13 (7DTE): 694 @ 2.33 = **+$162k** MID | vol 9,128 / OI 386
- **QQQ** PUT 660 2026-11-09 (3DTE): 200 @ 7.60 = **+$152k** BUY | vol 22,210 / OI 1,084
- **QQQ** PUT 660 2026-11-09 (3DTE): 171 @ 7.70 = **+$132k** BUY | vol 22,210 / OI 1,084
- **MU** CALL 670 2026-11-06 (0DTE): 65 @ 18.40 = **+$120k** SELL | vol 3,028 / OI 0
- **QQQ** CALL 657 2026-11-06 (0DTE): 500 @ 2.27 = **+$114k** SELL | vol 57,003 / OI 9
- **MU** CALL 695 2026-11-09 (3DTE): 67 @ 16.67 = **+$112k** SELL | vol 1,467 / OI 0
- **QQQ** CALL 631 2026-11-13 (7DTE): 33 @ 32.27 = **+$106k** SELL | vol 46 / OI 0
- **MU** CALL 702.5 2026-11-09 (3DTE): 67 @ 13.47 = **+$90k** SELL | vol 929 / OI 0
- **BABA** CALL 106 2026-11-06 (0DTE): 222 @ 3.30 = **+$73k** MID | vol 855 / OI 2,401
- **ARM** PUT 175 2026-11-06 (0DTE): 199 @ 3.00 = **+$60k** BUY | vol 532 / OI 1,116

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 772 2026-11-11 (5DTE): 922 traded vs OI 311
- **SPY** CALL 810 2026-11-17 (11DTE): 1,323 traded vs OI 0
- **SPY** PUT 706 2026-11-30 (24DTE): 1,132 traded vs OI 706
- **QQQ** PUT 625 2026-11-11 (5DTE): 512 traded vs OI 95
- **QQQ** CALL 725 2026-11-11 (5DTE): 561 traded vs OI 0
- **QQQ** CALL 685 2026-11-11 (5DTE): 501 traded vs OI 183
- **QQQ** CALL 676 2026-11-13 (7DTE): 513 traded vs OI 141
- **SMH** CALL 510 2026-11-13 (7DTE): 524 traded vs OI 79
- **SMH** CALL 462.5 2026-11-06 (0DTE): 504 traded vs OI 0
- **NVDA** CALL 172.5 2026-11-11 (5DTE): 520 traded vs OI 0
- **TSLA** CALL 382.5 2026-11-13 (7DTE): 524 traded vs OI 365
- **AMD** CALL 490 2026-11-13 (7DTE): 578 traded vs OI 0
- **AMD** CALL 490 2026-11-20 (14DTE): 588 traded vs OI 0
- **META** CALL 647.5 2026-11-06 (0DTE): 811 traded vs OI 810
- **META** CALL 652.5 2026-11-09 (3DTE): 507 traded vs OI 58

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
