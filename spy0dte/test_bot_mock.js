// Dress rehearsal: runs the real bot.js against a fake Public API that replays a saved day on a fast clock.
//   node spy0dte/test_bot_mock.js 2026-11-17 dry|live
// LIVE here talks only to the fake API (orders are filled from the saved bars), nothing leaves this machine.
const fs = require("fs");
const os = require("os");
const path = require("path");

const day = process.argv[2] || "2026-11-17";
const mode = process.argv[3] || "dry";
const SRC = __dirname;
const TMP = fs.mkdtempSync(path.join(os.tmpdir(), "spy0dte-"));
for (const f of fs.readdirSync(SRC)) if (f.endsWith(".js")) fs.copyFileSync(path.join(SRC, f), path.join(TMP, f));

const B = JSON.parse(fs.readFileSync(path.join(SRC, "..", "results", `bars_${day}.json`), "utf8"));
const off = B.spy[0][0].slice(-6);
const base = Date.parse(day + "T09:30:00" + off);
const iso = (ms) => new Date(ms + Number(off.slice(0, 3)) * 3600000).toISOString().slice(0, 19) + off;
const spy = B.spy.map(([t, o, h, l, c, v]) => ({ ms: Date.parse(t), timestamp: t.slice(0, 19) + t.slice(-6), open: String(o), high: String(h), low: String(l), close: String(c), volume: String(v) }));
const opt = {};
for (const [sym, rows] of Object.entries(B.opt)) opt[sym] = rows.map(([i, o, h, l, c]) => ({ ms: base + i * 60000, timestamp: iso(base + i * 60000), open: String(o), high: String(h), low: String(l), close: String(c), volume: "5" }));

// ---------- fake clock ----------
let NOW = base - 10 * 60000; // 9:20 ET
const RealDate = Date;
class FakeDate extends RealDate {
  constructor(...a) { if (a.length) super(...a); else super(NOW); }
  static now() { return NOW; }
}
global.Date = FakeDate;
const realSetTimeout = setTimeout;
global.setTimeout = (fn, ms) => { NOW += ms || 0; return realSetTimeout(fn, 0); };

// bars visible at NOW: closed bars + the running (partial) one, like the real API
const visible = (bars) => bars.filter((b) => b.ms <= NOW).map(({ ms, ...b }) => b);
const barAt = (bars) => [...bars].reverse().find((b) => b.ms + 60000 <= NOW);

// ---------- fake broker ----------
const orders = new Map();
const pos = {};
function settle(o) {
  if (o.status !== "NEW") return;
  const bars = opt[o.instrument.symbol] || [];
  const since = bars.filter((b) => b.ms >= o.placedMs - 60000 && b.ms + 60000 <= NOW);
  let px = null;
  if (o.orderType === "LIMIT" && o.orderSide === "BUY") { const b = since.find((b) => +b.low <= +o.limitPrice - 0.01); if (b) px = +o.limitPrice; }
  if (o.orderType === "LIMIT" && o.orderSide === "SELL") { const b = barAt(bars); if (b && +b.close >= +o.limitPrice) px = +o.limitPrice; }
  if (o.orderType === "STOP") { const b = since.find((b) => +b.low <= +o.stopPrice); if (b) px = +o.stopPrice; }
  if (px != null) {
    o.status = "FILLED"; o.filledQuantity = o.quantity; o.averagePrice = px.toFixed(2); o.filledAt = new RealDate(NOW).toISOString();
    const s = o.instrument.symbol;
    pos[s] = (pos[s] || 0) + (o.orderSide === "BUY" ? 1 : -1) * +o.quantity;
    if (pos[s] < 0) throw new Error("fake broker: oversold " + s);
  }
}
const calls = [];
global.fetch = async (url, opts = {}) => {
  const u = new URL(url), p = u.pathname, m = opts.method || "GET", body = opts.body ? JSON.parse(opts.body) : null;
  calls.push(`${m} ${p}`);
  const ok = (j) => ({ ok: true, status: 200, text: async () => JSON.stringify(j) });
  if (p.endsWith("/access-tokens")) return ok({ accessToken: "fake" });
  if (p.endsWith("/trading/account")) return ok({ accounts: [{ accountId: "TEST1234", accountType: "BROKERAGE" }] });
  let mm;
  if ((mm = p.match(/historicdata\/(\w+)\/([^/]+)\/DAY\/ONE_MINUTE$/))) {
    const sym = decodeURIComponent(mm[2]);
    return ok({ regularMarket: { bars: visible(mm[1] === "EQUITY" ? spy : opt[sym] || []) } });
  }
  if (p.endsWith("/quotes")) {
    const quotes = body.instruments.map(({ symbol }) => {
      const b = barAt(opt[symbol] || []);
      if (!b) return { instrument: { symbol, type: "OPTION" }, outcome: "FAILED" };
      const c = +b.close, ts = new RealDate(NOW - 2000).toISOString();
      return { instrument: { symbol, type: "OPTION" }, outcome: "SUCCESS", last: b.close, bid: (c - 0.01).toFixed(2), ask: (c + 0.01).toFixed(2), bidTimestamp: ts, askTimestamp: ts };
    });
    return ok({ quotes });
  }
  if (p.endsWith("/option-expirations")) return ok({ expirations: [day, "2026-11-18", "2026-11-19"] });
  if (p.endsWith("/portfolio/v2") && process.env.MOCK_BREAK && NOW >= base + 75 * 60000) return ok({ buyingPower: { optionsBuyingPower: "100000" }, positions: [] }); // 10:45: Public "loses" the position
  if (p.endsWith("/portfolio/v2")) return ok({ buyingPower: { optionsBuyingPower: "100000" }, positions: Object.entries(pos).filter(([, q]) => q).map(([symbol, q]) => ({ instrument: { symbol, type: "OPTION" }, quantity: String(q) })) });
  if (p.endsWith("/preflight/single-leg")) return ok({ estimatedCost: "1" });
  if (p.endsWith("/order") && m === "POST") { orders.set(body.orderId, { ...body, status: process.env.MOCK_STOP_STUCK && body.orderType === "STOP" ? "PENDING_NEW" : "NEW", placedMs: NOW }); return ok({ orderId: body.orderId }); }
  if ((mm = p.match(/\/order\/([\w-]+)$/))) {
    const o = orders.get(mm[1]);
    if (!o) return { ok: false, status: 404, text: async () => "" };
    settle(o);
    if (m === "DELETE") { if (o.status === "NEW" || o.status === "PENDING_NEW") o.status = "CANCELLED"; return ok({}); }
    return ok(o);
  }
  return { ok: false, status: 400, text: async () => "unknown " + p };
};

process.env.PUBLIC_API_SECRET = "fake";
process.env.SPY0DTE_LIVE = mode === "live" ? "yes" : "";
process.env.MODE = "run";
process.on("exit", () => {
  const st = JSON.parse(fs.readFileSync(path.join(TMP, "state.json"), "utf8"));
  console.error(`\n[mock] ${mode}: ${calls.length} API calls, orders sent ${orders.size}, open fake positions ${JSON.stringify(Object.fromEntries(Object.entries(pos).filter(([, q]) => q)))}, balance ${st.balance}`);
  if (Object.values(pos).some((q) => q)) { console.error("[mock] FAIL: position left open"); process.exitCode = 1; }
});
require(path.join(TMP, "bot.js"));
