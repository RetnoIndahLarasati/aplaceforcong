import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_img = r'<img src="./foto6.jpeg" style="width: 100vw; height: 100vh; object-fit: cover; filter: contrast\(150%\) sepia\(100%\) hue-rotate\(300deg\);">'
new_img = r'<img src="./nyawit.jpeg" style="max-width: 90vw; max-height: 90vh; object-fit: contain; animation: popout 0.2s ease-out; box-shadow: 0 0 50px red; border-radius: 20px;">'

html = re.sub(old_img, new_img, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Add the popout animation to CSS
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if "keyframes popout" not in css:
    css += "\n@keyframes popout { 0% { transform: scale(0.1); opacity: 0; } 100% { transform: scale(1.2); opacity: 1; } }\n"
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)
