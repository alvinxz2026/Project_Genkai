import json
import os
import re

def apply_tags():
    with open("results.json", "r", encoding="utf-8") as f:
        results = json.load(f)

    directory = "raw/gs2/_chapters/autocon"
    for r in results:
        fname = r.get('filename')
        if not fname: continue
        fpath = os.path.join(directory, fname)
        if not os.path.exists(fpath): continue
        
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        parts = content.split("---\n", 2)
        if len(parts) >= 3:
            fm = parts[1]
            body = parts[2]
            
            # YAML array format
            covers = r.get('covers', [])
            if not isinstance(covers, list):
                covers = []
            covers_str = "[" + ", ".join(covers) + "]"
            
            kind = r.get('kind', 'meta')
            region = r.get('region', '')
            
            fm = re.sub(r"^kind:.*$", f"kind: {kind}", fm, flags=re.MULTILINE)
            fm = re.sub(r"^covers:.*$", f"covers: {covers_str}", fm, flags=re.MULTILINE)
            fm = re.sub(r"^region:.*$", f"region: {region}", fm, flags=re.MULTILINE)
            
            new_content = parts[0] + "---\n" + fm + "---\n" + body
            
            with open(fpath, "w", encoding="utf-8", newline='\n') as f:
                f.write(new_content)
            
            print(f"{fname} / {kind} / {covers_str} / {region}")

if __name__ == "__main__":
    apply_tags()
