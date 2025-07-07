from pathlib import Path

def get_sound_path(prompt):
    if "glass" in prompt:
        return "assets/sounds/glass_cut.mp3"
    
    return "assets/sounds/default.mp3"  # Standardljud om inget matchar