import re

# 1. Update HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'<h3 class="section-title" style="margin-top: 80px;">From This 👉 To This</h3>\s*<div class="from-to-container" id="from-to-container"></div>', '', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update Script
with open('script.js', 'r', encoding='utf-8') as f:
    script = f.read()
script = re.sub(r'// From To\s*const ftContainer = document\.getElementById\(\'from-to-container\'\);\s*if \(ftContainer && oceanData\.fromTo\) \{[\s\S]*?\}\s*// Wishes', '// Wishes', script)
with open('script.js', 'w', encoding='utf-8') as f:
    f.write(script)

# 3. Update CSS (optional, but good to clean up)
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()
css = re.sub(r'/\* ===== FROM THIS TO THIS ===== \*/[\s\S]*?(?=\@media \(max-width: 768px\))', '', css)
# Clean up media query
css = re.sub(r'\.ft-arrow \{ transform: rotate\(90deg\); animation: bounceDown 2s infinite; \}\s*@keyframes bounceDown \{\s*0%, 100% \{ transform: translateY\(0\) rotate\(90deg\); \}\s*50% \{ transform: translateY\(20px\) rotate\(90deg\); \}\s*\}', '', css)
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
