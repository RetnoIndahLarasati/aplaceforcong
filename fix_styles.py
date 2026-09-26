import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(r'\.giant-bg-obj \{[^}]+\}', '.giant-bg-obj {\n    position: absolute;\n    top: 50%;\n    font-size: 20rem;\n    z-index: 0;\n    opacity: 0.3;\n    pointer-events: none;\n    filter: blur(1px);\n}', css)

css = re.sub(r'\.bright-light \{[^}]+\}', '.bright-light {\n    position: absolute;\n    left: 20px;\n    top: 50%;\n    transform: translateY(-50%);\n    width: 250px;\n    height: 250px;\n    background: radial-gradient(circle, rgba(255,255,255,1) 0%, rgba(255,255,255,0.8) 30%, rgba(129,212,250,0.4) 60%, rgba(129,212,250,0) 80%);\n    border-radius: 50%;\n    opacity: 0;\n    transition: opacity 3s ease-in;\n    pointer-events: none;\n    z-index: 5;\n    box-shadow: 0 0 80px 40px rgba(255,255,255,0.2);\n}', css)

css = re.sub(r'\.fish-group \{[^}]+\}', '.fish-group {\n    position: absolute;\n    right: 150px;\n    top: 50%;\n    transform: translateY(-50%);\n    width: 150px;\n    height: 150px;\n}', css)

css = re.sub(r'\.fish-group span \{[^}]+\}', '.fish-group span {\n    position: absolute;\n    font-size: 3.5rem;\n    animation: sway 3s ease-in-out infinite alternate;\n}', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_fish_group = '''                <div class="fish-group">
                    <span style="top: -40px; left: 40px;">🐳</span>
                    <span style="top: 0px; left: 0px;">🐙</span>
                    <span style="top: 40px; left: 30px;">🐢</span>
                    <span style="top: 80px; left: 70px;">🐬</span>
                    <span style="top: -20px; left: 90px;">🦀</span>
                    <span style="top: -60px; left: 120px;">🐡</span>
                    <span style="top: 20px; left: 100px;">🦑</span>
                    <span style="top: 60px; left: 130px;">🐠</span>
                    <span style="top: -10px; left: 150px;">🐋</span>
                    <span style="top: 30px; left: 160px;">🦐</span>
                </div>'''

html = re.sub(r'<div class="fish-group">[\s\S]*?</div>', new_fish_group, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
