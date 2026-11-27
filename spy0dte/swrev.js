// "swrev" = Small-Win Vix Fix reversal (Nov 26, 2026). DRY RUN ONLY. Its own bot, files and workflow;
// it never touches the Robinhood dot bot (bot.js / engine.js settings / spy0dte/state.json) or the Public bots.
//
// The hand-trade sequence, as rules (SPY 1-minute closed bars from 9:30; d = +1 call / -1 put;
// "your side" = fear F for calls, greed G for puts; "other side" = the opposite line; both from VIX FIX RAINBOW math):
//   1) SETUP (hard run, don't enter yet): your side hit SW.setMin+ in the last SW.setBars bars, hovered there
//      (SW.hoverN+ bars at SW.hoverMin+), and the other side was collapsed (<= SW.oppMax) at that peak.
//      SPY ran SW.ranMin+ dollars the other way in 15 minutes.
//   2) STALL: no new low (calls) / high (puts) in the last SW.stallMin bars.
//   3) BREAK: your side turns down off the peak (this bar lower than the last, and SW.breakDrop+ under the peak),
//      the other side lifting. Fires on the FIRST break bar of a setup only.
//   4) CONTEXT (logged on every entry; the filters below were chosen on the 17 tracked days Nov 3-25):
//      trend line color, agree shading, TTM, SPY vs the option's own fear/greed.
//   5) CONFIRM within SW_CFG.confirmBars minutes of the fill: your side letting off (below its reading at the mark).
//      No confirm = out at that bar's close. (Pane arrow / shading stall are logged and selectable: SW_CFG.confirm.)
// Exits: SW_CFG.tp (+8%) on most (SW_CFG.sellFrac), the runner on a ratchet (stop trails the peak by SW_CFG.trail,
//   never under breakeven), runner max SW_CFG.runnerMax minutes. Hard stop -20% (see SW_CFG). Out at once if price breaks the
//   setup extreme AND your side climbs again (fear/greed breaking the same way as price = get out).
// SETUP B "swing" (post-morning swing fade, from 11:00): SPY pops/drops SWING.min+ dollars in SWING.bars minutes, stalls, and
//   SPY's side turns down off SWING.sideMin+; the call/put option panes must agree (the tired option's own run side
//   peaked SWING.optMin+ and is turning down). Puts on the pops, calls on the drops.
// BOOSTERS (each logged): "cross" = SPY's side crossing under the bought-side option pane's greed in the last 3 bars;
//   "weak_open" = first 15 minutes closed in the bottom 30% of their range with a gap under 0.30%;
//   "vix1d_div" = SPY made a new low (calls) / high (puts) in the last 5 bars but VIX1D didn't confirm it.
// SIZE: a setup + 1 or more boosters = full port; a setup alone = half port.
// VETOES: an x (same-side kill) printing after the mark = out; fear/greed breaking the same way as price = out;
//   2 losses on the day = done.
// Day: one trade at a time, stop after 2 losses or once the day is up SW_CFG.dayTarget. No entries after 1:00.
const { Engine } = require("./engine");
const { contractFor, shiftContract } = require("./marks");
const r2 = (x) => Math.round(x * 100) / 100;
const r1 = (x) => (x == null || !isFinite(x) ? null : Math.round(x * 10) / 10);

const SW = {
  setMin: 90, setBars: 12, hoverMin: 80, hoverN: 2, oppMax: 15,
  ranMin: 0.8, ranBars: 15,
  stallMin: 2,
  breakDrop: 10, oppLift: true,
  firstTod: 15,   // 9:45 AM
  agFilter: true, // skip if the agree shading is against the trade on the break bar
  // patience (Nov 27): arm the setup, then wait up to 3 minutes for BOTH option panes to start breaking your way
  // (calls: the call chart's fear easing AND the put chart's greed easing; puts mirrored). No cross needed.
  // If price pushes through the setup low/high while waiting (pause-and-go), the setup is dropped.
  patience: 3, waitFor: "both", crossW: 1,
};

