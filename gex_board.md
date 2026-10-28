# GEX + FLOW SCAN - Wed Oct 28, 12:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:40 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 96C | 0.77 | 0.51 | -1% (3m) | **-34%** | +49% | 93.02 |
| 11:05 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 97C | 0.63 | 0.45 | +19% (1m) | **-29%** (done) | +53% | 93.44 |
| 10:50 | **IWM** | **CALLS** | FLOW SURGE | 10/30 284C | 0.57 | 0.54 | +7% (2m) | **-5%** (done) | +22% | 280.64 |
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.34 | +11% (0m) | **-28%** (done) | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 345.64 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 33 | none: 84 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (52 contracts' greeks worked out here) | POS +$374.8M | 341.52 | 350 | 345 | -$610k | +$109k bull / -$108k bear | out (clean 28, ADX 14, RVol 0.6) |
| 2 | **TSLA** | 401.00 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 32 | 10/28 397.5P @ 0.61 (delta 0.22) = est -24% at 400 | POS +$596.2M | - | 400 | 395 | -$17.7M | +$122k bull / -$379k bear | out (clean 29, ADX 13, RVol 0.3) |
| 3 | **ORCL** | 130.74 | - | **-** | 21 | - | POS +$11.3M | 126.74 | 135 | 130 | -$948k | +$0 bull / -$97k bear | out (clean 29, ADX 18, RVol 0.4) |
| 4 | **MSFT** | 527.50 | - | **-** | 19 | - | POS +$453.6M | - | 550 | 500 | +$2.5M | +$371k bull / -$25k bear | out (clean 29, ADX 17, RVol 1.2) |
| 5 | **PLTR** | 193.90 | - | **-** | 19 | - | POS +$38.4M | 189.25 | 200 | 190 | +$61k | +$153k bull / +$0 bear | out (clean 27, ADX 43, RVol 0.4) |
| 6 | **NVDA** | 217.02 | - | **-** | 18 | - | POS +$509.5M | 209.83 | 220 | 215 | +$8.1M | +$164k bull / -$721k bear | out (clean 27, ADX 18, RVol 0.5) |
| 7 | **META** | 613.30 | - | **-** | 18 | - | NEG -$257.1M | 635.85 | 650 | 610 | +$8.1M | +$354k bull / -$405k bear | out (clean 29, ADX 18, RVol 0.7) |
| 8 | **MU** | 972.22 | - | **-** | 18 | - | POS +$612.5M | - | 950 | 950 | +$16.3M | +$3.3M bull / -$1.3M bear | out (clean 28, ADX 28, RVol 0.3) |
| 9 | **SMH** | 565.15 | - | **-** | 17 | - | POS +$59.6M | 560.03 | 570 | 555 | -$4.1M | - | out (clean 28, ADX 22, RVol 0.5) |
| 10 | **AMD** | 567.94 | - | **-** | 17 | - | POS +$168.9M | - | 600 | 550 | +$1.2M | +$60k bull / -$755k bear | out (clean 28, ADX 26, RVol 0.8) |
| 11 | **GOOGL** | 323.47 | - | **-** | 16 | - | POS +$14.0M | 320.8 | 355 | 300 | -$1.3M | +$25k bull / -$153k bear | out (clean 33, ADX 12, RVol 0.6) |
| 12 | **HOOD** | 90.72 | - | **-** | 16 | - | NEG -$16.8M | - | 95 | 90 | +$3.8M | - | out (clean 30, ADX 32, RVol 0.7) |
| 13 | **AVGO** | 347.15 | - | **-** | 15 | - | POS +$53.4M | 336.18 | 350 | 340 | -$247k | +$0 bull / -$55k bear | out (clean 29, ADX 19, RVol 0.5) |
| 14 | **SPY** | 771.16 | - | **-** | 14 | - | NEG -$2.4B | 773.58 | 780 | 750 | -$17.3M | +$456k bull / -$630k bear | out (clean 29, ADX 10, RVol 0.3) |
| 15 | **AMZN** | 252.74 | - | **-** | 14 | - | POS +$189.7M | 238.91 | 255 | 250 | -$407k | +$0 bull / -$161k bear | out (clean 32, ADX 15, RVol 0.5) |
| 16 | **QQQ** | 722.14 | - | **-** | 12 | - | NEG -$1.7B | 727.85 | 720 | 720 | -$614k | +$145k bull / -$553k bear | out (clean 29, ADX 7, RVol 0.3) |
| 17 | **SHOP** | 168.45 | - | **-** | 12 | - | NEG -$3.3M | 171.84 | 175 | 165 | -$31k | - | out (clean 28, ADX 25, RVol 0.6) |
| 18 | **IWM** | 280.12 | - | **-** | 11 | - | NEG -$340.1M | 281.25 | 280 | 270 | +$9.3M | - | out (clean 24, ADX 16, RVol 0.4) |
| 19 | **UBER** | 65.62 | - | **-** | 10 | - | NEG -$25.9M | 69.14 | 70 | 65 | -$63k | - | out (clean 30, ADX 33, RVol 0.5) |
| 20 | **SMCI** | 34.77 | - | **-** | 9 | - | POS +$18.6M | - | 35 | 35 | +$111k | - | out (clean 28, ADX 22, RVol 0.2) |
| 21 | **ARM** | 232.62 | - | **-** | 6 | - | POS +$1.7M | 222.97 | 220 | 250 | +$69k | - | out (clean 27, ADX 20, RVol 0.4) |
| 22 | **CRM** | 240.61 | - | **-** | 6 | - | POS +$4.5M | 235.64 | 260 | 240 | +$23k | - | out (clean 27, ADX 18, RVol 0.2) |
| 23 | **BABA** | 100.42 | - | **-** | 6 | - | NEG -$13.4M | 103.42 | 102 | 100 | +$19k | - | out (clean 28, ADX 16, RVol 0.5) |
| 24 | **NFLX** | 61.83 | - | **-** | 5 | - | NEG -$56.9M | - | 65 | 60 | -$22k | - | out (clean 32, ADX 24, RVol 0.4) |
| 25 | **COIN** | 158.47 | - | **-** | 5 | - | POS +$1.2M | 155.65 | 170 | 150 | -$36k | - | out (clean 29, ADX 8, RVol 0.4) |
| 26 | **DELL** | 493.04 | - | **-** | 4 | - | POS +$28.0M | - | 500 | 500 | +$67k | - | out (clean 30, ADX 17, RVol 0.3) |
| 27 | **MSTR** | 139.25 | - | **-** | 3 | - | POS +$15.5M | - | 152.5 | 140 | -$35k | - | out (clean 27, ADX 9, RVol 0.3) |

## Big prints this scan (55)
- **MU** PUT 990 2026-10-28 (0DTE): 500 @ 18.22 = **+$911k** SELL | vol 2,448 / OI 19
- **MU** PUT 985 2026-10-28 (0DTE): 500 @ 13.92 = **+$696k** SELL | vol 2,134 / OI 25
- **MU** CALL 935 2026-10-28 (0DTE): 78 @ 38.10 = **+$297k** BUY | vol 1,214 / OI 559
- **MSFT** CALL 540 2026-10-30 (2DTE): 337 @ 8.18 = **+$276k** BUY | vol 1,488 / OI 7,800
- **SPY** CALL 748 2026-10-30 (2DTE): 100 @ 23.67 = **+$237k** MID | vol 126 / OI 432
- **SPY** PUT 772 2026-10-29 (1DTE): 500 @ 3.68 = **+$184k** BUY | vol 11,065 / OI 264
- **QQQ** PUT 722 2026-11-02 (5DTE): 204 @ 7.16 = **+$146k** MID | vol 1,246 / OI 87
- **SPY** PUT 772 2026-10-28 (0DTE): 500 @ 2.72 = **+$136k** BUY | vol 39,411 / OI 544
- **SPY** PUT 773 2026-10-28 (0DTE): 414 @ 3.15 = **+$130k** MID | vol 32,549 / OI 703
- **SPY** PUT 772 2026-10-28 (0DTE): 500 @ 2.59 = **+$130k** SELL | vol 39,411 / OI 544
- **SPY** PUT 771 2026-10-29 (1DTE): 344 @ 3.20 = **+$110k** MID | vol 29,037 / OI 583
- **SPY** PUT 771 2026-10-29 (1DTE): 316 @ 3.18 = **+$100k** SELL | vol 29,037 / OI 583
- **META** CALL 615 2026-10-28 (0DTE): 400 @ 2.42 = **+$97k** SELL | vol 13,155 / OI 62
- **MU** CALL 975 2026-10-30 (2DTE): 40 @ 18.95 = **+$76k** BUY | vol 5,475 / OI 5,300
- **AAPL** PUT 345 2026-10-30 (2DTE): 288 @ 2.56 = **+$74k** BUY | vol 7,005 / OI 9,983

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 772 2026-10-30 (2DTE): 2,597 traded vs OI 2,543
- **NVDA** PUT 210 2026-11-02 (5DTE): 1,494 traded vs OI 1,402
- **TSLA** PUT 387.5 2026-11-06 (9DTE): 501 traded vs OI 147
- **AAPL** CALL 337.5 2026-10-30 (2DTE): 574 traded vs OI 573
- **AAPL** CALL 340 2026-10-28 (0DTE): 541 traded vs OI 465
- **AAPL** PUT 347.5 2026-10-30 (2DTE): 1,843 traded vs OI 1,832
- **AMD** CALL 552.5 2026-10-30 (2DTE): 500 traded vs OI 290
- **META** PUT 670 2026-10-28 (0DTE): 505 traded vs OI 60
- **META** CALL 627.5 2026-10-30 (2DTE): 500 traded vs OI 74
- **META** CALL 630 2026-11-02 (5DTE): 500 traded vs OI 292

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
