# GEX + FLOW SCAN - Thu Nov 05, 03:35 PM ET
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
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors
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
| 1 | **GOOGL** | 284.55 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 38 | none: 69 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$25.3M | 281.62 | 285 | 290 | +$8.8M | +$94k bull / +$0 bear | out (clean 34, ADX 15, RVol 0.7) |
| 2 | **SPY** | 735.72 | - | **-** | 26 | - | NEG -$14.0B | 769.32 | 760 | 740 | +$1.3B | +$9.6M bull / -$103k bear | out (clean 36, ADX 25, RVol 1.7) |
| 3 | **NFLX** | 64.84 | PINNED between the walls (positive gamma) - chop | **-** | 26 | - | POS +$27.3M | 62.6 | 65 | 65 | +$747k | - | out (clean 32, ADX 24, RVol 1.0) |
| 4 | **AVGO** | 295.50 | - | **-** | 26 | - | NEG -$114.7M | - | 325 | 300 | +$9.6M | +$376k bull / +$0 bear | out (clean 31, ADX 20, RVol 2.0) |
| 5 | **DELL** | 322.87 | - | **-** | 26 | - | NEG -$16.2M | - | 350 | 340 | +$6.6M | +$28k bull / +$0 bear | out (clean 32, ADX 19, RVol 1.8) |
| 6 | **QQQ** | 651.96 | - | **-** | 25 | - | NEG -$4.8B | - | 700 | 650 | +$860.3M | +$7.5M bull / -$300k bear | out (clean 35, ADX 20, RVol 2.4) |
| 7 | **PLTR** | 155.12 | - | **-** | 25 | - | NEG -$56.3M | - | 165 | 150 | +$12.4M | +$90k bull / +$0 bear | out (clean 27, ADX 15, RVol 1.3) |
| 8 | **MSFT** | 535.41 | - | **-** | 24 | - | POS +$716.1M | - | 540 | 500 | +$23.0M | +$248k bull / +$0 bear | out (clean 32, ADX 22, RVol 0.9) |
| 9 | **SMH** | 453.86 | - | **-** | 23 | - | NEG -$282.9M | - | 445 | 465 | +$30.1M | +$303k bull / +$0 bear | out (clean 34, ADX 18, RVol 1.3) |
| 10 | **TSLA** | 343.52 | - | **-** | 23 | - | NEG -$161.7M | - | 350 | 350 | +$110.4M | +$285k bull / -$854k bear | out (clean 35, ADX 15, RVol 2.7) |
| 11 | **MU** | 675.02 | - | **-** | 22 | - | NEG -$104.1M | - | 700 | 700 | +$237.1M | +$4.2M bull / -$976k bear | out (clean 31, ADX 18, RVol 1.9) |
| 12 | **BABA** | 107.99 | - | **-** | 22 | - | POS +$19.8M | - | 110 | 110 | +$832k | +$0 bull / -$27k bear | out (clean 35, ADX 23, RVol 1.3) |
| 13 | **NVDA** | 182.99 | - | **-** | 21 | - | NEG -$276.7M | - | 200 | 190 | +$75.5M | +$809k bull / -$68k bear | out (clean 33, ADX 18, RVol 0.9) |
| 14 | **AAPL** | 346.02 | - | **-** | 21 | - | POS +$524.7M | 335.28 | 350 | 330 | +$25.9M | +$138k bull / -$223k bear | out (clean 31, ADX 17, RVol 2.0) |
| 15 | **AMZN** | 259.65 | - | **-** | 20 | - | POS +$348.9M | - | 265 | 250 | +$25.3M | +$74k bull / -$65k bear | out (clean 34, ADX 14, RVol 0.7) |
| 16 | **MSTR** | 129.73 | - | **-** | 20 | - | POS +$48.2M | - | 135 | 125 | +$4.2M | +$26k bull / -$33k bear | out (clean 33, ADX 17, RVol 1.4) |
| 17 | **AMD** | 412.76 | - | **-** | 19 | - | NEG -$113.2M | - | 430 | 440 | +$36.8M | +$471k bull / +$0 bear | out (clean 32, ADX 16, RVol 0.8) |
| 18 | **CRM** | 221.60 | - | **-** | 19 | - | NEG -$18.3M | - | 240 | 220 | +$560k | - | out (clean 33, ADX 16, RVol 1.9) |
| 19 | **ORCL** | 115.30 | - | **-** | 18 | - | NEG -$66.4M | - | 125 | 115 | +$2.9M | +$27k bull / +$0 bear | out (clean 31, ADX 12, RVol 0.5) |
| 20 | **IWM** | 271.18 | - | **-** | 14 | - | NEG -$2.9B | - | 285 | 270 | +$57.0M | - | out (clean 36, ADX 21, RVol 1.7) |
| 21 | **COIN** | 137.42 | - | **-** | 13 | - | POS +$11.0M | 134.07 | 142 | 130 | +$1.6M | - | out (clean 33, ADX 25, RVol 0.8) |
| 22 | **ARM** | 168.73 | - | **-** | 12 | - | NEG -$6.7M | - | 180 | 180 | +$1.5M | - | out (clean 26, ADX 15, RVol 1.2) |
| 23 | **HOOD** | 78.41 | - | **-** | 10 | - | NEG -$14.5M | - | 85 | 80 | +$2.4M | - | out (clean 31, ADX 22, RVol 1.1) |
| 24 | **UBER** | 68.50 | - | **-** | 10 | - | POS +$878k | 68.3 | 70 | 65 | +$199k | - | out (clean 30, ADX 12, RVol 0.9) |
| 25 | **SMCI** | 27.25 | - | **-** | 8 | - | NEG -$4.2M | - | 28 | 27 | +$174k | - | out (clean 34, ADX 22, RVol 0.8) |
| 26 | **SHOP** | 143.95 | - | **-** | 7 | - | NEG -$6.0M | - | 144 | 135 | -$130k | - | out (clean 37, ADX 12, RVol 0.7) |
| 27 | **META** | 606.01 | - | **-** | 6 | - | NEG -$147.1M | 624.14 | 650 | 600 | +$18.1M | - | out (clean 33, ADX 10, RVol 0.7) |

