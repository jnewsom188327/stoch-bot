# GEX + FLOW SCAN - Thu Nov 05, 02:50 PM ET
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
Last 1m check 14:50:08 ET, last candle SPY 14:49, QQQ 14:49 | no errors
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
| 1 | **MSFT** | 539.88 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 41 | none: 129 puts 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$870.9M | - | 540 | 500 | +$20.9M | +$470k bull / -$423k bear | out (clean 32, ADX 22, RVol 0.6) |
| 2 | **SPY** | 739.52 | - | **-** | 27 | - | NEG -$13.4B | 768.89 | 760 | 740 | +$1.2B | +$2.4M bull / -$2.1M bear | out (clean 36, ADX 33, RVol 1.2) |
| 3 | **DELL** | 329.39 | - | **-** | 26 | - | NEG -$14.8M | - | 360 | 350 | +$6.3M | +$0 bull / -$35k bear | out (clean 33, ADX 21, RVol 1.6) |
| 4 | **IWM** | 272.87 | - | **-** | 25 | - | NEG -$2.7B | 285.92 | 285 | 270 | +$54.6M | +$368k bull / -$70k bear | out (clean 36, ADX 30, RVol 1.4) |
| 5 | **PLTR** | 156.43 | - | **-** | 25 | - | NEG -$48.3M | - | 165 | 160 | +$12.4M | +$0 bull / -$373k bear | out (clean 28, ADX 20, RVol 0.7) |
| 6 | **QQQ** | 656.94 | - | **-** | 23 | - | NEG -$4.8B | - | 700 | 680 | +$821.7M | +$2.8M bull / -$4.3M bear | out (clean 35, ADX 25, RVol 1.1) |
| 7 | **SMH** | 460.30 | - | **-** | 23 | - | NEG -$323.3M | - | 505 | 500 | +$28.5M | +$91k bull / -$608k bear | out (clean 34, ADX 22, RVol 0.8) |
| 8 | **TSLA** | 344.56 | - | **-** | 23 | - | NEG -$140.7M | - | 370 | 350 | +$109.2M | +$932k bull / -$464k bear | out (clean 35, ADX 23, RVol 1.4) |
| 9 | **MU** | 690.50 | - | **-** | 23 | - | NEG -$92.2M | - | 700 | 700 | +$216.8M | +$3.3M bull / -$3.5M bear | out (clean 32, ADX 22, RVol 2.0) |
| 10 | **BABA** | 107.92 | - | **-** | 23 | - | POS +$17.7M | - | 110 | 110 | +$929k | +$0 bull / -$29k bear | out (clean 35, ADX 15, RVol 1.6) |
| 11 | **NVDA** | 184.58 | - | **-** | 22 | - | NEG -$255.6M | - | 200 | 190 | +$70.9M | +$2.0M bull / -$802k bear | out (clean 33, ADX 26, RVol 0.9) |
| 12 | **AAPL** | 345.31 | - | **-** | 20 | - | POS +$529.0M | 334.66 | 350 | 340 | +$24.2M | +$342k bull / -$342k bear | out (clean 31, ADX 20, RVol 0.8) |
| 13 | **AMZN** | 261.26 | - | **-** | 20 | - | POS +$413.8M | - | 265 | 250 | +$22.9M | +$128k bull / -$117k bear | out (clean 34, ADX 17, RVol 0.6) |
| 14 | **GOOGL** | 285.42 | - | **-** | 20 | - | POS +$37.7M | 281.06 | 290 | 290 | +$8.2M | +$35k bull / +$0 bear | out (clean 34, ADX 15, RVol 0.7) |
| 15 | **HOOD** | 78.94 | - | **-** | 20 | - | NEG -$8.6M | - | 85 | 80 | +$1.9M | +$26k bull / +$0 bear | out (clean 30, ADX 26, RVol 1.1) |
| 16 | **AMD** | 419.86 | - | **-** | 19 | - | NEG -$105.2M | - | 430 | 440 | +$33.4M | +$711k bull / -$67k bear | out (clean 32, ADX 20, RVol 0.5) |
| 17 | **CRM** | 222.13 | - | **-** | 19 | - | NEG -$16.8M | - | 240 | 220 | +$552k | - | out (clean 34, ADX 19, RVol 1.3) |
| 18 | **MSTR** | 130.52 | - | **-** | 17 | - | POS +$70.7M | - | 135 | 125 | +$3.1M | +$60k bull / +$0 bear | out (clean 33, ADX 17, RVol 0.6) |
| 19 | **META** | 607.47 | - | **-** | 16 | - | NEG -$105.4M | 621.42 | 650 | 600 | +$16.7M | +$39k bull / -$385k bear | out (clean 33, ADX 12, RVol 0.4) |
| 20 | **AVGO** | 299.39 | - | **-** | 14 | - | NEG -$108.6M | - | 325 | 300 | +$8.7M | - | out (clean 31, ADX 22, RVol 1.0) |
| 21 | **NFLX** | 65.17 | - | **-** | 12 | - | POS +$30.3M | 62.09 | 65 | 65 | +$862k | - | out (clean 32, ADX 25, RVol 0.9) |
| 22 | **COIN** | 139.26 | - | **-** | 12 | - | POS +$25.5M | - | 142 | 135 | +$1.5M | - | out (clean 33, ADX 24, RVol 0.6) |
| 23 | **SMCI** | 27.61 | - | **-** | 12 | - | NEG -$3.9M | - | 30 | 30 | +$348k | - | out (clean 35, ADX 22, RVol 1.6) |
| 24 | **ARM** | 170.33 | - | **-** | 12 | - | NEG -$7.2M | - | 180 | 180 | +$1.4M | - | out (clean 26, ADX 15, RVol 0.9) |
| 25 | **UBER** | 68.66 | - | **-** | 10 | - | POS +$4.1M | 68.01 | 70 | 65 | +$193k | - | out (clean 30, ADX 12, RVol 0.9) |
| 26 | **ORCL** | 116.39 | - | **-** | 9 | - | NEG -$58.6M | - | 125 | 115 | +$2.6M | - | out (clean 31, ADX 17, RVol 0.7) |
| 27 | **SHOP** | 145.25 | - | **-** | 7 | - | NEG -$4.5M | - | 144 | 135 | -$138k | - | out (clean 37, ADX 14, RVol 0.4) |

