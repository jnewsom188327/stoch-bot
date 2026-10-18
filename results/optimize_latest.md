# Trend Flip optimizer + Monte Carlo - 2026-10-18 16:09 ET
Data 2020-01-01 to 2026-10-17, SPY 2m, SPY 3m, QQQ 2m, QQQ 3m. DATA ONLY - no orders.

## The answer in 30 seconds
- Entry idea picked on 2020-2023: **+ 15m and 60m agree**
- Exit idea picked on 2020-2023: **EXIT ride + cut, warning after 3 candles**
- Final setup: **QUIET + + 15m and 60m agree + EXIT ride + cut, warning after 3 candles** - beat QUIET on 2024-now (never seen) on 2/4 charts
- Monte Carlo of the final setup, 1 contract per trade, after $2 costs per trade:
- **SPY 2m** (1DTE): typical year -$814, bad year -$1,946, chance of a losing year 84%, bad-case worst drop -$2,093, chance the edge is real 1%
- **SPY 3m** (1DTE): typical year -$131, bad year -$1,632, chance of a losing year 55%, bad-case worst drop -$1,949, chance the edge is real 42%
- **QQQ 2m** (1DTE): typical year -$696, bad year -$1,926, chance of a losing year 79%, bad-case worst drop -$2,101, chance the edge is real 2%
- **QQQ 3m** (1DTE): typical year -$357, bad year -$2,001, chance of a losing year 63%, bad-case worst drop -$2,252, chance the edge is real 24%

Assumptions: option $ = Black-Scholes estimate for an at-the-money option (theta and gamma included), implied vol from the daily ATR, in today's QQQ, SPY prices, $2 per round trip. Real fills, IV changes and slippage will differ. Quiet day = yesterday's range < 0.7 daily ATR.

## Scoreboard: does the idea beat the quiet-day setup? (4 charts, 1DTE $ per year)
Picked = beats QUIET on TRAIN (2020-2023) on at least 3 of 4 charts. TEST (2024-now) was never used to pick.

| Idea | TRAIN: charts better | TEST: charts better | TRAIN $/yr vs QUIET (avg) | TEST $/yr vs QUIET (avg) | Picked on TRAIN? | Held up on TEST? |
|---|---|---|---|---|---|---|
| + 15m and 60m agree | 4/4 | 0/4 | +$724 | -$274 | ✅ | ❌ no |
| no VWAP rule on the line | 3/4 | 2/4 | +$450 | +$34 | ✅ | ❌ no |
| Vix Fix spike within 5 | 3/4 | 1/4 | +$429 | -$7 | ✅ | ❌ no |
| + 15m agrees | 3/4 | 0/4 | +$293 | -$205 | ✅ | ❌ no |
| EXIT ride + cut, warning after 3 candles | 3/4 | 3/4 | +$223 | -$176 | ✅ | ❌ no |
| EXIT cut losers on warning | 3/4 | 3/4 | +$135 | -$23 | ✅ | ❌ no |
| EXIT stop 1.5 ATR | 3/4 | 2/4 | +$130 | +$98 | ✅ | ❌ no |
| wait up to 10 for a spike | 3/4 | 0/4 | +$103 | -$143 | ✅ | ❌ no |
| no entries after 14:00 | 3/4 | 3/4 | +$92 | +$188 | ✅ | ✅ yes |
| entries from 10:00 | 3/4 | 3/4 | +$91 | +$125 | ✅ | ✅ yes |
| EXIT no stop (flip / time / 15:55 only) | 3/4 | 2/4 | +$57 | -$72 | ✅ | ❌ no |
| EXIT stop 3 ATR | 2/4 | 2/4 | +$16 | -$85 |  |  |
| EXIT hold 25 candles | 3/4 | 0/4 | -$18 | -$149 |  |  |
| EXIT ride strong trend | 2/4 | 2/4 | -$45 | -$334 |  |  |
| EXIT hold 10 candles | 2/4 | 1/4 | -$52 | -$0 |  |  |
| EXIT ride if 15m agrees | 2/4 | 2/4 | -$70 | -$149 |  |  |
| EXIT ride + cut losers | 2/4 | 2/4 | -$76 | -$151 |  |  |
| EXIT hold 20 candles | 2/4 | 2/4 | -$77 | -$112 |  |  |
| no waiting for a late spike (wait 0) | 1/4 | 2/4 | -$105 | -$20 |  |  |
| Vix Fix spike within 20 | 1/4 | 1/4 | -$532 | -$132 |  |  |
| no Vix Fix filter | 0/4 | 0/4 | -$1,498 | -$1,254 |  |  |

