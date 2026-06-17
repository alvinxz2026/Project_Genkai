"""Generate tools/gs1_build_planner.html — the GS1 Class / Build Planner (App A).

A self-contained static page: reads the source-of-truth JSON (classes, psynergy,
characters) and embeds it inline (so the page works over file:// with no fetch /
CORS), exactly like the existing tools/gs1_*_explorer.html. The page is a pure
read view; this script is the build step. Rerun after any data change:

    python scripts/build_planner.py

Matching model (forward: djinn distribution -> class):
  Class is determined by the count of Djinn per element set on a character. We
  resolve against ONE coherent source, plz2bstfu-class (distinct native-element
  ranges per tier + explicit off-element combos). It covers every GS1-reachable
  class for all four adepts except Ivan's White Mage, which falls back to
  strawhat (deterministic there, agrees with aku-chi). A class matches when:
    - every element named in its parsed requirement is within [min,max], AND
    - every OTHER non-native element is 0 (unnamed off-elements must be absent);
      the native element is unconstrained unless the requirement names it.
  Classes needing 8 djinn (Slayer/Chaos Lord/War Adept) are reachable_in_gs1
  =false (GS1 caps at 7 set djinn) and are excluded from matching.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "gs1"
OUT = ROOT / "tools" / "gs1_build_planner.html"


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def embed(data):
    """Minified JSON, safe to drop inside a <script> element."""
    return (json.dumps(data, separators=(",", ":"), ensure_ascii=False)
            .replace("</", "<\\/"))


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Adept's Codex — Build Planner</title>
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
  body {
    background:var(--bg);
    background-image:
      radial-gradient(ellipse 80% 50% at 50% -10%, rgba(176,140,46,.10), transparent),
      radial-gradient(ellipse 50% 40% at 10% 90%, rgba(143,106,14,.06), transparent);
    background-attachment:fixed; color:var(--text);
    font-family:var(--font-body); font-size:14px; min-height:100vh;
  }
  header { text-align:center; padding:30px 20px 6px; }
  header h1 {
    font-family:var(--font-display); font-size:32px; font-weight:400;
    letter-spacing:5px; text-transform:uppercase; color:var(--gold-bright);
    text-shadow:0 1px 0 rgba(255,255,255,.7), 0 0 24px rgba(176,140,46,.25);
  }
  header .subtitle { color:var(--text-dim); font-size:12.5px; letter-spacing:2.5px; text-transform:uppercase; margin-top:6px; }
  .header-rule { width:420px; max-width:80%; height:1px; margin:16px auto 0; background:linear-gradient(90deg,transparent,var(--gold),transparent); position:relative; }
  .header-rule::after { content:"\25C6"; position:absolute; left:50%; top:50%; transform:translate(-50%,-50%); color:var(--gold); font-size:9px; background:var(--bg); padding:0 10px; }

  main { max-width:1500px; margin:0 auto 60px; padding:18px; }
  .infobox {
    background:linear-gradient(180deg,var(--panel-2),var(--panel));
    border:1px solid var(--line); border-left:3px solid var(--gold-dim);
    border-radius:var(--radius); padding:12px 16px; margin-bottom:18px;
    color:var(--text-dim); font-size:13px; line-height:1.55;
  }
  .infobox b { color:var(--gold-bright); font-weight:600; }
  .infobox code { color:var(--text); background:var(--bg-deep); padding:1px 6px; border-radius:4px; font-size:12px; }

  .grid { display:grid; grid-template-columns:repeat(4,1fr); gap:16px; align-items:start; }
  @media (max-width:1200px){ .grid{ grid-template-columns:repeat(2,1fr);} }
  @media (max-width:640px){ .grid{ grid-template-columns:1fr;} }

  .charcard { background:var(--panel); border:1px solid var(--line); border-radius:var(--radius); padding:14px 15px; border-top:3px solid var(--neutral); }
  .charcard h2 { font-family:var(--font-display); font-size:21px; font-weight:400; letter-spacing:1.5px; color:var(--gold-bright); display:flex; align-items:center; gap:8px; }
  .charcard .nativetag { color:var(--text-faint); font-size:11px; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:12px; }

  .el-dot { display:inline-block; width:10px; height:10px; border-radius:50%; }
  .el-earth{background:var(--earth)} .el-fire{background:var(--fire)} .el-wind{background:var(--wind)} .el-water{background:var(--water)}
  .tx-earth{color:var(--earth)} .tx-fire{color:var(--fire)} .tx-wind{color:var(--wind)} .tx-water{color:var(--water)}

  .stepper { display:flex; align-items:center; justify-content:space-between; padding:5px 0; border-bottom:1px solid var(--line-soft); }
  .stepper .lbl { display:flex; align-items:center; gap:7px; font-size:13px; color:var(--text-dim); }
  .stepper .lbl.native .nm { font-weight:700; color:var(--text); }
  .stepper .ctrls { display:flex; align-items:center; gap:8px; }
  .stepper button { width:24px; height:24px; border-radius:6px; border:1px solid var(--line); background:var(--panel-2); color:var(--gold-bright); font-size:15px; line-height:1; cursor:pointer; font-family:var(--font-body); }
  .stepper button:hover:not(:disabled){ border-color:var(--gold-dim); background:var(--panel-3); }
  .stepper button:disabled{ opacity:.35; cursor:default; }
  .stepper .val { min-width:18px; text-align:center; font-variant-numeric:tabular-nums; font-size:15px; color:var(--text); }

  .totalrow { display:flex; justify-content:space-between; align-items:center; margin-top:8px; font-size:12px; color:var(--text-faint); letter-spacing:.5px; }
  .totalrow .over { color:var(--bad); font-weight:700; }
  .totalrow .reset { cursor:pointer; color:var(--gold-dim); text-decoration:underline; }

  .reverse { margin-top:10px; }
  .reverse select { width:100%; background:#fffdf6; border:1px solid var(--line); color:var(--text); border-radius:6px; padding:6px 8px; font-size:12.5px; font-family:var(--font-body); }

  .result { margin-top:14px; padding-top:12px; border-top:1px solid var(--line); }
  .result .classname { font-family:var(--font-display); font-size:20px; letter-spacing:1px; color:var(--gold-bright); }
  .result .meta { font-size:11.5px; color:var(--text-faint); letter-spacing:1px; text-transform:uppercase; margin-top:2px; }
  .result .none { color:var(--bad); font-style:italic; font-size:13px; }
  .result .multi { color:var(--text-dim); font-size:12px; margin-top:6px; }
  .result .multi .alt { cursor:pointer; text-decoration:underline dotted; }

  .statgrid { display:grid; grid-template-columns:34px 1fr 38px; gap:4px 8px; align-items:center; margin-top:10px; }
  .statgrid .sn { color:var(--text-dim); font-size:10.5px; letter-spacing:1px; text-transform:uppercase; }
  .statgrid .sv { font-size:12px; text-align:right; font-variant-numeric:tabular-nums; }
  .barwrap { background:var(--bg-deep); border-radius:4px; height:11px; position:relative; overflow:hidden; }
  .barwrap .bar { height:100%; border-radius:4px; background:linear-gradient(90deg,#d6bd7e,var(--gold)); }
  .barwrap .bar.low { background:linear-gradient(90deg,#d49a94,var(--bad)); }
  .barwrap .bar.high{ background:linear-gradient(90deg,#9ad4b2,var(--good)); }
  .barwrap .base { position:absolute; top:0; bottom:0; width:1px; background:rgba(44,38,24,.4); }

  .psy { margin-top:12px; }
  .psy h3 { font-size:10.5px; letter-spacing:2px; text-transform:uppercase; color:var(--gold-dim); border-bottom:1px solid var(--line-soft); padding-bottom:4px; margin-bottom:6px; }
  .psy ul { list-style:none; max-height:230px; overflow-y:auto; }
  .psy li { display:flex; align-items:center; gap:7px; padding:2.5px 0; font-size:12.5px; color:var(--text-dim); }
  .psy li .pn { color:var(--text); }
  .psy li .pp { margin-left:auto; color:var(--text-faint); font-size:11px; font-variant-numeric:tabular-nums; }
  .psy .empty { color:var(--text-faint); font-style:italic; font-size:12px; }
  footer { text-align:center; color:var(--text-faint); font-size:11px; letter-spacing:1px; padding:10px; }
</style>
</head>
<body>
<header>
  <h1>Adept's Codex</h1>
  <div class="subtitle">Build Planner &middot; Golden Sun</div>
  <div class="header-rule"></div>
</header>
<main>
  <div class="infobox">
    Set the Djinn each adept has <b>Set</b> (by element) and the planner resolves their
    <b>current class</b>, <b>stat multipliers</b>, and the <b>Psynergy</b> it grants. Or pick a
    target class from the dropdown to see the Djinn it needs. Class rules follow
    <code>plz2bstfu-class</code>; GS1 caps each adept at <b>7</b> Set Djinn, so 8-Djinn classes
    (Slayer, Chaos Lord, War Adept) are out of reach and omitted.
  </div>
  <div class="grid" id="grid"></div>
</main>
<footer>Pure read view over <code>data/gs1/</code> &middot; rebuild: <code>python scripts/build_planner.py</code></footer>

<script type="application/json" id="data-classes">__CLASSES__</script>
<script type="application/json" id="data-psynergy">__PSYNERGY__</script>
<script type="application/json" id="data-characters">__CHARACTERS__</script>
<script>
"use strict";
const CLASSES    = JSON.parse(document.getElementById("data-classes").textContent);
const PSYNERGY   = JSON.parse(document.getElementById("data-psynergy").textContent);
const CHARACTERS = JSON.parse(document.getElementById("data-characters").textContent);

const ELEMS = ["earth","fire","wind","water"];
const EL_DJINN = { earth:"Venus", fire:"Mars", wind:"Jupiter", water:"Mercury" };
const CAP = 7;
const psyById = {}; PSYNERGY.forEach(p => psyById[p.id] = p);
const NATIVE = {}; CHARACTERS.forEach(c => NATIVE[c.name] = c.element);
const PARTY = CHARACTERS.filter(c => c.is_permanent && c.element);
const REQ_ORDER = ["plz2bstfu-class","strawhat","aku-chi"];

function esc(s){ return String(s).replace(/[&<>]/g, m => ({"&":"&amp;","<":"&lt;",">":"&gt;"}[m])); }

// pick the requirement used for matching this (class, character)
function pickReq(av){
  for(const src of REQ_ORDER){
    const r = av.djinn_requirements.find(r => r.source === src && r.parsed && r.parsed.length);
    if(r) return r;
  }
  return null;
}
// does a djinn-count map satisfy a parsed requirement, given the native element?
function satisfies(parsed, counts, native){
  const named = {};
  for(const p of parsed){
    if(counts[p.element] < p.min || counts[p.element] > p.max) return false;
    named[p.element] = true;
  }
  for(const el of ELEMS){
    if(el === native || named[el]) continue;
    if(counts[el] > 0) return false;   // unnamed off-element must be absent
  }
  return true;
}
function matchClasses(charName, counts){
  const native = NATIVE[charName];
  const out = [];
  for(const c of CLASSES){
    if(!c.reachable_in_gs1) continue;
    const av = c.available_to.find(a => a.character === charName);
    if(!av) continue;
    const req = pickReq(av);
    if(req && satisfies(req.parsed, counts, native)) out.push({ cls:c, av:av, req:req });
  }
  // primary = the most specific requirement (boundary cases like "1 native + 6
  // off" can satisfy both an explicit dual class and a pure-6 shaman): prefer
  // more named elements, then tighter ranges.
  out.sort((a,b) => {
    if(a.req.parsed.length !== b.req.parsed.length) return b.req.parsed.length - a.req.parsed.length;
    const w = r => r.parsed.reduce((s,p) => s + (p.max - p.min), 0);
    return w(a.req) - w(b.req);
  });
  return out;
}
// a representative djinn distribution that yields the given class (reverse)
function reverseCounts(av){
  const req = pickReq(av);
  const counts = { earth:0, fire:0, wind:0, water:0 };
  if(req) for(const p of req.parsed) counts[p.element] = p.min;
  return counts;
}

const state = {}; // charName -> {earth,fire,wind,water}
PARTY.forEach(c => state[c.name] = { earth:0, fire:0, wind:0, water:0 });

function statBars(sm){
  if(!sm) return '<div class="psy empty" style="margin-top:10px">No stat multipliers in source.</div>';
  const keys = [["hp","HP"],["pp","PP"],["atk","ATK"],["def","DEF"],["agi","AGI"],["lck","LCK"]];
  let h = '<div class="statgrid">';
  for(const [k,lbl] of keys){
    const v = sm[k];
    const pct = Math.max(0, Math.min(100, (v/200)*100));      // 0..200% scale
    const cls = v > 100 ? "high" : (v < 100 ? "low" : "");
    h += `<div class="sn">${lbl}</div>`
       + `<div class="barwrap"><div class="bar ${cls}" style="width:${pct}%"></div><div class="base" style="left:50%"></div></div>`
       + `<div class="sv">${v}%</div>`;
  }
  return h + "</div>";
}
function psyList(cls){
  if(!cls.psynergy.length) return '<div class="empty">None.</div>';
  const rows = cls.psynergy.map(ps => {
    const p = psyById[ps.id] || {};
    const el = p.element || "none";
    const pp = (p.pp_cost != null) ? `${p.pp_cost} PP` : "";
    return `<li><span class="el-dot el-${el}"></span><span class="pn">${esc(ps.name)}</span><span class="pp">${pp}</span></li>`;
  }).join("");
  return `<ul>${rows}</ul>`;
}

function renderResult(charName){
  const counts = state[charName];
  const total = ELEMS.reduce((s,e)=>s+counts[e],0);
  const matches = matchClasses(charName, counts);
  const box = document.getElementById("res-"+charName);
  if(!matches.length){
    box.innerHTML = `<div class="none">No class in the data matches this Djinn mix.</div>`;
    return;
  }
  const primary = matches[0];
  const c = primary.cls;
  const lineTip = c.class_line !== c.id ? ` &middot; ${esc(c.class_line)} line` : "";
  let h = `<div class="classname">${esc(c.qualified_name || c.name)}</div>`
        + `<div class="meta">acr ${primary.av.acr != null ? primary.av.acr+"/10" : "&mdash;"}${lineTip}</div>`;
  if(matches.length > 1){
    h += `<div class="multi">Also valid: ` + matches.slice(1).map(m =>
        `<span class="alt" data-c="${charName}" data-id="${m.cls.id}">${esc(m.cls.qualified_name||m.cls.name)}</span>`
      ).join(", ") + `</div>`;
  }
  h += statBars(c.stat_multiplier);
  h += `<div class="psy"><h3>Psynergy &middot; ${c.psynergy.length}</h3>${psyList(c)}</div>`;
  box.innerHTML = h;
}

function setCounts(charName, counts){
  state[charName] = Object.assign({earth:0,fire:0,wind:0,water:0}, counts);
  renderCard(charName);
}
function renderCard(charName){
  const counts = state[charName];
  const total = ELEMS.reduce((s,e)=>s+counts[e],0);
  ELEMS.forEach(el => {
    document.getElementById(`val-${charName}-${el}`).textContent = counts[el];
    document.getElementById(`inc-${charName}-${el}`).disabled = total >= CAP;
    document.getElementById(`dec-${charName}-${el}`).disabled = counts[el] <= 0;
  });
  const tot = document.getElementById("tot-"+charName);
  tot.innerHTML = `Set Djinn: <span class="${total>CAP?'over':''}">${total}</span> / ${CAP}`;
  renderResult(charName);
}

function buildCard(c){
  const native = c.element;
  const reachable = CLASSES
    .filter(cl => cl.reachable_in_gs1 && cl.available_to.some(a => a.character === c.name))
    .map(cl => ({ id: cl.id, label: cl.qualified_name || cl.name }))
    .sort((a,b)=>a.label.localeCompare(b.label));

  let steppers = ELEMS.map(el => {
    const isN = el === native;
    return `<div class="stepper">
      <span class="lbl ${isN?'native':''}"><span class="el-dot el-${el}"></span><span class="nm tx-${el}">${EL_DJINN[el]}</span>${isN?' &#9733;':''}</span>
      <span class="ctrls">
        <button id="dec-${c.name}-${el}" data-c="${c.name}" data-el="${el}" data-d="-1">&minus;</button>
        <span class="val" id="val-${c.name}-${el}">0</span>
        <button id="inc-${c.name}-${el}" data-c="${c.name}" data-el="${el}" data-d="1">+</button>
      </span></div>`;
  }).join("");

  const opts = `<option value="">&mdash; set Djinn for a target class &mdash;</option>` +
    reachable.map(r => `<option value="${r.id}">${esc(r.label)}</option>`).join("");

  return `<div class="charcard" style="border-top-color:var(--${native})">
    <h2><span class="el-dot el-${native}"></span>${esc(c.name)}</h2>
    <div class="nativetag tx-${native}">${EL_DJINN[native]} Adept</div>
    ${steppers}
    <div class="totalrow"><span id="tot-${c.name}"></span><span class="reset" data-c="${c.name}">reset</span></div>
    <div class="reverse"><select id="rev-${c.name}" data-c="${c.name}">${opts}</select></div>
    <div class="result" id="res-${c.name}"></div>
  </div>`;
}

const grid = document.getElementById("grid");
grid.innerHTML = PARTY.map(buildCard).join("");

grid.addEventListener("click", e => {
  const btn = e.target.closest("button[data-d]");
  if(btn){
    const {c, el, d} = btn.dataset;
    const counts = state[c];
    const total = ELEMS.reduce((s,x)=>s+counts[x],0);
    const nv = counts[el] + (+d);
    if(nv < 0) return;
    if(+d > 0 && total >= CAP) return;
    counts[el] = nv; renderCard(c); return;
  }
  const rs = e.target.closest(".reset[data-c]");
  if(rs){ setCounts(rs.dataset.c, {}); document.getElementById("rev-"+rs.dataset.c).value=""; return; }
  const alt = e.target.closest(".alt[data-id]");
  if(alt){
    const cl = CLASSES.find(x => x.id === alt.dataset.id);
    const av = cl.available_to.find(a => a.character === alt.dataset.c);
    setCounts(alt.dataset.c, reverseCounts(av));
    return;
  }
});
grid.addEventListener("change", e => {
  const sel = e.target.closest("select[data-c]");
  if(!sel || !sel.value) return;
  const cl = CLASSES.find(x => x.id === sel.value);
  const av = cl.available_to.find(a => a.character === sel.dataset.c);
  setCounts(sel.dataset.c, reverseCounts(av));
});

PARTY.forEach(c => renderCard(c.name));
</script>
</body>
</html>
"""


def main():
    classes = load("classes.json")
    psynergy = load("psynergy.json")
    characters = load("characters.json")

    # trim psynergy to the fields the page actually reads (keeps the file small)
    psy_lite = [{"id": p["id"], "name": p["name"], "element": p.get("element"),
                 "pp_cost": p.get("pp_cost"), "tier": p.get("tier")}
                for p in psynergy]

    html = (TEMPLATE
            .replace("__CLASSES__", embed(classes))
            .replace("__PSYNERGY__", embed(psy_lite))
            .replace("__CHARACTERS__", embed(characters)))
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(html):,} bytes)")
    print(f"  classes={len(classes)} psynergy={len(psy_lite)} characters={len(characters)}")


if __name__ == "__main__":
    main()
