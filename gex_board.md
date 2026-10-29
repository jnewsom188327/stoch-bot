# GEX + FLOW SCAN - Thu Oct 29, 02:55 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 284P | 0.65 | 0.22 | +3% (25m) | **-66%** (done) | +232% | 281.86 |
| 10:00 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 145C | 0.79 | 0.84 | +18% (37m) | **+6%** (done) | +139% | 143.92 |
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.68 | +17% (2m) | **-12%** (done) | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.18 | +20% (21m) | **-64%** (done) | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:55:08 ET, last candle SPY 14:54, QQQ 14:54 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 14:31 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 14:23 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 86 puts 0-1DTE > 5 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |
| 14:17 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 86 puts 0-1DTE > 6 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 14:12 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 86 puts 0-1DTE > 8 priced 0.40-0.80 > 3 delta 0.15+ > 3 spread ok > 3 liquid  |

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 528.72 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 43 | none: 126 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$627.8M | 501.86 | 525 | 530 | +$25.7M | +$1.4M bull / -$64k bear | out (clean 28, ADX 23, RVol 1.1) |
| 2 | **ARM** | 227.21 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 33 | none: 18 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$3.0M | 222.03 | 227.5 | 220 | +$1.5M | - | out (clean 24, ADX 18, RVol 0.7) |
| 3 | **AAPL** | 350.38 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 31 | none: 55 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | POS +$693.9M | 340.85 | 350 | 345 | +$3.0M | +$0 bull / -$244k bear | out (clean 29, ADX 12, RVol 0.5) |
| 4 | **DELL** | 473.52 | - | **-** | 25 | - | NEG -$10.7M | 482.81 | 500 | 460 | +$2.5M | +$70k bull / +$0 bear | out (clean 31, ADX 54, RVol 1.2) |
| 5 | **GOOGL** | 283.43 | - | **-** | 22 | - | NEG -$198.1M | - | 300 | 290 | -$7.1M | +$0 bull / -$1.5M bear | out (clean 32, ADX 36, RVol 1.9) |
| 6 | **MU** | 930.33 | - | **-** | 22 | - | POS +$187.7M | 899.15 | 950 | 900 | +$41.9M | +$2.9M bull / -$390k bear | out (clean 29, ADX 53, RVol 0.3) |
| 7 | **SPY** | 767.55 | - | **-** | 19 | - | NEG -$6.3B | 772.46 | 770 | 765 | -$93.9M | +$104k bull / +$0 bear | out (clean 25, ADX 28, RVol 0.6) |
| 8 | **QQQ** | 713.12 | - | **-** | 18 | - | NEG -$5.6B | 725.65 | 720 | 700 | -$75.4M | +$753k bull / -$796k bear | out (clean 26, ADX 28, RVol 0.6) |
| 9 | **META** | 627.43 | - | **-** | 18 | - | NEG -$41.2M | 630.61 | 650 | 625 | -$11.4M | +$0 bull / -$729k bear | out (clean 27, ADX 28, RVol 0.5) |
| 10 | **AMZN** | 245.25 | - | **-** | 18 | - | POS +$10.3M | 242.07 | 265 | 250 | -$4.4M | +$492k bull / -$2.2M bear | out (clean 31, ADX 25, RVol 1.0) |
| 11 | **ORCL** | 138.19 | - | **-** | 18 | - | POS +$117.9M | - | 135 | 140 | +$508k | +$43k bull / +$0 bear | out (clean 33, ADX 24, RVol 1.3) |
| 12 | **IWM** | 283.21 | - | **-** | 17 | - | POS +$725.5M | 280.89 | 284 | 270 | -$854k | +$0 bull / -$69k bear | out (clean 26, ADX 33, RVol 0.7) |
| 13 | **NVDA** | 212.91 | - | **-** | 17 | - | POS +$142.8M | 211.27 | 215 | 210 | -$1.8M | +$39k bull / -$39k bear | out (clean 24, ADX 30, RVol 0.5) |
| 14 | **MSTR** | 141.52 | - | **-** | 16 | - | POS +$26.7M | - | 152.5 | 140 | -$16k | +$42k bull / +$0 bear | out (clean 26, ADX 24, RVol 1.0) |
| 15 | **TSLA** | 405.64 | - | **-** | 15 | - | POS +$506.0M | - | 400 | 400 | -$20.1M | +$1.9M bull / -$135k bear | out (clean 28, ADX 13, RVol 0.3) |
| 16 | **AMD** | 563.20 | - | **-** | 15 | - | POS +$112.0M | - | 550 | 550 | +$255k | +$658k bull / -$84k bear | out (clean 29, ADX 24, RVol 0.3) |
| 17 | **SMCI** | 34.52 | - | **-** | 15 | - | POS +$19.5M | - | 35 | 35 | +$311k | - | out (clean 27, ADX 43, RVol 0.6) |
| 18 | **SMH** | 558.03 | - | **-** | 14 | - | NEG -$86.5M | 562.48 | 560 | 555 | +$2.6M | - | out (clean 27, ADX 31, RVol 0.5) |
| 19 | **UBER** | 65.43 | - | **-** | 14 | - | NEG -$29.3M | 67.75 | 67 | 65 | -$159k | - | out (clean 28, ADX 21, RVol 0.7) |
| 20 | **BABA** | 98.84 | - | **-** | 10 | - | NEG -$21.6M | 101.56 | 100 | 100 | -$11k | - | out (clean 29, ADX 34, RVol 1.6) |
| 21 | **HOOD** | 90.30 | - | **-** | 9 | - | NEG -$27.4M | - | 95 | 90 | -$540k | - | out (clean 29, ADX 36, RVol 0.5) |
| 22 | **NFLX** | 61.93 | - | **-** | 8 | - | NEG -$52.5M | - | 63 | 60 | -$425k | - | out (clean 31, ADX 20, RVol 0.4) |
| 23 | **COIN** | 158.73 | - | **-** | 8 | - | POS +$2.1M | 155.42 | 170 | 155 | -$47k | - | out (clean 25, ADX 26, RVol 1.7) |
| 24 | **CRM** | 230.56 | - | **-** | 8 | - | NEG -$16.1M | 239.77 | 240 | 230 | -$225k | - | out (clean 27, ADX 12, RVol 0.8) |
| 25 | **SHOP** | 166.70 | - | **-** | 8 | - | NEG -$5.0M | 170.42 | 175 | 165 | -$61k | - | out (clean 25, ADX 19, RVol 0.3) |
| 26 | **AVGO** | 344.40 | - | **-** | 4 | - | POS +$15.7M | 342.39 | 350 | 340 | +$1.3M | - | out (clean 28, ADX 12, RVol 0.3) |
| 27 | **PLTR** | 193.93 | - | **-** | 4 | - | POS +$21.4M | 191.96 | 200 | 190 | -$188k | - | out (clean 25, ADX 14, RVol 0.4) |

