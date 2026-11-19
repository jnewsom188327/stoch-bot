// SPY 0DTE bot rules: which marks to take, the contract, the entry, the exits, the size ladder and the shutoffs.
// The same engine runs DRY RUN (orders logged, fills judged on real 1-minute option bars exactly like the
// Edge Stress Test) and LIVE (orders sent to Public, fills read back from Public).

const CFG = {
  startStake: 1000,
  kinds: ["D", "P"],     // white dots + pane arrows (SPY, call, put); "A" (arrows) not traded
  lastEntryTod: 210,     // minutes after 9:30 -> no new entries from 1:00 PM
  firstEntryTod: 10,     // backtest: no marks before 9:40 (Robinhood: 15, its option stops are refused before 9:45)
  posCheckSec: 20,       // live: how often the position is checked against the broker
  stopCheckSec: 5,       // live: how often the resting stop is checked for a fill
  minPrice: 0.8,         // skip contracts under $0.80
  maxSpread: 0.10,       // skip if (ask-bid)/mid > 10%
  staleSec: 30,          // skip if the quote is older than this
  entryDisc: 0.05,       // limit 5% under the option's price at the mark
  limitDown: true,       // round that limit DOWN to the cent, so it's always at least 5% under
  cancelMin: 5,          // unfilled entry cancelled after 5 minutes
  tradeThrough: 0.01,    // a limit only counts as filled if the option trades 1 cent through it
  slip: 0.01,            // slippage, each way, per contract
  tp: 0.10,              // +10%
  runnerMin: 15,         // sell the rest at minute 15
  xMin: 10,              // after an x: out at minute 10 (or right away if red)
  maxHold: 120,          // minutes
  flattenAtTod: 338,     // 3:08 PM: nothing held into the close
  // size: always full port (live = Public's buying power at that moment; dry run = the bot's paper balance)
  pct: 1.0,
  stopPct: 0.75,
  // shutoffs
  stopConfirmSec: 30,    // a stop not showing as working at Public by then = sell + stop for the day
  dayMaxLoss: 0.30, dayLockAt: 0.25, dayGiveBack: 1 / 3, reviewStops: 2, reviewWindow: 10,
  fractional: false,     // replay-only: fractional contracts, to compare 1:1 with the backtest sim
  simUnroundedFill: false, // replay-only: the sim checks fills against the un-rounded 95% price (live orders are in cents)
};

const r2 = (x) => Math.round(x * 100) / 100;
const WORKING = ["NEW", "PARTIALLY_FILLED", "PENDING_REPLACE"]; // Public order statuses that mean "live at the exchange"

class Engine {
  /**
   * @param o.state   persisted ledger (mutated)
   * @param o.market  { nowC(), quote(sym), optBars(sym), expiryFor(dte) }
   * @param o.broker  null = DRY RUN, else a PublicAPI
   * @param o.log     (event, data) => void
   */
  constructor({ state, market, broker = null, log, cfg = {} }) {
    this.cfg = { ...CFG, ...cfg };
    this.st = state;
    this.mk = market;
    this.br = broker;
    this.live = !!broker;
    this.log = log;
    this.pending = null;
    this.pos = null;
    this.kills = [];
  }

  halted() { return this.st.halt || this.st.reviewHold; }
  todOf(c) { return (((c % 86400) + 86400) % 86400) / 60 - 570; }

  // ------------------------------------------------------------------ marks
  async onMarks(marks, kills) {
    this.kills = kills || this.kills; // every x printed so far today
    for (const m of marks) {
      const why = this.markSkip(m);
      if (why) { this.log("mark_skip", { mark: brief(m), why }); continue; }
      await this.tryEntry(m);
      if (this.pending || this.pos) break; // one trade at a time: first qualifying mark of the minute wins
    }
  }

  markSkip(m) {
    if (this.halted()) return "stopped: " + (this.st.reviewHold ? "waiting for your review" : this.st.halt);
    if (this.pos || (this.lastExitBarT != null && m.ts <= this.lastExitBarT)) return "in a trade (marks that print while in a trade are ignored)";
    if (!this.cfg.kinds.includes(m.k)) return "arrows not traded (dots + pane arrows only)";
    if (m.tod >= this.cfg.lastEntryTod) return "after 1:00 PM";
    if (m.tod < this.cfg.firstEntryTod) return "before the first entry time";
    if (m.tw !== 1) return "trend line not your way";
    if (m.ag === -1) return "shading against you";
    return null;
  }

