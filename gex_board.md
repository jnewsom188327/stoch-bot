# GEX + FLOW SCAN - Wed Nov 04, 09:45 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (1)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.56 | -11% (0m) | **-11%** | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:45:08 ET, last candle SPY 09:44, QQQ 09:44 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **GOOGL** | 290.11 | PINNED between the walls (positive gamma) - chop | **-** | 66 | - | POS +$70.6M | 284.46 | 290 | 290 | -$3.1M | - | LONG (clean 33, ADX 37, RVol 2.2) |
| 2 | **ORCL** | 129.84 | TREND (flow not with it) | **CALLS** | 60 | none: 26 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$23.6M | - | 130 | 125 | -$41k | - | LONG (clean 35, ADX 29, RVol 3.8) |
| 3 | **TSLA** | 382.80 | FLOW SURGE | **PUTS** | 58 | none: 124 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (55 contracts' greeks worked out here) | NEG -$137.7M | 397.16 | 400 | 380 | -$5.6M | +$0 bull / -$42k bear | out (clean 31, ADX 26, RVol 4.1) |
| 4 | **AMZN** | 269.19 | TREND (flow not with it) | **CALLS** | 57 | 11/04 272.5C @ 0.58 (delta 0.23) = est +298% at 274.12 | POS +$529.3M | - | 270 | 250 | -$5.1M | - | LONG (clean 33, ADX 43, RVol 5.1) |
| 5 | **MSFT** | 549.51 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 57 | none: 167 puts 0-7DTE > 13 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (78 contracts' greeks worked out here) | POS +$972.9M | - | 550 | 535 | -$4.8M | - | out (clean 28, ADX 45, RVol 4.4) |
| 6 | **AAPL** | 350.41 | PINNED between the walls (positive gamma) - chop | **-** | 55 | - | POS +$744.3M | 341.77 | 350 | 350 | -$16.3M | - | out (clean 31, ADX 28, RVol 4.2) |
| 7 | **UBER** | 68.83 | FLIP CROSS down into negative gamma | **PUTS** | 55 | 11/06 67P @ 0.63 (delta 0.29) = est +27% at 68.03 | NEG -$1.3M | 69.04 | 70 | 65 | -$24k | - | out (clean 30, ADX 28, RVol 4.6) |
| 8 | **IWM** | 286.04 | TREND (flow not with it) | **CALLS** | 51 | 11/04 287C @ 0.60 (delta 0.35) = est +43% at 287 | POS +$234.6M | 285.18 | 285 | 270 | -$817k | - | LONG (clean 34, ADX 36, RVol 4.7) |
| 9 | **BABA** | 105.76 | TREND (flow not with it) | **CALLS** | 41 | 11/06 110C @ 0.55 (delta 0.20) = est +37% at 106.9 | POS +$16.2M | - | 110 | 100 | +$0 | - | LONG (clean 35, ADX 32, RVol 4.5) |
| 10 | **HOOD** | 86.10 | FLIP CROSS up into positive gamma | **CALLS** | 33 | 11/06 90C @ 0.72 (delta 0.23) = est +31% at 87.22 | POS +$622k | 85.54 | 90 | 85 | -$66k | - | out (clean 29, ADX 18, RVol 2.0) |
| 11 | **AMD** | 507.23 | - | **-** | 32 | - | NEG -$33.0M | - | 510 | 500 | -$2.8M | +$50k bull / +$0 bear | out (clean 32, ADX 27, RVol 7.2) |
| 12 | **META** | 630.51 | - | **-** | 31 | - | POS +$146.8M | 618.94 | 650 | 625 | +$2.7M | - | out (clean 30, ADX 36, RVol 2.5) |
| 13 | **NFLX** | 65.19 | - | **-** | 31 | - | POS +$16.0M | 62.78 | 65 | 65 | -$179k | - | out (clean 29, ADX 39, RVol 3.6) |
| 14 | **CRM** | 230.12 | - | **-** | 31 | - | NEG -$8.0M | 238.53 | 240 | 220 | -$22k | - | out (clean 30, ADX 32, RVol 4.1) |
| 15 | **SPY** | 767.74 | - | **-** | 30 | - | NEG -$2.4B | 770.37 | 770 | 750 | -$19.6M | +$176k bull / +$0 bear | out (clean 30, ADX 28, RVol 3.1) |
| 16 | **ARM** | 207.37 | - | **-** | 28 | - | NEG -$4.4M | - | 212.5 | 200 | -$24k | - | out (clean 26, ADX 26, RVol 1.9) |
| 17 | **COIN** | 148.42 | - | **-** | 27 | - | POS +$30.1M | - | 148 | 150 | -$6k | - | out (clean 30, ADX 21, RVol 2.4) |
| 18 | **PLTR** | 172.09 | - | **-** | 26 | - | NEG -$48.8M | - | 165 | 170 | -$240k | +$0 bull / -$540k bear | out (clean 27, ADX 21, RVol 3.8) |
| 19 | **SMH** | 520.13 | - | **-** | 24 | - | NEG -$361.7M | - | 532.5 | 500 | -$127k | - | out (clean 32, ADX 22, RVol 4.5) |
| 20 | **NVDA** | 206.37 | - | **-** | 24 | - | POS +$122.5M | 203.92 | 210 | 200 | -$1.4M | - | out (clean 29, ADX 31, RVol 4.6) |
| 21 | **SMCI** | 32.55 | - | **-** | 24 | - | POS +$7.4M | - | 34.5 | 30 | -$72k | - | out (clean 33, ADX 14, RVol 4.8) |
| 22 | **DELL** | 387.62 | - | **-** | 23 | - | NEG -$29.8M | - | 400 | 400 | +$22k | - | out (clean 32, ADX 24, RVol 3.3) |
| 23 | **QQQ** | 697.43 | - | **-** | 19 | - | NEG -$4.2B | 722.2 | 700 | 680 | -$12.8M | - | out (clean 29, ADX 24, RVol 4.5) |
| 24 | **AVGO** | 332.84 | - | **-** | 19 | - | NEG -$65.2M | 351.34 | 340 | 330 | +$129k | - | out (clean 30, ADX 20, RVol 3.5) |
| 25 | **SHOP** | 147.51 | - | **-** | 19 | - | NEG -$10.3M | - | 160 | 135 | -$5k | - | out (clean 35, ADX 39, RVol 5.0) |
| 26 | **MSTR** | 140.72 | - | **-** | 17 | - | POS +$126.5M | - | 135 | 140 | +$61k | - | out (clean 29, ADX 25, RVol 2.1) |
| 27 | **MU** | 845.90 | - | **-** | 14 | - | NEG -$255.6M | - | 880 | 850 | +$895k | - | out (clean 31, ADX 20, RVol 2.8) |

## Big prints this scan (0)

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 761 2026-11-04 (0DTE): 2,983 traded vs OI 622
- **SPY** CALL 774 2026-11-05 (1DTE): 778 traded vs OI 0
- **SPY** PUT 747 2026-11-05 (1DTE): 895 traded vs OI 0
- **SPY** CALL 771 2026-11-05 (1DTE): 542 traded vs OI 0
- **SPY** CALL 756 2026-11-04 (0DTE): 1,281 traded vs OI 1,095
- **SPY** CALL 766 2026-11-04 (0DTE): 4,552 traded vs OI 1,133
- **SPY** CALL 769 2026-11-05 (1DTE): 2,212 traded vs OI 0
- **SPY** CALL 768 2026-11-04 (0DTE): 5,593 traded vs OI 1,095
- **SPY** PUT 763 2026-11-04 (0DTE): 3,042 traded vs OI 744
- **SPY** CALL 763 2026-11-05 (1DTE): 2,121 traded vs OI 0
- **SPY** CALL 764 2026-11-04 (0DTE): 3,571 traded vs OI 973
- **SPY** PUT 754 2026-11-05 (1DTE): 1,002 traded vs OI 0
- **SPY** PUT 757 2026-11-04 (0DTE): 10,137 traded vs OI 1,960
- **SPY** PUT 746 2026-11-05 (1DTE): 744 traded vs OI 0
- **SPY** CALL 769 2026-11-04 (0DTE): 2,770 traded vs OI 1,451

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
