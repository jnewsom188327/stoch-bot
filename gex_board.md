# GEX + FLOW SCAN - Thu Oct 29, 02:45 PM ET
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
Last 1m check 14:45:08 ET, last candle SPY 14:44, QQQ 14:44 | no errors
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
| 1 | **AAPL** | 350.02 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 32 | none: 55 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$678.4M | 340.62 | 350 | 345 | +$3.3M | +$29k bull / +$0 bear | out (clean 29, ADX 12, RVol 0.5) |
| 2 | **AMZN** | 244.91 | FLIP CROSS up into positive gamma | **CALLS** | 32 | none: 57 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$10.4M | 241.89 | 265 | 250 | -$2.1M | +$2.0M bull / -$229k bear | out (clean 32, ADX 28, RVol 0.9) |
| 3 | **DELL** | 473.02 | - | **-** | 24 | - | NEG -$11.4M | 483.15 | 500 | 460 | +$2.3M | +$70k bull / +$0 bear | out (clean 31, ADX 53, RVol 0.8) |
| 4 | **MSFT** | 526.83 | - | **-** | 23 | - | POS +$589.6M | 502.75 | 525 | 530 | +$25.7M | +$2.1M bull / +$0 bear | out (clean 28, ADX 24, RVol 1.3) |
| 5 | **GOOGL** | 282.36 | - | **-** | 23 | - | NEG -$181.4M | - | 300 | 290 | -$5.4M | +$0 bull / -$85k bear | out (clean 32, ADX 40, RVol 2.0) |
| 6 | **MU** | 930.00 | - | **-** | 22 | - | POS +$195.7M | 899.26 | 950 | 900 | +$46.0M | +$1.8M bull / -$84k bear | out (clean 28, ADX 52, RVol 0.3) |
| 7 | **SPY** | 767.05 | - | **-** | 19 | - | NEG -$6.7B | 772.35 | 770 | 765 | -$82.0M | +$581k bull / +$0 bear | out (clean 25, ADX 29, RVol 0.6) |
| 8 | **QQQ** | 712.44 | - | **-** | 18 | - | NEG -$5.7B | 725.65 | 720 | 700 | -$56.8M | +$1.0M bull / +$0 bear | out (clean 26, ADX 29, RVol 0.6) |
| 9 | **META** | 626.98 | - | **-** | 18 | - | NEG -$43.8M | 630.49 | 650 | 625 | -$9.8M | +$73k bull / -$165k bear | out (clean 28, ADX 29, RVol 0.6) |
| 10 | **NFLX** | 61.77 | - | **-** | 18 | - | NEG -$54.9M | - | 63 | 61 | -$357k | +$40k bull / +$0 bear | out (clean 31, ADX 23, RVol 0.5) |
| 11 | **NVDA** | 212.61 | - | **-** | 17 | - | POS +$128.1M | 211.15 | 215 | 210 | -$608k | +$162k bull / -$29k bear | out (clean 24, ADX 31, RVol 0.5) |
| 12 | **MSTR** | 140.50 | - | **-** | 17 | - | POS +$22.7M | - | 152.5 | 140 | +$254k | +$42k bull / +$0 bear | out (clean 26, ADX 25, RVol 0.9) |
| 13 | **SMH** | 557.45 | - | **-** | 15 | - | NEG -$93.1M | 563.04 | 560 | 555 | +$2.7M | - | out (clean 27, ADX 29, RVol 0.8) |
| 14 | **TSLA** | 404.77 | - | **-** | 15 | - | POS +$505.7M | - | 400 | 400 | -$18.2M | +$2.2M bull / +$0 bear | out (clean 28, ADX 14, RVol 0.3) |
| 15 | **AMD** | 561.62 | - | **-** | 15 | - | POS +$115.6M | - | 550 | 550 | +$986k | +$854k bull / -$79k bear | out (clean 29, ADX 25, RVol 0.4) |
| 16 | **SMCI** | 34.48 | - | **-** | 15 | - | POS +$20.4M | - | 35 | 35 | +$304k | - | out (clean 27, ADX 41, RVol 0.6) |
| 17 | **PLTR** | 193.74 | - | **-** | 14 | - | POS +$20.2M | 192.01 | 200 | 190 | -$170k | +$61k bull / +$0 bear | out (clean 25, ADX 14, RVol 0.5) |
| 18 | **ARM** | 226.92 | - | **-** | 14 | - | POS +$3.2M | 221.33 | 227.5 | 220 | +$1.6M | - | out (clean 24, ADX 17, RVol 0.7) |
| 19 | **UBER** | 65.39 | - | **-** | 14 | - | NEG -$30.9M | 67.56 | 67 | 65 | -$154k | - | out (clean 28, ADX 22, RVol 0.7) |
| 20 | **COIN** | 158.14 | - | **-** | 8 | - | POS +$1.7M | 155.37 | 170 | 155 | -$89k | - | out (clean 25, ADX 23, RVol 1.5) |
| 21 | **ORCL** | 138.36 | - | **-** | 8 | - | POS +$113.6M | - | 135 | 140 | +$586k | - | out (clean 32, ADX 27, RVol 1.1) |
| 22 | **HOOD** | 90.05 | - | **-** | 8 | - | NEG -$27.5M | - | 95 | 90 | -$324k | - | out (clean 29, ADX 35, RVol 0.5) |
| 23 | **CRM** | 230.96 | - | **-** | 8 | - | NEG -$16.7M | 242.73 | 240 | 230 | -$241k | - | out (clean 27, ADX 10, RVol 0.7) |
| 24 | **SHOP** | 166.34 | - | **-** | 8 | - | NEG -$5.4M | 169.76 | 175 | 165 | -$63k | - | out (clean 25, ADX 18, RVol 0.3) |
| 25 | **BABA** | 98.86 | - | **-** | 8 | - | NEG -$20.9M | 101.98 | 100 | 100 | -$15k | - | out (clean 29, ADX 31, RVol 0.8) |
| 26 | **IWM** | 282.98 | - | **-** | 7 | - | POS +$720.4M | 281.02 | 284 | 270 | +$321k | - | out (clean 26, ADX 33, RVol 0.7) |
| 27 | **AVGO** | 344.14 | - | **-** | 5 | - | POS +$13.8M | 342.35 | 350 | 340 | +$1.7M | - | out (clean 28, ADX 14, RVol 0.4) |