  async tryEntry(m) {
    const c = this.cfg;
    const sym = m.contract.sym; // 0DTE, the backtest's strike (first one out of the money)
    const q = await this.mk.quote(sym, m);
    if (!q) return this.log("mark_skip", { mark: brief(m), sym, why: "no quote" });
    const why = q.stale ? `stale quote (${q.ageSec}s old)` : !(q.bid > 0 && q.ask > 0) ? "no bid/ask"
      : q.ref < c.minPrice ? `under $${c.minPrice.toFixed(2)} ($${q.ref.toFixed(2)})`
      : q.spreadPct > c.maxSpread ? `spread ${(q.spreadPct * 100).toFixed(1)}% > ${c.maxSpread * 100}%` : null;
    if (why) return this.log("mark_skip", { mark: brief(m), sym, why, quote: q });
    const raw = q.ref * (1 - c.entryDisc);
    const limit = c.limitDown ? Math.floor(raw * 100 + 1e-9) / 100 : r2(raw); // orders are in cents
    const cost = (limit + c.slip) * 100;
    // Full port. Live: Public's options buying power right now (margin account: unsettled sale proceeds count),
    // but never more than the bot's own money (day-start buying power + today's closed P&L), so it never borrows.
    const bp = this.live ? await this.br.optionsBuyingPower() : null;
    const budget = (this.live ? Math.min(bp, this.st.balance) : this.st.balance) * c.pct;
    if (this.live && bp > this.st.balance + 1) this.log("size_cap", { publicBuyingPower: Math.round(bp), botMoney: Math.round(this.st.balance) });
    let qty = c.fractional ? budget / cost : Math.floor(budget / cost);
    if (this.live) qty = Math.min(qty, Math.floor(budget / (limit * 100)));
    if (!(qty >= (c.fractional ? 1e-9 : 1))) return this.log("mark_skip", { mark: brief(m), sym, why: `size under 1 contract (budget $${budget.toFixed(0)}, cost $${cost.toFixed(0)})` });

    if (this.pending) await this.cancelPending("replaced by a new mark");
    const order = { symbol: sym, side: "BUY", type: "LIMIT", qty, limit, openClose: "OPEN" };
    let id = "dry-" + m.ts + "-" + m.k;
    if (this.live) id = await this.br.place(order);
    else if (this.mk.preflight) await this.mk.preflight(order); // dry run: Public checks the order, nothing is sent
    this.pending = { m, sym, qty, limit, fillAt: c.simUnroundedFill ? q.ref * (1 - c.entryDisc) : limit, id, markT: m.ts, placedC: this.mk.nowC() };
    this.log(this.live ? "order_buy" : "order_buy_DRY", { mark: brief(m), sym, qty, limit, ref: q.ref, bid: q.bid, ask: q.ask, budget: Math.round(budget) });
  }

  async cancelPending(why) {
    const p = this.pending;
    if (!p) return;
    this.pending = null;
    if (this.live) {
      const o = await this.br.cancel(p.id);
      const filled = Math.round(+(o.filledQuantity || 0));
      if (filled > 0) { // partly filled before the cancel: keep what we got
        this.log("entry_partial", { sym: p.sym, filled, of: p.qty });
        return this.openPosition(p, filled, +o.averagePrice, this.barOf(o.filledAt));
      }
    }
    this.log("entry_cancel", { sym: p.sym, limit: p.limit, why });
  }

  // ------------------------------------------------------------------ every tick
  async tick() {
    const nowC = this.mk.nowC();
    if (this.pending) await this.checkPending(nowC);
    if (this.pos) await this.manage(nowC);
    if (this.todOf(nowC) >= this.cfg.flattenAtTod && (this.pos || this.pending)) await this.flatten("3:08 PM: nothing held into the close");
  }

  async checkPending(nowC) {
    const p = this.pending, c = this.cfg;
    if (!this.live) {
      // Edge Stress Test fill rule: any of the 6 option bars from the one after the mark trades 1 cent under the limit
      const bars = this.mk.optBars(p.sym).filter((b) => b.t >= p.markT + 60 && b.t <= p.markT + 60 + c.cancelMin * 60);
      const f = bars.find((b) => b.l <= p.fillAt - c.tradeThrough + 1e-9);
      if (f) { this.pending = null; return this.openPosition(p, p.qty, p.limit, f.t); }
      if (nowC >= p.markT + 60 + (c.cancelMin + 1) * 60) await this.cancelPending("not filled in 5 minutes");
      return;
    }
    const o = await this.br.order(p.id);
    if (o.status === "FILLED") { this.pending = null; return this.openPosition(p, Math.round(+o.filledQuantity), +o.averagePrice, this.barOf(o.filledAt)); }
    if (o.status === "PARTIALLY_FILLED") return this.cancelPending("part filled: keep what filled and protect it now");
    if (["REJECTED", "CANCELLED", "EXPIRED"].includes(o.status)) { this.pending = null; throw new Error(`entry order ${o.status}: ${o.rejectReason || ""}`); }
    if (nowC >= p.placedC + c.cancelMin * 60) await this.cancelPending("not filled in 5 minutes");
  }

