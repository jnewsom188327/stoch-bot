# GEX + FLOW SCAN - Thu Nov 05, 01:50 PM ET
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
Last 1m check 13:50:08 ET, last candle SPY 13:49, QQQ 13:49 | no errors
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
| 1 | **MSFT** | 538.83 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 46 | none: 132 puts 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$819.8M | - | 540 | 500 | +$21.4M | +$0 bull / -$264k bear | out (clean 32, ADX 33, RVol 0.9) |
| 2 | **PLTR** | 154.79 | FLOW SURGE | **CALLS** | 38 | none: 16 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$44.7M | - | 165 | 150 | +$13.3M | +$49k bull / +$0 bear | out (clean 28, ADX 27, RVol 0.5) |
| 3 | **MU** | 670.76 | TREND (flow not with it) | **PUTS** | 33 | none: 76 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | NEG -$53.8M | - | 700 | 700 | +$245.1M | +$7.8M bull / -$220k bear | SHORT (clean 34, ADX 31, RVol 1.2) |
| 4 | **SPY** | 736.12 | - | **-** | 30 | - | NEG -$13.0B | 769.41 | 760 | 740 | +$1.2B | +$3.0M bull / -$1.2M bear | out (clean 37, ADX 50, RVol 1.2) |
| 5 | **SMH** | 454.56 | - | **-** | 29 | - | NEG -$258.9M | - | 445 | 500 | +$41.7M | +$449k bull / -$505k bear | out (clean 35, ADX 34, RVol 0.5) |
| 6 | **IWM** | 271.31 | - | **-** | 27 | - | NEG -$2.7B | 287.49 | 285 | 270 | +$54.0M | +$256k bull / +$0 bear | out (clean 37, ADX 46, RVol 0.9) |
| 7 | **QQQ** | 651.74 | - | **-** | 26 | - | NEG -$4.4B | - | 700 | 680 | +$829.4M | +$3.1M bull / -$2.0M bear | out (clean 36, ADX 39, RVol 0.7) |
| 8 | **NVDA** | 182.84 | - | **-** | 26 | - | NEG -$243.1M | - | 200 | 190 | +$73.3M | +$523k bull / -$518k bear | out (clean 34, ADX 42, RVol 0.8) |
| 9 | **AVGO** | 297.30 | - | **-** | 26 | - | NEG -$104.8M | - | 325 | 300 | +$8.9M | +$187k bull / -$32k bear | out (clean 32, ADX 29, RVol 0.7) |
| 10 | **TSLA** | 340.78 | - | **-** | 25 | - | NEG -$130.5M | - | 350 | 350 | +$110.6M | +$1.1M bull / -$81k bear | out (clean 35, ADX 37, RVol 1.1) |
| 11 | **AAPL** | 343.75 | - | **-** | 22 | - | POS +$422.3M | 334.4 | 350 | 330 | +$23.4M | +$516k bull / -$365k bear | out (clean 31, ADX 32, RVol 0.6) |
| 12 | **HOOD** | 76.99 | - | **-** | 22 | - | NEG -$7.7M | - | 83 | 80 | +$2.2M | +$28k bull / -$93k bear | out (clean 32, ADX 35, RVol 1.0) |
| 13 | **AMD** | 412.91 | - | **-** | 21 | - | NEG -$92.7M | - | 430 | 440 | +$34.5M | +$28k bull / +$0 bear | out (clean 34, ADX 32, RVol 0.5) |
| 14 | **AMZN** | 259.40 | - | **-** | 20 | - | POS +$376.8M | - | 265 | 250 | +$23.4M | +$138k bull / -$225k bear | out (clean 35, ADX 17, RVol 0.5) |
| 15 | **GOOGL** | 283.43 | - | **-** | 20 | - | POS +$19.0M | 280.89 | 285 | 290 | +$8.5M | +$0 bull / -$140k bear | out (clean 35, ADX 17, RVol 0.3) |
| 16 | **CRM** | 221.08 | - | **-** | 19 | - | NEG -$16.8M | - | 240 | 220 | +$559k | - | out (clean 34, ADX 21, RVol 1.0) |
| 17 | **MSTR** | 127.85 | - | **-** | 18 | - | POS +$42.9M | - | 135 | 125 | +$3.6M | +$62k bull / -$106k bear | out (clean 34, ADX 21, RVol 0.4) |
| 18 | **META** | 604.31 | - | **-** | 16 | - | NEG -$116.8M | 622.51 | 650 | 600 | +$17.9M | +$0 bull / -$600k bear | out (clean 34, ADX 14, RVol 0.3) |
| 19 | **COIN** | 135.68 | - | **-** | 15 | - | POS +$14.8M | - | 142 | 135 | +$1.9M | - | out (clean 33, ADX 26, RVol 0.3) |
| 20 | **DELL** | 322.83 | - | **-** | 15 | - | NEG -$12.3M | - | 350 | 340 | +$6.2M | - | out (clean 34, ADX 28, RVol 0.5) |
| 21 | **BABA** | 106.78 | - | **-** | 15 | - | POS +$20.6M | - | 110 | 110 | +$1.3M | - | out (clean 36, ADX 10, RVol 0.7) |
| 22 | **NFLX** | 65.34 | - | **-** | 14 | - | POS +$31.1M | 62.18 | 65 | 65 | +$939k | - | out (clean 32, ADX 25, RVol 0.5) |
| 23 | **ARM** | 168.60 | - | **-** | 12 | - | NEG -$6.9M | - | 180 | 180 | +$1.4M | - | out (clean 27, ADX 20, RVol 0.6) |
| 24 | **SMCI** | 26.72 | - | **-** | 11 | - | NEG -$3.0M | - | 28 | 27 | +$415k | - | out (clean 36, ADX 19, RVol 0.7) |
| 25 | **ORCL** | 114.67 | - | **-** | 10 | - | NEG -$56.7M | - | 125 | 115 | +$2.9M | - | out (clean 31, ADX 22, RVol 0.6) |
| 26 | **UBER** | 68.42 | - | **-** | 8 | - | POS +$3.2M | 67.93 | 70 | 65 | +$190k | - | out (clean 32, ADX 8, RVol 0.4) |
| 27 | **SHOP** | 144.23 | - | **-** | 7 | - | NEG -$4.5M | - | 144 | 135 | -$131k | - | out (clean 38, ADX 16, RVol 0.4) |

