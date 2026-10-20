# TREND LINE STUDY - 2026-10-20 07:33 ET
Data 2020-01-01 to 2026-10-19, SPY, QQQ, 1m, 2m, 3m, 5m. DATA ONLY - no orders. Runtime 4 min.
**Edge** = how much more often price went +1 ATR YOUR way before 1 ATR against, than the other way, at the same moment (percentage points, over the next 30 candles; 0 = coin flip). Half of the difference, so +5 means e.g. 55% vs 45%. **R** = the same idea for a +2 / -1 ATR bracket, in ATR per trade. TRAIN = 2020-2023 (everything is picked here). TEST = 2024-now (never used to pick).

## The answer in 30 seconds
- **Recipes that held up on 2024-now (never seen): 1 of 4**
- Luck reference: the same search on RANDOM price data found recipes with TRAIN edge about +2 to +2.5 that fell to about 0 (or below) on TEST. A real recipe needs a clearly positive TEST edge on nearly every chart.
- **PINK appears -> long / BLUE appears -> short - FADED**: Fast-slow EMA gap (ATR, + = your way) >= 1.152 AND TTM momentum slope (ATR, + = turning your way) <= -0.421 -> TRAIN edge +7.0 (event alone +1.0) | **TEST edge +2.3** (event alone +0.1), helped on 7/8 charts in TEST, R(+2/-1) +0.058 ATR ✅
- **RED or PINK ends -> long / GREEN or BLUE ends -> short**: 3m trend = agrees AND TTM momentum size (ATR, + = your way) >= -1.27 AND Length of the previous color run (bars) <= 11 -> TRAIN edge +2.8 (event alone +0.3) | **TEST edge +0.5** (event alone +0.7), helped on 3/6 charts in TEST, R(+2/-1) -0.007 ATR
- **Line turns GREEN (long) / RED (short)**: Slow EMA 34 slope (ATR per 5 bars, + = your way) <= 0.116 AND VIX FIX pane bar YOUR way (0-100 as on your pane; red fear for longs, blue greed for shorts) <= 36.932 AND Volatility now vs normal (ATR ratio) <= 1.522 -> TRAIN edge +4.1 (event alone +1.0) | **TEST edge -0.5** (event alone +0.0), helped on 3/8 charts in TEST, R(+2/-1) -0.019 ATR
- **Strong color returns after a warning**: TTM momentum color (vs your trade) = against you + turning (yellow for longs) AND Distance from VWAP (ATR, + = your side) >= 4.273 AND Vix Fix raw number YOUR way <= 0.285 -> TRAIN edge +4.1 (event alone +0.6) | **TEST edge -1.1** (event alone -0.5), helped on 1/8 charts in TEST, R(+2/-1) -0.019 ATR

## 1. Line anatomy - how long green and red runs last (runs starting 9:30-16:00)
| Chart | Color | Runs | Median length | 80% are shorter than | Chop (2 bars or less) | 10+ bars | Avg move start->end (ATR) | Avg best move (ATR) |
|---|---|---|---|---|---|---|---|---|
| 1m | GREEN | 23,030 | 9 bars (9 min) | 47 bars (47 min) | 26% | 49% | +0.83 | 2.74 |
| 1m | RED | 21,152 | 8 bars (8 min) | 39 bars (39 min) | 29% | 46% | +0.79 | 2.96 |
| 2m | GREEN | 13,933 | 8 bars (16 min) | 44 bars (88 min) | 28% | 46% | +0.90 | 2.54 |
| 2m | RED | 13,403 | 6 bars (12 min) | 35 bars (70 min) | 31% | 42% | +0.84 | 2.75 |
| 3m | GREEN | 10,626 | 7 bars (21 min) | 44 bars (132 min) | 30% | 44% | +0.96 | 2.40 |
| 3m | RED | 10,376 | 6 bars (18 min) | 33 bars (99 min) | 32% | 40% | +0.86 | 2.61 |
| 5m | GREEN | 7,508 | 7 bars (35 min) | 44 bars (220 min) | 29% | 44% | +1.02 | 2.28 |
| 5m | RED | 7,795 | 5 bars (25 min) | 30 bars (150 min) | 33% | 38% | +0.88 | 2.39 |

## 2. The entry events by themselves (edge per cell: SPY 2020-2023 | SPY 2024-now | QQQ 2020-2023 | QQQ 2024-now). FADED = the same numbers with the sign flipped.
| Event | Direction | Chart | Events/yr per symbol | Edge per cell | R (+2/-1) per cell |
|---|---|---|---|---|---|
| Turns green/red | as is | 1m | 2865 | +0.5 | +1.0 | +1.6 | -0.9 | +0.013 | +0.012 | +0.030 | -0.031 |
| Turns green/red | as is | 2m | 1770 | +1.7 | +0.4 | +0.9 | -0.5 | +0.034 | +0.015 | +0.005 | -0.014 |
| Turns green/red | as is | 3m | 1370 | +0.5 | +0.2 | +1.1 | -0.3 | +0.009 | +0.006 | +0.008 | +0.010 |
| Turns green/red | as is | 5m | 1017 | +1.5 | +0.2 | +0.0 | +0.3 | +0.025 | -0.001 | +0.001 | +0.017 |
| Red/pink ends | as is | 1m | 2895 | -0.3 | +1.1 | +1.4 | +2.1 | -0.002 | +0.017 | +0.023 | +0.033 |
| Red/pink ends | as is | 2m | 1776 | +0.2 | +1.2 | +0.8 | +0.9 | +0.008 | +0.018 | +0.005 | +0.021 |
| Red/pink ends | as is | 3m | 1354 | -0.6 | -0.4 | +0.1 | -0.5 | -0.029 | -0.005 | -0.006 | -0.001 |
| Red/pink ends | as is | 5m | 972 | -0.6 | +0.4 | +0.4 | -3.0 | -0.020 | -0.015 | -0.001 | -0.077 |
| Pink/blue appears | as is | 1m | 3673 | -1.6 | -1.1 | -0.9 | +0.6 | -0.039 | -0.018 | -0.025 | +0.012 |
| Pink/blue appears | as is | 2m | 1806 | -1.1 | -0.7 | -0.9 | +0.7 | -0.038 | -0.030 | -0.024 | +0.006 |
| Pink/blue appears | as is | 3m | 1156 | -0.7 | -0.0 | -1.1 | -0.7 | -0.004 | -0.010 | -0.034 | -0.017 |
| Pink/blue appears | as is | 5m | 604 | +1.2 | +1.0 | -1.1 | +1.3 | +0.002 | +0.021 | -0.032 | +0.010 |
| Strong again | as is | 1m | 2550 | +1.7 | +0.0 | +0.4 | -0.3 | +0.031 | +0.006 | +0.010 | -0.003 |
| Strong again | as is | 2m | 1285 | +0.9 | -0.3 | +0.9 | -0.4 | +0.020 | -0.007 | +0.031 | -0.015 |
| Strong again | as is | 3m | 842 | -0.6 | -0.8 | -0.6 | -1.2 | -0.017 | +0.011 | -0.012 | -0.016 |
| Strong again | as is | 5m | 446 | -1.3 | -2.7 | -1.2 | -1.3 | -0.009 | -0.055 | -0.001 | -0.057 |

## 4. Confluence recipes step by step (each step picked on TRAIN; must help every chart in TRAIN)
### Line turns GREEN (long) / RED (short)
| Step | Add condition | Events kept TRAIN / TEST | TRAIN edge | TEST edge |
|---|---|---|---|---|
| 0 | (event alone) | 56,533 / 38,600 | +1.0 | +0.0 |
| 1 | Slow EMA 34 slope (ATR per 5 bars, + = your way) <= 0.116 | 22,559 / 15,503 | +1.6 | **-0.1** |
| 2 | VIX FIX pane bar YOUR way (0-100 as on your pane; red fear for longs, blue greed for shorts) <= 36.932 | 8,875 / 6,210 | +2.9 | **+0.2** |
| 3 | Volatility now vs normal (ATR ratio) <= 1.522 | 5,793 / 3,986 | +4.1 | **-0.5** |