  barOf(iso) { // fill time -> its bar start in CORE time
    const nowC = this.mk.nowC();
    if (!iso) return Math.floor(nowC / 60) * 60;
    const off = nowC - Math.floor(Date.now() / 1000);
    return Math.floor((Date.parse(iso) / 1000 + off) / 60) * 60;
  }

  async openPosition(p, qty, price, fillBarT) {
    const c = this.cfg;
    const pos = {
      m: p.m, sym: p.sym, qty, left: qty, entry: price, cost: price + c.slip, fillBarT,
      stopPct: c.stopPct, stop: r2(price * (1 - c.stopPct)), sold: false, done: [], nBars: 0, lastBarT: fillBarT,
      stopId: null, xAt: null,
    };
    this.pos = pos;
    this.log(this.live ? "entry_fill" : "entry_fill_DRY", { sym: pos.sym, qty, price, stop: pos.stop });
    await this.placeStop(pos.stop, qty);
  }

  async placeStop(level, qty) {
    const pos = this.pos, c = this.cfg;
    if (pos.stopId && this.live) await this.br.cancel(pos.stopId);
    pos.stop = level;
    if (this.live) {
      pos.stopId = await this.br.place({ symbol: pos.sym, side: "SELL", type: "STOP", qty, stop: level, openClose: "CLOSE" });
      // The stop must show as working at Public within 30 s; if not, the bot sells and stops for the day
      const t0 = Date.now();
      let o = null;
      for (;;) {
        o = await this.br.order(pos.stopId).catch(() => null);
        if (o && WORKING.includes(o.status)) break;
        if (o && o.status === "FILLED") { this.log("order_stop", { sym: pos.sym, qty, stop: level, note: "filled at once" }); return this.closed(pos.left, +o.averagePrice, pos.sold ? "breakeven stop" : `stop -${Math.round(pos.stopPct * 100)}%`, !pos.sold); }
        if (Date.now() - t0 >= c.stopConfirmSec * 1000) throw new Error(`stop order not working at the broker after ${c.stopConfirmSec}s (status ${o ? o.status : "unknown"}${o && o.rejectReason ? ": " + o.rejectReason : ""})`);
        await new Promise((r) => setTimeout(r, 2000));
      }
      this.log("stop_confirmed", { sym: pos.sym, status: o.status, sec: Math.round((Date.now() - t0) / 1000) });
    }
    this.log(this.live ? "order_stop" : "order_stop_DRY", { sym: pos.sym, qty, stop: level });
  }

  // x = the white dot's x (a same-side kill within 10 minutes of the dot); only dots carry it in the backtest
  xFor(pos) {
    if (pos.m.k !== "D") return null;
    const k = this.kills.find((x) => x.side === pos.m.side && x.ts > pos.m.ts && x.ts - pos.m.ts <= 600);
    return k ? k.ts : null;
  }

