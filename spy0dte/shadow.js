// SHADOW LOGS for the small-win dry-run bot (Nov 28, 2026). LOG ONLY: nothing in this file can place an order,
// block a real trade or change a size. The small-win bot (swrev.js / swbot.js) trades exactly as before; this file
// only watches the same bars, writes spy0dte/smallwin/shadow.csv and adds "What it passed on" to the daily issue.
//
// The five shadow avenues are copied from the code that already tracks them (copies in spy0dte/shadow_src/):
//   trend  "Trend your way (Option 2)"  - Edge Stress Test build/track.js + bs_build.js 'opt2': white dots + pane arrows,
//           filter twok (SPY trend line your way, agree shading not against), before 1:00; strike "trend":
//           strong trend (mv30 >= $0.30 and EMA13-EMA34 >= $0.10 your way) = 1 ITM full port, weak = 3 ITM half port.
//           Exits: base (half at +10%, breakeven after, runner out at 15 min, -75% stop, x exit at minute 10).
//           Extra flag (Nov 28): both_charts = the call and put pane charts both breaking your way (swrev bothBreak, 2 min).
//   lined  "Lined up + ran hard"        - 1 ITM Confluence asset 31af2678 (lu_track.js) / 2570fec1 (bs_build.js 'lu_run'):
//           white dot with a same-side pane arrow within 2 min, last 3 candle bodies < 0.8x the 10 before, SPY ran
//           $1.50+ against in 15 min. Flag "stalled" = no new day extreme in 5 min. 1 ITM, Fade ratchet exits.
//   swing  "Swing Break"                - build/swing.js + track.js: SPY fear (calls) / greed (puts) 95+ with the other side
//           25 or under, first minute both break together, SPY ran $1.00-3.50 against in 15 min, 12:00-3:00. 1 ITM,
//           ratchet from +10%, -50% stop, no x exit.
//   fade   "Fade MAIN"                  - track.js / bs_build.js 'fadeA': Vix Fix reversal on a pane arrow (trend line not your
//           way, SPY ran $1.50+ against, no new extreme in 5 min, candles shrinking), SPY's side 90+ in 10 min with the
//           other side 20 or under, the 1 ITM contract's fear 90+ in 10 min with its greed 20 or under, SPY your way on
//           the day 0.3%+, before 1:45. 1 ITM, whole ratchet from +20%.
//   smart  "Smart dots"                 - lu_track.js: white dots with 3+ of 4 (your side of the day range, your side of VWAP,
//           candles not expanding, wick rejecting). 1 ITM, Fade ratchet exits (lu_track EX.fade).
//
// Each shadow signal is scored two ways, with a 5% limit bid (skipped if it never fills within 5 minutes):
//   (a) the avenue's own exits: tradeReturn() from the Edge Stress Test page (shadow_src/est_page.js, unchanged)
//   (b) the small-win exits: +8% sells 1 of 2, the runner rides the ratchet (5% under its peak, never under breakeven,
//       out after 20 min), -10% closed-bar cut while not confirmed, confirm = your side letting off within 3 min
//       (else out), x after the mark = out, -20% hard stop, no +8% by minute 15 = out.
// Results are on the 1DTE bars the bot saves (the expiry it trades); the 0DTE twins are scored too.
// Signals are read off the 0DTE charts, as the tracking code did.
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const { loadCore } = require("./core");
const { computeMarks, osi } = require("./marks");
const { SW_CFG, bothBreak } = require("./swrev");

const SRC = path.join(__dirname, "shadow_src", "est_page.js");
const EST_SHA256 = "c8db676de45de7afbbf6670a34d9c207c441cae74cfe98f390ff8b8623fb9312";
let EST = null;
function est() {
  if (EST) return EST;
  const raw = fs.readFileSync(SRC);
  const sha = crypto.createHash("sha256").update(raw).digest("hex");
  if (sha !== EST_SHA256) throw new Error(`shadow_src/est_page.js changed (sha ${sha}); shadow exits would no longer match the tracker`);
  // same way track.js loads it (M = the marks array, unused here; document stubbed)
  const code = raw.toString("utf8").replace("let M=[];", "let M=Mdata;");
  EST = new Function("Mdata", "document", code + ";return {tradeReturn,entryOf,strikeOf};")([], { getElementById: () => ({ value: "" }) });
  return EST;
}

const AVENUES = [
  { id: "trend", name: "Trend your way (Option 2)" },
  { id: "lined", name: "Lined up + ran hard" },
  { id: "swing", name: "Swing Break" },
  { id: "fade", name: "Fade MAIN" },
  { id: "smart", name: "Smart dots" },
];
const NAME = Object.fromEntries(AVENUES.map((a) => [a.id, a.name]));
// exits, copied from track.js / bs_build.js / lu_track.js
const base = { hold: 120, slip: 0.01, entry: 0.05, sl: 0.75, tp: 0.1, style: "half", be: true, run: "15", cut5: false, xr: true };
const EXITS = {
  trend: { ...base },
  lined: { ...base, tp: 0.2, style: "ratchet", be: false },
  swing: { ...base, tp: 0.1, sl: 0.5, style: "ratchet", be: false, xr: false },
  fade: { ...base, tp: 0.2, style: "ratchet", be: false },
  smart: { ...base, sl: 0.75, tp: 0.2, style: "ratchet", be: false },
};

const r1 = (x) => (x == null || !isFinite(x) ? null : Math.round(x * 10) / 10);
const hm = (tod) => { const m = 570 + tod; const h = Math.floor(m / 60); return `${(h % 12) || 12}:${String(m % 60).padStart(2, "0")}`; };
const yymmdd = (d) => d.slice(2, 4) + d.slice(5, 7) + d.slice(8, 10);
const toRes = (bars) => JSON.stringify({ regularMarket: { bars } });

