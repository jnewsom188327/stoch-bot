# GEX + FLOW SCAN - Mon Nov 02, 10:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:10:08 ET, last candle SPY 10:09, QQQ 10:09 | no errors

## Flow surges NOT fired - price disagreed (3 today, last 5)
- 10:10 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 10:05 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 09:50 BABA PUTS: price +0.75 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BABA** | 103.49 | FLOW SURGE | **PUTS** | 57 | 11/06 99P @ 0.70 (delta 0.20) = est +31% at 102.35 | POS +$3.2M | 100.81 | 105 | 100 | -$1.2M | +$0 bull / -$148k bear | out (clean 33, ADX 51, RVol 3.8) |
| 2 | **AAPL** | 340.28 | FLOW SURGE | **CALLS** | 49 | none: 81 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$46.5M | 336.88 | 350 | 330 | +$7.6M | +$1.1M bull / -$25k bear | out (clean 32, ADX 31, RVol 2.2) |
| 3 | **MU** | 875.21 | FLOW SURGE | **CALLS** | 48 | none: 149 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (59 contracts' greeks worked out here) | NEG -$216.8M | - | 910 | 900 | +$27.1M | +$5.7M bull / -$218k bear | out (clean 30, ADX 27, RVol 2.0) |
| 4 | **META** | 619.77 | FLOW SURGE | **PUTS** | 45 | none: 196 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (80 contracts' greeks worked out here) | NEG -$76.0M | 627.61 | 650 | 600 | -$10.8M | +$0 bull / -$444k bear | out (clean 29, ADX 33, RVol 0.9) |
| 5 | **GOOGL** | 285.81 | TREND (flow not with it) | **CALLS** | 45 | 11/02 287.5C @ 0.79 (delta 0.32) = est +247% at 290 | NEG -$76.9M | - | 285 | 290 | -$2.1M | +$459k bull / -$82k bear | LONG (clean 33, ADX 49, RVol 1.4) |
| 6 | **SPY** | 760.78 | FLOW SURGE | **PUTS** | 43 | none: 471 puts 0-7DTE > 29 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only -2% at the target (needs +20%) (199 contracts' greeks worked out here) | NEG -$9.4B | 775.43 | 770 | 750 | -$56.1M | +$264k bull / -$3.8M bear | out (clean 29, ADX 41, RVol 1.1) |
| 7 | **ARM** | 202.25 | FLOW SURGE | **CALLS** | 43 | none: 16 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$6.7M | - | 220 | 200 | +$343k | +$170k bull / +$0 bear | out (clean 26, ADX 22, RVol 0.6) |
| 8 | **AVGO** | 329.63 | FLOW SURGE | **PUTS** | 42 | none: 108 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (46 contracts' greeks worked out here) | NEG -$105.8M | - | 340 | 330 | -$4.4M | +$0 bull / -$256k bear | out (clean 31, ADX 43, RVol 0.8) |
| 9 | **AMZN** | 251.42 | FLOW SURGE | **PUTS** | 41 | none: 80 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (34 contracts' greeks worked out here) | POS +$102.3M | 242.27 | 250 | 250 | -$16.7M | +$668k bull / -$859k bear | out (clean 32, ADX 51, RVol 1.3) |
| 10 | **HOOD** | 86.47 | FLOW SURGE | **PUTS** | 41 | none: 18 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$9.0M | - | 93 | 90 | -$1.0M | +$0 bull / -$27k bear | out (clean 32, ADX 57, RVol 0.5) |
| 11 | **SMH** | 525.52 | - | **-** | 30 | - | NEG -$325.6M | - | 532.5 | 500 | +$2.1M | +$49k bull / -$119k bear | out (clean 31, ADX 38, RVol 1.2) |
| 12 | **IWM** | 282.34 | - | **-** | 27 | - | NEG -$817.5M | 286.56 | 285 | 270 | -$2.6M | +$0 bull / -$311k bear | out (clean 31, ADX 42, RVol 2.2) |
| 13 | **MSFT** | 525.42 | - | **-** | 27 | - | POS +$360.8M | 498.98 | 540 | 530 | -$4.4M | +$1.0M bull / -$437k bear | out (clean 27, ADX 23, RVol 1.7) |
| 14 | **AMD** | 503.89 | - | **-** | 25 | - | NEG -$96.9M | - | 550 | 500 | +$6.2M | +$660k bull / -$766k bear | out (clean 30, ADX 34, RVol 1.2) |
| 15 | **MSTR** | 135.98 | - | **-** | 24 | - | POS +$3.9M | - | 135 | 140 | +$943k | +$296k bull / -$29k bear | out (clean 27, ADX 38, RVol 1.0) |
| 16 | **ORCL** | 123.59 | - | **-** | 24 | - | NEG -$39.4M | - | 130 | 120 | +$404k | +$313k bull / -$83k bear | out (clean 32, ADX 40, RVol 2.3) |
| 17 | **CRM** | 231.32 | - | **-** | 24 | - | NEG -$5.8M | 242.64 | 240 | 220 | +$108k | - | out (clean 28, ADX 24, RVol 1.8) |
| 18 | **TSLA** | 404.08 | - | **-** | 23 | - | POS +$234.0M | - | 400 | 400 | +$22.8M | +$3.4M bull / -$2.6M bear | out (clean 30, ADX 28, RVol 1.7) |
| 19 | **PLTR** | 185.46 | - | **-** | 23 | - | NEG -$11.0M | - | 200 | 180 | -$1.1M | +$0 bull / -$103k bear | out (clean 26, ADX 12, RVol 2.7) |
| 20 | **DELL** | 415.08 | - | **-** | 23 | - | NEG -$23.7M | - | 440 | 400 | +$981k | +$80k bull / -$84k bear | out (clean 34, ADX 26, RVol 1.6) |
| 21 | **UBER** | 67.19 | - | **-** | 23 | - | NEG -$7.9M | - | 70 | 65 | -$214k | - | out (clean 27, ADX 41, RVol 1.3) |
| 22 | **NFLX** | 62.20 | - | **-** | 22 | - | NEG -$23.1M | - | 63 | 60 | +$481k | - | out (clean 30, ADX 31, RVol 2.0) |
| 23 | **NVDA** | 208.07 | - | **-** | 21 | - | NEG -$179.3M | 214.55 | 210 | 210 | +$1.4M | +$2.8M bull / -$152k bear | out (clean 30, ADX 36, RVol 1.8) |
| 24 | **QQQ** | 695.35 | - | **-** | 20 | - | NEG -$5.7B | 731.64 | 720 | 680 | -$5.8M | +$2.7M bull / -$268k bear | out (clean 30, ADX 37, RVol 1.4) |
| 25 | **SMCI** | 33.09 | - | **-** | 14 | - | POS +$564k | - | 35 | 33 | +$77k | - | out (clean 32, ADX 46, RVol 1.4) |
| 26 | **SHOP** | 159.46 | - | **-** | 13 | - | NEG -$264k | - | 175 | 175 | +$3k | - | out (clean 28, ADX 40, RVol 3.4) |
| 27 | **COIN** | 142.64 | - | **-** | 10 | - | NEG -$8.7M | - | 150 | 150 | +$23k | - | out (clean 26, ADX 35, RVol 1.5) |

## Big prints this scan (120)
- **SPY** CALL 760 2026-11-02 (0DTE): 1,500 @ 1.79 = **+$268k** SELL | vol 67,551 / OI 467
- **SPY** CALL 760 2026-11-06 (4DTE): 406 @ 6.50 = **+$264k** BUY | vol 4,323 / OI 1,345
- **SPY** CALL 755 2026-11-02 (0DTE): 430 @ 5.80 = **+$249k** SELL | vol 2,656 / OI 59
- **GOOGL** PUT 287.5 2026-11-06 (4DTE): 425 @ 5.29 = **+$225k** SELL | vol 473 / OI 555
- **MSFT** CALL 510 2026-11-02 (0DTE): 120 @ 16.77 = **+$201k** BUY | vol 144 / OI 51
- **SPY** CALL 756 2026-11-02 (0DTE): 419 @ 4.70 = **+$197k** SELL | vol 2,846 / OI 51
- **GOOGL** PUT 290 2026-11-02 (0DTE): 425 @ 4.26 = **+$181k** MID | vol 477 / OI 668
- **MSFT** CALL 512.5 2026-11-02 (0DTE): 120 @ 14.31 = **+$172k** BUY | vol 131 / OI 37
- **MU** CALL 885 2026-11-04 (2DTE): 100 @ 17.08 = **+$171k** BUY | vol 524 / OI 10
- **TSLA** PUT 395 2026-11-02 (0DTE): 928 @ 1.84 = **+$171k** BUY | vol 15,570 / OI 1,254
- **QQQ** PUT 694 2026-11-02 (0DTE): 921 @ 1.80 = **+$166k** BUY | vol 31,031 / OI 0
- **MU** PUT 850 2026-11-06 (4DTE): 100 @ 15.95 = **+$160k** SELL | vol 681 / OI 1,436
- **TSLA** CALL 400 2026-11-02 (0DTE): 454 @ 3.50 = **+$159k** SELL | vol 12,743 / OI 1,359
- **SPY** CALL 756 2026-11-06 (4DTE): 177 @ 8.90 = **+$158k** SELL | vol 307 / OI 188
- **MU** CALL 890 2026-11-04 (2DTE): 100 @ 15.02 = **+$150k** BUY | vol 542 / OI 67

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 761 2026-11-03 (1DTE): 689 traded vs OI 628
- **SPY** CALL 750 2026-11-02 (0DTE): 521 traded vs OI 75
- **SPY** CALL 782 2026-11-04 (2DTE): 535 traded vs OI 212
- **SPY** CALL 775 2026-11-10 (8DTE): 3,841 traded vs OI 714
- **SPY** PUT 715 2026-11-10 (8DTE): 536 traded vs OI 257
- **SPY** PUT 741 2026-11-06 (4DTE): 921 traded vs OI 836
- **SPY** PUT 759 2026-11-03 (1DTE): 2,858 traded vs OI 2,770
- **SPY** CALL 752 2026-11-06 (4DTE): 557 traded vs OI 43
- **QQQ** PUT 691 2026-11-03 (1DTE): 563 traded vs OI 0
- **QQQ** PUT 686 2026-11-03 (1DTE): 523 traded vs OI 0
- **QQQ** CALL 699 2026-11-03 (1DTE): 537 traded vs OI 0
- **QQQ** PUT 690 2026-11-03 (1DTE): 1,898 traded vs OI 1,780
- **QQQ** PUT 654 2026-11-02 (0DTE): 1,998 traded vs OI 0
- **QQQ** PUT 689 2026-11-03 (1DTE): 724 traded vs OI 0
- **QQQ** CALL 710 2026-11-13 (11DTE): 5,145 traded vs OI 688

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
