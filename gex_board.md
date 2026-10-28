# GEX + FLOW SCAN - Wed Oct 28, 11:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:50 | **IWM** | **CALLS** | FLOW SURGE | 10/30 284C | 0.57 | 0.53 | +7% (2m) | **-7%** | +22% | 280.64 |
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.30 | +11% (0m) | **-36%** | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **HOOD** | 91.80 | FLOW SURGE | **CALLS** | 50 | none: 18 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$16.1M | - | 100 | 90 | +$2.1M | +$179k bull / -$49k bear | out (clean 30, ADX 38, RVol 2.1) |
| 2 | **META** | 612.18 | FLOW SURGE | **CALLS** | 48 | none: 179 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (75 contracts' greeks worked out here) | NEG -$260.4M | 634.73 | 650 | 610 | +$13.5M | +$683k bull / -$112k bear | out (clean 29, ADX 32, RVol 1.6) |
| 3 | **GOOGL** | 323.17 | FLOW SURGE | **CALLS** | 45 | none: 78 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$13.4M | 320.74 | 355 | 300 | +$3.0M | +$160k bull / +$0 bear | out (clean 33, ADX 22, RVol 2.0) |
| 4 | **IWM** | 279.79 | FLOW SURGE | **CALLS** | 42 | 10/30 283C @ 0.74 (delta 0.26) = est +2% at 280 | NEG -$495.6M | 281.4 | 280 | 270 | +$11.1M | +$51k bull / +$0 bear | out (clean 24, ADX 20, RVol 1.0) |
| 5 | **AAPL** | 345.46 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 39 | 10/28 347.5C @ 0.40 (delta 0.24) = est +135% at 347.5 | POS +$354.6M | 341.18 | 350 | 345 | -$392k | +$45k bull / -$53k bear | out (clean 30, ADX 28, RVol 1.1) |
| 6 | **TSLA** | 400.56 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 38 | none: 128 puts 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (62 contracts' greeks worked out here) | POS +$568.3M | - | 400 | 395 | -$4.8M | +$0 bull / -$545k bear | out (clean 28, ADX 32, RVol 0.8) |
| 7 | **AMZN** | 252.05 | FLOW SURGE | **CALLS** | 35 | none: 80 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (33 contracts' greeks worked out here) | POS +$179.8M | 237.53 | 250 | 250 | +$4.1M | +$806k bull / +$0 bear | out (clean 32, ADX 19, RVol 0.8) |
| 8 | **PLTR** | 194.86 | - | **-** | 26 | - | POS +$49.2M | 188.89 | 200 | 190 | -$1.2M | +$82k bull / +$0 bear | out (clean 28, ADX 52, RVol 0.6) |
| 9 | **ORCL** | 130.07 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 25 | none: 26 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$9.6M | 126.59 | 135 | 130 | +$59k | - | out (clean 28, ADX 14, RVol 0.9) |
| 10 | **MSFT** | 527.84 | - | **-** | 24 | - | POS +$458.0M | - | 550 | 500 | +$1.3M | +$109k bull / +$0 bear | out (clean 30, ADX 20, RVol 1.2) |
| 11 | **DELL** | 492.32 | - | **-** | 24 | - | POS +$28.3M | - | 500 | 500 | +$277k | +$25k bull / +$0 bear | out (clean 30, ADX 29, RVol 1.2) |
| 12 | **CRM** | 240.75 | - | **-** | 24 | - | POS +$4.7M | 235.46 | 260 | 240 | +$60k | - | out (clean 27, ADX 18, RVol 1.9) |
| 13 | **SHOP** | 165.87 | - | **-** | 24 | - | NEG -$5.8M | 172.69 | 175 | 165 | +$21k | - | out (clean 26, ADX 21, RVol 0.9) |
| 14 | **AVGO** | 344.57 | - | **-** | 23 | - | POS +$41.0M | 336.98 | 350 | 340 | +$1.8M | +$53k bull / +$0 bear | out (clean 30, ADX 18, RVol 0.8) |
| 15 | **SMH** | 563.49 | - | **-** | 21 | - | POS +$38.2M | 560.09 | 570 | 555 | +$371k | +$0 bull / -$119k bear | out (clean 29, ADX 28, RVol 0.5) |
| 16 | **MU** | 968.78 | - | **-** | 21 | - | POS +$600.3M | - | 950 | 950 | +$20.7M | +$1.9M bull / -$2.2M bear | out (clean 28, ADX 34, RVol 0.5) |
| 17 | **COIN** | 158.30 | - | **-** | 20 | - | POS +$1.2M | 155.33 | 170 | 150 | -$43k | +$0 bull / -$81k bear | out (clean 30, ADX 20, RVol 0.9) |
| 18 | **NVDA** | 217.57 | - | **-** | 18 | - | POS +$560.1M | 209.82 | 220 | 215 | +$4.1M | +$489k bull / +$0 bear | out (clean 27, ADX 11, RVol 0.7) |
| 19 | **SPY** | 770.26 | - | **-** | 17 | - | NEG -$3.3B | 773.55 | 780 | 750 | +$22.8M | +$2.2M bull / +$0 bear | out (clean 30, ADX 15, RVol 0.6) |
| 20 | **AMD** | 563.39 | - | **-** | 17 | - | POS +$171.0M | - | 550 | 550 | +$1.5M | +$0 bull / -$867k bear | out (clean 28, ADX 20, RVol 0.6) |
| 21 | **BABA** | 100.10 | - | **-** | 16 | - | NEG -$14.5M | 103.64 | 102 | 100 | +$48k | - | out (clean 28, ADX 22, RVol 0.6) |
| 22 | **UBER** | 64.82 | - | **-** | 15 | - | NEG -$34.0M | - | 70 | 65 | +$53k | - | out (clean 28, ADX 40, RVol 0.8) |
| 23 | **SMCI** | 34.74 | - | **-** | 13 | - | POS +$18.6M | - | 35 | 35 | +$142k | - | out (clean 28, ADX 18, RVol 0.5) |
| 24 | **ARM** | 232.39 | - | **-** | 11 | - | POS +$1.8M | 222.59 | 220 | 250 | +$147k | - | out (clean 26, ADX 28, RVol 0.6) |
| 25 | **NFLX** | 61.73 | - | **-** | 10 | - | NEG -$56.6M | - | 65 | 60 | +$29k | - | out (clean 32, ADX 47, RVol 0.5) |
| 26 | **QQQ** | 721.16 | - | **-** | 6 | - | NEG -$2.0B | 727.94 | 720 | 720 | +$13.1M | - | out (clean 31, ADX 14, RVol 0.5) |
| 27 | **MSTR** | 139.54 | - | **-** | 3 | - | POS +$17.2M | - | 152.5 | 140 | -$78k | - | out (clean 29, ADX 9, RVol 0.3) |

## Big prints this scan (93)
- **MU** CALL 950 2026-10-28 (0DTE): 128 @ 20.74 = **+$265k** SELL | vol 2,987 / OI 1,527
- **SPY** PUT 773 2026-10-28 (0DTE): 700 @ 3.62 = **+$253k** SELL | vol 18,405 / OI 703
- **SPY** PUT 770 2026-10-28 (0DTE): 1,000 @ 2.05 = **+$205k** SELL | vol 127,870 / OI 1,789
- **META** CALL 625 2026-11-04 (7DTE): 211 @ 9.05 = **+$191k** MID | vol 454 / OI 38
- **SPY** PUT 773 2026-10-28 (0DTE): 500 @ 3.78 = **+$189k** SELL | vol 18,405 / OI 703
- **SPY** PUT 773 2026-10-28 (0DTE): 445 @ 3.76 = **+$167k** SELL | vol 18,405 / OI 703
- **MU** CALL 960 2026-10-28 (0DTE): 128 @ 13.01 = **+$167k** SELL | vol 6,094 / OI 2,947
- **MU** PUT 1,000 2026-10-30 (2DTE): 39 @ 39.60 = **+$154k** BUY | vol 363 / OI 1,100
- **AMD** PUT 560 2026-11-04 (7DTE): 60 @ 23.36 = **+$140k** BUY | vol 171 / OI 31
- **AMD** PUT 557.5 2026-11-04 (7DTE): 60 @ 22.00 = **+$132k** MID | vol 152 / OI 8
- **AMD** PUT 560 2026-11-04 (7DTE): 43 @ 23.36 = **+$100k** BUY | vol 171 / OI 31
- **AMD** PUT 560 2026-11-04 (7DTE): 43 @ 23.36 = **+$100k** BUY | vol 171 / OI 31
- **AMD** PUT 557.5 2026-11-04 (7DTE): 43 @ 22.00 = **+$95k** MID | vol 152 / OI 8
- **AMD** PUT 557.5 2026-11-04 (7DTE): 43 @ 22.00 = **+$95k** MID | vol 152 / OI 8
- **MU** CALL 970 2026-10-28 (0DTE): 128 @ 7.01 = **+$90k** BUY | vol 16,138 / OI 3,109

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 795 2026-11-04 (7DTE): 609 traded vs OI 307
- **QQQ** CALL 736 2026-10-29 (1DTE): 517 traded vs OI 294
- **IWM** PUT 275 2026-10-29 (1DTE): 501 traded vs OI 479
- **IWM** CALL 279 2026-11-04 (7DTE): 528 traded vs OI 146
- **SMH** PUT 550 2026-10-28 (0DTE): 500 traded vs OI 75
- **TSLA** CALL 410 2026-11-06 (9DTE): 1,575 traded vs OI 1,555
- **TSLA** PUT 390 2026-11-06 (9DTE): 1,147 traded vs OI 1,094
- **META** PUT 590 2026-10-28 (0DTE): 542 traded vs OI 522
- **META** PUT 615 2026-10-30 (2DTE): 1,174 traded vs OI 1,074
- **AMZN** CALL 275 2026-11-04 (7DTE): 687 traded vs OI 67
- **AMZN** PUT 237.5 2026-10-30 (2DTE): 774 traded vs OI 727
- **GOOGL** CALL 350 2026-11-04 (7DTE): 1,151 traded vs OI 156
- **NFLX** CALL 64 2026-10-30 (2DTE): 5,679 traded vs OI 5,616
- **AVGO** CALL 362.5 2026-10-30 (2DTE): 806 traded vs OI 797
- **SMCI** CALL 35.5 2026-10-30 (2DTE): 2,278 traded vs OI 2,213

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
