# GEX + FLOW SCAN - Wed Oct 28, 01:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (6)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:56 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/28 730C | 0.63 | 0.59 | -2% (0m) | **-6%** | -35% | 723.9 |
| 12:56 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/29 779C | 0.63 | 0.57 | -3% (0m) | **-10%** | +10% | 772.67 |
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
| 1 | **HOOD** | 90.81 | - | **-** | 25 | - | NEG -$17.0M | - | 95 | 90 | +$3.8M | +$0 bull / -$198k bear | out (clean 30, ADX 27, RVol 0.7) |
| 2 | **IWM** | 280.44 | - | **-** | 22 | - | NEG -$285.6M | 281.34 | 280 | 270 | +$9.6M | +$0 bull / -$282k bear | out (clean 24, ADX 18, RVol 0.7) |
| 3 | **SMCI** | 34.92 | PINNED between the walls (positive gamma) - chop | **-** | 20 | - | POS +$19.1M | - | 35 | 35 | +$115k | - | out (clean 28, ADX 21, RVol 0.3) |
| 4 | **ORCL** | 130.69 | - | **-** | 20 | - | POS +$11.7M | 126.7 | 135 | 130 | -$984k | +$27k bull / +$0 bear | out (clean 29, ADX 16, RVol 0.4) |
| 5 | **PLTR** | 194.26 | - | **-** | 19 | - | POS +$41.2M | 189.27 | 200 | 190 | +$66k | +$0 bull / -$36k bear | out (clean 27, ADX 44, RVol 0.5) |
| 6 | **SMH** | 566.84 | - | **-** | 18 | - | POS +$83.2M | 558.66 | 570 | 555 | -$4.4M | - | out (clean 28, ADX 25, RVol 0.5) |
| 7 | **GOOGL** | 324.01 | - | **-** | 18 | - | POS +$19.8M | 320.75 | 355 | 330 | -$3.8M | +$121k bull / -$301k bear | out (clean 33, ADX 12, RVol 0.7) |
| 8 | **MU** | 973.01 | - | **-** | 18 | - | POS +$606.7M | - | 970 | 950 | +$22.2M | +$1.2M bull / +$0 bear | out (clean 28, ADX 25, RVol 0.5) |
| 9 | **NVDA** | 217.57 | - | **-** | 17 | - | POS +$551.5M | 210.2 | 220 | 215 | +$6.5M | +$0 bull / -$237k bear | out (clean 27, ADX 17, RVol 0.4) |
| 10 | **AMD** | 571.40 | - | **-** | 17 | - | POS +$165.7M | - | 600 | 550 | -$555k | +$0 bull / -$583k bear | out (clean 29, ADX 32, RVol 0.7) |
| 11 | **META** | 613.25 | - | **-** | 17 | - | NEG -$233.3M | 630.59 | 650 | 610 | +$6.8M | +$166k bull / -$391k bear | out (clean 29, ADX 16, RVol 0.7) |
| 12 | **MSFT** | 527.59 | - | **-** | 17 | - | POS +$457.9M | - | 550 | 500 | +$2.4M | +$58k bull / -$245k bear | out (clean 29, ADX 15, RVol 0.7) |
| 13 | **AVGO** | 348.56 | - | **-** | 17 | - | POS +$58.2M | 337.82 | 350 | 340 | -$1.0M | +$0 bull / -$61k bear | out (clean 29, ADX 24, RVol 0.5) |
| 14 | **TSLA** | 402.24 | - | **-** | 16 | - | POS +$599.7M | - | 400 | 395 | -$18.9M | +$25k bull / -$700k bear | out (clean 29, ADX 13, RVol 0.3) |
| 15 | **AAPL** | 345.90 | - | **-** | 16 | - | POS +$403.3M | 341.46 | 350 | 345 | -$1.4M | +$0 bull / -$147k bear | out (clean 28, ADX 18, RVol 0.6) |
| 16 | **SPY** | 771.85 | - | **-** | 15 | - | NEG -$1.7B | 773.54 | 780 | 750 | -$28.2M | +$555k bull / -$1.3M bear | out (clean 29, ADX 14, RVol 0.6) |
| 17 | **AMZN** | 252.97 | - | **-** | 15 | - | POS +$183.4M | 242.7 | 255 | 250 | -$945k | +$0 bull / -$27k bear | out (clean 32, ADX 16, RVol 0.5) |
| 18 | **QQQ** | 723.17 | - | **-** | 13 | - | NEG -$1.4B | 727.66 | 720 | 720 | -$2.0M | +$666k bull / +$0 bear | out (clean 29, ADX 11, RVol 0.3) |
| 19 | **SHOP** | 168.25 | - | **-** | 13 | - | NEG -$4.1M | 172.58 | 175 | 165 | -$32k | - | out (clean 29, ADX 29, RVol 0.8) |
| 20 | **UBER** | 65.67 | - | **-** | 10 | - | NEG -$24.7M | 68.54 | 70 | 65 | -$38k | - | out (clean 30, ADX 38, RVol 0.7) |
| 21 | **NFLX** | 61.86 | - | **-** | 7 | - | NEG -$52.1M | - | 65 | 60 | -$97k | - | out (clean 32, ADX 23, RVol 0.6) |
| 22 | **BABA** | 100.31 | - | **-** | 7 | - | NEG -$13.4M | 103.41 | 102 | 100 | +$19k | - | out (clean 28, ADX 19, RVol 0.9) |
| 23 | **ARM** | 233.42 | - | **-** | 6 | - | POS +$2.5M | - | 227.5 | 250 | +$39k | - | out (clean 27, ADX 23, RVol 0.8) |
| 24 | **DELL** | 493.97 | - | **-** | 4 | - | POS +$28.8M | - | 500 | 500 | +$68k | - | out (clean 31, ADX 15, RVol 0.2) |
| 25 | **CRM** | 240.98 | - | **-** | 4 | - | POS +$5.5M | 235.02 | 260 | 240 | -$6k | - | out (clean 27, ADX 15, RVol 0.2) |
| 26 | **COIN** | 158.37 | - | **-** | 3 | - | POS +$997k | 155.81 | 170 | 150 | -$7k | - | out (clean 29, ADX 8, RVol 0.6) |
| 27 | **MSTR** | 139.65 | - | **-** | 3 | - | POS +$16.5M | - | 152.5 | 140 | -$15k | - | out (clean 27, ADX 11, RVol 0.6) |

