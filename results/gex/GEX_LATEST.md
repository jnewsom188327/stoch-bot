# GEX latest

2026-11-03 14:38:10 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 4.61 pts (0.61%); nearest wall is the put wall at 755.00, 0.01 pts (0.00%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 685.00, 0.50 pts (0.07%) away.

SPY top |GEX| strikes: 740.00 ($686.27M), 755.00 ($520.49M), 750.00 ($421.36M).
QQQ top |GEX| strikes: 680.00 ($457.31M), 685.00 ($338.07M), 675.00 ($315.93M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 754.99 | 685.50 |
| 0DTE flip | 750.38 |  |
| All-expiry flip |  |  |
| 0DTE call wall | 756.00 | 686.00 |
| 0DTE put wall | 755.00 | 685.00 |
| Net GEX 0DTE | -$46.50M | -$391.68M |
| Net GEX all | -$2.94B | -$2.21B |
| Vol-adj net 0DTE | -$2.83B | -$15.66B |
| Vol-adj net all | -$4.88B | -$17.90B |
| Missing greeks | 379/888 | 271/840 |
| OI used | 1070754 | 899569 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