// ---------- the day, in the results/bars_<day>.json shape, from 9:30 ----------
// B = { day, exp, spy: [[ts,o,h,l,c,v]], opt: {sym: [[minute,o,h,l,c]]} (minutes from B.spy[0]), vix?: [[ts,o,h,l,c]] }
function normDay(B) {
  const off = B.spy[0][0].slice(-6);
  const t930 = Date.parse(B.day + "T09:30:00" + off), first = Date.parse(B.spy[0][0]);
  const shift = Math.round((t930 - first) / 60000);
  const spy = B.spy.filter((b) => { const t = Date.parse(b[0]); return t >= t930 && t < t930 + 390 * 60000; });
  const opt = {};
  for (const [s, rows] of Object.entries(B.opt || {})) opt[s] = rows.map((r) => [r[0] - shift, r[1], r[2], r[3], r[4]]).filter((r) => r[0] >= 0);
  return { day: B.day, exp: B.exp || B.day, off, t930, spy, opt, vix: B.vix || null };
}
// Public bars (what swbot.js keeps in `saved`) -> B
function fromSaved(day, exp, saved) {
  if (!saved.SPY || !saved.SPY.length) return null;
  const base0 = Date.parse(saved.SPY[0].timestamp);
  const out = { day, exp, spy: saved.SPY.map((b) => [b.timestamp, +b.open, +b.high, +b.low, +b.close, +b.volume]), opt: {} };
  if (saved.VIX_INDEX) out.vix = saved.VIX_INDEX.map((b) => [b.timestamp, +b.open, +b.high, +b.low, +b.close]);
  for (const [sym, bars] of Object.entries(saved)) if (sym !== "SPY" && sym !== "VIX_INDEX") out.opt[sym] = bars.map((b) => [Math.round((Date.parse(b.timestamp) - base0) / 60000), +b.open, +b.high, +b.low, +b.close]);
  return out;
}

