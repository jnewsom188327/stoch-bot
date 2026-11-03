# GEX latest

2026-11-03 13:51:35 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot below the 0DTE flip by 0.32 pts (0.04%); nearest wall is the call wall at 756.00, 0.21 pts (0.03%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 685.00, 2.22 pts (0.32%) away.

SPY top |GEX| strikes: 740.00 ($616.56M), 755.00 ($434.97M), 750.00 ($414.32M).
QQQ top |GEX| strikes: 680.00 ($406.38M), 675.00 ($302.30M), 685.00 ($258.47M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 756.21 | 687.22 |
| 0DTE flip | 756.53 |  |
| All-expiry flip |  |  |
| 0DTE call wall | 756.00 | 690.00 |
| 0DTE put wall | 755.00 | 685.00 |
| Net GEX 0DTE | $113.42M | -$257.86M |
| Net GEX all | -$2.59B | -$2.08B |
| Vol-adj net 0DTE | $56.21B | $14.09B |
| Vol-adj net all | $54.89B | $12.12B |
| Missing greeks | 351/882 | 285/848 |
| OI used | 1067904 | 902998 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
