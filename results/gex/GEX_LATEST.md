# GEX latest

2026-10-26 12:06:19 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 765.00, 0.41 pts (0.05%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 715.00, 2.13 pts (0.30%) away.

SPY top |GEX| strikes: 766.00 ($1.52B), 767.00 ($1.20B), 762.00 ($632.04M).
QQQ top |GEX| strikes: 710.00 ($90.24M), 700.00 ($58.37M), 722.00 ($55.30M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 765.41 | 712.87 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 765.00 | 715.00 |
| 0DTE put wall | 766.00 | 710.00 |
| Net GEX 0DTE | -$2.22B | -$130.39M |
| Net GEX all | -$3.87B | -$281.57M |
| Vol-adj net 0DTE | $33.67B | $15.38B |
| Vol-adj net all | $34.70B | $15.96B |
| Missing greeks | 330/796 | 288/756 |
| OI used | 729363 | 380158 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
