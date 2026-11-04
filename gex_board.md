# GEX + FLOW SCAN - Wed Nov 04, 09:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:40:08 ET, last candle SPY 09:39, QQQ 09:39 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 285.63 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 56 | none: 314 puts 0-7DTE > 21 priced 0.40-0.80 > 3 delta 0.2+ > 3 spread ok > 3 liquid > best one only +6% at the target (needs +20%) (109 contracts' greeks worked out here) | POS +$126.2M | 285.21 | 285 | 270 | +$0 | - | LONG (clean 34, ADX 33, RVol 4.5) |
| 2 | **AMZN** | 268.64 | TREND (flow not with it) | **CALLS** | 42 | none: 88 calls 0-7DTE > 9 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +13% at the target (needs +20%) (38 contracts' greeks worked out here) | POS +$534.8M | - | 270 | 250 | +$0 | - | LONG (clean 33, ADX 40, RVol 4.8) |
| 3 | **MSFT** | 551.34 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 42 | none: 167 puts 0-7DTE > 13 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (84 contracts' greeks worked out here) | POS +$960.0M | - | 550 | 535 | +$0 | - | out (clean 28, ADX 42, RVol 4.1) |
| 4 | **BABA** | 105.52 | TREND (flow not with it) | **CALLS** | 40 | 11/06 109C @ 0.69 (delta 0.24) = est +32% at 106.68 | POS +$14.1M | 99.37 | 105 | 100 | +$0 | - | LONG (clean 34, ADX 28, RVol 3.8) |
| 5 | **NFLX** | 64.98 | PINNED between the walls (positive gamma) - chop | **-** | 36 | - | POS +$17.8M | 62.67 | 65 | 65 | +$0 | - | out (clean 29, ADX 35, RVol 3.5) |
| 6 | **NVDA** | 204.45 | FLIP CROSS up into positive gamma | **CALLS** | 35 | none: 64 calls 0-7DTE > 5 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -12% at the target (needs +20%) (27 contracts' greeks worked out here) | POS +$40.6M | 203.96 | 210 | 200 | +$0 | - | out (clean 29, ADX 30, RVol 4.2) |
| 7 | **UBER** | 68.91 | FLIP CROSS up into positive gamma | **CALLS** | 35 | 11/06 71C @ 0.48 (delta 0.25) = est +58% at 70 | NEG -$990k | 68.88 | 70 | 65 | +$0 | - | out (clean 30, ADX 26, RVol 4.5) |
| 8 | **GOOGL** | 288.35 | TREND (flow not with it) | **CALLS** | 33 | none: 92 calls 0-7DTE > 9 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +17% at the target (needs +20%) (50 contracts' greeks worked out here) | POS +$71.2M | 282.78 | 285 | 290 | +$0 | - | LONG (clean 33, ADX 33, RVol 2.0) |
| 9 | **SPY** | 765.93 | - | **-** | 19 | - | NEG -$3.9B | 770.2 | 770 | 750 | +$0 | +$176k bull / +$0 bear | out (clean 30, ADX 25, RVol 2.7) |
| 10 | **TSLA** | 380.42 | - | **-** | 19 | - | NEG -$107.3M | 389.8 | 400 | 380 | +$0 | +$0 bull / -$42k bear | out (clean 31, ADX 24, RVol 3.8) |
| 11 | **AMD** | 499.08 | - | **-** | 19 | - | NEG -$49.2M | - | 510 | 500 | +$0 | +$50k bull / +$0 bear | out (clean 32, ADX 25, RVol 4.7) |
| 12 | **PLTR** | 171.87 | - | **-** | 18 | - | NEG -$47.1M | - | 165 | 170 | +$0 | +$0 bull / -$540k bear | out (clean 27, ADX 19, RVol 3.6) |
| 13 | **SHOP** | 146.44 | - | **-** | 12 | - | NEG -$12.1M | - | 160 | 135 | +$0 | - | out (clean 35, ADX 40, RVol 5.1) |
| 14 | **META** | 631.94 | - | **-** | 11 | - | POS +$161.8M | 618.58 | 650 | 625 | +$0 | - | out (clean 30, ADX 34, RVol 2.6) |
| 15 | **ORCL** | 127.62 | - | **-** | 11 | - | NEG -$25.8M | - | 130 | 125 | +$0 | - | out (clean 35, ADX 31, RVol 3.4) |
| 16 | **CRM** | 229.45 | - | **-** | 10 | - | NEG -$8.7M | 239.46 | 240 | 220 | +$0 | - | out (clean 30, ADX 28, RVol 4.1) |
| 17 | **QQQ** | 693.79 | - | **-** | 9 | - | NEG -$4.8B | 720.35 | 700 | 680 | +$0 | - | out (clean 29, ADX 20, RVol 4.4) |
| 18 | **SMH** | 514.06 | - | **-** | 9 | - | NEG -$424.4M | - | 532.5 | 500 | +$0 | - | out (clean 32, ADX 23, RVol 4.0) |
| 19 | **AAPL** | 348.37 | - | **-** | 9 | - | POS +$563.0M | 341.84 | 350 | 340 | +$0 | - | out (clean 31, ADX 24, RVol 3.9) |
| 20 | **AVGO** | 329.90 | - | **-** | 9 | - | NEG -$77.6M | 345.72 | 340 | 330 | +$0 | - | out (clean 30, ADX 20, RVol 3.4) |
| 21 | **DELL** | 384.68 | - | **-** | 9 | - | NEG -$28.6M | - | 400 | 400 | +$0 | - | out (clean 32, ADX 21, RVol 3.0) |
| 22 | **COIN** | 146.01 | - | **-** | 8 | - | POS +$30.7M | - | 148 | 140 | +$0 | - | out (clean 30, ADX 22, RVol 2.2) |
| 23 | **SMCI** | 32.33 | - | **-** | 8 | - | POS +$7.7M | - | 34.5 | 33 | +$0 | - | out (clean 33, ADX 15, RVol 4.9) |
| 24 | **MU** | 831.55 | - | **-** | 8 | - | NEG -$289.8M | - | 850 | 850 | +$0 | - | out (clean 31, ADX 20, RVol 2.3) |
| 25 | **ARM** | 202.71 | - | **-** | 8 | - | NEG -$5.5M | - | 212.5 | 200 | +$0 | - | out (clean 26, ADX 25, RVol 1.8) |
| 26 | **MSTR** | 138.24 | - | **-** | 7 | - | POS +$119.3M | - | 135 | 135 | +$0 | - | out (clean 29, ADX 21, RVol 1.8) |
| 27 | **HOOD** | 84.88 | - | **-** | 7 | - | NEG -$419k | 85.8 | 90 | 85 | +$0 | - | out (clean 29, ADX 19, RVol 1.8) |

## Big prints this scan (4)
- **PLTR** PUT 175 2026-11-06 (2DTE): 249 @ 9.45 = **+$235k** BUY | vol 0 / OI 4,401
- **PLTR** PUT 170 2026-11-06 (2DTE): 248 @ 6.50 = **+$161k** BUY | vol 0 / OI 7,695
- **PLTR** PUT 170 2026-11-06 (2DTE): 249 @ 5.76 = **+$143k** BUY | vol 0 / OI 7,695
- **TSLA** PUT 380 2026-11-04 (0DTE): 100 @ 4.15 = **+$42k** BUY | vol 0 / OI 2,106

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
