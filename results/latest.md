# Trend Flip v3.0 / v4.0 backtest - 2026-10-18 15:01 ET
Data: 2020-01-01 to 2026-10-17, 2/3-minute candles. ATR / trade = average result per trade in ATR (the same number as the TradingView box). Healthy = above +0.30 with PF above 1.3.

## SPY 2-minute  (sip data, 2019-12-31 to 2026-10-16)

### v4.0 ideas vs v3.0 (one change at a time)
| Test | Trades | Win | ATR / trade | PF | Total ATR | Worst drawdown (ATR) | Longest losing run |
|---|---|---|---|---|---|---|---|
| **v3.0 (your settings)** | 4807 | 40% | **+0.00** | 1.00 | +0 | 212.4 | 15 |
| ENTRY + 15m agrees | 2715 | 40% | **-0.03** | 0.96 | -95 | 180.0 | 17 |
| ENTRY + 15m and 60m agree | 1854 | 41% | **-0.02** | 0.98 | -34 | 136.8 | 15 |
| EXIT ride strong trend | 4801 | 36% | **+0.05** | 1.05 | +218 | 137.8 | 20 |
| EXIT ride if 15m agrees | 4802 | 38% | **+0.03** | 1.04 | +163 | 158.8 | 20 |
| EXIT cut losers on warning | 5315 | 29% | **-0.01** | 0.99 | -30 | 220.1 | 20 |
| EXIT ride + cut losers | 5314 | 27% | **+0.02** | 1.03 | +126 | 161.9 | 21 |
| 15m agrees + ride + cut | 2971 | 28% | **+0.01** | 1.02 | +35 | 115.4 | 21 |
| no Vix Fix filter | 9436 | 42% | **+0.03** | 1.04 | +318 | 193.9 | 18 |
| Vix Fix spike within 5 | 3303 | 38% | **-0.02** | 0.98 | -51 | 227.7 | 15 |
| Vix Fix spike within 20 | 6844 | 42% | **+0.04** | 1.05 | +279 | 205.5 | 16 |
| hold 10 candles | 4905 | 44% | **-0.01** | 0.99 | -30 | 238.8 | 18 |
| hold 25 candles | 4690 | 36% | **+0.04** | 1.03 | +171 | 155.7 | 16 |
| stop 1.5 ATR | 5002 | 36% | **+0.02** | 1.02 | +85 | 144.1 | 15 |
| stop 3 ATR | 4657 | 43% | **-0.00** | 1.00 | -1 | 180.1 | 12 |

### v3.0 details
- Longs: 2422 trades, +0.00 ATR | Shorts: 2385 trades, -0.00 ATR
- 1st half +0.00 | 2nd half -0.00 ATR per trade
- Went +1 ATR your way before -1 ATR against: 51% | avg best +2.0 / avg worst -1.5 ATR
- 3.0 trades per trading day | rough $ per option per trade (0.6 delta, before theta + spread): $-0

### v3.0 by year
| Year | Trades | Win | ATR / trade | PF | Total ATR |
|---|---|---|---|---|---|
| 2020 | 732 | 43% | **+0.09** | 1.10 | +62 |
| 2021 | 727 | 40% | **+0.01** | 1.01 | +9 |
| 2022 | 680 | 40% | **-0.03** | 0.97 | -21 |
| 2023 | 750 | 38% | **-0.09** | 0.91 | -68 |
| 2024 | 677 | 38% | **-0.04** | 0.96 | -24 |
| 2025 | 740 | 42% | **+0.04** | 1.04 | +28 |
| 2026 | 501 | 41% | **+0.03** | 1.03 | +14 |

## SPY 3-minute  (sip data, 2019-12-31 to 2026-10-16)

