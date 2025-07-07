import openai
import os
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024",
        response_format="url"
    )
    
    image_url = response['data'][0]['url']
    
    image_path = Path("assets/images") / f"{prompt.replace(' ', '_')}.png"
    
    # ✅ Använd requests istället för curl
    img_data = requests.get(image_url).content
    with open(image_path, 'wb') as f:
        f.write(img_data)

    return str(image_path)
