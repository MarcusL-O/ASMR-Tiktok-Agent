from pathlib import Path

def get_sound_path(prompt):
    if "glass" in prompt:
        return "assets/sounds/glass_cut.mp3"
    elif "ice" in prompt:
        return "assets/sounds/ice_crack.mp3"
    elif "stone" in prompt or "obsidian" in prompt:
        return "assets/sounds/stone_scrape.mp3"
    else:
        return "assets/sounds/default_slicey.mp3"
