# GEX latest

2026-10-30 10:40:16 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 55.12 pts (7.26%); the call wall and the put wall are the same distance, 0.53 pts (0.07%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 690.00, 6.49 pts (0.93%) away.

SPY top |GEX| strikes: 760.00 ($1.54B), 765.00 ($1.41B), 755.00 ($1.21B).
QQQ top |GEX| strikes: 690.00 ($1.22B), 700.00 ($1.13B), 695.00 ($671.55M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 759.47 | 696.49 |
| 0DTE flip | 704.35 |  |
| All-expiry flip |  |  |
| 0DTE call wall | 760.00 | 705.00 |
| 0DTE put wall | 760.00 | 690.00 |
| Net GEX 0DTE | -$6.41B | -$4.92B |
| Net GEX all | -$8.01B | -$5.60B |
| Vol-adj net 0DTE | -$16.63B | -$486.21M |
| Vol-adj net all | -$18.38B | -$963.66M |
| Missing greeks | 397/898 | 339/898 |
| OI used | 1737641 | 1123878 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
