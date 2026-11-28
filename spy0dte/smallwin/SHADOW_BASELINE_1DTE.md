# Shadow baseline 1dte · 17 saved days (2026-11-03 to 2026-11-25) · 1DTE bars (Alpaca 1-minute history, the bot and the shadow avenues both trade the next-day expiry)

Every signal scored on its own (one row per signal, overlapping signals all counted). 5% bid, skipped if it doesn't fill.

| Avenue | Signals | Filled | Own exits: won · avg · total · worst | Small-win exits: won · avg · total · worst |
|---|---|---|---|---|
| Trend your way (Option 2) | 101 | 73 | 68/73 (93%) · 9.5% · 694% · -75.2% | 52/73 (71%) · 3.8% · 280.8% · -12.8% |
| Lined up + ran hard | 52 | 38 | 27/38 (71%) · 10.1% · 382.2% · -16.6% | 21/38 (55%) · 1.9% · 71.9% · -9.7% |
| Swing Break | 68 | 50 | 43/50 (86%) · 8.4% · 419.3% · -40.8% | 32/50 (64%) · 3.1% · 155.6% · -20.7% |
| Fade MAIN | 17 | 14 | 12/14 (86%) · 12.6% · 177% · -35.4% | 11/14 (79%) · 8.8% · 122.5% · -2.4% |
| Smart dots | 111 | 86 | 57/86 (66%) · 9.2% · 787.4% · -36.4% | 55/86 (64%) · 3.2% · 279% · -20.5% |

Trend safety check (both charts breaking your way): yes 42/46 (91%) avg 8.2% · no 26/27 (96%) avg 11.8%

One $1,000 account, first come, one trade at a time (full port; weak-trend signals half):

| Account | Own exits | Small-win exits |
|---|---|---|
| Small-win reversal bot alone | $789 · 42 trades · 19 won · worst drop 47% | (same) |
| Trend (safety check) + reversal dots (lined up) | $160,178 · 63 trades · 52 won · worst drop 38% | $3,734 · 74 trades · 43 won · worst drop 23% |
| All three (+ Swing Break) | $533,896 · 89 trades · 72 won · worst drop 38% | $8,285 · 111 trades · 66 won · worst drop 33% |
| Small-win bot + Trend your way (Option 2) | $4,668 · 64 trades · 41 won · worst drop 46% | $1,589 · 75 trades · 38 won · worst drop 46% |
| Small-win bot + Lined up + ran hard | $15,809 · 73 trades · 40 won · worst drop 36% | $1,226 · 77 trades · 37 won · worst drop 53% |
| Small-win bot + Swing Break | $6,084 · 80 trades · 51 won · worst drop 48% | $2,531 · 87 trades · 48 won · worst drop 30% |
| Small-win bot + Fade MAIN | $1,975 · 47 trades · 24 won · worst drop 45% | $2,143 · 50 trades · 26 won · worst drop 45% |
| Small-win bot + Smart dots | $212,859 · 100 trades · 59 won · worst drop 49% | $8,006 · 115 trades · 66 won · worst drop 46% |

Rules are copied from the Edge Stress Test (build/track.js, swing.js, itm.js) and the 1 ITM Confluence trackers (lu_track.js, bs_build.js). Replay fills at the next bar's open with the 1¢ slip the trackers use; live fills will cost a little more.
