// 3:30 PM ET safety close: finds ANY open option position in the Public account and closes it with a limit at the bid
// (cancelling that contract's open orders first, e.g. a resting stop). Runs whether or not the main bot is running,
// and ignores dry run / live: it always acts on the real account. Turn it off with repo variable SPY0DTE_SAFETY = off.
const fs = require("fs");
const path = require("path");
const { PublicAPI, sleep } = require("./public");

const r2 = (x) => Math.round(x * 100) / 100;
const OPEN = ["NEW", "PARTIALLY_FILLED", "PENDING_REPLACE", "PENDING_NEW", "QUEUED"];

function etNow() {
  const p = Object.fromEntries(new Intl.DateTimeFormat("en-US", { timeZone: "America/New_York", year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", second: "2-digit", hourCycle: "h23" }).formatToParts(new Date()).map((x) => [x.type, x.value]));
  return { day: `${p.year}-${p.month}-${p.day}`, min: +p.hour * 60 + +p.minute, hms: `${p.hour}:${p.minute}:${p.second}` };
}

async function main() {
  const t = etNow();
  const lines = [];
  const log = (event, data = {}) => { const row = { at: etNow().hms, event, ...data }; lines.push(row); console.log(`${row.at} ${event} ${JSON.stringify(data)}`); };
  if (process.env.SPY0DTE_SAFETY === "off") return console.log("Safety close is turned off (SPY0DTE_SAFETY = off).");
  // two cron times cover summer/winter clocks; only the one landing 3:20-4:14 PM ET acts
  if (!process.env.FORCE && (t.min < 15 * 60 + 20 || t.min > 16 * 60 + 14)) return console.log(`Not the 3:30 PM ET run (it is ${t.hms} ET); exiting.`);

  const api = new PublicAPI(process.env.PUBLIC_API_SECRET, { accountId: process.env.PUBLIC_ACCOUNT_ID || "" });
  await api.auth();
  const p = await api.portfolio();
  const isOpt = (x) => x && x.instrument && String(x.instrument.type).toUpperCase() === "OPTION";
  const positions = ((p && p.positions) || []).filter((x) => isOpt(x) && Math.round(+x.quantity) !== 0);
  log("safety_check", { account: "…" + String(api.accountId).slice(-4), optionPositions: positions.map((x) => `${x.instrument.symbol} x${x.quantity}`) });

  let problems = 0;
  for (const pos of positions) {
    const sym = pos.instrument.symbol;
    try {
      // cancel that contract's open orders (a resting stop would hold the contracts)
      for (const o of ((p && p.orders) || []).filter((o) => o.instrument && o.instrument.symbol === sym && OPEN.includes(o.status))) {
        await api.cancel(o.orderId);
        log("cancelled_order", { sym, orderId: o.orderId, type: o.type || o.orderType, side: o.side || o.orderSide });
      }
      let left = Math.round(+pos.quantity);
      const side = left > 0 ? "SELL" : "BUY"; // a short option is bought back at the ask
      left = Math.abs(left);
      for (let tries = 0; tries < 8 && left > 0; tries++) {
        const q = (await api.quotes([sym], "OPTION"))[sym];
        const px = q ? (side === "SELL" ? +q.bid : +q.ask) : 0;
        if (!(px > 0)) { log("no_price", { sym, side, note: side === "SELL" ? "no bid" : "no ask" }); await sleep(5000); continue; }
        const limit = r2(px);
        const id = await api.place({ symbol: sym, side, type: "LIMIT", qty: left, limit, openClose: "CLOSE" });
        log("order_close", { sym, side, qty: left, limit });
        await sleep(5000);
        let st = await api.order(id);
        if (st.status !== "FILLED") st = await api.cancel(id);
        const f = Math.round(+(st.filledQuantity || 0));
        if (f > 0) { left -= f; log("closed", { sym, qty: f, price: st.averagePrice }); }
      }
      const still = Math.abs(await api.positionQty(sym));
      if (still > 0) { problems++; log("STILL_OPEN", { sym, qty: still, note: "CHECK YOUR PUBLIC ACCOUNT" }); }
    } catch (e) {
      problems++;
      log("ERROR", { sym, err: String(e.message || e).slice(0, 300), note: "CHECK YOUR PUBLIC ACCOUNT" });
    }
  }

  const md = [
    `## Safety close · ${t.day} · ${etNow().hms} ET`,
    "",
    positions.length ? `Open option positions found: ${positions.map((x) => `${x.instrument.symbol} x${x.quantity}`).join(", ")}` : "No open option positions. Nothing to do.",
    ...lines.filter((l) => !["safety_check"].includes(l.event)).map((l) => `- ${l.at} ${l.event} ${JSON.stringify(Object.fromEntries(Object.entries(l).filter(([k]) => !["at", "event"].includes(k))))}`),
    problems ? "\n**⚠ Something is still open or errored. Check your Public account now.**" : "",
  ].join("\n");
  fs.mkdirSync(path.join(__dirname, "summaries"), { recursive: true });
  fs.writeFileSync(path.join(__dirname, "summaries", `${t.day}-safety.md`), md + "\n");
  if (process.env.GITHUB_STEP_SUMMARY) fs.appendFileSync(process.env.GITHUB_STEP_SUMMARY, md + "\n");
  // only bother you when it actually had to close something or failed
  if (positions.length || problems) fs.writeFileSync(path.join(__dirname, "summaries", `${t.day}-safety.notify`), problems ? "PROBLEM: check Public" : `closed ${positions.length} position(s)`);
  if (problems) process.exitCode = 1;
}

main().catch((e) => { console.error(e); process.exit(1); });