## Big prints this scan (82)
- **SPY** PUT 750 2026-11-06 (1DTE): 454 @ 14.41 = **+$654k** SELL | vol 43,207 / OI 42,367
- **SPY** PUT 749 2026-11-06 (1DTE): 454 @ 13.57 = **+$616k** SELL | vol 17,771 / OI 10,969
- **MU** CALL 650 2026-11-11 (6DTE): 70 @ 53.80 = **+$377k** BUY | vol 484 / OI 0
- **MU** CALL 650 2026-11-11 (6DTE): 70 @ 53.65 = **+$376k** BUY | vol 484 / OI 0
- **SPY** PUT 735 2026-11-05 (0DTE): 1,257 @ 2.40 = **+$302k** BUY | vol 299,113 / OI 15,976
- **QQQ** CALL 655 2026-11-06 (1DTE): 413 @ 6.86 = **+$283k** BUY | vol 18,216 / OI 1,189
- **QQQ** PUT 650 2026-11-05 (0DTE): 844 @ 2.90 = **+$245k** BUY | vol 253,674 / OI 3,473
- **MU** CALL 650 2026-11-11 (6DTE): 36 @ 53.75 = **+$194k** BUY | vol 484 / OI 0
- **MU** CALL 650 2026-11-11 (6DTE): 36 @ 53.70 = **+$193k** BUY | vol 484 / OI 0
- **MU** PUT 660 2026-11-06 (1DTE): 99 @ 16.00 = **+$158k** SELL | vol 19,011 / OI 0
- **SPY** PUT 750 2026-11-06 (1DTE): 100 @ 14.70 = **+$147k** MID | vol 43,207 / OI 42,367
- **SPY** PUT 752 2026-11-05 (0DTE): 90 @ 15.66 = **+$141k** SELL | vol 81,900 / OI 392
- **SPY** CALL 738 2026-11-06 (1DTE): 280 @ 5.01 = **+$140k** BUY | vol 7,544 / OI 61
- **SPY** PUT 733 2026-11-05 (0DTE): 941 @ 1.48 = **+$139k** SELL | vol 126,045 / OI 705
- **QQQ** PUT 655 2026-11-05 (0DTE): 242 @ 5.50 = **+$133k** SELL | vol 140,841 / OI 1,387

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 732 2026-11-06 (1DTE): 517 traded vs OI 312
- **SPY** CALL 754 2026-11-13 (8DTE): 1,059 traded vs OI 1,005
- **QQQ** PUT 652 2026-11-12 (7DTE): 504 traded vs OI 5
- **QQQ** PUT 610 2026-11-11 (6DTE): 523 traded vs OI 106
- **QQQ** CALL 675 2026-11-12 (7DTE): 514 traded vs OI 17
- **QQQ** PUT 640 2026-11-18 (13DTE): 549 traded vs OI 0
- **IWM** CALL 275 2026-11-10 (5DTE): 502 traded vs OI 17
- **NVDA** CALL 182.5 2026-11-11 (6DTE): 503 traded vs OI 2
- **NVDA** PUT 175 2026-12-04 (29DTE): 2,679 traded vs OI 2,670
- **NVDA** PUT 185 2026-11-18 (13DTE): 500 traded vs OI 105
- **TSLA** CALL 342.5 2026-11-09 (4DTE): 500 traded vs OI 0
- **AMD** PUT 385 2026-11-20 (15DTE): 646 traded vs OI 0
- **SMCI** CALL 28 2026-11-20 (15DTE): 503 traded vs OI 391
- **MU** PUT 690 2026-11-20 (15DTE): 1,805 traded vs OI 1,801
- **ORCL** CALL 115 2026-11-13 (8DTE): 597 traded vs OI 127

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
