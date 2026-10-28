# GEX + FLOW SCAN - Wed Oct 28, 03:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 14:35 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/28 730C | 0.67 | 0.46 | +64% (2m) | **-31%** | -70% | 724.9 hit |
| 14:35 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R2 R5 R6) | 10/29 778C | 0.75 | 0.58 | +43% (2m) | **-23%** | +27% | 772.74 hit |
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
| 1 | **ORCL** | 147.75 | FLOW SURGE | **PUTS** | 55 | none: 23 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$26.5M | - | 135 | 140 | -$29.4M | +$0 bull / -$5.1M bear | out (clean 30, ADX 49, RVol 8.6) |
| 2 | **AVGO** | 350.52 | PINNED between the walls (positive gamma) - chop | **-** | 36 | - | POS +$62.9M | 340.23 | 350 | 350 | +$551k | +$364k bull / -$50k bear | out (clean 29, ADX 36, RVol 1.4) |
| 3 | **AAPL** | 344.43 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 35 | 10/30 350C @ 0.76 (delta 0.20) = est +5% at 345 | POS +$266.0M | 341.61 | 350 | 345 | +$2.8M | +$260k bull / -$30k bear | out (clean 29, ADX 13, RVol 0.8) |
| 4 | **SMH** | 567.43 | - | **-** | 24 | - | POS +$82.6M | 560.48 | 570 | 555 | -$3.8M | +$26k bull / -$314k bear | out (clean 28, ADX 24, RVol 1.5) |
| 5 | **IWM** | 279.84 | - | **-** | 23 | - | NEG -$484.7M | 280.81 | 280 | 270 | +$11.4M | +$62k bull / -$239k bear | out (clean 24, ADX 27, RVol 1.3) |
| 6 | **HOOD** | 91.17 | - | **-** | 22 | - | NEG -$16.9M | - | 100 | 90 | +$4.5M | +$29k bull / +$0 bear | out (clean 30, ADX 17, RVol 1.0) |
| 7 | **AMD** | 576.49 | - | **-** | 21 | - | POS +$171.4M | - | 600 | 550 | +$2.6M | +$1.4M bull / -$1.3M bear | out (clean 29, ADX 40, RVol 1.5) |
| 8 | **MSTR** | 140.81 | - | **-** | 20 | - | POS +$19.2M | - | 152.5 | 140 | +$1.1M | +$45k bull / +$0 bear | out (clean 27, ADX 25, RVol 1.4) |
| 9 | **NVDA** | 216.17 | - | **-** | 19 | - | POS +$443.2M | 210.54 | 220 | 215 | +$14.0M | +$646k bull / -$175k bear | out (clean 26, ADX 18, RVol 1.2) |
| 10 | **MSFT** | 529.56 | - | **-** | 19 | - | POS +$480.2M | - | 550 | 500 | -$2.2M | +$364k bull / -$1.3M bear | out (clean 29, ADX 23, RVol 1.7) |
| 11 | **GOOGL** | 325.06 | - | **-** | 19 | - | POS +$22.8M | 320.13 | 355 | 330 | -$2.2M | +$475k bull / -$1.0M bear | out (clean 32, ADX 22, RVol 1.6) |
| 12 | **SPY** | 771.24 | - | **-** | 18 | - | NEG -$2.0B | 773.08 | 780 | 765 | -$10.0M | +$903k bull / -$451k bear | out (clean 28, ADX 22, RVol 2.1) |
| 13 | **PLTR** | 194.17 | - | **-** | 18 | - | POS +$40.7M | 189.56 | 200 | 190 | +$797k | +$356k bull / -$98k bear | out (clean 27, ADX 28, RVol 0.7) |
| 14 | **ARM** | 234.33 | - | **-** | 18 | - | POS +$2.6M | - | 227.5 | 250 | +$129k | +$0 bull / -$273k bear | out (clean 26, ADX 24, RVol 1.4) |
| 15 | **QQQ** | 723.68 | - | **-** | 17 | - | NEG -$1.1B | 727.17 | 720 | 720 | +$17.0M | +$3.3M bull / -$1.0M bear | out (clean 29, ADX 24, RVol 1.1) |
| 16 | **TSLA** | 403.39 | - | **-** | 17 | - | POS +$578.8M | - | 400 | 400 | -$12.1M | +$2.5M bull / -$1.0M bear | out (clean 30, ADX 26, RVol 0.7) |
| 17 | **META** | 613.75 | - | **-** | 17 | - | NEG -$280.8M | 634.79 | 650 | 610 | +$4.2M | +$164k bull / -$477k bear | out (clean 29, ADX 23, RVol 1.0) |
| 18 | **AMZN** | 253.50 | - | **-** | 17 | - | POS +$201.4M | 240.04 | 255 | 250 | +$705k | +$28k bull / -$116k bear | out (clean 31, ADX 23, RVol 1.4) |
| 19 | **MU** | 981.34 | - | **-** | 17 | - | POS +$566.1M | - | 1,000 | 950 | +$2.5M | +$1.2M bull / -$6.6M bear | out (clean 28, ADX 24, RVol 1.2) |
| 20 | **NFLX** | 61.62 | - | **-** | 15 | - | NEG -$58.6M | - | 65 | 60 | -$64k | +$28k bull / +$0 bear | out (clean 31, ADX 14, RVol 0.8) |
| 21 | **SMCI** | 35.31 | - | **-** | 11 | - | POS +$21.1M | - | 35 | 35 | +$111k | - | out (clean 28, ADX 31, RVol 1.2) |
| 22 | **COIN** | 159.71 | - | **-** | 9 | - | POS +$2.0M | 155.22 | 170 | 150 | +$94k | - | out (clean 28, ADX 16, RVol 1.6) |
| 23 | **SHOP** | 167.53 | - | **-** | 9 | - | NEG -$4.2M | 171.7 | 175 | 165 | -$26k | - | out (clean 29, ADX 19, RVol 0.7) |
| 24 | **DELL** | 498.03 | - | **-** | 8 | - | POS +$33.1M | - | 500 | 500 | +$213k | - | out (clean 31, ADX 23, RVol 1.0) |
| 25 | **BABA** | 100.53 | - | **-** | 8 | - | NEG -$13.2M | 103.17 | 102 | 100 | +$30k | - | out (clean 29, ADX 25, RVol 0.9) |
| 26 | **UBER** | 65.23 | - | **-** | 6 | - | NEG -$32.7M | - | 70 | 65 | +$57k | - | out (clean 30, ADX 19, RVol 0.6) |
| 27 | **CRM** | 240.71 | - | **-** | 5 | - | POS +$4.8M | 235.79 | 260 | 240 | +$33k | - | out (clean 26, ADX 14, RVol 0.4) |

