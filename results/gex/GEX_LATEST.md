# GEX latest

2026-11-06 13:39:36 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 739.00, 1.28 pts (0.17%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 655.00, 2.42 pts (0.37%) away.

SPY top |GEX| strikes: 740.00 ($1.11B), 735.00 ($1.02B), 730.00 ($234.20M).
QQQ top |GEX| strikes: 660.00 ($385.38M), 655.00 ($182.21M), 650.00 ($151.85M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 737.72 | 657.42 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 739.00 | 655.00 |
| 0DTE put wall | 740.00 | 660.00 |
| Net GEX 0DTE | -$3.51B | -$1.31B |
| Net GEX all | -$4.59B | -$1.68B |
| Vol-adj net 0DTE | -$14.58B | -$14.51B |
| Vol-adj net all | -$15.62B | -$15.04B |
| Missing greeks | 343/890 | 306/1010 |
| OI used | 987598 | 888606 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
