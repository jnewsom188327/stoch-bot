# GEX + FLOW SCAN - Wed Oct 28, 02:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 14:35 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/28 730C | 0.67 | 0.72 | +64% (2m) | **+7%** | -70% | 724.9 hit |
| 14:35 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R2 R5 R6) | 10/29 778C | 0.75 | 0.80 | +43% (2m) | **+7%** | +27% | 772.74 hit |
| 12:56 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/28 730C | 0.63 | 0.67 | +24% (10m) | **+6%** (done) | -35% | 723.9 |
| 12:56 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/29 779C | 0.63 | 0.51 | +3% (9m) | **-19%** (done) | +10% | 772.67 |
| 11:40 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 96C | 0.77 | 0.55 | -1% (3m) | **-29%** (done) | +49% | 93.02 |
| 11:05 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 97C | 0.63 | 0.45 | +19% (1m) | **-29%** (done) | +53% | 93.44 |
| 10:50 | **IWM** | **CALLS** | FLOW SURGE | 10/30 284C | 0.57 | 0.54 | +7% (2m) | **-5%** (done) | +22% | 280.64 |
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.34 | +11% (0m) | **-28%** (done) | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 14:34 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | WITH you | **FIRE** QQQ261028C00730000 |
| 14:34 | SPY | 1m WHIPSAW | R1 R2 R5 R6 | CALLS | WITH you | **FIRE** SPY261029C00778000 |
| 12:55 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | WITH you | **FIRE** QQQ261028C00730000 |
| 12:55 | SPY | 1m WHIPSAW | R1 R2 | CALLS | WITH you | **FIRE** SPY261029C00779000 |

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **ORCL** | 145.90 | FLOW SURGE | **PUTS** | 53 | none: 23 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$29.9M | - | 135 | 140 | -$17.4M | +$0 bull / -$4.8M bear | out (clean 30, ADX 42, RVol 12.1) |
| 2 | **AAPL** | 344.69 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 36 | 10/28 345C @ 0.52 (delta 0.43) = est -77% at 345 | POS +$305.8M | 341.85 | 350 | 345 | +$2.2M | +$109k bull / -$234k bear | out (clean 28, ADX 13, RVol 1.0) |
| 3 | **AVGO** | 350.55 | PINNED between the walls (positive gamma) - chop | **-** | 35 | - | POS +$66.2M | 338.05 | 350 | 350 | -$414k | +$0 bull / -$160k bear | out (clean 29, ADX 35, RVol 1.2) |
| 4 | **SMH** | 568.16 | - | **-** | 25 | - | POS +$115.2M | 557.56 | 570 | 555 | -$4.5M | +$0 bull / -$348k bear | out (clean 28, ADX 22, RVol 1.3) |
| 5 | **IWM** | 280.73 | - | **-** | 22 | - | NEG -$25.8M | 280.95 | 280 | 270 | +$8.5M | +$0 bull / -$2.3M bear | out (clean 24, ADX 30, RVol 1.1) |
| 6 | **SPY** | 772.30 | - | **-** | 19 | - | NEG -$838.1M | 773.33 | 780 | 750 | -$31.3M | +$0 bull / -$728k bear | out (clean 29, ADX 20, RVol 1.9) |
| 7 | **AMD** | 576.76 | - | **-** | 19 | - | POS +$180.6M | - | 600 | 550 | +$212k | +$0 bull / -$1.4M bear | out (clean 29, ADX 37, RVol 1.4) |
| 8 | **MSFT** | 529.12 | - | **-** | 19 | - | POS +$477.1M | - | 550 | 500 | -$2.5M | +$0 bull / -$2.5M bear | out (clean 29, ADX 20, RVol 1.8) |
| 9 | **GOOGL** | 324.70 | - | **-** | 19 | - | POS +$21.9M | 320.35 | 355 | 330 | -$2.3M | +$0 bull / -$1.1M bear | out (clean 32, ADX 21, RVol 1.7) |
| 10 | **MSTR** | 141.05 | - | **-** | 19 | - | POS +$19.9M | - | 152.5 | 150 | +$609k | +$0 bull / -$30k bear | out (clean 27, ADX 23, RVol 1.4) |
| 11 | **NVDA** | 216.51 | - | **-** | 18 | - | POS +$476.6M | 210.15 | 220 | 215 | +$11.6M | +$193k bull / -$204k bear | out (clean 26, ADX 16, RVol 0.9) |
| 12 | **TSLA** | 403.91 | - | **-** | 18 | - | POS +$645.0M | - | 400 | 400 | -$19.8M | +$0 bull / -$1.4M bear | out (clean 29, ADX 24, RVol 0.7) |
| 13 | **META** | 612.80 | - | **-** | 18 | - | NEG -$265.4M | 634.31 | 650 | 610 | +$6.3M | +$0 bull / -$1.8M bear | out (clean 29, ADX 24, RVol 1.1) |
| 14 | **PLTR** | 194.18 | - | **-** | 17 | - | POS +$42.3M | 189.68 | 200 | 190 | +$123k | +$0 bull / -$158k bear | out (clean 27, ADX 31, RVol 0.8) |
| 15 | **MU** | 981.00 | - | **-** | 17 | - | POS +$617.2M | - | 1,000 | 950 | +$8.1M | +$0 bull / -$3.0M bear | out (clean 28, ADX 22, RVol 1.0) |
| 16 | **ARM** | 234.67 | - | **-** | 17 | - | POS +$2.5M | - | 250 | 250 | -$56k | +$0 bull / -$681k bear | out (clean 26, ADX 21, RVol 1.4) |
| 17 | **QQQ** | 724.38 | - | **-** | 16 | - | NEG -$751.0M | 727.33 | 720 | 720 | +$6.8M | +$0 bull / -$604k bear | out (clean 29, ADX 21, RVol 1.1) |
| 18 | **AMZN** | 253.56 | - | **-** | 16 | - | POS +$191.0M | - | 255 | 250 | +$872k | +$0 bull / -$390k bear | out (clean 31, ADX 22, RVol 1.1) |
| 19 | **BABA** | 100.43 | - | **-** | 16 | - | NEG -$12.0M | 103.35 | 102 | 100 | -$2k | +$0 bull / -$48k bear | out (clean 29, ADX 24, RVol 0.9) |
| 20 | **HOOD** | 91.59 | - | **-** | 12 | - | NEG -$17.4M | - | 100 | 90 | +$4.1M | - | out (clean 30, ADX 18, RVol 0.9) |
| 21 | **SHOP** | 167.49 | - | **-** | 11 | - | NEG -$3.3M | 171.33 | 175 | 165 | -$27k | - | out (clean 28, ADX 21, RVol 1.2) |
| 22 | **SMCI** | 35.23 | - | **-** | 10 | - | POS +$21.1M | - | 35 | 35 | +$98k | - | out (clean 28, ADX 29, RVol 1.0) |
| 23 | **COIN** | 159.87 | - | **-** | 6 | - | POS +$2.5M | 154.76 | 170 | 150 | +$16k | - | out (clean 28, ADX 16, RVol 1.2) |
| 24 | **UBER** | 65.39 | - | **-** | 6 | - | NEG -$31.9M | - | 70 | 65 | +$41k | - | out (clean 30, ADX 19, RVol 0.7) |
| 25 | **NFLX** | 61.72 | - | **-** | 5 | - | NEG -$59.0M | - | 65 | 60 | -$106k | - | out (clean 31, ADX 15, RVol 0.7) |
| 26 | **DELL** | 497.65 | - | **-** | 5 | - | POS +$33.3M | - | 500 | 500 | -$13k | - | out (clean 31, ADX 19, RVol 0.9) |
| 27 | **CRM** | 240.85 | - | **-** | 4 | - | POS +$4.9M | 235.97 | 260 | 240 | +$20k | - | out (clean 26, ADX 14, RVol 0.4) |

