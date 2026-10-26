# GEX latest

2026-10-26 15:27:04 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 765.00, 0.40 pts (0.05%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 715.00, 1.90 pts (0.27%) away.

SPY top |GEX| strikes: 766.00 ($2.76B), 767.00 ($1.35B), 755.00 ($488.87M).
QQQ top |GEX| strikes: 722.00 ($133.81M), 710.00 ($78.16M), 715.00 ($65.21M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 765.40 | 713.10 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 765.00 | 715.00 |
| 0DTE put wall | 766.00 | 722.00 |
| Net GEX 0DTE | -$3.05B | -$107.85M |
| Net GEX all | -$4.84B | -$233.70M |
| Vol-adj net 0DTE | $23.80B | $21.16B |
| Vol-adj net all | $23.26B | $21.44B |
| Missing greeks | 344/796 | 343/756 |
| OI used | 729363 | 380158 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
