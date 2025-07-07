import openai
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']

    image_path = Path("assets/images") / f"{prompt.replace(' ', '_')}.png"
    os.system(f"curl {image_url} -o {image_path}")
    return str(image_path)
