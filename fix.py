import re

with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix carrier emojis
text = re.sub(r'const carrierEmojis = \[.*?\];', 'const carrierEmojis = [\'🐡\', \'🐠\', \'🐟\', \'🦈\', \'🦀\', \'🦑\'];', text)

# Fix clam icon
text = re.sub(r'<span class="clam-icon">.*?</span>', '<span class="clam-icon">🦪</span>', text)

# Fix jelly icon
text = re.sub(r'<div class="jelly-icon">.*?</div>', '<div class="jelly-icon">🪼</div>', text)

# Fix play pause
text = re.sub(r'btnPlayPause\.textContent = ".*?";', 'btnPlayPause.textContent = "⏸";', text)
text = text.replace('audio.pause();\n            btnPlayPause.textContent = "⏸";', 'audio.pause();\n            btnPlayPause.textContent = "▶";')
text = text.replace('audio.pause();\n\n            btnPlayPause.textContent = "⏸";', 'audio.pause();\n            btnPlayPause.textContent = "▶";')

# Strip double newlines if any are left
text = re.sub(r'\n{3,}', '\n\n', text)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(text)
