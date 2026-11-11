# GEX latest

2026-11-11 11:28:16 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 2.62 pts (0.34%); the call wall and the put wall are the same distance, 0.91 pts (0.12%) away.
QQQ: spot above the 0DTE flip by 9.64 pts (1.39%); nearest wall is the call wall at 690.00, 1.99 pts (0.29%) away.

SPY top |GEX| strikes: 760.00 ($502.50M), 745.00 ($236.28M), 770.00 ($214.42M).
QQQ top |GEX| strikes: 700.00 ($194.46M), 696.00 ($189.20M), 685.00 ($143.65M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 759.09 | 691.99 |
| 0DTE flip | 756.47 | 682.35 |
| All-expiry flip | 764.24 | 693.24 |
| 0DTE call wall | 760.00 | 690.00 |
| 0DTE put wall | 760.00 | 695.00 |
| Net GEX 0DTE | $609.14M | $489.80M |
| Net GEX all | $1.14B | $1.03B |
| Vol-adj net 0DTE | $67.07B | $27.74B |
| Vol-adj net all | $70.36B | $29.35B |
| Missing greeks | 359/904 | 330/970 |
| OI used | 1090376 | 714652 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
