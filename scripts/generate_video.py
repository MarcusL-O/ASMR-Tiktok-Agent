import requests
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
RUNWAY_API_KEY = os.getenv("RUNWAY_API_KEY")

def generate_video(prompt, image_path):
    headers = {
        "Authorization": f"Bearer {RUNWAY_API_KEY}"
    }

    files = {"input_image": open(image_path, "rb")}
    data = {
        "prompt": prompt,
        "motion": "slow",
        "num_frames": 75,
        "output_format": "mp4"
    }

    response = requests.post("https://api.runwayml.com/v2/models/gen4_turbo/generate", headers=headers, files=files, data=data)
    video_url = response.json()["video_url"]

    output_path = Path("assets/videos") / f"{prompt.replace(' ', '_')}.mp4"
    os.system(f"curl {video_url} -o {output_path}")
    return str(output_path)