| Chart | TRAIN edge (n) | TEST edge (n) |
|---|---|---|
| SPY 1m | +1.9 (1143) | **-0.4** (828) |
| SPY 2m | +5.2 (738) | **+0.5** (501) |
| SPY 3m | +3.0 (686) | **-5.2** (382) |
| SPY 5m | +4.7 (564) | **-0.2** (293) |
| QQQ 1m | +8.0 (966) | **+1.5** (812) |
| QQQ 2m | +3.1 (661) | **+1.0** (471) |
| QQQ 3m | +4.1 (599) | **-3.4** (379) |
| QQQ 5m | +1.4 (436) | **-0.2** (320) |

### Line turns GREEN (long) / RED (short) - FADED
No condition helped every chart in TRAIN.

### RED or PINK ends -> long / GREEN or BLUE ends -> short
| Step | Add condition | Events kept TRAIN / TEST | TRAIN edge | TEST edge |
|---|---|---|---|---|
| 0 | (event alone) | 56,265 / 38,519 | +0.3 | +0.7 |
| 1 | 3m trend = agrees | 10,155 / 7,117 | +1.1 | **+1.2** |
| 2 | TTM momentum size (ATR, + = your way) >= -1.27 | 6,584 / 4,784 | +2.1 | **+0.5** |
| 3 | Length of the previous color run (bars) <= 11 | 5,124 / 3,798 | +2.8 | **+0.5** |

| Chart | TRAIN edge (n) | TEST edge (n) |
|---|---|---|
| SPY 1m | +1.8 (1580) | **+2.4** (1143) |
| SPY 2m | +2.8 (527) | **-0.9** (377) |
| SPY 3m | - | - |
| SPY 5m | +1.5 (558) | **+0.0** (393) |
| QQQ 1m | +4.6 (1427) | **+1.4** (1098) |
| QQQ 2m | +2.6 (510) | **+1.5** (403) |
| QQQ 3m | - | - |
| QQQ 5m | +2.4 (522) | **-7.0** (384) |

### RED or PINK ends -> long / GREEN or BLUE ends -> short - FADED
No condition helped every chart in TRAIN.

### PINK appears -> long / BLUE appears -> short
No condition helped every chart in TRAIN.

### PINK appears -> long / BLUE appears -> short - FADED
| Step | Add condition | Events kept TRAIN / TEST | TRAIN edge | TEST edge |
|---|---|---|---|---|
| 0 | (event alone) | 57,965 / 40,103 | +1.0 | +0.1 |
| 1 | Fast-slow EMA gap (ATR, + = your way) >= 1.152 | 11,596 / 7,686 | +4.6 | **+1.4** |
| 2 | TTM momentum slope (ATR, + = turning your way) <= -0.421 | 4,984 / 3,164 | +7.0 | **+2.3** |

| Chart | TRAIN edge (n) | TEST edge (n) |
|---|---|---|
| SPY 1m | +7.6 (1271) | **+3.5** (753) |
| SPY 2m | +6.8 (562) | **+6.2** (384) |
| SPY 3m | +10.8 (334) | **-5.2** (233) |
| SPY 5m | +3.2 (186) | **+1.0** (146) |
| QQQ 1m | +6.4 (1399) | **+0.5** (814) |
| QQQ 2m | +6.1 (651) | **+3.6** (420) |
| QQQ 3m | +8.8 (368) | **+2.6** (265) |
| QQQ 5m | +4.2 (213) | **+5.0** (149) |

### Strong color returns after a warning
| Step | Add condition | Events kept TRAIN / TEST | TRAIN edge | TEST edge |
|---|---|---|---|---|
| 0 | (event alone) | 41,140 / 28,275 | +0.6 | -0.5 |
| 1 | TTM momentum color (vs your trade) = against you + turning (yellow for longs) | 10,121 / 7,157 | +1.8 | **-0.5** |
| 2 | Distance from VWAP (ATR, + = your side) >= 4.273 | 4,296 / 3,065 | +3.7 | **-1.0** |
| 3 | Vix Fix raw number YOUR way <= 0.285 | 3,709 / 2,884 | +4.1 | **-1.1** |

| Chart | TRAIN edge (n) | TEST edge (n) |
|---|---|---|
| SPY 1m | +5.5 (1228) | **-2.8** (966) |
| SPY 2m | +1.2 (417) | **-3.7** (311) |
| SPY 3m | +2.6 (153) | **-1.7** (121) |
| SPY 5m | +22.7 (11) | **+0.0** (12) |
| QQQ 1m | +3.6 (1320) | **+2.5** (963) |
| QQQ 2m | +5.4 (397) | **-2.3** (350) |
| QQQ 3m | +1.2 (167) | **-5.0** (140) |
| QQQ 5m | +12.5 (16) | **-4.8** (21) |

### Strong color returns after a warning - FADED
No condition helped every chart in TRAIN.

