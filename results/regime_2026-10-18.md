# Trend Flip market-conditions study - 2026-10-18 15:18 ET
v3.0 rules. TRAIN = 2020 to 2023 (rules are picked here). TEST = 2024 to now (never used to pick anything). ATR / trade like the TradingView box.

## SPY 2-minute
TRAIN 2020-2023: 2889 trades, **-0.006** ATR/trade | TEST 2024-now: 1918 trades, **+0.009** ATR/trade (thirds hold ~963 trades each: differences under about 0.10 are noise)

### Each condition split into thirds (cut points from TRAIN only)
| Condition | Third | TRAIN n | TRAIN ATR | TEST n | TEST ATR |
|---|---|---|---|---|---|
| Daily trend: yesterday's close vs its 20-day average (ATR, + = with my trade) | low (< -0.90) | 944 | -0.02 | 651 | +0.01 |
|  | mid | 944 | -0.00 | 684 | +0.12 |
|  | high (> 1.07) | 944 | -0.01 | 583 | -0.12 |
| Today's opening gap (daily ATR, + = gap in my trade's direction) | low (< -0.12) | 962 | +0.08 | 687 | +0.06 |
|  | mid | 960 | -0.17 | 669 | -0.09 |
|  | high (> 0.19) | 965 | +0.06 | 562 | +0.06 |
| Move since today's 9:30 open (daily ATR, + = day already moving my way) | low (< 0.03) | 962 | +0.16 | 654 | +0.06 |
|  | mid | 962 | -0.18 | 632 | -0.13 |
|  | high (> 0.14) | 963 | -0.00 | 632 | +0.09 |
| Distance from VWAP at the signal (3m ATR, + = stretched my way) | low (< 0.49) | 963 | +0.10 | 589 | -0.01 |
|  | mid | 963 | -0.05 | 658 | -0.01 |
|  | high (> 1.45) | 963 | -0.07 | 671 | +0.05 |
| Volatility level: daily ATR as % of price | low (< 1.14) | 962 | +0.06 | 1187 | +0.01 |
|  | mid | 959 | -0.07 | 589 | -0.01 |
|  | high (> 1.69) | 966 | -0.01 | 142 | +0.09 |
| Yesterday's range vs normal (1 = normal day) | low (< 0.66) | 959 | +0.05 | 655 | +0.11 |
|  | mid | 965 | -0.01 | 652 | +0.02 |
|  | high (> 0.97) | 963 | -0.06 | 611 | -0.12 |
| Today's range so far vs normal | low (< 0.31) | 962 | -0.07 | 734 | -0.07 |
|  | mid | 962 | +0.06 | 599 | +0.01 |
|  | high (> 0.51) | 963 | -0.01 | 585 | +0.11 |
| 3-minute ATR now vs its 20-day normal | low (< 1.24) | 963 | +0.10 | 560 | -0.02 |
|  | mid | 963 | -0.04 | 608 | +0.12 |
|  | high (> 1.65) | 963 | -0.08 | 750 | -0.06 |
| Time of day | 9:35-10:30 | 1174 | -0.03 | 812 | -0.08 |
|  | 10:30-12:00 | 550 | +0.03 | 412 | +0.01 |
|  | 12:00-14:00 | 567 | +0.01 | 393 | +0.11 |
|  | 14:00-15:30 | 598 | -0.01 | 301 | +0.11 |

