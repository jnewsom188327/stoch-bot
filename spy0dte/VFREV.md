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
  4. stalled: no new day low (calls) / high (puts) in the last **5 bars** (i−4..i) vs everything before
  5. shrinking: average |close−open| of bars i−2..i < 0.8 × the average of bars i−12..i−3
  6. before **2:00 PM**
- **Contract:** 0DTE, 1 strike in the money (2 strikes in from the first-out strike: calls K−2, puts K+2). Skip under $0.80, spread over 10%, quote over 30 s old.
- **Entry:** limit **3% under the mid** (main bot: 5%), cancelled after 5 min.
- **Size / stop / shutoffs:** full port of the Public account (capped at the bot's own money), −75% stop at Public, the main bot's day shutoffs.
- **Safety brake** (replaces the 2-of-10 review hold): after a trade that loses 25% or more, the bot trades on **paper only** (no orders) until 5 paper trades in a row win; after a −75% stop it trades **half port** until its money is back to where it was before that stop. `clear_review = yes` clears both.
- **Exits:** +20% sell half (1 contract: all), stop to breakeven; rest out at minute 15; **if +20% hasn't hit by minute 45, sell it all**; 120-min max; flat by 3:08.
- **Shadow log:** marks from 2:00 to 2:45 PM that pass every check are logged as `shadow_late` but never traded, to judge a later cutoff.

## Changes on Nov 22 (re-check at 2¢ costs, Sep 1 – Nov 20 and the year both ways)
- Cutoff 1:00 → **2:00 PM**; stall 8 → **5 bars**; **safety brake** added. Kept: pane arrows only, 3% entry, 45-minute cut, +20% half.
- Sim, $1,000, 2¢ a side: Nov 3–20 $47,093 (20 trades, 0 losers); the year Nov 2025 → Nov 2026 in time order with the brake $17,500 (never broke).
- Half days: the 11:00 entry cutoff now applies to the Vix Fix check too.

## Changes after the Nov 20 replay sweep
- Stall window 5 → **8 bars**: removes the Nov 19 11:59 call that sat at −53%; 7, 8, 10 and 12 bars all give the same result.
- **Entry limit 5% → 3% under the mid**: better in Sep, Oct and Nov (2% about the same); 5% missed the trades that take off right away. Deeper limits (8–20%) and waiting for a confirmation bar were worse.
- **45-minute cut** added after October showed a trade (Oct 22 12:36 call) that never hit +20% or the −75% stop and rode 120 minutes to −72%. 45–60 minutes is the best range; it changes nothing in Nov 3–19.

| Replay ($1,000 start, whole contracts) | End | Trades | Worst heat |
|---|---|---|---|
| Nov 3–19 | $14,694 | 14/14 wins | −24% |
| Oct 1–30 (history files) | $1,446 | 5/6 wins | −50% |
| Sep 1–30 (history files) | $2,241 | 5/5 wins | −49% |
| Sep 1 → Nov 19 in a row | $58,760 | 24/25 wins | −50% |

## Tests (no key needed)
- `node spy0dte/replay_vfrev.js` — every `results/bars_*.json` through the vfrev engine from $1,000 (`why` lists every pane arrow and why it was taken or skipped). `node spy0dte/replay_vfrev.js 2026-10` replays a month from the history files (`results/spy_1m.csv.gz` + `results/opt_1m/`).
- `node spy0dte/test_vfrev_mock.js 2026-11-19 dry|live` — the full vfbot.js against a fake Public on a fast clock.
