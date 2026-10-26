# GEX latest

2026-10-26 14:03:14 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 766.00, 0.36 pts (0.05%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 715.00, 1.38 pts (0.19%) away.

SPY top |GEX| strikes: 766.00 ($2.10B), 767.00 ($1.25B), 762.00 ($511.68M).
QQQ top |GEX| strikes: 722.00 ($120.49M), 710.00 ($70.96M), 715.00 ($65.96M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 765.64 | 713.62 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 765.00 | 715.00 |
| 0DTE put wall | 766.00 | 722.00 |
| Net GEX 0DTE | -$2.65B | -$89.01M |
| Net GEX all | -$4.31B | -$205.79M |
| Vol-adj net 0DTE | $43.21B | $24.53B |
| Vol-adj net all | $43.57B | $24.89B |
| Missing greeks | 332/796 | 307/756 |
| OI used | 729363 | 380158 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