### v4.0 ideas vs v3.0 (one change at a time)
| Test | Trades | Win | ATR / trade | PF | Total ATR | Worst drawdown (ATR) | Longest losing run |
|---|---|---|---|---|---|---|---|
| **v3.0 (your settings)** | 3796 | 40% | **+0.01** | 1.01 | +33 | 204.0 | 13 |
| ENTRY + 15m agrees | 2274 | 41% | **+0.03** | 1.03 | +61 | 137.6 | 16 |
| ENTRY + 15m and 60m agree | 1534 | 42% | **+0.05** | 1.06 | +84 | 83.9 | 11 |
| EXIT ride strong trend | 3787 | 36% | **+0.03** | 1.03 | +125 | 151.2 | 14 |
| EXIT ride if 15m agrees | 3790 | 37% | **+0.04** | 1.04 | +136 | 135.9 | 14 |
| EXIT cut losers on warning | 4215 | 29% | **+0.00** | 1.00 | +12 | 251.6 | 22 |
| EXIT ride + cut losers | 4214 | 27% | **+0.02** | 1.02 | +74 | 205.5 | 22 |
| 15m agrees + ride + cut | 2537 | 28% | **+0.04** | 1.06 | +114 | 133.6 | 23 |
| no Vix Fix filter | 7328 | 41% | **+0.02** | 1.02 | +160 | 235.2 | 15 |
| Vix Fix spike within 5 | 2666 | 38% | **-0.01** | 0.99 | -20 | 159.4 | 15 |
| Vix Fix spike within 20 | 5340 | 41% | **+0.03** | 1.03 | +159 | 247.5 | 12 |
| hold 10 candles | 3864 | 44% | **-0.02** | 0.97 | -94 | 261.0 | 13 |
| hold 25 candles | 3656 | 35% | **+0.04** | 1.03 | +130 | 137.0 | 16 |
| stop 1.5 ATR | 3945 | 36% | **+0.01** | 1.01 | +36 | 192.2 | 14 |
| stop 3 ATR | 3642 | 43% | **+0.02** | 1.02 | +56 | 171.0 | 13 |

### v3.0 details
- Longs: 1898 trades, +0.03 ATR | Shorts: 1898 trades, -0.01 ATR
- 1st half -0.05 | 2nd half +0.06 ATR per trade
- Went +1 ATR your way before -1 ATR against: 51% | avg best +2.0 / avg worst -1.5 ATR
- 2.5 trades per trading day | rough $ per option per trade (0.6 delta, before theta + spread): $-1

### v3.0 by year
| Year | Trades | Win | ATR / trade | PF | Total ATR |
|---|---|---|---|---|---|
| 2020 | 582 | 40% | **+0.05** | 1.06 | +30 |
| 2021 | 572 | 37% | **-0.06** | 0.94 | -36 |
| 2022 | 550 | 39% | **-0.15** | 0.84 | -84 |
| 2023 | 558 | 41% | **+0.01** | 1.01 | +4 |
| 2024 | 542 | 39% | **-0.02** | 0.98 | -8 |
| 2025 | 559 | 42% | **+0.17** | 1.19 | +94 |
| 2026 | 433 | 42% | **+0.08** | 1.09 | +33 |

## QQQ 2-minute  (sip data, 2019-12-31 to 2026-10-16)

### v4.0 ideas vs v3.0 (one change at a time)
| Test | Trades | Win | ATR / trade | PF | Total ATR | Worst drawdown (ATR) | Longest losing run |
|---|---|---|---|---|---|---|---|
| **v3.0 (your settings)** | 4683 | 41% | **+0.01** | 1.01 | +47 | 176.6 | 16 |
| ENTRY + 15m agrees | 2663 | 41% | **-0.00** | 1.00 | -8 | 119.2 | 16 |
| ENTRY + 15m and 60m agree | 1819 | 42% | **-0.02** | 0.98 | -32 | 119.8 | 12 |
| EXIT ride strong trend | 4671 | 36% | **+0.01** | 1.01 | +55 | 214.6 | 16 |
| EXIT ride if 15m agrees | 4677 | 38% | **+0.00** | 1.00 | +14 | 206.2 | 16 |
| EXIT cut losers on warning | 5168 | 30% | **-0.00** | 1.00 | -6 | 166.9 | 24 |
| EXIT ride + cut losers | 5168 | 28% | **+0.00** | 1.00 | +5 | 227.0 | 24 |
| 15m agrees + ride + cut | 2899 | 29% | **-0.03** | 0.96 | -81 | 148.2 | 27 |
| no Vix Fix filter | 9205 | 42% | **+0.02** | 1.02 | +176 | 207.2 | 14 |
| Vix Fix spike within 5 | 3183 | 39% | **-0.00** | 1.00 | -6 | 139.5 | 18 |
| Vix Fix spike within 20 | 6745 | 42% | **+0.03** | 1.03 | +187 | 188.5 | 13 |
| hold 10 candles | 4761 | 44% | **-0.01** | 0.99 | -44 | 191.0 | 14 |
| hold 25 candles | 4565 | 36% | **+0.03** | 1.02 | +116 | 221.7 | 15 |
| stop 1.5 ATR | 4858 | 36% | **+0.02** | 1.02 | +89 | 164.7 | 17 |
| stop 3 ATR | 4535 | 43% | **-0.00** | 1.00 | -12 | 216.4 | 13 |

