# GEX latest

2026-10-28 11:25:17 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 0.71 pts (0.09%); nearest wall is the call wall at 772.00, 0.73 pts (0.09%) away.
QQQ: spot above the 0DTE flip by 2.98 pts (0.41%); the call wall and the put wall are the same distance, 2.15 pts (0.30%) away.

SPY top |GEX| strikes: 765.00 ($845.19M), 755.00 ($757.14M), 780.00 ($507.63M).
QQQ top |GEX| strikes: 730.00 ($240.05M), 700.00 ($239.96M), 740.00 ($233.34M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 771.27 | 722.15 |
| 0DTE flip | 770.56 | 719.17 |
| All-expiry flip |  |  |
| 0DTE call wall | 772.00 | 720.00 |
| 0DTE put wall | 765.00 | 720.00 |
| Net GEX 0DTE | $678.69M | $325.44M |
| Net GEX all | -$78.77M | -$133.84M |
| Vol-adj net 0DTE | $1.31B | $1.50B |
| Vol-adj net all | $456.16M | $901.13M |
| Missing greeks | 322/884 | 314/888 |
| OI used | 1884905 | 1176188 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