## Final setup (picked on TRAIN): **QUIET + + 15m and 60m agree + EXIT ride + cut, warning after 3 candles**
Choices tried (best average TRAIN wins): QUIET only; QUIET + + 15m and 60m agree; QUIET + EXIT ride + cut, warning after 3 candles; QUIET + + 15m and 60m agree + EXIT ride + cut, warning after 3 candles.
TradingView v4.1 settings: Higher timeframes > Entry filter = Both agree | Exit > Exit = Ride + cut losers, and Warning colors > N = 3 (quiet-day filter stays ON).

| Chart | Setup | TRAIN ATR / trade | TEST ATR / trade | TRAIN 1DTE $/yr | TEST 1DTE $/yr | TEST 0DTE $/yr |
|---|---|---|---|---|---|---|
| SPY 2m | v3.0 every day | -0.006 | **+0.009** | -$3,849 | **-$2,028** | -$3,107 |
| SPY 2m | QUIET | +0.032 | **+0.081** | -$1,493 | **-$614** | -$1,262 |
| SPY 2m | **FINAL** | -0.080 | **+0.060** | -$1,028 | **-$392** | -$784 |
| SPY 3m | v3.0 every day | -0.038 | **+0.078** | -$4,755 | **-$1,005** | -$2,248 |
| SPY 3m | QUIET | +0.035 | **+0.202** | -$1,647 | **-$55** | -$847 |
| SPY 3m | **FINAL** | +0.182 | **+0.461** | -$286 | **+$261** | -$159 |
| QQQ 2m | v3.0 every day | -0.005 | **+0.033** | -$3,389 | **-$1,827** | -$3,484 |
| QQQ 2m | QUIET | +0.077 | **+0.118** | -$231 | **-$231** | -$1,054 |
| QQQ 2m | **FINAL** | +0.063 | **-0.078** | -$378 | **-$1,016** | -$1,527 |
| QQQ 3m | v3.0 every day | -0.020 | **+0.148** | -$4,269 | **+$326** | -$1,530 |
| QQQ 3m | QUIET | +0.059 | **+0.141** | -$966 | **-$448** | -$1,408 |
| QQQ 3m | **FINAL** | +0.315 | **-0.143** | +$326 | **-$1,183** | -$1,741 |

## Monte Carlo: 10,000 possible years (1 contract per trade, today's prices, after costs)
How it works: the real trading days (including days with no trade) are drawn at random, with replacement, 252 at a time = one possible year. Repeated 10,000 times. *Chance the edge is real* = how often a re-shuffled copy of the whole history still ended in profit (95%+ = strong, 80-95% = maybe, under 80% = could easily be luck). *Worst drop* = biggest fall from a high point during the year.

### SPY 2m
| Setup | Option | Days sampled from | Trades / yr | Typical year | Bad year (1 in 20) | Good year (1 in 20) | Chance of a losing year | Chance of a losing 3 months | Typical worst drop | Bad-case worst drop | Chance the edge is real |
|---|---|---|---|---|---|---|---|---|---|---|---|
| v3.0 every day | 1DTE | all years | 710 | **-$3,124** | -$6,986 | +$808 | **90%** | 74% | -$4,283 | -$7,585 | 0% |
| QUIET | 1DTE | all years | 278 | **-$1,136** | -$3,001 | +$763 | **84%** | 69% | -$1,758 | -$3,322 | 1% |
| FINAL | 1DTE | all years | 112 | **-$814** | -$1,946 | +$622 | **84%** | 74% | -$1,160 | -$2,093 | 1% |
| FINAL | 1DTE | only 2020-2023 (if that market comes back) | 116 | **-$1,095** | -$2,293 | +$454 | **88%** | 79% | -$1,414 | -$2,428 | 2% |
| FINAL | 1DTE | only 2024-now | 107 | **-$405** | -$1,450 | +$755 | **73%** | 64% | -$844 | -$1,642 | 16% |
| v3.0 every day | 0DTE | all years | 710 | **-$4,453** | -$8,481 | -$324 | **96%** | 82% | -$5,446 | -$9,069 | 0% |
| QUIET | 0DTE | all years | 278 | **-$2,037** | -$4,054 | -$3 | **95%** | 80% | -$2,494 | -$4,273 | 0% |
| FINAL | 0DTE | all years | 112 | **-$1,267** | -$2,535 | +$432 | **90%** | 80% | -$1,594 | -$2,642 | 0% |

