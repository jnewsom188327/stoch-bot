// Robinhood (Agentic / MCP account) broker for the bot: OAuth tokens, an MCP client, and the same order interface as
// public.js (place / order / cancel / positionQty / optionsBuyingPower). Prices still come from Public.
// Tokens live encrypted in spy0dte/rh_tokens.enc (AES-256-GCM). Key: secret RH_TOKEN_KEY, or if that isn't set,
// one derived from PUBLIC_API_SECRET. The repo is public, so the file is useless without that secret.
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const { execSync } = require("child_process");

const MCP_URL = "https://agent.robinhood.com/mcp/trading";
const TOKEN_URL = "https://api.robinhood.com/oauth2/token/";
const TOKEN_FILE = path.join(__dirname, "rh_tokens.enc");
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// ---------- token store ----------
function key() {
  const k = process.env.RH_TOKEN_KEY || (process.env.PUBLIC_API_SECRET ? "spy0dte-rh|" + process.env.PUBLIC_API_SECRET : "");
  if (!k) throw new Error("no key to read the Robinhood tokens (set RH_TOKEN_KEY or PUBLIC_API_SECRET)");
  return crypto.createHash("sha256").update(k).digest();
}
function saveTokens(t, { push = false } = {}) {
  const iv = crypto.randomBytes(12);
  const c = crypto.createCipheriv("aes-256-gcm", key(), iv);
  const enc = Buffer.concat([c.update(JSON.stringify(t), "utf8"), c.final()]);
  fs.writeFileSync(TOKEN_FILE, JSON.stringify({ v: 1, iv: iv.toString("base64"), tag: c.getAuthTag().toString("base64"), data: enc.toString("base64") }) + "\n");
  if (push && process.env.GITHUB_ACTIONS) pushTokens();
}
function loadTokens() {
  if (!fs.existsSync(TOKEN_FILE)) throw new Error("No Robinhood login saved yet: run the 'Robinhood login' workflow first");
  const f = JSON.parse(fs.readFileSync(TOKEN_FILE, "utf8"));
  const d = crypto.createDecipheriv("aes-256-gcm", key(), Buffer.from(f.iv, "base64"));
  d.setAuthTag(Buffer.from(f.tag, "base64"));
  return JSON.parse(Buffer.concat([d.update(Buffer.from(f.data, "base64")), d.final()]).toString("utf8"));
}
// a refreshed token may replace the old one: commit it right away so a crash can't lose the login
function pushTokens() {
  try {
    execSync(`git config user.name "spy0dte-bot" && git config user.email "spy0dte-bot@users.noreply.github.com" && git add "${TOKEN_FILE}" && (git diff --cached --quiet || git commit -q -m "rh login refresh")`, { stdio: "pipe", shell: "/bin/bash" });
    for (let i = 0; i < 4; i++) {
      try { execSync("git pull -q --rebase origin main && git push -q origin HEAD:main", { stdio: "pipe", shell: "/bin/bash" }); return; } catch { execSync("sleep 3"); }
    }
  } catch (e) { console.log("token push warning:", String(e.message).slice(0, 200)); }
}

// ---------- MCP client (streamable HTTP) ----------
class RobinhoodMCP {
  constructor({ log = () => {} } = {}) {
    this.t = loadTokens();
    this.session = null;
    this.n = 0;
    this.log = log;
  }