const SWING = {
  firstTod: 90,   // 11:00 AM
  bars: 20, min: 1.0,       // SPY moved $1.00+ in 20 minutes
  sideMin: 70, sideBars: 8, drop: 8,
  stallMin: 2,
  optMin: 70, optBars: 8,  // the tired option pane's run side peaked 70+ and is turning down
};
const BOOST = { crossBars: 3, weakFrac: 0.30, gapMax: 0.003, divNow: 5, divBefore: 10 };

const SW_CFG = {
  kinds: ["S"], firstEntryTod: SW.firstTod, lastEntryTod: 210, // no entries from 1:00 PM
  entryDisc: 0.0, cancelMin: 2, minPrice: 0.8, maxSpread: 0.10,
  trendSizing: false, pct: 1.0, steps: 4,     // 2 strikes in the money (beat 1 ITM and first-out on the 17 days)
  tp: 0.08, sellFrac: 0.75,                    // +8% on most
  trail: 0.05, runnerMax: 20,                  // runner: ratchet 5% under its peak, floor = breakeven
  stopPct: 0.20,                               // hard stop -20% (a -10% stop got tagged by 1-minute wicks: $517 vs $3,066 on the 17 days)
  halfPct: 0.5,
  xVeto: true,                                 // an x (same-side kill) after the mark = out
  softCut: 0, softCutAlways: false,            // cut on a closed bar at -softCut (0 = off)
  confirmBars: 3, confirm: "letoff",           // your side must be letting off within 3 minutes, else out (best of arrow/shading/let-off)
  cutMin: 15,                                  // no +8% by minute 15 = out
  failBuf: 0.05,                               // price $0.05 past the setup extreme with your side rising = out
  maxLosses: 2, dayTarget: 0.15,               // stop after 2 losers or +15% on the day
  flattenAtTod: 338, maxHold: 60, reviewStops: 99, dayMaxLoss: 0.30, dayLockAt: 99,
};

const keys = (d) => (d > 0 ? { S: "F", O: "G", sA: "fA", ext: "l" } : { S: "G", O: "F", sA: "gA", ext: "h" });

/** swSignal(rows, i, d, P) -> null | { x (setup extreme), read } ; rows = core compute() rows (closed bars) */
function swSignal(rows, i, d, P = SW) {
  if (i < 20) return null;
  const K = keys(d), r = rows[i], p = rows[i - 1];
  let pk = -1, peak = -1, hover = 0;
  for (let k = Math.max(0, i - P.setBars + 1); k <= i; k++) {
    if (rows[k][K.S] >= peak) { peak = rows[k][K.S]; pk = k; }
    if (rows[k][K.S] >= P.hoverMin) hover++;
  }
  if (peak < P.setMin || hover < P.hoverN) return null;
  const oppAtPeak = rows[pk][K.O];
  if (oppAtPeak > P.oppMax) return null;
  const ran = d * (r.c - rows[i - P.ranBars].c);
  if (ran > -P.ranMin) return null;
  // stall: the extreme of the run is at least stallMin bars old
  let x = d > 0 ? Infinity : -Infinity, xi = i;
  for (let k = Math.max(0, i - P.setBars - 8); k <= i; k++) {
    const v = rows[k][K.ext];
    if (d > 0 ? v <= x : v >= x) { x = v; xi = k; }
  }
  const stall = i - xi;
  if (stall < P.stallMin) return null;
  // break: first bar off the peak by breakDrop, falling, other side lifting
  const brk = r[K.S] < p[K.S] && r[K.S] <= peak - P.breakDrop;
  const firstBrk = !(p[K.S] < rows[i - 2][K.S] && p[K.S] <= peak - P.breakDrop); // the bar before wasn't already a break
  if (!brk || !firstBrk) return null;
  if (P.oppLift && !(r[K.O] > p[K.O])) return null;
  const agYour = d * (r.ag || 0);
  if (P.agFilter && agYour === -1) return null;
  return {
    x,
    read: {
      peak: r1(peak), peakAgo: i - pk, hover, oppAtPeak: r1(oppAtPeak), sideNow: r1(r[K.S]), oppNow: r1(r[K.O]),
      ran15: r2(-ran), stall, trendLine: d * (r.col || 0) > 0 ? "your way" : d * (r.col || 0) < 0 ? "against" : "chop",
      col: r.col, shading: agYour === 1 ? "your way" : agYour === -1 ? "against" : "none", ttm: r1(r.m), ttmTurning: d > 0 ? r.m > p.m : r.m < p.m,
      spy: r.c, ext: x,
    },
  };
}

