# GEX latest

2026-10-30 09:48:21 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 51.42 pts (6.77%); nearest wall is the call wall at 762.00, 2.05 pts (0.27%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 690.00, 5.73 pts (0.82%) away.

SPY top |GEX| strikes: 765.00 ($1.55B), 760.00 ($1.50B), 755.00 ($1.11B).
QQQ top |GEX| strikes: 690.00 ($1.29B), 700.00 ($972.51M), 695.00 ($586.40M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 759.95 | 695.73 |
| 0DTE flip | 708.53 |  |
| All-expiry flip | 706.08 |  |
| 0DTE call wall | 762.00 | 705.00 |
| 0DTE put wall | 765.00 | 690.00 |
| Net GEX 0DTE | -$6.14B | -$4.54B |
| Net GEX all | -$7.74B | -$5.22B |
| Vol-adj net 0DTE | -$8.72B | -$4.90B |
| Vol-adj net all | -$10.52B | -$5.66B |
| Missing greeks | 376/898 | 342/890 |
| OI used | 1737641 | 1123254 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
