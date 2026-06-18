import os
import re
import ast

dir_path = r'C:\Users\Nunu\Documents\Project_Genkai\lore-engine\raw\gs2\_chapters\cloud-blazer'

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
    
    if num in [0, 1, 2, 4, 5, 6, 7, 8, 10, 11, 89, 90, 91, 93, 94]:
        kind = 'meta'
        covers = []
        region = ''
    elif num in [3, 9]:
        kind = 'story'
        covers = []
        region = ''
        
    lines = [l for l in body.splitlines() if l.strip() and not set(l.strip()).issubset(set(' #/\\<-='))]
    if len(lines) <= 5 and num not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 89, 90, 91, 93, 94]:
        kind = 'meta'
        covers = []
        region = ''
        
    if kind == 'data-table' and 'boss' in body_lower and not re.search(r'\|\s*-\s*\|', body):
        kind = 'prose-walkthrough'
        
    if kind == 'data-table':
        if len(covers) > 1:
            if 'djinn' in title.lower(): covers = ['djinn']
            elif 'item' in title.lower(): covers = ['items']
            elif 'character' in title.lower(): covers = ['characters']
            
    if kind == 'prose-walkthrough':
        if 'locations' not in covers: covers.insert(0, 'locations')
        if 'walkthrough' not in covers: covers.append('walkthrough')
        
        if 'djinn' not in covers and re.search(r'(?i)(get|got|found|receive|obtain|join|acquire).*djinni?', body):
            covers.append('djinn')
        if 'djinn' not in covers and re.search(r'(?i)djinni?.*(get|got|found|receive|obtain|join|acquire)', body):
            covers.append('djinn')
            
        psynergy_items = ['lash pebble', 'pound cube', 'tremor bit', 'scoop gem', 'cyclone', 'burst brooch', 'sand', 'parch', 'teleport']
        for pi in psynergy_items:
            if pi in body_lower and re.search(rf'(?i)(get|got|found|receive|obtain).*{pi}', body):
                if 'psynergy' not in covers:
                    covers.append('psynergy')
                break
        if 'psynergy' not in covers and re.search(r'(?i)(get|got|found|receive|obtain|learn).*psynergy', body):
            covers.append('psynergy')

        if not region:
            region = re.sub(r'(?i)\s+revisited|\s+cave|\s+islet', '', title).strip()
            
    covers_str = f"[{', '.join(covers)}]"
    
    new_fm = fm
    new_fm = re.sub(r'^kind:.*$', f"kind: {kind}", new_fm, flags=re.MULTILINE)
    new_fm = re.sub(r'^covers:.*$', f"covers: {covers_str}", new_fm, flags=re.MULTILINE)
    new_fm = re.sub(r'^region:.*$', f'region: "{region}"' if region else 'region: ', new_fm, flags=re.MULTILINE)
    
    new_content = content.replace(fm, new_fm)
    
    with open(os.path.join(dir_path, filename), 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"{filename} / {kind} / {covers_str} / {region}")
