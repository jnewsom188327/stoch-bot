# GEX latest

2026-10-30 13:37:00 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 48.08 pts (6.37%); nearest wall is the put wall at 755.00, 0.32 pts (0.04%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 690.00, 1.93 pts (0.28%) away.

SPY top |GEX| strikes: 755.00 ($2.41B), 750.00 ($1.98B), 760.00 ($837.81M).
QQQ top |GEX| strikes: 690.00 ($2.63B), 685.00 ($742.73M), 680.00 ($394.71M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 754.68 | 688.07 |
| 0DTE flip | 706.60 |  |
| All-expiry flip | 704.09 |  |
| 0DTE call wall | 760.00 | 695.00 |
| 0DTE put wall | 755.00 | 690.00 |
| Net GEX 0DTE | -$7.56B | -$5.30B |
| Net GEX all | -$9.03B | -$5.99B |
| Vol-adj net 0DTE | -$78.87B | -$29.38B |
| Vol-adj net all | -$82.10B | -$29.78B |
| Missing greeks | 419/896 | 350/844 |
| OI used | 1645981 | 1112014 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
