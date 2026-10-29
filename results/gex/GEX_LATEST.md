# GEX latest

2026-10-29 13:14:30 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 768.00, 0.25 pts (0.03%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 714.00, 0.10 pts (0.01%) away.

SPY top |GEX| strikes: 765.00 ($1.45B), 760.00 ($466.61M), 770.00 ($311.50M).
QQQ top |GEX| strikes: 700.00 ($405.56M), 710.00 ($356.47M), 715.00 ($293.74M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 768.25 | 713.90 |
| 0DTE flip |  |  |
| All-expiry flip | 709.60 |  |
| 0DTE call wall | 768.00 | 715.00 |
| 0DTE put wall | 770.00 | 714.00 |
| Net GEX 0DTE | -$171.17M | -$500.40M |
| Net GEX all | -$2.05B | -$2.60B |
| Vol-adj net 0DTE | -$9.87B | -$7.07B |
| Vol-adj net all | -$13.68B | -$10.05B |
| Missing greeks | 346/886 | 357/852 |
| OI used | 1714928 | 1184452 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
