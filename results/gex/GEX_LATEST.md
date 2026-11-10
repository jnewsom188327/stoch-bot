# GEX latest

2026-11-10 11:22:02 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 7.74 pts (1.04%); nearest wall is the put wall at 745.00, 1.91 pts (0.26%) away.
QQQ: spot above the 0DTE flip by 1.81 pts (0.27%); nearest wall is the call wall at 672.00, 0.89 pts (0.13%) away.

SPY top |GEX| strikes: 730.00 ($520.28M), 745.00 ($388.99M), 750.00 ($349.54M).
QQQ top |GEX| strikes: 650.00 ($232.86M), 685.00 ($183.81M), 672.00 ($120.06M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 746.91 | 672.89 |
| 0DTE flip | 739.17 | 671.08 |
| All-expiry flip |  |  |
| 0DTE call wall | 750.00 | 672.00 |
| 0DTE put wall | 745.00 | 671.00 |
| Net GEX 0DTE | $1.07B | $280.81M |
| Net GEX all | -$298.24M | -$150.96M |
| Vol-adj net 0DTE | -$28.17B | -$8.29B |
| Vol-adj net all | -$31.55B | -$9.31B |
| Missing greeks | 394/896 | 389/1046 |
| OI used | 1115025 | 615793 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
