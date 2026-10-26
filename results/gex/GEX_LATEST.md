# GEX latest

2026-10-26 14:45:58 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 765.00, 0.45 pts (0.06%) away.
QQQ: spot below the 0DTE flip by 4.81 pts (0.67%); nearest wall is the put wall at 714.00, 0.42 pts (0.06%) away.

SPY top |GEX| strikes: 766.00 ($2.48B), 767.00 ($1.26B), 762.00 ($537.76M).
QQQ top |GEX| strikes: 715.00 ($70.54M), 710.00 ($69.46M), 700.00 ($51.47M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 765.45 | 713.58 |
| 0DTE flip |  | 718.39 |
| All-expiry flip |  |  |
| 0DTE call wall | 765.00 | 715.00 |
| 0DTE put wall | 766.00 | 714.00 |
| Net GEX 0DTE | -$2.98B | $59.39M |
| Net GEX all | -$4.67B | -$79.37M |
| Vol-adj net 0DTE | $30.81B | $25.79B |
| Vol-adj net all | $30.90B | $26.24B |
| Missing greeks | 337/796 | 316/756 |
| OI used | 729363 | 380158 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
