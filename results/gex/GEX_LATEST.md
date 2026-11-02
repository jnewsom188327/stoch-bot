# GEX latest

2026-11-02 12:32:54 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 1.23 pts (0.16%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 3.28 pts (0.47%) away.

SPY top |GEX| strikes: 767.00 ($619.62M), 760.00 ($476.26M), 755.00 ($339.51M).
QQQ top |GEX| strikes: 695.00 ($338.64M), 680.00 ($195.25M), 690.00 ($158.77M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 758.77 | 691.72 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 760.00 | 695.00 |
| 0DTE put wall | 760.00 | 695.00 |
| Net GEX 0DTE | -$1.47B | -$597.03M |
| Net GEX all | -$2.96B | -$1.08B |
| Vol-adj net 0DTE | -$15.55B | -$11.22B |
| Vol-adj net all | -$17.60B | -$11.56B |
| Missing greeks | 291/642 | 353/730 |
| OI used | 429826 | 319201 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