### Rules picked on TRAIN, checked on TEST
Baseline v3.0: TRAIN -0.006 | TEST +0.009. ✅ = helps on BOTH TRAIN and TEST.
| Rule | TRAIN ATR | TEST ATR | TEST trades | |
|---|---|---|---|---|
| skip mid - daymove | +0.080 | +0.078 | 1286 | ✅ |
| skip mid - gap | +0.071 | +0.064 | 1249 | ✅ |
| skip high (> 1.65) - ivol | +0.032 | +0.052 | 1168 | ✅ |
| skip high (> 1.45) - vwap | +0.025 | -0.013 | 1247 |  |
| skip low (< 0.31) - dayrange | +0.025 | +0.061 | 1184 | ✅ |
| skip mid - vol | +0.021 | +0.018 | 1329 | ✅ |
| skip high (> 0.97) - yrange | +0.017 | +0.068 | 1307 | ✅ |
| skip 9:35-10:30 - tod | +0.008 | +0.074 | 1106 | ✅ |
| skip low (< -0.90) - trend | -0.007 | +0.011 | 1267 |  |
| ONLY low (< 0.03) - daymove | +0.162 | +0.063 | 654 | ✅ |
| ONLY low (< 1.24) - ivol | +0.103 | -0.020 | 560 |  |
| ONLY low (< 0.49) - vwap | +0.101 | -0.011 | 589 |  |
| ONLY low (< -0.12) - gap | +0.085 | +0.064 | 687 | ✅ |
| ONLY mid - dayrange | +0.060 | +0.013 | 599 | ✅ |
| ONLY low (< 1.14) - vol | +0.058 | +0.010 | 1187 | ✅ |
| ONLY low (< 0.66) - yrange | +0.046 | +0.112 | 655 | ✅ |
| ONLY 10:30-12:00 - tod | +0.025 | +0.011 | 412 | ✅ |
| ONLY mid - trend | -0.001 | +0.121 | 684 | ✅ |

### Best 2 rules combined (picked on TRAIN, full candle-by-candle re-run): skip mid daymove AND skip mid gap
| Test | Trades | Win | ATR / trade | PF | Total ATR | Worst drawdown (ATR) | Longest losing run |
|---|---|---|---|---|---|---|---|
| v3.0 TRAIN | 2889 | 40% | **-0.01** | 0.99 | -18 | 169.9 | 15 |
| **combined TRAIN** | 1590 | 42% | **+0.10** | 1.11 | +152 | 48.5 | 13 |
| v3.0 TEST (never seen) | 1918 | 40% | **+0.01** | 1.01 | +18 | 91.3 | 13 |
| **combined TEST (never seen)** | 1035 | 42% | **+0.07** | 1.08 | +75 | 54.7 | 8 |

| Year | Trades | ATR / trade (combined) | ATR / trade (v3.0) |
|---|---|---|---|
| 2020 | 405 | **+0.07** | +0.09 |
| 2021 | 398 | **+0.08** | +0.01 |
| 2022 | 368 | **+0.17** | -0.03 |
| 2023 | 419 | **+0.07** | -0.09 |
| 2024 | 348 | **+0.02** | -0.04 |
| 2025 | 383 | **+0.12** | +0.04 |
| 2026 | 304 | **+0.08** | +0.03 |

## SPY 3-minute
TRAIN 2020-2023: 2262 trades, **-0.038** ATR/trade | TEST 2024-now: 1534 trades, **+0.078** ATR/trade (thirds hold ~754 trades each: differences under about 0.10 are noise)

### Each condition split into thirds (cut points from TRAIN only)
| Condition | Third | TRAIN n | TRAIN ATR | TEST n | TEST ATR |
|---|---|---|---|---|---|
| Daily trend: yesterday's close vs its 20-day average (ATR, + = with my trade) | low (< -0.98) | 740 | -0.08 | 489 | +0.10 |
|  | mid | 740 | -0.05 | 545 | +0.18 |
|  | high (> 0.99) | 740 | +0.02 | 500 | -0.05 |
| Today's opening gap (daily ATR, + = gap in my trade's direction) | low (< -0.12) | 754 | -0.06 | 538 | +0.09 |
|  | mid | 751 | -0.12 | 526 | +0.03 |
|  | high (> 0.20) | 756 | +0.06 | 470 | +0.11 |
| Move since today's 9:30 open (daily ATR, + = day already moving my way) | low (< 0.03) | 754 | +0.03 | 501 | +0.13 |
|  | mid | 753 | -0.16 | 532 | -0.02 |
|  | high (> 0.15) | 754 | +0.01 | 501 | +0.13 |
| Distance from VWAP at the signal (3m ATR, + = stretched my way) | low (< 0.44) | 754 | -0.11 | 472 | -0.02 |
|  | mid | 754 | -0.03 | 495 | +0.06 |
|  | high (> 1.25) | 754 | +0.03 | 567 | +0.17 |
| Volatility level: daily ATR as % of price | low (< 1.16) | 753 | +0.02 | 963 | +0.11 |
|  | mid | 754 | -0.04 | 464 | +0.06 |
|  | high (> 1.70) | 754 | -0.11 | 107 | -0.14 |
| Yesterday's range vs normal (1 = normal day) | low (< 0.66) | 754 | +0.08 | 505 | +0.22 |
|  | mid | 753 | -0.10 | 520 | +0.07 |
|  | high (> 0.97) | 754 | -0.11 | 509 | -0.05 |
| Today's range so far vs normal | low (< 0.30) | 754 | -0.02 | 552 | -0.00 |
|  | mid | 753 | -0.10 | 483 | +0.17 |
|  | high (> 0.50) | 754 | +0.00 | 499 | +0.08 |
| 3-minute ATR now vs its 20-day normal | low (< 1.22) | 754 | +0.17 | 457 | -0.04 |
|  | mid | 754 | -0.10 | 521 | +0.09 |
|  | high (> 1.62) | 754 | -0.18 | 556 | +0.17 |
| Time of day | 9:35-10:30 | 956 | -0.11 | 654 | +0.10 |
|  | 10:30-12:00 | 542 | -0.11 | 375 | +0.05 |
|  | 12:00-14:00 | 347 | +0.11 | 251 | +0.06 |
|  | 14:00-15:30 | 417 | +0.09 | 254 | +0.07 |

