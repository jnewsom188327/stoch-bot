# GEX latest

2026-10-30 15:41:48 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 2.96 pts (0.39%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 690.00, 2.61 pts (0.38%) away.

SPY top |GEX| strikes: 750.00 ($3.06B), 755.00 ($2.39B), 752.00 ($559.53M).
QQQ top |GEX| strikes: 690.00 ($2.92B), 685.00 ($1.04B), 687.00 ($492.87M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 752.96 | 687.39 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 750.00 | 695.00 |
| 0DTE put wall | 750.00 | 690.00 |
| Net GEX 0DTE | -$8.32B | -$5.86B |
| Net GEX all | -$9.76B | -$6.54B |
| Vol-adj net 0DTE | -$110.85B | -$31.33B |
| Vol-adj net all | -$115.73B | -$31.60B |
| Missing greeks | 420/890 | 321/846 |
| OI used | 1620566 | 1114998 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
