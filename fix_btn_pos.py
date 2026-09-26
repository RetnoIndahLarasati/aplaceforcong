import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Change right: 20px to left: 140px for .reply-btn
css = re.sub(r'\.reply-btn \{\s*position: fixed;\s*top: 20px;\s*right: 20px;', 
             r'.reply-btn {\n    position: fixed;\n    top: 20px;\n    left: 150px;', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
