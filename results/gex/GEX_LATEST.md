# GEX latest

2026-11-06 12:14:23 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 740.00, 0.92 pts (0.12%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 660.00, 0.82 pts (0.12%) away.

SPY top |GEX| strikes: 740.00 ($1.03B), 735.00 ($758.31M), 745.00 ($366.62M).
QQQ top |GEX| strikes: 660.00 ($330.01M), 664.00 ($144.89M), 665.00 ($137.55M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 739.08 | 659.18 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 745.00 | 655.00 |
| 0DTE put wall | 740.00 | 660.00 |
| Net GEX 0DTE | -$3.56B | -$1.32B |
| Net GEX all | -$4.74B | -$1.70B |
| Vol-adj net 0DTE | $6.76B | -$2.49B |
| Vol-adj net all | $6.37B | -$2.74B |
| Missing greeks | 313/884 | 290/1026 |
| OI used | 986699 | 926109 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
