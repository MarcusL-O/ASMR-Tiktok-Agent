from scripts.generate_prompt_image import generate_image
from scripts.generate_video import generate_video
from scripts.select_sound import get_sound_path
from scripts.sync_audio import sync_audio
from scripts.hardcoded_options import random_person, random_knife
from scripts.generate_object_prompt import generate_object_and_material

# 🔮 Generera objekt + material
generated = generate_object_and_material()
object_text = generated["object"]
material = generated["material"]

# 🎲 Slumpa person + kniv
person = random_person()
knife = random_knife()

# 🧠 Sätt ihop prompt
prompt = (
    f"{person} picks up {knife} from a wooden cutting board, "
    f"then slowly slices a {object_text}. "
    f"The background is pitch black, cinematic, high contrast, 4K, slow motion, ultra detailed, ASMR style."
)

# 🖼️ Bild + 🎥 Video + 🎧 Ljud
image_path = generate_image(prompt)
video_path = generate_video(prompt, image_path)
sound_path = get_sound_path(material)
final_output = sync_audio(video_path, sound_path)

print("✅ Video klar:", final_output)