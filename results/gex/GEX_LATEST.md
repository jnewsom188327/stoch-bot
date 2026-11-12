# GEX latest

2026-11-12 11:43:19 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 7.08 pts (0.93%); the call wall and the put wall are the same distance, 0.33 pts (0.04%) away.
QQQ: spot above the 0DTE flip by 17.67 pts (2.56%); the call wall and the put wall are the same distance, 0.51 pts (0.07%) away.

SPY top |GEX| strikes: 762.00 ($321.20M), 765.00 ($301.04M), 759.00 ($281.41M).
QQQ top |GEX| strikes: 700.00 ($209.31M), 696.00 ($183.74M), 685.00 ($142.20M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 760.33 | 690.51 |
| 0DTE flip | 753.25 | 672.84 |
| All-expiry flip | 761.43 | 694.22 |
| 0DTE call wall | 760.00 | 690.00 |
| 0DTE put wall | 760.00 | 690.00 |
| Net GEX 0DTE | $929.21M | $423.67M |
| Net GEX all | $1.99B | $884.44M |
| Vol-adj net 0DTE | $52.84B | $18.76B |
| Vol-adj net all | $56.78B | $20.05B |
| Missing greeks | 321/904 | 300/952 |
| OI used | 1124489 | 674456 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
