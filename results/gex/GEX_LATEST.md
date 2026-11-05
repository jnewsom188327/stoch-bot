# GEX latest

2026-11-05 11:49:56 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 745.00, 2.69 pts (0.36%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 670.00, 11.98 pts (1.82%) away.

SPY top |GEX| strikes: 750.00 ($647.00M), 735.00 ($638.12M), 740.00 ($485.58M).
QQQ top |GEX| strikes: 675.00 ($316.00M), 680.00 ($188.33M), 670.00 ($183.04M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 742.31 | 658.02 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 745.00 | 690.00 |
| 0DTE put wall | 735.00 | 670.00 |
| Net GEX 0DTE | -$756.43M | -$323.82M |
| Net GEX all | -$3.84B | -$1.92B |
| Vol-adj net 0DTE | -$32.95B | -$2.53B |
| Vol-adj net all | -$40.16B | -$5.18B |
| Missing greeks | 330/878 | 209/692 |
| OI used | 916970 | 852080 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
