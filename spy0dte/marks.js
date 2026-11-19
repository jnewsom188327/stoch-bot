// Live marks: the same mark loop as build_day.js, run on the closed 1-minute bars seen so far today.
// Input bars are Public's own bar objects ({timestamp, open, high, low, close, volume}).
const { loadCore } = require("./core");

const MAX_TOD = 330; // build_day.js: marks before 9:40 (tod<10) or after 3:00 (tod>330) are dropped

// Public option bars -> the same shape build_day.js feeds CORE: minutes with no trades dropped, volume "1"
function optToCoreBars(bars) {
  return bars
    .filter((b) => +b.volume > 0)
    .map((b) => ({ timestamp: b.timestamp, open: String(b.open), high: String(b.high), low: String(b.low), close: String(b.close), volume: "1" }));
}
function spyToCoreBars(bars) {
  return bars.map((b) => ({ timestamp: b.timestamp, open: String(b.open), high: String(b.high), low: String(b.low), close: String(b.close), volume: String(b.volume) }));
}
const barStart = (b) => Math.floor(Date.parse(b.timestamp) / 1000);
// CORE keeps times as ET clock seconds (epoch + UTC offset); this gives a bar's time in that form
const coreT = (b) => {
  const m = String(b.timestamp).match(/([+-])(\d\d):(\d\d)$/);
  const off = m ? (m[1] === "-" ? -1 : 1) * (+m[2] * 3600 + +m[3] * 60) : -18000;
  return Math.floor(Date.parse(b.timestamp) / 60000) * 60 + off;
};

// Keep only bars that have finished (bar start + 60s <= nowSec)
function closedOnly(bars, nowSec) {
  return bars.filter((b) => barStart(b) + 60 <= nowSec);
}

function contractFor(day, side, px) {
  // build_day.js strike: call = first strike above; put = first strike below (or 1 under if price sits on a strike)
  const Lg = side === "long";
  const K = Lg ? Math.floor(px) + 1 : Number.isInteger(px) ? px - 1 : Math.floor(px);
  const yymmdd = day.slice(2, 4) + day.slice(5, 7) + day.slice(8, 10);
  return { K, cp: Lg ? "C" : "P", sym: "SPY" + yymmdd + (Lg ? "C" : "P") + String(K * 1000).padStart(8, "0") };
}
// The 0DTE option charts the pane arrows are read from, for a SPY close
function paneStrikes(close) {
  return { call: Math.floor(close) + 1, put: Math.ceil(close) - 1 };
}
function osi(day, cp, K, expiry) {
  const d = expiry || day;
  return "SPY" + d.slice(2, 4) + d.slice(5, 7) + d.slice(8, 10) + cp + String(Math.round(K * 1000)).padStart(8, "0");
}

/**
 * computeMarks(day, spyBars, optBars) -> { marks, kills, rows }
 *  spyBars: Public SPY 1m bars (closed only), optBars: { OSI: Public bars } for the 0DTE pane strikes.
 *  marks: [{ ts, t, k:"A"|"D"|"P", src, side, s:"C"|"P", grade, px, tod, busy, tw, ag, kill, contract }]
 */
function computeMarks(day, spyBars, optBars) {
  const L = loadCore();
  const S = L.S;
  const toRes = (bars) => JSON.stringify({ regularMarket: { bars } });
  const parsed = L.parseBars(toRes(spyToCoreBars(spyBars)));
  if (!parsed) return { marks: [], kills: [], rows: [] };
  const R = L.compute(L.cleanPrints(parsed.filter((x) => !x.live && !x.fill)));
  S.spy = R;
  // build_day.js runs signals on R.slice(0,-1) because its last bar is the live one on the chart pages;
  // here every bar passed in is already closed, so the newest closed bar is included.
  S.sigs = L.signals(R);
  const byT = new Map(R.map((r) => [r.t, r]));
  const idx = new Map(R.map((r, i) => [r.t, i]));
  const atrPct = (t) => {
    const i = idx.get(t);
    if (i == null || i < 14) return 0;
    let s = 0;
    for (let k = i - 13; k <= i; k++) s += Math.max(R[k].h - R[k].l, Math.abs(R[k].h - R[k - 1].c), Math.abs(R[k].l - R[k - 1].c));
    return (100 * (s / 14)) / R[i].c;
  };
  const OB = {};
  for (const [sym, bars] of Object.entries(optBars || {})) {
    const p = L.parseBars(toRes(optToCoreBars(bars)));
    OB[sym] = (p || []).filter((x) => !x.live && !x.fill).sort((x, y) => x.t - y.t);
  }
  const marks = [];
  for (const s of S.sigs) {
    if (s.kind === "add") marks.push(["A", s, null]);
    if (s.kind === "stall") {
      const d = L.dotTrade(s);
      if (d) {
        let kill = 0;
        for (const a of S.sigs) if (a.kind === "kill" && a.side === s.side && a.t > s.t && a.t - s.t <= 600) kill = 1;
        marks.push(["D", d, null, kill]);
      }
    }
  }
  const a = L.vixArrows(R);
  for (const t of a.g) marks.push(["P", { t, side: "long" }, "SPY"]);
  for (const t of a.f) marks.push(["P", { t, side: "short" }, "SPY"]);
  for (const sym of Object.keys(OB)) {
    const cp = sym[9], K = +sym.slice(10) / 1000;
    const rows = L.compute(L.cleanPrints(OB[sym]));
    for (const t of L.vixArrows(rows).g) {
      const r = byT.get(t);
      if (!r) continue;
      if ((cp === "C" ? Math.floor(r.c) + 1 : Math.ceil(r.c) - 1) !== K) continue;
      marks.push(["P", { t, side: cp === "C" ? "long" : "short" }, cp === "C" ? "call" : "put"]);
    }
  }
  const out = [];
  for (const [k, m0, src, kill] of marks) {
    const s = m0.px ? m0 : L.dotTrade(m0);
    if (!s) continue;
    const tod = L.etMin(s.t) - 570;
    if (tod > MAX_TOD || tod < 10) continue;
    const Lg = s.side === "long";
    const r0 = byT.get(s.t) || {};
    const d = Lg ? 1 : -1;
    out.push({
      ts: s.t, t: L.hmLabel(s.t), k, src, side: s.side, s: Lg ? "C" : "P", grade: s.grade || null, px: s.px, tod,
      busy: atrPct(s.t) >= 0.048 ? 1 : 0, tw: d * (r0.col || 0) > 0 ? 1 : 0, ag: d * (r0.ag || 0), kill: kill || 0,
      contract: contractFor(day, s.side, s.px),
    });
  }
  out.sort((x, y) => x.ts - y.ts); // stable, same order as build_day.js
  const kills = S.sigs.filter((x) => x.kind === "kill").map((x) => ({ ts: x.t, side: x.side }));
  return { marks: out, kills, rows: R };
}

module.exports = { computeMarks, closedOnly, contractFor, paneStrikes, osi, barStart, coreT };
