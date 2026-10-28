# GEX + FLOW SCAN - Wed Oct 28, 02:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (6)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:56 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/28 730C | 0.63 | 0.67 | +24% (10m) | **+6%** (done) | -35% | 723.9 |
| 12:56 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/29 779C | 0.63 | 0.51 | +3% (9m) | **-19%** (done) | +10% | 772.67 |
| 11:40 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 96C | 0.77 | 0.55 | -1% (3m) | **-29%** (done) | +49% | 93.02 |
| 11:05 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 97C | 0.63 | 0.45 | +19% (1m) | **-29%** (done) | +53% | 93.44 |
| 10:50 | **IWM** | **CALLS** | FLOW SURGE | 10/30 284C | 0.57 | 0.54 | +7% (2m) | **-5%** (done) | +22% | 280.64 |
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.34 | +11% (0m) | **-28%** (done) | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 12:55 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | WITH you | **FIRE** QQQ261028C00730000 |
| 12:55 | SPY | 1m WHIPSAW | R1 R2 | CALLS | WITH you | **FIRE** SPY261029C00779000 |

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 344.67 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 38 | 10/28 345C @ 0.58 (delta 0.43) = est -54% at 345 | POS +$295.9M | 341.55 | 350 | 345 | +$3.2M | +$356k bull / +$0 bear | out (clean 28, ADX 15, RVol 1.2) |
| 2 | **IWM** | 279.75 | - | **-** | 23 | - | NEG -$429.0M | 280.96 | 280 | 270 | +$12.3M | +$146k bull / +$0 bear | out (clean 25, ADX 29, RVol 0.6) |
| 3 | **SMH** | 565.96 | - | **-** | 22 | - | POS +$67.3M | 560.47 | 570 | 555 | -$3.6M | +$35k bull / -$51k bear | out (clean 28, ADX 14, RVol 1.0) |
| 4 | **HOOD** | 90.44 | - | **-** | 22 | - | NEG -$17.6M | - | 95 | 90 | +$4.2M | +$95k bull / +$0 bear | out (clean 30, ADX 16, RVol 0.9) |
| 5 | **META** | 610.18 | - | **-** | 21 | - | NEG -$275.8M | 636.81 | 650 | 610 | +$12.2M | +$696k bull / -$102k bear | out (clean 29, ADX 28, RVol 1.1) |
| 6 | **SMCI** | 34.98 | PINNED between the walls (positive gamma) - chop | **-** | 21 | - | POS +$20.1M | - | 35 | 35 | +$131k | - | out (clean 27, ADX 18, RVol 0.5) |
| 7 | **AMD** | 571.65 | - | **-** | 20 | - | POS +$166.5M | - | 600 | 550 | +$5.4M | +$890k bull / -$426k bear | out (clean 29, ADX 29, RVol 1.3) |
| 8 | **PLTR** | 193.96 | - | **-** | 20 | - | POS +$37.3M | 189.73 | 200 | 190 | +$517k | +$58k bull / +$0 bear | out (clean 27, ADX 38, RVol 1.1) |
| 9 | **NVDA** | 217.04 | - | **-** | 17 | - | POS +$519.3M | 210.22 | 220 | 215 | +$9.2M | +$199k bull / -$238k bear | out (clean 26, ADX 16, RVol 0.6) |
| 10 | **GOOGL** | 323.64 | - | **-** | 17 | - | POS +$14.0M | 320.71 | 355 | 300 | +$667k | +$915k bull / +$0 bear | out (clean 33, ADX 20, RVol 1.3) |
| 11 | **TSLA** | 403.26 | - | **-** | 16 | - | POS +$623.1M | - | 400 | 400 | -$16.2M | +$1.5M bull / -$487k bear | out (clean 29, ADX 16, RVol 0.5) |
| 12 | **AMZN** | 252.88 | - | **-** | 16 | - | POS +$184.0M | 243.08 | 255 | 250 | +$2.4M | +$798k bull / -$1.0M bear | out (clean 31, ADX 18, RVol 0.8) |
| 13 | **AVGO** | 349.00 | - | **-** | 16 | - | POS +$60.0M | 338.2 | 350 | 340 | -$142k | +$265k bull / -$34k bear | out (clean 29, ADX 27, RVol 0.6) |
| 14 | **MU** | 970.33 | - | **-** | 16 | - | POS +$633.3M | - | 950 | 950 | +$23.0M | +$3.8M bull / -$1.0M bear | out (clean 28, ADX 18, RVol 0.4) |
| 15 | **MSTR** | 140.37 | - | **-** | 16 | - | POS +$18.5M | - | 152.5 | 140 | +$668k | +$59k bull / +$0 bear | out (clean 27, ADX 14, RVol 0.5) |
| 16 | **QQQ** | 722.55 | - | **-** | 15 | - | NEG -$1.5B | 727.34 | 720 | 720 | +$32.9M | +$2.1M bull / -$1.3M bear | out (clean 29, ADX 11, RVol 0.8) |
| 17 | **MSFT** | 528.13 | - | **-** | 15 | - | POS +$471.7M | - | 550 | 500 | -$81k | +$419k bull / +$0 bear | out (clean 29, ADX 14, RVol 1.2) |
| 18 | **NFLX** | 61.65 | - | **-** | 15 | - | NEG -$56.6M | - | 65 | 60 | -$94k | +$0 bull / -$38k bear | out (clean 31, ADX 16, RVol 0.8) |
| 19 | **ORCL** | 141.63 | - | **-** | 15 | - | POS +$38.8M | - | 135 | 140 | -$1.2M | - | out (clean 30, ADX 27, RVol 7.1) |
| 20 | **SPY** | 770.89 | - | **-** | 14 | - | NEG -$2.4B | 773.28 | 780 | 750 | +$8.0M | +$1.8M bull / -$1.1M bear | out (clean 29, ADX 12, RVol 0.8) |
| 21 | **SHOP** | 167.41 | - | **-** | 11 | - | NEG -$3.9M | 171.57 | 175 | 165 | -$26k | - | out (clean 29, ADX 21, RVol 1.4) |
| 22 | **UBER** | 65.35 | - | **-** | 10 | - | NEG -$30.9M | - | 70 | 65 | +$62k | - | out (clean 30, ADX 23, RVol 1.6) |
| 23 | **BABA** | 100.16 | - | **-** | 10 | - | NEG -$13.6M | 102.97 | 102 | 100 | +$66k | - | out (clean 28, ADX 17, RVol 1.0) |
| 24 | **COIN** | 158.91 | - | **-** | 5 | - | POS +$2.0M | 154.93 | 170 | 150 | +$58k | - | out (clean 28, ADX 10, RVol 0.7) |
| 25 | **DELL** | 494.19 | - | **-** | 5 | - | POS +$30.6M | - | 500 | 500 | +$216k | - | out (clean 30, ADX 11, RVol 0.4) |
| 26 | **ARM** | 232.72 | - | **-** | 4 | - | POS +$1.9M | 222.24 | 227.5 | 250 | +$64k | - | out (clean 26, ADX 13, RVol 0.5) |
| 27 | **CRM** | 241.35 | - | **-** | 4 | - | POS +$6.8M | 234.59 | 260 | 240 | +$14k | - | out (clean 26, ADX 13, RVol 0.5) |