## 3. Single conditions (picked by TRAIN edge, checked on TEST)
Cells = edge for SPY 2020-2023 | SPY 2024-now | QQQ 2020-2023 | QQQ 2024-now. Charts OK = 1/2/3/5m charts where it helped in BOTH periods. Share = % of events kept.
### Line turns GREEN (long) / RED (short) (event alone: TRAIN +1.0, TEST +0.0)
| Condition | Share kept | TRAIN edge | TEST edge | Edge per cell | Cells > 0 | Charts OK |
|---|---|---|---|---|---|---|
| TTM momentum color (vs your trade) = against you + turning (yellow for longs) | 20% | +2.3 | **+0.6** | +2.4 | +1.1 | +2.2 | +0.2 | 4/4 | 2/4 |
| TTM squeeze = fired 4-10 bars ago | 14% | +2.0 | **+0.2** | +1.5 | +0.3 | +2.6 | +0.0 | 4/4 | 2/4 |
| TTM turn in the last 2 bars = turned YOUR way (red>yellow before a long) | 12% | +1.9 | **+0.6** | +1.3 | +1.3 | +2.6 | -0.0 | 3/4 | 2/4 |
| TTM squeeze = in squeeze | 26% | +1.8 | **-0.2** | +1.9 | -0.4 | +1.8 | +0.0 | 3/4 | 1/4 |
| Day's move so far (daily ATR, + = your way) >= 0.222 | 20% | +1.7 | **+1.0** | +2.2 | +1.0 | +1.2 | +0.9 | 4/4 | 3/4 |
| Slow EMA 34 slope (ATR per 5 bars, + = your way) <= 0.116 | 40% | +1.6 | **-0.1** | +1.4 | +0.2 | +1.9 | -0.3 | 3/4 | 2/4 |
| Signal candle body (ATR, + = your way) >= 0.761 | 40% | +1.6 | **+0.1** | +1.4 | +0.7 | +1.7 | -0.6 | 3/4 | 2/4 |
| Signal candle range (ATR) >= 1.196 | 40% | +1.6 | **-0.5** | +1.5 | -0.2 | +1.7 | -0.7 | 2/4 | 0/4 |
| Candles since a Vix Fix spike YOUR way <= 3 | 23% | +1.5 | **-0.1** | +1.4 | +0.4 | +1.7 | -0.6 | 3/4 | 1/4 |
| Signal candle range (ATR) >= 1.536 | 20% | +1.5 | **-1.3** | +1.4 | -1.3 | +1.7 | -1.3 | 2/4 | 0/4 |
| Signal candle body (ATR, + = your way) >= 1.11 | 20% | +1.5 | **-1.1** | +0.7 | -0.3 | +2.4 | -2.0 | 2/4 | 0/4 |
| Distance from VWAP (ATR, + = your side) >= 1.995 | 20% | +1.5 | **-0.7** | +1.4 | +0.1 | +1.6 | -1.4 | 3/4 | 2/4 |
| Distance from VWAP (ATR, + = your side) >= 0.972 | 40% | +1.5 | **-0.3** | +1.2 | +0.3 | +1.7 | -0.9 | 3/4 | 2/4 |
| VIX FIX pane bar AGAINST you (0-100) <= 36.317 | 20% | +1.5 | **+0.6** | +1.7 | +0.6 | +1.2 | +0.6 | 4/4 | 2/4 |
| TTM stretch vs typical wave (1 = median full stretch; + = momentum your way, - = against) <= -0.166 | 20% | +1.5 | **+0.6** | +1.7 | +0.9 | +1.3 | +0.3 | 4/4 | 3/4 |
| TTM momentum size (ATR, + = your way) <= 0.315 | 40% | +1.4 | **+0.2** | +1.4 | +0.5 | +1.5 | -0.1 | 3/4 | 3/4 |
| TTM stretch vs typical wave (1 = median full stretch; + = momentum your way, - = against) <= 0.143 | 40% | +1.4 | **+0.2** | +1.3 | +0.5 | +1.6 | -0.1 | 3/4 | 2/4 |
| Vix Fix spike level AGAINST you (1 = spike line) <= 0.531 | 20% | +1.4 | **+0.9** | +1.7 | +1.0 | +1.1 | +0.9 | 4/4 | 3/4 |
| TTM momentum size (ATR, + = your way) <= -0.366 | 20% | +1.4 | **+0.4** | +1.6 | +0.7 | +1.1 | +0.1 | 4/4 | 3/4 |
| 1m trend = agrees | 44% | +1.4 | **-0.2** | +1.5 | +0.5 | +1.2 | -0.8 | 3/4 | 1/4 |
| 3m trend = disagrees | 31% | +1.3 | **-0.0** | +1.1 | +0.7 | +1.5 | -0.7 | 3/4 | 2/4 |
| 2m trend = disagrees | 24% | +1.3 | **-0.3** | +0.7 | -0.3 | +1.9 | -0.4 | 2/4 | 1/4 |
| 5m trend = agrees | 45% | +1.3 | **-0.1** | +1.3 | +0.0 | +1.3 | -0.2 | 3/4 | 1/4 |
| TTM momentum size (ATR, + = your way) <= 0.894 | 60% | +1.3 | **+0.2** | +1.2 | +0.7 | +1.4 | -0.3 | 3/4 | 2/4 |
| 30m trend = agrees | 51% | +1.3 | **+0.3** | +0.5 | +1.0 | +2.1 | -0.3 | 3/4 | 4/4 |
| TTM stretch vs typical wave (1 = median full stretch; + = momentum your way, - = against) <= 0.403 | 60% | +1.3 | **+0.2** | +1.2 | +0.7 | +1.3 | -0.3 | 3/4 | 2/4 |
| Vix Fix raw number YOUR way <= 0.052 | 20% | +1.2 | **-0.7** | +0.7 | -0.3 | +2.1 | -1.4 | 2/4 | 1/4 |
| TTM wave age (bars since momentum crossed zero) <= 9 | 62% | +1.2 | **+0.1** | +0.8 | +0.8 | +1.7 | -0.6 | 3/4 | 3/4 |
| Vix Fix spike level AGAINST you (1 = spike line) <= 1.165 | 80% | +1.2 | **+0.1** | +1.3 | +0.6 | +1.0 | -0.3 | 3/4 | 3/4 |
| Vix Fix spike level YOUR way (fear before long / greed before short; 1 = spike line) >= 0.205 | 80% | +1.2 | **-0.0** | +1.0 | +0.4 | +1.4 | -0.4 | 3/4 | 2/4 |
| Candles since a Vix Fix spike YOUR way <= 9 | 42% | +1.2 | **+0.1** | +0.8 | +0.5 | +1.5 | -0.4 | 3/4 | 2/4 |
| Vix Fix raw number YOUR way >= 0.272 | 20% | +1.1 | **+0.8** | +0.8 | -0.3 | +1.3 | +1.4 | 3/4 | 2/4 |
| TTM momentum size (ATR, + = your way) <= 1.566 | 80% | +1.1 | **+0.1** | +1.0 | +0.6 | +1.2 | -0.5 | 3/4 | 1/4 |
| 1h trend = agrees | 51% | +1.1 | **+0.4** | +0.6 | +0.5 | +1.7 | +0.2 | 4/4 | 3/4 |
| TTM momentum slope (ATR, + = turning your way) <= 0.24 | 60% | +1.1 | **-0.2** | +0.9 | +0.5 | +1.4 | -0.8 | 3/4 | 2/4 |
| TTM momentum crossed zero your way in last 3 bars = no | 83% | +1.1 | **+0.0** | +1.2 | +0.6 | +1.1 | -0.6 | 3/4 | 2/4 |
| Vix Fix raw number YOUR way >= 0.156 | 40% | +1.1 | **-0.2** | +0.8 | -0.3 | +1.4 | -0.1 | 2/4 | 2/4 |
| TTM wave age (bars since momentum crossed zero) >= 5 | 63% | +1.1 | **-0.0** | +1.2 | +0.4 | +1.0 | -0.4 | 3/4 | 2/4 |
| Vix Fix spike level YOUR way (fear before long / greed before short; 1 = spike line) >= 0.827 | 20% | +1.1 | **-0.1** | +1.3 | -0.6 | +0.9 | +0.4 | 3/4 | 2/4 |
| TTM stretch vs typical wave (1 = median full stretch; + = momentum your way, - = against) <= 0.709 | 80% | +1.1 | **-0.1** | +1.0 | +0.5 | +1.2 | -0.7 | 3/4 | 1/4 |
| TTM wave age (bars since momentum crossed zero) >= 2 | 84% | +1.1 | **+0.1** | +1.2 | +0.8 | +1.0 | -0.6 | 3/4 | 4/4 |
| Vix Fix spike level YOUR way (fear before long / greed before short; 1 = spike line) <= 0.567 | 60% | +1.1 | **-0.0** | +0.9 | +0.5 | +1.3 | -0.5 | 3/4 | 2/4 |
| Vix Fix raw number YOUR way <= 0.094 | 40% | +1.1 | **+0.2** | +1.2 | +0.9 | +0.9 | -0.9 | 3/4 | 1/4 |
| Candles since a Vix Fix spike YOUR way >= 17 | 40% | +1.1 | **-0.4** | +0.9 | +0.2 | +1.3 | -0.9 | 3/4 | 0/4 |
| 15m trend = agrees | 51% | +1.1 | **+0.9** | +0.5 | +1.3 | +1.7 | +0.5 | 4/4 | 4/4 |
| TTM wave age (bars since momentum crossed zero) <= 14 | 80% | +1.1 | **-0.0** | +0.8 | +0.5 | +1.4 | -0.6 | 3/4 | 2/4 |
| Vix Fix spike level AGAINST you (1 = spike line) <= 0.966 | 60% | +1.1 | **-0.3** | +1.0 | +0.5 | +1.1 | -1.1 | 3/4 | 1/4 |
| TTM wave age (bars since momentum crossed zero) <= 5 | 43% | +1.1 | **+0.4** | +0.6 | +1.0 | +1.6 | -0.4 | 3/4 | 3/4 |
| Candles since a Vix Fix spike YOUR way <= 28 | 80% | +1.1 | **+0.1** | +1.0 | +0.6 | +1.2 | -0.4 | 3/4 | 3/4 |
| Vix Fix spike level AGAINST you (1 = spike line) <= 0.77 | 40% | +1.0 | **+0.1** | +1.0 | +0.8 | +1.1 | -0.7 | 3/4 | 2/4 |
| TTM momentum slope (ATR, + = turning your way) <= 0.389 | 80% | +1.0 | **-0.1** | +0.8 | +0.4 | +1.3 | -0.6 | 3/4 | 0/4 |
| TTM momentum slope (ATR, + = turning your way) >= -0.065 | 80% | +1.0 | **+0.1** | +0.8 | +0.7 | +1.2 | -0.5 | 3/4 | 3/4 |
| Vix Fix spike level YOUR way (fear before long / greed before short; 1 = spike line) <= 0.36 | 40% | +1.0 | **+0.8** | +1.0 | +1.3 | +1.1 | +0.2 | 4/4 | 4/4 |
| TTM momentum slope (ATR, + = turning your way) <= 0.1 | 40% | +1.0 | **-0.3** | +1.1 | +0.4 | +1.0 | -1.1 | 3/4 | 1/4 |
| TTM momentum slope (ATR, + = turning your way) >= 0.1 | 60% | +1.0 | **+0.3** | +0.8 | +0.7 | +1.2 | -0.1 | 3/4 | 4/4 |
| Vix Fix spike level YOUR way (fear before long / greed before short; 1 = spike line) >= 0.36 | 60% | +1.0 | **-0.4** | +0.9 | +0.1 | +1.1 | -1.0 | 3/4 | 0/4 |
| Vix Fix spike level AGAINST you (1 = spike line) >= 0.77 | 60% | +1.0 | **+0.0** | +0.9 | +0.4 | +1.1 | -0.4 | 3/4 | 2/4 |
| Vix Fix spike level YOUR way (fear before long / greed before short; 1 = spike line) <= 0.827 | 80% | +1.0 | **+0.1** | +0.8 | +0.9 | +1.1 | -0.7 | 3/4 | 2/4 |
| TTM turn in the last 2 bars = no fresh turn | 81% | +1.0 | **+0.0** | +1.0 | +0.6 | +0.9 | -0.5 | 3/4 | 2/4 |
| Vix Fix raw number YOUR way <= 0.272 | 80% | +1.0 | **-0.1** | +0.9 | +0.6 | +1.0 | -0.9 | 3/4 | 1/4 |
| Vix Fix raw number YOUR way >= 0.052 | 80% | +1.0 | **+0.3** | +1.0 | +1.0 | +0.9 | -0.2 | 3/4 | 3/4 |
| Vix Fix raw number YOUR way >= 0.094 | 60% | +1.0 | **-0.1** | +0.7 | +0.1 | +1.2 | -0.2 | 3/4 | 2/4 |
| TTM wave age (bars since momentum crossed zero) >= 9 | 42% | +0.9 | **-0.1** | +1.3 | +0.2 | +0.6 | -0.4 | 3/4 | 2/4 |
| Vix Fix raw number YOUR way <= 0.156 | 60% | +0.9 | **+0.2** | +1.0 | +0.8 | +0.8 | -0.7 | 3/4 | 3/4 |
| Candles since a Vix Fix spike YOUR way <= 17 | 62% | +0.9 | **+0.3** | +0.9 | +0.7 | +1.0 | -0.2 | 3/4 | 4/4 |
| 15m trend = disagrees | 49% | +0.9 | **-0.8** | +1.3 | -0.1 | +0.5 | -1.5 | 2/4 | 0/4 |
| Candles since a Vix Fix spike YOUR way >= 9 | 61% | +0.9 | **-0.0** | +1.0 | +0.7 | +0.9 | -0.8 | 3/4 | 2/4 |
| TTM momentum slope (ATR, + = turning your way) <= -0.065 | 20% | +0.9 | **-0.1** | +1.3 | +0.1 | +0.5 | -0.4 | 3/4 | 1/4 |
| TTM momentum size (ATR, + = your way) >= -0.366 | 80% | +0.9 | **-0.0** | +0.8 | +0.5 | +1.1 | -0.6 | 3/4 | 1/4 |
| Vix Fix spike level AGAINST you (1 = spike line) >= 0.531 | 80% | +0.9 | **-0.2** | +0.7 | +0.5 | +1.1 | -0.8 | 3/4 | 0/4 |
| TTM momentum slope (ATR, + = turning your way) >= 0.389 | 20% | +0.9 | **+0.7** | +1.4 | +1.5 | +0.5 | -0.0 | 3/4 | 3/4 |
| 3m trend = agrees | 49% | +0.9 | **+0.1** | +1.0 | +0.7 | +0.8 | -0.4 | 3/4 | 1/4 |
| Vix Fix spike level AGAINST you (1 = spike line) >= 0.966 | 40% | +0.9 | **+0.6** | +0.8 | +0.7 | +1.0 | +0.5 | 4/4 | 4/4 |
| TTM stretch vs typical wave (1 = median full stretch; + = momentum your way, - = against) >= -0.166 | 80% | +0.9 | **-0.1** | +0.7 | +0.5 | +1.0 | -0.7 | 3/4 | 1/4 |
| 1h trend = disagrees | 49% | +0.9 | **-0.3** | +1.3 | +0.7 | +0.4 | -1.2 | 3/4 | 1/4 |
| Vix Fix spike level YOUR way (fear before long / greed before short; 1 = spike line) >= 0.567 | 40% | +0.9 | **+0.2** | +1.0 | +0.7 | +0.8 | -0.5 | 3/4 | 2/4 |
| Candles since a Vix Fix spike YOUR way >= 28 | 21% | +0.9 | **-0.3** | +1.0 | +0.3 | +0.7 | -0.9 | 3/4 | 1/4 |
| Candles since a Vix Fix spike YOUR way >= 3 | 81% | +0.9 | **+0.1** | +0.8 | +0.6 | +0.9 | -0.4 | 3/4 | 2/4 |
| TTM momentum slope (ATR, + = turning your way) >= 0.24 | 40% | +0.8 | **+0.4** | +0.9 | +0.7 | +0.7 | +0.0 | 4/4 | 3/4 |
| 5m trend = disagrees | 41% | +0.8 | **+0.1** | +0.3 | +1.3 | +1.3 | -1.2 | 3/4 | 1/4 |
| 30m trend = disagrees | 49% | +0.8 | **-0.3** | +1.4 | +0.1 | +0.0 | -0.7 | 3/4 | 1/4 |
| TTM stretch vs typical wave (1 = median full stretch; + = momentum your way, - = against) >= 0.143 | 60% | +0.7 | **-0.1** | +0.7 | +0.7 | +0.8 | -0.8 | 3/4 | 2/4 |
| TTM momentum size (ATR, + = your way) >= 0.315 | 60% | +0.7 | **-0.1** | +0.6 | +0.6 | +0.8 | -0.8 | 3/4 | 2/4 |
| 2m trend = agrees | 50% | +0.7 | **+0.3** | +0.7 | +1.0 | +0.8 | -0.5 | 3/4 | 2/4 |
| TTM squeeze = fired 0-3 bars ago | 13% | +0.7 | **+0.8** | +0.1 | +1.9 | +1.4 | -0.5 | 3/4 | 2/4 |
| TTM wave age (bars since momentum crossed zero) >= 14 | 23% | +0.7 | **+0.0** | +1.1 | +0.2 | +0.2 | -0.1 | 3/4 | 2/4 |
| TTM wave age (bars since momentum crossed zero) <= 2 | 24% | +0.7 | **+0.1** | -0.3 | +0.3 | +1.7 | -0.1 | 2/4 | 2/4 |
| TTM stretch vs typical wave (1 = median full stretch; + = momentum your way, - = against) >= 0.403 | 40% | +0.7 | **-0.2** | +0.6 | +0.4 | +0.8 | -0.7 | 3/4 | 1/4 |
| TTM stretch vs typical wave (1 = median full stretch; + = momentum your way, - = against) >= 0.709 | 20% | +0.6 | **+0.5** | +0.5 | +0.9 | +0.7 | +0.1 | 4/4 | 3/4 |
| TTM momentum color (vs your trade) = with you + rising (cyan for longs) | 53% | +0.6 | **+0.1** | +0.3 | +0.7 | +1.0 | -0.5 | 3/4 | 2/4 |
| TTM momentum color (vs your trade) = with you + fading (blue for longs) | 17% | +0.6 | **-0.8** | +1.1 | +0.0 | +0.1 | -1.6 | 3/4 | 1/4 |
| TTM momentum size (ATR, + = your way) >= 0.894 | 40% | +0.6 | **-0.2** | +0.6 | +0.3 | +0.6 | -0.7 | 3/4 | 1/4 |
| TTM momentum size (ATR, + = your way) >= 1.566 | 20% | +0.5 | **+0.0** | +0.5 | +0.3 | +0.5 | -0.3 | 3/4 | 2/4 |
| TTM momentum crossed zero your way in last 3 bars = yes | 17% | +0.5 | **+0.1** | -0.3 | +0.4 | +1.2 | -0.1 | 2/4 | 1/4 |
| TTM squeeze = no squeeze in 10+ bars | 47% | +0.3 | **-0.1** | +0.4 | +0.9 | +0.2 | -1.0 | 3/4 | 1/4 |
| Vix Fix spike level YOUR way (fear before long / greed before short; 1 = spike line) <= 0.205 | 20% | +0.3 | **+0.3** | +0.7 | +1.5 | -0.1 | -0.8 | 2/4 | 2/4 |
| Vix Fix spike level AGAINST you (1 = spike line) >= 1.165 | 20% | +0.3 | **-0.3** | -0.8 | +0.5 | +1.3 | -1.2 | 2/4 | 1/4 |
| 1m trend = disagrees | 16% | +0.1 | **+0.5** | +0.5 | -0.2 | -0.4 | +1.3 | 2/4 | 1/4 |

