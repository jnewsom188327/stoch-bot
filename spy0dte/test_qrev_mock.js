// Dress rehearsal for the PUBLIC QQQ reversal bot: runs the real qbot.js against a fake Public API that replays a saved day on a fast clock.
//   node spy0dte/test_vfrev_mock.js 2026-11-19 dry|live
// LIVE here talks only to the fake API (orders are filled from the saved bars), nothing leaves this machine.
const fs = require("fs");
const os = require("os");
const path = require("path");

const day = process.argv[2] || "2026-11-19";
const mode = process.argv[3] || "dry";
const SRC = __dirname;
const TMP = fs.mkdtempSync(path.join(os.tmpdir(), "spy0dte-"));
for (const f of fs.readdirSync(SRC)) if (f.endsWith(".js")) fs.copyFileSync(path.join(SRC, f), path.join(TMP, f));

const B = JSON.parse(fs.readFileSync(path.join(process.env.MOCK_BARS || path.join(SRC, "..", "results", "qqq"), `bars_${day}.json`), "utf8")); // QQQ bars file
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
// ---------- fake Robinhood MCP (shapes copied from the real server's replies) ----------
const RH = process.env.MOCK_BROKER === "robinhood";
const rhState = { NEW: "confirmed", PENDING_NEW: "queued", FILLED: "filled", CANCELLED: "cancelled", REJECTED: "rejected" };
const idToSym = (id) => id.replace(/^opt-/, "");
function rhTool(name, a) {
  const D = (data) => ({ data, guide: "" });
  if (name === "get_accounts") return D({ accounts: [{ account_number: "5SM0MAIN", type: "margin", agentic_allowed: false, option_level: "option_level_3" }, { account_number: "528047145", type: "limited_margin", agentic_allowed: true, option_level: "option_level_3", nickname: "MCP" }] });
  if (name === "get_trade_approval_setting") return D({ setting: { account_number: a.account_number, human_must_approve_trades: false } });
  if (name === "get_option_chains") return D({ chains: [{ id: "chain-spy", symbol: "QQQ", expiration_dates: [day] }] });
  if (name === "get_option_instruments") {
    const t = a.type === "call" ? "C" : "P";
    const sym = "QQQ" + a.expiration_dates.slice(2, 4) + a.expiration_dates.slice(5, 7) + a.expiration_dates.slice(8, 10) + t + String(Math.round(+a.strike_price * 1000)).padStart(8, "0");
    return D({ instruments: [{ id: "opt-" + sym, expiration_date: a.expiration_dates, strike_price: a.strike_price, type: a.type, state: "active", tradability: "tradable" }] });
  }
  if (name === "get_portfolio") return D({ cash: "1000", buying_power: { buying_power: "1000.0000" } });
  if (name === "place_option_order") {
    const l = a.legs[0], id = "rh-" + (orders.size + 1);
    const nowMin = (NOW - base) / 60000;
    const tooEarly = a.type === "stop_market" && nowMin < 15;
    orders.set(id, { orderId: id, instrument: { symbol: idToSym(l.option_id), type: "OPTION" }, orderSide: l.side.toUpperCase(), orderType: a.type === "stop_market" ? "STOP" : "LIMIT", quantity: a.quantity, limitPrice: a.price, stopPrice: a.stop_price, status: tooEarly ? "REJECTED" : process.env.MOCK_STOP_STUCK && a.type === "stop_market" ? "PENDING_NEW" : "NEW", placedMs: NOW });
    return process.env.MOCK_NO_ID ? D({ message: "Order submitted" }) : D({ order: { id, state: "queued" } });
  }
  if (name === "get_option_orders" && !a.order_id) {
    const list = [...orders.values()].filter((o) => (a.state_group !== "open" || ["NEW", "PENDING_NEW"].includes(o.status)) && (!a.created_at_gte || o.placedMs >= Date.parse(a.created_at_gte)));
    return D({ orders: list.map((o) => ({ id: o.orderId, state: rhState[o.status], quantity: o.quantity, legs: [{ option_id: "opt-" + o.instrument.symbol, side: o.orderSide.toLowerCase() }] })) });
  }
  if (name === "get_option_orders") {
    const o = orders.get(a.order_id);
    if (!o) return D({ orders: [] });
    settle(o);
    const q = o.status === "FILLED" ? +o.quantity : 0;
    return D({ orders: [{ id: o.orderId, state: rhState[o.status] || "confirmed", quantity: o.quantity, processed_quantity: String(q), processed_premium: q ? String(Math.round(q * 100 * +o.averagePrice)) : "", updated_at: new RealDate(NOW).toISOString(), legs: [{ option_id: "opt-" + o.instrument.symbol, executions: q ? [{ price: o.averagePrice, quantity: String(q), timestamp: o.filledAt }] : [] }] }] });
  }
  if (name === "cancel_option_order") { const o = orders.get(a.order_id); if (o && (o.status === "NEW" || o.status === "PENDING_NEW")) o.status = "CANCELLED"; return D({}); }
  if (name === "get_option_positions") {
    const sym = a.option_ids ? idToSym(a.option_ids) : null;
    if (process.env.MOCK_BREAK && NOW >= base + 75 * 60000) return D({ positions: [] }); // 10:45: broker "loses" the position
    return D({ positions: Object.entries(pos).filter(([s, q]) => q && (!sym || s === sym)).map(([s, q]) => ({ option_id: "opt-" + s, type: "long", quantity: String(q) })) });
  }
  throw new Error("fake RH: unknown tool " + name);
}
const realFetch = global.fetch;
global.fetch = async (url, opts = {}) => {
  const u0 = new URL(url);
  if (u0.host === "api.robinhood.com") { calls.push("RH token"); return { ok: true, status: 200, headers: { get: () => "application/json" }, text: async () => JSON.stringify({ access_token: "at2", refresh_token: "rt2", expires_in: 3600 }) }; }
  if (u0.host === "agent.robinhood.com") {
    const msg = JSON.parse(opts.body);
    calls.push("RH " + (msg.params && msg.params.name || msg.method));
    const hdr = (ct) => ({ get: (k) => (k.toLowerCase() === "content-type" ? ct : k.toLowerCase() === "mcp-session-id" ? "sess-1" : null) });
    if (!msg.id) return { ok: true, status: 202, headers: hdr("application/json"), text: async () => "" };
    if (msg.method === "initialize") return { ok: true, status: 200, headers: hdr("application/json"), text: async () => JSON.stringify({ jsonrpc: "2.0", id: msg.id, result: { protocolVersion: "2025-06-18", capabilities: {}, serverInfo: { name: "rh" } } }) };
    let result;
    try { result = { content: [{ type: "text", text: JSON.stringify(rhTool(msg.params.name, msg.params.arguments)) }] }; }
    catch (e) { result = { isError: true, content: [{ type: "text", text: String(e.message) }] }; }
    const sse = `event: message\ndata: ${JSON.stringify({ jsonrpc: "2.0", id: msg.id, result })}\n\n`;
    return { ok: true, status: 200, headers: hdr("text/event-stream"), text: async () => sse };
  }
  return publicFetch(url, opts);
};
async function publicFetch(url, opts = {}) {
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
}

