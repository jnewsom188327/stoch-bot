# v4.0 signal + FILTERS - 2026-10-20 10:16 ET
Data 2020-01-01 to 2026-10-19, SPY, QQQ, 1m, 2m, 3m, 5m. Base = v4.0 signal (line flip + Vix Fix spike, as v3.0). DATA ONLY. Runtime 3 min.
**Edge** = +1-ATR-your-way-first rate minus the other way, halved (0 = coin flip). **Charts better** = charts where the filtered signal beat the plain signal in TEST (2024-now). **Hold** = ATR per trade held to 15:55 (TEST). ✅ = beats the plain signal by 1.0+ in BOTH periods and on 6+ of 8 charts. Luck check: on RANDOM price data, 1 of ~25 filters passed a looser (0.5) version of this test, so treat a single ✅ with care.

**Plain v4.0 signal (line flip + Vix Fix spike, as v3.0): 44,459 signals | TRAIN edge +1.0 | TEST edge +0.1 | hold to 15:55 +0.06 ATR**

## The answer in 30 seconds
- **Filters that make it better in both periods on most charts: 1**: Volume vs same time of day (20-day avg): 2.5+ (TEST +1.8 over the plain signal)
- Note: a filter that keeps only a small share of signals can look good by luck - check 'Kept' and 'Charts better'.

### Stoch %K your way (0 = fully oversold for longs / overbought for shorts)
| Filter | Kept | Edge 2020-2023 | Edge 2024-now | Charts better (TEST) | Hold (TEST) | |
|---|---|---|---|---|---|---|
| 0 to 20 | 7% | +1.8 | **+2.4** | 6/8 | -0.04 |  |
| 20 to 40 | 22% | +0.8 | **+1.0** | 6/8 | +0.12 |  |
| 40 to 60 | 24% | +1.7 | **-1.2** | 2/8 | +0.07 |  |
| 60 to 80 | 22% | +0.9 | **-0.8** | 3/8 | -0.00 |  |
| 80 to 101 | 26% | +0.4 | **+0.6** | 6/8 | +0.07 |  |

### Stoch %K crossed %D your way (last 2 candles)
| Filter | Kept | Edge 2020-2023 | Edge 2024-now | Charts better (TEST) | Hold (TEST) | |
|---|---|---|---|---|---|---|
| = no | 71% | +0.9 | **-0.2** | 3/8 | +0.04 |  |
| = yes | 29% | +1.4 | **+0.8** | 5/8 | +0.11 |  |

### Volume vs last 20 candles (1 = normal)
| Filter | Kept | Edge 2020-2023 | Edge 2024-now | Charts better (TEST) | Hold (TEST) | |
|---|---|---|---|---|---|---|
| 0 to 0.7 | 25% | +0.8 | **+1.0** | 7/8 | +0.11 |  |
| 0.7 to 1 | 24% | +1.2 | **+0.2** | 5/8 | +0.09 |  |
| 1 to 1.5 | 22% | +1.1 | **-0.5** | 3/8 | -0.09 |  |
| 1.5 to 2.5 | 16% | +0.7 | **-1.1** | 2/8 | +0.01 |  |
| 2.5+ | 13% | +1.3 | **+0.3** | 5/8 | +0.21 |  |

### Volume vs same time of day (20-day avg)
| Filter | Kept | Edge 2020-2023 | Edge 2024-now | Charts better (TEST) | Hold (TEST) | |
|---|---|---|---|---|---|---|
| 0 to 0.7 | 35% | +1.3 | **+0.0** | 5/8 | +0.06 |  |
| 0.7 to 1 | 25% | +0.5 | **-0.5** | 4/8 | +0.01 |  |
| 1 to 1.5 | 22% | +0.8 | **+1.1** | 5/8 | +0.07 |  |
| 1.5 to 2.5 | 12% | +0.9 | **-1.5** | 2/8 | -0.01 |  |
| 2.5+ | 6% | +2.4 | **+1.8** | 6/8 | +0.39 | ✅ helps |