### Line turns GREEN (long) / RED (short) - FADED (event alone: TRAIN -1.0, TEST -0.0)
| Condition | Share kept | TRAIN edge | TEST edge | Edge per cell | Cells > 0 | Charts OK |
|---|---|---|---|---|---|---|
| Yesterday's range (daily ATR; low = quiet day) >= 1.155 | 20% | +0.2 | **-0.6** | -1.0 | -1.9 | +1.4 | +0.8 | 2/4 | 0/4 |
| 1m trend = agrees | 16% | -0.1 | **-0.5** | -0.5 | +0.2 | +0.4 | -1.3 | 2/4 | 0/4 |
| Vix Fix spike level YOUR way (fear before long / greed before short; 1 = spike line) >= 1.165 | 20% | -0.3 | **+0.3** | +0.8 | -0.5 | -1.3 | +1.2 | 2/4 | 1/4 |
| Vix Fix spike level AGAINST you (1 = spike line) <= 0.205 | 20% | -0.3 | **-0.3** | -0.7 | -1.5 | +0.1 | +0.8 | 2/4 | 0/4 |
| TTM squeeze = no squeeze in 10+ bars | 47% | -0.3 | **+0.1** | -0.4 | -0.9 | -0.2 | +1.0 | 1/4 | 1/4 |
| VIX FIX pane bar AGAINST you (0-100) <= 13.984 | 20% | -0.3 | **+0.3** | -0.5 | -0.7 | -0.2 | +1.2 | 1/4 | 1/4 |
| Volatility now vs normal (ATR ratio) >= 1.887 | 20% | -0.4 | **-0.9** | -0.7 | -2.0 | -0.1 | +0.0 | 1/4 | 0/4 |
| TTM momentum size (ATR, + = your way) <= -1.566 | 20% | -0.5 | **+0.0** | -0.5 | -0.3 | -0.5 | +0.3 | 1/4 | 0/4 |
| Volatility now vs normal (ATR ratio) >= 1.522 | 40% | -0.5 | **-0.4** | -0.4 | -0.9 | -0.6 | -0.0 | 0/4 | 0/4 |
| Signal candle body (ATR, + = your way) >= -0.503 | 40% | -0.6 | **-0.1** | -0.6 | -0.2 | -0.6 | -0.0 | 0/4 | 0/4 |
| Distance from VWAP (ATR, + = your side) >= -0.519 | 40% | -0.6 | **-0.5** | -0.5 | -0.9 | -0.6 | +0.0 | 1/4 | 0/4 |
| Fast-slow EMA gap (ATR, + = your way) <= -0.451 | 20% | -0.6 | **-1.0** | -0.6 | -1.6 | -0.6 | -0.4 | 0/4 | 0/4 |
| Slow EMA 34 slope (ATR per 5 bars, + = your way) <= -0.116 | 60% | -0.6 | **-0.1** | -0.6 | -0.8 | -0.6 | +0.6 | 1/4 | 1/4 |
| TTM momentum size (ATR, + = your way) <= -0.894 | 40% | -0.6 | **+0.2** | -0.6 | -0.3 | -0.6 | +0.7 | 1/4 | 0/4 |
| TTM momentum color (vs your trade) = against you + turning (yellow for longs) | 17% | -0.6 | **+0.8** | -1.1 | -0.0 | -0.1 | +1.6 | 1/4 | 3/4 |

