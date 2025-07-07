import openai
import os
import requests
from pathlib import Path
from dotenv import load_dotenv
import hashlib

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(prompt):
    print(f"🖼️ Prompt till OpenAI: {prompt}")  # Debug: visa prompten
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024",
        response_format="url"
    )
    image_url = response['data'][0]['url']

    # Skapa ett säkert och kort filnamn
    safe_prompt = ''.join(c for c in prompt[:40] if c.isalnum() or c == '_')
    prompt_hash = hashlib.sha1(prompt.encode()).hexdigest()[:8]
    filename = f"{safe_prompt}_{prompt_hash}.png"
    image_path = Path("assets/images") / filename

    img_data = requests.get(image_url).content
    with open(image_path, 'wb') as f:
        f.write(img_data)

    return str(image_path)