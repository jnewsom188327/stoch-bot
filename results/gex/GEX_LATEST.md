# GEX latest

2026-11-12 15:13:29 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 3.88 pts (0.51%); nearest wall is the call wall at 759.00, 1.68 pts (0.22%) away.
QQQ: spot above the 0DTE flip by 30.51 pts (4.44%); the call wall and the put wall are the same distance, 2.18 pts (0.32%) away.

SPY top |GEX| strikes: 759.00 ($364.16M), 760.00 ($312.51M), 745.00 ($260.05M).
QQQ top |GEX| strikes: 696.00 ($139.87M), 700.00 ($135.54M), 685.00 ($113.20M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 757.32 | 687.18 |
| 0DTE flip | 753.43 | 656.67 |
| All-expiry flip | 762.55 | 694.18 |
| 0DTE call wall | 759.00 | 685.00 |
| 0DTE put wall | 755.00 | 685.00 |
| Net GEX 0DTE | $859.15M | $422.71M |
| Net GEX all | $966.42M | $575.73M |
| Vol-adj net 0DTE | -$76.46B | -$21.74B |
| Vol-adj net all | -$79.41B | -$22.13B |
| Missing greeks | 363/896 | 302/968 |
| OI used | 1123000 | 681421 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