// The option's own fear/greed at a time (rows = core compute() of the contract's bars): for a call bought on a SPY drop,
// the call's fear is high; "the cross" = SPY's side falling while the option's greed (other side) rises.
function optRead(optRows, t, d) {
  if (!optRows || !optRows.length) return null;
  let j = -1;
  for (let k = 0; k < optRows.length; k++) if (optRows[k].t <= t) j = k;
  if (j < 1) return null;
  const o = optRows[j], q = optRows[j - 1];
  return { optFear: r1(o.F), optGreed: r1(o.G), optGreedRising: o.G > q.G, optFearFalling: o.F < q.F };
}

const optSym = (day, cp, K) => "SPY" + day.slice(2, 4) + day.slice(5, 7) + day.slice(8, 10) + cp + String(Math.round(K * 1000)).padStart(8, "0");
const upTo = (R, t) => { if (!R) return []; let j = -1; for (let k = 0; k < R.length; k++) if (R[k].t <= t) j = k; return R.slice(0, j + 1); };

/** swingSignal(rows, i, d, ctx) -> null | { x, read }: the post-morning swing fade */
function swingSignal(rows, i, d, ctx = {}, P = SWING) {
  if (i < P.bars + 2) return null;
  const K = keys(d), r = rows[i], p = rows[i - 1];
  const tod = ((((r.t % 86400) + 86400) % 86400) / 60) - 570;
  if (tod < P.firstTod) return null;
  const move = d * (r.c - rows[i - P.bars].c);
  let x = d > 0 ? Infinity : -Infinity, xi = i;
  for (let k = i - P.bars; k <= i; k++) { const v = rows[k][K.ext]; if (d > 0 ? v <= x : v >= x) { x = v; xi = k; } }
  const swing = d > 0 ? rows[i - P.bars].c - x : x - rows[i - P.bars].c; // size of the pop/drop to its extreme
  if (swing < P.min) return null;
  if (i - xi < P.stallMin) return null;
  let peak = 0, pk = i;
  for (let k = i - P.sideBars + 1; k <= i; k++) if (rows[k][K.S] >= peak) { peak = rows[k][K.S]; pk = k; }
  if (peak < P.sideMin || !(r[K.S] < p[K.S]) || r[K.S] > peak - P.drop) return null;
  if (p[K.S] < rows[i - 2][K.S] && p[K.S] <= peak - P.drop) return null; // first break bar only
  // the option panes: calls on a drop -> the put chart's greed and the call chart's fear were running; one must be turning down
  const ks = { call: Math.floor(r.c) + 1, put: Math.ceil(r.c) - 1 };
  const panes = [];
  for (const [cp, K2, key] of d > 0 ? [["P", ks.put, "G"], ["C", ks.call, "F"]] : [["C", ks.call, "G"], ["P", ks.put, "F"]]) {
    const R = upTo(ctx.optRows && ctx.optRows[optSym(ctx.day, cp, K2)], r.t);
    if (R.length < 3) continue;
    let pkO = 0; for (let k = Math.max(0, R.length - P.optBars); k < R.length; k++) pkO = Math.max(pkO, R[k][key]);
    const a = R[R.length - 1], b = R[R.length - 2];
    if (pkO >= P.optMin && a[key] < b[key]) panes.push(`${cp === "C" ? "call" : "put"} ${key === "G" ? "greed" : "fear"} ${r1(pkO)}->${r1(a[key])}`);
  }
  if (!panes.length) return null;
  const agYour = d * (r.ag || 0);
  return {
    x,
    read: {
      swing: r2(swing), move20: r2(move), peak: r1(peak), peakAgo: i - pk, sideNow: r1(r[K.S]), oppNow: r1(r[K.O]), stall: i - xi, panes: panes.join(", "),
      trendLine: d * (r.col || 0) > 0 ? "your way" : d * (r.col || 0) < 0 ? "against" : "chop", col: r.col,
      shading: agYour === 1 ? "your way" : agYour === -1 ? "against" : "none", ttm: r1(r.m), ttmTurning: d > 0 ? r.m > p.m : r.m < p.m, spy: r.c, ext: x,
    },
  };
}

