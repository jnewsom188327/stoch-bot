// "vfrev" = Vix Fix reversal, the PUBLIC account's own strategy (Nov 20, 2026).
// Pane arrows only (SPY pane, call-chart pane, put-chart pane), read by the same live marks code as the main bot.
// Takes a mark only when ALL of these are true (SPY 1-minute bars from 9:30; i = the mark's bar, d = +1 call / -1 put):
//   1) trend line AGAINST the trade (tw != 1)
//   2) Vix Fix stretch on your side hit 80+ in the last 10 bars (bars i-9..i)
//        calls (fear): wvf = (highest close of last 22 - low) / that close x 100, F = wvf / max(wvf, last 50) x 100
//        puts (greed): wvs = (high - lowest close of last 22) / that close x 100, G = wvs / max(wvs, last 50) x 100
//   3) ran hard: d x (close[i] - close[i-15]) <= -1.50
//   4) stalled: no new day low (calls) / high (puts) in bars i-4..i vs everything before
//   5) shrinking: average |close-open| of bars i-2..i < 0.8 x the average of bars i-12..i-3
//   6) before 1:00 PM (and no marks before 10:01)
// Contract: 0DTE, 1 strike in the money = 2 strikes in from the first-out strike (calls K-2, puts K+2).
// Exits: +20% sell half (1 contract: all) and stop to breakeven; rest out at minute 15; 120-min max; flat by 3:08.
// Everything else (entry, size, -75% broker stop, shutoffs, $0.80 / 10% spread / stale checks) is the main engine's.
// This file does NOT change engine.js or the Robinhood bot; it only extends the Engine class.
const { Engine } = require("./engine");
const { shiftContract, coreT } = require("./marks");

const VF = {
  firstTod: 31,      // 10:01 AM
  lastTod: 210,      // 1:00 PM
  look: 22,          // highest/lowest close lookback
  norm: 50,          // stretch normalised by the max over the last 50 bars
  stretchMin: 80,    // F or G must reach 80+
  stretchBars: 10,   // ... in bars i-9..i
  ranBars: 15, ranMin: 1.5,
  stallBars: 5,      // bars i-4..i
  shrinkNow: 3, shrinkBefore: 10, shrinkRatio: 0.8,
  steps: 2,          // 1 strike in the money
};

const todOf = (t) => (((t % 86400) + 86400) % 86400) / 60 - 570;

// SPY regular-hours bars (Public shape) -> arrays, from 9:30
function series(spyBars) {
  const rth = spyBars.filter((b) => todOf(coreT(b)) >= 0);
  return {
    t: rth.map(coreT), o: rth.map((b) => +b.open), h: rth.map((b) => +b.high), l: rth.map((b) => +b.low), c: rth.map((b) => +b.close),
  };
}

// The stretch line (F for calls, G for puts) at every bar
function stretch(S, d) {
  const n = S.c.length, raw = new Array(n), out = new Array(n);
  for (let j = 0; j < n; j++) {
    let ext = S.c[j];
    for (let k = Math.max(0, j - VF.look + 1); k <= j; k++) ext = d > 0 ? Math.max(ext, S.c[k]) : Math.min(ext, S.c[k]);
    raw[j] = d > 0 ? ((ext - S.l[j]) / ext) * 100 : ((S.h[j] - ext) / ext) * 100;
    let mx = 0;
    for (let k = Math.max(0, j - VF.norm + 1); k <= j; k++) mx = Math.max(mx, raw[k]);
    out[j] = mx > 0 ? (raw[j] / mx) * 100 : 0;
  }
  return out;
}

