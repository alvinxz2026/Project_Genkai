"""Generate tools/gs1_codex.html — the unified GS1 "Adept's Codex" app.

Supersedes the three standalone tools (class/equipment explorers + build planner)
with ONE self-contained static page that embeds the source-of-truth JSON inline
(works over file:// with no fetch/CORS). This script is the build step; the page
is a pure read view. Rerun after any data change:

    python scripts/build_codex.py

Two tabs:
  * Wiki (B') — graph-aware browser over all 11 entities + location_refs.json:
    search/filter, master-detail, and every cross-entity FK rendered as a
    clickable chip (both directions) so you can walk the connected graph. The
    location hub reads location_refs.json directly.
  * Planner (A) — the djinn-distribution -> class/stat/psynergy calculator
    (ported from build_planner.py); class & psynergy names link into the Wiki.

E (graph visualization) is intentionally deferred; the reverse-index layer built
here is its data foundation.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "gs1"
OUT = ROOT / "tools" / "gs1_codex.html"

ENTITIES = ["djinn", "summons", "classes", "psynergy", "equipment", "items",
            "shops", "monsters", "bosses", "locations", "characters"]


def load(name):
    return json.loads((DATA / f"{name}.json").read_text(encoding="utf-8"))


def embed(data):
    return (json.dumps(data, separators=(",", ":"), ensure_ascii=False)
            .replace("</", "<\\/"))


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Adept's Codex — Golden Sun</title>
<style>
  :root {
    --bg:#f1ead8; --bg-deep:#e4dac0; --panel:#faf6eb; --panel-2:#f1ebda;
    --panel-3:#e9e1ca; --line:#cfc4a4; --line-soft:#ddd3b6;
    --gold:#b08c2e; --gold-bright:#7a5d10; --gold-dim:#a98f4d;
    --text:#2c2618; --text-dim:#5f5740; --text-faint:#8d8468;
    --earth:#8f6a0e; --fire:#b8431d; --wind:#6f37b5; --water:#1d6cb0;
    --neutral:#6e7384; --good:#2c8a52; --bad:#b13d3d; --radius:10px;
    --font-display:Palatino,"Palatino Linotype","Book Antiqua",Georgia,serif;
    --font-body:"Segoe UI",system-ui,-apple-system,sans-serif;
  }
  * { box-sizing:border-box; margin:0; padding:0; }
  body { background:var(--bg);
    background-image:radial-gradient(ellipse 80% 50% at 50% -10%, rgba(176,140,46,.10), transparent),
                     radial-gradient(ellipse 50% 40% at 10% 90%, rgba(143,106,14,.06), transparent);
    background-attachment:fixed; color:var(--text); font-family:var(--font-body); font-size:14px; min-height:100vh; }
  header { text-align:center; padding:26px 20px 4px; }
  header h1 { font-family:var(--font-display); font-size:32px; font-weight:400; letter-spacing:5px;
    text-transform:uppercase; color:var(--gold-bright); text-shadow:0 1px 0 rgba(255,255,255,.7), 0 0 24px rgba(176,140,46,.25); }
  header .subtitle { color:var(--text-dim); font-size:12px; letter-spacing:2.5px; text-transform:uppercase; margin-top:6px; }

  nav { display:flex; justify-content:center; gap:6px; padding:16px 20px 0; flex-wrap:wrap; }
  nav button { font-family:var(--font-display); font-size:14px; letter-spacing:2px; text-transform:uppercase;
    background:transparent; color:var(--text-dim); border:1px solid transparent; border-bottom:none;
    padding:9px 28px; cursor:pointer; border-radius:var(--radius) var(--radius) 0 0; transition:color .15s, background .15s; }
  nav button:hover { color:var(--gold-bright); }
  nav button.active { color:var(--gold-bright); background:var(--panel); border-color:var(--line); box-shadow:0 -4px 16px rgba(80,64,24,.08); }

  main { max-width:1500px; margin:0 auto 60px; border-top:1px solid var(--line); min-height:72vh; padding:18px; }
  .tabpane { display:none; } .tabpane.active { display:block; }

  .el-dot { display:inline-block; width:9px; height:9px; border-radius:50%; margin-right:4px; vertical-align:1px; }
  .el-earth{background:var(--earth)} .el-fire{background:var(--fire)} .el-wind{background:var(--wind)} .el-water{background:var(--water)} .el-none{background:var(--neutral)}
  .tx-earth{color:var(--earth)} .tx-fire{color:var(--fire)} .tx-wind{color:var(--wind)} .tx-water{color:var(--water)}

  .badge { display:inline-block; font-size:10px; letter-spacing:1px; text-transform:uppercase; border:1px solid var(--line);
    border-radius:5px; padding:1px 7px; color:var(--text-dim); background:var(--panel-2); }
  .badge.t-djinn{color:#6b4f12;border-color:#c8a85a} .badge.t-summons{color:#8a5a12} .badge.t-classes{color:#7a5d10}
  .badge.t-psynergy{color:#6f37b5;border-color:#b89ad6} .badge.t-equipment{color:#b8431d;border-color:#d6a08f}
  .badge.t-items{color:#2c8a52;border-color:#9ad4b2} .badge.t-shops{color:#1d6cb0;border-color:#9ec6e2}
  .badge.t-monsters{color:#7a3030;border-color:#c89a9a} .badge.t-bosses{color:#a01818;border-color:#d49a94}
  .badge.t-locations{color:#5f5740;border-color:var(--gold-dim)} .badge.t-characters{color:#1d6cb0}

  /* ---- wiki layout ---- */
  .toolbar { display:flex; gap:12px; flex-wrap:wrap; align-items:center; background:var(--panel); border:1px solid var(--line);
    border-radius:var(--radius); padding:10px 14px; margin-bottom:14px; }
  .toolbar input[type=text] { background:#fffdf6; border:1px solid var(--line); color:var(--text); border-radius:6px;
    padding:7px 10px; font-size:13px; outline:none; font-family:var(--font-body); width:240px; }
  .toolbar input[type=text]:focus { border-color:var(--gold-dim); }
  .chipbar { display:flex; gap:5px; flex-wrap:wrap; }
  .fchip { background:var(--panel-2); border:1px solid var(--line-soft); color:var(--text-dim); border-radius:13px;
    padding:3px 11px; font-size:12px; cursor:pointer; user-select:none; transition:all .12s; }
  .fchip:hover { color:var(--text); border-color:var(--gold-dim); }
  .fchip.on { background:var(--gold); color:#fdfbf4; border-color:var(--gold); font-weight:600; }
  .wiki-layout { display:grid; grid-template-columns:minmax(0,1fr) 560px; gap:16px; align-items:start; }
  @media (max-width:1150px){ .wiki-layout{ grid-template-columns:1fr; } }

  .list { background:var(--panel); border:1px solid var(--line); border-radius:var(--radius); padding:6px; max-height:calc(100vh - 60px); overflow-y:auto; }
  .lrow { display:flex; align-items:center; gap:8px; padding:6px 9px; border-radius:7px; cursor:pointer; }
  .lrow:hover { background:var(--panel-3); }
  .lrow.sel { background:var(--panel-3); box-shadow:inset 3px 0 0 var(--gold); }
  .lrow .lname { color:var(--text); font-size:13px; }
  .lrow .lmeta { margin-left:auto; }
  .listcount { color:var(--text-faint); font-size:11px; letter-spacing:1px; padding:6px 9px; }

  .detail { position:sticky; top:12px; background:var(--panel); border:1px solid var(--line); border-radius:var(--radius);
    padding:16px 18px; max-height:calc(100vh - 24px); overflow-y:auto; }
  .detail .placeholder { color:var(--text-faint); text-align:center; padding:70px 10px; font-style:italic; }
  .detail h2 { font-family:var(--font-display); font-size:23px; letter-spacing:1px; color:var(--gold-bright); font-weight:400; }
  .detail .subline { margin-top:4px; }
  .sect { margin-top:16px; }
  .sect h3 { font-size:10.5px; letter-spacing:2.5px; text-transform:uppercase; color:var(--gold-dim);
    border-bottom:1px solid var(--line-soft); padding-bottom:4px; margin-bottom:8px; }
  .kv { display:grid; grid-template-columns:130px 1fr; gap:3px 10px; font-size:13px; }
  .kv .k { color:var(--text-faint); }
  .kv .v { color:var(--text-dim); }
  .prose { font-size:12.5px; color:var(--text-dim); line-height:1.55; }
  .reflist { display:flex; gap:6px; flex-wrap:wrap; }
  .ref { display:inline-flex; align-items:center; gap:4px; background:var(--panel-2); border:1px solid var(--line-soft);
    border-radius:13px; padding:3px 10px; font-size:12.5px; color:var(--text); cursor:pointer; transition:all .12s; }
  .ref:hover { border-color:var(--gold); background:var(--panel-3); }
  .ref .rt { font-size:9px; letter-spacing:.5px; text-transform:uppercase; color:var(--text-faint); }
  .linkgroup { margin-bottom:10px; }
  .linkgroup .glabel { font-size:11.5px; color:var(--text-dim); margin-bottom:5px; }
  .linkgroup .glabel b { color:var(--gold-bright); font-weight:600; }

  .statgrid { display:grid; grid-template-columns:40px 1fr 46px; gap:4px 8px; align-items:center; }
  .statgrid .sn { color:var(--text-dim); font-size:10.5px; letter-spacing:1px; text-transform:uppercase; }
  .statgrid .sv { font-size:12px; text-align:right; font-variant-numeric:tabular-nums; }
  .barwrap { background:var(--bg-deep); border-radius:4px; height:11px; position:relative; overflow:hidden; }
  .barwrap .bar { height:100%; border-radius:4px; background:linear-gradient(90deg,#d6bd7e,var(--gold)); }
  .barwrap .bar.low{ background:linear-gradient(90deg,#d49a94,var(--bad)); } .barwrap .bar.high{ background:linear-gradient(90deg,#9ad4b2,var(--good)); }
  .barwrap .base { position:absolute; top:0; bottom:0; width:1px; background:rgba(44,38,24,.4); }

  /* ---- planner ---- */
  .infobox { background:linear-gradient(180deg,var(--panel-2),var(--panel)); border:1px solid var(--line); border-left:3px solid var(--gold-dim);
    border-radius:var(--radius); padding:12px 16px; margin-bottom:18px; color:var(--text-dim); font-size:13px; line-height:1.55; }
  .infobox b { color:var(--gold-bright); } .infobox code { color:var(--text); background:var(--bg-deep); padding:1px 6px; border-radius:4px; font-size:12px; }
  .pgrid { display:grid; grid-template-columns:repeat(4,1fr); gap:16px; align-items:start; }
  @media (max-width:1200px){ .pgrid{ grid-template-columns:repeat(2,1fr);} } @media (max-width:640px){ .pgrid{ grid-template-columns:1fr;} }
  .charcard { background:var(--panel); border:1px solid var(--line); border-radius:var(--radius); padding:14px 15px; border-top:3px solid var(--neutral); }
  .charcard h2 { font-family:var(--font-display); font-size:21px; font-weight:400; letter-spacing:1.5px; color:var(--gold-bright); display:flex; align-items:center; gap:8px; }
  .charcard .nativetag { color:var(--text-faint); font-size:11px; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:12px; }
  .stepper { display:flex; align-items:center; justify-content:space-between; padding:5px 0; border-bottom:1px solid var(--line-soft); }
  .stepper .lbl { display:flex; align-items:center; gap:7px; font-size:13px; color:var(--text-dim); }
  .stepper .lbl.native .nm { font-weight:700; color:var(--text); }
  .stepper .ctrls { display:flex; align-items:center; gap:8px; }
  .stepper button { width:24px; height:24px; border-radius:6px; border:1px solid var(--line); background:var(--panel-2); color:var(--gold-bright); font-size:15px; line-height:1; cursor:pointer; font-family:var(--font-body); }
  .stepper button:hover:not(:disabled){ border-color:var(--gold-dim); background:var(--panel-3); } .stepper button:disabled{ opacity:.35; cursor:default; }
  .stepper .val { min-width:18px; text-align:center; font-variant-numeric:tabular-nums; font-size:15px; color:var(--text); }
  .totalrow { display:flex; justify-content:space-between; align-items:center; margin-top:8px; font-size:12px; color:var(--text-faint); }
  .totalrow .over { color:var(--bad); font-weight:700; } .totalrow .reset { cursor:pointer; color:var(--gold-dim); text-decoration:underline; }
  .reverse { margin-top:10px; } .reverse select { width:100%; background:#fffdf6; border:1px solid var(--line); color:var(--text); border-radius:6px; padding:6px 8px; font-size:12.5px; font-family:var(--font-body); }
  .result { margin-top:14px; padding-top:12px; border-top:1px solid var(--line); }
  .result .classname { font-family:var(--font-display); font-size:20px; letter-spacing:1px; color:var(--gold-bright); cursor:pointer; }
  .result .classname:hover { text-decoration:underline; }
  .result .meta { font-size:11.5px; color:var(--text-faint); letter-spacing:1px; text-transform:uppercase; margin-top:2px; }
  .result .none { color:var(--bad); font-style:italic; font-size:13px; }
  .result .multi { color:var(--text-dim); font-size:12px; margin-top:6px; } .result .multi .alt { cursor:pointer; text-decoration:underline dotted; }
  .psy { margin-top:12px; } .psy h3 { font-size:10.5px; letter-spacing:2px; text-transform:uppercase; color:var(--gold-dim); border-bottom:1px solid var(--line-soft); padding-bottom:4px; margin-bottom:6px; }
  .psy ul { list-style:none; max-height:230px; overflow-y:auto; } .psy li { display:flex; align-items:center; gap:7px; padding:2.5px 0; font-size:12.5px; color:var(--text-dim); cursor:pointer; }
  .psy li:hover .pn { text-decoration:underline; } .psy li .pn { color:var(--text); } .psy li .pp { margin-left:auto; color:var(--text-faint); font-size:11px; }
  .psy .empty { color:var(--text-faint); font-style:italic; font-size:12px; }
  footer { text-align:center; color:var(--text-faint); font-size:11px; letter-spacing:1px; padding:10px; }
</style>
</head>
<body>
<header>
  <h1>Adept's Codex</h1>
  <div class="subtitle">Golden Sun &middot; Knowledge Graph</div>
</header>
<nav>
  <button id="navbtn-wiki" class="active" data-tab="wiki">Wiki</button>
  <button id="navbtn-planner" data-tab="planner">Build Planner</button>
</nav>
<main>
  <div class="tabpane active" id="tab-wiki">
    <div class="toolbar">
      <input type="text" id="search" placeholder="Search any entity&hellip;" autocomplete="off">
      <div class="chipbar" id="typechips"></div>
    </div>
    <div class="wiki-layout">
      <div>
        <div class="listcount" id="listcount"></div>
        <div class="list" id="list"></div>
      </div>
      <div class="detail" id="detail"><div class="placeholder">Pick an entity, or click any linked chip to walk the graph.</div></div>
    </div>
  </div>
  <div class="tabpane" id="tab-planner">
    <div class="infobox">
      Set the Djinn each adept has <b>Set</b> (by element) to resolve their <b>current class</b>,
      <b>stat multipliers</b>, and <b>Psynergy</b>. Or pick a target class to see the Djinn it needs.
      Rules follow <code>plz2bstfu-class</code>; GS1 caps each adept at <b>7</b> Set Djinn.
      Class &amp; Psynergy names link into the Wiki.
    </div>
    <div class="pgrid" id="pgrid"></div>
  </div>
</main>
<footer>Pure read view over <code>data/gs1/</code> &middot; rebuild: <code>python scripts/build_codex.py</code></footer>

<script type="application/json" id="data-db">__DB__</script>
<script type="application/json" id="data-lr">__LR__</script>
<script>
"use strict";
const DB = JSON.parse(document.getElementById("data-db").textContent);
const LR = JSON.parse(document.getElementById("data-lr").textContent);
const TYPES = ["djinn","summons","classes","psynergy","equipment","items","shops","monsters","bosses","locations","characters"];
const ELEMS = ["earth","fire","wind","water"];
const EL_DJINN = { earth:"Venus", fire:"Mars", wind:"Jupiter", water:"Mercury" };
const TYPE_LABEL = { djinn:"Djinni", summons:"Summon", classes:"Class", psynergy:"Psynergy", equipment:"Equipment",
  items:"Item", shops:"Shop", monsters:"Monster", bosses:"Boss", locations:"Location", characters:"Character" };

function esc(s){ return String(s==null?"":s).replace(/[&<>]/g, m=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[m])); }
function elDot(el){ return `<span class="el-dot el-${el||"none"}"></span>`; }

/* ---------------- indexes ---------------- */
const byId = {}; TYPES.forEach(t => { byId[t]={}; (DB[t]||[]).forEach(o => byId[t][o.id]=o); });
const charByName = {}; (DB.characters||[]).forEach(c => charByName[c.name]=c);
function charRef(name){ const c=charByName[name]; return c ? {type:"characters", id:c.id} : null; }

// reverse indices over every FK edge
const rev = {
  psyToClasses:{}, charToClasses:{}, gearToShops:{}, gearToMonsters:{},
  djinnToMonster:{}, itemToPsy:{}, charToEquip:{}, charToPsy:{}, locOf:{}
};
function push(map,k,v){ (map[k]=map[k]||[]).push(v); }

(DB.classes||[]).forEach(c => {
  (c.psynergy||[]).forEach(p => { if(p.id) push(rev.psyToClasses, p.id, c.id); });
  (c.available_to||[]).forEach(a => { if(a.character_id) push(rev.charToClasses, a.character_id, c.id); });
});
(DB.shops||[]).forEach(s => (s.stock||[]).forEach(st => { if(st.ref_id) push(rev.gearToShops, st.ref_type+":"+st.ref_id, s.id); }));
(DB.monsters||[]).forEach(m => {
  ((m.drops||{}).items||[]).forEach(d => { if(d.ref_id) push(rev.gearToMonsters, d.ref_type+":"+d.ref_id, m.id); });
  if(m.djinn_id) push(rev.djinnToMonster, m.djinn_id, m.id);
});
(DB.psynergy||[]).forEach(p => { const a=p.acquired_via_item; if(a && a.item_id) push(rev.itemToPsy, a.item_id, p.id); });
(DB.equipment||[]).forEach(e => (e.equippable_by||[]).forEach(n => { const c=charByName[n]; if(c) push(rev.charToEquip, c.id, e.id); }));
(DB.psynergy||[]).forEach(p => (p.available_to||[]).forEach(n => { const c=charByName[n]; if(c) push(rev.charToPsy, c.id, p.id); }));
// invert location_refs: "<cat>:<id>" -> [locId]
const LR_CATS = { djinn:"djinn", equipment:"equipment", monsters:"monsters", bosses:"bosses", shops:"shops", items:"items" };
Object.keys(LR.locations||{}).forEach(lid => {
  const rec = LR.locations[lid];
  Object.keys(LR_CATS).forEach(cat => (rec[cat]||[]).forEach(eid => push(rev.locOf, cat+":"+eid, lid)));
});
function uniq(a){ return [...new Set(a)]; }
function djinnByElement(el){ return (DB.djinn||[]).filter(d=>d.element===el).map(d=>d.id); }
function summonsByElement(el){ return (DB.summons||[]).filter(s=>s.element===el).map(s=>s.id); }

/* ---------------- shared rendering ---------------- */
function entEl(type,o){ // element accent for an entity if it has one
  if(["djinn","summons","psynergy","characters"].includes(type)) return o.element||null;
  return null;
}
function nameOf(type,id){ const o=byId[type]&&byId[type][id]; return o ? (o.qualified_name||o.name) : id; }
function refChip(type,id){
  if(!byId[type]||!byId[type][id]) return "";
  const o=byId[type][id]; const el=entEl(type,o);
  return `<span class="ref" data-type="${type}" data-id="${id}">${el?elDot(el):""}${esc(o.qualified_name||o.name)}<span class="rt">${TYPE_LABEL[type]}</span></span>`;
}
function refsFromList(type, ids){ ids=uniq(ids); if(!ids.length) return ""; return `<div class="reflist">${ids.map(id=>refChip(type,id)).join("")}</div>`; }
function linkGroup(label, html){ if(!html) return ""; return `<div class="linkgroup"><div class="glabel"><b>${label}</b></div>${html}</div>`; }

function statBars(obj, keys, scaleMax, baselinePct){
  let h='<div class="statgrid">';
  for(const [k,lbl] of keys){
    const v=obj[k]; if(v==null) continue;
    const pct=Math.max(0,Math.min(100,(v/scaleMax)*100));
    const cls = baselinePct!=null ? (v>100?"high":(v<100?"low":"")) : "";
    h+=`<div class="sn">${lbl}</div><div class="barwrap"><div class="bar ${cls}" style="width:${pct}%"></div>`
      +(baselinePct!=null?`<div class="base" style="left:${baselinePct}%"></div>`:"")+`</div>`
      +`<div class="sv">${v}${baselinePct!=null?"%":""}</div>`;
  }
  return h+"</div>";
}
function kv(rows){ return `<div class="kv">${rows.filter(r=>r[1]!=null&&r[1]!=="").map(r=>`<div class="k">${r[0]}</div><div class="v">${r[1]}</div>`).join("")}</div>`; }

/* ---------------- per-type core fields + links ---------------- */
function coreHTML(type,o){
  switch(type){
    case "djinn": return kv([["Element",`${elDot(o.element)}<span class="tx-${o.element}">${EL_DJINN[o.element]}</span>`],
      ["Unleash",o.battle_effect&&(o.battle_effect.damage||o.battle_effect.special)?esc((o.battle_effect.damage||"")+" "+(o.battle_effect.special||"")):"effect only"],
      ["Must fight",o.must_fight?"yes":"no"],["Found",esc((o.location||{}).area)]])
      + (o.location&&o.location.description?`<div class="prose" style="margin-top:8px">${esc(o.location.description)}</div>`:"");
    case "summons": return kv([["Element",`${elDot(o.element)}<span class="tx-${o.element}">${EL_DJINN[o.element]}</span>`],
      ["Djinn needed",o.djinn_required],["Base power",o.damage_power],["+ Max HP",o.damage_hp_mod!=null?(o.damage_hp_mod*100)+"% of target":null],["Effect",esc(o.effect)]]);
    case "classes": { let h=kv([["Class line",esc(o.class_line)],["Reachable (GS1)",o.reachable_in_gs1?"yes":"no — needs 8 djinn"]]);
      if(o.stat_multiplier) h+=`<div class="sect"><h3>Stat Multipliers</h3>${statBars(o.stat_multiplier,[["hp","HP"],["pp","PP"],["atk","ATK"],["def","DEF"],["agi","AGI"],["lck","LCK"]],200,50)}</div>`;
      const reqs=(o.available_to||[]).map(a=>`<div><b>${esc(a.character)}</b>: ${esc((a.djinn_requirements||[]).map(r=>r.requirement).join(" / "))||"—"}</div>`).join("");
      if(reqs) h+=`<div class="sect"><h3>Djinn Setup</h3><div class="prose">${reqs}</div></div>`;
      return h; }
    case "psynergy": return kv([["Element",`${elDot(o.element)}<span class="tx-${o.element}">${o.element}</span>`],["Category",esc(o.category)],
      ["PP cost",o.pp_cost],["Range",esc(o.range)],["Target",esc(o.target)],["Tier / series",`${o.tier!=null?o.tier:"?"}${o.series?" · "+esc(o.series):""}`],
      ["Learned at",esc(o.level_learned_variants||o.level_learned)]]) + (o.description?`<div class="prose" style="margin-top:8px">${esc(o.description)}</div>`:"");
    case "equipment": { const flags=[o.is_artifact?"artifact":"",o.is_cursed?"cursed":"",o.increases_critical?"crit+":""].filter(Boolean).join(", ");
      let h=kv([["Type",`${esc(o.category)} · ${esc(o.type)}`],["Flags",esc(flags)||"none"],["Acquisition",o.acquisition?esc(`${o.acquisition.method}${o.acquisition.location?" — "+o.acquisition.location:""}${o.acquisition.price!=null?" ("+o.acquisition.price+"c)":""}`):null]]);
      if(o.stat_bonus) h+=`<div class="sect"><h3>Stat Bonus</h3>${statBars(o.stat_bonus,[["atk","ATK"],["def","DEF"],["hp","HP"],["pp","PP"],["agi","AGI"],["lck","LCK"]],150)}</div>`;
      if(o.unleash) h+=`<div class="sect"><h3>Unleash</h3><div class="prose">${elDot(o.unleash.element)}<b>${esc(o.unleash.name)}</b> — ${esc(o.unleash.rate)} rate, ${esc(o.unleash.power_level)} power${o.unleash.effects&&o.unleash.effects.length?"; "+esc(o.unleash.effects.join(", ")):""}</div></div>`;
      if(o.use_effect) h+=`<div class="sect"><h3>Use</h3><div class="prose">${esc(o.use_effect.description)}${o.use_effect.may_break?" (may break)":""}</div></div>`;
      return h; }
    case "items": return kv([["Type",esc(o.item_type)],["Effect",esc(o.effect)],["Usable in battle",o.usable_in_battle?"yes":"no"],
      ["Buy / Sell",`${o.buy_price!=null?o.buy_price:"—"} / ${o.sell_price!=null?o.sell_price:"—"}`]]);
    case "shops": return kv([["Town",esc(o.name)],["Availability",esc(o.availability_notes)||"always open"],["Stock size",(o.stock||[]).length]]);
    case "monsters": { let h=kv([["Variant",esc(o.variant)],["Djinn enemy",o.is_djinn_enemy?"yes":"no"]]);
      if(o.stats) h+=`<div class="sect"><h3>Stats</h3>${statBars(o.stats,[["hp","HP"],["pp","PP"],["atk","ATK"],["def","DEF"],["agi","AGI"],["lck","LCK"]],Math.max(100,(o.stats.hp||100)))}</div>`;
      const ab=(o.abilities||[]).map(a=>esc(a.name||a)).join(", "); if(ab) h+=`<div class="sect"><h3>Abilities</h3><div class="prose">${ab}</div></div>`;
      const dr=(o.drops||{}); h+=`<div class="prose" style="margin-top:8px">EXP ${dr.exp!=null?dr.exp:"?"} · ${dr.coins!=null?dr.coins:"?"} coins</div>`;
      return h; }
    case "bosses": { let h=kv([["Optional",o.is_optional?"yes":"no"],["Superboss",o.is_superboss?"yes":"no"],
      ["Weakness",(o.weakness||[]).map(w=>`${elDot(w)}${w}`).join(" ")||"none"],["Rec. level",o.recommended_level]]);
      const enc=(o.encounters||[]).map(e=>{ const s=e.stats||{}; return `<div><b>${esc(e.location)}</b> — HP ${s.hp!=null?s.hp:"?"}, ATK ${s.atk!=null?s.atk:"?"}, DEF ${s.def!=null?s.def:"?"}${e.is_winnable===false?" (scripted loss)":""}</div>`; }).join("");
      if(enc) h+=`<div class="sect"><h3>Encounters</h3><div class="prose">${enc}</div></div>`;
      if(o.strategy) h+=`<div class="sect"><h3>Strategy</h3><div class="prose">${esc(o.strategy)}</div></div>`;
      return h; }
    case "locations": return kv([["Type",esc(o.type)],["Region",esc(o.region)],["Chapter",esc(o.chapter_first_seen)],["Has map",o.has_map?"yes":"no"],["Aliases",esc((o.aliases||[]).join(", "))]])
      + (o.summary?`<div class="prose" style="margin-top:8px">${esc(o.summary)}</div>`:"");
    case "characters": return kv([["Element",`${elDot(o.element)}<span class="tx-${o.element}">${EL_DJINN[o.element]}</span>`],["Permanent",o.is_permanent?"yes":"no (prologue only)"]])
      + (o.notes?`<div class="prose" style="margin-top:8px">${esc(o.notes)}</div>`:"");
  }
  return "";
}

function linksHTML(type,o){
  const g=[];
  const locs = rev.locOf[type+":"+o.id]||[];
  switch(type){
    case "djinn":
      g.push(linkGroup("Monster form", refsFromList("monsters", rev.djinnToMonster[o.id]||[])));
      g.push(linkGroup("Found at", refsFromList("locations", locs)));
      g.push(linkGroup("Fuels summons (same element)", refsFromList("summons", summonsByElement(o.element))));
      break;
    case "summons":
      g.push(linkGroup("Powered by Djinn (same element)", refsFromList("djinn", djinnByElement(o.element))));
      break;
    case "classes":
      g.push(linkGroup("Grants Psynergy", refsFromList("psynergy", (o.psynergy||[]).map(p=>p.id).filter(Boolean))));
      g.push(linkGroup("Available to", refsFromList("characters", (o.available_to||[]).map(a=>a.character_id).filter(Boolean))));
      g.push(linkGroup("Same class line", refsFromList("classes", (DB.classes||[]).filter(c=>c.class_line===o.class_line&&c.id!==o.id).map(c=>c.id))));
      break;
    case "psynergy":
      g.push(linkGroup("Granted by classes", refsFromList("classes", rev.psyToClasses[o.id]||[])));
      g.push(linkGroup("Available to", refsFromList("characters", (o.available_to||[]).map(n=>{const c=charByName[n];return c&&c.id;}).filter(Boolean))));
      if(o.acquired_via_item&&o.acquired_via_item.item_id) g.push(linkGroup("Acquired via item", refChip("items",o.acquired_via_item.item_id)?`<div class="reflist">${refChip("items",o.acquired_via_item.item_id)}</div>`:""));
      if(o.series) g.push(linkGroup("Series", refsFromList("psynergy", (DB.psynergy||[]).filter(p=>p.series===o.series&&p.id!==o.id).map(p=>p.id))));
      break;
    case "equipment":
      g.push(linkGroup("Equippable by", refsFromList("characters", (o.equippable_by||[]).map(n=>{const c=charByName[n];return c&&c.id;}).filter(Boolean))));
      g.push(linkGroup("Sold at", refsFromList("shops", rev.gearToShops["equipment:"+o.id]||[])));
      g.push(linkGroup("Dropped by", refsFromList("monsters", rev.gearToMonsters["equipment:"+o.id]||[])));
      g.push(linkGroup("Found at", refsFromList("locations", locs)));
      break;
    case "items":
      g.push(linkGroup("Sold at", refsFromList("shops", rev.gearToShops["item:"+o.id]||[])));
      g.push(linkGroup("Dropped by", refsFromList("monsters", rev.gearToMonsters["item:"+o.id]||[])));
      g.push(linkGroup("Grants Psynergy", refsFromList("psynergy", rev.itemToPsy[o.id]||[])));
      g.push(linkGroup("Found at", refsFromList("locations", locs)));
      break;
    case "shops":
      g.push(linkGroup("Stock", refsFromList("equipment", (o.stock||[]).filter(s=>s.ref_type==="equipment").map(s=>s.ref_id)) + refsFromList("items", (o.stock||[]).filter(s=>s.ref_type==="item").map(s=>s.ref_id))));
      g.push(linkGroup("Location", refsFromList("locations", locs)));
      break;
    case "monsters":
      if(o.djinn_id) g.push(linkGroup("Djinni", refChip("djinn",o.djinn_id)?`<div class="reflist">${refChip("djinn",o.djinn_id)}</div>`:""));
      g.push(linkGroup("Drops", refsFromList("equipment", ((o.drops||{}).items||[]).filter(d=>d.ref_type==="equipment").map(d=>d.ref_id)) + refsFromList("items", ((o.drops||{}).items||[]).filter(d=>d.ref_type==="item").map(d=>d.ref_id))));
      g.push(linkGroup("Found at", refsFromList("locations", locs)));
      break;
    case "bosses":
      g.push(linkGroup("Found at", refsFromList("locations", locs)));
      break;
    case "locations": {
      const rec=LR.locations[o.id]||{};
      [["djinn","Djinn"],["bosses","Bosses"],["monsters","Monsters"],["equipment","Equipment"],["items","Items"],["shops","Shops"]].forEach(([cat,label])=>{
        g.push(linkGroup(label, refsFromList(cat, rec[cat]||[])));
      });
      break; }
    case "characters":
      g.push(linkGroup("Classes", refsFromList("classes", rev.charToClasses[o.id]||[])));
      g.push(linkGroup("Equippable equipment", refsFromList("equipment", rev.charToEquip[o.id]||[])));
      g.push(linkGroup("Psynergy", refsFromList("psynergy", rev.charToPsy[o.id]||[])));
      break;
  }
  const body=g.filter(Boolean).join("");
  return body ? `<div class="sect"><h3>Links</h3>${body}</div>` : "";
}

/* ---------------- wiki controller ---------------- */
let curType="locations", curId=null, search="";
function renderDetail(){
  const d=document.getElementById("detail");
  if(!curId || !byId[curType] || !byId[curType][curId]){ d.innerHTML='<div class="placeholder">Pick an entity, or click any linked chip to walk the graph.</div>'; return; }
  const o=byId[curType][curId]; const el=entEl(curType,o);
  d.innerHTML = `<h2>${el?elDot(el):""}${esc(o.qualified_name||o.name)}</h2>`
    + `<div class="subline"><span class="badge t-${curType}">${TYPE_LABEL[curType]}</span></div>`
    + `<div class="sect">${coreHTML(curType,o)}</div>`
    + linksHTML(curType,o)
    + (o.sources&&o.sources.length?`<div class="sect"><h3>Sources</h3><div class="prose">${esc(o.sources.join(", "))}</div></div>`:"");
}
function matchesSearch(o){ if(!search) return true; const s=search.toLowerCase();
  return (o.name||"").toLowerCase().includes(s) || (o.qualified_name||"").toLowerCase().includes(s) || (o.id||"").toLowerCase().includes(s); }
function renderList(){
  const rows=[];
  const types = curType==="__all__" ? TYPES : [curType];
  let n=0;
  types.forEach(t => (DB[t]||[]).filter(matchesSearch).forEach(o => { n++;
    const el=entEl(t,o);
    rows.push(`<div class="lrow ${t===curType&&o.id===curId?"sel":""}" data-type="${t}" data-id="${o.id}">${el?elDot(el):""}<span class="lname">${esc(o.qualified_name||o.name)}</span><span class="lmeta"><span class="badge t-${t}">${TYPE_LABEL[t]}</span></span></div>`);
  }));
  document.getElementById("list").innerHTML = rows.join("") || '<div class="listcount">no matches</div>';
  document.getElementById("listcount").textContent = `${n} ${curType==="__all__"?"entities":TYPE_LABEL[curType].toLowerCase()+(n===1?"":"s")}`;
}
function openEntity(type,id){
  curType=type; curId=id;
  document.getElementById("navbtn-wiki").click();
  renderList(); renderDetail();
  document.getElementById("detail").scrollTop=0;
}

// type filter chips
const chipbar=document.getElementById("typechips");
chipbar.innerHTML = [["__all__","All"]].concat(TYPES.map(t=>[t,TYPE_LABEL[t]+"s"]))
  .map(([t,l])=>`<span class="fchip ${t===curType?"on":""}" data-t="${t}">${l}</span>`).join("");
chipbar.addEventListener("click",e=>{ const c=e.target.closest(".fchip"); if(!c) return;
  curType=c.dataset.t; [...chipbar.children].forEach(x=>x.classList.toggle("on",x.dataset.t===curType)); renderList(); });
document.getElementById("search").addEventListener("input",e=>{ search=e.target.value.trim(); renderList(); });
document.getElementById("list").addEventListener("click",e=>{ const r=e.target.closest(".lrow"); if(!r) return;
  curType=r.dataset.type; curId=r.dataset.id; [...chipbar.children].forEach(x=>x.classList.toggle("on",x.dataset.t===curType)); renderList(); renderDetail(); });
document.getElementById("detail").addEventListener("click",e=>{ const r=e.target.closest(".ref[data-id]"); if(!r) return; openEntity(r.dataset.type,r.dataset.id); });

/* ---------------- planner (App A) ---------------- */
const CLASSES=DB.classes, PSYNERGY=DB.psynergy, CHARACTERS=DB.characters;
const psyById={}; PSYNERGY.forEach(p=>psyById[p.id]=p);
const NATIVE={}; CHARACTERS.forEach(c=>NATIVE[c.name]=c.element);
const PARTY=CHARACTERS.filter(c=>c.is_permanent&&c.element);
const REQ_ORDER=["plz2bstfu-class","strawhat","aku-chi"]; const CAP=7;
function pickReq(av){ for(const src of REQ_ORDER){ const r=av.djinn_requirements.find(r=>r.source===src&&r.parsed&&r.parsed.length); if(r) return r; } return null; }
function satisfies(parsed,counts,native){ const named={};
  for(const p of parsed){ if(counts[p.element]<p.min||counts[p.element]>p.max) return false; named[p.element]=true; }
  for(const el of ELEMS){ if(el===native||named[el]) continue; if(counts[el]>0) return false; } return true; }
function matchClasses(charName,counts){ const native=NATIVE[charName]; const out=[];
  for(const c of CLASSES){ if(!c.reachable_in_gs1) continue; const av=c.available_to.find(a=>a.character===charName); if(!av) continue;
    const req=pickReq(av); if(req&&satisfies(req.parsed,counts,native)) out.push({cls:c,av,req}); }
  out.sort((a,b)=>{ if(a.req.parsed.length!==b.req.parsed.length) return b.req.parsed.length-a.req.parsed.length;
    const w=r=>r.parsed.reduce((s,p)=>s+(p.max-p.min),0); return w(a.req)-w(b.req); });
  return out; }
function reverseCounts(av){ const req=pickReq(av); const c={earth:0,fire:0,wind:0,water:0}; if(req) for(const p of req.parsed) c[p.element]=p.min; return c; }
const pstate={}; PARTY.forEach(c=>pstate[c.name]={earth:0,fire:0,wind:0,water:0});
function pStatBars(sm){ if(!sm) return '<div class="psy empty" style="margin-top:10px">No stat multipliers in source.</div>';
  return `<div class="statgrid" style="margin-top:10px">`+[["hp","HP"],["pp","PP"],["atk","ATK"],["def","DEF"],["agi","AGI"],["lck","LCK"]].map(([k,l])=>{
    const v=sm[k]; const pct=Math.max(0,Math.min(100,(v/200)*100)); const cls=v>100?"high":(v<100?"low":"");
    return `<div class="sn">${l}</div><div class="barwrap"><div class="bar ${cls}" style="width:${pct}%"></div><div class="base" style="left:50%"></div></div><div class="sv">${v}%</div>`;
  }).join("")+`</div>`; }
function pPsyList(cls){ if(!cls.psynergy.length) return '<div class="empty">None.</div>';
  return "<ul>"+cls.psynergy.map(ps=>{ const p=psyById[ps.id]||{}; const el=p.element||"none"; const pp=p.pp_cost!=null?p.pp_cost+" PP":"";
    return `<li data-pid="${ps.id}">${elDot(el)}<span class="pn">${esc(ps.name)}</span><span class="pp">${pp}</span></li>`; }).join("")+"</ul>"; }
function renderResult(name){ const counts=pstate[name]; const matches=matchClasses(name,counts); const box=document.getElementById("res-"+name);
  if(!matches.length){ box.innerHTML='<div class="none">No class in the data matches this Djinn mix.</div>'; return; }
  const c=matches[0].cls; const lineTip=c.class_line!==c.id?` &middot; ${esc(c.class_line)} line`:"";
  let h=`<div class="classname" data-cid="${c.id}">${esc(c.qualified_name||c.name)}</div>`
    +`<div class="meta">acr ${matches[0].av.acr!=null?matches[0].av.acr+"/10":"&mdash;"}${lineTip}</div>`;
  if(matches.length>1) h+=`<div class="multi">Also valid: `+matches.slice(1).map(m=>`<span class="alt" data-c="${name}" data-id="${m.cls.id}">${esc(m.cls.qualified_name||m.cls.name)}</span>`).join(", ")+`</div>`;
  h+=pStatBars(c.stat_multiplier)+`<div class="psy"><h3>Psynergy &middot; ${c.psynergy.length}</h3>${pPsyList(c)}</div>`;
  box.innerHTML=h; }
function setCounts(name,counts){ pstate[name]=Object.assign({earth:0,fire:0,wind:0,water:0},counts); renderCard(name); }
function renderCard(name){ const counts=pstate[name]; const total=ELEMS.reduce((s,e)=>s+counts[e],0);
  ELEMS.forEach(el=>{ document.getElementById(`pval-${name}-${el}`).textContent=counts[el];
    document.getElementById(`pinc-${name}-${el}`).disabled=total>=CAP; document.getElementById(`pdec-${name}-${el}`).disabled=counts[el]<=0; });
  document.getElementById("ptot-"+name).innerHTML=`Set Djinn: <span class="${total>CAP?'over':''}">${total}</span> / ${CAP}`; renderResult(name); }
function buildCard(c){ const native=c.element;
  const reachable=CLASSES.filter(cl=>cl.reachable_in_gs1&&cl.available_to.some(a=>a.character===c.name)).map(cl=>({id:cl.id,label:cl.qualified_name||cl.name})).sort((a,b)=>a.label.localeCompare(b.label));
  const steppers=ELEMS.map(el=>{ const isN=el===native; return `<div class="stepper">
    <span class="lbl ${isN?'native':''}">${elDot(el)}<span class="nm tx-${el}">${EL_DJINN[el]}</span>${isN?' &#9733;':''}</span>
    <span class="ctrls"><button id="pdec-${c.name}-${el}" data-c="${c.name}" data-el="${el}" data-d="-1">&minus;</button>
    <span class="val" id="pval-${c.name}-${el}">0</span><button id="pinc-${c.name}-${el}" data-c="${c.name}" data-el="${el}" data-d="1">+</button></span></div>`; }).join("");
  const opts=`<option value="">&mdash; set Djinn for a target class &mdash;</option>`+reachable.map(r=>`<option value="${r.id}">${esc(r.label)}</option>`).join("");
  return `<div class="charcard" style="border-top-color:var(--${native})"><h2>${elDot(native)}${esc(c.name)}</h2>
    <div class="nativetag tx-${native}">${EL_DJINN[native]} Adept</div>${steppers}
    <div class="totalrow"><span id="ptot-${c.name}"></span><span class="reset" data-c="${c.name}">reset</span></div>
    <div class="reverse"><select id="prev-${c.name}" data-c="${c.name}">${opts}</select></div>
    <div class="result" id="res-${c.name}"></div></div>`; }
const pgrid=document.getElementById("pgrid"); pgrid.innerHTML=PARTY.map(buildCard).join("");
pgrid.addEventListener("click",e=>{
  const btn=e.target.closest("button[data-d]"); if(btn){ const {c,el,d}=btn.dataset; const counts=pstate[c]; const total=ELEMS.reduce((s,x)=>s+counts[x],0);
    const nv=counts[el]+(+d); if(nv<0) return; if(+d>0&&total>=CAP) return; counts[el]=nv; renderCard(c); return; }
  const rs=e.target.closest(".reset[data-c]"); if(rs){ setCounts(rs.dataset.c,{}); document.getElementById("prev-"+rs.dataset.c).value=""; return; }
  const alt=e.target.closest(".alt[data-id]"); if(alt){ const cl=CLASSES.find(x=>x.id===alt.dataset.id); const av=cl.available_to.find(a=>a.character===alt.dataset.c); setCounts(alt.dataset.c,reverseCounts(av)); return; }
  const cn=e.target.closest(".classname[data-cid]"); if(cn){ openEntity("classes",cn.dataset.cid); return; }
  const li=e.target.closest("li[data-pid]"); if(li){ openEntity("psynergy",li.dataset.pid); return; }
});
pgrid.addEventListener("change",e=>{ const sel=e.target.closest("select[data-c]"); if(!sel||!sel.value) return;
  const cl=CLASSES.find(x=>x.id===sel.value); const av=cl.available_to.find(a=>a.character===sel.dataset.c); setCounts(sel.dataset.c,reverseCounts(av)); });
PARTY.forEach(c=>renderCard(c.name));

/* ---------------- tabs ---------------- */
document.querySelector("nav").addEventListener("click",e=>{ const b=e.target.closest("button[data-tab]"); if(!b) return;
  const tab=b.dataset.tab; document.querySelectorAll("nav button").forEach(x=>x.classList.toggle("active",x===b));
  document.querySelectorAll(".tabpane").forEach(p=>p.classList.toggle("active",p.id==="tab-"+tab)); });

/* ---------------- init ---------------- */
renderList(); renderDetail();
</script>
</body>
</html>
"""


def main():
    db = {name: load(name) for name in ENTITIES}
    lr = load("location_refs")
    html = (TEMPLATE
            .replace("__DB__", embed(db))
            .replace("__LR__", embed(lr)))
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(html):,} bytes)")
    for name in ENTITIES:
        print(f"  {name:12} {len(db[name])}")


if __name__ == "__main__":
    main()