// ---------- everything the avenues read, for one day (bars so far live, the whole day at night) ----------
function analyze(B0, o = {}) {
  const L = loadCore();
  const B = normDay(B0);
  const day = B.day, n = B.spy.length;
  if (n < 32) return { rows: [], needs: [] };
  const iso = (ms) => new Date(ms + Number(B.off.slice(0, 3)) * 3600000).toISOString().slice(0, 19) + B.off;
  const pubOpt = (rows) => rows.map(([i, op, h, l, c]) => ({ timestamp: iso(B.t930 + i * 60000), open: op, high: h, low: l, close: c, volume: 1 }));
  const spyPub = B.spy.map(([t, op, h, l, c, v]) => ({ timestamp: t.slice(0, 19) + t.slice(-6), open: op, high: h, low: l, close: c, volume: v }));
  const zero = {};
  for (const [s, rows] of Object.entries(B.opt)) if (s.slice(3, 9) === yymmdd(day)) zero[s] = pubOpt(rows);
  // white dots + pane arrows exactly as the live bot / build_day.js finds them (0DTE pane charts, as the tracker read them)
  const { marks, kills, rows: R } = computeMarks(day, spyPub, zero);
  if (!R.length) return { rows: [], needs: [] };
  const byT = new Map(R.map((r) => [r.t, r]));
  const OB = {}, parsed = (sym) => {
    if (sym in OB) return OB[sym];
    const rows = B.opt[sym];
    if (!rows || !rows.length) return (OB[sym] = null);
    return (OB[sym] = (L.parseBars(toRes(pubOpt(rows).map((b) => ({ ...b, open: String(b.open), high: String(b.high), low: String(b.low), close: String(b.close), volume: "1" })))) || []).filter((x) => !x.live && !x.fill).sort((x, y) => x.t - y.t));
  };
  const needs = new Set();
  // ---- itm.js readings (mv30, eg, rv: mv15 ne5 st vk dm bar15 so cF cG), same math ----
  const C = B.spy.map((r) => +r[4]), O = B.spy.map((r) => +r[1]), H = B.spy.map((r) => +r[2]), Lo = B.spy.map((r) => +r[3]);
  const e13 = [], e34 = []; { let a = C[0], b = C[0]; for (const x of C) { a += (x - a) * (2 / 14); b += (x - b) * (2 / 35); e13.push(a); e34.push(b); } }
  const fgArr = (H_, L_, Cc) => { const N = Cc.length, wf = [], ws = [], F = [], G = []; for (let k = 0; k < N; k++) { const a = Cc.slice(Math.max(0, k - 21), k + 1), hc = Math.max(...a), lc = Math.min(...a); wf.push(hc > 0 ? (hc - L_[k]) / hc * 100 : 0); ws.push(lc > 0 ? (H_[k] - lc) / lc * 100 : 0); }
    for (let k = 0; k < N; k++) { const mf = Math.max(...wf.slice(Math.max(0, k - 49), k + 1)) || 1e-9, mg = Math.max(...ws.slice(Math.max(0, k - 49), k + 1)) || 1e-9; F.push(wf[k] / mf * 100); G.push(ws[k] / mg * 100); } return [F, G]; };
  const [SF, SG] = fgArr(H, Lo, C);
  const optFG = {}, fgOf = (sym) => { if (sym in optFG) return optFG[sym]; const rows = B.opt[sym]; if (!rows) { needs.add(sym); return (optFG[sym] = null); } const by = new Map(rows.map((r) => [r[0], r])); const h = [], l = [], c = []; let last = null;
    for (let i = 0; i < C.length; i++) { const r = by.get(i); if (r) { last = +r[4]; h.push(+r[2]); l.push(+r[3]); c.push(+r[4]); } else { h.push(last); l.push(last); c.push(last); } }
    const f = c.findIndex((v) => v != null); if (f < 0) return (optFG[sym] = null); for (let i = 0; i < f; i++) { h[i] = l[i] = c[i] = c[f]; } return (optFG[sym] = fgArr(h, l, c)); };
  const K0of = (px, Lg) => (Lg ? Math.floor(px) + 1 : Number.isInteger(px) ? px - 1 : Math.floor(px));
  const symFor = (px, Lg, steps, expiry) => osi(day, Lg ? "C" : "P", Lg ? K0of(px, true) - steps : K0of(px, false) + steps, expiry);
  function readings(m) {
    const d = m.s === "C" ? 1 : -1, i = m.tod;
    const x = { mv30: null, eg: null, rv: null };
    if (!(i >= 31 && i < C.length)) return x;
    x.mv30 = +(d * (C[i] - C[i - 30])).toFixed(3); x.eg = +(d * (e13[i] - e34[i])).toFixed(3);
    const ne5 = d === 1 ? Math.min(...Lo.slice(i - 4, i + 1)) <= Math.min(...Lo.slice(0, i - 4)) : Math.max(...H.slice(i - 4, i + 1)) >= Math.max(...H.slice(0, i - 4));
    const bod = (a, z) => { let t = 0; for (let j = a; j < z; j++) t += Math.abs(C[j] - O[j]); return t / (z - a); };
    const rv = { mv15: +(d * (C[i] - C[i - 15])).toFixed(3), ne5: ne5 ? 1 : 0, st: +(bod(i - 2, i + 1) / Math.max(0.001, bod(i - 12, i - 2))).toFixed(3) };
    const sideAt = (j) => {
      if (d === 1) { const w = (k) => { const hc = Math.max(...C.slice(Math.max(0, k - 21), k + 1)); return (hc - Lo[k]) / hc * 100; }; let mx = 0; for (let k = Math.max(0, j - 49); k <= j; k++) mx = Math.max(mx, w(k)); return w(j) / (mx || 1e-9) * 100; }
      const w = (k) => { const lc = Math.min(...C.slice(Math.max(0, k - 21), k + 1)); return (H[k] - lc) / lc * 100; }; let mx = 0; for (let k = Math.max(0, j - 49); k <= j; k++) mx = Math.max(mx, w(k)); return w(j) / (mx || 1e-9) * 100; };
    let pk = 0; for (let j = i - 9; j <= i; j++) pk = Math.max(pk, sideAt(j)); rv.vk = +pk.toFixed(1);
    const O0 = +B.spy[0][1]; rv.dm = +(d * (C[i] - O0) / O0 * 100).toFixed(3);
    let b15 = 0; for (let j = i - 14; j <= i; j++) b15 += H[j] - Lo[j]; rv.bar15 = +(b15 / 15).toFixed(3);
    rv.so = +(d === 1 ? SG[i] : SF[i]).toFixed(1);
    x.rv = rv;
    x.cfSym = symFor(m.px, d === 1, 2); // the 1 ITM 0DTE contract (itm.js s2) for cF / cG
    return x;
  }
  const fadeCF = (m) => { const cf = fgOf(m.x.cfSym); if (cf) { let p = 0; for (let j = m.tod - 9; j <= m.tod; j++) p = Math.max(p, cf[0][j]); m.x.rv.cF = +p.toFixed(1); m.x.rv.cG = +cf[1][m.tod].toFixed(1); } };
  // ---- lu_track.js smart(): your side of the day range, VWAP, candles not expanding, wick rejecting ----
  const avg = (a) => a.reduce((p, q) => p + q, 0) / a.length;
  function smart(m) {
    const i = m.tod; if (i < 15 || i >= B.spy.length) return null; const sg = m.s === "C" ? 1 : -1, V = B.spy.map((b) => b[5]);
    let pv = 0, vv = 0; for (let k = 0; k <= i; k++) { pv += (H[k] + Lo[k] + C[k]) / 3 * V[k]; vv += V[k]; } const vwap = pv / vv;
    const hi = Math.max(...H.slice(0, i + 1)), lo = Math.min(...Lo.slice(0, i + 1)), rg = hi - lo;
    const pos = rg > 0 ? (sg > 0 ? (C[i] - lo) / rg : (hi - C[i]) / rg) : 0.5; const vd = sg * (C[i] - vwap);
    const sz = (k) => H[k] - Lo[k]; const ex = avg([sz(i), sz(i - 1), sz(i - 2)]) / Math.max(1e-6, avg(Array.from({ length: 10 }, (_, j) => sz(i - 3 - j))));
    const wk = sz(i) > 0 ? (sg > 0 ? (Math.min(O[i], C[i]) - Lo[i]) : (H[i] - Math.max(O[i], C[i]))) / sz(i) : 0;
    const f = [pos >= 0.57, vd >= 0.07, ex < 1.05, wk >= 0.11];
    return { n: f.filter(Boolean).length, flags: ["range", "vwap", "not expanding", "wick"].filter((_, k) => f[k]).join("+") };
  }
  // ---- the marks: white dots (D) and pane arrows (P) from computeMarks, Swing Breaks (S) from swing.js ----
  const M = marks.filter((m) => m.k === "D" || m.k === "P").map((m) => ({ ...m }));
  const t0 = R[0].t;
  for (const side of ["C", "P"]) {
    const Lg = side === "C"; let armed = false;
    for (let i = 31; i < R.length && i < 330; i++) {
      const hi = Lg ? R[i].F : R[i].G, lo = Lg ? R[i].G : R[i].F, hp = Lg ? R[i - 1].F : R[i - 1].G, lp = Lg ? R[i - 1].G : R[i - 1].F;
      if (hi >= 95 && lo <= 25) armed = true;
      if (!armed || !(hi < hp && lo > lp)) continue;
      armed = false;
      const px = R[i].c, back = R[Math.max(0, i - 15)].c;
      M.push({ k: "S", src: "swing", s: side, side: Lg ? "long" : "short", ts: R[i].t, tod: Math.round((R[i].t - t0) / 60), px, kill: 0, tw: 0, ag: 0,
        swing: { run15: +((Lg ? 1 : -1) * (back - px)).toFixed(3), spyMy: +hi.toFixed(1), spyOther: +lo.toFixed(1) } });
    }
  }
  const P = M.filter((m) => m.k === "P");
  const LU2 = (m) => { const ps = P.filter((q) => q.s === m.s && Math.abs(q.tod - m.tod) <= 2); return ps.length ? ps : null; };
  // ---- which avenue each mark fires ----
  const sig = [];
  const seen = new Set();
  const push = (av, m, extra) => { const key = `${av}|${m.s}|${m.tod}`; if (seen.has(key)) return; seen.add(key); sig.push({ av, m, ...extra }); };
  for (const m of M.sort((a, b) => a.tod - b.tod)) {
    if (m.k !== "S") m.x = readings(m);
    const rv = m.x && m.x.rv;
    if (m.k === "D" || m.k === "P") {
      if (m.tw === 1 && m.ag !== undefined && m.ag !== -1 && m.tod < 210) {
        const strong = !!(m.x.mv30 != null && m.x.mv30 >= 0.3 && m.x.eg >= 0.1);
        push("trend", m, { steps: strong ? 2 : 4, size: strong ? 1 : 0.5, flag: (strong ? "strong trend, 1 ITM" : "weak trend, 3 ITM half port") + (m.k === "D" ? ", white dot" : `, ${m.src} pane arrow`) });
      }
    }
    if (m.k === "D" && m.tod < 330) {
      const lu = LU2(m);
      if (lu && rv && rv.st < 0.8 && rv.mv15 <= -1.5) {
        const known = Math.max(m.tod, Math.min(...lu.map((q) => q.tod)));
        push("lined", m, { steps: 2, size: 1, known, flag: (rv.ne5 === 0 ? "stalled" : "not stalled") + (known > m.tod ? `, arrow ${known - m.tod} min after the dot` : "") });
      }
      const sm = smart(m);
      if (sm && sm.n >= 3) push("smart", m, { steps: 2, size: 1, flag: `smart ${sm.n}/4 (${sm.flags})` });
    }
    if (m.k === "S" && m.tod >= 150 && m.tod < 330 && m.swing.run15 >= 1 && m.swing.run15 < 3.5) push("swing", m, { steps: 2, size: 1, flag: `ran $${m.swing.run15.toFixed(2)}, SPY ${m.swing.spyMy}/${m.swing.spyOther}` });
    if (m.k === "P" && m.tod < 255 && rv && m.tw !== 1 && rv.mv15 <= -1.5 && rv.ne5 === 0 && rv.st < 0.8 && rv.vk >= 90 && rv.so != null && rv.so <= 20 && rv.dm >= 0.3) {
      fadeCF(m);
      if (rv.cF >= 90 && rv.cG <= 20) push("fade", m, { steps: 2, size: 1, flag: `SPY side ${rv.vk}/${rv.so}, contract ${rv.cF}/${rv.cG}, day ${rv.dm}%` });
    }
  }
  // ---- readings at entry + context ----
  const coreRows = {}, rowsOf = (sym) => { if (sym in coreRows) return coreRows[sym]; const p = parsed(sym); return (coreRows[sym] = p && p.length ? L.compute(L.cleanPrints(p)) : null); };
  const at = (rows, t) => { if (!rows) return null; let r = null; for (const x of rows) { if (x.t <= t) r = x; else break; } return r; };
  let vixRows = null;
  if (B.vix && B.vix.length) { const p = L.parseBars(toRes(B.vix.map(([t, op, h, l, c]) => ({ timestamp: t, open: String(op), high: String(h), low: String(l), close: String(c), volume: "1" })))); if (p) vixRows = L.compute(L.cleanPrints(p.filter((x) => !x.live && !x.fill))); }
  const optRowsExp = {};
  const out = [];
  for (const s of sig) {
    const m = s.m, d = m.s === "C" ? 1 : -1, Lg = d === 1;
    const sp = byT.get(m.ts) || at(R, m.ts) || {};
    const kc = Math.floor(m.px) + 1, kp = Math.ceil(m.px) - 1;
    const cS = osi(day, "C", kc, B.exp), pS = osi(day, "P", kp, B.exp);
    const cr = at(rowsOf(cS), m.ts), pr = at(rowsOf(pS), m.ts), vr = at(vixRows, m.ts);
    if (!B.opt[cS]) needs.add(cS); if (!B.opt[pS]) needs.add(pS);
    let both = "";
    if (s.av === "trend") {
      optRowsExp[cS] = optRowsExp[cS] || rowsOf(cS); optRowsExp[pS] = optRowsExp[pS] || rowsOf(pS);
      const i = R.findIndex((r) => r.t === m.ts);
      both = i >= 2 && optRowsExp[cS] && optRowsExp[pS] ? (bothBreak({ optRows: optRowsExp, day: B.exp }, R, i, d, 2) ? "yes" : "no") : "";
    }
    const row = {
      date: day, time: hm(m.tod), known_at: hm(s.known != null ? s.known : m.tod), avenue: s.av, side: m.s, flag: s.flag + (both ? `, both charts ${both}` : ""), both_charts: both, port: s.size === 1 ? "full" : "half",
      spy_fear: r1(sp.F), spy_greed: r1(sp.G), call_fear: r1(cr && cr.F), call_greed: r1(cr && cr.G), put_fear: r1(pr && pr.F), put_greed: r1(pr && pr.G), vix_fear: r1(vr && vr.F), vix_greed: r1(vr && vr.G),
      _m: m, _s: s,
    };
    // the real bot at that minute
    const busy = o.busy && o.busy.get(m.tod);
    row.real_in_trade = busy ? (busy === m.s ? "same side" : "opposite side") : "no";
    row.real_same_move = (o.real || []).some((t) => t.s === m.s && Math.abs(t.tod - m.tod) <= 5) ? "yes" : "no";
    out.push(row);
  }
  // ---- scoring (needs the bars after the signal) ----
  if (o.score) {
    const E = est();
    const pathFor = (sym, t, Lg) => {
      const Bo = parsed(sym); if (!Bo) { needs.add(sym); return null; }
      const i0 = Bo.findIndex((b) => b.t > t); if (i0 < 0) return null; const e = Bo[i0].o; if (!(e > 0)) return null;
      const seg = Bo.slice(i0).filter((b) => b.t <= Bo[i0].t + 150 * 60); if (seg.length < 5) return null;
      const q = (x) => Math.round((x / e - 1) * 1000); const h = [], l = [], c = [], tl = [], ts = [];
      for (const b of seg) { h.push(q(b.h)); l.push(q(b.l)); c.push(q(b.c)); ts.push(b.t); const r = byT.get(b.t); tl.push(r && (Lg ? r.c < r.ef : r.c > r.ef) ? 1 : 0); }
      return { e: +e.toFixed(2), h, l, c, tl: tl.join(""), ts, sym };
    };
    const killsFor = (m) => kills.filter((k) => k.side === m.side && k.ts > m.ts && k.ts - m.ts <= 600);
    const score = (row, expiry) => {
      const m = row._m, s = row._s, Lg = m.s === "C", Pp = EXITS[s.av];
      const sym = symFor(m.px, Lg, s.steps, expiry);
      needs.add(sym); // always refreshed at night: a saved pane chart stops updating once price moves away from that strike
      const p = pathFor(sym, m.ts, Lg);
      if (!p) return { sym, why: "no bars" };
      const mm = { ...m, e: p.e, h: p.h, l: p.l, c: p.c, tl: p.tl };
      const f = E.entryOf(mm, Pp);
      if (!f) return { sym, why: "no fill at the 5% bid" };
      const t = E.tradeReturn(f, Pp);
      const a = Math.max(0, f.e * (1 + t.r) - Pp.slip) / (f.e + Pp.slip) - 1;
      const fi = f.tod - m.tod - 1; // the bar the bid filled on (entryOf re-bases the path after it)
      const b = smallWin(f, p.ts.slice(fi + 1), m, killsFor(m), R, Pp.slip);
      return { sym, fill: f.e, a, b: b.ret, why_b: b.why, min_b: b.n, best: Math.max(0, ...f.h.slice(0, t.n + 1)) / 1000, heat: Math.min(0, ...f.l.slice(0, t.n + 1)) / 1000, min: t.n, startTod: f.tod };
    };
    for (const row of out) {
      const one = B.exp !== day ? score(row, B.exp) : null, zero0 = score(row, null);
      const main = one && one.fill != null ? one : zero0;
      row.dte = main === one ? 1 : 0;
      row.strike = main.sym;
      row.entry = main.fill != null ? main.fill.toFixed(2) : "";
      row.result_a = main.fill != null ? r1(main.a * 100) : null;
      row.result_b = main.fill != null ? r1(main.b * 100) : null;
      row.best = main.fill != null ? r1(main.best * 100) : null;
      row.heat = main.fill != null ? r1(main.heat * 100) : null;
      row.minutes = main.fill != null ? main.min : null;
      row.minutes_b = main.fill != null ? main.min_b : null;
      row.exit_b = main.fill != null ? main.why_b : "";
      row.result_a_0dte = zero0.fill != null ? r1(zero0.a * 100) : null;
      row.result_b_0dte = zero0.fill != null ? r1(zero0.b * 100) : null;
      row.minutes_0dte = zero0.fill != null ? zero0.min : null;
      row.minutes_b_0dte = zero0.fill != null ? zero0.min_b : null;
      row.start_tod_0dte = zero0.fill != null ? zero0.startTod : null;
      row.note = main.fill != null ? "" : (one ? `1DTE: ${one.why}; ` : "") + `0DTE: ${zero0.why}`;
      row.start_tod = main.fill != null ? main.startTod : null;
      // contracts it will want at night (1DTE + 0DTE)
      if (!B.opt[symFor(row._m.px, row._m.s === "C", row._s.steps, null)]) needs.add(symFor(row._m.px, row._m.s === "C", row._s.steps, null));
      if (B.exp !== day && !B.opt[symFor(row._m.px, row._m.s === "C", row._s.steps, B.exp)]) needs.add(symFor(row._m.px, row._m.s === "C", row._s.steps, B.exp));
    }
  } else {
    for (const row of out) { needs.add(symFor(row._m.px, row._m.s === "C", row._s.steps, null)); if (B.exp !== day) needs.add(symFor(row._m.px, row._m.s === "C", row._s.steps, B.exp)); }
  }
  // fade candidates that still need the 1 ITM contract's bars for cF / cG
  for (const m of M) if (m.x && m.x.cfSym && m.k === "P" && !B.opt[m.x.cfSym]) { const rv = m.x.rv; if (rv && m.tw !== 1 && rv.mv15 <= -1.5 && rv.ne5 === 0 && rv.st < 0.8 && rv.vk >= 90 && rv.so <= 20 && rv.dm >= 0.3 && m.tod < 255) needs.add(m.x.cfSym); }
  return { rows: out, needs: [...needs] };
}

