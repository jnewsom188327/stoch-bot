# GEX latest

2026-11-04 10:39:18 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot below the 0DTE flip by 5.62 pts (0.73%); nearest wall is the put wall at 767.00, 0.17 pts (0.02%) away.
QQQ: spot below the 0DTE flip by 9.54 pts (1.37%); the call wall and the put wall are the same distance, 2.43 pts (0.35%) away.

SPY top |GEX| strikes: 770.00 ($493.00M), 767.00 ($492.06M), 750.00 ($343.94M).
QQQ top |GEX| strikes: 713.00 ($348.10M), 680.00 ($273.68M), 675.00 ($255.17M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 767.17 | 697.57 |
| 0DTE flip | 772.79 | 707.11 |
| All-expiry flip | 779.31 |  |
| 0DTE call wall | 765.00 | 700.00 |
| 0DTE put wall | 767.00 | 700.00 |
| Net GEX 0DTE | $235.82M | $63.33M |
| Net GEX all | $393.80M | -$1.58B |
| Vol-adj net 0DTE | $19.09B | $7.50B |
| Vol-adj net all | $21.63B | $7.32B |
| Missing greeks | 336/894 | 288/856 |
| OI used | 1099225 | 1024877 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
