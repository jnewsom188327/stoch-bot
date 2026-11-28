# Shadow baseline 1dte · 9 saved days (2026-11-03 to 2026-11-13) · 1DTE bars (Alpaca 1-minute history, the bot and the shadow avenues both trade the next-day expiry)

Every signal scored on its own (one row per signal, overlapping signals all counted). 5% bid, skipped if it doesn't fill.

| Avenue | Signals | Filled | Own exits: won · avg · total · worst | Small-win exits: won · avg · total · worst |
|---|---|---|---|---|
| Trend your way (Option 2) | 62 | 43 | 40/43 (93%) · 7.9% · 341% · -62% | 31/43 (72%) · 3.7% · 158.4% · -12.8% |
| Lined up + ran hard | 12 | 9 | 6/9 (67%) · 6% · 53.8% · -16.6% | 4/9 (44%) · -1.6% · -14.1% · -9.7% |
| Swing Break | 21 | 10 | 8/10 (80%) · 1.2% · 12% · -24.3% | 8/10 (80%) · 4.9% · 49.2% · -4.5% |
| Fade MAIN | 7 | 6 | 6/6 (100%) · 19.4% · 116.3% · 14.4% | 5/6 (83%) · 8% · 48.1% · -2.4% |
| Smart dots | 66 | 49 | 33/49 (67%) · 9.1% · 444.2% · -26.7% | 30/49 (61%) · 3% · 148.2% · -20.5% |

Trend safety check (both charts breaking your way): yes 24/26 (92%) avg 4.7% · no 16/17 (94%) avg 12.8%

One $1,000 account, first come, one trade at a time (full port; weak-trend signals half):

| Account | Own exits | Small-win exits |
|---|---|---|
| Small-win reversal bot alone | $815 · 31 trades · 14 won · worst drop 45% | (same) |
| Trend (safety check) + reversal dots (lined up) | $4,906 · 25 trades · 23 won · worst drop 17% | $1,175 · 30 trades · 17 won · worst drop 23% |
| All three (+ Swing Break) | $5,141 · 35 trades · 31 won · worst drop 24% | $1,883 · 40 trades · 25 won · worst drop 23% |
| Small-win bot + Trend your way (Option 2) | $2,263 · 42 trades · 27 won · worst drop 25% | $1,106 · 49 trades · 24 won · worst drop 45% |
| Small-win bot + Lined up + ran hard | $947 · 36 trades · 16 won · worst drop 36% | $650 · 39 trades · 17 won · worst drop 51% |
| Small-win bot + Swing Break | $854 · 41 trades · 22 won · worst drop 48% | $1,305 · 41 trades · 22 won · worst drop 27% |
| Small-win bot + Fade MAIN | $1,137 · 31 trades · 14 won · worst drop 45% | $1,024 · 34 trades · 16 won · worst drop 45% |
| Small-win bot + Smart dots | $12,822 · 61 trades · 35 won · worst drop 49% | $2,965 · 70 trades · 39 won · worst drop 46% |

Rules are copied from the Edge Stress Test (build/track.js, swing.js, itm.js) and the 1 ITM Confluence trackers (lu_track.js, bs_build.js). Replay fills at the next bar's open with the 1¢ slip the trackers use; live fills will cost a little more.