## Big prints this scan (61)
- **SMH** PUT 470 2026-11-06 (1DTE): 150 @ 18.65 = **+$280k** BUY | vol 12,298 / OI 11,200
- **QQQ** CALL 650 2026-11-06 (1DTE): 200 @ 9.55 = **+$191k** SELL | vol 9,757 / OI 889
- **QQQ** CALL 650 2026-11-06 (1DTE): 200 @ 9.24 = **+$185k** SELL | vol 9,757 / OI 889
- **QQQ** PUT 685 2026-11-05 (0DTE): 55 @ 33.54 = **+$184k** BUY | vol 9,080 / OI 2,551
- **MU** PUT 720 2026-11-06 (1DTE): 35 @ 52.00 = **+$182k** BUY | vol 6,384 / OI 607
- **QQQ** CALL 652 2026-11-06 (1DTE): 200 @ 8.40 = **+$168k** SELL | vol 7,917 / OI 0
- **SMH** CALL 445 2026-11-06 (1DTE): 100 @ 16.33 = **+$163k** SELL | vol 135 / OI 0
- **QQQ** PUT 655 2026-11-05 (0DTE): 339 @ 4.75 = **+$161k** BUY | vol 158,858 / OI 1,387
- **MSFT** PUT 535 2026-11-11 (6DTE): 150 @ 8.94 = **+$134k** BUY | vol 731 / OI 60
- **MU** PUT 720 2026-11-06 (1DTE): 25 @ 52.00 = **+$130k** BUY | vol 6,384 / OI 607
- **QQQ** PUT 675 2026-11-05 (0DTE): 55 @ 23.57 = **+$130k** BUY | vol 34,892 / OI 1,830
- **MU** CALL 700 2026-11-06 (1DTE): 100 @ 12.35 = **+$124k** SELL | vol 29,260 / OI 61
- **MSFT** PUT 532.5 2026-11-11 (6DTE): 150 @ 8.03 = **+$120k** BUY | vol 358 / OI 1
- **NVDA** PUT 185 2026-11-06 (1DTE): 225 @ 5.01 = **+$113k** BUY | vol 82,905 / OI 9,821
- **SPY** PUT 758 2026-11-06 (1DTE): 50 @ 22.00 = **+$110k** BUY | vol 8,235 / OI 2,698

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 736 2026-11-11 (6DTE): 518 traded vs OI 0
- **SPY** PUT 760 2026-11-13 (8DTE): 4,511 traded vs OI 4,486
- **SPY** CALL 738 2026-12-04 (29DTE): 512 traded vs OI 9
- **SPY** CALL 737 2026-11-20 (15DTE): 503 traded vs OI 105
- **QQQ** PUT 650 2026-11-20 (15DTE): 44,805 traded vs OI 44,257
- **QQQ** PUT 650 2026-11-19 (14DTE): 563 traded vs OI 0
- **QQQ** CALL 692 2026-11-20 (15DTE): 559 traded vs OI 554
- **QQQ** CALL 670 2026-11-18 (13DTE): 500 traded vs OI 0
- **QQQ** PUT 625 2026-11-30 (25DTE): 713 traded vs OI 705
- **NVDA** PUT 180 2026-11-27 (22DTE): 2,680 traded vs OI 2,521
- **TSLA** CALL 360 2026-11-27 (22DTE): 514 traded vs OI 285
- **AAPL** CALL 347.5 2026-11-13 (8DTE): 546 traded vs OI 337
- **MSFT** CALL 565 2026-11-13 (8DTE): 666 traded vs OI 658
- **AVGO** PUT 270 2026-11-09 (4DTE): 529 traded vs OI 0
- **AVGO** CALL 320 2026-12-04 (29DTE): 687 traded vs OI 91

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
