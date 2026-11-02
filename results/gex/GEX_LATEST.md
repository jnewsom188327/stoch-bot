# GEX latest

2026-11-02 09:50:42 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 760.00, 0.00 pts (0.00%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 0.23 pts (0.03%) away.

SPY top |GEX| strikes: 767.00 ($658.60M), 760.00 ($440.48M), 755.00 ($290.24M).
QQQ top |GEX| strikes: 695.00 ($337.19M), 700.00 ($177.73M), 680.00 ($157.35M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 760.00 | 694.77 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 770.00 | 695.00 |
| 0DTE put wall | 760.00 | 695.00 |
| Net GEX 0DTE | -$1.15B | -$526.33M |
| Net GEX all | -$2.60B | -$981.93M |
| Vol-adj net 0DTE | -$189.10M | -$193.23M |
| Vol-adj net all | -$1.96B | -$604.61M |
| Missing greeks | 266/650 | 341/746 |
| OI used | 430259 | 313176 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
