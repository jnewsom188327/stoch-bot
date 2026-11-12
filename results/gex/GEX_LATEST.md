# GEX latest

2026-11-12 15:58:42 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 3.87 pts (0.51%); nearest wall is the call wall at 757.00, 0.02 pts (0.00%) away.
QQQ: spot above the 0DTE flip by 9.08 pts (1.32%); the call wall and the put wall are the same distance, 1.96 pts (0.28%) away.

SPY top |GEX| strikes: 760.00 ($315.30M), 759.00 ($299.52M), 745.00 ($277.33M).
QQQ top |GEX| strikes: 696.00 ($145.32M), 700.00 ($142.00M), 685.00 ($130.66M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 756.98 | 688.04 |
| 0DTE flip | 753.11 | 678.96 |
| All-expiry flip | 762.14 | 695.09 |
| 0DTE call wall | 757.00 | 690.00 |
| 0DTE put wall | 755.00 | 690.00 |
| Net GEX 0DTE | $886.80M | $380.05M |
| Net GEX all | $924.85M | $546.48M |
| Vol-adj net 0DTE | -$118.66B | -$22.03B |
| Vol-adj net all | -$122.98B | -$22.66B |
| Missing greeks | 383/896 | 348/962 |
| OI used | 1123000 | 681377 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
