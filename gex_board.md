# GEX + FLOW SCAN - Wed Oct 28, 10:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:50 | **IWM** | **CALLS** | FLOW SURGE | 10/30 284C | 0.57 | 0.56 | -2% (0m) | **-2%** | +22% | 280.64 |
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.35 | +11% (0m) | **-26%** | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 279.93 | FLOW SURGE | **CALLS** | 46 | 10/30 284C @ 0.57 (delta 0.21) = est +22% at 280.64 | NEG -$410.9M | 281.43 | 280 | 270 | +$10.0M | +$3.8M bull / +$0 bear | out (clean 24, ADX 19, RVol 1.4) |
| 2 | **META** | 612.12 | FLOW SURGE | **CALLS** | 44 | none: 179 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (72 contracts' greeks worked out here) | NEG -$256.5M | 635.34 | 650 | 610 | +$9.2M | +$511k bull / +$0 bear | out (clean 28, ADX 29, RVol 1.1) |
| 3 | **AAPL** | 344.72 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 38 | none: 81 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (48 contracts' greeks worked out here) | POS +$295.7M | 341.04 | 350 | 345 | +$330k | +$45k bull / -$82k bear | out (clean 30, ADX 31, RVol 0.9) |
| 4 | **TSLA** | 400.02 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 36 | none: 128 puts 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (59 contracts' greeks worked out here) | POS +$555.4M | - | 400 | 395 | -$1.4M | +$38k bull / -$1.2M bear | out (clean 28, ADX 34, RVol 0.7) |
| 5 | **MSTR** | 139.99 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 32 | none: 26 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$17.7M | - | 152.5 | 140 | -$168k | +$0 bull / -$35k bear | out (clean 29, ADX 10, RVol 0.3) |
| 6 | **HOOD** | 91.95 | - | **-** | 32 | - | NEG -$16.1M | - | 100 | 90 | +$1.3M | +$0 bull / -$25k bear | out (clean 31, ADX 41, RVol 1.8) |
| 7 | **GOOGL** | 323.63 | - | **-** | 31 | - | POS +$12.3M | 321.1 | 355 | 300 | +$2.5M | +$37k bull / -$65k bear | out (clean 33, ADX 25, RVol 1.7) |
| 8 | **ORCL** | 130.18 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 28 | none: 26 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$8.8M | 126.73 | 135 | 130 | -$92k | - | out (clean 28, ADX 12, RVol 1.0) |
| 9 | **SMCI** | 34.97 | PINNED between the walls (positive gamma) - chop | **-** | 24 | - | POS +$18.9M | - | 35 | 35 | +$126k | - | out (clean 27, ADX 16, RVol 0.5) |
| 10 | **ARM** | 232.23 | - | **-** | 24 | - | POS +$1.7M | 223.49 | 227.5 | 250 | +$205k | +$32k bull / +$0 bear | out (clean 26, ADX 29, RVol 0.7) |
| 11 | **MU** | 969.59 | - | **-** | 23 | - | POS +$598.5M | - | 950 | 900 | +$23.6M | +$4.3M bull / -$812k bear | out (clean 28, ADX 35, RVol 0.6) |
| 12 | **MSFT** | 528.61 | - | **-** | 22 | - | POS +$456.0M | - | 550 | 500 | +$1.0M | +$255k bull / -$1.2M bear | out (clean 30, ADX 18, RVol 1.2) |
| 13 | **AVGO** | 345.53 | - | **-** | 22 | - | POS +$53.0M | 335.87 | 350 | 340 | +$1.3M | +$60k bull / +$0 bear | out (clean 30, ADX 20, RVol 1.0) |
| 14 | **DELL** | 494.43 | - | **-** | 22 | - | POS +$28.4M | - | 500 | 500 | +$225k | +$29k bull / +$0 bear | out (clean 30, ADX 28, RVol 0.9) |
| 15 | **UBER** | 64.72 | - | **-** | 22 | - | NEG -$35.4M | - | 70 | 65 | +$82k | - | out (clean 27, ADX 39, RVol 0.8) |
| 16 | **CRM** | 241.11 | - | **-** | 22 | - | POS +$5.3M | 234.84 | 260 | 240 | +$60k | - | out (clean 27, ADX 16, RVol 1.0) |
| 17 | **SHOP** | 166.14 | - | **-** | 22 | - | NEG -$5.7M | 172.67 | 175 | 165 | +$15k | - | out (clean 26, ADX 18, RVol 0.8) |
| 18 | **SMH** | 564.00 | - | **-** | 21 | - | POS +$43.8M | 559.71 | 570 | 555 | +$294k | +$28k bull / +$0 bear | out (clean 29, ADX 31, RVol 0.5) |
| 19 | **AMZN** | 252.69 | - | **-** | 21 | - | POS +$176.0M | 243.64 | 255 | 250 | +$1.2M | +$555k bull / -$40k bear | out (clean 32, ADX 18, RVol 0.7) |
| 20 | **PLTR** | 195.35 | - | **-** | 21 | - | POS +$49.9M | 188.92 | 200 | 190 | -$1.8M | - | out (clean 28, ADX 51, RVol 0.8) |
| 21 | **AMD** | 563.44 | - | **-** | 19 | - | POS +$174.3M | - | 550 | 550 | +$2.4M | +$66k bull / -$329k bear | out (clean 29, ADX 20, RVol 0.5) |
| 22 | **NVDA** | 217.77 | - | **-** | 16 | - | POS +$577.1M | 209.89 | 220 | 215 | +$2.1M | +$737k bull / -$33k bear | out (clean 27, ADX 12, RVol 0.7) |
| 23 | **SPY** | 770.20 | - | **-** | 15 | - | NEG -$3.3B | 773.51 | 780 | 750 | +$7.9M | +$1.8M bull / -$408k bear | out (clean 30, ADX 14, RVol 0.6) |
| 24 | **QQQ** | 721.38 | - | **-** | 15 | - | NEG -$2.0B | 728.01 | 720 | 720 | +$5.3M | +$353k bull / -$330k bear | out (clean 30, ADX 14, RVol 0.6) |
| 25 | **BABA** | 100.17 | - | **-** | 12 | - | NEG -$14.2M | 103.38 | 102 | 100 | +$17k | - | out (clean 29, ADX 25, RVol 0.6) |
| 26 | **NFLX** | 61.69 | - | **-** | 10 | - | NEG -$56.2M | - | 65 | 60 | +$39k | - | out (clean 32, ADX 45, RVol 0.5) |
| 27 | **COIN** | 158.73 | - | **-** | 10 | - | POS +$1.8M | 154.77 | 170 | 150 | -$37k | - | out (clean 30, ADX 21, RVol 1.0) |

## Big prints this scan (53)
- **AMZN** CALL 247.5 2026-10-30 (2DTE): 279 @ 13.08 = **+$365k** BUY | vol 350 / OI 2,411
- **SPY** PUT 775 2026-10-30 (2DTE): 450 @ 6.00 = **+$270k** SELL | vol 860 / OI 3,175
- **SPY** PUT 770 2026-10-28 (0DTE): 1,002 @ 1.85 = **+$185k** SELL | vol 111,614 / OI 1,789
- **SPY** PUT 770 2026-10-28 (0DTE): 1,000 @ 1.83 = **+$183k** SELL | vol 111,614 / OI 1,789
- **MU** CALL 945 2026-10-28 (0DTE): 48 @ 26.20 = **+$126k** BUY | vol 515 / OI 660
- **SPY** PUT 770 2026-10-29 (1DTE): 420 @ 2.97 = **+$125k** SELL | vol 17,222 / OI 727
- **SPY** CALL 770 2026-11-02 (5DTE): 200 @ 5.56 = **+$111k** BUY | vol 2,027 / OI 934
- **SPY** CALL 770 2026-11-02 (5DTE): 200 @ 5.47 = **+$109k** BUY | vol 2,027 / OI 934
- **SPY** CALL 770 2026-11-02 (5DTE): 200 @ 5.44 = **+$109k** BUY | vol 2,027 / OI 934
- **MU** CALL 1,010 2026-10-30 (2DTE): 116 @ 6.40 = **+$74k** BUY | vol 1,533 / OI 1,578
- **MU** CALL 1,010 2026-10-30 (2DTE): 100 @ 6.90 = **+$69k** BUY | vol 1,533 / OI 1,578
- **TSLA** PUT 395 2026-10-30 (2DTE): 182 @ 3.71 = **+$68k** BUY | vol 7,959 / OI 2,798
- **TSLA** PUT 395 2026-10-30 (2DTE): 182 @ 3.71 = **+$68k** BUY | vol 7,959 / OI 2,798
- **MU** PUT 965 2026-10-28 (0DTE): 100 @ 6.50 = **+$65k** BUY | vol 8,497 / OI 17
- **NVDA** CALL 220 2026-10-30 (2DTE): 294 @ 2.11 = **+$62k** BUY | vol 21,847 / OI 53,027

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 742 2026-10-28 (0DTE): 763 traded vs OI 715
- **SPY** PUT 770 2026-11-04 (7DTE): 501 traded vs OI 420
- **QQQ** PUT 700 2026-10-28 (0DTE): 3,584 traded vs OI 3,519
- **IWM** PUT 277 2026-10-29 (1DTE): 503 traded vs OI 386
- **SMH** CALL 580 2026-10-28 (0DTE): 582 traded vs OI 194
- **NVDA** CALL 222.5 2026-11-04 (7DTE): 521 traded vs OI 139
- **NVDA** CALL 202.5 2026-10-30 (2DTE): 718 traded vs OI 668
- **TSLA** CALL 440 2026-11-06 (9DTE): 871 traded vs OI 0
- **TSLA** CALL 440 2026-10-28 (0DTE): 800 traded vs OI 0
- **TSLA** CALL 420 2026-11-02 (5DTE): 994 traded vs OI 975
- **TSLA** CALL 432.5 2026-10-28 (0DTE): 875 traded vs OI 652
- **AMD** CALL 570 2026-10-30 (2DTE): 1,656 traded vs OI 1,640
- **META** CALL 620 2026-11-06 (9DTE): 503 traded vs OI 28
- **MSFT** CALL 577.5 2026-10-30 (2DTE): 538 traded vs OI 179
- **MU** CALL 970 2026-11-02 (5DTE): 502 traded vs OI 191

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
