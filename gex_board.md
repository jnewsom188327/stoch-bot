# GEX + FLOW SCAN - Thu Oct 29, 09:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (1)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.49 | -2% (0m) | **-2%** | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:50:08 ET, last candle SPY 09:49, QQQ 09:49 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 529.50 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 64 | none: 126 calls 0-7DTE > 16 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (14 contracts' greeks worked out here) | POS +$566.2M | - | 525 | 530 | +$8.5M | +$1.5M bull / -$725k bear | out (clean 29, ADX 38, RVol 7.5) |
| 2 | **AVGO** | 340.64 | FLOW SURGE | **CALLS** | 64 | none: 81 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (14 contracts' greeks worked out here) | NEG -$19.8M | 342.71 | 350 | 340 | +$2.1M | +$142k bull / +$0 bear | out (clean 29, ADX 40, RVol 3.5) |
| 3 | **MSTR** | 139.86 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 62 | none: 26 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$23.0M | - | 152.5 | 140 | -$534k | +$165k bull / +$0 bear | out (clean 26, ADX 27, RVol 4.3) |
| 4 | **MU** | 946.89 | FLOW SURGE | **CALLS** | 60 | none: 120 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | POS +$335.0M | - | 950 | 950 | +$19.4M | +$5.6M bull / +$0 bear | out (clean 29, ADX 33, RVol 3.5) |
| 5 | **IWM** | 283.83 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 57 | 10/29 283P @ 0.50 (delta 0.35) = est +159% at 282 | POS +$686.2M | 281.61 | 284 | 270 | -$769k | +$0 bull / -$53k bear | out (clean 24, ADX 39, RVol 3.2) |
| 6 | **AAPL** | 348.85 | FLOW SURGE | **CALLS** | 55 | none: 55 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (14 contracts' greeks worked out here) | POS +$583.9M | 338.57 | 350 | 345 | +$11.6M | +$5.4M bull / -$246k bear | out (clean 28, ADX 24, RVol 3.6) |
| 7 | **ORCL** | 140.24 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 54 | none: 25 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$108.4M | - | 135 | 140 | -$37k | +$102k bull / +$0 bear | out (clean 31, ADX 45, RVol 4.7) |
| 8 | **SMH** | 557.34 | FLOW SURGE | **CALLS** | 53 | none: 135 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (22 contracts' greeks worked out here) | NEG -$89.1M | 563.39 | 560 | 555 | +$293k | +$87k bull / +$0 bear | out (clean 28, ADX 25, RVol 3.2) |
| 9 | **SHOP** | 166.29 | FLOW SURGE | **PUTS** | 51 | none: 14 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$5.9M | 172.28 | 175 | 165 | -$34k | +$0 bull / -$29k bear | out (clean 27, ADX 21, RVol 1.9) |
| 10 | **DELL** | 487.83 | FLOW SURGE | **PUTS** | 45 | none: 39 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | POS +$11.0M | 476.31 | 500 | 500 | -$916k | +$0 bull / -$171k bear | out (clean 31, ADX 28, RVol 1.7) |
| 11 | **AMZN** | 244.80 | - | **-** | 36 | - | POS +$7.4M | 242.14 | 265 | 250 | -$2.4M | +$547k bull / +$0 bear | out (clean 32, ADX 46, RVol 7.7) |
| 12 | **SPY** | 767.71 | - | **-** | 35 | - | NEG -$5.6B | 772.87 | 770 | 765 | -$29.2M | +$1.5M bull / +$0 bear | out (clean 28, ADX 24, RVol 4.4) |
| 13 | **META** | 618.31 | - | **-** | 35 | - | NEG -$117.3M | 630.32 | 650 | 625 | -$6.4M | +$520k bull / -$364k bear | out (clean 28, ADX 28, RVol 2.0) |
| 14 | **QQQ** | 712.78 | - | **-** | 33 | - | NEG -$5.3B | 726.77 | 720 | 700 | -$36.3M | +$2.2M bull / -$656k bear | out (clean 29, ADX 32, RVol 3.3) |
| 15 | **NVDA** | 213.15 | - | **-** | 28 | - | POS +$196.1M | 210.53 | 215 | 210 | -$2.0M | +$425k bull / -$272k bear | out (clean 26, ADX 32, RVol 3.0) |
| 16 | **GOOGL** | 283.26 | - | **-** | 28 | - | NEG -$187.3M | - | 300 | 290 | -$3.0M | +$500k bull / -$367k bear | out (clean 33, ADX 37, RVol 14.0) |
| 17 | **NFLX** | 61.85 | - | **-** | 28 | - | NEG -$52.6M | - | 63 | 60 | -$99k | +$30k bull / +$0 bear | out (clean 31, ADX 29, RVol 2.3) |
| 18 | **PLTR** | 195.28 | - | **-** | 28 | - | POS +$44.9M | 190.67 | 200 | 190 | -$941k | +$0 bull / -$93k bear | out (clean 26, ADX 20, RVol 3.5) |
| 19 | **ARM** | 226.13 | - | **-** | 28 | - | POS +$2.0M | 223.45 | 227.5 | 220 | +$46k | - | out (clean 26, ADX 28, RVol 4.2) |
| 20 | **TSLA** | 402.82 | - | **-** | 27 | - | POS +$449.6M | - | 400 | 400 | -$5.5M | +$2.0M bull / -$29k bear | out (clean 29, ADX 28, RVol 1.9) |
| 21 | **AMD** | 566.06 | - | **-** | 26 | - | POS +$135.4M | - | 600 | 550 | +$1.1M | +$546k bull / -$935k bear | out (clean 30, ADX 41, RVol 2.8) |
| 22 | **COIN** | 160.84 | - | **-** | 26 | - | POS +$5.3M | 152.41 | 170 | 155 | -$42k | - | out (clean 27, ADX 20, RVol 4.1) |
| 23 | **BABA** | 99.56 | - | **-** | 26 | - | NEG -$19.4M | 102.02 | 102 | 100 | -$19k | - | out (clean 28, ADX 30, RVol 3.1) |
| 24 | **HOOD** | 90.18 | - | **-** | 25 | - | NEG -$25.7M | - | 95 | 90 | -$694k | - | out (clean 29, ADX 17, RVol 3.0) |
| 25 | **SMCI** | 35.18 | - | **-** | 23 | - | POS +$24.1M | - | 35 | 35 | +$51k | - | out (clean 28, ADX 28, RVol 2.3) |
| 26 | **CRM** | 231.01 | - | **-** | 21 | - | NEG -$18.2M | - | 240 | 230 | -$53k | - | out (clean 27, ADX 26, RVol 5.2) |
| 27 | **UBER** | 64.87 | - | **-** | 14 | - | NEG -$33.3M | - | 70 | 65 | -$5k | - | out (clean 29, ADX 28, RVol 3.0) |

## Big prints this scan (364)
- **AAPL** PUT 350 2026-11-04 (6DTE): 4,205 @ 7.00 = **+$2.9M** SELL | vol 5,176 / OI 755
- **AMD** CALL 560 2026-10-30 (1DTE): 289 @ 13.50 = **+$390k** MID | vol 362 / OI 1,633
- **QQQ** PUT 734 2026-10-29 (0DTE): 200 @ 17.01 = **+$340k** SELL | vol 200 / OI 35
- **MU** PUT 980 2026-10-30 (1DTE): 100 @ 30.23 = **+$302k** SELL | vol 228 / OI 477
- **SPY** PUT 780 2026-10-30 (1DTE): 241 @ 12.05 = **+$290k** SELL | vol 1,587 / OI 4,038
- **SPY** PUT 780 2026-10-30 (1DTE): 241 @ 11.98 = **+$289k** SELL | vol 1,587 / OI 4,038
- **SPY** PUT 780 2026-10-30 (1DTE): 241 @ 11.98 = **+$289k** SELL | vol 1,587 / OI 4,038
- **TSLA** PUT 405 2026-10-30 (1DTE): 498 @ 5.35 = **+$266k** SELL | vol 3,669 / OI 2,059
- **TSLA** PUT 405 2026-10-30 (1DTE): 490 @ 5.30 = **+$260k** SELL | vol 3,669 / OI 2,059
- **MU** CALL 980 2026-10-30 (1DTE): 204 @ 12.70 = **+$259k** BUY | vol 1,640 / OI 3,066
- **SPY** PUT 780 2026-10-30 (1DTE): 213 @ 11.98 = **+$255k** SELL | vol 1,587 / OI 4,038
- **MU** CALL 980 2026-10-30 (1DTE): 196 @ 12.70 = **+$249k** BUY | vol 1,640 / OI 3,066
- **TSLA** PUT 405 2026-10-30 (1DTE): 456 @ 5.10 = **+$233k** SELL | vol 3,669 / OI 2,059
- **MU** CALL 980 2026-10-30 (1DTE): 300 @ 7.50 = **+$225k** BUY | vol 1,640 / OI 3,066
- **AAPL** PUT 350 2026-11-04 (6DTE): 320 @ 7.00 = **+$224k** SELL | vol 5,176 / OI 755

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 760 2026-10-29 (0DTE): 5,132 traded vs OI 2,278
- **SPY** CALL 775 2026-10-29 (0DTE): 5,247 traded vs OI 2,356
- **SPY** PUT 768 2026-11-02 (4DTE): 750 traded vs OI 659
- **SPY** PUT 759 2026-10-29 (0DTE): 2,204 traded vs OI 1,106
- **SPY** CALL 830 2026-11-02 (4DTE): 600 traded vs OI 173
- **SPY** CALL 776 2026-10-29 (0DTE): 5,234 traded vs OI 2,014
- **SPY** PUT 751 2026-10-29 (0DTE): 1,822 traded vs OI 338
- **SPY** CALL 774 2026-10-29 (0DTE): 4,030 traded vs OI 1,672
- **SPY** PUT 740 2026-10-29 (0DTE): 2,702 traded vs OI 1,982
- **SPY** PUT 756 2026-10-29 (0DTE): 1,217 traded vs OI 755
- **SPY** CALL 767 2026-10-29 (0DTE): 2,292 traded vs OI 1,002
- **SPY** PUT 761 2026-10-29 (0DTE): 3,491 traded vs OI 1,297
- **SPY** CALL 766 2026-10-29 (0DTE): 2,822 traded vs OI 865
- **SPY** PUT 692 2026-10-30 (1DTE): 1,040 traded vs OI 670
- **SPY** CALL 768 2026-10-29 (0DTE): 7,268 traded vs OI 2,119

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