## Big prints this scan (167)
- **MSFT** CALL 527.5 2026-10-30 (2DTE): 305 @ 13.67 = **+$417k** SELL | vol 2,114 / OI 454
- **SPY** CALL 770 2026-10-30 (2DTE): 400 @ 5.20 = **+$208k** SELL | vol 9,622 / OI 22,207
- **MSFT** PUT 517.5 2026-10-30 (2DTE): 245 @ 8.15 = **+$200k** BUY | vol 1,982 / OI 585
- **MSFT** CALL 550 2026-10-30 (2DTE): 399 @ 4.91 = **+$196k** SELL | vol 5,323 / OI 7,100
- **MSFT** PUT 505 2026-10-30 (2DTE): 399 @ 4.43 = **+$177k** BUY | vol 1,872 / OI 1,059
- **AMD** CALL 570 2026-10-28 (0DTE): 400 @ 4.40 = **+$176k** SELL | vol 24,975 / OI 956
- **AMD** CALL 565 2026-10-28 (0DTE): 200 @ 7.80 = **+$156k** SELL | vol 10,158 / OI 610
- **QQQ** PUT 722 2026-11-02 (5DTE): 200 @ 7.25 = **+$145k** BUY | vol 1,925 / OI 87
- **SPY** PUT 770 2026-10-28 (0DTE): 731 @ 1.94 = **+$142k** BUY | vol 297,088 / OI 1,789
- **SMH** CALL 567.5 2026-10-30 (2DTE): 188 @ 7.40 = **+$139k** SELL | vol 987 / OI 410
- **QQQ** CALL 707 2026-11-02 (5DTE): 68 @ 19.18 = **+$130k** SELL | vol 88 / OI 53
- **SMH** CALL 567.5 2026-10-30 (2DTE): 169 @ 7.40 = **+$125k** SELL | vol 987 / OI 410
- **MSFT** CALL 550 2026-10-30 (2DTE): 245 @ 4.93 = **+$121k** SELL | vol 5,323 / OI 7,100
- **MU** CALL 975 2026-10-28 (0DTE): 242 @ 4.75 = **+$115k** SELL | vol 56,968 / OI 683
- **QQQ** PUT 725 2026-10-29 (1DTE): 200 @ 5.49 = **+$110k** BUY | vol 3,162 / OI 643

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 755 2026-11-02 (5DTE): 1,291 traded vs OI 1,251
- **SPY** CALL 778 2026-11-02 (5DTE): 514 traded vs OI 282
- **SPY** CALL 773 2026-11-03 (6DTE): 512 traded vs OI 252
- **SPY** PUT 755 2026-11-11 (14DTE): 549 traded vs OI 0
- **QQQ** PUT 719 2026-10-30 (2DTE): 1,151 traded vs OI 1,088
- **QQQ** PUT 700 2026-11-03 (6DTE): 1,019 traded vs OI 720
- **IWM** PUT 279 2026-10-30 (2DTE): 2,283 traded vs OI 2,134
- **IWM** CALL 281 2026-11-02 (5DTE): 703 traded vs OI 692
- **IWM** CALL 290 2026-11-05 (8DTE): 550 traded vs OI 68
- **IWM** CALL 279 2026-10-29 (1DTE): 1,174 traded vs OI 1,142
- **SMH** CALL 587.5 2026-10-30 (2DTE): 855 traded vs OI 841
- **NVDA** PUT 207.5 2026-10-28 (0DTE): 3,685 traded vs OI 3,342
- **NVDA** CALL 210 2026-11-04 (7DTE): 504 traded vs OI 222
- **NVDA** PUT 202.5 2026-10-30 (2DTE): 2,660 traded vs OI 2,488
- **TSLA** PUT 397.5 2026-11-06 (9DTE): 517 traded vs OI 113

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
