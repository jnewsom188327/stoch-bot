# GEX + FLOW SCAN - Mon Nov 09, 12:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:04 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/09 754C | 0.41 | 0.23 | -2% (0m) | **-44%** (done) | +28% | 752.23 |
| 10:35 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 272.5C | 0.49 | 0.05 | +2% (2m) | **-90%** (done) | +225% | 273.49 |
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.72 | +51% (23m) | **-6%** (done) | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.02 | +13% (6m) | **-96%** (done) | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:20:08 ET, last candle SPY 12:19, QQQ 12:19 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:03 | SPY | 1m WHIPSAW | R1 | CALLS | TURNING away | **FIRE** SPY261109C00754000 |

## Flow surges NOT fired - price disagreed (17 today, last 5)
- 10:55 AVGO PUTS: price +2.40 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 AVGO PUTS: price +1.16 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 QQQ PUTS: price +0.45 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:35 AVGO PUTS: price +1.05 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:30 QQQ PUTS: price +0.53 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 350.19 | PINNED between the walls (positive gamma) - chop | **-** | 31 | - | POS +$425.7M | 339.21 | 350 | 350 | -$6.2M | +$0 bull / -$35k bear | out (clean 28, ADX 32, RVol 0.4) |
| 2 | **UBER** | 70.12 | PINNED between the walls (positive gamma) - chop | **-** | 30 | - | POS +$4.1M | 69.1 | 70 | 70 | -$149k | - | out (clean 31, ADX 35, RVol 1.1) |
| 3 | **SPY** | 752.24 | - | **-** | 27 | - | NEG -$6.2B | 761.71 | 750 | 740 | -$269.4M | +$0 bull / -$1.1M bear | out (clean 32, ADX 50, RVol 0.4) |
| 4 | **AVGO** | 320.44 | - | **-** | 27 | - | NEG -$65.3M | - | 340 | 320 | -$8.3M | +$0 bull / -$162k bear | out (clean 31, ADX 54, RVol 0.7) |
| 5 | **QQQ** | 677.75 | - | **-** | 26 | - | NEG -$2.0B | 698.75 | 680 | 680 | -$237.6M | +$0 bull / -$445k bear | out (clean 32, ADX 45, RVol 0.4) |
| 6 | **TSLA** | 377.53 | - | **-** | 26 | - | POS +$125.4M | - | 380 | 380 | -$93.0M | +$0 bull / -$633k bear | out (clean 34, ADX 36, RVol 0.3) |
| 7 | **AMD** | 502.28 | - | **-** | 26 | - | POS +$20.5M | 488.93 | 500 | 500 | -$54.1M | +$0 bull / -$651k bear | out (clean 32, ADX 49, RVol 0.3) |
| 8 | **PLTR** | 169.61 | - | **-** | 26 | - | POS +$11.9M | - | 165 | 180 | -$4.8M | +$0 bull / -$54k bear | out (clean 30, ADX 42, RVol 0.3) |
| 9 | **NVDA** | 177.44 | - | **-** | 24 | - | NEG -$193.0M | - | 190 | 190 | -$58.6M | +$0 bull / -$2.1M bear | out (clean 32, ADX 35, RVol 1.9) |
| 10 | **META** | 642.30 | - | **-** | 22 | - | POS +$178.3M | 614.82 | 650 | 640 | -$10.6M | +$0 bull / -$291k bear | out (clean 32, ADX 38, RVol 0.3) |
| 11 | **DELL** | 352.31 | - | **-** | 21 | - | NEG -$6.2M | - | 350 | 340 | -$600k | +$0 bull / -$78k bear | out (clean 32, ADX 44, RVol 0.3) |
| 12 | **HOOD** | 84.08 | - | **-** | 21 | - | NEG -$1.6M | - | 85 | 85 | -$2.0M | +$46k bull / -$25k bear | out (clean 31, ADX 34, RVol 0.4) |
| 13 | **IWM** | 281.23 | - | **-** | 19 | - | NEG -$942.6M | 284.88 | 285 | 270 | -$20.7M | - | out (clean 35, ADX 61, RVol 0.3) |
| 14 | **MSFT** | 544.22 | - | **-** | 18 | - | POS +$612.3M | - | 550 | 540 | +$1.9M | +$0 bull / -$31k bear | out (clean 34, ADX 29, RVol 0.4) |
| 15 | **GOOGL** | 291.62 | - | **-** | 18 | - | POS +$15.6M | 288.78 | 300 | 290 | +$3.8M | +$0 bull / -$46k bear | out (clean 31, ADX 15, RVol 0.8) |
| 16 | **MU** | 733.18 | - | **-** | 18 | - | POS +$2.4M | 731.26 | 750 | 750 | -$13.5M | +$486k bull / -$806k bear | out (clean 32, ADX 36, RVol 0.3) |
| 17 | **MSTR** | 126.30 | - | **-** | 18 | - | POS +$1.3M | 123.66 | 135 | 120 | -$2.3M | +$88k bull / +$0 bear | out (clean 30, ADX 17, RVol 0.5) |
| 18 | **BABA** | 105.44 | - | **-** | 18 | - | POS +$2.0M | 104.33 | 110 | 110 | +$113k | +$0 bull / -$25k bear | out (clean 32, ADX 34, RVol 0.3) |
| 19 | **COIN** | 137.15 | - | **-** | 15 | - | NEG -$6.5M | - | 140 | 135 | -$2.0M | - | out (clean 32, ADX 17, RVol 0.3) |
| 20 | **SMCI** | 29.52 | - | **-** | 14 | - | NEG -$24k | - | 30 | 30 | -$995k | - | out (clean 30, ADX 11, RVol 0.4) |
| 21 | **SMH** | 485.44 | - | **-** | 13 | - | NEG -$216.6M | - | 500 | 475 | -$2.8M | - | out (clean 31, ADX 38, RVol 0.4) |
| 22 | **AMZN** | 268.61 | - | **-** | 12 | - | POS +$397.0M | - | 270 | 265 | +$20.2M | - | out (clean 34, ADX 12, RVol 0.3) |
| 23 | **SHOP** | 150.80 | - | **-** | 12 | - | POS +$1.9M | - | 150 | 140 | -$88k | - | out (clean 34, ADX 17, RVol 0.1) |
| 24 | **ARM** | 188.07 | - | **-** | 11 | - | NEG -$4.5M | - | 185 | 190 | +$252k | - | out (clean 27, ADX 46, RVol 0.6) |
| 25 | **ORCL** | 119.12 | - | **-** | 7 | - | NEG -$26.5M | - | 125 | 125 | -$541k | - | out (clean 30, ADX 21, RVol 0.6) |
| 26 | **CRM** | 216.31 | - | **-** | 6 | - | NEG -$11.5M | - | 230 | 220 | -$11k | - | out (clean 34, ADX 23, RVol 0.3) |
| 27 | **NFLX** | 63.87 | - | **-** | 4 | - | NEG -$19.4M | 67.66 | 65 | 65 | +$25k | - | out (clean 31, ADX 15, RVol 0.5) |