### RED or PINK ends -> long / GREEN or BLUE ends -> short (event alone: TRAIN +0.3, TEST +0.7)
| Condition | Share kept | TRAIN edge | TEST edge | Edge per cell | Cells > 0 | Charts OK |
|---|---|---|---|---|---|---|
| Yesterday's range (daily ATR; low = quiet day) >= 1.155 | 20% | +1.7 | **+1.4** | +1.8 | +2.3 | +1.6 | +0.6 | 4/4 | 3/4 |
| Distance from VWAP (ATR, + = your side) >= 0.584 | 20% | +1.5 | **+1.3** | +0.5 | +1.3 | +2.7 | +1.3 | 4/4 | 2/4 |
| 5m trend = agrees | 25% | +1.5 | **+1.3** | +1.5 | -0.7 | +1.5 | +3.3 | 3/4 | 2/4 |
| Length of the previous color run (bars) <= 2 | 30% | +1.4 | **-0.0** | +0.7 | +0.1 | +2.2 | -0.2 | 3/4 | 2/4 |
| VIX FIX pane bar AGAINST you (0-100) <= 32.426 | 20% | +1.4 | **+1.3** | +0.9 | +0.2 | +1.9 | +2.3 | 4/4 | 2/4 |
| 30m trend = agrees | 46% | +1.3 | **+0.8** | +0.1 | +1.2 | +2.7 | +0.4 | 4/4 | 2/4 |
| Length of the previous color run (bars) <= 4 | 42% | +1.3 | **+0.4** | +0.6 | +0.4 | +2.0 | +0.3 | 4/4 | 2/4 |
| 15m trend = agrees | 41% | +1.2 | **+1.3** | +0.1 | +0.9 | +2.2 | +1.6 | 4/4 | 2/4 |
| Opening gap (daily ATR, + = your way) >= 0.301 | 20% | +1.1 | **+1.5** | +0.9 | +1.6 | +1.4 | +1.4 | 4/4 | 2/4 |
| Vix Fix raw number YOUR way >= 0.355 | 20% | +1.1 | **-0.6** | +0.2 | -1.8 | +1.6 | -0.1 | 2/4 | 0/4 |
| Day's move so far (daily ATR, + = your way) >= 0.115 | 20% | +1.1 | **+1.7** | +0.6 | +0.6 | +1.6 | +2.8 | 4/4 | 3/4 |
| 3m trend = agrees | 18% | +1.1 | **+1.2** | +0.9 | +0.7 | +1.3 | +1.7 | 4/4 | 2/4 |
| Volatility now vs normal (ATR ratio) >= 1.876 | 20% | +1.1 | **+0.8** | +0.7 | +1.7 | +1.4 | +0.1 | 4/4 | 2/4 |
| Vix Fix spike level AGAINST you (1 = spike line) <= 0.559 | 20% | +1.0 | **+1.0** | +0.3 | +0.7 | +1.8 | +1.4 | 4/4 | 3/4 |
| TTM squeeze = in squeeze | 27% | +1.0 | **+1.0** | +0.5 | +1.5 | +1.6 | +0.5 | 4/4 | 2/4 |

