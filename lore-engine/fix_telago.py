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
        elif k in ('title', 'toc_path', 'parent', 'source_id', 'chapter_no', 'source_lines'):
            if k in ('title', 'toc_path', 'parent'):
                lines.append(f'{k}: "{v}"')
            else:
                lines.append(f"{k}: {v}")
        else:
            lines.append(f"{k}: {v}")
    return "\n".join(lines) + "\n"

def process():
    directory = "raw/gs2/_chapters/telago"
    for filename in sorted(os.listdir(directory)):
        if not filename.endswith(".md"): continue
        
        path = os.path.join(directory, filename)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        fm_str, body = get_frontmatter_and_body(content)
        if not fm_str: continue
        
        fm = {}
        for line in fm_str.strip().split("\n"):
            if ":" in line:
                k, v = line.split(":", 1)
                k = k.strip()
                v = v.strip().strip('"').strip("'")
                if k == 'covers':
                    inner = v.strip("[]")
                    fm[k] = [x.strip() for x in inner.split(",")] if inner else []
                else:
                    fm[k] = v
        
        toc = fm.get('toc_path', '')
        title = fm.get('title', '')
        
        body_lines = [l for l in body.split("\n") if l.strip() and not l.startswith("#") and not l.startswith("---") and not l.startswith("=====")]
        is_header_only = len(body_lines) <= 3
        
        kind = fm.get('kind', 'meta')
        covers = fm.get('covers', [])
        region = fm.get('region', '')
        
        prefix = int(filename.split("-")[0])
        
        if filename == "00-front.md" or is_header_only:
            kind = "meta"
            covers = []
            region = ""
        elif 1 <= prefix <= 23 or 36 <= prefix <= 39:
            # Walkthrough areas
            kind = "prose-walkthrough"
            
            c = set(["locations", "walkthrough"])
            b_lower = body.lower()
            
            if re.search(r'\bdjinn(i)?\b', b_lower):
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
                
            if "password" in b_lower or "transfer" in b_lower:
                c.add("transfer")
                
            covers = sorted(list(c))
            region = fm.get('region') or title
        elif prefix == 24:
            kind = "data-table"
            covers = ["djinn"]
            region = ""
        elif prefix == 25:
            kind = "data-table"
            covers = ["summons"]
            region = ""
        elif prefix == 26:
            kind = "data-table"
            covers = ["classes"]
            region = ""
        elif prefix == 27:
            kind = "data-table"
            covers = ["items"]
            region = ""
        elif 28 <= prefix <= 32 or prefix == 34:
            kind = "data-table"
            covers = ["equipment"]
            region = ""
        elif prefix == 33:
            kind = "data-table"
            covers = ["psynergy"]
            region = ""
        elif prefix == 35:
            kind = "data-table"
            covers = ["monsters"]
            region = ""
        else:
            kind = "meta"
            covers = []
            region = ""
        
        fm['kind'] = kind
        fm['covers'] = covers
        fm['region'] = region
        
        new_fm = dump_frontmatter(fm)
        new_content = "---\n" + new_fm + "---\n" + body
        with open(path, "w", encoding="utf-8", newline='\n') as f:
            f.write(new_content)
        
        print(f"{filename} / {kind} / [{', '.join(covers)}] / {region}")

if __name__ == "__main__":
    process()