  async refresh() {
    const body = new URLSearchParams({ grant_type: "refresh_token", refresh_token: this.t.refresh_token, client_id: this.t.client_id, resource: MCP_URL });
    const res = await fetch(TOKEN_URL, { method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded", Accept: "application/json" }, body, signal: AbortSignal.timeout(20000) });
    const text = await res.text();
    if (!res.ok) throw new Error(`Robinhood login refresh failed (HTTP ${res.status}): ${text.slice(0, 200)}. Run the 'Robinhood login' workflow again.`);
    const j = JSON.parse(text);
    this.t.access_token = j.access_token;
    if (j.refresh_token) this.t.refresh_token = j.refresh_token;
    this.t.expires_at = Date.now() + (+j.expires_in || 3600) * 1000;
    saveTokens(this.t, { push: true });
    this.log("rh_token_refreshed", { expires_in: j.expires_in, new_refresh_token: !!j.refresh_token });
  }

  async ensureToken() {
    if (!this.t.access_token || !this.t.expires_at || this.t.expires_at - Date.now() < 5 * 60 * 1000) await this.refresh();
  }

  async rpc(method, params, { notify = false, retry = true } = {}) {
    await this.ensureToken();
    const msg = notify ? { jsonrpc: "2.0", method, params } : { jsonrpc: "2.0", id: ++this.n, method, params };
    const headers = { "Content-Type": "application/json", Accept: "application/json, text/event-stream", Authorization: `Bearer ${this.t.access_token}`, "MCP-Protocol-Version": "2025-06-18" };
    if (this.session) headers["Mcp-Session-Id"] = this.session;
    let res;
    try {
      res = await fetch(MCP_URL, { method: "POST", headers, body: JSON.stringify(msg), signal: AbortSignal.timeout(30000) });
    } catch (e) {
      if (retry) { await sleep(1500); return this.rpc(method, params, { notify, retry: false }); }
      throw e;
    }
    const sid = res.headers.get("mcp-session-id");
    if (sid) this.session = sid;
    if (res.status === 401 && retry) { await this.refresh(); return this.rpc(method, params, { notify, retry: false }); }
    if (res.status === 404 && this.session && retry && method !== "initialize") { this.session = null; await this.init(); return this.rpc(method, params, { notify, retry: false }); }
    if ((res.status === 429 || res.status >= 500) && retry) { await sleep(2500); return this.rpc(method, params, { notify, retry: false }); }
    if (notify) return null;
    const text = await res.text();
    if (!res.ok) throw new Error(`Robinhood ${method} HTTP ${res.status}: ${text.slice(0, 300)}`);
    let reply = null;
    if ((res.headers.get("content-type") || "").includes("text/event-stream")) {
      for (const line of text.split(/\r?\n/)) {
        if (!line.startsWith("data:")) continue;
        try { const j = JSON.parse(line.slice(5).trim()); if (j.id === msg.id) reply = j; } catch {}
      }
    } else reply = JSON.parse(text);
    if (!reply) throw new Error(`Robinhood ${method}: no reply`);
    if (reply.error) throw new Error(`Robinhood ${method}: ${reply.error.message || JSON.stringify(reply.error)}`);
    return reply.result;
  }

  async init() {
    if (this.inited) return;
    await this.rpc("initialize", { protocolVersion: "2025-06-18", capabilities: {}, clientInfo: { name: "spy0dte-bot", version: "1.0" } });
    await this.rpc("notifications/initialized", {}, { notify: true });
    this.inited = true;
  }

  async call(name, args = {}) {
    await this.init();
    const r = await this.rpc("tools/call", { name, arguments: args });
    const text = (r.content || []).filter((c) => c.type === "text").map((c) => c.text).join("");
    let j = r.structuredContent || null;
    if (!j) { try { j = JSON.parse(text); } catch { j = { text }; } }
    if (r.isError) throw new Error(`Robinhood ${name}: ${(text || JSON.stringify(j)).slice(0, 400)}`);
    return j && j.data !== undefined ? j.data : j;
  }

  async tools() { await this.init(); return (await this.rpc("tools/list", {})).tools || []; }
}

// ---------- broker with the same interface as public.js ----------
const STATE = { queued: "PENDING_NEW", unconfirmed: "PENDING_NEW", confirmed: "NEW", partially_filled: "PARTIALLY_FILLED", filled: "FILLED", cancelled: "CANCELLED", voided: "CANCELLED", rejected: "REJECTED", failed: "REJECTED" };

class RobinhoodBroker {
  constructor({ accountNumber = "", log = () => {} } = {}) {
    this.mcp = new RobinhoodMCP({ log });
    this.acct = accountNumber;
    this.log = log;
    this.ids = new Map(); // OSI symbol -> option_id
    this.chainId = null;
  }

  async setup() {
    const a = await this.mcp.call("get_accounts");
    const accts = (a && a.accounts) || [];
    const mine = accts.filter((x) => x.agentic_allowed);
    const pick = this.acct ? mine.find((x) => x.account_number === this.acct) : mine.length === 1 ? mine[0] : null;
    if (!pick) throw new Error(`Robinhood: no agent-tradable account${this.acct ? " " + this.acct : ""} found`);
    if (!["option_level_2", "option_level_3"].includes(pick.option_level)) throw new Error(`Robinhood account needs options level 2+ (has ${pick.option_level || "none"})`);
    this.acct = pick.account_number;
    this.acctType = pick.type;
    const s = await this.mcp.call("get_trade_approval_setting", { account_number: this.acct });
    if (s && s.setting && s.setting.human_must_approve_trades) throw new Error("Robinhood trade approvals are ON for the agent account: orders would wait for you. Turn them off in the Robinhood app.");
    const ch = await this.mcp.call("get_option_chains", { underlying_symbol: "SPY" });
    this.chainId = ((ch && ch.chains) || []).find((c) => c.symbol === "SPY").id;
    return { account: this.acct, type: pick.type, optionLevel: pick.option_level };
  }

  async optionId(sym) {
    if (this.ids.has(sym)) return this.ids.get(sym);
    const exp = `20${sym.slice(3, 5)}-${sym.slice(5, 7)}-${sym.slice(7, 9)}`;
    const type = sym[9] === "C" ? "call" : "put";
    const strike = (+sym.slice(10) / 1000).toFixed(4);
    const r = await this.mcp.call("get_option_instruments", { chain_id: this.chainId, expiration_dates: exp, strike_price: strike, type });
    const inst = ((r && r.instruments) || []).find((x) => x.type === type && (+x.strike_price).toFixed(4) === strike && x.expiration_date === exp);
    if (!inst || inst.tradability !== "tradable") throw new Error(`Robinhood: ${sym} not found or not tradable`);
    this.ids.set(sym, inst.id);
    return inst.id;
  }

  // o = { symbol, side: BUY|SELL, type: LIMIT|STOP, qty, limit, stop, openClose: OPEN|CLOSE }
  async place(o) {
    const option_id = await this.optionId(o.symbol);
    const args = {
      account_number: this.acct,
      legs: [{ option_id, side: o.side.toLowerCase(), position_effect: o.openClose === "OPEN" ? "open" : "close" }],
      quantity: String(o.qty),
      type: o.type === "STOP" ? "stop_market" : "limit",
      time_in_force: "gfd",
      ref_id: crypto.randomUUID(),
    };
    if (o.type === "STOP") args.stop_price = o.stop.toFixed(2);
    else args.price = o.limit.toFixed(2);
    const since = new Date(Date.now() - 120000).toISOString();
    let r = null, err = null;
    try { r = await this.mcp.call("place_option_order", args); } catch (e) { err = e; }
    if (r && r.customer_approval_required) throw new Error("Robinhood sent the order to you for approval: turn off trade approvals for the agent account");
    let id = (r && ((r.order && r.order.id) || r.id || r.order_id || (r.orders && r.orders[0] && r.orders[0].id))) || null;
    if (!id) {
      // the reply didn't give an id (or the call errored after Robinhood took it): find the order we just sent
      await sleep(1500);
      const o = await this.mcp.call("get_option_orders", { account_number: this.acct, created_at_gte: since });
      const mine = ((o && o.orders) || []).find((x) => (x.legs || []).some((l) => l.option_id === option_id && l.side === args.legs[0].side) && String(+x.quantity) === String(+args.quantity));
      if (mine) { id = mine.id; this.log("rh_order_found", { id, note: "order id read back from the order list" }); }
    }
    if (!id) throw err || new Error(`Robinhood place_option_order: no order id in reply ${JSON.stringify(r).slice(0, 300)}`);
    return id;
  }

  async order(id) {
    const r = await this.mcp.call("get_option_orders", { account_number: this.acct, order_id: id });
    const o = r && r.orders && r.orders[0];
    if (!o) { const e = new Error(`Robinhood order ${id} not found`); e.status = 404; throw e; }
    const q = +o.processed_quantity || 0;
    const ex = (o.legs || []).flatMap((l) => l.executions || []);
    let avg = q > 0 && +o.processed_premium > 0 ? +o.processed_premium / (q * 100) : 0;
    if (!avg && ex.length) avg = ex.reduce((a, e) => a + +e.price * +e.quantity, 0) / ex.reduce((a, e) => a + +e.quantity, 0);
    const last = ex.map((e) => e.timestamp).sort().pop();
    return { status: STATE[o.state] || o.state, filledQuantity: String(q), averagePrice: avg ? avg.toFixed(4) : "0", filledAt: last || o.updated_at, rejectReason: o.state === "rejected" || o.state === "failed" ? o.reject_reason || o.state : "", raw_state: o.state };
  }

  async cancel(id) {
    let first = await this.order(id).catch(() => null);
    if (first && ["FILLED", "CANCELLED", "REJECTED"].includes(first.status)) return first;
    try { await this.mcp.call("cancel_option_order", { account_number: this.acct, order_id: id }); }
    catch (e) { this.log("rh_cancel_note", { id, err: String(e.message).slice(0, 200) }); }
    for (let i = 0; i < 15; i++) {
      const o = await this.order(id);
      if (["FILLED", "CANCELLED", "REJECTED"].includes(o.status)) return o;
      await sleep(800);
    }
    throw new Error(`order ${id} would not cancel`);
  }

  async positionQty(sym) {
    const option_id = await this.optionId(sym);
    const r = await this.mcp.call("get_option_positions", { account_number: this.acct, option_ids: option_id, nonzero: true });
    return ((r && r.positions) || []).filter((p) => p.option_id === option_id).reduce((a, p) => a + (p.type === "short" ? -1 : 1) * Math.round(+p.quantity), 0);
  }

  async optionsBuyingPower() {
    const r = await this.mcp.call("get_portfolio", { account_number: this.acct });
    return +((r && r.buying_power && r.buying_power.buying_power) || 0);
  }

  // emergency: cancel every open order in the agent account (it only holds the bot's orders)
  async cancelAllOpen() {
    const open = await this.openOptionOrders();
    for (const o of open) { try { await this.cancel(o.id); } catch (e) { this.log("rh_cancel_note", { id: o.id, err: String(e.message).slice(0, 200) }); } }
    return open.length;
  }

  // used by the safety close
  async openOptionPositions() {
    const r = await this.mcp.call("get_option_positions", { account_number: this.acct, nonzero: true });
    return ((r && r.positions) || []).filter((p) => Math.round(+p.quantity) !== 0);
  }
  async openOptionOrders() {
    const r = await this.mcp.call("get_option_orders", { account_number: this.acct, state_group: "open" });
    return (r && r.orders) || [];
  }
  async optionBid(option_id) {
    const r = await this.mcp.call("get_option_quotes", { instrument_ids: [option_id] });
    const q = r && r.results && r.results[0] && r.results[0].quote;
    return q ? { bid: +q.bid_price, ask: +q.ask_price } : null;
  }
  async placeById({ option_id, side, qty, limit }) {
    const r = await this.mcp.call("place_option_order", { account_number: this.acct, legs: [{ option_id, side, position_effect: "close" }], quantity: String(qty), type: "limit", price: limit.toFixed(2), time_in_force: "gfd", ref_id: crypto.randomUUID() });
    return (r && ((r.order && r.order.id) || r.id || r.order_id)) || null;
  }
}

module.exports = { RobinhoodMCP, RobinhoodBroker, saveTokens, loadTokens, MCP_URL, TOKEN_URL, TOKEN_FILE };
