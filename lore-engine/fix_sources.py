import os, json, glob, re

with open('data/gs2/intermediate/region_spine.json', 'r', encoding='utf-8') as f:
    spine = json.load(f)['spine']

spine_map = {node['id']: [ch['file'] for ch in node['chapters']] for node in spine}

for md_file in glob.glob('data/gs2/walkthrough/*.md'):
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parts = content.split('---')
    if len(parts) >= 3:
        frontmatter = parts[1]
        region_id_match = re.search(r'region_id:\s*(.+)', frontmatter)
        if region_id_match:
            region_id = region_id_match.group(1).strip()
            valid_sources = spine_map.get(region_id, [])
            
            sources_match = re.search(r'(sources:\s*\n(?:\s+- .+\n?)*)', frontmatter)
            if sources_match:
                sources_str = sources_match.group(1)
                listed_sources = []
                for line in sources_str.splitlines():
                    if line.strip().startswith('- '):
                        src = line.strip()[2:].strip()
                        if src.startswith('"') and src.endswith('"'): src = src[1:-1]
                        if src.startswith("'") and src.endswith("'"): src = src[1:-1]
                        if not src.startswith('raw/gs2/_chapters/'):
                            src = 'raw/gs2/_chapters/' + src
                        listed_sources.append(src)
                
                final_sources = [s for s in listed_sources if s in valid_sources]
                if not final_sources:
                    final_sources = valid_sources
                
                new_sources = 'sources:\n'
                for s in final_sources:
                    new_sources += f'  - {s}\n'
                
                new_frontmatter = frontmatter.replace(sources_str, new_sources)
                content = content.replace(frontmatter, new_frontmatter)
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
