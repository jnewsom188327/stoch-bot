// One-time Robinhood login for the bot (run from the "Robinhood login" workflow).
// 1) registers the bot as an OAuth client, 2) opens a GitHub issue with the Robinhood sign-in link,
// 3) waits for you to comment the address you land on (http://localhost:1455/callback?code=...),
// 4) trades the code for tokens (PKCE: the code is useless without this run's secret verifier),
// 5) saves them encrypted to spy0dte/rh_tokens.enc, deletes your comment, and proves the login works.
const crypto = require("crypto");
const { execSync } = require("child_process");
const { saveTokens, RobinhoodBroker, MCP_URL, TOKEN_URL } = require("./rh");

const REG_URL = "https://agent.robinhood.com/oauth/trading/register";
const AUTH_URL = "https://robinhood.com/oauth";
const REDIRECT = "http://localhost:1455/callback";
const REPO = process.env.GITHUB_REPOSITORY;
const b64u = (b) => b.toString("base64").replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const gh = (args, input) => execSync(`gh ${args}`, { input, encoding: "utf8", stdio: ["pipe", "pipe", "pipe"] });
const fs = require("fs");
function closeWith(issue, text) {
  fs.writeFileSync("/tmp/rh_comment.md", text);
  try { gh(`issue comment ${issue} -R ${REPO} --body-file /tmp/rh_comment.md`); } catch {}
  try { gh(`issue close ${issue} -R ${REPO}`); } catch {}
}

async function main() {
  // 1) dynamic client registration
  const reg = await fetch(REG_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json", Accept: "application/json" },
    body: JSON.stringify({ client_name: "spy0dte-bot", redirect_uris: [REDIRECT], grant_types: ["authorization_code", "refresh_token"], response_types: ["code"], token_endpoint_auth_method: "none", scope: "internal" }),
  });
  const regText = await reg.text();
  if (!reg.ok) throw new Error(`client registration failed: HTTP ${reg.status} ${regText.slice(0, 300)}`);
  const client_id = JSON.parse(regText).client_id;
  console.log("registered client", client_id);

  // 2) PKCE + sign-in link
  const verifier = b64u(crypto.randomBytes(48));
  const challenge = b64u(crypto.createHash("sha256").update(verifier).digest());
  const state = b64u(crypto.randomBytes(16));
  const url = `${AUTH_URL}?` + new URLSearchParams({ response_type: "code", client_id, redirect_uri: REDIRECT, scope: "internal", state, code_challenge: challenge, code_challenge_method: "S256", resource: MCP_URL });
  const body = [
    "**Robinhood login for the SPY 0DTE bot.** You have 20 minutes.",
    "",
    "1. Open this link (on a computer browser if your iPad keeps jumping to the Robinhood app):",
    "",
    url,
    "",
    "2. Sign in to Robinhood and approve. Pick your **MCP** agent account if asked.",
    "3. You'll land on a page that won't load (`localhost`). That's expected. **Copy the whole address** from the address bar (it starts with `http://localhost:1455/callback?code=`).",
    "4. **Right away** (the code expires in about a minute), paste it as a **comment on this issue**. Tip: have this issue open in a second tab so you can paste fast. The bot picks it up within 2 seconds, saves the login, and deletes your comment.",
  ].join("\n");
  const issueUrl = gh(`issue create -R ${REPO} --title "Robinhood login: tap the link inside (20 min)" --body-file -`, body).trim();
  const issue = issueUrl.split("/").pop();
  console.log("login issue:", issueUrl);

  // 3) wait for the comment
  let code = null, commentId = null;
  const t0 = Date.now();
  while (!code && Date.now() - t0 < 20 * 60 * 1000) {
    await sleep(2000);
    const comments = JSON.parse(gh(`api repos/${REPO}/issues/${issue}/comments`));
    for (const c of comments) {
      const m = String(c.body).match(/https?:\/\/localhost:1455\/callback\?[^\s)>]+/);
      if (!m) continue;
      const u = new URL(m[0].replace(/&amp;/g, "&"));
      if (u.searchParams.get("state") !== state) { console.log("ignoring a link from an older login attempt"); continue; }
      if (u.searchParams.get("error")) throw new Error("Robinhood said: " + u.searchParams.get("error") + " " + (u.searchParams.get("error_description") || ""));
      // read the code straight from the address: URLSearchParams would turn a "+" in it into a space
      const raw = (m[0].replace(/&amp;/g, "&").match(/[?&]code=([^&#\s]+)/) || [])[1] || "";
      const codes = [...new Set([decodeURIComponent(raw), u.searchParams.get("code")].filter(Boolean))];
      code = codes;
      commentId = c.id;
      console.log("code characters:", [...new Set(raw.replace(/[A-Za-z0-9]/g, ""))].join("") || "letters/digits only", "| variants:", codes.length);
      console.log(`login link pasted ${Math.round((Date.now() - Date.parse(c.created_at)) / 1000)}s ago (comment), ${Math.round((Date.now() - t0) / 1000)}s after the issue opened; code length ${raw.length}`);
    }
  }
  if (!code) { closeWith(issue, "Timed out: run the Robinhood login workflow again."); throw new Error("no login link pasted within 20 minutes"); }

  // 4) code -> tokens (if Robinhood rejects the resource setting, the same code is tried once without it)
  let res, text;
  attempts: for (const cd of code) for (const [label, withResource, json] of [["form + resource", true, false], ["form", false, false], ["json + resource", true, true]]) {
    const form = { grant_type: "authorization_code", code: cd, redirect_uri: REDIRECT, client_id, code_verifier: verifier };
    if (withResource) form.resource = MCP_URL;
    res = await fetch(TOKEN_URL, { method: "POST", headers: { "Content-Type": json ? "application/json" : "application/x-www-form-urlencoded", Accept: "application/json" }, body: json ? JSON.stringify(form) : new URLSearchParams(form) });
    text = await res.text();
    console.log(`token exchange (${label}, code variant ${code.indexOf(cd) + 1}): HTTP ${res.status} ${res.ok ? "" : text.slice(0, 200)}`);
    if (res.ok) break attempts;
  }
  try { gh(`api -X DELETE repos/${REPO}/issues/comments/${commentId}`); } catch {}
  if (!res.ok) { closeWith(issue, `Login failed (HTTP ${res.status} ${text.slice(0, 120)}). Run the workflow again and paste the address as fast as you can: the code expires quickly.`); throw new Error(`token exchange failed: HTTP ${res.status} ${text.slice(0, 300)}`); }
  const j = JSON.parse(text);
  if (!j.refresh_token) console.log("WARNING: Robinhood returned no refresh token: the login will last only", j.expires_in, "seconds");
  saveTokens({ client_id, access_token: j.access_token, refresh_token: j.refresh_token, expires_at: Date.now() + (+j.expires_in || 3600) * 1000, saved_at: new Date().toISOString() });

  // 5) prove it works
  const br = new RobinhoodBroker({ log: (e, d) => console.log(e, JSON.stringify(d)) });
  const tools = await br.mcp.tools();
  const info = await br.setup();
  const bp = await br.optionsBuyingPower();
  const msg = `Robinhood login saved ✓\n\n- Tools available: ${tools.length}\n- Agent account: ••••${info.account.slice(-4)} (${info.type}, ${info.optionLevel})\n- Buying power: $${bp.toFixed(2)}\n- Access token lasts ${j.expires_in}s; refresh token: ${j.refresh_token ? "yes" : "NO"}`;
  console.log(msg);
  closeWith(issue, msg);
}

main().catch((e) => { console.error(e); process.exit(1); });
