# GEX latest

2026-10-26 12:47:42 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 765.00, 0.58 pts (0.08%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 1.37 pts (0.19%) away.

SPY top |GEX| strikes: 766.00 ($1.31B), 767.00 ($1.14B), 762.00 ($853.06M).
QQQ top |GEX| strikes: 722.00 ($123.74M), 710.00 ($100.23M), 700.00 ($63.25M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 764.42 | 711.37 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 765.00 | 710.00 |
| 0DTE put wall | 766.00 | 710.00 |
| Net GEX 0DTE | -$2.76B | -$287.44M |
| Net GEX all | -$4.46B | -$465.31M |
| Vol-adj net 0DTE | $6.80B | $10.45B |
| Vol-adj net all | $6.50B | $10.42B |
| Missing greeks | 327/796 | 314/756 |
| OI used | 729363 | 380158 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