### RED or PINK ends -> long / GREEN or BLUE ends -> short - FADED (event alone: TRAIN -0.3, TEST -0.7)
| Condition | Share kept | TRAIN edge | TEST edge | Edge per cell | Cells > 0 | Charts OK |
|---|---|---|---|---|---|---|
| Day's move so far (daily ATR, + = your way) >= 0.191 | 20% | +1.7 | **+0.2** | +2.4 | -0.5 | +1.0 | +0.8 | 3/4 | 3/4 |
| Distance from VWAP (ATR, + = your side) >= 0.557 | 20% | +1.5 | **-0.3** | +2.1 | -0.8 | +1.0 | +0.2 | 3/4 | 2/4 |
| Length of the previous color run (bars) >= 31 | 20% | +1.3 | **-0.1** | +2.1 | -0.7 | +0.5 | +0.5 | 3/4 | 1/4 |
| VIX FIX pane bar AGAINST you (0-100) <= 15.791 | 20% | +1.3 | **-0.5** | +2.4 | -0.9 | +0.2 | -0.2 | 2/4 | 3/4 |
| Slow EMA 34 slope (ATR per 5 bars, + = your way) <= -0.135 | 20% | +1.3 | **-0.4** | +1.6 | -0.8 | +0.9 | +0.0 | 2/4 | 1/4 |
| TTM momentum slope (ATR, + = turning your way) <= -0.404 | 20% | +1.1 | **-1.5** | +1.7 | -1.1 | +0.4 | -1.9 | 2/4 | 1/4 |
| Vix Fix spike level YOUR way (fear before long / greed before short; 1 = spike line) >= 1.176 | 20% | +1.0 | **-0.6** | +2.3 | -1.0 | -0.4 | -0.2 | 1/4 | 2/4 |
| TTM momentum size (ATR, + = your way) <= -1.074 | 20% | +0.9 | **+0.1** | +1.3 | -0.5 | +0.5 | +0.7 | 3/4 | 1/4 |
| TTM stretch vs typical wave (1 = median full stretch; + = momentum your way, - = against) <= -0.486 | 20% | +0.8 | **+0.2** | +1.2 | -0.7 | +0.5 | +1.0 | 3/4 | 1/4 |
| VIX FIX pane bar YOUR way (0-100 as on your pane; red fear for longs, blue greed for shorts) >= 95.989 | 20% | +0.7 | **-0.4** | +2.4 | -1.2 | -0.9 | +0.3 | 2/4 | 1/4 |
| Length of the previous color run (bars) >= 11 | 41% | +0.7 | **-0.6** | +1.4 | -0.9 | -0.0 | -0.4 | 1/4 | 1/4 |
| Opening gap (daily ATR, + = your way) >= 0.341 | 20% | +0.7 | **-0.7** | +1.7 | -1.8 | -0.5 | +0.3 | 2/4 | 0/4 |
| Vix Fix spike level AGAINST you (1 = spike line) <= 0.229 | 20% | +0.6 | **-0.9** | +1.2 | -1.4 | +0.0 | -0.4 | 2/4 | 1/4 |
| 30m trend = agrees | 54% | +0.6 | **-0.5** | +0.6 | -0.3 | +0.6 | -0.7 | 2/4 | 1/4 |
| Vix Fix spike level YOUR way (fear before long / greed before short; 1 = spike line) >= 0.988 | 40% | +0.6 | **-0.9** | +1.2 | -0.9 | -0.1 | -0.9 | 1/4 | 2/4 |

### PINK appears -> long / BLUE appears -> short (event alone: TRAIN -1.0, TEST -0.1)
| Condition | Share kept | TRAIN edge | TEST edge | Edge per cell | Cells > 0 | Charts OK |
|---|---|---|---|---|---|---|
| TTM squeeze = fired 4-10 bars ago | 11% | +1.4 | **+1.4** | +1.3 | +0.5 | +1.6 | +2.4 | 4/4 | 2/4 |
| Fast-slow EMA gap (ATR, + = your way) >= -0.339 | 20% | +0.8 | **+0.4** | +0.7 | +0.2 | +1.0 | +0.5 | 4/4 | 3/4 |
| TTM momentum slope (ATR, + = turning your way) <= 0.212 | 40% | +0.7 | **+0.8** | +1.0 | +0.5 | +0.5 | +1.1 | 4/4 | 3/4 |
| TTM momentum slope (ATR, + = turning your way) <= 0.092 | 20% | +0.6 | **+0.2** | +0.6 | +0.5 | +0.7 | +0.0 | 4/4 | 2/4 |
| Distance from VWAP (ATR, + = your side) >= -0.887 | 20% | +0.5 | **+0.6** | +0.8 | +0.4 | +0.1 | +0.8 | 4/4 | 4/4 |
| TTM squeeze = in squeeze | 35% | +0.5 | **+1.0** | +0.7 | +0.5 | +0.2 | +1.4 | 4/4 | 2/4 |
| Fast-slow EMA gap (ATR, + = your way) >= -0.586 | 40% | +0.4 | **+0.6** | +0.4 | +0.0 | +0.5 | +1.1 | 4/4 | 3/4 |
| TTM momentum slope (ATR, + = turning your way) <= 0.311 | 60% | +0.4 | **+0.6** | +0.2 | +0.0 | +0.5 | +1.2 | 4/4 | 2/4 |
| Slow EMA 34 slope (ATR per 5 bars, + = your way) >= -0.124 | 20% | +0.3 | **+0.5** | +0.4 | -0.2 | +0.1 | +1.3 | 3/4 | 2/4 |
| Fast-slow EMA gap (ATR, + = your way) >= -0.834 | 60% | +0.2 | **+0.8** | +0.2 | +0.1 | +0.2 | +1.4 | 4/4 | 3/4 |
| 30m trend = agrees | 35% | +0.2 | **+0.4** | +0.1 | -0.2 | +0.3 | +1.1 | 3/4 | 3/4 |
| Yesterday's range (daily ATR; low = quiet day) >= 1.145 | 20% | +0.2 | **+1.5** | +0.1 | +1.7 | +0.2 | +1.2 | 4/4 | 1/4 |
| TTM wave age (bars since momentum crossed zero) <= 10 | 43% | +0.1 | **+0.3** | +0.3 | -0.1 | -0.0 | +0.7 | 2/4 | 2/4 |
| 15m trend = agrees | 24% | +0.1 | **+0.6** | -0.9 | +0.3 | +1.3 | +0.8 | 3/4 | 3/4 |
| TTM momentum size (ATR, + = your way) >= -0.276 | 40% | +0.1 | **+0.1** | +0.4 | +0.2 | -0.2 | -0.1 | 2/4 | 1/4 |