/** boosters(rows, i, d, ctx) -> [names] */
function boosters(rows, i, d, ctx = {}, B = BOOST) {
  const out = [], K = keys(d), r = rows[i];
  if (ctx.bothBoost && bothBreak(ctx, rows, i, d, 2)) out.push("both_break");
  // 1) cross: SPY's side crossing under the bought-side option pane's greed (calls: the call chart, puts: the put chart)
  const cp = d > 0 ? "C" : "P", K2 = d > 0 ? Math.floor(r.c) + 1 : Math.ceil(r.c) - 1;
  const O = ctx.optRows && ctx.optRows[optSym(ctx.day, cp, K2)];
  if (O) {
    const om = new Map(O.map((x) => [x.t, x]));
    for (let k = Math.max(1, i - B.crossBars + 1); k <= i; k++) {
      const a = om.get(rows[k].t), b = om.get(rows[k - 1].t);
      if (a && b && rows[k - 1][K.S] > b.G && rows[k][K.S] <= a.G) { out.push("cross"); break; }
    }
  }
  // 2) weak-open day
  if (ctx.weakOpen) out.push("weak_open");
  // 3) VIX1D not confirming the new extreme
  if (ctx.vix && ctx.vix.size && i >= B.divNow + B.divBefore) {
    const now = rows.slice(i - B.divNow + 1, i + 1), before = rows.slice(i - B.divNow - B.divBefore + 1, i - B.divNow + 1);
    const vx = (R) => R.map((x) => ctx.vix.get(x.t)).filter((v) => v != null);
    const vn = vx(now), vb = vx(before);
    if (vn.length >= 3 && vb.length >= 5) {
      const newExt = d > 0 ? Math.min(...now.map((x) => x.l)) < Math.min(...before.map((x) => x.l)) : Math.max(...now.map((x) => x.h)) > Math.max(...before.map((x) => x.h));
      const conf = d > 0 ? Math.max(...vn) > Math.max(...vb) : Math.min(...vn) < Math.min(...vb);
      if (newExt && !conf) out.push("vix1d_div");
    }
  }
  return out;
}

/** weak-open day: first 15 bars close in the bottom 30% of their range, gap from yesterday's close under 0.30% */
function weakOpen(rows, prevClose, B = BOOST) {
  if (rows.length < 15 || !(prevClose > 0)) return null;
  const f = rows.slice(0, 15), hi = Math.max(...f.map((x) => x.h)), lo = Math.min(...f.map((x) => x.l));
  const pos = hi > lo ? (f[14].c - lo) / (hi - lo) : 0.5, gap = Math.abs(f[0].o - prevClose) / prevClose;
  return pos <= B.weakFrac && gap <= B.gapMax;
}

/** marks for the newest closed bar: { k:"S", ts, t, s, side, tod, px, contract, x, read } */
// The call and put pane charts breaking against each other: for calls, the call chart's greed crossing above the put
// chart's greed (and the put's greed falling); mirrored for puts. Returns true if it crossed within the last `w` bars.
function optCross(ctx, rows, i, d, w = 3) {
  const r = rows[i], ks = { call: Math.floor(r.c) + 1, put: Math.ceil(r.c) - 1 };
  const C = ctx.optRows && ctx.optRows[optSym(ctx.day, "C", ks.call)], Pt = ctx.optRows && ctx.optRows[optSym(ctx.day, "P", ks.put)];
  if (!C || !Pt) return false;
  const cm = new Map(C.map((x) => [x.t, x])), pm = new Map(Pt.map((x) => [x.t, x]));
  const gap = (k) => { const a = cm.get(rows[k].t), b = pm.get(rows[k].t); return a && b ? d * (a.G - b.G) : null; };
  const g0 = gap(i);
  if (g0 == null || g0 <= 0) return false;
  for (let k = i - 1; k >= Math.max(0, i - w); k--) { const g = gap(k); if (g != null && g <= 0) return true; }
  return false;
}