  async manage(nowC) {
    const pos = this.pos, c = this.cfg;
    if (!this.live) {
      // one decision per closed option bar after the fill bar, in the backtest's order
      const bars = this.mk.optBars(pos.sym).filter((b) => b.t > pos.lastBarT);
      for (const b of bars) {
        if (!this.pos) return;
        const i = pos.nBars++;
        pos.lastBarT = b.t;
        this.exitBarT = b.t;
        await this.step(i, { hi: b.h, lo: b.l, close: b.c, barT: b.t });
      }
      return;
    }
    // LIVE: did the broker stop fill? (checked every few seconds; the quote below is checked every tick)
    if (pos.stopId && (!pos.stopCheckedAt || Date.now() - pos.stopCheckedAt >= c.stopCheckSec * 1000)) {
      pos.stopCheckedAt = Date.now();
      const o = await this.br.order(pos.stopId);
      if (o.status === "FILLED") return this.closed(pos.left, +o.averagePrice, pos.sold ? "breakeven stop" : `stop -${Math.round(pos.stopPct * 100)}%`, !pos.sold);
      if (["REJECTED", "CANCELLED", "EXPIRED"].includes(o.status)) throw new Error(`stop order ${o.status}: ${o.rejectReason || ""}`);
    }
    if (!pos.checkedAt || Date.now() - pos.checkedAt >= c.posCheckSec * 1000) {
      const have = await this.br.positionQty(pos.sym);
      pos.checkedAt = Date.now();
      if (have !== pos.left) throw new Error(`position check: the broker shows ${have} ${pos.sym}, bot expects ${pos.left}`);
    }
    const q = await this.mk.quote(pos.sym);
    if (!q || !(q.bid > 0)) return;
    this.exitBarT = Math.floor(nowC / 60) * 60; // a live exit happens during this minute's bar
    const i = Math.floor((nowC - pos.fillBarT) / 60) - 2; // last fully closed bar index after the fill bar
    await this.step(i, { hi: q.bid, lo: q.bid, close: q.bid, bid: q.bid, live: true });
  }

  // One decision step. i = bars since the fill bar (0 = first full minute after the fill).
  async step(i, o) {
    const pos = this.pos, c = this.cfg, E = pos.entry;
    // 1) stop (dry run; live it's the broker's stop order)
    if (!this.live && o.lo <= pos.stop + 1e-9) return this.closed(pos.left, pos.stop, pos.sold ? "breakeven stop" : `stop -${Math.round(pos.stopPct * 100)}%`, !pos.sold);
    // 2) +10%: sell half (1 contract: all of it), stop to breakeven
    if (!pos.sold && o.hi >= E * (1 + c.tp) - 1e-9) {
      const px = this.live ? o.bid : r2(E * (1 + c.tp));
      const half = c.fractional ? pos.left / 2 : pos.qty === 1 ? 1 : Math.floor(pos.qty / 2);
      pos.sold = true;
      await this.sell(half, px, half >= pos.left ? "+10% all out (1 contract)" : "+10% half");
      if (!this.pos) return;
      await this.placeStop(r2(E), pos.left);
    }
    if (!this.pos) return;
    // 3) the x (white-dot trades only): everything out at minute 10
    const xT = this.xFor(pos);
    if (xT && !pos.xAt) { pos.xAt = xT; this.log("x_printed", { sym: pos.sym }); }
    if (pos.xAt && i >= c.xMin) return this.sellAll(o, "x printed: out at minute 10");
    // 4) runner out at minute 15 (only once the half is sold)
    if (pos.sold && i >= 1 && i >= c.runnerMin) return this.sellAll(o, "runner: minute 15");
    // 5) max hold
    if (i >= c.maxHold) return this.sellAll(o, "max hold 120 min");
  }

  async sellAll(o, why) {
    return this.sell(this.pos.left, this.live ? o.bid : o.close, why);
  }

  // Sell at the bid or better. DRY: fills at the price given (bar close / level) minus slippage.
  async sell(qty, px, why) {
    const pos = this.pos;
    if (!this.live) return this.closed(qty, px, why);
    if (pos.stopId) { const s = await this.br.cancel(pos.stopId); pos.stopId = null; if (s.status === "FILLED") return this.closed(pos.left, +s.averagePrice, pos.sold ? "breakeven stop" : `stop -${Math.round(pos.stopPct * 100)}%`, !pos.sold); }
    let left = qty, got = 0, value = 0;
    for (let tries = 0; tries < 6 && left > 0; tries++) {
      const q = await this.mk.quote(pos.sym);
      const limit = r2(Math.max(0.01, (q && q.bid) || px));
      const id = await this.br.place({ symbol: pos.sym, side: "SELL", type: "LIMIT", qty: left, limit, openClose: "CLOSE" });
      this.log("order_sell", { sym: pos.sym, qty: left, limit, why });
      await new Promise((r) => setTimeout(r, 4000));
      let st = await this.br.order(id);
      if (st.status !== "FILLED") st = await this.br.cancel(id);
      const f = Math.round(+(st.filledQuantity || 0));
      if (f > 0) { got += f; value += f * +st.averagePrice; left -= f; }
    }
    if (left > 0) throw new Error(`could not sell ${left} ${pos.sym} after 6 tries`);
    return this.closed(got, value / got, why);
  }

