# GEX latest

2026-11-06 11:20:42 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 735.00, 2.77 pts (0.38%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 655.00, 1.90 pts (0.29%) away.

SPY top |GEX| strikes: 740.00 ($796.89M), 735.00 ($765.65M), 750.00 ($437.12M).
QQQ top |GEX| strikes: 660.00 ($260.65M), 675.00 ($226.86M), 650.00 ($161.52M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 737.77 | 656.90 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 745.00 | 655.00 |
| 0DTE put wall | 735.00 | 660.00 |
| Net GEX 0DTE | -$3.62B | -$1.46B |
| Net GEX all | -$4.68B | -$1.82B |
| Vol-adj net 0DTE | $3.48B | -$4.41B |
| Vol-adj net all | $2.91B | -$4.65B |
| Missing greeks | 342/890 | 307/1002 |
| OI used | 987598 | 886798 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