### Rules picked on TRAIN, checked on TEST
Baseline v3.0: TRAIN -0.038 | TEST +0.078. ✅ = helps on BOTH TRAIN and TEST.
| Rule | TRAIN ATR | TEST ATR | TEST trades | |
|---|---|---|---|---|
| skip high (> 1.62) - ivol | +0.035 | +0.028 | 978 |  |
| skip mid - daymove | +0.019 | +0.130 | 1002 | ✅ |
| skip mid - gap | -0.000 | +0.101 | 1008 | ✅ |
| skip low (< 0.44) - vwap | -0.002 | +0.122 | 1062 | ✅ |
| skip high (> 0.97) - yrange | -0.007 | +0.143 | 1025 | ✅ |
| skip high (> 1.70) - vol | -0.007 | +0.093 | 1427 | ✅ |
| skip mid - dayrange | -0.009 | +0.034 | 1051 |  |
| skip low (< -0.98) - trend | -0.015 | +0.069 | 1045 |  |
| skip 10:30-12:00 - tod | -0.016 | +0.086 | 1159 | ✅ |
| ONLY low (< 1.22) - ivol | +0.166 | -0.044 | 457 |  |
| ONLY 12:00-14:00 - tod | +0.113 | +0.061 | 251 |  |
| ONLY low (< 0.66) - yrange | +0.084 | +0.218 | 505 | ✅ |
| ONLY high (> 0.20) - gap | +0.062 | +0.108 | 470 | ✅ |
| ONLY low (< 0.03) - daymove | +0.029 | +0.128 | 501 | ✅ |
| ONLY high (> 1.25) - vwap | +0.025 | +0.173 | 567 | ✅ |
| ONLY low (< 1.16) - vol | +0.024 | +0.112 | 963 | ✅ |
| ONLY high (> 0.99) - trend | +0.018 | -0.050 | 500 |  |
| ONLY high (> 0.50) - dayrange | +0.001 | +0.077 | 499 |  |

### Best 2 rules combined (picked on TRAIN, full candle-by-candle re-run): skip high (> 1.62) ivol AND skip mid daymove
| Test | Trades | Win | ATR / trade | PF | Total ATR | Worst drawdown (ATR) | Longest losing run |
|---|---|---|---|---|---|---|---|
| v3.0 TRAIN | 2262 | 39% | **-0.04** | 0.96 | -86 | 181.0 | 13 |
| **combined TRAIN** | 1212 | 41% | **+0.07** | 1.08 | +89 | 47.3 | 10 |
| v3.0 TEST (never seen) | 1534 | 41% | **+0.08** | 1.09 | +119 | 77.0 | 10 |
| **combined TEST (never seen)** | 788 | 40% | **+0.07** | 1.07 | +53 | 70.1 | 13 |

| Year | Trades | ATR / trade (combined) | ATR / trade (v3.0) |
|---|---|---|---|
| 2020 | 353 | **+0.06** | +0.05 |
| 2021 | 309 | **+0.12** | -0.06 |
| 2022 | 259 | **-0.06** | -0.15 |
| 2023 | 291 | **+0.16** | +0.01 |
| 2024 | 296 | **-0.12** | -0.02 |
| 2025 | 282 | **+0.22** | +0.17 |
| 2026 | 210 | **+0.13** | +0.08 |