### SPY 3m
| Setup | Option | Days sampled from | Trades / yr | Typical year | Bad year (1 in 20) | Good year (1 in 20) | Chance of a losing year | Chance of a losing 3 months | Typical worst drop | Bad-case worst drop | Chance the edge is real |
|---|---|---|---|---|---|---|---|---|---|---|---|
| v3.0 every day | 1DTE | all years | 560 | **-$3,251** | -$7,553 | +$1,403 | **88%** | 75% | -$4,608 | -$8,205 | 0% |
| QUIET | 1DTE | all years | 217 | **-$1,031** | -$3,192 | +$1,258 | **78%** | 66% | -$1,844 | -$3,579 | 3% |
| FINAL | 1DTE | all years | 88 | **-$131** | -$1,632 | +$1,842 | **55%** | 57% | -$951 | -$1,949 | 42% |
| FINAL | 1DTE | only 2020-2023 (if that market comes back) | 89 | **-$404** | -$2,076 | +$1,886 | **63%** | 63% | -$1,180 | -$2,331 | 29% |
| FINAL | 1DTE | only 2024-now | 88 | **+$244** | -$1,058 | +$1,659 | **38%** | 46% | -$682 | -$1,443 | 69% |
| v3.0 every day | 0DTE | all years | 560 | **-$4,616** | -$9,133 | +$652 | **93%** | 79% | -$5,862 | -$9,702 | 0% |
| QUIET | 0DTE | all years | 217 | **-$1,865** | -$4,200 | +$620 | **89%** | 75% | -$2,537 | -$4,564 | 0% |
| FINAL | 0DTE | all years | 88 | **-$631** | -$2,318 | +$1,624 | **70%** | 66% | -$1,362 | -$2,585 | 14% |

### QQQ 2m
| Setup | Option | Days sampled from | Trades / yr | Typical year | Bad year (1 in 20) | Good year (1 in 20) | Chance of a losing year | Chance of a losing 3 months | Typical worst drop | Bad-case worst drop | Chance the edge is real |
|---|---|---|---|---|---|---|---|---|---|---|---|
| v3.0 every day | 1DTE | all years | 691 | **-$2,771** | -$7,521 | +$2,197 | **82%** | 68% | -$4,542 | -$8,507 | 1% |
| QUIET | 1DTE | all years | 225 | **-$228** | -$2,489 | +$2,089 | **57%** | 54% | -$1,458 | -$3,054 | 32% |
| FINAL | 1DTE | all years | 89 | **-$696** | -$1,926 | +$805 | **79%** | 70% | -$1,136 | -$2,101 | 2% |
| FINAL | 1DTE | only 2020-2023 (if that market comes back) | 81 | **-$430** | -$1,761 | +$1,293 | **68%** | 64% | -$1,030 | -$1,956 | 20% |
| FINAL | 1DTE | only 2024-now | 100 | **-$1,048** | -$2,115 | +$151 | **93%** | 78% | -$1,316 | -$2,234 | 1% |
| v3.0 every day | 0DTE | all years | 691 | **-$4,508** | -$9,458 | +$636 | **93%** | 77% | -$5,907 | -$10,214 | 0% |
| QUIET | 0DTE | all years | 225 | **-$1,155** | -$3,556 | +$1,317 | **79%** | 67% | -$2,057 | -$3,991 | 2% |
| FINAL | 0DTE | all years | 89 | **-$1,331** | -$2,650 | +$456 | **90%** | 80% | -$1,657 | -$2,772 | 0% |

