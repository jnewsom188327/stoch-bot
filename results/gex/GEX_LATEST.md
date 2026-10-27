# GEX latest

2026-10-27 11:15:37 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 770.00, 0.51 pts (0.07%) away.
QQQ: spot above the 0DTE flip by 4.93 pts (0.69%); nearest wall is the call wall at 719.00, 0.69 pts (0.10%) away.

SPY top |GEX| strikes: 755.00 ($1.45B), 767.00 ($1.19B), 765.00 ($690.35M).
QQQ top |GEX| strikes: 700.00 ($446.73M), 690.00 ($335.19M), 719.00 ($213.35M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 769.49 | 719.69 |
| 0DTE flip |  | 714.76 |
| All-expiry flip | 694.69 |  |
| 0DTE call wall | 770.00 | 719.00 |
| 0DTE put wall | 767.00 | 722.00 |
| Net GEX 0DTE | -$521.26M | $454.81M |
| Net GEX all | -$3.07B | -$1.12B |
| Vol-adj net 0DTE | $61.75B | $29.27B |
| Vol-adj net all | $61.32B | $28.35B |
| Missing greeks | 326/888 | 315/924 |
| OI used | 1957126 | 1231092 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
