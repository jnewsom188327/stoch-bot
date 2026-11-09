# GEX latest

2026-11-09 13:30:24 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot below the 0DTE flip by 2.14 pts (0.28%); nearest wall is the call wall at 750.00, 2.28 pts (0.30%) away.
QQQ: spot above the 0DTE flip by 18.05 pts (2.67%); nearest wall is the put wall at 675.00, 1.84 pts (0.27%) away.

SPY top |GEX| strikes: 755.00 ($266.57M), 750.00 ($217.14M), 740.00 ($71.25M).
QQQ top |GEX| strikes: 680.00 ($209.51M), 672.00 ($64.84M), 674.00 ($62.67M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 752.28 | 676.84 |
| 0DTE flip | 754.42 | 658.79 |
| All-expiry flip | 754.94 | 662.92 |
| 0DTE call wall | 750.00 | 680.00 |
| 0DTE put wall | 755.00 | 675.00 |
| Net GEX 0DTE | $74.40M | $501.32M |
| Net GEX all | $449.09M | $591.49M |
| Vol-adj net 0DTE | $78.46B | $11.17B |
| Vol-adj net all | $81.90B | $11.27B |
| Missing greeks | 367/896 | 363/1006 |
| OI used | 658564 | 345001 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
