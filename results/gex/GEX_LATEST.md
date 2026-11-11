# GEX latest

2026-11-11 10:32:55 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot below the 0DTE flip by 2.01 pts (0.27%); nearest wall is the put wall at 753.00, 3.25 pts (0.43%) away.
QQQ: spot above the 0DTE flip by 5.12 pts (0.74%); nearest wall is the call wall at 690.00, 2.84 pts (0.41%) away.

SPY top |GEX| strikes: 745.00 ($326.79M), 760.00 ($317.00M), 744.00 ($209.51M).
QQQ top |GEX| strikes: 696.00 ($141.34M), 685.00 ($137.74M), 700.00 ($125.91M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 756.25 | 687.16 |
| 0DTE flip | 758.26 | 682.04 |
| All-expiry flip |  | 695.58 |
| 0DTE call wall | 760.00 | 690.00 |
| 0DTE put wall | 753.00 | 675.00 |
| Net GEX 0DTE | $237.65M | $351.11M |
| Net GEX all | -$2.56M | $527.27M |
| Vol-adj net 0DTE | $5.63B | $4.90B |
| Vol-adj net all | $5.60B | $5.23B |
| Missing greeks | 316/904 | 316/984 |
| OI used | 1090376 | 714452 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
