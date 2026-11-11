# GEX latest

2026-11-11 14:16:50 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 3.73 pts (0.49%); nearest wall is the call wall at 760.00, 0.33 pts (0.04%) away.
QQQ: spot above the 0DTE flip by 13.20 pts (1.91%); nearest wall is the put wall at 695.00, 2.36 pts (0.34%) away.

SPY top |GEX| strikes: 760.00 ($537.59M), 770.00 ($269.84M), 765.00 ($261.40M).
QQQ top |GEX| strikes: 696.00 ($199.18M), 700.00 ($194.16M), 685.00 ($156.36M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 760.33 | 692.64 |
| 0DTE flip | 756.60 | 679.44 |
| All-expiry flip | 761.67 | 692.63 |
| 0DTE call wall | 760.00 | 690.00 |
| 0DTE put wall | 763.00 | 695.00 |
| Net GEX 0DTE | $723.39M | $529.40M |
| Net GEX all | $1.58B | $1.12B |
| Vol-adj net 0DTE | $134.19B | $32.97B |
| Vol-adj net all | $139.79B | $34.83B |
| Missing greeks | 337/912 | 314/962 |
| OI used | 1092944 | 714375 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
