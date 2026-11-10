# GEX latest

2026-11-10 09:47:18 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 8.79 pts (1.17%); nearest wall is the call wall at 750.00, 1.72 pts (0.23%) away.
QQQ: spot above the 0DTE flip by 2.15 pts (0.32%); nearest wall is the call wall at 672.00, 1.47 pts (0.22%) away.

SPY top |GEX| strikes: 730.00 ($498.38M), 745.00 ($346.88M), 750.00 ($312.18M).
QQQ top |GEX| strikes: 650.00 ($231.73M), 685.00 ($172.68M), 672.00 ($81.91M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 748.28 | 673.47 |
| 0DTE flip | 739.49 | 671.32 |
| All-expiry flip |  |  |
| 0DTE call wall | 750.00 | 672.00 |
| 0DTE put wall | 755.00 | 660.00 |
| Net GEX 0DTE | $889.96M | $217.90M |
| Net GEX all | -$289.17M | -$166.71M |
| Vol-adj net 0DTE | -$903.51M | -$445.68M |
| Vol-adj net all | -$2.24B | -$1.00B |
| Missing greeks | 380/896 | 370/1038 |
| OI used | 1115025 | 615363 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