### v3.0 details
- Longs: 2369 trades, +0.04 ATR | Shorts: 2314 trades, -0.02 ATR
- 1st half -0.00 | 2nd half +0.02 ATR per trade
- Went +1 ATR your way before -1 ATR against: 50% | avg best +1.9 / avg worst -1.5 ATR
- 2.9 trades per trading day | rough $ per option per trade (0.6 delta, before theta + spread): $+0

### v3.0 by year
| Year | Trades | Win | ATR / trade | PF | Total ATR |
|---|---|---|---|---|---|
| 2020 | 703 | 39% | **-0.03** | 0.97 | -20 |
| 2021 | 702 | 39% | **-0.10** | 0.89 | -71 |
| 2022 | 676 | 42% | **+0.08** | 1.09 | +57 |
| 2023 | 742 | 41% | **+0.03** | 1.03 | +20 |
| 2024 | 673 | 40% | **-0.03** | 0.96 | -23 |
| 2025 | 682 | 42% | **+0.10** | 1.12 | +71 |
| 2026 | 505 | 40% | **+0.02** | 1.03 | +12 |

## QQQ 3-minute  (sip data, 2019-12-31 to 2026-10-16)

### v4.0 ideas vs v3.0 (one change at a time)
| Test | Trades | Win | ATR / trade | PF | Total ATR | Worst drawdown (ATR) | Longest losing run |
|---|---|---|---|---|---|---|---|
| **v3.0 (your settings)** | 3768 | 41% | **+0.05** | 1.05 | +170 | 162.2 | 17 |
| ENTRY + 15m agrees | 2262 | 43% | **+0.10** | 1.11 | +220 | 76.1 | 10 |
| ENTRY + 15m and 60m agree | 1503 | 44% | **+0.08** | 1.09 | +113 | 84.6 | 14 |
| EXIT ride strong trend | 3760 | 37% | **+0.05** | 1.05 | +189 | 139.6 | 17 |
| EXIT ride if 15m agrees | 3762 | 38% | **+0.06** | 1.07 | +232 | 126.3 | 17 |
| EXIT cut losers on warning | 4185 | 30% | **+0.04** | 1.06 | +178 | 146.5 | 17 |
| EXIT ride + cut losers | 4184 | 28% | **+0.03** | 1.04 | +138 | 134.1 | 20 |
| 15m agrees + ride + cut | 2519 | 29% | **+0.09** | 1.12 | +215 | 67.9 | 25 |
| no Vix Fix filter | 7069 | 42% | **+0.02** | 1.02 | +154 | 174.6 | 13 |
| Vix Fix spike within 5 | 2694 | 40% | **+0.05** | 1.05 | +128 | 141.4 | 14 |
| Vix Fix spike within 20 | 5190 | 42% | **+0.06** | 1.06 | +300 | 148.8 | 15 |
| hold 10 candles | 3846 | 44% | **+0.03** | 1.04 | +115 | 140.7 | 14 |
| hold 25 candles | 3638 | 36% | **+0.07** | 1.07 | +262 | 112.3 | 15 |
| stop 1.5 ATR | 3900 | 38% | **+0.08** | 1.10 | +321 | 121.3 | 18 |
| stop 3 ATR | 3633 | 44% | **+0.04** | 1.04 | +157 | 138.5 | 16 |

### v3.0 details
- Longs: 1828 trades, +0.03 ATR | Shorts: 1940 trades, +0.06 ATR
- 1st half -0.04 | 2nd half +0.13 ATR per trade
- Went +1 ATR your way before -1 ATR against: 51% | avg best +2.0 / avg worst -1.5 ATR
- 2.5 trades per trading day | rough $ per option per trade (0.6 delta, before theta + spread): $+1

### v3.0 by year
| Year | Trades | Win | ATR / trade | PF | Total ATR |
|---|---|---|---|---|---|
| 2020 | 583 | 43% | **+0.06** | 1.06 | +33 |
| 2021 | 568 | 35% | **-0.15** | 0.85 | -84 |
| 2022 | 558 | 39% | **-0.03** | 0.97 | -16 |
| 2023 | 594 | 41% | **+0.03** | 1.03 | +19 |
| 2024 | 525 | 42% | **+0.03** | 1.03 | +16 |
| 2025 | 533 | 45% | **+0.25** | 1.30 | +133 |
| 2026 | 407 | 44% | **+0.17** | 1.19 | +68 |

