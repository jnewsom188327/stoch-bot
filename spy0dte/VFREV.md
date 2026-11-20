# SPY 0DTE Public Vix Fix bot ("vfrev")

The **Public** account's own strategy. It is separate from the Robinhood dot bot and never touches its settings, variables, state or files.
Workflow **SPY 0DTE Public Vix Fix** (`.github/workflows/spy0dte_public_vf.yml`) · code `vfbot.js` (minute loop) + `vfrev.js` (rules) · files in `spy0dte/vfrev/` (state.json, logs/, summaries/, trades.csv).

**DRY RUN** unless the repo variable **`SPY0DTE_PUBLIC_VF_LIVE`** = `yes`. Orders go only to Public (`SPY0DTE_LIVE` / `SPY0DTE_BROKER` are ignored).

## Rules
- **Marks:** pane arrows only (SPY pane, call-chart pane, put-chart pane), from the same live marks code (`marks.js`).
- **Take a mark only if ALL are true** (SPY 1-minute bars from 9:30; i = mark bar, d = +1 call / −1 put; no marks before 10:01):
  1. trend line **against** the trade (tw ≠ 1)
  2. Vix Fix stretch on your side hit **80+** in bars i−9..i. Calls (fear): wvf = (highest close of last 22 − low) / that close × 100, F = wvf / max(wvf, last 50) × 100. Puts (greed): wvs = (high − lowest close of last 22) / that close × 100, G = wvs / max(wvs, last 50) × 100
  3. ran hard: d × (close[i] − close[i−15]) ≤ −1.50
  4. stalled: no new day low (calls) / high (puts) in bars i−4..i vs everything before
  5. shrinking: average |close−open| of bars i−2..i < 0.8 × the average of bars i−12..i−3
  6. before 1:00 PM
- **Contract:** 0DTE, 1 strike in the money (2 strikes in from the first-out strike: calls K−2, puts K+2). Skip under $0.80, spread over 10%, quote over 30 s old.
- **Entry / size / stop / shutoffs:** same as the main bot: limit 5% under mid, cancelled after 5 min, full port of the Public account (capped at the bot's own money), −75% stop at Public, day shutoffs and the 2-of-10 review hold.
- **Exits:** +20% sell half (1 contract: all), stop to breakeven; rest out at minute 15; 120-min max; flat by 3:08.

## Tests (no key needed)
- `node spy0dte/replay_vfrev.js` — every `results/bars_*.json` through the vfrev engine from $1,000 (`why` as an argument lists every pane arrow and why it was taken or skipped).
- `node spy0dte/test_vfrev_mock.js 2026-11-19 dry|live` — the full vfbot.js against a fake Public on a fast clock.