## Big prints this scan (46)
- **AMZN** CALL 255 2026-10-30 (1DTE): 600 @ 5.22 = **+$313k** SELL | vol 9,750 / OI 12,075
- **AMZN** CALL 255 2026-10-30 (1DTE): 600 @ 5.21 = **+$313k** SELL | vol 9,750 / OI 12,075
- **QQQ** PUT 712 2026-10-29 (0DTE): 981 @ 1.75 = **+$172k** BUY | vol 204,935 / OI 1,739
- **AMZN** CALL 255 2026-10-30 (1DTE): 270 @ 5.19 = **+$140k** SELL | vol 9,750 / OI 12,075
- **AMZN** CALL 255 2026-10-30 (1DTE): 245 @ 5.19 = **+$127k** SELL | vol 9,750 / OI 12,075
- **QQQ** PUT 717 2026-10-30 (1DTE): 171 @ 6.54 = **+$112k** BUY | vol 11,901 / OI 3,101
- **AMZN** CALL 255 2026-10-30 (1DTE): 196 @ 5.19 = **+$102k** SELL | vol 9,750 / OI 12,075
- **AMZN** CALL 235 2026-10-30 (1DTE): 60 @ 14.77 = **+$89k** SELL | vol 662 / OI 538
- **AMZN** CALL 255 2026-10-30 (1DTE): 154 @ 5.24 = **+$81k** SELL | vol 9,750 / OI 12,075
- **AMZN** CALL 255 2026-10-30 (1DTE): 154 @ 5.22 = **+$80k** SELL | vol 9,750 / OI 12,075
- **AAPL** CALL 347.5 2026-10-30 (1DTE): 200 @ 3.50 = **+$70k** SELL | vol 11,425 / OI 7,887
- **MU** CALL 945 2026-11-02 (4DTE): 50 @ 13.10 = **+$66k** SELL | vol 625 / OI 220
- **AAPL** PUT 352.5 2026-10-30 (1DTE): 200 @ 3.25 = **+$65k** BUY | vol 3,276 / OI 1,564
- **AAPL** CALL 342.5 2026-10-30 (1DTE): 82 @ 7.85 = **+$64k** SELL | vol 2,238 / OI 2,614
- **MSFT** CALL 525 2026-10-30 (1DTE): 100 @ 6.40 = **+$64k** SELL | vol 19,455 / OI 17,429

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 804 2026-11-04 (6DTE): 2,219 traded vs OI 6
- **SPY** PUT 712 2026-10-30 (1DTE): 1,541 traded vs OI 1,510
- **SPY** CALL 803 2026-11-04 (6DTE): 2,248 traded vs OI 1
- **SPY** PUT 762 2026-11-03 (5DTE): 511 traded vs OI 281
- **SPY** CALL 802 2026-11-06 (8DTE): 1,282 traded vs OI 1,217
- **SPY** CALL 809 2026-11-06 (8DTE): 1,203 traded vs OI 999
- **QQQ** CALL 732 2026-10-30 (1DTE): 3,191 traded vs OI 3,182
- **IWM** CALL 284 2026-11-03 (5DTE): 500 traded vs OI 270
- **META** CALL 620 2026-11-04 (6DTE): 513 traded vs OI 106
- **AVGO** PUT 340 2026-10-30 (1DTE): 3,104 traded vs OI 3,080
- **MU** CALL 995 2026-11-02 (4DTE): 505 traded vs OI 55
- **HOOD** PUT 84 2026-11-06 (8DTE): 500 traded vs OI 431

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