// (b) the small-win exits on a filled path (f = entryOf result, ts = the bar times after the fill)
function smallWin(f, ts, m, kills, R, slip) {
  const c = SW_CFG, tp = c.tp, trail = c.trail, runnerMax = c.runnerMax, cutMin = c.cutMin, confirmBars = c.confirmBars, softCut = 0.10;
  const K = m.s === "C" ? "F" : "G";
  const r0 = R.find((r) => r.t === m.ts) || R.filter((r) => r.t <= m.ts).pop();
  const byT = new Map(R.map((r) => [r.t, r]));
  let held = 1, bank = 0, sold = false, soldAt = 0, peak = 0, stop = -c.stopPct, conf = false;
  const fin = (x, j, why) => ({ ret: Math.max(0, f.e * (1 + bank + held * x) - slip) / (f.e + slip) - 1, n: j, why });
  const N = Math.min(f.h.length, ts.length, (c.maxHold || 60) + 1);
  for (let j = 0; j < N; j++) {
    const hi = f.h[j] / 1000, lo = f.l[j] / 1000, cl = f.c[j] / 1000;
    if (lo <= stop + 1e-9) return fin(stop, j, sold ? "runner ratchet" : `stop -${Math.round(c.stopPct * 100)}%`);
    if (!sold && hi >= tp - 1e-9) { bank += 0.5 * tp; held = 0.5; sold = true; soldAt = j; stop = Math.max(stop, 0); peak = hi; }
    if (kills.some((k) => k.ts <= ts[j])) return fin(cl, j, "x after the mark");
    if (sold) { peak = Math.max(peak, hi); stop = Math.max(stop, 0, (1 + peak) * (1 - trail) - 1); if (j - soldAt >= runnerMax) return fin(cl, j, `runner ${runnerMax} min`); continue; }
    if (!conf) { const r = byT.get(ts[j]); if (r && r0 && r[K] < r0[K]) conf = true; else if (j + 1 >= confirmBars) return fin(cl, j, `no confirm in ${confirmBars} min`); }
    if (!conf && cl <= -softCut) return fin(cl, j, "cut -10% (no confirm)");
    if (j >= cutMin) return fin(cl, j, `no +${Math.round(tp * 100)}% by minute ${cutMin}`);
  }
  return fin(N ? f.c[N - 1] / 1000 : 0, N - 1, "end of bars");
}

