# GEX + FLOW SCAN - Tue Nov 03, 10:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:00:08 ET, last candle SPY 09:59, QQQ 09:59 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SHOP** | 141.43 | FLOW SURGE | **PUTS** | 64 | none: 25 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$4.1M | - | 145 | 140 | -$2.0M | +$0 bull / -$1.8M bear | out (clean 31, ADX 52, RVol 6.0) |
| 2 | **ORCL** | 124.50 | FLOW SURGE | **PUTS** | 63 | none: 24 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$40.8M | - | 135 | 125 | -$3.1M | +$0 bull / -$898k bear | out (clean 32, ADX 39, RVol 5.1) |
| 3 | **DELL** | 411.26 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 60 | none: 32 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$24.3M | - | 440 | 400 | +$457k | +$0 bull / -$688k bear | LONG (clean 35, ADX 44, RVol 1.6) |
| 4 | **AVGO** | 333.00 | FLOW SURGE | **CALLS** | 51 | none: 81 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$61.7M | - | 340 | 340 | +$2.4M | +$538k bull / -$28k bear | out (clean 31, ADX 36, RVol 2.3) |
| 5 | **SMCI** | 31.61 | TREND (flow not with it) | **CALLS** | 50 | none: 13 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$2.2M | - | 34.5 | 30 | -$365k | +$87k bull / -$69k bear | LONG (clean 36, ADX 38, RVol 1.5) |
| 6 | **MSTR** | 134.64 | FLOW SURGE | **PUTS** | 47 | none: 27 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$77.1M | - | 135 | 125 | -$2.1M | +$0 bull / -$793k bear | out (clean 26, ADX 32, RVol 1.2) |
| 7 | **GOOGL** | 278.20 | FLOW SURGE | **CALLS** | 45 | none: 66 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | NEG -$44.4M | 285.06 | 285 | 290 | +$1.9M | +$916k bull / +$0 bear | SHORT (clean 33, ADX 32, RVol 0.8) |
| 8 | **BABA** | 100.81 | TREND (flow not with it) | **PUTS** | 44 | none: 20 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$2.5M | 99.95 | 102 | 100 | +$36k | - | SHORT (clean 34, ADX 58, RVol 1.5) |
| 9 | **META** | 614.65 | FLOW SURGE | **PUTS** | 39 | none: 146 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$72.6M | 626.37 | 650 | 610 | -$3.3M | +$312k bull / -$1.0M bear | out (clean 27, ADX 21, RVol 1.0) |
| 10 | **PLTR** | 169.99 | - | **-** | 32 | - | NEG -$27.8M | - | 165 | 180 | +$3.3M | +$1.0M bull / -$469k bear | out (clean 28, ADX 57, RVol 7.6) |
| 11 | **CRM** | 216.33 | - | **-** | 32 | - | NEG -$15.1M | - | 230 | 220 | +$147k | +$66k bull / +$0 bear | out (clean 28, ADX 52, RVol 3.0) |
| 12 | **COIN** | 144.28 | - | **-** | 30 | - | POS +$19.2M | - | 148 | 140 | -$691k | - | out (clean 26, ADX 41, RVol 1.3) |
| 13 | **AAPL** | 331.34 | - | **-** | 29 | - | NEG -$368.0M | 343.94 | 350 | 330 | -$17.5M | +$200k bull / -$7.2M bear | out (clean 32, ADX 32, RVol 5.5) |
| 14 | **MU** | 861.64 | - | **-** | 27 | - | NEG -$185.4M | - | 900 | 850 | +$11.7M | +$8.2M bull / -$5.9M bear | out (clean 32, ADX 43, RVol 2.0) |
| 15 | **SMH** | 518.89 | - | **-** | 26 | - | NEG -$285.9M | - | 532.5 | 500 | +$414k | +$246k bull / -$752k bear | out (clean 33, ADX 41, RVol 2.6) |
| 16 | **AMZN** | 247.00 | - | **-** | 26 | - | POS +$132.2M | 236 | 250 | 250 | +$1.4M | +$385k bull / +$0 bear | out (clean 34, ADX 33, RVol 1.2) |
| 17 | **MSFT** | 510.95 | - | **-** | 26 | - | POS +$105.7M | 501.14 | 535 | 500 | -$901k | +$755k bull / -$588k bear | out (clean 29, ADX 51, RVol 1.1) |
| 18 | **NVDA** | 207.85 | - | **-** | 25 | - | POS +$104.7M | 203.47 | 210 | 200 | +$5.4M | +$3.7M bull / -$1.4M bear | out (clean 31, ADX 40, RVol 2.0) |
| 19 | **AMD** | 487.82 | - | **-** | 25 | - | NEG -$84.7M | - | 520 | 440 | +$2.3M | +$3.2M bull / -$4.6M bear | out (clean 33, ADX 50, RVol 3.9) |
| 20 | **QQQ** | 684.93 | - | **-** | 24 | - | NEG -$5.0B | - | 700 | 680 | +$24.3M | +$11.5M bull / -$6.0M bear | out (clean 32, ADX 34, RVol 1.6) |
| 21 | **ARM** | 203.88 | - | **-** | 22 | - | NEG -$6.5M | - | 220 | 200 | -$86k | +$30k bull / -$31k bear | out (clean 25, ADX 34, RVol 1.0) |
| 22 | **TSLA** | 402.38 | - | **-** | 21 | - | POS +$237.9M | - | 400 | 400 | +$5.0M | +$3.3M bull / -$3.0M bear | out (clean 31, ADX 28, RVol 1.1) |
| 23 | **SPY** | 753.80 | - | **-** | 20 | - | NEG -$9.4B | 770.94 | 750 | 750 | -$695k | +$3.2M bull / -$4.9M bear | out (clean 31, ADX 33, RVol 2.0) |
| 24 | **HOOD** | 84.79 | - | **-** | 20 | - | NEG -$2.8M | - | 90 | 85 | -$456k | - | out (clean 32, ADX 30, RVol 0.8) |
| 25 | **IWM** | 280.54 | - | **-** | 19 | - | NEG -$1.2B | 287.43 | 285 | 270 | -$518k | +$52k bull / -$291k bear | out (clean 32, ADX 21, RVol 1.6) |
| 26 | **NFLX** | 62.41 | - | **-** | 19 | - | NEG -$13.7M | 64.64 | 63 | 60 | -$60k | +$0 bull / -$32k bear | out (clean 28, ADX 24, RVol 0.8) |
| 27 | **UBER** | 66.53 | - | **-** | 19 | - | NEG -$13.5M | - | 70 | 65 | -$27k | - | out (clean 29, ADX 31, RVol 1.0) |

