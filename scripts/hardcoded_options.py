import random

def random_person():
    options = [
        "A woman with elegant slow movements",
        "A tattooed hand with dark nail polish",
        "A robotic hand with metallic joints",
    ]
    return random.choice(options)

def random_knife():
    options = [
        "a Damascus steel knife",
        "a Japanese chef's knife",
        "a ceramic blade",
        "a glowing futuristic knife"
    ]
    return random.choice(options)
