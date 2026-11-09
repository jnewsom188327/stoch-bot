# GEX latest

2026-11-09 09:56:17 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 750.00, 2.26 pts (0.30%) away.
QQQ: spot above the 0DTE flip by 12.83 pts (1.91%); nearest wall is the call wall at 670.00, 2.65 pts (0.39%) away.

SPY top |GEX| strikes: 750.00 ($166.40M), 745.00 ($102.00M), 734.00 ($91.52M).
QQQ top |GEX| strikes: 670.00 ($65.41M), 672.00 ($62.22M), 680.00 ($53.44M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 747.74 | 672.65 |
| 0DTE flip |  | 659.82 |
| All-expiry flip | 767.20 | 664.89 |
| 0DTE call wall | 750.00 | 670.00 |
| 0DTE put wall | 745.00 | 680.00 |
| Net GEX 0DTE | -$30.06M | $305.94M |
| Net GEX all | $162.06M | $353.22M |
| Vol-adj net 0DTE | $7.95B | $3.18B |
| Vol-adj net all | $8.79B | $3.37B |
| Missing greeks | 345/896 | 322/1030 |
| OI used | 668222 | 333360 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