process.env.PUBLIC_API_SECRET = "fake";
if (RH) {
  process.env.SPY0DTE_BROKER = "robinhood";
  process.env.RH_TOKEN_KEY = "test-key";
  require(path.join(TMP, "rh.js")).saveTokens({ client_id: "c1", access_token: "at1", refresh_token: "rt1", expires_at: NOW + 3600e3 });
}
process.env.QQQ0DTE_PUBLIC_LIVE = mode === "live" ? "yes" : "";
process.env.MODE = "run";
process.on("exit", () => {
  const st = JSON.parse(fs.readFileSync(path.join(TMP, "qrev", "state.json"), "utf8"));
  console.error(`\n[mock] ${mode}: ${calls.length} API calls, orders sent ${orders.size}, open fake positions ${JSON.stringify(Object.fromEntries(Object.entries(pos).filter(([, q]) => q)))}, balance ${st.balance}`);
  if (Object.values(pos).some((q) => q)) { console.error("[mock] FAIL: position left open"); process.exitCode = 1; }
});
// MOCK_BRAKE=N: start with the safety brake on (paper only until N paper wins), to prove paper mode sends no orders
if (process.env.MOCK_BRAKE) {
  fs.mkdirSync(path.join(TMP, "qrev"), { recursive: true });
  const { freshState } = require(path.join(TMP, "ledger.js"));
  fs.writeFileSync(path.join(TMP, "qrev", "state.json"), JSON.stringify({ ...freshState(), brake: { need: +process.env.MOCK_BRAKE, half: false, target: null } }));
}
require(path.join(TMP, "qbot.js"));
