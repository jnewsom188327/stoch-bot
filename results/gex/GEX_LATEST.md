# GEX latest

2026-10-29 15:29:20 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 768.00, 0.22 pts (0.03%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 714.00, 0.34 pts (0.05%) away.

SPY top |GEX| strikes: 765.00 ($1.47B), 760.00 ($462.22M), 770.00 ($357.31M).
QQQ top |GEX| strikes: 700.00 ($397.14M), 710.00 ($388.48M), 715.00 ($323.88M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 768.22 | 713.66 |
| 0DTE flip |  |  |
| All-expiry flip | 692.26 |  |
| 0DTE call wall | 768.00 | 715.00 |
| 0DTE put wall | 770.00 | 714.00 |
| Net GEX 0DTE | -$137.68M | -$536.49M |
| Net GEX all | -$2.36B | -$2.77B |
| Vol-adj net 0DTE | -$6.05B | -$12.27B |
| Vol-adj net all | -$10.33B | -$16.32B |
| Missing greeks | 391/886 | 344/852 |
| OI used | 1714928 | 1184452 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
