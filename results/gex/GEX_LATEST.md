# GEX latest

2026-11-17 15:52:30 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 730.00, 0.10 pts (0.01%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 652.00, 1.21 pts (0.19%) away.

SPY top |GEX| strikes: 725.00 ($742.03M), 730.00 ($738.25M), 720.00 ($469.06M).
QQQ top |GEX| strikes: 650.00 ($353.61M), 680.00 ($202.68M), 655.00 ($201.28M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 729.90 | 653.21 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 734.00 | 652.00 |
| 0DTE put wall | 730.00 | 655.00 |
| Net GEX 0DTE | -$408.02M | -$412.83M |
| Net GEX all | -$9.03B | -$2.66B |
| Vol-adj net 0DTE | -$78.11B | -$19.46B |
| Vol-adj net all | -$91.32B | -$22.38B |
| Missing greeks | 319/836 | 300/970 |
| OI used | 2195728 | 1418804 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
