# GEX latest

2026-11-11 13:16:18 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 3.92 pts (0.51%); nearest wall is the call wall at 760.00, 1.41 pts (0.19%) away.
QQQ: spot above the 0DTE flip by 5.37 pts (0.77%); the call wall and the put wall are the same distance, 0.61 pts (0.09%) away.

SPY top |GEX| strikes: 760.00 ($498.51M), 765.00 ($336.36M), 770.00 ($325.07M).
QQQ top |GEX| strikes: 700.00 ($232.58M), 696.00 ($231.90M), 703.00 ($138.02M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 761.41 | 694.39 |
| 0DTE flip | 757.49 | 689.02 |
| All-expiry flip | 761.78 | 694.38 |
| 0DTE call wall | 760.00 | 695.00 |
| 0DTE put wall | 763.00 | 695.00 |
| Net GEX 0DTE | $722.53M | $519.68M |
| Net GEX all | $1.83B | $1.21B |
| Vol-adj net 0DTE | $141.39B | $51.18B |
| Vol-adj net all | $148.06B | $53.72B |
| Missing greeks | 350/904 | 339/958 |
| OI used | 1087015 | 720175 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
