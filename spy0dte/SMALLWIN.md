# SPY 0DTE small-win Vix Fix bot ("swrev") — DRY RUN ONLY

Workflow **SPY 0DTE small-win Vix Fix (dry run)** (`.github/workflows/spy0dte_smallwin.yml`) · code `swbot.js` (minute loop) + `swrev.js` (rules) · files in `spy0dte/smallwin/` (state.json, logs/, summaries/, trades.csv).
No live switch: the engine is built with no broker, so it never sends an order. Public is used for prices only. It reads none of the Robinhood dot bot's or the Public bots' state and changes none of their files.

## Setups (one trade at a time)
- **A "maxed"** (your hand sequence): your side (fear for calls, greed for puts) hit **90+** in the last 12 bars and hovered (2+ bars at 80+), the other side **≤15** at the peak, SPY ran **$0.80+** the other way in 15 min. Then price **stalls** (no new low/high for 2 bars) and your side **breaks**: lower than the bar before and 10+ under the peak, other side lifting. First break bar only; skipped if the agree shading is against you. From 9:45.
- **B "swing"** (post-morning swing fade, from **11:00**): SPY popped/dropped **$1.00+** in 20 min, stalled 2+ bars, SPY's side peaked 70+ in the last 8 bars and turned down 8+. The option panes must agree: the tired option's run side (calls on a drop: the put chart's greed or the call chart's fear) peaked 70+ and is turning down. Puts on pops, calls on drops.

- **Patience (both panes):** a setup doesn't enter on the first pause. It's armed and waits up to 3 minutes for BOTH option panes to start breaking your way (calls: the call chart's fear easing and the put chart's greed easing; puts mirrored). If price pushes through the setup low/high while it waits (pause-and-go), the setup is dropped.

## Nov 28: back to 0DTE
- **Trades 0DTE again** (`SW_CFG.dte = 0`). On the 17 days with real 1DTE bars (Alpaca, Nov 3–25) the same bot made $789 on 1DTE vs $3,075 on 0DTE, and 192 of 349 shadow signals never filled at the 5% bid on 1DTE.
- **Still saves 1DTE every day** (the pane strikes' 1DTE twins and every shadow contract) and the shadow log scores 1DTE, for the 1DTE study. `bars/<day>.json` has `exp1`.

## Changes for Mon Nov 30 (from the Nov 27 review) (its 1DTE parts were replaced on Nov 28, see above)
- **1DTE:** trades the next trading day's expiry and reads its option panes on 1DTE (1DTE bars swung 4–5% a minute on Nov 27 vs 11–23% on 0DTE).
- **Always a runner:** picks the deepest strike (from 4 strikes in toward OTM) where 2+ contracts fit, so +8% sells one and the other rides the ratchet. If only 1 fits, that 1 locks +6% at +8% and rides the ratchet instead of selling.
- **Saves the day's bars** (SPY + every option chart it read, 1DTE and the 0DTE twins) to `spy0dte/smallwin/bars/<day>.json`, so 1DTE can be replayed: `BARS_DIR=spy0dte/smallwin/bars node spy0dte/replay_swrev.js`.
- **Shadow log `lead_shadow`:** where "the option panes lead" (enter while SPY is still maxed) would have entered. Not traded: on 0DTE panes it lost (best of 72 versions: $978 on the 18 days), so it gets retested on 1DTE panes.
- **VIX pane (confluence, log only):** VIX's own fear/greed pane moves with the put chart and against the call chart (Nov 27: VIX greed moved with the put's greed 76% of minutes; your 11:55 put had both launch together, the 12:03 chase had both already maxed). Every trade logs VIX greed/fear and a `vix_pane` flag (puts: VIX greed lifting 15+ in 3 min, not maxed; calls: VIX fear rising while greed falls). It never changes size: as a sizing booster it lowered the 18 days ($2,893 -> $2,633, VIXY standing in for VIX before Nov 27).
- **Backup starts** at :27, :41 and :53 in case GitHub skips the 9:20 start (it did on Nov 27). A backup after the bot already ran exits at once.
- Tested and **not used:** a stricter "both panes break" check and "don't chase" filters (stall age, option greed already maxed) all ended lower on the 18 days.
- Nov 27 replayed with these rules (0DTE bars, 2-contract pick): 5 of 6 wins, $1,000 → $1,162. 18 days: $2,893, worst drop −21%.

## Boosters (logged on every trade) and size
- **cross**: SPY's side crossed under the bought-side pane option's greed in the last 3 bars.
- **weak_open**: the first 15 minutes closed in the bottom 30% of their range, gap from yesterday's close under 0.30%.
- **vix1d_div**: SPY made a new low (calls) / high (puts) in the last 5 bars but VIX1D didn't confirm it. Live it reads VIX1D from Public; if Public doesn't serve it, this booster is off and the log says so.
- **Size:** a setup + 1 or more boosters = **full port**; a setup alone = **half port**. Contract: 0DTE, **2 strikes in the money**.

## Exits and vetoes
- **+8%** on 75% of the contracts (1 contract: all of it); the runner rides a **ratchet**: stop 5% under its peak, never under breakeven, out after 20 min.
- **Confirm within 3 minutes**: your side must be letting off (under its reading at the mark). No confirm = out.
- **Vetoes:** an **x** (same-side kill) after the mark = out; **fear/greed breaking the same way as price** (a new low/high past the setup extreme with your side rising) = out; **2 losses** on the day = done.
- Hard stop **−20%**; no +8% by minute 15 = out.
- **No entries after 1:00 PM.** Day-target stop off for the review dry run (the 2-loss stop stays). Half days: entries until 12:30, flat by 12:50 (0DTE expires at 1:00).

