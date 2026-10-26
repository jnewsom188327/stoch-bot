# GEX latest

2026-10-26 11:07:08 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 766.00, 1.21 pts (0.16%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 715.00, 0.50 pts (0.07%) away.

SPY top |GEX| strikes: 766.00 ($1.14B), 767.00 ($1.11B), 755.00 ($435.40M).
QQQ top |GEX| strikes: 710.00 ($69.68M), 735.00 ($60.87M), 700.00 ($50.38M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 767.21 | 714.50 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 765.00 | 715.00 |
| 0DTE put wall | 766.00 | 710.00 |
| Net GEX 0DTE | -$1.74B | -$96.07M |
| Net GEX all | -$3.02B | -$160.09M |
| Vol-adj net 0DTE | $52.14B | $18.40B |
| Vol-adj net all | $54.84B | $19.53B |
| Missing greeks | 303/788 | 281/764 |
| OI used | 725691 | 380969 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
