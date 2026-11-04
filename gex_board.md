# GEX + FLOW SCAN - Wed Nov 04, 12:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:38 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/04 686P | 0.80 | 0.10 | -1% (0m) | **-88%** | +26% | 689.6 |
| 11:21 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/04 685P | 0.67 | 0.12 | +66% (7m) | **-82%** (done) | +25% | 690.3 hit |
| 10:20 | **SMCI** | **CALLS** | FLOW SURGE | 11/06 33C | 0.65 | 0.13 | -3% (1m) | **-80%** (done) | +39% | 32.81 |
| 10:20 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 284C | 0.49 | 0.17 | +2% (22m) | **-65%** (done) | +131% | 284.74 |
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 1.54 | +169% (60m) | **+126%** (done) | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.56 | +168% (52m) | **+160%** (done) | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.06 | +2% (1m) | **-89%** (done) | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.10 | -3% (1m) | **-84%** (done) | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:30:08 ET, last candle SPY 12:29, QQQ 12:29 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:37 | QQQ | 1m FAILED POP | R3 | PUTS | TURNING away | **FIRE** QQQ261104P00686000 |
| 11:20 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** QQQ261104P00685000 |

## Flow surges NOT fired - price disagreed (36 today, last 5)
- 11:50 SMCI CALLS: under EMA 20 - flow says one way, price says the other
- 11:45 SMCI CALLS: under EMA 20 - flow says one way, price says the other
- 11:40 SMCI CALLS: under EMA 20 - flow says one way, price says the other
- 11:35 SMCI CALLS: price -0.19 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:30 SMCI CALLS: price -0.20 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 352.83 | - | **-** | 31 | - | POS +$1.0B | 341.65 | 355 | 350 | -$81.2M | +$1.4M bull / -$253k bear | out (clean 32, ADX 48, RVol 0.9) |
| 2 | **BABA** | 107.12 | TREND (flow not with it) | **CALLS** | 31 | none: 21 calls 0-7DTE > 2 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +15% at the target (needs +20%) | POS +$16.3M | - | 110 | 110 | -$848k | - | LONG (clean 36, ADX 39, RVol 0.7) |
| 3 | **SMH** | 508.89 | - | **-** | 27 | - | NEG -$527.7M | - | 532.5 | 500 | +$20.4M | +$0 bull / -$506k bear | out (clean 32, ADX 23, RVol 0.8) |
| 4 | **UBER** | 71.41 | - | **-** | 27 | - | POS +$12.6M | 68.32 | 70 | 70 | -$1.1M | +$118k bull / +$0 bear | out (clean 30, ADX 38, RVol 1.0) |
| 5 | **NFLX** | 65.95 | - | **-** | 26 | - | POS +$20.8M | 62.34 | 65 | 65 | -$2.0M | +$31k bull / +$0 bear | out (clean 31, ADX 43, RVol 0.7) |
| 6 | **MSFT** | 555.90 | - | **-** | 25 | - | POS +$1.0B | - | 550 | 535 | -$18.1M | +$518k bull / -$126k bear | out (clean 29, ADX 58, RVol 1.1) |
| 7 | **GOOGL** | 291.43 | - | **-** | 25 | - | POS +$97.9M | 283.04 | 290 | 290 | -$27.2M | +$0 bull / -$40k bear | out (clean 36, ADX 24, RVol 0.4) |
| 8 | **AMZN** | 267.93 | - | **-** | 22 | - | POS +$563.0M | - | 270 | 250 | -$18.7M | +$0 bull / -$269k bear | out (clean 35, ADX 33, RVol 0.7) |
| 9 | **SMCI** | 30.45 | - | **-** | 22 | - | NEG -$506k | 31.98 | 33 | 30 | +$1.9M | - | out (clean 34, ADX 41, RVol 1.4) |
| 10 | **MU** | 810.63 | - | **-** | 22 | - | NEG -$365.9M | - | 850 | 800 | +$95.8M | +$877k bull / -$821k bear | out (clean 32, ADX 28, RVol 0.6) |
| 11 | **COIN** | 151.85 | - | **-** | 21 | - | POS +$29.0M | - | 148 | 150 | -$1.3M | +$0 bull / -$28k bear | out (clean 31, ADX 16, RVol 0.3) |
| 12 | **TSLA** | 387.66 | - | **-** | 20 | - | NEG -$97.5M | 394.05 | 400 | 380 | -$72.7M | +$0 bull / -$689k bear | out (clean 30, ADX 17, RVol 0.6) |
| 13 | **SPY** | 768.42 | - | **-** | 19 | - | NEG -$2.0B | 770.09 | 770 | 750 | -$113.8M | +$0 bull / -$554k bear | out (clean 32, ADX 26, RVol 0.7) |
| 14 | **IWM** | 284.37 | - | **-** | 19 | - | NEG -$115.2M | 284.7 | 285 | 270 | +$8.9M | +$0 bull / -$1.3M bear | out (clean 34, ADX 19, RVol 1.2) |
| 15 | **AMD** | 488.59 | - | **-** | 19 | - | NEG -$90.6M | - | 500 | 500 | +$41.8M | +$616k bull / -$199k bear | out (clean 32, ADX 11, RVol 0.6) |
| 16 | **QQQ** | 696.35 | - | **-** | 17 | - | NEG -$4.6B | 720.15 | 700 | 680 | -$144.0M | +$289k bull / -$904k bear | out (clean 31, ADX 14, RVol 0.5) |
| 17 | **NVDA** | 203.49 | - | **-** | 17 | - | NEG -$41.8M | 203.94 | 210 | 200 | -$525k | +$347k bull / -$90k bear | out (clean 30, ADX 28, RVol 0.8) |
| 18 | **MSTR** | 144.59 | - | **-** | 17 | - | POS +$124.4M | - | 135 | 150 | +$329k | +$102k bull / -$195k bear | out (clean 31, ADX 33, RVol 0.5) |
| 19 | **META** | 637.77 | - | **-** | 16 | - | POS +$234.2M | 620.74 | 650 | 625 | -$1.2M | +$96k bull / -$177k bear | out (clean 30, ADX 24, RVol 0.9) |
| 20 | **HOOD** | 87.96 | - | **-** | 16 | - | POS +$3.0M | 84.54 | 90 | 90 | -$1.1M | +$0 bull / -$27k bear | out (clean 28, ADX 16, RVol 0.6) |
| 21 | **SHOP** | 151.75 | - | **-** | 13 | - | NEG -$5.8M | - | 160 | 150 | -$357k | - | out (clean 34, ADX 27, RVol 0.4) |
| 22 | **CRM** | 225.22 | - | **-** | 10 | - | NEG -$13.5M | - | 240 | 220 | -$96k | - | out (clean 33, ADX 35, RVol 0.7) |
| 23 | **DELL** | 375.09 | - | **-** | 9 | - | NEG -$30.7M | - | 400 | 400 | +$1.1M | - | out (clean 33, ADX 28, RVol 0.8) |
| 24 | **ORCL** | 126.90 | - | **-** | 9 | - | NEG -$29.9M | - | 130 | 125 | +$2.2M | - | out (clean 34, ADX 12, RVol 1.4) |
| 25 | **ARM** | 196.96 | - | **-** | 8 | - | NEG -$7.2M | - | 212.5 | 200 | +$312k | - | out (clean 26, ADX 26, RVol 0.6) |
| 26 | **AVGO** | 328.39 | - | **-** | 7 | - | NEG -$91.7M | - | 340 | 330 | +$1.6M | - | out (clean 30, ADX 21, RVol 0.8) |
| 27 | **PLTR** | 170.73 | - | **-** | 7 | - | NEG -$50.5M | - | 165 | 170 | -$1.5M | - | out (clean 26, ADX 24, RVol 0.6) |

