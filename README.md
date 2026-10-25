# stoch-bot

## 0DTE scalp on real option prices

Phone steps and the example inputs (vix_min 16, late-day 1otm): [docs/README.md](docs/README.md).

## Intraday GEX logger (log only)

`gex_logger.py` records dealer gamma exposure for SPY and QQQ about every five minutes during the regular session. It does not place orders and it does not change the trading bots.

The scheduled workflow commits the CSVs to the `gex-data` branch, never to `main`. Assumptions, the dollar-GEX formula, and the pre-declared analysis plan are in [docs/GEX.md](docs/GEX.md).

```bash
python3 gex_logger.py --dry-run --out /tmp/gex-dry
python3 -m unittest tests.test_gex
```