### QQQ 3m
| Setup | Option | Days sampled from | Trades / yr | Typical year | Bad year (1 in 20) | Good year (1 in 20) | Chance of a losing year | Chance of a losing 3 months | Typical worst drop | Bad-case worst drop | Chance the edge is real |
|---|---|---|---|---|---|---|---|---|---|---|---|
| v3.0 every day | 1DTE | all years | 556 | **-$2,367** | -$7,538 | +$2,748 | **78%** | 65% | -$4,503 | -$8,505 | 3% |
| QUIET | 1DTE | all years | 181 | **-$779** | -$3,108 | +$1,808 | **70%** | 62% | -$1,821 | -$3,581 | 9% |
| FINAL | 1DTE | all years | 74 | **-$357** | -$2,001 | +$1,731 | **63%** | 61% | -$1,152 | -$2,252 | 24% |
| FINAL | 1DTE | only 2020-2023 (if that market comes back) | 65 | **+$227** | -$1,586 | +$2,532 | **42%** | 50% | -$987 | -$2,037 | 71% |
| FINAL | 1DTE | only 2024-now | 85 | **-$1,230** | -$2,519 | +$327 | **91%** | 78% | -$1,551 | -$2,648 | 2% |
| v3.0 every day | 0DTE | all years | 556 | **-$4,206** | -$9,569 | +$1,329 | **89%** | 75% | -$5,936 | -$10,556 | 0% |
| QUIET | 0DTE | all years | 181 | **-$1,744** | -$4,271 | +$1,028 | **86%** | 71% | -$2,566 | -$4,669 | 0% |
| FINAL | 0DTE | all years | 74 | **-$856** | -$2,598 | +$1,525 | **74%** | 68% | -$1,541 | -$2,847 | 7% |

## Year by year (1DTE $ per year, 1 contract)
| Chart | Year | v3.0 every day | QUIET | FINAL | FINAL trades |
|---|---|---|---|---|---|
| SPY 2m | 2020 | -$2,786 | -$2,197 | **-$1,945** | 139 |
| SPY 2m | 2021 | -$2,126 | -$2,083 | **-$1,772** | 136 |
| SPY 2m | 2022 | -$5,566 | -$55 | **+$277** | 90 |
| SPY 2m | 2023 | -$4,888 | -$1,625 | **-$663** | 97 |
| SPY 2m | 2024 | -$3,089 | -$5 | **-$213** | 100 |
| SPY 2m | 2025 | -$1,675 | -$1,540 | **-$1,538** | 130 |
| SPY 2m | 2026 | -$876 | -$162 | **+$659** | 69 |
| SPY 3m | 2020 | -$3,634 | -$3,774 | **-$2,231** | 117 |
| SPY 3m | 2021 | -$4,906 | -$1,156 | **-$99** | 95 |
| SPY 3m | 2022 | -$6,991 | +$103 | **+$1,942** | 67 |
| SPY 3m | 2023 | -$3,452 | -$1,750 | **-$756** | 76 |
| SPY 3m | 2024 | -$1,969 | +$884 | **+$153** | 84 |
| SPY 3m | 2025 | -$96 | -$1,853 | **-$693** | 95 |
| SPY 3m | 2026 | -$730 | +$816 | **+$1,266** | 65 |
| QQQ 2m | 2020 | -$4,707 | -$1,088 | **-$241** | 91 |
| QQQ 2m | 2021 | -$4,752 | -$1,388 | **-$1,143** | 79 |
| QQQ 2m | 2022 | -$2,250 | +$878 | **+$890** | 77 |
| QQQ 2m | 2023 | -$1,821 | +$676 | **-$1,015** | 78 |
| QQQ 2m | 2024 | -$3,277 | -$261 | **-$1,173** | 94 |
| QQQ 2m | 2025 | -$25 | +$116 | **-$1,087** | 112 |
| QQQ 2m | 2026 | -$1,779 | -$497 | **-$565** | 72 |
| QQQ 3m | 2020 | -$911 | -$1,274 | **-$298** | 81 |
| QQQ 3m | 2021 | -$6,803 | -$1,718 | **-$897** | 52 |
| QQQ 3m | 2022 | -$6,136 | +$176 | **+$2,511** | 64 |
| QQQ 3m | 2023 | -$3,191 | -$1,041 | **-$16** | 64 |
| QQQ 3m | 2024 | -$808 | -$134 | **-$1,670** | 70 |
| QQQ 3m | 2025 | +$1,628 | -$276 | **-$829** | 106 |
| QQQ 3m | 2026 | +$86 | -$837 | **-$792** | 61 |

## SPY 2m: every idea on top of the quiet-day filter
Today's prices: SPY ≈ 763.27, 1 ATR (2m) ≈ 0.36 pts. TRAIN 2020-2023 = 1006 sessions, TEST 2024-now = 701 sessions. $ = 1 contract per trade, after $2 costs.

