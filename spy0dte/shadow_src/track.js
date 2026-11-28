// Forward tracker for the Aggressive rules and every variant the user is watching.
// Usage: node track.js <saved page file> <marks.json> [first forward day M/D, default 11/19]
// Scores ONLY days on/after the start day (days not used to pick the rules), plus all days for reference.
const fs=require('fs');const html=fs.readFileSync(process.argv[2],'utf8');
const s=[...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(x=>x[1]);let code=s[s.length-1];code=code.slice(0,code.indexOf('const css='));
global.document={getElementById:()=>({value:''})};
const ALL=JSON.parse(fs.readFileSync(process.argv[3]));
const {tradeReturn,entryOf,strikeOf}=new Function('Mdata',code.replace('let M=[];','let M=Mdata;')+';return {tradeReturn,entryOf,strikeOf:typeof strikeOf==="function"?strikeOf:null};')(ALL);
// in-the-money prices (itm.json next to marks.json) for option 2: strong trend = 1 in the money full port, weak = 3 in, half port
{const p=require('path').join(require('path').dirname(process.argv[3]),'itm.json');const X=fs.existsSync(p)?JSON.parse(fs.readFileSync(p)):{};for(const m of ALL)m.x=X[[m.d,m.t,m.k,m.src||'',m.s].join('|')]||null;const sp=require('path').join(require('path').dirname(process.argv[3]),'swing.json');if(fs.existsSync(sp)){const mo=m=>m.d.split('/').map(Number);ALL.push(...JSON.parse(fs.readFileSync(sp)));ALL.sort((a,b)=>{const x=mo(a),y=mo(b);return x[0]-y[0]||x[1]-y[1]||a.tod-b.tod})}}
const [sm,sd]=(process.argv[4]||'11/19').split('/').map(Number);const md=d=>d.split('/').map(Number);
const FWD=ALL.filter(m=>{const [a,b]=md(m.d);return a>sm||(a===sm&&b>=sd)});
const lastDay=ALL.length?ALL[ALL.length-1].d:null;const TODAY=ALL.filter(m=>m.d===lastDay);
const G=m=>(m.k==='S'?'Swing break':m.k==='A'?'Arrow':m.k==='D'?'White dot':m.src==='SPY'?'SPY pane':m.src==='call'?'Call-chart pane':'Put-chart pane')+' '+(m.s==='C'?'calls':'puts');
const F={swing:m=>{const r=m.x&&m.x.rv;return m.k==='S'&&m.tod>=150&&!!r&&r.run15>=1&&r.run15<3.5},fadeA:m=>{const r=m.x&&m.x.rv;return F.rev(m)&&r.vk>=90&&r.so!=null&&r.so<=20&&r.cF>=90&&r.cG<=20&&r.dm>=0.3},fadeB:m=>{const r=m.x&&m.x.rv;return F.rev(m)&&r.vk>=80&&r.dm!=null&&r.dm<0.3&&r.bar15>=0.6},revvf:m=>{const r=m.x&&m.x.rv;return m.tw!==1&&!!r&&r.mv15<=-1.5&&r.ne5===0&&r.st<0.8&&r.vk>=80},rev:m=>{const r=m.x&&m.x.rv;return m.tw!==1&&!!r&&r.mv15<=-1.5&&r.ne5===0&&r.st<0.8},twok:m=>m.tw===1&&m.ag!==undefined&&m.ag!==-1,tw:m=>m.tw===1,agok:m=>m.ag!==undefined&&m.ag!==-1,any:m=>true};
const base={hold:120,slip:.01,entry:.05,sl:.75,tp:.1,style:'half',be:true,run:'15',cut5:false,xr:true};
const R=(o={},f='twok',cut=210)=>({f,cut,P:{...base,...o}});
// each trigger's best exits on Nov 3-18 (same filter for all; arrows off)
const BEST={'Call-chart pane calls':R({style:'all',tp:.1,entry:.08}),'Put-chart pane puts':R({tp:.2}),'SPY pane calls':R({}),'SPY pane puts':R({style:'all',tp:.2,entry:.03}),
 'White dot calls':R({tp:.2,sl:.5,entry:.08}),'White dot puts':R({style:'all',tp:.2,sl:.5})};
function run(ruleOf,marks,start=1000,strike){let eq=start,pk=eq,mdd=0,busy={d:null,u:-1},day=null,ds=eq,dpk=0,locked=false;const log=[];
 for(const m0 of marks){if(m0.d!==day){day=m0.d;ds=eq;dpk=0;locked=false}if(locked)continue;
  const g=G(m0);const r=ruleOf(g,m0);if(!r||!F[r.f](m0)||m0.tod>=r.cut)continue;if(m0.d===busy.d&&m0.tod<busy.u)continue;
  const sv=(r.strike||strike)&&strikeOf?strikeOf(m0,{strike:r.strike||strike}):{m:m0,size:1};const m=entryOf(sv.m,r.P);if(!m)continue;if(m.d===busy.d&&m.tod<busy.u)continue;const price=m.e+r.P.slip,q=Math.floor(eq*sv.size/(price*100));if(q<1)continue;
  const t=tradeReturn(m,r.P);const ex=Math.max(0,m.e*(1+t.r)-r.P.slip);const ret=ex/price-1;eq+=q*100*(ex-price);
  log.push({d:m.d,t:m0.t,g,ret});busy={d:m.d,u:m.tod+t.n+1};pk=Math.max(pk,eq);mdd=Math.max(mdd,(pk-eq)/pk);
  const gd=eq/ds-1;dpk=Math.max(dpk,gd);if(dpk>=.25&&gd<=dpk*2/3)locked=true; if(gd<=-.30)locked=true}
 return{eq,mdd,n:log.length,wins:log.filter(x=>x.ret>0).length,stops:log.filter(x=>x.ret<=-.7).length,worst:log.length?Math.min(...log.map(x=>x.ret)):0,log}}
const noA=f=>g=>(g.startsWith('Arrow')||g.startsWith('Swing'))?null:f(g);
const ACCTS=[['Public Swing Break (fear/greed break together after a flush, 12:00-3:00, run $1-3.50, 1 ITM, ratchet from +10%, -50% stop)',g=>g.startsWith('Swing')?R({tp:.1,sl:.5,style:'ratchet',be:false,xr:false},'swing',330):null,'i1'],['Option 2 (the bot: in the money by trend)',noA(g=>R()),'trend'],['Aggressive (old bot, first-out strike)',noA(g=>R())],['Public Vix Fix reversal (the reversal + fear/greed 80+ in 10 min; runs on Public)',g=>/pane/.test(g)?R({tp:.2},'revvf'):null,'i1'],['Public Fade MAIN (matching charts + day backs it; reversal, whole ratchet)',g=>/pane/.test(g)?R({tp:.2,style:'ratchet',be:false},'fadeA',255):null,'i1'],['Public Fade with the run (day not backing it, fast market; buys the other side)',g=>/pane/.test(g)?R({tp:.2,style:'ratchet',be:false},'fadeB',255):null,'opp1'],['Public Fade both (main + with the run, one account)',(g,m)=>{if(!/pane/.test(g))return null;if(F.fadeA(m))return R({tp:.2,style:'ratchet',be:false},'fadeA',255);if(F.fadeB(m))return{...R({tp:.2,style:'ratchet',be:false},'fadeB',255),strike:'opp1'};return null},'i1'],['Public Fade: whole ratchet (Vix Fix reversal to 1:45; at +20% stop to +15%, then up 5% behind each 5% high; out at 30 min if no +20%)',g=>/pane/.test(g)?R({tp:.2,style:'ratchet',be:false},'revvf',255):null,'i1'],['Public Fade: half +20%, half ratchet (same, half sold at +20%)',g=>/pane/.test(g)?R({tp:.2,style:'hratchet',be:false},'revvf',255):null,'i1'],['Public reversal (ran hard, stalled, shrinking; 1 in the money, half at +20%)',g=>/pane/.test(g)?R({tp:.2},'rev'):null,'i1'],['Puts half at +20%, calls as bot',noA(g=>g.endsWith('puts')?R({tp:.2}):R())],
 ['Each trigger its own exits',noA(g=>BEST[g]||R())],['Smart trail',noA(g=>R({style:'smart'}))],['Aggressive WITH arrows',g=>R()]];
const fmt=r=>`$${Math.round(r.eq).toLocaleString()} · ${r.n} trades · ${r.wins} won · ${r.stops} hit -75% · worst trade ${(r.worst*100).toFixed(0)}% · worst drop ${Math.round(r.mdd*100)}%`;
console.log(`FORWARD DAYS (${[...new Set(FWD.map(m=>m.d))].join(', ')||'none yet'}) — $1,000 start, full port, day lock on`);
for(const [n,f,k] of ACCTS)console.log(`  ${n}: ${fmt(run(f,FWD,1000,k))}`);
console.log(`\nTODAY (${lastDay}) — $1,000 start`);
for(const [n,f,k] of ACCTS.slice(0,13)){const r=run(f,TODAY,1000,k);console.log(`  ${n}: $${Math.round(r.eq)} | `+(r.log.map(x=>`${x.t} ${x.g} ${(x.ret*100).toFixed(1)}%`).join(', ')||'no trade'))}
const tr=(m,P)=>{const x=entryOf(m,P);if(!x)return null;const t=tradeReturn(x,P);const pr=x.e+P.slip;return Math.max(0,x.e*(1+t.r)-P.slip)/pr-1};
const st=(L,P)=>{const Rr=L.map(m=>tr(m,P)).filter(x=>x!=null);if(!Rr.length)return 'none';return `n${Rr.length} avg ${(Rr.reduce((a,b)=>a+b,0)/Rr.length*100).toFixed(1)}% won ${Math.round(Rr.filter(x=>x>0).length/Rr.length*100)}% worst ${(Math.min(...Rr)*100).toFixed(0)}%`};
console.log('\nEACH TRIGGER on forward days (filtered: trend+shading, before 1) — current exits | half +20% | all out +10% | all out +20%');
for(const g of ['White dot calls','White dot puts','SPY pane calls','SPY pane puts','Call-chart pane calls','Put-chart pane puts','Arrow calls','Arrow puts']){const L=FWD.filter(m=>G(m)===g&&F.twok(m)&&m.tod<210);
 console.log(`  ${g}: ${st(L,base)} | ${st(L,{...base,tp:.2})} | ${st(L,{...base,style:'all'})} | ${st(L,{...base,style:'all',tp:.2})}`)}
console.log('\nVARIABLES on forward days (bot rules, change one thing) — $1,000 account');
const V=[['cutoff 11:00',R({},'twok',90)],['cutoff 12:00',R({},'twok',150)],['cutoff 1:00 (bot)',R()],['cutoff 2:00',R({},'twok',270)],['cutoff 3:00',R({},'twok',330)],
 ['stop -50%',R({sl:.5})],['stop -75% (bot)',R()],['no stop',R({sl:null})],['bid 3%',R({entry:.03})],['bid 5% (bot)',R()],['bid 8%',R({entry:.08})],['market (no bid)',R({entry:0})],
 ['half +10% (bot)',R()],['half +15%',R({tp:.15})],['half +20%',R({tp:.2})],['all out +10%',R({style:'all'})],['runner on trend line',R({run:'tl'})],['x exit off',R({xr:false})],
 ['filter: trend only',R({},'tw')],['filter: none',R({},'any')]];
for(const [n,r] of V){const x=run(noA(()=>r),FWD);console.log(`  ${n}: $${Math.round(x.eq).toLocaleString()} · ${x.n} trades · ${x.stops} at -75% · worst drop ${Math.round(x.mdd*100)}%`)}
console.log('\nALL DAYS for reference — $1,000 start');for(const [n,f,k] of ACCTS.slice(0,12))console.log(`  ${n}: ${fmt(run(f,ALL,1000,k))}`);
