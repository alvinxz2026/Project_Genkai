import os
import re
import ast

dir_path = r'C:\Users\Nunu\Documents\Project_Genkai\lore-engine\raw\gs2\_chapters\shotgunnova'

def get_body(content):
    parts = content.split('---')
    if len(parts) >= 3:
        return '---'.join(parts[2:]).strip()
    return ''

for filename in sorted(os.listdir(dir_path)):
    if not filename.endswith('.md'): continue
    with open(os.path.join(dir_path, filename), 'r', encoding='utf-8') as f:
        content = f.read()
        
    fm_match = re.search(r'---(.*?)---', content, re.DOTALL)
    if not fm_match: continue
    fm = fm_match.group(1)
    
    body = get_body(content)
    body_lower = body.lower()
    
    kind_m = re.search(r'^kind:\s*(.*)$', fm, re.MULTILINE)
    covers_m = re.search(r'^covers:\s*(.*)$', fm, re.MULTILINE)
    region_m = re.search(r'^region:\s*\"?(.*?)\"?$', fm, re.MULTILINE)
    title_m = re.search(r'^title:\s*\"(.*?)\"', fm, re.MULTILINE)
    
    kind = kind_m.group(1).strip() if kind_m else 'prose-walkthrough'
    covers_str = covers_m.group(1).strip() if covers_m else '[]'
    
    try:
        covers = ast.literal_eval(covers_str)
        if not isinstance(covers, list): covers = [c.strip() for c in covers_str.strip('[]').split(',')]
    except:
        covers = [c.strip() for c in covers_str.strip('[]').split(',') if c.strip()]
        
    region = region_m.group(1).strip() if region_m else ''
    title = title_m.group(1).strip() if title_m else ''
    
    num = int(filename.split('-')[0])
    
    # Defaults based on chapter ranges
    if num in [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 65, 66, 67, 68]:
        kind = 'meta'
        covers = []
        region = ''
    elif num in [3]:
        kind = 'story'
        covers = []
        region = ''
    elif num in [59, 60, 61, 62, 63, 64]:
        kind = 'data-table'
        if num == 59: covers = ['shops']
        elif num == 60: covers = ['equipment']
        elif num == 61: covers = ['djinn']
        elif num == 62: covers = ['psynergy']
        elif num == 63: covers = ['classes']
        elif num == 64: covers = ['forging']
        region = ''
    else:
        # Walkthrough area chapter
        kind = 'prose-walkthrough'
        # Start fresh for walkthrough covers, or preserve some?
        # The audit says "severe covers inflation", so let's rebuild from scratch based on text
        # and previous if they are valid. Wait, if it has severe inflation, it's safer to clear
        # and rebuild accurately.
        new_covers = ['locations', 'walkthrough']
        
        # Check Items
        if re.search(r'\b(chest|found|got \w+|receive|give|obtained)\b', body_lower):
            new_covers.append('items')
            
        # Check Djinn
        if re.search(r'(?i)(get|got|found|receive|obtain|join|acquire).*djinni?', body) or \
           re.search(r'(?i)djinni?.*(get|got|found|receive|obtain|join|acquire)', body):
            new_covers.append('djinn')
            
        # Check Psynergy
        psynergy_items = ['lash pebble', 'pound cube', 'tremor bit', 'scoop gem', 'cyclone', 'burst brooch', 'sand', 'parch', 'teleport']
        has_psynergy = False
        for pi in psynergy_items:
            if pi in body_lower and re.search(rf'(?i)(get|got|found|receive|obtain).*{pi}', body):
                has_psynergy = True
                break
        if not has_psynergy and re.search(r'(?i)(get|got|found|receive|obtain|learn).*psynergy', body):
            has_psynergy = True
        if has_psynergy:
            new_covers.append('psynergy')
            
        # Check Summons
        if re.search(r'(?i)(summon\s*tablet|tablet|obtain.*summon)', body):
            new_covers.append('summons')
            
        # Check Bosses
        if re.search(r'(?i)(boss|boss:|hp:)', body):
            new_covers.append('bosses')
            
        # Check Monsters
        if re.search(r'(?i)(enemies:|monsters:|random encounters:)', body):
            new_covers.append('monsters')
            
        # Check Shops
        if re.search(r'(?i)(weapon shop|armor shop|item shop|inn\b)', body):
            new_covers.append('shops')
            
        # Check Forging
        if re.search(r'(?i)\b(forge|sunshine)\b', body):
            new_covers.append('forging')
            
        # Check Characters joining
        if re.search(r'(?i)\b(joins|joined)\b', body):
            new_covers.append('characters')
            
        # Check Equipment explicitly obtained
        if re.search(r'(?i)\b(sword|blade|axe|mace|staff|bow|shield|armor|robe|helm|hat|ring|boots)\b', body_lower):
            new_covers.append('equipment')
            
        # Retain transfer if it's there
        if 'transfer' in covers:
            new_covers.append('transfer')
            
        covers = new_covers
        
        # Region cleaning
        if not region:
            region = re.sub(r'(?i)\s*-\s*optional|\s+ii|\s+cave|\s+islet', '', title).strip()
            
    # Check if 1-3 line section-header-only chapter
    lines = [l for l in body.splitlines() if l.strip() and not set(l.strip()).issubset(set(' #/\\<-='))]
    if len(lines) <= 5 and num not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]:
        kind = 'meta'
        covers = []
        region = ''
        
    covers_str = f"[{', '.join(covers)}]"
    
    new_fm = fm
    new_fm = re.sub(r'^kind:.*$', f"kind: {kind}", new_fm, flags=re.MULTILINE)
    new_fm = re.sub(r'^covers:.*$', f"covers: {covers_str}", new_fm, flags=re.MULTILINE)
    new_fm = re.sub(r'^region:.*$', f'region: "{region}"' if region else 'region: ', new_fm, flags=re.MULTILINE)
    
    new_content = content.replace(fm, new_fm)
    
    with open(os.path.join(dir_path, filename), 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"{filename} / {kind} / {covers_str} / {region}")
