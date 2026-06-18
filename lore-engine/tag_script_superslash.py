import os
import re
import ast

dir_path = r'C:\Users\Nunu\Documents\Project_Genkai\lore-engine\raw\gs2\_chapters\super-slash'

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
    if num in [0, 2, 3, 15, 16, 17, 18, 19]:
        kind = 'meta'
        covers = []
        region = ''
    elif num in [1]:
        kind = 'story'
        covers = []
        region = ''
    elif num in [6, 7, 8, 9, 10, 11, 12, 13, 14]:
        kind = 'data-table'
        if num == 6: covers = ['items']
        elif num in [7, 8, 9]: covers = ['equipment']
        elif num == 10: covers = ['djinn']
        elif num == 11: covers = ['classes']
        elif num == 12: covers = ['forging']
        elif num == 13: covers = ['psynergy']
        elif num == 14: covers = ['monsters']
        region = ''
    else:
        # Walkthrough area chapter (4, 5)
        kind = 'prose-walkthrough'
        
        new_covers = ['locations', 'walkthrough']
        
        if re.search(r'\b(chest|found|got \w+|receive|give|obtained)\b', body_lower):
            new_covers.append('items')
            
        if re.search(r'(?i)(get|got|found|receive|obtain|join|acquire).*djinni?', body) or \
           re.search(r'(?i)djinni?.*(get|got|found|receive|obtain|join|acquire)', body):
            new_covers.append('djinn')
            
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
            
        if re.search(r'(?i)(summon\s*tablet|tablet|obtain.*summon)', body):
            new_covers.append('summons')
            
        if re.search(r'(?i)(boss|boss:|hp:)', body):
            new_covers.append('bosses')
            
        if re.search(r'(?i)(enemies:|monsters:|random encounters:)', body):
            new_covers.append('monsters')
            
        if re.search(r'(?i)(weapon shop|armor shop|item shop|inn\b)', body):
            new_covers.append('shops')
            
        if re.search(r'(?i)\b(forge|sunshine)\b', body):
            new_covers.append('forging')
            
        if re.search(r'(?i)\b(joins|joined)\b', body):
            new_covers.append('characters')
            
        if re.search(r'(?i)\b(sword|blade|axe|mace|staff|bow|shield|armor|robe|helm|hat|ring|boots)\b', body_lower):
            new_covers.append('equipment')
            
        if re.search(r'(?i)(transfer|password)', body_lower):
            new_covers.append('transfer')
            
        covers = new_covers
        
        if num == 4:
            region = 'Weyard'
        elif num == 5:
            region = 'Weyard'
        
    covers_str = f"[{', '.join(covers)}]"
    
    new_fm = fm
    new_fm = re.sub(r'^kind:.*$', f"kind: {kind}", new_fm, flags=re.MULTILINE)
    new_fm = re.sub(r'^covers:.*$', f"covers: {covers_str}", new_fm, flags=re.MULTILINE)
    new_fm = re.sub(r'^region:.*$', f'region: "{region}"' if region else 'region: ', new_fm, flags=re.MULTILINE)
    
    new_content = content.replace(fm, new_fm)
    
    with open(os.path.join(dir_path, filename), 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"{filename} / {kind} / {covers_str} / {region}")
