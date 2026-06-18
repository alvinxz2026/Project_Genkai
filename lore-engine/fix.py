import os
import re
import yaml

def get_frontmatter_and_body(content):
    parts = content.split("---\n", 2)
    if len(parts) >= 3:
        return parts[1], parts[2]
    return "", content

def dump_frontmatter(fm_dict):
    lines = []
    for k, v in fm_dict.items():
        if k == 'covers':
            lines.append(f"covers: [{', '.join(v)}]")
        elif k == 'region':
            lines.append(f'region: "{v}"' if v else 'region: ""')
        elif k == 'title' or k == 'toc_path' or k == 'parent':
            lines.append(f'{k}: "{v}"')
        else:
            lines.append(f"{k}: {v}")
    return "\n".join(lines) + "\n"

def process():
    directory = "raw/gs2/_chapters/autocon"
    for filename in sorted(os.listdir(directory)):
        if not filename.endswith(".md"): continue
        
        path = os.path.join(directory, filename)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        fm_str, body = get_frontmatter_and_body(content)
        if not fm_str: continue
        
        # simple parsing of fm
        fm = {}
        for line in fm_str.strip().split("\n"):
            if ":" in line:
                k, v = line.split(":", 1)
                k = k.strip()
                v = v.strip().strip('"').strip("'")
                if k == 'covers':
                    # parse list
                    inner = v.strip("[]")
                    fm[k] = [x.strip() for x in inner.split(",")] if inner else []
                else:
                    fm[k] = v
        
        # Now apply the rules
        
        toc = fm.get('toc_path', '')
        title = fm.get('title', '')
        
        # Count non-empty lines in body
        body_lines = [l for l in body.split("\n") if l.strip() and not l.startswith("#") and not l.startswith("---")]
        is_header_only = len(body_lines) <= 3
        
        kind = fm.get('kind', 'meta')
        covers = fm.get('covers', [])
        region = fm.get('region', '')
        
        if filename == "00-front.md":
            kind = "meta"
            covers = []
            region = ""
        elif is_header_only:
            kind = "meta"
            covers = []
            region = ""
        elif toc.startswith("3") and (" > " not in toc or toc.startswith("3 > ")): # Djinn and Summons
            if "3.6" in toc:
                kind = "data-table"
                covers = ["summons"]
            elif " > " in toc:
                kind = "data-table"
                covers = ["djinn"]
            else:
                kind = "meta"
                covers = []
            region = ""
        elif toc.startswith("4") and (" > " not in toc or toc.startswith("4 > ")): # Psynergy and Classes
            if " > " in toc:
                kind = "data-table"
                covers = ["classes", "psynergy"]
            else:
                kind = "meta"
                covers = []
            region = ""
        elif toc.startswith("5") and (" > " not in toc or toc.startswith("5 > ")): # Transfer Events
            if " > " in toc:
                kind = "prose-walkthrough"
                covers = ["transfer"]
            else:
                kind = "meta"
                covers = []
            region = ""
        elif toc.startswith("6") and (" > " not in toc or toc.startswith("6 > ")): # Sunshine Blacksmith
            if " > " in toc:
                kind = "data-table"
                covers = ["forging"]
            else:
                kind = "meta"
                covers = []
            region = ""
        elif toc.startswith("7") and (" > " not in toc or toc.startswith("7 > ")): # Ultimate Equipment
            if " > " in toc:
                kind = "data-table"
                covers = ["equipment"]
            else:
                kind = "meta"
                covers = []
            region = ""
        elif toc.startswith("8") and (" > " not in toc or toc.startswith("8 > ")): # Boss Strategies
            if " > " in toc:
                kind = "prose-walkthrough"
                covers = ["bosses"]
            else:
                kind = "meta"
                covers = []
            region = ""
        elif any(toc.startswith(x) for x in ["9", "10", "12", "13"]):
            kind = "meta"
            covers = []
            region = ""
        elif toc.startswith("11"): # Bestiary
            if " > " in toc:
                kind = "data-table"
                covers = ["monsters"]
            else:
                kind = "meta"
                covers = []
            region = ""
        elif toc.startswith("1 > ") or toc.startswith("2 > "):
            # Walkthrough areas
            kind = "prose-walkthrough"
            
            # Extract content from body
            c = set(["locations", "walkthrough"])
            b_lower = body.lower()
            
            if "djinni alert" in b_lower or re.search(r'\bdjinn(i)?\b', b_lower):
                c.add("djinn")
                
            if re.search(r'\b(atk \+|def \+|equip |sword|armor|shield|circlet)\b', b_lower):
                c.add("equipment")
                
            if re.search(r'\b(buy |shops?|cost |inn)\b', b_lower):
                c.add("shops")
                
            if re.search(r'\b(boss|hp[: ])\b', b_lower):
                c.add("bosses")
                
            if re.search(r'\b(chest|find |got |item|potion|nut|mint)\b', b_lower):
                c.add("items")
                
            if "summon" in b_lower and "tablet" in b_lower:
                c.add("summons")
                
            if "psynergy" in b_lower or "lapis" in b_lower or "bit" in b_lower or "pebble" in b_lower:
                c.add("psynergy")
                
            if "joins" in b_lower or "party" in b_lower: # basic character logic
                # c.add("characters") # too noisy, omit unless clear. Let's just drop it if uncertain.
                pass
                
            if "password" in b_lower or "transfer" in b_lower:
                c.add("transfer")
                
            covers = sorted(list(c))
            
            # Set region to title
            region = title
        else:
            # fallback
            if "Guide" in title or "Walkthrough" in title:
                kind = "meta"
                covers = []
                region = ""
        
        fm['kind'] = kind
        fm['covers'] = covers
        fm['region'] = region
        
        # write back
        new_fm = dump_frontmatter(fm)
        new_content = "---\n" + new_fm + "---\n" + body
        with open(path, "w", encoding="utf-8", newline='\n') as f:
            f.write(new_content)
        
        # print one line per file
        print(f"{filename} / {kind} / [{', '.join(covers)}] / {region}")

if __name__ == "__main__":
    process()