// ---------- files ----------
const COLS = ["date", "time", "known_at", "avenue", "side", "strike", "dte", "port", "entry", "result_a", "result_b", "best", "heat", "minutes", "minutes_b", "exit_b", "result_a_0dte", "result_b_0dte", "flag", "both_charts",
  "spy_fear", "spy_greed", "call_fear", "call_greed", "put_fear", "put_greed", "vix_fear", "vix_greed", "real_in_trade", "real_same_move", "start_tod", "note", "minutes_0dte", "minutes_b_0dte", "start_tod_0dte"];
const q = (v) => { const s = v == null ? "" : String(v); return /[",\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s; };
const csvLine = (r) => COLS.map((k) => q(r[k])).join(",") + "\n";
function parseCsv(file) {
  if (!fs.existsSync(file)) return [];
  const L = fs.readFileSync(file, "utf8").trim().split("\n"); if (L.length < 2) return [];
  const H = L[0].split(",");
  return L.slice(1).map((l) => { const c = []; let cur = "", inq = false; for (let i = 0; i < l.length; i++) { const ch = l[i]; if (ch === '"') { if (inq && l[i + 1] === '"') { cur += '"'; i++; } else inq = !inq; continue; } if (ch === "," && !inq) { c.push(cur); cur = ""; continue; } cur += ch; } c.push(cur); return Object.fromEntries(H.map((h, i) => [h, c[i]])); });
}
function writeRows(file, rows, day) {
  const keep = parseCsv(file).filter((r) => r.date !== day); // a rerun of the same day replaces its rows
  fs.writeFileSync(file, COLS.join(",") + "\n" + keep.map(csvLine).join("") + rows.map(csvLine).join(""));
}
const REAL_COLS = ["date", "mark_tod", "side", "start_tod", "end_tod", "acct_pct", "ret_pct"];
function writeReal(file, rows, day) {
  const keep = parseCsv(file).filter((r) => r.date !== day);
  fs.writeFileSync(file, REAL_COLS.join(",") + "\n" + [...keep, ...rows].map((r) => REAL_COLS.map((k) => q(r[k])).join(",")).join("\n") + "\n");
}
// real trades as intervals: from the minute-by-minute busy record (side per minute)
function realIntervals(day, busy, trades) {
  const mins = [...busy.keys()].sort((a, b) => a - b), iv = [];
  for (const t of mins) { const s = busy.get(t), last = iv[iv.length - 1]; if (last && last.side === s && t <= last.end_tod + 1) last.end_tod = t; else iv.push({ date: day, side: s, start_tod: t, end_tod: t }); }
  const T = trades.filter((t) => t.day === day);
  return iv.map((x, k) => { const t = T[k]; const before = t ? t.balance - t.pnl : 0; return { ...x, mark_tod: t && t.mark ? t.mark.tod : x.start_tod, acct_pct: t && before > 0 ? r1((t.pnl / before) * 100) : "", ret_pct: t ? t.ret : "" }; });
}

// ---------- records ----------
const num = (v) => (v === "" || v == null ? null : +v);
function record(rows, k) {
  const R = rows.map((r) => num(r[k])).filter((v) => v != null);
  const won = R.filter((v) => v > 0).length;
  return { n: rows.length, filled: R.length, won, pct: R.length ? Math.round((won / R.length) * 100) : null, sum: r1(R.reduce((a, b) => a + b, 0)), avg: R.length ? r1(R.reduce((a, b) => a + b, 0) / R.length) : null, worst: R.length ? Math.min(...R) : null };
}
const fmtRec = (x) => (x.filled ? `${x.won}/${x.filled} won (${x.pct}%) · avg ${x.avg}% · worst ${x.worst}%` : "no fills");

// One $1,000 account taking whichever comes first (one trade at a time, full port, each trade's own % on the account;
// "half port" trend signals at half). Real small-win trades use their own account % (acct_pct).
function combine(rows, realRows, k, ids, withReal) {
  const ev = [];
  for (const r of rows) if (ids.includes(r.avenue) && num(r[k]) != null) { const s = num(r.start_tod), mins = num(k === "result_b" ? r.minutes_b : r.minutes) || 0; ev.push({ date: r.date, s, e: s + mins, eff: (num(r[k]) / 100) * (r.port === "half" ? 0.5 : 1), who: r.avenue, sig: `${r.time} ${NAME[r.avenue]} ${r.side === "C" ? "call" : "put"}` }); }
  if (withReal) for (const r of realRows) if (r.acct_pct !== "") ev.push({ date: r.date, s: num(r.start_tod), e: num(r.end_tod), eff: num(r.acct_pct) / 100, who: "real", sig: "small-win" });
  ev.sort((a, b) => (a.date < b.date ? -1 : a.date > b.date ? 1 : a.s - b.s || (a.who === "real" ? -1 : 1)));
  let eq = 1000, pk = 1000, mdd = 0, busy = { d: null, u: -1 }, n = 0, won = 0, worst = 0;
  for (const x of ev) { if (x.date === busy.d && x.s <= busy.u) continue; eq *= 1 + x.eff; n++; if (x.eff > 0) won++; worst = Math.min(worst, x.eff); busy = { d: x.date, u: x.e }; pk = Math.max(pk, eq); mdd = Math.max(mdd, (pk - eq) / pk); }
  return { eq, n, won, mdd, worst };
}
const usd = (x) => (x < 0 ? "-$" : "$") + Math.abs(Math.round(x)).toLocaleString("en-US");

// ---------- the account grid (the "Shadow Avenues Stats" Sheet), rebuilt every night ----------
// Every account x both exit styles x 25/50/100% of the account per trade, one trade at a time, first come, $1,000 start.
// "0DTE" = the saved days from Nov 3 (the baseline replay) plus each dry-run day's 0DTE twins; "1DTE" = dry-run days only.
const GRID_SETS = [["Small-win bot alone", [], true, false], ["Fade MAIN", ["fade"], false], ["Swing Break", ["swing"], false], ["Trend (safety check)", ["trend"], false, true], ["Trend (all)", ["trend"], false], ["Lined up", ["lined"], false], ["Smart dots", ["smart"], false],
  ["Trend (safety check) + Lined", ["trend", "lined"], false, true], ["Trend (safety check) + Lined + Swing", ["trend", "lined", "swing"], false, true], ["Swing + Fade", ["swing", "fade"], false], ["Trend (safety check) + Swing + Fade", ["trend", "swing", "fade"], false, true], ["All 5 (trend safe)", ["trend", "lined", "swing", "fade", "smart"], false, true],
  ["Small-win bot + Fade", ["fade"], true], ["Small-win bot + Swing", ["swing"], true], ["Small-win bot + Swing + Fade", ["swing", "fade"], true], ["Small-win bot + Trend (safety check) + Swing + Fade", ["trend", "swing", "fade"], true, true]];
const GRID_HEAD = ["Account", "Exits", "Size %", "End $", "Worst drop %", "Win %", "Trades", "Won", "Worst trade %", "Worst hit to account %", "Worst day %", "Green days", "Days traded"];
// sig rows: {date, avenue, port, both_charts, a, b, s, ma, mb}; real rows: {date, s, e, ret, acct}
function gridSim(sig, real, ids, k, size, withReal, safe) {
  const ev = [];
  for (const r of sig) { if (!ids.includes(r.avenue) || r[k] == null) continue; if (safe && r.avenue === "trend" && r.both_charts !== "yes") continue;
    ev.push({ d: r.date, s: r.s, e: r.s + ((k === "b" ? r.mb : r.ma) || 0), ret: r[k] / 100, eff: (r[k] / 100) * (r.port === "half" ? 0.5 : 1) * size }); }
  if (withReal) for (const r of real) if (r.acct != null) ev.push({ d: r.date, s: r.s, e: r.e, ret: r.ret / 100, eff: (r.acct / 100) * size });
  ev.sort((a, b) => (a.d < b.d ? -1 : a.d > b.d ? 1 : a.s - b.s));
  let eq = 1000, pk = 1000, mdd = 0, busy = { d: null, u: -1 }, n = 0, w = 0, worst = 0, worstAcct = 0, day = null, ds = 1000;
  const dayMap = {};
  for (const x of ev) { if (x.d === busy.d && x.s <= busy.u) continue; if (x.d !== day) { if (day) dayMap[day] = eq / ds - 1; day = x.d; ds = eq; }
    eq *= 1 + x.eff; n++; if (x.ret > 0) w++; worst = Math.min(worst, x.ret); worstAcct = Math.min(worstAcct, x.eff); busy = { d: x.d, u: x.e }; pk = Math.max(pk, eq); mdd = Math.max(mdd, (pk - eq) / pk); }
  if (day) dayMap[day] = eq / ds - 1;
  const dv = Object.values(dayMap);
  return [Math.round(eq), -Math.round(mdd * 100), n ? Math.round((w / n) * 100) : 0, n, w, Math.round(worst * 100), Math.round(worstAcct * 100), dv.length ? Math.round(Math.min(...dv) * 100) : 0, dv.filter((v) => v > 0).length, dv.length];
}
function gridTable(sig, real) {
  const out = [];
  for (const [name, ids, withReal, safe] of GRID_SETS) for (const [k, lab] of [["a", "own"], ["b", "small-win"]]) for (const size of [0.25, 0.5, 1]) {
    if (!ids.length && k === "b") continue;
    out.push([name, lab, size * 100, ...gridSim(sig, real, ids, k, size, withReal, safe)]);
  }
  return out.sort((x, y) => (x[0] < y[0] ? -1 : x[0] > y[0] ? 1 : x[1] < y[1] ? -1 : x[1] > y[1] ? 1 : x[2] - y[2]));
}
function writeGrid(dir) {
  const live = parseCsv(path.join(dir, "shadow.csv")), base = parseCsv(path.join(dir, "shadow_baseline.csv"));
  const realLive = parseCsv(path.join(dir, "shadow_real.csv")), realBase = parseCsv(path.join(dir, "shadow_baseline_real.csv"));
  const realOf = (R) => R.filter((r) => r.acct_pct !== "").map((r) => ({ date: r.date, s: num(r.start_tod), e: num(r.end_tod), ret: num(r.ret_pct), acct: num(r.acct_pct) }));
  const sigOf = (r, z) => ({ date: r.date, avenue: r.avenue, port: r.port, both_charts: r.both_charts, a: num(z ? r.result_a_0dte : r.result_a), b: num(z ? r.result_b_0dte : r.result_b),
    s: num(z ? r.start_tod_0dte : r.start_tod), ma: num(z ? r.minutes_0dte : r.minutes), mb: num(z ? r.minutes_b_0dte : r.minutes_b) });
  const liveDays = new Set(live.map((r) => r.date));
  const zero = [...base.filter((r) => !liveDays.has(r.date)).map((r) => sigOf(r, false)), ...live.map((r) => sigOf(r, r.dte === "1"))];
  // 1DTE: the 1DTE history (Alpaca bars, Nov 3-13, build_1dte_history.js) + dry-run days
  const hist1 = parseCsv(path.join(dir, "shadow_baseline_1dte.csv")).filter((r) => r.dte === "1" && !liveDays.has(r.date)), hist1Days = new Set(hist1.map((r) => r.date));
  const one = [...hist1.map((r) => sigOf(r, false)), ...live.filter((r) => r.dte === "1").map((r) => sigOf(r, false))];
  const zeroReal = realOf([...realBase.filter((r) => !liveDays.has(r.date)), ...realLive]);
  const oneReal = realOf([...parseCsv(path.join(dir, "shadow_baseline_1dte_real.csv")).filter((r) => hist1Days.has(r.date)), ...realLive.filter((r) => one.some((x) => x.date === r.date))]);
  const dates = (S) => { const d = [...new Set(S.map((x) => x.date))].sort(); return d.length ? `${d[0]} to ${d[d.length - 1]} (${d.length} days)` : "no days yet"; };
  const csvOut = (T) => GRID_HEAD.join(",") + "\n" + T.map((r) => r.map(q).join(",")).join("\n") + "\n";
  fs.writeFileSync(path.join(dir, "shadow_grid_0dte.csv"), csvOut(gridTable(zero, zeroReal)));
  fs.writeFileSync(path.join(dir, "shadow_grid_1dte.csv"), csvOut(gridTable(one, oneReal)));
  fs.writeFileSync(path.join(dir, "shadow_grid_days.txt"), `0DTE: ${dates(zero)}\n1DTE: ${dates(one)}\nupdated: ${new Date().toISOString()}\n`);
}

// The daily issue section
function section({ day, rows, all, real }) {
  const L = ["", "### What it passed on (shadow log, never traded)", ""];
  const today = rows;
  const passed = today.filter((r) => (num(r.result_a) > 0 || num(r.result_b) > 0) && r.real_in_trade === "no" && r.real_same_move === "no");
  if (passed.length) {
    L.push("**Won while the real bot sat out:**");
    for (const r of passed) L.push(`- ${r.time} ${NAME[r.avenue]} ${r.side === "C" ? "call" : "put"} ${r.strike.slice(-9)} @ ${r.entry}: own exits ${r.result_a}% · small-win exits ${r.result_b}% (best +${r.best}%, heat ${r.heat}%)`);
    L.push("");
  } else L.push("No shadow trade won while the real bot sat out today.", "");
  L.push("| Avenue | Signals today | Own exits today | Small-win exits today | Running record (own exits) | Running record (small-win exits) |", "|---|---|---|---|---|---|");
  for (const a of AVENUES) {
    const T = today.filter((r) => r.avenue === a.id), A = all.filter((r) => r.avenue === a.id);
    const ta = record(T, "result_a"), tb = record(T, "result_b"), ra = record(A, "result_a"), rb = record(A, "result_b");
    L.push(`| ${a.name} | ${T.length} | ${ta.filled ? `${ta.won}/${ta.filled} · ${ta.sum >= 0 ? "+" : ""}${ta.sum}%` : "—"} | ${tb.filled ? `${tb.won}/${tb.filled} · ${tb.sum >= 0 ? "+" : ""}${tb.sum}%` : "—"} | ${fmtRec(ra)} | ${fmtRec(rb)} |`);
  }
  const tw = all.filter((r) => r.avenue === "trend" && r.both_charts);
  if (tw.length) { const y = record(tw.filter((r) => r.both_charts === "yes"), "result_a"), nn = record(tw.filter((r) => r.both_charts === "no"), "result_a"); L.push("", `Trend safety check (both charts breaking your way), running: yes ${fmtRec(y)} · no ${fmtRec(nn)}`); }
  // combined accounts (running, first-come, $1,000)
  const trendSafe = all.filter((r) => r.avenue !== "trend" || r.both_charts === "yes");
  const C1 = combine(trendSafe, real, "result_a", ["trend", "lined"], false), C2 = combine(trendSafe, real, "result_a", ["trend", "lined", "swing"], false);
  L.push("", `Combined accounts (running, first come, one at a time, $1,000, own exits): Trend (safety check) + reversal dots ${usd(C1.eq)} · ${C1.n} trades · ${C1.won} won · worst drop ${Math.round(C1.mdd * 100)}% | All three (+ Swing Break) ${usd(C2.eq)} · ${C2.n} trades · ${C2.won} won · worst drop ${Math.round(C2.mdd * 100)}%`);
  // promotion check (never automatic)
  const days = [...new Set(all.map((r) => r.date))];
  L.push("");
  if (days.length < 10) L.push(`Promotion check: ${days.length} of 10 dry-run days so far. Nothing gets promoted automatically; you decide.`);
  else {
    const base0 = combine([], real, "result_a", [], true).eq;
    const hits = [];
    for (const a of AVENUES) for (const [k, lab] of [["result_a", "own exits"], ["result_b", "small-win exits"]]) {
      const x = record(all.filter((r) => r.avenue === a.id), k);
      if (!x.filled || x.pct < 85 || x.worst < -50) continue;
      const c = combine(all, real, k, [a.id], true);
      if (c.eq > base0) hits.push(`- **${a.name}** (${lab}): ${fmtRec(x)}; with the reversal first-come ${usd(c.eq)} vs reversal alone ${usd(base0)}`);
    }
    L.push(`Promotion check (${days.length} dry-run days, 85%+ wins, no loss over -50%, adds money with the reversal). Your call, nothing changes on its own:`);
    L.push(...(hits.length ? hits : ["- none yet"]));
  }
  L.push("", `All shadow signals: spy0dte/smallwin/shadow.csv`);
  return L.join("\n");
}

// ---------- live helper for swbot.js (log only; every call is wrapped so it can't stop the bot) ----------
class ShadowLive {
  constructor({ day, exp, log, fetchOpt }) { this.day = day; this.exp = exp; this.log = log; this.fetchOpt = fetchOpt; this.seen = new Set(); this.busy = new Map(); this.err = 0; this.fetched = new Set(); }
  // which side the real bot holds this minute ("C"/"P"), read only
  noteBot(barT, eng) {
    try { const p = eng.pos || eng.pending; if (!p) return; const tod = Math.round(((((barT % 86400) + 86400) % 86400) / 60) - 570); const s = p.m ? p.m.s : String(p.sym || "").slice(-9, -8); if (s === "C" || s === "P") this.busy.set(tod, s); } catch {}
  }
  async minute(saved) {
    try {
      const B = fromSaved(this.day, this.exp, saved); if (!B) return;
      let r = analyze(B, { busy: this.busy });
      const want = r.needs.filter((s) => !this.fetched.has(s) && !saved[s]).slice(0, 4);
      if (want.length) { for (const s of want) { this.fetched.add(s); try { saved[s] = await this.fetchOpt(s); } catch {} } r = analyze(fromSaved(this.day, this.exp, saved), { busy: this.busy }); }
      for (const row of r.rows) {
        const key = `${row.avenue}|${row.side}|${row.time}`;
        if (this.seen.has(key)) continue;
        this.seen.add(key);
        this.log("shadow_fire", { avenue: NAME[row.avenue], side: row.side, at: row.time, known_at: row.known_at, flag: row.flag, real_bot: row.real_in_trade, spy: [row.spy_fear, row.spy_greed], call: [row.call_fear, row.call_greed], put: [row.put_fear, row.put_greed], vix: [row.vix_fear, row.vix_greed] });
      }
    } catch (e) { if (this.err++ < 3) this.log("shadow_error", { err: String((e && e.message) || e).slice(0, 300) }); }
  }
  // night: fetch the contracts the scoring needs (added to `saved`, so they're kept in bars/<day>.json), score, write files
  async final(saved, st, dir) {
    try {
      // contracts fetched during the day only had bars up to then: refresh them to the full day first
      const tried = new Set();
      for (const s of this.fetched) { tried.add(s); try { saved[s] = await this.fetchOpt(s); } catch {} }
      for (let round = 0; round < 3; round++) {
        const B = fromSaved(this.day, this.exp, saved); if (!B) return "";
        const r = analyze(B, { score: true, busy: this.busy });
        const want = r.needs.filter((s) => !tried.has(s));
        if (!want.length) break;
        for (const s of want) { tried.add(s); try { saved[s] = await this.fetchOpt(s); } catch {} }
      }
      const md = finish(this.day, fromSaved(this.day, this.exp, saved), this.busy, st.trades, dir, this.seen);
      try { writeGrid(dir); } catch (e) { this.log("shadow_error", { err: "grid: " + String(e.message).slice(0, 200) }); }
      return md;
    } catch (e) { this.log("shadow_error", { err: String((e && e.stack) || e).slice(0, 600) }); return "\n\n_Shadow log: error tonight (" + String((e && e.message) || e).slice(0, 120) + "). The real bot is not affected._"; }
  }
}

function finish(day, B, busy, trades, dir, seenLive) {
  const real = realIntervals(day, busy, trades);
  const realTod = trades.filter((t) => t.day === day && t.mark).map((t) => ({ tod: t.mark.tod, s: t.mark.s }));
  const r = analyze(B, { score: true, busy, real: realTod });
  const rows = r.rows.map((x) => { const { _m, _s, ...rest } = x; if (seenLive) rest.note = (rest.note ? rest.note + "; " : "") + (seenLive.has(`${x.avenue}|${x.side}|${x.time}`) ? "seen live" : "found at night"); return rest; });
  const file = path.join(dir, "shadow.csv"), rf = path.join(dir, "shadow_real.csv");
  writeRows(file, rows, day);
  writeReal(rf, real, day);
  return section({ day, rows, all: parseCsv(file), real: parseCsv(rf) });
}

module.exports = { writeGrid, gridTable, GRID_HEAD, analyze, smallWin, fromSaved, normDay, finish, section, record, combine, parseCsv, realIntervals, writeRows, writeReal, ShadowLive, AVENUES, NAME, EXITS, COLS, EST_SHA256 };
