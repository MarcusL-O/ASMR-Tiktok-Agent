from scripts.generate_prompt_image import generate_image
from scripts.generate_video import generate_video
from scripts.select_sound import get_sound_path
from scripts.sync_audio import sync_audio

object_prompt = "glass globe filled with soil"
image_path = generate_image(object_prompt)

video_path = generate_video(object_prompt, image_path)

sound_path = get_sound_path(object_prompt)

final_output = sync_audio(video_path, sound_path)
print("✅ Video klar:", final_output)
