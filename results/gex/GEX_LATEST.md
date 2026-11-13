# GEX latest

2026-11-13 09:49:52 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 4.38 pts (0.58%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 1.89 pts (0.28%) away.

SPY top |GEX| strikes: 755.00 ($877.06M), 760.00 ($669.42M), 763.00 ($398.86M).
QQQ top |GEX| strikes: 685.00 ($450.55M), 680.00 ($126.49M), 678.00 ($96.05M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 755.62 | 683.11 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 760.00 | 685.00 |
| 0DTE put wall | 760.00 | 685.00 |
| Net GEX 0DTE | -$2.31B | -$934.61M |
| Net GEX all | -$2.64B | -$870.39M |
| Vol-adj net 0DTE | -$4.48B | -$1.27B |
| Vol-adj net all | -$4.85B | -$1.21B |
| Missing greeks | 304/872 | 347/986 |
| OI used | 1133501 | 751637 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
