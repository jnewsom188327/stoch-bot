// "qrev" = the QQQ reversal, the PUBLIC account's strategy from Nov 23, 2026 (replaces the SPY Vix Fix bot there).
// Pane arrows only (QQQ pane, call-chart pane, put-chart pane), read by the same live marks code as the SPY bots.
// Takes a mark only when ALL of these are true (QQQ 1-minute bars from 9:30; i = the mark's bar, d = +1 call / -1 put):
//   1) trend line AGAINST the trade (tw != 1)
//   2) ran hard: d x (close[i] - close[i-15]) <= -3.00  (QQQ moved $3+ the other way in 15 minutes)
//   3) stalled: no new day low (calls) / high (puts) in bars i-4..i vs everything before
//   4) shrinking: average |close-open| of bars i-2..i < 0.8 x the average of bars i-12..i-3
//   5) 10:01 AM to 2:00 PM
// No fear/greed (Vix Fix) level is required for QQQ: it didn't change which trades passed.
// LIVE version: first-out strike (call = first strike above, put = first strike below), limit 3% under the mid,
//   ALL OUT at +50%, -75% broker stop, 2-hour max, flat by 3:08.
// SHADOW version (paper only, logged beside it so you can compare): 1 strike in the money, a third sold at +30%,
//   stop to breakeven, the rest out at minute 15.
// Oct 1 - Nov 13, 2026 ($1,000): live version 8 trades, 8 won, $20,191, no drop; shadow version 8 of 8, $6,409.
// Nov 23, 2026: HALF PORT, and an extra exit: if QQQ makes a new day low (calls) / high (puts) $1.00 beyond
//   the extreme it had when the arrow printed, sell everything.
// Safety brake, day lock and order handling: the same as the Public Vix Fix bot (vfrev.js / engine.js).
const { VfEngine, vfCheck, VF } = require("./vfrev");
const { shiftContract, coreT } = require("./marks");

const QR = { ...VF, ranMin: 3.0, stretchMin: 0, lastTod: 270, lastLabel: "2:00 PM", firstTod: 31, stallBars: 5, shrinkRatio: 0.8 };

const QR_CFG = {
  kinds: ["P"], lastEntryTod: QR.lastTod, firstEntryTod: QR.firstTod,
  entryDisc: 0.03, trendSizing: false, pct: 0.5,   // half port (Nov 23); 1.0 = full port
  failBuf: 1.00,     // sell all if QQQ breaks the arrow-time day extreme by this many dollars (0 = off)
  ranMin: null,      // null = QR.ranMin ($3.00); a number here overrides it (replays)
  steps: 0,          // 0 = first-out strike; 2 = 1 strike in the money
  tp: 0.50,          // target
  sellFrac: 1,       // share sold at the target: 1 = all out; 1/3 = a third, then breakeven stop and the rest out at runnerMin
  runnerMin: 15, cutMin: 0, maxHold: 120, flattenAtTod: 338, stopPct: 0.75,
  reviewStops: 99, brakeLoss: 0.25, brakeWins: 5, brakeHalfPct: 0.5,
};
const QR_SHADOW = { steps: 2, tp: 0.30, sellFrac: 1 / 3 };

class QEngine extends VfEngine {
  constructor(o) { super({ ...o, cfg: { ...QR_CFG, ...(o.cfg || {}) } }); }

  markSkip(m) {
    if (this.halted()) return "stopped: " + (this.st.reviewHold ? "waiting for your review" : this.st.halt);
    if (this.pos || (this.lastExitBarT != null && m.ts <= this.lastExitBarT)) return "in a trade (marks that print while in a trade are ignored)";
    const P = this.cfg.ranMin != null ? { ...QR, ranMin: this.cfg.ranMin } : QR;
    const r = vfCheck(this.spy, m, Math.min(QR.lastTod, this.cfg.lastEntryTod), P); // this.spy holds QQQ bars here
    if (r.ok) {
      m.vf = r.vf;
      // the day's extreme up to the arrow: the level that must hold (calls: the low; puts: the high)
      const upTo = this.spy.filter((b) => coreT(b) <= m.ts);
      m.qext = m.s === "C" ? Math.min(...upTo.map((b) => +b.low)) : Math.max(...upTo.map((b) => +b.high));
      return null;
    }
    return r.why;
  }

  planFor(m) {
    const b = this.brake(), c = this.cfg;
    const label = c.steps ? `qrev ${c.steps / 2} ITM` : "qrev first-out strike";
    return { sym: shiftContract(m.contract, c.steps).sym, pct: c.pct * (b.half && !this.paper ? c.brakeHalfPct : 1), trend: b.half ? label + ", half port (brake)" : label };
  }

  async step(i, o) {
    const pos = this.pos, c = this.cfg, E = pos.entry;
    if (!this.live && o.lo <= pos.stop + 1e-9) return this.closed(pos.left, pos.stop, pos.sold ? "breakeven stop" : `stop -${Math.round(pos.stopPct * 100)}%`, !pos.sold);
    const tpTxt = `+${Math.round(c.tp * 100)}%`;
    if (!pos.sold && o.hi >= E * (1 + c.tp) - 1e-9) {
      const px = this.live ? o.bid : Math.round(E * (1 + c.tp) * 100) / 100;
      pos.sold = true;
      if (c.sellFrac >= 1) return this.sell(pos.left, px, `${tpTxt} all out`);
      const part = c.fractional ? pos.left * c.sellFrac : Math.max(1, Math.floor(pos.qty * c.sellFrac));
      await this.sell(part, px, part >= pos.left ? `${tpTxt} all out (too few contracts to split)` : `${tpTxt} ${c.sellFrac < 0.4 ? "a third" : "half"}`);
      if (!this.pos) return;
      await this.placeStop(Math.round(E * 100) / 100, pos.left);
    }
    if (!this.pos) return;
    // the move didn't stall: QQQ broke the arrow-time extreme by failBuf after the fill -> out
    if (c.failBuf && pos.m.qext != null && this.spy && this.spy.length) {
      const after = this.spy.filter((b) => coreT(b) >= pos.fillBarT && (o.barT == null || coreT(b) <= o.barT));
      const broke = pos.m.s === "C" ? after.some((b) => +b.low < pos.m.qext - c.failBuf) : after.some((b) => +b.high > pos.m.qext + c.failBuf);
      if (broke) return this.sellAll(o, `QQQ broke the ${pos.m.s === "C" ? "low" : "high"} by $${c.failBuf.toFixed(2)}: the move didn't stall`);
    }
    if (pos.sold && i >= 1 && i >= c.runnerMin) return this.sellAll(o, `runner: minute ${c.runnerMin}`);
    if (!pos.sold && c.cutMin && i >= c.cutMin) return this.sellAll(o, `no ${tpTxt} by minute ${c.cutMin}`);
    if (i >= c.maxHold) return this.sellAll(o, "max hold 120 min");
  }
}

module.exports = { QEngine, QR, QR_CFG, QR_SHADOW };