function bothBreak(ctx, rows, i, d, w = 2) {
  const r = rows[i], ks = { call: Math.floor(r.c) + 1, put: Math.ceil(r.c) - 1 };
  const C = ctx.optRows && ctx.optRows[optSym(ctx.day, "C", ks.call)], Pt = ctx.optRows && ctx.optRows[optSym(ctx.day, "P", ks.put)];
  if (!C || !Pt) return false;
  const cm = new Map(C.map((x) => [x.t, x])), pm = new Map(Pt.map((x) => [x.t, x]));
  const a1 = cm.get(r.t), b1 = pm.get(r.t), a0 = cm.get(rows[Math.max(0, i - w)].t), b0 = pm.get(rows[Math.max(0, i - w)].t);
  if (!a1 || !b1 || !a0 || !b0) return false;
  // calls: the call's fear easing and the put's greed easing; puts: the put's fear easing and the call's greed easing
  return d > 0 ? a1.F < a0.F && b1.G < b0.G : b1.F < b0.F && a1.G < a0.G;
}

function swMarks(day, rows, P = SW, hmLabel, ctx = {}) {
  const i = rows.length - 1;
  if (i < 0) return [];
  const armed = ctx.armed || null; // patience: { long: {...}, short: {...} } kept by the caller across minutes
  ctx = { ...ctx, day };
  const out = [];
  for (const d of [1, -1]) {
    const side = d > 0 ? "long" : "short", r = rows[i];
    let setup = "maxed", g = swSignal(rows, i, d, P);
    if (!g && ctx.swing !== false) { setup = "swing"; g = swingSignal(rows, i, d, ctx); }
    if (P.patience && armed) {
      // don't take the first pause: arm the setup, then enter only when the call and put charts cross the trade's way
      if (g) armed[side] = { setup, g, i0: i, ts: r.t };
      const a = armed[side];
      if (!a) continue;
      const pauseAndGo = d > 0 ? r.l < a.g.x - 0.05 : r.h > a.g.x + 0.05; // price pushed through the setup extreme: the run kept going
      if (i - a.i0 > P.patience || pauseAndGo) { delete armed[side]; continue; }
      if (!(P.waitFor === "both" ? bothBreak(ctx, rows, i, d, P.crossW || 2) : optCross(ctx, rows, i, d, P.crossW || 3))) continue;
      delete armed[side];
      setup = a.setup; g = { ...a.g, read: { ...a.g.read, waited: i - a.i0 } };
    }
    if (!g) continue;
    if (P.needBoth && !bothBreak(ctx, rows, i, d, P.bothW || 2)) continue;
    const tod = ((((r.t % 86400) + 86400) % 86400) / 60) - 570;
    const bs = boosters(rows, i, d, ctx);
    const cp = d > 0 ? "C" : "P", K2 = d > 0 ? Math.floor(r.c) + 1 : Math.ceil(r.c) - 1;
    const orow = optRead(ctx.optRows && ctx.optRows[optSym(day, cp, K2)], r.t, d);
    out.push({ k: "S", src: setup, setup, boosters: bs, ts: r.t, t: hmLabel ? hmLabel(r.t) : String(tod), side, s: cp, tod, px: r.c, tw: d * (r.col || 0) > 0 ? 1 : 0, ag: d * (r.ag || 0), contract: contractFor(day, side, r.c), x: g.x, read: g.read, optRead: orow });
  }
  return out;
}

class SwEngine extends Engine {
  constructor(o) { super({ ...o, cfg: { ...SW_CFG, ...(o.cfg || {}) } }); this.rows = []; this.pane = []; }

