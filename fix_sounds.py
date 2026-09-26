import re

with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("https://actions.google.com/sounds/v1/weapons/explosion_large.ogg", "./explosion.mp3")
text = text.replace("https://actions.google.com/sounds/v1/foley/cork_pop.ogg", "./pop.mp3")
text = text.replace("https://actions.google.com/sounds/v1/weapons/fireworks_with_whistle.ogg", "./firework.mp3")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(text)