## Big prints this scan (78)
- **SPY** CALL 730 2026-11-10 (5DTE): 500 @ 12.50 = **+$625k** BUY | vol 8,346 / OI 5
- **SPY** CALL 730 2026-11-10 (5DTE): 293 @ 12.50 = **+$366k** BUY | vol 8,346 / OI 5
- **SPY** PUT 732 2026-11-06 (1DTE): 740 @ 3.79 = **+$280k** SELL | vol 20,574 / OI 3,388
- **SPY** CALL 730 2026-11-10 (5DTE): 207 @ 12.50 = **+$259k** BUY | vol 8,346 / OI 5
- **SPY** PUT 736 2026-11-06 (1DTE): 443 @ 5.41 = **+$240k** SELL | vol 28,564 / OI 3,602
- **SPY** PUT 735 2026-11-06 (1DTE): 443 @ 4.96 = **+$220k** SELL | vol 77,771 / OI 24,589
- **QQQ** PUT 671 2026-11-05 (0DTE): 100 @ 19.65 = **+$196k** BUY | vol 25,935 / OI 100
- **QQQ** CALL 655 2026-11-06 (1DTE): 302 @ 6.39 = **+$193k** BUY | vol 42,956 / OI 1,189
- **QQQ** PUT 667 2026-11-05 (0DTE): 100 @ 15.68 = **+$157k** MID | vol 29,035 / OI 165
- **NVDA** PUT 182.5 2026-11-11 (6DTE): 200 @ 6.50 = **+$130k** MID | vol 2,942 / OI 146
- **MU** PUT 680 2026-11-06 (1DTE): 50 @ 24.00 = **+$120k** SELL | vol 30,508 / OI 702
- **QQQ** PUT 660 2026-11-06 (1DTE): 95 @ 12.52 = **+$119k** MID | vol 39,668 / OI 14,507
- **QQQ** PUT 671 2026-11-05 (0DTE): 60 @ 19.38 = **+$116k** MID | vol 25,935 / OI 100
- **MU** PUT 687.5 2026-11-11 (6DTE): 26 @ 43.75 = **+$114k** SELL | vol 653 / OI 0
- **AAPL** PUT 340 2026-11-06 (1DTE): 660 @ 1.67 = **+$110k** BUY | vol 84,125 / OI 3,898

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 724 2026-11-10 (5DTE): 527 traded vs OI 112
- **SPY** PUT 712 2026-11-11 (6DTE): 697 traded vs OI 44
- **SPY** PUT 730 2026-11-11 (6DTE): 1,699 traded vs OI 1,588
- **SPY** CALL 770 2026-11-30 (25DTE): 2,292 traded vs OI 2,273
- **SPY** CALL 745 2026-11-20 (15DTE): 3,390 traded vs OI 3,377
- **QQQ** CALL 653 2026-11-12 (7DTE): 557 traded vs OI 0
- **SMH** CALL 462.5 2026-11-06 (1DTE): 1,049 traded vs OI 0
- **TSLA** CALL 342.5 2026-11-20 (15DTE): 502 traded vs OI 43
- **TSLA** PUT 377.5 2026-11-06 (1DTE): 1,039 traded vs OI 0
- **AAPL** CALL 380 2026-11-20 (15DTE): 1,058 traded vs OI 0
- **AAPL** CALL 380 2026-11-27 (22DTE): 559 traded vs OI 0
- **AMD** PUT 372.5 2026-11-06 (1DTE): 509 traded vs OI 0
- **META** CALL 660 2026-11-13 (8DTE): 523 traded vs OI 514
- **HOOD** PUT 81 2026-12-04 (29DTE): 509 traded vs OI 89

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
