# GEX + FLOW SCAN - Thu Nov 05, 03:15 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 15:00 | **SMCI** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 28.5C | 0.46 | 0.32 | -7% (0m) | **-30%** | +29% | 28.14 |
| 10:55 | **BABA** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/06 102P | 0.75 | 0.33 | -5% (9m) | **-56%** (done) | +27% | 103.58 |
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 11.35 | +1355% (60m) | **+1355%** (done) | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.20 | -12% (0m) | **-58%** (done) | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.10 | -4% (0m) | **-87%** (done) | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:15:08 ET, last candle SPY 15:14, QQQ 15:14 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 13:05 | SPY | 1m WHIPSAW | R1 | CALLS | AGAINST you | no contract: 87 calls 0-1DTE > 8 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid |
| 11:44 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:38 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 64 puts 0-1DTE > 1 priced 0.40-0.80 > 0 delta 0.15+ > 0 spread ok > 0 liquid  |
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (36 today, last 5)
- 12:55 IWM CALLS: price -0.16 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:50 IWM CALLS: price -0.60 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:45 IWM CALLS: price -0.70 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:40 IWM CALLS: price -0.66 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:20 IWM CALLS: under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMCI** | 27.26 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 46 | 11/06 28C @ 0.53 (delta 0.37) = est +44% at 28 | NEG -$4.1M | - | 28 | 27 | +$156k | - | LONG (clean 35, ADX 25, RVol 1.1) |
| 2 | **GOOGL** | 284.59 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 39 | none: 69 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$29.1M | 281.43 | 285 | 290 | +$8.6M | +$217k bull / +$0 bear | out (clean 34, ADX 17, RVol 0.8) |
| 3 | **DELL** | 323.18 | - | **-** | 26 | - | NEG -$16.4M | - | 350 | 340 | +$6.3M | +$101k bull / +$0 bear | out (clean 32, ADX 20, RVol 1.7) |
| 4 | **SPY** | 735.89 | - | **-** | 25 | - | NEG -$13.9B | 769.81 | 760 | 740 | +$1.2B | +$2.9M bull / -$4.0M bear | out (clean 36, ADX 27, RVol 1.2) |
| 5 | **PLTR** | 154.77 | - | **-** | 25 | - | NEG -$55.8M | - | 165 | 150 | +$12.1M | +$286k bull / -$91k bear | out (clean 28, ADX 19, RVol 1.0) |
| 6 | **IWM** | 271.49 | - | **-** | 24 | - | NEG -$2.9B | 287.38 | 285 | 270 | +$56.1M | +$174k bull / -$580k bear | out (clean 36, ADX 24, RVol 1.6) |
| 7 | **AVGO** | 295.38 | - | **-** | 24 | - | NEG -$113.1M | - | 320 | 300 | +$9.0M | +$245k bull / -$50k bear | out (clean 31, ADX 19, RVol 1.2) |
| 8 | **MU** | 675.05 | - | **-** | 24 | - | NEG -$104.2M | - | 700 | 700 | +$224.4M | +$7.3M bull / -$3.0M bear | out (clean 32, ADX 20, RVol 2.7) |
| 9 | **QQQ** | 651.77 | - | **-** | 23 | - | NEG -$4.7B | - | 700 | 650 | +$855.1M | +$7.0M bull / -$7.1M bear | out (clean 35, ADX 22, RVol 1.2) |
| 10 | **SMH** | 453.96 | - | **-** | 23 | - | NEG -$281.0M | - | 445 | 465 | +$29.5M | +$381k bull / -$62k bear | out (clean 34, ADX 21, RVol 0.9) |
| 11 | **MSFT** | 536.04 | - | **-** | 23 | - | POS +$754.2M | - | 540 | 500 | +$21.7M | +$311k bull / -$382k bear | out (clean 32, ADX 20, RVol 0.7) |
| 12 | **BABA** | 107.84 | - | **-** | 23 | - | POS +$20.9M | - | 110 | 110 | +$879k | +$38k bull / +$0 bear | out (clean 35, ADX 22, RVol 1.4) |
| 13 | **NVDA** | 182.86 | - | **-** | 22 | - | NEG -$274.3M | - | 200 | 190 | +$74.3M | +$1.1M bull / -$298k bear | out (clean 34, ADX 22, RVol 0.8) |
| 14 | **TSLA** | 341.38 | - | **-** | 22 | - | NEG -$159.8M | - | 350 | 350 | +$110.5M | +$2.2M bull / -$3.0M bear | out (clean 35, ADX 19, RVol 1.6) |
| 15 | **AAPL** | 345.30 | - | **-** | 21 | - | POS +$480.9M | 335.41 | 350 | 330 | +$24.9M | +$752k bull / -$390k bear | out (clean 31, ADX 19, RVol 1.8) |
| 16 | **AMZN** | 259.33 | - | **-** | 20 | - | POS +$354.6M | - | 265 | 250 | +$25.3M | +$860k bull / -$199k bear | out (clean 34, ADX 16, RVol 0.5) |
| 17 | **AMD** | 414.08 | - | **-** | 19 | - | NEG -$115.1M | - | 430 | 440 | +$35.0M | +$1.8M bull / -$194k bear | out (clean 32, ADX 19, RVol 0.8) |
| 18 | **MSTR** | 128.77 | - | **-** | 19 | - | POS +$41.9M | - | 135 | 125 | +$3.8M | +$0 bull / -$145k bear | out (clean 33, ADX 18, RVol 0.9) |
| 19 | **ORCL** | 115.21 | - | **-** | 19 | - | NEG -$66.5M | - | 125 | 115 | +$2.8M | +$30k bull / +$0 bear | out (clean 31, ADX 15, RVol 0.7) |
| 20 | **CRM** | 220.76 | - | **-** | 19 | - | NEG -$18.7M | - | 240 | 220 | +$558k | - | out (clean 33, ADX 17, RVol 1.5) |
| 21 | **META** | 606.34 | - | **-** | 16 | - | NEG -$138.7M | 623.51 | 650 | 600 | +$17.5M | +$103k bull / -$232k bear | out (clean 33, ADX 12, RVol 0.5) |
| 22 | **ARM** | 168.35 | - | **-** | 14 | - | NEG -$6.7M | - | 180 | 180 | +$1.5M | - | out (clean 26, ADX 15, RVol 2.1) |
| 23 | **COIN** | 137.56 | - | **-** | 13 | - | POS +$12.3M | 133.86 | 142 | 130 | +$1.6M | - | out (clean 33, ADX 27, RVol 0.6) |
| 24 | **NFLX** | 64.81 | - | **-** | 11 | - | POS +$28.6M | 62.43 | 65 | 65 | +$859k | - | out (clean 32, ADX 23, RVol 0.7) |
| 25 | **HOOD** | 78.19 | - | **-** | 10 | - | NEG -$14.6M | - | 85 | 80 | +$2.2M | - | out (clean 31, ADX 25, RVol 1.0) |
| 26 | **UBER** | 68.56 | - | **-** | 9 | - | POS +$2.2M | 68.25 | 70 | 65 | +$188k | - | out (clean 30, ADX 12, RVol 0.7) |
| 27 | **SHOP** | 144.18 | - | **-** | 7 | - | NEG -$5.6M | - | 144 | 135 | -$134k | - | out (clean 37, ADX 13, RVol 0.4) |

