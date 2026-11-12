# GEX latest

2026-11-12 12:34:22 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 4.29 pts (0.56%); the call wall and the put wall are the same distance, 1.14 pts (0.15%) away.
QQQ: spot above the 0DTE flip by 11.36 pts (1.65%); the call wall and the put wall are the same distance, 0.74 pts (0.11%) away.

SPY top |GEX| strikes: 762.00 ($356.38M), 765.00 ($334.49M), 761.00 ($302.70M).
QQQ top |GEX| strikes: 700.00 ($204.22M), 696.00 ($192.13M), 685.00 ($143.54M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 761.14 | 690.74 |
| 0DTE flip | 756.85 | 679.37 |
| All-expiry flip | 761.69 | 693.60 |
| 0DTE call wall | 760.00 | 690.00 |
| 0DTE put wall | 760.00 | 690.00 |
| Net GEX 0DTE | $945.02M | $430.86M |
| Net GEX all | $2.03B | $894.62M |
| Vol-adj net 0DTE | $68.84B | $20.78B |
| Vol-adj net all | $73.14B | $22.08B |
| Missing greeks | 367/896 | 346/952 |
| OI used | 1117964 | 674456 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
