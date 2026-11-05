# GEX + FLOW SCAN - Thu Nov 05, 01:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:55 | **BABA** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/06 102P | 0.75 | 0.33 | -5% (9m) | **-56%** (done) | +27% | 103.58 |
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 11.35 | +1355% (60m) | **+1355%** (done) | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.20 | -12% (0m) | **-58%** (done) | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.10 | -4% (0m) | **-87%** (done) | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:30:08 ET, last candle SPY 13:29, QQQ 13:29 | no errors
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
| 1 | **SPY** | 736.60 | TREND (flow not with it) | **PUTS** | 51 | none: 657 puts 0-7DTE > 16 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (231 contracts' greeks worked out here) | NEG -$12.8B | 768.98 | 760 | 740 | +$1.2B | +$3.4M bull / -$9.8M bear | SHORT (clean 37, ADX 54, RVol 1.5) |
| 2 | **MU** | 679.38 | TREND (flow not with it) | **PUTS** | 49 | none: 82 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | NEG -$66.5M | - | 700 | 700 | +$224.1M | +$4.4M bull / -$8.7M bear | SHORT (clean 34, ADX 33, RVol 1.8) |
| 3 | **NVDA** | 182.81 | TREND (flow not with it) | **PUTS** | 47 | none: 36 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$244.5M | - | 200 | 190 | +$72.2M | +$413k bull / -$3.2M bear | SHORT (clean 34, ADX 46, RVol 1.3) |
| 4 | **SMH** | 455.71 | - | **-** | 31 | - | NEG -$268.8M | - | 445 | 500 | +$41.2M | +$90k bull / -$227k bear | out (clean 35, ADX 39, RVol 0.8) |
| 5 | **IWM** | 272.12 | - | **-** | 28 | - | NEG -$2.7B | 286.94 | 285 | 270 | +$50.9M | +$82k bull / -$6.9M bear | out (clean 38, ADX 50, RVol 1.5) |
| 6 | **PLTR** | 155.36 | - | **-** | 28 | - | NEG -$44.8M | - | 165 | 150 | +$13.0M | +$34k bull / -$188k bear | out (clean 28, ADX 30, RVol 0.8) |
| 7 | **QQQ** | 652.27 | - | **-** | 27 | - | NEG -$4.5B | - | 700 | 680 | +$806.9M | +$3.3M bull / -$9.2M bear | out (clean 36, ADX 43, RVol 0.9) |
| 8 | **MSFT** | 536.88 | - | **-** | 27 | - | POS +$792.4M | - | 540 | 500 | +$21.8M | +$305k bull / +$0 bear | out (clean 32, ADX 34, RVol 1.1) |
| 9 | **TSLA** | 340.81 | - | **-** | 26 | - | NEG -$128.3M | - | 350 | 350 | +$108.6M | +$765k bull / -$3.1M bear | out (clean 35, ADX 39, RVol 1.5) |
| 10 | **AVGO** | 297.61 | - | **-** | 26 | - | NEG -$105.0M | - | 325 | 300 | +$8.9M | +$0 bull / -$208k bear | out (clean 32, ADX 31, RVol 0.6) |
| 11 | **AMD** | 414.31 | - | **-** | 23 | - | NEG -$94.8M | - | 430 | 440 | +$33.9M | +$0 bull / -$2.4M bear | out (clean 34, ADX 36, RVol 0.7) |
| 12 | **AAPL** | 342.88 | - | **-** | 22 | - | POS +$371.3M | 334.41 | 350 | 330 | +$24.4M | +$668k bull / -$947k bear | out (clean 31, ADX 33, RVol 0.7) |
| 13 | **AMZN** | 259.55 | - | **-** | 21 | - | POS +$381.7M | - | 265 | 250 | +$23.2M | +$237k bull / +$0 bear | out (clean 35, ADX 16, RVol 0.7) |
| 14 | **GOOGL** | 283.14 | - | **-** | 20 | - | POS +$17.8M | 280.79 | 285 | 290 | +$8.8M | +$177k bull / +$0 bear | out (clean 35, ADX 16, RVol 0.5) |
| 15 | **MSTR** | 128.73 | - | **-** | 20 | - | POS +$51.4M | - | 135 | 125 | +$3.5M | +$38k bull / -$71k bear | out (clean 34, ADX 27, RVol 0.5) |
| 16 | **CRM** | 221.36 | - | **-** | 19 | - | NEG -$16.3M | - | 240 | 220 | +$562k | - | out (clean 34, ADX 23, RVol 0.8) |
| 17 | **COIN** | 136.16 | - | **-** | 18 | - | POS +$16.1M | - | 142 | 135 | +$2.0M | - | out (clean 33, ADX 34, RVol 0.5) |
| 18 | **META** | 602.58 | - | **-** | 17 | - | NEG -$117.9M | 621.17 | 650 | 600 | +$18.8M | +$937k bull / -$1.2M bear | out (clean 34, ADX 16, RVol 0.4) |
| 19 | **BABA** | 106.70 | - | **-** | 17 | - | POS +$21.4M | - | 110 | 110 | +$1.4M | - | out (clean 36, ADX 12, RVol 0.8) |
| 20 | **NFLX** | 65.27 | - | **-** | 15 | - | POS +$29.9M | 62.11 | 65 | 65 | +$991k | - | out (clean 33, ADX 28, RVol 0.5) |
| 21 | **DELL** | 324.81 | - | **-** | 15 | - | NEG -$13.0M | - | 350 | 340 | +$6.2M | - | out (clean 35, ADX 29, RVol 0.5) |
| 22 | **HOOD** | 77.35 | - | **-** | 13 | - | NEG -$8.7M | - | 85 | 80 | +$2.0M | - | out (clean 32, ADX 39, RVol 1.0) |
| 23 | **ARM** | 169.24 | - | **-** | 13 | - | NEG -$6.9M | - | 180 | 180 | +$1.4M | - | out (clean 27, ADX 24, RVol 0.9) |
| 24 | **SMCI** | 26.80 | - | **-** | 12 | - | NEG -$2.9M | - | 28 | 27 | +$428k | - | out (clean 36, ADX 24, RVol 0.9) |
| 25 | **ORCL** | 114.71 | - | **-** | 11 | - | NEG -$56.7M | - | 125 | 115 | +$2.8M | - | out (clean 32, ADX 26, RVol 0.7) |
| 26 | **UBER** | 68.47 | - | **-** | 8 | - | POS +$3.0M | 67.97 | 70 | 65 | +$188k | - | out (clean 32, ADX 8, RVol 0.4) |
| 27 | **SHOP** | 144.59 | - | **-** | 8 | - | NEG -$4.6M | - | 144 | 135 | -$131k | - | out (clean 38, ADX 17, RVol 0.5) |

## Big prints this scan (193)
- **SPY** CALL 740 2026-11-10 (5DTE): 1,430 @ 8.05 = **+$1.2M** BUY | vol 14,540 / OI 44
- **SPY** PUT 760 2026-11-05 (0DTE): 240 @ 22.04 = **+$529k** SELL | vol 76,784 / OI 3,384
- **TSLA** PUT 335 2026-11-06 (1DTE): 799 @ 4.86 = **+$388k** SELL | vol 18,603 / OI 1,231
- **QQQ** PUT 650 2026-11-06 (1DTE): 500 @ 6.88 = **+$344k** SELL | vol 54,016 / OI 11,913
- **MU** CALL 680 2026-11-06 (1DTE): 111 @ 26.62 = **+$295k** BUY | vol 9,273 / OI 21
- **QQQ** CALL 655 2026-11-06 (1DTE): 355 @ 7.47 = **+$265k** BUY | vol 15,999 / OI 1,189
- **AMD** CALL 420 2026-11-06 (1DTE): 250 @ 10.19 = **+$255k** SELL | vol 5,040 / OI 51
- **AMD** CALL 420 2026-11-06 (1DTE): 250 @ 10.19 = **+$255k** SELL | vol 5,040 / OI 51
- **NVDA** PUT 180 2026-11-06 (1DTE): 968 @ 2.53 = **+$245k** SELL | vol 63,360 / OI 8,001
- **MU** CALL 680 2026-11-06 (1DTE): 96 @ 24.65 = **+$237k** BUY | vol 9,273 / OI 21
- **MU** PUT 700 2026-11-09 (4DTE): 60 @ 38.70 = **+$232k** SELL | vol 3,956 / OI 0
- **SPY** CALL 740 2026-11-10 (5DTE): 275 @ 8.05 = **+$221k** BUY | vol 14,540 / OI 44
- **SPY** CALL 740 2026-11-10 (5DTE): 250 @ 8.05 = **+$201k** BUY | vol 14,540 / OI 44
- **META** PUT 585 2026-11-06 (1DTE): 500 @ 4.00 = **+$200k** BUY | vol 5,058 / OI 630
- **SPY** CALL 730 2026-11-06 (1DTE): 175 @ 10.83 = **+$190k** BUY | vol 1,470 / OI 271

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 752 2026-11-10 (5DTE): 501 traded vs OI 188
- **SPY** CALL 734 2026-11-09 (4DTE): 539 traded vs OI 0
- **SPY** CALL 743 2026-11-11 (6DTE): 500 traded vs OI 0
- **SPY** PUT 680 2026-11-12 (7DTE): 516 traded vs OI 0
- **SPY** PUT 728 2026-11-13 (8DTE): 779 traded vs OI 730
- **SPY** PUT 738 2026-11-12 (7DTE): 504 traded vs OI 1
- **SPY** PUT 704 2026-11-12 (7DTE): 617 traded vs OI 2
- **SPY** CALL 757 2026-11-20 (15DTE): 1,657 traded vs OI 1,364
- **SPY** CALL 730 2026-12-04 (29DTE): 521 traded vs OI 182
- **SPY** PUT 730 2026-11-19 (14DTE): 507 traded vs OI 0
- **SPY** CALL 759 2026-11-20 (15DTE): 955 traded vs OI 898
- **QQQ** CALL 700 2026-11-10 (5DTE): 1,202 traded vs OI 1,185
- **QQQ** CALL 660 2026-11-18 (13DTE): 500 traded vs OI 0
- **QQQ** CALL 685 2026-11-18 (13DTE): 504 traded vs OI 0
- **QQQ** PUT 620 2026-11-19 (14DTE): 590 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
