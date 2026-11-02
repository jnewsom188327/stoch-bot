# GEX latest

2026-11-02 13:24:27 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 1.51 pts (0.20%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 3.71 pts (0.54%) away.

SPY top |GEX| strikes: 767.00 ($576.25M), 760.00 ($559.48M), 755.00 ($345.55M).
QQQ top |GEX| strikes: 695.00 ($327.92M), 680.00 ($200.25M), 690.00 ($176.42M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 758.49 | 691.29 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 760.00 | 695.00 |
| 0DTE put wall | 760.00 | 695.00 |
| Net GEX 0DTE | -$1.46B | -$539.52M |
| Net GEX all | -$2.94B | -$1.04B |
| Vol-adj net 0DTE | -$37.36B | -$18.83B |
| Vol-adj net all | -$39.71B | -$19.21B |
| Missing greeks | 303/642 | 342/730 |
| OI used | 429826 | 319201 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