## Big prints this scan (41)
- **SPY** CALL 738 2026-11-09 (0DTE): 200 @ 13.15 = **+$263k** SELL | vol 3,463 / OI 906
- **QQQ** CALL 655 2026-11-09 (0DTE): 100 @ 21.65 = **+$216k** SELL | vol 593 / OI 682
- **SPY** PUT 754 2026-11-09 (0DTE): 599 @ 2.95 = **+$177k** BUY | vol 11,985 / OI 1,253
- **AMD** CALL 490 2026-11-13 (4DTE): 48 @ 25.20 = **+$121k** SELL | vol 2,706 / OI 1,648
- **NVDA** CALL 175 2026-11-09 (0DTE): 457 @ 2.44 = **+$112k** SELL | vol 79,048 / OI 296
- **QQQ** PUT 680 2026-11-16 (7DTE): 100 @ 10.72 = **+$107k** BUY | vol 1,079 / OI 284
- **TSLA** CALL 365 2026-11-13 (4DTE): 62 @ 16.90 = **+$105k** SELL | vol 1,100 / OI 944
- **NVDA** CALL 175 2026-11-09 (0DTE): 351 @ 2.80 = **+$98k** SELL | vol 79,048 / OI 296
- **AMD** CALL 490 2026-11-13 (4DTE): 35 @ 25.20 = **+$88k** SELL | vol 2,706 / OI 1,648
- **MSTR** PUT 126 2026-11-13 (4DTE): 195 @ 4.50 = **+$88k** SELL | vol 1,304 / OI 193
- **NVDA** CALL 175 2026-11-09 (0DTE): 380 @ 2.10 = **+$80k** SELL | vol 79,048 / OI 296
- **AMD** CALL 490 2026-11-13 (4DTE): 26 @ 25.60 = **+$67k** SELL | vol 2,706 / OI 1,648
- **NVDA** PUT 175 2026-11-13 (4DTE): 150 @ 4.40 = **+$66k** BUY | vol 17,430 / OI 5,460
- **AMD** CALL 490 2026-11-13 (4DTE): 23 @ 24.75 = **+$57k** SELL | vol 2,706 / OI 1,648
- **PLTR** PUT 167.5 2026-11-13 (4DTE): 150 @ 3.60 = **+$54k** BUY | vol 1,382 / OI 744

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 718 2026-11-10 (1DTE): 503 traded vs OI 404
- **SPY** CALL 774 2026-11-12 (3DTE): 544 traded vs OI 419
- **SPY** CALL 765 2026-11-17 (8DTE): 582 traded vs OI 246
- **SPY** PUT 746 2026-11-13 (4DTE): 1,343 traded vs OI 1,297
- **SPY** CALL 763 2026-11-18 (9DTE): 569 traded vs OI 209
- **SPY** CALL 752 2026-11-16 (7DTE): 534 traded vs OI 142
- **QQQ** PUT 680 2026-11-11 (2DTE): 503 traded vs OI 451
- **QQQ** PUT 650 2026-11-16 (7DTE): 593 traded vs OI 589
- **AAPL** PUT 345 2026-11-13 (4DTE): 2,796 traded vs OI 2,755
- **AMD** PUT 495 2026-11-11 (2DTE): 517 traded vs OI 56
- **META** PUT 610 2026-11-09 (0DTE): 517 traded vs OI 391
- **META** CALL 660 2026-11-13 (4DTE): 607 traded vs OI 600
- **META** PUT 612.5 2026-11-11 (2DTE): 618 traded vs OI 37
- **META** PUT 615 2026-11-11 (2DTE): 866 traded vs OI 48
- **MSFT** PUT 530 2026-11-11 (2DTE): 509 traded vs OI 228

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
