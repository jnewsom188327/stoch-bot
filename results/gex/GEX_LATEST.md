# GEX latest

2026-10-29 09:46:55 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 770.00, 0.74 pts (0.10%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 718.00, 3.26 pts (0.46%) away.

SPY top |GEX| strikes: 765.00 ($1.16B), 760.00 ($426.90M), 775.00 ($351.22M).
QQQ top |GEX| strikes: 700.00 ($403.45M), 710.00 ($304.56M), 715.00 ($243.27M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 769.26 | 714.74 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 768.00 | 725.00 |
| 0DTE put wall | 770.00 | 718.00 |
| Net GEX 0DTE | -$90.87M | -$346.52M |
| Net GEX all | -$1.39B | -$2.22B |
| Vol-adj net 0DTE | $6.79M | -$760.61M |
| Vol-adj net all | -$1.32B | -$2.74B |
| Missing greeks | 353/884 | 314/850 |
| OI used | 1714109 | 1182529 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
