# GEX latest

2026-11-06 12:56:10 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 1.40 pts (0.19%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 655.00, 0.58 pts (0.09%) away.

SPY top |GEX| strikes: 735.00 ($921.21M), 740.00 ($800.68M), 730.00 ($317.36M).
QQQ top |GEX| strikes: 660.00 ($267.09M), 650.00 ($190.89M), 675.00 ($172.54M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 736.40 | 655.58 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 735.00 | 655.00 |
| 0DTE put wall | 735.00 | 660.00 |
| Net GEX 0DTE | -$3.36B | -$1.57B |
| Net GEX all | -$4.53B | -$1.96B |
| Vol-adj net 0DTE | -$17.27B | -$13.72B |
| Vol-adj net all | -$18.40B | -$14.26B |
| Missing greeks | 319/888 | 270/994 |
| OI used | 986063 | 884439 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
