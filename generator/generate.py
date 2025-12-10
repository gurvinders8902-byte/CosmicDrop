# generate.py
import os
from datetime import datetime
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

def make_drop():
    prompt = (
        "You are CosmicDrop: write a short (30-60 words) imaginative cosmic micro-poem "
        "about stars, planets, or a cosmic idea, plus a simple short image prompt "
        "for an illustration. Return JSON with 'title', 'body', 'image_prompt'."
    )
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini", # or another model you prefer
        messages=[{"role":"user","content":prompt}],
        max_tokens=250,
        temperature=0.9,
    )
    text = resp['choices'][0]['message']['content'].strip()
    return text

def write_drop(content):
    now = datetime.utcnow().strftime("%Y-%m-%d")
    out_dir = "public/drops"
    os.makedirs(out_dir, exist_ok=True)
    filename = f"{out_dir}/{now}.html"
    html = f"<html><body><article>{content}</article></body></html>"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print("Wrote", filename)

if __name__ == "__main__":
    content = make_drop()
    write_drop(content)