## Big prints this scan (60)
- **SPY** PUT 775 2026-10-30 (2DTE): 1,171 @ 6.25 = **+$732k** BUY | vol 4,238 / OI 3,175
- **QQQ** CALL 710 2026-10-30 (2DTE): 223 @ 14.29 = **+$319k** SELL | vol 598 / OI 9,707
- **QQQ** CALL 717 2026-10-30 (2DTE): 223 @ 9.15 = **+$204k** SELL | vol 700 / OI 1,332
- **SPY** PUT 772 2026-10-29 (1DTE): 311 @ 3.91 = **+$122k** BUY | vol 21,154 / OI 264
- **NVDA** CALL 217.5 2026-10-28 (0DTE): 1,786 @ 0.59 = **+$105k** SELL | vol 121,958 / OI 7,446
- **AMZN** CALL 265 2026-10-30 (2DTE): 172 @ 5.07 = **+$87k** SELL | vol 1,891 / OI 18,534
- **MU** CALL 960 2026-10-28 (0DTE): 80 @ 10.90 = **+$87k** SELL | vol 8,612 / OI 2,947
- **AMZN** PUT 247.5 2026-10-30 (2DTE): 100 @ 7.80 = **+$78k** BUY | vol 841 / OI 1,100
- **TSLA** CALL 397.5 2026-10-28 (0DTE): 190 @ 4.10 = **+$78k** SELL | vol 21,107 / OI 2,326
- **AMZN** PUT 247.5 2026-10-30 (2DTE): 90 @ 7.78 = **+$70k** BUY | vol 841 / OI 1,100
- **MU** CALL 955 2026-10-28 (0DTE): 50 @ 13.50 = **+$68k** SELL | vol 3,411 / OI 340
- **AMZN** CALL 260 2026-10-30 (2DTE): 90 @ 6.82 = **+$61k** SELL | vol 2,629 / OI 8,793
- **META** PUT 610 2026-10-28 (0DTE): 200 @ 2.63 = **+$53k** SELL | vol 39,638 / OI 1,065
- **MU** PUT 990 2026-10-30 (2DTE): 16 @ 32.83 = **+$53k** BUY | vol 1,317 / OI 542
- **NVDA** PUT 217.5 2026-10-30 (2DTE): 155 @ 3.24 = **+$50k** BUY | vol 13,287 / OI 5,808

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 776 2026-11-02 (5DTE): 605 traded vs OI 431
- **SMH** CALL 567.5 2026-11-06 (9DTE): 512 traded vs OI 316
- **TSLA** CALL 422.5 2026-11-02 (5DTE): 508 traded vs OI 187
- **META** PUT 605 2026-10-30 (2DTE): 875 traded vs OI 864
- **AMZN** CALL 250 2026-10-28 (0DTE): 6,532 traded vs OI 6,491
- **MSFT** PUT 505 2026-11-06 (9DTE): 523 traded vs OI 271
- **GOOGL** PUT 307.5 2026-11-06 (9DTE): 1,389 traded vs OI 63
- **MU** PUT 1,000 2026-10-28 (0DTE): 508 traded vs OI 35
- **MSTR** CALL 146 2026-10-30 (2DTE): 845 traded vs OI 785
- **ORCL** CALL 155 2026-10-30 (2DTE): 530 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