  // Book a (partial) exit. hitStop = the original stop (counts for the shutoffs)
  async closed(qty, px, why, hitStop = false) {
    const pos = this.pos, c = this.cfg;
    const exitPx = Math.max(0, px - c.slip);
    pos.done.push({ qty, px: exitPx, why });
    pos.left -= qty;
    pos.hitStop = pos.hitStop || hitStop;
    this.log(this.live ? "exit" : "exit_DRY", { sym: pos.sym, qty, px: r2(px), why });
    if (pos.left > 1e-9) return;
    if (pos.stopId && this.live) { await this.br.cancel(pos.stopId); pos.stopId = null; }
    this.pos = null;
    this.lastExitBarT = this.exitBarT != null ? this.exitBarT : Math.floor(this.mk.nowC() / 60) * 60 - 60;
    const pnl = pos.done.reduce((a, d) => a + d.qty * 100 * (d.px - pos.cost), 0);
    const ret = pos.done.reduce((a, d) => a + d.qty * d.px, 0) / pos.qty / pos.cost - 1;
    const before = this.st.balance;
    this.st.balance = r2(Math.max(0, before + pnl));
    const t = {
      day: this.st.day, mark: brief(pos.m), sym: pos.sym, qty: r2(pos.qty), entry: pos.entry, ret: Math.round(ret * 1000) / 10,
      pnl: r2(pnl), balance: r2(this.st.balance), exits: pos.done.map((d) => `${r2(d.qty)}@${d.px.toFixed(2)} ${d.why}`).join("; "), dry: !this.live,
    };
    this.st.trades.push(t);
    this.log("trade", t);
    this.st.last10 = [...(this.st.last10 || []), pos.hitStop ? 1 : 0].slice(-c.reviewWindow);
    this.afterTrade(pos);
  }

  afterTrade(pos) {
    const c = this.cfg, st = this.st;
    if (pos.hitStop) st.halt = "a -75% stop hit";
    if (st.last10.filter(Boolean).length >= c.reviewStops) st.reviewHold = `${c.reviewStops} of the last ${st.last10.length} trades hit the -75% stop`;
    // day shutoffs, on closed trades only
    const day = st.balance - st.dayStart;
    st.dayBest = Math.max(st.dayBest, day);
    if (!st.halt && st.balance <= st.dayStart * (1 - c.dayMaxLoss)) st.halt = "down 30% on the day";
    if (!st.halt && st.dayBest >= st.dayStart * c.dayLockAt && day <= st.dayBest * (1 - c.dayGiveBack)) st.halt = `gave back a third of the day's best (+$${st.dayBest.toFixed(0)})`;
    if (st.halt || st.reviewHold) this.log("shutoff", { why: st.halt || st.reviewHold });
  }

  // Close everything the bot holds or has working, then stop for the day
  async flatten(why, halt = false) {
    this.log("flatten", { why });
    if (this.pending) await this.cancelPending(why);
    if (this.pos) {
      if (this.live) {
        // trust Public's position, not the bot's: sell whatever is really there
        const pos = this.pos;
        if (pos.stopId) {
          const s = await this.br.cancel(pos.stopId).catch((e) => { this.log("stop_cancel_failed", { err: String(e.message).slice(0, 200) }); return {}; });
          pos.stopId = null;
          if (s.status === "FILLED") return this.closed(pos.left, +s.averagePrice, "stop", !pos.sold);
        }
        const have = await this.br.positionQty(pos.sym);
        if (have > 0) { pos.left = have; await this.sell(have, 0.01, why); }
        else { const q = await this.mk.quote(pos.sym).catch(() => null); await this.closed(pos.left, (q && q.bid) || 0, why + " (Public showed no position; price is a guess)"); }
      } else {
        const bars = this.mk.optBars(this.pos.sym);
        const q = await this.mk.quote(this.pos.sym).catch(() => null);
        const px = q && q.bid > 0 ? q.bid : bars.length ? bars[bars.length - 1].c : 0;
        await this.closed(this.pos.left, px, why);
      }
    }
    if (this.live && this.br.cancelAllOpen) {
      const n = await this.br.cancelAllOpen().catch((e) => { this.log("cancel_all_failed", { err: String(e.message).slice(0, 200) }); return 0; });
      if (n) this.log("cancelled_open_orders", { count: n });
    }
    if (halt) this.st.halt = this.st.halt || why;
  }
}

function brief(m) {
  return { t: m.t, k: m.k, src: m.src || "", s: m.s, tod: m.tod, tw: m.tw, ag: m.ag, px: m.px };
}

module.exports = { Engine, CFG };