### Last 3 candles' volume vs last 20 (the dip's volume)
| Filter | Kept | Edge 2020-2023 | Edge 2024-now | Charts better (TEST) | Hold (TEST) | |
|---|---|---|---|---|---|---|
| 0 to 0.7 | 19% | +0.6 | **+1.3** | 6/8 | +0.28 |  |
| 0.7 to 1 | 27% | +1.1 | **+0.5** | 4/8 | -0.05 |  |
| 1 to 1.5 | 24% | +2.1 | **-0.5** | 4/8 | +0.06 |  |
| 1.5 to 2.5 | 15% | +0.6 | **-0.8** | 2/8 | -0.01 |  |
| 2.5+ | 15% | +0.0 | **-0.5** | 3/8 | +0.04 |  |

### MACD histogram your way (ATR)
| Filter | Kept | Edge 2020-2023 | Edge 2024-now | Charts better (TEST) | Hold (TEST) | |
|---|---|---|---|---|---|---|
| under -0.3 | 5% | -0.0 | **+4.0** | 7/8 | +0.05 |  |
| -0.3 to -0.1 | 23% | +1.5 | **+0.7** | 6/8 | +0.19 |  |
| -0.1 to 0.1 | 34% | +1.5 | **-0.7** | 3/8 | -0.05 |  |
| 0.1 to 0.3 | 25% | +0.6 | **-1.1** | 2/8 | +0.11 |  |
| 0.3+ | 13% | +0.1 | **+1.5** | 6/8 | +0.04 |  |

### MACD histogram turning your way
| Filter | Kept | Edge 2020-2023 | Edge 2024-now | Charts better (TEST) | Hold (TEST) | |
|---|---|---|---|---|---|---|
| = no | 15% | +0.9 | **-0.9** | 2/8 | -0.07 |  |
| = yes | 85% | +1.0 | **+0.2** | 6/8 | +0.08 |  |

### MACD line on your side of zero
| Filter | Kept | Edge 2020-2023 | Edge 2024-now | Charts better (TEST) | Hold (TEST) | |
|---|---|---|---|---|---|---|
| = no | 19% | +0.5 | **+1.0** | 5/8 | -0.04 |  |
| = yes | 81% | +1.1 | **-0.2** | 3/8 | +0.08 |  |

### Distance from VWAP your side (ATR)
| Filter | Kept | Edge 2020-2023 | Edge 2024-now | Charts better (TEST) | Hold (TEST) | |
|---|---|---|---|---|---|---|
| 0 to 0.5 | 37% | +0.8 | **+0.7** | 6/8 | +0.06 |  |
| 0.5 to 1 | 21% | +1.3 | **-0.8** | 2/8 | +0.11 |  |
| 1 to 2 | 20% | +0.9 | **+0.5** | 6/8 | +0.02 |  |
| 2+ | 23% | +1.0 | **-0.7** | 3/8 | +0.04 |  |

### VIX FIX pane bar YOUR way (0-100; red before longs, blue before shorts)
| Filter | Kept | Edge 2020-2023 | Edge 2024-now | Charts better (TEST) | Hold (TEST) | |
|---|---|---|---|---|---|---|
| 0 to 20 | 16% | +1.0 | **+2.2** | 7/8 | +0.28 |  |
| 20 to 40 | 26% | +2.2 | **-0.7** | 3/8 | -0.07 |  |
| 40 to 60 | 21% | -0.6 | **-0.7** | 3/8 | -0.06 |  |
| 60 to 80 | 18% | +1.6 | **+0.5** | 5/8 | +0.11 |  |
| 80 to 95 | 12% | +0.1 | **-2.1** | 2/8 | -0.03 |  |
| 95 to 101 | 8% | +1.2 | **+2.4** | 7/8 | +0.35 |  |

