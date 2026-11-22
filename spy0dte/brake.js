// Safety brake for the Robinhood dot bot (Nov 22, 2026). Same rules as the Public bot's brake (vfrev.js):
//  - after a trade that loses 25% or more: PAPER ONLY (no orders) until 5 paper trades in a row win, then real again
//  - after a -75% stop: HALF PORT until the bot's money is back to where it was before that stop
//  clear_review = yes clears both by hand. Everything else (day lock, -75% day stop, 2-of-10 review) stays as it was.
// Oct 1 - Nov 20 replay (Option 2 + puts half at +15%): worst drop 22% with the brake vs 42%+ without.
const r2 = (x) => Math.round(x * 100) / 100;

const BRAKE_CFG = { brake: true, brakeLoss: 0.25, brakeWins: 5, brakeHalfPct: 0.5 };

const withBrake = (Base) => class extends Base {
  constructor(o) { super({ ...o, cfg: { ...BRAKE_CFG, ...(o.cfg || {}) } }); }

  brake() { if (!this.st.brake) this.st.brake = { need: 0, half: false, target: null }; return this.st.brake; }

  planFor(m) {
    const p = super.planFor(m), b = this.brake();
    if (!this.cfg.brake || !b.half || this.paper) return p;
    return { ...p, pct: p.pct * this.cfg.brakeHalfPct, trend: p.trend + ", half port (brake)" };
  }

  // Paper trades while the brake is on: the engine's own dry-run mode (fills/exits judged on the option's 1-minute bars), no orders
  async tryEntry(m) {
    const b = this.brake();
    if (this.cfg.brake && b.need > 0 && this.realLive === undefined && !this.pending) {
      this.realLive = this.live; this.live = false; this.paper = true;
      this.log("brake_paper", { mark: { t: m.t, k: m.k, src: m.src, s: m.s }, winsNeeded: b.need, note: "paper only, no order sent" });
    }
    this.inEntry = true; // a paper order replaced by a new mark must stay paper
    try { await super.tryEntry(m); } finally { this.inEntry = false; }
    if (!this.pending && !this.pos) this.endPaper();
  }
  endPaper() { if (this.paper) { this.live = this.realLive; this.realLive = undefined; this.paper = false; } }
  async cancelPending(why) { await super.cancelPending(why); if (!this.inEntry && !this.pending && !this.pos) this.endPaper(); }

  async closed(qty, px, why, hitStop = false) {
    if (!this.paper) {
      if (this.pos && this.pos.preBal === undefined) this.pos.preBal = this.st.balance;
      return super.closed(qty, px, why, hitStop);
    }
    // paper trade: score it for the brake, never touch the bot's money, trade list or shutoffs
    const pos = this.pos, c = this.cfg;
    pos.done.push({ qty, px: Math.max(0, px - c.slip), why });
    pos.left -= qty;
    this.log("exit_PAPER", { sym: pos.sym, qty, px: r2(px), why });
    if (pos.left > 1e-9) return;
    this.pos = null;
    this.lastExitBarT = this.exitBarT != null ? this.exitBarT : Math.floor(this.mk.nowC() / 60) * 60 - 60;
    const ret = pos.done.reduce((a, d) => a + d.qty * d.px, 0) / pos.qty / pos.cost - 1;
    const b = this.brake();
    b.need = ret > 0 ? b.need - 1 : c.brakeWins;
    this.log("paper_trade", { mark: { t: pos.m.t, k: pos.m.k, src: pos.m.src, s: pos.m.s }, sym: pos.sym, entry: pos.entry, ret: Math.round(ret * 1000) / 10, winsStillNeeded: b.need });
    (this.st.paper = this.st.paper || []).push({ day: this.st.day, t: pos.m.t, s: pos.m.s, sym: pos.sym, ret: Math.round(ret * 1000) / 10 });
    if (b.need <= 0) { b.need = 0; this.log("brake_off", { note: "5 paper wins in a row: real trades again" }); }
    this.endPaper();
  }

  afterTrade(pos) {
    super.afterTrade(pos);
    const c = this.cfg, b = this.brake(), t = this.st.trades[this.st.trades.length - 1];
    if (!c.brake) return;
    if (t && t.ret <= -c.brakeLoss * 100 + 1e-9) { b.need = c.brakeWins; this.log("brake_on", { why: `lost ${t.ret}%`, note: "paper only until 5 paper wins in a row" }); }
    if (pos.hitStop) { b.half = true; b.target = Math.max(b.target || 0, pos.preBal || 0); this.log("brake_half", { until: Math.round(b.target) }); }
    if (b.half && b.target != null && this.st.balance >= b.target - 0.5) { b.half = false; b.target = null; this.log("brake_half_off", { balance: this.st.balance }); }
  }
};

module.exports = { withBrake, BRAKE_CFG };
