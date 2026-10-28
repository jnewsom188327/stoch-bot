# GEX + FLOW SCAN - Wed Oct 28, 12:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:40 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 96C | 0.77 | 0.55 | -1% (3m) | **-29%** (done) | +49% | 93.02 |
| 11:05 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 97C | 0.63 | 0.45 | +19% (1m) | **-29%** (done) | +53% | 93.44 |
| 10:50 | **IWM** | **CALLS** | FLOW SURGE | 10/30 284C | 0.57 | 0.54 | +7% (2m) | **-5%** (done) | +22% | 280.64 |
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.34 | +11% (0m) | **-28%** (done) | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMH** | 565.57 | FLOW SURGE | **PUTS** | 34 | none: 180 puts 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (88 contracts' greeks worked out here) | POS +$60.9M | 559.51 | 570 | 555 | -$4.3M | +$0 bull / -$148k bear | out (clean 28, ADX 22, RVol 0.4) |
| 2 | **HOOD** | 90.68 | - | **-** | 25 | - | NEG -$16.7M | - | 95 | 90 | +$3.8M | +$0 bull / -$29k bear | out (clean 30, ADX 32, RVol 0.6) |
| 3 | **META** | 613.61 | - | **-** | 18 | - | NEG -$265.7M | 636.09 | 650 | 610 | +$7.7M | +$541k bull / -$405k bear | out (clean 29, ADX 16, RVol 0.6) |
| 4 | **MSFT** | 527.10 | - | **-** | 18 | - | POS +$423.6M | - | 550 | 500 | +$2.7M | +$408k bull / +$0 bear | out (clean 29, ADX 17, RVol 0.7) |
| 5 | **MU** | 967.24 | - | **-** | 18 | - | POS +$621.9M | - | 950 | 950 | +$20.0M | +$2.8M bull / -$191k bear | out (clean 28, ADX 26, RVol 0.4) |
| 6 | **NVDA** | 217.34 | - | **-** | 17 | - | POS +$531.0M | 210.41 | 220 | 215 | +$7.6M | +$0 bull / -$341k bear | out (clean 27, ADX 18, RVol 0.5) |
| 7 | **GOOGL** | 323.46 | - | **-** | 17 | - | POS +$12.1M | 320.97 | 355 | 300 | -$2.8M | +$1.4M bull / -$221k bear | out (clean 33, ADX 12, RVol 0.7) |
| 8 | **AAPL** | 346.14 | - | **-** | 16 | - | POS +$408.6M | 341.92 | 350 | 345 | -$1.5M | +$0 bull / -$193k bear | out (clean 28, ADX 16, RVol 0.6) |
| 9 | **AMD** | 569.13 | - | **-** | 16 | - | POS +$171.7M | - | 600 | 550 | -$3k | +$0 bull / -$977k bear | out (clean 29, ADX 29, RVol 0.6) |
| 10 | **AVGO** | 347.54 | - | **-** | 16 | - | POS +$54.5M | 336.66 | 350 | 340 | -$781k | +$0 bull / -$156k bear | out (clean 29, ADX 20, RVol 0.4) |
| 11 | **TSLA** | 401.20 | - | **-** | 15 | - | POS +$605.3M | - | 400 | 395 | -$18.0M | +$25k bull / -$553k bear | out (clean 29, ADX 12, RVol 0.2) |
| 12 | **SPY** | 771.45 | - | **-** | 14 | - | NEG -$2.3B | 773.53 | 780 | 750 | -$21.0M | +$785k bull / -$1.2M bear | out (clean 29, ADX 9, RVol 0.3) |
| 13 | **AMZN** | 252.70 | - | **-** | 14 | - | POS +$186.2M | 240.14 | 255 | 250 | -$357k | +$26k bull / -$38k bear | out (clean 32, ADX 14, RVol 0.4) |
| 14 | **SHOP** | 168.35 | - | **-** | 13 | - | NEG -$3.3M | 171.97 | 175 | 165 | -$32k | - | out (clean 28, ADX 28, RVol 0.8) |
| 15 | **QQQ** | 722.29 | - | **-** | 12 | - | NEG -$1.7B | 727.64 | 720 | 720 | +$451k | +$666k bull / -$151k bear | out (clean 29, ADX 7, RVol 0.2) |
| 16 | **IWM** | 280.17 | - | **-** | 11 | - | NEG -$336.9M | 281.25 | 280 | 270 | +$9.4M | - | out (clean 24, ADX 15, RVol 0.4) |
| 17 | **ORCL** | 130.42 | - | **-** | 10 | - | POS +$10.2M | 126.88 | 135 | 130 | -$892k | - | out (clean 29, ADX 16, RVol 0.6) |
| 18 | **PLTR** | 193.81 | - | **-** | 9 | - | POS +$35.2M | 189.3 | 200 | 190 | +$141k | - | out (clean 27, ADX 44, RVol 0.4) |
| 19 | **SMCI** | 34.77 | - | **-** | 9 | - | POS +$18.6M | - | 35 | 35 | +$118k | - | out (clean 28, ADX 22, RVol 0.2) |
| 20 | **UBER** | 65.64 | - | **-** | 9 | - | NEG -$26.7M | 68.92 | 70 | 65 | -$36k | - | out (clean 30, ADX 35, RVol 0.5) |
| 21 | **ARM** | 233.00 | - | **-** | 6 | - | POS +$2.2M | 221.37 | 227.5 | 250 | +$52k | - | out (clean 27, ADX 21, RVol 0.7) |
| 22 | **BABA** | 100.35 | - | **-** | 6 | - | NEG -$13.9M | 103.59 | 102 | 100 | +$20k | - | out (clean 28, ADX 17, RVol 0.3) |
| 23 | **NFLX** | 61.84 | - | **-** | 5 | - | NEG -$55.7M | - | 65 | 60 | -$42k | - | out (clean 31, ADX 22, RVol 0.4) |
| 24 | **DELL** | 493.00 | - | **-** | 5 | - | POS +$27.3M | - | 500 | 500 | +$105k | - | out (clean 30, ADX 18, RVol 0.2) |
| 25 | **CRM** | 240.95 | - | **-** | 5 | - | POS +$6.1M | 234.42 | 260 | 240 | +$24k | - | out (clean 27, ADX 16, RVol 0.2) |
| 26 | **COIN** | 158.27 | - | **-** | 4 | - | POS +$1.2M | 155.58 | 170 | 150 | -$18k | - | out (clean 29, ADX 9, RVol 0.4) |
| 27 | **MSTR** | 138.85 | - | **-** | 3 | - | POS +$15.3M | - | 152.5 | 140 | -$8k | - | out (clean 27, ADX 11, RVol 0.4) |

## Big prints this scan (42)
- **SPY** PUT 771 2026-10-28 (0DTE): 955 @ 2.13 = **+$203k** BUY | vol 132,565 / OI 1,490
- **QQQ** CALL 721 2026-10-28 (0DTE): 473 @ 4.00 = **+$189k** BUY | vol 42,453 / OI 752
- **SPY** PUT 767 2026-11-04 (7DTE): 400 @ 4.12 = **+$165k** SELL | vol 13,407 / OI 94
- **SPY** PUT 773 2026-10-28 (0DTE): 501 @ 3.07 = **+$154k** SELL | vol 35,168 / OI 703
- **QQQ** CALL 730 2026-10-30 (2DTE): 500 @ 2.90 = **+$145k** BUY | vol 4,432 / OI 13,989
- **SPY** PUT 767 2026-11-04 (7DTE): 313 @ 4.12 = **+$129k** SELL | vol 13,407 / OI 94
- **SPY** PUT 773 2026-10-28 (0DTE): 389 @ 3.13 = **+$122k** BUY | vol 35,168 / OI 703
- **QQQ** PUT 722 2026-10-28 (0DTE): 382 @ 3.06 = **+$117k** SELL | vol 84,147 / OI 552
- **QQQ** CALL 721 2026-10-29 (1DTE): 192 @ 5.88 = **+$113k** BUY | vol 4,751 / OI 183
- **META** CALL 615 2026-10-28 (0DTE): 400 @ 2.75 = **+$110k** BUY | vol 14,815 / OI 62
- **TSLA** PUT 400 2026-10-28 (0DTE): 800 @ 1.36 = **+$109k** BUY | vol 151,170 / OI 868
- **SPY** PUT 767 2026-11-04 (7DTE): 260 @ 4.12 = **+$107k** SELL | vol 13,407 / OI 94
- **QQQ** CALL 722 2026-10-29 (1DTE): 192 @ 5.32 = **+$102k** BUY | vol 8,650 / OI 328
- **META** CALL 615 2026-10-28 (0DTE): 400 @ 2.49 = **+$100k** MID | vol 14,815 / OI 62
- **MU** CALL 965 2026-10-28 (0DTE): 80 @ 10.70 = **+$86k** BUY | vol 6,905 / OI 281

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 783 2026-10-29 (1DTE): 1,107 traded vs OI 1,088
- **SPY** CALL 772 2026-10-30 (2DTE): 4,584 traded vs OI 4,558
- **SPY** PUT 747 2026-10-28 (0DTE): 671 traded vs OI 628
- **SPY** CALL 770 2026-11-06 (9DTE): 2,604 traded vs OI 2,603
- **SPY** PUT 770 2026-11-09 (12DTE): 502 traded vs OI 104
- **QQQ** PUT 689 2026-10-30 (2DTE): 1,163 traded vs OI 928
- **MSFT** PUT 492.5 2026-10-30 (2DTE): 503 traded vs OI 76
- **UBER** CALL 66 2026-10-30 (2DTE): 1,327 traded vs OI 1,326

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
