from moviepy.editor import VideoFileClip, AudioFileClip
from pathlib import Path

def sync_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path).set_duration(video.duration)

    final = video.set_audio(audio)
    output_path = Path("assets/output") / Path(video_path).name
    final.write_videofile(str(output_path), codec="libx264", audio_codec="aac")
    return str(output_path)
