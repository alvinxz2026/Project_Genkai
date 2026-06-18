import os
import re

d = r'C:\Users\Nunu\Documents\Project_Genkai\lore-engine\raw\gs2\_chapters\killerfusion'
files = sorted([f for f in os.listdir(d) if f.endswith('.md')])

for f in files:
    path = os.path.join(d, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    parts = content.split('---')
    if len(parts) < 3: continue
    
    frontmatter = parts[1]
    body = '---'.join(parts[2:]).strip()
    lines = [line for line in body.splitlines() if line.strip()]
    
    kind = ""
    covers = []
    region = ""
    
    title_match = re.search(r'title: "(.*?)"', frontmatter)
    title = title_match.group(1).strip() if title_match else ""

    # Check for header-only chapters (1-3 lines)
    if len(lines) <= 3:
        kind = "meta"
        covers = []
        region = ""
    elif f in ["00-front.md", "01-version-history.md", "02-introduction.md", "04-walkthrough.md", "57-boss-strategies.md", "63-dijnn.md", "67-item-list.md", "74-artifact.md", "82-credits.md"]:
        kind = "meta"
        covers = []
        region = ""
    elif f == "03-story.md":
        kind = "story"
        covers = []
        region = ""
    elif f == "62-characters.md":
        kind = "data-table"
        covers = ["characters"]
        region = ""
    elif f == "64-dijnn-list.md":
        kind = "data-table"
        covers = ["djinn"]
        region = ""
    elif f == "65-dijnn-locations.md":
        kind = "data-table"
        # Since it lists locations of djinn, it's a djinn guide
        covers = ["djinn"]
        region = ""
    elif f == "66-defeating-dijnns.md":
        # Strategy on defeating djinn - wait, is this mechanics/meta, or prose-walkthrough, or data-table?
        # The prompt says: "mechanics overviews (battle / djinn / menu basics) -> meta"
        # "Boss-fight strategy in prose -> prose-walkthrough"
        # Let's read defeating-dijnns later. It might be prose-walkthrough if it's boss strategy, but it's for djinn. Let's look at the body length. We'll tag it based on prose-walkthrough and [djinn].
        kind = "prose-walkthrough"
        covers = ["djinn", "walkthrough"]
        region = ""
    elif f in ["68-weapons.md", "69-armor.md", "70-shield.md", "71-gloves.md", "72-helmet.md", "73-boots.md", "75-weapons.md", "76-armor.md", "77-hands.md", "78-helm.md", "79-boots.md", "80-rings.md"]:
        kind = "data-table"
        covers = ["equipment"]
        region = ""
    elif f == "81-stats-raising-items.md":
        kind = "data-table"
        covers = ["items"]
        region = ""
    elif f in ["58-chestbeaters.md", "59-king-scorpion.md", "60-briggs.md", "61-aqua-hydra.md"]:
        # Boss-fight strategy written as prose
        kind = "prose-walkthrough"
        covers = ["bosses", "walkthrough"]
        region = ""
    else:
        # It's a walkthrough area or similar
        kind = "prose-walkthrough"
        covers = ["locations", "walkthrough"]
        region = title
        
        b_lower = body.lower()
        
        # Heuristics for covers
        if "chest" in b_lower or "found" in b_lower or "got " in b_lower or "item:" in b_lower or "potion" in b_lower or "herb" in b_lower:
            covers.append("items")
        if "weapon" in b_lower or "armor" in b_lower or "equip" in b_lower or "sword" in b_lower or "shield" in b_lower or "vest" in b_lower or "axe" in b_lower:
            covers.append("equipment")
        if "djinni" in b_lower or "dijnn" in b_lower or "djinn" in b_lower:
            covers.append("djinn")
        if "summon" in b_lower or "tablet" in b_lower or "rune" in b_lower:
            covers.append("summons")
        if "psynergy" in b_lower or "cast " in b_lower or "learn" in b_lower:
            covers.append("psynergy")
        if "boss:" in b_lower or "hp:" in b_lower or "boss " in b_lower:
            covers.append("bosses")
        if "monster" in b_lower or "encounter" in b_lower or "battle" in b_lower:
            covers.append("monsters")
        if "inn:" in b_lower or "weapons:" in b_lower or "armor:" in b_lower or "items:" in b_lower or "shop" in b_lower:
            covers.append("shops")
        if "forge" in b_lower or "blacksmith" in b_lower:
            covers.append("forging")
        if "password" in b_lower or "transfer" in b_lower:
            covers.append("transfer")
        if " joins" in b_lower:
            covers.append("characters")
            
        covers = sorted(list(set(covers)))

    # Apply in-place
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
