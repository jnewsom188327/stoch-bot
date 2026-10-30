# GEX latest

2026-10-30 11:28:01 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 64.48 pts (8.50%); the call wall and the put wall are the same distance, 1.32 pts (0.17%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 695.00, 0.27 pts (0.04%) away.

SPY top |GEX| strikes: 760.00 ($1.74B), 755.00 ($1.45B), 765.00 ($1.06B).
QQQ top |GEX| strikes: 690.00 ($1.49B), 700.00 ($1.06B), 695.00 ($793.29M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 758.68 | 695.27 |
| 0DTE flip | 694.20 |  |
| All-expiry flip | 692.55 |  |
| 0DTE call wall | 760.00 | 695.00 |
| 0DTE put wall | 760.00 | 690.00 |
| Net GEX 0DTE | -$5.98B | -$5.04B |
| Net GEX all | -$7.58B | -$5.74B |
| Vol-adj net 0DTE | -$27.37B | -$2.70B |
| Vol-adj net all | -$29.00B | -$2.77B |
| Missing greeks | 401/892 | 326/884 |
| OI used | 1726862 | 1124902 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