| Setup | Trades / yr | Win | ATR / trade TRAIN | ATR / trade TEST | 1DTE $/yr TRAIN | 1DTE $/yr TEST | 0DTE $/yr TRAIN | 0DTE $/yr TEST | beats QUIET (1DTE) |
|---|---|---|---|---|---|---|---|---|---|
| **v3.0 (every day)** | 710 | 40% | -0.006 | **+0.009** | -$3,849 | **-$2,028** | -$5,388 | -$3,107 |  |
| **QUIET (v3.0 + quiet-day filter)** | 278 | 40% | +0.032 | **+0.081** | -$1,493 | **-$614** | -$2,546 | -$1,262 |  |
| + 15m agrees | 155 | 40% | -0.019 | **-0.019** | -$1,070 | **-$669** | -$1,652 | -$1,077 | TRAIN only |
| + 15m and 60m agree | 103 | 40% | -0.034 | **-0.134** | -$687 | **-$678** | -$1,049 | -$984 | TRAIN only |
| Vix Fix spike within 5 | 190 | 39% | +0.069 | **+0.020** | -$835 | **-$616** | -$1,404 | -$951 | TRAIN only |
| Vix Fix spike within 20 | 396 | 42% | +0.032 | **+0.119** | -$2,197 | **-$979** | -$3,832 | -$2,130 |  |
| no Vix Fix filter | 550 | 42% | +0.035 | **+0.079** | -$2,866 | **-$1,877** | -$5,347 | -$3,610 |  |
| no waiting for a late spike (wait 0) | 272 | 41% | +0.037 | **+0.103** | -$1,482 | **-$468** | -$2,531 | -$1,097 | ✅ both |
| wait up to 10 for a spike | 289 | 41% | +0.023 | **+0.076** | -$1,688 | **-$706** | -$2,815 | -$1,419 |  |
| entries from 10:00 | 221 | 41% | +0.031 | **+0.123** | -$1,340 | **-$441** | -$2,334 | -$1,064 | ✅ both |
| no entries after 14:00 | 223 | 40% | -0.006 | **+0.056** | -$1,188 | **-$559** | -$1,730 | -$944 | ✅ both |
| no VWAP rule on the line | 184 | 41% | -0.050 | **+0.168** | -$1,077 | **-$456** | -$1,882 | -$1,015 | ✅ both |
| EXIT ride strong trend | 278 | 36% | +0.079 | **+0.136** | -$1,677 | **-$500** | -$3,002 | -$1,439 | TEST only |
| EXIT ride if 15m agrees | 278 | 37% | +0.059 | **+0.140** | -$1,772 | **-$301** | -$3,034 | -$1,151 | TEST only |
| EXIT cut losers on warning | 308 | 29% | +0.011 | **+0.084** | -$1,184 | **-$431** | -$1,950 | -$935 | ✅ both |
| EXIT ride + cut losers | 308 | 27% | +0.038 | **+0.133** | -$1,372 | **-$185** | -$2,334 | -$894 | ✅ both |
| EXIT ride + cut, warning after 3 candles | 308 | 27% | +0.063 | **+0.128** | -$1,421 | **-$538** | -$2,565 | -$1,411 | ✅ both |
| EXIT hold 10 candles | 284 | 42% | -0.012 | **+0.034** | -$1,641 | **-$707** | -$2,407 | -$1,172 |  |
| EXIT hold 20 candles | 276 | 38% | +0.065 | **+0.055** | -$1,519 | **-$771** | -$2,759 | -$1,607 |  |
| EXIT hold 25 candles | 272 | 36% | +0.104 | **+0.069** | -$1,460 | **-$804** | -$2,764 | -$1,775 | TRAIN only |
| EXIT stop 1.5 ATR | 289 | 36% | +0.073 | **+0.061** | -$1,101 | **-$689** | -$1,999 | -$1,302 | TRAIN only |
| EXIT stop 3 ATR | 271 | 43% | -0.002 | **+0.086** | -$1,830 | **-$711** | -$2,879 | -$1,429 |  |
| EXIT no stop (flip / time / 15:55 only) | 268 | 44% | +0.012 | **+0.056** | -$1,760 | **-$838** | -$2,828 | -$1,562 |  |

## SPY 3m: every idea on top of the quiet-day filter
Today's prices: SPY ≈ 763.27, 1 ATR (3m) ≈ 0.45 pts. TRAIN 2020-2023 = 1006 sessions, TEST 2024-now = 701 sessions. $ = 1 contract per trade, after $2 costs.