## QQQ 2-minute
TRAIN 2020-2023: 2823 trades, **-0.005** ATR/trade | TEST 2024-now: 1860 trades, **+0.033** ATR/trade (thirds hold ~941 trades each: differences under about 0.10 are noise)

### Each condition split into thirds (cut points from TRAIN only)
| Condition | Third | TRAIN n | TRAIN ATR | TEST n | TEST ATR |
|---|---|---|---|---|---|
| Daily trend: yesterday's close vs its 20-day average (ATR, + = with my trade) | low (< -1.04) | 923 | -0.00 | 524 | +0.06 |
|  | mid | 923 | +0.01 | 789 | -0.02 |
|  | high (> 1.08) | 924 | -0.03 | 547 | +0.09 |
| Today's opening gap (daily ATR, + = gap in my trade's direction) | low (< -0.13) | 940 | +0.08 | 680 | +0.02 |
|  | mid | 940 | -0.09 | 531 | +0.02 |
|  | high (> 0.15) | 940 | -0.01 | 649 | +0.05 |
| Move since today's 9:30 open (daily ATR, + = day already moving my way) | low (< 0.04) | 940 | -0.02 | 665 | -0.11 |
|  | mid | 940 | -0.00 | 561 | +0.17 |
|  | high (> 0.16) | 940 | -0.00 | 634 | +0.05 |
| Distance from VWAP at the signal (3m ATR, + = stretched my way) | low (< 0.52) | 941 | +0.07 | 624 | -0.01 |
|  | mid | 941 | -0.00 | 642 | +0.04 |
|  | high (> 1.56) | 941 | -0.09 | 594 | +0.07 |
| Volatility level: daily ATR as % of price | low (< 1.54) | 939 | -0.06 | 1030 | +0.05 |
|  | mid | 940 | -0.00 | 694 | -0.00 |
|  | high (> 2.27) | 941 | +0.04 | 136 | +0.06 |
| Yesterday's range vs normal (1 = normal day) | low (< 0.73) | 940 | +0.08 | 771 | +0.11 |
|  | mid | 940 | +0.01 | 526 | +0.11 |
|  | high (> 1.00) | 940 | -0.11 | 563 | -0.14 |
| Today's range so far vs normal | low (< 0.35) | 939 | -0.02 | 674 | +0.13 |
|  | mid | 941 | -0.02 | 596 | -0.03 |
|  | high (> 0.56) | 940 | +0.02 | 590 | -0.01 |
| 3-minute ATR now vs its 20-day normal | low (< 1.34) | 941 | +0.04 | 606 | +0.06 |
|  | mid | 941 | +0.02 | 608 | -0.01 |
|  | high (> 1.83) | 941 | -0.07 | 646 | +0.05 |
| Time of day | 9:35-10:30 | 1189 | -0.01 | 822 | +0.05 |
|  | 10:30-12:00 | 499 | +0.07 | 343 | +0.14 |
|  | 12:00-14:00 | 554 | +0.06 | 375 | -0.04 |
|  | 14:00-15:30 | 581 | -0.13 | 320 | -0.05 |

### Rules picked on TRAIN, checked on TEST
Baseline v3.0: TRAIN -0.005 | TEST +0.033. ✅ = helps on BOTH TRAIN and TEST.
| Rule | TRAIN ATR | TEST ATR | TEST trades | |
|---|---|---|---|---|
| skip high (> 1.00) - yrange | +0.042 | +0.107 | 1297 | ✅ |
| skip mid - gap | +0.037 | +0.036 | 1329 | ✅ |
| skip high (> 1.56) - vwap | +0.035 | +0.016 | 1266 |  |
| skip high (> 1.83) - ivol | +0.029 | +0.024 | 1214 |  |
| skip 14:00-15:30 - tod | +0.029 | +0.050 | 1540 | ✅ |
| skip low (< 1.54) - vol | +0.019 | +0.006 | 830 |  |
| skip high (> 1.08) - trend | +0.006 | +0.008 | 1313 |  |
| skip mid - dayrange | +0.001 | +0.064 | 1264 | ✅ |
| skip low (< 0.04) - daymove | -0.001 | +0.110 | 1195 | ✅ |
| ONLY low (< -0.13) - gap | +0.078 | +0.023 | 680 |  |
| ONLY low (< 0.73) - yrange | +0.075 | +0.105 | 771 | ✅ |
| ONLY 10:30-12:00 - tod | +0.073 | +0.140 | 343 | ✅ |
| ONLY low (< 0.52) - vwap | +0.072 | -0.006 | 624 |  |
| ONLY high (> 2.27) - vol | +0.040 | +0.062 | 136 | ✅ |
| ONLY low (< 1.34) - ivol | +0.040 | +0.060 | 606 | ✅ |
| ONLY high (> 0.56) - dayrange | +0.019 | -0.009 | 590 |  |
| ONLY mid - trend | +0.014 | -0.024 | 789 |  |
| ONLY mid - daymove | -0.001 | +0.173 | 561 | ✅ |