### PINK appears -> long / BLUE appears -> short - FADED (event alone: TRAIN +1.0, TEST +0.1)
| Condition | Share kept | TRAIN edge | TEST edge | Edge per cell | Cells > 0 | Charts OK |
|---|---|---|---|---|---|---|
| Fast-slow EMA gap (ATR, + = your way) >= 1.152 | 20% | +4.6 | **+1.4** | +5.1 | +2.2 | +4.1 | +0.7 | 4/4 | 2/4 |
| TTM momentum slope (ATR, + = turning your way) <= -0.421 | 20% | +4.5 | **+1.3** | +5.0 | +2.1 | +4.0 | +0.5 | 4/4 | 3/4 |
| Slow EMA 34 slope (ATR per 5 bars, + = your way) >= 0.468 | 20% | +4.0 | **+0.7** | +4.5 | +1.0 | +3.6 | +0.3 | 4/4 | 2/4 |
| TTM momentum size (ATR, + = your way) >= 1.409 | 20% | +3.2 | **-0.5** | +3.0 | +0.2 | +3.4 | -1.1 | 3/4 | 2/4 |
| TTM stretch vs typical wave (1 = median full stretch; + = momentum your way, - = against) >= 0.63 | 20% | +3.1 | **-0.4** | +2.9 | +0.3 | +3.3 | -1.1 | 3/4 | 2/4 |
| TTM momentum slope (ATR, + = turning your way) <= -0.311 | 40% | +3.0 | **+1.2** | +3.1 | +1.8 | +3.0 | +0.7 | 4/4 | 3/4 |
| Vix Fix spike level YOUR way (fear before long / greed before short; 1 = spike line) >= 1.122 | 20% | +3.0 | **+0.4** | +3.2 | +0.9 | +2.8 | -0.2 | 3/4 | 2/4 |
| Fast-slow EMA gap (ATR, + = your way) >= 0.834 | 40% | +2.8 | **+1.4** | +3.1 | +1.9 | +2.6 | +1.0 | 4/4 | 3/4 |
| TTM squeeze = no squeeze in 10+ bars | 51% | +2.6 | **+1.2** | +2.9 | +1.9 | +2.3 | +0.6 | 4/4 | 4/4 |
| Slow EMA 34 slope (ATR per 5 bars, + = your way) >= 0.335 | 40% | +2.5 | **+0.9** | +2.6 | +1.4 | +2.5 | +0.4 | 4/4 | 3/4 |
| TTM momentum size (ATR, + = your way) >= 0.813 | 40% | +2.5 | **-0.0** | +2.8 | +1.0 | +2.2 | -1.0 | 3/4 | 1/4 |
| Opening gap (daily ATR, + = your way) >= 0.121 | 40% | +2.5 | **+0.3** | +2.3 | +0.8 | +2.7 | -0.1 | 3/4 | 3/4 |
| TTM stretch vs typical wave (1 = median full stretch; + = momentum your way, - = against) >= 0.362 | 40% | +2.5 | **-0.1** | +2.8 | +0.8 | +2.1 | -0.9 | 3/4 | 2/4 |
| Candles since a Vix Fix spike YOUR way <= 0 | 35% | +2.3 | **+0.9** | +2.5 | +1.7 | +2.2 | +0.1 | 4/4 | 3/4 |
| Candles since a Vix Fix spike YOUR way <= 3 | 41% | +2.3 | **+0.8** | +2.5 | +1.7 | +2.2 | -0.1 | 3/4 | 3/4 |

### Strong color returns after a warning (event alone: TRAIN +0.6, TEST -0.5)
| Condition | Share kept | TRAIN edge | TEST edge | Edge per cell | Cells > 0 | Charts OK |
|---|---|---|---|---|---|---|
| VIX FIX pane bar AGAINST you (0-100) <= 19.629 | 20% | +2.5 | **-1.1** | +3.8 | -2.1 | +1.3 | -0.3 | 2/4 | 0/4 |
| Signal candle body (ATR, + = your way) >= 1.018 | 20% | +2.2 | **-0.0** | +2.4 | -0.4 | +1.9 | +0.4 | 3/4 | 2/4 |
| TTM turn in the last 2 bars = turned YOUR way (red>yellow before a long) | 23% | +2.0 | **-0.8** | +2.8 | -1.0 | +1.3 | -0.6 | 2/4 | 1/4 |
| TTM squeeze = in squeeze | 40% | +1.8 | **+0.1** | +2.1 | +0.2 | +1.5 | +0.1 | 4/4 | 1/4 |
| TTM momentum color (vs your trade) = against you + turning (yellow for longs) | 25% | +1.8 | **-0.5** | +2.4 | -0.8 | +1.2 | -0.2 | 2/4 | 1/4 |
| Distance from VWAP (ATR, + = your side) >= 6.924 | 20% | +1.8 | **-2.3** | +2.2 | -2.3 | +1.4 | -2.3 | 2/4 | 0/4 |
| Opening gap (daily ATR, + = your way) <= -0.297 | 20% | +1.7 | **-1.6** | +2.2 | -2.4 | +1.1 | -0.9 | 2/4 | 0/4 |
| VIX FIX pane bar AGAINST you (0-100) <= 27.307 | 40% | +1.6 | **-0.2** | +2.3 | -0.7 | +1.0 | +0.2 | 3/4 | 1/4 |
| Distance from VWAP (ATR, + = your side) >= 4.273 | 40% | +1.6 | **-1.2** | +1.6 | -1.7 | +1.5 | -0.7 | 2/4 | 0/4 |
| TTM momentum slope (ATR, + = turning your way) >= -0.016 | 40% | +1.5 | **+0.2** | +2.3 | +0.3 | +0.7 | +0.1 | 4/4 | 2/4 |
| Length of the current color run (bars) >= 63 | 20% | +1.4 | **-1.0** | +1.7 | -1.1 | +1.1 | -0.8 | 2/4 | 0/4 |
| Signal candle body (ATR, + = your way) >= 0.769 | 40% | +1.4 | **-0.4** | +2.0 | -0.2 | +0.8 | -0.6 | 2/4 | 1/4 |
| Length of the current color run (bars) >= 40 | 41% | +1.4 | **-0.6** | +1.7 | -0.9 | +1.1 | -0.4 | 2/4 | 1/4 |
| TTM momentum slope (ATR, + = turning your way) >= 0.095 | 20% | +1.4 | **+0.6** | +1.4 | +0.6 | +1.3 | +0.6 | 4/4 | 2/4 |
| Volatility now vs normal (ATR ratio) <= 0.911 | 20% | +1.3 | **-1.6** | +0.9 | -1.4 | +1.8 | -1.8 | 2/4 | 0/4 |

### Strong color returns after a warning - FADED (event alone: TRAIN -0.6, TEST +0.5)
| Condition | Share kept | TRAIN edge | TEST edge | Edge per cell | Cells > 0 | Charts OK |
|---|---|---|---|---|---|---|
| Length of the current color run (bars) <= 16 | 22% | +0.9 | **+0.8** | +0.5 | -0.6 | +1.3 | +2.3 | 3/4 | 2/4 |
| Day's move so far (daily ATR, + = your way) >= -0.073 | 20% | +0.8 | **+1.1** | +1.4 | -0.2 | +0.1 | +2.5 | 3/4 | 3/4 |
| Distance from VWAP (ATR, + = your side) >= -1.576 | 20% | +0.7 | **+0.7** | +1.3 | +0.0 | +0.1 | +1.4 | 4/4 | 2/4 |
| Yesterday's range (daily ATR; low = quiet day) >= 1.138 | 20% | +0.7 | **+1.7** | -0.5 | +1.2 | +2.0 | +2.2 | 3/4 | 3/4 |
| TTM wave age (bars since momentum crossed zero) >= 22 | 20% | +0.7 | **+0.4** | +0.5 | -0.2 | +0.9 | +1.1 | 3/4 | 2/4 |
| TTM squeeze = no squeeze in 10+ bars | 47% | +0.6 | **+1.1** | +0.5 | +0.6 | +0.6 | +1.6 | 4/4 | 3/4 |
| Distance from VWAP (ATR, + = your side) >= -2.679 | 40% | +0.6 | **+0.3** | +0.5 | -0.1 | +0.6 | +0.7 | 3/4 | 2/4 |
| Vix Fix raw number YOUR way >= 0.308 | 20% | +0.6 | **+0.4** | +0.6 | -1.0 | +0.5 | +1.0 | 3/4 | 2/4 |
| Length of the current color run (bars) <= 27 | 41% | +0.4 | **+0.5** | +0.3 | +0.1 | +0.5 | +1.0 | 4/4 | 3/4 |
| 1m trend = agrees | 27% | +0.3 | **+2.0** | +0.2 | +1.8 | +0.4 | +2.3 | 4/4 | 2/4 |
| VIX FIX pane bar YOUR way (0-100 as on your pane; red fear for longs, blue greed for shorts) >= 51.205 | 20% | +0.3 | **+0.4** | +0.2 | -0.8 | +0.3 | +1.7 | 3/4 | 2/4 |
| TTM momentum slope (ATR, + = turning your way) >= 0.112 | 40% | +0.2 | **+0.6** | +0.2 | +0.5 | +0.3 | +0.7 | 4/4 | 2/4 |
| Signal candle body (ATR, + = your way) >= -0.581 | 40% | +0.2 | **+0.8** | +0.1 | +0.8 | +0.2 | +0.9 | 4/4 | 2/4 |
| TTM momentum color (vs your trade) = against you + turning (yellow for longs) | 37% | +0.2 | **+0.6** | +0.3 | +0.2 | +0.0 | +0.9 | 4/4 | 2/4 |
| Day's move so far (daily ATR, + = your way) >= -0.204 | 40% | +0.2 | **+0.3** | -0.1 | -0.7 | +0.5 | +1.4 | 2/4 | 2/4 |