| Setup | Trades / yr | Win | ATR / trade TRAIN | ATR / trade TEST | 1DTE $/yr TRAIN | 1DTE $/yr TEST | 0DTE $/yr TRAIN | 0DTE $/yr TEST | beats QUIET (1DTE) |
|---|---|---|---|---|---|---|---|---|---|
| **v3.0 (every day)** | 560 | 40% | -0.038 | **+0.078** | -$4,755 | **-$1,005** | -$6,046 | -$2,248 |  |
| **QUIET (v3.0 + quiet-day filter)** | 217 | 42% | +0.035 | **+0.202** | -$1,647 | **-$55** | -$2,580 | -$847 |  |
| + 15m agrees | 127 | 43% | -0.021 | **+0.190** | -$1,230 | **-$99** | -$1,826 | -$619 | TRAIN only |
| + 15m and 60m agree | 82 | 45% | +0.119 | **+0.219** | -$595 | **-$171** | -$901 | -$558 | TRAIN only |
| Vix Fix spike within 5 | 151 | 40% | +0.041 | **+0.192** | -$909 | **-$18** | -$1,470 | -$432 | ✅ both |
| Vix Fix spike within 20 | 306 | 43% | +0.056 | **+0.191** | -$2,411 | **-$448** | -$3,960 | -$1,779 |  |
| no Vix Fix filter | 420 | 43% | +0.040 | **+0.140** | -$3,437 | **-$1,204** | -$6,027 | -$3,262 |  |
| no waiting for a late spike (wait 0) | 213 | 42% | +0.023 | **+0.205** | -$1,824 | **-$69** | -$2,781 | -$856 |  |
| wait up to 10 for a spike | 225 | 42% | +0.051 | **+0.173** | -$1,431 | **-$236** | -$2,401 | -$1,064 | TRAIN only |
| entries from 10:00 | 166 | 43% | -0.001 | **+0.247** | -$1,440 | **+$21** | -$2,287 | -$728 | ✅ both |
| no entries after 14:00 | 177 | 41% | +0.001 | **+0.174** | -$1,561 | **-$240** | -$2,168 | -$708 | TRAIN only |
| no VWAP rule on the line | 128 | 43% | +0.117 | **+0.035** | -$554 | **-$718** | -$1,219 | -$1,407 | TRAIN only |
| EXIT ride strong trend | 217 | 37% | +0.079 | **+0.314** | -$1,362 | **-$26** | -$2,636 | -$1,139 | ✅ both |
| EXIT ride if 15m agrees | 217 | 38% | +0.084 | **+0.313** | -$1,271 | **+$94** | -$2,379 | -$935 | ✅ both |
| EXIT cut losers on warning | 241 | 30% | +0.037 | **+0.167** | -$1,289 | **+$28** | -$2,072 | -$540 | ✅ both |
| EXIT ride + cut losers | 240 | 28% | +0.056 | **+0.249** | -$1,236 | **+$116** | -$2,292 | -$706 | ✅ both |
| EXIT ride + cut, warning after 3 candles | 240 | 28% | +0.103 | **+0.288** | -$585 | **+$145** | -$1,772 | -$813 | ✅ both |
| EXIT hold 10 candles | 222 | 45% | +0.011 | **+0.148** | -$1,614 | **-$205** | -$2,352 | -$728 | TRAIN only |
| EXIT hold 20 candles | 213 | 39% | +0.048 | **+0.249** | -$1,599 | **-$15** | -$2,750 | -$974 | ✅ both |
| EXIT hold 25 candles | 208 | 37% | +0.103 | **+0.300** | -$1,378 | **-$78** | -$2,765 | -$1,201 | TRAIN only |
| EXIT stop 1.5 ATR | 225 | 38% | +0.010 | **+0.227** | -$1,596 | **+$138** | -$2,486 | -$577 | ✅ both |
| EXIT stop 3 ATR | 210 | 45% | +0.059 | **+0.214** | -$1,612 | **-$1** | -$2,598 | -$794 | ✅ both |
| EXIT no stop (flip / time / 15:55 only) | 207 | 46% | +0.062 | **+0.226** | -$1,607 | **+$145** | -$2,645 | -$666 | ✅ both |

