# Shadow baseline · 17 saved days (2026-11-03 to 2026-11-25) · 0DTE bars (1DTE bars are saved from Nov 30 on)

Every signal scored on its own (one row per signal, overlapping signals all counted). 5% bid, skipped if it doesn't fill.

| Avenue | Signals | Filled | Own exits: won · avg · total · worst | Small-win exits: won · avg · total · worst |
|---|---|---|---|---|
| Trend your way (Option 2) | 101 | 70 | 69/70 (99%) · 11.4% · 794.9% · -75.3% | 41/70 (59%) · 0.4% · 28.7% · -20.6% |
| Lined up + ran hard | 52 | 38 | 28/38 (74%) · 10.1% · 382% · -37.8% | 18/38 (47%) · -0.7% · -26.7% · -20.4% |
| Swing Break | 68 | 48 | 47/48 (98%) · 11.8% · 568.4% · -50.4% | 30/48 (63%) · 1.2% · 55.7% · -21% |
| Fade MAIN | 17 | 14 | 14/14 (100%) · 21.5% · 300.4% · 14.3% | 12/14 (86%) · 8.5% · 119.1% · -6.4% |
| Smart dots | 111 | 85 | 56/85 (66%) · 6.6% · 562.3% · -48.9% | 51/85 (60%) · 0.4% · 30.3% · -21.2% |

Trend safety check (both charts breaking your way): yes 39/40 (98%) avg 11.2% · no 30/30 (100%) avg 11.5%

One $1,000 account, first come, one trade at a time (full port; weak-trend signals half):

| Account | Own exits | Small-win exits |
|---|---|---|
| Small-win reversal bot alone | $3,075 · 78 trades · 52 won · worst drop 25% | (same) |
| Trend (safety check) + reversal dots (lined up) | $302,996 · 67 trades · 57 won · worst drop 38% | $544 · 73 trades · 35 won · worst drop 67% |
| All three (+ Swing Break) | $4,892,375 · 92 trades · 83 won · worst drop 38% | $537 · 110 trades · 58 won · worst drop 78% |
| Small-win bot + Trend your way (Option 2) | $33,254 · 98 trades · 73 won · worst drop 23% | $2,070 · 105 trades · 63 won · worst drop 47% |
| Small-win bot + Lined up + ran hard | $65,222 · 101 trades · 70 won · worst drop 51% | $1,695 · 110 trades · 66 won · worst drop 50% |
| Small-win bot + Swing Break | $119,591 · 113 trades · 87 won · worst drop 50% | $4,038 · 121 trades · 79 won · worst drop 40% |
| Small-win bot + Fade MAIN | $14,674 · 81 trades · 56 won · worst drop 25% | $7,669 · 85 trades · 58 won · worst drop 25% |
| Small-win bot + Smart dots | $89,867 · 125 trades · 83 won · worst drop 72% | $3,942 · 145 trades · 94 won · worst drop 70% |

Rules are copied from the Edge Stress Test (build/track.js, swing.js, itm.js) and the 1 ITM Confluence trackers (lu_track.js, bs_build.js). Replay fills at the next bar's open with the 1¢ slip the trackers use; live fills will cost a little more.
