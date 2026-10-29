# GEX latest

2026-10-29 14:38:17 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 768.00, 0.91 pts (0.12%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 714.00, 1.40 pts (0.20%) away.

SPY top |GEX| strikes: 765.00 ($1.54B), 760.00 ($560.30M), 755.00 ($348.86M).
QQQ top |GEX| strikes: 700.00 ($468.51M), 710.00 ($380.93M), 715.00 ($275.69M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 767.09 | 712.60 |
| 0DTE flip |  |  |
| All-expiry flip | 703.90 |  |
| 0DTE call wall | 768.00 | 715.00 |
| 0DTE put wall | 765.00 | 714.00 |
| Net GEX 0DTE | -$308.57M | -$528.72M |
| Net GEX all | -$2.89B | -$2.84B |
| Vol-adj net 0DTE | -$38.83B | -$14.59B |
| Vol-adj net all | -$44.92B | -$18.48B |
| Missing greeks | 341/880 | 332/846 |
| OI used | 1712665 | 1179706 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
