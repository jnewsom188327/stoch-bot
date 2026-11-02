# GEX latest

2026-11-02 10:41:14 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 765.00, 2.35 pts (0.31%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 695.00, 2.45 pts (0.35%) away.

SPY top |GEX| strikes: 767.00 ($748.26M), 760.00 ($410.88M), 765.00 ($372.56M).
QQQ top |GEX| strikes: 695.00 ($361.39M), 700.00 ($244.02M), 703.00 ($118.41M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 762.65 | 697.45 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 767.00 | 705.00 |
| 0DTE put wall | 765.00 | 695.00 |
| Net GEX 0DTE | -$1.10B | -$713.08M |
| Net GEX all | -$2.47B | -$1.13B |
| Vol-adj net 0DTE | $21.31B | $8.74B |
| Vol-adj net all | $22.20B | $8.82B |
| Missing greeks | 269/644 | 343/762 |
| OI used | 428456 | 314560 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
