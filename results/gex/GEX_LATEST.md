# GEX latest

2026-11-12 09:54:57 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 1.93 pts (0.25%); nearest wall is the call wall at 760.00, 1.92 pts (0.25%) away.
QQQ: spot above the 0DTE flip by 6.27 pts (0.91%); nearest wall is the call wall at 685.00, 2.12 pts (0.31%) away.

SPY top |GEX| strikes: 745.00 ($274.30M), 760.00 ($263.75M), 762.00 ($251.61M).
QQQ top |GEX| strikes: 700.00 ($148.96M), 685.00 ($140.59M), 696.00 ($137.89M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 758.08 | 687.12 |
| 0DTE flip | 756.15 | 680.85 |
| All-expiry flip | 764.69 | 696.83 |
| 0DTE call wall | 760.00 | 685.00 |
| 0DTE put wall | 744.00 | 680.00 |
| Net GEX 0DTE | $625.82M | $305.07M |
| Net GEX all | $925.27M | $457.80M |
| Vol-adj net 0DTE | $6.50B | $2.77B |
| Vol-adj net all | $7.09B | $2.92B |
| Missing greeks | 312/896 | 317/968 |
| OI used | 1123000 | 681421 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
