# GEX latest

2026-11-13 12:20:28 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 750.00, 0.99 pts (0.13%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 3.62 pts (0.54%) away.

SPY top |GEX| strikes: 755.00 ($658.61M), 745.00 ($624.25M), 753.00 ($377.79M).
QQQ top |GEX| strikes: 685.00 ($201.02M), 678.00 ($166.28M), 680.00 ($144.18M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 750.99 | 676.38 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 750.00 | 680.00 |
| 0DTE put wall | 755.00 | 680.00 |
| Net GEX 0DTE | -$2.20B | -$1.08B |
| Net GEX all | -$2.72B | -$1.18B |
| Vol-adj net 0DTE | -$37.50B | -$7.17B |
| Vol-adj net all | -$37.76B | -$7.63B |
| Missing greeks | 315/872 | 349/1008 |
| OI used | 1146816 | 754328 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
