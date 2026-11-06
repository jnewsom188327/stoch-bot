# GEX latest

2026-11-06 14:34:14 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 739.00, 1.51 pts (0.20%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 660.00, 1.96 pts (0.30%) away.

SPY top |GEX| strikes: 735.00 ($1.23B), 740.00 ($1.22B), 750.00 ($458.11M).
QQQ top |GEX| strikes: 660.00 ($512.69M), 655.00 ($190.83M), 675.00 ($120.54M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 737.49 | 658.04 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 739.00 | 655.00 |
| 0DTE put wall | 735.00 | 660.00 |
| Net GEX 0DTE | -$4.47B | -$1.43B |
| Net GEX all | -$5.61B | -$1.80B |
| Vol-adj net 0DTE | -$31.64B | -$14.24B |
| Vol-adj net all | -$32.91B | -$14.79B |
| Missing greeks | 352/890 | 312/1010 |
| OI used | 987598 | 888606 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
