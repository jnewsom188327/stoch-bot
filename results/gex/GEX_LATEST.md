# GEX latest

2026-11-10 12:56:00 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 6.43 pts (0.86%); nearest wall is the put wall at 745.00, 1.31 pts (0.18%) away.
QQQ: spot above the 0DTE flip by 0.28 pts (0.04%); nearest wall is the put wall at 671.00, 1.58 pts (0.24%) away.

SPY top |GEX| strikes: 730.00 ($571.09M), 745.00 ($404.87M), 750.00 ($324.31M).
QQQ top |GEX| strikes: 650.00 ($268.90M), 685.00 ($157.51M), 672.00 ($131.78M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 746.31 | 669.42 |
| 0DTE flip | 739.88 | 669.14 |
| All-expiry flip |  |  |
| 0DTE call wall | 748.00 | 672.00 |
| 0DTE put wall | 745.00 | 671.00 |
| Net GEX 0DTE | $786.69M | $190.86M |
| Net GEX all | -$790.11M | -$353.21M |
| Vol-adj net 0DTE | -$62.28B | -$30.53B |
| Vol-adj net all | -$67.06B | -$32.57B |
| Missing greeks | 377/896 | 405/1052 |
| OI used | 1115025 | 613029 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
