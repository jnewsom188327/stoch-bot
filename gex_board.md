# GEX + FLOW SCAN - Thu Nov 05, 03:05 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 15:00 | **SMCI** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 28.5C | 0.46 | 0.36 | -7% (0m) | **-22%** | +29% | 28.14 |
| 10:55 | **BABA** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/06 102P | 0.75 | 0.33 | -5% (9m) | **-56%** (done) | +27% | 103.58 |
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 11.35 | +1355% (60m) | **+1355%** (done) | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.20 | -12% (0m) | **-58%** (done) | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.10 | -4% (0m) | **-87%** (done) | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:05:08 ET, last candle SPY 15:04, QQQ 15:04 | no errors
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
| 1 | **SMCI** | 27.45 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 49 | 11/06 28C @ 0.62 (delta 0.41) = est +21% at 27.96 | NEG -$3.6M | - | 30 | 27 | +$148k | - | LONG (clean 35, ADX 27, RVol 1.4) |
| 2 | **GOOGL** | 284.69 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 30 | none: 69 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$37.8M | 280.78 | 285 | 290 | +$8.5M | - | out (clean 34, ADX 18, RVol 0.9) |
| 3 | **SPY** | 737.39 | - | **-** | 26 | - | NEG -$13.5B | 768.91 | 760 | 740 | +$1.2B | +$1.5M bull / -$7.3M bear | out (clean 36, ADX 29, RVol 1.2) |
| 4 | **PLTR** | 155.63 | - | **-** | 25 | - | NEG -$46.7M | - | 165 | 150 | +$12.1M | +$0 bull / -$91k bear | out (clean 28, ADX 21, RVol 0.7) |
| 5 | **DELL** | 327.45 | - | **-** | 25 | - | NEG -$14.7M | - | 360 | 340 | +$6.3M | +$45k bull / +$0 bear | out (clean 33, ADX 22, RVol 1.3) |
| 6 | **IWM** | 271.88 | - | **-** | 24 | - | NEG -$2.8B | 286.55 | 285 | 270 | +$55.4M | +$174k bull / -$841k bear | out (clean 36, ADX 26, RVol 1.6) |
| 7 | **NFLX** | 65.03 | PINNED between the walls (positive gamma) - chop | **-** | 24 | - | POS +$31.1M | 62.26 | 65 | 65 | +$846k | - | out (clean 32, ADX 21, RVol 0.7) |
| 8 | **AVGO** | 297.74 | - | **-** | 24 | - | NEG -$107.9M | - | 325 | 300 | +$9.0M | +$0 bull / -$50k bear | out (clean 31, ADX 19, RVol 1.0) |
| 9 | **MU** | 683.08 | - | **-** | 24 | - | NEG -$86.1M | - | 700 | 700 | +$224.3M | +$3.0M bull / -$5.9M bear | out (clean 32, ADX 22, RVol 2.5) |
| 10 | **QQQ** | 654.21 | - | **-** | 23 | - | NEG -$4.6B | - | 700 | 680 | +$840.7M | +$3.5M bull / -$7.4M bear | out (clean 35, ADX 24, RVol 1.1) |
| 11 | **SMH** | 457.97 | - | **-** | 23 | - | NEG -$302.5M | - | 500 | 500 | +$29.3M | +$134k bull / -$154k bear | out (clean 34, ADX 22, RVol 0.8) |
| 12 | **TSLA** | 342.61 | - | **-** | 23 | - | NEG -$133.2M | - | 350 | 350 | +$110.2M | +$1.1M bull / -$3.2M bear | out (clean 35, ADX 21, RVol 1.8) |
| 13 | **MSFT** | 536.97 | - | **-** | 23 | - | POS +$811.0M | - | 540 | 500 | +$21.5M | +$136k bull / -$382k bear | out (clean 31, ADX 20, RVol 0.7) |
| 14 | **NVDA** | 183.96 | - | **-** | 22 | - | NEG -$249.2M | - | 200 | 190 | +$74.0M | +$457k bull / -$399k bear | out (clean 33, ADX 25, RVol 0.8) |
| 15 | **AAPL** | 345.42 | - | **-** | 21 | - | POS +$526.8M | 334.87 | 350 | 330 | +$23.7M | +$150k bull / -$446k bear | out (clean 31, ADX 21, RVol 1.6) |
| 16 | **AMZN** | 259.07 | - | **-** | 20 | - | POS +$375.8M | - | 265 | 250 | +$24.8M | +$785k bull / -$285k bear | out (clean 34, ADX 16, RVol 0.5) |
| 17 | **AMD** | 418.43 | - | **-** | 19 | - | NEG -$105.2M | - | 430 | 440 | +$34.4M | +$932k bull / -$219k bear | out (clean 32, ADX 21, RVol 0.7) |
| 18 | **MSTR** | 129.50 | - | **-** | 19 | - | POS +$60.5M | - | 135 | 125 | +$3.8M | +$0 bull / -$145k bear | out (clean 33, ADX 20, RVol 0.8) |
| 19 | **ORCL** | 115.48 | - | **-** | 19 | - | NEG -$58.0M | - | 125 | 115 | +$2.8M | +$30k bull / +$0 bear | out (clean 31, ADX 16, RVol 0.8) |
| 20 | **CRM** | 221.11 | - | **-** | 19 | - | NEG -$15.8M | - | 240 | 220 | +$558k | - | out (clean 34, ADX 17, RVol 1.6) |
| 21 | **META** | 606.53 | - | **-** | 16 | - | NEG -$112.0M | 621.1 | 650 | 600 | +$17.3M | +$103k bull / -$273k bear | out (clean 33, ADX 13, RVol 0.4) |
| 22 | **ARM** | 169.54 | - | **-** | 14 | - | NEG -$7.3M | - | 180 | 180 | +$1.5M | - | out (clean 26, ADX 16, RVol 2.0) |
| 23 | **COIN** | 138.26 | - | **-** | 13 | - | POS +$21.3M | - | 142 | 135 | +$1.5M | - | out (clean 33, ADX 28, RVol 0.8) |
| 24 | **BABA** | 107.78 | - | **-** | 13 | - | POS +$21.4M | - | 110 | 110 | +$858k | - | out (clean 35, ADX 21, RVol 1.5) |
| 25 | **HOOD** | 78.64 | - | **-** | 11 | - | NEG -$8.4M | - | 85 | 80 | +$2.1M | - | out (clean 31, ADX 28, RVol 1.4) |
| 26 | **UBER** | 68.60 | - | **-** | 10 | - | POS +$4.2M | 67.94 | 70 | 65 | +$192k | - | out (clean 30, ADX 13, RVol 1.0) |
| 27 | **SHOP** | 144.19 | - | **-** | 7 | - | NEG -$4.6M | - | 144 | 135 | -$134k | - | out (clean 37, ADX 15, RVol 0.3) |

