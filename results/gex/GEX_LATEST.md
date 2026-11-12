# GEX latest

2026-11-12 10:45:15 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 4.67 pts (0.62%); nearest wall is the call wall at 759.00, 0.76 pts (0.10%) away.
QQQ: spot above the 0DTE flip by 7.34 pts (1.07%); nearest wall is the call wall at 685.00, 2.16 pts (0.31%) away.

SPY top |GEX| strikes: 759.00 ($285.88M), 762.00 ($264.20M), 745.00 ($255.46M).
QQQ top |GEX| strikes: 685.00 ($147.68M), 700.00 ($142.39M), 696.00 ($140.82M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 758.24 | 687.16 |
| 0DTE flip | 753.57 | 679.82 |
| All-expiry flip | 763.11 | 695.72 |
| 0DTE call wall | 759.00 | 685.00 |
| 0DTE put wall | 760.00 | 680.00 |
| Net GEX 0DTE | $776.76M | $323.01M |
| Net GEX all | $1.19B | $479.64M |
| Vol-adj net 0DTE | $15.64B | $5.38B |
| Vol-adj net all | $16.69B | $5.63B |
| Missing greeks | 342/896 | 313/968 |
| OI used | 1123000 | 681421 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