## Big prints this scan (167)
- **QQQ** CALL 710 2026-10-28 (0DTE): 170 @ 15.97 = **+$271k** BUY | vol 1,112 / OI 1,068
- **MU** PUT 975 2026-10-30 (2DTE): 135 @ 19.65 = **+$265k** BUY | vol 2,816 / OI 305
- **GOOGL** PUT 322.5 2026-10-30 (2DTE): 290 @ 8.65 = **+$251k** SELL | vol 1,468 / OI 1,055
- **QQQ** CALL 712 2026-10-28 (0DTE): 170 @ 14.02 = **+$238k** BUY | vol 1,054 / OI 639
- **QQQ** PUT 724 2026-10-30 (2DTE): 361 @ 5.90 = **+$213k** SELL | vol 3,264 / OI 847
- **MU** CALL 970 2026-10-30 (2DTE): 80 @ 25.45 = **+$204k** SELL | vol 9,119 / OI 1,990
- **QQQ** PUT 724 2026-10-30 (2DTE): 337 @ 5.88 = **+$198k** SELL | vol 3,264 / OI 847
- **AAPL** PUT 350 2026-10-30 (2DTE): 297 @ 6.08 = **+$181k** SELL | vol 2,716 / OI 1,979
- **ORCL** CALL 148 2026-10-30 (2DTE): 499 @ 3.60 = **+$180k** SELL | vol 2,206 / OI 0
- **QQQ** PUT 721 2026-10-30 (2DTE): 361 @ 4.65 = **+$168k** BUY | vol 6,027 / OI 1,287
- **AAPL** PUT 350 2026-10-28 (0DTE): 297 @ 5.40 = **+$160k** MID | vol 1,292 / OI 823
- **QQQ** PUT 721 2026-10-30 (2DTE): 337 @ 4.63 = **+$156k** BUY | vol 6,027 / OI 1,287
- **MU** CALL 980 2026-11-04 (7DTE): 50 @ 30.12 = **+$151k** SELL | vol 326 / OI 23
- **ORCL** CALL 149 2026-10-30 (2DTE): 500 @ 3.00 = **+$150k** SELL | vol 4,999 / OI 0
- **QQQ** PUT 724 2026-10-30 (2DTE): 240 @ 5.91 = **+$142k** MID | vol 3,264 / OI 847

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 740 2026-10-29 (1DTE): 1,475 traded vs OI 1,165
- **SPY** CALL 778 2026-11-04 (7DTE): 501 traded vs OI 123
- **QQQ** CALL 739 2026-11-02 (5DTE): 648 traded vs OI 573
- **QQQ** CALL 725 2026-11-03 (6DTE): 522 traded vs OI 450
- **QQQ** CALL 710 2026-10-28 (0DTE): 1,112 traded vs OI 1,068
- **QQQ** PUT 724 2026-11-02 (5DTE): 532 traded vs OI 42
- **QQQ** PUT 711 2026-10-30 (2DTE): 1,299 traded vs OI 1,248
- **QQQ** CALL 741 2026-10-30 (2DTE): 1,033 traded vs OI 954
- **QQQ** CALL 717 2026-10-29 (1DTE): 709 traded vs OI 637
- **QQQ** CALL 715 2026-11-20 (23DTE): 22,310 traded vs OI 15,648
- **IWM** CALL 282 2026-10-29 (1DTE): 10,680 traded vs OI 10,649
- **IWM** PUT 285 2026-10-28 (0DTE): 504 traded vs OI 37
- **SMH** CALL 590 2026-10-30 (2DTE): 1,039 traded vs OI 985
- **SMH** CALL 592.5 2026-10-30 (2DTE): 661 traded vs OI 546
- **SMH** CALL 582.5 2026-10-30 (2DTE): 535 traded vs OI 382

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
