# GEX + FLOW SCAN - Thu Oct 29, 10:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:00 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 145C | 0.79 | 0.51 | +9% (2m) | **-35%** | +139% | 143.92 |
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.60 | +17% (2m) | **-22%** | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.48 | +4% (7m) | **-4%** | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:10:08 ET, last candle SPY 10:09, QQQ 10:09 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 524.13 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 67 | none: 126 puts 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$489.6M | 497.87 | 525 | 530 | +$25.5M | +$4.9M bull / +$0 bear | out (clean 29, ADX 37, RVol 4.0) |
| 2 | **ARM** | 227.78 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 64 | none: 19 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | POS +$1.6M | 224.73 | 227.5 | 220 | +$1.9M | +$2.6M bull / -$40k bear | out (clean 27, ADX 27, RVol 2.1) |
| 3 | **GOOGL** | 285.21 | FLOW SURGE | **PUTS** | 58 | none: 51 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$194.7M | - | 300 | 290 | -$12.3M | +$0 bull / -$2.5M bear | out (clean 33, ADX 46, RVol 9.1) |
| 4 | **IWM** | 283.78 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 56 | 10/29 283P @ 0.54 (delta 0.36) = est +142% at 282 | POS +$634.5M | 281.61 | 284 | 270 | -$4.7M | +$1.1M bull / -$296k bear | out (clean 25, ADX 47, RVol 2.4) |
| 5 | **AMZN** | 245.36 | FLOW SURGE | **PUTS** | 52 | none: 57 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | POS +$8.9M | 242.31 | 265 | 250 | -$6.3M | +$0 bull / -$1.9M bear | out (clean 31, ADX 48, RVol 4.3) |
| 6 | **AAPL** | 350.65 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 48 | none: 55 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | POS +$636.5M | 339.55 | 350 | 345 | +$5.8M | +$0 bull / -$970k bear | out (clean 29, ADX 33, RVol 1.7) |
| 7 | **CRM** | 232.99 | FLOW SURGE | **PUTS** | 48 | none: 19 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$19.1M | - | 240 | 230 | -$338k | +$0 bull / -$90k bear | out (clean 27, ADX 28, RVol 1.1) |
| 8 | **META** | 623.56 | FLOW SURGE | **PUTS** | 45 | none: 144 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (12 contracts' greeks worked out here) | NEG -$86.8M | 630.13 | 650 | 625 | -$13.9M | +$65k bull / -$1.9M bear | out (clean 28, ADX 39, RVol 1.3) |
| 9 | **MU** | 949.90 | PINNED between the walls (positive gamma) - chop | **-** | 44 | - | POS +$342.8M | - | 950 | 950 | +$17.0M | +$7.7M bull / -$2.9M bear | out (clean 29, ADX 36, RVol 1.6) |
| 10 | **AVGO** | 341.82 | FLOW SURGE | **CALLS** | 42 | none: 81 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (13 contracts' greeks worked out here) | NEG -$6.1M | 341.84 | 350 | 340 | +$2.5M | +$26k bull / +$0 bear | out (clean 29, ADX 39, RVol 1.0) |
| 11 | **MSTR** | 140.75 | - | **-** | 30 | - | POS +$21.6M | - | 152.5 | 140 | -$1.1M | +$33k bull / -$31k bear | out (clean 26, ADX 22, RVol 1.7) |
| 12 | **AMD** | 567.97 | - | **-** | 27 | - | POS +$141.8M | - | 600 | 550 | +$6.1M | +$1.2M bull / -$350k bear | out (clean 29, ADX 40, RVol 2.1) |
| 13 | **SPY** | 768.72 | - | **-** | 25 | - | NEG -$5.2B | 773 | 770 | 765 | -$61.8M | +$0 bull / -$10.2M bear | out (clean 27, ADX 20, RVol 1.3) |
| 14 | **QQQ** | 715.33 | - | **-** | 24 | - | NEG -$4.8B | 727.26 | 720 | 700 | -$46.1M | +$0 bull / -$3.2M bear | out (clean 28, ADX 29, RVol 1.7) |
| 15 | **SMH** | 560.01 | - | **-** | 24 | - | NEG -$91.8M | 564.03 | 560 | 555 | +$506k | +$61k bull / -$63k bear | out (clean 28, ADX 22, RVol 1.0) |
| 16 | **PLTR** | 194.88 | - | **-** | 24 | - | POS +$29.3M | 190.9 | 200 | 190 | -$1.7M | +$56k bull / -$169k bear | out (clean 26, ADX 18, RVol 2.2) |
| 17 | **SMCI** | 35.49 | - | **-** | 24 | - | POS +$24.7M | - | 35 | 35 | +$99k | +$0 bull / -$27k bear | out (clean 27, ADX 25, RVol 0.8) |
| 18 | **NFLX** | 62.12 | - | **-** | 23 | - | NEG -$46.1M | - | 63 | 60 | -$529k | - | out (clean 31, ADX 36, RVol 1.2) |
| 19 | **COIN** | 161.45 | - | **-** | 23 | - | POS +$6.5M | - | 170 | 155 | -$160k | - | out (clean 27, ADX 19, RVol 1.8) |
| 20 | **UBER** | 64.90 | - | **-** | 23 | - | NEG -$32.1M | 67.79 | 70 | 65 | -$117k | - | out (clean 29, ADX 30, RVol 1.1) |
| 21 | **ORCL** | 138.70 | - | **-** | 22 | - | POS +$117.1M | - | 135 | 140 | +$297k | +$612k bull / +$0 bear | out (clean 31, ADX 39, RVol 1.4) |
| 22 | **SHOP** | 167.20 | - | **-** | 22 | - | NEG -$6.8M | 173.42 | 175 | 165 | -$59k | - | out (clean 27, ADX 18, RVol 1.2) |
| 23 | **BABA** | 99.84 | - | **-** | 22 | - | NEG -$17.5M | 102.95 | 102 | 100 | -$64k | - | out (clean 28, ADX 28, RVol 1.6) |
| 24 | **NVDA** | 213.16 | - | **-** | 21 | - | POS +$142.7M | 210.51 | 215 | 210 | +$1.2M | +$656k bull / -$163k bear | out (clean 26, ADX 33, RVol 1.7) |
| 25 | **TSLA** | 402.73 | - | **-** | 19 | - | POS +$462.6M | - | 400 | 400 | -$5.0M | +$928k bull / -$1.2M bear | out (clean 29, ADX 28, RVol 1.0) |
| 26 | **DELL** | 492.85 | - | **-** | 17 | - | POS +$14.9M | 474.59 | 500 | 500 | +$146k | +$0 bull / -$26k bear | out (clean 31, ADX 28, RVol 0.5) |
| 27 | **HOOD** | 91.00 | - | **-** | 17 | - | NEG -$24.2M | - | 95 | 90 | -$1.2M | - | out (clean 29, ADX 15, RVol 1.6) |

## Big prints this scan (101)
- **IWM** CALL 283 2026-10-30 (1DTE): 2,075 @ 2.02 = **+$419k** BUY | vol 5,659 / OI 5,369
- **SPY** PUT 775 2026-11-02 (4DTE): 500 @ 8.00 = **+$400k** BUY | vol 4,120 / OI 149
- **SPY** PUT 775 2026-11-02 (4DTE): 500 @ 8.00 = **+$400k** BUY | vol 4,120 / OI 149
- **IWM** CALL 284 2026-10-30 (1DTE): 2,625 @ 1.43 = **+$375k** BUY | vol 8,921 / OI 20,104
- **QQQ** CALL 703 2026-10-30 (1DTE): 260 @ 12.00 = **+$312k** SELL | vol 284 / OI 351
- **AMZN** CALL 245 2026-10-30 (1DTE): 200 @ 9.61 = **+$192k** SELL | vol 3,114 / OI 2,504
- **NVDA** CALL 215 2026-11-02 (4DTE): 999 @ 1.91 = **+$191k** BUY | vol 3,225 / OI 849
- **IWM** CALL 283 2026-10-30 (1DTE): 925 @ 2.03 = **+$188k** BUY | vol 5,659 / OI 5,369
- **QQQ** PUT 740 2026-10-30 (1DTE): 70 @ 26.80 = **+$188k** BUY | vol 96 / OI 6,764
- **AMZN** CALL 247.5 2026-10-30 (1DTE): 200 @ 8.61 = **+$172k** SELL | vol 979 / OI 2,330
- **QQQ** CALL 705 2026-10-29 (0DTE): 149 @ 9.55 = **+$142k** SELL | vol 437 / OI 283
- **QQQ** PUT 725 2026-10-30 (1DTE): 100 @ 12.72 = **+$127k** BUY | vol 2,376 / OI 25,057
- **QQQ** PUT 715 2026-11-04 (6DTE): 129 @ 9.05 = **+$117k** BUY | vol 2,976 / OI 3,574
- **NVDA** CALL 215 2026-10-30 (1DTE): 999 @ 1.16 = **+$116k** BUY | vol 21,891 / OI 36,103
- **SPY** CALL 755 2026-10-29 (0DTE): 86 @ 12.68 = **+$109k** SELL | vol 125 / OI 23

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 778 2026-10-30 (1DTE): 5,081 traded vs OI 4,827
- **SPY** CALL 772 2026-10-30 (1DTE): 5,266 traded vs OI 5,250
- **SPY** CALL 775 2026-11-04 (6DTE): 1,374 traded vs OI 498
- **SPY** PUT 767 2026-11-02 (4DTE): 686 traded vs OI 665
- **SPY** CALL 768 2026-11-03 (5DTE): 715 traded vs OI 312
- **SPY** CALL 772 2026-11-02 (4DTE): 537 traded vs OI 446
- **SPY** PUT 762 2026-10-30 (1DTE): 5,880 traded vs OI 5,731
- **SPY** CALL 762 2026-10-29 (0DTE): 678 traded vs OI 329
- **SPY** CALL 767 2026-10-30 (1DTE): 3,177 traded vs OI 3,077
- **SPY** PUT 763 2026-11-02 (4DTE): 1,429 traded vs OI 1,265
- **SPY** CALL 779 2026-10-30 (1DTE): 2,900 traded vs OI 2,420
- **SPY** PUT 739 2026-10-29 (0DTE): 703 traded vs OI 240
- **SPY** CALL 774 2026-10-30 (1DTE): 3,313 traded vs OI 3,234
- **SPY** PUT 750 2026-10-29 (0DTE): 3,074 traded vs OI 2,991
- **SPY** PUT 777 2026-10-29 (0DTE): 564 traded vs OI 80

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