  // call each minute before tick/onMarks: SPY compute() rows so far, and today's pane arrows [{ts, side}]
  setCtx(rows, pane) { this.rows = rows || []; this.pane = pane || []; }

  dayStats() {
    const st = this.st;
    if (st.swDay !== st.day) { st.swDay = st.day; st.dayLosses = 0; st.dayTrades = 0; }
    return st;
  }

  markSkip(m) {
    this.dayStats();
    if (this.halted()) return "stopped: " + this.st.halt;
    if (this.pos || this.pending || (this.lastExitBarT != null && m.ts <= this.lastExitBarT)) return "in a trade (one at a time)";
    if (m.tod < this.cfg.firstEntryTod) return "before the first entry time";
    if (m.tod >= this.cfg.lastEntryTod) return "after the entry cutoff";
    return null;
  }

  // setup + 1 or more boosters = full port; setup alone = half port
  planFor(m) {
    const full = (m.boosters || []).length > 0;
    return { sym: shiftContract(m.contract, this.cfg.steps).sym, pct: this.cfg.pct * (full ? 1 : this.cfg.halfPct), trend: `${m.setup} ${full ? "full port (" + m.boosters.join("+") + ")" : "half port (no booster)"}` };
  }

  async tryEntry(m) {
    this.log("setup_read", { mark: { t: m.t, s: m.s }, setup: m.setup, boosters: m.boosters, read: m.read, optRead: m.optRead });
    return super.tryEntry(m);
  }

  rowsUpTo(t) { return this.rows.filter((r) => r.t <= t); }

  confirmed(pos, barT) {
    const c = this.cfg, m = pos.m, d = m.s === "C" ? 1 : -1;
    const arrow = this.pane.some((a) => a.side === m.side && a.ts >= m.ts && a.ts <= barT);
    const after = this.rows.filter((r) => r.t > m.ts && r.t <= barT);
    const bg = m.ag === 1 || after.some((r) => d * (r.ag || 0) >= 0 && (m.ag === -1 || d * (r.ag || 0) === 1)) || (m.ag === 0 && after.length > 0 && after.every((r) => d * (r.ag || 0) >= 0));
    // letoff = your side kept letting off after the mark (below its mark-bar reading on the latest bar)
    const K = keys(d), r0 = this.rows.find((r) => r.t === m.ts), rl = after[after.length - 1];
    const letoff = !!(r0 && rl && rl[K.S] < r0[K.S]);
    const why = arrow ? "pane arrow" : bg ? "shading stall" : letoff ? "fear/greed letting off" : null;
    if (c.confirm === "arrow") return arrow ? "pane arrow" : null;
    if (c.confirm === "bg") return bg ? "shading stall" : null;
    if (c.confirm === "letoff") return letoff ? "fear/greed letting off" : null;
    if (c.confirm === "arrow_letoff") return arrow ? "pane arrow" : letoff ? "fear/greed letting off" : null;
    if (c.confirm === "either") return arrow ? "pane arrow" : bg ? "shading stall" : null;
    if (c.confirm === "none") return "not required";
    return why; // "any"
  }

  // fear/greed breaking the same way as price: a new extreme past the setup low/high with your side rising
  failed(pos, barT) {
    const c = this.cfg, m = pos.m, d = m.s === "C" ? 1 : -1, K = keys(d);
    const R = this.rowsUpTo(barT);
    if (R.length < 2) return false;
    const r = R[R.length - 1], p = R[R.length - 2];
    const broke = d > 0 ? r.l < m.x - c.failBuf : r.h > m.x + c.failBuf;
    return broke && r[K.S] > p[K.S];
  }

