# GEX + FLOW SCAN - Thu Nov 05, 12:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:55 | **BABA** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/06 102P | 0.75 | 0.33 | -5% (9m) | **-56%** (done) | +27% | 103.58 |
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 11.35 | +1355% (60m) | **+1355%** (done) | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.20 | -12% (0m) | **-58%** (done) | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.10 | -4% (0m) | **-87%** (done) | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:20:08 ET, last candle SPY 12:19, QQQ 12:19 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:44 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:38 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 64 puts 0-1DTE > 1 priced 0.40-0.80 > 0 delta 0.15+ > 0 spread ok > 0 liquid  |
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (32 today, last 5)
- 12:20 IWM CALLS: under EMA 20 - flow says one way, price says the other
- 12:15 IWM CALLS: price -0.86 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:10 IWM CALLS: price -1.05 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:05 IWM CALLS: price -1.32 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:00 IWM CALLS: price -0.69 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 273.42 | FLOW SURGE | **CALLS** | 52 | 11/05 275C @ 0.44 (delta 0.27) = est +116% at 275.37 | NEG -$2.6B | 286.47 | 285 | 270 | +$54.5M | +$168k bull / +$0 bear | SHORT (clean 36, ADX 53, RVol 1.6) |
| 2 | **SPY** | 741.41 | FLOW SURGE | **CALLS** | 44 | none: 662 calls 0-7DTE > 25 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (245 contracts' greeks worked out here) | NEG -$12.8B | 769.87 | 760 | 740 | +$1.1B | +$1.6M bull / -$559k bear | out (clean 36, ADX 58, RVol 1.1) |
| 3 | **TSLA** | 342.99 | TREND (flow not with it) | **PUTS** | 41 | none: 71 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$129.8M | - | 370 | 350 | +$104.0M | +$1.2M bull / +$0 bear | SHORT (clean 35, ADX 43, RVol 1.8) |
| 4 | **PLTR** | 155.89 | FLOW SURGE | **CALLS** | 40 | none: 15 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$45.4M | - | 165 | 150 | +$13.1M | +$176k bull / +$0 bear | out (clean 28, ADX 38, RVol 0.4) |
| 5 | **SMH** | 459.85 | - | **-** | 34 | - | NEG -$314.8M | - | 505 | 500 | +$40.3M | +$31k bull / -$160k bear | out (clean 35, ADX 45, RVol 1.6) |
| 6 | **COIN** | 136.15 | - | **-** | 31 | - | POS +$16.4M | - | 142 | 135 | +$2.1M | +$0 bull / -$32k bear | out (clean 33, ADX 48, RVol 0.6) |
| 7 | **QQQ** | 657.29 | - | **-** | 28 | - | NEG -$4.9B | - | 700 | 680 | +$756.8M | +$2.1M bull / -$1.4M bear | out (clean 35, ADX 49, RVol 1.1) |
| 8 | **NVDA** | 185.61 | - | **-** | 28 | - | NEG -$263.3M | - | 200 | 190 | +$59.7M | +$413k bull / -$199k bear | out (clean 33, ADX 46, RVol 1.4) |
| 9 | **MSFT** | 542.62 | - | **-** | 28 | - | POS +$885.0M | - | 540 | 500 | +$19.1M | +$138k bull / -$31k bear | out (clean 32, ADX 36, RVol 1.6) |
| 10 | **AVGO** | 302.31 | - | **-** | 27 | - | NEG -$119.5M | - | 330 | 300 | +$7.4M | +$38k bull / -$46k bear | out (clean 31, ADX 32, RVol 1.0) |
| 11 | **MU** | 696.39 | - | **-** | 27 | - | NEG -$100.3M | - | 700 | 750 | +$184.6M | +$5.4M bull / -$2.6M bear | out (clean 33, ADX 42, RVol 1.3) |
| 12 | **ARM** | 170.16 | - | **-** | 26 | - | NEG -$7.0M | - | 180 | 180 | +$1.4M | +$28k bull / +$0 bear | out (clean 27, ADX 38, RVol 0.7) |
| 13 | **AMD** | 419.04 | - | **-** | 25 | - | NEG -$102.4M | - | 430 | 440 | +$38.0M | +$56k bull / -$145k bear | out (clean 33, ADX 41, RVol 0.8) |
| 14 | **AAPL** | 345.44 | - | **-** | 24 | - | POS +$507.0M | 334.43 | 350 | 330 | +$20.1M | +$63k bull / -$760k bear | out (clean 31, ADX 30, RVol 1.4) |
| 15 | **MSTR** | 128.54 | - | **-** | 24 | - | POS +$50.3M | - | 135 | 125 | +$3.6M | +$0 bull / -$81k bear | out (clean 34, ADX 41, RVol 1.0) |
| 16 | **HOOD** | 78.04 | - | **-** | 23 | - | NEG -$9.0M | - | 85 | 80 | +$1.8M | +$0 bull / -$63k bear | out (clean 32, ADX 46, RVol 0.6) |
| 17 | **SHOP** | 144.25 | TREND (flow not with it) | **CALLS** | 23 | none: 24 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$4.7M | - | 144 | 135 | -$136k | +$0 bull / -$32k bear | LONG (clean 38, ADX 28, RVol 0.4) |
| 18 | **AMZN** | 262.17 | - | **-** | 22 | - | POS +$412.7M | - | 265 | 250 | +$21.3M | +$316k bull / -$316k bear | out (clean 35, ADX 19, RVol 1.2) |
| 19 | **META** | 608.71 | - | **-** | 18 | - | NEG -$88.2M | 621.17 | 650 | 600 | +$17.1M | +$0 bull / -$1.0M bear | out (clean 34, ADX 20, RVol 0.8) |
| 20 | **DELL** | 328.03 | - | **-** | 18 | - | NEG -$14.4M | - | 360 | 340 | +$6.1M | - | out (clean 35, ADX 33, RVol 0.9) |
| 21 | **BABA** | 107.13 | - | **-** | 18 | - | POS +$21.2M | - | 110 | 110 | +$1.2M | - | out (clean 38, ADX 22, RVol 0.7) |
| 22 | **CRM** | 223.12 | - | **-** | 17 | - | NEG -$14.9M | - | 240 | 220 | +$517k | - | out (clean 34, ADX 17, RVol 0.3) |
| 23 | **SMCI** | 26.77 | - | **-** | 15 | - | NEG -$3.0M | - | 28 | 27 | +$420k | - | out (clean 36, ADX 37, RVol 0.9) |
| 24 | **ORCL** | 115.30 | - | **-** | 15 | - | NEG -$57.7M | - | 125 | 115 | +$2.6M | - | out (clean 34, ADX 40, RVol 1.3) |
| 25 | **NFLX** | 65.55 | - | **-** | 13 | - | POS +$33.1M | 62.17 | 65 | 65 | +$773k | - | out (clean 32, ADX 20, RVol 0.7) |
| 26 | **GOOGL** | 286.62 | - | **-** | 11 | - | POS +$39.5M | 281.66 | 290 | 290 | +$7.7M | - | out (clean 35, ADX 17, RVol 0.8) |
| 27 | **UBER** | 68.63 | - | **-** | 9 | - | POS +$5.5M | 67.92 | 70 | 65 | +$150k | - | out (clean 32, ADX 12, RVol 0.7) |

## Big prints this scan (133)
- **QQQ** CALL 663 2026-11-09 (4DTE): 752 @ 7.99 = **+$601k** BUY | vol 16,910 / OI 0
- **META** PUT 610 2026-11-06 (1DTE): 296 @ 12.90 = **+$382k** BUY | vol 4,765 / OI 3,587
- **QQQ** PUT 640 2026-11-09 (4DTE): 676 @ 4.93 = **+$333k** SELL | vol 11,259 / OI 5,186
- **META** PUT 610 2026-11-06 (1DTE): 204 @ 12.90 = **+$263k** BUY | vol 4,765 / OI 3,587
- **SPY** PUT 761 2026-11-06 (1DTE): 98 @ 20.51 = **+$201k** BUY | vol 4,906 / OI 5,109
- **SPY** PUT 755 2026-11-06 (1DTE): 125 @ 14.57 = **+$182k** SELL | vol 19,596 / OI 8,694
- **SPY** PUT 755 2026-11-06 (1DTE): 125 @ 14.57 = **+$182k** SELL | vol 19,596 / OI 8,694
- **SPY** PUT 774 2026-11-06 (1DTE): 49 @ 33.33 = **+$163k** MID | vol 584 / OI 932
- **QQQ** CALL 663 2026-11-09 (4DTE): 200 @ 7.83 = **+$157k** MID | vol 16,910 / OI 0
- **QQQ** PUT 665 2026-11-05 (0DTE): 150 @ 10.25 = **+$154k** BUY | vol 60,703 / OI 2,574
- **QQQ** PUT 640 2026-11-09 (4DTE): 261 @ 5.87 = **+$153k** BUY | vol 11,259 / OI 5,186
- **QQQ** PUT 640 2026-11-09 (4DTE): 250 @ 5.96 = **+$149k** BUY | vol 11,259 / OI 5,186
- **QQQ** PUT 654 2026-11-05 (0DTE): 500 @ 2.95 = **+$148k** BUY | vol 52,638 / OI 307
- **SPY** PUT 761 2026-11-06 (1DTE): 71 @ 20.46 = **+$145k** BUY | vol 4,906 / OI 5,109
- **NVDA** CALL 187.5 2026-11-06 (1DTE): 496 @ 2.85 = **+$141k** SELL | vol 30,025 / OI 151

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 708 2026-11-09 (4DTE): 711 traded vs OI 72
- **SPY** CALL 759 2026-11-10 (5DTE): 544 traded vs OI 75
- **SPY** CALL 736 2026-11-09 (4DTE): 551 traded vs OI 0
- **SPY** CALL 745 2026-11-16 (11DTE): 518 traded vs OI 4
- **SPY** PUT 713 2026-11-12 (7DTE): 504 traded vs OI 96
- **SPY** PUT 738 2026-11-11 (6DTE): 520 traded vs OI 83
- **SPY** CALL 741 2026-11-13 (8DTE): 519 traded vs OI 9
- **SPY** PUT 730 2026-11-18 (13DTE): 503 traded vs OI 0
- **QQQ** PUT 605 2026-11-09 (4DTE): 513 traded vs OI 0
- **QQQ** PUT 645 2026-11-12 (7DTE): 1,300 traded vs OI 1,134
- **QQQ** PUT 656 2026-11-11 (6DTE): 610 traded vs OI 13
- **QQQ** CALL 681 2026-11-09 (4DTE): 513 traded vs OI 12
- **QQQ** PUT 659 2026-11-13 (8DTE): 522 traded vs OI 55
- **QQQ** CALL 655 2026-11-20 (15DTE): 648 traded vs OI 133
- **QQQ** PUT 655 2026-11-13 (8DTE): 1,446 traded vs OI 1,438

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