## 5. Exits (ATR per trade; entry at the next open; 3 ATR safety stop; flat 15:55)
Columns = SPY 2020-2023 | SPY 2024-now | QQQ 2020-2023 | QQQ 2024-now. Compare rows within a table.
### Line turns green/red (no filter) (95,133 trades)
| Exit | SPY 2020-2023 | SPY 2024-now | QQQ 2020-2023 | QQQ 2024-now | Avg |
|---|---|---|---|---|---|
| Hold to 15:55 | +0.133 | +0.069 | +0.155 | -0.002 | **+0.089** |
| Opposite color starts | +0.109 | +0.107 | +0.145 | -0.037 | **+0.081** |
| Line leaves your color | +0.088 | +0.087 | +0.088 | +0.035 | **+0.074** |
| Time 30 candles | +0.057 | +0.073 | +0.053 | -0.009 | **+0.044** |
| TTM momentum crosses zero against you | +0.031 | +0.061 | +0.024 | +0.013 | **+0.032** |
| Warning color (blue/pink) or color ends | +0.027 | +0.043 | +0.026 | +0.017 | **+0.028** |
| +2 / -1 ATR bracket | +0.027 | +0.018 | +0.024 | -0.009 | **+0.015** |
| Time 15 candles | +0.019 | +0.024 | +0.019 | -0.014 | **+0.012** |
| TTM momentum peaks (turns against you) | +0.007 | +0.004 | +0.018 | +0.003 | **+0.008** |
| 1 ATR trailing stop (on closes) | +0.001 | +0.013 | +0.015 | -0.014 | **+0.004** |
| Time 10 candles | +0.010 | +0.006 | +0.001 | -0.002 | **+0.004** |
| Time 5 candles | +0.009 | -0.006 | -0.001 | +0.001 | **+0.000** |

### PINK appears -> long / BLUE appears -> short - FADED - best recipe (8,148 trades)
| Exit | SPY 2020-2023 | SPY 2024-now | QQQ 2020-2023 | QQQ 2024-now | Avg |
|---|---|---|---|---|---|
| Hold to 15:55 | +0.566 | +0.258 | +0.473 | +0.171 | **+0.367** |
| Opposite color starts | +0.535 | +0.266 | +0.416 | +0.129 | **+0.336** |
| Line leaves your color | +0.409 | +0.158 | +0.223 | +0.119 | **+0.227** |
| Time 30 candles | +0.312 | +0.219 | +0.183 | +0.097 | **+0.203** |
| Time 15 candles | +0.270 | +0.134 | +0.230 | +0.052 | **+0.172** |
| Time 10 candles | +0.238 | +0.130 | +0.184 | +0.048 | **+0.150** |
| Time 5 candles | +0.162 | +0.130 | +0.139 | +0.039 | **+0.118** |
| +2 / -1 ATR bracket | +0.160 | +0.093 | +0.159 | +0.055 | **+0.117** |
| 1 ATR trailing stop (on closes) | +0.161 | +0.086 | +0.162 | +0.035 | **+0.111** |
| TTM momentum crosses zero against you | +0.147 | +0.065 | +0.097 | +0.061 | **+0.093** |
| TTM momentum peaks (turns against you) | +0.111 | +0.036 | +0.092 | +0.041 | **+0.070** |
| Warning color (blue/pink) or color ends | +0.062 | +0.049 | +0.047 | +0.056 | **+0.053** |

### RED or PINK ends -> long / GREEN or BLUE ends -> short - best recipe (8,922 trades)
| Exit | SPY 2020-2023 | SPY 2024-now | QQQ 2020-2023 | QQQ 2024-now | Avg |
|---|---|---|---|---|---|
| 1 ATR trailing stop (on closes) | +0.074 | +0.088 | +0.108 | -0.083 | **+0.047** |
| Opposite color starts | +0.124 | +0.073 | +0.142 | -0.153 | **+0.047** |
| Line leaves your color | +0.039 | +0.106 | +0.028 | -0.045 | **+0.032** |
| Warning color (blue/pink) or color ends | +0.015 | +0.089 | +0.033 | -0.014 | **+0.031** |
| +2 / -1 ATR bracket | +0.059 | +0.026 | +0.072 | -0.040 | **+0.029** |
| Time 15 candles | +0.074 | +0.094 | +0.061 | -0.142 | **+0.022** |
| TTM momentum peaks (turns against you) | +0.060 | +0.061 | +0.068 | -0.104 | **+0.021** |
| Time 5 candles | +0.041 | +0.028 | +0.066 | -0.055 | **+0.020** |
| Time 10 candles | +0.050 | +0.079 | +0.048 | -0.130 | **+0.012** |
| Time 30 candles | +0.022 | +0.100 | +0.033 | -0.185 | **-0.007** |
| TTM momentum crosses zero against you | -0.005 | +0.075 | +0.006 | -0.115 | **-0.010** |
| Hold to 15:55 | +0.055 | +0.068 | +0.017 | -0.311 | **-0.043** |

### Line turns GREEN (long) / RED (short) - best recipe (9,779 trades)
| Exit | SPY 2020-2023 | SPY 2024-now | QQQ 2020-2023 | QQQ 2024-now | Avg |
|---|---|---|---|---|---|
| Opposite color starts | +0.187 | +0.008 | +0.278 | -0.042 | **+0.108** |
| Line leaves your color | +0.226 | +0.004 | +0.238 | -0.041 | **+0.107** |
| Hold to 15:55 | +0.243 | -0.009 | +0.117 | -0.026 | **+0.081** |
| Time 30 candles | +0.188 | -0.083 | +0.144 | -0.012 | **+0.059** |
| +2 / -1 ATR bracket | +0.087 | -0.024 | +0.135 | +0.005 | **+0.051** |
| Warning color (blue/pink) or color ends | +0.112 | -0.024 | +0.116 | -0.019 | **+0.046** |
| TTM momentum crosses zero against you | +0.110 | -0.005 | +0.058 | +0.022 | **+0.046** |
| Time 10 candles | +0.087 | -0.046 | +0.093 | +0.042 | **+0.044** |
| Time 15 candles | +0.119 | -0.043 | +0.092 | +0.001 | **+0.042** |
| TTM momentum peaks (turns against you) | +0.063 | -0.056 | +0.119 | +0.030 | **+0.039** |
| 1 ATR trailing stop (on closes) | +0.098 | -0.030 | +0.107 | -0.029 | **+0.036** |
| Time 5 candles | +0.055 | -0.030 | +0.044 | +0.017 | **+0.022** |

