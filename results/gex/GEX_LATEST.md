# GEX latest

2026-11-20 15:51:56 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 1.07 pts (0.15%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 1.12 pts (0.18%) away.

SPY top |GEX| strikes: 690.00 ($1.28B), 700.00 ($826.78M), 695.00 ($375.68M).
QQQ top |GEX| strikes: 610.00 ($409.55M), 600.00 ($280.14M), 625.00 ($244.08M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 691.07 | 611.12 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 690.00 | 610.00 |
| 0DTE put wall | 690.00 | 610.00 |
| Net GEX 0DTE | -$3.16B | -$2.05B |
| Net GEX all | -$3.62B | -$2.24B |
| Vol-adj net 0DTE | -$92.97B | -$31.12B |
| Vol-adj net all | -$94.78B | -$32.07B |
| Missing greeks | 222/752 | 280/852 |
| OI used | 1856193 | 861558 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
