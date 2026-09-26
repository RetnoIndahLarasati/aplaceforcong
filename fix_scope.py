import re

with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove them from DOMContentLoaded
pattern_remove = r"const explosionSound = new Audio\('\./explosion\.mp3'\);\nconst popSound = new Audio\('\./pop\.mp3'\);\nconst fireworkSound = new Audio\('\./firework\.mp3'\);\n"
text = re.sub(pattern_remove, "", text)

# 2. Add them to the top of the file
sounds = """
const explosionSound = new Audio('./explosion.mp3');
const popSound = new Audio('./pop.mp3');
const fireworkSound = new Audio('./firework.mp3');
"""
text = sounds + "\n" + text

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(text)
