# GEX latest

2026-11-04 14:59:04 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 1.02 pts (0.13%); nearest wall is the put wall at 767.00, 0.26 pts (0.03%) away.
QQQ: spot below the 0DTE flip by 1.41 pts (0.20%); nearest wall is the call wall at 694.00, 1.46 pts (0.21%) away.

SPY top |GEX| strikes: 767.00 ($1.52B), 770.00 ($624.60M), 765.00 ($442.79M).
QQQ top |GEX| strikes: 680.00 ($357.50M), 675.00 ($320.69M), 691.00 ($249.37M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 767.26 | 692.54 |
| 0DTE flip | 766.24 | 693.95 |
| All-expiry flip |  |  |
| 0DTE call wall | 765.00 | 694.00 |
| 0DTE put wall | 767.00 | 690.00 |
| Net GEX 0DTE | -$556.26M | $90.62M |
| Net GEX all | -$156.27M | -$1.94B |
| Vol-adj net 0DTE | $4.69B | -$36.53B |
| Vol-adj net all | $6.17B | -$38.69B |
| Missing greeks | 356/894 | 290/836 |
| OI used | 1099225 | 1022582 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
