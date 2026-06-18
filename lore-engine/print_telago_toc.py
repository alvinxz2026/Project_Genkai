import os
import yaml

def get_frontmatter_and_body(content):
    parts = content.split("---\n", 2)
    if len(parts) >= 3:
        return parts[1], parts[2]
    return "", content

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
                fm[k] = v
        
        toc = fm.get('toc_path', '')
        print(f"{filename}: '{toc}'")

if __name__ == "__main__":
    process()
