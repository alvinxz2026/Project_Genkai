import os
import re

d = r'C:\Users\Nunu\Documents\Project_Genkai\lore-engine\raw\gs2\_chapters\darkslime'
files = sorted([f for f in os.listdir(d) if f.endswith('.md')])

for f in files:
    path = os.path.join(d, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    parts = content.split('---')
    if len(parts) < 3: continue
    
    frontmatter = parts[1]
    body = '---'.join(parts[2:]).strip()
    
    kind = ""
    covers = []
    region = ""
    
    # Defaults and parsing
    title_match = re.search(r'title: "(.*?)"', frontmatter)
    title = title_match.group(1).strip() if title_match else ""

    if f in ["00-front.md", "01-introduction.md", "02-version-history-and-controls.md", "04-walkthrough.md", "27-indexes.md", "34-music-test.md", "35-miscellaneous.md", "36-manual-errors.md", "37-faqs.md", "38-coming-soon.md", "39-non-gameshark-cheats.md", "40-conclusion.md", "41-legal-info-and-credits.md"]:
        kind = "meta"
        covers = []
        region = ""
    elif f == "03-the-story-up-till-now.md":
        kind = "story"
        covers = []
        region = ""
    elif f == "28-character-guide.md":
        # The prompt says: "A pure index/list chapter -> data-table, and covers = ONLY the one entity it lists"
        # Since it lists characters, weapons, alignment -> data-table with [characters]
        kind = "data-table"
        covers = ["characters"]
        region = ""
    elif f == "29-items.md":
        kind = "data-table"
        covers = ["items"]
        region = ""
    elif f == "30-psynergy.md":
        kind = "data-table"
        covers = ["psynergy"]
        region = ""
    elif f == "31-djinn-guide.md":
        kind = "data-table"
        # The prompt says: "a Djinn List -> [djinn], not [characters, classes, items, ...]"
        # However, the chapter specifically says it lists djinn and summons. 
        # I'll stick to ONLY the main entity to strictly follow the hard rule. 
        covers = ["djinn"] 
        region = ""
    elif f == "32-class-guide.md":
        kind = "data-table"
        covers = ["classes"]
        region = ""
    elif f == "33-the-bestiary.md":
        kind = "data-table"
        covers = ["monsters", "bosses"]
        region = ""
    else:
        # prose-walkthrough
        kind = "prose-walkthrough"
        covers = ["locations", "walkthrough"]
        region = title
        
        # simple heuristic
        b_lower = body.lower()
        
        # Check items
        if "chest" in b_lower or "found" in b_lower or "got " in b_lower or "item:" in b_lower:
            covers.append("items")
        # Check equipment
        if "weapon" in b_lower or "armor" in b_lower or "equip" in b_lower or "sword" in b_lower or "shield" in b_lower or "vest" in b_lower or "axe" in b_lower:
            covers.append("equipment")
        # Check djinn
        if "djinni" in b_lower or "djinn" in b_lower:
            covers.append("djinn")
        # Check summons
        if "summon" in b_lower or "tablet" in b_lower or "rune" in b_lower:
            covers.append("summons")
        # Check psynergy
        if "psynergy" in b_lower or "cast " in b_lower or "learn" in b_lower:
            covers.append("psynergy")
        # Check bosses
        if "boss:" in b_lower or "hp:" in b_lower or "boss " in b_lower:
            covers.append("bosses")
        # Check monsters
        if "monster" in b_lower or "encounter" in b_lower or "battle" in b_lower:
            covers.append("monsters")
        # Check shops
        if "inn:" in b_lower or "weapons:" in b_lower or "armor:" in b_lower or "items:" in b_lower or "shop" in b_lower:
            covers.append("shops")
        # Check forging
        if "forge" in b_lower or "blacksmith" in b_lower:
            covers.append("forging")
        # Check transfer
        if "password" in b_lower or "transfer" in b_lower:
            covers.append("transfer")
        # Check characters
        if " joins" in b_lower:
            covers.append("characters")
            
        covers = sorted(list(set(covers)))
        
    # Replace in frontmatter
    # We replace the specific lines
    new_frontmatter = []
    for line in frontmatter.split('\n'):
        if line.startswith('kind:'):
            new_frontmatter.append(f"kind: {kind}")
        elif line.startswith('covers:'):
            covers_str = "[" + ", ".join(covers) + "]"
            new_frontmatter.append(f"covers: {covers_str}")
        elif line.startswith('region:'):
            if region:
                new_frontmatter.append(f'region: "{region}"')
            else:
                new_frontmatter.append(f"region: ")
        else:
            new_frontmatter.append(line)
            
    new_content = '---' + '\n'.join(new_frontmatter) + '---' + '\n' + body
    
    with open(path, 'w', encoding='utf-8', newline='\n') as file:
        file.write(new_content)
        
    print(f"{f} / {kind} / [{', '.join(covers)}] / {region}")
