# GEX latest

2026-11-04 14:07:56 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot below the 0DTE flip by 4.42 pts (0.57%); nearest wall is the call wall at 770.00, 1.42 pts (0.18%) away.
QQQ: spot above the 0DTE flip by 0.79 pts (0.11%); nearest wall is the put wall at 695.00, 0.18 pts (0.03%) away.

SPY top |GEX| strikes: 767.00 ($773.00M), 770.00 ($725.83M), 775.00 ($309.95M).
QQQ top |GEX| strikes: 680.00 ($304.51M), 713.00 ($278.39M), 675.00 ($271.48M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 768.58 | 695.18 |
| 0DTE flip | 773.00 | 694.39 |
| All-expiry flip | 774.66 |  |
| 0DTE call wall | 770.00 | 694.00 |
| 0DTE put wall | 767.00 | 695.00 |
| Net GEX 0DTE | $149.30M | $134.52M |
| Net GEX all | $737.98M | -$1.77B |
| Vol-adj net 0DTE | $89.37B | $9.29B |
| Vol-adj net all | $93.46B | $8.60B |
| Missing greeks | 403/902 | 300/840 |
| OI used | 1099520 | 1018743 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