## Big prints this scan (133)
- **AMD** PUT 407.5 2026-11-09 (4DTE): 499 @ 12.00 = **+$599k** SELL | vol 808 / OI 0
- **QQQ** CALL 660 2026-11-05 (0DTE): 2,411 @ 1.97 = **+$475k** BUY | vol 246,441 / OI 12
- **QQQ** CALL 660 2026-11-05 (0DTE): 2,500 @ 1.54 = **+$385k** BUY | vol 246,441 / OI 12
- **QQQ** CALL 651 2026-11-05 (0DTE): 399 @ 7.54 = **+$301k** BUY | vol 37,518 / OI 0
- **SPY** PUT 735 2026-11-06 (1DTE): 1,000 @ 2.89 = **+$289k** SELL | vol 70,549 / OI 24,589
- **MU** PUT 710 2026-11-11 (6DTE): 50 @ 45.65 = **+$228k** SELL | vol 400 / OI 0
- **QQQ** CALL 652 2026-11-05 (0DTE): 400 @ 5.50 = **+$220k** BUY | vol 54,773 / OI 0
- **TSLA** CALL 350 2026-11-06 (1DTE): 400 @ 5.05 = **+$202k** BUY | vol 46,253 / OI 1,359
- **QQQ** PUT 657 2026-11-06 (1DTE): 220 @ 8.60 = **+$189k** SELL | vol 11,756 / OI 1,814
- **SPY** CALL 738 2026-11-06 (1DTE): 306 @ 5.89 = **+$180k** BUY | vol 15,213 / OI 61
- **SPY** PUT 735 2026-11-06 (1DTE): 530 @ 3.37 = **+$179k** SELL | vol 70,549 / OI 24,589
- **QQQ** CALL 665 2026-11-05 (0DTE): 2,411 @ 0.73 = **+$176k** BUY | vol 237,614 / OI 21
- **TSLA** CALL 345 2026-11-06 (1DTE): 199 @ 7.75 = **+$154k** BUY | vol 15,919 / OI 104
- **QQQ** CALL 657 2026-11-09 (4DTE): 140 @ 10.97 = **+$154k** BUY | vol 1,393 / OI 0
- **TSLA** CALL 340 2026-11-06 (1DTE): 150 @ 10.15 = **+$152k** BUY | vol 11,661 / OI 161

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 761 2026-11-11 (6DTE): 526 traded vs OI 12
- **SPY** CALL 793 2026-11-09 (4DTE): 623 traded vs OI 26
- **SPY** CALL 792 2026-11-09 (4DTE): 3,516 traded vs OI 4
- **SPY** CALL 775 2026-11-06 (1DTE): 7,677 traded vs OI 7,600
- **SPY** CALL 740 2026-12-04 (29DTE): 504 traded vs OI 140
- **SPY** CALL 783 2026-12-04 (29DTE): 523 traded vs OI 355
- **SPY** PUT 738 2026-12-04 (29DTE): 518 traded vs OI 408
- **QQQ** PUT 696 2026-11-05 (0DTE): 969 traded vs OI 44
- **QQQ** PUT 625 2026-11-27 (22DTE): 516 traded vs OI 512
- **QQQ** PUT 650 2026-11-30 (25DTE): 9,518 traded vs OI 9,295
- **IWM** CALL 281 2026-11-06 (1DTE): 4,094 traded vs OI 4,047
- **TSLA** CALL 345 2026-11-11 (6DTE): 527 traded vs OI 149
- **TSLA** CALL 375 2026-11-13 (8DTE): 1,771 traded vs OI 1,764
- **AAPL** PUT 315 2026-11-13 (8DTE): 718 traded vs OI 0
- **AMD** CALL 427.5 2026-11-13 (8DTE): 504 traded vs OI 1

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