## Big prints this scan (43)
- **IWM** PUT 280 2026-10-30 (2DTE): 1,500 @ 1.88 = **+$282k** BUY | vol 4,553 / OI 5,182
- **SPY** PUT 772 2026-10-29 (1DTE): 500 @ 3.67 = **+$184k** BUY | vol 14,478 / OI 264
- **SPY** PUT 772 2026-10-28 (0DTE): 600 @ 2.63 = **+$158k** BUY | vol 46,954 / OI 544
- **SPY** PUT 772 2026-10-28 (0DTE): 494 @ 2.62 = **+$129k** BUY | vol 46,954 / OI 544
- **TSLA** CALL 402.5 2026-10-28 (0DTE): 1,000 @ 1.29 = **+$129k** SELL | vol 115,782 / OI 1,982
- **TSLA** PUT 400 2026-10-30 (2DTE): 169 @ 4.90 = **+$83k** BUY | vol 18,841 / OI 1,925
- **MU** PUT 975 2026-10-28 (0DTE): 100 @ 7.50 = **+$75k** SELL | vol 10,022 / OI 11
- **META** CALL 620 2026-11-02 (5DTE): 87 @ 8.40 = **+$73k** MID | vol 572 / OI 14
- **MSFT** PUT 510 2026-10-30 (2DTE): 105 @ 5.94 = **+$62k** BUY | vol 1,384 / OI 1,313
- **MU** PUT 970 2026-10-28 (0DTE): 100 @ 5.15 = **+$52k** SELL | vol 21,380 / OI 23
- **AMD** CALL 567.5 2026-10-30 (2DTE): 36 @ 13.60 = **+$49k** SELL | vol 1,188 / OI 726
- **TSLA** CALL 402.5 2026-10-28 (0DTE): 365 @ 1.29 = **+$47k** SELL | vol 115,782 / OI 1,982
- **MSFT** PUT 510 2026-10-30 (2DTE): 65 @ 5.94 = **+$39k** BUY | vol 1,384 / OI 1,313
- **MSFT** PUT 530 2026-11-02 (5DTE): 25 @ 14.90 = **+$37k** MID | vol 276 / OI 2,149
- **NVDA** PUT 217.5 2026-10-30 (2DTE): 123 @ 3.00 = **+$37k** BUY | vol 10,637 / OI 5,808

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 752 2026-10-29 (1DTE): 799 traded vs OI 718
- **SPY** CALL 768 2026-10-29 (1DTE): 1,966 traded vs OI 1,953
- **NVDA** CALL 212.5 2026-11-02 (5DTE): 550 traded vs OI 498
- **NVDA** CALL 222.5 2026-10-30 (2DTE): 16,718 traded vs OI 16,679
- **TSLA** CALL 410 2026-11-04 (7DTE): 884 traded vs OI 869
- **META** CALL 620 2026-11-02 (5DTE): 572 traded vs OI 14
- **AMZN** CALL 240 2026-11-02 (5DTE): 643 traded vs OI 21
- **MSFT** PUT 510 2026-10-30 (2DTE): 1,384 traded vs OI 1,313
- **GOOGL** PUT 307.5 2026-10-30 (2DTE): 1,333 traded vs OI 453
- **NFLX** CALL 65 2026-11-20 (23DTE): 3,525 traded vs OI 3,519
- **MU** CALL 1,070 2026-10-30 (2DTE): 545 traded vs OI 0
- **MSTR** CALL 148 2026-10-30 (2DTE): 1,830 traded vs OI 1,753
- **MSTR** CALL 139 2026-10-30 (2DTE): 781 traded vs OI 728

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
