import os
import re
import anthropic
import json
import time

# Load env
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def read_files(directory):
    files_data = []
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".md"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
                content = f.read()
                files_data.append({'filename': filename, 'content': content})
    return files_data

def process_batch(batch):
    prompt = """You are tagging derived walkthrough chapter files for a Golden Sun: The Lost Age knowledge base.

For each file, determine the exact values for three frontmatter keys — kind, covers, region.
kind (one): prose-walkthrough | data-table | story | meta
  - boss-fight strategy in prose = prose-walkthrough (NOT data-table)
  - data-table only when the body is dominated by a table/list
  - meta = intro/version/controls/mechanics-overview/legal/FAQ/credits/contact/front, or any chapter that is just a 1-3 line header/banner

covers (list of strings): include an entity only if the chapter is somewhere you'd go to extract/learn it — it has a list/table/stat-block for it, the entity is obtained/learned here, or an encounter is described in detail. Do NOT add an entity merely name-dropped as a tactic/aside.
Vocab: [locations, monsters, bosses, items, equipment, djinn, summons, psynergy, classes, characters, shops, forging, transfer, walkthrough].
  HARD RULES:
  - meta/story chapters -> covers: [] (00-front is ALWAYS meta + covers: [])
  - a pure index/list -> covers is ONLY the one entity it lists
  - a walkthrough area -> usually [locations, walkthrough] + only the entities with real content here

region (string): the primary in-game area (free text); blank string "" for meta/story/index.

Return ONLY a JSON array of objects, one for each file, with keys "filename", "kind", "covers", "region".
"""
    
    user_content = ""
    for file in batch:
        user_content += f"--- FILE: {file['filename']} ---\n{file['content']}\n\n"
    
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=4096,
        temperature=0.0,
        system=prompt,
        messages=[
            {"role": "user", "content": user_content}
        ]
    )
    
    text = response.content[0].text
    # Extract JSON array
    try:
        start = text.find('[')
        end = text.rfind(']') + 1
        return json.loads(text[start:end])
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        print("Raw text:", text)
        return []

def main():
    directory = "raw/gs2/_chapters/autocon"
    files = read_files(directory)
    
    batch_size = 15
    results = []
    
    for i in range(0, len(files), batch_size):
        batch = files[i:i+batch_size]
        print(f"Processing batch {i} to {i+len(batch)} / {len(files)}...")
        res = process_batch(batch)
        results.extend(res)
        time.sleep(1) # rate limit

    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
