"""Generate tools/gs2_codex.html — the GS2 "Adept's Codex" (Phase 1 MVP: connection layer).

Forked from build_codex.py (gs1). This MVP is the *Wiki connection layer*:
  * graph-aware browser over all 11 gs2 entities + location_refs.json,
  * every cross-entity FK rendered as a clickable chip (both directions) so you
    can walk the connected graph,
  * HOVER tooltips on any chip / list row (quick stat peek without navigating),
  * a Provenance / Source-Inspector layer: per-entity `sources`, `conflicts`,
    and `name_variants` surfaced on every record (the lore-engine differentiator).

Single self-contained static page; embeds the SoT JSON inline (works over file://
with no fetch/CORS). Pure read view. Rerun after any data change:

    python scripts/build_codex_gs2.py

Ported from gs1: the Build Planner tab (Set-Djinn distribution -> class/stats/
Psynergy), adapted to gs2 data shapes + a SHARED 72-Djinn pool across all 8 TLA
adepts. Phase 2 progression gate is LIVE: the region selector filters the pool to
Djinn reachable by that point (djinn.location.area -> locations.order join).
gs2 data shapes differ from gs1, so coreHTML/linksHTML/reverse-indexes were
rewritten for gs2 (see gs2_er_sketch.md).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "gs2"
OUT = ROOT / "tools" / "gs2_codex.html"

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
<title>Adept's Codex — Golden Sun: The Lost Age</title>
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

  main { max-width:1500px; margin:18px auto 60px; min-height:72vh; padding:0 18px; }

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
  .gs1tag { font-size:9px; letter-spacing:1px; text-transform:uppercase; color:var(--text-faint); border:1px dashed var(--line); border-radius:4px; padding:0 5px; margin-left:6px; }

  .toolbar { display:flex; gap:12px; flex-wrap:wrap; align-items:center; background:var(--panel); border:1px solid var(--line);
    border-radius:var(--radius); padding:10px 14px; margin-bottom:14px; }
  .toolbar input[type=text] { background:#fffdf6; border:1px solid var(--line); color:var(--text); border-radius:6px;
    padding:7px 10px; font-size:13px; outline:none; font-family:var(--font-body); width:260px; }
  .toolbar input[type=text]:focus { border-color:var(--gold-dim); }
  .chipbar { display:flex; gap:5px; flex-wrap:wrap; }
  .fchip { background:var(--panel-2); border:1px solid var(--line-soft); color:var(--text-dim); border-radius:13px;
    padding:3px 11px; font-size:12px; cursor:pointer; user-select:none; transition:all .12s; }
  .fchip:hover { color:var(--text); border-color:var(--gold-dim); }
  .fchip.on { background:var(--gold); color:#fdfbf4; border-color:var(--gold); font-weight:600; }
  .wiki-layout { display:grid; grid-template-columns:minmax(0,1fr) 600px; gap:16px; align-items:start; }
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
  .detail h2 { font-family:var(--font-display); font-size:23px; letter-spacing:1px; color:var(--gold-bright); font-weight:400; display:inline; }
  .detail .subline { margin-top:6px; }
  .srcpill { display:inline-block; font-size:10px; letter-spacing:.5px; color:var(--text-faint); border:1px solid var(--line-soft);
    background:var(--panel-2); border-radius:10px; padding:1px 8px; margin-left:8px; cursor:help; vertical-align:2px; }
  .sect { margin-top:16px; }
  .sect h3 { font-size:10.5px; letter-spacing:2.5px; text-transform:uppercase; color:var(--gold-dim);
    border-bottom:1px solid var(--line-soft); padding-bottom:4px; margin-bottom:8px; }
  .kv { display:grid; grid-template-columns:140px 1fr; gap:3px 10px; font-size:13px; }
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

  .statgrid { display:grid; grid-template-columns:44px 1fr 52px; gap:4px 8px; align-items:center; }
  .statgrid .sn { color:var(--text-dim); font-size:10.5px; letter-spacing:1px; text-transform:uppercase; }
  .statgrid .sv { font-size:12px; text-align:right; font-variant-numeric:tabular-nums; }
  .barwrap { background:var(--bg-deep); border-radius:4px; height:11px; position:relative; overflow:hidden; }
  .barwrap .bar { height:100%; border-radius:4px; background:linear-gradient(90deg,#d6bd7e,var(--gold)); }
  .barwrap .bar.low{ background:linear-gradient(90deg,#d49a94,var(--bad)); } .barwrap .bar.high{ background:linear-gradient(90deg,#9ad4b2,var(--good)); }
  .barwrap .base { position:absolute; top:0; bottom:0; width:1px; background:rgba(44,38,24,.4); }
  .elgrid { display:grid; grid-template-columns:repeat(4,1fr); gap:4px; font-size:11.5px; text-align:center; }
  .elgrid .ec { background:var(--panel-2); border:1px solid var(--line-soft); border-radius:6px; padding:4px 2px; }
  .elgrid .ec .en { font-size:9px; letter-spacing:.5px; text-transform:uppercase; color:var(--text-faint); }
  .elgrid .ec .ev { font-variant-numeric:tabular-nums; color:var(--text-dim); }

  .conflict { background:#fbf0ea; border:1px solid #d6a08f; border-left:3px solid var(--fire); border-radius:7px;
    padding:8px 11px; font-size:12px; color:#7a3030; margin-top:6px; }
  .variants { font-size:12px; color:var(--text-dim); }
  .variants b { color:var(--text); }

  /* contextual facet filters */
  .facetbar { display:flex; flex-wrap:wrap; gap:8px 18px; align-items:center; margin:-2px 2px 14px; }
  .facetbar:empty { display:none; }
  .facetgrp { display:flex; align-items:center; gap:6px; flex-wrap:wrap; }
  .facetgrp .flabel { font-size:10px; letter-spacing:1.5px; text-transform:uppercase; color:var(--text-faint); margin-right:1px; }
  .facet { display:inline-flex; align-items:center; background:var(--panel); border:1px solid var(--line-soft); color:var(--text-dim);
    border-radius:11px; padding:2px 9px; font-size:11.5px; cursor:pointer; user-select:none; transition:all .12s; }
  .facet:hover { border-color:var(--gold-dim); color:var(--text); }
  .facet.on { background:var(--gold); color:#fdfbf4; border-color:var(--gold); font-weight:600; }
  .facet .fc { font-size:10px; margin-left:4px; color:var(--text-faint); font-variant-numeric:tabular-nums; }
  .facet.on .fc { color:#fdf6e6; }
  .refmore { display:inline-block; font-size:11.5px; color:var(--gold-dim); cursor:pointer; text-decoration:underline dotted; padding:3px 6px; }
  .refmore:hover { color:var(--gold-bright); }

  /* hover tooltip */
  #tip { position:fixed; z-index:99; pointer-events:none; max-width:300px; background:#fffdf6; border:1px solid var(--gold-dim);
    border-radius:8px; box-shadow:0 8px 26px rgba(60,48,18,.22); padding:9px 12px; font-size:12px; color:var(--text-dim);
    display:none; }
  #tip .tt { font-family:var(--font-display); font-size:15px; color:var(--gold-bright); margin-bottom:4px; }
  #tip .tk { color:var(--text-faint); }
  #tip .ttype { font-size:9px; letter-spacing:1px; text-transform:uppercase; color:var(--text-faint); }

  /* ---- nav / tabs ---- */
  nav { display:flex; justify-content:center; gap:6px; padding:14px 20px 0; flex-wrap:wrap; }
  nav button { font-family:var(--font-display); font-size:14px; letter-spacing:2px; text-transform:uppercase;
    background:transparent; color:var(--text-dim); border:1px solid transparent; border-bottom:none;
    padding:9px 28px; cursor:pointer; border-radius:var(--radius) var(--radius) 0 0; transition:color .15s, background .15s; }
  nav button:hover { color:var(--gold-bright); }
  nav button.active { color:var(--gold-bright); background:var(--panel); border-color:var(--line); box-shadow:0 -4px 16px rgba(80,64,24,.08); }
  .tabpane { display:none; } .tabpane.active { display:block; }

  /* ---- planner ---- */
  .infobox { background:linear-gradient(180deg,var(--panel-2),var(--panel)); border:1px solid var(--line); border-left:3px solid var(--gold-dim);
    border-radius:var(--radius); padding:12px 16px; margin-bottom:14px; color:var(--text-dim); font-size:13px; line-height:1.55; }
  .infobox b { color:var(--gold-bright); } .infobox code { color:var(--text); background:var(--bg-deep); padding:1px 6px; border-radius:4px; font-size:12px; }
  .poolbar { display:flex; flex-wrap:wrap; gap:10px 22px; align-items:center; background:var(--panel); border:1px solid var(--line);
    border-radius:var(--radius); padding:10px 16px; margin-bottom:18px; }
  .poolbar .ptitle { font-size:10px; letter-spacing:2px; text-transform:uppercase; color:var(--text-faint); }
  .progress-row { display:flex; align-items:center; gap:10px; margin-bottom:12px; flex-wrap:wrap; }
  .progress-row label { font-size:12px; color:var(--text-faint); white-space:nowrap; }
  .progress-row select { background:var(--panel); color:var(--text); border:1px solid var(--line); border-radius:4px; padding:3px 8px; font-size:13px; }
  .pool-hint { font-size:12px; color:var(--text-faint); }
  .tk-reset { font-size:11px; color:var(--text-faint); cursor:pointer; text-decoration:underline; margin-left:auto; }
  .tk-reset:hover { color:var(--text); }
  #tracker-reachable { margin-bottom:18px; }
  .tk-reach { background:var(--panel); border:1px solid var(--line); border-left:3px solid var(--earth);
    border-radius:var(--radius); padding:12px 16px; }
  .tk-reach h3 { margin:0 0 8px; font-size:12px; letter-spacing:1px; text-transform:uppercase; color:var(--text-dim); }
  .tk-reach ul { margin:0; padding-left:0; list-style:none; display:flex; flex-wrap:wrap; gap:6px 10px; }
  .tk-reach li { font-size:12px; }
  .tk-reach .tk-go { color:var(--text); cursor:pointer; border-bottom:1px dotted var(--text-faint); }
  .tk-reach .tk-where { color:var(--text-faint); }
  .tk-reach.empty { border-left-color:var(--line); color:var(--text-faint); font-size:12px; }
  .tk-region { background:var(--panel); border:1px solid var(--line); border-radius:var(--radius);
    margin-bottom:10px; overflow:hidden; }
  .tk-region.locked { opacity:.55; }
  .tk-rhead { display:flex; align-items:center; gap:10px; padding:9px 14px; cursor:pointer; user-select:none; }
  .tk-rhead:hover { background:var(--panel-2,rgba(255,255,255,.02)); }
  .tk-rhead .tk-ord { font-size:11px; color:var(--text-faint); font-variant-numeric:tabular-nums; min-width:32px; }
  .tk-rhead .tk-name { font-weight:600; font-size:14px; }
  .tk-rhead .tk-count { margin-left:auto; font-size:12px; color:var(--text-dim); font-variant-numeric:tabular-nums; }
  .tk-rhead .tk-bar { width:60px; height:4px; border-radius:2px; background:var(--line); overflow:hidden; }
  .tk-rhead .tk-fill { height:100%; background:var(--earth); width:0; }
  .tk-rbody { padding:4px 14px 12px 14px; display:none; }
  .tk-region.open .tk-rbody { display:block; }
  .tk-row { display:flex; align-items:center; gap:9px; padding:4px 0; font-size:13px; }
  .tk-row input { accent-color:var(--earth); cursor:pointer; }
  .tk-row.done .tk-iname { text-decoration:line-through; color:var(--text-faint); }
  .tk-iname { cursor:pointer; }
  .tk-iname:hover { color:var(--earth); }
  .tk-kind { font-size:10px; text-transform:uppercase; letter-spacing:.5px; color:var(--text-faint);
    border:1px solid var(--line); border-radius:3px; padding:0 4px; }
  .tk-gate { font-size:11px; color:#caa84a; }
  .tk-gate.open { color:#6fae5f; }
  .poolel { display:flex; align-items:center; gap:8px; min-width:150px; }
  .poolel .pn { font-size:12px; min-width:54px; } .poolel .pcount { font-size:12px; font-variant-numeric:tabular-nums; color:var(--text-dim); min-width:42px; text-align:right; }
  .poolel .pcount.over { color:var(--bad); font-weight:700; }
  .poolwrap { flex:1; background:var(--bg-deep); border-radius:4px; height:9px; overflow:hidden; min-width:50px; }
  .poolwrap .pfill { height:100%; border-radius:4px; }
  .pgrid { display:grid; grid-template-columns:repeat(4,1fr); gap:14px; align-items:start; }
  @media (max-width:1200px){ .pgrid{ grid-template-columns:repeat(2,1fr);} } @media (max-width:640px){ .pgrid{ grid-template-columns:1fr;} }
  .charcard { background:var(--panel); border:1px solid var(--line); border-radius:var(--radius); padding:14px 15px; border-top:3px solid var(--neutral); }
  .charcard h2 { font-family:var(--font-display); font-size:20px; font-weight:400; letter-spacing:1.5px; color:var(--gold-bright); display:flex; align-items:center; gap:8px; }
  .charcard .nativetag { color:var(--text-faint); font-size:11px; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:12px; }
  .stepper { display:flex; align-items:center; justify-content:space-between; padding:5px 0; border-bottom:1px solid var(--line-soft); }
  .stepper .lbl { display:flex; align-items:center; gap:7px; font-size:13px; color:var(--text-dim); }
  .stepper .lbl.native .nm { font-weight:700; color:var(--text); }
  .stepper .ctrls { display:flex; align-items:center; gap:8px; }
  .stepper button { width:24px; height:24px; border-radius:6px; border:1px solid var(--line); background:var(--panel-2); color:var(--gold-bright); font-size:15px; line-height:1; cursor:pointer; font-family:var(--font-body); }
  .stepper button:hover:not(:disabled){ border-color:var(--gold-dim); background:var(--panel-3); } .stepper button:disabled{ opacity:.35; cursor:default; }
  .stepper .val { min-width:18px; text-align:center; font-variant-numeric:tabular-nums; font-size:15px; color:var(--text); }
  .totalrow { display:flex; justify-content:space-between; align-items:center; margin-top:8px; font-size:12px; color:var(--text-faint); }
  .totalrow .reset { cursor:pointer; color:var(--gold-dim); text-decoration:underline; }
  .reverse { margin-top:10px; } .reverse select { width:100%; background:#fffdf6; border:1px solid var(--line); color:var(--text); border-radius:6px; padding:6px 8px; font-size:12.5px; font-family:var(--font-body); }
  .result { margin-top:14px; padding-top:12px; border-top:1px solid var(--line); }
  .result .classname { font-family:var(--font-display); font-size:19px; letter-spacing:1px; color:var(--gold-bright); cursor:pointer; }
  .result .classname:hover { text-decoration:underline; }
  .result .meta { font-size:11.5px; color:var(--text-faint); letter-spacing:1px; text-transform:uppercase; margin-top:2px; }
  .result .none { color:var(--bad); font-style:italic; font-size:13px; }
  .result .multi { color:var(--text-dim); font-size:12px; margin-top:6px; } .result .multi .alt { cursor:pointer; text-decoration:underline dotted; }
  .psy { margin-top:12px; } .psy h3 { font-size:10.5px; letter-spacing:2px; text-transform:uppercase; color:var(--gold-dim); border-bottom:1px solid var(--line-soft); padding-bottom:4px; margin-bottom:6px; }
  .psy ul { list-style:none; max-height:230px; overflow-y:auto; } .psy li { display:flex; align-items:center; gap:7px; padding:2.5px 0; font-size:12.5px; color:var(--text-dim); cursor:pointer; }
  .psy li:hover .pn { text-decoration:underline; } .psy li .pn { color:var(--text); } .psy li .pp { margin-left:auto; color:var(--text-faint); font-size:11px; }
  .psy .empty { color:var(--text-faint); font-style:italic; font-size:12px; }
  footer { text-align:center; color:var(--text-faint); font-size:11px; letter-spacing:1px; padding:10px; }
  footer code { color:var(--text-dim); }
</style>
</head>
<body>
<header>
  <h1>Adept's Codex</h1>
  <div class="subtitle">Golden Sun: The Lost Age &middot; Knowledge Graph</div>
</header>
<nav>
  <button id="navbtn-wiki" class="active" data-tab="wiki">Wiki</button>
  <button id="navbtn-planner" data-tab="planner">Build Planner</button>
  <button id="navbtn-tracker" data-tab="tracker">Tracker</button>
</nav>
<main>
  <div class="tabpane active" id="tab-wiki">
    <div class="toolbar">
      <input type="text" id="search" placeholder="Search any entity&hellip;" autocomplete="off">
      <div class="chipbar" id="typechips"></div>
    </div>
    <div class="facetbar" id="facets"></div>
    <div class="wiki-layout">
      <div>
        <div class="listcount" id="listcount"></div>
        <div class="list" id="list"></div>
      </div>
      <div class="detail" id="detail"><div class="placeholder">Pick an entity, or click any linked chip to walk the graph. Hover a chip for a quick peek.</div></div>
    </div>
  </div>
  <div class="tabpane" id="tab-planner">
    <div class="infobox">
      Set the Djinn each adept has <b>Set</b> (by element) to resolve their <b>current class</b>, <b>stat multipliers</b>,
      and <b>Psynergy</b> — or pick a target class to see a Djinn setup for it. The whole party <b>shares one Djinn pool</b>
      (18 per element); assigning a Djinni to one adept removes it from the others. Matching follows <code>telago</code>
      ranges + <code>ultimalink</code> exact builds; <code>other</code> = "each non-native element" (Trickster lines).
      Class &amp; Psynergy names link into the Wiki. Use the <b>Progress gate</b> to restrict the pool to Djinn reachable at your current point in the game.
    </div>
    <div class="progress-row">
      <label for="region-sel">Progress gate:</label>
      <select id="region-sel"><option value="">Full game (sandbox)</option></select>
      <span class="pool-hint" id="pool-hint"></span>
    </div>
    <div class="poolbar" id="poolbar"></div>
    <div class="pgrid" id="pgrid"></div>
  </div>
  <div class="tabpane" id="tab-tracker">
    <div class="infobox">
      Tick off what you've collected; progress is saved in your browser (<code>localStorage</code>).
      Items behind a Psynergy or story event you don't yet have show a <b>return-trip badge</b>.
      Set the <b>Progress gate</b> to your current point and the panel up top lists everything that's
      become reachable but isn't checked off &mdash; your "go back for it" list. <i>GS2 is an open
      world: nothing is permanently missable, so this is a backtrack reminder, not a last-chance warning.</i>
    </div>
    <div class="progress-row">
      <label for="tracker-region-sel">Progress gate:</label>
      <select id="tracker-region-sel"><option value="">Full game (sandbox)</option></select>
      <span class="pool-hint" id="tracker-overall"></span>
      <span class="tk-reset" id="tracker-reset">reset checklist</span>
    </div>
    <div id="tracker-reachable"></div>
    <div id="tracker-list"></div>
  </div>
</main>
<footer>Pure read view over <code>data/gs2/</code> &middot; provenance-first &middot; rebuild: <code>python scripts/build_codex_gs2.py</code></footer>
<div id="tip"></div>

<script type="application/json" id="data-db">__DB__</script>
<script type="application/json" id="data-lr">__LR__</script>
<script type="application/json" id="data-ag">__AG__</script>
<script>
"use strict";
const DB = JSON.parse(document.getElementById("data-db").textContent);
const LR = JSON.parse(document.getElementById("data-lr").textContent);
const AG = JSON.parse(document.getElementById("data-ag").textContent);
const TYPES = ["djinn","summons","classes","psynergy","equipment","items","shops","monsters","bosses","locations","characters"];
const ELEMS = ["earth","fire","wind","water"];
const EL_DJINN = { earth:"Venus", fire:"Mars", wind:"Jupiter", water:"Mercury" };
const TYPE_LABEL = { djinn:"Djinni", summons:"Summon", classes:"Class", psynergy:"Psynergy", equipment:"Equipment",
  item:"Item", items:"Item", shops:"Shop", monsters:"Monster", bosses:"Boss", locations:"Location", characters:"Character" };
const EL_ORDER = ["earth","fire","wind","water","neutral"];
const CAP_REFS = 30;   // collapse link lists longer than this
// contextual sub-filters per entity type; get() -> value | array | null
const FACETS = {
  djinn:[{key:"element",label:"Element",get:o=>o.element}],
  summons:[{key:"element",label:"Element",get:o=>o.element},{key:"combo",label:"Kind",get:o=>o.is_combo?"combo":"standard"}],
  psynergy:[{key:"element",label:"Element",get:o=>o.element}],
  equipment:[{key:"category",label:"Category",get:o=>o.category},{key:"type",label:"Type",get:o=>o.type},
    {key:"src",label:"Set",get:o=>o.game==="gs1"?"base/GS1":"TLA"},
    {key:"flags",label:"Flags",get:o=>{const f=[];if(o.is_cursed)f.push("cursed");if(o.is_rusty)f.push("rusty");if(o.unleash)f.push("unleash");return f.length?f:null;}}],
  items:[{key:"item_type",label:"Type",get:o=>o.item_type}],
  monsters:[{key:"role",label:"Role",get:o=>o.is_boss?"boss":(o.is_djinn_enemy?"djinn":"normal")}],
  bosses:[{key:"kind",label:"Kind",get:o=>o.is_superboss?"superboss":(o.is_optional?"optional":"story")}],
  locations:[{key:"kind",label:"Kind",get:o=>o.kind}],
  characters:[{key:"element",label:"Element",get:o=>o.element}],
  classes:[{key:"dominance_group",label:"Group",get:o=>o.dominance_group}],
};

function esc(s){ return String(s==null?"":s).replace(/[&<>]/g, m=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[m])); }
function elDot(el){ return `<span class="el-dot el-${el||"none"}"></span>`; }
function uniq(a){ return [...new Set(a)]; }

/* ---------------- indexes ---------------- */
const byId = {}; TYPES.forEach(t => { byId[t]={}; (DB[t]||[]).forEach(o => byId[t][o.id]=o); });
const charByName = {}; (DB.characters||[]).forEach(c => charByName[c.name]=c);
const itemByName = {}; (DB.items||[]).forEach(o => { itemByName[(o.name||"").toLowerCase()]=o; (o.name_variants||[]).forEach(v=>itemByName[v.toLowerCase()]=o); });
const equipByName = {}; (DB.equipment||[]).forEach(o => { equipByName[(o.name||"").toLowerCase()]=o; (o.name_variants||[]).forEach(v=>equipByName[v.toLowerCase()]=o); });

const rev = { psyToClasses:{}, charToClasses:{}, gearToShops:{}, gearToMonsters:{},
  djinnToMonster:{}, bossToMonster:{}, charToEquip:{}, matToEquip:{} };
function push(map,k,v){ (map[k]=map[k]||[]).push(v); }

(DB.classes||[]).forEach(c => {
  (c.psynergy||[]).forEach(p => { if(p.id) push(rev.psyToClasses, p.id, c.id); });
  (c.available_to||[]).forEach(a => { if(a.character_id) push(rev.charToClasses, a.character_id, c.id); });
});
(DB.shops||[]).forEach(s => (s.stock||[]).forEach(st => { if(st.ref_id) push(rev.gearToShops, st.ref_type+":"+st.ref_id, s.id); }));
(DB.monsters||[]).forEach(m => {
  (((m.drops||{}).items)||[]).forEach(d => { if(d.ref_id) push(rev.gearToMonsters, d.ref_type+":"+d.ref_id, m.id); });
  if(m.djinn_id) push(rev.djinnToMonster, m.djinn_id, m.id);
  if(m.boss_id) push(rev.bossToMonster, m.boss_id, m.id);
});
(DB.equipment||[]).forEach(e => {
  (e.equippable_by||[]).forEach(n => { const c=charByName[n]; if(c) push(rev.charToEquip, c.id, e.id); });
  (e.forged_from||[]).forEach(mn => { const it=itemByName[(mn||"").toLowerCase()]; if(it) push(rev.matToEquip, it.id, e.id); });
});

// location_refs: index = {cat:{entityId:[regionId]}}; regions[rid].pickups carry ref_id for equipment/items.
const locOf = {};   // "cat:id" -> [regionId]
["djinn","monsters","bosses","summons","shops"].forEach(cat => {
  const m = (LR.index||{})[cat]||{};
  Object.keys(m).forEach(id => locOf[cat+":"+id] = m[id]);
});
Object.keys(LR.regions||{}).forEach(rid => {
  ((LR.regions[rid].pickups)||[]).forEach(p => { if(p.ref_id) push(locOf, p.ref_type+":"+p.ref_id, rid); });
});
function locFor(cat,id){ return uniq(locOf[cat+":"+id]||[]); }

function djinnByElement(el){ return (DB.djinn||[]).filter(d=>d.element===el).map(d=>d.id); }
function summonsByElement(el){ return (DB.summons||[]).filter(s=>s.element===el).map(s=>s.id); }

/* ---------------- shared rendering ---------------- */
function entEl(type,o){ if(["djinn","summons","psynergy","characters"].includes(type)) return o.element||null; return null; }
function fmtVal(v){
  if(v==null) return "";
  if(Array.isArray(v)) return v.map(fmtVal).filter(Boolean).join(", ");
  if(typeof v==="object") return Object.entries(v).filter(([,x])=>x!=null&&x!==""&&x!==0).map(([k,x])=>`${k} ${fmtVal(x)}`).join(", ");
  return String(v);
}
function nameOf(type,id){ const o=byId[type]&&byId[type][id]; return o ? (o.qualified_name||o.name) : id; }
function refChip(type,id){
  if(!byId[type]||!byId[type][id]) return "";
  const o=byId[type][id]; const el=entEl(type,o);
  return `<span class="ref" data-type="${type}" data-id="${esc(id)}">${el?elDot(el):""}${esc(o.qualified_name||o.name)}<span class="rt">${TYPE_LABEL[type]}</span></span>`;
}
function refsFromList(type, ids){ ids=uniq((ids||[]).filter(Boolean)); if(!ids.length) return "";
  if(ids.length<=CAP_REFS) return `<div class="reflist">${ids.map(id=>refChip(type,id)).join("")}</div>`;
  const head=ids.slice(0,CAP_REFS).map(id=>refChip(type,id)).join("");
  const tail=ids.slice(CAP_REFS).map(id=>refChip(type,id)).join("");
  return `<div class="reflist">${head}<span class="refhidden" hidden>${tail}</span><span class="refmore" data-more="1">+ ${ids.length-CAP_REFS} more</span></div>`; }
function linkGroup(label, html){ if(!html) return ""; return `<div class="linkgroup"><div class="glabel"><b>${label}</b></div>${html}</div>`; }
function kv(rows){ return `<div class="kv">${rows.filter(r=>r[1]!=null&&r[1]!=="").map(r=>`<div class="k">${r[0]}</div><div class="v">${r[1]}</div>`).join("")}</div>`; }

function statBars(obj, keys, scaleMax, baselinePct){
  const present=keys.filter(([k])=>obj[k]!=null); if(!present.length) return "";
  let h='<div class="statgrid">';
  for(const [k,lbl] of present){
    const v=obj[k]; const pct=Math.max(0,Math.min(100,(v/scaleMax)*100));
    const cls = baselinePct!=null ? (v>100?"high":(v<100?"low":"")) : "";
    h+=`<div class="sn">${lbl}</div><div class="barwrap"><div class="bar ${cls}" style="width:${pct}%"></div>`
      +(baselinePct!=null?`<div class="base" style="left:${baselinePct}%"></div>`:"")+`</div>`
      +`<div class="sv">${v}${baselinePct!=null?"%":""}</div>`;
  }
  return h+"</div>";
}
function elementGrid(obj){
  if(!obj) return ""; const present=ELEMS.filter(e=>obj[e]!=null); if(!present.length) return "";
  return `<div class="elgrid">`+ELEMS.map(e=>`<div class="ec"><div class="en tx-${e}">${EL_DJINN[e]}</div><div class="ev">${obj[e]!=null?obj[e]:"&middot;"}</div></div>`).join("")+`</div>`;
}

/* ---------------- per-type core fields ---------------- */
function coreHTML(type,o){
  switch(type){
    case "djinn": { let h=kv([["Element",`${elDot(o.element)}<span class="tx-${o.element}">${EL_DJINN[o.element]}</span>`],
        ["Battle effect",esc(fmtVal(o.battle_effect))||"stat bonus only"],
        ["Must fight",o.must_fight?"yes":"no"],["Found",esc((o.location||{}).area)]]);
      if(o.stat_bonus) h+=`<div class="sect"><h3>Set Bonus</h3>${statBars(o.stat_bonus,[["hp","HP"],["pp","PP"],["atk","ATK"],["def","DEF"],["agi","AGI"],["lck","LCK"]],50)}</div>`;
      return h; }
    case "summons": { let h=kv([["Element",`${elDot(o.element)}<span class="tx-${o.element}">${EL_DJINN[o.element]}</span>`],
        ["Combo",o.is_combo?"yes — standby recipe":"no"],
        ["Djinn needed",o.is_combo?esc((o.djinn_recipe||[]).map(r=>`${r.count} ${EL_DJINN[r.element]}`).join(" + ")):o.djinn_required],
        ["Base power",o.damage_power],["+ Max HP",o.damage_hp_mod!=null?(Math.round(o.damage_hp_mod*100))+"% of target":null],
        ["Range",o.range],["Effect",esc(o.effect)]]);
      if(o.acquisition&&o.acquisition.location) h+=`<div class="prose" style="margin-top:8px">Tablet at <b>${esc(o.acquisition.location)}</b>${o.acquisition.found_at?" — "+esc(o.acquisition.found_at):""}</div>`;
      return h; }
    case "classes": { let h=kv([["Class line",esc(o.class_line)],["Dominance group",esc(o.dominance_group)],
        ["Element reqs",esc(fmtVal(o.element_requirements))]]);
      if(o.stat_multiplier) h+=`<div class="sect"><h3>Stat Multipliers</h3>${statBars(o.stat_multiplier,[["hp","HP"],["pp","PP"],["atk","ATK"],["def","DEF"],["agi","AGI"],["lck","LCK"]],200,50)}</div>`;
      const reqs=(o.available_to||[]).map(a=>{ const rs=(a.djinn_requirements||[]).map(r=>`${esc(r.requirement)} <span class="tk">(${esc(r.source)})</span>`).join(" / ");
        return `<div><b>${esc(a.character)}</b>${a.acr!=null?` <span class="tk">acr ${a.acr}</span>`:""}: ${rs||"&mdash;"}</div>`; }).join("");
      if(reqs) h+=`<div class="sect"><h3>Djinn Setup (by adept)</h3><div class="prose">${reqs}</div></div>`;
      return h; }
    case "psynergy": return kv([["Element",`${elDot(o.element)}<span class="tx-${o.element}">${esc(o.element)}</span>`],
        ["PP cost",o.pp_cost],["Range",esc(o.range)],["Tier / series",`${o.tier!=null?o.tier:"?"}${o.series?" · "+esc(o.series):""}`]])
        + (o.description?`<div class="prose" style="margin-top:8px">${esc(o.description)}</div>`:"");
    case "equipment": { const flags=[o.is_artifact?"artifact":"",o.is_cursed?"cursed":"",o.is_rusty?"rusty (forge)":"",o.increases_critical?"crit+":""].filter(Boolean).join(", ");
      let h=kv([["Type",`${esc(o.category)} · ${esc(o.type)}`],["Flags",esc(flags)||"none"],
        ["Buy / Sell",`${o.buy_price!=null?o.buy_price:"—"} / ${o.sell_price!=null?o.sell_price:"—"}`],
        ["Forged from",esc((o.forged_from||[]).join(", "))]]);
      if(o.stat_bonus) h+=`<div class="sect"><h3>Stat Bonus</h3>${statBars(o.stat_bonus,[["atk","ATK"],["def","DEF"],["hp","HP"],["pp","PP"],["agi","AGI"],["lck","LCK"]],150)}</div>`;
      const ep=elementGrid(o.elemental_power); if(ep) h+=`<div class="sect"><h3>Elemental Power</h3>${ep}</div>`;
      if(o.unleash) h+=`<div class="sect"><h3>Unleash</h3><div class="prose">${o.unleash.element?elDot(o.unleash.element):""}<b>${esc(o.unleash.name)}</b>${o.unleash.power_level?" — "+esc(o.unleash.power_level)+" power":""}${o.unleash.rate?", "+esc(o.unleash.rate)+" rate":""}</div></div>`;
      if(o.use_effect) h+=`<div class="sect"><h3>Use</h3><div class="prose">${esc(fmtVal(o.use_effect))}</div></div>`;
      if(o.effects&&o.effects.length) h+=`<div class="sect"><h3>Effects</h3><div class="prose">${esc(o.effects.join(", "))}</div></div>`;
      return h; }
    case "items": return kv([["Type",esc(o.item_type)],["Effect",esc(o.effect)],["Usable in battle",o.usable_in_battle?"yes":"no"],
        ["Buy / Sell",`${o.buy_price!=null?o.buy_price:"—"} / ${o.sell_price!=null?o.sell_price:"—"}`]]);
    case "shops": return kv([["Town / location",esc(o.location||o.name)],["Availability",esc(o.availability_notes)||"always open"],["Stock size",(o.stock||[]).length]]);
    case "monsters": { let h=kv([["Variant",esc(o.variant)],["Boss form",o.is_boss?"yes":"no"],["Djinn enemy",o.is_djinn_enemy?"yes":"no"]]);
      if(o.stats) h+=`<div class="sect"><h3>Stats</h3>${statBars(o.stats,[["hp","HP"],["pp","PP"],["atk","ATK"],["def","DEF"],["agi","AGI"],["lck","LCK"]],Math.max(100,(o.stats.hp||100)))}</div>`;
      const er=elementGrid(o.elemental_resistance); if(er) h+=`<div class="sect"><h3>Elemental Resistance</h3>${er}</div>`;
      const ab=(o.abilities||[]).map(a=>esc(a.name||a)).join(", "); if(ab) h+=`<div class="sect"><h3>Abilities</h3><div class="prose">${ab}</div></div>`;
      const dr=(o.drops||{}); h+=`<div class="prose" style="margin-top:8px">EXP ${dr.exp!=null?dr.exp:"?"} · ${dr.coins!=null?dr.coins:"?"} coins</div>`;
      return h; }
    case "bosses": { let h=kv([["Optional",o.is_optional?"yes":"no"],["Superboss",o.is_superboss?"yes":"no"],
        ["Weakness",(o.weakness||[]).map(w=>`${elDot(w)}${w}`).join(" ")||"none"],["Rec. level",o.recommended_level]]);
      const enc=(o.encounters||[]).map(e=>{ const s=e.stats||{}; return `<div><b>${esc(e.location)}</b> — HP ${s.hp!=null?s.hp:"?"}, ATK ${s.atk!=null?s.atk:"?"}, DEF ${s.def!=null?s.def:"?"}</div>`; }).join("");
      if(enc) h+=`<div class="sect"><h3>Encounters</h3><div class="prose">${enc}</div></div>`;
      if(o.special_mechanics&&o.special_mechanics.length) h+=`<div class="sect"><h3>Mechanics</h3><div class="prose">${esc(o.special_mechanics.join("; "))}</div></div>`;
      if(o.strategy) h+=`<div class="sect"><h3>Strategy</h3><div class="prose">${esc(o.strategy)}</div></div>`;
      if(o.special_notes) h+=`<div class="prose" style="margin-top:8px"><i>${esc(o.special_notes)}</i></div>`;
      return h; }
    case "locations": { let h=kv([["Order",o.order],["Kind",esc(o.kind)],["Has shop",o.shop?"yes":"no"]]);
      if((o.pickups||[]).length) h+=`<div class="sect"><h3>Pickups</h3><div class="prose">${esc(o.pickups.join(", "))}</div></div>`;
      return h; }
    case "characters": { let h=kv([["Element",`${elDot(o.element)}<span class="tx-${o.element}">${EL_DJINN[o.element]} Adept</span>`],
        ["JP name",esc(o.jp_name)],["Starter",o.is_starter?"yes":"no"],["Hometown",esc(o.hometown)],
        ["Joins",esc(o.join)]]);
      if(o.can_equip&&o.can_equip.length) h+=`<div class="sect"><h3>Can Equip</h3><div class="prose">${esc(o.can_equip.join(", "))}</div></div>`;
      return h; }
  }
  return "";
}

/* ---------------- per-type cross-links ---------------- */
function linksHTML(type,o){
  const g=[];
  switch(type){
    case "djinn":
      g.push(linkGroup("Battle form (monster)", refsFromList("monsters", rev.djinnToMonster[o.id]||[])));
      g.push(linkGroup("Found in", refsFromList("locations", locFor("djinn",o.id))));
      g.push(linkGroup("Fuels summons (same element)", refsFromList("summons", summonsByElement(o.element))));
      break;
    case "summons":
      g.push(linkGroup("Powered by Djinn (same element)", refsFromList("djinn", djinnByElement(o.element))));
      if(o.is_combo&&o.acquisition&&o.acquisition.location) g.push(linkGroup("Tablet location", refsFromList("locations", locFor("summons",o.id))));
      break;
    case "classes":
      g.push(linkGroup("Grants Psynergy", refsFromList("psynergy", (o.psynergy||[]).map(p=>p.id))));
      g.push(linkGroup("Available to", refsFromList("characters", (o.available_to||[]).map(a=>a.character_id))));
      g.push(linkGroup("Same class line", refsFromList("classes", (DB.classes||[]).filter(c=>c.class_line===o.class_line&&c.id!==o.id).map(c=>c.id))));
      break;
    case "psynergy":
      g.push(linkGroup("Granted by classes", refsFromList("classes", rev.psyToClasses[o.id]||[])));
      if(o.series) g.push(linkGroup("Series", refsFromList("psynergy", (DB.psynergy||[]).filter(p=>p.series===o.series&&p.id!==o.id).map(p=>p.id))));
      break;
    case "equipment":
      g.push(linkGroup("Equippable by", refsFromList("characters", (o.equippable_by||[]).map(n=>{const c=charByName[n];return c&&c.id;}))));
      g.push(linkGroup("Sold at", refsFromList("shops", rev.gearToShops["equipment:"+o.id]||[])));
      g.push(linkGroup("Dropped by", refsFromList("monsters", rev.gearToMonsters["equipment:"+o.id]||[])));
      g.push(linkGroup("Forged from", refsFromList("items", (o.forged_from||[]).map(n=>{const it=itemByName[(n||"").toLowerCase()];return it&&it.id;}))));
      g.push(linkGroup("Found in", refsFromList("locations", locFor("equipment",o.id))));
      break;
    case "items":
      g.push(linkGroup("Sold at", refsFromList("shops", rev.gearToShops["item:"+o.id]||[])));
      g.push(linkGroup("Dropped by", refsFromList("monsters", rev.gearToMonsters["item:"+o.id]||[])));
      g.push(linkGroup("Forged into", refsFromList("equipment", rev.matToEquip[o.id]||[])));
      g.push(linkGroup("Found in", refsFromList("locations", locFor("item",o.id))));
      break;
    case "shops":
      g.push(linkGroup("Stock", refsFromList("equipment", (o.stock||[]).filter(s=>s.ref_type==="equipment").map(s=>s.ref_id)) + refsFromList("items", (o.stock||[]).filter(s=>s.ref_type==="item").map(s=>s.ref_id))));
      break;
    case "monsters":
      if(o.djinn_id) g.push(linkGroup("Is Djinni", refsFromList("djinn",[o.djinn_id])));
      if(o.boss_id) g.push(linkGroup("Is Boss", refsFromList("bosses",[o.boss_id])));
      g.push(linkGroup("Drops", refsFromList("equipment", ((o.drops||{}).items||[]).filter(d=>d.ref_type==="equipment").map(d=>d.ref_id)) + refsFromList("items", ((o.drops||{}).items||[]).filter(d=>d.ref_type==="item").map(d=>d.ref_id))));
      g.push(linkGroup("Found in", refsFromList("locations", locFor("monsters",o.id))));
      break;
    case "bosses":
      g.push(linkGroup("Battle stat-line (monster)", refsFromList("monsters", rev.bossToMonster[o.id]||[])));
      g.push(linkGroup("Fought in", refsFromList("locations", locFor("bosses",o.id))));
      break;
    case "locations": {
      const rec=LR.regions[o.id]||{};
      g.push(linkGroup("Connects to", refsFromList("locations", rec.connections||[])));
      g.push(linkGroup("Djinn", refsFromList("djinn", rec.djinn||[])));
      g.push(linkGroup("Summon tablets", refsFromList("summons", rec.summons||[])));
      g.push(linkGroup("Bosses", refsFromList("bosses", rec.bosses||[])));
      g.push(linkGroup("Monsters", refsFromList("monsters", rec.monsters||[])));
      const eq=(rec.pickups||[]).filter(p=>p.ref_type==="equipment").map(p=>p.ref_id);
      const it=(rec.pickups||[]).filter(p=>p.ref_type==="item").map(p=>p.ref_id);
      g.push(linkGroup("Pickups", refsFromList("equipment", eq) + refsFromList("items", it)));
      break; }
    case "characters":
      g.push(linkGroup("Classes", refsFromList("classes", rev.charToClasses[o.id]||[])));
      g.push(linkGroup("Equippable equipment", refsFromList("equipment", rev.charToEquip[o.id]||[])));
      break;
  }
  const body=g.filter(Boolean).join("");
  return body ? `<div class="sect"><h3>Links</h3>${body}</div>` : "";
}

/* ---------------- provenance (source inspector) ---------------- */
function provHTML(o){
  let h="";
  if(o.conflicts&&((Array.isArray(o.conflicts)&&o.conflicts.length)||(!Array.isArray(o.conflicts)&&Object.keys(o.conflicts).length)))
    h+=`<div class="conflict"><b>⚠ Cross-source conflict:</b> ${esc(fmtVal(o.conflicts))}</div>`;
  if(o.name_variants&&o.name_variants.length) h+=`<div class="variants"><b>Also known as:</b> ${esc(o.name_variants.join(", "))}${o.name_literal&&o.name_literal!==o.name?` · literal: ${esc(o.name_literal)}`:""}</div>`;
  if(o.sources&&o.sources.length) h+=`<div class="prose" style="margin-top:6px">Attested by ${o.sources.length} source${o.sources.length===1?"":"s"}: ${esc(o.sources.join(", "))}</div>`;
  return h ? `<div class="sect"><h3>Provenance</h3>${h}</div>` : "";
}

/* ---------------- hover tooltip ---------------- */
function tipHTML(type,o){
  const el=entEl(type,o); let rows=[];
  switch(type){
    case "djinn": rows=[["Element",EL_DJINN[o.element]],["Effect",fmtVal(o.battle_effect)||"stat only"],["Found",(o.location||{}).area]]; break;
    case "summons": rows=[["Element",EL_DJINN[o.element]],["Needs",o.is_combo?(o.djinn_recipe||[]).map(r=>r.count+" "+EL_DJINN[r.element]).join("+"):o.djinn_required+" "+EL_DJINN[o.element]],["Power",o.damage_power]]; break;
    case "classes": rows=[["Line",o.class_line],["HP×",(o.stat_multiplier||{}).hp],["ATK×",(o.stat_multiplier||{}).atk],["Psynergy",(o.psynergy||[]).length]]; break;
    case "psynergy": rows=[["Element",o.element],["PP",o.pp_cost],["Range",o.range],["Tier",o.tier]]; break;
    case "equipment": rows=[["Type",o.type],["ATK+",(o.stat_bonus||{}).atk],["DEF+",(o.stat_bonus||{}).def],["Unleash",o.unleash&&o.unleash.name],["Buy",o.buy_price]]; break;
    case "items": rows=[["Type",o.item_type],["Effect",o.effect],["Buy",o.buy_price]]; break;
    case "shops": rows=[["Location",o.location],["Stock",(o.stock||[]).length]]; break;
    case "monsters": rows=[["HP",(o.stats||{}).hp],["ATK",(o.stats||{}).atk],["EXP",(o.drops||{}).exp]]; break;
    case "bosses": { const s=((o.encounters||[])[0]||{}).stats||{}; rows=[["HP",s.hp],["Weak",(o.weakness||[]).join(", ")],["Rec. Lv",o.recommended_level]]; break; }
    case "locations": rows=[["Order",o.order],["Kind",o.kind],["Shop",o.shop?"yes":"no"]]; break;
    case "characters": rows=[["Adept",EL_DJINN[o.element]],["Home",o.hometown],["Starter",o.is_starter?"yes":"no"]]; break;
  }
  const body=rows.filter(r=>r[1]!=null&&r[1]!=="").map(r=>`<div><span class="tk">${r[0]}:</span> ${esc(fmtVal(r[1]))}</div>`).join("");
  return `<div class="tt">${el?elDot(el):""}${esc(o.qualified_name||o.name)}</div><div class="ttype">${TYPE_LABEL[type]}</div>${body}`;
}
const tip=document.getElementById("tip");
function showTip(type,id,x,y){ const o=byId[type]&&byId[type][id]; if(!o){hideTip();return;}
  tip.innerHTML=tipHTML(type,o); tip.style.display="block";
  const w=tip.offsetWidth,h=tip.offsetHeight; let nx=x+16,ny=y+16;
  if(nx+w>innerWidth-8) nx=x-w-16; if(ny+h>innerHeight-8) ny=innerHeight-h-8;
  tip.style.left=nx+"px"; tip.style.top=ny+"px"; }
function hideTip(){ tip.style.display="none"; }
document.addEventListener("mouseover",e=>{ const r=e.target.closest("[data-type][data-id]"); if(r) showTip(r.dataset.type,r.dataset.id,e.clientX,e.clientY); });
document.addEventListener("mousemove",e=>{ if(tip.style.display==="block"){ const r=e.target.closest("[data-type][data-id]"); if(!r){hideTip();return;} showTip(r.dataset.type,r.dataset.id,e.clientX,e.clientY);} });
document.addEventListener("mouseout",e=>{ const r=e.target.closest("[data-type][data-id]"); if(r) hideTip(); });

/* ---------------- wiki controller ---------------- */
let curType="locations", curId=null, search="", facetState={};
function facetVals(f,o){ const v=f.get(o); return v==null?[]:(Array.isArray(v)?v:[v]); }
function matchesFacets(type,o,except){ const fs=FACETS[type]||[];
  for(const f of fs){ if(f.key===except) continue; const sel=facetState[f.key]; if(!sel||!sel.size) continue;
    if(!facetVals(f,o).some(v=>sel.has(String(v)))) return false; }
  return true; }
function prettyFacet(v){ return String(v).replace(/[-_]/g," ").replace(/\b\w/g,c=>c.toUpperCase()); }
function renderFacets(){ const bar=document.getElementById("facets");
  if(curType==="__all__"||!FACETS[curType]){ bar.innerHTML=""; return; }
  const base=(DB[curType]||[]).filter(matchesSearch);
  bar.innerHTML=FACETS[curType].map(f=>{
    const counts={}; base.forEach(o=>{ if(!matchesFacets(curType,o,f.key)) return; facetVals(f,o).forEach(v=>{v=String(v); counts[v]=(counts[v]||0)+1;}); });
    let vals=Object.keys(counts); if(!vals.length) return "";
    if(f.key==="element") vals.sort((a,b)=>EL_ORDER.indexOf(a)-EL_ORDER.indexOf(b)); else vals.sort();
    const sel=facetState[f.key]||new Set();
    const chips=vals.map(v=>`<span class="facet ${sel.has(v)?'on':''}" data-fk="${esc(f.key)}" data-fv="${esc(v)}">${f.key==="element"?elDot(v):""}${esc(prettyFacet(v))}<span class="fc">${counts[v]}</span></span>`).join("");
    return `<div class="facetgrp"><span class="flabel">${esc(f.label)}</span>${chips}</div>`;
  }).filter(Boolean).join(""); }
function resetFacets(){ facetState={}; }
function renderDetail(){
  const d=document.getElementById("detail");
  if(!curId || !byId[curType] || !byId[curType][curId]){ d.innerHTML='<div class="placeholder">Pick an entity, or click any linked chip to walk the graph. Hover a chip for a quick peek.</div>'; return; }
  const o=byId[curType][curId]; const el=entEl(curType,o);
  const gs1 = o.game==="gs1" ? `<span class="gs1tag" title="first appeared in Golden Sun 1 (transferred / shared)">from GS1</span>` : "";
  d.innerHTML = `<h2>${el?elDot(el):""}${esc(o.qualified_name||o.name)}</h2>`
    + `<div class="subline"><span class="badge t-${curType}">${TYPE_LABEL[curType]}</span>${gs1}`
    + (o.sources&&o.sources.length?`<span class="srcpill" title="${esc(o.sources.join(', '))}">ⓢ ${o.sources.length} source${o.sources.length===1?"":"s"}</span>`:"")
    + `</div>`
    + `<div class="sect">${coreHTML(curType,o)}</div>`
    + linksHTML(curType,o)
    + provHTML(o);
  d.scrollTop=0;
}
function matchesSearch(o){ if(!search) return true; const s=search.toLowerCase();
  return (o.name||"").toLowerCase().includes(s) || (o.qualified_name||"").toLowerCase().includes(s) || (o.id||"").toLowerCase().includes(s)
    || (o.name_variants||[]).some(v=>v.toLowerCase().includes(s)); }
function renderList(){
  const rows=[]; const types = curType==="__all__" ? TYPES : [curType]; let n=0;
  types.forEach(t => (DB[t]||[]).filter(o=>matchesSearch(o)&&matchesFacets(t,o)).forEach(o => { n++;
    const el=entEl(t,o);
    rows.push(`<div class="lrow ${t===curType&&o.id===curId?"sel":""}" data-type="${t}" data-id="${esc(o.id)}">${el?elDot(el):""}<span class="lname">${esc(o.qualified_name||o.name)}</span><span class="lmeta"><span class="badge t-${t}">${TYPE_LABEL[t]}</span></span></div>`);
  }));
  document.getElementById("list").innerHTML = rows.join("") || '<div class="listcount">no matches</div>';
  document.getElementById("listcount").textContent = `${n} ${curType==="__all__"?"entities":(TYPE_LABEL[curType]||curType).toLowerCase()+(n===1?"":"s")}`;
}
function openEntity(type,id){ curType=type; curId=id; resetFacets();
  [...document.getElementById("typechips").children].forEach(x=>x.classList.toggle("on",x.dataset.t===curType));
  renderFacets(); renderList(); renderDetail(); }

const chipbar=document.getElementById("typechips");
chipbar.innerHTML = [["__all__","All"]].concat(TYPES.map(t=>[t,(TYPE_LABEL[t]||t)+"s"]))
  .map(([t,l])=>`<span class="fchip ${t===curType?"on":""}" data-t="${t}">${l}</span>`).join("");
chipbar.addEventListener("click",e=>{ const c=e.target.closest(".fchip"); if(!c) return;
  curType=c.dataset.t; resetFacets(); [...chipbar.children].forEach(x=>x.classList.toggle("on",x.dataset.t===curType)); renderFacets(); renderList(); });
document.getElementById("facets").addEventListener("click",e=>{ const c=e.target.closest(".facet"); if(!c) return;
  const k=c.dataset.fk,v=c.dataset.fv; const set=facetState[k]||(facetState[k]=new Set());
  set.has(v)?set.delete(v):set.add(v); renderFacets(); renderList(); });
document.getElementById("search").addEventListener("input",e=>{ search=e.target.value.trim(); renderFacets(); renderList(); });
document.getElementById("list").addEventListener("click",e=>{ const r=e.target.closest(".lrow"); if(!r) return;
  curType=r.dataset.type; curId=r.dataset.id; renderList(); renderDetail(); });
document.getElementById("detail").addEventListener("click",e=>{
  const more=e.target.closest(".refmore"); if(more){ const p=more.parentElement; p.querySelectorAll(".refhidden").forEach(s=>s.removeAttribute("hidden")); more.remove(); return; }
  const r=e.target.closest(".ref[data-id]"); if(!r) return; hideTip(); openEntity(r.dataset.type,r.dataset.id); });

renderFacets(); renderList(); renderDetail();

/* ================= BUILD PLANNER ==========================================
   Ported from gs1 build_codex.py. Same mechanic (Set-Djinn distribution by
   element -> class/stats/Psynergy), adapted to gs2 data shapes:
     * requirement rows live in available_to[].djinn_requirements[].parsed;
       telago rows are RANGES {element,count_min,count_max}; ultimalink rows are
       EXACT points {element,count}. We OR-combine both sources (a counts vector
       matches a class if ANY row is satisfied) and pick the tightest row.
     * pseudo-element "other" = "each non-native element" (Trickster lines:
       Harlequin/Acrobat...) -> expanded to all 3 off-native elements.
     * native-element fallback: any element a row does NOT name must be 0
       (unless it's the adept's native element, which is always free) — neither
       gs2 source names all 4 elements, so this disambiguates like gs1's legacy rows.
     * 8 adepts (TLA merges both parties) share ONE 72-Djinn pool (18/element). */
const CLASSES=DB.classes||[];
const NATIVE={}; (DB.characters||[]).forEach(c=>{ if(c.element) NATIVE[c.name]=c.element; });
const PARTY=(DB.characters||[]).filter(c=>c.element);

/* ----- progression-aware pool ----- */
const REGION_ORDER={};
(DB.locations||[]).forEach(l=>{ REGION_ORDER[l.region_id]=l.order; });
/* The 28 area==null Djinn are the GS1 set (game="gs1"); they arrive when Isaac's party
   rejoins at Contigo, NOT at the start. Anchor them to that reunion order (no TLA
   location.area exists for them, so the reunion is the most precise we can be). */
const GS1_DJINN_ORDER=(REGION_ORDER["contigo"]!=null?REGION_ORDER["contigo"]:49);
function djinnRegionOrder(d){
  const loc=d.location; if(!loc||loc.area==null) return GS1_DJINN_ORDER;   // GS1-transferred set: rejoin at Contigo
  const areas=Array.isArray(loc.area)?loc.area:[loc.area];
  const orders=areas.map(a=>REGION_ORDER[a]).filter(o=>o!=null);
  return orders.length?Math.min(...orders):GS1_DJINN_ORDER; }
let progressIndex=null;   // null = full game; number = region.order ceiling
function availableDjinnPool(){
  const pool={earth:0,fire:0,wind:0,water:0};
  (DB.djinn||[]).forEach(d=>{ if(pool[d.element]==null) return;
    if(progressIndex!=null&&djinnRegionOrder(d)>progressIndex) return;
    pool[d.element]++; });
  return pool; }
let POOL_MAX=availableDjinnPool();
function rebuildPool(){ POOL_MAX=availableDjinnPool(); renderAll(); updatePoolHint(); }

/* ----- matcher ----- */
function expandRow(parsed,native){ const out=[];
  for(const p of parsed){ const mn=(p.count_min!=null?p.count_min:p.count), mx=(p.count_max!=null?p.count_max:p.count);
    if(p.element==="other"){ for(const el of ELEMS) if(el!==native) out.push({element:el,min:mn,max:mx}); }
    else if(ELEMS.includes(p.element)) out.push({element:p.element,min:mn,max:mx}); }
  return out; }
function classRows(av,native){ const out=[];
  for(const r of av.djinn_requirements||[]){ if(!r.parsed||!r.parsed.length) continue;
    if(r.source==="telago"||r.source==="ultimalink"){ const ex=expandRow(r.parsed,native); if(ex.length) out.push(ex); } }
  return out; }
function rowSatisfies(parsed,counts,native){ const named={};
  for(const p of parsed){ if(counts[p.element]<p.min||counts[p.element]>p.max) return false; named[p.element]=true; }
  for(const el of ELEMS){ if(el===native||named[el]) continue; if(counts[el]>0) return false; } return true; }
function rowWidth(parsed){ return parsed.reduce((s,p)=>s+(p.max-p.min),0); }
function matchClasses(charName,counts){ const native=NATIVE[charName]; const out=[];
  for(const c of CLASSES){ const av=(c.available_to||[]).find(a=>a.character===charName); if(!av) continue;
    let best=null; for(const parsed of classRows(av,native)){ if(rowSatisfies(parsed,counts,native)){ const w=rowWidth(parsed); if(best===null||w<best) best=w; } }
    if(best!==null) out.push({cls:c,av,width:best}); }
  out.sort((a,b)=>a.width-b.width); return out; }
// reverse: prefer an ultimalink EXACT build (a concrete point); fall back to the first range row's mins.
function reverseCounts(av,native){
  const ulti=(av.djinn_requirements||[]).filter(r=>r.source==="ultimalink"&&r.parsed&&r.parsed.length);
  const src = ulti.length ? expandRow(ulti[ulti.length-1].parsed,native) : (classRows(av,native)[0]||null);
  const c={earth:0,fire:0,wind:0,water:0}; if(src) for(const p of src) c[p.element]=Math.max(c[p.element],p.min); return c; }

/* ----- shared-pool state + rendering ----- */
const psyById=byId.psynergy||{};
const pstate={}; PARTY.forEach(c=>pstate[c.name]={earth:0,fire:0,wind:0,water:0});
function poolUsed(){ const u={earth:0,fire:0,wind:0,water:0}; PARTY.forEach(c=>ELEMS.forEach(el=>u[el]+=pstate[c.name][el])); return u; }
function renderPool(used){
  const html=`<span class="ptitle">Djinn Pool</span>`+ELEMS.map(el=>{ const u=used[el],m=POOL_MAX[el]; const over=u>m;
    const pct=Math.max(0,Math.min(100,m?(u/m)*100:0));
    return `<div class="poolel">${elDot(el)}<span class="pn tx-${el}">${EL_DJINN[el]}</span>
      <div class="poolwrap"><div class="pfill" style="width:${pct}%;background:var(--${el})"></div></div>
      <span class="pcount ${over?'over':''}">${u} / ${m}</span></div>`; }).join("");
  document.getElementById("poolbar").innerHTML=html; }
function pStatBars(sm){ if(!sm) return '<div class="psy empty" style="margin-top:10px">No stat multipliers in source.</div>';
  return `<div class="statgrid" style="margin-top:10px">`+[["hp","HP"],["pp","PP"],["atk","ATK"],["def","DEF"],["agi","AGI"],["lck","LCK"]].map(([k,l])=>{
    const v=sm[k]; if(v==null) return ""; const pct=Math.max(0,Math.min(100,(v/200)*100)); const cls=v>100?"high":(v<100?"low":"");
    return `<div class="sn">${l}</div><div class="barwrap"><div class="bar ${cls}" style="width:${pct}%"></div><div class="base" style="left:50%"></div></div><div class="sv">${v}%</div>`;
  }).join("")+`</div>`; }
function pPsyList(cls){ const ps=cls.psynergy||[]; if(!ps.length) return '<div class="empty">None.</div>';
  return "<ul>"+ps.map(x=>{ const p=psyById[x.id]||{}; const el=p.element||"none"; const pp=p.pp_cost!=null?p.pp_cost+" PP":"";
    return `<li data-pid="${esc(x.id)}">${elDot(el)}<span class="pn">${esc(x.name||p.name||x.id)}</span><span class="pp">${pp}</span></li>`; }).join("")+"</ul>"; }
function renderResult(name){ const counts=pstate[name]; const matches=matchClasses(name,counts); const box=document.getElementById("res-"+name);
  if(!matches.length){ box.innerHTML='<div class="none">No class in the data matches this Djinn mix.</div>'; return; }
  const c=matches[0].cls; const lineTip=c.class_line&&c.class_line!==c.id?` &middot; ${esc(c.class_line)} line`:"";
  let h=`<div class="classname" data-cid="${esc(c.id)}">${esc(c.qualified_name||c.name)}</div><div class="meta">${esc(c.dominance_group||"")}${lineTip}</div>`;
  if(matches.length>1) h+=`<div class="multi">Also valid: `+matches.slice(1,6).map(m=>`<span class="alt" data-c="${esc(name)}" data-id="${esc(m.cls.id)}">${esc(m.cls.qualified_name||m.cls.name)}</span>`).join(", ")+`</div>`;
  h+=pStatBars(c.stat_multiplier)+`<div class="psy"><h3>Psynergy &middot; ${(c.psynergy||[]).length}</h3>${pPsyList(c)}</div>`;
  box.innerHTML=h; }
function renderCard(name,used){ used=used||poolUsed(); const counts=pstate[name]; const total=ELEMS.reduce((s,e)=>s+counts[e],0);
  ELEMS.forEach(el=>{ document.getElementById(`pval-${name}-${el}`).textContent=counts[el];
    document.getElementById(`pinc-${name}-${el}`).disabled=used[el]>=POOL_MAX[el];
    document.getElementById(`pdec-${name}-${el}`).disabled=counts[el]<=0; });
  document.getElementById("ptot-"+name).textContent=`Set: ${total} Djinn`; renderResult(name); }
function renderAll(){ const used=poolUsed(); renderPool(used); PARTY.forEach(c=>renderCard(c.name,used)); }
function setCounts(name,counts){ pstate[name]=Object.assign({earth:0,fire:0,wind:0,water:0},counts); renderAll(); }
function buildCard(c){ const native=c.element;
  const reachable=CLASSES.filter(cl=>(cl.available_to||[]).some(a=>a.character===c.name&&classRows(a,native).length))
    .map(cl=>({id:cl.id,label:cl.qualified_name||cl.name})).sort((a,b)=>a.label.localeCompare(b.label));
  const steppers=ELEMS.map(el=>{ const isN=el===native; return `<div class="stepper">
    <span class="lbl ${isN?'native':''}">${elDot(el)}<span class="nm tx-${el}">${EL_DJINN[el]}</span>${isN?' &#9733;':''}</span>
    <span class="ctrls"><button id="pdec-${c.name}-${el}" data-c="${esc(c.name)}" data-el="${el}" data-d="-1">&minus;</button>
    <span class="val" id="pval-${c.name}-${el}">0</span><button id="pinc-${c.name}-${el}" data-c="${esc(c.name)}" data-el="${el}" data-d="1">+</button></span></div>`; }).join("");
  const opts=`<option value="">&mdash; set Djinn for a target class &mdash;</option>`+reachable.map(r=>`<option value="${esc(r.id)}">${esc(r.label)}</option>`).join("");
  return `<div class="charcard" style="border-top-color:var(--${native})"><h2>${elDot(native)}${esc(c.name)}</h2>
    <div class="nativetag tx-${native}">${EL_DJINN[native]} Adept</div>${steppers}
    <div class="totalrow"><span id="ptot-${esc(c.name)}"></span><span class="reset" data-c="${esc(c.name)}">reset</span></div>
    <div class="reverse"><select id="prev-${esc(c.name)}" data-c="${esc(c.name)}">${opts}</select></div>
    <div class="result" id="res-${esc(c.name)}"></div></div>`; }
const pgrid=document.getElementById("pgrid"); pgrid.innerHTML=PARTY.map(buildCard).join("");
pgrid.addEventListener("click",e=>{
  const btn=e.target.closest("button[data-d]"); if(btn){ const {c,el,d}=btn.dataset; const counts=pstate[c]; const used=poolUsed();
    const nv=counts[el]+(+d); if(nv<0) return; if(+d>0&&used[el]>=POOL_MAX[el]) return; counts[el]=nv; renderAll(); return; }
  const rs=e.target.closest(".reset[data-c]"); if(rs){ setCounts(rs.dataset.c,{}); document.getElementById("prev-"+rs.dataset.c).value=""; return; }
  const alt=e.target.closest(".alt[data-id]"); if(alt){ const cl=CLASSES.find(x=>x.id===alt.dataset.id); if(!cl) return; const av=cl.available_to.find(a=>a.character===alt.dataset.c); setCounts(alt.dataset.c,reverseCounts(av,NATIVE[alt.dataset.c])); return; }
  const cn=e.target.closest(".classname[data-cid]"); if(cn){ document.getElementById("navbtn-wiki").click(); openEntity("classes",cn.dataset.cid); return; }
  const li=e.target.closest("li[data-pid]"); if(li){ document.getElementById("navbtn-wiki").click(); openEntity("psynergy",li.dataset.pid); return; }
});
pgrid.addEventListener("change",e=>{ const sel=e.target.closest("select[data-c]"); if(!sel||!sel.value) return;
  const cl=CLASSES.find(x=>x.id===sel.value); if(!cl) return; const av=cl.available_to.find(a=>a.character===sel.dataset.c); setCounts(sel.dataset.c,reverseCounts(av,NATIVE[sel.dataset.c])); });
renderAll();

/* ----- shared progress anchor (one selector drives BOTH the planner pool gate and the tracker) ----- */
const PROGRESS_LISTENERS=[];
function onProgressChange(fn){ PROGRESS_LISTENERS.push(fn); }
function setProgress(idx){ progressIndex=idx;
  document.querySelectorAll(".progress-sel").forEach(s=>{ s.value=idx==null?"":String(idx); });
  PROGRESS_LISTENERS.forEach(fn=>fn()); }
function fillRegionSelect(sel){
  (DB.locations||[]).slice().sort((a,b)=>a.order-b.order).forEach(l=>{
    const o=document.createElement("option"); o.value=l.order;
    o.textContent=`#${String(l.order+1).padStart(2,"0")} – ${l.name}`; sel.appendChild(o); });
  sel.classList.add("progress-sel");
  sel.addEventListener("change",()=>setProgress(sel.value===""?null:+sel.value)); }
fillRegionSelect(document.getElementById("region-sel"));
function updatePoolHint(){ const p=POOL_MAX; const t=p.earth+p.fire+p.wind+p.water;
  document.getElementById("pool-hint").textContent=progressIndex==null?"":`${t} / 72 Djinn available`; }
onProgressChange(()=>{ rebuildPool(); });
updatePoolHint();

/* ===== Collection Tracker (B2) ===== */
const TK_KEY="gs2-codex-collection";
const LOCS=(DB.locations||[]).slice().sort((a,b)=>a.order-b.order);
/* AG (access_gates sidecar): region_id -> {meta, items:{name->gate}} */
const AG_BY_REGION={}; AG.forEach(r=>{ const m={}; (r.gates||[]).forEach(g=>{ if(g.item) m[g.item]=g; });
  AG_BY_REGION[r.region_id]={meta:r,items:m}; });
/* name -> wiki entity id, to make checklist rows clickable into the Wiki */
const tkIdBy={}; ["djinn","summons","psynergy","items","equipment"].forEach(t=>{ tkIdBy[t]={};
  (DB[t]||[]).forEach(e=>{ if(e&&e.name!=null) tkIdBy[t][e.name]=e.id; }); });
function tkRef(kind,name){
  if(kind==="djinn")    return tkIdBy.djinn[name]!=null?["djinn",tkIdBy.djinn[name]]:null;
  if(kind==="summon")   return tkIdBy.summons[name]!=null?["summons",tkIdBy.summons[name]]:null;
  if(kind==="psynergy") return tkIdBy.psynergy[name]!=null?["psynergy",tkIdBy.psynergy[name]]:null;
  if(tkIdBy.items[name]!=null)     return ["items",tkIdBy.items[name]];
  if(tkIdBy.equipment[name]!=null) return ["equipment",tkIdBy.equipment[name]];
  return null; }
/* when a gate's Psynergy / event is satisfied at the current progress, the item is reachable.
   Psynergy order: derived from locations.psynergy_here + a curated map for the utility/class
   Psynergy granted by items or Djinn (not learned in a psynergy_here slot). Event anchors are
   approximate region orders; an unknown event stays "not yet" (conservative). */
const PSY_ACQUIRED_ORDER=(function(){ const m={};
  LOCS.forEach(l=>{ (l.psynergy_here||[]).forEach(p=>{ if(m[p]==null) m[p]=l.order; }); });
  const curated={Lift:46,Hover:47,Carry:51,Force:49,Growth:23,Cyclone:23};
  for(const k in curated) if(m[k]==null) m[k]=curated[k];
  return m; })();
const EVENT_ORDER={"Piers joins party":24,"Piers joins + Black Crystal":42,"Briggs escapes":27,
  "trade Healing Fungus":21,"all 72 Djinn collected":61,"Force Orb (GS1 transfer)":49};
function gateOpen(g){
  if(progressIndex==null) return true;                 // full-game sandbox
  for(const p of (g.requires_psynergy||[])){ const o=PSY_ACQUIRED_ORDER[p]; if(o==null||progressIndex<o) return false; }
  if(g.requires_event){ const o=EVENT_ORDER[g.requires_event]; if(o==null||progressIndex<o) return false; }
  return true; }

let tkCollected=new Set(); try{ tkCollected=new Set(JSON.parse(localStorage.getItem(TK_KEY)||"[]")); }catch(e){}
function tkSave(){ try{ localStorage.setItem(TK_KEY,JSON.stringify([...tkCollected])); }catch(e){} }
function tkKey(rid,kind,name){ return rid+"::"+kind+"::"+name; }
function regionItems(l){ const out=[];
  (l.pickups||[]).forEach(n=>out.push(["item",n]));
  (l.djinn_here||[]).forEach(n=>out.push(["djinn",n]));
  (l.psynergy_here||[]).forEach(n=>out.push(["psynergy",n]));
  (l.summons_here||[]).forEach(n=>out.push(["summon",n]));
  return out; }
const TK_TOTAL=LOCS.reduce((s,l)=>s+regionItems(l).length,0);

function renderReachable(){ const box=document.getElementById("tracker-reachable");
  if(progressIndex==null){ box.innerHTML='<div class="tk-reach empty">Set a Progress gate above to see what has become reachable but is not collected yet.</div>'; return; }
  const pending=[];
  LOCS.forEach(l=>{ const ag=AG_BY_REGION[l.region_id]; if(!ag) return;
    ag.meta.gates.forEach(g=>{ if(!g.item||!gateOpen(g)) return;
      if(tkCollected.has(tkKey(l.region_id,g.kind,g.item))) return; pending.push([l,g]); }); });
  if(!pending.length){ box.innerHTML='<div class="tk-reach empty">Nothing pending &mdash; every reachable gated item is checked off. &#10003;</div>'; return; }
  const lis=pending.map(([l,g])=>`<li><span class="tk-go" data-rid="${esc(l.region_id)}">${esc(g.item)}</span> <span class="tk-where">&mdash; ${esc(l.name)}</span></li>`).join("");
  box.innerHTML=`<div class="tk-reach"><h3>Reachable now, not yet collected &middot; ${pending.length}</h3><ul>${lis}</ul></div>`; }

function rowHTML(rid,kind,name,gate){ const key=tkKey(rid,kind,name); const done=tkCollected.has(key);
  const ref=tkRef(kind,name);
  const nm=ref?`<span class="tk-iname" data-t="${ref[0]}" data-id="${esc(ref[1])}">${esc(name)}</span>`:`<span class="tk-iname">${esc(name)}</span>`;
  let badge="";
  if(gate){ const open=gateOpen(gate);
    const reqs=[...(gate.requires_psynergy||[]),gate.requires_event].filter(Boolean).join(", ");
    badge=open?'<span class="tk-gate open">&#10003; reachable</span>':`<span class="tk-gate">&#128205; ${esc(reqs)}</span>`; }
  return `<div class="tk-row ${done?'done':''}" data-key="${esc(key)}">`+
    `<input type="checkbox" ${done?'checked':''} data-key="${esc(key)}">`+
    `<span class="tk-kind">${esc(kind)}</span>${nm}${badge}</div>`; }

function renderTracker(){ renderReachable();
  const html=LOCS.map(l=>{ const items=regionItems(l); if(!items.length) return "";
    const rid=l.region_id; const ag=AG_BY_REGION[rid];
    const rows=items.map(([kind,name])=>rowHTML(rid,kind,name,ag&&ag.items[name])).join("");
    const unnamed=ag?ag.meta.gates.filter(g=>!g.item):[];
    const note=unnamed.length?`<div class="tk-row" style="color:var(--text-faint);font-size:12px">&#128205; `+
      esc(unnamed.map(g=>(g.requires_psynergy||[]).join("+")+" chest (contents unconfirmed)").join("; "))+`</div>`:"";
    const total=items.length; const done=items.filter(([k,n])=>tkCollected.has(tkKey(rid,k,n))).length;
    const pct=total?Math.round(done/total*100):0;
    const locked=progressIndex!=null&&l.order>progressIndex;
    return `<div class="tk-region ${locked?'locked':''}" data-rid="${esc(rid)}">`+
      `<div class="tk-rhead"><span class="tk-ord">#${String(l.order+1).padStart(2,"0")}</span>`+
      `<span class="tk-name">${esc(l.name)}</span>`+
      `<span class="tk-bar"><span class="tk-fill" style="width:${pct}%"></span></span>`+
      `<span class="tk-count">${done}/${total}</span></div>`+
      `<div class="tk-rbody">${rows}${note}</div></div>`; }).join("");
  document.getElementById("tracker-list").innerHTML=html;
  document.getElementById("tracker-overall").textContent=`${tkCollected.size} / ${TK_TOTAL} collected`; }

function tkUpdateRegion(regEl){ if(!regEl) return; const rows=[...regEl.querySelectorAll(".tk-row[data-key]")];
  const total=rows.length, done=rows.filter(r=>tkCollected.has(r.dataset.key)).length;
  regEl.querySelector(".tk-count").textContent=`${done}/${total}`;
  regEl.querySelector(".tk-fill").style.width=(total?Math.round(done/total*100):0)+"%"; }

document.getElementById("tab-tracker").addEventListener("click",e=>{
  const cb=e.target.closest('input[type=checkbox][data-key]');
  if(cb){ const k=cb.dataset.key; if(cb.checked) tkCollected.add(k); else tkCollected.delete(k); tkSave();
    const row=cb.closest(".tk-row"); if(row) row.classList.toggle("done",cb.checked);
    tkUpdateRegion(cb.closest(".tk-region"));
    document.getElementById("tracker-overall").textContent=`${tkCollected.size} / ${TK_TOTAL} collected`;
    renderReachable(); return; }
  const nm=e.target.closest(".tk-iname[data-t]");
  if(nm){ document.getElementById("navbtn-wiki").click(); openEntity(nm.dataset.t,nm.dataset.id); return; }
  const go=e.target.closest(".tk-go[data-rid]");
  if(go){ const reg=document.querySelector(`.tk-region[data-rid="${go.dataset.rid}"]`);
    if(reg){ reg.classList.add("open"); reg.scrollIntoView({behavior:"smooth",block:"center"}); } return; }
  const hd=e.target.closest(".tk-rhead"); if(hd){ hd.parentElement.classList.toggle("open"); return; } });
document.getElementById("tracker-reset").addEventListener("click",()=>{
  if(confirm("Clear all collection checkmarks?")){ tkCollected.clear(); tkSave(); renderTracker(); } });
fillRegionSelect(document.getElementById("tracker-region-sel"));
onProgressChange(renderTracker);
renderTracker();

/* ----- tabs ----- */
document.querySelector("nav").addEventListener("click",e=>{ const b=e.target.closest("button[data-tab]"); if(!b) return; hideTip();
  const tab=b.dataset.tab; document.querySelectorAll("nav button").forEach(x=>x.classList.toggle("active",x===b));
  document.querySelectorAll(".tabpane").forEach(p=>p.classList.toggle("active",p.id==="tab-"+tab)); });
</script>
</body>
</html>
"""


def main():
    db = {name: load(name) for name in ENTITIES}
    # locations.json keys on `region_id`; give it a uniform `id` so the JS index works.
    for loc in db["locations"]:
        loc.setdefault("id", loc.get("region_id"))
    lr = load("location_refs")
    ag = load("access_gates")
    html = (TEMPLATE
            .replace("__DB__", embed(db))
            .replace("__LR__", embed(lr))
            .replace("__AG__", embed(ag)))
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(html):,} bytes)")
    for name in ENTITIES:
        print(f"  {name:12} {len(db[name])}")


if __name__ == "__main__":
    main()
