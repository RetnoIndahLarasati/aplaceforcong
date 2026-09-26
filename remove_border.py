import re

# 1. REMOVE DASHED BORDER FROM CSS
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the pseudo element for .scroll-paper::before
css = re.sub(r'\.scroll-paper::before\s*\{[^}]+\}', '', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. REMOVE PAPER-FOOTER EMOJIS FROM HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove <div class="paper-footer">🌊🐚🦀</div> or whatever emojis it has
html = re.sub(r'<div class="paper-footer">.*?</div>', '', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
