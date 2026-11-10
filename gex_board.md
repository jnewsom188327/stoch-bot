# GEX + FLOW SCAN - Tue Nov 10, 10:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 1.98 | +214% (35m) | **+214%** | +22% | 280 hit |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.93 | +21% (60m) | **+21%** | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.95 | +90% (60m) | **+83%** (done) | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:50:08 ET, last candle SPY 10:49, QQQ 10:49 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 10:15 BABA PUTS: price +0.24 over the last 15 min - flow says one way, price says the other
- 10:10 BABA PUTS: price +0.73 over the last 15 min - flow says one way, price says the other
- 10:00 NFLX CALLS: price -0.14 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AAPL CALLS: price -2.97 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 BABA CALLS: price -0.98 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AMZN** | 270.59 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 39 | none: 66 puts 0-7DTE > 6 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +4% at the target (needs +20%) (5 contracts' greeks worked out here) | POS +$471.8M | - | 270 | 265 | +$4.8M | +$107k bull / +$0 bear | out (clean 32, ADX 30, RVol 0.6) |
| 2 | **GOOGL** | 288.90 | FLIP CROSS down into negative gamma | **PUTS** | 31 | none: 69 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$3.3M | 289.01 | 300 | 290 | +$1.3M | +$90k bull / +$0 bear | out (clean 29, ADX 14, RVol 0.7) |
| 3 | **AAPL** | 347.92 | - | **-** | 27 | - | POS +$410.9M | 335.99 | 350 | 340 | +$15.7M | +$0 bull / -$256k bear | out (clean 28, ADX 18, RVol 0.7) |
| 4 | **AMD** | 522.72 | - | **-** | 26 | - | POS +$53.3M | - | 500 | 500 | -$66.5M | +$4.8M bull / +$0 bear | out (clean 31, ADX 31, RVol 1.6) |
| 5 | **COIN** | 130.85 | - | **-** | 24 | - | POS +$1.5M | 129.29 | 137 | 135 | +$312k | +$27k bull / +$0 bear | out (clean 30, ADX 30, RVol 0.6) |
| 6 | **NVDA** | 168.54 | - | **-** | 23 | - | NEG -$173.6M | - | 185 | 170 | +$19.9M | +$1.2M bull / +$0 bear | out (clean 32, ADX 32, RVol 1.9) |
| 7 | **AVGO** | 328.60 | - | **-** | 22 | - | NEG -$14.0M | 342.58 | 340 | 320 | -$8.5M | +$209k bull / +$0 bear | out (clean 31, ADX 31, RVol 0.9) |
| 8 | **ARM** | 179.24 | - | **-** | 21 | - | NEG -$4.9M | - | 185 | 190 | -$77k | +$35k bull / +$0 bear | out (clean 27, ADX 27, RVol 1.1) |
| 9 | **UBER** | 69.89 | PINNED between the walls (positive gamma) - chop | **-** | 20 | - | POS +$8.1M | 68.36 | 70 | 70 | -$9k | - | out (clean 33, ADX 39, RVol 0.4) |
| 10 | **DELL** | 331.14 | - | **-** | 19 | - | NEG -$11.0M | - | 350 | 340 | +$468k | +$142k bull / +$0 bear | out (clean 32, ADX 27, RVol 0.9) |
| 11 | **MSTR** | 120.93 | - | **-** | 19 | - | NEG -$7.9M | 124.13 | 133 | 110 | +$249k | +$215k bull / +$0 bear | out (clean 29, ADX 28, RVol 1.5) |
| 12 | **SPY** | 747.36 | - | **-** | 18 | - | NEG -$7.9B | 760.75 | 750 | 730 | +$22.5M | +$5.9M bull / +$0 bear | out (clean 32, ADX 31, RVol 0.6) |
| 13 | **TSLA** | 375.88 | - | **-** | 18 | - | POS +$190.4M | - | 380 | 380 | -$1.2M | +$891k bull / +$0 bear | out (clean 34, ADX 36, RVol 0.4) |
| 14 | **MU** | 715.84 | - | **-** | 17 | - | NEG -$30.0M | - | 750 | 750 | -$10.1M | +$4.8M bull / +$0 bear | out (clean 29, ADX 21, RVol 0.7) |
| 15 | **HOOD** | 81.01 | - | **-** | 17 | - | POS +$2.5M | 79.11 | 85 | 80 | +$695k | - | out (clean 30, ADX 34, RVol 0.6) |
| 16 | **ORCL** | 118.34 | - | **-** | 16 | - | NEG -$23.3M | - | 130 | 120 | +$58k | +$95k bull / +$0 bear | out (clean 28, ADX 28, RVol 0.3) |
| 17 | **CRM** | 212.73 | - | **-** | 16 | - | NEG -$10.2M | - | 195 | 220 | -$89k | - | out (clean 30, ADX 35, RVol 0.3) |
| 18 | **QQQ** | 673.43 | - | **-** | 15 | - | NEG -$2.0B | 692.2 | 680 | 680 | -$1.1M | +$3.4M bull / +$0 bear | out (clean 31, ADX 23, RVol 0.5) |
| 19 | **IWM** | 278.52 | - | **-** | 15 | - | NEG -$1.4B | 284.04 | 280 | 270 | +$4.6M | - | out (clean 36, ADX 45, RVol 1.0) |
| 20 | **SMH** | 480.98 | - | **-** | 15 | - | NEG -$218.3M | - | 500 | 475 | +$140k | +$74k bull / +$0 bear | out (clean 29, ADX 20, RVol 0.6) |
| 21 | **META** | 641.79 | - | **-** | 15 | - | POS +$253.4M | 604.15 | 650 | 650 | +$74k | +$154k bull / +$0 bear | out (clean 32, ADX 21, RVol 0.6) |
| 22 | **BABA** | 103.84 | - | **-** | 15 | - | NEG -$6.0M | 105.75 | 110 | 100 | -$398k | - | out (clean 29, ADX 32, RVol 0.5) |
| 23 | **PLTR** | 167.21 | - | **-** | 12 | - | POS +$53.1M | - | 165 | 170 | -$361k | - | out (clean 28, ADX 45, RVol 0.8) |
| 24 | **SHOP** | 148.91 | - | **-** | 11 | - | POS +$2.2M | 144.38 | 150 | 140 | +$7k | - | out (clean 31, ADX 37, RVol 0.3) |
| 25 | **MSFT** | 542.41 | - | **-** | 8 | - | POS +$673.5M | - | 550 | 535 | -$94k | - | out (clean 33, ADX 37, RVol 0.7) |
| 26 | **NFLX** | 62.97 | - | **-** | 8 | - | NEG -$22.4M | 65.45 | 65 | 60 | -$155k | - | out (clean 30, ADX 28, RVol 0.7) |
| 27 | **SMCI** | 28.02 | - | **-** | 7 | - | POS +$3.4M | - | 30 | 30 | -$43k | - | out (clean 28, ADX 21, RVol 0.5) |

## Big prints this scan (82)
- **SPY** PUT 760 2026-11-13 (3DTE): 1,740 @ 11.30 = **+$2.0M** SELL | vol 26,916 / OI 5,844
- **SPY** PUT 760 2026-11-13 (3DTE): 260 @ 11.30 = **+$294k** SELL | vol 26,916 / OI 5,844
- **SPY** PUT 750 2026-11-11 (1DTE): 741 @ 3.54 = **+$262k** SELL | vol 15,572 / OI 3,489
- **QQQ** CALL 670 2026-11-10 (0DTE): 268 @ 7.97 = **+$214k** BUY | vol 6,065 / OI 1,753
- **QQQ** CALL 679 2026-11-11 (1DTE): 498 @ 4.20 = **+$209k** BUY | vol 8,609 / OI 135
- **QQQ** CALL 678 2026-11-10 (0DTE): 999 @ 1.95 = **+$195k** BUY | vol 65,535 / OI 3,231
- **QQQ** PUT 660 2026-11-13 (3DTE): 710 @ 2.29 = **+$163k** SELL | vol 9,402 / OI 7,659
- **MU** PUT 725 2026-11-11 (1DTE): 100 @ 15.30 = **+$153k** SELL | vol 2,121 / OI 61
- **QQQ** CALL 679 2026-11-11 (1DTE): 316 @ 4.00 = **+$126k** BUY | vol 8,609 / OI 135
- **QQQ** CALL 672 2026-11-10 (0DTE): 200 @ 6.10 = **+$122k** BUY | vol 16,400 / OI 3,705
- **QQQ** CALL 672 2026-11-10 (0DTE): 200 @ 6.10 = **+$122k** BUY | vol 16,400 / OI 3,705
- **QQQ** CALL 672 2026-11-10 (0DTE): 200 @ 6.01 = **+$120k** BUY | vol 16,400 / OI 3,705
- **QQQ** CALL 672 2026-11-10 (0DTE): 200 @ 6.01 = **+$120k** BUY | vol 16,400 / OI 3,705
- **MU** PUT 700 2026-11-11 (1DTE): 200 @ 5.55 = **+$111k** SELL | vol 7,156 / OI 160
- **QQQ** PUT 675 2026-11-10 (0DTE): 499 @ 2.20 = **+$110k** SELL | vol 78,391 / OI 718

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 748 2026-11-13 (3DTE): 1,197 traded vs OI 1,196
- **SPY** CALL 767 2026-11-13 (3DTE): 1,614 traded vs OI 1,597
- **SPY** PUT 738 2026-11-13 (3DTE): 7,038 traded vs OI 5,354
- **SPY** CALL 819 2026-11-13 (3DTE): 531 traded vs OI 206
- **SPY** PUT 743 2026-11-12 (2DTE): 506 traded vs OI 349
- **SPY** PUT 730 2026-11-12 (2DTE): 1,140 traded vs OI 1,077
- **SPY** PUT 720 2026-11-16 (6DTE): 3,563 traded vs OI 2,768
- **SPY** PUT 730 2026-11-30 (20DTE): 6,385 traded vs OI 5,244
- **QQQ** CALL 680 2026-11-13 (3DTE): 3,284 traded vs OI 3,255
- **QQQ** CALL 677 2026-11-13 (3DTE): 766 traded vs OI 650
- **QQQ** PUT 660 2026-11-13 (3DTE): 9,402 traded vs OI 7,659
- **QQQ** CALL 677 2026-11-12 (2DTE): 518 traded vs OI 158
- **QQQ** CALL 691 2026-11-13 (3DTE): 512 traded vs OI 504
- **QQQ** PUT 662 2026-11-13 (3DTE): 662 traded vs OI 629
- **QQQ** CALL 700 2026-11-18 (8DTE): 1,189 traded vs OI 639

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
