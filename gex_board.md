# GEX + FLOW SCAN - Thu Nov 05, 09:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.42 | -12% (0m) | **-12%** | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.57 | -4% (0m) | **-27%** | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:50:08 ET, last candle SPY 09:49, QQQ 09:49 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (1 today, last 5)
- 09:50 NFLX CALLS: price -0.87 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BABA** | 107.40 | TREND + FLOW | **CALLS** | 67 | 11/06 111C @ 0.48 (delta 0.20) = est +136% at 110 | POS +$22.1M | - | 110 | 110 | +$97k | - | LONG (clean 37, ADX 37, RVol 8.1) |
| 2 | **NVDA** | 190.92 | FLOW SURGE | **CALLS** | 66 | none: 42 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$300.4M | - | 210 | 190 | +$12.8M | +$1.6M bull / +$0 bear | out (clean 31, ADX 47, RVol 5.4) |
| 3 | **TSLA** | 350.91 | FLOW SURGE | **CALLS** | 64 | none: 76 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | NEG -$165.9M | - | 370 | 350 | +$34.8M | +$931k bull / +$0 bear | out (clean 33, ADX 40, RVol 6.2) |
| 4 | **DELL** | 339.42 | FLOW SURGE | **CALLS** | 64 | none: 22 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | NEG -$18.6M | - | 360 | 350 | +$1.5M | +$132k bull / +$0 bear | out (clean 33, ADX 32, RVol 4.6) |
| 5 | **MU** | 722.86 | FLOW SURGE | **CALLS** | 64 | none: 103 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$163.5M | - | 700 | 750 | +$27.5M | +$3.7M bull / +$0 bear | out (clean 31, ADX 44, RVol 4.8) |
| 6 | **SPY** | 755.97 | FLOW SURGE | **CALLS** | 62 | none: 669 calls 0-7DTE > 17 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (278 contracts' greeks worked out here) | NEG -$8.8B | 769.16 | 770 | 750 | +$122.0M | +$5.2M bull / +$0 bear | out (clean 33, ADX 32, RVol 4.5) |
| 7 | **AVGO** | 309.11 | FLOW SURGE | **CALLS** | 62 | none: 70 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | NEG -$138.2M | - | 340 | 300 | +$753k | +$87k bull / +$0 bear | out (clean 30, ADX 39, RVol 4.6) |
| 8 | **PLTR** | 158.46 | FLOW SURGE | **CALLS** | 62 | none: 16 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$48.2M | - | 165 | 160 | +$4.0M | +$204k bull / +$0 bear | out (clean 27, ADX 28, RVol 4.5) |
| 9 | **SMCI** | 27.58 | TREND (flow not with it) | **PUTS** | 61 | 11/06 27P @ 0.62 (delta 0.40) = est +47% at 26.83 | NEG -$4.2M | - | 30 | 30 | +$114k | - | SHORT (clean 34, ADX 35, RVol 3.4) |
| 10 | **SHOP** | 144.12 | TREND (flow not with it) | **PUTS** | 60 | none: 24 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$4.3M | - | 144 | 135 | +$18k | - | SHORT (clean 34, ADX 39, RVol 2.5) |
| 11 | **QQQ** | 669.62 | FLOW SURGE | **CALLS** | 59 | none: 562 calls 0-7DTE > 35 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (136 contracts' greeks worked out here) | NEG -$6.0B | - | 700 | 680 | +$123.4M | +$9.1M bull / +$0 bear | out (clean 33, ADX 33, RVol 3.5) |
| 12 | **NFLX** | 65.78 | FLOW SURGE | **CALLS** | 59 | 11/06 66C @ 0.74 (delta 0.48) = est +39% at 66.4 | POS +$32.6M | 62.22 | 65 | 65 | +$163k | +$54k bull / +$0 bear | out (clean 33, ADX 31, RVol 3.2) |
| 13 | **AMD** | 435.08 | FLOW SURGE | **CALLS** | 57 | none: 105 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | NEG -$130.4M | - | 430 | 440 | +$7.4M | +$1.4M bull / +$0 bear | out (clean 31, ADX 27, RVol 4.4) |
| 14 | **META** | 614.18 | FLOW SURGE | **CALLS** | 56 | none: 147 calls 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | NEG -$66.7M | 619.55 | 650 | 600 | +$3.6M | +$317k bull / +$0 bear | out (clean 32, ADX 21, RVol 2.0) |
| 15 | **MSFT** | 546.79 | FLOW SURGE | **CALLS** | 56 | none: 132 calls 0-7DTE > 14 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (40 contracts' greeks worked out here) | POS +$1.0B | - | 550 | 535 | +$2.5M | +$410k bull / +$0 bear | out (clean 30, ADX 31, RVol 3.5) |
| 16 | **GOOGL** | 287.95 | FLOW SURGE | **CALLS** | 55 | none: 69 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$61.4M | 281.49 | 290 | 290 | +$2.2M | +$274k bull / +$0 bear | out (clean 35, ADX 20, RVol 2.6) |
| 17 | **AMZN** | 265.12 | FLOW SURGE | **CALLS** | 52 | none: 63 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$499.9M | - | 270 | 250 | +$2.7M | +$517k bull / +$0 bear | out (clean 34, ADX 16, RVol 4.0) |
| 18 | **ARM** | 174.24 | - | **-** | 34 | - | NEG -$9.3M | - | 180 | 180 | +$487k | +$0 bull / -$277k bear | out (clean 26, ADX 41, RVol 6.8) |
| 19 | **ORCL** | 119.05 | - | **-** | 31 | - | NEG -$53.6M | - | 130 | 120 | +$501k | - | out (clean 33, ADX 38, RVol 2.0) |
| 20 | **MSTR** | 135.56 | - | **-** | 29 | - | POS +$121.0M | - | 135 | 135 | +$651k | - | out (clean 32, ADX 47, RVol 2.8) |
| 21 | **COIN** | 144.10 | - | **-** | 28 | - | POS +$35.1M | - | 143 | 140 | +$92k | - | out (clean 31, ADX 26, RVol 1.5) |
| 22 | **UBER** | 68.39 | - | **-** | 28 | - | POS +$2.0M | 68.01 | 70 | 65 | +$61k | - | out (clean 31, ADX 24, RVol 3.5) |
| 23 | **HOOD** | 81.32 | - | **-** | 26 | - | NEG -$6.7M | - | 86 | 80 | +$204k | - | out (clean 29, ADX 33, RVol 2.0) |
| 24 | **AAPL** | 352.89 | - | **-** | 24 | - | POS +$827.8M | 333.68 | 350 | 340 | -$1.3M | +$430k bull / -$240k bear | out (clean 32, ADX 21, RVol 4.3) |
| 25 | **SMH** | 473.71 | - | **-** | 23 | - | NEG -$425.3M | - | 520 | 500 | +$325k | +$569k bull / +$0 bear | out (clean 33, ADX 32, RVol 4.7) |
| 26 | **IWM** | 280.80 | - | **-** | 21 | - | NEG -$1.2B | 285.14 | 285 | 270 | +$3.0M | - | out (clean 34, ADX 17, RVol 3.4) |
| 27 | **CRM** | 223.91 | - | **-** | 9 | - | NEG -$14.4M | - | 240 | 220 | +$665 | - | out (clean 34, ADX 17, RVol 2.3) |

## Big prints this scan (263)
- **QQQ** PUT 700 2026-11-06 (1DTE): 999 @ 21.30 = **+$2.1M** SELL | vol 3,962 / OI 19,842
- **QQQ** PUT 700 2026-11-06 (1DTE): 998 @ 20.50 = **+$2.0M** SELL | vol 3,962 / OI 19,842
- **QQQ** PUT 700 2026-11-06 (1DTE): 898 @ 20.60 = **+$1.8M** SELL | vol 3,962 / OI 19,842
- **SPY** PUT 772 2026-11-10 (5DTE): 1,000 @ 10.00 = **+$1.0M** SELL | vol 3,009 / OI 1
- **SPY** PUT 772 2026-11-10 (5DTE): 1,000 @ 9.50 = **+$950k** SELL | vol 3,009 / OI 1
- **SPY** PUT 769 2026-11-05 (0DTE): 855 @ 5.65 = **+$483k** SELL | vol 2,084 / OI 3
- **MU** CALL 755 2026-11-06 (1DTE): 300 @ 15.75 = **+$472k** BUY | vol 1,525 / OI 4
- **MU** CALL 755 2026-11-06 (1DTE): 300 @ 14.45 = **+$434k** BUY | vol 1,525 / OI 4
- **SPY** PUT 770 2026-11-06 (1DTE): 500 @ 6.95 = **+$348k** SELL | vol 1,780 / OI 6,051
- **SPY** PUT 767 2026-11-05 (0DTE): 855 @ 4.00 = **+$342k** SELL | vol 7,168 / OI 28
- **SPY** PUT 767 2026-11-06 (1DTE): 668 @ 4.25 = **+$284k** SELL | vol 3,626 / OI 1,033
- **SPY** PUT 770 2026-11-06 (1DTE): 400 @ 6.95 = **+$278k** SELL | vol 1,780 / OI 6,051
- **NVDA** CALL 195 2026-11-11 (6DTE): 500 @ 5.20 = **+$260k** BUY | vol 567 / OI 47
- **SPY** PUT 767 2026-11-06 (1DTE): 500 @ 4.65 = **+$232k** SELL | vol 3,626 / OI 1,033
- **QQQ** CALL 682 2026-11-05 (0DTE): 1,001 @ 2.20 = **+$220k** BUY | vol 4,140 / OI 39

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 776 2026-11-05 (0DTE): 1,576 traded vs OI 933
- **SPY** PUT 760 2026-11-05 (0DTE): 22,790 traded vs OI 3,384
- **SPY** CALL 762 2026-11-05 (0DTE): 2,319 traded vs OI 960
- **SPY** PUT 746 2026-11-05 (0DTE): 1,177 traded vs OI 805
- **SPY** PUT 769 2026-11-05 (0DTE): 2,084 traded vs OI 3
- **SPY** CALL 761 2026-11-05 (0DTE): 637 traded vs OI 291
- **SPY** PUT 767 2026-11-06 (1DTE): 3,626 traded vs OI 1,033
- **SPY** PUT 755 2026-11-05 (0DTE): 6,108 traded vs OI 2,900
- **SPY** PUT 771 2026-11-05 (0DTE): 590 traded vs OI 2
- **SPY** PUT 764 2026-11-09 (4DTE): 733 traded vs OI 5
- **SPY** CALL 764 2026-11-05 (0DTE): 7,144 traded vs OI 467
- **SPY** PUT 766 2026-11-06 (1DTE): 1,341 traded vs OI 1,088
- **SPY** PUT 753 2026-11-05 (0DTE): 2,884 traded vs OI 748
- **SPY** PUT 772 2026-11-10 (5DTE): 3,009 traded vs OI 1
- **SPY** PUT 751 2026-11-05 (0DTE): 3,881 traded vs OI 238

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
