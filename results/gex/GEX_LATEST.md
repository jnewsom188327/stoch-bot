# GEX latest

2026-10-28 09:44:14 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot below the 0DTE flip by 0.48 pts (0.06%); nearest wall is the call wall at 772.00, 1.40 pts (0.18%) away.
QQQ: spot above the 0DTE flip by 3.38 pts (0.47%); the call wall and the put wall are the same distance, 2.75 pts (0.38%) away.

SPY top |GEX| strikes: 765.00 ($870.88M), 755.00 ($817.52M), 780.00 ($474.76M).
QQQ top |GEX| strikes: 730.00 ($240.35M), 740.00 ($238.68M), 700.00 ($238.17M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 770.60 | 722.75 |
| 0DTE flip | 771.08 | 719.37 |
| All-expiry flip | 704.94 |  |
| 0DTE call wall | 772.00 | 720.00 |
| 0DTE put wall | 765.00 | 720.00 |
| Net GEX 0DTE | $569.69M | $331.65M |
| Net GEX all | -$615.61M | -$47.46M |
| Vol-adj net 0DTE | $2.66B | $1.84B |
| Vol-adj net all | $485.51M | $2.06B |
| Missing greeks | 303/886 | 315/888 |
| OI used | 1886450 | 1153756 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