## Tuning on the 17 tracked days (Nov 3–25), $1,000 start, compounding, full/half port
| Version | End | Trades | Wins | Worst trade | Max drop |
|---|---|---|---|---|---|
| Your spec as written: 1 ITM, −10% hard stop | $517 | 39 | 15 | −12.7% | −53% |
| −10% cut on closed bars, −20% hard stop | $1,362 | 69 | 44 | −20.5% | −28% |
| 2 ITM, −20% hard stop, let-off confirm in 3 min | $3,066 | 63 | 44 | −21.2% | −19.8% |
| **Chosen: + wait for both option panes to break your way (up to 3 min)** | **$3,106** | **63** | **45** | **−21.2%** | **−17.1%** |
| (tested, not used) wait for the call and put charts to cross | $950 | 37 | 25 | −20.5% | −44% |

Inside the chosen version: swing 32/41 wins (+$2,264), maxed 12/22 (−$198); full port with a booster 18/23, half port 26/40. cross 8/9, weak_open 8/11, vix1d_div 4/5 (VIXY stood in for VIX1D, through Nov 17). Average winner +9.0%, average loser −11.0%; only 1 trade hit the −20% stop. 10 of 17 days green.
The replay fills at the next bar's open with 1¢ slippage each way, so live spreads will cost a little more.

## Tests (no key needed)
- `node spy0dte/replay_swrev.js [first day] [last day]` — every tracked day through the engine, every trade with its setup, boosters, confirm and exits. `CFG`, `SWP`, `SWG` (JSON) override settings.
- `node spy0dte/test_swrev_mock.js 2026-11-25 [half]` — the full swbot.js against a fake Public on a fast clock; fails if it ever tries to send an order.

## Shadow logs (Nov 28) — log only, never traded
`shadow.js` watches five other avenues all day (9:30–3:00), including while the real bot is in a trade and after it stops for the day. **It cannot place an order, block a trade or change a size**: it only gets copies of the bars and reads which side the bot holds. `SW_SHADOW=off` turns it off; the real trades are identical either way (checked on 5 days in the mock test, including a 2-loss day and a half day).

| Avenue | Rules (copied from) | Strike | Own exits |
|---|---|---|---|
| Trend your way (Option 2) | white dots + pane arrows, trend line your way, shading not against, before 1:00 (track.js `opt2`) + logs the **both-charts safety check** | strong trend 1 ITM, weak 3 ITM half port | half +10%, breakeven, runner 15 min, −75% |
| Lined up + ran hard | dot + same-side pane arrow within 2 min, last 3 bodies < 0.8× the 10 before, SPY ran $1.50+ against (bs_build.js `lu_run`); flags "stalled" | 1 ITM | Fade ratchet |
| Swing Break | fear/greed 95+ with the other ≤25, first minute both break, ran $1–3.50 against, 12:00–3:00 (swing.js) | 1 ITM | ratchet from +10%, −50% |
| Fade MAIN | Vix Fix reversal + SPY 90+/≤20 + contract 90+/≤20 + day your way 0.3%+, before 1:45 (track.js `fadeA`) | 1 ITM | whole ratchet from +20% |
| Smart dots | white dots with 3+ of 4 (range, VWAP, not expanding, wick) (lu_track.js) | 1 ITM | Fade ratchet |

Each signal is scored two ways at a 5% bid (skipped if it doesn't fill): **(a)** the avenue's own exits (the Edge Stress Test page's `tradeReturn`, unchanged in `shadow_src/est_page.js`) and **(b)** the small-win exits (+8% sells 1 of 2, ratchet runner, −10% cut with no confirm, 3-min confirm, x veto, −20% stop, out at 15 min). Results use the 1DTE bars the bot saves; the 0DTE twins are scored too. Signals are read off the 0DTE charts, as the trackers did.
- Live: each new signal is logged as `shadow_fire`. At night it fetches the shadow contracts' full-day bars (kept in `bars/<day>.json`), scores them, writes `smallwin/shadow.csv` (one row per signal) and `shadow_real.csv` (the real bot's trade times), and adds **"What it passed on"** to the daily issue: winners while the real bot sat out first, then each avenue's day and running record, the trend safety check, and two combined accounts (Trend with the safety check + reversal dots; All three with Swing Break).
- **Promotion is never automatic.** After 10 dry-run days the issue lists any avenue with 85%+ wins, no loss worse than −50%, that also adds money when combined first-come with the reversal bot. You decide.
- Baseline: `SHADOW=1 node spy0dte/replay_swrev.js` → `smallwin/SHADOW_BASELINE.md` (17 saved days, 0DTE bars). Swing Break matches the tracker's swing.json exactly on all 66 shared signals.
- Known differences from the trackers: "lined up" can be confirmed by a pane arrow up to 2 min after the dot; it's scored from the dot like the tracker, and `known_at` shows when it was knowable. Overlapping signals are all counted (the trackers' $1,000 accounts skip them). The Fade contract fear/greed is read without waiting for its bars after the mark.
