# GEX latest

2026-11-02 15:06:55 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 755.00, 0.34 pts (0.05%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 685.00, 0.88 pts (0.13%) away.

SPY top |GEX| strikes: 755.00 ($467.38M), 767.00 ($441.73M), 757.00 ($260.30M).
QQQ top |GEX| strikes: 680.00 ($286.29M), 685.00 ($266.93M), 690.00 ($120.19M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 755.34 | 685.88 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 760.00 | 725.00 |
| 0DTE put wall | 755.00 | 685.00 |
| Net GEX 0DTE | -$1.34B | -$425.22M |
| Net GEX all | -$2.78B | -$960.61M |
| Vol-adj net 0DTE | -$105.54B | -$36.34B |
| Vol-adj net all | -$111.19B | -$38.19B |
| Missing greeks | 339/648 | 325/698 |
| OI used | 430406 | 317664 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