### VIX FIX pane bar AGAINST you (0-100)
| Filter | Kept | Edge 2020-2023 | Edge 2024-now | Charts better (TEST) | Hold (TEST) | |
|---|---|---|---|---|---|---|
| 0 to 20 | 9% | +1.4 | **+2.3** | 4/8 | +0.04 |  |
| 20 to 40 | 23% | +1.4 | **+1.3** | 5/8 | +0.09 |  |
| 40 to 60 | 25% | +0.1 | **-0.2** | 5/8 | +0.05 |  |
| 60 to 80 | 17% | +2.2 | **-2.3** | 1/8 | -0.05 |  |
| 80 to 95 | 9% | +1.4 | **+0.9** | 5/8 | +0.09 |  |
| 95 to 101 | 17% | +0.1 | **-0.6** | 3/8 | +0.13 |  |

### Candles since a Vix Fix spike your way
| Filter | Kept | Edge 2020-2023 | Edge 2024-now | Charts better (TEST) | Hold (TEST) | |
|---|---|---|---|---|---|---|
| 0 to 1 | 19% | +1.1 | **+0.0** | 4/8 | +0.06 |  |
| 1 to 3 | 22% | +2.1 | **-0.8** | 2/8 | +0.03 |  |
| 3 to 6 | 23% | +1.3 | **-0.4** | 3/8 | +0.02 |  |
| 6 to 11 | 33% | +0.3 | **+1.1** | 6/8 | +0.01 |  |
| 11+ | 3% | -2.2 | **-1.1** | 2/8 | +1.18 |  |

### TTM momentum your way (ATR)
| Filter | Kept | Edge 2020-2023 | Edge 2024-now | Charts better (TEST) | Hold (TEST) | |
|---|---|---|---|---|---|---|
| under -1 | 15% | +1.3 | **+2.0** | 7/8 | +0.18 |  |
| -1 to -0.3 | 22% | +1.4 | **+0.5** | 5/8 | +0.02 |  |
| -0.3 to 0.3 | 24% | +1.3 | **-0.5** | 4/8 | -0.08 |  |
| 0.3 to 1 | 23% | +0.4 | **-0.9** | 3/8 | +0.08 |  |
| 1 to 2 | 13% | +0.7 | **+0.0** | 6/8 | +0.13 |  |
| 2+ | 3% | +0.9 | **-1.0** | 4/8 | +0.37 |  |

### TTM momentum slope your way (ATR per candle)
| Filter | Kept | Edge 2020-2023 | Edge 2024-now | Charts better (TEST) | Hold (TEST) | |
|---|---|---|---|---|---|---|
| under -0.3 | 7% | +1.5 | **+0.7** | 4/8 | +0.03 |  |
| -0.3 to -0.1 | 15% | +1.5 | **+0.1** | 5/8 | +0.08 |  |
| -0.1 to 0.1 | 21% | +1.5 | **-1.4** | 2/8 | +0.13 |  |
| 0.1 to 0.3 | 23% | +0.9 | **+1.7** | 7/8 | +0.05 |  |
| 0.3+ | 34% | +0.4 | **-0.3** | 3/8 | +0.01 |  |

### TTM color (vs your trade)
| Filter | Kept | Edge 2020-2023 | Edge 2024-now | Charts better (TEST) | Hold (TEST) | |
|---|---|---|---|---|---|---|
| = blue-type: with you, fading | 16% | +1.8 | **-1.4** | 1/8 | +0.12 |  |
| = cyan-type: with you, rising | 35% | -0.2 | **-0.3** | 2/8 | +0.08 |  |
| = red-type: against you, falling | 16% | +1.2 | **+0.6** | 5/8 | +0.04 |  |
| = yellow-type: against you, turning | 33% | +1.8 | **+0.8** | 6/8 | +0.01 |  |

### TTM squeeze
| Filter | Kept | Edge 2020-2023 | Edge 2024-now | Charts better (TEST) | Hold (TEST) | |
|---|---|---|---|---|---|---|
| = fired 0-3 candles ago | 10% | -0.3 | **+1.1** | 6/8 | +0.28 |  |
| = fired 4-10 ago | 13% | +3.1 | **+0.2** | 5/8 | +0.14 |  |
| = in squeeze | 27% | +1.6 | **-0.7** | 3/8 | -0.15 |  |
| = none in 10+ | 50% | +0.4 | **+0.2** | 5/8 | +0.11 |  |

