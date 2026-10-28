# GEX + FLOW SCAN - Wed Oct 28, 03:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 14:35 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/28 730C | 0.67 | 0.10 | +64% (2m) | **-85%** (done) | -70% | 724.9 hit |
| 14:35 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R2 R5 R6) | 10/29 778C | 0.75 | 0.45 | +43% (2m) | **-40%** (done) | +27% | 772.74 hit |
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
| 1 | **NVDA** | 214.56 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 43 | 10/28 215C @ 0.60 (delta 0.41) = est -92% at 215 | POS +$314.5M | 210.32 | 220 | 215 | +$23.7M | +$804k bull / +$0 bear | out (clean 26, ADX 27, RVol 1.1) |
| 2 | **AMZN** | 254.44 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 42 | 10/28 252.5P @ 0.42 (delta 0.24) = est -40% at 252.5 | POS +$206.0M | 245.06 | 255 | 250 | -$1.6M | +$0 bull / -$226k bear | out (clean 31, ADX 34, RVol 1.5) |
| 3 | **AVGO** | 350.44 | PINNED between the walls (positive gamma) - chop | **-** | 37 | - | POS +$65.3M | 337.32 | 350 | 350 | +$1.9M | +$92k bull / +$0 bear | out (clean 29, ADX 37, RVol 1.3) |
| 4 | **AAPL** | 344.19 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 35 | none: 84 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (48 contracts' greeks worked out here) | POS +$270.0M | 341.82 | 350 | 345 | +$4.0M | +$400k bull / -$132k bear | out (clean 28, ADX 10, RVol 0.9) |
| 5 | **ORCL** | 145.45 | - | **-** | 32 | - | POS +$32.6M | - | 135 | 140 | -$29.0M | +$1.2M bull / -$137k bear | out (clean 30, ADX 60, RVol 2.6) |
| 6 | **CRM** | 240.34 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 25 | none: 19 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$4.3M | 236.13 | 260 | 240 | +$31k | - | out (clean 26, ADX 13, RVol 0.8) |
| 7 | **AMD** | 575.56 | - | **-** | 21 | - | POS +$175.3M | - | 600 | 550 | +$6.4M | +$62k bull / -$686k bear | out (clean 30, ADX 42, RVol 1.1) |
| 8 | **MSTR** | 141.31 | - | **-** | 19 | - | POS +$20.4M | - | 152.5 | 140 | +$1.3M | +$0 bull / -$56k bear | out (clean 26, ADX 27, RVol 0.5) |
| 9 | **QQQ** | 723.11 | - | **-** | 18 | - | NEG -$1.1B | 726.42 | 720 | 720 | +$45.4M | +$525k bull / -$388k bear | out (clean 29, ADX 25, RVol 1.0) |
| 10 | **META** | 610.77 | - | **-** | 18 | - | NEG -$264.4M | 631.95 | 650 | 610 | +$8.5M | +$776k bull / -$240k bear | out (clean 29, ADX 18, RVol 1.0) |
| 11 | **GOOGL** | 324.47 | - | **-** | 18 | - | POS +$15.4M | 320.67 | 355 | 300 | -$321k | +$2.9M bull / -$204k bear | out (clean 32, ADX 21, RVol 2.1) |
| 12 | **ARM** | 233.33 | - | **-** | 18 | - | POS +$2.0M | 222.59 | 227.5 | 250 | +$554k | +$45k bull / +$0 bear | out (clean 26, ADX 22, RVol 0.3) |
| 13 | **SPY** | 770.83 | - | **-** | 17 | - | NEG -$2.0B | 772.67 | 770 | 765 | +$24.9M | +$0 bull / -$2.5M bear | out (clean 28, ADX 21, RVol 1.1) |
| 14 | **MSFT** | 529.05 | - | **-** | 17 | - | POS +$476.6M | - | 550 | 500 | -$894k | +$53k bull / -$407k bear | out (clean 29, ADX 22, RVol 1.3) |
| 15 | **MU** | 980.55 | - | **-** | 17 | - | POS +$624.2M | - | 1,000 | 950 | +$16.4M | +$703k bull / -$3.2M bear | out (clean 29, ADX 23, RVol 0.7) |
| 16 | **TSLA** | 402.38 | - | **-** | 16 | - | POS +$640.7M | - | 400 | 400 | -$3.6M | +$539k bull / -$917k bear | out (clean 30, ADX 27, RVol 0.4) |
| 17 | **NFLX** | 61.79 | - | **-** | 16 | - | NEG -$54.6M | - | 65 | 60 | -$244k | +$0 bull / -$91k bear | out (clean 31, ADX 13, RVol 1.0) |
| 18 | **HOOD** | 91.17 | - | **-** | 13 | - | NEG -$18.2M | - | 100 | 90 | +$4.7M | - | out (clean 29, ADX 13, RVol 1.5) |
| 19 | **IWM** | 280.20 | - | **-** | 10 | - | NEG -$149.8M | 280.66 | 280 | 270 | +$11.4M | - | out (clean 24, ADX 23, RVol 0.8) |
| 20 | **SMH** | 565.78 | - | **-** | 9 | - | POS +$71.2M | 561.21 | 570 | 555 | -$3.1M | - | out (clean 28, ADX 18, RVol 0.5) |
| 21 | **SMCI** | 35.13 | - | **-** | 9 | - | POS +$20.8M | - | 35 | 35 | +$91k | - | out (clean 28, ADX 29, RVol 0.8) |
| 22 | **COIN** | 160.47 | - | **-** | 8 | - | POS +$2.5M | 155.51 | 170 | 150 | -$217k | - | out (clean 27, ADX 16, RVol 0.7) |
| 23 | **DELL** | 492.10 | - | **-** | 7 | - | POS +$28.2M | - | 500 | 500 | +$334k | - | out (clean 31, ADX 20, RVol 0.5) |
| 24 | **UBER** | 65.14 | - | **-** | 7 | - | NEG -$33.6M | - | 70 | 65 | +$56k | - | out (clean 29, ADX 21, RVol 0.9) |
| 25 | **SHOP** | 167.31 | - | **-** | 7 | - | NEG -$4.3M | 171.51 | 175 | 165 | -$21k | - | out (clean 28, ADX 13, RVol 0.8) |
| 26 | **BABA** | 100.67 | - | **-** | 7 | - | NEG -$12.0M | 103.12 | 102 | 100 | +$40k | - | out (clean 28, ADX 24, RVol 0.3) |
| 27 | **PLTR** | 193.91 | - | **-** | 6 | - | POS +$38.8M | 189.83 | 200 | 190 | +$983k | - | out (clean 27, ADX 19, RVol 0.6) |

## Big prints this scan (101)
- **SPY** PUT 775 2026-11-02 (5DTE): 1,000 @ 6.25 = **+$625k** BUY | vol 9,243 / OI 137
- **GOOGL** PUT 322.5 2026-10-30 (2DTE): 597 @ 8.65 = **+$516k** SELL | vol 2,593 / OI 1,055
- **GOOGL** PUT 330 2026-10-30 (2DTE): 306 @ 12.75 = **+$390k** SELL | vol 750 / OI 3,042
- **ORCL** CALL 143 2026-10-30 (2DTE): 500 @ 6.33 = **+$316k** BUY | vol 5,656 / OI 1,673
- **MU** CALL 950 2026-10-28 (0DTE): 100 @ 29.25 = **+$292k** SELL | vol 4,995 / OI 1,527
- **ORCL** CALL 146 2026-10-30 (2DTE): 500 @ 4.48 = **+$224k** BUY | vol 5,314 / OI 0
- **GOOGL** CALL 325 2026-11-02 (5DTE): 198 @ 10.30 = **+$204k** SELL | vol 1,056 / OI 82
- **MU** CALL 960 2026-10-28 (0DTE): 100 @ 19.50 = **+$195k** SELL | vol 9,606 / OI 2,947
- **NVDA** CALL 210 2026-11-04 (7DTE): 200 @ 7.50 = **+$150k** BUY | vol 773 / OI 222
- **ORCL** CALL 150 2026-10-30 (2DTE): 500 @ 2.74 = **+$137k** BUY | vol 34,416 / OI 0
- **META** PUT 625 2026-10-28 (0DTE): 100 @ 13.22 = **+$132k** SELL | vol 975 / OI 1,146
- **MU** CALL 970 2026-10-28 (0DTE): 100 @ 10.40 = **+$104k** SELL | vol 43,261 / OI 3,109
- **AMD** PUT 567.5 2026-11-04 (7DTE): 31 @ 24.10 = **+$75k** BUY | vol 63 / OI 3
- **META** PUT 640 2026-10-28 (0DTE): 25 @ 28.95 = **+$72k** MID | vol 202 / OI 564
- **META** PUT 640 2026-10-28 (0DTE): 25 @ 28.95 = **+$72k** MID | vol 202 / OI 564

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 699 2026-10-30 (2DTE): 891 traded vs OI 786
- **SPY** PUT 709 2026-10-30 (2DTE): 2,603 traded vs OI 948
- **SPY** PUT 740 2026-11-04 (7DTE): 807 traded vs OI 659
- **QQQ** PUT 707 2026-11-13 (16DTE): 1,334 traded vs OI 494
- **IWM** PUT 279 2026-11-09 (12DTE): 866 traded vs OI 16
- **IWM** CALL 285 2026-11-02 (5DTE): 665 traded vs OI 416
- **IWM** CALL 281 2026-11-09 (12DTE): 872 traded vs OI 13
- **NVDA** CALL 215 2026-11-02 (5DTE): 1,417 traded vs OI 1,367
- **NVDA** CALL 210 2026-11-13 (16DTE): 2,285 traded vs OI 927
- **NVDA** PUT 225 2026-11-02 (5DTE): 588 traded vs OI 181
- **NVDA** PUT 222.5 2026-11-02 (5DTE): 537 traded vs OI 154
- **NVDA** PUT 235 2026-11-02 (5DTE): 694 traded vs OI 10
- **AMD** CALL 582.5 2026-10-30 (2DTE): 518 traded vs OI 360
- **META** CALL 625 2026-11-04 (7DTE): 516 traded vs OI 38
- **MSFT** CALL 565 2026-10-30 (2DTE): 3,846 traded vs OI 3,691

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