### Best 2 rules combined (picked on TRAIN, full candle-by-candle re-run): skip high (> 1.00) yrange AND skip mid gap
| Test | Trades | Win | ATR / trade | PF | Total ATR | Worst drawdown (ATR) | Longest losing run |
|---|---|---|---|---|---|---|---|
| v3.0 TRAIN | 2823 | 40% | **-0.00** | 0.99 | -14 | 176.6 | 16 |
| **combined TRAIN** | 1152 | 43% | **+0.12** | 1.13 | +132 | 88.3 | 13 |
| v3.0 TEST (never seen) | 1860 | 41% | **+0.03** | 1.04 | +60 | 63.6 | 13 |
| **combined TEST (never seen)** | 911 | 43% | **+0.10** | 1.11 | +93 | 37.1 | 12 |

| Year | Trades | ATR / trade (combined) | ATR / trade (v3.0) |
|---|---|---|---|
| 2020 | 294 | **-0.01** | -0.03 |
| 2021 | 266 | **+0.04** | -0.10 |
| 2022 | 322 | **+0.20** | +0.08 |
| 2023 | 270 | **+0.23** | +0.03 |
| 2024 | 313 | **+0.02** | -0.03 |
| 2025 | 316 | **+0.15** | +0.10 |
| 2026 | 282 | **+0.14** | +0.02 |

## QQQ 3-minute
TRAIN 2020-2023: 2303 trades, **-0.020** ATR/trade | TEST 2024-now: 1465 trades, **+0.148** ATR/trade (thirds hold ~767 trades each: differences under about 0.10 are noise)

### Each condition split into thirds (cut points from TRAIN only)
| Condition | Third | TRAIN n | TRAIN ATR | TEST n | TEST ATR |
|---|---|---|---|---|---|
| Daily trend: yesterday's close vs its 20-day average (ATR, + = with my trade) | low (< -1.14) | 752 | -0.04 | 416 | +0.22 |
|  | mid | 751 | -0.03 | 643 | +0.06 |
|  | high (> 1.03) | 752 | +0.03 | 406 | +0.22 |
| Today's opening gap (daily ATR, + = gap in my trade's direction) | low (< -0.12) | 767 | -0.11 | 539 | +0.22 |
|  | mid | 767 | -0.06 | 438 | +0.15 |
|  | high (> 0.15) | 767 | +0.11 | 488 | +0.07 |
| Move since today's 9:30 open (daily ATR, + = day already moving my way) | low (< 0.05) | 767 | -0.01 | 522 | -0.01 |
|  | mid | 767 | -0.07 | 441 | +0.18 |
|  | high (> 0.16) | 767 | +0.02 | 502 | +0.28 |
| Distance from VWAP at the signal (3m ATR, + = stretched my way) | low (< 0.46) | 768 | +0.01 | 436 | -0.04 |
|  | mid | 767 | -0.06 | 526 | +0.10 |
|  | high (> 1.29) | 768 | -0.01 | 503 | +0.37 |
| Volatility level: daily ATR as % of price | low (< 1.53) | 760 | -0.08 | 792 | +0.18 |
|  | mid | 773 | -0.02 | 573 | +0.14 |
|  | high (> 2.28) | 768 | +0.04 | 100 | -0.09 |
| Yesterday's range vs normal (1 = normal day) | low (< 0.73) | 764 | +0.06 | 612 | +0.18 |
|  | mid | 768 | -0.08 | 413 | +0.15 |
|  | high (> 1.00) | 769 | -0.04 | 440 | +0.11 |
| Today's range so far vs normal | low (< 0.35) | 767 | -0.02 | 526 | +0.18 |
|  | mid | 767 | -0.08 | 482 | +0.14 |
|  | high (> 0.54) | 767 | +0.04 | 457 | +0.13 |
| 3-minute ATR now vs its 20-day normal | low (< 1.37) | 768 | +0.23 | 520 | +0.11 |
|  | mid | 767 | -0.09 | 485 | +0.22 |
|  | high (> 1.79) | 768 | -0.20 | 460 | +0.12 |
| Time of day | 9:35-10:30 | 1039 | -0.07 | 679 | +0.19 |
|  | 10:30-12:00 | 532 | -0.01 | 327 | +0.08 |
|  | 12:00-14:00 | 352 | -0.01 | 231 | +0.27 |
|  | 14:00-15:30 | 380 | +0.08 | 228 | -0.00 |