## Big prints this scan (230)
- **QQQ** PUT 678 2026-11-06 (3DTE): 1,512 @ 6.55 = **+$990k** SELL | vol 4,609 / OI 3,821
- **NVDA** CALL 215 2026-11-06 (3DTE): 3,600 @ 1.97 = **+$709k** BUY | vol 8,309 / OI 33,924
- **QQQ** CALL 690 2026-11-06 (3DTE): 794 @ 8.07 = **+$641k** BUY | vol 1,950 / OI 1,892
- **QQQ** PUT 678 2026-11-06 (3DTE): 958 @ 6.55 = **+$627k** SELL | vol 4,609 / OI 3,821
- **QQQ** PUT 678 2026-11-06 (3DTE): 958 @ 6.55 = **+$627k** SELL | vol 4,609 / OI 3,821
- **QQQ** PUT 668 2026-11-06 (3DTE): 1,512 @ 3.76 = **+$569k** SELL | vol 4,577 / OI 0
- **QQQ** PUT 682 2026-11-04 (1DTE): 1,125 @ 4.85 = **+$546k** SELL | vol 4,471 / OI 161
- **QQQ** PUT 700 2026-11-06 (3DTE): 270 @ 17.86 = **+$482k** SELL | vol 729 / OI 22,016
- **QQQ** PUT 682 2026-11-04 (1DTE): 853 @ 4.85 = **+$414k** SELL | vol 4,471 / OI 161
- **QQQ** PUT 668 2026-11-06 (3DTE): 958 @ 3.76 = **+$360k** SELL | vol 4,577 / OI 0
- **QQQ** PUT 668 2026-11-06 (3DTE): 958 @ 3.76 = **+$360k** SELL | vol 4,577 / OI 0
- **QQQ** PUT 700 2026-11-06 (3DTE): 200 @ 17.87 = **+$357k** SELL | vol 729 / OI 22,016
- **QQQ** CALL 700 2026-11-06 (3DTE): 794 @ 4.28 = **+$340k** BUY | vol 2,600 / OI 13,477
- **MSFT** CALL 515 2026-11-06 (3DTE): 499 @ 6.50 = **+$324k** BUY | vol 1,237 / OI 253
- **QQQ** PUT 675 2026-11-04 (1DTE): 1,125 @ 2.73 = **+$307k** SELL | vol 4,623 / OI 1,253

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 756 2026-11-04 (1DTE): 702 traded vs OI 680
- **SPY** CALL 763 2026-11-04 (1DTE): 809 traded vs OI 615
- **SPY** CALL 767 2026-11-04 (1DTE): 1,443 traded vs OI 1,046
- **SPY** CALL 757 2026-11-04 (1DTE): 793 traded vs OI 613
- **SPY** CALL 764 2026-11-04 (1DTE): 1,054 traded vs OI 840
- **SPY** PUT 757 2026-11-03 (0DTE): 1,206 traded vs OI 971
- **SPY** PUT 737 2026-11-05 (2DTE): 500 traded vs OI 0
- **SPY** PUT 720 2026-11-03 (0DTE): 1,209 traded vs OI 1,142
- **SPY** PUT 758 2026-11-03 (0DTE): 1,076 traded vs OI 952
- **SPY** CALL 758 2026-11-04 (1DTE): 1,649 traded vs OI 1,510
- **SPY** PUT 741 2026-11-05 (2DTE): 524 traded vs OI 0
- **SPY** PUT 750 2026-11-04 (1DTE): 2,297 traded vs OI 1,898
- **SPY** PUT 755 2026-11-03 (0DTE): 5,125 traded vs OI 4,672
- **SPY** CALL 753 2026-11-13 (10DTE): 531 traded vs OI 341
- **QQQ** CALL 717 2026-11-03 (0DTE): 762 traded vs OI 545

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