## Big prints this scan (61)
- **AAPL** CALL 360 2026-11-06 (2DTE): 7,330 @ 1.31 = **+$960k** BUY | vol 30,103 / OI 14,715
- **QQQ** PUT 695 2026-11-05 (1DTE): 443 @ 5.15 = **+$228k** BUY | vol 17,311 / OI 1,805
- **IWM** PUT 285 2026-11-04 (0DTE): 1,499 @ 1.51 = **+$226k** BUY | vol 22,093 / OI 131
- **SPY** CALL 770 2026-11-10 (6DTE): 381 @ 4.28 = **+$163k** SELL | vol 5,767 / OI 3,826
- **IWM** PUT 283 2026-11-05 (1DTE): 1,394 @ 1.12 = **+$156k** BUY | vol 7,525 / OI 111
- **MSFT** PUT 557.5 2026-11-04 (0DTE): 400 @ 3.15 = **+$126k** BUY | vol 2,793 / OI 0
- **SPY** CALL 770 2026-11-10 (6DTE): 268 @ 4.28 = **+$115k** SELL | vol 5,767 / OI 3,826
- **QQQ** PUT 693 2026-11-04 (0DTE): 888 @ 1.29 = **+$115k** BUY | vol 112,428 / OI 528
- **META** CALL 640 2026-11-04 (0DTE): 468 @ 2.06 = **+$96k** BUY | vol 35,203 / OI 670
- **MU** CALL 800 2026-11-06 (2DTE): 42 @ 22.57 = **+$95k** SELL | vol 2,757 / OI 342
- **UBER** CALL 69 2026-11-06 (2DTE): 289 @ 2.79 = **+$81k** BUY | vol 2,597 / OI 2,552
- **AMZN** CALL 260 2026-11-09 (5DTE): 89 @ 8.85 = **+$79k** SELL | vol 966 / OI 1,007
- **AMZN** CALL 260 2026-11-09 (5DTE): 85 @ 9.00 = **+$76k** SELL | vol 966 / OI 1,007
- **IWM** PUT 284 2026-11-04 (0DTE): 890 @ 0.85 = **+$76k** BUY | vol 36,862 / OI 236
- **MSTR** PUT 144 2026-11-06 (2DTE): 157 @ 4.35 = **+$68k** BUY | vol 2,119 / OI 190

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 770 2026-11-10 (6DTE): 5,767 traded vs OI 3,826
- **SPY** CALL 774 2026-11-10 (6DTE): 687 traded vs OI 0
- **SPY** CALL 783 2026-11-09 (5DTE): 505 traded vs OI 0
- **SPY** CALL 780 2026-11-10 (6DTE): 1,390 traded vs OI 1,370
- **QQQ** CALL 699 2026-11-13 (9DTE): 521 traded vs OI 278
- **IWM** CALL 295 2026-11-05 (1DTE): 515 traded vs OI 180
- **AAPL** PUT 357.5 2026-11-04 (0DTE): 1,048 traded vs OI 954
- **AAPL** PUT 327.5 2026-11-13 (9DTE): 584 traded vs OI 113
- **AAPL** PUT 330 2026-11-13 (9DTE): 1,638 traded vs OI 1,549
- **AAPL** CALL 370 2026-12-04 (30DTE): 937 traded vs OI 913
- **META** PUT 637.5 2026-11-06 (2DTE): 508 traded vs OI 31
- **META** CALL 640 2026-11-06 (2DTE): 6,853 traded vs OI 6,825
- **META** CALL 637.5 2026-11-06 (2DTE): 896 traded vs OI 883
- **MSFT** PUT 555 2026-11-20 (16DTE): 502 traded vs OI 235
- **MSFT** CALL 587.5 2026-11-06 (2DTE): 533 traded vs OI 159

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
