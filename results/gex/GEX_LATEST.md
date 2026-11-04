# GEX latest

2026-11-04 09:49:22 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot below the 0DTE flip by 6.38 pts (0.83%); nearest wall is the put wall at 767.00, 0.06 pts (0.01%) away.
QQQ: spot below the 0DTE flip by 12.69 pts (1.82%); nearest wall is the call wall at 700.00, 2.48 pts (0.36%) away.

SPY top |GEX| strikes: 770.00 ($457.05M), 767.00 ($425.92M), 750.00 ($351.85M).
QQQ top |GEX| strikes: 713.00 ($352.83M), 680.00 ($273.16M), 675.00 ($256.45M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 766.94 | 697.52 |
| 0DTE flip | 773.32 | 710.21 |
| All-expiry flip | 779.51 |  |
| 0DTE call wall | 765.00 | 700.00 |
| 0DTE put wall | 767.00 | 685.00 |
| Net GEX 0DTE | $206.86M | $38.93M |
| Net GEX all | $377.47M | -$1.47B |
| Vol-adj net 0DTE | $1.92B | $1.10B |
| Vol-adj net all | $2.96B | -$233.25M |
| Missing greeks | 328/894 | 281/856 |
| OI used | 1099225 | 1024877 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
