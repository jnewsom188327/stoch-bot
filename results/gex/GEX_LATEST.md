# GEX latest

2026-11-09 15:21:49 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 0.12 pts (0.02%) away.
QQQ: spot above the 0DTE flip by 21.83 pts (3.21%); the call wall and the put wall are the same distance, 1.03 pts (0.15%) away.

SPY top |GEX| strikes: 755.00 ($580.66M), 756.00 ($154.67M), 757.00 ($109.78M).
QQQ top |GEX| strikes: 680.00 ($217.30M), 672.00 ($42.98M), 675.00 ($30.34M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 755.12 | 681.03 |
| 0DTE flip |  | 659.20 |
| All-expiry flip | 754.04 | 679.09 |
| 0DTE call wall | 755.00 | 680.00 |
| 0DTE put wall | 755.00 | 680.00 |
| Net GEX 0DTE | -$214.42M | $238.27M |
| Net GEX all | $222.94M | $383.72M |
| Vol-adj net 0DTE | $115.22B | $43.70B |
| Vol-adj net all | $120.00B | $44.35B |
| Missing greeks | 389/904 | 381/990 |
| OI used | 659340 | 344683 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