### Rules picked on TRAIN, checked on TEST
Baseline v3.0: TRAIN -0.020 | TEST +0.148. ✅ = helps on BOTH TRAIN and TEST.
| Rule | TRAIN ATR | TEST ATR | TEST trades | |
|---|---|---|---|---|
| skip high (> 1.79) - ivol | +0.070 | +0.161 | 1005 | ✅ |
| skip low (< -0.12) - gap | +0.029 | +0.106 | 926 |  |
| skip 9:35-10:30 - tod | +0.018 | +0.112 | 786 |  |
| skip mid - dayrange | +0.010 | +0.154 | 983 | ✅ |
| skip low (< 1.53) - vol | +0.010 | +0.106 | 673 |  |
| skip mid - yrange | +0.009 | +0.148 | 1052 | ✅ |
| skip mid - daymove | +0.005 | +0.135 | 1024 |  |
| skip mid - vwap | +0.000 | +0.178 | 939 | ✅ |
| skip low (< -1.14) - trend | -0.001 | +0.121 | 1049 |  |
| ONLY low (< 1.37) - ivol | +0.225 | +0.109 | 520 |  |
| ONLY high (> 0.15) - gap | +0.113 | +0.070 | 488 |  |
| ONLY 14:00-15:30 - tod | +0.080 | -0.001 | 228 |  |
| ONLY low (< 0.73) - yrange | +0.060 | +0.179 | 612 | ✅ |
| ONLY high (> 0.54) - dayrange | +0.037 | +0.129 | 457 |  |
| ONLY high (> 2.28) - vol | +0.036 | -0.092 | 100 |  |
| ONLY high (> 1.03) - trend | +0.031 | +0.223 | 406 | ✅ |
| ONLY high (> 0.16) - daymove | +0.020 | +0.284 | 502 | ✅ |
| ONLY low (< 0.46) - vwap | +0.009 | -0.043 | 436 |  |

### Best 2 rules combined (picked on TRAIN, full candle-by-candle re-run): skip high (> 1.79) ivol AND skip low (< -0.12) gap
| Test | Trades | Win | ATR / trade | PF | Total ATR | Worst drawdown (ATR) | Longest losing run |
|---|---|---|---|---|---|---|---|
| v3.0 TRAIN | 2303 | 40% | **-0.02** | 0.98 | -47 | 162.2 | 17 |
| **combined TRAIN** | 1088 | 43% | **+0.13** | 1.14 | +142 | 64.8 | 10 |
| v3.0 TEST (never seen) | 1465 | 44% | **+0.15** | 1.17 | +217 | 41.4 | 15 |
| **combined TEST (never seen)** | 666 | 41% | **+0.07** | 1.07 | +45 | 56.0 | 15 |

| Year | Trades | ATR / trade (combined) | ATR / trade (v3.0) |
|---|---|---|---|
| 2020 | 304 | **+0.17** | +0.06 |
| 2021 | 250 | **-0.05** | -0.15 |
| 2022 | 252 | **+0.21** | -0.03 |
| 2023 | 282 | **+0.18** | +0.03 |
| 2024 | 251 | **-0.00** | +0.03 |
| 2025 | 240 | **+0.07** | +0.25 |
| 2026 | 175 | **+0.16** | +0.17 |

