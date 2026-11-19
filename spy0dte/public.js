// Small Public.com API client (prices + orders). Docs: https://public.com/api/docs
const crypto = require("crypto");

const BASE = "https://api.public.com";
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

class PublicAPI {
  constructor(secret, { accountId = "", log = () => {} } = {}) {
    if (!secret) throw new Error("PUBLIC_API_SECRET is missing (Settings > Secrets and variables > Actions)");
    this.secret = secret;
    this.accountId = accountId;
    this.token = null;
    this.tokenAt = 0;
    this.log = log;
  }

  async auth() {
    const r = await this.raw("POST", "/userapiauthservice/personal/access-tokens", { secret: this.secret, validityInMinutes: 1440 }, false);
    if (!r || !r.accessToken) throw new Error("Public login failed: no accessToken returned");
    this.token = r.accessToken;
    this.tokenAt = Date.now();
    if (!this.accountId) {
      const a = await this.req("GET", "/userapigateway/trading/account");
      const accts = (a && a.accounts) || [];
      const brk = accts.filter((x) => String(x.accountType || "").toUpperCase() === "BROKERAGE");
      const pick = brk.length === 1 ? brk[0] : accts.length === 1 ? accts[0] : null;
      if (!pick) throw new Error(`Public: found ${accts.length} accounts; set the PUBLIC_ACCOUNT_ID variable to pick one`);
      this.accountId = pick.accountId;
    }
    return this.accountId;
  }

  // HTTP with retries for 429 / 5xx / network blips (3 tries); anything else throws
  async raw(method, path, body, withAuth = true) {
    let last;
    for (let i = 0; i < 3; i++) {
      try {
        const headers = { "Content-Type": "application/json" };
        if (withAuth) headers.Authorization = `Bearer ${this.token}`;
        const res = await fetch(BASE + path, { method, headers, body: body ? JSON.stringify(body) : undefined, signal: AbortSignal.timeout(15000) });
        const text = await res.text();
        if (res.status === 429 || res.status >= 500) { last = new Error(`${method} ${path} -> HTTP ${res.status} ${text.slice(0, 200)}`); await sleep(1500 * (i + 1)); continue; }
        if (!res.ok) { const e = new Error(`${method} ${path} -> HTTP ${res.status} ${text.slice(0, 300)}`); e.status = res.status; throw e; }
        return text ? JSON.parse(text) : {};
      } catch (e) {
        if (e.status) throw e; // a real 4xx: don't retry
        last = e;
        await sleep(1500 * (i + 1));
      }
    }
    throw last;
  }

  async req(method, path, body) {
    if (!this.token || Date.now() - this.tokenAt > 20 * 3600 * 1000) await this.auth();
    try {
      return await this.raw(method, path, body);
    } catch (e) {
      if (e.status === 401) { await this.auth(); return this.raw(method, path, body); }
      throw e;
    }
  }

  // ---------- market data ----------
  async bars(symbol, type = "EQUITY") {
    const q = type === "EQUITY" ? "?tradingSessionToggle=REGULAR_HOURS" : "";
    const r = await this.req("GET", `/userapigateway/historicdata/${type}/${encodeURIComponent(symbol)}/DAY/ONE_MINUTE${q}`);
    return ((r && r.regularMarket && r.regularMarket.bars) || []).filter((b) => {
      const hm = String(b.timestamp).slice(11, 16);
      return hm >= "09:30" && hm <= "15:59";
    });
  }

  async quotes(symbols, type = "OPTION") {
    const r = await this.req("POST", `/userapigateway/marketdata/${this.accountId}/quotes`, { instruments: symbols.map((symbol) => ({ symbol, type })) });
    const out = {};
    for (const q of (r && r.quotes) || []) if (q && q.instrument) out[q.instrument.symbol] = q;
    return out;
  }

  async expirations(symbol = "SPY") {
    const r = await this.req("POST", `/userapigateway/marketdata/${this.accountId}/option-expirations`, { instrument: { symbol, type: "EQUITY" } });
    return ((r && (r.expirations || r.expirationDates)) || []).map(String).sort();
  }

  // ---------- account ----------
  async portfolio() {
    return this.req("GET", `/userapigateway/trading/${this.accountId}/portfolio/v2`);
  }
  async positionQty(symbol) {
    const p = await this.portfolio();
    const pos = ((p && p.positions) || []).find((x) => x.instrument && x.instrument.symbol === symbol);
    return pos ? Math.round(+pos.quantity) : 0;
  }
  async optionsBuyingPower() {
    const p = await this.portfolio();
    const b = (p && p.buyingPower) || {};
    return +(b.optionsBuyingPower ?? b.cashOnlyBuyingPower ?? 0);
  }

  // ---------- orders ----------
  orderBody({ symbol, side, type, qty, limit, stop, openClose }) {
    const body = {
      orderId: crypto.randomUUID(),
      instrument: { symbol, type: "OPTION" },
      orderSide: side,
      orderType: type,
      expiration: { timeInForce: "DAY" },
      quantity: String(qty),
      openCloseIndicator: openClose,
    };
    if (limit != null) body.limitPrice = limit.toFixed(2);
    if (stop != null) body.stopPrice = stop.toFixed(2);
    return body;
  }
  async preflight(o) {
    const b = this.orderBody(o);
    delete b.orderId;
    return this.req("POST", `/userapigateway/trading/${this.accountId}/preflight/single-leg`, b);
  }
  async place(o) {
    const b = this.orderBody(o);
    await this.req("POST", `/userapigateway/trading/${this.accountId}/order`, b);
    return b.orderId;
  }
  async order(id) {
    // a brand-new order can 404 for a moment while Public indexes it
    for (let i = 0; i < 4; i++) {
      try { return await this.req("GET", `/userapigateway/trading/${this.accountId}/order/${id}`); }
      catch (e) { if (e.status !== 404 || i === 3) throw e; await sleep(1000); }
    }
  }
  async cancel(id) {
    try { await this.req("DELETE", `/userapigateway/trading/${this.accountId}/order/${id}`); }
    catch (e) { if (e.status !== 404 && e.status !== 400) throw e; }
    // confirm it is done (cancel is not guaranteed instant)
    for (let i = 0; i < 10; i++) {
      const o = await this.order(id);
      if (["CANCELLED", "QUEUED_CANCELLED", "FILLED", "REJECTED", "EXPIRED", "REPLACED"].includes(o.status)) return o;
      await sleep(700);
    }
    throw new Error(`order ${id} would not cancel`);
  }
}

module.exports = { PublicAPI, sleep };
