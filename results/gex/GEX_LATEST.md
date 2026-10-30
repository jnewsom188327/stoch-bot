# GEX latest

2026-10-30 13:00:01 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 41.14 pts (5.44%); nearest wall is the put wall at 755.00, 0.78 pts (0.10%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 690.00, 0.54 pts (0.08%) away.

SPY top |GEX| strikes: 755.00 ($2.31B), 750.00 ($1.50B), 760.00 ($1.05B).
QQQ top |GEX| strikes: 690.00 ($2.63B), 695.00 ($547.90M), 700.00 ($510.10M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 755.78 | 690.54 |
| 0DTE flip | 714.64 |  |
| All-expiry flip | 706.14 |  |
| 0DTE call wall | 760.00 | 695.00 |
| 0DTE put wall | 755.00 | 690.00 |
| Net GEX 0DTE | -$6.83B | -$5.69B |
| Net GEX all | -$8.37B | -$6.39B |
| Vol-adj net 0DTE | -$63.37B | -$21.91B |
| Vol-adj net all | -$66.18B | -$22.09B |
| Missing greeks | 407/890 | 313/858 |
| OI used | 1648945 | 1106981 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