/** vfCheck(spyBars, m) -> { ok, why, vf } : the six entry conditions for one pane-arrow mark */
function vfCheck(spyBars, m) {
  if (m.k !== "P") return { ok: false, why: "not a pane arrow" };
  if (m.tod < VF.firstTod) return { ok: false, why: "before 10:01" };
  if (m.tod >= VF.lastTod) return { ok: false, why: "after 1:00 PM" };
  if (m.tw === 1) return { ok: false, why: "trend line with the trade (needs against)" };
  const S = series(spyBars);
  const i = S.t.indexOf(m.ts);
  if (i < 15) return { ok: false, why: "not enough bars" };
  const d = m.s === "C" ? 1 : -1;
  const st = stretch(S, d);
  let peak = 0;
  for (let k = Math.max(0, i - VF.stretchBars + 1); k <= i; k++) peak = Math.max(peak, st[k]);
  const ran = d * (S.c[i] - S.c[i - VF.ranBars]);
  let before = d > 0 ? Infinity : -Infinity, recent = d > 0 ? Infinity : -Infinity;
  for (let k = 0; k <= i; k++) {
    const x = d > 0 ? S.l[k] : S.h[k];
    if (k <= i - VF.stallBars) before = d > 0 ? Math.min(before, x) : Math.max(before, x);
    else recent = d > 0 ? Math.min(recent, x) : Math.max(recent, x);
  }
  const stalled = d > 0 ? recent >= before : recent <= before;
  const body = (k) => Math.abs(S.c[k] - S.o[k]);
  const avg = (a, b) => { let s = 0; for (let k = a; k <= b; k++) s += body(k); return s / (b - a + 1); };
  const bNow = avg(i - VF.shrinkNow + 1, i), bBefore = avg(Math.max(0, i - VF.shrinkNow - VF.shrinkBefore + 1), i - VF.shrinkNow);
  const vf = { stretch: Math.round(peak * 10) / 10, ran15: Math.round(d * ran * 100) / 100, stalled, bodyNow: Math.round(bNow * 1000) / 1000, bodyBefore: Math.round(bBefore * 1000) / 1000 };
  if (peak < VF.stretchMin) return { ok: false, why: `Vix Fix stretch ${vf.stretch} < 80`, vf };
  if (ran > -VF.ranMin + 1e-9) return { ok: false, why: `didn't run hard (${(d * ran).toFixed(2)} in 15 min)`, vf };
  if (!stalled) return { ok: false, why: `new day ${d > 0 ? "low" : "high"} in the last 5 bars`, vf };
  if (!(bNow < VF.shrinkRatio * bBefore)) return { ok: false, why: "bars not shrinking", vf };
  return { ok: true, why: null, vf };
}

// The Engine with the vfrev entry filter, contract and exits
const VF_CFG = {
  kinds: ["P"], lastEntryTod: VF.lastTod, firstEntryTod: VF.firstTod,
  trendSizing: false, pct: 1.0, tp: 0.20, runnerMin: 15, maxHold: 120, flattenAtTod: 338, stopPct: 0.75,
};

class VfEngine extends Engine {
  constructor(o) { super({ ...o, cfg: { ...VF_CFG, ...(o.cfg || {}) } }); this.spy = []; }

  // call before onMarks with today's closed SPY bars
  setSpy(spyBars) { this.spy = spyBars; }

  markSkip(m) {
    if (this.halted()) return "stopped: " + (this.st.reviewHold ? "waiting for your review" : this.st.halt);
    if (this.pos || (this.lastExitBarT != null && m.ts <= this.lastExitBarT)) return "in a trade (marks that print while in a trade are ignored)";
    const r = vfCheck(this.spy, m);
    if (r.ok) { m.vf = r.vf; return null; }
    return r.why;
  }

  planFor(m) {
    return { sym: shiftContract(m.contract, VF.steps).sym, pct: this.cfg.pct, trend: "vfrev 1 ITM" };
  }

  // Same order as the main engine, with +20% and no white-dot x (pane arrows only)
  async step(i, o) {
    const pos = this.pos, c = this.cfg, E = pos.entry;
    if (!this.live && o.lo <= pos.stop + 1e-9) return this.closed(pos.left, pos.stop, pos.sold ? "breakeven stop" : `stop -${Math.round(pos.stopPct * 100)}%`, !pos.sold);
    const tpTxt = `+${Math.round(c.tp * 100)}%`;
    if (!pos.sold && o.hi >= E * (1 + c.tp) - 1e-9) {
      const px = this.live ? o.bid : Math.round(E * (1 + c.tp) * 100) / 100;
      const half = c.fractional ? pos.left / 2 : pos.qty === 1 ? 1 : Math.floor(pos.qty / 2);
      pos.sold = true;
      await this.sell(half, px, half >= pos.left ? `${tpTxt} all out (1 contract)` : `${tpTxt} half`);
      if (!this.pos) return;
      await this.placeStop(Math.round(E * 100) / 100, pos.left);
    }
    if (!this.pos) return;
    if (pos.sold && i >= 1 && i >= c.runnerMin) return this.sellAll(o, "runner: minute 15");
    if (i >= c.maxHold) return this.sellAll(o, "max hold 120 min");
  }
}

module.exports = { VfEngine, vfCheck, VF, VF_CFG, stretch, series };
