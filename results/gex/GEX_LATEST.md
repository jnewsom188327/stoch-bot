# GEX latest

2026-11-03 09:50:07 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 755.00, 1.00 pts (0.13%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 690.00, 3.74 pts (0.54%) away.

SPY top |GEX| strikes: 740.00 ($753.67M), 750.00 ($362.72M), 755.00 ($304.87M).
QQQ top |GEX| strikes: 680.00 ($471.16M), 675.00 ($329.25M), 713.00 ($207.07M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 754.00 | 686.26 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 750.00 | 690.00 |
| 0DTE put wall | 755.00 | 680.00 |
| Net GEX 0DTE | -$31.61M | -$258.68M |
| Net GEX all | -$3.11B | -$2.09B |
| Vol-adj net 0DTE | $2.02B | $490.94M |
| Vol-adj net all | -$986.97M | -$1.37B |
| Missing greeks | 339/880 | 267/840 |
| OI used | 1069962 | 899569 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
