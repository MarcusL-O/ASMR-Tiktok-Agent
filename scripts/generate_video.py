import base64
from runwayml import RunwayML, TaskFailedError
from pathlib import Path
import os
from dotenv import load_dotenv
import hashlib

load_dotenv()

def generate_video(prompt, image_path):
    # ✅ Starta klienten med API-nyckel från miljövariabel (enligt dokumentation)
    client = RunwayML(api_key=os.getenv("RUNWAY_API_KEY"))

    # 🔁 Konvertera bilden till base64 (krav enligt Runway)
    with open(image_path, "rb") as f:
        base64_image = base64.b64encode(f.read()).decode("utf-8")
        data_uri = f"data:image/png;base64,{base64_image}"

    try:
        print("📤 Skickar prompt och bild till Runway...")

        task = client.image_to_video.create(
            model='gen4_turbo',
            prompt_image=data_uri,
            prompt_text=prompt,
            ratio='1280:720',
            duration=5
        ).wait_for_task_output()

        print("🧪 Fullt Runway-responsobjekt:")
        print(task)

        # ✅ Rätt attributväg
        video_url = task.output[0]
        print("✅ Video genererad:", video_url)

        # Skapa ett säkert och kort filnamn
        safe_prompt = ''.join(c for c in prompt[:40] if c.isalnum() or c == '_')
        prompt_hash = hashlib.sha1(prompt.encode()).hexdigest()[:8]
        filename = f"{safe_prompt}_{prompt_hash}.mp4"
        output_path = Path("assets/videos") / filename

        # ⬇️ Spara videon lokalt
        os.system(f"curl -L '{video_url}' -o {output_path}")
        return str(output_path)

    except TaskFailedError as e:
        print("❌ Runway misslyckades att generera videon.")
        print(e.task_details)
        return None