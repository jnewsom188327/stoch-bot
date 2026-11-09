# GEX latest

2026-11-09 12:42:44 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot below the 0DTE flip by 2.22 pts (0.29%); nearest wall is the call wall at 750.00, 2.07 pts (0.28%) away.
QQQ: spot above the 0DTE flip by 17.59 pts (2.60%); the call wall and the put wall are the same distance, 3.01 pts (0.45%) away.

SPY top |GEX| strikes: 755.00 ($261.42M), 750.00 ($226.74M), 745.00 ($73.26M).
QQQ top |GEX| strikes: 680.00 ($111.78M), 672.00 ($63.17M), 674.00 ($60.48M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 752.07 | 676.99 |
| 0DTE flip | 754.29 | 659.39 |
| All-expiry flip | 749.73 | 669.23 |
| 0DTE call wall | 750.00 | 680.00 |
| 0DTE put wall | 755.00 | 680.00 |
| Net GEX 0DTE | $30.68M | $348.34M |
| Net GEX all | $422.85M | $438.83M |
| Vol-adj net 0DTE | $72.45B | $21.65B |
| Vol-adj net all | $75.68B | $21.89B |
| Missing greeks | 338/896 | 355/1006 |
| OI used | 658564 | 345001 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
