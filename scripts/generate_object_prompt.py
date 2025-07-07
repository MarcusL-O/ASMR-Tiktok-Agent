import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_object_and_material():
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": (
                    "You generate realistic, safe materials. "
                    "Avoid anything dangerous, inappropriate, or not safe for work. "
                    "Respond ONLY in valid JSON like { \"object\": \"ice cube with lemon inside\", \"material\": \"ice\" }."
                )
            },
            {
                "role": "user",
                "content": "Give me one unique, safe object and its material."
            }
        ]
    )

    content = response.choices[0].message.content
    return json.loads(content)
