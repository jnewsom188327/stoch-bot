# GEX + FLOW SCAN - Wed Oct 28, 11:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:05 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 97C | 0.63 | 0.65 | +19% (1m) | **+3%** | +53% | 93.44 |
| 10:50 | **IWM** | **CALLS** | FLOW SURGE | 10/30 284C | 0.57 | 0.50 | +7% (2m) | **-12%** | +22% | 280.64 |
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.31 | +11% (0m) | **-34%** | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **HOOD** | 91.88 | FLOW SURGE | **CALLS** | 54 | 10/30 97C @ 0.70 (delta 0.21) = est +43% at 93.49 | NEG -$15.9M | - | 100 | 90 | +$2.4M | +$264k bull / +$0 bear | out (clean 30, ADX 35, RVol 2.7) |
| 2 | **CRM** | 240.37 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 45 | none: 19 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$3.8M | 235.66 | 260 | 240 | +$63k | - | out (clean 27, ADX 20, RVol 1.4) |
| 3 | **AMZN** | 252.40 | FLOW SURGE | **CALLS** | 37 | none: 84 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (31 contracts' greeks worked out here) | POS +$181.1M | 243.88 | 250 | 250 | +$4.7M | +$1.7M bull / -$28k bear | out (clean 32, ADX 21, RVol 1.1) |
| 4 | **AAPL** | 345.29 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 36 | none: 81 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (42 contracts' greeks worked out here) | POS +$340.9M | 341.25 | 350 | 345 | +$279k | +$387k bull / -$127k bear | out (clean 30, ADX 25, RVol 0.8) |
| 5 | **MSTR** | 140.06 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 31 | none: 25 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$17.3M | - | 152.5 | 140 | -$227k | +$0 bull / -$145k bear | out (clean 29, ADX 8, RVol 0.3) |
| 6 | **META** | 612.50 | - | **-** | 29 | - | NEG -$269.7M | 637.41 | 650 | 600 | +$12.6M | +$210k bull / -$447k bear | out (clean 29, ADX 32, RVol 1.6) |
| 7 | **ORCL** | 129.94 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 25 | none: 26 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$8.7M | 126.65 | 135 | 130 | +$148k | - | out (clean 28, ADX 14, RVol 0.7) |
| 8 | **PLTR** | 194.60 | - | **-** | 24 | - | POS +$47.3M | 188.98 | 200 | 190 | -$873k | +$146k bull / +$0 bear | out (clean 28, ADX 52, RVol 0.7) |
| 9 | **MSFT** | 528.21 | - | **-** | 22 | - | POS +$456.2M | - | 550 | 500 | +$1.5M | +$222k bull / -$248k bear | out (clean 30, ADX 21, RVol 1.1) |
| 10 | **AVGO** | 345.46 | - | **-** | 22 | - | POS +$52.5M | 336.65 | 350 | 340 | +$1.8M | +$28k bull / +$0 bear | out (clean 30, ADX 16, RVol 0.9) |
| 11 | **TSLA** | 401.62 | - | **-** | 21 | - | POS +$581.5M | - | 400 | 395 | -$16.0M | +$0 bull / -$1.5M bear | out (clean 28, ADX 29, RVol 0.8) |
| 12 | **SHOP** | 165.87 | - | **-** | 21 | - | NEG -$5.3M | 172.09 | 175 | 165 | +$19k | - | out (clean 26, ADX 23, RVol 1.0) |
| 13 | **DELL** | 495.28 | - | **-** | 20 | - | POS +$30.7M | - | 500 | 500 | +$130k | +$25k bull / +$0 bear | out (clean 30, ADX 27, RVol 1.3) |
| 14 | **MU** | 971.16 | - | **-** | 20 | - | POS +$603.2M | - | 950 | 950 | +$14.7M | +$229k bull / -$4.6M bear | out (clean 28, ADX 34, RVol 0.5) |
| 15 | **SMH** | 564.98 | - | **-** | 19 | - | POS +$50.4M | 559.82 | 570 | 555 | -$315k | +$0 bull / -$198k bear | out (clean 29, ADX 27, RVol 0.6) |
| 16 | **GOOGL** | 323.64 | - | **-** | 19 | - | POS +$12.5M | 321.01 | 355 | 300 | +$2.9M | - | out (clean 33, ADX 20, RVol 1.9) |
| 17 | **IWM** | 279.62 | - | **-** | 18 | - | NEG -$497.0M | 281.32 | 280 | 270 | +$11.5M | - | out (clean 24, ADX 22, RVol 0.7) |
| 18 | **NVDA** | 217.75 | - | **-** | 17 | - | POS +$562.4M | 210.02 | 220 | 215 | +$3.7M | +$359k bull / +$0 bear | out (clean 27, ADX 10, RVol 0.6) |
| 19 | **AMD** | 567.46 | - | **-** | 16 | - | POS +$164.1M | - | 600 | 550 | +$132k | +$0 bull / -$836k bear | out (clean 28, ADX 21, RVol 0.8) |
| 20 | **SPY** | 770.74 | - | **-** | 15 | - | NEG -$2.8B | 773.55 | 780 | 750 | +$11.3M | +$921k bull / -$355k bear | out (clean 30, ADX 13, RVol 0.6) |
| 21 | **BABA** | 100.33 | - | **-** | 12 | - | NEG -$13.3M | 103.3 | 102 | 100 | +$38k | - | out (clean 28, ADX 20, RVol 0.6) |
| 22 | **UBER** | 64.96 | - | **-** | 11 | - | NEG -$33.4M | - | 70 | 65 | +$34k | - | out (clean 28, ADX 38, RVol 0.7) |
| 23 | **NFLX** | 61.80 | - | **-** | 9 | - | NEG -$55.1M | - | 65 | 60 | -$19k | - | out (clean 32, ADX 46, RVol 0.5) |
| 24 | **SMCI** | 34.90 | - | **-** | 9 | - | POS +$19.1M | - | 35 | 35 | +$104k | - | out (clean 28, ADX 18, RVol 0.5) |
| 25 | **COIN** | 158.32 | - | **-** | 8 | - | POS +$1.4M | 155.17 | 170 | 150 | -$32k | - | out (clean 30, ADX 18, RVol 0.9) |
| 26 | **ARM** | 233.21 | - | **-** | 8 | - | POS +$1.7M | 223.36 | 227.5 | 250 | +$75k | - | out (clean 26, ADX 29, RVol 0.5) |
| 27 | **QQQ** | 721.89 | - | **-** | 3 | - | NEG -$1.8B | 727.87 | 720 | 720 | +$773k | - | out (clean 30, ADX 12, RVol 0.4) |

## Big prints this scan (86)
- **AAPL** CALL 335 2026-10-28 (0DTE): 370 @ 10.45 = **+$387k** BUY | vol 878 / OI 266
- **MU** PUT 965 2026-10-28 (0DTE): 436 @ 5.40 = **+$235k** BUY | vol 11,036 / OI 17
- **MU** CALL 945 2026-11-04 (7DTE): 50 @ 43.21 = **+$216k** SELL | vol 92 / OI 28
- **SPY** PUT 773 2026-10-28 (0DTE): 498 @ 3.79 = **+$189k** BUY | vol 21,109 / OI 703
- **META** PUT 630 2026-10-30 (2DTE): 53 @ 21.11 = **+$112k** BUY | vol 318 / OI 1,632
- **MSTR** PUT 141 2026-10-30 (2DTE): 200 @ 5.35 = **+$107k** BUY | vol 604 / OI 2,987
- **MSFT** CALL 530 2026-10-30 (2DTE): 80 @ 12.65 = **+$101k** MID | vol 1,412 / OI 7,642
- **TSLA** CALL 400 2026-10-28 (0DTE): 378 @ 2.44 = **+$92k** SELL | vol 57,065 / OI 4,776
- **MSFT** CALL 530 2026-10-30 (2DTE): 68 @ 12.65 = **+$86k** MID | vol 1,412 / OI 7,642
- **MU** CALL 925 2026-10-28 (0DTE): 20 @ 42.87 = **+$86k** SELL | vol 661 / OI 909
- **MU** CALL 945 2026-11-04 (7DTE): 20 @ 42.86 = **+$86k** SELL | vol 92 / OI 28
- **MU** PUT 1,000 2026-10-30 (2DTE): 18 @ 39.32 = **+$71k** BUY | vol 495 / OI 1,100
- **MSFT** CALL 527.5 2026-10-30 (2DTE): 50 @ 13.52 = **+$68k** SELL | vol 205 / OI 454
- **TSLA** CALL 400 2026-10-28 (0DTE): 280 @ 2.20 = **+$62k** SELL | vol 57,065 / OI 4,776
- **MSFT** CALL 530 2026-10-30 (2DTE): 50 @ 12.32 = **+$62k** SELL | vol 1,412 / OI 7,642

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 768 2026-10-30 (2DTE): 2,379 traded vs OI 2,258
- **SPY** PUT 774 2026-10-29 (1DTE): 508 traded vs OI 218
- **SPY** CALL 760 2026-10-28 (0DTE): 1,042 traded vs OI 943
- **QQQ** PUT 705 2026-10-29 (1DTE): 2,081 traded vs OI 2,008
- **IWM** PUT 266 2026-11-13 (16DTE): 1,003 traded vs OI 508
- **NVDA** PUT 232.5 2026-10-30 (2DTE): 795 traded vs OI 541
- **TSLA** CALL 415 2026-11-02 (5DTE): 807 traded vs OI 715
- **TSLA** CALL 412.5 2026-10-30 (2DTE): 2,320 traded vs OI 2,269
- **TSLA** CALL 440 2026-10-30 (2DTE): 502 traded vs OI 0
- **TSLA** CALL 417.5 2026-10-30 (2DTE): 1,615 traded vs OI 1,563
- **META** CALL 630 2026-11-06 (9DTE): 580 traded vs OI 92
- **GOOGL** PUT 320 2026-11-27 (30DTE): 1,121 traded vs OI 501
- **PLTR** CALL 195 2026-10-30 (2DTE): 2,889 traded vs OI 2,880
- **MU** CALL 1,000 2026-10-30 (2DTE): 8,951 traded vs OI 8,792
- **MU** CALL 1,055 2026-10-28 (0DTE): 519 traded vs OI 116

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
