# GEX + FLOW SCAN - Thu Nov 05, 11:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:55 | **BABA** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/06 102P | 0.75 | 0.32 | -5% (9m) | **-57%** | +27% | 103.58 |
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 11.35 | +1355% (60m) | **+1355%** (done) | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.20 | -12% (0m) | **-58%** (done) | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.10 | -4% (0m) | **-87%** (done) | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:40:08 ET, last candle SPY 11:39, QQQ 11:39 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:38 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 64 puts 0-1DTE > 1 priced 0.40-0.80 > 0 delta 0.15+ > 0 spread ok > 0 liquid  |
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (26 today, last 5)
- 11:15 IWM CALLS: price -0.15 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:10 IWM CALLS: price -0.10 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:05 IWM CALLS: price -1.05 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:00 IWM CALLS: price -1.16 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:55 IWM CALLS: price -2.06 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 275.80 | TREND (flow not with it) | **PUTS** | 63 | 11/05 274P @ 0.55 (delta 0.28) = est +114% at 273.62 | NEG -$2.3B | 286.11 | 285 | 270 | +$46.1M | +$0 bull / -$263k bear | SHORT (clean 36, ADX 53, RVol 2.7) |
| 2 | **META** | 609.57 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 62 | none: 147 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$79.4M | 619.44 | 650 | 600 | +$14.6M | +$0 bull / -$6.2M bear | LONG (clean 34, ADX 34, RVol 2.5) |
| 3 | **GOOGL** | 284.56 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 43 | none: 69 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | POS +$24.4M | 281.42 | 285 | 290 | +$7.9M | +$28k bull / +$0 bear | out (clean 35, ADX 23, RVol 0.9) |
| 4 | **SMH** | 464.00 | - | **-** | 36 | - | NEG -$330.3M | - | 505 | 500 | +$36.0M | +$323k bull / -$906k bear | out (clean 35, ADX 52, RVol 4.7) |
| 5 | **ORCL** | 115.23 | TREND (flow not with it) | **PUTS** | 36 | none: 23 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$57.0M | - | 125 | 115 | +$2.6M | - | SHORT (clean 34, ADX 50, RVol 1.3) |
| 6 | **SPY** | 744.63 | - | **-** | 34 | - | NEG -$12.2B | 769.64 | 760 | 750 | +$988.7M | +$2.0M bull / -$5.9M bear | out (clean 36, ADX 61, RVol 2.7) |
| 7 | **PLTR** | 157.33 | - | **-** | 32 | - | NEG -$45.9M | - | 165 | 160 | +$11.9M | +$81k bull / -$99k bear | out (clean 28, ADX 44, RVol 0.8) |
| 8 | **QQQ** | 660.46 | - | **-** | 30 | - | NEG -$5.0B | - | 700 | 680 | +$670.5M | +$5.2M bull / -$7.7M bear | out (clean 35, ADX 56, RVol 2.0) |
| 9 | **NVDA** | 187.28 | - | **-** | 30 | - | NEG -$295.6M | - | 200 | 190 | +$51.8M | +$34k bull / -$3.1M bear | out (clean 33, ADX 58, RVol 3.3) |
| 10 | **MSFT** | 543.90 | - | **-** | 30 | - | POS +$894.2M | - | 540 | 500 | +$18.3M | +$131k bull / -$1.3M bear | out (clean 32, ADX 45, RVol 1.4) |
| 11 | **AVGO** | 304.85 | - | **-** | 30 | - | NEG -$127.3M | - | 330 | 300 | +$6.3M | +$119k bull / -$703k bear | out (clean 32, ADX 42, RVol 2.0) |
| 12 | **TSLA** | 349.85 | - | **-** | 29 | - | NEG -$160.0M | - | 370 | 350 | +$88.8M | +$873k bull / -$2.7M bear | out (clean 35, ADX 47, RVol 2.5) |
| 13 | **DELL** | 334.05 | - | **-** | 29 | - | NEG -$16.0M | - | 360 | 350 | +$5.4M | +$0 bull / -$210k bear | out (clean 35, ADX 39, RVol 1.5) |
| 14 | **MU** | 707.20 | - | **-** | 29 | - | NEG -$117.3M | - | 700 | 750 | +$146.7M | +$3.7M bull / -$9.8M bear | out (clean 34, ADX 55, RVol 4.1) |
| 15 | **ARM** | 171.15 | - | **-** | 29 | - | NEG -$7.2M | - | 180 | 180 | +$1.3M | +$0 bull / -$103k bear | out (clean 28, ADX 49, RVol 1.7) |
| 16 | **MSTR** | 130.78 | - | **-** | 28 | - | POS +$66.8M | - | 135 | 125 | +$3.3M | +$145k bull / -$238k bear | out (clean 34, ADX 50, RVol 2.4) |
| 17 | **AMZN** | 260.30 | - | **-** | 27 | - | POS +$400.4M | - | 265 | 250 | +$25.9M | +$0 bull / -$471k bear | out (clean 34, ADX 28, RVol 1.4) |
| 18 | **AMD** | 425.55 | - | **-** | 26 | - | NEG -$109.8M | - | 430 | 440 | +$29.3M | +$1.1M bull / -$2.2M bear | out (clean 34, ADX 46, RVol 1.3) |
| 19 | **NFLX** | 65.65 | - | **-** | 24 | - | POS +$32.6M | 62.25 | 65 | 65 | +$778k | +$208k bull / +$0 bear | out (clean 33, ADX 17, RVol 1.2) |
| 20 | **AAPL** | 346.88 | - | **-** | 23 | - | POS +$567.2M | 334.35 | 350 | 340 | +$15.4M | +$147k bull / -$209k bear | out (clean 31, ADX 24, RVol 1.9) |
| 21 | **HOOD** | 79.24 | - | **-** | 22 | - | NEG -$7.8M | - | 85 | 80 | +$1.1M | +$30k bull / -$54k bear | out (clean 32, ADX 56, RVol 0.7) |
| 22 | **COIN** | 138.22 | - | **-** | 21 | - | POS +$18.6M | - | 142 | 135 | +$1.8M | - | out (clean 33, ADX 54, RVol 0.7) |
| 23 | **BABA** | 107.18 | - | **-** | 20 | - | POS +$19.1M | - | 110 | 110 | +$1.1M | - | out (clean 37, ADX 19, RVol 2.2) |
| 24 | **SMCI** | 27.20 | - | **-** | 17 | - | NEG -$3.1M | - | 28 | 27 | +$358k | - | out (clean 36, ADX 46, RVol 1.3) |
| 25 | **CRM** | 223.67 | - | **-** | 17 | - | NEG -$14.4M | - | 240 | 220 | +$482k | - | out (clean 33, ADX 15, RVol 0.6) |
| 26 | **UBER** | 68.50 | - | **-** | 11 | - | POS +$3.1M | 67.98 | 70 | 65 | +$160k | - | out (clean 32, ADX 15, RVol 0.8) |
| 27 | **SHOP** | 144.53 | - | **-** | 9 | - | NEG -$4.2M | - | 144 | 135 | +$13k | - | out (clean 37, ADX 39, RVol 0.6) |

