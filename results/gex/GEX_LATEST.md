# GEX latest

2026-11-06 15:20:17 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 739.00, 1.28 pts (0.17%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 660.00, 1.68 pts (0.26%) away.

SPY top |GEX| strikes: 740.00 ($1.34B), 735.00 ($1.20B), 750.00 ($496.31M).
QQQ top |GEX| strikes: 660.00 ($605.45M), 655.00 ($189.96M), 675.00 ($169.36M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 737.72 | 658.32 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 739.00 | 655.00 |
| 0DTE put wall | 740.00 | 660.00 |
| Net GEX 0DTE | -$4.72B | -$1.41B |
| Net GEX all | -$5.77B | -$1.79B |
| Vol-adj net 0DTE | -$35.59B | -$14.21B |
| Vol-adj net all | -$36.86B | -$14.82B |
| Missing greeks | 393/890 | 333/1018 |
| OI used | 987598 | 894566 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
