# SPY 0DTE small-win Vix Fix bot ("swrev") — DRY RUN ONLY

Workflow **SPY 0DTE small-win Vix Fix (dry run)** (`.github/workflows/spy0dte_smallwin.yml`) · code `swbot.js` (minute loop) + `swrev.js` (rules) · files in `spy0dte/smallwin/` (state.json, logs/, summaries/, trades.csv).
No live switch: the engine is built with no broker, so it never sends an order. Public is used for prices only. It reads none of the Robinhood dot bot's or the Public bots' state and changes none of their files.

## Setups (one trade at a time)
- **A "maxed"** (your hand sequence): your side (fear for calls, greed for puts) hit **90+** in the last 12 bars and hovered (2+ bars at 80+), the other side **≤15** at the peak, SPY ran **$0.80+** the other way in 15 min. Then price **stalls** (no new low/high for 2 bars) and your side **breaks**: lower than the bar before and 10+ under the peak, other side lifting. First break bar only; skipped if the agree shading is against you. From 9:45.
- **B "swing"** (post-morning swing fade, from **11:00**): SPY popped/dropped **$1.00+** in 20 min, stalled 2+ bars, SPY's side peaked 70+ in the last 8 bars and turned down 8+. The option panes must agree: the tired option's run side (calls on a drop: the put chart's greed or the call chart's fear) peaked 70+ and is turning down. Puts on pops, calls on drops.

## Boosters (logged on every trade) and size
- **cross**: SPY's side crossed under the bought-side pane option's greed in the last 3 bars.
- **weak_open**: the first 15 minutes closed in the bottom 30% of their range, gap from yesterday's close under 0.30%.
- **vix1d_div**: SPY made a new low (calls) / high (puts) in the last 5 bars but VIX1D didn't confirm it. Live it reads VIX1D from Public; if Public doesn't serve it, this booster is off and the log says so.
- **Size:** a setup + 1 or more boosters = **full port**; a setup alone = **half port**. Contract: 0DTE, **2 strikes in the money**.

## Exits and vetoes
- **+8%** on 75% of the contracts (1 contract: all of it); the runner rides a **ratchet**: stop 5% under its peak, never under breakeven, out after 20 min.
- **Confirm within 3 minutes**: your side must be letting off (under its reading at the mark). No confirm = out.
- **Vetoes:** an **x** (same-side kill) after the mark = out; **fear/greed breaking the same way as price** (a new low/high past the setup extreme with your side rising) = out; **2 losses** on the day = done.
- Hard stop **−20%**; no +8% by minute 15 = out; **day target +15%** = done for the day.
- **No entries after 1:00 PM.** Half days (Fri Nov 27): entries until 12:30, flat by 12:50 (0DTE expires at 1:00).

## Tuning on the 17 tracked days (Nov 3–25), $1,000 start, compounding, full/half port
| Version | End | Trades | Wins | Worst trade | Max drop |
|---|---|---|---|---|---|
| Your spec as written: 1 ITM, −10% hard stop | $517 | 39 | 15 | −12.7% | −53% |
| −10% cut on closed bars, −20% hard stop | $1,362 | 69 | 44 | −20.5% | −28% |
| **Chosen: 2 ITM, −20% hard stop, let-off confirm in 3 min** | **$3,066** | **63** | **44** | **−21.2%** | **−19.8%** |

Inside the chosen version: swing 32/41 wins (+$2,264), maxed 12/22 (−$198); full port with a booster 18/23, half port 26/40. cross 8/9, weak_open 8/11, vix1d_div 4/5 (VIXY stood in for VIX1D, through Nov 17). Average winner +9.0%, average loser −11.0%; only 1 trade hit the −20% stop. 10 of 17 days green.
The replay fills at the next bar's open with 1¢ slippage each way, so live spreads will cost a little more.

## Tests (no key needed)
- `node spy0dte/replay_swrev.js [first day] [last day]` — every tracked day through the engine, every trade with its setup, boosters, confirm and exits. `CFG`, `SWP`, `SWG` (JSON) override settings.
- `node spy0dte/test_swrev_mock.js 2026-11-25 [half]` — the full swbot.js against a fake Public on a fast clock; fails if it ever tries to send an order.