## QQQ 2m: every idea on top of the quiet-day filter
Today's prices: QQQ ≈ 709.86, 1 ATR (2m) ≈ 0.52 pts. TRAIN 2020-2023 = 1006 sessions, TEST 2024-now = 701 sessions. $ = 1 contract per trade, after $2 costs.

| Setup | Trades / yr | Win | ATR / trade TRAIN | ATR / trade TEST | 1DTE $/yr TRAIN | 1DTE $/yr TEST | 0DTE $/yr TRAIN | 0DTE $/yr TEST | beats QUIET (1DTE) |
|---|---|---|---|---|---|---|---|---|---|
| **v3.0 (every day)** | 691 | 41% | -0.005 | **+0.033** | -$3,389 | **-$1,827** | -$5,250 | -$3,484 |  |
| **QUIET (v3.0 + quiet-day filter)** | 225 | 42% | +0.077 | **+0.118** | -$231 | **-$231** | -$1,249 | -$1,054 |  |
| + 15m agrees | 124 | 41% | +0.038 | **-0.034** | -$423 | **-$612** | -$1,074 | -$1,084 |  |
| + 15m and 60m agree | 82 | 41% | +0.033 | **-0.064** | -$168 | **-$596** | -$637 | -$917 | TRAIN only |
| Vix Fix spike within 5 | 152 | 40% | +0.115 | **+0.043** | +$230 | **-$238** | -$341 | -$671 | TRAIN only |
| Vix Fix spike within 20 | 328 | 43% | +0.086 | **+0.160** | +$141 | **+$20** | -$1,466 | -$1,339 | ✅ both |
| no Vix Fix filter | 453 | 43% | +0.036 | **+0.091** | -$1,162 | **-$1,084** | -$3,640 | -$3,133 |  |
| no waiting for a late spike (wait 0) | 220 | 42% | +0.058 | **+0.129** | -$296 | **-$153** | -$1,313 | -$948 | TEST only |
| wait up to 10 for a spike | 234 | 42% | +0.095 | **+0.101** | -$166 | **-$391** | -$1,202 | -$1,282 | TRAIN only |
| entries from 10:00 | 171 | 43% | +0.073 | **+0.206** | -$451 | **+$32** | -$1,428 | -$765 | TEST only |
| no entries after 14:00 | 175 | 42% | +0.056 | **+0.182** | +$4 | **+$281** | -$463 | -$93 | ✅ both |
| no VWAP rule on the line | 149 | 40% | -0.071 | **+0.164** | -$1,055 | **-$472** | -$1,861 | -$1,198 |  |
| EXIT ride strong trend | 224 | 37% | +0.120 | **+0.094** | -$714 | **-$1,132** | -$2,146 | -$2,414 |  |
| EXIT ride if 15m agrees | 225 | 39% | +0.091 | **+0.085** | -$624 | **-$1,013** | -$1,957 | -$2,149 |  |
| EXIT cut losers on warning | 249 | 30% | +0.034 | **+0.020** | -$582 | **-$811** | -$1,447 | -$1,450 |  |
| EXIT ride + cut losers | 249 | 29% | +0.072 | **+0.032** | -$1,007 | **-$1,241** | -$2,227 | -$2,163 |  |
| EXIT ride + cut, warning after 3 candles | 249 | 29% | +0.093 | **+0.031** | -$940 | **-$1,483** | -$2,360 | -$2,612 |  |
| EXIT hold 10 candles | 229 | 45% | +0.010 | **+0.068** | -$549 | **-$313** | -$1,357 | -$894 |  |
| EXIT hold 20 candles | 222 | 39% | +0.052 | **+0.131** | -$801 | **-$585** | -$2,089 | -$1,673 |  |
| EXIT hold 25 candles | 220 | 37% | +0.054 | **+0.177** | -$882 | **-$317** | -$2,377 | -$1,590 |  |
| EXIT stop 1.5 ATR | 233 | 37% | +0.055 | **+0.121** | -$407 | **-$252** | -$1,303 | -$1,001 |  |
| EXIT stop 3 ATR | 218 | 45% | +0.050 | **+0.152** | -$329 | **-$89** | -$1,424 | -$1,013 | TEST only |
| EXIT no stop (flip / time / 15:55 only) | 215 | 46% | +0.045 | **+0.147** | -$182 | **-$104** | -$1,360 | -$1,002 | ✅ both |

