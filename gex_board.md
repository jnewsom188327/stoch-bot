# GEX + FLOW SCAN - Wed Oct 28, 02:10 PM ET
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
| 1 | **AAPL** | 345.26 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 35 | none: 81 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (49 contracts' greeks worked out here) | POS +$353.5M | 341.43 | 350 | 345 | +$1.1M | +$60k bull / -$44k bear | out (clean 28, ADX 14, RVol 1.0) |
| 2 | **ORCL** | 129.71 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 24 | none: 26 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$8.6M | 126.96 | 135 | 130 | -$823k | - | out (clean 29, ADX 14, RVol 0.4) |
| 3 | **IWM** | 279.77 | - | **-** | 23 | - | NEG -$456.1M | 281.05 | 280 | 270 | +$10.8M | +$411k bull / +$0 bear | out (clean 24, ADX 29, RVol 0.6) |
| 4 | **HOOD** | 90.52 | - | **-** | 22 | - | NEG -$17.7M | - | 95 | 90 | +$4.0M | +$0 bull / -$36k bear | out (clean 30, ADX 15, RVol 0.6) |
| 5 | **META** | 610.59 | - | **-** | 19 | - | NEG -$266.8M | 635.38 | 650 | 610 | +$9.2M | +$308k bull / +$0 bear | out (clean 28, ADX 20, RVol 0.8) |
| 6 | **PLTR** | 193.71 | - | **-** | 19 | - | POS +$36.1M | 189.54 | 200 | 190 | +$429k | +$56k bull / +$0 bear | out (clean 27, ADX 37, RVol 0.7) |
| 7 | **AMD** | 569.36 | - | **-** | 18 | - | POS +$182.1M | - | 600 | 550 | +$5.1M | +$0 bull / -$333k bear | out (clean 29, ADX 28, RVol 0.8) |
| 8 | **NVDA** | 216.67 | - | **-** | 17 | - | POS +$502.4M | 210.25 | 220 | 215 | +$9.2M | +$188k bull / +$0 bear | out (clean 26, ADX 16, RVol 0.7) |
| 9 | **MSTR** | 139.48 | - | **-** | 17 | - | POS +$16.7M | - | 152.5 | 140 | +$826k | +$27k bull / -$29k bear | out (clean 27, ADX 13, RVol 0.5) |
| 10 | **TSLA** | 402.13 | - | **-** | 16 | - | POS +$624.7M | - | 400 | 400 | -$17.3M | +$580k bull / -$378k bear | out (clean 29, ADX 16, RVol 0.3) |
| 11 | **AMZN** | 252.35 | - | **-** | 16 | - | POS +$178.5M | 242.29 | 250 | 250 | +$2.8M | +$28k bull / +$0 bear | out (clean 31, ADX 15, RVol 0.7) |
| 12 | **MSFT** | 527.02 | - | **-** | 16 | - | POS +$434.6M | - | 550 | 500 | -$992k | +$2.2M bull / +$0 bear | out (clean 29, ADX 13, RVol 1.3) |
| 13 | **GOOGL** | 323.52 | - | **-** | 16 | - | POS +$12.2M | 321.15 | 355 | 300 | -$426k | +$535k bull / +$0 bear | out (clean 32, ADX 24, RVol 0.8) |
| 14 | **AVGO** | 347.84 | - | **-** | 16 | - | POS +$61.7M | 337.5 | 350 | 340 | -$134k | +$31k bull / -$56k bear | out (clean 29, ADX 27, RVol 0.5) |
| 15 | **MU** | 968.66 | - | **-** | 16 | - | POS +$630.8M | - | 950 | 950 | +$19.0M | +$1.6M bull / -$1.9M bear | out (clean 28, ADX 19, RVol 0.5) |
| 16 | **SPY** | 770.51 | - | **-** | 14 | - | NEG -$3.0B | 773.35 | 780 | 750 | -$4.4M | +$325k bull / +$0 bear | out (clean 28, ADX 13, RVol 0.5) |
| 17 | **QQQ** | 721.60 | - | **-** | 14 | - | NEG -$1.9B | 727.59 | 720 | 720 | +$12.2M | +$0 bull / -$487k bear | out (clean 29, ADX 12, RVol 0.4) |
| 18 | **SMH** | 564.36 | - | **-** | 13 | - | POS +$58.8M | 559.16 | 570 | 555 | -$3.8M | - | out (clean 28, ADX 18, RVol 0.9) |
| 19 | **SHOP** | 167.62 | - | **-** | 11 | - | NEG -$4.2M | 172.1 | 175 | 165 | -$30k | - | out (clean 29, ADX 26, RVol 0.4) |
| 20 | **BABA** | 99.86 | - | **-** | 9 | - | NEG -$15.2M | 102.77 | 102 | 100 | +$69k | - | out (clean 28, ADX 16, RVol 0.6) |
| 21 | **SMCI** | 34.73 | - | **-** | 8 | - | POS +$19.1M | - | 35 | 35 | +$134k | - | out (clean 28, ADX 17, RVol 0.5) |
| 22 | **UBER** | 65.44 | - | **-** | 6 | - | NEG -$31.1M | 69.25 | 70 | 65 | +$20k | - | out (clean 30, ADX 23, RVol 0.6) |
| 23 | **COIN** | 158.89 | - | **-** | 5 | - | POS +$1.5M | 155.49 | 170 | 150 | +$20k | - | out (clean 29, ADX 10, RVol 1.3) |
| 24 | **ARM** | 231.69 | - | **-** | 5 | - | POS +$2.0M | 221.44 | 227.5 | 240 | +$97k | - | out (clean 26, ADX 14, RVol 0.4) |
| 25 | **CRM** | 241.02 | - | **-** | 5 | - | POS +$6.7M | 234.35 | 260 | 240 | +$25k | - | out (clean 27, ADX 14, RVol 0.7) |
| 26 | **NFLX** | 61.69 | - | **-** | 4 | - | NEG -$56.0M | - | 64 | 60 | -$51k | - | out (clean 31, ADX 13, RVol 0.7) |
| 27 | **DELL** | 492.68 | - | **-** | 4 | - | POS +$27.9M | - | 500 | 500 | +$165k | - | out (clean 30, ADX 11, RVol 0.3) |

## Big prints this scan (51)
- **MU** PUT 990 2026-10-28 (0DTE): 243 @ 20.58 = **+$500k** SELL | vol 3,417 / OI 19
- **MU** PUT 985 2026-10-28 (0DTE): 243 @ 16.08 = **+$391k** SELL | vol 3,220 / OI 25
- **MU** CALL 955 2026-10-28 (0DTE): 145 @ 15.00 = **+$218k** SELL | vol 3,143 / OI 340
- **SPY** PUT 775 2026-11-02 (5DTE): 350 @ 6.15 = **+$215k** SELL | vol 1,125 / OI 137
- **MU** CALL 955 2026-10-28 (0DTE): 100 @ 16.25 = **+$162k** BUY | vol 3,143 / OI 340
- **MSFT** CALL 530 2026-10-30 (2DTE): 96 @ 11.80 = **+$113k** BUY | vol 3,704 / OI 7,642
- **MU** CALL 960 2026-10-28 (0DTE): 85 @ 11.96 = **+$102k** BUY | vol 8,375 / OI 2,947
- **MU** PUT 990 2026-10-28 (0DTE): 42 @ 20.63 = **+$87k** SELL | vol 3,417 / OI 19
- **TSLA** CALL 402.5 2026-10-30 (2DTE): 150 @ 5.55 = **+$83k** BUY | vol 9,532 / OI 2,094
- **META** PUT 630 2026-10-28 (0DTE): 45 @ 18.20 = **+$82k** SELL | vol 715 / OI 757
- **NVDA** CALL 217.5 2026-10-28 (0DTE): 1,000 @ 0.80 = **+$80k** BUY | vol 109,865 / OI 7,446
- **MU** PUT 965 2026-10-28 (0DTE): 200 @ 3.75 = **+$75k** MID | vol 28,418 / OI 17
- **TSLA** CALL 410 2026-10-30 (2DTE): 292 @ 2.36 = **+$69k** BUY | vol 19,126 / OI 7,751
- **MU** PUT 985 2026-10-28 (0DTE): 42 @ 16.13 = **+$68k** SELL | vol 3,220 / OI 25
- **TSLA** CALL 397.5 2026-10-28 (0DTE): 125 @ 5.40 = **+$68k** BUY | vol 20,582 / OI 2,326

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 775 2026-11-02 (5DTE): 1,125 traded vs OI 137
- **QQQ** PUT 724 2026-10-30 (2DTE): 869 traded vs OI 847
- **IWM** PUT 277 2026-11-03 (6DTE): 722 traded vs OI 147
- **NVDA** PUT 195 2026-11-20 (23DTE): 1,261 traded vs OI 0
- **NVDA** PUT 195 2026-10-30 (2DTE): 1,897 traded vs OI 0
- **NVDA** PUT 195 2026-11-06 (9DTE): 559 traded vs OI 0
- **AAPL** PUT 347.5 2026-11-20 (23DTE): 584 traded vs OI 537
- **META** CALL 645 2026-10-30 (2DTE): 1,222 traded vs OI 1,191
- **MU** CALL 1,065 2026-10-30 (2DTE): 508 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