  async step(i, o) {
    const pos = this.pos, c = this.cfg, E = pos.entry;
    const barT = o.barT != null ? o.barT : this.rows.length ? this.rows[this.rows.length - 1].t : 0;
    // 1) the stop (hard -10%, or the runner's ratchet); a bar that opens through it fills at its open
    if (!this.live && o.lo <= pos.stop + 1e-9) {
      const bar = o.barT != null ? this.mk.optBars(pos.sym).find((b) => b.t === o.barT) : null;
      const px = bar && bar.o < pos.stop ? bar.o : pos.stop;
      return this.closed(pos.left, px, pos.sold ? "runner ratchet" : `stop -${Math.round(c.stopPct * 100)}%`, !pos.sold);
    }
    // 2) +8% on most
    if (!pos.sold && o.hi >= E * (1 + c.tp) - 1e-9) {
      const px = this.live ? o.bid : r2(E * (1 + c.tp));
      const n = c.fractional ? pos.left * c.sellFrac : pos.qty < 2 ? pos.qty : Math.max(1, Math.min(pos.qty - 1, Math.round(pos.qty * c.sellFrac)));
      pos.sold = true; pos.peak = o.hi;
      await this.sell(n, px, n >= pos.left ? `+${Math.round(c.tp * 100)}% all out` : `+${Math.round(c.tp * 100)}% most`);
      if (!this.pos) return;
      pos.soldAt = i;
      await this.placeStop(r2(E), pos.left);
    }
    if (!this.pos) return;
    if (c.xVeto && this.kills.some((k) => k.side === pos.m.side && k.ts > pos.m.ts && k.ts - pos.m.ts <= 600 && k.ts <= barT)) return this.sellAll(o, "veto: x printed after the mark");
    if (pos.sold) {
      pos.peak = Math.max(pos.peak || 0, o.hi);
      const lock = r2(Math.max(E, pos.peak * (1 - c.trail)));
      if (lock > pos.stop + 0.005) await this.placeStop(lock, pos.left);
      if (i - pos.soldAt >= c.runnerMax) return this.sellAll(o, `runner: ${c.runnerMax} min`);
      return;
    }
    // 3) before +8%: confirm or cut, and the fail exit
    if (!pos.conf) {
      const why = this.confirmed(pos, barT);
      if (why) { pos.conf = why; this.log("confirm", { sym: pos.sym, by: why, minute: i }); }
      else if (i + 1 >= c.confirmBars) return this.sellAll(o, `no confirm in ${c.confirmBars} min`);
    }
    if (this.failed(pos, barT)) return this.sellAll(o, "fear/greed breaking with price");
    // the -10% cut on a closed bar (the hard stop sits wider so a 1-minute wick doesn't take it); with no confirm yet it's out
    if (c.softCut && o.close <= E * (1 - c.softCut) + 1e-9 && (!pos.conf || c.softCutAlways)) return this.sellAll(o, `cut -${Math.round(c.softCut * 100)}% (no confirm)`);
    if (c.softCut && c.softCutAlways && o.close <= E * (1 - c.softCut) + 1e-9) return this.sellAll(o, `cut -${Math.round(c.softCut * 100)}%`);
    if (c.cutMin && i >= c.cutMin) return this.sellAll(o, `no +${Math.round(c.tp * 100)}% by minute ${c.cutMin}`);
    if (i >= c.maxHold) return this.sellAll(o, "max hold");
  }

  afterTrade(pos) {
    const st = this.dayStats(), c = this.cfg, t = st.trades[st.trades.length - 1];
    if (t) { t.setup = pos.m.setup; t.boosters = (pos.m.boosters || []).join("+") || "none"; t.read = pos.m.read; t.optRead = pos.m.optRead || null; t.confirm = pos.conf || "none"; }
    st.dayTrades++;
    if (t && t.pnl <= 0) st.dayLosses++;
    const day = st.balance - st.dayStart;
    if (!st.halt && st.dayLosses >= c.maxLosses) st.halt = `${c.maxLosses} losses today`;
    if (!st.halt && c.dayTarget && day >= st.dayStart * c.dayTarget) st.halt = `day target hit (+${Math.round(c.dayTarget * 100)}%)`;
    if (!st.halt && st.balance <= st.dayStart * (1 - c.dayMaxLoss)) st.halt = "down 30% on the day";
    if (st.halt) this.log("shutoff", { why: st.halt });
  }
}

module.exports = { bothBreak, optCross, SwEngine, swSignal, swingSignal, boosters, weakOpen, swMarks, optRead, optSym, SW, SWING, BOOST, SW_CFG };