## Big prints this scan (43)
- **AMD** CALL 550 2026-10-30 (1DTE): 200 @ 18.30 = **+$366k** BUY | vol 1,540 / OI 3,519
- **QQQ** PUT 717 2026-10-30 (1DTE): 353 @ 6.16 = **+$217k** SELL | vol 9,460 / OI 3,101
- **QQQ** PUT 717 2026-10-30 (1DTE): 263 @ 6.16 = **+$162k** SELL | vol 9,460 / OI 3,101
- **QQQ** PUT 717 2026-10-30 (1DTE): 254 @ 6.16 = **+$156k** SELL | vol 9,460 / OI 3,101
- **MU** CALL 932.5 2026-10-30 (1DTE): 100 @ 13.70 = **+$137k** BUY | vol 911 / OI 285
- **QQQ** PUT 716 2026-10-30 (1DTE): 206 @ 5.52 = **+$114k** SELL | vol 21,561 / OI 4,780
- **SPY** CALL 766 2026-10-29 (0DTE): 510 @ 2.04 = **+$104k** BUY | vol 31,906 / OI 865
- **MSFT** CALL 530 2026-10-30 (1DTE): 195 @ 4.19 = **+$82k** BUY | vol 25,247 / OI 7,797
- **MU** PUT 935 2026-10-30 (1DTE): 53 @ 15.10 = **+$80k** SELL | vol 7,522 / OI 1,035
- **AMZN** CALL 245 2026-10-30 (1DTE): 79 @ 9.60 = **+$76k** SELL | vol 7,815 / OI 2,504
- **MSFT** CALL 530 2026-10-30 (1DTE): 172 @ 4.06 = **+$70k** BUY | vol 25,247 / OI 7,797
- **MSFT** CALL 535 2026-10-30 (1DTE): 400 @ 1.74 = **+$70k** BUY | vol 22,839 / OI 2,646
- **AMZN** CALL 245 2026-10-30 (1DTE): 71 @ 9.45 = **+$67k** SELL | vol 7,815 / OI 2,504
- **AMD** CALL 570 2026-10-30 (1DTE): 83 @ 7.40 = **+$61k** BUY | vol 9,653 / OI 1,616
- **AMZN** PUT 245 2026-10-30 (1DTE): 59 @ 9.75 = **+$58k** SELL | vol 8,839 / OI 3,801

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 800 2026-11-03 (5DTE): 601 traded vs OI 472
- **QQQ** CALL 720 2026-11-03 (5DTE): 671 traded vs OI 670
- **QQQ** CALL 712 2026-11-02 (4DTE): 510 traded vs OI 113
- **IWM** PUT 277 2026-11-20 (22DTE): 32,245 traded vs OI 8,480
- **SMH** PUT 542.5 2026-10-30 (1DTE): 501 traded vs OI 275
- **NVDA** PUT 207.5 2026-11-06 (8DTE): 2,078 traded vs OI 2,075
- **TSLA** PUT 377.5 2026-10-30 (1DTE): 2,277 traded vs OI 2,225
- **TSLA** PUT 390 2026-11-06 (8DTE): 1,748 traded vs OI 1,737
- **AMD** CALL 575 2026-11-02 (4DTE): 500 traded vs OI 123
- **AMZN** CALL 235 2026-10-30 (1DTE): 598 traded vs OI 538
- **AMZN** CALL 255 2026-11-06 (8DTE): 2,534 traded vs OI 1,615
- **MSFT** PUT 475 2026-11-20 (22DTE): 586 traded vs OI 0
- **MSFT** CALL 562.5 2026-11-02 (4DTE): 851 traded vs OI 103
- **GOOGL** CALL 310 2026-11-04 (6DTE): 502 traded vs OI 24
- **HOOD** CALL 95 2026-11-13 (15DTE): 922 traded vs OI 843

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