## Big prints this scan (259)
- **QQQ** CALL 663 2026-11-09 (4DTE): 1,000 @ 9.77 = **+$977k** BUY | vol 12,747 / OI 0
- **SPY** PUT 762 2026-11-05 (0DTE): 300 @ 17.30 = **+$519k** SELL | vol 38,048 / OI 88
- **QQQ** PUT 660 2026-11-05 (0DTE): 1,107 @ 4.65 = **+$515k** BUY | vol 112,810 / OI 2,574
- **QQQ** CALL 663 2026-11-09 (4DTE): 500 @ 10.10 = **+$505k** BUY | vol 12,747 / OI 0
- **QQQ** CALL 663 2026-11-09 (4DTE): 424 @ 10.11 = **+$429k** BUY | vol 12,747 / OI 0
- **SPY** CALL 743 2026-11-06 (1DTE): 500 @ 7.10 = **+$355k** BUY | vol 6,145 / OI 515
- **QQQ** CALL 680 2026-11-12 (7DTE): 500 @ 6.25 = **+$312k** BUY | vol 1,214 / OI 163
- **QQQ** CALL 663 2026-11-09 (4DTE): 297 @ 10.40 = **+$309k** BUY | vol 12,747 / OI 0
- **QQQ** CALL 650 2026-11-06 (1DTE): 188 @ 16.19 = **+$304k** BUY | vol 3,357 / OI 889
- **QQQ** CALL 663 2026-11-09 (4DTE): 295 @ 10.20 = **+$301k** BUY | vol 12,747 / OI 0
- **MU** PUT 717.5 2026-11-11 (6DTE): 70 @ 40.95 = **+$287k** BUY | vol 321 / OI 0
- **MU** PUT 717.5 2026-11-11 (6DTE): 67 @ 40.95 = **+$274k** BUY | vol 321 / OI 0
- **QQQ** CALL 659 2026-11-05 (0DTE): 492 @ 5.13 = **+$252k** BUY | vol 28,795 / OI 0
- **SPY** CALL 745 2026-11-06 (1DTE): 400 @ 6.09 = **+$244k** BUY | vol 9,390 / OI 1,181
- **SPY** PUT 743 2026-11-05 (0DTE): 1,000 @ 2.41 = **+$241k** SELL | vol 97,975 / OI 1,127

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 731 2026-11-05 (0DTE): 501 traded vs OI 2
- **SPY** CALL 785 2026-11-09 (4DTE): 882 traded vs OI 863
- **SPY** PUT 685 2026-11-09 (4DTE): 591 traded vs OI 0
- **SPY** PUT 737 2026-11-11 (6DTE): 502 traded vs OI 13
- **SPY** PUT 675 2026-11-13 (8DTE): 630 traded vs OI 0
- **SPY** PUT 767 2026-11-30 (25DTE): 1,067 traded vs OI 1,041
- **QQQ** CALL 661 2026-11-09 (4DTE): 576 traded vs OI 0
- **QQQ** CALL 665 2026-11-12 (7DTE): 500 traded vs OI 11
- **QQQ** PUT 600 2026-11-10 (5DTE): 653 traded vs OI 0
- **QQQ** CALL 701 2026-11-09 (4DTE): 616 traded vs OI 23
- **QQQ** PUT 657 2026-11-13 (8DTE): 555 traded vs OI 28
- **QQQ** CALL 700 2026-11-18 (13DTE): 508 traded vs OI 0
- **QQQ** CALL 694 2026-11-30 (25DTE): 598 traded vs OI 247
- **QQQ** CALL 690 2026-12-04 (29DTE): 859 traded vs OI 748
- **SMH** CALL 467.5 2026-11-06 (1DTE): 604 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
