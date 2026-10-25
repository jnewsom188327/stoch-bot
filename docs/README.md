# 0DTE scalp on real option prices

Run this from your phone. It downloads old prices and writes a report. It does not place a trade.

1. Open this repo on GitHub.
2. Tap **Actions**.
3. Tap **0DTE scalp on real option prices**.
4. Tap **Run workflow**.

Use a fresh **Run workflow**. Do not tap **Re-run**. Re-run reuses the old inputs.

Example for a high-VIX afternoon scalp. The 15% target is already in the exit grid. Leave `vix_max` empty.

- vix_min: `16`
- strikes: `1otm,atm`
- premium_min: `0.45`
- premium_max: `0.80`
- first_entry: `13:00`
- last_entry: `15:00`

`vix_min` uses the prior trading day's VIX close (yesterday, or Friday before a Monday). Today's close is not used. A day is traded only when that close is at least 16. The same days are used for the signals, the paired random controls, and the reference random book.