## Big prints this scan (94)
- **QQQ** PUT 662 2026-11-06 (1DTE): 261 @ 10.10 = **+$264k** SELL | vol 8,211 / OI 96
- **QQQ** CALL 660 2026-11-06 (1DTE): 371 @ 5.75 = **+$213k** BUY | vol 47,932 / OI 333
- **QQQ** CALL 657 2026-11-05 (0DTE): 880 @ 2.34 = **+$206k** BUY | vol 87,123 / OI 0
- **QQQ** CALL 665 2026-11-05 (0DTE): 4,999 @ 0.38 = **+$190k** BUY | vol 246,414 / OI 21
- **QQQ** PUT 665 2026-11-06 (1DTE): 160 @ 11.79 = **+$189k** SELL | vol 14,048 / OI 7,114
- **SPY** PUT 753 2026-11-05 (0DTE): 125 @ 13.57 = **+$170k** SELL | vol 77,884 / OI 748
- **QQQ** CALL 652 2026-11-05 (0DTE): 300 @ 5.24 = **+$157k** BUY | vol 55,915 / OI 0
- **SPY** PUT 731 2026-11-11 (6DTE): 284 @ 5.35 = **+$152k** SELL | vol 1,348 / OI 316
- **QQQ** CALL 657 2026-11-09 (4DTE): 146 @ 10.03 = **+$146k** BUY | vol 2,465 / OI 0
- **SPY** CALL 738 2026-11-06 (1DTE): 223 @ 6.23 = **+$139k** BUY | vol 16,190 / OI 61
- **QQQ** PUT 654 2026-11-06 (1DTE): 200 @ 6.13 = **+$123k** SELL | vol 13,985 / OI 231
- **SPY** PUT 770 2026-11-06 (1DTE): 40 @ 30.25 = **+$121k** SELL | vol 3,679 / OI 6,051
- **QQQ** PUT 655 2026-11-06 (1DTE): 160 @ 6.77 = **+$108k** SELL | vol 33,887 / OI 5,889
- **QQQ** PUT 654 2026-11-06 (1DTE): 160 @ 6.35 = **+$102k** SELL | vol 13,985 / OI 231
- **AMD** CALL 420 2026-11-06 (1DTE): 75 @ 12.46 = **+$93k** BUY | vol 6,628 / OI 51

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 787 2026-11-10 (5DTE): 883 traded vs OI 107
- **QQQ** PUT 610 2026-11-10 (5DTE): 501 traded vs OI 411
- **QQQ** CALL 667 2026-11-12 (7DTE): 516 traded vs OI 1
- **IWM** PUT 270 2026-12-04 (29DTE): 798 traded vs OI 521
- **AAPL** CALL 345 2026-11-11 (6DTE): 512 traded vs OI 258
- **AMZN** CALL 285 2026-11-20 (15DTE): 2,998 traded vs OI 0
- **AMZN** CALL 285 2026-11-13 (8DTE): 580 traded vs OI 0
- **GOOGL** CALL 300 2026-11-16 (11DTE): 4,753 traded vs OI 188
- **MU** CALL 700 2026-11-11 (6DTE): 501 traded vs OI 0
- **HOOD** PUT 86 2026-11-06 (1DTE): 942 traded vs OI 0
- **HOOD** CALL 86 2026-11-06 (1DTE): 8,916 traded vs OI 0
- **HOOD** CALL 76 2026-11-27 (22DTE): 503 traded vs OI 0
- **HOOD** PUT 86 2026-12-04 (29DTE): 501 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