## QQQ 3m: every idea on top of the quiet-day filter
Today's prices: QQQ ≈ 709.86, 1 ATR (3m) ≈ 0.64 pts. TRAIN 2020-2023 = 1006 sessions, TEST 2024-now = 701 sessions. $ = 1 contract per trade, after $2 costs.

| Setup | Trades / yr | Win | ATR / trade TRAIN | ATR / trade TEST | 1DTE $/yr TRAIN | 1DTE $/yr TEST | 0DTE $/yr TRAIN | 0DTE $/yr TEST | beats QUIET (1DTE) |
|---|---|---|---|---|---|---|---|---|---|
| **v3.0 (every day)** | 556 | 41% | -0.020 | **+0.148** | -$4,269 | **+$326** | -$5,991 | -$1,530 |  |
| **QUIET (v3.0 + quiet-day filter)** | 181 | 41% | +0.059 | **+0.141** | -$966 | **-$448** | -$1,924 | -$1,408 |  |
| + 15m agrees | 107 | 42% | +0.101 | **+0.061** | -$441 | **-$789** | -$1,037 | -$1,448 | TRAIN only |
| + 15m and 60m agree | 67 | 42% | +0.132 | **-0.104** | +$11 | **-$996** | -$255 | -$1,508 | TRAIN only |
| Vix Fix spike within 5 | 129 | 39% | +0.014 | **+0.084** | -$1,109 | **-$504** | -$1,715 | -$1,005 |  |
| Vix Fix spike within 20 | 250 | 42% | +0.040 | **+0.158** | -$1,997 | **-$468** | -$3,664 | -$2,014 |  |
| no Vix Fix filter | 349 | 42% | +0.033 | **+0.049** | -$2,865 | **-$2,199** | -$5,531 | -$4,799 |  |
| no waiting for a late spike (wait 0) | 177 | 41% | +0.039 | **+0.104** | -$1,154 | **-$737** | -$2,134 | -$1,706 |  |
| wait up to 10 for a spike | 185 | 42% | +0.091 | **+0.127** | -$641 | **-$589** | -$1,600 | -$1,620 | TRAIN only |
| entries from 10:00 | 134 | 42% | +0.051 | **+0.162** | -$745 | **-$459** | -$1,653 | -$1,370 | TRAIN only |
| no entries after 14:00 | 147 | 42% | +0.005 | **+0.171** | -$1,226 | **-$79** | -$1,786 | -$538 | TEST only |
| no VWAP rule on the line | 103 | 44% | +0.182 | **+0.307** | +$149 | **+$434** | -$505 | -$157 | ✅ both |
| EXIT ride strong trend | 181 | 37% | +0.152 | **+0.118** | -$764 | **-$1,024** | -$2,054 | -$2,393 | TRAIN only |
| EXIT ride if 15m agrees | 181 | 38% | +0.119 | **+0.147** | -$953 | **-$722** | -$2,135 | -$1,956 | TRAIN only |
| EXIT cut losers on warning | 200 | 30% | +0.067 | **+0.110** | -$744 | **-$224** | -$1,547 | -$922 | ✅ both |
| EXIT ride + cut losers | 200 | 28% | +0.085 | **+0.088** | -$1,024 | **-$643** | -$2,096 | -$1,643 |  |
| EXIT ride + cut, warning after 3 candles | 200 | 29% | +0.138 | **+0.157** | -$498 | **-$176** | -$1,733 | -$1,294 | ✅ both |
| EXIT hold 10 candles | 184 | 45% | +0.056 | **+0.137** | -$741 | **-$122** | -$1,399 | -$750 | ✅ both |
| EXIT hold 20 candles | 177 | 39% | +0.128 | **+0.163** | -$727 | **-$425** | -$1,868 | -$1,608 | ✅ both |
| EXIT hold 25 candles | 175 | 36% | +0.146 | **+0.144** | -$692 | **-$745** | -$2,010 | -$2,200 | TRAIN only |
| EXIT stop 1.5 ATR | 188 | 37% | +0.089 | **+0.180** | -$714 | **-$154** | -$1,612 | -$989 | ✅ both |
| EXIT stop 3 ATR | 174 | 45% | +0.136 | **+0.076** | -$504 | **-$889** | -$1,491 | -$1,863 | TRAIN only |
| EXIT no stop (flip / time / 15:55 only) | 171 | 46% | +0.123 | **+0.084** | -$562 | **-$839** | -$1,554 | -$1,782 | TRAIN only |

